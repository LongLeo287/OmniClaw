---
id: openspec
type: knowledge
owner: OA_Triage
---
# openspec
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@fission-ai/openspec",
  "version": "1.2.0",
  "description": "AI-native system for spec-driven development",
  "keywords": [
    "openspec",
    "specs",
    "cli",
    "ai",
    "development"
  ],
  "homepage": "https://github.com/Fission-AI/OpenSpec",
  "repository": {
    "type": "git",
    "url": "https://github.com/Fission-AI/OpenSpec"
  },
  "license": "MIT",
  "author": "OpenSpec Contributors",
  "type": "module",
  "publishConfig": {
    "access": "public"
  },
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "default": "./dist/index.js"
    }
  },
  "bin": {
    "openspec": "./bin/openspec.js"
  },
  "files": [
    "dist",
    "bin",
    "schemas",
    "scripts/postinstall.js",
    "!dist/**/*.test.js",
    "!dist/**/__tests__",
    "!dist/**/*.map"
  ],
  "scripts": {
    "lint": "eslint src/",
    "build": "node build.js",
    "dev": "tsc --watch",
    "dev:cli": "pnpm build && node bin/openspec.js",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage",
    "test:postinstall": "node scripts/postinstall.js",
    "prepare": "pnpm run build",
    "prepublishOnly": "pnpm run build",
    "postinstall": "node scripts/postinstall.js",
    "check:pack-version": "node scripts/pack-version-check.mjs",
    "release": "pnpm run release:ci",
    "release:ci": "pnpm run check:pack-version && pnpm exec changeset publish",
    "changeset": "changeset"
  },
  "engines": {
    "node": ">=20.19.0"
  },
  "devDependencies": {
    "@changesets/changelog-github": "^0.5.2",
    "@changesets/cli": "^2.27.7",
    "@types/node": "^24.2.0",
    "@vitest/ui": "^3.2.4",
    "eslint": "^9.39.2",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.50.1",
    "vitest": "^3.2.4"
  },
  "dependencies": {
    "@inquirer/core": "^10.2.2",
    "@inquirer/prompts": "^7.8.0",
    "chalk": "^5.5.0",
    "commander": "^14.0.0",
    "fast-glob": "^3.3.3",
    "ora": "^8.2.0",
    "posthog-node": "^5.20.0",
    "yaml": "^2.8.2",
    "zod": "^4.0.17"
  }
}

```

### File: README.md
```md
<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec">
    <picture>
      <source srcset="assets/openspec_bg.png">
      <img src="assets/openspec_bg.png" alt="OpenSpec logo">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://www.npmjs.com/package/@fission-ai/openspec"><img alt="npm version" src="https://img.shields.io/npm/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" /></a>
  <a href="https://discord.gg/YctCnvvshC"><img alt="Discord" src="https://img.shields.io/discord/1411657095639601154?style=flat-square&logo=discord&logoColor=white&label=Discord&suffix=%20online" /></a>
</p>

<details>
<summary><strong>The most loved spec framework.</strong></summary>

[![Stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=Stars)](https://github.com/Fission-AI/OpenSpec/stargazers)
[![Downloads](https://img.shields.io/npm/dm/@fission-ai/openspec?style=flat-square&label=Downloads/mo)](https://www.npmjs.com/package/@fission-ai/openspec)
[![Contributors](https://img.shields.io/github/contributors/Fission-AI/OpenSpec?style=flat-square&label=Contributors)](https://github.com/Fission-AI/OpenSpec/graphs/contributors)

</details>
<p></p>
Our philosophy:

```text
→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
→ scalable from personal projects to enterprises
```

> [!TIP]
> **New workflow now available!** We've rebuilt OpenSpec with a new artifact-guided workflow.
>
> Run `/opsx:propose "your idea"` to get started. → [Learn more here](docs/opsx.md)

<p align="center">
  Follow <a href="https://x.com/0xTab">@0xTab on X</a> for updates · Join the <a href="https://discord.gg/YctCnvvshC">OpenSpec Discord</a> for help and questions.
</p>

### Teams

Using OpenSpec in a team? [Email here](mailto:teams@openspec.dev) for access to our Slack channel.

<!-- TODO: Add GIF demo of /opsx:propose → /opsx:archive workflow -->

## See it in action

```text
You: /opsx:propose add-dark-mode
AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/       — requirements and scenarios
     ✓ design.md    — technical approach
     ✓ tasks.md     — implementation checklist
     Ready for implementation!

You: /opsx:apply
AI:  Implementing tasks...
     ✓ 1.1 Add theme context provider
     ✓ 1.2 Create toggle component
     ✓ 2.1 Add CSS variables
     ✓ 2.2 Wire up localStorage
     All tasks complete!

You: /opsx:archive
AI:  Archived to openspec/changes/archive/2025-01-23-add-dark-mode/
     Specs updated. Ready for the next feature.
```

<details>
<summary><strong>OpenSpec Dashboard</strong></summary>

<p align="center">
  <img src="assets/openspec_dashboard.png" alt="OpenSpec dashboard preview" width="90%">
</p>

</details>

## Quick Start

**Requires Node.js 20.19.0 or higher.**

Install OpenSpec globally:

```bash
npm install -g @fission-ai/openspec@latest
```

Then navigate to your project directory and initialize:

```bash
cd your-project
openspec init
```

Now tell your AI: `/opsx:propose <what-you-want-to-build>`

If you want the expanded workflow (`/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:sync`, `/opsx:bulk-archive`, `/opsx:onboard`), select it with `openspec config profile` and apply with `openspec update`.

> [!NOTE]
> Not sure if your tool is supported? [View the full list](docs/supported-tools.md) – we support 20+ tools and growing.
>
> Also works with pnpm, yarn, bun, and nix. [See installation options](docs/installation.md).

## Docs

→ **[Getting Started](docs/getting-started.md)**: first steps<br>
→ **[Workflows](docs/workflows.md)**: combos and patterns<br>
→ **[Commands](docs/commands.md)**: slash commands & skills<br>
→ **[CLI](docs/cli.md)**: terminal reference<br>
→ **[Supported Tools](docs/supported-tools.md)**: tool integrations & install paths<br>
→ **[Concepts](docs/concepts.md)**: how it all fits<br>
→ **[Multi-Language](docs/multi-language.md)**: multi-language support<br>
→ **[Customization](docs/customization.md)**: make it yours


## Why OpenSpec?

AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightweight spec layer so you agree on what to build before any code is written.

- **Agree before you build** — human and AI align on specs before code gets written
- **Stay organized** — each change gets its own folder with proposal, specs, design, and tasks
- **Work fluidly** — update any artifact anytime, no rigid phase gates
- **Use your tools** — works with 20+ AI assistants via slash commands

### How we compare

**vs. [Spec Kit](https://github.com/github/spec-kit)** (GitHub) — Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely.

**vs. [Kiro](https://kiro.dev)** (AWS) — Powerful but you're locked into their IDE and limited to Claude models. OpenSpec works with the tools you already use.

**vs. nothing** — AI coding without specs means vague prompts and unpredictable results. OpenSpec brings predictability without the ceremony.

## Updating OpenSpec

**Upgrade the package**

```bash
npm install -g @fission-ai/openspec@latest
```

**Refresh agent instructions**

Run this inside each project to regenerate AI guidance and ensure the latest slash commands are active:

```bash
openspec update
```

## Usage Notes

**Model selection**: OpenSpec works best with high-reasoning models. We recommend Opus 4.5 and GPT 5.2 for both planning and implementation.

**Context hygiene**: OpenSpec benefits from a clean context window. Clear your context before starting implementation and maintain good context hygiene throughout your session.

## Contributing

**Small fixes** — Bug fixes, typo corrections, and minor improvements can be submitted directly as PRs.

**Larger changes** — For new features, significant refactors, or architectural changes, please submit an OpenSpec change proposal first so we can align on intent and goals before implementation begins.

When writing proposals, keep the OpenSpec philosophy in mind: we serve a wide variety of users across different coding agents, models, and use cases. Changes should work well for everyone.

**AI-generated code is welcome** — as long as it's been tested and verified. PRs containing AI-generated code should mention the coding agent and model used (e.g., "Generated with Claude Code using claude-opus-4-5-20251101").

### Development

- Install dependencies: `pnpm install`
- Build: `pnpm run build`
- Test: `pnpm test`
- Develop CLI locally: `pnpm run dev` or `pnpm run dev:cli`
- Conventional commits (one-line): `type(scope): subject`

## Other

<details>
<summary><strong>Telemetry</strong></summary>

OpenSpec collects anonymous usage stats.

We collect only command names and version to understand usage patterns. No arguments, paths, content, or PII. Automatically disabled in CI.

**Opt-out:** `export OPENSPEC_TELEMETRY=0` or `export DO_NOT_TRACK=1`

</details>

<details>
<summary><strong>Maintainers & Advisors</strong></summary>

See [MAINTAINERS.md](MAINTAINERS.md) for the list of core maintainers and advisors who help guide the project.

</details>



## License

MIT

```

### File: .changeset\README.md
```md
# Changesets

This directory is managed by [Changesets](https://github.com/changesets/changesets).

## Quick Start

```bash
pnpm changeset
```

Follow the prompts to select version bump type and describe your changes.

## Workflow

1. **Add a changeset** — Run `pnpm changeset` locally before or after your PR
2. **Version PR** — CI opens/updates a "Version Packages" PR when changesets merge to main
3. **Release** — Merging the Version PR triggers npm publish and GitHub Release

> **Note:** Contributors only need to run `pnpm changeset`. Versioning (`changeset version`) and publishing happen automatically in CI.

## Template

Use this structure for your changeset content:

```markdown
---
"@fission-ai/openspec": patch
---

### New Features

- **Feature name** — What users can now do

### Bug Fixes

- Fixed issue where X happened when Y

### Breaking Changes

- `oldMethod()` has been removed, use `newMethod()` instead

### Deprecations

- `legacyOption` is deprecated and will be removed in v2.0

### Other

- Internal refactoring of X for better performance
```

Include only the sections relevant to your change.

## Version Bump Guide

| Type | When to use | Example |
|------|-------------|---------|
| `patch` | Bug fixes, small improvements | Fixed crash when config missing |
| `minor` | New features, non-breaking additions | Added `--verbose` flag |
| `major` | Breaking changes, removed features | Renamed `init` to `setup` |

## When to Create a Changeset

**Create one for:**
- New features or commands
- Bug fixes that affect users
- Breaking changes or deprecations
- Performance improvements users would notice

**Skip for:**
- Documentation-only changes
- Test additions/fixes
- Internal refactoring with no user impact
- CI/tooling changes

## Writing Good Descriptions

**Do:** Write for users, not developers
```markdown
- **Shell completions** — Tab completion now available for Bash, Fish, and PowerShell
```

**Don't:** Write implementation details
```markdown
- Added ShellCompletionGenerator class with Bash/Fish/PowerShell subclasses
```

**Do:** Explain the impact
```markdown
- Fixed config loading to respect `XDG_CONFIG_HOME` on Linux
```

**Don't:** Just reference the fix
```markdown
- Fixed #123
```

```

### File: .devcontainer\README.md
```md
# Dev Container Setup

This directory contains the VS Code dev container configuration for OpenSpec development.

## What's Included

- **Node.js 20 LTS** (>=20.19.0) - TypeScript/JavaScript runtime
- **pnpm** - Fast, disk space efficient package manager
- **Git + GitHub CLI** - Version control tools
- **VS Code Extensions**:
  - ESLint & Prettier for code quality
  - Vitest Explorer for running tests
  - GitLens for enhanced git integration
  - Error Lens for inline error highlighting
  - Code Spell Checker
  - Path IntelliSense

## How to Use

### First Time Setup

1. **Install Prerequisites** (on your local machine):
   - [VS Code](https://code.visualstudio.com/)
   - [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in Container**:
   - Open this project in VS Code
   - You'll see a notification: "Folder contains a Dev Container configuration file"
   - Click "Reopen in Container"

   OR

   - Open Command Palette (`Cmd/Ctrl+Shift+P`)
   - Type "Dev Containers: Reopen in Container"
   - Press Enter

3. **Wait for Setup**:
   - The container will build (first time takes a few minutes)
   - `pnpm install` runs automatically via `postCreateCommand`
   - All extensions install automatically

### Daily Development

Once set up, the container preserves your development environment:

```bash
# Run development build
pnpm run dev

# Run CLI in development
pnpm run dev:cli

# Run tests
pnpm test

# Run tests in watch mode
pnpm test:watch

# Build the project
pnpm run build
```

### SSH Keys

Your SSH keys are mounted read-only from `~/.ssh`, so git operations work seamlessly with GitHub/GitLab.

### Rebuilding the Container

If you modify `.devcontainer/devcontainer.json`:
- Command Palette → "Dev Containers: Rebuild Container"

## Benefits

- No need to install Node.js or pnpm on your local machine
- Consistent development environment across team members
- Isolated from other Node.js projects on your machine
- All dependencies and tools containerized
- Easy onboarding for new developers

## Troubleshooting

**Container won't build:**
- Ensure Docker Desktop is running
- Check Docker has enough memory allocated (recommend 4GB+)

**Extensions not appearing:**
- Rebuild the container: "Dev Containers: Rebuild Container"

**Permission issues:**
- The container runs as the `node` user (non-root)
- Files created in the container are owned by this user

```

### File: scripts\README.md
```md
# OpenSpec Scripts

Utility scripts for OpenSpec maintenance and development.

## update-flake.sh

Updates `flake.nix` pnpm dependency hash automatically.

**When to use**: After updating dependencies (`pnpm install`, `pnpm update`).

**Usage**:
```bash
./scripts/update-flake.sh
```

**What it does**:
1. Reads version from `package.json` (dynamically used by `flake.nix`)
2. Automatically determines the correct pnpm dependency hash
3. Updates the hash in `flake.nix`
4. Verifies the build succeeds

**Example workflow**:
```bash
# After dependency updates
pnpm install
./scripts/update-flake.sh
git add flake.nix
git commit -m "chore: update flake.nix dependency hash"
```

## postinstall.js

Post-installation script that runs after package installation.

## pack-version-check.mjs

Validates package version consistency before publishing.

```

### File: .github\workflows\README.md
```md
# Github Workflows

## Testing CI Locally

Test GitHub Actions workflows locally using [act](https://nektosact.com/):

```bash
# Test all PR checks
act pull_request

# Test specific job
act pull_request -j nix-flake-validate

# Dry run to see what would execute
act pull_request --dryrun
```

The `.actrc` file configures act to use the appropriate Docker image.



```

### File: .coderabbit.yaml
```yaml
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
# Minimal configuration for getting started
language: "en-US"
reviews:
  profile: "chill"
  high_level_summary: true
  auto_review:
    enabled: true
    drafts: false
    base_branches:
      - ".*"
```

### File: AGENTS.md
```md

```

### File: build.js
```js
#!/usr/bin/env node

import { execFileSync } from 'child_process';
import { existsSync, rmSync } from 'fs';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);

const runTsc = (args = []) => {
  const tscPath = require.resolve('typescript/bin/tsc');
  execFileSync(process.execPath, [tscPath, ...args], { stdio: 'inherit' });
};

console.log('🔨 Building OpenSpec...\n');

// Clean dist directory
if (existsSync('dist')) {
  console.log('Cleaning dist directory...');
  rmSync('dist', { recursive: true, force: true });
}

// Run TypeScript compiler (use local version explicitly)
console.log('Compiling TypeScript...');
try {
  runTsc(['--version']);
  runTsc();
  console.log('\n✅ Build completed successfully!');
} catch (error) {
  console.error('\n❌ Build failed!');
  process.exit(1);
}

```

### File: CHANGELOG.md
```md
# @fission-ai/openspec

## 1.2.0

### Minor Changes

- [#747](https://github.com/Fission-AI/OpenSpec/pull/747) [`1e94443`](https://github.com/Fission-AI/OpenSpec/commit/1e94443a3551b228eecbc89e95d96d3b9600a192) Thanks [@TabishB](https://github.com/TabishB)! - ### New Features

  - **Profile system** — Choose between `core` (4 essential workflows) and `custom` (pick any subset) profiles to control which skills get installed. Manage profiles with the new `openspec config profile` command
  - **Propose workflow** — New one-step workflow creates a complete change proposal with design, specs, and tasks from a single request — no need to run `new` then `ff` separately
  - **AI tool auto-detection** — `openspec init` now scans your project for existing tool directories (`.claude/`, `.cursor/`, etc.) and pre-selects detected tools
  - **Pi (pi.dev) support** — Pi coding agent is now a supported tool with prompt and skill generation
  - **Kiro support** — AWS Kiro IDE is now a supported tool with prompt and skill generation
  - **Sync prunes deselected workflows** — `openspec update` now removes command files and skill directories for workflows you've deselected, keeping your project clean
  - **Config drift warning** — `openspec config list` warns when global config is out of sync with the current project

  ### Bug Fixes

  - Fixed onboard preflight giving a false "not initialized" error on freshly initialized projects
  - Fixed archive workflow stopping mid-way when syncing — it now properly resumes after sync completes
  - Added Windows PowerShell alternatives for onboard shell commands

## 1.1.1

### Patch Changes

- [#627](https://github.com/Fission-AI/OpenSpec/pull/627) [`afb73cf`](https://github.com/Fission-AI/OpenSpec/commit/afb73cf9ec59c6f8b26d0c538c0218c203ba3c56) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - **OpenCode command references** — Command references in generated files now use the correct `/opsx-` hyphen format instead of `/opsx:` colon format, ensuring commands work properly in OpenCode

## 1.1.0

### Minor Changes

- [#625](https://github.com/Fission-AI/OpenSpec/pull/625) [`53081fb`](https://github.com/Fission-AI/OpenSpec/commit/53081fb2a26ec66d2950ae0474b9a56cbc5b5a76) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - **Codex global path support** — Codex adapter now resolves global paths correctly, fixing workflow file generation when run outside the project directory (#622)
  - **Archive operations on cross-device or restricted paths** — Archive now falls back to copy+remove when rename fails with EPERM or EXDEV errors, fixing failures on networked/external drives (#605)
  - **Slash command hints in workflow messages** — Workflow completion messages now display helpful slash command hints for next steps (#603)
  - **Windsurf workflow file path** — Updated Windsurf adapter to use the correct `workflows` directory instead of the legacy `commands` path (#610)

### Patch Changes

- [#550](https://github.com/Fission-AI/OpenSpec/pull/550) [`86d2e04`](https://github.com/Fission-AI/OpenSpec/commit/86d2e04cae76a999dbd1b4571f52fa720036be0c) Thanks [@jerome-benoit](https://github.com/jerome-benoit)! - ### Improvements

  - **Nix flake maintenance** — Version now read dynamically from package.json, reducing manual sync issues
  - **Nix build optimization** — Source filtering excludes node_modules and artifacts, improving build times
  - **update-flake.sh script** — Detects when hash is already correct, skipping unnecessary rebuilds

  ### Other

  - Updated Nix CI actions to latest versions (nix-installer v21, magic-nix-cache v13)

## 1.0.2

### Patch Changes

- [#596](https://github.com/Fission-AI/OpenSpec/pull/596) [`e91568d`](https://github.com/Fission-AI/OpenSpec/commit/e91568deb948073f3e9d9bb2d2ab5bf8080d6cf4) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - Clarified spec naming convention — Specs should be named after capabilities (`specs/<capability>/spec.md`), not changes
  - Fixed task checkbox format guidance — Tasks now clearly require `- [ ]` checkbox format for apply phase tracking

## 1.0.1

### Patch Changes

- [#587](https://github.com/Fission-AI/OpenSpec/pull/587) [`943e0d4`](https://github.com/Fission-AI/OpenSpec/commit/943e0d41026d034de66b9442d1276c01b293eb2b) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - Fixed incorrect archive path in onboarding documentation — the template now shows the correct path `openspec/changes/archive/YYYY-MM-DD-<name>/` instead of the incorrect `openspec/archive/YYYY-MM-DD--<name>/`

## 1.0.0

### Major Changes

- [#578](https://github.com/Fission-AI/OpenSpec/pull/578) [`0cc9d90`](https://github.com/Fission-AI/OpenSpec/commit/0cc9d9025af367faa1688a7b2606a2549053cd3f) Thanks [@TabishB](https://github.com/TabishB)! - ## OpenSpec 1.0 — The OPSX Release

  The workflow has been rebuilt from the ground up. OPSX replaces the old phase-locked `/openspec:*` commands with an action-based system where AI understands what artifacts exist, what's ready to create, and what each action unlocks.

  ### Breaking Changes

  - **Old commands removed** — `/openspec:proposal`, `/openspec:apply`, and `/openspec:archive` no longer exist
  - **Config files removed** — Tool-specific instruction files (`CLAUDE.md`, `.cursorrules`, `AGENTS.md`, `project.md`) are no longer generated
  - **Migration** — Run `openspec init` to upgrade. Legacy artifacts are detected and cleaned up with confirmation.

  ### From Static Prompts to Dynamic Instructions

  **Before:** AI received the same static instructions every time, regardless of project state.

  **Now:** Instructions are dynamically assembled from three layers:

  1. **Context** — Project background from `config.yaml` (tech stack, conventions)
  2. **Rules** — Artifact-specific constraints (e.g., "propose spike tasks for unknowns")
  3. **Template** — The actual structure for the output file

  AI queries the CLI for real-time state: which artifacts exist, what's ready to create, what dependencies are satisfied, and what each action unlocks.

  ### From Phase-Locked to Action-Based

  **Before:** Linear workflow — proposal → apply → archive. Couldn't easily go back or iterate.

  **Now:** Flexible actions on a change. Edit any artifact anytime. The artifact graph tracks state automatically.

  | Command              | What it does                                         |
  | -------------------- | ---------------------------------------------------- |
  | `/opsx:explore`      | Think through ideas before committing to a change    |
  | `/opsx:new`          | Start a new change                                   |
  | `/opsx:continue`     | Create one artifact at a time (step-through)         |
  | `/opsx:ff`           | Create all planning artifacts at once (fast-forward) |
  | `/opsx:apply`        | Implement tasks                                      |
  | `/opsx:verify`       | Validate implementation matches artifacts            |
  | `/opsx:sync`         | Sync delta specs to main specs                       |
  | `/opsx:archive`      | Archive completed change                             |
  | `/opsx:bulk-archive` | Archive multiple changes with conflict detection     |
  | `/opsx:onboard`      | Guided 15-minute walkthrough of complete workflow    |

  ### From Text Merging to Semantic Spec Syncing

  **Before:** Spec updates required manual merging or wholesale file replacement.

  **Now:** Delta specs use semantic markers that AI understands:

  - `## ADDED Requirements` — New requirements to add
  - `## MODIFIED Requirements` — Partial updates (add scenario without copying existing ones)
  - `## REMOVED Requirements` — Delete with reason and migration notes
  - `## RENAMED Requirements` — Rename preserving content

  Archive parses these at the requirement level, not brittle header matching.

  ### From Scattered Files to Agent Skills

  **Before:** 8+ config files at project root + slash commands scattered across 21 tool-specific locations with different formats.

  **Now:** Single `.claude/skills/` directory with YAML-fronted markdown files. Auto-detected by Claude Code, Cursor, Windsurf. Cross-editor compatible.

  ### New Features

  - **Onboarding skill** — `/opsx:onboard` walks new users through their first complete change with codebase-aware task suggestions and step-by-step narration (11 phases, ~15 minutes)

  - **21 AI tools supported** — Claude Code, Cursor, Windsurf, Continue, Gemini CLI, GitHub Copilot, Amazon Q, Cline, RooCode, Kilo Code, Auggie, CodeBuddy, Qoder, Qwen, CoStrict, Crush, Factory, OpenCode, Antigravity, iFlow, and Codex

  - **Interactive setup** — `openspec init` shows animated welcome screen and searchable multi-select for choosing tools. Pre-selects already-configured tools for easy refresh.

  - **Customizable schemas** — Define custom artifact workflows in `openspec/schemas/` without touching package code. Teams can share workflows via version control.

  ### Bug Fixes

  - Fixed Claude Code YAML parsing failure when command names contained colons
  - Fixed task file parsing to handle trailing whitespace on checkbox lines
  - Fixed JSON instruction output to separate context/rules from template — AI was copying constraint blocks into artifact files

  ### Documentation

  - New getting-started guide, CLI reference, concepts documentation
  - Removed misleading "edit mid-flight and continue" claims that weren't implemented
  - Added migration guide for upgrading from pre-OPSX versions

## 0.23.0

### Minor Changes

- [#540](https://github.com/Fission-AI/OpenSpec/pull/540) [`c4cfdc7`](https://github.com/Fission-AI/OpenSpec/commit/c4cfdc7c499daef30d8a218f5f59b8d9e5adb754) Thanks [@TabishB](https://github.com/TabishB)! - ### New Features

  - **Bulk archive skill** — Archive multiple completed changes in a single operation with `/opsx:bulk-archive`. Includes batch validation, spec conflict detection, and consolidated confirmation

  ### Other

  - **Simplified setup** — Config creation now uses sensible defaults with helpful comments instead of interactive prompts

## 0.22.0

### Minor Changes

- [#530](https://github.com/Fission-AI/OpenSpec/pull/530) [`33466b1`](https://github.com/Fission-AI/OpenSpec/commit/33466b1e2a6798bdd6d0e19149173585b0612e6f) Thanks [@TabishB](https://github.com/TabishB)! - Add project-level configuration, project-local schemas, and schema management commands

  **New Features**

  - **Project-level configuration** — Configure OpenSpec behavior per-project via `openspec/config.yaml`, including custom rules injection, context files, and schema resolution settings
  - **Project-local schemas** — Define custom artifact schemas within your project's `openspec/schemas/` directory for project-specific workflows
  - **Schema management commands** — New `openspec schema` commands (`list`, `show`, `export`, `validate`) for inspecting and managing artifact schemas (experimental)

  **Bug Fixes**

  - Fixed config loading to handle null `rules` field in project configuration

## 0.21.0

### Minor Changes

- [#516](https://github.com/Fission-AI/OpenSpec/pull/516) [`b5a8847`](https://github.com/Fission-AI/OpenSpec/commit/b5a884748be6156a7bb140b4941cfec4f20a9fc8) Thanks [@TabishB](https://github.com/TabishB)! - Add feedback command and Nix flake support

  **New Features**

  - **Feedback command** — Submit feedback directly from the CLI with `openspec feedback`, which creates GitHub Issues with automatic metadata inclusion and graceful fallback for manual submission
  - **Nix flake support** — Install and develop openspec using Nix with the new `flake.nix`, including automated flake maintenance and CI validation

  **Bug Fixes**

  - **Explore mode guardrails** — Explore mode now explicitly prevents implementation, keeping the focus on thinking and discovery while still allowing artifact creation

  **Other**

  - Improved change inference in `opsx apply` — automatically detects the target change from conversation context or prompts when ambiguous
  - Streamlined archive sync assessment with clearer delta spec location guidance

## 0.20.0

### Minor Changes

- [#502](https://github.com/Fission-AI/OpenSpec/pull/502) [`9db74aa`](https://github.com/Fission-AI/OpenSpec/commit/9db74aa5ac6547efadaed795217cfa17444f2004) Thanks [@TabishB](https://github.com/TabishB)! - Add `/opsx:verify` command and fix vitest process storms

  **New Features**

  - **`/opsx:verify` command** — Validate that change implementations match their specifications

  **Bug Fixes**

  - Fixed vitest process storms by capping worker parallelism
  - Fixed agent workflows to use non-interactive mode for validation commands
  - Fixed PowerShell completions generator to remove trailing commas

## 0.19.0

### Minor Changes

- eb152eb: Add Continue IDE support, shell completions, and `/opsx:explore` command

  **New Features**

  - **Continue IDE support** – OpenSpec now generates slash commands for [Continue](https://continue.dev/), expanding editor integration options alongside Cursor, Windsurf, Claude Code, and others
  - **Shell completions for Bash, Fish, and PowerShell** – Run `openspec completion install` to set up tab completion in your preferred shell
  - **`/opsx:explore` command** – A new thinking partner mode for exploring ideas and investigating problems before committing to changes
  - **Codebuddy slash command improvements** – Updated frontmatter format for better compatibility

  **Bug Fixes**

  - Shell completions now correctly offer parent-level flags (like `--help`) when a command has subcommands
  - Fixed Windows compatibility issues in tests

  **Other**

  - Added optional anonymous usage statistics to help understand how OpenSpec is used. This is **opt-out** by default – set `OPENSPEC_TELEMETRY=0` or `DO_NOT_TRACK=1` to disable. Only command names and version are collected; no arguments, file paths, or content. Automatically disabled in CI environments.

## 0.18.0

### Minor Changes

- 8dfd824: Add OPSX experimental workflow commands and enhanced artifact system

  **New Commands:**

  - `/opsx:ff` - Fast-forward through artifact creation, generating all needed artifacts in one go
  - `/opsx:sync` - Sync delta specs from a change to main specs
  - `/opsx:archive` - Archive completed changes with smart sync check

  **Artifact Workflow Enhancements:**

  - Schema-aware apply instructions with inline guidance and XML output
  - Agent schema selection for experimental artifact workflow
  - Per-change schema metadata via `.openspec.yaml` files
  - Agent Skills for experimental artifact workflow
  - Instruction loader for template loading and change context
  - Restructured schemas as directories with templates

  **Improvements:**

  - Enhanced list command with last modified timestamps and sorting
  - Change creation utilities for better workflow support

  **Fixes:**

  - Normalize paths for cross-platform glob compatibilit
... [TRUNCATED]
```

### File: eslint.config.js
```js
import tseslint from 'typescript-eslint';

export default tseslint.config(
  {
    files: ['src/**/*.ts'],
    extends: [...tseslint.configs.recommended],
    rules: {
      // Prevent static imports of @inquirer modules to avoid pre-commit hook hangs.
      // These modules have side effects that can keep the Node.js event loop alive
      // when stdin is piped. Use dynamic import() instead.
      // See: https://github.com/Fission-AI/OpenSpec/issues/367
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            {
              group: ['@inquirer/*'],
              message:
                'Use dynamic import() for @inquirer modules to prevent pre-commit hook hangs. See #367.',
            },
          ],
        },
      ],
      // Disable rules that need broader cleanup - focus on critical issues only
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-unused-vars': 'off',
      'no-empty': 'off',
      'prefer-const': 'off',
    },
  },
  {
    // init.ts is dynamically imported from cli/index.ts, so static @inquirer
    // imports there are safe - they won't be loaded at CLI startup
    files: ['src/core/init.ts'],
    rules: {
      'no-restricted-imports': 'off',
    },
  },
  {
    ignores: ['dist/**', 'node_modules/**', '*.js', '*.mjs'],
  }
);

```

### File: MAINTAINERS.md
```md
# Maintainers

People who maintain and guide OpenSpec.

## Core Maintainers

| Name | GitHub | Role |
|------|--------|------|
| Tabish Bidiwale | [@TabishB](https://github.com/TabishB) | Lead maintainer |

## Advisors

Advisors help shape technical direction and provide guidance to the project.

| Name | GitHub | Focus |
|------|--------|-------|
| Hari Krishnan | [@harikrishnan83](https://github.com/harikrishnan83) | Technical direction |

```

### File: openspec-parallel-merge-plan.md
```md
# OpenSpec Parallel Delta Remediation Plan

## Problem Summary
- Active changes apply requirement-level replacements when archiving. When two changes touch the same requirement, the second archive overwrites the first and silently drops scenarios (e.g., Windsurf vs. Kilo Code slash command updates).
- The archive workflow (`src/core/archive.ts:191` and `src/core/archive.ts:501`) rebuilds main specs by replacing entire requirement blocks with the content contained in the change delta. The delta format (`src/core/parsers/requirement-blocks.ts:113`) has no notion of base versions or scenario-level operations.
- The tooling cannot detect divergence between the change author’s starting point and the live spec, so parallel development corrupts the source of truth without warning.

## Observed Failure Mode
- Change A (`add-windsurf-workflows`) adds a Windsurf scenario under `Slash Command Configuration`.
- Change B (`add-kilocode-workflows`) adds a Kilo Code scenario to the same requirement, starting from the pre-Windsurf spec.
- After Change A archives, the main spec contains both scenarios.
- When Change B archives, `buildUpdatedSpec` sees a `MODIFIED` block for `Slash Command Configuration` and replaces the requirement with the four-scenario variant shipped in that change. Because that file never learned about Windsurf, the Windsurf scenario disappears.
- There is no warning, diff, or conflict indicator—the archive completes successfully, and the source-of-truth spec now omits a shipped scenario.

## Root Causes
1. **Replace-only semantics.** `buildUpdatedSpec` performs hash-map substitution of requirement blocks and cannot merge or compare individual scenarios (`src/core/archive.ts:455`-`src/core/archive.ts:526`).
2. **Missing base fingerprint.** Changes do not persist the requirement content they were authored against, so the archive step cannot tell if the live spec diverged.
3. **Single-level granularity.** The delta language only understands requirements. Even if we introduced scenario-level parsing, we would still lose sibling edits without an accompanying merge strategy.
4. **Lack of conflict UX.** The CLI never forces contributors to reconcile parallel updates. There is no equivalent of `git merge`, `git rebase`, or conflict markers.

## Design Objectives
- Preserve every approved scenario regardless of archive order.
- Detect and block speculative archives when the live spec diverges from the author’s base.
- Provide a deterministic, reviewable conflict resolution flow that mirrors source-control best practices.
- Keep the authoring experience ergonomic: deltas should remain human-editable markdown.
- Support incremental adoption so existing repositories can roll forward without breaking active work.

## Proposed Fix: Layered Remediation

### Phase 0 – Stop the Bleeding (Detection & Guardrails)
1. **Persist requirement fingerprints alongside each change.**
   - When scaffolding or validating a change, capture the current requirement body for every `MODIFIED`/`REMOVED`/`RENAMED` entry and write it to `changes/<id>/meta.json`.
   - Store a stable hash (e.g., SHA-256) of the base requirement content and the raw text itself for later merges.
2. **Validate fingerprints during archive.**
   - Before `buildUpdatedSpec` mutates specs, recompute the requirement hash from the live spec.
   - If the hash differs from the stored base, abort and instruct the user to rebase. This makes the destructive path impossible.
3. **Surface intent in CLI output.**
   - Show which requirements are stale, when they diverged, and which change last touched them.
4. **Document interim manual mitigation.**
   - Update `openspec/AGENTS.md` and docs so contributors know to rerun `openspec change sync` (see Phase 1) whenever another change lands.

_Outcome:_ We prevent data loss immediately while we work on a richer merge story.

### Phase 1 – Add a Rebase Workflow (Author-Side Merge)
1. **Introduce `openspec change sync <id>` (or `rebase`).**
   - Reads the stored base snapshot, the current spec, and the author’s delta.
   - Performs a 3-way merge per requirement. A naive diff3 on markdown lines is acceptable initially because we already operate on requirement-sized chunks.
   - If the merge is clean, rewrite the `MODIFIED` block with the merged text and refresh the stored fingerprint.
   - On conflict, write conflict markers inside the change delta (similar to Git) and require the author to hand-edit before re-running validation.
2. **Enrich validator messages.**
   - `openspec validate` should flag unresolved conflict markers or fingerprint mismatches so errors appear early in the workflow.
3. **Optional:** Offer a `--rewrite-scenarios` helper that merges bullet lists of scenarios to reduce manual editing noise.

_Outcome:_ Contributors can safely reconcile their work with the latest spec before archiving, restoring true parallel development.

### Phase 2 – Increase Delta Granularity
1. **Extend the delta language with scenario-level directives.**
   - Allow `## MODIFIED Requirements` + `## ADDED Scenarios` / `## MODIFIED Scenarios` sections nested under the requirement header.
   - Backed by stable scenario identifiers (explicit IDs or generated hashes) stored in `meta.json`. This lets the system reason about individual scenarios.
2. **Teach the parser to understand nested operations.**
   - Update `parseDeltaSpec` to emit scenario-level operations in addition to requirement blocks.
   - Update `buildUpdatedSpec` (or its replacement) to merge scenario lists, preserving order while inserting new entries in a deterministic fashion.
3. **Automate migration.**
   - Provide a one-time command that inspects each existing spec, injects scenario IDs, and rewrites in-flight change deltas into the richer format.
4. **Continue to rely on the Phase 1 rebase flow for conflicts when two changes edit the same scenario body or description.**

_Outcome:_ Most concurrent updates become commutative, drastically reducing the odds of human merges.

### Phase 3 – Structured Spec Graph (Long-Term)
1. **Define stable requirement IDs.**
   - Embed `Requirement ID: <uuid>` markers in specs so renames and moves are trackable.
   - This enables future features like cross-capability references and better diff visualizations.
2. **Model spec edits as operations over an AST.**
   - Build an intermediate representation (IR) for requirements/scenarios/metadata.
   - Use operational transforms or CRDT-like techniques to guarantee merge associativity.
3. **Integrate with Git directly.**
   - Offer optional `openspec branch` scaffolding that aligns spec changes with Git branches, letting teams leverage Git’s conflict editor for the markdown IR.

_Outcome:_ OpenSpec graduates from replace-based updates to a resilient, intent-preserving spec management platform.

## Migration & Product Impacts
- **Backfill metadata:** add hashes for all active changes and the current main specs during the initial rollout.
- **CLI UX:** new commands (`change sync`, enhanced `archive`) require documentation, help text, and release notes.
- **Docs & AGENTS updates:** reinforce the rebase workflow and explain conflict resolution to AI assistants.
- **Testing:** introduce fixtures covering divergent requirement fingerprints and merge resolution logic.
- **Telemetry (optional):** log fingerprint mismatches so we can see how often teams hit conflicts after the rollout.

## Open Questions / Risks
- How should we order scenarios when multiple changes insert at different points? (Consider optional `position` metadata or deterministic alphabetical fallbacks.)
- What is the graceful failure mode if contributors delete the `meta.json` file? (CLI should recreate fingerprints on demand.)
- Do we need to support offline authors who cannot easily re-run the sync command before archiving? (Potential `--accept-outdated` escape hatch for emergencies.)
- How will archived historical changes be handled? We may need a migration script to embed fingerprints retroactively so re-validation succeeds.

## Immediate Next Steps
1. Prototype fingerprint capture during `openspec change validate` and block archive on mismatches.
2. Ship `openspec change sync` with line-based diff3 merging and conflict markers.
3. Update contributor docs and AI instructions to mandate running `sync` before archiving.
4. Plan the scenario-level delta extension and migration path as a follow-up RFC.

```

### File: package-lock.json
```json
{
  "name": "@fission-ai/openspec",
  "version": "1.1.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "@fission-ai/openspec",
      "version": "1.1.1",
      "hasInstallScript": true,
      "license": "MIT",
      "dependencies": {
        "@inquirer/core": "^10.2.2",
        "@inquirer/prompts": "^7.8.0",
        "chalk": "^5.5.0",
        "commander": "^14.0.0",
        "fast-glob": "^3.3.3",
        "ora": "^8.2.0",
        "posthog-node": "^5.20.0",
        "yaml": "^2.8.2",
        "zod": "^4.0.17"
      },
      "bin": {
        "openspec": "bin/openspec.js"
      },
      "devDependencies": {
        "@changesets/changelog-github": "^0.5.2",
        "@changesets/cli": "^2.27.7",
        "@types/node": "^24.2.0",
        "@vitest/ui": "^3.2.4",
        "eslint": "^9.39.2",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.50.1",
        "vitest": "^3.2.4"
      },
      "engines": {
        "node": ">=20.19.0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.28.6.tgz",
      "integrity": "sha512-05WQkdpL9COIMz4LjTxGpPNCdlpyimKppYNoJ5Di5EUObifl8t4tuLuUBBZEpoLYOmfvIWrsp9fCl0HoPRVTdA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@changesets/apply-release-plan": {
      "version": "7.0.14",
      "resolved": "https://registry.npmjs.org/@changesets/apply-release-plan/-/apply-release-plan-7.0.14.tgz",
      "integrity": "sha512-ddBvf9PHdy2YY0OUiEl3TV78mH9sckndJR14QAt87KLEbIov81XO0q0QAmvooBxXlqRRP8I9B7XOzZwQG7JkWA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/config": "^3.1.2",
        "@changesets/get-version-range-type": "^0.4.0",
        "@changesets/git": "^3.0.4",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "detect-indent": "^6.0.0",
        "fs-extra": "^7.0.1",
        "lodash.startcase": "^4.4.0",
        "outdent": "^0.5.0",
        "prettier": "^2.7.1",
        "resolve-from": "^5.0.0",
        "semver": "^7.5.3"
      }
    },
    "node_modules/@changesets/assemble-release-plan": {
      "version": "6.0.9",
      "resolved": "https://registry.npmjs.org/@changesets/assemble-release-plan/-/assemble-release-plan-6.0.9.tgz",
      "integrity": "sha512-tPgeeqCHIwNo8sypKlS3gOPmsS3wP0zHt67JDuL20P4QcXiw/O4Hl7oXiuLnP9yg+rXLQ2sScdV1Kkzde61iSQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@changesets/get-dependents-graph": "^2.1.3",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "semver": "^7.5.3"
      }
    },
    "node_modules/@changesets/changelog-git": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/@changesets/changelog-git/-/changelog-git-0.2.1.tgz",
      "integrity": "sha512-x/xEleCFLH28c3bQeQIyeZf8lFXyDFVn1SgcBiR2Tw/r4IAWlk1fzxCEZ6NxQAjF2Nwtczoen3OA2qR+UawQ8Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0"
      }
    },
    "node_modules/@changesets/changelog-github": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/@changesets/changelog-github/-/changelog-github-0.5.2.tgz",
      "integrity": "sha512-HeGeDl8HaIGj9fQHo/tv5XKQ2SNEi9+9yl1Bss1jttPqeiASRXhfi0A2wv8yFKCp07kR1gpOI5ge6+CWNm1jPw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/get-github-info": "^0.7.0",
        "@changesets/types": "^6.1.0",
        "dotenv": "^8.1.0"
      }
    },
    "node_modules/@changesets/cli": {
      "version": "2.29.8",
      "resolved": "https://registry.npmjs.org/@changesets/cli/-/cli-2.29.8.tgz",
      "integrity": "sha512-1weuGZpP63YWUYjay/E84qqwcnt5yJMM0tep10Up7Q5cS/DGe2IZ0Uj3HNMxGhCINZuR7aO9WBMdKnPit5ZDPA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/apply-release-plan": "^7.0.14",
        "@changesets/assemble-release-plan": "^6.0.9",
        "@changesets/changelog-git": "^0.2.1",
        "@changesets/config": "^3.1.2",
        "@changesets/errors": "^0.2.0",
        "@changesets/get-dependents-graph": "^2.1.3",
        "@changesets/get-release-plan": "^4.0.14",
        "@changesets/git": "^3.0.4",
        "@changesets/logger": "^0.1.1",
        "@changesets/pre": "^2.0.2",
        "@changesets/read": "^0.6.6",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@changesets/write": "^0.4.0",
        "@inquirer/external-editor": "^1.0.2",
        "@manypkg/get-packages": "^1.1.3",
        "ansi-colors": "^4.1.3",
        "ci-info": "^3.7.0",
        "enquirer": "^2.4.1",
        "fs-extra": "^7.0.1",
        "mri": "^1.2.0",
        "p-limit": "^2.2.0",
        "package-manager-detector": "^0.2.0",
        "picocolors": "^1.1.0",
        "resolve-from": "^5.0.0",
        "semver": "^7.5.3",
        "spawndamnit": "^3.0.1",
        "term-size": "^2.1.0"
      },
      "bin": {
        "changeset": "bin.js"
      }
    },
    "node_modules/@changesets/config": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@changesets/config/-/config-3.1.2.tgz",
      "integrity": "sha512-CYiRhA4bWKemdYi/uwImjPxqWNpqGPNbEBdX1BdONALFIDK7MCUj6FPkzD+z9gJcvDFUQJn9aDVf4UG7OT6Kog==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@changesets/get-dependents-graph": "^2.1.3",
        "@changesets/logger": "^0.1.1",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "fs-extra": "^7.0.1",
        "micromatch": "^4.0.8"
      }
    },
    "node_modules/@changesets/errors": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/@changesets/errors/-/errors-0.2.0.tgz",
      "integrity": "sha512-6BLOQUscTpZeGljvyQXlWOItQyU71kCdGz7Pi8H8zdw6BI0g3m43iL4xKUVPWtG+qrrL9DTjpdn8eYuCQSRpow==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "extendable-error": "^0.1.5"
      }
    },
    "node_modules/@changesets/get-dependents-graph": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/@changesets/get-dependents-graph/-/get-dependents-graph-2.1.3.tgz",
      "integrity": "sha512-gphr+v0mv2I3Oxt19VdWRRUxq3sseyUpX9DaHpTUmLj92Y10AGy+XOtV+kbM6L/fDcpx7/ISDFK6T8A/P3lOdQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "picocolors": "^1.1.0",
        "semver": "^7.5.3"
      }
    },
    "node_modules/@changesets/get-github-info": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/@changesets/get-github-info/-/get-github-info-0.7.0.tgz",
      "integrity": "sha512-+i67Bmhfj9V4KfDeS1+Tz3iF32btKZB2AAx+cYMqDSRFP7r3/ZdGbjCo+c6qkyViN9ygDuBjzageuPGJtKGe5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "dataloader": "^1.4.0",
        "node-fetch": "^2.5.0"
      }
    },
    "node_modules/@changesets/get-release-plan": {
      "version": "4.0.14",
      "resolved": "https://registry.npmjs.org/@changesets/get-release-plan/-/get-release-plan-4.0.14.tgz",
      "integrity": "sha512-yjZMHpUHgl4Xl5gRlolVuxDkm4HgSJqT93Ri1Uz8kGrQb+5iJ8dkXJ20M2j/Y4iV5QzS2c5SeTxVSKX+2eMI0g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/assemble-release-plan": "^6.0.9",
        "@changesets/config": "^3.1.2",
        "@changesets/pre": "^2.0.2",
        "@changesets/read": "^0.6.6",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3"
      }
    },
    "node_modules/@changesets/get-version-range-type": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@changesets/get-version-range-type/-/get-version-range-type-0.4.0.tgz",
      "integrity": "sha512-hwawtob9DryoGTpixy1D3ZXbGgJu1Rhr+ySH2PvTLHvkZuQ7sRT4oQwMh0hbqZH1weAooedEjRsbrWcGLCeyVQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@changesets/git": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@changesets/git/-/git-3.0.4.tgz",
      "integrity": "sha512-BXANzRFkX+XcC1q/d27NKvlJ1yf7PSAgi8JG6dt8EfbHFHi4neau7mufcSca5zRhwOL8j9s6EqsxmT+s+/E6Sw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@manypkg/get-packages": "^1.1.3",
        "is-subdir": "^1.1.1",
        "micromatch": "^4.0.8",
        "spawndamnit": "^3.0.1"
      }
    },
    "node_modules/@changesets/logger": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/@changesets/logger/-/logger-0.1.1.tgz",
      "integrity": "sha512-OQtR36ZlnuTxKqoW4Sv6x5YIhOmClRd5pWsjZsddYxpWs517R0HkyiefQPIytCVh4ZcC5x9XaG8KTdd5iRQUfg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "picocolors": "^1.1.0"
      }
    },
    "node_modules/@changesets/parse": {
      "version": "0.4.2",
      "resolved": "https://registry.npmjs.org/@changesets/parse/-/parse-0.4.2.tgz",
      "integrity": "sha512-Uo5MC5mfg4OM0jU3up66fmSn6/NE9INK+8/Vn/7sMVcdWg46zfbvvUSjD9EMonVqPi9fbrJH9SXHn48Tr1f2yA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "js-yaml": "^4.1.1"
      }
    },
    "node_modules/@changesets/pre": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/@changesets/pre/-/pre-2.0.2.tgz",
      "integrity": "sha512-HaL/gEyFVvkf9KFg6484wR9s0qjAXlZ8qWPDkTyKF6+zqjBe/I2mygg3MbpZ++hdi0ToqNUF8cjj7fBy0dg8Ug==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "fs-extra": "^7.0.1"
      }
    },
    "node_modules/@changesets/read": {
      "version": "0.6.6",
      "resolved": "https://registry.npmjs.org/@changesets/read/-/read-0.6.6.tgz",
      "integrity": "sha512-P5QaN9hJSQQKJShzzpBT13FzOSPyHbqdoIBUd2DJdgvnECCyO6LmAOWSV+O8se2TaZJVwSXjL+v9yhb+a9JeJg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/git": "^3.0.4",
        "@changesets/logger": "^0.1.1",
        "@changesets/parse": "^0.4.2",
        "@changesets/types": "^6.1.0",
        "fs-extra": "^7.0.1",
        "p-filter": "^2.1.0",
        "picocolors": "^1.1.0"
      }
    },
    "node_modules/@changesets/should-skip-package": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/@changesets/should-skip-package/-/should-skip-package-0.1.2.tgz",
      "integrity": "sha512-qAK/WrqWLNCP22UDdBTMPH5f41elVDlsNyat180A33dWxuUDyNpg6fPi/FyTZwRriVjg0L8gnjJn2F9XAoF0qw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3"
      }
    },
    "node_modules/@changesets/types": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/@changesets/types/-/types-6.1.0.tgz",
      "integrity": "sha512-rKQcJ+o1nKNgeoYRHKOS07tAMNd3YSN0uHaJOZYjBAgxfV7TUE7JE+z4BzZdQwb5hKaYbayKN5KrYV7ODb2rAA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@changesets/write": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@changesets/write/-/write-0.4.0.tgz",
      "integrity": "sha512-CdTLvIOPiCNuH71pyDu3rA+Q0n65cmAbXnwWH84rKGiFumFzkmHNT8KHTMEchcxN+Kl8I54xGUhJ7l3E7X396Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "fs-extra": "^7.0.1",
        "human-id": "^4.1.1",
        "prettier": "^2.7.1"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.3.tgz",
      "integrity": "sha512-9fJMTNFTWZMh5qwrBItuziu834eOCUcEqymSH7pY+zoMVEZg3gcPuBNxH1EvfVYe9h0x/Ptw8KBzv7qxb7l8dg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.3.tgz",
      "integrity": "sha512-i5D1hPY7GIQmXlXhs2w8AWHhenb00+GxjxRncS2ZM7YNVGNfaMxgzSGuO8o8SJzRc/oZwU2bcScvVERk03QhzA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.3.tgz",
      "integrity": "sha512-YdghPYUmj/FX2SYKJ0OZxf+iaKgMsKHVPF1MAq/P8WirnSpCStzKJFjOjzsW0QQ7oIAiccHdcqjbHmJxRb/dmg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.3.tgz",
      "integrity": "sha512-IN/0BNTkHtk8lkOM8JWAYFg4ORxBkZQf9zXiEOfERX/CzxW3Vg1ewAhU7QSWQpVIzTW+b8Xy+lGzdYXV6UZObQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.3.tgz",
      "integrity": "sha512-Re491k7ByTVRy0t3EKWajdLIr0gz2kKKfzafkth4Q8A5n1xTHrkqZgLLjFEHVD+AXdUGgQMq+Godfq45mGpCKg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.3.tgz",
      "integrity": "sha512-vHk/hA7/1AckjGzRqi6wbo+jaShzRowYip6rt6q7VYEDX4LEy1pZfDpdxCBnGtl+A5zq8iXDcyuxwtv3hNtHFg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.3",
      "resolved": "https://re
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
