---
id: repo-fetched-claude-bootstrap-114457
type: knowledge
owner: OA
registered_at: 2026-04-05T04:13:41.970838
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_claude-bootstrap_114457

## Assimilation Report
Auto-cloned repository: FETCHED_claude-bootstrap_114457

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Claude Bootstrap

> An opinionated project initialization system for Claude Code. **Agent teams by default, strict TDD pipeline, multi-engine code review, security-first.**

**The bottleneck has moved from code generation to code comprehension.** AI can generate infinite code, but humans still need to review, understand, and maintain it. Claude Bootstrap provides guardrails that keep AI-generated code simple, secure, and verifiable.

**New in v3.3.1:** Mnemos two-layer post-compaction task restoration — guaranteed context recovery when Claude Code's compaction fires, crashes, or doesn't run. Typed memory graph (goals never evicted), 4-dimension fatigue monitoring, checkpoint/resume across sessions. iCPG intent-augmented code property graph — track why code exists, detect drift, prevent duplicate work.

## Core Philosophy

```
┌────────────────────────────────────────────────────────────────┐
│  TDD LOOPS VIA STOP HOOKS                                      │
│  ─────────────────────────────────────────────────────────────│
│  Stop hooks run tests after each Claude response.              │
│  Failures feed back automatically. Claude iterates until green.│
│  Real Claude Code infrastructure — no plugins needed.          │
├────────────────────────────────────────────────────────────────┤
│  TESTS FIRST, ALWAYS                                           │
│  ─────────────────────────────────────────────────────────────│
│  Features: Write tests → Watch them fail → Implement → Pass    │
│  Bugs: Find test gap → Write failing test → Fix → Pass         │
│  No code ships without a test that failed first.               │
├────────────────────────────────────────────────────────────────┤
│  SIMPLICITY IS THE GOAL                                        │
│  ─────────────────────────────────────────────────────────────│
│  20 lines per function │ 200 lines per file │ 3 params max     │
│  Enforced via .claude/rules/ with paths: frontmatter.          │
├────────────────────────────────────────────────────────────────┤
│  SECURITY BY DEFAULT                                           │
│  ─────────────────────────────────────────────────────────────│
│  No secrets in code │ Permission deny rules for .env files     │
│  Dependency scanning │ Pre-commit hooks │ CI enforcement       │
├────────────────────────────────────────────────────────────────┤
│  AGENT TEAMS BY DEFAULT                                        │
│  ─────────────────────────────────────────────────────────────│
│  Every project runs as a coordinated team of AI agents.        │
│  Agent definitions use proper frontmatter: tools, model,       │
│  maxTurns, effort, disallowedTools.                            │
├────────────────────────────────────────────────────────────────┤
│  CONDITIONAL RULES                                             │
│  ─────────────────────────────────────────────────────────────│
│  Rules in .claude/rules/ activate based on file paths.         │
│  React rules only load when editing .tsx files.                │
│  Python rules only load when editing .py files.                │
│  Saves tokens. Reduces noise. More targeted guidance.          │
└────────────────────────────────────────────────────────────────┘
```

## Quick Start

```bash
# Clone and install (clone anywhere you like)
git clone https://github.com/alinaqi/claude-bootstrap.git
cd claude-bootstrap && ./install.sh

# In any project directory
claude
> /initialize-project
```

Claude will:
1. **Validate tools** - Check gh, vercel, supabase CLIs
2. **Ask questions** - Language, framework, AI-first?, database, graph analysis level
3. **Set up repository** - Create or connect GitHub repo
4. **Create structure** - Skills, rules, settings, security, CI/CD, specs, todos
5. **Copy settings.json** - Pre-configured permissions and Stop hooks
6. **Generate CLAUDE.md** - With `@include` directives for modular skills
7. **Generate CLAUDE.local.md** - Template for private developer overrides
8. **Spawn agent team** - Deploy Team Lead + Quality + Security + Review + Merger + Feature agents

## How TDD Loops Work (Stop Hooks)

**No plugins. No fake commands.** Claude Code's Stop hook runs a script when Claude finishes a response. Exit code 2 feeds stderr back to Claude and continues the conversation.

```
┌─────────────────────────────────────────────────────────────┐
│  1. You say: "Add email validation to signup"               │
│  2. Claude writes tests + implementation                    │
│  3. Claude finishes response                                │
│  4. Stop hook runs: npm test && npm run lint                │
│  5a. All pass (exit 0) → Done!                              │
│  5b. Failures (exit 2) → stderr fed back to Claude          │
│  6. Claude sees failures, fixes, finishes again             │
│  7. Stop hook runs again → repeat until green               │
└─────────────────────────────────────────────────────────────┘
```

**Configuration** in `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "scripts/tdd-loop-check.sh",
        "timeout": 60,
        "statusMessage": "Running tests..."
      }]
    }]
  }
}
```

The `tdd-loop-check.sh` script runs tests, lint, and typecheck. It tracks iteration count (max 25) and distinguishes code errors (loop) from environment errors (stop).

## @include Directives

CLAUDE.md uses `@include` to modularly load skills:

```markdown
# CLAUDE.md
@.claude/skills/base/SKILL.md
@.claude/skills/iterative-development/SKILL.md
@.claude/skills/security/SKILL.md
```

These are **resolved at load time** by Claude Code — the content is recursively inlined (max depth 5, cycle detection built in). This means skills actually become part of the prompt instead of just being listed as text.

## Conditional Rules

Rules in `.claude/rules/` use YAML frontmatter with `paths:` to activate only when relevant files are being edited:

```yaml
# .claude/rules/react.md
---
paths: ["src/components/**", "**/*.tsx"]
---
Prefer functional components with hooks...
```

```yaml
# .claude/rules/python.md
---
paths: ["**/*.py"]
---
Use type hints, pytest, ruff...
```

**Included rules:**

| Rule | Activates When |
|------|----------------|
| `quality-gates.md` | Always (no paths: filter) |
| `tdd-workflow.md` | Always |
| `security.md` | Always |
| `react.md` | Editing .tsx/.jsx files |
| `typescript.md` | Editing .ts/.tsx files |
| `python.md` | Editing .py files |
| `nodejs-backend.md` | Editing api/routes/server files |

## Smarter Compaction (PreCompact Hook)

Claude Code's built-in compaction fires at ~83% context and summarizes everything into 20K tokens using a generic 9-section template. It doesn't know what YOUR project cares about.

The PreCompact hook fixes this by injecting **project-specific preservation priorities** into the summarizer:

```
┌─────────────────────────────────────────────────────────────┐
│  Built-in compaction:                                       │
│  "Summarize this conversation" → generic summary            │
├─────────────────────────────────────────────────────────────┤
│  With PreCompact hook:                                      │
│  "Summarize, but preserve ALL schema decisions verbatim,    │
│   keep exact error messages, keep API contract details,     │
│   reference these Key Decisions by name, and here's the     │
│   current git state to include" → project-aware summary     │
└─────────────────────────────────────────────────────────────┘
```

The hook auto-detects:
- **Project type** (TypeScript/Next.js, Python/FastAPI, Flutter, etc.)
- **Schema files** (Drizzle, Prisma, SQLAlchemy) → tells summarizer to preserve schema discussion
- **API directories** → tells summarizer to preserve endpoint paths and contracts
- **Key Decisions from CLAUDE.md** → tells summarizer to reference them by name
- **Git state** → injects branch, uncommitted changes, staged files

Zero overhead during normal usage. Only runs when compaction actually fires.

## Mnemos — Task-Scoped Memory Lifecycle

Claude Code's built-in compaction is lossy and unreliable. It sometimes doesn't fire, `/compact` and `/clear` can fail (especially in multi-agent executions), and crashes/restarts lose all context. Mnemos provides **disk-persistent structured state** that survives all of these failure modes.

```
┌─────────────────────────────────────────────────────────────┐
│  DEFAULT CLAUDE CODE          vs  WITH MNEMOS               │
├─────────────────────────────────────────────────────────────┤
│  Blind until 83.5%               Continuous 4-dim monitoring│
│  Sudden hard compaction           Graduated: 40→60→75→83%   │
│  Uniform summarization            Typed: goals never evict  │
│  No cross-session memory          Auto checkpoint/resume    │
│  Crash = total context loss       Crash = resume from disk  │
│  Multi-agent: no shared state     Per-agent structured state│
│  No behavioral awareness          Detects re-reads, scatter │
└─────────────────────────────────────────────────────────────┘
```

### Post-Compaction Task Restoration (Two-Layer Defense)

When compaction fires, the built-in summarizer often drops task-specific state. Mnemos uses two independent layers to guarantee restoration:

```
BEFORE COMPACTION                    AFTER COMPACTION

PreCompact hook fires                First tool call → PreToolUse fires
├── Write emergency checkpoint       ├── Detect ".mnemos/just-compacted" marker
├── Build task narrative from        ├── Read checkpoint-latest.json
│   signals.jsonl (files, tools)     ├── Output full checkpoint into context
├── Output STRONG preservation       ├── Delete marker (one-shot)
│   instructions to summarizer       └── Claude now has: summary + checkpoint
└── Write ".mnemos/just-compacted"
    marker file                      = Task fully restored
```

**Layer 1** (best-effort): PreCompact tells the summarizer what to keep, including inline checkpoint content with typed eviction priorities.

**Layer 2** (guaranteed): Post-compaction injection via PreToolUse re-injects the full checkpoint on the first tool call after compaction. Doesn't depend on the summarizer. Fast path ~5ms when no compaction occurred.

### Why Not Just Write to a Plain File?

You could — but you'd immediately face: what format? When to update? How to distinguish "this is critical" from "this is nice to have"? The MnemoGraph's typed nodes solve this:

| Node Type | Eviction Policy | Example |
|-----------|----------------|---------|
| GoalNode | NEVER evict | "Implement auth module" |
| ConstraintNode | NEVER evict | "API backward compatibility" |
| ResultNode | Compress first | "JWT middleware tested" → summary kept |
| WorkingNode | Compress first | Current reasoning / in-progress analysis |
| ContextNode | Evictable | File contents → re-read from disk |

Without typed priorities, a checkpoint is just a blob. With them, the system knows goals > constraints > working memory > context, and makes intelligent decisions about what to restore within token budgets.

### Resilience Beyond Normal Compaction

The real value isn't the happy path — it's when things go wrong:

| Failure Mode | CC Built-in | Mnemos |
|---|---|---|
| Session crash/collapse | Context gone | Checkpoint on disk survives |
| `/compact` doesn't fire | Truncation at limit | Fatigue hooks wrote checkpoints earlier |
| Multi-agent child dies | No recovery | Child's `.mnemos/` has structured state |
| Forced restart | Generic summary | SessionStart reloads full checkpoint |
| `/clear` fails in multi-agent | Stuck in weird state | MnemoGraph is independent of CC's state |

### Fatigue Model

4 dimensions passively observed from hooks — no agent cooperation needed:

| Dimension | Weight | Signal Source | Detects |
|-----------|--------|---------------|---------|
| Token utilization | 0.40 | Statusline JSON | How full the context window is |
| Scope scatter | 0.25 | PreToolUse file paths | Agent bouncing between directories |
| Re-read ratio | 0.20 | PreToolUse Read calls | Agent re-reading files (context loss) |
| Error density | 0.15 | PostToolUse outcomes | Agent struggling (high error rate) |

Fatigue states: **FLOW** (0-0.4) → **COMPRESS** (0.4-0.6) → **PRE-SLEEP** (0.6-0.75) → **REM** (0.75-0.9) → **EMERGENCY** (0.9+). The fatigue model ensures checkpoints are written *before* things go wrong — so when a crash happens at 0.85, you have a recent checkpoint from 0.6.

### CLI

```bash
mnemos init                    # Initialize .mnemos/
mnemos status                  # Node counts + fatigue
mnemos fatigue                 # Detailed 4-dimension breakdown
mnemos checkpoint --force      # Write checkpoint now
mnemos resume                  # Output checkpoint for session inject
mnemos add goal "Build auth"   # Create a GoalNode
mnemos bridge-icpg             # Import iCPG ReasonNodes
```

**Overhead:** ~5ms per tool call (fast path), 84KB on disk. Token signal auto-feeds via statusline.

## iCPG — Intent-Augmented Code Property Graph

iCPG tracks *why* code exists, not just what it does. Every code change is linked to a ReasonNode that captures the intent, postconditions, and invariants.

```bash
icpg create "Implement auth" --scope src/auth/   # Create intent
icpg record src/auth/middleware.ts                # Link symbols
icpg query constraints src/auth/middleware.ts     # Get invariants
icpg drift                                        # Check for drift
icpg bootstrap                                    # Infer from git history
```

**Pre-Task Queries** (injected automatically via PreToolUse hook):
- `icpg query context <file>` — What intents touch this file?
- `icpg query constraints <file>` — What invariants must hold?
- `icpg drift file <file>` — Has this file drifted from its intent?

**6-Dimension Drift Detection:** spec drift, decision drift, ownership drift, test drift, usage drift, dependency drift.

## Pre-configured Permissions

`.claude/settings.json` includes permission rules so users don't get pestered for routine operations:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test *)",
      "Bash(npm run lint *)",
      "Bash(pytest *)",
      "Bash(git status *)",
      "Bash(gh pr *)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)",
      "Write(.env)",
      "Write(.env.*)"
    ]
  }
}
```

## CLAUDE.local.md (Private Overrides)

Each developer gets a `.gitignore`'d `CLAUDE.local.md` for personal preferences:

```markdown
# My Preferences
- I prefer verbose explanations
- My local DB runs on port 5433
- Use pnpm instead of npm
```

This loads at **higher priority** than project `CLAUDE.md` — personal preferences override team config without polluting the repo.

## Agent Teams

Every project runs as a coordinated team of AI agents with **proper frontmatter definitions**:

```yaml
# .claude/agents/team-lead.md
---
name: team-lead
description: Orchestrates the agent team
mode
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to Claude Bootstrap will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [3.3.1] - 2026-04-03

### Added
- **Post-Compaction Task Restoration** (Two-Layer Defense)
  - `templates/mnemos-post-compact-inject.sh` — PreToolUse hook (no matcher, fires on ALL tools) that detects compaction via `.mnemos/just-compacted` marker and re-injects the full checkpoint into Claude's context. Fast path ~5ms when no compaction, ~100ms injection when triggered.
  - `build_task_narrative()` in `checkpoint.py` — Reads signals.jsonl to build human-readable summary of recent activity (files edited, read counts, focus area, error patterns). Automatically included in checkpoints.
  - `format_for_post_compact_injection()` in `checkpoint.py` — Formats checkpoint as structured restoration block with goal, constraints, activity narrative, progress, key files, git state.
  - Compaction marker system (`write_compaction_marker`, `check_compaction_marker`, `consume_compaction_marker`) — Atomic marker write/consume to prevent parallel injection.

### Changed
- **`mnemos-pre-compact.sh`** — Enhanced from advisory to assertive. Now includes inline checkpoint content in preservation instructions, writes compaction marker for Layer 2, builds task narrative from signals, and uses stronger verbatim framing.
- **`CheckpointNode`** — Added `task_narrative` (str) and `recent_files` (list[dict]) fields for richer checkpoint content.
- **`settings.json`** — Added new PreToolUse entry (no matcher) for `mnemos-post-compact-inject.sh` before the existing Edit|Write matcher.
- **`SKILL.md`** — Documented post-compaction recovery mechanism.
- **`README.md`** — Rewrote Mnemos section with two-layer defense architecture, resilience failure mode table, "why not just a plain file" rationale, and post-compaction restoration flow diagram.

## [3.3.0] - 2026-04-03

### Added

#### Mnemos — Task-Scoped Memory Lifecycle
Agents crash when context fills up. Claude Code's compaction is lossy — it summarizes everything uniformly. Mnemos solves this with typed memory, continuous fatigue monitoring, and checkpoint/resume.

- **`scripts/mnemos/`** — Python package (zero external dependencies)
  - `models.py` — MnemoNode (8 types with typed eviction policies), FatigueState, CheckpointNode
  - `store.py` — SQLite MnemoGraph storage with mnemo_nodes, checkpoints, fatigue_log tables
  - `fatigue.py` — 4-dimension fatigue model from passively observed signals (no agent cooperation needed)
  - `signals.py` — Behavioral signal collection from hooks (scope scatter, re-read ratio, error density)
  - `checkpoint.py` — CheckpointNode write/load with iCPG bridge, git state capture, formatted resume output
  - `consolidation.py` — Micro-consolidation: compress ResultNodes, evict cold ContextNodes, decay weights
  - `__main__.py` — CLI: init, status, fatigue, checkpoint, resume, consolidate, nodes, add, bridge-icpg

- **4-Dimension Fatigue Model** (all passively observed from hooks):
  - Token utilization (0.40) — real context_window.used_percentage from statusline
  - Scope scatter (0.25) — unique directories in recent tool calls (from PreToolUse)
  - Re-read ratio (0.20) — files Read more than once, strongest signal of context loss (from PreToolUse)
  - Error density (0.15) — failed tool calls ratio (from PostToolUse)
  - States: FLOW (0-0.4), COMPRESS (0.4-0.6), PRE-SLEEP (0.6-0.75), REM (0.75-0.9), EMERGENCY (0.9+)

- **Auto-Feeding Token Signal**:
  - `templates/mnemos-statusline.sh` — Statusline receives `context_window` JSON from Claude Code, writes `fatigue.json`, delegates display to ccusage (if installed) or shows simple context %
  - JSONL fallback in PostToolUse — reads conversation JSONL to estimate context usage when statusline not configured (0.75 correction factor for cache overhead, ~1-2pp accuracy)
  - `statusLine` config added to `templates/settings.json` — auto-activates on install, no separate configuration needed

- **Fatigue-Aware Hook System**:
  - `templates/mnemos-pre-edit.sh` — PreToolUse: logs file signals, reads fatigue, auto-checkpoints at 0.60+, auto-consolidates at 0.40+, includes iCPG context
  - `templates/mnemos-post-tool.sh` — PostToolUse: logs tool success/failure for error density, auto-feeds token signal from JSONL when statusline is stale
  - `templates/mnemos-session-start.sh` — SessionStart: loads checkpoint on resume, bridges iCPG state
  - `templates/mnemos-pre-compact.sh` — PreCompact: emergency checkpoint + typed preservation priorities (NEVER DROP goals/constraints, OK TO DROP file contents)
  - `templates/mnemos-stop-checkpoint.sh` — Stop: writes final session checkpoint

- **MnemoNode Eviction Policies**:
  - GoalNodes, ConstraintNodes, CheckpointNodes, HandoffNodes: NEVER evicted
  - ResultNodes, WorkingNodes, SkillNodes: compressed first (summary kept), then evictable
  - ContextNodes: evictable when activation weight drops below threshold

- **iCPG Bridge**: `mnemos bridge-icpg` imports ReasonNodes as GoalNodes, postconditions/invariants as ConstraintNodes

- **Skill + Commands**:
  - `skills/mnemos/SKILL.md` — Full skill documentation with fatigue states, CLI reference, agent instructions
  - `commands/mnemos-status.md` — `/mnemos-status` slash command
  - `commands/mnemos-checkpoint.md` — `/mnemos-checkpoint` slash command

- **Documentation**:
  - `docs/mnemos-implementation.md` — Implementation addendum for the Mnemos RFC

### Changed

#### iCPG Fixes
- `scripts/icpg/bootstrap.py` — Fixed `_get_commits()` git log parsing (was producing 0 symbols linked)
- `scripts/icpg/drift.py` — Added `check_file_drift()` for fast, file-scoped drift (O(symbols-in-file))
- `scripts/icpg/__main__.py` — Added `drift file <path>` subcommand, `_resolve_path()` for relative path handling
- `templates/icpg-pre-edit.sh` — Now includes file-scoped drift detection alongside context and constraints

#### Settings Template
- `templates/settings.json` — Added `statusLine` config for auto-feeding token signal, Mnemos hooks replace standalone iCPG hooks, added PostToolUse hook, added mnemos permission allows
- `templates/CLAUDE.md` — Added `@.claude/skills/mnemos/SKILL.md` to skill includes

---

## [3.2.0] - 2026-04-02

### Added

#### iCPG Full Implementation (Intent-Augmented Code Property Graph)
- **`scripts/icpg/`** — Python CLI package implementing the full iCPG RFC v8
  - `models.py` — ReasonNode, Symbol, Edge, DriftEvent data models with Design by Contract (preconditions, postconditions, invariants)
  - `store.py` — SQLite storage layer with 4 tables, WAL mode, indexed queries
  - `symbols.py` — Language-aware symbol extraction: Python (AST), TypeScript/JS (regex), Go, Rust, Elixir
  - `drift.py` — 6-dimension drift detection: spec, decision, ownership, test, usage, dependency
  - `contracts.py` — Design by Contract layer with LLM inference (Claude/OpenAI) and heuristic fallback
  - `vectors.py` — Tiered duplicate detection: ChromaDB → TF-IDF → exact match fallback
  - `bootstrap.py` — Git history inference: cluster commits, LLM-infer ReasonNodes, link symbols
  - `__main__.py` — CLI with subcommands: init, create, record, query, drift, bootstrap, status
  - `pyproject.toml` — pip-installable with optional deps (chromadb, sentence-transformers, openai)

- **3 Canonical Pre-Task Queries** (RFC Section 2.1):
  - `icpg query prior "<goal>"` — Vector-based duplicate detection before starting work
  - `icpg query constraints <file>` — Get invariants/contracts for files being modified
  - `icpg query risk <symbol>` — Drift score, ownership history, modification count

- **Hook Integration**:
  - `templates/icpg-pre-edit.sh` — PreToolUse hook: injects intent context + constraints before every Edit/Write
  - `templates/icpg-stop-record.sh` — Stop hook: auto-records symbols to active ReasonNode after implementation

- **Slash Commands**:
  - `commands/icpg-impact.md` — `/icpg-impact <id>` blast radius visualization
  - `commands/icpg-why.md` — `/icpg-why <symbol>` trace symbol to creating intent
  - `commands/icpg-drift.md` — `/icpg-drift` full drift report across all dimensions
  - `commands/icpg-bootstrap.md` — `/icpg-bootstrap` infer intents from git history

### Changed

#### iCPG Skill Rewrite
- **`skills/icpg/SKILL.md`** — Complete rewrite aligning with RFC v8
  - ReasonNode now carries formal contracts (preconditions, postconditions, invariants)
  - Drift formally defined as predicate failure (not vague metric)
  - 6-dimension drift model with 0-1 severity scores per dimension
  - CLI reference for all `icpg` subcommands
  - Hook integration documentation (PreToolUse + Stop)
  - Agent Teams integration section with updated pipeline

#### Agent Team iCPG Integration
- **`skills/agent-teams/agents/team-lead.md`** — Team lead now creates ReasonNodes and checks for duplicates before creating task chains
- **`skills/agent-teams/agents/feature.md`** — Feature agents query constraints/risk before implementing, auto-record symbols after
- **`skills/agent-teams/agents/quality.md`** — Quality agent runs drift checks during GREEN verify, validates spec-intent alignment
- **`skills/agent-teams/SKILL.md`** — Updated "Integration with Existing Skills" table with iCPG + code-graph entries

#### Settings Template
- **`templates/settings.json`** — Added PreToolUse hook (icpg-pre-edit.sh), Stop hook extension (icpg-stop-record.sh), icpg permission allows

---

## [3.1.0] - 2026-04-02

### Added

#### iCPG Skill (Initial Spec)
- **`skills/icpg/SKILL.md`** — Initial iCPG skill spec (now superseded by 3.2.0 full implementation)

---

## [3.0.0] - 2026-03-31

### Breaking Changes

This release aligns Claude Bootstrap with how Claude Code actually works internally. Several features that referenced non-existent infrastructure have been replaced with real Claude Code mechanisms.

- **Ralph Wiggum plugin removed** — The `/ralph-loop` command, `claude-plugins-official` marketplace, and plugin stop-hook mechanism never existed in Claude Code. All references removed.
- **TDD loops now use real Stop hooks** — Claude Code's Stop hook (exit code 2 feeds stderr back to the model) replaces the fake plugin. `scripts/tdd-loop-check.sh` runs tests/lint/typecheck after each response.
- **`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` removed** — Agent spawning and task management are standard Claude Code features, not gated behind an env var. All references removed.
- **CLAUDE.md template uses `@include` directives** — Skills are loaded via `@.claude/skills/base/SKILL.md` syntax which Claude Code resolves at parse time (recursive, max depth 5, cycle detection).
- **Quality gates moved from CLAUDE.md to `.claude/rules/`** — Rules use YAML frontmatter with `paths:` globs for conditional activation.
- **"STRICTLY ENFORCED" / "Non-Negotiable" language removed** — Claude Code treats CLAUDE.md as user-level context (not system prompt) wrapped in `<system-reminder>` tags with "may or may not be relevant" caveat. Aggressive language wastes tokens without creating binding constraints.

### Added

#### Stop Hook TDD Loops
- **`templates/tdd-loop-check.sh`** — Universal TDD loop script for Stop hooks
  - Runs tests, lint, typecheck after each Claude response
  - Exit 0 (all pass) = Claude stops; Exit 2 (failures) = stderr fed back to Claude
  - Iteration counter with configurable max (default 25)
  - Detects project type (Node.js/Python) and runs appropriate commands
  - Distinguishes code errors (loop) from environment errors (stop)

- **`templates/settings.json`** — Pre-configured Claude Code settings
  - Stop hook configuration for TDD loops
  - SessionStart hook for auto-context injection
  - Permission allow rules: test runners, linters, git read commands, gh CLI
  - Permission deny rules: `rm -rf`, `git push --force`, writing `.env` files
  - Ready to copy into any project's `.claude/settings.json`

#### Conditional Rules System
- **`.claude/rules/` directory** with 7 rule files using proper YAML frontmatter:
  - `quality-gates.md` — Always active: 20 lines/function, 200 lines/file, 3 params, 80% coverage
  - `tdd-workflow.md` — Always active: RED-GREEN-VALIDATE workflow
  - `security.md` — Always active: no secrets in code, parameterized queries, bcrypt
  - `react.md` — Active on `**/*.tsx`, `**/*.jsx`, `src/components/**`
  - `typescript.md` — Active on `**/*.ts`, `**/*.tsx`
  - `python.md` — Active on `**/*.py`
  - `nodejs-backend.md` — Active on `src/api/**`, `src/routes/**`, `server/**`

#### CLAUDE.local.md
- **`templates/CLAUDE.local.md`** — Private developer override template
  - Not checked into git (higher priority than project CLAUDE.md)
  - Template with common overrides: preferences, local environment, quality gate tweaks

#### Agent Definition Frontmatter
- All 6 agent definitions now use proper Claude Code frontmatter:
  - `name` — Agent identifier
  - `description` — When-to-use hint
  - `model` — Model selection (sonnet, inherit)
  - `tools` — Tool allowlist (e.g., `[Read, Glob, Grep, TaskCreate]`)
  - `disallowedTools` — Tool denylist (e.g., `[Write, Edit, Bash]`)
  - `maxTurns` — Maximum agentic turns before stopping
  - `effort` — Thinking depth (medium/high)

#### @include Directives in CLAUDE.md
- CLAUDE.md template now uses `@.claude/skills/base/SKILL.md` syntax
- Claude Code resolves these at load time (recursively inlined)
- Skills actually become part of the prompt instead of decorative text

#### CLAUDE.md Template Structure
- Added **Project Structure** section — tells Claude where things live without filesystem exploration
- Added **Key Decisions** section — prevents Claude from re-litigating settled architectural choices
- Added **Conventions** section — patterns Claude should follow (test colocation, API shape, etc.)
- Added **Don't** section — short guardrails (no .env writes, no secret leaks)
- Removed Session Persistence section (belongs in skills, not root template)

#### PreCompact Hook for Smarter Compaction
- **`templates/pre-compact.sh`** — PreCompact hook that injects project-specific preservation priorities into the compaction summarizer
  - Auto-detects project type (TypeScript, Python, Next.js, FastAPI, Flutter, etc.)
  - Finds schema files (Drizzle, Prisma, SQLAlchemy) and tells summarizer to preserve all schema discussion verbatim
  - Finds API directories and tells summarizer to preserve exact endpoint paths, request/response shapes
  - Extracts Key Decisions from CLAUDE.md and tells summarizer to reference them by name
  - Injects live git state (branch, uncommitted changes, staged files) into summary priorities
  - Tells summarizer to preserve exact error messages and fix context (not paraphrased)
  - Tells summarizer what NOT to preserve (dead ends, full file contents, formatting noise)
  - Zero overhead during normal usage — only runs when compaction fires
  - Configured in `.claude/settings.json` under `hooks.PreCompact`

#### Full Skill Frontmatter (all
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to Claude Bootstrap

Thanks for your interest in contributing! This project aims to make AI-assisted development more reliable and consistent.

## Philosophy

Before contributing, understand the core philosophy:

1. **Complexity is the enemy** - Every line of code is a liability
2. **Measurable constraints** - Prefer specific numbers (20 lines/fn) over vague guidance
3. **Security is non-negotiable** - All projects must pass security checks
4. **AI-first thinking** - LLMs for logic, code for plumbing
5. **Spec-driven** - Define before you build

## How to Contribute

### Adding a New Skill

1. Create a new file in `skills/` following the naming pattern: `[topic].md`
2. Start with the header and dependency line:
   ```markdown
   # [Topic] Skill

   *Load with: base.md + [other dependencies]*
   ```
3. Include these sections:
   - Core principles
   - Project structure (if applicable)
   - Patterns with code examples
   - Anti-patterns list
4. Add measurable constraints where possible
5. Update `README.md` to include the new skill

### Improving Existing Skills

1. Keep changes focused on one improvement
2. Maintain the existing structure
3. Ensure examples are correct and tested
4. Update version comments if significant

### Updating the Initialize Command

1. Test changes locally before submitting
2. Ensure idempotency - running twice shouldn't break anything
3. Preserve user customizations (never overwrite `_project_specs/`)

## Skill Guidelines

### Do

- Use specific, measurable constraints
- Provide working code examples
- Include anti-patterns with explanations
- Keep skills focused on one topic
- Reference other skills when building on them

### Don't

- Use vague guidance ("write clean code")
- Include time estimates
- Add features beyond what's needed
- Break existing projects when run as update

## Testing Your Changes

```bash
# Install your changes
./install.sh

# Test on a new project
mkdir test-project && cd test-project
claude
> /initialize-project

# Test on an existing project
cd existing-project
claude
> /initialize-project
# Should update skills without breaking existing config
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Make your changes
4. Test locally
5. Submit PR with clear description of changes

## Code of Conduct

- Be respectful and constructive
- Focus on technical merit
- Welcome newcomers
- Share knowledge freely

## Questions?

Open an issue for:
- Bug reports
- Feature requests
- Clarification on philosophy
- Help with implementation

```

### File: install.sh
```sh
#!/bin/bash

# Claude Bootstrap Installer

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$HOME/.claude"

echo "Installing Claude Bootstrap v3.0.0..."
echo ""

# Save bootstrap directory location for other scripts
echo "$SCRIPT_DIR" > "$HOME/.claude/.bootstrap-dir"

# Create directories
mkdir -p "$CLAUDE_DIR/commands"
mkdir -p "$CLAUDE_DIR/skills"
mkdir -p "$CLAUDE_DIR/hooks"
mkdir -p "$CLAUDE_DIR/rules"

# Copy all commands
cp "$SCRIPT_DIR/commands/"*.md "$CLAUDE_DIR/commands/"
echo "✓ Installed commands:"
ls -1 "$CLAUDE_DIR/commands/" | sed 's/^/  - \//' | sed 's/\.md$//'

# Copy skills (folder structure with SKILL.md)
echo ""
echo "Installing skills..."
rm -rf "$CLAUDE_DIR/skills"
mkdir -p "$CLAUDE_DIR/skills"
skill_count=0
for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    if [ -d "$skill_dir" ] && [ -f "$skill_dir/SKILL.md" ]; then
        skill_name=$(basename "$skill_dir")
        cp -r "${skill_dir%/}" "$CLAUDE_DIR/skills/"
        skill_count=$((skill_count + 1))
    fi
done
echo "✓ Installed $skill_count skills (folder/SKILL.md structure)"

# Copy conditional rules
echo ""
echo "Installing conditional rules..."
rm -rf "$CLAUDE_DIR/rules"
mkdir -p "$CLAUDE_DIR/rules"
rule_count=0
for rule_file in "$SCRIPT_DIR/rules/"*.md; do
    if [ -f "$rule_file" ]; then
        cp "$rule_file" "$CLAUDE_DIR/rules/"
        rule_count=$((rule_count + 1))
    fi
done
echo "✓ Installed $rule_count conditional rules (with paths: frontmatter)"
ls -1 "$CLAUDE_DIR/rules/" | sed 's/^/  - /' | sed 's/\.md$//'

# Copy hooks
cp "$SCRIPT_DIR/hooks/"* "$CLAUDE_DIR/hooks/" 2>/dev/null || true
chmod +x "$CLAUDE_DIR/hooks/"* 2>/dev/null || true
echo ""
echo "✓ Installed git hooks (templates)"

# Copy templates
echo ""
echo "Installing templates..."
mkdir -p "$CLAUDE_DIR/templates"
cp "$SCRIPT_DIR/templates/"* "$CLAUDE_DIR/templates/" 2>/dev/null || true
chmod +x "$CLAUDE_DIR/templates/tdd-loop-check.sh" 2>/dev/null || true
chmod +x "$CLAUDE_DIR/templates/pre-compact.sh" 2>/dev/null || true
echo "✓ Installed templates (CLAUDE.md, CLAUDE.local.md, settings.json, tdd-loop-check.sh, pre-compact.sh)"

# Copy hook installer script
cp "$SCRIPT_DIR/scripts/install-hooks.sh" "$CLAUDE_DIR/" 2>/dev/null || true
chmod +x "$CLAUDE_DIR/install-hooks.sh" 2>/dev/null || true

# Copy graph tools installer
cp "$SCRIPT_DIR/scripts/install-graph-tools.sh" "$CLAUDE_DIR/" 2>/dev/null || true
chmod +x "$CLAUDE_DIR/install-graph-tools.sh" 2>/dev/null || true

# Run validation
echo ""
echo "Running validation..."
if [ -f "$SCRIPT_DIR/tests/validate-structure.sh" ]; then
    if "$SCRIPT_DIR/tests/validate-structure.sh" --quick; then
        echo ""
    else
        echo ""
        echo "⚠ Validation found issues. Run full validation:"
        echo "  $SCRIPT_DIR/tests/validate-structure.sh --full"
    fi
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "  Installation complete! (v3.0.0)"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "What's new in v3.0.0:"
echo "  • Stop hooks for TDD loops (replaces Ralph Wiggum plugin)"
echo "  • @include directives in CLAUDE.md"
echo "  • Conditional rules with paths: frontmatter"
echo "  • Pre-configured permissions in settings.json"
echo "  • Agent definitions with proper frontmatter"
echo "  • CLAUDE.local.md for private overrides"
echo ""
echo "Usage:"
echo "  1. Open any project folder"
echo "  2. Run: claude"
echo "  3. Type: /initialize-project"
echo ""
echo "Commands installed:"
echo "  /initialize-project   - Full project setup"
echo "  /spawn-team           - Spawn agent team for parallel development"
echo "  /check-contributors   - Team coordination"
echo "  /update-code-index    - Regenerate code index"
echo ""
echo "New in this version:"
echo "  Conditional rules:  ~/.claude/rules/ (auto-activate by file path)"
echo "  Settings template:  ~/.claude/templates/settings.json"
echo "  TDD loop script:    ~/.claude/templates/tdd-loop-check.sh"
echo "  Local overrides:    ~/.claude/templates/CLAUDE.local.md"
echo ""
echo "Git Hooks (per-project):"
echo "  cd your-project && ~/.claude/install-hooks.sh"
echo ""
echo "Code Graph Tools:"
echo "  ~/.claude/install-graph-tools.sh            - Install Tier 1 (default)"
echo "  ~/.claude/install-graph-tools.sh --joern     - Also install Tier 2 (CPG)"
echo "  ~/.claude/install-graph-tools.sh --codeql    - Also install Tier 3 (security)"
echo "  ~/.claude/install-graph-tools.sh --all       - Install all tiers"
echo ""
echo "Validation:"
echo "  $SCRIPT_DIR/tests/validate-structure.sh --full"
echo ""

```

### File: commands\analyze-repo.md
```md
# Analyze Repository

Analyze an existing repository's structure, conventions, and guardrails.

**This command runs automatically** when `/initialize-project` detects an existing codebase without Claude setup. You can also run it standalone anytime.

**Use this command standalone when:**
- You want to re-analyze after making changes
- You want analysis without running `/initialize-project`
- Auditing code quality and guardrails on any repo
- Reviewing a codebase without adding Claude skills

**Automatic trigger:**
- `/initialize-project` on existing codebase → auto-runs this analysis first

---

## Phase 1: Repository Detection

Run these checks to understand the repo:

```bash
# Git info
echo "=== Git Status ===" && \
git remote -v 2>/dev/null && \
git branch -a 2>/dev/null | head -10 && \
git log --oneline -5 2>/dev/null

# Config files
echo "=== Config Files ===" && \
ls -la *.json *.toml *.yaml *.yml 2>/dev/null

# Directory structure (3 levels, excluding noise)
echo "=== Directory Structure ===" && \
find . -type d -maxdepth 3 \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    -not -path "*/venv/*" \
    -not -path "*/__pycache__/*" \
    -not -path "*/dist/*" \
    -not -path "*/build/*" \
    2>/dev/null | head -40
```

---

## Phase 2: Tech Stack Detection

Identify the primary technologies:

```bash
# JavaScript/TypeScript
if [ -f "package.json" ]; then
    echo "=== Package.json ===" && \
    cat package.json | head -50
fi

# Python
if [ -f "pyproject.toml" ]; then
    echo "=== pyproject.toml ===" && \
    cat pyproject.toml
fi

# Mobile
ls pubspec.yaml android/build.gradle ios/*.xcodeproj 2>/dev/null
```

Based on findings, determine:

| File | Technology |
|------|------------|
| package.json + tsconfig.json | TypeScript |
| package.json (no tsconfig) | JavaScript |
| pyproject.toml | Python |
| pubspec.yaml | Flutter (Dart) |
| android/build.gradle | Android Native |
| Cargo.toml | Rust |
| go.mod | Go |

---

## Phase 3: Repo Structure Type

Classify the repository:

```bash
# Check structure type
echo "=== Repo Structure Type ===" && \
if [ -d "packages" ] || [ -d "apps" ] || grep -q '"workspaces"' package.json 2>/dev/null; then
    echo "MONOREPO - Multiple packages/apps with shared tooling"
elif [ -d "frontend" ] && [ -d "backend" ]; then
    echo "FULL-STACK MONOLITH - Frontend + Backend in same repo"
elif [ -d "src" ] && grep -q '"react\|vue\|angular"' package.json 2>/dev/null; then
    echo "FRONTEND - Single frontend application"
elif [ -d "src" ] && grep -q '"express\|fastify\|koa"' package.json 2>/dev/null; then
    echo "BACKEND - Single backend application"
elif [ -f "pyproject.toml" ] && grep -q "fastapi\|django\|flask" pyproject.toml 2>/dev/null; then
    echo "BACKEND (Python) - Single backend application"
else
    echo "STANDARD - Single-purpose repository"
fi
```

---

## Phase 4: Guardrails Audit

Check existing code quality tools:

```bash
echo "=== Guardrails Audit ===" && \

# Pre-commit hooks
echo "Pre-commit Hooks:" && \
[ -d ".husky" ] && echo "  [x] Husky installed" || echo "  [ ] Husky NOT installed" && \
[ -f ".pre-commit-config.yaml" ] && echo "  [x] pre-commit framework" || echo "  [ ] pre-commit framework NOT installed" && \
[ -f ".git/hooks/pre-commit" ] && echo "  [x] Git hooks present" || echo "  [ ] No git hooks"

# Linting
echo "Linting:" && \
(grep -q '"eslint"' package.json 2>/dev/null && echo "  [x] ESLint") || \
(grep -q '"biome"' package.json 2>/dev/null && echo "  [x] Biome") || \
(grep -q "ruff" pyproject.toml 2>/dev/null && echo "  [x] Ruff") || \
echo "  [ ] No linter detected"

# Formatting
echo "Formatting:" && \
(grep -q '"prettier"' package.json 2>/dev/null && echo "  [x] Prettier") || \
(grep -q "black" pyproject.toml 2>/dev/null && echo "  [x] Black") || \
(grep -q "ruff" pyproject.toml 2>/dev/null && echo "  [x] Ruff (formatting)") || \
echo "  [ ] No formatter detected"

# Type checking
echo "Type Checking:" && \
([ -f "tsconfig.json" ] && echo "  [x] TypeScript") || \
(grep -q "mypy" pyproject.toml 2>/dev/null && echo "  [x] mypy") || \
(grep -q "pyright" pyproject.toml 2>/dev/null && echo "  [x] pyright") || \
echo "  [ ] No type checker detected"

# Testing
echo "Testing:" && \
(grep -q '"jest\|vitest"' package.json 2>/dev/null && echo "  [x] Jest/Vitest") || \
(grep -q "pytest" pyproject.toml 2>/dev/null && echo "  [x] pytest") || \
echo "  [ ] No test framework detected"

# Commit validation
echo "Commit Validation:" && \
([ -f "commitlint.config.js" ] && echo "  [x] commitlint") || \
(grep -q "conventional-pre-commit" .pre-commit-config.yaml 2>/dev/null && echo "  [x] conventional-pre-commit") || \
echo "  [ ] No commit validation"

# CI/CD
echo "CI/CD:" && \
[ -d ".github/workflows" ] && echo "  [x] GitHub Actions" || echo "  [ ] No GitHub Actions" && \
[ -f ".gitlab-ci.yml" ] && echo "  [x] GitLab CI" || true && \
[ -f "Jenkinsfile" ] && echo "  [x] Jenkins" || true
```

---

## Phase 5: Convention Detection

Identify existing code patterns:

```bash
echo "=== Convention Detection ===" && \

# File naming
echo "File Naming:" && \
ls src/**/*.ts 2>/dev/null | head -5 && \
ls src/**/*.py 2>/dev/null | head -5

# Import style (JS/TS)
echo "Import Style:" && \
grep -h "^import" src/**/*.ts 2>/dev/null | head -5

# Export style (JS/TS)
echo "Export Style:" && \
grep -h "^export" src/**/*.ts 2>/dev/null | head -5

# Test file location
echo "Test Location:" && \
find . -name "*.test.*" -o -name "*.spec.*" -o -name "test_*.py" 2>/dev/null | head -5
```

---

## Phase 6: Generate Report

Based on all findings, generate this report structure:

```markdown
# Repository Analysis Report

**Generated:** [timestamp]
**Repository:** [name from git remote or directory]

## Overview

| Attribute | Value |
|-----------|-------|
| Type | [Monorepo / Full-Stack / Frontend / Backend] |
| Language | [TypeScript / Python / ...] |
| Framework | [React / FastAPI / ...] |
| Package Manager | [npm / pnpm / uv / pip] |

## Directory Structure

[Simplified tree output]

## Tech Stack

| Category | Technology | Config |
|----------|------------|--------|
| Language | X | X |
| Framework | X | X |
| Testing | X | X |
| Linting | X | X |
| Formatting | X | X |

## Guardrails Status

### Present
- [x] Item 1
- [x] Item 2

### Missing (Recommended to Add)
- [ ] Item 1 - [brief reason]
- [ ] Item 2 - [brief reason]

## Conventions Observed

| Pattern | Observed Value | Example |
|---------|----------------|---------|
| Naming | camelCase / snake_case | file.ts |
| Imports | Absolute / Relative | @/components |
| Tests | Colocated / Separate | *.test.ts |
| Exports | Named / Default | export { X } |

## Recommendations

1. **High Priority**
   - [Recommendation with reason]

2. **Medium Priority**
   - [Recommendation with reason]

3. **Low Priority / Nice to Have**
   - [Recommendation with reason]

## Key Files to Review

| File | Purpose | Why Review |
|------|---------|------------|
| src/index.ts | Entry point | Understand app bootstrap |
| src/config.ts | Configuration | Understand env handling |
| tests/setup.ts | Test setup | Understand test patterns |
```

---

## Phase 7: Offer Next Steps

After generating the report, offer these options:

> **Analysis complete!** Here's what I found: [summary]
>
> What would you like to do next?
> 1. **Add missing guardrails** - Set up pre-commit hooks, linting, etc.
> 2. **Generate detailed conventions doc** - Document patterns for team
> 3. **Set up Claude integration** - Run `/initialize-project` to add Claude skills
> 4. **Start working on code** - I'll follow the conventions I detected
> 5. **Something else**

---

## Quick Analysis (One Command)

For a quick overview without the full report:

```bash
echo "=== Quick Analysis ===" && \
echo "Repo: $(basename $(pwd))" && \
echo "Type: $([ -d packages ] && echo 'Monorepo' || ([ -d frontend ] && [ -d backend ] && echo 'Full-Stack') || echo 'Standard')" && \
echo "Tech: $([ -f package.json ] && echo 'JS/TS' || ([ -f pyproject.toml ] && echo 'Python') || echo 'Other')" && \
echo "Guardrails: $([ -d .husky ] || [ -f .pre-commit-config.yaml ] && echo 'Present' || echo 'Missing')" && \
echo "CI/CD: $([ -d .github/workflows ] && echo 'GitHub Actions' || echo 'None')"
```

```

### File: commands\analyze-workspace.md
```md
# /analyze-workspace

> Full dynamic analysis of workspace topology, dependencies, and contracts.

## Trigger

Run this command when:
- First time setting up workspace awareness
- Major refactor or new module added
- Weekly scheduled refresh
- `/sync-contracts` reports too much drift
- Switching to work on a different workspace

## Behavior

### Phase 1: Topology Discovery (~30 seconds)

```
🔍 Analyzing workspace topology...

Checking workspace indicators:
  ✓ Found turbo.json (Turborepo)
  ✓ Found pnpm-workspace.yaml
  ✗ No nx.json
  ✗ No lerna.json

Workspace type: Monorepo (Turborepo)
Root: /Users/ali/code/myapp

Discovering modules...
  ✓ apps/web (package.json found)
  ✓ apps/api (pyproject.toml found)
  ✓ packages/shared-types (package.json found)
  ✓ packages/db (package.json found)

Modules found: 4
```

### Phase 2: Module Analysis (~60 seconds)

For each module, analyze:

```
📦 Analyzing apps/web...
  Tech stack: Next.js 14, TypeScript, TailwindCSS
  Entry point: src/app/layout.tsx
  Key directories: src/lib/, src/components/, src/types/
  Dependencies: @repo/shared-types, @repo/ui
  External calls: fetch → apps/api (15 files)
  Token estimate: 18K full, 5K summarized

📦 Analyzing apps/api...
  Tech stack: FastAPI, Python 3.12, SQLAlchemy
  Entry point: app/main.py
  Key directories: app/routes/, app/schemas/, app/models/
  Dependencies: packages/db (internal)
  Exposes: OpenAPI spec (47 endpoints)
  Token estimate: 24K full, 7K summarized

📦 Analyzing packages/shared-types...
  Tech stack: TypeScript
  Entry point: src/index.ts
  Exports: 34 types
  Consumed by: apps/web, apps/api (codegen)
  Token estimate: 3K

📦 Analyzing packages/db...
  Tech stack: Drizzle ORM, TypeScript
  Entry point: src/index.ts
  Tables: 12
  Migrations: 23
  Token estimate: 8K full, 2K schema only
```

### Phase 3: Contract Extraction (~45 seconds)

```
📜 Extracting contracts...

OpenAPI Detection:
  ✓ apps/api/openapi.json (47 endpoints, 23 schemas)

GraphQL Detection:
  ✗ No GraphQL schemas found

TypeScript Types:
  ✓ packages/shared-types/src/index.ts (34 exports)

Pydantic Schemas:
  ✓ apps/api/app/schemas/ (23 models)

Database Schema:
  ✓ packages/db/schema/ (12 tables)

Contract sources registered: 5 files
```

### Phase 4: Dependency Graph (~30 seconds)

```
🔗 Building dependency graph...

Internal dependencies:
  apps/web → packages/shared-types (23 imports)
  apps/web → apps/api (15 API calls)
  apps/api → packages/db (12 imports)
  apps/api → packages/shared-types (codegen)
  packages/db → (none)
  packages/shared-types → (none)

Dependency order (for changes):
  1. packages/shared-types (leaf)
  2. packages/db (leaf)
  3. apps/api (depends on db, shared-types)
  4. apps/web (depends on api, shared-types)
```

### Phase 5: Key File Identification (~30 seconds)

```
📁 Identifying key files...

High priority (always relevant):
  ✓ apps/api/openapi.json
  ✓ packages/shared-types/src/index.ts
  ✓ apps/web/src/lib/api/client.ts

Context-specific:
  ✓ API work: apps/api/app/routes/*.py
  ✓ DB work: packages/db/schema/*.ts
  ✓ Auth work: apps/api/app/routes/auth.py + deps
  ✓ Frontend: apps/web/src/components/**

Token budget by context:
  Frontend API: ~8K tokens
  Backend endpoints: ~12K tokens
  Database changes: ~6K tokens
  Shared types: ~4K tokens
```

### Phase 6: Generate Artifacts

```
📝 Generating workspace artifacts...

Created:
  ✓ _project_specs/workspace/TOPOLOGY.md
  ✓ _project_specs/workspace/CONTRACTS.md
  ✓ _project_specs/workspace/DEPENDENCY_GRAPH.md
  ✓ _project_specs/workspace/KEY_FILES.md
  ✓ _project_specs/workspace/CROSS_REPO_INDEX.md
  ✓ _project_specs/workspace/.contract-sources
```

## Final Output

```
════════════════════════════════════════════════════════════════
  WORKSPACE ANALYSIS COMPLETE
════════════════════════════════════════════════════════════════

Workspace: myapp
Type: Monorepo (Turborepo)
Modules: 4 (2 apps, 2 packages)

┌─────────────────────────────────────────────────┐
│ apps/web (Next.js) ←──── apps/api (FastAPI)     │
│      │                        │                 │
│      ▼                        ▼                 │
│ packages/shared-types    packages/db            │
└─────────────────────────────────────────────────┘

Contracts:
  REST API: 47 endpoints
  Shared types: 34 interfaces
  DB tables: 12

Token Estimates:
  Current module only: ~20K tokens
  With cross-module context: ~45K tokens
  Full workspace: ~53K tokens
  Budget remaining: ~100K tokens ✓

Artifacts generated in: _project_specs/workspace/

Next steps:
  • Contracts will auto-sync on commit (if changed)
  • Run /sync-contracts manually to refresh
  • Run /workspace-status for quick check

════════════════════════════════════════════════════════════════
```

## Flags

| Flag | Description |
|------|-------------|
| `--force` | Regenerate all artifacts even if recent |
| `--type <type>` | Override auto-detection: `monorepo`, `multi-repo`, `hybrid` |
| `--repos <paths>` | For multi-repo: comma-separated paths to related repos |
| `--skip-contracts` | Skip contract extraction (faster) |
| `--verbose` | Show detailed analysis output |
| `--json` | Output as JSON (for tooling) |

## Multi-Repo Mode

For workspaces with separate git repositories:

```bash
# Auto-detect sibling repos
/analyze-workspace --type multi-repo

# Specify repo locations explicitly
/analyze-workspace --type multi-repo --repos "../backend,../shared,../mobile"
```

Claude will:
1. Detect related repos in parent directory
2. Set up symlinks in `.workspace/repos/` if needed
3. Analyze each repo
4. Build cross-repo dependency graph
5. Extract contracts from each

## Integration Points

### On First Run

Creates the full workspace context structure:

```
_project_specs/
└── workspace/
    ├── TOPOLOGY.md
    ├── CONTRACTS.md
    ├── DEPENDENCY_GRAPH.md
    ├── KEY_FILES.md
    ├── CROSS_REPO_INDEX.md
    ├── .contract-sources
    └── cache/              # Cached cross-repo files
```

### Updates CLAUDE.md

Adds workspace skill reference:

```markdown
## Skills
- .claude/skills/workspace.md
```

### Sets Up Hooks

Installs contract freshness hooks:
- Session start: Staleness check
- Post-commit: Auto-sync trigger
- Pre-push: Validation gate

## Error Handling

### No Workspace Detected

```
⚠️  No workspace configuration detected

This appears to be a single-repo project.
Use /analyze-repo for single repository analysis.

Or specify workspace type manually:
  /analyze-workspace --type monorepo
  /analyze-workspace --type multi-repo --repos "../other-repo"
```

### Access Denied to Related Repo

```
⚠️  Cannot access related repository: ../backend

Options:
  1. Ensure the repo exists at that path
  2. Create symlink: ln -s /path/to/backend .workspace/repos/backend
  3. Skip this repo: /analyze-workspace --skip-repo backend
```

### Contract Extraction Failed

```
⚠️  Failed to extract contracts from apps/api

Reason: openapi.json not found

Suggestions:
  1. Generate OpenAPI spec: cd apps/api && python -m app.generate_openapi
  2. Skip contract extraction: /analyze-workspace --skip-contracts
  3. Use inferred contracts: /analyze-workspace --infer-contracts
```

## When to Re-run

| Scenario | Action |
|----------|--------|
| Added new module/package | Full `/analyze-workspace` |
| Changed API endpoints | `/sync-contracts` (lightweight) |
| Major refactor | Full `/analyze-workspace --force` |
| Weekly maintenance | Full `/analyze-workspace` |
| Quick check | `/workspace-status` |

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
