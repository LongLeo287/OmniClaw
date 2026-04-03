---
description: "Fast session validation and environment check at session start."
id: workflow-boot-check
version: "1.0"
updated_at: "2026-04-03"
type: workflow
platform: antigravity
tier: 1
trigger: "every session start — fast validation before accepting CEO commands"
---

# Workflow: Boot Check (Fast Session Validation)

> **Purpose:** A lean, fast checklist Antigravity runs at session start.
> Replaces the need to read the entire GEMINI.md on every session.
> Ref: `GEMINI.md [rule-agent-mechanics-01]` — "boot file lean, keep context low"

---

## Checklist (Run in Order, <30 seconds total)

### ✅ 1. Blackboard Status

```
Read: brain/shared-context/blackboard.json
Check:
  [ ] `system_status`: If DOWN -> HARD-BLOCK. System core daemon has failed. DO NOT accept commands.
  [ ] `corp_cycle_status` = IDLE or ACTIVE (not RUNNING → stale, needs reset)
  [ ] `handoff_available` = TRUE. (If FALSE, do not interact with Claude Code).
  [ ] `open_items[]` — Report pending tasks to CEO.
```

### ✅ 2. Escalations

```
Check: brain/memory/corp_memory/escalations.md (if exists)
  [ ] Any [L3] items? → Alert CEO FIRST before anything else
  [ ] Any [L2] items? → Note in session summary
  [ ] No file = clean state ✅
```

### ✅ 3. Active Campaign

```
From blackboard.json → active_campaign
  [ ] If exists: remind CEO of current campaign context
  [ ] If "none": ready for new campaign
```



---

## Output Format (Report to CEO at Session Start)

Only report **issues** — not a full status dump. Keep it brief:

```
🟢 OmniClaw Boot OK — [Cycle 12 | Campaign: v12.0.0_zero_trust_hardening]
🔴 SYSTEM DOWN — Blackboard flags system failure. Handoff disabled.
📌 Open items (2): [item1], [item2]
```

If everything is clean:
```
🟢 OmniClaw Boot OK — System nominal. Ready.
```

---

## Skip Conditions

Skip this workflow if:
- CEO explicitly says "skip boot check" / "quick"
- This is a continuation of an active session (same context window)
- Only a quick question (no task execution planned)

---

## Time Budget

| Check | Max time |
|-------|---------|
| Blackboard read | < 0.5s |
| Escalations read | < 0.5s |
| **Total** | **< 1s** |
