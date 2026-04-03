---
id: hanfang-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:50.751630
---

# KNOWLEDGE EXTRACT: hanfang
> **Extracted on:** 2026-03-30 17:38:03
> **Source:** hanfang

---

## File: `claude-memory-skill.md`
```markdown
# 📦 hanfang/claude-memory-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/hanfang/claude-memory-skill


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 1
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A minimal, low-friction memory system for Claude Code

## README (trích đầu)
```
# claude-memory-skill

```
╔══●══●══●══════════════════════════════════════════════╗
║                                                       ║
║  > tree ~/.claude/memory                              ║
║                                                       ║
║    ├── core.md          claude-memory-skill           ║
║    ├── topics/          ───────────────────           ║
║    │   └── *.md         a skill is all you need       ║
║    └── me.md                                          ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

> *An embarrassingly simple and minimal implementation for agentic memory.*
>
> No databases. No embeddings. No semantic search. Just markdown files and a skill that teaches Claude when to read and write.

## The Problem

Claude Code forgets everything between sessions. Built-in auto-memory exists but:
- It's opaque (Claude decides what's "meaningful")
- Limited to 200 lines loaded at startup
- Not tightly integrated into the agentic loop
- No hierarchical organization (scales poorly)

## The Solution

A skill-based memory protocol with:
- **Hierarchical storage**: `core.md` summaries → `topics/<topic>.md` details
- **Background agents**: Memory ops don't block the main agent
- **Categorized entries**: No dumping ground, everything has a topic
- **Filesystem-based**: Robust, inspectable, git-trackable

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/hanfang/claude-memory-skill/main/install.sh | bash
```

Or clone and run locally:

```bash
git clone https://github.com/hanfang/claude-memory-skill.git
cd claude-memory-skill
./install.sh
```

## What Gets Installed

```
~/.claude/
├── CLAUDE.md              # Hook added (or created)
├── commands/
│   └── mem.md             # The memory skill
└── memory/
    ├── core.md            # Summaries + pointers (always loaded)
    ├── me.md              # About you (always loaded)
    ├── topics/            # Detailed entries by topic
    │   └── <topic>.md
    └── projects/          # Project-specific memories
        └── <project>.md
```

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  Main Agent                                         │
│  - Focuses on user's task                           │
│  - Spawns memory agent when needed                  │
│  - Doesn't wait (background)                        │
└─────────────────────┬───────────────────────────────┘
                      │ spawn (background)
                      ▼
┌─────────────────────────────────────────────────────┐
│  Memory Agent                                       │
│  - Reads core.md + relevant topics                  │
│  - Writes to topic files                            │
│  - Updates core.md summaries                        │
└─────────────────────────────────────────────────────┘
```

## How It Works

### Agent-Initiated (Automatic)

These run automatically — you don't invoke them:
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

