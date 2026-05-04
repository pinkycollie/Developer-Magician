# Hybrid Multi-Project Backend

**Modular FastAPI + Next.js Backend for Multiple Projects**

[![CI Status](https://github.com/pinkycollie/accessibility-validator/workflows/CI%20-%20Build%20and%20Test/badge.svg)](https://github.com/pinkycollie/accessibility-validator/actions)
[![Security](https://github.com/pinkycollie/accessibility-validator/workflows/Security%20Scanning/badge.svg)](https://github.com/pinkycollie/accessibility-validator/security)

A flexible, scalable backend system designed to handle multiple projects under one unified API. Built with FastAPI and Next.js 14, this hybrid architecture supports REST APIs, SaaS applications, automation workflows, and more - all dynamically managed from a single codebase.

> 📖 **New to this system?** Start with [OVERVIEW.md](OVERVIEW.md) for a visual guide, then follow [QUICKSTART.md](QUICKSTART.md) to get running in 5 minutes!

## 🎯 What Makes This Hybrid?

This backend is designed to solve the "scattered projects" problem. Instead of managing separate FastAPI apps, Django projects, and automation scripts across different repositories, this system provides:

- **Multi-Project Support**: Run multiple independent APIs under different prefixes
- **Dynamic Loading**: Projects load automatically based on configuration
- **Shared Integrations**: Reusable Google AI, Supabase, and other integrations
- **Flexible Deployment**: Works on Vercel, Cloud Run, Docker, or traditional servers
- **Technology Agnostic**: Support FastAPI, Django, automation scripts, and more
The Accessibility Validator is a core service within PinkSync that ensures all interfaces prioritize ASL flow and bypass audio-only UX. This service validates websites and applications for Deaf-first accessibility, going beyond standard WCAG compliance to focus on visual ui and sign language navigation patterns.

## 🎯 Purpose in MBTQ Ecosystem

- **PinkSync Role**: Acts as the “nervous system” executor for accessibility validation
- **DeafAUTH Integration**: Validates identity flows work for Deaf users
- **Fibonrose Logging**: Reports accessibility scores to trust/reputation system
- **360Magicians Compatible**: AI agents can trigger validation tasks
- **DAO Governed**: Validation standards controlled by mbtquniverse.com governance

## ✨ Key Features

- 🤖 **Automated CI/CD Pipeline** - Continuous integration and deployment with GitHub Actions
- 🔒 **Security Scanning** - Automated vulnerability detection with CodeQL and dependency audits
- 🔄 **Auto-Fix** - Automatic code formatting and linting fixes
- 📦 **Dependency Management** - Automated updates via Dependabot
- 🐳 **Docker Support** - Lightweight containerized deployment
- 🏢 **Multi-Tenant** - Configurable deployments for different use cases
- 🧪 **Test Infrastructure** - Automated testing for Python and JavaScript

## 🚀 Quick Deploy

### Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/pinkycollie/developer-magician.git
cd accessibility-validator

# Run automated setup script
npm run setup
# or
bash scripts/setup-dev.sh
```

This will:
- Install all dependencies (Node.js and Python)
- Create Python virtual environment
- Generate `.env.local` template
- Provide next steps

### One-Click Vercel Deploy
## 🚀 Quick Start

### One Command Setup

```bash
git clone https://github.com/pinkycollie/backend.git
cd backend

# Install all dependencies
npm install
pip install -r requirements.txt

# Copy environment template
cp .env.template .env.local
# Edit .env.local with your configuration

# Run development server
# Run development server (Next.js + FastAPI)
npm run dev
```

**Access:**
- Frontend: http://localhost:3000
- API Documentation: http://localhost:8000/api/py/docs
- Backend API: http://localhost:8000/api/py

### Docker Deployment

```bash
# Build and run with Docker Compose
npm run docker:run
# or
docker-compose up -d

# Stop services
npm run docker:stop
```

## 🏗️ Architecture
### Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/pinkycollie/backend)

Vercel automatically detects and deploys both Next.js frontend and FastAPI backend.

## 🏗️ Architecture

### Current Projects

The backend includes these pre-configured projects:

1. **Core API** (`/api/py`)
   - Base FastAPI endpoints
   - Health checks and system status
   - Project management

2. **Accessibility Validator** (`/api/accessibility`)
   - Deaf-first website validation
   - ASL navigation compatibility checks
   - Audio-bypass detection
   - Visual accessibility scoring

3. **Automation Services** (`/api/automation`)
   - AI-powered task automation
   - Workflow management
   - Background job processing
   - Google AI integration

### Tech Stack

**Frontend:**
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS

**Backend:**
- FastAPI (Python)
- Pydantic for data validation
- Modular architecture

**Integrations (Optional):**
- Google AI
- Supabase
- PostgreSQL
- Redis
- Cloud Run

## 🔧 API Endpoints

### System Endpoints

- `GET /api/py` - Backend info and project list
- `GET /api/py/projects` - List all enabled projects
- `GET /api/py/health` - Health check
- `GET /api/py/docs` - Interactive API documentation

### Accessibility Validator

- `POST /api/accessibility/validate` - Validate URL or HTML content
- `POST /api/accessibility/asl-flow-check` - Check ASL compatibility
- `POST /api/accessibility/audio-bypass-scan` - Detect audio-only elements
- `GET /api/accessibility/deaf-score/{url}` - Get Deaf-first score

### Automation Services

- `POST /api/automation/tasks` - Create automation task
- `GET /api/automation/tasks/{task_id}` - Get task status
- `POST /api/automation/workflows` - Create workflow
- `POST /api/automation/ai/generate` - AI text generation

## 📊 Project Configuration

Projects are configured in `api/core/config.py`:

```python
ProjectConfig(
    name="Your Project",
    type=ProjectType.REST_API,  # or SAAS, AUTOMATION, etc.
    prefix="/api/your-project",
    integrations=[IntegrationType.GOOGLE_AI, IntegrationType.SUPABASE],
    description="Your project description"
)
```

**Supported Project Types:**
- `REST_API` - Standard REST API
- `SAAS` - SaaS application
- `AUTOMATION` - Automation workflows
- `FASTAPI` - FastAPI-specific features
- `DJANGO` - Django integration (coming soon)

**Available Integrations:**
- `GOOGLE_AI` - Google Generative AI
- `SUPABASE` - Supabase database
- `VERCEL` - Vercel deployment
- `CLOUD_RUN` - Google Cloud Run

## 🔗 Adding a New Project

### 1. Create Project Module

```python
# api/projects/my_project.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/my-project",
    tags=["My Project"]
)

@router.get("/")
def get_info():
    return {"name": "My Project", "status": "active"}

@router.post("/action")
async def perform_action(data: dict):
    # Your logic here
    return {"result": "success"}
```

### 2. Add Configuration

```python
# api/core/config.py
"my_project": ProjectConfig(
    name="My Project",
    type=ProjectType.REST_API,
    prefix="/api/my-project",
    integrations=[IntegrationType.GOOGLE_AI],
    description="Custom project description"
)
```

### 3. Include Router

### Available Scripts

```bash
# Development
npm run dev              # Start both Next.js and FastAPI dev servers
npm run next-dev         # Start only Next.js dev server
npm run fastapi-dev      # Start only FastAPI dev server

# Building
npm run build            # Build Next.js production bundle
npm run build:lightweight # Run lightweight build script

# Testing
npm run lint             # Run ESLint on JavaScript/TypeScript
npm run lint:fix         # Run ESLint with auto-fix
npm run test:api         # Run Python API tests

# Utilities
npm run setup            # Run automated development setup
npm run docker:build     # Build Docker image
npm run docker:run       # Start Docker containers
npm run docker:stop      # Stop Docker containers
npm run update-deps      # Update all dependencies
```

### Project Structure
```python
# api/index.py
from .projects import my_project

app.include_router(my_project.router)
```
accessibility-validator/
├── .github/
│   ├── workflows/          # CI/CD automation workflows
│   └── dependabot.yml      # Automated dependency updates
├── app/                    # Next.js frontend
│   ├── components/         # UI components
│   ├── validation/         # Validation dashboard
│   └── api/               # Next.js API routes
├── api/                   # FastAPI backend
│   ├── tests/             # API test suite
│   ├── validators/        # Core validation logic
│   ├── deaf_first/       # Deaf-specific checks
│   ├── integrations/     # MBTQ ecosystem connections
│   └── models/           # Data models
├── config/                # Multi-tenant configurations
├── docs/                  # Documentation
├── scripts/               # Build and setup scripts
├── public/                # Static assets
└── tests/                 # Test suites
```

That's it! Your project is now live at `/api/my-project`

## 🛠️ Environment Variables

Create `.env.local`:

Copy `.env.template` to `.env.local` and configure:

```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
TENANT_CONFIG=development  # Options: default, enterprise, startup, community, development

# MBTQ Ecosystem (optional)
DEAFAUTH_API_KEY=your_deafauth_key
FIBONROSE_ENDPOINT=https://fibonrose.api.url
DAO_PERMISSIONS_URL=https://mbtquniverse.com/api
```
# Google AI (Optional)
GOOGLE_AI_API_KEY=your_api_key

# Supabase (Optional)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

# Database (Optional)
DATABASE_URL=postgresql://user:pass@localhost:5432/db

# Redis (Optional)
REDIS_HOST=localhost
REDIS_PORT=6379

# Vercel (Optional)
VERCEL_TOKEN=your_vercel_token
```

## 📈 Use Cases

### 1. Pure REST API
- Focus on `api/` directory
- Multiple API projects under different prefixes
- Shared integrations and services

### 2. Full-Stack SaaS
- Next.js frontend in `app/`
- FastAPI backend in `api/`
- Database integration with Supabase

### 3. Automation Platform
- AI-powered workflows
- Background task processing
- Integration with Google AI

### 4. Microservices
- Multiple independent services
- Shared authentication
- Unified API gateway

### 5. Legacy Integration
- Django app integration
- Gradual migration path
- Shared resources

## 🚢 Deployment

### Automated CI/CD (GitHub Actions)

This repository includes comprehensive CI/CD automation:

- ✅ **Continuous Integration**: Automatic linting, testing, and building on every push
- 🚀 **Continuous Deployment**: Auto-deploy to Vercel on merge to main
- 🔒 **Security Scanning**: Weekly vulnerability scans and CodeQL analysis
- 🔄 **Auto-Fix**: Automatic code formatting and dependency updates
- 📦 **Dependabot**: Automated dependency update PRs

**Setup:**
1. Fork/clone this repository
2. Add GitHub Secrets for Vercel deployment (see [CI/CD Guide](docs/CI-CD-GUIDE.md))
3. Push to `main` branch to trigger automatic deployment

**Required GitHub Secrets:**
- `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` (for deployment)
- `DEAFAUTH_API_KEY`, `FIBONROSE_API_KEY`, `MAGICIAN_API_KEY` (optional, for ecosystem integration)

See the complete [CI/CD Documentation](docs/CI-CD-GUIDE.md) for detailed setup and usage.

### Vercel (Recommended)

1. Push to GitHub
2. Import to Vercel
3. Add environment variables
4. Deploy automatically

### Cloud Run

```bash
gcloud run deploy backend \
  --source . \
  --platform managed \
  --region us-central1
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "api.index:app", "--host", "0.0.0.0"]
```

```bash
docker build -t backend .
docker run -p 8000:8000 backend
```

### Traditional Server

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build and run manually
docker build -t accessibility-validator .
docker run -p 3000:3000 -p 8000:8000 accessibility-validator

# Stop services
docker-compose down
```

### Multi-Tenant Deployment

The application supports multiple deployment configurations (see `config/multi-tenant.yml`):
- **Enterprise**: Full features for large organizations
- **Startup**: Lightweight for small teams
- **Community**: Free tier with basic features
- **Development**: Full access for testing

Set `TENANT_CONFIG` environment variable to select configuration.
pip install gunicorn
gunicorn api.index:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📚 Documentation

- **[📋 OVERVIEW.md](OVERVIEW.md)** - System overview and visual guide ⭐ Start here!
- **[⚡ QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
- **[🏗️ ARCHITECTURE.md](ARCHITECTURE.md)** - Detailed system architecture
- **[🔧 SETUP_GUIDE.md](SETUP_GUIDE.md)** - Step-by-step setup for different use cases
- **[💡 EXAMPLES.md](EXAMPLES.md)** - Practical usage examples
- **[📖 API Documentation](http://localhost:8000/api/py/docs)** - Interactive API docs (when running)

## 🤝 Contributing

This is a modular system designed for extensibility:

1. **Add Projects**: Create new modules in `api/projects/`
2. **Add Integrations**: Extend `api/integrations/`
3. **Add Services**: Build reusable services in `api/services/`
4. **Configure**: Manage in `api/core/config.py`

## 🎯 Key Features

✅ **Multi-Project Support** - Run multiple APIs from one codebase
✅ **Dynamic Loading** - Projects load based on configuration
✅ **Shared Integrations** - Reuse Google AI, Supabase, etc.
✅ **Modular Architecture** - Clean separation of concerns
✅ **Type Safety** - Full Pydantic validation
✅ **Auto Documentation** - Built-in Swagger/OpenAPI docs
✅ **Flexible Deployment** - Vercel, Cloud Run, Docker, or traditional
✅ **Technology Agnostic** - Support any Python framework

## 📄 License

MIT License - Feel free to use for your projects

## 🔗 Part of MBTQ Ecosystem

- **Main**: [mbtq.dev](https://mbtq.dev)
- **DeafAUTH**: Identity and authentication for Deaf users
- **Fibonrose**: Trust and reputation system
- **MagicianCore**: Vendors, Providers, Agente
- **PinkSync**: Accessibility and automation nervous system

-----

**Built for scalability, designed for flexibility** 🚀
**Built with ❤️ for the Deaf community by MBTQ**
