# Accessibility-Validator - PinkSync Accessibility Project Management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/pinkycollie/Developer-Magician)
[![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://www.python.org/)
[![Auto-fix Code Issues](https://github.com/pinkycollie/Developer-Magician/actions/workflows/auto-fix.yml/badge.svg)](https://github.com/pinkycollie/Developer-Magician/actions/workflows/auto-fix.yml)

**Part of the MBTQ Ecosystem - Deaf-First Accessibility Automation**

The Developer-Magician is a core service within PinkSync that ensures all interfaces prioritize ASL flow and bypass audio-only UX. This service validates websites and applications for Deaf-first accessibility, going beyond standard WCAG compliance to focus on visual UI and sign language navigation patterns.

## 🎯 Purpose in AI Ecosystem

- **PinkSync Role**: Acts as the “nervous system” executor for accessibility validation
- **DeafAUTH Integration**: Validates identity flows work for Deaf users
- **Fibonrose Logging**: Reports accessibility scores to trust/reputation system
- **360Magicians Compatible**: AI agents can trigger validation tasks
- **DAO Governed**: Validation standards controlled by open source governance

## 🚀 Quick Deploy

### One-Click Vercel Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/pinkycollie/Developer-Magician)

### Manual Setup

```bash
# Clone and setup
git clone https://github.com/pinkycollie/Developer-Magician.git
cd Developer-Magician

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
npm install
pip install -r requirements.txt

# Run development server
npm run dev
```

Open <http://localhost:3000> to see the validator interface.
FastAPI server runs on <http://127.0.0.1:8000>

## 🏗️ Architecture

### Frontend (Next.js 14)

- **Validation Dashboard**: Real-time accessibility scanning interface
- **Visual Report Generator**: Deaf-first accessibility scores and recommendations
- **URL Input Interface**: Analyze live websites or upload designs
- **Integration Panel**: Connect to MBTQ ecosystem components

### Backend (FastAPI)

- **Web Scraping Engine**: Analyze live websites for accessibility issues
- **ASL Flow Validator**: Check if interfaces support sign language navigation
- **Audio-Bypass Detector**: Identify audio-only elements needing visual alternatives
- **Deaf-First Scoring**: Custom algorithms beyond standard WCAG

## 🤖 CI/CD Workflows (Educational & Lightweight)

This repository features **educational CI/CD workflows** that teach you about continuous integration and deployment while keeping operations lightweight and transparent.

📖 **[Complete Workflow Usage Guide →](docs/WORKFLOW_GUIDE.md)**

### 🎓 Workflow Philosophy

- **Storytelling Approach**: Each workflow step includes educational "toast notifications" explaining what's happening and why
- **Manual Control**: Deployment is manual via `workflow_dispatch` - YOU decide when to deploy
- **Lightweight Operations**: Focus on validation, skip heavy builds in CI
- **Transparency**: Clear feedback about missing secrets or skipped steps
- **Learning-First**: Designed to teach CI/CD concepts through practical examples

### 📋 Available Workflows

#### 1. 🎓 CI - Continuous Integration (Educational Path)

**File**: `.github/workflows/ci.yml`  
**Triggers**: Push to main/develop, Pull Requests  

**What it does**:
- ✅ Repository checkout with educational explanations
- ✅ Node.js and Python environment setup
- ✅ Dependency installation (npm ci, pip)
- ✅ Code linting with ESLint
- ✅ Python syntax validation
- ✅ Build validation (lightweight mode)

**Educational Features**:
- Toast notifications explaining each step
- Learning checkpoints at every stage
- Tips on fixing common issues
- No failures, only guidance

**Run locally**:
```bash
npm ci
npm run lint
python -m py_compile api/index.py
```

#### 2. 🚀 Deploy to Vercel (Manual)

**File**: `.github/workflows/deploy-vercel.yml`  
**Trigger**: Manual via `workflow_dispatch`

**How to deploy**:
1. Go to **Actions** tab in GitHub
2. Select **"Deploy to Vercel (Manual)"**
3. Click **"Run workflow"**
4. Choose environment (production/preview)
5. Optionally add a deployment reason

**What it does**:
- 🔍 Pre-deployment validation
- 🔐 Verifies Vercel secrets are configured
- 🚀 Deploys to Vercel (if secrets present)
- 📊 Provides educational feedback throughout

**Required Secrets** (Optional):
- `VERCEL_TOKEN` - Your Vercel authentication token
- `VERCEL_ORG_ID` - Your Vercel organization ID
- `VERCEL_PROJECT_ID` - Your Vercel project ID

**Without secrets**: Workflow runs successfully, provides setup instructions, skips deployment gracefully.

#### 3. 🔒 Security Checks (Educational)

**File**: `.github/workflows/security.yml`  
**Triggers**: Push, Pull Request, Weekly Schedule (Mondays 2 AM UTC), Manual

**What it does**:
- 🔍 NPM security audit (moderate+ severity)
- 🐍 Python package vulnerability scan
- 🔬 Optional deep code analysis
- 📊 Educational security summary

**Run locally**:
```bash
npm audit --audit-level=moderate
pip install pip-audit && pip-audit -r requirements.txt
```

#### 4. 🌐 MBTQ Ecosystem Sync (Educational)

**File**: `.github/workflows/ecosystem-sync.yml`  
**Triggers**: Push to main, Manual via `workflow_dispatch`

**What it does**:
- 🔐 Checks for ecosystem integration secrets
- 🔗 Syncs with DeafAUTH (if configured)
- 📊 Updates Fibonrose registry (if configured)
- 🤖 Notifies 360Magicians (if configured)
- 📚 Educational content about distributed systems

**Optional Secrets** (for ecosystem integration):
- `DEAFAUTH_API_KEY` & `DEAFAUTH_WEBHOOK_URL`
- `FIBONROSE_API_KEY` & `FIBONROSE_ENDPOINT`
- `MAGICIAN_API_KEY` & `MAGICIAN_DISPATCHER_URL`

**Without secrets**: Workflow provides educational content about each service, continues successfully.

### 💡 CI/CD Best Practices in This Repo

1. **Educational First**: Learn by doing, with explanations at every step
2. **Fail Gracefully**: Missing secrets don't cause failures, they provide guidance
3. **Manual Control**: You control when code goes live
4. **Lightweight CI**: Fast feedback, skip heavy operations
5. **Transparent**: Clear visibility into what's happening and why

## 🔧 Developer Magician API

The Developer Magician API extends the FastAPI backend with storytelling workflows and educational endpoints.

**API Documentation**: <http://localhost:8000/api/py/docs> (when running locally)

### Storytelling Workflow Endpoints

These endpoints provide narrative structures for understanding CI/CD concepts:

- `GET /api/py/workflows/ci-cd-story` - Complete CI/CD workflow as educational journey
- `GET /api/py/workflows/security-story` - Security learning pathway
- `GET /api/py/workflows/deployment-story` - Manual deployment mastery guide

**Example Response** (`/api/py/workflows/ci-cd-story`):
```json
{
  "workflow_name": "CI/CD Learning Journey",
  "description": "An educational pathway through continuous integration and deployment",
  "stages": [
    {
      "stage": "checkout",
      "status": "success",
      "description": "Repository checkout - Getting your code ready",
      "educational_content": {
        "title": "🎯 Stage 1: Repository Checkout",
        "message": "This is where the magic begins!...",
        "learning_points": [...],
        "tips": [...],
        "resources": [...]
      }
    }
  ],
  "current_stage": "deploy",
  "overall_progress": 75
}
```

### Educational Pathway Endpoints

Learn CI/CD concepts through interactive documentation:

- `GET /api/py/learn/ci-cd-basics` - Fundamentals of continuous integration/deployment
- `GET /api/py/learn/workflow-stages/{stage}` - Deep dive into specific stages
- `GET /api/py/learn/mbtq-ecosystem` - Understanding the MBTQ ecosystem

**Example Usage**:
```bash
# Learn CI/CD basics
curl http://localhost:8000/api/py/learn/ci-cd-basics

# Deep dive into deployment stage
curl http://localhost:8000/api/py/learn/workflow-stages/deploy

# Understand MBTQ ecosystem
curl http://localhost:8000/api/py/learn/mbtq-ecosystem
```

### Toast Notification Endpoint

Generate educational feedback for workflow stages:

- `POST /api/py/toast/workflow-feedback` - Create educational toast messages

**Parameters**:
- `stage` - The workflow stage (checkout, lint, test, build, deploy, etc.)
- `status` - Status (pending, in_progress, success, failed, skipped)
- `custom_message` - Optional custom message

**Example**:
```bash
curl -X POST "http://localhost:8000/api/py/toast/workflow-feedback?stage=deploy&status=success"
```

### Core API Endpoints

- `GET /api/py/health` - Health check with feature list
- `GET /api/py/ecosystem-status` - MBTQ ecosystem integration status
- `GET /api/py` - Root endpoint with API navigation

### Legacy Endpoints (Backward Compatible)

- `GET /api/py/helloFastApi` - Original hello endpoint

## 📊 Validation Criteria

### Visual-First Standards

- ✅ **Color Contrast**: Enhanced ratios for visual clarity
- ✅ **Visual Indicators**: All audio cues have visual alternatives
- ✅ **Text Readability**: Optimized for visual processing
- ✅ **Motion Sensitivity**: Respectful of visual processing differences

### ASL Navigation Compatibility

- ✅ **Gesture Support**: Interface responds to sign language input patterns
- ✅ **Visual Feedback**: Clear visual responses to all interactions
- ✅ **Spatial Logic**: Layout supports spatial thinking patterns
- ✅ **Time Flexibility**: No time-based interactions that exclude processing time

### Audio-Bypass Requirements

- ✅ **No Audio-Only Content**: All audio has visual alternatives
- ✅ **Visual Alerts**: System notifications are visual-first
- ✅ **Captions**: Video content includes accurate captions
- ✅ **Transcript Access**: Audio content has full text alternatives

## 🔗 MBTQ Ecosystem Integration

### DeafAUTH Connection

```javascript
// Validate authentication flow accessibility
const authValidation = await fetch('/api/py/deafauth-validate', {
  method: 'POST',
  body: JSON.stringify({ auth_flow_url: 'https://your-auth.com' })
});
```

### Fibonrose Trust Reporting

```javascript
// Report accessibility scores to trust system
const trustReport = await fetch('/api/py/fibonrose-report', {
  method: 'POST',
  body: JSON.stringify({ 
    url: 'https://validated-site.com',
    deaf_score: 92,
    asl_compatible: true
  })
});
```

### 360Magicians AI Integration

```javascript
// AI agents can trigger validation tasks
const aiValidation = await fetch('/api/py/ai-validate', {
  method: 'POST',
  headers: { 'X-Magician-Role': 'accessibility-auditor' },
  body: JSON.stringify({ task: 'validate_batch', urls: [...] })
});
```

## 🛠️ Development

### Project Structure

```
Developer-Magician/
├── app/                    # Next.js frontend
│   ├── components/         # UI components
│   ├── validation/         # Validation dashboard
│   └── api/               # Next.js API routes
├── api/                   # FastAPI backend
│   ├── validators/        # Core validation logic
│   ├── deaf_first/       # Deaf-specific checks
│   ├── integrations/     # MBTQ ecosystem connections
│   └── models/           # Data models
├── public/               # Static assets
└── tests/               # Test suites
```

### Environment Variables

```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
DEAFAUTH_API_KEY=your_deafauth_key
FIBONROSE_ENDPOINT=https://fibonrose.api.url
DAO_PERMISSIONS_URL=https://mbtquniverse.com/api
```

### Adding Custom Validators

```python
# api/validators/custom_validator.py
from .base import BaseValidator

class MyDeafFirstValidator(BaseValidator):
    def validate(self, content):
        # Your custom Deaf-first validation logic
        return {
            'passed': True,
            'score': 95,
            'recommendations': [...]
        }
```

## 📈 Scoring System

### Deaf-First Score (0-100)

- **Visual Clarity**: 25 points
- **ASL Compatibility**: 25 points
- **Audio Independence**: 25 points
- **Navigation Logic**: 25 points

### Trust Integration

- Scores automatically logged to Fibonrose
- DAO governance can adjust scoring criteria
- Community validation through mbtquniverse.com

## 🚢 Deployment

### Vercel (Recommended)

```bash
# Deploy to Vercel
vercel --prod
```

### GitHub Pages

This project is configured to deploy to GitHub Pages automatically via GitHub Actions.

#### Automatic Deployment

When you push to the `main` branch, the GitHub Actions workflow will automatically:
1. Build the Next.js application as a static site
2. Export the static files to the `out/` directory
3. Deploy to GitHub Pages

**Live URL**: `https://pinkycollie.github.io/Developer-Magician/`

#### Manual Deployment

To deploy manually:

```bash
# Install dependencies
npm install

# Build and export the static site
npm run build-export

# The static files will be in the 'out/' directory
```

The workflow file is located at `.github/workflows/deploy-github-pages.yml`.

**Note**: The site uses `output: 'export'` in `next.config.js` for static site generation. This means dynamic routes and API routes won't work in the GitHub Pages deployment. For full functionality including FastAPI backend, use Vercel or a manual server deployment.

### Manual Server

```bash
# Production build
npm run build

# Start production server
npm start
```

### Docker

```bash
# Build and run
docker build -t developer-magician .
docker run -p 3000:3000 developer-magician
```

## 🤝 Contributing

This service is part of the 360 Magicians and follows Deaf-first development principles:

1. **Visual-First Development**: All UI changes must prioritize visual communication
1. **ASL Logic**: Consider sign language navigation patterns
1. **Community Validation**: Changes reviewed by Deaf community members
1. **Ecosystem Integration**: Maintain compatibility with other services

## 📄 License

MIT License - 360 Magicians

## 🔗 Developer Magician Link


-----

**Built with ❤️ for the Deaf community by MBTQ**
