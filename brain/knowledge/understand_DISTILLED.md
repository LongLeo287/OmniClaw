---
id: understand
type: knowledge
owner: OA_Triage
---
# understand
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "understand-anything",
  "private": true,
  "type": "module",
  "main": ".opencode/plugins/understand-anything.js",
  "packageManager": "pnpm@10.6.2+sha512.47870716bea1572b53df34ad8647b42962bc790ce2bf4562ba0f643237d7302a3d6a8ecef9e4bdfc01d23af1969aa90485d4cebb0b9638fa5ef1daef656f6c1b",
  "scripts": {
    "prepare": "pnpm --filter @understand-anything/core build",
    "build": "pnpm -r build",
    "test": "vitest",
    "dev:dashboard": "pnpm --filter @understand-anything/dashboard dev",
    "lint": "eslint ."
  },
  "devDependencies": {
    "typescript": "^5.7.0",
    "vitest": "^3.1.0"
  }
}

```

### File: README.md
```md
<h1 align="center">Understand Anything</h1>

<p align="center">
  <strong>Turn any codebase into an interactive knowledge graph you can explore, search, and ask questions about.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ja-JP.md">日本語</a> | <a href="README.tr-TR.md">Türkçe</a>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-blue" alt="Quick Start" /></a>
  <a href="https://github.com/Lum1104/Understand-Anything/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT" /></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Claude_Code-Plugin-8A2BE2" alt="Claude Code Plugin" /></a>
  <a href="https://lum1104.github.io/Understand-Anything"><img src="https://img.shields.io/badge/Homepage-d4a574" alt="Homepage" /></a>
  <a href="https://lum1104.github.io/Understand-Anything/demo/"><img src="https://img.shields.io/badge/Live_Demo-00c853" alt="Live Demo" /></a>
</p>

<p align="center">
  <img src="assets/hero.jpg" alt="Understand Anything — Turn any codebase into an interactive knowledge graph" width="800" />
</p>

---

> [!TIP]
> **A huge thank you to the community!** The support for Understand-Anything has been incredible. If this tool saves you a few minutes of digging through complexity, that's all I wanted. 🚀

**You just joined a new team. The codebase is 200,000 lines of code. Where do you even start?**

Understand Anything is a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that analyzes your project with a multi-agent pipeline, builds a knowledge graph of every file, function, class, and dependency, then gives you an interactive dashboard to explore it all visually. Stop reading code blind. Start seeing the big picture.

---

## 🤔 Why?

Reading code is hard. Understanding a whole codebase is harder. Documentation is always out of date, onboarding takes weeks, and every new feature feels like archaeology.

Understand Anything fixes this by combining **LLM intelligence** with **static analysis** to produce a living, explorable map of your project — with plain-English explanations for everything.

---

## 🎯 Who is this for?

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>👩‍💻 Junior Developers</h3>
      <p>Stop drowning in unfamiliar code. Get guided tours that walk you through the architecture step by step, with every function and class explained in plain English.</p>
    </td>
    <td width="33%" valign="top">
      <h3>📋 Product Managers & Designers</h3>
      <p>Finally understand how the system actually works without reading code. Ask questions like "how does authentication work?" and get clear answers grounded in the real codebase.</p>
    </td>
    <td width="33%" valign="top">
      <h3>🤖 AI-Assisted Developers</h3>
      <p>Give your AI tools deep context about your project. Use <code>/understand-diff</code> before code review, <code>/understand-explain</code> to dive into any module, or <code>/understand-chat</code> to reason about architecture.</p>
    </td>
  </tr>
</table>

---

## 🚀 Quick Start

### 1. Install the plugin

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### 2. Analyze your codebase

```bash
/understand
```

A multi-agent pipeline scans your project, extracts every file, function, class, and dependency, then builds a knowledge graph saved to `.understand-anything/knowledge-graph.json`.

### 3. Explore the dashboard

```bash
/understand-dashboard
```

An interactive web dashboard opens with your codebase visualized as a graph — color-coded by architectural layer, searchable, and clickable. Select any node to see its code, relationships, and a plain-English explanation.

### 4. Keep learning

```bash
# Ask anything about the codebase
/understand-chat How does the payment flow work?

# Analyze impact of your current changes
/understand-diff

# Deep-dive into a specific file or function
/understand-explain src/auth/login.ts

# Generate an onboarding guide for new team members
/understand-onboard

# Extract business domain knowledge (domains, flows, steps)
/understand-domain
```

---

## 🌐 Multi-Platform Installation

Understand-Anything works across multiple AI coding platforms.

### Claude Code (Native)

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### Codex

Tell Codex:
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.codex/INSTALL.md
```

### OpenCode

Tell OpenCode:
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.opencode/INSTALL.md
```

### OpenClaw

Tell OpenClaw:
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.openclaw/INSTALL.md
```

### Cursor

Cursor auto-discovers the plugin via `.cursor-plugin/plugin.json` when this repo is cloned. No manual installation needed — just clone and open in Cursor.

### VS Code + GitHub Copilot

VS Code with GitHub Copilot (v1.108+) auto-discovers the plugin via `.copilot-plugin/plugin.json` when this repo is cloned. No manual installation needed — just clone and open in VS Code.

For personal skills (available across all projects), tell GitHub Copilot:
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.vscode/INSTALL.md
```

### Antigravity

Tell Antigravity:
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.antigravity/INSTALL.md
```

### Gemini CLI

Tell Gemini CLI:
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.gemini/INSTALL.md
```

### Pi Agent

Tell Pi Agent:
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.pi/INSTALL.md
```

### Platform Compatibility

| Platform | Status | Install Method |
|----------|--------|----------------|
| Claude Code | ✅ Native | Plugin marketplace |
| Codex | ✅ Supported | AI-driven install |
| OpenCode | ✅ Supported | AI-driven install |
| OpenClaw | ✅ Supported | AI-driven install |
| Cursor | ✅ Supported | Auto-discovery |
| VS Code + GitHub Copilot | ✅ Supported | Auto-discovery |
| Antigravity | ✅ Supported | AI-driven install |
| Gemini CLI | ✅ Supported | AI-driven install |
| Pi Agent | ✅ Supported | AI-driven install |

---

## ✨ Features

<p align="center">
  <img src="assets/overview.png" alt="Dashboard Screenshot" width="800" />
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🗺️ Interactive Knowledge Graph</h3>
      <p>Files, functions, classes, and their relationships visualized with React Flow. Click any node to see its code and connections.</p>
    </td>
    <td width="50%" valign="top">
      <h3>💬 Plain-English Summaries</h3>
      <p>Every node described by an LLM so anyone — technical or not — can understand what it does and why it exists.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🧭 Guided Tours</h3>
      <p>Auto-generated walkthroughs of the architecture, ordered by dependency. Learn the codebase in the right order.</p>
    </td>
    <td width="50%" valign="top">
      <h3>🔍 Fuzzy & Semantic Search</h3>
      <p>Find anything by name or by meaning. Search "which parts handle auth?" and get relevant results across the graph.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>📊 Diff Impact Analysis</h3>
      <p>See which parts of the system your changes affect before you commit. Understand ripple effects across the codebase.</p>
    </td>
    <td width="50%" valign="top">
      <h3>🎭 Persona-Adaptive UI</h3>
      <p>The dashboard adjusts its detail level based on who you are — junior dev, PM, or power user.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏗️ Layer Visualization</h3>
      <p>Automatic grouping by architectural layer — API, Service, Data, UI, Utility — with color-coded legend.</p>
    </td>
    <td width="50%" valign="top">
      <h3>📚 Language Concepts</h3>
      <p>12 programming patterns (generics, closures, decorators, etc.) explained in context wherever they appear.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏢 Business Domain Knowledge</h3>
      <p>Extract business domains, flows, and process steps from your codebase. See how business logic maps to code with an interactive horizontal flow graph — domains contain flows, flows contain steps.</p>
    </td>
    <td width="50%" valign="top">
      <h3>🔀 Structural + Domain Views</h3>
      <p>Toggle between the structural code graph and the business domain graph in the dashboard. Understand both how the code is organized and what business processes it implements.</p>
    </td>
  </tr>
</table>

---

## 🔧 Under the Hood

### Multi-Agent Pipeline

The `/understand` command orchestrates 5 specialized agents, and `/understand-domain` adds a 6th:

| Agent | Role |
|-------|------|
| `project-scanner` | Discover files, detect languages and frameworks |
| `file-analyzer` | Extract functions, classes, imports; produce graph nodes and edges |
| `architecture-analyzer` | Identify architectural layers |
| `tour-builder` | Generate guided learning tours |
| `graph-reviewer` | Validate graph completeness and referential integrity (runs inline by default; use `--review` for full LLM review) |
| `domain-analyzer` | Extract business domains, flows, and process steps (used by `/understand-domain`) |

File analyzers run in parallel (up to 5 concurrent, 20-30 files per batch). Supports incremental updates — only re-analyzes files that changed since the last run.

### Project Structure

```
understand-anything-plugin/
  .claude-plugin/  — Plugin manifest
  agents/          — Specialized AI agents
  skills/          — Skill definitions (/understand, /understand-chat, etc.)
  src/             — TypeScript source (context-builder, diff-analyzer, etc.)
  packages/
    core/          — Analysis engine (types, persistence, tree-sitter, search, schema, tours)
    dashboard/     — React + TypeScript web dashboard
```

### Tech Stack

TypeScript, pnpm workspaces, React 18, Vite, TailwindCSS v4, React Flow, Zustand, web-tree-sitter, Fuse.js, Zod, Dagre

### Development Commands

| Command | Description |
|---------|-------------|
| `pnpm install` | Install all dependencies |
| `pnpm --filter @understand-anything/core build` | Build the core package |
| `pnpm --filter @understand-anything/core test` | Run core tests |
| `pnpm --filter @understand-anything/skill build` | Build the plugin package |
| `pnpm --filter @understand-anything/skill test` | Run plugin tests |
| `pnpm --filter @understand-anything/dashboard build` | Build the dashboard |
| `pnpm dev:dashboard` | Start dashboard dev server |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Run the tests (`pnpm --filter @understand-anything/core test`)
4. Commit your changes and open a pull request

Please open an issue first for major changes so we can discuss the approach.

---

<p align="center">
  <strong>Stop reading code blind. Start understanding everything.</strong>
</p>

## Star History

<a href="https://www.star-history.com/?repos=Lum1104%2FUnderstand-Anything&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />
 </picture>
</a>

<p align="center">
  MIT License &copy; <a href="https://github.com/Lum1104">Lum1104</a>
</p>

```

### File: homepage\package.json
```json
{
  "name": "homepage",
  "type": "module",
  "version": "0.0.1",
  "engines": {
    "node": ">=22.12.0"
  },
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^6.0.4"
  }
}
```

### File: homepage\README.md
```md
# Astro Starter Kit: Minimal

```sh
pnpm create astro@latest -- --template minimal
```

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `pnpm install`             | Installs dependencies                            |
| `pnpm dev`             | Starts local dev server at `localhost:4321`      |
| `pnpm build`           | Build your production site to `./dist/`          |
| `pnpm preview`         | Preview your build locally, before deploying     |
| `pnpm astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).

```

### File: understand-anything-plugin\package.json
```json
{
  "name": "@understand-anything/skill",
  "version": "2.1.0",
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "test": "vitest run"
  },
  "dependencies": {
    "@understand-anything/core": "workspace:*"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "typescript": "^5.7.0",
    "vitest": "^3.1.0"
  }
}

```

### File: CLAUDE.md
```md
# Understand Anything

## Project Overview
An open-source tool combining LLM intelligence + static analysis to produce interactive dashboards for understanding codebases.

## Prerequisites
- Node.js >= 22 (developed on v24)
- pnpm >= 10 (pinned via `packageManager` field in root `package.json`)

## Architecture
- **Monorepo** with pnpm workspaces
- **understand-anything-plugin/** — Claude Code plugin containing all source code:
  - **packages/core** — Shared analysis engine (types, persistence, tree-sitter, search, schema, tours, plugins)
  - **packages/dashboard** — React + TypeScript web dashboard (React Flow, Zustand, TailwindCSS v4)
  - **src/** — Skill TypeScript source for `/understand-chat`, `/understand-diff`, `/understand-explain`, `/understand-onboard`
  - **skills/** — Skill definitions (`/understand`, `/understand-dashboard`, etc.)
  - **agents/** — Agent definitions (project-scanner, file-analyzer, architecture-analyzer, tour-builder, graph-reviewer)

## Dashboard
- Dark luxury theme: deep blacks (#0a0a0a), gold/amber accents (#d4a574), DM Serif Display typography
- Graph-first layout: 75% graph + 360px right sidebar
- No ChatPanel or Monaco Editor
- Sidebar: ProjectOverview (default) → NodeInfo (node selected) → LearnPanel (Learn persona)
- Code viewer: styled summary overlay (slides up from bottom on file node click)
- Schema validation on graph load with error banner

## Agent Pipeline
- Agents write intermediate results to `.understand-anything/intermediate/` on disk (not returned to context)
- Agent models: all set to `inherit` for cross-platform compatibility (Claude Code, Cursor, opencode, etc.)
- `/understand` auto-triggers `/understand-dashboard` after completion
- Intermediate files cleaned up after graph assembly

## Key Commands
- `pnpm install` — Install all dependencies
- `pnpm --filter @understand-anything/core build` — Build the core package
- `pnpm --filter @understand-anything/core test` — Run core tests
- `pnpm --filter @understand-anything/skill build` — Build the plugin package
- `pnpm --filter @understand-anything/skill test` — Run plugin tests
- `pnpm --filter @understand-anything/dashboard build` — Build the dashboard
- `pnpm dev:dashboard` — Start dashboard dev server
- `pnpm lint` — Run ESLint across the project

## Conventions
- TypeScript strict mode everywhere
- Vitest for testing
- ESM modules (`"type": "module"`)
- Knowledge graph JSON lives in `.understand-anything/` directory of analyzed projects
- Core uses subpath exports (`./search`, `./types`, `./schema`) to avoid pulling Node.js modules into browser

## Gotchas
- **tree-sitter**: Uses `web-tree-sitter` (WASM) instead of native `tree-sitter` — native bindings fail on darwin/arm64 + Node 24
- **Dashboard imports**: Dashboard must only import from core's browser-safe subpath exports (`./search`, `./types`, `./schema`), never the main entry point which pulls in Node.js modules

## Scripts
- `scripts/generate-large-graph.mjs` — Generates a fake knowledge graph for performance testing (e.g. large-graph layout). Writes to `.understand-anything/knowledge-graph.json`. Usage: `node scripts/generate-large-graph.mjs [nodeCount]` (default: 3000 nodes). Not part of the production pipeline.

## Versioning
When pushing to remote, bump the version in **all four** of these files (keep them in sync):
- `understand-anything-plugin/package.json` → `"version"` field
- `.claude-plugin/marketplace.json` → `plugins[0].version` field
- `.claude-plugin/plugin.json` → `"version"` field
- `.cursor-plugin/plugin.json` → `"version"` field

## Testing Local Plugin Changes

Claude Code caches installed plugins at `~/.claude/plugins/cache/understand-anything/understand-anything/<version>/`. Symlinks don't work because Claude's Search/Glob tools can't follow them. To test local changes:

1. **Build the packages:**
   ```bash
   pnpm --filter @understand-anything/core build
   pnpm --filter @understand-anything/skill build
   ```

2. **Find the installed version** (must match what the marketplace currently serves):
   ```bash
   ls ~/.claude/plugins/cache/understand-anything/understand-anything/
   ```

3. **Copy your local plugin into the cache**, replacing `<VERSION>` with the version from step 2:
   ```bash
   rm -rf ~/.claude/plugins/cache/understand-anything/understand-anything/<VERSION>
   cp -R ./understand-anything-plugin ~/.claude/plugins/cache/understand-anything/understand-anything/<VERSION>
   ```

4. **Start a fresh Claude Code session** (existing sessions cache the old prompts in context).

5. **Run `/understand --full`** in the target project to verify.

**Re-sync after further changes:**
```bash
pnpm --filter @understand-anything/core build && \
cp -R ./understand-anything-plugin/* ~/.claude/plugins/cache/understand-anything/understand-anything/<VERSION>/
```

**To revert to upstream:** Uninstall and reinstall the plugin from the marketplace — it repopulates the cache from the upstream repo.

```

### File: CONTRIBUTING.md
```md
# Contributing to Understand Anything

Thank you for your interest in contributing to Understand Anything! This document provides guidelines and instructions for contributing to the project.

## 🌟 Ways to Contribute

- **Bug Reports**: Found a bug? Open an issue with detailed reproduction steps
- **Feature Requests**: Have an idea? Share it in the issues section
- **Documentation**: Improve or translate documentation
- **Code**: Fix bugs, add features, or improve performance
- **Testing**: Write tests to improve code coverage

## 🚀 Getting Started

### Prerequisites

- Node.js >= 22 (developed on v24)
- pnpm >= 10 (pinned via `packageManager` field in root `package.json`)
- Git for version control

### Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Understand-Anything.git
   cd Understand-Anything
   ```

2. **Install Dependencies**
   ```bash
   pnpm install
   ```

3. **Build Core Package**
   ```bash
   pnpm --filter @understand-anything/core build
   ```

4. **Run Tests**
   ```bash
   pnpm --filter @understand-anything/core test
   pnpm --filter @understand-anything/skill test
   ```

5. **Start Dashboard (Optional)**
   ```bash
   pnpm dev:dashboard
   ```

## 📝 Development Workflow

### 1. Create a Branch

Create a descriptive branch name:
```bash
git checkout -b feat/my-feature        # For new features
git checkout -b fix/bug-description    # For bug fixes
git checkout -b docs/update-readme     # For documentation
```

### 2. Make Changes

- Write clean, readable code
- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run all tests
pnpm --filter @understand-anything/core test
pnpm --filter @understand-anything/skill test

# Run linter
pnpm lint

# Build packages
pnpm build
```

### 4. Commit Your Changes

Write clear, descriptive commit messages:
```bash
git add .
git commit -m "feat: add keyboard shortcuts to dashboard"
```

**Commit Message Convention:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin your-branch-name
```

Then open a Pull Request on GitHub with:
- Clear title describing the change
- Detailed description of what changed and why
- Link to related issues (if any)
- Screenshots (for UI changes)

## 🧪 Testing Guidelines

### Writing Tests

- Use Vitest for testing
- Place tests in `__tests__` directories or `*.test.ts` files
- Aim for high test coverage for new features
- Test edge cases and error conditions

Example test structure:
```typescript
import { describe, it, expect } from 'vitest';

describe('MyFeature', () => {
  it('should do something', () => {
    // Arrange
    const input = 'test';

    // Act
    const result = myFunction(input);

    // Assert
    expect(result).toBe('expected');
  });
});
```

### Running Tests

```bash
# Run all tests
pnpm test

# Run tests for specific package
pnpm --filter @understand-anything/core test

# Run tests in watch mode
pnpm --filter @understand-anything/core test --watch
```

## 📚 Code Style Guidelines

### TypeScript

- Use TypeScript strict mode
- Define explicit types for function parameters and return values
- Avoid `any` type - use `unknown` if type is truly unknown
- Use interfaces for object shapes
- Use type aliases for unions and complex types

### Formatting

- The project uses ESLint for code quality
- Consistent indentation (2 spaces)
- Use meaningful variable and function names
- Keep functions small and focused

### React/Dashboard

- Use functional components with hooks
- Keep components focused and single-purpose
- Use Zustand for state management
- Follow the existing component structure

### File Organization

```
understand-anything-plugin/
├── packages/
│   ├── core/              # Core analysis engine
│   │   ├── src/
│   │   └── package.json
│   └── dashboard/         # React dashboard
│       ├── src/
│       │   ├── components/
│       │   ├── utils/
│       │   └── store.ts
│       └── package.json
├── src/                   # Plugin skills implementation
├── agents/                # AI agent prompts
└── skills/                # Skill definitions
```

## 🌍 Translation Guidelines

### Adding a New Language

1. Create `README.{language-code}.md` (e.g., `README.fr-FR.md`)
2. Translate all sections while maintaining formatting
3. Update main `README.md` to include language link
4. Keep technical terms in English where appropriate
5. Ensure all links still work

Example:
```markdown
<a href="README.md">English</a> | <a href="README.fr-FR.md">Français</a>
```

## 🐛 Bug Reports

When reporting bugs, include:

- **Description**: Clear description of the issue
- **Steps to Reproduce**: Detailed steps to reproduce the bug
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: OS, Node version, pnpm version
- **Screenshots**: If applicable
- **Error Messages**: Full error output

## 💡 Feature Requests

When requesting features:

- **Use Case**: Describe the problem you're trying to solve
- **Proposed Solution**: How you envision the feature working
- **Alternatives**: Other solutions you've considered
- **Additional Context**: Any other relevant information

## 📋 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows the project's style guidelines
- [ ] All tests pass (`pnpm test`)
- [ ] New code has test coverage
- [ ] Documentation is updated (if needed)
- [ ] Commit messages follow convention
- [ ] PR description clearly explains changes
- [ ] No console.log or debug code left behind
- [ ] Branch is up to date with main

## 🤝 Code Review Process

1. **Automated Checks**: CI runs tests and linting
2. **Maintainer Review**: Project maintainers review the code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, PR will be merged
5. **Cleanup**: Delete your branch after merge

## 📞 Getting Help

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: Check existing docs first

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes (for significant contributions)
- Special mentions for exceptional contributions

---

**Thank you for contributing to Understand Anything! Your contributions help make code understanding accessible to everyone.** 🚀

```

### File: pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    devDependencies:
      typescript:
        specifier: ^5.7.0
        version: 5.9.3
      vitest:
        specifier: ^3.1.0
        version: 3.2.4(@types/debug@4.1.12)(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3)

  homepage:
    dependencies:
      astro:
        specifier: ^6.0.4
        version: 6.0.4(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(rollup@4.59.0)(typescript@5.9.3)(yaml@2.8.3)

  understand-anything-plugin:
    dependencies:
      '@understand-anything/core':
        specifier: workspace:*
        version: link:packages/core
    devDependencies:
      '@types/node':
        specifier: ^22.0.0
        version: 22.19.15
      typescript:
        specifier: ^5.7.0
        version: 5.9.3
      vitest:
        specifier: ^3.1.0
        version: 3.2.4(@types/debug@4.1.12)(@types/node@22.19.15)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3)

  understand-anything-plugin/packages/core:
    dependencies:
      fuse.js:
        specifier: ^7.1.0
        version: 7.1.0
      tree-sitter-javascript:
        specifier: ^0.25.0
        version: 0.25.0
      tree-sitter-typescript:
        specifier: ^0.23.2
        version: 0.23.2
      web-tree-sitter:
        specifier: ^0.26.6
        version: 0.26.6
      yaml:
        specifier: ^2.8.3
        version: 2.8.3
      zod:
        specifier: ^4.3.6
        version: 4.3.6
    devDependencies:
      '@types/node':
        specifier: ^25.5.0
        version: 25.5.0
      '@vitest/coverage-v8':
        specifier: 3.2.4
        version: 3.2.4(vitest@3.2.4(@types/debug@4.1.12)(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3))
      typescript:
        specifier: ^5.7.0
        version: 5.9.3
      vitest:
        specifier: ^3.1.0
        version: 3.2.4(@types/debug@4.1.12)(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3)

  understand-anything-plugin/packages/dashboard:
    dependencies:
      '@dagrejs/dagre':
        specifier: ^2.0.4
        version: 2.0.4
      '@understand-anything/core':
        specifier: workspace:*
        version: link:../core
      '@xyflow/react':
        specifier: ^12.0.0
        version: 12.10.1(@types/react@19.2.14)(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      devlop:
        specifier: ^1.1.0
        version: 1.1.0
      hast-util-to-jsx-runtime:
        specifier: ^2.3.6
        version: 2.3.6
      react:
        specifier: ^19.0.0
        version: 19.2.4
      react-dom:
        specifier: ^19.0.0
        version: 19.2.4(react@19.2.4)
      react-markdown:
        specifier: ^10.1.0
        version: 10.1.0(@types/react@19.2.14)(react@19.2.4)
      zustand:
        specifier: ^5.0.0
        version: 5.0.11(@types/react@19.2.14)(react@19.2.4)(use-sync-external-store@1.6.0(react@19.2.4))
    devDependencies:
      '@tailwindcss/vite':
        specifier: ^4.0.0
        version: 4.2.1(vite@6.4.1(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3))
      '@types/react':
        specifier: ^19.0.0
        version: 19.2.14
      '@types/react-dom':
        specifier: ^19.0.0
        version: 19.2.3(@types/react@19.2.14)
      '@vitejs/plugin-react':
        specifier: ^4.3.0
        version: 4.7.0(vite@6.4.1(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3))
      tailwindcss:
        specifier: ^4.0.0
        version: 4.2.1
      typescript:
        specifier: ^5.7.0
        version: 5.9.3
      vite:
        specifier: ^6.0.0
        version: 6.4.1(@types/node@25.5.0)(jiti@2.6.1)(lightningcss@1.31.1)(yaml@2.8.3)

packages:

  '@ampproject/remapping@2.3.0':
    resolution: {integrity: sha512-30iZtAPgz+LTIYoeivqYo853f02jBYSd5uGnGpkFV0M3xOt9aN73erkgYAmZU43x4VfqcnLxW9Kpg3R5LC4YYw==}
    engines: {node: '>=6.0.0'}

  '@astrojs/compiler@3.0.0':
    resolution: {integrity: sha512-MwAbDE5mawZ1SS+D8qWiHdprdME5Tlj2e0YjxnEICvcOpbSukNS7Sa7hA5PK+6RrmUr/t6Gi5YgrdZKjbO/WPQ==}

  '@astrojs/internal-helpers@0.8.0':
    resolution: {integrity: sha512-J56GrhEiV+4dmrGLPNOl2pZjpHXAndWVyiVDYGDuw6MWKpBSEMLdFxHzeM/6sqaknw9M+HFfHZAcvi3OfT3D/w==}

  '@astrojs/markdown-remark@7.0.0':
    resolution: {integrity: sha512-jTAXHPy45L7o1ljH4jYV+ShtOHtyQUa1mGp3a5fJp1soX8lInuTJQ6ihmldHzVM4Q7QptU4SzIDIcKbBJO7sXQ==}

  '@astrojs/prism@4.0.0':
    resolution: {integrity: sha512-NndtNPpxaGinRpRytljGBvYHpTOwHycSZ/c+lQi5cHvkqqrHKWdkPEhImlODBNmbuB+vyQUNUDXyjzt66CihJg==}
    engines: {node: ^20.19.1 || >=22.12.0}

  '@astrojs/telemetry@3.3.0':
    resolution: {integrity: sha512-UFBgfeldP06qu6khs/yY+q1cDAaArM2/7AEIqQ9Cuvf7B1hNLq0xDrZkct+QoIGyjq56y8IaE2I3CTvG99mlhQ==}
    engines: {node: 18.20.8 || ^20.3.0 || >=22.0.0}

  '@babel/code-frame@7.29.0':
    resolution: {integrity: sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==}
    engines: {node: '>=6.9.0'}

  '@babel/compat-data@7.29.0':
    resolution: {integrity: sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==}
    engines: {node: '>=6.9.0'}

  '@babel/core@7.29.0':
    resolution: {integrity: sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==}
    engines: {node: '>=6.9.0'}

  '@babel/generator@7.29.1':
    resolution: {integrity: sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-compilation-targets@7.28.6':
    resolution: {integrity: sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-globals@7.28.0':
    resolution: {integrity: sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-imports@7.28.6':
    resolution: {integrity: sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-transforms@7.28.6':
    resolution: {integrity: sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-plugin-utils@7.28.6':
    resolution: {integrity: sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-string-parser@7.27.1':
    resolution: {integrity: sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.28.5':
    resolution: {integrity: sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-option@7.27.1':
    resolution: {integrity: sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==}
    engines: {node: '>=6.9.0'}

  '@babel/helpers@7.28.6':
    resolution: {integrity: sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.29.0':
    resolution: {integrity: sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/plugin-transform-react-jsx-self@7.27.1':
    resolution: {integrity: sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/plugin-transform-react-jsx-source@7.27.1':
    resolution: {integrity: sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/template@7.28.6':
    resolution: {integrity: sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==}
    engines: {node: '>=6.9.0'}

  '@babel/traverse@7.29.0':
    resolution: {integrity: sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==}
    engines: {node: '>=6.9.0'}

  '@babel/types@7.29.0':
    resolution: {integrity: sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==}
    engines: {node: '>=6.9.0'}

  '@bcoe/v8-coverage@1.0.2':
    resolution: {integrity: sha512-6zABk/ECA/QYSCQ1NGiVwwbQerUCZ+TQbp64Q3AgmfNvurHH0j8TtXa1qbShXA6qqkpAj4V5W8pP6mLe1mcMqA==}
    engines: {node: '>=18'}

  '@capsizecss/unpack@4.0.0':
    resolution: {integrity: sha512-VERIM64vtTP1C4mxQ5thVT9fK0apjPFobqybMtA1UdUujWka24ERHbRHFGmpbbhp73MhV+KSsHQH9C6uOTdEQA==}
    engines: {node: '>=18'}

  '@clack/core@1.1.0':
    resolution: {integrity: sha512-SVcm4Dqm2ukn64/8Gub2wnlA5nS2iWJyCkdNHcvNHPIeBTGojpdJ+9cZKwLfmqy7irD4N5qLteSilJlE0WLAtA==}

  '@clack/prompts@1.1.0':
    resolution: {integrity: sha512-pkqbPGtohJAvm4Dphs2M8xE29ggupihHdy1x84HNojZuMtFsHiUlRvqD24tM2+XmI+61LlfNceM3Wr7U5QES5g==}

  '@dagrejs/dagre@2.0.4':
    resolution: {integrity: sha512-J6vCWTNpicHF4zFlZG1cS5DkGzMr9941gddYkakjrg3ZNev4bbqEgLHFTWiFrcJm7UCRu7olO3K6IRDd9gSGhA==}

  '@dagrejs/graphlib@3.0.4':
    resolution: {integrity: sha512-HxZ7fCvAwTLCWCO0WjDkzAFQze8LdC6iOpKbetDKHIuDfIgMlIzYzqZ4nxwLlclQX+3ZVeZ1K2OuaOE2WWcyOg==}

  '@emnapi/runtime@1.9.0':
    resolution: {integrity: sha512-QN75eB0IH2ywSpRpNddCRfQIhmJYBCJ1x5Lb3IscKAL8bMnVAKnRg8dCoXbHzVLLH7P38N2Z3mtulB7W0J0FKw==}

  '@esbuild/aix-ppc64@0.25.12':
    resolution: {integrity: sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/aix-ppc64@0.27.4':
    resolution: {integrity: sha512-cQPwL2mp2nSmHHJlCyoXgHGhbEPMrEEU5xhkcy3Hs/O7nGZqEpZ2sUtLaL9MORLtDfRvVl2/3PAuEkYZH0Ty8Q==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.25.12':
    resolution: {integrity: sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm64@0.27.4':
    resolution: {integrity: sha512-gdLscB7v75wRfu7QSm/zg6Rx29VLdy9eTr2t44sfTW7CxwAtQghZ4ZnqHk3/ogz7xao0QAgrkradbBzcqFPasw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.25.12':
    resolution: {integrity: sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-arm@0.27.4':
    resolution: {integrity: sha512-X9bUgvxiC8CHAGKYufLIHGXPJWnr0OCdR0anD2e21vdvgCI8lIfqFbnoeOz7lBjdrAGUhqLZLcQo6MLhTO2DKQ==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.25.12':
    resolution: {integrity: sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/android-x64@0.27.4':
    resolution: {integrity: sha512-PzPFnBNVF292sfpfhiyiXCGSn9HZg5BcAz+ivBuSsl6Rk4ga1oEXAamhOXRFyMcjwr2DVtm40G65N3GLeH1Lvw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.25.12':
    resolution: {integrity: sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-arm64@0.27.4':
    resolution: {integrity: sha512-b7xaGIwdJlht8ZFCvMkpDN6uiSmnxxK56N2GDTMYPr2/gzvfdQN8rTfBsvVKmIVY/X7EM+/hJKEIbbHs9oA4tQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.25.12':
    resolution: {integrity: sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/darwin-x64@0.27.4':
    resolution: {integrity: sha512-sR+OiKLwd15nmCdqpXMnuJ9W2kpy0KigzqScqHI3Hqwr7IXxBp3Yva+yJwoqh7rE8V77tdoheRYataNKL4QrPw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.25.12':
    resolution: {integrity: sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-arm64@0.27.4':
    resolution: {integrity: sha512-jnfpKe+p79tCnm4GVav68A7tUFeKQwQyLgESwEAUzyxk/TJr4QdGog9sqWNcUbr/bZt/O/HXouspuQDd9JxFSw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.25.12':
    resolution: {integrity: sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.27.4':
    resolution: {integrity: sha512-2kb4ceA/CpfUrIcTUl1wrP/9ad9Atrp5J94Lq69w7UwOMolPIGrfLSvAKJp0RTvkPPyn6CIWrNy13kyLikZRZQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.25.12':
    resolution: {integrity: sha512-8bwX7a8FghIgrupcxb4aUmYDLp8pX06rGh5HqDT7bB+8Rdells6mHvrFHHW2JAOPZUbnjUpKTLg6ECyzvas2AQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm64@0.27.4':
    resolution: {integrity: sha512-7nQOttdzVGth1iz57kxg9uCz57dxQLHWxopL6mYuYthohPKEK0vU0C3O21CcBK6KDlkYVcnDXY099HcCDXd9dA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.25.12':
    resolution: {integrity: sha512-lPDGyC1JPDou8kGcywY0YILzWlhhnRjdof3UlcoqYmS9El818LLfJJc3PXXgZHrHCAKs/Z2SeZtDJr5MrkxtOw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-arm@0.27.4':
    resolution: {integrity: sha512-aBYgcIxX/wd5n2ys0yESGeYMGF+pv6g0DhZr3G1ZG4jMfruU9Tl1i2Z+Wnj9/KjGz1lTLCcorqE2viePZqj4Eg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.25.12':
    resolution: {integrity: sha512-0y9KrdVnbMM2/vG8KfU0byhUN+EFCny9+8g202gYqSSVMonbsCfLjUO+rCci7pM0WBEtz+oK/PIwHkzxkyharA==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-ia32@0.27.4':
    resolution: {integrity: sha512-oPtixtAIzgvzYcKBQM/qZ3R+9TEUd1aNJQu0HhGyqtx6oS7qTpvjheIWBbes4+qu1bNlo2V4cbkISr8q6gRBFA==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.25.12':
    resolution: {integrity: sha512-h///Lr5a9rib/v1GGqXVGzjL4TMvVTv+s1DPoxQdz7l/AYv6LDSxdIwzxkrPW438oUXiDtwM10o9PmwS/6Z0Ng==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-loong64@0.27.4':
    resolution: {integrity: sha512-8mL/vh8qeCoRcFH2nM8wm5uJP+ZcVYGGayMavi8GmRJjuI3g1v6Z7Ni0JJKAJW+m0EtUuARb6Lmp4hMjzCBWzA==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os
... [TRUNCATED]
```

### File: pnpm-workspace.yaml
```yaml
packages:
  - 'understand-anything-plugin/packages/*'
  - 'understand-anything-plugin'
  - 'homepage'

```

### File: README.ja-JP.md
```md
<h1 align="center">Understand Anything</h1>

<p align="center">
  <strong>あらゆるコードベースを、探索・検索・質問ができるインタラクティブなナレッジグラフに変換します。</strong>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ja-JP.md">日本語</a> | <a href="README.tr-TR.md">Türkçe</a>
</p>

<p align="center">
  <a href="#-クイックスタート"><img src="https://img.shields.io/badge/Quick_Start-blue" alt="クイックスタート" /></a>
  <a href="https://github.com/Lum1104/Understand-Anything/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT" /></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Claude_Code-Plugin-8A2BE2" alt="Claude Code Plugin" /></a>
  <a href="https://lum1104.github.io/Understand-Anything"><img src="https://img.shields.io/badge/Homepage-d4a574" alt="ホームページ" /></a>
  <a href="https://lum1104.github.io/Understand-Anything/demo/"><img src="https://img.shields.io/badge/Live_Demo-00c853" alt="ライブデモ" /></a>
</p>

<p align="center">
  <img src="assets/hero.jpg" alt="Understand Anything — あらゆるコードベースをインタラクティブなナレッジグラフに変換" width="800" />
</p>

---

> [!TIP]
> **コミュニティの皆さんに感謝！** Understand-Anythingへのサポートは本当に素晴らしいものです。このツールが複雑なコードを理解する時間を少しでも短縮できたなら、それが私の望みです。🚀

**新しいチームに参加したばかり。コードベースは20万行。どこから手をつければいいのか？**

Understand Anything は [Claude Code](https://docs.anthropic.com/en/docs/claude-code) プラグインです。マルチエージェントパイプラインでプロジェクトを分析し、すべてのファイル・関数・クラス・依存関係のナレッジグラフを構築して、インタラクティブなダッシュボードで視覚的に探索できるようにします。コードを闇雲に読むのはやめて、全体像を把握しましょう。

---

## 🤔 なぜ必要なのか？

コードを読むのは大変です。コードベース全体を理解するのはさらに大変です。ドキュメントは常に古く、オンボーディングには数週間かかり、新機能の開発はまるで考古学のようです。

Understand Anything は、**LLMの知能**と**静的解析**を組み合わせることでこの問題を解決します。プロジェクトの生きた探索可能なマップを生成し、すべてに平易な日本語の説明が付きます。

---

## 🎯 誰のためのツール？

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>👩‍💻 ジュニア開発者</h3>
      <p>不慣れなコードに溺れるのはもう終わり。アーキテクチャをステップバイステップで案内するガイドツアーで、すべての関数やクラスが平易な言葉で説明されます。</p>
    </td>
    <td width="33%" valign="top">
      <h3>📋 プロダクトマネージャー＆デザイナー</h3>
      <p>コードを読まなくても、システムが実際にどう動くかを理解できます。「認証はどう動いているの？」のような質問をすれば、実際のコードベースに基づいた明確な回答が得られます。</p>
    </td>
    <td width="33%" valign="top">
      <h3>🤖 AI活用開発者</h3>
      <p>AIツールにプロジェクトの深いコンテキストを与えましょう。コードレビュー前に <code>/understand-diff</code>、モジュールの詳細調査に <code>/understand-explain</code>、アーキテクチャの推論に <code>/understand-chat</code> を使えます。</p>
    </td>
  </tr>
</table>

---

## 🚀 クイックスタート

### 1. プラグインをインストール

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### 2. コードベースを分析

```bash
/understand
```

マルチエージェントパイプラインがプロジェクトをスキャンし、すべてのファイル・関数・クラス・依存関係を抽出して、`.understand-anything/knowledge-graph.json` にナレッジグラフを保存します。

### 3. ダッシュボードで探索

```bash
/understand-dashboard
```

インタラクティブなWebダッシュボードが開き、コードベースがグラフとして可視化されます。アーキテクチャ層ごとに色分けされ、検索やクリックが可能です。ノードを選択すると、コード・関連関係・平易な説明が表示されます。

### 4. さらに学ぶ

```bash
# コードベースについて何でも質問
/understand-chat 支払いフローはどう動いているの？

# 現在の変更の影響を分析
/understand-diff

# 特定のファイルや関数を詳しく調べる
/understand-explain src/auth/login.ts

# 新メンバー向けのオンボーディングガイドを生成
/understand-onboard

# ビジネスドメイン知識を抽出（ドメイン、フロー、ステップ）
/understand-domain
```

---

## 🌐 マルチプラットフォームインストール

Understand-Anythingは複数のAIコーディングプラットフォームで動作します。

### Claude Code（ネイティブ）

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### Codex

Codexに以下を伝えてください：
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.codex/INSTALL.md
```

### OpenCode

OpenCodeに以下を伝えてください：
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.opencode/INSTALL.md
```

### OpenClaw

OpenClawに以下を伝えてください：
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.openclaw/INSTALL.md
```

### Cursor

Cursorはこのリポジトリをクローンすると `.cursor-plugin/plugin.json` 経由でプラグインを自動検出します。手動インストールは不要です — クローンしてCursorで開くだけです。

### VS Code + GitHub Copilot

GitHub Copilot拡張機能（v1.108+）をインストールしたVS Codeは、`.copilot-plugin/plugin.json` 経由でプラグインを自動検出します。クローンしてVS Codeで開くだけで、手動インストールは不要です。

全プロジェクトで使用するパーソナルスキルとして設定する場合は、GitHub Copilotに以下を伝えてください：
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.vscode/INSTALL.md
```

### Antigravity

Antigravityに以下を伝えてください：
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.antigravity/INSTALL.md
```

### Gemini CLI

Gemini CLIに以下を伝えてください：
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.gemini/INSTALL.md
```

### Pi Agent

Pi Agentに以下を伝えてください：
```text
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.pi/INSTALL.md
```

### プラットフォーム互換性

| プラットフォーム | ステータス | インストール方法 |
|----------|--------|----------------|
| Claude Code | ✅ ネイティブ | プラグインマーケットプレイス |
| Codex | ✅ サポート | AI駆動インストール |
| OpenCode | ✅ サポート | AI駆動インストール |
| OpenClaw | ✅ サポート | AI駆動インストール |
| Cursor | ✅ サポート | 自動検出 |
| VS Code + GitHub Copilot | ✅ サポート | 自動検出 |
| Antigravity | ✅ サポート | AI駆動インストール |
| Gemini CLI | ✅ サポート | AI駆動インストール |
| Pi Agent | ✅ サポート | AI駆動インストール |

---

## ✨ 機能

<p align="center">
  <img src="assets/overview.png" alt="ダッシュボードスクリーンショット" width="800" />
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🗺️ インタラクティブナレッジグラフ</h3>
      <p>ファイル・関数・クラスとそれらの関係をReact Flowで可視化。ノードをクリックするとコードと接続関係が表示されます。</p>
    </td>
    <td width="50%" valign="top">
      <h3>💬 平易な言葉での説明</h3>
      <p>すべてのノードがLLMによって説明されるため、技術者でなくても、それが何をしているのか、なぜ存在するのかを理解できます。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🧭 ガイドツアー</h3>
      <p>依存関係順に並べられた、自動生成のアーキテクチャウォークスルー。正しい順序でコードベースを学べます。</p>
    </td>
    <td width="50%" valign="top">
      <h3>🔍 ファジー＆セマンティック検索</h3>
      <p>名前や意味で何でも検索できます。「認証を処理する部分は？」と検索すれば、グラフ全体から関連する結果が得られます。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>📊 差分影響分析</h3>
      <p>コミット前に、変更がシステムのどの部分に影響するかを確認。コードベース全体への波及効果を把握できます。</p>
    </td>
    <td width="50%" valign="top">
      <h3>🎭 ペルソナ適応型UI</h3>
      <p>ダッシュボードは、ジュニア開発者・PM・パワーユーザーなど、ユーザーに応じて詳細レベルを調整します。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏗️ レイヤー可視化</h3>
      <p>API・Service・Data・UI・Utilityなどのアーキテクチャ層ごとに自動グループ化。色分けされた凡例付き。</p>
    </td>
    <td width="50%" valign="top">
      <h3>📚 言語コンセプト</h3>
      <p>ジェネリクス・クロージャ・デコレータなど12のプログラミングパターンが、出現箇所のコンテキストで説明されます。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏢 ビジネスドメイン知識</h3>
      <p>コードベースからビジネスドメイン、フロー、処理ステップを抽出。インタラクティブな水平フローグラフでビジネスロジックがコードにどうマッピングされるかを確認 — ドメインにはフロー、フローにはステップが含まれます。</p>
    </td>
    <td width="50%" valign="top">
      <h3>🔀 構造 + ドメインビュー</h3>
      <p>ダッシュボードでコード構造グラフとビジネスドメイングラフを切り替え。コードの組織方法と、それが実装するビジネスプロセスの両方を理解できます。</p>
    </td>
  </tr>
</table>

---

## 🔧 内部の仕組み

### マルチエージェントパイプライン

`/understand` コマンドは5つの専門エージェントをオーケストレーションし、`/understand-domain` は6つ目を追加します：

| エージェント | 役割 |
|-------|------|
| `project-scanner` | ファイルの検出、言語やフレームワークの検出 |
| `file-analyzer` | 関数・クラス・インポートの抽出、グラフノードとエッジの生成 |
| `architecture-analyzer` | アーキテクチャ層の特定 |
| `tour-builder` | ガイド学習ツアーの生成 |
| `graph-reviewer` | グラフの完全性と参照整合性の検証 |
| `domain-analyzer` | ビジネスドメイン、フロー、処理ステップの抽出（`/understand-domain` で使用） |

ファイルアナライザーは並列実行されます（最大3つ同時）。インクリメンタル更新に対応しており、前回の実行から変更されたファイルのみを再分析します。

### プロジェクト構成

```
understand-anything-plugin/
  .claude-plugin/  — プラグインマニフェスト
  agents/          — 専門AIエージェント
  skills/          — スキル定義（/understand、/understand-chatなど）
  src/             — TypeScriptソース（context-builder、diff-analyzerなど）
  packages/
    core/          — 分析エンジン（types、persistence、tree-sitter、search、schema、tours）
    dashboard/     — React + TypeScript Webダッシュボード
```

### 技術スタック

TypeScript、pnpm workspaces、React 18、Vite、TailwindCSS v4、React Flow、Zustand、web-tree-sitter、Fuse.js、Zod、Dagre

### 開発コマンド

| コマンド | 説明 |
|---------|-------------|
| `pnpm install` | すべての依存関係をインストール |
| `pnpm --filter @understand-anything/core build` | coreパッケージをビルド |
| `pnpm --filter @understand-anything/core test` | coreテストを実行 |
| `pnpm --filter @understand-anything/skill build` | プラグインパッケージをビルド |
| `pnpm --filter @understand-anything/skill test` | プラグインテストを実行 |
| `pnpm --filter @understand-anything/dashboard build` | ダッシュボードをビルド |
| `pnpm dev:dashboard` | ダッシュボード開発サーバーを起動 |

---

## 🤝 コントリビュート

コントリビュートを歓迎します！始め方は以下の通りです：

1. リポジトリをフォーク
2. フィーチャーブランチを作成（`git checkout -b feature/my-feature`）
3. テストを実行（`pnpm --filter @understand-anything/core test`）
4. 変更をコミットしてプルリクエストを作成

大きな変更については、まずIssueを作成してアプローチを議論してください。

---

<p align="center">
  <strong>コードを闇雲に読むのはやめよう。すべてを理解しよう。</strong>
</p>

## Star History

<a href="https://www.star-history.com/?repos=Lum1104%2FUnderstand-Anything&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />
 </picture>
</a>

<p align="center">
  MIT License &copy; <a href="https://github.com/Lum1104">Lum1104</a>
</p>

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
