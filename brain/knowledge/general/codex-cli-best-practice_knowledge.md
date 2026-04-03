---
id: codex-cli-best-practice-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:08.226161
---

# KNOWLEDGE EXTRACT: codex-cli-best-practice
> **Extracted on:** 2026-03-30 13:47:15
> **Source:** codex-cli-best-practice

---

## File: `.gitignore`
```
# Personal overrides (not shared with team)
AGENTS.override.md

# Local Codex config (personal settings)
.codex/config.local.toml

# Generated workflow output
orchestration-workflow/output.md

# Dependencies
node_modules/

# OS files
.DS_Store
Thumbs.db

# Editor files
*.swp
*.swo
*~
.vscode/settings.json
.idea/

# Environment variables
.env
.env.local
.claude/settings.local.json
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

This file provides guidance to Codex CLI when working with code in this repository.

## Repository Overview

This is a best practices repository for OpenAI Codex CLI configuration, demonstrating patterns for skills, agents, orchestration workflows, and project-scoped configuration. It serves as a reference implementation rather than an application codebase.

## Key Components

### Weather System (Example Workflow)

A demonstration of the **Agent → Skill** orchestration pattern:
- `weather-agent` (`.codex/agents/weather-agent.toml`): Entry point — fetches temperature from Open-Meteo API, invokes renderer skill
- `weather-svg-creator` skill (`.agents/skills/weather-svg-creator/SKILL.md`): Invoked by agent — creates SVG weather card

The orchestration flow: agent fetches temperature from Open-Meteo (using caller-provided unit, defaults to Celsius), then invokes `/weather-svg-creator` to render the SVG output. See `orchestration-workflow/orchestration-workflow.md` for the complete flow diagram.

### Skill Definition Structure

Skills live in `.agents/skills/<name>/SKILL.md` and use YAML frontmatter:
- `name`: Display name (defaults to directory name)
- `description`: When to invoke the skill (used for auto-discovery)

Each skill directory may also contain:
- `scripts/`: Executable code the skill invokes
- `references/`: Documentation the skill references
- `assets/`: Templates, resources, or static files
- `agents/openai.yaml`: Optional appearance and dependency metadata

Codex discovers skills via progressive disclosure — it starts with metadata and loads full instructions only when a skill is activated.

### Configuration System

Codex CLI uses TOML-based configuration at two levels:
- **User-level**: `~/.codex/config.toml` — personal defaults across all projects
- **Project-level**: `.codex/config.toml` — team-shared, project-scoped overrides (loaded only when the project is trusted)

### Configuration Hierarchy

1. `.codex/config.toml`: Team-shared project settings (checked in)
2. `~/.codex/config.toml`: Personal user-level settings
3. CLI flags (`--model`, `--ask-for-approval`, `--sandbox`): Override both config files
4. `--config key=value`: One-off overrides from the command line

### Agents and Skills

Skills are discovered from multiple scopes in order of precedence:
1. `$CWD/.agents/skills` — current working directory (most specific)
2. `$CWD/../.agents/skills` — parent directories up to repo root
3. `$REPO_ROOT/.agents/skills` — repository root
4. `$HOME/.agents/skills` — user-level personal skills
5. `/etc/codex/skills` — core/admin-level shared skills

Agents are registered under `[agents.<name>]` in `.codex/config.toml` and can
optionally point to dedicated role files in `.codex/agents/*.toml`.

## AGENTS.md Discovery

Codex walks from the Git root down to the current working directory, loading `AGENTS.override.md` then `AGENTS.md` in each directory. Files closer to the current directory appear later in the combined prompt and take precedence. The combined size is capped at 32 KiB by default (`project_doc_max_bytes`).

## Profiles

Define named profiles in `config.toml` under `[profiles.<name>]` to switch between configurations quickly:

```bash
codex --profile conservative   # read-only, asks before every action
codex --profile development    # workspace-write sandbox, on-request approval
codex --profile trusted        # no approval prompts, workspace-write sandbox
codex --profile ci             # headless CI/CD mode
codex --profile review         # read-only code review mode
```

Set a default profile with `profile = "conservative"` at the top level of `config.toml`. Example profile configs are in `examples/profiles/`.

## Workflow Best Practices

From experience with this repository:

- Keep AGENTS.md under 150 lines for reliable adherence
- Use skills with clear `name` and `description` frontmatter for auto-discovery
- Organize skills by feature domain (e.g., `weather-svg-creator`)
- Use profiles to switch between safety levels (`conservative` for review, `trusted` for development)
- Use `AGENTS.override.md` for personal preferences without affecting the team
- Break complex tasks into composable skills rather than monolithic instructions

### Sandbox Modes

- `read-only`: Only reads files, no writes or network access
- `workspace-write`: Reads and writes within the project, sandboxed network
- `danger-full-access`: Unrestricted access (use with caution)

### Approval Policies

- `untrusted`: Only safe read commands auto-approved; everything else asks
- `on-request`: Model decides when to ask for approval (recommended default)
- `never`: All commands auto-approved; failures returned to model directly

## MCP Servers

MCP servers are configured under `[mcp_servers.*]` in `.codex/config.toml`. Currently configured:
- `context7`: Documentation lookup via `@upstash/context7-mcp@latest`

## Documentation

- `best-practice/codex-agents-md.md`: AGENTS.md authoring guide
- `best-practice/codex-config.md`: Config, profiles, and MCP layout
- `best-practice/codex-mcp.md`: MCP servers best practices
- `best-practice/codex-skills.md`: Skills best practices
- `best-practice/codex-subagents.md`: Subagents guide
- `brain/knowledge/docs_legacy/SKILLS.md`: Skills system reference
- `orchestration-workflow/orchestration-workflow.md`: Weather system flow diagram
- `examples/`: Example profile configs and CI/CD setup

```

## File: `README.md`
```markdown
# codex-cli-best-practice
practice makes codex perfect

![updated with Codex CLI](https://img.shields.io/badge/updated_with_Codex_CLI-v0.117.0%20(Mar%2028%2C%202026%2011%3A09%20PM%20PKT)-white?style=flat&labelColor=555) <a href="https://github.com/shanraisshan/codex-cli-best-practice/stargazers"><img src="https://img.shields.io/github/stars/shanraisshan/codex-cli-best-practice?style=flat&label=%E2%98%85&labelColor=555&color=white" alt="GitHub Stars"></a>

[![Best Practice](!/tags/best-practice.svg)](best-practice/) [![Implemented](!/tags/implemented.svg)](.codex/) [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) ![Click on these badges below to see the actual sources](!/tags/click-badges.svg)<br>
<img src="!/tags/a.svg" height="14"> = Agents · <img src="!/tags/c.svg" height="14"> = Commands · <img src="!/tags/s.svg" height="14"> = Skills

<p align="center">
  <img src="!/codex-jumping.svg" alt="Codex CLI mascot jumping" width="120" height="100">
</p>

## CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| <img src="!/tags/c.svg" height="14"> [**Commands**](https://developers.openai.com/codex/cli/slash-commands) | `custom not supported` | Custom commands (`.codex/commands/`) are not yet supported — 29 built-in slash commands: `/plan`, `/skills`, `/fast`, `/fork`, `/review`, `/apps`, `/agent`, `/model`, `/personality`, `/ps`, `/debug-config`, and more |
| <img src="!/tags/a.svg" height="14"> [**Subagents**](https://developers.openai.com/codex/subagents) | [`.codex/agents/<name>.toml`](.codex/agents/) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-subagents.md) [![Implemented](!/tags/implemented.svg)](.codex/agents/) Custom agents registered under `[agents.<name>]` with dedicated TOML role configs, CSV batch processing, and multi-agent orchestration · Built-in: `default`, `worker`, `explorer` |
| <img src="!/tags/s.svg" height="14"> [**Skills**](https://developers.openai.com/codex/skills) | [`.agents/skills/<name>/SKILL.md`](.agents/skills/) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-skills.md) [![Implemented](!/tags/implemented.svg)](.agents/skills/) [Reference](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/fastmcp_server/references/providers/skills.md) Reusable instruction packages with YAML frontmatter — invoke with `/skill-name` or preload into agents · Built-in: `$plan`, `$skill-creator`, `$web-search` · Distributed via [Plugins](https://developers.openai.com/codex/plugins) |
| [**Plugins**](https://developers.openai.com/codex/plugins) | `.codex-plugin/plugin.json` | Distributable bundles combining skills + app integrations + MCP servers — local/personal [marketplace](https://developers.openai.com/codex/plugins/build) system · Built-in: `$plugin-creator` · Browse via `/plugins` or Codex App |
| [**Workflows**](https://developers.openai.com/codex/workflows/) | [`.codex/agents/weather-agent.toml`](.codex/agents/weather-agent.toml) | [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) End-to-end usage patterns — explain codebase, fix bugs, write tests, prototype from screenshot, iterate UI, delegate to cloud, code review, update docs |
| [**MCP Servers**](https://developers.openai.com/codex/mcp) | `config.toml` → `[mcp_servers.*]` | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-mcp.md) [![Implemented](!/tags/implemented.svg)](.codex/config.toml) Model Context Protocol for external tools — STDIO + Streamable HTTP servers · OAuth support (`codex mcp login`) |
| [**Config**](https://developers.openai.com/codex/config-basic) | [`.codex/config.toml`](.codex/config.toml) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-config.md) [![Implemented](!/tags/implemented.svg)](.codex/config.toml) TOML-based layered config system · [Profiles](https://developers.openai.com/codex/config-basic) · [Sandbox](https://developers.openai.com/codex/cli/features) · [Approval Policy](https://developers.openai.com/codex/cli/features) · [Advanced](https://developers.openai.com/codex/config-advanced) (`[features]`, `[otel]`, `[shell_environment_policy]`, `[tui]`, model providers, granular approvals) |
| [**Rules**](https://developers.openai.com/codex/rules) | `.codex/rules/` | Starlark-based command execution policies — `allow`, `prompt`, `forbidden` decisions with pattern matching · Test via `codex execpolicy check` · [AGENTS.override.md](https://developers.openai.com/codex/guides/agents-md) for personal instruction overrides |
| [**AGENTS.md**](https://developers.openai.com/codex/guides/agents-md) | [`AGENTS.md`](../../../.claude/skills/supabase-postgres-best-practices/AGENTS.md) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-agents-md.md) Project-level context for Codex CLI — hierarchical discovery from cwd to repo root, capped at 32 KiB (`project_doc_max_bytes`) · `AGENTS.override.md` for personal overrides |
| [**Hooks**](https://developers.openai.com/codex/hooks) ![beta](!/tags/beta.svg) | [`.codex/hooks.json`](.codex/) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-hooks.md) [![Implemented](!/tags/implemented.svg)](https://github.com/shanraisshan/codex-cli-hooks) User-defined shell scripts that inject into the agentic loop — logging, security scanning, validation, and custom automation · Requires `codex_hooks = true` feature flag |
| [**Speed**](https://developers.openai.com/codex/speed) | `config.toml` → `service_tier` | Fast Mode (1.5x speed, 2x credits) on gpt-5.4 — toggle with `/fast on\|off\|status` · GPT-5.3-Codex-Spark for near-instant iteration (Pro subscribers) |
| [**Multi-Agent**](https://developers.openai.com/codex/multi-agent/) | `config.toml` → `[agents]` | Spawn specialized sub-agents in parallel — fan-out work, collect results, synthesize · `max_threads` (default 6), `max_depth` (default 1) · GA (`multi_agent = true` by default) |
| **AI Terms** | | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-codex-cursor-gemini/blob/main/reports/ai-terms.md) Agentic Engineering · Context Engineering · Vibe Coding |
| [**Best Practices**](https://developers.openai.com/codex/learn/best-practices) | | Official best practices · [Prompt Engineering](https://platform.openai.com/brain/knowledge/docs_legacy/guides/prompt-engineering) · [Codex Guides](https://developers.openai.com/codex/overview) |

[![Orchestration Workflow](!/tags/orchestration-workflow-hd.svg)](orchestration-workflow/orchestration-workflow.md)

See [orchestration-workflow](../claude_bp_repo/orchestration-workflow.md) for implementation details of <img src="!/tags/a.svg" height="14"> **Agent** → <img src="!/tags/s.svg" height="14"> **Skill** pattern. The agent fetches temperature from Open-Meteo and invokes the SVG creator skill.

<p align="center">
  <img src="!/orchestration-workflow-diagram.svg" alt="Orchestration Workflow: Agent → Skill → Output" width="100%">
</p>

![How to Use](!/tags/how-to-use.svg)

```bash
codex
> Fetch the current weather for Dubai in Celsius and create the SVG weather card output using the repo.
```

> **Note:** This workflow is not 100% in sync with the [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) orchestration workflow. Codex CLI does not yet support custom commands (`.codex/commands/`), so the full <img src="!/tags/c.svg" height="14"> **Command** → <img src="!/tags/a.svg" height="14"> **Agent** → <img src="!/tags/s.svg" height="14"> **Skill** pattern is not possible. There is an experimental `tool/requestUserInput` in the Codex App Server docs and an internal `request_user_input` capability gated behind an under-development feature flag in codex-cli 0.115.0, but neither is publicly available yet.

## DEVELOPMENT WORKFLOWS
- [Cross-Model Claude Code + Codex](https://github.com/shanraisshan/claude-code-best-practice/blob/main/development-workflows/cross-model-workflow/cross-model-workflow.md) [![Implemented](!/tags/implemented.svg)](https://github.com/shanraisshan/claude-code-best-practice/blob/main/development-workflows/cross-model-workflow/cross-model-workflow.md)

## TIPS AND TRICKS

![Community](!/tags/community.svg)

■ **Planning (2)**
- use [`/plan`](https://developers.openai.com/codex/cli/slash-commands) when you want an explicit plan — Codex may also plan automatically for multi-step tasks
- use [cross-model](https://github.com/shanraisshan/claude-code-best-practice/blob/main/development-workflows/cross-model-workflow/cross-model-workflow.md) (e.g., Claude Code) to review your plan before execution

■ **Workflows (8)**
- keep [`AGENTS.md`](https://developers.openai.com/codex/guides/agents-md) concise — 150 lines is a useful heuristic, but the actual limit is byte-based
- use [skills](https://developers.openai.com/codex/skills) with clear `name` and `description` frontmatter for auto-discovery
- use [`AGENTS.override.md`](https://developers.openai.com/codex/rules) for personal preferences without affecting the team
- use [profiles](https://developers.openai.com/codex/config-basic) to switch between project-defined safety levels — in this repo, `conservative` and `trusted` are examples
- use the built-in skill creator to scaffold new skills, and document one invocation style consistently across the repo
- start with [`on-request`](https://developers.openai.com/codex/cli/features) approval policy — only escalate to `never` when confident
- use [`--fork`](https://developers.openai.com/codex/cli/features) to explore alternatives without losing your session, [`--resume`](https://developers.openai.com/codex/cli/features) to pick up where you left off
- commit often — as soon as a task is completed, commit

■ **Workflows Advanced (4)**
- use [multi-agent](https://developers.openai.com/codex/multi-agent/) to spawn sub-agents for parallel fan-out work (GA — enabled by default)
- use [`codex exec`](https://developers.openai.com/codex/noninteractive) for headless/CI pipelines
- combine [sandbox modes](https://developers.openai.com/codex/cli/features) with [approval policies](https://developers.openai.com/codex/cli/features) — `workspace-write` + `on-request` is a good default
- [git worktrees](https://git-scm.com/brain/knowledge/docs_legacy/git-worktree) for parallel development

■ **Debugging (4)**
- always ask Codex to run the terminal (you want to see logs of) as a background task for better debugging
- use MCP ([Chrome DevTools](https://developer.chrome.com/blog/chrome-devtools-mcp), [Playwright](https://github.com/microsoft/playwright-mcp)) to let Codex see browser console logs on its own
- make it a habit to take screenshots and share with Codex whenever you are stuck with any issue
- use a different model for QA — e.g. [Claude Code](https://github.com/shanraisshan/claude-code-best-practice) for plan and implementation review

■ **Utilities (4)**
- [iTerm](https://iterm2.com/) terminal instead of IDE (crash issue)
- [Wispr Flow](https://wisprflow.ai) for voice prompting (10x productivity)
- [codex-cli-hooks](https://github.com/shanraisshan/codex-cli-hooks) for Codex feedback
- explore `config.toml` features like [profiles](https://developers.openai.com/codex/config-basic), [sandbox modes](https://developers.openai.com/codex/cli/features), and [MCP](https://developers.openai.com/codex/mcp) for a personalized experience

■ **Daily (2)**
- update Codex CLI daily and start your day by reading the [changelog](https://github.com/openai/codex/releases)
- follow [Tibo](https://x.com/thsottiaux), [Embiricos](https://x.com/embirico), [Jason](https://x.com/jxnlco), [Romain](https://x.com/romainhuet), [Dominik](https://x.com/dkundel), [Fouad](https://x.com/fouadmatin), [Bolin](https://x.com/bolinfest), [OpenAI Devs](https://x.com/OpenAIDevs) on X

![Codex Team](!/tags/codex-team.svg)

- Codex CLI — open-source local coding agent, first look (Fouad + Romain) | Apr 2025 ● [Tweet](https://x.com/OpenAIDevs/status/1912556874211422572)
- AMA with Codex team — CLI, sandbox, agents (Embiricos, Fouad, Tibo + team) | May 2025 ● [Reddit](https://www.reddit.com/r/ChatGPT/comments/1ko3tp1/ama_with_openai_codex_team/)
- Skills in Codex — standardizing .agents/skills across agents (Embiricos) | Feb 2026 ● [Tweet](https://x.com/embirico/status/2002102889653924111)
- Unrolling the Codex agent loop — how Codex works internally (Bolin) | Jan 2026 ● [Tweet](https://x.com/OpenAIDevs/status/2014794871962533970)
- How Codex is built — 90% self-built in Rust (Tibo, Pragmatic Engineer) | 17 Feb 2026 ● [Post](https://newsletter.pragmaticengineer.com/p/how-codex-is-built)
- Dogfood — Codex team uses Codex to build Codex (Tibo, Stack Overflow) | 24 Feb 2026 ● [Podcast](https://stackoverflow.blog/2026/02/24/dogfood-so-nutritious-it-s-building-the-future-of-sdlcs/)
- Why humans are AI's biggest bottleneck — Codex product vision (Embiricos, Lenny's) | Feb 2026 ● [Podcast](https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck)
- How Codex team uses their coding agent (Tibo + Andrew, Every) | 18 Feb 2026 ● [Podcast](https://every.to/podcast/transcript-how-openai-s-codex-team-uses-their-coding-agent)

<a href="https://github.com/shanraisshan/claude-code-best-practice#billion-dollar-questions"><img src="!/tags/billion-dollar-questions.svg" alt="Billion-Dollar Questions"></a>

## Other Repos

<a href="https://github.com/shanraisshan/codex-cli-hooks"><img src="!/codex-speaking.svg" alt="Codex CLI Hooks" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/codex-cli-hooks"><strong>codex-cli-hooks</strong></a> · <a href="https://github.com/shanraisshan/claude-code-best-practice"><img src="!/claude-jumping.svg" alt="Claude Code" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/claude-code-best-practice"><strong>claude-code-best-practice</strong></a> · <a href="https://github.com/shanraisshan/claude-code-hooks"><img src="!/claude-speaking.svg" alt="Claude Code Hooks" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/claude-code-hooks"><strong>claude-code-hooks</strong></a>

---

<a href="https://openai.com/form/codex-for-oss/"><img src="!/tags/codex-for-oss.svg" alt="Codex for Open Source" width="720"></a>
```

## File: `best-practice/codex-agents-md.md`
```markdown
# Best Practice: AGENTS.md

The `AGENTS.md` file is the primary instructions file for Codex CLI — providing project-level context and behavioral directives.

## File Naming and Fallbacks

Codex CLI searches for instructions in this order:
1. `AGENTS.md` (preferred)
2. `CODEX.md` (alias)

Use `AGENTS.md` for new projects.

## Sizing: Keep It Under 150 Lines

The single most impactful best practice: **keep AGENTS.md concise**.

- Lines beyond ~150 are increasingly likely to be ignored or truncated
- Long files dilute important instructions with noise
- The model processes instructions better when they are focused

**If you exceed 150 lines**, extract detailed content into:
- Skill files (`skills/<name>/SKILL.md`) for specialized procedures
- Separate docs files referenced by path
- Agent-preloaded skills for domain-specific knowledge

## Hierarchy and Override Mechanism

AGENTS.md files follow directory hierarchy:

```
/repo/AGENTS.md              # Root-level instructions
/repo/packages/api/AGENTS.md # Package-specific overrides
/repo/packages/web/AGENTS.md # Package-specific overrides
```

**Loading behavior**:
- Codex walks up from the working directory, loading each AGENTS.md it finds
- More specific (deeper) files take precedence over general (higher) ones
- All files are concatenated into context, with deeper files appearing later

## Recommended Structure

```markdown
# AGENTS.md

## Repository Overview
One paragraph describing what this project is and does.

## Key Components
Brief descriptions of major subsystems, with file paths.

## Critical Patterns
Non-obvious conventions the model MUST follow.

## Workflow Rules
Build, test, lint commands. Deployment patterns.

## Do NOT
Explicit anti-patterns to avoid.
```

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Dumping entire API docs | Exceeds line limit; dilutes focus | Link to docs; use skills |
| Repeating obvious conventions | Wastes lines on things the model knows | Only document the non-obvious |
| Long code examples | Eats line budget fast | Keep examples under 10 lines |
| Vague instructions ("be careful") | Not actionable | Be specific: "Always run `npm test` before committing" |
| Contradictory rules | Model picks one arbitrarily | Audit for conflicts |

## Monorepo Strategy

For monorepos, use a layered approach:

1. **Root `AGENTS.md`**: Shared conventions (git workflow, CI commands, coding standards)
2. **Package `AGENTS.md`**: Package-specific build commands, architecture decisions, testing patterns
3. **Skills**: Extract complex procedures (deployment, migration) into skills that any AGENTS.md can reference

This keeps each file short while maintaining comprehensive coverage.

## Truncation Behavior

When AGENTS.md exceeds the model's processing capacity:
- Content at the end of the file is most likely to be truncated
- Put the most critical instructions at the top
- Use clear section headers so the model can scan structure even if details are lost
- Test by asking the model to repeat instructions from different sections
```

## File: `best-practice/codex-config.md`
```markdown
# Best Practice: Config

A comprehensive guide to Codex CLI's TOML-based configuration system — covering config hierarchy, profiles, sandbox modes, and approval policies.

<table width="100%">
<tr>
<td><a href="../">← Back to Codex CLI Best Practice</a></td>
<td align="right"><img src="../!/codex-jumping.svg" alt="Codex" width="60" /></td>
</tr>
</table>

## Settings Hierarchy

Settings apply in order of precedence (highest to lowest):

| Priority | Location | Scope | Purpose |
|----------|----------|-------|---------|
| 1 | CLI flags / `-c key=value` | Invocation | One-off overrides for a single run |
| 2 | `.codex/config.toml` | Project | Team-shared defaults, profiles, MCP, agents |
| 3 | `~/.codex/config.toml` | Global | Personal defaults across projects |

## Core Configuration

```toml
# .codex/config.toml
model = "o4-mini"
sandbox_mode = "workspace-write"
approval_policy = "on-request"
```

## Profiles

Named presets under `[profiles.<name>]` — switch with `codex --profile <name>`:

```toml
[profiles.conservative]
sandbox_mode = "read-only"
approval_policy = "untrusted"

[profiles.development]
sandbox_mode = "workspace-write"
approval_policy = "on-request"

[profiles.ci]
model = "o4-mini"
sandbox_mode = "read-only"
approval_policy = "never"

[profiles.trusted]
sandbox_mode = "danger-full-access"
approval_policy = "never"
```

Set a default profile with `profile = "conservative"` at the top level.

## Sandbox Modes

| Mode | File Access | Network | Best for |
|---|---|---|---|
| `read-only` | Read-only project access | Blocked | Reviews, audits, CI analysis |
| `workspace-write` | Read/write inside the workspace | Blocked | Local development and doc/code edits |
| `danger-full-access` | Unrestricted filesystem access | Allowed | Fully trusted automation that needs network or installs |

## Approval Policies

| Policy | Behavior | Best for |
|---|---|---|
| `untrusted` | Auto-runs only trusted read-style commands; asks for the rest | New repos, audits, reviews |
| `on-request` | Model decides when it should ask | Everyday development |
| `never` | Never asks; failures come straight back to the model | Non-interactive runs and tightly controlled automation |

## Override

Use `AGENTS.override.md` for personal instruction overrides — loaded before `AGENTS.md`, not committed to git.

## MCP Servers

Declare shared integrations in the same config file:

```toml
[mcp_servers.github]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-github"]
env = { GITHUB_TOKEN = "$GITHUB_TOKEN" }
```

## Agents

Register agents under `[agents.<name>]` and optionally point them at dedicated role files:

```toml
[agents.backend-dev]
description = "Handles backend implementation tasks"
config_file = "agents/backend-dev.toml"
```

## One-Off Overrides

```bash
codex -c model=\"o3\" -c approval_policy=\"never\" exec "summarize this diff"
```

## Anti-Patterns

- Using `danger-full-access` for ordinary editing tasks
- Treating `never` as a general-purpose local default
- Using `danger-full-access` and `never` together without a real containment boundary
- Hardcoding secrets instead of using `$ENV_VAR` expansion
- Mixing unrelated concerns into one profile instead of creating focused profiles
```

## File: `best-practice/codex-hooks.md`
```markdown
# Best Practice: Hooks

Hooks are an extensibility framework that inject custom scripts into the Codex agentic loop — enabling deterministic automation for logging, security scanning, validation, conversation summarization, and context-aware prompting.

<table width="100%">
<tr>
<td><a href="../">← Back to Codex CLI Best Practice</a></td>
<td align="right"><img src="../!/codex-jumping.svg" alt="Codex" width="60" /></td>
</tr>
</table>

> **Status:** Experimental — under active development. Windows support temporarily disabled.

## Feature Flag

Hooks require enabling in `config.toml`:

```toml
[features]
codex_hooks = true
```

## Discovery Locations

Codex discovers `hooks.json` files at two levels — both load simultaneously; higher-precedence layers don't replace lower-precedence hooks:

| Priority | Location | Scope |
|----------|----------|-------|
| 1 | `.codex/hooks.json` | Project (team-shared) |
| 2 | `~/.codex/hooks.json` | Global (personal) |

## Hook Events

| Event | Matcher | Description |
|-------|---------|-------------|
| `SessionStart` | `startup \| resume` | Runs at session initialization |
| `PreToolUse` | `Bash` | Intercepts tool execution before running (Bash only) |
| `PostToolUse` | `Bash` | Reviews tool results after execution (Bash only) |
| `UserPromptSubmit` | Not supported | Runs when user submits a prompt |
| `Stop` | Not supported | Runs when a turn completes — determines whether to continue |

## Configuration Structure

Hooks organize into three levels: **event → matcher group → hook handlers**

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "pattern|regex",
        "hooks": [
          {
            "type": "command",
            "command": "script_path",
            "statusMessage": "optional UI feedback",
            "timeout": 600
          }
        ]
      }
    ]
  }
}
```

### Key Options

| Option | Default | Description |
|--------|---------|-------------|
| `timeout` / `timeoutSec` | 600s | Execution time limit in seconds |
| `statusMessage` | — | Optional UI feedback during execution |
| `matcher` | Match all | Regex to filter event firing (`"*"`, `""`, or omit for all) |

## Runtime Behavior

- Matching hooks from multiple files all execute
- Multiple command hooks for the same event launch **concurrently**
- One hook cannot prevent another from running
- Commands run with session `cwd` as working directory

## Hook Events Deep Dive

### SessionStart

Injects context at session initialization.

**Input fields:** `source`, `session_id`, `transcript_path`, `cwd`, `hook_event_name`, `model`

**Output:** Plain text on stdout is added as developer context. JSON output supports:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "text added as context"
  }
}
```

### PreToolUse

Intercepts tool execution before running (currently Bash only).

> **Note:** The model can circumvent this by writing and executing scripts directly — treat as a useful guardrail rather than a complete enforcement boundary.

**Input fields:** `turn_id`, `tool_name`, `tool_use_id`, `tool_input.command`, plus common fields

**Deny execution:**

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "reason text"
  }
}
```

**Alternative:** Exit code `2` with blocking reason on stderr.

### PostToolUse

Reviews tool results after execution (Bash only). Cannot undo side effects but can replace the tool result with feedback.

**Input fields:** `turn_id`, `tool_name`, `tool_use_id`, `tool_input.command`, `tool_response`, plus common fields

**Block and replace result:**

```json
{
  "decision": "block",
  "reason": "feedback reason",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "context text"
  }
}
```

**Alternative:** Exit code `2` with feedback reason on stderr.

### UserPromptSubmit

Runs when user submits a prompt. Matcher not supported.

**Input fields:** `turn_id`, `prompt`, plus common fields

**Block submission:**

```json
{
  "decision": "block",
  "reason": "reason text"
}
```

**Add context:**

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "context text"
  }
}
```

### Stop

Runs when a turn completes — determines whether to continue automatically. Matcher not supported.

**Input fields:** `turn_id`, `stop_hook_active`, `last_assistant_message`, plus common fields

**Continue with automatic prompt:**

```json
{
  "decision": "block",
  "reason": "continuation reason text"
}
```

> `decision: "block"` tells Codex to **continue** (not reject). The reason becomes the next prompt text. If any matching hook returns `continue: false`, that takes precedence.

## Common Input Fields

Every command hook receives JSON on stdin:

| Field | Type | Description |
|-------|------|-------------|
| `session_id` | string | Session/thread ID |
| `transcript_path` | string \| null | Path to session transcript |
| `cwd` | string | Working directory |
| `hook_event_name` | string | Current event name |
| `model` | string | Active model slug |
| `turn_id` | string | Turn-scoped hooks only |

## Common Output Fields

`SessionStart`, `UserPromptSubmit`, and `Stop` support:

| Field | Type | Description |
|-------|------|-------------|
| `continue` | boolean | `false` marks hook as stopped |
| `stopReason` | string | Recorded as stop reason |
| `systemMessage` | string | Surfaced as UI warning |
| `suppressOutput` | boolean | Parsed, not yet implemented |

Exit `0` with no output is treated as success — Codex continues normally.

## Path Resolution

For repo-local hooks, prefer git-root-based paths to avoid issues when Codex starts from subdirectories:

```
/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/script.py"
```

## Full Example

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| Relying on `PreToolUse` as a security boundary | Treat as a guardrail — the model can write scripts to bypass it |
| Using relative paths in hook commands | Use `$(git rev-parse --show-toplevel)` for stability |
| Missing the `[features]` flag | Always enable `codex_hooks = true` in `config.toml` |
| Setting very long timeouts on blocking hooks | Keep timeouts short to avoid stalling the agent loop |
| Assuming hooks can undo `PostToolUse` side effects | They can only replace the result, not reverse the action |
| Not handling JSON stdin properly | Every hook receives JSON on stdin — parse it correctly |
```

## File: `best-practice/codex-mcp.md`
```markdown
# Best Practice: MCP (Model Context Protocol)

Codex CLI uses `[mcp_servers.<name>]` in `.codex/config.toml` for MCP
integrations, and it can also run as an MCP server via `codex mcp-server`.

## MCP Server Configuration

```toml
[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "."]

[mcp_servers.github]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-github"]
env = { GITHUB_TOKEN = "$GITHUB_TOKEN" }
```

## Agent-Scoped MCP Servers

Keep MCP access narrow by attaching servers to specific agents:

```toml
[agents.data-analyst]
description = "Works with repository and database context"
config_file = "agents/data-analyst.toml"
```

```toml
# .codex/agents/data-analyst.toml
model = "o4-mini"
mcp_servers = ["filesystem", "github"]
```

## Codex as an MCP Server

```bash
codex mcp-server
```

Consumer example:

```json
{
  "mcpServers": {
    "codex": {
      "command": "codex",
      "args": ["mcp-server"]
    }
  }
}
```

## Security Guidance

1. Use `$ENV_VAR` references for secrets
2. Scope MCP servers per agent instead of making every server globally available
3. Prefer `workspace-write` or `read-only` when a server does not need network
4. Switch to `danger-full-access` only when the MCP workflow truly requires network access

## Anti-Patterns

- Documenting the retired MCP table naming from older Codex releases
- Hardcoding tokens in config
- Giving every agent the same MCP surface area
- Using the retired one-flag MCP server syntax instead of `codex mcp-server`
```

## File: `best-practice/codex-skills.md`
```markdown
# Best Practice: Skills

Skills are the primary mechanism for extending Codex CLI with reusable, composable instruction packages. They follow the SKILL.md open standard.

## Two Skill Patterns

### 1. User-Invocable Skills (Slash Commands)

Triggered explicitly by the user via `/skill-name`:

```yaml
---
name: deploy
description: Deploy to target environment
argument-hint: "[env] [version]"
allowed-tools: Bash, Read
---
```

**Best for**: Workflows the user triggers on demand (deploy, review, generate).

### 2. Agent-Preloaded Skills (Background Knowledge)

Defined as regular skills, then attached to an agent through the current
agent configuration model:

```toml
# .codex/config.toml
[agents.api-developer]
description = "Builds and reviews HTTP APIs"
config_file = "agents/api-developer.toml"
```

```toml
# .codex/agents/api-developer.toml
model = "o4-mini"
skills = ["api-conventions", "error-handling"]

prompt = """
Work on backend APIs for this project.
"""
```

**Best for**: Domain knowledge that agents need but users never invoke directly.

## Frontmatter Guidelines

### Write Descriptive `description` Fields
The description drives auto-discovery. Be specific about when the skill should be used:

```yaml
# Good: specific trigger condition
description: Review TypeScript files for type safety issues and suggest fixes

# Bad: vague, matches too many contexts
description: Help with TypeScript
```

### Scope `allowed-tools` Tightly
Only grant tools the skill actually needs:

```yaml
# Good: minimal permissions
allowed-tools: Read, Grep, Glob

# Bad: overly permissive
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch
```

### Choose the Right Model
Use cheaper models for simple tasks:

```yaml
# Fast analysis tasks
model: o4-mini

# Complex reasoning tasks
model: o3
```

## Skill Organization

```
.agents/skills/
  deploy/
    SKILL.md          # Main skill instructions
  pr-review/
    SKILL.md
  code-standards/     # Agent-preloaded, not user-invocable
    SKILL.md
  security-audit/
    SKILL.md
```

### Naming Conventions
- Use kebab-case for directory names: `pr-review`, not `prReview`
- Keep names short but descriptive
- Avoid generic names like `helper` or `utils`

## String Substitutions

Use `$ARGUMENTS` for the full argument string, `$0` for the first positional arg:

```markdown
---
name: fix-issue
argument-hint: "[issue-number]"
---

# Fix Issue Skill

Fetch issue #$0 from GitHub and implement a fix:
1. Run `gh issue view $0` to read the issue
2. Analyze the reported problem
3. Implement and test the fix
```

## Composing Skills

### Skill Chains via Commands
Use a command to orchestrate multiple skills:

```markdown
<!-- commands/full-review.md -->
1. Invoke /security-audit on the changed files
2. Invoke /pr-review for code quality
3. Combine findings into a single report
```

### Agent + Skills
Agents with preloaded skills get domain expertise without user intervention:

```toml
# .codex/config.toml
[agents.backend-dev]
description = "Handles backend development tasks"
config_file = "agents/backend-dev.toml"
```

```toml
# .codex/agents/backend-dev.toml
model = "o4-mini"
skills = ["api-conventions", "database-patterns", "error-handling"]
```

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| Putting all instructions in AGENTS.md | Extract into focused skills |
| Skills longer than 100 lines | Split into multiple skills or use linked docs |
| Skills that do everything | One skill, one responsibility |
| Forgetting `user-invocable: false` for knowledge skills | Always set for agent-only skills |
| Hardcoding values that vary by environment | Use `$ARGUMENTS` for dynamic values |
```

## File: `best-practice/codex-subagents.md`
```markdown
# Best Practice: Subagents

Subagents let Codex spawn specialized agents in parallel to tackle complex, highly parallel tasks — such as codebase exploration or multi-step feature plans — then collect their results in one response.

With subagent workflows you can also define custom agents with different model configurations and instructions depending on the task.

## When to Use Subagents

Subagents are ideal for tasks that are:
- **Highly parallel** — multiple independent review or exploration threads
- **Domain-specialized** — different tasks need different models, tools, or instructions
- **Large-scope** — reviewing a full PR across security, quality, tests, etc.

Codex only spawns subagents when you explicitly ask it to. Each subagent does its own model and tool work, so subagent workflows consume more tokens than single-agent runs.

## Typical Workflow

Codex handles orchestration: spawning subagents, routing follow-up instructions, waiting for results, and closing threads. When many agents are running, Codex waits until all results are available before returning a consolidated response.

**Try this prompt on your project:**

```
I would like to review the following points on the current PR (this branch vs main).
Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race conditions
5. Test flakiness
6. Maintainability of the code
```

## Managing Subagents

- Use `/agent` in the CLI to switch between active agent threads and inspect ongoing work
- Ask Codex directly to steer a running subagent, stop it, or close completed threads

## Approvals and Sandbox Controls

Subagents inherit your current sandbox policy.

- In interactive CLI sessions, approval requests can surface from inactive threads. The overlay shows the source thread label — press `o` to open that thread before you approve/reject.
- In non-interactive flows, actions needing new approval fail and Codex surfaces the error to the parent workflow.
- Codex reapplies the parent turn's live runtime overrides (sandbox, `/approvals` changes, `--yolo`) when spawning children, even if a custom agent file sets different defaults.
- You can override sandbox config per custom agent (e.g., mark one as read-only).

## Built-in Agents

Codex ships with three built-in agents:

| Agent | Purpose |
|-------|---------|
| `default` | General-purpose fallback |
| `worker` | Execution-focused for implementation and fixes |
| `explorer` | Read-heavy codebase exploration |

## Custom Agents

Define custom agents as standalone TOML files:
- `~/.codex/agents/` — personal agents
- `.codex/agents/` — project-scoped agents

Each file defines one agent and can override the same settings as a normal Codex session config.

### Required Fields

Every custom agent must define:

| Field | Type | Purpose |
|-------|------|---------|
| `name` | string | Agent name Codex uses when spawning |
| `description` | string | When Codex should use this agent |
| `developer_instructions` | string | Core behavior instructions |

### Optional Fields

These inherit from the parent session when omitted:

- `nickname_candidates` — display nicknames for spawned instances
- `model` — model override
- `model_reasoning_effort` — reasoning effort level
- `sandbox_mode` — sandbox override (e.g., `read-only`)
- `mcp_servers` — MCP server connections
- `skills.config` — skill configurations

### Global Subagent Settings

Configure in your `config.toml` under `[agents]`:

| Field | Default | Purpose |
|-------|---------|---------|
| `agents.max_threads` | 6 | Concurrent open agent thread cap |
| `agents.max_depth` | 1 | Spawned agent nesting depth (root = 0) |
| `agents.job_max_runtime_seconds` | 1800 | Default timeout per worker for CSV jobs |

### Display Nicknames

Use `nickname_candidates` for readable labels when running many instances of the same agent:

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
"""
nickname_candidates = ["Atlas", "Delta", "Echo"]
```

Nicknames are presentation-only — Codex still identifies agents by `name`.

### Best Practices for Custom Agents

The best custom agents are **narrow and opinionated**:
- Give each one a clear, single job
- Match the tool surface to that job
- Write instructions that prevent drifting into adjacent work
- If a custom agent name matches a built-in (e.g., `explorer`), the custom agent takes precedence

## Example: PR Review Pattern

Split review across three focused agents:

**Project config (`.codex/config.toml`):**
```toml
[agents]
max_threads = 6
max_depth = 1
```

**`.codex/agents/pr-explorer.toml`:**
```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes
unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""
```

**`.codex/agents/reviewer.toml`:**
```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible,
and avoid style-only comments unless they hide a real bug.
"""
```

**`.codex/agents/docs-researcher.toml`:**
```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

**Prompt:**
```
Review this branch against main. Have pr_explorer map the affected code paths,
reviewer find real risks, and docs_researcher verify the framework APIs
that the patch relies on.
```

## Example: Frontend Integration Debugging

Three agents for UI regressions and cross-stack bugs:

**`.codex/agents/code-mapper.toml`:**
```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating relevant frontend and backend code paths."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""
```

**`.codex/agents/browser-debugger.toml`:**
```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20
```

**`.codex/agents/ui-fixer.toml`:**
```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched,
and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false
```

**Prompt:**
```
Investigate why the settings modal fails to save. Have browser_debugger reproduce it,
code_mapper trace the responsible code path, and ui_fixer implement the smallest fix
once the failure mode is clear.
```

## CSV Batch Processing (Experimental)

Use `spawn_agents_on_csv` for many similar tasks that map to one row per work item. Codex reads the CSV, spawns one worker per row, waits for the batch to finish, and exports combined results.

**Good for:**
- Reviewing one file, package, or service per row
- Checking lists of incidents, PRs, or migration targets
- Generating structured summaries for many similar inputs

**Parameters:**

| Parameter | Purpose |
|-----------|---------|
| `csv_path` | Source CSV |
| `instruction` | Worker prompt template with `{column_name}` placeholders |
| `id_column` | Column for stable item IDs |
| `output_schema` | JSON object shape each worker must return |
| `output_csv_path` | Export path |
| `max_concurrency` | Parallel worker limit |
| `max_runtime_seconds` | Per-worker timeout |

Each worker must call `report_agent_job_result` exactly once — if a worker exits without reporting, Codex marks that row with an error.

**Example prompt:**
```
Create /tmp/components.csv with columns path,owner and one row per frontend component.

Then call spawn_agents_on_csv with:
- csv_path: /tmp/components.csv
- id_column: path
- instruction: "Review {path} owned by {owner}. Return JSON with keys path, risk,
  summary, and follow_up via report_agent_job_result."
- output_csv_path: /tmp/components-review.csv
- output_schema: an object with required string fields path, risk, summary, and follow_up
```
```

## File: `brain/knowledge/docs_legacy/SKILLS.md`
```markdown
# Skills System Reference

Skills are reusable instruction packages that extend Codex CLI's capabilities. They follow the open **SKILL.md standard**, making them portable and shareable across projects.

## SKILL.md File Format

Skills live in `.agents/skills/<name>/SKILL.md`. Each skill is a Markdown file with YAML frontmatter:

```markdown
---
name: my-skill
description: When to invoke this skill — used for auto-discovery
argument-hint: "[file-path]"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
model: o4-mini
---

# My Skill Instructions

Detailed instructions for what the skill should do when invoked...
```

## Frontmatter Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `name` | string | Directory name | Display name and `/slash-command` trigger |
| `description` | string | — | Purpose description; used for auto-discovery ranking |
| `argument-hint` | string | — | Autocomplete hint shown after `/name` (e.g., `[issue-number]`) |
| `disable-model-invocation` | bool | `false` | Prevents automatic invocation; must be explicitly called |
| `user-invocable` | bool | `true` | If `false`, hidden from `/` menu (background knowledge only) |
| `allowed-tools` | string | — | Comma-separated tools allowed without permission prompts |
| `model` | string | Inherited | Model to use: `o4-mini`, `o3`, `gpt-4.1` |
| `context` | string | — | Set to `fork` to run in isolated subagent context |
| `agent` | string | `general-purpose` | Subagent type when `context: fork` |
| `hooks` | object | — | Lifecycle hooks scoped to this skill |

## String Substitutions

Skills support dynamic variable injection:

| Variable | Expands To |
|---|---|
| `$ARGUMENTS` | Full argument string passed after the skill name |
| `$0` | First positional argument |
| `$1`, `$2`, ... | Subsequent positional arguments |

**Example**: If user types `/deploy staging v2.1`, then `$ARGUMENTS` = `staging v2.1`, `$0` = `staging`, `$1` = `v2.1`.

## Built-in Skills

Codex CLI ships with several built-in skills prefixed with `$`:

### $plan
Structured planning skill. Creates a step-by-step plan before executing complex tasks. Automatically invoked when tasks appear multi-step.

### $skill-creator
Meta-skill that generates new SKILL.md files. Invoke with `/skill-creator` and describe what the skill should do.

### $web-search
Web search capability. Fetches and processes web content to answer questions requiring current information.

## Discovery Paths

Codex CLI discovers skills from multiple locations, in priority order:

1. **Project skills**: `./.agents/skills/` in the current project (scanned up to repo root)
2. **User skills**: `~/.agents/skills/` for personal cross-project skills
3. **Built-in skills**: Shipped with Codex CLI (`$plan`, `$skill-creator`, etc.)

When multiple skills share a name, the most local version wins (project > user > built-in).

## Skill Patterns

### User-Invocable Skill (Slash Command)
```yaml
---
name: deploy
description: Deploy the application to a target environment
argument-hint: "[environment] [version]"
allowed-tools: Bash, Read
---
```
User triggers with `/deploy production v2.0`.

### Agent-Preloaded Skill (Background Knowledge)
```yaml
---
name: code-standards
description: Team coding standards and conventions
user-invocable: false
---
```
Loaded into agent context via `[agents.<name>]` role configuration in `.codex/config.toml` and a companion TOML file:

```toml
# .codex/config.toml
[agents.backend-dev]
description = "Handles backend development tasks"
config_file = "agents/backend-dev.toml"
```

```toml
# .codex/agents/backend-dev.toml
model = "o4-mini"
skills = ["code-standards"]
```

Never shown in `/` menu.

### Forked Skill (Isolated Execution)
```yaml
---
name: security-audit
description: Run security analysis in isolated context
context: fork
agent: security-reviewer
allowed-tools: Bash, Read, Grep, Glob
---
```
Runs in a separate subagent context to avoid polluting the main conversation.

## Example: Complete Skill

```markdown
---
name: pr-review
description: Review a pull request and provide structured feedback
argument-hint: "[pr-number]"
allowed-tools: Bash, Read, Grep, Glob
model: o4-mini
---

# PR Review Skill

Review pull request #$0 and provide structured feedback.

## Steps
1. Fetch the PR diff using `gh pr diff $0`
2. Read all changed files for full context
3. Analyze for: correctness, security issues, performance, style
4. Output a structured review with severity ratings

## Output Format
Use this template:
- **Critical**: Issues that must be fixed
- **Warning**: Issues that should be addressed
- **Suggestion**: Optional improvements
- **Praise**: What was done well
```
```

## File: `examples/ci-cd/ci-config.toml`
```
# CI-specific Codex CLI configuration
#
# This config is optimized for automated pipeline execution:
# - Fast model (o4-mini) for cost efficiency
# - Full sandbox for maximum isolation
# - Full-auto approval with scoped allow-list
# - No network access (full sandbox blocks it)
#
# Usage:
#   codex --profile ci exec "your prompt here"
#
# Or set as the project default for CI environments:
#   CODEX_PROFILE=ci codex exec "your prompt here"

# Default model for all profiles
model = "o4-mini"

# Default interactive behavior
approval_policy = "on-request"
sandbox_mode = "workspace-write"

# ─────────────────────────────────────
# CI Profile
# ─────────────────────────────────────
[profiles.ci]
model = "o4-mini"
approval_policy = "never"
sandbox_mode = "read-only"

# ─────────────────────────────────────
# Review Profile (read-only analysis)
# ─────────────────────────────────────
[profiles.review]
model = "o3"
approval_policy = "untrusted"
sandbox_mode = "read-only"

# ─────────────────────────────────────
# Development Profile (local work)
# ─────────────────────────────────────
[profiles.development]
model = "o4-mini"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

## File: `examples/ci-cd/github-actions.yml`
```yaml
# GitHub Actions workflow using Codex CLI for automated code review and analysis.
#
# This workflow demonstrates:
# - Running codex exec in CI with the ci profile
# - PR review automation
# - Test failure analysis
# - Documentation validation
#
# Prerequisites:
# - OPENAI_API_KEY secret configured in repository settings
# - .codex/config.toml with a [profiles.ci] section in the repository

name: Codex CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read
  pull-requests: write

jobs:
  # Job 1: Automated PR review using Codex CLI
  pr-review:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for accurate diffs

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Codex CLI
        run: npm install -g @openai/codex

      - name: Run PR Review
        run: |
          codex --profile ci exec \
            "Review the diff between origin/main and HEAD. \
             Focus on: correctness, security issues, performance. \
             Output a markdown summary with severity ratings."
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

  # Job 2: Test analysis — runs when tests fail
  test-analysis:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        id: tests
        run: npm test 2>&1 | tee test-output.txt
        continue-on-error: true

      - name: Install Codex CLI
        if: steps.tests.outcome == 'failure'
        run: npm install -g @openai/codex

      - name: Analyze test failures
        if: steps.tests.outcome == 'failure'
        run: |
          codex --profile ci exec \
            "Read test-output.txt and analyze the test failures. \
             For each failure, explain the likely cause and suggest a fix. \
             Output as markdown."
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

      - name: Fail if tests failed
        if: steps.tests.outcome == 'failure'
        run: exit 1

  # Job 3: Documentation check
  docs-check:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Codex CLI
        run: npm install -g @openai/codex

      - name: Check documentation
        run: |
          codex --profile ci exec \
            "Check whether README.md, best-practice/, and reports/ use the \
             current Codex CLI schema. List any stale paths, commands, or \
             configuration keys."
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## File: `examples/profiles/conservative.toml`
```
# Conservative Profile
#
# Maximum safety configuration for:
# - Untrusted repositories
# - Security-sensitive projects
# - New users learning Codex CLI
# - Code review and auditing
#
# Every action requires explicit approval. No file changes persist.
# This is the safest possible configuration.

model = "o4-mini"
approval_policy = "untrusted"
sandbox_mode = "read-only"

# Read-only sandbox prevents file changes and blocks network access.
#
# Usage:
#   codex --profile conservative
#
# Or copy to ~/.codex/config.toml as global default for maximum safety.
```

## File: `examples/profiles/development.toml`
```
# Development Profile
#
# Balanced configuration for day-to-day local development:
# - Workspace writes are allowed
# - The model can ask when it needs approval
# - Network blocked (no accidental data exfiltration)
#
# This is the recommended default for most developers.

model = "o4-mini"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

# Usage:
#   codex --profile development
#
# Recommended as the project default in .codex/config.toml.
# Override with --profile conservative when reviewing unfamiliar code.
```

## File: `examples/profiles/trusted-project.toml`
```
# Trusted Project Profile
#
# Permissive configuration for well-understood, trusted projects:
# - Full automation with broad allow-list
# - Network access enabled (for API calls, package installs)
# - No sandbox restrictions
#
# WARNING: This profile provides maximum autonomy. Use only when:
# - You fully trust the codebase
# - You need network access (APIs, package managers)
# - You have a good git safety net (working on branches, not main)
#
# NOT recommended for: untrusted repos, CI pipelines, security reviews.

model = "o3"
approval_policy = "never"
sandbox_mode = "danger-full-access"

# Safety notes:
# - sandbox_mode = "danger-full-access" means Codex has full filesystem and network access
# - approval_policy = "never" means Codex will not stop to ask before acting
# - Always work on a branch, never directly on main
# - Review changes with `git diff` before pushing
#
# Usage:
#   codex --profile trusted-project
```

## File: `orchestration-workflow/orchestration-workflow.md`
```markdown
# Orchestration Workflow

This document describes the **Agent → Skill** orchestration workflow, demonstrated through a weather data fetching and SVG rendering system.

<table width="100%">
<tr>
<td><a href="../">← Back to Codex CLI Best Practice</a></td>
<td align="right"><img src="../!/codex-jumping.svg" alt="Codex" width="60" /></td>
</tr>
</table>

## System Overview

The weather system demonstrates two component patterns within a single orchestration workflow:
- **Agent**: `weather-agent` fetches temperature from Open-Meteo using inlined `developer_instructions`
- **Skill** (independent): `weather-svg-creator` is invoked by the agent to create the visual output

This showcases the **Agent → Skill** architecture pattern, where:
- An agent fetches data and orchestrates the workflow
- A skill creates the visual output independently

## ![How to Use](../!/tags/how-to-use.svg)

```bash
codex
> Fetch the current weather for Dubai in Celsius and create the SVG weather card output using the repo.
```

Specify "in Fahrenheit" in your prompt to switch units. The agent defaults to Celsius if no preference is given.

Output files:
- `orchestration-workflow/weather.svg` — SVG weather card
- `orchestration-workflow/output.md` — Markdown summary

> **Note:** This workflow is not 100% in sync with the [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) orchestration workflow. Codex CLI does not yet support [custom commands](https://developers.openai.com/codex/cli/slash-commands) (`.codex/commands/`) or a stable ask-user tool for mid-turn user interaction. There is an experimental `tool/requestUserInput` in the [Codex App Server](https://developers.openai.com/codex) docs and an internal `request_user_input` capability gated behind an under-development feature flag in codex-cli 0.115.0, but neither is publicly available for normal CLI usage yet. As a result, the Codex pattern is **Agent → Skill** instead of **Command → Agent → Skill**, and the user must specify preferences (e.g., Celsius/Fahrenheit) in the prompt rather than being asked by the agent.

## Component Summary

| Component | Role | Example |
|-----------|------|---------|
| **Agent** | Entry point, data fetching, skill invocation | [`weather-agent`](../.codex/agents/weather-agent.toml) |
| **Skill** | Creates output independently | [`weather-svg-creator`](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) |

## Flow Diagram

<p align="center">
  <img src="../!/orchestration-workflow-diagram.svg" alt="Orchestration Workflow: Agent → Skill → Output" width="100%">
</p>

```
╔══════════════════════════════════════════════════════════════════╗
║              ORCHESTRATION WORKFLOW                              ║
║                    Agent  →  Skill                               ║
╚══════════════════════════════════════════════════════════════════╝

                         ┌───────────────────┐
                         │  User Prompt      │
                         │  (specifies C°/F°)│
                         └─────────┬─────────┘
                                   │
                         Step 1 — Agent
                                   │
                                   ▼
         ┌─────────────────────────────────────────────────────┐
         │  weather-agent — Agent ● developer_instructions     │
         └─────────────────────────┬───────────────────────────┘
                                   │
                          Returns: temp + unit
                                   │
                         Step 2 — Skill
                                   │
                                   ▼
         ┌─────────────────────────────────────────────────────┐
         │  weather-svg-creator — Skill ● SVG card + output    │
         └─────────────────────────┬───────────────────────────┘
                                   │
                          ┌────────┴────────┐
                          │                 │
                          ▼                 ▼
                   ┌────────────┐    ┌────────────┐
                   │weather.svg │    │ output.md  │
                   └────────────┘    └────────────┘
```

## Component Details

### 1. Agent

#### `weather-agent` (Agent)
- **Location**: `.codex/agents/weather-agent.toml`
- **Purpose**: Entry point — fetches temperature, invokes skill
- **Model**: o4-mini
- **Registration**: `[agents.weather-agent]` in `.codex/config.toml`

The agent's `developer_instructions` contain the full workflow: fetch from Open-Meteo API using curl (using the caller-provided unit preference, defaulting to Celsius), then invoke `/weather-svg-creator` with the data.

### 2. Skill

#### `weather-svg-creator` (Skill)
- **Location**: `.agents/skills/weather-svg-creator/SKILL.md`
- **Purpose**: Create a visual SVG weather card and write output files
- **Invocation**: Via skill invocation from the agent
- **Outputs**:
  - `orchestration-workflow/weather.svg` — SVG weather card
  - `orchestration-workflow/output.md` — Weather summary

## Execution Flow

1. **User Prompt**: User prompts Codex, specifying city and unit preference (e.g., "Dubai in Celsius")
2. **Agent Start**: Codex auto-selects `weather-agent` based on the task
3. **Data Fetching**: Agent fetches temperature from Open-Meteo API for Dubai using curl
4. **Skill Invocation**: Agent invokes `/weather-svg-creator` skill
   - Skill creates SVG weather card at `orchestration-workflow/weather.svg`
   - Skill writes summary to `orchestration-workflow/output.md`
5. **Result Display**: Summary shown to user with temperature, SVG location, and output file

## Example Execution

```
Input: Fetch the current weather for Dubai in Celsius and create the SVG weather card
├─ Step 1: Agent fetches from Open-Meteo API
│  └─ Returns: temperature=29, unit=Celsius, city=Dubai
├─ Step 2: Agent invokes skill → /weather-svg-creator
│  ├─ Creates: orchestration-workflow/weather.svg
│  └─ Writes: orchestration-workflow/output.md
└─ Output:
   ├─ Unit: Celsius
   ├─ Temperature: 29°C
   ├─ SVG: orchestration-workflow/weather.svg
   └─ Summary: orchestration-workflow/output.md
```

## Key Design Principles

1. **Agent as Entry Point**: The agent handles data fetching and skill invocation — no separate orchestrator needed
2. **Skill for Rendering**: The SVG creator runs independently, receiving data from the agent's context
3. **Inlined Instructions**: The agent's `developer_instructions` contain the fetching logic directly, since Codex CLI subagents do not support preloaded skills
4. **Clean Separation**: Fetch (agent) → Render (skill) — each component has a single responsibility
5. **Idempotent Output**: Running the workflow again overwrites the previous output cleanly

## Architecture Patterns

### Agent (Developer Instructions)

```toml
# In agent definition (.codex/agents/weather-agent.toml)
name = "weather-agent"
description = "Fetches temperature from Open-Meteo, invokes skill."
developer_instructions = """
Step 1: Fetch from Open-Meteo API (use caller's unit preference, default Celsius)
Step 2: Invoke /weather-svg-creator skill
"""
```

- **Self-contained**: The agent has everything it needs — data fetching and skill invocation
- **No preloaded skills**: Codex CLI subagents do not support the `skills:` preloading pattern
- **Prompt-driven skill invocation**: The agent tells Codex to invoke `/weather-svg-creator` via natural language instructions

### Skill (Direct Invocation)

```yaml
# In skill definition (.agents/skills/weather-svg-creator/SKILL.md)
---
name: weather-svg-creator
description: Creates an SVG weather card...
---
```

- **Invoked by agent**: Agent instructions tell Codex to invoke `/weather-svg-creator`
- **Independent execution**: Runs in the conversation context with the temperature data available
- **Receives data from context**: Uses temperature data already available in the conversation

## Comparison with Claude Code

| Aspect | Claude Code | Codex CLI |
|---|---|---|
| **Entry point** | Custom Command (`.claude/commands/`) | Agent (`.codex/agents/`) |
| **User interaction** | Command asks via `AskUserQuestion` tool | User specifies in prompt (no mid-turn asking) |
| **Data fetching** | Agent with preloaded skill | Agent with inlined `developer_instructions` |
| **Skill invocation** | `Skill()` tool call (deterministic) | `/skill-name` instruction (prompt-driven) |
| **Agent knowledge** | Preloaded skills via `skills:` field | Inlined via `developer_instructions` |
| **Pattern name** | Command → Agent → Skill | Agent → Skill |
| **Orchestration style** | Imperative (explicit tool calls) | Declarative (instruction-based) |
```

