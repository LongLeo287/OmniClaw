---
id: oh-my-openagent
type: knowledge
owner: OA_Triage
---
# oh-my-openagent
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "oh-my-opencode",
  "version": "3.15.1",
  "description": "The Best AI Agent Harness - Batteries-Included OpenCode Plugin with Multi-Model Orchestration, Parallel Background Agents, and Crafted LSP/AST Tools",
  "main": "./dist/index.js",
  "types": "dist/index.d.ts",
  "type": "module",
  "bin": {
    "oh-my-opencode": "bin/oh-my-opencode.js"
  },
  "files": [
    "dist",
    "bin",
    "postinstall.mjs"
  ],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    },
    "./schema.json": "./dist/oh-my-opencode.schema.json"
  },
  "scripts": {
    "build": "bun build src/index.ts --outdir dist --target bun --format esm --external @ast-grep/napi && tsc --emitDeclarationOnly && bun build src/cli/index.ts --outdir dist/cli --target bun --format esm --external @ast-grep/napi && bun run build:schema",
    "build:all": "bun run build && bun run build:binaries",
    "build:binaries": "bun run script/build-binaries.ts",
    "build:schema": "bun run script/build-schema.ts",
    "build:model-capabilities": "bun run script/build-model-capabilities.ts",
    "clean": "rm -rf dist",
    "prepare": "bun run build",
    "postinstall": "node postinstall.mjs",
    "prepublishOnly": "bun run clean && bun run build",
    "test:model-capabilities": "bun test src/shared/model-capability-aliases.test.ts src/shared/model-capability-guardrails.test.ts src/shared/model-capabilities.test.ts src/cli/doctor/checks/model-resolution.test.ts --bail",
    "typecheck": "tsc --noEmit",
    "test": "bun test"
  },
  "keywords": [
    "opencode",
    "plugin",
    "oracle",
    "librarian",
    "agents",
    "ai",
    "llm"
  ],
  "author": "YeonGyu-Kim",
  "license": "SUL-1.0",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/code-yeongyu/oh-my-openagent.git"
  },
  "bugs": {
    "url": "https://github.com/code-yeongyu/oh-my-openagent/issues"
  },
  "homepage": "https://github.com/code-yeongyu/oh-my-openagent#readme",
  "dependencies": {
    "@ast-grep/cli": "^0.41.1",
    "@ast-grep/napi": "^0.41.1",
    "@clack/prompts": "^0.11.0",
    "@code-yeongyu/comment-checker": "^0.7.0",
    "@modelcontextprotocol/sdk": "^1.25.2",
    "@opencode-ai/plugin": "^1.2.24",
    "@opencode-ai/sdk": "^1.2.24",
    "commander": "^14.0.2",
    "detect-libc": "^2.0.0",
    "diff": "^8.0.3",
    "js-yaml": "^4.1.1",
    "jsonc-parser": "^3.3.1",
    "picocolors": "^1.1.1",
    "picomatch": "^4.0.2",
    "vscode-jsonrpc": "^8.2.0",
    "zod": "^4.1.8"
  },
  "devDependencies": {
    "@types/js-yaml": "^4.0.9",
    "@types/picomatch": "^3.0.2",
    "bun-types": "1.3.11",
    "typescript": "^5.7.3"
  },
  "optionalDependencies": {
    "oh-my-opencode-darwin-arm64": "3.15.1",
    "oh-my-opencode-darwin-x64": "3.15.1",
    "oh-my-opencode-darwin-x64-baseline": "3.15.1",
    "oh-my-opencode-linux-arm64": "3.15.1",
    "oh-my-opencode-linux-arm64-musl": "3.15.1",
    "oh-my-opencode-linux-x64": "3.15.1",
    "oh-my-opencode-linux-x64-baseline": "3.15.1",
    "oh-my-opencode-linux-x64-musl": "3.15.1",
    "oh-my-opencode-linux-x64-musl-baseline": "3.15.1",
    "oh-my-opencode-windows-x64": "3.15.1",
    "oh-my-opencode-windows-x64-baseline": "3.15.1"
  },
  "overrides": {
    "@opencode-ai/sdk": "^1.2.24"
  },
  "trustedDependencies": [
    "@ast-grep/cli",
    "@ast-grep/napi",
    "@code-yeongyu/comment-checker"
  ]
}

```

### File: README.md
```md
> [!TIP]
> **Building in Public**
>
> The maintainer builds and maintains oh-my-opencode in real-time with Jobdori, an AI assistant built on a heavily customized fork of OpenClaw.
> Every feature, every fix, every issue triage — live in our Discord.
>
> [![Building in Public](./.github/assets/building-in-public.png)](https://discord.gg/PUwSMR9XNk)
>
> [**→ Watch it happen in #building-in-public**](https://discord.gg/PUwSMR9XNk)

> [!NOTE]
>
> [![Sisyphus Labs - Sisyphus is the agent that codes like your team.](./.github/assets/sisyphuslabs.png?v=2)](https://sisyphuslabs.ai)
> > **We're building a fully productized version of Sisyphus to define the future of frontier agents. <br />Join the waitlist [here](https://sisyphuslabs.ai).**

> [!TIP]
> Be with us!
>
> | [<img alt="Discord link" src="https://img.shields.io/discord/1452487457085063218?color=5865F2&label=discord&labelColor=black&logo=discord&logoColor=white&style=flat-square" width="156px" />](https://discord.gg/PUwSMR9XNk) | Join our [Discord community](https://discord.gg/PUwSMR9XNk) to connect with contributors and fellow `oh-my-opencode` users. |
> | :-----| :----- |
> | [<img alt="X link" src="https://img.shields.io/badge/Follow-%40justsisyphus-00CED1?style=flat-square&logo=x&labelColor=black" width="156px" />](https://x.com/justsisyphus) | News and updates for `oh-my-opencode` used to be posted on my X account. <br /> Since it was suspended mistakenly, [@justsisyphus](https://x.com/justsisyphus) now posts updates on my behalf. |
> | [<img alt="GitHub Follow" src="https://img.shields.io/github/followers/code-yeongyu?style=flat-square&logo=github&labelColor=black&color=24292f" width="156px" />](https://github.com/code-yeongyu) | Follow [@code-yeongyu](https://github.com/code-yeongyu) on GitHub for more projects. |

<!-- <CENTERED SECTION FOR GITHUB DISPLAY> -->

<div align="center">

[![Oh My OpenCode](./.github/assets/hero.jpg)](https://github.com/code-yeongyu/oh-my-openagent#oh-my-opencode)

[![Preview](./.github/assets/omo.png)](https://github.com/code-yeongyu/oh-my-openagent#oh-my-opencode)


</div>

> Anthropic [**blocked OpenCode because of us.**](https://x.com/thdxr/status/2010149530486911014) **Yes this is true.**
> They want you locked in. Claude Code's a nice prison, but it's still a prison.
>
> We don't do lock-in here. We ride every model. Claude / Kimi / GLM for orchestration. GPT for reasoning. Minimax for speed. Gemini for creativity.
> The future isn't picking one winner—it's orchestrating them all. Models get cheaper every month. Smarter every month. No single provider will dominate. We're building for that open market, not their walled gardens.

<div align="center">

[![GitHub Release](https://img.shields.io/github/v/release/code-yeongyu/oh-my-openagent?color=369eff&labelColor=black&logo=github&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/releases)
[![npm downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fohmyopenagent.com%2Fapi%2Fnpm-downloads&style=flat-square)](https://www.npmjs.com/package/oh-my-opencode)
[![GitHub Contributors](https://img.shields.io/github/contributors/code-yeongyu/oh-my-openagent?color=c4f042&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/graphs/contributors)
[![GitHub Forks](https://img.shields.io/github/forks/code-yeongyu/oh-my-openagent?color=8ae8ff&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/network/members)
[![GitHub Stars](https://img.shields.io/github/stars/code-yeongyu/oh-my-openagent?color=ffcb47&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/code-yeongyu/oh-my-openagent?color=ff80eb&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/issues)
[![License](https://img.shields.io/badge/license-SUL--1.0-white?labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/blob/dev/LICENSE.md)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/code-yeongyu/oh-my-openagent)

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-cn.md)

</div>

<!-- </CENTERED SECTION FOR GITHUB DISPLAY> -->

## Reviews

> "It made me cancel my Cursor subscription. Unbelievable things are happening in the open source community." - [Arthur Guiot](https://x.com/arthur_guiot/status/2008736347092382053?s=20)

> "If Claude Code does in 7 days what a human does in 3 months, Sisyphus does it in 1 hour. It just works until the task is done. It is a discipline agent." <br/>- B, Quant Researcher

> "Knocked out 8000 eslint warnings with Oh My Opencode, just in a day" <br/>- [Jacob Ferrari](https://x.com/jacobferrari_/status/2003258761952289061)

> "I converted a 45k line tauri app into a SaaS web app overnight using Ohmyopencode and ralph loop. Started with interview me prompt, asked it for ratings and recommendations on the questions. It was amazing to watch it work and to wake up this morning to a mostly working website!" - [James Hargis](https://x.com/hargabyte/status/2007299688261882202)

> "use oh-my-opencode, you will never go back" <br/>- [d0t3ch](https://x.com/d0t3ch/status/2001685618200580503)

> "I haven't really been able to articulate exactly what makes it so great yet, but the development experience has reached a completely different dimension." - [
苔硯:こけすずり](https://x.com/kokesuzuri/status/2008532913961529372?s=20)

> "Experimenting with open code, oh my opencode and supermemory this weekend to build some minecraft/souls-like abomination."
> "Asking it to add crouch animations while I go take my post-lunch walk. [Video]" - [MagiMetal](https://x.com/MagiMetal/status/2005374704178373023)

> "You guys should pull this into core and recruit him. Seriously. It's really, really, really good." <br/>- Henning Kilset

> "Hire @yeon_gyu_kim if you can convince him, this dude has revolutionized opencode." <br/>- [mysticaltech](https://x.com/mysticaltech/status/2001858758608376079)

> "Oh My OpenCode Is Actually Insane" - [YouTube - Darren Builds AI](https://www.youtube.com/watch?v=G_Snfh2M41M)

---

# Oh My OpenCode

You're juggling Claude Code, Codex, random OSS models. Configuring workflows. Debugging agents.

We did the work. Tested everything. Kept what actually shipped.

Install OmO. Type `ultrawork`. Done.


## Installation

### For Humans

Copy and paste this prompt to your LLM agent (Claude Code, AmpCode, Cursor, etc.):

```
Install and configure oh-my-opencode by following the instructions here:
https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

Or read the [Installation Guide](docs/guide/installation.md), but seriously, let an agent do it. Humans fat-finger configs.

### For LLM Agents

Fetch the installation guide and follow it:

```bash
curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

**Note**: Use the published package and binary name `oh-my-opencode`. Inside `opencode.json`, the compatibility layer now prefers the plugin entry `oh-my-openagent`, while legacy `oh-my-opencode` entries still load with a warning. Plugin config files still commonly use `oh-my-opencode.json` or `oh-my-opencode.jsonc`, and both legacy and renamed basenames are recognized during the transition.

---

## Skip This README

We're past the era of reading docs. Just paste this into your agent:

```
Read this and tell me why it's not just another boilerplate: https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/README.md
```

## Highlights

### 🪄 `ultrawork`

You're actually reading this? Wild.

Install. Type `ultrawork` (or `ulw`). Done.

Everything below, every feature, every optimization, you don't need to know it. It just works.

Even only with following subscriptions, ultrawork will work well (this project is not affiliated, this is just personal recommendation):
- [ChatGPT Subscription ($20)](https://chatgpt.com/)
- [Kimi Code Subscription ($0.99) (*only this month)](https://www.kimi.com/kimiplus/sale)
- [GLM Coding Plan ($10)](https://z.ai/subscribe)
- If you are eligible for pay-per-token, using kimi and gemini models won't cost you that much.

|       | Feature                                                  | What it does                                                                                                                                                                                                     |
| :---: | :------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   🤖   | **Discipline Agents**                                    | Sisyphus orchestrates Hephaestus, Oracle, Librarian, Explore. A full AI dev team in parallel.                                                                                                                    |
|   ⚡   | **`ultrawork` / `ulw`**                                  | One word. Every agent activates. Doesn't stop until done.                                                                                                                                                        |
|   🚪   | **[IntentGate](https://factory.ai/news/terminal-bench)** | Analyzes true user intent before classifying or acting. No more literal misinterpretations.                                                                                                                      |
|   🔗   | **Hash-Anchored Edit Tool**                              | `LINE#ID` content hash validates every change. Zero stale-line errors. Inspired by [oh-my-pi](https://github.com/can1357/oh-my-pi). [The Harness Problem →](https://blog.can.ac/2026/02/12/the-harness-problem/) |
|   🛠️   | **LSP + AST-Grep**                                       | Workspace rename, pre-build diagnostics, AST-aware rewrites. IDE precision for agents.                                                                                                                           |
|   🧠   | **Background Agents**                                    | Fire 5+ specialists in parallel. Context stays lean. Results when ready.                                                                                                                                         |
|   📚   | **Built-in MCPs**                                        | Exa (web search), Context7 (official docs), Grep.app (GitHub search). Always on.                                                                                                                                 |
|   🔁   | **Ralph Loop / `/ulw-loop`**                             | Self-referential loop. Doesn't stop until 100% done.                                                                                                                                                             |
|   ✅   | **Todo Enforcer**                                        | Agent goes idle? System yanks it back. Your task gets done, period.                                                                                                                                              |
|   💬   | **Comment Checker**                                      | No AI slop in comments. Code reads like a senior wrote it.                                                                                                                                                       |
|   🖥️   | **Tmux Integration**                                     | Full interactive terminal. REPLs, debuggers, TUIs. All live.                                                                                                                                                     |
|   🔌   | **Claude Code Compatible**                               | Your hooks, commands, skills, MCPs, and plugins? All work here.                                                                                                                                                  |
|   🎯   | **Skill-Embedded MCPs**                                  | Skills carry their own MCP servers. No context bloat.                                                                                                                                                            |
|   📋   | **Prometheus Planner**                                   | Interview-mode strategic planning before any execution.                                                                                                                                                          |
|   🔍   | **`/init-deep`**                                         | Auto-generates hierarchical `AGENTS.md` files throughout your project. Great for both token efficiency and your agent's performance                                                                              |

### Discipline Agents

<table><tr>
<td align="center"><img src=".github/assets/sisyphus.png" height="300" /></td>
<td align="center"><img src=".github/assets/hephaestus.png" height="300" /></td>
</tr></table>

**Sisyphus** (`claude-opus-4-6` / **`kimi-k2.5`** / **`glm-5`** ) is your main orchestrator. He plans, delegates to specialists, and drives tasks to completion with aggressive parallel execution. He does not stop halfway.

**Hephaestus** (`gpt-5.4`) is your autonomous deep worker. Give him a goal, not a recipe. He explores the codebase, researches patterns, and executes end-to-end without hand-holding. *The Legitimate Craftsman.*

**Prometheus** (`claude-opus-4-6` / **`kimi-k2.5`** / **`glm-5`** ) is your strategic planner. Interview mode: it questions, identifies scope, and builds a detailed plan before a single line of code is touched.

Every agent is tuned to its model's specific strengths. No manual model-juggling. [Learn more →](docs/guide/overview.md)

> Anthropic [blocked OpenCode because of us.](https://x.com/thdxr/status/2010149530486911014) That's why Hephaestus is called "The Legitimate Craftsman." The irony is intentional.
>
> We run best on Opus, but Kimi K2.5 + GPT-5.4 already beats vanilla Claude Code. Zero config needed.

### Agent Orchestration

When Sisyphus delegates to a subagent, it doesn't pick a model. It picks a **category**. The category maps automatically to the right model:

| Category             | What it's for                      |
| :------------------- | :--------------------------------- |
| `visual-engineering` | Frontend, UI/UX, design            |
| `deep`               | Autonomous research + execution    |
| `quick`              | Single-file changes, typos         |
| `ultrabrain`         | Hard logic, architecture decisions |

Agent says what kind of work. Harness picks the right model. `ultrabrain` now routes to GPT-5.4 
... [TRUNCATED]
```

### File: AGENTS.md
```md
# oh-my-opencode — O P E N C O D E Plugin

**Generated:** 2026-03-06 | **Commit:** 7fe44024 | **Branch:** dev

## OVERVIEW

OpenCode plugin (npm: `oh-my-opencode`) that extends Claude Code (OpenCode fork) with multi-agent orchestration, 48 lifecycle hooks, 26 tools, skill/command/MCP systems, and Claude Code compatibility. 1268 TypeScript files, 160k LOC.

## STRUCTURE

```
oh-my-opencode/
├── src/
│   ├── index.ts              # Plugin entry: loadConfig → createManagers → createTools → createHooks → createPluginInterface
│   ├── plugin-config.ts      # JSONC multi-level config: user → project → defaults (Zod v4)
│   ├── agents/               # 11 agents (Sisyphus, Hephaestus, Oracle, Librarian, Explore, Atlas, Prometheus, Metis, Momus, Multimodal-Looker, Sisyphus-Junior)
│   ├── hooks/                # 48 lifecycle hooks across dedicated modules and standalone files
│   ├── tools/                # 26 tools across 15 directories
│   ├── features/             # 19 feature modules (background-agent, skill-loader, tmux, MCP-OAuth, etc.)
│   ├── shared/               # 95+ utility files in 13 categories
│   ├── config/               # Zod v4 schema system (24 files)
│   ├── cli/                  # CLI: install, run, doctor, mcp-oauth (Commander.js)
│   ├── mcp/                  # 3 built-in remote MCPs (websearch, context7, grep_app)
│   ├── plugin/               # 8 OpenCode hook handlers + 48 hook composition
│   └── plugin-handlers/      # 6-phase config loading pipeline
├── packages/                 # Monorepo: cli-runner, 12 platform binaries
└── local-ignore/             # Dev-only test fixtures
```

## INITIALIZATION FLOW

```
OhMyOpenCodePlugin(ctx)
  ├─→ loadPluginConfig()         # JSONC parse → project/user merge → Zod validate → migrate
  ├─→ createManagers()           # TmuxSessionManager, BackgroundManager, SkillMcpManager, ConfigHandler
  ├─→ createTools()              # SkillContext + AvailableCategories + ToolRegistry (26 tools)
  ├─→ createHooks()              # 3-tier: Core(39) + Continuation(7) + Skill(2) = 48 hooks
  └─→ createPluginInterface()    # 8 OpenCode hook handlers → PluginInterface
```

## 8 OPENCODE HOOK HANDLERS

| Handler | Purpose |
|---------|---------|
| `config` | 6-phase: provider → plugin-components → agents → tools → MCPs → commands |
| `tool` | 26 registered tools |
| `chat.message` | First-message variant, session setup, keyword detection |
| `chat.params` | Anthropic effort level adjustment |
| `chat.headers` | Copilot x-initiator header injection |
| `event` | Session lifecycle (created, deleted, idle, error) |
| `tool.execute.before` | Pre-tool hooks (file guard, label truncator, rules injector) |
| `tool.execute.after` | Post-tool hooks (output truncation, metadata store) |
| `experimental.chat.messages.transform` | Context injection, thinking block validation |

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Add new agent | `src/agents/` + `src/agents/builtin-agents/` | Follow createXXXAgent factory pattern |
| Add new hook | `src/hooks/{name}/` + register in `src/plugin/hooks/create-*-hooks.ts` | Match event type to tier |
| Add new tool | `src/tools/{name}/` + register in `src/plugin/tool-registry.ts` | Follow createXXXTool factory |
| Add new feature module | `src/features/{name}/` | Standalone module, wire in plugin/ |
| Add new MCP | `src/mcp/` + register in `createBuiltinMcps()` | Remote HTTP only |
| Add new skill | `src/features/builtin-skills/skills/` | Implement BuiltinSkill interface |
| Add new command | `src/features/builtin-commands/` | Template in templates/ |
| Add new CLI command | `src/cli/cli-program.ts` | Commander.js subcommand |
| Add new doctor check | `src/cli/doctor/checks/` | Register in checks/index.ts |
| Modify config schema | `src/config/schema/` + update root schema | Zod v4, add to OhMyOpenCodeConfigSchema |
| Add new category | `src/tools/delegate-task/constants.ts` | DEFAULT_CATEGORIES + CATEGORY_MODEL_REQUIREMENTS |

## MULTI-LEVEL CONFIG

```
Project (.opencode/oh-my-opencode.jsonc)  →  User (~/.config/opencode/oh-my-opencode.jsonc)  →  Defaults
```

- `agents`, `categories`, `claude_code`: deep merged recursively
- `disabled_*` arrays: Set union (concatenated + deduplicated)
- All other fields: override replaces base value
- Zod `safeParse()` fills defaults for omitted fields
- `migrateConfigFile()` transforms legacy keys automatically

Fields: agents (14 overridable, 21 fields each), categories (8 built-in + custom), disabled_* arrays (agents, hooks, mcps, skills, commands, tools), 19 feature-specific configs.

## THREE-TIER MCP SYSTEM

| Tier | Source | Mechanism |
|------|--------|-----------|
| Built-in | `src/mcp/` | 3 remote HTTP: websearch (Exa/Tavily), context7, grep_app |
| Claude Code | `.mcp.json` | `${VAR}` env expansion via claude-code-mcp-loader |
| Skill-embedded | SKILL.md YAML | Managed by SkillMcpManager (stdio + HTTP) |

## CONVENTIONS

- **Runtime**: Bun only — never use npm/yarn
- **TypeScript**: strict mode, ESNext, bundler moduleResolution, `bun-types` (never `@types/node`)
- **Test pattern**: Bun test (`bun:test`), co-located `*.test.ts`, given/when/then style (nested describe with `#given`/`#when`/`#then` prefixes)
- **CI test split**: mock-heavy tests run in isolation (separate `bun test` processes), rest in batch
- **Factory pattern**: `createXXX()` for all tools, hooks, agents
- **Hook tiers**: Session (23) → Tool-Guard (12) → Transform (4) → Continuation (7) → Skill (2)
- **Agent modes**: `primary` (respects UI model) vs `subagent` (own fallback chain) vs `all`
- **Model resolution**: 4-step: override → category-default → provider-fallback → system-default
- **Config format**: JSONC with comments, Zod v4 validation, snake_case keys
- **File naming**: kebab-case for all files/directories
- **Module structure**: index.ts barrel exports, no catch-all files (utils.ts, helpers.ts banned), 200 LOC soft limit
- **Imports**: relative within module, barrel imports across modules (`import { log } from "./shared"`)
- **No path aliases**: no `@/` — relative imports only

## ANTI-PATTERNS

- Never use `as any`, `@ts-ignore`, `@ts-expect-error`
- Never suppress lint/type errors
- Never add emojis to code/comments unless user explicitly asks
- Never commit unless explicitly requested
- Never run `bun publish` directly — use GitHub Actions
- Never modify `package.json` version locally
- Test: given/when/then — never use Arrange-Act-Assert comments
- Comments: avoid AI-generated comment patterns (enforced by comment-checker hook)
- Never create catch-all files (`utils.ts`, `helpers.ts`, `service.ts`)
- Empty catch blocks `catch(e) {}` — always handle errors
- Never use em dashes (—), en dashes (–), or AI filler phrases in generated content
- index.ts is entry point ONLY — never dump business logic there

## COMMANDS

```bash
bun test                    # Bun test suite
bun run build              # Build plugin (ESM + declarations + schema)
bun run build:all          # Build + platform binaries
bun run typecheck           # tsc --noEmit
bunx oh-my-opencode install # Interactive setup
bunx oh-my-opencode doctor  # Health diagnostics
bunx oh-my-opencode run     # Non-interactive session
```

## CI/CD

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| ci.yml | push/PR to master/dev | Tests (split: mock-heavy isolated + batch), typecheck, build, schema auto-commit |
| publish.yml | manual dispatch | Version bump, npm publish, platform binaries, GitHub release, merge to master |
| publish-platform.yml | called by publish | 12 platform binaries via bun compile (darwin/linux/windows) |
| sisyphus-agent.yml | @mention / dispatch | AI agent handles issues/PRs |
| cla.yml | issue_comment/PR | CLA assistant for contributors |
| lint-workflows.yml | push to .github/ | actionlint + shellcheck on workflow files |

## NOTES

- Logger writes to `/tmp/oh-my-opencode.log` — check there for debugging
- Background tasks: 5 concurrent per model/provider (configurable)
- Plugin load timeout: 10s for Claude Code plugins
- Model fallback priority: Claude > OpenAI > Gemini > Copilot > OpenCode Zen > Z.ai > Kimi
- Config migration runs automatically on legacy keys (agent names, hook names, model versions)
- Build: bun build (ESM) + tsc --emitDeclarationOnly, externals: @ast-grep/napi
- Test setup: `test-setup.ts` preloaded via bunfig.toml, mock-heavy tests run in isolation in CI
- 98 barrel export files (index.ts) establish module boundaries
- Architecture rules enforced via `.sisyphus/rules/modular-code-enforcement.md`

```

### File: bun-test.d.ts
```ts
declare module "bun:test" {
  type AnyFunction = (...args: any[]) => any

  interface MockMetadata<TArgs extends unknown[]> {
    calls: TArgs[]
  }

  interface MockFunction<TFunction extends AnyFunction = AnyFunction> {
    (...args: Parameters<TFunction>): ReturnType<TFunction>
    mock: MockMetadata<Parameters<TFunction>>
    mockClear(): void
    mockReset(): void
    mockRestore(): void
    mockReturnValue(value: ReturnType<TFunction>): void
    mockResolvedValue(value: Awaited<ReturnType<TFunction>>): void
    mockImplementation(fn: TFunction): MockFunction<TFunction>
  }

  export function describe(name: string, fn: () => void): void
  export function test(name: string, fn: () => void | Promise<void>): void
  export function it(name: string, fn: () => void | Promise<void>): void
  export function beforeEach(fn: () => void | Promise<void>): void
  export function afterEach(fn: () => void | Promise<void>): void
  export function beforeAll(fn: () => void | Promise<void>): void
  export function afterAll(fn: () => void | Promise<void>): void
  export function mock<TFunction extends AnyFunction>(fn: TFunction): MockFunction<TFunction>

  export function spyOn<TObject extends object>(
    object: TObject,
    key: keyof TObject,
  ): MockFunction<AnyFunction>

  export namespace mock {
    function module(modulePath: string, factory: () => Record<string, unknown>): void
    function restore(): void
  }

  interface Matchers {
    toBe(expected: unknown): void
    toBeDefined(): void
    toBeUndefined(): void
    toBeNull(): void
    toEqual(expected: unknown): void
    toContain(expected: unknown): void
    toMatch(expected: RegExp | string): void
    toHaveLength(expected: number): void
    toHaveBeenCalled(): void
    toHaveBeenCalledTimes(expected: number): void
    toHaveBeenCalledWith(...expected: unknown[]): void
    toBeGreaterThan(expected: number): void
    toThrow(expected?: RegExp | string): void
    toStartWith(expected: string): void
    not: Matchers
  }

  export function expect(received: unknown): Matchers
}

```

### File: CLA.md
```md
# Contributor License Agreement

Thank you for your interest in contributing to oh-my-opencode ("Project"), owned by YeonGyu Kim ("Owner").

By signing this Contributor License Agreement ("Agreement"), you agree to the following terms:

## 1. Definitions

- **"Contribution"** means any original work of authorship, including any modifications or additions to existing work, that you submit to the Project.
- **"Submit"** means any form of communication sent to the Project, including but not limited to pull requests, issues, commits, and documentation changes.

## 2. Grant of Rights

By submitting a Contribution, you grant the Owner:

1. **Copyright License**: A perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare derivative works of, publicly display, publicly perform, sublicense, and distribute your Contributions and such derivative works.

2. **Patent License**: A perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Contribution.

3. **Relicensing Rights**: The right to relicense the Contribution under any license, including proprietary licenses, without requiring additional permission from you.

## 3. Representations

You represent that:

1. You are legally entitled to grant the above licenses.
2. Each Contribution is your original creation or you have sufficient rights to submit it.
3. Your Contribution does not violate any third party's intellectual property rights.
4. If your employer has rights to intellectual property that you create, you have received permission to make Contributions on behalf of that employer.

## 4. No Obligation

You understand that:

1. The Owner is not obligated to use or include your Contribution.
2. The decision to include any Contribution is at the sole discretion of the Owner.
3. You are not entitled to any compensation for your Contributions.

## 5. Future License Changes

You acknowledge and agree that:

1. The Project may change its license in the future.
2. Your Contributions may be distributed under a different license than the one in effect at the time of your Contribution.
3. This includes, but is not limited to, relicensing under source-available or proprietary licenses.

## 6. Miscellaneous

- This Agreement is governed by the laws of the Republic of Korea.
- This Agreement represents the entire agreement between you and the Owner concerning Contributions.

---

## How to Sign

By submitting a pull request to this repository, you agree to the terms of this Contributor License Agreement. The CLA Assistant bot will automatically track your agreement.

If you have any questions, please open an issue or contact the Owner.

```

### File: CONTRIBUTING.md
```md
# Contributing to Oh My OpenCode

First off, thanks for taking the time to contribute! This document provides guidelines and instructions for contributing to oh-my-opencode.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Development Setup](#development-setup)
  - [Testing Your Changes Locally](#testing-your-changes-locally)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
  - [Build Commands](#build-commands)
  - [Code Style & Conventions](#code-style--conventions)
- [Making Changes](#making-changes)
  - [Adding a New Agent](#adding-a-new-agent)
  - [Adding a New Hook](#adding-a-new-hook)
  - [Adding a New Tool](#adding-a-new-tool)
  - [Adding a New MCP Server](#adding-a-new-mcp-server)
- [Pull Request Process](#pull-request-process)
- [Publishing](#publishing)
- [Getting Help](#getting-help)

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to make better tools together.

## Language Policy

**English is the primary language for all communications in this repository.**

This includes:

- Issues and bug reports
- Pull requests and code reviews
- Documentation and comments
- Discussions and community interactions

### Why English?

- **Global Accessibility**: English allows contributors from all regions to collaborate effectively
- **Consistency**: A single language keeps discussions organized and searchable
- **Open Source Best Practice**: Most successful open-source projects use English as the lingua franca

### Need Help with English?

If English isn't your first language, don't worry! We value your contributions regardless of perfect grammar. You can:

- Use translation tools to help compose messages
- Ask for help from other community members
- Focus on clear, simple communication rather than perfect prose

## Getting Started

### Prerequisites

- **Bun** (latest version) - The only supported package manager
- **TypeScript 5.7.3+** - For type checking and declarations
- **OpenCode 1.0.150+** - For testing the plugin

### Development Setup

```bash
# Clone the repository
git clone https://github.com/code-yeongyu/oh-my-openagent.git
cd oh-my-openagent

# Install dependencies (bun only - never use npm/yarn)
bun install

# Build the project
bun run build
```

### Testing Your Changes Locally

After making changes, you can test your local build in OpenCode:

1. **Build the project**:

   ```bash
   bun run build
   ```

2. **Update your OpenCode config** (`~/.config/opencode/opencode.json` or `opencode.jsonc`):

   ```json
   {
     "plugin": ["file:///absolute/path/to/oh-my-opencode/dist/index.js"]
   }
   ```

   For example, if your project is at `/Users/yourname/projects/oh-my-opencode`:

   ```json
   {
     "plugin": ["file:///Users/yourname/projects/oh-my-opencode/dist/index.js"]
   }
   ```

   > **Note**: Remove `"oh-my-opencode"` from the plugin array if it exists, to avoid conflicts with the npm version.

3. **Restart OpenCode** to load the changes.

4. **Verify** the plugin is loaded by checking for OmO agent availability or startup messages.

## Project Structure

```
oh-my-opencode/
├── src/
│   ├── index.ts         # Plugin entry (OhMyOpenCodePlugin)
│   ├── plugin-config.ts # JSONC multi-level config (Zod v4)
│   ├── agents/          # 11 agents (Sisyphus, Hephaestus, Oracle, Librarian, Explore, Atlas, Prometheus, Metis, Momus, Multimodal-Looker, Sisyphus-Junior)
│   ├── hooks/           # Lifecycle hooks for orchestration, recovery, UX, and context management
│   ├── tools/           # 26 tools across 15 directories
│   ├── mcp/             # 3 built-in remote MCPs (websearch, context7, grep_app)
│   ├── features/        # 19 feature modules (background-agent, skill-loader, tmux, MCP-OAuth, etc.)
│   ├── config/          # Zod v4 schema system
│   ├── shared/          # Cross-cutting utilities
│   ├── cli/             # CLI: install, run, doctor, mcp-oauth (Commander.js)
│   ├── plugin/          # 8 OpenCode hook handlers + hook composition
│   └── plugin-handlers/ # 6-phase config loading pipeline
├── packages/            # Monorepo: comment-checker, opencode-sdk
└── dist/                # Build output (ESM + .d.ts)
```

## Development Workflow

### Build Commands

```bash
# Type check only
bun run typecheck

# Full build (ESM + TypeScript declarations + JSON schema)
bun run build

# Clean build output
bun run clean

# Rebuild from scratch
bun run clean && bun run build

# Build schema only (after modifying src/config/schema.ts)
bun run build:schema
```

### Code Style & Conventions

| Convention       | Rule                                                                      |
| ---------------- | ------------------------------------------------------------------------- |
| Package Manager  | **Bun only** (`bun run`, `bun build`, `bunx`)                             |
| Types            | Use `bun-types`, not `@types/node`                                        |
| Directory Naming | kebab-case (`ast-grep/`, `claude-code-hooks/`)                            |
| File Operations  | Never use bash commands (mkdir/touch/rm) for file creation in code        |
| Tool Structure   | Each tool: `index.ts`, `types.ts`, `constants.ts`, `tools.ts`, `utils.ts` |
| Hook Pattern     | `createXXXHook(input: PluginInput)` function naming                       |
| Exports          | Barrel pattern (`export * from "./module"` in index.ts)                   |

**Anti-Patterns (Do Not Do)**:

- Using npm/yarn instead of bun
- Using `@types/node` instead of `bun-types`
- Suppressing TypeScript errors with `as any`, `@ts-ignore`, `@ts-expect-error`
- Generic AI-generated comment bloat
- Direct `bun publish` (use GitHub Actions only)
- Local version modifications in `package.json`

## Making Changes

### Adding a New Agent

1. Create a new `.ts` file in `src/agents/`
2. Define the agent configuration following existing patterns
3. Add to `builtinAgents` in `src/agents/index.ts`
4. Update `src/agents/types.ts` if needed
5. Run `bun run build:schema` to update the JSON schema

```typescript
// src/agents/my-agent.ts
import type { AgentConfig } from "./types";

export const myAgent: AgentConfig = {
  name: "my-agent",
  model: "anthropic/claude-opus-4-6",
  description: "Description of what this agent does",
  prompt: `Your agent's system prompt here`,
  temperature: 0.1,
  // ... other config
};
```

### Adding a New Hook

1. Create a new directory in `src/hooks/` (kebab-case)
2. Implement `createXXXHook()` function returning event handlers
3. Export from `src/hooks/index.ts`

```typescript
// src/hooks/my-hook/index.ts
import type { PluginInput } from "@opencode-ai/plugin";

export function createMyHook(input: PluginInput) {
  return {
    onSessionStart: async () => {
      // Hook logic here
    },
  };
}
```

### Adding a New Tool

1. Create a new directory in `src/tools/` with required files:
   - `index.ts` - Main exports
   - `types.ts` - TypeScript interfaces
   - `constants.ts` - Constants and tool descriptions
   - `tools.ts` - Tool implementations
   - `utils.ts` - Helper functions
2. Add to `builtinTools` in `src/tools/index.ts`

### Adding a New MCP Server

1. Create configuration in `src/mcp/`
2. Add to `src/mcp/index.ts`
3. Document in README if it requires external setup

## Pull Request Process

1. **Fork** the repository and create your branch from `dev`
2. **Make changes** following the conventions above
3. **Build and test** locally:
   ```bash
   bun run typecheck  # Ensure no type errors
   bun run build      # Ensure build succeeds
   ```
4. **Test in OpenCode** using the local build method described above
5. **Commit** with clear, descriptive messages:
   - Use present tense ("Add feature" not "Added feature")
   - Reference issues if applicable ("Fix #123")
6. **Push** to your fork and create a Pull Request
7. **Describe** your changes clearly in the PR description

### PR Checklist

- [ ] Code follows project conventions
- [ ] `bun run typecheck` passes
- [ ] `bun run build` succeeds
- [ ] Tested locally with OpenCode
- [ ] Updated documentation if needed (README, AGENTS.md)
- [ ] No version changes in `package.json`

## Publishing

**Important**: Publishing is handled exclusively through GitHub Actions.

- **Never** run `bun publish` directly (OIDC provenance issues)
- **Never** modify `package.json` version locally
- Maintainers use GitHub Actions workflow_dispatch:
  ```bash
  gh workflow run publish -f bump=patch  # or minor/major
  ```

## Getting Help

- **Project Knowledge**: Check `AGENTS.md` for detailed project documentation
- **Code Patterns**: Review existing implementations in `src/`
- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Start a discussion for questions or ideas

---

Thank you for contributing to Oh My OpenCode! Your efforts help make AI-assisted coding better for everyone.

```

### File: LICENSE.md
```md
# License

Portions of this software are licensed as follows:

- All third party components incorporated into the oh-my-opencode Software are licensed under the original license
  provided by the owner of the applicable component.
- Content outside of the above mentioned files or restrictions is available under the "Sustainable Use
  License" as defined below.

## Sustainable Use License

Version 1.0

### Acceptance

By using the software, you agree to all of the terms and conditions below.

### Copyright License

The licensor grants you a non-exclusive, royalty-free, worldwide, non-sublicensable, non-transferable license
to use, copy, distribute, make available, and prepare derivative works of the software, in each case subject
to the limitations below.

### Limitations

You may use or modify the software only for your own internal business purposes or for non-commercial or
personal use. You may distribute the software or provide it to others only if you do so free of charge for
non-commercial purposes. You may not alter, remove, or obscure any licensing, copyright, or other notices of
the licensor in the software. Any use of the licensor's trademarks is subject to applicable law.

### Patents

The licensor grants you a license, under any patent claims the licensor can license, or becomes able to
license, to make, have made, use, sell, offer for sale, import and have imported the software, in each case
subject to the limitations and conditions in this license. This license does not cover any patent claims that
you cause to be infringed by modifications or additions to the software. If you or your company make any
written claim that the software infringes or contributes to infringement of any patent, your patent license
for the software granted under these terms ends immediately. If your company makes such a claim, your patent
license ends immediately for work on behalf of your company.

### Notices

You must ensure that anyone who gets a copy of any part of the software from you also gets a copy of these
terms. If you modify the software, you must include in any modified copies of the software a prominent notice
stating that you have modified the software.

### No Other Rights

These terms do not imply any licenses other than those expressly granted in these terms.

### Termination

If you use the software in violation of these terms, such use is not licensed, and your license will
automatically terminate. If the licensor provides you with a notice of your violation, and you cease all
violation of this license no later than 30 days after you receive that notice, your license will be reinstated
retroactively. However, if you violate these terms after such reinstatement, any additional violation of these
terms will cause your license to terminate automatically and permanently.

### No Liability

As far as the law allows, the software comes as is, without any warranty or condition, and the licensor will
not be liable to you for any damages arising out of these terms or the use or nature of the software, under
any kind of legal claim.

### Definitions

The "licensor" is the entity offering these terms.

The "software" is the software the licensor makes available under these terms, including any portion of it.

"You" refers to the individual or entity agreeing to these terms.

"Your company" is any legal entity, sole proprietorship, or other kind of organization that you work for, plus
all organizations that have control over, are under the control of, or are under common control with that
organization. Control means ownership of substantially all the assets of an entity, or the power to direct its
management and policies by vote, contract, or otherwise. Control can be direct or indirect.

"Your license" is the license granted to you for the software under these terms.

"Use" means anything you do with the software requiring your license.

"Trademark" means trademarks, service marks, and similar rights.

```

### File: README.ja.md
```md
> [!WARNING]
> **一時的なお知らせ（今週）: メンテナー対応遅延のお知らせ**
>
> コアメンテナーのQが負傷したため、今週は Issue/PR への返信とリリースが遅れる可能性があります。
> ご理解とご支援に感謝します。

> [!TIP]
> **Building in Public**
>
> メンテナーが Jobdori を使い、oh-my-opencode をリアルタイムで開発・メンテナンスしています。Jobdori は OpenClaw をベースに大幅カスタマイズされた AI アシスタントです。
> すべての機能開発、修正、Issue トリアージを Discord でライブでご覧いただけます。
>
> [![Building in Public](./.github/assets/building-in-public.png)](https://discord.gg/PUwSMR9XNk)
>
> [**→ #building-in-public で確認する**](https://discord.gg/PUwSMR9XNk)


> [!NOTE]
>
> [![Sisyphus Labs - Sisyphus is the agent that codes like your team.](./.github/assets/sisyphuslabs.png?v=2)](https://sisyphuslabs.ai)
> > **私たちは、フロンティアエージェントの未来を定義するために、Sisyphusの完全なプロダクト版を構築しています。 <br />[こちら](https://sisyphuslabs.ai)からウェイトリストにご登録ください。**

> [!TIP]
> 私たちと一緒に！
>
> | [<img alt="Discord link" src="https://img.shields.io/discord/1452487457085063218?color=5865F2&label=discord&labelColor=black&logo=discord&logoColor=white&style=flat-square" width="156px" />](https://discord.gg/PUwSMR9XNk) | [Discordコミュニティ](https://discord.gg/PUwSMR9XNk)に参加して、コントリビューターや他の `oh-my-opencode` ユーザーと交流しましょう。 |
> | :-----| :----- |
> | [<img alt="X link" src="https://img.shields.io/badge/Follow-%40justsisyphus-00CED1?style=flat-square&logo=x&labelColor=black" width="156px" />](https://x.com/justsisyphus) | `oh-my-opencode` のニュースやアップデートは私のXアカウントで投稿されていましたが、 <br /> 誤って凍結されてしまったため、現在は [@justsisyphus](https://x.com/justsisyphus) が代わりにアップデートを投稿しています。 |
> | [<img alt="GitHub Follow" src="https://img.shields.io/github/followers/code-yeongyu?style=flat-square&logo=github&labelColor=black&color=24292f" width="156px" />](https://github.com/code-yeongyu) | さらに多くのプロジェクトを見たい場合は、GitHubで [@code-yeongyu](https://github.com/code-yeongyu) をフォローしてください。 |

<!-- <CENTERED SECTION FOR GITHUB DISPLAY> -->

<div align="center">

[![Oh My OpenCode](./.github/assets/hero.jpg)](https://github.com/code-yeongyu/oh-my-openagent#oh-my-opencode)

[![Preview](./.github/assets/omo.png)](https://github.com/code-yeongyu/oh-my-openagent#oh-my-opencode)

</div>

> これはステロイドを打ったコーディングです。一つのモデルのステロイドじゃない——薬局丸ごとです。
>
> Claudeでオーケストレーションし、GPTで推論し、Kimiでスピードを出し、Geminiでビジョンを処理する。モデルはどんどん安くなり、どんどん賢くなる。特定のプロバイダーが独占することはない。私たちはその開かれた市場のために構築している。Anthropicの牢獄は素敵だ。だが、私たちはそこに住まない。

<div align="center">

[![GitHub Release](https://img.shields.io/github/v/release/code-yeongyu/oh-my-openagent?color=369eff&labelColor=black&logo=github&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/releases)
[![npm downloads](https://img.shields.io/npm/dt/oh-my-opencode?color=ff6b35&labelColor=black&style=flat-square)](https://www.npmjs.com/package/oh-my-opencode)
[![GitHub Contributors](https://img.shields.io/github/contributors/code-yeongyu/oh-my-openagent?color=c4f042&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/graphs/contributors)
[![GitHub Forks](https://img.shields.io/github/forks/code-yeongyu/oh-my-openagent?color=8ae8ff&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/network/members)
[![GitHub Stars](https://img.shields.io/github/stars/code-yeongyu/oh-my-openagent?color=ffcb47&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/code-yeongyu/oh-my-openagent?color=ff80eb&labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/issues)
[![License](https://img.shields.io/badge/license-SUL--1.0-white?labelColor=black&style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent/blob/dev/LICENSE.md)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/code-yeongyu/oh-my-openagent)

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-cn.md)

</div>

<!-- </CENTERED SECTION FOR GITHUB DISPLAY> -->

## レビュー

> 「これのおかげで Cursor のサブスクリプションを解約しました。オープンソースコミュニティで信じられないことが起きています。」 - [Arthur Guiot](https://x.com/arthur_guiot/status/2008736347092382053?s=20)

> 「Claude Codeが人間なら3ヶ月かかることを7日でやるとしたら、Sisyphusはそれを1時間でやってのけます。タスクが終わるまでひたすら働き続けます。まさに規律あるエージェントです。」 <br/>- B, Quant Researcher

> 「Oh My Opencodeを使って、たった1日で8000個の eslint 警告を叩き潰しました。」 <br/>- [Jacob Ferrari](https://x.com/jacobferrari_/status/2003258761952289061)

> 「Ohmyopencodeとralph loopを使って、45k行のtauriアプリを一晩でSaaSウェブアプリに変換しました。インタビューモードから始めて、私のプロンプトに対して質問や推奨事項を尋ねました。勝手に作業していくのを見るのは楽しかったし、今朝起きたらウェブサイトがほぼ動いているのを見て驚愕しました！」 - [James Hargis](https://x.com/hargabyte/status/2007299688261882202)

> 「oh-my-opencodeを使ってください。もう二度と元には戻れません。」 <br/>- [d0t3ch](https://x.com/d0t3ch/status/2001685618200580503)

> 「何がどうすごいのかまだ上手く言語化できないんですが、開発体験が完全に異次元に到達してしまいました。」 - [苔硯:こけすずり](https://x.com/kokesuzuri/status/2008532913961529372?s=20)

> 「週末にマインクラフト/ソウルライクな化け物を作ろうと、open code、oh my opencode、supermemoryで実験中です。昼食後の散歩に行っている間に、しゃがむアニメーションを追加するように指示しておきました。[動画]」 - [MagiMetal](https://x.com/MagiMetal/status/2005374704178373023)

> 「これをコアに取り込んで彼を採用すべきだ。マジで。これ、本当に、本当に、本当に良い。」 <br/>- Henning Kilset

> 「彼を説得できるなら @yeon_gyu_kim を雇ってください。彼がopencodeに革命を起こしました。」 <br/>- [mysticaltech](https://x.com/mysticaltech/status/2001858758608376079)

> 「Oh My OpenCodeはマジでヤバい」 - [YouTube - Darren Builds AI](https://www.youtube.com/watch?v=G_Snfh2M41M)

---

# Oh My OpenCode

最初はこれを「Claude Codeにステロイドを打ったもの」と呼んでいました。それは過小評価でした。

一つのモデルに薬を盛るのではありません。カルテルを動かすんです。Claude、GPT、Kimi、Gemini——それぞれが得意なことを、並列で、止まらずに。モデルは毎月安くなっており、どのプロバイダーも独占できません。私たちはすでにその世界に生きています。

その泥臭い作業をすべてやっておきました。すべてをテストし、実際に機能するものだけを残しました。

OmOをインストールして、`ultrawork`とタイプしてください。狂ったようにコーディングしてください。


## インストール

### 人間向け

以下のプロンプトをコピーして、あなたのLLMエージェント（Claude Code、AmpCode、Cursorなど）に貼り付けてください：

```
Install and configure oh-my-opencode by following the instructions here:
https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

もしくは[インストールガイド](docs/guide/installation.md)を直接読んでもいいですが、マジでエージェントにやらせてください。人間は設定で必ずタイポします。

### LLMエージェント向け

インストールガイドを取得して、それに従ってください：

```bash
curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

---

## このREADMEをスキップする

ドキュメントを読む時代は終わりました。このテキストをエージェントに貼り付けるだけです：

```
Read this and tell me why it's not just another boilerplate: https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/README.md
```

## ハイライト

### 🪄 `ultrawork`

本当にこれを全部読んでるんですか？信じられない。

インストールして、`ultrawork`（または `ulw`）とタイプする。完了です。

以下の内容、すべての機能、すべての最適化、何も知る必要はありません。ただ勝手に動きます。

以下のサブスクリプションだけでも、ultraworkは十分に機能します（このプロジェクトとは無関係であり、個人的な推奨にすぎません）：
- [ChatGPT サブスクリプション ($20)](https://chatgpt.com/)
- [Kimi Code サブスクリプション ($0.99) (*今月限定)](https://www.kimi.com/membership/pricing?track_id=5cdeca93-66f0-4d35-aabb-b6df8fcea328)
- [GLM Coding プラン ($10)](https://z.ai/subscribe)
- 従量課金（pay-per-token）の対象であれば、kimiやgeminiモデルを使っても費用はほとんどかかりません。

|       | 機能                                                     | 何をするのか                                                                                                                                                                                                                   |
| :---: | :------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   🤖   | **規律あるエージェント (Discipline Agents)**             | Sisyphusが Hephaestus、Oracle、Librarian、Exploreをオーケストレーションします。完全なAI開発チームが並列で動きます。                                                                                                            |
|   ⚡   | **`ultrawork` / `ulw`**                                  | 一言でOK。すべてのエージェントがアクティブになり、終わるまで止まりません。                                                                                                                                                     |
|   🚪   | **[IntentGate](https://factory.ai/news/terminal-bench)** | ユーザーの真の意図を分析してから分類・行動します。もう文字通りに誤解して的外れなことをすることはありません。                                                                                                                   |
|   🔗   | **ハッシュベースの編集ツール**                           | `LINE#ID` のコンテンツハッシュですべての変更を検証します。stale-lineエラー0%。[oh-my-pi](https://github.com/can1357/oh-my-pi)にインスパイアされています。[ハーネス問題 →](https://blog.can.ac/2026/02/12/the-harness-problem/) |
|   🛠️   | **LSP + AST-Grep**                                       | ワークスペース単位のリネーム、ビルド前の診断、ASTを考慮した書き換え。エージェントにIDEレベルの精度を提供します。                                                                                                               |
|   🧠   | **バックグラウンドエージェント**                         | 5人以上の専門家を並列で投入します。コンテキストは軽く保ち、結果は準備ができ次第受け取ります。                                                                                                                                  |
|   📚   | **組み込みMCP**                                          | Exa（Web検索）、Context7（公式ドキュメント）、Grep.app（GitHub検索）。常にオンです。                                                                                                                                           |
|   🔁   | **Ralph Loop / `/ulw-loop`**                             | 自己参照ループ。100%完了するまで絶対に止まりません。                                                                                                                                                                           |
|   ✅   | **Todoの強制執行**                                       | エージェントがサボる？システムが首根っこを掴んで戻します。あなたのタスクは必ず終わります。                                                                                                                                     |
|   💬   | **コメントチェッカー**                                   | コメントからAI臭い無駄話を排除します。シニアエンジニアが書いたようなコードになります。                                                                                                                                         |
|   🖥️   | **Tmux統合**                                             | 完全なインタラクティブターミナル。REPL、デバッガー、TUIアプリがすべてリアルタイムで動きます。                                                                                                                                  |
|   🔌   | **Claude Code互換性**                                    | 既存のフック、コマンド、スキル、MCP、プラグイン？すべてここでそのまま動きます。                                                                                                                                                |
|   🎯   | **スキル内蔵MCP**                                        | スキルが独自のMCPサーバーを持ち歩きます。コンテキストが肥大化しません。                                                                                                                                                        |
|   📋   | **Prometheusプランナー**                                 | インタビューモードで、コードを1行触る前に戦略的な計画から立てます。                                                                                                                                                            |
|   🔍   | **`/init-deep`**                                         | プロジェクト全体にわたって階層的な `AGENTS.md` ファイルを自動生成します。トークン効率とエージェントのパフォーマンスの両方を向上させます。                                                                                      |

### 規律あるエージェント (Discipline Agents)

<table><tr>
<td align="center"><img src=".github/assets/sisyphus.png" height="300" /></td>
<td align="center"><img src=".github/assets/hephaestus.png" height="300" /></td>
</tr></table>

**Sisyphus** (`claude-opus-4-6` / **`kimi-k2.5`** / **`glm-5`**) はあなたのメインのオーケストレーターです。計画を立て、専門家に委任し、攻撃的な並列実行でタスクを完了まで推進します。途中で投げ出すことはありません。

**Hephaestus** (`gpt-5.4`) はあなたの自律的なディープワーカーです。レシピではなく、目標を与えてください。手取り足取り教えなくても、コードベースを探索し、パターンを研究し、端から端まで実行します。*正当なる職人 (The Legitimate Craftsman).*

**Prometheus** (`claude-opus-4-6` / **`kimi-k2.5`** / **`glm-5`**) はあなたの戦略プランナーです。インタビューモードで動作し、コードに触れる前に質問をしてスコープを特定し、詳細な計画を構築します。

すべてのエージェントは、それぞれのモデルの強みに合わせてチューニングされています。手動でモデルを切り替える必要はありません。[詳しくはこちら →](docs/guide/overview.md)

> Anthropicが[私たちのせいでOpenCodeをブロックしました。](https://x.com/thdxr/status/2010149530486911014) だからこそHephaestusは「正当なる職人 (The Legitimate Craftsman)」と呼ばれているのです。皮肉を込めています。
>
> Opusで最もよく動きますが、Kimi K2.5 + GPT-5.4の組み合わせだけでも、バニラのClaude Codeを軽く凌駕します。設定は一切不要です。

### エージェントの��ーケストレーション

Sisyphusがサブエージェントにタスクを委任する際、モデルを直接選ぶことはありません。**カテゴリー**を選びます。カテゴリーは自動的に適切なモデルにマッピングされます：

| カテゴリー           | 用途                                 |
| :------------------- | :----------------------------------- |
| `visual-engineering` | フロントエンド、UI/UX、デザイン      |
| `deep`               | 自律的なリサーチと実行               |
| `quick`              | 単一ファイルの変更、タイポの修正     |
| `ultrabrain`         | ハードロジック、アーキテクチャの決定 |

エージェントがどのような種類の作業かを伝え、ハーネスが適切なモデルを選択します。あなたは何も触る必要はありません。

### Claude Code互換性

Claude Codeの設定を頑張りましたね。素晴らしい。

すべてのフック、コマンド、スキル、MCP、プラグインが、変更なしでここで動きます。プラグインも含めて完全互換です。

### エージェントのためのワールドクラスのツール

LSP、AST-Grep、Tmux、MCPが、ただテープで貼り付けただけでなく、本当に「統合」されています。

- **LSP**: `lsp_rename`、`lsp_goto_definition`、`lsp_find_references`、`lsp_diagnostics`。エージェントにIDEレベルの精度を提供。
- **AST-Grep**: 25言語に対応したパターン認識コード検索と書き換え。
- **Tmux**: 完全なインタラクティブターミナル。REPL、デバッガー、TUIアプリ。エージェントがセッション内で動きます。
- **MCP**: Web検索、公式ドキュメント、GitHubコード検索がすべて組み込まれています。

### スキル内蔵MCP

MCPサーバーがあなたのコンテキスト予算を食いつぶしています。私たちがそれを修正しました。

スキルが独自のMCPサーバーを持ち歩きます。必要なときだけ起動し、終われば消えます。コンテキストウィンドウがきれいに保たれます。

### ハッシュベースの編集 (Codes Better. Hash-Anchored Edits)

ハーネスの問題は深刻です。エージェントが失敗する原因の大半はモデルではなく、編集ツールにあります。

> *「どのツールも、モデルに変更したい行に対する安定して検証可能な識別子を提供していません... すべてのツールが、モデルがすでに見た内容を正確に再現することに依存しています。それができないとき——そして大抵はできないのですが——ユーザーはモデルのせいにします。」*
>
> <br/>- [Can Bölük, ハーネス問題 (The Harness Problem)](https://blog.can.ac/2026/02/12/the-harness-problem/)

[oh-my-pi](https://github.com/can1357/oh-my-pi) に触発され、**Hashline**を実装しました。エージェントが読むすべての行にコンテンツハッシュがタグ付けされて返されます：

```
11#VK| function hello() {
22#XJ|   return "world";
33#MB| }
```

エージェントはこのタグを参照して編集します。最後に読んだ後でファイルが変更されていた場合、ハッシュが一致せず、コードが壊れる前に編集が拒否されます。空白を正確に再現する必要もなく、間違った行を編集するエラー (stale-line) もありません。

Grok Code Fast 1 で、成功率が **6.7% → 68.3%** に上昇しました。編集ツールを1つ変えただけで、です。

### 深い初期化。`/init-deep`

`/init-deep` を実行してください。階層的な `AGENTS.md` ファイルを生成します：

```
project/
├── AGENTS.md              ← プロジェクト全体のコンテキスト
├── src/
│   ├── AGENTS.md          ← src 専用のコンテキスト
│   └── components/
│       └── AGENTS.md      ← コンポーネント専用のコンテキスト
```

エージェントが関連するコンテキストだけを自動で読み込みます。手動での管理はゼロです。

### プランニング。Prometheus

複雑なタスクですか？プロンプトを投げて祈るのはやめましょう。

`/start-work` で Prometheus が呼び出されます。**本物のエンジニアのようにあなたにインタビューし**、スコープと曖昧さを特定し、コードに触れる前に検証済みの計画を構築します。エージェントは作業を始める前に、自分が何を作るべきか正確に理解します。

### スキル (Skills)

スキルは単なるプロンプトではありません。それぞれ以下をもたらします：

- ドメインに最適化されたシステム命令
- 必要なときに起動する組み込みMCPサーバー
- スコープ制限された権限（エージェントが境界を越えないようにする）

組み込み：`playwright`（ブラウザ自動化）、`git-master`（アトミックなコミット、リベース手術）、`frontend-ui-ux`（デザイン重視のUI）。

独自に追加するには：`.opencode/skills/*/SKILL.md` または `~/.config/opencode/skills/*/SKILL.md`。

**全機能を知りたいですか？** エージェント、フック、ツール、MCPなどの詳細は **[機能ドキュメント (Features)](docs/reference/features.md)** をご覧ください。

---

> **背景のストーリーを知りたいですか？** なぜSisyphusは岩を転がすのか、なぜHephaestusは「正当なる職人」なのか、そして[オーケストレーションガイド](docs/guide/orchestration.md)をお読みください。
>
> oh-my-opencodeは初めてですか？どのモデルを使うべきかについては、**[
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
