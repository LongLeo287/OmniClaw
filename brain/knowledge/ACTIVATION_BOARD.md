---
id: activation-board
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.412889
---

# 🚦 ACTIVATION BOARD — OmniClaw Services & Dashboards
# Updated: 2026-03-16
# Everything that needs activation / localhost opening must be in this board

> **Rule:** Before using any plugin below, the startup command must be run.
> These services DO NOT auto-start — manual activation or auto-start configuration is required.

---

## 🟢 Running / Always-On

| Service | URL | Port | Notes |
|---------|-----|------|---------|
| **OmniClaw Dashboard** | http://127.0.0.1:19000 | 19000 | Auto-starts via pre-session.md |

---

## 🔴 Manual Activation Required

### 🦞 LobsterBoard — AI usage aggregation dashboard
```bash
cd "$OMNICLAW_ROOT\plugins\LobsterBoard"
cp config.example.json config.json   # first time
# Edit config.json: city, target API keys
node server.cjs
```
| | |
|-|-|
| **URL** | http://localhost:3000 |
| **Port** | 3000 |
| **Requires** | Node.js ≥ 18 |
| **Reason** | Monitor Antigravity + Claude Code + Gemini + Cursor + Copilot usage from a single screen |
| **Special Widget** | Antigravity widget: `antigravity-usage login` → view Gemini 3 + Claude usage |

---

### 📡 Remote Bridge (Channels) — Zalo / Telegram / Discord / Facebook

> **Current status (2026-03-16):** Channels ARE NOT CONFIGURED YET
> Run `python channels/health_check.py` to check.

```bash
# 1. Fill tokens in .env (mandatory before running)
# TELEGRAM_BOT_TOKEN=your_token  ← from @BotFather
# DISCORD_BOT_TOKEN=your_token   ← from Discord Developer Portal
# ZALO_ACCESS_TOKEN=your_token   ← from Zalo OA
# MESSENGER_ACCESS_TOKEN=token   ← from Facebook Developer Portal

# 2. Health check
python "$OMNICLAW_ROOT\channels\health_check.py"

# 3. Telegram (easiest, no ngrok needed):
python "$OMNICLAW_ROOT\channels\telegram_bridge.py"

# 4. All at once:
python "$OMNICLAW_ROOT\channels\start_bridges.py"

# 5. Public URL required for Zalo & Facebook → run ngrok first:
python "$OMNICLAW_ROOT\channels\ngrok_connector.py"
```

| | |
|-|-|
| **Port** | 5001 (webhook server for Zalo/FB) |
| **Requires** | Tokens in `.env` (TELEGRAM_BOT_TOKEN, etc.) |
| **Health Check** | `python channels/health_check.py` |
| **Upgrade path** | PicoClaw (Go) — 8 channels incl. QQ/LINE/WeChat — see `knowledge/claws_evaluation.md` |

---

### 🔍 LightRAG — Local RAG (Retrieval-Augmented Generation)
```bash
cd "$OMNICLAW_ROOT\plugins\LightRAG"
pip install -r requirements.txt   # first time
python -m lightrag.api.lightrag_server
```
| | |
|-|-|
| **Port** | 9621 (default) |
| **URL** | http://localhost:9621 |
| **Requires** | Python, embedding model |

---

### 🕷️ Firecrawl — Web Crawler API
```bash
cd "$OMNICLAW_ROOT\plugins\firecrawl"
npm install   # first time
npm run dev
```
| | |
|-|-|
| **Port** | 3002 (default) |
| **URL** | http://localhost:3002 |
| **Requires** | Node.js |

---

### 🤖 MCP Server Bridge
```bash
cd "$OMNICLAW_ROOT\mcp"
# See README.md in the mcp/ directory for specific commands
```
| | |
|-|-|
| **Port** | See mcp/README.md |
| **Requires** | Node.js or Python |

---

## ⚙️ Auto-Start (1-time configuration)

### Using pm2 (starts with Windows):
```bash
npm install -g pm2

# LobsterBoard
pm2 start "$OMNICLAW_ROOT\plugins\LobsterBoard\server.cjs" --name lobsterboard

# Remote Bridge
pm2 start "python $OMNICLAW_ROOT\channels\start_bridges.py" --name omniclaw-channels

# Save to auto-start on Windows boot
pm2 startup
pm2 save
```

### Check all via PowerShell:
```powershell
# View running ports
@(19000, 3000, 3002, 5001, 9621) | ForEach-Object {
    $conn = Get-NetTCPConnection -LocalPort $_ -ErrorAction SilentlyContinue
    $status = if ($conn) { "✅ RUNNING" } else { "❌ STOPPED" }
    Write-Host "$status  port $_"
}
```

---

## 📋 When adding new plugins/services with localhost

> **Rule:** When injecting any plugin featuring a new server/dashboard/localhost, it MUST be added to this board.
>
> Template for additions:
> ```
> ### 🔷 [Plugin Name] — [Short description]
> \```bash
> cd "$OMNICLAW_ROOT\plugins\<name>"
> [start command]
> \```
> | URL | http://localhost:<port> |
> | Port | <number> |
> | Requires | [dependencies] |
> | Reason | [why it's used] |
> ```

---

*Update this file whenever a new plugin requiring activation is added.*
