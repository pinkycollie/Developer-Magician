from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(
    title="Developer Magician API",
    description="Deaf-First Accessibility Automation with Educational Storytelling Workflows",
    version="2.0.0",
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# MODELS - Data structures for storytelling and educational workflows
# ============================================================================

class WorkflowStage(str, Enum):
    """CI/CD workflow stages for educational tracking"""
    CHECKOUT = "checkout"
    SETUP = "setup"
    LINT = "lint"
    TEST = "test"
    BUILD = "build"
    DEPLOY = "deploy"
    VALIDATE = "validate"

class StageStatus(str, Enum):
    """Status of a workflow stage"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"

class EducationalMessage(BaseModel):
    """Educational feedback message with storytelling context"""
    title: str
    message: str
    learning_points: List[str]
    tips: Optional[List[str]] = []
    resources: Optional[List[str]] = []

class WorkflowStageInfo(BaseModel):
    """Information about a CI/CD workflow stage"""
    stage: WorkflowStage
    status: StageStatus
    description: str
    educational_content: EducationalMessage
    timestamp: Optional[str] = None

class StorytellingWorkflow(BaseModel):
    """Complete workflow with storytelling pathway"""
    workflow_name: str
    description: str
    stages: List[WorkflowStageInfo]
    current_stage: Optional[WorkflowStage] = None
    overall_progress: int = 0

# ============================================================================
# ORIGINAL ENDPOINTS - Keeping backward compatibility
# ============================================================================

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    """Original hello endpoint - kept for backward compatibility"""
    return {"message": "Hello from FastAPI"}

# ============================================================================
# HEALTH & STATUS ENDPOINTS
# ============================================================================

@app.get("/api/py/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "accessibility-validator",
        "version": "2.0.0",
        "api_type": "developer-magician",
        "features": [
            "storytelling-workflows",
            "educational-pathways",
            "ci-cd-learning",
            "accessibility-validation"
        ]
    }

@app.get("/api/py/ecosystem-status")
async def ecosystem_status():
    """Check MBTQ ecosystem integration health"""
    return {
        "pinksync": "healthy",
        "deafauth": "available",
        "fibonrose": "available",
        "magicians": "active",
        "dao": "governed",
        "educational_mode": True,
        "storytelling_enabled": True
    }

# ============================================================================
# STORYTELLING WORKFLOW ENDPOINTS
# ============================================================================

@app.get("/api/py/workflows/ci-cd-story")
async def get_cicd_story() -> StorytellingWorkflow:
    """
    Get the complete CI/CD workflow as an educational storytelling pathway.
    
    This endpoint provides a narrative structure for understanding CI/CD,
    with each stage explained in accessible, educational language.
    """
    stages = [
        WorkflowStageInfo(
            stage=WorkflowStage.CHECKOUT,
            status=StageStatus.SUCCESS,
            description="Repository checkout - Getting your code ready",
            educational_content=EducationalMessage(
                title="🎯 Stage 1: Repository Checkout",
                message="This is where the magic begins! We clone your code from GitHub into a clean, isolated environment.",
                learning_points=[
                    "Every CI/CD run starts with a fresh copy of your code",
                    "This ensures consistency - no 'works on my machine' problems",
                    "Isolation prevents conflicts between different builds"
                ],
                tips=[
                    "Think of this like getting a new notebook for each assignment",
                    "Clean slate = reliable results"
                ],
                resources=[
                    "GitHub Actions Checkout: https://github.com/actions/checkout"
                ]
            )
        ),
        WorkflowStageInfo(
            stage=WorkflowStage.SETUP,
            status=StageStatus.SUCCESS,
            description="Environment setup - Installing dependencies",
            educational_content=EducationalMessage(
                title="📦 Stage 2: Environment Setup",
                message="Setting up Node.js, Python, and installing all the packages your project needs.",
                learning_points=[
                    "Dependencies are like ingredients for a recipe",
                    "We use package managers (npm, pip) to install them",
                    "Caching speeds up subsequent runs"
                ],
                tips=[
                    "Use npm ci instead of npm install in CI for faster, reliable installs",
                    "Pin dependency versions for reproducible builds"
                ]
            )
        ),
        WorkflowStageInfo(
            stage=WorkflowStage.LINT,
            status=StageStatus.SUCCESS,
            description="Code quality checks - Linting and formatting",
            educational_content=EducationalMessage(
                title="🔍 Stage 3: Code Quality Checks",
                message="Automated code analysis to catch errors and enforce consistent style.",
                learning_points=[
                    "Linters find bugs before they become problems",
                    "Consistent code style makes collaboration easier",
                    "Catches common mistakes automatically"
                ],
                tips=[
                    "Fix linting issues locally: npm run lint",
                    "Use editor plugins for real-time feedback"
                ]
            )
        ),
        WorkflowStageInfo(
            stage=WorkflowStage.TEST,
            status=StageStatus.SUCCESS,
            description="Running tests - Validating functionality",
            educational_content=EducationalMessage(
                title="🧪 Stage 4: Testing",
                message="Run automated tests to ensure your code works as expected.",
                learning_points=[
                    "Tests are your safety net",
                    "They verify features work correctly",
                    "Catch regressions before users do"
                ],
                tips=[
                    "Write tests as you code, not after",
                    "Good tests document how your code should behave"
                ]
            )
        ),
        WorkflowStageInfo(
            stage=WorkflowStage.BUILD,
            status=StageStatus.SKIPPED,
            description="Production build - Optimizing for deployment",
            educational_content=EducationalMessage(
                title="🏗️ Stage 5: Build (Lightweight Mode)",
                message="In lightweight CI, we skip the full build to save time and resources.",
                learning_points=[
                    "Full builds happen during deployment",
                    "This approach focuses on code quality first",
                    "Saves compute resources and time"
                ],
                tips=[
                    "Build validation happens in the deploy workflow",
                    "Lightweight CI is great for rapid feedback"
                ]
            )
        ),
        WorkflowStageInfo(
            stage=WorkflowStage.DEPLOY,
            status=StageStatus.PENDING,
            description="Deployment - Publishing to production",
            educational_content=EducationalMessage(
                title="🚀 Stage 6: Manual Deployment",
                message="Deployment is manual - YOU control when your code goes live!",
                learning_points=[
                    "Manual deployment puts you in control",
                    "Review changes before publishing",
                    "Educational: Learn deployment deliberately"
                ],
                tips=[
                    "Go to Actions → Deploy to Vercel → Run workflow",
                    "Choose production or preview environment"
                ]
            )
        )
    ]
    
    return StorytellingWorkflow(
        workflow_name="CI/CD Learning Journey",
        description="An educational pathway through continuous integration and deployment",
        stages=stages,
        current_stage=WorkflowStage.DEPLOY,
        overall_progress=75
    )

@app.get("/api/py/workflows/security-story")
async def get_security_story() -> Dict[str, Any]:
    """
    Get the security workflow as an educational story.
    
    Learn about security best practices through a narrative structure.
    """
    return {
        "workflow_name": "Security Learning Journey",
        "description": "Understanding security through automated scanning",
        "chapters": [
            {
                "chapter": 1,
                "title": "Why Security Matters",
                "content": "Security isn't just about preventing attacks - it's about protecting users and building trust.",
                "learning_points": [
                    "Vulnerabilities can exist in your dependencies",
                    "Regular scanning catches issues early",
                    "Prevention is cheaper than remediation"
                ]
            },
            {
                "chapter": 2,
                "title": "Dependency Scanning",
                "content": "Your code relies on libraries (npm, pip packages). These can have security vulnerabilities.",
                "tools": ["npm audit", "pip-audit"],
                "learning_points": [
                    "Check for known CVEs in dependencies",
                    "Update packages regularly",
                    "Review security advisories"
                ]
            },
            {
                "chapter": 3,
                "title": "Code Analysis",
                "content": "Static analysis finds security issues in your own code.",
                "tools": ["ESLint security plugins", "CodeQL"],
                "learning_points": [
                    "Prevent SQL injection",
                    "Avoid XSS vulnerabilities",
                    "Secure data handling"
                ]
            }
        ],
        "best_practices": [
            "Run security scans on every push",
            "Enable GitHub Dependabot alerts",
            "Respond quickly to critical issues",
            "Keep learning about security patterns"
        ]
    }

@app.get("/api/py/workflows/deployment-story")
async def get_deployment_story() -> Dict[str, Any]:
    """
    Get the deployment workflow story with manual control narrative.
    
    Learn why manual deployment empowers developers.
    """
    return {
        "workflow_name": "Manual Deployment Mastery",
        "description": "Learn deployment by doing it deliberately",
        "philosophy": {
            "why_manual": [
                "Full control over deployment timing",
                "Review changes before going live",
                "Educational: understand each step",
                "Prevents accidental deploys"
            ],
            "when_to_deploy": [
                "After code review approval",
                "When tests are passing",
                "During scheduled maintenance windows",
                "When you're ready to support it"
            ]
        },
        "deployment_stages": [
            {
                "stage": "Pre-deployment Check",
                "description": "Verify everything is ready",
                "checklist": [
                    "All tests passing",
                    "Code reviewed and approved",
                    "Dependencies updated",
                    "Documentation current"
                ]
            },
            {
                "stage": "Build & Package",
                "description": "Create optimized production build",
                "what_happens": [
                    "Compile TypeScript to JavaScript",
                    "Bundle and minify assets",
                    "Generate static pages",
                    "Package serverless functions"
                ]
            },
            {
                "stage": "Deploy to Vercel",
                "description": "Publish to production",
                "what_happens": [
                    "Upload build artifacts",
                    "Deploy to CDN",
                    "Configure routing",
                    "Run health checks"
                ]
            },
            {
                "stage": "Post-deployment",
                "description": "Verify and monitor",
                "checklist": [
                    "Check deployment URL",
                    "Test critical paths",
                    "Monitor error rates",
                    "Notify team"
                ]
            }
        ],
        "pro_tips": [
            "Use preview deployments for testing",
            "Deploy during low-traffic periods",
            "Have a rollback plan ready",
            "Monitor logs after deployment"
        ]
    }

# ============================================================================
# EDUCATIONAL PATHWAY ENDPOINTS
# ============================================================================

@app.get("/api/py/learn/ci-cd-basics")
async def learn_cicd_basics() -> Dict[str, Any]:
    """
    Educational endpoint: Learn CI/CD fundamentals through examples.
    """
    return {
        "title": "CI/CD Basics - A Beginner's Guide",
        "introduction": "CI/CD stands for Continuous Integration and Continuous Deployment. It's about automating the process of testing and deploying your code.",
        "key_concepts": [
            {
                "concept": "Continuous Integration (CI)",
                "explanation": "Automatically test code every time someone pushes changes",
                "benefits": [
                    "Catch bugs early",
                    "Ensure code quality",
                    "Enable team collaboration"
                ],
                "example": "Every push to GitHub triggers linting and tests"
            },
            {
                "concept": "Continuous Deployment (CD)",
                "explanation": "Automatically deploy code after it passes tests",
                "benefits": [
                    "Faster time to market",
                    "Reduced manual errors",
                    "Consistent deployments"
                ],
                "example": "Manual deployment via workflow_dispatch in this repo"
            }
        ],
        "your_journey": [
            "✅ Step 1: Understanding version control (Git)",
            "✅ Step 2: Writing automated tests",
            "✅ Step 3: Setting up CI workflows (You are here!)",
            "🎯 Step 4: Implementing CD pipelines",
            "🚀 Step 5: Monitoring and optimization"
        ],
        "next_steps": [
            "Explore the CI workflow in .github/workflows/ci.yml",
            "Try triggering the manual deployment workflow",
            "Review the logs to understand each step",
            "Experiment with making changes and watching CI run"
        ]
    }

@app.get("/api/py/learn/workflow-stages/{stage}")
async def learn_workflow_stage(stage: WorkflowStage) -> Dict[str, Any]:
    """
    Deep dive into a specific workflow stage.
    
    Provides detailed educational content about a particular CI/CD stage.
    """
    stage_info = {
        WorkflowStage.CHECKOUT: {
            "title": "Repository Checkout",
            "what_it_does": "Clones your code from GitHub into the CI environment",
            "why_important": "Ensures every build starts from a known, clean state",
            "common_issues": [
                "Submodules not checked out (use: with: submodules: true)",
                "Large repos timing out (use: fetch-depth for shallow clone)"
            ],
            "best_practices": [
                "Always use the latest version of actions/checkout",
                "Consider fetch-depth: 0 for full history when needed",
                "Use LFS for large binary files"
            ]
        },
        WorkflowStage.LINT: {
            "title": "Code Linting",
            "what_it_does": "Analyzes code for errors and style issues",
            "why_important": "Catches bugs early and enforces consistent style",
            "tools": ["ESLint for JavaScript/TypeScript", "Prettier for formatting"],
            "common_issues": [
                "ESLint configuration conflicts",
                "Too strict rules blocking development",
                "Formatting inconsistencies"
            ],
            "best_practices": [
                "Configure ESLint in .eslintrc.json",
                "Use extends for shared configs",
                "Fix issues locally before pushing"
            ]
        },
        WorkflowStage.DEPLOY: {
            "title": "Deployment",
            "what_it_does": "Publishes your application to production servers",
            "why_important": "Makes your code available to users",
            "platforms": [options]
            "common_issues": [
                "Missing environment variables",
                "Build timeouts",
                "Incorrect routing configuration"
            ],
            "best_practices": [
                "Use staging environments first",
                "Test deployments in preview mode",
                "Have rollback procedures ready",
                "Monitor post-deployment metrics"
            ]
        }
    }
    
    if stage not in stage_info:
        return {
            "title": stage.value.title(),
            "message": "Detailed information for this stage is coming soon!",
            "general_info": "This stage is part of the CI/CD pipeline."
        }
    
    return stage_info[stage]

@app.get("/api/py/learn/mbtq-ecosystem")
async def learn_mbtq_ecosystem() -> Dict[str, Any]:
    """
    Educational content about the MBTQ ecosystem and its services.
    """
    return {
        "title": "Understanding the MBTQ Ecosystem",
        "overview": "MBTQ is a network of interconnected services designed to empower the Deaf community through accessible, AI-powered tools.",
        "services": [
            {
                "name": "PinkSync (This Service!)",
                "icon": "💜",
                "role": "Accessibility Validator",
                "description": "Ensures all interfaces prioritize ASL flow and visual-first design",
                "key_features": [
                    "Deaf-first accessibility validation",
                    "ASL navigation compatibility checks",
                    "Audio-bypass requirement verification"
                ]
            },
            {
                "name": "DeafAUTH",
                "icon": "🔐",
                "role": "Identity & Authentication",
                "description": "ASL-first authentication flows for Deaf users",
                "key_features": [
                    "Visual authentication methods",
                    "ASL video verification",
                    "Deaf-friendly identity management"
                ]
            },
            {
                "name": "Fibonrose",
                "icon": "📊",
                "role": "Trust & Reputation",
                "description": "Logs accessibility scores and builds community trust",
                "key_features": [
                    "Service quality tracking",
                    "Accessibility score history",
                    "Community reputation system"
                ]
            },
            {
                "name": "360Magicians",
                "icon": "🤖",
                "role": "AI Automation",
                "description": "Developer magicians that automate tasks intelligently",
                "key_features": [
                    "AI-powered code generation",
                    "Intelligent task orchestration",
                    "Self-improving systems"
                ]
            },
            {
                "name": "DAO Governance",
                "icon": "🏛️",
                "role": "Community Control",
                "description": "Democratic decision-making for ecosystem standards",
                "key_features": [
                    "Community voting on standards",
                    "Transparent governance",
                    "Inclusive decision-making"
                ]
            }
        ],
        "integration_benefits": [
            "Services work better together",
            "Shared authentication via DeafAUTH",
            "Trust scores across the ecosystem",
            "AI agents that understand your needs"
        ],
        "getting_started": {
            "step_1": "Start with one service (like PinkSync)",
            "step_2": "Learn its API and capabilities",
            "step_3": "Integrate other services as needed",
            "step_4": "Participate in DAO governance"
        },
        "resources": [
            "Main site: mbtquniverse.com",
            "Documentation: docs.mbtquniverse.com",
            "Community: community.mbtquniverse.com"
        ]
    }

# ============================================================================
# TOAST NOTIFICATION ENDPOINTS (For workflow feedback)
# ============================================================================

@app.post("/api/py/toast/workflow-feedback")
async def create_workflow_toast(
    stage: WorkflowStage,
    status: StageStatus,
    custom_message: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate educational toast notification for workflow stages.
    
    Used by GitHub Actions to create user-friendly feedback messages.
    """
    toast_templates = {
        (WorkflowStage.CHECKOUT, StageStatus.SUCCESS): {
            "emoji": "✅",
            "title": "Code Retrieved Successfully!",
            "message": custom_message or "Your repository is ready for testing.",
            "tip": "This fresh copy ensures reproducible builds."
        },
        (WorkflowStage.LINT, StageStatus.FAILED): {
            "emoji": "⚠️",
            "title": "Code Quality Issues Found",
            "message": custom_message or "Linting found some issues that need attention.",
            "tip": "Run 'npm run lint' locally to see and fix issues.",
            "action": "Review the logs above for specific problems."
        },
        (WorkflowStage.DEPLOY, StageStatus.SUCCESS): {
            "emoji": "🎉",
            "title": "Deployment Successful!",
            "message": custom_message or "Your application is now live!",
            "tip": "Check your Vercel dashboard for the deployment URL."
        }
    }
    
    key = (stage, status)
    toast = toast_templates.get(key, {
        "emoji": "ℹ️",
        "title": f"{stage.value.title()} - {status.value.title()}",
        "message": custom_message or "Workflow stage completed.",
        "tip": "Check the workflow logs for details."
    })
    
    return {
        "toast": toast,
        "timestamp": datetime.utcnow().isoformat(),
        "stage": stage.value,
        "status": status.value
    }

# ============================================================================
# ROOT ENDPOINT
# ============================================================================

@app.get("/api/py")
async def root():
    """Root API endpoint with navigation"""
    return {
        "message": "Welcome to the Developer Magician API!",
        "version": "2.0.0",
        "features": [
            "Storytelling Workflows",
            "Educational Pathways",
            "CI/CD Learning",
            "MBTQ Ecosystem Integration"
        ],
        "endpoints": {
            "health": "/api/py/health",
            "docs": "/api/py/docs",
            "workflows": {
                "ci_cd_story": "/api/py/workflows/ci-cd-story",
                "security_story": "/api/py/workflows/security-story",
                "deployment_story": "/api/py/workflows/deployment-story"
            },
            "learning": {
                "ci_cd_basics": "/api/py/learn/ci-cd-basics",
                "workflow_stage": "/api/py/learn/workflow-stages/{stage}",
                "mbtq_ecosystem": "/api/py/learn/mbtq-ecosystem"
            }
        },
        "deaf_first": True,
        "accessibility": "priority"
    }