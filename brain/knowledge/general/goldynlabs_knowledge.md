---
id: goldynlabs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.792963
---

# KNOWLEDGE EXTRACT: goldynlabs
> **Extracted on:** 2026-03-30 17:38:00
> **Source:** goldynlabs

---

## File: `prr-kit.md`
```markdown
# 📦 goldynlabs/prr-kit [🔖 PENDING/APPROVE]
🔗 https://github.com/goldynlabs/prr-kit
🌐 https://prrkit.sitenow.cloud

## Meta
- **Stars:** ⭐ 23 | **Forks:** 🍴 2
- **Language:** Astro | **License:** MIT
- **Last updated:** 2026-03-13
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AI-driven Pull Request Review Framework — structured agent workflows for thorough, consistent code review

## README (trích đầu)
```
# PR Review Kit

<p align="center">
  <img src="docs/assets/banner.svg" alt="PR Review Kit" width="100%"/>
</p>

[![Version](https://img.shields.io/npm/v/prr-kit?color=blue&label=version)](https://www.npmjs.com/package/prr-kit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Website](https://img.shields.io/npm/dm/prr-kit?color=orange&label=downloads)](https://prrkit.sitenow.cloud)
[![Docs](https://img.shields.io/badge/docs-prrkit.sitenow.cloud-blue)](https://prrkit.sitenow.cloud/docs)

> AI-driven Pull Request code review — structured, multi-perspective, actionable.

Module system, agent YAML, step-file workflows, CLI installer with full IDE integration.

**[🌐 Website](https://prrkit.sitenow.cloud)** **[📖 Full Documentation](https://prrkit.sitenow.cloud/docs)**

<a href="https://unikorn.vn/p/prr-kit?ref=embed" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/prr-kit?theme=light" alt="PR Review Kit trên Unikorn.vn" style="width: 256px; height: 64px;" width="256" height="64" /></a>
<a href="https://unikorn.vn/p/prr-kit?ref=embed" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/prr-kit/rank?theme=light&type=daily" alt="PR Review Kit - Hàng ngày" style="width: 250px; height: 64px;" width="250" height="64" /></a>


## Quick Start

```bash
# Install into your repo (interactive — recommended)
npx prr-kit install

# Or use the alias
npx pr-review install

# Silent install with all defaults
npx prr-kit install --directory /path/to/repo --modules prr --tools claude-code --yes
```

Then open your IDE in the installed project and use one of these commands to start:

- `/prr-quick` — one command, full pipeline (select PR → review → report)
- `/prr-master` — full menu with all options

> **Note:** The exact command depends on your IDE. See [IDE Support](https://prrkit.sitenow.cloud/docs/ide-support) for the command specific to your IDE.

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                    /prr-quick                           │
│              Load config.yaml                           │
└───────────────────────┬─────────────────────────────────┘
                        │
        ╔═══════════════▼════════════════╗
        ║       PHASE 1 — SELECT PR      ║
        ╚═══════════════╤════════════════╝
                        │
             ┌──────────▼──────────┐
             │ 1a. git fetch origin │
             └──────────┬──────────┘
                        │
             ┌──────────▼───────────────┐
             │ 1b. List open PRs/MRs    │
             │     + recent branches    │
             └──────────┬───────────────┘
                        │
             ┌──────────▼───────────────┐
             │ 1c. ⌨️  Select PR/branch  │  ← USER INPUT
             │     Enter PR# or name    │
             └──────────┬───────────────┘
                      
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

