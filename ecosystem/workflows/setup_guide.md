# Department: operations
# OmniClaw Corp Ã¢â‚¬â€ Setup Guide
# Sau khi clone, chÃ¡Â»â€° cÃ¡ÂºÂ§n 2 bÃ†Â°Ã¡Â»â€ºc lÃƒÂ  chÃ¡ÂºÂ¡y Ã„â€˜Ã†Â°Ã¡Â»Â£c

## Ã¢Å¡Â¡ Quick Start

```powershell
# 1. Clone repo (Code LÃµi)
git clone <repo-url> "d:\OmniClaw Corp"

# 2. Auto-Setup: KÃ©o Data Vault (HuggingFace) & CÃ i Dependencies
cd "d:\OmniClaw Corp\OmniClaw REMOTE\scripts"
powershell -ExecutionPolicy Bypass -File setup.ps1

# 3. Khá»Ÿi Ä‘á»™ng Master Dashboard
"$OMNICLAW_ROOT\launcher\OmniClaw Corp.cmd"
```

---

## System Requirements (cÃƒÂ i 1 lÃ¡ÂºÂ§n nÃ¡ÂºÂ¿u chÃ†Â°a cÃƒÂ³)

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.10+ | [python.org](https://python.org/downloads) hoÃ¡ÂºÂ·c `winget install Python.Python.3.12` |
| Node.js | 18+ | [nodejs.org](https://nodejs.org) hoÃ¡ÂºÂ·c `winget install OpenJS.NodeJS` |
| Git | any | `winget install Git.Git` |
| Docker | any | [docker.com](https://docker.com/products/docker-desktop) |
| Ollama | any | [ollama.ai](https://ollama.ai/download) |

> **Bun, uv** Ã¢â‚¬â€ optional, cÃ¡ÂºÂ§n khi dÃƒÂ¹ng claude-mem hoÃ¡ÂºÂ·c cognee

---

## Python Dependencies

TÃ¡ÂºÂ¥t cÃ¡ÂºÂ£ trong `requirements.txt` Ã¢â‚¬â€ chÃ¡ÂºÂ¡y 1 lÃ¡ÂºÂ§n:

```powershell
pip install -r requirements.txt
```

| Package | DÃƒÂ¹ng cho |
|---------|---------|
| python-dotenv | ClawTask, AgAuto |
| pypdf | ClawTask (Ã„â€˜Ã¡Â»Âc PDF) |
| fastapi + uvicorn | ACP, AgAuto API |
| supabase | ClawTask backend |
| requests + httpx | HTTP general |
| mem0ai | Agent memory plugin |
| firecrawl-py | Web intelligence (Phase 2) |
| crewai | Multi-agent (Phase 4) |
| lightrag-hku | Knowledge graph (Phase 3) |

---

## Special Installs (cÃ¡ÂºÂ§n thÃƒÂªm bÃ†Â°Ã¡Â»â€ºc)

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

### nullclaw (binary Ã„â€˜ÃƒÂ£ cÃƒÂ³ sÃ¡ÂºÂµn)
```
# KhÃƒÂ´ng cÃ¡ÂºÂ§n cÃƒÂ i thÃƒÂªm Ã¢â‚¬â€ binary cÃƒÂ³ tÃ¡ÂºÂ¡i:
REMOTE\claws\nullclaw\zig-out\bin\nullclaw.exe
```

---

## External API Keys

ThÃƒÂªm vÃƒÂ o `ops/secrets/MASTER.env`:

```env
OPENROUTER_API_KEY=sk-or-...
FIRECRAWL_API_KEY=fc-...
```

---

*Dashboard: `launcher\OmniClaw Corp.cmd` Ã¢â€ â€™ [I] Install Manager Ã„â€˜Ã¡Â»Æ’ kiÃ¡Â»Æ’m tra trÃ¡ÂºÂ¡ng thÃƒÂ¡i*


