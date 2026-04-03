---
id: conorluddy-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:09.924208
---

# KNOWLEDGE EXTRACT: conorluddy
> **Extracted on:** 2026-03-30 17:35:37
> **Source:** conorluddy

---

## File: `ios-simulator-skill.md`
```markdown
# 📦 conorluddy/ios-simulator-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/conorluddy/ios-simulator-skill
🌐 https://deepwiki.com/conorluddy/ios-simulator-skill

## Meta
- **Stars:** ⭐ 660 | **Forks:** 🍴 37
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

## README (trích đầu)
```
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/conorluddy/ios-simulator-skill)

# iOS Simulator Skill for Claude Code

Production-ready automation for iOS app testing and building. 21 scripts optimized for both human developers and AI agents.

This is basically a Skill version of my XCode MCP: [https://github.com/conorluddy/xc-mcp](https://github.com/conorluddy/xc-mcp)


> [!WARNING]
> You want to take the `ios-simulator-skill` directory from this repo and drop it into your skills directory - not this entire repo. I'll update this soon with an easier approach. Feel free to fork this and get Claude to adjust it to your specific needs.


MCPs load a lot of tokens into the context window when they're active, but also seem to work really well. Skills don't load in any context. I'll make a plugin next and try to find the balance...

Updated: The Plugin version lets you easily disable MCPs for different tool groups. Optimise your context window by only enabling the tools you're actively using, such as xcodebuild: [https://github.com/conorluddy/xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)

## What It Does

Instead of pixel-based navigation that breaks when UI changes:

```bash
# Fragile - breaks if UI changes
idb ui tap 320 400

# Robust - finds by meaning
python scripts/navigator.py --find-text "Login" --tap
```

Uses semantic navigation on accessibility APIs to interact with elements by their meaning, not coordinates. Works across different screen sizes and survives UI redesigns.

## Features

- **21 production scripts** for building, testing, and automation
- **Semantic navigation** - find elements by text, type, or ID
- **Token optimized** - 96% reduction vs raw tools (3-5 lines default)
- **Zero configuration** - works immediately on macOS with Xcode
- **Structured output** - JSON and formatted text, easy to parse
- **Auto-UDID detection** - no need to specify device each time
- **Batch operations** - boot, delete, erase multiple simulators at once
- **Comprehensive testing** - WCAG compliance, visual diffs, accessibility audits
- **CI/CD ready** - JSON output, exit codes, automated device lifecycle

## Installation

### As Claude Code Skill

```bash
# Personal installation
git clone https://github.com/conorluddy/ios-simulator-skill.git ~/.claude/skills/ios-simulator-skill

# Project installation
git clone https://github.com/conorluddy/ios-simulator-skill.git .claude/skills/ios-simulator-skill
```

Restart Claude Code. The skill loads automatically.

### From Release

```bash
# Download latest release
curl -L https://github.com/conorluddy/ios-simulator-skill/releases/download/vX.X.X/ios-simulator-skill-vX.X.X.zip -o skill.zip

# Extract
unzip skill.zip -d ~/.claude/skills/ios-simulator-skill
```

## Prerequisites

- macOS 12+
- Xcode Command Line Tools (`xcode-select --install`)
- Python 3
- IDB (optional, for interactive features: `brew tap facebook/fb && brew install idb-companion`)

## Quick Start

```bas
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

