---
id: francyjglisboa-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.572236
---

# KNOWLEDGE EXTRACT: FrancyJGLisboa
> **Extracted on:** 2026-03-30 17:37:23
> **Source:** FrancyJGLisboa

---

## File: `agent-skill-creator.md`
```markdown
# 📦 FrancyJGLisboa/agent-skill-creator [🔖 PENDING/APPROVE]
🔗 https://github.com/FrancyJGLisboa/agent-skill-creator


## Meta
- **Stars:** ⭐ 582 | **Forks:** 🍴 91
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Turn any workflow into reusable AI agent skills that install on 14+ tools — Claude Code, Copilot, Cursor, Windsurf, Codex, Gemini, Kiro, and more. One SKILL.md, every platform.

## README (trích đầu)
```
# Agent Skill Creator

**Turn any workflow into reusable AI agent software that installs on 14+ tools — no spec writing, no prompt engineering, no coding required.**

[![Agent Skills Open Standard](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-blue)](https://github.com/anthropics/agent-skills-spec)
[![Version](https://img.shields.io/badge/version-5.0.0-brightgreen)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

![Agent Skill Creator Overview](Dynamous/agentskillimage.png)

---

## The Problem

Every AI coding tool — Claude Code, GitHub Copilot, Cursor, Windsurf, Codex, Gemini, Kiro, and more — starts from zero. It doesn't know your company's processes, data sources, or compliance requirements. So every person re-explains the same workflows in every conversation. Knowledge stays in individual chat histories. New hires start from scratch.

**Agent skills fix this.** A skill is structured knowledge your agent loads automatically — like installing an app. Once installed, anyone on your team can invoke it and get consistent results, every time, on any platform.

**The catch:** building a proper skill requires understanding the spec format, writing clear prompt instructions, designing how information loads progressively, writing functional code, and getting activation keywords right. Even simple skills take [multiple rounds of iteration](https://www.youtube.com/watch?v=izJkgLqlbN8) to get right.

**Agent Skill Creator removes that barrier entirely.** You pass in whatever you have — messy docs, links, code, PDFs, transcripts, vague descriptions — and it produces a validated, security-scanned skill ready to install on 14+ tools and share with your team. You describe what you do; it builds the software.

---

## Quick Start

### 1. Install

**Option A — One-liner (installs to all detected tools):**

```bash
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/agent-skill-creator/main/scripts/bootstrap.sh | sh
```

This clones to `~/.agents/skills/agent-skill-creator` and symlinks to every detected global platform (Claude Code, Gemini CLI, Goose, OpenCode, Copilot). Run `git pull` once to update everywhere.

**Option B — Git clone (pick your tool):**

```bash
# Claude Code / VS Code Copilot (global — works in all projects)
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git ~/.claude/skills/agent-skill-creator

# Cursor (per-project)
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git .cursor/rules/agent-skill-creator

# Codex CLI / Gemini CLI / Kiro / Antigravity (universal path)
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git ~/.agents/skills/agent-skill-creator
```

**Option C — Already cloned? Symlink to all tools:**

```bash
cd agent-skill-creator
./install.sh              # Symlink to all detected platforms
./install.sh --dry-run    # Preview without changes
./install.sh --uninstall  # Remove all symlinks
```

One install at `~/.claude/skills/` works
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

