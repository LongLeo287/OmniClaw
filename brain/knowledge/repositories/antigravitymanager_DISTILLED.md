---
id: repo-fetched-antigravitymanager-050348
type: knowledge
owner: OA
registered_at: 2026-04-05T03:26:07.340531
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_AntigravityManager_050348

## Assimilation Report
Auto-cloned repository: FETCHED_AntigravityManager_050348

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="docs/assets/logo.png" alt="Antigravity Manager" width="128" height="128" />
</p>

<h1 align="center">Antigravity Manager</h1>

<p align="center">
  <strong>🚀 Professional multi-account manager for Google Gemini & Claude AI</strong>
</p>

<p align="center">
  English | <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/Draculabo/AntigravityManager/actions/workflows/testing.yaml">
    <img src="https://github.com/Draculabo/AntigravityManager/actions/workflows/testing.yaml/badge.svg" alt="Tests" />
  </a>
  <a href="https://github.com/Draculabo/AntigravityManager/actions/workflows/lint.yaml">
    <img src="https://github.com/Draculabo/AntigravityManager/actions/workflows/lint.yaml/badge.svg" alt="Lint" />
  </a>
  <a href="https://github.com/Draculabo/AntigravityManager/releases">
    <img src="https://img.shields.io/github/v/release/Draculabo/AntigravityManager?style=flat-square" alt="Release" />
  </a>
  <a href="https://github.com/Draculabo/AntigravityManager/releases">
    <img src="https://img.shields.io/github/downloads/Draculabo/AntigravityManager/total?style=flat-square&color=blue" alt="Downloads" />
  </a>
  <a href="https://github.com/Draculabo/AntigravityManager/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Draculabo/AntigravityManager?style=flat-square" alt="License" />
  </a>
  <a href="https://github.com/Draculabo/AntigravityManager/stargazers">
    <img src="https://img.shields.io/github/stars/Draculabo/AntigravityManager?style=flat-square" alt="Stars" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Electron-191970?style=for-the-badge&logo=Electron&logoColor=white" alt="Electron" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="TailwindCSS" />
</p>

---

## 📖 Table of Contents

- [Why Antigravity Manager?](#-why-antigravity-manager)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Quick Start](#-quick-start)
- [Tech Stack](#️-tech-stack)
- [Development](#-development)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Why Antigravity Manager?

When using Antigravity IDE, have you ever encountered these problems?

- 😫 Single account quota runs out quickly, requiring frequent manual switching
- 🔄 Managing multiple Google/Claude accounts is cumbersome
- 📊 Don't know how much quota is left on the current account
- ⏰ Worried about missing quota reset times
- 🔌 Need a reliable local API proxy for development tools

**Antigravity Manager** is here to solve these problems! It's a professional Electron desktop app that helps you:

- ✅ **Unlimited Account Pool** - Add any number of Google Gemini / Claude accounts
- ✅ **Smart Auto-Switching** - Automatically switch to the next available account when quota is low or rate-limited
- ✅ **Real-time Monitoring** - Visualize quota usage for all accounts
- ✅ **Local API Proxy** - Built-in OpenAI/Anthropic compatible proxy server
- ✅ **Secure Encryption** - AES-256-GCM encryption for sensitive data

---

## 🎯 Features

<table>
  <tr>
    <td width="50%">
      <h3>☁️ Cloud Account Pool</h3>
      <ul>
        <li>Add unlimited Google Gemini / Claude accounts via OAuth</li>
        <li>Display avatar, email, status, and last used time</li>
        <li>Real-time status monitoring (Active, Rate Limited, Expired)</li>
      </ul>
    </td>
    <td width="50%">
      <h3>📊 Real-time Quota Monitoring</h3>
      <ul>
        <li>Multi-model support: gemini-pro, claude-3-5-sonnet, etc.</li>
        <li>Visual progress bars with color indicators</li>
        <li>Auto & manual refresh capabilities</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🔄 Intelligent Auto-Switching</h3>
      <ul>
        <li>Unlimited pool mode with smart backup selection</li>
        <li>Auto-switch when quota < 5% or rate-limited</li>
        <li>Background monitoring every 5 minutes</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🔐 Security First</h3>
      <ul>
        <li>AES-256-GCM encryption for sensitive data</li>
        <li>OS native credential manager integration</li>
        <li>Auto migration of legacy plaintext data</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>💾 Account Backup</h3>
      <ul>
        <li>Capture snapshots of account state</li>
        <li>Fast switching between saved accounts</li>
        <li>View, organize, and delete snapshots</li>
      </ul>
    </td>
    <td width="50%">
      <h3>⚙️ Process Control</h3>
      <ul>
        <li>Auto-detect if Antigravity is running</li>
        <li>Launch via URI protocol or executable</li>
        <li>Graceful close or force kill</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🔌 Local API Proxy</h3>
      <ul>
        <li>OpenAI & Anthropic API compatible</li>
        <li>Configurable port and request timeout</li>
        <li>Model mapping (e.g. Claude → Gemini)</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🛠️ Developer Tools</h3>
      <ul>
        <li>Built-in cURL & Python code generation</li>
        <li>Visual service status monitoring</li>
        <li>One-click API Key regeneration</li>
      </ul>
    </td>
  </tr>
</table>

### Additional Features

- **🖥️ System Tray** - Background mode with tray icon and right-click menu
- **🔗 IDE Sync** - Automatically scan and import accounts from IDE's `state.vscdb`
- **📦 Batch Operations** - Batch refresh and delete multiple accounts
- **🌏 Internationalization** - Multi-language support (English / 中文)
- **🎨 Modern UI** - Built with React, TailwindCSS, and Shadcn UI

---

## 📸 Screenshots

<p align="center">
  <img src="docs/assets/screenshot-main.png" alt="Main Interface" width="80%" />
</p>

<p align="center">
  <img src="docs/assets/screenshot-proxy.png" alt="Proxy Interface" width="48%" />
  <img src="docs/assets/screenshot-setting.png" alt="Settings Interface" width="48%" />
</p>


---

## � Quick Start

### Download

Download the latest release for your platform from the [Releases](https://github.com/Draculabo/AntigravityManager/releases) page.

| Platform | Download |
|----------|----------|
| Windows (x64/ARM64) | [.exe installer](https://github.com/Draculabo/AntigravityManager/releases/latest) |
| macOS | [.dmg installer](https://github.com/Draculabo/AntigravityManager/releases/latest) |
| Linux | [.deb / .rpm](https://github.com/Draculabo/AntigravityManager/releases/latest) |

### Build from Source

#### Prerequisites

- Node.js v18 or higher
- npm or yarn

#### Steps

```bash
# Clone the repository
git clone https://github.com/Draculabo/AntigravityManager.git
cd AntigravityManager

# Install dependencies
npm install

# Start development
npm start

# Build for production
npm run make
```

---

## �🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Core** | [Electron](https://www.electronjs.org/), [React](https://react.dev/), [TypeScript](https://www.typescriptlang.org/) |
| **Build Tool** | [Vite](https://vitejs.dev/) |
| **Styling** | [TailwindCSS](https://tailwindcss.com/), [Shadcn UI](https://ui.shadcn.com/) |
| **State** | [TanStack Query](https://tanstack.com/query/latest), [TanStack Router](https://tanstack.com/router/latest) |
| **Database** | [Better-SQLite3](https://github.com/WiseLibs/better-sqlite3) |
| **Testing** | [Vitest](https://vitest.dev/), [Playwright](https://playwright.dev/) |

---

## � Development

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm start` | Start the app in development mode |
| `npm run lint` | Run ESLint to check for code issues |
| `npm run format:write` | Format code with Prettier |
| `npm run test:unit` | Run unit tests with Vitest |
| `npm run test:e2e` | Run E2E tests with Playwright |
| `npm run test:all` | Run all tests |
| `npm run type-check` | Run TypeScript type checking |
| `npm run make` | Build production packages |

### Project Structure

```
AntigravityManager/
├── src/
│   ├── main.ts          # Electron main process
│   ├── preload.ts       # Preload script
│   ├── renderer/        # React renderer process
│   ├── ipc/             # IPC communication handlers
│   └── server/          # Built-in server
├── docs/                # Documentation and assets
└── .github/             # GitHub configuration
```

---

## ❓ FAQ

<details>
<summary><b>Q: The app won't start?</b></summary>

Please check:
1. Make sure all dependencies are installed: `npm install`
2. Check if Node.js version is >= 18
3. Try deleting `node_modules` and reinstalling

</details>

<details>
<summary><b>Q: Account login failed?</b></summary>

1. Ensure network connection is working
2. Try clearing app data and logging in again
3. Check if the account is restricted by Google/Claude

</details>

<details>
<summary><b>Q: macOS shows Keychain/Credential error and OAuth cannot be saved?</b></summary>

This is a common macOS security behavior, usually when the app is unsigned or run directly from Downloads.
This is a **temporary workaround** for personal use:

1. Move the app to `/Applications`
2. Run the following commands in Terminal (repeat after every update)

```plaintext
sudo xattr -dr com.apple.quarantine "/Applications/Antigravity Manager 2.app"
codesign --force --deep --sign - "/Applications/Antigravity Manager 2.app"
```

Reopen the app and allow Keychain access if prompted.

</details>

<details>
<summary><b>Q: How to report issues or suggestions?</b></summary>

Please submit issues or suggestions via [GitHub Issues](https://github.com/Draculabo/AntigravityManager/issues).

</details>

---

## 🌟 Star History

<a href="https://github.com/Draculabo/AntigravityManager/stargazers">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Draculabo/AntigravityManager&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Draculabo/AntigravityManager&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Draculabo/AntigravityManager&type=Date" />
  </picture>
</a>

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

We follow the [Contributor Covenant](CODE_OF_CONDUCT.md) Code of Conduct.

---

## 📄 License

[CC BY-NC-SA 4.0](LICENSE)

---

## ⚠️ Disclaimer

> [!WARNING]
> **For Educational Purposes Only**
>
> This project is intended solely for educational and research purposes. It is provided "as-is" without any warranty. **Commercial use is strictly prohibited.**
>
> By using this software, you agree that you will not use it for any commercial purposes, and you are solely responsible for ensuring your use complies with all applicable laws and regulations. The authors and contributors are not responsible for any misuse or damages arising from the use of this software.

---

<p align="center">
  If this project helps you, please give it a ⭐ Star!
</p>

```

### File: AGENTS.md
```md
# User Guide

This document is a user-level guide for AI assistants working in this repository. It standardizes language, tool/script preferences, and development notes for the current tech stack.

## 💬 Communication Conventions

- **Language**: Use English consistently for conversation, TODOs, and code-related content (comments, UI copy, commit messages, PR descriptions, and similar artifacts).
- **Conclusion first**: Start with the core conclusion/summary, then provide details.
- **References**: When citing code, always provide full file paths (for example, `src/main.ts:42`).

## 💻 Runtime and Tooling

- **Runtime**: Node.js (Electron environment)
- **Node**: Recommended Node.js 20+
- **Package manager**: `npm` (this project includes `package-lock.json`; use npm only)
- **Build tools**: Electron Forge + Vite
- **Terminal**: Windows (PowerShell) / VSCode MCP tools can be used safely

## 🧩 Tech Stack Overview

- **Frontend**:
  - React 19, TypeScript
  - Tailwind CSS v4, `clsx`, `tailwind-merge`, `tailwindcss-animate`
  - Radix UI (Primitives), Lucide React (Icons), Simple Icons (`@icons-pack/react-simple-icons`)
  - `class-variance-authority` (CVA), `react-i18next` + `i18next`
  - TanStack Router (Routing), TanStack Query (State Management)
  - Components: Modular design under `src/components`
- **Backend (Electron Main/Server)**:
  - Electron (Main/Preload/Renderer architecture)
  - NestJS (internal proxy/gateway service, started by main process)
  - Better-SQLite3 (local database), Drizzle ORM / Raw SQL
  - ORPC (type-safe RPC)
  - gRPC (`@grpc/grpc-js`, `@grpc/proto-loader`)
  - Logging: `winston` + `winston-daily-rotate-file`
  - Zod (validation)
- **Testing**:
  - Vitest (unit/integration), Testing Library
  - Playwright (E2E)

## 📁 Directory Structure

```plaintext
.
├─ src/
│  ├─ actions/           # App actions and flow orchestration
│  ├─ assets/            # Static assets
│  ├─ components/        # React UI components (base components under ui/)
│  ├─ constants/         # Constants
│  ├─ hooks/             # Custom React hooks
│  ├─ ipc/               # Electron IPC logic (Database, Config, etc.)
│  ├─ layouts/           # Layout components
│  ├─ lib/               # Shared low-level utilities
│  ├─ localization/      # i18n translation resources
│  ├─ mocks/             # Mock data for tests and development
│  ├─ routes/            # TanStack Router route definitions
│  ├─ server/            # NestJS backend logic (Gateway/Proxy)
│  ├─ services/          # Service layer
│  ├─ styles/            # Global styles (Tailwind classes)
│  ├─ tests/             # Test code
│  ├─ types/             # TypeScript type definitions
│  ├─ utils/             # Utility functions
│  ├─ App.tsx            # React app entry
│  ├─ main.ts            # Electron main entry
│  ├─ preload.ts         # Electron preload script
│  └─ renderer.ts        # Electron renderer entry
├─ forge.config.ts       # Electron Forge config
└─ package.json
```

## 🧱 Component Architecture

- **Modular components**: Each component should have its own directory, with at least a `.tsx` file and optional styles/subcomponents.
- **Shared capabilities**: General helpers in `src/utils/`; low-level shared wrappers in `src/lib/`.
- **Service layer**: Centralize data access in `src/services/` or `src/ipc/`; frontend should consume IPC or RPC only.

## 📦 Common Scripts

Use `npm` for all commands:

- **Development (Dev)**:
  - `npm start` - Start Electron dev environment (Electron Forge)
  - `npm run lint` - Run ESLint checks
  - `npm run format` - Run Prettier check
  - `npm run format:write` - Auto-format with Prettier
  - `npm run type-check` - Run TypeScript type check

- **Build**:
  - `npm run package` - Package app (application bundle only)
  - `npm run make` - Build and generate distributable installers
  - `npm run publish` - Publish app

- **Testing**:
  - `npm test` - Run Vitest tests
  - `npm run test:watch` - Run Vitest in watch mode
  - `npm run test:unit` - Same as above for unit-focused runs
  - `npm run test:e2e` - Run Playwright E2E tests
  - `npm run test:all` - Run all tests

### Running a Single Test

- Unit test: `npm run test:unit path/to/test.test.ts`
- E2E test: `npm run test:e2e path/to/test.spec.ts`
- Type check: `npm run type-check`

## 🧪 Development Notes

- **Build**: Build stage may ignore TS/ESLint errors depending on project/CI configuration.
- **DevTools**: `code-inspector-plugin` is integrated; use `Shift + Click` on page elements to jump to source code.
- **React**: React Strict Mode is disabled.
- **NestJS**: Runs as an Electron child process; logs are visible in main-process console.

## Security and Data

- **Security**: Never commit secrets; use environment variables for sensitive config; validate all user input; encrypt sensitive data.
- **Database**: Use Better-SQLite3; encapsulate operations in services layer; always use prepared statements; test DB operations independently.
- **i18n**: Use `react-i18next`; keys should use kebab-case; translation files are stored in `src/localization/`.

## 📝 Conventions

- **File naming**:
  - Components: PascalCase (for example, `Button.tsx`)
  - Tools/config: camelCase or kebab-case
- **Import paths**: Use `@/` alias for `src/`.
- **Type safety**: Avoid `any`; enforce end-to-end type safety with Zod + TypeScript.
- **Utility methods**: Prefer `lodash-es` over native JavaScript utilities for array/object/string transformations to improve consistency and maintainability.
  - Use named imports (for example, `import { get, groupBy, uniqBy } from 'lodash-es'`), and avoid full-package imports.
- **Component design**:
  - Prefer Radix UI Primitives.
  - Use Tailwind utility classes; avoid CSS Modules unless necessary.
- **API communication**: Frontend should prioritize ORPC client or IPC for strong type inference.

### Naming Specifics

- **Functions/Variables**: camelCase (for example, `handleClick`, `isCurrent`)
- **Constants**: UPPER_SNAKE_CASE (for example, `LOCAL_STORAGE_KEYS`)
- **Files**:
  - Services: `ServiceName.service.ts`
  - Types: `type-name.ts`

### Import Organization

```typescript
// 1. React and core libraries
import React, { useEffect } from 'react';
import { createRoot } from 'react-dom/client';

// 2. External dependencies (alphabetical order)
import { useTranslation } from 'react-i18next';
import { formatDistanceToNow } from 'date-fns';

// 3. Internal imports (using @ alias)
import { Account } from '@/types/account';
import { Card, CardContent } from '@/components/ui/card';
```

### Component Structure

```typescript
// 1. Imports
import React, { useState } from 'react';

// 2. Type definitions
interface ComponentProps { /* props */ }

// 3. Component implementation
export const Component: React.FC<ComponentProps> = ({ prop1 }) => {
  // 4. Hooks
  const { t } = useTranslation();
  // 5. Render
  return <div>{/* JSX */}</div>;
};
```

> Before commit, run `npm run lint` and `npm run format`.

## 📝 Terminal Output and References

- Prefer code blocks; avoid Markdown tables and Mermaid unless necessary.
- If tables are used, keep them left-aligned and check display consistency.

Example:

```plaintext
+------+---------+---------+
|  ID  |  Name   |  Role   |
+------+---------+---------+
|  1   |  Alice  |  Admin  |
|  2   |  Bob    |  User   |
+------+---------+---------+
```

### Reference Rules

- External resources: use full clickable links (issues, docs, API references).
- Source code location: use full file paths (optionally with line numbers).

Example:

```plaintext
- "resolveFilePath owns this logic"
- "VSCode has a known limitation in undo behavior"

References:
- resolveFilePath: src/utils/workspace.ts:40
- VSCode undo limitation: https://github.com/microsoft/vscode/issues/77190
```

## 🏷️ Markdown Writing

- Always specify a language for fenced code blocks; use `plaintext` if unsure.
- Keep one blank line after headings for readability.

## Line-Break Rule

`return` and similar statements should not share a line with other statements. Keep them on separate lines.

## 💭 Commenting Rules

- Required comment scenarios: complex business logic/algorithms, non-obvious behaviors, important design tradeoffs, and key reference links.
- Principles:
  - Explain **why**, not **what**, and not changelog history.
  - Update comments whenever related code changes.
  - Prefer JSDoc; for complex functions, start with high-level overview, then annotate key steps (1, 2, 3...).
  - Keep spacing between English and Chinese words if both appear for readability; do not comment deleted legacy code.

Quality self-check: six months later, what useful context does a new teammate gain from this comment? If the answer is "none", remove it.

Example:

```typescript
/**
 * Handle payment request with multi-step validation.
 */
function processPayment(request: PaymentRequest) {
  // 1. Input validation
  // 2. Risk evaluation (low/medium/high paths)
  // 3. Gateway call
  // 4. User notification
}

export enum BudgetType {
  Free = 'free',
  /** ✅ Prefer JSDoc over end-of-line comments */
  Package = 'package',
}
```

## 🛠️ Development Guide

### General Principles

- Prioritize stability and maintainability before optimization.
- For uncertainty, state assumptions/tradeoffs/validation approach clearly, then implement.
- Trust agreed preconditions; avoid excessive defensive coding against guaranteed invariants.
- Refactor legacy code conservatively; use modern approaches for new features where appropriate.
- Avoid premature optimization: implement simple and direct first; optimize only when justified.
- Always use braces for control flow (`if`, `while`, and similar statements).

### Error Handling

```typescript
// Use try-catch for async operations
try {
  const result = await someOperation();
  return result;
} catch (error) {
  console.error('Operation failed:', error);
  throw new Error('Failed to complete operation');
}

// Use proper error typing
if (error instanceof Error) {
  /* handle Error instance */
}
```

### New Feature Implementation

- Code should be clear, readable, reusable, efficient, and testable.
- Prefer mature and reliable modern APIs.

### Refactoring and Bug Fixing

- Prefer incremental changes; align scope first before large refactors.
- Preserve existing structure and style; avoid over-abstraction risk.

### Development Lifecycle Checklist

Exploration / planning:

- \[ ] Fully understand requirements; break down into 3-6 steps
- \[ ] Review documentation and existing solutions first
- \[ ] Validate ideas by reading actual code
- \[ ] Build a TODO list

Implementation / refactor / fix:

- [ ] Review related templates and surrounding code; follow existing patterns
- [ ] Fail fast on invalid inputs/states
- [ ] Improve frontend interaction and UX within constraints

Acceptance / validation:

- \[ ] Validate implementation through tests or temporary scripts
- \[ ] After multiple incremental edits, evaluate whether changes should be consolidated
- \[ ] Run quality checks
- \[ ] Update related docs

Summary / output:

- \[ ] Verify output formatting requirements
- \[ ] List deviations from plan and key decisions for human review
- \[ ] Provide optimization suggestions
- \[ ] Include full references at the end

## 🔍 Code Quality and Lint

- Use descriptive variable names (`mutationObserver`, `button`, `element`) and avoid `mo`, `btn`, `el`.
- Check for missing critical comments and keep comment language consistent.
- Use VSCode MCP diagnostics for TS/ESLint issues and fix key findings.
- If tests are added/updated, run and fix them before submission.

## ⛔ Operations Requiring Explicit Confirmation

- Running destructive commands
- Executing `git commit` or `git push`
- Creating new test files (maintainer review required first)

## 🔧 Tool Preferences and Commands

Packages and scripts:

- `npm install` (or `npm i`)

Shell:

- Run commands in repository root.
- Quote file paths when appropriate.

Web search:

- Use `WebSearch` for latest information; use `mcp__SearXNG__search` when needed.

Documentation/usage lookup:

- Use `context7` for latest dependency usage.

VSCode MCP (if available):

- `mcp__vscode-mcp__get_references` for refactor impact analysis
- `mcp__vscode-mcp__rename_symbol` for safe renaming
- `mcp__vscode-mcp__get_symbol_lsp_info` for types/signatures/definitions

## 🚨 Local Quality Checks (Optional Flow)

After a set of changes, run these three checks in parallel instead of full lint immediately:

```plaintext
Task(subagent_type: "quick-code-review", description: "Code review", prompt: "[change description]")
Task(subagent_type: "diagnostics", description: "Diagnostics", prompt: "[same as above]")
Task(subagent_type: "run-related-tests", description: "Run tests", prompt: "[same as above]")
```

`change description` example:

```plaintext
- Modified files: list of relative paths
- Context: requirement/business background
```

Flow: initial check -> fix key issues -> re-check -> iterate until key issues are resolved.

Note: these tools are read-only analyzers; you still need to apply fixes manually. Pass precise file paths, not broad directories.

<skills_system priority="1">

## Available Skills

<!-- SKILLS_TABLE_START -->
<usage>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

How to use skills:

- Invoke: Bash("openskills read <skill-name>")
- The skill content will load with detailed instructions on how to complete the task
- Base directory provided in output for resolving bundled resources (references/, scripts/, assets/)

Usage notes:

- Only use skills listed in <available_skills> below
- Do not invoke a skill that is already loaded in your context
- Each skill invocation is stateless
  </usage>

<available_skills>

<skill>
<name>algorithmic-art</name>
<description>Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.</description>
<location>project</location>
</skill>

<skill>
<name>brand-guidelines</name>
<description>Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.</description>
<location>project</location>
</skill>

<skill>
<name>canvas-design</name>
<description>Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violati
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
<a name="readme-top"></a>

# Changelog

## [0.10.0](https://github.com/Draculabo/AntigravityManager/compare/v0.9.2...v0.10.0) (2026-02-19)

### ✨ Features

* Add powerful CLI for account management ([#115](https://github.com/Draculabo/AntigravityManager/issues/115)) ([b949764](https://github.com/Draculabo/AntigravityManager/commit/b9497648c6a7f50dd9b05a7f3d54ac95fa373349))
* Implement provider groupings with account calculator and compre… ([#113](https://github.com/Draculabo/AntigravityManager/issues/113)) ([1e59a1c](https://github.com/Draculabo/AntigravityManager/commit/1e59a1c901d5feedb1089015060fc8c31b614d4d))

### 🐛 Bug Fixes

* refactor layout containers for proxy and settings pages to ensure full height and unified scrolling ([#102](https://github.com/Draculabo/AntigravityManager/issues/102)) ([caaaaf5](https://github.com/Draculabo/AntigravityManager/commit/caaaaf571864aeb2bd68dc271972fd197c999bd1))
* **statusbar:** reduce process polling from 2s to 10s to prevent heap corruption crash ([#110](https://github.com/Draculabo/AntigravityManager/issues/110)) ([118fad5](https://github.com/Draculabo/AntigravityManager/commit/118fad567eeaac4e173b97d3eeb84e1f3edd4556))

## [0.9.2](https://github.com/Draculabo/AntigravityManager/compare/v0.9.1...v0.9.2) (2026-02-11)

### 🐛 Bug Fixes

* project id fallback and stream error regression ([#94](https://github.com/Draculabo/AntigravityManager/issues/94)) ([caf9d58](https://github.com/Draculabo/AntigravityManager/commit/caf9d5849ac86f4c83cb7b33804b873e0c2ff545))

## [0.9.1](https://github.com/Draculabo/AntigravityManager/compare/v0.9.0...v0.9.1) (2026-02-11)

### 🐛 Bug Fixes

* project id forwarding regression ([#93](https://github.com/Draculabo/AntigravityManager/issues/93)) ([ab78d93](https://github.com/Draculabo/AntigravityManager/commit/ab78d9325213623067b5bd867b35464cd4eefd73))

## [0.9.0](https://github.com/Draculabo/AntigravityManager/compare/v0.8.0...v0.9.0) (2026-02-10)

### ✨ Features

* add vercel and ui skills ([#86](https://github.com/Draculabo/AntigravityManager/issues/86)) ([0f7a629](https://github.com/Draculabo/AntigravityManager/commit/0f7a629a4794b5e340371c8d6614c36d14b5ef43))
* global error fallback and e2e ([#91](https://github.com/Draculabo/AntigravityManager/issues/91)) ([b89dd2c](https://github.com/Draculabo/AntigravityManager/commit/b89dd2c3bbb8ae1617cec511960c934c260abc7c))
* implement protocol parity and harden upstream handling ([#88](https://github.com/Draculabo/AntigravityManager/issues/88)) ([13f10fe](https://github.com/Draculabo/AntigravityManager/commit/13f10fe32f73306470a50b0284c8026117b65695))

### 🐛 Bug Fixes

* prevent page crash on 500 and add toast-based fallback ([#90](https://github.com/Draculabo/AntigravityManager/issues/90)) ([bcca5ec](https://github.com/Draculabo/AntigravityManager/commit/bcca5ec9351cef6b1cda708777459055a0bc1a0c))
* prevent sensitive data logging ([#70](https://github.com/Draculabo/AntigravityManager/issues/70)) ([5155e37](https://github.com/Draculabo/AntigravityManager/commit/5155e37fd1ceb4bc72f121fbc9ca53e6b12ce646))

### 📝 Documentation

* upgrade openspec workflow ([#85](https://github.com/Draculabo/AntigravityManager/issues/85)) ([e4584d0](https://github.com/Draculabo/AntigravityManager/commit/e4584d0bc4627054cc2d2b07f998e9f61614e88c))

### 🔧 Continuous Integration

* fix publish workflow release tag resolution ([#82](https://github.com/Draculabo/AntigravityManager/issues/82)) ([5613709](https://github.com/Draculabo/AntigravityManager/commit/56137092beab315843d401e17a3edd456d38ba87))
* remove darwin universal build from publish workflow ([#81](https://github.com/Draculabo/AntigravityManager/issues/81)) ([5b93ca8](https://github.com/Draculabo/AntigravityManager/commit/5b93ca889108ac354e6c9a84f01149f4653ed7c6))
* split publish into build and gated release with dry-run ([#80](https://github.com/Draculabo/AntigravityManager/issues/80)) ([3eaf927](https://github.com/Draculabo/AntigravityManager/commit/3eaf9278ae2ef0103efaeed7a0ebdc77a4961025))

## [0.8.0](https://github.com/Draculabo/AntigravityManager/compare/v0.7.0...v0.8.0) (2026-02-07)

### ✨ Features

* complete account-bound profile switching and hardening ([#78](https://github.com/Draculabo/AntigravityManager/issues/78)) ([a93c6d0](https://github.com/Draculabo/AntigravityManager/commit/a93c6d0cea5b9904a30234faffe767505f753373))

### 🐛 Bug Fixes

* **ci:** increase Node heap for publish step to prevent macOS OOM ([#76](https://github.com/Draculabo/AntigravityManager/issues/76)) ([ee64179](https://github.com/Draculabo/AntigravityManager/commit/ee641799c27425ceb6d2d6d00a132881bedb1f04))
* **ci:** make WiX Toolset setup resilient on Windows runners ([#73](https://github.com/Draculabo/AntigravityManager/issues/73)) ([5fe434f](https://github.com/Draculabo/AntigravityManager/commit/5fe434f7050cb8975d65502baeb03b1747e00611))

### 📝 Documentation

* **openspec:** backfill missing proposals ([287e848](https://github.com/Draculabo/AntigravityManager/commit/287e848b3291d2ee43b173802b87491c2a90930d))

## [0.7.0](https://github.com/Draculabo/AntigravityManager/compare/v0.6.0...v0.7.0) (2026-02-06)

### ✨ Features

* add multi-arch release artifacts and MSI packaging ([#65](https://github.com/Draculabo/AntigravityManager/issues/65)) ([f572ae4](https://github.com/Draculabo/AntigravityManager/commit/f572ae4652937efb25ab66defcfa55ddf65ac484))

### 🐛 Bug Fixes

* restore account switching on Antigravity 1.16.5 and migrate db sync to drizzle ([#69](https://github.com/Draculabo/AntigravityManager/issues/69)) ([ed94abf](https://github.com/Draculabo/AntigravityManager/commit/ed94abf0d6e90c0a1bf9c76f1ec3fdea091f6c4b))

### 📝 Documentation

* translate repository documentation to English ([#72](https://github.com/Draculabo/AntigravityManager/issues/72)) ([18389b9](https://github.com/Draculabo/AntigravityManager/commit/18389b975392f63441ede8369f13f6ef068214ab))

### ♻️ Code Refactoring

* migrate to winston and enable daily rotated app logs ([#71](https://github.com/Draculabo/AntigravityManager/issues/71)) ([2ae2216](https://github.com/Draculabo/AntigravityManager/commit/2ae2216f1ed3fa503ffd87a14cafd3921077a5c4))

## [0.6.0](https://github.com/Draculabo/AntigravityManager/compare/v0.5.0...v0.6.0) (2026-02-04)

### ✨ Features

*  add cloud reset time UI ([#56](https://github.com/Draculabo/AntigravityManager/issues/56)) ([f6f8069](https://github.com/Draculabo/AntigravityManager/commit/f6f8069ce4673ae7027c6ba248daa18c8b602218))
* windows install guidance ([#63](https://github.com/Draculabo/AntigravityManager/issues/63)) ([ce71470](https://github.com/Draculabo/AntigravityManager/commit/ce7147025d37648a82f6f6b300502ef4462bfde6))

### 🐛 Bug Fixes

* correct Windows install notice path ([5bda4b1](https://github.com/Draculabo/AntigravityManager/commit/5bda4b19dfc9ce64735cd39600d41a5deefc26ee))
* **proxy:** route Claude Code CLI requests on /v1/chat/completions to Anthropic handler ([#61](https://github.com/Draculabo/AntigravityManager/issues/61)) ([476d297](https://github.com/Draculabo/AntigravityManager/commit/476d297e4b2dd3015f7ebcbb915b643730816dc6))

## [0.5.0](https://github.com/Draculabo/AntigravityManager/compare/v0.4.0...v0.5.0) (2026-01-30)

### ✨ Features

* **i18n:** add Russian localization ([#48](https://github.com/Draculabo/AntigravityManager/issues/48)) ([63956c9](https://github.com/Draculabo/AntigravityManager/commit/63956c9c2d60f829a998237abe6ade675fdb01ed))
* Implement collapsible sidebar and refined status bar UI ([#45](https://github.com/Draculabo/AntigravityManager/issues/45)) ([1265d04](https://github.com/Draculabo/AntigravityManager/commit/1265d044f69e52fba7da72fde6c47a0b85c58232))
* sentry integration ([#51](https://github.com/Draculabo/AntigravityManager/issues/51)) ([a785640](https://github.com/Draculabo/AntigravityManager/commit/a785640d7a51b65a6852383401bd7c284b716975))

## [0.4.0](https://github.com/Draculabo/AntigravityManager/compare/v0.3.5...v0.4.0) (2026-01-28)

### ✨ Features

* add system autostart and single-instance support ([ea51253](https://github.com/Draculabo/AntigravityManager/commit/ea51253d589abd537682344d3bdb684b8fc9a511))
* implement smart foreground quota refresh with debounce ([dd9e84a](https://github.com/Draculabo/AntigravityManager/commit/dd9e84a0dbefad6066193b6bd468689a755a02e3))

### 🐛 Bug Fixes

* stub nestjs optional modules for packaging ([f0eb7c6](https://github.com/Draculabo/AntigravityManager/commit/f0eb7c6b619a3ea9ea203d66f5dbce731d731e3c))

## [0.3.5](https://github.com/Draculabo/AntigravityManager/compare/v0.3.4...v0.3.5) (2026-01-26)

### 🐛 Bug Fixes

- "Check Quota Now" button not refreshing UI after polling ([#42](https://github.com/Draculabo/AntigravityManager/issues/42)) ([e959ee3](https://github.com/Draculabo/AntigravityManager/commit/e959ee346e7c26a8a4c5b7deefa5bd2452153f9d))

### 📝 Documentation

- remove beta download links from README ([5a21680](https://github.com/Draculabo/AntigravityManager/commit/5a2168030eac4ddeffa1c3b002b2de48b6a11a8f))

## [0.3.4](https://github.com/Draculabo/AntigravityManager/compare/v0.3.3...v0.3.4) (2026-01-26)

### 🐛 Bug Fixes

- **security:** add safeStorage fallback for production builds ([#38](https://github.com/Draculabo/AntigravityManager/issues/38)) ([#43](https://github.com/Draculabo/AntigravityManager/issues/43)) ([0208058](https://github.com/Draculabo/AntigravityManager/commit/02080588b764ed88a5831152a3a1249f1d077d29))

### 📝 Documentation

- update beta release link ([d5ee08d](https://github.com/Draculabo/AntigravityManager/commit/d5ee08d5a06a915a8b82f680b38e2f532105498c))

## [0.3.4-beta.1](https://github.com/Draculabo/AntigravityManager/compare/v0.3.3...v0.3.4-beta.1) (2026-01-25)

### 🐛 Bug Fixes

- **security:** add safeStorage fallback for production builds ([#38](https://github.com/Draculabo/AntigravityManager/issues/38)) ([92dc2f6](https://github.com/Draculabo/AntigravityManager/commit/92dc2f6f2169eb1a32950694387f2333ea2de682))

## [0.3.3](https://github.com/Draculabo/AntigravityManager/compare/v0.3.2...v0.3.3) (2026-01-25)

### 🐛 Bug Fixes

- accept lowercase antigravity in process detection ([0d4e2ab](https://github.com/Draculabo/AntigravityManager/commit/0d4e2ab21f37704e09ef1a67c181c48b42df1180))

### 📝 Documentation

- add beta download link to readme ([f15bb48](https://github.com/Draculabo/AntigravityManager/commit/f15bb48fdda10fda3c2382941ee0ce51204f750a))
- clean up changelog duplicate ([22265e1](https://github.com/Draculabo/AntigravityManager/commit/22265e153c9d394229aa48afdc5948044b74e842))

## [0.3.2](https://github.com/Draculabo/AntigravityManager/compare/v0.3.1...v0.3.2) (2026-01-25)

### 🐛 Bug Fixes

- handle keychain hint and suppress pgrep spam ([bd3d41a](https://github.com/Draculabo/AntigravityManager/commit/bd3d41aed17bafe9d684c5c421bad8b90afa19a8))

### 📝 Documentation

- add macOS self-signing workaround for Keychain issues ([01e3f8f](https://github.com/Draculabo/AntigravityManager/commit/01e3f8f8fd6dacc5eed214ed4b505d6d85f4bcff))

### 🔧 Continuous Integration

- setup semantic release configuration and github actions workflow ([d2945a6](https://github.com/Draculabo/AntigravityManager/commit/d2945a6e8a14d75f577716183cdff093443d9636))
- trigger publish on release published event ([6a07bc0](https://github.com/Draculabo/AntigravityManager/commit/6a07bc0a10a5ad802777e007cfd7390852119b15))

## [0.3.1] - 2026-01-25

### Bug Fixes

- Fixed startup race condition causing cloud accounts verify failure ([f0718db])
- Enabled WAL mode and force initialization on startup to resolve process resource contention ([1bce5d3])

## [0.3.0] - 2026-01-23

### New Features

- Verify Google OAuth code automatically after receipt
- Add button to open logs folder
- Add expiration warning for Google OAuth authentication

### Bug Fixes

- Fixed `state.vscdb` path on Linux to include `User/globalStorage` subdirectory (Fixed [#26](https://github.com/Draculabo/AntigravityManager/issues/26))
- Improved process detection on macOS/Linux using `find-process` to reliably identify the main application and exclude helper processes (Fixed [#27](https://github.com/Draculabo/AntigravityManager/issues/27))
- Fixed keychain access error on macOS Apple Silicon (M1/M2/M3) by adding arm64 build to CI

### Maintenance

- Add VS Code settings for auto-formatting and ESLint

## [0.2.2] - 2026-01-19

### Bug Fixes

- Fixed tray icon not appearing in production builds on Windows
  - Used `extraResource` config to properly copy assets outside of ASAR package
  - Added debug logging for tray icon path resolution

## [0.2.1] - 2026-01-19

### Bug Fixes

- Fixed process detection to be case-insensitive on Linux/macOS (`pgrep -xi`) ([#24](https://github.com/Draculabo/AntigravityManager/pull/24)) - Thanks [@Olbrasoft](https://github.com/Olbrasoft)!
- Fixed manager exclusion logic to prevent accidental self-termination ([#24](https://github.com/Draculabo/AntigravityManager/pull/24))
- Fixed zombie tray icons on application restart/hot reload ([#24](https://github.com/Draculabo/AntigravityManager/pull/24))

### Maintenance

- Applied Prettier formatting to entire codebase (68 files)
- Added node globals to ESLint configuration

## [0.2.0] - 2026-01-16

### New Features

- Enhanced cloudHandler to inject minimal auth state when database entry is missing, improving onboarding reliability.
- Implemented stability fixes and enhanced error handling across the application.

### Improvements

- Upgraded Electron from 32.3.3 to 37.3.1 for improved performance and security.
- Conditionally include plugins based on start command in forge.config.ts for better build flexibility.

### Bug Fixes

- Fixed "Converting circular structure to JSON" error.

### Documentation

- Added curly brace constraints for conditional statements.
- Fixed incorrect reference documentation name.

## [0.1.1] - 2026-01-11

### Bug Fixes

- Fix Antigravity visibility issue on account switch. (Fixed [#19](https://github.com/Draculabo/AntigravityManager/issues/19))

## [0.1.0] - 2026-01-10

### New Features

- LAN Connection Support: Users can now connect via Local Area Network (LAN) for improved flexibility and internal environment support.
- Antigravity Integration: Added native support and adaptation for Antigravity, enhancing overall compatibility.
- Local API Proxy: Built-in OpenAI/Anthropic compatible proxy server.

### Bug Fixes

- Reverse Proxy Issue: Resolved a critical error occurring during reverse proxy configurations. (Fixed [#11](https://github.com/Draculabo/AntigravityManager/issues/11))

## [0.0.1] - 2025-12-22

### Added

- Initial release of Antigravity Manager
- Multi-account management for Google Gemini and Claude
- Real-time quota monitoring
- Intelligent auto-switching capabilities
- Secure credential storage (AES-256-GCM)
- IDE synchronization
- Dark mode support
- System tray integration

```

### File: CLAUDE.md
```md
Always refer to `@AGENTS.md`.

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [INSERT EMAIL ADDRESS]. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

---

**Note**: Please replace `[INSERT EMAIL ADDRESS]` with your actual contact email if you wish to receive reports.

```

### File: CONTRIBUTING.md
```md
# Contributing to Antigravity Manager

First off, thank you for considering contributing to Antigravity Manager! 🎉

It's people like you that make Antigravity Manager such a great tool. We welcome contributions from everyone, whether it's a bug report, feature suggestion, documentation improvement, or code contribution.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AntigravityManager.git
   cd AntigravityManager
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/Draculabo/AntigravityManager.git
   ```

## 💻 Development Setup

### Prerequisites

- Node.js v18 or higher
- npm (comes with Node.js)
- Git

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm start
```

### Available Scripts

| Command                | Description                         |
| ---------------------- | ----------------------------------- |
| `npm start`            | Start the app in development mode   |
| `npm run lint`         | Run ESLint to check for code issues |
| `npm run format:write` | Format code with Prettier           |
| `npm run test:unit`    | Run unit tests with Vitest          |
| `npm run test:e2e`     | Run E2E tests with Playwright       |
| `npm run test:all`     | Run all tests                       |
| `npm run type-check`   | Run TypeScript type checking        |
| `npm run make`         | Build production packages           |

## ✏️ Making Changes

1. **Create a new branch** from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** and commit them:

   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

3. **Keep your branch updated**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

### Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/). Each commit message should be structured as follows:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types:**

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect code meaning (formatting, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding or correcting tests
- `chore`: Changes to build process or auxiliary tools

**Examples:**

```
feat(auth): add Google OAuth support
fix(quota): resolve quota refresh timeout issue
docs(readme): update installation instructions
```

## 🔄 Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features
3. **Ensure all tests pass**: `npm run test:all`
4. **Ensure code is formatted**: `npm run format:write`
5. **Ensure no lint errors**: `npm run lint`
6. **Push to your fork** and create a Pull Request

### PR Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or my feature works
- [ ] New and existing unit tests pass locally with my changes

## 🎨 Style Guidelines

### TypeScript/JavaScript

- Use TypeScript for all new code
- Follow the existing code style (enforced by ESLint and Prettier)
- Use meaningful variable and function names
- Add JSDoc comments for public APIs

### React Components

- Use functional components with hooks
- Keep components small and focused
- Use TypeScript interfaces for props
- Follow the existing file structure

### CSS/Styling

- Use TailwindCSS utility classes
- Follow the design system in `components.json`
- Ensure responsive design

## 🐛 Reporting Bugs

Found a bug? Please [create an issue](https://github.com/Draculabo/AntigravityManager/issues/new?template=bug_report.md) with:

- **Clear title** describing the issue
- **Steps to reproduce** the behavior
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, app version)

## 💡 Suggesting Features

Have an idea? Please [create an issue](https://github.com/Draculabo/AntigravityManager/issues/new?template=feature_request.md) with:

- **Clear description** of the feature
- **Use case** - why is this feature needed?
- **Possible implementation** ideas (optional)

## 🙏 Thank You

Your contributions help make Antigravity Manager better for everyone. Thank you for taking the time to contribute!

---

If you have any questions, feel free to open an issue or reach out to the maintainers.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
