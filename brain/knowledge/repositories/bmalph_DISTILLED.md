---
id: repo-fetched-bmalph-070543
type: knowledge
owner: OA
registered_at: 2026-04-05T03:59:05.730575
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bmalph_070543

## Assimilation Report
Auto-cloned repository: FETCHED_bmalph_070543

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# bmalph

[![npm](https://img.shields.io/npm/v/bmalph)](https://www.npmjs.com/package/bmalph)
[![npm downloads](https://img.shields.io/npm/dm/bmalph)](https://www.npmjs.com/package/bmalph)
[![license](https://img.shields.io/npm/l/bmalph)](LICENSE)
[![node](https://img.shields.io/node/v/bmalph)](https://nodejs.org)
[![CI](https://github.com/LarsCowe/bmalph/actions/workflows/ci.yml/badge.svg)](https://github.com/LarsCowe/bmalph/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/LarsCowe/bmalph/branch/main/graph/badge.svg)](https://codecov.io/gh/LarsCowe/bmalph)

[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) planning + [Ralph](https://github.com/snarktank/ralph) autonomous implementation, wired through platform-specific instructions, skills, and command indexes.

<p align="center">
  <img src="docs/bmalph-diagram.png" alt="bmalph workflow diagram" width="800" />
</p>

## What is bmalph?

bmalph bundles and installs two AI development systems:

- **[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** — Planning agents and workflows (Phases 1-3)
- **[Ralph](https://github.com/snarktank/ralph)** — Autonomous implementation loop (Phase 4)

bmalph provides:

- `bmalph init` — Install both systems
- `bmalph upgrade` — Update to latest versions
- `bmalph doctor` — Check installation health
- `bmalph implement` — Transition from BMAD to Ralph
- `bmalph run` — Start Ralph loop with live dashboard
- `bmalph check-updates` — Check for upstream updates
- `bmalph status` — Show project status and phase
- `bmalph reset` — Remove all bmalph files
- ~~`bmalph watch`~~ — _(deprecated)_ Use `bmalph run` instead

## Supported Platforms

bmalph works with multiple AI coding assistants. Each platform gets BMAD planning (Phases 1-3). The Ralph autonomous loop (Phase 4) requires a CLI-based platform.

| Platform       | ID            | Tier                | Instructions File                 | Commands                              |
| -------------- | ------------- | ------------------- | --------------------------------- | ------------------------------------- |
| Claude Code    | `claude-code` | full                | `CLAUDE.md`                       | `.claude/commands/` directory         |
| OpenAI Codex   | `codex`       | full                | `AGENTS.md`                       | Codex Skills (`.agents/skills/`)      |
| OpenCode       | `opencode`    | full                | `AGENTS.md`                       | OpenCode Skills (`.opencode/skills/`) |
| Cursor         | `cursor`      | full (experimental) | `.cursor/rules/bmad.mdc`          | `_bmad/COMMANDS.md`                   |
| Windsurf       | `windsurf`    | instructions-only   | `.windsurf/rules/bmad.md`         | `_bmad/COMMANDS.md`                   |
| GitHub Copilot | `copilot`     | full (experimental) | `.github/copilot-instructions.md` | `_bmad/COMMANDS.md`                   |
| Aider          | `aider`       | instructions-only   | `CONVENTIONS.md`                  | `_bmad/COMMANDS.md`                   |

**Tiers:**

- **full** — Phases 1-4. BMAD planning + Ralph autonomous implementation loop.
- **instructions-only** — Phases 1-3. BMAD planning only. Ralph is not available.

## Prerequisites

- Node.js 20+
- Bash (WSL or Git Bash on Windows)
- A supported AI coding platform (see table above)
- For Ralph loop (Phase 4): Claude Code (`claude`), Codex CLI (`codex`), OpenCode (`opencode`), Copilot CLI (`copilot`), or Cursor CLI (`cursor-agent`; older `agent` installs are also supported)

## Installation

```bash
npm install -g bmalph
```

## Quick Start

```bash
cd my-project
bmalph init --name my-project

# To target a specific platform, add --platform (e.g. codex, cursor, windsurf)
# Without --platform, bmalph auto-detects strong project markers and
# prompts interactively when detection is ambiguous or missing
```

## Workflow

### Step 1: Initialize

```bash
cd my-project
bmalph init
```

**Platform resolution:** `--platform` flag > auto-detect from project markers > interactive prompt > default `claude-code`

Strong markers such as `.cursor/`, `.claude/`, `.opencode/`, `.windsurf/`, `.github/copilot-instructions.md`, and `.aider.conf.yml` are auto-detected directly. Root-only `AGENTS.md` and `CLAUDE.md` are treated as weak hints and may still trigger the interactive platform prompt.

This installs:

- `_bmad/` — BMAD agents and workflows
- `.ralph/` — Ralph loop, libs, templates (drivers for claude-code, codex, opencode, copilot, and cursor)
- `bmalph/` — State management (config.json, stores selected platform)
- Updates the platform's instructions file with BMAD workflow instructions (e.g. `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/bmad.mdc`)
- Delivers BMAD commands using the platform's native mechanism (Claude Code: `.claude/commands/`; Codex: `.agents/skills/`; OpenCode: `.opencode/skills/`; Cursor, Windsurf, Copilot, and Aider: `_bmad/COMMANDS.md`)

### Migrating from standalone BMAD

If you already have BMAD installed (a `_bmad/` directory), `bmalph init` works as a migration path:

- `_bmad/` (framework files) will be replaced with the bmalph-managed version
- `_bmad-output/` (your planning artifacts: PRDs, architecture, stories) is not touched
- If you've customized framework files inside `_bmad/`, commit first so you can review changes with `git diff`

### Step 2: Plan with BMAD (Phases 1-3)

Work interactively with BMAD agents in your AI coding assistant.

- **Claude Code** — use `/bmalph` to see your current phase and available commands.
- **OpenAI Codex** — use Codex Skills such as `$analyst` and `$create-prd`.
- **Cursor** — Read `_bmad/COMMANDS.md` and ask Cursor to run the BMAD master agent.
- **Windsurf, Copilot, Aider** — use `_bmad/COMMANDS.md` as the command reference and ask the assistant to follow the named BMAD workflow.

| Phase         | Agent            | Commands           |
| ------------- | ---------------- | ------------------ |
| 1 Analysis    | Analyst          | BP, MR, DR, TR, CB |
| 2 Planning    | PM / UX Designer | CP, VP, EP, CU     |
| 3 Solutioning | Architect / PM   | CA, CE, IR         |

Validation commands (`validate-brief`, `validate-prd`, `validate-ux`, `validate-architecture`, `validate-epics-stories`) run the same workflow in Validate mode. In Claude Code, invoke them as slash commands; on other platforms use the equivalent entry from `_bmad/COMMANDS.md` or Codex Skills.

**Phase 1 — Analysis**

- `BP` Brainstorm Project — guided facilitation through brainstorming techniques
- `MR` Market Research — market analysis, competitive landscape, customer needs
- `DR` Domain Research — industry domain deep dive
- `TR` Technical Research — technical feasibility, architecture options
- `CB` Create Brief — guided experience to nail down your product idea

**Phase 2 — Planning**

- `CP` Create PRD — expert led facilitation to produce your PRD (required)
- `VP` Validate PRD — validate PRD is comprehensive and cohesive
- `EP` Edit PRD — improve and enhance an existing PRD
- `CU` Create UX — guidance through realizing the plan for your UX

**Phase 3 — Solutioning**

- `CA` Create Architecture — guided workflow to document technical decisions (required)
- `CE` Create Epics and Stories — create the epics and stories listing (required)
- `IR` Implementation Readiness — ensure PRD, UX, architecture, and stories are aligned (required)

**Anytime Commands**

Available in any phase for supporting tasks:

- `QS` Quick Spec — lightweight spec for small tasks without full planning
- `QD` Quick Dev — quick implementation for small tasks
- `DP` Document Project — analyze existing project to produce documentation
- `GPC` Generate Project Context — scan codebase to generate LLM-optimized context
- `CC` Correct Course — navigate significant changes mid-project
- `WD` Write Document — tech writer agent for documentation
- `MG` Mermaid Generate — create Mermaid diagrams
- `VD` Validate Document — review documents against standards
- `BSP` Brainstorming — interactive idea generation techniques (core, distinct from BP)
- `ID` Index Docs — create lightweight doc index for LLM scanning
- `SD` Shard Document — split large documents into smaller files
- `ES` Editorial Review (Structure) — propose document reorganization
- `AR` Adversarial Review — critical content review for QA
- `US` Update Standards — update tech-writer documentation standards
- `EC` Explain Concept — create technical explanations with examples
- `_bmad/COMMANDS.md` — generated command reference for platforms without native slash commands

> **Note:** `EP` means Edit PRD in the bmm workflow (Phase 2) and Editorial Review — Prose in the core module. `PM` is Party Mode in core. The bmm meanings are the primary workflow codes.

### Step 3: Implement with Ralph (Phase 4)

> **Note:** Ralph is only available on **full** tier platforms (Claude Code, OpenAI Codex, OpenCode, GitHub Copilot, Cursor). Instructions-only platforms (Windsurf, Aider) support Phases 1-3 only. GitHub Copilot and Cursor support is experimental.

Run `bmalph implement` from the terminal, or use the `/bmalph-implement` slash command in Claude Code.

This transitions your BMAD artifacts into Ralph's format:

1. Reads your stories from BMAD output
2. Generates `.ralph/@fix_plan.md` with ordered tasks
3. Copies specs to `.ralph/specs/` with changelog tracking
4. Instructs you to start the Ralph autonomous loop

Then start Ralph:

```bash
bmalph run
```

> **Advanced:** Ralph loads the platform drivers internally. Start the loop with `bmalph run`, or run `bash .ralph/ralph_loop.sh` directly if you need to bypass the CLI.

Ralph picks stories one by one, implements with TDD, and commits. The loop stops when all stories are done or the circuit breaker triggers.

### Incremental Development

bmalph supports iterative development cycles:

```
BMAD (Epic 1) → bmalph implement → Ralph works on Epic 1
     ↓
BMAD (add Epic 2) → bmalph implement → Ralph sees changes + picks up Epic 2
```

**Smart Merge**: When you run `bmalph implement` again after Ralph has made progress:

- Completed stories (`[x]`) are preserved in the new fix_plan
- New stories from BMAD are added as pending (`[ ]`)

**Specs Changelog**: `.ralph/SPECS_CHANGELOG.md` shows what changed in specs since the last run, so Ralph knows what's new or modified.

## CLI Reference

| Command                | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `bmalph init`          | Install BMAD + Ralph into project                   |
| `bmalph upgrade`       | Update bundled assets to current version            |
| `bmalph doctor`        | Check installation health                           |
| `bmalph check-updates` | Check if bundled BMAD/Ralph versions are up to date |
| `bmalph status`        | Show current project status and phase               |
| `bmalph implement`     | Transition BMAD planning artifacts to Ralph format  |
| `bmalph run`           | Start Ralph loop with live dashboard                |
| `bmalph reset`         | Remove all bmalph files from the project            |
| `bmalph watch`         | _(deprecated)_ Use `bmalph run` instead             |

### Global options

| Flag                       | Description                   |
| -------------------------- | ----------------------------- |
| `--verbose`                | Enable debug logging          |
| `--no-color`               | Disable colored output        |
| `--quiet`                  | Suppress non-essential output |
| `-C, --project-dir <path>` | Run in specified directory    |
| `--version`                | Show version                  |
| `--help`                   | Show help                     |

### init options

| Flag                       | Description                                                                                    | Default        |
| -------------------------- | ---------------------------------------------------------------------------------------------- | -------------- |
| `-n, --name <name>`        | Project name                                                                                   | directory name |
| `-d, --description <desc>` | Project description                                                                            | (prompted)     |
| `--platform <id>`          | Target platform (`claude-code`, `codex`, `opencode`, `cursor`, `windsurf`, `copilot`, `aider`) | auto-detect    |
| `--dry-run`                | Preview changes without writing files                                                          |                |

### implement options

| Flag      | Description                           |
| --------- | ------------------------------------- |
| `--force` | Override pre-flight validation errors |

### check-updates options

| Flag     | Description    |
| -------- | -------------- |
| `--json` | Output as JSON |

### doctor options

| Flag     | Description    |
| -------- | -------------- |
| `--json` | Output as JSON |

### status options

| Flag     | Description    |
| -------- | -------------- |
| `--json` | Output as JSON |

### upgrade options

| Flag        | Description               |
| ----------- | ------------------------- |
| `--force`   | Skip confirmation prompts |
| `--dry-run` | Preview changes           |

### reset options

| Flag        | Description              |
| ----------- | ------------------------ |
| `--dry-run` | Preview changes          |
| `--force`   | Skip confirmation prompt |

### run options

| Flag                  | Description                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------- |
| `--driver <platform>` | Override platform driver (claude-code, codex, opencode, copilot, cursor)                 |
| `--review [mode]`     | Quality review: `enhanced` (every 5 loops) or `ultimate` (every story). Claude Code only |
| `--interval <ms>`     | Dashboard refresh interval in milliseconds (default: 2000)                               |
| `--no-dashboard`      | Run Ralph without the dashboard overlay                                                  |

### watch options

> **Deprecated:** Use `bmalph run` instead. The `watch` command will be removed in a future release.

| Flag              | Description                                      |
| ----------------- | ------------------------------------------------ |
| `--interval <ms>` | Refresh interval in milliseconds (default: 2000) |

## Command Delivery

bmalph bundles 54 BMAD and bmalph command definitions. Delivery varies by platform:

- **Claude Code** — installed as files in `.claude/commands/` (invoke with `/command-name`)
- **OpenAI Codex** — delivered as Codex Skills in `.agents/skills/` (invoke with `$command-name`)
- **OpenCode** — delivered as OpenCode Skills in `.opencode/skills/`
- **Cur
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.11.0](https://github.com/LarsCowe/bmalph/compare/v2.10.0...v2.11.0) (2026-03-24)


### Features

* **ralph:** capture stderr and log exit reason on driver crash/timeout ([#145](https://github.com/LarsCowe/bmalph/issues/145)) ([75ffebb](https://github.com/LarsCowe/bmalph/commit/75ffebbda345b30207849a2f0fbe2e0179856766))
* **run:** inject git diff summary into inter-loop context ([#117](https://github.com/LarsCowe/bmalph/issues/117)) ([4c0c4f4](https://github.com/LarsCowe/bmalph/commit/4c0c4f48f8405253db8eb3650ce8ea18bd2cc959))
* **run:** inject next unchecked task into loop context ([#118](https://github.com/LarsCowe/bmalph/issues/118)) ([fb93dca](https://github.com/LarsCowe/bmalph/commit/fb93dca6ce5dda66640b4205347e84b98664a896))


### Bug Fixes

* **prompt:** restructure PROMPT.md to code-first, read-on-demand ([#147](https://github.com/LarsCowe/bmalph/issues/147)) ([77bb7f3](https://github.com/LarsCowe/bmalph/commit/77bb7f31ce4322c4b5ba2b23d19d4a39d4ea2502))
* **ralph:** detect and warn when no git repository is initialized ([#144](https://github.com/LarsCowe/bmalph/issues/144)) ([4674441](https://github.com/LarsCowe/bmalph/commit/4674441133fdfa95ef521633bac3d86cd09e95f4))
* **run:** separate format confidence from completion confidence ([#124](https://github.com/LarsCowe/bmalph/issues/124)) ([2f8d71a](https://github.com/LarsCowe/bmalph/commit/2f8d71aefa5f259c87fa9ebac29fe5645b315be0))
* **transition:** match numbered section headers in preflight checks ([b78e1a8](https://github.com/LarsCowe/bmalph/commit/b78e1a85060a37d4c2aaddf707bb2269d6271626))


### Performance

* **tests:** add parallel BATS execution with --jobs ([64b306c](https://github.com/LarsCowe/bmalph/commit/64b306c5045513f9d92f393f2896a1d9200869a3))
* **tests:** optimize BATS with setup_file and parallel execution ([49d041f](https://github.com/LarsCowe/bmalph/commit/49d041f697139a2ddd9d317f3d83d0a94f84bb00))

## [2.10.0](https://github.com/LarsCowe/bmalph/compare/v2.9.0...v2.10.0) (2026-03-23)


### Features

* **run:** add ultimate review mode for per-story code review ([33af4b9](https://github.com/LarsCowe/bmalph/commit/33af4b9e6ee63a3ea03d4dedfafd9022c5e29922))
* **run:** prioritize HIGH/CRITICAL review findings over new stories ([e0ce427](https://github.com/LarsCowe/bmalph/commit/e0ce42791b2a89f6369ebcf3c3ac69c60fb7722b))


### Bug Fixes

* **bash:** Codex driver resume and ralph_loop.sh default path fixes ([#137](https://github.com/LarsCowe/bmalph/issues/137)) ([de8639f](https://github.com/LarsCowe/bmalph/commit/de8639f81b0118f1d0d177f7d9a4cfcd6a052afa))
* **run:** enforce word boundaries in completion keyword matching ([8887a0f](https://github.com/LarsCowe/bmalph/commit/8887a0f36eded9e9ee19719dc449c10fdef917c5)), closes [#122](https://github.com/LarsCowe/bmalph/issues/122)
* **run:** restore --no-review CLI flag and harden bash delta parsing ([e20e301](https://github.com/LarsCowe/bmalph/commit/e20e3015efd431c01ef838b71421577993247883))
* **run:** trust RALPH_STATUS block over heuristic analysis ([#140](https://github.com/LarsCowe/bmalph/issues/140)) ([0838617](https://github.com/LarsCowe/bmalph/commit/0838617bdbde02f35d9f006e6e09a09e05186b62)), closes [#123](https://github.com/LarsCowe/bmalph/issues/123)

## [2.9.0](https://github.com/LarsCowe/bmalph/compare/v2.8.0...v2.9.0) (2026-03-19)


### Features

* **run:** add periodic code review loop for Ralph ([#102](https://github.com/LarsCowe/bmalph/issues/102)) ([4bab0ef](https://github.com/LarsCowe/bmalph/commit/4bab0ef94436f40f482750e113af155a15fd92d2))


### Bug Fixes

* use strict equality in renderer hasAnyData check ([6660539](https://github.com/LarsCowe/bmalph/commit/6660539c2f9c1976b1fa60ace2a5dcc90ffe8af0))


### Code Quality

* strengthen type safety and deduplicate constants ([1f154a0](https://github.com/LarsCowe/bmalph/commit/1f154a09f5f64acd234da5f30fac7f456c4ec629))

## [2.8.0](https://github.com/LarsCowe/bmalph/compare/v2.7.7...v2.8.0) (2026-03-17)


### Features

* add OpenCode platform support and harden quality gates ([738de2b](https://github.com/LarsCowe/bmalph/commit/738de2b6438d66c38587bde6727a562085946e26))
* upgrade bundled BMAD to v6.1.0 ([53fcd96](https://github.com/LarsCowe/bmalph/commit/53fcd963ab8c62a4a6524f67a097977f4e772218))
* upgrade bundled BMAD to v6.2.0 ([508250e](https://github.com/LarsCowe/bmalph/commit/508250eb6e6adef6a7c5c4112f2ba602c424063b))


### Bug Fixes

* render a single footer in run dashboard ([5cd1aea](https://github.com/LarsCowe/bmalph/commit/5cd1aea6280bd9dd068137979c32e10764a5dfa9))
* replace Bash 4+ syntax for macOS 3.2 compatibility ([#110](https://github.com/LarsCowe/bmalph/issues/110)) ([1029d48](https://github.com/LarsCowe/bmalph/commit/1029d48758ba0397226b185d019cf0b75c06132f))
* stabilize doctor sequential test on Windows CI ([204f813](https://github.com/LarsCowe/bmalph/commit/204f81327b1aa1fe84900df2c047c03ad548d18b))


### Code Quality

* harden detectBashVersion and add missing test ([e4d49e8](https://github.com/LarsCowe/bmalph/commit/e4d49e8cf92c5441d1c880672757a7e7b3ce6f1f))

## [2.7.7](https://github.com/LarsCowe/bmalph/compare/v2.7.6...v2.7.7) (2026-03-15)


### Bug Fixes

* enforce fix-plan progress tracking ([941aabb](https://github.com/LarsCowe/bmalph/commit/941aabb9e046373884f3831174d635b6f688d48a))
* harden autonomous Claude loop defaults ([5f56e02](https://github.com/LarsCowe/bmalph/commit/5f56e02b3603474060cfcddd184dc74de68f78c8))
* harden Ralph terminal dashboard ([8204435](https://github.com/LarsCowe/bmalph/commit/8204435e03018cf3bb33d0fd44bf9e8503301174))

## [2.7.6](https://github.com/LarsCowe/bmalph/compare/v2.7.5...v2.7.6) (2026-03-14)


### Bug Fixes

* display execution progress in monitor dashboard (closes [#101](https://github.com/LarsCowe/bmalph/issues/101)) ([#103](https://github.com/LarsCowe/bmalph/issues/103)) ([0751b06](https://github.com/LarsCowe/bmalph/commit/0751b06021274b05db2e726a20eb7819fea347b5))
* handle permission denials in current loop ([8b1d967](https://github.com/LarsCowe/bmalph/commit/8b1d96710a5dfe3350f15123f78aec04a147d443))
* harden Ralph runtime state parsing ([16f53f4](https://github.com/LarsCowe/bmalph/commit/16f53f4a454bf8c9d21a38288e02c2db729d408f))
* harden Ralph session state recovery ([5a77d86](https://github.com/LarsCowe/bmalph/commit/5a77d861ea0e6e058853af3fdf507affe338b6ed))
* stabilize Claude permission mode for unattended loops ([e64d010](https://github.com/LarsCowe/bmalph/commit/e64d01077e2249242a4e39d1c63437485609d6e8))


### Code Quality

* split installer into smaller modules ([2f5e3b1](https://github.com/LarsCowe/bmalph/commit/2f5e3b18bef2624e1a921570dbf980e237cbc748))
* split transition orchestration pipeline ([989dc50](https://github.com/LarsCowe/bmalph/commit/989dc50f613e6ffc5a3307c37611d89f1f1d6fc6))

## [2.7.5](https://github.com/LarsCowe/bmalph/compare/v2.7.4...v2.7.5) (2026-03-09)


### Bug Fixes

* harden Cursor runtime contract and docs ([ac1404a](https://github.com/LarsCowe/bmalph/commit/ac1404aa211b435783e799d18008d2a62fa13d8f))
* **installer:** restore _bmad after post-swap failures ([e3f6354](https://github.com/LarsCowe/bmalph/commit/e3f635461c1d9afdf74184afcb6c648a7dcfa269)), closes [#83](https://github.com/LarsCowe/bmalph/issues/83)
* kill Ralph process tree on Windows ([c9f2327](https://github.com/LarsCowe/bmalph/commit/c9f2327414f82bc9289090b93c1c2cfc50096bd8))
* stabilize ci test runners ([28d9195](https://github.com/LarsCowe/bmalph/commit/28d91950f3b79f1c81fe27e7e438edf8d4bc76b3))

## [2.7.4](https://github.com/LarsCowe/bmalph/compare/v2.7.3...v2.7.4) (2026-03-09)


### Bug Fixes

* handle malformed story IDs deterministically ([c7beddb](https://github.com/LarsCowe/bmalph/commit/c7beddb6db5ccd96804704eb477d79264663051e))
* parse Codex JSONL responses in Ralph loop ([#89](https://github.com/LarsCowe/bmalph/issues/89)) ([90677d0](https://github.com/LarsCowe/bmalph/commit/90677d060883f7efefd8f427e7250046f1e8e908))
* preserve specs on transition swap failure ([208c2eb](https://github.com/LarsCowe/bmalph/commit/208c2eb1b4cd86c0a1d35a3274d2acbbf3120bb5)), closes [#85](https://github.com/LarsCowe/bmalph/issues/85)

## [2.7.3](https://github.com/LarsCowe/bmalph/compare/v2.7.2...v2.7.3) (2026-03-07)


### Bug Fixes

* harden BMAD transition artifact handling ([dbf298a](https://github.com/LarsCowe/bmalph/commit/dbf298aa979315001a037ca8e1cc91552a1eaaf0))
* resolve Windows Cursor driver compatibility ([62d0906](https://github.com/LarsCowe/bmalph/commit/62d0906fb1e0b40ef6a5ee19522a1a15be092548)), closes [#72](https://github.com/LarsCowe/bmalph/issues/72)

## [2.7.2](https://github.com/LarsCowe/bmalph/compare/v2.7.1...v2.7.2) (2026-03-05)


### Bug Fixes

* support BMAD-native transition artifacts ([450e7f3](https://github.com/LarsCowe/bmalph/commit/450e7f32a73c09730ca3539dbed394b2693318ea))

## [2.7.1](https://github.com/LarsCowe/bmalph/compare/v2.7.0...v2.7.1) (2026-03-04)


### Bug Fixes

* **doctor:** return non-zero exit for failed checks in json mode ([53801bd](https://github.com/LarsCowe/bmalph/commit/53801bd136953ea5c5630b44817640f054673dd1))
* **run:** propagate Ralph exit code ([176350d](https://github.com/LarsCowe/bmalph/commit/176350d141eda413d1948ab38ff0e7b438282794))
* **run:** use bash-safe relative ralph loop spawn path ([abc0627](https://github.com/LarsCowe/bmalph/commit/abc0627f80de6738cb34113fd7c813bc76d0cf79))

## [2.7.0](https://github.com/LarsCowe/bmalph/compare/v2.6.0...v2.7.0) (2026-03-04)


### Features

* add Codex skills delivery, promote Cursor to full tier, and add lite PRD workflow ([36c5c72](https://github.com/LarsCowe/bmalph/commit/36c5c726ae887ff144e6fe464264904c7b1bb578))
* promote Cursor to full tier with experimental flag ([1b3a9e6](https://github.com/LarsCowe/bmalph/commit/1b3a9e69f6c55c5f06e074bc8eb828c1a6490177))


### Bug Fixes

* harden error handling, eliminate injection surfaces, and reduce duplication ([d5e169b](https://github.com/LarsCowe/bmalph/commit/d5e169bb7bcc24a0a01f5eb82ebcd873d0d3e0bf))
* harden process lifecycle, tighten artifact matching, and fill test gaps ([ebf75ac](https://github.com/LarsCowe/bmalph/commit/ebf75ac2afe128eca70324b0bcadfaae71435c83))


### Code Quality

* eliminate duplication, normalize patterns, and expand test coverage ([238a1d8](https://github.com/LarsCowe/bmalph/commit/238a1d8c9f2f97f5dfb8b21e049a345d7aacbf84))

## [2.6.0](https://github.com/LarsCowe/bmalph/compare/v2.5.0...v2.6.0) (2026-02-28)


### Features

* add bmalph run command to start Ralph loop with dashboard ([70bf737](https://github.com/LarsCowe/bmalph/commit/70bf737c791582cef2d8caebf15ba8abe21b1e3d))
* deprecate bmalph watch in favor of bmalph run ([4da6764](https://github.com/LarsCowe/bmalph/commit/4da676466b5cac915d649f07dbf8870c99cd5bf7))
* promote Copilot to full tier with experimental flag ([a776dc3](https://github.com/LarsCowe/bmalph/commit/a776dc38d0fd2e1d3a032aaa9efd60dfc1083665))


### Code Quality

* simplify codebase and extract shared platform logic ([233f4be](https://github.com/LarsCowe/bmalph/commit/233f4be6924e47fa79c7225b3e39041c8897bb73))

## [2.5.0](https://github.com/LarsCowe/bmalph/compare/v2.4.0...v2.5.0) (2026-02-27)


### Features

* **ralph:** add /bmalph-watch slash command ([902376f](https://github.com/LarsCowe/bmalph/commit/902376ff692b54caa2846984499507fb82a7f022))
* **watch:** add live dashboard for Ralph loop monitoring ([be9ec34](https://github.com/LarsCowe/bmalph/commit/be9ec344a11a34ed8112b64909f6e42ffd410a1d))


### Bug Fixes

* **ralph:** deduplicate PRD task extraction in task_sources ([add09fc](https://github.com/LarsCowe/bmalph/commit/add09fcfcbc7fe3e94ad48e4c244329a7f715c23))
* **ralph:** detect completion mismatch and deprecate legacy scripts ([1711aab](https://github.com/LarsCowe/bmalph/commit/1711aabd2daab4616dfcc28b9694435b49fb2b6b))
* **ralph:** prevent set -e leak and CWD pollution in ralph_loop tests ([2d0b98d](https://github.com/LarsCowe/bmalph/commit/2d0b98d166fc6684f8f02a2dfd4d3504a41434cb))
* **ralph:** resolve 3 known bugs in wizard_utils, enable_core, task_sources ([a311aaa](https://github.com/LarsCowe/bmalph/commit/a311aaa461f9dc365bec10d4e6e9a0ce355dc739))
* **ralph:** use jq for JSON generation to prevent injection from special characters ([1270f14](https://github.com/LarsCowe/bmalph/commit/1270f1415fe4079ff297a66d07c3d1f3fd3aa63b))
* **tests:** increase previewUpgrade timeout for Windows CI ([cdcd647](https://github.com/LarsCowe/bmalph/commit/cdcd6471a2512e0b5fb72fe1e4998a0604b5642b))
* **watch:** rename completionMismatch to ralphCompleted, fix status tests ([e679c9f](https://github.com/LarsCowe/bmalph/commit/e679c9f3b7d2d7c9223c6c4593f01fef851ae040))


### Code Quality

* remove deprecated exports and update docs ([ee817d4](https://github.com/LarsCowe/bmalph/commit/ee817d4c71bfc50ec7f2190e39423c6153581c8e))

## [2.4.0](https://github.com/LarsCowe/bmalph/compare/v2.3.0...v2.4.0) (2026-02-23)


### Features

* add bmalph implement CLI command with pre-flight validation ([9932717](https://github.com/LarsCowe/bmalph/commit/99327171e53afd2d0394611835e1d9c19ee1dfb6))
* add slash commands and remove /bmalph-reset reference ([a30d484](https://github.com/LarsCowe/bmalph/commit/a30d484a26f8c29335ac6af97d7a01dc71fe8d4c))
* **doctor:** add jq availability check ([19824dc](https://github.com/LarsCowe/bmalph/commit/19824dc8d80577bc315b75982ee6943b23e8aa39))
* **implement:** add re-run protection and file generation summary ([e53d0d4](https://github.com/LarsCowe/bmalph/commit/e53d0d4597b910014da5631a81f106f2c557f66a))
* **reset:** add bmalph reset command ([3231b6a](https://github.com/LarsCowe/bmalph/commit/3231b6add12135ebde5226cd172c19e2020e85a7))
* **status:** detect phase from BMAD artifacts during phases 1-3 ([67593c4](https://github.com/LarsCowe/bmalph/commit/67593c4dadfcece0b8606fce89c6f5e011e52971))
* **transition:** improve artifact detection and progress preservation ([02709cc](https://github.com/LarsCowe/bmalph/commit/02709ccf37c502fd1af5bf431a2582e563a24696))
* **validate:** read task counts from Ralph status data ([329e8b5](https://github.com/LarsCowe/bmalph/commit/329e8b5f0e86c5b1d404b909cc9c899ac9e32c7a))

## [2.3.0](https://github.com/LarsCowe/bmalph/compare/v2.2.1...v2.3.0) (2026-02-21)


### Features

* add multi-platform support for six AI coding assistants ([#54](https://github.com/LarsCowe/bmalph/issues/54)) ([864316e](https://github.com/LarsCowe/bmalph/commit/864316ed91aa329110bc0859e886b1cbd25f99e1))
* **init:** detect existing BMAD installation during init ([42d0047](https://github.com/LarsCowe/bmalph/commit/42d0047573f69484c84eff09fd0098a53332cec6)), closes [#52](https://github.com/LarsCowe/bmalph/issues/52)


### Bug Fixes

* prevent data loss in atomic _bmad copy with rename-aside pattern ([b728a58](https:
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# bmalph

Integration layer between [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) and [Ralph](https://github.com/snarktank/ralph).

## What is bmalph?

bmalph bundles and installs two AI development systems:

- **[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** — Planning agents and workflows (Phases 1-3)
- **[Ralph](https://github.com/snarktank/ralph)** — Autonomous implementation loop (Phase 4)

## Architecture

```
Phases 1-3 (Planning): BMAD agents + workflows (interactive, command-driven)
Phase 4 (Implementation): Ralph loop (autonomous, bash-driven)
bmalph: CLI + transition logic
```

### Directory structure after `bmalph init`

```
project-root/
├── _bmad/              # BMAD agents, workflows, core, lite workflows
├── .ralph/             # Ralph runtime (loop, libs, specs, logs, drivers)
│   ├── drivers/        # Platform driver scripts (claude-code, codex, opencode, copilot, cursor)
│   ├── lib/            # Shell libraries (circuit breaker, response analysis, etc.)
│   └── templates/      # Prompt, agent, fix plan, review, and ralphrc templates
├── bmalph/             # bmalph state (config.json with platform, state/)
└── <instructions file> # Varies by platform (CLAUDE.md, AGENTS.md, etc.)
```

The instructions file depends on the configured platform — see `src/platform/` for the mapping.

## CLI Commands

| Command                | Action                                    |
| ---------------------- | ----------------------------------------- |
| `bmalph init`          | Install BMAD + Ralph, configure project   |
| `bmalph upgrade`       | Update bundled assets to current version  |
| `bmalph doctor`        | Check installation health                 |
| `bmalph check-updates` | Check for upstream updates                |
| `bmalph status`        | Show project installation status          |
| `bmalph implement`     | Transition BMAD artifacts to Ralph format |
| `bmalph run`           | Start Ralph loop with live dashboard      |
| `bmalph reset`         | Remove all bmalph files from the project  |
| `bmalph watch`         | _(deprecated)_ Use `bmalph run` instead   |

## Dev Workflow

- TDD: write tests first, then implement
- When a test fails, analyse the root cause before changing anything. Do not take the easy route of just making the test pass — understand why it fails and fix the actual problem. A failing test is a signal, not an obstacle.
- Tests live in `tests/<module>/` (mirrors `src/` structure), not colocated
- Conventional Commits with SemVer
- Application language: English
- Node 20+ LTS
- Always run `npm run ci` locally before committing to catch formatting, lint, type, and test failures early

`npm run ci` runs (in order):

1. `type-check` — `tsc --noEmit`
2. `lint` — ESLint
3. `fmt:check` — Prettier (check only)
4. `build` — compile TypeScript
5. `test:all` — unit + e2e + bash tests

### Bash tests (BATS)

Ralph's shell scripts and platform drivers are tested with [BATS](https://github.com/bats-core/bats-core):

- Test files: `tests/bash/*.bats` + `tests/bash/drivers/*.bats`
- Fixtures: `tests/bash/fixtures/`
- Helpers: `tests/bash/test_helper/` (bats-assert, bats-support, common-setup.bash)
- Runner: `npm run test:bash` (via `scripts/run-bash-tests.mjs`)
- First-time setup: `scripts/setup-bats.sh` (installs BATS dependencies)

### Updating bundled BMAD assets

`npm run update-bundled` syncs `bmad/` from the upstream BMAD-METHOD repo (tracked as a git checkout in `.refs/bmad/`). It pulls latest from main (or a specific ref with `-- --bmad-ref <ref>`), copies `bmm/` and `core/` into `bmad/`, and updates `bundled-versions.json` with the commit SHA. After running, build + test + review diffs before committing.

Note: `bmad/lite/` is bmalph-owned content (not synced from upstream).

## CI Pipeline

- **Triggers:** push to `main`, PRs targeting `main`
- **Lint job** (ubuntu, Node 22): type-check, lint, fmt:check
- **Test matrix** (3 jobs): ubuntu/Node 22, ubuntu/Node 20, windows/Node 22
- **Test steps:** build, unit tests, e2e tests, bash tests (ubuntu only), coverage, `npm pack --dry-run`
- **Coverage:** Codecov upload on Node 22 + ubuntu only
- **Gate job:** `ci-success` aggregates all jobs — single required check for branch protection

## Release Process

- [release-please](https://github.com/googleapis/release-please) manages changelogs, version bumps, and release PRs
- On release creation: publish job runs build + test + `npm publish` to npm
- Version bumps follow Conventional Commits: `feat` = MINOR, `fix` = PATCH, `BREAKING CHANGE` = MAJOR
- Visible changelog sections: Features, Bug Fixes, Performance, Code Quality
- Hidden changelog sections: docs, tests, chores, CI, build, style

## Dependency Management

- Dependabot opens weekly grouped PRs for minor/patch updates
- Two groups: npm (production + development) and GitHub Actions
- Minor/patch PRs are auto-approved and auto-merged (squash)
- Major updates require manual review
- PR limits: 10 npm, 5 GitHub Actions

```

### File: CONTRIBUTING.md
```md
# Contributing to bmalph

## Development Setup

```bash
# Clone the repository
git clone https://github.com/LarsCowe/bmalph.git
cd bmalph

# Install dependencies
npm install

# Build TypeScript
npm run build

# Run the full local test matrix
npm run test:all

# Run the full local gate
npm run ci
```

### Requirements

- Node.js 20+ (LTS)
- npm 10+
- Bash for bundled Ralph and Bats coverage

## Project Structure

```text
bmalph/
├── src/                           # TypeScript source
│   ├── cli.ts                     # Commander.js CLI entry point
│   ├── installer/                 # Asset copying, command delivery, skills generation
│   ├── commands/                  # init, upgrade, doctor, status, implement, run, watch, reset
│   ├── platform/                  # Platform registry, detection, snippets, runtime checks
│   │   ├── cursor-runtime-checks.ts
│   │   ├── doctor-checks.ts
│   │   └── instructions-snippet.ts
│   ├── run/                       # Bash discovery, Ralph spawn, live dashboard
│   ├── transition/                # BMAD -> Ralph transition pipeline
│   ├── watch/                     # Deprecated standalone dashboard path
│   ├── reset.ts                   # Reset planner/executor
│   └── utils/                     # Shared utilities
├── tests/                         # Vitest suites
│   ├── bash/                      # Bats coverage for bundled shell assets
│   ├── commands/                  # Command unit tests
│   ├── e2e/                       # CLI workflow smoke tests
│   ├── platform/                  # Platform and detection tests
│   ├── run/                       # Run/dashboard process tests
│   ├── transition/                # Transition tests
│   └── watch/                     # Dashboard/watch tests
├── bmad/                          # Bundled BMAD-METHOD assets
├── ralph/                         # Bundled Ralph assets and templates
│   ├── drivers/                   # claude-code.sh, codex.sh, opencode.sh, copilot.sh, cursor.sh, cursor-agent-wrapper.sh
│   ├── lib/                       # Shared shell libraries
│   ├── templates/                 # PROMPT, AGENT, ralphrc templates
│   └── RALPH-REFERENCE.md         # Bundled loop/runtime reference
├── slash-commands/                # Claude Code command sources
├── scripts/                       # Maintenance and test runner scripts
├── bin/                           # CLI entry point
└── dist/                          # Compiled JavaScript (generated)
```

High-signal files for the current multi-platform runtime path:

- `src/platform/cursor-runtime-checks.ts`
- `src/run/ralph-process.ts`
- `tests/bash/`

## Test Workflow

### Unit Tests

```bash
# Run all Vitest suites except the dedicated E2E config
npm test

# Run a specific test file
npm test -- --run tests/platform/cursor-runtime-checks.test.ts

# Run tests in watch mode
npm run test:watch

# Run with coverage
npm run test:coverage
```

### Bash Tests

**Prerequisites:**

- [bats-core](https://github.com/bats-core/bats-core) must be installed
  (`brew install bats-core` on macOS, `sudo apt-get install bats` on Ubuntu).

Bundled shell assets are covered by Bats tests under `tests/bash/`.

Test helpers (`bats-support`, `bats-assert`) are installed automatically by
the script below.

```bash
# Install bats-core test helpers (one-time setup)
bash scripts/setup-bats.sh

# Run bash/driver/response-analyzer coverage
npm run test:bash
```

`npm run test:bash` uses system-installed `bats` if available, falling back to `npx bats`
when bats-core is not in PATH.

### End-to-End Tests

E2E tests verify complete workflows in isolated temp directories.

```bash
# Run E2E tests only
npm run test:e2e

# Run all tests (Vitest + E2E + Bats)
npm run test:all
```

### Test Philosophy

- **TDD**: Write tests first, then implement
- Unit tests mock external dependencies at system boundaries
- E2E tests run actual CLI commands in real directories
- Bash tests protect the bundled Ralph loop, drivers, and response analyzer

## Updating Bundled Assets

bmalph bundles BMAD-METHOD from its upstream repository. Ralph is maintained in-tree in this repo.

### Check for Updates

```bash
# Check if bundled versions are up to date
bmalph check-updates
```

### Update Process

```bash
# Sync bundled BMAD assets
npm run update-bundled

# This script:
# 1. Syncs bmad/ from the tracked checkout in .refs/bmad/
# 2. Copies bmm/ and core/ into bmad/
# 3. Updates bundled-versions.json with the upstream BMAD commit

# After updating:
npm run build
npm run test:all
```

### What Gets Bundled

| Source                     | Destination | Contents                             |
| -------------------------- | ----------- | ------------------------------------ |
| `.refs/bmad/bmm` + `core/` | `bmad/`     | Agents, workflows, templates, config |

## Commit Guidelines

We use [Conventional Commits](https://www.conventionalcommits.org/) with SemVer versioning.

### Commit Types

| Type       | SemVer | Description           |
| ---------- | ------ | --------------------- |
| `feat`     | MINOR  | New feature           |
| `fix`      | PATCH  | Bug fix               |
| `docs`     | PATCH  | Documentation only    |
| `refactor` | PATCH  | Code restructuring    |
| `test`     | PATCH  | Adding/updating tests |
| `chore`    | PATCH  | Maintenance tasks     |

### Version Bumping

Versions are managed automatically by [release-please](https://github.com/googleapis/release-please). Do **not** manually edit `package.json` version.

On every push to `main`, release-please analyzes commit messages and opens (or updates) a release PR with the correct version bump and changelog. Merging that PR triggers npm publish.

### Breaking Changes

Use `!` after type or add `BREAKING CHANGE:` footer:

```bash
git commit -m "feat(api)!: change response format"
```

## Code Style

- TypeScript strict mode
- ESLint for linting
- Prettier for formatting

```bash
# Check lint
npm run lint

# Format code
npm run fmt:fix

# Full check (types + lint + format + build + tests)
npm run ci
```

## Pull Request Process

1. Create a feature branch from `main`.
2. Write tests first.
3. Implement the change.
4. Ensure `npm run ci` passes locally.
5. Open a PR with a clear description.

## Questions?

Open an issue at [github.com/LarsCowe/bmalph/issues](https://github.com/LarsCowe/bmalph/issues)

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bmalph
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Summary

Brief description of the changes.

## Checklist

- [ ] Tests pass (`npm test`)
- [ ] Linting passes (`npm run lint`)
- [ ] Build succeeds (`npm run build`)
- [ ] Changelog updated (if applicable)
- [ ] Version bumped in `package.json` (if applicable)

```

### File: .claude\rules\cli-reference.md
```md
---
paths:
  - "src/cli.ts"
  - "src/commands/**"
  - "src/run/**"
---

# CLI Reference

## Global options

`--verbose`, `--quiet`, `--no-color`, `-C/--project-dir <path>`

## Per-command flags

| Command         | Flags                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------- |
| `init`          | `-n/--name`, `-d/--description`, `--platform <id>`, `--dry-run`                              |
| `upgrade`       | `--dry-run`, `--force`                                                                       |
| `doctor`        | `--json`                                                                                     |
| `check-updates` | `--json`                                                                                     |
| `status`        | `--json`                                                                                     |
| `implement`     | `--force`                                                                                    |
| `reset`         | `--dry-run`, `--force`                                                                       |
| `run`           | `--driver <platform>`, `--interval <ms>`, `--no-dashboard`, `--review [mode]`, `--no-review` |
| `watch`         | `--interval <ms>` _(deprecated)_                                                             |

## `bmalph run` features

- **Periodic code review** — runs between implementation loops. Modes: `enhanced` (~10-14% extra tokens) or `ultimate` (~20-30%). Disable with `--no-review`.
- **Task injection** — injects the next unchecked task into each loop's context
- **Git diff injection** — summarizes staged/unstaged changes into inter-loop context
- **Error resilience** — captures stderr, logs exit reason on driver crash/timeout, detects missing git repos

```

### File: .claude\rules\command-delivery.md
```md
---
paths:
  - "src/installer/commands.ts"
  - "src/installer/metadata.ts"
  - "src/platform/**"
  - "slash-commands/**"
---

# Command Delivery

bmalph bundles 54 BMAD and bmalph command definitions. Delivery varies by platform:

- **Claude Code** — `.claude/commands/` slash commands
- **OpenAI Codex** — `.agents/skills/` Codex Skills
- **OpenCode** — `.opencode/skills/` OpenCode Skills
- **Cursor, Windsurf, Copilot, Aider** — `_bmad/COMMANDS.md` reference index

Key commands in Claude Code syntax:

| Command                 | Description                         |
| ----------------------- | ----------------------------------- |
| `/bmalph`               | BMAD master agent — navigate phases |
| `/analyst`              | Analyst agent                       |
| `/pm`                   | Product Manager agent               |
| `/architect`            | Architect agent                     |
| `/create-prd`           | Create PRD workflow                 |
| `/create-architecture`  | Create architecture workflow        |
| `/create-epics-stories` | Create epics and stories            |
| `/dev`                  | Developer agent                     |
| `/sm`                   | Scrum Master agent                  |
| `/qa`                   | QA agent                            |
| `/ux-designer`          | UX Designer agent                   |
| `/tech-writer`          | Tech Writer agent                   |
| `/quick-flow-solo-dev`  | Quick Flow solo developer agent     |
| `/bmalph-watch`         | Launch Ralph live dashboard         |
| `/bmad-help`            | List all BMAD commands              |

For the full list, run `/bmad-help` in Claude Code or inspect `_bmad/COMMANDS.md` / `.agents/skills/` for the other platforms.

## Transition to Ralph

Use `bmalph implement` (or `/bmalph-implement`) to transition from BMAD planning to Ralph implementation.

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Report a bug to help us improve bmalph
title: ""
labels: bug
assignees: ""
---

## Describe the bug

A clear and concise description of what the bug is.

## To reproduce

Steps to reproduce the behavior:

1. Run `bmalph ...`
2. See error

## Expected behavior

A clear and concise description of what you expected to happen.

## Environment

- OS: [e.g. Windows 11, macOS 14, Ubuntu 22.04]
- Node.js version: [e.g. 20.11.0]
- bmalph version: [e.g. 2.0.0]
- Shell: [e.g. bash, zsh, Git Bash]

## Additional context

Add any other context, logs, or screenshots about the problem here.

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest a new feature for bmalph
title: ""
labels: enhancement
assignees: ""
---

## Problem

A clear and concise description of what problem this feature would solve.

## Proposed solution

Describe the solution you'd like.

## Alternatives considered

Describe any alternative solutions or features you've considered.

## Additional context

Add any other context about the feature request here.

```

