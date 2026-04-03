---
id: lean-spec-template
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:24.332023
---

# Technical Spec: [Feature Name]

**Type**: Lean Spec | **Engineer**: [User]

## 1. Goal (The "Why")

_One sentence: What does this feature do and why?_

## 2. Core Logic (The "How")

- **Trigger**: User clicks X / API call Y.
- **Process**:
  1.  Step 1
  2.  Step 2
- **Outcome**: DB updated / UI changes.

## 3. Data Model (Schema Changes)

```sql
-- Short description of changes
ALTER TABLE x ADD COLUMN y;
```

## 4. API Contract (Endpoints)

- `POST /api/v1/resource`
  - Input: `{ "field": "value" }`
  - Output: `201 Created`

## 5. Implementation Steps (Checklist)

- [ ] Backend: ...
- [ ] Frontend: ...
- [ ] Tests: ...
