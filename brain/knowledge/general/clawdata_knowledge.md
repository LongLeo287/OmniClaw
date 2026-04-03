---
id: clawdata-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.775705
---

# KNOWLEDGE EXTRACT: clawdata
> **Extracted on:** 2026-03-30 17:33:18
> **Source:** clawdata

---

## File: `clawdata.md`
```markdown
# 📦 clawdata/clawdata [🔖 PENDING/APPROVE]
🔗 https://github.com/clawdata/clawdata


## Meta
- **Stars:** ⭐ 26 | **Forks:** 🍴 13
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Your own personal data engineer for OpenClaw.

## README (trích đầu)
```
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

All commands also have non-interactive variant
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

