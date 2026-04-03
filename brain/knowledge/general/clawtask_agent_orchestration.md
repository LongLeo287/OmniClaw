---
id: clawtask-agent-orchestration
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.940301
---

# Knowledge File: ClawTask — AI Agent Task Orchestration Platform
# Source: https://vnrom.net/2026/03/clawta[REDACTED_API_KEY]ts-khong-chi-la-mot-kanban-board/
# Ingested: 2026-03-19 | Tier: T1 (Internal — OmniClaw uses ClawTask)
# Author: Duy Nghien (vnROM)

---

## SUMMARY

ClawTask is a **task orchestration platform for AI agents** — not just a traditional Kanban board. It is designed for the **human + AI agent collaboration** model, where agents maintain state, workflows have checkpoints, and humans can intervene at the exact right moment.

**OmniClaw is using ClawTask at:** `$OMNICLAW_ROOT\tools\clawtask\`
**Server:** `clawtask_api.py` — runs on port 7474

---

## WHY CLAWTASK IS DIFFERENT

Traditional task management tools (Trello, Notion, Jira) are designed for **humans**. ClawTask is designed for **human + AI agent collaboration**.

| Problem with traditional tools | ClawTask Solution |
|--------------------|-------------------|
| Agents lack a standard mechanism to receive tasks | API/MCP layer for agents to register + receive tasks |
| No pausing flow to ask humans for clarification | **Clarification Flow** — precise workflow pausing |
| No storage for intermediate outputs | **Notebook layer** per task |
| Unable to accurately track blocked tasks | Task states: todo/inprogress/blocked/review/done |
| Lack of recurring workflows | **Recurring task definitions** |

---

## 5 CORE FEATURES

### 1. Task Lifecycle Management
Agents act as stateful workers, not just chatbots:
```
todo → inprogress → [blocked/review] → done
                 ↕
          awaiting_clarification  (NEW — to be implemented)
```

### 2. Clarification Flow ⭐ (Most critical feature)
When an agent lacks information → creates clarification tied to task → workflow PAUSES → human responds → agent resumes.

Instead of: blindly guessing / failing silently / outputting incorrect data.

```
Agent hits blocker
  → POST /api/tasks/:id/clarification
  → {"question": "...", "context": "...", "blocking": true}
  → Dashboard displays badge 🔴 NEEDS CLARIFICATION
  → Human responds via dashboard
  → Agent polls GET /api/tasks/:id/clarifications
  → Agent continues with answer
```

### 3. Notebook Layer
Stores intermediate outputs: research notes, reasoning chains, audit checklists, analysis logs.

```
POST /api/tasks/:id/note
  → {"content": "...", "type": "reasoning|research|checkpoint"}
```

### 4. Recurring Tasks
Auto-generates tasks on schedule: daily briefs, server checks, SLA reviews, weekly reports.

### 5. MCP + REST Endpoints
```
POST /mcp/*              — MCP protocol
/api/mcp or /mcp/rpc    — streamable RPC
Standard REST API        — usable by any HTTP-capable agent
```

---

## OmniClaw — INTEGRATION STATUS

| Feature | Status | File |
|-----------|--------|------|
| Basic task CRUD | ✅ Implemented | clawtask_api.py |
| Agent briefing | ✅ Implemented | /api/agent-briefing/:id |
| GitNexus proxy | ✅ Implemented | /api/gitnexus/* |
| Change alerts | ✅ Implemented | /api/intel/change-alert |
| Clarification flow | 🔶 ADDED 2026-03-19 | clawtask_api.py |
| Notebook layer | 🔶 ADDED 2026-03-19 | clawtask_api.py |
| Recurring tasks | ⬜ Planned | — |
| MCP protocol | ⬜ Planned | — |

---

## CLARIFICATION FLOW DESIGN (OmniClaw)

```
Mapping department → clarification targets:
- engineering tasks     → CTO
- finance tasks         → CFO
- client tasks          → COO → CEO
- security tasks        → CSO → COO
- content tasks         → content_review dept head
- default               → department head
```

---

## LINKS

- Article: https://vnrom.net/2026/03/clawta[REDACTED_API_KEY]ts-khong-chi-la-mot-kanban-board/
- Tool path: `$OMNICLAW_ROOT\tools\clawtask\`
- API file: `$OMNICLAW_ROOT\tools\clawtask\clawtask_api.py`
- Related: `planning_pmo` department (owner of ClawTask)
- Related: `monitoring_inspection` (consumes ClawTask data)

---

## TAGS
`task-orchestration` `ai-agents` `workflow` `kanban` `clarification` `human-in-the-loop` `MCP` `REST-API` `T1-internal`
