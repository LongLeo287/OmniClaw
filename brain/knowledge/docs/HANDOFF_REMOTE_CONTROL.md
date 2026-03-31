# OmniClaw Corp â€” Remote Control System HANDOFF
# Project: nullclaw Telegram Bot + Automation Gateway
# Owner: CEO @LongLeo | Assigned: Scrum-Master (COO)
# Date: 2026-03-18 | Status: LIVE âœ…

---

## ðŸŽ¯ Project Overview

nullclaw adalah gateway tá»± Ä‘á»™ng hÃ³a chÃ­nh cá»§a OmniClaw Corp â€” káº¿t ná»‘i Telegram cá»§a CEO (@LongLeo) vá»›i toÃ n bá»™ há»‡ thá»‘ng AI agents. CEO Ä‘iá»u khiá»ƒn má»i thá»© qua chat.

---

## ðŸ“¦ Stack Hiá»‡n Táº¡i

| Component | Status | Location | Port |
|-----------|--------|----------|------|
| **nullclaw** (Telegram gateway) | ðŸŸ¢ LIVE | `REMOTE/claws/nullclaw/` | 3000 |
| **AstrBot v4.20.1** | ðŸŸ¡ INSTALLED | `plugins/AstrBot/` + `runtime/astrbot/` | 6185 |
| **ClawTask Dashboard** | ðŸŸ¢ LIVE | `tools/clawtask/` | 7474 |
| **LightRAG** | âš« IDLE | `plugins/LightRAG/` | â€” |
| **cognee** | âš« IDLE | `plugins/cognee/` | â€” |

---

## ðŸ¤– Bot Credentials (SECURE)

```
Platform:    Telegram
Bot Token:   [REDACTED_TELEGRAM_TOKEN]
Admin ID:    646106732 (@LongLeo)
LLM:         Gemini 2.0 Flash ([REDACTED_GEMINI_API_KEY])
Config:      <USER_PROFILE>\.nullclaw\config.json
Binary:      <AI_OS_ROOT>\REMOTE\claws\nullclaw\zig-out\bin\nullclaw.exe
```

Full credentials: `<AI_OS_ROOT>\secrets\.env.telegram`

---

## ðŸš€ Startup Commands

```powershell
# Khá»Ÿi Ä‘á»™ng há»‡ thá»‘ng Ä‘áº§y Ä‘á»§
powershell -ExecutionPolicy Bypass -File "<AI_OS_ROOT>\scripts\startup.ps1"

# Chá»‰ nullclaw bot
& "<AI_OS_ROOT>\REMOTE\claws\nullclaw\zig-out\bin\nullclaw.exe" gateway

# Chá»‰ ClawTask Dashboard
python -m http.server 7474 --directory "<AI_OS_ROOT>\tools\clawtask"

# Check bot status
& "<AI_OS_ROOT>\REMOTE\claws\nullclaw\zig-out\bin\nullclaw.exe" status
```

---

## ðŸ“‹ Sprint Tasks (Scrum-Master quáº£n lÃ½)

### ðŸ”´ HIGH â€” Ngay bÃ¢y giá»

- [ ] **TG-001** Test bot hoáº¡t Ä‘á»™ng: @LongLeo nháº¯n â†’ bot reply Gemini
- [ ] **TG-002** ThÃªm OmniClaw Corp system prompt chi tiáº¿t hÆ¡n vÃ o config
- [ ] **TG-003** Auto-start bot khi Windows boot (Task Scheduler)

### ðŸŸ¡ MEDIUM â€” Sprint nÃ y

- [ ] **omniclaw-004** AstrBot WebUI config: thÃªm Telegram token qua http://localhost:6185/
- [ ] **omniclaw-005** Plugin `astrbot_plugin_aios_corp` â€” test /clawtask command
- [ ] **omniclaw-006** Sync ClawTask â†’ JSON file Ä‘á»ƒ plugin Ä‘á»c Ä‘Æ°á»£c
- [ ] **REG-007** SKILL_REGISTRY.json update â€” promote LightRAG + cognee + crewAI lÃªn T2
- [ ] **LEG-008** GATE_LEGAL review `awesome-claude-skills` license

### ðŸ”µ LOW â€” Backlog

- [ ] **INF-009** ThÃªm Discord channel vÃ o nullclaw config
- [ ] **INF-010** Setup Tailscale tunnel Ä‘á»ƒ truy cáº­p remote (khÃ´ng chá»‰ localhost)
- [ ] **INF-011** nullclaw heartbeat.md â€” autonomous proactive checks
- [ ] **INF-012** LightRAG integration â€” RAG pipeline cho Research Agent
- [ ] **INF-013** cognee integration â€” Agent Memory Engine
- [ ] **INF-014** Zalo OA bot evaluation (cáº§n business account)
- [ ] **INF-015** CIV Batch 4 planning

---

## ðŸ”„ SOPs (Standard Operating Procedures)

### SOP-BOT-01: Khá»Ÿi Ä‘á»™ng bot hÃ ng ngÃ y

1. Open PowerShell as Admin
2. `& "<AI_OS_ROOT>\REMOTE\claws\nullclaw\zig-out\bin\nullclaw.exe" gateway`
3. Telegram â†’ nháº¯n "status" â†’ confirm reply

### SOP-BOT-02: Restart khi bot khÃ´ng pháº£n há»“i

1. `taskkill /F /IM nullclaw.exe`
2. Chá» 2 giÃ¢y
3. Khá»Ÿi Ä‘á»™ng láº¡i theo SOP-BOT-01

### SOP-BOT-03: Update config (system prompt, model, tools)

1. Edit `<USER_PROFILE>\.nullclaw\config.json`
2. Restart bot theo SOP-BOT-02
3. Test báº±ng tin nháº¯n Telegram

### SOP-CONFIG-01: Rebuild nullclaw binary

```powershell
powershell -ExecutionPolicy Bypass -File "<AI_OS_ROOT>\scripts\build-nullclaw.ps1"
```

---

## ðŸ—ºï¸ Roadmap

| Milestone | Target | Status |
|-----------|--------|--------|
| nullclaw Telegram bot LIVE | Mar 2026 | âœ… DONE |
| AstrBot WebUI configured | Mar 2026 | ðŸŸ¡ IN PROGRESS |
| ClawTask â†” Bot sync | Apr 2026 | âš« PLANNED |
| LightRAG RAG pipeline | Apr 2026 | âš« PLANNED |
| Discord + multi-channel | Apr 2026 | âš« PLANNED |
| Zalo OA integration | Q2 2026 | âš« PLANNED |
| Full autonomous operation | Q2 2026 | âš« PLANNED |

---

## ðŸ“ Agent Notes

### Orchestrator_Pro (CEO Assistant)
> Khi CEO nháº¯n qua Telegram, bot hiá»‡n táº¡i connect trá»±c tiáº¿p Gemini 2.0 Flash. ChÆ°a cÃ³ memory persistence giá»¯a cÃ¡c session â€” cáº§n setup SQLite memory backend.

### Scrum-Master (COO)
> Quáº£n lÃ½ sprint tasks trong file nÃ y vÃ  ClawTask dashboard (localhost:7474). Priority: TG-001 test live, sau Ä‘Ã³ TG-003 auto-start.

### Sw-Architect (CTO)
> nullclaw config hiá»‡n táº¡i dÃ¹ng Gemini OpenAI-compatible endpoint. CÃ³ thá»ƒ switch sang Anthropic báº¥t ká»³ lÃºc nÃ o báº±ng cÃ¡ch update `models.providers` vÃ  `agents.defaults.model.primary`.

### Registry-Manager
> REG-007 pending: promote LightRAG (T2 Primary RAG) + cognee (T2 Agent Memory) + crewAI (T2 Orchestration) trong SKILL_REGISTRY.json.

