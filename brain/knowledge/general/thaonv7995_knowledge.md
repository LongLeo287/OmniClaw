---
id: thaonv7995-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.912059
---

# KNOWLEDGE EXTRACT: thaonv7995
> **Extracted on:** 2026-03-30 17:54:16
> **Source:** thaonv7995

---

## File: `acpms.md`
```markdown
# 📦 thaonv7995/acpms [🔖 PENDING/APPROVE]
🔗 https://github.com/thaonv7995/acpms


## Meta
- **Stars:** ⭐ 10 | **Forks:** 🍴 5
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agentic Coding Project Management System

## README (trích đầu)
```
# ACPMS - Agentic Coding Project Management System

![Agentic Coding Architecture](docs/screenshots/architecture.webp)

A platform that integrates Project Management (Requirements, Tasks, Bugs) with **AI Agents** (Claude Code / Codex / Gemini / Cursor AI) to automate the software development lifecycle. Inspired by **Vibe Kanban**, with a simpler, lightweight design.

Focused on **project management** and **breaking down requirements** into manageable pieces so projects stay under control. **BA, PO, PM, and Tester** can drive work from ticket to deployable preview—AI agents handle coding and deployment based on approved specs, with human-in-the-loop review. Preview environments let non-developers verify results before production. Best suited for **small teams and small projects**.

## Features

- **Contextual Awareness** – Agents work on Tasks linked to approved Requirements and Architecture
- **Full Lifecycle** – Plan → Code → Deploy → Fix with human-in-the-loop review
- **Multi-Agent Support** – Claude Code, OpenAI Codex, Gemini CLI, Cursor AI CLI (selectable in Settings)
- **OpenClaw Gateway** – Connect ACPMS to OpenClaw so you can **manage projects from the chat channels** (e.g. Telegram, Slack).
- **GitLab Integration** – OAuth, MR creation, webhooks
- **Single Binary Distribution** – Backend serves frontend + S3 proxy for self-hosting

**Project & Assistant**

![ACPMS Project and Assistant](docs/screenshots/project-assistant.png)

**Settings**

![ACPMS Settings](docs/screenshots/settings.png)

**Tasks**

![ACPMS Tasks Kanban](docs/screenshots/tasks-kanban.png)

## Requirements

- **Docker** – PostgreSQL 16 + MinIO (S3)
- **curl, jq, tar** – For installer script
- **Rust** (for development) – rustup
- **Node.js 20+** (for development) – Frontend build

## Quick Start (Install from Release)

**Prerequisites:** Docker + Docker Compose, curl, jq, tar.

The installer auto-starts Postgres + MinIO via Docker Compose if not running. It does **not** install Docker.

**Supported OS (installer + release binary):**

- Linux (`x86_64`/`amd64`, `arm64`/`aarch64`)
- macOS (`x86_64` Intel, `arm64` Apple Silicon)
- Windows via WSL2 (run `install.sh` inside a Linux distro such as Ubuntu/Debian)

**Option A – One-liner (recommended default for all supported OS):**

```bash
bash -c "$(curl -sSL https://raw.githubusercontent.com/thaonv7995/acpms/main/install.sh)"
```

Uninstall (one-liner mode):

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/thaonv7995/acpms/main/install.sh)" -- --uninstall
```

**Update** (when ACPMS is already installed):

```bash
# Update to latest release
bash -c "$(curl -sSL https://raw.githubusercontent.com/thaonv7995/acpms/main/update.sh)"

# Update to specific version
bash -c "$(curl -sSL https://raw.githubusercontent.com/thaonv7995/acpms/main/update.sh)" -- --version v1.2.0
```

From cloned repo: `bash update.sh` or `bash update.sh --version v1.2.0`

**Option B – Clone repo, then install** (alternative):

```bash
git c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

