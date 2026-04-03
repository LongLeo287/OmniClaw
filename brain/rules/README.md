---
id: readme
type: system_rule
registered: true
---

# ⚖️ DEPARTMENTAL RULE MATRIX
**Function:** This directory contains the specific regulations, boundaries of authority, and System-Level Standard Operating Procedures (SOPs) for individual Departments and Agents within the OmniClaw Ecosystem.

## 🗂️ Rule Space Architecture
To keep `CLAUDE.md` and `GEMINI.md` lightweight (containing only the System Boot Protocol), all detailed rules regarding specific agents or departments are mandated to be stored here. AI Agents must implicitly load their respective departmental rule file into memory upon activation.

### 🛡️ Standard Rule Structure (Recommended):
File naming convention: `[dept_id]_rules.md` (e.g., `engineering_rules.md`, `qa_testing_rules.md`)

```markdown
# DEPARTMENT RULES: [DEPT NAME]
**Department ID:** `[dept_id]`

## 1. Scope of Authority
- [List permitted read/write directories]
- [List strictly forbidden operations (Blacklist)]

## 2. Approval Gates (QA & Security)
- [List workflows that require QA/Security sign-off]
- All code commits must bear the stamp/sign-off of `[agent_name]`.

## 3. Memory & Tenant Policy
- This department's memory is isolated at `brain/memory/tenants/[dept_id]/`.
- Agents within this department are STRICTLY FORBIDDEN from reading the cross-tenant memory of `[other_dept]`.
```

## 🔄 Dynamic Mapping
These Rule files are dynamically mapped to the Organizational Graph. Agents are instructed to autonomously locate and adhere to their departmental ruleset based on the `[Dept Name] + _rules.md` naming convention.
