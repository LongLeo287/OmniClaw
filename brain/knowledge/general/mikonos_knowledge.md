---
id: mikonos-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.174970
---

# KNOWLEDGE EXTRACT: mikonos
> **Extracted on:** 2026-03-30 17:42:49
> **Source:** mikonos

---

## File: `zk-steward-companion.md`
```markdown
# 📦 mikonos/zk-steward-companion [🔖 PENDING/APPROVE]
🔗 https://github.com/mikonos/zk-steward-companion


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Shell | **License:** Unknown
- **Last updated:** 2026-03-10
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Companion skills for ZK Steward (agency-agents): link-proposer, index-note, strategic-advisor, workflow-audit

## README (trích đầu)
```
# ZK Steward Companion Skills

Companion skills for **[ZK Steward](https://github.com/msitarzewski/agency-agents)** (from [The Agency](https://github.com/msitarzewski/agency-agents)). Use these with the ZK Steward agent to get the full Luhmann-style knowledge-base workflow.

## What’s in this repo

| Skill | Purpose |
|-------|---------|
| **link-proposer** | For new notes: suggest link candidates (3-way search), keyword/index entries, and one Gegenrede (counter-question). |
| **index-note** | Create or update index/MOC entries; daily sweep; network repair from health reports. |
| **strategic-advisor** | Default when intent is unclear: multi-perspective analysis, trade-offs, action options. |
| **workflow-audit** | Check multi-phase flows (e.g. deep-learning, meeting-note) against a checklist; Deming + Gawande style. |
| **structure-note** | Reading-order and logic trees for articles, project docs, or complex topics; Folgezettel-style argument chains. |
| **random-walk** | Random walk the knowledge network; tension/forgotten/island modes; script in `random-walk/scripts/get_random_notes.sh`. |
| **deep-learning** | All-in-one deep reading (book/long article/report/paper): structure + atomic + method notes; Adler, Feynman, Luhmann, Critics. |

Skills are in **Chinese** (original language). Paths in the docs (e.g. `05_每日记录/`, `03_索引/`, `memory/`) follow the original vault layout—**adapt them to your own folder names** when installing.

## Install (Cursor)

1. Copy the `skills/` folder into your project so that Cursor can see it as skills, e.g.:
   - **Option A**: Copy each skill under `.cursor/skills/` in your repo:
     ```bash
     cp -r skills/link-proposer .cursor/skills/
     cp -r skills/index-note   .cursor/skills/
     cp -r skills/strategic-advisor .cursor/skills/
     cp -r skills/workflow-audit .cursor/skills/
     cp -r skills/structure-note .cursor/skills/
     cp -r skills/random-walk .cursor/skills/
     cp -r skills/deep-learning .cursor/skills/
     ```
   - **Option B**: Clone this repo as a subfolder and add it to your Cursor rules/skills path if your setup supports it.

2. **Path customization**: If your vault uses different folders (e.g. `daily/`, `index/`), edit the paths inside each SKILL.md and, for link-proposer and random-walk, the script `get_random_notes.sh` in each (or set env vars `NOTES_DIR`, `INDEX_DIR` before running).

3. **Random-notes script** (link-proposer path C, random-walk): From your vault root, run so path defaults work:
   ```bash
   export NOTES_DIR="05_每日记录"   # or your daily-notes folder
   export INDEX_DIR="03_索引"      # or your index folder
   ./path/to/skills/link-proposer/scripts/get_random_notes.sh --mode tension --count 6
   ```

## Install (Claude Code / other tools)

Copy the contents of each `skills/<name>/SKILL.md` into your tool’s agent/skill format (e.g. Claude Code agents). Ensure paths and any script paths are adjusted for your environment.

## ZK Steward agent

Get the ZK Steward personal
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

