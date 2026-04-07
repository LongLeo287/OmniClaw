---
id: oh
type: knowledge
owner: OA_Triage
---
# oh
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "omp-monorepo",
	"private": true,
	"type": "module",
	"workspaces": [
		"packages/*"
	],
	"scripts": {
		"install:dev": "bun install && bun --cwd=packages/coding-agent link && bun --cwd=packages/ai link",
		"dev": "bun --cwd=packages/coding-agent src/cli.ts",
		"stats": "bun --cwd=packages/coding-agent src/cli.ts stats",
		"test": "bun run --workspaces --if-present --parallel test",
		"check": "bun run --parallel check:ts check:rs",
		"check:ts": "biome check . && tsgo -p tsconfig.json",
		"check:rs": "cargo fmt --all -- --check && cargo clippy --workspace -- -D warnings",
		"lint": "bun run --parallel lint:ts lint:rs",
		"lint:ts": "biome lint .",
		"lint:rs": "cargo clippy --workspace -- -D warnings",
		"fmt": "bun run --parallel fmt:ts fmt:rs",
		"fmt:ts": "biome format --write .",
		"fmt:rs": "cargo fmt --all",
		"fix": "bun run --parallel fix:ts fix:rs",
		"fix:ts": "biome check --write --unsafe . && bun --cwd=packages/coding-agent run format-prompts && bun --cwd=packages/coding-agent run generate-docs-index",
		"fix:rs": "cargo fmt --all && cargo clippy --fix --allow-dirty --all-targets --no-deps --allow-staged --broken-code --allow-no-vcs",
		"build:native": "bun --cwd=packages/natives run build:native",
		"dev:native": "bun --cwd=packages/natives run dev:native",
		"bench:gen-fixtures": "bun --cwd=packages/react-edit-benchmark run src/generate.ts --react-dir /tmp/react-source --count-per-type 8",
		"bench:edit": "bun --cwd=packages/react-edit-benchmark run start",
		"prepublishOnly": "bun run check",
		"prepare": "bun --cwd=packages/coding-agent run generate-docs-index",
		"publish": "bun run prepublishOnly && npm publish -ws --access public",
		"publish:dry": "bun run prepublishOnly && npm publish -ws --access public --dry-run",
		"release": "bun scripts/release.ts",
		"generate-models": "bun --cwd=packages/ai scripts/generate-models.ts",
		"generate-docs-index": "bun --cwd=packages/coding-agent run generate-docs-index",
		"generate-template": "bun --cwd=packages/coding-agent run generate-template",
		"sync-exports": "bun scripts/sync-exports.ts",
		"check-spoofed-versions": "bun scripts/check-spoofed-versions.ts"
	},
	"devDependencies": {
		"@biomejs/biome": "^2.4",
		"@bufbuild/protoc-gen-es": "^2.11",
		"@types/bun": "^1.3",
		"@typescript/native-preview": "^7.0.0-dev.20260302.1",
		"lint-staged": "^16.3",
		"prettier": "^3.8"
	},
	"lint-staged": {
		"*.{js,ts,jsx,tsx,json,jsonc,css}": "biome check --write --no-errors-on-unmatched"
	}
}

```

### File: README.md
```md
<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/hero.png?raw=true" alt="Pi Monorepo">
</p>

<p align="center">
  <strong>AI coding agent for the terminal</strong>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent"><img src="https://img.shields.io/npm/v/@oh-my-pi/pi-coding-agent?style=flat&colorA=222222&colorB=CB3837" alt="npm version"></a>
  <a href="https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/CHANGELOG.md"><img src="https://img.shields.io/badge/changelog-keep-E05735?style=flat&colorA=222222" alt="Changelog"></a>
  <a href="https://github.com/can1357/oh-my-pi/actions"><img src="https://img.shields.io/github/actions/workflow/status/can1357/oh-my-pi/ci.yml?style=flat&colorA=222222&colorB=3FB950" alt="CI"></a>
  <a href="https://github.com/can1357/oh-my-pi/blob/main/LICENSE"><img src="https://img.shields.io/github/license/can1357/oh-my-pi?style=flat&colorA=222222&colorB=58A6FF" alt="License"></a>
  <a href="https://www.typescriptlang.org"><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&colorA=222222&logo=typescript&logoColor=white" alt="TypeScript"></a>
  <a href="https://www.rust-lang.org"><img src="https://img.shields.io/badge/Rust-DEA584?style=flat&colorA=222222&logo=rust&logoColor=white" alt="Rust"></a>
  <a href="https://bun.sh"><img src="https://img.shields.io/badge/runtime-Bun-f472b6?style=flat&colorA=222222" alt="Bun"></a>
  <a href="https://discord.gg/4NMW9cdXZa"><img src="https://img.shields.io/badge/Discord-5865F2?style=flat&colorA=222222&logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  Fork of <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a> by <a href="https://github.com/mariozechner">@mariozechner</a>
</p>

## Table of Contents

- [Highlights](#highlights)
- [Installation](#installation)
- [Getting Started](#getting-started)
  - [Terminal Setup](#terminal-setup)
  - [API Keys & OAuth](#api-keys--oauth)
  - [First 15 Minutes (Recommended)](#first-15-minutes-recommended)
- [Usage](#usage)
  - [Slash Commands](#slash-commands)
  - [Editor Features](#editor-features)
  - [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Bash Mode](#bash-mode)
  - [Image Support](#image-support)
- [Sessions](#sessions)
  - [Session Management](#session-management)
  - [Context Compaction](#context-compaction)
  - [Branching](#branching)
  - [Autonomous Memory](#autonomous-memory)
- [Configuration](#configuration)
  - [Project Context Files](#project-context-files)
  - [Custom System Prompt](#custom-system-prompt)
  - [Custom Models and Providers](#custom-models-and-providers)
  - [Settings File](#settings-file)
- [Extensions](#extensions)
  - [Themes](#themes)
  - [Custom Slash Commands](#custom-slash-commands)
  - [Skills](#skills)
  - [Hooks](#hooks)
  - [Custom Tools](#custom-tools)
- [CLI Reference](#cli-reference)
- [Tools](#tools)
- [Programmatic Usage](#programmatic-usage)
  - [SDK](#sdk)
  - [RPC Mode](#rpc-mode)
  - [HTML Export](#html-export)
- [Philosophy](#philosophy)
- [Development](#development)
- [Monorepo Packages](#monorepo-packages)
- [License](#license)

---

## Highlights

### + Commit Tool (AI-Powered Git Commits)

AI-powered conventional commit generation with intelligent change analysis:

- **Agentic mode**: Tool-based git inspection with `git-overview`, `git-file-diff`, `git-hunk` for fine-grained analysis
- **Split commits**: Automatically separates unrelated changes into atomic commits with dependency ordering
- **Hunk-level staging**: Stage individual hunks when changes span multiple concerns
- **Changelog generation**: Proposes and applies changelog entries to `CHANGELOG.md` files
- **Commit validation**: Detects filler words, meta phrases, and enforces conventional commit format
- **Legacy mode**: `--legacy` flag for deterministic pipeline when preferred
- Run via `omp commit` with options: `--push`, `--dry-run`, `--no-changelog`, `--context`

### + Python Tool (IPython Kernel)

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/python.webp?raw=true" alt="python">
</p>

Execute Python code with a persistent IPython kernel and rich helper prelude:

- **Streaming output**: Real-time stdout/stderr with image and JSON rendering
- **Prelude helpers**: File I/O, search, find/replace, line operations, shell, and text utilities built into the kernel
- **Line operations**: `lines()`, `insert_at()`, `delete_lines()`, `delete_matching()` and related helpers for precise edits
- **Shared gateway**: Resource-efficient kernel reuse across sessions (`python.sharedGateway` setting)
- **Custom modules**: Load extensions from `.omp/modules/` and `~/.omp/agent/modules/`
- **Rich output**: Supports `display()` for HTML, Markdown, images, and interactive JSON trees
- **Markdown rendering**: Python cell output with Markdown content renders inline
- **Mermaid diagrams**: Renders mermaid code blocks as inline graphics in iTerm2/Kitty terminals
- Install dependencies via `omp setup python`

### + LSP Integration (Language Server Protocol)

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/lspv.webp?raw=true" alt="lsp">
</p>

Full IDE-like code intelligence with automatic formatting and diagnostics:

- **11 LSP operations**: `diagnostics`, `definition`, `type_definition`, `implementation`, `references`, `hover`, `symbols`, `rename`, `code_actions`, `status`, `reload`
- **Format-on-write**: Auto-format code using the language server's formatter (rustfmt, gofmt, prettier, etc.)
- **Diagnostics on write/edit**: Immediate feedback on syntax errors and type issues after every file change
- **Workspace diagnostics**: Check entire project for errors with `lsp` action `diagnostics` (without a file)
- **40+ language configs**: Out-of-the-box support for Rust, Go, Python, TypeScript, Java, Kotlin, Scala, Haskell, OCaml, Elixir, Ruby, PHP, C#, Lua, Nix, and many more
- **Local binary resolution**: Auto-discovers project-local LSP servers in `node_modules/.bin/`, `.venv/bin/`, etc.
- **Symbol disambiguation**: `occurrence` parameter resolves repeated symbols on the same line

### + Time Traveling Streamed Rules (TTSR)

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/ttsr.webp?raw=true" alt="ttsr">
</p>

Zero context-use rules that inject themselves only when needed:

- **Pattern-triggered injection**: Rules define regex triggers that watch the model's output stream
- **Just-in-time activation**: When a pattern matches, the stream aborts, the rule injects as a system reminder, and the request retries
- **Zero upfront cost**: TTSR rules consume no context until they're actually relevant
- **One-shot per session**: Each rule only triggers once, preventing loops
- Define via `ttsrTrigger` field in rule files (regex pattern)

Example: A "don't use deprecated API" rule only activates when the model starts writing deprecated code, saving context for sessions that never touch that API.

### + Interactive Code Review

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/review.webp?raw=true" alt="review">
</p>

Structured code review with priority-based findings:

- **`/review` command**: Interactive mode selection (branch comparison, uncommitted changes, commit review)
- **Structured findings**: `report_finding` tool with priority levels (P0-P3: critical → nit)
- **Verdict rendering**: aggregates findings into approve/request-changes/comment
- Combined result tree showing verdict and all findings

### + Task Tool (Subagent System)

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/task.webp?raw=true" alt="task">
</p>

Parallel execution framework with specialized agents and real-time streaming:

- **6 bundled agents**: explore, plan, designer, reviewer, task, quick_task
- **Parallel exploration**: Reviewer agent can spawn explore agents for large codebase analysis
- **Real-time artifact streaming**: Task outputs stream as they're created, not just at completion
- **Full output access**: Read complete subagent output via `agent://<id>` resources when previews truncate
- **Isolation backends**: `isolated: true` runs tasks in git worktrees, Unix fuse-overlay filesystems, or Windows ProjFS (`fuse-projfs`), with patch or branch merge strategies
- **Async background jobs**: Background execution with configurable concurrency (up to 100 jobs) and `await` tool for blocking on results
- **Agent Control Center**: `/agents` dashboard for managing and creating custom agents
- **AI-powered agent creation**: Generate custom agent definitions with the architect model
- **Per-agent model overrides**: Assign specific models to individual agents via swarm extension
- User-level (`~/.omp/agent/agents/`) and project-level (`.omp/agents/`) custom agents

### + Model Roles

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/models.webp?raw=true" alt="models">
</p>

Configure different models for different purposes with automatic discovery:

- **Role-based routing**: `default`, `smol`, `slow`, `plan`, and `commit` roles
- **Configurable discovery**: Role defaults are auto-resolved and can be overridden per role
- **Role-based selection**: Task tool agents can use `model: pi/smol` for cost-effective exploration
- CLI args (`--smol`, `--slow`, `--plan`) and env vars (`PI_SMOL_MODEL`, `PI_SLOW_MODEL`, `PI_PLAN_MODEL`)
- Configure roles interactively via `/model` selector and persist assignments to settings

### + Todo Tool (Task Tracking)

Structured task management with phased progress tracking:

- **Phased task lists**: Organize work into named phases with ordered tasks
- **5 operations**: `replace` (setup), `add_phase`, `add_task`, `update` (status changes), `remove_task`
- **4 task states**: `pending`, `in_progress`, `completed`, `abandoned`
- **Auto-normalization**: Ensures exactly one task is `in_progress` at all times
- **Persistent panel**: Todo list displays above the editor with real-time progress
- **Completion reminders**: Agent warned when stopping with incomplete todos (`todo.reminders` setting)
- **Toggle visibility**: `Ctrl+T` expands/collapses the todo panel

### + Ask Tool (Interactive Questioning)

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/ask.webp?raw=true" alt="ask">
</p>

Structured user interaction with typed options:

- **Multiple choice questions**: Present options with descriptions for user selection
- **Multi-select support**: Allow multiple answers when choices aren't mutually exclusive
- **Multi-part questions**: Ask multiple related questions in sequence via `questions` array parameter

### + Custom TypeScript Slash Commands

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/slash.webp?raw=true" alt="slash">
</p>

Programmable commands with full API access:

- Create at `~/.omp/agent/commands/[name]/index.ts` or `.omp/commands/[name]/index.ts`
- Export factory returning `{ name, description, execute(args, ctx) }`
- Full access to `HookCommandContext` for UI dialogs, session control, shell execution
- Return string to send as LLM prompt, or void for fire-and-forget actions
- Also loads from Claude Code directories (`~/.claude/commands/`, `.claude/commands/`)

### + Universal Config Discovery

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/discovery.webp?raw=true" alt="discovery">
</p>

Unified capability-based discovery that loads configuration from 8 AI coding tools:

- **Multi-tool support**: Claude Code, Cursor, Windsurf, Gemini, Codex, Cline, GitHub Copilot, VS Code
- **Discovers everything**: MCP servers, rules, skills, hooks, tools, slash commands, prompts, context files
- **Native format support**: Cursor MDC frontmatter, Windsurf rules, Cline `.clinerules`, Copilot `applyTo` globs, Gemini `system.md`, Codex `AGENTS.md`
- **Provider attribution**: See which tool contributed each configuration item
- **Discovery settings**: Enable/disable individual providers via `/extensions` interactive dashboard
- **Priority ordering**: Multi-path resolution across `.omp`, `.claude`, `.codex`, and `.gemini` directories

### + MCP & Plugin System

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/perplexity.webp?raw=true" alt="perplexity">
</p>

Full Model Context Protocol support with external tool integration:

- Stdio and HTTP transports for connecting to MCP servers
- **OAuth support**: Explicit `clientId` and `callbackPort` in MCP server config, manual OAuth callbacks via slash commands
- **Browser server filtering**: Automatically filters browser-type MCP servers to prevent conflicts with built-in browser tool
- **Automatic Exa filtering**: Extracts Exa API keys and prefers the native Exa integration
- **Config schema + setup guide**: [`docs/mcp-config.md`](./docs/mcp-config.md) and [`packages/coding-agent/src/config/mcp-schema.json`](./packages/coding-agent/src/config/mcp-schema.json)
- Plugin CLI (`omp plugin install/enable/configure/doctor`)
- Hot-loadable plugins from `~/.omp/plugins/` with npm/bun integration
- `disabledServers` works on both project-level and user-level third-party servers

### + Web Search & Fetch

<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/arxiv.webp?raw=true" alt="arxiv">
</p>

Multi-provider search and full-page scraping with specialized handlers:

- **Multi-provider search**: `auto`, `exa`, `brave`, `jina`, `kimi`, `zai`, `anthropic`, `perplexity`, `gemini`, `codex`, `synthetic`
- **Specialized handlers**: Site-specific extraction for code hosts, registries, research sources, forums, and docs
- **Package registries**: npm, PyPI, crates.io, Hex, Hackage, NuGet, Maven, RubyGems, Packagist, pub.dev, Go packages
- **Security databases**: NVD, OSV, CISA KEV vulnerability data
- HTML-to-markdown conversion with link preservation

### + SSH Tool

Remote command execution with persistent connections:

- **Project discovery**: Reads SSH hosts from `ssh.json` / `.ssh.json` in your project
- **Host management**: Add, remove, and list hosts via `omp ssh` CLI or `/ssh` slash command
- **Persistent connections**: Reuses SSH connections across commands for faster execution
- **OS/shell detection**: Automatically detects remote OS and shell type
- **SSHFS mounts**: Optional automatic mounting of remote directories
- **Compat mode**: Windows host support with automatic shell probing

### + Browser Tool (Puppeteer with Stealth)

Headless browser automation with 14 stealth scripts to evade bot detection:

- **Automation actions**: Navigate, click, type, fill, scroll, drag, screenshot, evaluate JS, and extract readable content
- **Accessibility snapshots**: Observe interactive elements via the accessibility tree with numeric IDs for reliable targeting
- **14 stealth plugins**: Custom script
... [TRUNCATED]
```

### File: playground\README.md
```md
# Autoresearch Research Showcase

This folder collects **small, reproducible research-style demos** used to showcase `omx autoresearch` on harder optimization problems.

Design goals:
- deterministic or seed-controlled evaluations
- small code footprint
- no large datasets checked into git
- no heavyweight runtime artifacts committed
- evaluator-driven keep/discard loops that are easy to inspect under `.omx/logs/autoresearch/`

## Layout

- `playground/*` — demo code and benchmark logic
- `missions/*` — autoresearch mission contracts used by the showcase
- `scripts/eval-*` — focused evaluator entrypoints
- `scripts/run-autoresearch-showcase.sh` — convenience launcher for the bundled showcase missions

Naming convention:
- playground demo dirs use `*_demo` when they are standalone benchmark implementations
- mission dirs use problem/task slugs under `missions/`
- evaluator scripts follow `scripts/eval-<mission-slug>.(js|py)`
- the showcase runner maps short names (for example `bayesopt`, `latent`, `sorting`) to mission dirs

## Index

| Showcase | Mission | Evaluator | Status | Representative result |
|---|---|---|---|---|
| OMX self-optimization | `missions/in-action-cat-shellout-demo/` | `scripts/eval-in-action-cat-shellout-demo.js` | ✅ completed | kept commit `99ebf16` / cherry-picked as `8478261` removing the autoresearch manifest `cat` shell-out |
| Kaggle-style tabular ML | `missions/ml-kaggle-model-optimization/` | `scripts/eval-ml-kaggle-model-optimization.py` | ✅ completed | ROC AUC improved from `0.9458071278825997` to `0.9976939203354298` |
| Noisy high-dimensional Bayes-opt | `missions/noisy-bayesopt-highdim/` | `scripts/eval-noisy-bayesopt-highdim.py` | ✅ completed | score improved from `2.833048700169374` to `4.75978993804531` |
| Latent subspace discovery | `missions/noisy-latent-subspace-discovery/` | `scripts/eval-noisy-latent-subspace-discovery.py` | ✅ completed | score improved from `3.7019658949006504` to `4.176124116152444` with a compact `cem_search` strategy |
| Adaptive sorting optimization | `missions/adaptive-sort-optimization/` | `scripts/eval-adaptive-sort-optimization.py` | ✅ completed | score improved from `2.1198297352756628` to `9.411498969440865` by switching counting sort to the observed value span |

Use `scripts/run-autoresearch-showcase.sh --list` to see the bundled launch targets, or run one or more showcases directly with the wrapper script.

## Results matrix

| Showcase | Baseline | Kept / best documented result | Delta |
|---|---:|---:|---:|
| OMX self-optimization | n/a | behavior-preserving cleanup | n/a |
| Kaggle-style tabular ML | 0.9458071278825997 AUC | 0.9976939203354298 AUC | +0.0518867924528301 |
| Noisy high-dimensional Bayes-opt | 2.833048700169374 | 4.75978993804531 | +1.926741237875936 |
| Latent subspace discovery | 3.7019658949006504 | 4.176124116152444 | +0.47415822125179353 |
| Adaptive sorting optimization | 2.1198297352756628 | 9.411498969440865 | +7.291669234165202 |

## Demos

### 1. OMX self-optimization
- Mission: `missions/in-action-cat-shellout-demo/`
- Evaluator: `scripts/eval-in-action-cat-shellout-demo.js`
- What it demonstrates: a tiny self-hosted code optimization loop where autoresearch removes an unnecessary shell-out from OMX itself.

### 2. Kaggle-style tabular ML optimization
- Demo code: `playground/ml_kaggle_demo/`
- Mission: `missions/ml-kaggle-model-optimization/`
- Evaluator: `scripts/eval-ml-kaggle-model-optimization.py`
- What it demonstrates: model-family / hyperparameter search on a deterministic tabular classification benchmark with a score-improvement keep policy.

### 3. Noisy high-dimensional Bayes-opt demo
- Demo code: `playground/bayesopt_highdim_demo/`
- Mission: `missions/noisy-bayesopt-highdim/`
- Evaluator: `scripts/eval-noisy-bayesopt-highdim.py`
- What it demonstrates: a harder black-box optimization task with noise, limited evaluation budget, and curse-of-dimensionality pressure. The successful autoresearch run switched from random search to a subspace-aware fixed-kernel GP with denoised incumbent selection.

### 4. Latent subspace discovery demo
- Demo code: `playground/bayesopt_latent_discovery_demo/`
- Mission: `missions/noisy-latent-subspace-discovery/`
- Evaluator: `scripts/eval-noisy-latent-subspace-discovery.py`
- What it demonstrates: a follow-on harder variant where useful structure is mixed through latent directions rather than directly exposed as obvious coordinates.

### 5. Adaptive sorting optimization demo
- Demo code: `playground/adaptive_sort_demo/`
- Mission: `missions/adaptive-sort-optimization/`
- Evaluator: `scripts/eval-adaptive-sort-optimization.py`
- What it demonstrates: algorithm-engineering optimization over a deterministic mixed-distribution sorting benchmark using weighted comparison/move cost rather than noisy wall-clock timing.

## Running the showcase

Example:

```bash
omx autoresearch missions/noisy-bayesopt-highdim
```

Then inspect:

```bash
RUN_ID=$(find .omx/logs/autoresearch -maxdepth 1 -mindepth 1 -type d -printf '%f\n' | sort | tail -n 1)
cat .omx/logs/autoresearch/$RUN_ID/manifest.json
cat .omx/logs/autoresearch/$RUN_ID/candidate.json
cat .omx/logs/autoresearch/$RUN_ID/iteration-ledger.json
```

You can also run evaluators directly without the supervisor:

```bash
node scripts/eval-in-action-cat-shellout-demo.js
python3 scripts/eval-ml-kaggle-model-optimization.py
python3 scripts/eval-noisy-bayesopt-highdim.py
python3 scripts/eval-noisy-latent-subspace-discovery.py
python3 scripts/eval-adaptive-sort-optimization.py
```

## Repository hygiene

These showcases are meant to stay lightweight.

Please avoid committing:
- downloaded datasets
- large model artifacts
- benchmark output dumps
- generated caches like `__pycache__/`
- runtime autoresearch logs under `.omx/logs/`

Keep research state in code, configs, missions, and evaluator scripts; keep bulky runtime outputs local.

```

### File: packages\agent\package.json
```json
{
	"type": "module",
	"name": "@oh-my-pi/pi-agent-core",
	"version": "13.18.0",
	"description": "General-purpose agent with transport abstraction, state management, and attachment support",
	"homepage": "https://github.com/can1357/oh-my-pi",
	"author": "Can Boluk",
	"contributors": [
		"Mario Zechner"
	],
	"license": "MIT",
	"repository": {
		"type": "git",
		"url": "git+https://github.com/can1357/oh-my-pi.git",
		"directory": "packages/agent"
	},
	"bugs": {
		"url": "https://github.com/can1357/oh-my-pi/issues"
	},
	"keywords": [
		"ai",
		"agent",
		"llm",
		"transport",
		"state-management"
	],
	"main": "./src/index.ts",
	"types": "./src/index.ts",
	"scripts": {
		"check": "tsgo -p tsconfig.json",
		"test": "bun test"
	},
	"dependencies": {
		"@oh-my-pi/pi-ai": "workspace:*",
		"@oh-my-pi/pi-utils": "workspace:*"
	},
	"devDependencies": {
		"@sinclair/typebox": "^0.34",
		"@types/bun": "^1.3"
	},
	"engines": {
		"bun": ">=1.3.7"
	},
	"files": [
		"src",
		"README.md",
		"CHANGELOG.md"
	],
	"exports": {
		".": {
			"types": "./src/index.ts",
			"import": "./src/index.ts"
		},
		"./*": {
			"types": "./src/*.ts",
			"import": "./src/*.ts"
		}
	}
}

```

### File: packages\agent\README.md
```md
# @oh-my-pi/pi-agent

Stateful agent with tool execution and event streaming. Built on `@oh-my-pi/pi-ai`.

## Installation

```bash
npm install @oh-my-pi/pi-agent
```

## Quick Start

```typescript
import { Agent } from "@oh-my-pi/pi-agent";
import { getModel } from "@oh-my-pi/pi-ai";

const agent = new Agent({
	initialState: {
		systemPrompt: "You are a helpful assistant.",
		model: getModel("anthropic", "claude-sonnet-4-20250514"),
	},
});

agent.subscribe((event) => {
	if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
		// Stream just the new text chunk
		process.stdout.write(event.assistantMessageEvent.delta);
	}
});

await agent.prompt("Hello!");
```

## Core Concepts

### AgentMessage vs LLM Message

The agent works with `AgentMessage`, a flexible type that can include:

- Standard LLM messages (`user`, `assistant`, `toolResult`)
- Custom app-specific message types via declaration merging

LLMs only understand `user`, `assistant`, and `toolResult`. The `convertToLlm` function bridges this gap by filtering and transforming messages before each LLM call.

### Message Flow

```
AgentMessage[] → transformContext() → AgentMessage[] → convertToLlm() → Message[] → LLM
                    (optional)                           (required)
```

1. **transformContext**: Prune old messages, inject external context
2. **convertToLlm**: Filter out UI-only messages, convert custom types to LLM format

## Event Flow

The agent emits events for UI updates. Understanding the event sequence helps build responsive interfaces.

### prompt() Event Sequence

When you call `prompt("Hello")`:

```
prompt("Hello")
├─ agent_start
├─ turn_start
├─ message_start   { message: userMessage }      // Your prompt
├─ message_end     { message: userMessage }
├─ message_start   { message: assistantMessage } // LLM starts responding
├─ message_update  { message: partial... }       // Streaming chunks
├─ message_update  { message: partial... }
├─ message_end     { message: assistantMessage } // Complete response
├─ turn_end        { message, toolResults: [] }
└─ agent_end       { messages: [...] }
```

### With Tool Calls

If the assistant calls tools, the loop continues:

```
prompt("Read config.json")
├─ agent_start
├─ turn_start
├─ message_start/end  { userMessage }
├─ message_start      { assistantMessage with toolCall }
├─ message_update...
├─ message_end        { assistantMessage }
├─ tool_execution_start  { toolCallId, toolName, args }
├─ tool_execution_update { partialResult }           // If tool streams
├─ tool_execution_end    { toolCallId, result }
├─ message_start/end  { toolResultMessage }
├─ turn_end           { message, toolResults: [toolResult] }
│
├─ turn_start                                        // Next turn
├─ message_start      { assistantMessage }           // LLM responds to tool result
├─ message_update...
├─ message_end
├─ turn_end
└─ agent_end
```

### continue() Event Sequence

`continue()` resumes from existing context without adding a new message. Use it for retries after errors.

```typescript
// After an error, retry from current state
await agent.continue();
```

The last message in context must be `user` or `toolResult` (not `assistant`).

### Event Types

| Event                   | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| `agent_start`           | Agent begins processing                                         |
| `agent_end`             | Agent completes with all new messages                           |
| `turn_start`            | New turn begins (one LLM call + tool executions)                |
| `turn_end`              | Turn completes with assistant message and tool results          |
| `message_start`         | Any message begins (user, assistant, toolResult)                |
| `message_update`        | **Assistant only.** Includes `assistantMessageEvent` with delta |
| `message_end`           | Message completes                                               |
| `tool_execution_start`  | Tool begins                                                     |
| `tool_execution_update` | Tool streams progress                                           |
| `tool_execution_end`    | Tool completes                                                  |

## Agent Options

```typescript
const agent = new Agent({
  // Initial state
  initialState: {
    systemPrompt: string,
    model: Model,
    thinkingLevel: "off" | "minimal" | "low" | "medium" | "high" | "xhigh",
    tools: AgentTool<any>[],
    messages: AgentMessage[],
  },

  // Convert AgentMessage[] to LLM Message[] (required for custom message types)
  convertToLlm: (messages) => messages.filter(...),

  // Transform context before convertToLlm (for pruning, compaction)
  transformContext: async (messages, signal) => pruneOldMessages(messages),

  // How to handle queued messages: "one-at-a-time" (default) or "all"
  queueMode: "one-at-a-time",

  // Custom stream function (for proxy backends)
  streamFn: streamProxy,

  // Dynamic API key resolution (for expiring OAuth tokens)
  getApiKey: async (provider) => refreshToken(),

  // Tool execution context (late-bound UI/session access)
  getToolContext: () => ({ /* app-defined */ }),
});
```

## Agent State

```typescript
interface AgentState {
	systemPrompt: string;
	model: Model;
	thinkingLevel: ThinkingLevel;
	tools: AgentTool<any>[];
	messages: AgentMessage[];
	isStreaming: boolean;
	streamMessage: AgentMessage | null; // Current partial during streaming
	pendingToolCalls: Set<string>;
	error?: string;
}
```

Access via `agent.state`. During streaming, `streamMessage` contains the partial assistant message.

## Methods

### Prompting

```typescript
// Text prompt
await agent.prompt("Hello");

// With images
await agent.prompt("What's in this image?", [{ type: "image", data: base64Data, mimeType: "image/jpeg" }]);

// AgentMessage directly
await agent.prompt({ role: "user", content: "Hello", timestamp: Date.now() });

// Continue from current context (last message must be user or toolResult)
await agent.continue();
```

### State Management

```typescript
agent.setSystemPrompt("New prompt");
agent.setModel(getModel("openai", "gpt-4o"));
agent.setThinkingLevel("medium");
agent.setTools([myTool]);
agent.replaceMessages(newMessages);
agent.appendMessage(message);
agent.clearMessages();
agent.reset(); // Clear everything
```

### Control

```typescript
agent.abort(); // Cancel current operation
await agent.waitForIdle(); // Wait for completion
```

### Events

```typescript
const unsubscribe = agent.subscribe((event) => {
	console.log(event.type);
});
unsubscribe();
```

## Steering & Follow-up

Queue messages to inject during tool execution (steering) or after the agent would otherwise stop (follow-up):

```typescript
agent.setSteeringMode("one-at-a-time");
agent.setInterruptMode("immediate");

// While agent is running tools
agent.steer({
	role: "user",
	content: "Stop! Do this instead.",
	timestamp: Date.now(),
});

// Queue a follow-up to run after the current turn completes
agent.followUp({
	role: "user",
	content: "After that, summarize the changes.",
	timestamp: Date.now(),
});
```

Steering messages are checked after each tool call by default. Set `interruptMode` to `"wait"` to defer
steering until the current turn completes.

## Custom Message Types

Extend `AgentMessage` via declaration merging:

```typescript
declare module "@oh-my-pi/pi-agent" {
	interface CustomAgentMessages {
		notification: { role: "notification"; text: string; timestamp: number };
	}
}

// Now valid
const msg: AgentMessage = { role: "notification", text: "Info", timestamp: Date.now() };
```

Handle custom types in `convertToLlm`:

```typescript
const agent = new Agent({
	convertToLlm: (messages) =>
		messages.flatMap((m) => {
			if (m.role === "notification") return []; // Filter out
			return [m];
		}),
});
```

## Tools

Define tools using `AgentTool`:

```typescript
import { Type } from "@sinclair/typebox";

const readFileTool: AgentTool = {
	name: "read_file",
	label: "Read File", // For UI display
	description: "Read a file's contents",
	parameters: Type.Object({
		path: Type.String({ description: "File path" }),
	}),
	execute: async (toolCallId, params, signal, onUpdate, context) => {
		const content = await fs.readFile(params.path, "utf-8");

		// Optional: stream progress
		onUpdate?.({ content: [{ type: "text", text: "Reading..." }], details: {} });

		return {
			content: [{ type: "text", text: content }],
			details: { path: params.path, size: content.length },
		};
	},
};

agent.setTools([readFileTool]);
```

### Error Handling

**Throw an error** when a tool fails. Do not return error messages as content.

```typescript
execute: async (toolCallId, params, signal, onUpdate) => {
	if (!fs.existsSync(params.path)) {
		throw new Error(`File not found: ${params.path}`);
	}
	// Return content only on success
	return { content: [{ type: "text", text: "..." }] };
};
```

Thrown errors are caught by the agent and reported to the LLM as tool errors with `isError: true`.

## Proxy Usage

For browser apps that proxy through a backend:

```typescript
import { Agent, streamProxy } from "@oh-my-pi/pi-agent";

const agent = new Agent({
	streamFn: (model, context, options) =>
		streamProxy(model, context, {
			...options,
			authToken: "...",
			proxyUrl: "https://your-server.com",
		}),
});
```

## Low-Level API

For direct control without the Agent class:

```typescript
import { agentLoop, agentLoopContinue } from "@oh-my-pi/pi-agent";

const context: AgentContext = {
	systemPrompt: "You are helpful.",
	messages: [],
	tools: [],
};

const config: AgentLoopConfig = {
	model: getModel("openai", "gpt-4o"),
	convertToLlm: (msgs) => msgs.filter((m) => ["user", "assistant", "toolResult"].includes(m.role)),
};

const userMessage = { role: "user", content: "Hello", timestamp: Date.now() };

for await (const event of agentLoop([userMessage], context, config)) {
	console.log(event.type);
}

// Continue from existing context
for await (const event of agentLoopContinue(context, config)) {
	console.log(event.type);
}
```

## License

MIT

```

### File: packages\ai\package.json
```json
{
	"type": "module",
	"name": "@oh-my-pi/pi-ai",
	"version": "13.18.0",
	"description": "Unified LLM API with automatic model discovery and provider configuration",
	"homepage": "https://github.com/can1357/oh-my-pi",
	"author": "Can Boluk",
	"contributors": [
		"Mario Zechner"
	],
	"license": "MIT",
	"repository": {
		"type": "git",
		"url": "git+https://github.com/can1357/oh-my-pi.git",
		"directory": "packages/ai"
	},
	"bugs": {
		"url": "https://github.com/can1357/oh-my-pi/issues"
	},
	"keywords": [
		"ai",
		"llm",
		"openai",
		"anthropic",
		"gemini",
		"unified",
		"api"
	],
	"main": "./src/index.ts",
	"types": "./src/index.ts",
	"bin": {
		"pi-ai": "./src/cli.ts"
	},
	"scripts": {
		"check": "tsgo -p tsconfig.json",
		"generate-models": "bun scripts/generate-models.ts",
		"test": "bun test"
	},
	"dependencies": {
		"@anthropic-ai/sdk": "^0.78",
		"@aws-sdk/client-bedrock-runtime": "^3",
		"@bufbuild/protobuf": "^2.11",
		"@google/genai": "^1.43",
		"@oh-my-pi/pi-utils": "workspace:*",
		"@sinclair/typebox": "^0.34",
		"@smithy/node-http-handler": "^4.4",
		"ajv": "^8.18",
		"ajv-formats": "^3.0",
		"openai": "^6.25",
		"partial-json": "^0.1",
		"zod": "^4.3"
	},
	"devDependencies": {
		"@types/bun": "^1.3"
	},
	"engines": {
		"bun": ">=1.3.7"
	},
	"files": [
		"src",
		"README.md",
		"CHANGELOG.md"
	],
	"exports": {
		".": {
			"types": "./src/index.ts",
			"import": "./src/index.ts"
		},
		"./*": {
			"types": "./src/*.ts",
			"import": "./src/*.ts"
		},
		"./models.json": {
			"types": "./src/models.json.d.ts",
			"import": "./src/models.json"
		},
		"./provider-models": {
			"types": "./src/provider-models/index.ts",
			"import": "./src/provider-models/index.ts"
		},
		"./provider-models/*": {
			"types": "./src/provider-models/*.ts",
			"import": "./src/provider-models/*.ts"
		},
		"./providers/*": {
			"types": "./src/providers/*.ts",
			"import": "./src/providers/*.ts"
		},
		"./providers/cursor/gen/*": {
			"types": "./src/providers/cursor/gen/*.ts",
			"import": "./src/providers/cursor/gen/*.ts"
		},
		"./providers/openai-codex/*": {
			"types": "./src/providers/openai-codex/*.ts",
			"import": "./src/providers/openai-codex/*.ts"
		},
		"./usage/*": {
			"types": "./src/usage/*.ts",
			"import": "./src/usage/*.ts"
		},
		"./utils/*": {
			"types": "./src/utils/*.ts",
			"import": "./src/utils/*.ts"
		},
		"./utils/discovery": {
			"types": "./src/utils/discovery/index.ts",
			"import": "./src/utils/discovery/index.ts"
		},
		"./utils/discovery/*": {
			"types": "./src/utils/discovery/*.ts",
			"import": "./src/utils/discovery/*.ts"
		},
		"./utils/oauth": {
			"types": "./src/utils/oauth/index.ts",
			"import": "./src/utils/oauth/index.ts"
		},
		"./utils/oauth/*": {
			"types": "./src/utils/oauth/*.ts",
			"import": "./src/utils/oauth/*.ts"
		},
		"./utils/schema": {
			"types": "./src/utils/schema/index.ts",
			"import": "./src/utils/schema/index.ts"
		},
		"./utils/schema/*": {
			"types": "./src/utils/schema/*.ts",
			"import": "./src/utils/schema/*.ts"
		}
	}
}

```

### File: packages\ai\README.md
```md
# @oh-my-pi/pi-ai

Unified LLM API with automatic model discovery, provider configuration, token and cost tracking, and simple context persistence and hand-off to other models mid-session.

**Note**: This library only includes models that support tool calling (function calling), as this is essential for agentic workflows.

## Table of Contents

- [Supported Providers](#supported-providers)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Tools](#tools)
  - [Defining Tools](#defining-tools)
  - [Handling Tool Calls](#handling-tool-calls)
  - [Streaming Tool Calls with Partial JSON](#streaming-tool-calls-with-partial-json)
  - [Validating Tool Arguments](#validating-tool-arguments)
  - [Complete Event Reference](#complete-event-reference)
- [Image Input](#image-input)
- [Thinking/Reasoning](#thinkingreasoning)
  - [Unified Interface](#unified-interface-streamsimplecompletesimple)
  - [Provider-Specific Options](#provider-specific-options-streamcomplete)
  - [Streaming Thinking Content](#streaming-thinking-content)
- [Stop Reasons](#stop-reasons)
- [Error Handling](#error-handling)
  - [Aborting Requests](#aborting-requests)
  - [Continuing After Abort](#continuing-after-abort)
- [APIs, Models, and Providers](#apis-models-and-providers)
  - [Providers and Models](#providers-and-models)
  - [Querying Providers and Models](#querying-providers-and-models)
  - [Custom Models](#custom-models)
  - [OpenAI Compatibility Settings](#openai-compatibility-settings)
  - [Type Safety](#type-safety)
- [Cross-Provider Handoffs](#cross-provider-handoffs)
- [Context Serialization](#context-serialization)
- [Browser Usage](#browser-usage)
  - [Environment Variables](#environment-variables-nodejs-only)
  - [Checking Environment Variables](#checking-environment-variables)
- [OAuth Providers](#oauth-providers)
  - [Vertex AI (ADC)](#vertex-ai-adc)
  - [CLI Login](#cli-login)
  - [Programmatic OAuth](#programmatic-oauth)
  - [Login Flow Example](#login-flow-example)
  - [Using OAuth Tokens](#using-oauth-tokens)
  - [Provider Notes](#provider-notes)
- [License](#license)

## Supported Providers

- **OpenAI**
- **OpenAI Codex** (ChatGPT Plus/Pro subscription, requires OAuth, see below)
- **Anthropic**
- **Google**
- **Vertex AI** (Gemini via Vertex AI)
- **Mistral**
- **Groq**
- **Cerebras**
- **Together**
- **Moonshot** (requires `MOONSHOT_API_KEY`)
- **Qianfan** (requires `QIANFAN_API_KEY`)
- **NVIDIA** (requires `NVIDIA_API_KEY`)
- **NanoGPT** (requires `NANO_GPT_API_KEY`)
- **Hugging Face Inference**
- **xAI**
- **Venice** (requires `VENICE_API_KEY`)
- **OpenRouter**
- **Kilo Gateway** (supports OAuth `/login kilo` or `KILO_API_KEY`)
- **LiteLLM** (requires `LITELLM_API_KEY`)
- **zAI** (requires `ZAI_API_KEY`)
- **MiniMax Coding Plan** (requires `MINIMAX_CODE_API_KEY` or `MINIMAX_CODE_CN_API_KEY`)
- **Xiaomi MiMo** (requires `XIAOMI_API_KEY`)
- **ZenMux** (requires `ZENMUX_API_KEY`)
- **Qwen Portal** (supports `QWEN_OAUTH_TOKEN` or `QWEN_PORTAL_API_KEY`)
- **Cloudflare AI Gateway** (requires `CLOUDFLARE_AI_GATEWAY_API_KEY` and provider-specific gateway base URL)
- **Ollama** (local OpenAI-compatible runtime; optional `OLLAMA_API_KEY`)
- **llama.cpp** (local OpenAI and Anthropic compatible inference server)
- **vLLM** (OpenAI-compatible server; `VLLM_API_KEY` for secured deployments)
- **GitHub Copilot** (requires OAuth, see below)
- **Google Gemini CLI** (requires OAuth, see below)
- **Antigravity** (requires OAuth, see below)
- **Any OpenAI-compatible API**: LM Studio, custom proxies, etc.

## Installation

```bash
npm install @oh-my-pi/pi-ai
```

## Quick Start

```typescript
import { Type, getModel, stream, complete, Context, Tool, StringEnum } from "@oh-my-pi/pi-ai";

// Fully typed with auto-complete support for both providers and models
const model = getModel("openai", "gpt-4o-mini");

// Define tools with TypeBox schemas for type safety and validation
const tools: Tool[] = [
	{
		name: "get_time",
		description: "Get the current time",
		parameters: Type.Object({
			timezone: Type.Optional(Type.String({ description: "Optional timezone (e.g., America/New_York)" })),
		}),
	},
];

// Build a conversation context (easily serializable and transferable between models)
const context: Context = {
	systemPrompt: "You are a helpful assistant.",
	messages: [{ role: "user", content: "What time is it?" }],
	tools,
};

// Option 1: Streaming with all event types
const s = stream(model, context);

for await (const event of s) {
	switch (event.type) {
		case "start":
			console.log(`Starting with ${event.partial.model}`);
			break;
		case "text_start":
			console.log("\n[Text started]");
			break;
		case "text_delta":
			process.stdout.write(event.delta);
			break;
		case "text_end":
			console.log("\n[Text ended]");
			break;
		case "thinking_start":
			console.log("[Model is thinking...]");
			break;
		case "thinking_delta":
			process.stdout.write(event.delta);
			break;
		case "thinking_end":
			console.log("[Thinking complete]");
			break;
		case "toolcall_start":
			console.log(`\n[Tool call started: index ${event.contentIndex}]`);
			break;
		case "toolcall_delta":
			// Partial tool arguments are being streamed
			const partialCall = event.partial.content[event.contentIndex];
			if (partialCall.type === "toolCall") {
				console.log(`[Streaming args for ${partialCall.name}]`);
			}
			break;
		case "toolcall_end":
			console.log(`\nTool called: ${event.toolCall.name}`);
			console.log(`Arguments: ${JSON.stringify(event.toolCall.arguments)}`);
			break;
		case "done":
			console.log(`\nFinished: ${event.reason}`);
			break;
		case "error":
			console.error(`Error: ${event.error}`);
			break;
	}
}

// Get the final message after streaming, add it to the context
const finalMessage = await s.result();
context.messages.push(finalMessage);

// Handle tool calls if any
const toolCalls = finalMessage.content.filter((b) => b.type === "toolCall");
for (const call of toolCalls) {
	// Execute the tool
	const result =
		call.name === "get_time"
			? new Date().toLocaleString("en-US", {
					timeZone: call.arguments.timezone || "UTC",
					dateStyle: "full",
					timeStyle: "long",
				})
			: "Unknown tool";

	// Add tool result to context (supports text and images)
	context.messages.push({
		role: "toolResult",
		toolCallId: call.id,
		toolName: call.name,
		content: [{ type: "text", text: result }],
		isError: false,
		timestamp: Date.now(),
	});
}

// Continue if there were tool calls
if (toolCalls.length > 0) {
	const continuation = await complete(model, context);
	context.messages.push(continuation);
	console.log("After tool execution:", continuation.content);
}

console.log(`Total tokens: ${finalMessage.usage.input} in, ${finalMessage.usage.output} out`);
console.log(`Cost: $${finalMessage.usage.cost.total.toFixed(4)}`);

// Option 2: Get complete response without streaming
const response = await complete(model, context);

for (const block of response.content) {
	if (block.type === "text") {
		console.log(block.text);
	} else if (block.type === "toolCall") {
		console.log(`Tool: ${block.name}(${JSON.stringify(block.arguments)})`);
	}
}
```

## Tools

Tools enable LLMs to interact with external systems. This library uses TypeBox schemas for type-safe tool definitions with automatic validation using AJV. TypeBox schemas can be serialized and deserialized as plain JSON, making them ideal for distributed systems.

### Defining Tools

```typescript
import { Type, Tool, StringEnum } from "@oh-my-pi/pi-ai";

// Define tool parameters with TypeBox
const weatherTool: Tool = {
	name: "get_weather",
	description: "Get current weather for a location",
	parameters: Type.Object({
		location: Type.String({ description: "City name or coordinates" }),
		units: StringEnum(["celsius", "fahrenheit"], { default: "celsius" }),
	}),
};

// Note: For Google API compatibility, use StringEnum helper instead of Type.Enum
// Type.Enum generates anyOf/const patterns that Google doesn't support

const bookMeetingTool: Tool = {
	name: "book_meeting",
	description: "Schedule a meeting",
	parameters: Type.Object({
		title: Type.String({ minLength: 1 }),
		startTime: Type.String({ format: "date-time" }),
		endTime: Type.String({ format: "date-time" }),
		attendees: Type.Array(Type.String({ format: "email" }), { minItems: 1 }),
	}),
};
```

### Handling Tool Calls

Tool results use content blocks and can include both text and images:

```typescript
import * as fs from "node:fs";

const context: Context = {
	messages: [{ role: "user", content: "What is the weather in London?" }],
	tools: [weatherTool],
};

const response = await complete(model, context);

// Check for tool calls in the response
for (const block of response.content) {
	if (block.type === "toolCall") {
		// Execute your tool with the arguments
		// See "Validating Tool Arguments" section for validation
		const result = await executeWeatherApi(block.arguments);

		// Add tool result with text content
		context.messages.push({
			role: "toolResult",
			toolCallId: block.id,
			toolName: block.name,
			content: [{ type: "text", text: JSON.stringify(result) }],
			isError: false,
			timestamp: Date.now(),
		});
	}
}

// Tool results can also include images (for vision-capable models)
const imageBuffer = fs.readFileSync("chart.png");
context.messages.push({
	role: "toolResult",
	toolCallId: "tool_xyz",
	toolName: "generate_chart",
	content: [
		{ type: "text", text: "Generated chart showing temperature trends" },
		{ type: "image", data: imageBuffer.toBase64(), mimeType: "image/png" },
	],
	isError: false,
	timestamp: Date.now(),
});
```

### Streaming Tool Calls with Partial JSON

During streaming, tool call arguments are progressively parsed as they arrive. This enables real-time UI updates before the complete arguments are available:

```typescript
const s = stream(model, context);

for await (const event of s) {
	if (event.type === "toolcall_delta") {
		const toolCall = event.partial.content[event.contentIndex];

		// toolCall.arguments contains partially parsed JSON during streaming
		// This allows for progressive UI updates
		if (toolCall.type === "toolCall" && toolCall.arguments) {
			// BE DEFENSIVE: arguments may be incomplete
			// Example: Show file path being written even before content is complete
			if (toolCall.name === "write_file" && toolCall.arguments.path) {
				console.log(`Writing to: ${toolCall.arguments.path}`);

				// Content might be partial or missing
				if (toolCall.arguments.content) {
					console.log(`Content preview: ${toolCall.arguments.content.substring(0, 100)}...`);
				}
			}
		}
	}

	if (event.type === "toolcall_end") {
		// Here toolCall.arguments is complete (but not yet validated)
		const toolCall = event.toolCall;
		console.log(`Tool completed: ${toolCall.name}`, toolCall.arguments);
	}
}
```

**Important notes about partial tool arguments:**

- During `toolcall_delta` events, `arguments` contains the best-effort parse of partial JSON
- Fields may be missing or incomplete - always check for existence before use
- String values may be truncated mid-word
- Arrays may be incomplete
- Nested objects may be partially populated
- At minimum, `arguments` will be an empty object `{}`, never `undefined`
- The Google provider does not support function call streaming. Instead, you will receive a single `toolcall_delta` event with the full arguments.

### Validating Tool Arguments

When using `agentLoop`, tool arguments are automatically validated against your TypeBox schemas before execution. If validation fails, the error is returned to the model as a tool result, allowing it to retry.

When implementing your own tool execution loop with `stream()` or `complete()`, use `validateToolCall` to validate arguments before passing them to your tools:

```typescript
import { stream, validateToolCall, Tool } from "@oh-my-pi/pi-ai";

const tools: Tool[] = [weatherTool, calculatorTool];
const s = stream(model, { messages, tools });

for await (const event of s) {
	if (event.type === "toolcall_end") {
		const toolCall = event.toolCall;

		try {
			// Validate arguments against the tool's schema (throws on invalid args)
			const validatedArgs = validateToolCall(tools, toolCall);
			const result = await executeMyTool(toolCall.name, validatedArgs);
			// ... add tool result to context
		} catch (error) {
			// Validation failed - return error as tool result so model can retry
			context.messages.push({
				role: "toolResult",
				toolCallId: toolCall.id,
				toolName: toolCall.name,
				content: [{ type: "text", text: error.message }],
				isError: true,
				timestamp: Date.now(),
			});
		}
	}
}
```

### Complete Event Reference

All streaming events emitted during assistant message generation:

| Event Type       | Description              | Key Properties                                                                              |
| ---------------- | ------------------------ | ------------------------------------------------------------------------------------------- |
| `start`          | Stream begins            | `partial`: Initial assistant message structure                                              |
| `text_start`     | Text block starts        | `contentIndex`: Position in content array                                                   |
| `text_delta`     | Text chunk received      | `delta`: New text, `contentIndex`: Position                                                 |
| `text_end`       | Text block complete      | `content`: Full text, `contentIndex`: Position                                              |
| `thinking_start` | Thinking block starts    | `contentIndex`: Position in content array                                                   |
| `thinking_delta` | Thinking chunk received  | `delta`: New text, `contentIndex`: Position                                                 |
| `thinking_end`   | Thinking block complete  | `content`: Full thinking, `contentIndex`: Position                                          |
| `toolcall_start` | Tool call begins         | `contentIndex`: Position in content array                                                   |
| `toolcall_delta` | Tool arguments streaming | `delta`: JSON chunk, `partial.content[contentIndex].arguments`: Partial parsed args         |
| `toolcall_end`   | Tool call complete       | `toolCall`: Complete validated tool call with `id`, `name`, `arguments`                     |
| `done`           | Stream complete          | `reason`: Stop reason ("stop", "length", "toolUse"), `message`: Final assistant message     |
| `error`          | Error occurred           | `reason`: Error type ("error" or "aborted"), `error`: AssistantMessage with partial content |

## Image Input

Models with vision capabilities can process images. You can check if a model supports images via the `input` property. If you pass images to a non-vision model, they are silently ignored.

```typescript
import * as fs from 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
