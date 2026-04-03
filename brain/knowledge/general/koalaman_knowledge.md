---
id: koalaman-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:01.556460
---

# KNOWLEDGE EXTRACT: koalaman
> **Extracted on:** 2026-03-30 17:38:56
> **Source:** koalaman

---

## File: `shellcheck-precommit.md`
```markdown
# 📦 koalaman/shellcheck-precommit [🔖 PENDING/APPROVE]
🔗 https://github.com/koalaman/shellcheck-precommit


## Meta
- **Stars:** ⭐ 124 | **Forks:** 🍴 16
- **Language:** Shell | **License:** NOASSERTION
- **Last updated:** 2026-03-02
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Pre-commit hook for ShellCheck

## README (trích đầu)
```
# ShellCheck pre-commit hook

This is the official [pre-commit hook](https://pre-commit.com/) for
[ShellCheck](https://github.com/koalaman/shellcheck),
the static analysis tool for shell scripts.

Activate by adding it to your `.pre-commit-config.yaml`:

```sh
repos:
-   repo: https://github.com/koalaman/shellcheck-precommit
    rev: v0.11.0
    hooks:
    -   id: shellcheck
#       args: ["--severity=warning"]  # Optionally only show errors and warnings
```

#### Why a separate repo?

This repo keeps the pre-commit hook out of the critical path of ShellCheck
releases, reducing the number of things that can go wrong. This in turn helps
ensure a smoother `pre-commit autoupdate`. 


```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

