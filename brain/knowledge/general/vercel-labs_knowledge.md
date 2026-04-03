---
id: vercel-labs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:40.510612
---

# KNOWLEDGE EXTRACT: vercel-labs
> **Extracted on:** 2026-03-30 17:58:08
> **Source:** vercel-labs

---

## File: `agent-browser.md`
```markdown
# 📦 vercel-labs/agent-browser [🔖 PENDING/APPROVE]
🔗 https://github.com/vercel-labs/agent-browser
🌐 https://agent-browser.dev

## Meta
- **Stars:** ⭐ 25036 | **Forks:** 🍴 1506
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Browser automation CLI for AI agents

## README (trích đầu)
```
# agent-browser

Headless browser automation CLI for AI agents. Fast native Rust CLI.

## Installation

### Global Installation (recommended)

Installs the native Rust binary:

```bash
npm install -g agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### Project Installation (local dependency)

For projects that want to pin the version in `package.json`:

```bash
npm install agent-browser
agent-browser install
```

Then use via `package.json` scripts or by invoking `agent-browser` directly.

### Homebrew (macOS)

```bash
brew install agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### Cargo (Rust)

```bash
cargo install agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### From Source

```bash
git clone https://github.com/vercel-labs/agent-browser
cd agent-browser
pnpm install
pnpm build
pnpm build:native   # Requires Rust (https://rustup.rs)
pnpm link --global  # Makes agent-browser available globally
agent-browser install
```

### Linux Dependencies

On Linux, install system dependencies:

```bash
agent-browser install --with-deps
```

### Updating

Upgrade to the latest version:

```bash
agent-browser upgrade
```

Detects your installation method (npm, Homebrew, or Cargo) and runs the appropriate update command automatically.

### Requirements

- **Chrome** - Run `agent-browser install` to download Chrome from [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) (Google's official automation channel). No Playwright or Node.js required for the daemon.
- **Rust** - Only needed when building from source (see From Source above).

## Quick Start

```bash
agent-browser open example.com
agent-browser snapshot                    # Get accessibility tree with refs
agent-browser click @e2                   # Click by ref from snapshot
agent-browser fill @e3 "test@example.com" # Fill by ref
agent-browser get text @e1                # Get text by ref
agent-browser screenshot page.png
agent-browser close
```

### Traditional Selectors (also supported)

```bash
agent-browser click "#submit"
agent-browser fill "#email" "test@example.com"
agent-browser find role button click --name "Submit"
```

## Commands

### Core Commands

```bash
agent-browser open <url>              # Navigate to URL (aliases: goto, navigate)
agent-browser click <sel>             # Click element (--new-tab to open in new tab)
agent-browser dblclick <sel>          # Double-click element
agent-browser focus <sel>             # Focus element
agent-browser type <sel> <text>       # Type into element
agent-browser fill <sel> <text>       # Clear and fill
agent-browser press <key>             # Press key (Enter, Tab, Control+a) (alias: key)
agent-browser keyboard type <text>    # Type with real keystrokes (no selector, current focus)
agent-browser keyboard inserttext <text>  # Insert text without key events (no sele
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `agent-skills.md`
```markdown
# 📦 vercel-labs/agent-skills [⭐ ACTIVE]
🔗 https://github.com/vercel-labs/agent-skills
🌐 https://skills.sh/vercel-labs/agent-skills

## Meta
- **Stars:** ⭐ 23950 | **Forks:** 🍴 2179
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-27
- **Topics:** (none)
- **Status trong AI OS:** ⭐ ACTIVE

## Description:
Vercel's official collection of agent skills

## README (FULL)
```
# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### react-best-practices

React and Next.js performance optimization guidelines from Vercel Engineering. Contains 40+ rules across 8 categories, prioritized by impact.

**Use when:**
- Writing new React components or Next.js pages
- Implementing data fetching (client or server-side)
- Reviewing code for performance issues
- Optimizing bundle size or load times

**Categories covered:**
- Eliminating waterfalls (Critical)
- Bundle size optimization (Critical)
- Server-side performance (High)
- Client-side data fetching (Medium-High)
- Re-render optimization (Medium)
- Rendering performance (Medium)
- JavaScript micro-optimizations (Low-Medium)

### web-design-guidelines

Review UI code for compliance with web interface best practices. Audits your code for 100+ rules covering accessibility, performance, and UX.

**Use when:**
- "Review my UI"
- "Check accessibility"
- "Audit design"
- "Review UX"
- "Check my site against best practices"

**Categories covered:**
- Accessibility (aria-labels, semantic HTML, keyboard handlers)
- Focus States (visible focus, focus-visible patterns)
- Forms (autocomplete, validation, error handling)
- Animation (prefers-reduced-motion, compositor-friendly transforms)
- Typography (curly quotes, ellipsis, tabular-nums)
- Images (dimensions, lazy loading, alt text)
- Performance (virtualization, layout thrashing, preconnect)
- Navigation & State (URL reflects state, deep-linking)
- Dark Mode & Theming (color-scheme, theme-color meta)
- Touch & Interaction (touch-action, tap-highlight)
- Locale & i18n (Intl.DateTimeFormat, Intl.NumberFormat)

### react-native-guidelines

React Native best practices optimized for AI agents. Contains 16 rules across 7 sections covering performance, architecture, and platform-specific patterns.

**Use when:**
- Building React Native or Expo apps
- Optimizing mobile performance
- Implementing animations or gestures
- Working with native modules or platform APIs

**Categories covered:**
- Performance (Critical) - FlashList, memoization, heavy computation
- Layout (High) - flex patterns, safe areas, keyboard handling
- Animation (High) - Reanimated, gesture handling
- Images (Medium) - expo-image, caching, lazy loading
- State Management (Medium) - Zustand patterns, React Compiler
- Architecture (Medium) - monorepo structure, imports
- Platform (Medium) - iOS/Android specific patterns

### composition-patterns

React composition patterns that scale. Helps avoid boolean prop proliferation through compound components, state lifting, and internal composition.

**Use when:**
- Refactoring components with many boolean props
- Building reusable component libraries
- Designing flexible APIs
- Reviewing component architecture

**Patterns covered:**
- Extracting compound components
- Lifting state to reduce props
- Composing internals for flexibility
- Avoiding prop drilling

### vercel-deploy-claimable

Deploy applications and websites to Vercel instantly. Designed for use with claude.ai and Claude Desktop to enable deployments directly from conversations. Deployments are "claimable" - users can transfer ownership to their own Vercel account.

**Use when:**
- "Deploy my app"
- "Deploy this to production"
- "Push this live"
- "Deploy and give me the link"

**Features:**
- Auto-detects 40+ frameworks from `package.json`
- Returns preview URL (live site) and claim URL (transfer ownership)
- Handles static HTML projects automatically
- Excludes `node_modules` and `.git` from uploads

**How it works:**
1. Packages your project into a tarball
2. Detects framework (Next.js, Vite, Astro, etc.)
3. Uploads to deployment service
4. Returns preview URL and claim URL

**Output:**
```
Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...
```

## Installation

```bash
npx skills add vercel-labs/agent-skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
```
Deploy my app
```
```
Review this React component for performance issues
```
```
Help me optimize this Next.js page
```

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API FULL | Owner: Dept 07 Knowledge*
```

## File: `next-skills.md`
```markdown
# 📦 vercel-labs/next-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/vercel-labs/next-skills


## Meta
- **Stars:** ⭐ 773 | **Forks:** 🍴 49
- **Language:** N/A | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Next.js Agent Skills

Agent skills for common Next.js workflows.

## Essential Skills

Start here. These background skills are auto-applied to prevent common mistakes.

### `next-best-practices`

Core Next.js knowledge:

- [File Conventions](./skills/next-best-practices/file-conventions.md) - Project structure and special files
- [RSC Boundaries](./skills/next-best-practices/rsc-boundaries.md) - Server/Client Component rules
- [Data Patterns](./skills/next-best-practices/data-patterns.md) - Fetching and mutation strategies
- [Async Patterns](./skills/next-best-practices/async-patterns.md) - Next.js 15+ async APIs
- [Directives](./skills/next-best-practices/directives.md) - `'use client'`, `'use server'`, `'use cache'`
- [Functions](./skills/next-best-practices/functions.md) - Navigation hooks, server functions, generate functions
- [Runtime Selection](./skills/next-best-practices/runtime-selection.md) - Node.js vs Edge runtime
- [Error Handling](./skills/next-best-practices/error-handling.md) - Error boundaries and redirects
- [Route Handlers](./skills/next-best-practices/route-handlers.md) - API routes with `route.ts`
- [Metadata](./skills/next-best-practices/metadata.md) - SEO, OG images, sitemaps
- [Image](./skills/next-best-practices/image.md) - `next/image` optimization
- [Font](./skills/next-best-practices/font.md) - `next/font` optimization
- [Bundling](./skills/next-best-practices/bundling.md) - Package compatibility, CSS imports, polyfills
- [Scripts](./skills/next-best-practices/scripts.md) - Third-party scripts, Google Analytics
- [Hydration Errors](./skills/next-best-practices/hydration-error.md) - Debugging mismatches
- [Suspense Boundaries](./skills/next-best-practices/suspense-boundaries.md) - CSR bailout, Cache Components requirements
- [Parallel Routes](./skills/next-best-practices/parallel-routes.md) - Modal patterns with intercepting routes
- [Self-Hosting](./skills/next-best-practices/self-hosting.md) - Docker, standalone output, ISR
- [Debug Tricks](./skills/next-best-practices/debug-tricks.md) - MCP endpoint, rebuild specific routes

## Installation

```bash
# Install essentials (recommended)
npx skills add vercel-labs/next-skills --skill next-best-practices

# Or install everything
npx skills add vercel-labs/next-skills
```

## Advanced Use Cases

Optional skills for specific needs. Invoke via slash commands.

### `next-upgrade`

Upgrading between Next.js versions with official migration guides.

```bash
npx skills add vercel-labs/next-skills --skill next-upgrade
```

### `next-cache-components`

Next.js 16 Cache Components and PPR. Covers `cacheComponents: true`, `'use cache'` directive, cache profiles, `cacheLife()`, `cacheTag()`, and `updateTag()`.

```bash
npx skills add vercel-labs/next-skills --skill next-cache-components
```

## Usage

**Background skills** (`next-best-practices`) are automatically applied when relevant.

**Slash commands** for advanced skills:

```
/next-upgrade
/next-cache-components
```

## Rela
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `skills.md`
```markdown
# 📦 vercel-labs/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/vercel-labs/skills
🌐 https://skills.sh

## Meta
- **Stars:** ⭐ 11886 | **Forks:** 🍴 963
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The open agent skills tool - npx skills

## README (trích đầu)
```
# skills

The CLI for the open agent skills ecosystem.

<!-- agent-list:start -->
Supports **OpenCode**, **Claude Code**, **Codex**, **Cursor**, and [39 more](#available-agents).
<!-- agent-list:end -->

## Install a Skill

```bash
npx skills add vercel-labs/agent-skills
```

### Source Formats

```bash
# GitHub shorthand (owner/repo)
npx skills add vercel-labs/agent-skills

# Full GitHub URL
npx skills add https://github.com/vercel-labs/agent-skills

# Direct path to a skill in a repo
npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

# GitLab URL
npx skills add https://gitlab.com/org/repo

# Any git URL
npx skills add git@github.com:vercel-labs/agent-skills.git

# Local path
npx skills add ./my-local-skills
```

### Options

| Option                    | Description                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-g, --global`            | Install to user directory instead of project                                                                                                       |
| `-a, --agent <agents...>` | <!-- agent-names:start -->Target specific agents (e.g., `claude-code`, `codex`). See [Available Agents](#available-agents)<!-- agent-names:end --> |
| `-s, --skill <skills...>` | Install specific skills by name (use `'*'` for all skills)                                                                                         |
| `-l, --list`              | List available skills without installing                                                                                                           |
| `--copy`                  | Copy files instead of symlinking to agent directories                                                                                              |
| `-y, --yes`               | Skip all confirmation prompts                                                                                                                      |
| `--all`                   | Install all skills to all agents without prompts                                                                                                   |

### Examples

```bash
# List skills in a repository
npx skills add vercel-labs/agent-skills --list

# Install specific skills
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# Install a skill with spaces in the name (must be quoted)
npx skills add owner/repo --skill "Convex Best Practices"

# Install to specific agents
npx skills add vercel-labs/agent-skills -a claude-code -a opencode

# Non-interactive installation (CI/CD friendly)
npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# Install all skills from a repo to all a
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

