---
id: wavyrai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.486203
---

# KNOWLEDGE EXTRACT: wavyrai
> **Extracted on:** 2026-03-30 18:01:16
> **Source:** wavyrai

---

## File: `tmux-ide.md`
```markdown
# 📦 wavyrai/tmux-ide [🔖 PENDING/APPROVE]
🔗 https://github.com/wavyrai/tmux-ide
🌐 https://tmux.thijsverreck.com

## Meta
- **Stars:** ⭐ 286 | **Forks:** 🍴 19
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Turn any project into a tmux-powered terminal IDE with a simple ide.yml

## README (trích đầu)
```
# tmux-ide

[![CI](https://github.com/wavyrai/tmux-ide/actions/workflows/ci.yml/badge.svg)](https://github.com/wavyrai/tmux-ide/actions/workflows/ci.yml)

Turn any project into a tmux-powered terminal IDE with a simple `ide.yml` config file.

## Install

```bash
npm install -g tmux-ide
```

Global install also registers the bundled Claude Code skill and enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in `~/.claude/settings.json` if Claude Code is installed locally on the machine.

## Quick Start

```bash
tmux-ide init         # Scaffold ide.yml (auto-detects your stack)
tmux-ide              # Launch the IDE
tmux-ide stop         # Kill the session
tmux-ide restart      # Stop and relaunch
tmux-ide attach       # Reattach to a running session
tmux-ide inspect      # Inspect effective config + runtime state
```

## ide.yml Format

```yaml
name: project-name # tmux session name

before: pnpm install # optional pre-launch hook

rows:
  - size: 70% # row height percentage
    panes:
      - title: Editor # pane border label
        command: vim # command to run (optional)
        size: 60% # pane width percentage (optional)
        dir: apps/web # per-pane working directory (optional)
        focus: true # initial focus (optional)
        env: # environment variables (optional)
          PORT: 3000
      - title: Shell

  - panes:
      - title: Dev Server
        command: pnpm dev
      - title: Tests
        command: pnpm test

theme: # optional color overrides
  accent: colour75
  border: colour238
  bg: colour235
  fg: colour248
```

## Commands

| Command                                            | Description                             |
| -------------------------------------------------- | --------------------------------------- |
| `tmux-ide`                                         | Launch IDE from `ide.yml`               |
| `tmux-ide <path>`                                  | Launch from a specific directory        |
| `tmux-ide init [--template <name>]`                | Scaffold a new `ide.yml`                |
| `tmux-ide stop`                                    | Kill the current IDE session            |
| `tmux-ide restart`                                 | Stop and relaunch the IDE session       |
| `tmux-ide attach`                                  | Reattach to a running session           |
| `tmux-ide ls`                                      | List all tmux sessions                  |
| `tmux-ide status`                                  | Show session status                     |
| `tmux-ide inspect`                                 | Show effective config and runtime state |
| `tmux-ide doctor`                                  | Check system requirements               |
| `tmux-ide validate`                                | Validate `ide.yml`                      |
| `tmux-ide detect`                                  | Detect project stack and explain why    |
| `tmux-ide detect --write`                          | Detect and wr
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

