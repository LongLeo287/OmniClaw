---
id: setup-guide
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:12.548647
---

# Department: operations
# OmniClaw Corp â€” Setup Guide
# Sau khi clone, chá»‰ cáº§n 2 bÆ°á»›c lÃ  cháº¡y Ä‘Æ°á»£c

## âš¡ Quick Start

```powershell
# 1. Clone repo (Code Lõi)
git clone <repo-url> "d:\OmniClaw Corp"

# 2. Auto-Setup: Kéo Data Vault (HuggingFace) & Cài Dependencies
cd "d:\OmniClaw Corp\OmniClaw REMOTE\scripts"
powershell -ExecutionPolicy Bypass -File setup.ps1

# 3. Khởi động Master Dashboard
"$OMNICLAW_ROOT\launcher\OmniClaw Corp.cmd"
```

---

## System Requirements (cÃ i 1 láº§n náº¿u chÆ°a có)

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.10+ | [python.org](https://python.org/downloads) hoáº·c `winget install Python.Python.3.12` |
| Node.js | 18+ | [nodejs.org](https://nodejs.org) hoáº·c `winget install OpenJS.NodeJS` |
| Git | any | `winget install Git.Git` |
| Docker | any | [docker.com](https://docker.com/products/docker-desktop) |
| Ollama | any | [ollama.ai](https://ollama.ai/download) |

> **Bun, uv** â€” optional, cáº§n khi dùng claude-mem hoáº·c cognee

---

## Python Dependencies

Táº¥t cáº£ trong `requirements.txt` â€” cháº¡y 1 láº§n:

```powershell
pip install -r requirements.txt
```

| Package | Dùng cho |
|---------|---------|
| python-dotenv | ClawTask, AgAuto |
| pypdf | ClawTask (Ä‘á»c PDF) |
| fastapi + uvicorn | ACP, AgAuto API |
| supabase | ClawTask backend |
| requests + httpx | HTTP chung |
| mem0ai | Agent memory plugin |
| firecrawl-py | Web intelligence (Phase 2) |
| crewai | Multi-agent (Phase 4) |
| lightrag-hku | Knowledge graph (Phase 3) |

---

## Special Installs (cáº§n thêm bÆ°á»›c)

### MaxKB
```powershell
cd "$OMNICLAW_ROOT\plugins\MaxKB"
docker compose up -d
# UI: http://localhost:8080/maxkb
```

### claude-mem (trong Claude Code)
```
/plugin install claude-mem
```

### nullclaw (binary Ä‘ã có sáºµn)
```
# Không cáº§n cÃ i thêm â€” binary có táº¡i:
REMOTE\claws\nullclaw\zig-out\bin\nullclaw.exe
```

---

## External API Keys

Thêm vÃ o `ops/secrets/MASTER.env`:

```env
OPENROUTER_API_KEY=sk-or-...
FIRECRAWL_API_KEY=fc-...
```

---

*Dashboard: `launcher\OmniClaw Corp.cmd` â†’ [I] Install Manager Ä‘á»ƒ kiá»ƒm tra tráº¡ng thái*

