---
id: clawdata
type: knowledge
owner: OA_Triage
---
# clawdata
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# ClawData

<p align="center">
  <img src="web/public/assets/shell.svg" alt="ClawData" width="120" />
</p>

An easy-to-use dashboard, CLI, and FastAPI backend for managing [OpenClaw](https://docs.openclaw.ai/) agents built for data teams. Spin up agents that understand your pipelines, query your warehouses, generate dbt models, review SQL, and more — from the web UI or the terminal. Built for data engineers and analysts who want AI assistance without leaving their stack.

## Screenshots

### Dashboard

Overview of your agents, system health, and quick actions.

![Home](web/public/assets/home.png)

### Chat

Talk to any agent directly. Switch agents, view connection status, and review conversation history.

![Chat](web/public/assets/chat.png)

### Agent Configuration

Set up agents with custom models, skills, and linked sub-agents.

![Agent Configuration](web/public/assets/agent_configure.png)

### Skills

Browse, enable, and install skills for your agents — databases, APIs, data tools, and more.

![Skills](web/public/assets/skills.png)

### Costing

Track token usage and estimated costs across all agents and sessions.

![Costing](web/public/assets/costing.png)

## Quick Start (Docker)

The fastest way to get running:

```bash
# Copy env and configure
cp .env.example .env
# Edit .env with your OpenClaw gateway token

# Start everything
docker compose up --build
```

This starts:
- **API** at http://localhost:8000 (FastAPI + OpenClaw gateway)
- **Web UI** at http://localhost:3000 (Next.js)

Data is persisted in Docker volumes (`clawdata-db`, `clawdata-userdata`).

To stop: `docker compose down` (add `-v` to also remove volumes/data).

## Quick Start (Local)

```bash
# Create venv and install
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Copy env and configure
cp .env.example .env
# Edit .env with your OpenClaw gateway token

# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd web
npm install
npm run dev
# Open http://localhost:3000
```

### CLI

ClawData includes an interactive CLI for managing agents and skills without the web UI:

```bash
# Launch the interactive menu
clawdata

# Or jump straight to a section
clawdata skills       # Toggle skills on/off per agent (↑↓ navigate, Space toggle, Enter confirm)
clawdata agents       # Browse, create, and configure agents
clawdata gateway      # Gateway health, logs, models, and providers
clawdata templates    # Browse project templates
clawdata status       # Quick system overview
clawdata setup        # Guided setup wizard
clawdata tui          # Launch the OpenClaw TUI
```

Skill management uses an interactive checklist — arrow keys to move, space bar to toggle, enter to apply:

```
  Skills for 🦞 main  (↑↓ navigate, Space toggle, Enter confirm)
> [x] Azure
  [ ] BigQuery
  [x] Data Analysis
  [x] Databricks Skill
  [ ] dbt
  [ ] DuckDB
  ...
```

All commands also have non-interactive variants for scripting:

```bash
clawdata skills list --project
clawdata skills deploy dbt --agent main
clawdata agents list --gateway
clawdata gateway health
```

## API Docs

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Architecture

See [PLAN.md](PLAN.md) for the full implementation plan.

## Project Layout

| Directory | Purpose |
|-----------|---------|
| `app/` | FastAPI application (routers, services, adapters) |
| `app/cli/` | Interactive CLI (`clawdata` command) |
| `templates/` | Jinja2 reference templates (dbt, airflow, sql) |
| `skills/` | Agent skill definitions (SKILL.md markdown) |
| `userdata/` | Agent workspaces (head agent + sub-agents) |
| `migrations/` | Alembic database migrations |
| `tests/` | Test suite |
| `web/` | Next.js 16 frontend (App Router, shadcn/ui) |

```

### File: skills\README.md
```md
# Skills

Data engineering skill definitions for OpenClaw agents. Each skill is a directory
containing a `SKILL.md` file following the
[AgentSkills](https://agentskills.io/) spec.

## Available Skills

| Skill | Description |
|-------|------------|
| `dbt-model-gen` | Generate dbt models from source definitions |
| `duckdb` | Query & explore a local DuckDB warehouse via CLI |
| `sql-reviewer` | Review SQL for best practices and anti-patterns |
| `airflow-dag-gen` | Generate Airflow DAGs from pipeline specs |
| `data-quality` | Add data quality checks to dbt models |

## Adding Skills

Create a new directory under `skills/` with a `SKILL.md` file containing YAML
frontmatter (`name`, `description`) and instructions for the agent.

```

### File: templates\README.md
```md
# Templates

Reference Jinja2 templates that agents can use when generating data engineering
artifacts. Organized by domain.

## Categories

| Category | Contents |
|----------|----------|
| `dbt/` | dbt model templates (staging, intermediate, mart), source/schema YAML |
| `airflow/` | Airflow DAG templates (basic, dbt-run, ELT pattern) |
| `azure/` | Azure Functions (HTTP & Event Hub triggers), Event Hub producer/consumer, streaming analytics pipeline |
| `databricks/` | PySpark notebooks, Delta Live Tables pipelines, job definitions, Unity Catalog setup |
| `sql/` | Raw SQL patterns (CREATE TABLE, SCD2 merge) |

## Usage

Templates are served via the API (`GET /api/templates`) and can be rendered with
variables (`POST /api/templates/{id}/render`). The agent can also read them
directly from the `templates/` directory using the `read` tool.

## Variables

Each template declares expected variables in its metadata. Use Jinja2 `{{ var }}`
syntax. Variables are validated at render time.

```

### File: entrypoint.sh
```sh
#!/bin/bash
set -e

# Run migrations
alembic upgrade head

# Start the FastAPI server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

```

### File: skills_DISTILLED.md
```md
---
id: skills
type: distilled_knowledge
---
# skills

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Skills

Data engineering skill definitions for OpenClaw agents. Each skill is a directory
containing a `SKILL.md` file following the
[AgentSkills](https://agentskills.io/) spec.

## Available Skills

| Skill | Description |
|-------|------------|
| `dbt-model-gen` | Generate dbt models from source definitions |
| `duckdb` | Query & explore a local DuckDB warehouse via CLI |
| `sql-reviewer` | Review SQL for best practices and anti-patterns |
| `airflow-dag-gen` | Generate Airflow DAGs from pipeline specs |
| `data-quality` | Add data quality checks to dbt models |

## Adding Skills

Create a new directory under `skills/` with a `SKILL.md` file containing YAML
frontmatter (`name`, `description`) and instructions for the agent.

```


```

### File: templates_DISTILLED.md
```md
---
id: templates
type: distilled_knowledge
---
# templates

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Templates

Reference Jinja2 templates that agents can use when generating data engineering
artifacts. Organized by domain.

## Categories

| Category | Contents |
|----------|----------|
| `dbt/` | dbt model templates (staging, intermediate, mart), source/schema YAML |
| `airflow/` | Airflow DAG templates (basic, dbt-run, ELT pattern) |
| `azure/` | Azure Functions (HTTP & Event Hub triggers), Event Hub producer/consumer, streaming analytics pipeline |
| `databricks/` | PySpark notebooks, Delta Live Tables pipelines, job definitions, Unity Catalog setup |
| `sql/` | Raw SQL patterns (CREATE TABLE, SCD2 merge) |

## Usage

Templates are served via the API (`GET /api/templates`) and can be rendered with
variables (`POST /api/templates/{id}/render`). The agent can also read them
directly from the `templates/` directory using the `read` tool.

## Variables

Each template declares expected variables in its metadata. Use Jinja2 `{{ var }}`
syntax. Variables are validated at render time.

```


```

### File: tests_DISTILLED.md
```md
---
id: tests
type: distilled_knowledge
---
# tests

## SWALLOW ENGINE DISTILLATION

### File: conftest.py
```py
"""Shared test fixtures."""

import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_clawdata.db"

engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSession = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestSession() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()

```

### File: test_agents.py
```py
"""Agent API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_agents_empty(client: AsyncClient):
    resp = await client.get("/api/agents/")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_and_get_agent(client: AsyncClient):
    payload = {
        "id": "test-head",
        "name": "Test Head Agent",
        "description": "A test agent",
        "role": "agent",
    }
    resp = await client.post("/api/agents/", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == "test-head"
    assert data["name"] == "Test Head Agent"
    assert data["is_active"] is True
    assert data["source"] == "local"

    # Get by ID
    resp = await client.get("/api/agents/test-head")
    assert resp.status_code == 200
    assert resp.json()["id"] == "test-head"


@pytest.mark.asyncio
async def test_create_duplicate_agent(client: AsyncClient):
    payload = {"id": "dup-agent", "name": "Dup"}
    await client.post("/api/agents/", json=payload)
    resp = await client.post("/api/agents/", json=payload)
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_update_agent(client: AsyncClient):
    await client.post("/api/agents/", json={"id": "upd-agent", "name": "Before"})
    resp = await client.patch("/api/agents/upd-agent", json={"name": "After"})
    assert resp.status_code == 200
    assert resp.json()["name"] == "After"


@pytest.mark.asyncio
async def test_delete_agent(client: AsyncClient):
    await client.post("/api/agents/", json={"id": "del-agent", "name": "Delete Me"})
    resp = await client.delete("/api/agents/del-agent")
    assert resp.status_code == 204

    resp = await client.get("/api/agents/del-agent")
    assert resp.status_code == 404

```

### File: test_chat.py
```py
"""Chat tests (WebSocket — requires OpenClaw to be running, skip by default)."""

import pytest


@pytest.mark.skip(reason="Requires a running OpenClaw gateway")
@pytest.mark.asyncio
async def test_chat_ws():
    """Placeholder — integration test for the chat WebSocket."""
    pass

```

### File: test_lifecycle.py
```py
"""Tests for the OpenClaw lifecycle management API."""

from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient

from app.schemas.lifecycle import (
    ActionResult,
    ConfigGetResponse,
    ConfigPatchResponse,
    DoctorResult,
    FullStatus,
    GatewayStartRequest,
    GatewayState,
    GatewayStatus,
    HealthResult,
    InstallResult,
    NodeStatus,
    NpmStatus,
    OnboardingStatus,
    OpenClawPackage,
    PrerequisiteStatus,
    UpdateResult,
)

LIFECYCLE = "app.services.openclaw_lifecycle"


# ── GET /api/openclaw/status ─────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_status(client: AsyncClient):
    mock_status = FullStatus(
        prerequisites=PrerequisiteStatus(
            node=NodeStatus(installed=True, version="22.11.0", meets_minimum=True),
            npm=NpmStatus(installed=True, version="10.9.2"),
            openclaw=OpenClawPackage(installed=True, version="2026.2.23"),
            ready=True,
        ),
        gateway=GatewayStatus(state=GatewayState.RUNNING, port=18789),
    )
    with patch(f"{LIFECYCLE}.get_full_status", new_callable=AsyncMock, return_value=mock_status):
        resp = await client.get("/api/openclaw/status")
    assert resp.status_code == 200
    data = resp.json()
    assert data["prerequisites"]["ready"] is True
    assert data["gateway"]["state"] == "running"


@pytest.mark.asyncio
async def test_get_status_not_installed(client: AsyncClient):
    mock_status = FullStatus(
        prerequisites=PrerequisiteStatus(ready=False),
        gateway=GatewayStatus(state=GatewayState.NOT_INSTALLED),
    )
    with patch(f"{LIFECYCLE}.get_full_status", new_callable=AsyncMock, return_value=mock_status):
        resp = await client.get("/api/openclaw/status")
    assert resp.status_code == 200
    assert resp.json()["gateway"]["state"] == "not_installed"
    assert resp.json()["prerequisites"]["ready"] is False


# ── GET /api/openclaw/onboarding ─────────────────────────────────────


@pytest.mark.asyncio
async def test_get_onboarding(client: AsyncClient):
    mock = OnboardingStatus(
        config_exists=True, workspace_exists=True,
        gateway_token_set=True, any_channel_configured=False,
        any_api_key_configured=True, onboarded=True,
    )
    with patch(f"{LIFECYCLE}.check_onboarding", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/onboarding")
    assert resp.status_code == 200
    assert resp.json()["onboarded"] is True


# ── POST /api/openclaw/install ───────────────────────────────────────


@pytest.mark.asyncio
async def test_install(client: AsyncClient):
    mock_result = InstallResult(success=True, version_installed="2026.2.23", message="Done")
    with patch(f"{LIFECYCLE}.install_openclaw", new_callable=AsyncMock, return_value=mock_result):
        resp = await client.post("/api/openclaw/install", json={"version": "latest"})
    assert resp.status_code == 200
    assert resp.json()["success"] is True
    assert resp.json()["version_installed"] == "2026.2.23"


@pytest.mark.asyncio
async def test_install_no_node(client: AsyncClient):
    mock_result = InstallResult(success=False, message="Node.js >= 22 required.")
    with patch(f"{LIFECYCLE}.install_openclaw", new_callable=AsyncMock, return_value=mock_result):
        resp = await client.post("/api/openclaw/install")
    assert resp.status_code == 200
    assert resp.json()["success"] is False


# ── POST /api/openclaw/update ────────────────────────────────────────


@pytest.mark.asyncio
async def test_update(client: AsyncClient):
    mock = UpdateResult(success=True, previous_version="2026.2.22", new_version="2026.2.23")
    with patch(f"{LIFECYCLE}.update_openclaw", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/update", json={"channel": "stable"})
    assert resp.status_code == 200
    assert resp.json()["new_version"] == "2026.2.23"


# ── POST /api/openclaw/start ────────────────────────────────────────


@pytest.mark.asyncio
async def test_start(client: AsyncClient):
    mock = ActionResult(success=True, message="Gateway started")
    with patch(f"{LIFECYCLE}.start_gateway", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/start", json={"port": 18789})
    assert resp.status_code == 200
    assert resp.json()["success"] is True


# ── POST /api/openclaw/stop ─────────────────────────────────────────


@pytest.mark.asyncio
async def test_stop(client: AsyncClient):
    mock = ActionResult(success=True, message="Gateway stopped.")
    with patch(f"{LIFECYCLE}.stop_gateway", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/stop")
    assert resp.status_code == 200
    assert resp.json()["success"] is True


# ── POST /api/openclaw/restart ──────────────────────────────────────


@pytest.mark.asyncio
async def test_restart(client: AsyncClient):
    mock = ActionResult(success=True, message="Gateway restarted.")
    with patch(f"{LIFECYCLE}.restart_gateway", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/restart")
    assert resp.status_code == 200
    assert resp.json()["success"] is True


# ── GET /api/openclaw/health ────────────────────────────────────────


@pytest.mark.asyncio
async def test_health(client: AsyncClient):
    mock = HealthResult(healthy=True, raw={"status": "ok"})
    with patch(f"{LIFECYCLE}.get_health", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/health")
    assert resp.status_code == 200
    assert resp.json()["healthy"] is True


# ── GET /api/openclaw/doctor ────────────────────────────────────────


@pytest.mark.asyncio
async def test_doctor(client: AsyncClient):
    mock = DoctorResult(success=True, issues=[], fixes_applied=[])
    with patch(f"{LIFECYCLE}.run_doctor", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/doctor")
    assert resp.status_code == 200
    assert resp.json()["success"] is True
    assert resp.json()["issues"] == []


@pytest.mark.asyncio
async def test_doctor_with_fix(client: AsyncClient):
    mock = DoctorResult(success=True, fixes_applied=["Fixed X"])
    with patch(f"{LIFECYCLE}.run_doctor", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/doctor?fix=true")
    assert resp.status_code == 200
    assert "Fixed X" in resp.json()["fixes_applied"]


# ── GET /api/openclaw/logs ──────────────────────────────────────────


@pytest.mark.asyncio
async def test_logs(client: AsyncClient):
    with patch(f"{LIFECYCLE}.get_logs", new_callable=AsyncMock, return_value="log line 1\nlog line 2"):
        resp = await client.get("/api/openclaw/logs?lines=50")
    assert resp.status_code == 200
    assert "log line 1" in resp.json()["output"]


# ── Config endpoints ────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_config(client: AsyncClient):
    mock = ConfigGetResponse(path="/home/.openclaw/openclaw.json", exists=True, config={"agent": {}})
    with patch(f"{LIFECYCLE}.get_config", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/config")
    assert resp.status_code == 200
    assert resp.json()["exists"] is True


@pytest.mark.asyncio
async def test_set_config(client: AsyncClient):
    new_conf = {"agent": {"model": "anthropic/claude-opus-4-6"}}
    mock = ConfigPatchResponse(success=True, config=new_conf, message="Config written.")
    with patch(f"{LIFECYCLE}.set_config", new_callable=AsyncMock, return_value=mock):
        resp = await client.put("/api/openclaw/config", json={"config": new_conf})
    assert resp.status_code == 200
    assert resp.json()["success"] is True


@pytest.mark.asyncio
async def test_patch_config(client: AsyncClient):
    patch_data = {"channels": {"whatsapp": {"allowFrom": ["+1555"]}}}
    mock = ConfigPatchResponse(success=True, config=patch_data, message="Config patched.")
    with patch(f"{LIFECYCLE}.patch_config", new_callable=AsyncMock, return_value=mock):
        resp = await client.patch("/api/openclaw/config", json={"patch": patch_data})
    assert resp.status_code == 200
    assert resp.json()["success"] is True

```

### File: test_skills.py
```py
"""Skill API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_skills_empty(client: AsyncClient):
    resp = await client.get("/api/skills/")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_skill(client: AsyncClient):
    payload = {
        "id": "test-skill",
        "name": "Test Skill",
        "description": "A test skill",
        "content": "---\nname: test-skill\ndescription: A test skill\n---\n\nDo the thing.\n",
    }
    resp = await client.post("/api/skills/", json=payload)
    assert resp.status_code == 201
    assert resp.json()["id"] == "test-skill"

```

### File: test_templates.py
```py
"""Template API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_templates_empty(client: AsyncClient):
    resp = await client.get("/api/templates/")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_and_render_template(client: AsyncClient):
    payload = {
        "id": "test-tpl",
        "name": "Test Template",
        "category": "sql",
        "description": "A test SQL template",
        "content": "SELECT * FROM {{ schema }}.{{ table }};",
        "variables": ["schema", "table"],
    }
    resp = await client.post("/api/templates/", json=payload)
    assert resp.status_code == 201

    # Render
    resp = await client.post(
        "/api/templates/test-tpl/render",
        json={"variables": {"schema": "public", "table": "users"}},
    )
    assert resp.status_code == 200
    assert resp.json()["rendered"] == "SELECT * FROM public.users;"

```

### File: __init__.py
```py

```


```

### File: tests\conftest.py
```py
"""Shared test fixtures."""

import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_clawdata.db"

engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSession = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestSession() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()

```

### File: tests\test_agents.py
```py
"""Agent API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_agents_empty(client: AsyncClient):
    resp = await client.get("/api/agents/")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_and_get_agent(client: AsyncClient):
    payload = {
        "id": "test-head",
        "name": "Test Head Agent",
        "description": "A test agent",
        "role": "agent",
    }
    resp = await client.post("/api/agents/", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == "test-head"
    assert data["name"] == "Test Head Agent"
    assert data["is_active"] is True
    assert data["source"] == "local"

    # Get by ID
    resp = await client.get("/api/agents/test-head")
    assert resp.status_code == 200
    assert resp.json()["id"] == "test-head"


@pytest.mark.asyncio
async def test_create_duplicate_agent(client: AsyncClient):
    payload = {"id": "dup-agent", "name": "Dup"}
    await client.post("/api/agents/", json=payload)
    resp = await client.post("/api/agents/", json=payload)
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_update_agent(client: AsyncClient):
    await client.post("/api/agents/", json={"id": "upd-agent", "name": "Before"})
    resp = await client.patch("/api/agents/upd-agent", json={"name": "After"})
    assert resp.status_code == 200
    assert resp.json()["name"] == "After"


@pytest.mark.asyncio
async def test_delete_agent(client: AsyncClient):
    await client.post("/api/agents/", json={"id": "del-agent", "name": "Delete Me"})
    resp = await client.delete("/api/agents/del-agent")
    assert resp.status_code == 204

    resp = await client.get("/api/agents/del-agent")
    assert resp.status_code == 404

```

### File: tests\test_chat.py
```py
"""Chat tests (WebSocket — requires OpenClaw to be running, skip by default)."""

import pytest


@pytest.mark.skip(reason="Requires a running OpenClaw gateway")
@pytest.mark.asyncio
async def test_chat_ws():
    """Placeholder — integration test for the chat WebSocket."""
    pass

```

### File: tests\test_lifecycle.py
```py
"""Tests for the OpenClaw lifecycle management API."""

from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient

from app.schemas.lifecycle import (
    ActionResult,
    ConfigGetResponse,
    ConfigPatchResponse,
    DoctorResult,
    FullStatus,
    GatewayStartRequest,
    GatewayState,
    GatewayStatus,
    HealthResult,
    InstallResult,
    NodeStatus,
    NpmStatus,
    OnboardingStatus,
    OpenClawPackage,
    PrerequisiteStatus,
    UpdateResult,
)

LIFECYCLE = "app.services.openclaw_lifecycle"


# ── GET /api/openclaw/status ─────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_status(client: AsyncClient):
    mock_status = FullStatus(
        prerequisites=PrerequisiteStatus(
            node=NodeStatus(installed=True, version="22.11.0", meets_minimum=True),
            npm=NpmStatus(installed=True, version="10.9.2"),
            openclaw=OpenClawPackage(installed=True, version="2026.2.23"),
            ready=True,
        ),
        gateway=GatewayStatus(state=GatewayState.RUNNING, port=18789),
    )
    with patch(f"{LIFECYCLE}.get_full_status", new_callable=AsyncMock, return_value=mock_status):
        resp = await client.get("/api/openclaw/status")
    assert resp.status_code == 200
    data = resp.json()
    assert data["prerequisites"]["ready"] is True
    assert data["gateway"]["state"] == "running"


@pytest.mark.asyncio
async def test_get_status_not_installed(client: AsyncClient):
    mock_status = FullStatus(
        prerequisites=PrerequisiteStatus(ready=False),
        gateway=GatewayStatus(state=GatewayState.NOT_INSTALLED),
    )
    with patch(f"{LIFECYCLE}.get_full_status", new_callable=AsyncMock, return_value=mock_status):
        resp = await client.get("/api/openclaw/status")
    assert resp.status_code == 200
    assert resp.json()["gateway"]["state"] == "not_installed"
    assert resp.json()["prerequisites"]["ready"] is False


# ── GET /api/openclaw/onboarding ─────────────────────────────────────


@pytest.mark.asyncio
async def test_get_onboarding(client: AsyncClient):
    mock = OnboardingStatus(
        config_exists=True, workspace_exists=True,
        gateway_token_set=True, any_channel_configured=False,
        any_api_key_configured=True, onboarded=True,
    )
    with patch(f"{LIFECYCLE}.check_onboarding", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/onboarding")
    assert resp.status_code == 200
    assert resp.json()["onboarded"] is True


# ── POST /api/openclaw/install ───────────────────────────────────────


@pytest.mark.asyncio
async def test_install(client: AsyncClient):
    mock_result = InstallResult(success=True, version_installed="2026.2.23", message="Done")
    with patch(f"{LIFECYCLE}.install_openclaw", new_callable=AsyncMock, return_value=mock_result):
        resp = await client.post("/api/openclaw/install", json={"version": "latest"})
    assert resp.status_code == 200
    assert resp.json()["success"] is True
    assert resp.json()["version_installed"] == "2026.2.23"


@pytest.mark.asyncio
async def test_install_no_node(client: AsyncClient):
    mock_result = InstallResult(success=False, message="Node.js >= 22 required.")
    with patch(f"{LIFECYCLE}.install_openclaw", new_callable=AsyncMock, return_value=mock_result):
        resp = await client.post("/api/openclaw/install")
    assert resp.status_code == 200
    assert resp.json()["success"] is False


# ── POST /api/openclaw/update ────────────────────────────────────────


@pytest.mark.asyncio
async def test_update(client: AsyncClient):
    mock = UpdateResult(success=True, previous_version="2026.2.22", new_version="2026.2.23")
    with patch(f"{LIFECYCLE}.update_openclaw", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/update", json={"channel": "stable"})
    assert resp.status_code == 200
    assert resp.json()["new_version"] == "2026.2.23"


# ── POST /api/openclaw/start ────────────────────────────────────────


@pytest.mark.asyncio
async def test_start(client: AsyncClient):
    mock = ActionResult(success=True, message="Gateway started")
    with patch(f"{LIFECYCLE}.start_gateway", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/start", json={"port": 18789})
    assert resp.status_code == 200
    assert resp.json()["success"] is True


# ── POST /api/openclaw/stop ─────────────────────────────────────────


@pytest.mark.asyncio
async def test_stop(client: AsyncClient):
    mock = ActionResult(success=True, message="Gateway stopped.")
    with patch(f"{LIFECYCLE}.stop_gateway", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/stop")
    assert resp.status_code == 200
    assert resp.json()["success"] is True


# ── POST /api/openclaw/restart ──────────────────────────────────────


@pytest.mark.asyncio
async def test_restart(client: AsyncClient):
    mock = ActionResult(success=True, message="Gateway restarted.")
    with patch(f"{LIFECYCLE}.restart_gateway", new_callable=AsyncMock, return_value=mock):
        resp = await client.post("/api/openclaw/restart")
    assert resp.status_code == 200
    assert resp.json()["success"] is True


# ── GET /api/openclaw/health ────────────────────────────────────────


@pytest.mark.asyncio
async def test_health(client: AsyncClient):
    mock = HealthResult(healthy=True, raw={"status": "ok"})
    with patch(f"{LIFECYCLE}.get_health", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/health")
    assert resp.status_code == 200
    assert resp.json()["healthy"] is True


# ── GET /api/openclaw/doctor ────────────────────────────────────────


@pytest.mark.asyncio
async def test_doctor(client: AsyncClient):
    mock = DoctorResult(success=True, issues=[], fixes_applied=[])
    with patch(f"{LIFECYCLE}.run_doctor", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/doctor")
    assert resp.status_code == 200
    assert resp.json()["success"] is True
    assert resp.json()["issues"] == []


@pytest.mark.asyncio
async def test_doctor_with_fix(client: AsyncClient):
    mock = DoctorResult(success=True, fixes_applied=["Fixed X"])
    with patch(f"{LIFECYCLE}.run_doctor", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/doctor?fix=true")
    assert resp.status_code == 200
    assert "Fixed X" in resp.json()["fixes_applied"]


# ── GET /api/openclaw/logs ──────────────────────────────────────────


@pytest.mark.asyncio
async def test_logs(client: AsyncClient):
    with patch(f"{LIFECYCLE}.get_logs", new_callable=AsyncMock, return_value="log line 1\nlog line 2"):
        resp = await client.get("/api/openclaw/logs?lines=50")
    assert resp.status_code == 200
    assert "log line 1" in resp.json()["output"]


# ── Config endpoints ────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_config(client: AsyncClient):
    mock = ConfigGetResponse(path="/home/.openclaw/openclaw.json", exists=True, config={"agent": {}})
    with patch(f"{LIFECYCLE}.get_config", new_callable=AsyncMock, return_value=mock):
        resp = await client.get("/api/openclaw/config")
    assert resp.status_code == 200
    assert resp.json()["exists"] is True


@pytest.mark.asyncio
async def test_set_config(client: AsyncClient):
    new_conf = {"agent": {"model": "anthropic/claude-opus-4-6"}}
    mock = ConfigPatchResponse(success=True, config=new_conf, message="Config written.")
    with patch(f"{LIFECYCLE}.set_config", new_callable=AsyncMock, return_value=mock):
        resp = await client.put("/api/openclaw/config", json={"config": new_conf})
    assert resp.status_code == 200
    assert resp.json()["success"] is True


@pytest.mark.asyncio
async def test_patch_config(client: AsyncClient):
    patch_data = {"channels": {"whatsapp": {"allowFrom": ["+1555"]}}}
    mock = ConfigPatchResponse(success=True, config=patch_data, message="Config patched.")
    with patch(f"{LIFECYCLE}.patch_config", new_callable=AsyncMock, return_value=mock):
        resp = await client.patch("/api/openclaw/config", json={"patch": patch_data})
    assert resp.status_code == 200
    assert resp.json()["success"] is True

```

### File: tests\test_skills.py
```py
"""Skill API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_skills_empty(client: AsyncClient):
    resp = await client.get("/api/skills/")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_skill(client: AsyncClient):
    payload = {
        "id": "test-skill",
        "name": "Test Skill",
        "description": "A test skill",
        "content": "---\nname: test-skill\ndescription: A test skill\n---\n\nDo the thing.\n",
    }
    resp = await client.post("/api/skills/", json=payload)
    assert resp.status_code == 201
    assert resp.json()["id"] == "test-skill"

```

### File: tests\test_templates.py
```py
"""Template API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_templates_empty(client: AsyncClient):
    resp = await client.get("/api/templates/")
    assert resp.status_code == 200
    assert resp.json() == []


@pytest.mark.asyncio
async def test_create_and_render_template(client: AsyncClient):
    payload = {
        "id": "test-tpl",
        "name": "Test Template",
        "category": "sql",
        "description": "A test SQL template",
        "content": "SELECT * FROM {{ schema }}.{{ table }};",
        "variables": ["schema", "table"],
    }
    resp = await client.post("/api/templates/", json=payload)
    assert resp.status_code == 201

    # Render
    resp = await client.post(
        "/api/templates/test-tpl/render",
        json={"variables": {"schema": "public", "table": "users"}},
    )
    assert resp.status_code == 200
    assert resp.json()["rendered"] == "SELECT * FROM public.users;"

```

### File: tests\__init__.py
```py

```

