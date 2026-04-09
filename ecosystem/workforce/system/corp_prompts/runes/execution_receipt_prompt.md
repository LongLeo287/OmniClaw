---
description: Execution Receipt — post-execution report after Claude Code or Antigravity completes a task. Required for all significant executions.
id: execution_receipt_prompt
type: corp_document
registered: true
---
## MANDATORY DELIVERY RULE
Write to artifact file → notify_user → NEVER paste in chat

---
## ✅ Execution Receipt

**Task:** [task name]
**Executed by:** [Antigravity / Claude Code]
**Date:** [YYYY-MM-DD HH:MM]
**Status:** [COMPLETED ✅ / PARTIAL ⚠️ / FAILED ❌]

---
### 📋 Summary

> [Brief description of what was done — 2-3 sentences]

---
### 📁 Modified Files

| File | Change Type | Notes |
|------|-------------|-------|
| [path/to/file.py] | Created / Modified / Deleted | [...] |
| [path/to/file.md] | Created / Modified / Deleted | [...] |

---
### ⚡ Executed Commands

```bash
# List executed commands
$ [command 1]
$ [command 2]
```

---
### 🧪 Verification Results

| Test / Verification | Result | Notes |
|---------------------|--------|-------|
| [build / test / manual check] | ✅ Pass / ❌ Fail | [...] |

---
### ⚠️ Outstanding Issues

- [Issue 1] — Priority: High/Med/Low
- [Issue 2] — Priority: High/Med/Low

---
### ➡️ Proposed Next Steps

1. [...]
2. [...]
