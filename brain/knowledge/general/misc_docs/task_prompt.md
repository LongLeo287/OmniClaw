---
id: task-prompt
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.092544
---

﻿# task_prompt.md — Fill Template execution_template.md

## Instructions

After the user approves the brainstorm, Antigravity populates this template
and save to project workspace (DO NOT save in OmniClaw core).
This file is task_file placed in blackboard.json.

---
## How to Fill

```
Replace all [placeholders] with actual information.
Each STEP must have: Role, Depends on, Input, Action, Output, Success.
There is always STEP QA Final and STEP FINAL (Synthesis).
```

---
## Template (Copy and Fill)

```markdown
TASK_ID : TASK-[YYYYMMDD]-[NNN]
WORKSPACE : [absolute path to project workspace]
PRIORITY : HIGH | MEDIUM | LOW
CREATED_AT : [ISO 8601]
APPROVED_BY : Antigravity (user approved [date])
PROJECT : [project name]
PHASE : [Phase X: Phase name]
BACKGROUND : [1-3 context sentences]
GOAL: [1 sentence: what is it]
CONSTRAINTS :
  - [constraint 1]
  - [constraint 2]

---
### STEP 1: [Description name]
Role : RESEARCHER | DEVELOPER | QA
Depends on : none
Input : [what]
Action : [do something specific]
Output : [what is produced]
Success : [check how to know success]

QA Checklist:
- [ ] [check specifically 1]
- [ ] [check specifically 2]

---
### STEP 2: [Description name]
Role: DEVELOPER
Depends on : STEP 1
[... similar...]

---
### STEP N: QA Final Review
Role: QA
Depends on : ALL previous DEVELOPER steps
Action : Full QA pass on all outputs
Success : All critical checks pass, no regressions

---
### STEP FINAL: Synthesis & Handoff
Role : DEVELOPER (acting as Manager)
Depends on : STEP N
Action : Aggregate receipts → update blackboard.json
Output : blackboard.json result.summary updated
```

---
## After Filling

1. Save the file to: `[workspace]/task_file.md`
2. Update `blackboard.json`:
   ```json
   {
     "handoff_trigger": "READY",
     "task_file": "[workspace]/task_file.md"
   }
   ```
3. Run `handoff_to_claude_code.ps1`
