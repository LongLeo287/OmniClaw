---
id: report-prompt
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.853966
---

## Instructions

After reading blackboard.json + receipts from Claude Code,
Antigravity uses this template to generate a report for the user.
Language: VIETNAMESE. Send as a Mermaid walkthrough.

---
## Report Structure (Mandatory)

### Header
```
## Report: [Task name — from blackboard.json]
📅 Completed: [timestamp]
```

### Overview
[1-2 sentences summarizing the results: what was done, what was the outcome]

### Execution Flow
```mermaid
flowchart LR
    S([🚀 Start]) --> D1[Step 1: DevName]
    D1 --> Q1{QA Review}
    Q1 -->|PASS| D2[Step 2: DevName]
    Q1 -->|FAIL| F1[Fix → Retry]
    F1 --> Q1
    D2 --> Q2{QA Review}
    Q2 -->|PASS| R([✅ Complete])
    Q2 -->|BLOCKED| B([🔴 Blocked])
```

### Detailed Results

| Step | Role | Result | Modified Files |
|------|------|--------|----------------|
| 1 | DEVELOPER | ✅ PASS | path/to/file.ts |
| 2 | QA | ✅ PASS | — |
| 3 | DEVELOPER | ⚠️ PARTIAL | path/to/file2.ts |

### Key Learnings
[From cognitive_reflector — max 3 points]
- 💡 [lesson 1]
- 💡 [lesson 2]

### Next Steps
[Recommended actions — from open_items]
- [ ] [next task to do]

---
*Would you like to drill down into any specific step?*
