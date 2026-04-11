---
id: notification-bridge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:13.028060
---

# Department: operations
---
description: OmniClaw notification routing â€” gá»­i alert qua Telegram, log há»‡ thá»‘ng, CEO dashboard
---
# notification-bridge.md â€” Notification Bridge Protocol
# Version: 1.0 | Created: 2026-03-24
# Owner: Antigravity (Tier 1)
# Trigger: Báº¥t ká»³ agent nÃ o cáº§n gá»­i alert/notification

---

## Overview

notification-bridge lÃ  lá»›p trung gian nháº­n notification tá»« má»i agent vÃ  route Ä‘úng channel:

```
Agent â†’ [notification-bridge] â†’ Telegram (CEO)
                              â†˜â†’ blackboard.json (system log)
                              â†˜â†’ telemetry/receipts/ (audit trail)
                              â†˜â†’ corp/escalations.md (náº¿u lÃ  escalation)
```

---

## Notification Types

| Type | Priority | Channel | Format |
|------|----------|---------|--------|
| `GAP_PROPOSAL` | HIGH | Telegram + blackboard | [A/B/C/D] options |
| `SECURITY_ALERT` | CRITICAL | Telegram + escalations.md | Immediate action needed |
| `CIV_COMPLETE` | NORMAL | blackboard only | Ticket status update |
| `CIV_REJECTED` | NORMAL | blackboard + Telegram | Reason + source |
| `SKILL_CREATED` | LOW | blackboard only | Skill name + path |
| `SYSTEM_ERROR` | HIGH | Telegram + escalations.md | Error context + fix suggestion |
| `CYCLE_COMPLETE` | NORMAL | blackboard | Phase 7 retro summary |
| `OPEN_ITEM_SLA` | HIGH | Telegram | Item ID + SLA breach |

---

## How Agents Send Notifications

### Format (any agent, any language):
```json
{
  "type": "GAP_PROPOSAL | SECURITY_ALERT | CIV_COMPLETE | ...",
  "priority": "CRITICAL | HIGH | NORMAL | LOW",
  "source_agent": "<agent-name>",
  "title": "<short title>",
  "body": "<message body>",
  "data": { "<extra context>" },
  "timestamp": "<ISO8601>"
}
```

### ANTIGRAVITY sends via:
- Telegram: `nullclaw_gateway` (start_nullclaw.ps1) â†’ nullclaw bot message
- blackboard: Update `open_items[]` or `last_actions_this_cycle[]`

---

## Telegram Channel Setup

Config at: `ops/secrets/MASTER.env`
```
TELEGRAM_BOT_TOKEN=<bot token>
TELEGRAM_CHAT_ID=<CEO chat ID>
NULLCLAW_GATEWAY=http://localhost:<nullclaw-port>
```

Tool: `tools/core_intel/` â€” nullclaw messenger module
Script: `start_nullclaw.ps1` (launcher/)

### Test notification:
```powershell
# Test tá»« PowerShell
$body = @{
    type = "SYSTEM_ERROR"
    priority = "NORMAL"
    title = "Test notification"
    body = "OmniClaw notification-bridge working âœ…"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:<nullclaw-port>/notify" -Method POST -Body $body -ContentType "application/json"
```

---

## GAP PROPOSAL Format (CEO nháº­n qua Telegram)

```
ðŸ†• GAP PROPOSAL â€” [GAP-2026-03-24-DOMAIN]

DOMAIN: <chÆ°a có agent/dept phá»¥ trách X>
CONTENT: <tên repo/URL Ä‘ã nháº­n>

Options:
[A] Táº¡o agent má»›i â†’ agent-auto-create.md
[B] Assign vÃ o dept gáº§n nháº¥t: <dept-name>
[C] Create new department â†’ dept-builder-agent
[D] Skip â€” lÆ°u reference, không táº¡o gÃ¬

Reply A/B/C/D trong 24h. Default: B náº¿u không reply.
GAP saved: corp/gaps/GAP-<date>-<domain>.md
```

---

## LightRAG Port Verification

LightRAG API: `http://localhost:9621`
```bash
# Test LightRAG (run in terminal):
curl http://localhost:9621/health
# Expected: {"status": "ok"}

# Start LightRAG (náº¿u DOWN):
cd tools/lightrag  # hoáº·c nÆ¡i cÃ i lightrag
python -m lightrag.api --host 0.0.0.0 --port 9621 --working-dir brain/knowledge/lightrag_db
```

Config: `brain/lightrag_adapter.py` vÃ  `ops/scripts/index_skills_lightrag.py`

---

## open-notebook Port Verification

open-notebook API: `http://localhost:5055`
```bash
# Test open-notebook (run in terminal):
curl http://localhost:5055/health
# Expected: 200 OK

# Start open-notebook (náº¿u DOWN):
# Ref: skills/ hoáº·c plugins/openrag/ directory
```

---

## KPI / Escalations / Mission â€” Correct Paths

> **CANONICAL PATH:** `brain/brain/memory/system_memory/`

| File | Correct Path |
|------|-------------|
| kpi_scoreboard.json | `brain/memory/system_memory/kpi_scoreboard.json` |
| escalations.md | `brain/brain/memory/system_memory/escalations.md` |
| mission.md | `brain/brain/memory/system_memory/mission.md` |
| proposals/ | `brain/brain/memory/system_memory/proposals/` |
| daily_briefs/ | `brain/brain/memory/system_memory/daily_briefs/` |

**corp/escalations.md** = redirect/alias. Real file = `brain/brain/memory/system_memory/escalations.md`

GEMINI.md boot references should use `brain/brain/memory/system_memory/` prefix.

---

*v1.0 | 2026-03-24 | notification-bridge covers ALL channels*

