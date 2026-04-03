---
id: roundtable02-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:09.976449
---

# KNOWLEDGE EXTRACT: RoundTable02
> **Extracted on:** 2026-03-30 17:53:01
> **Source:** RoundTable02

---

## File: `tutor-skills.md`
```markdown
# 📦 RoundTable02/tutor-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/RoundTable02/tutor-skills


## Meta
- **Stars:** ⭐ 540 | **Forks:** 🍴 51
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Claude Code skill that turns PDFs, docs, and codebases into Obsidian study vaults

## README (trích đầu)
```
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
- Full interlinking wit
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

