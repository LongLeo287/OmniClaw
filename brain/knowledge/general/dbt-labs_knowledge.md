---
id: dbt-labs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.749715
---

# KNOWLEDGE EXTRACT: dbt-labs
> **Extracted on:** 2026-03-30 17:35:45
> **Source:** dbt-labs

---

## File: `dbt-agent-skills.md`
```markdown
# 📦 dbt-labs/dbt-agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/dbt-labs/dbt-agent-skills


## Meta
- **Stars:** ⭐ 324 | **Forks:** 🍴 14
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A curated collection of Agent Skills for working with dbt, to help AI agents understand and execute dbt workflows more effectively.

## README (trích đầu)
```
# dbt Agent Skills

A curated collection of [Agent Skills](https://agentskills.io/home) for working with dbt. These skills help AI agents understand and execute dbt workflows more effectively.

## What are Agent Skills?

Agent Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently.

## How They Work

These skills are **not** slash commands or user-invoked actions. Once installed, the agent automatically loads the relevant skill when your prompt matches its use case. Just describe what you need in natural language and the agent handles the rest. See [skill invocation control](https://code.claude.com/brain/knowledge/docs_legacy/en/skills#control-who-invokes-a-skill) for more details.

## What's Included

- **Analytics engineering**: Build and modify dbt models, write tests, explore data sources
- **Semantic layer**: Create metrics, dimensions, and semantic models with MetricFlow
- **dbt Mesh**: Work with multi-project setups, cross-project refs, model governance (contracts, versions, access)
- **Platform operations**: Troubleshoot job failures, configure the dbt MCP server
- **Migration**: Move projects from dbt Core to the Fusion engine

## Installation

### Claude Code

Add the dbt skills marketplace and install the plugins:

```bash
# Add the marketplace
/plugin marketplace add dbt-labs/dbt-agent-skills

# Install the dbt skills (analytics engineering, semantic layer, testing, etc.)
/plugin install dbt@dbt-agent-marketplace

# Install the migration skills (typically a one-off — not needed for every session)
/plugin install dbt-migration@dbt-agent-marketplace
```

### Other AI Clients

#### Vercel Skills CLI

Use the [Vercel Skills CLI](https://github.com/vercel-labs/skills) to install skills from this repository. Supports 30+ AI agents including Cursor, Cline, GitHub Copilot, and others.

```bash
# Preview available skills
npx skills add dbt-labs/dbt-agent-skills --list

# Install all skills
npx skills add dbt-labs/dbt-agent-skills

# Install only the dbt skills (analytics engineering, semantic layer, etc.)
npx skills add dbt-labs/dbt-agent-skills/skills/dbt

# Install only the migration skills
npx skills add dbt-labs/dbt-agent-skills/skills/dbt-migration

# Install a specific skill
npx skills add dbt-labs/dbt-agent-skills --skill using-dbt-for-analytics-engineering

# Install globally (available in all projects, stored in ~/.<agent>/skills/)
npx skills add dbt-labs/dbt-agent-skills --global

# Check for updates
npx skills check

# Update installed skills
npx skills update
```

#### Tessl

Install skills using [Tessl](https://tessl.io/), a package manager for agent skills:

```bash
# Install all skills
tessl install dbt-labs/dbt-agent-skills

# Install a specific skill
tessl install dbt-labs/dbt-agent-skills --skill using-dbt-for-analytics-engineering

# Install from GitHub directly
tessl install github:dbt-labs/dbt-agent-skills
```

Browse the tile on the [Tessl registry](https://tessl.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

