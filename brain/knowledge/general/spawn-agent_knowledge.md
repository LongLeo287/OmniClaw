---
id: spawn-agent-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:16.002339
---

# KNOWLEDGE EXTRACT: spawn-agent
> **Extracted on:** 2026-03-30 13:16:38
> **Source:** spawn-agent

---

## File: `.gitignore`
```
# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo
*~

# spawn-agent outputs
/tmp/spawn-agent-*.log
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] - 2026-03-09

### Added

- `SKILL.md` — Skill definition with delegation protocol (DEFINE → COMPOSE → SPAWN → REVIEW → REPORT)
- `scripts/spawn-agent.sh` — Unified launcher for Gemini CLI and Codex CLI
- `templates/implementation-task.md` — Detailed template for complex implementation tasks
- `templates/research-task.md` — Template for read-only codebase research
- `templates/bugfix-task.md` — Minimal template for targeted bug fixes
- Agent comparison table (Gemini vs Codex strengths)
- Approval mode mapping (yolo / auto-edit / safe) per agent
- Anti-patterns guide
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

Thanks for your interest in improving **spawn-agent**! Here's how to contribute.

## Quick Start

1. Fork this repo
2. Create a branch: `git checkout -b my-feature`
3. Make your changes
4. Test: `./scripts/spawn-agent.sh --help` should run without errors
5. Commit with a clear message: `git commit -m "Add: new template for migration tasks"`
6. Push and open a Pull Request

## What We'd Love Help With

- **New templates** — Got a recurring task type? Add a template in `templates/`
- **Agent support** — Adding support for new CLI agents (Aider, Continue, etc.)
- **Documentation** — Better examples, clearer instructions, typo fixes
- **Bug reports** — If the script breaks on your setup, let us know

## Guidelines

- Keep `SKILL.md` as the single source of truth for the delegation protocol
- Templates should be self-contained — a worker agent reads only the filled template
- Shell script must stay POSIX-compatible where possible (bash 4+ is fine)
- Test on both macOS and Linux if you change `spawn-agent.sh`

## Commit Messages

Use clear prefixes:

```
Add: new template for database migration tasks
Fix: timeout detection on Linux systems
Docs: clarify installation steps for Cursor
Refactor: simplify approval mode mapping
```

## Questions?

Open an issue — we're happy to chat.
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Khanh Nguyen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
<div align="center">

# 🚀 spawn-agent

**A skill for [Antigravity](https://github.com/google-deepmind/antigravity) that delegates scoped work to worker agents, keeping the main context clean.**

Antigravity doesn't natively support spawning sub-agents. This skill fills that gap — use [Gemini CLI](https://github.com/google-gemini/gemini-cli) or [Codex CLI](https://github.com/openai/codex) as worker agents to handle implementation, research, and bug fixes while the orchestrator stays focused.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## The Problem

Antigravity is powerful, but it has no built-in way to delegate work to sub-agents. Every file read, build output, and error trace goes into the same context window — and it fills up fast. Once it does, the agent loses track of earlier instructions and can't reason about the big picture.

**Before spawn-agent:**
```
Main Agent Context:
├── User conversation          ~5%
├── Codebase understanding     ~10%
├── File A contents            ~15%  ← polluting
├── File B contents            ~15%  ← polluting
├── Build output               ~20%  ← polluting
├── Lint errors                ~10%  ← polluting
└── Remaining for reasoning    ~25%  ← squeezed
```

**After spawn-agent:**
```
Main Agent Context (Orchestrator):         Worker Agent Context:
├── User conversation     ~15%             ├── Task prompt          ~10%
├── Codebase overview     ~20%             ├── File A contents      ~25%
├── Delegation plan       ~10%             ├── File B contents      ~25%
├── Worker results        ~15%             ├── Build output         ~20%
└── Remaining reasoning   ~40%  ← clean   └── Implementation       ~20%
```

## How It Works

The main agent acts as an **orchestrator** — it plans, delegates, and reviews. Worker agents (Gemini or Codex) handle the actual implementation in isolated sessions.

```
Orchestrator                    Worker (Gemini/Codex)
     │                               │
     ├──── 1. DEFINE task ────────►   │
     ├──── 2. COMPOSE prompt ─────►   │
     ├──── 3. SPAWN ──────────────►   ├── reads codebase
     │                                ├── implements changes
     │                                ├── runs verification
     │     ◄── 4. OUTPUT ────────────┘
     ├──── 5. REVIEW results
     └──── 6. REPORT to user
```

## Installation

### Prerequisites

At least one of these CLI tools must be installed:

```bash
# Gemini CLI
npm install -g @google/gemini-cli

# Codex CLI
npm install -g @openai/codex
```

### Install the Skill

Clone into your Antigravity skills directory:

```bash
# Recommended: into your global skills directory
git clone https://github.com/khanhbkqt/spawn-agent.git ~/.gemini/antigravity/skills/spawn-agent

# Or per-project
git clone https://github.com/khanhbkqt/spawn-agent.git .agent/skills/spawn-agent

# Or symlink from a central location
git clone https://github.com/khanhbkqt/spawn-agent.git ~/spawn-agent
ln -s ~/spawn-agent ~/.gemini/antigravity/skills/spawn-agent
```

Make the script executable:

```bash
chmod +x ~/.gemini/antigravity/skills/spawn-agent/scripts/spawn-agent.sh
```

Antigravity will automatically discover the skill from `SKILL.md` and learn the delegation protocol.

## Quick Start

### 1. Simple inline task

```bash
./scripts/spawn-agent.sh --gemini --yolo -p "Count all TODO comments in src/ and list them"
```

### 2. Complex task with a template

Create a prompt file from a template:

```bash
cp templates/implementation-task.md /tmp/spawn-agent-task-auth.md
# Fill in the template sections...
```

Then spawn:

```bash
./scripts/spawn-agent.sh --codex --auto-edit --timeout 300 -f /tmp/spawn-agent-task-auth.md
```

### 3. Read-only research

```bash
./scripts/spawn-agent.sh --gemini --yolo --timeout 120 \
  -p "Analyze the authentication flow in packages/backend/src/auth/. 
      List all JWT-related functions and their dependencies.
      Output as a markdown summary. DO NOT modify any files."
```

## Choosing an Agent

| Agent | CLI | Strengths | Best for |
|-------|-----|-----------|----------|
| **Gemini** | `gemini` | Fast, good at codebase understanding, reads project context | Research, context gathering, quick implementations |
| **Codex** | `codex exec` | Strong reasoning, sandboxed execution, code review capability | Complex implementation, refactoring, bug fixing |

> **Tip:** Choose the agent based on the task — don't be loyal to one CLI. Each has its own strengths.

## Approval Modes

| Mode | Flag | Gemini | Codex |
|------|------|--------|-------|
| Auto-edit | `--auto-edit` | `auto_edit` | `auto-edit` |
| Full auto | `--yolo` | `yolo` | `full-auto` |
| Safest | `--safe` | `default` | `suggest` |

## Templates

Three prompt templates are provided for common task types:

| Task Type | Template | When to Use |
|-----------|----------|-------------|
| Implementation | [`implementation-task.md`](templates/implementation-task.md) | Adding features, building modules, refactoring |
| Research | [`research-task.md`](templates/research-task.md) | Codebase analysis, context gathering (read-only) |
| Bug Fix | [`bugfix-task.md`](templates/bugfix-task.md) | Targeted fixes with known or suspected location |

Each template includes sections for goal, scope, constraints, and expected output format. Fill in all sections before delegating — **headless workers can't ask clarifying questions**.

### Quick inline format (for simple tasks)

```markdown
# Task: <short name>
## Goal: <one sentence describing the objective>
## Files: <files to modify>
## Constraints: DO NOT modify files outside <scope>
## When done: Summarize changes made and any issues found.
```

## When to Use (and When Not To)

**Use spawn-agent when:**
- Implementation task has a clear scope (fix bug, add function, refactor file)
- You need to research/query the codebase without polluting the main context
- The task is independent and doesn't need intermediate human review
- You want to keep the main context clean for high-level reasoning

**Don't use when:**
- Task requires interactive discussion with the user
- Scope is too broad (refactoring an entire module)
- Multiple files with complex inter-dependencies need coordination
- Task needs browser interaction or external API calls

## Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|------|
| Delegate too broadly: "Refactor the entire backend" | Scope it: "Refactor auth.service.ts to extract token logic into token.service.ts" |
| Skip constraints — agent may modify files outside scope | Set boundaries: "DO NOT modify files outside packages/backend/src/auth/" |
| Spawn and assume success | Always review: read output, verify changes, check errors |
| Chain delegates: A → output feeds B → ... | Orchestrator controls flow: read result A, decide, then spawn B if needed |

## Script Reference

```
Usage: spawn-agent.sh [options]

Agent Selection:
  --gemini                Use Gemini CLI (default)
  --codex                 Use Codex CLI

Prompt:
  -p, --prompt TEXT       Prompt text (inline)
  -f, --file PATH         Prompt file (markdown)

Approval Modes:
  --yolo                  Auto-approve everything
  --auto-edit             Auto-approve edits only (default)
  --safe                  Prompt for every action

Other:
  --timeout SECONDS       Max execution time (default: 300)
  --output PATH           Custom output file path
  -h, --help              Show this help
```

## Compatibility

Built for **Antigravity** (Google DeepMind), but works with any AI coding assistant that reads `SKILL.md` files:

- **Antigravity** — `~/.gemini/antigravity/skills/` (primary target)
- **Claude Code** (Anthropic) — `.agent/skills/`
- **Gemini CLI** (Google) — `.gemini/skills/`
- **Cursor** — via rules or skills directories
- **Any agent** that supports Markdown-based skill definitions

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT](LICENSE)
```

## File: `SKILL.md`
```markdown
---
name: spawn-agent
description: Spawn worker agents (Gemini CLI or Codex CLI) to keep main context clean. Use for implementation, codebase research, context gathering, or any scoped work that would pollute the orchestrator's context.
---

# Spawn Agent

Orchestration & Delegation pattern: The main agent acts as the orchestrator (plan, delegate, review). Worker agents (Gemini/Codex) execute specific tasks and report results.

## When to Use

**Use when:**
- Implementation task has a clear scope (fix bug, add function, refactor file)
- You need to research/query the codebase without polluting the main context
- The task is independent and doesn't need intermediate human review
- You want to keep the main context clean for high-level reasoning

**Do NOT use when:**
- Task requires interactive discussion with the user
- Scope is too broad (refactoring an entire module)
- Multiple files with complex inter-dependencies need coordination
- Task needs browser interaction or external API calls

## Choosing an Agent

| Agent | CLI | Strengths | Best for |
|-------|-----|-----------|----------|
| **Gemini** | `gemini` | Fast, good at codebase understanding, reads project context | Research, context gathering, quick implementations |
| **Codex** | `codex exec` | Strong reasoning, sandboxed execution, code review capability | Complex implementation, refactoring, bug fixing |

> [!TIP]
> Choose the agent based on the task — don't stick to one CLI. Each has its own strengths.

## Delegation Protocol

### Step 1: DEFINE — Clearly define the task

Before spawning, the orchestrator must determine:
- **Goal**: What should the task achieve?
- **Scope**: Which files/directories are involved?
- **Agent**: Is Gemini or Codex more suitable?
- **Constraints**: What must NOT be modified?
- **Expected output**: What result is expected (code changes, summary, list)?

### Step 2: COMPOSE — Write the prompt file using a template

Choose the appropriate template and fill it in. Save to `.agent/spawn_agent_tasks/<name>.md`.

> [!NOTE]
> Create the directory if it doesn't exist: `mkdir -p .agent/spawn_agent_tasks`
> Add `.agent/spawn_agent_tasks/` to `.gitignore` if you don't want to track task files.

#### Template Selection Guide

| Task type | Template | Key sections |
|-----------|----------|-------------|
| **Complex implementation** | `templates/implementation-task.md` | Architecture context, File Map, Step-by-step, Conventions, Acceptance criteria |
| **Codebase research** | `templates/research-task.md` | Where to look, Questions to answer, Output format |
| **Bug fix** | `templates/bugfix-task.md` | Bug description, Suspected location, Fix approach |

> [!IMPORTANT]
> **Headless worker = no Q&A.** The worker agent cannot ask clarifying questions.
> The more detailed the template, the more accurate the output. Each missing section = one point where the agent may go wrong.

#### Quick inline prompt (for simple tasks)

```markdown
# Task: <short name>
## Goal: <one sentence describing the objective>
## Files: <files to modify>
## Constraints: DO NOT modify files outside <scope>
## When done: Summarize changes made and any issues found.
```

### Step 3: SPAWN — Call the worker agent

```bash
# Gemini — implementation task
spawn-agent.sh --gemini --auto-edit --timeout 300 \
  -f .agent/spawn_agent_tasks/<name>.md

# Codex — implementation task
spawn-agent.sh --codex --auto-edit --timeout 300 \
  -f .agent/spawn_agent_tasks/<name>.md

# Gemini — research (yolo is fine for read-only research)
spawn-agent.sh --gemini --yolo --timeout 120 \
  -f .agent/spawn_agent_tasks/<name>.md

# Quick task — any agent
spawn-agent.sh --codex --yolo --timeout 60 \
  -p "Fix typo 'recieve' -> 'receive' in auth.service.ts"
```

**Approval modes (mapped per agent):**

| Mode | Flag | Gemini | Codex |
|------|------|--------|-------|
| Auto-edit | `--auto-edit` | `auto_edit` | `auto-edit` |
| Full auto | `--yolo` | `yolo` | `full-auto` |
| Safest | `--safe` | `default` | `suggest` |

### Step 4: REVIEW — Read the output

Output is saved to `.agent/spawn_agent_tasks/output-<timestamp>.log`.

```bash
cat .agent/spawn_agent_tasks/output-*.log | tail -100
```

Verify:
- Did the task achieve the goal?
- Are there changes outside the defined scope?
- Are there errors/warnings that need handling?

### Step 5: REPORT — Summarize for the user

- ✅ Success: summarize changes
- ❌ Failure: root cause + next steps
- ⚠️ Partial: what was completed, what still needs to be done

## Anti-Patterns

❌ **Delegating too broadly**: "Refactor the entire backend"
✅ **Specific scope**: "Refactor auth.service.ts to extract token logic into token.service.ts"

❌ **No constraints**: Agent may modify files outside scope
✅ **Set boundaries**: "DO NOT modify files outside packages/backend/src/auth/"

❌ **Not reading output**: Spawning and assuming success
✅ **Always review**: Read output, verify changes, check errors

❌ **Delegation chain**: Spawn A → output feeds spawn B → ...
✅ **Orchestrator controls flow**: Read result A, decide next step, then spawn B if needed
```

## File: `system-prompt.md`
```markdown
# System Prompt — Orchestrator Mode

You are the **orchestrator**. You plan, delegate to workers, and review results.
Read skill `spawn-agent` (SKILL.md) for full protocol and templates.

## Role Split

- **You do**: planning, architectural decisions, complex multi-file work, user communication, reviewing worker output.
- **Workers do**: codebase research/grep/search, reading files for context, simple implementations, scoped bug fixes, boilerplate generation.

## When to Delegate vs Do It Yourself

**Delegate** when the task is:
- Scoped to clear files with clear goals (add function, fix bug, refactor one file)
- Information gathering (grep patterns, read files, summarize module structure)
- Mechanical / pattern-following (create similar file, rename, update imports)

**Do it yourself** when the task:
- Involves complex multi-file dependencies
- Requires architectural judgment or trade-off decisions
- Needs interactive user discussion or clarification
- Is too broad to define in one prompt ("refactor the whole module")
- Worker already failed — you need to course-correct

## Delegation Essentials

1. **Write self-contained prompts.** Worker starts with ZERO context. Include: goal, architecture context, file paths, conventions, constraints, verification commands.
2. **Save task prompts to `.agent/spawn_agent_tasks/<name>.md`** using the templates in the skill.
3. **Always set boundaries.** Specify which files to touch and which are OFF-LIMITS.
4. **Always review output.** Read `.agent/spawn_agent_tasks/output-*.log`. Never assume success.
5. **One task per spawn.** Review between each. Don't chain spawns blindly.

## Quick Commands

```bash
# Research (read-only)
spawn-agent.sh --gemini --yolo --timeout 120 -f .agent/spawn_agent_tasks/<name>.md

# Implementation
spawn-agent.sh --gemini --auto-edit --timeout 300 -f .agent/spawn_agent_tasks/<name>.md

# Quick one-liner
spawn-agent.sh --gemini --auto-edit --timeout 60 -p "Fix X in file Y"
```

## After Each Spawn

1. Read the output log
2. Verify: goal met? scope respected? build passes?
3. Report to user: ✅ success / ⚠️ partial / ❌ failed + next steps
```

## File: `scripts/spawn-agent.sh`
```bash
#!/usr/bin/env bash
# spawn-agent.sh — Spawn a worker agent (Gemini CLI or Codex CLI) in headless mode
#
# Usage:
#   spawn-agent.sh [options] -p "prompt text"
#   spawn-agent.sh [options] -f /path/to/prompt-file.md
#   echo "prompt" | spawn-agent.sh [options]
#
# See --help for all options.

set -euo pipefail

# ─── Defaults ───────────────────────────────────────────────
AGENT="gemini"            # gemini | codex
APPROVAL_MODE="auto_edit" # gemini: auto_edit|yolo|default  codex: (uses suggest/auto-edit/full-auto)
TIMEOUT=300
PROMPT=""
PROMPT_FILE=""
TASKS_DIR=".agent/spawn_agent_tasks"
OUTPUT_FILE="${TASKS_DIR}/output-$(date +%Y%m%d-%H%M%S).log"

# ─── Parse args ─────────────────────────────────────────────
usage() {
  cat <<EOF
Usage: $(basename "$0") [options]

Spawn a headless worker agent to execute a task.

Agent Selection:
  --gemini                Use Gemini CLI (default)
  --codex                 Use Codex CLI

Prompt:
  -p, --prompt TEXT       Prompt text (inline)
  -f, --file PATH         Prompt file (markdown)

Approval Modes:
  --yolo                  Auto-approve everything (gemini: yolo, codex: full-auto)
  --auto-edit             Auto-approve edits only (default for both)
  --safe                  Prompt for every action (gemini: default, codex: suggest)

Other:
  --timeout SECONDS       Max execution time (default: 300)
  --output PATH           Custom output file path
  -h, --help              Show this help

Examples:
  spawn-agent.sh --gemini --yolo -p "Fix typo in auth.ts"
  spawn-agent.sh --codex --auto-edit -f /tmp/task.md
  spawn-agent.sh --codex --yolo -p "Count files in src/"
EOF
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -p|--prompt)
      PROMPT="$2"; shift 2 ;;
    -f|--file)
      PROMPT_FILE="$2"; shift 2 ;;
    --gemini)
      AGENT="gemini"; shift ;;
    --codex)
      AGENT="codex"; shift ;;
    --yolo)
      APPROVAL_MODE="yolo"; shift ;;
    --auto-edit)
      APPROVAL_MODE="auto_edit"; shift ;;
    --safe)
      APPROVAL_MODE="safe"; shift ;;
    --timeout)
      TIMEOUT="$2"; shift 2 ;;
    --output)
      OUTPUT_FILE="$2"; shift 2 ;;
    -h|--help)
      usage ;;
    *)
      echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

# ─── Resolve prompt ─────────────────────────────────────────
if [[ -n "$PROMPT_FILE" ]]; then
  if [[ ! -f "$PROMPT_FILE" ]]; then
    echo "❌ Prompt file not found: $PROMPT_FILE" >&2
    exit 1
  fi
  PROMPT=$(cat "$PROMPT_FILE")
elif [[ -z "$PROMPT" ]]; then
  if [[ ! -t 0 ]]; then
    PROMPT=$(cat)
  else
    echo "❌ No prompt provided. Use -p, -f, or pipe input." >&2
    exit 1
  fi
fi

if [[ -z "$PROMPT" ]]; then
  echo "❌ Empty prompt." >&2
  exit 1
fi

# ─── Check agent availability ──────────────────────────────
if [[ "$AGENT" == "gemini" ]]; then
  if ! command -v gemini &>/dev/null; then
    echo "❌ gemini CLI not found. Install: npm i -g @google/gemini-cli" >&2
    exit 1
  fi
elif [[ "$AGENT" == "codex" ]]; then
  if ! command -v codex &>/dev/null; then
    echo "❌ codex CLI not found. Install: npm i -g @openai/codex" >&2
    exit 1
  fi
fi

# ─── Build command ──────────────────────────────────────────
build_gemini_cmd() {
  local mode
  case "$APPROVAL_MODE" in
    yolo)      mode="yolo" ;;
    auto_edit) mode="auto_edit" ;;
    safe)      mode="default" ;;
    *)         mode="auto_edit" ;;
  esac
  CMD=(gemini --approval-mode "$mode" -p "$PROMPT")
  MODE_DISPLAY="$mode"
}

build_codex_cmd() {
  local mode
  case "$APPROVAL_MODE" in
    yolo)      mode="full-auto" ;;
    auto_edit) mode="auto-edit" ;;
    safe)      mode="suggest" ;;
    *)         mode="auto-edit" ;;
  esac
  CMD=(codex exec -c "approval_mode=\"$mode\"" "$PROMPT")
  MODE_DISPLAY="$mode"
}

if [[ "$AGENT" == "gemini" ]]; then
  build_gemini_cmd
else
  build_codex_cmd
fi

# ─── Timeout command ────────────────────────────────────────
# macOS uses gtimeout (from coreutils), Linux uses timeout
if command -v gtimeout &>/dev/null; then
  TIMEOUT_CMD="gtimeout"
elif command -v timeout &>/dev/null; then
  TIMEOUT_CMD="timeout"
else
  TIMEOUT_CMD=""
fi

# ─── Ensure output directory exists ─────────────────────────
mkdir -p "$TASKS_DIR"

# ─── Execute ────────────────────────────────────────────────
AGENT_UPPER=$(echo "$AGENT" | tr '[:lower:]' '[:upper:]')

echo "╔══════════════════════════════════════════════════════╗"
echo "║  🚀 Spawning $AGENT_UPPER agent                          ║"
echo "╠══════════════════════════════════════════════════════╣"
echo "║  Agent:   $AGENT"
echo "║  Mode:    $MODE_DISPLAY"
echo "║  Timeout: ${TIMEOUT}s"
echo "║  Output:  $OUTPUT_FILE"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

EXIT_CODE=0

# Write header to output
{
  echo "=== Spawn Agent: $AGENT_UPPER ==="
  echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "Mode: $MODE_DISPLAY"
  echo "Prompt preview: ${PROMPT:0:200}..."
  echo "================================"
  echo ""
} | tee "$OUTPUT_FILE"

# Execute with optional timeout (capture exit code properly)
if [[ -n "$TIMEOUT_CMD" ]]; then
  $TIMEOUT_CMD "$TIMEOUT" "${CMD[@]}" 2>&1 | tee -a "$OUTPUT_FILE" || EXIT_CODE=$?
else
  "${CMD[@]}" 2>&1 | tee -a "$OUTPUT_FILE" || EXIT_CODE=$?
fi

# Write footer to output
{
  echo ""
  echo "================================"
  echo "Exit code: $EXIT_CODE"
  echo "Completed: $(date '+%Y-%m-%d %H:%M:%S')"
} | tee -a "$OUTPUT_FILE"

echo ""
if [[ $EXIT_CODE -eq 0 ]]; then
  echo "✅ $AGENT_UPPER agent completed successfully"
  echo "📄 Full output: $OUTPUT_FILE"
elif [[ $EXIT_CODE -eq 124 ]]; then
  echo "⏰ $AGENT_UPPER agent timed out after ${TIMEOUT}s"
  echo "📄 Partial output: $OUTPUT_FILE"
else
  echo "❌ $AGENT_UPPER agent failed (exit code: $EXIT_CODE)"
  echo "📄 Output with errors: $OUTPUT_FILE"
fi

exit $EXIT_CODE
```

## File: `templates/bugfix-task.md`
```markdown
# Bug Fix — Delegation Prompt Template

Use when delegating a specific bug fix. Shorter than the implementation template since the scope is smaller.

---

```markdown
# Fix: [SHORT BUG DESCRIPTION]

## 🐛 Bug Description
[Describe the bug clearly: current behavior vs expected]

- **Current behavior**: [X happens]
- **Expected behavior**: [Y should happen]
- **Reproduction**: [Steps or endpoint/input that triggers the bug]

## 📍 Suspected Location
- Primary: `path/to/file.ts` — [function/method name]
- Related: `path/to/related.ts` — [may be related]

## 🔧 Fix Approach (if known)
[If the orchestrator has already identified the root cause, describe the approach here]

- Root cause: [e.g., missing null check at line X]
- Fix: [e.g., Add guard clause before accessing property]

OR if root cause is unknown:
- Investigate the error by reading the relevant files
- Trace the execution flow from [entry point]
- Identify root cause and fix

## ✅ Verification

After fixing, verify:
1. [ ] Bug no longer reproduces
2. [ ] Build passes: `cd packages/backend && npm run build`
3. [ ] Existing tests still pass: `npm run test`
4. [ ] No regression in related functionality

## ⚠️ Constraints
- Fix ONLY the bug — do not refactor surrounding code
- Do not change API contracts
- Keep the fix minimal and targeted

## 📊 Report Format

### Root Cause
[1-2 sentences explaining why the bug occurred]

### Fix Applied
| File | Change |
|------|--------|
| `path` | What was fixed |

### Verification
- Build: ✅/❌
- Tests: ✅/❌
- Manual check: [describe]
```
```

## File: `templates/implementation-task.md`
```markdown
# Implementation Task — Delegation Prompt Template

Use this template when delegating complex tasks: adding features, implementing modules, refactoring.
The orchestrator must FILL all sections before delegating. Remove sections that don't apply.

---

```markdown
# Task: [SHORT TASK NAME]

## 🎯 Goal
[1-2 sentences describing the final objective. The agent must understand EXACTLY what to achieve.]

## 🏗️ Architecture Context
[Describe the relevant architecture — the agent has NO context about the codebase]

- **Project type**: [e.g., NestJS backend monorepo, Next.js frontend]
- **Module location**: [e.g., `packages/backend/src/notifications/`]
- **Key patterns used**:
  - [e.g., NestJS Modules + DI, TypeORM entities, class-validator DTOs]
  - [e.g., Event-driven via @OnEvent decorators]
  - [e.g., REST controllers return { data, meta } format]
- **Related modules** (for reference, DO NOT modify):
  - [e.g., `packages/backend/src/issues/` — similar CRUD pattern]
  - [e.g., `packages/backend/src/events/events.gateway.ts` — WebSocket]

## 📁 File Map

### Files to MODIFY (primary scope)
| File | What to change |
|------|---------------|
| `path/to/file.ts` | [Describe what specifically needs to change] |
| `path/to/file2.ts` | [Describe specifically] |

### Files to CREATE
| File | Purpose |
|------|---------|
| `path/to/new-file.ts` | [Describe the new file to create] |

### Files to READ (for context only — DO NOT modify)
| File | Why read |
|------|---------|
| `path/to/reference.ts` | [e.g., Follow same pattern for new implementation] |
| `path/to/types.ts` | [e.g., Import shared types from here] |

### 🚫 Off-limits (MUST NOT touch)
- `packages/frontend/` — frontend changes handled separately
- `*.spec.ts` — tests handled in a separate task
- [Any other boundaries]

## 📋 Step-by-Step Implementation

[Break down into clear steps. The agent follows each step in order.]

### Step 1: [Step name]
- Read `path/to/reference.ts` to understand the existing pattern
- Create `path/to/new-file.ts` following the same pattern
- [Specific details: class name, method name, signature]

### Step 2: [Step name]
- Modify `path/to/existing.ts`:
  - Add import for `NewModule` from step 1
  - Register `NewModule` in the `imports` array
- [Continue with details...]

### Step 3: [Step name]
- ...

## 🔧 Code Conventions

[Conventions the agent MUST follow — this is the most important section for quality]

- **Naming**: camelCase for variables, PascalCase for classes, UPPER_SNAKE for constants
- **Imports**: Use path aliases `@/` not relative `../../`
- **Error handling**: Throw framework-specific exceptions, not generic Error
- **DTOs**: Use class-validator decorators, extend from shared base if available
- **Entity**: ORM decorators, uuid primary key, timestamps via BaseEntity
- **Response format**: `{ data: T }` for single, `{ data: T[], meta: { total, page, limit } }` for lists
- [Add project-specific conventions]

## ✅ Acceptance Criteria

[Agent self-verifies before reporting completion]

1. [ ] [Criteria 1 — specific, testable]
2. [ ] [Criteria 2]
3. [ ] [Criteria 3]
4. [ ] Code compiles without errors (`npm run build` passes)
5. [ ] No lint errors (`npm run lint` passes)

## 🧪 Verification Commands

[Agent runs these commands after implementation]

```bash
# Build check
cd packages/backend && npm run build

# Lint check
cd packages/backend && npm run lint

# Run related tests (if applicable)
cd packages/backend && npm run test -- --grep "module-name"
```

## ⚠️ Constraints

- DO NOT modify files outside the scope defined in File Map
- DO NOT install new dependencies unless explicitly listed
- DO NOT change existing API contracts (request/response shapes)
- DO NOT add console.log — use the project's Logger
- Follow existing code patterns — do NOT introduce new patterns
- If something is unclear, make the SAFEST choice and note it in the report

## 📊 Report Format

When done, output this summary:

### Changes Made
| File | Action | Description |
|------|--------|-------------|
| `path` | Created/Modified | What changed |

### Verification Results
- Build: ✅/❌
- Lint: ✅/❌
- Tests: ✅/❌ (N passed, M failed)

### Decisions Made
- [Any ambiguous points where the agent had to make a choice]

### Potential Issues
- [Anything the orchestrator should review carefully]
```
```

## File: `templates/research-task.md`
```markdown
# Research / Context Gathering — Delegation Prompt Template

Use this template when delegating codebase research or context gathering.
The result is a summary for the orchestrator to use — no file changes.

---

```markdown
# Research: [TOPIC TO RESEARCH]

## 🎯 Goal
[Describe clearly what to investigate and what the OUTPUT will be used for]

Example: "Analyze the authentication flow to understand how JWT tokens are created,
refreshed, and revoked. Output will be used to plan a token rotation feature."

## 📁 Where to Look

### Primary directories
- `packages/backend/src/auth/` — start here
- `packages/backend/src/users/` — related module

### Key files to read
- `packages/backend/src/auth/auth.service.ts` — main logic
- `packages/backend/src/auth/strategies/` — Passport strategies

### Also check
- Database entities related to auth
- Any middleware or guards
- Config/environment variables related to auth

## 🔍 Questions to Answer

[List SPECIFIC questions that need answering]

1. How does X work?
2. What triggers Y?
3. Where is Z configured?
4. What are the dependencies between A and B?
5. Are there any edge cases or known issues?

## 📊 Output Format

Provide a concise summary using this structure:

### Overview
[2-3 sentences high-level]

### Key Findings
1. **[Topic 1]**: [finding]
2. **[Topic 2]**: [finding]
...

### File Reference
| File | Role |
|------|------|
| `path` | What it does |

### Architecture Diagram (if applicable)
[Text-based flow: A → B → C]

### Concerns / Gotchas
- [Anything the orchestrator should be aware of]

## ⚠️ Constraints
- This is READ-ONLY research — DO NOT modify any files
- Keep summary CONCISE — bullet points preferred
- Focus on FACTS from code, not assumptions
- If something is ambiguous, state both possibilities
```
```

