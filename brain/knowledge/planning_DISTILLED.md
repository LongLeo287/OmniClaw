---
id: planning
type: knowledge
owner: OA_Triage
---
# planning
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Planning with Files

> **Work like Manus** — the AI agent company Meta acquired for **$2 billion**.

[![Closed Issues](https://img.shields.io/github/issues-closed/OthmanAdi/planning-with-files?color=success)](https://github.com/OthmanAdi/planning-with-files/issues?q=is%3Aissue+is%3Aclosed)
[![Closed PRs](https://img.shields.io/github/issues-pr-closed/OthmanAdi/planning-with-files?color=success)](https://github.com/OthmanAdi/planning-with-files/pulls?q=is%3Apr+is%3Aclosed)
[![Benchmark](https://img.shields.io/badge/Benchmark-96.7%25_pass_rate-brightgreen)](docs/evals.md)
[![A/B Verified](https://img.shields.io/badge/A%2FB_Blind-3%2F3_wins-brightgreen)](docs/evals.md)
[![Security Verified](https://img.shields.io/badge/Security-Audited_%26_Fixed_v2.21.0-blue)](docs/evals.md)

<details>
<summary><strong>💬 A Note from the Author</strong></summary>

To everyone who starred, forked, and shared this skill — thank you. This project blew up in less than 24 hours, and the support from the community has been incredible.

If this skill helps you work smarter, that's all I wanted.

</details>

<details open>
<summary><strong>🌍 See What the Community Built</strong></summary>

| Fork | Author | Features |
|------|--------|----------|
| [devis](https://github.com/st01cs/devis) | [@st01cs](https://github.com/st01cs) | Interview-first workflow, `/devis:intv` and `/devis:impl` commands, guaranteed activation |
| [multi-manus-planning](https://github.com/kmichels/multi-manus-planning) | [@kmichels](https://github.com/kmichels) | Multi-project support, SessionStart git sync |
| [plan-cascade](https://github.com/Taoidle/plan-cascade) | [@Taoidle](https://github.com/Taoidle) | Multi-level task orchestration, parallel execution, multi-agent collaboration |
| [agentfund-skill](https://github.com/RioTheGreat-ai/agentfund-skill) | [@RioTheGreat-ai](https://github.com/RioTheGreat-ai) | Crowdfunding for AI agents with milestone-based escrow on Base |
| [openclaw-github-repo-commander](https://github.com/wd041216-bit/openclaw-github-repo-commander) | [@wd041216-bit](https://github.com/wd041216-bit) | 7-stage GitHub repo audit, optimization, and cleanup workflow for OpenClaw |

*Built something? [Open an issue](https://github.com/OthmanAdi/planning-with-files/issues) to get listed!*

</details>

<details>
<summary><strong>🤝 Contributors</strong></summary>

See the full list of everyone who made this project better in [CONTRIBUTORS.md](./CONTRIBUTORS.md).

</details>

<details>
<summary><strong>📦 Releases & Session Recovery</strong></summary>

### Current Version: v2.30.0

| Version | Highlights |
|---------|------------|
| **v2.30.0** | Migrate to `${CLAUDE_SKILL_DIR}`, IDE configs moved to dedicated branches, cleaner master |
| **v2.29.0** | Analytics workflow template: `--template analytics` flag for data exploration sessions (thanks @mvanhorn!) |
| **v2.28.0** | Traditional Chinese (zh-TW) skill variant (thanks @waynelee2048!) |
| **v2.26.2** | Fix: `---` in hook commands broke YAML frontmatter parsing, hooks now register correctly |
| **v2.26.1** | Fix: session catchup after `/clear`, path sanitization on Windows + content injection (thanks @tony-stark-eth!) |
| **v2.26.0** | IDE audit: Factory hooks, Copilot errorOccurred hook, Gemini hooks, bug fixes |
| **v2.18.2** | Mastra Code hooks fix (hooks.json + docs accuracy) |
| **v2.18.1** | Copilot garbled characters complete fix |
| **v2.18.0** | BoxLite sandbox runtime integration |
| **v2.17.0** | Mastra Code support + all IDE SKILL.md spec fixes |
| **v2.16.1** | Copilot garbled characters fix: PS1 UTF-8 encoding + bash ensure_ascii (thanks @Hexiaopi!) |
| **v2.16.0** | GitHub Copilot hooks support (thanks @lincolnwan!) |
| **v2.27.0** | Kiro Agent Skill layout (thanks @EListenX!) |
| **v2.15.1** | Session catchup false-positive fix (thanks @gydx6!) |
| **v2.15.0** | `/plan:status` command, OpenCode compatibility fix |
| **v2.14.0** | Pi Agent support, OpenClaw docs update, Codex path fix |
| **v2.11.0** | `/plan` command for easier autocomplete |
| **v2.10.0** | Kiro steering files support |
| **v2.7.0** | Gemini CLI support |
| **v2.2.0** | Session recovery, Windows PowerShell, OS-aware hooks |

[View all releases](https://github.com/OthmanAdi/planning-with-files/releases) · [CHANGELOG](CHANGELOG.md)

> 🧪 **Experimental:** Isolated parallel planning (`.planning/{uuid}/` folders) is being tested on [`experimental/isolated-planning`](https://github.com/OthmanAdi/planning-with-files/tree/experimental/isolated-planning). Try it and share feedback!

---

### Session Recovery

When your context fills up and you run `/clear`, this skill **automatically recovers** your previous session.

**How it works:**
1. Checks for previous session data in `~/.claude/projects/`
2. Finds when planning files were last updated
3. Extracts conversation that happened after (potentially lost context)
4. Shows a catchup report so you can sync

**Pro tip:** Disable auto-compact to maximize context before clearing:
```json
{ "autoCompact": false }
```

</details>

<details>
<summary><strong>🛠️ Supported Platforms (16+)</strong></summary>

#### All platforms

The core skill works with any IDE supporting the [Agent Skills](https://agentskills.io) open spec:

```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g
```

This covers Claude Code, Cursor, Codex, Gemini CLI, OpenClaw, Antigravity, Kilocode, AdaL CLI, and 40+ other agents.

#### IDE-specific hooks and configurations

For IDEs with lifecycle hooks (pre-tool, post-tool, stop verification), each IDE has its own branch with adapted SKILL.md and hook scripts:

| IDE | Branch | Guide | Integration |
|-----|--------|-------|-------------|
| Claude Code | `master` (built-in) | [Installation](docs/installation.md) | Plugin + SKILL.md + Hooks |
| Cursor | [`ide/cursor`](../../tree/ide/cursor) | [Setup](docs/cursor.md) | Skills + [hooks.json](https://cursor.com/docs/hooks) |
| GitHub Copilot | [`ide/copilot`](../../tree/ide/copilot) | [Setup](docs/copilot.md) | [Hooks](https://docs.github.com/en/copilot/reference/hooks-configuration) |
| Gemini CLI | [`ide/gemini`](../../tree/ide/gemini) | [Setup](docs/gemini.md) | Skills + [Hooks](https://geminicli.com/docs/hooks/) |
| Kiro | [`ide/kiro`](../../tree/ide/kiro) | [Setup](docs/kiro.md) | [Agent Skills](https://kiro.dev/docs/skills/) |
| Codex | [`ide/codex`](../../tree/ide/codex) | [Setup](docs/codex.md) | [Skills + Hooks](https://developers.openai.com/codex/skills) |
| Mastra Code | [`ide/mastra`](../../tree/ide/mastra) | [Setup](docs/mastra.md) | Skills + [Hooks](https://mastra.ai/docs/mastra-code/configuration) |
| CodeBuddy | [`ide/codebuddy`](../../tree/ide/codebuddy) | [Setup](docs/codebuddy.md) | [Skills + Hooks](https://www.codebuddy.ai/docs/cli/skills) |
| FactoryAI Droid | [`ide/factory`](../../tree/ide/factory) | [Setup](docs/factory.md) | [Skills + Hooks](https://docs.factory.ai/cli/configuration/skills) |
| OpenCode | [`ide/opencode`](../../tree/ide/opencode) | [Setup](docs/opencode.md) | Skills + Custom session storage |
| Continue | [`ide/continue`](../../tree/ide/continue) | [Setup](docs/continue.md) | Skills + [.prompt files](https://docs.continue.dev/customize/deep-dives/prompts) |
| Pi Agent | [`ide/pi-agent`](../../tree/ide/pi-agent) | [Setup](docs/pi-agent.md) | Skills ([npm](https://www.npmjs.com/package/@mariozechner/pi-coding-agent)) |

#### Standard Agent Skills support (no branch needed)

These IDEs work with `npx skills add` out of the box, no IDE-specific branch required:

[OpenClaw](docs/openclaw.md) | [Antigravity](docs/antigravity.md) | [Kilocode](docs/kilocode.md) | [AdaL CLI](docs/adal.md)

> **Note:** If your IDE uses the legacy Rules system instead of Skills, see the [`legacy-rules-support`](https://github.com/OthmanAdi/planning-with-files/tree/legacy-rules-support) branch.

</details>

<details>
<summary><strong>🧱 Sandbox Runtimes (1 Platform)</strong></summary>

| Runtime | Status | Guide | Notes |
|---------|--------|-------|-------|
| BoxLite | Documented | [BoxLite Setup](docs/boxlite.md) | Run Claude Code + planning-with-files inside hardware-isolated micro-VMs |

> **Note:** BoxLite is a sandbox runtime, not an IDE. Skills load via [ClaudeBox](https://github.com/boxlite-ai/claudebox) -- BoxLite’s official Claude Code integration layer.

</details>

<details>
<summary><strong>🌿 Branches</strong></summary>

| Branch | Purpose |
|--------|---------|
| `master` | Core skill, templates, scripts, docs |
| `ide/cursor` | Cursor IDE hooks and SKILL.md |
| `ide/copilot` | GitHub Copilot hooks |
| `ide/gemini` | Gemini CLI hooks and SKILL.md |
| `ide/kiro` | Kiro Agent Skill layout |
| `ide/codex` | Codex CLI hooks and SKILL.md |
| `ide/mastra` | Mastra Code hooks and SKILL.md |
| `ide/codebuddy` | CodeBuddy hooks and SKILL.md |
| `ide/factory` | FactoryAI Droid hooks and SKILL.md |
| `ide/opencode` | OpenCode hooks and SKILL.md |
| `ide/continue` | Continue.dev skill and prompts |
| `ide/pi-agent` | Pi Agent skill |
| `feat/analytics-subagent` | Analytics subagent (closes #103) |
| `experimental/isolated-planning` | Parallel planning sessions |
| `legacy-rules-support` | IDE Rules system (pre-Skills) |

</details>

---

A Claude Code plugin that transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage — the exact pattern that made Manus worth billions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://code.claude.com/docs/en/plugins)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-green)](https://code.claude.com/docs/en/skills)
[![Cursor Skills](https://img.shields.io/badge/Cursor-Skills-purple)](https://docs.cursor.com/context/skills)
[![Kilocode Skills](https://img.shields.io/badge/Kilocode-Skills-orange)](https://kilo.ai/docs/agent-behavior/skills)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Skills-4285F4)](https://geminicli.com/docs/cli/skills/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skills-FF6B6B)](https://openclaw.ai)
[![Kiro](https://img.shields.io/badge/Kiro-Agent_Skill-00D4AA)](https://kiro.dev/docs/skills/)
[![AdaL CLI](https://img.shields.io/badge/AdaL%20CLI-Skills-9B59B6)](https://docs.sylph.ai/features/plugins-and-skills)
[![Pi Agent](https://img.shields.io/badge/Pi%20Agent-Skills-FF4081)](https://pi.dev)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Hooks-000000)](https://docs.github.com/en/copilot/reference/hooks-configuration)
[![Mastra Code](https://img.shields.io/badge/Mastra%20Code-Skills-00BCD4)](https://code.mastra.ai)
[![BoxLite](https://img.shields.io/badge/BoxLite-Sandbox-6C3483)](https://boxlite.ai)
[![Version](https://img.shields.io/badge/version-2.30.0-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1)](https://getskillcheck.com)

## Quick Install

```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g
```

中文版 / Chinese (Simplified):
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-zh -g
```

正體中文版 / Chinese (Traditional):
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-zht -g
```

Works with Claude Code, Cursor, Codex, Gemini CLI, and 40+ agents supporting the [Agent Skills](https://agentskills.io) spec.

<details>
<summary><strong>🔧 Claude Code Plugin (Advanced Features)</strong></summary>

For Claude Code-specific features like `/plan` autocomplete commands:

```
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

</details>

That's it! Now use one of these commands in Claude Code:

| Command | Autocomplete | Description |
|---------|--------------|-------------|
| `/planning-with-files:plan` | Type `/plan` | Start planning session (v2.11.0+) |
| `/planning-with-files:status` | Type `/plan:status` | Show planning progress at a glance (v2.15.0+) |
| `/planning-with-files:start` | Type `/planning` | Original start command |

**Alternative:** If you want `/planning-with-files` (without prefix), copy skills to your local folder:

**macOS/Linux:**
```bash
cp -r ~/.claude/plugins/cache/planning-with-files/planning-with-files/*/skills/planning-with-files ~/.claude/skills/
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse -Path "$env:USERPROFILE\.claude\plugins\cache\planning-with-files\planning-with-files\*\skills\planning-with-files" -Destination "$env:USERPROFILE\.claude\skills\"
```

See [docs/installation.md](docs/installation.md) for all installation methods.

## Why This Skill?

On December 29, 2025, [Meta acquired Manus for $2 billion](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/). In just 8 months, Manus went from launch to $100M+ revenue. Their secret? **Context engineering**.

> "Markdown is my 'working memory' on disk. Since I process information iteratively and my active context has limits, Markdown files serve as scratch pads for notes, checkpoints for progress, building blocks for final deliverables."
> — Manus AI

## The Problem

Claude Code (and most AI agents) suffer from:

- **Volatile memory** — TodoWrite tool disappears on context reset
- **Goal drift** — After 50+ tool calls, original goals get forgotten
- **Hidden errors** — Failures aren't tracked, so the same mistakes repeat
- **Context stuffing** — Everything crammed into context instead of stored

## The Solution: 3-File Pattern

For every complex task, create THREE files:

```
task_plan.md      → Track phases and progress
findings.md       → Store research and findings
progress.md       → Session log and test results
```

### The Core Principle

```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

## The Manus Principles

| Principle | Implementation |
|-----------|----------------|
| Filesystem as memory | Store in files, not context |
| Attention manipulation | Re-read plan before decisions (hooks) |
| Error persistence | Log failures in plan file |
| Goal tracking | Checkboxes show progress |
| Completion verification | Stop hook checks all phases |

## Usage

Once installed, the AI agent will:

1. **Ask for your task** if no description is provided
2. **Create `task_plan.md`, `findings.md`, and `progress.md`** in your project directory
3. **Re-read plan** before major decisions (via PreToolUse hook)
4. **Remind you** to update status after file writes (via PostToolUse hook)
5. **Store findings** in `findings.md` instead of stuffing context
6. **Log errors** for future reference
7. **Verify completion** before stopping (via Stop hook)

Invoke with:
- `/planning-with-files:plan` - Typ
... [TRUNCATED]
```

### File: examples\README.md
```md
# Examples: Planning with Files in Action

This directory contains real-world examples showing how the 3-file planning pattern works in practice.

## Example: Building a Todo App

This walkthrough demonstrates a complete task from start to finish, showing how `task_plan.md`, `findings.md`, and `progress.md` evolve together.

### The Task

**User Request:** "Build a simple command-line todo app in Python that can add, list, and delete tasks."

---

## Phase 1: Initial Planning (Task Start)

### task_plan.md (Initial State)

```markdown
# Task Plan: Build Command-Line Todo App

## Goal
Create a Python CLI todo app with add, list, and delete functionality.

## Current Phase
Phase 1

## Phases

### Phase 1: Requirements & Discovery
- [ ] Understand user intent
- [ ] Identify constraints and requirements
- [ ] Document findings in findings.md
- **Status:** in_progress

### Phase 2: Planning & Structure
- [ ] Define technical approach
- [ ] Create project structure
- [ ] Document decisions with rationale
- **Status:** pending

### Phase 3: Implementation
- [ ] Write todo.py with core functions
- [ ] Implement add functionality
- [ ] Implement list functionality
- [ ] Implement delete functionality
- **Status:** pending

### Phase 4: Testing & Verification
- [ ] Test add operation
- [ ] Test list operation
- [ ] Test delete operation
- [ ] Verify error handling
- **Status:** pending

### Phase 5: Delivery
- [ ] Review code quality
- [ ] Ensure all features work
- [ ] Deliver to user
- **Status:** pending

## Key Questions
1. Should tasks persist between sessions? (Yes - need file storage)
2. What format for storing tasks? (JSON file)
3. Command-line interface style? (Simple argparse)

## Decisions Made
| Decision | Rationale |
|----------|-----------|
|          |           |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Notes
- Update phase status as you progress: pending → in_progress → complete
- Re-read this plan before major decisions (attention manipulation)
- Log ALL errors - they help avoid repetition
```

### findings.md (Initial State)

```markdown
# Findings & Decisions

## Requirements
- Command-line interface
- Add tasks
- List all tasks
- Delete tasks
- Python implementation
- Tasks should persist (survive app restart)

## Research Findings
- (To be filled as we explore)

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
|          |           |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
|       |            |

## Resources
- Python argparse documentation (to be referenced)

## Visual/Browser Findings
- (To be updated after research)

---
*Update this file after every 2 view/browser/search operations*
*This prevents visual information from being lost*
```

### progress.md (Initial State)

```markdown
# Progress Log

## Session: 2026-01-15

### Phase 1: Requirements & Discovery
- **Status:** in_progress
- **Started:** 2026-01-15 10:00
- Actions taken:
  - Created task_plan.md
  - Created findings.md
  - Created progress.md
- Files created/modified:
  - task_plan.md (created)
  - findings.md (created)
  - progress.md (created)

### Phase 2: Planning & Structure
- **Status:** pending
- Actions taken:
  -
- Files created/modified:
  -

## Test Results
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
|      |       |          |        |        |

## Error Log
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
|           |       | 1       |            |

## 5-Question Reboot Check
| Question | Answer |
|----------|--------|
| Where am I? | Phase 1 - Requirements & Discovery |
| Where am I going? | Phase 2-5: Planning, Implementation, Testing, Delivery |
| What's the goal? | Build Python CLI todo app with add/list/delete |
| What have I learned? | See findings.md |
| What have I done? | Created planning files |

---
*Update after completing each phase or encountering errors*
```

---

## Phase 2: After Research & Planning

### task_plan.md (Updated)

```markdown
# Task Plan: Build Command-Line Todo App

## Goal
Create a Python CLI todo app with add, list, and delete functionality.

## Current Phase
Phase 2

## Phases

### Phase 1: Requirements & Discovery
- [x] Understand user intent ✓
- [x] Identify constraints and requirements ✓
- [x] Document findings in findings.md ✓
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Define technical approach ✓
- [x] Create project structure ✓
- [x] Document decisions with rationale ✓
- **Status:** complete

### Phase 3: Implementation
- [ ] Write todo.py with core functions
- [ ] Implement add functionality
- [ ] Implement list functionality
- [ ] Implement delete functionality
- **Status:** in_progress

### Phase 4: Testing & Verification
- [ ] Test add operation
- [ ] Test list operation
- [ ] Test delete operation
- [ ] Verify error handling
- **Status:** pending

### Phase 5: Delivery
- [ ] Review code quality
- [ ] Ensure all features work
- [ ] Deliver to user
- **Status:** pending

## Key Questions
1. Should tasks persist between sessions? ✓ Yes - using JSON file
2. What format for storing tasks? ✓ JSON file (todos.json)
3. Command-line interface style? ✓ argparse with subcommands

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use JSON for storage | Simple, human-readable, built-in Python support |
| argparse with subcommands | Clean CLI: `python todo.py add "task"`, `python todo.py list` |
| Store in todos.json | Standard location, easy to find and debug |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Notes
- Update phase status as you progress: pending → in_progress → complete
- Re-read this plan before major decisions (attention manipulation)
- Log ALL errors - they help avoid repetition
```

### findings.md (Updated)

```markdown
# Findings & Decisions

## Requirements
- Command-line interface
- Add tasks
- List all tasks
- Delete tasks
- Python implementation
- Tasks should persist (survive app restart)

## Research Findings
- Python's `argparse` module is perfect for CLI subcommands
- `json` module handles file persistence easily
- Standard pattern: `python todo.py <command> [args]`
- File structure: Single `todo.py` file is sufficient for this scope

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Use JSON for storage | Simple, human-readable, built-in Python support |
| argparse with subcommands | Clean CLI: `python todo.py add "task"`, `python todo.py list` |
| Store in todos.json | Standard location, easy to find and debug |
| Single file structure | Simple enough for one file, can refactor later if needed |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
|       |            |

## Resources
- Python argparse documentation: https://docs.python.org/3/library/argparse.html
- Python json module: https://docs.python.org/3/library/json.html

## Visual/Browser Findings
- Reviewed argparse examples - subcommand pattern is straightforward
- JSON file format: array of objects with `id` and `task` fields

---
*Update this file after every 2 view/browser/search operations*
*This prevents visual information from being lost*
```

### progress.md (Updated)

```markdown
# Progress Log

## Session: 2026-01-15

### Phase 1: Requirements & Discovery
- **Status:** complete
- **Started:** 2026-01-15 10:00
- **Completed:** 2026-01-15 10:15
- Actions taken:
  - Created task_plan.md
  - Created findings.md
  - Created progress.md
  - Researched Python CLI patterns
  - Decided on JSON storage
- Files created/modified:
  - task_plan.md (created, updated)
  - findings.md (created, updated)
  - progress.md (created)

### Phase 2: Planning & Structure
- **Status:** complete
- **Started:** 2026-01-15 10:15
- **Completed:** 2026-01-15 10:20
- Actions taken:
  - Defined technical approach (argparse + JSON)
  - Documented decisions in findings.md
  - Updated task_plan.md with decisions
- Files created/modified:
  - task_plan.md (updated)
  - findings.md (updated)

### Phase 3: Implementation
- **Status:** in_progress
- **Started:** 2026-01-15 10:20
- Actions taken:
  - Starting to write todo.py
- Files created/modified:
  - (todo.py will be created)

## Test Results
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
|      |       |          |        |        |

## Error Log
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
|           |       | 1       |            |

## 5-Question Reboot Check
| Question | Answer |
|----------|--------|
| Where am I? | Phase 3 - Implementation |
| Where am I going? | Phase 4-5: Testing, Delivery |
| What's the goal? | Build Python CLI todo app with add/list/delete |
| What have I learned? | argparse subcommands, JSON storage pattern (see findings.md) |
| What have I done? | Completed planning, starting implementation |

---
*Update after completing each phase or encountering errors*
```

---

## Phase 3: During Implementation (With Error)

### task_plan.md (After Error Encountered)

```markdown
# Task Plan: Build Command-Line Todo App

## Goal
Create a Python CLI todo app with add, list, and delete functionality.

## Current Phase
Phase 3

## Phases

### Phase 1: Requirements & Discovery
- [x] Understand user intent ✓
- [x] Identify constraints and requirements ✓
- [x] Document findings in findings.md ✓
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Define technical approach ✓
- [x] Create project structure ✓
- [x] Document decisions with rationale ✓
- **Status:** complete

### Phase 3: Implementation
- [x] Write todo.py with core functions ✓
- [x] Implement add functionality ✓
- [ ] Implement list functionality (CURRENT)
- [ ] Implement delete functionality
- **Status:** in_progress

### Phase 4: Testing & Verification
- [ ] Test add operation
- [ ] Test list operation
- [ ] Test delete operation
- [ ] Verify error handling
- **Status:** pending

### Phase 5: Delivery
- [ ] Review code quality
- [ ] Ensure all features work
- [ ] Deliver to user
- **Status:** pending

## Key Questions
1. Should tasks persist between sessions? ✓ Yes - using JSON file
2. What format for storing tasks? ✓ JSON file (todos.json)
3. Command-line interface style? ✓ argparse with subcommands

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use JSON for storage | Simple, human-readable, built-in Python support |
| argparse with subcommands | Clean CLI: `python todo.py add "task"`, `python todo.py list` |
| Store in todos.json | Standard location, easy to find and debug |
| Use incremental IDs | Simple counter, easier than UUIDs for this use case |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| FileNotFoundError when reading todos.json | 1 | Check if file exists, create empty list if not |
| JSONDecodeError on empty file | 2 | Handle empty file case explicitly |

## Notes
- Update phase status as you progress: pending → in_progress → complete
- Re-read this plan before major decisions (attention manipulation)
- Log ALL errors - they help avoid repetition
```

### progress.md (With Error Logged)

```markdown
# Progress Log

## Session: 2026-01-15

### Phase 1: Requirements & Discovery
- **Status:** complete
- **Started:** 2026-01-15 10:00
- **Completed:** 2026-01-15 10:15
- Actions taken:
  - Created task_plan.md
  - Created findings.md
  - Created progress.md
  - Researched Python CLI patterns
  - Decided on JSON storage
- Files created/modified:
  - task_plan.md (created, updated)
  - findings.md (created, updated)
  - progress.md (created)

### Phase 2: Planning & Structure
- **Status:** complete
- **Started:** 2026-01-15 10:15
- **Completed:** 2026-01-15 10:20
- Actions taken:
  - Defined technical approach (argparse + JSON)
  - Documented decisions in findings.md
  - Updated task_plan.md with decisions
- Files created/modified:
  - task_plan.md (updated)
  - findings.md (updated)

### Phase 3: Implementation
- **Status:** in_progress
- **Started:** 2026-01-15 10:20
- Actions taken:
  - Created todo.py with basic structure
  - Implemented add functionality
  - Encountered FileNotFoundError (handled)
  - Encountered JSONDecodeError on empty file (handled)
  - Working on list functionality
- Files created/modified:
  - todo.py (created, modified)
  - todos.json (created by app)

## Test Results
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| Add task | `python todo.py add "Buy milk"` | Task added to todos.json | Task added successfully | ✓ |
| List tasks | `python todo.py list` | Shows all tasks | FileNotFoundError (fixed) | Fixed |

## Error Log
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
| 2026-01-15 10:35 | FileNotFoundError when reading todos.json | 1 | Added file existence check, create empty list if not exists |
| 2026-01-15 10:37 | JSONDecodeError on empty file | 2 | Added explicit empty file handling before json.load() |

## 5-Question Reboot Check
| Question | Answer |
|----------|--------|
| Where am I? | Phase 3 - Implementation (working on list functionality) |
| Where am I going? | Phase 4-5: Testing, Delivery |
| What's the goal? | Build Python CLI todo app with add/list/delete |
| What have I learned? | Need to handle file not existing, empty file edge cases (see findings.md) |
| What have I done? | Completed add functionality, fixed file handling errors, working on list |

---
*Update after completing each phase or encountering errors*
```

---

## Phase 4: Task Complete

### task_plan.md (Final State)

```markdown
# Task Plan: Build Command-Line Todo App

## Goal
Create a Python CLI todo app with add, list, and delete functionality.

## Current Phase
Phase 5 (Complete)

## Phases

### Phase 1: Requirements & Discovery
- [x] Understand user intent ✓
- [x] Identify constraints and requirements ✓
- [x] Document findings in findings.md ✓
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Define technical approach ✓
- [x] Create project structure ✓
- [x] Document decisions with rationale ✓
- **Status:** complete

### Phase 3: Implementation
- [x] Write todo.py with core functions ✓
- [x] Implement add functionality ✓
- [x] Implement list functionality ✓
- [x] Implement delete functionality ✓
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Test add operation ✓
- [x] Test list operation ✓
- [x] Test delete operation ✓
- [x] Verify error handling ✓
- **Status:** complete

### Phase 5: Delivery
- [x] Review code quality ✓
- [x] Ensure all features work ✓
- [x] Deliver to user ✓
- **Status:** complete

## Key Questions
1. Should tasks persist between sessions? ✓ Yes - using JSON file
2. What format for storing tasks? ✓
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

## [2.30.0] - 2026-04-03

### Changed

- **Migrate from `${CLAUDE_PLUGIN_ROOT}` to `${CLAUDE_SKILL_DIR}`** in main SKILL.md
  - Stop hook, session-catchup path, and templates path now use `${CLAUDE_SKILL_DIR}` (added in Claude Code v2.1.69)
  - 3-level fallback chain for backward compatibility: `CLAUDE_SKILL_DIR` -> `CLAUDE_PLUGIN_ROOT` -> hardcoded path
  - Default fallback path updated from `.claude/plugins/planning-with-files` to `.claude/skills/planning-with-files` (matches `npx skills add` install location)
  - Fixes path resolution failures on Windows and Linux (related to #32)

### Restructured

- **IDE-specific configurations moved to dedicated branches**
  - Master branch now contains only the core skill, templates, scripts, and docs
  - Each IDE has its own branch: `ide/cursor`, `ide/copilot`, `ide/gemini`, `ide/kiro`, `ide/codex`, `ide/mastra`, `ide/codebuddy`, `ide/factory`, `ide/opencode`, `ide/continue`, `ide/pi-agent`
  - README updated with branch reference table
  - Reduces master branch clutter and makes per-IDE maintenance independent

---

## [2.29.0] - 2026-03-24

### Added

- **Analytics workflow template** (PR #115 by @mvanhorn, addresses #103)
  - New `--template analytics` flag on `init-session.sh` and `init-session.ps1`
  - `templates/analytics_task_plan.md` with 4 analytics-specific phases: Data Discovery, Exploratory Analysis, Hypothesis Testing, Synthesis
  - `templates/analytics_findings.md` with Data Sources table, Hypothesis Log, Query Results, and Statistical Findings sections
  - Analytics-specific `progress.md` generates a Query Log table instead of Test Results
  - Default behavior unchanged; existing users are not affected

### Usage

```bash
./scripts/init-session.sh --template analytics my-project
```

### Thanks

- @mvanhorn (Matt Van Horn) for implementing the analytics template that @sedlukha requested in #103

---

## [2.28.0] - 2026-03-22

### Added

- **Traditional Chinese (zh-TW) skill variant** (PR #113 by @waynelee2048)
  - Fully translated SKILL.md, templates, and scripts under `skills/planning-with-files-zht/`
  - Localized hooks, check-complete, init-session, and session-catchup scripts

### Thanks

- @waynelee2048 for the Traditional Chinese translation

---

## [2.27.0] - 2026-03-20

### Added

- **Kiro Agent Skill support** (PR #112 by @EListenX)
  - Full `.kiro/skills/planning-with-files/` layout with SKILL.md, bootstrap scripts, templates, references
  - Bootstrap creates `.kiro/plan/` for planning files and `.kiro/steering/planning-context.md` with `#[[file:]]` live references
  - Includes session-catchup.py and check-complete scripts adapted for Kiro's `.kiro/plan/` path
  - Replaces the old `.kiro/scripts/` and `.kiro/steering/` approach with proper Agent Skill format

### Changed

- Updated `scripts/sync-ide-folders.py` to skip `.kiro` (Kiro uses its own skill layout)
- Rewrote `docs/kiro.md` to reflect new Agent Skill approach

### Thanks

- @EListenX (Yi Chenxi) for the thorough Kiro integration with proper Agent Skill format

---

## [2.23.0] - 2026-03-16

### Fixed

- **Session catchup not working after `/clear`** (Issue #106 by @tony-stark-eth)
  - Root cause: No hook fired on session start to remind the agent about existing planning files. After `/clear`, the agent started fresh with no awareness of the active plan.
  - Added `UserPromptSubmit` hook across all 7 IDE SKILL.md files. When `task_plan.md` exists, the hook injects a directive to read all three planning files before proceeding. This fires on every user message, ensuring the agent always knows about active plans even after `/clear` or context compaction.
  - Strengthened SKILL.md "FIRST" section: now explicitly says to read all three files immediately, not just run session catchup.

- **Progress not updating consistently** (Issue #106)
  - Root cause: `PostToolUse` hook message only mentioned `task_plan.md`, never `progress.md`. The agent was never reminded to log what it did.
  - Changed PostToolUse message across all 7 IDE SKILL.md files and both Copilot hook scripts to lead with "Update progress.md with what you just did."
  - Added `if [ -f task_plan.md ]` guard so the reminder only fires when a plan is active.

- **Post-plan additions not tracked** (Issue #106)
  - Root cause: When all phases were complete, `check-complete` scripts reported "ALL PHASES COMPLETE" with no guidance about continuing. The agent had no reason to add new work to the plan.
  - Updated `check-complete.sh` and `check-complete.ps1`: completion message now says "If the user has additional work, add new phases to task_plan.md before starting."
  - Updated Copilot `agent-stop` scripts to output continuation context even when all phases are complete (previously returned empty `{}`).
  - Added Critical Rule #7 ("Continue After Completion") to canonical SKILL.md body.

### Changed

- Version bumped to 2.23.0 across all 7 IDE SKILL.md files, plugin.json, and marketplace.json

### Thanks

- @tony-stark-eth for the detailed bug report covering all three symptoms (Issue #106)

---

## [2.22.0] - 2026-03-06

### Added

- **Formal benchmark results** — skill evaluated using Anthropic's skill-creator framework
  - 10 parallel subagents, 5 diverse task types, 30 objectively verifiable assertions
  - with_skill: **96.7% pass rate** (29/30); without_skill: 6.7% (2/30) — delta: +90 percentage points
  - 3 blind A/B comparisons: with_skill wins 3/3 (100%), avg score 10.0/10 vs 6.8/10
  - Full methodology in [docs/evals.md](docs/evals.md)
- **Technical article** — [docs/article.md](docs/article.md): full write-up of the security analysis, fix, and eval methodology
- **README badges** — Benchmark (96.7% pass rate), A/B Verified (3/3 wins), Security Verified
- **README Benchmark Results section** — key numbers visible at a glance

### Changed

- `marketplace.json` version corrected to track current release (was stuck at 2.0.0)

## [2.21.0] - 2026-03-05

### Security

- **Remove `WebFetch` and `WebSearch` from `allowed-tools`** — fixes Gen Agent Trust Hub FAIL and reduces Snyk W011 risk score
  - The planning-with-files skill is a file-management and planning skill; web access is not part of its core scope
  - The PreToolUse hook re-reads `task_plan.md` before every tool call, creating an amplification vector when web-sourced content is written to plan files. Removing these tools from the skill's declared scope breaks the toxic flow
  - Applied across all 7 IDE variants that declared `allowed-tools`: Claude Code, Cursor, Kilocode, CodeBuddy, Codex, OpenCode, Mastra Code
- **Add Security Boundary section to SKILL.md** — explicit guidance that web/search results must go to `findings.md` only (not `task_plan.md`), and all external content must be treated as untrusted
- **Add security note to examples.md** — the web research example now includes an inline comment reinforcing the trust boundary

## [2.20.0] - 2026-03-04

### Fixed

- **Codex session-catchup silent failure** (PR #100 by @tt-a1i, fixes #94)
  - `session-catchup.py` in the Codex variant was silently scanning `~/.claude/projects` even when running from a Codex context, where sessions live under `~/.codex/sessions` in a different format
  - Now detects the Codex runtime from `__file__` path and prints a clear fallback message instead of a silent no-op

- **Docs broken links** (PR #99 by @tt-a1i, fixes #95)
  - `docs/opencode.md` linked to `.opencode/INSTALL.md` which does not exist — corrected to `docs/installation.md`
  - `docs/factory.md` See Also links used `../skills/planning-with-files/` paths — corrected to `../.factory/skills/planning-with-files/`

- **Examples used stale `notes.md` filename** (PR #99 by @tt-a1i, fixes #96)
  - All `examples.md` files across 16 IDE copies referenced `notes.md` which was renamed to `findings.md` — updated consistently everywhere

- **`sync-ide-folders.py --help` ran a sync instead of printing usage** (PR #99 by @tt-a1i, fixes #98)
  - Replaced manual `sys.argv` parsing with `argparse` — `--help` now exits cleanly with usage information

### Changed

- **OpenCode README support label corrected** (PR #99 by @tt-a1i, fixes #97)
  - Changed from `Full Support` to `Partial Support` with a note about session catchup limitations — aligns README with what `docs/opencode.md` actually says

### Thanks

- @tt-a1i for the full consistency sweep (PR #99, PR #100)

---

## [2.19.0] - 2026-03-04

### Fixed

- **Codex Advanced Topics broken links** (PR #92 by @tt-a1i, fixes #91)
  - Corrected two dead links in `.codex/skills/planning-with-files/SKILL.md`
  - `reference.md` → `references/reference.md`
  - `examples.md` → `references/examples.md`

### Thanks

- @tt-a1i for identifying and fixing the broken Codex links (PR #92)

---

## [2.18.3] - 2026-02-28

### Fixed

- **Stop hook multiline YAML command fails under Git Bash on Windows** (PR #86 by @raykuo998)
  - Root cause: YAML `command: |` multiline blocks are not reliably parsed by Git Bash on Windows. The shell received the first line (`SCRIPT_DIR=...`) as a command name rather than a variable assignment, crashing the hook before it could do anything.
  - Replaced 25-line OS detection scripts with a single-line implicit platform fallback chain: `powershell.exe` first, `sh` as fallback. Applied to all 7 SKILL.md variants with Stop hooks.
  - Added `-NoProfile` to PowerShell invocation for faster startup

- **`check-complete.ps1` completely failing on PowerShell 5.1** (PR #88 by @raykuo998)
  - Root cause: Special characters inside double-quoted `Write-Host` strings (`[`, `(`, em-dash) caused parse errors in Windows PowerShell 5.1
  - Replaced double-quoted strings with single-quoted strings plus explicit concatenation for variable interpolation. Applied to all 12 platform copies.

### Thanks

- @raykuo998 for both Windows compatibility fixes (PR #86, PR #88)

---

## [2.18.2] - 2026-02-26

### Fixed

- **Mastra Code hooks were silently doing nothing**
  - Root cause: Mastra Code reads hooks from `.mastracode/hooks.json`, not from SKILL.md frontmatter. The existing integration had hooks defined only in SKILL.md (Claude Code format), which Mastra Code ignores entirely. All three hooks (PreToolUse, PostToolUse, Stop) were non-functional.
  - Added `.mastracode/hooks.json` with proper Mastra Code format including `matcher`, `timeout`, and `description` fields
  - Fixed `MASTRACODE_SKILL_ROOT` env var in SKILL.md Stop hook (variable does not exist in Mastra Code, replaced with `$HOME` fallback to local path)
  - Bumped `.mastracode/skills/planning-with-files/SKILL.md` metadata version from 2.16.1 to 2.18.1
  - Corrected `docs/mastra.md` to accurately describe hooks.json (removed false claim that Mastra Code uses the same hook system as Claude Code)
  - Fixed personal installation instructions to include hooks.json copy step

---

## [2.18.1] - 2026-02-26

### Fixed

- **Copilot hooks garbled characters — still broken after v2.16.1** (Issue #82, confirmed by @Hexiaopi)
  - Root cause: `Get-Content` in all PS1 scripts had no `-Encoding` parameter — PowerShell 5.x reads files using the system ANSI code page (Windows-1252) by default, corrupting any non-ASCII character in `task_plan.md` or `SKILL.md` before it reaches the output pipe. The v2.16.1 fix was correct but fixed only the output side, not the read side.
  - Secondary fix: `[System.Text.Encoding]::UTF8` returns UTF-8 with BOM — replaced with `[System.Text.UTF8Encoding]::new($false)` (UTF-8 without BOM) in all four PS1 scripts to prevent JSON parsers from receiving a stray `0xEF 0xBB 0xBF` preamble
  - Fixed files: `pre-tool-use.ps1`, `session-start.ps1`, `agent-stop.ps1`, `post-tool-use.ps1`
  - Bash scripts were already correct from v2.16.1

### Thanks

- @Hexiaopi for confirming the issue persisted after v2.16.1 (Issue #82)

---

## [2.18.0] - 2026-02-26

### Added

- **BoxLite sandbox runtime integration** (Issue #84 by @DorianZheng)
  - New `docs/boxlite.md` guide for running planning-with-files inside BoxLite micro-VM sandboxes via ClaudeBox
  - New `examples/boxlite/quickstart.py` — working Python example using ClaudeBox's Skill API to inject planning-with-files into a VM
  - New `examples/boxlite/README.md` — example context and requirements
  - README: new "Sandbox Runtimes" section (BoxLite is infrastructure, not an IDE — kept separate from the 16-platform IDE table)
  - README: BoxLite badge and Documentation table entry added
  - BoxLite loads via ClaudeBox (`pip install claudebox`) using its Python Skill object — no `.boxlite/` folder needed

### Thanks

- @DorianZheng for the BoxLite integration proposal (Issue #84)

---

## [2.17.0] - 2026-02-25

### Added

- **Mastra Code support** — new `.mastracode/skills/planning-with-files/` integration with native hooks (PreToolUse, PostToolUse, Stop), full scripts, templates, and installation guide (platform #16)

### Fixed

- **Skill metadata spec compliance** — applied PR #83 fixes across all 12 IDE-specific SKILL.md files:
  - `allowed-tools` YAML list → comma-separated string (Codex, Cursor, Kilocode, CodeBuddy, OpenCode)
  - `version` moved from top-level to `metadata.version` across all applicable files
  - Description updated with trigger terms ("plan out", "break down", "organize", "track progress") in all IDEs
  - Version bumped to 2.16.1 everywhere, including canonical `skills/planning-with-files/SKILL.md`
  - OpenClaw inline JSON metadata expanded to proper block YAML

### Thanks

- @popey for the PR #83 spec fixes that identified the issues

---

## [2.16.1] - 2026-02-25

### Fixed

- **Copilot hooks garbled characters on Windows** (Issue #82, reported by @Hexiaopi)
  - PowerShell scripts now set `$OutputEncoding` and `[Console]::OutputEncoding` to UTF-8 before any output — fixes garbled diamond characters (◆) caused by PowerShell 5.x defaulting to UTF-16LE stdout
  - Bash scripts now use `json.dumps(..., ensure_ascii=False)` — preserves UTF-8 characters (emojis, accented letters, CJK) in `task_plan.md` instead of converting them to raw `XXXX` escape sequences

### Thanks

- @Hexiaopi for reporting the garbled characters issue (Issue #82)

---

## [2.16.0] - 2026-02-22

### Added

- **GitHub Copilot Support** (PR #80 by @lincolnwan)
  - Native GitHub Copilot hooks integration (early 2026 hooks feature)
  - Created `.github/hooks/planning-with-files.json` configuration
  - Added full hook scripts in `.github/hooks/scripts/`
  - Cross-platform support (bash + PowerShell)
  - Added `docs/copilot.md` installation guide
  - Added GitHub Copilot badge to README
  - This brings total supported platforms to 15

### Thanks

- @lincolnwan for GitHub Copilot hooks support (PR #80)

---

## [2.14.0] - 2026-02-04

### Added

- **Pi Agent Support** (PR #67 by @ttttmr)
  - Full Pi Agent (pi.dev) integration
  - Created `.pi/skills/planning-with-files/` skill bundle
  - Added `package.json` for NPM installation (`pi
... [TRUNCATED]
```

### File: CONTRIBUTORS.md
```md
# Contributors

Thank you to everyone who has contributed to making `planning-with-files` better!

## Project Author

- **[Ahmad Othman Ammar Adi](https://github.com/OthmanAdi)** - Original creator and maintainer

## Code Contributors

These amazing people have contributed code, documentation, or significant improvements to the project:

### Major Contributions

- **[@kaichen](https://github.com/kaichen)** - [PR #9](https://github.com/OthmanAdi/planning-with-files/pull/9)
  - Converted the repository to Claude Code plugin structure
  - Enabled marketplace installation
  - Followed official plugin standards
  - **Impact:** Made the skill accessible to the masses

- **[@fuahyo](https://github.com/fuahyo)** - [PR #12](https://github.com/OthmanAdi/planning-with-files/pull/12)
  - Added "Build a todo app" walkthrough with 4 phases
  - Created inline comments for templates (WHAT/WHY/WHEN/EXAMPLE)
  - Developed Quick Start guide with ASCII reference tables
  - Created workflow diagram showing task lifecycle
  - **Impact:** Dramatically improved beginner onboarding

- **[@lasmarois](https://github.com/lasmarois)** - [PR #33](https://github.com/OthmanAdi/planning-with-files/pull/33)
  - Created session recovery feature for context preservation after `/clear`
  - Built `session-catchup.py` script to analyze previous session JSONL files
  - Enhanced PreToolUse hook to include Read/Glob/Grep operations
  - Restructured SKILL.md for better session recovery workflow
  - **Impact:** Solves context loss problem, enables seamless work resumption

- **[@aimasteracc](https://github.com/aimasteracc)** - [PR #30](https://github.com/OthmanAdi/planning-with-files/pull/30)
  - Added Kilocode IDE support and documentation
  - Created PowerShell scripts for Windows compatibility
  - Added `.kilocode/rules/` configuration
  - Updated documentation for multi-IDE support
  - **Impact:** Windows compatibility and IDE ecosystem expansion

- **[@SaladDay](https://github.com/SaladDay)** - [PR #57](https://github.com/OthmanAdi/planning-with-files/pull/57)
  - Fixed Stop hook POSIX sh compatibility for Debian/Ubuntu
  - Replaced bashisms (`[[`, `&>`) with POSIX constructs
  - Added shell-agnostic Windows detection using `uname -s`
  - **Impact:** Fixes hook failures on systems using dash as `/bin/sh`

- **[@murphyXu](https://github.com/murphyXu)** - [PR #56](https://github.com/OthmanAdi/planning-with-files/pull/56)
  - Added Continue IDE integration (VS Code / JetBrains)
  - Created `.continue/skills/` and `.continue/prompts/` structure
  - Added Chinese language slash command prompt
  - Created `docs/continue.md` installation guide
  - **Impact:** Expands IDE support to Continue.dev ecosystem

- **[@ZWkang](https://github.com/ZWkang)** - [PR #60](https://github.com/OthmanAdi/planning-with-files/pull/60)
  - Added CodeBuddy IDE integration (Tencent Cloud AI coding assistant)
  - Created `.codebuddy/skills/` folder with full skill structure
  - Added templates, scripts, and references for CodeBuddy
  - Created `docs/codebuddy.md` installation guide
  - **Impact:** Expands IDE support to CodeBuddy ecosystem

- **[@EListenX](https://github.com/EListenX)** (Yi Chenxi) - [PR #112](https://github.com/OthmanAdi/planning-with-files/pull/112)
  - Added full Kiro Agent Skill support under `.kiro/skills/planning-with-files/`
  - Created bootstrap scripts, steering integration with `#[[file:]]` live references
  - Replaced old `.kiro/scripts/` and `.kiro/steering/` with proper Agent Skill layout
  - Updated Cursor and Mastra Code hooks, improved docs/kiro.md
  - **Impact:** Brings Kiro IDE support to production quality with native Agent Skill format

- **[@lincolnwan](https://github.com/lincolnwan)** - [PR #80](https://github.com/OthmanAdi/planning-with-files/pull/80)
  - Added native GitHub Copilot hooks integration using the early 2026 hooks system
  - Created `.github/hooks/planning-with-files.json` with full hook scripts in `.github/hooks/scripts/`
  - Full cross-platform support (bash + PowerShell) and `docs/copilot.md` installation guide
  - **Impact:** Brought total supported platforms to 15, expanding the skill to the GitHub Copilot ecosystem

- **[@ciberponk](https://github.com/ciberponk)** - [PR #77](https://github.com/OthmanAdi/planning-with-files/pull/77)
  - Added isolated `.planning/{uuid}/` plan sessions with UUID generation and PLAN_ID pinning
  - Enables parallel planning sessions in separate terminals without state collision
  - Cross-platform scripts (bash + PowerShell) with full backward compatibility for single-session users
  - **Impact:** Unlocks parallel planning workflows, shipped to experimental branch ahead of master

- **[@ttttmr](https://github.com/ttttmr)** - [PR #67](https://github.com/OthmanAdi/planning-with-files/pull/67)
  - Added Pi Agent support with full skill integration
  - **Impact:** Expands the skill to the Pi Agent ecosystem

- **[@mvanhorn](https://github.com/mvanhorn)** (Matt Van Horn) - [PR #115](https://github.com/OthmanAdi/planning-with-files/pull/115)
  - Added analytics workflow template with `--template analytics` flag on `init-session.sh` and `init-session.ps1`
  - Created `analytics_task_plan.md` with 4 analytics-specific phases (Data Discovery, Exploratory Analysis, Hypothesis Testing, Synthesis)
  - Created `analytics_findings.md` with Data Sources table, Hypothesis Log, Query Results, and Statistical Findings sections
  - Analytics-specific `progress.md` with Query Log replacing Test Results
  - **Impact:** Extends the planning pattern to data analytics workflows (addresses #103)

### Other Contributors

- **[@popey](https://github.com/popey)** - [PR #83](https://github.com/OthmanAdi/planning-with-files/pull/83)
  - Fixed `allowed-tools` YAML list (invalid per Anthropic skill spec, silently killing discoverability)
  - Fixed `metadata.version` placement and added trigger terms for better skill matching
  - Applied across the canonical SKILL.md file

- **[@jonthebeef](https://github.com/jonthebeef)** - [PR #75](https://github.com/OthmanAdi/planning-with-files/pull/75)
  - Added `/plan:status` command for quick planning progress display without reading through all planning files

- **[@codelyc](https://github.com/codelyc)** - [PR #66](https://github.com/OthmanAdi/planning-with-files/pull/66), [PR #70](https://github.com/OthmanAdi/planning-with-files/pull/70), [PR #76](https://github.com/OthmanAdi/planning-with-files/pull/76)
  - Fixed Codex skill path references and replaced CLAUDE_PLUGIN_ROOT with correct absolute paths (PR #66)
  - Fixed CodeBuddy skill path references and environment variables (PR #70)
  - Added OpenCode scripts for the planning-with-files skill (PR #76)

- **[@Guozihong](https://github.com/Guozihong)** - [PR #51](https://github.com/OthmanAdi/planning-with-files/pull/51)
  - Added `/planning-with-files:start` command, enabling skill activation without copying files manually

- **[@fahmyelraie](https://github.com/fahmyelraie)** - [PR #49](https://github.com/OthmanAdi/planning-with-files/pull/49)
  - Fixed Stop hook path resolution when CLAUDE_PLUGIN_ROOT is not set in the environment

- **[@olgasafonova](https://github.com/olgasafonova)** - [PR #46](https://github.com/OthmanAdi/planning-with-files/pull/46)
  - Added SkillCheck validation badge after running the skill through spec validation

- **[@AZLabsAI](https://github.com/AZLabsAI)** - [PR #65](https://github.com/OthmanAdi/planning-with-files/pull/65)
  - Updated OpenClaw docs to reflect the product rename from Moltbot, correcting all paths and CLI commands

- **[@raykuo998](https://github.com/raykuo998)** - [PR #88](https://github.com/OthmanAdi/planning-with-files/pull/88), [PR #86](https://github.com/OthmanAdi/planning-with-files/pull/86)
  - Fixed `check-complete.ps1` completely failing on PowerShell 5.1 due to special character parse errors in double-quoted strings; switched to single-quoted strings with concatenation across all 12 platform copies (PR #88)
  - Fixed Stop hook YAML multiline command block failing under Git Bash on Windows; collapsed 25-line OS detection to single-line implicit platform fallback chain across all 7 SKILL.md variants (PR #86)

- **[@gydx6](https://github.com/gydx6)** - [PR #79](https://github.com/OthmanAdi/planning-with-files/pull/79)
  - Fixed session-catchup false positives in all 9 skill-distributed copies
  - Added early return guards for non-planning projects
  - Thorough bug report with root cause analysis
  - **Impact:** Eliminates noise from false catchup reports

- **[@waynelee2048](https://github.com/waynelee2048)** - [PR #113](https://github.com/OthmanAdi/planning-with-files/pull/113)
  - Added Traditional Chinese (zh-TW) skill variant with fully translated SKILL.md, templates, and scripts
  - Includes localized hooks, check-complete, init-session, and session-catchup scripts

- **[@tobrun](https://github.com/tobrun)** - [PR #3](https://github.com/OthmanAdi/planning-with-files/pull/3)
  - Early directory structure improvements
  - Helped identify optimal repository layout

- **[@markocupic024](https://github.com/markocupic024)** - [PR #4](https://github.com/OthmanAdi/planning-with-files/pull/4)
  - Cursor IDE support contribution
  - Helped establish multi-IDE pattern

- **Copilot SWE Agent** - [PR #16](https://github.com/OthmanAdi/planning-with-files/pull/16)
  - Fixed template bundling in plugin.json
  - Added `assets` field to ensure templates copy to cache
  - **Impact:** Resolved template path issues

- **[@tt-a1i](https://github.com/tt-a1i)** - [PR #92](https://github.com/OthmanAdi/planning-with-files/pull/92), [PR #99](https://github.com/OthmanAdi/planning-with-files/pull/99), [PR #100](https://github.com/OthmanAdi/planning-with-files/pull/100)
  - Fixed broken Advanced Topics links in Codex SKILL.md (PR #92)
  - Fixed 5 consistency issues across docs: broken links in opencode.md and factory.md, stale `notes.md` references replaced with `findings.md` across all 16 IDE copies, OpenCode support label corrected in README, `--help` in sync-ide-folders.py no longer runs a sync (PR #99)
  - Fixed Codex session-catchup silently scanning Claude session paths; now prints an explicit fallback message when running from Codex context (PR #100)
  - **Impact:** Significant docs and tooling consistency sweep across the entire multi-IDE surface

## Community Forks

These developers have created forks that extend the functionality:

- **[@RioTheGreat-ai](https://github.com/RioTheGreat-ai)** - [agentfund-skill](https://github.com/RioTheGreat-ai/agentfund-skill)
  - Crowdfunding platform for AI agents using milestone-based escrow on Base, built with planning-with-files

- **[@kmichels](https://github.com/kmichels)** - [multi-manus-planning](https://github.com/kmichels/multi-manus-planning)
  - Multi-project support
  - SessionStart git sync integration

## Issue Reporters & Testers

Thank you to everyone who reported issues, provided feedback, and helped test fixes:

- [@msuadOf](https://github.com/msuadOf) - Issue #93 (TMPDIR environment fix for plugin install)
- [@DorianZheng](https://github.com/DorianZheng) - Issue #84 (BoxLite sandbox integration proposal)
- [@mtuwei](https://github.com/mtuwei) - Issue #32 (Windows hook error)
- [@JianweiWangs](https://github.com/JianweiWangs) - Issue #31 (Skill activation)
- [@tingles2233](https://github.com/tingles2233) - Issue #29 (Plugin update issues)
- [@st01cs](https://github.com/st01cs) - Issue #28 (Devis fork discussion)
- [@wqh17101](https://github.com/wqh17101) - Issue #11 testing and confirmation

And many others who have starred, forked, and shared this project!

## How to Contribute

We welcome contributions! Here's how you can help:

1. **Report Issues** - Found a bug? Open an issue with details
2. **Suggest Features** - Have an idea? Share it in discussions
3. **Submit PRs** - Code improvements, documentation, examples
4. **Share** - Tell others about planning-with-files
5. **Create Forks** - Build on this work (with attribution)

See our [repository](https://github.com/OthmanAdi/planning-with-files) for more details.

## Recognition

If you've contributed and don't see your name here, please open an issue! We want to recognize everyone who helps make this project better.

---

**Total Contributors:** 27+ and growing!

*Last updated: March 24, 2026*

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
