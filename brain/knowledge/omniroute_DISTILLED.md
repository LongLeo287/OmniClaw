---
id: OmniRoute
type: knowledge
owner: OA_Triage
---
# OmniRoute
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "omniroute",
  "version": "3.5.2",
  "description": "Smart AI Router with auto fallback — route to FREE & cheap models, zero downtime. Works with Cursor, Cline, Claude Desktop, Codex, and any OpenAI-compatible tool.",
  "type": "module",
  "bin": {
    "omniroute": "bin/omniroute.mjs",
    "omniroute-reset-password": "bin/reset-password.mjs"
  },
  "files": [
    "bin/",
    "app/",
    "open-sse/mcp-server/",
    "src/shared/contracts/",
    "scripts/postinstall.mjs",
    "scripts/native-binary-compat.mjs",
    "README.md",
    "LICENSE"
  ],
  "workspaces": [
    "open-sse"
  ],
  "engines": {
    "node": ">=18.0.0 <24.0.0"
  },
  "keywords": [
    "ai",
    "router",
    "proxy",
    "openai",
    "claude",
    "anthropic",
    "gemini",
    "fallback",
    "cursor",
    "cline",
    "codex",
    "llm",
    "auto-fallback"
  ],
  "license": "MIT",
  "author": "diegosouzapw",
  "repository": {
    "type": "git",
    "url": "https://github.com/diegosouzapw/OmniRoute"
  },
  "homepage": "https://omniroute.online",
  "scripts": {
    "dev": "node scripts/run-next.mjs dev",
    "build": "node scripts/build-next-isolated.mjs",
    "build:cli": "node scripts/prepublish.mjs",
    "start": "node scripts/run-next.mjs start",
    "lint": "eslint .",
    "electron:dev": "concurrently \"npm run dev\" \"wait-on http://localhost:20128 && cd electron && npm run dev\"",
    "electron:build": "npm run build && cd electron && npm run build",
    "electron:build:win": "npm run build && cd electron && npm run build:win",
    "electron:build:mac": "npm run build && cd electron && npm run build:mac",
    "electron:build:linux": "npm run build && cd electron && npm run build:linux",
    "test": "cross-env DISABLE_SQLITE_AUTO_BACKUP=true node --import tsx/esm --test tests/unit/*.test.mjs",
    "test:unit": "cross-env DISABLE_SQLITE_AUTO_BACKUP=true node --import tsx/esm --test tests/unit/*.test.mjs",
    "test:plan3": "cross-env DISABLE_SQLITE_AUTO_BACKUP=true node --import tsx/esm --test tests/unit/plan3-p0.test.mjs",
    "test:fixes": "cross-env DISABLE_SQLITE_AUTO_BACKUP=true node --import tsx/esm --test tests/unit/fixes-p1.test.mjs",
    "test:security": "cross-env DISABLE_SQLITE_AUTO_BACKUP=true node --import tsx/esm --test tests/unit/security-fase01.test.mjs",
    "check:cycles": "node scripts/check-cycles.mjs",
    "check:route-validation:t06": "node scripts/check-route-validation.mjs",
    "check:any-budget:t11": "node scripts/check-t11-any-budget.mjs",
    "check:docs-sync": "node scripts/check-docs-sync.mjs",
    "typecheck:core": "tsc --pretty false -p tsconfig.typecheck-core.json",
    "typecheck:noimplicit:core": "tsc --pretty false -p tsconfig.typecheck-noimplicit-core.json",
    "test:integration": "node --import tsx/esm --test tests/integration/*.test.mjs",
    "test:e2e": "node scripts/run-playwright-tests.mjs test tests/e2e/*.spec.ts",
    "test:protocols:e2e": "node scripts/run-protocol-clients-tests.mjs",
    "test:vitest": "vitest run --config vitest.mcp.config.ts",
    "test:ecosystem": "node scripts/run-ecosystem-tests.mjs",
    "test:coverage": "c8 --exclude=tests/** --exclude=**/*.test.* --reporter=text-summary --reporter=html --reporter=json-summary --reporter=lcov --check-coverage --statements 55 --lines 55 --functions 55 --branches 60 node --import tsx/esm --test tests/unit/*.test.mjs",
    "test:coverage:legacy": "c8 --exclude=open-sse --check-coverage --lines 50 --functions 50 --branches 50 node --import tsx/esm --test tests/unit/*.test.mjs",
    "coverage:report": "c8 report --exclude=tests/** --exclude=**/*.test.* --reporter=text --reporter=text-summary --reporter=html --reporter=json-summary --reporter=lcov",
    "coverage:report:legacy": "c8 report --exclude=open-sse --reporter=text --reporter=text-summary",
    "test:all": "npm run test:unit && npm run test:vitest && npm run test:ecosystem && npm run test:e2e",
    "check": "npm run lint && npm run test",
    "prepublishOnly": "npm run build:cli",
    "postinstall": "node scripts/postinstall.mjs",
    "prepare": "husky",
    "system-info": "node scripts/system-info.mjs"
  },
  "dependencies": {
    "@lobehub/icons": "^5.0.1",
    "@modelcontextprotocol/sdk": "^1.27.1",
    "@monaco-editor/react": "^4.7.0",
    "@swc/helpers": "0.5.19",
    "bcryptjs": "^3.0.3",
    "better-sqlite3": "^12.6.2",
    "bottleneck": "^2.19.5",
    "dompurify": "^3.3.2",
    "express": "^5.2.1",
    "fetch-socks": "^1.3.2",
    "http-proxy-middleware": "^3.0.5",
    "https-proxy-agent": "^8.0.0",
    "jose": "^6.1.3",
    "js-yaml": "^4.1.0",
    "lowdb": "^7.0.1",
    "monaco-editor": "^0.55.1",
    "next": "16.0.10",
    "next-intl": "^4.8.3",
    "node-machine-id": "^1.1.12",
    "open": "^11.0.0",
    "ora": "^9.1.0",
    "pino": "^10.3.1",
    "pino-pretty": "^13.1.3",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "recharts": "^3.7.0",
    "selfsigned": "^5.5.0",
    "tsx": "^4.21.0",
    "undici": "^7.19.2",
    "uuid": "^13.0.0",
    "wreq-js": "^2.0.1",
    "yazl": "^3.3.1",
    "zod": "^4.3.6",
    "zustand": "^5.0.10"
  },
  "optionalDependencies": {
    "keytar": "^7.9.0"
  },
  "devDependencies": {
    "@playwright/test": "^1.58.2",
    "@tailwindcss/postcss": "^4.1.18",
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.2",
    "@types/bcryptjs": "^3.0.0",
    "@types/better-sqlite3": "^7.6.13",
    "@types/keytar": "^4.4.0",
    "@types/node": "^25.2.3",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^6.0.1",
    "c8": "^11.0.0",
    "concurrently": "^9.2.1",
    "cross-env": "^10.1.0",
    "eslint": "^9.39.2",
    "eslint-config-next": "16.0.10",
    "husky": "^9.1.7",
    "jsdom": "^29.0.1",
    "lint-staged": "^16.2.7",
    "prettier": "^3.8.1",
    "prop-types": "^15.8.1",
    "tailwindcss": "^4",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.56.0",
    "vitest": "^4.1.2",
    "wait-on": "^9.0.4"
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx,mjs}": [
      "prettier --write",
      "eslint --fix --no-error-on-unmatched-pattern"
    ],
    "*.{json,md,yml,yaml,css}": [
      "prettier --write"
    ]
  },
  "pnpm": {
    "onlyBuiltDependencies": [
      "@parcel/watcher",
      "@swc/core",
      "better-sqlite3",
      "esbuild",
      "omniroute",
      "sharp"
    ]
  },
  "overrides": {
    "lodash-es": "^4.18.1",
    "dompurify": "^3.3.2",
    "path-to-regexp": "^8.4.0",
    "react": "$react",
    "react-dom": "$react-dom"
  }
}

```

### File: README.md
```md
# 🚀 OmniRoute — The Free AI Gateway

### Never stop coding. Smart routing to **FREE & low-cost AI models** with automatic fallback.

_Your universal API proxy — one endpoint, 60+ providers, zero downtime. Now with **MCP Server (25 tools)**, **A2A Protocol**, **Memory/Skills Systems** & **Electron Desktop App**._

**Chat Completions • Embeddings • Image Generation • Video • Music • Audio • Reranking • **Web Search** • MCP Server • A2A Protocol • 100% TypeScript**

---

<div align="center">

[![npm version](https://img.shields.io/npm/v/omniroute?color=cb3837&logo=npm)](https://www.npmjs.com/package/omniroute)
[![Docker Hub](https://img.shields.io/docker/v/diegosouzapw/omniroute?label=Docker%20Hub&logo=docker&color=2496ED)](https://hub.docker.com/r/diegosouzapw/omniroute)

![NPM Downloads](https://img.shields.io/npm/dw/omniroute?label=npm%20down%20week&color=red)
![NPM Downloads](https://img.shields.io/npm/dm/omniroute?label=npm%20down%20month&color=red)

![NPM Downloads](https://img.shields.io/npm/d18m/omniroute?label=npm%20down%20year&color=red)
![Docker Pulls](https://img.shields.io/docker/pulls/diegosouzapw/omniroute)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/diegosouzapw/omniroute/total?style=flat&label=eletron%20donwloads&color=blue)

[![stars](https://custom-icon-badges.demolab.com/github/stars/diegosouzapw/OmniRoute?logo=star&style=flat)](https://github.com/diegosouzapw/OmniRoute/stargazers)
[![open issues](https://custom-icon-badges.demolab.com/github/issues-raw/diegosouzapw/OmniRoute?logo=issue)](https://github.com/diegosouzapw/OmniRoute/issues)
[![license](https://custom-icon-badges.demolab.com/github/license/diegosouzapw/OmniRoute?logo=law)](https://github.com/diegosouzapw/OmniRoute/blob/main/LICENSE)
[![last commit](https://custom-icon-badges.demolab.com/github/last-commit/diegosouzapw/OmniRoute?logo=history&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/commits/main)
[![total contributions](https://custom-icon-badges.demolab.com/badge/dynamic/json?logo=graph&logoColor=fff&color=blue&label=total%20contributions&query=%24.totalContributions&url=https%3A%2F%2Fstreak-stats.demolab.com%2F%3Fuser%3Ddiegosouzapw%26type%3Djson)](https://github.com/diegosouzapw)
[![code size](https://custom-icon-badges.demolab.com/github/languages/code-size/diegosouzapw/OmniRoute?logo=file-code&logoColor=white)](https://github.com/diegosouzapw/OmniRoute)
[![pr closed](https://custom-icon-badges.demolab.com/github/issues-pr-closed/diegosouzapw/OmniRoute?color=purple&logo=git-pull-request&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/pulls?q=is%3Apr+is%3Aclosed)
[![tag](https://custom-icon-badges.demolab.com/github/v/tag/diegosouzapw/OmniRoute?logo=tag&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/tags)
[![github streak](https://custom-icon-badges.demolab.com/badge/dynamic/json?logo=fire&logoColor=fff&color=orange&label=github%20streak&query=%24.currentStreak.length&suffix=%20days&url=https%3A%2F%2Fstreak-stats.demolab.com%2F%3Fuser%3Ddiegosouzapw%26type%3Djson)](https://github.com/diegosouzapw)
[![followers](https://custom-icon-badges.demolab.com/github/followers/diegosouzapw?logo=person-add)](https://github.com/diegosouzapw?tab=followers)
[![fork](https://custom-icon-badges.demolab.com/github/forks/diegosouzapw/OmniRoute?logo=fork)](https://github.com/diegosouzapw/OmniRoute/network/members)
[![watch](https://custom-icon-badges.demolab.com/github/watchers/diegosouzapw/OmniRoute?logo=eye)](https://github.com/diegosouzapw/OmniRoute/watchers)

[![License](https://img.shields.io/github/license/diegosouzapw/OmniRoute)](https://github.com/diegosouzapw/OmniRoute/blob/main/LICENSE)
[![Website](https://img.shields.io/badge/Website-omniroute.online-blue?logo=google-chrome&logoColor=white)](https://omniroute.online)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Community-25D366?logo=whatsapp&logoColor=white)](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)

[🌐 Website](https://omniroute.online) • [🚀 Quick Start](#-quick-start) • [💡 Features](#-key-features) • [📖 Docs](#-documentation) • [💰 Pricing](#-pricing-at-a-glance) • [💬 WhatsApp](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)

</div>

🌐 **Available in:** 🇺🇸 [English](README.md) | 🇧🇷 [Português (Brasil)](docs/i18n/pt-BR/README.md) | 🇪🇸 [Español](docs/i18n/es/README.md) | 🇫🇷 [Français](docs/i18n/fr/README.md) | 🇮🇹 [Italiano](docs/i18n/it/README.md) | 🇷🇺 [Русский](docs/i18n/ru/README.md) | 🇨🇳 [中文 (简体)](docs/i18n/zh-CN/README.md) | 🇩🇪 [Deutsch](docs/i18n/de/README.md) | 🇮🇳 [हिन्दी](docs/i18n/in/README.md) | 🇹🇭 [ไทย](docs/i18n/th/README.md) | 🇺🇦 [Українська](docs/i18n/uk-UA/README.md) | 🇸🇦 [العربية](docs/i18n/ar/README.md) | 🇯🇵 [日本語](docs/i18n/ja/README.md) | 🇻🇳 [Tiếng Việt](docs/i18n/vi/README.md) | 🇧🇬 [Български](docs/i18n/bg/README.md) | 🇩🇰 [Dansk](docs/i18n/da/README.md) | 🇫🇮 [Suomi](docs/i18n/fi/README.md) | 🇮🇱 [עברית](docs/i18n/he/README.md) | 🇭🇺 [Magyar](docs/i18n/hu/README.md) | 🇮🇩 [Bahasa Indonesia](docs/i18n/id/README.md) | 🇰🇷 [한국어](docs/i18n/ko/README.md) | 🇲🇾 [Bahasa Melayu](docs/i18n/ms/README.md) | 🇳🇱 [Nederlands](docs/i18n/nl/README.md) | 🇳🇴 [Norsk](docs/i18n/no/README.md) | 🇵🇹 [Português (Portugal)](docs/i18n/pt/README.md) | 🇷🇴 [Română](docs/i18n/ro/README.md) | 🇵🇱 [Polski](docs/i18n/pl/README.md) | 🇸🇰 [Slovenčina](docs/i18n/sk/README.md) | 🇸🇪 [Svenska](docs/i18n/sv/README.md) | 🇵🇭 [Filipino](docs/i18n/phi/README.md) | 🇨🇿 [Čeština](docs/i18n/cs/README.md)

---

## 🖼️ Main Dashboard

<div align="center">
  <img src="./docs/screenshots/MainOmniRoute.png" alt="OmniRoute Dashboard" width="800"/>
</div>

---

## 📸 Dashboard Preview

<details>
<summary><b>Click to see dashboard screenshots</b></summary>

| Page           | Screenshot                                        |
| -------------- | ------------------------------------------------- |
| **Providers**  | ![Providers](docs/screenshots/01-providers.png)   |
| **Combos**     | ![Combos](docs/screenshots/02-combos.png)         |
| **Analytics**  | ![Analytics](docs/screenshots/03-analytics.png)   |
| **Health**     | ![Health](docs/screenshots/04-health.png)         |
| **Translator** | ![Translator](docs/screenshots/05-translator.png) |
| **Settings**   | ![Settings](docs/screenshots/06-settings.png)     |
| **CLI Tools**  | ![CLI Tools](docs/screenshots/07-cli-tools.png)   |
| **Usage Logs** | ![Usage](docs/screenshots/08-usage.png)           |
| **Endpoints**  | ![Endpoints](docs/screenshots/09-endpoint.png)    |

</details>

---

### 🤖 Free AI Provider for your favorite coding agents

_Connect any AI-powered IDE or CLI tool through OmniRoute — free API gateway for unlimited coding._

  <table>
    <tr>
      <td align="center" width="110">
        <a href="https://github.com/openclaw/openclaw">
          <img src="./public/providers/openclaw.png" alt="OpenClaw" width="48"/><br/>
          <b>OpenClaw</b>
        </a><br/>
        <sub>⭐ 205K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/HKUDS/nanobot">
          <img src="./public/providers/nanobot.png" alt="NanoBot" width="48"/><br/>
          <b>NanoBot</b>
        </a><br/>
        <sub>⭐ 20.9K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/sipeed/picoclaw">
          <img src="./public/providers/picoclaw.jpg" alt="PicoClaw" width="48"/><br/>
          <b>PicoClaw</b>
        </a><br/>
        <sub>⭐ 14.6K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/zeroclaw-labs/zeroclaw">
          <img src="./public/providers/zeroclaw.png" alt="ZeroClaw" width="48"/><br/>
          <b>ZeroClaw</b>
        </a><br/>
        <sub>⭐ 9.9K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/nearai/ironclaw">
          <img src="./public/providers/ironclaw.png" alt="IronClaw" width="48"/><br/>
          <b>IronClaw</b>
        </a><br/>
        <sub>⭐ 2.1K</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="110">
        <a href="https://github.com/anomalyco/opencode">
          <img src="./public/providers/opencode.svg" alt="OpenCode" width="48"/><br/>
          <b>OpenCode</b>
        </a><br/>
        <sub>⭐ 106K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/openai/codex">
          <img src="./public/providers/codex.png" alt="Codex CLI" width="48"/><br/>
          <b>Codex CLI</b>
        </a><br/>
        <sub>⭐ 60.8K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/anthropics/claude-code">
          <img src="./public/providers/claude.png" alt="Claude Code" width="48"/><br/>
          <b>Claude Code</b>
        </a><br/>
        <sub>⭐ 67.3K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/google-gemini/gemini-cli">
          <img src="./public/providers/gemini-cli.png" alt="Gemini CLI" width="48"/><br/>
          <b>Gemini CLI</b>
        </a><br/>
        <sub>⭐ 94.7K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/Kilo-Org/kilocode">
          <img src="./public/providers/kilocode.png" alt="Kilo Code" width="48"/><br/>
          <b>Kilo Code</b>
        </a><br/>
        <sub>⭐ 15.5K</sub>
      </td>
    </tr>
  </table>

<sub>📡 All agents connect via <code>http://localhost:20128/v1</code> or <code>http://cloud.omniroute.online/v1</code> — one config, unlimited models and quota</sub>

---

## 🤔 Why OmniRoute?

**Stop wasting money and hitting limits:**

- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Subscription quota expires unused every month
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Rate limits stop you mid-coding
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Expensive APIs ($20-50/month per provider)
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Manual switching between providers

**OmniRoute solves this:**

- ✅ **Maximize subscriptions** - Track quota, use every bit before reset
- ✅ **Auto fallback** - Subscription → API Key → Cheap → Free, zero downtime
- ✅ **Multi-account** - Round-robin between accounts per provider
- ✅ **Universal** - Works with Claude Code, Codex, Gemini CLI, Cursor, Cline, OpenClaw, any CLI tool

---

## 📧 Support

> 💬 **Join our community!** [WhatsApp Group](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t) — Get help, share tips, and stay updated.

- **Website**: [omniroute.online](https://omniroute.online)
- **GitHub**: [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- **Issues**: [github.com/diegosouzapw/OmniRoute/issues](https://github.com/diegosouzapw/OmniRoute/issues)
- **WhatsApp**: [Community Group](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md), open a PR, or pick a `good first issue`
- **Original Project**: [9router by decolua](https://github.com/decolua/9router)

### 🐛 Reporting a Bug?

When opening an issue, please run the system-info command and attach the generated file:

```bash
npm run system-info
```

This generates a `system-info.txt` with your Node.js version, OmniRoute version, OS details, installed CLI tools (qoder, gemini, claude, codex, antigravity, droid, etc.), Docker/PM2 status, and system packages — everything we need to reproduce your issue quickly. Attach the file directly to your GitHub issue.

---

## 🔄 How It Works

```
┌─────────────┐
│  Your CLI   │  (Claude Code, Codex, Gemini CLI, OpenClaw, Cursor, Cline...)
│   Tool      │
└──────┬──────┘
       │ http://localhost:20128/v1
       ↓
┌─────────────────────────────────────────┐
│           OmniRoute (Smart Router)        │
│  • Format translation (OpenAI ↔ Claude) │
│  • Quota tracking + Embeddings + Images │
│  • Auto token refresh                   │
└──────┬──────────────────────────────────┘
       │
       ├─→ [Tier 1: SUBSCRIPTION] Claude Code, Codex, Gemini CLI
       │   ↓ quota exhausted
       ├─→ [Tier 2: API KEY] DeepSeek, Groq, xAI, Mistral, NVIDIA NIM, etc.
       │   ↓ budget limit
       ├─→ [Tier 3: CHEAP] GLM ($0.6/1M), MiniMax ($0.2/1M)
       │   ↓ budget limit
       └─→ [Tier 4: FREE] Qoder, Qwen, Kiro (unlimited)

Result: Never stop coding, minimal cost
```

---

## 🎯 What OmniRoute Solves — 30 Real Pain Points & Use Cases

> **Every developer using AI tools faces these problems daily.** OmniRoute was built to solve them all — from cost overruns to regional blocks, from broken OAuth flows to protocol operations and enterprise observability.

<details>
<summary><b>💸 1. "I pay for an expensive subscription but still get interrupted by limits"</b></summary>

Developers pay $20–200/month for Claude Pro, Codex Pro, or GitHub Copilot. Even paying, quota has a ceiling — 5h of usage, weekly limits, or per-minute rate limits. Mid-coding session, the provider stops responding and the developer loses flow and productivity.

**How OmniRoute solves it:**

- **Smart 4-Tier Fallback** — If subscription quota runs out, automatically redirects to API Key → Cheap → Free with zero manual intervention
- **Provider Limits Tracking** — Cached quota snapshots refresh on a server-side schedule (default `PROVIDER_LIMITS_SYNC_INTERVAL_MINUTES=70`) with manual refresh available in the UI
- **Multi-Account Support** — Multiple accounts per provider with auto round-robin — when one runs out, switches to the next
- **Custom Combos** — Customizable fallback chains with 9 balancing strategies (priority, weighted, fill-first, round-robin, P2C, random, least-used, cost-optimized, strict-random)
- **Codex Business Quotas** — Business/Team workspace quota monitoring directly in the dashboard

</details>

<details>
<summary><b>🔌 2. "I need to use multiple providers but each has a different API"</b></summary>

OpenAI uses one format, Claude (Anthropic) uses another, Gemini yet another. If a dev wants to test models from different providers or fallback between them, they need to reconfigure SDKs, change endpoints, deal with incompatible formats. Custom providers (FriendLI, NIM) have non-standard model endpoints.

**How OmniRoute solves it:**

- **Unified Endpoint** — A single `http://localhost:20128/v1` serves as proxy for all 60+ providers
- **Format Translation** — Automatic and transparent: OpenAI ↔ Claude ↔ Gemini ↔ Responses API
- **Response Sanitization** — Strips non-standard fields (`x_groq`, `usage_breakdown`, `service_tier`) that break OpenAI SDK v1.83+
- **Role Normalization** — Converts `developer` → `system` for non-OpenAI providers; `system` → `user` for GLM/ERNIE
- **Think Tag Extraction** — Extracts `<think>` blocks from models like DeepSeek R1 into standardized `reasoning_content`
- **Structured Output for Gemini** — `json_sc
... [TRUNCATED]
```

### File: docs\i18n\README.md
```md
# 🌐 Multilingual Documentation — 9router

Translations of documentation into 32 languages. Code blocks remain in English.

---

- 🇪🇸 **Español** (`es`): [Docs Root](./es/README.md)
- 🇫🇷 **Français** (`fr`): [Docs Root](./fr/README.md)
- 🇩🇪 **Deutsch** (`de`): [Docs Root](./de/README.md)
- 🇮🇹 **Italiano** (`it`): [Docs Root](./it/README.md)
- 🇷🇺 **Русский** (`ru`): [Docs Root](./ru/README.md)
- 🇨🇳 **中文（简体）** (`zh-CN`): [Docs Root](./zh-CN/README.md)
- 🇯🇵 **日本語** (`ja`): [Docs Root](./ja/README.md)
- 🇰🇷 **한국어** (`ko`): [Docs Root](./ko/README.md)
- 🇸🇦 **العربية** (`ar`): [Docs Root](./ar/README.md)
- 🇮🇳 **हिन्दी** (`hi`): [Docs Root](./hi/README.md)
- 🇮🇳 **हिन्दी (IN)** (`in`): [Docs Root](./in/README.md)
- 🇹🇭 **ไทย** (`th`): [Docs Root](./th/README.md)
- 🇻🇳 **Tiếng Việt** (`vi`): [Docs Root](./vi/README.md)
- 🇮🇩 **Bahasa Indonesia** (`id`): [Docs Root](./id/README.md)
- 🇲🇾 **Bahasa Melayu** (`ms`): [Docs Root](./ms/README.md)
- 🇳🇱 **Nederlands** (`nl`): [Docs Root](./nl/README.md)
- 🇵🇱 **Polski** (`pl`): [Docs Root](./pl/README.md)
- 🇸🇪 **Svenska** (`sv`): [Docs Root](./sv/README.md)
- 🇳🇴 **Norsk** (`no`): [Docs Root](./no/README.md)
- 🇩🇰 **Dansk** (`da`): [Docs Root](./da/README.md)
- 🇫🇮 **Suomi** (`fi`): [Docs Root](./fi/README.md)
- 🇵🇹 **Português (Portugal)** (`pt`): [Docs Root](./pt/README.md)
- 🇷🇴 **Română** (`ro`): [Docs Root](./ro/README.md)
- 🇭🇺 **Magyar** (`hu`): [Docs Root](./hu/README.md)
- 🇧🇬 **Български** (`bg`): [Docs Root](./bg/README.md)
- 🇸🇰 **Slovenčina** (`sk`): [Docs Root](./sk/README.md)
- 🇺🇦 **Українська** (`uk-UA`): [Docs Root](./uk-UA/README.md)
- 🇮🇱 **עברית** (`he`): [Docs Root](./he/README.md)
- 🇵🇭 **Filipino** (`phi`): [Docs Root](./phi/README.md)
- 🇧🇷 **Português (Brasil)** (`pt-BR`): [Docs Root](./pt-BR/README.md)
- 🇨🇿 **Čeština** (`cs`): [Docs Root](./cs/README.md)
- 🇹🇷 **Türkçe** (`tr`): [Docs Root](./tr/README.md)

```

### File: docs\i18n\ar\README.md
```md
# 🚀 OmniRoute — The Free AI Gateway (العربية)

🌐 **Languages:** 🇺🇸 [English](../../../README.md) · 🇪🇸 [es](../es/README.md) · 🇫🇷 [fr](../fr/README.md) · 🇩🇪 [de](../de/README.md) · 🇮🇹 [it](../it/README.md) · 🇷🇺 [ru](../ru/README.md) · 🇨🇳 [zh-CN](../zh-CN/README.md) · 🇯🇵 [ja](../ja/README.md) · 🇰🇷 [ko](../ko/README.md) · 🇸🇦 [ar](../ar/README.md) · 🇮🇳 [hi](../hi/README.md) · 🇮🇳 [in](../in/README.md) · 🇹🇭 [th](../th/README.md) · 🇻🇳 [vi](../vi/README.md) · 🇮🇩 [id](../id/README.md) · 🇲🇾 [ms](../ms/README.md) · 🇳🇱 [nl](../nl/README.md) · 🇵🇱 [pl](../pl/README.md) · 🇸🇪 [sv](../sv/README.md) · 🇳🇴 [no](../no/README.md) · 🇩🇰 [da](../da/README.md) · 🇫🇮 [fi](../fi/README.md) · 🇵🇹 [pt](../pt/README.md) · 🇷🇴 [ro](../ro/README.md) · 🇭🇺 [hu](../hu/README.md) · 🇧🇬 [bg](../bg/README.md) · 🇸🇰 [sk](../sk/README.md) · 🇺🇦 [uk-UA](../uk-UA/README.md) · 🇮🇱 [he](../he/README.md) · 🇵🇭 [phi](../phi/README.md) · 🇧🇷 [pt-BR](../pt-BR/README.md) · 🇨🇿 [cs](../cs/README.md) · 🇹🇷 [tr](../tr/README.md)

---

### Never stop coding. Smart routing to **FREE & low-cost AI models** with automatic fallback.

_Your universal API proxy — one endpoint, 60+ providers, zero downtime. Now with **MCP Server (25 tools)**, **A2A Protocol**, **Memory/Skills Systems** & **Electron Desktop App**._

**Chat Completions • Embeddings • Image Generation • Video • Music • Audio • Reranking • **Web Search** • MCP Server • A2A Protocol • 100% TypeScript**

---

<div align="center">

[![npm version](https://img.shields.io/npm/v/omniroute?color=cb3837&logo=npm)](https://www.npmjs.com/package/omniroute)
[![Docker Hub](https://img.shields.io/docker/v/diegosouzapw/omniroute?label=Docker%20Hub&logo=docker&color=2496ED)](https://hub.docker.com/r/diegosouzapw/omniroute)

![NPM Downloads](https://img.shields.io/npm/dw/omniroute?label=npm%20down%20week&color=red)
![NPM Downloads](https://img.shields.io/npm/dm/omniroute?label=npm%20down%20month&color=red)

![NPM Downloads](https://img.shields.io/npm/d18m/omniroute?label=npm%20down%20year&color=red)
![Docker Pulls](https://img.shields.io/docker/pulls/diegosouzapw/omniroute)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/diegosouzapw/omniroute/total?style=flat&label=eletron%20donwloads&color=blue)

[![stars](https://custom-icon-badges.demolab.com/github/stars/diegosouzapw/OmniRoute?logo=star&style=flat)](https://github.com/diegosouzapw/OmniRoute/stargazers)
[![open issues](https://custom-icon-badges.demolab.com/github/issues-raw/diegosouzapw/OmniRoute?logo=issue)](https://github.com/diegosouzapw/OmniRoute/issues)
[![license](https://custom-icon-badges.demolab.com/github/license/diegosouzapw/OmniRoute?logo=law)](https://github.com/diegosouzapw/OmniRoute/blob/main/LICENSE)
[![last commit](https://custom-icon-badges.demolab.com/github/last-commit/diegosouzapw/OmniRoute?logo=history&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/commits/main)
[![total contributions](https://custom-icon-badges.demolab.com/badge/dynamic/json?logo=graph&logoColor=fff&color=blue&label=total%20contributions&query=%24.totalContributions&url=https%3A%2F%2Fstreak-stats.demolab.com%2F%3Fuser%3Ddiegosouzapw%26type%3Djson)](https://github.com/diegosouzapw)
[![code size](https://custom-icon-badges.demolab.com/github/languages/code-size/diegosouzapw/OmniRoute?logo=file-code&logoColor=white)](https://github.com/diegosouzapw/OmniRoute)
[![pr closed](https://custom-icon-badges.demolab.com/github/issues-pr-closed/diegosouzapw/OmniRoute?color=purple&logo=git-pull-request&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/pulls?q=is%3Apr+is%3Aclosed)
[![tag](https://custom-icon-badges.demolab.com/github/v/tag/diegosouzapw/OmniRoute?logo=tag&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/tags)
[![github streak](https://custom-icon-badges.demolab.com/badge/dynamic/json?logo=fire&logoColor=fff&color=orange&label=github%20streak&query=%24.currentStreak.length&suffix=%20days&url=https%3A%2F%2Fstreak-stats.demolab.com%2F%3Fuser%3Ddiegosouzapw%26type%3Djson)](https://github.com/diegosouzapw)
[![followers](https://custom-icon-badges.demolab.com/github/followers/diegosouzapw?logo=person-add)](https://github.com/diegosouzapw?tab=followers)
[![fork](https://custom-icon-badges.demolab.com/github/forks/diegosouzapw/OmniRoute?logo=fork)](https://github.com/diegosouzapw/OmniRoute/network/members)
[![watch](https://custom-icon-badges.demolab.com/github/watchers/diegosouzapw/OmniRoute?logo=eye)](https://github.com/diegosouzapw/OmniRoute/watchers)

[![License](https://img.shields.io/github/license/diegosouzapw/OmniRoute)](https://github.com/diegosouzapw/OmniRoute/blob/main/LICENSE)
[![Website](https://img.shields.io/badge/Website-omniroute.online-blue?logo=google-chrome&logoColor=white)](https://omniroute.online)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Community-25D366?logo=whatsapp&logoColor=white)](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)

[🌐 Website](https://omniroute.online) • [🚀 Quick Start](#-quick-start) • [💡 Features](#-key-features) • [📖 Docs](#-documentation) • [💰 Pricing](#-pricing-at-a-glance) • [💬 WhatsApp](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)

</div>

🌐 **Available in:** 🇺🇸 [English](README.md) | 🇧🇷 [Português (Brasil)](docs/i18n/pt-BR/README.md) | 🇪🇸 [Español](docs/i18n/es/README.md) | 🇫🇷 [Français](docs/i18n/fr/README.md) | 🇮🇹 [Italiano](docs/i18n/it/README.md) | 🇷🇺 [Русский](docs/i18n/ru/README.md) | 🇨🇳 [中文 (简体)](docs/i18n/zh-CN/README.md) | 🇩🇪 [Deutsch](docs/i18n/de/README.md) | 🇮🇳 [हिन्दी](docs/i18n/in/README.md) | 🇹🇭 [ไทย](docs/i18n/th/README.md) | 🇺🇦 [Українська](docs/i18n/uk-UA/README.md) | 🇸🇦 [العربية](docs/i18n/ar/README.md) | 🇯🇵 [日本語](docs/i18n/ja/README.md) | 🇻🇳 [Tiếng Việt](docs/i18n/vi/README.md) | 🇧🇬 [Български](docs/i18n/bg/README.md) | 🇩🇰 [Dansk](docs/i18n/da/README.md) | 🇫🇮 [Suomi](docs/i18n/fi/README.md) | 🇮🇱 [עברית](docs/i18n/he/README.md) | 🇭🇺 [Magyar](docs/i18n/hu/README.md) | 🇮🇩 [Bahasa Indonesia](docs/i18n/id/README.md) | 🇰🇷 [한국어](docs/i18n/ko/README.md) | 🇲🇾 [Bahasa Melayu](docs/i18n/ms/README.md) | 🇳🇱 [Nederlands](docs/i18n/nl/README.md) | 🇳🇴 [Norsk](docs/i18n/no/README.md) | 🇵🇹 [Português (Portugal)](docs/i18n/pt/README.md) | 🇷🇴 [Română](docs/i18n/ro/README.md) | 🇵🇱 [Polski](docs/i18n/pl/README.md) | 🇸🇰 [Slovenčina](docs/i18n/sk/README.md) | 🇸🇪 [Svenska](docs/i18n/sv/README.md) | 🇵🇭 [Filipino](docs/i18n/phi/README.md) | 🇨🇿 [Čeština](docs/i18n/cs/README.md)

---

## 🖼️ Main Dashboard

<div align="center">
  <img src="./docs/screenshots/MainOmniRoute.png" alt="OmniRoute Dashboard" width="800"/>
</div>

---

## 📸 Dashboard Preview

<details>
<summary><b>Click to see dashboard screenshots</b></summary>

| Page           | Screenshot                                        |
| -------------- | ------------------------------------------------- |
| **Providers**  | ![Providers](docs/screenshots/01-providers.png)   |
| **Combos**     | ![Combos](docs/screenshots/02-combos.png)         |
| **Analytics**  | ![Analytics](docs/screenshots/03-analytics.png)   |
| **Health**     | ![Health](docs/screenshots/04-health.png)         |
| **Translator** | ![Translator](docs/screenshots/05-translator.png) |
| **Settings**   | ![Settings](docs/screenshots/06-settings.png)     |
| **CLI Tools**  | ![CLI Tools](docs/screenshots/07-cli-tools.png)   |
| **Usage Logs** | ![Usage](docs/screenshots/08-usage.png)           |
| **Endpoints**  | ![Endpoints](docs/screenshots/09-endpoint.png)    |

</details>

---

### 🤖 Free AI Provider for your favorite coding agents

_Connect any AI-powered IDE or CLI tool through OmniRoute — free API gateway for unlimited coding._

  <table>
    <tr>
      <td align="center" width="110">
        <a href="https://github.com/openclaw/openclaw">
          <img src="./public/providers/openclaw.png" alt="OpenClaw" width="48"/><br/>
          <b>OpenClaw</b>
        </a><br/>
        <sub>⭐ 205K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/HKUDS/nanobot">
          <img src="./public/providers/nanobot.png" alt="NanoBot" width="48"/><br/>
          <b>NanoBot</b>
        </a><br/>
        <sub>⭐ 20.9K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/sipeed/picoclaw">
          <img src="./public/providers/picoclaw.jpg" alt="PicoClaw" width="48"/><br/>
          <b>PicoClaw</b>
        </a><br/>
        <sub>⭐ 14.6K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/zeroclaw-labs/zeroclaw">
          <img src="./public/providers/zeroclaw.png" alt="ZeroClaw" width="48"/><br/>
          <b>ZeroClaw</b>
        </a><br/>
        <sub>⭐ 9.9K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/nearai/ironclaw">
          <img src="./public/providers/ironclaw.png" alt="IronClaw" width="48"/><br/>
          <b>IronClaw</b>
        </a><br/>
        <sub>⭐ 2.1K</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="110">
        <a href="https://github.com/anomalyco/opencode">
          <img src="./public/providers/opencode.svg" alt="OpenCode" width="48"/><br/>
          <b>OpenCode</b>
        </a><br/>
        <sub>⭐ 106K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/openai/codex">
          <img src="./public/providers/codex.png" alt="Codex CLI" width="48"/><br/>
          <b>Codex CLI</b>
        </a><br/>
        <sub>⭐ 60.8K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/anthropics/claude-code">
          <img src="./public/providers/claude.png" alt="Claude Code" width="48"/><br/>
          <b>Claude Code</b>
        </a><br/>
        <sub>⭐ 67.3K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/google-gemini/gemini-cli">
          <img src="./public/providers/gemini-cli.png" alt="Gemini CLI" width="48"/><br/>
          <b>Gemini CLI</b>
        </a><br/>
        <sub>⭐ 94.7K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/Kilo-Org/kilocode">
          <img src="./public/providers/kilocode.png" alt="Kilo Code" width="48"/><br/>
          <b>Kilo Code</b>
        </a><br/>
        <sub>⭐ 15.5K</sub>
      </td>
    </tr>
  </table>

<sub>📡 All agents connect via <code>http://localhost:20128/v1</code> or <code>http://cloud.omniroute.online/v1</code> — one config, unlimited models and quota</sub>

---

## 🤔 Why OmniRoute?

**Stop wasting money and hitting limits:**

- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Subscription quota expires unused every month
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Rate limits stop you mid-coding
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Expensive APIs ($20-50/month per provider)
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Manual switching between providers

**OmniRoute solves this:**

- ✅ **Maximize subscriptions** - Track quota, use every bit before reset
- ✅ **Auto fallback** - Subscription → API Key → Cheap → Free, zero downtime
- ✅ **Multi-account** - Round-robin between accounts per provider
- ✅ **Universal** - Works with Claude Code, Codex, Gemini CLI, Cursor, Cline, OpenClaw, any CLI tool

---

## 📧 Support

> 💬 **Join our community!** [WhatsApp Group](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t) — Get help, share tips, and stay updated.

- **Website**: [omniroute.online](https://omniroute.online)
- **GitHub**: [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- **Issues**: [github.com/diegosouzapw/OmniRoute/issues](https://github.com/diegosouzapw/OmniRoute/issues)
- **WhatsApp**: [Community Group](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md), open a PR, or pick a `good first issue`
- **Original Project**: [9router by decolua](https://github.com/decolua/9router)

### 🐛 Reporting a Bug?

When opening an issue, please run the system-info command and attach the generated file:

```bash
npm run system-info
```

This generates a `system-info.txt` with your Node.js version, OmniRoute version, OS details, installed CLI tools (qoder, gemini, claude, codex, antigravity, droid, etc.), Docker/PM2 status, and system packages — everything we need to reproduce your issue quickly. Attach the file directly to your GitHub issue.

---

## 🔄 How It Works

```
┌─────────────┐
│  Your CLI   │  (Claude Code, Codex, Gemini CLI, OpenClaw, Cursor, Cline...)
│   Tool      │
└──────┬──────┘
       │ http://localhost:20128/v1
       ↓
┌─────────────────────────────────────────┐
│           OmniRoute (Smart Router)        │
│  • Format translation (OpenAI ↔ Claude) │
│  • Quota tracking + Embeddings + Images │
│  • Auto token refresh                   │
└──────┬──────────────────────────────────┘
       │
       ├─→ [Tier 1: SUBSCRIPTION] Claude Code, Codex, Gemini CLI
       │   ↓ quota exhausted
       ├─→ [Tier 2: API KEY] DeepSeek, Groq, xAI, Mistral, NVIDIA NIM, etc.
       │   ↓ budget limit
       ├─→ [Tier 3: CHEAP] GLM ($0.6/1M), MiniMax ($0.2/1M)
       │   ↓ budget limit
       └─→ [Tier 4: FREE] Qoder, Qwen, Kiro (unlimited)

Result: Never stop coding, minimal cost
```

---

## 🎯 What OmniRoute Solves — 30 Real Pain Points & Use Cases

> **Every developer using AI tools faces these problems daily.** OmniRoute was built to solve them all — from cost overruns to regional blocks, from broken OAuth flows to protocol operations and enterprise observability.

<details>
<summary><b>💸 1. "I pay for an expensive subscription but still get interrupted by limits"</b></summary>

Developers pay $20–200/month for Claude Pro, Codex Pro, or GitHub Copilot. Even paying, quota has a ceiling — 5h of usage, weekly limits, or per-minute rate limits. Mid-coding session, the provider stops responding and the developer loses flow and productivity.

**How OmniRoute solves it:**

- **Smart 4-Tier Fallback** — If subscription quota runs out, automatically redirects to API Key → Cheap → Free with zero manual intervention
- **Provider Limits Tracking** — Cached quota snapshots refresh on a server-side schedule (default `PROVIDER_LIMITS_SYNC_INTERVAL_MINUTES=70`) with manual refresh available in the UI
- **Multi-Account Support** — Multiple accounts per provider with auto round-robin — when one runs out, switches to the next
- **Custom Combos** — Customizable fallback chains with 9 balancing strategies (priority, weighted, fill-first, round-robin, P2C, random, least-used, cost-optimized, strict-random)
- **Codex Business Quotas** — Business/Team workspace quota monitoring directly in the dashboard

</details>

<details>
<summary><b>🔌 2. "I need to use multiple providers but each has a different API"</b></summary>

... [TRUNCATED]
```

### File: docs\i18n\de\README.md
```md
# 🚀 OmniRoute — The Free AI Gateway (Deutsch)

🌐 **Languages:** 🇺🇸 [English](../../../README.md) · 🇪🇸 [es](../es/README.md) · 🇫🇷 [fr](../fr/README.md) · 🇩🇪 [de](../de/README.md) · 🇮🇹 [it](../it/README.md) · 🇷🇺 [ru](../ru/README.md) · 🇨🇳 [zh-CN](../zh-CN/README.md) · 🇯🇵 [ja](../ja/README.md) · 🇰🇷 [ko](../ko/README.md) · 🇸🇦 [ar](../ar/README.md) · 🇮🇳 [hi](../hi/README.md) · 🇮🇳 [in](../in/README.md) · 🇹🇭 [th](../th/README.md) · 🇻🇳 [vi](../vi/README.md) · 🇮🇩 [id](../id/README.md) · 🇲🇾 [ms](../ms/README.md) · 🇳🇱 [nl](../nl/README.md) · 🇵🇱 [pl](../pl/README.md) · 🇸🇪 [sv](../sv/README.md) · 🇳🇴 [no](../no/README.md) · 🇩🇰 [da](../da/README.md) · 🇫🇮 [fi](../fi/README.md) · 🇵🇹 [pt](../pt/README.md) · 🇷🇴 [ro](../ro/README.md) · 🇭🇺 [hu](../hu/README.md) · 🇧🇬 [bg](../bg/README.md) · 🇸🇰 [sk](../sk/README.md) · 🇺🇦 [uk-UA](../uk-UA/README.md) · 🇮🇱 [he](../he/README.md) · 🇵🇭 [phi](../phi/README.md) · 🇧🇷 [pt-BR](../pt-BR/README.md) · 🇨🇿 [cs](../cs/README.md) · 🇹🇷 [tr](../tr/README.md)

---

### Never stop coding. Smart routing to **FREE & low-cost AI models** with automatic fallback.

_Your universal API proxy — one endpoint, 60+ providers, zero downtime. Now with **MCP Server (25 tools)**, **A2A Protocol**, **Memory/Skills Systems** & **Electron Desktop App**._

**Chat Completions • Embeddings • Image Generation • Video • Music • Audio • Reranking • **Web Search** • MCP Server • A2A Protocol • 100% TypeScript**

---

<div align="center">

[![npm version](https://img.shields.io/npm/v/omniroute?color=cb3837&logo=npm)](https://www.npmjs.com/package/omniroute)
[![Docker Hub](https://img.shields.io/docker/v/diegosouzapw/omniroute?label=Docker%20Hub&logo=docker&color=2496ED)](https://hub.docker.com/r/diegosouzapw/omniroute)

![NPM Downloads](https://img.shields.io/npm/dw/omniroute?label=npm%20down%20week&color=red)
![NPM Downloads](https://img.shields.io/npm/dm/omniroute?label=npm%20down%20month&color=red)

![NPM Downloads](https://img.shields.io/npm/d18m/omniroute?label=npm%20down%20year&color=red)
![Docker Pulls](https://img.shields.io/docker/pulls/diegosouzapw/omniroute)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/diegosouzapw/omniroute/total?style=flat&label=eletron%20donwloads&color=blue)

[![stars](https://custom-icon-badges.demolab.com/github/stars/diegosouzapw/OmniRoute?logo=star&style=flat)](https://github.com/diegosouzapw/OmniRoute/stargazers)
[![open issues](https://custom-icon-badges.demolab.com/github/issues-raw/diegosouzapw/OmniRoute?logo=issue)](https://github.com/diegosouzapw/OmniRoute/issues)
[![license](https://custom-icon-badges.demolab.com/github/license/diegosouzapw/OmniRoute?logo=law)](https://github.com/diegosouzapw/OmniRoute/blob/main/LICENSE)
[![last commit](https://custom-icon-badges.demolab.com/github/last-commit/diegosouzapw/OmniRoute?logo=history&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/commits/main)
[![total contributions](https://custom-icon-badges.demolab.com/badge/dynamic/json?logo=graph&logoColor=fff&color=blue&label=total%20contributions&query=%24.totalContributions&url=https%3A%2F%2Fstreak-stats.demolab.com%2F%3Fuser%3Ddiegosouzapw%26type%3Djson)](https://github.com/diegosouzapw)
[![code size](https://custom-icon-badges.demolab.com/github/languages/code-size/diegosouzapw/OmniRoute?logo=file-code&logoColor=white)](https://github.com/diegosouzapw/OmniRoute)
[![pr closed](https://custom-icon-badges.demolab.com/github/issues-pr-closed/diegosouzapw/OmniRoute?color=purple&logo=git-pull-request&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/pulls?q=is%3Apr+is%3Aclosed)
[![tag](https://custom-icon-badges.demolab.com/github/v/tag/diegosouzapw/OmniRoute?logo=tag&logoColor=white)](https://github.com/diegosouzapw/OmniRoute/tags)
[![github streak](https://custom-icon-badges.demolab.com/badge/dynamic/json?logo=fire&logoColor=fff&color=orange&label=github%20streak&query=%24.currentStreak.length&suffix=%20days&url=https%3A%2F%2Fstreak-stats.demolab.com%2F%3Fuser%3Ddiegosouzapw%26type%3Djson)](https://github.com/diegosouzapw)
[![followers](https://custom-icon-badges.demolab.com/github/followers/diegosouzapw?logo=person-add)](https://github.com/diegosouzapw?tab=followers)
[![fork](https://custom-icon-badges.demolab.com/github/forks/diegosouzapw/OmniRoute?logo=fork)](https://github.com/diegosouzapw/OmniRoute/network/members)
[![watch](https://custom-icon-badges.demolab.com/github/watchers/diegosouzapw/OmniRoute?logo=eye)](https://github.com/diegosouzapw/OmniRoute/watchers)

[![License](https://img.shields.io/github/license/diegosouzapw/OmniRoute)](https://github.com/diegosouzapw/OmniRoute/blob/main/LICENSE)
[![Website](https://img.shields.io/badge/Website-omniroute.online-blue?logo=google-chrome&logoColor=white)](https://omniroute.online)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Community-25D366?logo=whatsapp&logoColor=white)](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)

[🌐 Website](https://omniroute.online) • [🚀 Quick Start](#-quick-start) • [💡 Features](#-key-features) • [📖 Docs](#-documentation) • [💰 Pricing](#-pricing-at-a-glance) • [💬 WhatsApp](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)

</div>

🌐 **Available in:** 🇺🇸 [English](README.md) | 🇧🇷 [Português (Brasil)](docs/i18n/pt-BR/README.md) | 🇪🇸 [Español](docs/i18n/es/README.md) | 🇫🇷 [Français](docs/i18n/fr/README.md) | 🇮🇹 [Italiano](docs/i18n/it/README.md) | 🇷🇺 [Русский](docs/i18n/ru/README.md) | 🇨🇳 [中文 (简体)](docs/i18n/zh-CN/README.md) | 🇩🇪 [Deutsch](docs/i18n/de/README.md) | 🇮🇳 [हिन्दी](docs/i18n/in/README.md) | 🇹🇭 [ไทย](docs/i18n/th/README.md) | 🇺🇦 [Українська](docs/i18n/uk-UA/README.md) | 🇸🇦 [العربية](docs/i18n/ar/README.md) | 🇯🇵 [日本語](docs/i18n/ja/README.md) | 🇻🇳 [Tiếng Việt](docs/i18n/vi/README.md) | 🇧🇬 [Български](docs/i18n/bg/README.md) | 🇩🇰 [Dansk](docs/i18n/da/README.md) | 🇫🇮 [Suomi](docs/i18n/fi/README.md) | 🇮🇱 [עברית](docs/i18n/he/README.md) | 🇭🇺 [Magyar](docs/i18n/hu/README.md) | 🇮🇩 [Bahasa Indonesia](docs/i18n/id/README.md) | 🇰🇷 [한국어](docs/i18n/ko/README.md) | 🇲🇾 [Bahasa Melayu](docs/i18n/ms/README.md) | 🇳🇱 [Nederlands](docs/i18n/nl/README.md) | 🇳🇴 [Norsk](docs/i18n/no/README.md) | 🇵🇹 [Português (Portugal)](docs/i18n/pt/README.md) | 🇷🇴 [Română](docs/i18n/ro/README.md) | 🇵🇱 [Polski](docs/i18n/pl/README.md) | 🇸🇰 [Slovenčina](docs/i18n/sk/README.md) | 🇸🇪 [Svenska](docs/i18n/sv/README.md) | 🇵🇭 [Filipino](docs/i18n/phi/README.md) | 🇨🇿 [Čeština](docs/i18n/cs/README.md)

---

## 🖼️ Main Dashboard

<div align="center">
  <img src="./docs/screenshots/MainOmniRoute.png" alt="OmniRoute Dashboard" width="800"/>
</div>

---

## 📸 Dashboard Preview

<details>
<summary><b>Click to see dashboard screenshots</b></summary>

| Page           | Screenshot                                        |
| -------------- | ------------------------------------------------- |
| **Providers**  | ![Providers](docs/screenshots/01-providers.png)   |
| **Combos**     | ![Combos](docs/screenshots/02-combos.png)         |
| **Analytics**  | ![Analytics](docs/screenshots/03-analytics.png)   |
| **Health**     | ![Health](docs/screenshots/04-health.png)         |
| **Translator** | ![Translator](docs/screenshots/05-translator.png) |
| **Settings**   | ![Settings](docs/screenshots/06-settings.png)     |
| **CLI Tools**  | ![CLI Tools](docs/screenshots/07-cli-tools.png)   |
| **Usage Logs** | ![Usage](docs/screenshots/08-usage.png)           |
| **Endpoints**  | ![Endpoints](docs/screenshots/09-endpoint.png)    |

</details>

---

### 🤖 Free AI Provider for your favorite coding agents

_Connect any AI-powered IDE or CLI tool through OmniRoute — free API gateway for unlimited coding._

  <table>
    <tr>
      <td align="center" width="110">
        <a href="https://github.com/openclaw/openclaw">
          <img src="./public/providers/openclaw.png" alt="OpenClaw" width="48"/><br/>
          <b>OpenClaw</b>
        </a><br/>
        <sub>⭐ 205K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/HKUDS/nanobot">
          <img src="./public/providers/nanobot.png" alt="NanoBot" width="48"/><br/>
          <b>NanoBot</b>
        </a><br/>
        <sub>⭐ 20.9K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/sipeed/picoclaw">
          <img src="./public/providers/picoclaw.jpg" alt="PicoClaw" width="48"/><br/>
          <b>PicoClaw</b>
        </a><br/>
        <sub>⭐ 14.6K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/zeroclaw-labs/zeroclaw">
          <img src="./public/providers/zeroclaw.png" alt="ZeroClaw" width="48"/><br/>
          <b>ZeroClaw</b>
        </a><br/>
        <sub>⭐ 9.9K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/nearai/ironclaw">
          <img src="./public/providers/ironclaw.png" alt="IronClaw" width="48"/><br/>
          <b>IronClaw</b>
        </a><br/>
        <sub>⭐ 2.1K</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="110">
        <a href="https://github.com/anomalyco/opencode">
          <img src="./public/providers/opencode.svg" alt="OpenCode" width="48"/><br/>
          <b>OpenCode</b>
        </a><br/>
        <sub>⭐ 106K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/openai/codex">
          <img src="./public/providers/codex.png" alt="Codex CLI" width="48"/><br/>
          <b>Codex CLI</b>
        </a><br/>
        <sub>⭐ 60.8K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/anthropics/claude-code">
          <img src="./public/providers/claude.png" alt="Claude Code" width="48"/><br/>
          <b>Claude Code</b>
        </a><br/>
        <sub>⭐ 67.3K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/google-gemini/gemini-cli">
          <img src="./public/providers/gemini-cli.png" alt="Gemini CLI" width="48"/><br/>
          <b>Gemini CLI</b>
        </a><br/>
        <sub>⭐ 94.7K</sub>
      </td>
      <td align="center" width="110">
        <a href="https://github.com/Kilo-Org/kilocode">
          <img src="./public/providers/kilocode.png" alt="Kilo Code" width="48"/><br/>
          <b>Kilo Code</b>
        </a><br/>
        <sub>⭐ 15.5K</sub>
      </td>
    </tr>
  </table>

<sub>📡 All agents connect via <code>http://localhost:20128/v1</code> or <code>http://cloud.omniroute.online/v1</code> — one config, unlimited models and quota</sub>

---

## 🤔 Why OmniRoute?

**Stop wasting money and hitting limits:**

- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Subscription quota expires unused every month
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Rate limits stop you mid-coding
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Expensive APIs ($20-50/month per provider)
- <img src="https://img.shields.io/badge/✗-e74c3c?style=flat-square" height="16"/> Manual switching between providers

**OmniRoute solves this:**

- ✅ **Maximize subscriptions** - Track quota, use every bit before reset
- ✅ **Auto fallback** - Subscription → API Key → Cheap → Free, zero downtime
- ✅ **Multi-account** - Round-robin between accounts per provider
- ✅ **Universal** - Works with Claude Code, Codex, Gemini CLI, Cursor, Cline, OpenClaw, any CLI tool

---

## 📧 Support

> 💬 **Join our community!** [WhatsApp Group](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t) — Get help, share tips, and stay updated.

- **Website**: [omniroute.online](https://omniroute.online)
- **GitHub**: [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- **Issues**: [github.com/diegosouzapw/OmniRoute/issues](https://github.com/diegosouzapw/OmniRoute/issues)
- **WhatsApp**: [Community Group](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md), open a PR, or pick a `good first issue`
- **Original Project**: [9router by decolua](https://github.com/decolua/9router)

### 🐛 Reporting a Bug?

When opening an issue, please run the system-info command and attach the generated file:

```bash
npm run system-info
```

This generates a `system-info.txt` with your Node.js version, OmniRoute version, OS details, installed CLI tools (qoder, gemini, claude, codex, antigravity, droid, etc.), Docker/PM2 status, and system packages — everything we need to reproduce your issue quickly. Attach the file directly to your GitHub issue.

---

## 🔄 How It Works

```
┌─────────────┐
│  Your CLI   │  (Claude Code, Codex, Gemini CLI, OpenClaw, Cursor, Cline...)
│   Tool      │
└──────┬──────┘
       │ http://localhost:20128/v1
       ↓
┌─────────────────────────────────────────┐
│           OmniRoute (Smart Router)        │
│  • Format translation (OpenAI ↔ Claude) │
│  • Quota tracking + Embeddings + Images │
│  • Auto token refresh                   │
└──────┬──────────────────────────────────┘
       │
       ├─→ [Tier 1: SUBSCRIPTION] Claude Code, Codex, Gemini CLI
       │   ↓ quota exhausted
       ├─→ [Tier 2: API KEY] DeepSeek, Groq, xAI, Mistral, NVIDIA NIM, etc.
       │   ↓ budget limit
       ├─→ [Tier 3: CHEAP] GLM ($0.6/1M), MiniMax ($0.2/1M)
       │   ↓ budget limit
       └─→ [Tier 4: FREE] Qoder, Qwen, Kiro (unlimited)

Result: Never stop coding, minimal cost
```

---

## 🎯 What OmniRoute Solves — 30 Real Pain Points & Use Cases

> **Every developer using AI tools faces these problems daily.** OmniRoute was built to solve them all — from cost overruns to regional blocks, from broken OAuth flows to protocol operations and enterprise observability.

<details>
<summary><b>💸 1. "I pay for an expensive subscription but still get interrupted by limits"</b></summary>

Developers pay $20–200/month for Claude Pro, Codex Pro, or GitHub Copilot. Even paying, quota has a ceiling — 5h of usage, weekly limits, or per-minute rate limits. Mid-coding session, the provider stops responding and the developer loses flow and productivity.

**How OmniRoute solves it:**

- **Smart 4-Tier Fallback** — If subscription quota runs out, automatically redirects to API Key → Cheap → Free with zero manual intervention
- **Provider Limits Tracking** — Cached quota snapshots refresh on a server-side schedule (default `PROVIDER_LIMITS_SYNC_INTERVAL_MINUTES=70`) with manual refresh available in the UI
- **Multi-Account Support** — Multiple accounts per provider with auto round-robin — when one runs out, switches to the next
- **Custom Combos** — Customizable fallback chains with 9 balancing strategies (priority, weighted, fill-first, round-robin, P2C, random, least-used, cost-optimized, strict-random)
- **Codex Business Quotas** — Business/Team workspace quota monitoring directly in the dashboard

</details>

<details>
<summary><b>🔌 2. "I need to use multiple providers but each has a different API"</b></summary>

... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
