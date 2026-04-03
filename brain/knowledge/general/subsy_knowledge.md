---
id: subsy-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.014959
---

# KNOWLEDGE EXTRACT: subsy
> **Extracted on:** 2026-03-30 17:54:09
> **Source:** subsy

---

## File: `ralph-tui.md`
```markdown
# 📦 subsy/ralph-tui [🔖 PENDING/APPROVE]
🔗 https://github.com/subsy/ralph-tui
🌐 https://ralph-tui.com

## Meta
- **Stars:** ⭐ 2171 | **Forks:** 🍴 208
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Ralph TUI

[![npm version](https://img.shields.io/npm/v/ralph-tui.svg)](https://www.npmjs.com/package/ralph-tui)
[![CI](https://github.com/subsy/ralph-tui/actions/workflows/ci.yml/badge.svg)](https://github.com/subsy/ralph-tui/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/subsy/ralph-tui/graph/badge.svg)](https://codecov.io/gh/subsy/ralph-tui)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Built with Bun](https://img.shields.io/badge/Built%20with-Bun-f9f1e1.svg)](https://bun.sh)

**AI Agent Loop Orchestrator** - A terminal UI for orchestrating AI coding agents to work through task lists autonomously.

Ralph TUI connects your AI coding assistant (Claude Code, OpenCode, Factory Droid, Gemini CLI, Codex, Kiro CLI) to your task tracker and runs them in an autonomous loop, completing tasks one-by-one with intelligent selection, error handling, and full visibility.

![Ralph TUI Screenshot](docs/images/ralph-tui.png)

## Quick Start

```bash
# Install
bun install -g ralph-tui

# Setup your project
cd your-project
ralph-tui setup

# Create a PRD with AI assistance
ralph-tui create-prd --chat

# Run Ralph!
ralph-tui run --prd ./prd.json
```

That's it! Ralph will work through your tasks autonomously.

## Documentation

**[ralph-tui.com](https://ralph-tui.com)** - Full documentation, guides, and examples.

### Quick Links

- **[Quick Start Guide](https://ralph-tui.com/docs/getting-started/quick-start)** - Get running in 2 minutes
- **[Installation](https://ralph-tui.com/docs/getting-started/installation)** - All installation options
- **[CLI Reference](https://ralph-tui.com/docs/cli/overview)** - Complete command reference
- **[Configuration](https://ralph-tui.com/docs/configuration/overview)** - Customize Ralph for your workflow
- **[Troubleshooting](https://ralph-tui.com/docs/troubleshooting/common-issues)** - Common issues and solutions

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐   │
│   │  1. SELECT   │────▶│  2. BUILD    │────▶│  3. EXECUTE  │   │
│   │    TASK      │     │    PROMPT    │     │    AGENT     │   │
│   └──────────────┘     └──────────────┘     └──────────────┘   │
│          ▲                                         │            │
│          │                                         ▼            │
│   ┌──────────────┐                         ┌──────────────┐    │
│   │  5. NEXT     │◀────────────────────────│  4. DETECT   │    │
│   │    TASK      │                         │  COMPLETION  │    │
│   └──────────────┘                         └──────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Ralph selects the highest-priority task, builds a prompt, executes your AI agent, detects
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

