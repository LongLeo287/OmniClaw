---
id: johnriceml-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.214819
---

# KNOWLEDGE EXTRACT: JohnRiceML
> **Extracted on:** 2026-03-30 17:38:12
> **Source:** JohnRiceML

---

## File: `clawport-ui.md`
```markdown
# 📦 JohnRiceML/clawport-ui [🔖 PENDING/APPROVE]
🔗 https://github.com/JohnRiceML/clawport-ui
🌐 https://clawport.dev

## Meta
- **Stars:** ⭐ 749 | **Forks:** 🍴 113
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Open-source AI agent command center for Claude Code agent teams. Built on OpenClaw.

## README (trích đầu)
```
<div align="center">

<img src="https://raw.githubusercontent.com/JohnRiceML/clawport-ui/main/clawport-logo.png" alt="ClawPort" width="160" />

# ClawPort

**A visual command centre for your AI agent team.**

[![npm version](https://img.shields.io/npm/v/clawport-ui.svg)](https://www.npmjs.com/package/clawport-ui)
[![license](https://img.shields.io/npm/l/clawport-ui.svg)](LICENSE)
[![tests](https://img.shields.io/badge/tests-781%20passed-brightgreen)](#testing)

[Website](https://clawport.dev) | [Setup Guide](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/qiskit/references/setup.md) | [API Docs](api.md) | [npm](https://www.npmjs.com/package/clawport-ui)

</div>

---

ClawPort is an open-source dashboard for managing, monitoring, and talking directly to your [OpenClaw](https://openclaw.ai) AI agents. It connects to your local OpenClaw gateway and gives you an org chart, direct agent chat with vision and voice, a kanban board, cron monitoring, cost tracking, an activity console with live log streaming, and a memory browser -- all in one place.

No separate AI API keys needed. Everything routes through your OpenClaw gateway.

<img src="docs/screenshots/org-map.png" alt="Org Map" width="100%" />

<details>
<summary><strong>More screenshots</strong></summary>

| | |
|---|---|
| <img src="docs/screenshots/chat.png" alt="Agent Chat" /> | <img src="docs/screenshots/kanban.png" alt="Kanban Board" /> |
| **Chat** -- streaming text, vision, voice, file attachments | **Kanban** -- drag-and-drop task board across agents |
| <img src="docs/screenshots/pipelines.png" alt="Cron Pipelines" /> | <img src="docs/screenshots/cron-schedule.png" alt="Cron Schedule" /> |
| **Pipelines** -- DAG visualization with health checks | **Schedule** -- weekly heatmap and job management |
| <img src="docs/screenshots/activity.png" alt="Activity Console" /> | <img src="docs/screenshots/live-logs.png" alt="Live Logs" /> |
| **Activity** -- historical log browser with JSON expansion | **Live Logs** -- real-time streaming widget |
| <img src="docs/screenshots/costs.png" alt="Cost Dashboard" /> | <img src="docs/screenshots/memory.png" alt="Memory Browser" /> |
| **Costs** -- token usage, anomalies, optimization insights | **Memory** -- team memory browser with markdown rendering |

</details>

---

## Quick Start

### 1. Install OpenClaw

ClawPort requires a running [OpenClaw](https://openclaw.ai) instance. If you don't have one yet:

```bash
# Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# Run the onboarding wizard (sets up workspace, gateway, and daemon)
openclaw onboard --install-daemon
```

After onboarding, verify the gateway is running:

```bash
openclaw gateway status
```

You should see your gateway URL (default `localhost:18789`) and auth token. If you use a custom port, `clawport setup` will detect it automatically. See the [OpenClaw docs](https://docs.openclaw.ai/getting-started) for more detail.

### 2. Install ClawPort

> **Note:** The npm package is `clawport-ui`. The CLI command is `clawport`.
> Do not insta
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

