---
id: services-readme
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:12.495356
---

# OmniClaw Corp — Services

Folder centralizing all services. Everything starts, stops, configuration: from here.

---

## Structure

```
services/
├── boot.ps1        ← Start all (called from machine or bot /boot)
├── stop.ps1        ← Stop all
├── config.json     ← Centralized configuration (ports, keys, paths)
├── screenshot.py   ← Screenshot → send Telegram (/snap)
└── README.md       ← This file
```

---

## Services

| # | Name | Port | URL | Type |
|---|------|------|-----|------|
| 1 | **ClawTask Dashboard** | 7474 | http://localhost:7474/ | Local |
| 2 | **9router (LLM Gateway)** | 20128 | http://localhost:20128/ | Local |
| 3 | **OmniClaw Bot (nullclaw)** | 3000 | http://localhost:3000/ | Local |
| 4 | **Ollama (Local AI)** | 11434 | http://localhost:11434/ | Local |
| 5 | **OpenRouter** | — | https://openrouter.ai/ | Cloud |

---

## How to Start

### Method 1 — From Computer (Desktop Shortcut)
Double-click **"OmniClaw Boot"** on Desktop.

### Method 2 — From Telegram Bot
Send `/boot` to **OmniClaw Bot** — bot automatically calls `boot.ps1`.

### Method 3 — Auto on Boot
Task Scheduler `AI_OS_Watchdog` auto-starts nullclaw bot on login.
Then send `/boot` if you want to also start ClawTask + 9router + Ollama.

---

## Manual Commands

```powershell
# Start all
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\services\boot.ps1"

# Check status (no start)
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\services\boot.ps1" -Status

# Stop all
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\services\stop.ps1"
```

---

## Telegram Commands (OmniClaw Bot)

| Command | Description: |
|------|-------|
| `/sys` | Check CPU, RAM, Ports |
| `/task` | View/Add ClawTask |
| `/clawtask` | Link + status Dashboard |
| `/snap` | Screenshot → send here |
| `/log` | View watchdog log |
| `/run <cmd>` | Run PowerShell |
| `/web <q>` | Google search/read link |
| `/boot` | Start all services |
| `/stop` | Stop all services |
| `/new` | Clear history, start over |
