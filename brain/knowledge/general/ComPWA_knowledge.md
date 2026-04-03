---
id: compwa-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:09.673550
---

# KNOWLEDGE EXTRACT: ComPWA
> **Extracted on:** 2026-03-30 17:35:37
> **Source:** ComPWA

---

## File: `taplo-pre-commit.md`
```markdown
# 📦 ComPWA/taplo-pre-commit [🔖 PENDING/APPROVE]
🔗 https://github.com/ComPWA/taplo-pre-commit
🌐 https://github.com/tamasfe/taplo

## Meta
- **Stars:** ⭐ 32 | **Forks:** 🍴 8
- **Language:** N/A | **License:** Unknown
- **Last updated:** 2026-02-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A pre-commit hook for Taplo, a TOML formatter written in Rust

## README (trích đầu)
```
# Pre-commit hook for the Taplo TOML formatter

Mirror of [github.com/tamasfe/taplo](https://github.com/tamasfe/taplo) and the [`taplo` PyPI package](https://pypi.org/project/taplo) for [pre-commit](https://pre-commit.com).

### Using Taplo with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/ComPWA/taplo-pre-commit
    rev: v0.9.3
    hooks:
      - id: taplo-format
```

To get the [latest release](https://github.com/ComPWA/taplo-pre-commit/releases), run

```shell
pre-commit autoupdate --repo https://github.com/ComPWA/taplo-pre-commit
```

Optionally, you can also install the Taplo linter as a pre-commit hook:

```yaml
repos:
  - repo: https://github.com/ComPWA/taplo-pre-commit
    rev: v0.9.3
    hooks:
      - id: taplo-format
      - id: taplo-lint
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

