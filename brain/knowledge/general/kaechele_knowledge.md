---
id: kaechele-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.962175
---

# KNOWLEDGE EXTRACT: kaechele
> **Extracted on:** 2026-03-30 17:38:14
> **Source:** kaechele

---

## File: `pre-commit-mirror-prettier.md`
```markdown
# 📦 kaechele/pre-commit-mirror-prettier [🔖 PENDING/APPROVE]
🔗 https://github.com/kaechele/pre-commit-mirror-prettier


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-01-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
mirror of the `prettier` npm package for pre-commit

## README (trích đầu)
```
# prettier mirror

Mirror of prettier package for pre-commit.

This mirror contains only stable versions.

For notes on how "stable" versions are determined see <https://github.com/kaechele/pre-commit-mirror-maker/blob/main/README.md>

For pre-commit: see <https://github.com/pre-commit/pre-commit>

For prettier: see <https://github.com/prettier/prettier>

## Using prettier with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/kaechele/pre-commit-mirror-prettier
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: prettier
```

*note*: only prettier versions >= 2.1.0 are supported

When using plugins with `prettier` you'll need to declare them under
`additional_dependencies`. For example:

```yaml
-   repo: https://github.com/kaechele/pre-commit-mirror-prettier
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: prettier
        additional_dependencies:
        -   prettier@2.1.2
        -   '@prettier/plugin-xml@0.12.0'
```

By default, all files are passed to `prettier`, if you want to limit the
file list, adjust `types` / `types_or` / `files`:

```yaml
    -   id: prettier
        types_or: [css, javascript]
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

