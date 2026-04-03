---
id: wordpress-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:46.555092
---

# KNOWLEDGE EXTRACT: WordPress
> **Extracted on:** 2026-03-30 18:01:18
> **Source:** WordPress

---

## File: `agent-skills.md`
```markdown
# 📦 WordPress/agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/WordPress/agent-skills


## Meta
- **Stars:** ⭐ 1005 | **Forks:** 🍴 140
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Expert-level WordPress knowledge for AI coding assistants - blocks, themes, plugins, and best practices

## README (trích đầu)
```
# Agent Skills for WordPress

**Teach AI coding assistants how to build WordPress the right way.**

Agent Skills are portable bundles of instructions, checklists, and scripts that help AI assistants (Claude, Copilot, Codex, Cursor, etc.) understand WordPress development patterns, avoid common mistakes, and follow best practices.

> **AI Authorship Disclosure:** These skills were generated using GPT-5.2 Codex (High Reasoning) from official Gutenberg and WordPress documentation, then reviewed and edited by WordPress contributors. We tested skills with AI assistants and iterated based on results. This is v1, and skills will improve as the community uses them and contributes fixes. See [docs/ai-authorship.md](docs/ai-authorship.md) for details. ([WordPress AI Guidelines](https://make.wordpress.org/ai/handbook/ai-guidelines/))

## Why Agent Skills?

AI coding assistants are powerful, but they often:
- Generate outdated WordPress patterns (pre-Gutenberg, pre-block themes)
- Miss critical security considerations in plugin development
- Skip proper block deprecations, causing "Invalid block" errors
- Ignore existing tooling in your repo

Agent Skills solve this by giving AI assistants **expert-level WordPress knowledge** in a format they can actually use.

## Available Skills

| Skill | What it teaches |
|-------|-----------------|
| **wordpress-router** | Classifies WordPress repos and routes to the right workflow |
| **wp-project-triage** | Detects project type, tooling, and versions automatically |
| **wp-block-development** | Gutenberg blocks: `block.json`, attributes, rendering, deprecations |
| **wp-block-themes** | Block themes: `theme.json`, templates, patterns, style variations |
| **wp-plugin-development** | Plugin architecture, hooks, settings API, security |
| **wp-rest-api** | REST API routes/endpoints, schema, auth, and response shaping |
| **wp-interactivity-api** | Frontend interactivity with `data-wp-*` directives and stores |
| **wp-abilities-api** | Capability-based permissions and REST API authentication |
| **wp-wpcli-and-ops** | WP-CLI commands, automation, multisite, search-replace |
| **wp-performance** | Profiling, caching, database optimization, Server-Timing |
| **wp-phpstan** | PHPStan static analysis for WordPress projects (config, baselines, WP-specific typing) |
| **wp-playground** | WordPress Playground for instant local environments |
| **wpds** | WordPress Design System |
| **blueprint** | WordPress Playground Blueprints for declarative Playground environment setup |

## Quick Start

### Install globally for Claude Code

```bash
# Clone agent-skills
git clone https://github.com/WordPress/agent-skills.git
cd agent-skills

# Build the distribution
node shared/scripts/skillpack-build.mjs --clean

# Install all skills globally (available across all projects)
node shared/scripts/skillpack-install.mjs --global

# Or install specific skills only
node shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

