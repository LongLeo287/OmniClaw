---
description: Quick-reference selector for all OmniClaw report formats. Full definitions in brain/shared-context/report_formats.md
id: report_formats
type: corp_document
registered: true
---
---
## CRITICAL RULE (Never Skip)

ALL brainstorms, reports, and analyses TO THE CEO:
1. Write to an artifact `.md` file — NEVER paste inline in chat
2. Call `notify_user` with `PathsToReview` → always use the left panel
3. Wait for CEO feedback before proceeding to implementation

---
## Format Selector — CEO-Facing (Part A)

```
What are you presenting to CEO?
│
├─ Exploring a problem / comparing options?
│   └─► A1: Visual Brainstorm  [runes/brainstorm_prompt.md]
│
├─ High-stakes design / needs peer-review?
│   └─► A2: Multi-Agent Review [runes/multi_agent_brainstorm_prompt.md]
│        → Only after A1 is confirmed
│
├─ Product feature / new capability discovery?
│   └─► A3: BMAD Method        [runes/bmad_prompt.md]
│
├─ Logging a decision already made?
│   └─► A4: Decision Log       [runes/decision_log_prompt.md]
│
└─ Reporting completed work (post-execution)?
    └─► A5: Execution Receipt  [runes/execution_receipt_prompt.md]
```

---
## Format Selector — Corp System (Part B)

```
What corp format do you need?
│
├─ Dept status update each cycle?           → B1: DAILY_BRIEF
├─ Autonomous action audit trail?           → B2: TASK_RECEIPT
├─ Problem needs CEO decision?              → B3: ESCALATION_REPORT
├─ Show KPI board to CEO?                   → B4: KPI_SNAPSHOT
├─ Proposing new skill/workflow/resource?   → B5: PROPOSAL
├─ Security or system incident?             → B6: INCIDENT_REPORT
└─ Mid-task progress checkpoint?            → B7: PROGRESS_UPDATE
```

---
> Full templates, field definitions, and storage paths:
> **`brain/shared-context/report_formats.md`**
