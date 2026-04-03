---
id: cross-dept-task
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:15.613916
---

# Department: operations
---
description: Cross-department task protocol — when a task requires cooperation between two or more departments
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

## Step 1: — CEO / Coordinator Creates Cross-Dept Task

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

Save to: `brain/shared-context/corp/cross_dept_tasks.json`
---

## Step 2: — pmo-agent Dispatch

1. Read `cross_dept_tasks.json`, filter OPEN tasks
2. For each task → create sub‑task for each department:
   - `subagents/mq/<dept>_tasks.md` ← append cross‑dept task
3. Notify each department via blackboard: `cross_dept_signal`

```
Example: CROSS-001 → engineering receives "Implement feature X"
                → security_grc receives "Security review for feature X"
```
---

## Step 3: — Departments Execute Independently

- Each department writes its own brief: `BRIEF_<date>_cross_<task_id>.md`
- No need to wait for other departments (async)
- If blocked → escalate via `corp/escalations.md`
---

## STEP 4 — pmo-agent Consolidates Results:

1. Collect all cross‑dept briefs for `task_id`
2. Verify deliverable completeness
3. If complete → mark `DONE`, notify CEO via Telegram
4. If missing → ping lagging department

```
Slack/Telegram: "✅ CROSS-001 completed — Engineering + Security submitted"
or: "⚠️ CROSS-001 lagging — security_grc has not submitted (SLA: 2h)"
```
---

## STEP 5 — CEO Approves (if needed)

- Task with `ceo_approval: true` → CEO reviews synthesis brief
- CEO approves → pmo-agent archives → close task
- CEO rejects → pmo-agent re‑dispatch with feedback
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
