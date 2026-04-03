---
id: phuryn-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:21.171789
---

# KNOWLEDGE EXTRACT: phuryn
> **Extracted on:** 2026-03-30 17:51:01
> **Source:** phuryn

---

## File: `awesome-agent-skills.md`
```markdown
# 📦 phuryn/awesome-agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/phuryn/awesome-agent-skills
🌐 https://github.com/VoltAgent/voltagent

## Meta
- **Stars:** ⭐ 8 | **Forks:** 🍴 1
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-19
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code Skills and 500+ agent skills from official dev teams and the community, compatible with Codex, Antigravity, Gemini CLI, Cursor and others.

## README (trích đầu)
```
<a href="https://github.com/VoltAgent/voltagent">
     <img width="1500" height="801" alt="claude-skills" src="https://github.com/user-attachments/assets/3a9d4cb3-04bd-4fb1-9146-fd3b53d26961" />
</a>


<br/>
<br/>

<div align="center">
    <strong>A curated collection of official Agent Skills from leading development teams and the community.
    </strong>
    <br />
    <br />

</div>

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="https://github.com/VoltAgent/voltagent">
  <img alt="VoltAgent" src="https://cdn.voltagent.dev/website/logo/logo-2-svg.svg" height="20" />
</a>

[![AI Agent Papers](https://img.shields.io/badge/AI%20Agent-Research%20Papers-b31b1b)](https://github.com/VoltAgent/awesome-ai-agent-papers)
![Skills Count](https://img.shields.io/badge/Skills-549+-blue?style=flat-square)
![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-agent-skills?label=Last%20update&style=flat-square)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![GitHub forks](https://img.shields.io/github/forks/VoltAgent/awesome-agent-skills?style=social)](https://github.com/VoltAgent/awesome-agent-skills/network/members)

</div>

# Awesome Agent Skills

Unlike many bulk-generated skill repositories, this collection focuses on real-world Agent Skills created and used by actual engineering teams, not mass AI‑generated stuff.

This collection features official skills published by leading development teams, including Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, and more, alongside community-built skills.

Compatible with Claude Code, Codex, Antigravity, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Windsurf, and more. See the table below for paths and documentation.

The most contributed Agent Skills repository, built and maintained together with the community.


## 🔒 Security Notice

Skills in this list are curated, not audited. They may be updated, modified, or replaced by their original maintainers at any time after being added here.

Before installing or using any Agent Skill, review potential security risks and validate the source yourself.

Recommended tools:

- [Synk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)

Agent skills can include prompt injections, tool poisoning, hidden malware payloads, or unsafe data handling patterns. Always review the code and use skills at your own discretion.

## Table of Contents

| | | |
|---|---|---|
| [Official Claude Skills](#official-claude-skills) | [Skills by VoltAgent](#skills-by-voltagent) | [Skills by Composio](#skills-by-composio-team) |
| [Skills by Supabase](#skills-by-supabase-team) | [Skills by Google Gemini](#skills-by-google-gemini) | [Skills by Stripe](#skills-by-stripe-team) |
| [Skills b
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pm-skills.md`
```markdown
# 📦 phuryn/pm-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/phuryn/pm-skills
🌐 https://www.productcompass.pm/p/pm-skills-marketplace-claude

## Meta
- **Stars:** ⭐ 8217 | **Forks:** 🍴 846
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.

## README (trích đầu)
```
![GitHub stars](https://img.shields.io/github/stars/phuryn/pm-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/CONTRIBUTING.md)

# PM Skills Marketplace: The AI Operating System for Better Product Decisions

> 65 PM skills and 36 chained workflows across 8 plugins. Claude Code, Cowork, and more. From discovery to strategy, execution, launch, and growth. 

![Plugin overview](.docs/images/plugins-overview.webp)

Designed for Claude Code and Cowork. Skills compatible with other AI assistants.

## Start Here

New idea? → `/discover`  
Need strategic clarity? → `/strategy`  
Writing a PRD? → `/write-prd`  
Planning a launch? → `/plan-launch`  
Defining metrics? → `/north-star`

If this project helps you, ⭐ the repo.

## Why PM Skills Marketplace?

Generic AI gives you text. PM Skills Marketplace gives you structure.

Each skill encodes a proven PM framework — discovery, assumption mapping, prioritization, strategy — and walks you through it step by step. You get the rigor of Teresa Torres, Marty Cagan, and Alberto Savoia built into your daily workflow, not sitting on a bookshelf.

The result: better product decisions, not just faster documents.

## How It Works (Skills, Commands, Plugins)

**Skills** are the building blocks of the marketplace. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific PM task. Some skills also work as reusable foundations that multiple commands share. 

Skills are loaded automatically when relevant to the conversation — no explicit invocation needed. If needed (e.g., prioritizing skills over general knowledge), you can **force loading skills** with `/plugin-name:skill-name` or `/skill-name` (Claude will add the prefix).

**Commands** are user-triggered workflows invoked with `/command-name`. They chain one or more skills into an end-to-end process. For example, `/discover` chains four skills together: brainstorm-ideas → identify-assumptions → prioritize-assumptions → brainstorm-experiments.

**Plugins** group related skills and commands into installable packages. Each plugin covers a PM domain — discovery, strategy, execution, and so on. Installing the marketplace gives you all 8 plugins at once.

![How skills work](.docs/images/how-skills-work.webp)

Commands use skills. Some skills serve multiple commands. Some skills (like `prioritization-frameworks` or `opportunity-solution-tree`) are standalone references that Claude draws on whenever relevant — no command needed.

Commands are designed to flow into each other, matching the PM workflow. After any command completes, it suggests relevant next commands — just follow the prompts.

## Installation

### Claude Cowork (recommended for non-developers)

1. Open **Customize** (bottom-left)
2. Go to **B
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

