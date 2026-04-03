---
description: "Perform deep cleaning, token clearing, and state archiving at session end."
id: workflow-post-session
version: "1.0"
updated_at: "2026-04-03"
type: workflow
platform: antigravity
tier: 1
trigger: "session ending signals detected by Antigravity"
---

# Workflow: Post-Session Handoff (Auto-Handoff)

> **Rule ref:** `GEMINI.md § rule: auto-handoff` — Antigravity automatically runs
> this workflow when session-ending signals are detected. CEO does NOT need to say
> "handoff", "update blackboard", or "write brief" — it's fully automatic.

---

## Trigger Signals (Auto-Detect)

| CEO Signal | Meaning | Action |
|-----------|---------|--------|
| "end session" / "wrap up" / "bye" | Session closing | Run immediately |
| "done" / "finished" / after final plan approval | Task complete, CEO done | Run immediately |
| CEO no reply after Antigravity finishes reporting | Session naturally closing | Run immediately |
| "start new session" / "restart" | Next session starting | Run old session handoff first |

---

## Steps (Execute in Order, Non-Blocking)

### Step 1 — Update Blackboard

**File:** `brain/memory/blackboard.json`

```json
{
  "session_end": "<ISO timestamp GMT+7>",
  "last_task": "<title of last completed task>",
  "corp_cycle_status": "IDLE",
  "handoff_trigger": "IDLE",
  "open_items": ["<list any unresolved items from session>"],
  "last_agent": "antigravity"
}
```

Rules:
- `corp_cycle_status` → set to `IDLE` (never leave as RUNNING at session end)
- `open_items` → list anything CEO asked but is not yet resolved
- Do NOT reset `active_campaign` — it persists across sessions

### Step 2 — Update HUD (Non-Blocking)

```
1. Run: python core/ops/omniclaw_startup.py --no-telegram --check-only
   → Captures current service state
2. Optionally update brain/memory/core/STATUS.json with session_end timestamp
3. Non-blocking: if this fails, continue to Step 3
```

### Step 3 — Write Daily Brief

**Path:** `brain/memory/daily/<YYYY-MM-DD>/brief_<YYYY-MM-DD>.md`

```markdown
---
date: <YYYY-MM-DD>
session_end: <timestamp>
agent: antigravity
campaign: <active_campaign>
---

# Session Brief — <YYYY-MM-DD>

## Completed
- <bullet list of what was done>

## Open Items
- <bullet list of unresolved tasks>

## Key Decisions
- <any architecture/governance decisions made>

## Next Session Priorities
- <what CEO should focus on next>
```

Create parent directory if not exists.

### Step 4 — Log Decisions

**File:** `brain/memory/corp_memory/global/decisions_log.md`

Append entry:
```markdown
## [<YYYY-MM-DD>] <Session Topic>
- **Decision:** <what was decided>
- **Rationale:** <why>
- **Impact:** <files changed / systems affected>
- **Agent:** antigravity | **Campaign:** <active_campaign>
```

Create file if not exists (with standard header).

### Step 5 — CEO Summary (Vietnamese, Max 5 Lines)

Output to CEO chat **after** all above steps complete:

```
📋 **Session Ended — <date>**
✅ Completed: <1-2 items>
📌 Open: <unresolved count> items → <brief description>
💾 Brief: brain/memory/daily/<date>/brief_<date>.md
🔄 Next Session: <suggested priority>
```

---

## On Failure

If any step fails:
- Log the failure to `brain/registry/cli_run.log`
- Continue to next step (non-blocking)
- Include failure note in Step 5 CEO summary
- Do NOT halt the entire handoff because of one failed step

---

## File Paths Reference

| Step | File |
|------|------|
| Blackboard | `brain/memory/blackboard.json` |
| HUD status | `brain/memory/core/STATUS.json` |
| Daily brief | `brain/memory/daily/<date>/brief_<date>.md` |
| Decisions log | `brain/memory/corp_memory/global/decisions_log.md` |
| Error log | `brain/registry/cli_run.log` |
