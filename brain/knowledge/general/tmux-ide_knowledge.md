---
id: tmux-ide-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.484434
---

# KNOWLEDGE EXTRACT: tmux-ide
> **Extracted on:** 2026-03-30 13:52:54
> **Source:** tmux-ide

---

## File: `.gitignore`
```
# dependencies
node_modules
docs/node_modules

# docs build output
docs/.next

# turbo cache
.turbo

# local package artifacts
*.tgz

# local OS files
.DS_Store

# local tool settings
.claude/
ide.yml

# local authoring context
context/

# local planning artifacts
plans/

# TypeScript build output
dist/
```

## File: `.prettierignore`
```
node_modules
docs/.next
docs/.source
docs/node_modules
coverage
.next
.turbo
plans
package-lock.json
pnpm-lock.yaml
docs/pnpm-lock.yaml
```

## File: `.prettierrc.json`
```json
{
  "semi": true,
  "singleQuote": false,
  "printWidth": 100
}
```

## File: `AGENTS.md`
```markdown
# tmux-ide

A CLI tool that turns any project into a tmux-powered terminal IDE using a simple `ide.yml` config file.

## Quick Start

```bash
tmux-ide              # Launch IDE from ide.yml
tmux-ide init         # Scaffold ide.yml (auto-detects stack)
tmux-ide inspect      # Show resolved config + live tmux state
tmux-ide stop         # Kill session
tmux-ide attach       # Reattach to running session
```

## ide.yml Format

```yaml
name: project-name # tmux session name

before: pnpm install # optional pre-launch hook

rows:
  - size: 70% # row height percentage
    panes:
      - title: Claude 1 # pane border label
        command: claude # command to run (optional)
        size: 50% # pane width percentage (optional)
        dir: apps/web # per-pane working directory (optional)
        focus: true # initial focus (optional)
        env: # environment variables (optional)
          PORT: 3000

  - panes:
      - title: Dev Server
        command: pnpm dev
      - title: Shell

team: # optional agent team config
  name: my-team

theme: # optional color overrides
  accent: colour75
  border: colour238
  bg: colour235
  fg: colour248
```

### Agent Team Pane Fields

```yaml
panes:
  - title: Lead
    command: claude
    role: lead # optional layout metadata: "lead" or "teammate"
    focus: true
  - title: Frontend
    command: claude
    role: teammate
    task: "Work on components" # suggested task text for your prompts
```

## Architecture

- `bin/cli.js` — CLI entry point and top-level error boundary
- `src/launch.js` — Launch orchestration for tmux sessions
- `src/restart.js` — Stop + relaunch flow
- `src/init.js` — Scaffolds ide.yml with smart detection
- `src/stop.js` — Kills the tmux session
- `src/attach.js` — Reattach to running session
- `src/ls.js` — List tmux sessions
- `src/doctor.js` — System health check
- `src/status.js` — Session status query
- `src/inspect.js` — Resolved config + live tmux inspection
- `src/validate.js` — Config validation
- `src/detect.js` — Project stack detection
- `src/config.js` — Programmatic config mutations
- `src/lib/tmux.js` — Shared tmux process helpers
- `src/lib/launch-plan.js` — Pane startup planning + theme option generation
- `src/lib/yaml-io.js` — Shared config read/write
- `src/lib/dot-path.js` — Dot-notation get/set
- `src/lib/output.js` — Structured CLI error/output helpers
- `src/lib/sizes.js` — Row/pane sizing math
- `src/*.test.js`, `src/lib/*.test.js` — CLI, unit, and integration coverage
- `docs/content/docs/` — User-facing docs site content
- `.github/workflows/ci.yml` — CI quality gates and release checks
- `templates/` — Preset configs (default, nextjs, convex, vite, python, go, agent-team, agent-team-nextjs, agent-team-monorepo)

## Programmatic CLI Reference

All commands support `--json` for structured output.

### Read Commands

```bash
# Session status
tmux-ide status --json
# → { "session": "...", "running": true, "configExists": true, "panes": [...] }

# Validate config
tmux-ide validate --json
# → { "valid": true, "errors": [] }

# Detect project stack
tmux-ide detect --json
# → { "detected": { "packageManager": "pnpm", "frameworks": ["next", "convex"], ... }, "suggestedConfig": {...} }

# Dump config as JSON
tmux-ide config --json
# → { "name": "...", "rows": [...] }

# List sessions
tmux-ide ls --json
# → { "sessions": [{ "name": "...", "created": "...", "attached": true }] }

# System check
tmux-ide doctor --json
# → { "ok": true, "checks": [...] }

# Inspect resolved config + live tmux data
tmux-ide inspect --json
# → { "valid": true, "session": "...", "resolved": {...}, "tmux": {...} }
```

### Write Commands

```bash
# Detect and write config
tmux-ide detect --write

# Set a config value by dot path
tmux-ide config set name "my-app"
tmux-ide config set rows.0.size "70%"
tmux-ide config set rows.1.panes.0.command "npm run dev"

# Add a pane to a row
tmux-ide config add-pane --row 1 --title "Tests" --command "pnpm test"

# Remove a pane
tmux-ide config remove-pane --row 1 --pane 2

# Add a new row
tmux-ide config add-row --size "30%"

# Enable agent teams
tmux-ide config enable-team --name "my-team"

# Disable agent teams
tmux-ide config disable-team
```

### Session Commands

```bash
tmux-ide              # Launch (or re-launch) IDE
tmux-ide stop         # Kill session
tmux-ide attach       # Reattach
tmux-ide init         # Scaffold config (auto-detects stack)
tmux-ide init --template nextjs  # Use specific template
```

## Agent Workflow

### When to suggest tmux-ide

- User mentions multi-pane, tmux, terminal IDE, dev environment
- User wants to set up a development workspace
- User asks about running multiple terminals/tools side-by-side
- User wants coordinated multi-agent development (agent teams)
- User mentions team lead, teammates, or task delegation

### Setup workflow

1. Check if `ide.yml` exists: `tmux-ide status --json`
2. Auto-detect the project: `tmux-ide detect --json`
3. Present 2-3 layout options to the user using ASCII diagrams before writing any config.
4. Once the user picks an option, write the config:
   - Quick path: `tmux-ide detect --write` then modify as needed
   - Or build custom with `tmux-ide config add-row`, `add-pane`, and `config set`
5. Validate: `tmux-ide validate --json`

### Modification workflow

1. Read current config: `tmux-ide config --json`
2. Modify: `tmux-ide config set <path> <value>` or `add-pane`/`remove-pane`
3. Validate: `tmux-ide validate --json`
4. Inspect when needed: `tmux-ide inspect --json`

### Agent Teams workflow

For coordinated multi-agent development:

1. `tmux-ide config enable-team --name "my-team"` or `tmux-ide init --template agent-team`
2. Assign tasks: `tmux-ide config set rows.0.panes.1.task "Work on frontend"`
3. Validate: `tmux-ide validate --json`
4. Launch: `tmux-ide` or `tmux-ide restart`
5. In the lead pane, ask Claude to create and organize the team in natural language

tmux-ide prepares the tmux layout and enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` when `team` is configured. It does not synthesize hidden Claude CLI flags for team creation.

The team lead can self-configure the workspace layout with `tmux-ide config ...`, then `restart` to apply changes.

## Contributor Workflow

```bash
pnpm install --frozen-lockfile
pnpm lint
pnpm format:check
pnpm test
pnpm pack:check
```

- Main release gate: `pnpm check`
- Live tmux coverage: `pnpm test:integration`
- Docs build: `pnpm docs:build`

## Best practices

- Always use `--json` for programmatic access
- Always run `validate --json` after config mutations
- Prefer `inspect --json` when debugging config/runtime mismatches
- Top row should be ~70% height for Claude panes
- 2-3 Claude panes in the top row (or lead + 2 teammate-ready panes for agent teams)
- Dev servers + shell in the bottom row
- Use `detect --json` first to understand the project stack
- For agent teams: assign specific tasks to teammate panes for focused parallel work
```

## File: `ARCHITECTURE.md`
```markdown
# Architecture

## Overview

`tmux-ide` is a small Node.js CLI that turns an `ide.yml` file into a tmux session layout.

The codebase is intentionally simple:

- [bin/cli.js](/Users/thijs/Developer/tmux-ide/bin/cli.js) is the CLI edge
- [src/](/Users/thijs/Developer/tmux-ide/src) contains command modules and runtime helpers
- [templates/](/Users/thijs/Developer/tmux-ide/templates) contains starter configs
- [docs/](/Users/thijs/Developer/tmux-ide/docs) is the public docs app

## Runtime Model

The main runtime flow is:

1. Parse CLI arguments in [bin/cli.js](/Users/thijs/Developer/tmux-ide/bin/cli.js)
2. Load and validate `ide.yml`
3. Resolve pane layout and tmux session structure
4. Create or inspect the tmux session
5. Send commands, apply titles, theme, focus, and optional team behavior

Key modules:

- [src/validate.js](/Users/thijs/Developer/tmux-ide/src/validate.js): config validation
- [src/launch.js](/Users/thijs/Developer/tmux-ide/src/launch.js): launch orchestration
- [src/lib/tmux.js](/Users/thijs/Developer/tmux-ide/src/lib/tmux.js): shared tmux command boundary
- [src/lib/launch-plan.js](/Users/thijs/Developer/tmux-ide/src/lib/launch-plan.js): pure launch planning logic
- [src/inspect.js](/Users/thijs/Developer/tmux-ide/src/inspect.js): effective config + runtime inspection

## Error Boundary

Structured command failures should reach the CLI edge as `CommandError` instances from [src/lib/output.js](/Users/thijs/Developer/tmux-ide/src/lib/output.js).

That keeps:

- human output and `--json` output consistent
- exit behavior centralized in the CLI entrypoint
- command modules easier to test

## tmux Boundary

[src/lib/tmux.js](/Users/thijs/Developer/tmux-ide/src/lib/tmux.js) is the shared wrapper for tmux operations.

It currently owns:

- session existence/state checks
- session creation and kill behavior
- pane listing
- pane splitting, titles, selection, and command injection
- tmux error classification

The direction of the codebase is to keep more tmux child-process handling here rather than in individual command modules.

## Testing Strategy

The project uses the Node.js built-in test runner.

Test layers:

- pure unit tests for helpers under [src/lib/](/Users/thijs/Developer/tmux-ide/src/lib)
- CLI contract tests in [src/cli.test.js](/Users/thijs/Developer/tmux-ide/src/cli.test.js)
- targeted command tests such as [src/inspect.test.js](/Users/thijs/Developer/tmux-ide/src/inspect.test.js)
- live tmux integration coverage in [src/integration.test.js](/Users/thijs/Developer/tmux-ide/src/integration.test.js)

The highest-risk path is still the launch lifecycle, so changes there should prefer:

- extracting pure helpers first
- adding unit coverage for decision-making
- adding live tmux coverage with `attach: false` when possible

## Release Checks

The intended release path is:

```bash
npm run check
```

That should cover:

- lint
- formatting
- tests
- docs build
- package packing sanity
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

## 1.1.0

### Added

- `inspect` command for resolved config and runtime state
- detection reasoning in human and JSON output
- targeted CLI hardening tests for error handling and edge cases
- docs build validation in the release workflow
- contributor, release, and security project documentation

### Changed

- centralized tmux session state handling for several lifecycle commands
- improved config mutation validation and error reporting
- tightened npm packaging and CI coverage
- limited Claude integration postinstall changes to global installs with existing Claude config

### Fixed

- `inspect` now reports invalid config state instead of crashing on malformed pane arrays
- `restart --json` now preserves structured launch errors
- launch logic now uses returned tmux pane IDs instead of assuming sequential numbering
```

## File: `CLAUDE.md`
```markdown
# tmux-ide

A CLI tool that turns any project into a tmux-powered terminal IDE using a simple `ide.yml` config file.

## Quick Start

```bash
tmux-ide              # Launch IDE from ide.yml
tmux-ide init         # Scaffold ide.yml (auto-detects stack)
tmux-ide inspect      # Show resolved config + live tmux state
tmux-ide stop         # Kill session
tmux-ide attach       # Reattach to running session
```

## ide.yml Format

```yaml
name: project-name # tmux session name

before: pnpm install # optional pre-launch hook

rows:
  - size: 70% # row height percentage
    panes:
      - title: Claude 1 # pane border label
        command: claude # command to run (optional)
        size: 50% # pane width percentage (optional)
        dir: apps/web # per-pane working directory (optional)
        focus: true # initial focus (optional)
        env: # environment variables (optional)
          PORT: 3000

  - panes:
      - title: Dev Server
        command: pnpm dev
      - title: Shell

team: # optional agent team config
  name: my-team

theme: # optional color overrides
  accent: colour75
  border: colour238
  bg: colour235
  fg: colour248
```

### Agent Team Pane Fields

```yaml
panes:
  - title: Lead
    command: claude
    role: lead # optional layout metadata: "lead" or "teammate"
    focus: true
  - title: Frontend
    command: claude
    role: teammate
    task: "Work on components" # suggested task text for your prompts
```

## Architecture

The project is written in TypeScript. Source lives in `src/`, compiled output in `dist/`. Tests run via Node's `--experimental-strip-types`; the published package ships compiled JS from `tsc`.

- `bin/cli.js` — CLI entry point and top-level error boundary (stays JS, imports from `dist/`)
- `tsconfig.json` — TypeScript config (strict, NodeNext, rewriteRelativeImportExtensions)
- `src/types.ts` — Shared interfaces (IdeConfig, Row, Pane, ThemeConfig, PaneAction, SessionState)
- `src/launch.ts` — Launch orchestration for tmux sessions
- `src/restart.ts` — Stop + relaunch flow
- `src/init.ts` — Scaffolds ide.yml with smart detection
- `src/stop.ts` — Kills the tmux session
- `src/attach.ts` — Reattach to running session
- `src/ls.ts` — List tmux sessions
- `src/doctor.ts` — System health check
- `src/status.ts` — Session status query
- `src/inspect.ts` — Resolved config + live tmux inspection
- `src/validate.ts` — Config validation
- `src/detect.ts` — Project stack detection
- `src/config.ts` — Programmatic config mutations
- `src/lib/tmux.ts` — Shared tmux process helpers
- `src/lib/launch-plan.ts` — Pane startup planning + theme option generation
- `src/lib/yaml-io.ts` — Shared config read/write
- `src/lib/dot-path.ts` — Dot-notation get/set
- `src/lib/output.ts` — Structured CLI error/output helpers
- `src/lib/sizes.ts` — Row/pane sizing math
- `src/lib/errors.ts` — Error class hierarchy (IdeError, ConfigError, TmuxError, SessionError)
- `src/lib/session-options.ts` — Composable tmux session option builders
- `src/lib/session-monitor.ts` — Agent/port status monitor (runs as detached process)
- `src/*.test.ts`, `src/lib/*.test.ts` — CLI, unit, and integration coverage
- `docs/content/docs/` — User-facing docs site content
- `.github/workflows/ci.yml` — CI quality gates and release checks
- `templates/` — Preset configs (default, nextjs, convex, vite, python, go, agent-team, agent-team-nextjs, agent-team-monorepo)

## Programmatic CLI Reference

All commands support `--json` for structured output.

### Read Commands

```bash
# Session status
tmux-ide status --json
# → { "session": "...", "running": true, "configExists": true, "panes": [...] }

# Validate config
tmux-ide validate --json
# → { "valid": true, "errors": [] }

# Detect project stack
tmux-ide detect --json
# → { "detected": { "packageManager": "pnpm", "frameworks": ["next", "convex"], ... }, "suggestedConfig": {...} }

# Dump config as JSON
tmux-ide config --json
# → { "name": "...", "rows": [...] }

# List sessions
tmux-ide ls --json
# → { "sessions": [{ "name": "...", "created": "...", "attached": true }] }

# System check
tmux-ide doctor --json
# → { "ok": true, "checks": [...] }

# Inspect resolved config + live tmux data
tmux-ide inspect --json
# → { "valid": true, "session": "...", "resolved": {...}, "tmux": {...} }
```

### Write Commands

```bash
# Detect and write config
tmux-ide detect --write

# Set a config value by dot path
tmux-ide config set name "my-app"
tmux-ide config set rows.0.size "70%"
tmux-ide config set rows.1.panes.0.command "npm run dev"

# Add a pane to a row
tmux-ide config add-pane --row 1 --title "Tests" --command "pnpm test"

# Remove a pane
tmux-ide config remove-pane --row 1 --pane 2

# Add a new row
tmux-ide config add-row --size "30%"

# Enable agent teams
tmux-ide config enable-team --name "my-team"

# Disable agent teams
tmux-ide config disable-team
```

### Session Commands

```bash
tmux-ide              # Launch (or re-launch) IDE
tmux-ide stop         # Kill session
tmux-ide attach       # Reattach
tmux-ide init         # Scaffold config (auto-detects stack)
tmux-ide init --template nextjs  # Use specific template
```

## Claude Skill

### When to suggest tmux-ide

- User mentions multi-pane, tmux, terminal IDE, dev environment
- User wants to set up a development workspace
- User asks about running multiple terminals/tools side-by-side
- User wants coordinated multi-agent development (agent teams)
- User mentions team lead, teammates, or task delegation

### Setup workflow

1. Check if `ide.yml` exists: `tmux-ide status --json`
2. Auto-detect the project: `tmux-ide detect --json`
3. **Present 2-3 layout options to the user using ASCII diagrams** before writing any config. Show the pane arrangement visually so the user can pick or tweak. Example:

   **Option A — Dual Claude + Dev (recommended)**

   ```
   ┌─────────────────┬─────────────────┐
   │                 │                 │
   │    Claude 1     │    Claude 2     │  70%
   │                 │                 │
   ├────────┬────────┴────────┬────────┤
   │Dev Srv │  Tests  │ Shell │        │  30%
   └────────┴─────────┴───────┘────────┘
   ```

   **Option B — Triple Claude**

   ```
   ┌───────────┬───────────┬───────────┐
   │           │           │           │
   │ Claude 1  │ Claude 2  │ Claude 3  │  70%
   │           │           │           │
   ├───────────┴─────┬─────┴───────────┤
   │    Dev Server    │     Shell       │  30%
   └─────────────────┴─────────────────┘
   ```

   **Option C — Single Claude + wide dev**

   ```
   ┌─────────────────────────────────────┐
   │             Claude                  │  60%
   ├──────────┬──────────┬──────────────┤
   │ Dev Srv  │  Tests   │    Shell     │  40%
   └──────────┴──────────┴──────────────┘
   ```

   Adapt pane names/commands to the detected stack (e.g., `pnpm dev`, `cargo watch`, `go run`). Always tailor the options to the project.

4. Once the user picks an option, write the config:
   - Quick path: `tmux-ide detect --write` then modify as needed
   - Or build custom:
     ```bash
     tmux-ide config add-row --size "70%"
     tmux-ide config add-pane --row 0 --title "Claude 1" --command "claude"
     tmux-ide config add-pane --row 0 --title "Claude 2" --command "claude"
     tmux-ide config add-row
     tmux-ide config add-pane --row 1 --title "Dev" --command "pnpm dev"
     tmux-ide config add-pane --row 1 --title "Shell"
     tmux-ide validate --json
     ```

### Modification workflow

1. Read current config: `tmux-ide config --json`
2. Modify: `tmux-ide config set <path> <value>` or `add-pane`/`remove-pane`
3. Validate: `tmux-ide validate --json`

### Agent Teams workflow

For coordinated multi-agent development:

1. `tmux-ide config enable-team --name "my-team"` or `tmux-ide init --template agent-team`
2. Assign tasks: `tmux-ide config set rows.0.panes.1.task "Work on frontend"`
3. Validate: `tmux-ide validate --json`
4. Launch: `tmux-ide` or `tmux-ide restart`
5. In the lead pane, ask Claude to create and organize the team in natural language

tmux-ide prepares the tmux layout and enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` when `team` is configured. It does not synthesize hidden Claude CLI flags for team creation.

The team lead can self-configure the workspace layout with `tmux-ide config ...`, then `restart` to apply changes.

## Contributor Workflow

```bash
pnpm install --frozen-lockfile
pnpm lint
pnpm format:check
pnpm test
pnpm pack:check
```

- Main release gate: `pnpm check`
- Live tmux coverage: `pnpm test:integration`
- Docs build: `pnpm docs:build`

### Best practices

- Always use `--json` for programmatic access
- Always run `validate --json` after config mutations
- Prefer `inspect --json` when debugging config/runtime mismatches
- Top row should be ~70% height for Claude panes
- 2-3 Claude panes in the top row (or lead + 2 teammate-ready panes for agent teams)
- Dev servers + shell in the bottom row
- Use `detect --json` first to understand the project stack
- For agent teams: assign specific tasks to teammate panes for focused parallel work
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

## Setup

Requirements:

- Node.js 18 or newer
- pnpm 10 or newer
- tmux 3.0 or newer for manual CLI smoke tests

Install dependencies:

```bash
pnpm install --frozen-lockfile
```

## Development Workflow

Main commands:

```bash
pnpm test
pnpm docs:build
pnpm check
```

`pnpm check` is the default pre-push command. It runs the CLI test suite, builds the docs site, and verifies the package can be packed cleanly.

`npm publish` is guarded by `prepublishOnly`, so a publish attempt runs the same full check path automatically.

## Testing Notes

- `npm test` runs the Node test suite.
- `pnpm test:integration` exercises live tmux behavior and is skipped automatically when tmux is unavailable.
- `pnpm docs:build` validates the docs app production build.

For a manual tmux smoke test:

```bash
node bin/cli.js init
node bin/cli.js inspect --json
node bin/cli.js
```

Then in another shell:

```bash
node bin/cli.js status --json
node bin/cli.js stop --json
```

## Pull Requests

- Keep behavior changes covered by tests.
- Update README and docs when the CLI contract changes.
- Keep `CHANGELOG.md` changes under `Unreleased` until the release is actually cut.
- Prefer focused PRs over large mixed changes.
- Run `pnpm check` before opening or updating a PR.
```

## File: `eslint.config.js`
```javascript
import js from "@eslint/js";
import globals from "globals";
import tsParser from "@typescript-eslint/parser";
import tsPlugin from "@typescript-eslint/eslint-plugin";

export default [
  {
    ignores: [
      "docs/**",
      "node_modules/**",
      "coverage/**",
      "context/**",
      "dist/**",
      ".next/**",
      "plans/**",
      "templates/**",
      ".github/**",
    ],
  },
  js.configs.recommended,
  {
    files: ["bin/**/*.js", "scripts/**/*.js", "src/**/*.js", "*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        ...globals.node,
      },
    },
    rules: {
      "no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
    },
  },
  {
    files: ["src/**/*.ts"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      parser: tsParser,
      globals: {
        ...globals.node,
      },
    },
    plugins: {
      "@typescript-eslint": tsPlugin,
    },
    rules: {
      ...tsPlugin.configs.recommended.rules,
      "no-undef": "off",
      "no-unused-vars": "off",
      "@typescript-eslint/no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
    },
  },
];
```

## File: `ide.yml`
```yaml
name: tmux-ide

team:
  name: tmux-ide

rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead
        focus: true
      - title: Docs Agent
        command: claude
        role: teammate
        task: "Work on the docs site at docs/ — Next.js + Fumadocs, landing page, MDX content"
        dir: docs
      - title: CLI Agent
        command: claude
        role: teammate
        task: "Work on the CLI source code at src/ and bin/ — commands, validation, templates"

  - panes:
      - title: Docs Dev
        command: pnpm docs
      - title: Shell
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 wavyrai

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

## File: `package.json`
```json
{
  "name": "tmux-ide",
  "version": "1.3.1",
  "description": "Turn any project into a tmux-powered terminal IDE with a simple ide.yml",
  "type": "module",
  "bin": {
    "tmux-ide": "bin/cli.js"
  },
  "files": [
    "bin",
    "dist",
    "scripts",
    "skill",
    "templates"
  ],
  "scripts": {
    "clean": "rm -rf dist",
    "build": "pnpm run clean && tsc",
    "typecheck": "tsc --noEmit",
    "dev": "node --experimental-strip-types bin/cli.js",
    "test": "node --experimental-strip-types --test src/*.test.ts src/lib/*.test.ts",
    "test:unit": "node --experimental-strip-types --test src/cli.test.ts src/config-cli.test.ts src/config.test.ts src/detect.test.ts src/doctor.test.ts src/init.test.ts src/inspect.test.ts src/launch.test.ts src/ls.test.ts src/stop.test.ts src/validate.test.ts src/lib/*.test.ts",
    "test:integration": "node --experimental-strip-types --test src/integration.test.ts",
    "lint": "eslint .",
    "lint:workspace": "turbo run lint",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "build:workspace": "turbo run build",
    "typecheck:workspace": "turbo run typecheck",
    "docs:build": "turbo run build --filter=@tmux-ide/docs",
    "pack:check": "npm pack --dry-run --cache /tmp/tmux-ide-npm-cache > /dev/null",
    "check": "pnpm run lint:workspace && pnpm run format:check && pnpm run build && pnpm run test:unit && pnpm run docs:build && pnpm run pack:check",
    "prepublishOnly": "pnpm run build",
    "postinstall": "node scripts/postinstall.js",
    "docs": "turbo run dev --filter=@tmux-ide/docs"
  },
  "keywords": [
    "tmux",
    "ide",
    "terminal",
    "workspace",
    "developer-tools"
  ],
  "engines": {
    "node": ">=18"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/wavyrai/tmux-ide.git"
  },
  "homepage": "https://github.com/wavyrai/tmux-ide#readme",
  "bugs": {
    "url": "https://github.com/wavyrai/tmux-ide/issues"
  },
  "license": "MIT",
  "packageManager": "pnpm@10.21.0",
  "dependencies": {
    "js-yaml": "^4.1.1"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@types/node": "^25.5.0",
    "@typescript-eslint/eslint-plugin": "^8.57.1",
    "@typescript-eslint/parser": "^8.57.1",
    "eslint": "^10.0.3",
    "globals": "^17.4.0",
    "prettier": "^3.8.1",
    "turbo": "^2.3.3",
    "typescript": "^5.9.3"
  }
}
```

## File: `pnpm-workspace.yaml`
```yaml
packages:
  - .
  - docs
```

## File: `README.md`
```markdown
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
| `tmux-ide detect --write`                          | Detect and write `ide.yml`              |
| `tmux-ide config`                                  | Dump config as JSON                     |
| `tmux-ide config set <path> <value>`               | Set a config value                      |
| `tmux-ide config add-pane --row <N>`               | Add a pane to a row                     |
| `tmux-ide config remove-pane --row <N> --pane <M>` | Remove a pane                           |
| `tmux-ide config add-row [--size <percent>]`       | Add a new row                           |
| `tmux-ide config enable-team --name <name>`        | Enable agent teams                      |
| `tmux-ide config disable-team`                     | Disable agent teams                     |

All commands support `--json` for structured output.

`tmux-ide detect` now includes reasoning about the package manager, language, framework, and dev-command signals it used. `tmux-ide inspect` combines config validation, resolved layout details, and live tmux state in one command.

## Templates

Use `tmux-ide init --template <name>` with one of:

- `default` - General-purpose layout
- `nextjs` - Next.js development
- `convex` - Convex + Next.js
- `vite` - Vite project
- `python` - Python development
- `go` - Go development
- `agent-team` - Agent team with lead + teammates
- `agent-team-nextjs` - Agent team for Next.js
- `agent-team-monorepo` - Agent team for monorepos

## Contributor Workflow

The repo now uses a pnpm workspace with a root CLI package and a separate docs app package:

```bash
pnpm install
pnpm test
pnpm docs:build
pnpm check
pnpm pack:check
```

`pnpm check` is the intended local pre-push command and matches the default release checklist. `npm publish` is still guarded by `prepublishOnly`, so publishing runs the same full check path automatically.

## CI

GitHub Actions validates:

- the Node CLI test suite on Node 18, 20, and 22
- the docs site production build
- the package can be packed successfully with `npm pack --dry-run`

That keeps the release surface small but catches the main regressions for a CLI-first package.

## Open Source Project Files

- [CONTRIBUTING.md](CONTRIBUTING.md) for local setup and contribution workflow
- [RELEASE.md](RELEASE.md) for the publish checklist
- [CHANGELOG.md](CHANGELOG.md) for release notes
- [SECURITY.md](SECURITY.md) for vulnerability reporting

Release note convention:

- Keep the next version under an `Unreleased` heading in `CHANGELOG.md` until the tag is cut.
- Move it to a dated release entry when the release is actually published.

## Requirements

- **tmux** >= 3.0
- **Node.js** >= 18

## License

[MIT](LICENSE)
```

## File: `RELEASE.md`
```markdown
# Release Checklist

## Preflight

1. Confirm `package.json` has the intended version.
2. Make sure `CHANGELOG.md` is updated under `Unreleased`.
3. Review `git status` and ensure only intentional changes are present.

## Verification

Run the full release checks from the repo root:

```bash
pnpm check
```

If tmux is available locally, also run:

```bash
pnpm test:integration
```

Recommended manual smoke test:

```bash
node bin/cli.js init
node bin/cli.js inspect --json
node bin/cli.js
```

In a second shell:

```bash
node bin/cli.js status --json
node bin/cli.js stop --json
```

If you want to verify the global install hook on a machine with Claude Code already configured:

```bash
npm install -g .
```

Then confirm:

- `~/.claude/skills/tmux-ide/SKILL.md` exists
- `~/.claude/settings.json` contains `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`

## Publish

1. Move the `Unreleased` changelog notes into a dated release entry.
2. Commit the release changes.
3. Create an annotated tag such as `v1.1.0`.
4. Push the branch and tag.
5. Publish with `npm publish`.
6. Create a GitHub release using the matching changelog notes.

## Post-release

1. Verify the npm package page and install command.
2. Verify the GitHub release notes and tag.
3. Smoke test `npm install -g tmux-ide` on a clean machine if possible.
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

Security fixes are applied to the latest released version of `tmux-ide`.

## Reporting a Vulnerability

Please do not open a public GitHub issue for security-sensitive reports.

Preferred private reporting path:

1. Use GitHub Security Advisories for this repository:
   `https://github.com/wavyrai/tmux-ide/security/advisories`
2. If advisories are unavailable, use the private contact method listed on the maintainer GitHub profile or npm package profile.

If neither private path is available, do not file a public issue with exploit details. Open a minimal issue asking the maintainer to provide a private contact channel without including sensitive information.

When reporting, include:

- affected version
- operating system and shell
- reproduction steps
- impact assessment
- any proposed mitigation

We will aim to acknowledge reports promptly and work on a fix before public disclosure where possible.
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "dist",
    "rootDir": "src",
    "declaration": true,
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "skipLibCheck": true,
    "rewriteRelativeImportExtensions": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["src/**/*.test.ts"]
}
```

## File: `turbo.json`
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {
      "outputs": []
    },
    "test": {
      "outputs": [],
      "cache": false
    },
    "typecheck": {
      "dependsOn": ["^typecheck"],
      "outputs": []
    }
  }
}
```

## File: `docs/.gitignore`
```
# deps
/node_modules

# generated source files
.source
/.turbo

# Next.js build output
/coverage
/.next/
/out/
/build
*.tsbuildinfo

# local environment and deployment files
.env*.local
.vercel
next-env.d.ts

# misc
.DS_Store
*.pem
/.pnp
.pnp.js
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `docs/mdx-components.tsx`
```tsx
import defaultMdxComponents from "fumadocs-ui/mdx";
import type { MDXComponents } from "mdx/types";

export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    ...components,
  };
}
```

## File: `docs/next.config.mjs`
```
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createMDX } from "fumadocs-mdx/next";

const withMDX = createMDX();
const docsDir = dirname(fileURLToPath(import.meta.url));

/** @type {import('next').NextConfig} */
const config = {
  serverExternalPackages: ["@takumi-rs/image-response"],
  reactStrictMode: true,
  transpilePackages: ["geist"],
  turbopack: {
    root: resolve(docsDir, ".."),
  },
  async rewrites() {
    return [
      {
        source: "/docs/:path*.mdx",
        destination: "/llms.mdx/docs/:path*",
      },
    ];
  },
};

export default withMDX(config);
```

## File: `docs/package.json`
```json
{
  "name": "@tmux-ide/docs",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "generate": "fumadocs-mdx",
    "build": "pnpm run generate && next build",
    "dev": "pnpm run generate && next dev",
    "lint": "pnpm run typecheck",
    "start": "next start",
    "typecheck": "pnpm run generate && tsc --noEmit",
    "types:check": "pnpm run typecheck"
  },
  "dependencies": {
    "@takumi-rs/image-response": "^0.70.4",
    "fumadocs-core": "16.6.13",
    "fumadocs-mdx": "14.2.9",
    "fumadocs-ui": "16.6.13",
    "geist": "^1.7.0",
    "js-yaml": "^4.1.1",
    "lucide-react": "^0.577.0",
    "next": "16.1.6",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "tailwind-merge": "^3.5.0"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4.2.1",
    "@types/js-yaml": "^4.0.9",
    "@types/mdx": "^2.0.13",
    "@types/node": "^25.3.5",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "postcss": "^8.5.8",
    "tailwindcss": "^4.2.1",
    "typescript": "^5.9.3"
  }
}
```

## File: `docs/postcss.config.mjs`
```
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};

export default config;
```

## File: `docs/README.md`
```markdown
# Docs

This is the documentation app for `tmux-ide`. It is a Next.js site built with Fumadocs and published as the project docs surface.

## Commands

```bash
pnpm install --frozen-lockfile
pnpm docs
pnpm docs:build
```

Open the local site at `http://localhost:3000` after starting `pnpm docs`.

## Maintenance Notes

- Content pages live under `content/docs/`.
- The docs navigation is defined in `content/docs/meta.json`.
- Root-level `pnpm docs:build` delegates to this app's production build and is part of the release check path.
- Keep docs changes aligned with CLI behavior changes in the main package.

## Explore

In the project, you can see:

- `lib/source.ts`: Code for content source adapter, [`loader()`](https://fumadocs.dev/docs/headless/source-api) provides the interface to access your content.
- `lib/layout.shared.tsx`: Shared options for layouts, optional but preferred to keep.

| Route                     | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `app/(home)`              | The route group for your landing page and other pages. |
| `app/docs`                | The documentation layout and pages.                    |
| `app/api/search/route.ts` | The Route Handler for search.                          |

### Fumadocs MDX

A `source.config.ts` config file is included for frontmatter and content-source behavior.

Read the [Introduction](https://fumadocs.dev/docs/mdx) for further details.
```

## File: `docs/source.config.ts`
```typescript
import { defineConfig, defineDocs } from "fumadocs-mdx/config";
import { metaSchema, pageSchema } from "fumadocs-core/source/schema";

// You can customise Zod schemas for frontmatter and `meta.json` here
// see https://fumadocs.dev/docs/mdx/collections
export const docs = defineDocs({
  dir: "content/docs",
  docs: {
    schema: pageSchema,
    postprocess: {
      includeProcessedMarkdown: true,
    },
  },
  meta: {
    schema: metaSchema,
  },
});

export default defineConfig({
  mdxOptions: {
    // MDX options
  },
});
```

## File: `docs/tsconfig.json`
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "paths": {
      "@/*": ["./*"],
      "fumadocs-mdx:collections/*": [".source/*"]
    },
    "plugins": [
      {
        "name": "next"
      }
    ]
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": ["node_modules"]
}
```

## File: `docs/turbo.json`
```json
{
  "extends": ["//"],
  "tasks": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**", ".source/**"]
    },
    "typecheck": {
      "outputs": [".next/types/**", ".next/dev/types/**", ".source/**"]
    }
  }
}
```

## File: `docs/app/apple-icon.tsx`
```tsx
import { ImageResponse } from "next/og";

export const size = {
  width: 180,
  height: 180,
};

export const contentType = "image/png";

export default function AppleIcon() {
  return new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#0a0a0a",
        borderRadius: "32px",
      }}
    >
      <span
        style={{
          fontSize: "120px",
          fontWeight: "bold",
          color: "#fff",
          fontFamily: "monospace",
        }}
      >
        t
      </span>
    </div>,
    {
      ...size,
    },
  );
}
```

## File: `docs/app/global.css`
```css
@import "tailwindcss";
@import "fumadocs-ui/css/neutral.css";
@import "fumadocs-ui/css/preset.css";

@theme {
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
  --font-pixel: var(--font-geist-pixel-square);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes paneIn {
  from {
    flex: 0 0 0%;
    opacity: 0;
    transform: scaleX(0.3);
  }
  to {
    flex: 1 1 0%;
    opacity: 1;
    transform: scaleX(1);
  }
}

@utility animate-fade-in {
  animation: fadeIn 400ms ease-out;
}

@utility animate-pane-in {
  animation: paneIn 600ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

## File: `docs/app/icon.tsx`
```tsx
import { ImageResponse } from "next/og";

export const size = {
  width: 32,
  height: 32,
};

export const contentType = "image/png";

export default function Icon() {
  return new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#0a0a0a",
        borderRadius: "6px",
      }}
    >
      <span
        style={{
          fontSize: "20px",
          fontWeight: "bold",
          color: "#fff",
          fontFamily: "monospace",
        }}
      >
        t
      </span>
    </div>,
    {
      ...size,
    },
  );
}
```

## File: `docs/app/layout.tsx`
```tsx
import { RootProvider } from "fumadocs-ui/provider/next";
import "./global.css";
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import { GeistPixelSquare } from "geist/font/pixel";
import type { Metadata } from "next";

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "https://tmux.thijsverreck.com";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "tmux-ide — Prepare Claude agent-team layouts in one terminal",
    template: "%s | tmux-ide",
  },
  description:
    "Prepare Claude Code agent-team-ready tmux layouts with lead and teammate panes plus the right environment setup.",
  keywords: [
    "Claude Code",
    "agent teams",
    "tmux",
    "terminal IDE",
    "Claude",
    "multi-agent",
    "tmux-ide",
    "CLI",
    "developer tools",
    "AI coding",
    "terminal multiplexer",
  ],
  authors: [{ name: "Thijs Verreck", url: "https://thijsverreck.com" }],
  creator: "Thijs Verreck",
  openGraph: {
    type: "website",
    locale: "en_US",
    siteName: "tmux-ide",
    title: "tmux-ide — Prepare Claude agent-team layouts in one terminal",
    description:
      "Prepare Claude Code agent-team-ready tmux layouts with lead and teammate panes plus the right environment setup.",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "tmux-ide — Claude agent-team layouts in tmux",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "tmux-ide — Prepare Claude agent-team layouts in one terminal",
    description:
      "Prepare Claude Code agent-team-ready tmux layouts with lead and teammate panes plus the right environment setup.",
    images: ["/og-image.png"],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
};

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="en"
      className={`${GeistSans.variable} ${GeistMono.variable} ${GeistPixelSquare.variable}`}
      suppressHydrationWarning
    >
      <body className="flex flex-col min-h-screen">
        <RootProvider>{children}</RootProvider>
      </body>
    </html>
  );
}
```

## File: `docs/app/robots.ts`
```typescript
import type { MetadataRoute } from "next";

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "https://tmux.thijsverreck.com";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
      },
    ],
    sitemap: `${siteUrl}/sitemap.xml`,
  };
}
```

## File: `docs/app/sitemap.ts`
```typescript
import type { MetadataRoute } from "next";
import { source } from "@/lib/source";

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "https://tmux.thijsverreck.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const docs = source.getPages().map((page) => ({
    url: `${siteUrl}${page.url}`,
    lastModified: new Date(),
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  return [
    {
      url: siteUrl,
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 1,
    },
    ...docs,
  ];
}
```

## File: `docs/app/(home)/agent-team-demo.tsx`
```tsx
"use client";

import { useState, useEffect, useRef, useCallback } from "react";

// ── Types ──────────────────────────────────────────────────────────────

interface DemoPane {
  id: string;
  title: string;
  role?: "lead" | "teammate";
  lines: string[];
}

interface DemoRow {
  size: number;
  panes: DemoPane[];
}

// ── Pane component ───────────────────────────────────────────────────

function DemoPaneView({
  pane,
  isActive,
  isNew,
}: {
  pane: DemoPane;
  isActive: boolean;
  isNew: boolean;
}) {
  return (
    <div
      className={`
        flex flex-col rounded-sm overflow-hidden min-w-0
        ${isNew ? "animate-pane-in" : ""}
        ${isActive ? "ring-1 ring-amber-500/40" : ""}
      `}
      style={isNew ? undefined : { flex: "1 1 0%" }}
    >
      {/* Pane title bar */}
      <div
        className={`
          flex items-center gap-1.5 px-2.5 py-1 text-[11px] border-b shrink-0
          ${isActive ? "border-amber-500/40 bg-amber-500/5" : "border-white/5 bg-white/[0.02]"}
        `}
      >
        <span
          className={`font-medium truncate ${isActive ? "text-amber-400" : "text-neutral-400"}`}
        >
          {isActive ? "▸" : "·"} {pane.title}
        </span>
        {pane.role === "lead" && (
          <span className="text-[9px] px-1 py-0.5 rounded bg-amber-500/20 text-amber-400 font-medium shrink-0 ml-auto">
            lead
          </span>
        )}
        {pane.role === "teammate" && (
          <span className="text-[9px] px-1 py-0.5 rounded bg-blue-500/20 text-blue-400 font-medium shrink-0 ml-auto">
            teammate
          </span>
        )}
      </div>
      {/* Pane content */}
      <div className="flex-1 p-2.5 bg-neutral-900/80 font-mono text-[11px] leading-[1.6] overflow-hidden">
        {pane.lines.map((line, i) => (
          <div key={i} className={lineColor(line)}>
            {line}
          </div>
        ))}
      </div>
    </div>
  );
}

function lineColor(line: string): string {
  if (line.startsWith("$")) return "text-neutral-300";
  if (line.startsWith("→") || line.startsWith("✓")) return "text-green-400/80";
  if (line.startsWith("⟡") || line.startsWith("●")) return "text-amber-400/80";
  if (line.startsWith("…")) return "text-blue-400/70";
  return "text-neutral-500";
}

// ── Demo orchestrator ────────────────────────────────────────────────

export function AgentTeamDemo() {
  const [rows, setRows] = useState<DemoRow[]>([]);
  const [activePane, setActivePane] = useState("lead");
  const [newPaneId, setNewPaneId] = useState<string | null>(null);
  const [phase, setPhase] = useState(0);
  const timeoutsRef = useRef<ReturnType<typeof setTimeout>[]>([]);

  const addLine = useCallback((paneId: string, line: string) => {
    setRows((prev) =>
      prev.map((row) => ({
        ...row,
        panes: row.panes.map((p) => (p.id === paneId ? { ...p, lines: [...p.lines, line] } : p)),
      })),
    );
  }, []);

  const resetDemo = useCallback(() => {
    for (const t of timeoutsRef.current) clearTimeout(t);
    timeoutsRef.current = [];
    setNewPaneId(null);
    setActivePane("lead");
    setPhase(0);

    // Initial state: Lead + Frontend teammate | Dev + Shell
    setRows([
      {
        size: 70,
        panes: [
          {
            id: "lead",
            title: "Lead",
            role: "lead",
            lines: ['> "Start an agent team for my-app."'],
          },
          {
            id: "frontend",
            title: "Frontend",
            role: "teammate",
            lines: ["… teammate pane ready"],
          },
        ],
      },
      {
        size: 30,
        panes: [
          { id: "dev", title: "Next.js", lines: ["$ pnpm dev", "→ ready on localhost:3000"] },
          { id: "shell", title: "Shell", lines: ["$"] },
        ],
      },
    ]);

    const schedule = (ms: number, fn: () => void) => {
      timeoutsRef.current.push(setTimeout(fn, ms));
    };

    // Lead analyzes
    schedule(800, () => {
      addLine("lead", "⟡ Analyzing project structure...");
      addLine("frontend", "… Waiting for task assignment...");
      setPhase(1);
    });

    // Lead decides to spawn
    schedule(2200, () => {
      addLine("lead", "● Need an API specialist. Adding a teammate pane...");
      setPhase(2);
    });

    // New pane slides in
    schedule(3200, () => {
      setRows((prev) => {
        const newRows = [...prev];
        newRows[0] = {
          ...newRows[0],
          panes: [
            ...newRows[0].panes,
            {
              id: "api",
              title: "API Agent",
              role: "teammate",
              lines: ["… teammate pane ready"],
            },
          ],
        };
        return newRows;
      });
      setNewPaneId("api");
      setPhase(3);
    });

    // Team ready
    schedule(4000, () => {
      addLine("lead", "✓ Team ready — 3 Claude panes coordinating.");
      setNewPaneId(null);
      setPhase(4);
    });

    // Assign tasks
    schedule(5000, () => {
      addLine("lead", "");
      addLine("lead", "⟡ Assigning tasks:");
      addLine("lead", "  → Frontend: React components");
      addLine("lead", "  → API Agent: REST endpoints");
      setPhase(5);
    });

    // Teammates acknowledge
    schedule(6000, () => {
      addLine("frontend", "✓ Task received: React components");
      addLine("frontend", "… Reading src/components/...");
      setActivePane("frontend");
      setPhase(6);
    });

    schedule(6800, () => {
      addLine("api", "✓ Task received: REST endpoints");
      addLine("api", "… Reading src/api/routes/...");
      setActivePane("api");
    });

    // Working state
    schedule(7800, () => {
      setActivePane("lead");
      addLine("lead", "");
      addLine("lead", "⟡ Monitoring team progress...");
      setPhase(7);
    });

    // Loop
    schedule(11000, () => resetDemo());
  }, [addLine]);

  useEffect(() => {
    resetDemo();
    return () => {
      for (const t of timeoutsRef.current) clearTimeout(t);
    };
  }, [resetDemo]);

  return (
    <div className="w-full max-w-4xl mx-auto">
      <div className="rounded-xl border border-white/10 overflow-hidden bg-neutral-950 shadow-2xl shadow-black/40">
        {/* Terminal chrome */}
        <div className="flex items-center gap-2 px-4 py-2.5 border-b border-white/10 bg-neutral-900/50">
          <div className="flex gap-1.5">
            <div className="w-2.5 h-2.5 rounded-full bg-[#ff5f57]/80" />
            <div className="w-2.5 h-2.5 rounded-full bg-[#febc2e]/80" />
            <div className="w-2.5 h-2.5 rounded-full bg-[#28c840]/80" />
          </div>
          <span className="text-[11px] text-neutral-500 font-mono ml-2">MY-APP IDE</span>
          <div className="ml-auto flex items-center gap-2">
            {phase >= 3 ? (
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-green-500/10 text-green-400/80 font-mono animate-fade-in">
                3 agents
              </span>
            ) : phase > 0 ? (
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-400/80 font-mono">
                2 agents
              </span>
            ) : null}
          </div>
        </div>

        {/* Pane grid */}
        <div className="flex flex-col min-h-[340px]">
          {rows.map((row, ri) => (
            <div key={ri} className="flex gap-px" style={{ flex: `${row.size} 0 0%` }}>
              {row.panes.map((pane) => (
                <DemoPaneView
                  key={pane.id}
                  pane={pane}
                  isActive={activePane === pane.id}
                  isNew={newPaneId === pane.id}
                />
              ))}
            </div>
          ))}
        </div>

        {/* Status bar */}
        <div className="flex items-center justify-between px-3 py-1.5 border-t border-white/10 text-[10px] font-mono bg-neutral-900/50">
          <span className="text-amber-400/60">MY-APP IDE</span>
          <span className="text-neutral-600">
            {phase >= 3
              ? "team: my-app (3 members)"
              : phase > 0
                ? "team: my-app (2 members)"
                : "team: my-app"}
          </span>
        </div>
      </div>
    </div>
  );
}
```

## File: `docs/app/(home)/config-playground.tsx`
```tsx
"use client";

import { useState, useCallback, useRef, type KeyboardEvent } from "react";
import yaml from "js-yaml";

// ── Types ──────────────────────────────────────────────────────────────

interface Pane {
  title?: string;
  command?: string;
  size?: string;
  focus?: boolean;
  role?: "lead" | "teammate";
  task?: string;
}

interface Row {
  size?: string;
  panes: Pane[];
}

interface Team {
  name: string;
  model?: string;
  permissions?: string[];
}

interface IdeConfig {
  name?: string;
  team?: Team;
  rows: Row[];
}

// ── Templates ──────────────────────────────────────────────────────────

const templates = [
  {
    id: "default",
    label: "Default",
    yaml: `name: my-project

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Dev Server
      - title: Shell`,
  },
  {
    id: "nextjs",
    label: "Next.js",
    yaml: `name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude
      - title: Claude 3
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Shell
        focus: true`,
  },
  {
    id: "convex",
    label: "Convex",
    yaml: `name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude
      - title: Claude 3
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Convex
        command: npx convex dev
      - title: Shell
        focus: true`,
  },
  {
    id: "vite",
    label: "Vite",
    yaml: `name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Vite
        command: pnpm dev
      - title: Shell
        focus: true`,
  },
  {
    id: "python",
    label: "Python",
    yaml: `name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Server
        command: uvicorn main:app --reload
      - title: Shell
        focus: true`,
  },
  {
    id: "go",
    label: "Go",
    yaml: `name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Go
        command: go run .
      - title: Shell
        focus: true`,
  },
  {
    id: "agent-team",
    label: "Agent Team",
    yaml: `name: my-app

team:
  name: my-app

rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead
        focus: true
      - title: Frontend
        command: claude
        role: teammate
        task: "Work on React components"
      - title: Backend
        command: claude
        role: teammate
        task: "Work on API routes"

  - panes:
      - title: Dev Server
        command: pnpm dev
      - title: Shell`,
  },
];

// ── Parsing ────────────────────────────────────────────────────────────

function parseConfig(text: string): IdeConfig | null {
  try {
    const parsed = yaml.load(text) as Record<string, unknown>;
    if (!parsed || typeof parsed !== "object" || !Array.isArray(parsed.rows)) return null;
    for (const row of parsed.rows) {
      if (!row || typeof row !== "object" || !Array.isArray(row.panes)) return null;
    }
    return parsed as unknown as IdeConfig;
  } catch {
    return null;
  }
}

// ── Sizing ─────────────────────────────────────────────────────────────

function computeSizes(items: { size?: string }[]): number[] {
  let claimed = 0;
  let unclaimed = 0;
  for (const item of items) {
    if (item.size) claimed += parseFloat(item.size);
    else unclaimed++;
  }
  const remaining = Math.max(0, 100 - claimed);
  const defaultSize = unclaimed > 0 ? remaining / unclaimed : 0;
  return items.map((item) => (item.size ? parseFloat(item.size) : defaultSize));
}

// ── Preview ────────────────────────────────────────────────────────────

function LayoutPreview({ config }: { config: IdeConfig }) {
  const rowSizes = computeSizes(config.rows);

  return (
    <div className="flex flex-col h-full">
      {/* Terminal chrome */}
      <div className="flex items-center gap-2 px-4 py-2.5 border-b border-white/10">
        <div className="flex gap-1.5">
          <div className="w-3 h-3 rounded-full bg-[#ff5f57]" />
          <div className="w-3 h-3 rounded-full bg-[#febc2e]" />
          <div className="w-3 h-3 rounded-full bg-[#28c840]" />
        </div>
        <span className="text-xs text-neutral-400 font-mono ml-2">tmux session</span>
      </div>

      {/* Pane grid */}
      <div className="flex-1 flex flex-col p-2 gap-px min-h-[280px]">
        {config.rows.map((row, ri) => {
          const paneSizes = computeSizes(row.panes);
          return (
            <div key={ri} className="flex gap-px" style={{ flex: `${rowSizes[ri]} 0 0%` }}>
              {row.panes.map((pane, pi) => (
                <div
                  key={pi}
                  className={`flex flex-col rounded-sm px-3 py-2 bg-neutral-800/80 ${
                    pane.focus ? "border-l-2 border-l-green-500" : ""
                  }`}
                  style={{ flex: `${paneSizes[pi]} 0 0%` }}
                >
                  <div className="flex items-center gap-1.5">
                    <span className="text-xs font-bold text-neutral-200 truncate">
                      {pane.title || `Pane ${pi + 1}`}
                    </span>
                    {pane.role === "lead" && (
                      <span className="text-[9px] px-1 py-0.5 rounded bg-amber-500/20 text-amber-400 font-medium shrink-0">
                        lead
                      </span>
                    )}
                    {pane.role === "teammate" && (
                      <span className="text-[9px] px-1 py-0.5 rounded bg-blue-500/20 text-blue-400 font-medium shrink-0">
                        team
                      </span>
                    )}
                  </div>
                  {pane.command && (
                    <span className="text-[11px] font-mono text-neutral-500 truncate mt-0.5">
                      $ {pane.command}
                    </span>
                  )}
                  {pane.task && (
                    <span className="text-[10px] text-neutral-500 truncate mt-0.5 italic">
                      {pane.task}
                    </span>
                  )}
                  {pane.focus && (
                    <span className="text-[10px] text-green-500 mt-auto">◉ focus</span>
                  )}
                </div>
              ))}
            </div>
          );
        })}
      </div>

      {/* Status bar */}
      <div className="flex items-center justify-between px-3 py-1.5 border-t border-white/10 text-[11px] font-mono text-neutral-500">
        <span>[0] {config.name || "session"}</span>
        <span>12:00</span>
      </div>
    </div>
  );
}

// ── Playground ─────────────────────────────────────────────────────────

export function ConfigPlayground() {
  const [yamlText, setYamlText] = useState(templates[0].yaml);
  const [config, setConfig] = useState<IdeConfig>(() => parseConfig(templates[0].yaml)!);
  const [error, setError] = useState<string | null>(null);
  const [activeTemplate, setActiveTemplate] = useState<string>("default");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleYamlChange = useCallback(
    (text: string) => {
      setYamlText(text);
      if (activeTemplate) setActiveTemplate("");
      const parsed = parseConfig(text);
      if (parsed) {
        setConfig(parsed);
        setError(null);
      } else {
        setError("Invalid YAML");
      }
    },
    [activeTemplate],
  );

  const handleTemplateClick = useCallback((t: (typeof templates)[0]) => {
    setYamlText(t.yaml);
    setActiveTemplate(t.id);
    setConfig(parseConfig(t.yaml)!);
    setError(null);
  }, []);

  const handleKeyDown = useCallback(
    (e: KeyboardEvent<HTMLTextAreaElement>) => {
      if (e.key === "Tab") {
        e.preventDefault();
        const ta = textareaRef.current;
        if (!ta) return;
        const start = ta.selectionStart;
        const end = ta.selectionEnd;
        const newText = yamlText.substring(0, start) + "  " + yamlText.substring(end);
        setYamlText(newText);
        // Update config from the new text
        const parsed = parseConfig(newText);
        if (parsed) {
          setConfig(parsed);
          setError(null);
        }
        // Restore cursor position after React re-renders
        requestAnimationFrame(() => {
          ta.selectionStart = ta.selectionEnd = start + 2;
        });
      }
    },
    [yamlText],
  );

  return (
    <div className="w-full max-w-5xl mx-auto">
      {/* Template buttons */}
      <div className="flex flex-wrap gap-2 mb-4 justify-center">
        {templates.map((t) => (
          <button
            key={t.id}
            onClick={() => handleTemplateClick(t)}
            className={`px-3 py-1.5 rounded-md text-sm font-medium transition-colors cursor-pointer ${
              activeTemplate === t.id
                ? "bg-fd-primary text-fd-primary-foreground"
                : "bg-fd-muted text-fd-muted-foreground hover:bg-fd-accent hover:text-fd-accent-foreground"
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      {/* Editor + Preview */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 items-stretch">
        {/* YAML editor */}
        <div className="rounded-lg border border-fd-border bg-fd-background overflow-hidden flex flex-col">
          <div className="flex items-center justify-between px-4 py-2.5 border-b border-fd-border">
            <span className="text-xs text-fd-muted-foreground font-mono">ide.yml</span>
            {error && <span className="text-xs text-red-500 font-mono">{error}</span>}
          </div>
          <textarea
            ref={textareaRef}
            value={yamlText}
            onChange={(e) => handleYamlChange(e.target.value)}
            onKeyDown={handleKeyDown}
            spellCheck={false}
            className="flex-1 p-4 font-mono text-sm leading-relaxed bg-transparent text-fd-foreground/80 resize-none outline-none min-h-[320px]"
          />
        </div>

        {/* Layout preview */}
        <div className="rounded-lg border border-fd-border overflow-hidden bg-neutral-900 text-neutral-200 flex flex-col">
          <LayoutPreview config={config} />
        </div>
      </div>
    </div>
  );
}
```

## File: `docs/app/(home)/copy-button.tsx`
```tsx
"use client";

import { useState, useCallback } from "react";

export function CopyButton({
  text,
  className,
  children,
}: {
  text: string;
  className?: string;
  children: React.ReactNode;
}) {
  const [copied, setCopied] = useState(false);

  const copy = useCallback(() => {
    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
      });
    } else {
      // Fallback for non-HTTPS (e.g. localhost dev server)
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  }, [text]);

  return (
    <button
      type="button"
      onClick={copy}
      className={className}
      aria-label={copied ? "Copied!" : "Copy to clipboard"}
    >
      {copied ? (
        <span className="inline-flex items-center gap-2">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <polyline points="20 6 9 17 4 12" />
          </svg>
          Copied!
        </span>
      ) : (
        children
      )}
    </button>
  );
}
```

## File: `docs/app/(home)/layout.tsx`
```tsx
import { HomeLayout } from "fumadocs-ui/layouts/home";
import { baseOptions } from "@/lib/layout.shared";

export default function Layout({ children }: { children: React.ReactNode }) {
  return <HomeLayout {...baseOptions()}>{children}</HomeLayout>;
}
```

## File: `docs/app/(home)/page.tsx`
```tsx
import Link from "next/link";
import type { Metadata } from "next";
import { CopyButton } from "./copy-button";
import { ConfigPlayground } from "./config-playground";
import { AgentTeamDemo } from "./agent-team-demo";

export const metadata: Metadata = {
  title: "tmux-ide — Prepare Claude agent-team layouts in one terminal",
  description:
    "Prepare Claude Code agent-team-ready tmux layouts. One lead pane, multiple teammate panes, practical prompts, and the right environment setup in one YAML config.",
  openGraph: {
    title: "tmux-ide — Prepare Claude agent-team layouts in one terminal",
    description:
      "Prepare Claude Code agent-team-ready tmux layouts with lead and teammate panes plus the right environment setup.",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "tmux-ide — Claude agent-team layouts in tmux",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "tmux-ide — Prepare Claude agent-team layouts in one terminal",
    description:
      "Prepare Claude Code agent-team-ready tmux layouts with lead and teammate panes plus the right environment setup.",
    images: ["/og-image.png"],
  },
  alternates: {
    canonical: "/",
  },
};

const installCommand = "curl -fsSL https://tmux.thijsverreck.com/install.sh | sh";

function InstallButton() {
  return (
    <div className="flex flex-col items-center gap-3">
      <CopyButton
        text={installCommand}
        className="group inline-flex items-center gap-3 rounded-lg border border-fd-border bg-fd-background px-5 py-3 font-mono text-sm transition-colors hover:bg-fd-accent cursor-pointer"
      >
        <span className="text-fd-muted-foreground select-none">$</span>
        <span className="text-fd-foreground">{installCommand}</span>
        <svg
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="text-fd-muted-foreground group-hover:text-fd-foreground transition-colors shrink-0"
        >
          <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
        </svg>
      </CopyButton>
      <div className="flex flex-wrap items-center justify-center gap-x-4 gap-y-1 text-xs text-fd-muted-foreground">
        <span>
          or <code className="font-mono text-fd-foreground">npm i -g tmux-ide</code>
        </span>
        <span>
          or try instantly with <code className="font-mono text-fd-foreground">npx tmux-ide</code>
        </span>
      </div>
    </div>
  );
}

function Feature({ title, description }: { title: string; description: string }) {
  return (
    <div className="text-center space-y-2">
      <h3 className="font-medium text-fd-foreground">{title}</h3>
      <p className="text-sm text-fd-muted-foreground leading-relaxed">{description}</p>
    </div>
  );
}

export default function HomePage() {
  return (
    <div className="flex flex-col items-center flex-1">
      {/* Hero */}
      <section className="flex flex-col items-center gap-8 px-6 pt-24 pb-16 max-w-3xl mx-auto text-center">
        <div className="flex flex-col items-center gap-3">
          <span
            aria-hidden="true"
            className="font-pixel text-6xl sm:text-7xl md:text-8xl tracking-tight text-fd-foreground select-none"
          >
            tmux-ide
          </span>
          <Link
            href="/docs/release-1-3-0"
            className="inline-flex items-center rounded-full border border-fd-border bg-fd-card px-3 py-1 text-[11px] font-mono font-medium uppercase tracking-[0.18em] text-fd-muted-foreground transition-colors hover:bg-fd-accent hover:text-fd-foreground"
          >
            New 1.3.0
          </Link>
        </div>
        <h1 className="text-4xl sm:text-5xl font-bold tracking-tight text-fd-foreground">
          Prepare Claude agent-team layouts
          <br />
          <span className="text-fd-muted-foreground">in one terminal.</span>
        </h1>
        <p className="text-lg text-fd-muted-foreground max-w-xl leading-relaxed">
          Build a lead pane, teammate-ready Claude panes, and your dev tools in one tmux layout.
          tmux-ide enables the right environment; Claude forms the team after you prompt it.
        </p>

        <div className="flex flex-col sm:flex-row items-center gap-4">
          <Link
            href="/docs/agent-teams"
            className="rounded-lg bg-fd-primary px-6 py-2.5 text-sm font-medium text-fd-primary-foreground hover:bg-fd-primary/90 transition-colors"
          >
            Set Up Agent Teams
          </Link>
          <Link
            href="/docs/getting-started"
            className="rounded-lg border border-fd-border px-6 py-2.5 text-sm font-medium text-fd-foreground hover:bg-fd-accent transition-colors"
          >
            Get Started
          </Link>
          <Link
            href="/docs"
            className="rounded-lg border border-fd-border px-6 py-2.5 text-sm font-medium text-fd-muted-foreground hover:bg-fd-accent hover:text-fd-foreground transition-colors"
          >
            Docs
          </Link>
        </div>
      </section>

      {/* Install */}
      <section className="flex flex-col items-center gap-4 px-6 pb-20">
        <InstallButton />
        <p className="text-xs text-fd-muted-foreground mt-2">
          The install script also registers the{" "}
          <Link
            href="/docs/getting-started#claude-code-skill"
            className="underline hover:text-fd-foreground transition-colors"
          >
            Claude Code skill
          </Link>{" "}
          — so Claude can configure your workspace automatically.
        </p>
      </section>

      {/* Agent Teams Demo */}
      <section className="w-full px-6 pb-24">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-semibold text-fd-foreground">
            Team-ready panes, then Claude takes over
          </h2>
          <p className="text-sm text-fd-muted-foreground mt-2 max-w-lg mx-auto">
            tmux-ide prepares the panes and enables agent-team mode. From there, prompt the lead to
            organize the team and assign work in natural language.
          </p>
        </div>
        <AgentTeamDemo />
        <div className="flex justify-center mt-6">
          <Link
            href="/docs/agent-teams"
            className="text-sm text-fd-muted-foreground hover:text-fd-foreground transition-colors"
          >
            Read the Agent Teams guide →
          </Link>
        </div>
      </section>

      {/* Config Playground */}
      <section className="w-full px-6 pb-20">
        <div className="text-center mb-8">
          <h2 className="text-2xl font-semibold text-fd-foreground">Config in, layout out</h2>
          <p className="text-sm text-fd-muted-foreground mt-2">
            Edit the YAML and watch the layout update live. Try a preset to get started.
          </p>
        </div>
        <ConfigPlayground />
      </section>

      {/* Features */}
      <section className="w-full max-w-4xl mx-auto px-6 pb-24">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
          <Feature
            title="Lead + teammates"
            description="One Claude coordinates the team. Teammates work independently in their own panes, each with a focused task."
          />
          <Feature
            title="Shared task list"
            description="Agents communicate through shared tasks and messages. The lead assigns, teammates claim and report back."
          />
          <Feature
            title="Self-organizing"
            description="Once the layout is running, the lead can recruit teammates, reassign work, and reshape the workflow through normal Claude prompting."
          />
          <Feature
            title="Declarative YAML"
            description="Define your team layout in ide.yml — roles, tasks, pane sizes. Reproducible across machines and projects."
          />
          <Feature
            title="Any stack"
            description="Auto-detects Next.js, Vite, Python, Go, and more. Dev servers run alongside your agent team."
          />
          <Feature
            title="One command"
            description="tmux-ide handles tmux sessions, pane splitting, and the experimental env flag. You launch the layout, then tell Claude how to organize the team."
          />
          <Feature
            title="Claude Code skill built in"
            description="The install script registers a Claude Code skill automatically. Ask Claude to set up your workspace and it handles detection, layout, and config."
          />
        </div>
      </section>

      {/* Workflow */}
      <section className="w-full max-w-2xl mx-auto px-6 pb-24">
        <div className="rounded-lg border border-fd-border bg-fd-background overflow-hidden">
          <div className="px-4 py-2.5 border-b border-fd-border">
            <span className="text-xs text-fd-muted-foreground font-mono">Quick start</span>
          </div>
          <div className="p-4 font-mono text-sm space-y-1 text-fd-foreground/80">
            <p>
              <span className="text-fd-muted-foreground select-none">$ </span>
              cd ~/Developer/my-project
            </p>
            <p>
              <span className="text-fd-muted-foreground select-none">$ </span>
              tmux-ide init --template agent-team
            </p>
            <p className="text-fd-muted-foreground">→ Created ide.yml with agent team layout.</p>
            <p>
              <span className="text-fd-muted-foreground select-none">$ </span>
              tmux-ide
            </p>
            <p className="text-fd-muted-foreground">
              → Launching IDE session with lead and teammate-ready panes...
            </p>
            <p>
              <span className="text-fd-muted-foreground select-none">$ </span>
              tmux-ide restart
            </p>
            <p className="text-fd-muted-foreground">→ Restarted with updated layout.</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="w-full border-t border-fd-border py-8 px-6">
        <div className="max-w-3xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-fd-muted-foreground">
          <span>
            tmux-ide by{" "}
            <a
              href="https://thijsverreck.com"
              className="hover:text-fd-foreground transition-colors"
              target="_blank"
              rel="noopener noreferrer"
            >
              Thijs Verreck
            </a>
          </span>
          <div className="flex items-center gap-4">
            <Link href="/docs" className="hover:text-fd-foreground transition-colors">
              Docs
            </Link>
            <a
              href={`https://github.com/wavyrai/tmux-ide`}
              className="hover:text-fd-foreground transition-colors"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
```

## File: `docs/app/api/search/route.ts`
```typescript
import { source } from "@/lib/source";
import { createFromSource } from "fumadocs-core/search/server";

export const { GET } = createFromSource(source, {
  // https://docs.orama.com/docs/orama-js/supported-languages
  language: "english",
});
```

## File: `docs/app/docs/layout.tsx`
```tsx
import { source } from "@/lib/source";
import { DocsLayout } from "fumadocs-ui/layouts/docs";
import { baseOptions } from "@/lib/layout.shared";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <DocsLayout tree={source.getPageTree()} {...baseOptions()}>
      {children}
    </DocsLayout>
  );
}
```

## File: `docs/app/docs/[[...slug]]/page.tsx`
```tsx
import { getPageImage, source } from "@/lib/source";
import {
  DocsBody,
  DocsDescription,
  DocsPage,
  DocsTitle,
  MarkdownCopyButton,
  ViewOptionsPopover,
} from "fumadocs-ui/layouts/docs/page";
import { notFound } from "next/navigation";
import { getMDXComponents } from "@/mdx-components";
import type { Metadata } from "next";
import { createRelativeLink } from "fumadocs-ui/mdx";
import { gitConfig } from "@/lib/layout.shared";

export default async function Page(props: { params: Promise<{ slug?: string[] }> }) {
  const params = await props.params;
  const page = source.getPage(params.slug);
  if (!page) notFound();

  const MDX = page.data.body;

  return (
    <DocsPage toc={page.data.toc} full={page.data.full}>
      <DocsTitle>{page.data.title}</DocsTitle>
      <DocsDescription className="mb-0">{page.data.description}</DocsDescription>
      <div className="flex flex-row gap-2 items-center border-b pb-6">
        <MarkdownCopyButton markdownUrl={`${page.url}.mdx`} />
        <ViewOptionsPopover
          markdownUrl={`${page.url}.mdx`}
          githubUrl={`https://github.com/${gitConfig.user}/${gitConfig.repo}/blob/${gitConfig.branch}/content/docs/${page.path}`}
        />
      </div>
      <DocsBody>
        <MDX
          components={getMDXComponents({
            // this allows you to link to other pages with relative file paths
            a: createRelativeLink(source, page),
          })}
        />
      </DocsBody>
    </DocsPage>
  );
}

export async function generateStaticParams() {
  return source.generateParams();
}

export async function generateMetadata(props: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const params = await props.params;
  const page = source.getPage(params.slug);
  if (!page) notFound();

  return {
    title: page.data.title,
    description: page.data.description,
    openGraph: {
      images: getPageImage(page).url,
    },
  };
}
```

## File: `docs/app/llms-full.txt/route.ts`
```typescript
import { getLLMText, source } from "@/lib/source";

export const revalidate = false;

export async function GET() {
  const scan = source.getPages().map(getLLMText);
  const scanned = await Promise.all(scan);

  return new Response(scanned.join("\n\n"));
}
```

## File: `docs/app/llms.mdx/docs/[[...slug]]/route.ts`
```typescript
import { getLLMText, source } from "@/lib/source";
import { notFound } from "next/navigation";

export const revalidate = false;

export async function GET(_req: Request, { params }: { params: Promise<{ slug?: string[] }> }) {
  const { slug } = await params;
  const page = source.getPage(slug);
  if (!page) notFound();

  return new Response(await getLLMText(page), {
    headers: {
      "Content-Type": "text/markdown",
    },
  });
}

export function generateStaticParams() {
  return source.generateParams();
}
```

## File: `docs/app/llms.txt/route.ts`
```typescript
import { source } from "@/lib/source";
import { llms } from "fumadocs-core/source";

export const revalidate = false;

export function GET() {
  return new Response(llms(source).index());
}
```

## File: `docs/app/og/docs/[...slug]/route.tsx`
```tsx
import { getPageImage, source } from "@/lib/source";
import { notFound } from "next/navigation";
import { ImageResponse } from "@takumi-rs/image-response";
import { generate as DefaultImage } from "fumadocs-ui/og/takumi";

export const revalidate = false;

export async function GET(_req: Request, { params }: { params: Promise<{ slug: string[] }> }) {
  const { slug } = await params;
  const page = source.getPage(slug.slice(0, -1));
  if (!page) notFound();

  return new ImageResponse(
    <DefaultImage title={page.data.title} description={page.data.description} site="tmux-ide" />,
    {
      width: 1200,
      height: 630,
      format: "webp",
    },
  );
}

export function generateStaticParams() {
  return source.getPages().map((page) => ({
    lang: page.locale,
    slug: getPageImage(page).segments,
  }));
}
```

## File: `docs/app/og-image.png/route.tsx`
```tsx
import { ImageResponse } from "@takumi-rs/image-response";

export const revalidate = false;

export async function GET() {
  return new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#0a0a0a",
        fontFamily: "monospace",
      }}
    >
      {/* Terminal window chrome */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          width: "1040px",
          borderRadius: "16px",
          border: "1px solid rgba(255,255,255,0.1)",
          overflow: "hidden",
          backgroundColor: "#111",
        }}
      >
        {/* Title bar */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            padding: "14px 20px",
            borderBottom: "1px solid rgba(255,255,255,0.1)",
            backgroundColor: "#161616",
          }}
        >
          <div style={{ display: "flex", gap: "8px" }}>
            <div
              style={{
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "#ff5f57",
              }}
            />
            <div
              style={{
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "#febc2e",
              }}
            />
            <div
              style={{
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: "#28c840",
              }}
            />
          </div>
          <span
            style={{
              marginLeft: "16px",
              fontSize: "13px",
              color: "#666",
            }}
          >
            MY-APP IDE
          </span>
        </div>

        {/* Pane layout */}
        <div style={{ display: "flex", height: "240px", gap: "1px" }}>
          {/* Lead pane */}
          <div
            style={{
              flex: 1,
              display: "flex",
              flexDirection: "column",
              backgroundColor: "#0d0d0d",
              borderRight: "1px solid rgba(255,255,255,0.06)",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "6px",
                padding: "8px 14px",
                borderBottom: "1px solid rgba(217,173,69,0.3)",
                fontSize: "12px",
              }}
            >
              <span style={{ color: "#d9ad45" }}>▸ Lead</span>
              <span
                style={{
                  fontSize: "10px",
                  padding: "2px 6px",
                  borderRadius: "4px",
                  backgroundColor: "rgba(217,173,69,0.15)",
                  color: "#d9ad45",
                  marginLeft: "auto",
                }}
              >
                lead
              </span>
            </div>
            <div style={{ padding: "10px 14px", fontSize: "12px" }}>
              <div style={{ color: "#999" }}>{'> "Start the my-app team."'}</div>
              <div style={{ color: "#22c55e", marginTop: "4px" }}>
                ✓ Team ready — lead and teammates coordinating
              </div>
            </div>
          </div>

          {/* Teammate 1 */}
          <div
            style={{
              flex: 1,
              display: "flex",
              flexDirection: "column",
              backgroundColor: "#0d0d0d",
              borderRight: "1px solid rgba(255,255,255,0.06)",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "6px",
                padding: "8px 14px",
                borderBottom: "1px solid rgba(255,255,255,0.04)",
                fontSize: "12px",
              }}
            >
              <span style={{ color: "#777" }}>· Frontend</span>
              <span
                style={{
                  fontSize: "10px",
                  padding: "2px 6px",
                  borderRadius: "4px",
                  backgroundColor: "rgba(59,130,246,0.15)",
                  color: "#60a5fa",
                  marginLeft: "auto",
                }}
              >
                teammate
              </span>
            </div>
            <div style={{ padding: "10px 14px", fontSize: "12px" }}>
              <div style={{ color: "#666" }}>… teammate pane ready</div>
              <div style={{ color: "#60a5fa", marginTop: "4px", opacity: 0.7 }}>
                … components/Header.tsx
              </div>
            </div>
          </div>

          {/* Teammate 2 */}
          <div
            style={{
              flex: 1,
              display: "flex",
              flexDirection: "column",
              backgroundColor: "#0d0d0d",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "6px",
                padding: "8px 14px",
                borderBottom: "1px solid rgba(255,255,255,0.04)",
                fontSize: "12px",
              }}
            >
              <span style={{ color: "#777" }}>· API Agent</span>
              <span
                style={{
                  fontSize: "10px",
                  padding: "2px 6px",
                  borderRadius: "4px",
                  backgroundColor: "rgba(59,130,246,0.15)",
                  color: "#60a5fa",
                  marginLeft: "auto",
                }}
              >
                teammate
              </span>
            </div>
            <div style={{ padding: "10px 14px", fontSize: "12px" }}>
              <div style={{ color: "#666" }}>… teammate pane ready</div>
              <div style={{ color: "#60a5fa", marginTop: "4px", opacity: 0.7 }}>
                … src/api/routes/...
              </div>
            </div>
          </div>
        </div>

        {/* Bottom row */}
        <div
          style={{
            display: "flex",
            height: "80px",
            gap: "1px",
            borderTop: "1px solid rgba(255,255,255,0.06)",
          }}
        >
          <div
            style={{
              flex: 1,
              padding: "8px 14px",
              backgroundColor: "#0d0d0d",
              borderRight: "1px solid rgba(255,255,255,0.06)",
            }}
          >
            <div style={{ fontSize: "12px", color: "#777", marginBottom: "4px" }}>· Next.js</div>
            <div style={{ fontSize: "11px", color: "#22c55e" }}>→ ready on localhost:3000</div>
          </div>
          <div
            style={{
              flex: 1,
              padding: "8px 14px",
              backgroundColor: "#0d0d0d",
            }}
          >
            <div style={{ fontSize: "12px", color: "#777", marginBottom: "4px" }}>· Shell</div>
            <div style={{ fontSize: "11px", color: "#999" }}>$</div>
          </div>
        </div>

        {/* Status bar */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "6px 14px",
            borderTop: "1px solid rgba(255,255,255,0.1)",
            backgroundColor: "#161616",
            fontSize: "11px",
          }}
        >
          <span style={{ color: "#d9ad45", opacity: 0.6 }}>MY-APP IDE</span>
          <span style={{ color: "#555" }}>team: my-app (3 members)</span>
        </div>
      </div>

      {/* Branding below */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          marginTop: "32px",
          gap: "8px",
        }}
      >
        <span
          style={{ fontSize: "42px", fontWeight: "bold", color: "#fff", letterSpacing: "-1px" }}
        >
          tmux-ide
        </span>
        <span style={{ fontSize: "16px", color: "#888" }}>Terminal IDE powered by tmux</span>
      </div>
    </div>,
    {
      width: 1200,
      height: 630,
      format: "png",
    },
  );
}
```

## File: `docs/content/docs/agent-teams.mdx`
```
---
title: Agent Teams
description: Coordinate multiple Claude Code instances as a team
---

## Overview

Agent Teams lets you run coordinated Claude Code instances in your tmux-ide layout. One pane acts as the **team lead**, coordinating work and assigning tasks. The others are **teammates** that work independently on their assigned tasks.

tmux-ide handles the tmux layout and enables the Claude Code agent-team environment. You declare the roles in `ide.yml`, launch the layout, then ask Claude inside the lead pane to start or organize the team.

<Callout type="warn">
  Agent teams are experimental in Claude Code and disabled by default. tmux-ide automatically sets
  `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` when your config includes a `team` block.
</Callout>

## Quick Start

The fastest way to get started:

```bash
tmux-ide init --template agent-team
tmux-ide
```

This creates a layout with a lead and two teammate-ready Claude panes in the top row, plus a dev server and shell in the bottom row.

## Configuration

Add a `team` block to your `ide.yml` and annotate your Claude panes:

```yaml
name: my-app

team:
  name: my-app

rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead
        focus: true
      - title: Frontend
        command: claude
        role: teammate
        task: "Work on React components and pages"
      - title: Backend
        command: claude
        role: teammate
        task: "Work on API routes and server logic"

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Shell
```

### `team` fields

| Field              | Required | Description                                     |
| ------------------ | -------- | ----------------------------------------------- |
| `team.name`        | Yes      | Team name to reference in your Claude prompts   |
| `team.model`       | No       | Optional metadata for your own team conventions |
| `team.permissions` | No       | Optional metadata for your own team conventions |

### Pane role fields

| Field  | Description                                                                                                    |
| ------ | -------------------------------------------------------------------------------------------------------------- |
| `role` | `"lead"` or `"teammate"` metadata for your layout, pane labels, and prompts                                    |
| `task` | Suggested task description for a teammate pane. Use it in your prompt when asking Claude to organize the team. |

## How It Works

When you launch a team-enabled config, tmux-ide:

1. Creates the tmux session and all panes as usual
2. Sets `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` on the session
3. Starts the configured Claude panes in the layout you declared
4. Leaves you in a lead-focused workspace that is ready for team setup prompts

From there, ask Claude in the lead pane to start the team and assign the teammate panes practical tasks, for example:

```text
Start an agent team named my-app. Use the Frontend pane for React components and the Backend pane for API routes.
```

Claude Code handles the actual team creation, coordination, and task assignment.

## Enable Teams on Existing Config

Already have an `ide.yml`? Enable teams in one command:

```bash
tmux-ide config enable-team --name "my-team"
```

This finds all `command: claude` panes and assigns roles — the first becomes the lead, the rest become teammates. Those fields act as layout metadata and prompt scaffolding. Then set practical task hints:

```bash
tmux-ide config set rows.0.panes.1.task "Work on frontend components"
tmux-ide config set rows.0.panes.2.task "Work on API routes"
tmux-ide validate --json
```

## Disable Teams

To go back to independent Claude instances:

```bash
tmux-ide config disable-team
```

This removes the `team` config and all `role`/`task` fields.

## Team Lead Self-Configuration

The team lead can reconfigure its own team from within the session. Since the lead is a full Claude Code instance running inside tmux-ide, it can use the CLI to reshape the layout:

```bash
# Add a new teammate
tmux-ide config add-pane --row 0 --title "Reviewer" --command "claude"
tmux-ide config set rows.0.panes.3.role teammate
tmux-ide config set rows.0.panes.3.task "Review code and check for issues"

# Apply changes
tmux-ide validate --json
tmux-ide restart
```

After restart, the new teammate pane appears in the layout. Ask the lead to include it in the team workflow.

## Templates

### Agent Team (default)

Lead + 2 teammates with a generic dev setup.

```bash
tmux-ide init --template agent-team
```

```
┌───────────┬───────────┬───────────┐
│           │           │           │
│   Lead    │Teammate 1 │Teammate 2 │  70%
│           │           │           │
├───────────┴─────┬─────┴───────────┤
│   Dev Server    │     Shell       │  30%
└─────────────────┴─────────────────┘
```

### Agent Team — Next.js

Lead + frontend teammate + backend teammate with Next.js dev server.

```bash
tmux-ide init --template agent-team-nextjs
```

```
┌───────────┬───────────┬───────────┐
│           │           │           │
│   Lead    │ Frontend  │  Backend  │  70%
│           │           │           │
├───────────┴─────┬─────┴───────────┤
│     Next.js     │     Shell       │  30%
└─────────────────┴─────────────────┘
```

### Agent Team — Monorepo

Lead architect + per-app teammates with separate working directories.

```bash
tmux-ide init --template agent-team-monorepo
```

```
┌───────────┬───────────┬───────────┐
│           │ Frontend  │  Backend  │
│   Lead    │  Agent    │   Agent   │  70%
│ Architect │ (apps/web)│(apps/api) │
├─────┬─────┴─────┬─────┴──────────┤
│ Web │    API    │     Shell      │  30%
└─────┴───────────┴────────────────┘
```

## Best Practices

- **One lead, 2-3 teammates** — more teammates increases token cost and coordination overhead
- **Specific tasks** — give teammate panes focused task descriptions so your prompts stay clear
- **Separate files** — assign teammates to different directories or modules to avoid conflicts
- **Lead as coordinator** — the lead should delegate and review, not do implementation
- **Use `restart` to apply changes** — after modifying the team config, `tmux-ide restart` applies the new layout
- **Validate before launch** — always run `tmux-ide validate --json` after config changes

## Comparison with Claude Code Agent Teams

tmux-ide manages the **layout** — it creates the tmux panes, preserves your roles/tasks annotations, and enables the required environment flag. Claude Code manages the **team itself** — creation, coordination, task lists, messaging, and work assignment.

| Aspect                 | tmux-ide handles | Claude Code handles |
| ---------------------- | ---------------- | ------------------- |
| Pane layout and sizing | Yes              | No                  |
| Environment setup      | Yes              | No                  |
| Role/task hints        | Yes              | No                  |
| Team creation          | No               | Yes                 |
| Task coordination      | No               | Yes                 |
| Inter-agent messaging  | No               | Yes                 |
| Shared task list       | No               | Yes                 |

This separation means you get reproducible, declarative layouts from tmux-ide with the coordination intelligence of Claude Code's agent teams.
```

## File: `docs/content/docs/commands.mdx`
```
---
title: Commands
description: CLI commands reference
---

## `tmux-ide`

Launch the IDE from the current directory. Reads `ide.yml` and creates a tmux session.

```bash
tmux-ide
```

You can also point it at a different directory:

```bash
tmux-ide ~/Developer/other-project
```

If a session with the same name already exists, it will reattach to it instead of recreating it. To force a fresh session, run `tmux-ide stop` first.

## `tmux-ide init`

Scaffold a new `ide.yml` in the current directory. Auto-detects your project stack and picks the right template.

```bash
cd ~/Developer/my-project
tmux-ide init
# → Detected next + convex. Created ide.yml for "my-project".
```

Force a specific template:

```bash
tmux-ide init --template nextjs
```

Available templates: `default`, `nextjs`, `convex`, `vite`, `python`, `go`, `agent-team`, `agent-team-nextjs`, `agent-team-monorepo`

Will refuse to overwrite an existing `ide.yml`.

## `tmux-ide stop`

Kill the tmux session for the current project.

```bash
tmux-ide stop
```

Reads the session name from `ide.yml`. If no config is found, uses the directory name as the session name.

## `tmux-ide restart`

Stop the current session and immediately relaunch it. Equivalent to running `tmux-ide stop` followed by `tmux-ide`.

```bash
tmux-ide restart
```

Useful when you've changed your `ide.yml` and want to apply the new layout.

## `tmux-ide attach`

Reattach to a running tmux-ide session.

```bash
tmux-ide attach
```

If the session isn't running, it will suggest starting it with `tmux-ide`.

## `tmux-ide ls`

List all running tmux sessions.

```bash
tmux-ide ls
```

Shows session name, creation time, and whether it's currently attached.

## `tmux-ide doctor`

Check that your system meets all requirements.

```bash
tmux-ide doctor
```

Checks:

- tmux installed
- tmux version ≥ 3.0
- Node.js ≥ 18
- 256-color terminal
- `ide.yml` exists in current directory

## `tmux-ide status`

Show the status of the current IDE session.

```bash
tmux-ide status
tmux-ide status --json
```

Returns session name, running state, config existence, and pane details.

## `tmux-ide inspect`

Show the effective project config and current runtime state in one place.

```bash
tmux-ide inspect
tmux-ide inspect --json
```

Returns:

- resolved config path and session name
- validation status and errors
- row and pane counts
- focus target
- team and theme config
- live tmux pane state when the session is running

## `tmux-ide validate`

Validate your `ide.yml` config file.

```bash
tmux-ide validate
tmux-ide validate --json
```

Checks structure and types: config is an object, `rows` is a non-empty array, each row has panes, all pane fields have correct types (`title`/`command`/`dir` are strings, `focus` is boolean, `env` is an object with string/number values), `theme` fields are strings, and sizes require a `%` suffix with values between 1–100%.

## `tmux-ide detect`

Analyze the current project and suggest an `ide.yml` config.

```bash
tmux-ide detect            # show what was detected
tmux-ide detect --json     # structured output
tmux-ide detect --write    # write suggested config to ide.yml
```

Detects: package manager (npm/pnpm/yarn/bun), frameworks (Next.js, Vite, Convex, Remix, Nuxt, FastAPI, Django, Flask, Go, Rust), and dev commands.

`detect` also explains why it reached those conclusions. Human output includes a `Reasoning:` section, and JSON output includes a `reasons` array under `detected`.

## `tmux-ide config`

Read and modify your `ide.yml` programmatically.

### Dump config

```bash
tmux-ide config            # print config
tmux-ide config --json     # as JSON
```

### Set a value

```bash
tmux-ide config set name "my-app"
tmux-ide config set rows.0.size "70%"
tmux-ide config set rows.1.panes.0.command "npm run dev"
```

### Add a pane

```bash
tmux-ide config add-pane --row 1 --title "Tests" --command "pnpm test"
```

### Remove a pane

```bash
tmux-ide config remove-pane --row 1 --pane 2
```

### Add a row

```bash
tmux-ide config add-row --size "30%"
```

### Enable agent teams

```bash
tmux-ide config enable-team --name "my-team"
```

Finds all `command: claude` panes and assigns the first as `lead`, the rest as `teammate`. Adds a `team` block to the config. See [Agent Teams](/docs/agent-teams) for details.

### Disable agent teams

```bash
tmux-ide config disable-team
```

Removes the `team` config and all `role`/`task` fields from panes.

## Global Flags

| Flag                | Description                              |
| ------------------- | ---------------------------------------- |
| `--json`            | Output as structured JSON (all commands) |
| `--template <name>` | Use a specific template for `init`       |
| `--write`           | Write detected config for `detect`       |
```

## File: `docs/content/docs/configuration.mdx`
```
---
title: Configuration
description: The ide.yml config file reference
---

## Overview

tmux-ide is configured with an `ide.yml` file in your project root. It defines the session name, layout rows, panes, and optional theming.

## Full Example

```yaml
name: my-app

before: pnpm install

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
        size: 40%
      - title: Claude 2 — review
        command: claude
      - title: Claude 3 — explore
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
        dir: apps/web
        env:
          PORT: 3000
      - title: Convex
        command: npx convex dev
      - title: Shell
        focus: true

theme:
  accent: colour75
  border: colour238
  bg: colour235
  fg: colour248
```

## Fields

### `name`

The tmux session name. Used to identify the session for `tmux attach` and `tmux-ide stop`.

```yaml
name: my-app
```

### `before`

Optional shell command to run before creating the tmux session. Useful for installing dependencies or running setup scripts.

```yaml
before: pnpm install
```

### `rows`

An array of horizontal rows. Each row contains panes that are split side-by-side within it.

```yaml
rows:
  - size: 70% # this row gets 70% of screen height
    panes: [...]
  - panes: [...] # remaining 30%
```

#### `rows[].size`

Optional. The percentage of screen height this row should occupy. If omitted, remaining space is divided evenly among rows without a `size`.

#### `rows[].panes`

An array of panes within the row. Panes are split horizontally (side-by-side).

### Pane Options

```yaml
panes:
  - title: My Pane
    command: pnpm dev
    size: 60%
    dir: apps/web
    focus: true
    env:
      PORT: 3000
      NODE_ENV: development
```

| Field     | Required | Description                                                                             |
| --------- | -------- | --------------------------------------------------------------------------------------- |
| `title`   | No       | Label displayed in the pane border                                                      |
| `command` | No       | Shell command to execute when the pane opens. If omitted, you get an interactive shell. |
| `size`    | No       | Width percentage within its row. If omitted, panes share equal width.                   |
| `dir`     | No       | Working directory for this pane, relative to the project root.                          |
| `focus`   | No       | Set to `true` to give this pane initial focus when the session starts.                  |
| `env`     | No       | Key-value pairs of environment variables to set before running the command.             |

### `team`

Optional. Enables [Agent Teams](/docs/agent-teams) — coordinated Claude Code instances with a lead and teammates.

```yaml
team:
  name: my-team
```

| Field              | Required | Description                                     |
| ------------------ | -------- | ----------------------------------------------- |
| `team.name`        | Yes      | Team name to reference in Claude prompts        |
| `team.model`       | No       | Optional metadata for your own team conventions |
| `team.permissions` | No       | Optional metadata for your own team conventions |

When `team` is set, tmux-ide enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` for the tmux session. See [Agent Teams](/docs/agent-teams) for the recommended lead/teammate pane pattern.

### Pane Team Fields

When using agent teams, panes can have additional fields:

| Field  | Description                                                          |
| ------ | -------------------------------------------------------------------- |
| `role` | `"lead"` or `"teammate"` metadata for pane labels and Claude prompts |
| `task` | Suggested task description for a teammate pane                       |

```yaml
panes:
  - title: Lead
    command: claude
    role: lead
  - title: Frontend
    command: claude
    role: teammate
    task: "Work on React components"
```

### `theme`

Optional color overrides for the tmux styling.

```yaml
theme:
  accent: colour75 # Active pane border + status bar accent
  border: colour238 # Inactive pane border
  bg: colour235 # Status bar background
  fg: colour248 # Status bar text
```

Colors use tmux color names: `colour0`–`colour255`, or standard names like `red`, `green`, `blue`.

## Layout Logic

The layout is built as a grid:

1. **Rows** stack vertically — the first row is at the top
2. **Panes** within a row split horizontally — evenly distributed by default
3. The first row with `size: 70%` takes 70% of the terminal height
4. Rows without a `size` share the remaining space equally
5. Panes with `size` set control their width within the row
6. The pane with `focus: true` gets initial focus (defaults to pane 0)

```
Row 1 (size: 70%):  [ Pane A | Pane B | Pane C ]
Row 2 (remaining):  [ Pane D | Pane E ]
```
```

## File: `docs/content/docs/contributing.mdx`
```
---
title: Contributing
description: Development workflow, release checks, and open source project conventions
---

## Local Setup

Requirements:

- Node.js 18 or newer
- pnpm 10 or newer
- tmux 3.0 or newer for manual session smoke tests

Install dependencies from the repo root:

```bash
pnpm install --frozen-lockfile
```

## Main Commands

Run these from the repository root:

```bash
pnpm test
pnpm typecheck
pnpm build
pnpm docs:build
pnpm pack:check
pnpm check
```

What they do:

- `pnpm test` runs the Node CLI test suite (uses `--experimental-strip-types` on `.ts` files)
- `pnpm typecheck` runs `tsc --noEmit` to verify types without emitting output
- `pnpm build` compiles TypeScript to `dist/` via `tsc`
- `pnpm docs:build` validates the docs site production build
- `pnpm pack:check` verifies the published npm package can be packed cleanly
- `pnpm check` runs the full default pre-push and pre-release check path

`npm publish` is guarded by `prepublishOnly`, so publishing runs `pnpm check` automatically before npm actually publishes the package.

## Integration and Manual Smoke Tests

If tmux is available locally, also run:

```bash
pnpm test:integration
```

Recommended manual smoke test:

```bash
node bin/cli.js init
node bin/cli.js inspect --json
node bin/cli.js
```

Then in a second shell:

```bash
node bin/cli.js status --json
node bin/cli.js stop --json
```

## CI

GitHub Actions validates:

- the CLI test suite on Node 18, 20, and 22
- the docs production build
- package packing with `npm pack --dry-run`

That keeps the release path close to the local `pnpm check` workflow while still exercising multiple Node versions in CI.

## Release Workflow

Before publishing a release:

1. Update `CHANGELOG.md` under `Unreleased`.
2. Confirm the version in `package.json`.
3. Run `pnpm check`.
4. Run `pnpm test:integration` if tmux is available.
5. Do the manual smoke test if the release includes CLI behavior changes.
6. Move `Unreleased` notes into the final version entry.
7. Tag and publish the release.

The repository root also includes:

- `CONTRIBUTING.md` for contributor setup
- `RELEASE.md` for the release checklist
- `CHANGELOG.md` for release notes
- `SECURITY.md` for vulnerability reporting

## Pull Request Expectations

- Keep CLI behavior changes covered by tests.
- Update docs when command behavior or output changes.
- Prefer focused pull requests over mixed refactors.
- Run `pnpm check` before opening or updating a pull request.
```

## File: `docs/content/docs/getting-started.mdx`
```
---
title: Getting Started
description: Set up tmux-ide in your project in under a minute
---

## Prerequisites

- [tmux](https://github.com/tmux/tmux) installed (`brew install tmux` on macOS)
- Node.js 18+

## Install

```bash
npm i -g tmux-ide
```

Or use it directly with `npx` — no install needed:

```bash
npx tmux-ide
```

## Create your first workspace

Navigate to your project and scaffold a config:

```bash
cd ~/Developer/my-project
tmux-ide init
```

This creates an `ide.yml` in your project root:

```yaml
name: my-project

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Dev Server
      - title: Shell
```

## Launch

```bash
tmux-ide
```

That's it. You'll get a tmux session with labeled panes, split exactly as configured.

## Stop

Detach with `Ctrl-b d` to leave it running in the background, or kill it:

```bash
tmux-ide stop
```

## Restart

If you've changed your `ide.yml`, restart to apply the new layout:

```bash
tmux-ide restart
```

## Reconnect

If you detach or close your terminal, just run `tmux-ide` again — it will reattach to the existing session:

```bash
tmux-ide
```

Or use tmux directly:

```bash
tmux attach -t my-project
```

## Claude Code Skill

tmux-ide ships with a built-in [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill. When you install tmux-ide, the skill is automatically registered so Claude Code knows how to configure and manage your workspace.

**What the skill enables:**

- Ask Claude to "set up a tmux IDE" and it will auto-detect your stack, present layout options with ASCII diagrams, and write the config for you
- Ask Claude to "add a pane" or "prepare an agent-team layout" and it will use the programmatic CLI to modify your `ide.yml`
- The team lead agent can self-configure — spawning new teammates, assigning tasks, and restarting the layout

**How it works:**

If Claude Code is already set up on the machine, the global install hook copies `SKILL.md` into `~/.claude/skills/tmux-ide/` and sets `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in `~/.claude/settings.json`. That keeps the npm install side effects limited to existing Claude Code setups.

If you installed via `npx` (without a global install), you can manually register the skill:

```bash
mkdir -p ~/.claude/skills/tmux-ide
cp "$(npm root -g)/tmux-ide/skill/SKILL.md" ~/.claude/skills/tmux-ide/
```

If Claude Code is not installed yet, create `~/.claude/` first or complete Claude Code setup before using the automatic registration path.

And if you want agent teams enabled for Claude Code outside tmux-ide-launched sessions, add this to `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Once installed, just ask Claude Code something like:

> "Set up a tmux IDE for this project"

and it will handle the rest.
```

## File: `docs/content/docs/index.mdx`
```
---
title: tmux-ide
description: Turn any project into a tmux-powered terminal IDE
---

# tmux-ide

Turn any project into a tmux-powered terminal IDE with a simple `ide.yml` config file.

```
┌───────────────┬───────────────┬───────────────┐
│               │               │               │
│   Claude 1    │   Claude 2    │   Claude 3    │
│               │               │               │
│               │               │               │
├───────┬───────┴───────────────┴───────────────┤
│       │                                       │
│ Dev   │              Shell                    │
│ Server│                                       │
└───────┴───────────────────────────────────────┘
```

Define your workspace layout in an `ide.yml` file, run `tmux-ide`, and get a fully configured tmux session with labeled panes, dev servers running, and Claude instances ready to go.

## Quick Start

```bash
# Install globally
npm i -g tmux-ide

# Or run directly
npx tmux-ide init    # scaffold an ide.yml
npx tmux-ide         # launch the IDE
npx tmux-ide restart # restart with new config
```

<Cards>
  <Card title="What's New in 1.3.0" href="/docs/release-1-3-0" />
  <Card title="Getting Started" href="/docs/getting-started" />
  <Card title="Configuration" href="/docs/configuration" />
  <Card title="Templates" href="/docs/templates" />
  <Card title="Agent Teams" href="/docs/agent-teams" />
  <Card title="Contributing" href="/docs/contributing" />
</Cards>
```

## File: `docs/content/docs/meta.json`
```json
{
  "title": "Docs",
  "pages": [
    "index",
    "release-1-3-0",
    "release-1-2-0",
    "release-1-1-0",
    "getting-started",
    "configuration",
    "commands",
    "programmatic",
    "templates",
    "agent-teams",
    "contributing",
    "tips"
  ]
}
```

## File: `docs/content/docs/programmatic.mdx`
```
---
title: Programmatic CLI
description: Using tmux-ide from Claude Code and scripts
---

## Overview

tmux-ide provides a programmatic CLI designed for automation and Claude Code integration. Every command supports `--json` for structured output, and mutation commands let you build and modify configs without editing YAML directly.

## JSON Output

Add `--json` to any command for structured output:

```bash
tmux-ide status --json
tmux-ide inspect --json
tmux-ide validate --json
tmux-ide detect --json
tmux-ide config --json
tmux-ide ls --json
tmux-ide doctor --json
```

## Config Mutations

### Set a value by dot path

```bash
tmux-ide config set name "my-app"
tmux-ide config set rows.0.size "70%"
tmux-ide config set rows.1.panes.0.command "npm run dev"
tmux-ide config set rows.0.panes.1.title "Claude 2 — review"
```

### Add a pane

```bash
tmux-ide config add-pane --row 1 --title "Tests" --command "pnpm test"
tmux-ide config add-pane --row 0 --title "Claude 3" --command "claude"
```

### Remove a pane

```bash
tmux-ide config remove-pane --row 1 --pane 2
```

### Add a row

```bash
tmux-ide config add-row --size "30%"
```

## Claude Code Integration

### Setup workflow

The recommended flow for setting up tmux-ide in a new project:

1. **Detect the project stack:**

   ```bash
   tmux-ide detect --json
   ```

   Use the returned `detected.reasons` array to explain the recommendation before writing config.

2. **Present layout options with ASCII diagrams.** Before writing any config, show the user 2-3 layout options visually so they can pick or tweak:

   **Option A — Dual Claude + Dev**

   ```
   ┌─────────────────┬─────────────────┐
   │                 │                 │
   │    Claude 1     │    Claude 2     │  70%
   │                 │                 │
   ├────────┬────────┴────────┬────────┤
   │Dev Srv │  Tests  │ Shell │        │  30%
   └────────┴─────────┴───────┘────────┘
   ```

   **Option B — Triple Claude**

   ```
   ┌───────────┬───────────┬───────────┐
   │           │           │           │
   │ Claude 1  │ Claude 2  │ Claude 3  │  70%
   │           │           │           │
   ├───────────┴─────┬─────┴───────────┤
   │    Dev Server    │     Shell       │  30%
   └─────────────────┴─────────────────┘
   ```

   Adapt pane names and commands to the detected stack (e.g., `pnpm dev`, `cargo watch`, `go run`).

3. **Write the chosen config:**

   ```bash
   tmux-ide detect --write
   ```

4. **Validate and launch:**
   ```bash
   tmux-ide validate --json
   tmux-ide              # first launch
   tmux-ide restart      # or restart to apply config changes
   ```

### Custom config workflow

Build a config from scratch without touching YAML:

```bash
# Start with detection to get a base
tmux-ide detect --write

# Or build manually
tmux-ide config add-row --size "70%"
tmux-ide config add-pane --row 0 --title "Claude 1" --command "claude"
tmux-ide config add-pane --row 0 --title "Claude 2" --command "claude"
tmux-ide config add-row
tmux-ide config add-pane --row 1 --title "Dev" --command "pnpm dev"
tmux-ide config add-pane --row 1 --title "Shell"
tmux-ide config set name "my-project"
tmux-ide validate --json
```

### Modification workflow

Modify an existing config:

```bash
# 1. Read current state
tmux-ide inspect --json

# 2. Make changes
tmux-ide config set rows.1.panes.0.command "bun dev"
tmux-ide config add-pane --row 1 --title "Tests" --command "bun test"

# 3. Validate
tmux-ide validate --json
```

### Agent Teams workflow

Set up coordinated Claude Code instances:

```bash
# 1. Start with an existing config
tmux-ide config --json

# 2. Enable agent teams
tmux-ide config enable-team --name "my-team"

# 3. Assign tasks to teammates
tmux-ide config set rows.0.panes.1.task "Work on frontend components"
tmux-ide config set rows.0.panes.2.task "Work on API routes"

# 4. Validate and launch
tmux-ide validate --json
tmux-ide
tmux-ide restart      # or restart to apply config changes
```

The team lead can also reconfigure from within its session — see [Agent Teams](/docs/agent-teams#team-lead-self-configuration).

## Best Practices

- **Always use `--json`** for programmatic access — human output may change between versions
- **Prefer `inspect --json`** when you need both config validity and runtime state
- **Always validate after mutations** — `tmux-ide validate --json` catches errors before launch
- **Top row ~70%** for Claude panes — gives editors enough space
- **2-3 Claude panes** in the top row for parallel work (feature, review, explore)
- **Dev servers + shell** in the bottom row
- **Use `detect --json` first** to understand the project stack before suggesting a config
```

## File: `docs/content/docs/release-1-1-0.mdx`
```
---
title: Version 1.1.0
description: Release notes for tmux-ide 1.1.0
---

# tmux-ide 1.1.0

Version `1.1.0` tightens the CLI, makes install behavior safer, improves the maintainer workflow, and strengthens the runtime path that actually launches and manages tmux sessions.

## Highlights

### Safer, more predictable CLI behavior

- Hardened command parsing and error handling across the CLI
- Added clearer structured `--json` failures for more command paths
- Improved `inspect` so it reports invalid config state instead of crashing
- Tightened config mutation edge cases and invalid-input handling

### Safer postinstall behavior

- Reduced Claude integration side effects during install
- Limited postinstall changes to safer, more intentional cases
- Kept agent-team setup documented while making the install path less invasive

### Better launch and tmux runtime behavior

- Reduced raw tmux process handling by moving more logic behind shared helpers
- Improved launch orchestration and startup planning
- Corrected agent-team startup behavior and sequencing
- Added better non-interactive launch and restart coverage for tmux-backed flows

### Stronger quality gates

- Added repository lint and formatting checks
- Enforced release checks before publish
- Improved package contents so the published tarball stays focused on runtime files
- Strengthened test coverage for CLI regressions, runtime helpers, and tmux lifecycle behavior

### Better maintainer and contributor workflow

- Expanded contributor and release guidance
- Improved docs coverage for new commands and maintainer workflows
- Added clearer architecture and project-quality documentation
- Tightened CI to better reflect the real release path

## What Changed

This release focused on quality and correctness more than feature sprawl:

- CLI hardening and error-boundary cleanup
- postinstall safety improvements
- docs, contributing, and release polish
- lint and format gates
- packaging cleanup
- agent-team behavior correction
- launch/runtime refactoring
- broader integration coverage around tmux-driven flows

## Recommended Upgrade Check

If you are upgrading and want a quick confidence pass:

```bash
tmux-ide inspect --json
tmux-ide validate --json
tmux-ide doctor --json
```

For contributors and maintainers, `pnpm check` is the main pre-release verification path.
```

## File: `docs/content/docs/release-1-2-0.mdx`
```
---
title: Version 1.2.0
description: Release notes for tmux-ide 1.2.0 — real IDE terminal experience
---

# tmux-ide 1.2.0

Version `1.2.0` transforms tmux-ide sessions from basic pane layouts into a real terminal IDE experience — with mouse support, live process indicators, a two-line clickable status bar, and a cleaner internal architecture.

## Highlights

### Mouse support

Sessions now enable `mouse on` by default. Click to focus panes, scroll with your trackpad, and drag pane borders to resize — no keyboard gymnastics required.

### Two-line status bar with pane tabs

The status bar gains a second line showing all pane titles as clickable tabs. Click a tab to switch to that pane. The active pane is highlighted in your accent color.

```
Line 0:  MY-PROJECT IDE            ●            14:30 │ Mar 17
Line 1:  Claude 1 │ Claude 2 │ Dev Server │ Shell
         ^^^^^^^^ highlighted = active pane
```

### Live dev server detection

A background monitor detects when a process in any pane starts listening on a TCP port (1024–20000). A green `⏺` dot appears next to that pane's tab — you can tell at a glance whether your dev server is up.

### Agent busy indicator

When Claude or Codex is actively working (spinner visible in the pane title), a pulsing `⏺` dot appears next to the pane tab. When the agent is idle, a dim `●` shows instead. No more switching panes just to check if Claude is still thinking.

### Enhanced pane borders

Pane borders now show the current working directory alongside the title. Active panes use your accent color with a bold `▸` indicator; inactive panes are dimmed with `·`. The `escape-time` is set to `0` for snappy ESC key response.

### Config drift detection

If you edit `ide.yml` while a session is running, `tmux-ide` now detects the change and warns you:

```
Session "my-project" is running but ide.yml has changed.
Run "tmux-ide restart" to apply changes.
```

### `--verbose` debugging

Pass `--verbose` (or set `TMUX_IDE_DEBUG=1`) to log every tmux command to stderr. Makes debugging layout issues transparent instead of blind.

```bash
$ tmux-ide --verbose
  [tmux] has-session -t my-project
  [tmux] new-session -d -P -F #{pane_id} -s my-project ...
  [tmux] set-option -t my-project mouse on
  ...
```

## Architecture improvements

### Unified session monitor (pure JS)

The port watcher and agent status detection — previously two separate shell scripts — are now a single Node.js daemon (`session-monitor.js`). One language, one poll loop, testable with `node --test`. The tmux status format string is now purely declarative — it reads variables, no more `#()` shell calls.

### Composable session options

`buildThemeOptions()` (a growing kitchen-sink function) was split into five composable builders in `session-options.js`: `themeOptions`, `borderOptions`, `behaviorOptions`, `statusBarOptions`, and `keyBindings`. Each is independently testable and returns an array of tmux commands.

### Unified error hierarchy

Three inconsistent error patterns were consolidated into a single hierarchy: `IdeError` → `ConfigError` / `TmuxError` / `SessionError`. No more silent fallbacks. `getSessionName()` now returns `{ name, source }` so callers know whether the name came from config or a fallback.

### Dead code cleanup

Removed unused exports (`output()`), always-null returns (`leadPane`), empty arrays (`teammateCommands`), and unused parameters (`_team`). Cleaner foundation for future features.

## What Changed

- Mouse support enabled by default
- Two-line status bar with clickable pane tabs
- Live port detection via background JS monitor
- Agent busy/idle indicators in status bar
- Enhanced pane borders showing working directory
- Config drift detection with user warning
- `--verbose` flag for tmux command tracing
- Shell scripts replaced with unified JS daemon
- Session options split into composable builders
- Unified `IdeError` hierarchy across all modules
- Dead code and unused stubs removed
- 134 tests (up from 112)

## Recommended Upgrade Check

```bash
npm install -g tmux-ide@latest
tmux-ide doctor --json
tmux-ide validate --json
tmux-ide restart          # to pick up the new status bar and indicators
```

For contributors: `pnpm check` remains the main pre-release gate.
```

## File: `docs/content/docs/release-1-3-0.mdx`
```
---
title: Version 1.3.0
description: Release notes for tmux-ide 1.3.0 — TypeScript migration and validation hardening
---

# tmux-ide 1.3.0

Version `1.3.0` migrates the entire codebase to TypeScript and strengthens config validation, backed by 225 tests across unit, integration, and CLI contract suites.

## TypeScript Migration

Every source file in `src/` is now TypeScript. The published package still ships compiled JavaScript via `tsc`, so nothing changes for users — but contributors get strict types, better IDE support, and catch-at-compile-time guarantees.

Key interfaces like `IdeConfig`, `Row`, `Pane`, `ThemeConfig`, `PaneAction`, and `SessionState` are defined in `src/types.ts` and used throughout the codebase.

The build pipeline:

- **Dev**: `node --experimental-strip-types` runs `.ts` files directly — no build step needed during development
- **Build**: `tsc` emits strict JavaScript to `dist/`
- **Publish**: `bin/cli.js` imports from `dist/`, so the published package works on Node 18+ without TypeScript

## Validation Hardening

The config validator now catches more edge cases:

- **Leading zeros rejected**: sizes like `00%` and `007%` are no longer accepted
- **Row size sum check**: row sizes that exceed 100% total produce a clear error
- **Pane size sum check**: pane sizes within a single row that exceed 100% are rejected
- **Multiple focus check**: only one pane per row can have `focus: true`

## Config Refactor

Internal config mutation code was deduplicated. The repeated read-validate-mutate-write pattern (7 copies) was extracted into `withConfig()` and `readConfigSafe()` helpers. `readConfig()` is now called in exactly one place.

## Test Coverage

The test suite grew to 225 tests covering:

- All CLI commands (structured JSON and human output)
- Config mutations (set, add-pane, remove-pane, add-row, enable-team, disable-team)
- Validation edge cases (sizes, focus, sums)
- tmux session lifecycle (launch, restart, stop, attach, inspect)
- Agent team layouts and role assignment
- Doctor checks, detect/init flows, and postinstall behavior
```

## File: `docs/content/docs/templates.mdx`
```
---
title: Templates
description: Pre-built ide.yml configs for common stacks
---

tmux-ide ships with templates for common setups. Copy these into your project as `ide.yml` and adjust to your needs.

## Default

A minimal setup with two Claude panels and a shell.

```yaml
name: my-project

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Dev Server
      - title: Shell
```

## Next.js

Three Claude panels with a Next.js dev server.

```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude
      - title: Claude 3 — explore
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Shell
```

## Next.js + Convex

Full-stack setup with Next.js frontend and Convex backend.

```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude
      - title: Claude 3 — explore
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Convex
        command: npx convex dev
      - title: Shell
```

## Vite

Two Claude panels with a Vite dev server.

```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Vite
        command: pnpm dev
      - title: Shell
        focus: true
```

## Go

Two Claude panels with a Go server.

```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Go
        command: go run .
      - title: Shell
        focus: true
```

## Agent Team

A lead-focused layout with two teammate-ready Claude panes. See [Agent Teams](/docs/agent-teams) for details.

```yaml
name: my-project

team:
  name: my-project

rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead
        focus: true
      - title: Teammate 1
        command: claude
        role: teammate
      - title: Teammate 2
        command: claude
        role: teammate

  - panes:
      - title: Dev Server
      - title: Shell
```

## Agent Team — Monorepo

Specialized teammate-ready panes with per-app working directories.

```yaml
name: my-monorepo

team:
  name: my-monorepo

rows:
  - size: 70%
    panes:
      - title: Lead — Architect
        command: claude
        role: lead
        focus: true
      - title: Frontend Agent
        command: claude
        role: teammate
        task: "Work on the frontend application"
        dir: apps/web
      - title: Backend Agent
        command: claude
        role: teammate
        task: "Work on the backend services"
        dir: apps/api

  - panes:
      - title: Frontend
        command: pnpm dev
        dir: apps/web
      - title: Backend
        command: pnpm dev
        dir: apps/api
      - title: Shell
```

## Custom Examples

### Python / FastAPI

```yaml
name: my-api

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: FastAPI
        command: uvicorn main:app --reload
      - title: Shell
```

### Monorepo

```yaml
name: my-monorepo

rows:
  - size: 60%
    panes:
      - title: Claude — frontend
        command: claude
      - title: Claude — backend
        command: claude

  - size: 40%
    panes:
      - title: Frontend
        command: cd apps/web && pnpm dev
      - title: Backend
        command: cd apps/api && pnpm dev
      - title: Shell
```
```

## File: `docs/content/docs/tips.mdx`
```
---
title: Tips & Tricks
description: Get the most out of your tmux IDE
---

## Navigation

| Shortcut         | Action                                    |
| ---------------- | ----------------------------------------- |
| `Ctrl-b ←/→/↑/↓` | Move between panes                        |
| `Ctrl-b z`       | Zoom current pane (fullscreen toggle)     |
| `Ctrl-b q`       | Flash pane numbers, press number to jump  |
| `Ctrl-b d`       | Detach session (keeps everything running) |

## Scrolling

Enter scroll mode with `Ctrl-b [`, then use arrow keys or Page Up/Down. Press `q` to exit.

Or enable mouse support in `~/.tmux.conf`:

```bash
set -g mouse on
```

This lets you scroll with your trackpad and click to switch panes.

## Faster Pane Switching

Add to `~/.tmux.conf` for prefix-free navigation with Option+arrow:

```bash
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D
```

Reload with `tmux source-file ~/.tmux.conf`.

## macOS: Fix Arrow Key Conflicts

macOS uses `Ctrl+←/→` for switching desktops, which conflicts with tmux.

Go to **System Settings > Desktop & Dock > Mission Control** and disable:

- Move left a space (`^←`)
- Move right a space (`^→`)

Or use the Option+arrow bindings above to avoid the conflict entirely.

## Reconnecting

If you close your terminal or detach, your session is still running:

```bash
# List all sessions
tmux ls

# Reattach
tmux attach -t my-project
```

## Resizing Panes

Drag pane borders with the mouse (if `set -g mouse on` is enabled), or:

```bash
# From inside tmux:
Ctrl-b : resize-pane -D 10   # down
Ctrl-b : resize-pane -U 10   # up
Ctrl-b : resize-pane -L 10   # left
Ctrl-b : resize-pane -R 10   # right
```

## Recommended `~/.tmux.conf`

A minimal config that works well with tmux-ide:

```bash
# Mouse support
set -g mouse on

# Option+arrow pane switching (no prefix needed)
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D

# Start window numbering at 1
set -g base-index 1
setw -g pane-base-index 1

# Increase scrollback
set -g history-limit 10000
```
```

## File: `docs/lib/cn.ts`
```typescript
export { twMerge as cn } from "tailwind-merge";
```

## File: `docs/lib/layout.shared.tsx`
```tsx
import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";

export const gitConfig = {
  user: "wavyrai",
  repo: "tmux-ide",
  branch: "main",
};

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: <span className="font-pixel text-lg">tmux-ide</span>,
    },
    githubUrl: `https://github.com/${gitConfig.user}/${gitConfig.repo}`,
  };
}
```

## File: `docs/lib/source.ts`
```typescript
import { docs } from "fumadocs-mdx:collections/server";
import { type InferPageType, loader } from "fumadocs-core/source";
import { lucideIconsPlugin } from "fumadocs-core/source/lucide-icons";

// See https://fumadocs.dev/docs/headless/source-api for more info
export const source = loader({
  baseUrl: "/docs",
  source: docs.toFumadocsSource(),
  plugins: [lucideIconsPlugin()],
});

export function getPageImage(page: InferPageType<typeof source>) {
  const segments = [...page.slugs, "image.webp"];

  return {
    segments,
    url: `/og/docs/${segments.join("/")}`,
  };
}

export async function getLLMText(page: InferPageType<typeof source>) {
  const processed = await page.data.getText("processed");

  return `# ${page.data.title}

${processed}`;
}
```

## File: `docs/public/install.sh`
```bash
#!/bin/sh
# tmux-ide installer
# Usage: curl -fsSL https://tmux.thijsverreck.com/install.sh | sh
set -e

BOLD='\033[1m'
DIM='\033[2m'
GREEN='\033[32m'
RED='\033[31m'
RESET='\033[0m'

info() { printf "${BOLD}%s${RESET}\n" "$1"; }
success() { printf "${GREEN}${BOLD}%s${RESET}\n" "$1"; }
error() { printf "${RED}${BOLD}error:${RESET} %s\n" "$1" >&2; exit 1; }

# Check for tmux
if ! command -v tmux >/dev/null 2>&1; then
  error "tmux is not installed. Install it first: https://github.com/tmux/tmux/wiki/Installing"
fi

# Check for Node.js
if ! command -v node >/dev/null 2>&1; then
  error "Node.js is not installed. Install it first: https://nodejs.org"
fi

NODE_VERSION=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
  error "Node.js 18+ is required (found v${NODE_VERSION})"
fi

# Detect package manager
if command -v pnpm >/dev/null 2>&1; then
  PM="pnpm"
elif command -v bun >/dev/null 2>&1; then
  PM="bun"
elif command -v yarn >/dev/null 2>&1; then
  PM="yarn"
else
  PM="npm"
fi

info "Installing tmux-ide..."

case "$PM" in
  npm)  npm install -g tmux-ide ;;
  pnpm) pnpm add -g tmux-ide ;;
  yarn) yarn global add tmux-ide ;;
  bun)  bun add -g tmux-ide ;;
esac

if command -v tmux-ide >/dev/null 2>&1; then
  # Install Claude Code skill (if Claude Code is present)
  if [ -d "$HOME/.claude" ]; then
    mkdir -p "$HOME/.claude/skills/tmux-ide"
    SKILL_SRC="$(npm root -g)/tmux-ide/skill/SKILL.md"
    if [ -f "$SKILL_SRC" ]; then
      cp "$SKILL_SRC" "$HOME/.claude/skills/tmux-ide/SKILL.md"
    fi
  fi

  echo ""
  success "tmux-ide installed successfully!"
  echo ""
  printf "${DIM}Get started:${RESET}\n"
  echo "  cd your-project"
  echo "  tmux-ide init     # scaffold ide.yml"
  echo "  tmux-ide          # launch"
  echo ""
else
  error "Installation failed. Try: npm install -g tmux-ide"
fi
```

## File: `scripts/postinstall.js`
```javascript
import { existsSync, mkdirSync, copyFileSync, readFileSync, writeFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { homedir } from "node:os";

const claudeDir = resolve(homedir(), ".claude");
if (!shouldInstallClaudeIntegration() || !existsSync(claudeDir)) {
  process.exit(0);
}

const skillDir = resolve(claudeDir, "skills", "tmux-ide");
mkdirSync(skillDir, { recursive: true });
const src = resolve(dirname(import.meta.dirname), "skill", "SKILL.md");
if (existsSync(src)) {
  copyFileSync(src, resolve(skillDir, "SKILL.md"));
}

const settingsPath = resolve(claudeDir, "settings.json");
let settings = {};

if (existsSync(settingsPath)) {
  try {
    settings = JSON.parse(readFileSync(settingsPath, "utf-8"));
  } catch (error) {
    console.warn(
      `[tmux-ide] Skipping Claude settings update: could not parse ${settingsPath}: ${error.message}`,
    );
    process.exit(0);
  }
}

if (settings == null || typeof settings !== "object" || Array.isArray(settings)) {
  console.warn(
    `[tmux-ide] Skipping Claude settings update: ${settingsPath} does not contain a JSON object.`,
  );
  process.exit(0);
}

const nextSettings = {
  ...settings,
  env: {
    ...(settings.env && typeof settings.env === "object" && !Array.isArray(settings.env)
      ? settings.env
      : {}),
    CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: "1",
  },
};

writeFileSync(settingsPath, `${JSON.stringify(nextSettings, null, 2)}\n`);

function shouldInstallClaudeIntegration() {
  return process.env.npm_config_global === "true";
}
```

## File: `skill/SKILL.md`
```markdown
# tmux-ide — Claude Code Skill

tmux-ide turns any project into a tmux-powered terminal IDE using a simple `ide.yml` config file.

## When to use

- User mentions multi-pane, tmux, terminal IDE, or dev environment
- User wants to set up a development workspace
- User asks about running multiple terminals/tools side-by-side
- User wants to coordinate multiple Claude Code instances as a team
- User mentions agent teams, team lead, or multi-agent workflows

## Setup workflow

1. Check if `ide.yml` exists: `tmux-ide status --json`
2. Auto-detect the project: `tmux-ide detect --json`
3. **Present 2-3 layout options using ASCII diagrams** before writing config. Example:

   **Option A — Dual Claude + Dev (recommended)**

   ```
   ┌─────────────────┬─────────────────┐
   │                 │                 │
   │    Claude 1     │    Claude 2     │  70%
   │                 │                 │
   ├────────┬────────┴────────┬────────┤
   │Dev Srv │  Tests  │ Shell │        │  30%
   └────────┴─────────┴───────┘────────┘
   ```

   **Option B — Triple Claude**

   ```
   ┌───────────┬───────────┬───────────┐
   │           │           │           │
   │ Claude 1  │ Claude 2  │ Claude 3  │  70%
   │           │           │           │
   ├───────────┴─────┬─────┴───────────┤
   │    Dev Server    │     Shell       │  30%
   └─────────────────┴─────────────────┘
   ```

   **Option C — Single Claude + wide dev**

   ```
   ┌─────────────────────────────────────┐
   │             Claude                  │  60%
   ├──────────┬──────────┬──────────────┤
   │ Dev Srv  │  Tests   │    Shell     │  40%
   └──────────┴──────────┴──────────────┘
   ```

   Adapt pane names/commands to the detected stack.

4. Once the user picks, write the config:
   - Quick: `tmux-ide detect --write` then modify
   - Or build custom with `tmux-ide config` subcommands

## Agent Teams workflow

Agent teams coordinate multiple Claude Code instances where a lead delegates tasks to teammates. Each gets its own tmux pane, and tmux-ide prepares that layout before Claude starts the actual team workflow.

### When to suggest agent teams

- User wants coordinated multi-agent development
- User mentions team lead, teammates, or task delegation
- User wants parallel work with inter-agent communication
- User's task benefits from specialized roles (e.g., frontend + backend + review)

### Prerequisites

Agent teams require `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. The tmux-ide install hook enables this in Claude Code settings, and tmux-ide also sets it automatically inside tmux sessions when `team` is configured in `ide.yml`.

### Setup from scratch

1. **Scaffold with agent team template:**

   ```bash
   tmux-ide init --template agent-team
   ```

2. **Or enable teams on an existing config:**

   ```bash
   tmux-ide config enable-team --name "my-team"
   ```

   This finds all `command: claude` panes and assigns the first as `lead`, the rest as `teammate`.

3. **Assign initial task hints to teammate panes:**

   ```bash
   tmux-ide config set rows.0.panes.1.task "Work on frontend components"
   tmux-ide config set rows.0.panes.2.task "Work on API routes"
   ```

4. **Validate and launch the layout:**

   ```bash
   tmux-ide validate --json
   tmux-ide
   ```

5. **Inside the lead pane, ask Claude to form the team:**

   ```text
   Start an agent team named my-team. Use the Frontend pane for components and the Backend pane for API routes.
   ```

### Present team layout options

When suggesting agent team layouts, show the roles and note that Claude will create the team after launch:

**Option A — Lead + 2 Teammates**

```
┌───────────┬───────────┬───────────┐
│           │           │           │
│   Lead    │Teammate 1 │Teammate 2 │  70%
│ (claude)  │ (claude)  │ (claude)  │
├───────────┴─────┬─────┴───────────┤
│   Dev Server    │     Shell       │  30%
└─────────────────┴─────────────────┘
```

**Option B — Lead + 3 Specialized Teammates**

```
┌────────┬────────┬────────┬────────┐
│        │Frontend│Backend │ Review │
│  Lead  │ Agent  │ Agent  │ Agent  │  70%
│        │        │        │        │
├────────┴────────┴──┬─────┴────────┤
│    Dev Server      │    Shell     │  30%
└────────────────────┴──────────────┘
```

### Team lead self-configuration

When running as the team lead inside a tmux-ide session, you can reconfigure the layout for the team:

```bash
# Read current config
tmux-ide config --json

# Add a new teammate pane
tmux-ide config add-pane --row 0 --title "Reviewer" --command "claude"
tmux-ide config set rows.0.panes.3.role teammate
tmux-ide config set rows.0.panes.3.task "Review all PRs and check for issues"

# Or remove a teammate
tmux-ide config remove-pane --row 0 --pane 2

# Validate and restart to apply
tmux-ide validate --json
tmux-ide restart
```

### Disable teams

```bash
tmux-ide config disable-team
```

Removes the `team` config and all `role`/`task` fields from panes.

## Session features (v1.2.0)

tmux-ide sessions include these built-in features:

### Mouse support

Mouse is enabled by default. Users can click to focus panes, scroll with trackpad, and drag pane borders to resize.

### Two-line status bar

```
Line 0:  MY-PROJECT IDE            ●            14:30 │ Mar 17
Line 1:  ⏺ Claude 1 │ ● Claude 2 │ ⏺ Dev Server │ Shell
```

- Line 0: session name, window indicators, time/date
- Line 1: clickable pane tabs (click to switch panes)
- Green `⏺` next to panes with a running dev server (listening TCP port)
- Pulsing `⏺` next to panes where Claude/Codex is actively working
- Dim `●` next to panes where Claude/Codex is idle

### Config drift detection

If `ide.yml` is edited while a session is running, `tmux-ide` warns the user and suggests `tmux-ide restart` to apply changes.

### Debugging

```bash
tmux-ide --verbose          # Log all tmux commands to stderr
TMUX_IDE_DEBUG=1 tmux-ide   # Same via env var
```

## Programmatic CLI

All commands support `--json` for structured output.

### Read commands

```bash
tmux-ide status --json      # Session status
tmux-ide validate --json    # Validate config
tmux-ide detect --json      # Detect project stack
tmux-ide config --json      # Dump config as JSON
tmux-ide ls --json          # List sessions
tmux-ide doctor --json      # System health check
```

### Write commands

```bash
tmux-ide detect --write                                    # Detect and write config
tmux-ide config set name "my-app"                          # Set config value by dot path
tmux-ide config set rows.0.size "70%"
tmux-ide config add-pane --row 0 --title "Claude" --command "claude"
tmux-ide config remove-pane --row 1 --pane 2
tmux-ide config add-row --size "30%"
tmux-ide config enable-team --name "my-team"               # Enable agent teams
tmux-ide config disable-team                               # Disable agent teams
```

### Session commands

```bash
tmux-ide              # Launch (or re-launch) IDE
tmux-ide stop         # Kill session
tmux-ide restart      # Stop and relaunch
tmux-ide attach       # Reattach
tmux-ide init         # Scaffold config
tmux-ide --verbose    # Launch with tmux command tracing
```

## Modification workflow

1. Read: `tmux-ide config --json`
2. Modify: `tmux-ide config set <path> <value>` or `add-pane`/`remove-pane`
3. Validate: `tmux-ide validate --json`
4. Apply: `tmux-ide restart` (needed if session is already running)

## Best practices

- Always use `--json` for programmatic access
- Always run `validate --json` after config mutations
- Top row ~70% height for Claude panes
- 2-3 Claude panes in the top row (or lead + 2 teammates for teams)
- Dev servers + shell in the bottom row
- Use `detect --json` first to understand the project stack
- For agent teams: assign specific tasks to teammate panes so your prompts stay focused
- The team lead should have `focus: true` for easy access
- Use `tmux-ide --verbose` or `TMUX_IDE_DEBUG=1` when debugging layout issues

## ide.yml format

```yaml
name: project-name
before: pnpm install # optional pre-launch hook
team: # optional agent team config
  name: my-team
rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead # optional layout metadata: "lead" or "teammate"
        focus: true
      - title: Teammate 1
        command: claude
        role: teammate
        task: "Work on frontend" # suggested task text for your prompts
      - title: Teammate 2
        command: claude
        role: teammate
        task: "Work on backend"
  - panes:
      - title: Dev Server
        command: pnpm dev
        dir: apps/web # per-pane working directory
        env:
          PORT: 3000
      - title: Shell
theme:
  accent: colour75
  border: colour238
```
```

## File: `src/attach.ts`
```typescript
import { resolve } from "node:path";
import { getSessionName } from "./lib/yaml-io.ts";
import { outputError } from "./lib/output.ts";
import { attachSession, getSessionState } from "./lib/tmux.ts";

export async function attach(
  targetDir: string | undefined,
  { json: _json }: { json?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  const { name: session } = getSessionName(dir);
  const state = getSessionState(session);

  if (!state.running) {
    outputError(`Session "${session}" is not running. Start it with: tmux-ide`, "NOT_RUNNING");
    return;
  }

  attachSession(session);
}
```

## File: `src/cli.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const cli = join(__dirname, "..", "bin", "cli.js");

function makeProject(config = "name: test-session\nrows:\n  - panes:\n      - title: Shell\n") {
  const dir = mkdtempSync(join(tmpdir(), "tmux-ide-cli-test-"));
  writeFileSync(join(dir, "ide.yml"), config);
  return dir;
}

function runCli(args, { cwd, env } = {}) {
  const mergedEnv = { ...process.env };
  for (const [key, value] of Object.entries(env ?? {})) {
    if (value === undefined) {
      delete mergedEnv[key];
    } else {
      mergedEnv[key] = value;
    }
  }

  return spawnSync("node", [cli, ...args], {
    cwd,
    env: mergedEnv,
    encoding: "utf-8",
  });
}

describe("cli contract regressions", () => {
  it("treats an unknown first positional as a start target path", () => {
    const missingDir = join(tmpdir(), "tmux-ide-missing-project");
    const result = runCli([missingDir]);

    assert.notStrictEqual(result.status, 0);
    assert.match(result.stderr, /No ide\.yml found in/);
    assert.doesNotMatch(result.stderr, /Unknown command:/);
  });

  it("returns a structured start json error when ide.yml is missing", () => {
    const missingDir = join(tmpdir(), "tmux-ide-missing-project-json");
    const result = runCli([missingDir, "--json"]);

    assert.notStrictEqual(result.status, 0);
    const payload = JSON.parse(result.stderr);
    assert.strictEqual(payload.code, "CONFIG_NOT_FOUND");
    assert.match(payload.error, /No ide\.yml found in/);
    assert.match(payload.error, /tmux-ide init/);
    assert.match(payload.error, /tmux-ide detect --write/);
  });

  it("prints help for --help without trying to launch tmux", () => {
    const result = runCli(["--help"]);

    assert.strictEqual(result.status, 0);
    assert.match(result.stdout, /Usage:/);
    assert.match(result.stdout, /tmux-ide <path>/);
    assert.doesNotMatch(result.stderr, /tmux new-session/);
  });

  it("includes inspect in the CLI help output", () => {
    const result = runCli(["--help"]);

    assert.strictEqual(result.status, 0);
    assert.match(result.stdout, /tmux-ide inspect/);
  });

  it("returns the full non-running status json shape", () => {
    const dir = makeProject();

    try {
      const result = runCli(["status", "--json"], { cwd: dir });

      assert.strictEqual(result.status, 0);
      assert.deepStrictEqual(JSON.parse(result.stdout), {
        session: "test-session",
        running: false,
        configExists: true,
        panes: [],
      });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns the detect json envelope with reasoning", () => {
    const dir = mkdtempSync(join(tmpdir(), "tmux-ide-detect-json-test-"));
    writeFileSync(
      join(dir, "package.json"),
      JSON.stringify({
        name: "demo",
        scripts: { dev: "vite" },
        dependencies: { vite: "^5.0.0" },
      }),
    );

    try {
      const result = runCli(["detect", "--json"], { cwd: dir });

      assert.strictEqual(result.status, 0);
      const payload = JSON.parse(result.stdout);
      assert.deepStrictEqual(Object.keys(payload).sort(), ["detected", "suggestedConfig"]);
      assert.ok(Array.isArray(payload.detected.reasons));
      assert.ok(Array.isArray(payload.suggestedConfig.rows));
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a clean attach error without throwing a TypeError", () => {
    const dir = makeProject();

    try {
      const result = runCli(["attach"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /Session "test-session" is not running/);
      assert.doesNotMatch(result.stderr, /ERR_INVALID_ARG_TYPE/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a clean init error when ide.yml already exists", () => {
    const dir = makeProject();

    try {
      const result = runCli(["init"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /ide\.yml already exists/i);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured init json error when ide.yml already exists", () => {
    const dir = makeProject();

    try {
      const result = runCli(["init", "--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.deepStrictEqual(JSON.parse(result.stderr), {
        error: "ide.yml already exists in this directory",
        code: "EXISTS",
      });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured init json error for an unknown template", () => {
    const dir = mkdtempSync(join(tmpdir(), "tmux-ide-cli-init-test-"));

    try {
      const result = runCli(["init", "--template", "missing-template", "--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.deepStrictEqual(JSON.parse(result.stderr), {
        error: 'Template "missing-template" not found',
        code: "NOT_FOUND",
      });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a clean start error for invalid config", () => {
    const dir = makeProject("name: broken\nrows: []\n");

    try {
      const result = runCli([], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /Invalid ide\.yml/);
      assert.match(result.stderr, /tmux-ide validate/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured start json error for invalid config", () => {
    const dir = makeProject("name: broken\nrows: []\n");

    try {
      const result = runCli(["--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      const payload = JSON.parse(result.stderr);
      assert.strictEqual(payload.code, "INVALID_CONFIG");
      assert.match(payload.error, /Invalid ide\.yml/);
      assert.match(payload.error, /tmux-ide validate/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured restart json error for invalid config", () => {
    const dir = makeProject("name: broken\nrows: []\n");

    try {
      const result = runCli(["restart", "--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      const payload = JSON.parse(result.stderr);
      assert.strictEqual(payload.code, "INVALID_CONFIG");
      assert.match(payload.error, /Invalid ide\.yml/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a clean launch error when the before hook fails", () => {
    const dir = makeProject(
      'name: before-fails\nbefore: node -e "process.exit(3)"\nrows:\n  - panes:\n      - title: Shell\n',
    );

    try {
      const result = runCli([], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /before.*hook failed/i);
      assert.match(result.stderr, /node -e/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured start json error when the before hook fails", () => {
    const dir = makeProject(
      'name: before-fails\nbefore: node -e "process.exit(3)"\nrows:\n  - panes:\n      - title: Shell\n',
    );

    try {
      const result = runCli(["--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      const payload = JSON.parse(result.stderr);
      assert.strictEqual(payload.code, "BEFORE_HOOK_FAILED");
      assert.match(payload.error, /before.*hook/i);
      assert.match(payload.error, /node -e/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured attach json error with a non-zero exit code", () => {
    const dir = makeProject();

    try {
      const result = runCli(["attach", "--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.deepStrictEqual(JSON.parse(result.stderr), {
        error: 'Session "test-session" is not running. Start it with: tmux-ide',
        code: "NOT_RUNNING",
      });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a non-zero exit code when stop cannot find the session", () => {
    const dir = makeProject();

    try {
      const result = runCli(["stop"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /No active session "test-session" found/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("returns a structured stop json error with a non-zero exit code", () => {
    const dir = makeProject();

    try {
      const result = runCli(["stop", "--json"], { cwd: dir });

      assert.notStrictEqual(result.status, 0);
      assert.deepStrictEqual(JSON.parse(result.stderr), {
        error: 'No active session "test-session" found',
        code: "NOT_RUNNING",
      });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("keeps doctor human and json success semantics aligned for optional checks", () => {
    const dir = makeProject();

    try {
      const human = runCli(["doctor"], {
        cwd: dir,
        env: { CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: undefined },
      });
      const json = runCli(["doctor", "--json"], {
        cwd: dir,
        env: { CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: undefined },
      });

      assert.strictEqual(human.status === 0, JSON.parse(json.stdout).ok);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
});
```

## File: `src/config-cli.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const cli = join(__dirname, "..", "bin", "cli.js");

function makeProject(config) {
  const dir = mkdtempSync(join(tmpdir(), "tmux-ide-config-test-"));
  writeFileSync(join(dir, "ide.yml"), config);
  return dir;
}

function runCli(args, cwd) {
  return spawnSync("node", [cli, ...args], {
    cwd,
    encoding: "utf-8",
  });
}

describe("config command hardening", () => {
  it("rejects config set when the YAML root is not an object", () => {
    const dir = makeProject("null\n");

    try {
      const result = runCli(["config", "set", "rows.0.title", "Shell"], dir);

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /config root must be an object/);
      assert.doesNotMatch(result.stderr, /TypeError/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("rejects add-pane when row panes is not an array", () => {
    const dir = makeProject("rows:\n  - panes: nope\n");

    try {
      const result = runCli(["config", "add-pane", "--row", "0", "--title", "Shell"], dir);

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /row 0 panes must be an array/);
      assert.doesNotMatch(result.stderr, /TypeError/);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("refuses enable-team when there are no Claude panes to assign", () => {
    const dir = makeProject("name: my-app\nrows:\n  - panes:\n      - title: Shell\n");

    try {
      const result = runCli(["config", "enable-team"], dir);

      assert.notStrictEqual(result.status, 0);
      assert.match(result.stderr, /no Claude panes found/i);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("assigns team metadata and Claude pane roles when enable-team succeeds", () => {
    const dir = makeProject(
      "name: my-app\nrows:\n  - panes:\n      - title: Lead\n        command: claude\n      - title: Reviewer\n        command: claude\n",
    );

    try {
      const result = runCli(["config", "enable-team", "--json"], dir);

      assert.strictEqual(result.status, 0);

      const payload = JSON.parse(result.stdout);
      assert.deepStrictEqual(payload.team, { name: "my-app" });
      assert.deepStrictEqual(payload.roles, [
        { row: 0, pane: 0, title: "Lead", role: "lead" },
        { row: 0, pane: 1, title: "Reviewer", role: "teammate" },
      ]);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
});
```

## File: `src/config.test.ts`
```typescript
import { describe, it, beforeEach, afterEach } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import yaml from "js-yaml";
import { config } from "./config.ts";

let tmpDir;
let origLog;
let logged;

beforeEach(() => {
  tmpDir = mkdtempSync(join(tmpdir(), "tmux-ide-config-test-"));
  logged = [];
  origLog = console.log;
  console.log = (...a) => logged.push(a.join(" "));
});

afterEach(() => {
  console.log = origLog;
  rmSync(tmpDir, { recursive: true, force: true });
});

function writeIdeYml(obj) {
  writeFileSync(
    join(tmpDir, "ide.yml"),
    yaml.dump(obj, { lineWidth: -1, noRefs: true, quotingType: '"' }),
  );
}

function readIdeYml() {
  return yaml.load(readFileSync(join(tmpDir, "ide.yml"), "utf-8"));
}

describe("config dump", () => {
  it("outputs config as JSON", async () => {
    const cfg = { name: "test", rows: [{ panes: [{ title: "Shell" }] }] };
    writeIdeYml(cfg);
    await config(tmpDir, { json: true, action: "dump", args: [] });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.name, "test");
    assert.strictEqual(output.rows[0].panes[0].title, "Shell");
  });
});

describe("config set", () => {
  it("updates a top-level value", async () => {
    writeIdeYml({ name: "old", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, { json: true, action: "set", args: ["name", "new-name"] });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.ok, true);
    assert.strictEqual(output.value, "new-name");
    const saved = readIdeYml();
    assert.strictEqual(saved.name, "new-name");
  });

  it("updates a nested value", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, { json: true, action: "set", args: ["rows.0.panes.0.title", "Editor"] });
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes[0].title, "Editor");
  });

  it("coerces boolean strings", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, { json: true, action: "set", args: ["rows.0.panes.0.focus", "true"] });
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes[0].focus, true);
  });

  it("coerces numeric strings", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, { json: true, action: "set", args: ["rows.0.panes.0.width", "120"] });
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes[0].width, 120);
  });
});

describe("config add-pane", () => {
  it("adds pane to existing row", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, {
      json: true,
      action: "add-pane",
      args: ["--row", "0", "--title", "Tests", "--command", "pnpm test"],
    });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.ok, true);
    assert.strictEqual(output.pane.title, "Tests");
    assert.strictEqual(output.pane.command, "pnpm test");
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes.length, 2);
    assert.strictEqual(saved.rows[0].panes[1].title, "Tests");
  });

  it("adds pane with size", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, {
      json: true,
      action: "add-pane",
      args: ["--row", "0", "--title", "Wide", "--size", "60%"],
    });
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes[1].size, "60%");
  });
});

describe("config remove-pane", () => {
  it("removes pane by index", async () => {
    writeIdeYml({
      name: "test",
      rows: [{ panes: [{ title: "A" }, { title: "B" }, { title: "C" }] }],
    });
    await config(tmpDir, {
      json: true,
      action: "remove-pane",
      args: ["--row", "0", "--pane", "1"],
    });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.ok, true);
    assert.strictEqual(output.removed.title, "B");
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes.length, 2);
    assert.strictEqual(saved.rows[0].panes[0].title, "A");
    assert.strictEqual(saved.rows[0].panes[1].title, "C");
  });
});

describe("config add-row", () => {
  it("creates row with default Shell pane", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, { json: true, action: "add-row", args: [] });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.ok, true);
    assert.strictEqual(output.row, 1);
    const saved = readIdeYml();
    assert.strictEqual(saved.rows.length, 2);
    assert.deepStrictEqual(saved.rows[1].panes, [{ title: "Shell" }]);
  });

  it("creates row with size", async () => {
    writeIdeYml({ name: "test", rows: [{ panes: [{ title: "Shell" }] }] });
    await config(tmpDir, { json: true, action: "add-row", args: ["--size", "30%"] });
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[1].size, "30%");
  });

  it("initializes rows array when it doesn't exist", async () => {
    writeIdeYml({ name: "test" });
    await config(tmpDir, { json: true, action: "add-row", args: [] });
    const saved = readIdeYml();
    assert.strictEqual(saved.rows.length, 1);
  });
});

describe("config enable-team", () => {
  it("assigns roles to Claude panes", async () => {
    writeIdeYml({
      name: "my-app",
      rows: [
        {
          panes: [
            { title: "Lead", command: "claude" },
            { title: "Worker", command: "claude" },
            { title: "Shell" },
          ],
        },
      ],
    });
    await config(tmpDir, { json: true, action: "enable-team", args: [] });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.ok, true);
    assert.strictEqual(output.team.name, "my-app");
    const saved = readIdeYml();
    assert.strictEqual(saved.rows[0].panes[0].role, "lead");
    assert.strictEqual(saved.rows[0].panes[1].role, "teammate");
    assert.strictEqual(saved.rows[0].panes[2].role, undefined);
  });
});

describe("config disable-team", () => {
  it("removes team and role/task fields", async () => {
    writeIdeYml({
      name: "my-app",
      team: { name: "my-app" },
      rows: [
        {
          panes: [
            { title: "Lead", command: "claude", role: "lead" },
            { title: "Worker", command: "claude", role: "teammate", task: "Build UI" },
          ],
        },
      ],
    });
    await config(tmpDir, { json: true, action: "disable-team", args: [] });
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.ok, true);
    assert.strictEqual(output.disabled, true);
    const saved = readIdeYml();
    assert.strictEqual(saved.team, undefined);
    assert.strictEqual(saved.rows[0].panes[0].role, undefined);
    assert.strictEqual(saved.rows[0].panes[1].role, undefined);
    assert.strictEqual(saved.rows[0].panes[1].task, undefined);
  });
});
```

## File: `src/config.ts`
```typescript
import { resolve } from "node:path";
import { readConfig, writeConfig } from "./lib/yaml-io.ts";
import { setByPath } from "./lib/dot-path.ts";
import { outputError } from "./lib/output.ts";
import type { IdeConfig, Pane, Row } from "./types.ts";

/**
 * Read config safely (read-only, no write). Returns config or undefined on error.
 */
function readConfigSafe(dir: string): IdeConfig | undefined {
  let cfg: IdeConfig;
  try {
    ({ config: cfg } = readConfig(dir));
  } catch (e) {
    outputError(`Cannot read ide.yml: ${(e as Error).message}`, "READ_ERROR");
    return;
  }
  return cfg;
}

/**
 * Read config, validate it's an object, run mutator, then write back.
 * Returns the mutator's return value, or undefined on error.
 */
function withConfig<T>(dir: string, mutator: (cfg: IdeConfig) => T): T | undefined {
  const cfg = readConfigSafe(dir);
  if (cfg === undefined) return;

  if (!isConfigObject(cfg)) {
    outputError("Invalid ide.yml: config root must be an object", "INVALID_CONFIG");
    return;
  }

  const result = mutator(cfg);
  writeConfig(dir, cfg);
  return result;
}

export async function config(
  targetDir: string | null,
  { json, action, args }: { json?: boolean; action?: string; args?: string[] } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");

  switch (action) {
    case "dump":
      return dumpConfig(dir, { json });
    case "set":
      return setConfig(dir, args ?? [], { json });
    case "add-pane":
      return addPane(dir, args ?? [], { json });
    case "remove-pane":
      return removePane(dir, args ?? [], { json });
    case "add-row":
      return addRow(dir, args ?? [], { json });
    case "enable-team":
      return enableTeam(dir, args ?? [], { json });
    case "disable-team":
      return disableTeam(dir, { json });
    default:
      return dumpConfig(dir, { json });
  }
}

function dumpConfig(dir: string, { json }: { json?: boolean }): void {
  const cfg = readConfigSafe(dir);
  if (cfg === undefined) return;

  if (json) {
    console.log(JSON.stringify(cfg, null, 2));
  } else {
    console.log(JSON.stringify(cfg, null, 2));
  }
}

function setConfig(dir: string, args: string[], { json }: { json?: boolean }): void {
  const [dotpath, ...rest] = args;
  if (!dotpath || rest.length === 0) {
    outputError("Usage: tmux-ide config set <dotpath> <value>", "USAGE");
    return;
  }

  let value: string | boolean | number = rest.join(" ");
  if (value === "true") value = true;
  else if (value === "false") value = false;
  else if (/^\d+$/.test(value)) value = parseInt(value);

  withConfig(dir, (cfg) => {
    setByPath(cfg as unknown as Record<string, unknown>, dotpath, value);
  });

  if (json) {
    console.log(JSON.stringify({ ok: true, path: dotpath, value }, null, 2));
  } else {
    console.log(`Set ${dotpath} = ${JSON.stringify(value)}`);
  }
}

function addPane(dir: string, args: string[], { json }: { json?: boolean }): void {
  const { row, title, command, size } = parseNamedArgs(args);
  if (row === undefined) {
    outputError(
      "Usage: tmux-ide config add-pane --row <N> --title <T> [--command <C>] [--size <S>]",
      "USAGE",
    );
    return;
  }

  const rowIdx = parseIndex(row);
  if (rowIdx == null) {
    outputError(`Invalid row index "${row}"`, "USAGE");
    return;
  }

  const pane: Partial<Pane> = {};
  if (title) pane.title = title;
  if (command) pane.command = command;
  if (size) pane.size = size;

  withConfig(dir, (cfg) => {
    if (!Array.isArray(cfg.rows)) {
      outputError("Invalid ide.yml: 'rows' must be an array", "INVALID_CONFIG");
    }

    if (!cfg.rows[rowIdx]) {
      outputError(`Row ${rowIdx} does not exist`, "INVALID_ROW");
    }

    if (!Array.isArray(cfg.rows[rowIdx]!.panes)) {
      outputError(`Invalid ide.yml: row ${rowIdx} panes must be an array`, "INVALID_CONFIG");
    }

    cfg.rows[rowIdx]!.panes.push(pane as Pane);
  });

  if (json) {
    console.log(JSON.stringify({ ok: true, row: rowIdx, pane }, null, 2));
  } else {
    console.log(`Added pane "${title ?? "untitled"}" to row ${rowIdx}`);
  }
}

function removePane(dir: string, args: string[], { json }: { json?: boolean }): void {
  const { row, pane } = parseNamedArgs(args);
  if (row === undefined || pane === undefined) {
    outputError("Usage: tmux-ide config remove-pane --row <N> --pane <M>", "USAGE");
    return;
  }

  const rowIdx = parseIndex(row);
  const paneIdx = parseIndex(pane);
  if (rowIdx == null || paneIdx == null) {
    outputError("Usage: tmux-ide config remove-pane --row <N> --pane <M>", "USAGE");
    return;
  }

  let removed: Pane | undefined;
  withConfig(dir, (cfg) => {
    if (!Array.isArray(cfg.rows)) {
      outputError("Invalid ide.yml: 'rows' must be an array", "INVALID_CONFIG");
    }

    if (!Array.isArray(cfg.rows[rowIdx]?.panes)) {
      outputError(`Invalid ide.yml: row ${rowIdx} panes must be an array`, "INVALID_CONFIG");
    }

    if (!cfg.rows[rowIdx]!.panes[paneIdx]) {
      outputError(`Pane ${paneIdx} in row ${rowIdx} does not exist`, "INVALID_PANE");
    }

    removed = cfg.rows[rowIdx]!.panes.splice(paneIdx, 1)[0];
  });

  if (json) {
    console.log(JSON.stringify({ ok: true, row: rowIdx, pane: paneIdx, removed }, null, 2));
  } else {
    console.log(`Removed pane ${paneIdx} ("${removed?.title ?? "untitled"}") from row ${rowIdx}`);
  }
}

function addRow(dir: string, args: string[], { json }: { json?: boolean }): void {
  const { size } = parseNamedArgs(args);

  let rowIdx: number | undefined;
  withConfig(dir, (cfg) => {
    if (cfg.rows !== undefined && !Array.isArray(cfg.rows)) {
      outputError("Invalid ide.yml: 'rows' must be an array", "INVALID_CONFIG");
    }

    const row: Row = { panes: [{ title: "Shell" }] };
    if (size) row.size = size;
    cfg.rows = cfg.rows ?? [];
    cfg.rows.push(row);
    rowIdx = cfg.rows.length - 1;
  });

  if (json) {
    console.log(JSON.stringify({ ok: true, row: rowIdx, size: size ?? null }, null, 2));
  } else {
    console.log(`Added row ${rowIdx}${size ? ` (${size})` : ""}`);
  }
}

function enableTeam(dir: string, args: string[], { json }: { json?: boolean }): void {
  const { name } = parseNamedArgs(args);

  let teamName: string | undefined;
  let result: { team: IdeConfig["team"]; roles: ReturnType<typeof summarizeRoles> } | undefined;
  withConfig(dir, (cfg) => {
    if (cfg.rows !== undefined && !Array.isArray(cfg.rows)) {
      outputError("Invalid ide.yml: 'rows' must be an array", "INVALID_CONFIG");
    }

    teamName = name ?? cfg.name ?? "my-team";
    cfg.team = { name: teamName };

    let leadAssigned = false;
    for (const row of cfg.rows ?? []) {
      for (const pane of row.panes ?? []) {
        if (pane.command === "claude" || pane.role === "lead" || pane.role === "teammate") {
          if (!leadAssigned) {
            pane.role = "lead";
            leadAssigned = true;
          } else {
            pane.role = "teammate";
          }
        }
      }
    }
    if (!leadAssigned) {
      delete cfg.team;
      outputError("Cannot enable agent team: no Claude panes found", "INVALID_CONFIG");
    }

    result = { team: cfg.team, roles: summarizeRoles(cfg) };
  });

  if (json) {
    console.log(JSON.stringify({ ok: true, ...result }, null, 2));
  } else {
    console.log(`Enabled agent team "${teamName}"`);
  }
}

function disableTeam(dir: string, { json }: { json?: boolean }): void {
  withConfig(dir, (cfg) => {
    if (cfg.rows !== undefined && !Array.isArray(cfg.rows)) {
      outputError("Invalid ide.yml: 'rows' must be an array", "INVALID_CONFIG");
    }

    delete cfg.team;
    for (const row of cfg.rows ?? []) {
      if (!Array.isArray(row?.panes)) continue;
      for (const pane of row.panes) {
        delete pane.role;
        delete pane.task;
      }
    }
  });

  if (json) {
    console.log(JSON.stringify({ ok: true, disabled: true }, null, 2));
  } else {
    console.log("Disabled agent team");
  }
}

function summarizeRoles(
  cfg: IdeConfig,
): { row: number; pane: number; title: string | null; role: string }[] {
  const roles: { row: number; pane: number; title: string | null; role: string }[] = [];
  for (let i = 0; i < (cfg.rows ?? []).length; i++) {
    for (let j = 0; j < (cfg.rows[i]!.panes ?? []).length; j++) {
      const p = cfg.rows[i]!.panes[j]!;
      if (p.role) {
        roles.push({ row: i, pane: j, title: p.title ?? null, role: p.role });
      }
    }
  }
  return roles;
}

function parseNamedArgs(args: string[]): Record<string, string> {
  const result: Record<string, string> = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i]!.startsWith("--") && i + 1 < args.length) {
      const key = args[i]!.slice(2);
      result[key] = args[i + 1]!;
      i++;
    }
  }
  return result;
}

function isConfigObject(value: unknown): value is Record<string, unknown> {
  return value != null && typeof value === "object" && !Array.isArray(value);
}

function parseIndex(value: string): number | null {
  if (!/^\d+$/.test(String(value))) return null;
  return Number.parseInt(value, 10);
}
```

## File: `src/detect.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { detectStack, suggestConfig } from "./detect.ts";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

describe("suggestConfig", () => {
  it("creates Next.js config with pnpm", () => {
    const config = suggestConfig("/project", {
      packageManager: "pnpm",
      frameworks: ["next"],
      devCommand: "pnpm dev",
      language: "javascript",
    });
    assert.strictEqual(config.rows[0].size, "70%");
    assert.strictEqual(config.rows[0].panes.length, 2);
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom[0].title, "Next.js");
    assert.strictEqual(bottom[0].command, "pnpm dev");
    assert.strictEqual(bottom[bottom.length - 1].title, "Shell");
  });

  it("creates Next.js + Convex config with 3 Claude panes", () => {
    const config = suggestConfig("/project", {
      packageManager: "pnpm",
      frameworks: ["next", "convex"],
      devCommand: "pnpm dev",
      language: "javascript",
    });
    assert.strictEqual(config.rows[0].panes.length, 3);
    const bottom = config.rows[1].panes;
    const titles = bottom.map((p) => p.title);
    assert.ok(titles.includes("Next.js"));
    assert.ok(titles.includes("Convex"));
    assert.ok(titles.includes("Shell"));
  });

  it("creates Go config", () => {
    const config = suggestConfig("/project", {
      packageManager: null,
      frameworks: ["go"],
      devCommand: null,
      language: "go",
    });
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom[0].title, "Go");
    assert.strictEqual(bottom[0].command, "go run .");
  });

  it("creates Cargo config", () => {
    const config = suggestConfig("/project", {
      packageManager: null,
      frameworks: ["cargo"],
      devCommand: null,
      language: "rust",
    });
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom[0].title, "Cargo");
    assert.strictEqual(bottom[0].command, "cargo watch -x run");
  });

  it("falls back to dev command when no framework detected", () => {
    const config = suggestConfig("/project", {
      packageManager: "npm",
      frameworks: [],
      devCommand: "npm run dev",
      language: "javascript",
    });
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom[0].title, "Dev Server");
    assert.strictEqual(bottom[0].command, "npm run dev");
  });

  it("creates minimal config with just shell when nothing detected", () => {
    const config = suggestConfig("/project", {
      packageManager: null,
      frameworks: [],
      devCommand: null,
      language: null,
    });
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom.length, 1);
    assert.strictEqual(bottom[0].title, "Shell");
  });

  it("uses npm run for npm package manager", () => {
    const config = suggestConfig("/project", {
      packageManager: "npm",
      frameworks: ["next"],
      devCommand: "npm run dev",
      language: "javascript",
    });
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom[0].command, "npm run dev");
  });

  it("uses bun for bun package manager", () => {
    const config = suggestConfig("/project", {
      packageManager: "bun",
      frameworks: ["vite"],
      devCommand: "bun dev",
      language: "javascript",
    });
    const bottom = config.rows[1].panes;
    assert.strictEqual(bottom[0].command, "bun dev");
  });

  it("uses project directory basename as session name", () => {
    const config = suggestConfig("/home/user/my-app", {
      packageManager: null,
      frameworks: [],
      devCommand: null,
      language: null,
    });
    assert.strictEqual(config.name, "my-app");
  });
});

describe("detectStack reasoning", () => {
  it("includes reasons for detected frameworks and command choices", () => {
    const dir = mkdtempSync(join(tmpdir(), "tmux-ide-detect-test-"));

    try {
      writeFileSync(
        join(dir, "package.json"),
        JSON.stringify({
          dependencies: { next: "latest", convex: "latest" },
          scripts: { dev: "next dev" },
        }),
      );
      writeFileSync(join(dir, "pnpm-lock.yaml"), "lockfileVersion: 9");

      const detected = detectStack(dir);
      assert.strictEqual(detected.packageManager, "pnpm");
      assert.ok(detected.reasons.some((reason) => reason.includes("pnpm-lock.yaml")));
      assert.ok(detected.reasons.some((reason) => reason.includes('dependency "next"')));
      assert.ok(detected.reasons.some((reason) => reason.includes("dev command")));
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
});
```

## File: `src/detect.ts`
```typescript
import { resolve, basename } from "node:path";
import { readFileSync, existsSync } from "node:fs";
import { writeConfig } from "./lib/yaml-io.ts";
import type { IdeConfig } from "./types.ts";

interface DetectedStack {
  packageManager: string | null;
  frameworks: string[];
  devCommand: string | null;
  language: string | null;
  reasons: string[];
}

function fileExists(dir: string, name: string): boolean {
  return existsSync(resolve(dir, name));
}

function readJson(dir: string, name: string): Record<string, unknown> | null {
  try {
    return JSON.parse(readFileSync(resolve(dir, name), "utf-8")) as Record<string, unknown>;
  } catch {
    return null;
  }
}

export function detectStack(dir: string): DetectedStack {
  const detected: DetectedStack = {
    packageManager: null,
    frameworks: [],
    devCommand: null,
    language: null,
    reasons: [],
  };

  // Detect package manager from lockfile
  if (fileExists(dir, "pnpm-lock.yaml")) {
    detected.packageManager = "pnpm";
    detected.reasons.push('Detected pnpm from "pnpm-lock.yaml".');
  } else if (fileExists(dir, "bun.lockb") || fileExists(dir, "bun.lock")) {
    detected.packageManager = "bun";
    detected.reasons.push('Detected bun from "bun.lockb" or "bun.lock".');
  } else if (fileExists(dir, "yarn.lock")) {
    detected.packageManager = "yarn";
    detected.reasons.push('Detected yarn from "yarn.lock".');
  } else if (fileExists(dir, "package-lock.json")) {
    detected.packageManager = "npm";
    detected.reasons.push('Detected npm from "package-lock.json".');
  }

  const pkg = readJson(dir, "package.json");
  if (pkg) {
    detected.language = "javascript";
    detected.reasons.push('Detected JavaScript from "package.json".');
    const deps = {
      ...(pkg.dependencies as Record<string, unknown> | undefined),
      ...(pkg.devDependencies as Record<string, unknown> | undefined),
    };

    if (deps["next"]) pushFramework(detected, "next", 'Found dependency "next".');
    if (deps["convex"]) pushFramework(detected, "convex", 'Found dependency "convex".');
    if (deps["vite"]) pushFramework(detected, "vite", 'Found dependency "vite".');
    if (deps["remix"] || deps["@remix-run/node"])
      pushFramework(detected, "remix", "Found Remix dependency.");
    if (deps["nuxt"]) pushFramework(detected, "nuxt", 'Found dependency "nuxt".');
    if (deps["astro"]) pushFramework(detected, "astro", 'Found dependency "astro".');
    if (deps["svelte"] || deps["@sveltejs/kit"])
      pushFramework(detected, "svelte", "Found Svelte dependency.");

    // Detect dev command
    const pm = detected.packageManager ?? "npm";
    const run = pm === "npm" ? "npm run" : pm;
    const scripts = pkg.scripts as Record<string, unknown> | undefined;
    if (scripts?.dev) {
      detected.devCommand = `${run} dev`;
      detected.reasons.push(
        `Using dev command "${detected.devCommand}" from package.json scripts.`,
      );
    } else if (scripts?.start) {
      detected.devCommand = `${run} start`;
      detected.reasons.push(
        `Using start command "${detected.devCommand}" from package.json scripts.`,
      );
    }
  }

  // Python
  if (fileExists(dir, "pyproject.toml") || fileExists(dir, "requirements.txt")) {
    detected.language = detected.language ?? "python";
    detected.reasons.push('Detected Python from "pyproject.toml" or "requirements.txt".');
    try {
      const pyproject = readFileSync(resolve(dir, "pyproject.toml"), "utf-8");
      if (pyproject.includes("fastapi"))
        pushFramework(detected, "fastapi", 'Found "fastapi" in pyproject.toml.');
      else if (pyproject.includes("django"))
        pushFramework(detected, "django", 'Found "django" in pyproject.toml.');
      else if (pyproject.includes("flask"))
        pushFramework(detected, "flask", 'Found "flask" in pyproject.toml.');
    } catch {
      // Ignore missing or unreadable pyproject metadata.
    }
  }

  // Rust
  if (fileExists(dir, "Cargo.toml")) {
    detected.language = detected.language ?? "rust";
    detected.reasons.push('Detected Rust from "Cargo.toml".');
    pushFramework(detected, "cargo", 'Using Cargo workflow from "Cargo.toml".');
  }

  // Go
  if (fileExists(dir, "go.mod")) {
    detected.language = detected.language ?? "go";
    detected.reasons.push('Detected Go from "go.mod".');
    pushFramework(detected, "go", 'Using Go workflow from "go.mod".');
  }

  // Docker
  if (fileExists(dir, "docker-compose.yml") || fileExists(dir, "docker-compose.yaml")) {
    pushFramework(
      detected,
      "docker",
      'Detected Docker from "docker-compose.yml" or "docker-compose.yaml".',
    );
  }

  if (detected.reasons.length === 0) {
    detected.reasons.push("No framework-specific signals found; using the generic layout.");
  }

  return detected;
}

export function suggestConfig(dir: string, detected: DetectedStack): IdeConfig {
  const name = basename(dir);
  const pm = detected.packageManager ?? "npm";
  const run = pm === "npm" ? "npm run" : pm;

  // Default: 2 claude panes + shell
  const config: IdeConfig = {
    name,
    rows: [
      {
        size: "70%",
        panes: [
          { title: "Claude 1", command: "claude" },
          { title: "Claude 2", command: "claude" },
        ],
      },
      {
        panes: [],
      },
    ],
  };

  const bottom = config.rows[1]!.panes;
  const frameworks = detected.frameworks;

  // Add 3rd claude pane for complex stacks
  if (frameworks.length >= 2) {
    config.rows[0]!.panes.push({ title: "Claude 3", command: "claude" });
  }

  // Add dev servers
  if (frameworks.includes("next")) {
    bottom.push({ title: "Next.js", command: `${run} dev` });
  } else if (frameworks.includes("vite")) {
    bottom.push({ title: "Vite", command: `${run} dev` });
  } else if (frameworks.includes("nuxt")) {
    bottom.push({ title: "Nuxt", command: `${run} dev` });
  } else if (frameworks.includes("remix")) {
    bottom.push({ title: "Remix", command: `${run} dev` });
  } else if (frameworks.includes("astro")) {
    bottom.push({ title: "Astro", command: `${run} dev` });
  } else if (frameworks.includes("svelte")) {
    bottom.push({ title: "SvelteKit", command: `${run} dev` });
  } else if (frameworks.includes("fastapi")) {
    bottom.push({ title: "FastAPI", command: "uvicorn main:app --reload" });
  } else if (frameworks.includes("django")) {
    bottom.push({ title: "Django", command: "python manage.py runserver" });
  } else if (frameworks.includes("flask")) {
    bottom.push({ title: "Flask", command: "flask run --reload" });
  } else if (frameworks.includes("cargo")) {
    bottom.push({ title: "Cargo", command: "cargo watch -x run" });
  } else if (frameworks.includes("go")) {
    bottom.push({ title: "Go", command: "go run ." });
  } else if (detected.devCommand) {
    bottom.push({ title: "Dev Server", command: detected.devCommand });
  }

  if (frameworks.includes("convex")) {
    bottom.push({ title: "Convex", command: "npx convex dev" });
  }

  // Always add shell
  bottom.push({ title: "Shell" });

  return config;
}

export async function detect(
  targetDir: string | undefined,
  { json, write }: { json?: boolean; write?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  const detected = detectStack(dir);
  const suggested = suggestConfig(dir, detected);

  if (write) {
    writeConfig(dir, suggested);
    if (json) {
      console.log(JSON.stringify({ detected, suggestedConfig: suggested, written: true }, null, 2));
    } else {
      const desc =
        detected.frameworks.length > 0
          ? detected.frameworks.join(" + ")
          : (detected.language ?? "generic project");
      console.log(`Detected ${desc}. Created ide.yml.`);
      console.log("\nWhy this layout:");
      for (const reason of detected.reasons) {
        console.log(`  - ${reason}`);
      }
    }
    return;
  }

  if (json) {
    console.log(JSON.stringify({ detected, suggestedConfig: suggested }, null, 2));
    return;
  }

  console.log("Detected stack:");
  if (detected.packageManager) console.log(`  Package manager: ${detected.packageManager}`);
  if (detected.language) console.log(`  Language: ${detected.language}`);
  if (detected.frameworks.length) console.log(`  Frameworks: ${detected.frameworks.join(", ")}`);
  if (detected.devCommand) console.log(`  Dev command: ${detected.devCommand}`);
  console.log("\nReasoning:");
  for (const reason of detected.reasons) {
    console.log(`  - ${reason}`);
  }
  console.log("\nRun with --write to create ide.yml, or --json to see the suggested config.");
}

function pushFramework(detected: DetectedStack, framework: string, reason: string): void {
  if (!detected.frameworks.includes(framework)) {
    detected.frameworks.push(framework);
  }
  detected.reasons.push(reason);
}
```

## File: `src/doctor.test.ts`
```typescript
import { describe, it, beforeEach, afterEach } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { doctor } from "./doctor.ts";

let tmpDir: string;
let origCwd: string;
let origLog: typeof console.log;
let logged: string[];
let origExitCode: number | undefined;

beforeEach(() => {
  tmpDir = mkdtempSync(join(tmpdir(), "tmux-ide-doctor-test-"));
  origCwd = process.cwd();
  logged = [];
  origLog = console.log;
  origExitCode = process.exitCode;
  console.log = (...a: string[]) => logged.push(a.join(" "));
});

afterEach(() => {
  process.chdir(origCwd);
  console.log = origLog;
  process.exitCode = origExitCode;
  rmSync(tmpDir, { recursive: true, force: true });
});

describe("doctor", () => {
  it("reports tmux installed check", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    await doctor({ json: true });
    const output = JSON.parse(logged[0]);
    const tmuxCheck = output.checks.find((c) => c.label === "tmux installed");
    assert.ok(tmuxCheck, "should have a 'tmux installed' check");
    // tmux is installed in this CI/test environment, so it should pass
    assert.strictEqual(tmuxCheck.pass, true);
  });

  it("reports tmux version check", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    await doctor({ json: true });
    const output = JSON.parse(logged[0]);
    const versionCheck = output.checks.find((c) => c.label.includes("tmux version"));
    assert.ok(versionCheck, "should have a tmux version check");
  });

  it("reports Node.js version check as passing", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    await doctor({ json: true });
    const output = JSON.parse(logged[0]);
    const nodeCheck = output.checks.find((c) => c.label.includes("Node.js"));
    assert.ok(nodeCheck);
    assert.strictEqual(nodeCheck.pass, true);
  });

  it("reports ide.yml exists check as passing when present", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    await doctor({ json: true });
    const output = JSON.parse(logged[0]);
    const ideCheck = output.checks.find((c) => c.label.includes("ide.yml"));
    assert.ok(ideCheck);
    assert.strictEqual(ideCheck.pass, true);
  });

  it("reports ide.yml exists check as failing when absent", async () => {
    process.chdir(tmpDir);
    // No ide.yml written
    await doctor({ json: true });
    const output = JSON.parse(logged[0]);
    const ideCheck = output.checks.find((c) => c.label.includes("ide.yml"));
    assert.ok(ideCheck);
    assert.strictEqual(ideCheck.pass, false);
  });

  it("marks agent teams check as optional", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    await doctor({ json: true });
    const output = JSON.parse(logged[0]);
    const teamsCheck = output.checks.find((c) => c.label.includes("agent teams"));
    assert.ok(teamsCheck);
    assert.strictEqual(teamsCheck.optional, true);
  });

  it("optional checks don't fail the overall result", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    // Even if agent teams env var is not set, ok should still be true
    const origEnv = process.env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS;
    delete process.env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS;
    try {
      await doctor({ json: true });
      const output = JSON.parse(logged[0]);
      // ok depends on required checks, not optional ones
      const requiredFailing = output.checks.filter((c) => !c.pass && !c.optional);
      if (requiredFailing.length === 0) {
        assert.strictEqual(output.ok, true);
      }
    } finally {
      if (origEnv !== undefined) {
        process.env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS = origEnv;
      }
    }
  });

  it("prints human-readable output without --json", async () => {
    process.chdir(tmpDir);
    writeFileSync(join(tmpDir, "ide.yml"), "name: test\nrows:\n  - panes:\n      - title: Shell\n");
    await doctor();
    // Should have printed colored output with ✓ or ✗
    assert.ok(logged.length > 0);
    assert.ok(logged.some((l) => l.includes("tmux installed")));
  });
});
```

## File: `src/doctor.ts`
```typescript
import { execSync } from "node:child_process";
import { existsSync } from "node:fs";
import { resolve } from "node:path";

interface CheckResult {
  label: string;
  pass: boolean;
  detail: string;
  optional: boolean;
}

function check(
  label: string,
  fn: () => string,
  { optional = false }: { optional?: boolean } = {},
): CheckResult {
  try {
    const result = fn();
    return { label, pass: true, detail: result, optional };
  } catch (e) {
    return { label, pass: false, detail: (e as Error).message, optional };
  }
}

export async function doctor({ json }: { json?: boolean } = {}): Promise<void> {
  const checks: CheckResult[] = [];

  checks.push(
    check("tmux installed", () => {
      execSync("which tmux", { stdio: "ignore" });
      return "found";
    }),
  );

  checks.push(
    check("tmux version ≥ 3.0", () => {
      const version = execSync("tmux -V", { encoding: "utf-8" }).trim();
      const num = parseFloat(version.replace(/[^0-9.]/g, ""));
      if (num < 3.0) throw new Error(`${version} (need ≥ 3.0)`);
      return version;
    }),
  );

  checks.push(
    check("Node.js ≥ 18", () => {
      const major = parseInt(process.versions.node.split(".")[0]!);
      if (major < 18) throw new Error(`Node ${process.versions.node} (need ≥ 18)`);
      return `v${process.versions.node}`;
    }),
  );

  checks.push(
    check("256-color terminal", () => {
      const term = process.env.TERM ?? "";
      if (
        !term.includes("256color") &&
        !term.includes("ghostty") &&
        !term.includes("kitty") &&
        term !== "tmux-256color"
      ) {
        throw new Error(`$TERM is "${term}"`);
      }
      return term;
    }),
  );

  checks.push(
    check("ide.yml exists", () => {
      const path = resolve(".", "ide.yml");
      if (!existsSync(path)) throw new Error("not found in current directory");
      return "found";
    }),
  );

  checks.push(
    check(
      "Claude Code agent teams",
      () => {
        if (process.env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS !== "1") {
          throw new Error("not set (enable with CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)");
        }
        return "enabled";
      },
      { optional: true },
    ),
  );

  const allPass = checks.every((c) => c.pass || c.optional);

  if (json) {
    console.log(JSON.stringify({ ok: allPass, checks }, null, 2));
    return;
  }

  for (const c of checks) {
    const icon = c.pass ? "✓" : c.optional ? "○" : "✗";
    const color = c.pass ? "\x1b[32m" : c.optional ? "\x1b[33m" : "\x1b[31m";
    console.log(`${color}${icon}\x1b[0m ${c.label} — ${c.detail}`);
  }

  if (!allPass) process.exitCode = 1;
}
```

## File: `src/init.test.ts`
```typescript
import { describe, it, beforeEach, afterEach } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, readFileSync, existsSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { IdeError } from "./lib/errors.ts";
import { init } from "./init.ts";

let tmpDir;
let origCwd;
let origLog;
let logged;

beforeEach(() => {
  tmpDir = mkdtempSync(join(tmpdir(), "tmux-ide-init-test-"));
  origCwd = process.cwd();
  process.chdir(tmpDir);
  logged = [];
  origLog = console.log;
  console.log = (...a) => logged.push(a.join(" "));
});

afterEach(() => {
  process.chdir(origCwd);
  console.log = origLog;
  rmSync(tmpDir, { recursive: true, force: true });
});

describe("init", () => {
  it("creates ide.yml from default template when no stack detected", async () => {
    await init({ json: true });
    assert.ok(existsSync(join(tmpDir, "ide.yml")));
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.created, true);
    assert.strictEqual(output.template, "default");
  });

  it("creates ide.yml from named template", async () => {
    await init({ template: "nextjs", json: true });
    assert.ok(existsSync(join(tmpDir, "ide.yml")));
    const content = readFileSync(join(tmpDir, "ide.yml"), "utf-8");
    assert.ok(content.includes("rows"));
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.created, true);
    assert.strictEqual(output.template, "nextjs");
  });

  it("creates ide.yml from detected stack", async () => {
    // Create a package.json with a Next.js dependency to trigger detection
    writeFileSync(
      join(tmpDir, "package.json"),
      JSON.stringify({
        name: "test-app",
        dependencies: { next: "14.0.0" },
        scripts: { dev: "next dev" },
      }),
    );
    await init({ json: true });
    assert.ok(existsSync(join(tmpDir, "ide.yml")));
    const output = JSON.parse(logged[0]);
    assert.strictEqual(output.created, true);
    assert.ok(output.detected.length > 0);
  });

  it("rejects when ide.yml already exists", async () => {
    writeFileSync(join(tmpDir, "ide.yml"), "name: existing\n");
    await assert.rejects(
      () => init({ json: true }),
      (err) => err instanceof IdeError && err.message.includes("already exists"),
    );
  });

  it("rejects unknown template name", async () => {
    await assert.rejects(
      () => init({ template: "nonexistent-template-xyz", json: true }),
      (err) => err instanceof IdeError && err.message.includes("not found"),
    );
  });

  it("replaces the name field with the directory basename", async () => {
    await init({ template: "default", json: true });
    const content = readFileSync(join(tmpDir, "ide.yml"), "utf-8");
    const dirName = tmpDir.split("/").pop();
    assert.ok(content.includes(`name: ${dirName}`));
  });

  it("prints human-readable output without --json", async () => {
    await init();
    assert.ok(logged.some((l) => l.includes("Created ide.yml")));
  });
});
```

## File: `src/init.ts`
```typescript
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { resolve, basename, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
import { detectStack, suggestConfig } from "./detect.ts";
import { outputError, printLayout } from "./lib/output.ts";
import type { IdeConfig } from "./types.ts";

export async function init({
  template,
  json,
}: { template?: string; json?: boolean } = {}): Promise<void> {
  const dir = process.cwd();
  const configPath = resolve(dir, "ide.yml");

  if (existsSync(configPath)) {
    outputError("ide.yml already exists in this directory", "EXISTS");
  }

  // If a specific template is requested, use it
  if (template) {
    const templatePath = resolve(__dirname, "..", "templates", `${template}.yml`);
    if (!existsSync(templatePath)) {
      outputError(`Template "${template}" not found`, "NOT_FOUND");
    }

    let content = readFileSync(templatePath, "utf-8");
    const name = basename(dir);
    content = content.replace(/^name: .+/m, `name: ${name}`);
    writeFileSync(configPath, content);

    if (json) {
      console.log(JSON.stringify({ created: true, template, name }));
    } else {
      console.log(`Created ide.yml from "${template}" template for "${name}"`);
      const yaml = (await import("js-yaml")).default;
      printLayout(yaml.load(content) as IdeConfig);
    }
    return;
  }

  // Smart detection
  const detected = detectStack(dir);
  const name = basename(dir);

  if (detected.frameworks.length > 0) {
    // Use detected stack to generate config
    const config = suggestConfig(dir, detected);
    const yaml = (await import("js-yaml")).default;
    writeFileSync(configPath, yaml.dump(config, { lineWidth: -1, noRefs: true, quotingType: '"' }));

    const desc = detected.frameworks.join(" + ");
    if (json) {
      console.log(JSON.stringify({ created: true, detected: detected.frameworks, name }));
    } else {
      console.log(`Detected ${desc}. Created ide.yml for "${name}".`);
      printLayout(config);
      console.log("Edit it to customize, then run: tmux-ide");
    }
  } else {
    // Fallback to default template
    const templatePath = resolve(__dirname, "..", "templates", "default.yml");
    let content = readFileSync(templatePath, "utf-8");
    content = content.replace(/^name: .+/m, `name: ${name}`);
    writeFileSync(configPath, content);

    if (json) {
      console.log(JSON.stringify({ created: true, template: "default", name }));
    } else {
      console.log(`Created ide.yml for "${name}"`);
      const yaml = (await import("js-yaml")).default;
      printLayout(yaml.load(content) as IdeConfig);
      console.log("Edit it to configure your workspace, then run: tmux-ide");
    }
  }
}
```

## File: `src/inspect.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const cli = join(__dirname, "..", "bin", "cli.js");

function makeProject(config = "name: inspect-session\nrows:\n  - panes:\n      - title: Shell\n") {
  const dir = mkdtempSync(join(tmpdir(), "tmux-ide-inspect-test-"));
  writeFileSync(join(dir, "ide.yml"), config);
  return dir;
}

function runCli(args, cwd) {
  return spawnSync("node", [cli, ...args], {
    cwd,
    encoding: "utf-8",
  });
}

describe("inspect command", () => {
  it("prints resolved config state as json", () => {
    const dir = makeProject(
      "name: inspect-session\nrows:\n  - size: 70%\n    panes:\n      - title: Claude\n        command: claude\n        focus: true\n      - title: Shell\n",
    );

    try {
      const result = runCli(["inspect", "--json"], dir);

      assert.strictEqual(result.status, 0);
      const payload = JSON.parse(result.stdout);
      assert.strictEqual(payload.session, "inspect-session");
      assert.strictEqual(payload.valid, true);
      assert.strictEqual(payload.summary.rows, 1);
      assert.strictEqual(payload.summary.panes, 2);
      assert.strictEqual(payload.summary.focus, "rows.0.panes.0");
      assert.strictEqual(payload.tmux.running, false);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  it("reports validation errors for invalid pane arrays instead of crashing", () => {
    const dir = makeProject("name: inspect-session\nrows:\n  - panes: nope\n");

    try {
      const result = runCli(["inspect", "--json"], dir);

      assert.strictEqual(result.status, 0);
      const payload = JSON.parse(result.stdout);
      assert.strictEqual(payload.valid, false);
      assert.match(JSON.stringify(payload.errors), /rows\[0\]\.panes must be an array/);
      assert.deepStrictEqual(payload.rows, [
        {
          index: 0,
          size: null,
          panes: [],
        },
      ]);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
});
```

## File: `src/inspect.ts`
```typescript
import { resolve, basename } from "node:path";
import { readConfig } from "./lib/yaml-io.ts";
import { validateConfig } from "./validate.ts";
import { outputError } from "./lib/output.ts";
import { getSessionState, listPanes } from "./lib/tmux.ts";
import type { IdeConfig } from "./types.ts";

interface ResolvedPane {
  index: number;
  title: string | null;
  command: string | null;
  dir: string;
  size: string | null;
  focus: boolean;
  role: string | null;
  task: string | null;
  env: Record<string, unknown>;
}

interface ResolvedRow {
  index: number;
  size: string | null;
  panes: ResolvedPane[];
}

interface Inspection {
  dir: string;
  configPath: string;
  valid: boolean;
  errors: string[];
  session: string;
  before: string | null;
  summary: { rows: number; panes: number; focus: string | null };
  team: IdeConfig["team"] | null;
  theme: IdeConfig["theme"] | null;
  focus: { row: number; pane: number; title: string | null } | null;
  rows: ResolvedRow[];
  rawConfig: IdeConfig;
  tmux: { running: boolean; panes: ReturnType<typeof listPanes> };
}

export function buildInspection(
  dir: string,
  {
    config,
    configPath,
    running,
    panes,
  }: {
    config: IdeConfig;
    configPath: string;
    running: boolean;
    panes: ReturnType<typeof listPanes>;
  },
): Inspection {
  const errors = validateConfig(config);
  const rows = Array.isArray(config?.rows) ? config.rows : [];
  const resolvedRows: ResolvedRow[] = rows.map((row, rowIndex) => ({
    index: rowIndex,
    size: row.size ?? null,
    panes: (Array.isArray(row?.panes) ? row.panes : []).map((pane, paneIndex) => ({
      index: paneIndex,
      title: pane.title ?? null,
      command: pane.command ?? null,
      dir: pane.dir ?? ".",
      size: pane.size ?? null,
      focus: pane.focus === true,
      role: pane.role ?? null,
      task: pane.task ?? null,
      env: pane.env ?? {},
    })),
  }));

  const focusPane =
    resolvedRows
      .flatMap((row) => row.panes.map((pane) => ({ row: row.index, pane })))
      .find(({ pane }) => pane.focus) ?? null;
  const session = config?.name ?? basename(dir);

  return {
    dir,
    configPath,
    valid: errors.length === 0,
    errors,
    session,
    before: config?.before ?? null,
    summary: {
      rows: resolvedRows.length,
      panes: resolvedRows.reduce((sum, row) => sum + row.panes.length, 0),
      focus: focusPane ? `rows.${focusPane.row}.panes.${focusPane.pane.index}` : null,
    },
    team: config?.team ?? null,
    theme: config?.theme ?? null,
    focus: focusPane
      ? {
          row: focusPane.row,
          pane: focusPane.pane.index,
          title: focusPane.pane.title,
        }
      : null,
    rows: resolvedRows,
    rawConfig: config,
    tmux: {
      running,
      panes,
    },
  };
}

export async function inspect(
  targetDir: string | undefined,
  { json }: { json?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");

  let config;
  let configPath: string;
  try {
    ({ config, configPath } = readConfig(dir));
  } catch (error) {
    outputError(`Cannot read ide.yml: ${(error as Error).message}`, "READ_ERROR");
    return;
  }

  const session = config?.name ?? basename(dir);
  const state = getSessionState(session);
  const panes = state.running ? listPanes(session) : [];
  const data = buildInspection(dir, { config, configPath, running: state.running, panes });

  if (json) {
    console.log(JSON.stringify(data, null, 2));
    return;
  }

  console.log(`Directory: ${data.dir}`);
  console.log(`Config:    ${data.configPath}`);
  console.log(`Valid:     ${data.valid ? "yes" : "no"}`);
  console.log(`Session:   ${data.session}`);
  console.log(`Running:   ${data.tmux.running ? "yes" : "no"}`);
  console.log(`Rows:      ${data.summary.rows}`);
  console.log(`Panes:     ${data.summary.panes}`);
  console.log(`Team:      ${data.team ? data.team.name : "disabled"}`);

  if (data.focus) {
    console.log(
      `Focus:     row ${data.focus.row}, pane ${data.focus.pane}${data.focus.title ? ` (${data.focus.title})` : ""}`,
    );
  }

  if (!data.valid) {
    console.log("\nValidation Errors:");
    for (const error of data.errors) {
      console.log(`  - ${error}`);
    }
  }

  console.log("\nResolved Layout:");
  for (const row of data.rows) {
    console.log(`  Row ${row.index}${row.size ? ` (${row.size})` : ""}`);
    for (const pane of row.panes) {
      const parts: string[] = [];
      if (pane.title) parts.push(pane.title);
      if (pane.command) parts.push(`cmd=${pane.command}`);
      if (pane.dir && pane.dir !== ".") parts.push(`dir=${pane.dir}`);
      if (pane.role) parts.push(`role=${pane.role}`);
      if (pane.focus) parts.push("focus");
      console.log(`    - pane ${pane.index}: ${parts.join(" | ") || "shell"}`);
    }
  }

  if (data.tmux.running && data.tmux.panes.length > 0) {
    console.log("\nLive Panes:");
    for (const pane of data.tmux.panes) {
      const active = pane.active ? " (active)" : "";
      console.log(`  ${pane.index}: ${pane.title} [${pane.width}x${pane.height}]${active}`);
    }
  }
}
```

## File: `src/integration.test.ts`
```typescript
import { describe, it, before, after } from "node:test";
import assert from "node:assert/strict";
import { execSync, execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";
import { launch } from "./launch.ts";
import { restart } from "./restart.ts";

// Skip entire suite unless tmux is installed and we can create sessions.
let tmuxAvailable = false;
try {
  execSync("tmux -V", { stdio: "ignore" });
  const probeSession = `tmux-ide-test-probe-${process.pid}`;
  try {
    execSync(`tmux new-session -d -s "${probeSession}" -x 80 -y 24`, { stdio: "ignore" });
    execSync(`tmux kill-session -t "${probeSession}"`, { stdio: "ignore" });
    tmuxAvailable = true;
  } catch {
    // tmux is installed but session creation is blocked in this environment.
  }
} catch {
  // tmux is not installed.
}

describe(
  "integration",
  { skip: !tmuxAvailable && "tmux is unavailable or session access is blocked" },
  () => {
    let tmpDir;
    const session = "tmux-ide-test-integration";
    const __dirname = dirname(fileURLToPath(import.meta.url));
    const cli = join(__dirname, "..", "bin", "cli.js");

    function run(args) {
      return execFileSync("node", [cli, ...args], { cwd: tmpDir, encoding: "utf-8" });
    }

    function runJSON(args) {
      return JSON.parse(run([...args, "--json"]));
    }

    function killSession() {
      try {
        execSync(`tmux kill-session -t "${session}"`, { stdio: "ignore" });
      } catch {
        // Session was already absent.
      }
    }

    function createSession() {
      execSync(`tmux new-session -d -s "${session}" -x 80 -y 24`, { stdio: "ignore" });
    }

    before(() => {
      tmpDir = mkdtempSync(join(tmpdir(), "tmux-ide-test-"));
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nrows:\n  - panes:\n      - title: Shell\n`,
      );
    });

    after(() => {
      killSession();
      rmSync(tmpDir, { recursive: true, force: true });
    });

    it("status --json reports not running when no session exists", () => {
      killSession();
      const result = runJSON(["status"]);
      assert.strictEqual(result.running, false);
    });

    it("status --json reports running after session is created", () => {
      killSession();
      createSession();
      const result = runJSON(["status"]);
      assert.strictEqual(result.running, true);
      killSession();
    });

    it("inspect --json includes live tmux pane state when the session is running", () => {
      killSession();
      createSession();
      const result = runJSON(["inspect"]);

      assert.strictEqual(result.session, session);
      assert.strictEqual(result.tmux.running, true);
      assert.ok(Array.isArray(result.tmux.panes));
      assert.ok(result.tmux.panes.length >= 1);

      killSession();
    });

    it("launch creates the configured session without attaching when requested", async () => {
      killSession();

      await launch(tmpDir, { attach: false });

      const result = runJSON(["status"]);
      assert.strictEqual(result.running, true);
      assert.ok(result.panes.length >= 1);

      killSession();
    });

    it("launch reuses an existing session instead of creating a new layout", async () => {
      killSession();
      await launch(tmpDir, { attach: false });

      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nrows:\n  - panes:\n      - title: Changed\n      - title: Shell\n`,
      );

      await launch(tmpDir, { attach: false });

      const result = runJSON(["status"]);
      assert.strictEqual(result.running, true);
      assert.deepStrictEqual(
        result.panes.map((pane) => pane.title),
        ["Shell"],
      );

      killSession();
    });

    it("launch runs a successful before hook before creating the session", async () => {
      killSession();
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nbefore: node -e "require('node:fs').writeFileSync('before.ok','ok')"\nrows:\n  - panes:\n      - title: Shell\n`,
      );

      await launch(tmpDir, { attach: false });

      assert.strictEqual(runJSON(["status"]).running, true);
      assert.strictEqual(existsSync(join(tmpDir, "before.ok")), true);
      killSession();
    });

    it("launch does not create a session when the before hook fails", async () => {
      killSession();
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nbefore: node -e "process.exit(3)"\nrows:\n  - panes:\n      - title: Shell\n`,
      );

      await assert.rejects(() => launch(tmpDir, { attach: false }), /before hook failed/i);
      assert.strictEqual(runJSON(["status"]).running, false);
    });

    it("restart recreates the session without attaching when requested", async () => {
      killSession();
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nrows:\n  - panes:\n      - title: Shell\n`,
      );
      createSession();

      await restart(tmpDir, { attach: false });

      const result = runJSON(["status"]);
      assert.strictEqual(result.running, true);
      assert.ok(result.panes.length >= 1);

      killSession();
    });

    it("restart applies the updated layout from ide.yml", async () => {
      killSession();
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nrows:\n  - panes:\n      - title: Shell\n`,
      );
      await launch(tmpDir, { attach: false });

      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nrows:\n  - panes:\n      - title: Claude\n      - title: Shell\n`,
      );

      await restart(tmpDir, { attach: false });

      const result = runJSON(["status"]);
      assert.strictEqual(result.running, true);
      assert.strictEqual(result.panes.length, 2);
      assert.deepStrictEqual(
        result.panes.map((pane) => pane.title),
        ["Claude", "Shell"],
      );

      killSession();
    });

    it("launch applies a team layout without interactive attach", async () => {
      killSession();
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nteam:\n  name: test-team\nrows:\n  - panes:\n      - title: Lead\n        command: claude\n        role: lead\n      - title: Worker\n        command: claude\n        role: teammate\n        task: Review changes\n`,
      );

      await launch(tmpDir, { attach: false });

      const result = runJSON(["inspect"]);
      assert.strictEqual(result.valid, true);
      assert.strictEqual(result.team.name, "test-team");
      assert.strictEqual(result.tmux.running, true);
      assert.deepStrictEqual(
        result.tmux.panes.map((pane) => pane.title),
        ["Lead", "Worker"],
      );

      killSession();
    });

    it("launch creates the expected pane layout for a team config", async () => {
      killSession();
      writeFileSync(
        join(tmpDir, "ide.yml"),
        `name: ${session}\nteam:\n  name: review-team\nrows:\n  - panes:\n      - title: Lead\n        command: claude\n        role: lead\n      - title: Reviewer\n        command: claude\n        role: teammate\n        task: Review the diff\n`,
      );

      await launch(tmpDir, { attach: false });

      const statusResult = runJSON(["status"]);
      const inspectResult = runJSON(["inspect"]);
      assert.strictEqual(statusResult.running, true);
      assert.strictEqual(statusResult.panes.length, 2);
      assert.strictEqual(inspectResult.team.name, "review-team");
      assert.strictEqual(inspectResult.summary.panes, 2);

      killSession();
    });

    it("stop --json kills a running session", () => {
      createSession();
      run(["stop"]);
      // Verify it's gone
      const result = runJSON(["status"]);
      assert.strictEqual(result.running, false);
    });

    it("validate --json reports valid for our test config", () => {
      const result = runJSON(["validate"]);
      assert.strictEqual(result.valid, true);
      assert.deepStrictEqual(result.errors, []);
    });

    it("doctor --json passes checks", () => {
      const result = runJSON(["doctor"]);
      assert.strictEqual(result.ok, true);
    });

    it("config --json dumps config", () => {
      const result = runJSON(["config"]);
      assert.strictEqual(result.name, session);
      assert.ok(Array.isArray(result.rows));
    });

    it("ls --json returns sessions list", () => {
      const result = runJSON(["ls"]);
      assert.ok(Array.isArray(result.sessions));
    });
  },
);
```

## File: `src/js-yaml.d.ts`
```typescript
declare module "js-yaml" {
  function load(input: string): unknown;
  function dump(
    input: unknown,
    options?: { lineWidth?: number; noRefs?: boolean; quotingType?: string },
  ): string;
  const _default: { load: typeof load; dump: typeof dump };
  export default _default;
  export { load, dump };
}
```

## File: `src/launch.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { buildPaneMap, waitForPaneCommand } from "./launch.ts";

describe("buildPaneMap", () => {
  it("uses returned pane ids instead of assuming sequential numbering", () => {
    const rows = [
      {
        size: "60%",
        panes: [{ title: "A" }, { title: "B" }],
      },
      {
        panes: [{ title: "C" }, { title: "D", dir: "apps/api" }],
      },
    ];
    const splitCalls = [];
    const returnedPaneIds = ["%42", "%99", "%7"];

    const { paneMap, firstPanesOfRows } = buildPaneMap(
      rows,
      "/workspace",
      "%1",
      ({ targetPane, direction, cwd, percent }) => {
        splitCalls.push({ targetPane, direction, cwd, percent });
        return returnedPaneIds.shift();
      },
    );

    assert.deepStrictEqual(splitCalls, [
      { targetPane: "%1", direction: "vertical", cwd: "/workspace", percent: 40 },
      { targetPane: "%1", direction: "horizontal", cwd: "/workspace", percent: 50 },
      { targetPane: "%42", direction: "horizontal", cwd: "/workspace/apps/api", percent: 50 },
    ]);

    assert.deepStrictEqual(paneMap, [
      ["%1", "%99"],
      ["%42", "%7"],
    ]);
    assert.deepStrictEqual([...firstPanesOfRows], ["%1", "%42"]);
  });

  it("chains additional row splits from the returned row pane ids", () => {
    const rows = [
      { size: "50%", panes: [{ title: "Lead" }] },
      { size: "30%", panes: [{ title: "Worker" }] },
      { panes: [{ title: "Shell" }] },
    ];
    const splitCalls = [];
    const returnedPaneIds = ["%21", "%34"];

    const { paneMap, firstPanesOfRows } = buildPaneMap(
      rows,
      "/workspace",
      "%5",
      ({ targetPane, direction, cwd, percent }) => {
        splitCalls.push({ targetPane, direction, cwd, percent });
        return returnedPaneIds.shift();
      },
    );

    assert.deepStrictEqual(splitCalls, [
      { targetPane: "%5", direction: "vertical", cwd: "/workspace", percent: 50 },
      { targetPane: "%21", direction: "vertical", cwd: "/workspace", percent: 40 },
    ]);
    assert.deepStrictEqual(paneMap, [["%5"], ["%21"], ["%34"]]);
    assert.deepStrictEqual([...firstPanesOfRows], ["%5", "%21", "%34"]);
  });
});

describe("waitForPaneCommand", () => {
  it("returns true once the pane reports an expected command", () => {
    const seenSleeps = [];
    const commands = ["zsh", "zsh", "claude"];

    const result = waitForPaneCommand("%1", ["claude"], {
      attempts: 5,
      delayMs: 25,
      getCurrentCommand: () => commands.shift(),
      sleep: (ms) => seenSleeps.push(ms),
    });

    assert.strictEqual(result, true);
    assert.deepStrictEqual(seenSleeps, [25, 25]);
  });

  it("returns false after exhausting retries", () => {
    const seenSleeps = [];

    const result = waitForPaneCommand("%1", ["claude"], {
      attempts: 3,
      delayMs: 10,
      getCurrentCommand: () => "zsh",
      sleep: (ms) => seenSleeps.push(ms),
    });

    assert.strictEqual(result, false);
    assert.deepStrictEqual(seenSleeps, [10, 10]);
  });
});
```

## File: `src/launch.ts`
```typescript
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { execSync } from "node:child_process";
import { createHash } from "node:crypto";
import { readConfig, getSessionName } from "./lib/yaml-io.ts";
import { computeSizes, toSplitPercents } from "./lib/sizes.ts";
import { outputError } from "./lib/output.ts";
import { collectPaneStartupPlan } from "./lib/launch-plan.ts";
import { buildSessionOptions } from "./lib/session-options.ts";
import {
  attachSession,
  createDetachedSession,
  getPaneCurrentCommand,
  getSessionVariable,
  hasSession,
  runSessionCommand,
  selectPane,
  sendLiteral,
  setPaneTitle,
  setSessionEnvironment,
  setSessionVariable,
  splitPane,
  startSessionMonitor,
} from "./lib/tmux.ts";
import { validateConfig } from "./validate.ts";
import type { IdeConfig, Row } from "./types.ts";

interface SplitPaneArgs {
  targetPane: string;
  direction: "vertical" | "horizontal";
  cwd: string;
  percent: number;
}

function sleepMs(ms: number): void {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

function configHash(config: IdeConfig): string {
  return createHash("sha256").update(JSON.stringify(config)).digest("hex").slice(0, 12);
}

export function waitForPaneCommand(
  targetPane: string,
  expectedCommands: string[],
  {
    attempts = 20,
    delayMs = 100,
    getCurrentCommand = getPaneCurrentCommand,
    sleep = sleepMs,
  }: {
    attempts?: number;
    delayMs?: number;
    getCurrentCommand?: (pane: string) => string;
    sleep?: (ms: number) => void;
  } = {},
): boolean {
  const allowed = new Set(expectedCommands.map((command) => command.toLowerCase()));

  for (let attempt = 0; attempt < attempts; attempt++) {
    try {
      const current = getCurrentCommand(targetPane)?.trim().toLowerCase();
      if (current && allowed.has(current)) return true;
    } catch {
      // Fall through to retry; tmux can briefly report transitional state.
    }

    if (attempt < attempts - 1) {
      sleep(delayMs);
    }
  }

  return false;
}

export function buildPaneMap(
  rows: Row[],
  dir: string,
  rootPaneId: string,
  splitPaneFn: (args: SplitPaneArgs) => string,
): { paneMap: string[][]; firstPanesOfRows: Set<string> } {
  const rowSizes = computeSizes(rows);
  const rowSplitPercents = toSplitPercents(rowSizes);

  // Create all rows vertically first so each row spans the full width.
  const rowPaneIds = [rootPaneId];
  for (let rowIdx = 1; rowIdx < rows.length; rowIdx++) {
    const splitFrom = rowPaneIds[rowIdx - 1]!;
    const newPaneId = splitPaneFn({
      targetPane: splitFrom,
      direction: "vertical",
      cwd: dir,
      percent: rowSplitPercents[rowIdx - 1]!,
    });
    rowPaneIds.push(newPaneId);
  }

  const paneMap: string[][] = [];
  const firstPanesOfRows = new Set(rowPaneIds);

  for (let rowIdx = 0; rowIdx < rows.length; rowIdx++) {
    const row = rows[rowIdx]!;
    const panes = row.panes ?? [];
    const rowPaneId = rowPaneIds[rowIdx]!;
    const rowPanes = [rowPaneId];

    const paneSizes = computeSizes(panes);
    const paneSplitPercents = toSplitPercents(paneSizes);

    for (let paneIdx = 1; paneIdx < panes.length; paneIdx++) {
      const pane = panes[paneIdx]!;
      const targetPane = rowPanes[paneIdx - 1]!;
      const paneDir = pane.dir ? resolve(dir, pane.dir) : dir;
      const newPaneId = splitPaneFn({
        targetPane,
        direction: "horizontal",
        cwd: paneDir,
        percent: paneSplitPercents[paneIdx - 1]!,
      });
      rowPanes.push(newPaneId);
    }

    paneMap.push(rowPanes);
  }

  return { paneMap, firstPanesOfRows };
}

function loadLaunchConfig(dir: string): IdeConfig {
  let config;

  try {
    ({ config } = readConfig(dir));
  } catch (error) {
    if ((error as NodeJS.ErrnoException)?.code === "ENOENT") {
      outputError(
        `No ide.yml found in ${dir}. Run "tmux-ide init" or "tmux-ide detect --write" to create one.`,
        "CONFIG_NOT_FOUND",
      );
    }

    outputError(`Cannot read ide.yml: ${(error as Error).message}`, "READ_ERROR");
  }

  const errors = validateConfig(config);
  if (errors.length > 0) {
    outputError(
      `Invalid ide.yml in ${dir}. Run "tmux-ide validate" for details.`,
      "INVALID_CONFIG",
    );
  }

  return config;
}

function runBeforeHook(command: string | undefined, dir: string): void {
  if (!command) return;

  console.log(`Running: ${command}`);

  try {
    execSync(command, { cwd: dir, stdio: "inherit" });
  } catch {
    outputError(`The before hook failed: ${command}`, "BEFORE_HOOK_FAILED");
  }
}

export async function launch(
  targetDir: string | undefined,
  { json = false, attach = true }: { json?: boolean; attach?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  const config = loadLaunchConfig(dir);

  const { name: fallbackName } = getSessionName(dir);
  const session = config.name ?? fallbackName;
  const rows = config.rows;
  const theme = config.theme ?? {};
  const team = config.team ?? null;

  runBeforeHook(config.before, dir);

  // If session already exists, check for config drift and attach
  if (hasSession(session)) {
    const currentHash = configHash(config);
    const storedHash = getSessionVariable(session, "@config_hash");
    const configChanged = Boolean(storedHash && currentHash !== storedHash);

    if (json) {
      console.log(JSON.stringify({ session, running: true, configChanged }));
    } else if (configChanged) {
      console.log(`Session "${session}" is running but ide.yml has changed.`);
      console.log(`Run "tmux-ide restart" to apply changes.`);
    } else {
      console.log(`Session "${session}" is already running. Attaching...`);
    }

    if (attach) {
      attachSession(session);
    }
    return;
  }

  // Get terminal dimensions
  const cols = process.stdout.columns ?? 200;
  const lines = process.stdout.rows ?? 50;

  // Create session with first pane
  const rootPaneId = createDetachedSession(session, dir, { cols, lines });

  // Set agent teams env var if team config is present
  if (team) {
    setSessionEnvironment(session, "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS", "1");
  }

  const { paneMap, firstPanesOfRows } = buildPaneMap(
    rows,
    dir,
    rootPaneId,
    ({ targetPane, direction, cwd, percent }) => splitPane(targetPane, direction, cwd, percent),
  );

  const { focusPane, paneActions } = collectPaneStartupPlan(rows, paneMap, firstPanesOfRows, dir);

  for (const action of paneActions) {
    if (action.title) {
      setPaneTitle(action.targetPane, action.title);
    }

    if (action.chdir) {
      sendLiteral(action.targetPane, `cd ${action.chdir}`);
    }

    for (const exportCommand of action.exports) {
      sendLiteral(action.targetPane, exportCommand);
    }

    if (action.command) {
      sendLiteral(action.targetPane, action.command);
    }
  }

  for (const command of buildSessionOptions(session, { theme })) {
    runSessionCommand(command);
  }

  // Store config hash for drift detection on re-launch
  setSessionVariable(session, "@config_hash", configHash(config));

  // Start background session monitor (port detection + agent status)
  const monitorScript = resolve(
    dirname(fileURLToPath(import.meta.url)),
    "lib",
    "session-monitor.js",
  );
  startSessionMonitor(session, monitorScript);

  // Focus the correct pane
  selectPane(focusPane);

  // Launch summary
  const totalPanes = rows.reduce((sum, r) => sum + (r.panes?.length ?? 0), 0);
  console.log(
    `Starting "${session}" (${rows.length} row${rows.length === 1 ? "" : "s"}, ${totalPanes} pane${totalPanes === 1 ? "" : "s"})...`,
  );

  // Attach
  if (attach) {
    attachSession(session);
  }
}
```

## File: `src/ls.test.ts`
```typescript
import { describe, it, beforeEach, afterEach } from "node:test";
import assert from "node:assert/strict";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const cli = join(__dirname, "..", "bin", "cli.js");

// ls.js uses execSync directly (not our tmux.js layer), so we test via CLI
// to avoid needing to mock execSync at the module level.

let origLog;
let logged;

beforeEach(() => {
  logged = [];
  origLog = console.log;
  console.log = (...a) => logged.push(a.join(" "));
});

afterEach(() => {
  console.log = origLog;
});

describe("ls", () => {
  it("returns sessions array via CLI --json", () => {
    const result = spawnSync("node", [cli, "ls", "--json"], {
      encoding: "utf-8",
      timeout: 10000,
    });
    assert.strictEqual(result.status, 0);
    const output = JSON.parse(result.stdout);
    assert.ok(Array.isArray(output.sessions));
  });

  it("parses session list with expected fields", () => {
    const result = spawnSync("node", [cli, "ls", "--json"], {
      encoding: "utf-8",
      timeout: 10000,
    });
    const output = JSON.parse(result.stdout);
    // If there are sessions, each should have name, created, attached fields
    for (const session of output.sessions) {
      assert.ok(typeof session.name === "string");
      assert.ok(typeof session.created === "string");
      assert.ok(typeof session.attached === "boolean");
    }
  });

  it("returns valid JSON structure even if sessions exist", () => {
    const result = spawnSync("node", [cli, "ls", "--json"], {
      encoding: "utf-8",
      timeout: 10000,
    });
    assert.strictEqual(result.status, 0);
    const output = JSON.parse(result.stdout);
    assert.ok(Object.hasOwn(output, "sessions"));
    assert.ok(Array.isArray(output.sessions));
    // Each session must have the expected shape
    for (const s of output.sessions) {
      assert.ok(typeof s.name === "string" && s.name.length > 0);
      assert.ok(typeof s.created === "string");
      assert.ok(typeof s.attached === "boolean");
    }
  });

  it("prints human-readable output without --json", () => {
    // Just verify it doesn't crash and produces output
    const result = spawnSync("node", [cli, "ls"], {
      encoding: "utf-8",
      timeout: 10000,
    });
    assert.strictEqual(result.status, 0);
    assert.ok(result.stdout.length > 0);
  });
});
```

## File: `src/ls.ts`
```typescript
import { execSync } from "node:child_process";

export async function ls({ json }: { json?: boolean } = {}): Promise<void> {
  let raw: string;
  try {
    raw = execSync(
      'tmux list-sessions -F "#{session_name}|#{session_created}|#{session_attached}"',
      { encoding: "utf-8" },
    ).trim();
  } catch {
    if (json) {
      console.log(JSON.stringify({ sessions: [] }));
    } else {
      console.log("No tmux sessions running.");
    }
    return;
  }

  const sessions = raw.split("\n").map((line) => {
    const [name, created, attached] = line.split("|");
    return {
      name,
      created: new Date(parseInt(created!) * 1000).toISOString(),
      attached: attached !== "0",
    };
  });

  if (json) {
    console.log(JSON.stringify({ sessions }, null, 2));
    return;
  }

  // Table output
  console.log("SESSION".padEnd(24) + "CREATED".padEnd(22) + "ATTACHED");
  console.log("─".repeat(54));
  for (const s of sessions) {
    const date = new Date(s.created).toLocaleString();
    console.log(s.name!.padEnd(24) + date.padEnd(22) + (s.attached ? "yes" : "no"));
  }
}
```

## File: `src/postinstall.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync, existsSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const script = join(__dirname, "..", "scripts", "postinstall.js");

function makeHome() {
  const root = mkdtempSync(join(tmpdir(), "tmux-ide-postinstall-test-"));
  const home = join(root, "home");
  mkdirSync(home, { recursive: true });
  return { root, home };
}

function runPostinstall({ home, env } = {}) {
  return spawnSync("node", [script], {
    env: {
      ...process.env,
      HOME: home,
      ...env,
    },
    encoding: "utf-8",
  });
}

describe("postinstall", () => {
  it("does not create Claude config for non-global installs", () => {
    const { root, home } = makeHome();

    try {
      const result = runPostinstall({ home, env: { npm_config_global: undefined } });

      assert.strictEqual(result.status, 0);
      assert.strictEqual(existsSync(join(home, ".claude")), false);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  it("does not create Claude config when Claude is not installed", () => {
    const { root, home } = makeHome();

    try {
      const result = runPostinstall({ home, env: { npm_config_global: "true" } });

      assert.strictEqual(result.status, 0);
      assert.strictEqual(existsSync(join(home, ".claude")), false);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  it("updates existing Claude settings for global installs", () => {
    const { root, home } = makeHome();
    const claudeDir = join(home, ".claude");
    const settingsPath = join(claudeDir, "settings.json");

    mkdirSync(claudeDir, { recursive: true });
    writeFileSync(settingsPath, `${JSON.stringify({ env: { KEEP_ME: "1" } }, null, 2)}\n`);

    try {
      const result = runPostinstall({ home, env: { npm_config_global: "true" } });

      assert.strictEqual(result.status, 0);
      assert.strictEqual(existsSync(join(claudeDir, "skills", "tmux-ide", "SKILL.md")), true);

      const settings = JSON.parse(readFileSync(settingsPath, "utf-8"));
      assert.deepStrictEqual(settings.env, {
        KEEP_ME: "1",
        CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: "1",
      });
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });
});
```

## File: `src/restart.ts`
```typescript
import { resolve } from "node:path";
import { getSessionName } from "./lib/yaml-io.ts";
import { launch } from "./launch.ts";
import { killSession } from "./lib/tmux.ts";

export async function restart(
  targetDir: string | undefined,
  { json, attach }: { json?: boolean; attach?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  const { name: session } = getSessionName(dir);
  const result = killSession(session);

  if (result.stopped) {
    console.log(`Stopped session "${session}"`);
  }

  await launch(dir, { json, attach });
}
```

## File: `src/status.ts`
```typescript
import { resolve } from "node:path";
import { existsSync } from "node:fs";
import { getSessionName } from "./lib/yaml-io.ts";
import { getSessionState, listPanes } from "./lib/tmux.ts";

export async function status(
  targetDir: string | undefined,
  { json }: { json?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  const { name: session } = getSessionName(dir);
  const configExists = existsSync(resolve(dir, "ide.yml"));

  const state = getSessionState(session);
  const running = state.running;
  let panes: ReturnType<typeof listPanes> = [];

  if (running) panes = listPanes(session);

  const data = { session, running, configExists, panes };

  if (json) {
    console.log(JSON.stringify(data, null, 2));
    return;
  }

  console.log(`Session: ${session}`);
  console.log(`Running: ${running ? "yes" : "no"}`);
  console.log(`Config:  ${configExists ? "ide.yml found" : "no ide.yml"}`);

  if (panes.length > 0) {
    console.log(`\nPanes:`);
    for (const p of panes) {
      const active = p.active ? " (active)" : "";
      console.log(`  ${p.index}: ${p.title} [${p.width}x${p.height}]${active}`);
    }
  }
}
```

## File: `src/stop.test.ts`
```typescript
import { describe, it, beforeEach, afterEach, mock } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { _setExecutor } from "./lib/tmux.ts";
import { IdeError } from "./lib/errors.ts";
import { stop } from "./stop.ts";

let mockExec;
let restoreExec;
let tmpDir;

beforeEach(() => {
  mockExec = mock.fn();
  restoreExec = _setExecutor(mockExec);
  tmpDir = mkdtempSync(join(tmpdir(), "tmux-ide-stop-test-"));
});

afterEach(() => {
  restoreExec();
  mock.restoreAll();
  rmSync(tmpDir, { recursive: true, force: true });
});

function writeIdeYml(name) {
  writeFileSync(join(tmpDir, "ide.yml"), `name: ${name}\n`);
}

function makeExecError(stderr) {
  const err = new Error("Command failed");
  err.stderr = stderr;
  return err;
}

describe("stop", () => {
  it("calls stopSessionMonitor before killSession", async () => {
    writeIdeYml("my-app");
    const callLog = [];
    mockExec.mock.mockImplementation((_cmd, args) => {
      callLog.push(args[0]);
      if (args[0] === "show-option") return "\n";
      return "";
    });

    const logged = [];
    const origLog = console.log;
    console.log = (...a) => logged.push(a.join(" "));

    try {
      await stop(tmpDir);
      // show-option (stopSessionMonitor) should come before kill-session
      const showIdx = callLog.indexOf("show-option");
      const killIdx = callLog.indexOf("kill-session");
      assert.ok(showIdx < killIdx, "stopSessionMonitor should be called before killSession");
    } finally {
      console.log = origLog;
    }
  });

  it("outputs JSON when --json is passed", async () => {
    writeIdeYml("test-proj");
    mockExec.mock.mockImplementation((_cmd, args) => {
      if (args[0] === "show-option") return "\n";
      return "";
    });

    const logged = [];
    const origLog = console.log;
    console.log = (...a) => logged.push(a.join(" "));

    try {
      await stop(tmpDir, { json: true });
      const output = JSON.parse(logged[0]);
      assert.deepStrictEqual(output, { stopped: "test-proj" });
    } finally {
      console.log = origLog;
    }
  });

  it("outputs human-readable message by default", async () => {
    writeIdeYml("my-app");
    mockExec.mock.mockImplementation((_cmd, args) => {
      if (args[0] === "show-option") return "\n";
      return "";
    });

    const logged = [];
    const origLog = console.log;
    console.log = (...a) => logged.push(a.join(" "));

    try {
      await stop(tmpDir);
      assert.ok(logged[0].includes('Stopped session "my-app"'));
    } finally {
      console.log = origLog;
    }
  });

  it("throws IdeError when session not found", async () => {
    writeIdeYml("missing");
    mockExec.mock.mockImplementation((_cmd, args) => {
      if (args[0] === "show-option") {
        throw makeExecError("can't find session: missing");
      }
      if (args[0] === "kill-session") {
        throw makeExecError("can't find session: missing");
      }
      return "";
    });

    await assert.rejects(
      () => stop(tmpDir),
      (err) => err instanceof IdeError && err.message.includes("No active session"),
    );
  });

  it("falls back to dir basename when ide.yml has no name", async () => {
    // Write minimal YAML without a name field
    writeFileSync(join(tmpDir, "ide.yml"), "rows:\n  - panes:\n      - title: Shell\n");
    mockExec.mock.mockImplementation((_cmd, args) => {
      if (args[0] === "show-option") return "\n";
      return "";
    });

    const logged = [];
    const origLog = console.log;
    console.log = (...a) => logged.push(a.join(" "));

    try {
      await stop(tmpDir);
      // Session name should be the basename of the temp dir
      assert.ok(logged[0].includes("Stopped session"));
    } finally {
      console.log = origLog;
    }
  });

  it("falls back to dir basename when no ide.yml exists", async () => {
    // No ide.yml written
    mockExec.mock.mockImplementation((_cmd, args) => {
      if (args[0] === "show-option") return "\n";
      return "";
    });

    const logged = [];
    const origLog = console.log;
    console.log = (...a) => logged.push(a.join(" "));

    try {
      await stop(tmpDir);
      assert.ok(logged[0].includes("Stopped session"));
    } finally {
      console.log = origLog;
    }
  });
});
```

## File: `src/stop.ts`
```typescript
import { resolve } from "node:path";
import { getSessionName } from "./lib/yaml-io.ts";
import { outputError } from "./lib/output.ts";
import { killSession, stopSessionMonitor } from "./lib/tmux.ts";

export async function stop(
  targetDir: string | undefined,
  { json }: { json?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  const { name: session } = getSessionName(dir);

  // Stop the session monitor before killing the session
  stopSessionMonitor(session);

  const result = killSession(session);

  if (result.stopped) {
    if (json) {
      console.log(JSON.stringify({ stopped: session }));
    } else {
      console.log(`Stopped session "${session}"`);
    }
    return;
  }

  outputError(`No active session "${session}" found`, "NOT_RUNNING");
}
```

## File: `src/types.ts`
```typescript
export interface IdeConfig {
  name?: string;
  before?: string;
  team?: { name: string };
  rows: Row[];
  theme?: ThemeConfig;
}

export interface Row {
  size?: string;
  panes: Pane[];
}

export interface Pane {
  title?: string;
  command?: string;
  dir?: string;
  size?: string;
  focus?: boolean;
  env?: Record<string, string | number>;
  role?: "lead" | "teammate";
  task?: string;
}

export interface ThemeConfig {
  accent?: string;
  border?: string;
  bg?: string;
  fg?: string;
}

export type TmuxCommand = string[];

export interface PaneAction {
  targetPane: string;
  title: string | null;
  chdir: string | null;
  exports: string[];
  command: string | null;
}

export interface SessionState {
  running: boolean;
  reason: string | null;
}
```

## File: `src/validate.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { validateConfig } from "./validate.ts";

describe("validateConfig", () => {
  it("accepts a valid minimal config", () => {
    const errors = validateConfig({ rows: [{ panes: [{}] }] });
    assert.deepStrictEqual(errors, []);
  });

  it("accepts a valid full config", () => {
    const errors = validateConfig({
      name: "my-project",
      before: "pnpm install",
      rows: [
        {
          size: "70%",
          panes: [
            {
              title: "Editor",
              command: "vim",
              dir: "src",
              size: "60%",
              focus: true,
              env: { PORT: 3000, HOST: "localhost" },
            },
            { title: "Shell" },
          ],
        },
        {
          panes: [{ title: "Dev", command: "pnpm dev" }],
        },
      ],
      theme: { accent: "colour75", border: "colour238", bg: "colour235", fg: "colour248" },
    });
    assert.deepStrictEqual(errors, []);
  });

  it("rejects null config", () => {
    const errors = validateConfig(null);
    assert.deepStrictEqual(errors, ["config must be an object"]);
  });

  it("rejects string config", () => {
    const errors = validateConfig("hello");
    assert.deepStrictEqual(errors, ["config must be an object"]);
  });

  it("rejects array config", () => {
    const errors = validateConfig([]);
    assert.deepStrictEqual(errors, ["config must be an object"]);
  });

  it("requires rows to be an array", () => {
    const errors = validateConfig({ rows: "nope" });
    assert.ok(errors.includes("'rows' must be an array"));
  });

  it("requires rows to be non-empty", () => {
    const errors = validateConfig({ rows: [] });
    assert.ok(errors.includes("'rows' must not be empty"));
  });

  it("requires rows to have a panes array", () => {
    const errors = validateConfig({ rows: [{}] });
    assert.ok(errors.includes("rows[0].panes must be an array"));
  });

  it("requires panes to be non-empty", () => {
    const errors = validateConfig({ rows: [{ panes: [] }] });
    assert.ok(errors.includes("rows[0].panes must not be empty"));
  });

  it("rejects non-string name", () => {
    const errors = validateConfig({ name: 123, rows: [{ panes: [{}] }] });
    assert.ok(errors.includes("'name' must be a string"));
  });

  it("rejects non-string before", () => {
    const errors = validateConfig({ before: true, rows: [{ panes: [{}] }] });
    assert.ok(errors.includes("'before' must be a string"));
  });

  it("rejects non-string pane.title", () => {
    const errors = validateConfig({ rows: [{ panes: [{ title: 42 }] }] });
    assert.ok(errors.includes("rows[0].panes[0].title must be a string"));
  });

  it("rejects non-string pane.command", () => {
    const errors = validateConfig({ rows: [{ panes: [{ command: false }] }] });
    assert.ok(errors.includes("rows[0].panes[0].command must be a string"));
  });

  it("rejects non-string pane.dir", () => {
    const errors = validateConfig({ rows: [{ panes: [{ dir: [] }] }] });
    assert.ok(errors.includes("rows[0].panes[0].dir must be a string"));
  });

  it("rejects non-boolean pane.focus", () => {
    const errors = validateConfig({ rows: [{ panes: [{ focus: "yes" }] }] });
    assert.ok(errors.includes("rows[0].panes[0].focus must be a boolean"));
  });

  it("rejects non-object pane.env", () => {
    const errors = validateConfig({ rows: [{ panes: [{ env: "PORT=3000" }] }] });
    assert.ok(errors.includes("rows[0].panes[0].env must be an object"));
  });

  it("rejects invalid env values", () => {
    const errors = validateConfig({ rows: [{ panes: [{ env: { PORT: true } }] }] });
    assert.ok(errors.includes("rows[0].panes[0].env.PORT must be a string or number"));
  });

  it("rejects size without % suffix", () => {
    const errors = validateConfig({ rows: [{ size: "70", panes: [{}] }] });
    assert.ok(errors.some((e) => e.includes("must be a percentage")));
  });

  it("rejects 0% size", () => {
    const errors = validateConfig({ rows: [{ size: "0%", panes: [{}] }] });
    assert.ok(errors.some((e) => e.includes("must be a percentage")));
  });

  it("rejects >100% size", () => {
    const errors = validateConfig({ rows: [{ panes: [{ size: "150%" }] }] });
    assert.ok(errors.some((e) => e.includes("must not exceed 100%")));
  });

  it("validates theme fields as strings", () => {
    const errors = validateConfig({ rows: [{ panes: [{}] }], theme: { accent: 123 } });
    assert.ok(errors.includes("theme.accent must be a string"));
  });

  it("accepts team metadata without requiring a lead pane", () => {
    const errors = validateConfig({
      team: { name: "my-team" },
      rows: [
        {
          panes: [{ title: "Claude", command: "claude" }, { title: "Shell" }],
        },
      ],
    });
    assert.deepStrictEqual(errors, []);
  });

  it("validates team pane role and task field types when provided", () => {
    const errors = validateConfig({
      team: { name: "my-team" },
      rows: [
        {
          panes: [
            { command: "claude", role: "manager", task: false },
            { command: "claude", role: "teammate", task: "Review changes" },
          ],
        },
      ],
    });
    assert.ok(errors.includes('rows[0].panes[0].role must be "lead" or "teammate"'));
    assert.ok(errors.includes("rows[0].panes[0].task must be a string"));
  });

  it("rejects non-object theme", () => {
    const errors = validateConfig({ rows: [{ panes: [{}] }], theme: "blue" });
    assert.ok(errors.includes("'theme' must be an object"));
  });

  it("rejects leading zeros in size (00%, 007%)", () => {
    const errors = validateConfig({ rows: [{ size: "007%", panes: [{ size: "00%" }] }] });
    assert.ok(errors.some((e) => e.includes('rows[0].size "007%"') && e.includes("percentage")));
    assert.ok(
      errors.some((e) => e.includes('rows[0].panes[0].size "00%"') && e.includes("percentage")),
    );
  });

  it("rejects row sizes summing over 100%", () => {
    const errors = validateConfig({
      rows: [
        { size: "70%", panes: [{}] },
        { size: "40%", panes: [{}] },
      ],
    });
    assert.ok(errors.some((e) => e.includes("Row sizes sum to 110%")));
  });

  it("accepts row sizes summing to exactly 100%", () => {
    const errors = validateConfig({
      rows: [
        { size: "70%", panes: [{}] },
        { size: "30%", panes: [{}] },
      ],
    });
    assert.deepStrictEqual(errors, []);
  });

  it("rejects multiple focus: true in one row", () => {
    const errors = validateConfig({
      rows: [{ panes: [{ focus: true }, { focus: true }] }],
    });
    assert.ok(errors.some((e) => e.includes("Row 0 has 2 panes with focus: true")));
  });

  it("accepts single focus: true per row", () => {
    const errors = validateConfig({
      rows: [{ panes: [{ focus: true }, {}] }, { panes: [{}, { focus: true }] }],
    });
    assert.deepStrictEqual(errors, []);
  });

  it("rejects pane sizes summing over 100% in a row", () => {
    const errors = validateConfig({
      rows: [{ panes: [{ size: "60%" }, { size: "50%" }] }],
    });
    assert.ok(errors.some((e) => e.includes("Row 0 pane sizes sum to 110%")));
  });

  it("accepts pane sizes summing to exactly 100%", () => {
    const errors = validateConfig({
      rows: [{ panes: [{ size: "60%" }, { size: "40%" }] }],
    });
    assert.deepStrictEqual(errors, []);
  });

  it("collects multiple errors at once", () => {
    const errors = validateConfig({
      name: 123,
      before: [],
      rows: [{ panes: [{ title: 42, focus: "yes", size: "0%" }] }],
      theme: "nope",
    });
    assert.ok(errors.length >= 4);
  });
});
```

## File: `src/validate.ts`
```typescript
import { resolve } from "node:path";
import { readConfig } from "./lib/yaml-io.ts";
import { outputError } from "./lib/output.ts";

export function validateConfig(config: unknown): string[] {
  const errors: string[] = [];

  if (config == null || typeof config !== "object" || Array.isArray(config)) {
    errors.push("config must be an object");
    return errors;
  }

  const cfg = config as Record<string, unknown>;

  if (cfg.name !== undefined && typeof cfg.name !== "string") {
    errors.push("'name' must be a string");
  }

  if (cfg.before !== undefined && typeof cfg.before !== "string") {
    errors.push("'before' must be a string");
  }

  if (!Array.isArray(cfg.rows)) {
    errors.push("'rows' must be an array");
  } else if (cfg.rows.length === 0) {
    errors.push("'rows' must not be empty");
  } else {
    for (let i = 0; i < cfg.rows.length; i++) {
      const row = cfg.rows[i] as Record<string, unknown>;
      if (!row.panes || !Array.isArray(row.panes)) {
        errors.push(`rows[${i}].panes must be an array`);
        continue;
      }
      if (row.panes.length === 0) {
        errors.push(`rows[${i}].panes must not be empty`);
      }
      if (row.size !== undefined) {
        validateSize(row.size, `rows[${i}].size`, errors);
      }
      for (let j = 0; j < row.panes.length; j++) {
        const pane = row.panes[j] as Record<string, unknown>;
        if (pane.title !== undefined && typeof pane.title !== "string") {
          errors.push(`rows[${i}].panes[${j}].title must be a string`);
        }
        if (pane.command !== undefined && typeof pane.command !== "string") {
          errors.push(`rows[${i}].panes[${j}].command must be a string`);
        }
        if (pane.dir !== undefined && typeof pane.dir !== "string") {
          errors.push(`rows[${i}].panes[${j}].dir must be a string`);
        }
        if (pane.focus !== undefined && typeof pane.focus !== "boolean") {
          errors.push(`rows[${i}].panes[${j}].focus must be a boolean`);
        }
        if (pane.env !== undefined) {
          if (pane.env == null || typeof pane.env !== "object" || Array.isArray(pane.env)) {
            errors.push(`rows[${i}].panes[${j}].env must be an object`);
          } else {
            for (const [key, val] of Object.entries(pane.env as Record<string, unknown>)) {
              if (typeof val !== "string" && typeof val !== "number") {
                errors.push(`rows[${i}].panes[${j}].env.${key} must be a string or number`);
              }
            }
          }
        }
        if (pane.size !== undefined) {
          validateSize(pane.size, `rows[${i}].panes[${j}].size`, errors);
        }
        if (pane.role !== undefined) {
          if (pane.role !== "lead" && pane.role !== "teammate") {
            errors.push(`rows[${i}].panes[${j}].role must be "lead" or "teammate"`);
          }
        }
        if (pane.task !== undefined && typeof pane.task !== "string") {
          errors.push(`rows[${i}].panes[${j}].task must be a string`);
        }
      }

      // Check multiple focus panes in this row
      const focusCount = (row.panes as Record<string, unknown>[]).filter(
        (p) => p.focus === true,
      ).length;
      if (focusCount > 1) {
        errors.push(`Row ${i} has ${focusCount} panes with focus: true (max 1)`);
      }

      // Check pane sizes sum within this row
      const paneSizes = (row.panes as Record<string, unknown>[])
        .map((p) => p.size)
        .filter((s): s is string => typeof s === "string" && /^[1-9]\d*%$/.test(s))
        .map((s) => parseInt(s, 10));
      const paneSum = paneSizes.reduce((a, b) => a + b, 0);
      if (paneSum > 100) {
        errors.push(`Row ${i} pane sizes sum to ${paneSum}%, which exceeds 100%`);
      }
    }

    // Check row sizes sum
    const rowSizes = (cfg.rows as Record<string, unknown>[])
      .map((r) => r.size)
      .filter((s): s is string => typeof s === "string" && /^[1-9]\d*%$/.test(s))
      .map((s) => parseInt(s, 10));
    const rowSum = rowSizes.reduce((a, b) => a + b, 0);
    if (rowSum > 100) {
      errors.push(`Row sizes sum to ${rowSum}%, which exceeds 100%`);
    }
  }

  // Validate team config
  if (cfg.team !== undefined) {
    if (cfg.team == null || typeof cfg.team !== "object" || Array.isArray(cfg.team)) {
      errors.push("'team' must be an object");
    } else {
      const team = cfg.team as Record<string, unknown>;
      if (team.name === undefined) {
        errors.push("'team.name' is required when team is specified");
      } else if (typeof team.name !== "string") {
        errors.push("'team.name' must be a string");
      }
      if (team.model !== undefined && typeof team.model !== "string") {
        errors.push("'team.model' must be a string");
      }
      if (team.permissions !== undefined && !Array.isArray(team.permissions)) {
        errors.push("'team.permissions' must be an array");
      }
    }
  }

  if (cfg.theme !== undefined) {
    if (cfg.theme == null || typeof cfg.theme !== "object" || Array.isArray(cfg.theme)) {
      errors.push("'theme' must be an object");
    } else {
      const theme = cfg.theme as Record<string, unknown>;
      for (const key of ["accent", "border", "bg", "fg"]) {
        if (theme[key] !== undefined && typeof theme[key] !== "string") {
          errors.push(`theme.${key} must be a string`);
        }
      }
    }
  }

  return errors;
}

function validateSize(value: unknown, path: string, errors: string[]): void {
  const s = String(value);
  if (!/^[1-9]\d*%$/.test(s)) {
    errors.push(`${path} "${value}" must be a percentage (e.g. "50%")`);
    return;
  }
  const num = parseInt(s, 10);
  if (num > 100) {
    errors.push(`${path} must not exceed 100%`);
  }
}

export async function validate(
  targetDir: string | undefined,
  { json }: { json?: boolean } = {},
): Promise<void> {
  const dir = resolve(targetDir ?? ".");
  let config;

  try {
    ({ config } = readConfig(dir));
  } catch (e) {
    outputError(`Cannot read ide.yml: ${(e as Error).message}`, "READ_ERROR");
    return;
  }

  const errors = validateConfig(config);
  const valid = errors.length === 0;

  if (json) {
    console.log(JSON.stringify({ valid, errors }, null, 2));
    return;
  }

  if (valid) {
    console.log("✓ ide.yml is valid");
  } else {
    console.log("✗ ide.yml has errors:");
    for (const e of errors) {
      console.log(`  - ${e}`);
    }
    process.exitCode = 1;
  }
}
```

## File: `src/lib/dot-path.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { getByPath, setByPath } from "./dot-path.ts";

describe("getByPath", () => {
  it("gets a top-level key", () => {
    assert.strictEqual(getByPath({ name: "test" }, "name"), "test");
  });

  it("gets a nested value", () => {
    const obj = { rows: [{ panes: [{ title: "Shell" }] }] };
    assert.strictEqual(getByPath(obj, "rows.0.panes.0.title"), "Shell");
  });

  it("returns undefined for non-existent path", () => {
    assert.strictEqual(getByPath({}, "a.b.c"), undefined);
  });

  it("returns undefined for partially valid path", () => {
    assert.strictEqual(getByPath({ a: { b: 1 } }, "a.b.c"), undefined);
  });
});

describe("setByPath", () => {
  it("sets a top-level key", () => {
    const obj = {};
    setByPath(obj, "name", "test");
    assert.deepStrictEqual(obj, { name: "test" });
  });

  it("sets a nested value", () => {
    const obj = { rows: [{ panes: [{ title: "old" }] }] };
    setByPath(obj, "rows.0.panes.0.title", "new");
    assert.strictEqual(obj.rows[0].panes[0].title, "new");
  });

  it("creates arrays for numeric keys", () => {
    const obj = {};
    setByPath(obj, "rows.0.title", "test");
    assert.ok(Array.isArray(obj.rows));
    assert.strictEqual(obj.rows[0].title, "test");
  });

  it("creates objects for string keys", () => {
    const obj = {};
    setByPath(obj, "a.b.c", "val");
    assert.deepStrictEqual(obj, { a: { b: { c: "val" } } });
  });

  it("handles duplicate segment values (regression)", () => {
    // Bug: rows.0.panes.0 — both "0" segments caused indexOf to return
    // the same index, breaking the lookahead for array vs object creation
    const obj = {};
    setByPath(obj, "rows.0.panes.0", "value");
    assert.ok(Array.isArray(obj.rows), "rows should be an array");
    assert.ok(Array.isArray(obj.rows[0].panes), "panes should be an array");
    assert.strictEqual(obj.rows[0].panes[0], "value");
  });

  it("handles deeper duplicate segments", () => {
    const obj = {};
    setByPath(obj, "a.0.b.0.c", "deep");
    assert.ok(Array.isArray(obj.a));
    assert.ok(Array.isArray(obj.a[0].b));
    assert.strictEqual(obj.a[0].b[0].c, "deep");
  });
});
```

## File: `src/lib/dot-path.ts`
```typescript
/* eslint-disable @typescript-eslint/no-explicit-any */
export function getByPath(obj: Record<string, any>, path: string): unknown {
  return path.split(".").reduce((o: any, k) => o?.[k], obj);
}

export function setByPath(obj: Record<string, any>, path: string, value: unknown): void {
  const keys = path.split(".");
  const last = keys.pop()!;
  let i = 0;
  const target = keys.reduce((o: any, k) => {
    const nextKey = keys[i + 1] ?? last;
    if (o[k] === undefined) o[k] = /^\d+$/.test(nextKey) ? [] : {};
    i++;
    return o[k];
  }, obj);
  target[last] = value;
}
```

## File: `src/lib/errors.ts`
```typescript
export class IdeError extends Error {
  code: string | undefined;
  exitCode: number;

  constructor(
    message: string,
    { code, exitCode = 1, cause }: { code?: string; exitCode?: number; cause?: Error } = {},
  ) {
    super(message, { cause });
    this.name = "IdeError";
    this.code = code;
    this.exitCode = exitCode;
  }

  toJSON(): { error: string; code: string | undefined; cause?: string } {
    const obj: { error: string; code: string | undefined; cause?: string } = {
      error: this.message,
      code: this.code,
    };
    if (this.cause) obj.cause = (this.cause as Error).message;
    return obj;
  }
}

export class ConfigError extends IdeError {
  constructor(message: string, code: string, { cause }: { cause?: Error } = {}) {
    super(message, { code, exitCode: 1, cause });
    this.name = "ConfigError";
  }
}

export class TmuxError extends IdeError {
  constructor(message: string, code: string, { cause }: { cause?: Error } = {}) {
    super(message, { code, exitCode: 1, cause });
    this.name = "TmuxError";
  }
}

export class SessionError extends IdeError {
  constructor(message: string, code: string, { cause }: { cause?: Error } = {}) {
    super(message, { code, exitCode: 1, cause });
    this.name = "SessionError";
  }
}
```

## File: `src/lib/launch-plan.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { buildPaneCommand, collectPaneStartupPlan } from "./launch-plan.ts";

describe("buildPaneCommand", () => {
  it("passes through normal pane commands", () => {
    assert.strictEqual(buildPaneCommand({ command: "pnpm dev" }), "pnpm dev");
  });

  it("returns the command unchanged for Claude panes", () => {
    assert.strictEqual(buildPaneCommand({ command: "claude", role: "lead" }), "claude");
    assert.strictEqual(
      buildPaneCommand({ command: "claude", role: "teammate", task: 'Fix "lint"' }),
      "claude",
    );
  });
});

describe("collectPaneStartupPlan", () => {
  it("launches team panes as normal pane commands", () => {
    const rows = [
      {
        panes: [
          { title: "Lead", command: "claude", role: "lead", focus: true, env: { PORT: 3000 } },
          { title: "Worker", command: "claude", role: "teammate", task: "Review" },
        ],
      },
      {
        panes: [{ title: "Shell", dir: "apps/web" }],
      },
    ];

    const result = collectPaneStartupPlan(
      rows,
      [["%1", "%2"], ["%3"]],
      new Set(["%1", "%3"]),
      "/workspace",
    );

    assert.strictEqual(result.focusPane, "%1");
    assert.deepStrictEqual(result.paneActions, [
      {
        targetPane: "%1",
        title: "Lead",
        chdir: null,
        exports: ["export PORT=3000"],
        command: "claude",
      },
      {
        targetPane: "%2",
        title: "Worker",
        chdir: null,
        exports: [],
        command: "claude",
      },
      {
        targetPane: "%3",
        title: "Shell",
        chdir: "/workspace/apps/web",
        exports: [],
        command: null,
      },
    ]);
  });
});
```

## File: `src/lib/launch-plan.ts`
```typescript
import { resolve } from "node:path";
import type { Pane, Row, PaneAction } from "../types.ts";

export function buildPaneCommand(pane: Pane): string | null {
  if (!pane.command) return null;
  return pane.command;
}

export function collectPaneStartupPlan(
  rows: Row[],
  paneMap: string[][],
  firstPanesOfRows: Set<string>,
  dir: string,
): { focusPane: string; paneActions: PaneAction[] } {
  let focusPane = paneMap[0]![0]!;
  const paneActions: PaneAction[] = [];

  for (let rowIdx = 0; rowIdx < rows.length; rowIdx++) {
    const row = rows[rowIdx]!;
    const panes = row.panes ?? [];

    for (let paneIdx = 0; paneIdx < panes.length; paneIdx++) {
      const pane = panes[paneIdx]!;
      const tmuxPane = paneMap[rowIdx]![paneIdx]!;
      const action: PaneAction = {
        targetPane: tmuxPane,
        title: pane.title ?? null,
        chdir: null,
        exports: [],
        command: null,
      };

      if (pane.dir && firstPanesOfRows.has(tmuxPane)) {
        action.chdir = resolve(dir, pane.dir);
      }

      if (pane.env && typeof pane.env === "object") {
        action.exports = Object.entries(pane.env).map(([key, value]) => `export ${key}=${value}`);
      }

      const command = buildPaneCommand(pane);
      if (command) {
        action.command = command;
      }

      if (pane.focus) {
        focusPane = tmuxPane;
      }

      paneActions.push(action);
    }
  }

  return { focusPane, paneActions };
}
```

## File: `src/lib/output.ts`
```typescript
import { IdeError } from "./errors.ts";
import type { IdeConfig } from "../types.ts";

export function printLayout(config: IdeConfig): void {
  const INNER = 40;
  const rows = config.rows ?? [];
  if (rows.length === 0) return;

  for (let r = 0; r < rows.length; r++) {
    const panes = rows[r]!.panes ?? [];
    const count = panes.length || 1;
    const widths: number[] = [];
    let remaining = INNER;
    for (let i = 0; i < count; i++) {
      const w = i < count - 1 ? Math.floor(INNER / count) : remaining;
      widths.push(w);
      remaining -= w;
    }

    // Top border or mid divider
    if (r === 0) {
      let top = "  \u250c";
      for (let i = 0; i < count; i++) {
        top += "\u2500".repeat(widths[i]!);
        top += i < count - 1 ? "\u252c" : "\u2510";
      }
      console.log(top);
    } else {
      console.log("  \u251c" + "\u2500".repeat(INNER + count - 1) + "\u2524");
    }

    // Content line
    const sizeLabel = rows[r]!.size ?? "";
    let line = "  \u2502";
    for (let i = 0; i < count; i++) {
      const title = panes[i]?.title ?? "";
      const w = widths[i]!;
      const pad = Math.max(0, w - title.length);
      const left = Math.floor(pad / 2);
      const right = pad - left;
      line += " ".repeat(left) + title + " ".repeat(right) + "\u2502";
    }
    if (sizeLabel) line += "  " + sizeLabel;
    console.log(line);

    // Bottom border (last row only)
    if (r === rows.length - 1) {
      let bot = "  \u2514";
      for (let i = 0; i < count; i++) {
        bot += "\u2500".repeat(widths[i]!);
        bot += i < count - 1 ? "\u2534" : "\u2518";
      }
      console.log(bot);
    }
  }
}

export function outputError(
  message: string,
  code: string,
  { exitCode = 1 }: { exitCode?: number } = {},
): never {
  throw new IdeError(message, { code, exitCode });
}

export function printCommandError(
  error: IdeError,
  { json = false }: { json?: boolean } = {},
): never {
  if (json) {
    console.error(JSON.stringify(error.toJSON(), null, 2));
  } else {
    console.error(error.message);
  }
  process.exit(error.exitCode ?? 1);
}
```

## File: `src/lib/session-monitor.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { computeAgentStates, computePortPanes } from "./session-monitor.ts";

describe("computeAgentStates", () => {
  it("returns null for non-agent panes", () => {
    const panes = [
      { id: "%0", pid: "100", cmd: "zsh", title: "Shell" },
      { id: "%1", pid: "101", cmd: "node", title: "Dev Server" },
    ];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), null);
    assert.strictEqual(states.get("%1"), null);
  });

  it("detects idle claude pane", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "claude", title: "Claude Code" }];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), "idle");
  });

  it("detects busy claude pane with Braille spinner", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "claude", title: "\u280B Working on something" }];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), "busy");
  });

  it("detects busy codex pane with spinner", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "codex", title: "\u2839 Thinking" }];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), "busy");
  });

  it("handles case-insensitive command matching", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "Claude", title: "idle title" }];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), "idle");
  });

  it("handles missing cmd and title gracefully", () => {
    const panes = [{ id: "%0", pid: "100", cmd: undefined, title: undefined }];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), null);
  });

  it("handles mixed panes correctly", () => {
    const panes = [
      { id: "%0", pid: "100", cmd: "claude", title: "\u280B Busy" },
      { id: "%1", pid: "101", cmd: "zsh", title: "Shell" },
      { id: "%2", pid: "102", cmd: "claude", title: "Idle Claude" },
    ];
    const states = computeAgentStates(panes);
    assert.strictEqual(states.get("%0"), "busy");
    assert.strictEqual(states.get("%1"), null);
    assert.strictEqual(states.get("%2"), "idle");
  });
});

describe("computePortPanes", () => {
  it("returns empty set when no listeners", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "zsh", title: "Shell" }];
    const result = computePortPanes(panes, {
      listeners: new Set(),
      tree: new Map(),
    });
    assert.strictEqual(result.size, 0);
  });

  it("maps a listener PID directly to its pane", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "node", title: "Dev" }];
    const result = computePortPanes(panes, {
      listeners: new Set(["100"]),
      tree: new Map([["100", "1"]]),
    });
    assert.ok(result.has("%0"));
  });

  it("walks up the process tree to find pane owner", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "zsh", title: "Shell" }];
    // Listener PID 300 -> parent 200 -> parent 100 (pane pid)
    const tree = new Map([
      ["300", "200"],
      ["200", "100"],
      ["100", "1"],
    ]);
    const result = computePortPanes(panes, {
      listeners: new Set(["300"]),
      tree,
    });
    assert.ok(result.has("%0"));
  });

  it("does not match listener to unrelated pane", () => {
    const panes = [{ id: "%0", pid: "100", cmd: "zsh", title: "Shell" }];
    // Listener PID 300 walks up to 200 -> 1, never reaching 100
    const tree = new Map([
      ["300", "200"],
      ["200", "1"],
      ["100", "1"],
    ]);
    const result = computePortPanes(panes, {
      listeners: new Set(["300"]),
      tree,
    });
    assert.strictEqual(result.size, 0);
  });

  it("handles multiple panes with different listeners", () => {
    const panes = [
      { id: "%0", pid: "100", cmd: "node", title: "Web" },
      { id: "%1", pid: "200", cmd: "node", title: "API" },
    ];
    const tree = new Map([
      ["150", "100"],
      ["250", "200"],
      ["100", "1"],
      ["200", "1"],
    ]);
    const result = computePortPanes(panes, {
      listeners: new Set(["150", "250"]),
      tree,
    });
    assert.ok(result.has("%0"));
    assert.ok(result.has("%1"));
    assert.strictEqual(result.size, 2);
  });
});
```

## File: `src/lib/session-monitor.ts`
```typescript
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";

const INTERVAL = 1000;
const SPINNERS = /^[⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏⠂⠒⠢⠆⠐⠠⠄◐◓◑◒|/\\-] /;

interface MonitorPane {
  id: string;
  pid: string;
  cmd?: string;
  title?: string;
}

// --- Port detection (pure helpers) ---

function getListeningPids(): Set<string> {
  // Returns Set of PIDs that have a listening TCP port in range 1024-20000
  try {
    const raw = execFileSync("lsof", ["-nP", "-iTCP", "-sTCP:LISTEN", "-FpPn"], {
      encoding: "utf-8",
      stdio: ["ignore", "pipe", "ignore"],
    });
    const pids = new Set<string>();
    let currentPid: string | null = null;
    for (const line of raw.split("\n")) {
      if (line.startsWith("p")) {
        currentPid = line.slice(1);
      } else if (line.startsWith("n") && currentPid) {
        const match = line.match(/:(\d+)$/);
        if (match) {
          const port = parseInt(match[1]!, 10);
          if (port >= 1024 && port <= 20000) pids.add(currentPid);
        }
      }
    }
    return pids;
  } catch {
    return new Set<string>();
  }
}

function getProcessTree(): Map<string, string> {
  // Returns Map<pid, ppid>
  try {
    const raw = execFileSync("ps", ["-axo", "pid=,ppid="], {
      encoding: "utf-8",
      stdio: ["ignore", "pipe", "ignore"],
    });
    const tree = new Map<string, string>();
    for (const line of raw.trim().split("\n")) {
      const parts = line.trim().split(/\s+/);
      if (parts.length === 2) tree.set(parts[0]!, parts[1]!);
    }
    return tree;
  } catch {
    return new Map<string, string>();
  }
}

export function computePortPanes(
  panes: MonitorPane[],
  { listeners, tree }: { listeners?: Set<string>; tree?: Map<string, string> } = {},
): Set<string> {
  // Walk up from each listening PID to find which pane owns it
  const resolvedListeners = listeners ?? getListeningPids();
  const resolvedTree = tree ?? getProcessTree();
  if (resolvedListeners.size === 0) return new Set<string>();

  const panePids = new Map(panes.map((p) => [p.pid, p.id]));
  const result = new Set<string>();

  for (const listenerPid of resolvedListeners) {
    let pid: string | undefined = listenerPid;
    while (pid && pid !== "0") {
      if (panePids.has(pid)) {
        result.add(panePids.get(pid)!);
        break;
      }
      pid = resolvedTree.get(pid);
    }
  }
  return result;
}

// --- Agent detection ---

export function computeAgentStates(panes: MonitorPane[]): Map<string, "busy" | "idle" | null> {
  // Returns Map<paneId, "busy" | "idle" | null>
  const states = new Map<string, "busy" | "idle" | null>();
  for (const pane of panes) {
    const cmd = (pane.cmd ?? "").toLowerCase();
    if (!cmd.includes("claude") && !cmd.includes("codex")) {
      states.set(pane.id, null);
      continue;
    }
    states.set(pane.id, SPINNERS.test(pane.title ?? "") ? "busy" : "idle");
  }
  return states;
}

// --- Main loop (only runs when executed directly) ---

const isMainModule = process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMainModule) {
  const session: string = process.argv[2]!;
  if (!session) process.exit(1);

  function tmux(...args: string[]): string {
    return execFileSync("tmux", args, { encoding: "utf-8" }).trim();
  }

  function tmuxSilent(...args: string[]): string {
    try {
      return tmux(...args);
    } catch {
      return "";
    }
  }

  function sessionExists(): boolean {
    try {
      tmux("has-session", "-t", session);
      return true;
    } catch {
      return false;
    }
  }

  function hasClients(): boolean {
    return tmuxSilent("list-clients").length > 0;
  }

  function listPanes(): MonitorPane[] {
    const raw = tmuxSilent(
      "list-panes",
      "-t",
      session,
      "-F",
      "#{pane_id}\t#{pane_pid}\t#{pane_current_command}\t#{pane_title}",
    );
    if (!raw) return [];
    return raw.split("\n").map((line) => {
      const [id, pid, cmd, title] = line.split("\t");
      return { id: id!, pid: pid!, cmd, title };
    });
  }

  let lastState = "";

  function tick(): void {
    if (!sessionExists()) process.exit(0);
    if (!hasClients()) return; // skip when nobody is watching

    const panes = listPanes();
    if (panes.length === 0) return;

    const portPanes = computePortPanes(panes);
    const agentStates = computeAgentStates(panes);

    // Build state fingerprint for change detection
    const stateKey = panes
      .map((p) => {
        const port = portPanes.has(p.id) ? "1" : "0";
        const agent = agentStates.get(p.id) ?? "-";
        return `${p.id}:${port}:${agent}`;
      })
      .join("|");

    if (stateKey === lastState) return;

    // Apply changes
    for (const pane of panes) {
      const hasPort = portPanes.has(pane.id) ? "1" : "0";
      const agent = agentStates.get(pane.id);

      tmuxSilent("set-option", "-pqt", pane.id, "@has_port", hasPort);
      tmuxSilent("set-option", "-pqt", pane.id, "@agent_busy", agent === "busy" ? "1" : "0");
      tmuxSilent("set-option", "-pqt", pane.id, "@agent_idle", agent === "idle" ? "1" : "0");
    }

    tmuxSilent("refresh-client", "-S");
    lastState = stateKey;
  }

  setInterval(tick, INTERVAL);
  tick(); // run immediately
}
```

## File: `src/lib/session-options.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import {
  buildSessionOptions,
  themeOptions,
  borderOptions,
  behaviorOptions,
  statusBarOptions,
  keyBindings,
} from "./session-options.ts";

describe("buildSessionOptions", () => {
  it("returns an array of command arrays", () => {
    const options = buildSessionOptions("my-session");

    assert.ok(Array.isArray(options));
    assert.ok(options.length > 0);
    for (const cmd of options) {
      assert.ok(Array.isArray(cmd), "each option should be an array");
      assert.ok(cmd.length >= 2, "each command should have at least 2 elements");
    }
  });

  it("composes all sub-builders", () => {
    const session = "test";
    const theme = {};
    const all = buildSessionOptions(session, { theme });
    const expected = [
      ...themeOptions(session, theme),
      ...borderOptions(session, theme),
      ...behaviorOptions(session),
      ...statusBarOptions(session, theme),
      ...keyBindings(),
    ];

    assert.deepStrictEqual(all, expected);
  });
});

describe("themeOptions", () => {
  it("includes expected color settings", () => {
    const opts = themeOptions("my-session", {});

    const optionNames = opts.map((o) => o[3]);
    assert.ok(optionNames.includes("status-style"));
    assert.ok(optionNames.includes("pane-border-style"));
    assert.ok(optionNames.includes("pane-active-border-style"));
  });

  it("uses default colors when no theme provided", () => {
    const opts = themeOptions("s", {});

    assert.deepStrictEqual(opts[0], [
      "set-option",
      "-t",
      "s",
      "status-style",
      "bg=colour235,fg=colour248",
    ]);
    assert.deepStrictEqual(opts[1], ["set-option", "-t", "s", "pane-border-style", "fg=colour238"]);
    assert.deepStrictEqual(opts[2], [
      "set-option",
      "-t",
      "s",
      "pane-active-border-style",
      "fg=colour75",
    ]);
  });

  it("respects custom theme overrides", () => {
    const opts = themeOptions("my-session", { accent: "red", border: "blue" });

    assert.deepStrictEqual(opts[1], [
      "set-option",
      "-t",
      "my-session",
      "pane-border-style",
      "fg=blue",
    ]);
    assert.deepStrictEqual(opts[2], [
      "set-option",
      "-t",
      "my-session",
      "pane-active-border-style",
      "fg=red",
    ]);
  });
});

describe("borderOptions", () => {
  it("includes pane-border-status and pane-border-format", () => {
    const opts = borderOptions("my-session", {});

    assert.deepStrictEqual(opts[0], [
      "set-option",
      "-t",
      "my-session",
      "pane-border-status",
      "top",
    ]);
    assert.strictEqual(opts[1][3], "pane-border-format");
    assert.ok(opts[1][4].includes("pane_current_path"));
  });
});

describe("behaviorOptions", () => {
  it("includes mouse, escape-time, and status-interval", () => {
    const opts = behaviorOptions("test-session");

    const mouseOpt = opts.find((o) => o[3] === "mouse");
    assert.deepStrictEqual(mouseOpt, ["set-option", "-t", "test-session", "mouse", "on"]);

    const escapeOpt = opts.find((o) => o[3] === "escape-time");
    assert.deepStrictEqual(escapeOpt, ["set-option", "-t", "test-session", "escape-time", "0"]);

    const intervalOpt = opts.find((o) => o[3] === "status-interval");
    assert.deepStrictEqual(intervalOpt, [
      "set-option",
      "-t",
      "test-session",
      "status-interval",
      "1",
    ]);
  });
});

describe("statusBarOptions", () => {
  it("includes two-line status mode", () => {
    const opts = statusBarOptions("my-session", {});
    const statusOpt = opts.find((o) => o[3] === "status");
    assert.deepStrictEqual(statusOpt, ["set-option", "-t", "my-session", "status", "2"]);
  });

  it("includes status-format[1] with pane tabs", () => {
    const opts = statusBarOptions("my-session", {});
    const formatOpt = opts.find((o) => o[3] === "status-format[1]");
    assert.ok(formatOpt, "should include status-format[1]");
    assert.ok(formatOpt[4].includes("#{P:"), "format should use pane loop");
    assert.ok(formatOpt[4].includes("pane_id"), "format should reference pane_id");
  });

  it("includes status-left with session name", () => {
    const opts = statusBarOptions("my-session", {});
    const leftOpt = opts.find((o) => o[3] === "status-left");
    assert.ok(leftOpt[4].includes("MY-SESSION IDE"));
  });

  it("includes all expected status bar settings", () => {
    const opts = statusBarOptions("s", {});
    const names = opts.map((o) => o[3]);

    assert.ok(names.includes("status-left"));
    assert.ok(names.includes("status-left-length"));
    assert.ok(names.includes("status-right"));
    assert.ok(names.includes("status-justify"));
    assert.ok(names.includes("window-status-current-format"));
    assert.ok(names.includes("window-status-format"));
    assert.ok(names.includes("status"));
    assert.ok(names.includes("status-format[1]"));
  });
});

describe("keyBindings", () => {
  it("includes the mouse click binding", () => {
    const bindings = keyBindings();

    assert.strictEqual(bindings.length, 1);
    assert.deepStrictEqual(bindings[0], [
      "bind-key",
      "-n",
      "MouseDown1StatusDefault",
      "select-pane",
      "-t",
      "=",
    ]);
  });
});
```

## File: `src/lib/session-options.ts`
```typescript
/**
 * Composable builders for tmux session configuration.
 * Each returns an array of tmux command arrays.
 */

import type { ThemeConfig, TmuxCommand } from "../types.ts";

export function buildSessionOptions(
  session: string,
  { theme = {} }: { theme?: ThemeConfig } = {},
): TmuxCommand[] {
  return [
    ...themeOptions(session, theme),
    ...borderOptions(session, theme),
    ...behaviorOptions(session),
    ...statusBarOptions(session, theme),
    ...keyBindings(),
  ];
}

export function themeOptions(session: string, theme: ThemeConfig): TmuxCommand[] {
  const accent = theme.accent ?? "colour75";
  const border = theme.border ?? "colour238";
  const bg = theme.bg ?? "colour235";
  const fg = theme.fg ?? "colour248";

  return [
    ["set-option", "-t", session, "status-style", `bg=${bg},fg=${fg}`],
    ["set-option", "-t", session, "pane-border-style", `fg=${border}`],
    ["set-option", "-t", session, "pane-active-border-style", `fg=${accent}`],
  ];
}

export function borderOptions(session: string, theme: ThemeConfig): TmuxCommand[] {
  const accent = theme.accent ?? "colour75";
  const border = theme.border ?? "colour238";
  const fg = theme.fg ?? "colour248";

  return [
    ["set-option", "-t", session, "pane-border-status", "top"],
    [
      "set-option",
      "-t",
      session,
      "pane-border-format",
      ` #{?pane_active,#[fg=${accent}#,bold]▸ #T  #[fg=${fg}]#{pane_current_path},#[fg=${border}]· #T  #{pane_current_path}} `,
    ],
  ];
}

export function behaviorOptions(session: string): TmuxCommand[] {
  return [
    ["set-option", "-t", session, "mouse", "on"],
    ["set-option", "-t", session, "escape-time", "0"],
    ["set-option", "-t", session, "status-interval", "1"],
  ];
}

export function statusBarOptions(session: string, theme: ThemeConfig): TmuxCommand[] {
  const accent = theme.accent ?? "colour75";
  const border = theme.border ?? "colour238";
  const fg = theme.fg ?? "colour248";

  // Pane tab components — each is a self-contained piece
  const agentIndicator = [
    `#{?#{==:#{@agent_busy},1},#[fg=${accent}]⏺ ,`,
    `#{?#{==:#{@agent_idle},1},#[fg=${border}]● ,}}`,
  ].join("");
  const portIndicator = `#{?#{==:#{@has_port},1},#[fg=green]⏺ ,}`;
  const paneStyle = `#{?pane_active,#[fg=${accent}],#[fg=${border}]}`;
  const paneTab = `${agentIndicator}${portIndicator}${paneStyle}#[range=pane|#{pane_id}] #T #[norange]#[default]`;
  const separator = `#{?loop_last_flag,,#[fg=${border}]│}`;

  return [
    [
      "set-option",
      "-t",
      session,
      "status-left",
      `#[fg=colour0,bg=${accent},bold]  ${session.toUpperCase()} IDE #[default] `,
    ],
    ["set-option", "-t", session, "status-left-length", "30"],
    [
      "set-option",
      "-t",
      session,
      "status-right",
      `#[fg=colour243]%H:%M #[fg=${accent}]│ #[fg=${fg}]%b %d `,
    ],
    ["set-option", "-t", session, "status-justify", "centre"],
    ["set-option", "-t", session, "window-status-current-format", `#[fg=${accent},bold]●`],
    ["set-option", "-t", session, "window-status-format", `#[fg=${border}]○`],
    ["set-option", "-t", session, "status", "2"],
    ["set-option", "-t", session, "status-format[1]", `  #{P:${paneTab}${separator}}`],
  ];
}

export function keyBindings(): TmuxCommand[] {
  return [["bind-key", "-n", "MouseDown1StatusDefault", "select-pane", "-t", "="]];
}
```

## File: `src/lib/sizes.test.ts`
```typescript
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { computeSizes, toSplitPercents } from "./sizes.ts";

describe("computeSizes", () => {
  it("distributes remaining space to items without size", () => {
    const result = computeSizes([{ size: "70%" }, {}]);
    assert.deepStrictEqual(result, [70, 30]);
  });

  it("passes through all explicit sizes", () => {
    const result = computeSizes([{ size: "60%" }, { size: "40%" }]);
    assert.deepStrictEqual(result, [60, 40]);
  });

  it("splits equally when no sizes specified", () => {
    const result = computeSizes([{}, {}, {}]);
    const expected = [100 / 3, 100 / 3, 100 / 3];
    assert.deepStrictEqual(result, expected);
  });

  it("handles 3 items with mixed sizes", () => {
    const result = computeSizes([{ size: "60%" }, { size: "25%" }, {}]);
    assert.deepStrictEqual(result, [60, 25, 15]);
  });

  it("handles single item without size", () => {
    const result = computeSizes([{}]);
    assert.deepStrictEqual(result, [100]);
  });

  it("handles single item with size", () => {
    const result = computeSizes([{ size: "50%" }]);
    assert.deepStrictEqual(result, [50]);
  });

  it("handles empty array", () => {
    const result = computeSizes([]);
    assert.deepStrictEqual(result, []);
  });

  it("clamps remaining to zero when sizes exceed 100", () => {
    const result = computeSizes([{ size: "80%" }, { size: "30%" }, {}]);
    assert.deepStrictEqual(result, [80, 30, 0]);
  });
});

describe("toSplitPercents", () => {
  it("converts 70/30 to [30]", () => {
    assert.deepStrictEqual(toSplitPercents([70, 30]), [30]);
  });

  it("converts 60/25/15 correctly", () => {
    const result = toSplitPercents([60, 25, 15]);
    assert.deepStrictEqual(result, [40, 38]);
  });

  it("converts equal 50/50 to [50]", () => {
    assert.deepStrictEqual(toSplitPercents([50, 50]), [50]);
  });

  it("converts equal thirds", () => {
    const result = toSplitPercents([100 / 3, 100 / 3, 100 / 3]);
    assert.deepStrictEqual(result, [67, 50]);
  });

  it("returns empty array for single item", () => {
    assert.deepStrictEqual(toSplitPercents([100]), []);
  });

  it("returns empty array for empty input", () => {
    assert.deepStrictEqual(toSplitPercents([]), []);
  });
});
```

## File: `src/lib/sizes.ts`
```typescript
/**
 * Compute absolute sizes for items where some have explicit sizes and others don't.
 * Items with `size` (e.g. "70%") keep their value; remaining space is split equally
 * among items without a size.
 */
export function computeSizes(items: { size?: string }[]): number[] {
  let claimed = 0;
  let unclaimed = 0;
  for (const item of items) {
    if (item.size) {
      claimed += parseFloat(item.size);
    } else {
      unclaimed++;
    }
  }
  const remaining = Math.max(0, 100 - claimed);
  const defaultSize = unclaimed > 0 ? remaining / unclaimed : 0;
  return items.map((item) => (item.size ? parseFloat(item.size) : defaultSize));
}

/**
 * Convert absolute sizes (e.g. [70, 30]) to tmux split percentages for sequential splits.
 * Returns array of -p values (one per split after the first item).
 *
 * Each tmux split divides the current pane. The percentage given to -p is
 * the portion allocated to the NEW (bottom/right) pane.
 */
export function toSplitPercents(sizes: number[]): number[] {
  const percents: number[] = [];
  for (let i = 1; i < sizes.length; i++) {
    const remaining = sizes.slice(i - 1).reduce((a, b) => a + b, 0);
    const topShare = sizes[i - 1]!;
    percents.push(Math.round(((remaining - topShare) / remaining) * 100));
  }
  return percents;
}
```

## File: `src/lib/tmux.test.ts`
```typescript
import { describe, it, beforeEach, afterEach, mock } from "node:test";
import assert from "node:assert/strict";
import {
  _setExecutor,
  _setSpawner,
  TmuxError,
  getSessionState,
  hasSession,
  killSession,
  listPanes,
  createDetachedSession,
  splitPane,
  sendLiteral,
  getSessionVariable,
  setSessionVariable,
  startSessionMonitor,
  stopSessionMonitor,
  setPaneTitle,
  selectPane,
  getPaneCurrentCommand,
  setSessionEnvironment,
  attachSession,
  runSessionCommand,
} from "./tmux.ts";

let mockExec;
let restoreExec;

beforeEach(() => {
  mockExec = mock.fn();
  restoreExec = _setExecutor(mockExec);
});

afterEach(() => {
  restoreExec();
  mock.restoreAll();
});

// --- Helpers ---

function makeExecError(stderr) {
  const err = new Error("Command failed");
  err.stderr = stderr;
  return err;
}

// --- Error classification (via public API) ---

describe("getSessionState", () => {
  it("returns running: true when has-session succeeds", () => {
    mockExec.mock.mockImplementation(() => "");
    const result = getSessionState("my-session");
    assert.deepStrictEqual(result, { running: true, reason: null });
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], [
      "has-session",
      "-t",
      "my-session",
    ]);
  });

  it('returns SESSION_NOT_FOUND for "can\'t find session"', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("can't find session: my-session");
    });
    const result = getSessionState("my-session");
    assert.deepStrictEqual(result, { running: false, reason: "SESSION_NOT_FOUND" });
  });

  it('returns TMUX_UNAVAILABLE for "connection refused"', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("error connecting to /tmp/tmux-1000/default (connection refused)");
    });
    const result = getSessionState("my-session");
    assert.deepStrictEqual(result, { running: false, reason: "TMUX_UNAVAILABLE" });
  });

  it('returns TMUX_UNAVAILABLE for "no server running"', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("no server running on /tmp/tmux-1000/default");
    });
    const result = getSessionState("my-session");
    assert.deepStrictEqual(result, { running: false, reason: "TMUX_UNAVAILABLE" });
  });

  it("throws for unknown errors", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("something totally unexpected");
    });
    assert.throws(
      () => getSessionState("my-session"),
      (err) => err instanceof TmuxError && err.code === "TMUX_ERROR",
    );
  });
});

describe("hasSession", () => {
  it("returns true when session exists", () => {
    mockExec.mock.mockImplementation(() => "");
    assert.strictEqual(hasSession("proj"), true);
  });

  it("returns false for SESSION_NOT_FOUND", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("can't find session: proj");
    });
    assert.strictEqual(hasSession("proj"), false);
  });

  it("returns false for TMUX_UNAVAILABLE", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("no server running on /tmp/tmux-1000/default");
    });
    assert.strictEqual(hasSession("proj"), false);
  });

  it("throws for unknown errors", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("unexpected failure");
    });
    assert.throws(
      () => hasSession("proj"),
      (err) => err instanceof TmuxError && err.code === "TMUX_ERROR",
    );
  });
});

describe("killSession", () => {
  it("returns stopped: true when kill succeeds", () => {
    mockExec.mock.mockImplementation(() => "");
    const result = killSession("proj");
    assert.deepStrictEqual(result, { stopped: true, reason: null });
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], ["kill-session", "-t", "proj"]);
  });

  it("returns stopped: false for missing session", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("can't find session: proj");
    });
    const result = killSession("proj");
    assert.deepStrictEqual(result, { stopped: false, reason: "SESSION_NOT_FOUND" });
  });

  it("returns stopped: false for unavailable tmux", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("failed to connect to server");
    });
    const result = killSession("proj");
    assert.deepStrictEqual(result, { stopped: false, reason: "TMUX_UNAVAILABLE" });
  });

  it("throws for unknown errors", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("disk error");
    });
    assert.throws(
      () => killSession("proj"),
      (err) => err instanceof TmuxError && err.code === "TMUX_ERROR",
    );
  });
});

// --- listPanes ---

describe("listPanes", () => {
  it("parses multi-pane output correctly", () => {
    mockExec.mock.mockImplementation(() => "0|Editor|120|40|1\n1|Shell|80|40|0\n");
    const panes = listPanes("proj");
    assert.deepStrictEqual(panes, [
      { index: 0, title: "Editor", width: 120, height: 40, active: true },
      { index: 1, title: "Shell", width: 80, height: 40, active: false },
    ]);
  });

  it("returns empty array for empty output", () => {
    mockExec.mock.mockImplementation(() => "  \n");
    const panes = listPanes("proj");
    assert.deepStrictEqual(panes, []);
  });

  it("handles pane titles containing pipe characters", () => {
    // The split("|") will split on the first pipe in the title, causing misparse.
    // This documents the current behavior — titles with pipes are truncated.
    mockExec.mock.mockImplementation(() => "0|A|B|120|40|0\n");
    const panes = listPanes("proj");
    // With pipe in title, index=0, title="A", width=NaN (from "B"), ...
    assert.strictEqual(panes[0].index, 0);
    assert.strictEqual(panes[0].title, "A");
  });
});

// --- createDetachedSession ---

describe("createDetachedSession", () => {
  it("returns trimmed pane ID", () => {
    mockExec.mock.mockImplementation(() => "  %0\n");
    const id = createDetachedSession("proj", "/workspace");
    assert.strictEqual(id, "%0");
  });

  it("uses default dimensions when not specified", () => {
    mockExec.mock.mockImplementation(() => "%0\n");
    createDetachedSession("proj", "/workspace");
    const args = mockExec.mock.calls[0].arguments[1];
    assert.ok(args.includes("200")); // default cols
    assert.ok(args.includes("50")); // default lines
  });

  it("passes custom dimensions", () => {
    mockExec.mock.mockImplementation(() => "%0\n");
    createDetachedSession("proj", "/workspace", { cols: 300, lines: 80 });
    const args = mockExec.mock.calls[0].arguments[1];
    assert.ok(args.includes("300"));
    assert.ok(args.includes("80"));
  });
});

// --- splitPane ---

describe("splitPane", () => {
  it("uses -v for vertical direction", () => {
    mockExec.mock.mockImplementation(() => "%1\n");
    splitPane("%0", "vertical", "/workspace", 30);
    const args = mockExec.mock.calls[0].arguments[1];
    assert.ok(args.includes("-v"));
    assert.ok(!args.includes("-h"));
  });

  it("uses -h for horizontal direction", () => {
    mockExec.mock.mockImplementation(() => "%2\n");
    splitPane("%0", "horizontal", "/workspace", 50);
    const args = mockExec.mock.calls[0].arguments[1];
    assert.ok(args.includes("-h"));
    assert.ok(!args.includes("-v"));
  });

  it("passes percent correctly", () => {
    mockExec.mock.mockImplementation(() => "%3\n");
    splitPane("%0", "vertical", "/workspace", 42);
    const args = mockExec.mock.calls[0].arguments[1];
    const pIdx = args.indexOf("-p");
    assert.strictEqual(args[pIdx + 1], "42");
  });

  it("returns trimmed pane ID", () => {
    mockExec.mock.mockImplementation(() => "  %5\n");
    const id = splitPane("%0", "vertical", "/workspace", 30);
    assert.strictEqual(id, "%5");
  });
});

// --- sendLiteral ---

describe("sendLiteral", () => {
  it("sends text with -l flag then Enter", () => {
    mockExec.mock.mockImplementation(() => "");
    sendLiteral("%0", "echo hello");
    assert.strictEqual(mockExec.mock.callCount(), 2);
    // First call: send-keys with -l and the text
    const firstArgs = mockExec.mock.calls[0].arguments[1];
    assert.deepStrictEqual(firstArgs, ["send-keys", "-t", "%0", "-l", "--", "echo hello"]);
    // Second call: send Enter
    const secondArgs = mockExec.mock.calls[1].arguments[1];
    assert.deepStrictEqual(secondArgs, ["send-keys", "-t", "%0", "Enter"]);
  });
});

// --- getSessionVariable / setSessionVariable ---

describe("getSessionVariable", () => {
  it("returns trimmed value when variable exists", () => {
    mockExec.mock.mockImplementation(() => "  some-value\n");
    const value = getSessionVariable("proj", "@my_var");
    assert.strictEqual(value, "some-value");
  });

  it("returns null when variable is empty", () => {
    mockExec.mock.mockImplementation(() => "\n");
    const value = getSessionVariable("proj", "@my_var");
    assert.strictEqual(value, null);
  });

  it("returns null when show-option throws", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("can't find session: proj");
    });
    const value = getSessionVariable("proj", "@my_var");
    assert.strictEqual(value, null);
  });
});

describe("setSessionVariable", () => {
  it("sets variable with correct args", () => {
    mockExec.mock.mockImplementation(() => "");
    setSessionVariable("proj", "@my_var", "hello");
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], [
      "set-option",
      "-t",
      "proj",
      "@my_var",
      "hello",
    ]);
  });
});

// --- startSessionMonitor / stopSessionMonitor ---

describe("startSessionMonitor", () => {
  it("spawns detached process and stores PID", () => {
    const fakeChild = { pid: 12345, unref: mock.fn() };
    const restoreSpawn = _setSpawner(mock.fn(() => fakeChild));

    mockExec.mock.mockImplementation(() => "");
    startSessionMonitor("proj", "/path/to/monitor.js");

    // Check spawn was called correctly
    assert.strictEqual(fakeChild.unref.mock.callCount(), 1);

    // Check PID was stored via set-option
    const setArgs = mockExec.mock.calls[0].arguments[1];
    assert.deepStrictEqual(setArgs, ["set-option", "-t", "proj", "@monitor_pid", "12345"]);

    restoreSpawn();
  });
});

describe("stopSessionMonitor", () => {
  it("kills process by stored PID", () => {
    mockExec.mock.mockImplementation(() => "  42\n");
    const origKill = process.kill;
    const killCalls = [];
    process.kill = (pid) => killCalls.push(pid);
    try {
      stopSessionMonitor("proj");
      assert.deepStrictEqual(killCalls, [42]);
    } finally {
      process.kill = origKill;
    }
  });

  it("handles missing PID gracefully", () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("can't find session: proj");
    });
    // Should not throw
    stopSessionMonitor("proj");
  });

  it("handles empty PID gracefully", () => {
    mockExec.mock.mockImplementation(() => "\n");
    // Should not throw (no pid to kill)
    stopSessionMonitor("proj");
  });
});

// --- Other public functions ---

describe("setPaneTitle", () => {
  it("calls select-pane with -T flag", () => {
    mockExec.mock.mockImplementation(() => "");
    setPaneTitle("%0", "My Pane");
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], [
      "select-pane",
      "-t",
      "%0",
      "-T",
      "My Pane",
    ]);
  });
});

describe("selectPane", () => {
  it("calls select-pane with target", () => {
    mockExec.mock.mockImplementation(() => "");
    selectPane("%2");
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], ["select-pane", "-t", "%2"]);
  });
});

describe("getPaneCurrentCommand", () => {
  it("returns trimmed command name", () => {
    mockExec.mock.mockImplementation(() => "  zsh\n");
    assert.strictEqual(getPaneCurrentCommand("%0"), "zsh");
  });
});

describe("setSessionEnvironment", () => {
  it("calls set-environment with correct args", () => {
    mockExec.mock.mockImplementation(() => "");
    setSessionEnvironment("proj", "PORT", 3000);
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], [
      "set-environment",
      "-t",
      "proj",
      "PORT",
      "3000",
    ]);
  });
});

describe("attachSession", () => {
  it("calls attach with correct args and stdio inherit", () => {
    mockExec.mock.mockImplementation(() => "");
    attachSession("proj");
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], ["attach", "-t", "proj"]);
    assert.strictEqual(mockExec.mock.calls[0].arguments[2].stdio, "inherit");
  });
});

describe("runSessionCommand", () => {
  it("passes args through to tmux", () => {
    mockExec.mock.mockImplementation(() => "");
    runSessionCommand(["resize-pane", "-t", "%0", "-x", "100"]);
    assert.deepStrictEqual(mockExec.mock.calls[0].arguments[1], [
      "resize-pane",
      "-t",
      "%0",
      "-x",
      "100",
    ]);
  });
});

// --- Debug logging ---

describe("debug logging", () => {
  it("logs to stderr when globalThis.__tmuxIdeVerbose is true", () => {
    const origVerbose = globalThis.__tmuxIdeVerbose;
    const stderrCalls = [];
    const origConsoleError = console.error;
    console.error = (...args) => stderrCalls.push(args.join(" "));

    globalThis.__tmuxIdeVerbose = true;
    mockExec.mock.mockImplementation(() => "");

    try {
      hasSession("test-session");
      assert.ok(stderrCalls.some((msg) => msg.includes("[tmux]")));
      assert.ok(stderrCalls.some((msg) => msg.includes("has-session")));
    } finally {
      globalThis.__tmuxIdeVerbose = origVerbose;
      console.error = origConsoleError;
    }
  });

  it("does not log when neither DEBUG nor verbose is set", () => {
    const origVerbose = globalThis.__tmuxIdeVerbose;
    const stderrCalls = [];
    const origConsoleError = console.error;
    console.error = (...args) => stderrCalls.push(args.join(" "));

    globalThis.__tmuxIdeVerbose = false;
    mockExec.mock.mockImplementation(() => "");

    try {
      hasSession("test-session");
      assert.strictEqual(stderrCalls.length, 0);
    } finally {
      globalThis.__tmuxIdeVerbose = origVerbose;
      console.error = origConsoleError;
    }
  });
});

// --- Error classification edge cases ---

describe("error classification", () => {
  it('classifies "can\'t find window" as SESSION_NOT_FOUND', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("can't find window: proj:0");
    });
    const result = getSessionState("proj");
    assert.deepStrictEqual(result, { running: false, reason: "SESSION_NOT_FOUND" });
  });

  it('classifies "unknown target" as SESSION_NOT_FOUND', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("unknown target: proj");
    });
    const result = getSessionState("proj");
    assert.deepStrictEqual(result, { running: false, reason: "SESSION_NOT_FOUND" });
  });

  it('classifies "failed to connect to server" as TMUX_UNAVAILABLE', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("failed to connect to server: /tmp/tmux-1000/default");
    });
    const result = getSessionState("proj");
    assert.deepStrictEqual(result, { running: false, reason: "TMUX_UNAVAILABLE" });
  });

  it('classifies "error connecting to" as TMUX_UNAVAILABLE', () => {
    mockExec.mock.mockImplementation(() => {
      throw makeExecError("error connecting to /tmp/tmux-1000/default");
    });
    const result = getSessionState("proj");
    assert.deepStrictEqual(result, { running: false, reason: "TMUX_UNAVAILABLE" });
  });

  it("handles Buffer stderr in error", () => {
    mockExec.mock.mockImplementation(() => {
      const err = new Error("Command failed");
      err.stderr = Buffer.from("can't find session: proj");
      throw err;
    });
    const result = getSessionState("proj");
    assert.deepStrictEqual(result, { running: false, reason: "SESSION_NOT_FOUND" });
  });

  it("falls back to error.message when stderr is empty", () => {
    mockExec.mock.mockImplementation(() => {
      const err = new Error("can't find session: proj");
      err.stderr = "";
      throw err;
    });
    const result = getSessionState("proj");
    assert.deepStrictEqual(result, { running: false, reason: "SESSION_NOT_FOUND" });
  });
});
```

## File: `src/lib/tmux.ts`
```typescript
import { execFileSync, spawn, type ExecFileSyncOptions } from "node:child_process";
import { TmuxError } from "./errors.ts";
import type { SessionState } from "../types.ts";

const DEBUG = process.env.TMUX_IDE_DEBUG === "1";

const SESSION_NOT_FOUND_PATTERNS = ["can't find session", "can't find window", "unknown target"];

const TMUX_UNAVAILABLE_PATTERNS = [
  "failed to connect to server",
  "no server running",
  "error connecting to",
  "connection refused",
];

export { TmuxError };

export function getSessionState(session: string): SessionState {
  try {
    runTmux(["has-session", "-t", session]);
    return { running: true, reason: null };
  } catch (error) {
    if (error instanceof TmuxError) {
      if (error.code === "SESSION_NOT_FOUND") {
        return { running: false, reason: "SESSION_NOT_FOUND" };
      }
      if (error.code === "TMUX_UNAVAILABLE") {
        return { running: false, reason: "TMUX_UNAVAILABLE" };
      }
    }
    throw error;
  }
}

export function attachSession(session: string): void {
  runTmux(["attach", "-t", session], { stdio: "inherit" });
}

export function hasSession(session: string): boolean {
  try {
    runTmux(["has-session", "-t", session]);
    return true;
  } catch (error) {
    if (
      error instanceof TmuxError &&
      (error.code === "SESSION_NOT_FOUND" || error.code === "TMUX_UNAVAILABLE")
    ) {
      return false;
    }
    throw error;
  }
}

export function killSession(session: string): { stopped: boolean; reason: string | null } {
  try {
    runTmux(["kill-session", "-t", session]);
    return { stopped: true, reason: null };
  } catch (error) {
    if (error instanceof TmuxError) {
      if (error.code === "SESSION_NOT_FOUND") {
        return { stopped: false, reason: "SESSION_NOT_FOUND" };
      }
      if (error.code === "TMUX_UNAVAILABLE") {
        return { stopped: false, reason: "TMUX_UNAVAILABLE" };
      }
    }
    throw error;
  }
}

export function listPanes(session: string) {
  const raw = (
    runTmux(
      [
        "list-panes",
        "-t",
        session,
        "-F",
        "#{pane_index}|#{pane_title}|#{pane_width}|#{pane_height}|#{pane_active}",
      ],
      { encoding: "utf-8" },
    ) as string
  ).trim();

  if (!raw) return [];

  return raw.split("\n").map((line) => {
    const [index, title, width, height, active] = line.split("|");
    return {
      index: Number.parseInt(index!, 10),
      title,
      width: Number.parseInt(width!, 10),
      height: Number.parseInt(height!, 10),
      active: active === "1",
    };
  });
}

export function createDetachedSession(
  session: string,
  cwd: string,
  { cols, lines }: { cols?: number; lines?: number } = {},
): string {
  return (
    runTmux(
      [
        "new-session",
        "-d",
        "-P",
        "-F",
        "#{pane_id}",
        "-s",
        session,
        "-c",
        cwd,
        "-x",
        String(cols ?? 200),
        "-y",
        String(lines ?? 50),
      ],
      { encoding: "utf-8" },
    ) as string
  ).trim();
}

export function setSessionEnvironment(session: string, key: string, value: string | number): void {
  runTmux(["set-environment", "-t", session, key, String(value)]);
}

export function splitPane(
  targetPane: string,
  direction: string,
  cwd: string,
  percent: number,
): string {
  return (
    runTmux(
      [
        "split-window",
        "-P",
        "-F",
        "#{pane_id}",
        "-t",
        targetPane,
        direction === "vertical" ? "-v" : "-h",
        "-c",
        cwd,
        "-p",
        String(percent),
      ],
      { encoding: "utf-8" },
    ) as string
  ).trim();
}

export function sendLiteral(targetPane: string, text: string): void {
  runTmux(["send-keys", "-t", targetPane, "-l", "--", text], { stdio: "inherit" });
  runTmux(["send-keys", "-t", targetPane, "Enter"], { stdio: "inherit" });
}

export function getPaneCurrentCommand(targetPane: string): string {
  return (
    runTmux(["display-message", "-p", "-t", targetPane, "#{pane_current_command}"], {
      encoding: "utf-8",
    }) as string
  ).trim();
}

export function selectPane(targetPane: string): void {
  runTmux(["select-pane", "-t", targetPane], { stdio: "inherit" });
}

export function setPaneTitle(targetPane: string, title: string): void {
  runTmux(["select-pane", "-t", targetPane, "-T", title], { stdio: "inherit" });
}

export function runSessionCommand(args: string[]): void {
  runTmux(args, { stdio: "inherit" });
}

export function startSessionMonitor(session: string, monitorScript: string): void {
  const child = _spawner("node", [monitorScript, session], {
    detached: true,
    stdio: "ignore",
  });
  child.unref();
  // Store PID as tmux session variable for later cleanup
  runTmux(["set-option", "-t", session, "@monitor_pid", String(child.pid)]);
}

export function stopSessionMonitor(session: string): void {
  try {
    const pid = (
      runTmux(["show-option", "-gqvt", session, "@monitor_pid"], {
        encoding: "utf-8",
      }) as string
    ).trim();
    if (pid) process.kill(parseInt(pid, 10));
  } catch {
    /* session or process already gone */
  }
}

export function getSessionVariable(session: string, name: string): string | null {
  try {
    const raw = runTmux(["show-option", "-gqvt", session, name], {
      encoding: "utf-8",
    }) as string;
    return raw.trim() || null;
  } catch {
    return null;
  }
}

export function setSessionVariable(session: string, name: string, value: string): void {
  runTmux(["set-option", "-t", session, name, value]);
}

type Executor = typeof execFileSync;
type Spawner = typeof spawn;

let _executor: Executor = execFileSync;
let _spawner: Spawner = spawn;

/** @internal Replace the executor for testing. Returns a restore function. */
export function _setExecutor(fn: Executor): () => void {
  const prev = _executor;
  _executor = fn;
  return () => {
    _executor = prev;
  };
}

/** @internal Replace the spawner for testing. Returns a restore function. */
export function _setSpawner(fn: Spawner): () => void {
  const prev = _spawner;
  _spawner = fn;
  return () => {
    _spawner = prev;
  };
}

declare global {
  var __tmuxIdeVerbose: boolean | undefined;
}

function runTmux(args: string[], options: ExecFileSyncOptions = {}) {
  if (DEBUG || globalThis.__tmuxIdeVerbose) {
    console.error(`  [tmux] ${args.join(" ")}`);
  }

  const execOptions: ExecFileSyncOptions = {
    stdio: ["ignore", "pipe", "pipe"],
    ...options,
  };

  try {
    return _executor("tmux", args, execOptions);
  } catch (error) {
    throw classifyTmuxError(error);
  }
}

function classifyTmuxError(error: unknown): TmuxError {
  const detail = getErrorDetail(error).toLowerCase();

  if (SESSION_NOT_FOUND_PATTERNS.some((pattern) => detail.includes(pattern))) {
    return new TmuxError("tmux session was not found", "SESSION_NOT_FOUND", {
      cause: error as Error,
    });
  }

  if (TMUX_UNAVAILABLE_PATTERNS.some((pattern) => detail.includes(pattern))) {
    return new TmuxError("tmux is unavailable or its socket is inaccessible", "TMUX_UNAVAILABLE", {
      cause: error as Error,
    });
  }

  return new TmuxError("tmux command failed", "TMUX_ERROR", { cause: error as Error });
}

function getErrorDetail(error: unknown): string {
  const stderr = (error as { stderr?: string | Buffer })?.stderr;
  if (typeof stderr === "string" && stderr.length > 0) return stderr;
  if (Buffer.isBuffer(stderr) && stderr.length > 0) return stderr.toString("utf-8");
  return (error as Error)?.message ?? "";
}
```

## File: `src/lib/yaml-io.ts`
```typescript
import { readFileSync, writeFileSync } from "node:fs";
import { resolve, basename } from "node:path";
import yaml from "js-yaml";
import type { IdeConfig } from "../types.ts";

export function readConfig(dir: string): { config: IdeConfig; configPath: string } {
  const configPath = resolve(dir, "ide.yml");
  const raw = readFileSync(configPath, "utf-8");
  const config = yaml.load(raw) as IdeConfig;
  return { config, configPath };
}

export function writeConfig(dir: string, config: IdeConfig): string {
  const configPath = resolve(dir, "ide.yml");
  const out = yaml.dump(config, { lineWidth: -1, noRefs: true, quotingType: '"' });
  writeFileSync(configPath, out);
  return configPath;
}

export function getSessionName(dir: string): { name: string; source: "config" | "fallback" } {
  try {
    const { config } = readConfig(dir);
    return { name: config.name ?? basename(dir), source: config.name ? "config" : "fallback" };
  } catch {
    return { name: basename(dir), source: "fallback" };
  }
}
```

## File: `templates/agent-team-monorepo.yml`
```yaml
name: my-monorepo

team:
  name: my-monorepo

rows:
  - size: 70%
    panes:
      - title: Lead — Architect
        command: claude
        role: lead
        focus: true
      - title: Frontend Agent
        command: claude
        role: teammate
        task: "Work on the frontend application"
        dir: apps/web
      - title: Backend Agent
        command: claude
        role: teammate
        task: "Work on the backend services"
        dir: apps/api

  - panes:
      - title: Frontend
        command: pnpm dev
        dir: apps/web
      - title: Backend
        command: pnpm dev
        dir: apps/api
      - title: Shell
```

## File: `templates/agent-team-nextjs.yml`
```yaml
name: my-app

team:
  name: my-app

before: pnpm install

rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead
        focus: true
      - title: Frontend
        command: claude
        role: teammate
        task: "Work on React components and pages"
      - title: Backend
        command: claude
        role: teammate
        task: "Work on API routes and server logic"

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Shell
```

## File: `templates/agent-team.yml`
```yaml
name: my-project

team:
  name: my-project

rows:
  - size: 70%
    panes:
      - title: Lead
        command: claude
        role: lead
        focus: true
      - title: Teammate 1
        command: claude
        role: teammate
      - title: Teammate 2
        command: claude
        role: teammate

  - panes:
      - title: Dev Server
        # command: npm run dev
      - title: Shell
```

## File: `templates/convex.yml`
```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude
      - title: Claude 3 — explore
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Convex
        command: npx convex dev
      - title: Shell
        focus: true
```

## File: `templates/default.yml`
```yaml
name: my-project

# before: npm install  # optional pre-launch hook

rows:
  - size: 70%
    panes:
      - title: Claude 1
        command: claude
      - title: Claude 2
        command: claude

  - panes:
      - title: Dev Server
        # command: npm run dev
        # dir: apps/web       # per-pane working directory
        # env:                 # per-pane environment variables
        #   PORT: 3000
      - title: Shell
        # focus: true          # give this pane initial focus
```

## File: `templates/go.yml`
```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude

  - panes:
      - title: Go
        command: go run .
      - title: Shell
        focus: true
```

## File: `templates/nextjs.yml`
```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude
      - title: Claude 3 — explore
        command: claude

  - panes:
      - title: Next.js
        command: pnpm dev
      - title: Shell
        focus: true
```

## File: `templates/python.yml`
```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude

  - panes:
      - title: Server
        # command: uvicorn main:app --reload
      - title: Shell
        focus: true
```

## File: `templates/vite.yml`
```yaml
name: my-app

rows:
  - size: 70%
    panes:
      - title: Claude 1 — feature
        command: claude
      - title: Claude 2 — review
        command: claude

  - panes:
      - title: Vite
        command: pnpm dev
      - title: Shell
        focus: true
```

