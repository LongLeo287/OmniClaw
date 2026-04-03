---
id: charlie85270-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.706672
---

# KNOWLEDGE EXTRACT: Charlie85270
> **Extracted on:** 2026-03-30 17:31:17
> **Source:** Charlie85270

---

## File: `Dorothy.md`
```markdown
# 📦 Charlie85270/Dorothy [🔖 PENDING/APPROVE]
🔗 https://github.com/Charlie85270/Dorothy
🌐 https://dorothyai.app

## Meta
- **Stars:** ⭐ 239 | **Forks:** 🍴 37
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Dorothy, the wife your AI agents needs.

## README (trích đầu)
```
# Dorothy

![Dorothy](screenshots/background-2.png)

A beautiful desktop app to orchestrate your [Claude Code](https://claude.ai/code) ,[Codex](https://chatgpt.com/codex), [Gemini](https://geminicli.com/) and local agents. Deploy, monitor, and debug — all from one delightful interface. Free and open source.

![Dorothy Dashboard](screenshots/0.png)

## Table of Contents

- [Why Dorothy](#why-dorothy)
- [Core Features](#core-features)
- [Automations](#automations)
- [Kanban Task Management](#kanban-task-management)
- [Scheduled Tasks](#scheduled-tasks)
- [Remote Control](#remote-control)
- [Vault](#vault)
- [SocialData (Twitter/X)](#socialdata-twitterx)
- [Google Workspace](#google-workspace)
- [MCP Servers & Tools](#mcp-servers--tools)
- [Installation](#installation)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Configuration & Storage](#configuration--storage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## Why Dorothy

AI CLI tools are powerful — but it runs one agent at a time, in one terminal. Dorothy removes that limitation:

- **Run 10+ agents simultaneously** across different projects and codebases
- **Automate agent workflows** — trigger agents on GitHub PRs, issues, and external events
- **Delegate and coordinate** — a Super Agent orchestrates other agents via MCP tools
- **Manage tasks visually** — Kanban board with automatic agent assignment
- **Schedule recurring work** — cron-based tasks that run autonomously
- **Control from anywhere** — Telegram and Slack integration for remote management

---

## Core Features

### Parallel Agent Management

Run multiple agents simultaneously, each in its own isolated PTY terminal session. Agents operate independently across different projects, codebases, and tasks.

![Agents View](screenshots/agetns.png)

**Capabilities:**
- Spawn unlimited concurrent agents across multiple projects
- Each agent runs in an isolated terminal with full PTY support
- Assign skills, model selection (sonnet, opus, haiku), and project context per agent
- Send interactive input to any running agent in real-time
- Real-time terminal output streaming per agent
- Agent lifecycle management: `idle` → `running` → `completed` / `error` / `waiting`
- Secondary project paths via `--add-dir` for multi-repo context
- Git worktree support for branch-isolated development
- Persistent agent state across app restarts
- Autonomous execution mode (`--dangerously-skip-permissions`) for unattended operation

### Super Agent (Orchestrator)

A meta-agent that programmatically controls all other agents. Give it a high-level task and it delegates, monitors, and coordinates the work across your agent pool.

![Super Agent](screenshots/super-agent.png)

- Creates, starts, and stops agents programmatically via MCP tools
- Delegates tasks based on agent capabilities and assigned skills
- Monitors progress, captures output, and handles errors
- R
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

