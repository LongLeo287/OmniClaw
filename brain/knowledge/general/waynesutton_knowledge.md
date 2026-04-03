---
id: waynesutton-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.502246
---

# KNOWLEDGE EXTRACT: waynesutton
> **Extracted on:** 2026-03-30 18:01:16
> **Source:** waynesutton

---

## File: `convexskills.md`
```markdown
# 📦 waynesutton/convexskills [🔖 PENDING/APPROVE]
🔗 https://github.com/waynesutton/convexskills
🌐 https://docs.convex.dev/

## Meta
- **Stars:** ⭐ 385 | **Forks:** 🍴 29
- **Language:** JavaScript | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AI agent skills and templates for building production ready apps with Convex. Patterns for queries, mutations, cron jobs, webhooks, migrations, and more.

## README (trích đầu)
```
# For official Convex Skills use Convex Agent Plugins

Official Convex plugins for AI coding agents, providing development tools for building reactive backends with TypeScript.

https://github.com/get-convex/convex-agent-plugins


## Convex (unofficial) Skills 

[![npm version](https://img.shields.io/npm/v/@waynesutton/convex-skills.svg)](https://www.npmjs.com/package/@waynesutton/convex-skills)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

A collection of AI-consumable skills for building production-ready applications with [Convex](https://convex.dev), following the Agent Skills open format.

## Overview

This repository contains skills that help AI assistants understand and implement Convex best practices. Each skill provides structured guidance for specific aspects of Convex development.

## Code Quality

All skills are designed to produce code that passes @convex-dev/eslint-plugin by default. This creates a complementary workflow:

- **Skills** prevent mistakes at generation time
- **ESLint** catches anything that slips through at build time

See the Code Quality section in [convex-best-practices](/skills/convex-best-practices/SKILL.md) for setup instructions.

## Installation

### npm (recommended)

```bash
# Install globally for CLI access
npm install -g @waynesutton/convex-skills

# List available skills
convex-skills list

# Install a specific skill to your project
convex-skills install convex-best-practices

# Install all skills
convex-skills install-all

# Install all skills to .agents/skills
convex-skills install-all --target agents

# Symlink SKILL.md files instead of copying
convex-skills install-all --target agents --link

# Install templates (CLAUDE.md + skill templates)
convex-skills install-templates
```

Or use npx without installing:

```bash
npx @waynesutton/convex-skills list
npx @waynesutton/convex-skills install-all
```

### Programmatic Usage

```bash
npm install @waynesutton/convex-skills
```

```javascript
import { listSkills, getSkill, SKILLS } from "@waynesutton/convex-skills";

// List all skills
console.log(listSkills());

// Get a specific skill's content
const content = getSkill("convex-best-practices");
```

### Claude Code (from local clone)

```bash
git clone https://github.com/waynesutton/convexskills.git
cd convexskills
# Point Claude Code to this directory
```

### Codex

Follow the Codex skills guide and place the skill under `$CODEX_HOME/skills`:

```bash
# From the repo root
# Defaults to ~/.codex if CODEX_HOME is unset
cp -r skills/convex-best-practices "$CODEX_HOME/skills/"
```

Codex will auto-discover `SKILL.md` files in that directory on the next start.

If you are working from a repo clone, Codex also auto-discovers skills from `.codex/skills` at the repo root. You can symlink this repo’s `skills/*` into `.codex/skills` so updates flow through without copying.

### Standard Agent Skills Path

Some tools are standardizing on `.agents/skills` for discovery. This repo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

