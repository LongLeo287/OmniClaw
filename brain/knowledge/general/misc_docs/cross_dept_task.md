---
id: cross-dept-task
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:15.613916
---

# Department: operations
---
description: Cross-department task protocol â€” when a task requires cooperation between two or more departments
---
# ops/workflows/cross-dept-task.md
# Version: 1.0 | 2026-03-25 | Owner: planning_pmo
# Trigger: Task requiring 2+ departments | Coordinator: pmo-agent
---

## When should this workflow be used?

- Task requires engineering + security (Example: deploy a new feature)
- Task requires research & development + registry (Example: new skill from research)
- Task requires content_intake + engineering (Example: integrate a new tool)
- Any task that has `cross_dept: true` in `task_backlog.json`
---

## Step 1: â€” CEO / Coordinator Creates Cross-Dept Task

```json
{
  "id": "CROSS-001",
  "title": "Task description",
  "depts": ["engineering", "security_grc"],
  "coordinator": "pmo-agent",
  "priority": "HIGH",
  "due": "YYYY-MM-DD",
  "deliverable": "Result: final output required"
}
```

Save to: `brain/brain/memory/system_memory/cross_dept_tasks.json`
---

## Step 2: â€” pmo-agent Dispatch

1. Read `cross_dept_tasks.json`, filter OPEN tasks
2. For each task â†’ create subâ€‘task for each department:
   - `subagents/mq/<dept>_tasks.md` â† append crossâ€‘dept task
3. Notify each department via blackboard: `cross_dept_signal`

```
Example: CROSS-001 â†’ engineering receives "Implement feature X"
                â†’ security_grc receives "Security review for feature X"
```
---

## Step 3: â€” Departments Execute Independently

- Each department writes its own brief: `BRIEF_<date>_cross_<task_id>.md`
- No need to wait for other departments (async)
- If blocked â†’ escalate via `corp/escalations.md`
---

## STEP 4 â€” pmo-agent Consolidates Results:

1. Collect all crossâ€‘dept briefs for `task_id`
2. Verify deliverable completeness
3. If complete â†’ mark `DONE`, notify CEO via Telegram
4. If missing â†’ ping lagging department

```
Slack/Telegram: "âœ… CROSS-001 completed â€” Engineering + Security submitted"
or: "âš ï¸ CROSS-001 lagging â€” security_grc has not submitted (SLA: 2h)"
```
---

## STEP 5 â€” CEO Approves (if needed)

- Task with `ceo_approval: true` â†’ CEO reviews synthesis brief
- CEO approves â†’ pmo-agent archives â†’ close task
- CEO rejects â†’ pmo-agent reâ€‘dispatch with feedback
---

## Template: cross_dept_tasks.json

```json
{
  "tasks": [
    {
      "id": "CROSS-001",
      "title": "...",
      "depts": ["dept1", "dept2"],
      "coordinator": "pmo-agent",
      "priority": "HIGH",
      "due": "YYYY-MM-DD",
      "deliverable": "...",
      "ceo_approval": false,
      "status": "OPEN",
      "created": "2026-03-25"
    }
  ]
}
```
---

*Workflow v1.0 | Owner: planning_pmo | Trigger: `cross_dept: true` in `task_backlog*`

