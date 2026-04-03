---
id: github.com-roundtable02-tutor-skills-97705f30-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:17.504721
---

# KNOWLEDGE EXTRACT: github.com_RoundTable02_tutor-skills_97705f30
> **Extracted on:** 2026-04-01 16:25:14
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525115/github.com_RoundTable02_tutor-skills_97705f30

---

## File: `.gitignore`
```
.DS_Store
*.swp
*.swo
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 tak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# tutor-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-blue)](https://docs.anthropic.com/en/docs/claude-code)
[![Install with npx skills](https://img.shields.io/badge/npx_skills-add-green)](https://github.com/vercel-labs/skills)

Two [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills that turn any knowledge source into an **Obsidian StudyVault** and then quiz you on it — closing the loop from content to comprehension.

## How It Works

```
  Documents / Code                    Obsidian                    Quiz Session
 ┌──────────────────┐           ┌──────────────────┐          ┌──────────────────┐
 │  PDF, MD, HTML,  │  /tutor   │   StudyVault/    │  /tutor  │  4 questions per  │
 │  EPUB, source    │──setup──▶ │   structured     │────────▶ │  round, graded,   │
 │  code projects   │           │   interlinked    │          │  concept tracking  │
 └──────────────────┘           │   notes + MOC    │          └────────┬─────────┘
                                └──────────────────┘                   │
                                         ▲                             │
                                         └─────── progress updates ────┘
```

## Skills Overview

| Skill | Command | Purpose | Input | Output |
|-------|---------|---------|-------|--------|
| **tutor-setup** | `/tutor-setup` | Generate a StudyVault | Documents or source code | Obsidian vault with notes, dashboards, practice questions |
| **tutor** | `/tutor` | Interactive quiz tutor | An existing StudyVault | Quiz sessions with concept-level progress tracking |

## Quick Start

### One-line install (recommended)

```bash
npx skills add RoundTable02/tutor-skills
```

> Requires [npx skills](https://github.com/vercel-labs/skills) — works with Claude Code, Cursor, Windsurf, and more.

### Manual install

```bash
git clone https://github.com/RoundTable02/tutor-skills.git
cd tutor-skills
./install.sh
```

### Step 1: Generate a StudyVault

```bash
cd ~/study-materials/          # or any source code project
claude
> /tutor-setup
```

### Step 2: Start Quizzing

```bash
claude
> /tutor
```

---

## tutor-setup

Transforms knowledge sources into a structured Obsidian StudyVault. Mode is auto-detected:

| Marker Found | Mode |
|---|---|
| `package.json`, `pom.xml`, `build.gradle`, `Cargo.toml`, `go.mod`, etc. | Codebase Mode |
| No project markers | Document Mode |

### Document Mode

Turns PDFs, text files, web pages, and other sources into comprehensive study notes.

- Auto-scans working directory for source files (PDF, TXT, MD, HTML, EPUB)
- Extracts and analyzes content with verified source mapping
- Generates concept notes with comparison tables, ASCII diagrams, and exam patterns
- Creates practice questions with hidden answers (active recall via fold callouts)
- Builds a dashboard with Map of Content (MOC), Quick Reference, and Exam Traps
- Full interlinking with `[[wiki-links]]` across all notes

**Phases**

| Phase | Name | Description |
|-------|------|-------------|
| D1 | Source Discovery | Scan, extract, and verify source content mapping |
| D2 | Content Analysis | Build topic hierarchy and dependency map |
| D3 | Tag Standard | Define English kebab-case tag registry |
| D4 | Vault Structure | Create numbered folders per topic |
| D5 | Dashboard | MOC, Quick Reference, Exam Traps |
| D6 | Concept Notes | Structured notes with tables, diagrams, callouts |
| D7 | Practice Questions | Active recall with fold callouts (8+ per topic) |
| D8 | Interlinking | Cross-reference all notes with wiki-links |
| D9 | Self-Review | Verify against quality checklist |

**Generated structure**

```
StudyVault/
  00-Dashboard/          # MOC + Quick Reference + Exam Traps
  01-<Topic1>/           # Concept notes + practice questions
  02-<Topic2>/
  ...
```

### Codebase Mode

Generates a new-developer onboarding vault from a source code project.

- Auto-detects tech stack, architecture patterns, and module boundaries
- Traces request flows and data flows end-to-end
- Creates per-module notes with key files, public interfaces, and dependency maps
- Generates onboarding exercises (code reading, configuration, debugging, extension)
- Builds a dashboard with architecture overview, module map, API surface, and getting started guide

**Phases**

| Phase | Name | Description |
|-------|------|-------------|
| C1 | Project Exploration | Scan files, detect tech stack, map layout |
| C2 | Architecture Analysis | Identify patterns, trace flows, map modules |
| C3 | Tag Standard | Define `#arch-*`, `#module-*`, `#pattern-*` registry |
| C4 | Vault Structure | Create dashboard + per-module folders |
| C5 | Dashboard | MOC with module map, API surface, getting started |
| C6 | Module Notes | Purpose, key files, interface, flow, dependencies |
| C7 | Exercises | Code reading, config, debugging, extension tasks |
| C8 | Interlinking | Cross-link all modules and exercises |
| C9 | Self-Review | Verify against quality checklist |

**Generated structure**

```
StudyVault/
  00-Dashboard/          # MOC + Quick Reference + Getting Started
  01-Architecture/       # System overview, request flow, data flow
  02-<Module1>/          # Per-module notes
  03-<Module2>/
  ...
  NN-DevOps/             # Build, deploy, CI/CD
  NN+1-Exercises/        # Onboarding exercises
```

---

## tutor

Interactive quiz tutor that tracks what you know and don't know at the **concept level**. Works with any StudyVault generated by `tutor-setup`.

### Session Types

| Type | When Available | Focus |
|------|----------------|-------|
| Diagnostic | Unmeasured areas (⬜) exist | Broad assessment of new areas |
| Drill weak areas | Weak areas (🟥/🟨) exist | Targeted practice on struggles |
| Choose a section | Always | Study any area on demand |
| Hard-mode review | All areas 🟩/🟦 | Challenge mastered material |

### Quiz Flow

1. Detects your StudyVault and reads the learning dashboard
2. Presents session options based on your current proficiency
3. Delivers 4 questions per round (4 options each, zero hints)
4. Grades answers and explains mistakes
5. Updates concept files and dashboard automatically

### Progress Tracking

Proficiency is tracked per area with emoji badges:

| Badge | Level | Rate |
|-------|-------|------|
| 🟥 | Weak | 0–39% |
| 🟨 | Fair | 40–69% |
| 🟩 | Good | 70–89% |
| 🟦 | Mastered | 90–100% |
| ⬜ | Unmeasured | No data |

Concept-level tracking stores attempts, correct count, last tested date, and error notes for wrong answers — so drill sessions rephrase missed concepts in new contexts.

---

## The Learning Cycle

```
           ┌────────────────────────────┐
           │   /tutor-setup             │
           │   Generate StudyVault      │
           └──────────┬─────────────────┘
                      │
                      ▼
           ┌────────────────────────────┐
           │   Read & review notes      │
           │   in Obsidian              │
           └──────────┬─────────────────┘
                      │
                      ▼
           ┌────────────────────────────┐
           │   /tutor                   │
           │   Take diagnostic quiz     │◀──────────┐
           └──────────┬─────────────────┘           │
                      │                              │
                      ▼                              │
           ┌────────────────────────────┐           │
           │   Review weak areas        │           │
           │   in Obsidian              │           │
           └──────────┬─────────────────┘           │
                      │                              │
                      ▼                              │
           ┌────────────────────────────┐           │
           │   /tutor                   │           │
           │   Drill weak concepts      │───────────┘
           └────────────────────────────┘
```

## Requirements

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured
- [Obsidian](https://obsidian.md/) (recommended) to open and navigate the generated vault

## Repository Structure

```
tutor-skill/
├── skills/
│   ├── tutor-setup/              # Vault generation skill
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── templates.md
│   │       ├── codebase-workflow.md
│   │       ├── quality-checklist.md
│   │       └── codebase-templates.md
│   └── tutor/                    # Interactive quiz skill
│       ├── SKILL.md
│       └── references/
│           └── quiz-rules.md
├── examples/
├── install.sh
├── uninstall.sh
├── README.md
└── LICENSE
```

## Uninstall

```bash
./uninstall.sh
```

Or manually:

```bash
rm -rf ~/.claude/skills/tutor-setup
rm -rf ~/.claude/skills/tutor
```

## License

[MIT](LICENSE)
```

## File: `install.sh`
```bash
#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS=("tutor-setup" "tutor")

for skill in "${SKILLS[@]}"; do
  SKILL_DIR="$HOME/.claude/skills/$skill"

  if [ -d "$SKILL_DIR" ]; then
    echo "$skill skill already exists at $SKILL_DIR"
    printf "Overwrite? (y/N): "
    read -r answer
    if [ "$answer" != "y" ] && [ "$answer" != "Y" ]; then
      echo "Skipping $skill."
      continue
    fi
  fi

  mkdir -p "$SKILL_DIR/references"
  cp "$SCRIPT_DIR/skills/$skill/SKILL.md" "$SKILL_DIR/"
  cp "$SCRIPT_DIR/skills/$skill/references/"* "$SKILL_DIR/references/"
  echo "Installed $skill to $SKILL_DIR"
done

echo ""
echo "Done! Usage in Claude Code:"
echo "  /tutor-setup  — Generate a StudyVault from documents or code"
echo "  /tutor        — Start an interactive quiz session"
```

## File: `uninstall.sh`
```bash
#!/bin/bash
set -e

SKILLS=("tutor-setup" "tutor")

for skill in "${SKILLS[@]}"; do
  SKILL_DIR="$HOME/.claude/skills/$skill"

  if [ -d "$SKILL_DIR" ]; then
    rm -rf "$SKILL_DIR"
    echo "Removed $skill from $SKILL_DIR"
  else
    echo "$skill not found at $SKILL_DIR (skipping)"
  fi
done
```

## File: `skills/tutor/SKILL.md`
```markdown
---
name: tutor
description: >
  Interactive quiz tutor for Obsidian StudyVault learning. Use when the user wants to:
  (1) Take a diagnostic assessment of their knowledge,
  (2) Study or review specific sections/topics,
  (3) Drill weak areas identified in previous sessions,
  (4) Check their learning progress or dashboard,
  or says things like "quiz me", "test me", "let's study", "/tutor", "학습", "퀴즈", "평가".
---

# Tutor Skill

Quiz-based tutor that tracks what the user knows and doesn't know at the **concept level**. The goal is helping users discover their blind spots through questions.

## File Structure

```
StudyVault/
├── *dashboard*              ← Compact overview: proficiency table + stats
└── concepts/
    ├── {area-name}.md       ← Per-area concept tracking (attempts, status, error notes)
    └── ...
```

- **Dashboard**: Only aggregated numbers. Links to concept files. Stays small forever.
- **Concept files**: One per area. Tracks each concept with attempts, correct count, date, status, and error notes. Grows proportionally to unique concepts tested (bounded).

## Workflow

### Phase 0: Detect Language

Detect user's language from their message → `{LANG}`. All output and file content in `{LANG}`.

### Phase 1: Discover Vault

1. Glob `**/StudyVault/` in project
2. List section directories
3. Glob `**/StudyVault/*dashboard*` to find dashboard
4. If found, read it. Preserve existing file path regardless of language.
5. If not found, create from template (see Dashboard Template below)

If no StudyVault exists, inform user and stop.

### Phase 2: Ask Session Type

**MANDATORY**: Use AskUserQuestion to let the user choose what to do. Analyze the dashboard to build context-aware options, then present them.

Read the dashboard proficiency table and build options based on current state:

1. If unmeasured areas (⬜) exist → include "Diagnostic" option targeting those areas
2. If weak areas (🟥/🟨) exist → include "Drill weak areas" option naming the weakest area(s)
3. Always include "Choose a section" option so the user can pick any area
4. If all areas are 🟩/🟦 → include "Hard-mode review" option

Present these as an AskUserQuestion with header "Session" and concise descriptions showing which areas each option targets. The user MUST select before proceeding.

### Phase 3: Build Questions

1. Read markdown files in target section(s)
2. If drilling weak area: also read `concepts/{area}.md` to find 🔴 unresolved concepts — rephrase these in new contexts (don't repeat the same question)
3. Craft exactly 4 questions following `references/quiz-rules.md`

**CRITICAL**: Read `references/quiz-rules.md` before crafting ANY question. Zero hints allowed.

### Phase 4: Present Quiz

Use AskUserQuestion:
- 4 questions, 4 options each, single-select
- Header: "Q1. Topic" (max 12 chars)
- Descriptions: neutral, no hints

### Phase 5: Grade & Explain

1. Show results table (question / correct answer / user answer / result)
2. Wrong answers: concise explanation
3. Map each question to its area

### Phase 6: Update Files

#### 1. Update concept file (`concepts/{area}.md`)

For each question answered:
- **New concept**: Add row to table + if wrong, add error note under `### 오답 메모` (or localized equivalent)
- **Existing 🔴 concept answered correctly**: Increment attempts & correct, change status to 🟢, keep error note (learning history)
- **Existing 🟢 concept answered wrong again**: Increment attempts, change status back to 🔴, update error note

Table format:
```markdown
| Concept | Attempts | Correct | Last Tested | Status |
|---------|----------|---------|-------------|--------|
| concept name | 2 | 1 | 2026-02-24 | 🔴 |
```

Error notes format (only for wrong answers):
```markdown
### Error Notes

**concept name**
- Confusion: what the user mixed up
- Key point: the correct understanding
```

#### 2. Update dashboard

- Recalculate per-area stats from concept files (sum attempts/correct across all concepts in that area)
- Update proficiency badges: 🟥 0-39% · 🟨 40-69% · 🟩 70-89% · 🟦 90-100% · ⬜ no data
- Update stats: total questions, cumulative rate, unresolved/resolved counts, weakest/strongest

Dashboard stays compact — no session logs, no per-question details.

## Dashboard Template

Create when no dashboard exists. Filename localized to `{LANG}`. Example in English:

```markdown
# Learning Dashboard

> Concept-based metacognition tracking. See linked files for details.

---

## Proficiency by Area

| Area | Correct | Wrong | Rate | Level | Details |
|------|---------|-------|------|-------|---------|
(one row per section, last column = [[concepts/{area}]] link)
| **Total** | **0** | **0** | **-** | ⬜ Unmeasured | |

> 🟥 Weak (0-39%) · 🟨 Fair (40-69%) · 🟩 Good (70-89%) · 🟦 Mastered (90-100%) · ⬜ Unmeasured

---

## Stats

- **Total Questions**: 0
- **Cumulative Rate**: -
- **Unresolved Concepts**: 0
- **Resolved Concepts**: 0
- **Weakest Area**: -
- **Strongest Area**: -
```

## Concept File Template

Create per area when first question is asked. Example:

```markdown
# {Area Name} — Concept Tracker

| Concept | Attempts | Correct | Last Tested | Status |
|---------|----------|---------|-------------|--------|

### Error Notes

(added as concepts are missed)
```

## Important Reminders

- ALWAYS read `references/quiz-rules.md` before creating questions
- NEVER include hints in option labels or descriptions
- NEVER use "(Recommended)" on any option
- Randomize correct answer position
- After grading, ALWAYS update both concept file AND dashboard
- Communicate in user's language
```

## File: `skills/tutor/references/quiz-rules.md`
```markdown
# Quiz Design Rules

## Zero-Hint Policy (CRITICAL)

Every question must be answerable ONLY by someone who actually knows the material.

1. **Option descriptions**: NEVER reveal correctness
   - BAD: `label: "stderr"`, `description: "Error output stream used by Cloud Run for error classification"`
   - GOOD: `label: "stderr"`, `description: "Standard error stream"`

2. **No "(Recommended)" tag** on any option

3. **Randomize** correct answer position — never always first or last

4. **Question phrasing**: Ask about behavior/purpose/output, don't hint at the answer
   - BAD: "Which error stream does error() use?"
   - GOOD: "Where does error() method output go?"

5. **Plausible distractors**: Wrong options must be real concepts from the domain, representing common misconceptions

## Question Types

1. **Factual recall**: "What HTTP status code is returned when...?"
2. **Conceptual understanding**: "Why does the system use X pattern?"
3. **Behavioral prediction**: "What happens when X fails?"
4. **Comparison/distinction**: "What is the difference between X and Y?"
5. **Debugging scenario**: "Given this error, what is the most likely cause?"

## Difficulty Balancing

- Diagnostic: easy 40%, medium 40%, hard 20%
- Weak-area drill: medium 30%, hard 70%
- Review: all levels evenly

## Drilling Unresolved Concepts

When targeting 🔴 concepts from concept files:
- Do NOT repeat the exact same question — rephrase in a new context
- Test the same underlying knowledge from a different angle
- E.g., if user confused "400 vs 422", ask a scenario question where they must choose the correct status code for a new situation

## AskUserQuestion Format

- 4 questions per round, 4 options each, single-select
- Header: max 12 chars, "Q1. Topic"

## File Update Protocol

After grading:
1. Update `concepts/{area}.md` — add/update concept rows + error notes
2. Update dashboard — recalculate area stats from concept files
3. Badges: 🟥 0-39% · 🟨 40-69% · 🟩 70-89% · 🟦 90-100% · ⬜ no data

## Language Rule

All file content and output in the user's detected language. Badge emojis are universal.
```

## File: `skills/tutor-setup/SKILL.md`
```markdown
---
name: tutor-setup
description: >
  Transforms knowledge sources into an Obsidian StudyVault. Two modes:
  (1) Document Mode — PDF/text/web sources → study notes with practice questions.
  (2) Codebase Mode — source code project → onboarding vault for new developers.
  Mode is auto-detected based on project markers in CWD.
argument-hint: "[source-path-or-url]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
---

# Tutor Setup — Knowledge to Obsidian StudyVault

## CWD Boundary Rule (ALL MODES)

> **NEVER access files outside the current working directory (CWD).**
> All source scanning, reading, and vault output MUST stay within CWD and its subdirectories.
> If the user provides an external path, ask them to copy the files into CWD first.

## Mode Detection

On invocation, detect mode automatically:

1. **Check for project markers** in CWD:
   - `package.json`, `pom.xml`, `build.gradle`, `Cargo.toml`, `go.mod`, `Makefile`,
     `*.sln`, `pyproject.toml`, `setup.py`, `Gemfile`
2. **If any marker found** → **Codebase Mode**
3. **If no marker found** → **Document Mode**
4. **Tie-break**: If `.git/` is the sole indicator and no source code files (`*.ts`, `*.py`, `*.java`, `*.go`, `*.rs`, etc.) exist, default to Document Mode.
5. Announce detected mode and ask user to confirm or override.

---

## Document Mode

> Transforms knowledge sources (PDF, text, web, epub) into study notes.
> Templates: [templates.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/executing_marketing_campaigns/reference/templates.md)

### Phase D1: Source Discovery & Extraction

1. **Auto-scan CWD** for `**/*.pdf`, `**/*.txt`, `**/*.md`, `**/*.html`, `**/*.epub` (exclude `node_modules/`, `.git/`, `dist/`, `build/`, `StudyVault/`). Present for user confirmation.
2. **Extract text (MANDATORY tools)**:
   - **PDF → `pdftotext` CLI ONLY** (run via Bash tool). NEVER use the Read tool directly on PDF files — it renders pages as images and wastes 10-50x more tokens. Convert to `.txt` first, then Read the `.txt` file.
     ```bash
     pdftotext "source.pdf" "/tmp/source.txt"
     ```
   - If `pdftotext` is not installed, install it first: `brew install poppler` (macOS) or `apt-get install poppler-utils` (Linux).
   - URL → WebFetch
   - Other formats (`.md`, `.txt`, `.html`) → Read directly.
3. **Read extracted `.txt` files** — understand scope, structure, depth. Work exclusively from the converted text, never from the raw PDF.
4. **Source Content Mapping (MANDATORY for multi-file sources)**:
   - Read **cover page + TOC + 3+ sample pages from middle/end** for EVERY source file
   - **NEVER assume content from filename** — file numbering often ≠ chapter numbering
   - Build verified mapping: `{ source_file → actual_topics → page_ranges }`
   - Flag non-academic files and missing sources
   - Present mapping to user for verification before proceeding

### Phase D2: Content Analysis

1. Identify topic hierarchy — sections, chapters, domain divisions.
2. Separate concept content vs practice questions.
3. Map dependencies between topics.
4. Identify key patterns — comparisons, decision trees, formulas.
5. **Full topic checklist (MANDATORY)** — every topic/subtopic listed. Drives all subsequent phases.

> **Equal Depth Rule**: Even a briefly mentioned subtopic MUST get a full dedicated note supplemented with textbook-level knowledge.

6. **Classification completeness**: When source enumerates categories ("3 types of X"), every member gets a dedicated note. Scan for: "types of", "N가지", "categories", "there are N".
7. **Source-to-note cross-verification (MANDATORY)**: Record which source file(s) and page range(s) cover each topic. Flag untraceable topics as "source not available".

### Phase D3: Tag Standard

Define tag vocabulary before creating notes:
- **Format**: English, lowercase, kebab-case (e.g., `#data-hazard`)
- **Hierarchy**: top-level → domain → detail → technique → note-type
- **Registry**: Only registered tags allowed. Detail tags co-attach parent domain tag.

### Phase D4: Vault Structure

Create `StudyVault/` with numbered folders per [templates.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/executing_marketing_campaigns/reference/templates.md). Group 3-5 related concepts per file.

### Phase D5: Dashboard Creation

Create `00-Dashboard/`: MOC, Quick Reference, Exam Traps. See [templates.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/executing_marketing_campaigns/reference/templates.md).

- **MOC**: Topic Map + Practice Notes + Study Tools + Tag Index (with rules) + Weak Areas (with links) + Non-core Topic Policy
- **Quick Reference**: every heading includes `→ [[Concept Note]]` link; all key formulas
- **Exam Traps**: per-topic trap points in fold callouts, linked to concept notes

### Phase D6: Concept Notes

Per [templates.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/executing_marketing_campaigns/reference/templates.md). Key rules:
- YAML frontmatter: `source_pdf`, `part`, `keywords` (MANDATORY)
- **source_pdf MUST match verified Phase D1 mapping** — never guess from filename
- If unavailable: `source_pdf: 원문 미보유`
- `[[wiki-links]]`, callouts (`[!tip]`, `[!important]`, `[!warning]`), comparison tables > prose
- ASCII diagrams for processes/flows/sequences
- **Simplification-with-exceptions**: general statements must note edge cases

### Phase D7: Practice Questions

Per [templates.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/executing_marketing_campaigns/reference/templates.md). Key rules:
- Every topic folder MUST have a practice file (8+ questions)
- **Active recall**: answers use `> [!answer]- 정답 보기` fold callout
- Patterns use `> [!hint]-` / `> [!summary]-` fold callouts
- **Question type diversity**: ≥60% recall, ≥20% application, ≥2 analysis per file
- `## Related Concepts` with `[[wiki-links]]`

### Phase D8: Interlinking

1. `## Related Notes` on every concept note
2. MOC links to every concept + practice note
3. Cross-link concept ↔ practice; siblings reference each other
4. Quick Reference sections → `[[Concept Note]]` links
5. Weak Areas → relevant note + Exam Traps; Exam Traps → concept notes

### Phase D9: Self-Review (MANDATORY)

Verify against [quality-checklist.md](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/development/jupyter-notebook/references/quality-checklist.md) **Document Mode** section. Fix and re-verify until all checks pass.

---

## Codebase Mode

> Generates a new-developer onboarding StudyVault from a source code project.
> Full workflow: [codebase-workflow.md](references/codebase-workflow.md)
> Templates: [codebase-templates.md](references/codebase-templates.md)

### Phase Summary

| Phase | Name | Key Action |
|-------|------|------------|
| C1 | Project Exploration | Scan files, detect tech stack, read entry points, map directory layout |
| C2 | Architecture Analysis | Identify patterns, trace request flow, map module boundaries and data flow |
| C3 | Tag Standard | Define `#arch-*`, `#module-*`, `#pattern-*`, `#api-*` tag registry |
| C4 | Vault Structure | Create `StudyVault/` with Dashboard, Architecture, per-module, DevOps, Exercises folders |
| C5 | Dashboard | MOC (Module Map + API Surface + Getting Started + Onboarding Path) + Quick Reference |
| C6 | Module Notes | Per-module notes: Purpose, Key Files, Public Interface, Internal Flow, Dependencies |
| C7 | Onboarding Exercises | Code reading, configuration, debugging, extension exercises (5+ per major module) |
| C8 | Interlinking | Cross-link modules, architecture ↔ implementations, exercises ↔ modules |
| C9 | Self-Review | Verify against [quality-checklist.md](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/development/jupyter-notebook/references/quality-checklist.md) **Codebase Mode** section |

See [codebase-workflow.md](references/codebase-workflow.md) for detailed per-phase instructions.

---

## Language

- Match source material language (Korean → Korean notes, etc.)
- **Tags/keywords**: ALWAYS English
```

## File: `skills/tutor-setup/references/codebase-templates.md`
```markdown
# Codebase Mode — Templates Reference

## Vault Folder Structure

```
StudyVault/
  00-Dashboard/          # MOC + Quick Reference + Getting Started
  01-Architecture/       # System overview, request flow, data flow
  02-<Module1>/          # Per-module notes
  03-<Module2>/
  ...
  NN-DevOps/             # Build, deploy, CI/CD, env config
  NN+1-Exercises/        # Onboarding exercises
```

## Dashboard MOC Template

```markdown
---
module: dashboard
path: 00-Dashboard
keywords: MOC, onboarding, architecture, <project-name>
---

# <Project Name> — Onboarding Map

#dashboard #onboarding

## Architecture Overview
- Pattern: <architectural pattern>
- Tech stack: <languages, frameworks, key libraries>
- → [[System Architecture]]
- → [[Request Flow]]

## Module Map
| Module | Purpose | Key Entry Point | Notes |
|--------|---------|-----------------|-------|
| <name> | <1-line purpose> | `<path>` | [[Module Note]] |

## API Surface
| Method | Path / Command | Module | Notes |
|--------|---------------|--------|-------|
| GET | `/endpoint` | <module> | [[API Note]] |

## Getting Started
1. Prerequisites: ...
2. Install: `<install command>`
3. Configure: copy `.env.example` → `.env`
4. Run: `<run command>`
5. Test: `<test command>`

## Tag Index
| Tag | Description | Rule |
|-----|-------------|------|
| `#arch-*` | Architecture concepts | Top-level pattern tags |
| `#module-*` | Module-specific | One per module |

## Onboarding Path
> Recommended reading order for new developers:

1. [[System Architecture]] — big picture
2. [[Request Flow]] — how a request moves through the system
3. [[Module A]] → [[Module B]] → ... — module deep dives
4. [[Exercises]] — hands-on practice
```

## Quick Reference Template

```markdown
---
module: dashboard
path: 00-Dashboard
keywords: quick-reference, commands, setup
---

# Quick Reference

#dashboard #quick-reference

## Key Commands
| Action | Command |
|--------|---------|
| Install deps | `<command>` |
| Run dev | `<command>` |
| Run tests | `<command>` |
| Build | `<command>` |
| Lint | `<command>` |

## Environment Setup
1. ...

## Important File Locations
| File / Dir | Purpose |
|------------|---------|
| `<path>` | <description> |

## Common Debugging
| Symptom | Where to Look | → Note |
|---------|---------------|--------|
| <problem> | `<file/log>` | [[Module Note]] |
```

## Module Note Template

```markdown
---
module: <module-name>
path: <relative-path-from-project-root>
keywords: <3-5 English keywords>
---

# <Module Name> (<Importance: ★~★★★>)

#module-<name> #<pattern-tag>

## Purpose
<1-3 sentences: what this module does and why it exists>

## Key Files
| File | Role |
|------|------|
| `<relative-path>` | <description> |

## Public Interface
| Export | Type | Description |
|--------|------|-------------|
| `<name>` | function/class/endpoint | <what it does> |

## Internal Flow

```text
<ASCII diagram showing data/control flow within this module>
```

## Dependencies
| Direction | Module / Service | Via |
|-----------|-----------------|-----|
| **Uses** | <dependency> | `<import/call>` |
| **Used by** | <dependent> | `<import/call>` |

## Configuration
| Env Var / Config Key | Purpose | Default |
|---------------------|---------|---------|
| `<VAR>` | <description> | `<default>` |

## Testing
- Run: `<test command for this module>`
- Pattern: <unit/integration/e2e>
- Coverage notes: ...

## Related Notes
- [[Other Module]]
- [[Architecture Note]]
```

## API Note Template

```markdown
---
module: <module-name>
path: <relative-path>
keywords: API, <endpoint-keywords>
---

# <Endpoint Group> API

#api-<group> #module-<name>

## Endpoints
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/path` | required | <description> |

## Request / Response

### <Endpoint Name>

**Request**:
```json
{
  "field": "type — description"
}
```

**Response (success)**:
```json
{
  "field": "type — description"
}
```

**Error cases**:
| Status | Condition | Response |
|--------|-----------|----------|
| 400 | <condition> | `{ "error": "..." }` |

## Related Notes
- [[Module Note]]
- [[Other API Note]]
```

## Onboarding Exercise Template

```markdown
---
module: exercises
path: <NN+1>-Exercises
keywords: practice, onboarding, <topic>
---

# <Topic> — Onboarding Exercises

#practice #onboarding #module-<name>

## Related Modules
- [[Module Note 1]]
- [[Module Note 2]]

---

## Exercise 1 — Code Reading [trace]
> Trace what happens when <specific trigger>. List the files and functions involved in order.

> [!answer]- View Answer
> 1. `<file>` → `<function>` — <what happens>
> 2. `<file>` → `<function>` — <what happens>
> 3. ...

---

## Exercise 2 — Configuration [config]
> How would you change <specific setting>? Which files need modification?

> [!answer]- View Answer
> - File: `<path>`
> - Change: <description>
> - Related env var: `<VAR>`

---

## Exercise 3 — Debugging [debug]
> If <symptom> occurs, where would you look first? Describe your investigation steps.

> [!answer]- View Answer
> 1. Check `<file/log>` for ...
> 2. Verify `<config>` is ...
> 3. Common cause: ...

---

## Exercise 4 — Extension [extend]
> How would you add <new feature/endpoint>? Describe the files you'd create or modify.

> [!answer]- View Answer
> 1. Create `<path>` — <purpose>
> 2. Modify `<path>` — <what to add>
> 3. Add test in `<path>` — <what to test>
> 4. Register in `<path>` — <wiring>

---

> [!summary]- 학습 포인트 요약
> | Topic | Key Takeaway |
> |-------|-------------|
> | <topic> | <insight> |
```

## Formatting Rules

- `[[wiki-links]]` for all cross-references
- `> [!tip]`, `> [!important]`, `> [!warning]` callouts for key information
- ASCII diagrams for flows, architecture, and module interactions
- Tables over prose for structured information
- **Bold** for critical terms and file paths in descriptions
- Code blocks with language hints for commands and snippets
- **Localization**: Fold callout labels (e.g., `View Answer`) should match team language. Korean: `정답 보기`, English: `View Answer`
```

## File: `skills/tutor-setup/references/codebase-workflow.md`
```markdown
# Codebase Mode — Onboarding Vault Workflow

> Generates a StudyVault that helps new developers understand and navigate a source code project.
> All scanning and output MUST stay within CWD.

## Phase C1: Project Exploration

1. **Scan project structure**: `Glob` for source files, config files, test files. Build a file tree.
2. **Identify tech stack**: Detect languages, frameworks, build tools, package managers from config files.
3. **Read key files**: README, CONTRIBUTING, entry points (`main.*`, `index.*`, `app.*`), config files.
4. **Map project layout**: Record directory purposes (e.g., `src/`, `test/`, `config/`, `scripts/`).
5. **Present findings** to user for confirmation before proceeding.

## Phase C2: Architecture Analysis

1. **Identify architectural patterns**: layered, hexagonal, microservice, monolith, serverless, etc.
2. **Map module boundaries**: Which directories/packages form distinct modules or domains?
3. **Trace request flow**: For a typical request (HTTP, event, CLI), trace the path through the code.
4. **Identify key abstractions**: Interfaces, base classes, shared utilities, middleware, interceptors.
5. **Map dependencies**: Internal module dependencies + external service integrations.
6. **Document data flow**: How data enters, transforms, persists, and exits the system.
7. **Build architecture summary**: Create a concise diagram (ASCII) + description for the vault.

## Phase C3: Tag Standard

Define tag vocabulary before creating notes:
- **Format**: English, lowercase, kebab-case
- **Categories**: `#arch-*` (architecture), `#module-*` (modules), `#pattern-*` (patterns), `#config-*` (config), `#api-*` (API), `#test-*` (testing)
- **Registry**: Only registered tags allowed. Present registry to user for approval.

## Phase C4: Vault Structure

Create `StudyVault/` per [codebase-templates.md](codebase-templates.md) folder structure:
- `00-Dashboard/` — MOC, Quick Reference, Getting Started
- `01-Architecture/` — System overview, request flow, data flow
- `02-XX/` through `NN-XX/` — One folder per module/domain
- `NN+1-DevOps/` — Build, deploy, CI/CD, environment config
- `NN+2-Exercises/` — Onboarding exercises

## Phase C5: Dashboard Creation

Create `00-Dashboard/` with:

### MOC (Map of Content)
- **Architecture Overview**: Link to architecture notes
- **Module Map**: Table of all modules with purpose + links
- **API Surface**: Summary of endpoints/commands/events
- **Getting Started**: Setup instructions, dev workflow, key commands
- **Tag Index**: Tag registry with hierarchy rules
- **Onboarding Path**: Recommended reading order for new developers

### Quick Reference
- Key commands (build, test, deploy, lint)
- Environment setup steps
- Common debugging tips
- Important file locations

## Phase C6: Module Notes

One note per module/domain. Per [codebase-templates.md](codebase-templates.md). Key rules:

- YAML frontmatter: `module`, `path`, `keywords` (MANDATORY)
- **Purpose**: What this module does (1-3 sentences)
- **Key Files**: Table of important files with descriptions
- **Public Interface**: Exported functions/classes/endpoints
- **Internal Flow**: How data moves through this module (ASCII diagram)
- **Dependencies**: What this module depends on + what depends on it
- **Configuration**: Relevant env vars, config keys
- **Testing**: How to run tests for this module, test patterns used
- **Related Notes**: Links to related modules and architecture notes

For API-heavy modules, create separate API notes per [codebase-templates.md](codebase-templates.md).

## Phase C7: Onboarding Exercises

Create exercises that guide new developers through the codebase. Per [codebase-templates.md](codebase-templates.md).

- **Code Reading**: "Trace what happens when X occurs" — answer in fold callout
- **Configuration**: "How would you change Y?" — answer with file paths + snippets
- **Debugging**: "Where would you look if Z breaks?" — answer with investigation steps
- **Extension**: "How would you add feature W?" — answer with architectural approach
- Minimum 5 exercises per major module
- All answers use `> [!answer]- <label>` fold callout (localize label to team language, e.g., "정답 보기" for Korean, "View Answer" for English)

## Phase C8: Interlinking

1. `## Related Notes` on every module note
2. MOC links to every module note + exercise file
3. Cross-link modules that depend on each other
4. Architecture notes reference specific module implementations
5. Exercises reference the modules they cover
6. Quick Reference links to relevant module notes

## Phase C9: Self-Review (MANDATORY)

Verify against [quality-checklist.md](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/development/jupyter-notebook/references/quality-checklist.md) **Codebase Mode** section. Fix and re-verify until all checks pass.
```

## File: `skills/tutor-setup/references/quality-checklist.md`
```markdown
# Quality Checklist — Self-Review

Before reporting completion, verify every item in the relevant mode's section. Fix and re-verify if any check fails.

---

## Document Mode

### Source Traceability
- [ ] Every source file's content verified (not filename-based assumption)
- [ ] Source content mapping table built and verified in Phase D1
- [ ] Every `source_pdf` frontmatter matches verified mapping
- [ ] Non-academic files excluded and documented
- [ ] Missing sources marked as `원문 미보유`
- [ ] Non-core topic policy documented in MOC

### Coverage
- [ ] Every topic from Phase D2 checklist has a concept note
- [ ] Every enumerated category member has its own note
- [ ] No source topic missing or underrepresented

### Tags
- [ ] All tags: English kebab-case, from registry only
- [ ] Tag Index includes hierarchy rules
- [ ] Detail tags co-attached with parent domain tags

### Structure & Formatting
- [ ] Every note has YAML frontmatter: `source_pdf`, `part`, `keywords`
- [ ] Every concept note has comparison table + exam/test patterns section
- [ ] Process/flow topics have ASCII diagrams
- [ ] Notes are concise (tables > prose)
- [ ] Simplified statements include exception caveats

### Dashboard
- [ ] MOC: Topic Map + Practice Notes + Study Tools + Tag Index + Weak Areas + Non-core Policy
- [ ] MOC links to every concept note AND practice note
- [ ] Weak Areas link to `→ [[note]]` AND `→ [[Exam Traps]]`
- [ ] Exam Traps exists with per-topic fold callouts and bidirectional links

### Quick Reference
- [ ] All key formulas and condition expressions included
- [ ] Every section links to concept note via `→ [[Note]]`

### Practice — Active Recall
- [ ] Every topic folder has practice file (8+ questions)
- [ ] All answers use `> [!answer]- 정답 보기` fold — never immediately visible
- [ ] Key Patterns: `> [!hint]-` fold; Pattern Summary: `> [!summary]-` fold
- [ ] `## Related Concepts` with backlinks in every practice file
- [ ] Question type diversity: ≥60% recall, ≥20% application, ≥2 analysis per file

### Interlinking
- [ ] Every concept note has `## Related Notes`
- [ ] `[[wiki-links]]` for all cross-references
- [ ] Siblings reference each other; concept ↔ practice cross-linked
- [ ] Exam Traps ↔ Concept notes bidirectionally linked

### CWD Boundary
- [ ] No source files accessed outside CWD
- [ ] No absolute file paths in notes or frontmatter
- [ ] External URLs accessed only via WebFetch, not file paths

---

## Codebase Mode

### Project Coverage
- [ ] All major modules/domains identified and documented
- [ ] Architecture pattern documented with ASCII diagram
- [ ] Request flow traced end-to-end
- [ ] Data flow documented (input → processing → persistence → output)
- [ ] External dependencies and integrations listed

### Module Completeness
- [ ] Every module has a dedicated note with YAML frontmatter (`module`, `path`, `keywords`)
- [ ] Every module note includes: Purpose, Key Files, Public Interface, Internal Flow, Dependencies
- [ ] Configuration section lists relevant env vars / config keys
- [ ] Testing section includes commands and patterns

### Tags
- [ ] All tags: English kebab-case, from registry only
- [ ] Tag Index in MOC with hierarchy rules
- [ ] Tags cover: `#arch-*`, `#module-*`, `#pattern-*`, `#api-*`

### Dashboard
- [ ] MOC: Architecture Overview + Module Map + API Surface + Getting Started + Tag Index + Onboarding Path
- [ ] MOC links to every module note and exercise file
- [ ] Quick Reference: key commands, env setup, file locations, debugging tips
- [ ] Getting Started section is actionable (copy-paste commands)

### Onboarding Exercises
- [ ] Minimum 5 exercises per major module
- [ ] Exercise types: code reading (trace), configuration, debugging, extension
- [ ] All answers use `> [!answer]- 정답 보기` fold callout
- [ ] Exercises reference relevant module notes via `[[wiki-links]]`

### Interlinking
- [ ] Every module note has `## Related Notes`
- [ ] `[[wiki-links]]` for all cross-references
- [ ] Dependent modules cross-linked bidirectionally
- [ ] Architecture notes reference specific module implementations
- [ ] Exercises link back to the modules they cover

### CWD Boundary
- [ ] No references to files outside the project directory
- [ ] All file paths in notes are relative to project root
- [ ] No hardcoded absolute paths
```

## File: `skills/tutor-setup/references/templates.md`
```markdown
# Templates Reference

## Vault Folder Structure

```
StudyVault/
  00-Dashboard/          # MOC + cheat sheets + Exam Traps
  01-<Topic1>/           # Concept notes per domain
  02-<Topic2>/
  ...
  NN-문제풀이/ (or Practice/)
```

## Dashboard MOC Template

```markdown
---
source_pdf: <list all source files>
part: <part numbers or "all">
keywords: MOC, study map, <subject>
---

# <Subject> Study Map

#dashboard #<subject-tag>

## Overview
- Exam/certification info (if applicable)
- Domain weights or topic importance

## Topic Map
| Section | Source | Notes | Status |
|---------|--------|-------|--------|
| Topic 1 | Part 1 | [[Note 1]], [[Note 2]] | [ ] |

## Practice Notes
| 문제셋 | 문항 수 | 링크 |
|--------|---------|------|
| Topic 1 | N문제 | [[Topic 1 Practice]] |

## Study Tools
| 도구 | 설명 | 링크 |
|------|------|------|
| Exam Traps | 시험 함정/오답 포인트 모음 | [[Exam Traps]] |
| Quick Reference | 전체 치트시트 | [[빠른 참조]] |

## Tag Index
| Tag | 관련 주제 | 규칙 |
|-----|-----------|------|
| `#tag-name` | Brief description | 상위/도메인/세부/기법/유형 |

> **태그 규칙**: <1-line summary of hierarchy rule>

## Weak Areas
- [ ] Area needing review → [[Relevant Note]] → [[Exam Traps]]

## Non-core Topic Policy
| Source | Content | Handling |
|--------|---------|----------|
| <file> | <description> | **Excluded** — reason |
```

## Quick Reference Template

- **Every section heading MUST include `→ [[Concept Note]]` link**
- One-line summary table per concept/term
- Grouped by category
- All key formulas and condition expressions
- "Must-know formulas/patterns" section at bottom with `→ [[Note]]` links

## Exam Traps Template

```markdown
---
keywords: exam traps, weak areas, common mistakes
---

# Exam Traps (시험 함정 포인트)

#dashboard #exam-traps

> [!warning] 이 노트의 목적
> 시험에서 자주 틀리거나 헷갈리는 포인트만 모은 **오답/함정 노트**입니다.

## <Topic 1>

> [!danger]- Trap: <Short description>
> - <What the trap is>
> - <Why it's confusing>
> - <The correct answer/approach>
> - [[Related Concept Note]]

---

## Related
- [[MOC - <Subject>]] → Weak Areas 섹션
- [[빠른 참조]]
```

## Concept Note Template

```markdown
---
source_pdf: <filename.pdf — MUST match verified Phase 1 mapping>
part: <part number>
keywords: <3-5 English keywords>
---

# <Title> (<Importance: ★~★★★>)

#<tag-from-registry> #<tag-from-registry>

## Overview Table (한눈에 비교)
| Item | Key Point |
|------|-----------|
| A    | ...       |

## <Concept 1>
Concise explanation (3-5 lines max).
- Bullet points for key facts
- Use **bold** for critical terms

---

## Exam/Test Patterns (시험 빈출 패턴)
| Scenario/Keyword | Answer |
|-------------------|--------|
| "keyword X" | **Solution Y** |

## Related Notes
- [[Other Note 1]]
```

### Formatting Rules

- `[[wiki-links]]` for cross-references
- `> [!tip]`, `> [!important]`, `> [!warning]` callouts
- Comparison tables over prose; bold for key vocabulary

### Visualization Rule

Include ASCII diagrams when applicable:
- Processes/stages → timeline or sequence diagram
- Signal/data flow → flow DAG
- Strategy comparisons → quantitative table
- State-based behavior → state transition diagram

### Simplification-with-Exceptions Rule

General statements must check for edge cases — add `> [!warning]` or link to exception details.

## Practice Question Template

```markdown
---
source_pdf: <filename.pdf — MUST match verified Phase 1 mapping>
part: <part number>
keywords: practice, <topic keywords>
---

# <Topic> Practice (N questions)

#practice #<topic-tag>

## Related Concepts
- [[Concept Note 1]]

> [!hint]- 핵심 패턴 (클릭하여 보기)
> | Keyword | Answer |
> |---------|--------|
> | pattern 1 | **Solution** |

---

## Question 1 - <Short Label> [recall]
> Scenario summary in one line

> [!answer]- 정답 보기
> Answer text here with explanation.

---

## Question 2 - <Short Label> [application]
> Given this scenario, what would you do?

> [!answer]- 정답 보기
> Answer with applied reasoning.

---

## Question 3 - <Short Label> [analysis]
> Compare X and Y in this context. Which is better and why?

> [!answer]- 정답 보기
> Comparative analysis answer.

---

> [!summary]- 패턴 요약 (클릭하여 보기)
> | Keyword | Answer |
> |---------|--------|
> | ... | ... |
```

### Practice Question Rules

- Every topic folder MUST have a practice file (8+ questions)
- **Answer hiding**: ALL answers use `> [!answer]- 정답 보기` fold callout
- **Patterns**: `> [!hint]-` / `> [!summary]-` fold callouts (MANDATORY)
- **Question type diversity**: tag `[recall]`, `[application]`, `[analysis]` in heading
  - ≥60% recall, ≥20% application, ≥2 analysis per file
- Scenario in one `>` blockquote line; answer 1-3 lines in fold
- `## Related Concepts` with `[[wiki-links]]` (MANDATORY)
```

