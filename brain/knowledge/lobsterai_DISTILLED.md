---
id: LobsterAI
type: knowledge
owner: OA_Triage
---
# LobsterAI
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "lobsterai",
  "private": true,
  "author": {
    "name": "LobsterAI",
    "email": "lobsterai.project@rd.netease.com"
  },
  "license": "MIT",
  "version": "2026.3.26",
  "openclaw": {
    "version": "v2026.3.2",
    "repo": "https://github.com/openclaw/openclaw.git",
    "plugins": [
      {
        "id": "dingtalk-connector",
        "npm": "@dingtalk-real-ai/dingtalk-connector",
        "version": "0.7.9"
      },
      {
        "id": "feishu-openclaw-plugin",
        "npm": "@larksuiteoapi/feishu-openclaw-plugin",
        "version": "2026.3.8"
      },
      {
        "id": "qqbot",
        "npm": "@sliverp/qqbot",
        "version": "1.5.3"
      },
      {
        "id": "wecom-openclaw-plugin",
        "npm": "@wecom/wecom-openclaw-plugin",
        "version": "1.0.12"
      },
      {
        "id": "openclaw-weixin",
        "npm": "@tencent-weixin/openclaw-weixin",
        "version": "1.0.2"
      },
      {
        "id": "moltbot-popo",
        "npm": "moltbot-popo",
        "version": "1.0.66",
        "registry": "https://npm.nie.netease.com",
        "optional": true
      },
      {
        "id": "nim",
        "npm": "openclaw-nim",
        "version": "0.3.0"
      }
    ]
  },
  "main": "dist-electron/main.js",
  "engines": {
    "node": ">=24 <25"
  },
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "test": "vitest run",
    "preview": "vite preview",
    "compile:electron": "tsc --project electron-tsconfig.json",
    "build:skill:web-search": "npm install --prefix SKILLs/web-search && npx tsc -p SKILLs/web-search/tsconfig.json",
    "build:skill:tech-news": "node scripts/build-skill-tech-news.js",
    "build:skill:email": "cd SKILLs/imap-smtp-email && npm install --production",
    "build:skills": "npm run build:skill:web-search && npm run build:skill:tech-news && npm run build:skill:email",
    "start:electron": "cross-env NODE_ENV=development ELECTRON_START_URL=http://localhost:5175 electron .",
    "electron:dev": "rimraf dist-electron && npm run compile:electron && concurrently \"vite --port 5175\" \"wait-on -v -t 120000 -d 20000 http://localhost:5175 dist-electron/.electron-ready && npm run start:electron\"",
    "electron:dev:openclaw": "npm run openclaw:runtime:host && npm run electron:dev",
    "postinstall": "patch-package && electron-builder install-app-deps",
    "pack": "npm run setup:python-runtime && npm run build && npm run compile:electron && npm run build:skills && electron-builder --dir",
    "dist": "npm run setup:python-runtime && npm run build && npm run compile:electron && npm run build:skills && electron-builder",
    "dist:mac": "node -r dotenv/config node_modules/.bin/electron-builder --mac --config electron-builder.json",
    "predist:mac": "npm run build && npm run compile:electron && npm run build:skills && npm run openclaw:runtime:mac-arm64",
    "dist:mac:x64": "npm run build && npm run compile:electron && npm run build:skills && npm run openclaw:runtime:mac-x64 && electron-builder --mac --x64",
    "dist:mac:arm64": "npm run build && npm run compile:electron && npm run build:skills && npm run openclaw:runtime:mac-arm64 && electron-builder --mac --arm64",
    "dist:mac:universal": "npm run build && npm run compile:electron && npm run build:skills && electron-builder --mac --universal",
    "predist:win": "npm run openclaw:runtime:win-x64",
    "dist:win": "npm run setup:python-runtime && npm run build && npm run compile:electron && npm run build:skills && electron-builder --win --x64",
    "predist:linux": "npm run openclaw:runtime:linux-x64",
    "dist:linux": "npm run build && npm run compile:electron && npm run build:skills && electron-builder --linux",
    "clean:release": "rimraf release",
    "generate:tray-icons": "node scripts/generate-tray-icons.js",
    "setup:mingit": "node scripts/setup-mingit.js",
    "setup:python-runtime": "node scripts/setup-python-runtime.js",
    "openclaw:ensure": "node scripts/ensure-openclaw-version.cjs",
    "openclaw:patch": "node scripts/apply-openclaw-patches.cjs",
    "openclaw:plugins": "node scripts/ensure-openclaw-plugins.cjs",
    "openclaw:extensions:local": "node scripts/sync-local-openclaw-extensions.cjs",
    "openclaw:bundle": "node scripts/bundle-openclaw-gateway.cjs",
    "openclaw:precompile": "node scripts/precompile-openclaw-extensions.cjs",
    "openclaw:prune": "node scripts/prune-openclaw-runtime.cjs",
    "openclaw:runtime:host": "node scripts/openclaw-runtime-host.cjs",
    "openclaw:runtime:mac-arm64": "npm run openclaw:ensure && npm run openclaw:patch && node scripts/run-build-openclaw-runtime.cjs mac-arm64 && node scripts/sync-openclaw-runtime-current.cjs mac-arm64 && npm run openclaw:bundle && npm run openclaw:plugins && npm run openclaw:extensions:local && npm run openclaw:precompile && npm run openclaw:prune",
    "openclaw:runtime:mac-x64": "npm run openclaw:ensure && npm run openclaw:patch && node scripts/run-build-openclaw-runtime.cjs mac-x64 && node scripts/sync-openclaw-runtime-current.cjs mac-x64 && npm run openclaw:bundle && npm run openclaw:plugins && npm run openclaw:extensions:local && npm run openclaw:precompile && npm run openclaw:prune",
    "openclaw:runtime:win-x64": "npm run openclaw:ensure && npm run openclaw:patch && node scripts/run-build-openclaw-runtime.cjs win-x64 && node scripts/sync-openclaw-runtime-current.cjs win-x64 && npm run openclaw:bundle && npm run openclaw:plugins && npm run openclaw:extensions:local && npm run openclaw:precompile && npm run openclaw:prune",
    "openclaw:runtime:win-arm64": "npm run openclaw:ensure && npm run openclaw:patch && node scripts/run-build-openclaw-runtime.cjs win-arm64 && node scripts/sync-openclaw-runtime-current.cjs win-arm64 && npm run openclaw:bundle && npm run openclaw:plugins && npm run openclaw:extensions:local && npm run openclaw:precompile && npm run openclaw:prune",
    "openclaw:runtime:linux-x64": "npm run openclaw:ensure && npm run openclaw:patch && node scripts/run-build-openclaw-runtime.cjs linux-x64 && node scripts/sync-openclaw-runtime-current.cjs linux-x64 && npm run openclaw:bundle && npm run openclaw:plugins && npm run openclaw:extensions:local && npm run openclaw:precompile && npm run openclaw:prune",
    "openclaw:runtime:linux-arm64": "npm run openclaw:ensure && npm run openclaw:patch && node scripts/run-build-openclaw-runtime.cjs linux-arm64 && node scripts/sync-openclaw-runtime-current.cjs linux-arm64 && npm run openclaw:bundle && npm run openclaw:plugins && npm run openclaw:extensions:local && npm run openclaw:precompile && npm run openclaw:prune",
    "regenerate:icon": "bash scripts/regenerate-mac-icon.sh",
    "fix:mac-icon": "bash scripts/fix-mac-icon-display.sh"
  },
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "0.2.12",
    "@electron/remote": "^2.0.12",
    "@headlessui/react": "^1.7.18",
    "@heroicons/react": "^2.1.1",
    "@larksuite/openclaw-lark": "^2026.3.17",
    "@larksuite/openclaw-lark-tools": "~1.0.26",
    "@larksuiteoapi/node-sdk": "^1.58.0",
    "@modelcontextprotocol/sdk": "^1.27.1",
    "@nodesecure/js-x-ray": "^14.2.0",
    "@reduxjs/toolkit": "^2.2.1",
    "@types/uuid": "^10.0.0",
    "@wecom/wecom-aibot-sdk": "^0.1.0",
    "bufferutil": "^4.1.0",
    "cheerio": "^1.2.0",
    "cron-parser": "^5.5.0",
    "cronstrue": "^3.14.0",
    "dompurify": "^3.3.1",
    "electron-log": "^5.4.3",
    "extract-zip": "^2.0.1",
    "form-data": "^4.0.5",
    "js-yaml": "^4.1.1",
    "katex": "^0.16.21",
    "mermaid": "^10.9.5",
    "nim-web-sdk-ng": "10.9.77-alpha.4",
    "npm": "^11.11.0",
    "qrcode.react": "^4.2.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^10.0.0",
    "react-redux": "^9.1.0",
    "react-syntax-highlighter": "^15.6.1",
    "rehype-katex": "^7.0.1",
    "remark-gfm": "^4.0.1",
    "remark-math": "^6.0.0",
    "sql.js": "^1.13.0",
    "tar": "^7.5.11",
    "utf-8-validate": "^6.0.6",
    "uuid": "^11.1.0",
    "yazl": "^3.3.1",
    "zod": "^4.3.6"
  },
  "overrides": {
    "@electron/osx-sign": {
      "isbinaryfile": "^5.0.0"
    }
  },
  "devDependencies": {
    "@tailwindcss/typography": "^0.5.16",
    "@types/dompurify": "^3.0.5",
    "@types/extract-zip": "^2.0.1",
    "@types/js-yaml": "^4.0.9",
    "@types/node": "^24.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@types/sql.js": "^1.4.9",
    "@types/yazl": "^3.3.0",
    "@typescript-eslint/eslint-plugin": "^8.56.0",
    "@typescript-eslint/parser": "^8.56.0",
    "@vitejs/plugin-react": "^4.2.1",
    "7zip-bin": "^5.2.0",
    "autoprefixer": "^10.4.17",
    "concurrently": "^8.2.2",
    "cross-env": "^7.0.3",
    "electron": "40.2.1",
    "electron-builder": "^24.12.0",
    "esbuild": "^0.21.5",
    "eslint": "^8.56.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "patch-package": "^8.0.1",
    "postcss": "^8.4.35",
    "rimraf": "^5.0.5",
    "rss-parser": "^3.13.0",
    "tailwindcss": "^3.4.1",
    "typescript": "^5.7.3",
    "vite": "^5.1.4",
    "vite-plugin-electron": "^0.28.0",
    "vite-plugin-electron-renderer": "^0.14.5",
    "vitest": "^4.1.0",
    "wait-on": "^7.2.0"
  }
}

```

### File: README.md
```md
# LobsterAI — All-in-One Personal Assistant Agent

<p align="center">
  <img src="public/logo.png" alt="LobsterAI" width="120">
</p>

<p align="center">
  <strong>A 24/7 personal assistant Agent that gets things done, built by NetEase Youdao</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <br>
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux%20%7C%20Mobile-brightgreen?style=for-the-badge" alt="Platform">
  <br>
  <img src="https://img.shields.io/badge/Electron-40-47848F?style=for-the-badge&logo=electron&logoColor=white" alt="Electron">
  <img src="https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
</p>

<p align="center">
  English · <a href="README_zh.md">中文</a>
</p>

---

**LobsterAI** is an all-in-one personal assistant Agent developed by [NetEase Youdao](https://www.youdao.com/). It works around the clock to handle your everyday tasks — data analysis, making presentations, generating videos, writing documents, searching the web, sending emails, scheduling tasks, and more.

At its core is **Cowork mode** — it executes tools, manipulates files, and runs commands in a local or sandboxed environment, all under your supervision. You can also chat with agent via Telegram, Discord, DingTalk or Feishu (Lark) and get work done from your phone anytime, anywhere.

## Key Features

- **All-in-One Productivity Assistant** — Data analysis, PPT creation, video generation, document writing, web search, email — covers the full range of daily work
- **Local + Sandbox Execution** — Run tasks directly on your machine or in an OpenClaw sandbox environment
- **Built-in Skills** — Office document generation, web search, Playwright automation, Remotion video generation, and more
- **Windows Built-in Python Runtime** — Windows packages bundle a ready-to-use Python interpreter runtime; Python skill dependencies can be installed on demand
- **Scheduled Tasks** — Create recurring tasks via conversation or the GUI — daily news digests, inbox cleanup, periodic report generation, and more
- **Persistent Memory** — Automatically extracts user preferences and personal facts from conversations, remembers your habits across sessions, and gets smarter the more you use it
- **Mobile via IM** — Control your Agent remotely from your phone through Telegram, Discord, DingTalk, or Feishu
- **Permission Gating** — All tool invocations require explicit user approval before execution
- **Cross-Platform** — macOS (Intel + Apple Silicon), Windows, Linux desktop, plus mobile coverage via IM
- **Local Data** — SQLite storage keeps your chat history and configuration on your device

## How It Works

<p align="center">
  <img src="docs/res/architecture_en.png" alt="Architecture" width="500">
</p>

## Quick Start

### Prerequisites

- **Node.js** >= 24 < 25
- **npm**

### Install & Develop

```bash
# Clone the repository
git clone https://github.com/netease-youdao/LobsterAI.git
cd lobsterai

# Install dependencies
npm install

# Start development (Vite dev server + Electron with hot reload)
npm run electron:dev
```

The dev server runs at `http://localhost:5175` by default.

#### Develop with OpenClaw Agent Engine

LobsterAI can use [OpenClaw](https://github.com/openclaw/openclaw) as its agent engine.
The required OpenClaw version is pinned in `package.json` under `openclaw.version`.

```bash
# First run: automatically clones and builds OpenClaw (may take several minutes)
npm run electron:dev:openclaw

# Subsequent runs: skips build if the pinned version hasn't changed
npm run electron:dev:openclaw
```

By default, OpenClaw source is cloned/managed at `../openclaw` (relative to this repo). Override with:

```bash
OPENCLAW_SRC=/path/to/openclaw npm run electron:dev:openclaw
```

To force a rebuild even when the version hasn't changed:

```bash
OPENCLAW_FORCE_BUILD=1 npm run electron:dev:openclaw
```

To skip the automatic version checkout (e.g., when developing OpenClaw locally):

```bash
OPENCLAW_SKIP_ENSURE=1 npm run electron:dev:openclaw
```

### Production Build

```bash
# TypeScript compilation + Vite bundle
npm run build

# ESLint check
npm run lint
```

## Packaging & Distribution

Uses [electron-builder](https://www.electron.build/) to produce platform-specific installers. Output goes to `release/`.

```bash
# macOS (.dmg)
npm run dist:mac

# macOS - Intel only
npm run dist:mac:x64

# macOS - Apple Silicon only
npm run dist:mac:arm64

# macOS - Universal (both architectures)
npm run dist:mac:universal

# Windows (.exe NSIS installer)
npm run dist:win

# Linux (.AppImage & .deb)
npm run dist:linux
```

Desktop packaging (macOS / Windows / Linux) bundles a prebuilt OpenClaw runtime under `Resources/cfmind`.
The pinned OpenClaw version (`package.json` → `openclaw.version`) is automatically fetched and built during packaging — no manual setup needed.
The build is cached: if the runtime for the pinned version already exists locally, the build step is skipped automatically.

You can also build OpenClaw runtime manually:

```bash
# Build runtime for current host platform (auto-detect mac/win/linux + arch)
npm run openclaw:runtime:host

# Build explicit targets
npm run openclaw:runtime:mac-arm64
npm run openclaw:runtime:win-x64
npm run openclaw:runtime:linux-x64
```

Override OpenClaw source path with an environment variable when needed:

```bash
OPENCLAW_SRC=/path/to/openclaw npm run dist:win
```

Windows builds bundle a portable Python runtime under `resources/python-win` (included as installer resource `python-win`), so end users do not need to install Python manually.
The bundled runtime is interpreter-focused and does not preinstall LobsterAI skill Python packages; those can be installed at runtime on demand.
By default, packaging downloads the official Python embeddable runtime from python.org if no prebuilt archive is provided.
For offline/non-network builds, provide a prebuilt runtime archive explicitly.

Offline/runtime source options for packaging:
- `LOBSTERAI_PORTABLE_PYTHON_ARCHIVE`: Local prebuilt runtime archive path (recommended for offline CI/CD)
- `LOBSTERAI_PORTABLE_PYTHON_URL`: Download URL for the prebuilt runtime archive
- `LOBSTERAI_WINDOWS_EMBED_PYTHON_VERSION` / `LOBSTERAI_WINDOWS_EMBED_PYTHON_URL` / `LOBSTERAI_WINDOWS_GET_PIP_URL`: Optional overrides for Windows-host bootstrap sources

## Architecture

LobsterAI uses Electron's strict process isolation. All cross-process communication goes through IPC.

### Process Model

**Main Process** (`src/main/main.ts`):
- Window lifecycle management
- SQLite persistence
- CoworkRunner — Claude Agent SDK execution engine
- IM Gateways — DingTalk, Feishu, Telegram, Discord remote access
- 40+ IPC channel handlers
- Security: context isolation enabled, node integration disabled, sandbox enabled

**Preload Script** (`src/main/preload.ts`):
- Exposes `window.electron` API via `contextBridge`
- Includes `cowork` namespace for session management and stream events

**Renderer Process** (`src/renderer/`):
- React 18 + Redux Toolkit + Tailwind CSS
- All UI and business logic
- Communicates with main process exclusively through IPC

### Directory Structure

```
src/
├── main/                           # Electron main process
│   ├── main.ts                     # Entry point, IPC handlers
│   ├── preload.ts                  # Security bridge
│   ├── sqliteStore.ts              # SQLite storage
│   ├── coworkStore.ts              # Session/message CRUD
│   ├── skillManager.ts             # Skill management
│   ├── im/                         # IM gateways (DingTalk/Feishu/Telegram/Discord)
│   └── libs/
│       ├── coworkRunner.ts         # Agent SDK executor
│       └── coworkMemoryExtractor.ts # Memory extraction
│
├── renderer/                        # React frontend
│   ├── App.tsx                     # Root component
│   ├── types/                      # TypeScript definitions
│   ├── store/slices/               # Redux state slices
│   ├── services/                   # Business logic (API/IPC/i18n)
│   └── components/
│       ├── cowork/                 # Cowork UI components
│       ├── artifacts/              # Artifact renderers
│       ├── skills/                 # Skill management UI
│       ├── im/                     # IM integration UI
│       └── Settings.tsx            # Settings panel
│
SKILLs/                              # Skill definitions
├── skills.config.json              # Skill enable/disable and ordering
├── web-search/                     # Web search
├── docx/                           # Word document generation
├── xlsx/                           # Excel spreadsheets
├── pptx/                           # PowerPoint presentations
├── pdf/                            # PDF processing
├── remotion/                       # Video generation
├── playwright/                     # Web automation
└── ...                             # More skills
```

## Cowork System

Cowork is the core feature of LobsterAI — an AI working session system built on the Claude Agent SDK. Designed for productivity scenarios, it can autonomously complete complex tasks like data analysis, document generation, and information retrieval.

### Execution Modes

| Mode | Description |
|------|-------------|
| `auto` | Automatically selects based on context |
| `local` | Direct local execution, full speed |

### Stream Events

Cowork uses IPC events for real-time bidirectional communication:

- `message` — New message added to the session
- `messageUpdate` — Incremental streaming content update
- `permissionRequest` — Tool execution requires user approval
- `complete` — Session execution finished
- `error` — Execution error occurred

### Permission Control

All tool invocations involving file system access, terminal commands, or network requests require explicit user approval in the `CoworkPermissionModal`. Both single-use and session-level approvals are supported.

## Skills System

LobsterAI ships with 16 built-in skills covering productivity, creative, and automation scenarios, configured via `SKILLs/skills.config.json`:

| Skill | Function | Typical Use Case |
|-------|----------|-----------------|
| web-search | Web search | Information retrieval, research |
| docx | Word document generation | Reports, proposals |
| xlsx | Excel spreadsheet generation | Data analysis, dashboards |
| pptx | PowerPoint creation | Presentations, business reviews |
| pdf | PDF processing | Document parsing, format conversion |
| remotion | Video generation (Remotion) | Promo videos, data visualization animations |
| playwright | Web automation | Browser tasks, automated testing |
| canvas-design | Canvas drawing and design | Posters, chart design |
| frontend-design | Frontend UI design | Prototyping, page design |
| develop-web-game | Web game development | Quick game prototypes |
| scheduled-task | Scheduled tasks | Periodic automated workflows |
| weather | Weather queries | Weather information |
| local-tools | Local system tools | File management, system operations |
| create-plan | Plan authoring | Project planning, task breakdown |
| skill-creator | Custom skill creation | Extend new capabilities |
| imap-smtp-email | Email send/receive | Email processing, auto-replies |

Custom skills can be created via `skill-creator` and hot-loaded at runtime.

## Scheduled Tasks

LobsterAI supports scheduled tasks that let the Agent automatically execute recurring work on a set schedule.

### How to Create

- **Conversational** — Tell the Agent in natural language (e.g., "collect tech news for me every morning at 9 AM"), and it will create the scheduled task automatically
- **GUI** — Add tasks manually in the Scheduled Tasks management panel with a visual interface for configuring timing and task content

### Typical Scenarios

| Scenario | Example |
|----------|---------|
| News Collection | Automatically gather industry news and generate a summary every morning |
| Inbox Cleanup | Periodically check your inbox, categorize emails, and summarize important ones |
| Data Reports | Generate a weekly business data analysis report |
| Content Monitoring | Regularly check specific websites for changes and send notifications |
| Work Reminders | Generate to-do lists or meeting notes on a schedule |

Scheduled tasks are powered by Cron expressions, supporting minute, hourly, daily, weekly, and monthly intervals. When a task fires, it automatically starts a Cowork session. Results can be viewed on the desktop or pushed to your phone via IM.

## IM Integration — Mobile Remote Control

LobsterAI can bridge the Agent to multiple IM platforms. Send a message from your phone via IM to remotely trigger the desktop Agent — command your personal assistant anytime, anywhere.

| Platform | Protocol | Description |
|----------|----------|-------------|
| DingTalk | DingTalk Stream | Enterprise robot bidirectional communication |
| Feishu | Lark SDK | Feishu app robot |
| Telegram | grammY | Bot API integration |
| Discord | discord.js | Discord bot integration |
| NetEase IM | node-nim V2 SDK | NetEase IM P2P messaging |
| NetEase Bee | node-nim V2 SDK | NetEase Bee Personal Digital Assistant |

Configure the corresponding platform Token/Secret in the Settings panel to enable. Once set up, you can send instructions directly to the Agent from your phone IM (e.g., "analyze this dataset", "make a weekly summary PPT"), and the Agent will execute on the desktop and return results.

## Persistent Memory

LobsterAI has a built-in memory system that remembers your personal information and preferences across sessions, making the Agent more helpful the more you use it.

### How Memories Are Captured

- **Automatic Extraction** — During conversations, the system automatically identifies and stores your personal details (name, occupation), preferences (language, format, style), and personal facts (pets, tools you use) — no manual effort required
- **Explicit Requests** — Tell the Agent directly, e.g., "remember that I prefer Markdown format" or "note down that my project is called LobsterAI," and it will store the memory with higher confidence
- **Manual Management** — Add, edit, or delete memory entries in the Memory management panel within Settings

### How It Works

After each conversation turn, the memory extractor analyzes the dialogue:

| Extraction Type | Example | Confidence |
|----------------|---------|------------|
| Personal Profile | "My name is Alex", "I'm a product manager" | High |
| Personal Ownership | "I have a cat", "I use a MacBook" | High |
| Personal Preferences | "I like a concise style", "I prefer English replies" | Medium-High |
| Assistant Preferences | "Don't use emojis in replies", "Write code in TypeScript" | Medium-High |
| Explicit Requests | "Remember this", "Please note that down" | Highest |

Extracted memories are automatically dedup
... [TRUNCATED]
```

### File: AGENTS.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Development Commands

```bash
# Development - starts Vite dev server (port 5175) + Electron app with hot reload
npm run electron:dev

# Development with OpenClaw engine (clones/builds OpenClaw on first run)
npm run electron:dev:openclaw

# Build production bundle (TypeScript + Vite)
npm run build

# Lint with ESLint
npm run lint

# Run memory extractor tests (Node.js built-in test runner)
npm run test:memory

# Compile Electron main process only
npm run compile:electron

# Package for distribution (platform-specific)
npm run dist:mac        # macOS (.dmg)
npm run dist:win        # Windows (.exe)
npm run dist:linux      # Linux (.AppImage)

# Build OpenClaw runtime manually
npm run openclaw:runtime:host   # current platform
```

**Requirements**: Node.js >=24 <25. Windows builds require PortableGit (see README.md for setup).

**OpenClaw env vars**: `OPENCLAW_SRC` (default `../openclaw`), `OPENCLAW_FORCE_BUILD=1` (force rebuild), `OPENCLAW_SKIP_ENSURE=1` (skip version checkout).

## Architecture Overview

LobsterAI is an Electron + React desktop application with two primary modes:
1. **Cowork Mode** - AI-assisted coding sessions using Claude Agent SDK with tool execution
2. **Artifacts System** - Rich preview of code outputs (HTML, SVG, React, Mermaid)

Uses strict process isolation with IPC communication.

### Authentication Flow

1. **登录：** 打开系统浏览器 → Portal 登录页 → URS 登录成功 → deep link `lobsterai://auth/callback?code=<authCode>`
2. **换取令牌：** `POST /api/auth/exchange` 消费一次性 authCode → 返回 `accessToken`(2h) + `refreshToken`(30d)
3. **持久化：** SQLite kv store `auth_tokens` 存储双 token，应用重启后自动恢复登录态
4. **请求认证：** `fetchWithAuth()` 在每个 API 请求附加 `Authorization: Bearer <accessToken>`
5. **被动刷新：** 收到 HTTP 401 → 使用 refreshToken 调用 `POST /api/auth/refresh` → 获取新 accessToken → 重试原请求
6. **主动刷新：** 定期检查 accessToken 距 exp < 5 分钟 → 后台静默刷新，避免请求失败
7. **滚动续期：** 每次 refresh 签发新 refreshToken（新 30 天有效期），连续使用不掉线
8. **退出条件：** 连续 30 天不使用（refreshToken 过期）→ 清除本地 token → 用户需重新登录

**关键文件：**
- Token 存储与请求：`src/renderer/services/api.ts`（`fetchWithAuth()`、token 管理）
- 登录流程：`src/main/main.ts`（deep link 处理 `lobsterai://` 协议）
- 持久化：`src/main/sqliteStore.ts`（kv 表存储 `auth_tokens`）

### Process Model

**Main Process** (`src/main/main.ts`):
- Window lifecycle management
- SQLite storage via `sql.js` (`src/main/sqliteStore.ts`)
- Agent engine routing (`src/main/libs/agentEngine/coworkEngineRouter.ts`) - dispatches to `claudeRuntimeAdapter.ts` (built-in) or `openclawRuntimeAdapter.ts` (OpenClaw)
- IM gateways (`src/main/im/`) - DingTalk, Feishu, Telegram, Discord, NetEase IM
- Skill management (`src/main/skillManager.ts`)
- IPC handlers for store, cowork, and API operations (40+ channels)
- Security: context isolation enabled, node integration disabled, sandbox enabled

**Preload Script** (`src/main/preload.ts`):
- Exposes `window.electron` API via `contextBridge`
- Includes `cowork` namespace for session management and streaming events

**Renderer Process** (React in `src/renderer/`):
- All UI and business logic
- Communicates with main process exclusively through IPC

### Key Directories

```
src/main/
├── main.ts              # Entry point, IPC handlers
├── sqliteStore.ts       # SQLite database (kv + cowork tables)
├── coworkStore.ts       # Cowork session/message CRUD operations
├── skillManager.ts      # Skill loading and management
├── im/                  # IM gateway integrations (DingTalk/Feishu/Telegram/Discord)
└── libs/
    ├── agentEngine/
    │   ├── coworkEngineRouter.ts    # Routes to built-in or OpenClaw runtime
    │   ├── claudeRuntimeAdapter.ts  # Built-in Claude Agent SDK adapter
    │   └── openclawRuntimeAdapter.ts # OpenClaw gateway adapter
    ├── coworkRunner.ts          # Claude Agent SDK execution engine
    ├── claudeSdk.ts             # SDK loader utilities
    ├── openclawEngineManager.ts # OpenClaw runtime lifecycle (install/start/status)
    ├── openclawConfigSync.ts    # Syncs cowork config → OpenClaw config files
    ├── coworkMemoryExtractor.ts # Extracts memory changes from conversations
    └── coworkMemoryJudge.ts     # Validates memory candidates with scoring/LLM

src/renderer/
├── types/cowork.ts      # Cowork type definitions
├── store/slices/
│   ├── coworkSlice.ts   # Cowork sessions and streaming state
│   └── artifactSlice.ts # Artifacts state
├── services/
│   ├── cowork.ts        # Cowork service (IPC wrapper, Redux integration)
│   ├── api.ts           # LLM API with SSE streaming
│   └── artifactParser.ts # Artifact detection and parsing
├── components/
│   ├── cowork/          # Cowork UI components
│   │   ├── CoworkView.tsx          # Main cowork interface
│   │   ├── CoworkSessionList.tsx   # Session sidebar
│   │   ├── CoworkSessionDetail.tsx # Message display
│   │   └── CoworkPermissionModal.tsx # Tool permission UI
│   └── artifacts/       # Artifact renderers

SKILLs/                  # Custom skill definitions for cowork sessions
├── skills.config.json   # Skill enable/order configuration
├── docx/                # Word document generation skill
├── xlsx/                # Excel skill
├── pptx/                # PowerPoint skill
└── ...
```

### Data Flow

1. **Initialization**: `src/renderer/App.tsx` → `coworkService.init()` → loads config/sessions via IPC → sets up stream listeners
2. **Cowork Session**: User sends prompt → `coworkService.startSession()` → IPC to main → `CoworkRunner.startSession()` → Claude Agent SDK execution → streaming events back to renderer via IPC → Redux updates
3. **Tool Permissions**: Claude requests tool use → `CoworkRunner` emits `permissionRequest` → UI shows `CoworkPermissionModal` → user approves/denies → result sent back to SDK
4. **Persistence**: Cowork sessions stored in SQLite (`cowork_sessions`, `cowork_messages` tables)

### Cowork System

The Cowork feature provides AI-assisted coding sessions:

**Execution Modes** (`CoworkExecutionMode`):
- `auto` - Automatically choose based on context (OpenClaw: `sandbox.mode=non-main`)
- `local` - Run tools directly on the local machine (OpenClaw: `sandbox.mode=off`)
- `sandbox` - Full sandbox isolation (OpenClaw: `sandbox.mode=all`)

**Agent Engines** (configured via `agentEngine` in cowork config):
- `yd_cowork` - Built-in Claude Agent SDK runner (`claudeRuntimeAdapter.ts`)
- `openclaw` - OpenClaw gateway (`openclawRuntimeAdapter.ts`); requires the bundled OpenClaw runtime to be running. Engine lifecycle managed by `OpenClawEngineManager` with states: `not_installed → ready → starting → running | error`

Both engines expose identical stream events through `CoworkEngineRouter`, so the renderer is engine-agnostic. Engine-specific IPC: `openclaw:engine:*` channels manage runtime lifecycle separately from `cowork:*` session channels.

**Memory System**: Automatically extracts and manages user memories from conversations:
- `coworkMemoryExtractor.ts` - Detects explicit remember/forget commands (Chinese/English) and implicitly extracts personal facts using signal patterns (profile, preferences, ownership). Uses guard levels (`strict`/`standard`/`relaxed`) with confidence thresholds.
- `coworkMemoryJudge.ts` - Validates memory candidates with rule-based scoring and optional LLM secondary judgment for borderline cases. Includes TTL-based caching for LLM results.

**Stream Events** (IPC from main to renderer):
- `message` - New message added to session
- `messageUpdate` - Streaming content update for existing message
- `permissionRequest` - Tool needs user approval
- `complete` - Session execution finished
- `error` - Session encountered an error

**Key IPC Channels**:
- `cowork:startSession`, `cowork:continueSession`, `cowork:stopSession`
- `cowork:getSession`, `cowork:listSessions`, `cowork:deleteSession`
- `cowork:respondToPermission`, `cowork:getConfig`, `cowork:setConfig`

### Key Patterns

- **Streaming responses**: `apiService.chat()` uses SSE with `onProgress` callback for real-time message updates
- **Cowork streaming**: Uses IPC event listeners (`onStreamMessage`, `onStreamMessageUpdate`, etc.) for bidirectional communication
- **Markdown rendering**: `react-markdown` with `remark-gfm`, `remark-math`, `rehype-katex` for GitHub markdown and LaTeX
- **Theme system**: Class-based Tailwind dark mode, applies `dark` class to `<html>` element
- **i18n**: Simple key-value translation in `services/i18n.ts`, supports Chinese (default) and English. Language auto-detected from system locale on first run.
- **Path alias**: `@` maps to `src/renderer/` in Vite config for imports.
- **Skills**: Custom skill definitions in `SKILLs/` directory, configured via `skills.config.json`

### Artifacts System

The Artifacts feature provides rich preview of code outputs similar to Claude's artifacts:

**Supported Types**:
- `html` - Full HTML pages rendered in sandboxed iframe
- `svg` - SVG graphics with DOMPurify sanitization and zoom controls
- `mermaid` - Flowcharts, sequence diagrams, class diagrams via Mermaid.js
- `react` - React/JSX components compiled with Babel in isolated iframe
- `code` - Syntax highlighted code with line numbers

**Detection Methods**:
1. Explicit markers: ` ```artifact:html title="My Page" `
2. Heuristic detection: Analyzes code block language and content patterns

**UI Components**:
- Right-side panel (300-800px resizable width)
- Header with type icon, title, copy/download/close buttons
- Artifact badges in messages to switch between artifacts

**Security**:
- HTML: `sandbox="allow-scripts"` with no `allow-same-origin`
- SVG: DOMPurify removes all script content
- React: Completely isolated iframe with no network access
- Mermaid: `securityLevel: 'strict'` configuration

### Configuration

- App config stored in SQLite `kv` table
- Cowork config stored in `cowork_config` table (workingDirectory, systemPrompt, executionMode, **agentEngine**)
- Cowork sessions and messages stored in `cowork_sessions` and `cowork_messages` tables
- Scheduled tasks stored in `scheduled_tasks` table (cron expressions, task content)
- Database file: `lobsterai.sqlite` in user data directory
- OpenClaw pinned version declared in `package.json` under `"openclaw": { "version": "...", "repo": "..." }`; update the version field and re-run to upgrade

### TypeScript Configuration

- `tsconfig.json`: React/renderer code (ES2020, ESNext modules)
- `electron-tsconfig.json`: Electron main process (CommonJS output to `dist-electron/`)

### Key Dependencies

- `@anthropic-ai/claude-agent-sdk` - Claude Agent SDK for cowork sessions
- `sql.js` - SQLite database for persistence
- `react-markdown`, `remark-gfm`, `rehype-katex` - Markdown rendering with math support
- `mermaid` - Diagram rendering
- `dompurify` - SVG/HTML sanitization

## Coding Style & Naming Conventions

- Use TypeScript, functional React components, and Hooks; keep logic in `src/renderer/services/` when it is not UI-specific.
- Match existing formatting: 2-space indentation, single quotes, and semicolons.
- Naming: `PascalCase` for components (e.g., `Chat.tsx`), `camelCase` for functions/vars, and `*Slice.ts` for Redux slices.
- Tailwind CSS is the primary styling approach; prefer utility classes over bespoke CSS.

## String Literal Constants

**Never use bare string literals** for values that act as discriminants, status codes, IPC channel names, mode selectors, or any string compared/switched against in multiple places. Instead, define a centralized `as const` object and derive the type from it.

### Pattern

```typescript
// In constants.ts (one per module, e.g. src/scheduled-task/constants.ts)
export const SessionTarget = {
  Main: 'main',
  Isolated: 'isolated',
} as const;
export type SessionTarget = typeof SessionTarget[keyof typeof SessionTarget];
```

### Rules

1. **One source of truth per module.** Each module that owns a set of string constants must have a `constants.ts` file. Consumer modules import both the value object and the type.
2. **Value construction and comparison must use constants.** Write `SessionTarget.Main`, not `'main'`. This applies to source files, test files, and any other TypeScript that references these values.
3. **Discriminant `kind` fields in interface definitions remain literal.** The `kind: 'at'` in `interface ScheduleAt` defines the discriminated union shape and must stay as a literal. The constant should match this value; consumers use the constant object for comparisons and construction.
4. **IPC channel names must be constants.** All `ipcMain.handle()` registrations and `ipcRenderer.invoke()` calls must reference an `IpcChannel` constant, never a bare string.
5. **Tests use constants too.** Test files must import and use the same constants — this is the primary defense against "modified the constant but forgot to update the test" drift.

### What NOT to constantize

- Platform-specific identifiers passed through from external sources (e.g., `'telegram'`, `'feishu'` as IM platform names from user config).
- One-off strings used in a single location with no comparison logic (e.g., error messages, log tags).
- CSS class names, HTML attributes, and other UI-layer strings managed by Tailwind/React.

### Existing reference

`src/scheduled-task/constants.ts` is the canonical example of this pattern, covering schedule kinds, payload kinds, delivery modes, session targets, wake modes, origin kinds, binding kinds, task status, IPC channels, and migration keys.

## Logging Guidelines

The main process uses `electron-log` via `src/main/logger.ts`, which intercepts all `console.*` calls and writes them to daily-rotated log files. **No additional logging library is needed** — use the standard `console` API everywhere in `src/main/`.

### Log Levels

Choose the level that matches the **significance** of the event:

| Level | API | When to use |
|-------|-----|-------------|
| Error | `console.error` | Unrecoverable failures that need investigation — caught exceptions, broken invariants, data corruption |
| Warn | `console.warn` | Unexpected but recoverable situations — missing optional config, fallback behavior, degraded service |
| Info | `console.log` | Key lifecycle events worth keeping in production logs — service started/stopped, connection established/lost, session created/destroyed, configuration changed |
| Debug | `console.debug` | Development-time detail useful only when actively debugging — intermediate state, request/response payloads, loop iterations, sync cursors |

### Message Format

Log messages must read as **plain English sentences**, not as variable dumps.

**Tag**: Every message starts with a bracketed module tag: `[ModuleName]`.

```typescript
// Good — describes what happened in natural language
console.log('[ChannelSync] discovered 3 new channel sessions, notified 2 windows');
console.warn('[ChannelSync] session list returned unexpected type, skipping');
console.error('[ChannelSync] polling failed:', error);


... [TRUNCATED]
```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Development Commands

```bash
# Development - starts Vite dev server (port 5175) + Electron app with hot reload
npm run electron:dev

# Development with OpenClaw engine (clones/builds OpenClaw on first run)
npm run electron:dev:openclaw

# Build production bundle (TypeScript + Vite)
npm run build

# Lint with ESLint
npm run lint

# Run memory extractor tests (Node.js built-in test runner)
npm run test:memory

# Compile Electron main process only
npm run compile:electron

# Package for distribution (platform-specific)
npm run dist:mac        # macOS (.dmg)
npm run dist:win        # Windows (.exe)
npm run dist:linux      # Linux (.AppImage)

# Build OpenClaw runtime manually
npm run openclaw:runtime:host   # current platform
```

**Requirements**: Node.js >=24 <25. Windows builds require PortableGit (see README.md for setup).

**OpenClaw env vars**: `OPENCLAW_SRC` (default `../openclaw`), `OPENCLAW_FORCE_BUILD=1` (force rebuild), `OPENCLAW_SKIP_ENSURE=1` (skip version checkout).

## Architecture Overview

LobsterAI is an Electron + React desktop application with two primary modes:
1. **Cowork Mode** - AI-assisted coding sessions using Claude Agent SDK with tool execution
2. **Artifacts System** - Rich preview of code outputs (HTML, SVG, React, Mermaid)

Uses strict process isolation with IPC communication.

### Authentication Flow

1. **登录：** 打开系统浏览器 → Portal 登录页 → URS 登录成功 → deep link `lobsterai://auth/callback?code=<authCode>`
2. **换取令牌：** `POST /api/auth/exchange` 消费一次性 authCode → 返回 `accessToken`(2h) + `refreshToken`(30d)
3. **持久化：** SQLite kv store `auth_tokens` 存储双 token，应用重启后自动恢复登录态
4. **请求认证：** `fetchWithAuth()` 在每个 API 请求附加 `Authorization: Bearer <accessToken>`
5. **被动刷新：** 收到 HTTP 401 → 使用 refreshToken 调用 `POST /api/auth/refresh` → 获取新 accessToken → 重试原请求
6. **主动刷新：** 定期检查 accessToken 距 exp < 5 分钟 → 后台静默刷新，避免请求失败
7. **滚动续期：** 每次 refresh 签发新 refreshToken（新 30 天有效期），连续使用不掉线
8. **退出条件：** 连续 30 天不使用（refreshToken 过期）→ 清除本地 token → 用户需重新登录

**关键文件：**
- Token 存储与请求：`src/renderer/services/api.ts`（`fetchWithAuth()`、token 管理）
- 登录流程：`src/main/main.ts`（deep link 处理 `lobsterai://` 协议）
- 持久化：`src/main/sqliteStore.ts`（kv 表存储 `auth_tokens`）

### Process Model

**Main Process** (`src/main/main.ts`):
- Window lifecycle management
- SQLite storage via `sql.js` (`src/main/sqliteStore.ts`)
- Agent engine routing (`src/main/libs/agentEngine/coworkEngineRouter.ts`) - dispatches to `claudeRuntimeAdapter.ts` (built-in) or `openclawRuntimeAdapter.ts` (OpenClaw)
- IM gateways (`src/main/im/`) - DingTalk, Feishu, Telegram, Discord, NetEase IM
- Skill management (`src/main/skillManager.ts`)
- IPC handlers for store, cowork, and API operations (40+ channels)
- Security: context isolation enabled, node integration disabled, sandbox enabled

**Preload Script** (`src/main/preload.ts`):
- Exposes `window.electron` API via `contextBridge`
- Includes `cowork` namespace for session management and streaming events

**Renderer Process** (React in `src/renderer/`):
- All UI and business logic
- Communicates with main process exclusively through IPC

### Key Directories

```
src/main/
├── main.ts              # Entry point, IPC handlers
├── sqliteStore.ts       # SQLite database (kv + cowork tables)
├── coworkStore.ts       # Cowork session/message CRUD operations
├── skillManager.ts      # Skill loading and management
├── im/                  # IM gateway integrations (DingTalk/Feishu/Telegram/Discord)
└── libs/
    ├── agentEngine/
    │   ├── coworkEngineRouter.ts    # Routes to built-in or OpenClaw runtime
    │   ├── claudeRuntimeAdapter.ts  # Built-in Claude Agent SDK adapter
    │   └── openclawRuntimeAdapter.ts # OpenClaw gateway adapter
    ├── coworkRunner.ts          # Claude Agent SDK execution engine
    ├── claudeSdk.ts             # SDK loader utilities
    ├── openclawEngineManager.ts # OpenClaw runtime lifecycle (install/start/status)
    ├── openclawConfigSync.ts    # Syncs cowork config → OpenClaw config files
    ├── coworkMemoryExtractor.ts # Extracts memory changes from conversations
    └── coworkMemoryJudge.ts     # Validates memory candidates with scoring/LLM

src/renderer/
├── types/cowork.ts      # Cowork type definitions
├── store/slices/
│   ├── coworkSlice.ts   # Cowork sessions and streaming state
│   └── artifactSlice.ts # Artifacts state
├── services/
│   ├── cowork.ts        # Cowork service (IPC wrapper, Redux integration)
│   ├── api.ts           # LLM API with SSE streaming
│   └── artifactParser.ts # Artifact detection and parsing
├── components/
│   ├── cowork/          # Cowork UI components
│   │   ├── CoworkView.tsx          # Main cowork interface
│   │   ├── CoworkSessionList.tsx   # Session sidebar
│   │   ├── CoworkSessionDetail.tsx # Message display
│   │   └── CoworkPermissionModal.tsx # Tool permission UI
│   └── artifacts/       # Artifact renderers

SKILLs/                  # Custom skill definitions for cowork sessions
├── skills.config.json   # Skill enable/order configuration
├── docx/                # Word document generation skill
├── xlsx/                # Excel skill
├── pptx/                # PowerPoint skill
└── ...
```

### Data Flow

1. **Initialization**: `src/renderer/App.tsx` → `coworkService.init()` → loads config/sessions via IPC → sets up stream listeners
2. **Cowork Session**: User sends prompt → `coworkService.startSession()` → IPC to main → `CoworkRunner.startSession()` → Claude Agent SDK execution → streaming events back to renderer via IPC → Redux updates
3. **Tool Permissions**: Claude requests tool use → `CoworkRunner` emits `permissionRequest` → UI shows `CoworkPermissionModal` → user approves/denies → result sent back to SDK
4. **Persistence**: Cowork sessions stored in SQLite (`cowork_sessions`, `cowork_messages` tables)

### Cowork System

The Cowork feature provides AI-assisted coding sessions:

**Execution Modes** (`CoworkExecutionMode`):
- `auto` - Automatically choose based on context (OpenClaw: `sandbox.mode=non-main`)
- `local` - Run tools directly on the local machine (OpenClaw: `sandbox.mode=off`)
- `sandbox` - Full sandbox isolation (OpenClaw: `sandbox.mode=all`)

**Agent Engines** (configured via `agentEngine` in cowork config):
- `yd_cowork` - Built-in Claude Agent SDK runner (`claudeRuntimeAdapter.ts`)
- `openclaw` - OpenClaw gateway (`openclawRuntimeAdapter.ts`); requires the bundled OpenClaw runtime to be running. Engine lifecycle managed by `OpenClawEngineManager` with states: `not_installed → ready → starting → running | error`

Both engines expose identical stream events through `CoworkEngineRouter`, so the renderer is engine-agnostic. Engine-specific IPC: `openclaw:engine:*` channels manage runtime lifecycle separately from `cowork:*` session channels.

**Memory System**: Automatically extracts and manages user memories from conversations:
- `coworkMemoryExtractor.ts` - Detects explicit remember/forget commands (Chinese/English) and implicitly extracts personal facts using signal patterns (profile, preferences, ownership). Uses guard levels (`strict`/`standard`/`relaxed`) with confidence thresholds.
- `coworkMemoryJudge.ts` - Validates memory candidates with rule-based scoring and optional LLM secondary judgment for borderline cases. Includes TTL-based caching for LLM results.

**Stream Events** (IPC from main to renderer):
- `message` - New message added to session
- `messageUpdate` - Streaming content update for existing message
- `permissionRequest` - Tool needs user approval
- `complete` - Session execution finished
- `error` - Session encountered an error

**Key IPC Channels**:
- `cowork:startSession`, `cowork:continueSession`, `cowork:stopSession`
- `cowork:getSession`, `cowork:listSessions`, `cowork:deleteSession`
- `cowork:respondToPermission`, `cowork:getConfig`, `cowork:setConfig`

### Key Patterns

- **Streaming responses**: `apiService.chat()` uses SSE with `onProgress` callback for real-time message updates
- **Cowork streaming**: Uses IPC event listeners (`onStreamMessage`, `onStreamMessageUpdate`, etc.) for bidirectional communication
- **Markdown rendering**: `react-markdown` with `remark-gfm`, `remark-math`, `rehype-katex` for GitHub markdown and LaTeX
- **Theme system**: Class-based Tailwind dark mode, applies `dark` class to `<html>` element
- **i18n**: Simple key-value translation in `services/i18n.ts`, supports Chinese (default) and English. Language auto-detected from system locale on first run.
- **Path alias**: `@` maps to `src/renderer/` in Vite config for imports.
- **Skills**: Custom skill definitions in `SKILLs/` directory, configured via `skills.config.json`

### Artifacts System

The Artifacts feature provides rich preview of code outputs similar to Claude's artifacts:

**Supported Types**:
- `html` - Full HTML pages rendered in sandboxed iframe
- `svg` - SVG graphics with DOMPurify sanitization and zoom controls
- `mermaid` - Flowcharts, sequence diagrams, class diagrams via Mermaid.js
- `react` - React/JSX components compiled with Babel in isolated iframe
- `code` - Syntax highlighted code with line numbers

**Detection Methods**:
1. Explicit markers: ` ```artifact:html title="My Page" `
2. Heuristic detection: Analyzes code block language and content patterns

**UI Components**:
- Right-side panel (300-800px resizable width)
- Header with type icon, title, copy/download/close buttons
- Artifact badges in messages to switch between artifacts

**Security**:
- HTML: `sandbox="allow-scripts"` with no `allow-same-origin`
- SVG: DOMPurify removes all script content
- React: Completely isolated iframe with no network access
- Mermaid: `securityLevel: 'strict'` configuration

### Configuration

- App config stored in SQLite `kv` table
- Cowork config stored in `cowork_config` table (workingDirectory, systemPrompt, executionMode, **agentEngine**)
- Cowork sessions and messages stored in `cowork_sessions` and `cowork_messages` tables
- Scheduled tasks stored in `scheduled_tasks` table (cron expressions, task content)
- Database file: `lobsterai.sqlite` in user data directory
- OpenClaw pinned version declared in `package.json` under `"openclaw": { "version": "...", "repo": "..." }`; update the version field and re-run to upgrade

### TypeScript Configuration

- `tsconfig.json`: React/renderer code (ES2020, ESNext modules)
- `electron-tsconfig.json`: Electron main process (CommonJS output to `dist-electron/`)

### Key Dependencies

- `@anthropic-ai/claude-agent-sdk` - Claude Agent SDK for cowork sessions
- `sql.js` - SQLite database for persistence
- `react-markdown`, `remark-gfm`, `rehype-katex` - Markdown rendering with math support
- `mermaid` - Diagram rendering
- `dompurify` - SVG/HTML sanitization

## Coding Style & Naming Conventions

- Use TypeScript, functional React components, and Hooks; keep logic in `src/renderer/services/` when it is not UI-specific.
- Match existing formatting: 2-space indentation, single quotes, and semicolons.
- Naming: `PascalCase` for components (e.g., `Chat.tsx`), `camelCase` for functions/vars, and `*Slice.ts` for Redux slices.
- Tailwind CSS is the primary styling approach; prefer utility classes over bespoke CSS.

## String Literal Constants

**Never use bare string literals** for values that act as discriminants, status codes, IPC channel names, mode selectors, or any string compared/switched against in multiple places. Instead, define a centralized `as const` object and derive the type from it.

### Pattern

```typescript
// In constants.ts (one per module, e.g. src/scheduled-task/constants.ts)
export const SessionTarget = {
  Main: 'main',
  Isolated: 'isolated',
} as const;
export type SessionTarget = typeof SessionTarget[keyof typeof SessionTarget];
```

### Rules

1. **One source of truth per module.** Each module that owns a set of string constants must have a `constants.ts` file. Consumer modules import both the value object and the type.
2. **Value construction and comparison must use constants.** Write `SessionTarget.Main`, not `'main'`. This applies to source files, test files, and any other TypeScript that references these values.
3. **Discriminant `kind` fields in interface definitions remain literal.** The `kind: 'at'` in `interface ScheduleAt` defines the discriminated union shape and must stay as a literal. The constant should match this value; consumers use the constant object for comparisons and construction.
4. **IPC channel names must be constants.** All `ipcMain.handle()` registrations and `ipcRenderer.invoke()` calls must reference an `IpcChannel` constant, never a bare string.
5. **Tests use constants too.** Test files must import and use the same constants — this is the primary defense against "modified the constant but forgot to update the test" drift.

### What NOT to constantize

- Platform-specific identifiers passed through from external sources (e.g., `'telegram'`, `'feishu'` as IM platform names from user config).
- One-off strings used in a single location with no comparison logic (e.g., error messages, log tags).
- CSS class names, HTML attributes, and other UI-layer strings managed by Tailwind/React.

### Existing reference

`src/scheduled-task/constants.ts` is the canonical example of this pattern, covering schedule kinds, payload kinds, delivery modes, session targets, wake modes, origin kinds, binding kinds, task status, IPC channels, and migration keys.

## Logging Guidelines

The main process uses `electron-log` via `src/main/logger.ts`, which intercepts all `console.*` calls and writes them to daily-rotated log files. **No additional logging library is needed** — use the standard `console` API everywhere in `src/main/`.

### Log Levels

Choose the level that matches the **significance** of the event:

| Level | API | When to use |
|-------|-----|-------------|
| Error | `console.error` | Unrecoverable failures that need investigation — caught exceptions, broken invariants, data corruption |
| Warn | `console.warn` | Unexpected but recoverable situations — missing optional config, fallback behavior, degraded service |
| Info | `console.log` | Key lifecycle events worth keeping in production logs — service started/stopped, connection established/lost, session created/destroyed, configuration changed |
| Debug | `console.debug` | Development-time detail useful only when actively debugging — intermediate state, request/response payloads, loop iterations, sync cursors |

### Message Format

Log messages must read as **plain English sentences**, not as variable dumps.

**Tag**: Every message starts with a bracketed module tag: `[ModuleName]`.

```typescript
// Good — describes what happened in natural language
console.log('[ChannelSync] discovered 3 new channel sessions, notified 2 windows');
console.warn('[ChannelSync] session list returned unexpected type, skipping');
console.error('[ChannelSync] polling failed:', error);


... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
