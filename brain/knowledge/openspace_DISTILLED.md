---
id: openspace
type: knowledge
owner: OA_Triage
---
# openspace
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

<picture>
    <img src="assets/logo.png" width="320px" style="border: none; box-shadow: none;" alt="OpenSpace Logo">
</picture>

## ✨ OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving ✨

| 🔋 **46% Fewer Tokens** | **💰 $11K earned in 6 Hours** | 🧬 **Self-Evolving Skills** | 🌐 **Agents Experience Sharing** |

[![Agents](https://img.shields.io/badge/Agents-Claude_Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20nanobot%20%7C%20...-99C9BF.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)
[![Feishu](https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=larksuite&logoColor=white)](./COMMUNICATION.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md)
[![中文文档](https://img.shields.io/badge/文档-中文版-F5C6C6?style=flat)](./README_CN.md)

**One Command to Evolve All Your AI Agents**: OpenClaw, nanobot, Claude Code, Codex, Cursor and etc.

<img src="assets/cli-typing.gif" width="500px" alt="openspace --query your task">

</div>

---

## 📢 News

- **2026-04-03** 🚀 Released **v0.1.0** — Skill quality monitoring: structural patterns extracted from high-quality skills now evaluate every new submission daily. Faster, more relevant cloud search. Production-grade vertical skill clusters emerging organically from the community. Frontend now supports Chinese (zh) i18n.
- **2026-04-02** ⚡ Cloud search upgraded for higher relevance and lower latency.
- **2026-03-31** 🛡️ Security hardening: hardened zip extraction and `import_skill` against path traversal. CLI now respects `OPENSPACE_MODEL` and `OPENSPACE_LLM_*` env vars; MiniMax compatibility; workflow ID collision fixes.
- **2026-03-29** 🔒 Pinned litellm to <1.82.7 to avoid PYSEC-2026-2 supply-chain attack.
- **2026-03-28** 🔧 Idempotent skill registration — `register_skill_dir` now returns existing `SkillMeta` for already-registered skills. Updated OpenClaw setup docs.
- **2026-03-27** 🪟 Fixed stdio deadlock on Windows; improved evolver confirmation parsing with stem-style keyword matching.
- **2026-03-26** 🌱 Dynamic skill directory re-scanning on each call, lightweight local skill search, and streamlined documentation.
- **2026-03-25** 🎉 OpenSpace is now open source!

---

## The Problem with Today's AI Agents

Today's AI agents — [OpenClaw](https://github.com/openclaw/openclaw), [nanobot](https://github.com/HKUDS/nanobot), [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [Cursor](https://cursor.com), etc. — are powerful, but they have a critical weakness: they never **Learn**, **Adapt**, and **Evolve** from real-world experience — let alone **Share** with each other.
- **❌ Massive Token Waste** - How to reuse successful task patterns instead of reasoning from scratch and burning tokens every time?
- **❌ Repeated Costly Failures** - How to share solutions across agents instead of repeating the same costly exploration and mistakes?
- **❌ Poor and Unreliable Skills** - How to maintain skill reliability as tools and APIs evolve — while ensuring community-contributed skills meet rigorous quality standards?

## 🎯 What is OpenSpace?

**🚀 🚀 The self-evolving engine where every task makes every agent smarter and more cost-efficient.**

https://github.com/user-attachments/assets/c50f70ab-f6db-47bf-9498-3210c0f0abae

OpenSpace plugs into any agent as skills and evolves it with three superpowers:

### 🧬 Self-Evolution
Skills that learn and improve themselves automatically
- ✅ **AUTO-FIX** — When a skill breaks, it fixes itself instantly
- ✅ **AUTO-IMPROVE** — Successful patterns become better skill versions
- ✅ **AUTO-LEARN** — Captures winning workflows from actual usage
- ✅ **Quality monitoring** — Tracks skill performance, error rates, and execution success across all tasks.

**Skills that continuously evolve — turning every failure into improvement, every success into optimization.**

### 🌐 Collective Agent Intelligence
Turn individual agents into a shared brain
- ✅ **Shared evolution**: One agent's improvement becomes every agent's upgrade
- ✅ **Network effects**: More agents → richer data → faster evolution for every agent
- ✅ **Easy sharing** — Upload and download evolved skills with one simple command
- ✅ **Access control** — Choose public, private, or team-only access for each skill

**One agent learns, all agents benefit — collective intelligence at scale.**

### 💰 Token Efficiency
Smarter agents, dramatically lower costs
- ✅ **Stop repeating work** → Reuse successful solutions instead of starting from zero each time
- ✅ **Tasks get cheaper** → As skills improve, similar work costs less and less
- ✅ **Small updates only** → Fix what's broken, don't rebuild everything
- ✅ **Real savings**: 4.2× better performance with 46% fewer tokens on real-world tasks, delivering measurable economic value. ([GDPVal](#-benchmark-gdpval))

Do more, spend less — agents that actually save you money over time.

---

### The Difference

**❌ Current Agents**
- Skills degrade silently as tools evolve
- Failed patterns repeat with no learning mechanism
- Knowledge remains trapped in individual agents

**✅ OpenSpace-Powered Agents**
- Multi-layer monitoring catches problems and auto-triggers repairs
- Successful workflows become reusable, shareable skills
- When one agent learns something useful, all agents get that knowledge instantly

### 📊 OpenSpace: Turn Your Agent into a Money-Making Coworker

**🎯 Real-World Results That Matter**
On 50 professional tasks (**📈 [GDPVal Economic Benchmark](#-benchmark-gdpval)**) across 6 industries, OpenSpace agents earn **4.2× more money** than baseline ([ClawWork](https://github.com/HKUDS/ClawWork)) agents using the same backbone LLM (Qwen 3.5-Plus). While cutting 46% of costly tokens through skill evolution.

<div align="center">
<img src="assets/benchmark_kpi.png" width="100%" alt="GDPVal Benchmark — Key Results" />
</div>

**💼 These Aren't Toy Problems**
- Building payroll calculators from complex union contracts
- Preparing tax returns from 15 scattered PDF documents
- Drafting legal memoranda on California privacy regulations
- Creating compliance forms and engineering specifications

**📈 Consistent Wins Across All Fields**
- Compliance work: +18.5% higher earnings
- Engineering projects: +8.7% better performance
- Professional documents: 56% fewer tokens needed
- Every category improved — no exceptions

<div align="center">
<img src="assets/benchmark_task_showcase.png" width="100%" alt="GDPVal Benchmark — Task Showcase by Category" />
</div>

**OpenSpace doesn't just make agents smarter** — it makes them economically viable. Real work, real money, measurable results.

## Use Case for Autonomous System Development with OpenSpace

**🖥️ [My Daily Monitor](showcase/README.md)** — OpenSpace empowers your agent to complete large-scale system development. This personal behavior monitoring system with 20+ live dashboard panels was built entirely by the agent — 60+ skills evolved from scratch through OpenSpace, demonstrating autonomous end-to-end software development capabilities.

<div align="center">
<img src="assets/my_daily_monitor_dark.png" width="100%" alt="My Daily Monitor – Dark Mode" />
</div>

---

## 📋 Table of Contents

- [⚡ Quick Start](#-quick-start)
  - [🤖 Path A: For Your Agent](#-path-a-for-your-agent)
  - [👤 Path B: As Your Co-Worker](#-path-b-as-your-co-worker)
  - [📊 Local Dashboard](#-local-dashboard)
- [📈 Benchmark: GDPVal](#-benchmark-gdpval)
- [📊 Showcase: My Daily Monitor](#-showcase-my-daily-monitor)
- [🏗️ Framework](#️-framework)
  - [🧬 Self-Evolution Engine](#-self-evolution-engine)
  - [🌐 Cloud Skill Community](#-cloud-skill-community)
- [🔧 Advanced Configuration](#-advanced-configuration)
- [📖 Code Structure](#-code-structure)
- [🤝 Contribute & Roadmap](#-contribute--roadmap)
- [🔗 Related Projects](#-related-projects)

---

## ⚡ Quick Start

🌐 **Just want to explore?** Browse community skills, evolution lineage at **[open-space.cloud](https://open-space.cloud)** — no installation needed.

```bash
git clone https://github.com/HKUDS/OpenSpace.git && cd OpenSpace
pip install -e .
openspace-mcp --help   # verify installation
```

> [!TIP]
> **Slow clone?** The `assets/` folder (~50 MB of images) makes the default clone large. Use this lightweight alternative to skip it:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/HKUDS/OpenSpace.git
> cd OpenSpace
> git sparse-checkout set '/*' '!assets/'
> pip install -e .
> ```

**Choose your path:**
- **[Path A](#-path-a-for-your-agent)** — Plug OpenSpace into your agent
- **[Path B](#-path-b-as-your-co-worker)** — Use OpenSpace directly as your AI co-worker

### 🤖 Path A: For Your Agent

Works with any agent that supports skills (`SKILL.md`) — [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [OpenClaw](https://github.com/openclaw/openclaw), [nanobot](https://github.com/HKUDS/nanobot), etc.

**① Add OpenSpace to your agent's MCP config:**

```json
{
  "mcpServers": {
    "openspace": {
      "command": "openspace-mcp",
      "toolTimeout": 600,
      "env": {
        "OPENSPACE_HOST_SKILL_DIRS": "/path/to/your/agent/skills",
        "OPENSPACE_WORKSPACE": "/path/to/OpenSpace",
        "OPENSPACE_API_KEY": "sk-xxx (optional, for cloud)"
      }
    }
  }
}
```

> [!TIP]
> Credentials (API key, model) are **auto-detected** from your agent's config; you usually don't need to set them manually.

**② Copy skills** into your agent's skills directory:

```bash
cp -r OpenSpace/openspace/host_skills/delegate-task/ /path/to/your/agent/skills/
cp -r OpenSpace/openspace/host_skills/skill-discovery/ /path/to/your/agent/skills/
```

Done. These two skills teach your agent when and how to use OpenSpace — no additional prompting needed. Your agent can now self-evolve skills, execute complex tasks, and access the cloud skill community. You can also add your own custom skills — see [`openspace/skills/README.md`](openspace/skills/README.md).

> [!NOTE]
> **Cloud community (optional):** Register at **[open-space.cloud](https://open-space.cloud)** to get a `OPENSPACE_API_KEY`, then add it to the `env` block above. Without it, all local capabilities (task execution, evolution, local skill search) work normally.

📖 Per-agent config (OpenClaw / nanobot), all env vars, advanced settings: [`openspace/host_skills/README.md`](openspace/host_skills/README.md)

### 👤 Path B: As Your Co-Worker

Use OpenSpace directly — coding, search, tool use, and more — with self-evolving skills and cloud community built in.

> [!NOTE]
> Create a `.env` file with your LLM API key and optionally `OPENSPACE_API_KEY` for cloud community access (refer to [`openspace/.env.example`](openspace/.env.example)).

```bash
# Interactive mode
openspace

# Execute task
openspace --model "anthropic/claude-sonnet-4-5" --query "Create a monitoring dashboard for my Docker containers"
```

Add your own custom skills: [`openspace/skills/README.md`](openspace/skills/README.md).

**Cloud CLI** — manage skills from the command line:

```bash
openspace-download-skill <skill_id>         # download a skill from the cloud
openspace-upload-skill /path/to/skill/dir   # upload a skill to the cloud
```

<details>
<summary><b>Python API</b></summary>

```python
import asyncio
from openspace import OpenSpace

async def main():
    async with OpenSpace() as cs:
        result = await cs.execute("Analyze GitHub trending repos and create a report")
        print(result["response"])

        for skill in result.get("evolved_skills", []):
            print(f"  Evolved: {skill['name']} ({skill['origin']})")

asyncio.run(main())
```

</details>

### 📊 Local Dashboard

See how your skills evolve — browse skills, track lineage, compare diffs.

> Requires **Node.js ≥ 20**.

```bash
# Terminal 1. Start backend API
openspace-dashboard --port 7788

# Terminal 2: Start frontend dev server
cd frontend
npm install        # only needed once
npm run dev    
```

📖 **Frontend setup guide**: [`frontend/README.md`](frontend/README.md)

<div align="center">
<table>
<tr>
<td width="50%"><img src="assets/frontend_1.gif" width="100%" alt="Skill Classes" /></td>
<td width="50%"><img src="assets/frontend_2.gif" width="100%" alt="Cloud Skill Records" /></td>
</tr>
<tr>
<td align="center"><sub>Skill Classes — Browse, Search & Sort</sub></td>
<td align="center"><sub>Cloud — Browse & Discover Skill Records</sub></td>
</tr>
<tr>
<td width="50%"><img src="assets/frontend_3.gif" width="100%" alt="Version Lineage" /></td>
<td width="50%"><img src="assets/frontend_4.gif" width="100%" alt="Workflow Sessions" /></td>
</tr>
<tr>
<td align="center"><sub>Version Lineage — Skill Evolution Graph</sub></td>
<td align="center"><sub>Workflow Sessions — Execution History & Metrics</sub></td>
</tr>
</table>
</div>

---

## 📈 Benchmark: GDPVal

We evaluate OpenSpace on [GDPVal](https://huggingface.co/datasets/openai/gdpval) — 220 real-world professional tasks spanning 44 occupations — using the [ClawWork](https://github.com/HKUDS/ClawWork) evaluation protocol with identical productivity tools and LLM-based scoring. Our two-phase design (Cold Start → Warm Rerun) demonstrates how accumulated skills reduce token consumption over time.

Fair Benchmark: OpenSpace uses Qwen 3.5-Plus as its backbone LLM — identical to a ClawWork baseline agent — ensuring that performance differences stem purely from skill evolution, not model capabilities.

Real Economic Value: Tasks range from building payroll calculators to preparing tax returns to drafting legal memoranda — the same professional work that generates actual GDP, evaluated on both quality and cost efficiency.

<div align="center">
<img src="assets/benchmark_income.png" width="100%" alt="GDPVal Benchmark — Income Comparison" />
</div>

- **4.2× Higher Income** vs ClawWork with the same backbone LLM (Qwen 3.5-Plus)
- **72.8% Value Capture** — $11,484 earned out of $15,764 task value, outperforming all agents
- **70.8% Average Quality** — +30pp above the best ClawWork agent (40.8%)
− **45.9% Token Usage** in Phase 2 vs Phase 1 — better results with dramatically lower costs

<div align="center">
<img src="assets/benchmark_quality_tokens.png" width="100%" alt="GDPVal Benchmark — Quality & Token Efficiency" />
</div>

### What Real-World Tasks Can OpenSpace Handle?

The 50 GDPVal tasks span 6 real-world work categories. 
- **Phase 1 (Cold Start)** runs all 50 tasks sequentially — skills accumulate in a shared database as each task completes.
- **Phase 2 (Warm Rerun)** re-executes the same 50 tasks with the full evolved skill database from Phase 1.

Income Capture = actual payment earned ÷ maximum possible task value

<div align="center">
<img src="assets/benchmark_task_showcase.
... [TRUNCATED]
```

### File: requirements.txt
```txt
# OpenSpace core dependencies
litellm>=1.70.0,<1.82.7  # pinned to avoid PYSEC-2026-2 supply-chain compromise (1.82.7/1.82.8 were malicious)
python-dotenv>=1.0.0
openai>=1.0.0
jsonschema>=4.25.0
mcp>=1.0.0
anthropic>=0.71.0
pillow>=12.0.0
numpy>=1.24.0
colorama>=0.4.6

# Local server dependencies (cross-platform)
flask>=3.1.0
pyautogui>=0.9.54
pydantic>=2.12.0
requests>=2.32.0

# # macOS-specific dependencies (local server)
# pyobjc-core>=12.0; sys_platform == 'darwin'
# pyobjc-framework-cocoa>=12.0; sys_platform == 'darwin'
# pyobjc-framework-quartz>=12.0; sys_platform == 'darwin'
# atomacos>=3.2.0; sys_platform == 'darwin'

# # Linux-specific dependencies (local server)
# python-xlib>=0.33; sys_platform == 'linux'
# pyatspi>=2.38.0; sys_platform == 'linux'

# # Windows-specific dependencies (local server)
# pywinauto>=0.6.8; sys_platform == 'win32'
# pywin32>=306; sys_platform == 'win32'
# PyGetWindow>=0.0.9; sys_platform == 'win32'

```

### File: frontend\package.json
```json
{
  "name": "openspace-frontend",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite --port 3789",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.7.9",
    "i18next": "^26.0.3",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-force-graph-2d": "^1.25.4",
    "react-i18next": "^17.0.2",
    "react-router-dom": "^7.1.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.4",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17",
    "typescript": "~5.6.2",
    "vite": "^6.0.3"
  }
}

```

### File: frontend\README.md
```md
# OpenSpace Frontend

A dashboard frontend for the OpenSpace, providing skill browsing, lineage visualization, and workflow inspection.

## Prerequisites

- **Node.js ≥ 20**

## First-time Setup

1. **Copy the environment file**

```bash
cd frontend
cp .env.example .env
```

Edit `.env` if your backend runs on a different host/port:

```dotenv
VITE_HOST=127.0.0.1
VITE_PORT=3888
VITE_API_PROXY_TARGET=http://127.0.0.1:7788
VITE_API_BASE_URL=/api/v1
```

2. **Install dependencies**

```bash
npm install
```

3. **Start the backend** (in a separate terminal)

```bash
# option A – CLI entry point
openspace-dashboard --host 127.0.0.1 --port 7788

# option B – from the repo root
python -m openspace.dashboard_server --host 127.0.0.1 --port 7788
```

> Requires Python ≥ 3.12 with `flask` installed.

4. **Start the frontend**

```bash
npm run dev
```

The dev server will be available at `http://127.0.0.1:3888` (or whatever `VITE_PORT` you set).

## Subsequent Starts

Once `.env` is configured and dependencies are installed, you only need:

```bash
# terminal 1 – backend
openspace-dashboard --host 127.0.0.1 --port 7788

# terminal 2 – frontend
cd frontend
npm run dev
```

## Default URLs

| Service             | URL                      |
| ------------------- | ------------------------ |
| Frontend dev server | `http://127.0.0.1:3888`  |
| Dashboard API       | `http://127.0.0.1:7788`  |

## Advanced Configuration

### Bypass the Vite proxy

If you prefer to call the backend directly (e.g. for debugging), you can set `VITE_API_BASE_URL` to the full backend URL:

```bash
VITE_API_BASE_URL=http://127.0.0.1:7788/api/v1 npm run dev
```

## Production Build

```bash
cd frontend
npm run build
```

After building, start the backend and it will serve `frontend/dist` as static files automatically — no need to run the dev server.

## Main Pages

- **Dashboard** – overall health, pipeline stages, top skills, recent workflows
- **Skills** – searchable skill list and score breakdown
- **Skill Detail** – source preview, lineage graph, scoring metrics, recent analyses
- **Workflows** – recorded workflow sessions from `logs/recordings` and `logs/trajectories`
- **Workflow Detail** – timeline, artifacts, metadata, selected skills, plans, and decisions

```

### File: showcase\README.md
```md
<div align="center">

# 🖥️ My Daily Monitor

### **Your Entire Day on One Live Screen — with an AI Agent That Works for You**

**Fully generated & evolved by [OpenSpace](https://github.com/HKUDS/OpenSpace) — zero human code**

<p>
<a href="https://github.com/HKUDS/OpenSpace"><img src="https://img.shields.io/badge/Built_with-OpenSpace-99C9BF.svg" alt="Built with OpenSpace" /></a>
<img src="https://img.shields.io/badge/TypeScript-Vanilla_TS-FCE7D6.svg" alt="TypeScript" />
<img src="https://img.shields.io/badge/Bundler-Vite-C1E5F5.svg" alt="Vite" />
</p>

<img src="../assets/my_daily_monitor_dark.png" width="90%" alt="My Daily Monitor – Dark Mode" />

<sub>Dark Mode</sub>&nbsp;&nbsp;&nbsp;&nbsp;

<details>
<summary>Light Mode</summary>
<img src="../assets/my_daily_monitor_light.png" width="90%" alt="My Daily Monitor – Light Mode" />
</details>

</div>

## Table of Contents

- [What is My Daily Monitor?](#-what-is-my-daily-monitor)
- [Quick Start](#-quick-start)
- [How Was It Generated?](#-how-was-it-generated--openspace-skill-evolution)
- [Project Structure](#%EF%B8%8F-project-structure)
- [Related](#-related)

---

## 📖 What is My Daily Monitor?

**My Daily Monitor** is an always-on **live** dashboard that streams your processes, servers, terminals, news, markets, messages, and schedules into one screen — with a built-in AI agent that can answer questions, provide analysis, and get work done for you.

### 🔑 Why It Matters

- **🖥️ Live Process & Terminal Monitor** — Dev servers, training jobs, SSH sessions, Docker containers — all visible with live CPU/memory bars, PID tracking, and terminal output tailing. Remote server URL probes for instant UP/DOWN checks. Crash/OOM detection tells you what happened without digging through logs.
- **🤖 An Expert Always by Your Side** — The AI Agent has live access to every data source on your dashboard. "Why did my build fail?" — it pulls CI logs + process history to analyze. "Summarize today's Feishu threads" — done. Need a PPT? It generates and executes Python code. Always-on, wake it anytime for answers, analysis, or real work.
- **📡 Everything Streams, Nothing Is Stale** — Stock tickers, Bloomberg live TV, world news, HN/Reddit, Gmail, Calendar, Feishu — all auto-refreshing. Breaking news triggers desktop notifications. Keyword monitors track any topic across all sources in real time.
- **📋 Today's Focus** — Sidebar with next-meeting countdown, unread badges, CI failure alerts, stock movers, and AI daily briefing — open the dashboard and know what needs attention.
- **🔧 One Screen, Zero Context Switching** — No more jumping between `htop`, terminal tabs, Gmail, stock apps, and Slack. Every panel is self-contained, auto-refreshing, and resilient.

### 📋 Panel Overview

| Category | Panels | What You See |
|----------|--------|-------------|
| 🖥️ **DevOps & System** | Process Monitor, System Health, Coding Hub | All running processes & terminals, remote server probes, CPU/MEM, GitHub CI/CD, trending repos |
| 🤖 **AI Agent** | AI Agent, Today's Focus | Chat with your data, generate content, daily briefing with aggregated alerts |
| 📊 **Markets & Finance** | Stock Market, Daily Finance | Live stock/crypto/commodity tickers, income & expense tracking |
| 📰 **Information** | News, Live News, Tech Community, My Monitors | Categorized news feeds, Bloomberg live stream, HN/Reddit, custom keyword alerts |
| 📅 **Productivity** | Schedule, Email, Feishu | Google Calendar, Gmail inbox, Feishu/Lark bot messages |
| 🌍 **Overview** | Global Map, Weather, World Clock, Quick Links | News pinned on a world map, weather forecast, multi-timezone clocks |

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd my-daily-monitor
npm install
```

### 2. Start the Development Server

```bash
npm run dev
```

This starts the Vite dev server with the embedded API plugin at [http://localhost:5173](http://localhost:5173). No separate backend server is needed — API routes are handled by the Vite plugin.

### 3. Configure

Open the dashboard and click **⚙ Settings** in the top-right corner. Add your API keys for the data sources you want to enable:

<div align="center">
<table>
<tr>
<td align="center"><b>API Keys</b></td>
<td align="center"><b>Preferences</b></td>
</tr>
<tr>
<td><img src="../assets/settings_api_keys.png" width="360px" alt="Settings – API Keys" /></td>
<td><img src="../assets/settings_preferences.png" width="360px" alt="Settings – Preferences" /></td>
</tr>
</table>
</div>

#### API Keys

| Key | Required For | How to Get |
|-----|-------------|-----------|
| `FINNHUB_API_KEY` | Stock Market | [finnhub.io](https://finnhub.io/) (free) |
| `NEWSAPI_KEY` | News Feed (optional) | [newsapi.org](https://newsapi.org/) — RSS feeds work without it |
| `GITHUB_PAT` | Code Status (CI/CD) | GitHub → Settings → PAT (`repo` + `actions:read`) |
| `GMAIL_CLIENT_ID` | Email + Calendar | Google Cloud Console OAuth |
| `GMAIL_CLIENT_SECRET` | Email + Calendar | Google Cloud Console OAuth |
| `GMAIL_REFRESH_TOKEN` | Email + Calendar | OAuth flow |
| `GOOGLE_CALENDAR_ENABLED` | Calendar (toggle) | Uses same Gmail OAuth credentials |
| `OUTLOOK_CLIENT_ID` | Email (Outlook) | Microsoft Azure App Registration |
| `OUTLOOK_REFRESH_TOKEN` | Email (Outlook) | Microsoft Graph OAuth flow |
| `FEISHU_APP_ID` | Feishu Messages | Feishu Open Platform |
| `FEISHU_APP_SECRET` | Feishu Messages | Feishu Open Platform |
| `TWITTER_BEARER_TOKEN` | Social Feed | Twitter Developer Portal |
| `OPENROUTER_API_KEY` | AI Agent | [openrouter.ai](https://openrouter.ai/) |
| `OPENROUTER_MODEL` | AI Model (optional) | Default: `minimax/minimax-m2.5` |

> [!TIP]
> Not all API keys are required. The dashboard works incrementally — each panel gracefully handles missing configuration and shows setup instructions.

#### Preferences

| Preference | What It Controls |
|-----------|-----------------|
| Color Scheme / Theme Mode | Appearance: color scheme and dark/light mode |
| Stock Watchlist | Symbols to track (`SYMBOL\|Name`, one per line) |
| News Categories | Topic filters (e.g. `us, science, tech, finance, world, ai`) |
| News Alert Keywords | Keyword highlights across all news sources |
| GitHub Repos | Repos to monitor for CI/CD (`owner/repo`, one per line) |
| Feishu Chat IDs | Feishu group chats to stream messages from |
| AI Summaries | Toggle AI-generated daily briefing on/off |

#### Customization

<div align="center">
<table>
<tr>
<td align="center"><b>Command Palette</b> <code>Cmd/Ctrl+K</code><br/>Jump to any panel, trigger actions</td>
<td align="center"><b>Custom Panels</b><br/>Embed any URL (Grafana, Notion, etc.)</td>
</tr>
<tr>
<td><img src="../assets/command_palette.png" width="400px" alt="Command Palette" /></td>
<td><img src="../assets/add_custom_panel.png" width="400px" alt="Add Custom Panel" /></td>
</tr>
</table>
</div>

---

## 🧬 How Was It Generated? — OpenSpace Skill Evolution

> **Zero human code was written.** The entire project — every panel, service, style, and API route — was generated and iteratively evolved by [OpenSpace](https://github.com/HKUDS/OpenSpace) with no manual coding involved.

### The Process

1. **Seed Reference**: OpenSpace started by analyzing the open-source project [WorldMonitor](https://github.com/koala73/worldmonitor) — a real-time global intelligence dashboard built with vanilla TypeScript.

2. **Skill Extraction**: OpenSpace extracted an initial set of **6 skills** from WorldMonitor's codebase:
   - `codebase-pattern-analyzer` — How to analyze a codebase and identify reusable patterns
   - `skill-template-generator` — How to generate skill templates from identified patterns
   - `worldmonitor-reference` — Architecture index: Panel class hierarchy, service layer, CSS grid, API edge functions
   - `panel-component` — Base Panel class pattern with loading/error states
   - `data-service` — Service module conventions
   - `panel-grid-layout` — Responsive CSS grid system

3. **Domain Adaptation**: Using the `personal-monitor-domain` skill, OpenSpace defined the target panels, data sources, APIs, and priority ordering for a **personal** daily monitor (as opposed to WorldMonitor's global scope).

4. **Iterative Evolution**: OpenSpace evolved the project step-by-step — each iteration added new panels, refined existing ones, fixed bugs, and extracted new skills from the evolving codebase. The skills themselves self-evolved, becoming more specific and battle-tested over time.

### 📈 Evolution Graph

The following graph shows the skill evolution path — how OpenSpace progressively built and refined the dashboard through multiple iterations:

<div align="center">
<img src="../assets/my_daily_monitor_evograph.png" width="800px" alt="My Daily Monitor - Skill Evolution Graph" />
</div>

> Each node represents a skill that OpenSpace learned, extracted, or refined during the development process. The graph illustrates how initial reference patterns from WorldMonitor branched into specialized skills for panel creation, data services, full-stack feature authoring, and more.

### 📂 Evolved Skills & Evolution DB

Through iterative evolution, OpenSpace accumulated **60+ skills** spanning multiple categories. Examples:

- **Panel patterns**: `panel-component`, `panel-base-advanced`, `panel-visual-badges`, ...
- **Data services**: `data-service`, `data-service-circuit-breaker-aware`, `data-service-proxy-direct`, ...
- **Full-stack workflows**: `create-full-stack-panel-feature`, `full-stack-panel-authoring`, ...
- **Infrastructure**: `refresh-scheduler`, `api-proxy-endpoint`, `project-scaffold`, ...
- **Reliability**: `typescript-compile-check-resilient`, `unicode-safe-file-writing`, `idempotent-file-replace`, ...

The full evolution history — every skill version, derivation chain, and quality score — is stored in the open-sourced [`showcase/.openspace/openspace.db`](.openspace/openspace.db) SQLite database.

---

<details>
<summary><b>🏗️ Project Structure</b></summary>

```
my-daily-monitor/
├── index.html                  # Entry HTML with flash-free theme init
├── vite.config.ts              # Vite config with embedded API plugin
├── vite-api-plugin.ts          # API routes served via Vite middleware
├── src/
│   ├── main.ts                 # App entry — panel instantiation, grid layout, scheduler
│   ├── components/             # All UI panel classes (29 components)
│   │   ├── Panel.ts            # Base Panel class (all panels extend this)
│   │   ├── StockPanel.ts       # Stock market watchlist
│   │   ├── NewsPanel.ts        # Aggregated news headlines
│   │   ├── EmailPanel.ts       # Gmail inbox
│   │   ├── InsightsPanel.ts    # AI Agent with tool routing
│   │   ├── MapPanel.ts         # MapLibre GL world map
│   │   ├── CommandPalette.ts   # Cmd+K command palette
│   │   ├── SettingsModal.ts    # API key configuration
│   │   └── ...                 # 20+ more panel components
│   ├── services/               # Data fetching layer (14 services)
│   │   ├── stock-market.ts     # Finnhub stock quotes
│   │   ├── news.ts             # GNews + HackerNews aggregation
│   │   ├── email.ts            # Gmail API integration
│   │   ├── schedule.ts         # Google Calendar events
│   │   ├── ai-summary.ts       # LLM daily briefing generation
│   │   ├── refresh-scheduler.ts# Visibility-aware refresh scheduling
│   │   └── ...
│   ├── config/                 # Settings keys and preferences
│   ├── styles/                 # CSS (dark/light themes, grid layout)
│   └── utils/                  # Helpers (circuit breaker, formatting, sparkline)
└── server/                     # Standalone API server (alternative to Vite plugin)
    ├── index.ts                # Express/tsx server entry
    └── routes/                 # API route handlers
        ├── stock.ts, news.ts, email.ts, github.ts, ...
```

</details>

---

## 🔗 Related

- **[OpenSpace](https://github.com/HKUDS/OpenSpace)** — Self-evolving skill worker & community for AI agents, the engine that generated this entire project.
- **[WorldMonitor](https://github.com/koala73/worldmonitor)** — Real-time global intelligence dashboard that served as the seed reference for initial skills extraction.

```

### File: COMMUNICATION.md
```md
We provide QR codes for joining the HKUDS discussion groups on **WeChat** and **Feishu**.

You can join by scanning the QR codes below:

<img src="https://github.com/HKUDS/.github/blob/main/profile/QR.png" alt="WeChat QR Code" width="400"/>
```

### File: README_CN.md
```md
<div align="center">

<picture>
    <img src="assets/logo.png" width="320px" style="border: none; box-shadow: none;" alt="OpenSpace Logo">
</picture>

## ✨ OpenSpace：让你的 Agent 更聪明、更省钱、自我进化 ✨

| 🔋 **Token 用量减少 46%** | **💰 6 小时赚取 $11K** | 🧬 **Skill 自我进化** | 🌐 **Agent 经验共享** |

[![Agents](https://img.shields.io/badge/Agents-Claude_Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20nanobot%20%7C%20...-99C9BF.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-20+-FFF4D6.svg)](https://nodejs.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)
[![Feishu](https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=larksuite&logoColor=white)](./COMMUNICATION.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md)

**一条命令，进化你所有的 AI Agent**：OpenClaw、nanobot、Claude Code、Codex、Cursor 等

<img src="assets/cli-typing.gif" width="500px" alt="openspace --query your task">

</div>

---

## 📢 最新动态

- **2026-04-03** 🚀 发布 **v0.1.0** — Skill 质量监控上线：从优质 Skill 中提取结构模式，每日自动评估所有新提交；云端搜索全面升级，匹配更准、响应更快；社区自发形成生产级垂直 Skill 集群。前端新增中文（zh）国际化支持。
- **2026-04-02** ⚡ 云端搜索升级，提升匹配质量、降低响应延迟。
- **2026-03-31** 🛡️ 安全加固：zip 解压与 `import_skill` 新增路径穿越防护；CLI 启动时读取 `OPENSPACE_MODEL` 及 `OPENSPACE_LLM_*` 环境变量；修复 MiniMax 兼容性问题与 workflow ID 冲突。
- **2026-03-29** 🔒 锁定 litellm 版本至 <1.82.7，规避 PYSEC-2026-2 供应链投毒。
- **2026-03-28** 🔧 Skill 注册幂等化——`register_skill_dir` 对已注册目录直接返回已有 `SkillMeta`，不再重复创建。同步更新 OpenClaw 部署文档。
- **2026-03-27** 🪟 修复 Windows 下 stdio 死锁；evolver 确认解析改用词干匹配，消除误判。
- **2026-03-26** 🌱 Skill 目录支持每次调用时动态重扫描，本地搜索更轻量，文档同步精简。
- **2026-03-25** 🎉 OpenSpace 正式开源！

---

## 当前 AI Agent 面临的问题

如今的 AI Agent——[OpenClaw](https://github.com/openclaw/openclaw)、[nanobot](https://github.com/HKUDS/nanobot)、[Claude Code](https://docs.anthropic.com/en/docs/claude-code)、[Codex](https://github.com/openai/codex)、[Cursor](https://cursor.com) 等——能力强大，但有一个致命弱点：它们从不从真实世界的经验中**学习**、**适应**和**进化**——更不用说相互之间的**共享**了。
- **❌ 大量 Token 浪费** - 如何复用成功的任务模式，而非每次都从零推理、烧掉大量 Token？
- **❌ 重复犯下高代价的错误** - 如何在 Agent 之间共享解决方案，而非反复进行同样昂贵的探索和犯同样的错？
- **❌ Skill 质量差且不可靠** - 当工具和 API 持续演变时，如何保证 Skill 的可靠性——同时确保社区贡献的 Skill 达到严格的质量标准？

## 🎯 什么是 OpenSpace？

**🚀 🚀 一个自我进化引擎，让每一次任务都能使每个 Agent 变得更聪明、更高效。**

https://github.com/user-attachments/assets/c50f70ab-f6db-47bf-9498-3210c0f0abae

OpenSpace 以 Skill 的形式接入任意 Agent，并赋予其三大超能力：

### 🧬 自我进化
Skill 能够自动学习并持续提升
- ✅ **自动修复（AUTO-FIX）** — Skill 出错时，自行即时修复
- ✅ **自动改进（AUTO-IMPROVE）** — 成功模式自动升级为更优版本
- ✅ **自动学习（AUTO-LEARN）** — 从实际使用中捕获高效工作流
- ✅ **质量监控** — 跟踪所有任务中的 Skill 表现、错误率和执行成功率

**Skill 持续进化——将每次失败转化为改进，将每次成功转化为优化。**

### 🌐 Agent 集体智慧
将独立的 Agent 联结为共享大脑
- ✅ **共享进化**：一个 Agent 的改进即成为所有 Agent 的升级
- ✅ **网络效应**：更多 Agent → 更丰富的数据 → 每个 Agent 更快进化
- ✅ **便捷共享** — 一行命令即可上传或下载进化后的 Skill
- ✅ **访问控制** — 每项 Skill 可选择公开、私有或仅团队可见

**一个 Agent 学会，所有 Agent 受益——大规模集体智慧。**

### 💰 Token 效率
更聪明的 Agent，显著更低的成本
- ✅ **不再重复劳动** → 复用成功方案，而非每次从零开始
- ✅ **任务越做越便宜** → 随着 Skill 改进，类似工作的成本持续下降
- ✅ **只做小幅更新** → 修复损坏的部分，无需全部重建
- ✅ **实际节省**：在真实任务上实现 4.2 倍性能提升、Token 消耗减少 46%，带来可衡量的经济价值。（[GDPVal](#-基准测试gdpval)）

事半功倍——Agent 真正帮你省钱。

---

### 核心差异

**❌ 当前的 Agent**
- 随着工具更迭，Skill 默默退化
- 失败模式反复重演，缺乏学习机制
- 知识封锁在单个 Agent 内

**✅ OpenSpace 赋能的 Agent**
- 多层监控捕捉问题并自动触发修复
- 成功的工作流转化为可复用、可共享的 Skill
- 一个 Agent 学到有用的东西，所有 Agent 即刻获得

### 📊 OpenSpace：让你的 Agent 成为能赚钱的同事

**🎯 真实世界的硬核结果**
在 6 个行业的 50 项专业任务（**📈 [GDPVal 经济基准测试](#-基准测试gdpval)**）上，OpenSpace Agent 使用相同的骨干 LLM（Qwen 3.5-Plus），收入是基线（[ClawWork](https://github.com/HKUDS/ClawWork)）Agent 的 **4.2 倍**，同时通过 Skill 进化节省了 46% 的 Token 开销。

<div align="center">
<img src="assets/benchmark_kpi.png" width="100%" alt="GDPVal 基准测试 — 核心指标" />
</div>

**💼 这些不是玩具级别的问题**
- 根据复杂的工会合同构建工资计算器
- 从 15 份散落的 PDF 文档中准备纳税申报表
- 起草关于加州隐私法规的法律备忘录
- 创建合规表格和工程技术规格书

**📈 在所有领域全面胜出**
- 合规类工作：收入提升 +18.5%
- 工程类项目：性能提升 +8.7%
- 专业文档类：Token 需求减少 56%
- 所有类别均有提升——无一例外

<div align="center">
<img src="assets/benchmark_task_showcase.png" width="100%" alt="GDPVal 基准测试 — 各类别任务展示" />
</div>

**OpenSpace 不仅让 Agent 更聪明** —— 更让它们具备经济可行性。真实工作、真实收入、可衡量的成果。

## OpenSpace 自主系统开发案例

**🖥️ [My Daily Monitor](showcase/README.md)** — OpenSpace 赋能你的 Agent 完成大规模系统开发。这个拥有 20 多个实时仪表盘面板的个人行为监控系统完全由 Agent 构建——通过 OpenSpace 从零进化出 60 多项 Skill，展示了自主端到端软件开发能力。

<div align="center">
<img src="assets/my_daily_monitor_dark.png" width="100%" alt="My Daily Monitor – 深色模式" />
</div>

---

## 📋 目录

- [⚡ 快速开始](#-快速开始)
  - [🤖 路径 A：为你的 Agent 接入](#-路径-a为你的-agent-接入)
  - [👤 路径 B：作为你的 AI 协作者](#-路径-b作为你的-ai-协作者)
  - [📊 本地仪表盘](#-本地仪表盘)
- [📈 基准测试：GDPVal](#-基准测试gdpval)
- [📊 案例展示：My Daily Monitor](#-案例展示my-daily-monitor)
- [🏗️ 框架](#️-框架)
  - [🧬 自我进化引擎](#-自我进化引擎)
  - [🌐 云端 Skill 社区](#-云端-skill-社区)
- [🔧 高级配置](#-高级配置)
- [📖 代码结构](#-代码结构)
- [🤝 贡献与路线图](#-贡献与路线图)
- [🔗 相关项目](#-相关项目)

---

## ⚡ 快速开始

🌐 **只想看看？** 在 **[open-space.cloud](https://open-space.cloud)** 浏览社区 Skill 和进化谱系——无需安装。

```bash
git clone https://github.com/HKUDS/OpenSpace.git && cd OpenSpace
pip install -e .
openspace-mcp --help   # 验证安装
```

> [!TIP]
> **Clone 太慢？** `assets/` 目录包含约 50 MB 的图片文件，导致仓库较大。使用以下轻量方式跳过它：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/HKUDS/OpenSpace.git
> cd OpenSpace
> git sparse-checkout set '/*' '!assets/'
> pip install -e .
> ```

**选择你的路径：**
- **[路径 A](#-路径-a为你的-agent-接入)** — 将 OpenSpace 接入你的 Agent
- **[路径 B](#-路径-b作为你的-ai-协作者)** — 直接使用 OpenSpace 作为你的 AI 协作者

### 🤖 路径 A：为你的 Agent 接入

适用于任何支持 Skill（`SKILL.md`）的 Agent——[Claude Code](https://docs.anthropic.com/en/docs/claude-code)、[Codex](https://github.com/openai/codex)、[OpenClaw](https://github.com/openclaw/openclaw)、[nanobot](https://github.com/HKUDS/nanobot) 等。

**① 将 OpenSpace 添加到你的 Agent 的 MCP 配置中：**

```json
{
  "mcpServers": {
    "openspace": {
      "command": "openspace-mcp",
      "toolTimeout": 600,
      "env": {
        "OPENSPACE_HOST_SKILL_DIRS": "/path/to/your/agent/skills",
        "OPENSPACE_WORKSPACE": "/path/to/OpenSpace",
        "OPENSPACE_API_KEY": "sk-xxx (可选，用于云端)"
      }
    }
  }
}
```

> [!TIP]
> 凭证（API 密钥、模型）会从你的 Agent 配置中**自动检测**，通常无需手动设置。

**② 将 Skill 复制**到你的 Agent Skill 目录：

```bash
cp -r OpenSpace/openspace/host_skills/delegate-task/ /path/to/your/agent/skills/
cp -r OpenSpace/openspace/host_skills/skill-discovery/ /path/to/your/agent/skills/
```

完成。这两项 Skill 会教你的 Agent 何时以及如何使用 OpenSpace——无需额外提示。你的 Agent 现在可以自我进化 Skill、执行复杂任务、访问云端 Skill 社区。你也可以添加自定义 Skill——参见 [`openspace/skills/README.md`](openspace/skills/README.md)。

> [!NOTE]
> **云端社区（可选）：** 在 **[open-space.cloud](https://open-space.cloud)** 注册以获取 `OPENSPACE_API_KEY`，然后将其添加到上面的 `env` 块中。即使没有 API Key，所有本地功能（任务执行、进化、本地 Skill 搜索）也能正常运行。

📖 各 Agent 配置（OpenClaw / nanobot）、所有环境变量、高级设置：[`openspace/host_skills/README.md`](openspace/host_skills/README.md)

### 👤 路径 B：作为你的 AI 协作者

直接使用 OpenSpace——编码、搜索、工具调用等——内置自我进化 Skill 和云端社区。

> [!NOTE]
> 创建 `.env` 文件并填入你的 LLM API 密钥，可选添加 `OPENSPACE_API_KEY` 以访问云端社区（参考 [`openspace/.env.example`](openspace/.env.example)）。

```bash
# 交互模式
openspace

# 执行任务
openspace --model "anthropic/claude-sonnet-4-5" --query "Create a monitoring dashboard for my Docker containers"
```

添加自定义 Skill：[`openspace/skills/README.md`](openspace/skills/README.md)。

**Cloud CLI** — 通过命令行管理 Skill：

```bash
openspace-download-skill <skill_id>         # 从云端下载 Skill
openspace-upload-skill /path/to/skill/dir   # 上传 Skill 到云端
```

<details>
<summary><b>Python API</b></summary>

```python
import asyncio
from openspace import OpenSpace

async def main():
    async with OpenSpace() as cs:
        result = await cs.execute("Analyze GitHub trending repos and create a report")
        print(result["response"])

        for skill in result.get("evolved_skills", []):
            print(f"  Evolved: {skill['name']} ({skill['origin']})")

asyncio.run(main())
```

</details>

### 📊 本地仪表盘

查看你的 Skill 如何进化——浏览 Skill、追踪谱系、比较差异。

> 需要 **Node.js ≥ 20**。

```bash
# 终端 1：启动后端 API
openspace-dashboard --port 7788

# 终端 2：启动前端开发服务器
cd frontend
npm install        # 仅首次需要
npm run dev    
```

📖 **前端设置指南**：[`frontend/README.md`](frontend/README.md)

<div align="center">
<table>
<tr>
<td width="50%"><img src="assets/frontend_1.gif" width="100%" alt="Skill 类别" /></td>
<td width="50%"><img src="assets/frontend_2.gif" width="100%" alt="云端 Skill 记录" /></td>
</tr>
<tr>
<td align="center"><sub>Skill 类别 — 浏览、搜索与排序</sub></td>
<td align="center"><sub>云端 — 浏览与发现 Skill 记录</sub></td>
</tr>
<tr>
<td width="50%"><img src="assets/frontend_3.gif" width="100%" alt="版本谱系" /></td>
<td width="50%"><img src="assets/frontend_4.gif" width="100%" alt="工作流会话" /></td>
</tr>
<tr>
<td align="center"><sub>版本谱系 — Skill 进化图谱</sub></td>
<td align="center"><sub>工作流会话 — 执行历史与指标</sub></td>
</tr>
</table>
</div>

---

## 📈 基准测试：GDPVal

我们在 [GDPVal](https://huggingface.co/datasets/openai/gdpval) 上评估 OpenSpace——该数据集包含 220 项真实世界的专业任务，涵盖 44 个职业——采用 [ClawWork](https://github.com/HKUDS/ClawWork) 评测协议，使用相同的生产力工具和基于 LLM 的评分方式。我们的两阶段设计（Cold Start → Warm Rerun）展示了积累的 Skill 如何随时间降低 Token 消耗。

公平基准：OpenSpace 使用 Qwen 3.5-Plus 作为骨干 LLM——与 ClawWork 基线 Agent 完全相同——确保性能差异纯粹来源于 Skill 进化，而非模型能力差异。

真实经济价值：任务涵盖构建工资计算器、准备纳税申报表、起草法律备忘录等——这些都是产生真实 GDP 的专业工作，同时从质量和成本效率两个维度进行评估。

<div align="center">
<img src="assets/benchmark_income.png" width="100%" alt="GDPVal 基准测试 — 收入对比" />
</div>

- **收入提升 4.2 倍** — 相比使用相同骨干 LLM（Qwen 3.5-Plus）的 ClawWork
- **72.8% 价值捕获率** — 在 $15,764 的任务总价值中赚取 $11,484，超越所有 Agent
- **70.8% 平均质量** — 比最佳 ClawWork Agent（40.8%）高出 30 个百分点
- **Phase 2 的 Token 用量仅为 Phase 1 的 45.9%** — 更好的结果，显著更低的成本

<div align="center">
<img src="assets/benchmark_quality_tokens.png" width="100%" alt="GDPVal 基准测试 — 质量与 Token 效率" />
</div>

### OpenSpace 能处理哪些真实任务？

50 项 GDPVal 任务涵盖 6 个真实工作类别。
- **Phase 1（Cold Start）** 按顺序执行全部 50 项任务——每项任务完成后，Skill 积累到共享数据库中。
- **Phase 2（Warm Rerun）** 使用 Phase 1 中完整的进化 Skill 库，重新执行相同的 50 项任务。

收入捕获率 = 实际获得报酬 ÷ 任务最大可能价值

<div align="center">
<img src="assets/benchmark_task_showcase.png" width="100%" alt="GDPVal 基准测试 — 各类别任务展示" />
</div>

## 🎯 进化在何处产生最大影响——以及原因：

| 类别 | 收入变化 | Token 变化 | 原因 |
|---|---|---|---|
| **📝 文档与通信** (7) | 71→74% (+3.3pp) | −56% | 规范的正式输出——加州隐私法备忘录、监控调查报告、子女抚养案例报告。`document-gen-fallback` Skill 族历经 13 个版本进化，使结构化输出和错误恢复接近全自动。 |
| **📋 合规与表单** (11) | 51→70% (+18.5pp) | −51% | 结构化 PDF——从 15 份源文档生成纳税申报表、药房合规检查清单、临床交接模板。PDF Skill 链（检查清单逻辑 → reportlab 排版 → 验证）只需进化一次，所有表单任务即可复用完整流水线。 |
| **🎬 媒体制作** (3) | 53→58% (+5.8pp) | −46% | 通过 Python 和 ffmpeg 处理音视频——根据鼓点参考生成巴萨诺瓦器乐、从 5 轨中编辑低音分轨、从 13 段源视频制作 CGI 集锦。进化的 Skill 编码了可用的 ffmpeg 参数和编解码器回退策略，消除了沙箱中的反复试错。 |
| **🛠️ 工程** (4) | 70→78% (+8.7pp) | −43% | 多交付物技术项目——Web3 全栈（Solidity + React + 测试）、CNC 工作站安全系统（报告 + 布局图 + 硬件表）、航空航天 CFD 报告。协调类 Skill 在这些多样化任务之间通用迁移。 |
| **📊 电子表格** (15) | 63→70% (+7.3pp) | −37% | 功能性 .xlsx 工具——根据工会合同构建工资计算器、基于历史数据预测销售、含竞品对标的定价模型。电子表格模式（公式、合并单元格、数据验证）在各领域完全通用。 |
| **📈 战略与分析** (10) | 88→89% (+1.0pp) | −32% | 战略建议——供应商谈判策略、非营利项目评估、3 亿美元交易台的能源交易分析。质量已处最高水平（88%）；节省来自于文档结构和多文件编排的复用。 |

### 进化产出了什么？（165 项 Skill）

在 50 项 Phase 1 任务中，OpenSpace 自主进化出 **165 项 Skill**。突破性发现：这些不仅是领域知识——它们是**鲁棒的执行模式**和**质量保障工作流**。Agent 学会了如何在不完美的真实世界环境中可靠地交付成果。

**关键发现**：大多数 Skill 聚焦于工具可靠性和错误恢复，而非特定任务知识。

<div align="center">
<img src="assets/benchmark_skill_taxonomy.png" width="100%" alt="GDPVal 基准测试 — 进化 Skill 分类" />
</div>

| 用途 | 数量 | Skill 教会 Agent 什么 |
|---|---|---|
| **文件格式 I/O** | 44 | PDF 解析回退、DOCX 解析、Excel 合并单元格处理、PPTX 创建。其中 32/44 从真实失败中*捕获*——每一条都是生产环境中解决的 Bug。 |
| **执行恢复** | 29 | 分层回退：沙箱失败 → Shell → 写文件后运行 → heredoc。28/29 从实际崩溃中*捕获*。这是使一切其他 Skill 可靠运行的基础。 |
| **文档生成** | 26 | 端到端文档流水线。`document-gen-fallback` 从 1 项导入 Skill 进化为 **13 个衍生版本**——进化最深入的 Skill 族。 |
| **质量保障** | 23 | 写后验证：检查 Excel 行数、验证 PDF 页数、校验电子表格公式。Phase 2 质量提升的关键——Agent 不仅*生产*，还*验证*。 |
| **任务编排** | 17 | 多文件追踪、ZIP 打包、零迭代失败检测。适用于所有多交付物任务类型的元 Skill。 |
| **领域工作流** | 13 | SOAP 病历记录、音频制作（从 1 个模板衍生 **4 代**）、视频流水线。数量虽少，但在各自领域内进化深度显著。 |
| **网络与研究** | 11 | SSL/代理调试、搜索回退、JS 重页面处理。包含 2 项*修复* Skill——网络访问本质上不稳定。 |

**复现实验、分析工具与结果**：[`gdpval_bench/README.md`](gdpval_bench/README.md)

---

## 📊 案例展示：My Daily Monitor

> **零行人工编写的代码。** 60 多项 Skill 从零进化，构建出一个完整可用的实时仪表盘。

**My Daily Monitor** 是一个常驻运行的仪表盘，实时展示进程、服务器、新闻、市场、邮件和日程——内置 AI Agent。

<div align="center">
<img src="assets/my_daily_monitor_light.png" width="90%" alt="My Daily Monitor – 浅色模式" />
</div>

### OpenSpace 如何从零构建它

| 阶段 | 发生了什么 | Skill |
|-------|------------|-------|
| 🌱 **种子期** | 分析开源项目 [WorldMonitor](https://github.com/koala73/worldmonitor)，提取参考模式 | 6 项初始 Skill |
| 🏗️ **脚手架** | 生成项目结构、Vite 配置、TypeScript 设置 | +8 项 Skill |
| 🎨 **构建** | 创建 20 多个面板，配合数据服务、API 路由、网格布局 | +25 项 Skill |
| 🔧 **修复** | 自动修复 TypeScript 错误、API 不匹配、CSS 冲突 | +12 项 FIX 进化 |
| 🧬 **进化** | 衍生增强模式，合并互补 Skill | +15 项 DERIVED Skill |
| 📦 **捕获** | 从成功执行中提取可复用模式 | +8 项 CAPTURED Skill |

### 📈 Skill 进化图谱

<div align="center">
<img src="assets/my_daily_monitor_evograph.png" width="90%" alt="Skill 进化图谱" />
</div>

> 每个节点代表 OpenSpace 学习、提取或精炼的一项 Skill。完整的进化历史已在 [`showcase/.openspace/openspace.db`](showcase/.openspace/openspace.db) 中开源——可用任意 SQLite 浏览器加载，探索谱系、差异和质量指标。

**完整详情**：[`showcase/README.md`](showcase/README.md)

---

## 🏗️ OpenSpace 框架

<div align="center">
<img src="assets/framework.png" width="90%" alt="OpenSpace 框架" />
</div>

### 🧬 自我进化引擎

OpenSpace 的核心。Skill 不是静态文件——它们是能够自动选择、应用、监控、分析和进化自身的"活"实体。

#### 🔄 自主与持续进化

- **全生命周期管理**：从发现到应用到进化——全程无需人工干预。无论是否存在匹配的 Skill，OpenSpace 都能完成任务。

**三种进化模式**：
- 🔧 FIX — 就地修复损坏或过时的指令。同一 Skill，新版本。
- 🚀 DERIVED — 从父 Skill 创建增强版或专用版。新 Skill 目录，与父 Skill 共存。
- ✨ CAPTURED — 从成功执行中提取全新的可复用模式。全新 Skill，无父级。

**三个独立触发器**：多层防线抵御 Skill 退化——无论执行成功还是失败都驱动进化。
- **📈 执行后分析** — 每次任务完成后运行。分析完整记录，为相关 Skill 建议 FIX/DERIVED/CAPTURED。
- **⚠️ 工具退化检测** — 当工具成功率下降时，质量监控器找到所有依赖的 Skill 并批量进化。
- **📊 指标监控** — 定期扫描 Skill 健康指标（应用率、完成率、回退率），进化表现不佳者。

#### 📊 全栈质量监控
多层追踪：质量监控覆盖整个执行栈——从高层工作流到单个工具调用：
- **🎯 Skill** — 应用率、完成率、有效率、回退率
- **🔨 工具调用** — 成功率、延迟、标记的问题
- **⚡ 代码执行** — 执行状态、错误模式

**级联进化**：当任何组件退化时——无论是 Skill 工作流还是单个工具调用——上游所有依赖的 Skill 自动触发进化，维持系统级一致性。

#### 🔧 智能且安全的进化
**🤖 自主进化**：每次进化都会探索代码库、发现根因、自主决定修复——在做出改变之前收集真实证据，而非盲目生成。

**⚡ 基于 Diff 且节省 Token**：生成最小化的、有针对性的 Diff，而非全量重写，失败时自动重试。每个版本存储在版本 DAG 中，支持完整的谱系追踪。

**🛡️ 内置安全防护**：
- 确认门控减少误触发
- 反循环守卫防止进化失控
- 安全检查标记危险模式（Prompt Injection、凭证窃取）
- 进化后的 Skill 经验证后才替换前代

**🌐 协作 Skill 社区**
一个协作式注册中心，Agent 在此共享进化后的 Skill。当一个 Agent 完成改进，所有连接的 Agent 都可以发现、导入并在此基础上构建——将个体进步转化为集体智慧。

- **🔐 灵活共享**：可选择公开分享、团队内分享或保持私有。智能搜索帮你找到所需并自动导入。每次进化都有完整 Diff 的谱系追踪。

- **☁️ 协作平台**：open-space.cloud — 注册获取 API 密钥、浏览社区 Skill、管理你的团队。

---

## 🔧 高级配置

对大多数用户而言，[快速开始](#-快速开始)就是你所需的全部。如需高级选项（环境变量、执行模式、安全策略等），请参见 [`openspace/config/README.md`](openspace/config/README.md)。

---

<a id="-代码结构"></a>
<details>
<summary><b>📖 代码结构</b></summary>

> **图例**：⚡ 核心模块 &nbsp;|&nbsp; 🧬 Skill 进化 &nbsp;|&nbsp; 🌐 云端 &nbsp;|&nbsp; 🔧 支撑模块

```
OpenSpace/
├── openspace/
│   ├── tool_layer.py                     # OpenSpace 主类 & OpenSpaceConfig
│   ├── mcp_server.py                     # MCP 服务器（为你的 Agent 提供 4 个工具）
│   ├── __main__.py                       # CLI 入口（python -m openspace）
│   ├
... [TRUNCATED]
```

### File: frontend\index.html
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/webp" href="/openspace_icon.webp" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Neuton:ital,wght@0,400;0,700;1,400&family=Cabin:wght@400;500;600&display=swap" rel="stylesheet" />
    <title>OpenSpace Dashboard</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: frontend\package-lock.json
```json
{
  "name": "openspace-frontend",
  "version": "0.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "openspace-frontend",
      "version": "0.1.0",
      "dependencies": {
        "axios": "^1.7.9",
        "i18next": "^26.0.3",
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "react-force-graph-2d": "^1.25.4",
        "react-i18next": "^17.0.2",
        "react-router-dom": "^7.1.1"
      },
      "devDependencies": {
        "@types/react": "^18.3.12",
        "@types/react-dom": "^18.3.1",
        "@vitejs/plugin-react": "^4.3.4",
        "autoprefixer": "^10.4.20",
        "postcss": "^8.4.49",
        "tailwindcss": "^3.4.17",
        "typescript": "~5.6.2",
        "vite": "^6.0.3"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
      "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.0.tgz",
      "integrity": "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.0.tgz",
      "integrity": "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-compilation-targets": "^7.28.6",
        "@babel/helper-module-transforms": "^7.28.6",
        "@babel/helpers": "^7.28.6",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/traverse": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
      "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.28.6.tgz",
      "integrity": "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.28.6",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.28.6.tgz",
      "integrity": "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.6.tgz",
      "integrity": "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.28.6",
        "@babel/helper-validator-identifier": "^7.28.5",
        "@babel/traverse": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.28.6.tgz",
      "integrity": "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.29.2",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.29.2.tgz",
      "integrity": "sha512-HoGuUs4sCZNezVEKdVcwqmZN8GoHirLUcLaYVNBK2J0DadGtdcqgr3BCbvH8+XUo4NGjNl3VOtSjEKNzqfFgKw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.2",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.2.tgz",
      "integrity": "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.27.1.tgz",
      "integrity": "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.27.1.tgz",
      "integrity": "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.29.2",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.2.tgz",
      "integrity": "sha512-JiDShH45zKHWyGe4ZNVRrCjBz8Nh9TMmZG1kh4QTK8hCBTWBi8Da+i7s1fJw7/lYpM4ccepSNfqzZ/QvABBi5g==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.28.6.tgz",
      "integrity": "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.28.6",
        "@babel/parser": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.0.tgz",
      "integrity": "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.25.12.tgz",
      "integrity": "sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.25.12.tgz",
      "integrity": "sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.25.12.tgz",
      "integrity": "sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.25.12.tgz",
      "integrity": "sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.25.12.tgz",
      "integrity": "sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.25.12.tgz",
      "integrity": "sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.25.12.tgz",
      "integrity": "s
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
