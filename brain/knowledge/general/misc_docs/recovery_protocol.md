---
id: recovery-protocol
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.197011
---

# Department: operations
---
description: How to recover agent state after a session reset, context compression, or context rot
---

# Recovery Protocol â€” OmniClaw Corp
# Version: 2.0 | Updated: 2026-03-22
# Authority: Tier 2 (Operations)
# Trigger: Automatically by CLAUDE.md boot fallback | Manually when agent detects context rot

---

## What is Context Rot?

Context rot = agent loses awareness of:
- Current active task or cycle phase
- Recent decisions or changes
- Which governance rules apply right now

Signs: agent asks questions already answered, re-does completed work, ignores open blockers.

---

## Recovery Steps

### Step 1: Re-Boot from CLAUDE.md

Follow the full boot sequence in `CLAUDE.md` Section 2:

```
STEP 1  â†’ Read CLAUDE.md                        (this re-grounds you)
STEP 2  â†’ Read brain/memory/SOUL.md     (identity + values)
STEP 3  â†’ Read brain/memory/GOVERNANCE.md
STEP 4  â†’ Read brain/indices/FAST_AGENT_INDEX.json
STEP 5  â†’ Read brain/memory/THESIS.md
STEP 6  â†’ Read brain/memory/report_formats.md
STEP 7  â†’ Read brain/memory/blackboard.json   â† KEY: find current task
STEP 8  â†’ Read brain/registry/SKILL_REGISTRY.json
```

---

### Step 2: Read Blackboard State

`brain/memory/blackboard.json` tells you:

| Field | Meaning |
|-------|---------|
| `handoff_trigger` | READY / COMPLETE / BLOCKED / CYCLE_START / null |
| `task_payload.task_id` | Active task ID |
| `task_payload.task_file` | Path to task definition |
| `task_payload.workspace_path` | Where to work |
| `corp_state.corp_cycle_status` | IDLE / RUNNING |
| `open_items[]` | Pending items this cycle |

---

### Step 3: Check Subagent Message Queue

Read messages addressed to you:
```
subagents/mq/claude_code_tasks.md         â† tasks from C-Suite/managers
subagents/mq/<dept>_escalation.md         â† pending L1 escalations
subagents/mq/BOOT_SYNC_*.md               â† boot sync messages
```

---

### Step 4: Check Recent Receipts

```
telemetry/receipts/                        â† what was completed last session
brain/brain/memory/system_memory/daily_briefs/   â† what depts reported
```

---

### Step 5: State Re-Broadcast

After reading the above, briefly state reconstructed context to CEO:

```
"Context recovered.
 Current cycle: [N] | Status: [corp_cycle_status]
 Active task: [task_id] â€” [description]
 Last action: [from most recent receipt]
 Open blockers: [from open_items or escalations]
 Ready to continue."
```

---

## Emergency Recovery (BLOCKED state)

If blackboard shows `handoff_trigger: "BLOCKED"`:

```
1. Read: blocked_task.reason + escalation_ref
2. Read: subagents/mq/<dept>_escalation.md for full context
3. Check: has manager responded? (look for response below the L1 escalation)
4. If YES â†’ read manager instructions â†’ resume with new approach
5. If NO  â†’ report BLOCKED status to CEO, await instruction
6. Do NOT retry the same failed approach
```

---

## Git Rollback (if files corrupted)

If file system state is corrupted from a failed Claude Code run:

```powershell
cd <workspace_path>
git log --oneline -5              # find last good snapshot commit
git reset --hard <commit-hash>    # roll back to that state
```

Snapshots are created by `claude_code_handoff.md` Step 1 before each run.

---

*"A recovered agent that knows where it is â€” is better than a confused agent that keeps going."*

