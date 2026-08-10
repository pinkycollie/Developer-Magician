#!/usr/bin/env python3
"""
ci_controller.py — CI/CD dispatch + monitoring controller for mbtq-dev.

Built for solo use right now (pmaster-dev = you), but structured so
"remote controllers" — other people or bots with their own identity —
can be added later without a redesign. See ALLOWED_CONTROLLERS below
and the NegraRosa integration point.

What this does:
    - Triggers a GitHub Actions workflow_dispatch run
    - Polls it until it finishes
    - On failure, pulls the failed job's log lines so you don't have
      to go dig through the Actions UI
    - Retries transient network/API errors with backoff; fails fast
      and clearly on real errors (bad auth, bad repo, workflow missing)

Auth: reads GITHUB_TOKEN from the environment. Never hardcode a token
here — see FOUNDATION.md's secrets rule.

Vendor note: this talks to GitHub's own API directly, no third-party
CI vendor involved, so there's nothing to bracket-placeholder here —
GitHub is already the settled choice per CLAUDE.md.
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Optional

try:
    import requests
except ImportError:
    print("This script needs the 'requests' package: pip install requests", file=sys.stderr)
    sys.exit(1)


# ----------------------------------------------------------------------
# Logging — structured, not print(). Makes this usable in CI itself later.
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("ci_controller")


# ----------------------------------------------------------------------
# Identity allowlist — the "remote controller" extension point.
#
# Right now this is just you. When a team forms, each person/bot gets
# an entry here (or, once DeafAUTH issues real PASETO tokens, this
# whole allowlist gets replaced by a call to DeafAUTH/NegraRosa to
# verify identity properly instead of a static list). Keeping it as an
# explicit, obvious function now means swapping it later is a one-function
# change, not a rewrite.
# ----------------------------------------------------------------------
ALLOWED_CONTROLLERS = {"pmaster-dev", "pinkycollie"}


def verify_controller_identity(controller_id: str) -> bool:
    """
    Confirms a controller is allowed to dispatch pipeline runs.

    TODO (future): replace this static allowlist check with a real
    call to DeafAUTH / NegraRosa once those issue verifiable identity
    tokens. The function signature is deliberately kept simple so that
    swap doesn't ripple through the rest of this file — everything
    below just calls this function, it doesn't care how the check works.
    """
    return controller_id in ALLOWED_CONTROLLERS


# ----------------------------------------------------------------------
# Errors — specific exception types instead of bare Exception, so
# callers (and you, reading a traceback at 1am) know what actually
# went wrong without re-parsing a message string.
# ----------------------------------------------------------------------
class CIControllerError(Exception):
    """Base error for anything this script raises on purpose."""


class AuthError(CIControllerError):
    """GITHUB_TOKEN missing, invalid, or lacking the right scope."""


class WorkflowNotFoundError(CIControllerError):
    """The named workflow file doesn't exist on the target repo/branch."""


class WorkflowTimeoutError(CIControllerError):
    """The run didn't finish within the allowed wait time."""


class TransientAPIError(CIControllerError):
    """A likely-temporary failure (5xx, network blip) — safe to retry."""


# ----------------------------------------------------------------------
# Config — no hardcoded owner/repo names beyond what's already settled
# (GitHub itself, per CLAUDE.md). Everything else comes from env vars
# or CLI args so this script works for any repo without editing code.
# ----------------------------------------------------------------------
@dataclass
class Config:
    token: str
    owner: str
    repo: str
    workflow_file: str
    ref: str = "main"
    poll_interval_seconds: int = 15
    timeout_seconds: int = 1800  # 30 min ceiling before giving up
    max_retries: int = 4

    @classmethod
    def from_env_and_args(cls, args: argparse.Namespace) -> "Config":
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise AuthError(
                "GITHUB_TOKEN is not set. Export it before running this script — "
                "never pass a token as a CLI argument, it ends up in shell history."
            )
        return cls(
            token=token,
            owner=args.owner,
            repo=args.repo,
            workflow_file=args.workflow,
            ref=args.ref,
        )


# ----------------------------------------------------------------------
# Retry helper — exponential backoff for transient errors only.
# Real errors (bad auth, 404) fail immediately instead of retrying
# something that will never succeed.
# ----------------------------------------------------------------------
def with_retries(fn, *, max_retries: int, base_delay: float = 2.0):
    attempt = 0
    while True:
        try:
            return fn()
        except TransientAPIError as e:
            attempt += 1
            if attempt > max_retries:
                log.error("Giving up after %d attempts: %s", attempt, e)
                raise
            delay = base_delay * (2 ** (attempt - 1))
            log.warning("Transient error (attempt %d/%d): %s — retrying in %.0fs",
                        attempt, max_retries, e, delay)
            time.sleep(delay)


# ----------------------------------------------------------------------
# GitHub API wrapper — narrow surface, just what this script needs.
# ----------------------------------------------------------------------
class GitHubDispatcher:
    API_BASE = "https://api.github.com"

    def __init__(self, config: Config):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {config.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        })

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.API_BASE}{path}"
        try:
            resp = self.session.request(method, url, timeout=30, **kwargs)
        except requests.exceptions.RequestException as e:
            raise TransientAPIError(f"Network error calling {url}: {e}") from e

        if resp.status_code == 401:
            raise AuthError("GITHUB_TOKEN was rejected — check it's valid and has 'workflow' scope.")
        if resp.status_code == 404:
            raise WorkflowNotFoundError(
                f"404 from {url} — check owner/repo/workflow filename are correct."
            )
        if resp.status_code >= 500:
            raise TransientAPIError(f"{resp.status_code} from {url}")
        if resp.status_code >= 400:
            raise CIControllerError(f"{resp.status_code} from {url}: {resp.text[:300]}")

        return resp

    def trigger_workflow(self) -> None:
        path = (f"/repos/{self.config.owner}/{self.config.repo}"
                f"/actions/workflows/{self.config.workflow_file}/dispatches")
        with_retries(
            lambda: self._request("POST", path, json={"ref": self.config.ref}),
            max_retries=self.config.max_retries,
        )
        log.info("Dispatched workflow '%s' on %s/%s@%s",
                  self.config.workflow_file, self.config.owner, self.config.repo, self.config.ref)

    def get_latest_run(self) -> dict:
        path = (f"/repos/{self.config.owner}/{self.config.repo}"
                f"/actions/workflows/{self.config.workflow_file}/runs")
        resp = with_retries(
            lambda: self._request("GET", path, params={"branch": self.config.ref, "per_page": 1}),
            max_retries=self.config.max_retries,
        )
        runs = resp.json().get("workflow_runs", [])
        if not runs:
            raise WorkflowNotFoundError("No runs found yet — the dispatch may not have registered.")
        return runs[0]

    def get_failed_job_logs(self, run_id: int) -> str:
        path = f"/repos/{self.config.owner}/{self.config.repo}/actions/runs/{run_id}/jobs"
        resp = with_retries(
            lambda: self._request("GET", path),
            max_retries=self.config.max_retries,
        )
        jobs = resp.json().get("jobs", [])
        failed = [j for j in jobs if j.get("conclusion") == "failure"]
        if not failed:
            return "(no failed job found — check the Actions UI directly)"

        summary_lines = []
        for job in failed:
            summary_lines.append(f"Failed job: {job['name']}")
            for step in job.get("steps", []):
                if step.get("conclusion") == "failure":
                    summary_lines.append(f"  -> failed step: {step['name']}")
        return "\n".join(summary_lines)


# ----------------------------------------------------------------------
# Orchestration — the part you actually call.
# ----------------------------------------------------------------------
def dispatch_and_watch(config: Config, controller_id: str) -> int:
    """
    Triggers the pipeline and waits for it to finish.
    Returns 0 on success, 1 on failure, raises on anything unexpected.
    """
    if not verify_controller_identity(controller_id):
        log.error("'%s' is not an authorized controller. Allowed: %s",
                   controller_id, ", ".join(sorted(ALLOWED_CONTROLLERS)))
        return 1

    gh = GitHubDispatcher(config)

    try:
        gh.trigger_workflow()
    except AuthError as e:
        log.error("Auth problem, stopping: %s", e)
        return 1
    except WorkflowNotFoundError as e:
        log.error("Workflow not found, stopping: %s", e)
        return 1

    # Give GitHub a moment to register the dispatch before polling for it.
    time.sleep(5)

    start = time.time()
    last_status = None
    while True:
        elapsed = time.time() - start
        if elapsed > config.timeout_seconds:
            raise WorkflowTimeoutError(
                f"Run did not finish within {config.timeout_seconds}s — check the Actions UI, "
                f"this may mean a hung job rather than a real failure."
            )

        run = gh.get_latest_run()
        status = run["status"]        # queued / in_progress / completed
        conclusion = run.get("conclusion")  # success / failure / None

        if status != last_status:
            log.info("Run status: %s", status)
            last_status = status

        if status == "completed":
            if conclusion == "success":
                log.info("Pipeline succeeded.")
                return 0
            else:
                log.error("Pipeline finished with conclusion: %s", conclusion)
                logs = gh.get_failed_job_logs(run["id"])
                log.error("Failure summary:\n%s", logs)
                return 1

        time.sleep(config.poll_interval_seconds)


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------
def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Dispatch and watch a GitHub Actions pipeline.")
    p.add_argument("--owner", default="pinkycollie", help="GitHub owner/org (default: pinkycollie)")
    p.add_argument("--repo", required=True, help="Repo name, e.g. vr4deaf")
    p.add_argument("--workflow", default="pipeline-devsecops.yml", help="Workflow filename")
    p.add_argument("--ref", default="main", help="Branch or ref to run against")
    p.add_argument("--controller-id", default="pmaster-dev",
                    help="Identity triggering this run (checked against the allowlist)")
    return p


def main() -> int:
    args = build_arg_parser().parse_args()
    try:
        config = Config.from_env_and_args(args)
    except AuthError as e:
        log.error(str(e))
        return 1

    try:
        return dispatch_and_watch(config, args.controller_id)
    except CIControllerError as e:
        log.error("Stopping: %s", e)
        return 1
    except KeyboardInterrupt:
        log.warning("Interrupted by user — the pipeline run itself is still going on GitHub's side.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
