---
id: transloadit-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.976928
---

# KNOWLEDGE EXTRACT: transloadit
> **Extracted on:** 2026-03-30 17:55:21
> **Source:** transloadit

---

## File: `skills.md`
```markdown
# 📦 transloadit/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/transloadit/skills


## Meta
- **Stars:** ⭐ 1 | **Forks:** 🍴 0
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-11
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent skills for Transloadit

## README (trích đầu)
```
# Transloadit Skills

This repo hosts agent skills for Transloadit.

If you’re a developer/agent consuming this repo, start with the `transloadit` router skill and then jump into a specific `docs-*`, `transform-*`, or `integrate-*` skill.

## Install / Use

This repo is compatible with the `skills` installer CLI (https://skills.sh/).

Browse what’s available:
```bash
npx -y skills add https://github.com/transloadit/skills --list
```

Install into this project (or use `-g` for user-level):
```bash
npx -y skills add https://github.com/transloadit/skills --all
```

Install a single skill (direct path):
```bash
npx -y skills add https://github.com/transloadit/skills/tree/main/skills/docs-transloadit-robots
```

Local dev (already cloned):
```bash
npx -y skills add ./skills --list
npx -y skills add ./skills --all
```

Manual option (symlink the `skills/` catalog into your agent’s skill directory):
```bash
git clone https://github.com/transloadit/skills
ln -s /ABS/PATH/TO/THIS/REPO/skills ~/.codex/skills
ln -s /ABS/PATH/TO/THIS/REPO/skills ~/.claude/skills
ln -s /ABS/PATH/TO/THIS/REPO/skills ~/.gemini/skills
```

Note: this repo also contains developer-only skills under `.ai/dev-skills/` for working on this repo. The public catalog lives under `skills/`.

## Skill Catalog

Categories:
- `docs-*`: offline reference lookups (no API calls)
- `transform-*`: one-off transforms (CLI driven, outputs downloaded via `-o`)
- `integrate-*`: real-world integration guides (validated via `scenarios/` + E2E, but not requiring any test harness)

The public catalog is whatever currently lives under [`skills/`](/Users/kvz/code/skills/skills).
For a current list, use:

```bash
npx -y skills add https://github.com/transloadit/skills --list
```

Or inspect the directories under `skills/` directly.

Builtin template discovery (token-efficient NDJSON, good for agents):
```bash
npx -y @transloadit/node templates list --include-builtin exclusively-latest --fields id,name --json
```

## Conventions (For Agents)

- Prefer `npx -y @transloadit/node ...` for any Transloadit-side operations and use `-j/--json` when parsing output.
- Never expose `TRANSLOADIT_SECRET` to the browser; keep signing strictly server-side.
- `integrate-*` skills are written as real app integration playbooks (framework-agnostic where possible).
- `scenarios/` are internal reference implementations with E2E validation; they are not required by the skills.

## Notes

Repository layout:
- `skills/`: skill catalog (`skills/<name>/SKILL.md`)
- `scenarios/`: runnable reference implementations (E2E-validated)
- `scripts/`: internal harness tooling (not a skill)
- `starter-projects/`: starter templates used by the harness (not a skill)

Skill discovery is `SKILL.md`-based, so it’s fine for `starter-projects/` and `scenarios/` to be siblings of `skills/` without being interpreted as skills.

## Contributing

### Scenarios

`scenarios/` is for integration scenarios that can later be distilled into agent skills.

Wor
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

