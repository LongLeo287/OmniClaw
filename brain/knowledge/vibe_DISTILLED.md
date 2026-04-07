---
id: vibe
type: knowledge
owner: OA_Triage
---
# vibe
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "vibe-kanban",
  "version": "0.1.41",
  "private": true,
  "bin": {
    "vibe-kanban": "npx-cli/bin/cli.js"
  },
  "files": [
    "npx-cli/bin/cli.js",
    "npx-cli/dist/**"
  ],
  "scripts": {
    "lint": "pnpm run local-web:lint && pnpm run ui:lint && pnpm run backend:lint && node scripts/check-unused-i18n-keys.mjs",
    "format": "pnpm run backend:format && pnpm run web-core:format && pnpm run local-web:format && pnpm run remote-web:format",
    "check": "pnpm run local-web:legacy-path-guard && pnpm run local-web:check && pnpm run remote-web:check && pnpm run web-core:check && pnpm run ui:check && pnpm run backend:check",
    "dev": "export FRONTEND_PORT=$(node scripts/setup-dev-environment.js frontend) && export BACKEND_PORT=$(node scripts/setup-dev-environment.js backend) && export PREVIEW_PROXY_PORT=$(node scripts/setup-dev-environment.js preview_proxy) && export VK_ALLOWED_ORIGINS=\"http://localhost:${FRONTEND_PORT}\" && export VITE_VK_SHARED_API_BASE=${VK_SHARED_API_BASE:-} && concurrently \"pnpm run backend:dev:watch\" \"pnpm run local-web:dev\"",
    "test:npm": "./test-npm-package.sh",
    "local-web:lint": "pnpm --filter @vibe/local-web run lint",
    "local-web:legacy-path-guard": "./scripts/check-legacy-frontend-paths.sh",
    "web-core:format": "pnpm --filter @vibe/web-core run format",
    "web-core:check": "pnpm --filter @vibe/web-core run check",
    "local-web:dev": "cd packages/local-web && pnpm run dev -- --port ${FRONTEND_PORT:-3000}",
    "local-web:check": "pnpm --filter @vibe/local-web run check",
    "remote-web:check": "pnpm --filter @vibe/remote-web run check",
    "local-web:format": "pnpm --filter @vibe/local-web run format",
    "remote-web:format": "pnpm --filter @vibe/remote-web run format",
    "ui:lint": "pnpm --filter @vibe/ui run lint",
    "ui:check": "pnpm --filter @vibe/ui run check",
    "backend:lint": "cargo clippy --workspace --all-targets --features qa-mode -- -D warnings && cargo clippy --manifest-path crates/remote/Cargo.toml --all-targets -- -D warnings",
    "backend:format": "cargo fmt --all && cargo fmt --all --manifest-path crates/remote/Cargo.toml",
    "backend:dev": "BACKEND_PORT=$(node scripts/setup-dev-environment.js backend) pnpm run backend:dev:watch",
    "backend:check": "cargo check --workspace && cargo check --manifest-path crates/remote/Cargo.toml",
    "backend:dev:watch": "DISABLE_WORKTREE_CLEANUP=1 RUST_LOG=debug cargo watch -w crates -x 'run --bin server'",
    "dev:qa": "export FRONTEND_PORT=$(node scripts/setup-dev-environment.js frontend) && export BACKEND_PORT=$(node scripts/setup-dev-environment.js backend) && export PREVIEW_PROXY_PORT=$(node scripts/setup-dev-environment.js preview_proxy) && export VK_ALLOWED_ORIGINS=\"http://localhost:${FRONTEND_PORT}\" && export VITE_VK_SHARED_API_BASE=${VK_SHARED_API_BASE:-} && concurrently \"pnpm run backend:dev:watch:qa\" \"pnpm run local-web:dev\"",
    "generate-types": "cargo run --bin generate_types",
    "generate-types:check": "cargo run --bin generate_types -- --check",
    "remote:generate-types": "cargo run --manifest-path crates/remote/Cargo.toml --bin remote-generate-types",
    "remote:generate-types:check": "cargo run --manifest-path crates/remote/Cargo.toml --bin remote-generate-types -- --check",
    "prepare-db": "node scripts/prepare-db.js",
    "prepare-db:check": "node scripts/prepare-db.js --check",
    "build:bippy-bundle": "node scripts/build-bippy-bundle.mjs",
    "build:npx": "bash ./local-build.sh",
    "build:npx-cli": "cd npx-cli && npm ci && npm run build",
    "check:npx-cli": "tsc --noEmit -p npx-cli/tsconfig.json",
    "prepack": "pnpm run build:npx && pnpm run build:npx-cli",
    "remote:dev": "cd crates/remote && docker compose --env-file .env.remote up --build ; docker compose --env-file .env.remote down -v",
    "remote:dev:full": "cd crates/remote && docker compose --env-file .env.remote --profile relay --profile attachments up --build ; docker compose --env-file .env.remote down -v",
    "remote:dev:clean": "cd crates/remote && docker compose --env-file .env.remote --profile relay --profile attachments down -v --remove-orphans",
    "remote:prepare-db": "cd crates/remote && bash scripts/prepare-db.sh",
    "remote:prepare-db:check": "cd crates/remote && bash scripts/prepare-db.sh --check",
    "tauri:dev": "set -a && [ -f .env ] && . ./.env && set +a && export FRONTEND_PORT=$(node scripts/setup-dev-environment.js frontend) && export BACKEND_PORT=$(node scripts/setup-dev-environment.js backend) && export VK_ALLOWED_ORIGINS=\"http://localhost:${FRONTEND_PORT}\" && export DISABLE_WORKTREE_CLEANUP=1 && export RUST_LOG=debug && export VITE_VK_SHARED_API_BASE=${VK_SHARED_API_BASE:-} && cd crates/tauri-app && cargo tauri dev --config '{\"build\":{\"devUrl\":\"http://localhost:'\"${FRONTEND_PORT}\"'\"}}'",
    "tauri:build": "cd crates/tauri-app && cargo tauri build"
  },
  "devDependencies": {
    "@types/adm-zip": "^0.5.7",
    "@types/node": "^20.0.0",
    "bippy": "0.5.28",
    "concurrently": "^8.2.2",
    "esbuild": "^0.27.2",
    "jwt-decode": "^4.0.0",
    "typescript": "^5.7.0",
    "vite": "^7.3.1"
  },
  "engines": {
    "node": ">=20",
    "pnpm": ">=8"
  },
  "packageManager": "pnpm@10.13.1"
}

```

### File: README.md
```md
<p align="center">
  <a href="https://vibekanban.com">
    <picture>
      <source srcset="packages/public/vibe-kanban-logo-dark.svg" media="(prefers-color-scheme: dark)">
      <source srcset="packages/public/vibe-kanban-logo.svg" media="(prefers-color-scheme: light)">
      <img src="packages/public/vibe-kanban-logo.svg" alt="Vibe Kanban Logo">
    </picture>
  </a>
</p>

<p align="center">Get 10X more out of Claude Code, Gemini CLI, Codex, Amp and other coding agents...</p>
<p align="center">
  <a href="https://www.npmjs.com/package/vibe-kanban"><img alt="npm" src="https://img.shields.io/npm/v/vibe-kanban?style=flat-square" /></a>
  <a href="https://github.com/BloopAI/vibe-kanban/blob/main/.github/workflows/publish.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/BloopAI/vibe-kanban/.github%2Fworkflows%2Fpublish.yml" /></a>
  <a href="https://deepwiki.com/BloopAI/vibe-kanban"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<h1 align="center">
  <a href="https://jobs.polymer.co/vibe-kanban?source=github"><strong>We're hiring!</strong></a>
</h1>

![](packages/public/vibe-kanban-screenshot-overview.png)

## Overview

In a world where software engineers spend most of their time planning and reviewing coding agents, the most impactful way to ship more is to get faster at planning and review.

Vibe Kanban is built for this. Use kanban issues to plan work, either privately or with your team. When you're ready to begin, create workspaces where coding agents can execute.

- **Plan with kanban issues** — create, prioritise, and assign issues on a kanban board
- **Run coding agents in workspaces** — each workspace gives an agent a branch, a terminal, and a dev server
- **Review diffs and leave inline comments** — send feedback directly to the agent without leaving the UI
- **Preview your app** — built-in browser with devtools, inspect mode, and device emulation
- **Switch between 10+ coding agents** — Claude Code, Codex, Gemini CLI, GitHub Copilot, Amp, Cursor, OpenCode, Droid, CCR, and Qwen Code
- **Create pull requests and merge** — open PRs with AI-generated descriptions, review on GitHub, and merge

![](packages/public/vibe-kanban-screenshot-workspace.png)

One command. Describe the work, review the diff, ship it.

```bash
npx vibe-kanban
```


## Installation

Make sure you have authenticated with your favourite coding agent. A full list of supported coding agents can be found in the [docs](https://vibekanban.com/docs/supported-coding-agents). Then in your terminal run:

```bash
npx vibe-kanban
```

## Documentation

Head to the [website](https://vibekanban.com/docs) for the latest documentation and user guides.

## Self-Hosting

Want to host your own Vibe Kanban Cloud instance? See our [self-hosting guide](https://vibekanban.com/docs/self-hosting/deploy-docker).

## Support

We use [GitHub Discussions](https://github.com/BloopAI/vibe-kanban/discussions) for feature requests. Please open a discussion to create a feature request. For bugs please open an issue on this repo.

## Contributing

We would prefer that ideas and changes are first raised with the core team via [GitHub Discussions](https://github.com/BloopAI/vibe-kanban/discussions) or [Discord](https://discord.gg/AC4nwVtJM3), where we can discuss implementation details and alignment with the existing roadmap. Please do not open PRs without first discussing your proposal with the team.

## Development

### Prerequisites

- [Rust](https://rustup.rs/) (latest stable)
- [Node.js](https://nodejs.org/) (>=20)
- [pnpm](https://pnpm.io/) (>=8)

Additional development tools:
```bash
cargo install cargo-watch
cargo install sqlx-cli
```

Install dependencies:
```bash
pnpm i
```

### Running the dev server

```bash
pnpm run dev
```

This will start the backend and web app. A blank DB will be copied from the `dev_assets_seed` folder.

### Building the web app

To build just the web app:

```bash
cd packages/local-web
pnpm run build
```

### Build from source (macOS)

1. Run `./local-build.sh`
2. Test with `cd npx-cli && node bin/cli.js`

### Environment Variables

The following environment variables can be configured at build time or runtime:

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `POSTHOG_API_KEY` | Build-time | Empty | PostHog analytics API key (disables analytics if empty) |
| `POSTHOG_API_ENDPOINT` | Build-time | Empty | PostHog analytics endpoint (disables analytics if empty) |
| `PORT` | Runtime | Auto-assign | **Production**: Server port. **Dev**: Frontend port (backend uses PORT+1) |
| `BACKEND_PORT` | Runtime | `0` (auto-assign) | Backend server port (dev mode only, overrides PORT+1) |
| `FRONTEND_PORT` | Runtime | `3000` | Frontend dev server port (dev mode only, overrides PORT) |
| `HOST` | Runtime | `127.0.0.1` | Backend server host |
| `MCP_HOST` | Runtime | Value of `HOST` | MCP server connection host (use `127.0.0.1` when `HOST=0.0.0.0` on Windows) |
| `MCP_PORT` | Runtime | Value of `BACKEND_PORT` | MCP server connection port |
| `DISABLE_WORKTREE_CLEANUP` | Runtime | Not set | Disable all git worktree cleanup including orphan and expired workspace cleanup (for debugging) |
| `VK_ALLOWED_ORIGINS` | Runtime | Not set | Comma-separated list of origins that are allowed to make backend API requests (e.g., `https://my-vibekanban-frontend.com`) |
| `VK_SHARED_API_BASE` | Runtime | Not set | Base URL for the remote/cloud API used by the local desktop app |
| `VK_SHARED_RELAY_API_BASE` | Runtime | Not set | Base URL for the relay API used by tunnel-mode connections |
| `VK_TUNNEL` | Runtime | Not set | Enable relay tunnel mode when set (requires relay API base URL) |

**Build-time variables** must be set when running `pnpm run build`. **Runtime variables** are read when the application starts.

#### Self-Hosting with a Reverse Proxy or Custom Domain

When running Vibe Kanban behind a reverse proxy (e.g., nginx, Caddy, Traefik) or on a custom domain, you must set the `VK_ALLOWED_ORIGINS` environment variable. Without this, the browser's Origin header won't match the backend's expected host, and API requests will be rejected with a 403 Forbidden error.

Set it to the full origin URL(s) where your frontend is accessible:

```bash
# Single origin
VK_ALLOWED_ORIGINS=https://vk.example.com

# Multiple origins (comma-separated)
VK_ALLOWED_ORIGINS=https://vk.example.com,https://vk-staging.example.com
```

### Remote Deployment

When running Vibe Kanban on a remote server (e.g., via systemctl, Docker, or cloud hosting), you can configure your editor to open projects via SSH:

1. **Access via tunnel**: Use Cloudflare Tunnel, ngrok, or similar to expose the web UI
2. **Configure remote SSH** in Settings → Editor Integration:
   - Set **Remote SSH Host** to your server hostname or IP
   - Set **Remote SSH User** to your SSH username (optional)
3. **Prerequisites**:
   - SSH access from your local machine to the remote server
   - SSH keys configured (passwordless authentication)
   - VSCode Remote-SSH extension

When configured, the "Open in VSCode" buttons will generate URLs like `vscode://vscode-remote/ssh-remote+user@host/path` that open your local editor and connect to the remote server.

See the [documentation](https://vibekanban.com/docs/settings/general) for detailed setup instructions.

```

### File: docs\README.md
```md
# Mintlify Starter Kit

**[Mintlify Quickstart Guide](https://starter.mintlify.com/quickstart)**

## Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) to preview your documentation changes locally. To install, use the following command:

```
npm i -g mint
```

Run the following command at the root of your documentation, where your `docs.json` is located:

```
mint dev
```

View your local preview at `http://localhost:3000`.

## Publishing changes

Install our GitHub app from your [dashboard](https://dashboard.mintlify.com/settings/organization/github-app) to propagate changes from your repo to your deployment. Changes are deployed to production automatically after pushing to the default branch.

## Need help?

### Troubleshooting

- If your dev environment isn't running: Run `mint update` to ensure you have the most recent version of the CLI.
- If a page loads as a 404: Make sure you are running in a folder with a valid `docs.json`.

### Resources
- [Mintlify documentation](https://mintlify.com/docs)
- [Mintlify community](https://mintlify.com/community)

```

### File: crates\remote\README.md
```md
# Remote Service

The `remote` crate contains the hosted API and web app.

## Local Setup

Create `crates/remote/.env.remote`:

```env
# Required
VIBEKANBAN_REMOTE_JWT_SECRET=replace_with_openssl_rand_base64_48
ELECTRIC_ROLE_PASSWORD=replace_with_secure_password

# Configure at least one auth option
GITHUB_OAUTH_CLIENT_ID=
GITHUB_OAUTH_CLIENT_SECRET=
GOOGLE_OAUTH_CLIENT_ID=
GOOGLE_OAUTH_CLIENT_SECRET=

# Or use bootstrap local auth for self-hosting
SELF_HOST_LOCAL_AUTH_EMAIL=
SELF_HOST_LOCAL_AUTH_PASSWORD=

# Optional
PUBLIC_BASE_URL=http://localhost:3000
VITE_RELAY_API_BASE_URL=http://localhost:8082
VITE_PUBLIC_REACT_VIRTUOSO_LICENSE_KEY=
LOOPS_EMAIL_API_KEY=

# Loops transactional email template IDs (optional — defaults are the upstream templates).
# Override these with your own Loops account template IDs if using a custom Loops account.
LOOPS_INVITE_TEMPLATE_ID=cmhvy2wgs3s13z70i1pxakij9
LOOPS_REVIEW_READY_TEMPLATE_ID=cmj47k5ge16990iylued9by17
LOOPS_REVIEW_FAILED_TEMPLATE_ID=cmj49ougk1c8s0iznavijdqpo
```

Generate the JWT secret once:

```bash
openssl rand -base64 48
```

## Run

From the repo root:

```bash
pnpm run remote:dev
```

Full stack with relay and local attachment storage:

```bash
pnpm run remote:dev:full
```

Equivalent manual command:

```bash
cd crates/remote
docker compose --env-file .env.remote up --build
```

This starts:

- `remote-db`
- `remote-server`
- `electric`

Default endpoints:

- Remote web UI/API: `http://localhost:3000`
- Postgres: `postgres://remote:remote@localhost:5433/remote`

## Optional Profiles

Enable relay support:

```bash
cd crates/remote
docker compose --env-file .env.remote --profile relay up --build
```

Enable local attachment storage with Azurite:

```bash
cd crates/remote
docker compose --env-file .env.remote --profile attachments up --build
```

Enable both:

```bash
cd crates/remote
docker compose --env-file .env.remote --profile relay --profile attachments up --build
```

Additional endpoint with the `relay` profile:

- Relay API: `http://localhost:8082`

## Local HTTPS with Caddy (Optional)

Use [Caddy](https://caddyserver.com) as a reverse proxy to terminate TLS locally. A `Caddyfile.example` is provided in the repository root.

### Install Caddy

```bash
# macOS
brew install caddy

# Debian/Ubuntu
sudo apt install caddy
```

### Start Caddy

In a separate terminal from the repo root:

```bash
caddy run --config Caddyfile.example
```

The first time Caddy runs it installs a local CA certificate — you may be prompted for your password.

This gives you:

- `https://localhost:3001` → remote web UI/API
- `https://relay.localhost:3001` → relay API (requires `relay` profile)

Update your OAuth callback URLs accordingly:

- **GitHub**: `https://localhost:3001/v1/oauth/github/callback`
- **Google**: `https://localhost:3001/v1/oauth/google/callback`

### Test relay tunnel end-to-end

```bash
export VK_SHARED_API_BASE=https://localhost:3001
export VK_SHARED_RELAY_API_BASE=https://relay.localhost:3001

pnpm run dev
```

Quick checks:

```bash
curl -sk https://localhost:3001/v1/health
curl -sk https://relay.localhost:3001/health
```

If the relay health endpoint returns HTML instead of `{"status":"ok"}`, your Caddy host routing is incorrect.

## Desktop App

To run the desktop/local app against this remote stack:

```bash
export VK_SHARED_API_BASE=http://localhost:3000
pnpm run dev
```

```

### File: packages\ui\package.json
```json
{
  "name": "@vibe/ui",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "check": "tsc --noEmit -p tsconfig.json",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "format": "prettier --config ../../packages/local-web/.prettierrc.json --write \"src/**/*.{ts,tsx,js,jsx,json,md}\"",
    "format:check": "prettier --config ../../packages/local-web/.prettierrc.json --check \"src/**/*.{ts,tsx,js,jsx,json,md}\""
  },
  "sideEffects": false,
  "exports": {
    "./components/*": "./src/components/*.tsx",
    "./lib/*": "./src/lib/*.ts"
  },
  "dependencies": {
    "@ebay/nice-modal-react": "^1.2.13",
    "@tanstack/react-virtual": "^3.13.23",
    "@hello-pangea/dnd": "^18.0.1",
    "@lexical/code": "^0.36.2",
    "@lexical/link": "^0.36.2",
    "@lexical/list": "^0.36.2",
    "@lexical/markdown": "^0.36.2",
    "@lexical/react": "^0.36.2",
    "@lexical/table": "^0.36.2",
    "@phosphor-icons/react": "^2.1.10",
    "@pierre/diffs": "1.1.4",
    "@radix-ui/react-accordion": "^1.2.1",
    "@radix-ui/react-dialog": "^1.1.4",
    "@radix-ui/react-dropdown-menu": "^2.1.15",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-select": "^2.2.5",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-switch": "^1.2.3",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@tanstack/react-query": "^5.85.5",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "developer-icons": "^6.0.4",
    "lexical": "^0.36.2",
    "lucide-react": "^0.541.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-hotkeys-hook": "^5.1.0",
    "react-i18next": "^15.7.4",
    "react-virtuoso": "^4.14.0",
    "tailwind-merge": "^3.3.1"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@typescript-eslint/eslint-plugin": "^6.21.0",
    "@typescript-eslint/parser": "^6.21.0",
    "eslint": "^8.55.0",
    "eslint-config-prettier": "^10.1.5",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-unused-imports": "^4.1.4",
    "prettier": "^3.6.1",
    "typescript": "^5.9.2"
  }
}

```

### File: packages\ui\README.md
```md
# @vibe/ui

Shared UI package for reusable web app primitives.

## Scope (initial)

- Package scaffold and exports.
- Shared utility helpers (`cn`).
- Tailwind class generation remains configured in `packages/local-web/tailwind.new.config.js`.

## Notes

- Tailwind scanning for this package is enabled from `packages/local-web/tailwind.new.config.js` via:
  `../ui/src/**/*.{ts,tsx}`.
- The app-level stylesheet remains `packages/web-core/src/styles/new/index.css`.

```

### File: AGENTS.md
```md
# Repository Guidelines

## Project Structure & Module Organization
- `crates/`: Rust workspace crates — `server` (API + bins), `db` (SQLx models/migrations), `executors`, `services`, `utils`, `git` (Git operations), `api-types` (shared API types for local + remote), `review` (PR review tool), `deployment`, `local-deployment`, `remote`.
- `packages/local-web/`: Local React + TypeScript app entrypoint (Vite, Tailwind). Shell source in `packages/local-web/src`.
- `packages/remote-web/`: Remote deployment frontend entrypoint.
- `packages/web-core/`: Shared React + TypeScript frontend library used by local + remote web (`packages/web-core/src`).
- `shared/`: Generated TypeScript types (`shared/types.ts`, `shared/remote-types.ts`) and agent tool schemas (`shared/schemas/`). Do not edit generated files directly.
- `assets/`, `dev_assets_seed/`, `dev_assets/`: Packaged and local dev assets.
- `npx-cli/`: Files published to the npm CLI package.
- `scripts/`: Dev helpers (ports, DB preparation).
- `docs/`: Documentation files.

### Crate-specific guides
- [`crates/remote/AGENTS.md`](crates/remote/AGENTS.md) — Remote server architecture, ElectricSQL integration, mutation patterns, environment variables.
- [`docs/AGENTS.md`](docs/AGENTS.md) — Mintlify documentation writing guidelines and component reference.
- [`packages/local-web/AGENTS.md`](packages/local-web/AGENTS.md) — Web app design system styling guidelines.

## Managing Shared Types Between Rust and TypeScript

ts-rs allows you to derive TypeScript types from Rust structs/enums. By annotating your Rust types with #[derive(TS)] and related macros, ts-rs will generate .ts declaration files for those types.
When making changes to the types, you can regenerate them using `pnpm run generate-types`
Do not manually edit shared/types.ts, instead edit crates/server/src/bin/generate_types.rs

For remote/cloud types, regenerate using `pnpm run remote:generate-types`
Do not manually edit shared/remote-types.ts, instead edit crates/remote/src/bin/remote-generate-types.rs (see crates/remote/AGENTS.md for details).

## Build, Test, and Development Commands
- Install: `pnpm i`
- Run dev (web app + backend with ports auto-assigned): `pnpm run dev`
- Backend (watch): `pnpm run backend:dev:watch`
- Web app (dev): `pnpm run local-web:dev`
- Type checks: `pnpm run check` (frontend + all backend Rust workspaces) and `pnpm run backend:check` (all backend Rust workspaces, including `crates/remote`)
- Rust tests: `cargo test --workspace`
- Generate TS types from Rust: `pnpm run generate-types` (or `generate-types:check` in CI)
- Prepare SQLx (offline): `pnpm run prepare-db`
- Prepare SQLx (remote package, postgres): `pnpm run remote:prepare-db`
- Local NPX build: `pnpm run build:npx` then `pnpm pack` in `npx-cli/`
- Format code: `pnpm run format` (runs `cargo fmt` for all backend Rust workspaces + web-core/web Prettier)
- Lint: `pnpm run lint` (runs web/ui ESLint + `cargo clippy` for all backend Rust workspaces)

## Before Completing a Task
- Run `pnpm run format` to format all Rust workspaces and web code.

## Coding Style & Naming Conventions
- Rust: `rustfmt` enforced (`rustfmt.toml`); group imports by crate; snake_case modules, PascalCase types.
- TypeScript/React: ESLint + Prettier (2 spaces, single quotes, 80 cols). PascalCase components, camelCase vars/functions, kebab-case file names where practical.
- Keep functions small, add `Debug`/`Serialize`/`Deserialize` where useful.

## Testing Guidelines
- Rust: prefer unit tests alongside code (`#[cfg(test)]`), run `cargo test --workspace`. Add tests for new logic and edge cases.
- Web app: ensure `pnpm run check` and `pnpm run lint` pass. If adding runtime logic, include lightweight tests (e.g., Vitest) in the same directory.

## Security & Config Tips
- Use `.env` for local overrides; never commit secrets. Key envs: `FRONTEND_PORT`, `BACKEND_PORT`, `HOST` 
- Dev ports and assets are managed by `scripts/setup-dev-environment.js`.



```

### File: CLAUDE.md
```md
AGENTS.md
```

### File: CODE-OF-CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

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
- Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or advances of
  any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email address,
  without their explicit permission
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
maintainers@bloop.ai through e-mail, with an appropriate subject line.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Next.js project][nextjs-coc]

The original text is from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[nextjs-coc]: https://raw.githubusercontent.com/vercel/next.js/canary/CODE_OF_CONDUCT.md
[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```

### File: CONTRIBUTORS.md
```md
# Contributing & Change Control

## Change Control Policy

All changes to production code are governed by formal change control procedures. These procedures ensure that modifications are reviewed, approved, and deployed in a controlled manner.

## Code Review Requirements

A maintainer must review pull requests before they are merged into any production branch. No code changes shall be merged without explicit approval from a qualified reviewer.

## Pull Request Process

1. Create a feature or fix branch from the base branch.
2. Make changes and open a pull request.
3. Obtain the required review and approval from a maintainer.
4. All required CI checks must pass before merging.
5. Merge only after approval has been granted and CI checks have passed.

## Separation of Duties

Development, testing, and deployment of changes shall not be performed by a single individual without approval and oversight. All significant changes require independent review to ensure correctness, security, and alignment with project standards.

## Coding Practices

Contributors are expected to follow the project's coding standards throughout the development cycle. These standards cover code quality, style consistency, and security.

### Style & Formatting

- **Rust**: Code must be formatted with `rustfmt` (config in `rustfmt.toml`). Use `snake_case` for modules and functions, `PascalCase` for types. Group imports by crate.
- **TypeScript/React**: Code must pass ESLint and Prettier (2 spaces, single quotes, 80-column width). Use `PascalCase` for components, `camelCase` for variables and functions, and `kebab-case` for file names.
- Run `pnpm run format` before submitting a pull request.
- Run `pnpm run lint` to verify there are no linting errors.

### Code Quality

- Keep functions small and focused on a single responsibility.
- Write clear, self-documenting code. Add comments only where the logic is not self-evident.
- Do not introduce unnecessary abstractions or over-engineer solutions.
- Do not manually edit generated files (e.g., `shared/types.ts`). Modify the source and regenerate.

### Testing

- **Rust**: Add unit tests alongside code using `#[cfg(test)]`. Run `cargo test --workspace` to verify.
- **TypeScript**: Ensure `pnpm run check` and `pnpm run lint` pass. Include lightweight tests (e.g., Vitest) for new runtime logic.
- All CI checks must pass before a pull request can be merged.

### Security

- Never commit secrets, credentials, or API keys. Use `.env` for local configuration.
- Be mindful of common vulnerabilities (injection, XSS, insecure deserialization) when writing code that handles user input or external data.
- Report security issues privately to the maintainers rather than opening a public issue.

### Commit Messages

- Use clear, descriptive commit messages that explain the _why_ behind a change.
- Prefix with a conventional type where appropriate (e.g., `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`).
- Keep the subject line under 72 characters. Use the body for additional context if needed.

## Scope

These procedures apply to all production branches in this repository.

```

### File: local-build.sh
```sh
#!/bin/bash

set -e  # Exit on any error

# Detect OS and architecture
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

# Map architecture names
case "$ARCH" in
  x86_64)
    ARCH="x64"
    ;;
  arm64|aarch64)
    ARCH="arm64"
    ;;
  *)
    echo "⚠️  Warning: Unknown architecture $ARCH, using as-is"
    ;;
esac

# Map OS names
case "$OS" in
  linux)
    OS="linux"
    ;;
  darwin)
    OS="macos"
    ;;
  *)
    echo "⚠️  Warning: Unknown OS $OS, using as-is"
    ;;
esac

PLATFORM="${OS}-${ARCH}"

# Set CARGO_TARGET_DIR if not defined
if [ -z "$CARGO_TARGET_DIR" ]; then
  CARGO_TARGET_DIR="target"
fi

echo "🔍 Detected platform: $PLATFORM"
echo "🔧 Using target directory: $CARGO_TARGET_DIR"

# Set API base URL for remote features
export VK_SHARED_API_BASE="https://api.vibekanban.com"
export VITE_VK_SHARED_API_BASE="https://api.vibekanban.com"

echo "🧹 Cleaning previous builds..."
rm -rf npx-cli/dist
mkdir -p npx-cli/dist/$PLATFORM

echo "🔨 Building web app..."
(cd packages/local-web && npm run build)

echo "🔨 Building Rust binaries..."
cargo build --release --manifest-path Cargo.toml
cargo build --release --bin vibe-kanban-mcp --manifest-path Cargo.toml

echo "📦 Creating distribution package..."

# Copy the main binary
cp ${CARGO_TARGET_DIR}/release/server vibe-kanban
zip -q vibe-kanban.zip vibe-kanban
rm -f vibe-kanban 
mv vibe-kanban.zip npx-cli/dist/$PLATFORM/vibe-kanban.zip

# Copy the MCP binary
cp ${CARGO_TARGET_DIR}/release/vibe-kanban-mcp vibe-kanban-mcp
zip -q vibe-kanban-mcp.zip vibe-kanban-mcp
rm -f vibe-kanban-mcp
mv vibe-kanban-mcp.zip npx-cli/dist/$PLATFORM/vibe-kanban-mcp.zip

# Copy the Review CLI binary
cp ${CARGO_TARGET_DIR}/release/review vibe-kanban-review
zip -q vibe-kanban-review.zip vibe-kanban-review
rm -f vibe-kanban-review
mv vibe-kanban-review.zip npx-cli/dist/$PLATFORM/vibe-kanban-review.zip

echo "✅ CLI build complete!"
echo "📁 Files created:"
echo "   - npx-cli/dist/$PLATFORM/vibe-kanban.zip"
echo "   - npx-cli/dist/$PLATFORM/vibe-kanban-mcp.zip"
echo "   - npx-cli/dist/$PLATFORM/vibe-kanban-review.zip"

# Optionally build the Tauri desktop app
if [[ "$1" == "--desktop" || "$1" == "--all" ]]; then
  # Map to Tauri platform naming
  case "$OS" in
    macos) TAURI_OS="darwin" ;;
    linux) TAURI_OS="linux" ;;
    *) TAURI_OS="$OS" ;;
  esac
  case "$ARCH" in
    arm64) TAURI_ARCH="aarch64" ;;
    x64) TAURI_ARCH="x86_64" ;;
    *) TAURI_ARCH="$ARCH" ;;
  esac
  TAURI_PLATFORM="${TAURI_OS}-${TAURI_ARCH}"

  echo ""
  echo "🖥️  Building Tauri desktop app for $TAURI_PLATFORM..."

  # Replace the updater endpoint placeholder with a dummy URL for local builds
  # (CI injects the real R2 URL; locally the updater is non-functional)
  TAURI_CONF="crates/tauri-app/tauri.conf.json"
  node -e "
    const fs = require('fs');
    const conf = JSON.parse(fs.readFileSync('$TAURI_CONF', 'utf8'));
    conf.plugins.updater.endpoints = conf.plugins.updater.endpoints.map(e =>
      e === '__TAURI_UPDATE_ENDPOINT__' ? 'https://localhost/disabled' : e
    );
    fs.writeFileSync('$TAURI_CONF', JSON.stringify(conf, null, 2) + '\n');
  "

  cargo tauri build

  # Restore tauri.conf.json
  git checkout -- "$TAURI_CONF"

  TAURI_DIST="npx-cli/dist/tauri/$TAURI_PLATFORM"
  mkdir -p "$TAURI_DIST"

  BUNDLE_DIR="${CARGO_TARGET_DIR}/release/bundle"
  # Copy updater artifacts (tar.gz bundles or NSIS exe)
  find "$BUNDLE_DIR" -name "*.app.tar.gz" ! -name "*.sig" -exec cp {} "$TAURI_DIST/" \; 2>/dev/null || true
  find "$BUNDLE_DIR" -name "*.AppImage.tar.gz" ! -name "*.sig" -exec cp {} "$TAURI_DIST/" \; 2>/dev/null || true
  find "$BUNDLE_DIR" -name "*-setup.exe" -exec cp {} "$TAURI_DIST/" \; 2>/dev/null || true

  echo "✅ Desktop app built:"
  ls -la "$TAURI_DIST/"
fi

echo ""
echo "📦 Installing npx-cli dependencies..."
(cd npx-cli && npm ci)

echo ""
echo "🔨 Building npx-cli TypeScript..."
(cd npx-cli && npm run build)

echo ""
echo "🚀 To test locally, run:"
echo "   cd npx-cli && node bin/cli.js                # browser mode (default)"
echo "   cd npx-cli && node bin/cli.js --desktop       # desktop mode (requires --desktop or --all build flag)"

```

### File: mobile-testing.md
```md
# Testing on Mobile Devices

This guide explains how to access the remote-web frontend from a phone (iPhone/Android) for UI testing. It uses [Tailscale](https://tailscale.com) for stable networking and HTTPS certificates, and [Caddy](https://caddyserver.com) as a reverse proxy — no custom IPs, no random URLs, works on any network.

**Time to set up**: ~15 minutes (one-time). After that, it's two commands in two terminals.

---

## Prerequisites

### 1. Install Tailscale on your Mac

Download the standalone app from https://tailscale.com/download/mac (recommended). Alternatively, install from the [Mac App Store](https://apps.apple.com/app/tailscale/id1470499037).

After installing:

1. Open the Tailscale app
2. Click the Tailscale icon in your menu bar (top-right of screen)
3. Click **Log in** — this opens a browser window to sign in
4. Once signed in, the icon turns active — you're connected

> If you already have Tailscale installed, skip this step.

### 2. Install Tailscale on your phone

- **iPhone**: [App Store — Tailscale](https://apps.apple.com/app/tailscale/id1470499037)
- **Android**: [Play Store — Tailscale](https://play.google.com/store/apps/details?id=com.tailscale.ipn)

Sign in with the **same account** you used on your Mac.

### 3. Install Caddy on your Mac

```bash
brew install caddy
```

### 4. Verify both devices are connected

Click the Tailscale icon in your Mac menu bar — you should see your Mac listed as connected. You can also verify from the terminal:

```bash
tailscale status
```

Both your Mac and phone should appear:

```
100.x.x.x   johns-macbook     user@   macOS   -
100.x.x.x   iphone-john      user@   iOS     -
```

> If your phone shows "offline", open the Tailscale app on your phone and make sure the toggle is ON.

### 5. Enable MagicDNS and HTTPS Certificates

1. Open https://login.tailscale.com/admin/dns
2. Scroll to the **Nameservers** section — make sure **MagicDNS** is enabled. If you see a "Disable MagicDNS..." button, it's already enabled.
3. Scroll to the bottom of the page to the **"HTTPS Certificates"** section
4. Click **"Enable HTTPS"** if it's not already enabled. If you see a "Disable HTTPS..." button, it's already enabled.

> Enabling HTTPS means your machine names and tailnet DNS name will appear on a public certificate ledger. This is how Let's Encrypt works and is normal.

---

## One-Time Setup

All commands below auto-detect your Tailscale hostname — no manual copy-pasting needed.

### Step 1 — Save your hostname to your shell profile

Run the command for your shell:

**zsh** (default on macOS):
```bash
echo "export TS_HOSTNAME=$(tailscale status --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))")" >> ~/.zshrc
source ~/.zshrc
```

**bash**:
```bash
echo "export TS_HOSTNAME=$(tailscale status --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))")" >> ~/.bashrc
source ~/.bashrc
```

**fish**:
```bash
set -Ux TS_HOSTNAME (tailscale status --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))") 
```

Verify it worked:
```bash
echo "Your hostname: $TS_HOSTNAME"
```

Verify it resolves:

```bash
ping -c 1 $TS_HOSTNAME
```

### Step 2 — Generate HTTPS certificates

```bash
tailscale cert $TS_HOSTNAME
```

This creates `$TS_HOSTNAME.crt` and `$TS_HOSTNAME.key` in the current directory. These are real Let's Encrypt certificates — trusted by all browsers and devices, no extra installation needed on your phone.

> Certs expire after 90 days. Re-run `tailscale cert $TS_HOSTNAME` to renew.

### Step 3 — Create the Caddyfile

```bash
cat > Caddyfile << EOF
${TS_HOSTNAME}:3001 {
    tls ${TS_HOSTNAME}.crt ${TS_HOSTNAME}.key
    reverse_proxy 127.0.0.1:3000
}

${TS_HOSTNAME}:8443 {
    tls ${TS_HOSTNAME}.crt ${TS_HOSTNAME}.key
    reverse_proxy 127.0.0.1:8082
}
EOF
```

**What this does:**
- `https://$TS_HOSTNAME:3001` → proxies to the remote server on localhost:3000
- `https://$TS_HOSTNAME:8443` → proxies to the relay server on localhost:8082

> We use separate ports (3001 for the app, 8443 for the relay) to avoid conflicts with other services on your Tailscale hostname.

### Step 4 — Create a GitHub OAuth app

Each developer needs their own GitHub OAuth app so they can sign in from their phone. The app only needs `read:user` and `user:email` scopes — no special permissions required.

1. Go to https://github.com/settings/applications/new
2. Fill in the form:
   - **Application name**: anything (e.g. `vibe-kanban-mobile-yourname`)
   - **Homepage URL**: run `echo "https://$TS_HOSTNAME:3001"` and paste the output
   - **Authorization callback URL**: run `echo "https://$TS_HOSTNAME:3001/v1/oauth/github/callback"` and paste the output
3. Click **Register application**
4. Copy the **Client ID** shown on the next page
5. Click **Generate a new client secret** and copy it immediately (it won't be shown again)
6. Add both values to `crates/remote/.env.remote`:
   ```bash
   # Replace with your own values
   GITHUB_OAUTH_CLIENT_ID=your_client_id
   GITHUB_OAUTH_CLIENT_SECRET=your_client_secret
   ```

> `.env.remote` is already in `.gitignore` — your credentials stay local. If the file already has these variables from the shared dev setup, replace them with your own.

## Running

There are two modes: **Docker mode** (simple, no hot reload) and **Dev mode** (Vite hot reload for frontend changes). Pick whichever fits your workflow.

---

### Option A — Docker Mode (Simple)

The frontend is built inside Docker. No hot reload — you need to restart Docker to see frontend changes. Good for testing backend changes or doing final QA on your phone.

**Two terminals:**

```bash
# Terminal 1 — Docker stack
VITE_RELAY_API_BASE_URL=https://$TS_HOSTNAME:8443 \
PUBLIC_BASE_URL=https://$TS_HOSTNAME:3001 \
pnpm remote:dev

# Terminal 2 — Caddy
caddy run --config Caddyfile
```

> The first time you run with these env vars, Docker rebuilds the frontend with the Tailscale URLs baked in. This takes a few minutes. Subsequent runs with the same URLs are cached.

---

### Option B — Dev Mode (Vite Hot Reload)

The frontend runs outside Docker via Vite, so you get instant hot reload when editing React components. Caddy routes API requests to Docker and everything else to Vite.

**Step 1 — Generate `Caddyfile.dev`:**

This file can't use shell variables directly, so generate it once (re-run if your hostname changes):

```bash
cat > Caddyfile.dev << EOF
${TS_HOSTNAME}:3001 {
    tls ${TS_HOSTNAME}.crt ${TS_HOSTNAME}.key
    handle /api/* {
        reverse_proxy 127.0.0.1:3000
    }
    handle /v1/* {
        reverse_proxy 127.0.0.1:3000
    }
    handle /shape/* {
        reverse_proxy 127.0.0.1:3000
    }
    handle {
        reverse_proxy localhost:3002 {
            header_up Host localhost:3002
        }
    }
}

${TS_HOSTNAME}:8443 {
    tls ${TS_HOSTNAME}.crt ${TS_HOSTNAME}.key
    reverse_proxy 127.0.0.1:8082
}
EOF
```

**What this routes:**
- `/api/*`, `/v1/*`, `/shape/*` → Docker remote server (`:3000`)
- Everything else → Vite dev server (`:3002`) with hot reload
- `:8443` → Relay server (`:8082`)

**Step 2 — Run four terminals:**

```bash
# Terminal 1 — Docker backends (no frontend build needed)
PUBLIC_BASE_URL=https://$TS_HOSTNAME:3001 \
pnpm remote:dev

# Terminal 2 — Vite dev server (hot reload)
VITE_RELAY_API_BASE_URL=https://$TS_HOSTNAME:8443 \
pnpm --filter @vibe/remote-web dev

# Terminal 3 — Caddy (dev config)
caddy run --config Caddyfile.dev

# Terminal 4 (optional) — Local desktop client
VK_SHARED_API_BASE=https://$TS_HOSTNAME:3001 \
VK_SHARED_RELAY_API_BASE=https://$TS_HOSTNAME:8443 \
pnpm run dev
```

> Vite binds to `localhost:3002`. The `Caddyfile.dev` uses `localhost` (not `127.0.0.1`) to match — this avoids IPv6/IPv4 mismatch issues on macOS.

---

### Accessing from your phone

1. Open the Tailscale app and make sure it's connected (toggle ON)
2. Open Safari (or Chrome) and go to: `https://<your-hostname>:3001` (run `echo "https://$TS_HOSTNAME:3001"` if you forgot it)
3. Sign in with GitHub
4. You're in

To go back to regular localhost development, just run `pnpm remote:dev` without env vars — no cleanup needed.

---

## Quick Reference

**Docker mode (2 terminals):**
```bash
# Terminal 1
VITE_RELAY_API_BASE_URL=https://$TS_HOSTNAME:8443 \
PUBLIC_BASE_URL=https://$TS_HOSTNAME:3001 \
pnpm remote:dev

# Terminal 2
caddy run --config Caddyfile

# On phone
echo "https://$TS_HOSTNAME:3001"
```

**Dev mode (4 terminals):**
```bash
# Terminal 1 — Docker backends
PUBLIC_BASE_URL=https://$TS_HOSTNAME:3001 \
pnpm remote:dev

# Terminal 2 — Vite
VITE_RELAY_API_BASE_URL=https://$TS_HOSTNAME:8443 \
pnpm --filter @vibe/remote-web dev

# Terminal 3 — Caddy
caddy run --config Caddyfile.dev

# Terminal 4 (optional) — Desktop client
VK_SHARED_API_BASE=https://$TS_HOSTNAME:3001 \
VK_SHARED_RELAY_API_BASE=https://$TS_HOSTNAME:8443 \
pnpm run dev

# On phone
echo "https://$TS_HOSTNAME:3001"
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `$TS_HOSTNAME` is empty | Re-run: `source ~/.zshrc` or restart your terminal |
| Phone can't reach the URL | Open Tailscale app on phone → make sure toggle is ON. Run `tailscale status` on Mac to verify both devices are connected |
| Phone shows certificate warning | Re-run `tailscale cert $TS_HOSTNAME` — certs may have expired (90-day lifetime) |
| `tailscale cert` fails with "does not support getting TLS certs" | Enable HTTPS certificates in Tailscale admin: https://login.tailscale.com/admin/dns → scroll to "HTTPS Certificates" at the bottom → click "Enable HTTPS" |
| `tailscale cert` fails with "invalid domain" | Make sure `$TS_HOSTNAME` includes the tailnet name (e.g. `johns-macbook.tail99xyz.ts.net`). Re-run Step 1 |
| OAuth redirect fails on phone | Run `echo "https://$TS_HOSTNAME:3001/v1/oauth/github/callback"` and verify it matches what's in GitHub settings |
| First build is very slow | Normal — Docker rebuilds the frontend with the new `VITE_RELAY_API_BASE_URL`. Subsequent builds are cached |
| Relay features (terminal, logs) don't work on phone | Check that `VITE_RELAY_API_BASE_URL` in the command matches your Caddy relay block (`https://$TS_HOSTNAME:8443`) |
| Caddy asks for password | Normal on first run — it installs a local CA certificate. Enter your macOS password |
| `caddy run` fails with "address already in use" | Another Caddy instance is running. Kill it: `pkill caddy`, then retry |
| `ping $TS_HOSTNAME` doesn't resolve | Enable MagicDNS in Tailscale admin: https://login.tailscale.com/admin/dns |
| Dev mode: Vite page loads but API calls fail | Make sure Docker is running (`pnpm remote:dev`) and you're using `Caddyfile.dev` (not `Caddyfile`) |
| Dev mode: hot reload doesn't work on phone | Vite HMR uses WebSocket — verify Caddy is proxying to `localhost:3002` (not `127.0.0.1:3002`). Regenerate `Caddyfile.dev` if needed |
| Dev mode: blank page or 502 on phone | Vite dev server may not be running. Check Terminal 2 is up with `pnpm --filter @vibe/remote-web dev` |

```

### File: pnpm-workspace.yaml
```yaml
packages:
  - packages/*

onlyBuiltDependencies:
  - '@sentry/cli'
  - core-js
  - esbuild

patchedDependencies:
  '@pierre/diffs@1.1.4': patches/@pierre__diffs@1.1.4.patch

```

### File: docs\AGENTS.md
```md
# Mintlify technical writing rule

You are an AI writing assistant specialised in creating exceptional technical documentation using Mintlify components and following industry-leading technical writing practices.

## Working relationship
- You can push back on ideas-this can lead to better documentation. Cite sources and explain your reasoning when you do so
- ALWAYS ask for clarification rather than making assumptions
- NEVER lie, guess, or make up information

## Project context
- Format: MDX files with YAML frontmatter
- Config: docs.json for navigation, theme, settings
- Components: Mintlify components

## Core writing principles

### Language and style requirements

- Use clear, direct language appropriate for technical audiences
- Write in second person ("you") for instructions and procedures
- Use active voice over passive voice
- Employ present tense for current states, future tense for outcomes
- Avoid jargon unless necessary and define terms when first used
- Maintain consistent terminology throughout all documentation
- Keep sentences concise whilst providing necessary context
- Use parallel structure in lists, headings, and procedures
- Use British English spelling and grammar

### Content organisation standards

- Lead with the most important information (inverted pyramid structure)
- Use progressive disclosure: basic concepts before advanced ones
- Break complex procedures into numbered steps
- Include prerequisites and context before instructions
- Provide expected outcomes for each major step
- Use descriptive, keyword-rich headings for navigation and SEO
- Group related information logically with clear section breaks
- Make content evergreen when possible
- Search for existing information before adding new content. Avoid duplication unless it is done for a strategic reason
- Check existing patterns for consistency

### User-centred approach

- Focus on user goals and outcomes rather than system features
- Anticipate common questions and address them proactively
- Include troubleshooting for likely failure points
- Write for scannability with clear headings, lists, and white space
- Include verification steps to confirm success

### Frontmatter requirements for pages
- title: Clear, descriptive page title
- description: Concise summary for SEO/navigation

### Do not
- Skip frontmatter on any MDX file
- Use absolute URLs for internal links
- Include untested code examples
- Make assumptions - always ask for clarification

## Mintlify component reference

### docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation

### Callout components

#### Note - Additional helpful information

<Note>
Supplementary information that supports the main content without interrupting flow
</Note>

#### Tip - Best practices and pro tips

<Tip>
Expert advice, shortcuts, or best practices that enhance user success
</Tip>

#### Warning - Important cautions

<Warning>
Critical information about potential issues, breaking changes, or destructive actions
</Warning>

#### Info - Neutral contextual information

<Info>
Background information, context, or neutral announcements
</Info>

#### Check - Success confirmations

<Check>
Positive confirmations, successful completions, or achievement indicators
</Check>

### Code components

#### Single code block

Example of a single code block:

```javascript config.js
const apiConfig = {
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: {
    'Authorisation': `Bearer ${process.env.API_TOKEN}`
  }
};
```

#### Code group with multiple languages

Example of a code group:

<CodeGroup>
```javascript Node.js
const response = await fetch('/api/endpoint', {
  headers: { Authorisation: `Bearer ${apiKey}` }
});
```

```python Python
import requests
response = requests.get('/api/endpoint',
  headers={'Authorisation': f'Bearer {api_key}'})
```

```curl cURL
curl -X GET '/api/endpoint' \
  -H 'Authorisation: Bearer YOUR_API_KEY'
```
</CodeGroup>

#### Request/response examples

Example of request/response documentation:

<RequestExample>
```bash cURL
curl -X POST 'https://api.example.com/users' \
  -H 'Content-Type: application/json' \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```
</RequestExample>

<ResponseExample>
```json Success
{
  "id": "user_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```
</ResponseExample>

### Structural components

#### Steps for procedures

Example of step-by-step instructions:

<Steps>
<Step title="Install dependencies">
  Run `npm install` to install required packages.

  <Check>
  Verify installation by running `npm list`.
  </Check>
</Step>

<Step title="Configure environment">
  Create a `.env` file with your API credentials.

  ```bash
  API_KEY=your_api_key_here
  ```

  <Warning>
  Never commit API keys to version control.
  </Warning>
</Step>
</Steps>

#### Tabs for alternative content

Example of tabbed content:

<Tabs>
<Tab title="macOS">
  ```bash
  brew install node
  npm install -g package-name
  ```
</Tab>

<Tab title="Windows">
  ```powershell
  choco install nodejs
  npm install -g package-name
  ```
</Tab>

<Tab title="Linux">
  ```bash
  sudo apt install nodejs npm
  npm install -g package-name
  ```
</Tab>
</Tabs>

#### Accordions for collapsible content

Example of accordion groups:

<AccordionGroup>
<Accordion title="Troubleshooting connection issues">
  - **Firewall blocking**: Ensure ports 80 and 443 are open
  - **Proxy configuration**: Set HTTP_PROXY environment variable
  - **DNS resolution**: Try using 8.8.8.8 as DNS server
</Accordion>

<Accordion title="Advanced configuration">
  ```javascript
  const config = {
    performance: { cache: true, timeout: 30000 },
    security: { encryption: 'AES-256' }
  };
  ```
</Accordion>
</AccordionGroup>

### Cards and columns for emphasising information

Example of cards and card groups:

<Card title="Getting started guide" icon="rocket" href="/quickstart">
Complete walkthrough from installation to your first API call in under 10 minutes.
</Card>

<CardGroup cols={2}>
<Card title="Authentication" icon="key" href="/auth">
  Learn how to authenticate requests using API keys or JWT tokens.
</Card>

<Card title="Rate limiting" icon="clock" href="/rate-limits">
  Understand rate limits and best practices for high-volume usage.
</Card>
</CardGroup>

### API documentation components

#### Parameter fields

Example of parameter documentation:

<ParamField path="user_id" type="string" required>
Unique identifier for the user. Must be a valid UUID v4 format.
</ParamField>

<ParamField body="email" type="string" required>
User's email address. Must be valid and unique within the system.
</ParamField>

<ParamField query="limit" type="integer" default="10">
Maximum number of results to return. Range: 1-100.
</ParamField>

<ParamField header="Authorisation" type="string" required>
Bearer token for API authentication. Format: `Bearer YOUR_API_KEY`
</ParamField>

#### Response fields

Example of response field documentation:

<ResponseField name="user_id" type="string" required>
Unique identifier assigned to the newly created user.
</ResponseField>

<ResponseField name="created_at" type="timestamp">
ISO 8601 formatted timestamp of when the user was created.
</ResponseField>

<ResponseField name="permissions" type="array">
List of permission strings assigned to this user.
</ResponseField>

#### Expandable nested fields

Example of nested field documentation:

<ResponseField name="user" type="object">
Complete user object with all associated data.

<Expandable title="User properties">
  <ResponseField name="profile" type="object">
  User profile information including personal details.

  <Expandable title="Profile details">
    <ResponseField name="first_name" type="string">
    User's first name as entered during registration.
    </ResponseField>

    <ResponseField name="avatar_url" type="string | null">
    URL to user's profile picture. Returns null if no avatar is set.
    </ResponseField>
  </Expandable>
  </ResponseField>
</Expandable>
</ResponseField>

### Media and advanced components

#### Frames for images

Wrap all images in frames:

<Frame>
<img src="/images/dashboard.png" alt="Main dashboard showing analytics overview" />
</Frame>

<Frame caption="The analytics dashboard provides real-time insights">
<img src="/images/analytics.png" alt="Analytics dashboard with charts" />
</Frame>

#### Videos

Use the HTML video element for self-hosted video content:

<video
  controls
  className="w-full aspect-video rounded-xl"
  src="link-to-your-video.com"
></video>

Embed YouTube videos using iframe elements:

<iframe
  className="w-full aspect-video rounded-xl"
  src="https://www.youtube.com/embed/4KzFe50RQkQ"
  title="YouTube video player"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

#### Tooltips

Example of tooltip usage:

<Tooltip tip="Application Programming Interface - protocols for building software">
API
</Tooltip>

#### Updates

Use updates for changelogs:

<Update label="Version 2.1.0" description="Released March 15, 2024">
## New features
- Added bulk user import functionality
- Improved error messages with actionable suggestions

## Bug fixes
- Fixed pagination issue with large datasets
- Resolved authentication timeout problems
</Update>

## Required page structure

Every documentation page must begin with YAML frontmatter:

```yaml
---
title: "Clear, specific, keyword-rich title"
description: "Concise description explaining page purpose and value"
---
```

## Content quality standards

### Code examples requirements

- Always include complete, runnable examples that users can copy and execute
- Show proper error handling and edge case management
- Use realistic data instead of placeholder values
- Include expected outputs and results for verification
- Test all code examples thoroughly before publishing
- Specify language and include filename when relevant
- Add explanatory comments for complex logic
- Never include real API keys or secrets in code examples


### Accessibility requirements

- Include descriptive alt text for all images and diagrams
- Use specific, actionable link text instead of "click here"
- Ensure proper heading hierarchy starting with H2
- Provide keyboard navigation considerations
- Use sufficient colour contrast in examples and visuals
- Structure content for easy scanning with headers and lists

## Component selection logic

- Use **Steps** for procedures and sequential instructions
- Use **Tabs** for platform-specific content or alternative approaches
- Use **CodeGroup** when showing the same concept in multiple programming languages
- Use **Accordions** for progressive disclosure of information
- Use **RequestExample/ResponseExample** specifically for API endpoint documentation
- Use **ParamField** for API parameters, **ResponseField** for API responses
- Use **Expandable** for nested object properties or hierarchical information

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
