---
id: shpigford-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.590011
---

# KNOWLEDGE EXTRACT: Shpigford
> **Extracted on:** 2026-03-30 17:53:20
> **Source:** Shpigford

---

## File: `skills.md`
```markdown
# 📦 Shpigford/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/Shpigford/skills


## Meta
- **Stars:** ⭐ 153 | **Forks:** 🍴 9
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent skills for common tasks

## README (trích đầu)
```
# Skills

Agent Skills for AI coding assistants. These skills follow the [Agent Skills Standard](https://github.com/anthropics/agent-skills-standard) and work with Claude Code, Cursor, Gemini Code Assist, GitHub Copilot, and other compatible tools.

## Installation

```bash
npx skills add Shpigford/skills
```

Or manually:

```bash
git clone https://github.com/Shpigford/skills.git ~/.skills/shpigford
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [build](#build) | Feature development pipeline - research, plan, track, implement |
| [but-for-real](#but-for-real) | Force a skeptical second pass on your own work |
| [chat-widget](#chat-widget) | Build real-time support chat with floating widget |
| [conductor-setup](#conductor-setup) | Configure Rails projects for Conductor |
| [favicon](#favicon) | Generate favicon sets from source images |
| [feature-image](#feature-image) | Generate branded social media images for feature announcements |
| [issues](#issues) | Create, list, and view GitHub issues |
| [new-rails-project](#new-rails-project) | Create opinionated Rails 8 + React projects |
| [readme](#readme) | Generate comprehensive project documentation |
| [screenshots](#screenshots) | Generate marketing screenshots with Playwright |

---

### readme

Creates comprehensive README.md documentation for projects. Performs deep codebase exploration before writing, covering:

- Local development setup (step-by-step)
- Architecture overview with directory structure and data flow
- Environment variables reference
- Deployment instructions (auto-detects platform)
- Troubleshooting common issues

**Triggers:** "write readme", "create readme", "document this project", "project documentation"

**Example usage:**

```
Write a readme for this project
```

---

### build

Feature development pipeline for building major features. Manages a 4-phase workflow:

1. **Research** - Deep exploration of a feature idea
2. **Implementation** - Create phased implementation plan
3. **Progress** - Set up progress tracking
4. **Phase execution** - Implement each phase with tracking

**Subcommands:**

```
/build research [name]        Deep research on a feature idea
/build implementation [name]  Create phased implementation plan
/build progress [name]        Set up progress tracking
/build phase [n] [name]       Execute implementation phase n
/build status [name]          Show status and next steps
```

**Example workflow:**

```
/build research chat-interface
/build implementation chat-interface
/build progress chat-interface
/build phase 1 chat-interface
```

---

### but-for-real

Force a skeptical second pass on your own work. Runs after you've made changes to catch the things you missed — wrong logic, forgotten tests, unused imports, scope creep, and the classic "it should work" without actually running it.

**What it checks:**
- Did you actually do what was asked (and only what was asked)?
- Would you approve this if someone else wrote it?
- W
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

