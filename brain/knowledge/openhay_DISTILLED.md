---
id: openhay
type: knowledge
owner: OA_Triage
---
# openhay
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# OpenHay

<p align="center">
  <img src="./assets/logo-openhay.png" alt="OpenHay Logo" width="100"/>
</p>

<p align="center">
  <strong>An Vietnamese open-source, self-hostable implementation of a AI search and research platform.</strong>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit">
    <img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg" alt="Conventional Commits">
</p>

---

## Live Demo (Sadly, we shut it down...)

~Check out the live deployed version of OpenHay at https://www.openhay.vn~

---

## About The Project

[AIHay.vn](https://ai-hay.vn/) is a prominent Vietnamese startup that recently [raised over $10M in funding](https://news.tuoitre.vn/vietnamese-ai-startup-raises-10mn-in-series-a-funding-103250703165541286.htm) for its generative AI-powered knowledge platform.

**OpenHay** is an open-source implementation of its core features, developed by 2 engineers. The goal is to provide a powerful, self-hostable AI companion that is free to use for anyone with their own API keys, removing the need for a paid subscription.

## Core Features

-   **Q&A with Citations**: Delivers reliable, LLM-generated answers with citations extracted from web sources.
-   **Daily News Gathering**: An autonomous agent crawls predefined Vietnamese news sites, using an LLM to select and summarize the most significant articles. For technical details, see the [**Discover Agent README**](./backend/core/agents/discover/README.md).
-   **Deep Research Agent**: A hierarchical, multi-agent system for conducting in-depth, autonomous research. It parallelizes web investigation across multiple sub-agents and synthesizes their findings into a final, cited report. This system is optimized for performance and cost-efficiency using `gemini-3-flash-preview`. For a detailed architectural breakdown, read the [**Research Agent README**](./backend/core/agents/research/README.md).
-   **Translation**: Translates content from web links or uploaded documents (PDF, DOCX, etc.) while preserving context and technical terms.

## Getting Started

To deploy a local instance, follow the setup instructions in the respective directories:

-   **[Backend Setup](./backend/README.md)**
-   **[Frontend Setup](./frontend/README.md)**

The system operates on a "bring-your-own-key" model. You will need API keys for services like Google AI (for Gemini models), Brave API (for web search) which typically offer a free tier sufficient for personal use.

## Development & Support

Contributions are welcome.

### Contributing

This project enforces `pre-commit` and `conventional-commit` standards to maintain code quality and a structured commit history.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/NewFeature`).
3.  Install hooks: `pre-commit install`.
4.  Commit your changes with a conventional message (`git commit -m 'feat: Add NewFeature'`).
5.  Push to your branch (`git push origin feature/NewFeature`).
6.  Open a Pull Request.

### Code of Conduct

All contributors are expected to adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md).

### Support

For questions or issues, please contact:
-   **Primary Contact**: Quang Pham via [quangphamm1902@gmail.com](mailto:quangphamm1902@gmail.com).
-   **Issues**: Use the [GitHub Issues tracker](https://github.com/your-repo/openhay/issues) for bugs and feature requests.

## License

Distributed under the MIT License. See the `LICENSE` file for more information.

```

### File: backend\README.md
```md
# Backend for Open AI Hay

This is the backend for Open AI Hay, a FastAPI application that provides AI-powered features. It uses PostgreSQL for data storage and connects to various LLM providers.

## Local Development Setup

Follow these steps to get the backend running directly on your local machine without Docker.

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended for package management)
- A running PostgreSQL instance

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/open-ai-hay.git
cd open-ai-hay/backend
```

### 2. Install Dependencies

It's recommended to use a virtual environment.

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
uv sync --locked
```

### 3. Crawl4AI Setup (one-time)

Run the setup command once:

```bash
uv run crawl4ai-setup
```

If you later see Playwright/browser errors, install Chromium:

```bash
uv run playwright install --with-deps chromium
```

### 4. Configure Environment Variables

Create a `.env` file by copying the example file:

```bash
cp env.example .env
```

Now, open the `.env` file and fill in the required values. At a minimum, you must provide:

- `DATABASE_URL`
- `JWT_SECRET_KEY`
- The API key for your chosen `LLM_PROVIDER` (e.g., `GOOGLE_API_KEY`)

See the comments in the `.env.example` file for more details on each variable.

### 5. Database Setup

Ensure PostgreSQL is running and a database (e.g., `openhay`) exists. The app will create tables, extensions, and seed presets on first start.

For macOS with Homebrew:

```bash
# Install and start PostgreSQL
brew install postgresql@16
brew services start postgresql@16

# Create a default user and the database
createuser -s postgres || true
psql -U postgres -h 127.0.0.1 -p 5432 -c "ALTER USER postgres WITH PASSWORD 'postgres';"
createdb -U postgres -h 127.0.0.1 -p 5432 openhay
```

Set your database URL in `.env`:

```env
DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/openhay"
```

Optional: verify connectivity

```bash
psql "postgresql://postgres:postgres@localhost:5432/openhay" -c "SELECT 1;"
```

### 6. Run the Application

```bash
uv run uvicorn backend.api.main:app --reload --port 8000
```

The API will be available at `http://127.0.0.1:8000`.

## Architecture Overview

The backend is structured in a layered architecture to separate concerns. Here is a high-level overview of the request flow and component interaction:

```mermaid
graph TD
    subgraph User
        Client[Client / Frontend]
    end

    subgraph Backend Application
        API[API Layer<br>/api/routers]
        Services[Service Layer<br>/core/services]
        Agents[Agent Layer<br>/core/agents]
        Repositories[Data Access Layer<br>/core/repositories]
        DB[(PostgreSQL Database)]
    end

    subgraph External Services
        LLM[LLM Providers]
    end

    Client --> API
    API --> Services
    Services --> Agents
    Services --> Repositories
    Repositories --> DB
    Agents --> LLM

    style Client fill:#f9f,stroke:#333,stroke-width:2px
    style DB fill:#cff,stroke:#333,stroke-width:2px
    style LLM fill:#cff,stroke:#333,stroke-width:2px
```

The application leverages a few key libraries to handle complex tasks:

- **LLM Orchestration**: [pydantic-ai](https://github.com/pydantic/pydantic-ai) is used within the Agent Layer to orchestrate interactions with LLM providers, manage agentic workflows, and handle structured data parsing.
- **Observability**: [logfire](https://github.com/pydantic/logfire) is integrated for comprehensive logging and tracing, offering deep insights into request lifecycles and the behavior of LLM chains.

## Deployment on Railway

This project is configured to be deployed on [Railway](https://railway.app/) using the provided `Dockerfile`.

### 1. Create Project

- Create a new project on Railway and choose "Deploy from GitHub repo".
- Select your forked repository. Railway will automatically detect the `Dockerfile`.

### 2. Add a PostgreSQL Database

- Within your Railway project, add a new service and select "PostgreSQL".
- Railway will automatically provision a database and inject the `DATABASE_URL` environment variable into your application service.

### 3. Configure Environment Variables

- In your application service settings, go to the "Variables" tab.
- Add the required environment variables. You can copy them from your local `.env` file or reference `env.example`.
- Key variables to set include:
  - `JWT_SECRET_KEY`
  - `LLM_PROVIDER` and the corresponding API key (e.g., `GOOGLE_API_KEY`)
  - `BRAVE_API_KEY` (if used)
- **CORS Configuration**: To allow your frontend to communicate with the API, you need to configure CORS. Set the `HOST_URL` environment variable to your frontend's full URL (e.g., `https://my-frontend.up.railway.app`). If you have multiple domains, use `ALLOWED_ORIGINS` with a comma-separated list. Railway will automatically inject the `DATABASE_URL`.

### 4. Deployment

Railway will automatically build and deploy your application.

```

### File: frontend\package.json
```json
{
  "name": "vite_react_shadcn_ts",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "build:dev": "vite build --mode development",
    "lint": "eslint .",
    "preview": "vite preview",
    "start": "vite preview --host 0.0.0.0 --port $PORT",
    "start:caddy": "caddy run --config Caddyfile --adapter caddyfile"
  },
  "dependencies": {
    "@hookform/resolvers": "^3.10.0",
    "@radix-ui/react-accordion": "^1.2.11",
    "@radix-ui/react-alert-dialog": "^1.1.14",
    "@radix-ui/react-aspect-ratio": "^1.1.7",
    "@radix-ui/react-avatar": "^1.1.10",
    "@radix-ui/react-checkbox": "^1.3.2",
    "@radix-ui/react-collapsible": "^1.1.11",
    "@radix-ui/react-context-menu": "^2.2.15",
    "@radix-ui/react-dialog": "^1.1.14",
    "@radix-ui/react-dropdown-menu": "^2.1.15",
    "@radix-ui/react-hover-card": "^1.1.14",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-menubar": "^1.1.15",
    "@radix-ui/react-navigation-menu": "^1.2.13",
    "@radix-ui/react-popover": "^1.1.14",
    "@radix-ui/react-progress": "^1.1.7",
    "@radix-ui/react-radio-group": "^1.3.7",
    "@radix-ui/react-scroll-area": "^1.2.9",
    "@radix-ui/react-select": "^2.2.5",
    "@radix-ui/react-separator": "^1.1.7",
    "@radix-ui/react-slider": "^1.3.5",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-switch": "^1.2.5",
    "@radix-ui/react-tabs": "^1.1.12",
    "@radix-ui/react-toast": "^1.2.14",
    "@radix-ui/react-toggle": "^1.1.9",
    "@radix-ui/react-toggle-group": "^1.1.10",
    "@radix-ui/react-tooltip": "^1.2.7",
    "@tanstack/react-query": "^5.83.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "date-fns": "^3.6.0",
    "embla-carousel-react": "^8.6.0",
    "input-otp": "^1.4.2",
    "lucide-react": "^0.462.0",
    "next-themes": "^0.3.0",
    "react": "^18.3.1",
    "react-day-picker": "^8.10.1",
    "react-dom": "^18.3.1",
    "react-hook-form": "^7.61.1",
    "react-markdown": "^10.1.0",
    "react-resizable-panels": "^2.1.9",
    "react-router-dom": "^6.30.1",
    "recharts": "^2.15.4",
    "remark-gfm": "^4.0.1",
    "sonner": "^1.7.4",
    "tailwind-merge": "^2.6.0",
    "tailwindcss-animate": "^1.0.7",
    "vaul": "^0.9.9",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@eslint/js": "^9.32.0",
    "@tailwindcss/typography": "^0.5.16",
    "@types/node": "^22.16.5",
    "@types/react": "^18.3.23",
    "@types/react-dom": "^18.3.7",
    "@vitejs/plugin-react-swc": "^3.11.0",
    "autoprefixer": "^10.4.21",
    "eslint": "^9.32.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.20",
    "globals": "^15.15.0",
    "postcss": "^8.5.6",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.8.3",
    "typescript-eslint": "^8.38.0",
    "vite": "^5.4.19"
  }
}

```

### File: frontend\README.md
```md
## Frontend — Setup and Deployment

This guide covers setting up and deploying the Vite/React frontend.

---

### 1. Local Development

**Prerequisites:**
- Node.js (v18+)
- A running backend API

**Steps:**

1.  **Install Dependencies**
    Navigate to the frontend directory and install the required packages.
    ```bash
    cd frontend
    npm ci
    ```

2.  **Configure Environment**
    Create a `.env` file from the example and add your backend API URL.
    ```bash
    cp env.example .env
    ```
    Inside `.env`, set the following variable:
    ```env
    # Example for a local backend running on port 8000
    VITE_API_BASE=http://localhost:8000
    ```

3.  **Run the Development Server**
    Start the Vite dev server, which will be accessible at `http://localhost:8080`.
    ```bash
    npm run dev
    ```

---

### 2. Deploy to Railway

This project is configured to deploy automatically on Railway using Nixpacks and Caddy.

**Steps:**

1.  **Push to GitHub**
    Ensure your latest code is committed and pushed to your GitHub repository.

2.  **Create a New Railway Project**
    - In your Railway dashboard, select "New Project" and choose "Deploy from GitHub repo".
    - Select your repository.
    - When prompted for a service root, enter `frontend`.

3.  **Configure Service Variables**
    - In your new Railway service, go to the "Variables" tab.
    - Add the `VITE_API_BASE` variable and set it to your deployed backend's public URL.
    ```
    VITE_API_BASE=https://your-backend-service.up.railway.app
    ```
    Railway will automatically build and deploy the service. The build and start commands are defined in `nixpacks.toml` and do not need to be set manually.

4.  **Access Your Site**
    Once the deployment is complete, use the URL generated by Railway to access your live application.

```

### File: backend\api\main.py
```py
from __future__ import annotations

from contextlib import asynccontextmanager

import logfire
from backend.api.routers.auth import router as auth_router
from backend.api.routers.chat import router as chat_router
from backend.api.routers.contact import router as contact_router
from backend.api.routers.featured import router as featured_router
from backend.api.routers.health import router as health_router
from backend.api.routers.metrics import router as metrics_router
from backend.api.routers.research import router as research_router
from backend.api.routers.translate import router as translate_router
from backend.core.middleware import (
    APIRateLimitMiddleware,
    RequestSizeLimitMiddleware,
    SecurityHeadersMiddleware,
)
from backend.db import async_engine, create_all, seed_feature_presets
from backend.settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sqlalchemy import text


def _get_cors_origins() -> list[str]:
    # Allow localhost dev ports by default
    # Avoid '*' when allow_credentials is True
    origins: list[str] = []
    # Add Railway public domain if provided
    railway_domain = settings.railway_public_domain
    if railway_domain:
        origins.append(f"https://{railway_domain}")
    # Add explicit HOST_URL if provided
    host_url = settings.host_url
    if host_url:
        origins.append(host_url)
    # Optional comma-separated ALLOWED_ORIGINS env
    extra = settings.allowed_origins
    if extra:
        for item in extra.split(","):
            val = item.strip()
            if val:
                origins.append(val)
    # Normalize: strip trailing slashes and whitespace
    normalized: list[str] = []
    for o in origins:
        try:
            oo = o.strip().rstrip("/")
        except Exception:
            oo = o
        if oo:
            normalized.append(oo)
    # De-duplicate while preserving order
    seen = set()
    unique: list[str] = []
    for o in normalized:
        if o not in seen:
            unique.append(o)
            seen.add(o)

    logger.info(f"Allowed origins: {unique}")

    return unique


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Verify DB connectivity on startup; dispose engine on shutdown
    async with async_engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    # Ensure database schema and seeds are initialized (idempotent)
    await create_all()
    await seed_feature_presets()
    try:
        yield
    finally:
        await async_engine.dispose()


app = FastAPI(title="Open AI Hay API", lifespan=lifespan)

logfire.configure(
    token=settings.logfire_token,
    scrubbing=False,
    environment=settings.env,
    send_to_logfire="if-token-present",
)
logfire.instrument_fastapi(app)
logfire.instrument_pydantic_ai()

# Security and rate limiting middleware
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RequestSizeLimitMiddleware, max_size=10 * 1024 * 1024)
app.add_middleware(APIRateLimitMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Public routes
app.include_router(health_router)
app.include_router(auth_router)

# Protected routes
app.include_router(chat_router)
app.include_router(featured_router)
app.include_router(research_router)
app.include_router(translate_router)
app.include_router(contact_router)
app.include_router(metrics_router)


# Convenience for `uvicorn backend.api.main:app --reload`
__all__ = ["app"]

```

### File: backend\core\agents\discover\README.md
```md
# Discover Agent

The Discover Agent automates daily news gathering. It crawls a predefined list of Vietnamese news sources, uses an LLM to select the most relevant articles, and generates concise Vietnamese titles.

## Architecture

The agent processes each configured news source sequentially.

```mermaid
graph TD
    A[Start Daily Task] --> B{Read Sources from Config};
    B --> C{For each source};
    C --> D[1. Deep Crawl Website];
    D -- Crawled Pages --> E[2. Select Articles via LLM];
    E -- Selected Articles --> F{Append to Final List};
    C -- Loop --> G{Next Source};
    G --> C;
    F -- When all sources done --> H[Return All Selected Articles];

    subgraph "Article Selection"
      E --> E1{Truncate Content};
      E1 --> E2{Prompt LLM with Articles};
      E2 --> E3{LLM returns selected articles with new Vietnamese titles};
    end
```

### Workflow

1.  **Configuration**: The agent reads a list of target news websites from `discover_sources_config` in the settings. Each source configuration specifies the entry URL, crawl depth, page limits, and URL patterns.

    > **To add more news sources**, append a new source configuration to the `discover_sources_config` list in your `settings.py` file.

2.  **Deep Crawl**: For each source, the agent performs a deep crawl using a Breadth-First Search (BFS) strategy, collecting a pool of potential articles based on the configured URL patterns.

3.  **LLM-Powered Selection**: The crawled content is truncated and sent to the `discover_model` LLM, which selects the most significant articles based on a source-specific prompt.

4.  **Title Generation**: The LLM also generates a new, short, and engaging title in Vietnamese for each selected article.

5.  **Aggregation**: The selected articles are added to a final list. The agent then proceeds to the next configured source.

6.  **Completion**: Once all sources are processed, the agent returns a flat list of all selected articles, which is used to populate the "Daily Suggestions" feature.

```

### File: backend\core\agents\research\README.md
```md
# Research Agent

The Research Agent is an autonomous system designed for in-depth research. It uses a hierarchical, multi-agent architecture to parallelize information gathering and synthesis, producing a comprehensive, cited report for a given query.

## Architecture

The system comprises a **Lead Research Agent**, multiple **Sub-agents**, and a **Citation Agent**.

```mermaid
graph TD
    A[User Query] --> B{Lead Research Agent};
    B --> C{1. Create Research Plan};
    C --> D{2. Delegate Sub-Tasks};
    D -- task 1 --> E1[Sub-agent 1];
    D -- task 2 --> E2[Sub-agent 2];
    D -- ... --> En[Sub-agent N];

    subgraph Sub-agent Execution
        E1 --> F1{web_search};
        F1 --> G1{web_fetch};
        G1 --> H1[Generate Report 1];

        E2 --> F2{web_search};
        F2 --> G2{web_fetch};
        G2 --> H2[Generate Report 2];

        En --> Fn{web_search};
        Fn --> Gn{web_fetch};
        Gn --> Hn[Generate Report N];
    end

    H1 --> I{3. Synthesize Reports};
    H2 --> I;
    Hn --> I;
    I -- Final Report --> J{4. Citation Agent};
    J --> K[Final Report with Citations];

```

### Workflow

1.  **Planning**: The `Lead Research Agent` receives a user query and formulates a research plan, decomposing the topic into parallelizable sub-tasks.

2.  **Delegation**: The lead agent delegates each sub-task to an available `Sub-agent` with a detailed prompt.

3.  **Execution (Sub-agents)**: Each sub-agent operates independently in parallel. Its primary tools are:

    - `web_search`: Discovers relevant URLs.
    - `web_fetch`: Retrieves full content from discovered URLs.
      Each sub-agent produces a report summarizing its findings.

4.  **Synthesis**: The `Lead Research Agent` gathers the reports from all sub-agents and synthesizes them into a single, cohesive final report.

5.  **Citation**: The synthesized report and the history of fetched URLs are passed to the `Citation Agent`, which:
    - Attributes claims in the report to their sources.
    - Inserts inline numeric citations (e.g., `[1]`, `[2]`).
    - Generates a bibliography mapping citations to source URLs and titles.

This architecture ensures the final output is thorough, verifiable, and well-supported by evidence. The use of `gemini-3-flash-preview` optimizes for speed and cost.

```

### File: CODE_OF_CONDUCT.md
```md
[//]: # (This is a template, feel free to edit it!)

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

*   Demonstrating empathy and kindness toward other people
*   Being respectful of differing opinions, viewpoints, and experiences
*   Giving and gracefully accepting constructive feedback
*   Accepting responsibility and apologizing to those affected by our mistakes,
    and learning from the experience
*   Focusing on what is best not just for us as individuals, but for the overall
    community

Examples of unacceptable behavior include:

*   The use of sexualized language or imagery, and sexual attention or advances of
    any kind
*   Trolling, insulting or derogatory comments, and personal or political attacks
*   Public or private harassment
*   Publishing others' private information, such as a physical or email address,
    without their explicit permission
*   Other conduct which could reasonably be considered inappropriate in a
    professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
quangphamm1902@gmail.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interaction in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][faq]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[faq]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```

### File: llms-full.txt
```txt
# Open AI Hay API — Extended LLM Context

> FastAPI backend providing chat, research, and translation via pydantic-ai agents with SSE streaming, Brave web search + crawl4ai content extraction, and persistent conversation history with ownership checks.

## Overview

- Primary routes
  - /api/chat (list, stream chat, history)
  - /api/research (lead agent orchestrating parallel subagents; citations)
  - /api/translate/url, /api/translate/file (streamed translation)
  - /api/featured (daily curated items)
  - /api/metrics/* (aggregations over conversation runs)
  - /api/auth/* (token/guest/refresh/logout)
  - /api/contact/* (support, waitlist)
  - /healthz, /health, /health/detailed
- Authentication
  - Bearer JWT for: /api/chat, /api/research, /api/translate, /api/metrics/*
  - Tokens
    - POST /api/auth/token { identifier }
    - POST /api/auth/token/guest
    - POST /api/auth/refresh (refresh cookie rotates)
  - Ownership: conversations scoped via feature_params.user_id; enforced before access
- Rate limits (per IP)
  - /api/chat: 20/min; /api/research: 10/min; /api/translate: 30/min; default: 50/min
  - Provider RPM guard + provider-aware retries for LLM calls
- Streaming (SSE)
  - media_type: text/event-stream; charset=utf-8
  - Common events: ai_message, conversation_created, error
  - Chat extras: search_results, fetch_url_results
  - Research extras: lead_thinking, lead_answer, web_search_query, web_search_results, subagent_completed, final_report
- Agents and tools
  - chat_agent tools: search_web(query,n), fetch_url_content(urls)
  - research subagent tools: web_search(query,max_results), web_fetch(urls)
  - research lead deferred tool: run_parallel_subagents(prompts)
- Web discovery
  - Search: Brave API (requires BRAVE_API_KEY), shared 1.1s throttle process-wide
  - Crawl: crawl4ai markdown extraction (pruning filter; optional deep crawl)
- Persistence
  - ConversationMessageRun.messages stored as JSONB list of ModelMessage (bytes base64)
  - Runs appended chronologically; used as message_history
- Security & cache
  - Security headers added globally
  - /api/chat, /api/research, /api/translate responses: no-store, no-cache

## Request Schemas (concise)

- ChatRequest
```json
{
  "message": "string",
  "conversation_id": "UUID (optional)",
  "media": [
    { "data": "<base64>", "media_type": "image/png", "identifier": "optional" }
  ]
}
```

- ResearchRequest
```json
{
  "query": "string",
  "conversation_id": "UUID (optional)",
  "media": [ { "data": "<base64>", "media_type": "text/markdown" } ]
}
```

- TranslateURLRequest
```json
{
  "url": "https://example.com",
  "message": "Dịch sang tiếng Việt",
  "target_lang": "vi",
  "source_lang": "en (optional)",
  "conversation_id": "UUID (optional)"
}
```

- TranslateFileRequest
```json
{
  "message": "Translate this file",
  "target_lang": "vi",
  "source_lang": "auto (optional)",
  "media": [ { "data": "<base64>", "media_type": "application/pdf" } ],
  "conversation_id": "UUID (optional)"
}
```

- BinaryContentIn
```json
{ "data": "<base64>", "media_type": "string", "identifier": "string (optional)" }
```

## Streaming Event Examples (SSE)

- ai_message
```
event: ai_message
data: {"chunk": {"content": "Xin chào"}, "model": "google:gemini-3-flash-preview"}
```

- conversation_created
```
event: conversation_created
data: {"conversation_id": "2a2b0e5b-46f3-4e57-9f2c-0c4b0a0a7dcb"}
```

- error
```
event: error
data: {"error": "Chat execution error", "error_type": "RuntimeError", "details": "..."}
```

- search_results
```
event: search_results
data: {"results": [{"title": "...", "url": "https://...", "description": "...", "content": "...", "image_url": "..."}]}
```

- fetch_url_results
```
event: fetch_url_results
data: {"results": [{"url": "https://...", "title": "...", "description": "...", "content": "# extracted markdown...", "image_url": "..."}]}
```

- lead_thinking
```
event: lead_thinking
data: {"thinking": "...streamed internal reasoning..."}
```

- lead_answer
```
event: lead_answer
data: {"answer": "...partial final output with resolved [domain](https://url) markers..."}
```

- web_search_query
```
event: web_search_query
data: {"id": "tool_call_id", "index": 0, "query": "ai tin tức"}
```

- web_search_results
```
event: web_search_results
data: {"id": "tool_call_id", "index": 0, "results": [{"title": "...", "url": "https://...", "description": "..."}]}
```

- subagent_completed
```
event: subagent_completed
data: {}
```

- final_report
```
event: final_report
data: {"report": "...report text with [reuters](https://reuters.com/...) style links..."}
```

## Usage Examples (curl)

- Obtain token
```bash
curl -s -X POST https://<host>/api/auth/token \
  -H 'Content-Type: application/json' \
  -d '{"identifier":"user@example.com"}'
```

- Chat stream
```bash
curl -N -X POST https://<host>/api/chat \
  -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: application/json' \
  -d '{"message":"Xin chào"}'
```

- Research stream
```bash
curl -N -X POST https://<host>/api/research \
  -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: application/json' \
  -d '{"query":"Tóm tắt tình hình AI gần đây"}'
```

- Translate URL stream
```bash
curl -N -X POST https://<host>/api/translate/url \
  -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","message":"Dịch sang tiếng Việt","target_lang":"vi"}'
```

## Environment & Configuration

- Required: DATABASE_URL
- Important: JWT_SECRET_KEY (prod), BRAVE_API_KEY (web search), LOGFIRE_TOKEN (telemetry)
- LLM keys: GOOGLE_API_KEY / OPENAI_API_KEY / ANTHROPIC_API_KEY
- CORS: RAILWAY_PUBLIC_DOMAIN, HOST_URL, ALLOWED_ORIGINS
- Email: SMTP_* or RESEND_*; SUPPORT_* addresses
- Privacy: COLLECT_CLIENT_IP, ANALYTICS_IP_SALT

```

### File: llms.txt
```txt
# Open AI Hay API

> FastAPI backend providing chat, research, and translation via pydantic-ai agents with SSE streaming, web search/crawl tools (Brave + crawl4ai), and persistent conversation history with ownership checks.

Important notes:

- Primary routes:
  - /api/chat (list, stream chat, history)
  - /api/research (lead agent orchestrating parallel subagents, citations)
  - /api/translate/url, /api/translate/file (streamed translation)
  - /api/featured (daily curated items)
  - /api/metrics/* (aggregations over conversation runs)
  - /api/auth/* (token/guest/refresh/logout)
  - /api/contact/* (support, waitlist)
  - /healthz, /health, /health/detailed
- Authentication:
  - Bearer JWT required for: /api/chat, /api/research, /api/translate, /api/metrics/*
  - Get tokens:
    - POST /api/auth/token { identifier }
    - POST /api/auth/token/guest
    - POST /api/auth/refresh (refresh cookie rotates)
  - Ownership: conversations scoped via feature_params.user_id; enforced in protected routes
- Rate limits (per IP):
  - /api/chat: 20/min; /api/research: 10/min; /api/translate: 30/min; default: 50/min
  - Provider RPM guard via internal invoker with provider-aware retries
- Streaming:
  - Server-Sent Events (SSE), media_type: text/event-stream; charset=utf-8
  - Common events: ai_message, conversation_created, error
  - Chat extras: search_results, fetch_url_results
  - Research extras: lead_thinking, lead_answer, web_search_query, web_search_results, subagent_completed, final_report
- Minimal request shapes:
  - ChatRequest: { message: string; conversation_id?: UUID; media?: BinaryContentIn[] }
  - ResearchRequest: { query: string; conversation_id?: UUID; media?: BinaryContentIn[] }
  - TranslateURLRequest: { url: string; message: string; target_lang: string; source_lang?: string; conversation_id?: UUID }
  - TranslateFileRequest: { message: string; target_lang: string; source_lang?: string; media: BinaryContentIn[]; conversation_id?: UUID }
  - BinaryContentIn: { data: base64; media_type: string; identifier?: string }
- Agents and tools:
  - chat_agent tools: search_web(query,n), fetch_url_content(urls)
  - research subagent tools: web_search(query,max_results), web_fetch(urls)
  - research lead tool (deferred): run_parallel_subagents(prompts)
- Web discovery:
  - Search: Brave API (requires BRAVE_API_KEY), shared 1.1s throttle
  - Crawl: crawl4ai markdown extraction with pruning; optional deep crawl
- Persistence:
  - ConversationMessageRun.messages stored as JSONB (ModelMessage adapter; bytes base64)
  - History is appended chronologically and passed back to agents
- Security & cache:
  - Security headers added; /api/chat, /api/research, /api/translate responses are no-store/no-cache
- Examples (SSE):

```
# Chat stream
curl -N -X POST https://<host>/api/chat \
  -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: application/json' \
  -d '{"message":"Xin chào"}'

# Research stream
curl -N -X POST https://<host>/api/research \
  -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: application/json' \
  -d '{"query":"Tóm tắt tình hình AI gần đây"}'

# Translate URL stream
curl -N -X POST https://<host>/api/translate/url \
  -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","message":"Dịch sang tiếng Việt","target_lang":"vi"}'
```

Optional:

- LLM providers (defaults): google: gemini-3-flash-preview; research models also Gemini with thinking enabled
- Environment:
  - Required: DATABASE_URL
  - Important: JWT_SECRET_KEY (prod), BRAVE_API_KEY, LOGFIRE_TOKEN
  - Keys: GOOGLE_API_KEY / OPENAI_API_KEY / ANTHROPIC_API_KEY
  - CORS: RAILWAY_PUBLIC_DOMAIN, HOST_URL, ALLOWED_ORIGINS
  - Email: SMTP_* or RESEND_*; SUPPORT_* addresses
  - Privacy: COLLECT_CLIENT_IP, ANALYTICS_IP_SALT
- Answering guidelines:
  - Use chat vs research vs translate appropriately
  - Include auth in protected examples
  - Prefer original sources over aggregators; provide citations when using web content

```

### File: backend\.pre_commit_config.yaml
```yaml
repos:
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: "v0.12.0"
    hooks:
      - id: ruff
        args: [--fix]
        types_or: [python, pyi]
      - id: ruff-format
        types_or: [python, pyi]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: mixed-line-ending
        args: ["--fix=lf"]

  - repo: https://github.com/compilerla/conventional-pre-commit
    rev: v4.2.0
    hooks:
      - id: conventional-pre-commit
        stages: [commit-msg]
        args: [] # optional: list of Conventional Commits types to allow e.g. [feat, fix, ci, chore, test]

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
        args: ["--baseline", "backend/.secrets.baseline"]
        exclude: package.lock.json
        additional_dependencies: ["gibberish-detector"]

```

### File: backend\db.py
```py
from __future__ import annotations

import asyncio
from typing import AsyncGenerator

from backend.core.models import FeatureKey, FeaturePreset
from backend.settings import settings
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlmodel import SQLModel, select


def _to_async_url(url: str) -> str:
    # Normalize URL to async driver without forcing the user to change envs
    if url.startswith("postgresql+asyncpg://") or url.startswith("postgresql+psycopg://"):
        return url
    if url.startswith(("postgresql://", "postgres://")):
        return url.replace("postgresql://", "postgresql+psycopg://").replace(
            "postgres://", "postgresql+psycopg://"
        )
    return url


async_engine: AsyncEngine = create_async_engine(
    _to_async_url(settings.database_url),
    pool_pre_ping=True,
    connect_args={"options": "-c timezone=utc"},
)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, class_=AsyncSession
)


async def drop_all() -> None:
    """Drop all tables."""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)


async def create_all() -> None:
    # Ensure required extensions exist before creating tables
    async with async_engine.begin() as conn:
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS pgcrypto"))
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm"))
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent"))
        await conn.run_sync(SQLModel.metadata.create_all)
        # Create or replace trigger function to touch conversation.updated_at
        await conn.execute(
            text(
                """
                CREATE OR REPLACE FUNCTION touch_conversation_updated_at()
                RETURNS trigger AS $$
                BEGIN
                  UPDATE conversation SET updated_at = now()
                  WHERE id = NEW.conversation_id;
                  RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;
                """
            )
        )
        # Ensure triggers exist for both message and
        # conversation_message_run tables
        await conn.execute(
            text(
                """
                DROP TRIGGER IF EXISTS trg_message_touch_conversation
                ON message;
                CREATE TRIGGER trg_message_touch_conversation
                AFTER INSERT ON message
                FOR EACH ROW EXECUTE FUNCTION
                  touch_conversation_updated_at();
                """
            )
        )
        await conn.execute(
            text(
                """
                DROP TRIGGER IF EXISTS trg_conv_run_touch_conversation
                ON conversation_message_run;
                CREATE TRIGGER trg_conv_run_touch_conversation
                AFTER INSERT ON conversation_message_run
                FOR EACH ROW EXECUTE FUNCTION
                  touch_conversation_updated_at();
                """
            )
        )


async def seed_feature_presets() -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(FeaturePreset))
        existing = {fp.key for fp in result.scalars().all()}
        seeds = [
            FeaturePreset(
                key=FeatureKey.ai_tim_kiem,
                name="AI Tìm kiếm",
                system_prompt=(
                    "Bạn là trợ lý AI trả lời ngắn gọn, dẫn nguồn báo chí Việt Nam khi có."
                ),
                default_params={},
            ),
            FeaturePreset(
                key=FeatureKey.giai_bai_tap,
                name="Giải bài tập",
                system_prompt=("Bạn là trợ giảng giải thích từng bước, có ví dụ và kiểm tra lại."),
                default_params={"show_steps": True},
            ),
            FeaturePreset(
                key=FeatureKey.ai_viet_van,
                name="AI viết văn",
                system_prompt=("Bạn là biên tập viên viết tiếng Việt tự nhiên, mạch lạc."),
                default_params={"length": "medium", "tone": "trung_lap"},
            ),
            FeaturePreset(
                key=FeatureKey.dich,
                name="Dịch",
                system_prompt=("Bạn là dịch giả, giữ nguyên tên riêng và thuật ngữ."),
                default_params={
                    "source_lang": "vi",
                    "target_lang": "en",
                },
            ),
            FeaturePreset(
                key=FeatureKey.tom_tat,
                name="Tóm tắt",
                system_prompt=("Tóm tắt trọng tâm, có gạch đầu dòng."),
                default_params={"bullet_count": 5},
            ),
            FeaturePreset(
                key=FeatureKey.mindmap,
                name="Mindmap",
                system_prompt=("Trả về cấu trúc chủ đề dạng cây."),
                default_params={"max_depth": 3},
            ),
        ]

        new_items = [s for s in seeds if s.key not in existing]
        if new_items:
            session.add_all(new_items)
            await session.commit()
            print(f"Seeded {len(new_items)} feature presets.")
        else:
            print("Feature presets already present, skipping.")


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def main() -> None:
    print("Dropping existing tables...")
    await drop_all()
    print("Creating tables...")
    await create_all()
    print("Seeding presets...")
    await seed_feature_presets()
    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())

```

### File: backend\settings.py
```py
from typing import Literal, Optional

from dotenv import load_dotenv
from pydantic_ai.models import Model
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.google import GoogleModel, GoogleModelSettings
from pydantic_ai.models.openai import OpenAIModel
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    database_url: str

    # LLM Providers
    llm_provider: Literal["openai", "anthropic", "google", "ollama"] = "google"
    llm_model: str = "gemini-3-flash-preview"

    # For deep research
    lead_research_llm_model: str = "gemini-3-flash-preview"
    subagent_research_llm_model: str = "gemini-3-flash-preview"

    google_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None

    # Local LLM
    ollama_base_url: str = "http://localhost:11434/v1"
    ollama_model: str = "qwen3:8b"

    # Web Search
    brave_api_key: Optional[str] = None
    brave_search_url: str = "https://api.search.brave.com/res/v1/web/search"

    # Telemetry
    logfire_token: Optional[str] = None

    # SMTP / Support
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 465
    smtp_username: Optional[str] = None
    smtp_password: Optional[str] = None
    smtp_use_tls: bool = True
    support_owner_email: Optional[str] = None
    support_from_email: Optional[str] = None

    # Email provider (prod: use https provider like resend)
    email_provider: Literal["smtp", "resend"] = "smtp"
    resend_api_key: Optional[str] = None

    # Analytics / Privacy
    collect_client_ip: bool = True
    analytics_ip_salt: Optional[str] = None

    # Deployment / CORS
    host_url: Optional[str] = None
    railway_public_domain: Optional[str] = None
    # Comma-separated list of extra origins
    allowed_origins: Optional[str] = None

    # JWT Authentication
    jwt_secret_key: Optional[str] = None
    access_token_expire_days: int = 7
    guest_token_expire_hours: int = 24
    refresh_token_expire_days: int = 30

    # Environment
    env: Literal["prod", "dev"] = "prod"

    # Discover sources config
    discover_sources_config: list[dict] = [
        {
            "url": "https://kenh14.vn",
            # These will be used for crawl4ai deep crawling.
            # Adding more sites if needed.
            # More info: https://docs.crawl4ai.com/core/deep-crawling/#41-basic-url-pattern-filter
            "max_depth": 1,
            "max_pages": 50,
            "patterns": [
                r"^https?://(?:www\.)?kenh14\.vn/.+?-\d{17,18}\.chn$",
            ],
            "category": "Giải trí",
            "target_prompt": "Prioritize Genz-focused, viral content from Kenh14.vn, zeroing in on celebrity-centric news (Sao Việt, K-pop, Cbiz), showbiz scandals, and 'nóng trên mạng' trends. Select posts with high engagement potential, strong visuals, and a fast-paced, youth-oriented tone. Include fashion/beauty/lifestyle stories only if they feature major influencers or are globally trending. Strictly filter out hard news, politics, and serious social commentary unless directly tied to a major celebrity controversy.",
        },
        {
            "url": "https://vnexpress.net",
            "max_depth": 1,
            "max_pages": 50,
            "patterns": [
                ".html",
            ],
            "category": "Thời sự",
            "target_prompt": "Curate top-impact, breaking news from VnExpress focusing on Current Affairs (Thời sự), World (Thế giới), Business (Kinh doanh), and Law (Pháp luật). Prioritize articles with significant national or international implications, major policy changes, or market-moving business developments. Exclude soft news, local-only stories, sports, and entertainment unless of major national importance.",
        },
        {
            "url": "https://cafef.vn/thi-truong-chung-khoan.chn",
            "max_depth": 1,
            "max_pages": 50,
            "patterns": [
                r"^https?://(?:www\.)?cafef\.vn/.+?-\d{17,18}\.chn$",
            ],
            "category": "Chứng khoán",
            "target_prompt": "Select investment-critical articles from CafeF's stock market section. Focus on market analysis, macroeconomic trends affecting stocks, corporate earnings reports, M&A activities, and official announcements from listed companies. Prioritize deep analysis over simple price updates. Exclude general business news not directly tied to stock market performance.",
        },
        {
            "url": "https://genk.vn/ai.chn",
            "max_depth": 1,
            "max_pages": 50,
            "patterns": [
                r"^https?://(?:www\.)?genk\.vn/.+?-\d{17,18}\.chn$",
            ],
            "category": "AI & Công nghệ",
            "target_prompt": "From Genk's AI section, curate articles on significant AI advancements, new model releases, in-depth reviews of AI products/tools, and expert analysis of AI trends. Prioritize technical depth and practical application insights. Exclude brief news updates, rumors, and non-AI-related tech news.",
        },
    ]

    # RPM
    gemini_flash_rpm: int = 5
    gemini_pro_rpm: int = 3

    @property
    def model(self) -> Model:
        if self.llm_provider == "openai":
            return OpenAIModel(model_name=self.llm_model, provider="openai")
        elif self.llm_provider == "anthropic":
            return AnthropicModel(model_name=self.llm_model)
        elif self.llm_provider == "google":
            return GoogleModel(model_name=self.llm_model)
        elif self.llm_provider == "ollama":
            from pydantic_ai.providers.ollama import OllamaProvider

            assert self.ollama_base_url is not None, "OLLAMA_BASE_URL must be set to use Ollama"
            return OpenAIModel(
                model_name=self.llm_model,
                provider=OllamaProvider(base_url=self.ollama_base_url),
            )
        else:
            raise ValueError(f"Invalid LLM: {self.llm_provider}")

    @property
    def lead_research_model(self) -> Model:
        google_settings = GoogleModelSettings(
            google_thinking_config={
                "thinking_budget": 8096,
                "include_thoughts": True,
            }
        )
        return GoogleModel(
            model_name=self.subagent_research_llm_model,
            settings=google_settings,
        )

    @property
    def subagent_research_model(self) -> Model:
        google_settings = GoogleModelSettings(
            google_thinking_config={
                "thinking_budget": 2048,
                "include_thoughts": True,
            }
        )
        return GoogleModel(
            model_name=self.subagent_research_llm_model,
            settings=google_settings,
        )

    @property
    def discover_model(self) -> Model:
        google_settings = GoogleModelSettings(
            google_thinking_config={
                "thinking_budget": 4096,
                "include_thoughts": True,
            }
        )
        return GoogleModel(
            model_name=self.llm_model,
            settings=google_settings,
        )


settings = Settings()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
