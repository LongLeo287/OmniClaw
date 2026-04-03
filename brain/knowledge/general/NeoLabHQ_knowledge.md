---
id: neolabhq-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.297994
---

# KNOWLEDGE EXTRACT: NeoLabHQ
> **Extracted on:** 2026-03-30 17:49:10
> **Source:** NeoLabHQ

---

## File: `context-engineering-kit.md`
```markdown
# 📦 NeoLabHQ/context-engineering-kit [🔖 PENDING/APPROVE]
🔗 https://github.com/NeoLabHQ/context-engineering-kit
🌐 https://cek.neolab.finance/

## Meta
- **Stars:** ⭐ 715 | **Forks:** 🍴 59
- **Language:** TypeScript | **License:** GPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemini CLI, and others.

## README (trích đầu)
```
<p align="center">
  <a href="https://cek.neolab.finance/" target="blank"><img src="docs/assets/Context-Engineering-Kit6.png" width="512" alt="Context Engineering Kit - advanced context engineering techniques" /></a>
</p>

<div align="center">

[![License](https://img.shields.io/badge/license-GPL%203.0-blue.svg)](LICENSE)
[![agentskills.io](https://img.shields.io/badge/format-agentskills.io-purple.svg)](https://agentskills.io)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

Advanced context engineering techniques and patterns for Claude Code, OpenCode, Cursor, Antigravity and more.

[Quick Start](#quick-start) · [Plugins](#plugins-list) · [Github Action](https://cek.neolab.finance/guides/ci-integration) · [Reference](https://cek.neolab.finance/reference) · [Docs](https://cek.neolab.finance/)

</div>

# [Context Engineering Kit](https://cek.neolab.finance)

Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint, focused on improving agent result quality and predictability.

The marketplace is based on prompts used daily by our company developers for a long time, supplemented by plugins from benchmarked papers and high-quality projects.

> [!IMPORTANT]
> **v2 marketplace release:** [Spec-Driven Development plugin](https://cek.neolab.finance/plugins/sdd) was rewritten from scratch. It is now able to produce working code in 100% of cases on real-life production projects!

## Key Features

- **Simple to Use** - Easy to install and use without any dependencies. Contains automatically used skills and self-explanatory commands.
- **Token-Efficient** - Carefully crafted prompts and architecture, preferring command-oriented skills with sub-agents over general information skills when possible, to minimize populating context with unnecessary information.
- **Quality-Focused** - Each plugin is focused on meaningfully improving agent results in a specific area.
- **Granular** - Install only the plugins you need. Each plugin loads only its specific agents, commands, and skills. Each without overlap and redundant skills.
- **Scientifically proven** - Plugins are based on proven techniques and patterns that were tested by well-trusted benchmarks and studies.
- **Open-Standards** - Skills are based on [agentskills.io](https://agentskills.io) specification. The [SDD](https://cek.neolab.finance/plugins/sdd) plugin is based on the **Arc42** specification standard for software development documentation.

## Quick Start

### Step 1: Install Marketplace and Plugins

#### Claude Code

Open Claude Code and add the Context Engineering Kit marketplace

```bash
/plugin marketplace add NeoLabHQ/context-engineering-kit
```

This makes all plugins available for installation, but does not load any agents or skills into your context.

Install any plugin, for example reflexion:

```bash
/plugin install reflexion@NeoLabHQ/context-engineering-kit

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

