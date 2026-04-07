---
id: queryweaver
type: knowledge
owner: OA_Triage
---
# queryweaver
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "dependencies": {
    "queryweaver-app": "file:app"
  },
  "devDependencies": {
    "@playwright/test": "^1.57.0",
    "@types/node": "^22.10.2",
    "playwright": "^1.57.0",
    "tailwindcss-animate": "^1.0.7"
  },
  "scripts": {}
}

```

### File: README.md
```md
<div align="center">  
  <h1>QueryWeaver (Text2SQL)</h1>

**REST API · MCP · Graph-powered** 

QueryWeaver is an **open-source Text2SQL** tool that converts plain-English questions into SQL using **graph-powered schema understanding**. It helps you ask databases natural-language questions and returns SQL and results.

Connect and ask questions: [![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white)](https://discord.gg/b32KEzMzce)

[![Try Free](https://img.shields.io/badge/Try%20Free-FalkorDB%20Cloud-FF8101?labelColor=FDE900&link=https://app.falkordb.cloud)](https://app.falkordb.cloud)
[![Dockerhub](https://img.shields.io/docker/pulls/falkordb/queryweaver?label=Docker)](https://hub.docker.com/r/falkordb/queryweaver/)
[![Tests](https://github.com/FalkorDB/QueryWeaver/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/FalkorDB/QueryWeaver/actions/workflows/tests.yml)
[![Swagger UI](https://img.shields.io/badge/API-Swagger-11B48A?logo=swagger&logoColor=white)](https://app.queryweaver.ai/docs)
</div>

![new-qw-ui-gif](https://github.com/user-attachments/assets/34663279-0273-4c21-88a8-d20700020a07)


## Get Started

### Docker

> 💡 Recommended for evaluation purposes (Local Python or Node are not required)
```bash
docker run -p 5000:5000 -it falkordb/queryweaver
```


Launch: http://localhost:5000

---

### Use an .env file (Recommended)

Create a local `.env` by copying `.env.example` and passing it to Docker. This is the simplest way to provide all required configuration:

```bash
cp .env.example .env
# edit .env to set your values, then:
docker run -p 5000:5000 --env-file .env falkordb/queryweaver
```

### Alternative: Pass individual environment variables

If you prefer to pass variables on the command line, use `-e` flags (less convenient for many variables):

```bash
docker run -p 5000:5000 -it \
  -e APP_ENV=production \
  -e FASTAPI_SECRET_KEY=your_super_secret_key_here \
  -e GOOGLE_CLIENT_ID=your_google_client_id \
  -e GOOGLE_CLIENT_SECRET=your_google_client_secret \
  -e GITHUB_CLIENT_ID=your_github_client_id \
  -e GITHUB_CLIENT_SECRET=your_github_client_secret \
  -e AZURE_API_KEY=your_azure_api_key \
  falkordb/queryweaver
```

> Note: QueryWeaver supports multiple AI providers. You can use `OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, or `AZURE_API_KEY`. See the [AI/LLM configuration](#aillm-configuration) section for details.

> For a full list of configuration options, consult `.env.example`.

## Memory TTL (optional)

QueryWeaver stores per-user conversation memory in FalkorDB. By default these graphs persist indefinitely. Set `MEMORY_TTL_SECONDS` to apply a Redis TTL (in seconds) so idle memory graphs are automatically cleaned up.

```bash
# Expire memory graphs after 1 week of inactivity
MEMORY_TTL_SECONDS=604800
```

The TTL is refreshed on every user interaction, so active users keep their memory.

## MCP server: host or connect (optional)

QueryWeaver includes optional support for the Model Context Protocol (MCP). You can either have QueryWeaver expose an MCP-compatible HTTP surface (so other services can call QueryWeaver as an MCP server), or configure QueryWeaver to call an external MCP server for model/context services.

What QueryWeaver provides
- The app registers MCP operations focused on Text2SQL flows:
   - `list_databases`
   - `connect_database`
   - `database_schema`
   - `query_database`

- To disable the built-in MCP endpoints set `DISABLE_MCP=true` in your `.env` or environment (default: MCP enabled).
- Configuration

- `DISABLE_MCP` — disable QueryWeaver's built-in MCP HTTP surface. Set to `true` to disable. Default: `false` (MCP enabled).

Examples

Disable the built-in MCP when running with Docker:

```bash
docker run -p 5000:5000 -it --env DISABLE_MCP=true falkordb/queryweaver
```

Calling the built-in MCP endpoints (example)
- The MCP surface is exposed as HTTP endpoints. 


### Server Configuration

Below is a minimal example `mcp.json` client configuration that targets a local QueryWeaver instance exposing the MCP HTTP surface at `/mcp`.

```json
{
   "servers": {
      "queryweaver": {
         "type": "http",
         "url": "http://127.0.0.1:5000/mcp",
         "headers": {
            "Authorization": "Bearer your_token_here"
         }
      }
   },
   "inputs": []
}
```

## REST API 

### API Documentation

Swagger UI: https://app.queryweaver.ai/docs

OpenAPI JSON: https://app.queryweaver.ai/openapi.json

### Overview

QueryWeaver exposes a small REST API for managing graphs (database schemas) and running Text2SQL queries. All endpoints that modify or access user-scoped data require authentication via a bearer token. In the browser the app uses session cookies and OAuth flows; for CLI and scripts you can use an API token (see `tokens` routes or the web UI to create one).

Core endpoints
- GET /graphs — list available graphs for the authenticated user
- GET /graphs/{graph_id}/data — return nodes/links (tables, columns, foreign keys) for the graph
- POST /graphs — upload or create a graph (JSON payload or file upload)
- POST /graphs/{graph_id} — run a Text2SQL chat query against the named graph (streaming response)

Authentication
- Add an Authorization header: `Authorization: Bearer <API_TOKEN>`

Examples

1) List graphs (GET)

curl example:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
   https://app.queryweaver.ai/graphs
```

Python example:

```python
import requests
resp = requests.get('https://app.queryweaver.ai/graphs', headers={'Authorization': f'Bearer {TOKEN}'})
print(resp.json())
```

2) Get graph schema (GET)

curl example:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
   https://app.queryweaver.ai/graphs/my_database/data
```

Python example:

```python
resp = requests.get('https://app.queryweaver.ai/graphs/my_database/data', headers={'Authorization': f'Bearer {TOKEN}'})
print(resp.json())
```

3) Load a graph (POST) — JSON payload

```bash
curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
   -d '{"database": "my_database", "tables": [...]}' \
   https://app.queryweaver.ai/graphs
```

Or upload a file (multipart/form-data):

```bash
curl -H "Authorization: Bearer $TOKEN" -F "file=@schema.json" \
   https://app.queryweaver.ai/graphs
```

4) Query a graph (POST) — run a chat-based Text2SQL request

The `POST /graphs/{graph_id}` endpoint accepts a JSON body with at least a `chat` field (an array of messages). The endpoint streams processing steps and the final SQL back as server-sent-message chunks delimited by a special boundary used by the frontend. For simple scripting you can call it and read the final JSON object from the streamed messages.

Example payload:

```json
{
   "chat": ["How many users signed up last month?"],
   "result": [],
   "instructions": "Prefer PostgreSQL compatible SQL"
}
```

curl example (simple, collects whole response):

```bash
curl -s -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
   -d '{"chat": ["Count orders last week"]}' \
   https://app.queryweaver.ai/graphs/my_database
```

Python example (stream-aware):

```python
import requests
import json

url = 'https://app.queryweaver.ai/graphs/my_database'
headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
with requests.post(url, headers=headers, json={"chat": ["Count orders last week"]}, stream=True) as r:
      # The server yields JSON objects delimited by a message boundary string
      boundary = '|||FALKORDB_MESSAGE_BOUNDARY|||'
      buffer = ''
      for chunk in r.iter_content(decode_unicode=True, chunk_size=1024):
            buffer += chunk
            while boundary in buffer:
                  part, buffer = buffer.split(boundary, 1)
                  if not part.strip():
                        continue
                  obj = json.loads(part)
                  print('STREAM:', obj)
```

Notes & tips
- Graph IDs are namespaced per-user. When calling the API directly use the plain graph id (the server will namespace by the authenticated user). For uploaded files the `database` field determines the saved graph id.
- The streaming response includes intermediate reasoning steps, follow-up questions (if the query is ambiguous or off-topic), and the final SQL. The frontend expects the boundary string `|||FALKORDB_MESSAGE_BOUNDARY|||` between messages.
- For destructive SQL (INSERT/UPDATE/DELETE etc) the service will include a confirmation step in the stream; the frontend handles this flow. If you automate destructive operations, ensure you handle confirmation properly (see the `ConfirmRequest` model in the code).


## Development

Follow these steps to run and develop QueryWeaver from source.

### Prerequisites

- Python 3.12+
- uv (Python package manager)
- A FalkorDB instance (local or remote)
- Node.js and npm (for the React frontend)

### Install and configure

Quickstart (recommended for development):

```bash
# Clone the repo
git clone https://github.com/FalkorDB/QueryWeaver.git
cd QueryWeaver

# Install dependencies (backend + frontend) and start the dev server
make install
make run-dev
```

If you prefer to set up manually or need a custom environment, use uv:

```bash
# Install Python (backend) and frontend dependencies
uv sync

# Create a local environment file
cp .env.example .env
# Edit .env with your values (set APP_ENV=development for local development)
```

### Run the app locally

```bash
uv run uvicorn api.index:app --host 0.0.0.0 --port 5000 --reload
```

The server will be available at http://localhost:5000

Alternatively, the repository provides Make targets for running the app:

```bash
make run-dev   # development server (reload, debug-friendly)
make run-prod  # production mode (ensure frontend build if needed)
```

### Frontend build (when needed)

The frontend is a modern React + Vite app in `app/`. Build before production runs or after frontend changes:

```bash
make install       # installs backend and frontend deps
make build-prod    # builds the frontend into app/dist/

# or manually
cd app
npm ci
npm run build
```

### OAuth configuration

QueryWeaver supports Google and GitHub OAuth. Create OAuth credentials for each provider and paste the client IDs/secrets into your `.env` file.

- Google: set authorized origin and callback `http://localhost:5000/login/google/authorized`
- GitHub: set homepage and callback `http://localhost:5000/login/github/authorized`

#### Environment-specific OAuth settings

For production/staging deployments, set `APP_ENV=production` or `APP_ENV=staging` in your environment to enable secure session cookies (HTTPS-only). This prevents OAuth CSRF state mismatch errors.

```bash
# For production/staging (enables HTTPS-only session cookies)
APP_ENV=production

# For development (allows HTTP session cookies)
APP_ENV=development
```

**Important**: If you're getting "mismatching_state: CSRF Warning!" errors on staging/production, ensure `APP_ENV` is set to `production` or `staging` to enable secure session handling.

### AI/LLM configuration

QueryWeaver supports multiple AI providers. Set one API key and QueryWeaver auto-detects which provider to use.

**Priority order:** Ollama > OpenAI > Gemini > Anthropic > Cohere > Azure (default)

| Provider | API Key | Default Models |
|----------|---------|----------------|
| Ollama | `OLLAMA_MODEL` | `ollama/<your-model>`, `ollama/nomic-embed-text` |
| OpenAI | `OPENAI_API_KEY` | `openai/gpt-4.1`, `openai/text-embedding-ada-002` |
| Google Gemini | `GEMINI_API_KEY` | `gemini/gemini-3-pro-preview`, `gemini/gemini-embedding-001` |
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic/claude-sonnet-4-5-20250929`, `voyage/voyage-3`* |
| Cohere | `COHERE_API_KEY` | `cohere/command-a-03-2025`, `cohere/embed-v4.0` |
| Azure OpenAI | `AZURE_API_KEY` | `azure/gpt-4.1`, `azure/text-embedding-ada-002` |

\* Anthropic has no native embeddings. You must set `VOYAGE_API_KEY` or `EMBEDDING_MODEL` for embeddings, otherwise startup will fail with an error.

**Optional: Override default models**

```bash
COMPLETION_MODEL=gemini/gemini-3-pro-preview
EMBEDDING_MODEL=gemini/gemini-embedding-001
```

Both must match your API key's provider.

#### Docker examples with AI configuration

Using OpenAI:
```bash
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e OPENAI_API_KEY=your_openai_api_key \
  falkordb/queryweaver
```

Using Google Gemini:
```bash
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e GEMINI_API_KEY=your_gemini_api_key \
  falkordb/queryweaver
```

Using Anthropic:
```bash
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e ANTHROPIC_API_KEY=your_anthropic_api_key \
  falkordb/queryweaver
```

Using Azure OpenAI:
```bash
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e AZURE_API_KEY=your_azure_api_key \
  -e AZURE_API_BASE=https://your-resource.openai.azure.com/ \
  -e AZURE_API_VERSION=2024-12-01-preview \
  falkordb/queryweaver
```

## Testing

> Quick note: many tests require FalkorDB to be available. Use the included helper to run a test DB in Docker if needed.

### Prerequisites

- Install dev dependencies: `uv sync`
- Start FalkorDB (see `make docker-falkordb`)
- Install Playwright browsers: `uv run playwright install`

### Quick commands

Recommended: prepare the development/test environment using the Make helper (installs dependencies and Playwright browsers):

```bash
# Prepare development/test environment (installs deps and Playwright browsers)
make setup-dev
```

Alternatively, you can run the E2E-specific setup script and then run tests manually:

```bash
# Prepare E2E test environment (installs browsers and other setup)
./setup_e2e_tests.sh

# Run all tests
make test

# Run unit tests only (faster)
make test-unit

# Run E2E tests (headless)
make test-e2e

# Run E2E tests with a visible browser for debugging
make test-e2e-headed
```

### Test types

- Unit tests: focus on individual modules and utilities. Run with `make test-unit` or `uv run python -m pytest tests/ -k "not e2e"`.
- End-to-end (E2E) tests: run via Playwright and exercise UI flows, OAuth, file uploads, schema processing, chat queries, and API endpoints. Use `make test-e2e`.

See `tests/e2e/README.md` for full E2E test instructions.

### CI/CD

GitHub Actions run unit and E2E tests on pushes and pull requests. Failures capture screenshots and artifacts for debugging.

## Troubleshooting

- FalkorDB connection issues: start the DB helper `make docker-falkordb` or check network/host settings.
- Playwright/browser failures: install browsers with `uv run playwright install` and ensure system deps are present.
- Missing environment variables: copy `.env.example` and fill required values.
- **OAuth "mismatching_state: CSRF Warning!" errors**: Set `APP_ENV=production` (or `staging`) in your environment for HTTPS deployments, or `APP_ENV=development` for HTTP develo
... [TRUNCATED]
```

### File: app\package.json
```json
{
  "name": "queryweaver-app",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "build:dev": "vite build --mode development",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@falkordb/canvas": "^0.0.44",
    "@hookform/resolvers": "^5.2.2",
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
    "@tanstack/react-query": "^5.90.21",
    "@types/d3": "^7.4.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "d3": "^7.9.0",
    "date-fns": "^3.6.0",
    "embla-carousel-react": "^8.6.0",
    "input-otp": "^1.4.2",
    "lucide-react": "^0.577.0",
    "next-themes": "^0.3.0",
    "preact": "^10.28.4",
    "react": "^18.3.1",
    "react-day-picker": "^8.10.1",
    "react-dom": "^18.3.1",
    "react-hook-form": "^7.71.2",
    "react-resizable-panels": "^2.1.9",
    "react-router-dom": "^7.13.1",
    "recharts": "^2.15.4",
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
    "autoprefixer": "^10.4.27",
    "eslint": "^9.32.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.20",
    "globals": "^17.3.0",
    "postcss": "^8.5.8",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.8.3",
    "typescript-eslint": "^8.57.0",
    "vite": "^7.3.0"
  },
  "overrides": {
    "glob": "^10.5.0"
  }
}

```

### File: app\README.md
```md
TypeScript frontend sources live in `app/ts/`.

Build (from repo root or `app` dir):

```bash
# from repo root
cd app
npm install
npm run build
```

This will bundle the frontend and place the result in `api/static/dist/bundle.js` which your FASTAPI templates should load via `/static/dist/bundle.js`.

Notes:
- Keep original JS files in `api/static/js/` for backward compatibility until you update templates.
- After verification you can remove `api/static/js/*` and the `api/static/ts/` copies.

```

### File: api\agents\README.md
```md
# Agents Module

This module contains various AI agents for the text2sql application. Each agent is responsible for a specific task in the query processing pipeline.

## Agents

### AnalysisAgent (`analysis_agent.py`)
- **Purpose**: Analyzes user queries and generates database analysis
- **Key Method**: `get_analysis()` - Analyzes user queries against database schema
- **Features**: Schema formatting, prompt building, conversation history tracking

### RelevancyAgent (`relevancy_agent.py`)
- **Purpose**: Determines if queries are relevant to the database schema
- **Key Method**: `get_answer()` - Assesses query relevancy against database description
- **Features**: Topic classification (On-topic, Off-topic, Inappropriate)

### FollowUpAgent (`follow_up_agent.py`)
- **Purpose**: Handles follow-up questions and conversational context
- **Key Method**: `get_answer()` - Processes follow-up questions using conversation history
- **Features**: Context awareness, data availability assessment

### TaxonomyAgent (`taxonomy_agent.py`)
- **Purpose**: Provides taxonomy classification and clarification for SQL queries
- **Key Method**: `get_answer()` - Generates clarification questions for SQL queries
- **Features**: WHERE clause analysis, user-friendly clarifications

### ResponseFormatterAgent (`response_formatter_agent.py`)
- **Purpose**: Formats SQL query results into user-readable responses
- **Key Method**: `format_response()` - Converts raw SQL results to natural language
- **Features**: Result formatting, operation type detection, user-friendly explanations

## Utilities

### utils.py
- **parse_response()**: Shared utility function for parsing JSON responses from AI models
- Used by multiple agents for consistent response parsing

## Usage

```python
from api.agents import AnalysisAgent, RelevancyAgent, ResponseFormatterAgent

# Initialize agents
analysis_agent = AnalysisAgent(queries_history, result_history)
relevancy_agent = RelevancyAgent(queries_history, result_history)
formatter_agent = ResponseFormatterAgent()

# Use agents
analysis = analysis_agent.get_analysis(query, tables, db_description)
relevancy = relevancy_agent.get_answer(question, database_desc)
response = formatter_agent.format_response(query, sql, results, db_description)
```

## Architecture

Each agent follows a consistent pattern:
1. **Initialization**: Set up with necessary context (history, configuration)
2. **Main Method**: Primary interface for the agent's functionality
3. **Helper Methods**: Private methods for internal processing
4. **Prompt Templates**: Stored as module-level constants for easy maintenance
5. **LLM Integration**: Uses litellm for AI model interactions

This modular structure improves:
- **Maintainability**: Each agent is self-contained
- **Testability**: Agents can be tested independently
- **Reusability**: Agents can be used in different contexts
- **Scalability**: New agents can be added without affecting existing ones

```

### File: AGENTS.md
```md
# AGENTS.md — QueryWeaver (Text2SQL)

## Project Overview

QueryWeaver is an open-source Text2SQL tool that converts natural-language questions into SQL using graph-powered schema understanding backed by FalkorDB. It is a full-stack monorepo with a Python/FastAPI backend (`api/`) and a React/TypeScript frontend (`app/`).

Repository: `FalkorDB/QueryWeaver`

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12+, FastAPI, Uvicorn |
| Frontend | React 18, TypeScript 5.8, Vite 7, Tailwind CSS |
| Graph DB | FalkorDB |
| LLM | LiteLLM (multi-provider: OpenAI, Gemini, Anthropic, Cohere, Azure, Ollama) |
| Auth | OAuth 2.0 (Google, GitHub) via authlib |
| Package mgmt | uv (Python), npm (Node) |
| Testing | pytest (unit), Playwright (E2E) |
| Linting | pylint (Python), ESLint (TypeScript) |
| CI/CD | GitHub Actions |

## Directory Structure

```
api/              Python backend (FastAPI)
  agents/         AI agents (analysis, healing, relevancy, follow-up)
  analyzers/      Code/syntax analyzers
  auth/           OAuth handlers, user management
  core/           Core text2sql logic, schema loading, errors
  entities/       Data models / DTOs
  loaders/        Database loaders (PostgreSQL, MySQL)
  memory/         Conversation memory management
  routes/         API endpoints (auth, graphs, database, tokens, settings)
  sql_utils/      SQL sanitization
  config.py       LLM provider detection, configuration
  app_factory.py  FastAPI app init, middleware
  index.py        Application entry point
app/              React + Vite frontend
  src/components/ React components
  src/contexts/   React contexts (Auth, Chat, Database, Settings)
  src/services/   API service layer
  src/types/      TypeScript type definitions
tests/            Unit tests (pytest)
e2e/              End-to-end tests (Playwright)
docs/             Documentation
.github/workflows/ CI/CD pipelines
```

## Quick Reference

### Install & Setup

```bash
make install          # uv sync + npm ci
make setup-dev        # install + Playwright browsers
cp .env.example .env  # configure environment
```

### Run

```bash
make run-dev          # dev server with hot reload (localhost:5000)
make run-prod         # production server
make docker-falkordb  # start FalkorDB in Docker
```

### Test

```bash
make test-unit        # pytest unit tests
make test-e2e         # Playwright E2E (headless)
make test-e2e-headed  # Playwright E2E (visible browser)
make test             # build + unit + E2E
```

### Lint

```bash
make lint             # pylint + ESLint
make lint-frontend    # ESLint only
```

### Build

```bash
make build-dev        # Vite dev build
make build-prod       # Vite production build
```

## Code Conventions

### Python (backend)

- PEP 8 with **120-char line limit**
- Type hints throughout
- pylint for linting (docstring checks disabled)
- FastAPI routers split by domain under `api/routes/`
- Custom exceptions in `api/core/errors.py` (GraphNotFoundError, InternalError, InvalidArgumentError)
- Middleware: CSRF (double-submit cookies), HSTS headers
- Environment config via dotenv; see `api/config.py` for defaults and provider detection
- Run backend: `uv run uvicorn api.index:app`

### TypeScript / React (frontend)

- Strict TypeScript
- ESLint with `@typescript-eslint`; unused vars prefixed with `_` are allowed
- State management via React Context API
- API calls through service layer (`app/src/services/`)
- Styling with Tailwind CSS + Radix UI primitives
- Routing with React Router v7
- Forms with React Hook Form + Zod validation
- Build tool: Vite (dev proxy to backend on port 5000)

### Testing

- **Unit tests** (`tests/`): pytest with markers `e2e`, `slow`, `auth`, `integration`, `unit`
- **E2E tests** (`e2e/`): Playwright with Page Object Model pattern; auth setup runs first
- E2E infra lives in `e2e/infra/`, page objects in `e2e/logic/pom/`
- Test data (SQL init scripts) in `e2e/test-data/`

## Environment Variables

Required:
- `FASTAPI_SECRET_KEY` — session secret
- `FALKORDB_URL` — FalkorDB connection string (e.g. `redis://localhost:6379/0`)

LLM provider (set one): `OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `COHERE_API_KEY`, `AZURE_API_KEY`, or `OLLAMA_MODEL`

Optional overrides: `COMPLETION_MODEL`, `EMBEDDING_MODEL` (must match provider)

See `.env.example` for the full list.

## CI/CD

GitHub Actions workflows (`.github/workflows/`):
- **tests.yml** — unit tests + lint on push/PR to main/staging
- **playwright.yml** — dedicated Playwright E2E suite
- **pylint.yml** — Python linting
- **spellcheck.yml** — docs spellcheck
- **publish-docker.yml** — build & push Docker image to DockerHub
- **dependency-review.yml** — dependency security review

## Branching

- `main` — production branch, target for PRs
- `staging` — integration branch

```

### File: CLAUDE.md
```md
AGENTS.md
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
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
info@falkordb.com.
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

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

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
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: package-lock.json
```json
{
  "name": "queryweaver",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "queryweaver-app": "file:app"
      },
      "devDependencies": {
        "@playwright/test": "^1.57.0",
        "@types/node": "^22.10.2",
        "playwright": "^1.57.0",
        "tailwindcss-animate": "^1.0.7"
      }
    },
    "app": {
      "name": "queryweaver-app",
      "version": "0.1.0",
      "dependencies": {
        "@falkordb/canvas": "^0.0.44",
        "@hookform/resolvers": "^5.2.2",
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
        "@tanstack/react-query": "^5.90.21",
        "@types/d3": "^7.4.3",
        "class-variance-authority": "^0.7.1",
        "clsx": "^2.1.1",
        "cmdk": "^1.1.1",
        "d3": "^7.9.0",
        "date-fns": "^3.6.0",
        "embla-carousel-react": "^8.6.0",
        "input-otp": "^1.4.2",
        "lucide-react": "^0.577.0",
        "next-themes": "^0.3.0",
        "preact": "^10.28.4",
        "react": "^18.3.1",
        "react-day-picker": "^8.10.1",
        "react-dom": "^18.3.1",
        "react-hook-form": "^7.71.2",
        "react-resizable-panels": "^2.1.9",
        "react-router-dom": "^7.13.1",
        "recharts": "^2.15.4",
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
        "autoprefixer": "^10.4.27",
        "eslint": "^9.32.0",
        "eslint-plugin-react-hooks": "^5.2.0",
        "eslint-plugin-react-refresh": "^0.4.20",
        "globals": "^17.3.0",
        "postcss": "^8.5.8",
        "tailwindcss": "^3.4.17",
        "typescript": "^5.8.3",
        "typescript-eslint": "^8.57.0",
        "vite": "^7.3.0"
      }
    },
    "app/node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "app/node_modules/@babel/runtime": {
      "version": "7.28.6",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "app/node_modules/@esbuild/linux-x64": {
      "version": "0.27.2",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "app/node_modules/@falkordb/canvas": {
      "version": "0.0.44",
      "license": "MIT",
      "dependencies": {
        "d3": "^7.9.0",
        "force-graph": "^1.44.4",
        "react": "^19.2.3"
      }
    },
    "app/node_modules/@falkordb/canvas/node_modules/react": {
      "version": "19.2.4",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "app/node_modules/@floating-ui/core": {
      "version": "1.7.3",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/utils": "^0.2.10"
      }
    },
    "app/node_modules/@floating-ui/dom": {
      "version": "1.7.4",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/core": "^1.7.3",
        "@floating-ui/utils": "^0.2.10"
      }
    },
    "app/node_modules/@floating-ui/react-dom": {
      "version": "2.1.6",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/dom": "^1.7.4"
      },
      "peerDependencies": {
        "react": ">=16.8.0",
        "react-dom": ">=16.8.0"
      }
    },
    "app/node_modules/@floating-ui/utils": {
      "version": "0.2.10",
      "license": "MIT"
    },
    "app/node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "app/node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "app/node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "license": "MIT"
    },
    "app/node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "app/node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "app/node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "app/node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "app/node_modules/@radix-ui/number": {
      "version": "1.1.1",
      "license": "MIT"
    },
    "app/node_modules/@radix-ui/primitive": {
      "version": "1.1.3",
      "license": "MIT"
    },
    "app/node_modules/@radix-ui/react-accordion": {
      "version": "1.2.12",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collapsible": "1.1.12",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-alert-dialog": {
      "version": "1.1.15",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dialog": "1.1.15",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-alert-dialog/node_modules/@radix-ui/react-slot": {
      "version": "1.2.3",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-compose-refs": "1.1.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-arrow": {
      "version": "1.1.7",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-aspect-ratio": {
      "version": "1.1.8",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.4"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-aspect-ratio/node_modules/@radix-ui/react-primitive": {
      "version": "2.1.4",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-slot": "1.2.4"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-avatar": {
      "version": "1.1.11",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-context": "1.1.3",
        "@radix-ui/react-primitive": "2.1.4",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-is-hydrated": "0.1.0",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-avatar/node_modules/@radix-ui/react-context": {
      "version": "1.1.3",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-avatar/node_modules/@radix-ui/react-primitive": {
      "version": "2.1.4",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-slot": "1.2.4"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-checkbox": {
      "version": "1.3.3",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-collapsible": {
      "version": "1.1.12",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "app/node_modules/@radix-ui/react-collection": {
      "version": "1.1.7",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional"
... [TRUNCATED]
```

### File: playwright.config.ts
```ts
import { defineConfig, devices } from '@playwright/test';

/**
 * Read environment variables from file.
 * https://github.com/motdotla/dotenv
 */
// import dotenv from 'dotenv';
// import path from 'path';
// dotenv.config({ path: path.resolve(__dirname, '.env') });

/**
 * See https://playwright.dev/docs/test-configuration.
 */
export default defineConfig({
  testDir: './e2e/tests',
  /* Run tests in files in parallel */
  fullyParallel: true,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* Serialize on CI — e2e specs share mutable backend/DB state */
  workers: process.env.CI ? 1 : undefined,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: 'html',
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('')`. */
    baseURL: process.env.BASE_URL || 'http://localhost:5000',

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'on-first-retry',

    /* Screenshot on failure */
    screenshot: 'only-on-failure',
  },

  /* Configure projects for major browsers */
  projects: [
    // Setup project to run before all tests
    {
      name: 'setup',
      testMatch: /.*\.setup\.ts/,
    },

    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        // Use saved authentication state
        storageState: 'e2e/.auth/user.json',
      },
      dependencies: ['setup'],
    },

    // Firefox is only run locally; skipped in CI to halve test time
    ...(!process.env.CI ? [{
      name: 'firefox',
      use: {
        ...devices['Desktop Firefox'],
        storageState: 'e2e/.auth/user.json',
      },
      dependencies: ['setup'],
    }] : []),

    // {
    //   name: 'webkit',
    //   use: { ...devices['Desktop Safari'] },
    // },

    /* Test against mobile viewports. */
    // {
    //   name: 'Mobile Chrome',
    //   use: { ...devices['Pixel 5'] },
    // },
    // {
    //   name: 'Mobile Safari',
    //   use: { ...devices['iPhone 12'] },
    // },

    /* Test against branded browsers. */
    // {
    //   name: 'Microsoft Edge',
    //   use: { ...devices['Desktop Edge'], channel: 'msedge' },
    // },
    // {
    //   name: 'Google Chrome',
    //   use: { ...devices['Desktop Chrome'], channel: 'chrome' },
    // },
  ],

  /* Run your local dev server before starting the tests */
  // webServer: {
  //   command: 'npm run start',
  //   url: 'http://localhost:3000',
  //   reuseExistingServer: !process.env.CI,
  // },
});

```

### File: SECURITY.md
```md
- [Security Policy](#security-policy)
  - [Supported Versions](#supported-versions)
  - [Reporting a Vulnerability](#reporting-a-vulnerability)

# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for
receiving such patches depends on the CVSS v3.0 Rating:

| CVSS v3.0 | Supported Versions                        |
| --------- | ----------------------------------------- |
| X.Y.Z     | Releases within the previous three months |
| X.Y.Z     | Most recent release                       |

## Reporting a Vulnerability

Please report (suspected) security vulnerabilities to
**[security@falkordb.com](mailto:security@falkordb.com)**. You will receive a response from
us within 48 hours. If the issue is confirmed, we will release a patch as soon
as possible depending on complexity but historically within a few days.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
