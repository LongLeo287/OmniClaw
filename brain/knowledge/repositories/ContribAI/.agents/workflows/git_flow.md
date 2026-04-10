---
description: Git branching strategy – defines the branching model, commit conventions, and merge policies
---

# Git Flow Workflow

## Branch Model

```
main ─────────────────────────────────── production-ready
  │
  ├─ feat/xyz ──── feature branch ── squash merge → main
  ├─ fix/abc ───── bug fix branch ── squash merge → main
  ├─ docs/readme ─ docs branch ───── squash merge → main
  └─ release/vX.Y ─ release prep ── merge → main + tag
```

## Steps

### Starting work
1. **Always start from latest main**
// turbo
```bash
git checkout main
git pull origin main
```

2. **Create a branch with the right prefix**
```bash
git checkout -b <prefix>/<short-kebab-description>
```

Prefixes:
| Prefix | Purpose | Example |
|--------|---------|---------|
| `feat/` | New feature | `feat/issue-driven-contributions` |
| `fix/` | Bug fix | `fix/rate-limit-retry` |
| `refactor/` | Code restructuring | `refactor/analyzer-pipeline` |
| `docs/` | Documentation | `docs/api-reference` |
| `test/` | Tests only | `test/memory-module` |
| `perf/` | Performance | `perf/parallel-analysis` |
| `chore/` | Maintenance | `chore/update-deps` |
| `ci/` | CI/CD changes | `ci/add-security-scan` |

### Committing
3. **Use conventional commits**
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Examples:
```
feat(analysis): add Django-specific security checks
fix(github): handle 403 rate limit with exponential backoff
refactor(llm): extract common prompt builder
docs(readme): add configuration reference
test(memory): add edge cases for duplicate PR detection
perf(analyzer): parallelize file content fetching
chore(deps): bump httpx to 0.28
```

### Creating a PR
4. **Push to remote**
```bash
git push origin <branch-name>
```

5. **Create PR on GitHub**
- Title matches the main commit message
- Description follows the PR template
- Assign reviewers
- Add labels

### Merging
6. **Squash merge feature branches**
All feature/fix branches should be squash-merged to keep main history clean.

7. **Never force push to main**
Main branch is protected. Only merge via PR.

### Keeping branch up to date
8. **Rebase on main when needed**
```bash
git fetch origin
git rebase origin/main
```

## Branch Rules
- `main` → Protected: requires PR, CI pass, 1 approval
- Feature branches → Short-lived (< 1 week)
- Delete branches after merge
- No direct commits to main
