---
id: poco
type: knowledge
owner: OA_Triage
---
# poco
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

![Poco Hero](assets/hero.png)

# Poco: Your Pocket Coworker

A safer, more beautiful, and easier-to-use OpenClaw alternative

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Docs](https://img.shields.io/badge/poco-docs-blueviolet)](https://docs.poco-ai.com/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/poco-ai/poco-agent)

[English](README.md) | [简体中文](README_zh.md)

</div>

## Core Features

- **Secure Sandbox**
  All tasks run in an isolated container. Feel free to install dependencies, modify files, and execute commands — without affecting the host environment.
- **More Than a Chatbot**
  - Supports Plan Mode, conversation queueing, conversation termination ...
  - **Project management**: organize and switch between tasks and contexts more effectively
  - **File uploads**: accept and work with multiple file formats
- **Polished, Productive UI**
  - **Artifacts view**: render and preview many formats (HTML, PDF, Markdown, images, videos, Xmind, Excalidraw, Drawio, and more)
  - **Playback view**: replay command I/O, browser sessions, and Skills/MCP tool calls
  - **Light/Dark mode** support
- **Agentic Experience**
  - **native Claude Code experience** - Slash Commands, Plan Mode, AskQuestion ...
  - **MCP & Skills** - easy to import and infinitely extensible
  - **Browser** - Built-in browser for autonomous web research
  - **GitHub repo integration** for code search and editing
  - **Background execution & scheduled triggers** — your agent can keep running in the cloud even after you close the browser
- **Interaction**
  - **Mobile support**: control your agent anytime, anywhere
  - **IM integration**: embedded backend messaging via DingTalk, Feishu, and Telegram, with push notifications and event subscriptions
  - **Self-hosting**: one-click Docker deployment with a full runtime environment
  - **Cloud subscription**: coming soon
  - **Multilingual** support
- **Smart Memory**
  Powered by **mem0**: the agent remembers your preferences, project context, and past interactions to deliver increasingly personalized help.
- Many more powerful features waiting for you to discover!

## Quick Start

Run the interactive setup script to automatically generate configuration and start services:

```bash
./scripts/quickstart.sh
```

Visit: `http://localhost:3000` after startup completes.

For detailed deployment documentation and troubleshooting, please refer to the [Deployment Guide](https://docs.poco-ai.com/en/deployment).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=poco-ai/poco-agent&type=date&legend=top-left)](https://www.star-history.com/#poco-ai/poco-agent&type=date&legend=top-left)

```

### File: backend\README.md
```md

```

### File: executor\README.md
```md

```

### File: frontend\package.json
```json
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "format": "prettier --write ."
  },
  "dependencies": {
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@dnd-kit/utilities": "^3.2.2",
    "@excalidraw/excalidraw": "^0.18.0",
    "@hookform/resolvers": "^5.2.2",
    "@radix-ui/react-accordion": "^1.2.12",
    "@radix-ui/react-alert-dialog": "^1.1.15",
    "@radix-ui/react-aspect-ratio": "^1.1.8",
    "@radix-ui/react-avatar": "^1.1.11",
    "@radix-ui/react-checkbox": "^1.3.3",
    "@radix-ui/react-collapsible": "^1.1.12",
    "@radix-ui/react-context-menu": "^2.2.16",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-dropdown-menu": "^2.1.16",
    "@radix-ui/react-hover-card": "^1.1.15",
    "@radix-ui/react-label": "^2.1.8",
    "@radix-ui/react-menubar": "^1.1.16",
    "@radix-ui/react-navigation-menu": "^1.2.14",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-progress": "^1.1.8",
    "@radix-ui/react-radio-group": "^1.3.8",
    "@radix-ui/react-scroll-area": "^1.2.10",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-separator": "^1.1.8",
    "@radix-ui/react-slider": "^1.3.6",
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-switch": "^1.2.6",
    "@radix-ui/react-tabs": "^1.1.13",
    "@radix-ui/react-toggle": "^1.1.10",
    "@radix-ui/react-toggle-group": "^1.1.11",
    "@radix-ui/react-tooltip": "^1.2.8",
    "accept-language": "^3.0.20",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "date-fns": "^4.1.0",
    "embla-carousel-react": "^8.6.0",
    "gsap": "^3.14.2",
    "highlight.js": "^11.11.1",
    "html-to-image": "^1.11.13",
    "i18next": "^25.7.4",
    "i18next-browser-languagedetector": "^8.2.0",
    "i18next-resources-to-backend": "^1.2.1",
    "input-otp": "^1.4.2",
    "lucide-react": "^0.562.0",
    "mermaid": "^10.9.3",
    "motion": "^12.29.0",
    "next": "16.1.1",
    "next-themes": "^0.4.6",
    "react": "19.2.3",
    "react-day-picker": "^9.13.0",
    "react-doc-viewer": "^0.1.15",
    "react-dom": "19.2.3",
    "react-hook-form": "^7.71.0",
    "react-i18next": "^16.5.2",
    "react-markdown": "^10.1.0",
    "react-pdf": "9.0.0",
    "react-resizable-panels": "^2.x.x",
    "react-speech-recognition": "^4.0.1",
    "react-syntax-highlighter": "^16.1.0",
    "recharts": "2.15.4",
    "rehype-highlight": "^7.0.2",
    "rehype-katex": "^7.0.1",
    "remark-breaks": "^4.0.0",
    "remark-gfm": "^4.0.1",
    "remark-math": "^6.0.0",
    "sonner": "^2.0.7",
    "swiper": "^12.0.3",
    "tailwind-merge": "^3.4.0",
    "vaul": "^1.1.2",
    "zod": "^4.3.5"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@types/react-syntax-highlighter": "^15.5.13",
    "eslint": "^9",
    "eslint-config-next": "16.1.1",
    "eslint-config-prettier": "^10.1.8",
    "prettier": "^3.7.4",
    "tailwindcss": "^4",
    "tw-animate-css": "^1.4.0",
    "typescript": "^5"
  }
}

```

### File: frontend\README.md
```md
# Poco Frontend

Poco frontend is a Next.js 16 + React 19 application for task creation, agent execution monitoring, and capability management.

## Tech stack

- Next.js 16 (App Router)
- React 19 + TypeScript
- Tailwind CSS v4
- shadcn/ui
- i18next based internationalization
- pnpm

## Run locally

```bash
pnpm install
pnpm dev
```

Open `http://localhost:3000`.

## Common commands

```bash
pnpm dev
pnpm build
pnpm start
pnpm lint
```

## Environment

Frontend talks to backend through the Next.js proxy route at `app/api/v1/[...path]/route.ts`.

Useful variables:

- `BACKEND_URL`
- `POCO_BACKEND_URL`
- `POCO_API_URL`
- `NEXT_PUBLIC_API_URL`

## Architecture

Quick map:

- `app/`: routes + layouts + global styles
- `components/ui`: reusable UI primitives
- `components/shared`: feature-agnostic shared components
- `components/shell`: application shell & layout composition (may depend on `features/*`)
- `features/*`: domain modules
- `hooks/`: shared React hooks
- `lib/`: shared runtime utilities
- `services/`: API client and cross-feature service modules
- `types/`: global TypeScript types

## i18n

All user-facing strings should be translated via i18n keys.

Locale files:

- `lib/i18n/locales/en/translation.json`
- `lib/i18n/locales/zh/translation.json`

```

### File: backend\app\main.py
```py
from fastapi import FastAPI

from app.api import setup_routers
from app.core.errors.exception_handlers import setup_exception_handlers
from app.core.middleware import setup_middleware
from app.core.observability.logging import configure_logging
from app.core.settings import get_settings
from app.lifecycle.lifespan import lifespan


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(
        debug=settings.debug,
        service_name="backend",
        log_sql=settings.log_sql,
        access_log=settings.uvicorn_access_log,
    )

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        lifespan=lifespan,
    )

    setup_middleware(app)
    setup_exception_handlers(app, debug=settings.debug)
    setup_routers(app)

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    settings = get_settings()
    uvicorn.run(app, host=settings.host, port=settings.port)

```

### File: executor\app\main.py
```py
import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api import task_router
from app.core.middleware import setup_middleware
from app.core.observability.logging import configure_logging

configure_logging(
    debug=os.getenv("DEBUG", "").strip().lower() in {"1", "true", "yes", "y", "on"},
    service_name="executor",
)

app = FastAPI()

setup_middleware(app)
app.include_router(task_router)


@app.get("/health")
async def health_check() -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)

```

### File: .pre_commit_config.yaml
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.10
    hooks:
      - id: ruff-check
        name: backend · lint
        exclude: ^backend/assets/
      - id: ruff-format
        name: backend · format
        exclude: ^backend/assets/

  - repo: https://github.com/facebook/pyrefly-pre-commit
    rev: 0.47.0
    hooks:
      - id: pyrefly-check
        name: backend · typecheck
        exclude: ^backend/assets/
        pass_filenames: true
        language: system

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.39.1
    hooks:
      - id: eslint
        name: frontend · lint
        exclude: ^backend/assets/
        args: ["--config", "frontend/eslint.config.mjs"]
        files: ^frontend/.*\.[jt]sx?$
        types: [file]
        additional_dependencies:
          - eslint@9.39.1
          - eslint-config-next@16.1.1
          - eslint-config-prettier@10.1.8

  - repo: https://github.com/rbubley/mirrors-prettier
    rev: v3.7.4
    hooks:
      - id: prettier
        name: frontend · format
        exclude: ^backend/assets/

```

### File: AGENTS.md
```md
# AGENTS.md

This file provides guidance for AI coding agents working with code in this repository.

## Project Overview

Poco is a multi-service AI agent execution platform that orchestrates Claude AI agents to perform coding tasks. The system consists of four main components:

- **Frontend** (Next.js 16) - Web UI for task management and monitoring
- **Backend** (FastAPI) - API server, database management, and session orchestration
- **Executor** (FastAPI + Claude Agent SDK) - Agent execution engine with hook-based extensibility
- **Executor Manager** (FastAPI + APScheduler) - Task scheduling and dispatch service

## Architecture Flow

1. User creates task via Frontend
2. Executor Manager receives task, creates session via Backend
3. Executor Manager schedules task with APScheduler
4. Task Dispatcher sends task to Executor with callback URL
5. Executor runs Claude Agent SDK with configured hooks
6. Hooks send progress callbacks to Executor Manager during execution
7. Executor Manager forwards callbacks to Backend for persistence
8. Frontend polls Backend for session status updates

## Development Commands

### Frontend (Next.js)

```bash
cd frontend
pnpm install        # Install dependencies
pnpm dev            # Development server
pnpm build          # Build for production
pnpm start          # Start production server
pnpm lint           # ESLint
pnpm format         # Prettier
```

### Python Services (Backend, Executor, Executor Manager)

Each Python service has its own directory with a `pyproject.toml`. Run commands from within the service directory:

```bash
cd <service>        # backend/, executor/, or executor_manager/
uv sync             # Install dependencies
uv run python -m app.main    # Run development server
# Or directly with uvicorn:
uvicorn app.main:app --reload
```

### Database Migrations (Backend)

```bash
cd backend
uv run -m alembic revision --autogenerate -m "description"  # Autogenerate migration (review and adjust)
uv run -m alembic upgrade head                               # Apply migrations
uv run -m alembic downgrade -1                               # Rollback one migration
```

Guideline: Always start migrations with `--autogenerate` + `upgrade head`, then manually review and adjust the generated revision file. Do not hand-write a migration from scratch as the first step.

### Pre-commit Hooks

```bash
pre-commit install      # Install hooks
pre-commit run --all-files  # Run manually
```

## Technology Stack

**Frontend:** Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v4, shadcn/ui, pnpm

**Backend Services:** Python 3.12+, FastAPI, Uvicorn, SQLAlchemy 2.0, Alembic, Pydantic Settings, PostgreSQL

**Executor:** claude-agent-sdk, FastAPI

**Executor Manager:** APScheduler, httpx, FastAPI

**Package Managers:** UV for Python, pnpm for Node.js

**Python Package Index:** Tsinghua mirror (<https://pypi.tuna.tsinghua.edu.cn/simple>)

## Code Organization

### Backend (`backend/app/`)

- `api/v1/` - API endpoints (sessions, callback)
- `core/` - Settings, error handlers, middleware, observability
- `models/` - SQLAlchemy models (agent_session, agent_message, tool_execution, usage_log)
- `repositories/` - Data access layer (session_repository, message_repository, etc.)
- `schemas/` - Pydantic schemas (session, callback, response)
- `services/` - Business logic (session_service, callback_service)
- `main.py` - FastAPI app factory

### Executor (`executor/app/`)

- `core/` - AgentExecutor engine, workspace management, callback client
- `hooks/` - Hook system for extensibility (base, manager, callback, todo, workspace)
- `utils/` - Serializer, git platform clients (GitHub, GitLab)
- `schemas/` - Request, response, callback, state schemas and enums
- `api/v1/` - Task execution callback endpoint

### Executor Manager (`executor_manager/app/`)

- `core/settings.py` - Service configuration
- `scheduler/` - APScheduler config and task dispatcher
- `services/` - Backend and executor API clients
- `schemas/` - Task and callback schemas
- `api/v1/` - Task creation, status, and callback endpoints

### Frontend (`frontend/`)

- `app/` - App Router routes, layouts, loading states, proxy routes
- `features/` - Domain modules (chat, projects, capabilities, scheduled-tasks, etc.)
- `components/` - Cross-feature shared components (`ui/`, `shared/`, `shell/`)
- `hooks/` - Cross-feature reusable hooks only
- `lib/` - Framework-agnostic utilities, i18n setup, startup preload logic
- `services/` - Global infrastructure only (e.g., API client); do not put feature business logic here
- `types/` - Global shared types only; feature-specific types stay in each feature

## Key Design Patterns

- **Repository Pattern** - Data access abstraction in `backend/app/repositories/`
- **Service Layer** - Business logic in `backend/app/services/`
- **Hook Pattern** - Plugin-based extensibility in `executor/app/hooks/`
- **Abstract Base Classes** - Git platform clients extend `BaseGitClient`

## Environment Configuration

Each Python service requires a `.env` file. See `backend/.env.example` for the Backend template.

**Backend:** DATABASE_URL, HOST, PORT, CORS_ORIGINS, SECRET_KEY, DEBUG
**Executor Manager:** backend_url, callback_base_url, max_concurrent_tasks, callback_token
**Executor:** DEFAULT_MODEL, workspace mount path

## Development Standards

### Code Comments

- All comments must be in English
- Keep comments concise - omit obvious comments
- Follow Google Python Style Guide for docstrings

### Type Annotations (Python 3.12+)

All Python code MUST use proper type annotations. Since we use Python 3.12+, prefer built-in generic types over `typing` module (e.g., `list[T]` instead of `List[T]`, `T | None` instead of `Optional[T]`).

### Backend Layer Separation

**Repositories (`backend/app/repositories/`):**

- Database operations only (CRUD)
- No business logic
- Return SQLAlchemy model instances

**Services (`backend/app/services/`):**

- Business logic
- Transaction management
- Orchestrate multiple repository calls
- **Return types:** SQLAlchemy models OR Pydantic schemas
- **DO NOT** return `dict[str, Any]` - use explicit schemas for type safety

**Database Injection:**

Database sessions MUST be injected via FastAPI dependency injection at the API endpoint level, then passed as parameters to service/repository methods. Each request gets its own db session from the connection pool.

**Schemas (`backend/app/schemas/`):**

- Data transfer objects
- Define API request/response contracts
- Pydantic models for validation and serialization
- **Naming:** `{Entity}{Action}Request` / `{Entity}Response` (e.g., `SessionCreateRequest`, `CallbackResponse`)
- Internal/nested models use descriptive names (e.g., `TaskConfig`, `AgentCurrentState`)

### API Endpoint Exception Handling

Global handlers in `app/core/errors/exception_handlers.py` process:

- `AppException` -> 400 with error code
- `HTTPException` -> preserve status code
- `Exception` -> 500 with stack trace logged

**Rules:**

- **DO NOT** catch `Exception` to re-raise as `HTTPException(500, ...)` (redundant)
- **DO** raise `AppException` for business errors, `HTTPException` for HTTP-specific errors
- **DO NOT** log errors - global handler uses `logger.exception()`

### Frontend Styling

Use Tailwind CSS v4 utility classes with CSS variables. All colors, shadows, and spacing should reference the design system variables in `app/globals.css`:

- Colors: `var(--background)`, `var(--foreground)`, `var(--primary)`, `var(--border)`, etc.
- Shadows: `var(--shadow-sm)`, `var(--shadow-md)`, `var(--shadow-lg)`, etc.
- Border radius: `var(--radius)`

**DO NOT** hardcode colors like `#ffffff` or write raw CSS without using these variables.

### Frontend Internationalization (i18n)

All user-facing text MUST use i18n translations, NOT hardcoded strings:

```tsx
import { useT } from "@/lib/i18n/client";
const { t } = useT();

// ✅ Correct
<Button>{t("sidebar.newTask")}</Button>

// ❌ Wrong
<Button>New Task</Button>
```

Translation files: `frontend/lib/i18n/locales/{lng}/translation.json` | Config: `frontend/lib/i18n/settings.ts`

### Frontend Architecture and Boundaries

Use feature-first organization with internal layering:

- Recommended internal layout for each feature: `api/`, `model/`, `ui/`, `lib/`, `index.ts`
- `api/`: backend calls and DTO mapping only
- `model/`: business state, domain types, feature hooks/actions
- `ui/`: feature UI components/pages
- `lib/`: pure utility functions scoped to the feature
- `index.ts`: public surface of the feature

Boundary rules:

- `app/` should compose feature public APIs and should not import deep internals from other features
- Cross-feature imports should go through `features/<feature>/index.ts` whenever possible
- Do not import from `features/*/services/*`; use `features/*/api/*` instead
- Do not let low-level features depend on shell/container modules (avoid reverse dependencies)

### Frontend Component Standards

- Prefer one primary component per file
- Split large components into container + presentational parts
- If a component exceeds ~300 lines or mixes unrelated responsibilities, split it
- Keep render logic declarative; move heavy data shaping into hooks or `lib/`
- Reuse shared UI primitives from `components/ui` and shared composites from `components/shared`

### Frontend State and Data Flow

- Keep server data access in feature `api` modules
- Keep feature state in feature hooks/context (`model` layer), not in route files
- Avoid duplicated derived state; compute from source state with memoization
- Use optimistic updates only with rollback handling for failures
- Co-locate domain-specific state with the owning feature

### Frontend Type Safety

- No `any` unless absolutely unavoidable; use explicit interfaces/types
- Keep API request/response types near the feature consuming them
- Validate untrusted external input with schema validation (e.g., `zod`) before mutation calls
- Avoid component-to-component type coupling through container modules

### Next.js App Router Conventions

- Default to Server Components; add `"use client"` only when interactivity is required
- Place route-specific loading UI in `loading.tsx`
- Keep route files thin; delegate business logic to feature modules
- Use proxy route `app/api/v1/[...path]/route.ts` for browser-side API forwarding

### Frontend Performance Guidelines

- Dynamic-import heavy viewers/editors and browser-only libraries
- Memoize expensive computations and stable callbacks in hot rendering paths
- Virtualize or paginate long lists when item count is large
- Avoid unnecessary re-renders caused by unstable object/array literals in props

### Frontend Quality Gates

Before submitting frontend changes:

- `pnpm lint` must pass
- `pnpm build` must pass
- Manually verify key flows impacted by changes (create task, chat execution, project switching, capabilities CRUD)

## Linting and Formatting

**Python:**

- Ruff for linting and formatting
- Pyrefly for type checking
- Configured in root `pyproject.toml` and `.pre-commit-config.yaml`

**TypeScript/React:**

- ESLint with Next.js config
- Prettier for formatting
- Configured in `.pre-commit-config.yaml`

## Important Notes

- The workspace mount path in `executor/app/core/engine.py` is hardcoded to `/Users/qychen/01-Develop/toto`

- APScheduler uses in-memory job storage (jobs lost on restart)
- Callback endpoints use token-based authentication
- Git operations support GitHub and GitLab platforms
- All services can run independently for local development

```

### File: CLAUDE.md
```md
# AGENTS.md

This file provides guidance for AI coding agents working with code in this repository.

## Project Overview

Poco is a multi-service AI agent execution platform that orchestrates Claude AI agents to perform coding tasks. The system consists of four main components:

- **Frontend** (Next.js 16) - Web UI for task management and monitoring
- **Backend** (FastAPI) - API server, database management, and session orchestration
- **Executor** (FastAPI + Claude Agent SDK) - Agent execution engine with hook-based extensibility
- **Executor Manager** (FastAPI + APScheduler) - Task scheduling and dispatch service

## Architecture Flow

1. User creates task via Frontend
2. Executor Manager receives task, creates session via Backend
3. Executor Manager schedules task with APScheduler
4. Task Dispatcher sends task to Executor with callback URL
5. Executor runs Claude Agent SDK with configured hooks
6. Hooks send progress callbacks to Executor Manager during execution
7. Executor Manager forwards callbacks to Backend for persistence
8. Frontend polls Backend for session status updates

## Development Commands

### Frontend (Next.js)

```bash
cd frontend
pnpm install        # Install dependencies
pnpm dev            # Development server
pnpm build          # Build for production
pnpm start          # Start production server
pnpm lint           # ESLint
pnpm format         # Prettier
```

### Python Services (Backend, Executor, Executor Manager)

Each Python service has its own directory with a `pyproject.toml`. Run commands from within the service directory:

```bash
cd <service>        # backend/, executor/, or executor_manager/
uv sync             # Install dependencies
uv run python -m app.main    # Run development server
# Or directly with uvicorn:
uvicorn app.main:app --reload
```

### Database Migrations (Backend)

```bash
cd backend
uv run -m alembic revision --autogenerate -m "description"  # Autogenerate migration (review and adjust)
uv run -m alembic upgrade head                               # Apply migrations
uv run -m alembic downgrade -1                               # Rollback one migration
```

Guideline: Always start migrations with `--autogenerate` + `upgrade head`, then manually review and adjust the generated revision file. Do not hand-write a migration from scratch as the first step.

### Pre-commit Hooks

```bash
pre-commit install      # Install hooks
pre-commit run --all-files  # Run manually
```

## Technology Stack

**Frontend:** Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v4, shadcn/ui, pnpm

**Backend Services:** Python 3.12+, FastAPI, Uvicorn, SQLAlchemy 2.0, Alembic, Pydantic Settings, PostgreSQL

**Executor:** claude-agent-sdk, FastAPI

**Executor Manager:** APScheduler, httpx, FastAPI

**Package Managers:** UV for Python, pnpm for Node.js

**Python Package Index:** Tsinghua mirror (<https://pypi.tuna.tsinghua.edu.cn/simple>)

## Code Organization

### Backend (`backend/app/`)

- `api/v1/` - API endpoints (sessions, callback)
- `core/` - Settings, error handlers, middleware, observability
- `models/` - SQLAlchemy models (agent_session, agent_message, tool_execution, usage_log)
- `repositories/` - Data access layer (session_repository, message_repository, etc.)
- `schemas/` - Pydantic schemas (session, callback, response)
- `services/` - Business logic (session_service, callback_service)
- `main.py` - FastAPI app factory

### Executor (`executor/app/`)

- `core/` - AgentExecutor engine, workspace management, callback client
- `hooks/` - Hook system for extensibility (base, manager, callback, todo, workspace)
- `utils/` - Serializer, git platform clients (GitHub, GitLab)
- `schemas/` - Request, response, callback, state schemas and enums
- `api/v1/` - Task execution callback endpoint

### Executor Manager (`executor_manager/app/`)

- `core/settings.py` - Service configuration
- `scheduler/` - APScheduler config and task dispatcher
- `services/` - Backend and executor API clients
- `schemas/` - Task and callback schemas
- `api/v1/` - Task creation, status, and callback endpoints

### Frontend (`frontend/`)

- `app/` - App Router routes, layouts, loading states, proxy routes
- `features/` - Domain modules (chat, projects, capabilities, scheduled-tasks, etc.)
- `components/` - Cross-feature shared components (`ui/`, `shared/`, `shell/`)
- `hooks/` - Cross-feature reusable hooks only
- `lib/` - Framework-agnostic utilities, i18n setup, startup preload logic
- `services/` - Global infrastructure only (e.g., API client); do not put feature business logic here
- `types/` - Global shared types only; feature-specific types stay in each feature

## Key Design Patterns

- **Repository Pattern** - Data access abstraction in `backend/app/repositories/`
- **Service Layer** - Business logic in `backend/app/services/`
- **Hook Pattern** - Plugin-based extensibility in `executor/app/hooks/`
- **Abstract Base Classes** - Git platform clients extend `BaseGitClient`

## Environment Configuration

Each Python service requires a `.env` file. See `backend/.env.example` for the Backend template.

**Backend:** DATABASE_URL, HOST, PORT, CORS_ORIGINS, SECRET_KEY, DEBUG
**Executor Manager:** backend_url, callback_base_url, max_concurrent_tasks, callback_token
**Executor:** DEFAULT_MODEL, workspace mount path

## Development Standards

### Code Comments

- All comments must be in English
- Keep comments concise - omit obvious comments
- Follow Google Python Style Guide for docstrings

### Type Annotations (Python 3.12+)

All Python code MUST use proper type annotations. Since we use Python 3.12+, prefer built-in generic types over `typing` module (e.g., `list[T]` instead of `List[T]`, `T | None` instead of `Optional[T]`).

### Backend Layer Separation

**Repositories (`backend/app/repositories/`):**

- Database operations only (CRUD)
- No business logic
- Return SQLAlchemy model instances

**Services (`backend/app/services/`):**

- Business logic
- Transaction management
- Orchestrate multiple repository calls
- **Return types:** SQLAlchemy models OR Pydantic schemas
- **DO NOT** return `dict[str, Any]` - use explicit schemas for type safety

**Database Injection:**

Database sessions MUST be injected via FastAPI dependency injection at the API endpoint level, then passed as parameters to service/repository methods. Each request gets its own db session from the connection pool.

**Schemas (`backend/app/schemas/`):**

- Data transfer objects
- Define API request/response contracts
- Pydantic models for validation and serialization
- **Naming:** `{Entity}{Action}Request` / `{Entity}Response` (e.g., `SessionCreateRequest`, `CallbackResponse`)
- Internal/nested models use descriptive names (e.g., `TaskConfig`, `AgentCurrentState`)

### API Endpoint Exception Handling

Global handlers in `app/core/errors/exception_handlers.py` process:

- `AppException` -> 400 with error code
- `HTTPException` -> preserve status code
- `Exception` -> 500 with stack trace logged

**Rules:**

- **DO NOT** catch `Exception` to re-raise as `HTTPException(500, ...)` (redundant)
- **DO** raise `AppException` for business errors, `HTTPException` for HTTP-specific errors
- **DO NOT** log errors - global handler uses `logger.exception()`

### Frontend Styling

Use Tailwind CSS v4 utility classes with CSS variables. All colors, shadows, and spacing should reference the design system variables in `app/globals.css`:

- Colors: `var(--background)`, `var(--foreground)`, `var(--primary)`, `var(--border)`, etc.
- Shadows: `var(--shadow-sm)`, `var(--shadow-md)`, `var(--shadow-lg)`, etc.
- Border radius: `var(--radius)`

**DO NOT** hardcode colors like `#ffffff` or write raw CSS without using these variables.

### Frontend Internationalization (i18n)

All user-facing text MUST use i18n translations, NOT hardcoded strings:

```tsx
import { useT } from "@/lib/i18n/client";
const { t } = useT();

// ✅ Correct
<Button>{t("sidebar.newTask")}</Button>

// ❌ Wrong
<Button>New Task</Button>
```

Translation files: `frontend/lib/i18n/locales/{lng}/translation.json` | Config: `frontend/lib/i18n/settings.ts`

### Frontend Architecture and Boundaries

Use feature-first organization with internal layering:

- Recommended internal layout for each feature: `api/`, `model/`, `ui/`, `lib/`, `index.ts`
- `api/`: backend calls and DTO mapping only
- `model/`: business state, domain types, feature hooks/actions
- `ui/`: feature UI components/pages
- `lib/`: pure utility functions scoped to the feature
- `index.ts`: public surface of the feature

Boundary rules:

- `app/` should compose feature public APIs and should not import deep internals from other features
- Cross-feature imports should go through `features/<feature>/index.ts` whenever possible
- Do not import from `features/*/services/*`; use `features/*/api/*` instead
- Do not let low-level features depend on shell/container modules (avoid reverse dependencies)

### Frontend Component Standards

- Prefer one primary component per file
- Split large components into container + presentational parts
- If a component exceeds ~300 lines or mixes unrelated responsibilities, split it
- Keep render logic declarative; move heavy data shaping into hooks or `lib/`
- Reuse shared UI primitives from `components/ui` and shared composites from `components/shared`

### Frontend State and Data Flow

- Keep server data access in feature `api` modules
- Keep feature state in feature hooks/context (`model` layer), not in route files
- Avoid duplicated derived state; compute from source state with memoization
- Use optimistic updates only with rollback handling for failures
- Co-locate domain-specific state with the owning feature

### Frontend Type Safety

- No `any` unless absolutely unavoidable; use explicit interfaces/types
- Keep API request/response types near the feature consuming them
- Validate untrusted external input with schema validation (e.g., `zod`) before mutation calls
- Avoid component-to-component type coupling through container modules

### Next.js App Router Conventions

- Default to Server Components; add `"use client"` only when interactivity is required
- Place route-specific loading UI in `loading.tsx`
- Keep route files thin; delegate business logic to feature modules
- Use proxy route `app/api/v1/[...path]/route.ts` for browser-side API forwarding

### Frontend Performance Guidelines

- Dynamic-import heavy viewers/editors and browser-only libraries
- Memoize expensive computations and stable callbacks in hot rendering paths
- Virtualize or paginate long lists when item count is large
- Avoid unnecessary re-renders caused by unstable object/array literals in props

### Frontend Quality Gates

Before submitting frontend changes:

- `pnpm lint` must pass
- `pnpm build` must pass
- Manually verify key flows impacted by changes (create task, chat execution, project switching, capabilities CRUD)

## Linting and Formatting

**Python:**

- Ruff for linting and formatting
- Pyrefly for type checking
- Configured in root `pyproject.toml` and `.pre-commit-config.yaml`

**TypeScript/React:**

- ESLint with Next.js config
- Prettier for formatting
- Configured in `.pre-commit-config.yaml`

## Important Notes

- The workspace mount path in `executor/app/core/engine.py` is hardcoded to `/Users/qychen/01-Develop/toto`

- APScheduler uses in-memory job storage (jobs lost on restart)
- Callback endpoints use token-based authentication
- Git operations support GitHub and GitLab platforms
- All services can run independently for local development

```

### File: CONTRIBUTING.md
```md
# Poco Contribution Guide (PR & Development Standards)

This document describes the contribution process for the Poco repository and the development standards that must be followed when submitting code.

## 1. Standard Contribution Workflow

1. First, sync the latest code and create a branch from `main`.
2. Develop in a single-topic branch; avoid putting unrelated changes in the same PR.
3. Complete self-checks locally (see "Pre-commit Checks").
4. Push the branch and create a PR to `main`.
5. Maintainers will review and request changes.
6. Continue pushing to the same branch until the review passes and a maintainer merges it.

## 2. Branch and Commit Standards

It is recommended to use semantic branch names:

- `feat/<short-description>`
- `fix/<short-description>`
- `refactor/<short-description>`
- `docs/<short-description>`
- `chore/<short-description>`

Commit messages should follow Conventional Commits (consistent with the repository's existing history):

- `feat: ...`
- `fix: ...`
- `refactor: ...`
- `docs: ...`
- `chore: ...`

Recommendations:

- Each commit should focus on one logical point.
- Avoid mixing refactoring, formatting, and feature changes in the same commit.

## 3. Pre-commit Checks

Run in the repository root:

```bash
pre-commit run --all-files
```

If you modified the frontend, also run:

```bash
cd frontend
pnpm lint
pnpm build
```

If you modified Python services (`backend`/`executor`/`executor_manager`), please install dependencies and verify the service can start:

```bash
cd <service>
uv sync
uv run python -m app.main
```

If you modified database models, handle migrations as follows (in the `backend` directory):

```bash
uv run -m alembic revision --autogenerate -m "description"
uv run -m alembic upgrade head
```

Then manually verify the auto-generated migration meets expectations.

## 4. PR Description Template

It is recommended to include at least the following in your PR description:

- Background and goals of the changes
- Main changes
- Affected areas (frontend/backend/executor/executor_manager)
- Local verification commands and results
- If UI changes: provide screenshots or recordings
- If database changes: provide migration and rollback instructions
- If breaking changes: clearly state upgrade considerations

## 5. Development Standards

### 5.1 General Standards

- Do not commit keys, tokens, private configuration, or any sensitive information.
- When adding new features, simultaneously update relevant documentation (README, docs, or API docs).
- Keep changes minimal; prioritize fixing root causes, avoid unrelated refactoring.

### 5.2 Python (Backend Services)

- Python version: `3.12+`
- Must write complete type annotations, prefer built-in generics: `list[T]`, `dict[str, Any]`, `X | None`.
- Code comments must be in English; Docstrings follow Google style.

Backend layering standards (`backend`):

- `repositories/` - Database CRUD only, no business logic.
- `services/` - Business orchestration and transaction management.
- `services/` returns SQLAlchemy Model or Pydantic Schema, not raw `dict[str, Any]`.
- Database sessions are created via FastAPI dependency injection at the API layer, then passed to services/repositories.

Exception handling standards (`backend`):

- Business errors use `AppException`.
- HTTP semantic errors use `HTTPException`.
- Do not catch generic `Exception` and wrap it as `HTTPException(500, ...)`.

### 5.3 Frontend (Next.js)

- Use Tailwind CSS v4 with design variables (`frontend/app/globals.css`).
- Do not hardcode colors, shadows, or border-radius; prefer design tokens (e.g., `var(--primary)`, `var(--shadow-md)`, `var(--radius)`).
- All user-facing text must go through i18n; do not write hardcoded strings.
- i18n related paths:
  - `frontend/lib/i18n/client.ts`
  - `frontend/lib/i18n/settings.ts`
  - `frontend/lib/i18n/locales/*/translation.json`

## 6. Review and Merge Criteria

Usually ready to merge when:

- Change goals are clear, PR description is complete.
- Local checks pass, and verification steps are reproducible.
- Code follows layering and style standards.
- Necessary documentation is updated.
- Review comments are addressed or consensus is reached.

Final merge is executed by repository maintainers.

```

### File: README_zh.md
```md
<div align="center">

![Poco Hero](assets/hero.png)

# Poco: Your Pocket Coworker

更安全、更漂亮、更易用的 OpenClaw 替代方案

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Docs](https://img.shields.io/badge/poco-docs-blueviolet)](https://docs.poco-ai.com/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/poco-ai/poco-agent)

[English](README.md) | [简体中文](README_zh.md)

</div>

## 核心功能

- **安全沙箱（Secure Sandbox）**
  所有任务运行在隔离容器中，可自由安装依赖、修改文件与执行命令，**不影响宿主环境**。
- **不仅是 ChatBot**
  - 支持**计划模式（Plan Mode）**、对话排队、对话终止等能力
  - **项目管理**：更好地组织与切换不同任务/上下文
  - **文件上传**：支持多种文件格式输入与处理
- **精美而高效的界面**
  - **产物界面**：支持多种格式渲染与预览（HTML、PDF、Markdown、图片、视频、Xmind、Excalidraw、Drawio 等）
  - **回放界面**：可回看命令输入输出、浏览器操作与 Skills/MCP 调用记录
  - 支持**明暗模式**
- **Agentic 体验**
  - 完整复刻 **Claude Code** 原生体验：Slash Commands、Plan Mode、AskQuestion
  - 支持 **MCP 协议** 与自定义 Skills：易导入、可无限扩展
  - 内置**浏览器**：支持自主网络研究与信息整合
  - 支持 **GitHub 仓库连接**：代码检索、阅读与编辑
  - 支持**后台执行与定时任务**：即使关闭浏览器，Agent 也能在云端持续运行
- **交互重构（多端与消息驱动）**
  - **移动端支持**：随时随地操控你的 Agent
  - **IM 支持**：后端内嵌的钉钉 / 飞书 / Telegram 消息传递，支持推送与事件订阅
  - **个人部署**：一键 Docker 启动，获得完整运行环境
  - **云端订阅**：敬请期待
  - **多语言支持**
- **智能记忆（Smart Memory）**
  Powered by **mem0**：Agent 能记住你的偏好、项目上下文与历史交互，让协作越来越顺手。
- **更多能力等你发现！**

## 快速开始

运行交互式安装脚本，自动生成配置并启动服务：

```bash
./scripts/quickstart.sh
```

启动完成后访问：`http://localhost:3000`

详细的部署文档和问题排查，请参考 [部署指南](https://docs.poco-ai.com/zh/deployment)。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=poco-ai/poco-agent&type=date&legend=top-left)](https://www.star-history.com/#poco-ai/poco-agent&type=date&legend=top-left)

```

### File: frontend\components.json
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "registries": {
    "@react-bits": "https://reactbits.dev/r/{name}.json"
  }
}

```

### File: frontend\next.config.ts
```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // NOTE: added for Docker deployment
  output: "standalone",
  // Disable image optimization for local development
  images: {
    unoptimized: true,
  },
};

export default nextConfig;

```

### File: frontend\pnpm_workspace.yaml
```yaml
packages:
  - .
ignoredBuiltDependencies:
  - sharp
  - unrs-resolver

```

### File: frontend\proxy.ts
```ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import acceptLanguage from "accept-language";
import {
  fallbackLng,
  languages,
  cookieName,
  headerName,
} from "@/lib/i18n/settings";

acceptLanguage.languages(languages);

export const config = {
  matcher: [
    // Exclude Next internals and static assets (e.g. /logo.jpg) from locale redirects.
    "/((?!api|_next/static|_next/image|assets|favicon.ico|sw.js|site.webmanifest|.*\\..*).*)",
  ],
};

/**
 * Next.js middleware for i18n locale detection and routing.
 *
 * Responsibilities:
 * - Detect user language from cookie, Accept-Language header, or URL path
 * - Redirect to locale-prefixed routes when missing
 * - Persist detected language in response headers and cookies
 */
export function proxy(req: NextRequest) {
  const url = new URL(req.url);

  // Skip icon and chrome-related paths
  if (
    url.pathname.indexOf("icon") > -1 ||
    url.pathname.indexOf("chrome") > -1
  ) {
    return NextResponse.next();
  }

  // 1. Detect language from cookie
  let lng: string | undefined;
  if (req.headers.has("cookie")) {
    const cookies = req.headers
      .get("cookie")
      ?.split(";")
      .map((c) => c.trim());
    const i18nCookie = cookies?.find((c) => c.startsWith(`${cookieName}=`));
    if (i18nCookie) {
      const value = i18nCookie.split("=")[1];
      lng = acceptLanguage.get(value) ?? undefined;
    }
  }

  // 2. Fallback to Accept-Language header
  if (!lng) {
    lng = acceptLanguage.get(req.headers.get("Accept-Language")) ?? undefined;
  }

  // 3. Final fallback
  if (!lng) lng = fallbackLng;

  // 4. Check if locale already exists in path
  const lngInPath = languages.find((loc) => url.pathname.startsWith(`/${loc}`));

  const headers = new Headers(req.headers);
  headers.set(headerName, lngInPath || lng);

  // 5. Redirect to locale-prefixed path if missing
  if (!lngInPath && !url.pathname.startsWith("/_next")) {
    return NextResponse.redirect(
      new URL(`/${lng}${url.pathname}${url.search}`, req.url),
    );
  }

  // 6. Persist language from referer
  if (req.headers.has("referer")) {
    const refererUrl = new URL(req.headers.get("referer")!);
    const lngInReferer = languages.find((l) =>
      refererUrl.pathname.startsWith(`/${l}`),
    );

    const response = NextResponse.next({ headers });
    if (lngInReferer) response.cookies.set(cookieName, lngInReferer);
    return response;
  }

  return NextResponse.next({ headers });
}

```

### File: frontend\tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts",
    "**/*.mts"
  ],
  "exclude": ["node_modules"]
}

```

### File: scripts\quickstart.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ENV_FILE:-${ROOT_DIR}/.env}"

DATA_DIR="./oss_data"
DATA_DIR_SET=false
WORKSPACE_DIR="./tmp_workspace"
WORKSPACE_DIR_SET=false
RUSTFS_UID="10001"
RUSTFS_GID="10001"
CHOWN_RUSTFS=true
S3_BUCKET=""
S3_BUCKET_SET=false
S3_ACCESS_KEY=""
S3_ACCESS_KEY_SET=false
S3_SECRET_KEY=""
S3_SECRET_KEY_SET=false
S3_PUBLIC_ENDPOINT=""
S3_PUBLIC_ENDPOINT_SET=false
CORS_ORIGINS=""
CORS_ORIGINS_SET=false
DOCKER_GID=""
START_ALL=true
ONLY_RUSTFS=false
INIT_BUCKET=true
PULL_EXECUTOR=true
FORCE_ENV=false
# Default interactive mode only when stdin is a TTY.
INTERACTIVE=false
if [[ -t 0 ]]; then
  INTERACTIVE=true
fi
ANTHROPIC_KEY=""
ANTHROPIC_BASE_URL=""
DEFAULT_MODEL=""
API_PROVIDER_MODE=""
# Language setting (en or zh)
LANG="en"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Localization function
msg() {
  local key="$1"
  case "$key" in
    # Usage messages
    "usage.header") [[ "$LANG" == "zh" ]] && echo "用法: scripts/quickstart.sh [选项]" || echo "Usage: scripts/quickstart.sh [options]" ;;
    "usage.options") [[ "$LANG" == "zh" ]] && echo "选项:" || echo "Options:" ;;
    "usage.interactive") [[ "$LANG" == "zh" ]] && echo "  -i, --interactive         交互模式（在终端运行时默认启用）" || echo "  -i, --interactive         Interactive mode (default when run in a terminal)" ;;
    "usage.non_interactive") [[ "$LANG" == "zh" ]] && echo "  --non-interactive         禁用交互式提示（推荐用于 CI）" || echo "  --non-interactive         Disable interactive prompts (recommended for CI)" ;;
    "usage.no_start") [[ "$LANG" == "zh" ]] && echo "  --no-start                仅准备环境和目录" || echo "  --no-start                Only prepare env and directories" ;;
    "usage.force_env") [[ "$LANG" == "zh" ]] && echo "  --force-env               覆盖环境文件中的现有密钥" || echo "  --force-env               Overwrite existing keys in env file" ;;
    "usage.llm_api_key") [[ "$LANG" == "zh" ]] && echo "  --llm-api-key KEY         模型 API 密钥（Anthropic 兼容，写入环境文件）" || echo "  --llm-api-key KEY         Model API key (Anthropic-compatible, writes to env)" ;;
    "usage.llm_base_url") [[ "$LANG" == "zh" ]] && echo "  --llm-base-url URL        模型 API Base URL（写入环境文件）" || echo "  --llm-base-url URL        Model API base URL (writes to env)" ;;
    "usage.model") [[ "$LANG" == "zh" ]] && echo "  --model MODEL             默认模型 ID（写入环境文件）" || echo "  --model MODEL             Default model ID (writes to env)" ;;
    "usage.anthropic_key") [[ "$LANG" == "zh" ]] && echo "  --anthropic-key KEY       兼容旧参数，等同于 --llm-api-key" || echo "  --anthropic-key KEY       Legacy alias for --llm-api-key" ;;
    "usage.lang") [[ "$LANG" == "zh" ]] && echo "  --lang LANG               语言设置 (en 或 zh，默认: en)" || echo "  --lang LANG               Language setting (en or zh, default: en)" ;;
    "usage.help") [[ "$LANG" == "zh" ]] && echo "  -h, --help                显示此帮助信息" || echo "  -h, --help                Show this help" ;;
    "usage.advanced") [[ "$LANG" == "zh" ]] && echo "高级选项:" || echo "Advanced options:" ;;
    "usage.examples") [[ "$LANG" == "zh" ]] && echo "示例:" || echo "Examples:" ;;
    "usage.example1") [[ "$LANG" == "zh" ]] && echo "  # 交互式设置（默认）" || echo "  # Interactive setup (default)" ;;
    "usage.example2") [[ "$LANG" == "zh" ]] && echo "  # 交互式设置但不启动服务" || echo "  # Interactive setup without starting services" ;;
    "usage.example3") [[ "$LANG" == "zh" ]] && echo "  # 通过 CLI 快速设置模型 API" || echo "  # Quick model API setup via CLI" ;;
    "usage.example4") [[ "$LANG" == "zh" ]] && echo "  # 使用中文界面" || echo "  # Use Chinese interface" ;;

    # Print messages
    "print.success") [[ "$LANG" == "zh" ]] && echo "成功" || echo "ok" ;;
    "print.warn") [[ "$LANG" == "zh" ]] && echo "警告" || echo "warn" ;;
    "print.error") [[ "$LANG" == "zh" ]] && echo "错误" || echo "error" ;;
    "print.info") [[ "$LANG" == "zh" ]] && echo "信息" || echo "info" ;;

    # Error messages
    "error.missing_cmd") [[ "$LANG" == "zh" ]] && echo "缺少命令" || echo "Missing command" ;;
    "error.unknown_option") [[ "$LANG" == "zh" ]] && echo "未知选项" || echo "Unknown option" ;;
    "error.docker_not_found") [[ "$LANG" == "zh" ]] && echo "未找到 docker compose" || echo "docker compose not found" ;;
    "error.anthropic_not_set") [[ "$LANG" == "zh" ]] && echo "未设置模型 API Key（ANTHROPIC_API_KEY）。请在 .env 中设置，或运行 ./scripts/quickstart.sh（交互式）并传递 --llm-api-key。" || echo "Model API key is not set (ANTHROPIC_API_KEY). Configure it in .env, or run ./scripts/quickstart.sh (interactive) / pass --llm-api-key." ;;

    # Headers
    "header.quickstart") [[ "$LANG" == "zh" ]] && echo "Poco 快速启动" || echo "Poco Quickstart" ;;
    "header.interactive_setup") [[ "$LANG" == "zh" ]] && echo "Poco 交互式设置" || echo "Poco Interactive Setup" ;;
    "header.required_config") [[ "$LANG" == "zh" ]] && echo "必需配置" || echo "Required Configuration" ;;
    "header.optional_config") [[ "$LANG" == "zh" ]] && echo "可选配置" || echo "Optional Configuration" ;;
    "header.s3_endpoint") [[ "$LANG" == "zh" ]] && echo "S3 公共端点配置" || echo "S3 Public Endpoint Configuration" ;;
    "header.setup_complete") [[ "$LANG" == "zh" ]] && echo "设置完成" || echo "Setup Complete" ;;
    "header.lang_select") [[ "$LANG" == "zh" ]] && echo "语言选择" || echo "Language Selection" ;;

    # Interactive setup
    "setup.welcome") [[ "$LANG" == "zh" ]] && echo "欢迎使用 Poco！此向导将帮助您配置基本设置。" || echo "Welcome to Poco! This wizard will help you configure the essential settings." ;;
    "setup.input") [[ "$LANG" == "zh" ]] && echo "请输入" || echo "Input" ;;
    "setup.keep_current") [[ "$LANG" == "zh" ]] && echo "按 Enter 保留" || echo "Press Enter to keep" ;;
    "setup.skipping") [[ "$LANG" == "zh" ]] && echo "跳过" || echo "Skipping" ;;
    "setup.optional") [[ "$LANG" == "zh" ]] && echo "可选" || echo "optional" ;;
    "setup.required") [[ "$LANG" == "zh" ]] && echo "是必需的" || echo "is required" ;;

    # API Key prompts
    "prompt.provider_select") [[ "$LANG" == "zh" ]] && echo "请选择模型 API 端点类型" || echo "Select your model API endpoint type" ;;
    "prompt.provider_official") [[ "$LANG" == "zh" ]] && echo "1) Anthropic 官方 API（默认）" || echo "1) Anthropic official API (default)" ;;
    "prompt.provider_compatible") [[ "$LANG" == "zh" ]] && echo "2) Anthropic 兼容 API（代理/第三方网关）" || echo "2) Anthropic-compatible API (proxy/third-party gateway)" ;;
    "prompt.provider_choice") [[ "$LANG" == "zh" ]] && echo "请输入选择 [1-2]" || echo "Enter choice [1-2]" ;;
    "prompt.anthropic_key") [[ "$LANG" == "zh" ]] && echo "请输入模型 API 密钥（支持 Anthropic 兼容 API）" || echo "Enter your model API key (Anthropic-compatible)" ;;
    "prompt.anthropic_warn") [[ "$LANG" == "zh" ]] && echo "您选择了 Anthropic 官方 API，密钥通常以 'sk-ant-' 开头，请确认。" || echo "You selected Anthropic official API. Keys usually start with 'sk-ant-'; please double-check." ;;

    # Success messages
    "success.env_created") [[ "$LANG" == "zh" ]] && echo "已从 .env.example 创建 .env" || echo "Created .env from .env.example" ;;
    "success.anthropic_configured") [[ "$LANG" == "zh" ]] && echo "已配置模型 API 密钥" || echo "Model API key configured" ;;
    "success.anthropic_base_url") [[ "$LANG" == "zh" ]] && echo "已配置模型 API Base URL" || echo "Model API base URL configured" ;;
    "success.default_model") [[ "$LANG" == "zh" ]] && echo "已配置默认模型" || echo "Default model configured" ;;
    "success.s3_endpoint") [[ "$LANG" == "zh" ]] && echo "已配置 S3 公共端点" || echo "S3 public endpoint configured" ;;
    "success.bootstrap") [[ "$LANG" == "zh" ]] && echo "引导完成！" || echo "Bootstrap completed!" ;;

    # Info messages
    "info.anthropic_configured") [[ "$LANG" == "zh" ]] && echo "已配置模型 API 密钥" || echo "Model API key is configured" ;;
    "info.pulling_images") [[ "$LANG" == "zh" ]] && echo "正在拉取执行器镜像..." || echo "Pulling executor images..." ;;

    # Warnings
    "warn.docker_gid") [[ "$LANG" == "zh" ]] && echo "未检测到 DOCKER_GID；executor-manager 可能无法访问 docker.sock" || echo "DOCKER_GID not detected; executor-manager may fail to access docker.sock" ;;
    "warn.chown_failed") [[ "$LANG" == "zh" ]] && echo "chown RustFS 数据目录失败。您可能需要运行: sudo chown -R" || echo "Failed to chown RustFS data dir. You may need to run: sudo chown -R" ;;
    "warn.chmod_data_failed") [[ "$LANG" == "zh" ]] && echo "chmod RustFS 数据目录失败。您可能需要运行: sudo chown -R" || echo "Failed to chmod RustFS data dir. You may need to run: sudo chown -R" ;;
    "warn.chmod_workspace_failed") [[ "$LANG" == "zh" ]] && echo "chmod 工作空间目录失败。您可能需要运行: sudo chown -R" || echo "Failed to chmod workspace directories. You may need to run: sudo chown -R" ;;
    "warn.rustfs_init_failed") [[ "$LANG" == "zh" ]] && echo "rustfs-init 失败；您可以重试: docker compose --profile init up -d rustfs-init" || echo "rustfs-init failed; you can retry: docker compose --profile init up -d rustfs-init" ;;
    "warn.anthropic_not_set") [[ "$LANG" == "zh" ]] && echo "未设置模型 API Key（ANTHROPIC_API_KEY）！" || echo "Model API key is not set (ANTHROPIC_API_KEY)!" ;;
    "warn.default_model") [[ "$LANG" == "zh" ]] && echo "您选择了 Anthropic 官方 API，DEFAULT_MODEL 通常应以 'claude-' 开头，请确认模型 ID 是否正确。" || echo "You selected Anthropic official API. DEFAULT_MODEL usually starts with 'claude-'; please verify model ID." ;;

    # Language selection
    "lang.prompt") [[ "$LANG" == "zh" ]] && echo "请选择语言 / Please select language:" || echo "Please select language / 请选择语言:" ;;
    "lang.english") echo "1) English" ;;
    "lang.chinese") echo "2) 中文" ;;
    "lang.choice") [[ "$LANG" == "zh" ]] && echo "请输入选择 [1-2]" || echo "Enter choice [1-2]" ;;

    *) echo "$key" ;;
  esac
}

usage() {
  echo "$(msg "usage.header")"
  echo ""
  echo "$(msg "usage.options")"
  echo "$(msg "usage.interactive")"
  echo "$(msg "usage.non_interactive")"
  echo "$(msg "usage.no_start")"
  echo "$(msg "usage.force_env")"
  echo "$(msg "usage.llm_api_key")"
  echo "$(msg "usage.llm_base_url")"
  echo "$(msg "usage.model")"
  echo "$(msg "usage.anthropic_key")"
  echo "$(msg "usage.lang")"
  echo "$(msg "usage.help")"
  echo ""
  echo "$(msg "usage.advanced")"
  if [[ "$LANG" == "zh" ]]; then
    cat <<'ADVANCED'
  --data-dir PATH           RustFS 数据的主机路径（默认: ./oss_data）
  --workspace-dir PATH      工作空间的主机路径（默认: ./tmp_workspace）
  --rustfs-uid UID          数据目录所有权的 RustFS uid（默认: 10001）
  --rustfs-gid GID          数据目录所有权的 RustFS gid（默认: 10001）
  --no-chown-rustfs         跳过 RustFS 数据目录的 chown 操作
  --s3-bucket NAME          存储桶名称（写入环境文件）
  --s3-access-key KEY       S3 访问密钥（写入环境文件）
  --s3-secret-key KEY       S3 密钥（写入环境文件）
  --s3-public-endpoint URL  用于访问构件的 S3 公共端点（写入环境文件）
  --cors-origins CSV|JSON   允许的来源（写入环境文件）
  --docker-gid GID          Docker 套接字组 ID（如省略则自动检测）
  --env-file PATH           目标环境文件（默认: ./.env）
  --only-rustfs             仅启动 rustfs（和 rustfs-init）
  --no-init-bucket          跳过 rustfs-init 存储桶创建
  --no-pull-executor        跳过拉取执行器镜像
ADVANCED
  else
    cat <<'ADVANCED'
  --data-dir PATH           Host path for RustFS data (default: ./oss_data)
  --workspace-dir PATH      Host path for workspaces (default: ./tmp_workspace)
  --rustfs-uid UID          RustFS uid for data dir ownership (default: 10001)
  --rustfs-gid GID          RustFS gid for data dir ownership (default: 10001)
  --no-chown-rustfs         Skip chown for RustFS data dir
  --s3-bucket NAME          Bucket name (writes to env)
  --s3-access-key KEY       S3 access key (writes to env)
  --s3-secret-key KEY       S3 secret key (writes to env)
  --s3-public-endpoint URL  S3 public endpoint for artifact access (writes to env)
  --cors-origins CSV|JSON   Allowed origins (writes to env)
  --docker-gid GID          Docker socket group id (auto-detect if omitted)
  --env-file PATH           Target env file (default: ./.env)
  --only-rustfs             Start only rustfs (and rustfs-init)
  --no-init-bucket          Skip rustfs-init bucket creation
  --no-pull-executor        Skip pulling executor image
ADVANCED
  fi
  echo ""
  echo "$(msg "usage.examples")"
  echo "$(msg "usage.example1")"
  echo "  ./scripts/quickstart.sh"
  echo ""
  echo "$(msg "usage.example2")"
  echo "  ./scripts/quickstart.sh --no-start"
  echo ""
  echo "$(msg "usage.example3")"
  echo "  ./scripts/quickstart.sh --non-interactive --llm-api-key <your-key> --llm-base-url <base-url> --model <model-id>"
  echo ""
  echo "$(msg "usage.example4")"
  echo "  ./scripts/quickstart.sh --lang zh"
}

print_header() {
  local title="$1"
  echo ""
  echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${BLUE}  $title${NC}"
  echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo ""
}

print_success() {
  echo -e "${GREEN}[$(msg "print.success")]${NC} $*"
}

print_warn() {
  echo -e "${YELLOW}[$(msg "print.warn")]${NC} $*" >&2
}

print_error() {
  echo -e "${RED}[$(msg "print.error")]${NC} $*" >&2
}

print_info() {
  echo -e "${BLUE}[$(msg "print.info")]${NC} $*"
}

warn() {
  print_warn "$@"
}

read_line() {
  local var_name="$1"
  local value=""
  if [[ -r /dev/tty ]]; then
    IFS= read -r value < /dev/tty
  else
    IFS= read -r value
  fi
  printf -v "$var_name" '%s' "$value"
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    print_error "$(msg "error.missing_cmd"): $1"
    exit 1
  fi
}

resolve_path() {
  local path="$1"
  if [[ "$path" = /* ]]; then
    echo "$path"
  else
    echo "${ROOT_DIR}/${path#./}"
  fi
}

to_json_array() {
  local raw="$1"
  if [[ "$raw" == "["* ]]; then
    echo "$raw"
    return
  fi
  local IFS=','
  read -r -a parts <<< "$raw"
  local json="["
  local first=true
  for item in "${parts[@]}"; do
    item="${item## }"
    item="${item%% }"
    if [[ -z "$item" ]]; then
      continue
    fi
    if [[ "$first" = true ]]; then
      first=false
    else
      json+=","
    fi
    json+="\"$item\""
  done
  json+="]"
  echo "$json"
}

detect_docker_gid() {
  local sock="/var/run/docker.sock"
  if [[ ! -S "$sock" ]]; then
    return 1
  fi
  if stat -c "%g" "$sock" >/dev/null 2>&1; then
    stat -c "%g" "$sock"
    return
  fi
  if stat -f "%g" "$sock" >/dev/null 2>&1; then
    stat -f "%g" "$sock"
    return
  fi
  return 1
}

ensure_gitignore() {
  local dir="$1"
  local path="${dir}/.gitignore"
  if [[ ! -f "$path" ]]; then
    printf "*\n" > "$path"
  fi
}

read_env_key() {
  local key="$1"
  if [[ -f "$ENV_FILE" ]]; then
    local line
    line="$(grep -E "^[[:space:]]*${key}=" "$ENV_FILE" | tail -n 1 || true)"
    if [[ -n "$line" ]]; then
      local value="${line#*=}"
      value="${value%\"}"
      value="${value#\"}"
      value="${value%\'}"
      value="${value#\'}"
      # 将空值视为"未设置"
      if [[ -z "$value" ]]; then
        return 1
      fi
      # 将示例占位符视为"未设置"
      if [[ "$key" == "ANTHROPIC_API_KEY" && "$value" == "sk-ant-xxxxx" ]]; then
        return 1
      fi
      echo "$value"
      return 0
    fi
  fi
  return 1
}

anthropic_api_key_state() {
  if read_env_key "ANTHROPIC_API_KEY" >/dev/null 2>&1; then
    ec
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
