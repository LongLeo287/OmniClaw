---
id: obra-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:13.617621
---

# KNOWLEDGE EXTRACT: obra
> **Extracted on:** 2026-03-30 17:49:32
> **Source:** obra

---

## File: `superpowers-lab.md`
```markdown
# 📦 obra/superpowers-lab [🔖 PENDING/APPROVE]
🔗 https://github.com/obra/superpowers-lab


## Meta
- **Stars:** ⭐ 249 | **Forks:** 🍴 17
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Experimental skills for Claude Code Superpowers - new techniques and tools

## README (trích đầu)
```
# Superpowers Lab

Experimental skills for [Claude Code Superpowers](https://github.com/obra/superpowers) - new techniques and tools under active development.

## What is this?

This plugin contains experimental skills that extend Claude Code's capabilities with new techniques that are still being refined and tested. These skills are functional but may evolve based on real-world usage and feedback.

## Current Skills

### finding-duplicate-functions

Detect semantic code duplication in LLM-generated codebases. Unlike traditional copy-paste detectors that find syntactic duplicates, this skill identifies functions with the same intent but different implementations.

**Use cases:**
- Audit codebases that have grown organically with multiple contributors
- Identify utility functions that have been reimplemented multiple times
- Find consolidation opportunities before major refactoring
- Complement jscpd after syntactic duplicates are handled

**How it works:** Two-phase approach using classical function extraction followed by LLM-powered intent clustering. Haiku categorizes functions by domain, then Opus analyzes each category to find semantic duplicates.

See [skills/finding-duplicate-functions/SKILL.md](../bmad_repo/SKILL.md) for full documentation.

### mcp-cli

Use MCP servers on-demand via the `mcp` CLI tool. Discover and invoke tools, resources, and prompts without polluting context with pre-loaded MCP integrations.

**Use cases:**
- Query MCP servers without permanent configuration
- Explore available tools before deciding to integrate
- One-off MCP tool invocations

See [skills/mcp-cli/SKILL.md](../bmad_repo/SKILL.md) for full documentation.

### using-tmux-for-interactive-commands

Enables Claude Code to control interactive CLI tools (vim, git rebase -i, menuconfig, REPLs, etc.) through tmux sessions.

**Use cases:**
- Interactive text editors (vim, nano)
- Terminal UI tools (menuconfig, htop)
- Interactive REPLs (Python, Node, etc.)
- Interactive git operations (rebase -i, add -p)
- Any tool requiring keyboard navigation and real-time interaction

**How it works:** Creates detached tmux sessions, sends keystrokes programmatically, and captures terminal output to enable automation of traditionally manual workflows.

See [skills/using-tmux-for-interactive-commands/SKILL.md](../bmad_repo/SKILL.md) for full documentation.

### windows-vm

Create, manage, or connect to a headless Windows 11 VM running in Docker with KVM acceleration and SSH access — no RDP or GUI required.

**Use cases:**
- Spin up a Windows environment for testing or development
- Run Claude Code on Windows via SSH
- Test cross-platform behavior without leaving the terminal

**How it works:** Uses [dockur/windows](https://github.com/dockur/windows) to run Windows 11 in a Docker container with KVM acceleration. Manages the full lifecycle: create, start, stop, restart, SSH, and status checks. Includes automated setup of OpenSS
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `superpowers.md`
```markdown
# 📦 obra/superpowers [🔖 PENDING]
🔗 https://github.com/obra/superpowers


## Meta
- **Stars:** ⭐ 115380 | **Forks:** 🍴 9237
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
An agentic skills framework & software development methodology that works.

## README (trích đầu)
```
# Superpowers

Superpowers is a complete software development workflow for your coding agents, built on top of a set of composable "skills" and some initial instructions that make sure your agent uses them.

## How it works

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do. 

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. 

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY. 

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.


## Sponsorship

If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider [sponsoring my opensource work](https://github.com/sponsors/obra).

Thanks! 

- Jesse


## Installation

**Note:** Installation differs by platform. Claude Code or Cursor have built-in plugin marketplaces. Codex and OpenCode require manual setup.

### Claude Code Official Marketplace

Superpowers is available via the [official Claude plugin marketplace](https://claude.com/plugins/superpowers)

Install the plugin from Claude marketplace:

```bash
/plugin install superpowers@claude-plugins-official
```

### Claude Code (via Plugin Marketplace)

In Claude Code, register the marketplace first:

```bash
/plugin marketplace add obra/superpowers-marketplace
```

Then install the plugin from this marketplace:

```bash
/plugin install superpowers@superpowers-marketplace
```

### Cursor (via Plugin Marketplace)

In Cursor Agent chat, install from marketplace:

```text
/add-plugin superpowers
```

or search for "superpowers" in the plugin marketplace.

### Codex

Tell Codex:

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

**Detailed docs:** [docs/README.codex.md](docs/README.codex.md)

### OpenCode

Tell OpenCode:

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

**Detailed docs:** [docs/README.opencode.md](docs/README.opencode.md)

### Gemini CLI

```bash
gemini extensions 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

