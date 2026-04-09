# Contributing to Agent Teams Lite

Thanks for contributing. Agent Teams Lite enforces a strict **issue-first workflow** — every change starts with an approved issue.

---

## Contribution Workflow

```
Open Issue → Get status:approved → Open PR → Add type:* label → Review & Merge
```

### Step 1: Open an Issue

Use the correct template:
- **Bug Report** — for bugs
- **Feature Request** — for new features or improvements

> ⚠️ Blank issues are disabled. You must use a template.

Fill in all required fields. Your issue will automatically receive the `status:needs-review` label.

### Step 2: Wait for Approval

A maintainer will review the issue and add the `status:approved` label if it's accepted for implementation.

**Do not open a PR until the issue is approved.** Automated checks will block PRs that reference unapproved issues.

### Step 3: Open a Pull Request

Once the issue is approved:

1. Fork the repo and create a branch from `main` (see branch naming below)
2. Implement your change with conventional commits
3. Open a PR using the PR template — **link the approved issue** with `Closes #N`
4. Add exactly **one `type:*` label** to the PR (see label system below)

### Branch Naming

Branch names MUST follow this format:

```
type/description
```

**Regex:** `^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)\/[a-z0-9._-]+$`

**Examples:** `feat/user-login`, `fix/zsh-glob-error`, `docs/installation-guide`

Allowed types: `feat`, `fix`, `chore`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `revert`

### Step 4: Automated PR Checks

Checks run automatically on every PR:

| Check | What it verifies |
|-------|-----------------|
| **Check Issue Reference** | PR body contains `Closes #N`, `Fixes #N`, or `Resolves #N` |
| **Check Issue Has status:approved** | The linked issue has the `status:approved` label |
| **Check PR Has type:\* Label** | PR has exactly one `type:*` label |
| **Shellcheck** | Shell scripts pass `shellcheck` linting |

All checks must pass before a PR can be merged.

---

## Label System

### Type Labels (required on every PR — pick exactly one)

| Label | Color | Use for |
|-------|-------|---------|
| `type:bug` | 🔴 | Bug fixes |
| `type:feature` | 🔵 | New features |
| `type:docs` | 🔵 | Documentation-only changes |
| `type:refactor` | 🟣 | Code refactoring with no behavior change |
| `type:chore` | ⚪ | Maintenance, tooling, dependencies |
| `type:breaking-change` | 🔴 | Breaking changes |

### Status Labels (set by maintainers)

| Label | Meaning |
|-------|---------|
| `status:needs-review` | Awaiting maintainer review (auto-applied to new issues) |
| `status:approved` | Approved for implementation — PRs can now be opened |

### Priority Labels (set by maintainers)

`priority:high`, `priority:medium`, `priority:low`

---

## PR Rules

- Keep PR scope focused — one logical change per PR
- Use [conventional commits](https://www.conventionalcommits.org/) format
- Run `shellcheck` on any modified shell scripts before pushing
- Update docs in the same PR when behavior changes
- Do not include `Co-Authored-By` trailers in commits

### Conventional Commit Format

Commit messages MUST match this regex:

```
^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9\._-]+\))?!?: .+
```

**Format:** `type(scope): description` or `type: description`

- `type` — required: `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`
- `(scope)` — optional, lowercase with `a-z0-9._-`
- `!` — optional, indicates breaking change
- `description` — required, starts after `: `

**Examples:**

```
feat(scripts): add multi-model setup for OpenCode
fix(skills): correct engram topic key format in sdd-apply
docs(readme): update installation instructions
refactor(skills): extract shared persistence logic
chore(ci): add shellcheck to PR validation workflow
perf(scripts): reduce setup.sh execution time
style(skills): fix markdown formatting
test(scripts): add setup.sh integration tests
ci(workflows): add branch name validation
revert: undo broken setup change
feat!: redesign skill loading system
```

Types map to labels: `feat` → `type:feature`, `fix` → `type:bug`, `docs` → `type:docs`, `refactor` → `type:refactor`, `chore`/`style`/`test`/`build`/`ci` → `type:chore`, `perf` → `type:feature`, `revert` → `type:bug`.

---

## Skill Authoring Standard

Repository skills live in `skills/`.

Use a **hybrid format**:

1. Structured base (purpose, when to use, critical rules, checklists)
2. Cookbook section (`If / Then / Example`) for repetitive actions

Why hybrid:
- Structured base protects correctness and architecture intent
- Cookbook improves execution consistency for common flows
