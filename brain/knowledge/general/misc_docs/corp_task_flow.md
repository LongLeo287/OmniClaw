---
id: corp-task-flow
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:10.402719
---

# Department: operations
# corp-task-flow.md â€” CEO â†’ C-Suite â†’ Manager â†’ Worker â†’ QA Flow
# Version: 1.0 | Updated: 2026-03-17
# Authority: Tier 2 (Operations) / Corp Mode

---

## Overview

This workflow defines how a single piece of work flows through all 5 levels
of OmniClaw Corp from conception to completion.

```
CEO           â”€â”€â–º WRITE MISSION + PRIORITIES
    â”‚
C-SUITE       â”€â”€â–º TRANSLATE TO DEPT GOALS
    â”‚
DEPT MANAGER  â”€â”€â–º CREATE TASK CARD + ASSIGN WORKER
    â”‚
WORKER        â”€â”€â–º EXECUTE + WRITE RECEIPT
    â”‚
GATE          â”€â”€â–º REVIEW (if qa_required)
    â”‚
MANAGER       â”€â”€â–º RECEIVE RESULT + UPDATE BRIEF
    â”‚
C-SUITE       â”€â”€â–º KPI UPDATE + REPORT TO CEO
    â”‚
CEO           â”€â”€â–º READ RESULTS + NEXT DECISION
```

---

## Step 1: CEO â†’ Mission

CEO writes to `brain/memory/system_memory/mission.md`:
```markdown
## Mission â€” [DATE]
Strategic Focus: [1-2 sentences]
Priorities this cycle:
  1. [Dept]: [specific goal]
  2. [Dept]: [specific goal]
  3. [Dept]: [specific goal]
Budget constraint: [any cost controls]
Deadline: [if applicable]
```

---

## Step 2: C-Suite â†’ Department Specs (Spec-Driven Intent)

Each C-Suite member reads mission â†’ translates to concrete Spec-Driven Intents:

```
CTO reads â†’ Engineering, QA, IT Specs
CMO reads â†’ Marketing, Support, Content Specs
COO reads â†’ Operations, HR, Security Specs
CFO reads â†’ Finance budget constraints
CSO reads â†’ Strategy, Legal, R&D Specs
```

C-Suite writes to `brain/memory/blackboard.json` for each dept:
```json
{
  "dept": "<dept-name>",
  "cycle": "N",
  "spec_intent": "<concise what-to-build spec>",
  "kpi_targets": ["<metric>: <value>"],
  "priority": "HIGH | MEDIUM | LOW",
  "deadline": "<date or ASAP>"
}
```

---

## Step 3: Manager â†’ Spec Card

Dept head reads blackboard â†’ creates actionable Spec Cards for Workers (never micromanage "how" to code, only provide "what" the spec requires):

Write to `subagents/mq/<dept>_tasks.md`:
```markdown
## Spec Card: <ID> â€” <title>
Assigned to: <worker-agent>
Dept: <dept>
Context: <2-3 sentences of context (include memory reference if relevant)>
Spec / Acceptance Criteria:
  - [ ] <requirement 1>
  - [ ] <requirement 2>
Deadline: <estimate>
LLM tier: economy | balanced | premium
QA required: true | false
Output path: <where to write the output>
Skills suggested: [<skill-id>]
```

---

## Step 4: Worker â†’ Execution

Worker reads task card â†’ executes WORKER_PROMPT.md loop:

```
1. Load SKILL matching task type
2. <thought> dry-run plan </thought>
3. Execute in atomic steps
4. Verify against acceptance criteria
5. Write receipt to telemetry/receipts/<dept>/<T-ID>.json
6. Update task card status: DONE | FAILED
7. If qa_required: true â†’ route to gate
8. If FAILED (2-strike) â†’ write L1 escalation
```

---

## Step 5: Gate Review (if qa_required)

```
Add item to correct gate queue:
  GATE_QA       â†’ subagents/mq/qa_review_queue.md
  GATE_CONTENT  â†’ subagents/mq/gate_content_queue.md
  GATE_SECURITY â†’ automatic (security_grc monitors autonomously)
  GATE_LEGAL    â†’ subagents/mq/legal_review_queue.md

Gate agent runs checklist from APPROVAL_GATES.md:
  PASS        â†’ notify manager. Proceed.
  FAIL        â†’ return to worker with specific fixes required
  CONDITIONAL â†’ proceed with stated conditions

Receipt stored: telemetry/qa_receipts/<gate>/<T-ID>.json
```

---

## Step 6: Manager â†’ Brief Update

After all tasks complete (or cycle ends):
```
Manager writes:
- Updated task statuses in subagents/mq/<dept>_tasks.md
- Daily brief to brain/memory/system_memory/daily_briefs/<dept>.md
- Lesson to corp/memory/departments/<dept>.md (if learned anything)
- Any L2 escalations to brain/memory/system_memory/escalations.md
```

---

## Step 7: C-Suite â†’ KPI Update

```
C-Suite reads all dept briefs in their domain:
1. Update kpi_scoreboard.json with actual values
2. Flag any yellow/red KPIs
3. Write C-Suite dispatch summary
4. Escalate L3 items to CEO if any
```

---

## Step 8: CEO â†’ Decision

CEO reads:
- `brain/memory/system_memory/kpi_scoreboard.json`
- `brain/memory/system_memory/escalations.md`
- `brain/memory/system_memory/proposals/`

CEO decides:
- APPROVE items â†’ log to decisions_log.md
- REJECT with reason â†’ escalations.md response
- DEFER with ETA
- Set next cycle priorities â†’ update mission.md

---

## Task ID Convention

```
<DEPT-ABBR>-<CYCLE>-<SEQ>

Examples:
  ENG-01-001  â†’ Engineering, Cycle 1, Task 1
  MKT-01-003  â†’ Marketing, Cycle 1, Task 3
  SEC-02-001  â†’ Security, Cycle 2, Task 1
  HR-01-002   â†’ HR, Cycle 1, Task 2
```

---

*"A task that doesn't flow through the hierarchy isn't a corporate task. It's chaos."*

