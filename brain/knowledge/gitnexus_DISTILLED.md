---
id: gitnexus
type: knowledge
owner: OA_Triage
---
# gitnexus
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "gitnexus-monorepo",
  "private": true,
  "scripts": {
    "prepare": "husky",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "lint": "eslint .",
    "lint:fix": "eslint --fix ."
  },
  "devDependencies": {
    "@typescript-eslint/eslint-plugin": "^8.57.2",
    "@typescript-eslint/parser": "^8.57.2",
    "eslint": "^9.39.4",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-unused-imports": "^4.4.1",
    "husky": "^9.1.7",
    "lint-staged": "^15.5.0",
    "prettier": "^3.8.0",
    "prettier-plugin-tailwindcss": "^0.7.0"
  },
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{js,jsx,mjs,json,css,yml,yaml}": "prettier --write"
  }
}

```

### File: README.md
```md
# GitNexus
⚠️ Important Notice:** GitNexus has NO official cryptocurrency, token, or coin. Any token/coin using the GitNexus name on Pump.fun or any other platform is **not affiliated with, endorsed by, or created by** this project or its maintainers. Do not purchase any cryptocurrency claiming association with GitNexus.

<div align="center">

  <a href="https://trendshift.io/repositories/19809" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/19809" alt="abhigyanpatwari%2FGitNexus | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>

  <h2>Join the official Discord to discuss ideas, issues etc!</h2>

  <a href="https://discord.gg/AAsRVT6fGb">
    <img src="https://img.shields.io/discord/1477255801545429032?color=5865F2&logo=discord&logoColor=white" alt="Discord"/>
  </a>
  <a href="https://www.npmjs.com/package/gitnexus">
    <img src="https://img.shields.io/npm/v/gitnexus.svg" alt="npm version"/>
  </a>
  <a href="https://polyformproject.org/licenses/noncommercial/1.0.0/">
    <img src="https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg" alt="License: PolyForm Noncommercial"/>
  </a>

  <p><strong>Enterprise (SaaS & Self-hosted)</strong> - <a href="https://akonlabs.com">akonlabs.com</a></p>

</div>

**Building nervous system for agent context.**

Indexes any codebase into a knowledge graph — every dependency, call chain, cluster, and execution flow — then exposes it through smart tools so AI agents never miss code.




https://github.com/user-attachments/assets/172685ba-8e54-4ea7-9ad1-e31a3398da72



> *Like DeepWiki, but deeper.* DeepWiki helps you *understand* code. GitNexus lets you *analyze* it — because a knowledge graph tracks every relationship, not just descriptions.

**TL;DR:** The **Web UI** is a quick way to chat with any repo. The **CLI + MCP** is how you make your AI agent actually reliable — it gives Cursor, Claude Code, Codex, and friends a deep architectural view of your codebase so they stop missing dependencies, breaking call chains, and shipping blind edits. Even smaller models get full architectural clarity, making it compete with goliath models.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=abhigyanpatwari/GitNexus&type=date&legend=top-left)](https://www.star-history.com/#abhigyanpatwari/GitNexus&type=date&legend=top-left)


## Two Ways to Use GitNexus

|                   | **CLI + MCP**                                            | **Web UI**                                             |
| ----------------- | -------------------------------------------------------------- | ------------------------------------------------------------ |
| **What**    | Index repos locally, connect AI agents via MCP                 | Visual graph explorer + AI chat in browser                   |
| **For**     | Daily development with Cursor, Claude Code, Codex, Windsurf, OpenCode | Quick exploration, demos, one-off analysis                   |
| **Scale**   | Full repos, any size                                           | Limited by browser memory (~5k files), or unlimited via backend mode |
| **Install** | `npm install -g gitnexus`                                    | No install —[gitnexus.vercel.app](https://gitnexus.vercel.app) |
| **Storage** | LadybugDB native (fast, persistent)                               | LadybugDB WASM (in-memory, per session)                         |
| **Parsing** | Tree-sitter native bindings                                    | Tree-sitter WASM                                             |
| **Privacy** | Everything local, no network                                   | Everything in-browser, no server                             |

> **Bridge mode:** `gitnexus serve` connects the two — the web UI auto-detects the local server and can browse all your CLI-indexed repos without re-uploading or re-indexing.

---

## Enterprise

GitNexus is available as an **enterprise offering** - either as a fully managed **SaaS** or a **self-hosted** deployment. Also available for **commercial use** of the OSS version with proper licensing.

Enterprise includes:
- **PR Review** - automated blast radius analysis on pull requests
- **Auto-updating Code Wiki** - always up-to-date documentation (Code Wiki is also available in OSS)
- **Auto-reindexing** - knowledge graph stays fresh automatically
- **Multi-repo support** - unified graph across repositories
- **OCaml support** - additional language coverage
- **Priority feature/language support** - request new languages or features

**Upcoming:**
- Auto regression forensics
- End-to-end test generation

👉 Learn more at [akonlabs.com](https://akonlabs.com)

💬 For commercial licensing or enterprise inquiries, ping us on [Discord](https://discord.gg/AAsRVT6fGb) or drop an email at founders@akonlabs.com

---

## Development

- [ARCHITECTURE.md](ARCHITECTURE.md) — packages, index → graph → MCP flow, where to change code
- [RUNBOOK.md](RUNBOOK.md) — analyze, embeddings, stale index, MCP recovery, CI snippets
- [GUARDRAILS.md](GUARDRAILS.md) — safety rules and operational “Signs” for contributors and agents
- [CONTRIBUTING.md](CONTRIBUTING.md) — license, setup, commits, and pull requests
- [TESTING.md](TESTING.md) — test commands for `gitnexus` and `gitnexus-web`

## CLI + MCP (recommended)

The CLI indexes your repository and runs an MCP server that gives AI agents deep codebase awareness.

### Quick Start

```bash
# Index your repo (run from repo root)
npx gitnexus analyze
```

That's it. This indexes the codebase, installs agent skills, registers Claude Code hooks, and creates `AGENTS.md` / `CLAUDE.md` context files — all in one command.

To configure MCP for your editor, run `npx gitnexus setup` once — or set it up manually below.

### MCP Setup

`gitnexus setup` auto-detects your editors and writes the correct global MCP config. You only need to run it once.

### Editor Support

| Editor                | MCP | Skills | Hooks (auto-augment) | Support        |
| --------------------- | --- | ------ | -------------------- | -------------- |
| **Claude Code** | Yes | Yes    | Yes (PreToolUse + PostToolUse) | **Full** |
| **Cursor**      | Yes | Yes    | —                   | MCP + Skills   |
| **Codex**       | Yes | Yes    | —                   | MCP + Skills   |
| **Windsurf**    | Yes | —     | —                   | MCP            |
| **OpenCode**    | Yes | Yes    | —                   | MCP + Skills   |
| **Codex**       | Yes | —     | —                   | MCP            |

> **Claude Code** gets the deepest integration: MCP tools + agent skills + PreToolUse hooks that enrich searches with graph context + PostToolUse hooks that auto-reindex after commits.

## Community Integrations

Built by the community — not officially maintained, but worth checking out.

| Project | Author | Description |
|---------|--------|-------------|
| [pi-gitnexus](https://github.com/tintinweb/pi-gitnexus) | [@tintinweb](https://github.com/tintinweb) | GitNexus plugin for [pi](https://pi.dev) — `pi install npm:pi-gitnexus` |
| [gitnexus-stable-ops](https://github.com/ShunsukeHayashi/gitnexus-stable-ops) | [@ShunsukeHayashi](https://github.com/ShunsukeHayashi) | Stable ops & deployment workflows (Miyabi ecosystem) |

> Have a project built on GitNexus? Open a PR to add it here!

If you prefer manual configuration:

**Claude Code** (full support — MCP + skills + hooks):

```bash
# macOS / Linux
claude mcp add gitnexus -- npx -y gitnexus@latest mcp

# Windows
claude mcp add gitnexus -- cmd /c npx -y gitnexus@latest mcp
```

**Codex** (full support — MCP + skills):

```bash
codex mcp add gitnexus -- npx -y gitnexus@latest mcp
```

**Cursor** (`~/.cursor/mcp.json` — global, works for all projects):

```json
{
  "mcpServers": {
    "gitnexus": {
      "command": "npx",
      "args": ["-y", "gitnexus@latest", "mcp"]
    }
  }
}
```

**OpenCode** (`~/.config/opencode/config.json`):

```json
{
  "mcp": {
    "gitnexus": {
      "type": "local",
      "command": ["gitnexus", "mcp"]
    }
  }
}
```

**Codex** (`~/.codex/config.toml` for system scope, or `.codex/config.toml` for project scope):

```toml
[mcp_servers.gitnexus]
command = "npx"
args = ["-y", "gitnexus@latest", "mcp"]
```

### CLI Commands

```bash
gitnexus setup                   # Configure MCP for your editors (one-time)
gitnexus analyze [path]          # Index a repository (or update stale index)
gitnexus analyze --force         # Force full re-index
gitnexus analyze --skills        # Generate repo-specific skill files from detected communities
gitnexus analyze --skip-embeddings  # Skip embedding generation (faster)
gitnexus analyze --skip-agents-md  # Preserve custom AGENTS.md/CLAUDE.md gitnexus section edits
gitnexus analyze --embeddings    # Enable embedding generation (slower, better search)
gitnexus analyze --verbose       # Log skipped files when parsers are unavailable
gitnexus mcp                     # Start MCP server (stdio) — serves all indexed repos
gitnexus serve                   # Start local HTTP server (multi-repo) for web UI connection
gitnexus list                    # List all indexed repositories
gitnexus status                  # Show index status for current repo
gitnexus clean                   # Delete index for current repo
gitnexus clean --all --force     # Delete all indexes
gitnexus wiki [path]             # Generate repository wiki from knowledge graph
gitnexus wiki --model <model>    # Wiki with custom LLM model (default: gpt-4o-mini)
gitnexus wiki --base-url <url>   # Wiki with custom LLM API base URL

# Repository groups (multi-repo / monorepo service tracking)
gitnexus group create <name>     # Create a repository group
gitnexus group add <name> <repo> # Add a repo to a group
gitnexus group remove <name> <repo> # Remove a repo from a group
gitnexus group list [name]       # List groups, or show one group's config
gitnexus group sync <name>       # Extract contracts and match across repos/services
gitnexus group contracts <name>  # Inspect extracted contracts and cross-links
gitnexus group query <name> <q>  # Search execution flows across all repos in a group
gitnexus group status <name>     # Check staleness of repos in a group
```

### What Your AI Agent Gets

**16 tools** exposed via MCP (11 per-repo + 5 group):

| Tool               | What It Does                                                      | `repo` Param |
| ------------------ | ----------------------------------------------------------------- | -------------- |
| `list_repos`     | Discover all indexed repositories                                 | —             |
| `query`          | Process-grouped hybrid search (BM25 + semantic + RRF)             | Optional       |
| `context`        | 360-degree symbol view — categorized refs, process participation | Optional       |
| `impact`         | Blast radius analysis with depth grouping and confidence          | Optional       |
| `detect_changes` | Git-diff impact — maps changed lines to affected processes       | Optional       |
| `rename`         | Multi-file coordinated rename with graph + text search            | Optional       |
| `cypher`         | Raw Cypher graph queries                                          | Optional       |
| `group_list`     | List configured repository groups                                 | —             |
| `group_sync`     | Extract contracts and match across repos/services                 | —             |
| `group_contracts`| Inspect extracted contracts and cross-links                       | —             |
| `group_query`    | Search execution flows across all repos in a group                | —             |
| `group_status`   | Check staleness of repos in a group                               | —             |

> When only one repo is indexed, the `repo` parameter is optional. With multiple repos, specify which one: `query({query: "auth", repo: "my-app"})`.

**Resources** for instant context:

| Resource                                  | Purpose                                              |
| ----------------------------------------- | ---------------------------------------------------- |
| `gitnexus://repos`                      | List all indexed repositories (read this first)      |
| `gitnexus://repo/{name}/context`        | Codebase stats, staleness check, and available tools |
| `gitnexus://repo/{name}/clusters`       | All functional clusters with cohesion scores         |
| `gitnexus://repo/{name}/cluster/{name}` | Cluster members and details                          |
| `gitnexus://repo/{name}/processes`      | All execution flows                                  |
| `gitnexus://repo/{name}/process/{name}` | Full process trace with steps                        |
| `gitnexus://repo/{name}/schema`         | Graph schema for Cypher queries                      |

**2 MCP prompts** for guided workflows:

| Prompt            | What It Does                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| `detect_impact` | Pre-commit change analysis — scope, affected processes, risk level       |
| `generate_map`  | Architecture documentation from the knowledge graph with mermaid diagrams |

**4 agent skills** installed to `.claude/skills/` automatically:

- **Exploring** — Navigate unfamiliar code using the knowledge graph
- **Debugging** — Trace bugs through call chains
- **Impact Analysis** — Analyze blast radius before changes
- **Refactoring** — Plan safe refactors using dependency mapping

**Repo-specific skills** generated with `--skills`:

When you run `gitnexus analyze --skills`, GitNexus detects the functional areas of your codebase (via Leiden community detection) and generates a `SKILL.md` file for each one under `.claude/skills/generated/`. Each skill describes a module's key files, entry points, execution flows, and cross-area connections — so your AI agent gets targeted context for the exact area of code you're working in. Skills are regenerated on each `--skills` run to stay current with the codebase.

---

## Multi-Repo MCP Architecture

GitNexus uses a **global registry** so one MCP server can serve multiple indexed repos. No per-project MCP config needed — set it up once and it works everywhere.

```mermaid
flowchart TD
    subgraph CLI [CLI Commands]
        Setup["gitnexus setup"]
        Analyze["gitnexus analyze"]
        Clean["gitnexus clean"]
        List["gitnexus list"]
    end

    subgraph Registry ["~/.gitnexus/"]
        RegFile["registry.json"]
    end

    subgraph Repos [Project Repos]
        RepoA[".gitnexus/ in repo A"]
        RepoB[".gitnexus/ in repo B"]
    end

    subgraph MCP [MCP Server]
        Server["server.ts"]
        Backend["LocalBackend"]
        Pool["Connection Pool"]
        ConnA["LadybugDB conn A"]
        ConnB["LadybugDB conn B"]
    end

    Setup -->|"
... [TRUNCATED]
```

### File: eval\README.md
```md
# GitNexus SWE-bench Evaluation Harness

Evaluate whether GitNexus code intelligence improves AI agent performance on real software engineering tasks. Runs SWE-bench instances across multiple models and compares baseline (no graph) vs GitNexus-enhanced configurations.

## What This Tests

**Hypothesis**: Giving AI agents structural code intelligence (call graphs, execution flows, blast radius analysis) improves their ability to resolve real GitHub issues — measured by resolve rate, cost, and efficiency.

**Evaluation modes:**

| Mode | What the agent gets |
|------|-------------------|
| `baseline` | Standard bash tools (grep, find, cat, sed) — control group |
| `native` | Baseline + explicit GitNexus tools via eval-server (~100ms) |
| `native_augment` | Native tools + grep results automatically enriched with graph context (**recommended**) |

> **Recommended**: Use `native_augment` mode. It mirrors the Claude Code model — the agent gets both explicit GitNexus tools (fast bash commands) AND automatic enrichment of grep results with callers, callees, and execution flows. The agent decides when to use explicit tools vs rely on enriched search output.

**Models supported:**

- Claude 3.5 Haiku, Claude Sonnet 4, Claude Opus 4
- MiniMax M1 2.5
- GLM 4.7, GLM 5
- Any model supported by litellm (add a YAML config)

## Prerequisites

- Python 3.11+
- Docker (for SWE-bench containers)
- Node.js 18+ (for GitNexus)
- API keys for your chosen models

## Setup

```bash
cd eval

# Install dependencies
pip install -e .

# Set up API keys — copy the template and fill in your keys
cp .env.example .env
# Then edit .env and paste your key(s)
```

All models are routed through **OpenRouter** by default, so a single `OPENROUTER_API_KEY` is all you need. To use provider APIs directly (Anthropic, ZhipuAI, etc.), edit the model YAML in `configs/models/` and set the corresponding key in `.env`.

```bash
# Pull SWE-bench Docker images (pulled on-demand, but you can pre-pull)
docker pull swebench/sweb.eval.x86_64.django_1776_django-16527:latest
```

### Debug logging

Set `GITNEXUS_EVAL_DEBUG=1` to include full Python tracebacks in run summaries and logs. By default, errors are sanitized to avoid leaking host paths or stack traces.

## Quick Start

### Debug a single instance

```bash
# Fastest way to verify everything works
python run_eval.py debug -m claude-haiku -i django__django-16527 --subset lite
```

### Run a single configuration

```bash
# 5 instances, Claude Sonnet, native_augment mode (default)
python run_eval.py single -m claude-sonnet --subset lite --slice 0:5

# Baseline comparison (no GitNexus)
python run_eval.py single -m claude-sonnet --mode baseline --subset lite --slice 0:5

# Full Lite benchmark, 4 parallel workers
python run_eval.py single -m claude-sonnet --subset lite -w 4
```

### Run the full matrix

```bash
# All models x all modes
python run_eval.py matrix --subset lite -w 4

# Key comparison: baseline vs native_augment
python run_eval.py matrix -m claude-sonnet -m claude-haiku --modes baseline --modes native_augment --subset lite --slice 0:50
```

### Analyze results

```bash
# Summary table
python -m analysis.analyze_results results/

# Compare modes for a specific model
python -m analysis.analyze_results compare-modes results/ -m claude-sonnet

# GitNexus tool usage analysis
python -m analysis.analyze_results gitnexus-usage results/

# Export as CSV for further analysis
python -m analysis.analyze_results summary results/ --format csv > results.csv

# Run official SWE-bench test evaluation
python -m analysis.analyze_results summary results/ --swebench-eval
```

### List available configurations

```bash
python run_eval.py list-configs
```

## Architecture

```
eval/
  run_eval.py              # Main entry point (single, matrix, debug commands)
  agents/
    gitnexus_agent.py      # GitNexusAgent: extends DefaultAgent with augmentation + metrics
  environments/
    gitnexus_docker.py     # Docker env with GitNexus + eval-server + standalone tool scripts
  bridge/
    gitnexus_tools.sh      # Bash wrappers (legacy — now standalone scripts are installed directly)
    mcp_bridge.py          # Legacy MCP bridge (kept for reference)
  prompts/
    system_baseline.jinja          # System: persona + format rules
    instance_baseline.jinja        # Instance: task + workflow
    system_native.jinja            # System: + GitNexus tool reference
    instance_native.jinja          # Instance: + GitNexus debugging workflow
    system_native_augment.jinja    # System: + GitNexus tools + grep enrichment docs
    instance_native_augment.jinja  # Instance: + GitNexus workflow + risk assessment
  configs/
    models/                # Per-model YAML configs
    modes/                 # Per-mode YAML configs (baseline, native, native_augment)
  analysis/
    analyze_results.py     # Post-run comparative analysis
  results/                 # Output directory (gitignored)
```

## How It Works

### Template structure

mini-swe-agent requires two Jinja templates:
- **system_template** → system message: persona, format rules, tool reference (static)
- **instance_template** → first user message: task, workflow, rules, examples (contains `{{task}}`)

Each mode has a `system_{mode}.jinja` + `instance_{mode}.jinja` pair. The agent loads both automatically based on the configured mode.

### Per-instance flow

1. Docker container starts with SWE-bench instance (repo at specific commit)
2. **GitNexus setup**: Node.js + gitnexus installed, `gitnexus analyze` runs (or restores from cache)
3. **Eval-server starts**: `gitnexus eval-server` daemon (persistent HTTP server, keeps LadybugDB warm)
4. **Standalone tool scripts installed** in `/usr/local/bin/` — works with `subprocess.run` (no `.bashrc` needed)
5. Agent runs with the configured model + system prompt + GitNexus tools
6. Agent's patch is extracted as a git diff
7. Metrics collected: cost, tokens, tool calls, GitNexus usage, augmentation stats

### Tool architecture

```
Agent → bash command → /usr/local/bin/gitnexus-query
  → curl localhost:4848/tool/query     (fast path: eval-server, ~100ms)
  → npx gitnexus query                 (fallback: cold CLI, ~5-10s)
```

Each tool script in `/usr/local/bin/` is standalone — no sourcing, no env inheritance needed. This is critical because mini-swe-agent runs every command via `subprocess.run` in a fresh subshell.

### Eval-server

The eval-server is a lightweight HTTP daemon that:
- Keeps LadybugDB warm in memory (no cold start per tool call)
- Returns LLM-friendly text (not raw JSON — saves tokens)
- Includes next-step hints to guide tool chaining (query → context → impact → fix)
- Auto-shuts down after idle timeout

### Index caching

SWE-bench repos repeat (Django has 200+ instances at different commits). The harness caches GitNexus indexes per `(repo, commit)` hash in `~/.gitnexus-eval-cache/` to avoid redundant re-indexing.

### Grep augmentation (native_augment mode)

When the agent runs `grep` or `rg`, the observation is post-processed: the agent class calls `gitnexus-augment` on the search pattern and appends `[GitNexus]` annotations showing callers, callees, and execution flows for matched symbols. This mirrors the Claude Code / Cursor hook integration.

## Adding Models

Create a YAML file in `configs/models/`:

```yaml
# configs/models/my-model.yaml
model:
  model_name: "openrouter/provider/model-name"
  cost_tracking: "ignore_errors"  # if not in litellm's cost DB
  model_kwargs:
    max_tokens: 8192
    temperature: 0
```

The model name follows [litellm conventions](https://docs.litellm.ai/docs/providers).

## Metrics Collected

| Metric | Description |
|--------|-------------|
| Patch Rate | % of instances where agent produced a patch |
| Resolve Rate | % of instances where patch passes tests (requires --swebench-eval) |
| Total Cost | API cost across all instances |
| Avg Cost/Instance | Cost efficiency |
| API Calls | Number of LLM calls |
| GN Tool Calls | How many GitNexus tools the agent used |
| Augment Hits | How many grep/find results got enriched |
| Augment Hit Rate | % of search commands that got useful enrichment |

```

### File: .github\scripts\triage\requirements.txt
```txt
fastembed>=0.5.0
numpy>=1.26.0
scikit-learn>=1.4.0
scipy>=1.10.0

```

### File: .mcp.json
```json
{
  "mcpServers": {
    "gitnexus": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "gitnexus@latest", "mcp"]
    }
  }
}

```

### File: AGENTS.md
```md
<!-- version: 1.2.0 -->
<!--
  Metadata: version, last reviewed, scope, model policy, reference docs, changelog.
  Last updated: 2026-03-22
-->

Last reviewed: 2026-03-24

**Project:** GitNexus · **Environment:** dev · **Maintainer:** repository maintainers (see GitHub)

This file uses a standard agent header (version, scope, model policy, reference docs, changelog), adapted for this **TypeScript/JavaScript monorepo**.

## Scope

| | |
|--|--|
| **Reads** | Repository tree as needed for the task: `gitnexus/`, `gitnexus-web/`, `eval/`, plugin packages, `.github/`, `.gitnexus/` when present, and docs. |
| **Writes** | Only paths required for the requested change; keep diffs minimal. Update lockfiles when dependencies change. |
| **Executes** | `npm`, `npx`, `node` under `gitnexus/` and `gitnexus-web/`; `uv run` for Python under `eval/` when applicable; shell utilities for documented CI/dev workflows. |
| **Off-limits** | User secrets (e.g. real `.env`), production deployment credentials, unrelated repositories, destructive git history operations without explicit human confirmation. |

## Model Configuration

- **Primary:** Pin in **Cursor** (Settings → model). Use a **named** model (e.g. GPT-5.2, Claude Sonnet 4.x). Avoid relying on **Auto** when reproducibility or audit trail matters.
- **Fallback:** As configured in Cursor or your organization (do not encode `latest` or wildcards in automation configs).
- **Notes:** The open-source GitNexus CLI indexer does not call an LLM. Optional Nexus AI in the web UI uses end-user provider keys and models.

## Execution Sequence (complex tasks)

Long sessions dilute instructions. For **multi-step** work, state up front:

1. Which rules in this file and **[GUARDRAILS.md](GUARDRAILS.md)** apply (and any relevant Signs).
2. Current **Scope** boundaries (Reads / Writes / Off-limits).
3. Which **validation commands** you will run (e.g. `cd gitnexus && npm test`, `npx tsc --noEmit`).

On very long threads, the human may add *“Remember: apply all AGENTS.md rules”* to re-weight rule tokens against context dilution.

## Claude Code hooks

Hooks enforce gates that prompts cannot. In **Claude Code**, **PreToolUse** hooks can block tools such as `git_commit` until checks pass. Adapt to this repo: e.g. `cd gitnexus && npm test` before commit.

## Context budget (Cursor / standards)

Generic “core standards” playbooks are often long and stack-specific. For this monorepo, commands and gotchas live under **Cursor Cloud specific instructions** below and in **[CONTRIBUTING.md](CONTRIBUTING.md)**. If always-on rules grow, split domain rules into **`.cursor/rules/*.mdc`** (globs). **Cursor:** project-wide rules live in **`.cursor/index.mdc`** (YAML frontmatter with `alwaysApply: true`). **Claude Code:** optionally load a **`STANDARDS.md`** only when needed (e.g. *“When writing new code, read STANDARDS.md”*) to save context.

## Reference Documentation

- **This repository:** **[ARCHITECTURE.md](ARCHITECTURE.md)**, **[CONTRIBUTING.md](CONTRIBUTING.md)**, **[GUARDRAILS.md](GUARDRAILS.md)**.
- **Cursor:** `.cursor/index.mdc` (always-on rules); optional `.cursor/rules/*.mdc` (glob-scoped). Legacy `.cursorrules` is deprecated — see `.cursor/index.mdc`.
- **Optional local files:** `NOTES.md` (short vendor-neutral project snapshot). For handoffs, keep notes local (e.g., a scratch file outside the repo) rather than committing `HANDOFF.md`.
- **GitNexus:** skills under `.claude/skills/gitnexus/`; machine-oriented rules in the `gitnexus:start` … `gitnexus:end` block below.

## Changelog

| Date | Version | Change |
|------|---------|--------|
| 2026-03-24 | 1.2.0 | Fixed gitnexus:start block duplication (was inlined in Reference Docs bullet). |
| 2026-03-23 | 1.1.0 | Updated agent instructions (sections, references, Cursor layout). |
| 2026-03-22 | 1.0.0 | Added structured agent header and changelog. |

---

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **GitNexus** (3298 symbols, 7954 relationships, 185 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## When Debugging

1. `gitnexus_query({query: "<error or symptom>"})` — find execution flows related to the issue
2. `gitnexus_context({name: "<suspect function>"})` — see all callers, callees, and process participation
3. `READ gitnexus://repo/GitNexus/process/{processName}` — trace the full execution flow step by step
4. For regressions: `gitnexus_detect_changes({scope: "compare", base_ref: "main"})` — see what your branch changed

## When Refactoring

- **Renaming**: MUST use `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` first. Review the preview — graph edits are safe, text_search edits need manual review. Then run with `dry_run: false`.
- **Extracting/Splitting**: MUST run `gitnexus_context({name: "target"})` to see all incoming/outgoing refs, then `gitnexus_impact({target: "target", direction: "upstream"})` to find all external callers before moving code.
- After any refactor: run `gitnexus_detect_changes({scope: "all"})` to verify only expected files changed.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Tools Quick Reference

| Tool | When to use | Command |
|------|-------------|---------|
| `query` | Find code by concept | `gitnexus_query({query: "auth validation"})` |
| `context` | 360-degree view of one symbol | `gitnexus_context({name: "validateUser"})` |
| `impact` | Blast radius before editing | `gitnexus_impact({target: "X", direction: "upstream"})` |
| `detect_changes` | Pre-commit scope check | `gitnexus_detect_changes({scope: "staged"})` |
| `rename` | Safe multi-file rename | `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` |
| `cypher` | Custom graph queries | `gitnexus_cypher({query: "MATCH ..."})` |

## Impact Risk Levels

| Depth | Meaning | Action |
|-------|---------|--------|
| d=1 | WILL BREAK — direct callers/importers | MUST update these |
| d=2 | LIKELY AFFECTED — indirect deps | Should test |
| d=3 | MAY NEED TESTING — transitive | Test if critical path |

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/GitNexus/context` | Codebase overview, check index freshness |
| `gitnexus://repo/GitNexus/clusters` | All functional areas |
| `gitnexus://repo/GitNexus/processes` | All execution flows |
| `gitnexus://repo/GitNexus/process/{name}` | Step-by-step execution trace |

## Self-Check Before Finishing

Before completing any code modification task, verify:
1. `gitnexus_impact` was run for all modified symbols
2. No HIGH/CRITICAL risk warnings were ignored
3. `gitnexus_detect_changes()` confirms changes match expected scope
4. All d=1 (WILL BREAK) dependents were updated

## Keeping the Index Fresh

After committing code changes, the GitNexus index becomes stale. Re-run analyze to update it:

```bash
npx gitnexus analyze
```

If the index previously included embeddings, preserve them by adding `--embeddings`:

```bash
npx gitnexus analyze --embeddings
```

To check whether embeddings exist, inspect `.gitnexus/meta.json` — the `stats.embeddings` field shows the count (0 means no embeddings). **Running analyze without `--embeddings` will delete any previously generated embeddings.**

> Claude Code users: A PostToolUse hook handles this automatically after `git commit` and `git merge`.

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->

## Cursor Cloud specific instructions

### Repository structure

This is a monorepo with two main products and supporting config packages:

| Component | Path | Purpose |
|-----------|------|---------|
| **GitNexus CLI/Core** | `gitnexus/` | Main product — TypeScript CLI, indexing pipeline, MCP server. Published to npm. |
| **GitNexus Web UI** | `gitnexus-web/` | React/Vite browser app — graph explorer + AI chat. Runs entirely in WASM. |
| Claude Plugin | `gitnexus-claude-plugin/` | Static config for Claude marketplace (no build). |
| Cursor Integration | `gitnexus-cursor-integration/` | Static config for Cursor editor (no build). |
| SWE-bench Eval | `eval/` | Python evaluation harness (optional; needs Docker + LLM API keys). |

### Running services

- **CLI/Core**: `cd gitnexus && npm run dev` (tsx watch mode) or `npm run build && node dist/cli/index.js <command>`
- **Web UI**: `cd gitnexus-web && npm run dev` (Vite on port 5173)
- **Backend mode**: `cd <indexed-repo> && node /workspace/gitnexus/dist/cli/index.js serve` (HTTP API on port 3741 by default)

### Testing

**CLI / Core (`gitnexus/`)**
- **Unit tests**: `cd gitnexus && npm test` (vitest, ~2000 tests)
- **Integration tests**: `cd gitnexus && npm run test:integration` (vitest, ~1850 tests). Two LadybugDB file-locking tests (`lbug-core-adapter`, `search-core`) may fail in containerized environments due to `/tmp` locking limitations — this is a known environment issue, not a code bug.
- **TypeScript check**: `cd gitnexus && npx tsc --noEmit`

**Web UI (`gitnexus-web/`)**
- **Unit tests**: `cd gitnexus-web && npm test` (vitest, ~200 tests)
- **E2E tests**: `cd gitnexus-web && E2E=1 npx playwright test` (Playwright, 5 tests — requires `gitnexus serve` + `npm run dev` running)
- **TypeScript check**: `cd gitnexus-web && npx tsc -b --noEmit`

No separate lint command is configured; TypeScript strict checking serves as the primary static analysis.

### Gotchas

- `npm install` in `gitnexus/` triggers `prepare` (builds via `tsc`) and `postinstall` (patches tree-sitter-swift). Native tree-sitter bindings require `python3`, `make`, and `g++` to be present.
- `tree-sitter-kotlin` and `tree-sitter-swift` are optional dependencies — install warnings for these are expected and non-blocking.
- The Web UI uses `vite-plugin-wasm` and requires `Cross-Origin-Opener-Policy`/`Cross-Origin-Embedder-Policy` headers for `SharedArrayBuffer` (handled automatically by Vite dev server).
- There is no ESLint/Prettier configuration in this repo.

```

### File: ARCHITECTURE.md
```md
# Architecture — GitNexus

This repository is a **monorepo** with two main products: the **CLI / MCP package** (`gitnexus/`) and the **browser UI** (`gitnexus-web/`). Supporting folders ship editor integrations and plugins without changing the core graph engine.

## Repository layout

| Path | Role |
|------|------|
| `gitnexus/` | Published npm package `gitnexus`: CLI, MCP server (stdio), local HTTP API for bridge mode, ingestion pipeline, LadybugDB graph, embeddings (optional). |
| `gitnexus-web/` | Vite + React UI: in-browser indexing (WASM), graph visualization, optional connection to `gitnexus serve`. |
| `.claude/`, `gitnexus-claude-plugin/`, `gitnexus-cursor-integration/` | Packaged **skills** and plugin metadata so agents discover the same workflows as documented in `AGENTS.md`. |
| `eval/` | Evaluation harnesses and docs for benchmarking tool usage. |
| `.github/` | CI workflows (quality, unit, integration, E2E) and composite actions. |

## End-to-end flow: index → graph → tools

1. **Ingestion** (`gitnexus analyze`)  
   - Entry: `gitnexus/src/cli/analyze.ts` → `runPipelineFromRepo` in `gitnexus/src/core/ingestion/pipeline.ts`.  
   - Walks the git working tree, parses supported languages via **Tree-sitter**, resolves imports/calls/inheritance, detects **communities** and **processes** (execution flows), and builds an in-memory **knowledge graph** (`gitnexus/src/core/graph/`).  
   - Output is loaded into **LadybugDB** under **`.gitnexus/`** at the repo root (`lbug/`, `meta.json`, etc.). Optional **FTS** indexes and **embeddings** attach to the same store.  
   - The repo is registered in **`~/.gitnexus/registry.json`** so MCP can find it from any working directory.

2. **Persistence & metadata**  
   - `gitnexus/src/storage/repo-manager.ts` — paths, registry, cleanup of legacy Kuzu artifacts.  
   - `gitnexus/src/core/lbug/lbug-adapter.ts` — graph load, queries, embedding restore batches.

3. **Query & agents**  
   - **MCP (stdio):** `gitnexus/src/cli/mcp.ts` → `startMCPServer` → `LocalBackend` (`gitnexus/src/mcp/local/local-backend.ts`) opens registered repos and serves **tools** from `gitnexus/src/mcp/tools.ts` and **resources** from `gitnexus/src/mcp/resources.ts`.  
   - **Bridge HTTP:** `gitnexus/src/cli/serve.ts` → Express app in `gitnexus/src/server/api.ts` (CORS-limited) exposes REST + MCP-over-HTTP for the web UI.  
   - **CLI tools (no MCP):** `gitnexus query`, `context`, `impact`, `cypher` in `gitnexus/src/cli/tool.ts` call the same backend for scripts and CI.

4. **Staleness**  
   - `gitnexus/src/mcp/staleness.ts` compares indexed `lastCommit` to `HEAD` and surfaces hints when the graph is behind git.

## MCP tools (summary)

| Tool | Purpose |
|------|---------|
| `list_repos` | Discover indexed repositories when more than one is registered. |
| `query` | Natural-language / keyword search over the graph (hybrid BM25 + optional vectors). |
| `cypher` | Ad hoc **Cypher** against the schema (see resource `gitnexus://repo/{name}/schema`). |
| `context` | Callers, callees, processes for one symbol (with disambiguation). |
| `impact` | Blast radius (upstream/downstream) with depth and risk summary. |
| `detect_changes` | Map git diffs to affected symbols and processes. |
| `rename` | Graph-assisted rename with `dry_run` preview (`graph` vs `text_search` confidence). |

## Where to change what

| If you are changing… | Start in… |
|----------------------|-----------|
| CLI commands / flags | `gitnexus/src/cli/` (`index.ts`, per-command modules). |
| Parsing or graph construction | `gitnexus/src/core/ingestion/` (pipeline, processors, resolvers, type-extractors). |
| Graph schema / DB access | `gitnexus/src/core/lbug/` (`schema.ts`, `lbug-adapter.ts`), `gitnexus/src/mcp/core/lbug-adapter.ts` if MCP-specific. |
| MCP protocol, tools, resources | `gitnexus/src/mcp/server.ts`, `tools.ts`, `resources.ts`. |
| Search ranking | `gitnexus/src/core/search/` (BM25, hybrid fusion). |
| Embeddings | `gitnexus/src/core/embeddings/`, phases in `analyze.ts`. |
| Wiki generation | `gitnexus/src/core/wiki/`. |
| Web UI behavior | `gitnexus-web/src/` (components, workers, graph client). |
| CI | `.github/workflows/*.yml`, `.github/actions/setup-gitnexus/`. |

## Related docs

- [RUNBOOK.md](RUNBOOK.md) — operational commands and recovery.  
- [GUARDRAILS.md](GUARDRAILS.md) — safety boundaries for humans and agents.  
- [TESTING.md](TESTING.md) — how to run tests.  
- `AGENTS.md` / `CLAUDE.md` — agent workflows and tool usage expectations for **this** repo when indexed by GitNexus.

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to GitNexus will be documented in this file.

## [Unreleased]

### Changed
- Migrated from KuzuDB to LadybugDB v0.15 (`@ladybugdb/core`, `@ladybugdb/wasm-core`)
- Renamed all internal paths from `kuzu` to `lbug` (storage: `.gitnexus/kuzu` → `.gitnexus/lbug`)
- Added automatic cleanup of stale KuzuDB index files
- LadybugDB v0.15 requires explicit VECTOR extension loading for semantic search

## [1.5.3] - 2026-04-01

### Added

- **TypeScript/JavaScript MethodExtractor config** — shared extraction config covering abstract methods, visibility modifiers, async/override keywords, decorators, rest/optional/destructured parameters, and return types (#588) — @compound-ai

### Fixed

- **Azure OpenAI compatibility** — use `max_completion_tokens` instead of deprecated `max_tokens` (newer models reject `max_tokens`); skip `temperature` for Azure provider (some models reject non-default values) (#618)
- **Simplified Azure interactive setup** — 3 prompts (endpoint, deployment, key) instead of 7 (#618)
- **Wiki HTML viewer script injection** — escape `</script>` in embedded JSON so LLM-generated markdown no longer breaks the viewer (#618)
- Ensure import rewrites survive npm publish lifecycle

## [1.4.0] - 2026-03-13

### Added

- **Language-aware symbol resolution engine** with 3-tier resolver: exact FQN → scope-walk → guarded fuzzy fallback that refuses ambiguous matches (#238) — @magyargergo
- **Method Resolution Order (MRO)** with 5 language-specific strategies: C++ leftmost-base, C#/Java class-over-interface, Python C3 linearization, Rust qualified syntax, default BFS (#238) — @magyargergo
- **Constructor & struct literal resolution** across all languages — `new Foo()`, `User{...}`, C# primary constructors, target-typed new (#238) — @magyargergo
- **Receiver-constrained resolution** using per-file TypeEnv — disambiguates `user.save()` vs `repo.save()` via `ownerId` matching (#238) — @magyargergo
- **Heritage & ownership edges** — HAS_METHOD, OVERRIDES, Go struct embedding, Swift extension heritage, method signatures (`parameterCount`, `returnType`) (#238) — @magyargergo
- **Language-specific resolver directory** (`resolvers/`) — extracted JVM, Go, C#, PHP, Rust resolvers from monolithic import-processor (#238) — @magyargergo
- **Type extractor directory** (`type-extractors/`) — per-language type binding extraction with `Record<SupportedLanguages, Handler>` + `satisfies` dispatch (#238) — @magyargergo
- **Export detection dispatch table** — compile-time exhaustive `Record` + `satisfies` pattern replacing switch/if chains (#238) — @magyargergo
- **Language config module** (`language-config.ts`) — centralized tsconfig, go.mod, composer.json, .csproj, Swift package config loaders (#238) — @magyargergo
- **Optional skill generation** via `npx gitnexus analyze --skills` — generates AI agent skills from KuzuDB knowledge graph (#171) — @zander-raycraft
- **First-class C# support** — sibling-based modifier scanning, record/delegate/property/field/event declaration types (#163, #170, #178 via #237) — @Alice523, @benny-yamagata, @jnMetaCode
- **C/C++ support fixes** — `.h` → C++ mapping, static-linkage export detection, qualified/parenthesized declarators, 48 entry point patterns (#163, #227 via #237) — @Alice523, @bitgineer
- **Rust support fixes** — sibling-based `visibility_modifier` scanning for `pub` detection (#227 via #237) — @bitgineer
- **Adaptive tree-sitter buffer sizing** — `Math.min(Math.max(contentLength * 2, 512KB), 32MB)` (#216 via #237) — @JasonOA888
- **Call expression matching** in tree-sitter queries (#234 via #237) — @ex-nihilo-jg
- **DeepSeek model configurations** (#217) — @JasonOA888
- 282+ new unit tests, 178 integration resolver tests across 9 languages, 53 test files, 1146 total tests passing

### Fixed

- Skip unavailable native Swift parsers in sequential ingestion (#188) — @Gujiassh
- Heritage heuristic language-gated — no longer applies class/interface rules to wrong languages (#238) — @magyargergo
- C# `base_list` distinguishes EXTENDS vs IMPLEMENTS via symbol table + `I[A-Z]` heuristic (#238) — @magyargergo
- Go `qualified_type` (`models.User`) correctly unwrapped in TypeEnv (#238) — @magyargergo
- Global tier no longer blocks resolution when kind/arity filtering can narrow to 1 candidate (#238) — @magyargergo

### Changed

- `import-processor.ts` reduced from 1412 → 711 lines (50% reduction) via resolver and config extraction (#238) — @magyargergo
- `type-env.ts` reduced from 635 → ~125 lines via type-extractor extraction (#238) — @magyargergo
- CI/CD workflows hardened with security fixes and fork PR support (#222, #225) — @magyargergo

## [1.3.11] - 2026-03-08

### Security

- Fix FTS Cypher injection by escaping backslashes in search queries (#209) — @magyargergo

### Added

- Auto-reindex hook that runs `gitnexus analyze` after commits and merges, with automatic embeddings preservation (#205) — @L1nusB
- 968 integration tests (up from ~840) covering unhappy paths across search, enrichment, CLI, pipeline, worker pool, and KuzuDB (#209) — @magyargergo
- Coverage auto-ratcheting so thresholds bump automatically on CI (#209) — @magyargergo
- Rich CI PR report with coverage bars, test counts, and threshold tracking (#209) — @magyargergo
- Modular CI workflow architecture with separate unit-test, integration-test, and orchestrator jobs (#209) — @magyargergo

### Fixed

- KuzuDB native addon crashes on Linux/macOS by running integration tests in isolated vitest processes with `--pool=forks` (#209) — @magyargergo
- Worker pool `MODULE_NOT_FOUND` crash when script path is invalid (#209) — @magyargergo

### Changed

- Added macOS to the cross-platform CI test matrix (#208) — @magyargergo

## [1.3.10] - 2026-03-07

### Security

- **MCP transport buffer cap**: Added 10 MB `MAX_BUFFER_SIZE` limit to prevent out-of-memory attacks via oversized `Content-Length` headers or unbounded newline-delimited input
- **Content-Length validation**: Reject `Content-Length` values exceeding the buffer cap before allocating memory
- **Stack overflow prevention**: Replaced recursive `readNewlineMessage` with iterative loop to prevent stack overflow from consecutive empty lines
- **Ambiguous prefix hardening**: Tightened `looksLikeContentLength` to require 14+ bytes before matching, preventing false framing detection on short input
- **Closed transport guard**: `send()` now rejects with a clear error when called after `close()`, with proper write-error propagation

### Added

- **Dual-framing MCP transport** (`CompatibleStdioServerTransport`): Auto-detects Content-Length (Codex/OpenCode) and newline-delimited JSON (Cursor/Claude Code) framing on the first message, responds in the same format (#207)
- **Lazy CLI module loading**: All CLI subcommands now use `createLazyAction()` to defer heavy imports (tree-sitter, ONNX, KuzuDB) until invocation, significantly improving `gitnexus mcp` startup time (#207)
- **Type-safe lazy actions**: `createLazyAction` uses constrained generics to validate export names against module types at compile time
- **Regression test suite**: 13 unit tests covering transport framing, security hardening, buffer limits, and lazy action loading

### Fixed

- **CALLS edge sourceId alignment**: `findEnclosingFunctionId` now generates IDs with `:startLine` suffix matching node creation format, fixing process detector finding 0 entry points (#194)
- **LRU cache zero maxSize crash**: Guard `createASTCache` against `maxSize=0` when repos have no parseable files (#144)

### Changed

- Transport constructor accepts `NodeJS.ReadableStream` / `NodeJS.WritableStream` (widened from concrete `ReadStream`/`WriteStream`)
- `processReadBuffer` simplified to break on first error instead of stale-buffer retry loop

## [1.3.9] - 2026-03-06

### Fixed

- Aligned CALLS edge sourceId with node ID format in parse worker (#194)

## [1.3.8] - 2026-03-05

### Fixed

- Force-exit after analyze to prevent KuzuDB native cleanup hang (#192)

```

### File: CLAUDE.md
```md
<!-- version: 1.2.0 -->
<!--
  Metadata: version, last reviewed, scope, model policy, reference docs, changelog.
  Last updated: 2026-03-22
-->

Last reviewed: 2026-03-24

**Project:** GitNexus · **Environment:** dev · **Maintainer:** repository maintainers (see GitHub)

Follow **AGENTS.md** for the canonical rules; this file adds Claude Code–specific deltas. Cursor-specific notes live only in `AGENTS.md`.

## Scope

See the **Scope** table in [AGENTS.md](AGENTS.md) for read/write/execute/off-limits boundaries. Cursor-specific workflow notes also live only in AGENTS.md.

## Model Configuration

- **Primary:** Pin per **Claude Code** / Anthropic org policy (explicit model id). Do not rely on an unversioned `latest` alias for governed workflows.
- **Fallback:** As configured in Claude Code (organization default or user override).
- **Notes:** The GitNexus CLI analyzer does not call an LLM.

## Execution Sequence (complex tasks)

Same discipline as [AGENTS.md](AGENTS.md): before large multi-step work, state which **AGENTS.md** / **GUARDRAILS.md** rules apply, current **Scope**, and planned validation commands (`npm test`, `tsc`, etc.). When pausing, summarize progress in the chat or a **local** scratch file (do not add `HANDOFF.md` to the repo), then `/clear` and resume with that summary.

## Claude Code hooks

Prefer **PreToolUse** hooks for hard gates (e.g. tests before `git_commit`). Adapt hook commands to `gitnexus/` npm scripts.

## Context budget

If always-on instructions grow, load deep conventions via conditional reads (e.g. *“When writing new code, read STANDARDS.md”*) instead of pasting long blocks here. In Cursor, prefer `.cursor/index.mdc` plus optional `.cursor/rules/*.mdc` globs (see [AGENTS.md](AGENTS.md) § Context budget).

## Reference Documentation

- **This repository:** [AGENTS.md](AGENTS.md) (Cursor + monorepo notes), [ARCHITECTURE.md](ARCHITECTURE.md), [CONTRIBUTING.md](CONTRIBUTING.md), [GUARDRAILS.md](GUARDRAILS.md).
- **GitNexus:** `.claude/skills/gitnexus/`; MCP and indexed-repo rules live only in [AGENTS.md](AGENTS.md) (`gitnexus:start` … `gitnexus:end`). See **GitNexus rules** below.

## Changelog

| Date | Version | Change |
|------|---------|--------|
| 2026-03-24 | 1.2.0 | Removed duplicated gitnexus:start block and scope table; replaced with pointers to AGENTS.md. |
| 2026-03-23 | 1.1.0 | Updated agent instructions to match AGENTS.md. |
| 2026-03-22 | 1.0.0 | Added structured header and changelog. |

---

## GitNexus rules

GitNexus MCP rules are in the `<!-- gitnexus:start -->` … `<!-- gitnexus:end -->`  block in **[AGENTS.md](AGENTS.md)** — load that section when working with MCP tools or the graph index.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **GitNexus** (3298 symbols, 7954 relationships, 185 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## When Debugging

1. `gitnexus_query({query: "<error or symptom>"})` — find execution flows related to the issue
2. `gitnexus_context({name: "<suspect function>"})` — see all callers, callees, and process participation
3. `READ gitnexus://repo/GitNexus/process/{processName}` — trace the full execution flow step by step
4. For regressions: `gitnexus_detect_changes({scope: "compare", base_ref: "main"})` — see what your branch changed

## When Refactoring

- **Renaming**: MUST use `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` first. Review the preview — graph edits are safe, text_search edits need manual review. Then run with `dry_run: false`.
- **Extracting/Splitting**: MUST run `gitnexus_context({name: "target"})` to see all incoming/outgoing refs, then `gitnexus_impact({target: "target", direction: "upstream"})` to find all external callers before moving code.
- After any refactor: run `gitnexus_detect_changes({scope: "all"})` to verify only expected files changed.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Tools Quick Reference

| Tool | When to use | Command |
|------|-------------|---------|
| `query` | Find code by concept | `gitnexus_query({query: "auth validation"})` |
| `context` | 360-degree view of one symbol | `gitnexus_context({name: "validateUser"})` |
| `impact` | Blast radius before editing | `gitnexus_impact({target: "X", direction: "upstream"})` |
| `detect_changes` | Pre-commit scope check | `gitnexus_detect_changes({scope: "staged"})` |
| `rename` | Safe multi-file rename | `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` |
| `cypher` | Custom graph queries | `gitnexus_cypher({query: "MATCH ..."})` |

## Impact Risk Levels

| Depth | Meaning | Action |
|-------|---------|--------|
| d=1 | WILL BREAK — direct callers/importers | MUST update these |
| d=2 | LIKELY AFFECTED — indirect deps | Should test |
| d=3 | MAY NEED TESTING — transitive | Test if critical path |

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/GitNexus/context` | Codebase overview, check index freshness |
| `gitnexus://repo/GitNexus/clusters` | All functional areas |
| `gitnexus://repo/GitNexus/processes` | All execution flows |
| `gitnexus://repo/GitNexus/process/{name}` | Step-by-step execution trace |

## Self-Check Before Finishing

Before completing any code modification task, verify:
1. `gitnexus_impact` was run for all modified symbols
2. No HIGH/CRITICAL risk warnings were ignored
3. `gitnexus_detect_changes()` confirms changes match expected scope
4. All d=1 (WILL BREAK) dependents were updated

## Keeping the Index Fresh

After committing code changes, the GitNexus index becomes stale. Re-run analyze to update it:

```bash
npx gitnexus analyze
```

If the index previously included embeddings, preserve them by adding `--embeddings`:

```bash
npx gitnexus analyze --embeddings
```

To check whether embeddings exist, inspect `.gitnexus/meta.json` — the `stats.embeddings` field shows the count (0 means no embeddings). **Running analyze without `--embeddings` will delete any previously generated embeddings.**

> Claude Code users: A PostToolUse hook handles this automatically after `git commit` and `git merge`.

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
