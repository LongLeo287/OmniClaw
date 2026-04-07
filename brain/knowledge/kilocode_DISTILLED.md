---
id: kilocode
type: knowledge
owner: OA_Triage
---
# kilocode
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "$schema": "https://json.schemastore.org/package.json",
  "name": "@kilocode/kilo",
  "description": "AI-powered development tool",
  "private": true,
  "type": "module",
  "packageManager": "bun@1.3.10",
  "scripts": {
    "dev": "bun run --cwd packages/opencode --conditions=browser src/index.ts",
    "dev:desktop": "bun --cwd packages/desktop tauri dev",
    "dev:web": "bun --cwd packages/app dev",
    "dev:storybook": "bun --cwd packages/storybook storybook",
    "typecheck": "bun turbo typecheck",
    "prepare": "husky",
    "random": "echo 'Random script'",
    "hello": "echo 'Hello World!'",
    "test": "echo 'do not run tests from root' && exit 1",
    "extension": "bun --cwd packages/kilo-vscode script/launch.ts"
  },
  "workspaces": {
    "packages": [
      "packages/*",
      "packages/sdk/js"
    ],
    "catalog": {
      "@types/bun": "1.3.9",
      "@octokit/rest": "22.0.0",
      "@hono/zod-validator": "0.4.2",
      "ulid": "3.0.1",
      "@kobalte/core": "0.13.11",
      "@types/luxon": "3.7.1",
      "@types/node": "22.13.9",
      "@types/semver": "7.7.1",
      "@tsconfig/node22": "22.0.2",
      "@tsconfig/bun": "1.0.9",
      "@cloudflare/workers-types": "4.20251008.0",
      "@openauthjs/openauth": "0.0.0-20250322224806",
      "@pierre/diffs": "1.1.0-beta.18",
      "@solid-primitives/storage": "4.3.3",
      "@tailwindcss/vite": "4.1.11",
      "diff": "8.0.2",
      "dompurify": "3.3.1",
      "drizzle-kit": "1.0.0-beta.16-ea816b6",
      "drizzle-orm": "1.0.0-beta.16-ea816b6",
      "ai": "5.0.124",
      "hono": "4.10.7",
      "hono-openapi": "1.1.2",
      "fuzzysort": "3.1.0",
      "luxon": "3.6.1",
      "marked": "17.0.1",
      "marked-shiki": "1.2.1",
      "@playwright/test": "1.51.0",
      "typescript": "5.8.2",
      "@typescript/native-preview": "7.0.0-dev.20260316.1",
      "zod": "4.1.8",
      "remeda": "2.26.0",
      "shiki": "3.20.0",
      "solid-list": "0.3.0",
      "tailwindcss": "4.1.11",
      "virtua": "0.42.3",
      "vite": "7.1.4",
      "@solidjs/meta": "0.29.4",
      "@solidjs/router": "0.15.4",
      "@solidjs/start": "https://pkg.pr.new/@solidjs/start@dfb2020",
      "solid-js": "1.9.10",
      "vite-plugin-solid": "2.11.10"
    }
  },
  "devDependencies": {
    "@actions/artifact": "5.0.1",
    "@tsconfig/bun": "catalog:",
    "@types/mime-types": "3.0.1",
    "@typescript/native-preview": "catalog:",
    "glob": "13.0.5",
    "husky": "9.1.7",
    "prettier": "3.6.2",
    "semver": "^7.6.0",
    "sst": "3.18.10",
    "turbo": "2.8.13"
  },
  "dependencies": {
    "@aws-sdk/client-s3": "3.933.0",
    "@kilocode/plugin": "workspace:*",
    "@opencode-ai/script": "workspace:*",
    "@kilocode/sdk": "workspace:*",
    "typescript": "catalog:",
    "@morphllm/morphsdk": "0.2.141"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/Kilo-Org/kilocode"
  },
  "license": "MIT",
  "prettier": {
    "semi": false,
    "printWidth": 120
  },
  "trustedDependencies": [
    "esbuild",
    "protobufjs",
    "tree-sitter",
    "tree-sitter-bash",
    "web-tree-sitter",
    "electron"
  ],
  "overrides": {
    "@types/bun": "catalog:",
    "@types/node": "catalog:"
  },
  "patchedDependencies": {
    "@standard-community/standard-openapi@0.2.9": "patches/@standard-community%2Fstandard-openapi@0.2.9.patch",
    "@openrouter/ai-sdk-provider@1.5.4": "patches/@openrouter%2Fai-sdk-provider@1.5.4.patch",
    "ghostty-web@0.3.0": "patches/ghostty-web@0.3.0.patch"
  },
  "version": "7.1.20",
  "peerDependencies": {}
}

```

### File: README.md
```md
<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code"><img src="https://raster.shields.io/badge/VS_Code_Marketplace-007ACC?style=flat&logo=visualstudiocode&logoColor=white" alt="VS Code Marketplace" height="20"></a>
  <a href="https://x.com/kilocode"><img src="https://raster.shields.io/badge/kilocode-000000?style=flat&logo=x&logoColor=white" alt="X (Twitter)" height="20"></a>
  <a href="https://blog.kilo.ai"><img src="https://raster.shields.io/badge/Blog-555?style=flat&logo=substack&logoColor=white" alt="Substack Blog" height="20"></a>
  <a href="https://kilo.ai/discord"><img src="https://raster.shields.io/badge/Join%20Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord" height="20"></a>
  <a href="https://www.reddit.com/r/kilocode/"><img src="https://raster.shields.io/badge/Join%20r%2Fkilocode-D84315?style=flat&logo=reddit&logoColor=white" alt="Reddit" height="20"></a>
</p>

# 🚀 Kilo

> Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most popular open source coding agent.
> [#1 coding agent on OpenRouter](https://openrouter.ai/apps/category/coding). 1.5M+ Kilo Coders. 25T+ tokens processed

- ✨ Generate code from natural language
- ✅ Checks its own work
- 🧪 Run terminal commands
- 🌐 Automate the browser
- ⚡ Inline autocomplete suggestions
- 🤖 Latest AI models
- 🎁 API keys optional
- 💡 **Get $20 in bonus credits when you top-up for the first time** Credits can be used with 500+ models like Gemini 3.1 Pro, Claude 4.6 Sonnet & Opus, and GPT-5.2

## Quick Links

- [VS Code Marketplace](https://kilo.ai/vscode-marketplace?utm_source=Readme) (download)
- Install CLI: `npm install -g @kilocode/cli`
- [Official Kilo.ai Home page](https://kilo.ai) (learn more)

## Key Features

- **Code Generation:** Kilo can generate code using natural language.
- **Inline Autocomplete:** Get intelligent code completions as you type, powered by AI.
- **Task Automation:** Kilo can automate repetitive coding tasks to save time.
- **Automated Refactoring:** Kilo can refactor and improve existing code efficiently.
- **MCP Server Marketplace**: Kilo can easily find, and use MCP servers to extend the agent capabilities.
- **Multi Mode**: Plan with Architect, Code with Coder, and Debug with Debugger, and make your own custom modes.

## Get Started in Visual Studio Code

1. Install the Kilo Code extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code).
2. Create your account to access 500+ cutting-edge AI models including Gemini 3 Pro, Claude 4.5 Sonnet & Opus, and GPT-5 – with transparent pricing that matches provider rates exactly.
3. Start coding with AI that adapts to your workflow. Watch our quick-start guide to see Kilo in action:

<a href="https://youtu.be/pqGfYXgrhig"><img src="https://img.youtube.com/vi/pqGfYXgrhig/maxresdefault.jpg" alt="Watch the video" width="640" height="360"></a>

## Get Started with the CLI

```bash
# npm
npm install -g @kilocode/cli

# Or run directly with npx
npx @kilocode/cli
```

Then run `kilo` in any project directory to start.

<!-- kilocode_change start -->

### npm Install Note: Hidden `.kilo` File

On some systems and npm versions, installing `@kilocode/cli` can create a hidden `.kilo` file near the installed `kilo` command (for example in a global npm bin directory). This file is an npm-generated launcher helper, not project data.

- Why it exists: npm may create helper artifacts while wiring CLI executables.
- Size caveat: size can vary by platform, npm version, and install mode (symlink vs copied launcher), so a strict fixed size is not guaranteed.
- Safety: it is safe to leave in place. Do not edit it manually. Use your package manager's uninstall (`npm uninstall -g @kilocode/cli`) to remove install artifacts cleanly.
<!-- kilocode_change end -->

### Install from GitHub Releases (Optional)

Download the latest binary or source code from the [Releases page](https://github.com/Kilo-Org/kilocode/releases), use this quick guide:

- `kilo-<os>-<arch>.zip` is the CLI binary for your OS and CPU architecture on Windows and macOS. (`kilo-linux-<arch>.tar.gz` for Linux)
- `darwin` means macOS.
- `x64` is standard 64-bit Intel/AMD CPUs.
- `x64-baseline` is a compatibility build for older x64 CPUs(do not support AVX Instruction).
- `arm64` is ARM-based Linux/MacOS.
- `musl` is statically linked Linux build for Alpine/minimal Docker without glibc. Alpine/minimal Docker users should prefer the matching \*-musl asset.
- `kilo-vscode-*.vsix` is the VS Code extension package and not the CLI binary.
- `Source code` releases are for building from source, not normal installation.

For most users:

- **Windows (most PCs):** `kilo-windows-x64.zip`
- **macOS Apple Silicon:** `kilo-darwin-arm64.zip`
- **macOS Intel:** `kilo-darwin-x64.zip`
- **Linux x64:** `kilo-linux-x64.tar.gz`
- **Linux on ARM:** `kilo-linux-arm64.tar.gz`

### Autonomous Mode (CI/CD)

Use the `--auto` flag with `kilo run` to enable fully autonomous operation without user interaction. This is ideal for CI/CD pipelines and automated workflows:

```bash
kilo run --auto "run tests and fix any failures"
```

**Important:** The `--auto` flag disables all permission prompts and allows the agent to execute any action without confirmation. Only use this in trusted environments like CI/CD pipelines.

## Contributing

We welcome contributions from developers, writers, and enthusiasts!
To get started, please read our [Contributing Guide](/CONTRIBUTING.md). It includes details on setting up your environment, coding standards, types of contribution and how to submit pull requests.

See [RELEASING.md](RELEASING.md) for the release process.

## Code of Conduct

Our community is built on respect, inclusivity, and collaboration. Please review our [Code of Conduct](/CODE_OF_CONDUCT.md) to understand the expectations for all contributors and community members.

## License

This project is licensed under the MIT License.
You’re free to use, modify, and distribute this code, including for commercial purposes as long as you include proper attribution and license notices. See [License](/LICENSE).

### Where did Kilo CLI come from?

Kilo CLI is a fork of [OpenCode](https://github.com/anomalyco/opencode), enhanced to work within the Kilo agentic engineering platform.

```

### File: github\README.md
```md
# Kilo GitHub Action

A GitHub Action that integrates [Kilo AI](https://kilo.ai) directly into your GitHub workflow.

Mention `/kilo` or `/kc` in your comment, and Kilo will execute tasks within your GitHub Actions runner.

## Features

#### Explain an issue

Leave the following comment on a GitHub issue. Kilo will read the entire thread, including all comments, and reply with a clear explanation.

```
/kilo explain this issue
```

#### Fix an issue

Leave the following comment on a GitHub issue. Kilo will create a new branch, implement the changes, and open a PR with the changes.

```
/kilo fix this
```

#### Review PRs and make changes

Leave the following comment on a GitHub PR. Kilo will implement the requested change and commit it to the same PR.

```
Delete the attachment from S3 when the note is removed /kc
```

#### Review specific code lines

Leave a comment directly on code lines in the PR's "Files" tab. Kilo will automatically detect the file, line numbers, and diff context to provide precise responses.

```
[Comment on specific lines in Files tab]
/kc add error handling here
```

When commenting on specific lines, Kilo receives:

- The exact file being reviewed
- The specific lines of code
- The surrounding diff context
- Line number information

This allows for more targeted requests without needing to specify file paths or line numbers manually.

## Installation

Run the following command in the terminal from your GitHub repo:

```bash
kilo github install
```

This will walk you through installing the KiloConnect GitHub app, creating the workflow, and setting up secrets.

### Manual Setup

1. Install the KiloConnect GitHub app at https://github.com/apps/kiloconnect. Make sure it is installed on the target repository.

2. Add the following workflow file to `.github/workflows/kilo.yml` in your repo. Set the appropriate `model` and required API keys.

   ```yml
   name: kilo

   on:
     issue_comment:
       types: [created]
     pull_request_review_comment:
       types: [created]

   jobs:
     kilo:
       if: |
         contains(github.event.comment.body, '/kc') ||
         contains(github.event.comment.body, '/kilo')
       runs-on: ubuntu-latest
       permissions:
         id-token: write
         contents: write
         pull-requests: write
         issues: write
       steps:
         - name: Checkout repository
           uses: actions/checkout@v6
           with:
             persist-credentials: false

         - name: Run Kilo
           uses: Kilo-Org/kilocode/github@latest
           with:
             model: kilo/claude-sonnet-4-20250514
             kilo_api_key: ${{ secrets.KILO_API_KEY }}
             kilo_org_id: ${{ secrets.KILO_ORG_ID }}
   ```

3. Store the API keys in secrets. In your organization or project **settings**, expand **Secrets and variables** on the left and select **Actions**. Add `KILO_API_KEY` and `KILO_ORG_ID`.

## Configuration

### Inputs

- `model` (required) - The AI model to use (e.g., `kilo/claude-sonnet-4-20250514`)
- `kilo_api_key` (optional) - Kilo API key for gateway authentication
- `kilo_org_id` (optional) - Kilo organization ID
- `agent` (optional) - Agent to use. Must be a primary agent.
- `share` (optional) - Share the Kilo session (defaults to true for public repos)
- `prompt` (optional) - Custom prompt to override the default prompt
- `mentions` (optional) - Comma-separated list of trigger phrases (defaults to `/kilo,/kc`)
- `use_github_token` (optional) - Use GITHUB_TOKEN directly instead of Kilo App token exchange (defaults to `false`)
- `oidc_base_url` (optional) - Base URL for OIDC token exchange API (defaults to `https://api.kilo.ai`)

### Using Other Providers

You can also use other AI providers by setting their API keys:

```yml
- name: Run Kilo
  uses: Kilo-Org/kilocode/github@latest
  with:
    model: anthropic/claude-sonnet-4-20250514
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Support

If you encounter issues or have feedback, please create an issue at https://github.com/Kilo-Org/kilocode/issues.

## Development

This directory contains the composite GitHub Action definition. The actual implementation is in the Kilo CLI (`packages/opencode/src/cli/cmd/github.ts`).

To test locally, see the main [AGENTS.md](../AGENTS.md) for development instructions.

```

### File: .opencode\glossary\README.md
```md
# Locale Glossaries

Use this folder for locale-specific translation guidance that supplements `.opencode/agent/translator.md`.

The global glossary in `translator.md` remains the source of truth for shared do-not-translate terms (commands, code, paths, product names, etc.). These locale files capture community learnings about phrasing and terminology preferences.

## File Naming

- One file per locale
- Use lowercase locale slugs that match docs locales when possible (for example, `zh-cn.md`, `zh-tw.md`)
- If only language-level guidance exists, use the language code (for example, `fr.md`)
- Some repo locale slugs may be aliases/non-BCP47 for consistency (for example, `br` for Brazilian Portuguese / `pt-BR`)

## What To Put In A Locale File

- **Sources**: PRs/issues/discussions that motivated the guidance
- **Do Not Translate (Locale Additions)**: locale-specific terms or casing decisions
- **Preferred Terms**: recurring UI/docs words with preferred translations
- **Guidance**: tone, style, and consistency notes
- **Avoid** (optional): common literal translations or wording we should avoid
- If the repo uses a locale alias slug, document the alias in **Guidance** (for example, prose may mention `pt-BR` while config/examples use `br`)

Prefer guidance that is:

- Repeated across multiple docs/screens
- Easy to apply consistently
- Backed by a community contribution or review discussion

## Template

```md
# <locale> Glossary

## Sources

- PR #12345: https://github.com/anomalyco/opencode/pull/12345

## Do Not Translate (Locale Additions)

- `OpenCode` (preserve casing)

## Preferred Terms

| English | Preferred | Notes     |
| ------- | --------- | --------- |
| prompt  | ...       | preferred |
| session | ...       | preferred |

## Guidance

- Prefer natural phrasing over literal translation

## Avoid

- Avoid ... when ...
```

## Contribution Notes

- Mark entries as preferred when they may evolve
- Keep examples short
- Add or update the `Sources` section whenever you add a new rule
- Prefer PR-backed guidance over invented term mappings; start with general guidance if no term-level corrections exist yet

```

### File: packages\app\package.json
```json
{
  "name": "@opencode-ai/app",
  "version": "7.1.20",
  "description": "",
  "type": "module",
  "exports": {
    ".": "./src/index.ts",
    "./vite": "./vite.js",
    "./index.css": "./src/index.css"
  },
  "scripts": {
    "typecheck": "tsgo -b",
    "start": "vite",
    "dev": "vite",
    "build": "vite build",
    "serve": "vite preview",
    "test": "bun run test:unit",
    "test:unit": "bun test --preload ./happydom.ts ./src",
    "test:unit:watch": "bun test --watch --preload ./happydom.ts ./src",
    "test:e2e": "playwright test",
    "test:e2e:local": "bun script/e2e-local.ts",
    "test:e2e:ui": "playwright test --ui",
    "test:e2e:report": "playwright show-report e2e/playwright-report"
  },
  "license": "MIT",
  "devDependencies": {
    "@happy-dom/global-registrator": "20.0.11",
    "@playwright/test": "1.57.0",
    "@tailwindcss/vite": "catalog:",
    "@tsconfig/bun": "1.0.9",
    "@types/bun": "catalog:",
    "@types/luxon": "catalog:",
    "@types/node": "catalog:",
    "@typescript/native-preview": "catalog:",
    "typescript": "catalog:",
    "vite": "catalog:",
    "vite-plugin-icons-spritesheet": "3.0.1",
    "vite-plugin-solid": "catalog:"
  },
  "dependencies": {
    "@kobalte/core": "catalog:",
    "@kilocode/sdk": "workspace:*",
    "@opencode-ai/ui": "workspace:*",
    "@opencode-ai/util": "workspace:*",
    "@shikijs/transformers": "3.9.2",
    "@solid-primitives/active-element": "2.1.3",
    "@solid-primitives/audio": "1.4.2",
    "@solid-primitives/i18n": "2.2.1",
    "@solid-primitives/event-bus": "1.1.2",
    "@solid-primitives/media": "2.3.3",
    "@solid-primitives/resize-observer": "2.1.3",
    "@solid-primitives/scroll": "2.1.3",
    "@solid-primitives/storage": "catalog:",
    "@solid-primitives/websocket": "1.3.1",
    "@solidjs/meta": "catalog:",
    "@solidjs/router": "catalog:",
    "@thisbeyond/solid-dnd": "0.7.5",
    "diff": "catalog:",
    "fuzzysort": "catalog:",
    "ghostty-web": "github:anomalyco/ghostty-web#main",
    "luxon": "catalog:",
    "marked": "catalog:",
    "marked-shiki": "catalog:",
    "remeda": "catalog:",
    "shiki": "catalog:",
    "solid-js": "catalog:",
    "solid-list": "catalog:",
    "tailwindcss": "catalog:",
    "virtua": "catalog:",
    "zod": "catalog:",
    "@kilocode/kilo-ui": "workspace:*",
    "@kilocode/kilo-i18n": "workspace:*"
  },
  "peerDependencies": {}
}

```

### File: packages\app\README.md
```md
## Usage

Dependencies for these templates are managed with [pnpm](https://pnpm.io) using `pnpm up -Lri`.

This is the reason you see a `pnpm-lock.yaml`. That said, any package manager will work. This file can safely be removed once you clone a template.

```bash
$ npm install # or pnpm install or yarn install
```

### Learn more on the [Solid Website](https://solidjs.com) and come chat with us on our [Discord](https://discord.com/invite/solidjs)

## Available Scripts

In the project directory, you can run:

### `npm run dev` or `npm start`

Runs the app in the development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br>

### `npm run build`

Builds the app for production to the `dist` folder.<br>
It correctly bundles Solid in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br>
Your app is ready to be deployed!

## E2E Testing

Playwright starts the Vite dev server automatically via `webServer`, and UI tests need an opencode backend (defaults to `localhost:4096`).
Use the local runner to create a temp sandbox, seed data, and run the tests.

```bash
bunx playwright install
bun run test:e2e:local
bun run test:e2e:local -- --grep "settings"
```

Environment options:

- `PLAYWRIGHT_SERVER_HOST` / `PLAYWRIGHT_SERVER_PORT` (backend address, default: `localhost:4096`)
- `PLAYWRIGHT_PORT` (Vite dev server port, default: `3000`)
- `PLAYWRIGHT_BASE_URL` (override base URL, default: `http://localhost:<PLAYWRIGHT_PORT>`)

## Deployment

You can deploy the `dist` folder to any static host provider (netlify, surge, now, etc.)

```

### File: AGENTS.md
```md
# AGENTS.md

Kilo CLI is an open source AI coding agent that generates code from natural language, automates tasks, and supports 500+ AI models.

- ALWAYS USE PARALLEL TOOLS WHEN APPLICABLE.
- The default branch in this repo is `main`.
- Prefer automation: execute requested actions without confirmation unless blocked by missing info or safety/irreversibility.
- You may be running in a git worktree. All changes must be made in your current working directory — never modify files in the main repo checkout.

## Build and Dev

- **Dev**: `bun run dev` (runs from root) or `bun run --cwd packages/opencode --conditions=browser src/index.ts`
- **Extension**: `bun run extension` (build + launch VS Code with the extension in dev mode). Pass `--no-build` to skip the build.
- **Typecheck**: `bun turbo typecheck` (uses `tsgo`, not `tsc`)
- **Test**: `bun test` from `packages/opencode/` (NOT from root -- root blocks tests)
- **Single test**: `bun test test/tool/tool.test.ts` from `packages/opencode/`
- **SDK regen**: After changing server endpoints in `packages/opencode/src/server/`, run `./script/generate.ts` from root to regenerate `packages/sdk/js/`
- **Knip** (unused exports): `bun run knip` from `packages/kilo-vscode/`. CI runs this — all exported types/functions must be imported somewhere. Remove or unexport unused exports before pushing.
- **Source links**: After adding or changing URLs in `packages/kilo-vscode/`, `packages/kilo-vscode/webview-ui/`, or `packages/opencode/src/`, run `bun run script/extract-source-links.ts` from the repo root and commit the updated `packages/kilo-docs/source-links.md`. CI runs this check — the build fails if the file is stale.
- **kilocode_change check**: `bun run check-kilocode-change` from `packages/kilo-vscode/`. CI runs this — `kilocode_change` is a marker for upstream merge conflicts and must not appear in `packages/kilo-vscode/` or `packages/kilo-ui/` (these are entirely Kilo Code additions). Remove the markers before pushing.

## Products

All products are clients of the **CLI** (`packages/opencode/`), which contains the AI agent runtime, HTTP server, and session management. Each client spawns or connects to a `kilo serve` process and communicates via HTTP + SSE using `@kilocode/sdk`.

| Product                | Package                 | Description                                                                                                                                                                          |
| ---------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kilo CLI               | `packages/opencode/`    | Core engine. TUI, `kilo run`, `kilo serve`, `kilo web`. Fork of upstream OpenCode.                                                                                                   |
| Kilo VS Code Extension | `packages/kilo-vscode/` | VS Code extension. Bundles the CLI binary, spawns `kilo serve` as a child process. Includes the **Agent Manager** — a multi-session orchestration panel with git worktree isolation. |
| OpenCode Desktop       | `packages/desktop/`     | Standalone Tauri native app. Bundles CLI as sidecar. Single-session UI. Unrelated to the VS Code extension. Not actively maintained — synced from upstream fork.                     |
| OpenCode Web           | `packages/app/`         | Shared SolidJS frontend used by both the desktop app and `kilo web` CLI command. Not actively maintained — synced from upstream fork.                                                |

**Agent Manager** refers to a feature inside `packages/kilo-vscode/` (extension code in `src/agent-manager/`, webview in `webview-ui/agent-manager/`). It is not a standalone product. See the extension's `AGENTS.md` for details.

## Monorepo Structure

Turborepo + Bun workspaces. The packages you'll work with most:

| Package                    | Name                       | Purpose                                                                                    |
| -------------------------- | -------------------------- | ------------------------------------------------------------------------------------------ |
| `packages/opencode/`       | `@kilocode/cli`            | Core CLI -- agents, tools, sessions, server, TUI. This is where most work happens.         |
| `packages/sdk/js/`         | `@kilocode/sdk`            | Auto-generated TypeScript SDK (client for the server API). Do not edit `src/gen/` by hand. |
| `packages/kilo-vscode/`    | `kilo-code`                | VS Code extension with sidebar chat + Agent Manager. See its own `AGENTS.md` for details.  |
| `packages/kilo-gateway/`   | `@kilocode/kilo-gateway`   | Kilo auth, provider routing, API integration                                               |
| `packages/kilo-telemetry/` | `@kilocode/kilo-telemetry` | PostHog analytics + OpenTelemetry                                                          |
| `packages/kilo-i18n/`      | `@kilocode/kilo-i18n`      | Internationalization / translations                                                        |
| `packages/kilo-ui/`        | `@kilocode/kilo-ui`        | SolidJS component library shared by the extension webview and `packages/app/`              |
| `packages/app/`            | `@opencode-ai/app`         | Shared SolidJS web UI for desktop app and `kilo web`                                       |
| `packages/desktop/`        | `@opencode-ai/desktop`     | Tauri desktop app shell                                                                    |
| `packages/util/`           | `@opencode-ai/util`        | Shared utilities (error, path, retry, slug, etc.)                                          |
| `packages/plugin/`         | `@kilocode/plugin`         | Plugin/tool interface definitions                                                          |

## Style Guide

- Keep things in one function unless composable or reusable
- Avoid unnecessary destructuring. Instead of `const { a, b } = obj`, use `obj.a` and `obj.b` to preserve context
- Avoid `try`/`catch` where possible
- Avoid using the `any` type
- Prefer single word variable names where possible
- Use Bun APIs when possible, like `Bun.file()`
- Rely on type inference when possible; avoid explicit type annotations or interfaces unless necessary for exports or clarity

### Avoid let statements

We don't like `let` statements, especially combined with if/else statements.
Prefer `const`.

Good:

### Naming Enforcement (Read This)

THIS RULE IS MANDATORY FOR AGENT WRITTEN CODE.

- Use single word names by default for new locals, params, and helper functions.
- Multi-word names are allowed only when a single word would be unclear or ambiguous.
- Do not introduce new camelCase compounds when a short single-word alternative is clear.
- Before finishing edits, review touched lines and shorten newly introduced identifiers where possible.
- Good short names to prefer: `pid`, `cfg`, `err`, `opts`, `dir`, `root`, `child`, `state`, `timeout`.
- Examples to avoid unless truly required: `inputPID`, `existingClient`, `connectTimeout`, `workerPath`.

```ts
const foo = condition ? 1 : 2
```

Bad:

```ts
let foo

if (condition) foo = 1
else foo = 2
```

### Avoid else statements

Prefer early returns or using an `iife` to avoid else statements.

Good:

```ts
function foo() {
  if (condition) return 1
  return 2
}
```

Bad:

```ts
function foo() {
  if (condition) return 1
  else return 2
}
```

### No empty catch blocks

Never leave a `catch` block empty. An empty `catch` silently swallows errors and hides bugs. If you're tempted to write one, ask yourself:

1. Is the `try`/`catch` even needed? (prefer removing it)
2. Should the error be handled explicitly? (recover, retry, rethrow)
3. At minimum, log it so failures are visible

Good:

```ts
try {
  await save(data)
} catch (err) {
  log.error("save failed", { err })
}
```

Bad:

```ts
try {
  await save(data)
} catch {}
```

### Prefer single word naming

Try your best to find a single word name for your variables, functions, etc.
Only use multiple words if you cannot.

Good:

```ts
const foo = 1
const bar = 2
const baz = 3
```

Bad:

```ts
const fooBar = 1
const barBaz = 2
const bazFoo = 3
```

## Testing

You MUST avoid using `mocks` as much as possible.
Tests MUST test actual implementation, do not duplicate logic into a test.

## Commit Conventions

[Conventional Commits](https://www.conventionalcommits.org/) with scopes matching packages: `vscode`, `cli`, `agent-manager`, `sdk`, `ui`, `i18n`, `kilo-docs`, `gateway`, `telemetry`, `desktop`. Omit scope when spanning multiple packages.

## Fork Merge Process

Kilo CLI is a fork of [opencode](https://github.com/anomalyco/opencode).

### Minimizing Merge Conflicts

We regularly merge upstream changes from opencode. To minimize merge conflicts and keep the sync process smooth:

1. **Prefer `kilocode` directories** - Place Kilo-specific code in dedicated directories whenever possible:
   - `packages/opencode/src/kilocode/` - Kilo-specific source code
   - `packages/opencode/test/kilocode/` - Kilo-specific tests
   - `packages/kilo-gateway/` - The Kilo Gateway package

2. **Minimize changes to shared files** - When you must modify files that exist in upstream opencode, keep changes as small and isolated as possible.

3. **Use `kilocode_change` markers** - When modifying shared code, mark your changes with `kilocode_change` comments so they can be easily identified during merges.
   Do not use these markers in files within directories with kilo in the name

4. **Avoid restructuring upstream code** - Don't refactor or reorganize code that comes from opencode unless absolutely necessary.

The goal is to keep our diff from upstream as small as possible, making regular merges straightforward and reducing the risk of conflicts.

### Kilocode Change Markers

To minimize merge conflicts when syncing with upstream, mark Kilo Code-specific changes in shared code with `kilocode_change` comments.

**Single line:**

```typescript
const value = 42 // kilocode_change
```

**Multi-line:**

```typescript
// kilocode_change start
const foo = 1
const bar = 2
// kilocode_change end
```

**New files:**

```typescript
// kilocode_change - new file
```

#### When markers are NOT needed

Code in these paths is Kilo Code-specific and does NOT need `kilocode_change` markers:

- `packages/opencode/src/kilocode/` - All files in this directory
- `packages/opencode/test/kilocode/` - All test files for kilocode
- Any other path containing `kilocode` in filename or directory name

These paths are entirely Kilo Code additions and won't conflict with upstream.

```

### File: CODE_OF_CONDUCT.md
```md
# Kilo Code Community Code of Conduct

## Our Pledge

We as community members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
hi@kilo.ai.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Kilo CLI

See [the Documentation for details on contributing](https://kilo.ai/docs/contributing).

## TL;DR

There are lots of ways to contribute to the project:

- **Code Contributions:** Implement new features or fix bugs
- **Documentation:** Improve existing docs or create new guides
- **Bug Reports:** Report issues you encounter
- **Feature Requests:** Suggest new features or improvements
- **Community Support:** Help other users in the community

The Kilo Community is [on Discord](https://kilo.ai/discord).

## Developing Kilo CLI

- **Requirements:** Bun 1.3.10+
- Install dependencies and start the dev server from the repo root:

  ```bash
  bun install
  bun dev
  ```

### Developing the VS Code Extension

Build and launch the extension in an isolated VS Code instance:

```bash
bun run extension        # Build + launch in dev mode
```

This auto-detects VS Code on macOS, Linux, and Windows. Override with `--app-path PATH` or `VSCODE_EXEC_PATH`. Use `--insiders` to prefer Insiders, `--workspace PATH` to open a specific folder, or `--clean` to reset cached state.

### Running against a different directory

By default, `bun dev` runs Kilo CLI in the `packages/opencode` directory. To run it against a different directory or repository:

```bash
bun dev <directory>
```

To run Kilo CLI in the root of the repo itself:

```bash
bun dev .
```

### Building a "local" binary

To compile a standalone executable:

```bash
./packages/opencode/script/build.ts --single
```

Then run it with:

```bash
./packages/opencode/dist/@kilocode/cli-<platform>/bin/kilo
```

Replace `<platform>` with your platform (e.g., `darwin-arm64`, `linux-x64`).

### Understanding bun dev vs kilo

During development, `bun dev` is the local equivalent of the built `kilo` command. Both run the same CLI interface:

```bash
# Development (from project root)
bun dev --help           # Show all available commands
bun dev serve            # Start headless API server
bun dev web              # Start server + open web interface

# Production
kilo --help          # Show all available commands
kilo serve           # Start headless API server
kilo web             # Start server + open web interface
```

### Testing with a local backend

To point the CLI at a local backend (e.g., a locally running Kilo API server on port 3000), set the `KILO_API_URL` environment variable:

```bash
KILO_API_URL=http://localhost:3000 bun dev
```

This redirects all gateway traffic (auth, model listing, provider routing, profile, etc.) to your local server. The default is `https://api.kilo.ai`.

There are also optional overrides for other services:

| Variable                  | Default                          | Purpose                                   |
| ------------------------- | -------------------------------- | ----------------------------------------- |
| `KILO_API_URL`            | `https://api.kilo.ai`            | Kilo API (gateway, auth, models, profile) |
| `KILO_SESSION_INGEST_URL` | `https://ingest.kilosessions.ai` | Session export / cloud sync               |
| `KILO_MODELS_URL`         | `https://models.dev`             | Model metadata                            |

> **VS Code:** The repo includes a "VSCode - Run Extension (Local Backend)" launch config in `.vscode/launch.json` that sets `KILO_API_URL=http://localhost:3000` automatically.

### Pull Request Expectations

- **Issue First Policy:** All PRs must reference an existing issue.
- **UI Changes:** Include screenshots or videos (before/after).
- **Logic Changes:** Explain how you verified it works.
- **PR Titles:** Follow conventional commit standards (`feat:`, `fix:`, `docs:`, etc.).

### Issue and PR Lifecycle

To keep our backlog manageable, we automatically close inactive issues and PRs after a period of inactivity. This isn't a judgment on quality — older items tend to lose context over time and we'd rather start fresh if they're still relevant. Feel free to reopen or create a new issue/PR if you're still working on something!

### Style Preferences

- **Functions:** Keep logic within a single function unless breaking it out adds clear reuse.
- **Destructuring:** Avoid unnecessary destructuring.
- **Control flow:** Avoid `else` statements; prefer early returns.
- **Types:** Avoid `any`.
- **Variables:** Prefer `const`.
- **Naming:** Concise single-word identifiers when descriptive.
- **Runtime APIs:** Use Bun helpers (e.g., `Bun.file()`).

```

### File: PRIVACY.md
```md
# Kilo CLI Privacy Policy

**Last Updated: March 7th, 2025**

Kilo CLI respects your privacy and is committed to transparency about how we handle your data. Below is a simple breakdown of where key pieces of data go—and, importantly, where they don't.

### **Where Your Data Goes (And Where It Doesn't)**

- **Code & Files**: Kilo CLI accesses files on your local machine when needed for AI-assisted features. When you send commands to Kilo CLI, relevant files may be transmitted to your chosen AI model provider (e.g., OpenAI, Anthropic, OpenRouter) to generate responses. We do not have access to this data, but AI providers may store it per their privacy policies.
- **Commands**: Any commands executed through Kilo CLI happen on your local environment. However, when you use AI-powered features, the relevant code and context from your commands may be transmitted to your chosen AI model provider (e.g., OpenAI, Anthropic, OpenRouter) to generate responses. We do not have access to or store this data, but AI providers may process it per their privacy policies.
- **Prompts & AI Requests**: When you use AI-powered features, your prompts and relevant project context are sent to your chosen AI model provider (e.g., OpenAI, Anthropic, OpenRouter) to generate responses. We do not store or process this data. These AI providers have their own privacy policies and may store data per their terms of service.
- **API Keys & Credentials**: If you enter an API key (e.g., to connect an AI model), it is stored locally on your device and never sent to us or any third party, except the provider you have chosen.

### **Your Choices & Control**

- You can run models locally to prevent data being sent to third-parties.

### **Security & Updates**

We take reasonable measures to secure your data, but no system is 100% secure. If our privacy policy changes, we will update this document and note the changes in our release notes.

### **Contact Us**

For any privacy-related questions, you can reach out to us at hi@kilo.ai.

---

By using Kilo CLI, you agree to this Privacy Policy.

```

### File: RELEASING.md
```md
# Releasing Kilo Code

Kilo Code uses a fully automated CI pipeline triggered via GitHub Actions `workflow_dispatch`. A single workflow handles version bumping, building all artifacts, publishing to every distribution channel, and updating package registries.

## How to Trigger a Release

1. Go to the [`publish` workflow](https://github.com/Kilo-Org/kilocode/actions/workflows/publish.yml) in GitHub Actions.
2. Click **"Run workflow"**.
3. Select the branch (typically `main`).
4. Fill in the inputs:
   - **`bump`** (choice): `patch`, `minor`, or `major`. Determines how the version number is incremented.
   - **`version`** (string, optional): Override the version explicitly instead of using `bump`. Leave empty to use the bump-based calculation.

   > **⚠️ Do not fill in `version` unless you have a specific reason to.**
   > The default behavior — leaving `version` empty and selecting a `bump` level — is almost always what you want. The automated bump logic computes the correct next version from the current state of the repo. Only use the `version` override for exceptional cases like skipping versions or publishing a pre-release (e.g. `1.5.0-beta.1`).

5. Click **"Run workflow"** to start the release.

## What Happens During a Release

The `publish.yml` workflow runs four jobs sequentially:

### 1. Version (`version`)

- Checks out the repo with full history (`fetch-depth: 0`).
- Runs `script/version.ts` to compute the next version based on the `bump` or `version` input.
- Generates release notes from the commit history since the last release.
- Creates a **draft** GitHub Release with the computed tag (e.g. `v1.2.3`) and release notes.
- Outputs the `version`, `release` (database ID), and `tag` for downstream jobs.

### 2. Build CLI (`build-cli`)

- Runs `packages/opencode/script/build.ts` to compile the Kilo CLI binary.
- Builds native binaries for **all supported platforms and architectures**:
  - Linux: x64, arm64 (glibc and musl), plus baseline (non-AVX2) variants
  - macOS: x64, arm64, plus baseline variants
  - Windows: x64 (plus baseline variant), arm64
- Patches ELF interpreters on Linux binaries for broad compatibility.
- Creates platform archives (`.tar.gz` for Linux, `.zip` for macOS/Windows) and uploads them to the draft GitHub Release.
- Uploads the `dist/` directory as a workflow artifact (`kilo-cli`) for subsequent jobs.

### 3. Build VS Code Extension (`build-vscode`)

- Downloads the CLI artifacts from the previous job.
- Runs `packages/kilo-vscode/script/build.ts` to build VSIX packages for all target platforms:
  - `linux-x64`, `linux-arm64`, `alpine-x64`, `alpine-arm64`, `darwin-x64`, `darwin-arm64`, `win32-x64`, `win32-arm64`
- Each VSIX bundles the platform-specific CLI binary.
- Uploads the VSIX files as a workflow artifact (`kilo-vscode`).

### 4. Publish (`publish`)

Downloads all build artifacts and publishes to every distribution channel:

#### Version Commit and Tagging

- Updates the `version` field in all `package.json` files across the monorepo.
- Updates the Zed extension manifest (`extension.toml`) with the new version.
- Rebuilds the TypeScript SDK (`packages/sdk/js`).
- Commits the version bump, tags the commit, and pushes to the repo.
- Promotes the draft GitHub Release to a published release.

#### CLI (`@kilocode/cli`)

- Publishes platform-specific binary packages to **npm** (e.g. `@kilocode/cli-linux-x64`, `@kilocode/cli-darwin-arm64`, etc.).
- Publishes the main `@kilocode/cli` package to **npm** with optional dependencies on the binary packages.
- Builds and pushes a multi-arch **Docker image** (`ghcr.io/kilo-org/kilo`) to GitHub Container Registry (linux/amd64 + linux/arm64).

#### SDK (`@kilocode/sdk`)

- Builds and publishes the TypeScript SDK to **npm**.

#### Plugin (`@kilocode/plugin`)

- Builds and publishes the plugin interface package to **npm**.

#### VS Code Extension

- Publishes platform-specific VSIX packages to the **VS Code Marketplace** via `vsce`.
- Uploads all VSIX files to the **GitHub Release** as assets.

#### Package Registries (stable releases only)

- **AUR (Arch Linux)**: Clones `kilo-bin` from the AUR, updates the `PKGBUILD` with new version and SHA256 checksums, and pushes.
- **Homebrew**: Clones `Kilo-Org/homebrew-tap`, updates the `kilo.rb` formula with new version, download URLs, and SHA256 checksums, and pushes.

## Prerequisites and Permissions

### Repository Access

- The workflow only runs in the `Kilo-Org/kilocode` repository (guarded by `if: github.repository == 'Kilo-Org/kilocode'`).
- You must have **write access** to the repository to trigger a `workflow_dispatch` event.

### Workflow Permissions

The workflow requires these GitHub token permissions:

- `id-token: write` -- for npm provenance attestation
- `contents: write` -- for creating releases, pushing tags, and uploading assets
- `packages: write` -- for publishing Docker images to GHCR

### Required Secrets

The following secrets must be configured in the repository:

| Secret                       | Purpose                                                          |
| ---------------------------- | ---------------------------------------------------------------- |
| `KILO_API_KEY`               | Kilo API key used during version computation                     |
| `KILO_ORG_ID`                | Kilo organization ID                                             |
| `KILO_MAINTAINER_APP_ID`     | GitHub App ID for the kilo-maintainer bot (used for git commits) |
| `KILO_MAINTAINER_APP_SECRET` | GitHub App secret for the kilo-maintainer bot                    |
| `NPM_TOKEN`                  | npm authentication token for publishing packages                 |
| `VSCE_TOKEN`                 | VS Code Marketplace personal access token                        |
| `OVSX_TOKEN`                 | Open VSX Registry token (currently unused but configured)        |
| `AUR_KEY`                    | SSH private key for pushing to the AUR                           |

### Concurrency

The workflow uses concurrency control (`workflow-ref-bump/version`) to prevent parallel releases from conflicting.

```

### File: SECURITY.md
```md
# Security

## IMPORTANT

We do not accept AI generated security reports. We receive a large number of
these and we absolutely do not have the resources to review them all. If you
submit one that will be an automatic ban from the project.

## Threat Model

### Overview

Kilo CLI is an AI-powered coding assistant that runs locally on your machine. It provides an agent system with access to powerful tools including shell execution, file operations, and web access.

### No Sandbox

Kilo CLI does **not** sandbox the agent. The permission system exists as a UX feature to help users stay aware of what actions the agent is taking - it prompts for confirmation before executing commands, writing files, etc. However, it is not designed to provide security isolation.

If you need true isolation, run Kilo CLI inside a Docker container or VM.

### Server Mode

Server mode is opt-in only. When enabled, set `KILO_SERVER_PASSWORD` to require HTTP Basic Auth. Without this, the server runs unauthenticated (with a warning). It is the end user's responsibility to secure the server - any functionality it provides is not a vulnerability.

### Out of Scope

| Category                        | Rationale                                                               |
| ------------------------------- | ----------------------------------------------------------------------- |
| **Server access when opted-in** | If you enable server mode, API access is expected behavior              |
| **Sandbox escapes**             | The permission system is not a sandbox (see above)                      |
| **LLM provider data handling**  | Data sent to your configured LLM provider is governed by their policies |
| **MCP server behavior**         | External MCP servers you configure are outside our trust boundary       |
| **Malicious config files**      | Users control their own config; modifying it is not an attack vector    |

---

# Reporting Security Issues

We value the contributions of the security research community and recognize the importance of a coordinated approach to vulnerability disclosure. If you have discovered a security vulnerability, we encourage you to let us know immediately. We welcome the opportunity to work with you to resolve the issue promptly.

Please email your findings to [security@kilo.ai](mailto:security@kilo.ai). We will acknowledge your report and work with you to resolve the issue.

After the initial reply to your report, the security team will keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

For more details, see our [Security Disclosure](https://kilo.ai/security) page.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
