---
id: output-format
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:24.553115
---

# Code Review Output Templates

## Standard Issue Block

````markdown
### 🔴 [BLOCKER]

**File**: `auth.ts`
**Issue**: SQL Injection risk in `login` function.
**Why**: Direct string concatenation allows attackers to bypass auth.
**Fix**: Use parameterized queries.

```typescript
db.query('SELECT * FROM users WHERE id = $1', [userId]);
```
````

```

## Severity Levels

| Tag | Meaning |
| :--- | :--- |
| `[BLOCKER]` | Security risk, crash, or broken build. Must fix. |
| `[MAJOR]` | Logic error, performance issue, or tech debt. |
| `[NIT]` | Variable naming, comment typos, minor structure. |
```
