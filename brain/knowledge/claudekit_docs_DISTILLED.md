---
id: claudekit-docs
type: knowledge
owner: OA_Triage
---
# claudekit-docs
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "claudekit-docs",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev 2>&1 | tee logs.txt",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/check": "^0.9.6",
    "@astrojs/mdx": "4.3.13",
    "@astrojs/react": "4.4.2",
    "@astrojs/tailwind": "^6.0.2",
    "@radix-ui/react-collapsible": "^1.1.2",
    "@radix-ui/react-dialog": "^1.1.4",
    "@radix-ui/react-dropdown-menu": "^2.1.4",
    "@radix-ui/react-scroll-area": "^1.2.2",
    "astro": "5.17.1",
    "astro-pagefind": "^1.8.5",
    "openai": "^4.75.1",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-markdown": "^10.1.0",
    "rehype-autolink-headings": "^7.1.0",
    "rehype-katex": "^7.0.1",
    "rehype-slug": "^6.0.0",
    "remark-gfm": "^4.0.0",
    "remark-math": "^6.0.0",
    "tailwindcss": "^3.4.17"
  },
  "overrides": {
    "baseline-browser-mapping": "^2.9.19"
  },
  "devDependencies": {
    "@types/react": "^18.3.17",
    "@types/react-dom": "^18.3.5",
    "remark-directive": "^4.0.0",
    "typescript": "^5.9.3",
    "unist-util-visit": "^5.0.0"
  }
}

```

### File: README.md
```md
# ClaudeKit Documentation

Official documentation website for ClaudeKit - AI-powered development toolkit with Claude.

🌐 **Live Site**: https://docs.claudekit.cc
📦 **Version**: 0.0.1 (MVP)
🚀 **Status**: Development

[![Code Hunt 2025](https://img.shields.io/badge/🎄_Code_Hunt_2025-FR0STYC0DE-brightgreen)](https://claudekit.cc)

---

## Overview

Modern documentation platform built with Astro v5, featuring bi-lingual content (EN/VI), AI assistant UI, collapsible navigation, and One Dark Pro-inspired design.

### Key Features

- ✨ **AI Assistant**: Interactive chat panel (UI complete, backend pending)
- 📝 **Type-Safe Content**: Zod-validated markdown, automatic routes
- 🎨 **Beautiful Design**: One Dark Pro theme, Polar docs aesthetics
- 📱 **Fully Responsive**: Mobile-first, adaptive 1/2/3-column layouts
- ⚡ **Blazing Fast**: Static generation, minimal JavaScript (< 200KB)
- 🌍 **Bi-Lingual**: English + Vietnamese, easy to add more locales
- ♿ **Accessible**: WCAG 2.1 AA compliant, keyboard navigation
- 🐳 **Production Ready**: Docker + Kubernetes with HA setup

---

## Technology Stack

**Core**: Astro v5.14.6, React 18.3.1, TypeScript 5.7.3, Node.js 20
**Styling**: Tailwind CSS 3.4, CSS Variables, Shiki (One Dark Pro)
**Content**: Astro Content Collections, Zod validation, GFM, Math equations
**UI**: Radix UI (Collapsible, Dialog, Dropdown, ScrollArea)
**Deployment**: Docker (multi-stage), Kubernetes (2 replicas), nginx-ingress, cert-manager

---

## Quick Start

### Prerequisites

- Node.js 20+
- npm 10+
- Git

### Local Development

```bash
# Clone repo
git clone https://github.com/claudekit/claudekit-docs.git
cd claudekit-docs

# Install dependencies
npm install

# Start dev server (http://localhost:4321)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Docker Development

```bash
# Build image
docker build -t claudekit-docs:local .

# Run container
docker run -d --name claudekit-docs -p 3000:3000 claudekit-docs:local

# View logs
docker logs claudekit-docs -f
```

---

## Project Structure

```
claudekit-docs/
├── src/
│   ├── components/          # Astro + React components
│   ├── content/
│   │   ├── docs/            # English docs (97 pages)
│   │   ├── docs-vi/         # Vietnamese docs (97 pages)
│   │   └── config.ts        # Zod schema
│   ├── i18n/                # Locales, translations, utils
│   ├── layouts/             # BaseLayout, DocsLayout
│   ├── lib/                 # Utilities (OpenRouter client)
│   ├── pages/               # File-based routing
│   └── styles/              # Global CSS (design tokens)
├── public/                  # Static assets (logos, images)
├── k8s/                     # Kubernetes manifests
├── docs/                    # Project documentation
│   ├── codebase-summary.md
│   ├── code-standards.md
│   ├── system-architecture.md
│   └── project-roadmap.md
├── astro.config.mjs         # Astro config
├── CLAUDE.md                # AI assistant instructions
├── Dockerfile               # Multi-stage build
├── package.json             # Dependencies
└── README.md                # This file
```

---

## Adding Documentation

### Create New Page

1. **Add markdown file** in `src/content/docs/<category>/`

```markdown
---
title: "Your Page Title"
description: "SEO description (150-160 chars)"
category: "getting-started"
order: 1
published: true
---

# Your Page Title

Brief intro paragraph.

## Section

Content with [links](https://example.com) and **formatting**.

\```typescript
// Code blocks with syntax highlighting
const example: string = 'Hello';
\```
```

2. **Route auto-generated** from file path:
   - `src/content/docs/getting-started/intro.md` → `/docs/getting-started/intro`

3. **Add Vietnamese translation** (optional):
   - Mirror file in `src/content/docs-vi/<category>/<slug>.md`

### Valid Categories

- `getting-started` - Onboarding, installation, quick-start
- `cli` - CLI documentation
- `core-concepts` - Architecture, workflows
- `agents` - Agent documentation (14 agents)
- `commands` - Slash commands (25+ commands)
- `skills` - Built-in skills (15+ skills)
- `use-cases` - Real-world tutorials
- `troubleshooting` - Common issues
- `components` - (Future) UI components

---

## Content Statistics

- **Total Pages**: 561 documentation pages (357 EN + 204 VI)
  - **Engineer Kit**: 138 pages (18 agents + 66 commands + 49 skills + 4 configuration + 1 index + docs)
  - **Marketing Kit**: 156 pages (33 agents + 23 commands + 99 skills + 11 workflows + features)
    - All 99 marketing skills fully documented in English and Vietnamese
  - **CLI Kit**: 9 pages (commands, setup, reference)
  - **Getting Started**: Complete onboarding guides with quick-start tutorials
  - **Workflows**: Cross-kit workflow documentation with practical guides
  - **Tools & Support**: Troubleshooting, FAQ, and community support resources
  - **Changelog**: Version history and release notes
- **Vietnamese Coverage**: ~57% (204/357 pages translated, actively expanding)
- **Build Status**: PASSING - 561 pages generated, 0 errors

---

## Development

### Available Scripts

```bash
npm run dev       # Dev server (http://localhost:4321)
npm run build     # Production build → dist/
npm run preview   # Preview build
npm run astro     # Astro CLI
```

### Key Files

- `src/content/config.ts` - Content schema (Zod validation)
- `astro.config.mjs` - Astro config (integrations, markdown plugins)
- `tailwind.config.mjs` - Tailwind config (CSS variable mappings)
- `src/styles/global.css` - Design system (CSS variables)
- `src/i18n/ui.ts` - Translation strings

### Component Development

**Astro Components** (`.astro`):
- Static content and layouts
- Server-side rendering at build time
- Use for non-interactive UI

**React Islands** (`.tsx`):
- Interactive components only
- Client-side hydration
- Use `client:load`, `client:idle`, or `client:visible`

---

## Deployment

### Kubernetes (Production)

```bash
# Prerequisites: kubectl configured, nginx-ingress, cert-manager

# Create registry secret
kubectl create secret docker-registry github-registry \
  --docker-server=ghcr.io \
  --docker-username=YOUR_USERNAME \
  --docker-password=YOUR_TOKEN \
  --docker-email=YOUR_EMAIL

# Deploy
kubectl apply -f k8s/

# Verify
kubectl get pods -l app=claudekit-docs
kubectl get ingress claudekit-docs
```

See [Deployment Guide](./docs/deployment-guide.md) for details.

### Static Hosting

Deploy `dist/` to:
- Vercel
- Netlify
- Cloudflare Pages
- GitHub Pages

No special config needed (pure static site).

---

## Configuration

### Astro Config

- **Integrations**: MDX, React, Tailwind
- **i18n**: EN (default), VI (prefix: `/vi/`)
- **Markdown**: GFM, math equations, auto-link headings
- **Syntax Highlighting**: Shiki (One Dark Pro)
- **Output**: Static (SSG)

### Tailwind Config

- **Content**: All files in `src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}`
- **Dark Mode**: Data attribute (`[data-theme="dark"]`)
- **Theme**: Colors, spacing mapped to CSS variables
- **Plugins**: None (vanilla Tailwind)

---

## Current Status

### Completed ✅

- 561 documentation pages (357 EN + 204 VI) across 3 kits
- Kit-agnostic content architecture with Engineer/Marketing/CLI sections
- Comprehensive 8 content categories (getting-started, cli, engineer, marketing, workflows, tools, support, changelog)
- All 99 marketing skills documented in English and Vietnamese
- Responsive 3-column layout with mobile adaptation
- Context-aware sidebar navigation with kit switcher
- AI chat UI with OpenRouter integration (UI complete, backend pending)
- Language switcher with full bilingual support
- Docker + Kubernetes HA setup with 2 replicas
- Complete project documentation (codebase summary, standards, architecture, roadmap)
- URL redirect system for legacy content
- Pagefind search integration
- Production-ready build system

### In Progress 🔄

- Production deployment to docs.claudekit.cc
- AI chat backend integration via OpenRouter
- Search optimization with Pagefind indexing
- Vietnamese translation gap closure (targeting 100% coverage)

### Known Issues 🐛

- AI chat backend connection pending OpenRouter setup
- Some marketing skills have ~40% translation gap in Vietnamese (actively being filled)
- Engineer Skills category has ~2% translation gap (1/49 pages)
- `troubleshooting` category exists in schema but missing from SidebarNav navigation

---

## Roadmap

**Phase 1** (Q4 2025): Production deployment, Pagefind search, fix known issues
**Phase 2** (Q1 2026): OpenRouter AI backend, hierarchical navigation, analytics
**Phase 3** (Q2 2026): Theme toggle, community contributions, performance tuning
**Phase 4** (Q3 2026): Versioned docs, additional locales (ES, FR, DE, ZH)
**Phase 5** (Q4 2026): Enterprise features, HA, advanced AI

See [Project Roadmap](./docs/project-roadmap.md) for details.

---

## Documentation

Comprehensive docs in `docs/` directory:

- **[Codebase Summary](./docs/codebase-summary.md)** - Complete overview, 194 pages, tech stack
- **[Code Standards](./docs/code-standards.md)** - Naming, file org, patterns, quality
- **[System Architecture](./docs/system-architecture.md)** - SSG + islands, build/runtime layers
- **[Project Roadmap](./docs/project-roadmap.md)** - Status, phases, goals, issues
- **[Design Guidelines](./docs/design-guidelines.md)** - Design system specs (49KB)
- **[Deployment Guide](./docs/deployment-guide.md)** - K8s deployment, Docker, static hosting
- **[Tech Stack](./docs/tech-stack.md)** - Technology decisions, comparisons

---

## Related Projects

- **[ClaudeKit CLI](https://github.com/mrgoonie/claudekit-cli)** - CLI setup tool
- **[ClaudeKit Engineer](https://github.com/claudekit/claudekit-engineer)** - Engineering toolkit
- **[ClaudeKit Marketing](https://github.com/claudekit/claudekit-marketing)** - Marketing toolkit
- **[ClaudeKit](https://github.com/mrgoonie/claudekit)** - Main website

---

## Contributing

Contributions welcome! Please:

1. Read [Code Standards](./docs/code-standards.md)
2. Create branch: `feat/your-feature` or `fix/your-fix`
3. Follow TypeScript strict mode, conventional commits
4. Test locally: `npm run dev` and `npm run build`
5. Submit PR with description

---

## License

MIT License - see LICENSE file for details

---

## Support

- **Documentation**: See `docs/` directory
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions

---

**Last Updated**: 2026-03-03
**Maintainers**: ClaudeKit Team
**Build Status**: PASSING (561 pages, 0 errors)

```

### File: CLAUDE.md
```md
# ClaudeKit Docs

Astro v5 static docs site for ClaudeKit. Live: https://docs.claudekit.cc

## CRITICAL: Quality Gate

**MUST pass before ANY commit/PR. No exceptions.**

```bash
bun run build
```

**Build must pass before commit/PR. No exceptions.**

## Quick Commands

```bash
# Development
bun install           # Install deps
bun run dev           # Dev server → http://localhost:4321
bun run build         # Production build → dist/
bun run preview       # Preview build
```

## Key Locations

- **Content**: `src/content/docs/` (EN), `src/content/docs-vi/` (VI)
- **Components**: `src/components/` (Astro + React islands)
- **Nav config**: `src/lib/sidebar-nav-section-config.ts` (section registry)
- **Link validator**: `src/integrations/build-time-internal-link-validator.ts`
- **Layouts**: `src/layouts/` (BaseLayout, DocsLayout)
- **i18n**: `src/i18n/` (locales, translations, utils)
- **Config**: `src/content/config.ts` (Zod schema)
- **Docs**: `docs/` (codebase-summary, code-standards, system-architecture, project-roadmap)

## Related Projects & Directories

- **[ClaudeKit CLI](https://github.com/mrgoonie/claudekit-cli)** - CLI setup tool
  Location: `../claudekit-cli`
- **[ClaudeKit Engineer](https://github.com/claudekit/claudekit-engineer)** - Engineering toolkit
  Location: `../claudekit-engineer`
- **[ClaudeKit Marketing](https://github.com/claudekit/claudekit-marketing)** - Marketing toolkit
  Location: `../claudekit-marketing`
- **[ClaudeKit](https://github.com/mrgoonie/claudekit)** - Main website
  Location: `../claudekit`

## Adding Documentation

1. Create markdown file: `src/content/docs/<category>/<slug>.md`
2. Add frontmatter:
```yaml
---
title: "Page Title"
description: "SEO description (150-160 chars)"
category: "getting-started"  # See valid categories below
order: 1                      # Lower = higher in nav
published: true
---
```
3. Dev server auto-reloads
4. Optionally add Vietnamese: `src/content/docs-vi/<category>/<slug>.md`

## Valid Sections & Categories

**Sections** (top-level sidebar groups, from `SidebarNav.astro`):
- `getting-started`, `docs`, `engineer`, `marketing`, `cli`, `workflows`, `tools`, `changelog`, `support`

**Categories** (frontmatter `category` field, groups items within a section):
- Use top-level names in nav config's `categoryOrder` (e.g., `commands`, `skills`, `agents`)
- Subcategories like `commands/core`, `skills/backend` auto-group under the parent (`commands`, `skills`)
- Do NOT add subcategories to `categoryOrder` — they are handled automatically

**Nav architecture:**
- `SectionNav.astro` — single data-driven component for 7 sections (engineer, marketing, cli, workflows, tools, support, changelog)
- `src/lib/sidebar-nav-section-config.ts` — centralized config registry (categoryOrder, icons, badge, accentColor)
- Do NOT create per-section nav components. Add new sections by adding config to the registry.

## File Routes

- `src/content/docs/getting-started/intro.md` → `/docs/getting-started/intro`
- `src/content/docs-vi/getting-started/intro.md` → `/vi/docs/getting-started/intro`

## CRITICAL: Link Guidelines

**Build-time link validator** (`src/integrations/build-time-internal-link-validator.ts`) runs on every `bun run build` and **fails the build** if any broken internal links are detected. This catches issues before they reach production.

**ALWAYS use absolute paths for internal links. NEVER use relative paths.**

```markdown
# ✅ CORRECT - Absolute paths
[Quick Start](/docs/getting-started/quick-start)
[Commands](/docs/engineer/commands)

# ❌ WRONG - Relative paths (WILL BREAK)
[Quick Start](./quick-start)
[Commands](../docs/engineer/commands/)
```

**Why:** Relative links resolve differently based on trailing slash in URL:
- `/docs/getting-started` + `./quick-start` → `/docs/quick-start` (404!)
- `/docs/getting-started/` + `./quick-start` → `/docs/getting-started/quick-start` (works)

Since Astro serves URLs without trailing slashes by default, relative links break.

**Link validator details:**
- Validates markdown `[text](/docs/...)` and MDX `href="/docs/..."` syntax
- Skips links inside fenced code blocks (triple backticks)
- Strips anchors (`#section`) and query params (`?key=val`) before validation
- Supports `/index` suffix links
- Skips static assets (`.png`, `.jpg`, `.pdf`, etc.)
- Covers both EN (`/docs/...`) and VI (`/vi/docs/...`) links

**When moving docs:** Search for the old path and update all references:
```bash
grep -r "/docs/old/path" src/content/docs/
```
Then run `bun run build` — the validator will catch any links you missed.

## CRITICAL: Static Assets (Images, PDFs, etc.)

**All static assets MUST be placed in `public/` folder. Astro serves from `public/` only.**

```markdown
# ✅ CORRECT - File at public/docs/screenshots/example.png
![Example](/docs/screenshots/example.png)

# ✅ CORRECT - File at public/assets/diagram.jpg
![Diagram](/assets/diagram.jpg)

# ❌ WRONG - File in docs/ folder (NOT public/docs/)
# This path won't resolve! Astro doesn't serve from repo root.
```

**Asset locations:**
- Screenshots: `public/docs/screenshots/`
- General assets: `public/assets/`

**Before commit, verify all image refs resolve:**
```bash
# List all image paths and check each exists in public/
for p in $(grep -rhoP '!\[.*?\]\(\K/[^)]+' src/content/ | sort -u); do
  [ ! -f "public$p" ] && echo "MISSING: $p"
done
```

## Tech Stack

- **Astro v5.14.6**: SSG with islands architecture
- **React 18.3.1**: Interactive components (AIChat, LanguageSwitcher)
- **TypeScript 5.7.3**: Strict mode
- **Tailwind CSS 3.4**: Utility-first + CSS variables
- **Radix UI**: Accessible components
- **Bun**: Package manager & runtime

## Design System

- **Theme**: One Dark Pro (dark mode only)
- **CSS Variables**: `src/styles/global.css` (--color-*, --space-*, --text-*)
- **Fonts**: Inter (body), Geist Mono (code)
- **Inspiration**: Polar docs aesthetics

## CRITICAL: i18n Rules

**Locations:**
- English: `src/content/docs/` → routes `/docs/*`
- Vietnamese: `src/content/docs-vi/` → routes `/vi/docs/*`
- UI strings: `src/i18n/ui.ts`

**Rules by locale:**

| | English (`docs/`) | Vietnamese (`docs-vi/`) |
|---|---|---|
| Frontmatter | NO `lang:` tag | MUST have `lang: vi` |
| Content | English only | Vietnamese only |
| Internal links | `/docs/...` | `/vi/docs/...` |

**Workflow:** Create EN first → mirror structure in `docs-vi/` → translate

**Before commit, verify i18n compliance:**
```bash
# Check: VI files missing lang: vi
grep -rL "lang: vi" src/content/docs-vi/ --include="*.md" | head -20

# Check: EN files with wrong lang tag
grep -rl "lang: vi" src/content/docs/ --include="*.md"

# Check: EN files linking to /vi/docs/
grep -r "/vi/docs/" src/content/docs/ --include="*.md"

# Check: VI files linking to /docs/ (without /vi/ prefix)
grep -rP '\]\(/docs/' src/content/docs-vi/ --include="*.md"
```

## CRITICAL: Skills vs Commands Terminology

**Skills ARE invoked with `/slash` syntax.** The migration from "commands" to "skills" was organizational, NOT syntactical.

| Term | Syntax | Example | Notes |
|------|--------|---------|-------|
| **Skill** | `/skill-name` | `/git`, `/cook`, `/fix` | Migrated from commands, same slash syntax |
| **Command** | `/command-name` | `/plan`, `/ask`, `/test` | Legacy term, still valid |

**Migrated to Skills:** git, fix, cook, scout, design, content, skill-creator, copywriting
**Still called Commands:** plan, ask, test, bootstrap, debug, journal, watzup, kanban, preview

**DO NOT:**
- Replace `/git` with natural language like "use the git skill"
- Remove slash syntax from skill invocations
- Treat skills as non-slash-invocable

**DO:**
- Keep `/git`, `/cook`, `/fix` syntax in docs
- Update links from `/docs/commands/git/` → `/docs/skills/git`
- Replace `/code` with `/cook` (deprecated)

## Git Workflow

```bash
# Feature branch from dev
git checkout dev && git pull origin dev
git checkout -b kai/<feature>

# After work complete
bun run build
git push origin kai/<feature>
# Create PR to dev branch
```

## Commit Convention

- `feat:` → minor version bump
- `fix:` → patch version bump
- `docs:`, `refactor:`, `test:`, `chore:` → no version bump

## Known Issues / TODOs

- [ ] AI chat backend not connected (UI only)
- [ ] Search not implemented (Pagefind planned)
- [x] ~~Sidebar flat nav~~ — Fixed: SectionNav groups subcategories under parent automatically
- [x] ~~`troubleshooting` category missing~~ — Restructured under `support` section
- [x] ~~KaTeX Vietnamese locale warnings~~ — Fixed: disabled `singleDollarTextMath` in remark-math (#87)
- [x] ~~`baseline-browser-mapping` deprecation warning~~ — Fixed: overridden to latest (#87)

## Deployment

- **Docker**: Multi-stage build, node:20-alpine
- **K8s**: `k8s/` manifests (deployment, service, ingress, configmap)
- **Static**: Can deploy to Vercel, Netlify, Cloudflare Pages

## Documentation

See `docs/` directory:
- `codebase-summary.md`: Complete overview, 194 pages, 9 categories
- `code-standards.md`: Naming conventions, file org, component patterns
- `system-architecture.md`: SSG + islands architecture, build/runtime layers
- `project-roadmap.md`: Status, phases, known issues, goals
- `design-guidelines.md`: Design system specs (49KB)
- `deployment-guide.md`: Production deployment

```

### File: docs_DISTILLED.md
```md
---
id: docs
type: distilled_knowledge
---
# docs

## SWALLOW ENGINE DISTILLATION

### File: code-standards.md
```md
# Code Standards

**Last Updated**: 2025-12-30
**Version**: 0.1.0 (Kit-Agnostic Refactor)
**Applies To**: claudekit-docs codebase (20 components, 8 content categories)

## Overview

Coding standards for Astro v5 documentation site. Covers file organization, naming conventions, component patterns, content structure, and quality guidelines.

## Codebase Structure Overview

### Current Component Inventory (20 files)

**Layout Components**:
- `Header.astro` - Top navigation with logo and language switcher
- `Sidebar.astro` - Left sidebar container (responsive mobile/desktop)
- `SidebarNav.astro` - Navigation tree with kit-switching and section detection

**React Islands (Interactive)**:
- `AIChat.tsx` - Chat interface with OpenRouter integration (UI complete)
- `TableOfContents.tsx` - Dynamic heading extraction and navigation
- `CopyForLLMs.tsx` - Export content for LLM consumption
- `LanguageSwitcher.tsx` - EN/VI language switcher with i18n
- `KitSwitcher.tsx` - Switch between Engineer/Marketing/CLI kits
- `KitContext.tsx` - React context for kit state management

**Navigation Components** (Kit-specific):
- `DocsNav.astro` - General docs navigation
- `GettingStartedNav.astro` - Getting started section nav
- `CLINav.astro` - CLI kit section nav
- `EngineerNav.astro` - Engineer kit section nav
- `MarketingNav.astro` - Marketing kit section nav
- `WorkflowsNav.astro` - Workflows section nav
- `ToolsNav.astro` - Tools section nav
- `ChangelogNav.astro` - Changelog section nav
- `SupportNav.astro` - Support section nav

**UI Components**:
- `Search.astro` - Pagefind search interface (placeholder)
- `AIPanel.astro` - AI chat panel wrapper (disabled)

### Content Organization (451 pages)

**8 Main Categories**:
- `getting-started/` - 8+ pages (installation, quick-start, onboarding)
- `cli/` - CLI kit documentation
- `engineer/` - 138 pages (agents: 18, commands: 66, skills: 49, config: 4, index: 1)
- `marketing/` - 88 pages (agents, commands, skills, workflows, features)
- `workflows/` - 20+ cross-kit workflow guides
- `tools/` - Tools directory and references
- `support/` - FAQ, troubleshooting, community resources
- `changelog/` - Version history and release notes

**Vietnamese Coverage**: 176/275 pages (64% - targeting 100%)

### Key Files

- **Configuration**: `astro.config.mjs`, `tailwind.config.mjs`, `tsconfig.json`
- **Content Schema**: `src/content/config.ts` (Zod validation with 8 categories)
- **i18n**: `src/i18n/locales.ts`, `ui.ts` (18 keys × 2 locales), `utils.ts`
- **Deployment**: `Dockerfile` (multi-stage bun→node), `k8s/` manifests

## Core Principles

### YAGNI (You Aren't Gonna Need It)
- Build features when needed, not speculatively
- Avoid premature optimization
- Keep components simple and focused

### KISS (Keep It Simple, Stupid)
- Prefer simple solutions over complex
- Clear code over clever code
- Minimal dependencies

### DRY (Don't Repeat Yourself)
- Extract reusable components
- Use CSS variables for design tokens
- Centralize i18n strings

## File Organization

### Directory Structure

```
src/
├── components/        # UI components (Astro + React)
├── content/          # Markdown content (Zod validated)
│   ├── docs/         # English
│   └── docs-vi/      # Vietnamese
├── i18n/             # Internationalization
├── layouts/          # Page layouts
├── lib/              # Utilities
├── pages/            # File-based routing
└── styles/           # Global CSS
```

### File Naming Conventions

**Components**:
- Astro: PascalCase (e.g., `Header.astro`, `SidebarNav.astro`)
- React: PascalCase (e.g., `AIChat.tsx`, `LanguageSwitcher.tsx`)
- Use descriptive names indicating purpose

**Content**:
- Markdown: kebab-case (e.g., `quick-start.md`, `installation-issues.md`)
- Match URL structure
- Descriptive, lowercase, hyphen-separated

**Utilities**:
- TypeScript: kebab-case (e.g., `openrouter.ts`)
- Config: kebab-case (e.g., `astro.config.mjs`)

**Directories**:
- kebab-case for all directories
- Singular for utilities (e.g., `lib/`, `i18n/`)
- Plural for collections (e.g., `components/`, `layouts/`)

## File Size Limits

**Hard Limits**:
- Astro components: < 300 lines
- React components: < 250 lines
- TypeScript files: < 200 lines
- Markdown docs: < 500 lines (content only, code examples excluded)

**Refactoring Strategy**:
- Extract reusable logic to `lib/`
- Split large components into sub-components
- Create shared hooks for React components
- Use Astro slots for composition

## Naming Conventions

### Variables & Functions

**TypeScript/JavaScript**:
```typescript
// Variables: camelCase
const pageTitle = 'Introduction';
const isPublished = true;

// Functions: camelCase
function generateSlug(title: string) { }
const getLocalizedPath = (path, locale) => { };

// Constants: UPPER_SNAKE_CASE
const MAX_SIDEBAR_DEPTH = 3;
const DEFAULT_LOCALE = 'en';

// Types/Interfaces: PascalCase
interface DocsFrontmatter {
  title: string;
  category: string;
}

type LocaleCode = 'en' | 'vi';
```

**Astro Components**:
```astro
---
// Props: camelCase
interface Props {
  pageTitle: string;
  currentLocale: string;
}
const { pageTitle, currentLocale } = Astro.props;
---
```

### CSS

**Class Names**:
- Use Tailwind utility classes primarily
- Custom classes: kebab-case (e.g., `.sidebar-nav`, `.nav-item`)
- BEM-style for complex components (e.g., `.nav-section__title`)

**CSS Variables**:
```css
/* Design tokens: kebab-case with semantic names */
--color-bg-primary
--color-text-secondary
--space-4
--text-lg
--radius-md
```

### Content Frontmatter

```yaml
---
title: "Page Title"              # Human-readable
description: "SEO description"   # 150-160 chars
category: "getting-started"      # kebab-case enum
order: 1                         # Number for sorting
published: true                  # Boolean
---
```

**Valid Categories** (from `src/content/config.ts`):

**Main Kit-Agnostic Categories**:
- `getting-started` - Installation, quick-start, onboarding
- `cli` - CLI-specific documentation
- `engineer` - Engineer kit docs (agents, commands, skills, config)
- `marketing` - Marketing kit docs (agents, commands, skills, workflows, features)
- `workflows` - Cross-kit workflow guides
- `tools` - Tools directory and references
- `support` - FAQ, troubleshooting, community resources
- `changelog` - Version history and release notes

**Legacy Categories** (kept for backward compatibility):
- `core-concepts` - Architecture and concepts
- `components` - UI component reference (placeholder)

## Component Patterns

### Astro Components

**Structure**:
```astro
---
// 1. Imports
import Layout from '../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

// 2. Props interface
interface Props {
  title: string;
}

// 3. Props extraction
const { title } = Astro.props;

// 4. Data fetching
const docs = await getCollection('docs');

// 5. Logic
const sortedDocs = docs.sort((a, b) => a.data.order - b.data.order);
---

<!-- 6. Template -->
<Layout title={title}>
  <div class="container">
    <!-- Content -->
  </div>
</Layout>

<!-- 7. Scoped styles (if needed) -->
<style>
  .container {
    /* Prefer Tailwind, use scoped CSS for complex cases */
  }
</style>
```

**Best Practices**:
- Use Astro for static content and layout
- Frontmatter for data fetching and processing
- Minimal client-side JavaScript
- Prefer CSS variables over hardcoded values

### React Components (Islands)

**Structure**:
```tsx
import { useState } from 'react';

interface AIChat Props {
  initialMessages?: Message[];
}

export default function AIChat({ initialMessages = [] }: AIChatProps) {
  const [messages, setMessages] = useState(initialMessages);

  // Logic

  return (
    <div className="ai-chat">
      {/* JSX */}
    </div>
  );
}
```

**Client Directives**:
```astro
<!-- Load immediately -->
<AIChat client:load />

<!-- Load when visible -->
<AIChat client:visible />

<!-- Load when idle -->
<AIChat client:idle />

<!-- Only hydrate on interaction -->
<AIChat client:only="react" />
```

**Best Practices**:
- Use islands for interactive components only
- Keep state management simple (useState, useReducer)
- Prefer `client:visible` or `client:idle` for non-critical components
- TypeScript strict mode

**Cross-Component Communication** (Phase 1 - KitSwitcher):
- Use custom DOM events for component-to-component messaging
- Dispatch from React islands, listen in Astro/vanilla JS
- localStorage for persistent state shared across tabs
- Example: `window.dispatchEvent(new CustomEvent('kit-changed', { detail: { kit } }))`

**localStorage Conventions**:
- Use kebab-case keys: `claudekit-selected-kit`, `sidebar-section-${name}`
- Store simple values: strings, booleans, JSON-serialized objects
- Document key format and default values in component comments

### Layout Patterns

**BaseLayout.astro**:
- HTML document structure
- Meta tags, fonts, global scripts
- Theme initialization
- No layout-specific styles

**DocsLayout.astro**:
- Uses BaseLayout
- Defines page structure (sidebar, content, panel)
- Responsive breakpoints
- Grid/Flexbox layout

**Nested Layouts**:
```astro
---
import BaseLayout from './BaseLayout.astro';
---

<BaseLayout {...props}>
  <div class="docs-wrapper">
    <slot />
  </div>
</BaseLayout>
```

## Content Standards

### Markdown Structure

```markdown
---
title: "Clear, Descriptive Title"
description: "SEO-optimized description (150-160 chars)"
category: "appropriate-category"
order: 10
published: true
---

# Page Title (H1 - only one per page)

Brief introduction paragraph (1-3 sentences).

## First Section (H2)

Content with [links](https://example.com) and **formatting**.

### Subsection (H3)

More detailed content.

#### Detail Level (H4)

Avoid H5 and H6.

## Code Examples

\```typescript
// Always specify language
const example: string = 'Hello';
\```

## Lists

- Unordered lists for related items
- Start with dash, space, lowercase
- Parallel structure

1. Ordered lists for sequences
2. Start with number, period, space
3. Complete sentences or fragments (consistent)

## Tables

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value A  | Value B  | Value C  |

## Links

Internal: [Getting Started](./getting-started/introduction)
External: [Astro Docs](https://docs.astro.build)

## Notes

> **Note**: Use blockquotes for notes, warnings, tips.

## See Also

- [Related Doc 1](./related-1)
- [Related Doc 2](./related-2)
```

### Content Guidelines

**Tone**:
- Professional but friendly
- Active voice preferred
- Second person ("you") for instructions
- Present tense

**Formatting**:
- One sentence per line in source (easier diffs)
- Max 80-100 characters per line
- Two spaces after H1, one space after H2-H4
- Consistent list formatting

**Code Blocks**:
- Always specify language
- Include comments for clarity
- Show complete, runnable examples
- Syntax: \```language

**Links**:
- Descriptive anchor text (not "click here")
- Internal links relative (e.g., `./introduction`)
- External links absolute with https://
- Open external links in same tab (users decide)

**Images**:
- Store in `public/` directory
- Reference with `/image-name.png`
- Alt text required
- Optimize for web (<200KB)

## Styling Standards

### Tailwind CSS

**Utility-First Approach**:
```astro
<div class="flex items-center gap-4 p-6 bg-[var(--color-bg-secondary)]">
  <!-- Content -->
</div>
```

**Responsive Design**:
```astro
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- Mobile-first, breakpoints: md (768px), lg (1024px) -->
</div>
```

**Dark Mode**:
```css
/* Use CSS variables, not Tailwind dark: variant */
.element {
  color: var(--color-text-primary);
  background: var(--color-bg-secondary);
}
```

### CSS Variables

**Usage**:
```css
/* Defined in src/styles/global.css */
.custom-component {
  /* Colors */
  color: var(--color-text-primary);
  background: var(--color-bg-secondary);
  border-color: var(--color-border);

  /* Spacing */
  padding: var(--space-4);
  margin-bottom: var(--space-6);
  gap: var(--space-2);

  /* Typography */
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  font-weight: var(--font-medium);

  /* Effects */
  border-radius: var(--radius-md);
  transition: all var(--duration-normal) var(--ease-out);
}
```

**Never Hardcode**:
```css
/* ❌ Bad */
.element {
  color: #abb2bf;
  padding: 16px;
  font-size: 14px;
}

/* ✅ Good */
.element {
  color: var(--color-text-primary);
  padding: var(--space-4);
  font-size: var(--text-sm);
}
```

## i18n Standards

### Translation Keys

**Naming** (`src/i18n/ui.ts`):
```typescript
export const ui = {
  en: {
    'nav.getting-started': 'Getting Started',  // Dot notation
    'search.placeholder': 'Search docs...',
    'button.submit': 'Submit',
  },
  vi: {
    'nav.getting-started': 'Bắt Đầu',
    'search.placeholder': 'Tìm kiếm...',
    'button.submit': 'Gửi',
  }
};
```

**Usage in Components**:
```astro
---
import { useTranslations } from '../i18n/utils';
const t = useTranslations(currentLocale);
---

<button>{t('button.submit')}</button>
```

### Content Localization

**File Structure**:
```
src/content/
├── docs/              # English
│   └── category/
│       └── page.md
└── docs-vi/           # Vietnamese (mirror structure)
    └── category/
        └── page.md
```

**Translation Workflow**:
1. Create English content first
2. Mirror file structure in `docs-vi/`
3. Translate all frontmatter and content
4. Ensure code examples remain consistent
5. Test both locales

## TypeScript Standards

### Type Safety

**Strict Mode** (tsconfig.json):
```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}
```

**Interface Definitions**:
```typescript
// Prefer interfaces for objects
interface DocsFrontmatter {
  title: string;
  description: string;
  category?: Category;
  order?: number;
  published: boolean;
}

// Use type for unions, primitives
type Category =
  | 'getting-started'
  | 'core-concepts'
  | 'agents';

type LocaleCode = 'en' | 'vi';
```

**Type Annotations**:
```typescript
// Explicit return types
function getSlug(title: string): string {
  return title.toLowerCase().replace(/\s+/g, '-');
}

// Inferred types (simple cases)
const locale = 'en'; // Type: string

// Explicit when needed
const locale: LocaleCode = 'en'; // Type: LocaleCode
```

## Quality Standards

### Code Review Checklist

**Functionality**:
- [ ] Features work as specified
- [ ] Edge cases handled
- [ ] Error states covered
- [ ] Responsive on mobile/desktop

**Code Quality**:
- [ ] Follows naming conventions
- [ ] Under file size limits
- [ ] No code duplication
- [ ] TypeScript strict mode passes
- [ ] No unused imports/variables

**Performance**:
- [ ] Minimal client-side JavaScript
- [ ] Images optimized
- [ ] No unnecessary re-renders
- 
... [TRUNCATED]
```

### File: DOCUMENTATION-INDEX.md
```md
# Documentation Index - Phase 1 Complete

**Last Updated**: 2025-12-30
**Status**: Complete and Production Ready

## Quick Navigation

### For Developers (Daily Reference)
Start here for implementation tasks and troubleshooting:
- **[Component Navigation Guide](./docs/component-navigation-guide.md)** - Quick reference for all navigation components

### For Maintainers (Maintenance Tasks)
For keeping the system working and making updates:
- **[Phase 01 Completion Report](./docs/phase-01-header-navigation-completion.md)** - Complete implementation details
- **[Code Standards](./docs/code-standards.md)** - Coding patterns and conventions

### For Architects (System Understanding)
For understanding overall architecture and design:
- **[System Architecture](./docs/system-architecture.md)** - Complete system design, Section 4.2 for navigation
- **[Project Changelog](./docs/project-changelog.md)** - Version history and feature tracking

### For Managers (Project Tracking)
Project status and completion tracking:
- **[Documentation Report](./plans/reports/docs-manager-251230-1912-phase-01-navigation-docs.md)** - Comprehensive report
- **[Phase 01 Summary](./PHASE-01-DOCUMENTATION-SUMMARY.md)** - Quick summary of deliverables

---

## Phase 1: Header Navigation & Routing

### What Was Built
Header navigation with dynamic kit switching enabling users to navigate between Engineer and Marketing documentation sections with persistent state and cross-tab synchronization.

### Components Implemented
1. **Header.astro** - Dynamic Docs link routing based on kit selection
2. **KitSwitcher.tsx** - React island for Engineer/Marketing kit selection
3. **WorkflowsNav.astro** - Enhanced with kit identification badge
4. **Introduction.md** - Updated to feature both kits equally

### Key Features
- Persistent kit selection via localStorage
- Custom event system for component communication
- Cross-tab synchronization
- Mobile responsive design
- Zero performance impact (< 5KB additional JS)

### Documentation Provided
- 2 new comprehensive guides (5,000+ lines total)
- 3 updated architecture/standards documents
- 1 management report with metrics
- Testing checklist with 11 items
- Troubleshooting guide with debug commands
- Maintenance guidelines

---

## File Organization

### Core Documentation
```
docs/
├── phase-01-header-navigation-completion.md      ← Comprehensive completion report
├── component-navigation-guide.md                  ← Daily developer reference
├── system-architecture.md                         ← Includes Section 4.2
├── code-standards.md                              ← Updated with new patterns
├── project-changelog.md                           ← Version tracking
└── codebase-summary.md                            ← Complete codebase overview
```

### Reports
```
plans/reports/
└── docs-manager-251230-1912-phase-01-navigation-docs.md  ← Management report
```

### Implementation Files
```
src/
├── components/
│   ├── Header.astro                              ← Dynamic routing
│   ├── KitSwitcher.tsx                           ← Kit selection
│   └── nav/WorkflowsNav.astro                    ← Kit badge
└── content/docs/getting-started/
    └── introduction.md                            ← Updated content
```

---

## Documentation by Audience

### Frontend Developers
**Primary**: Component Navigation Guide
**Secondary**: Code Standards, System Architecture
**Tools**: Component code examples, typescript patterns, CSS variables

### DevOps/Infrastructure
**Primary**: System Architecture
**Secondary**: Project Changelog
**Tools**: Build verification, deployment readiness, performance metrics

### Product Managers
**Primary**: Phase 01 Summary, Project Changelog
**Secondary**: Documentation Report
**Tools**: Feature list, timeline, metrics, impact analysis

### New Team Members
**Primary**: Component Navigation Guide
**Secondary**: Code Standards, Phase 01 Completion
**Tertiary**: System Architecture
**Path**: Start with guide, use standards as reference, study completion for details

---

## Key Sections by Topic

### Kit Switching Implementation
- **High-level**: System Architecture Section 4.2
- **Reference**: Component Navigation Guide, Kit Detection section
- **Deep-dive**: Phase 01 Completion Report, Technical Specifications
- **Code**: KitSwitcher.tsx component

### Component Communication
- **Best Practices**: Code Standards, Cross-Component Communication section
- **Implementation**: Phase 01 Completion Report, KitSwitcher.tsx
- **Examples**: Component Navigation Guide, Communication Flow section
- **Testing**: Component Navigation Guide, Testing section

### State Management
- **Pattern**: Code Standards, localStorage Conventions
- **Implementation**: KitSwitcher.tsx, Header.astro setupDocsLinkRouting()
- **Persistence**: Component Navigation Guide, State Management Pattern
- **Testing**: Phase 01 Completion Report, Testing Checklist

### Navigation Architecture
- **Overview**: System Architecture Section 4
- **Components**: Component Navigation Guide, Component Details
- **Routing**: System Architecture Section 4.2, Routing Flow diagrams
- **Mobile**: Component Navigation Guide, Mobile Responsive Behavior

---

## Quick Reference

### localStorage Keys
```javascript
'claudekit-selected-kit'      // Kit selection (engineer/marketing)
'sidebar-section-${name}'     // Sidebar collapse state
```

### Event Types
```javascript
'kit-changed'                 // Dispatched on kit selection change
'storage'                     // Browser event for cross-tab sync
```

### Routing
```
Engineer: /docs/engineer/agents
Marketing: /docs/marketing/
```

### Component Files
```
Header.astro         →  /src/components/Header.astro
KitSwitcher.tsx      →  /src/components/KitSwitcher.tsx
WorkflowsNav.astro   →  /src/components/nav/WorkflowsNav.astro
Introduction.md      →  /src/content/docs/getting-started/introduction.md
```

---

## Maintenance Guide

### Adding a New Kit
1. Update KITS array in KitSwitcher.tsx
2. Add routing in Header.astro setupDocsLinkRouting()
3. Create kit-specific navigation section
4. Update Phase 2 documentation

### Debugging Kit Issues
1. Check localStorage: `localStorage.getItem('claudekit-selected-kit')`
2. Verify event dispatch: Listen for 'kit-changed' event
3. Inspect docs link: Check data-engineer-path and data-marketing-path attributes
4. Clear cache: localStorage.clear() and hard refresh

### Performance Monitoring
- Bundle size: < 5KB for navigation code
- localStorage operations: Synchronous but negligible impact
- Event listeners: Properly cleaned up on navigation
- No memory leaks: Verified with browser DevTools

---

## Build & Testing

### Build Verification
```bash
bun run build
# ✓ Completed in 2.04s
# ✓ Generated 464 pages
# ✓ No errors or warnings
```

### Testing Checklist
All 11 items documented and passing:
- Kit switcher display
- Kit persistence
- localStorage updates
- Event dispatch
- Link routing
- Cross-tab sync
- Mobile responsiveness
- Console errors
- Accessibility
- Performance

---

## Future Phases

### Phase 2: Marketing Workflows
- Add marketing-specific navigation section
- Implement marketing workflows nav
- Add marketing kit badge variations
- Create marketing documentation structure

### Phase 3: Enhanced Features
- i18n support for kit switching (Vietnamese)
- Analytics tracking for kit selection
- User preference persistence
- Kit customization interface

### Phase 4+: Expansion
- Support additional kit types
- Advanced kit-specific features
- A/B testing and analytics
- Mobile app integration

---

## Support & Issues

### Common Questions
**See**: Component Navigation Guide, Troubleshooting section

### Debug Commands
**See**: Component Navigation Guide, Debug Commands section

### Performance Concerns
**See**: System Architecture Section 4.2, Performance Notes

### Mobile Issues
**See**: Component Navigation Guide, Mobile Responsive Behavior

---

## Document Versions

| Document | Version | Date | Status |
|----------|---------|------|--------|
| Phase 01 Completion | 1.0.0 | 2025-12-30 | Final |
| Component Navigation Guide | 1.0.0 | 2025-12-30 | Final |
| System Architecture | 0.0.1 | 2025-12-30 | Updated |
| Code Standards | 0.0.1 | 2025-12-30 | Updated |
| Project Changelog | 0.0.4 | 2025-12-30 | Current |
| Documentation Report | 1.0.0 | 2025-12-30 | Final |

---

## Glossary

- **Kit**: Selection between Engineer or Marketing documentation sections
- **KitSwitcher**: React component for selecting active kit
- **localStorage**: Browser API for persistent state storage
- **Custom Event**: JavaScript mechanism for cross-component communication
- **Hydration**: Process of adding interactivity to static HTML
- **Island**: Astro pattern of interactive components in static sites
- **SSG**: Static Site Generation (Astro's primary pattern)

---

## Statistics

- **Documentation Lines Added**: ~5,000 lines
- **Code Examples**: 15+ examples
- **Components Documented**: 4 components
- **Testing Items**: 11 test cases
- **Quality Score**: 100% coverage
- **Build Status**: PASSING
- **Performance Impact**: < 5KB additional JavaScript

---

**Generated**: 2025-12-30
**Maintained By**: Documentation Team
**Last Updated**: 2025-12-30
**Next Review**: After Phase 2 completion

---

## Contact & Support

For documentation updates or questions about Phase 1 implementation:
- **Technical Details**: See Component Navigation Guide
- **Architecture Questions**: See System Architecture
- **Implementation Status**: See Phase 01 Summary
- **Bug Reports**: See Component Navigation Guide Troubleshooting

---

### Generated Files Summary
- Documentation Index: This file
- Phase 01 Summary: PHASE-01-DOCUMENTATION-SUMMARY.md
- Quick Reference: Component Navigation Guide
- Technical Deep-Dive: Phase 01 Completion Report
- Management Report: plans/reports/docs-manager-251230-1912-phase-01-navigation-docs.md

```

### File: src_DISTILLED.md
```md
---
id: src
type: distilled_knowledge
---
# src

## SWALLOW ENGINE DISTILLATION

### File: middleware.ts
```ts
import { defineMiddleware } from 'astro:middleware';

// URL redirect mapping for old paths → new paths
const exactRedirects: Record<string, string> = {
  // Getting Started moves
  '/docs/getting-started/greenfield-projects': '/docs/workflows/new-project',
  '/docs/getting-started/brownfield-projects': '/docs/workflows/existing-project',
  '/docs/getting-started/mcp-setup': '/docs/configuration/mcp-setup',
  '/docs/getting-started/gemini': '/docs/skills/ai/gemini-vision',

  // Core Concepts → Configuration/Docs
  '/docs/core-concepts/claude-md': '/docs/configuration/claude-md',
  '/docs/core-concepts/workflows': '/docs/configuration/workflows',
  '/docs/core-concepts/architecture': '/docs/agents',
  '/docs/core-concepts/code-standards': '/docs/configuration/claude-md',
  '/docs/core-concepts/system-architecture': '/docs/agents',

  // CLI → Docs (no /docs/docs prefix needed - pages now at /docs/cli)
  // '/docs/cli': '/docs/cli', // Same path, no redirect needed
  // '/docs/cli/installation': '/docs/cli/installation', // Same path, no redirect needed

  // Use Cases → Workflows
  '/docs/use-cases': '/docs/workflows',
  '/docs/use-cases/': '/docs/workflows',
  '/docs/use-cases/adding-feature': '/docs/workflows/adding-feature',
  '/docs/use-cases/fixing-bugs': '/docs/workflows/fixing-bugs',
  '/docs/use-cases/building-api': '/docs/workflows/building-api',
  '/docs/use-cases/implementing-auth': '/docs/workflows/implementing-auth',
  '/docs/use-cases/integrating-payment': '/docs/workflows/integrating-payment',
  '/docs/use-cases/optimizing-performance': '/docs/workflows/optimizing-performance',
  '/docs/use-cases/refactoring-code': '/docs/workflows/refactoring-code',
  '/docs/use-cases/understanding-codebases-with-gkg': '/docs/workflows/understanding-codebases',
  '/docs/use-cases/starting-new-project': '/docs/workflows/new-project',
};

export const onRequest = defineMiddleware((context, next) => {
  const { url, redirect } = context;
  const pathname = url.pathname;

  // Check exact matches first
  const exactMatch = exactRedirects[pathname];
  if (exactMatch) {
    return redirect(exactMatch, 301);
  }

  // Handle wildcard: /docs/troubleshooting/* → /docs/support/troubleshooting/*
  if (pathname.startsWith('/docs/troubleshooting')) {
    if (pathname === '/docs/troubleshooting' || pathname === '/docs/troubleshooting/') {
      return redirect('/docs/support/troubleshooting', 301);
    }
    const slug = pathname.replace('/docs/troubleshooting/', '');
    return redirect(`/docs/support/troubleshooting/${slug}`, 301);
  }

  // Handle wildcard: /docs/use-cases/* → /docs/workflows/*
  if (pathname.startsWith('/docs/use-cases/')) {
    const slug = pathname.replace('/docs/use-cases/', '');
    // Try to map to known workflow
    const workflowMap: Record<string, string> = {
      'adding-feature': 'adding-feature',
      'fixing-bugs': 'fixing-bugs',
      'building-api': 'building-api',
      'implementing-auth': 'implementing-auth',
      'integrating-payment': 'integrating-payment',
      'optimizing-performance': 'optimizing-performance',
      'refactoring-code': 'refactoring-code',
    };
    const mappedSlug = workflowMap[slug] || slug;
    return redirect(`/docs/workflows/${mappedSlug}`, 301);
  }

  // Cook command variants → skills/cook
  if (pathname.startsWith('/docs/engineer/commands/core/cook')) {
    return redirect('/docs/engineer/skills/cook', 301);
  }

  // VI: git commands → git skill
  if (pathname.startsWith('/vi/docs/engineer/commands/git/')) {
    return redirect('/vi/docs/engineer/skills/tools/git', 301);
  }

  // VI: fix commands → fix skill
  if (pathname.startsWith('/vi/docs/engineer/commands/fix/')) {
    return redirect('/vi/docs/engineer/skills/tools/fix', 301);
  }

  // VI: cook/code commands → cook skill
  if (pathname.match(/\/vi\/docs\/engineer\/commands\/core\/(cook|code)/)) {
    return redirect('/vi/docs/engineer/skills/tools/cook', 301);
  }

  // VI: scout commands → scout skill
  if (pathname.startsWith('/vi/docs/engineer/commands/core/scout')) {
    return redirect('/vi/docs/engineer/skills/tools/scout', 301);
  }

  // VI: design commands → canvas-design skill
  if (pathname.startsWith('/vi/docs/engineer/commands/design/')) {
    return redirect('/vi/docs/engineer/skills/ai/canvas-design', 301);
  }

  // VI: content commands → copywriting skill
  if (pathname.startsWith('/vi/docs/engineer/commands/content/')) {
    return redirect('/vi/docs/engineer/skills/ai/copywriting', 301);
  }

  // VI: skill commands → skill-creator
  if (pathname.startsWith('/vi/docs/engineer/commands/skill/')) {
    return redirect('/vi/docs/engineer/skills/tools/skill-creator', 301);
  }

  // VI: integrate commands → integrate skill
  if (pathname.startsWith('/vi/docs/engineer/commands/integrate/')) {
    return redirect('/vi/docs/engineer/skills/tools/integrate', 301);
  }

  return next();
});

```


```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
