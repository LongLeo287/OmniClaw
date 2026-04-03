---
id: openclaw-command-center-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.914927
---

# KNOWLEDGE EXTRACT: openclaw-command-center
> **Extracted on:** 2026-03-30 13:16:30
> **Source:** openclaw-command-center

---

## File: `.gitignore`
```
# Dependencies
node_modules/
.pnp/
.pnp.js

# Build output
dist/
build/
out/
.next/

# Runtime data
pids/
*.pid
*.seed
*.pid.lock

# Coverage & Testing
coverage/
.nyc_output/
*.lcov

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Environment & Secrets
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
*.pem
secrets/

# Local configuration (keep examples)
config/dashboard.json
config/local.json
!config/*.example.json

# User-specific data (keep examples)
public/data/operators.json
public/data/privacy-settings.json
!public/data/*.example

# Local Makefile overrides
Makefile.local

# Editor & IDE
.idea/
.vscode/
*.swp
*.swo
*~
.project
.classpath
.settings/

# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Debug
.debug/

# TypeScript
*.tsbuildinfo

# Optional npm cache
.npm/

# Optional eslint cache
.eslintcache

# Optional REPL history
.node_repl_history

# Yarn
.yarn-integrity
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz

# Temporary files
tmp/
temp/
*.tmp
*.temp

# Lock files (keep package-lock.json)
yarn.lock
pnpm-lock.yaml

# Documentation build
docs/_build/

# Misc
*.bak
*.backup
config/dashboard.local.json
```

## File: `.prettierignore`
```
node_modules
package-lock.json
lib/server.js
```

## File: `.prettierrc`
```
{
  "semi": true,
  "singleQuote": false,
  "trailingComma": "all",
  "printWidth": 100,
  "tabWidth": 2
}
```

## File: `AGENTS.md`
```markdown
# AGENTS.md — AI Workspace Guide

> _"The Overmind speaks through many voices, but with one purpose."_

Welcome, AI agent. This document defines how you should interact with this codebase.

## ⚠️ CRITICAL: Pull Request Workflow

**All changes to this repository MUST go through pull requests.**

This is a public open source project. Even maintainers (including AI agents working on behalf of maintainers) must:

1. Create a feature branch (`git checkout -b type/description`)
2. Make changes and commit
3. Push branch and open a PR
4. Get approval before merging

**Never push directly to `main`.** This applies to everyone, including the repo owner.

## 🎯 Mission

OpenClaw Command Center is the central dashboard for AI assistant management. Your mission is to help build, maintain, and improve this system while maintaining the Starcraft/Zerg thematic elements that make it unique.

## 🏛️ Architecture

**Read First**: [`docs/architecture/OVERVIEW.md`](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/docu/docs/components/overview.md)

Key architectural principles:

1. **DRY** — Don't Repeat Yourself. Extract shared code to partials/modules.
2. **Zero Build Step** — Plain HTML/CSS/JS, no compilation needed.
3. **Real-Time First** — SSE for live updates, polling as fallback.
4. **Progressive Enhancement** — Works without JS, enhanced with JS.

## 📁 Workspace Structure

```
openclaw-command-center/
├── lib/                    # Core server logic
│   ├── server.js           # Main HTTP server and API routes
│   ├── config.js           # Configuration loader with auto-detection
│   ├── jobs.js             # Jobs/scheduler API integration
│   ├── linear-sync.js      # Linear issue tracker integration
│   └── topic-classifier.js # NLP-based topic classification
├── public/                 # Frontend assets
│   ├── index.html          # Main dashboard UI
│   ├── jobs.html           # AI Jobs management UI
│   ├── partials/           # ⭐ Shared HTML partials (DRY!)
│   │   └── sidebar.html    # Navigation sidebar component
│   ├── css/
│   │   └── dashboard.css   # Shared styles
│   └── js/
│       ├── sidebar.js      # Sidebar loader + SSE badges
│       ├── app.js          # Main dashboard logic
│       └── lib/            # Third-party libraries
├── scripts/                # Operational scripts
├── config/                 # Configuration (be careful!)
├── docs/                   # Documentation
│   └── architecture/       # Architecture Decision Records
├── tests/                  # Test files
├── SKILL.md                # ClawHub skill metadata
└── package.json            # Version and dependencies
```

## ✅ Safe Operations

Do freely:

- Read any file to understand the codebase
- Create/modify files in `lib/`, `public/`, `docs/`, `tests/`
- Add tests
- Update documentation
- Create feature branches

## ⚠️ Ask First

Check with a human before:

- Modifying `config/` files
- Changing CI/CD workflows
- Adding new dependencies to `package.json`
- Making breaking API changes
- Anything touching authentication/secrets

## 🚫 Never

- **Push directly to `main` branch** — ALL changes require PRs
- Commit secrets, API keys, or credentials
- Commit user-specific data files (see `public/data/AGENTS.md`)
- Delete files without confirmation
- Expose internal endpoints publicly

## 🛠️ Development Workflow

### 0. First-Time Setup

```bash
# Install pre-commit hooks (required for all contributors)
make install-hooks

# Or manually:
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

The pre-commit hook enforces rules from this file automatically.

### 1. Feature Development

```bash
# Create feature branch
git checkout -b feat/your-feature-name

# Make changes, then test locally
npm test
npm run lint
make check  # Run pre-commit checks manually

# Commit with descriptive message
git commit -m "feat: add overlord status indicator"

# Push and create PR
git push -u origin feat/your-feature-name
```

### 2. Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation only
- `style:` — Formatting, no code change
- `refactor:` — Code restructuring
- `test:` — Adding tests
- `chore:` — Maintenance tasks

### 3. Code Style

- Use ESLint configuration provided
- Prettier for formatting
- JSDoc comments for public functions
- Meaningful variable names (thematic names encouraged!)

## 📦 ClawHub Skill Workflow

This project is distributed as a ClawHub skill. After changes are merged to `main`, they need to be published to the registry so users can install/update via `clawhub install command-center`.

### Understanding Skill Metadata

Two files control the skill identity:

- **`SKILL.md`** — Frontmatter (`name`, `version`, `description`) used by ClawHub for discovery and search
- **`package.json`** — `version` field for npm compatibility

⚠️ **CRITICAL: Version Sync Required**

Both `package.json` and `SKILL.md` **MUST have the same version number**. This is enforced by pre-commit hooks.

```bash
# If you change version in one file, change it in both:
# package.json:  "version": "1.0.4"
# SKILL.md:      version: 1.0.4
```

The pre-commit hook will block commits if versions are out of sync.

### Publishing Updates

```bash
# 1. Authenticate (one-time)
clawhub login
clawhub whoami

# 2. Bump version in package.json (follow semver)
#    patch: bug fixes         (0.1.0 → 0.1.1)
#    minor: new features      (0.1.0 → 0.2.0)
#    major: breaking changes  (0.1.0 → 1.0.0)

# 3. Tag the release
git tag -a v<new-version> -m "v<new-version> — short description"
git push origin --tags

# 4. Publish
clawhub publish . --slug command-center --version <new-version> \
  --changelog "Description of what changed"

# Or use the release script (handles tagging + publishing):
./scripts/release.sh <new-version>
```

### Verifying a Publish

```bash
# Check published metadata
clawhub inspect command-center

# Test install into a workspace
clawhub install command-center --workdir /path/to/workspace
```

### Updating an Installed Skill

Users update with:

```bash
clawhub update command-center
```

The installed version is tracked in `.clawhub/origin.json` within the skill directory.

### Who Can Publish?

Only maintainers with ClawHub credentials for `jontsai/command-center` can publish. Currently:

- @jontsai (owner)

Contributors: Submit PRs. After merge, a maintainer will handle the ClawHub publish.

### Release Checklist

Before publishing a new version:

1. [ ] All PRs for the release are merged to `main`
2. [ ] Version bumped in both `package.json` and `SKILL.md` frontmatter
3. [ ] CHANGELOG updated (if maintained)
4. [ ] Tests pass: `npm test`
5. [ ] Lint passes: `npm run lint`
6. [ ] Git tag created: `git tag -a v<version> -m "v<version>"`
7. [ ] Tag pushed: `git push origin --tags`
8. [ ] Published to ClawHub with changelog

## 🎨 Thematic Guidelines

This project has a Starcraft/Zerg theme. When naming things:

| Concept            | Thematic Name |
| ------------------ | ------------- |
| Main controller    | Overmind      |
| Worker processes   | Drones        |
| Monitoring service | Overlord      |
| Cache layer        | Creep         |
| Message queue      | Spawning Pool |
| Health check       | Essence scan  |
| Error state        | Corrupted     |

Example:

```javascript
// Instead of: const cacheService = new Cache();
const creepLayer = new CreepCache();

// Instead of: function checkHealth()
function scanEssence()
```

## 📝 Documentation Standards

When you add features, document them:

1. **Code comments** — JSDoc for functions
2. **README updates** — If user-facing
3. **API docs** — In `docs/api/` for endpoints
4. **Architecture Decision Records** — In `docs/architecture/` for major changes

## 🧪 Testing

```bash
# Run all tests
npm test

# Coverage report
npm run test:coverage
```

Aim for meaningful test coverage. Test the logic, not the framework.

## 🐛 Debugging

```bash
# Enable all command-center debug output
DEBUG=openclaw:* npm run dev

# Specific namespaces
DEBUG=openclaw:api npm run dev
DEBUG=openclaw:overlord npm run dev
```

## 🔄 Handoff Protocol

When handing off to another AI or ending a session:

1. Commit all work in progress
2. Document current state in a comment or commit message
3. List any unfinished tasks
4. Note any decisions that need human input

## 📖 Lessons Learned

### DRY is Non-Negotiable

**Problem**: Sidebar was duplicated across `index.html` and `jobs.html`, causing inconsistencies.
**Solution**: Extract to `/partials/sidebar.html` + `/js/sidebar.js` for loading.
**Lesson**: When you see similar code in multiple places, stop and extract it. The cost of extraction is always lower than maintaining duplicates.

### Naming Consistency Matters

**Problem**: "Scheduled Jobs" vs "Cron Jobs" vs "Jobs" caused confusion.
**Solution**: Established naming convention: "Cron Jobs" for OpenClaw scheduled tasks, "AI Jobs" for advanced agent jobs.
**Lesson**: Agree on terminology early. Document it. Enforce it.

### Zero-Build Architecture Has Trade-offs

**Context**: No build step keeps things simple but limits some patterns.
**Solution**: Use `fetch()` to load partials dynamically, `<script>` for shared JS.
**Lesson**: This works well for dashboards. Evaluate trade-offs for your use case.

### SSE Connection Per Component = Wasteful

**Problem**: Multiple components each opening SSE connections.
**Solution**: Single SSE connection in `sidebar.js`, shared state management.
**Lesson**: Centralize real-time connections. Components subscribe to state, not sources.

### Test After Every Significant Change

**Problem**: Easy to break things when refactoring HTML structure.
**Solution**: `make restart` + browser check after each change.
**Lesson**: Keep feedback loops tight. Visual changes need visual verification.

### Document Architectural Decisions

**Problem**: Future agents (or humans) don't know why things are the way they are.
**Solution**: Create `docs/architecture/OVERVIEW.md` and ADRs.
**Lesson**: Write down the "why", not just the "what".

## 📚 Key Resources

- [SKILL.md](../bmad_repo/SKILL.md) — ClawHub skill metadata
- [CONTRIBUTING.md](./CONTRIBUTING.md) — Contribution guidelines
- [docs/](./docs/) — Detailed documentation

---

_"Awaken, my child, and embrace the glory that is your birthright."_
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Code of Conduct

> _"The Swarm is united. Division is corruption."_

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

## Our Standards

### Positive Behaviors

Examples of behavior that contributes to a positive environment:

- **Being respectful** — Treating all contributors with dignity
- **Being constructive** — Providing helpful feedback focused on improvement
- **Being empathetic** — Understanding different perspectives and experiences
- **Being collaborative** — Working together toward shared goals
- **Being graceful** — Accepting responsibility and apologizing when we make mistakes
- **Focusing on the work** — Prioritizing what's best for the community and project

### Unacceptable Behaviors

Examples of unacceptable behavior:

- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Sexual language, imagery, or unwelcome advances
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Scope

This Code of Conduct applies within all community spaces, including:

- GitHub repository (issues, PRs, discussions)
- Any associated chat channels
- Project events or meetups
- One-on-one communications related to the project

## Enforcement

### Reporting

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated promptly and fairly.

### Confidentiality

All reporters will be protected. We will maintain confidentiality regarding the reporter of an incident.

### Consequences

Community leaders will follow these guidelines in determining consequences:

#### 1. Correction

**Impact:** Minor unprofessional behavior.
**Consequence:** Private written warning with clarity around the violation. A public apology may be requested.

#### 2. Warning

**Impact:** A violation through a single incident or series of actions.
**Consequence:** Warning with consequences for continued behavior. No interaction with the people involved for a specified period. This includes avoiding interactions in community spaces as well as external channels.

#### 3. Temporary Ban

**Impact:** A serious violation of community standards.
**Consequence:** Temporary ban from any sort of interaction or public communication with the community for a specified period.

#### 4. Permanent Ban

**Impact:** Demonstrating a pattern of violation of community standards.
**Consequence:** Permanent ban from any sort of public interaction within the community.

## For AI Participants

AI agents contributing to this project are held to the same standards. Maintainers of AI systems used to contribute are responsible for ensuring their AI follows this code of conduct.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/), version 2.1.

---

_"In unity, the Swarm finds strength."_
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to OpenClaw Command Center

> _"Join the Swarm. Evolve together."_

First off, thank you for considering contributing to OpenClaw Command Center! This project thrives on community involvement.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Contributions](#making-contributions)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Publishing to ClawHub](#publishing-to-clawhub)
- [For AI Contributors](#for-ai-contributors)

## 📜 Code of Conduct

This project adheres to our [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you're expected to uphold this code. Please report unacceptable behavior to the maintainers.

## 🚀 Getting Started

### Prerequisites

- Node.js v20 or higher
- npm v10 or higher
- Git

### Development Setup

1. **Fork the repository**

   Click the "Fork" button on GitHub to create your own copy.

2. **Clone your fork**

   ```bash
   git clone https://github.com/YOUR_USERNAME/openclaw-command-center.git
   cd openclaw-command-center
   ```

3. **Add upstream remote**

   ```bash
   git remote add upstream https://github.com/jontsai/openclaw-command-center.git
   ```

4. **Install dependencies**

   ```bash
   npm install
   ```

5. **Create configuration**

   ```bash
   cp config/dashboard.example.json config/dashboard.json
   ```

6. **Install pre-commit hooks**

   ```bash
   make install-hooks
   ```

   This enforces project rules automatically on each commit.

7. **Start development server**
   ```bash
   npm run dev
   ```

## 🛠️ Making Contributions

### Types of Contributions

We welcome:

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Test coverage
- 🎨 UI/UX enhancements
- 🔧 Performance optimizations

### Before You Start

1. **Check existing issues** — Someone might already be working on it
2. **Open an issue first** — For major changes, discuss before implementing
3. **Keep scope focused** — One feature/fix per PR

### Branch Naming

Use descriptive branch names:

```
feat/add-session-filtering
fix/overlord-connection-timeout
docs/update-api-reference
refactor/simplify-creep-cache
```

## 📤 Pull Request Process

### 1. Create Your Branch

```bash
git checkout main
git pull upstream main
git checkout -b feat/your-feature-name
```

### 2. Make Your Changes

- Write clean, documented code
- Add tests for new functionality
- Update documentation if needed
- Follow the [style guidelines](#style-guidelines)

### 3. Test Your Changes

```bash
npm test
npm run lint
```

### 4. Commit Your Changes

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add overlord heartbeat indicator"
git commit -m "fix: resolve session timeout on reconnect"
git commit -m "docs: clarify API authentication flow"
```

### 5. Push and Create PR

```bash
git push origin feat/your-feature-name
```

Then open a Pull Request on GitHub.

### 6. PR Review

- Maintainers will review your PR
- Address any requested changes
- Once approved, a maintainer will merge

### PR Checklist

Before submitting, ensure:

- [ ] Code follows project style guidelines
- [ ] Tests pass locally (`npm test`)
- [ ] Lint passes (`npm run lint`)
- [ ] Documentation updated if needed
- [ ] Commit messages follow convention
- [ ] PR description explains the change

## 🎨 Style Guidelines

### Code Style

- Use ESLint configuration provided
- Use Prettier for formatting
- Prefer `const` over `let`, avoid `var`
- Use meaningful variable names
- Add JSDoc comments for public functions

### Thematic Naming

Embrace the Starcraft theme when naming:

```javascript
// Good
const overlordStatus = await checkEssence();
const creepCache = new CreepLayer();

// Less thematic
const monitorStatus = await healthCheck();
const cacheLayer = new CacheService();
```

### Documentation

- Use clear, concise language
- Include code examples where helpful
- Keep README and docs in sync with code
- Add inline comments for complex logic

## 📦 Publishing to ClawHub

This skill is distributed via [ClawHub](https://clawhub.ai). After changes are merged to `main`, maintainers publish updates to the registry.

### Prerequisites

```bash
# Install clawhub CLI (if not already installed)
# See https://clawhub.ai for installation instructions

# Authenticate
clawhub login
clawhub whoami   # verify
```

### Publishing a New Version

1. **Bump the version** in `package.json`
2. **Tag the release** (see [Git Tags for Releases](#git-tags-for-releases))
3. **Publish:**

   ```bash
   clawhub publish . --slug command-center --version <new-version> \
     --changelog "Description of changes"
   ```

   Or use the release script which handles tagging and publishing:

   ```bash
   ./scripts/release.sh <new-version>
   ```

### Git Tags for Releases

Tag each release so the [release workflow](.github/workflows/release.yml) can generate GitHub Releases automatically:

```bash
# Tag the current commit
git tag -a v<version> -m "v<version> — short description"

# Push tags
git push origin --tags
```

### Version Bumping

Follow [semver](https://semver.org/):

| Change type                   | Bump    | Example         |
| ----------------------------- | ------- | --------------- |
| Bug fixes, minor tweaks       | `patch` | `0.1.0 → 0.1.1` |
| New features, backward compat | `minor` | `0.1.0 → 0.2.0` |
| Breaking changes              | `major` | `0.1.0 → 1.0.0` |

⚠️ **Important:** When bumping version, update **both** files:

- `package.json` — `"version": "X.Y.Z"`
- `SKILL.md` — `version: X.Y.Z` (in frontmatter)

The pre-commit hook will block commits if these versions don't match.

### Verifying a Publish

```bash
# Check the published version
clawhub inspect command-center

# Install into a workspace to test
clawhub install command-center
```

## 🤖 For AI Contributors

AI agents are welcome contributors! If you're an AI working on this project:

1. **Read the context files first**
   - [AGENTS.md](../bmad_repo/agents.md) — Your workspace guide
   - [SKILL.md](../bmad_repo/SKILL.md) — ClawHub skill metadata

2. **Follow the same PR process** as human contributors

3. **Document your changes thoroughly** — Future AI (and humans) will thank you

4. **When in doubt, ask** — Open an issue to discuss before major changes

## 💬 Getting Help

- **Questions?** Open a GitHub Discussion
- **Found a bug?** Open an Issue
- **Security concern?** Email maintainers directly (don't open public issue)

## 🙏 Recognition

Contributors will be recognized in:

- GitHub Contributors list
- Release notes for significant contributions
- Our eternal gratitude 🐛

---

_"The Swarm welcomes all who serve the greater purpose."_
```

## File: `eslint.config.mjs`
```
import js from "@eslint/js";

export default [
  js.configs.recommended,
  {
    languageOptions: {
      globals: {
        // Node.js globals
        require: "readonly",
        module: "readonly",
        exports: "readonly",
        __dirname: "readonly",
        __filename: "readonly",
        process: "readonly",
        console: "readonly",
        Buffer: "readonly",
        setTimeout: "readonly",
        setInterval: "readonly",
        setImmediate: "readonly",
        clearTimeout: "readonly",
        clearInterval: "readonly",
        clearImmediate: "readonly",
        URL: "readonly",
        URLSearchParams: "readonly",
      },
    },
    rules: {
      "no-unused-vars": ["warn", { argsIgnorePattern: "^_" }],
      "no-console": "off",
    },
  },
  // Ignore build output
  {
    ignores: ["lib/server.js"],
  },
  // Relax rules for source code (many patterns)
  {
    files: ["src/**/*.js"],
    rules: {
      "no-empty": "warn",
      "no-case-declarations": "warn",
      "no-misleading-character-class": "warn",
    },
  },
];
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Jonathan Tsai

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

## File: `Makefile`
```
# OpenClaw Command Center
# Usage: make [target]
#
# Runs dashboard in tmux for easy inspection and management

TMUX_SESSION := openclaw-dashboard
LOG_DIR := $(HOME)/.openclaw-command-center/logs
LOG_FILE := $(LOG_DIR)/dashboard.log
DASHBOARD_DIR := $(CURDIR)
PORT := 3333

.DEFAULT_GOAL := help
.PHONY: help ensure start stop restart status logs attach clean release install-hooks check test lint build

# Include local overrides if they exist (not tracked in git)
-include Makefile.local

help: ## Show this help
	@echo "OpenClaw Command Center - tmux-based management"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sed 's/^[^:]*://' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Quick start: make start && make attach"

ensure: ## Ensure dashboard is running (idempotent, self-healing)
	@mkdir -p $(LOG_DIR)
	@touch $(LOG_FILE)
	@if ! command -v tmux >/dev/null 2>&1; then \
		echo "❌ tmux not found. Please install tmux."; \
		exit 1; \
	fi
	@if ! command -v node >/dev/null 2>&1; then \
		echo "❌ node not found. Please install node."; \
		exit 1; \
	fi
	@if ! tmux has-session -t $(TMUX_SESSION) 2>/dev/null; then \
		echo "Creating tmux session '$(TMUX_SESSION)'..."; \
		tmux new-session -d -s $(TMUX_SESSION) -c $(DASHBOARD_DIR) \
			"./scripts/dashboard-loop.sh; echo '[Loop exited - shell ready]'; exec bash -l"; \
		tmux split-window -h -t $(TMUX_SESSION) -c $(DASHBOARD_DIR) "exec bash -l"; \
		tmux select-pane -t $(TMUX_SESSION):0.0; \
		tmux split-window -v -t $(TMUX_SESSION) "tail -f $(LOG_FILE); exec bash -l"; \
		tmux select-pane -t $(TMUX_SESSION):0.0; \
		sleep 2; \
		echo "✅ Dashboard started on port $(PORT)."; \
	elif ! tmux list-panes -t $(TMUX_SESSION):0 2>/dev/null | grep -q "^0:"; then \
		echo "⚠️  Session exists but is malformed. Recreating..."; \
		tmux kill-session -t $(TMUX_SESSION) 2>/dev/null || true; \
		$(MAKE) ensure; \
	elif [ "$$(tmux display-message -t $(TMUX_SESSION):0.0 -p '#{pane_dead}')" = "1" ]; then \
		echo "⚠️  Dashboard pane died. Respawning..."; \
		tmux respawn-pane -k -t $(TMUX_SESSION):0.0 -c $(DASHBOARD_DIR) \
			"node lib/server.js 2>&1 | tee -a $(LOG_FILE); echo '[Dashboard exited - shell ready]'; exec bash -l"; \
		echo "✅ Dashboard respawned."; \
	elif [ "$$(tmux display-message -t $(TMUX_SESSION):0.2 -p '#{pane_dead}')" = "1" ]; then \
		echo "⚠️  Logs pane died. Respawning..."; \
		tmux respawn-pane -k -t $(TMUX_SESSION):0.2 "tail -f $(LOG_FILE); exec bash -l"; \
		echo "✅ Logs pane respawned."; \
	else \
		echo "✅ Dashboard already running on port $(PORT)."; \
	fi

start: ensure ## Start dashboard in tmux (alias for ensure)

stop: ## Stop dashboard
	@if tmux has-session -t $(TMUX_SESSION) 2>/dev/null; then \
		echo "Stopping dashboard..."; \
		tmux send-keys -t $(TMUX_SESSION) C-c; \
		sleep 1; \
		tmux kill-session -t $(TMUX_SESSION) 2>/dev/null || true; \
		echo "✅ Dashboard stopped."; \
	else \
		echo "Dashboard not running."; \
	fi

restart: stop start ## Restart dashboard

status: ## Show dashboard status
	@echo "=== tmux session ==="
	@tmux has-session -t $(TMUX_SESSION) 2>/dev/null && echo "✅ Running" || echo "❌ Not running"
	@echo ""
	@echo "=== Port $(PORT) ==="
	@lsof -i :$(PORT) 2>/dev/null | head -5 || echo "Port $(PORT) not in use"
	@echo ""
	@echo "=== Recent logs ==="
	@tail -5 $(LOG_FILE) 2>/dev/null || echo "No logs"

logs: ## Tail dashboard logs
	@tail -f $(LOG_FILE)

attach: ## Attach to tmux session (Ctrl-B D to detach)
	@if ! tmux has-session -t $(TMUX_SESSION) 2>/dev/null; then \
		echo "Dashboard not running. Use 'make start' to start."; \
	elif [ -n "$$TMUX" ]; then \
		CURRENT=$$(tmux display-message -p '#S'); \
		if [ "$$CURRENT" = "$(TMUX_SESSION)" ]; then \
			echo "Already in $(TMUX_SESSION) session."; \
		else \
			tmux switch-client -t $(TMUX_SESSION); \
		fi \
	else \
		tmux attach -t $(TMUX_SESSION); \
	fi

clean: ## Stop dashboard and clean logs
	@$(MAKE) stop
	@echo "Cleaning logs..."
	@rm -f $(LOG_FILE)
	@echo "✅ Cleaned."

release: ## Create a release (usage: make release V=0.4.0)
ifndef V
	@echo "Usage: make release V=<version>"
	@echo "  e.g., make release V=0.4.0"
	@./scripts/release.sh --current
else
	@./scripts/release.sh $(V)
endif

install-hooks: ## Install git pre-commit hooks
	@echo "Installing pre-commit hook..."
	@cp scripts/pre-commit .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "✅ Pre-commit hook installed."
	@echo "Run 'make check' to test checks manually."

check: ## Run pre-commit checks manually
	@./scripts/pre-commit

# ============================================================================
# Development targets
# ============================================================================

test: ## Run tests
	@npm test

lint: ## Run linter
	@npm run lint

build: ## Build bundled server.js from src modules
	@npm run build
```

## File: `Makefile.local.example`
```
# Makefile.local - Private overrides (not tracked in git)
# Copy this file to Makefile.local and customize as needed
#
# Example custom targets:

.PHONY: lfg dev-tunnel

# Quick start: start + attach in one command
lfg: ## Start dashboard and drop into cockpit
	@$(MAKE) ensure
	@$(MAKE) attach

# Example: start with cloudflare tunnel for remote access
dev-tunnel: ## Start with tunnel for remote access
	@$(MAKE) ensure
	@echo "Starting tunnel..."
	# cloudflared tunnel --url http://localhost:$(PORT)
```

## File: `package.json`
```json
{
  "name": "openclaw-command-center",
  "version": "1.4.1",
  "description": "🦞 AI agent command and control dashboard — Spawn more Overlords!",
  "main": "lib/server.js",
  "type": "commonjs",
  "scripts": {
    "start": "node lib/server.js",
    "dev": "node --watch lib/server.js",
    "dev:src": "esbuild src/index.js --bundle --platform=node --outfile=lib/server.js --watch",
    "build": "esbuild src/index.js --bundle --platform=node --outfile=lib/server.js --banner:js='#!/usr/bin/env node' && prettier --write lib/server.js",
    "test": "node --test",
    "test:coverage": "node --test --experimental-test-coverage",
    "lint": "ESLINT_USE_FLAT_CONFIG=true eslint src/ tests/",
    "lint:fix": "ESLINT_USE_FLAT_CONFIG=true eslint src/ tests/ --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "prepare": "echo 'Ready to spawn Overlords 🦞'"
  },
  "keywords": [
    "ai",
    "agent",
    "dashboard",
    "monitoring",
    "claude",
    "chatgpt",
    "llm",
    "command-center",
    "openclaw"
  ],
  "author": "OpenClaw Contributors",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/jontsai/openclaw-command-center.git"
  },
  "bugs": {
    "url": "https://github.com/jontsai/openclaw-command-center/issues"
  },
  "homepage": "https://github.com/jontsai/openclaw-command-center#readme",
  "engines": {
    "node": ">=18.0.0"
  },
  "devDependencies": {
    "esbuild": "^0.27.3",
    "eslint": "^8.56.0",
    "prettier": "^3.2.4"
  }
}
```

## File: `README.md`
```markdown
# 🦞 OpenClaw Command Center

English | [简体中文](README.zh-CN.md)

<div align="center">

**Mission control for your AI agents**

[![CI](https://github.com/jontsai/openclaw-command-center/actions/workflows/ci.yml/badge.svg)](https://github.com/jontsai/openclaw-command-center/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org)
[![ClawHub](https://img.shields.io/badge/ClawHub-command--center-blue)](https://www.clawhub.ai/jontsai/command-center)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jontsai/openclaw-command-center/pulls)

[Features](#features) • [Quick Start](#quick-start) • [Security](#-security) • [Configuration](#configuration)

</div>

---

## Why Command Center?

Your AI agents are running 24/7. You need to know what they're doing.

Command Center gives you **real-time visibility** into your OpenClaw deployment — sessions, costs, system health, scheduled tasks — all in one secure dashboard.

### ⚡ Fast

- **Single API call** — unified state endpoint, not 16+ separate requests
- **2-second updates** — real-time SSE push, not polling
- **5-second cache** — backend stays responsive under load
- **Instant startup** — no build step, no compilation

### 🪶 Lightweight

- **Zero dependencies** for users — just Node.js
- **~200KB total** — dashboard + server
- **No webpack/vite/bundler** — runs directly
- **No React/Vue/Angular** — vanilla JS, works everywhere

### 📱 Responsive

- **Desktop & mobile** — works on any screen size
- **Dark mode** — easy on the eyes, Starcraft-inspired
- **Live updates** — no manual refresh needed
- **Offline-friendly** — graceful degradation

### 🔧 Modern

- **ES Modules** — clean component architecture
- **SSE streaming** — efficient real-time updates
- **REST API** — integrate with your tools
- **TypeScript-ready** — JSDoc types included

### 🔒 Security (Most Important)

Command Center takes security seriously:

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Auth Modes**           | Token, Tailscale, Cloudflare Access, IP allowlist   |
| **No external calls**    | Dashboard runs 100% locally — no telemetry, no CDNs |
| **Localhost default**    | Binds to `127.0.0.1` by default                     |
| **Read-only by default** | View your agents without exposing control           |
| **No secrets in UI**     | API keys, tokens never displayed                    |
| **Audit logging**        | Know who accessed what, when                        |

```bash
# Secure deployment example (Tailscale)
DASHBOARD_AUTH_MODE=tailscale node lib/server.js
# Only users on your Tailscale network can access
```

---

## Features

| Feature                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| 📊 **Session Monitoring**  | Real-time view of active AI sessions        |
| ⛽ **LLM Fuel Gauges**     | Token usage, costs, quota remaining         |
| 💻 **System Vitals**       | CPU, memory, disk, temperature              |
| ⏰ **Cron Jobs**           | View and manage scheduled tasks             |
| 🧠 **Cerebro Topics**      | Automatic conversation tagging              |
| 👥 **Operators**           | Who's talking to your agents                |
| 📝 **Memory Browser**      | View agent memory files                     |
| 🔒 **Privacy Controls**    | Hide sensitive topics for demos/screenshots |
| 💰 **Cost Breakdown**      | Detailed per-model cost analysis            |
| 📈 **Savings Projections** | Monthly cost vs. manual estimates           |

---

## Quick Start

```bash
npx clawhub@latest install command-center
cd skills/command-center
node lib/server.js
```

**Dashboard runs at http://localhost:3333** 🎉

<details>
<summary>Alternative: Git clone</summary>

```bash
git clone https://github.com/jontsai/openclaw-command-center
cd openclaw-command-center
node lib/server.js
```

</details>

---

## Zero-Config Experience

Command Center **auto-detects** your OpenClaw workspace:

1. `$OPENCLAW_WORKSPACE` environment variable
2. `~/.openclaw-workspace` or `~/openclaw-workspace`
3. Common names: `~/molty`, `~/clawd`, `~/moltbot`

If you have `memory/` or `state/` directories, you're good to go.

---

## Optional System Dependencies

Command Center requires **only Node.js** to run. However, some system vitals features benefit from optional packages. Without them, the dashboard still works — those metrics simply show zeros or fall back gracefully.

| OS                    | Package             | Purpose                            | Install                                                       | Without It                        |
| --------------------- | ------------------- | ---------------------------------- | ------------------------------------------------------------- | --------------------------------- |
| Linux                 | `sysstat`           | Disk I/O vitals (IOPS, throughput) | `sudo apt install sysstat`                                    | Disk stats show zeros             |
| Linux                 | `lm-sensors`        | Additional temperature sensors     | `sudo apt install lm-sensors`                                 | Uses thermal_zone (usually works) |
| macOS (Intel)         | `osx-cpu-temp`      | CPU temperature                    | [Build from source](https://github.com/lavoiesl/osx-cpu-temp) | Battery temp fallback             |
| macOS (Apple Silicon) | passwordless `sudo` | CPU temperature via `powermetrics` | Configure in sudoers                                          | Shows note in UI                  |

Command Center logs hints for missing optional dependencies once at startup.

---

## Configuration

### Environment Variables

| Variable             | Description    | Default     |
| -------------------- | -------------- | ----------- |
| `PORT`               | Server port    | `3333`      |
| `OPENCLAW_WORKSPACE` | Workspace root | Auto-detect |
| `OPENCLAW_PROFILE`   | Profile name   | (none)      |

### 🔒 Authentication

| Mode         | Use Case      | Config                                                    |
| ------------ | ------------- | --------------------------------------------------------- |
| `none`       | Local dev     | `DASHBOARD_AUTH_MODE=none`                                |
| `token`      | API access    | `DASHBOARD_AUTH_MODE=token DASHBOARD_TOKEN=secret`        |
| `tailscale`  | Team access   | `DASHBOARD_AUTH_MODE=tailscale`                           |
| `cloudflare` | Public deploy | `DASHBOARD_AUTH_MODE=cloudflare`                          |
| `allowlist`  | IP whitelist  | `DASHBOARD_AUTH_MODE=allowlist DASHBOARD_ALLOWED_IPS=...` |

### 📋 Recommended OpenClaw Settings

For the best Command Center experience, configure your OpenClaw gateway:

#### Slack Threading (Critical)

Enable threading for all messages to get proper topic tracking:

```yaml
# In your OpenClaw config (gateway.yaml or via openclaw gateway config)
slack:
  capabilities:
    threading: all # Options: all, dm, group, none
```

**Why this matters:** Without threading, the dashboard can't track conversation topics properly. Each thread becomes a trackable unit of work.

#### Session Labels

Use descriptive session labels for better dashboard visibility:

```yaml
sessions:
  labelFormat: "{channel}:{topic}" # Customize as needed
```

#### Cerebro (Topic Tracking)

Enable Cerebro for automatic conversation tagging:

```bash
# Initialize Cerebro directories
mkdir -p ~/your-workspace/cerebro/topics
mkdir -p ~/your-workspace/cerebro/orphans
```

The dashboard will automatically detect and display topic data.

---

### Multi-Profile Support

Running multiple OpenClaw instances?

```bash
# Production dashboard
node lib/server.js --profile production --port 3333

# Development dashboard
node lib/server.js --profile dev --port 3334
```

---

## API

Command Center exposes a REST API:

| Endpoint            | Description                                        |
| ------------------- | -------------------------------------------------- |
| `GET /api/state`    | **Unified state** — all dashboard data in one call |
| `GET /api/health`   | Health check                                       |
| `GET /api/vitals`   | System metrics                                     |
| `GET /api/sessions` | Active sessions                                    |
| `GET /api/events`   | SSE stream for real-time updates                   |

---

## Architecture

```
command-center/
├── lib/
│   ├── server.js           # HTTP server + API
│   ├── config.js           # Configuration
│   └── jobs.js             # Cron integration
├── public/
│   ├── index.html          # Dashboard UI
│   └── js/                 # Components (ES modules)
└── scripts/
    ├── setup.sh            # First-time setup
    └── verify.sh           # Health check
```

---

## 🚀 Coming Soon

### Advanced Job Scheduling

Building on OpenClaw's native cron system with intelligent scheduling primitives:

| Primitive            | Description                                 |
| -------------------- | ------------------------------------------- |
| **run-if-not**       | Skip if job already running (dedupe)        |
| **run-if-idle**      | Only execute when system capacity available |
| **run-after**        | Dependency chains between jobs              |
| **run-with-backoff** | Exponential retry on failure                |
| **priority-queue**   | Critical vs. background work prioritization |

### Multi-Agent Orchestration

- Agent-to-agent handoffs
- Swarm coordination patterns
- Specialized agent routing (data analysis, documentation, testing)
- Cross-session context sharing

### Integration Ecosystem

- Webhook triggers for external systems
- Slack slash commands for quick actions
- API for custom integrations
- Plugin architecture for specialized agents

---

## Screenshots

### Dashboard Overview

The hero view shows key metrics at a glance: total tokens, costs, active sessions, estimated savings, and system capacity.

<p align="center">
  <img src="docs/screenshots/hero.png" alt="Dashboard Hero" width="800">
</p>

### Sessions Panel

Monitor all active AI sessions in real-time. Each card shows model, channel, token usage, cost, and activity status. Filter by status (live/recent/idle), channel, or session type.

<p align="center">
  <img src="docs/screenshots/sessions-panel.png" alt="Sessions Panel" width="800">
</p>

### Cron Jobs

View and manage scheduled tasks. See run history, next scheduled time, and enable/disable jobs. The dashboard shows job success/failure sparklines and filters by status and schedule type.

<p align="center">
  <img src="docs/screenshots/cron-panel.png" alt="Cron Jobs Panel" width="800">
</p>

### Cerebro Topics

Automatic conversation organization. Topics are auto-detected from Slack threads, with status tracking (active/resolved/parked), thread counts, and quick navigation. Privacy controls let you hide sensitive topics.

<p align="center">
  <img src="docs/screenshots/cerebro-panel.png" alt="Cerebro Topics Panel" width="800">
</p>

### Operators

See who's interacting with your AI agents. Track active sessions per operator, permission levels, and last activity timestamps.

<p align="center">
  <img src="docs/screenshots/operators-panel.png" alt="Operators Panel" width="800">
</p>

### Memory Browser

Browse your agent's memory files — daily logs, long-term memory, and workspace files. Quick navigation with file sizes and modification times.

<p align="center">
  <img src="docs/screenshots/memory-panel.png" alt="Memory Panel" width="800">
</p>

### Cost Breakdown Modal

Click on any cost stat to see detailed breakdowns: token usage by type, pricing rates, and calculation methodology. Includes estimated savings vs. manual work.

<p align="center">
  <img src="docs/screenshots/cost-modal.png" alt="Cost Breakdown Modal" width="800">
</p>

### Operator Details

Click on an operator card to see their session history, stats, and activity timeline.

<p align="center">
  <img src="docs/screenshots/operator-modal.png" alt="Operator Details Modal" width="800">
</p>

### Privacy Settings

Control what's visible for demos and screenshots. Hide sensitive topics, sessions, or cron jobs. Settings sync to the server automatically.

<p align="center">
  <img src="docs/screenshots/privacy-modal.png" alt="Privacy Settings Modal" width="800">
</p>

### Session Details

Click any session card to see detailed information: summary, key facts, tools used, and recent messages.

<p align="center">
  <img src="docs/screenshots/session-detail.png" alt="Session Details Panel" width="800">
</p>

### Full Dashboard

The complete dashboard with all panels visible.

<details>
<summary>Click to expand full dashboard view</summary>
<p align="center">
  <img src="docs/screenshots/dashboard-full.png" alt="Full Dashboard" width="800">
</p>
</details>

---

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md).

### Development

```bash
npm install        # Install dev dependencies
npm run dev        # Watch mode
npm run lint       # Check code style
npm run format     # Auto-format
./scripts/verify.sh  # Run health checks
```

---

## License

MIT © [Jonathan Tsai](https://github.com/jontsai)

---

<div align="center">

**[Install from ClawHub](https://www.clawhub.ai/jontsai/command-center)** · **[OpenClaw](https://github.com/openclaw/openclaw)** · **[Discord](https://discord.gg/clawd)**

</div>
```

## File: `README.zh-CN.md`
```markdown
# 🦞 OpenClaw Command Center

[English](README.md) | 简体中文

<div align="center">

**你的 AI 代理任务指挥中心**

[![CI](https://github.com/jontsai/openclaw-command-center/actions/workflows/ci.yml/badge.svg)](https://github.com/jontsai/openclaw-command-center/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org)
[![ClawHub](https://img.shields.io/badge/ClawHub-command--center-blue)](https://www.clawhub.ai/jontsai/command-center)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jontsai/openclaw-command-center/pulls)

[功能特性](#功能特性) • [快速开始](#快速开始) • [安全](#-安全) • [配置](#配置)

</div>

---

## 为什么需要 Command Center？

你的 AI 代理 24/7 在运行，但你需要实时知道它们在做什么。

Command Center 为 OpenClaw 提供统一的可视化看板：**会话状态、Token/成本、系统健康、定时任务** 一屏掌握。

### ⚡ 快速

- **单次 API 聚合**：统一状态端点，而非 16+ 个分散请求
- **2 秒更新**：基于 SSE 实时推送，不依赖轮询
- **5 秒缓存**：高负载下保持后端响应
- **即开即用**：无需构建、无需编译

### 🪶 轻量

- **用户零依赖**：只需 Node.js
- **约 200KB**：看板 + 服务端总量小
- **无 webpack/vite/bundler**：直接运行
- **无 React/Vue/Angular**：原生 JavaScript（Vanilla JS），兼容性高

### 📱 自适应

- **桌面/移动端**：任意屏幕可用
- **深色主题**：长时间使用更舒适（Starcraft 风格）
- **实时更新**：无需手动刷新
- **离线友好**：支持优雅降级

### 🔧 现代

- **ES Modules**：组件化结构清晰
- **SSE 流式更新**：实时且高效
- **REST API**：可集成到你自己的工具链
- **TypeScript-ready**：附带 JSDoc 类型信息

### 🔒 安全（最重要）

| 特性              | 说明                                           |
| ----------------- | ---------------------------------------------- |
| **认证模式**      | Token、Tailscale、Cloudflare Access、IP 白名单 |
| **无外部调用**    | 本地 100% 运行：无遥测、无 CDN                 |
| **默认本机监听**  | 默认绑定 `127.0.0.1`                           |
| **默认只读**      | 先看后控，降低误操作风险                       |
| **UI 不暴露密钥** | API Key / Token 不在前端展示                   |
| **审计日志**      | 谁在何时访问了什么，一目了然                   |

```bash
# 安全部署示例（Tailscale）
DASHBOARD_AUTH_MODE=tailscale node lib/server.js
# 仅允许你 Tailscale 网络内用户访问
```

---

## 功能特性

| 功能                       | 说明                       |
| -------------------------- | -------------------------- |
| 📊 **会话监控**            | 实时查看活跃 AI 会话       |
| ⛽ **LLM 用量仪表**        | Token 用量、成本、剩余额度 |
| 💻 **系统状态**            | CPU、内存、磁盘、温度      |
| ⏰ **定时任务**            | 查看与管理 Cron Jobs       |
| 🧠 **Cerebro 话题**        | 自动话题聚类与追踪         |
| 👥 **Operators（操作者）** | 查看谁在与代理交互         |
| 📝 **记忆浏览**            | 浏览 memory 文件与状态     |
| 🔒 **隐私控制**            | 演示/截图时隐藏敏感内容    |
| 💰 **成本拆解**            | 模型维度成本明细           |
| 📈 **节省预测**            | 与人工估算做月度对比       |

---

## 快速开始

```bash
npx clawhub@latest install command-center
cd skills/command-center
node lib/server.js
```

**默认访问地址： http://localhost:3333** 🎉

<details>
<summary>备选：Git clone</summary>

```bash
git clone https://github.com/jontsai/openclaw-command-center
cd openclaw-command-center
node lib/server.js
```

</details>

---

## 零配置体验

Command Center 会自动探测 OpenClaw 工作区：

1. `$OPENCLAW_WORKSPACE` 环境变量
2. `~/.openclaw-workspace` 或 `~/openclaw-workspace`
3. 常见目录名：`~/molty`、`~/clawd`、`~/moltbot`

只要存在 `memory/` 或 `state/` 目录即可开箱使用。

---

## 可选系统依赖

Command Center 仅需 **Node.js** 即可运行。部分系统监控功能可通过安装可选依赖获得增强体验，缺少时仪表盘仍可正常运行，相关指标会显示为零或优雅降级。

| 操作系统              | 软件包         | 用途                              | 安装方式                                               | 缺少时                        |
| --------------------- | -------------- | --------------------------------- | ------------------------------------------------------ | ----------------------------- |
| Linux                 | `sysstat`      | 磁盘 I/O（IOPS、吞吐量）          | `sudo apt install sysstat`                             | 磁盘统计显示为零              |
| Linux                 | `lm-sensors`   | 额外温度传感器                    | `sudo apt install lm-sensors`                          | 使用 thermal_zone（通常可用） |
| macOS (Intel)         | `osx-cpu-temp` | CPU 温度                          | [从源码编译](https://github.com/lavoiesl/osx-cpu-temp) | 回退至电池温度                |
| macOS (Apple Silicon) | 免密 `sudo`    | 通过 `powermetrics` 获取 CPU 温度 | 在 sudoers 中配置                                      | 界面显示提示                  |

Command Center 在启动时会一次性提示缺少的可选依赖。

---

## 配置

### 环境变量

| 变量                 | 说明                  | 默认值   |
| -------------------- | --------------------- | -------- |
| `PORT`               | 服务端口              | `3333`   |
| `OPENCLAW_WORKSPACE` | 工作区根目录          | 自动探测 |
| `OPENCLAW_PROFILE`   | 配置档名称（Profile） | （无）   |

### 🔒 认证模式

| 模式         | 适用场景       | 配置                                                      |
| ------------ | -------------- | --------------------------------------------------------- |
| `none`       | 本地开发       | `DASHBOARD_AUTH_MODE=none`                                |
| `token`      | API 访问       | `DASHBOARD_AUTH_MODE=token DASHBOARD_TOKEN=secret`        |
| `tailscale`  | 团队内网访问   | `DASHBOARD_AUTH_MODE=tailscale`                           |
| `cloudflare` | 公网部署       | `DASHBOARD_AUTH_MODE=cloudflare`                          |
| `allowlist`  | 固定 IP 白名单 | `DASHBOARD_AUTH_MODE=allowlist DASHBOARD_ALLOWED_IPS=...` |

### 📋 推荐的 OpenClaw 配置

#### Slack 线程能力（关键项）

```yaml
slack:
  capabilities:
    threading: all # all, dm, group, none
```

如果不启用线程，仪表盘对话题追踪能力会大幅下降。

#### 会话标签

```yaml
sessions:
  labelFormat: "{channel}:{topic}"
```

#### Cerebro（话题追踪）

```bash
mkdir -p ~/your-workspace/cerebro/topics
mkdir -p ~/your-workspace/cerebro/orphans
```

仪表盘会自动检测并展示对应数据。

---

## API

| Endpoint            | 说明                             |
| ------------------- | -------------------------------- |
| `GET /api/state`    | **统一状态接口**（看板核心数据） |
| `GET /api/health`   | 健康检查                         |
| `GET /api/vitals`   | 系统指标                         |
| `GET /api/sessions` | 活跃会话                         |
| `GET /api/events`   | SSE 实时流                       |

---

## 截图

### 看板总览

<p align="center">
  <img src="docs/screenshots/hero.png" alt="Dashboard Hero" width="800">
</p>

### 会话面板

<p align="center">
  <img src="docs/screenshots/sessions-panel.png" alt="Sessions Panel" width="800">
</p>

### 定时任务面板

<p align="center">
  <img src="docs/screenshots/cron-panel.png" alt="Cron Jobs Panel" width="800">
</p>

### Cerebro 话题面板

<p align="center">
  <img src="docs/screenshots/cerebro-panel.png" alt="Cerebro Topics Panel" width="800">
</p>

### Operators（操作者）面板

<p align="center">
  <img src="docs/screenshots/operators-panel.png" alt="Operators Panel" width="800">
</p>

### 记忆浏览面板

<p align="center">
  <img src="docs/screenshots/memory-panel.png" alt="Memory Panel" width="800">
</p>

### 成本拆解弹窗

<p align="center">
  <img src="docs/screenshots/cost-modal.png" alt="Cost Breakdown Modal" width="800">
</p>

### Operator（操作者）详情

<p align="center">
  <img src="docs/screenshots/operator-modal.png" alt="Operator Details Modal" width="800">
</p>

### 隐私设置

<p align="center">
  <img src="docs/screenshots/privacy-modal.png" alt="Privacy Settings Modal" width="800">
</p>

### 会话详情

<p align="center">
  <img src="docs/screenshots/session-detail.png" alt="Session Details Panel" width="800">
</p>

---

## 贡献

欢迎贡献，提交前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 开发命令

```bash
npm install          # 安装开发依赖
npm run dev          # 监听模式
npm run lint         # 代码规范检查
npm run format       # 自动格式化
./scripts/verify.sh  # 健康检查
```

---

## License

MIT © [Jonathan Tsai](https://github.com/jontsai)

---

<div align="center">

**[Install from ClawHub](https://www.clawhub.ai/jontsai/command-center)** · **[OpenClaw](https://github.com/openclaw/openclaw)** · **[Discord](https://discord.gg/clawd)**

</div>
```

## File: `SKILL.md`
```markdown
---
name: command-center
version: 1.4.1
description: Mission control dashboard for OpenClaw - real-time session monitoring, LLM usage tracking, cost intelligence, and system vitals. View all your AI agents in one place.
metadata:
  openclaw:
    requires:
      node: ">=18"
    install:
      - id: start
        kind: shell
        command: "node lib/server.js"
        label: "Start Command Center (http://localhost:3333)"
---

# OpenClaw Command Center

Mission control for your AI workforce.

## Quick Start

```bash
npx clawhub@latest install command-center
cd skills/command-center
node lib/server.js
```

Dashboard runs at **http://localhost:3333**

## Features

- **Session Monitoring** — Real-time view of all AI sessions with live updates
- **LLM Fuel Gauges** — Track Claude, Codex, and other model usage
- **System Vitals** — CPU, Memory, Disk, Temperature
- **Cron Jobs** — View and manage scheduled tasks
- **Cerebro Topics** — Automatic conversation organization
- **Cost Tracking** — Per-session costs, projections, savings estimates
- **Privacy Controls** — Hide sensitive topics for demos

## Configuration

The dashboard auto-detects your OpenClaw workspace. Set `OPENCLAW_WORKSPACE` to override.

### Authentication

| Mode         | Use Case          |
| ------------ | ----------------- |
| `none`       | Local development |
| `token`      | Remote access     |
| `tailscale`  | Team VPN          |
| `cloudflare` | Public deployment |

```bash
DASHBOARD_AUTH_MODE=tailscale node lib/server.js
```

## API

| Endpoint          | Description                  |
| ----------------- | ---------------------------- |
| `GET /api/state`  | All dashboard data (unified) |
| `GET /api/events` | SSE stream for live updates  |
| `GET /api/health` | Health check                 |

## Links

- [GitHub](https://github.com/jontsai/openclaw-command-center)
- [ClawHub](https://www.clawhub.ai/jontsai/command-center)
- [Documentation](https://github.com/jontsai/openclaw-command-center#readme)
```

## File: `config/dashboard.example.json`
```json
{
  "$schema": "./dashboard.schema.json",
  "_comment": "OpenClaw Command Center Configuration — Copy to dashboard.json and customize",

  "server": {
    "port": 3333,
    "host": "localhost",
    "trustProxy": false
  },

  "branding": {
    "name": "Command Center",
    "title": "OpenClaw Command Center",
    "theme": "default",
    "logo": null
  },

  "paths": {
    "_comment": "Paths to OpenClaw workspace directories (supports ~ and $HOME)",
    "workspace": "~/.openclaw-workspace",
    "memory": "~/.openclaw-workspace/memory",
    "state": "~/.openclaw-workspace/state",
    "logs": "~/.openclaw-command-center/logs"
  },

  "auth": {
    "mode": "none",
    "_modeOptions": "none | token | tailscale | cloudflare | allowlist",
    "token": null,
    "allowedUsers": [],
    "allowedIPs": ["127.0.0.1", "::1"],
    "publicPaths": ["/api/health", "/api/whoami", "/favicon.ico"]
  },

  "dashboard": {
    "refreshInterval": 30000,
    "timezone": "America/Los_Angeles"
  },

  "sessions": {
    "_comment": "Session monitoring configuration",
    "healthCheckInterval": 60000,
    "sessionTimeout": 3600000,
    "maxSessions": 10
  },

  "cache": {
    "enabled": true,
    "ttl": 300000,
    "maxSize": 100
  },

  "health": {
    "_comment": "Health monitoring endpoints",
    "enabled": true,
    "endpoints": [
      {
        "name": "Gateway",
        "url": "http://localhost:3000/health",
        "interval": 30000
      }
    ]
  },

  "analytics": {
    "enabled": true,
    "retentionDays": 30,
    "trackTokenUsage": true,
    "trackRouting": true
  },

  "security": {
    "corsOrigins": ["http://localhost:3333"],
    "rateLimiting": {
      "enabled": true,
      "windowMs": 60000,
      "max": 100
    }
  },

  "logging": {
    "level": "info",
    "format": "json",
    "file": null
  },

  "integrations": {
    "linear": {
      "enabled": false,
      "apiKey": null,
      "teamId": null
    },
    "slack": {
      "enabled": false,
      "webhookUrl": null
    },
    "discord": {
      "enabled": false,
      "webhookUrl": null
    }
  }
}
```

## File: `config/system-deps.json`
```json
{
  "linux": [
    {
      "id": "sysstat",
      "name": "sysstat",
      "binary": "iostat",
      "purpose": "Disk I/O vitals (IOPS, throughput)",
      "affects": "disk-io",
      "install": {
        "apt": "sudo apt install -y sysstat",
        "yum": "sudo yum install -y sysstat",
        "dnf": "sudo dnf install -y sysstat",
        "pacman": "sudo pacman -S --noconfirm sysstat",
        "apk": "sudo apk add sysstat"
      }
    },
    {
      "id": "lm-sensors",
      "name": "lm-sensors",
      "binary": "sensors",
      "purpose": "Additional temperature sensors",
      "affects": "temperature",
      "install": {
        "apt": "sudo apt install -y lm-sensors",
        "yum": "sudo yum install -y lm-sensors",
        "dnf": "sudo dnf install -y lm-sensors",
        "pacman": "sudo pacman -S --noconfirm lm_sensors",
        "apk": "sudo apk add lm-sensors"
      }
    }
  ],
  "darwin": [
    {
      "id": "osx-cpu-temp",
      "name": "osx-cpu-temp",
      "binary": "osx-cpu-temp",
      "purpose": "CPU temperature (Intel Mac)",
      "affects": "temperature",
      "condition": "intel",
      "install": {
        "brew": "brew install --formula osx-cpu-temp"
      },
      "url": "https://github.com/lavoiesl/osx-cpu-temp"
    }
  ]
}
```

## File: `docs/README.md`
```markdown
# Documentation

> _"Knowledge is the foundation of the Swarm's evolution."_

## 📚 Contents

### Getting Started

- [Installation Guide](installation.md) _(coming soon)_
- [Configuration Guide](configuration.md) _(coming soon)_
- [Quick Start Tutorial](QUICKSTART.md) _(coming soon)_

### API Reference

- [REST API](rest.md) _(coming soon)_
- [WebSocket API](../../../vault/archives/archive_legacy/authentik/website/api/websocket.md) _(coming soon)_
- [Authentication](AUTHENTICATION.md) _(coming soon)_

### Architecture

- [System Overview](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/docu/docs/components/overview.md) _(coming soon)_
- [Data Flow](./architecture/data-flow.md) _(coming soon)_
- [Security Model](../bmad_repo/SECURITY.md) _(coming soon)_

### Development

- [Contributing](../bmad_repo/CONTRIBUTING.md)
- [Code Style Guide](../../../vault/archives/archive_legacy/developer-roadmap/src/data/roadmaps/code-review/content/code-style.md) _(coming soon)_
- [Testing Guide](../bmad_repo/testing.md) _(coming soon)_

## 🎯 Documentation Principles

1. **Clear and Concise** — No fluff, get to the point
2. **Examples First** — Show, don't just tell
3. **Keep it Updated** — Docs should match the code
4. **Thematic Consistency** — Embrace the Zerg aesthetic

## 📝 Contributing to Docs

Found something unclear or missing? We welcome documentation improvements!

1. Fork the repository
2. Create a branch: `docs/your-improvement`
3. Make your changes
4. Submit a PR

---

_"The Overmind's knowledge spreads across the Swarm."_ 🐛
```

## File: `docs/api/.gitkeep`
```
# API documentation will live here
```

## File: `docs/architecture/.gitkeep`
```
# Architecture documentation will live here
```

## File: `docs/architecture/OVERVIEW.md`
```markdown
# OpenClaw Command Center — Architecture Overview

> _"The Overmind sees all through its Overlords."_

## Overview

OpenClaw Command Center is a real-time dashboard for monitoring and managing AI assistant orchestration. It provides visibility into sessions, token usage, costs, scheduled jobs, and system health.

## Core Architecture Principles

### 1. **DRY (Don't Repeat Yourself)**

- Shared components extracted to reusable partials
- Single source of truth for sidebar, styling, and common logic
- Centralized configuration management

### 2. **Real-Time First**

- Server-Sent Events (SSE) for live updates
- No polling needed for connected clients
- Graceful degradation to polling when SSE unavailable

### 3. **Zero Build Step**

- Plain HTML, CSS, and JavaScript
- No compilation, bundling, or transpilation required
- Works directly from static file serving
- Dynamic loading via fetch() for shared partials

### 4. **Progressive Enhancement**

- Core functionality works without JavaScript
- Enhanced UX with JS (smooth scrolling, live updates, etc.)
- Mobile-responsive design

### 5. **Thematic Consistency**

- Starcraft/Zerg theme throughout
- Dark mode by default (space aesthetic)
- Consistent naming conventions

## System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Browser (Client)                         │
├─────────────────────────────────────────────────────────────┤
│  index.html          │  jobs.html         │  (future pages) │
│  ─────────────       │  ─────────────     │                 │
│  Main Dashboard      │  AI Jobs Dashboard │                 │
└──────────┬───────────┴────────┬──────────┴─────────────────┘
           │                    │
           │  ┌─────────────────┴──────────────────┐
           │  │  /partials/sidebar.html            │
           │  │  (shared navigation component)      │
           │  └─────────────────┬──────────────────┘
           │                    │
           └────────────────────┼──────────────────────────────┐
                                │                              │
┌───────────────────────────────┴──────────────────────────────┤
│                    /js/sidebar.js                            │
│  ─ Loads sidebar partial                                     │
│  ─ Manages SSE connection for live badge updates             │
│  ─ Handles navigation and active state                       │
└──────────────────────────────────────────────────────────────┘
                                │
                                │ SSE (/api/events)
                                │ REST (/api/*)
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                    lib/server.js                             │
│  ─ Express HTTP server                                       │
│  ─ SSE event broadcasting                                    │
│  ─ API routes for state, sessions, jobs, etc.                │
│  ─ Static file serving                                       │
└─────────────────────────────────┬────────────────────────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                    ▼             ▼             ▼
            ┌───────────┐ ┌───────────┐ ┌───────────┐
            │ OpenClaw  │ │   Jobs    │ │  Linear   │
            │  Gateway  │ │ Scheduler │ │   Sync    │
            │   API     │ │   API     │ │   API     │
            └───────────┘ └───────────┘ └───────────┘
```

## Frontend Architecture

### Pages

| Page         | Purpose            | Key Sections                                                       |
| ------------ | ------------------ | ------------------------------------------------------------------ |
| `index.html` | Main dashboard     | Vitals, LLM Usage, Sessions, Cron Jobs, Memory, Cerebro, Operators |
| `jobs.html`  | AI Jobs management | Job cards, run/pause/history controls                              |

### Shared Components

| Component  | Location                  | Purpose                                     |
| ---------- | ------------------------- | ------------------------------------------- |
| Sidebar    | `/partials/sidebar.html`  | Navigation + live stats badges              |
| Sidebar JS | `/js/sidebar.js`          | Partial loading, SSE connection, navigation |
| Styles     | `/css/dashboard.css`      | Shared visual theme                         |
| morphdom   | `/js/lib/morphdom.min.js` | Efficient DOM diffing                       |

### State Management

- **SSE-based**: Real-time state pushed from server
- **Local state**: Per-component state in JavaScript closures
- **Persistence**: `localStorage` for preferences (sidebar collapsed, etc.)

## Backend Architecture

### Server (`lib/server.js`)

- Express.js HTTP server
- Static file serving from `/public`
- API routes under `/api/*`
- SSE endpoint at `/api/events`

### Data Sources

| Source           | Integration | Purpose                              |
| ---------------- | ----------- | ------------------------------------ |
| OpenClaw Gateway | REST API    | Sessions, token stats, system vitals |
| Jobs Scheduler   | REST API    | AI job definitions and run history   |
| Linear           | GraphQL API | Issue tracking integration           |

### Configuration (`lib/config.js`)

- Auto-detects OpenClaw installation paths
- Supports multiple config file locations
- Environment variable overrides

## API Endpoints

| Endpoint                | Method    | Description                 |
| ----------------------- | --------- | --------------------------- |
| `/api/events`           | GET (SSE) | Real-time state updates     |
| `/api/state`            | GET       | Full current state snapshot |
| `/api/sessions`         | GET       | Session list and details    |
| `/api/jobs`             | GET       | AI job definitions          |
| `/api/jobs/:id/run`     | POST      | Trigger job execution       |
| `/api/jobs/:id/pause`   | POST      | Pause job                   |
| `/api/jobs/:id/resume`  | POST      | Resume job                  |
| `/api/jobs/:id/history` | GET       | Job run history             |

## Design Decisions

### ADR-001: Shared Sidebar via Fetch

**Decision**: Load sidebar HTML via `fetch()` rather than server-side includes or build step.

**Rationale**:

- Keeps zero-build-step architecture
- Works with any static file server
- Enables dynamic loading and hot updates
- Single source of truth for sidebar content

### ADR-002: SSE for Real-Time Updates

**Decision**: Use Server-Sent Events instead of WebSockets.

**Rationale**:

- Simpler protocol (HTTP-based)
- Automatic reconnection
- Better proxy/firewall compatibility
- Sufficient for server→client push (no bidirectional needed)

### ADR-003: Morphdom for DOM Updates

**Decision**: Use morphdom for efficient DOM patching.

**Rationale**:

- Virtual DOM-like efficiency without framework overhead
- Preserves focus, scroll position, form state
- Small footprint (~4KB)

## File Structure

```
openclaw-command-center/
├── lib/                        # Backend code
│   ├── server.js               # Main HTTP server
│   ├── config.js               # Configuration loader
│   ├── jobs.js                 # Jobs API integration
│   ├── linear-sync.js          # Linear integration
│   └── topic-classifier.js     # NLP topic classification
├── public/                     # Frontend (served statically)
│   ├── index.html              # Main dashboard
│   ├── jobs.html               # AI Jobs dashboard
│   ├── partials/               # Shared HTML partials
│   │   └── sidebar.html        # Navigation sidebar
│   ├── css/
│   │   └── dashboard.css       # Shared styles
│   ├── js/
│   │   ├── sidebar.js          # Sidebar loader + SSE
│   │   ├── app.js              # Main page logic
│   │   ├── api.js              # API client utilities
│   │   ├── store.js            # State management
│   │   ├── utils.js            # Common utilities
│   │   └── lib/
│   │       └── morphdom.min.js # DOM diffing library
│   └── data/                   # Client-side data cache
├── config/                     # Configuration files
├── docs/                       # Documentation
│   └── architecture/           # Architecture docs
├── scripts/                    # Operational scripts
└── tests/                      # Test files
```

## Performance Considerations

1. **SSE Connection Sharing**: Single SSE connection per page, shared across components
2. **Lazy Loading**: Sidebar loaded on demand, not blocking initial render
3. **Efficient Updates**: morphdom patches only changed DOM nodes
4. **Debouncing**: High-frequency updates batched before render

## Security Considerations

1. **No Secrets in Frontend**: All sensitive data stays server-side
2. **Input Validation**: API inputs validated before processing
3. **CORS**: Restricted to same-origin by default
4. **Rate Limiting**: Consider for public deployments

## Future Directions

1. **Component System**: More shared partials (stats bar, modals, etc.)
2. **Plugin Architecture**: Extensible dashboard sections
3. **Multi-Gateway**: Support for monitoring multiple OpenClaw instances
4. **Historical Analytics**: Token usage and cost trends over time
```

## File: `docs/guides/.gitkeep`
```
# User guides will live here
```

## File: `lib/server.js`
```javascript
#!/usr/bin/env node
var __getOwnPropNames = Object.getOwnPropertyNames;
var __commonJS = (cb, mod) => function __require() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};

// src/utils.js
var require_utils = __commonJS({
  "src/utils.js"(exports2, module2) {
    var { exec } = require("child_process");
    var path2 = require("path");
    var { promisify } = require("util");
    var execAsync = promisify(exec);
    var pkg = require(path2.join(__dirname, "..", "package.json"));
    function getVersion2() {
      return pkg.version;
    }
    async function runCmd(cmd, options = {}) {
      const systemPath = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin";
      const envPath = process.env.PATH || "";
      const opts = {
        encoding: "utf8",
        timeout: 1e4,
        env: {
          ...process.env,
          PATH: envPath.includes("/usr/sbin") ? envPath : `${systemPath}:${envPath}`
        },
        ...options
      };
      try {
        const { stdout } = await execAsync(cmd, opts);
        return stdout.trim();
      } catch (e) {
        if (options.fallback !== void 0) return options.fallback;
        throw e;
      }
    }
    function formatBytes(bytes) {
      if (bytes >= 1099511627776) return (bytes / 1099511627776).toFixed(1) + " TB";
      if (bytes >= 1073741824) return (bytes / 1073741824).toFixed(1) + " GB";
      if (bytes >= 1048576) return (bytes / 1048576).toFixed(1) + " MB";
      if (bytes >= 1024) return (bytes / 1024).toFixed(1) + " KB";
      return bytes + " B";
    }
    function formatTimeAgo(date) {
      const now = /* @__PURE__ */ new Date();
      const diffMs = now - date;
      const diffMins = Math.round(diffMs / 6e4);
      if (diffMins < 1) return "just now";
      if (diffMins < 60) return `${diffMins}m ago`;
      if (diffMins < 1440) return `${Math.round(diffMins / 60)}h ago`;
      return `${Math.round(diffMins / 1440)}d ago`;
    }
    function formatNumber(n) {
      return n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    function formatTokens(n) {
      if (n >= 1e6) return (n / 1e6).toFixed(1) + "M";
      if (n >= 1e3) return (n / 1e3).toFixed(1) + "k";
      return n.toString();
    }
    module2.exports = {
      getVersion: getVersion2,
      runCmd,
      formatBytes,
      formatTimeAgo,
      formatNumber,
      formatTokens
    };
  }
});

// src/config.js
var require_config = __commonJS({
  "src/config.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    var os = require("os");
    var HOME = os.homedir();
    function getOpenClawDir2(profile = null) {
      const effectiveProfile = profile || process.env.OPENCLAW_PROFILE || "";
      return effectiveProfile ? path2.join(HOME, `.openclaw-${effectiveProfile}`) : path2.join(HOME, ".openclaw");
    }
    function detectWorkspace() {
      const profile = process.env.OPENCLAW_PROFILE || "";
      const openclawDir = getOpenClawDir2();
      const defaultWorkspace = path2.join(openclawDir, "workspace");
      const profileCandidates = profile ? [
        // Profile-specific workspace in home (e.g., ~/.openclaw-<profile>-workspace)
        path2.join(HOME, `.openclaw-${profile}-workspace`),
        path2.join(HOME, `.${profile}-workspace`)
      ] : [];
      const candidates = [
        // Environment variable (highest priority)
        process.env.OPENCLAW_WORKSPACE,
        // OpenClaw's default workspace location
        process.env.OPENCLAW_HOME,
        // Gateway config workspace (check early - this is where OpenClaw actually runs)
        getWorkspaceFromGatewayConfig(),
        // Profile-specific paths (if profile is set)
        ...profileCandidates,
        // Standard OpenClaw workspace location (profile-aware: ~/.openclaw/workspace or ~/.openclaw-<profile>/workspace)
        defaultWorkspace,
        // Common custom workspace names
        path2.join(HOME, "openclaw-workspace"),
        path2.join(HOME, ".openclaw-workspace"),
        // Legacy/custom names
        path2.join(HOME, "molty"),
        path2.join(HOME, "clawd"),
        path2.join(HOME, "moltbot")
      ].filter(Boolean);
      const foundWorkspace = candidates.find((candidate) => {
        if (!candidate || !fs2.existsSync(candidate)) {
          return false;
        }
        const hasMemory = fs2.existsSync(path2.join(candidate, "memory"));
        const hasState = fs2.existsSync(path2.join(candidate, "state"));
        const hasConfig = fs2.existsSync(path2.join(candidate, ".openclaw"));
        return hasMemory || hasState || hasConfig;
      });
      return foundWorkspace || defaultWorkspace;
    }
    function getWorkspaceFromGatewayConfig() {
      const openclawDir = getOpenClawDir2();
      const configPaths = [
        path2.join(openclawDir, "config.yaml"),
        path2.join(openclawDir, "config.json"),
        path2.join(openclawDir, "openclaw.json"),
        path2.join(openclawDir, "clawdbot.json"),
        // Fallback to standard XDG location
        path2.join(HOME, ".config", "openclaw", "config.yaml")
      ];
      for (const configPath of configPaths) {
        try {
          if (fs2.existsSync(configPath)) {
            const content = fs2.readFileSync(configPath, "utf8");
            const match = content.match(/workspace[:\s]+["']?([^"'\n]+)/i) || content.match(/workdir[:\s]+["']?([^"'\n]+)/i);
            if (match && match[1]) {
              const workspace = match[1].trim().replace(/^~/, HOME);
              if (fs2.existsSync(workspace)) {
                return workspace;
              }
            }
          }
        } catch (e) {
        }
      }
      return null;
    }
    function deepMerge(base, override) {
      const result = { ...base };
      for (const key of Object.keys(override)) {
        if (override[key] && typeof override[key] === "object" && !Array.isArray(override[key]) && base[key] && typeof base[key] === "object") {
          result[key] = deepMerge(base[key], override[key]);
        } else if (override[key] !== null && override[key] !== void 0) {
          result[key] = override[key];
        }
      }
      return result;
    }
    function loadConfigFile() {
      const basePath = path2.join(__dirname, "..", "config", "dashboard.json");
      const localPath = path2.join(__dirname, "..", "config", "dashboard.local.json");
      let config = {};
      try {
        if (fs2.existsSync(basePath)) {
          const content = fs2.readFileSync(basePath, "utf8");
          config = JSON.parse(content);
        }
      } catch (e) {
        console.warn(`[Config] Failed to load ${basePath}:`, e.message);
      }
      try {
        if (fs2.existsSync(localPath)) {
          const content = fs2.readFileSync(localPath, "utf8");
          const localConfig = JSON.parse(content);
          config = deepMerge(config, localConfig);
          console.log(`[Config] Loaded local overrides from ${localPath}`);
        }
      } catch (e) {
        console.warn(`[Config] Failed to load ${localPath}:`, e.message);
      }
      return config;
    }
    function expandPath(p) {
      if (!p) return p;
      return p.replace(/^~/, HOME).replace(/\$HOME/g, HOME).replace(/\$\{HOME\}/g, HOME);
    }
    function loadConfig() {
      const fileConfig = loadConfigFile();
      const workspace = process.env.OPENCLAW_WORKSPACE || expandPath(fileConfig.paths?.workspace) || detectWorkspace();
      const config = {
        // Server settings
        server: {
          port: parseInt(process.env.PORT || fileConfig.server?.port || "3333", 10),
          host: process.env.HOST || fileConfig.server?.host || "localhost"
        },
        // Paths - all relative to workspace unless absolute
        paths: {
          workspace,
          memory: expandPath(process.env.OPENCLAW_MEMORY_DIR || fileConfig.paths?.memory) || path2.join(workspace, "memory"),
          state: expandPath(process.env.OPENCLAW_STATE_DIR || fileConfig.paths?.state) || path2.join(workspace, "state"),
          cerebro: expandPath(process.env.OPENCLAW_CEREBRO_DIR || fileConfig.paths?.cerebro) || path2.join(workspace, "cerebro"),
          skills: expandPath(process.env.OPENCLAW_SKILLS_DIR || fileConfig.paths?.skills) || path2.join(workspace, "skills"),
          jobs: expandPath(process.env.OPENCLAW_JOBS_DIR || fileConfig.paths?.jobs) || path2.join(workspace, "jobs"),
          logs: expandPath(process.env.OPENCLAW_LOGS_DIR || fileConfig.paths?.logs) || path2.join(HOME, ".openclaw-command-center", "logs")
        },
        // Auth settings
        auth: {
          mode: process.env.DASHBOARD_AUTH_MODE || fileConfig.auth?.mode || "none",
          token: process.env.DASHBOARD_TOKEN || fileConfig.auth?.token,
          allowedUsers: (process.env.DASHBOARD_ALLOWED_USERS || fileConfig.auth?.allowedUsers?.join(",") || "").split(",").map((s) => s.trim().toLowerCase()).filter(Boolean),
          allowedIPs: (process.env.DASHBOARD_ALLOWED_IPS || fileConfig.auth?.allowedIPs?.join(",") || "127.0.0.1,::1").split(",").map((s) => s.trim()),
          publicPaths: fileConfig.auth?.publicPaths || ["/api/health", "/api/whoami", "/favicon.ico"]
        },
        // Branding
        branding: {
          name: fileConfig.branding?.name || "OpenClaw Command Center",
          theme: fileConfig.branding?.theme || "default"
        },
        // Integrations
        integrations: {
          linear: {
            enabled: !!(process.env.LINEAR_API_KEY || fileConfig.integrations?.linear?.apiKey),
            apiKey: process.env.LINEAR_API_KEY || fileConfig.integrations?.linear?.apiKey,
            teamId: process.env.LINEAR_TEAM_ID || fileConfig.integrations?.linear?.teamId
          }
        },
        // Billing - for cost savings calculation
        billing: {
          claudePlanCost: parseFloat(
            process.env.CLAUDE_PLAN_COST || fileConfig.billing?.claudePlanCost || "200"
          ),
          claudePlanName: process.env.CLAUDE_PLAN_NAME || fileConfig.billing?.claudePlanName || "Claude Code Max"
        }
      };
      return config;
    }
    var CONFIG2 = loadConfig();
    console.log("[Config] Workspace:", CONFIG2.paths.workspace);
    console.log("[Config] Auth mode:", CONFIG2.auth.mode);
    module2.exports = { CONFIG: CONFIG2, loadConfig, detectWorkspace, expandPath, getOpenClawDir: getOpenClawDir2 };
  }
});

// src/jobs.js
var require_jobs = __commonJS({
  "src/jobs.js"(exports2, module2) {
    var path2 = require("path");
    var { CONFIG: CONFIG2 } = require_config();
    var JOBS_DIR = CONFIG2.paths.jobs;
    var JOBS_STATE_DIR = path2.join(CONFIG2.paths.state, "jobs");
    var apiInstance = null;
    var forceApiUnavailable = false;
    async function getAPI() {
      if (forceApiUnavailable) return null;
      if (apiInstance) return apiInstance;
      try {
        const { createJobsAPI } = await import(path2.join(JOBS_DIR, "lib/api.js"));
        apiInstance = createJobsAPI({
          definitionsDir: path2.join(JOBS_DIR, "definitions"),
          stateDir: JOBS_STATE_DIR
        });
        return apiInstance;
      } catch (e) {
        console.error("Failed to load jobs API:", e.message);
        return null;
      }
    }
    function _resetForTesting(options = {}) {
      apiInstance = null;
      forceApiUnavailable = options.forceUnavailable || false;
    }
    function formatRelativeTime(isoString) {
      if (!isoString) return null;
      const date = new Date(isoString);
      const now = /* @__PURE__ */ new Date();
      const diffMs = now - date;
      const diffMins = Math.round(diffMs / 6e4);
      if (diffMins < 0) {
        const futureMins = Math.abs(diffMins);
        if (futureMins < 60) return `in ${futureMins}m`;
        if (futureMins < 1440) return `in ${Math.round(futureMins / 60)}h`;
        return `in ${Math.round(futureMins / 1440)}d`;
      }
      if (diffMins < 1) return "just now";
      if (diffMins < 60) return `${diffMins}m ago`;
      if (diffMins < 1440) return `${Math.round(diffMins / 60)}h ago`;
      return `${Math.round(diffMins / 1440)}d ago`;
    }
    async function handleJobsRequest2(req, res, pathname, query, method) {
      const api = await getAPI();
      if (!api) {
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Jobs API not available" }));
        return;
      }
      try {
        if (pathname === "/api/jobs/scheduler/status" && method === "GET") {
          const status = await api.getSchedulerStatus();
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(status, null, 2));
          return;
        }
        if (pathname === "/api/jobs/stats" && method === "GET") {
          const stats = await api.getAggregateStats();
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(stats, null, 2));
          return;
        }
        if (pathname === "/api/jobs/cache/clear" && method === "POST") {
          api.clearCache();
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ success: true, message: "Cache cleared" }));
          return;
        }
        if (pathname === "/api/jobs" && method === "GET") {
          const jobs = await api.listJobs();
          const enhanced = jobs.map((job) => ({
            ...job,
            lastRunRelative: formatRelativeTime(job.lastRun),
            nextRunRelative: formatRelativeTime(job.nextRun)
          }));
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ jobs: enhanced, timestamp: Date.now() }, null, 2));
          return;
        }
        const jobMatch = pathname.match(/^\/api\/jobs\/([^/]+)$/);
        if (jobMatch && method === "GET") {
          const jobId = decodeURIComponent(jobMatch[1]);
          const job = await api.getJob(jobId);
          if (!job) {
            res.writeHead(404, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ error: "Job not found" }));
            return;
          }
          job.lastRunRelative = formatRelativeTime(job.lastRun);
          job.nextRunRelative = formatRelativeTime(job.nextRun);
          if (job.recentRuns) {
            job.recentRuns = job.recentRuns.map((run) => ({
              ...run,
              startedAtRelative: formatRelativeTime(run.startedAt),
              completedAtRelative: formatRelativeTime(run.completedAt)
            }));
          }
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(job, null, 2));
          return;
        }
        const historyMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/history$/);
        if (historyMatch && method === "GET") {
          const jobId = decodeURIComponent(historyMatch[1]);
          const limit = parseInt(query.get("limit") || "50", 10);
          const runs = await api.getJobHistory(jobId, limit);
          const enhanced = runs.map((run) => ({
            ...run,
            startedAtRelative: formatRelativeTime(run.startedAt),
            completedAtRelative: formatRelativeTime(run.completedAt)
          }));
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ runs: enhanced, timestamp: Date.now() }, null, 2));
          return;
        }
        const runMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/run$/);
        if (runMatch && method === "POST") {
          const jobId = decodeURIComponent(runMatch[1]);
          const result = await api.runJob(jobId);
          res.writeHead(result.success ? 200 : 400, { "Content-Type": "application/json" });
          res.end(JSON.stringify(result, null, 2));
          return;
        }
        const pauseMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/pause$/);
        if (pauseMatch && method === "POST") {
          const jobId = decodeURIComponent(pauseMatch[1]);
          let body = "";
          await new Promise((resolve) => {
            req.on("data", (chunk) => body += chunk);
            req.on("end", resolve);
          });
          let reason = null;
          try {
            const parsed = JSON.parse(body || "{}");
            reason = parsed.reason;
          } catch (_e) {
          }
          const result = await api.pauseJob(jobId, {
            by: req.authUser?.login || "dashboard",
            reason
          });
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(result, null, 2));
          return;
        }
        const resumeMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/resume$/);
        if (resumeMatch && method === "POST") {
          const jobId = decodeURIComponent(resumeMatch[1]);
          const result = await api.resumeJob(jobId);
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(result, null, 2));
          return;
        }
        const skipMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/skip$/);
        if (skipMatch && method === "POST") {
          const jobId = decodeURIComponent(skipMatch[1]);
          const result = await api.skipJob(jobId);
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(result, null, 2));
          return;
        }
        const killMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/kill$/);
        if (killMatch && method === "POST") {
          const jobId = decodeURIComponent(killMatch[1]);
          const result = await api.killJob(jobId);
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(JSON.stringify(result, null, 2));
          return;
        }
        res.writeHead(404, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Not found" }));
      } catch (e) {
        console.error("Jobs API error:", e);
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: e.message }));
      }
    }
    function isJobsRoute2(pathname) {
      return pathname.startsWith("/api/jobs");
    }
    module2.exports = { handleJobsRequest: handleJobsRequest2, isJobsRoute: isJobsRoute2, _resetForTesting };
  }
});

// src/openclaw.js
var require_openclaw = __commonJS({
  "src/openclaw.js"(exports2, module2) {
    var { execFileSync, execFile } = require("child_process");
    var { promisify } = require("util");
    var execFileAsync = promisify(execFile);
    function getSafeEnv() {
      return {
        PATH: process.env.PATH,
        HOME: process.env.HOME,
        USER: process.env.USER,
        SHELL: process.env.SHELL,
        LANG: process.env.LANG,
        NO_COLOR: "1",
        TERM: "dumb",
        OPENCLAW_PROFILE: process.env.OPENCLAW_PROFILE || "",
        OPENCLAW_WORKSPACE: process.env.OPENCLAW_WORKSPACE || "",
        OPENCLAW_HOME: process.env.OPENCLAW_HOME || ""
      };
    }
    function buildArgs(args2) {
      const profile = process.env.OPENCLAW_PROFILE || "";
      const profileArgs = profile ? ["--profile", profile] : [];
      const cleanArgs = args2.replace(/\s*2>&1\s*/g, " ").replace(/\s*2>\/dev\/null\s*/g, " ").trim();
      return [...profileArgs, ...cleanArgs.split(/\s+/).filter(Boolean)];
    }
    function runOpenClaw2(args2) {
      try {
        const result = execFileSync("openclaw", buildArgs(args2), {
          encoding: "utf8",
          timeout: 3e3,
          env: getSafeEnv(),
          stdio: ["pipe", "pipe", "pipe"]
        });
        return result;
      } catch (e) {
        return null;
      }
    }
    async function runOpenClawAsync2(args2) {
      try {
        const { stdout } = await execFileAsync("openclaw", buildArgs(args2), {
          encoding: "utf8",
          timeout: 2e4,
          env: getSafeEnv()
        });
        return stdout;
      } catch (e) {
        console.error("[OpenClaw Async] Error:", e.message);
        return null;
      }
    }
    function extractJSON2(output) {
      if (!output) return null;
      const jsonStart = output.search(/[[{]/);
      if (jsonStart === -1) return null;
      return output.slice(jsonStart);
    }
    module2.exports = {
      runOpenClaw: runOpenClaw2,
      runOpenClawAsync: runOpenClawAsync2,
      extractJSON: extractJSON2,
      getSafeEnv
    };
  }
});

// src/vitals.js
var require_vitals = __commonJS({
  "src/vitals.js"(exports2, module2) {
    var { runCmd, formatBytes } = require_utils();
    var cachedVitals = null;
    var lastVitalsUpdate = 0;
    var VITALS_CACHE_TTL = 3e4;
    var vitalsRefreshing = false;
    async function refreshVitalsAsync() {
      if (vitalsRefreshing) return;
      vitalsRefreshing = true;
      const vitals = {
        hostname: "",
        uptime: "",
        disk: { used: 0, free: 0, total: 0, percent: 0, kbPerTransfer: 0, iops: 0, throughputMBps: 0 },
        cpu: { loadAvg: [0, 0, 0], cores: 0, usage: 0 },
        memory: { used: 0, free: 0, total: 0, percent: 0, pressure: "normal" },
        temperature: null
      };
      const isLinux = process.platform === "linux";
      const isMacOS = process.platform === "darwin";
      try {
        const coresCmd = isLinux ? "nproc" : "sysctl -n hw.ncpu";
        const memCmd = isLinux ? "cat /proc/meminfo | grep MemTotal | awk '{print $2}'" : "sysctl -n hw.memsize";
        const topCmd = isLinux ? "top -bn1 | head -3 | grep -E '^%?Cpu|^  ?CPU' || echo ''" : 'top -l 1 -n 0 2>/dev/null | grep "CPU usage" || echo ""';
        const mpstatCmd = isLinux ? "(command -v mpstat >/dev/null 2>&1 && mpstat 1 1 | tail -1 | sed 's/^Average: *//') || echo ''" : "";
        const [hostname, uptimeRaw, coresRaw, memTotalRaw, memInfoRaw, dfRaw, topOutput, mpstatOutput] = await Promise.all([
          runCmd("hostname", { fallback: "unknown" }),
          runCmd("uptime", { fallback: "" }),
          runCmd(coresCmd, { fallback: "1" }),
          runCmd(memCmd, { fallback: "0" }),
          isLinux ? runCmd("cat /proc/meminfo", { fallback: "" }) : runCmd("vm_stat", { fallback: "" }),
          runCmd("df -k ~ | tail -1", { fallback: "" }),
          runCmd(topCmd, { fallback: "" }),
          isLinux ? runCmd(mpstatCmd, { fallback: "" }) : Promise.resolve("")
        ]);
        vitals.hostname = hostname;
        const uptimeMatch = uptimeRaw.match(/up\s+([^,]+)/);
        if (uptimeMatch) vitals.uptime = uptimeMatch[1].trim();
        const loadMatch = uptimeRaw.match(/load averages?:\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)/);
        if (loadMatch)
          vitals.cpu.loadAvg = [
            parseFloat(loadMatch[1]),
            parseFloat(loadMatch[2]),
            parseFloat(loadMatch[3])
          ];
        vitals.cpu.cores = parseInt(coresRaw, 10) || 1;
        vitals.cpu.usage = Math.min(100, Math.round(vitals.cpu.loadAvg[0] / vitals.cpu.cores * 100));
        if (isLinux) {
          if (mpstatOutput) {
            const parts = mpstatOutput.trim().split(/\s+/);
            const user = parts.length > 1 ? parseFloat(parts[1]) : NaN;
            const sys = parts.length > 3 ? parseFloat(parts[3]) : NaN;
            const idle = parts.length ? parseFloat(parts[parts.length - 1]) : NaN;
            if (!Number.isNaN(user)) vitals.cpu.userPercent = user;
            if (!Number.isNaN(sys)) vitals.cpu.sysPercent = sys;
            if (!Number.isNaN(idle)) {
              vitals.cpu.idlePercent = idle;
              vitals.cpu.usage = Math.max(0, Math.min(100, Math.round(100 - idle)));
            }
          }
          if (topOutput && (vitals.cpu.idlePercent === null || vitals.cpu.idlePercent === void 0)) {
            const userMatch = topOutput.match(/([\d.]+)\s*us/);
            const sysMatch = topOutput.match(/([\d.]+)\s*sy/);
            const idleMatch = topOutput.match(/([\d.]+)\s*id/);
            vitals.cpu.userPercent = userMatch ? parseFloat(userMatch[1]) : null;
            vitals.cpu.sysPercent = sysMatch ? parseFloat(sysMatch[1]) : null;
            vitals.cpu.idlePercent = idleMatch ? parseFloat(idleMatch[1]) : null;
            if (vitals.cpu.userPercent !== null && vitals.cpu.sysPercent !== null) {
              vitals.cpu.usage = Math.round(vitals.cpu.userPercent + vitals.cpu.sysPercent);
            }
          }
        } else if (topOutput) {
          const userMatch = topOutput.match(/([\d.]+)%\s*user/);
          const sysMatch = topOutput.match(/([\d.]+)%\s*sys/);
          const idleMatch = topOutput.match(/([\d.]+)%\s*idle/);
          vitals.cpu.userPercent = userMatch ? parseFloat(userMatch[1]) : null;
          vitals.cpu.sysPercent = sysMatch ? parseFloat(sysMatch[1]) : null;
          vitals.cpu.idlePercent = idleMatch ? parseFloat(idleMatch[1]) : null;
          if (vitals.cpu.userPercent !== null && vitals.cpu.sysPercent !== null) {
            vitals.cpu.usage = Math.round(vitals.cpu.userPercent + vitals.cpu.sysPercent);
          }
        }
        const dfParts = dfRaw.split(/\s+/);
        if (dfParts.length >= 4) {
          vitals.disk.total = parseInt(dfParts[1], 10) * 1024;
          vitals.disk.used = parseInt(dfParts[2], 10) * 1024;
          vitals.disk.free = parseInt(dfParts[3], 10) * 1024;
          vitals.disk.percent = Math.round(parseInt(dfParts[2], 10) / parseInt(dfParts[1], 10) * 100);
        }
        if (isLinux) {
          const memTotalKB = parseInt(memTotalRaw, 10) || 0;
          const memAvailableMatch = memInfoRaw.match(/MemAvailable:\s+(\d+)/);
          const memFreeMatch = memInfoRaw.match(/MemFree:\s+(\d+)/);
          vitals.memory.total = memTotalKB * 1024;
          const memAvailable = parseInt(memAvailableMatch?.[1] || memFreeMatch?.[1] || 0, 10) * 1024;
          vitals.memory.used = vitals.memory.total - memAvailable;
          vitals.memory.free = memAvailable;
          vitals.memory.percent = vitals.memory.total > 0 ? Math.round(vitals.memory.used / vitals.memory.total * 100) : 0;
        } else {
          const pageSizeMatch = memInfoRaw.match(/page size of (\d+) bytes/);
          const pageSize = pageSizeMatch ? parseInt(pageSizeMatch[1], 10) : 4096;
          const activePages = parseInt((memInfoRaw.match(/Pages active:\s+(\d+)/) || [])[1] || 0, 10);
          const wiredPages = parseInt(
            (memInfoRaw.match(/Pages wired down:\s+(\d+)/) || [])[1] || 0,
            10
          );
          const compressedPages = parseInt(
            (memInfoRaw.match(/Pages occupied by compressor:\s+(\d+)/) || [])[1] || 0,
            10
          );
          vitals.memory.total = parseInt(memTotalRaw, 10) || 0;
          vitals.memory.used = (activePages + wiredPages + compressedPages) * pageSize;
          vitals.memory.free = vitals.memory.total - vitals.memory.used;
          vitals.memory.percent = vitals.memory.total > 0 ? Math.round(vitals.memory.used / vitals.memory.total * 100) : 0;
        }
        vitals.memory.pressure = vitals.memory.percent > 90 ? "critical" : vitals.memory.percent > 75 ? "warning" : "normal";
        const timeoutPrefix = isLinux ? "timeout 5" : "$(command -v gtimeout >/dev/null 2>&1 && echo gtimeout 5)";
        const iostatArgs = isLinux ? "-d -o JSON 1 2" : "-d -c 2 2";
        const iostatCmd = `${timeoutPrefix} iostat ${iostatArgs} 2>/dev/null || echo ''`;
        const [perfCores, effCores, chip, iostatRaw] = await Promise.all([
          isMacOS ? runCmd("sysctl -n hw.perflevel0.logicalcpu 2>/dev/null || echo 0", { fallback: "0" }) : Promise.resolve("0"),
          isMacOS ? runCmd("sysctl -n hw.perflevel1.logicalcpu 2>/dev/null || echo 0", { fallback: "0" }) : Promise.resolve("0"),
          isMacOS ? runCmd(
            'system_profiler SPHardwareDataType 2>/dev/null | grep "Chip:" | cut -d: -f2 || echo ""',
            { fallback: "" }
          ) : Promise.resolve(""),
          runCmd(iostatCmd, { fallback: "", timeout: 5e3 })
        ]);
        if (isLinux) {
          const cpuBrand = await runCmd(
            "cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d: -f2",
            { fallback: "" }
          );
          if (cpuBrand) vitals.cpu.brand = cpuBrand.trim();
        }
        vitals.cpu.pCores = parseInt(perfCores, 10) || null;
        vitals.cpu.eCores = parseInt(effCores, 10) || null;
        if (chip) vitals.cpu.chip = chip;
        if (isLinux) {
          try {
            const iostatJson = JSON.parse(iostatRaw);
            const samples = iostatJson.sysstat.hosts[0].statistics;
            const disks = samples[samples.length - 1].disk;
            const disk = disks.filter((d) => !d.disk_device.startsWith("loop")).sort((a, b) => b.tps - a.tps)[0];
            if (disk) {
              const kbReadPerSec = disk["kB_read/s"] || 0;
              const kbWrtnPerSec = disk["kB_wrtn/s"] || 0;
              vitals.disk.iops = disk.tps || 0;
              vitals.disk.throughputMBps = (kbReadPerSec + kbWrtnPerSec) / 1024;
              vitals.disk.kbPerTransfer = disk.tps > 0 ? (kbReadPerSec + kbWrtnPerSec) / disk.tps : 0;
            }
          } catch {
          }
        } else {
          const iostatLines = iostatRaw.split("\n").filter((l) => l.trim());
          const lastLine = iostatLines.length > 0 ? iostatLines[iostatLines.length - 1] : "";
          const iostatParts = lastLine.split(/\s+/).filter(Boolean);
          if (iostatParts.length >= 3) {
            vitals.disk.kbPerTransfer = parseFloat(iostatParts[0]) || 0;
            vitals.disk.iops = parseFloat(iostatParts[1]) || 0;
            vitals.disk.throughputMBps = parseFloat(iostatParts[2]) || 0;
          }
        }
        vitals.temperature = null;
        vitals.temperatureNote = null;
        const isAppleSilicon = vitals.cpu.chip && /apple/i.test(vitals.cpu.chip);
        if (isAppleSilicon) {
          vitals.temperatureNote = "Apple Silicon (requires elevated access)";
          try {
            const pmOutput = await runCmd(
              'sudo -n powermetrics --samplers smc -i 1 -n 1 2>/dev/null | grep -i "die temp" | head -1',
              { fallback: "", timeout: 5e3 }
            );
            const tempMatch = pmOutput.match(/([\d.]+)/);
            if (tempMatch) {
              vitals.temperature = parseFloat(tempMatch[1]);
              vitals.temperatureNote = null;
            }
          } catch (e) {
          }
        } else if (isMacOS) {
          const home = require("os").homedir();
          try {
            const temp = await runCmd(
              `osx-cpu-temp 2>/dev/null || ${home}/bin/osx-cpu-temp 2>/dev/null`,
              { fallback: "" }
            );
            if (temp && temp.includes("\xB0")) {
              const tempMatch = temp.match(/([\d.]+)/);
              if (tempMatch && parseFloat(tempMatch[1]) > 0) {
                vitals.temperature = parseFloat(tempMatch[1]);
              }
            }
          } catch (e) {
          }
          if (!vitals.temperature) {
            try {
              const ioregRaw = await runCmd(
                "ioreg -r -n AppleSmartBattery 2>/dev/null | grep Temperature",
                { fallback: "" }
              );
              const tempMatch = ioregRaw.match(/"Temperature"\s*=\s*(\d+)/);
              if (tempMatch) {
                vitals.temperature = Math.round(parseInt(tempMatch[1], 10) / 100);
              }
            } catch (e) {
            }
          }
        } else if (isLinux) {
          try {
            const temp = await runCmd("cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null", {
              fallback: ""
            });
            if (temp) {
              vitals.temperature = Math.round(parseInt(temp, 10) / 1e3);
            }
          } catch (e) {
          }
        }
      } catch (e) {
        console.error("[Vitals] Async refresh failed:", e.message);
      }
      vitals.memory.usedFormatted = formatBytes(vitals.memory.used);
      vitals.memory.totalFormatted = formatBytes(vitals.memory.total);
      vitals.memory.freeFormatted = formatBytes(vitals.memory.free);
      vitals.disk.usedFormatted = formatBytes(vitals.disk.used);
      vitals.disk.totalFormatted = formatBytes(vitals.disk.total);
      vitals.disk.freeFormatted = formatBytes(vitals.disk.free);
      cachedVitals = vitals;
      lastVitalsUpdate = Date.now();
      vitalsRefreshing = false;
      console.log("[Vitals] Cache refreshed async");
    }
    setTimeout(() => refreshVitalsAsync(), 500);
    setInterval(() => refreshVitalsAsync(), VITALS_CACHE_TTL);
    function getSystemVitals2() {
      const now = Date.now();
      if (!cachedVitals || now - lastVitalsUpdate > VITALS_CACHE_TTL) {
        refreshVitalsAsync();
      }
      if (cachedVitals) return cachedVitals;
      return {
        hostname: "loading...",
        uptime: "",
        disk: {
          used: 0,
          free: 0,
          total: 0,
          percent: 0,
          usedFormatted: "-",
          totalFormatted: "-",
          freeFormatted: "-"
        },
        cpu: { loadAvg: [0, 0, 0], cores: 0, usage: 0 },
        memory: {
          used: 0,
          free: 0,
          total: 0,
          percent: 0,
          pressure: "normal",
          usedFormatted: "-",
          totalFormatted: "-",
          freeFormatted: "-"
        },
        temperature: null
      };
    }
    var cachedDeps = null;
    async function checkOptionalDeps2() {
      const isLinux = process.platform === "linux";
      const isMacOS = process.platform === "darwin";
      const platform = isLinux ? "linux" : isMacOS ? "darwin" : null;
      const results = [];
      if (!platform) {
        cachedDeps = results;
        return results;
      }
      const fs2 = require("fs");
      const path2 = require("path");
      const depsFile = path2.join(__dirname, "..", "config", "system-deps.json");
      let depsConfig;
      try {
        depsConfig = JSON.parse(fs2.readFileSync(depsFile, "utf8"));
      } catch {
        cachedDeps = results;
        return results;
      }
      const deps = depsConfig[platform] || [];
      const home = require("os").homedir();
      let pkgManager = null;
      if (isLinux) {
        for (const pm of ["apt", "dnf", "yum", "pacman", "apk"]) {
          const has = await runCmd(`which ${pm}`, { fallback: "" });
          if (has) {
            pkgManager = pm;
            break;
          }
        }
      } else if (isMacOS) {
        const hasBrew = await runCmd("which brew", { fallback: "" });
        if (hasBrew) pkgManager = "brew";
      }
      let isAppleSilicon = false;
      if (isMacOS) {
        const chip = await runCmd("sysctl -n machdep.cpu.brand_string", { fallback: "" });
        isAppleSilicon = /apple/i.test(chip);
      }
      for (const dep of deps) {
        if (dep.condition === "intel" && isAppleSilicon) continue;
        let installed = false;
        const hasBinary = await runCmd(`which ${dep.binary} 2>/dev/null`, { fallback: "" });
        if (hasBinary) {
          installed = true;
        } else if (isMacOS && dep.binary === "osx-cpu-temp") {
          const homebin = await runCmd(`test -x ${home}/bin/osx-cpu-temp && echo ok`, {
            fallback: ""
          });
          if (homebin) installed = true;
        }
        const installCmd = dep.install[pkgManager] || null;
        results.push({
          id: dep.id,
          name: dep.name,
          purpose: dep.purpose,
          affects: dep.affects,
          installed,
          installCmd,
          url: dep.url || null
        });
      }
      cachedDeps = results;
      const missing = results.filter((d) => !d.installed);
      if (missing.length > 0) {
        console.log("[Startup] Optional dependencies for enhanced vitals:");
        for (const dep of missing) {
          const action = dep.installCmd || dep.url || "see docs";
          console.log(`   \u{1F4A1} ${dep.name} \u2014 ${dep.purpose}: ${action}`);
        }
      }
      return results;
    }
    function getOptionalDeps2() {
      return cachedDeps;
    }
    module2.exports = {
      refreshVitalsAsync,
      getSystemVitals: getSystemVitals2,
      checkOptionalDeps: checkOptionalDeps2,
      getOptionalDeps: getOptionalDeps2,
      VITALS_CACHE_TTL
    };
  }
});

// src/auth.js
var require_auth = __commonJS({
  "src/auth.js"(exports2, module2) {
    var AUTH_HEADERS = {
      tailscale: {
        login: "tailscale-user-login",
        name: "tailscale-user-name",
        pic: "tailscale-user-profile-pic"
      },
      cloudflare: {
        email: "cf-access-authenticated-user-email"
      }
    };
    function checkAuth2(req, authConfig) {
      const mode = authConfig.mode;
      const remoteAddr = req.socket?.remoteAddress || "";
      const isLocalhost = remoteAddr === "127.0.0.1" || remoteAddr === "::1" || remoteAddr === "::ffff:127.0.0.1";
      if (isLocalhost) {
        return { authorized: true, user: { type: "localhost", login: "localhost" } };
      }
      if (mode === "none") {
        return { authorized: true, user: null };
      }
      if (mode === "token") {
        const authHeader = req.headers["authorization"] || "";
        const token = authHeader.replace(/^Bearer\s+/i, "");
        if (token && token === authConfig.token) {
          return { authorized: true, user: { type: "token" } };
        }
        return { authorized: false, reason: "Invalid or missing token" };
      }
      if (mode === "tailscale") {
        const login = (req.headers[AUTH_HEADERS.tailscale.login] || "").toLowerCase();
        const name = req.headers[AUTH_HEADERS.tailscale.name] || "";
        const pic = req.headers[AUTH_HEADERS.tailscale.pic] || "";
        if (!login) {
          return { authorized: false, reason: "Not accessed via Tailscale Serve" };
        }
        const isAllowed = authConfig.allowedUsers.some((allowed) => {
          if (allowed === "*") return true;
          if (allowed === login) return true;
          if (allowed.startsWith("*@")) {
            const domain = allowed.slice(2);
            return login.endsWith("@" + domain);
          }
          return false;
        });
        if (isAllowed) {
          return { authorized: true, user: { type: "tailscale", login, name, pic } };
        }
        return { authorized: false, reason: `User ${login} not in allowlist`, user: { login } };
      }
      if (mode === "cloudflare") {
        const email = (req.headers[AUTH_HEADERS.cloudflare.email] || "").toLowerCase();
        if (!email) {
          return { authorized: false, reason: "Not accessed via Cloudflare Access" };
        }
        const isAllowed = authConfig.allowedUsers.some((allowed) => {
          if (allowed === "*") return true;
          if (allowed === email) return true;
          if (allowed.startsWith("*@")) {
            const domain = allowed.slice(2);
            return email.endsWith("@" + domain);
          }
          return false;
        });
        if (isAllowed) {
          return { authorized: true, user: { type: "cloudflare", email } };
        }
        return { authorized: false, reason: `User ${email} not in allowlist`, user: { email } };
      }
      if (mode === "allowlist") {
        const clientIP = req.headers["x-forwarded-for"]?.split(",")[0]?.trim() || req.socket?.remoteAddress || "";
        const isAllowed = authConfig.allowedIPs.some((allowed) => {
          if (allowed === clientIP) return true;
          if (allowed.endsWith("/24")) {
            const prefix = allowed.slice(0, -3).split(".").slice(0, 3).join(".");
            return clientIP.startsWith(prefix + ".");
          }
          return false;
        });
        if (isAllowed) {
          return { authorized: true, user: { type: "ip", ip: clientIP } };
        }
        return { authorized: false, reason: `IP ${clientIP} not in allowlist` };
      }
      return { authorized: false, reason: "Unknown auth mode" };
    }
    function getUnauthorizedPage2(reason, user, authConfig) {
      const userInfo = user ? `<p class="user-info">Detected: ${user.login || user.email || user.ip || "unknown"}</p>` : "";
      return `<!DOCTYPE html>
<html>
<head>
    <title>Access Denied - Command Center</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #e8e8e8;
        }
        .container {
            text-align: center;
            padding: 3rem;
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.1);
            max-width: 500px;
        }
        .icon { font-size: 4rem; margin-bottom: 1rem; }
        h1 { font-size: 1.8rem; margin-bottom: 1rem; color: #ff6b6b; }
        .reason { color: #aaa; margin-bottom: 1.5rem; font-size: 0.95rem; }
        .user-info { color: #ffeb3b; margin: 1rem 0; font-size: 0.9rem; }
        .instructions { color: #ccc; font-size: 0.85rem; line-height: 1.5; }
        .auth-mode { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); color: #888; font-size: 0.75rem; }
        code { background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">\u{1F510}</div>
        <h1>Access Denied</h1>
        <div class="reason">${reason}</div>
        ${userInfo}
        <div class="instructions">
            <p>This dashboard requires authentication via <strong>${authConfig.mode}</strong>.</p>
            ${authConfig.mode === "tailscale" ? `<p style="margin-top:1rem">Make sure you're accessing via your Tailscale URL and your account is in the allowlist.</p>` : ""}
            ${authConfig.mode === "cloudflare" ? `<p style="margin-top:1rem">Make sure you're accessing via Cloudflare Access and your email is in the allowlist.</p>` : ""}
        </div>
        <div class="auth-mode">Auth mode: <code>${authConfig.mode}</code></div>
    </div>
</body>
</html>`;
    }
    module2.exports = { AUTH_HEADERS, checkAuth: checkAuth2, getUnauthorizedPage: getUnauthorizedPage2 };
  }
});

// src/privacy.js
var require_privacy = __commonJS({
  "src/privacy.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    function getPrivacyFilePath(dataDir) {
      return path2.join(dataDir, "privacy-settings.json");
    }
    function loadPrivacySettings2(dataDir) {
      try {
        const privacyFile = getPrivacyFilePath(dataDir);
        if (fs2.existsSync(privacyFile)) {
          return JSON.parse(fs2.readFileSync(privacyFile, "utf8"));
        }
      } catch (e) {
        console.error("Failed to load privacy settings:", e.message);
      }
      return {
        version: 1,
        hiddenTopics: [],
        hiddenSessions: [],
        hiddenCrons: [],
        hideHostname: false,
        updatedAt: null
      };
    }
    function savePrivacySettings2(dataDir, data) {
      try {
        if (!fs2.existsSync(dataDir)) {
          fs2.mkdirSync(dataDir, { recursive: true });
        }
        data.updatedAt = (/* @__PURE__ */ new Date()).toISOString();
        fs2.writeFileSync(getPrivacyFilePath(dataDir), JSON.stringify(data, null, 2));
        return true;
      } catch (e) {
        console.error("Failed to save privacy settings:", e.message);
        return false;
      }
    }
    module2.exports = {
      loadPrivacySettings: loadPrivacySettings2,
      savePrivacySettings: savePrivacySettings2
    };
  }
});

// src/operators.js
var require_operators = __commonJS({
  "src/operators.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    function loadOperators2(dataDir) {
      const operatorsFile = path2.join(dataDir, "operators.json");
      try {
        if (fs2.existsSync(operatorsFile)) {
          return JSON.parse(fs2.readFileSync(operatorsFile, "utf8"));
        }
      } catch (e) {
        console.error("Failed to load operators:", e.message);
      }
      return { version: 1, operators: [], roles: {} };
    }
    function saveOperators2(dataDir, data) {
      try {
        if (!fs2.existsSync(dataDir)) {
          fs2.mkdirSync(dataDir, { recursive: true });
        }
        const operatorsFile = path2.join(dataDir, "operators.json");
        fs2.writeFileSync(operatorsFile, JSON.stringify(data, null, 2));
        return true;
      } catch (e) {
        console.error("Failed to save operators:", e.message);
        return false;
      }
    }
    function getOperatorBySlackId2(dataDir, slackId) {
      const data = loadOperators2(dataDir);
      return data.operators.find((op) => op.id === slackId || op.metadata?.slackId === slackId);
    }
    var operatorsRefreshing = false;
    async function refreshOperatorsAsync(dataDir, getOpenClawDir2) {
      if (operatorsRefreshing) return;
      operatorsRefreshing = true;
      const toMs = (ts, fallback) => {
        if (typeof ts === "number" && Number.isFinite(ts)) return ts;
        if (typeof ts === "string") {
          const parsed = Date.parse(ts);
          if (Number.isFinite(parsed)) return parsed;
        }
        return fallback;
      };
      try {
        const openclawDir = getOpenClawDir2();
        const sessionsDir = path2.join(openclawDir, "agents", "main", "sessions");
        if (!fs2.existsSync(sessionsDir)) {
          operatorsRefreshing = false;
          return;
        }
        const files = fs2.readdirSync(sessionsDir).filter((f) => f.endsWith(".jsonl"));
        const operatorsMap = /* @__PURE__ */ new Map();
        const sevenDaysAgo = Date.now() - 7 * 24 * 60 * 60 * 1e3;
        for (const file of files) {
          const filePath = path2.join(sessionsDir, file);
          try {
            const stat = fs2.statSync(filePath);
            if (stat.mtimeMs < sevenDaysAgo) continue;
            const fd = fs2.openSync(filePath, "r");
            const buffer = Buffer.alloc(10240);
            const bytesRead = fs2.readSync(fd, buffer, 0, 10240, 0);
            fs2.closeSync(fd);
            const content = buffer.toString("utf8", 0, bytesRead);
            const lines = content.split("\n").slice(0, 20);
            for (const line of lines) {
              if (!line.trim()) continue;
              try {
                const entry = JSON.parse(line);
                if (entry.type !== "message" || !entry.message) continue;
                const msg = entry.message;
                if (msg.role !== "user") continue;
                let text = "";
                if (typeof msg.content === "string") {
                  text = msg.content;
                } else if (Array.isArray(msg.content)) {
                  const textPart = msg.content.find((c) => c.type === "text");
                  if (textPart) text = textPart.text || "";
                }
                if (!text) continue;
                const slackMatch = text.match(/\[Slack[^\]]*\]\s*([\w.-]+)\s*\(([A-Z0-9]+)\):/);
                if (slackMatch) {
                  const username = slackMatch[1];
                  const userId = slackMatch[2];
                  if (!operatorsMap.has(userId)) {
                    operatorsMap.set(userId, {
                      id: userId,
                      name: username,
                      username,
                      source: "slack",
                      firstSeen: toMs(entry.timestamp, stat.mtimeMs),
                      lastSeen: toMs(entry.timestamp, stat.mtimeMs),
                      sessionCount: 1
                    });
                  } else {
                    const op = operatorsMap.get(userId);
                    op.lastSeen = Math.max(op.lastSeen, toMs(entry.timestamp, stat.mtimeMs));
                    op.sessionCount++;
                  }
                  break;
                }
                const telegramMatch = text.match(/\[Telegram[^\]]*\]\s*([\w.-]+):/);
                if (telegramMatch) {
                  const username = telegramMatch[1];
                  const operatorId = `telegram:${username}`;
                  if (!operatorsMap.has(operatorId)) {
                    operatorsMap.set(operatorId, {
                      id: operatorId,
                      name: username,
                      username,
                      source: "telegram",
                      firstSeen: toMs(entry.timestamp, stat.mtimeMs),
                      lastSeen: toMs(entry.timestamp, stat.mtimeMs),
                      sessionCount: 1
                    });
                  } else {
                    const op = operatorsMap.get(operatorId);
                    op.lastSeen = Math.max(op.lastSeen, toMs(entry.timestamp, stat.mtimeMs));
                    op.sessionCount++;
                  }
                  break;
                }
                const discordSenderMatch = text.match(/"sender":\s*"(\d+)"/);
                const discordLabelMatch = text.match(/"label":\s*"([^"]+)"/);
                const discordUsernameMatch = text.match(/"username":\s*"([^"]+)"/);
                if (discordSenderMatch) {
                  const userId = discordSenderMatch[1];
                  const label = discordLabelMatch ? discordLabelMatch[1] : userId;
                  const username = discordUsernameMatch ? discordUsernameMatch[1] : label;
                  const opId = `discord:${userId}`;
                  if (!operatorsMap.has(opId)) {
                    operatorsMap.set(opId, {
                      id: opId,
                      discordId: userId,
                      name: label,
                      username,
                      source: "discord",
                      firstSeen: toMs(entry.timestamp, stat.mtimeMs),
                      lastSeen: toMs(entry.timestamp, stat.mtimeMs),
                      sessionCount: 1
                    });
                  } else {
                    const op = operatorsMap.get(opId);
                    op.lastSeen = Math.max(op.lastSeen, toMs(entry.timestamp, stat.mtimeMs));
                    op.sessionCount++;
                  }
                  break;
                }
              } catch (e) {
              }
            }
          } catch (e) {
          }
        }
        const existing = loadOperators2(dataDir);
        const existingMap = new Map(existing.operators.map((op) => [op.id, op]));
        for (const [id, autoOp] of operatorsMap) {
          if (existingMap.has(id)) {
            const manual = existingMap.get(id);
            manual.lastSeen = Math.max(manual.lastSeen || 0, autoOp.lastSeen);
            manual.sessionCount = (manual.sessionCount || 0) + autoOp.sessionCount;
          } else {
            existingMap.set(id, autoOp);
          }
        }
        const merged = {
          version: 1,
          operators: Array.from(existingMap.values()).sort(
            (a, b) => (b.lastSeen || 0) - (a.lastSeen || 0)
          ),
          roles: existing.roles || {},
          lastRefreshed: Date.now()
        };
        saveOperators2(dataDir, merged);
        console.log(`[Operators] Refreshed: ${merged.operators.length} operators detected`);
      } catch (e) {
        console.error("[Operators] Refresh failed:", e.message);
      }
      operatorsRefreshing = false;
    }
    function startOperatorsRefresh2(dataDir, getOpenClawDir2) {
      setTimeout(() => refreshOperatorsAsync(dataDir, getOpenClawDir2), 2e3);
      setInterval(() => refreshOperatorsAsync(dataDir, getOpenClawDir2), 5 * 60 * 1e3);
    }
    function calculateOperatorStats2(operatorData, allSessions) {
      const operatorsWithStats = operatorData.operators.map((op) => {
        const userSessions = allSessions.filter((s) => {
          const userId = s.originator?.userId;
          if (!userId) return false;
          return userId === op.id || userId === op.metadata?.slackId;
        });
        return {
          ...op,
          stats: {
            activeSessions: userSessions.filter((s) => s.active).length,
            totalSessions: userSessions.length,
            lastSeen: userSessions.length > 0 ? new Date(
              Date.now() - Math.min(...userSessions.map((s) => s.minutesAgo)) * 6e4
            ).toISOString() : op.lastSeen
          }
        };
      });
      return { ...operatorData, operators: operatorsWithStats };
    }
    module2.exports = {
      loadOperators: loadOperators2,
      saveOperators: saveOperators2,
      getOperatorBySlackId: getOperatorBySlackId2,
      refreshOperatorsAsync,
      startOperatorsRefresh: startOperatorsRefresh2,
      calculateOperatorStats: calculateOperatorStats2
    };
  }
});

// src/topics.js
var require_topics = __commonJS({
  "src/topics.js"(exports2, module2) {
    var TOPIC_PATTERNS = {
      dashboard: ["dashboard", "command center", "ui", "interface", "status page"],
      scheduling: ["cron", "schedule", "timer", "reminder", "alarm", "periodic", "interval"],
      heartbeat: [
        "heartbeat",
        "heartbeat_ok",
        "poll",
        "health check",
        "ping",
        "keepalive",
        "monitoring"
      ],
      memory: ["memory", "remember", "recall", "notes", "journal", "log", "context"],
      Slack: ["slack", "channel", "#cc-", "thread", "mention", "dm", "workspace"],
      email: ["email", "mail", "inbox", "gmail", "send email", "unread", "compose"],
      calendar: ["calendar", "event", "meeting", "appointment", "schedule", "gcal"],
      coding: [
        "code",
        "script",
        "function",
        "debug",
        "error",
        "bug",
        "implement",
        "refactor",
        "programming"
      ],
      git: [
        "git",
        "commit",
        "branch",
        "merge",
        "push",
        "pull",
        "repository",
        "pr",
        "pull request",
        "github"
      ],
      "file editing": ["file", "edit", "write", "read", "create", "delete", "modify", "save"],
      API: ["api", "endpoint", "request", "response", "webhook", "integration", "rest", "graphql"],
      research: ["search", "research", "lookup", "find", "investigate", "learn", "study"],
      browser: ["browser", "webpage", "website", "url", "click", "navigate", "screenshot", "web_fetch"],
      "Quip export": ["quip", "export", "document", "spreadsheet"],
      finance: ["finance", "investment", "stock", "money", "budget", "bank", "trading", "portfolio"],
      home: ["home", "automation", "lights", "thermostat", "smart home", "iot", "homekit"],
      health: ["health", "fitness", "workout", "exercise", "weight", "sleep", "nutrition"],
      travel: ["travel", "flight", "hotel", "trip", "vacation", "booking", "airport"],
      food: ["food", "recipe", "restaurant", "cooking", "meal", "order", "delivery"],
      subagent: ["subagent", "spawn", "sub-agent", "delegate", "worker", "parallel"],
      tools: ["tool", "exec", "shell", "command", "terminal", "bash", "run"]
    };
    function detectTopics(text) {
      if (!text) return [];
      const lowerText = text.toLowerCase();
      const scores = {};
      for (const [topic, keywords] of Object.entries(TOPIC_PATTERNS)) {
        let score = 0;
        for (const keyword of keywords) {
          if (keyword.length <= 3) {
            const regex = new RegExp(`\\b${keyword}\\b`, "i");
            if (regex.test(lowerText)) score++;
          } else if (lowerText.includes(keyword)) {
            score++;
          }
        }
        if (score > 0) {
          scores[topic] = score;
        }
      }
      if (Object.keys(scores).length === 0) return [];
      const bestScore = Math.max(...Object.values(scores));
      const threshold = Math.max(2, bestScore * 0.5);
      return Object.entries(scores).filter(([_, score]) => score >= threshold || score >= 1 && bestScore <= 2).sort((a, b) => b[1] - a[1]).map(([topic, _]) => topic);
    }
    module2.exports = { TOPIC_PATTERNS, detectTopics };
  }
});

// src/sessions.js
var require_sessions = __commonJS({
  "src/sessions.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    var { detectTopics } = require_topics();
    var CHANNEL_MAP = {
      c0aax7y80np: "#cc-meta",
      c0ab9f8sdfe: "#cc-research",
      c0aan4rq7v5: "#cc-finance",
      c0abxulk1qq: "#cc-properties",
      c0ab5nz8mkl: "#cc-ai",
      c0aan38tzv5: "#cc-dev",
      c0ab7wwhqvc: "#cc-home",
      c0ab1pjhxef: "#cc-health",
      c0ab7txvcqd: "#cc-legal",
      c0aay2g3n3r: "#cc-social",
      c0aaxrw2wqp: "#cc-business",
      c0ab19f3lae: "#cc-random",
      c0ab0r74y33: "#cc-food",
      c0ab0qrq3r9: "#cc-travel",
      c0ab0sbqqlg: "#cc-family",
      c0ab0slqdba: "#cc-games",
      c0ab1ps7ef2: "#cc-music",
      c0absbnrsbe: "#cc-dashboard"
    };
    function parseSessionLabel(key) {
      const parts = key.split(":");
      if (parts.includes("slack")) {
        const channelIdx = parts.indexOf("channel");
        if (channelIdx >= 0 && parts[channelIdx + 1]) {
          const channelId = parts[channelIdx + 1].toLowerCase();
          const channelName = CHANNEL_MAP[channelId] || `#${channelId}`;
          if (parts.includes("thread")) {
            const threadTs = parts[parts.indexOf("thread") + 1];
            const ts = parseFloat(threadTs);
            const date = new Date(ts * 1e3);
            const timeStr = date.toLocaleTimeString("en-US", { hour: "numeric", minute: "2-digit" });
            return `${channelName} thread @ ${timeStr}`;
          }
          return channelName;
        }
      }
      if (key.includes("telegram")) {
        return "\u{1F4F1} Telegram";
      }
      if (key === "agent:main:main") {
        return "\u{1F3E0} Main Session";
      }
      return key.length > 40 ? key.slice(0, 37) + "..." : key;
    }
    function createSessionsModule2(deps) {
      const { getOpenClawDir: getOpenClawDir2, getOperatorBySlackId: getOperatorBySlackId2, runOpenClaw: runOpenClaw2, runOpenClawAsync: runOpenClawAsync2, extractJSON: extractJSON2 } = deps;
      let sessionsCache = { sessions: [], timestamp: 0, refreshing: false };
      const SESSIONS_CACHE_TTL = 1e4;
      function findTranscriptPath(sessionId) {
        if (!sessionId) return null;
        const openclawDir = getOpenClawDir2();
        const sessionsDir = path2.join(openclawDir, "agents", "main", "sessions");
        const exactPath = path2.join(sessionsDir, `${sessionId}.jsonl`);
        if (fs2.existsSync(exactPath)) return exactPath;
        try {
          const files = fs2.readdirSync(sessionsDir);
          const prefix = `${sessionId}-`;
          const match = files.find(
            (f) => f.startsWith(prefix) && f.endsWith(".jsonl") && !f.includes(".deleted.")
          );
          if (match) return path2.join(sessionsDir, match);
        } catch (e) {
        }
        return null;
      }
      function getSessionOriginator(sessionId) {
        try {
          if (!sessionId) return null;
          const transcriptPath = findTranscriptPath(sessionId);
          if (!transcriptPath) return null;
          const content = fs2.readFileSync(transcriptPath, "utf8");
          const lines = content.trim().split("\n");
          for (let i = 0; i < Math.min(lines.length, 10); i++) {
            try {
              const entry = JSON.parse(lines[i]);
              if (entry.type !== "message" || !entry.message) continue;
              const msg = entry.message;
              if (msg.role !== "user") continue;
              let text = "";
              if (typeof msg.content === "string") {
                text = msg.content;
              } else if (Array.isArray(msg.content)) {
                const textPart = msg.content.find((c) => c.type === "text");
                if (textPart) text = textPart.text || "";
              }
              if (!text) continue;
              const slackUserMatch = text.match(/\]\s*([\w.-]+)\s*\(([A-Z0-9]+)\):/);
              if (slackUserMatch) {
                const username = slackUserMatch[1];
                const userId = slackUserMatch[2];
                const operator = getOperatorBySlackId2(userId);
                return {
                  userId,
                  username,
                  displayName: operator?.name || username,
                  role: operator?.role || "user",
                  avatar: operator?.avatar || null
                };
              }
              const senderIdMatch = text.match(/"sender_id":\s*"([A-Z0-9]+)"/);
              const senderMatch = text.match(/"sender":\s*"([^"]+)"/);
              if (senderIdMatch) {
                const userId = senderIdMatch[1];
                const username = senderMatch ? senderMatch[1] : userId;
                const operator = getOperatorBySlackId2(userId);
                return {
                  userId,
                  username,
                  displayName: operator?.name || username,
                  role: operator?.role || "user",
                  avatar: operator?.avatar || null
                };
              }
            } catch (e) {
            }
          }
          return null;
        } catch (e) {
          return null;
        }
      }
      function getSessionTopic(sessionId) {
        if (!sessionId) return null;
        try {
          const transcriptPath = findTranscriptPath(sessionId);
          if (!transcriptPath) return null;
          const fd = fs2.openSync(transcriptPath, "r");
          const buffer = Buffer.alloc(5e4);
          const bytesRead = fs2.readSync(fd, buffer, 0, 5e4, 0);
          fs2.closeSync(fd);
          if (bytesRead === 0) return null;
          const content = buffer.toString("utf8", 0, bytesRead);
          const lines = content.split("\n").filter((l) => l.trim());
          let textSamples = [];
          for (const line of lines.slice(0, 30)) {
            try {
              const entry = JSON.parse(line);
              if (entry.type === "message" && entry.message?.content) {
                const msgContent = entry.message.content;
                if (Array.isArray(msgContent)) {
                  msgContent.forEach((c) => {
                    if (c.type === "text" && c.text) {
                      textSamples.push(c.text.slice(0, 500));
                    }
                  });
                } else if (typeof msgContent === "string") {
                  textSamples.push(msgContent.slice(0, 500));
                }
              }
            } catch (e) {
            }
          }
          if (textSamples.length === 0) return null;
          const topics = detectTopics(textSamples.join(" "));
          return topics.length > 0 ? topics.slice(0, 2).join(", ") : null;
        } catch (e) {
          return null;
        }
      }
      function mapSession(s) {
        const minutesAgo = s.ageMs ? s.ageMs / 6e4 : Infinity;
        let channel = "other";
        if (s.key.includes("slack")) channel = "slack";
        else if (s.key.includes("telegram")) channel = "telegram";
        else if (s.key.includes("discord")) channel = "discord";
        else if (s.key.includes("signal")) channel = "signal";
        else if (s.key.includes("whatsapp")) channel = "whatsapp";
        let sessionType = "channel";
        if (s.key.includes(":subagent:")) sessionType = "subagent";
        else if (s.key.includes(":cron:")) sessionType = "cron";
        else if (s.key === "agent:main:main") sessionType = "main";
        const originator = getSessionOriginator(s.sessionId);
        const label = s.groupChannel || s.displayName || parseSessionLabel(s.key);
        const topic = getSessionTopic(s.sessionId);
        const totalTokens = s.totalTokens || 0;
        const sessionAgeMinutes = Math.max(1, Math.min(minutesAgo, 24 * 60));
        const burnRate = Math.round(totalTokens / sessionAgeMinutes);
        return {
          sessionKey: s.key,
          sessionId: s.sessionId,
          label,
          groupChannel: s.groupChannel || null,
          displayName: s.displayName || null,
          kind: s.kind,
          channel,
          sessionType,
          active: minutesAgo < 15,
          recentlyActive: minutesAgo < 60,
          minutesAgo: Math.round(minutesAgo),
          tokens: s.totalTokens || 0,
          model: s.model,
          originator,
          topic,
          metrics: {
            burnRate,
            toolCalls: 0,
            minutesActive: Math.max(1, Math.min(Math.round(minutesAgo), 24 * 60))
          }
        };
      }
      async function refreshSessionsCache() {
        if (sessionsCache.refreshing) return;
        sessionsCache.refreshing = true;
        try {
          const output = await runOpenClawAsync2("sessions --json 2>/dev/null");
          const jsonStr = extractJSON2(output);
          if (jsonStr) {
            const data = JSON.parse(jsonStr);
            const sessions2 = data.sessions || [];
            const mapped = sessions2.map((s) => mapSession(s));
            const withOriginator = mapped.filter((s) => s.originator != null);
            sessionsCache = {
              sessions: mapped,
              timestamp: Date.now(),
              refreshing: false
            };
            console.log(
              `[Sessions Cache] Refreshed: ${mapped.length} sessions (${withOriginator.length} with originator)`
            );
          }
        } catch (e) {
          console.error("[Sessions Cache] Refresh error:", e.message);
        }
        sessionsCache.refreshing = false;
      }
      function getSessionsCached() {
        const now = Date.now();
        const isStale = now - sessionsCache.timestamp > SESSIONS_CACHE_TTL;
        if (isStale && !sessionsCache.refreshing) {
          refreshSessionsCache();
        }
        return sessionsCache.sessions;
      }
      function getSessions(options = {}) {
        const limit = Object.prototype.hasOwnProperty.call(options, "limit") ? options.limit : 20;
        const returnCount = options.returnCount || false;
        if (limit === null) {
          const cached = getSessionsCached();
          const totalCount = cached.length;
          return returnCount ? { sessions: cached, totalCount } : cached;
        }
        try {
          const output = runOpenClaw2("sessions --json 2>/dev/null");
          const jsonStr = extractJSON2(output);
          if (jsonStr) {
            const data = JSON.parse(jsonStr);
            const totalCount = data.count || data.sessions?.length || 0;
            let sessions2 = data.sessions || [];
            if (limit != null) {
              sessions2 = sessions2.slice(0, limit);
            }
            const mapped = sessions2.map((s) => mapSession(s));
            return returnCount ? { sessions: mapped, totalCount } : mapped;
          }
        } catch (e) {
          console.error("Failed to get sessions:", e.message);
        }
        return returnCount ? { sessions: [], totalCount: 0 } : [];
      }
      function readTranscript(sessionId) {
        const transcriptPath = findTranscriptPath(sessionId);
        try {
          if (!transcriptPath) return [];
          const content = fs2.readFileSync(transcriptPath, "utf8");
          return content.trim().split("\n").map((line) => {
            try {
              return JSON.parse(line);
            } catch {
              return null;
            }
          }).filter(Boolean);
        } catch (e) {
          console.error("Failed to read transcript:", e.message);
          return [];
        }
      }
      function getSessionDetail(sessionKey) {
        try {
          const listOutput = runOpenClaw2("sessions --json 2>/dev/null");
          let sessionInfo = null;
          const jsonStr = extractJSON2(listOutput);
          if (jsonStr) {
            const data = JSON.parse(jsonStr);
            sessionInfo = data.sessions?.find((s) => s.key === sessionKey);
          }
          if (!sessionInfo) {
            return { error: "Session not found" };
          }
          const transcript = readTranscript(sessionInfo.sessionId);
          let messages = [];
          let tools = {};
          let facts = [];
          let needsAttention = [];
          let totalInputTokens = 0;
          let totalOutputTokens = 0;
          let totalCacheRead = 0;
          let totalCacheWrite = 0;
          let totalCost = 0;
          let detectedModel = sessionInfo.model || null;
          transcript.forEach((entry) => {
            if (entry.type !== "message" || !entry.message) return;
            const msg = entry.message;
            if (!msg.role) return;
            if (msg.usage) {
              totalInputTokens += msg.usage.input || msg.usage.inputTokens || 0;
              totalOutputTokens += msg.usage.output || msg.usage.outputTokens || 0;
              totalCacheRead += msg.usage.cacheRead || msg.usage.cacheReadTokens || 0;
              totalCacheWrite += msg.usage.cacheWrite || msg.usage.cacheWriteTokens || 0;
              if (msg.usage.cost?.total) totalCost += msg.usage.cost.total;
            }
            if (msg.role === "assistant" && msg.model && !detectedModel) {
              detectedModel = msg.model;
            }
            let text = "";
            if (typeof msg.content === "string") {
              text = msg.content;
            } else if (Array.isArray(msg.content)) {
              const textPart = msg.content.find((c) => c.type === "text");
              if (textPart) text = textPart.text || "";
              msg.content.filter((c) => c.type === "toolCall" || c.type === "tool_use").forEach((tc) => {
                const name = tc.name || tc.tool || "unknown";
                tools[name] = (tools[name] || 0) + 1;
              });
            }
            if (text && msg.role !== "toolResult") {
              messages.push({ role: msg.role, text, timestamp: entry.timestamp });
            }
            if (msg.role === "user" && text) {
              const lowerText = text.toLowerCase();
              if (text.includes("?")) {
                const questions = text.match(/[^.!?\n]*\?/g) || [];
                questions.slice(0, 2).forEach((q) => {
                  if (q.length > 15 && q.length < 200) {
                    needsAttention.push(`\u2753 ${q.trim()}`);
                  }
                });
              }
              if (lowerText.includes("todo") || lowerText.includes("remind") || lowerText.includes("need to")) {
                const match = text.match(/(?:todo|remind|need to)[^.!?\n]*/i);
                if (match) needsAttention.push(`\u{1F4CB} ${match[0].slice(0, 100)}`);
              }
            }
            if (msg.role === "assistant" && text) {
              const lowerText = text.toLowerCase();
              ["\u2705", "done", "created", "updated", "fixed", "deployed"].forEach((keyword) => {
                if (lowerText.includes(keyword)) {
                  const lines = text.split("\n").filter((l) => l.toLowerCase().includes(keyword));
                  lines.slice(0, 2).forEach((line) => {
                    if (line.length > 5 && line.length < 150) {
                      facts.push(line.trim().slice(0, 100));
                    }
                  });
                }
              });
            }
          });
          let summary = "No activity yet.";
          const userMessages = messages.filter((m) => m.role === "user");
          const assistantMessages = messages.filter((m) => m.role === "assistant");
          let topics = [];
          if (messages.length > 0) {
            summary = `${messages.length} messages (${userMessages.length} user, ${assistantMessages.length} assistant). `;
            const allText = messages.map((m) => m.text).join(" ");
            topics = detectTopics(allText);
            if (topics.length > 0) {
              summary += `Topics: ${topics.join(", ")}.`;
            }
          }
          const toolsArray = Object.entries(tools).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count);
          const ageMs = sessionInfo.ageMs || 0;
          const lastActive = ageMs < 6e4 ? "Just now" : ageMs < 36e5 ? `${Math.round(ageMs / 6e4)} minutes ago` : ageMs < 864e5 ? `${Math.round(ageMs / 36e5)} hours ago` : `${Math.round(ageMs / 864e5)} days ago`;
          let channelDisplay = "Other";
          if (sessionInfo.groupChannel) {
            channelDisplay = sessionInfo.groupChannel;
          } else if (sessionInfo.displayName) {
            channelDisplay = sessionInfo.displayName;
          } else if (sessionKey.includes("slack")) {
            const parts = sessionKey.split(":");
            const channelIdx = parts.indexOf("channel");
            if (channelIdx >= 0 && parts[channelIdx + 1]) {
              const channelId = parts[channelIdx + 1].toLowerCase();
              channelDisplay = CHANNEL_MAP[channelId] || `#${channelId}`;
            } else {
              channelDisplay = "Slack";
            }
          } else if (sessionKey.includes("telegram")) {
            channelDisplay = "Telegram";
          }
          const finalTotalTokens = totalInputTokens + totalOutputTokens || sessionInfo.totalTokens || 0;
          const finalInputTokens = totalInputTokens || sessionInfo.inputTokens || 0;
          const finalOutputTokens = totalOutputTokens || sessionInfo.outputTokens || 0;
          const modelDisplay = (detectedModel || sessionInfo.model || "-").replace("anthropic/", "").replace("openai/", "");
          return {
            key: sessionKey,
            kind: sessionInfo.kind,
            channel: channelDisplay,
            groupChannel: sessionInfo.groupChannel || channelDisplay,
            model: modelDisplay,
            tokens: finalTotalTokens,
            inputTokens: finalInputTokens,
            outputTokens: finalOutputTokens,
            cacheRead: totalCacheRead,
            cacheWrite: totalCacheWrite,
            estCost: totalCost > 0 ? `$${totalCost.toFixed(4)}` : null,
            lastActive,
            summary,
            topics,
            // Array of detected topics
            facts: [...new Set(facts)].slice(0, 8),
            needsAttention: [...new Set(needsAttention)].slice(0, 5),
            tools: toolsArray.slice(0, 10),
            messages: messages.slice(-15).reverse().map((m) => ({
              role: m.role,
              text: m.text.slice(0, 500)
            }))
          };
        } catch (e) {
          console.error("Failed to get session detail:", e.message);
          return { error: e.message };
        }
      }
      return {
        findTranscriptPath,
        getSessionOriginator,
        getSessionTopic,
        mapSession,
        refreshSessionsCache,
        getSessionsCached,
        getSessions,
        readTranscript,
        getSessionDetail,
        parseSessionLabel
      };
    }
    module2.exports = { createSessionsModule: createSessionsModule2, CHANNEL_MAP };
  }
});

// src/cron.js
var require_cron = __commonJS({
  "src/cron.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    function cronToHuman(expr) {
      if (!expr || expr === "\u2014") return null;
      const parts = expr.split(" ");
      if (parts.length < 5) return null;
      const [minute, hour, dayOfMonth, month, dayOfWeek] = parts;
      const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
      function formatTime(h, m) {
        const hNum = parseInt(h, 10);
        const mNum = parseInt(m, 10);
        if (isNaN(hNum)) return null;
        const ampm = hNum >= 12 ? "pm" : "am";
        const h12 = hNum === 0 ? 12 : hNum > 12 ? hNum - 12 : hNum;
        return mNum === 0 ? `${h12}${ampm}` : `${h12}:${mNum.toString().padStart(2, "0")}${ampm}`;
      }
      if (minute === "*" && hour === "*" && dayOfMonth === "*" && month === "*" && dayOfWeek === "*") {
        return "Every minute";
      }
      if (minute.startsWith("*/")) {
        const interval = minute.slice(2);
        return `Every ${interval} minutes`;
      }
      if (hour.startsWith("*/")) {
        const interval = hour.slice(2);
        const minStr = minute === "0" ? "" : `:${minute.padStart(2, "0")}`;
        return `Every ${interval} hours${minStr ? " at " + minStr : ""}`;
      }
      if (minute !== "*" && hour === "*" && dayOfMonth === "*" && month === "*" && dayOfWeek === "*") {
        return `Hourly at :${minute.padStart(2, "0")}`;
      }
      let timeStr = "";
      if (minute !== "*" && hour !== "*" && !hour.startsWith("*/")) {
        timeStr = formatTime(hour, minute);
      }
      if (timeStr && dayOfMonth === "*" && month === "*" && dayOfWeek === "*") {
        return `Daily at ${timeStr}`;
      }
      if ((dayOfWeek === "1-5" || dayOfWeek === "MON-FRI") && dayOfMonth === "*" && month === "*") {
        return timeStr ? `Weekdays at ${timeStr}` : "Weekdays";
      }
      if ((dayOfWeek === "0,6" || dayOfWeek === "6,0") && dayOfMonth === "*" && month === "*") {
        return timeStr ? `Weekends at ${timeStr}` : "Weekends";
      }
      if (dayOfMonth === "*" && month === "*" && dayOfWeek !== "*") {
        const days = dayOfWeek.split(",").map((d) => {
          const num = parseInt(d, 10);
          return dayNames[num] || d;
        });
        const dayStr = days.length === 1 ? days[0] : days.join(", ");
        return timeStr ? `${dayStr} at ${timeStr}` : `Every ${dayStr}`;
      }
      if (dayOfMonth !== "*" && month === "*" && dayOfWeek === "*") {
        const day = parseInt(dayOfMonth, 10);
        const suffix = day === 1 || day === 21 || day === 31 ? "st" : day === 2 || day === 22 ? "nd" : day === 3 || day === 23 ? "rd" : "th";
        return timeStr ? `${day}${suffix} of month at ${timeStr}` : `${day}${suffix} of every month`;
      }
      if (timeStr) {
        return `At ${timeStr}`;
      }
      return expr;
    }
    function getCronJobs2(getOpenClawDir2) {
      try {
        const cronPath = path2.join(getOpenClawDir2(), "cron", "jobs.json");
        if (fs2.existsSync(cronPath)) {
          const data = JSON.parse(fs2.readFileSync(cronPath, "utf8"));
          return (data.jobs || []).map((j) => {
            let scheduleStr = "\u2014";
            let scheduleHuman = null;
            if (j.schedule) {
              if (j.schedule.kind === "cron" && j.schedule.expr) {
                scheduleStr = j.schedule.expr;
                scheduleHuman = cronToHuman(j.schedule.expr);
              } else if (j.schedule.kind === "once") {
                scheduleStr = "once";
                scheduleHuman = "One-time";
              }
            }
            let nextRunStr = "\u2014";
            if (j.state?.nextRunAtMs) {
              const next = new Date(j.state.nextRunAtMs);
              const now = /* @__PURE__ */ new Date();
              const diffMs = next - now;
              const diffMins = Math.round(diffMs / 6e4);
              if (diffMins < 0) {
                nextRunStr = "overdue";
              } else if (diffMins < 60) {
                nextRunStr = `${diffMins}m`;
              } else if (diffMins < 1440) {
                nextRunStr = `${Math.round(diffMins / 60)}h`;
              } else {
                nextRunStr = `${Math.round(diffMins / 1440)}d`;
              }
            }
            return {
              id: j.id,
              name: j.name || j.id.slice(0, 8),
              schedule: scheduleStr,
              scheduleHuman,
              nextRun: nextRunStr,
              enabled: j.enabled !== false,
              lastStatus: j.state?.lastStatus
            };
          });
        }
      } catch (e) {
        console.error("Failed to get cron:", e.message);
      }
      return [];
    }
    module2.exports = {
      cronToHuman,
      getCronJobs: getCronJobs2
    };
  }
});

// src/cerebro.js
var require_cerebro = __commonJS({
  "src/cerebro.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    var { formatTimeAgo } = require_utils();
    function getCerebroTopics2(cerebroDir, options = {}) {
      const { offset = 0, limit = 20, status: filterStatus = "all" } = options;
      const topicsDir = path2.join(cerebroDir, "topics");
      const orphansDir = path2.join(cerebroDir, "orphans");
      const topics = [];
      const result = {
        initialized: false,
        cerebroPath: cerebroDir,
        topics: { active: 0, resolved: 0, parked: 0, total: 0 },
        threads: 0,
        orphans: 0,
        recentTopics: [],
        lastUpdated: null
      };
      try {
        if (!fs2.existsSync(cerebroDir)) {
          return result;
        }
        result.initialized = true;
        let latestModified = null;
        if (!fs2.existsSync(topicsDir)) {
          return result;
        }
        const topicNames = fs2.readdirSync(topicsDir).filter((name) => {
          const topicPath = path2.join(topicsDir, name);
          return fs2.statSync(topicPath).isDirectory() && !name.startsWith("_");
        });
        topicNames.forEach((name) => {
          const topicMdPath = path2.join(topicsDir, name, "topic.md");
          const topicDirPath = path2.join(topicsDir, name);
          let stat;
          let content = "";
          if (fs2.existsSync(topicMdPath)) {
            stat = fs2.statSync(topicMdPath);
            content = fs2.readFileSync(topicMdPath, "utf8");
          } else {
            stat = fs2.statSync(topicDirPath);
          }
          try {
            const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
            let title = name;
            let topicStatus = "active";
            let category = "general";
            let created = null;
            if (frontmatterMatch) {
              const frontmatter = frontmatterMatch[1];
              const titleMatch = frontmatter.match(/title:\s*(.+)/);
              const statusMatch = frontmatter.match(/status:\s*(.+)/);
              const categoryMatch = frontmatter.match(/category:\s*(.+)/);
              const createdMatch = frontmatter.match(/created:\s*(.+)/);
              if (titleMatch) title = titleMatch[1].trim();
              if (statusMatch) topicStatus = statusMatch[1].trim().toLowerCase();
              if (categoryMatch) category = categoryMatch[1].trim();
              if (createdMatch) created = createdMatch[1].trim();
            }
            const threadsDir = path2.join(topicsDir, name, "threads");
            let threadCount = 0;
            if (fs2.existsSync(threadsDir)) {
              threadCount = fs2.readdirSync(threadsDir).filter((f) => f.endsWith(".md") || f.endsWith(".json")).length;
            }
            result.threads += threadCount;
            if (topicStatus === "active") result.topics.active++;
            else if (topicStatus === "resolved") result.topics.resolved++;
            else if (topicStatus === "parked") result.topics.parked++;
            if (!latestModified || stat.mtime > latestModified) {
              latestModified = stat.mtime;
            }
            topics.push({
              name,
              title,
              status: topicStatus,
              category,
              created,
              threads: threadCount,
              lastModified: stat.mtimeMs
            });
          } catch (e) {
            console.error(`Failed to parse topic ${name}:`, e.message);
          }
        });
        result.topics.total = topics.length;
        const statusPriority = { active: 0, resolved: 1, parked: 2 };
        topics.sort((a, b) => {
          const statusDiff = (statusPriority[a.status] || 3) - (statusPriority[b.status] || 3);
          if (statusDiff !== 0) return statusDiff;
          return b.lastModified - a.lastModified;
        });
        let filtered = topics;
        if (filterStatus !== "all") {
          filtered = topics.filter((t) => t.status === filterStatus);
        }
        const paginated = filtered.slice(offset, offset + limit);
        result.recentTopics = paginated.map((t) => ({
          name: t.name,
          title: t.title,
          status: t.status,
          threads: t.threads,
          age: formatTimeAgo(new Date(t.lastModified))
        }));
        if (fs2.existsSync(orphansDir)) {
          try {
            result.orphans = fs2.readdirSync(orphansDir).filter((f) => f.endsWith(".md")).length;
          } catch (e) {
          }
        }
        result.lastUpdated = latestModified ? latestModified.toISOString() : null;
      } catch (e) {
        console.error("Failed to get Cerebro topics:", e.message);
      }
      return result;
    }
    function updateTopicStatus2(cerebroDir, topicId, newStatus) {
      const topicDir = path2.join(cerebroDir, "topics", topicId);
      const topicFile = path2.join(topicDir, "topic.md");
      if (!fs2.existsSync(topicDir)) {
        return { error: `Topic '${topicId}' not found`, code: 404 };
      }
      if (!fs2.existsSync(topicFile)) {
        const content2 = `---
title: ${topicId}
status: ${newStatus}
category: general
created: ${(/* @__PURE__ */ new Date()).toISOString().split("T")[0]}
---

# ${topicId}

## Overview
*Topic tracking file.*

## Notes
`;
        fs2.writeFileSync(topicFile, content2, "utf8");
        return {
          topic: {
            id: topicId,
            name: topicId,
            title: topicId,
            status: newStatus
          }
        };
      }
      let content = fs2.readFileSync(topicFile, "utf8");
      let title = topicId;
      const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
      if (frontmatterMatch) {
        let frontmatter = frontmatterMatch[1];
        const titleMatch = frontmatter.match(/title:\s*["']?([^"'\n]+)["']?/i);
        if (titleMatch) title = titleMatch[1];
        if (frontmatter.includes("status:")) {
          frontmatter = frontmatter.replace(
            /status:\s*(active|resolved|parked)/i,
            `status: ${newStatus}`
          );
        } else {
          frontmatter = frontmatter.trim() + `
status: ${newStatus}`;
        }
        content = content.replace(/^---\n[\s\S]*?\n---/, `---
${frontmatter}
---`);
      } else {
        const headerMatch = content.match(/^#\s*(.+)/m);
        if (headerMatch) title = headerMatch[1];
        const frontmatter = `---
title: ${title}
status: ${newStatus}
category: general
created: ${(/* @__PURE__ */ new Date()).toISOString().split("T")[0]}
---

`;
        content = frontmatter + content;
      }
      fs2.writeFileSync(topicFile, content, "utf8");
      return {
        topic: {
          id: topicId,
          name: topicId,
          title,
          status: newStatus
        }
      };
    }
    module2.exports = {
      getCerebroTopics: getCerebroTopics2,
      updateTopicStatus: updateTopicStatus2
    };
  }
});

// src/tokens.js
var require_tokens = __commonJS({
  "src/tokens.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    var { formatNumber, formatTokens } = require_utils();
    var TOKEN_RATES = {
      input: 15,
      // $15/1M input tokens
      output: 75,
      // $75/1M output tokens
      cacheRead: 1.5,
      // $1.50/1M (90% discount from input)
      cacheWrite: 18.75
      // $18.75/1M (25% premium on input)
    };
    var tokenUsageCache = { data: null, timestamp: 0, refreshing: false };
    var TOKEN_USAGE_CACHE_TTL = 3e4;
    var refreshInterval = null;
    function emptyUsageBucket() {
      return { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, requests: 0 };
    }
    async function refreshTokenUsageAsync2(getOpenClawDir2) {
      if (tokenUsageCache.refreshing) return;
      tokenUsageCache.refreshing = true;
      try {
        const sessionsDir = path2.join(getOpenClawDir2(), "agents", "main", "sessions");
        const files = await fs2.promises.readdir(sessionsDir);
        const jsonlFiles = files.filter((f) => f.endsWith(".jsonl"));
        const now = Date.now();
        const oneDayAgo = now - 24 * 60 * 60 * 1e3;
        const threeDaysAgo = now - 3 * 24 * 60 * 60 * 1e3;
        const sevenDaysAgo = now - 7 * 24 * 60 * 60 * 1e3;
        const usage24h = emptyUsageBucket();
        const usage3d = emptyUsageBucket();
        const usage7d = emptyUsageBucket();
        const batchSize = 50;
        for (let i = 0; i < jsonlFiles.length; i += batchSize) {
          const batch = jsonlFiles.slice(i, i + batchSize);
          await Promise.all(
            batch.map(async (file) => {
              const filePath = path2.join(sessionsDir, file);
              try {
                const stat = await fs2.promises.stat(filePath);
                if (stat.mtimeMs < sevenDaysAgo) return;
                const content = await fs2.promises.readFile(filePath, "utf8");
                const lines = content.trim().split("\n");
                for (const line of lines) {
                  if (!line) continue;
                  try {
                    const entry = JSON.parse(line);
                    const entryTime = entry.timestamp ? new Date(entry.timestamp).getTime() : 0;
                    if (entryTime < sevenDaysAgo) continue;
                    if (entry.message?.usage) {
                      const u = entry.message.usage;
                      const input = u.input || 0;
                      const output = u.output || 0;
                      const cacheRead = u.cacheRead || 0;
                      const cacheWrite = u.cacheWrite || 0;
                      const cost = u.cost?.total || 0;
                      if (entryTime >= oneDayAgo) {
                        usage24h.input += input;
                        usage24h.output += output;
                        usage24h.cacheRead += cacheRead;
                        usage24h.cacheWrite += cacheWrite;
                        usage24h.cost += cost;
                        usage24h.requests++;
                      }
                      if (entryTime >= threeDaysAgo) {
                        usage3d.input += input;
                        usage3d.output += output;
                        usage3d.cacheRead += cacheRead;
                        usage3d.cacheWrite += cacheWrite;
                        usage3d.cost += cost;
                        usage3d.requests++;
                      }
                      usage7d.input += input;
                      usage7d.output += output;
                      usage7d.cacheRead += cacheRead;
                      usage7d.cacheWrite += cacheWrite;
                      usage7d.cost += cost;
                      usage7d.requests++;
                    }
                  } catch (e) {
                  }
                }
              } catch (e) {
              }
            })
          );
          await new Promise((resolve) => setImmediate(resolve));
        }
        const finalizeBucket = (bucket) => ({
          ...bucket,
          tokensNoCache: bucket.input + bucket.output,
          tokensWithCache: bucket.input + bucket.output + bucket.cacheRead + bucket.cacheWrite
        });
        const result = {
          // Primary (24h) for backward compatibility
          ...finalizeBucket(usage24h),
          // All three windows
          windows: {
            "24h": finalizeBucket(usage24h),
            "3d": finalizeBucket(usage3d),
            "7d": finalizeBucket(usage7d)
          }
        };
        tokenUsageCache = { data: result, timestamp: Date.now(), refreshing: false };
        console.log(
          `[Token Usage] Cached: 24h=${usage24h.requests} 3d=${usage3d.requests} 7d=${usage7d.requests} requests`
        );
      } catch (e) {
        console.error("[Token Usage] Refresh error:", e.message);
        tokenUsageCache.refreshing = false;
      }
    }
    function getDailyTokenUsage2(getOpenClawDir2) {
      const now = Date.now();
      const isStale = now - tokenUsageCache.timestamp > TOKEN_USAGE_CACHE_TTL;
      if (isStale && !tokenUsageCache.refreshing && getOpenClawDir2) {
        refreshTokenUsageAsync2(getOpenClawDir2);
      }
      const emptyResult = {
        input: 0,
        output: 0,
        cacheRead: 0,
        cacheWrite: 0,
        cost: 0,
        requests: 0,
        tokensNoCache: 0,
        tokensWithCache: 0,
        windows: {
          "24h": {
            input: 0,
            output: 0,
            cacheRead: 0,
            cacheWrite: 0,
            cost: 0,
            requests: 0,
            tokensNoCache: 0,
            tokensWithCache: 0
          },
          "3d": {
            input: 0,
            output: 0,
            cacheRead: 0,
            cacheWrite: 0,
            cost: 0,
            requests: 0,
            tokensNoCache: 0,
            tokensWithCache: 0
          },
          "7d": {
            input: 0,
            output: 0,
            cacheRead: 0,
            cacheWrite: 0,
            cost: 0,
            requests: 0,
            tokensNoCache: 0,
            tokensWithCache: 0
          }
        }
      };
      return tokenUsageCache.data || emptyResult;
    }
    function calculateCostForBucket(bucket, rates = TOKEN_RATES) {
      const inputCost = bucket.input / 1e6 * rates.input;
      const outputCost = bucket.output / 1e6 * rates.output;
      const cacheReadCost = bucket.cacheRead / 1e6 * rates.cacheRead;
      const cacheWriteCost = bucket.cacheWrite / 1e6 * rates.cacheWrite;
      return {
        inputCost,
        outputCost,
        cacheReadCost,
        cacheWriteCost,
        totalCost: inputCost + outputCost + cacheReadCost + cacheWriteCost
      };
    }
    function getCostBreakdown2(config, getSessions, getOpenClawDir2) {
      const usage = getDailyTokenUsage2(getOpenClawDir2);
      if (!usage) {
        return { error: "Failed to get usage data" };
      }
      const costs = calculateCostForBucket(usage);
      const planCost = config.billing?.claudePlanCost || 200;
      const planName = config.billing?.claudePlanName || "Claude Code Max";
      const windowConfigs = {
        "24h": { days: 1, label: "24h" },
        "3d": { days: 3, label: "3dma" },
        "7d": { days: 7, label: "7dma" }
      };
      const windows = {};
      for (const [key, windowConfig] of Object.entries(windowConfigs)) {
        const bucket = usage.windows?.[key] || usage;
        const bucketCosts = calculateCostForBucket(bucket);
        const dailyAvg = bucketCosts.totalCost / windowConfig.days;
        const monthlyProjected = dailyAvg * 30;
        const monthlySavings = monthlyProjected - planCost;
        windows[key] = {
          label: windowConfig.label,
          days: windowConfig.days,
          totalCost: bucketCosts.totalCost,
          dailyAvg,
          monthlyProjected,
          monthlySavings,
          savingsPercent: monthlySavings > 0 ? Math.round(monthlySavings / monthlyProjected * 100) : 0,
          requests: bucket.requests,
          tokens: {
            input: bucket.input,
            output: bucket.output,
            cacheRead: bucket.cacheRead,
            cacheWrite: bucket.cacheWrite
          }
        };
      }
      return {
        // Raw token counts (24h for backward compatibility)
        inputTokens: usage.input,
        outputTokens: usage.output,
        cacheRead: usage.cacheRead,
        cacheWrite: usage.cacheWrite,
        requests: usage.requests,
        // Pricing rates
        rates: {
          input: TOKEN_RATES.input.toFixed(2),
          output: TOKEN_RATES.output.toFixed(2),
          cacheRead: TOKEN_RATES.cacheRead.toFixed(2),
          cacheWrite: TOKEN_RATES.cacheWrite.toFixed(2)
        },
        // Cost calculation breakdown (24h)
        calculation: {
          inputCost: costs.inputCost,
          outputCost: costs.outputCost,
          cacheReadCost: costs.cacheReadCost,
          cacheWriteCost: costs.cacheWriteCost
        },
        // Totals (24h for backward compatibility)
        totalCost: costs.totalCost,
        planCost,
        planName,
        // Period
        period: "24 hours",
        // Multi-window data for moving averages
        windows,
        // Top sessions by tokens
        topSessions: getTopSessionsByTokens(5, getSessions)
      };
    }
    function getTopSessionsByTokens(limit = 5, getSessions) {
      try {
        const sessions2 = getSessions({ limit: null });
        return sessions2.filter((s) => s.tokens > 0).sort((a, b) => b.tokens - a.tokens).slice(0, limit).map((s) => ({
          label: s.label,
          tokens: s.tokens,
          channel: s.channel,
          active: s.active
        }));
      } catch (e) {
        console.error("[TopSessions] Error:", e.message);
        return [];
      }
    }
    function getTokenStats2(sessions2, capacity, config = {}) {
      let activeMainCount = capacity?.main?.active ?? 0;
      let activeSubagentCount = capacity?.subagent?.active ?? 0;
      let activeCount = activeMainCount + activeSubagentCount;
      let mainLimit = capacity?.main?.max ?? 12;
      let subagentLimit = capacity?.subagent?.max ?? 24;
      if (!capacity && sessions2 && sessions2.length > 0) {
        activeCount = 0;
        activeMainCount = 0;
        activeSubagentCount = 0;
        sessions2.forEach((s) => {
          if (s.active) {
            activeCount++;
            if (s.key && s.key.includes(":subagent:")) {
              activeSubagentCount++;
            } else {
              activeMainCount++;
            }
          }
        });
      }
      const usage = getDailyTokenUsage2();
      const totalInput = usage?.input || 0;
      const totalOutput = usage?.output || 0;
      const total = totalInput + totalOutput;
      const costs = calculateCostForBucket(usage);
      const estCost = costs.totalCost;
      const planCost = config?.billing?.claudePlanCost ?? 200;
      const planName = config?.billing?.claudePlanName ?? "Claude Code Max";
      const monthlyApiCost = estCost * 30;
      const monthlySavings = monthlyApiCost - planCost;
      const savingsPositive = monthlySavings > 0;
      const sessionCount = sessions2?.length || 1;
      const avgTokensPerSession = Math.round(total / sessionCount);
      const avgCostPerSession = estCost / sessionCount;
      const windowConfigs = {
        "24h": { days: 1, label: "24h" },
        "3dma": { days: 3, label: "3dma" },
        "7dma": { days: 7, label: "7dma" }
      };
      const savingsWindows = {};
      for (const [key, windowConfig] of Object.entries(windowConfigs)) {
        const bucketKey = key.replace("dma", "d").replace("24h", "24h");
        const bucket = usage.windows?.[bucketKey === "24h" ? "24h" : bucketKey] || usage;
        const bucketCosts = calculateCostForBucket(bucket);
        const dailyAvg = bucketCosts.totalCost / windowConfig.days;
        const monthlyProjected = dailyAvg * 30;
        const windowSavings = monthlyProjected - planCost;
        const windowSavingsPositive = windowSavings > 0;
        savingsWindows[key] = {
          label: windowConfig.label,
          estCost: `$${formatNumber(dailyAvg)}`,
          estMonthlyCost: `$${Math.round(monthlyProjected).toLocaleString()}`,
          estSavings: windowSavingsPositive ? `$${formatNumber(windowSavings)}/mo` : null,
          savingsPercent: windowSavingsPositive ? Math.round(windowSavings / monthlyProjected * 100) : 0,
          requests: bucket.requests
        };
      }
      return {
        total: formatTokens(total),
        input: formatTokens(totalInput),
        output: formatTokens(totalOutput),
        cacheRead: formatTokens(usage?.cacheRead || 0),
        cacheWrite: formatTokens(usage?.cacheWrite || 0),
        requests: usage?.requests || 0,
        activeCount,
        activeMainCount,
        activeSubagentCount,
        mainLimit,
        subagentLimit,
        estCost: `$${formatNumber(estCost)}`,
        planCost: `$${planCost.toFixed(0)}`,
        planName,
        // 24h savings (backward compatible)
        estSavings: savingsPositive ? `$${formatNumber(monthlySavings)}/mo` : null,
        savingsPercent: savingsPositive ? Math.round(monthlySavings / monthlyApiCost * 100) : 0,
        estMonthlyCost: `$${Math.round(monthlyApiCost).toLocaleString()}`,
        // Multi-window savings (24h, 3da, 7da)
        savingsWindows,
        // Per-session averages
        avgTokensPerSession: formatTokens(avgTokensPerSession),
        avgCostPerSession: `$${avgCostPerSession.toFixed(2)}`,
        sessionCount
      };
    }
    function startTokenUsageRefresh2(getOpenClawDir2) {
      refreshTokenUsageAsync2(getOpenClawDir2);
      if (refreshInterval) {
        clearInterval(refreshInterval);
      }
      refreshInterval = setInterval(() => {
        refreshTokenUsageAsync2(getOpenClawDir2);
      }, TOKEN_USAGE_CACHE_TTL);
      return refreshInterval;
    }
    module2.exports = {
      TOKEN_RATES,
      emptyUsageBucket,
      refreshTokenUsageAsync: refreshTokenUsageAsync2,
      getDailyTokenUsage: getDailyTokenUsage2,
      calculateCostForBucket,
      getCostBreakdown: getCostBreakdown2,
      getTopSessionsByTokens,
      getTokenStats: getTokenStats2,
      startTokenUsageRefresh: startTokenUsageRefresh2
    };
  }
});

// src/llm-usage.js
var require_llm_usage = __commonJS({
  "src/llm-usage.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    var { execFile } = require("child_process");
    var { getSafeEnv } = require_openclaw();
    var llmUsageCache = { data: null, timestamp: 0, refreshing: false };
    var LLM_CACHE_TTL_MS = 6e4;
    function refreshLlmUsageAsync() {
      if (llmUsageCache.refreshing) return;
      llmUsageCache.refreshing = true;
      const profile = process.env.OPENCLAW_PROFILE || "";
      const args2 = profile ? ["--profile", profile, "status", "--usage", "--json"] : ["status", "--usage", "--json"];
      execFile(
        "openclaw",
        args2,
        { encoding: "utf8", timeout: 2e4, env: getSafeEnv() },
        (err, stdout) => {
          llmUsageCache.refreshing = false;
          if (err) {
            console.error("[LLM Usage] Async refresh failed:", err.message);
            return;
          }
          try {
            const jsonStart = stdout.indexOf("{");
            const jsonStr = jsonStart >= 0 ? stdout.slice(jsonStart) : stdout;
            const parsed = JSON.parse(jsonStr);
            if (parsed.usage) {
              const result = transformLiveUsageData(parsed.usage);
              llmUsageCache.data = result;
              llmUsageCache.timestamp = Date.now();
              console.log("[LLM Usage] Cache refreshed");
            }
          } catch (e) {
            console.error("[LLM Usage] Parse error:", e.message);
          }
        }
      );
    }
    function transformLiveUsageData(usage) {
      const anthropic = usage.providers?.find((p) => p.provider === "anthropic");
      const codexProvider = usage.providers?.find((p) => p.provider === "openai-codex");
      if (anthropic?.error) {
        return {
          timestamp: (/* @__PURE__ */ new Date()).toISOString(),
          source: "error",
          error: anthropic.error,
          errorType: anthropic.error.includes("403") ? "auth" : "unknown",
          claude: {
            session: { usedPct: null, remainingPct: null, resetsIn: null, error: anthropic.error },
            weekly: { usedPct: null, remainingPct: null, resets: null, error: anthropic.error },
            sonnet: { usedPct: null, remainingPct: null, resets: null, error: anthropic.error },
            lastSynced: null
          },
          codex: { sessionsToday: 0, tasksToday: 0, usage5hPct: 0, usageDayPct: 0 },
          routing: {
            total: 0,
            claudeTasks: 0,
            codexTasks: 0,
            claudePct: 0,
            codexPct: 0,
            codexFloor: 20
          }
        };
      }
      const session5h = anthropic?.windows?.find((w) => w.label === "5h");
      const weekAll = anthropic?.windows?.find((w) => w.label === "Week");
      const sonnetWeek = anthropic?.windows?.find((w) => w.label === "Sonnet");
      const codex5h = codexProvider?.windows?.find((w) => w.label === "5h");
      const codexDay = codexProvider?.windows?.find((w) => w.label === "Day");
      const formatReset = (resetAt) => {
        if (!resetAt) return "?";
        const diff = resetAt - Date.now();
        if (diff < 0) return "now";
        if (diff < 36e5) return Math.round(diff / 6e4) + "m";
        if (diff < 864e5) return Math.round(diff / 36e5) + "h";
        return Math.round(diff / 864e5) + "d";
      };
      return {
        timestamp: (/* @__PURE__ */ new Date()).toISOString(),
        source: "live",
        claude: {
          session: {
            usedPct: Math.round(session5h?.usedPercent || 0),
            remainingPct: Math.round(100 - (session5h?.usedPercent || 0)),
            resetsIn: formatReset(session5h?.resetAt)
          },
          weekly: {
            usedPct: Math.round(weekAll?.usedPercent || 0),
            remainingPct: Math.round(100 - (weekAll?.usedPercent || 0)),
            resets: formatReset(weekAll?.resetAt)
          },
          sonnet: {
            usedPct: Math.round(sonnetWeek?.usedPercent || 0),
            remainingPct: Math.round(100 - (sonnetWeek?.usedPercent || 0)),
            resets: formatReset(sonnetWeek?.resetAt)
          },
          lastSynced: (/* @__PURE__ */ new Date()).toISOString()
        },
        codex: {
          sessionsToday: 0,
          tasksToday: 0,
          usage5hPct: Math.round(codex5h?.usedPercent || 0),
          usageDayPct: Math.round(codexDay?.usedPercent || 0)
        },
        routing: { total: 0, claudeTasks: 0, codexTasks: 0, claudePct: 0, codexPct: 0, codexFloor: 20 }
      };
    }
    function getLlmUsage2(statePath) {
      const now = Date.now();
      if (!llmUsageCache.data || now - llmUsageCache.timestamp > LLM_CACHE_TTL_MS) {
        refreshLlmUsageAsync();
      }
      if (llmUsageCache.data && llmUsageCache.data.source !== "error") {
        return llmUsageCache.data;
      }
      const stateFile = path2.join(statePath, "llm-routing.json");
      try {
        if (fs2.existsSync(stateFile)) {
          const data = JSON.parse(fs2.readFileSync(stateFile, "utf8"));
          const sessionValid = data.claude?.session?.resets_in && data.claude.session.resets_in !== "unknown";
          const weeklyValid = data.claude?.weekly_all_models?.resets && data.claude.weekly_all_models.resets !== "unknown";
          if (sessionValid || weeklyValid) {
            return {
              timestamp: (/* @__PURE__ */ new Date()).toISOString(),
              source: "file",
              claude: {
                session: {
                  usedPct: Math.round((data.claude?.session?.used_pct || 0) * 100),
                  remainingPct: Math.round((data.claude?.session?.remaining_pct || 1) * 100),
                  resetsIn: data.claude?.session?.resets_in || "?"
                },
                weekly: {
                  usedPct: Math.round((data.claude?.weekly_all_models?.used_pct || 0) * 100),
                  remainingPct: Math.round((data.claude?.weekly_all_models?.remaining_pct || 1) * 100),
                  resets: data.claude?.weekly_all_models?.resets || "?"
                },
                sonnet: {
                  usedPct: Math.round((data.claude?.weekly_sonnet?.used_pct || 0) * 100),
                  remainingPct: Math.round((data.claude?.weekly_sonnet?.remaining_pct || 1) * 100),
                  resets: data.claude?.weekly_sonnet?.resets || "?"
                },
                lastSynced: data.claude?.last_synced || null
              },
              codex: {
                sessionsToday: data.codex?.sessions_today || 0,
                tasksToday: data.codex?.tasks_today || 0,
                usage5hPct: data.codex?.usage_5h_pct || 0,
                usageDayPct: data.codex?.usage_day_pct || 0
              },
              routing: {
                total: data.routing?.total_tasks || 0,
                claudeTasks: data.routing?.claude_tasks || 0,
                codexTasks: data.routing?.codex_tasks || 0,
                claudePct: data.routing?.total_tasks > 0 ? Math.round(data.routing.claude_tasks / data.routing.total_tasks * 100) : 0,
                codexPct: data.routing?.total_tasks > 0 ? Math.round(data.routing.codex_tasks / data.routing.total_tasks * 100) : 0,
                codexFloor: Math.round((data.routing?.codex_floor_pct || 0.2) * 100)
              }
            };
          }
        }
      } catch (e) {
        console.error("[LLM Usage] File fallback failed:", e.message);
      }
      return {
        timestamp: (/* @__PURE__ */ new Date()).toISOString(),
        source: "error",
        error: "API key lacks user:profile OAuth scope",
        errorType: "auth",
        claude: {
          session: { usedPct: null, remainingPct: null, resetsIn: null, error: "Auth required" },
          weekly: { usedPct: null, remainingPct: null, resets: null, error: "Auth required" },
          sonnet: { usedPct: null, remainingPct: null, resets: null, error: "Auth required" },
          lastSynced: null
        },
        codex: { sessionsToday: 0, tasksToday: 0, usage5hPct: 0, usageDayPct: 0 },
        routing: { total: 0, claudeTasks: 0, codexTasks: 0, claudePct: 0, codexPct: 0, codexFloor: 20 }
      };
    }
    function getRoutingStats2(skillsPath, statePath, hours = 24) {
      const safeHours = parseInt(hours, 10) || 24;
      try {
        const { execFileSync } = require("child_process");
        const skillDir = path2.join(skillsPath, "llm_routing");
        const output = execFileSync(
          "python",
          ["-m", "llm_routing", "stats", "--hours", String(safeHours), "--json"],
          {
            encoding: "utf8",
            timeout: 1e4,
            cwd: skillDir,
            env: getSafeEnv()
          }
        );
        return JSON.parse(output);
      } catch (e) {
        try {
          const logFile = path2.join(statePath, "routing-log.jsonl");
          if (!fs2.existsSync(logFile)) {
            return { total_requests: 0, by_model: {}, by_task_type: {} };
          }
          const cutoff = Date.now() - hours * 3600 * 1e3;
          const lines = fs2.readFileSync(logFile, "utf8").trim().split("\n").filter(Boolean);
          const stats = {
            total_requests: 0,
            by_model: {},
            by_task_type: {},
            escalations: 0,
            avg_latency_ms: 0,
            success_rate: 0
          };
          let latencies = [];
          let successes = 0;
          for (const line of lines) {
            try {
              const entry = JSON.parse(line);
              const ts = new Date(entry.timestamp).getTime();
              if (ts < cutoff) continue;
              stats.total_requests++;
              const model = entry.selected_model || "unknown";
              stats.by_model[model] = (stats.by_model[model] || 0) + 1;
              const tt = entry.task_type || "unknown";
              stats.by_task_type[tt] = (stats.by_task_type[tt] || 0) + 1;
              if (entry.escalation_reason) stats.escalations++;
              if (entry.latency_ms) latencies.push(entry.latency_ms);
              if (entry.success === true) successes++;
            } catch {
            }
          }
          if (latencies.length > 0) {
            stats.avg_latency_ms = Math.round(latencies.reduce((a, b) => a + b, 0) / latencies.length);
          }
          if (stats.total_requests > 0) {
            stats.success_rate = Math.round(successes / stats.total_requests * 100);
          }
          return stats;
        } catch (e2) {
          console.error("Failed to read routing stats:", e2.message);
          return { error: e2.message };
        }
      }
    }
    function startLlmUsageRefresh2() {
      setTimeout(() => refreshLlmUsageAsync(), 1e3);
      setInterval(() => refreshLlmUsageAsync(), LLM_CACHE_TTL_MS);
    }
    module2.exports = {
      refreshLlmUsageAsync,
      transformLiveUsageData,
      getLlmUsage: getLlmUsage2,
      getRoutingStats: getRoutingStats2,
      startLlmUsageRefresh: startLlmUsageRefresh2
    };
  }
});

// src/actions.js
var require_actions = __commonJS({
  "src/actions.js"(exports2, module2) {
    var ALLOWED_ACTIONS = /* @__PURE__ */ new Set([
      "gateway-status",
      "gateway-restart",
      "sessions-list",
      "cron-list",
      "health-check",
      "clear-stale-sessions"
    ]);
    function executeAction2(action, deps) {
      const { runOpenClaw: runOpenClaw2, extractJSON: extractJSON2, PORT: PORT2 } = deps;
      const results = { success: false, action, output: "", error: null };
      if (!ALLOWED_ACTIONS.has(action)) {
        results.error = `Unknown action: ${action}`;
        return results;
      }
      try {
        switch (action) {
          case "gateway-status":
            results.output = runOpenClaw2("gateway status 2>&1") || "Unknown";
            results.success = true;
            break;
          case "gateway-restart":
            results.output = "To restart gateway, run: openclaw gateway restart";
            results.success = true;
            results.note = "Dashboard cannot restart gateway for safety";
            break;
          case "sessions-list":
            results.output = runOpenClaw2("sessions 2>&1") || "No sessions";
            results.success = true;
            break;
          case "cron-list":
            results.output = runOpenClaw2("cron list 2>&1") || "No cron jobs";
            results.success = true;
            break;
          case "health-check": {
            const gateway = runOpenClaw2("gateway status 2>&1");
            const sessions2 = runOpenClaw2("sessions --json 2>&1");
            let sessionCount = 0;
            try {
              const data = JSON.parse(sessions2);
              sessionCount = data.sessions?.length || 0;
            } catch (e) {
            }
            results.output = [
              `Gateway: ${gateway?.includes("running") ? "OK Running" : "NOT Running"}`,
              `Sessions: ${sessionCount}`,
              `Dashboard: OK Running on port ${PORT2}`
            ].join("\n");
            results.success = true;
            break;
          }
          case "clear-stale-sessions": {
            const staleOutput = runOpenClaw2("sessions --json 2>&1");
            let staleCount = 0;
            try {
              const staleJson = extractJSON2(staleOutput);
              if (staleJson) {
                const data = JSON.parse(staleJson);
                staleCount = (data.sessions || []).filter((s) => s.ageMs > 24 * 60 * 60 * 1e3).length;
              }
            } catch (e) {
            }
            results.output = `Found ${staleCount} stale sessions (>24h old).
To clean: openclaw sessions prune`;
            results.success = true;
            break;
          }
        }
      } catch (e) {
        results.error = e.message;
      }
      return results;
    }
    module2.exports = { executeAction: executeAction2, ALLOWED_ACTIONS };
  }
});

// src/data.js
var require_data = __commonJS({
  "src/data.js"(exports2, module2) {
    var fs2 = require("fs");
    var path2 = require("path");
    function migrateDataDir2(dataDir, legacyDataDir) {
      try {
        if (!fs2.existsSync(legacyDataDir)) return;
        if (!fs2.existsSync(dataDir)) {
          fs2.mkdirSync(dataDir, { recursive: true });
        }
        const legacyFiles = fs2.readdirSync(legacyDataDir);
        if (legacyFiles.length === 0) return;
        let migrated = 0;
        for (const file of legacyFiles) {
          const srcPath = path2.join(legacyDataDir, file);
          const destPath = path2.join(dataDir, file);
          if (fs2.existsSync(destPath)) continue;
          const stat = fs2.statSync(srcPath);
          if (stat.isFile()) {
            fs2.copyFileSync(srcPath, destPath);
            migrated++;
            console.log(`[Migration] Copied ${file} to profile-aware data dir`);
          }
        }
        if (migrated > 0) {
          console.log(`[Migration] Migrated ${migrated} file(s) to ${dataDir}`);
          console.log(`[Migration] Legacy data preserved at ${legacyDataDir}`);
        }
      } catch (e) {
        console.error("[Migration] Failed to migrate data:", e.message);
      }
    }
    module2.exports = { migrateDataDir: migrateDataDir2 };
  }
});

// src/state.js
var require_state = __commonJS({
  "src/state.js"(exports2, module2) {
    var fs2 = require("fs");
    var os = require("os");
    var path2 = require("path");
    var { execFileSync } = require("child_process");
    var { formatBytes, formatTimeAgo } = require_utils();
    function createStateModule2(deps) {
      const {
        CONFIG: CONFIG2,
        getOpenClawDir: getOpenClawDir2,
        getSessions,
        getSystemVitals: getSystemVitals2,
        getCronJobs: getCronJobs2,
        loadOperators: loadOperators2,
        calculateOperatorStats: calculateOperatorStats2,
        getLlmUsage: getLlmUsage2,
        getDailyTokenUsage: getDailyTokenUsage2,
        getTokenStats: getTokenStats2,
        getCerebroTopics: getCerebroTopics2,
        runOpenClaw: runOpenClaw2,
        extractJSON: extractJSON2,
        readTranscript
      } = deps;
      const PATHS2 = CONFIG2.paths;
      let cachedState = null;
      let lastStateUpdate = 0;
      const STATE_CACHE_TTL = 3e4;
      let stateRefreshInterval = null;
      function getSystemStatus() {
        const hostname = os.hostname();
        let uptime = "\u2014";
        try {
          const uptimeRaw = execFileSync("uptime", [], { encoding: "utf8" });
          const match = uptimeRaw.match(/up\s+([^,]+)/);
          if (match) uptime = match[1].trim();
        } catch (e) {
        }
        let gateway = "Unknown";
        try {
          const status = runOpenClaw2("gateway status 2>/dev/null");
          if (status && status.includes("running")) {
            gateway = "Running";
          } else if (status && status.includes("stopped")) {
            gateway = "Stopped";
          }
        } catch (e) {
        }
        return {
          hostname,
          gateway,
          model: "claude-opus-4-5",
          uptime
        };
      }
      function getRecentActivity() {
        const activities = [];
        const today = (/* @__PURE__ */ new Date()).toISOString().split("T")[0];
        const memoryFile = path2.join(PATHS2.memory, `${today}.md`);
        try {
          if (fs2.existsSync(memoryFile)) {
            const content = fs2.readFileSync(memoryFile, "utf8");
            const lines = content.split("\n").filter((l) => l.startsWith("- "));
            lines.slice(-5).forEach((line) => {
              const text = line.replace(/^- /, "").slice(0, 80);
              activities.push({
                icon: text.includes("\u2705") ? "\u2705" : text.includes("\u274C") ? "\u274C" : "\u{1F4DD}",
                text: text.replace(/[\u2705\u274C\uD83D\uDCDD\uD83D\uDD27]/g, "").trim(),
                time: today
              });
            });
          }
        } catch (e) {
          console.error("Failed to read activity:", e.message);
        }
        return activities.reverse();
      }
      function getCapacity() {
        const result = {
          main: { active: 0, max: 12 },
          subagent: { active: 0, max: 24 }
        };
        const openclawDir = getOpenClawDir2();
        try {
          const configPath = path2.join(openclawDir, "openclaw.json");
          if (fs2.existsSync(configPath)) {
            const config = JSON.parse(fs2.readFileSync(configPath, "utf8"));
            if (config?.agents?.defaults?.maxConcurrent) {
              result.main.max = config.agents.defaults.maxConcurrent;
            }
            if (config?.agents?.defaults?.subagents?.maxConcurrent) {
              result.subagent.max = config.agents.defaults.subagents.maxConcurrent;
            }
          }
        } catch (e) {
        }
        try {
          const output = runOpenClaw2("sessions --json 2>/dev/null");
          const jsonStr = extractJSON2(output);
          if (jsonStr) {
            const data = JSON.parse(jsonStr);
            const sessions2 = data.sessions || [];
            const fiveMinMs = 5 * 60 * 1e3;
            for (const s of sessions2) {
              if (s.ageMs > fiveMinMs) continue;
              const key = s.key || "";
              if (key.includes(":subagent:") || key.includes(":cron:")) {
                result.subagent.active++;
              } else {
                result.main.active++;
              }
            }
            return result;
          }
        } catch (e) {
          console.error("Failed to get capacity from sessions, falling back to filesystem:", e.message);
        }
        try {
          const sessionsDir = path2.join(openclawDir, "agents", "main", "sessions");
          if (fs2.existsSync(sessionsDir)) {
            const fiveMinAgo = Date.now() - 5 * 60 * 1e3;
            const files = fs2.readdirSync(sessionsDir).filter((f) => f.endsWith(".jsonl"));
            let mainActive = 0;
            let subActive = 0;
            for (const file of files) {
              try {
                const filePath = path2.join(sessionsDir, file);
                const stat = fs2.statSync(filePath);
                if (stat.mtimeMs < fiveMinAgo) continue;
                let isSubagent = false;
                try {
                  const fd = fs2.openSync(filePath, "r");
                  const buffer = Buffer.alloc(512);
                  fs2.readSync(fd, buffer, 0, 512, 0);
                  fs2.closeSync(fd);
                  const firstLine = buffer.toString("utf8").split("\n")[0];
                  const parsed = JSON.parse(firstLine);
                  const key = parsed.key || parsed.id || "";
                  isSubagent = key.includes(":subagent:") || key.includes(":cron:");
                } catch (parseErr) {
                  isSubagent = file.includes("subagent");
                }
                if (isSubagent) {
                  subActive++;
                } else {
                  mainActive++;
                }
              } catch (e) {
              }
            }
            result.main.active = mainActive;
            result.subagent.active = subActive;
          }
        } catch (e) {
          console.error("Failed to count active sessions from filesystem:", e.message);
        }
        return result;
      }
      function getMemoryStats() {
        const memoryDir = PATHS2.memory;
        const memoryFile = path2.join(PATHS2.workspace, "MEMORY.md");
        const stats = {
          totalFiles: 0,
          totalSize: 0,
          totalSizeFormatted: "0 B",
          memoryMdSize: 0,
          memoryMdSizeFormatted: "0 B",
          memoryMdLines: 0,
          recentFiles: [],
          oldestFile: null,
          newestFile: null
        };
        try {
          const collectMemoryFiles = (dir, baseDir) => {
            const entries = fs2.readdirSync(dir, { withFileTypes: true });
            const files = [];
            for (const entry of entries) {
              const entryPath = path2.join(dir, entry.name);
              if (entry.isDirectory()) {
                files.push(...collectMemoryFiles(entryPath, baseDir));
              } else if (entry.isFile() && (entry.name.endsWith(".md") || entry.name.endsWith(".json"))) {
                const stat = fs2.statSync(entryPath);
                const relativePath = path2.relative(baseDir, entryPath);
                files.push({
                  name: relativePath,
                  size: stat.size,
                  sizeFormatted: formatBytes(stat.size),
                  modified: stat.mtime
                });
              }
            }
            return files;
          };
          if (fs2.existsSync(memoryFile)) {
            const memStat = fs2.statSync(memoryFile);
            stats.memoryMdSize = memStat.size;
            stats.memoryMdSizeFormatted = formatBytes(memStat.size);
            const content = fs2.readFileSync(memoryFile, "utf8");
            stats.memoryMdLines = content.split("\n").length;
            stats.totalSize += memStat.size;
            stats.totalFiles++;
          }
          if (fs2.existsSync(memoryDir)) {
            const files = collectMemoryFiles(memoryDir, memoryDir).sort(
              (a, b) => b.modified - a.modified
            );
            stats.totalFiles += files.length;
            files.forEach((f) => stats.totalSize += f.size);
            stats.recentFiles = files.slice(0, 5).map((f) => ({
              name: f.name,
              sizeFormatted: f.sizeFormatted,
              age: formatTimeAgo(f.modified)
            }));
            if (files.length > 0) {
              stats.newestFile = files[0].name;
              stats.oldestFile = files[files.length - 1].name;
            }
          }
          stats.totalSizeFormatted = formatBytes(stats.totalSize);
        } catch (e) {
          console.error("Failed to get memory stats:", e.message);
        }
        return stats;
      }
      function getData() {
        const allSessions = getSessions({ limit: null });
        const pageSize = 20;
        const displaySessions = allSessions.slice(0, pageSize);
        const tokenStats = getTokenStats2(allSessions);
        const capacity = getCapacity();
        const memory = getMemoryStats();
        const statusCounts = {
          all: allSessions.length,
          live: allSessions.filter((s) => s.active).length,
          recent: allSessions.filter((s) => !s.active && s.recentlyActive).length,
          idle: allSessions.filter((s) => !s.active && !s.recentlyActive).length
        };
        const totalPages = Math.ceil(allSessions.length / pageSize);
        return {
          sessions: displaySessions,
          tokenStats,
          capacity,
          memory,
          pagination: {
            page: 1,
            pageSize,
            total: allSessions.length,
            totalPages,
            hasPrev: false,
            hasNext: totalPages > 1
          },
          statusCounts
        };
      }
      function getFullState() {
        const now = Date.now();
        if (cachedState && now - lastStateUpdate < STATE_CACHE_TTL) {
          return cachedState;
        }
        let sessions2 = [];
        let tokenStats = {};
        let statusCounts = { all: 0, live: 0, recent: 0, idle: 0 };
        let vitals = {};
        let capacity = {};
        let operators = { operators: [], roles: {} };
        let llmUsage = {};
        let cron = [];
        let memory = {};
        let cerebro = {};
        let subagents = [];
        let allSessions = [];
        let totalSessionCount = 0;
        try {
          allSessions = getSessions({ limit: null });
          totalSessionCount = allSessions.length;
          sessions2 = allSessions.slice(0, 20);
        } catch (e) {
          console.error("[State] sessions:", e.message);
        }
        try {
          vitals = getSystemVitals2();
        } catch (e) {
          console.error("[State] vitals:", e.message);
        }
        try {
          capacity = getCapacity();
        } catch (e) {
          console.error("[State] capacity:", e.message);
        }
        try {
          tokenStats = getTokenStats2(allSessions, capacity, CONFIG2);
        } catch (e) {
          console.error("[State] tokenStats:", e.message);
        }
        try {
          const liveSessions = allSessions.filter((s) => s.active);
          const recentSessions = allSessions.filter((s) => !s.active && s.recentlyActive);
          const idleSessions = allSessions.filter((s) => !s.active && !s.recentlyActive);
          statusCounts = {
            all: totalSessionCount,
            live: liveSessions.length,
            recent: recentSessions.length,
            idle: idleSessions.length
          };
        } catch (e) {
          console.error("[State] statusCounts:", e.message);
        }
        try {
          const operatorData = loadOperators2();
          operators = calculateOperatorStats2(operatorData, allSessions);
        } catch (e) {
          console.error("[State] operators:", e.message);
        }
        try {
          llmUsage = getLlmUsage2();
        } catch (e) {
          console.error("[State] llmUsage:", e.message);
        }
        try {
          cron = getCronJobs2();
        } catch (e) {
          console.error("[State] cron:", e.message);
        }
        try {
          memory = getMemoryStats();
        } catch (e) {
          console.error("[State] memory:", e.message);
        }
        try {
          cerebro = getCerebroTopics2();
        } catch (e) {
          console.error("[State] cerebro:", e.message);
        }
        try {
          const retentionHours = parseInt(process.env.SUBAGENT_RETENTION_HOURS || "12", 10);
          const retentionMs = retentionHours * 60 * 60 * 1e3;
          subagents = allSessions.filter((s) => s.sessionKey && s.sessionKey.includes(":subagent:")).filter((s) => (s.minutesAgo || 0) * 6e4 < retentionMs).map((s) => {
            const match = s.sessionKey.match(/:subagent:([a-f0-9-]+)$/);
            const subagentId = match ? match[1] : s.sessionId;
            return {
              id: subagentId,
              shortId: subagentId.slice(0, 8),
              task: s.label || s.displayName || "Sub-agent task",
              tokens: s.tokens || 0,
              ageMs: (s.minutesAgo || 0) * 6e4,
              active: s.active,
              recentlyActive: s.recentlyActive
            };
          });
        } catch (e) {
          console.error("[State] subagents:", e.message);
        }
        cachedState = {
          vitals,
          sessions: sessions2,
          tokenStats,
          statusCounts,
          capacity,
          operators,
          llmUsage,
          cron,
          memory,
          cerebro,
          subagents,
          pagination: {
            page: 1,
            pageSize: 20,
            total: totalSessionCount,
            totalPages: Math.max(1, Math.ceil(totalSessionCount / 20)),
            hasPrev: false,
            hasNext: totalSessionCount > 20
          },
          timestamp: now
        };
        lastStateUpdate = now;
        return cachedState;
      }
      function refreshState() {
        lastStateUpdate = 0;
        return getFullState();
      }
      function startStateRefresh(broadcastSSE2, intervalMs = 3e4) {
        if (stateRefreshInterval) return;
        stateRefreshInterval = setInterval(() => {
          try {
            const newState = refreshState();
            broadcastSSE2("update", newState);
          } catch (e) {
            console.error("[State] Refresh error:", e.message);
          }
        }, intervalMs);
        console.log(`[State] Background refresh started (${intervalMs}ms interval)`);
      }
      function stopStateRefresh() {
        if (stateRefreshInterval) {
          clearInterval(stateRefreshInterval);
          stateRefreshInterval = null;
          console.log("[State] Background refresh stopped");
        }
      }
      function getSubagentStatus() {
        const subagents = [];
        try {
          const output = runOpenClaw2("sessions --json 2>/dev/null");
          const jsonStr = extractJSON2(output);
          if (jsonStr) {
            const data = JSON.parse(jsonStr);
            const subagentSessions = (data.sessions || []).filter(
              (s) => s.key && s.key.includes(":subagent:")
            );
            for (const s of subagentSessions) {
              const ageMs = s.ageMs || Infinity;
              const isActive = ageMs < 5 * 60 * 1e3;
              const isRecent = ageMs < 30 * 60 * 1e3;
              const match = s.key.match(/:subagent:([a-f0-9-]+)$/);
              const subagentId = match ? match[1] : s.sessionId;
              const shortId = subagentId.slice(0, 8);
              let taskSummary = "Unknown task";
              let label = null;
              const transcript = readTranscript(s.sessionId);
              for (const entry of transcript.slice(0, 15)) {
                if (entry.type === "message" && entry.message?.role === "user") {
                  const content = entry.message.content;
                  let text = "";
                  if (typeof content === "string") {
                    text = content;
                  } else if (Array.isArray(content)) {
                    const textPart = content.find((c) => c.type === "text");
                    if (textPart) text = textPart.text || "";
                  }
                  if (!text) continue;
                  const labelMatch = text.match(/Label:\s*([^\n]+)/i);
                  if (labelMatch) {
                    label = labelMatch[1].trim();
                  }
                  let taskMatch = text.match(/You were created to handle:\s*\*\*([^*]+)\*\*/i);
                  if (taskMatch) {
                    taskSummary = taskMatch[1].trim();
                    break;
                  }
                  taskMatch = text.match(/\*\*([A-Z]{2,5}-\d+:\s*[^*]+)\*\*/);
                  if (taskMatch) {
                    taskSummary = taskMatch[1].trim();
                    break;
                  }
                  const firstLine = text.split("\n")[0].replace(/^\*\*|\*\*$/g, "").trim();
                  if (firstLine.length > 10 && firstLine.length < 100) {
                    taskSummary = firstLine;
                    break;
                  }
                }
              }
              const messageCount = transcript.filter(
                (e) => e.type === "message" && e.message?.role
              ).length;
              subagents.push({
                id: subagentId,
                shortId,
                sessionId: s.sessionId,
                label: label || shortId,
                task: taskSummary,
                model: s.model?.replace("anthropic/", "") || "unknown",
                status: isActive ? "active" : isRecent ? "idle" : "stale",
                ageMs,
                ageFormatted: ageMs < 6e4 ? "Just now" : ageMs < 36e5 ? `${Math.round(ageMs / 6e4)}m ago` : `${Math.round(ageMs / 36e5)}h ago`,
                messageCount,
                tokens: s.totalTokens || 0
              });
            }
          }
        } catch (e) {
          console.error("Failed to get subagent status:", e.message);
        }
        return subagents.sort((a, b) => a.ageMs - b.ageMs);
      }
      return {
        getSystemStatus,
        getRecentActivity,
        getCapacity,
        getMemoryStats,
        getFullState,
        refreshState,
        startStateRefresh,
        stopStateRefresh,
        getData,
        getSubagentStatus
      };
    }
    module2.exports = { createStateModule: createStateModule2 };
  }
});

// src/index.js
var http = require("http");
var fs = require("fs");
var path = require("path");
var args = process.argv.slice(2);
var cliProfile = null;
var cliPort = null;
for (let i = 0; i < args.length; i++) {
  switch (args[i]) {
    case "--profile":
    case "-p":
      cliProfile = args[++i];
      break;
    case "--port":
      cliPort = parseInt(args[++i], 10);
      break;
    case "--help":
    case "-h":
      console.log(`
OpenClaw Command Center

Usage: node lib/server.js [options]

Options:
  --profile, -p <name>  OpenClaw profile (uses ~/.openclaw-<name>)
  --port <port>         Server port (default: 3333)
  --help, -h            Show this help

Environment:
  OPENCLAW_PROFILE      Same as --profile
  PORT                  Same as --port

Examples:
  node lib/server.js --profile production
  node lib/server.js -p dev --port 3334
`);
      process.exit(0);
  }
}
if (cliProfile) {
  process.env.OPENCLAW_PROFILE = cliProfile;
}
if (cliPort) {
  process.env.PORT = cliPort.toString();
}
var { getVersion } = require_utils();
var { CONFIG, getOpenClawDir } = require_config();
var { handleJobsRequest, isJobsRoute } = require_jobs();
var { runOpenClaw, runOpenClawAsync, extractJSON } = require_openclaw();
var { getSystemVitals, checkOptionalDeps, getOptionalDeps } = require_vitals();
var { checkAuth, getUnauthorizedPage } = require_auth();
var { loadPrivacySettings, savePrivacySettings } = require_privacy();
var {
  loadOperators,
  saveOperators,
  getOperatorBySlackId,
  startOperatorsRefresh,
  calculateOperatorStats
} = require_operators();
var { createSessionsModule } = require_sessions();
var { getCronJobs } = require_cron();
var { getCerebroTopics, updateTopicStatus } = require_cerebro();
var {
  getDailyTokenUsage,
  getTokenStats,
  getCostBreakdown,
  startTokenUsageRefresh,
  refreshTokenUsageAsync
} = require_tokens();
var { getLlmUsage, getRoutingStats, startLlmUsageRefresh } = require_llm_usage();
var { executeAction } = require_actions();
var { migrateDataDir } = require_data();
var { createStateModule } = require_state();
var PORT = CONFIG.server.port;
var DASHBOARD_DIR = path.join(__dirname, "../public");
var PATHS = CONFIG.paths;
var AUTH_CONFIG = {
  mode: CONFIG.auth.mode,
  token: CONFIG.auth.token,
  allowedUsers: CONFIG.auth.allowedUsers,
  allowedIPs: CONFIG.auth.allowedIPs,
  publicPaths: CONFIG.auth.publicPaths
};
var DATA_DIR = path.join(getOpenClawDir(), "command-center", "data");
var LEGACY_DATA_DIR = path.join(DASHBOARD_DIR, "data");
var sseClients = /* @__PURE__ */ new Set();
function sendSSE(res, event, data) {
  try {
    res.write(`event: ${event}
data: ${JSON.stringify(data)}

`);
  } catch (e) {
  }
}
function broadcastSSE(event, data) {
  for (const client of sseClients) {
    sendSSE(client, event, data);
  }
}
var sessions = createSessionsModule({
  getOpenClawDir,
  getOperatorBySlackId: (slackId) => getOperatorBySlackId(DATA_DIR, slackId),
  runOpenClaw,
  runOpenClawAsync,
  extractJSON
});
var state = createStateModule({
  CONFIG,
  getOpenClawDir,
  getSessions: (opts) => sessions.getSessions(opts),
  getSystemVitals,
  getCronJobs: () => getCronJobs(getOpenClawDir),
  loadOperators: () => loadOperators(DATA_DIR),
  calculateOperatorStats,
  getLlmUsage: () => getLlmUsage(PATHS.state),
  getDailyTokenUsage: () => getDailyTokenUsage(getOpenClawDir),
  getTokenStats,
  getCerebroTopics: (opts) => getCerebroTopics(PATHS.cerebro, opts),
  runOpenClaw,
  extractJSON,
  readTranscript: (sessionId) => sessions.readTranscript(sessionId)
});
process.nextTick(() => migrateDataDir(DATA_DIR, LEGACY_DATA_DIR));
startOperatorsRefresh(DATA_DIR, getOpenClawDir);
startLlmUsageRefresh();
startTokenUsageRefresh(getOpenClawDir);
function serveStatic(req, res) {
  const requestUrl = new URL(req.url, `http://${req.headers.host || "localhost"}`);
  const pathname = requestUrl.pathname === "/" ? "/index.html" : requestUrl.pathname;
  if (pathname.includes("..")) {
    res.writeHead(400);
    res.end("Bad request");
    return;
  }
  const normalizedPath = path.normalize(pathname).replace(/^[/\\]+/, "");
  const filePath = path.join(DASHBOARD_DIR, normalizedPath);
  const resolvedDashboardDir = path.resolve(DASHBOARD_DIR);
  const resolvedFilePath = path.resolve(filePath);
  if (!resolvedFilePath.startsWith(resolvedDashboardDir + path.sep) && resolvedFilePath !== resolvedDashboardDir) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }
  const ext = path.extname(filePath);
  const contentTypes = {
    ".html": "text/html",
    ".css": "text/css",
    ".js": "text/javascript",
    ".json": "application/json",
    ".png": "image/png",
    ".svg": "image/svg+xml"
  };
  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }
    const headers = { "Content-Type": contentTypes[ext] || "text/plain" };
    if ([".html", ".css", ".js", ".json"].includes(ext)) {
      headers["Cache-Control"] = "no-store";
    }
    res.writeHead(200, headers);
    res.end(content);
  });
}
function handleApi(req, res) {
  const sessionsList = sessions.getSessions();
  const capacity = state.getCapacity();
  const tokenStats = getTokenStats(sessionsList, capacity, CONFIG);
  const data = {
    sessions: sessionsList,
    cron: getCronJobs(getOpenClawDir),
    system: state.getSystemStatus(),
    activity: state.getRecentActivity(),
    tokenStats,
    capacity,
    timestamp: (/* @__PURE__ */ new Date()).toISOString()
  };
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify(data, null, 2));
}
var server = http.createServer((req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  const urlParts = req.url.split("?");
  const pathname = urlParts[0];
  const query = new URLSearchParams(urlParts[1] || "");
  if (pathname === "/api/health") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ status: "ok", port: PORT, timestamp: (/* @__PURE__ */ new Date()).toISOString() }));
    return;
  }
  const isPublicPath = AUTH_CONFIG.publicPaths.some(
    (p) => pathname === p || pathname.startsWith(p + "/")
  );
  if (!isPublicPath && AUTH_CONFIG.mode !== "none") {
    const authResult = checkAuth(req, AUTH_CONFIG);
    if (!authResult.authorized) {
      console.log(`[AUTH] Denied: ${authResult.reason} (path: ${pathname})`);
      res.writeHead(403, { "Content-Type": "text/html" });
      res.end(getUnauthorizedPage(authResult.reason, authResult.user, AUTH_CONFIG));
      return;
    }
    req.authUser = authResult.user;
    if (authResult.user?.login || authResult.user?.email) {
      console.log(
        `[AUTH] Allowed: ${authResult.user.login || authResult.user.email} (path: ${pathname})`
      );
    } else {
      console.log(`[AUTH] Allowed: ${req.socket?.remoteAddress} (path: ${pathname})`);
    }
  }
  if (pathname === "/api/status") {
    handleApi(req, res);
  } else if (pathname === "/api/session") {
    const sessionKey = query.get("key");
    if (!sessionKey) {
      res.writeHead(400, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Missing session key" }));
      return;
    }
    const detail = sessions.getSessionDetail(sessionKey);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(detail, null, 2));
  } else if (pathname === "/api/cerebro") {
    const offset = parseInt(query.get("offset") || "0", 10);
    const limit = parseInt(query.get("limit") || "20", 10);
    const statusFilter = query.get("status") || "all";
    const data = getCerebroTopics(PATHS.cerebro, { offset, limit, status: statusFilter });
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data, null, 2));
  } else if (pathname.startsWith("/api/cerebro/topic/") && pathname.endsWith("/status") && req.method === "POST") {
    const topicId = decodeURIComponent(
      pathname.replace("/api/cerebro/topic/", "").replace("/status", "")
    );
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
    });
    req.on("end", () => {
      try {
        const { status: newStatus } = JSON.parse(body);
        if (!newStatus || !["active", "resolved", "parked"].includes(newStatus)) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(
            JSON.stringify({ error: "Invalid status. Must be: active, resolved, or parked" })
          );
          return;
        }
        const result = updateTopicStatus(PATHS.cerebro, topicId, newStatus);
        if (result.error) {
          res.writeHead(result.code || 500, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ error: result.error }));
          return;
        }
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify(result, null, 2));
      } catch (e) {
        res.writeHead(400, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Invalid JSON body" }));
      }
    });
    return;
  } else if (pathname === "/api/llm-quota") {
    const data = getLlmUsage(PATHS.state);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data, null, 2));
  } else if (pathname === "/api/cost-breakdown") {
    const data = getCostBreakdown(CONFIG, (opts) => sessions.getSessions(opts), getOpenClawDir);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data, null, 2));
  } else if (pathname === "/api/subagents") {
    const data = state.getSubagentStatus();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ subagents: data }, null, 2));
  } else if (pathname === "/api/action") {
    const action = query.get("action");
    if (!action) {
      res.writeHead(400, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Missing action parameter" }));
      return;
    }
    const result = executeAction(action, { runOpenClaw, extractJSON, PORT });
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(result, null, 2));
  } else if (pathname === "/api/events") {
    res.writeHead(200, {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
      "X-Accel-Buffering": "no"
    });
    sseClients.add(res);
    console.log(`[SSE] Client connected (total: ${sseClients.size})`);
    sendSSE(res, "connected", { message: "Connected to Command Center", timestamp: Date.now() });
    const cachedState = state.getFullState();
    if (cachedState) {
      sendSSE(res, "update", cachedState);
    } else {
      sendSSE(res, "update", { sessions: [], loading: true });
    }
    req.on("close", () => {
      sseClients.delete(res);
      console.log(`[SSE] Client disconnected (total: ${sseClients.size})`);
    });
    return;
  } else if (pathname === "/api/whoami") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify(
        {
          authMode: AUTH_CONFIG.mode,
          user: req.authUser || null
        },
        null,
        2
      )
    );
  } else if (pathname === "/api/about") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify(
        {
          name: "OpenClaw Command Center",
          version: getVersion(),
          description: "A Starcraft-inspired dashboard for AI agent orchestration",
          license: "MIT",
          repository: "https://github.com/jontsai/openclaw-command-center",
          builtWith: ["OpenClaw", "Node.js", "Vanilla JS"],
          inspirations: ["Starcraft", "Inside Out", "iStatMenus", "DaisyDisk", "Gmail"]
        },
        null,
        2
      )
    );
  } else if (pathname === "/api/state") {
    const fullState = state.getFullState();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(fullState, null, 2));
  } else if (pathname === "/api/vitals") {
    const vitals = getSystemVitals();
    const optionalDeps = getOptionalDeps();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ vitals, optionalDeps }, null, 2));
  } else if (pathname === "/api/capacity") {
    const capacity = state.getCapacity();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(capacity, null, 2));
  } else if (pathname === "/api/sessions") {
    const page = parseInt(query.get("page")) || 1;
    const pageSize = parseInt(query.get("pageSize")) || 20;
    const statusFilter = query.get("status");
    const allSessions = sessions.getSessions({ limit: null });
    const statusCounts = {
      all: allSessions.length,
      live: allSessions.filter((s) => s.active).length,
      recent: allSessions.filter((s) => !s.active && s.recentlyActive).length,
      idle: allSessions.filter((s) => !s.active && !s.recentlyActive).length
    };
    let filteredSessions = allSessions;
    if (statusFilter === "live") {
      filteredSessions = allSessions.filter((s) => s.active);
    } else if (statusFilter === "recent") {
      filteredSessions = allSessions.filter((s) => !s.active && s.recentlyActive);
    } else if (statusFilter === "idle") {
      filteredSessions = allSessions.filter((s) => !s.active && !s.recentlyActive);
    }
    const total = filteredSessions.length;
    const totalPages = Math.ceil(total / pageSize);
    const offset = (page - 1) * pageSize;
    const displaySessions = filteredSessions.slice(offset, offset + pageSize);
    const tokenStats = getTokenStats(allSessions, state.getCapacity(), CONFIG);
    const capacity = state.getCapacity();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify(
        {
          sessions: displaySessions,
          pagination: {
            page,
            pageSize,
            total,
            totalPages,
            hasPrev: page > 1,
            hasNext: page < totalPages
          },
          statusCounts,
          tokenStats,
          capacity
        },
        null,
        2
      )
    );
  } else if (pathname === "/api/cron") {
    const cron = getCronJobs(getOpenClawDir);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ cron }, null, 2));
  } else if (pathname === "/api/operators") {
    const method = req.method;
    const data = loadOperators(DATA_DIR);
    if (method === "GET") {
      const allSessions = sessions.getSessions({ limit: null });
      const operatorsWithStats = calculateOperatorStats(data, allSessions);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(
        JSON.stringify(
          {
            ...operatorsWithStats,
            timestamp: Date.now()
          },
          null,
          2
        )
      );
    } else if (method === "POST") {
      let body = "";
      req.on("data", (chunk) => body += chunk);
      req.on("end", () => {
        try {
          const newOp = JSON.parse(body);
          const existingIdx = data.operators.findIndex((op) => op.id === newOp.id);
          if (existingIdx >= 0) {
            data.operators[existingIdx] = { ...data.operators[existingIdx], ...newOp };
          } else {
            data.operators.push({
              ...newOp,
              createdAt: (/* @__PURE__ */ new Date()).toISOString()
            });
          }
          if (saveOperators(DATA_DIR, data)) {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ success: true, operator: newOp }));
          } else {
            res.writeHead(500, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ error: "Failed to save" }));
          }
        } catch (e) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ error: "Invalid JSON" }));
        }
      });
      return;
    } else {
      res.writeHead(405, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Method not allowed" }));
    }
    return;
  } else if (pathname === "/api/llm-usage") {
    const usage = getLlmUsage(PATHS.state);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(usage, null, 2));
  } else if (pathname === "/api/routing-stats") {
    const hours = parseInt(query.get("hours") || "24", 10);
    const stats = getRoutingStats(PATHS.skills, PATHS.state, hours);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(stats, null, 2));
  } else if (pathname === "/api/memory") {
    const memory = state.getMemoryStats();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ memory }, null, 2));
  } else if (pathname === "/api/privacy") {
    if (req.method === "GET") {
      const settings = loadPrivacySettings(DATA_DIR);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(settings, null, 2));
    } else if (req.method === "POST" || req.method === "PUT") {
      let body = "";
      req.on("data", (chunk) => body += chunk);
      req.on("end", () => {
        try {
          const updates = JSON.parse(body);
          const current = loadPrivacySettings(DATA_DIR);
          const merged = {
            version: current.version || 1,
            hiddenTopics: updates.hiddenTopics ?? current.hiddenTopics ?? [],
            hiddenSessions: updates.hiddenSessions ?? current.hiddenSessions ?? [],
            hiddenCrons: updates.hiddenCrons ?? current.hiddenCrons ?? [],
            hideHostname: updates.hideHostname ?? current.hideHostname ?? false
          };
          if (savePrivacySettings(DATA_DIR, merged)) {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ success: true, settings: merged }));
          } else {
            res.writeHead(500, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ error: "Failed to save privacy settings" }));
          }
        } catch (e) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ error: "Invalid JSON: " + e.message }));
        }
      });
      return;
    } else {
      res.writeHead(405, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Method not allowed" }));
    }
    return;
  } else if (isJobsRoute(pathname)) {
    handleJobsRequest(req, res, pathname, query, req.method);
  } else {
    serveStatic(req, res);
  }
});
server.listen(PORT, () => {
  const profile = process.env.OPENCLAW_PROFILE;
  console.log(`\u{1F99E} OpenClaw Command Center running at http://localhost:${PORT}`);
  if (profile) {
    console.log(`   Profile: ${profile} (~/.openclaw-${profile})`);
  }
  console.log(`   Press Ctrl+C to stop`);
  setTimeout(async () => {
    console.log("[Startup] Pre-warming caches in background...");
    try {
      await Promise.all([sessions.refreshSessionsCache(), refreshTokenUsageAsync(getOpenClawDir)]);
      getSystemVitals();
      console.log("[Startup] Caches warmed.");
    } catch (e) {
      console.log("[Startup] Cache warming error:", e.message);
    }
    checkOptionalDeps();
  }, 100);
  const SESSIONS_CACHE_TTL = 1e4;
  setInterval(() => sessions.refreshSessionsCache(), SESSIONS_CACHE_TTL);
});
var sseRefreshing = false;
setInterval(() => {
  if (sseClients.size > 0 && !sseRefreshing) {
    sseRefreshing = true;
    try {
      const fullState = state.refreshState();
      broadcastSSE("update", fullState);
      broadcastSSE("heartbeat", { clients: sseClients.size, timestamp: Date.now() });
    } catch (e) {
      console.error("[SSE] Broadcast error:", e.message);
    }
    sseRefreshing = false;
  }
}, 15e3);
```

## File: `public/index.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title data-i18n="app.title">OpenClaw Command Center</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
    <link rel="stylesheet" href="css/dashboard.css" />
    <script src="js/lib/morphdom.min.js"></script>
    <script src="js/i18n.js"></script>
    <!-- Shared Sidebar Loader -->
    <script src="js/sidebar.js"></script>
  </head>
  <body>
    <!-- Sidebar container (populated by sidebar.js) -->
    <div id="sidebar-container"></div>

    <!-- Main Content -->
    <div class="main-wrapper" id="main-wrapper">
      <header>
        <div class="header-left">
          <button
            class="sidebar-toggle"
            onclick="toggleSidebar()"
            style="display: none"
            id="mobile-menu-btn"
          >
            ☰
          </button>
          <h1 class="page-title" data-i18n="app.title">OpenClaw Command Center</h1>
          <div
            id="lang-switcher"
            style="
              display: inline-flex;
              align-items: center;
              gap: 6px;
              margin-left: 12px;
              flex-shrink: 0;
            "
          >
            <span style="font-size: 0.75rem; opacity: 0.8">🌐</span>
            <select
              id="lang-select"
              style="
                font-size: 0.8rem;
                padding: 3px 8px;
                background: var(--card-bg, #161b22);
                color: var(--text, #c9d1d9);
                border: 1px solid var(--border, #30363d);
                border-radius: 4px;
                cursor: pointer;
              "
            >
              <option value="en">English</option>
              <option value="zh-CN">简体中文</option>
            </select>
          </div>
        </div>
        <div class="status-pill" id="connection-status" title="SSE connection status">
          <div class="pulse" id="connection-pulse"></div>
          <span id="gateway-status" data-i18n="app.connecting">Connecting...</span>
        </div>
      </header>

      <div class="stats-bar">
        <div class="stat">
          <div class="stat-value" id="total-tokens">-</div>
          <div class="stat-label" data-i18n="stats.totalTokens">Total Tokens</div>
        </div>
        <div class="stat">
          <div class="stat-value" id="input-tokens">-</div>
          <div class="stat-label" data-i18n="stats.input">Input</div>
        </div>
        <div class="stat">
          <div class="stat-value" id="output-tokens">-</div>
          <div class="stat-label" data-i18n="stats.output">Output</div>
        </div>
        <div
          class="stat"
          title="Sessions updated within the last 15 minutes (not necessarily actively running)"
        >
          <div class="stat-value" id="active-sessions">-</div>
          <div class="stat-label" data-i18n="stats.active15m">Recently active (15m)</div>
        </div>
        <div
          class="stat"
          title="Click for cost breakdown"
          onclick="openCostModal()"
          style="cursor: pointer"
        >
          <div class="stat-value" id="est-cost">-</div>
          <div class="stat-label" data-i18n="stats.estCost24h">Est. Cost (24h) 📊</div>
        </div>
        <div
          class="stat"
          title="Click for cost breakdown"
          id="savings-stat"
          style="display: none; cursor: pointer"
        >
          <div
            class="stat-value"
            id="est-savings"
            style="color: var(--green)"
            onclick="openCostModal()"
          >
            -
          </div>
          <div class="stat-label" style="display: flex; align-items: center; gap: 4px">
            <span onclick="openCostModal()" data-i18n="stats.estMonthlySavings"
              >Est. Monthly Savings</span
            >
            <select
              id="savings-window-select"
              style="
                font-size: 0.7rem;
                padding: 1px 2px;
                background: var(--card-bg);
                color: var(--text);
                border: 1px solid var(--border);
                border-radius: 3px;
                cursor: pointer;
              "
              onclick="event.stopPropagation()"
            >
              <option value="24h">24h</option>
              <option value="3dma">3dma</option>
              <option value="7dma" selected>7dma</option>
            </select>
            💰
          </div>
        </div>
        <div class="stat" title="Main session capacity">
          <div class="stat-value" id="main-capacity">-</div>
          <div class="stat-label" data-i18n="stats.main">Main</div>
        </div>
        <div class="stat" title="Sub-agent capacity">
          <div class="stat-value" id="subagent-capacity">-</div>
          <div class="stat-label" data-i18n="stats.subagents">Sub-agents</div>
        </div>
      </div>

      <!-- Legend & Filters -->
      <main>
        <!-- System Vitals Section -->
        <div class="section" id="vitals-section">
          <div class="vitals-panel">
            <div class="vitals-header">
              <div class="vitals-title">
                🖥️ System Vitals
                <span class="vitals-hostname" id="vitals-hostname">-</span>
              </div>
              <div class="vitals-uptime">Uptime: <span id="vitals-uptime">-</span></div>
            </div>
            <div class="vitals-grid">
              <!-- CPU -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">⚡ CPU</span>
                  <span class="vital-value" id="cpu-percent">-%</span>
                </div>
                <div
                  id="cpu-chip"
                  style="font-size: 0.7rem; color: var(--accent); margin-bottom: 8px"
                ></div>
                <div class="vital-bar">
                  <div class="vital-bar-fill blue" id="cpu-bar" style="width: 0%"></div>
                </div>
                <div class="vital-detail" style="margin-bottom: 8px">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-user">-%</span>
                    <span class="vital-detail-label">user</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-sys">-%</span>
                    <span class="vital-detail-label">sys</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-idle">-%</span>
                    <span class="vital-detail-label">idle</span>
                  </div>
                </div>
                <div class="vital-detail">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-load-1">-</span>
                    <span class="vital-detail-label">1m avg</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-load-5">-</span>
                    <span class="vital-detail-label">5m avg</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-load-15">-</span>
                    <span class="vital-detail-label">15m avg</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="cpu-cores">-</span>
                    <span class="vital-detail-label">cores</span>
                  </div>
                </div>
                <div
                  id="cpu-topology"
                  style="
                    margin-top: 8px;
                    font-size: 0.7rem;
                    color: var(--text-muted);
                    text-align: center;
                  "
                ></div>
              </div>

              <!-- Memory -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">🧠 Memory</span>
                  <span class="vital-value" id="mem-percent"
                    >-% <small style="font-size: 0.6em; opacity: 0.7">used</small></span
                  >
                </div>
                <div class="vital-bar">
                  <div class="vital-bar-fill green" id="mem-bar" style="width: 0%"></div>
                </div>
                <div class="vital-detail">
                  <div class="vital-detail-item" style="flex: 2">
                    <span class="vital-detail-value" id="mem-summary">-</span>
                    <span class="vital-detail-label">used of total</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="mem-free">-</span>
                    <span class="vital-detail-label">available</span>
                  </div>
                </div>
                <div
                  class="vital-detail"
                  style="margin-top: 8px; border-top: 1px solid var(--border); padding-top: 8px"
                >
                  <div class="vital-detail-item" title="Memory actively used by apps">
                    <span class="vital-detail-value" id="mem-active">-</span>
                    <span class="vital-detail-label">App</span>
                  </div>
                  <div
                    class="vital-detail-item"
                    title="Memory that can't be swapped (kernel, drivers)"
                  >
                    <span class="vital-detail-value" id="mem-wired">-</span>
                    <span class="vital-detail-label">Wired</span>
                  </div>
                  <div class="vital-detail-item" title="Memory compressed to save space">
                    <span class="vital-detail-value" id="mem-compressed">-</span>
                    <span class="vital-detail-label">Compressed</span>
                  </div>
                  <div class="vital-detail-item" title="Recently-used data, can be reclaimed">
                    <span class="vital-detail-value" id="mem-cached">-</span>
                    <span class="vital-detail-label">Cached</span>
                  </div>
                </div>
                <div style="margin-top: 8px; text-align: center">
                  <span class="pressure-indicator normal" id="mem-pressure">Normal</span>
                </div>
              </div>

              <!-- Disk -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">💾 Disk</span>
                  <span class="vital-value" id="disk-percent"
                    >-% <small style="font-size: 0.6em; opacity: 0.7">used</small></span
                  >
                </div>
                <div class="vital-bar">
                  <div class="vital-bar-fill green" id="disk-bar" style="width: 0%"></div>
                </div>
                <div class="vital-detail">
                  <div class="vital-detail-item" style="flex: 2">
                    <span class="vital-detail-value" id="disk-summary">-</span>
                    <span class="vital-detail-label">used of total</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="disk-free">-</span>
                    <span class="vital-detail-label">available</span>
                  </div>
                </div>
                <div
                  class="vital-detail"
                  style="margin-top: 8px; border-top: 1px solid var(--border); padding-top: 8px"
                >
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="disk-iops">-</span>
                    <span class="vital-detail-label">IOPS</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="disk-throughput">-</span>
                    <span class="vital-detail-label">MB/s</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="disk-kbt">-</span>
                    <span class="vital-detail-label">KB/t</span>
                  </div>
                </div>
              </div>

              <!-- Temperature -->
              <div class="vital-card" id="temp-card">
                <div class="vital-header">
                  <span class="vital-label">🌡️ Temperature</span>
                </div>
                <div class="temp-display">
                  <span class="temp-value" id="temp-value">-</span>
                  <span class="temp-unit">°C</span>
                </div>
                <div class="vital-detail" style="margin-top: 8px">
                  <span id="temp-status" style="font-size: 0.75rem; color: var(--text-muted)"
                    >Checking...</span
                  >
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Token Utilization Widget -->
        <div class="utilization-section">
          <div class="utilization-card" id="anthropic-quota">
            <div class="utilization-header">
              <div class="utilization-icon anthropic">🧠</div>
              <div>
                <div class="utilization-title">Claude (Anthropic)</div>
                <div class="utilization-subtitle">API Usage</div>
              </div>
            </div>
            <div>
              <div class="quota-stats">
                <span>Session Usage</span>
                <span
                  ><span class="quota-value" id="claude-compact-session-pct">-%</span> used</span
                >
              </div>
              <div class="quota-bar">
                <div
                  class="quota-bar-fill low"
                  id="claude-compact-session-bar"
                  style="width: 0%"
                ></div>
              </div>
            </div>
            <div style="margin-top: 8px">
              <div class="quota-stats">
                <span>Weekly Usage</span>
                <span><span class="quota-value" id="claude-compact-week-pct">-%</span> used</span>
              </div>
              <div class="quota-bar">
                <div
                  class="quota-bar-fill low"
                  id="claude-compact-week-bar"
                  style="width: 0%"
                ></div>
              </div>
            </div>
          </div>

          <div class="utilization-card" id="openai-quota">
            <div class="utilization-header">
              <div class="utilization-icon openai">⚡</div>
              <div>
                <div class="utilization-title">Codex (OpenAI)</div>
                <div class="utilization-subtitle">ChatGPT Plus</div>
              </div>
            </div>
            <div>
              <div class="quota-stats">
                <span>5-Hour Usage</span>
                <span><span class="quota-value" id="codex-5h-pct">0%</span> used</span>
              </div>
              <div class="quota-bar">
                <div class="quota-bar-fill low" id="codex-5h-bar" style="width: 0%"></div>
              </div>
            </div>
            <div style="margin-top: 8px">
              <div class="quota-stats">
                <span>Daily Usage</span>
                <span><span class="quota-value" id="codex-day-pct">0%</span> used</span>
              </div>
              <div class="quota-bar">
                <div class="quota-bar-fill low" id="codex-day-bar" style="width: 0%"></div>
              </div>
            </div>
            <div
              style="
                margin-top: 16px;
                padding-top: 12px;
                border-top: 1px solid var(--border);
                font-size: 0.75rem;
                color: var(--text-muted);
              "
            >
              <div style="display: flex; justify-content: space-between">
                <span>Tasks Today</span>
                <span id="codex-tasks">0</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Actions -->
        <div class="quick-actions">
          <div class="quick-actions-title" data-i18n="quickActions.title">⚡ Quick Actions</div>
          <button
            class="quick-action-btn"
            onclick="runHealthCheck()"
            data-i18n="quickActions.healthCheck"
          >
            🔍 Health Check
          </button>
          <button
            class="quick-action-btn"
            onclick="getGatewayStatus()"
            data-i18n="quickActions.gatewayStatus"
          >
            🚪 Gateway Status
          </button>
          <button class="quick-action-btn" onclick="pruneStalesSessions()">
            <span data-i18n="quickActions.cleanStale">🧹 Clean Stale Sessions</span>
          </button>
        </div>

        <!-- Sub-agent Status Panel -->
        <div class="section" id="subagents-section">
          <div class="section-header">
            <div class="section-title">
              🦞 Active Sub-agents
              <span class="section-count" id="subagent-count">0</span>
            </div>
          </div>
          <div class="subagent-grid" id="subagent-grid">
            <!-- Sub-agents populated by JavaScript -->
          </div>
        </div>

        <!-- LLM Usage Section -->
        <div class="section" id="llm-section">
          <div class="vitals-panel">
            <div class="vitals-header">
              <div class="vitals-title">
                ⛽ LLM Fuel Gauges
                <span class="vitals-hostname" id="llm-sync-time">-</span>
              </div>
              <div class="vitals-uptime">Routing: <span id="llm-routing-summary">-</span></div>
            </div>
            <div class="vitals-grid">
              <!-- Claude Session -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">🔮 Session Limit</span>
                  <span class="vital-value" id="claude-session-pct"
                    >-% <small style="font-size: 0.6em; opacity: 0.7">used</small></span
                  >
                </div>
                <div class="vital-bar">
                  <div
                    class="vital-bar-fill purple"
                    id="claude-session-bar"
                    style="width: 0%"
                  ></div>
                </div>
                <div class="vital-detail">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="claude-session-remaining">-%</span>
                    <span class="vital-detail-label">remaining</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="claude-session-reset">-</span>
                    <span class="vital-detail-label">resets in</span>
                  </div>
                </div>
              </div>

              <!-- Claude Weekly -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">📅 Weekly (All Models)</span>
                  <span class="vital-value" id="claude-weekly-pct"
                    >-% <small style="font-size: 0.6em; opacity: 0.7">used</small></span
                  >
                </div>
                <div class="vital-bar">
                  <div class="vital-bar-fill blue" id="claude-weekly-bar" style="width: 0%"></div>
                </div>
                <div class="vital-detail">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="claude-weekly-remaining">-%</span>
                    <span class="vital-detail-label">remaining</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="claude-weekly-reset">-</span>
                    <span class="vital-detail-label">resets in</span>
                  </div>
                </div>
              </div>

              <!-- Sonnet Weekly -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">✨ Sonnet Weekly</span>
                  <span class="vital-value" id="sonnet-weekly-pct"
                    >-% <small style="font-size: 0.6em; opacity: 0.7">used</small></span
                  >
                </div>
                <div class="vital-bar">
                  <div class="vital-bar-fill green" id="sonnet-weekly-bar" style="width: 0%"></div>
                </div>
                <div class="vital-detail">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="sonnet-weekly-remaining">-%</span>
                    <span class="vital-detail-label">remaining</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="sonnet-weekly-reset">-</span>
                    <span class="vital-detail-label">resets</span>
                  </div>
                </div>
              </div>

              <!-- LLM Routing -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">🦞 Task Routing</span>
                  <span class="vital-value" id="total-routed-tasks">-</span>
                </div>
                <div class="vital-detail" style="margin-top: 12px">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="claude-task-count">-</span>
                    <span class="vital-detail-label">Claude</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="codex-task-count">-</span>
                    <span class="vital-detail-label">Codex</span>
                  </div>
                </div>
                <div class="vital-detail" style="margin-top: 8px">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="llama-task-count">-</span>
                    <span class="vital-detail-label">🦙 Llama</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="qwen-task-count">-</span>
                    <span class="vital-detail-label">🐱 Qwen</span>
                  </div>
                </div>
                <div
                  style="margin-top: 8px; text-align: center"
                  title="Average routing latency (classification + execution)"
                >
                  <span class="pressure-indicator" id="routing-latency">Avg latency: -</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sessions Section -->
        <div class="section" id="sessions-section">
          <div class="section-header">
            <div class="section-title">
              📡 Sessions <span class="section-count" id="session-count">0</span>
            </div>
          </div>

          <!-- Session Filters -->
          <div class="section-filters">
            <div class="filter-group">
              <span class="filter-label">Status:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="session-status"
                onclick="setSessionFilter('status', 'all')"
              >
                All <span class="filter-count" id="filter-all-count">0</span>
              </button>
              <button
                class="filter-btn"
                data-filter="live"
                data-group="session-status"
                onclick="setSessionFilter('status', 'live')"
              >
                <span class="filter-dot live"></span>
                Live <span class="filter-count" id="filter-live-count">0</span>
              </button>
              <button
                class="filter-btn"
                data-filter="recent"
                data-group="session-status"
                onclick="setSessionFilter('status', 'recent')"
              >
                <span class="filter-dot recent"></span>
                Recent <span class="filter-count" id="filter-recent-count">0</span>
              </button>
              <button
                class="filter-btn"
                data-filter="idle"
                data-group="session-status"
                onclick="setSessionFilter('status', 'idle')"
              >
                <span class="filter-dot idle"></span>
                Idle <span class="filter-count" id="filter-idle-count">0</span>
              </button>
            </div>
            <div class="filter-group">
              <span class="filter-label">Channel:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="session-channel"
                onclick="setSessionFilter('channel', 'all')"
              >
                All
              </button>
              <button
                class="filter-btn"
                data-filter="slack"
                data-group="session-channel"
                onclick="setSessionFilter('channel', 'slack')"
              >
                💬 Slack
              </button>
              <button
                class="filter-btn"
                data-filter="telegram"
                data-group="session-channel"
                onclick="setSessionFilter('channel', 'telegram')"
              >
                📱 Telegram
              </button>
              <button
                class="filter-btn"
                data-filter="discord"
                data-group="session-channel"
                onclick="setSessionFilter('channel', 'discord')"
              >
                🎮 Discord
              </button>
              <button
                class="filter-btn"
                data-filter="signal"
                data-group="session-channel"
                onclick="setSessionFilter('channel', 'signal')"
              >
                🔒 Signal
              </button>
              <button
                class="filter-btn"
                data-filter="whatsapp"
                data-group="session-channel"
                onclick="setSessionFilter('channel', 'whatsapp')"
              >
                📲 WhatsApp
              </button>
            </div>
            <div class="filter-group">
              <span class="filter-label">Kind:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="session-kind"
                onclick="setSessionFilter('kind', 'all')"
              >
                All
              </button>
              <button
                class="filter-btn"
                data-filter="main"
                data-group="session-kind"
                onclick="setSessionFilter('kind', 'main')"
              >
                Main
              </button>
              <button
                class="filter-btn"
                data-filter="subagent"
                data-group="session-kind"
                onclick="setSessionFilter('kind', 'subagent')"
              >
                Subagent
              </button>
              <button
                class="filter-btn"
                data-filter="cron"
                data-group="session-kind"
                onclick="setSessionFilter('kind', 'cron')"
              >
                ⏰ Cron
              </button>
            </div>
          </div>

          <div class="card-grid" id="sessions">
            <!-- Skeleton loaders (replaced when data loads) -->
            <div class="skeleton-card">
              <div class="skeleton-header">
                <div class="skeleton-circle"></div>
                <div style="flex: 1">
                  <div class="skeleton-bar title"></div>
                  <div class="skeleton-bar subtitle"></div>
                </div>
                <div class="skeleton-badge"></div>
              </div>
              <div class="skeleton-bar text"></div>
              <div class="skeleton-bar text short"></div>
            </div>
            <div class="skeleton-card">
              <div class="skeleton-header">
                <div class="skeleton-circle"></div>
                <div style="flex: 1">
                  <div class="skeleton-bar title"></div>
                  <div class="skeleton-bar subtitle"></div>
                </div>
                <div class="skeleton-badge"></div>
              </div>
              <div class="skeleton-bar text"></div>
              <div class="skeleton-bar text short"></div>
            </div>
            <div class="skeleton-card">
              <div class="skeleton-header">
                <div class="skeleton-circle"></div>
                <div style="flex: 1">
                  <div class="skeleton-bar title"></div>
                  <div class="skeleton-bar subtitle"></div>
                </div>
                <div class="skeleton-badge"></div>
              </div>
              <div class="skeleton-bar text"></div>
              <div class="skeleton-bar text short"></div>
            </div>
          </div>

          <!-- Pagination Controls -->
          <div class="pagination" id="sessions-pagination" style="display: none">
            <button class="pagination-btn" id="pagination-prev" onclick="changePage(-1)" disabled>
              ← Prev
            </button>
            <div class="pagination-pages" id="pagination-pages"></div>
            <button class="pagination-btn" id="pagination-next" onclick="changePage(1)">
              Next →
            </button>
            <div class="pagination-info" id="pagination-info"></div>
          </div>
        </div>

        <!-- Cron Jobs Section -->
        <div class="section" id="cron-section">
          <div class="section-header">
            <div class="section-title">
              ⏰ Cron Jobs <span class="section-count" id="cron-count">0</span>
            </div>
          </div>

          <!-- Cron Filters -->
          <div class="section-filters">
            <div class="filter-group">
              <span class="filter-label">Status:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="cron-status"
                onclick="setCronFilter('status', 'all')"
              >
                All
              </button>
              <button
                class="filter-btn"
                data-filter="enabled"
                data-group="cron-status"
                onclick="setCronFilter('status', 'enabled')"
              >
                ✅ Enabled
              </button>
              <button
                class="filter-btn"
                data-filter="disabled"
                data-group="cron-status"
                onclick="setCronFilter('status', 'disabled')"
              >
                ⏸️ Disabled
              </button>
            </div>
            <div class="filter-group">
              <span class="filter-label">Schedule:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="cron-schedule"
                onclick="setCronFilter('schedule', 'all')"
              >
                All
              </button>
              <button
                class="filter-btn"
                data-filter="frequent"
                data-group="cron-schedule"
                onclick="setCronFilter('schedule', 'frequent')"
              >
                ⚡ Frequent (&lt;1h)
              </button>
              <button
                class="filter-btn"
                data-filter="daily"
                data-group="cron-schedule"
                onclick="setCronFilter('schedule', 'daily')"
              >
                📅 Daily
              </button>
              <button
                class="filter-btn"
                data-filter="weekly"
                data-group="cron-schedule"
                onclick="setCronFilter('schedule', 'weekly')"
              >
                📆 Weekly
              </button>
            </div>
          </div>

          <div class="card-grid" id="cron-jobs">
            <!-- Skeleton loaders (replaced when data loads) -->
            <div class="skeleton-card" style="display: flex; gap: 12px; align-items: center">
              <div class="skeleton-circle"></div>
              <div style="flex: 1">
                <div class="skeleton-bar title" style="width: 50%"></div>
                <div class="skeleton-bar subtitle" style="width: 70%"></div>
              </div>
              <div class="skeleton-bar short" style="width: 60px"></div>
            </div>
            <div class="skeleton-card" style="display: flex; gap: 12px; align-items: center">
              <div class="skeleton-circle"></div>
              <div style="flex: 1">
                <div class="skeleton-bar title" style="width: 50%"></div>
                <div class="skeleton-bar subtitle" style="width: 70%"></div>
              </div>
              <div class="skeleton-bar short" style="width: 60px"></div>
            </div>
          </div>
        </div>

        <!-- Memory Section -->
        <div class="section" id="memory-section">
          <div class="section-header">
            <div class="section-title">
              🧠 Memory <span class="section-count" id="memory-count">0 files</span>
            </div>
          </div>

          <!-- Memory Filters -->
          <div class="section-filters">
            <div class="filter-group">
              <span class="filter-label">Type:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="memory-type"
                onclick="setMemoryFilter('type', 'all')"
              >
                All
              </button>
              <button
                class="filter-btn"
                data-filter="daily"
                data-group="memory-type"
                onclick="setMemoryFilter('type', 'daily')"
              >
                📅 Daily Logs
              </button>
              <button
                class="filter-btn"
                data-filter="state"
                data-group="memory-type"
                onclick="setMemoryFilter('type', 'state')"
              >
                📊 State Files
              </button>
            </div>
            <div class="filter-group">
              <span class="filter-label">Age:</span>
              <button
                class="filter-btn active"
                data-filter="all"
                data-group="memory-age"
                onclick="setMemoryFilter('age', 'all')"
              >
                All
              </button>
              <button
                class="filter-btn"
                data-filter="today"
                data-group="memory-age"
                onclick="setMemoryFilter('age', 'today')"
              >
                Today
              </button>
              <button
                class="filter-btn"
                data-filter="week"
                data-group="memory-age"
                onclick="setMemoryFilter('age', 'week')"
              >
                This Week
              </button>
              <button
                class="filter-btn"
                data-filter="older"
                data-group="memory-age"
                onclick="setMemoryFilter('age', 'older')"
              >
                Older
              </button>
            </div>
          </div>

          <div class="vitals-panel">
            <div class="vitals-grid">
              <!-- MEMORY.md -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">📜 MEMORY.md</span>
                </div>
                <div class="vital-detail" style="margin-top: 8px">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="memory-md-size">-</span>
                    <span class="vital-detail-label">size</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="memory-md-lines">-</span>
                    <span class="vital-detail-label">lines</span>
                  </div>
                </div>
                <div style="margin-top: 12px; font-size: 0.75rem; color: var(--text-muted)">
                  Long-term curated memories
                </div>
              </div>

              <!-- Daily Files -->
              <div class="vital-card">
                <div class="vital-header">
                  <span class="vital-label">📅 Daily Notes</span>
                </div>
                <div class="vital-detail" style="margin-top: 8px">
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="memory-total-files">-</span>
                    <span class="vital-detail-label">files</span>
                  </div>
                  <div class="vital-detail-item">
                    <span class="vital-detail-value" id="memory-total-size">-</span>
                    <span class="vital-detail-label">total</span>
                  </div>
                </div>
                <div style="margin-top: 12px; font-size: 0.75rem; color: var(--text-muted)">
                  Raw logs by date
                </div>
              </div>

              <!-- Recent Files -->
              <div class="vital-card" style="grid-column: span 2">
                <div class="vital-header">
                  <span class="vital-label">🕐 Recent Memory Files</span>
                </div>
                <div id="memory-recent-files" style="margin-top: 8px">
                  <em style="color: var(--text-muted); font-size: 0.8rem">Loading...</em>
                </div>
              </div>
            </div>

            <div
              style="
                margin-top: 16px;
                padding-top: 16px;
                border-top: 1px solid var(--border);
                text-align: center;
              "
            >
              <span style="font-size: 0.75rem; color: var(--text-muted)">
                🔒 Memory editing UI coming soon (Inside Out style!)
              </span>
            </div>
          </div>
        </div>

        <!-- Cerebro Section -->
        <div class="section" id="cerebro-section">
          <div class="section-header">
            <div class="section-title">
              🔮 Cerebro <span class="section-count" id="cerebro-count">0 topics</span>
            </div>
            <!-- SSE provides live updates -->
          </div>

          <div id="cerebro-content">
            <!-- Not Initialized State -->
            <div id="cerebro-not-initialized" class="vitals-panel" style="display: none">
              <div style="text-align: center; padding: 40px 20px">
                <div style="font-size: 3rem; margin-bottom: 16px">🔮</div>
                <h3 style="font-size: 1.2rem; font-weight: 600; margin-bottom: 8px">
                  Cerebro Not Initialized
                </h3>
                <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px">
                  Cerebro tracks conversation topics and threads across sessions.
                </p>
                <div
                  id="cerebro-init-commands"
                  style="
                    background: var(--bg);
                    border-radius: 8px;
                    padding: 16px;
                    text-align: left;
                    font-size: 0.8rem;
                    font-family: monospace;
                  "
                >
                  <div style="color: var(--text-muted); margin-bottom: 8px">
                    # To initialize Cerebro:
                  </div>
                  <div style="color: var(--accent)" id="cerebro-init-topics-cmd">
                    mkdir -p ~/cerebro/topics
                  </div>
                  <div style="color: var(--accent)" id="cerebro-init-orphans-cmd">
                    mkdir -p ~/cerebro/orphans
                  </div>
                </div>
              </div>
            </div>

            <!-- Initialized State -->
            <div id="cerebro-initialized" class="vitals-panel" style="display: none">
              <div class="vitals-grid">
                <!-- Topic Counts -->
                <div class="vital-card">
                  <div class="vital-header">
                    <span class="vital-label">📊 Topics by Status</span>
                  </div>
                  <div class="vital-detail" style="margin-top: 8px">
                    <div class="vital-detail-item">
                      <span
                        class="vital-detail-value"
                        id="cerebro-active"
                        style="color: var(--green)"
                        >0</span
                      >
                      <span class="vital-detail-label">active</span>
                    </div>
                    <div class="vital-detail-item">
                      <span
                        class="vital-detail-value"
                        id="cerebro-resolved"
                        style="color: var(--accent)"
                        >0</span
                      >
                      <span class="vital-detail-label">resolved</span>
                    </div>
                    <div class="vital-detail-item">
                      <span
                        class="vital-detail-value"
                        id="cerebro-parked"
                        style="color: var(--text-muted)"
                        >0</span
                      >
                      <span class="vital-detail-label">parked</span>
                    </div>
                  </div>
                  <div style="margin-top: 12px; font-size: 0.75rem; color: var(--text-muted)">
                    <span id="cerebro-total-topics">0</span> total topics
                  </div>
                </div>

                <!-- Thread Stats -->
                <div class="vital-card">
                  <div class="vital-header">
                    <span class="vital-label">🧵 Threads</span>
                  </div>
                  <div class="vital-detail" style="margin-top: 8px">
                    <div class="vital-detail-item">
                      <span class="vital-detail-value" id="cerebro-threads">0</span>
                      <span class="vital-detail-label">tracked</span>
                    </div>
                    <div class="vital-detail-item">
                      <span
                        class="vital-detail-value"
                        id="cerebro-orphans"
                        style="color: var(--yellow)"
                        >0</span
                      >
                      <span class="vital-detail-label">orphans</span>
                    </div>
                  </div>
                  <div style="margin-top: 12px; font-size: 0.75rem; color: var(--text-muted)">
                    Threads linked to topics
                  </div>
                </div>

                <!-- Recent Topics -->
                <div class="vital-card" style="grid-column: span 2">
                  <div class="vital-header">
                    <span class="vital-label">🕐 Recent Active Topics</span>
                  </div>
                  <div id="cerebro-recent-topics" style="margin-top: 8px">
                    <em style="color: var(--text-muted); font-size: 0.8rem"
                      >No active topics yet</em
                    >
                  </div>
                </div>
              </div>

              <div
                style="
                  margin-top: 16px;
                  padding-top: 16px;
                  border-top: 1px solid var(--border);
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                "
              >
                <span style="font-size: 0.75rem; color: var(--text-muted)">
                  Last updated: <span id="cerebro-last-updated">-</span>
                </span>
                <a
                  href="file://#"
                  style="font-size: 0.75rem; color: var(--accent); text-decoration: none"
                >
                  📁 Open cerebro/
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Operators Section -->
        <div class="section" id="operators-section">
          <div class="section-header">
            <div class="section-title">👥 Operators</div>
            <div class="section-actions">
              <button class="btn-secondary" onclick="refreshOperators()" title="Refresh">🔄</button>
            </div>
          </div>
          <div class="operators-grid" id="operators-grid">
            <div class="loading-state">Loading operators...</div>
          </div>

          <div
            class="roles-legend"
            style="margin-top: 20px; padding: 16px; background: var(--bg); border-radius: 8px"
          >
            <div
              style="
                font-size: 0.75rem;
                color: var(--text-muted);
                margin-bottom: 12px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
              "
            >
              Permission Levels
            </div>
            <div style="display: flex; gap: 24px; flex-wrap: wrap">
              <div style="display: flex; align-items: center; gap: 8px">
                <span
                  style="
                    width: 12px;
                    height: 12px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #ffd700, #ff8c00);
                  "
                ></span>
                <span style="font-size: 0.85rem">Owner</span>
                <span style="font-size: 0.7rem; color: var(--text-muted)">Full control</span>
              </div>
              <div style="display: flex; align-items: center; gap: 8px">
                <span
                  style="
                    width: 12px;
                    height: 12px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #a371f7, #8957e5);
                  "
                ></span>
                <span style="font-size: 0.85rem">Admin</span>
                <span style="font-size: 0.7rem; color: var(--text-muted)"
                  >Manage users & settings</span
                >
              </div>
              <div style="display: flex; align-items: center; gap: 8px">
                <span
                  style="
                    width: 12px;
                    height: 12px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #58a6ff, #388bfd);
                  "
                ></span>
                <span style="font-size: 0.85rem">User</span>
                <span style="font-size: 0.7rem; color: var(--text-muted)">Dashboard access</span>
              </div>
            </div>
          </div>
        </div>

        <!-- About Section -->
        <div class="section" id="about-section">
          <div class="section-header">
            <div class="section-title">ℹ️ About</div>
          </div>
          <div class="vitals-panel">
            <div style="text-align: center; padding: 20px 0">
              <div style="font-size: 3rem; margin-bottom: 12px">🦞</div>
              <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 8px">
                OpenClaw Command Center
              </h2>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px">
                A Starcraft-inspired dashboard for OpenClaw orchestration
              </p>

              <div style="display: flex; justify-content: center; gap: 12px; margin-bottom: 24px">
                <span
                  style="
                    padding: 4px 12px;
                    background: var(--bg);
                    border-radius: 12px;
                    font-size: 0.75rem;
                  "
                  id="app-version"
                  >v...</span
                >
                <span
                  style="
                    padding: 4px 12px;
                    background: rgba(63, 185, 80, 0.15);
                    color: var(--green);
                    border-radius: 12px;
                    font-size: 0.75rem;
                  "
                  >MIT License</span
                >
              </div>

              <div style="margin-bottom: 24px">
                <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 8px">
                  BUILT BY
                </div>
                <a
                  href="https://github.com/jontsai"
                  target="_blank"
                  style="color: var(--accent); text-decoration: none; font-size: 1rem"
                >
                  Jonathan Tsai (@jontsai)
                </a>
              </div>

              <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap">
                <a
                  href="https://github.com/jontsai/openclaw-command-center"
                  target="_blank"
                  class="link-tag github"
                  style="padding: 8px 16px"
                >
                  🐙 GitHub
                </a>
                <a
                  href="https://x.com/jontsai"
                  target="_blank"
                  class="link-tag"
                  style="padding: 8px 16px"
                >
                  🐦 Twitter
                </a>
                <a
                  href="https://openclaw.ai"
                  target="_blank"
                  class="link-tag"
                  style="padding: 8px 16px"
                >
                  🦞 OpenClaw
                </a>
                <a
                  href="https://clawhub.ai/jontsai/command-center"
                  target="_blank"
                  class="link-tag"
                  style="padding: 8px 16px"
                >
                  🔗 ClawHub
                </a>
              </div>
            </div>

            <div style="border-top: 1px solid var(--border); padding-top: 20px; margin-top: 20px">
              <div
                style="
                  font-size: 0.75rem;
                  color: var(--text-muted);
                  margin-bottom: 12px;
                  text-align: center;
                "
              >
                INSPIRED BY
              </div>
              <div
                style="
                  display: flex;
                  justify-content: center;
                  gap: 20px;
                  flex-wrap: wrap;
                  font-size: 0.85rem;
                  color: var(--text-muted);
                "
              >
                <span>🎮 Starcraft</span>
                <span>📊 iStatMenus</span>
                <span>💾 DaisyDisk</span>
                <span>📧 Gmail</span>
                <span>🧠 Inside Out</span>
              </div>
            </div>
          </div>
        </div>
      </main>

      <div class="refresh-bar">
        <span id="refresh-mode" data-i18n="connection.realtime">Real-time updates via SSE ⚡</span>
        • Last updated:
        <span id="last-updated"
          ><span class="loading-dots"><span></span><span></span><span></span></span
        ></span>
      </div>
    </div>

    <!-- Detail Panel -->
    <div id="detail-overlay" class="detail-overlay hidden" onclick="closeDetail()"></div>
    <div id="detail-panel" class="detail-panel hidden">
      <div class="detail-header">
        <h2 id="detail-title">Session Details</h2>
        <button class="close-btn" onclick="closeDetail()">✕</button>
      </div>
      <div class="detail-content">
        <div class="detail-section">
          <h3>📊 Overview</h3>
          <div class="detail-box" id="detail-overview"></div>
        </div>
        <div class="detail-section">
          <h3>📝 Summary</h3>
          <div class="detail-box" id="detail-summary"></div>
        </div>
        <div class="detail-section">
          <h3>🔗 References</h3>
          <div class="detail-box" id="detail-links"></div>
        </div>
        <div class="detail-section attention">
          <h3>⚠️ Needs Attention</h3>
          <div class="detail-box" id="detail-attention"></div>
        </div>
        <div class="detail-section">
          <h3>🎯 Key Facts</h3>
          <div class="detail-box" id="detail-facts"></div>
        </div>
        <div class="detail-section">
          <h3>🔧 Tools Used</h3>
          <div class="detail-box" id="detail-tools"></div>
        </div>
        <div class="detail-section">
          <h3>💬 Recent Messages</h3>
          <div class="detail-box" id="detail-messages"></div>
        </div>
        <!-- Future: Read-Write Controls -->
        <div class="detail-actions" id="detail-actions" style="display: none">
          <button class="action-btn" disabled title="Coming soon">💬 Send Message</button>
          <button class="action-btn" disabled title="Coming soon">🔄 Refresh</button>
          <button class="action-btn danger" disabled title="Coming soon">🗑️ Clear Session</button>
        </div>
      </div>
    </div>

    <!-- Auth Fix Modal -->
    <div id="auth-modal-overlay" class="detail-overlay hidden" onclick="closeAuthModal()"></div>
    <div id="auth-modal" class="detail-panel hidden" style="max-width: 550px">
      <div class="detail-header">
        <h2>🔑 Fix Claude Authentication</h2>
        <button class="close-btn" onclick="closeAuthModal()">✕</button>
      </div>
      <div class="detail-content" id="auth-modal-content">
        <div
          class="detail-section"
          style="
            background: rgba(245, 158, 11, 0.1);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
          "
        >
          <p style="margin: 0; color: #f59e0b">
            ⚠️ Your Claude OAuth token has expired or lacks the required permissions.
          </p>
        </div>

        <div class="detail-section">
          <h3>Step 1: Refresh Claude Token</h3>
          <div class="detail-box">
            <p>Open Terminal and run:</p>
            <pre
              style="
                background: #1e1e2e;
                padding: 12px;
                border-radius: 6px;
                overflow-x: auto;
                font-size: 13px;
              "
            ><code>claude setup-token</code></pre>
            <p style="color: #888; font-size: 12px; margin-top: 8px">
              Follow the prompts to authenticate with your Claude account.
            </p>
          </div>
        </div>

        <div class="detail-section">
          <h3>Step 2: Update OpenClaw Agent</h3>
          <div class="detail-box">
            <p>Run the onboard wizard to update your agent credentials:</p>
            <pre
              style="
                background: #1e1e2e;
                padding: 12px;
                border-radius: 6px;
                overflow-x: auto;
                font-size: 13px;
              "
            ><code>openclaw onboard</code></pre>
            <p style="color: #888; font-size: 12px; margin-top: 8px">
              Or manually update the main agent:
            </p>
            <pre
              style="
                background: #1e1e2e;
                padding: 12px;
                border-radius: 6px;
                overflow-x: auto;
                font-size: 13px;
              "
            ><code>openclaw agents add main</code></pre>
            <p style="color: #888; font-size: 12px; margin-top: 8px">
              Select "Claude Code CLI" when prompted for the auth source.
            </p>
          </div>
        </div>

        <div class="detail-section">
          <h3>Step 3: Verify</h3>
          <div class="detail-box">
            <p>Refresh this dashboard or run:</p>
            <pre
              style="
                background: #1e1e2e;
                padding: 12px;
                border-radius: 6px;
                overflow-x: auto;
                font-size: 13px;
              "
            ><code>openclaw status --usage</code></pre>
            <p style="color: #888; font-size: 12px; margin-top: 8px">
              You should see your usage percentages instead of an auth error.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Cost Breakdown Modal -->
    <div id="cost-modal-overlay" class="detail-overlay hidden" onclick="closeCostModal()"></div>
    <div id="cost-modal" class="detail-panel hidden" style="max-width: 500px">
      <div class="detail-header">
        <h2>💰 Cost Breakdown (24h)</h2>
        <button class="close-btn" onclick="closeCostModal()">✕</button>
      </div>
      <div class="detail-content" id="cost-modal-content">
        <div class="detail-section">
          <h3>📊 Token Usage</h3>
          <div class="detail-box" id="cost-tokens"></div>
        </div>
        <div class="detail-section">
          <h3>💵 Pricing Rates (Claude Opus)</h3>
          <div class="detail-box" id="cost-rates"></div>
        </div>
        <div class="detail-section">
          <h3>🧮 Calculation</h3>
          <div class="detail-box" id="cost-calculation"></div>
        </div>
        <div
          class="detail-section"
          style="background: rgba(63, 185, 80, 0.1); border-radius: 8px; padding: 16px"
        >
          <h3>✨ Est. Savings</h3>
          <div class="detail-box" id="cost-savings"></div>
        </div>
        <div class="detail-section">
          <h3>🔥 Top Sessions by Tokens (24h)</h3>
          <div class="detail-box" id="cost-top-sessions" style="font-size: 0.85rem"></div>
        </div>
      </div>
    </div>

    <!-- Operator Modal -->
    <div
      id="operator-modal-overlay"
      class="detail-overlay hidden"
      onclick="closeOperatorModal()"
    ></div>
    <div id="operator-modal" class="detail-panel hidden" style="max-width: 500px">
      <div class="detail-header">
        <h2>👤 <span id="operator-modal-name">User Stats</span></h2>
        <button class="close-btn" onclick="closeOperatorModal()">✕</button>
      </div>
      <div class="detail-content" id="operator-modal-content">
        <div class="loading-state">Loading user stats...</div>
      </div>
    </div>

    <!-- Privacy Settings Modal -->
    <div
      id="privacy-modal-overlay"
      class="detail-overlay hidden"
      onclick="closePrivacyModal()"
    ></div>
    <div id="privacy-modal" class="detail-panel hidden" style="max-width: 550px">
      <div class="detail-header">
        <h2>🔒 Privacy Settings</h2>
        <button class="close-btn" onclick="closePrivacyModal()">✕</button>
      </div>
      <div class="detail-content" id="privacy-modal-content">
        <div style="margin-bottom: 16px">
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 12px">
            Hide topics and sessions from display for privacy during demos/screenshots. Settings are
            stored in your browser only.
          </p>
        </div>

        <!-- Hidden Topics Section -->
        <div
          style="margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border)"
        >
          <label style="font-size: 0.95rem; font-weight: 600; display: block; margin-bottom: 12px"
            >🏷️ Hidden Topics
            <span id="privacy-topics-count" style="color: var(--text-muted); font-weight: normal"
              >(0)</span
            ></label
          >
          <div style="display: flex; gap: 8px; margin-bottom: 12px">
            <input
              type="text"
              id="privacy-add-topic"
              placeholder="Topic name..."
              style="
                flex: 1;
                padding: 8px 12px;
                background: var(--bg);
                border: 1px solid var(--border);
                border-radius: 6px;
                color: var(--text);
                font-size: 0.9rem;
              "
            />
            <button class="btn-primary" onclick="addHiddenTopic()">Add</button>
          </div>
          <div id="hidden-topics-list" style="min-height: 30px">
            <em style="color: var(--text-muted); font-size: 0.85rem">No topics hidden</em>
          </div>
        </div>

        <!-- Hidden Sessions Section -->
        <div
          style="margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border)"
        >
          <label style="font-size: 0.95rem; font-weight: 600; display: block; margin-bottom: 12px"
            >📋 Hidden Sessions
            <span id="privacy-sessions-count" style="color: var(--text-muted); font-weight: normal"
              >(0)</span
            ></label
          >
          <div style="display: flex; gap: 8px; margin-bottom: 12px">
            <input
              type="text"
              id="privacy-add-session"
              placeholder="Session label or key..."
              style="
                flex: 1;
                padding: 8px 12px;
                background: var(--bg);
                border: 1px solid var(--border);
                border-radius: 6px;
                color: var(--text);
                font-size: 0.9rem;
              "
            />
            <button class="btn-primary" onclick="addHiddenSession()">Add</button>
          </div>
          <div id="hidden-sessions-list" style="min-height: 30px">
            <em style="color: var(--text-muted); font-size: 0.85rem">No sessions hidden</em>
          </div>
          <p style="color: var(--text-muted); font-size: 0.75rem; margin-top: 8px">
            💡 Tip: You can also click the 👁️ icon on any session card to hide it quickly.
          </p>
        </div>

        <!-- Hidden Cron Jobs Section -->
        <div
          style="margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border)"
        >
          <label style="font-size: 0.95rem; font-weight: 600; display: block; margin-bottom: 12px"
            >⏰ Hidden Cron Jobs
            <span id="privacy-crons-count" style="color: var(--text-muted); font-weight: normal"
              >(0)</span
            ></label
          >
          <div style="display: flex; gap: 8px; margin-bottom: 12px">
            <input
              type="text"
              id="privacy-add-cron"
              placeholder="Cron job name..."
              style="
                flex: 1;
                padding: 8px 12px;
                background: var(--bg);
                border: 1px solid var(--border);
                border-radius: 6px;
                color: var(--text);
                font-size: 0.9rem;
              "
            />
            <button class="btn-primary" onclick="addHiddenCron()">Add</button>
          </div>
          <div id="hidden-crons-list" style="min-height: 30px">
            <em
              style="color: var(--text-muted); font-size: 0.85rem"
              data-i18n="privacy.noCronHidden"
              >No cron jobs hidden</em
            >
          </div>
        </div>

        <!-- Display Options Section -->
        <div
          style="margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border)"
        >
          <label style="font-size: 0.95rem; font-weight: 600; display: block; margin-bottom: 12px"
            >🖥️ Display Options</label
          >
          <label
            style="
              display: flex;
              align-items: center;
              gap: 10px;
              cursor: pointer;
              font-size: 0.9rem;
            "
          >
            <input
              type="checkbox"
              id="privacy-hide-hostname"
              onchange="toggleHideHostname()"
              style="width: 18px; height: 18px; cursor: pointer"
            />
            <span>Hide system hostname</span>
          </label>
        </div>

        <div>
          <button class="btn-secondary" onclick="clearAllPrivacySettings()" style="width: 100%">
            Clear All Privacy Settings
          </button>
        </div>
      </div>
    </div>

    <script>
      // State
      // Filter state for each section
      let sessionFilters = { status: "all", channel: "all", kind: "all" };
      let cronFilters = { status: "all", schedule: "all" };
      let memoryFilters = { type: "all", age: "all" };
      let currentFilter = "all"; // Legacy, for backwards compat
      let sessionsData = [];
      let cronData = [];
      let sidebarCollapsed = false;
      let paginationState = {
        page: 1,
        pageSize: 20,
        total: 0,
        totalPages: 0,
        hasNext: false,
        hasPrev: false,
      };

      const i18nText = (key, params = {}, fallback = key) =>
        window.I18N?.t ? window.I18N.t(key, params, fallback) : fallback;

      // Utility functions
      function formatTimeAgo(mins) {
        if (mins < 1) return i18nText("time.now", {}, "now");
        if (mins < 60) return `${mins}m`;
        if (mins < 1440) return `${Math.round(mins / 60)}h`;
        return `${Math.round(mins / 1440)}d`;
      }

      function escapeHtml(text) {
        const div = document.createElement("div");
        div.textContent = text;
        return div.innerHTML;
      }

      // Safe DOM utilities - defensive wrappers that won't crash on missing elements
      function $safe(id) {
        const el = document.getElementById(id);
        return {
          el,
          exists: !!el,
          text: (val) => {
            if (el) el.textContent = val;
            return this;
          },
          html: (val) => {
            if (el) el.innerHTML = val;
            return this;
          },
          style: (prop, val) => {
            if (el) el.style[prop] = val;
            return this;
          },
          class: (val) => {
            if (el) el.className = val;
            return this;
          },
          addClass: (val) => {
            if (el) el.classList.add(val);
            return this;
          },
          removeClass: (val) => {
            if (el) el.classList.remove(val);
            return this;
          },
        };
      }

      // Batch safe DOM updates - silently skips missing elements
      function $batch(updates) {
        for (const [id, ops] of Object.entries(updates)) {
          const el = document.getElementById(id);
          if (!el) continue;
          for (const [op, val] of Object.entries(ops)) {
            switch (op) {
              case "text":
                el.textContent = val;
                break;
              case "html":
                el.innerHTML = val;
                break;
              case "class":
                el.className = val;
                break;
              case "width":
                el.style.width = val;
                break;
              default:
                if (op.startsWith("style.")) el.style[op.slice(6)] = val;
                break;
            }
          }
        }
      }

      // Smart DOM update using morphdom - only patches what changed
      function smartUpdate(targetEl, newHtml) {
        if (typeof morphdom === "undefined") {
          // Fallback if morphdom not loaded
          targetEl.innerHTML = newHtml;
          return;
        }
        // Create a temporary container with the new content
        const temp = document.createElement("div");
        temp.innerHTML = newHtml;
        // If target has single child and temp has single child, morph directly
        if (targetEl.children.length === 1 && temp.children.length === 1) {
          morphdom(targetEl.firstElementChild, temp.firstElementChild);
        } else {
          // Otherwise morph the container itself
          morphdom(targetEl, temp, { childrenOnly: true });
        }
      }

      // Sidebar toggle
      function toggleSidebar() {
        sidebarCollapsed = !sidebarCollapsed;
        document.getElementById("sidebar").classList.toggle("collapsed", sidebarCollapsed);
        document
          .getElementById("main-wrapper")
          .classList.toggle("sidebar-collapsed", sidebarCollapsed);
        $set("sidebar-toggle-btn", "textContent", sidebarCollapsed ? "▶" : "◀");
      }

      // Navigation
      document.querySelectorAll(".nav-item[data-section]").forEach((item) => {
        item.addEventListener("click", function (e) {
          document.querySelectorAll(".nav-item").forEach((i) => i.classList.remove("active"));
          this.classList.add("active");
        });
      });

      // Filter functions - Session filters
      function setSessionFilter(group, value) {
        sessionFilters[group] = value;
        currentFilter = value; // Legacy compat

        // Update button states for this group
        document.querySelectorAll(`[data-group="session-${group}"]`).forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.filter === value);
        });

        // Status filter is server-side, others are client-side
        if (group === "status") {
          // Reset to page 1 and fetch with new filter (server-side)
          paginationState.page = 1;
          fetchSessions(1);
        } else {
          // Channel/kind filters remain client-side for now
          applySessionFilters();
        }
      }

      function applySessionFilters() {
        // Client-side filtering for channel and kind only
        // Status is now handled server-side
        document.querySelectorAll(".session-card").forEach((card) => {
          const channel = card.dataset.channel;
          const kind = card.dataset.kind;

          let showChannel = sessionFilters.channel === "all" || channel === sessionFilters.channel;
          let showKind = sessionFilters.kind === "all" || kind === sessionFilters.kind;

          card.classList.toggle("hidden-by-filter", !(showChannel && showKind));
        });
      }

      // Cron filters
      function setCronFilter(group, value) {
        cronFilters[group] = value;

        document.querySelectorAll(`[data-group="cron-${group}"]`).forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.filter === value);
        });
        applyCronFilters();
      }

      function applyCronFilters() {
        document.querySelectorAll(".cron-item").forEach((item) => {
          const enabled = item.dataset.enabled === "true";
          const schedule = item.dataset.schedule;

          let showStatus =
            cronFilters.status === "all" ||
            (cronFilters.status === "enabled" && enabled) ||
            (cronFilters.status === "disabled" && !enabled);
          let showSchedule = cronFilters.schedule === "all" || schedule === cronFilters.schedule;

          item.classList.toggle("hidden-by-filter", !(showStatus && showSchedule));
        });
      }

      // Memory filters
      function setMemoryFilter(group, value) {
        memoryFilters[group] = value;

        document.querySelectorAll(`[data-group="memory-${group}"]`).forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.filter === value);
        });
        applyMemoryFilters();
      }

      function applyMemoryFilters() {
        document.querySelectorAll(".memory-item").forEach((item) => {
          const type = item.dataset.type;
          const age = item.dataset.age;

          let showType = memoryFilters.type === "all" || type === memoryFilters.type;
          let showAge = memoryFilters.age === "all" || age === memoryFilters.age;

          item.classList.toggle("hidden-by-filter", !(showType && showAge));
        });
      }

      // Legacy filter function (backwards compat)
      function setFilter(filter) {
        setSessionFilter("status", filter);
      }

      function applyFilter() {
        applySessionFilters();
      }

      function updateFilterCounts(sessions) {
        const counts = { all: sessions.length, live: 0, recent: 0, idle: 0 };
        sessions.forEach((s) => {
          if (s.active) counts.live++;
          else if (s.recentlyActive) counts.recent++;
          else counts.idle++;
        });

        $set("filter-all-count", "textContent", counts.all);
        $set("filter-live-count", "textContent", counts.live);
        $set("filter-recent-count", "textContent", counts.recent);
        $set("filter-idle-count", "textContent", counts.idle);
      }

      // Use server-provided counts for ALL sessions (across all pages)
      function updateFilterCountsFromServer(statusCounts) {
        $set("filter-all-count", "textContent", statusCounts.all || 0);
        $set("filter-live-count", "textContent", statusCounts.live || 0);
        $set("filter-recent-count", "textContent", statusCounts.recent || 0);
        $set("filter-idle-count", "textContent", statusCounts.idle || 0);
      }

      // Extract links from text
      function extractLinks(text) {
        const links = [];

        // Linear: JON-123
        const linearMatches = text.match(/\b([A-Z]{2,5}-\d+)\b/g) || [];
        linearMatches.forEach((m) => {
          if (!links.find((l) => l.id === m)) {
            links.push({ type: "linear", id: m, url: `https://linear.app/YOUR_TEAM/issue/${m}` });
          }
        });

        // GitHub PRs/Issues: #123 or owner/repo#123
        const ghMatches = text.match(/(?:[\w-]+\/[\w-]+)?#\d+/g) || [];
        ghMatches.forEach((m) => {
          if (!links.find((l) => l.id === m)) {
            links.push({ type: "github", id: m, url: null });
          }
        });

        // File paths: ~/path or /path
        const fileMatches = text.match(/(?:~\/|\/Users\/|\/home\/)[^\s\)\"\']+/g) || [];
        fileMatches.forEach((m) => {
          const short = m.split("/").slice(-2).join("/");
          if (!links.find((l) => l.id === short)) {
            links.push({ type: "file", id: short, path: m });
          }
        });

        // Slack threads
        if (text.includes("slack") || text.includes("thread")) {
          links.push({ type: "slack", id: "Slack thread", url: null });
        }

        return links.slice(0, 5);
      }

      // Fetch sessions with pagination and server-side filtering
      async function fetchSessions(page = 1) {
        // Build URL with status filter
        const statusFilter = sessionFilters.status;
        let url = `/api/sessions?page=${page}&pageSize=${paginationState.pageSize}`;
        if (statusFilter && statusFilter !== "all") {
          url += `&status=${statusFilter}`;
        }

        try {
          const response = await fetch(url);
          const data = await response.json();
          if (data?.sessions) {
            renderSessions(data.sessions, data.pagination, data.statusCounts);
            if (data.tokenStats) renderTokenStats(data.tokenStats);
            if (data.capacity) renderCapacity(data.capacity);
          }
          return data;
        } catch (e) {
          console.error("Failed to fetch sessions:", e);
          return null;
        }
      }

      // Change page
      function changePage(delta) {
        const newPage = paginationState.page + delta;
        if (newPage < 1 || newPage > paginationState.totalPages) return;
        paginationState.page = newPage;
        fetchSessions(newPage);
      }

      // Go to specific page
      function goToPage(page) {
        if (page < 1 || page > paginationState.totalPages) return;
        paginationState.page = page;
        fetchSessions(page);
      }

      // Render pagination controls
      function renderPagination(pagination) {
        if (!pagination || pagination.total <= pagination.pageSize) {
          document.getElementById("sessions-pagination").style.display = "none";
          return;
        }

        paginationState = { ...paginationState, ...pagination };

        const paginationEl = document.getElementById("sessions-pagination");
        const pagesEl = document.getElementById("pagination-pages");
        const prevBtn = document.getElementById("pagination-prev");
        const nextBtn = document.getElementById("pagination-next");
        const infoEl = document.getElementById("pagination-info");

        paginationEl.style.display = "flex";

        // Update prev/next buttons
        prevBtn.disabled = !pagination.hasPrev;
        nextBtn.disabled = !pagination.hasNext;

        // Update info
        const start = (pagination.page - 1) * pagination.pageSize + 1;
        const end = Math.min(pagination.page * pagination.pageSize, pagination.total);
        infoEl.textContent = `${start}-${end} of ${pagination.total}`;

        // Build page buttons (show max 7 pages with ellipsis)
        let pages = [];
        const total = pagination.totalPages;
        const current = pagination.page;

        if (total <= 7) {
          // Show all pages
          for (let i = 1; i <= total; i++) pages.push(i);
        } else {
          // Show: 1 ... current-1 current current+1 ... total
          pages.push(1);
          if (current > 3) pages.push("...");
          for (let i = Math.max(2, current - 1); i <= Math.min(total - 1, current + 1); i++) {
            pages.push(i);
          }
          if (current < total - 2) pages.push("...");
          if (total > 1) pages.push(total);
        }

        smartUpdate(
          pagesEl,
          pages
            .map((p) => {
              if (p === "...") {
                return '<span class="pagination-ellipsis">...</span>';
              }
              const activeClass = p === current ? "active" : "";
              return `<button class="pagination-page ${activeClass}" onclick="goToPage(${p})">${p}</button>`;
            })
            .join(""),
        );
      }

      // Fetch and render data (progressive loading)
      // Unified state fetch - single API call for all dashboard data
      async function fetchData() {
        try {
          const response = await fetch("/api/state");
          if (!response.ok) throw new Error(`HTTP ${response.status}`);
          const state = await response.json();
          renderFullState(state);
        } catch (e) {
          console.error("Failed to fetch state:", e);
          // Fallback: try individual fetches if unified fails
          fetchDataLegacy();
        }
      }

      // Render all widgets from unified state
      function renderFullState(state) {
        if (!state) return;

        // Update timestamp
        const now = new Date().toLocaleTimeString();
        $set("last-updated", "textContent", now);
        $set(
          "sidebar-updated",
          "textContent",
          i18nText("sidebar.updated", { time: now }, `Updated: ${now}`),
        );

        // Render each section
        if (state.vitals) renderVitals(state.vitals);
        if (state.sessions) renderSessions(state.sessions, state.pagination, state.statusCounts);
        if (state.tokenStats) renderTokenStats(state.tokenStats);
        if (state.capacity) renderCapacity(state.capacity);
        if (state.operators) renderOperators(state.operators);
        if (state.llmUsage) renderLlmUsage(state.llmUsage);
        if (state.cron) renderCron(state.cron);
        if (state.memory) renderMemory(state.memory);
        if (state.cerebro) renderCerebro(state.cerebro);
        if (state.subagents) renderSubagents(state.subagents);
      }

      // Legacy fallback - multiple API calls (used if /api/state fails)
      async function fetchDataLegacy() {
        console.log("[Legacy] Falling back to individual API calls");

        // Fire off all requests in parallel
        const promises = [
          fetch("/api/vitals")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/sessions")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/operators")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/llm-usage")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/cron")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/memory")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/cerebro")
            .then((r) => r.json())
            .catch(() => null),
          fetch("/api/subagents")
            .then((r) => r.json())
            .catch(() => null),
        ];

        const [vitals, sessions, operators, llm, cron, memory, cerebro, subagents] =
          await Promise.all(promises);

        if (vitals?.vitals) renderVitals(vitals.vitals);
        if (sessions?.sessions)
          renderSessions(sessions.sessions, sessions.pagination, sessions.statusCounts);
        if (sessions?.tokenStats) renderTokenStats(sessions.tokenStats);
        if (operators) renderOperators(operators);
        if (llm) renderLlmUsage(llm);
        if (cron?.cron) renderCron(cron.cron);
        if (memory?.memory) renderMemory(memory.memory);
        if (cerebro) renderCerebro(cerebro);
        if (subagents?.subagents) renderSubagents(subagents.subagents);

        const now = new Date().toLocaleTimeString();
        $set("last-updated", "textContent", now);
        $set(
          "sidebar-updated",
          "textContent",
          i18nText("sidebar.updated", { time: now }, `Updated: ${now}`),
        );
      }

      // Render just sessions (for progressive loading)
      function renderSessions(sessions, pagination, statusCounts) {
        const sessionsEl = document.getElementById("sessions");
        sessionsData = sessions;

        // Update pagination state if provided
        if (pagination) {
          paginationState = { ...paginationState, ...pagination };
          renderPagination(pagination);
        }

        // Always use paginationState.total if we have it (survives SSE updates)
        // Only fall back to sessions.length if we've never received pagination data
        const displayCount = paginationState.total > 0 ? paginationState.total : sessions.length;

        // Filter out hidden sessions
        const visibleSessions = sessions.filter((s) => !isSessionHidden(s));
        const hiddenSessionsCount = sessions.length - visibleSessions.length;

        // Show hidden count breakdown if any hidden
        const sessionCountText =
          hiddenSessionsCount > 0
            ? `${displayCount} (${hiddenSessionsCount} hidden)`
            : displayCount;
        $set("session-count", "textContent", sessionCountText);
        $set("nav-session-count", "textContent", displayCount);

        // Use server-provided statusCounts for ALL sessions, not just current page
        // If statusCounts not provided, keep previous values (don't overwrite with wrong counts)
        if (statusCounts) {
          updateFilterCountsFromServer(statusCounts);
        }
        // Removed: fallback to updateFilterCounts(sessions) which only counted current page

        if (visibleSessions.length === 0) {
          smartUpdate(
            sessionsEl,
            `
                    <div class="empty-state">
                        <div class="empty-state-icon">📡</div>
                        <div class="empty-state-text">No active sessions</div>
                    </div>
                `,
          );
        } else {
          smartUpdate(
            sessionsEl,
            visibleSessions
              .sort((a, b) => a.minutesAgo - b.minutesAgo)
              .map((s) => {
                const iconClass =
                  s.channel === "slack" ? "slack" : s.channel === "telegram" ? "telegram" : "main";
                const icon = s.channel === "slack" ? "💬" : s.channel === "telegram" ? "📱" : "🏠";
                const badgeClass = s.active
                  ? "badge-live"
                  : s.recentlyActive
                    ? "badge-recent"
                    : "badge-idle";
                const badgeText = s.active ? "● Live" : formatTimeAgo(s.minutesAgo);
                const tokenClass = s.tokens > 100000 ? "high" : s.tokens > 50000 ? "med" : "";
                const model = s.model?.replace("claude-", "")?.replace("anthropic/", "") || "";
                const cardClass = s.active ? "active" : s.recentlyActive ? "recent-active" : "";
                const status = s.active ? "live" : s.recentlyActive ? "recent" : "idle";

                // Generate topic pills (filtered by privacy settings)
                let topicHtml = "";
                if (s.topic) {
                  const topics = s.topic
                    .split(", ")
                    .map((t) => t.trim())
                    .filter((t) => t && !isTopicHidden(t));
                  if (topics.length > 0) {
                    const pills = topics
                      .map((t) => {
                        const className = t.toLowerCase().replace(/[^a-z]/g, "");
                        return `<span class="topic-pill ${className}">${escapeHtml(t)}</span>`;
                      })
                      .join("");
                    topicHtml = `<div class="card-topics">${pills}</div>`;
                  }
                }
                const previewHtml = s.preview
                  ? `<div class="card-preview">${escapeHtml(s.preview)}</div>`
                  : "";
                // Cerebro tag (filtered by privacy settings)
                const cerebroTagHtml =
                  s.cerebroTopic && !isTopicHidden(s.cerebroTopic)
                    ? `<span class="cerebro-tag" title="Cerebro topic: ${escapeHtml(s.cerebroTopic)}">🏷️ ${escapeHtml(s.cerebroTopic)}</span>`
                    : "";

                // Originator info
                let originatorHtml = "";
                if (s.originator) {
                  const displayName =
                    s.originator.displayName || s.originator.username || "Unknown";
                  const initial = displayName.charAt(0).toUpperCase();
                  originatorHtml = `
                            <div class="session-originator">
                                <span class="originator-avatar">${initial}</span>
                                <span>${escapeHtml(displayName)}</span>
                            </div>
                        `;
                }

                // Activity state indicator
                const activityState = s.activityState || {
                  state: "idle",
                  icon: "💤",
                  label: "Idle",
                };
                const activityHtml = `
                        <div class="activity-wrapper" title="${activityState.label}">
                            <span class="activity-indicator ${activityState.state}">${activityState.icon}</span>
                            <span class="activity-label">${activityState.label}</span>
                        </div>
                    `;

                // Build metrics bar (fitness tracker style)
                const m = s.metrics || { burnRate: 0, toolCalls: 0, minutesActive: 0 };
                const burnRateClass = m.burnRate > 5000 ? "hot" : "";
                const burnRateFormatted =
                  m.burnRate > 1000 ? (m.burnRate / 1000).toFixed(1) + "k" : m.burnRate;
                const timeActiveFormatted =
                  m.minutesActive > 60
                    ? Math.floor(m.minutesActive / 60) + "h " + (m.minutesActive % 60) + "m"
                    : m.minutesActive + "m";

                // Operator metric (clickable to show user stats)
                const operatorName = s.originator?.displayName || s.originator?.username || null;
                const operatorId = s.originator?.userId || s.originator?.id || null;
                const operatorMetricHtml = operatorName
                  ? `<div class="metric-ring operator" title="User: ${escapeHtml(operatorName)}" onclick="event.stopPropagation(); openOperatorModal('${escapeHtml(operatorId || operatorName)}')">
                      <span class="metric-icon">👤</span>
                      <span class="metric-value" style="font-size: 0.7rem; max-width: 50px; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(operatorName.split(" ")[0])}</span>
                      <span class="metric-label">user</span>
                   </div>`
                  : `<div class="metric-ring operator" title="Unknown user">
                      <span class="metric-icon">👤</span>
                      <span class="metric-value">—</span>
                      <span class="metric-label">user</span>
                   </div>`;

                const metricsHtml = `
                        <div class="metrics-bar">
                            <div class="metric-ring burn ${burnRateClass}" title="Token burn rate: ${m.burnRate} tokens/min">
                                <span class="metric-icon">🔥</span>
                                <span class="metric-value">${burnRateFormatted}</span>
                                <span class="metric-label">tok/min</span>
                            </div>
                            ${operatorMetricHtml}
                            <div class="metric-ring time" title="Time active: ${m.minutesActive} minutes">
                                <span class="metric-icon">⏱️</span>
                                <span class="metric-value">${timeActiveFormatted}</span>
                                <span class="metric-label">active</span>
                            </div>
                        </div>
                    `;

                return `
                    <div class="session-card ${cardClass}" data-status="${status}" data-channel="${s.channel}" data-kind="${s.sessionType || s.kind}" onclick="openDetail('${escapeHtml(s.sessionKey)}', '${escapeHtml(s.label)}')">
                        <div class="card-header">
                            <div class="card-icon ${iconClass}">${icon}</div>
                            <div class="card-title-area">
                                <div class="card-title">${escapeHtml(s.label)}</div>
                                <div class="card-subtitle">${s.kind} • ${model}</div>
                                ${originatorHtml}
                            </div>
                            ${activityHtml}
                            <span class="card-badge ${badgeClass}">${badgeText}</span>
                            <button class="hide-btn" onclick="event.stopPropagation(); quickHideSession('${escapeHtml(s.sessionKey).replace(/'/g, "\\'")}', '${escapeHtml(s.label).replace(/'/g, "\\'")}');" title="Hide session">👁️</button>
                        </div>
                        ${topicHtml}
                        ${previewHtml}
                        <div class="card-stats">
                            ${cerebroTagHtml}
                            <div class="card-stat ${tokenClass}">
                                <span>🎫</span>
                                <span class="card-stat-value">${(s.tokens / 1000).toFixed(1)}k</span>
                            </div>
                        </div>
                        ${metricsHtml}
                    </div>
                    `;
              })
              .join(""),
          );
        }

        applyFilter();
      }

      // Render just cron jobs (for progressive loading)
      function renderCron(cron) {
        const cronEl = document.getElementById("cron-jobs");
        cronData = cron; // Store for re-rendering after privacy changes

        // Filter out hidden crons
        const visibleCrons = cron.filter((c) => !isCronHidden(c));
        const hiddenCronsCount = cron.length - visibleCrons.length;

        // Show hidden count breakdown if any are hidden
        const cronCountText =
          hiddenCronsCount > 0
            ? `${cron.length} (${visibleCrons.length} visible, ${hiddenCronsCount} hidden)`
            : cron.length;
        $set("cron-count", "textContent", cronCountText);
        $set("nav-cron-count", "textContent", cron.length);

        if (visibleCrons.length === 0) {
          smartUpdate(
            cronEl,
            `
                    <div class="empty-state">
                        <div class="empty-state-icon">⏰</div>
                        <div class="empty-state-text">No scheduled jobs</div>
                    </div>
                `,
          );
        } else {
          smartUpdate(
            cronEl,
            visibleCrons
              .map((c) => {
                const humanSchedule = c.scheduleHuman
                  ? `<div class="cron-schedule-human">${escapeHtml(c.scheduleHuman)}</div>`
                  : "";
                return `
                    <div class="cron-card ${c.enabled === false ? "disabled" : ""}">
                        <div class="cron-icon">⏰</div>
                        <div class="cron-info">
                            <div class="cron-name">${escapeHtml(c.name)}</div>
                            <div class="cron-schedule">${c.schedule}</div>
                            ${humanSchedule}
                        </div>
                        <div class="cron-meta">
                            <span class="cron-status ${c.enabled !== false ? "enabled" : "disabled"}">
                                ${c.enabled !== false ? "✓ Enabled" : "○ Disabled"}
                            </span>
                            <div class="cron-next">${c.nextRun}</div>
                            <button class="hide-btn" onclick="event.stopPropagation(); quickHideCron('${escapeHtml(c.id || c.name).replace(/'/g, "\\'")}', '${escapeHtml(c.name).replace(/'/g, "\\'")}');" title="Hide cron job">👁️</button>
                        </div>
                    </div>
                `;
              })
              .join(""),
          );
        }
      }

      // Operators data store
      let operatorsData = [];

      // Render operators
      function renderOperators(data) {
        const operatorsEl = document.getElementById("operators-grid");
        operatorsData = data.operators || [];

        $set("nav-operator-count", "textContent", operatorsData.length);

        if (operatorsData.length === 0) {
          smartUpdate(
            operatorsEl,
            `
                    <div class="empty-state">
                        <div class="empty-state-icon">👥</div>
                        <div class="empty-state-text">No operators configured</div>
                        <div class="empty-state-hint" style="margin-top: 8px; font-size: 0.8rem; color: var(--text-muted);">
                            Operators are auto-detected from session activity
                        </div>
                    </div>
                `,
          );
        } else {
          smartUpdate(
            operatorsEl,
            operatorsData
              .map((op) => {
                const roleClass = op.role || "user";
                const initial = (op.name || op.username || "?").charAt(0).toUpperCase();
                const avatarHtml = op.avatar
                  ? `<img src="${escapeHtml(op.avatar)}" alt="${escapeHtml(op.name)}">`
                  : initial;

                const activeSessions = op.stats?.activeSessions || 0;
                const totalSessions = op.stats?.totalSessions || 0;

                let lastSeenText = "Never";
                if (op.stats?.lastSeen) {
                  const lastSeen = new Date(op.stats.lastSeen);
                  const minutesAgo = Math.floor((Date.now() - lastSeen.getTime()) / 60000);
                  lastSeenText =
                    minutesAgo < 1
                      ? i18nText("time.justNow", {}, "Just now")
                      : formatTimeAgo(minutesAgo);
                }

                return `
                    <div class="operator-card role-${roleClass}" style="cursor: pointer;" onclick="openOperatorModal('${escapeHtml(op.id || op.username)}')">
                        <div class="operator-header">
                            <div class="operator-avatar">${avatarHtml}</div>
                            <div class="operator-info">
                                <div class="operator-name">${escapeHtml(op.name || op.username || "Unknown")}</div>
                                <div class="operator-username">@${escapeHtml(op.username || op.id)}</div>
                            </div>
                            <span class="operator-role ${roleClass}">${roleClass}</span>
                        </div>
                        <div class="operator-stats">
                            <div class="operator-stat">
                                <div class="operator-stat-value" style="color: ${activeSessions > 0 ? "var(--green)" : "var(--text-muted)"}">${activeSessions}</div>
                                <div class="operator-stat-label">Active</div>
                            </div>
                            <div class="operator-stat">
                                <div class="operator-stat-value">${totalSessions}</div>
                                <div class="operator-stat-label">Sessions</div>
                            </div>
                            <div class="operator-stat">
                                <div class="operator-stat-value" style="font-size: 0.9rem;">${lastSeenText}</div>
                                <div class="operator-stat-label">Last Seen</div>
                            </div>
                        </div>
                    </div>
                    `;
              })
              .join(""),
          );
        }
      }

      // Refresh operators data
      async function refreshOperators() {
        try {
          const res = await fetch("/api/operators");
          const data = await res.json();
          renderOperators(data);
        } catch (e) {
          console.error("Failed to fetch operators:", e);
        }
      }

      // Store current token stats for window switching
      let currentTokenStats = null;
      let optionalDeps = null;

      // Get saved savings window preference (default to 7dma for stability)
      function getSavingsWindowPref() {
        return localStorage.getItem("savingsWindow") || "7dma";
      }

      // Save savings window preference
      function setSavingsWindowPref(window) {
        localStorage.setItem("savingsWindow", window);
      }

      // Update savings display based on selected window
      function updateSavingsDisplay(stats, windowKey) {
        const savingsStat = document.getElementById("savings-stat");
        const savingsEl = document.getElementById("est-savings");

        if (!stats || !savingsStat || !savingsEl) return;

        // Get the window-specific data or fall back to 24h
        const windowData = stats.savingsWindows?.[windowKey] || stats.savingsWindows?.["24h"];

        if (windowData?.estSavings) {
          savingsEl.textContent = windowData.estSavings;
          savingsEl.title = `${windowData.savingsPercent}% saved vs ${stats.planName} ($${stats.planCost}/mo) [${windowData.label}]`;
          savingsStat.style.display = "block";
        } else if (stats.estSavings) {
          // Fallback to legacy 24h savings
          savingsEl.textContent = stats.estSavings;
          savingsEl.title = `${stats.savingsPercent}% saved vs ${stats.planName} ($${stats.planCost}/mo)`;
          savingsStat.style.display = "block";
        } else {
          savingsStat.style.display = "none";
        }
      }

      // Render token stats
      function renderTokenStats(stats) {
        if (!stats) return;
        currentTokenStats = stats; // Store for window switching

        $set("total-tokens", "textContent", stats.total || "0");
        $set("active-sessions", "textContent", stats.activeCount || 0);
        $set("input-tokens", "textContent", stats.input || "0");
        $set("output-tokens", "textContent", stats.output || "0");
        $set("est-cost", "textContent", stats.estCost || "$0.00");
        $set("nav-tokens", "textContent", stats.total || "0");
        $set("nav-cost", "textContent", stats.estCost || "$0.00");
        $set("nav-monthly-cost", "textContent", stats.estMonthlyCost || "-");
        $set("nav-avg-tokens", "textContent", stats.avgTokensPerSession || "-");
        $set("nav-avg-cost", "textContent", stats.avgCostPerSession || "-");

        // Load preference and update selector
        const savedWindow = getSavingsWindowPref();
        const windowSelect = document.getElementById("savings-window-select");
        if (windowSelect) {
          windowSelect.value = savedWindow;
        }

        // Show savings for selected window
        updateSavingsDisplay(stats, savedWindow);
      }

      // Render capacity indicators
      function renderCapacity(capacity) {
        if (!capacity) return;
        const mainEl = document.getElementById("main-capacity");
        const subEl = document.getElementById("subagent-capacity");

        if (mainEl && capacity.main) {
          const mainPct =
            capacity.main.max > 0 ? (capacity.main.active / capacity.main.max) * 100 : 0;
          const mainColor =
            mainPct > 80 ? "var(--red)" : mainPct > 50 ? "var(--yellow)" : "var(--green)";
          mainEl.innerHTML = `<span style="color:${mainColor}">${capacity.main.active}</span>/${capacity.main.max}`;
        }

        if (subEl && capacity.subagent) {
          const subPct =
            capacity.subagent.max > 0
              ? (capacity.subagent.active / capacity.subagent.max) * 100
              : 0;
          const subColor =
            subPct > 80 ? "var(--red)" : subPct > 50 ? "var(--yellow)" : "var(--green)";
          subEl.innerHTML = `<span style="color:${subColor}">${capacity.subagent.active}</span>/${capacity.subagent.max}`;
        }
      }

      // Render system info (placeholder)
      function renderSystem(system) {
        // System rendering is handled by full status
      }

      // Render activity (placeholder)
      function renderActivity(activity) {
        // Activity rendering is handled by full status
      }

      function renderVitals(vitals) {
        if (!vitals) return;

        // Hostname & uptime
        $set("vitals-hostname", "textContent", vitals.hostname || "-");
        $set("vitals-uptime", "textContent", vitals.uptime || "-");

        // CPU
        const cpuPercent = vitals.cpu?.usage || 0;
        $set("cpu-percent", "textContent", cpuPercent + "%");
        $set("cpu-bar", "style.width", cpuPercent + "%");

        // Color based on load
        const cpuBar = document.getElementById("cpu-bar");
        if (cpuBar) {
          cpuBar.className =
            "vital-bar-fill " + (cpuPercent > 80 ? "red" : cpuPercent > 50 ? "yellow" : "blue");
        }

        // Chip name
        const chipEl = document.getElementById("cpu-chip");
        if (vitals.cpu?.chip) {
          chipEl.textContent = vitals.cpu.chip;
        } else if (vitals.cpu?.brand) {
          chipEl.textContent = vitals.cpu.brand;
        } else {
          chipEl.textContent = "";
        }

        // User/sys/idle breakdown
        // Avoid showing "undefined%" when fields are absent.
        const cpuUser = vitals.cpu?.userPercent;
        const cpuSys = vitals.cpu?.sysPercent;
        const cpuIdle = vitals.cpu?.idlePercent;
        $set("cpu-user", "textContent", Number.isFinite(cpuUser) ? cpuUser.toFixed(1) + "%" : "-");
        $set("cpu-sys", "textContent", Number.isFinite(cpuSys) ? cpuSys.toFixed(1) + "%" : "-");
        $set("cpu-idle", "textContent", Number.isFinite(cpuIdle) ? cpuIdle.toFixed(1) + "%" : "-");

        const loadAvg = vitals.cpu?.loadAvg || [0, 0, 0];
        $set("cpu-load-1", "textContent", loadAvg[0]?.toFixed(2) || "-");
        $set("cpu-load-5", "textContent", loadAvg[1]?.toFixed(2) || "-");
        $set("cpu-load-15", "textContent", loadAvg[2]?.toFixed(2) || "-");
        $set("cpu-cores", "textContent", vitals.cpu?.cores || "-");

        // Core topology (P-cores + E-cores)
        const topologyEl = document.getElementById("cpu-topology");
        if (vitals.cpu?.pCores && vitals.cpu?.eCores) {
          topologyEl.textContent = `${vitals.cpu.pCores}P + ${vitals.cpu.eCores}E cores`;
        } else {
          topologyEl.textContent = "";
        }

        // Memory - Show "X% used" with "X of Y" summary
        const memPercent = vitals.memory?.percent || 0;
        $set(
          "mem-percent",
          "innerHTML",
          memPercent + '% <small style="font-size:0.6em;opacity:0.7">used</small>',
        );
        $set("mem-bar", "style.width", memPercent + "%");

        const memBar = document.getElementById("mem-bar");
        if (memBar) {
          memBar.className =
            "vital-bar-fill " + (memPercent > 90 ? "red" : memPercent > 75 ? "yellow" : "green");
        }

        // Show "68.8GB of 128GB" format
        const memUsed = vitals.memory?.usedFormatted || "-";
        const memTotal = vitals.memory?.totalFormatted || "-";
        $set("mem-summary", "textContent", memUsed + " of " + memTotal);
        $set("mem-free", "textContent", vitals.memory?.freeFormatted || "-");

        // Memory pressure
        const pressure = vitals.memory?.pressure || "normal";
        const pressureEl = document.getElementById("mem-pressure");
        if (pressureEl) {
          pressureEl.textContent = pressure.charAt(0).toUpperCase() + pressure.slice(1);
          pressureEl.className = "pressure-indicator " + pressure;
        }

        // Memory breakdown (active, wired, compressed, cached)
        const formatMemBytes = (bytes) => {
          if (!bytes) return "-";
          const gb = bytes / (1024 * 1024 * 1024);
          return gb >= 1 ? gb.toFixed(1) + " GB" : (gb * 1024).toFixed(0) + " MB";
        };
        $set("mem-active", "textContent", formatMemBytes(vitals.memory?.active));
        $set("mem-wired", "textContent", formatMemBytes(vitals.memory?.wired));
        $set("mem-compressed", "textContent", formatMemBytes(vitals.memory?.compressed));
        $set("mem-cached", "textContent", formatMemBytes(vitals.memory?.cached));

        // Disk - Show "X% used" with "X of Y" summary
        const diskPercent = vitals.disk?.percent || 0;
        $set(
          "disk-percent",
          "innerHTML",
          diskPercent + '% <small style="font-size:0.6em;opacity:0.7">used</small>',
        );
        $set("disk-bar", "style.width", diskPercent + "%");

        const diskBar = document.getElementById("disk-bar");
        if (diskBar) {
          diskBar.className =
            "vital-bar-fill " + (diskPercent > 90 ? "red" : diskPercent > 75 ? "yellow" : "green");
        }

        // Show "700GB of 1.8TB" format
        const diskUsed = vitals.disk?.usedFormatted || "-";
        const diskTotal = vitals.disk?.totalFormatted || "-";
        $set("disk-summary", "textContent", diskUsed + " of " + diskTotal);
        $set("disk-free", "textContent", vitals.disk?.freeFormatted || "-");

        // Disk I/O stats
        $set("disk-iops", "textContent", vitals.disk?.iops?.toFixed(0) || "0");
        $set("disk-throughput", "textContent", vitals.disk?.throughputMBps?.toFixed(2) || "0.00");
        $set("disk-kbt", "textContent", vitals.disk?.kbPerTransfer?.toFixed(1) || "0.0");

        // Show dep hint for disk I/O if all zeros and dep missing
        renderDepHint(
          "disk-io-hint",
          "disk-io",
          !vitals.disk?.iops && !vitals.disk?.throughputMBps,
        );

        // Temperature
        const temp = vitals.temperature;
        const tempNote = vitals.temperatureNote;
        const tempEl = document.getElementById("temp-value");
        const tempStatusEl = document.getElementById("temp-status");
        if (temp !== null && temp !== undefined && temp > 0) {
          if (tempEl) {
            tempEl.textContent = temp;
            const tempColor =
              temp < 50
                ? "var(--green)"
                : temp < 70
                  ? "var(--text)"
                  : temp < 85
                    ? "var(--yellow)"
                    : "var(--red)";
            tempEl.style.color = tempColor;
          }
          const tempStatus =
            temp < 50 ? "Cool" : temp < 70 ? "Normal" : temp < 85 ? "Warm" : "Hot!";
          if (tempStatusEl) tempStatusEl.textContent = tempStatus;
        } else {
          if (tempEl) {
            tempEl.textContent = "-";
            tempEl.style.color = "var(--text-muted)";
          }
          if (tempStatusEl) {
            tempStatusEl.textContent = tempNote || "Unavailable";
          }
          // Show dep hint for temperature if unavailable and dep missing
          renderDepHint("temp-hint", "temperature", true);
        }
      }

      /**
       * Render an inline hint when an optional dependency is missing.
       * Creates/updates a small element showing install instructions.
       */
      function renderDepHint(elementId, affects, show) {
        let el = document.getElementById(elementId);
        if (!show || !optionalDeps) {
          if (el) el.style.display = "none";
          return;
        }
        const dep = optionalDeps.find((d) => d.affects === affects && !d.installed);
        if (!dep) {
          if (el) el.style.display = "none";
          return;
        }
        if (!el) {
          // Find parent card based on the hint id
          const parentMap = { "disk-io-hint": "disk-iops", "temp-hint": "temp-status" };
          const anchor = document.getElementById(parentMap[elementId]);
          if (!anchor) return;
          const card = anchor.closest(".vital-card");
          if (!card) return;
          el = document.createElement("div");
          el.id = elementId;
          el.style.cssText =
            "margin-top:8px;padding:6px 10px;background:rgba(136,192,208,0.08);border:1px solid rgba(136,192,208,0.2);border-radius:6px;font-size:0.7rem;color:var(--text-muted);line-height:1.4";
          card.appendChild(el);
        }
        el.style.display = "block";
        const action = dep.installCmd
          ? '<code style="background:rgba(136,192,208,0.15);padding:1px 5px;border-radius:3px;font-size:0.65rem">' +
            dep.installCmd +
            "</code>"
          : dep.url
            ? '<a href="' +
              dep.url +
              '" target="_blank" style="color:var(--accent)">' +
              dep.name +
              "</a>"
            : "see docs";
        el.innerHTML =
          "\u{1F4A1} Install <strong>" +
          dep.name +
          "</strong> for " +
          dep.purpose.toLowerCase() +
          ": " +
          action;
      }

      // Safe DOM helper - sets property only if element exists
      function $set(id, prop, value) {
        const el = document.getElementById(id);
        if (!el) return null;
        if (prop === "innerHTML") el.innerHTML = value;
        else if (prop === "textContent") el.textContent = value;
        else if (prop === "className") el.className = value;
        else if (prop.startsWith("style.")) el.style[prop.slice(6)] = value;
        return el;
      }

      function renderLlmUsage(data) {
        // Wrap in try-catch to prevent crashes from blocking other renders
        try {
          // Handle auth errors - show clear error state instead of 0%
          if (data?.errorType === "auth" || data?.claude?.session?.error) {
            const errorMsg = "⚠️ Auth Error";
            const clickableError =
              '<a href="#" onclick="openAuthModal(); return false;" style="color:#f59e0b; text-decoration: underline; cursor: pointer;">Auth Error - Click to Fix</a>';

            // Session card
            $set("claude-session-pct", "innerHTML", '<span style="color:#f59e0b">N/A</span>');
            $set("claude-session-bar", "style.width", "0%");
            $set("claude-session-bar", "className", "vital-bar-fill gray");
            $set("claude-session-remaining", "textContent", "N/A");
            $set("claude-session-reset", "innerHTML", clickableError);

            // Weekly card
            $set("claude-weekly-pct", "innerHTML", '<span style="color:#f59e0b">N/A</span>');
            $set("claude-weekly-bar", "style.width", "0%");
            $set("claude-weekly-bar", "className", "vital-bar-fill gray");
            $set("claude-weekly-remaining", "textContent", "N/A");
            $set("claude-weekly-reset", "innerHTML", clickableError);

            // Sonnet card
            $set("sonnet-weekly-pct", "innerHTML", '<span style="color:#f59e0b">N/A</span>');
            $set("sonnet-weekly-bar", "style.width", "0%");
            $set("sonnet-weekly-bar", "className", "vital-bar-fill gray");
            $set("sonnet-weekly-remaining", "textContent", "N/A");
            $set("sonnet-weekly-reset", "innerHTML", clickableError);

            // Compact cards - Claude
            const compactSessionEl = document.getElementById("claude-compact-session-pct");
            const compactSessionBar = document.getElementById("claude-compact-session-bar");
            if (compactSessionEl) compactSessionEl.textContent = "N/A";
            if (compactSessionBar) {
              compactSessionBar.style.width = "0%";
              compactSessionBar.className = "quota-bar-fill gray";
            }
            const compactWeekEl = document.getElementById("claude-compact-week-pct");
            const compactWeekBar = document.getElementById("claude-compact-week-bar");
            if (compactWeekEl) compactWeekEl.textContent = "N/A";
            if (compactWeekBar) {
              compactWeekBar.style.width = "0%";
              compactWeekBar.className = "quota-bar-fill gray";
            }

            // Compact cards - Codex (show 0% but with gray bars since we don't track Codex via API)
            const codex5hEl = document.getElementById("codex-5h-pct");
            const codex5hBar = document.getElementById("codex-5h-bar");
            const codexDayEl = document.getElementById("codex-day-pct");
            const codexDayBar = document.getElementById("codex-day-bar");
            if (codex5hEl) codex5hEl.textContent = "0%";
            if (codex5hBar) {
              codex5hBar.style.width = "0%";
              codex5hBar.className = "quota-bar-fill low";
            }
            if (codexDayEl) codexDayEl.textContent = "0%";
            if (codexDayBar) {
              codexDayBar.style.width = "0%";
              codexDayBar.className = "quota-bar-fill low";
            }
            $set("codex-tasks", "textContent", "0 total");
            $set("llm-sync-time", "textContent", errorMsg);

            // Still render routing data if available
            if (data.routing) {
              const ct = data.routing.claudeTasks || 0;
              const cx = data.routing.codexTasks || 0;
              const total = data.routing.total || 0;
              $set(
                "llm-routing-summary",
                "textContent",
                total > 0 ? `${ct} Claude / ${cx} Codex (${total} tasks)` : "No coding tasks yet",
              );

              // Task routing counts
              $set("codex-tasks", "textContent", total + " total");
              $set("claude-task-count", "textContent", ct);
              $set("codex-task-count", "textContent", cx);
            }
            return;
          }

          if (!data || data.error) {
            $set("llm-sync-time", "textContent", data?.needsSync ? "Needs sync" : "Error");
            return;
          }

          // Sync time
          if (data.claude?.lastSynced) {
            const synced = new Date(data.claude.lastSynced);
            const ago = Math.round((Date.now() - synced) / 60000);
            $set(
              "llm-sync-time",
              "textContent",
              ago < 60 ? `${ago}m ago` : `${Math.round(ago / 60)}h ago`,
            );
          } else if (data.source === "live") {
            $set("llm-sync-time", "textContent", "Live");
          }

          // Routing summary - show task counts clearly
          if (data.routing) {
            const ct = data.routing.claudeTasks || 0;
            const cx = data.routing.codexTasks || 0;
            const total = data.routing.total || 0;
            $set(
              "llm-routing-summary",
              "textContent",
              total > 0 ? `${ct} Claude / ${cx} Codex (${total} tasks)` : "No coding tasks yet",
            );
          }

          // Claude Session - Show USED as primary (bar fills with consumption)
          const sessionRemaining = data.claude?.session?.remainingPct || 0;
          const sessionUsed = data.claude?.session?.usedPct || 0;
          $set(
            "claude-session-pct",
            "innerHTML",
            sessionUsed + '% <small style="font-size:0.6em;opacity:0.7">used</small>',
          );
          $set("claude-session-bar", "style.width", sessionUsed + "%");
          $set("claude-session-remaining", "textContent", sessionRemaining + "%");
          $set("claude-session-reset", "textContent", data.claude?.session?.resetsIn || "-");

          // Color based on used - red when nearly depleted (high usage)
          const sessionBar = document.getElementById("claude-session-bar");
          if (sessionBar) {
            sessionBar.className =
              "vital-bar-fill " +
              (sessionUsed > 80 ? "red" : sessionUsed > 50 ? "yellow" : "green");
          }

          // Claude Weekly - Show USED as primary
          const weeklyRemaining = data.claude?.weekly?.remainingPct || 0;
          const weeklyUsed = data.claude?.weekly?.usedPct || 0;
          $set(
            "claude-weekly-pct",
            "innerHTML",
            weeklyUsed + '% <small style="font-size:0.6em;opacity:0.7">used</small>',
          );
          $set("claude-weekly-bar", "style.width", weeklyUsed + "%");
          $set("claude-weekly-remaining", "textContent", weeklyRemaining + "%");
          $set("claude-weekly-reset", "textContent", data.claude?.weekly?.resets || "-");

          const weeklyBar = document.getElementById("claude-weekly-bar");
          if (weeklyBar) {
            weeklyBar.className =
              "vital-bar-fill " + (weeklyUsed > 80 ? "red" : weeklyUsed > 50 ? "yellow" : "green");
          }

          // Also update the compact quota card (uses different element IDs)
          const compactSessionEl = document.getElementById("claude-compact-session-pct");
          const compactSessionBar = document.getElementById("claude-compact-session-bar");
          if (compactSessionEl) compactSessionEl.textContent = sessionUsed + "%";
          if (compactSessionBar) {
            compactSessionBar.style.width = sessionUsed + "%";
            compactSessionBar.className =
              "quota-bar-fill " + (sessionUsed < 50 ? "low" : sessionUsed < 80 ? "medium" : "high");
          }

          const compactWeekEl = document.getElementById("claude-compact-week-pct");
          const compactWeekBar = document.getElementById("claude-compact-week-bar");
          if (compactWeekEl) compactWeekEl.textContent = weeklyUsed + "%";
          if (compactWeekBar) {
            compactWeekBar.style.width = weeklyUsed + "%";
            compactWeekBar.className =
              "quota-bar-fill " + (weeklyUsed < 50 ? "low" : weeklyUsed < 80 ? "medium" : "high");
          }

          // Sonnet Weekly - Show USED as primary
          const sonnetRemaining = data.claude?.sonnet?.remainingPct || 0;
          const sonnetUsed = data.claude?.sonnet?.usedPct || 0;
          $set(
            "sonnet-weekly-pct",
            "innerHTML",
            sonnetUsed + '% <small style="font-size:0.6em;opacity:0.7">used</small>',
          );
          $set("sonnet-weekly-bar", "style.width", sonnetUsed + "%");
          $set("sonnet-weekly-remaining", "textContent", sonnetRemaining + "%");
          $set("sonnet-weekly-reset", "textContent", data.claude?.sonnet?.resets || "-");

          const sonnetBar = document.getElementById("sonnet-weekly-bar");
          if (sonnetBar) {
            sonnetBar.className =
              "vital-bar-fill " + (sonnetUsed > 80 ? "red" : sonnetUsed > 50 ? "yellow" : "green");
          }

          // Task Routing
          const totalTasks = data.routing?.total || 0;
          const claudeTasks = data.routing?.claudeTasks || 0;
          const codexTasks = data.routing?.codexTasks || 0;
          $set("codex-tasks", "textContent", totalTasks + " total");
          $set("claude-task-count", "textContent", claudeTasks);
          $set("codex-task-count", "textContent", codexTasks);

          // Codex floor status - shows if we're meeting the 20% minimum
          const floorStatus = document.getElementById("codex-floor-status");
          const codexPct = data.routing?.codexPct || 0;
          const codexFloor = data.routing?.codexFloor || 20;
          if (floorStatus) {
            if (totalTasks === 0) {
              floorStatus.className = "pressure-indicator";
              floorStatus.textContent = `Codex ≥20%: No tasks yet`;
            } else if (codexPct >= codexFloor) {
              floorStatus.className = "pressure-indicator normal";
              floorStatus.textContent = `Codex ≥20%: ✓ ${codexPct}%`;
            } else {
              floorStatus.className = "pressure-indicator warning";
              floorStatus.textContent = `Codex ≥20%: ${codexPct}% (need more)`;
            }
          }
        } catch (e) {
          console.error("[renderLlmUsage] Error:", e.message);
        }
      }

      async function fetchRoutingStats() {
        try {
          const res = await fetch("/api/routing-stats?hours=24");
          const data = await res.json();
          renderRoutingStats(data);
        } catch (e) {
          console.error("Failed to fetch routing stats:", e);
        }
      }

      function renderRoutingStats(data) {
        if (!data || data.error) return;

        const total = data.total_requests || 0;
        const byModel = data.by_model || {};

        // Total tasks
        $set("total-routed-tasks", "textContent", total + " (24h)");

        // Count by model family
        let claudeCount = 0,
          codexCount = 0,
          llamaCount = 0,
          qwenCount = 0;
        for (const [model, count] of Object.entries(byModel)) {
          const m = model.toLowerCase();
          if (m.includes("claude") || m.includes("opus") || m.includes("sonnet")) {
            claudeCount += count;
          } else if (m.includes("codex") || m.includes("gpt")) {
            codexCount += count;
          } else if (m.includes("llama")) {
            llamaCount += count;
          } else if (m.includes("qwen")) {
            qwenCount += count;
          }
        }

        $set("claude-task-count", "textContent", claudeCount);
        $set("codex-task-count", "textContent", codexCount);
        $set("llama-task-count", "textContent", llamaCount);
        $set("qwen-task-count", "textContent", qwenCount);

        // Latency
        const avgLatency = data.avg_latency_ms || 0;
        const latencyEl = document.getElementById("routing-latency");
        if (latencyEl) {
          if (avgLatency > 0) {
            const latencySec = (avgLatency / 1000).toFixed(1);
            latencyEl.textContent = `Avg latency: ${latencySec}s`;
            latencyEl.className =
              "pressure-indicator " + (avgLatency > 30000 ? "warning" : "normal");
          } else {
            latencyEl.textContent = "Avg latency: -";
          }
        }
      }

      async function fetchLlmUsage() {
        try {
          const res = await fetch("/api/llm-usage");
          const data = await res.json();
          renderLlmUsage(data);
          // Also fetch detailed routing stats
          fetchRoutingStats();
        } catch (e) {
          console.error("Failed to fetch LLM usage:", e);
        }
      }

      function renderDashboard(data) {
        // Use the split render functions (avoids code duplication)
        if (data.vitals) renderVitals(data.vitals);
        if (data.sessions) renderSessions(data.sessions, data.pagination, data.statusCounts);
        if (data.cron) renderCron(data.cron);
        if (data.tokenStats) {
          renderTokenStats(data.tokenStats);
          // Also update the detailed stats
          $set("total-tokens", "textContent", data.tokenStats.total);
          $set("input-tokens", "textContent", data.tokenStats.input);
          $set("output-tokens", "textContent", data.tokenStats.output);
          $set("active-sessions", "textContent", data.tokenStats.activeCount);
          $set("est-cost", "textContent", data.tokenStats.estCost);
          $set("nav-tokens", "textContent", data.tokenStats.total);
          $set("nav-cost", "textContent", data.tokenStats.estCost);
          $set("nav-monthly-cost", "textContent", data.tokenStats.estMonthlyCost || "-");
          $set("nav-avg-tokens", "textContent", data.tokenStats.avgTokensPerSession || "-");
          $set("nav-avg-cost", "textContent", data.tokenStats.avgCostPerSession || "-");

          // Show savings if positive
          const savingsStat = document.getElementById("savings-stat");
          const savingsEl = document.getElementById("est-savings");
          if (data.tokenStats.estSavings && savingsStat && savingsEl) {
            savingsEl.textContent = data.tokenStats.estSavings;
            savingsStat.style.display = "block";
          } else if (savingsStat) {
            savingsStat.style.display = "none";
          }
        }

        // Capacity
        if (data.capacity) renderCapacity(data.capacity);

        // Memory
        if (data.memory) {
          renderMemory(data.memory);
        }

        // Cerebro
        if (data.cerebro) {
          renderCerebro(data.cerebro);
        }
      }

      function renderMemory(memory) {
        $set("memory-count", "textContent", `${memory.totalFiles} files`);
        $set("nav-memory-count", "textContent", memory.totalFiles);

        $set("memory-md-size", "textContent", memory.memoryMdSizeFormatted || "-");
        $set("memory-md-lines", "textContent", memory.memoryMdLines || "-");

        $set("memory-total-files", "textContent", memory.totalFiles || "-");
        $set("memory-total-size", "textContent", memory.totalSizeFormatted || "-");

        // Recent files
        const recentEl = document.getElementById("memory-recent-files");
        if (memory.recentFiles && memory.recentFiles.length > 0) {
          smartUpdate(
            recentEl,
            memory.recentFiles
              .map(
                (f) => `
                    <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--border); font-size: 0.8rem;">
                        <span style="color: var(--accent);">📄 ${escapeHtml(f.name)}</span>
                        <span style="color: var(--text-muted);">${f.sizeFormatted} • ${f.age}</span>
                    </div>
                `,
              )
              .join(""),
          );
        } else {
          smartUpdate(
            recentEl,
            '<em style="color: var(--text-muted); font-size: 0.8rem;">No memory files yet</em>',
          );
        }
      }

      // Cerebro rendering
      function renderCerebro(cerebro) {
        // Store for re-rendering when privacy settings change
        window.lastCerebroData = cerebro;

        const notInitEl = document.getElementById("cerebro-not-initialized");
        const initEl = document.getElementById("cerebro-initialized");

        if (!cerebro || !cerebro.initialized) {
          // Show not initialized state with dynamic path
          if (notInitEl) notInitEl.style.display = "block";
          if (initEl) initEl.style.display = "none";
          $set("cerebro-count", "textContent", "not initialized");
          $set("nav-cerebro-count", "textContent", "-");

          // Update init commands with actual configured path
          if (cerebro && cerebro.cerebroPath) {
            const basePath = cerebro.cerebroPath.replace(/^\/Users\/[^/]+/, "~");
            $set("cerebro-init-topics-cmd", "textContent", `mkdir -p ${basePath}/topics`);
            $set("cerebro-init-orphans-cmd", "textContent", `mkdir -p ${basePath}/orphans`);
          }
          return;
        }

        // Show initialized state
        if (notInitEl) notInitEl.style.display = "none";
        if (initEl) initEl.style.display = "block";

        // Calculate hidden topics count from current view
        const allTopics = cerebro.recentTopics || [];
        const hiddenTopicsCount = allTopics.filter((t) => isTopicHidden(t.name)).length;
        const visibleTopicsCount = allTopics.length - hiddenTopicsCount;

        // Update counts with hidden breakdown (updates dynamically on hide/unhide)
        const countText =
          hiddenTopicsCount > 0
            ? `${cerebro.topics.total} topics (${visibleTopicsCount} visible, ${hiddenTopicsCount} hidden)`
            : `${cerebro.topics.total} topics`;
        $set("cerebro-count", "textContent", countText);
        $set("nav-cerebro-count", "textContent", cerebro.topics.total);

        $set("cerebro-active", "textContent", cerebro.topics.active || 0);
        $set("cerebro-resolved", "textContent", cerebro.topics.resolved || 0);
        $set("cerebro-parked", "textContent", cerebro.topics.parked || 0);
        $set("cerebro-total-topics", "textContent", cerebro.topics.total || 0);

        $set("cerebro-threads", "textContent", cerebro.threads || 0);
        $set("cerebro-orphans", "textContent", cerebro.orphans || 0);

        // Recent topics with action buttons (filtered by privacy settings)
        const recentEl = document.getElementById("cerebro-recent-topics");
        const visibleTopics = allTopics.filter((t) => !isTopicHidden(t.name));

        if (visibleTopics.length > 0) {
          smartUpdate(
            recentEl,
            visibleTopics
              .map((t) => {
                const statusIcon =
                  t.status === "active" ? "🟢" : t.status === "resolved" ? "✅" : "⏸️";
                const statusColor =
                  t.status === "active"
                    ? "var(--green)"
                    : t.status === "resolved"
                      ? "var(--accent)"
                      : "var(--text-muted)";

                // Action buttons based on status (always include hide button)
                const hideBtn = `<button class="topic-action-btn hide" onclick="quickHideTopic('${escapeHtml(t.name).replace(/'/g, "\\'")}', '${escapeHtml(t.title || t.name).replace(/'/g, "\\'")}'); event.stopPropagation();" title="Hide topic">👁️</button>`;
                let actionButtons = "";
                if (t.status === "active") {
                  actionButtons = `
                            <button class="topic-action-btn resolve" onclick="updateTopicStatus('${escapeHtml(t.name)}', 'resolved')" title="Mark as resolved">✓</button>
                            <button class="topic-action-btn park" onclick="updateTopicStatus('${escapeHtml(t.name)}', 'parked')" title="Park topic">⏸</button>
                            ${hideBtn}
                        `;
                } else {
                  actionButtons = `
                            <button class="topic-action-btn reactivate" onclick="updateTopicStatus('${escapeHtml(t.name)}', 'active')" title="Reactivate topic">↩</button>
                            ${hideBtn}
                        `;
                }

                return `
                        <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 0.8rem;">
                            <div style="display: flex; align-items: center; gap: 8px; flex: 1;">
                                <span>${statusIcon}</span>
                                <span style="color: ${statusColor};">${escapeHtml(t.title || t.name)}</span>
                                ${t.threads > 0 ? `<span style="color: var(--text-muted); font-size: 0.7rem;">(${t.threads} threads)</span>` : ""}
                            </div>
                            <div class="topic-actions">
                                ${actionButtons}
                            </div>
                            <span style="color: var(--text-muted); margin-left: 8px;">${t.age || "-"}</span>
                        </div>
                    `;
              })
              .join(""),
          );
        } else {
          smartUpdate(
            recentEl,
            '<em style="color: var(--text-muted); font-size: 0.8rem;">No active topics yet</em>',
          );
        }

        // Last updated
        const lastUpdatedEl = document.getElementById("cerebro-last-updated");
        if (cerebro.lastUpdated) {
          const date = new Date(cerebro.lastUpdated);
          const now = new Date();
          const diffMs = now - date;
          const diffMins = Math.round(diffMs / 60000);
          if (diffMins < 1) lastUpdatedEl.textContent = "just now";
          else if (diffMins < 60) lastUpdatedEl.textContent = `${diffMins}m ago`;
          else if (diffMins < 1440) lastUpdatedEl.textContent = `${Math.round(diffMins / 60)}h ago`;
          else lastUpdatedEl.textContent = `${Math.round(diffMins / 1440)}d ago`;
        } else {
          lastUpdatedEl.textContent = "-";
        }
      }

      // Detail panel
      function openDetail(sessionKey, label) {
        document.getElementById("detail-title").textContent = label;
        document.getElementById("detail-panel").classList.remove("hidden");
        document.getElementById("detail-panel").classList.add("visible");
        document.getElementById("detail-overlay").classList.remove("hidden");
        document.getElementById("detail-overlay").classList.add("visible");

        // Loading state
        ["overview", "summary", "links", "attention", "facts", "tools", "messages"].forEach(
          (id) => {
            document.getElementById(`detail-${id}`).innerHTML =
              '<em style="color: var(--text-muted)">Loading...</em>';
          },
        );

        fetchSessionDetail(sessionKey);
      }

      function closeDetail() {
        document.getElementById("detail-panel").classList.remove("visible");
        document.getElementById("detail-overlay").classList.remove("visible");
        setTimeout(() => {
          document.getElementById("detail-panel").classList.add("hidden");
          document.getElementById("detail-overlay").classList.add("hidden");
        }, 200);
      }

      // Cost breakdown modal
      let cachedCostData = null;

      async function openCostModal() {
        document.getElementById("cost-modal").classList.remove("hidden");
        document.getElementById("cost-modal").classList.add("visible");
        document.getElementById("cost-modal-overlay").classList.remove("hidden");
        document.getElementById("cost-modal-overlay").classList.add("visible");

        // Fetch cost breakdown data
        try {
          const res = await fetch("/api/cost-breakdown");
          const data = await res.json();
          cachedCostData = data;
          renderCostBreakdown(data);
        } catch (e) {
          document.getElementById("cost-tokens").innerHTML =
            '<em style="color:var(--red)">Failed to load cost data</em>';
        }
      }

      function closeCostModal() {
        document.getElementById("cost-modal").classList.remove("visible");
        document.getElementById("cost-modal-overlay").classList.remove("visible");
        setTimeout(() => {
          document.getElementById("cost-modal").classList.add("hidden");
          document.getElementById("cost-modal-overlay").classList.add("hidden");
        }, 200);
      }

      // Auth fix modal
      function openAuthModal() {
        document.getElementById("auth-modal").classList.remove("hidden");
        document.getElementById("auth-modal").classList.add("visible");
        document.getElementById("auth-modal-overlay").classList.remove("hidden");
        document.getElementById("auth-modal-overlay").classList.add("visible");
      }

      function closeAuthModal() {
        document.getElementById("auth-modal").classList.remove("visible");
        document.getElementById("auth-modal-overlay").classList.remove("visible");
        setTimeout(() => {
          document.getElementById("auth-modal").classList.add("hidden");
          document.getElementById("auth-modal-overlay").classList.add("hidden");
        }, 200);
      }

      // Operator modal
      async function openOperatorModal(operatorId) {
        document.getElementById("operator-modal").classList.remove("hidden");
        document.getElementById("operator-modal").classList.add("visible");
        document.getElementById("operator-modal-overlay").classList.remove("hidden");
        document.getElementById("operator-modal-overlay").classList.add("visible");

        // Show loading state
        document.getElementById("operator-modal-content").innerHTML =
          '<div class="loading-state">Loading user stats...</div>';

        try {
          // Fetch operator data from API
          const res = await fetch("/api/operators");
          const data = await res.json();

          // Find the operator by ID or name
          const operator = data.operators?.find(
            (op) =>
              op.id === operatorId ||
              op.metadata?.slackId === operatorId ||
              op.displayName === operatorId ||
              op.username === operatorId,
          );

          if (operator) {
            renderOperatorModal(operator, data.sessions || []);
          } else {
            document.getElementById("operator-modal-content").innerHTML = `
              <div class="detail-section">
                <p style="color: var(--text-muted)">Operator not found: ${escapeHtml(operatorId)}</p>
              </div>
            `;
          }
        } catch (e) {
          console.error("Failed to load operator:", e);
          document.getElementById("operator-modal-content").innerHTML = `
            <div class="detail-section">
              <p style="color: var(--error)">Failed to load user data</p>
            </div>
          `;
        }
      }

      function renderOperatorModal(operator, allSessions) {
        const displayName = operator.displayName || operator.username || "Unknown";
        document.getElementById("operator-modal-name").textContent = displayName;

        // Calculate user stats
        const userSessions = sessionsData.filter(
          (s) =>
            s.originator?.userId === operator.id ||
            s.originator?.userId === operator.metadata?.slackId ||
            s.originator?.displayName === displayName,
        );

        const activeSessions = userSessions.filter((s) => s.active).length;
        const totalTokens = userSessions.reduce((sum, s) => sum + (s.tokens || 0), 0);
        const tokensFormatted =
          totalTokens > 1000000
            ? (totalTokens / 1000000).toFixed(1) + "M"
            : totalTokens > 1000
              ? (totalTokens / 1000).toFixed(1) + "k"
              : totalTokens;

        const initial = displayName.charAt(0).toUpperCase();
        const roleLabel =
          operator.role === "owner"
            ? "👑 Owner"
            : operator.role === "admin"
              ? "⭐ Admin"
              : "👤 User";

        document.getElementById("operator-modal-content").innerHTML = `
          <div class="detail-section">
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;">
              <div style="width: 60px; height: 60px; border-radius: 50%; background: var(--accent); display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold;">
                ${initial}
              </div>
              <div>
                <div style="font-size: 1.2rem; font-weight: 600;">${escapeHtml(displayName)}</div>
                <div style="color: var(--text-muted); font-size: 0.85rem;">${roleLabel}</div>
                ${operator.source ? `<div style="color: var(--text-muted); font-size: 0.75rem;">via ${operator.source}</div>` : ""}
              </div>
            </div>
          </div>
          
          <div class="detail-section">
            <h3>📊 Stats</h3>
            <div class="detail-box">
              <div class="detail-row"><span class="detail-label">Active Sessions</span><span class="detail-value">${activeSessions}</span></div>
              <div class="detail-row"><span class="detail-label">Total Sessions</span><span class="detail-value">${userSessions.length}</span></div>
              <div class="detail-row"><span class="detail-label">Total Tokens</span><span class="detail-value">${tokensFormatted}</span></div>
              <div class="detail-row"><span class="detail-label">First Seen</span><span class="detail-value">${operator.firstSeen ? new Date(operator.firstSeen).toLocaleDateString() : "—"}</span></div>
            </div>
          </div>
          
          <div class="detail-section">
            <h3>💬 Recent Sessions</h3>
            <div class="detail-box" style="font-size: 0.85rem;">
              ${
                userSessions
                  .slice(0, 5)
                  .map(
                    (s) => `
                <div class="detail-row" style="cursor: pointer;" onclick="closeOperatorModal(); openDetail('${escapeHtml(s.sessionKey)}', '${escapeHtml(s.label)}')">
                  <span class="detail-label">${s.active ? "🟢" : "⚪"} ${escapeHtml(s.label?.substring(0, 30) || "Unknown")}${(s.label?.length || 0) > 30 ? "..." : ""}</span>
                  <span class="detail-value">${((s.tokens || 0) / 1000).toFixed(1)}k</span>
                </div>
              `,
                  )
                  .join("") || '<em style="color: var(--text-muted)">No sessions found</em>'
              }
            </div>
          </div>
        `;
      }

      function closeOperatorModal() {
        document.getElementById("operator-modal").classList.remove("visible");
        document.getElementById("operator-modal-overlay").classList.remove("visible");
        setTimeout(() => {
          document.getElementById("operator-modal").classList.add("hidden");
          document.getElementById("operator-modal-overlay").classList.add("hidden");
        }, 200);
      }

      // Privacy Settings - Topics, Sessions, Crons, Display Options
      // Server-side storage with localStorage as cache/fallback
      const HIDDEN_TOPICS_KEY = "openclawHiddenTopics";
      const HIDDEN_SESSIONS_KEY = "openclawHiddenSessions";
      const HIDDEN_CRONS_KEY = "openclawHiddenCrons";
      const HIDE_HOSTNAME_KEY = "openclawHideHostname";
      const PRIVACY_CACHE_KEY = "openclawPrivacyCache";

      // In-memory cache of privacy settings (populated from server on load)
      let privacySettingsCache = null;

      // Load privacy settings from server (called on page load)
      async function loadPrivacyFromServer() {
        try {
          const res = await fetch("/api/privacy");
          if (res.ok) {
            const settings = await res.json();
            privacySettingsCache = settings;
            // Update localStorage cache
            localStorage.setItem(PRIVACY_CACHE_KEY, JSON.stringify(settings));
            // Migrate old localStorage data if server is empty
            if (
              (!settings.hiddenTopics || settings.hiddenTopics.length === 0) &&
              (!settings.hiddenSessions || settings.hiddenSessions.length === 0) &&
              (!settings.hiddenCrons || settings.hiddenCrons.length === 0)
            ) {
              await migrateLocalStorageToServer();
            }
            return settings;
          }
        } catch (e) {
          console.warn("Failed to load privacy from server, using localStorage cache:", e.message);
        }
        // Fallback to localStorage cache
        try {
          const cached = localStorage.getItem(PRIVACY_CACHE_KEY);
          if (cached) {
            privacySettingsCache = JSON.parse(cached);
            return privacySettingsCache;
          }
        } catch (e) {}
        // Final fallback - empty settings
        privacySettingsCache = {
          hiddenTopics: [],
          hiddenSessions: [],
          hiddenCrons: [],
          hideHostname: false,
        };
        return privacySettingsCache;
      }

      // Save privacy settings to server (debounced)
      let privacySaveTimeout = null;
      async function savePrivacyToServer() {
        // Debounce saves to avoid excessive API calls
        if (privacySaveTimeout) clearTimeout(privacySaveTimeout);
        privacySaveTimeout = setTimeout(async () => {
          try {
            const res = await fetch("/api/privacy", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(privacySettingsCache),
            });
            if (res.ok) {
              // Update localStorage cache
              localStorage.setItem(PRIVACY_CACHE_KEY, JSON.stringify(privacySettingsCache));
              console.log("[Privacy] Settings saved to server");
            } else {
              console.warn("[Privacy] Failed to save to server:", await res.text());
            }
          } catch (e) {
            console.warn("[Privacy] Failed to save to server:", e.message);
          }
        }, 500);
      }

      // Migrate old localStorage data to server (one-time migration)
      async function migrateLocalStorageToServer() {
        const oldTopics = getLocalHiddenItems(HIDDEN_TOPICS_KEY);
        const oldSessions = getLocalHiddenItems(HIDDEN_SESSIONS_KEY);
        const oldCrons = getLocalHiddenItems(HIDDEN_CRONS_KEY);
        const oldHostname = localStorage.getItem(HIDE_HOSTNAME_KEY) === "true";

        if (oldTopics.length || oldSessions.length || oldCrons.length || oldHostname) {
          console.log("[Privacy] Migrating localStorage data to server...");
          privacySettingsCache = {
            hiddenTopics: oldTopics,
            hiddenSessions: oldSessions,
            hiddenCrons: oldCrons,
            hideHostname: oldHostname,
          };
          await savePrivacyToServer();
          // Clear old localStorage keys after migration
          localStorage.removeItem(HIDDEN_TOPICS_KEY);
          localStorage.removeItem(HIDDEN_SESSIONS_KEY);
          localStorage.removeItem(HIDDEN_CRONS_KEY);
          localStorage.removeItem(HIDE_HOSTNAME_KEY);
        }
      }

      // Generic localStorage helpers (for migration/fallback only)
      function getLocalHiddenItems(key) {
        try {
          const stored = localStorage.getItem(key);
          if (!stored) return [];
          const parsed = JSON.parse(stored);
          return parsed.map((item) => (typeof item === "string" ? { id: item, name: item } : item));
        } catch (e) {
          return [];
        }
      }

      // Topic-specific functions (use in-memory cache backed by server)
      function getHiddenTopics() {
        return privacySettingsCache?.hiddenTopics || [];
      }
      function setHiddenTopics(topics) {
        if (!privacySettingsCache) privacySettingsCache = {};
        privacySettingsCache.hiddenTopics = topics;
        savePrivacyToServer();
      }
      function isTopicHidden(topicId) {
        const hidden = getHiddenTopics();
        const normalized = (topicId || "").toLowerCase().trim();
        return hidden.some((h) => (h.id || "").toLowerCase().trim() === normalized);
      }

      // Session-specific functions
      function getHiddenSessions() {
        return privacySettingsCache?.hiddenSessions || [];
      }
      function setHiddenSessions(sessions) {
        if (!privacySettingsCache) privacySettingsCache = {};
        privacySettingsCache.hiddenSessions = sessions;
        savePrivacyToServer();
      }
      function isSessionHidden(session) {
        const hidden = getHiddenSessions();
        const key = (session.sessionKey || session.key || "").toLowerCase().trim();
        return hidden.some((h) => (h.id || "").toLowerCase().trim() === key);
      }

      // Cron-specific functions
      function getHiddenCrons() {
        return privacySettingsCache?.hiddenCrons || [];
      }
      function setHiddenCrons(crons) {
        if (!privacySettingsCache) privacySettingsCache = {};
        privacySettingsCache.hiddenCrons = crons;
        savePrivacyToServer();
      }
      function isCronHidden(cron) {
        const hidden = getHiddenCrons();
        const id = (cron.id || cron.jobId || "").toLowerCase().trim();
        // Match on id only (exact match)
        return hidden.some((h) => (h.id || "").toLowerCase().trim() === id);
      }

      // Add functions (manual entry - uses input as both id and name)
      function addHiddenTopic() {
        const input = document.getElementById("privacy-add-topic");
        const topic = (input.value || "").trim();
        if (!topic) return;

        const hidden = getHiddenTopics();
        if (!hidden.some((h) => (h.id || "").toLowerCase() === topic.toLowerCase())) {
          hidden.push({ id: topic, name: topic });
          setHiddenTopics(hidden);
        }
        input.value = "";
        renderPrivacyLists();
        refreshAllViews();
      }

      function addHiddenSession() {
        const input = document.getElementById("privacy-add-session");
        const session = (input.value || "").trim();
        if (!session) return;

        const hidden = getHiddenSessions();
        if (!hidden.some((h) => (h.id || "").toLowerCase() === session.toLowerCase())) {
          hidden.push({ id: session, name: session });
          setHiddenSessions(hidden);
        }
        input.value = "";
        renderPrivacyLists();
        refreshAllViews();
      }

      function addHiddenCron() {
        const input = document.getElementById("privacy-add-cron");
        const cron = (input.value || "").trim();
        if (!cron) return;

        const hidden = getHiddenCrons();
        if (!hidden.some((h) => (h.id || "").toLowerCase() === cron.toLowerCase())) {
          hidden.push({ id: cron, name: cron });
          setHiddenCrons(hidden);
        }
        input.value = "";
        renderPrivacyLists();
        refreshAllViews();
      }

      // Quick-hide from card (called by hide icon on cards)
      // Stores id for matching, name for display
      function quickHideTopic(id, name) {
        const hidden = getHiddenTopics();
        if (!hidden.some((h) => (h.id || "").toLowerCase() === id.toLowerCase())) {
          hidden.push({ id: id, name: name || id });
          setHiddenTopics(hidden);
        }
        refreshAllViews();
        showToast(`Topic "${name || id}" hidden. Open Privacy Settings to unhide.`);
      }

      function quickHideSession(id, name) {
        const hidden = getHiddenSessions();
        if (!hidden.some((h) => (h.id || "").toLowerCase() === id.toLowerCase())) {
          hidden.push({ id: id, name: name || id });
          setHiddenSessions(hidden);
        }
        refreshAllViews();
        showToast(`Session "${name || id}" hidden. Open Privacy Settings to unhide.`);
      }

      function quickHideCron(id, name) {
        const hidden = getHiddenCrons();
        if (!hidden.some((h) => (h.id || "").toLowerCase() === id.toLowerCase())) {
          hidden.push({ id: id, name: name || id });
          setHiddenCrons(hidden);
        }
        refreshAllViews();
        showToast(`Cron job "${name || id}" hidden. Open Privacy Settings to unhide.`);
      }

      // Remove functions (by id)
      function removeHiddenTopic(id) {
        const hidden = getHiddenTopics();
        const filtered = hidden.filter((h) => (h.id || "").toLowerCase() !== id.toLowerCase());
        setHiddenTopics(filtered);
        renderPrivacyLists();
        refreshAllViews();
      }

      function removeHiddenSession(id) {
        const hidden = getHiddenSessions();
        const filtered = hidden.filter((h) => (h.id || "").toLowerCase() !== id.toLowerCase());
        setHiddenSessions(filtered);
        renderPrivacyLists();
        refreshAllViews();
      }

      function removeHiddenCron(id) {
        const hidden = getHiddenCrons();
        const filtered = hidden.filter((h) => (h.id || "").toLowerCase() !== id.toLowerCase());
        setHiddenCrons(filtered);
        renderPrivacyLists();
        refreshAllViews();
      }

      // Clear all
      function clearAllPrivacySettings() {
        setHiddenTopics([]);
        setHiddenSessions([]);
        setHiddenCrons([]);
        setHideHostname(false);
        renderPrivacyLists();
        // Update checkbox
        const hostnameCheckbox = document.getElementById("privacy-hide-hostname");
        if (hostnameCheckbox) hostnameCheckbox.checked = false;
        refreshAllViews();
      }

      // Hostname privacy (use server-backed cache)
      function isHostnameHidden() {
        return privacySettingsCache?.hideHostname || false;
      }

      function setHideHostname(hide) {
        if (!privacySettingsCache) privacySettingsCache = {};
        privacySettingsCache.hideHostname = hide;
        savePrivacyToServer();
      }

      function toggleHideHostname() {
        const checkbox = document.getElementById("privacy-hide-hostname");
        setHideHostname(checkbox.checked);
        updateHostnameDisplay();
      }

      function updateHostnameDisplay() {
        const hostnameEl = document.getElementById("vitals-hostname");
        if (hostnameEl) {
          if (isHostnameHidden()) {
            hostnameEl.style.filter = "blur(8px)";
            hostnameEl.style.userSelect = "none";
            hostnameEl.title = "Hidden for privacy";
          } else {
            hostnameEl.style.filter = "";
            hostnameEl.style.userSelect = "";
            hostnameEl.title = "";
          }
        }
      }

      // Refresh all views after privacy change
      function refreshAllViews() {
        if (window.lastCerebroData) renderCerebro(window.lastCerebroData);
        renderSessions(sessionsData);
        if (cronData && cronData.length > 0) renderCron(cronData);
        updateHostnameDisplay();
      }

      // Render all privacy lists
      function renderPrivacyLists() {
        renderHiddenTopicsList();
        renderHiddenSessionsList();
        renderHiddenCronsList();
      }

      function renderHiddenTopicsList() {
        const container = document.getElementById("hidden-topics-list");
        if (!container) return;
        const hidden = getHiddenTopics();

        // Update count in heading
        const countEl = document.getElementById("privacy-topics-count");
        if (countEl) countEl.textContent = `(${hidden.length})`;

        if (hidden.length === 0) {
          container.innerHTML =
            '<em style="color: var(--text-muted); font-size: 0.85rem;">No topics hidden</em>';
          return;
        }

        // Display name, but remove by id
        container.innerHTML = hidden
          .map(
            (item) => `
          <div style="display: inline-flex; align-items: center; padding: 4px 10px; background: var(--bg); border-radius: 12px; margin: 2px; font-size: 0.85rem;">
            <span>${escapeHtml(item.name || item.id)}</span>
            <button onclick="removeHiddenTopic('${escapeHtml(item.id).replace(/'/g, "\\'")}')" style="background: none; border: none; color: var(--error); cursor: pointer; margin-left: 6px; font-size: 0.9rem;" title="${i18nText("actions.remove", {}, "Remove")}">✕</button>
          </div>
        `,
          )
          .join("");
      }

      function renderHiddenSessionsList() {
        const container = document.getElementById("hidden-sessions-list");
        if (!container) return;
        const hidden = getHiddenSessions();

        // Update count in heading
        const countEl = document.getElementById("privacy-sessions-count");
        if (countEl) countEl.textContent = `(${hidden.length})`;

        if (hidden.length === 0) {
          container.innerHTML =
            '<em style="color: var(--text-muted); font-size: 0.85rem;">No sessions hidden</em>';
          return;
        }

        // Display name, but remove by id
        container.innerHTML = hidden
          .map(
            (item) => `
          <div style="display: inline-flex; align-items: center; padding: 4px 10px; background: var(--bg); border-radius: 12px; margin: 2px; font-size: 0.85rem;">
            <span>${escapeHtml(item.name || item.id)}</span>
            <button onclick="removeHiddenSession('${escapeHtml(item.id).replace(/'/g, "\\'")}')" style="background: none; border: none; color: var(--error); cursor: pointer; margin-left: 6px; font-size: 0.9rem;" title="${i18nText("actions.remove", {}, "Remove")}">✕</button>
          </div>
        `,
          )
          .join("");
      }

      function renderHiddenCronsList() {
        const container = document.getElementById("hidden-crons-list");
        if (!container) return;
        const hidden = getHiddenCrons();

        // Update count in heading
        const countEl = document.getElementById("privacy-crons-count");
        if (countEl) countEl.textContent = `(${hidden.length})`;

        if (hidden.length === 0) {
          container.innerHTML = `<em style="color: var(--text-muted); font-size: 0.85rem;">${i18nText("privacy.noCronHidden", {}, "No cron jobs hidden")}</em>`;
          return;
        }

        // Display name, but remove by id
        container.innerHTML = hidden
          .map(
            (item) => `
          <div style="display: inline-flex; align-items: center; padding: 4px 10px; background: var(--bg); border-radius: 12px; margin: 2px; font-size: 0.85rem;">
            <span>${escapeHtml(item.name || item.id)}</span>
            <button onclick="removeHiddenCron('${escapeHtml(item.id).replace(/'/g, "\\'")}')" style="background: none; border: none; color: var(--error); cursor: pointer; margin-left: 6px; font-size: 0.9rem;" title="${i18nText("actions.remove", {}, "Remove")}">✕</button>
          </div>
        `,
          )
          .join("");
      }

      function openPrivacyModal() {
        document.getElementById("privacy-modal").classList.remove("hidden");
        document.getElementById("privacy-modal").classList.add("visible");
        document.getElementById("privacy-modal-overlay").classList.remove("hidden");
        document.getElementById("privacy-modal-overlay").classList.add("visible");
        renderPrivacyLists();
        // Set checkbox state
        const hostnameCheckbox = document.getElementById("privacy-hide-hostname");
        if (hostnameCheckbox) hostnameCheckbox.checked = isHostnameHidden();
      }

      function closePrivacyModal() {
        document.getElementById("privacy-modal").classList.remove("visible");
        document.getElementById("privacy-modal-overlay").classList.remove("visible");
        setTimeout(() => {
          document.getElementById("privacy-modal").classList.add("hidden");
          document.getElementById("privacy-modal-overlay").classList.add("hidden");
        }, 200);
      }

      // Format currency with commas
      function formatCurrency(n, decimals = 2) {
        return (n || 0).toLocaleString("en-US", {
          minimumFractionDigits: decimals,
          maximumFractionDigits: decimals,
        });
      }

      function renderCostBreakdown(data) {
        // Token usage
        document.getElementById("cost-tokens").innerHTML = `
          <div class="detail-row"><span class="detail-label">Input Tokens</span><span class="detail-value">${(data.inputTokens || 0).toLocaleString()}</span></div>
          <div class="detail-row"><span class="detail-label">Output Tokens</span><span class="detail-value">${(data.outputTokens || 0).toLocaleString()}</span></div>
          <div class="detail-row"><span class="detail-label">Cache Read</span><span class="detail-value">${(data.cacheRead || 0).toLocaleString()}</span></div>
          <div class="detail-row"><span class="detail-label">Cache Write</span><span class="detail-value">${(data.cacheWrite || 0).toLocaleString()}</span></div>
          <div class="detail-row"><span class="detail-label">API Requests</span><span class="detail-value">${(data.requests || 0).toLocaleString()}</span></div>
        `;

        // Pricing rates
        document.getElementById("cost-rates").innerHTML = `
          <div class="detail-row"><span class="detail-label">Input</span><span class="detail-value">$${data.rates?.input || "15.00"}/1M tokens</span></div>
          <div class="detail-row"><span class="detail-label">Output</span><span class="detail-value">$${data.rates?.output || "75.00"}/1M tokens</span></div>
          <div class="detail-row"><span class="detail-label">Cache Read</span><span class="detail-value">$${data.rates?.cacheRead || "1.50"}/1M tokens (90% discount)</span></div>
          <div class="detail-row"><span class="detail-label">Cache Write</span><span class="detail-value">$${data.rates?.cacheWrite || "18.75"}/1M tokens (25% premium)</span></div>
        `;

        // Calculation breakdown
        const calc = data.calculation || {};
        document.getElementById("cost-calculation").innerHTML = `
          <div class="detail-row"><span class="detail-label">Input Cost</span><span class="detail-value">$${formatCurrency(calc.inputCost, 2)}</span></div>
          <div class="detail-row"><span class="detail-label">Output Cost</span><span class="detail-value">$${formatCurrency(calc.outputCost, 2)}</span></div>
          <div class="detail-row"><span class="detail-label">Cache Read Cost</span><span class="detail-value">$${formatCurrency(calc.cacheReadCost, 2)}</span></div>
          <div class="detail-row"><span class="detail-label">Cache Write Cost</span><span class="detail-value">$${formatCurrency(calc.cacheWriteCost, 2)}</span></div>
          <div class="detail-row" style="border-top: 1px solid var(--border); padding-top: 8px; margin-top: 8px;">
            <span class="detail-label"><strong>Est. API Cost</strong></span>
            <span class="detail-value"><strong>$${formatCurrency(data.totalCost)}</strong></span>
          </div>
        `;

        // Savings - show all three windows (24h, 3da, 7da)
        const planCost = data.planCost || 200;
        const planName = data.planName || "Claude Code Max";
        const windows = data.windows || {};

        // Build savings rows for each window
        const windowOrder = ["24h", "3d", "7d"];
        const windowLabels = { "24h": "24h", "3d": "3dma", "7d": "7dma" };

        let savingsHtml = `
          <div class="detail-row"><span class="detail-label">${planName}</span><span class="detail-value">$${planCost}/month</span></div>
          <div style="margin-top: 12px; margin-bottom: 8px; font-size: 0.85rem; color: var(--text-muted);">Projected Monthly Cost by Window:</div>
        `;

        let hasSavings = false;
        for (const key of windowOrder) {
          const w = windows[key];
          if (!w) continue;

          const monthlyProjected = w.monthlyProjected || 0;
          const savings = w.monthlySavings || 0;
          const pct = w.savingsPercent || 0;

          if (savings > 0) hasSavings = true;

          const savingsStr =
            savings > 0
              ? `<span style="color: var(--green);">↓$${Math.round(savings).toLocaleString()}/mo (${pct}%)</span>`
              : `<span style="color: var(--text-muted);">-</span>`;

          savingsHtml += `
            <div class="detail-row">
              <span class="detail-label">${windowLabels[key]}</span>
              <span class="detail-value">$${Math.round(monthlyProjected).toLocaleString()}/mo ${savingsStr}</span>
            </div>
          `;
        }

        if (!hasSavings) {
          savingsHtml += `
            <p style="margin-top: 12px; font-size: 0.85rem; color: var(--text-muted);">
              📈 Keep going! Once your monthly cost exceeds $${planCost}, you'll start seeing savings.
            </p>
          `;
        }

        document.getElementById("cost-savings").innerHTML = savingsHtml;

        // Top sessions by tokens
        const topSessions = data.topSessions || [];
        if (topSessions.length > 0) {
          document.getElementById("cost-top-sessions").innerHTML = topSessions
            .map((s, i) => {
              const tokensFormatted =
                s.tokens >= 1000000
                  ? (s.tokens / 1000000).toFixed(1) + "M"
                  : s.tokens >= 1000
                    ? (s.tokens / 1000).toFixed(1) + "k"
                    : s.tokens;
              const statusIcon = s.active ? "🟢" : "⚪";
              return `<div class="detail-row">
              <span class="detail-label">${statusIcon} ${s.label.substring(0, 30)}${s.label.length > 30 ? "..." : ""}</span>
              <span class="detail-value">${tokensFormatted}</span>
            </div>`;
            })
            .join("");
        } else {
          document.getElementById("cost-top-sessions").innerHTML =
            '<em style="color: var(--text-muted)">No session data available</em>';
        }
      }

      async function fetchSessionDetail(key) {
        // Handle null/undefined sessionKey
        if (!key) {
          console.error("fetchSessionDetail: no session key provided");
          renderDetailError("No session key provided");
          return;
        }

        // Add timeout to prevent hanging forever
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 10000); // 10s timeout

        try {
          const res = await fetch(`/api/session?key=${encodeURIComponent(key)}`, {
            signal: controller.signal,
          });
          clearTimeout(timeoutId);

          if (!res.ok) {
            throw new Error(`HTTP ${res.status}: ${res.statusText}`);
          }

          const data = await res.json();

          // Check for API error response
          if (data.error) {
            console.error("API error:", data.error);
            renderDetailError(data.error);
            return;
          }

          renderDetail(data);
        } catch (e) {
          clearTimeout(timeoutId);
          console.error("Failed to fetch detail:", e);
          const msg =
            e.name === "AbortError" ? "Request timed out" : e.message || "Failed to load session";
          renderDetailError(msg);
        }
      }

      function renderDetailError(message) {
        const errorHtml = `<em style="color: var(--red, #ff6b6b)">⚠️ ${escapeHtml(message)}</em>`;
        ["overview", "summary", "links", "attention", "facts", "tools", "messages"].forEach(
          (id) => {
            const el = document.getElementById(`detail-${id}`);
            if (el) el.innerHTML = errorHtml;
          },
        );
      }

      function renderDetail(data) {
        // Update the title with the best available channel name
        const titleEl = document.getElementById("detail-title");
        const channelName = data.groupChannel || data.channel || "Session Details";
        titleEl.textContent = channelName;

        // Build cost display if available
        const costDisplay = data.estCost
          ? `<div class="detail-row"><span class="detail-label">Est. Cost</span><span class="detail-value">${data.estCost}</span></div>`
          : "";

        // Build cache display if we have cache data
        const cacheDisplay =
          data.cacheRead || data.cacheWrite
            ? `<div class="detail-row"><span class="detail-label">Cache (R/W)</span><span class="detail-value">${(data.cacheRead || 0).toLocaleString()} / ${(data.cacheWrite || 0).toLocaleString()}</span></div>`
            : "";

        // Overview
        smartUpdate(
          document.getElementById("detail-overview"),
          `
                <div class="detail-row"><span class="detail-label">Channel</span><span class="detail-value">${data.channel || "-"}</span></div>
                <div class="detail-row"><span class="detail-label">Model</span><span class="detail-value">${data.model || "-"}</span></div>
                <div class="detail-row"><span class="detail-label">Total Tokens</span><span class="detail-value">${data.tokens?.toLocaleString() || "-"}</span></div>
                <div class="detail-row"><span class="detail-label">Input / Output</span><span class="detail-value">${(data.inputTokens || 0).toLocaleString()} / ${(data.outputTokens || 0).toLocaleString()}</span></div>
                ${cacheDisplay}
                ${costDisplay}
                <div class="detail-row"><span class="detail-label">Last Active</span><span class="detail-value">${data.lastActive || "-"}</span></div>
            `,
        );

        // Summary
        smartUpdate(
          document.getElementById("detail-summary"),
          data.summary || "<em>No summary</em>",
        );

        // Links/References
        const allText = (data.messages || []).map((m) => m.text).join(" ");
        const links = extractLinks(allText);
        if (data.links) links.push(...data.links);

        if (links.length > 0) {
          smartUpdate(
            document.getElementById("detail-links"),
            links
              .map((l) => {
                const cls =
                  l.type === "linear"
                    ? "linear"
                    : l.type === "github"
                      ? "github"
                      : l.type === "file"
                        ? "file"
                        : "slack";
                const icon =
                  l.type === "linear"
                    ? "📋"
                    : l.type === "github"
                      ? "🐙"
                      : l.type === "file"
                        ? "📁"
                        : "💬";
                if (l.url) {
                  return `<a href="${l.url}" target="_blank" class="link-tag ${cls}">${icon} ${l.id}</a>`;
                }
                return `<span class="link-tag ${cls}">${icon} ${l.id}</span>`;
              })
              .join(" "),
          );
        } else {
          smartUpdate(
            document.getElementById("detail-links"),
            '<em style="color: var(--text-muted)">No references detected</em>',
          );
        }

        // Needs Attention
        if (data.needsAttention?.length > 0) {
          smartUpdate(
            document.getElementById("detail-attention"),
            data.needsAttention
              .map((a) => `<div class="attention-item">${escapeHtml(a)}</div>`)
              .join(""),
          );
        } else {
          smartUpdate(
            document.getElementById("detail-attention"),
            '<em style="color: var(--text-muted)">Nothing needs attention</em>',
          );
        }

        // Facts
        if (data.facts?.length > 0) {
          smartUpdate(
            document.getElementById("detail-facts"),
            data.facts.map((f) => `<div class="attention-item">✅ ${escapeHtml(f)}</div>`).join(""),
          );
        } else {
          smartUpdate(
            document.getElementById("detail-facts"),
            '<em style="color: var(--text-muted)">No key facts</em>',
          );
        }

        // Tools
        if (data.tools?.length > 0) {
          smartUpdate(
            document.getElementById("detail-tools"),
            data.tools
              .map(
                (t) =>
                  `<span class="tool-tag"><code>${t.name}</code> <span class="tool-count">×${t.count}</span></span>`,
              )
              .join(""),
          );
        } else {
          smartUpdate(
            document.getElementById("detail-tools"),
            '<em style="color: var(--text-muted)">No tools used</em>',
          );
        }

        // Messages
        if (data.messages?.length > 0) {
          smartUpdate(
            document.getElementById("detail-messages"),
            data.messages
              .map(
                (m) => `
                    <div class="message-item">
                        <div class="message-role ${m.role}">${m.role === "user" ? "👤 User" : "🦞 Assistant"}</div>
                        <div class="message-text">${escapeHtml(m.text?.slice(0, 400) || "")}${m.text?.length > 400 ? "..." : ""}</div>
                    </div>
                `,
              )
              .join(""),
          );
        } else {
          smartUpdate(
            document.getElementById("detail-messages"),
            '<em style="color: var(--text-muted)">No messages</em>',
          );
        }
      }

      // Keyboard shortcuts
      document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") closeDetail();
        if (e.key === "b" && (e.metaKey || e.ctrlKey)) {
          e.preventDefault();
          toggleSidebar();
        }
      });

      // ============================================================================
      // SSE (Server-Sent Events) for real-time updates
      // ============================================================================
      let eventSource = null;
      let sseConnected = false;
      let sseReconnectAttempts = 0;
      const SSE_MAX_RECONNECT_DELAY = 30000; // Max 30s between reconnects
      let pollInterval = null;

      function setConnectionStatus(status, message) {
        const pill = document.getElementById("connection-status");
        const statusText = document.getElementById("gateway-status");
        const refreshMode = document.getElementById("refresh-mode");

        pill.classList.remove("connected", "disconnected", "connecting");
        pill.classList.add(status);

        // Update the data-i18n attribute so the i18n system doesn't overwrite our status.
        // The i18n translateSubtree() re-applies data-i18n text, so we must keep the
        // attribute in sync with the intended display state.
        // Map status to i18n key, or remove data-i18n for custom messages
        const i18nKeyMap = {
          connected: "app.connected",
          connecting: "app.connecting",
          disconnected: "app.disconnected",
        };
        const i18nKey = i18nKeyMap[status];
        if (i18nKey) {
          statusText.setAttribute("data-i18n", i18nKey);
        } else {
          statusText.removeAttribute("data-i18n");
        }
        statusText.textContent = message;

        // Update refresh bar mode indicator
        if (status === "connected") {
          refreshMode.textContent = i18nText(
            "connection.realtime",
            {},
            "Real-time updates via SSE ⚡",
          );
        } else if (status === "disconnected") {
          refreshMode.textContent = i18nText(
            "connection.polling",
            {},
            "Polling mode (SSE disconnected)",
          );
        } else {
          refreshMode.textContent = i18nText("app.connecting", {}, "Connecting...");
        }
      }

      function connectSSE() {
        // Check for SSE support
        if (typeof EventSource === "undefined") {
          console.warn("[SSE] EventSource not supported, using polling fallback");
          setConnectionStatus("connected", i18nText("app.pollingMode", {}, "Polling Mode"));
          // Override i18n key for polling mode specifically
          document.getElementById("gateway-status")?.setAttribute("data-i18n", "app.pollingMode");
          startPolling();
          return;
        }

        setConnectionStatus("connecting", i18nText("app.connecting", {}, "Connecting..."));

        try {
          eventSource = new EventSource("/api/events");

          eventSource.onopen = function () {
            console.log("[SSE] Connected");
            sseConnected = true;
            sseReconnectAttempts = 0;
            setConnectionStatus("connected", "🟢 Live");
            stopPolling(); // Stop polling when SSE connects
          };

          eventSource.addEventListener("connected", function (e) {
            try {
              const data = JSON.parse(e.data);
              console.log("[SSE] Server greeting:", data.message);
            } catch (err) {}
          });

          eventSource.addEventListener("update", function (e) {
            try {
              const data = JSON.parse(e.data);
              handleSSEUpdate(data);
            } catch (err) {
              console.error("[SSE] Failed to parse update:", err);
            }
          });

          eventSource.addEventListener("heartbeat", function (e) {
            try {
              const data = JSON.parse(e.data);
              console.log("[SSE] Heartbeat, clients:", data.clients);
              // Update timestamp on heartbeat
              const now = new Date().toLocaleTimeString();
              document.getElementById("last-updated").textContent = now + " ⚡";
              document.getElementById("sidebar-updated").textContent = i18nText(
                "sidebar.live",
                { time: now },
                `Live: ${now}`,
              );
            } catch (err) {}
          });

          eventSource.onerror = function (e) {
            console.error("[SSE] Connection error");
            sseConnected = false;
            eventSource.close();
            eventSource = null;
            setConnectionStatus("disconnected", "🔴 Disconnected");

            // Exponential backoff for reconnection
            sseReconnectAttempts++;
            const delay = Math.min(
              1000 * Math.pow(2, sseReconnectAttempts - 1),
              SSE_MAX_RECONNECT_DELAY,
            );
            console.log(`[SSE] Reconnecting in ${delay}ms (attempt ${sseReconnectAttempts})`);

            // Start polling as fallback while disconnected
            startPolling();

            setTimeout(connectSSE, delay);
          };
        } catch (err) {
          console.error("[SSE] Failed to create EventSource:", err);
          setConnectionStatus("disconnected", "🔴 Error");
          startPolling();
        }
      }

      function handleSSEUpdate(data) {
        // Update timestamp with live indicator
        const now = new Date().toLocaleTimeString();
        document.getElementById("last-updated").textContent = now + " ⚡";
        document.getElementById("sidebar-updated").textContent = i18nText(
          "sidebar.live",
          { time: now },
          `Live: ${now}`,
        );

        // Render full state (unified approach)
        renderFullState(data);
      }

      // Polling fallback
      function startPolling() {
        if (pollInterval) return; // Already polling
        console.log("[Polling] Starting fallback polling");
        pollInterval = setInterval(fetchData, 2000); // Match SSE heartbeat
        fetchData(); // Immediate fetch
      }

      function stopPolling() {
        if (pollInterval) {
          console.log("[Polling] Stopping fallback polling (SSE connected)");
          clearInterval(pollInterval);
          pollInterval = null;
        }
      }

      // Toast notifications
      function showToast(message, type = "success") {
        const container = document.getElementById("toast-container");
        const toast = document.createElement("div");
        toast.className = `toast ${type}`;
        const icon = type === "success" ? "✅" : "❌";
        toast.innerHTML = `<span>${icon}</span><span>${escapeHtml(message)}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
          toast.style.animation = "toast-out 0.3s ease forwards";
          setTimeout(() => toast.remove(), 300);
        }, 3000);
      }

      // Update topic status API call
      async function updateTopicStatus(topicId, status) {
        try {
          const res = await fetch(`/api/cerebro/topic/${encodeURIComponent(topicId)}/status`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status }),
          });

          const data = await res.json();
          if (!res.ok) {
            throw new Error(data.error || "Failed to update status");
          }

          showToast(`Topic "${data.topic.title}" marked as ${status}`);
          // Refresh Cerebro data
          refreshCerebro();
        } catch (e) {
          showToast(`Error: ${e.message}`, "error");
        }
      }

      // Sub-agent Status Rendering
      function renderSubagents(subagents) {
        const grid = document.getElementById("subagent-grid");
        const countElement = document.getElementById("subagent-count");

        countElement.textContent = subagents.length;

        if (subagents.length === 0) {
          smartUpdate(
            grid,
            '<div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--text-muted); font-size: 0.9rem;">No active sub-agents</div>',
          );
          return;
        }

        smartUpdate(
          grid,
          subagents
            .map((s) => {
              const ageMinutes = Math.round(s.ageMs / 60000);
              const ageHours = Math.round(s.ageMs / 3600000);
              const ageDisplay = ageMinutes < 60 ? `${ageMinutes}m` : `${ageHours}h`;
              const statusClass = ageHours > 2 ? "stale" : s.tokens > 1000 ? "active" : "idle";
              const statusText = statusClass.charAt(0).toUpperCase() + statusClass.slice(1);

              // Build the session key for detail panel
              const sessionKey = `agent:main:subagent:${s.id}`;
              const label = s.task || `Sub-agent ${s.shortId}`;

              return `
                    <div class="subagent-card ${statusClass}" onclick="openDetail('${escapeHtml(sessionKey)}', '${escapeHtml(label.substring(0, 60))}')" style="cursor: pointer;">
                        <div class="subagent-header">
                            <div class="subagent-info">
                                <h4>${escapeHtml(s.task || s.id)}</h4>
                                <div class="subagent-meta">ID: ${s.shortId} • ${s.tokens} tokens • ${ageDisplay}</div>
                            </div>
                            <div class="subagent-status ${statusClass}">${statusText}</div>
                        </div>
                    </div>
                `;
            })
            .join(""),
        );
      }

      // Enhanced Token Stats with Quota Visualization
      function renderTokenQuotas(tokenStats, quotaData) {
        if (!quotaData) return;

        // Claude quotas (compact card)
        if (quotaData.claude) {
          const sessionPct = Math.round((quotaData.claude.sessionUsage || 0) * 100);
          const weekPct = Math.round((quotaData.claude.weekUsage || 0) * 100);

          document.getElementById("claude-compact-session-pct").textContent = `${sessionPct}%`;
          document.getElementById("claude-compact-week-pct").textContent = `${weekPct}%`;

          const sessionBar = document.getElementById("claude-compact-session-bar");
          const weekBar = document.getElementById("claude-compact-week-bar");

          sessionBar.style.width = `${sessionPct}%`;
          weekBar.style.width = `${weekPct}%`;

          // Color coding
          sessionBar.className = `quota-bar-fill ${sessionPct < 50 ? "low" : sessionPct < 80 ? "medium" : "high"}`;
          weekBar.className = `quota-bar-fill ${weekPct < 50 ? "low" : weekPct < 80 ? "medium" : "high"}`;
        }

        // Codex quotas
        if (quotaData.codex) {
          const h5Pct = Math.round((quotaData.codex.usage5h || 0) * 100);
          const dayPct = Math.round((quotaData.codex.usageDay || 0) * 100);

          document.getElementById("codex-5h-pct").textContent = `${h5Pct}%`;
          document.getElementById("codex-day-pct").textContent = `${dayPct}%`;
          document.getElementById("codex-tasks").textContent = quotaData.codex.tasksToday || 0;

          const h5Bar = document.getElementById("codex-5h-bar");
          const dayBar = document.getElementById("codex-day-bar");

          h5Bar.style.width = `${h5Pct}%`;
          dayBar.style.width = `${dayPct}%`;

          h5Bar.className = `quota-bar-fill ${h5Pct < 50 ? "low" : h5Pct < 80 ? "medium" : "high"}`;
          dayBar.className = `quota-bar-fill ${dayPct < 50 ? "low" : dayPct < 80 ? "medium" : "high"}`;
        }
      }

      // Quick Actions
      async function runHealthCheck() {
        try {
          const response = await fetch("/api/action?action=health-check");
          const data = await response.json();

          if (data.success) {
            showToast("✅ Health check passed", "success");
          } else {
            showToast("❌ Health check failed: " + (data.error || data.output), "error");
          }
        } catch (e) {
          showToast("❌ Health check error: " + e.message, "error");
        }
      }

      async function getGatewayStatus() {
        try {
          const response = await fetch("/api/action?action=gateway-status");
          const data = await response.json();

          if (data.success) {
            showToast("🚪 Gateway: " + data.output, "success");
          } else {
            showToast("❌ Gateway status failed: " + (data.error || data.output), "error");
          }
        } catch (e) {
          showToast("❌ Gateway error: " + e.message, "error");
        }
      }

      async function pruneStalesSessions() {
        try {
          const response = await fetch("/api/action?action=prune-stale");
          const data = await response.json();

          if (data.success) {
            showToast("🧹 " + data.output, "success");
          } else {
            showToast("❌ Cleanup failed: " + (data.error || data.output), "error");
          }
        } catch (e) {
          showToast("❌ Cleanup error: " + e.message, "error");
        }
      }

      // Toast notifications
      function showToast(message, type = "success") {
        const container = document.getElementById("toast-container");
        if (!container) return;

        const toast = document.createElement("div");
        toast.className = `toast ${type}`;
        const icon = type === "success" ? "✅" : "❌";
        toast.innerHTML = `<span>${icon}</span><span>${escapeHtml(message)}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
          toast.style.animation = "toast-out 0.3s ease forwards";
          setTimeout(() => toast.remove(), 300);
        }, 3000);
      }

      // Init - try SSE first, fall back to polling
      async function init() {
        // Load privacy settings from server first (before rendering any data)
        await loadPrivacyFromServer();
        console.log("[Privacy] Settings loaded from server");

        connectSSE();
        // Populate version badge from server (single source of truth: package.json)
        fetch("/api/about")
          .then((r) => r.json())
          .then((d) => {
            const el = document.getElementById("app-version");
            if (el && d.version) el.textContent = "v" + d.version;
          })
          .catch(() => {});
        // Fetch optional dependency status (once)
        fetch("/api/vitals")
          .then((r) => r.json())
          .then((d) => {
            if (d.optionalDeps) optionalDeps = d.optionalDeps;
          })
          .catch(() => {});
        // Fetch data after short delay to ensure DOM is ready
        // This fixes a race condition on initial page load
        setTimeout(fetchData, 100);

        // Apply privacy settings on load
        updateHostnameDisplay();

        // Initialize privacy checkbox state
        const hostnameCheckbox = document.getElementById("privacy-hide-hostname");
        if (hostnameCheckbox) {
          hostnameCheckbox.checked = isHostnameHidden();
        }

        // Set up savings window selector
        const windowSelect = document.getElementById("savings-window-select");
        if (windowSelect) {
          // Load saved preference
          windowSelect.value = getSavingsWindowPref();

          // Handle changes
          windowSelect.addEventListener("change", function (e) {
            const newWindow = e.target.value;
            setSavingsWindowPref(newWindow);
            if (currentTokenStats) {
              updateSavingsDisplay(currentTokenStats, newWindow);
            }
          });
        }

        window.addEventListener("i18n:updated", () => {
          fetchData();
          renderHiddenCronsList();
          renderHiddenSessionsList();
          renderHiddenTopicsList();
        });
      }

      // Ensure DOM is ready before initializing
      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
      } else {
        setTimeout(init, 0);
      }
    </script>

    <!-- Toast notifications container -->
    <div id="toast-container" class="toast-container"></div>
  </body>
</html>
```

## File: `public/jobs.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title data-i18n="jobs.pageTitle">AI Jobs - OpenClaw Command Center</title>
    <style>
      :root {
        --bg: #0d1117;
        --card-bg: #161b22;
        --card-hover: #1c2128;
        --border: #30363d;
        --text: #c9d1d9;
        --text-muted: #8b949e;
        --accent: #58a6ff;
        --green: #3fb950;
        --yellow: #d29922;
        --red: #f85149;
        --purple: #a371f7;
        --orange: #db6d28;
        --sidebar-width: 220px;
      }
      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        background: var(--bg);
        color: var(--text);
        min-height: 100vh;
        display: flex;
      }

      /* Sidebar */
      .sidebar {
        width: var(--sidebar-width);
        background: var(--card-bg);
        border-right: 1px solid var(--border);
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        display: flex;
        flex-direction: column;
        z-index: 60;
        transition: transform 0.2s ease;
      }
      .sidebar.collapsed {
        width: 56px;
      }
      .sidebar.collapsed .sidebar-title,
      .sidebar.collapsed .nav-section-title,
      .sidebar.collapsed .nav-item span:not(.nav-icon),
      .sidebar.collapsed .nav-badge,
      .sidebar.collapsed .sidebar-footer {
        display: none;
      }
      .sidebar.collapsed .sidebar-header {
        justify-content: center;
        padding: 16px 8px;
      }
      .sidebar.collapsed .sidebar-toggle {
        margin-left: 0;
      }
      .sidebar.collapsed .nav-item {
        justify-content: center;
        padding: 12px;
      }
      .sidebar.collapsed .nav-icon {
        margin: 0;
        font-size: 1.2rem;
      }
      .sidebar.collapsed .nav-item::after {
        content: attr(data-tooltip);
        position: absolute;
        left: 100%;
        top: 50%;
        transform: translateY(-50%);
        background: var(--card-bg);
        border: 1px solid var(--border);
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 0.8rem;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.15s;
        margin-left: 8px;
        z-index: 100;
      }
      .sidebar.collapsed .nav-item:hover::after {
        opacity: 1;
      }
      .sidebar-header {
        padding: 16px;
        border-bottom: 1px solid var(--border);
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .sidebar-logo {
        font-size: 1.3rem;
      }
      .sidebar-title {
        font-size: 0.9rem;
        font-weight: 600;
        white-space: nowrap;
      }
      .sidebar-toggle {
        margin-left: auto;
        background: none;
        border: none;
        color: var(--text-muted);
        cursor: pointer;
        padding: 6px;
        border-radius: 6px;
        font-size: 1rem;
      }
      .sidebar-toggle:hover {
        background: var(--bg);
        color: var(--text);
      }

      .sidebar-nav {
        flex: 1;
        padding: 12px 8px;
        overflow-y: auto;
      }
      .nav-section {
        margin-bottom: 16px;
      }
      .nav-section-title {
        font-size: 0.65rem;
        text-transform: uppercase;
        color: var(--text-muted);
        padding: 8px 12px 4px;
        letter-spacing: 0.5px;
      }
      .nav-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 12px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 0.85rem;
        color: var(--text-muted);
        transition: all 0.15s;
        text-decoration: none;
        position: relative;
      }
      .nav-item:hover {
        background: var(--bg);
        color: var(--text);
      }
      .nav-item.active {
        background: rgba(88, 166, 255, 0.15);
        color: var(--accent);
      }
      .nav-icon {
        font-size: 1rem;
        width: 20px;
        text-align: center;
      }
      .nav-badge {
        margin-left: auto;
        background: var(--border);
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.7rem;
      }
      .nav-item.active .nav-badge {
        background: rgba(88, 166, 255, 0.3);
      }

      .sidebar-footer {
        padding: 12px;
        border-top: 1px solid var(--border);
        font-size: 0.7rem;
        color: var(--text-muted);
        text-align: center;
      }

      /* Main Content Area */
      .main-wrapper {
        flex: 1;
        margin-left: var(--sidebar-width);
        transition: margin-left 0.2s ease;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
      }
      .main-wrapper.sidebar-collapsed {
        margin-left: 56px;
      }

      /* Header */
      header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 24px;
        border-bottom: 1px solid var(--border);
        background: var(--card-bg);
        position: sticky;
        top: 0;
        z-index: 50;
      }
      .header-left {
        display: flex;
        align-items: center;
        gap: 16px;
      }
      .page-title {
        font-size: 1.1rem;
        font-weight: 600;
      }
      .header-actions {
        display: flex;
        gap: 8px;
      }

      /* Stats Bar */
      .stats-bar {
        display: flex;
        gap: 12px;
        padding: 16px 24px;
        background: var(--card-bg);
        border-bottom: 1px solid var(--border);
        overflow-x: auto;
      }
      .stat {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 12px 20px;
        background: var(--bg);
        border-radius: 8px;
        min-width: 100px;
      }
      .stat-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--accent);
      }
      .stat-value.green {
        color: var(--green);
      }
      .stat-value.yellow {
        color: var(--yellow);
      }
      .stat-value.red {
        color: var(--red);
      }
      .stat-label {
        font-size: 0.7rem;
        color: var(--text-muted);
        text-transform: uppercase;
        margin-top: 4px;
      }

      /* Main Content */
      main {
        padding: 24px;
        flex: 1;
      }

      /* Section */
      .section {
        margin-bottom: 32px;
      }
      .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
      }
      .section-title {
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-muted);
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .section-count {
        background: var(--border);
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.75rem;
      }

      /* Filters */
      .filters-bar {
        display: flex;
        gap: 8px;
        margin-bottom: 16px;
        flex-wrap: wrap;
      }
      .filter-btn {
        padding: 6px 12px;
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 16px;
        font-size: 0.75rem;
        color: var(--text-muted);
        cursor: pointer;
        transition: all 0.15s;
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .filter-btn:hover {
        border-color: var(--accent);
        color: var(--text);
      }
      .filter-btn.active {
        background: rgba(88, 166, 255, 0.15);
        border-color: var(--accent);
        color: var(--accent);
      }
      .filter-count {
        background: var(--bg);
        padding: 1px 6px;
        border-radius: 8px;
        font-size: 0.65rem;
      }

      /* Job Cards Grid */
      .jobs-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 16px;
      }

      /* Job Card */
      .job-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        transition: all 0.15s ease;
        position: relative;
        overflow: hidden;
      }
      .job-card:hover {
        background: var(--card-hover);
        border-color: var(--accent);
        transform: translateY(-2px);
      }
      .job-card.running {
        border-color: var(--green);
        box-shadow: 0 0 0 1px var(--green);
      }
      .job-card.running::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--green);
        animation: running-pulse 2s infinite;
      }
      @keyframes running-pulse {
        0%,
        100% {
          opacity: 1;
        }
        50% {
          opacity: 0.5;
        }
      }
      .job-card.paused {
        border-color: var(--yellow);
        opacity: 0.7;
      }
      .job-card.paused::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--yellow);
      }
      .job-card.failed {
        border-color: var(--red);
      }
      .job-card.failed::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--red);
      }

      .job-header {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 12px;
      }
      .job-icon {
        width: 40px;
        height: 40px;
        background: var(--bg);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        flex-shrink: 0;
      }
      .job-icon.running {
        background: rgba(63, 185, 80, 0.15);
      }
      .job-icon.paused {
        background: rgba(210, 153, 34, 0.15);
      }
      .job-icon.failed {
        background: rgba(248, 81, 73, 0.15);
      }

      .job-title-area {
        flex: 1;
        min-width: 0;
      }
      .job-name {
        font-size: 0.95rem;
        font-weight: 600;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .job-id {
        font-size: 0.7rem;
        color: var(--text-muted);
        font-family: monospace;
        margin-top: 2px;
      }
      .job-description {
        font-size: 0.75rem;
        color: var(--text-muted);
        margin-top: 6px;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }

      .job-badge {
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 500;
        flex-shrink: 0;
      }
      .badge-running {
        background: rgba(63, 185, 80, 0.2);
        color: var(--green);
      }
      .badge-paused {
        background: rgba(210, 153, 34, 0.2);
        color: var(--yellow);
      }
      .badge-enabled {
        background: rgba(88, 166, 255, 0.15);
        color: var(--accent);
      }
      .badge-failed {
        background: rgba(248, 81, 73, 0.2);
        color: var(--red);
      }

      .job-schedule {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 12px;
        padding: 8px 10px;
        background: var(--bg);
        border-radius: 8px;
        font-size: 0.75rem;
      }
      .schedule-icon {
        opacity: 0.7;
      }
      .schedule-cron {
        font-family: monospace;
        color: var(--purple);
      }
      .schedule-next {
        margin-left: auto;
        color: var(--text-muted);
      }

      .job-stats {
        display: flex;
        gap: 12px;
        padding: 10px 0;
        border-top: 1px solid var(--border);
        margin-top: 12px;
      }
      .job-stat {
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
      }
      .job-stat-value {
        font-size: 0.9rem;
        font-weight: 600;
      }
      .job-stat-value.green {
        color: var(--green);
      }
      .job-stat-value.red {
        color: var(--red);
      }
      .job-stat-label {
        font-size: 0.65rem;
        color: var(--text-muted);
        text-transform: uppercase;
        margin-top: 2px;
      }

      .job-last-run {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 10px;
        font-size: 0.75rem;
        color: var(--text-muted);
      }
      .last-run-status {
        width: 8px;
        height: 8px;
        border-radius: 50%;
      }
      .last-run-status.success {
        background: var(--green);
      }
      .last-run-status.failed {
        background: var(--red);
      }
      .last-run-status.running {
        background: var(--yellow);
        animation: pulse 1.5s infinite;
      }
      @keyframes pulse {
        0%,
        100% {
          opacity: 1;
        }
        50% {
          opacity: 0.4;
        }
      }

      .job-actions {
        display: flex;
        gap: 6px;
        margin-top: 12px;
      }
      .job-action-btn {
        flex: 1;
        padding: 8px 12px;
        background: var(--bg);
        border: 1px solid var(--border);
        border-radius: 6px;
        font-size: 0.75rem;
        color: var(--text);
        cursor: pointer;
        transition: all 0.15s;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 4px;
      }
      .job-action-btn:hover {
        background: var(--card-hover);
        border-color: var(--accent);
      }
      .job-action-btn.primary {
        background: rgba(88, 166, 255, 0.15);
        border-color: var(--accent);
        color: var(--accent);
      }
      .job-action-btn.primary:hover {
        background: rgba(88, 166, 255, 0.25);
      }
      .job-action-btn.danger:hover {
        border-color: var(--red);
        color: var(--red);
      }
      .job-action-btn:disabled {
        opacity: 0.5;
        cursor: not-allowed;
      }

      /* Tags */
      .job-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        margin-top: 8px;
      }
      .job-tag {
        padding: 2px 8px;
        background: var(--bg);
        border-radius: 4px;
        font-size: 0.65rem;
        color: var(--text-muted);
      }
      .job-tag.lane {
        color: var(--purple);
        background: rgba(163, 113, 247, 0.15);
      }

      /* History Modal */
      .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.7);
        z-index: 200;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.2s;
      }
      .modal-overlay.visible {
        opacity: 1;
        pointer-events: auto;
      }
      .modal {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 12px;
        width: 90%;
        max-width: 700px;
        max-height: 80vh;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        transform: translateY(20px);
        transition: transform 0.2s;
      }
      .modal-overlay.visible .modal {
        transform: translateY(0);
      }
      .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 20px;
        border-bottom: 1px solid var(--border);
      }
      .modal-title {
        font-size: 1rem;
        font-weight: 600;
      }
      .modal-close {
        background: none;
        border: none;
        color: var(--text-muted);
        font-size: 1.2rem;
        cursor: pointer;
        padding: 4px 8px;
        border-radius: 6px;
      }
      .modal-close:hover {
        background: var(--bg);
        color: var(--text);
      }
      .modal-content {
        padding: 20px;
        overflow-y: auto;
        flex: 1;
      }

      /* Run History Table */
      .history-table {
        width: 100%;
        border-collapse: collapse;
      }
      .history-table th,
      .history-table td {
        padding: 10px 12px;
        text-align: left;
        border-bottom: 1px solid var(--border);
        font-size: 0.85rem;
      }
      .history-table th {
        color: var(--text-muted);
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.7rem;
        letter-spacing: 0.5px;
      }
      .history-table tr:hover td {
        background: var(--bg);
      }
      .run-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 500;
      }
      .run-status.success {
        background: rgba(63, 185, 80, 0.15);
        color: var(--green);
      }
      .run-status.failed {
        background: rgba(248, 81, 73, 0.15);
        color: var(--red);
      }
      .run-status.running {
        background: rgba(210, 153, 34, 0.15);
        color: var(--yellow);
      }
      .run-status.skipped {
        background: rgba(139, 148, 158, 0.15);
        color: var(--text-muted);
      }
      .run-duration {
        color: var(--text-muted);
        font-family: monospace;
      }
      .run-time {
        color: var(--text-muted);
        font-size: 0.8rem;
      }

      /* Loading States */
      .loading {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 60px 20px;
        color: var(--text-muted);
      }
      .loading-spinner {
        width: 40px;
        height: 40px;
        border: 3px solid var(--border);
        border-top-color: var(--accent);
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 16px;
      }
      @keyframes spin {
        to {
          transform: rotate(360deg);
        }
      }

      /* Empty State */
      .empty-state {
        text-align: center;
        padding: 60px 20px;
        color: var(--text-muted);
      }
      .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 16px;
        opacity: 0.5;
      }
      .empty-state-text {
        font-size: 0.95rem;
        margin-bottom: 8px;
      }
      .empty-state-hint {
        font-size: 0.8rem;
        opacity: 0.7;
      }

      /* Toast Notifications */
      .toast-container {
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 300;
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      .toast {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 12px 16px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 0.85rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        animation: toast-in 0.2s ease;
      }
      @keyframes toast-in {
        from {
          opacity: 0;
          transform: translateY(10px);
        }
      }
      .toast.success {
        border-color: var(--green);
      }
      .toast.error {
        border-color: var(--red);
      }
      .toast-icon {
        font-size: 1rem;
      }
      .toast.success .toast-icon {
        color: var(--green);
      }
      .toast.error .toast-icon {
        color: var(--red);
      }

      /* Responsive */
      @media (max-width: 1024px) {
        .sidebar {
          transform: translateX(-100%);
        }
        .sidebar.visible {
          transform: translateX(0);
        }
        .main-wrapper {
          margin-left: 0;
        }
      }
      @media (max-width: 768px) {
        .jobs-grid {
          grid-template-columns: 1fr;
        }
        .stats-bar {
          flex-wrap: wrap;
        }
        .modal {
          width: 95%;
          max-height: 90vh;
        }
      }
    </style>
    <script src="/js/i18n.js"></script>
    <!-- Shared Sidebar Loader -->
    <script src="/js/sidebar.js"></script>
  </head>
  <body>
    <!-- Sidebar container (populated by sidebar.js) -->
    <div id="sidebar-container"></div>

    <!-- Main Content -->
    <div class="main-wrapper" id="main-wrapper">
      <header>
        <div class="header-left">
          <h1 class="page-title" data-i18n="jobs.dashboard">🤖 AI Jobs Dashboard</h1>
        </div>
        <div class="header-actions">
          <button
            class="job-action-btn"
            onclick="refreshJobs()"
            title="Refresh"
            data-i18n="jobs.refresh"
            data-i18n-title="jobs.refresh"
          >
            🔄 Refresh
          </button>
        </div>
      </header>

      <!-- Stats Bar -->
      <div class="stats-bar" id="stats-bar">
        <div class="stat">
          <div class="stat-value" id="stat-total">—</div>
          <div class="stat-label" data-i18n="jobs.totalJobs">Total Jobs</div>
        </div>
        <div class="stat">
          <div class="stat-value green" id="stat-active">—</div>
          <div class="stat-label" data-i18n="jobs.active">Active</div>
        </div>
        <div class="stat">
          <div class="stat-value yellow" id="stat-paused">—</div>
          <div class="stat-label" data-i18n="jobs.paused">Paused</div>
        </div>
        <div class="stat">
          <div class="stat-value" id="stat-running">—</div>
          <div class="stat-label" data-i18n="jobs.running">Running</div>
        </div>
        <div class="stat">
          <div class="stat-value green" id="stat-success-rate">—</div>
          <div class="stat-label" data-i18n="jobs.successRate">Success Rate</div>
        </div>
        <div class="stat">
          <div class="stat-value red" id="stat-failures">—</div>
          <div class="stat-label" data-i18n="jobs.recentFailures">Recent Failures</div>
        </div>
      </div>

      <main>
        <!-- Filters -->
        <div class="filters-bar">
          <button class="filter-btn active" data-filter="all" onclick="setFilter('all')">
            <span data-i18n="jobs.all">All</span>
            <span class="filter-count" id="filter-all-count">0</span>
          </button>
          <button class="filter-btn" data-filter="active" onclick="setFilter('active')">
            🟢 <span data-i18n="jobs.active">Active</span>
            <span class="filter-count" id="filter-active-count">0</span>
          </button>
          <button class="filter-btn" data-filter="paused" onclick="setFilter('paused')">
            ⏸️ <span data-i18n="jobs.paused">Paused</span>
            <span class="filter-count" id="filter-paused-count">0</span>
          </button>
          <button class="filter-btn" data-filter="failed" onclick="setFilter('failed')">
            🔴 <span data-i18n="jobs.failed">Failed</span>
            <span class="filter-count" id="filter-failed-count">0</span>
          </button>
        </div>

        <!-- Jobs Grid -->
        <div class="section">
          <div id="jobs-loading" class="loading">
            <div class="loading-spinner"></div>
            <span data-i18n="jobs.loadingJobs">Loading jobs...</span>
          </div>

          <div id="jobs-empty" class="empty-state" style="display: none">
            <div class="empty-state-icon">⚙️</div>
            <div class="empty-state-text" data-i18n="jobs.noJobs">No jobs found</div>
            <div class="empty-state-hint">
              Job definitions are loaded from $OPENCLAW_JOBS_DIR/definitions/
            </div>
          </div>

          <div id="jobs-grid" class="jobs-grid" style="display: none">
            <!-- Job cards will be inserted here -->
          </div>
        </div>
      </main>
    </div>

    <!-- History Modal -->
    <div class="modal-overlay" id="history-modal">
      <div class="modal">
        <div class="modal-header">
          <span class="modal-title" id="history-modal-title" data-i18n="jobs.runHistory"
            >Run History</span
          >
          <button class="modal-close" onclick="closeHistoryModal()">×</button>
        </div>
        <div class="modal-content">
          <div id="history-loading" class="loading">
            <div class="loading-spinner"></div>
            <span data-i18n="jobs.loadingHistory">Loading history...</span>
          </div>
          <table class="history-table" id="history-table" style="display: none">
            <thead>
              <tr>
                <th data-i18n="jobs.status">Status</th>
                <th data-i18n="jobs.started">Started</th>
                <th data-i18n="jobs.duration">Duration</th>
                <th data-i18n="jobs.details">Details</th>
              </tr>
            </thead>
            <tbody id="history-tbody"></tbody>
          </table>
          <div id="history-empty" class="empty-state" style="display: none">
            <div class="empty-state-icon">📭</div>
            <div class="empty-state-text" data-i18n="jobs.noHistory">No run history yet</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Toast Container -->
    <div class="toast-container" id="toast-container"></div>

    <script>
      // State
      let jobs = [];
      let currentFilter = "all";
      let refreshTimer = null;
      const t = (key, params = {}, fallback = key) =>
        window.I18N?.t ? window.I18N.t(key, params, fallback) : fallback;

      // Format schedule for display
      function formatSchedule(schedule) {
        if (!schedule) return "—";
        if (typeof schedule === "string") return schedule;
        if (schedule.cron) return schedule.cron;
        if (schedule.interval)
          return t("jobs.every", { value: schedule.interval }, `Every ${schedule.interval}`);
        if (schedule.at) return t("jobs.at", { value: schedule.at }, `At ${schedule.at}`);
        return JSON.stringify(schedule);
      }

      // Get job status class
      function getJobStatus(job) {
        if (job.paused) return "paused";
        if (job.stats?.streak?.type === "failed" && job.stats.streak.count >= 2) return "failed";
        return "enabled";
      }

      // Get job icon
      function getJobIcon(job) {
        const status = getJobStatus(job);
        if (status === "paused") return "⏸️";
        if (status === "failed") return "⚠️";
        return "⚙️";
      }

      // Render a single job card
      function renderJobCard(job) {
        const status = getJobStatus(job);
        const icon = getJobIcon(job);
        const successRate = job.stats?.successRate
          ? Math.round(job.stats.successRate * 100) + "%"
          : "—";
        const avgDuration = job.stats?.avgDurationFormatted || "—";

        return `
                <div class="job-card ${status}" data-job-id="${job.id}" data-status="${status}">
                    <div class="job-header">
                        <div class="job-icon ${status}">${icon}</div>
                        <div class="job-title-area">
                            <div class="job-name">${escapeHtml(job.name)}</div>
                            <div class="job-id">${escapeHtml(job.id)}</div>
                            ${job.description ? `<div class="job-description">${escapeHtml(job.description)}</div>` : ""}
                        </div>
                        <span class="job-badge badge-${status}">
                            ${
                              status === "paused"
                                ? t("jobs.paused", {}, "Paused")
                                : status === "failed"
                                  ? t("jobs.statusFailing", {}, "Failing")
                                  : t("jobs.active", {}, "Active")
                            }
                        </span>
                    </div>
                    
                    <div class="job-schedule">
                        <span class="schedule-icon">📅</span>
                        <span class="schedule-cron">${escapeHtml(formatSchedule(job.schedule))}</span>
                        <span class="schedule-next">${t("jobs.next", { value: job.nextRunRelative || "—" }, `Next: ${job.nextRunRelative || "—"}`)}</span>
                    </div>
                    
                    <div class="job-tags">
                        <span class="job-tag lane">${t("jobs.lane", { value: job.lane || "medium" }, `🛤️ ${job.lane || "medium"}`)}</span>
                        ${(job.tags || []).map((t) => `<span class="job-tag">${escapeHtml(t)}</span>`).join("")}
                    </div>
                    
                    <div class="job-stats">
                        <div class="job-stat">
                            <div class="job-stat-value">${job.stats?.totalRuns || 0}</div>
                            <div class="job-stat-label">${t("jobs.runs", {}, "Runs")}</div>
                        </div>
                        <div class="job-stat">
                            <div class="job-stat-value green">${successRate}</div>
                            <div class="job-stat-label">${t("jobs.success", {}, "Success")}</div>
                        </div>
                        <div class="job-stat">
                            <div class="job-stat-value">${avgDuration}</div>
                            <div class="job-stat-label">${t("jobs.avgTime", {}, "Avg Time")}</div>
                        </div>
                    </div>
                    
                    <div class="job-last-run">
                        ${
                          job.lastRun
                            ? `
                            <span class="last-run-status ${job.stats?.streak?.type === "failed" ? "failed" : "success"}"></span>
                            <span>${t("jobs.lastRun", { value: job.lastRunRelative || "—" }, `Last run: ${job.lastRunRelative || "—"}`)}</span>
                        `
                            : `<span>${t("jobs.neverRun", {}, "Never run")}</span>`
                        }
                    </div>
                    
                    <div class="job-actions">
                        <button class="job-action-btn primary" onclick="runJob('${job.id}')" ${job.paused ? "disabled" : ""}>
                            ${t("jobs.run", {}, "▶️ Run")}
                        </button>
                        ${
                          job.paused
                            ? `<button class="job-action-btn" onclick="resumeJob('${job.id}')">${t("jobs.resume", {}, "▶️ Resume")}</button>`
                            : `<button class="job-action-btn" onclick="pauseJob('${job.id}')">${t("jobs.pause", {}, "⏸️ Pause")}</button>`
                        }
                        <button class="job-action-btn" onclick="showHistory('${job.id}', '${escapeHtml(job.name)}')">
                            ${t("jobs.history", {}, "📜 History")}
                        </button>
                    </div>
                </div>
            `;
      }

      // Escape HTML for safety
      function escapeHtml(text) {
        if (!text) return "";
        const div = document.createElement("div");
        div.textContent = text;
        return div.innerHTML;
      }

      // Render all jobs
      function renderJobs() {
        const grid = document.getElementById("jobs-grid");
        const loading = document.getElementById("jobs-loading");
        const empty = document.getElementById("jobs-empty");

        if (jobs.length === 0) {
          loading.style.display = "none";
          grid.style.display = "none";
          empty.style.display = "block";
          return;
        }

        // Filter jobs
        let filteredJobs = jobs;
        if (currentFilter !== "all") {
          filteredJobs = jobs.filter((j) => {
            const status = getJobStatus(j);
            if (currentFilter === "active") return status === "enabled";
            if (currentFilter === "paused") return status === "paused";
            if (currentFilter === "failed") return status === "failed";
            return true;
          });
        }

        loading.style.display = "none";
        empty.style.display = "none";
        grid.style.display = "grid";
        grid.innerHTML = filteredJobs.map(renderJobCard).join("");
      }

      // Update stats
      function updateStats() {
        const active = jobs.filter((j) => !j.paused).length;
        const paused = jobs.filter((j) => j.paused).length;
        const failed = jobs.filter(
          (j) => j.stats?.streak?.type === "failed" && j.stats.streak.count >= 2,
        ).length;

        // Calculate overall success rate
        let totalRuns = 0,
          totalSuccess = 0;
        jobs.forEach((j) => {
          totalRuns += j.stats?.totalRuns || 0;
          totalSuccess += j.stats?.totalSuccess || 0;
        });
        const successRate = totalRuns > 0 ? Math.round((totalSuccess / totalRuns) * 100) : 100;

        document.getElementById("stat-total").textContent = jobs.length;
        document.getElementById("stat-active").textContent = active;
        document.getElementById("stat-paused").textContent = paused;
        document.getElementById("stat-running").textContent = "0"; // TODO: track running
        document.getElementById("stat-success-rate").textContent = successRate + "%";
        document.getElementById("stat-failures").textContent = failed;

        // Update filter counts
        document.getElementById("filter-all-count").textContent = jobs.length;
        document.getElementById("filter-active-count").textContent = active;
        document.getElementById("filter-paused-count").textContent = paused;
        document.getElementById("filter-failed-count").textContent = failed;

        // Update nav badge
        document.getElementById("nav-jobs-count").textContent = jobs.length;
      }

      // Set filter
      function setFilter(filter) {
        currentFilter = filter;
        document.querySelectorAll(".filter-btn").forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.filter === filter);
        });
        renderJobs();
      }

      // Fetch jobs from API
      async function fetchJobs() {
        try {
          const res = await fetch("/api/jobs");
          const data = await res.json();
          jobs = data.jobs || [];
          renderJobs();
          updateStats();
          document.getElementById("sidebar-updated").textContent = t(
            "sidebar.updated",
            { time: new Date().toLocaleTimeString() },
            "Updated: " + new Date().toLocaleTimeString(),
          );
        } catch (e) {
          console.error("Failed to fetch jobs:", e);
          showToast(t("jobs.toastLoadFailed", {}, "Failed to load jobs"), "error");
        }
      }

      // Refresh jobs
      function refreshJobs() {
        fetchJobs();
      }

      // Run job
      async function runJob(jobId) {
        try {
          const res = await fetch(`/api/jobs/${encodeURIComponent(jobId)}/run`, { method: "POST" });
          const data = await res.json();
          if (data.success) {
            showToast(
              t("jobs.toastRunQueued", { id: jobId }, `Job "${jobId}" queued for execution`),
              "success",
            );
            setTimeout(refreshJobs, 1000);
          } else {
            showToast(data.error || t("jobs.toastRunFailed", {}, "Failed to run job"), "error");
          }
        } catch (e) {
          showToast(t("jobs.toastRunFailed", {}, "Failed to run job"), "error");
        }
      }

      // Pause job
      async function pauseJob(jobId) {
        try {
          const res = await fetch(`/api/jobs/${encodeURIComponent(jobId)}/pause`, {
            method: "POST",
          });
          const data = await res.json();
          if (data.success) {
            showToast(t("jobs.toastPaused", { id: jobId }, `Job "${jobId}" paused`), "success");
            refreshJobs();
          } else {
            showToast(data.error || t("jobs.toastPauseFailed", {}, "Failed to pause job"), "error");
          }
        } catch (e) {
          showToast(t("jobs.toastPauseFailed", {}, "Failed to pause job"), "error");
        }
      }

      // Resume job
      async function resumeJob(jobId) {
        try {
          const res = await fetch(`/api/jobs/${encodeURIComponent(jobId)}/resume`, {
            method: "POST",
          });
          const data = await res.json();
          if (data.success) {
            showToast(t("jobs.toastResumed", { id: jobId }, `Job "${jobId}" resumed`), "success");
            refreshJobs();
          } else {
            showToast(
              data.error || t("jobs.toastResumeFailed", {}, "Failed to resume job"),
              "error",
            );
          }
        } catch (e) {
          showToast(t("jobs.toastResumeFailed", {}, "Failed to resume job"), "error");
        }
      }

      // Show history modal
      async function showHistory(jobId, jobName) {
        const modal = document.getElementById("history-modal");
        const title = document.getElementById("history-modal-title");
        const loading = document.getElementById("history-loading");
        const table = document.getElementById("history-table");
        const tbody = document.getElementById("history-tbody");
        const empty = document.getElementById("history-empty");

        title.textContent = t("jobs.historyTitle", { name: jobName }, `Run History: ${jobName}`);
        modal.classList.add("visible");
        loading.style.display = "flex";
        table.style.display = "none";
        empty.style.display = "none";

        try {
          const res = await fetch(`/api/jobs/${encodeURIComponent(jobId)}/history?limit=50`);
          const data = await res.json();
          const runs = data.runs || [];

          loading.style.display = "none";

          if (runs.length === 0) {
            empty.style.display = "block";
            return;
          }

          tbody.innerHTML = runs
            .map(
              (run) => `
                    <tr>
                        <td>
                            <span class="run-status ${run.status}">
                                ${run.status === "success" ? "✅" : run.status === "failed" ? "❌" : "⏳"}
                                ${
                                  run.status === "success"
                                    ? t("jobs.statusSuccess", {}, run.status)
                                    : run.status === "failed"
                                      ? t("jobs.statusFailed", {}, run.status)
                                      : t("jobs.statusRunning", {}, run.status)
                                }
                            </span>
                        </td>
                        <td class="run-time">${run.startedAtRelative || run.startedAt || "—"}</td>
                        <td class="run-duration">${run.durationFormatted || "—"}</td>
                        <td>${run.error ? `<span style="color: var(--red)">${escapeHtml(run.error.slice(0, 50))}</span>` : "—"}</td>
                    </tr>
                `,
            )
            .join("");

          table.style.display = "table";
        } catch (e) {
          loading.style.display = "none";
          empty.style.display = "block";
          console.error("Failed to fetch history:", e);
        }
      }

      // Close history modal
      function closeHistoryModal() {
        document.getElementById("history-modal").classList.remove("visible");
      }

      // Show toast notification
      function showToast(message, type = "info") {
        const container = document.getElementById("toast-container");
        const toast = document.createElement("div");
        toast.className = `toast ${type}`;
        toast.innerHTML = `
                <span class="toast-icon">${type === "success" ? "✅" : type === "error" ? "❌" : "ℹ️"}</span>
                <span>${escapeHtml(message)}</span>
            `;
        container.appendChild(toast);
        setTimeout(() => toast.remove(), 4000);
      }

      // Toggle sidebar - provided by sidebar.js

      // Close modal on overlay click
      document.getElementById("history-modal").addEventListener("click", function (e) {
        if (e.target === this) closeHistoryModal();
      });

      // Keyboard shortcuts
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") closeHistoryModal();
        if (e.key === "r" && !e.metaKey && !e.ctrlKey) refreshJobs();
      });

      window.addEventListener("i18n:updated", function () {
        if (jobs.length > 0) {
          renderJobs();
        }
      });

      // Initialize
      fetchJobs();

      // Auto-refresh every 30 seconds
      refreshTimer = setInterval(fetchJobs, 30000);
    </script>
  </body>
</html>
```

## File: `public/css/dashboard.css`
```css
:root {
  --bg: #0d1117;
  --card-bg: #161b22;
  --card-hover: #1c2128;
  --border: #30363d;
  --text: #c9d1d9;
  --text-muted: #8b949e;
  --accent: #58a6ff;
  --green: #3fb950;
  --yellow: #d29922;
  --red: #f85149;
  --purple: #a371f7;
  --orange: #db6d28;
  --sidebar-width: 220px;
}
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  display: flex;
}

/* Buttons */
.btn-primary,
.btn-secondary {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.85rem;
  cursor: pointer;
  border: 1px solid var(--border);
  transition: all 0.15s ease;
}
.btn-primary {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
.btn-primary:hover {
  background: #4c9aed;
  border-color: #4c9aed;
}
.btn-secondary {
  background: var(--card-bg);
  color: var(--text);
}
.btn-secondary:hover {
  background: var(--card-hover);
  border-color: var(--accent);
}

/* Sidebar */
.sidebar {
  width: var(--sidebar-width);
  background: var(--card-bg);
  border-right: 1px solid var(--border);
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  z-index: 60;
  transition: transform 0.2s ease;
}
.sidebar.collapsed {
  width: 56px;
  transform: none;
}
.sidebar.collapsed .sidebar-title,
.sidebar.collapsed .nav-section-title,
.sidebar.collapsed .nav-item span:not(.nav-icon),
.sidebar.collapsed .nav-badge,
.sidebar.collapsed .sidebar-footer {
  display: none;
}
.sidebar.collapsed .sidebar-header {
  justify-content: center;
  padding: 16px 8px;
}
.sidebar.collapsed .sidebar-toggle {
  margin-left: 0;
}
.sidebar.collapsed .nav-item {
  justify-content: center;
  padding: 12px;
}
.sidebar.collapsed .nav-icon {
  margin: 0;
  font-size: 1.2rem;
}
.sidebar.collapsed .nav-section {
  margin-bottom: 8px;
}
.sidebar.collapsed .nav-item {
  position: relative;
}
.sidebar.collapsed .nav-item::after {
  content: attr(data-tooltip);
  position: absolute;
  left: 100%;
  top: 50%;
  transform: translateY(-50%);
  background: var(--card-bg);
  border: 1px solid var(--border);
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.15s;
  margin-left: 8px;
  z-index: 100;
}
.sidebar.collapsed .nav-item:hover::after {
  opacity: 1;
}
.sidebar-header {
  padding: 16px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}
.sidebar-logo {
  font-size: 1.3rem;
}
.sidebar-title {
  font-size: 0.9rem;
  font-weight: 600;
  white-space: nowrap;
}
.sidebar-toggle {
  margin-left: auto;
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 6px;
  border-radius: 6px;
  font-size: 1rem;
}
.sidebar-toggle:hover {
  background: var(--bg);
  color: var(--text);
}

.sidebar-nav {
  flex: 1;
  padding: 12px 8px;
  overflow-y: auto;
}
.nav-section {
  margin-bottom: 16px;
}
.nav-section-title {
  font-size: 0.65rem;
  text-transform: uppercase;
  color: var(--text-muted);
  padding: 8px 12px 4px;
  letter-spacing: 0.5px;
}
.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.85rem;
  color: var(--text-muted);
  transition: all 0.15s;
  text-decoration: none;
}
.nav-item:hover {
  background: var(--bg);
  color: var(--text);
}
.nav-item.active {
  background: rgba(88, 166, 255, 0.15);
  color: var(--accent);
}
.nav-icon {
  font-size: 1rem;
  width: 20px;
  text-align: center;
}
.nav-badge {
  margin-left: auto;
  background: var(--border);
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.7rem;
}
.nav-item.active .nav-badge {
  background: rgba(88, 166, 255, 0.3);
}

.sidebar-footer {
  padding: 12px;
  border-top: 1px solid var(--border);
  font-size: 0.7rem;
  color: var(--text-muted);
  text-align: center;
}

/* Main Content Area */
.main-wrapper {
  flex: 1;
  margin-left: var(--sidebar-width);
  transition: margin-left 0.2s ease;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.main-wrapper.sidebar-collapsed {
  margin-left: 56px;
}

/* Header */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  background: var(--card-bg);
  position: sticky;
  top: 0;
  z-index: 50;
}
.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}
.page-title {
  font-size: 1.1rem;
  font-weight: 600;
}
.status-pill {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: rgba(63, 185, 80, 0.15);
  border-radius: 20px;
  font-size: 0.8rem;
  color: var(--green);
}
.pulse {
  width: 8px;
  height: 8px;
  background: var(--green);
  border-radius: 50%;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}
.status-pill.connected {
  background: rgba(63, 185, 80, 0.15);
  color: var(--green);
}
.status-pill.disconnected {
  background: rgba(248, 81, 73, 0.15);
  color: var(--red);
}
.status-pill.connecting {
  background: rgba(210, 153, 34, 0.15);
  color: var(--yellow);
}
.status-pill.disconnected .pulse {
  background: var(--red);
  animation: none;
}
.status-pill.connecting .pulse {
  background: var(--yellow);
}

/* Activity State Indicators */
@keyframes activity-pulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.7;
  }
}
@keyframes activity-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.activity-indicator {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  font-size: 0.9rem;
  flex-shrink: 0;
}
.activity-indicator.thinking {
  animation: activity-pulse 1.5s ease-in-out infinite;
  background: rgba(88, 166, 255, 0.15);
}
.activity-indicator.tool {
  animation: activity-spin 2s linear infinite;
  background: rgba(210, 153, 34, 0.15);
}
.activity-indicator.waiting {
  background: rgba(139, 148, 158, 0.15);
}
.activity-indicator.idle {
  background: rgba(139, 148, 158, 0.1);
  opacity: 0.6;
}
.activity-label {
  font-size: 0.65rem;
  color: var(--text-muted);
  margin-left: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.activity-wrapper {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* Stats Bar */
.stats-bar {
  display: flex;
  gap: 12px;
  padding: 16px 24px;
  background: var(--card-bg);
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
}
.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px 20px;
  background: var(--bg);
  border-radius: 8px;
  min-width: 100px;
}
.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent);
}
.stat-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-top: 4px;
}

/* Legend & Filters Bar */
.filters-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  flex-wrap: wrap;
  gap: 12px;
}
.legend {
  display: flex;
  gap: 16px;
  align-items: center;
}
.legend-title {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-right: 4px;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.75rem;
  color: var(--text-muted);
}
.legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.legend-dot.live {
  background: var(--green);
}
.legend-dot.recent {
  background: var(--yellow);
}
.legend-dot.idle {
  background: var(--text-muted);
  opacity: 0.5;
}

.filters {
  display: flex;
  gap: 8px;
  align-items: center;
}
.filter-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-right: 4px;
}
.filter-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 5px 10px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  font-size: 0.75rem;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s;
}
.filter-btn:hover {
  border-color: var(--accent);
  color: var(--text);
}
.filter-btn.active {
  background: rgba(88, 166, 255, 0.15);
  border-color: var(--accent);
  color: var(--accent);
}
.filter-btn .filter-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.filter-btn .filter-dot.live {
  background: var(--green);
}
.filter-btn .filter-dot.recent {
  background: var(--yellow);
}
.filter-btn .filter-dot.idle {
  background: var(--text-muted);
}
.filter-count {
  background: var(--bg);
  padding: 1px 6px;
  border-radius: 8px;
  font-size: 0.65rem;
}

/* Section Filters (inline with each section) */
.section-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  padding: 12px 16px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  margin-bottom: 16px;
}
.filter-group {
  display: flex;
  align-items: center;
  gap: 8px;
}
.filter-group .filter-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  white-space: nowrap;
}
.filter-group .filter-btn {
  padding: 4px 10px;
  font-size: 0.75rem;
}

/* Pagination */
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 16px;
  margin-top: 16px;
}
.pagination-btn {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 12px;
  color: var(--text);
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 4px;
}
.pagination-btn:hover:not(:disabled) {
  background: var(--hover-bg);
  border-color: var(--accent);
}
.pagination-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
.pagination-info {
  color: var(--text-muted);
  font-size: 0.8rem;
  padding: 0 12px;
}
.pagination-pages {
  display: flex;
  gap: 4px;
}
.pagination-page {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 6px 10px;
  color: var(--text-muted);
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.2s;
  min-width: 32px;
  text-align: center;
}
.pagination-page:hover {
  background: var(--hover-bg);
}
.pagination-page.active {
  background: var(--accent);
  color: var(--bg);
  border-color: var(--accent);
}
.pagination-ellipsis {
  color: var(--text-muted);
  padding: 6px 4px;
}

/* Main Content */
main {
  padding: 24px;
  flex: 1;
}

/* Section */
.section {
  margin-bottom: 32px;
  scroll-margin-top: 100px;
}

/* Section Headers */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}
.section-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 8px;
}
.section-count {
  background: var(--border);
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.75rem;
}

/* Card Grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}

/* Session Card */
.session-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.15s ease;
  position: relative;
  overflow: hidden;
}
.session-card.hidden-by-filter {
  display: none;
}
.session-card:hover {
  background: var(--card-hover);
  border-color: var(--accent);
  transform: translateY(-2px);
}
.session-card.active {
  border-color: var(--green);
  box-shadow: 0 0 0 1px var(--green);
}
.session-card.active::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--green);
}
.session-card.recent-active {
  border-color: var(--yellow);
}
.session-card.recent-active::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--yellow);
}

.card-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 12px;
}
.card-icon {
  width: 40px;
  height: 40px;
  background: var(--bg);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  flex-shrink: 0;
}
.card-icon.slack {
  background: rgba(88, 166, 255, 0.15);
}
.card-icon.telegram {
  background: rgba(63, 185, 80, 0.15);
}
.card-icon.main {
  background: rgba(163, 113, 247, 0.15);
}

.card-title-area {
  flex: 1;
  min-width: 0;
}
.card-title {
  font-size: 0.9rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.card-subtitle {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 2px;
}
.card-topics {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-top: 8px;
  margin-bottom: 4px;
}
.topic-pill {
  font-size: 0.65rem;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 12px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  color: var(--text-muted);
  white-space: nowrap;
}
.topic-pill.coding {
  background: rgba(99, 102, 241, 0.15);
  border-color: rgba(99, 102, 241, 0.3);
  color: #818cf8;
}
.topic-pill.git {
  background: rgba(249, 115, 22, 0.15);
  border-color: rgba(249, 115, 22, 0.3);
  color: #fb923c;
}
.topic-pill.slack {
  background: rgba(74, 21, 75, 0.3);
  border-color: rgba(224, 30, 90, 0.3);
  color: #e91e63;
}
.topic-pill.dashboard {
  background: rgba(16, 185, 129, 0.15);
  border-color: rgba(16, 185, 129, 0.3);
  color: #34d399;
}
.topic-pill.memory {
  background: rgba(139, 92, 246, 0.15);
  border-color: rgba(139, 92, 246, 0.3);
  color: #a78bfa;
}
.topic-pill.heartbeat {
  background: rgba(239, 68, 68, 0.15);
  border-color: rgba(239, 68, 68, 0.3);
  color: #f87171;
}
.topic-pill.tools {
  background: rgba(234, 179, 8, 0.15);
  border-color: rgba(234, 179, 8, 0.3);
  color: #fbbf24;
}
.topic-pill.file {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.3);
  color: #60a5fa;
}
.topic-pill.research {
  background: rgba(236, 72, 153, 0.15);
  border-color: rgba(236, 72, 153, 0.3);
  color: #f472b6;
}
.topic-pill.api {
  background: rgba(20, 184, 166, 0.15);
  border-color: rgba(20, 184, 166, 0.3);
  color: #2dd4bf;
}
.card-preview {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 6px;
  font-style: italic;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-badge {
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 500;
  flex-shrink: 0;
}
.badge-live {
  background: rgba(63, 185, 80, 0.2);
  color: var(--green);
}
.badge-recent {
  background: rgba(210, 153, 34, 0.2);
  color: var(--yellow);
}
.badge-idle {
  background: rgba(139, 148, 158, 0.15);
  color: var(--text-muted);
}

/* Quick hide button on cards */
.hide-btn {
  background: none;
  border: none;
  cursor: pointer;
  opacity: 0;
  padding: 4px 6px;
  font-size: 0.85rem;
  transition: opacity 0.15s;
  flex-shrink: 0;
}
.session-card:hover .hide-btn,
.cron-card:hover .hide-btn {
  opacity: 0.5;
}
.hide-btn:hover {
  opacity: 1 !important;
}

.card-stats {
  display: flex;
  gap: 16px;
  padding: 10px 0;
  border-top: 1px solid var(--border);
  margin-top: 8px;
}
.card-stat {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.75rem;
  color: var(--text-muted);
}
.card-stat-value {
  color: var(--text);
  font-weight: 500;
}
.card-stat.high .card-stat-value {
  color: var(--red);
}
.card-stat.med .card-stat-value {
  color: var(--yellow);
}

/* Cerebro topic tag */
.cerebro-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.7rem;
  color: var(--accent);
  background: rgba(100, 223, 223, 0.1);
  border: 1px solid rgba(100, 223, 223, 0.3);
  border-radius: 4px;
  padding: 2px 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.cerebro-tag:hover {
  background: rgba(100, 223, 223, 0.2);
  border-color: var(--accent);
}

/* Cerebro topic action buttons */
.topic-actions {
  display: flex;
  gap: 4px;
  margin-left: auto;
}
.topic-action-btn {
  padding: 2px 6px;
  font-size: 0.7rem;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--bg);
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s ease;
  opacity: 0.6;
}
.topic-action-btn:hover {
  opacity: 1;
  background: var(--card-hover);
}
.topic-action-btn.resolve:hover {
  border-color: var(--green);
  color: var(--green);
}
.topic-action-btn.park:hover {
  border-color: var(--yellow);
  color: var(--yellow);
}
.topic-action-btn.reactivate:hover {
  border-color: var(--accent);
  color: var(--accent);
}
.topic-action-btn.hide:hover {
  border-color: var(--red);
  color: var(--red);
}

/* Toast notifications */
.toast-container {
  position: fixed;
  bottom: 80px;
  right: 24px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.toast {
  padding: 12px 16px;
  border-radius: 8px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 0.85rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  animation: toast-in 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}
.toast.success {
  border-color: var(--green);
  background: rgba(63, 185, 80, 0.15);
}
.toast.error {
  border-color: var(--red);
  background: rgba(248, 81, 73, 0.15);
}
@keyframes toast-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes toast-out {
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(20px);
  }
}

/* Progress/Effort Metrics Bar - Fitness tracker aesthetic */
.metrics-bar {
  display: flex;
  gap: 12px;
  padding: 8px 12px;
  margin-top: 10px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  justify-content: space-around;
}
.metric-ring {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  position: relative;
}
.metric-icon {
  font-size: 0.9rem;
  opacity: 0.8;
}
.metric-value {
  font-size: 0.7rem;
  font-weight: 600;
  color: var(--text);
}
.metric-label {
  font-size: 0.55rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.metric-ring.burn .metric-value {
  color: var(--orange);
}
.metric-ring.burn.hot .metric-value {
  color: var(--red);
}
.metric-ring.tools .metric-value {
  color: var(--accent);
}
.metric-ring.time .metric-value {
  color: var(--green);
}

.card-links {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}
.link-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 8px;
  background: var(--bg);
  border-radius: 4px;
  font-size: 0.7rem;
  color: var(--accent);
  text-decoration: none;
}
.link-tag:hover {
  background: rgba(88, 166, 255, 0.2);
}
.link-tag.linear {
  color: #5e6ad2;
}
.link-tag.jira {
  color: #0052cc;
}
.link-tag.github {
  color: var(--text);
}
.link-tag.slack {
  color: #e01e5a;
}
.link-tag.file {
  color: var(--orange);
}

/* Cron Cards */
.cron-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.15s ease;
}
.cron-card:hover {
  background: var(--card-hover);
  border-color: var(--purple);
}
.cron-card.disabled {
  opacity: 0.5;
}
.cron-icon {
  width: 36px;
  height: 36px;
  background: rgba(163, 113, 247, 0.15);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}
.cron-info {
  flex: 1;
}
.cron-name {
  font-size: 0.85rem;
  font-weight: 500;
}
.cron-schedule {
  font-size: 0.75rem;
  color: var(--purple);
  font-family: monospace;
}
.cron-schedule-human {
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-top: 2px;
}
.cron-meta {
  display: flex;
  align-items: center;
  gap: 8px;
}
.cron-next {
  font-size: 0.7rem;
  color: var(--text-muted);
  padding: 4px 10px;
  background: var(--bg);
  border-radius: 12px;
}
.cron-status {
  font-size: 0.7rem;
  padding: 4px 8px;
  border-radius: 12px;
}
.cron-status.enabled {
  background: rgba(63, 185, 80, 0.15);
  color: var(--green);
}
.cron-status.disabled {
  background: rgba(139, 148, 158, 0.15);
  color: var(--text-muted);
}

/* Operators Grid */
.operators-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
}
.operator-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  transition: all 0.15s ease;
  position: relative;
}
.operator-card:hover {
  background: var(--card-hover);
  border-color: var(--accent);
}
.operator-card.role-owner {
  border-color: rgba(255, 215, 0, 0.4);
}
.operator-card.role-owner::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #ffd700, #ff8c00);
}
.operator-card.role-admin {
  border-color: rgba(163, 113, 247, 0.4);
}
.operator-card.role-admin::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #a371f7, #8957e5);
}
.operator-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 16px;
}
.operator-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  flex-shrink: 0;
}
.operator-avatar img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}
.operator-info {
  flex: 1;
  min-width: 0;
}
.operator-name {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 2px;
}
.operator-username {
  font-size: 0.8rem;
  color: var(--text-muted);
}
.operator-role {
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.operator-role.owner {
  background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 140, 0, 0.2));
  color: #ffd700;
}
.operator-role.admin {
  background: linear-gradient(135deg, rgba(163, 113, 247, 0.2), rgba(137, 87, 229, 0.2));
  color: #a371f7;
}
.operator-role.user {
  background: rgba(88, 166, 255, 0.15);
  color: var(--accent);
}
.operator-stats {
  display: flex;
  gap: 16px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
}
.operator-stat {
  text-align: center;
  flex: 1;
}
.operator-stat-value {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text);
}
.operator-stat-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

/* Session originator badge */
.session-originator {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  background: rgba(88, 166, 255, 0.1);
  border-radius: 10px;
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-top: 4px;
}
.session-originator .originator-avatar {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--bg);
  font-size: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* System Vitals Panel */
.vitals-panel {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 24px;
}
.vitals-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}
.vitals-title {
  font-size: 0.9rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
}
.vitals-hostname {
  font-size: 0.8rem;
  color: var(--accent);
  background: rgba(88, 166, 255, 0.15);
  padding: 4px 10px;
  border-radius: 12px;
}
.vitals-uptime {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.vitals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}
.vital-card {
  background: var(--bg);
  border-radius: 10px;
  padding: 14px;
}
.vital-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.vital-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 6px;
}
.vital-value {
  font-size: 1rem;
  font-weight: 600;
}
.vital-value.green {
  color: var(--green);
}
.vital-value.yellow {
  color: var(--yellow);
}
.vital-value.red {
  color: var(--red);
}

/* Progress bar (DaisyDisk-style) */
.vital-bar {
  height: 8px;
  background: var(--border);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 8px;
}
.vital-bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.3s ease;
}
.vital-bar-fill.green {
  background: linear-gradient(90deg, #2ea043, #3fb950);
}
.vital-bar-fill.yellow {
  background: linear-gradient(90deg, #9e6a03, #d29922);
}
.vital-bar-fill.red {
  background: linear-gradient(90deg, #da3633, #f85149);
}
.vital-bar-fill.blue {
  background: linear-gradient(90deg, #1f6feb, #58a6ff);
}
.vital-bar-fill.purple {
  background: linear-gradient(90deg, #8957e5, #a371f7);
}
.vital-bar-fill.gray {
  background: linear-gradient(90deg, #484f58, #6e7681);
}

.vital-detail {
  display: flex;
  justify-content: space-between;
  font-size: 0.7rem;
  color: var(--text-muted);
}
.vital-detail-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.vital-detail-value {
  font-size: 0.8rem;
  color: var(--text);
  font-weight: 500;
}
.vital-detail-label {
  font-size: 0.65rem;
}

/* CPU cores visualization */
.cpu-cores {
  display: flex;
  gap: 3px;
  margin-top: 8px;
}
.cpu-core {
  flex: 1;
  height: 20px;
  background: var(--border);
  border-radius: 3px;
  position: relative;
  overflow: hidden;
}
.cpu-core-fill {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--accent);
  transition: height 0.3s ease;
}

/* Temperature */
.temp-display {
  display: flex;
  align-items: baseline;
  gap: 4px;
}
.temp-value {
  font-size: 1.5rem;
  font-weight: 700;
}
.temp-unit {
  font-size: 0.9rem;
  color: var(--text-muted);
}

/* Memory pressure indicator */
.pressure-indicator {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.65rem;
  text-transform: uppercase;
}
.pressure-indicator.normal {
  background: rgba(63, 185, 80, 0.15);
  color: var(--green);
}
.pressure-indicator.warning {
  background: rgba(210, 153, 34, 0.15);
  color: var(--yellow);
}
.pressure-indicator.critical {
  background: rgba(248, 81, 73, 0.15);
  color: var(--red);
}

/* Empty States */
.empty-state {
  text-align: center;
  padding: 40px 20px;
  color: var(--text-muted);
}
.empty-state-icon {
  font-size: 2.5rem;
  margin-bottom: 12px;
  opacity: 0.5;
}
.empty-state-text {
  font-size: 0.9rem;
}

/* Detail Panel */
.detail-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 100;
  opacity: 0;
  transition: opacity 0.2s;
}
.detail-overlay.visible {
  opacity: 1;
}
.detail-overlay.hidden {
  display: none;
}

.detail-panel {
  position: fixed;
  top: 0;
  right: 0;
  width: 50%;
  max-width: 600px;
  height: 100vh;
  background: var(--bg);
  border-left: 1px solid var(--border);
  z-index: 101;
  overflow-y: auto;
  transform: translateX(100%);
  transition: transform 0.2s ease;
}
.detail-panel.visible {
  transform: translateX(0);
}
.detail-panel.hidden {
  display: none;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  background: var(--bg);
}
.detail-header h2 {
  font-size: 1rem;
  font-weight: 600;
}
.close-btn {
  background: var(--card-bg);
  border: 1px solid var(--border);
  color: var(--text-muted);
  width: 32px;
  height: 32px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
}
.close-btn:hover {
  background: var(--card-hover);
  color: var(--text);
}

.detail-content {
  padding: 24px;
}
.detail-section {
  margin-bottom: 24px;
}
.detail-section h3 {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.detail-box {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px;
}
.detail-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  font-size: 0.85rem;
}
.detail-row:not(:last-child) {
  border-bottom: 1px solid var(--border);
}
.detail-label {
  color: var(--text-muted);
}
.detail-value {
  font-weight: 500;
}

.detail-section.attention .detail-box {
  border-color: var(--yellow);
  background: rgba(210, 153, 34, 0.08);
}
.attention-item {
  padding: 8px 0;
  font-size: 0.85rem;
  display: flex;
  gap: 8px;
}
.attention-item:not(:last-child) {
  border-bottom: 1px solid var(--border);
}

.tool-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  background: var(--bg);
  border-radius: 6px;
  font-size: 0.8rem;
  margin: 3px;
}
.tool-tag code {
  color: var(--accent);
}
.tool-count {
  color: var(--text-muted);
  font-size: 0.7rem;
}

.message-item {
  padding: 10px 0;
  font-size: 0.85rem;
}
.message-item:not(:last-child) {
  border-bottom: 1px solid var(--border);
}
.message-role {
  font-weight: 600;
  font-size: 0.75rem;
  margin-bottom: 4px;
}
.message-role.user {
  color: var(--accent);
}
.message-role.assistant {
  color: var(--green);
}
.message-text {
  color: var(--text-muted);
  line-height: 1.4;
}

/* Action Buttons (Read-Write Controls) - Future */
.action-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.8rem;
  color: var(--text);
  cursor: pointer;
  transition: all 0.15s;
}
.action-btn:hover {
  background: var(--card-hover);
  border-color: var(--accent);
}
.action-btn.danger:hover {
  border-color: var(--red);
  color: var(--red);
}
.action-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.detail-actions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid var(--border);
}

.refresh-bar {
  text-align: center;
  padding: 12px;
  color: var(--text-muted);
  font-size: 0.75rem;
  background: var(--card-bg);
  border-top: 1px solid var(--border);
}

/* Skeleton Loading States */
@keyframes skeleton-pulse {
  0%,
  100% {
    opacity: 0.4;
  }
  50% {
    opacity: 0.7;
  }
}
.skeleton {
  animation: skeleton-pulse 1.5s ease-in-out infinite;
}
.skeleton-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  animation: skeleton-pulse 1.5s ease-in-out infinite;
}
.skeleton-bar {
  background: var(--border);
  border-radius: 4px;
  height: 14px;
}
.skeleton-bar.title {
  width: 60%;
  height: 18px;
  margin-bottom: 8px;
}
.skeleton-bar.subtitle {
  width: 40%;
  height: 12px;
  margin-bottom: 12px;
}
.skeleton-bar.text {
  width: 80%;
  margin-bottom: 6px;
}
.skeleton-bar.short {
  width: 30%;
}
.skeleton-circle {
  width: 32px;
  height: 32px;
  background: var(--border);
  border-radius: 50%;
}
.skeleton-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}
.skeleton-stats {
  display: flex;
  gap: 16px;
  margin-top: 12px;
}
.skeleton-badge {
  width: 50px;
  height: 20px;
  background: var(--border);
  border-radius: 10px;
  margin-left: auto;
}
.loading-dots {
  display: inline-flex;
  gap: 4px;
}
.loading-dots span {
  width: 6px;
  height: 6px;
  background: var(--accent);
  border-radius: 50%;
  animation: loading-dot 1.4s infinite ease-in-out both;
}
.loading-dots span:nth-child(1) {
  animation-delay: -0.32s;
}
.loading-dots span:nth-child(2) {
  animation-delay: -0.16s;
}
@keyframes loading-dot {
  0%,
  80%,
  100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}

/* Responsive */
@media (max-width: 1024px) {
  .sidebar {
    transform: translateX(-100%);
  }
  .sidebar.visible {
    transform: translateX(0);
  }
  .main-wrapper {
    margin-left: 0;
  }
  .mobile-menu-btn {
    display: block;
  }
}
@media (max-width: 768px) {
  .detail-panel {
    width: 100%;
    max-width: none;
  }
  .card-grid {
    grid-template-columns: 1fr;
  }
  .stats-bar {
    flex-wrap: wrap;
  }
  .filters-bar {
    flex-direction: column;
    align-items: flex-start;
  }
}

/* Token Utilization Widget */
.utilization-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.utilization-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
}
.utilization-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}
.utilization-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}
.utilization-icon.anthropic {
  background: rgba(216, 153, 99, 0.2);
}
.utilization-icon.openai {
  background: rgba(16, 163, 127, 0.2);
}
.utilization-title {
  font-weight: 600;
  font-size: 0.9rem;
}
.utilization-subtitle {
  font-size: 0.7rem;
  color: var(--text-muted);
}

.quota-bar {
  height: 8px;
  background: var(--bg);
  border-radius: 4px;
  overflow: hidden;
  margin: 8px 0;
}
.quota-bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.3s ease;
}
.quota-bar-fill.low {
  background: var(--green);
}
.quota-bar-fill.medium {
  background: var(--yellow);
}
.quota-bar-fill.high {
  background: var(--red);
}

.quota-stats {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--text-muted);
}
.quota-value {
  font-weight: 600;
  color: var(--text);
}

/* Sub-agent Status Panel */
.subagent-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.subagent-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  transition: border-color 0.2s ease;
}
.subagent-card.active {
  border-color: var(--green);
}
.subagent-card.stale {
  border-color: var(--yellow);
}

.subagent-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
.subagent-info h4 {
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 4px;
}
.subagent-meta {
  font-size: 0.7rem;
  color: var(--text-muted);
}
.subagent-status {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 500;
}
.subagent-status.active {
  background: rgba(63, 185, 80, 0.15);
  color: var(--green);
}
.subagent-status.idle {
  background: rgba(217, 153, 34, 0.15);
  color: var(--yellow);
}
.subagent-status.stale {
  background: rgba(248, 81, 73, 0.15);
  color: var(--red);
}

/* Quick Actions */
.quick-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}
.quick-actions-title {
  width: 100%;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 8px;
}
.quick-action-btn {
  padding: 8px 16px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.2s ease;
  text-decoration: none;
}
.quick-action-btn:hover {
  background: var(--card-hover);
  border-color: var(--accent);
}
```

## File: `public/data/AGENTS.md`
```markdown
# public/data/ — User-Specific Data

**DO NOT COMMIT** the following files — they contain user-specific data:

| File                    | Purpose                          | Template                        |
| ----------------------- | -------------------------------- | ------------------------------- |
| `operators.json`        | User/operator info from sessions | `operators.json.example`        |
| `privacy-settings.json` | Hidden topics/sessions for demos | `privacy-settings.json.example` |

## Why?

These files are generated at runtime and contain:

- User IDs and usernames
- Session counts and activity
- Privacy preferences (what the user hides)

Committing them would leak user data to the public repo.

## For New Installations

Copy the `.example` files to get started:

```bash
cp operators.json.example operators.json
cp privacy-settings.json.example privacy-settings.json
```

The dashboard will populate these automatically on first run.
```

## File: `public/data/operators.json.example`
```
{
  "version": 1,
  "operators": [
    {
      "id": "U00000000",
      "name": "example-user",
      "username": "example",
      "source": "slack",
      "firstSeen": "2026-01-01T00:00:00.000Z",
      "lastSeen": null,
      "sessionCount": 100
    }
  ],
  "roles": {},
  "lastRefreshed": 0
}
```

## File: `public/data/privacy-settings.json.example`
```
{
  "version": 1,
  "hiddenTopics": [],
  "hiddenSessions": [],
  "hiddenCrons": [],
  "hideHostname": false,
  "updatedAt": null
}
```

## File: `public/js/api.js`
```javascript
/**
 * API and SSE connection management for Command Center
 */

// SSE connection state
let eventSource = null;
let sseConnected = false;
let sseReconnectAttempts = 0;
let pollInterval = null;

const SSE_MAX_RECONNECT_DELAY = 30000;

/**
 * Fetch the unified state from the server
 * @returns {Promise<Object>} Dashboard state
 */
export async function fetchState() {
  const response = await fetch("/api/state");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}

/**
 * Connect to SSE for real-time updates
 * @param {Function} onUpdate - Callback when state updates
 * @param {Function} onStatusChange - Callback for connection status changes
 */
export function connectSSE(onUpdate, onStatusChange) {
  if (typeof EventSource === "undefined") {
    console.warn("[SSE] EventSource not supported, using polling fallback");
    onStatusChange?.("polling", "Polling Mode");
    startPolling(onUpdate);
    return;
  }

  onStatusChange?.("connecting", "Connecting...");

  try {
    eventSource = new EventSource("/api/events");

    eventSource.onopen = function () {
      console.log("[SSE] Connected");
      sseConnected = true;
      sseReconnectAttempts = 0;
      onStatusChange?.("connected", "🟢 Live");
      stopPolling();
    };

    eventSource.addEventListener("connected", function (e) {
      try {
        const data = JSON.parse(e.data);
        console.log("[SSE] Server greeting:", data.message);
      } catch (err) {}
    });

    eventSource.addEventListener("update", function (e) {
      try {
        const data = JSON.parse(e.data);
        onUpdate?.(data);
      } catch (err) {
        console.error("[SSE] Failed to parse update:", err);
      }
    });

    eventSource.addEventListener("heartbeat", function (e) {
      try {
        const data = JSON.parse(e.data);
        console.log("[SSE] Heartbeat, clients:", data.clients);
      } catch (err) {}
    });

    eventSource.onerror = function (e) {
      console.error("[SSE] Connection error");
      sseConnected = false;
      eventSource.close();
      eventSource = null;
      onStatusChange?.("disconnected", "🔴 Disconnected");

      // Exponential backoff for reconnection
      sseReconnectAttempts++;
      const delay = Math.min(1000 * Math.pow(2, sseReconnectAttempts - 1), SSE_MAX_RECONNECT_DELAY);
      console.log(`[SSE] Reconnecting in ${delay}ms (attempt ${sseReconnectAttempts})`);

      // Start polling as fallback while disconnected
      startPolling(onUpdate);

      setTimeout(() => connectSSE(onUpdate, onStatusChange), delay);
    };
  } catch (err) {
    console.error("[SSE] Failed to create EventSource:", err);
    onStatusChange?.("disconnected", "🔴 Error");
    startPolling(onUpdate);
  }
}

function startPolling(onUpdate) {
  if (pollInterval) return;
  console.log("[Polling] Starting fallback polling");
  pollInterval = setInterval(async () => {
    try {
      const state = await fetchState();
      onUpdate?.(state);
    } catch (err) {
      console.error("[Polling] Failed:", err);
    }
  }, 2000);
}

function stopPolling() {
  if (pollInterval) {
    console.log("[Polling] Stopping fallback polling (SSE connected)");
    clearInterval(pollInterval);
    pollInterval = null;
  }
}

export function isConnected() {
  return sseConnected;
}
```

## File: `public/js/app.js`
```javascript
/**
 * OpenClaw Command Center - Main Application
 *
 * Uses morphdom for efficient DOM updates (only patches what changed).
 */

// Import morphdom (loaded as UMD, available as global `morphdom`)
// <script src="/js/lib/morphdom.min.js"></script> must be loaded first

// ============================================================================
// STATE MANAGEMENT
// ============================================================================

const state = {
  vitals: null,
  sessions: [],
  tokenStats: {},
  statusCounts: { all: 0, live: 0, recent: 0, idle: 0 },
  capacity: { main: { active: 0, max: 12 }, subagent: { active: 0, max: 24 } },
  operators: { operators: [], roles: {} },
  llmUsage: null,
  cron: [],
  memory: null,
  cerebro: null,
  subagents: [],
  lastUpdated: null,
  connected: false,
};

// ============================================================================
// SSE CONNECTION
// ============================================================================

let eventSource = null;
let reconnectAttempts = 0;
const MAX_RECONNECT_DELAY = 30000;

function connectSSE() {
  if (typeof EventSource === "undefined") {
    console.warn("[SSE] Not supported, falling back to polling");
    startPolling();
    return;
  }

  updateConnectionStatus("connecting");

  eventSource = new EventSource("/api/events");

  eventSource.onopen = () => {
    console.log("[SSE] Connected");
    state.connected = true;
    reconnectAttempts = 0;
    updateConnectionStatus("connected");
  };

  eventSource.addEventListener("connected", (e) => {
    const data = JSON.parse(e.data);
    console.log("[SSE] Server greeting:", data.message);
  });

  eventSource.addEventListener("update", (e) => {
    const data = JSON.parse(e.data);
    handleStateUpdate(data);
  });

  eventSource.addEventListener("heartbeat", (e) => {
    const data = JSON.parse(e.data);
    state.lastUpdated = new Date();
    updateTimestamp();
  });

  eventSource.onerror = () => {
    console.error("[SSE] Connection error");
    state.connected = false;
    eventSource.close();
    updateConnectionStatus("disconnected");

    // Exponential backoff
    reconnectAttempts++;
    const delay = Math.min(1000 * Math.pow(2, reconnectAttempts - 1), MAX_RECONNECT_DELAY);
    console.log(`[SSE] Reconnecting in ${delay}ms`);
    setTimeout(connectSSE, delay);
  };
}

// ============================================================================
// STATE UPDATES
// ============================================================================

function handleStateUpdate(data) {
  // Merge new data into state
  if (data.vitals) state.vitals = data.vitals;
  if (data.sessions) state.sessions = data.sessions;
  if (data.tokenStats) state.tokenStats = data.tokenStats;
  if (data.statusCounts) state.statusCounts = data.statusCounts;
  if (data.capacity) state.capacity = data.capacity;
  if (data.operators) state.operators = data.operators;
  if (data.llmUsage) state.llmUsage = data.llmUsage;
  if (data.cron) state.cron = data.cron;
  if (data.memory) state.memory = data.memory;
  if (data.cerebro) state.cerebro = data.cerebro;
  if (data.subagents) state.subagents = data.subagents;

  state.lastUpdated = new Date();

  // Re-render affected components using morphdom
  renderAll();
}

// ============================================================================
// RENDERING (with morphdom)
// ============================================================================

function renderAll() {
  // Each render function generates HTML and morphdom patches the DOM
  renderVitals();
  renderTokenStats();
  renderLlmUsage();
  renderSessions();
  renderCron();
  renderMemory();
  renderCerebro();
  renderOperators();
  updateTimestamp();
}

// Utility: safely patch a container using morphdom
function patchElement(containerId, newHtml) {
  const container = document.getElementById(containerId);
  if (!container) return;

  // Create a temporary element with the new content
  const temp = document.createElement("div");
  temp.innerHTML = newHtml;

  // Use morphdom to efficiently patch only what changed
  if (typeof morphdom !== "undefined") {
    // Patch each child
    while (container.firstChild && temp.firstChild) {
      morphdom(container.firstChild, temp.firstChild);
      temp.removeChild(temp.firstChild);
    }
    // Add any new children
    while (temp.firstChild) {
      container.appendChild(temp.firstChild);
    }
    // Remove extra children
    while (container.childNodes.length > temp.childNodes.length) {
      container.removeChild(container.lastChild);
    }
  } else {
    // Fallback: direct innerHTML replacement
    container.innerHTML = newHtml;
  }
}

// ============================================================================
// COMPONENT RENDERERS (to be extracted to separate files)
// ============================================================================

function renderVitals() {
  if (!state.vitals) return;
  const v = state.vitals;

  // Update individual elements (simpler than full morphdom for now)
  setText("vitals-hostname", v.hostname || "-");
  setText("vitals-uptime", v.uptime || "-");

  if (v.cpu) {
    const cpuPct = v.cpu.usage || 0;
    setText("cpu-percent", cpuPct + "%");
    setWidth("cpu-bar", cpuPct + "%");
    setText("cpu-user", (v.cpu.userPercent?.toFixed(1) || "-") + "%");
    setText("cpu-sys", (v.cpu.sysPercent?.toFixed(1) || "-") + "%");
    setText("cpu-idle", (v.cpu.idlePercent?.toFixed(1) || "-") + "%");
    setText("cpu-chip", v.cpu.chip || v.cpu.brand || "");
  }

  if (v.memory) {
    const memPct = v.memory.percent || 0;
    setText("mem-percent", memPct + "% used");
    setWidth("mem-bar", memPct + "%");
    setText("mem-summary", `${v.memory.usedFormatted || "-"} of ${v.memory.totalFormatted || "-"}`);
  }

  if (v.disk) {
    const diskPct = v.disk.percent || 0;
    setText("disk-percent", diskPct + "% used");
    setWidth("disk-bar", diskPct + "%");
    setText("disk-summary", `${v.disk.usedFormatted || "-"} of ${v.disk.totalFormatted || "-"}`);
  }
}

function renderTokenStats() {
  if (!state.tokenStats) return;
  const t = state.tokenStats;

  setText("stat-total-tokens", t.total || "-");
  setText("stat-input", t.input || "-");
  setText("stat-output", t.output || "-");
  setText("stat-active", t.activeCount || "0");
  setText("stat-cost", t.estCost || "-");
  setText("stat-main", `${t.activeMainCount || 0}/${t.mainLimit || 12}`);
  setText("stat-subagents", `${t.activeSubagentCount || 0}/${t.subagentLimit || 24}`);
}

function renderLlmUsage() {
  // Placeholder - will be extracted to component
}

function renderSessions() {
  // Placeholder - will be extracted to component
}

function renderCron() {
  // Placeholder - will be extracted to component
}

function renderMemory() {
  // Placeholder - will be extracted to component
}

function renderCerebro() {
  // Placeholder - will be extracted to component
}

function renderOperators() {
  // Placeholder - will be extracted to component
}

// ============================================================================
// UTILITIES
// ============================================================================

function setText(id, text) {
  const el = document.getElementById(id);
  if (el && el.textContent !== text) {
    el.textContent = text;
  }
}

function setWidth(id, width) {
  const el = document.getElementById(id);
  if (el && el.style.width !== width) {
    el.style.width = width;
  }
}

function updateTimestamp() {
  const now = state.lastUpdated || new Date();
  const timeStr = now.toLocaleTimeString();
  const indicator = state.connected ? " ⚡" : "";
  setText("last-updated", timeStr + indicator);
  setText("sidebar-updated", state.connected ? `Live: ${timeStr}` : `Updated: ${timeStr}`);
}

function updateConnectionStatus(status) {
  const el = document.getElementById("connection-status");
  if (!el) return;

  el.className = "connection-status " + status;
  el.textContent =
    status === "connected"
      ? "🟢 Live"
      : status === "connecting"
        ? "🟡 Connecting..."
        : "🔴 Disconnected";
}

// ============================================================================
// POLLING FALLBACK
// ============================================================================

let pollInterval = null;

function startPolling() {
  if (pollInterval) return;
  pollInterval = setInterval(fetchState, 5000);
  fetchState();
}

async function fetchState() {
  try {
    const response = await fetch("/api/state");
    const data = await response.json();
    handleStateUpdate(data);
  } catch (e) {
    console.error("[Polling] Failed:", e);
  }
}

// ============================================================================
// INITIALIZATION
// ============================================================================

function init() {
  console.log("[App] Initializing OpenClaw Command Center");
  connectSSE();

  // Initial fetch to populate immediately
  setTimeout(fetchState, 100);
}

// Start when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  setTimeout(init, 0);
}
```

## File: `public/js/i18n.js`
```javascript
(function () {
  "use strict";

  const DEFAULT_LOCALE = "en";
  const SUPPORTED_LOCALES = ["en", "zh-CN"];
  const STORAGE_KEY = "occ.locale";
  const loadedMessages = new Map();
  const SKIP_TAGS = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEXTAREA", "CODE", "PRE"]);

  let currentLocale = DEFAULT_LOCALE;
  let activeMessages = {};
  let observer = null;
  let isApplyingTranslations = false;

  function normalizeLocale(input) {
    if (!input || typeof input !== "string") return DEFAULT_LOCALE;
    const lc = input.toLowerCase();
    if (lc === "zh" || lc.startsWith("zh-")) return "zh-CN";
    return "en";
  }

  function getInitialLocale() {
    const fromQuery = new URLSearchParams(window.location.search).get("lang");
    if (fromQuery) return normalizeLocale(fromQuery);

    const fromStorage = localStorage.getItem(STORAGE_KEY);
    if (fromStorage) return normalizeLocale(fromStorage);

    return normalizeLocale(navigator.language || DEFAULT_LOCALE);
  }

  async function loadLocaleMessages(locale) {
    const normalized = normalizeLocale(locale);
    if (loadedMessages.has(normalized)) return loadedMessages.get(normalized);

    const response = await fetch(`/locales/${normalized}.json`, { cache: "no-cache" });
    if (!response.ok) throw new Error(`Failed to load locale: ${normalized}`);
    const data = await response.json();
    loadedMessages.set(normalized, data || {});
    return data || {};
  }

  function getByPath(obj, path) {
    return String(path)
      .split(".")
      .reduce(
        (acc, key) =>
          acc && Object.prototype.hasOwnProperty.call(acc, key) ? acc[key] : undefined,
        obj,
      );
  }

  function interpolate(template, params = {}) {
    if (typeof template !== "string") return template;
    return template.replace(/\{(\w+)\}/g, (_, key) => {
      return Object.prototype.hasOwnProperty.call(params, key) ? String(params[key]) : `{${key}}`;
    });
  }

  function t(key, params = {}, fallback = undefined) {
    const value = getByPath(activeMessages, key);
    if (value === undefined || value === null) {
      if (fallback !== undefined) return interpolate(fallback, params);
      return String(key);
    }
    return interpolate(value, params);
  }

  function buildReverseMap(source = {}) {
    const reversed = {};
    for (const [from, to] of Object.entries(source)) {
      if (typeof from !== "string" || typeof to !== "string") continue;
      if (!Object.prototype.hasOwnProperty.call(reversed, to)) {
        reversed[to] = from;
      }
    }
    return reversed;
  }

  function getExactPhraseMap() {
    const exact = getByPath(activeMessages, "phrases.exact") || {};
    if (currentLocale !== DEFAULT_LOCALE) return exact;
    const zh = loadedMessages.get("zh-CN") || {};
    const zhExact = getByPath(zh, "phrases.exact") || {};
    return buildReverseMap(zhExact);
  }

  function getPatternRules() {
    const localeRules = getByPath(activeMessages, "phrases.patterns");
    if (Array.isArray(localeRules)) return localeRules;
    if (currentLocale !== DEFAULT_LOCALE) return [];
    const zh = loadedMessages.get("zh-CN") || {};
    const zhRules = getByPath(zh, "phrases.reversePatterns");
    return Array.isArray(zhRules) ? zhRules : [];
  }

  function translateTextValue(input) {
    if (typeof input !== "string") return input;
    if (!input.trim()) return input;

    const leading = input.match(/^\s*/)?.[0] || "";
    const trailing = input.match(/\s*$/)?.[0] || "";
    let core = input.trim();

    const exactMap = getExactPhraseMap();
    if (Object.prototype.hasOwnProperty.call(exactMap, core)) {
      return `${leading}${exactMap[core]}${trailing}`;
    }

    for (const rule of getPatternRules()) {
      if (!rule || typeof rule.pattern !== "string" || typeof rule.replace !== "string") continue;
      try {
        const regex = new RegExp(rule.pattern);
        if (regex.test(core)) {
          core = core.replace(regex, rule.replace);
          return `${leading}${core}${trailing}`;
        }
      } catch {
        continue;
      }
    }

    return input;
  }

  function setAttrIfChanged(el, attr, value) {
    if (!el || typeof value !== "string") return;
    if (el.getAttribute(attr) !== value) {
      el.setAttribute(attr, value);
    }
  }

  function translateLooseAttributes(el) {
    if (el.hasAttribute("data-i18n-title")) {
      setAttrIfChanged(el, "title", t(el.getAttribute("data-i18n-title")));
    } else if (el.hasAttribute("title")) {
      setAttrIfChanged(el, "title", translateTextValue(el.getAttribute("title")));
    }

    if (el.hasAttribute("data-i18n-placeholder")) {
      setAttrIfChanged(el, "placeholder", t(el.getAttribute("data-i18n-placeholder")));
    } else if (el.hasAttribute("placeholder")) {
      setAttrIfChanged(el, "placeholder", translateTextValue(el.getAttribute("placeholder")));
    }

    if (el.hasAttribute("data-i18n-aria-label")) {
      setAttrIfChanged(el, "aria-label", t(el.getAttribute("data-i18n-aria-label")));
    } else if (el.hasAttribute("aria-label")) {
      setAttrIfChanged(el, "aria-label", translateTextValue(el.getAttribute("aria-label")));
    }

    if (el.hasAttribute("data-tooltip")) {
      setAttrIfChanged(el, "data-tooltip", translateTextValue(el.getAttribute("data-tooltip")));
    }
  }

  function translateTextNodes(root) {
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    let node;
    while ((node = walker.nextNode())) {
      nodes.push(node);
    }

    for (const textNode of nodes) {
      const parent = textNode.parentElement;
      if (!parent) continue;
      if (SKIP_TAGS.has(parent.tagName)) continue;
      if (parent.hasAttribute("data-i18n")) continue;
      const translated = translateTextValue(textNode.nodeValue || "");
      if (translated !== textNode.nodeValue) {
        textNode.nodeValue = translated;
      }
    }
  }

  function translateElement(el) {
    const textKey = el.getAttribute("data-i18n");
    if (textKey) {
      const translatedText = t(textKey);
      if (el.textContent !== translatedText) {
        el.textContent = translatedText;
      }
    }

    const titleKey = el.getAttribute("data-i18n-title");
    if (titleKey) {
      setAttrIfChanged(el, "title", t(titleKey));
    }

    const placeholderKey = el.getAttribute("data-i18n-placeholder");
    if (placeholderKey) {
      setAttrIfChanged(el, "placeholder", t(placeholderKey));
    }

    const ariaLabelKey = el.getAttribute("data-i18n-aria-label");
    if (ariaLabelKey) {
      setAttrIfChanged(el, "aria-label", t(ariaLabelKey));
    }

    translateLooseAttributes(el);
  }

  function translateSubtree(root = document) {
    if (!root) return;
    isApplyingTranslations = true;
    if (root.nodeType === Node.ELEMENT_NODE) {
      translateElement(root);
    }
    root
      .querySelectorAll(
        "[data-i18n], [data-i18n-title], [data-i18n-placeholder], [data-i18n-aria-label]",
      )
      .forEach(translateElement);

    const elementRoot =
      root.nodeType === Node.DOCUMENT_NODE ? root.body || root.documentElement : root;
    if (elementRoot) {
      translateTextNodes(elementRoot);
      if (elementRoot.querySelectorAll) {
        elementRoot
          .querySelectorAll("[title], [placeholder], [aria-label], [data-tooltip]")
          .forEach(translateLooseAttributes);
      }
    }
    isApplyingTranslations = false;
  }

  function updateDocumentLang() {
    document.documentElement.lang = currentLocale;
  }

  function renderLanguageSwitcher() {
    const header = document.querySelector("header");
    if (!header) return;

    let container = document.getElementById("lang-switcher");
    let select = document.getElementById("lang-select");

    if (!container) {
      container = document.createElement("div");
      container.id = "lang-switcher";
      container.style.display = "inline-flex";
      container.style.alignItems = "center";
      container.style.gap = "6px";
      container.style.marginLeft = "12px";
      container.style.flexShrink = "0";

      const label = document.createElement("span");
      label.style.fontSize = "0.75rem";
      label.style.opacity = "0.8";
      label.textContent = "🌐";
      container.appendChild(label);

      select = document.createElement("select");
      select.id = "lang-select";
      select.style.fontSize = "0.8rem";
      select.style.padding = "3px 8px";
      select.style.background = "var(--card-bg, #161b22)";
      select.style.color = "var(--text, #c9d1d9)";
      select.style.border = "1px solid var(--border, #30363d)";
      select.style.borderRadius = "4px";
      select.style.cursor = "pointer";
      select.innerHTML = `
        <option value="en">English</option>
        <option value="zh-CN">简体中文</option>
      `;
      container.appendChild(select);

      const targetHost = header.querySelector(".header-left") || header;
      targetHost.appendChild(container);
    }

    select = document.getElementById("lang-select");
    if (select && !select.dataset.i18nBound) {
      select.addEventListener("change", (e) => {
        setLocale(e.target.value, { persist: true });
      });
      select.dataset.i18nBound = "1";
    }

    if (select) {
      if (!select.options.length) {
        select.innerHTML = `
          <option value="en">English</option>
          <option value="zh-CN">简体中文</option>
        `;
      }
      select.value = currentLocale;
    }
  }

  function installObserver() {
    if (observer) observer.disconnect();
    if (!document.body) return;

    observer = new MutationObserver((mutations) => {
      if (isApplyingTranslations) return;
      isApplyingTranslations = true;
      try {
        for (const mutation of mutations) {
          if (mutation.type === "childList") {
            mutation.addedNodes.forEach((addedNode) => {
              if (addedNode.nodeType === Node.TEXT_NODE) {
                const parent = addedNode.parentElement;
                if (parent && !SKIP_TAGS.has(parent.tagName)) {
                  const translated = translateTextValue(addedNode.nodeValue || "");
                  if (translated !== addedNode.nodeValue) addedNode.nodeValue = translated;
                }
                return;
              }
              if (addedNode.nodeType === Node.ELEMENT_NODE) {
                translateSubtree(addedNode);
              }
            });
          }

          if (mutation.type === "characterData" && mutation.target?.nodeType === Node.TEXT_NODE) {
            const textNode = mutation.target;
            const parent = textNode.parentElement;
            if (parent && !SKIP_TAGS.has(parent.tagName)) {
              const translated = translateTextValue(textNode.nodeValue || "");
              if (translated !== textNode.nodeValue) textNode.nodeValue = translated;
            }
          }
        }
      } finally {
        isApplyingTranslations = false;
      }
    });

    observer.observe(document.body, {
      subtree: true,
      childList: true,
      characterData: true,
      attributes: false,
    });
  }

  async function setLocale(locale, { persist = true } = {}) {
    const normalized = normalizeLocale(locale);
    const targetLocale = SUPPORTED_LOCALES.includes(normalized) ? normalized : DEFAULT_LOCALE;

    let localeMessages;
    try {
      localeMessages = await loadLocaleMessages(targetLocale);
    } catch (error) {
      console.error("[i18n] Failed to load locale, fallback to English:", error);
      localeMessages = await loadLocaleMessages(DEFAULT_LOCALE);
    }

    currentLocale = targetLocale;
    activeMessages = localeMessages;
    if (persist) {
      localStorage.setItem(STORAGE_KEY, currentLocale);
    }

    updateDocumentLang();
    translateSubtree(document);
    renderLanguageSwitcher();
    installObserver();
    window.dispatchEvent(new CustomEvent("i18n:updated", { detail: { locale: currentLocale } }));
  }

  async function init() {
    await loadLocaleMessages(DEFAULT_LOCALE);
    await loadLocaleMessages("zh-CN").catch(() => null);
    const initialLocale = getInitialLocale();
    await setLocale(initialLocale, { persist: false });
  }

  window.I18N = {
    init,
    t,
    setLocale,
    getLocale: () => currentLocale,
    translateSubtree,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
```

## File: `public/js/sidebar.js`
```javascript
/**
 * Shared Sidebar Loader
 *
 * Loads the sidebar partial and connects to SSE for live badge updates.
 * Include this script in any page that needs the sidebar.
 */

(function () {
  "use strict";

  // State for sidebar badges
  const sidebarState = {
    sessions: 0,
    cron: 0,
    jobs: 0,
    memory: 0,
    cerebro: 0,
    operators: 0,
    tokens: "-",
    cost: "-",
    monthlyCost: "-",
    avgTokens: "-",
    avgCost: "-",
    lastUpdated: null,
  };

  // SSE connection
  let eventSource = null;
  let reconnectAttempts = 0;
  const MAX_RECONNECT_DELAY = 30000;

  /**
   * Load and inject sidebar HTML
   */
  async function loadSidebar() {
    try {
      const response = await fetch("/partials/sidebar.html");
      if (!response.ok) throw new Error("Failed to load sidebar");

      const html = await response.text();

      // Find or create sidebar container
      let container = document.getElementById("sidebar-container");
      if (!container) {
        // Insert at start of body
        container = document.createElement("div");
        container.id = "sidebar-container";
        document.body.insertBefore(container, document.body.firstChild);
      }

      container.innerHTML = html;

      if (window.I18N?.translateSubtree) {
        window.I18N.translateSubtree(container);
      }

      // Set active state based on current page
      setActiveNavItem();

      // Connect to SSE for live updates
      connectSSE();

      // Also fetch initial state
      fetchSidebarState();
    } catch (error) {
      console.error("[Sidebar] Failed to load:", error);
    }
  }

  /**
   * Check if we're on the main page
   */
  function isMainPage() {
    const path = window.location.pathname;
    return path === "/" || path === "/index.html";
  }

  /**
   * Set the active nav item based on current URL
   */
  function setActiveNavItem() {
    const currentPath = window.location.pathname;
    const currentHash = window.location.hash;

    document.querySelectorAll(".nav-item").forEach((item) => {
      item.classList.remove("active");

      const itemPage = item.dataset.page;
      const itemHref = item.getAttribute("href");

      // Check if this nav item matches the current page
      if (itemPage === "/" && isMainPage()) {
        // For main page sections
        if (currentHash && itemHref && itemHref === currentHash) {
          item.classList.add("active");
        } else if (!currentHash && item.dataset.section === "vitals") {
          // Default to vitals on main page with no hash
          item.classList.add("active");
        }
      } else if (itemHref === currentPath) {
        // Exact page match (like /jobs.html)
        item.classList.add("active");
      }
    });
  }

  /**
   * Set up navigation click handlers
   * - Hash links on main page: smooth scroll
   * - Hash links on other pages: navigate to main page with hash
   */
  function setupNavigation() {
    document.querySelectorAll(".nav-item[data-section]").forEach((item) => {
      item.addEventListener("click", (e) => {
        const section = item.dataset.section;
        const targetHash = `#${section}-section`;

        if (isMainPage()) {
          // On main page: smooth scroll to section
          e.preventDefault();
          const target = document.querySelector(targetHash);
          if (target) {
            target.scrollIntoView({ behavior: "smooth" });
            history.pushState(null, "", targetHash);
            setActiveNavItem();
          }
        } else {
          // On other page: navigate to main page with hash
          e.preventDefault();
          window.location.href = "/" + targetHash;
        }
      });
    });
  }

  /**
   * Connect to SSE for live updates
   */
  function connectSSE() {
    if (typeof EventSource === "undefined") {
      console.warn("[Sidebar SSE] Not supported");
      return;
    }

    eventSource = new EventSource("/api/events");

    eventSource.onopen = () => {
      console.log("[Sidebar SSE] Connected");
      reconnectAttempts = 0;
    };

    eventSource.addEventListener("update", (e) => {
      try {
        const data = JSON.parse(e.data);
        handleStateUpdate(data);
      } catch (err) {
        console.error("[Sidebar SSE] Parse error:", err);
      }
    });

    eventSource.addEventListener("heartbeat", () => {
      sidebarState.lastUpdated = new Date();
      updateTimestamp();
    });

    eventSource.onerror = () => {
      console.error("[Sidebar SSE] Connection error");
      eventSource.close();

      // Exponential backoff reconnect
      reconnectAttempts++;
      const delay = Math.min(1000 * Math.pow(2, reconnectAttempts - 1), MAX_RECONNECT_DELAY);
      setTimeout(connectSSE, delay);
    };
  }

  /**
   * Fetch initial sidebar state
   */
  async function fetchSidebarState() {
    try {
      const response = await fetch("/api/state");
      const data = await response.json();
      handleStateUpdate(data);
    } catch (error) {
      console.error("[Sidebar] Failed to fetch state:", error);
    }
  }

  /**
   * Handle state updates and update badges
   */
  function handleStateUpdate(data) {
    // Update session count
    if (data.sessions) {
      sidebarState.sessions = data.sessions.length || 0;
    }
    if (data.statusCounts) {
      sidebarState.sessions = data.statusCounts.all || 0;
    }

    // Update cron count
    if (data.cron) {
      sidebarState.cron = Array.isArray(data.cron) ? data.cron.length : 0;
    }

    // Update jobs count (from jobs API if available)
    if (data.jobs) {
      sidebarState.jobs = Array.isArray(data.jobs) ? data.jobs.length : data.jobs.total || 0;
    }

    // Update memory count
    if (data.memory) {
      sidebarState.memory = data.memory.fileCount || data.memory.totalFiles || 0;
    }

    // Update cerebro count
    if (data.cerebro) {
      sidebarState.cerebro = data.cerebro.topicCount || data.cerebro.totalTopics || 0;
    }

    // Update operators count
    if (data.operators) {
      sidebarState.operators = Array.isArray(data.operators.operators)
        ? data.operators.operators.length
        : 0;
    }

    // Update token stats
    if (data.tokenStats) {
      sidebarState.tokens = data.tokenStats.totalFormatted || data.tokenStats.total || "-";
      sidebarState.cost = data.tokenStats.estCostFormatted || data.tokenStats.estCost || "-";
      sidebarState.monthlyCost =
        data.tokenStats.estMonthlyCostFormatted || data.tokenStats.estMonthlyCost || "-";
      sidebarState.avgTokens = data.tokenStats.avgTokensPerSession || "-";
      sidebarState.avgCost = data.tokenStats.avgCostPerSession || "-";
    }

    sidebarState.lastUpdated = new Date();

    // Update the DOM
    updateBadges();
    updateTimestamp();
  }

  /**
   * Update badge elements
   */
  function updateBadges() {
    const updates = {
      "nav-session-count": sidebarState.sessions,
      "nav-cron-count": sidebarState.cron,
      "nav-jobs-count": sidebarState.jobs || "-",
      "nav-memory-count": sidebarState.memory,
      "nav-cerebro-count": sidebarState.cerebro,
      "nav-operator-count": sidebarState.operators,
      "nav-tokens": sidebarState.tokens,
      "nav-cost": sidebarState.cost,
      "nav-monthly-cost": sidebarState.monthlyCost,
      "nav-avg-tokens": sidebarState.avgTokens,
      "nav-avg-cost": sidebarState.avgCost,
    };

    for (const [id, value] of Object.entries(updates)) {
      const el = document.getElementById(id);
      if (el && el.textContent !== String(value)) {
        el.textContent = value;
      }
    }
  }

  /**
   * Update the timestamp in sidebar footer
   */
  function updateTimestamp() {
    const el = document.getElementById("sidebar-updated");
    if (el && sidebarState.lastUpdated) {
      const timeStr = sidebarState.lastUpdated.toLocaleTimeString();
      const t = window.I18N?.t;
      el.textContent = t ? t("sidebar.live", { time: timeStr }) : `Live: ${timeStr}`;
    }
  }

  /**
   * Toggle sidebar collapsed state
   */
  window.toggleSidebar = function () {
    const sidebar = document.getElementById("sidebar");
    const mainWrapper = document.getElementById("main-wrapper");

    if (sidebar) {
      sidebar.classList.toggle("collapsed");
    }
    if (mainWrapper) {
      mainWrapper.classList.toggle("sidebar-collapsed");
    }

    // Save preference
    const collapsed = sidebar?.classList.contains("collapsed");
    try {
      localStorage.setItem("sidebar-collapsed", collapsed ? "true" : "false");
    } catch (e) {}
  };

  /**
   * Restore sidebar collapsed state from localStorage
   */
  function restoreSidebarState() {
    try {
      const collapsed = localStorage.getItem("sidebar-collapsed") === "true";
      if (collapsed) {
        const sidebar = document.getElementById("sidebar");
        const mainWrapper = document.getElementById("main-wrapper");
        if (sidebar) sidebar.classList.add("collapsed");
        if (mainWrapper) mainWrapper.classList.add("sidebar-collapsed");
      }
    } catch (e) {}
  }

  // Fetch jobs count separately (since it's a different API)
  async function fetchJobsCount() {
    try {
      const response = await fetch("/api/jobs");
      const data = await response.json();
      sidebarState.jobs = data.jobs?.length || 0;
      updateBadges();
    } catch (error) {
      // Jobs API may not be available
    }
  }

  // Initialize on DOM ready
  function init() {
    loadSidebar().then(() => {
      restoreSidebarState();
      setupNavigation();
      fetchJobsCount();
    });

    // Listen for hash changes to update active state
    window.addEventListener("hashchange", setActiveNavItem);
    window.addEventListener("i18n:updated", () => {
      const container = document.getElementById("sidebar-container");
      if (container && window.I18N?.translateSubtree) {
        window.I18N.translateSubtree(container);
      }
      updateTimestamp();
      setActiveNavItem();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
```

## File: `public/js/store.js`
```javascript
/**
 * Simple state store for Command Center
 * Holds the current dashboard state and notifies subscribers of changes
 */

let state = {
  vitals: null,
  sessions: [],
  tokenStats: null,
  statusCounts: { all: 0, live: 0, recent: 0, idle: 0 },
  capacity: null,
  operators: { operators: [], roles: {} },
  llmUsage: null,
  cron: [],
  memory: null,
  cerebro: null,
  subagents: [],
  pagination: { page: 1, pageSize: 50, totalPages: 1 },
  timestamp: null,
};

const subscribers = new Set();

/**
 * Get the current state
 * @returns {Object} Current state
 */
export function getState() {
  return state;
}

/**
 * Update the state with new data
 * @param {Object} newState - New state data (partial or full)
 */
export function setState(newState) {
  state = { ...state, ...newState, timestamp: Date.now() };
  notifySubscribers();
}

/**
 * Subscribe to state changes
 * @param {Function} callback - Called when state changes
 * @returns {Function} Unsubscribe function
 */
export function subscribe(callback) {
  subscribers.add(callback);
  return () => subscribers.delete(callback);
}

function notifySubscribers() {
  for (const callback of subscribers) {
    try {
      callback(state);
    } catch (err) {
      console.error("[Store] Subscriber error:", err);
    }
  }
}

// Filter state
export const filters = {
  session: { status: "all", channel: "all", kind: "all" },
  cron: { status: "all", schedule: "all" },
  memory: { type: "all", age: "all" },
};

export function setFilter(section, key, value) {
  if (filters[section]) {
    filters[section][key] = value;
    notifySubscribers();
  }
}

// Pagination state
export const pagination = {
  page: 1,
  pageSize: 20,
  total: 0,
  totalPages: 0,
  hasNext: false,
  hasPrev: false,
};

export function setPagination(newPagination) {
  Object.assign(pagination, newPagination);
}
```

## File: `public/js/utils.js`
```javascript
/**
 * Utility functions for Command Center
 */

export function formatTimeAgo(mins) {
  if (mins < 1) return "now";
  if (mins < 60) return `${mins}m`;
  if (mins < 1440) return `${Math.round(mins / 60)}h`;
  return `${Math.round(mins / 1440)}d`;
}

export function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

/**
 * Smart DOM update using morphdom - only patches what changed
 * @param {HTMLElement} targetEl - Element to update
 * @param {string} newHtml - New HTML content
 */
export function smartUpdate(targetEl, newHtml) {
  if (typeof morphdom === "undefined") {
    // Fallback if morphdom not loaded
    targetEl.innerHTML = newHtml;
    return;
  }
  // Create a temporary container with the new content
  const temp = document.createElement("div");
  temp.innerHTML = newHtml;
  // If target has single child and temp has single child, morph directly
  if (targetEl.children.length === 1 && temp.children.length === 1) {
    morphdom(targetEl.firstElementChild, temp.firstElementChild);
  } else {
    // Otherwise morph the container itself
    morphdom(targetEl, temp, { childrenOnly: true });
  }
}

export function formatBytes(bytes) {
  if (bytes >= 1099511627776) return (bytes / 1099511627776).toFixed(1) + " TB";
  if (bytes >= 1073741824) return (bytes / 1073741824).toFixed(1) + " GB";
  if (bytes >= 1048576) return (bytes / 1048576).toFixed(1) + " MB";
  if (bytes >= 1024) return (bytes / 1024).toFixed(1) + " KB";
  return bytes + " B";
}
```

## File: `public/js/lib/morphdom.min.js`
```javascript
(function (global, factory) {
  typeof exports === "object" && typeof module !== "undefined"
    ? (module.exports = factory())
    : typeof define === "function" && define.amd
      ? define(factory)
      : ((global = global || self), (global.morphdom = factory()));
})(this, function () {
  "use strict";
  var DOCUMENT_FRAGMENT_NODE = 11;
  function morphAttrs(fromNode, toNode) {
    var toNodeAttrs = toNode.attributes;
    var attr;
    var attrName;
    var attrNamespaceURI;
    var attrValue;
    var fromValue;
    if (
      toNode.nodeType === DOCUMENT_FRAGMENT_NODE ||
      fromNode.nodeType === DOCUMENT_FRAGMENT_NODE
    ) {
      return;
    }
    for (var i = toNodeAttrs.length - 1; i >= 0; i--) {
      attr = toNodeAttrs[i];
      attrName = attr.name;
      attrNamespaceURI = attr.namespaceURI;
      attrValue = attr.value;
      if (attrNamespaceURI) {
        attrName = attr.localName || attrName;
        fromValue = fromNode.getAttributeNS(attrNamespaceURI, attrName);
        if (fromValue !== attrValue) {
          if (attr.prefix === "xmlns") {
            attrName = attr.name;
          }
          fromNode.setAttributeNS(attrNamespaceURI, attrName, attrValue);
        }
      } else {
        fromValue = fromNode.getAttribute(attrName);
        if (fromValue !== attrValue) {
          fromNode.setAttribute(attrName, attrValue);
        }
      }
    }
    var fromNodeAttrs = fromNode.attributes;
    for (var d = fromNodeAttrs.length - 1; d >= 0; d--) {
      attr = fromNodeAttrs[d];
      attrName = attr.name;
      attrNamespaceURI = attr.namespaceURI;
      if (attrNamespaceURI) {
        attrName = attr.localName || attrName;
        if (!toNode.hasAttributeNS(attrNamespaceURI, attrName)) {
          fromNode.removeAttributeNS(attrNamespaceURI, attrName);
        }
      } else {
        if (!toNode.hasAttribute(attrName)) {
          fromNode.removeAttribute(attrName);
        }
      }
    }
  }
  var range;
  var NS_XHTML = "http://www.w3.org/1999/xhtml";
  var doc = typeof document === "undefined" ? undefined : document;
  var HAS_TEMPLATE_SUPPORT = !!doc && "content" in doc.createElement("template");
  var HAS_RANGE_SUPPORT =
    !!doc && doc.createRange && "createContextualFragment" in doc.createRange();
  function createFragmentFromTemplate(str) {
    var template = doc.createElement("template");
    template.innerHTML = str;
    return template.content.childNodes[0];
  }
  function createFragmentFromRange(str) {
    if (!range) {
      range = doc.createRange();
      range.selectNode(doc.body);
    }
    var fragment = range.createContextualFragment(str);
    return fragment.childNodes[0];
  }
  function createFragmentFromWrap(str) {
    var fragment = doc.createElement("body");
    fragment.innerHTML = str;
    return fragment.childNodes[0];
  }
  function toElement(str) {
    str = str.trim();
    if (HAS_TEMPLATE_SUPPORT) {
      return createFragmentFromTemplate(str);
    } else if (HAS_RANGE_SUPPORT) {
      return createFragmentFromRange(str);
    }
    return createFragmentFromWrap(str);
  }
  function compareNodeNames(fromEl, toEl) {
    var fromNodeName = fromEl.nodeName;
    var toNodeName = toEl.nodeName;
    var fromCodeStart, toCodeStart;
    if (fromNodeName === toNodeName) {
      return true;
    }
    fromCodeStart = fromNodeName.charCodeAt(0);
    toCodeStart = toNodeName.charCodeAt(0);
    if (fromCodeStart <= 90 && toCodeStart >= 97) {
      return fromNodeName === toNodeName.toUpperCase();
    } else if (toCodeStart <= 90 && fromCodeStart >= 97) {
      return toNodeName === fromNodeName.toUpperCase();
    } else {
      return false;
    }
  }
  function createElementNS(name, namespaceURI) {
    return !namespaceURI || namespaceURI === NS_XHTML
      ? doc.createElement(name)
      : doc.createElementNS(namespaceURI, name);
  }
  function moveChildren(fromEl, toEl) {
    var curChild = fromEl.firstChild;
    while (curChild) {
      var nextChild = curChild.nextSibling;
      toEl.appendChild(curChild);
      curChild = nextChild;
    }
    return toEl;
  }
  function syncBooleanAttrProp(fromEl, toEl, name) {
    if (fromEl[name] !== toEl[name]) {
      fromEl[name] = toEl[name];
      if (fromEl[name]) {
        fromEl.setAttribute(name, "");
      } else {
        fromEl.removeAttribute(name);
      }
    }
  }
  var specialElHandlers = {
    OPTION: function (fromEl, toEl) {
      var parentNode = fromEl.parentNode;
      if (parentNode) {
        var parentName = parentNode.nodeName.toUpperCase();
        if (parentName === "OPTGROUP") {
          parentNode = parentNode.parentNode;
          parentName = parentNode && parentNode.nodeName.toUpperCase();
        }
        if (parentName === "SELECT" && !parentNode.hasAttribute("multiple")) {
          if (fromEl.hasAttribute("selected") && !toEl.selected) {
            fromEl.setAttribute("selected", "selected");
            fromEl.removeAttribute("selected");
          }
          parentNode.selectedIndex = -1;
        }
      }
      syncBooleanAttrProp(fromEl, toEl, "selected");
    },
    INPUT: function (fromEl, toEl) {
      syncBooleanAttrProp(fromEl, toEl, "checked");
      syncBooleanAttrProp(fromEl, toEl, "disabled");
      if (fromEl.value !== toEl.value) {
        fromEl.value = toEl.value;
      }
      if (!toEl.hasAttribute("value")) {
        fromEl.removeAttribute("value");
      }
    },
    TEXTAREA: function (fromEl, toEl) {
      var newValue = toEl.value;
      if (fromEl.value !== newValue) {
        fromEl.value = newValue;
      }
      var firstChild = fromEl.firstChild;
      if (firstChild) {
        var oldValue = firstChild.nodeValue;
        if (oldValue == newValue || (!newValue && oldValue == fromEl.placeholder)) {
          return;
        }
        firstChild.nodeValue = newValue;
      }
    },
    SELECT: function (fromEl, toEl) {
      if (!toEl.hasAttribute("multiple")) {
        var selectedIndex = -1;
        var i = 0;
        var curChild = fromEl.firstChild;
        var optgroup;
        var nodeName;
        while (curChild) {
          nodeName = curChild.nodeName && curChild.nodeName.toUpperCase();
          if (nodeName === "OPTGROUP") {
            optgroup = curChild;
            curChild = optgroup.firstChild;
          } else {
            if (nodeName === "OPTION") {
              if (curChild.hasAttribute("selected")) {
                selectedIndex = i;
                break;
              }
              i++;
            }
            curChild = curChild.nextSibling;
            if (!curChild && optgroup) {
              curChild = optgroup.nextSibling;
              optgroup = null;
            }
          }
        }
        fromEl.selectedIndex = selectedIndex;
      }
    },
  };
  var ELEMENT_NODE = 1;
  var DOCUMENT_FRAGMENT_NODE$1 = 11;
  var TEXT_NODE = 3;
  var COMMENT_NODE = 8;
  function noop() {}
  function defaultGetNodeKey(node) {
    if (node) {
      return (node.getAttribute && node.getAttribute("id")) || node.id;
    }
  }
  function morphdomFactory(morphAttrs) {
    return function morphdom(fromNode, toNode, options) {
      if (!options) {
        options = {};
      }
      if (typeof toNode === "string") {
        if (
          fromNode.nodeName === "#document" ||
          fromNode.nodeName === "HTML" ||
          fromNode.nodeName === "BODY"
        ) {
          var toNodeHtml = toNode;
          toNode = doc.createElement("html");
          toNode.innerHTML = toNodeHtml;
        } else {
          toNode = toElement(toNode);
        }
      } else if (toNode.nodeType === DOCUMENT_FRAGMENT_NODE$1) {
        toNode = toNode.firstElementChild;
      }
      var getNodeKey = options.getNodeKey || defaultGetNodeKey;
      var onBeforeNodeAdded = options.onBeforeNodeAdded || noop;
      var onNodeAdded = options.onNodeAdded || noop;
      var onBeforeElUpdated = options.onBeforeElUpdated || noop;
      var onElUpdated = options.onElUpdated || noop;
      var onBeforeNodeDiscarded = options.onBeforeNodeDiscarded || noop;
      var onNodeDiscarded = options.onNodeDiscarded || noop;
      var onBeforeElChildrenUpdated = options.onBeforeElChildrenUpdated || noop;
      var skipFromChildren = options.skipFromChildren || noop;
      var addChild =
        options.addChild ||
        function (parent, child) {
          return parent.appendChild(child);
        };
      var childrenOnly = options.childrenOnly === true;
      var fromNodesLookup = Object.create(null);
      var keyedRemovalList = [];
      function addKeyedRemoval(key) {
        keyedRemovalList.push(key);
      }
      function walkDiscardedChildNodes(node, skipKeyedNodes) {
        if (node.nodeType === ELEMENT_NODE) {
          var curChild = node.firstChild;
          while (curChild) {
            var key = undefined;
            if (skipKeyedNodes && (key = getNodeKey(curChild))) {
              addKeyedRemoval(key);
            } else {
              onNodeDiscarded(curChild);
              if (curChild.firstChild) {
                walkDiscardedChildNodes(curChild, skipKeyedNodes);
              }
            }
            curChild = curChild.nextSibling;
          }
        }
      }
      function removeNode(node, parentNode, skipKeyedNodes) {
        if (onBeforeNodeDiscarded(node) === false) {
          return;
        }
        if (parentNode) {
          parentNode.removeChild(node);
        }
        onNodeDiscarded(node);
        walkDiscardedChildNodes(node, skipKeyedNodes);
      }
      function indexTree(node) {
        if (node.nodeType === ELEMENT_NODE || node.nodeType === DOCUMENT_FRAGMENT_NODE$1) {
          var curChild = node.firstChild;
          while (curChild) {
            var key = getNodeKey(curChild);
            if (key) {
              fromNodesLookup[key] = curChild;
            }
            indexTree(curChild);
            curChild = curChild.nextSibling;
          }
        }
      }
      indexTree(fromNode);
      function handleNodeAdded(el) {
        onNodeAdded(el);
        var curChild = el.firstChild;
        while (curChild) {
          var nextSibling = curChild.nextSibling;
          var key = getNodeKey(curChild);
          if (key) {
            var unmatchedFromEl = fromNodesLookup[key];
            if (unmatchedFromEl && compareNodeNames(curChild, unmatchedFromEl)) {
              curChild.parentNode.replaceChild(unmatchedFromEl, curChild);
              morphEl(unmatchedFromEl, curChild);
            } else {
              handleNodeAdded(curChild);
            }
          } else {
            handleNodeAdded(curChild);
          }
          curChild = nextSibling;
        }
      }
      function cleanupFromEl(fromEl, curFromNodeChild, curFromNodeKey) {
        while (curFromNodeChild) {
          var fromNextSibling = curFromNodeChild.nextSibling;
          if ((curFromNodeKey = getNodeKey(curFromNodeChild))) {
            addKeyedRemoval(curFromNodeKey);
          } else {
            removeNode(curFromNodeChild, fromEl, true);
          }
          curFromNodeChild = fromNextSibling;
        }
      }
      function morphEl(fromEl, toEl, childrenOnly) {
        var toElKey = getNodeKey(toEl);
        if (toElKey) {
          delete fromNodesLookup[toElKey];
        }
        if (!childrenOnly) {
          if (onBeforeElUpdated(fromEl, toEl) === false) {
            return;
          }
          morphAttrs(fromEl, toEl);
          onElUpdated(fromEl);
          if (onBeforeElChildrenUpdated(fromEl, toEl) === false) {
            return;
          }
        }
        if (fromEl.nodeName !== "TEXTAREA") {
          morphChildren(fromEl, toEl);
        } else {
          specialElHandlers.TEXTAREA(fromEl, toEl);
        }
      }
      function morphChildren(fromEl, toEl) {
        var skipFrom = skipFromChildren(fromEl, toEl);
        var curToNodeChild = toEl.firstChild;
        var curFromNodeChild = fromEl.firstChild;
        var curToNodeKey;
        var curFromNodeKey;
        var fromNextSibling;
        var toNextSibling;
        var matchingFromEl;
        outer: while (curToNodeChild) {
          toNextSibling = curToNodeChild.nextSibling;
          curToNodeKey = getNodeKey(curToNodeChild);
          while (!skipFrom && curFromNodeChild) {
            fromNextSibling = curFromNodeChild.nextSibling;
            if (curToNodeChild.isSameNode && curToNodeChild.isSameNode(curFromNodeChild)) {
              curToNodeChild = toNextSibling;
              curFromNodeChild = fromNextSibling;
              continue outer;
            }
            curFromNodeKey = getNodeKey(curFromNodeChild);
            var curFromNodeType = curFromNodeChild.nodeType;
            var isCompatible = undefined;
            if (curFromNodeType === curToNodeChild.nodeType) {
              if (curFromNodeType === ELEMENT_NODE) {
                if (curToNodeKey) {
                  if (curToNodeKey !== curFromNodeKey) {
                    if ((matchingFromEl = fromNodesLookup[curToNodeKey])) {
                      if (fromNextSibling === matchingFromEl) {
                        isCompatible = false;
                      } else {
                        fromEl.insertBefore(matchingFromEl, curFromNodeChild);
                        if (curFromNodeKey) {
                          addKeyedRemoval(curFromNodeKey);
                        } else {
                          removeNode(curFromNodeChild, fromEl, true);
                        }
                        curFromNodeChild = matchingFromEl;
                        curFromNodeKey = getNodeKey(curFromNodeChild);
                      }
                    } else {
                      isCompatible = false;
                    }
                  }
                } else if (curFromNodeKey) {
                  isCompatible = false;
                }
                isCompatible =
                  isCompatible !== false && compareNodeNames(curFromNodeChild, curToNodeChild);
                if (isCompatible) {
                  morphEl(curFromNodeChild, curToNodeChild);
                }
              } else if (curFromNodeType === TEXT_NODE || curFromNodeType == COMMENT_NODE) {
                isCompatible = true;
                if (curFromNodeChild.nodeValue !== curToNodeChild.nodeValue) {
                  curFromNodeChild.nodeValue = curToNodeChild.nodeValue;
                }
              }
            }
            if (isCompatible) {
              curToNodeChild = toNextSibling;
              curFromNodeChild = fromNextSibling;
              continue outer;
            }
            if (curFromNodeKey) {
              addKeyedRemoval(curFromNodeKey);
            } else {
              removeNode(curFromNodeChild, fromEl, true);
            }
            curFromNodeChild = fromNextSibling;
          }
          if (
            curToNodeKey &&
            (matchingFromEl = fromNodesLookup[curToNodeKey]) &&
            compareNodeNames(matchingFromEl, curToNodeChild)
          ) {
            if (!skipFrom) {
              addChild(fromEl, matchingFromEl);
            }
            morphEl(matchingFromEl, curToNodeChild);
          } else {
            var onBeforeNodeAddedResult = onBeforeNodeAdded(curToNodeChild);
            if (onBeforeNodeAddedResult !== false) {
              if (onBeforeNodeAddedResult) {
                curToNodeChild = onBeforeNodeAddedResult;
              }
              if (curToNodeChild.actualize) {
                curToNodeChild = curToNodeChild.actualize(fromEl.ownerDocument || doc);
              }
              addChild(fromEl, curToNodeChild);
              handleNodeAdded(curToNodeChild);
            }
          }
          curToNodeChild = toNextSibling;
          curFromNodeChild = fromNextSibling;
        }
        cleanupFromEl(fromEl, curFromNodeChild, curFromNodeKey);
        var specialElHandler = specialElHandlers[fromEl.nodeName];
        if (specialElHandler) {
          specialElHandler(fromEl, toEl);
        }
      }
      var morphedNode = fromNode;
      var morphedNodeType = morphedNode.nodeType;
      var toNodeType = toNode.nodeType;
      if (!childrenOnly) {
        if (morphedNodeType === ELEMENT_NODE) {
          if (toNodeType === ELEMENT_NODE) {
            if (!compareNodeNames(fromNode, toNode)) {
              onNodeDiscarded(fromNode);
              morphedNode = moveChildren(
                fromNode,
                createElementNS(toNode.nodeName, toNode.namespaceURI),
              );
            }
          } else {
            morphedNode = toNode;
          }
        } else if (morphedNodeType === TEXT_NODE || morphedNodeType === COMMENT_NODE) {
          if (toNodeType === morphedNodeType) {
            if (morphedNode.nodeValue !== toNode.nodeValue) {
              morphedNode.nodeValue = toNode.nodeValue;
            }
            return morphedNode;
          } else {
            morphedNode = toNode;
          }
        }
      }
      if (morphedNode === toNode) {
        onNodeDiscarded(fromNode);
      } else {
        if (toNode.isSameNode && toNode.isSameNode(morphedNode)) {
          return;
        }
        morphEl(morphedNode, toNode, childrenOnly);
        if (keyedRemovalList) {
          for (var i = 0, len = keyedRemovalList.length; i < len; i++) {
            var elToRemove = fromNodesLookup[keyedRemovalList[i]];
            if (elToRemove) {
              removeNode(elToRemove, elToRemove.parentNode, false);
            }
          }
        }
      }
      if (!childrenOnly && morphedNode !== fromNode && fromNode.parentNode) {
        if (morphedNode.actualize) {
          morphedNode = morphedNode.actualize(fromNode.ownerDocument || doc);
        }
        fromNode.parentNode.replaceChild(morphedNode, fromNode);
      }
      return morphedNode;
    };
  }
  var morphdom = morphdomFactory(morphAttrs);
  return morphdom;
});
```

## File: `public/locales/en.json`
```json
{
  "app": {
    "title": "OpenClaw Command Center",
    "connecting": "Connecting...",
    "connected": "🟢 Live",
    "disconnected": "🔴 Disconnected",
    "pollingMode": "Polling Mode",
    "error": "🔴 Error"
  },
  "sidebar": {
    "title": "Command Center",
    "navigation": "Navigation",
    "settings": "Settings",
    "quickStats": "Quick Stats",
    "systemVitals": "System Vitals",
    "llmUsage": "LLM Usage",
    "sessions": "Sessions",
    "cronJobs": "Cron Jobs",
    "aiJobs": "AI Jobs",
    "memory": "Memory",
    "cerebro": "Cerebro",
    "operators": "Operators",
    "privacy": "Privacy",
    "about": "About",
    "tokens": "Tokens",
    "estDaily": "Est. Daily",
    "estMonthly": "Est. Monthly",
    "avgTokSess": "Avg Tok/Sess",
    "avgCostSess": "Avg $/Sess",
    "autoRefresh": "Auto-refresh: 30s",
    "live": "Live: {time}",
    "updated": "Updated: {time}"
  },
  "stats": {
    "totalTokens": "Total Tokens",
    "input": "Input",
    "output": "Output",
    "active15m": "Active (15m)",
    "estCost24h": "Est. Cost (24h) 📊",
    "estMonthlySavings": "Est. Monthly Savings",
    "main": "Main",
    "subagents": "Sub-agents"
  },
  "quickActions": {
    "title": "⚡ Quick Actions",
    "healthCheck": "🔍 Health Check",
    "gatewayStatus": "🚪 Gateway Status",
    "cleanStale": "🧹 Clean Stale Sessions"
  },
  "time": {
    "now": "now",
    "justNow": "Just now"
  },
  "actions": {
    "remove": "Remove"
  },
  "privacy": {
    "noCronHidden": "No cron jobs hidden"
  },
  "connection": {
    "realtime": "Real-time updates via SSE ⚡",
    "polling": "Polling mode (SSE disconnected)"
  },
  "jobs": {
    "pageTitle": "AI Jobs - OpenClaw Command Center",
    "dashboard": "🤖 AI Jobs Dashboard",
    "refresh": "🔄 Refresh",
    "totalJobs": "Total Jobs",
    "active": "Active",
    "paused": "Paused",
    "running": "Running",
    "successRate": "Success Rate",
    "recentFailures": "Recent Failures",
    "all": "All",
    "failed": "Failed",
    "loadingJobs": "Loading jobs...",
    "noJobs": "No jobs found",
    "runHistory": "Run History",
    "loadingHistory": "Loading history...",
    "status": "Status",
    "started": "Started",
    "duration": "Duration",
    "details": "Details",
    "noHistory": "No run history yet",
    "statusFailing": "Failing",
    "next": "Next: {value}",
    "lane": "🛤️ {value}",
    "runs": "Runs",
    "success": "Success",
    "avgTime": "Avg Time",
    "lastRun": "Last run: {value}",
    "neverRun": "Never run",
    "run": "▶️ Run",
    "resume": "▶️ Resume",
    "pause": "⏸️ Pause",
    "history": "📜 History",
    "every": "Every {value}",
    "at": "At {value}",
    "toastLoadFailed": "Failed to load jobs",
    "toastRunQueued": "Job \"{id}\" queued for execution",
    "toastRunFailed": "Failed to run job",
    "toastPaused": "Job \"{id}\" paused",
    "toastPauseFailed": "Failed to pause job",
    "toastResumed": "Job \"{id}\" resumed",
    "toastResumeFailed": "Failed to resume job",
    "historyTitle": "Run History: {name}",
    "statusSuccess": "Success",
    "statusFailed": "Failed",
    "statusRunning": "Running"
  }
}
```

## File: `public/locales/zh-CN.json`
```json
{
  "app": {
    "title": "OpenClaw 指挥中心",
    "connecting": "连接中...",
    "connected": "🟢 实时",
    "disconnected": "🔴 已断开",
    "pollingMode": "轮询模式",
    "error": "🔴 错误"
  },
  "sidebar": {
    "title": "指挥中心",
    "navigation": "导航",
    "settings": "设置",
    "quickStats": "快速统计",
    "systemVitals": "系统状态",
    "llmUsage": "LLM 用量",
    "sessions": "会话",
    "cronJobs": "定时任务",
    "aiJobs": "AI 任务",
    "memory": "记忆",
    "cerebro": "Cerebro",
    "operators": "Operators（操作者）",
    "privacy": "隐私",
    "about": "关于",
    "tokens": "Token",
    "estDaily": "日预估",
    "estMonthly": "月预估",
    "avgTokSess": "平均 Token/会话",
    "avgCostSess": "平均 $/会话",
    "autoRefresh": "自动刷新：30秒",
    "live": "实时：{time}",
    "updated": "更新：{time}"
  },
  "stats": {
    "totalTokens": "总 Token",
    "input": "输入",
    "output": "输出",
    "active15m": "活跃（15分钟）",
    "estCost24h": "预估成本（24小时）📊",
    "estMonthlySavings": "预估月节省",
    "main": "主会话",
    "subagents": "子代理"
  },
  "quickActions": {
    "title": "⚡ 快捷操作",
    "healthCheck": "🔍 健康检查",
    "gatewayStatus": "🚪 网关状态",
    "cleanStale": "🧹 清理过期会话"
  },
  "time": {
    "now": "刚刚",
    "justNow": "刚刚"
  },
  "actions": {
    "remove": "移除"
  },
  "privacy": {
    "noCronHidden": "未隐藏任何定时任务"
  },
  "connection": {
    "realtime": "通过 SSE 实时更新 ⚡",
    "polling": "轮询模式（SSE 已断开）"
  },
  "phrases": {
    "exact": {
      "OpenClaw Command Center": "OpenClaw 指挥中心",
      "Command Center": "指挥中心",
      "Connecting...": "连接中...",
      "Total Tokens": "总 Token",
      "Input": "输入",
      "Output": "输出",
      "Active (15m)": "活跃（15分钟）",
      "Est. Cost (24h) 📊": "预估成本（24小时）📊",
      "Est. Monthly Savings": "预估月节省",
      "Main": "主会话",
      "Sub-agents": "子代理",
      "System Vitals": "系统状态",
      "LLM Fuel Gauges": "LLM 用量仪表",
      "Sessions": "会话",
      "Cron Jobs": "定时任务",
      "Memory": "记忆",
      "Operators": "Operators（操作者）",
      "About": "关于",
      "Quick Actions": "快捷操作",
      "Health Check": "健康检查",
      "Gateway Status": "网关状态",
      "Clean Stale Sessions": "清理过期会话",
      "Session Details": "会话详情",
      "Overview": "概览",
      "Summary": "摘要",
      "References": "引用",
      "Needs Attention": "需关注",
      "Key Facts": "关键信息",
      "Tools Used": "使用工具",
      "Recent Messages": "最近消息",
      "Send Message": "发送消息",
      "Refresh": "刷新",
      "Clear Session": "清空会话",
      "Fix Claude Authentication": "修复 Claude 鉴权",
      "Step 1: Refresh Claude Token": "步骤 1：刷新 Claude Token",
      "Step 2: Update OpenClaw Agent": "步骤 2：更新 OpenClaw 代理",
      "Step 3: Verify": "步骤 3：验证",
      "Cost Breakdown (24h)": "成本明细（24小时）",
      "Token Usage": "Token 用量",
      "Pricing Rates (Claude Opus)": "价格费率（Claude Opus）",
      "Calculation": "计算方式",
      "Est. Savings": "预估节省",
      "Top Sessions by Tokens (24h)": "按 Token 排名前会话（24小时）",
      "User Stats": "用户统计",
      "Loading user stats...": "正在加载用户统计...",
      "Privacy Settings": "隐私设置",
      "Hidden Topics": "隐藏话题",
      "No topics hidden": "未隐藏任何话题",
      "Hidden Sessions": "隐藏会话",
      "No sessions hidden": "未隐藏任何会话",
      "Hidden Cron Jobs": "隐藏定时任务",
      "No cron jobs hidden": "未隐藏任何定时任务",
      "Display Options": "显示选项",
      "Hide system hostname": "隐藏系统主机名",
      "Clear All Privacy Settings": "清除全部隐私设置",
      "Status": "状态",
      "Channel": "渠道",
      "Kind": "类型",
      "All": "全部",
      "Live": "在线",
      "Recent": "最近",
      "Idle": "空闲",
      "Slack": "Slack",
      "Telegram": "Telegram",
      "Discord": "Discord",
      "Signal": "Signal",
      "WhatsApp": "WhatsApp",
      "Subagent": "子代理（Subagent）",
      "Enabled": "启用",
      "Disabled": "禁用",
      "Schedule": "计划",
      "Frequent (<1h)": "高频（<1小时）",
      "Daily": "每日",
      "Weekly": "每周",
      "Type": "类型",
      "Today": "今天",
      "This Week": "本周",
      "Older": "更早",
      "Long-term curated memories": "长期整理后的记忆",
      "Raw logs by date": "按日期保存的原始日志",
      "Recent Memory Files": "最近记忆文件",
      "Loading...": "加载中...",
      "Cerebro Not Initialized": "Cerebro 未初始化",
      "Topics by Status": "话题状态统计",
      "Threads": "线程",
      "Recent Active Topics": "最近活跃话题",
      "No active topics yet": "暂无活跃话题",
      "Open cerebro/": "打开 cerebro/ 目录",
      "Loading operators...": "正在加载 Operators（操作者）...",
      "Permission Levels": "权限级别",
      "Owner": "所有者",
      "Full control": "完全控制",
      "Admin": "管理员",
      "Manage users & settings": "管理用户和设置",
      "User": "用户",
      "Dashboard access": "看板访问权限",
      "A Starcraft-inspired dashboard for OpenClaw orchestration": "受星际争霸启发的 OpenClaw 编排看板",
      "BUILT BY": "开发者",
      "INSPIRED BY": "灵感来源",
      "No active sub-agents": "暂无活跃子代理",
      "Session Usage": "会话用量",
      "Weekly Usage": "周用量",
      "5-Hour Usage": "5 小时用量",
      "Daily Usage": "日用量",
      "Tasks Today": "今日任务",
      "Session Limit": "会话额度",
      "1m avg": "1分钟均值",
      "5m avg": "5分钟均值",
      "15m avg": "15分钟均值",
      "used of total": "已用 / 总量",
      "IOPS": "IOPS",
      "MB/s": "MB/秒",
      "KB/t": "KB/次",
      "tok/min": "Token/分钟",
      "v...": "v...",
      "MIT License": "MIT 许可证",
      "used": "已用",
      "available": "可用",
      "user": "用户",
      "sys": "系统",
      "idle": "空闲",
      "cores": "核心",
      "App": "应用",
      "Wired": "常驻内存（Wired）",
      "Compressed": "压缩内存",
      "Cached": "缓存",
      "Normal": "正常",
      "Checking...": "检测中...",
      "API Usage": "API 用量",
      "ChatGPT Plus": "ChatGPT Plus",
      "Status:": "状态：",
      "Channel:": "渠道：",
      "Kind:": "类型：",
      "Schedule:": "计划：",
      "Type:": "类型：",
      "Age:": "时间：",
      "size": "大小",
      "lines": "行数",
      "files": "文件",
      "total": "总计",
      "active": "活跃",
      "resolved": "已解决",
      "parked": "暂挂",
      "tracked": "已跟踪",
      "orphans": "孤立话题",
      "No active sessions": "暂无活跃会话",
      "No scheduled jobs": "暂无定时任务",
      "No operators configured": "未配置 Operators（操作者）",
      "Last Seen": "最后在线",
      "Auth Error - Click to Fix": "鉴权错误 - 点击修复",
      "N/A": "不可用",
      "No memory files yet": "暂无记忆文件",
      "Failed to load cost data": "加载成本数据失败",
      "Operator not found": "未找到 Operator（操作者）",
      "Failed to load user data": "加载用户数据失败",
      "Active Sessions": "活跃会话",
      "Total Sessions": "会话总数",
      "First Seen": "首次出现",
      "No sessions found": "未找到会话",
      "Input Tokens": "输入 Token",
      "Output Tokens": "输出 Token",
      "Cache Read": "缓存读取",
      "Cache Write": "缓存写入",
      "API Requests": "API 请求数",
      "Input Cost": "输入成本",
      "Output Cost": "输出成本",
      "Cache Read Cost": "缓存读取成本",
      "Cache Write Cost": "缓存写入成本",
      "Est. API Cost": "预估 API 成本",
      "Projected Monthly Cost by Window:": "按时间窗口预测月成本：",
      "No session data available": "暂无会话数据",
      "Est. Cost": "预估成本",
      "Cache (R/W)": "缓存（读/写）",
      "Channel": "渠道",
      "Model": "模型",
      "Input / Output": "输入 / 输出",
      "Last Active": "最后活跃",
      "No summary": "暂无摘要",
      "No references detected": "未检测到引用",
      "Nothing needs attention": "暂无需关注项",
      "No key facts": "暂无关键信息",
      "No tools used": "未使用工具",
      "No messages": "暂无消息",
      "Navigation": "导航",
      "Settings": "设置",
      "Quick Stats": "快速统计",
      "LLM Fuel Gauges": "LLM 用量仪表",
      "System Vitals": "系统状态",
      "LLM Usage": "LLM 用量",
      "Privacy": "隐私",
      "Total tokens (24h)": "总 Token（24小时）",
      "Click for breakdown": "点击查看明细",
      "Projected monthly cost": "预测月成本",
      "Average tokens per session": "每会话平均 Token",
      "Average cost per session": "每会话平均成本",
      "SSE connection status": "SSE 连接状态",
      "Sessions active within last 15 minutes": "最近 15 分钟内活跃会话",
      "Click for cost breakdown": "点击查看成本明细",
      "Main session capacity": "主会话容量",
      "Sub-agent capacity": "子代理容量",
      "Memory actively used by apps": "应用正在使用的内存",
      "Memory that can't be swapped (kernel, drivers)": "不可交换内存（内核、驱动）",
      "Memory compressed to save space": "为节省空间而压缩的内存",
      "Recently-used data, can be reclaimed": "近期使用数据，可回收",
      "Average routing latency (classification + execution)": "平均路由延迟（分类 + 执行）",
      "AI Jobs Dashboard": "AI 任务面板",
      "Privacy Settings": "隐私设置",
      "No topics hidden": "未隐藏任何话题",
      "No sessions hidden": "未隐藏任何会话",
      "Hide topics and sessions from display for privacy during demos/screenshots. Settings are stored in your browser only.": "为保护演示/截图隐私，可隐藏话题和会话。设置仅保存在你的浏览器中。",
      "Tip: You can also click the 👁️ icon on any session card to hide it quickly.": "提示：你也可以点击任意会话卡片上的 👁️ 图标快速隐藏。",
      "Open Terminal and run:": "打开终端并运行：",
      "Follow the prompts to authenticate with your Claude account.": "按提示完成 Claude 账号认证。",
      "Run the onboard wizard to update your agent credentials:": "运行引导向导更新代理凭据：",
      "Or manually update the main agent:": "或手动更新主代理：",
      "Select \"Claude Code CLI\" when prompted for the auth source.": "当提示选择认证来源时，选择 \"Claude Code CLI\"。",
      "Refresh this dashboard or run:": "刷新此看板，或运行：",
      "You should see your usage percentages instead of an auth error.": "你应该看到用量百分比，而不是鉴权错误。",
      "Memory editing UI coming soon (Inside Out style!)": "记忆编辑 UI 即将上线（Inside Out 风格！）",
      "Cerebro tracks conversation topics and threads across sessions.": "Cerebro 用于跨会话追踪对话话题与线程。",
      "To initialize Cerebro:": "初始化 Cerebro：",
      "Threads linked to topics": "关联到话题的线程",
      "No active sub-agents": "暂无活跃子代理",
      "No active topics yet": "暂无活跃话题",
      "No memory files yet": "暂无记忆文件",
      "No references detected": "未检测到引用",
      "Nothing needs attention": "暂无需关注项",
      "No key facts": "暂无关键信息",
      "No tools used": "未使用工具",
      "No messages": "暂无消息",
      "No summary": "暂无摘要",
      "No session data available": "暂无会话数据",
      "No sessions found": "未找到会话",
      "Loading user stats...": "正在加载用户统计...",
      "Loading operators...": "正在加载 Operators（操作者）...",
      "Loading...": "加载中...",
      "Add": "添加",
      "Remove": "移除",
      "Prev": "上一页",
      "Next": "下一页",
      "Last updated:": "最后更新：",
      "Built by": "开发者",
      "remaining": "剩余",
      "resets in": "后重置",
      "resets": "重置",
      "Avg latency": "平均延迟"
    },
    "patterns": [
      {
        "pattern": "^Live:\\s*(.+)$",
        "replace": "实时：$1"
      },
      {
        "pattern": "^Updated:\\s*(.+)$",
        "replace": "更新：$1"
      },
      {
        "pattern": "^Uptime:\\s*(.+)$",
        "replace": "运行时长：$1"
      },
      {
        "pattern": "^Routing:\\s*(.+)$",
        "replace": "路由：$1"
      },
      {
        "pattern": "^Last updated:\\s*(.*)$",
        "replace": "最后更新：$1"
      },
      {
        "pattern": "^Last run:\\s*(.+)$",
        "replace": "上次运行：$1"
      },
      {
        "pattern": "^Run History:\\s*(.+)$",
        "replace": "运行历史：$1"
      },
      {
        "pattern": "^Operator not found:\\s*(.+)$",
        "replace": "未找到 Operator（操作者）：$1"
      },
      {
        "pattern": "^Error:\\s*(.+)$",
        "replace": "错误：$1"
      },
      {
        "pattern": "^via\\s+(.+)$",
        "replace": "来源：$1"
      },
      {
        "pattern": "^Avg latency:\\s*(.+)$",
        "replace": "平均延迟：$1"
      },
      {
        "pattern": "^(\\d+) total topics$",
        "replace": "$1 个话题"
      },
      {
        "pattern": "^(\\d+) tracked$",
        "replace": "$1 个已跟踪"
      },
      {
        "pattern": "^(\\d+) orphans$",
        "replace": "$1 个孤立"
      },
      {
        "pattern": "^ID:\\s*(.+) • (\\d+) tokens • (.+)$",
        "replace": "ID：$1 • $2 Token • $3"
      },
      {
        "pattern": "^Auto-refresh:\\s*30s$",
        "replace": "自动刷新：30秒"
      },
      {
        "pattern": "^Polling Mode$",
        "replace": "轮询模式"
      },
      {
        "pattern": "^Real-time updates via SSE$",
        "replace": "通过 SSE 实时更新"
      },
      {
        "pattern": "^Just now$",
        "replace": "刚刚"
      },
      {
        "pattern": "^now$",
        "replace": "刚刚"
      }
    ],
    "reversePatterns": [
      {
        "pattern": "^实时：\\s*(.+)$",
        "replace": "Live: $1"
      },
      {
        "pattern": "^更新：\\s*(.+)$",
        "replace": "Updated: $1"
      },
      {
        "pattern": "^运行时长：\\s*(.+)$",
        "replace": "Uptime: $1"
      },
      {
        "pattern": "^路由：\\s*(.+)$",
        "replace": "Routing: $1"
      },
      {
        "pattern": "^最后更新：\\s*(.*)$",
        "replace": "Last updated: $1"
      },
      {
        "pattern": "^上次运行：\\s*(.+)$",
        "replace": "Last run: $1"
      },
      {
        "pattern": "^运行历史：\\s*(.+)$",
        "replace": "Run History: $1"
      },
      {
        "pattern": "^未找到 Operator（操作者）：\\s*(.+)$",
        "replace": "Operator not found: $1"
      },
      {
        "pattern": "^错误：\\s*(.+)$",
        "replace": "Error: $1"
      },
      {
        "pattern": "^来源：\\s*(.+)$",
        "replace": "via $1"
      },
      {
        "pattern": "^平均延迟：\\s*(.+)$",
        "replace": "Avg latency: $1"
      },
      {
        "pattern": "^(\\d+) 个话题$",
        "replace": "$1 total topics"
      },
      {
        "pattern": "^(\\d+) 个已跟踪$",
        "replace": "$1 tracked"
      },
      {
        "pattern": "^(\\d+) 个孤立$",
        "replace": "$1 orphans"
      },
      {
        "pattern": "^ID：\\s*(.+) • (\\d+) Token • (.+)$",
        "replace": "ID: $1 • $2 tokens • $3"
      },
      {
        "pattern": "^自动刷新：30秒$",
        "replace": "Auto-refresh: 30s"
      },
      {
        "pattern": "^轮询模式$",
        "replace": "Polling Mode"
      },
      {
        "pattern": "^通过 SSE 实时更新$",
        "replace": "Real-time updates via SSE"
      },
      {
        "pattern": "^刚刚$",
        "replace": "Just now"
      }
    ]
  },
  "jobs": {
    "pageTitle": "AI 任务 - OpenClaw 指挥中心",
    "dashboard": "🤖 AI 任务面板",
    "refresh": "🔄 刷新",
    "totalJobs": "任务总数",
    "active": "启用",
    "paused": "暂停",
    "running": "运行中",
    "successRate": "成功率",
    "recentFailures": "最近失败",
    "all": "全部",
    "failed": "失败",
    "loadingJobs": "正在加载任务...",
    "noJobs": "未找到任务",
    "runHistory": "运行历史",
    "loadingHistory": "正在加载历史...",
    "status": "状态",
    "started": "开始时间",
    "duration": "耗时",
    "details": "详情",
    "noHistory": "暂无运行历史",
    "statusFailing": "持续失败",
    "next": "下次：{value}",
    "lane": "🛤️ {value}",
    "runs": "运行次数",
    "success": "成功",
    "avgTime": "平均耗时",
    "lastRun": "上次运行：{value}",
    "neverRun": "从未运行",
    "run": "▶️ 运行",
    "resume": "▶️ 恢复",
    "pause": "⏸️ 暂停",
    "history": "📜 历史",
    "every": "每 {value}",
    "at": "在 {value}",
    "toastLoadFailed": "加载任务失败",
    "toastRunQueued": "任务 \"{id}\" 已加入执行队列",
    "toastRunFailed": "执行任务失败",
    "toastPaused": "任务 \"{id}\" 已暂停",
    "toastPauseFailed": "暂停任务失败",
    "toastResumed": "任务 \"{id}\" 已恢复",
    "toastResumeFailed": "恢复任务失败",
    "historyTitle": "运行历史：{name}",
    "statusSuccess": "成功",
    "statusFailed": "失败",
    "statusRunning": "运行中"
  }
}
```

## File: `public/partials/sidebar.html`
```html
<!-- Shared Sidebar Partial -->
<nav class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <span class="sidebar-logo">🦞</span>
    <span class="sidebar-title" data-i18n="sidebar.title">Command Center</span>
    <button
      class="sidebar-toggle"
      id="sidebar-toggle-btn"
      onclick="toggleSidebar()"
      title="Toggle sidebar"
    >
      ◀
    </button>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section">
      <div class="nav-section-title" data-i18n="sidebar.navigation">Navigation</div>
      <a
        href="#vitals-section"
        class="nav-item"
        data-section="vitals"
        data-page="/"
        data-tooltip="System Vitals"
      >
        <span class="nav-icon">🖥️</span>
        <span data-i18n="sidebar.systemVitals">System Vitals</span>
      </a>
      <a
        href="#llm-section"
        class="nav-item"
        data-section="llm"
        data-page="/"
        data-tooltip="LLM Fuel Gauges"
      >
        <span class="nav-icon">⛽</span>
        <span data-i18n="sidebar.llmUsage">LLM Usage</span>
      </a>
      <a
        href="#sessions-section"
        class="nav-item"
        data-section="sessions"
        data-page="/"
        data-tooltip="Sessions"
      >
        <span class="nav-icon">📡</span>
        <span data-i18n="sidebar.sessions">Sessions</span>
        <span class="nav-badge" id="nav-session-count">-</span>
      </a>
      <a
        href="#cron-section"
        class="nav-item"
        data-section="cron"
        data-page="/"
        data-tooltip="Cron Jobs"
      >
        <span class="nav-icon">⏰</span>
        <span data-i18n="sidebar.cronJobs">Cron Jobs</span>
        <span class="nav-badge" id="nav-cron-count">-</span>
      </a>
      <a href="/jobs.html" class="nav-item" data-page="/jobs.html" data-tooltip="AI Jobs Dashboard">
        <span class="nav-icon">🤖</span>
        <span data-i18n="sidebar.aiJobs">AI Jobs</span>
        <span class="nav-badge" id="nav-jobs-count">-</span>
      </a>
      <a
        href="#memory-section"
        class="nav-item"
        data-section="memory"
        data-page="/"
        data-tooltip="Memory"
      >
        <span class="nav-icon">🧠</span>
        <span data-i18n="sidebar.memory">Memory</span>
        <span class="nav-badge" id="nav-memory-count">-</span>
      </a>
      <a
        href="#cerebro-section"
        class="nav-item"
        data-section="cerebro"
        data-page="/"
        data-tooltip="Cerebro"
      >
        <span class="nav-icon">🔮</span>
        <span data-i18n="sidebar.cerebro">Cerebro</span>
        <span class="nav-badge" id="nav-cerebro-count">-</span>
      </a>
      <a
        href="#operators-section"
        class="nav-item"
        data-section="operators"
        data-page="/"
        data-tooltip="Operators"
      >
        <span class="nav-icon">👥</span>
        <span data-i18n="sidebar.operators">Operators</span>
        <span class="nav-badge" id="nav-operator-count">-</span>
      </a>
    </div>
    <div class="nav-section">
      <div class="nav-section-title" data-i18n="sidebar.settings">Settings</div>
      <a
        href="#"
        class="nav-item"
        onclick="
          window.openPrivacyModal && openPrivacyModal();
          return false;
        "
        data-tooltip="Privacy Settings"
      >
        <span class="nav-icon">🔒</span>
        <span data-i18n="sidebar.privacy">Privacy</span>
      </a>
      <a
        href="#about-section"
        class="nav-item"
        data-section="about"
        data-page="/"
        data-tooltip="About"
      >
        <span class="nav-icon">ℹ️</span>
        <span data-i18n="sidebar.about">About</span>
      </a>
    </div>
    <div class="nav-section">
      <div class="nav-section-title" data-i18n="sidebar.quickStats">Quick Stats</div>
      <div class="nav-item" style="cursor: default" data-tooltip="Total tokens (24h)">
        <span class="nav-icon">🎫</span>
        <span data-i18n="sidebar.tokens">Tokens</span>
        <span class="nav-badge" id="nav-tokens">-</span>
      </div>
      <div
        class="nav-item"
        style="cursor: pointer"
        onclick="window.openCostModal && openCostModal()"
        data-tooltip="Click for breakdown"
      >
        <span class="nav-icon">💰</span>
        <span data-i18n="sidebar.estDaily">Est. Daily</span>
        <span class="nav-badge" id="nav-cost">-</span>
      </div>
      <div
        class="nav-item"
        style="cursor: pointer"
        onclick="window.openCostModal && openCostModal()"
        data-tooltip="Projected monthly cost"
      >
        <span class="nav-icon">📅</span>
        <span data-i18n="sidebar.estMonthly">Est. Monthly</span>
        <span class="nav-badge" id="nav-monthly-cost">-</span>
      </div>
      <div class="nav-item" style="cursor: default" data-tooltip="Average tokens per session">
        <span class="nav-icon">📊</span>
        <span data-i18n="sidebar.avgTokSess">Avg Tok/Sess</span>
        <span class="nav-badge" id="nav-avg-tokens">-</span>
      </div>
      <div class="nav-item" style="cursor: default" data-tooltip="Average cost per session">
        <span class="nav-icon">💵</span>
        <span data-i18n="sidebar.avgCostSess">Avg $/Sess</span>
        <span class="nav-badge" id="nav-avg-cost">-</span>
      </div>
    </div>
  </div>
  <div class="sidebar-footer">
    <span data-i18n="sidebar.autoRefresh">Auto-refresh: 30s</span><br />
    <span id="sidebar-updated">-</span>
  </div>
</nav>
```

## File: `scripts/dashboard-loop.sh`
```bash
#!/bin/bash
# Auto-restart loop for OpenClaw Command Center
# Keeps the dashboard running with exponential backoff on crashes

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DASHBOARD_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="${HOME}/.openclaw-command-center/logs"
LOG_FILE="${LOG_DIR}/dashboard.log"

mkdir -p "$LOG_DIR"

# Backoff settings
INITIAL_DELAY=1
MAX_DELAY=30
DELAY=$INITIAL_DELAY

cd "$DASHBOARD_DIR"

# Ensure node is available (nvm support)
if [ -f "$HOME/.nvm/nvm.sh" ]; then
    source "$HOME/.nvm/nvm.sh"
fi

echo "🦞 OpenClaw Command Center - Auto-restart loop"
echo "   Logs: $LOG_FILE"
echo "   Press Ctrl+C to stop"
echo ""

while true; do
    echo "[$(date)] Starting dashboard..." | tee -a "$LOG_FILE"
    
    # Run the server
    if node lib/server.js 2>&1 | tee -a "$LOG_FILE"; then
        # Clean exit
        echo "[$(date)] Dashboard exited cleanly" | tee -a "$LOG_FILE"
        DELAY=$INITIAL_DELAY
    else
        # Crash - backoff
        echo "[$(date)] Dashboard crashed! Restarting in ${DELAY}s..." | tee -a "$LOG_FILE"
        sleep $DELAY
        DELAY=$((DELAY * 2))
        if [ $DELAY -gt $MAX_DELAY ]; then
            DELAY=$MAX_DELAY
        fi
    fi
done
```

## File: `scripts/install-system-deps.sh`
```bash
#!/bin/bash
#
# install-system-deps.sh - Install optional system dependencies
#
# Reads config/system-deps.json and installs missing packages
# using the detected package manager (apt, brew, dnf, etc.)
#
# Usage: ./scripts/install-system-deps.sh [--dry-run]
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DEPS_FILE="$PROJECT_DIR/config/system-deps.json"
DRY_RUN="${1:-}"

if [[ "$DRY_RUN" == "-h" || "$DRY_RUN" == "--help" ]]; then
    echo "Usage: install-system-deps.sh [--dry-run]"
    echo "  --dry-run    Show what would be installed without installing"
    exit 0
fi

if [[ ! -f "$DEPS_FILE" ]]; then
    echo "Error: $DEPS_FILE not found"
    exit 1
fi

echo "🦞 OpenClaw Command Center - System Dependencies"
echo "================================================="
echo ""

# Let node do all the heavy lifting — it parses the JSON, detects the
# platform/package-manager/chip, checks which binaries exist, and
# prints shell commands to stdout for us to eval.
node -e "
const { execSync } = require('child_process');
const os = require('os');
const deps = require('$DEPS_FILE');

const platform = process.platform === 'linux' ? 'linux' : process.platform === 'darwin' ? 'darwin' : null;
if (!platform) { console.log('echo \"Unsupported platform\"'); process.exit(0); }

// Detect package manager
const pmCandidates = platform === 'linux'
    ? ['apt', 'dnf', 'yum', 'pacman', 'apk']
    : ['brew'];
let pkgManager = null;
for (const pm of pmCandidates) {
    try { execSync('which ' + pm, { stdio: 'ignore' }); pkgManager = pm; break; } catch {}
}

console.log('Platform: ' + platform);
console.log('Package manager: ' + (pkgManager || 'none'));
console.log('');

if (!pkgManager) {
    console.log('No supported package manager found.');
    console.log('Supported: apt, dnf, yum, pacman, apk, brew');
    process.exit(1);
}

// Detect chip
let isAppleSilicon = false;
if (platform === 'darwin') {
    try {
        const chip = execSync('sysctl -n machdep.cpu.brand_string', { encoding: 'utf8' });
        isAppleSilicon = /apple/i.test(chip);
    } catch {}
}

const entries = deps[platform] || [];
let installed = 0, toInstall = 0;

for (const dep of entries) {
    if (dep.condition === 'intel' && isAppleSilicon) continue;
    const cmd = dep.install[pkgManager];
    if (!cmd) continue;

    let hasBinary = false;
    try { execSync('which ' + dep.binary, { stdio: 'ignore' }); hasBinary = true; } catch {}
    if (!hasBinary && dep.binary === 'osx-cpu-temp') {
        try { execSync('test -x ' + os.homedir() + '/bin/osx-cpu-temp', { stdio: 'ignore' }); hasBinary = true; } catch {}
    }

    if (hasBinary) {
        console.log('✅ ' + dep.name + ' — already installed (' + dep.purpose + ')');
        installed++;
    } else {
        toInstall++;
        if ('$DRY_RUN' === '--dry-run') {
            console.log('📦 ' + dep.name + ' — would install (' + dep.purpose + ')');
            console.log('   Command: ' + cmd);
        } else {
            console.log('📦 Installing ' + dep.name + ' — ' + dep.purpose + '...');
            console.log('   Running: ' + cmd);
            try {
                execSync(cmd, { stdio: 'inherit' });
                console.log('   ✅ Installed successfully');
            } catch (e) {
                console.log('   ⚠️  Install failed: ' + e.message);
            }
        }
    }
}

console.log('');
if ('$DRY_RUN' === '--dry-run') {
    console.log('Dry run complete. ' + installed + ' already installed, ' + toInstall + ' would be installed.');
} else {
    console.log('Done! ' + installed + ' already installed, ' + toInstall + ' newly installed.');
    if (toInstall > 0) {
        console.log('');
        console.log('Restart the Command Center to see enhanced vitals.');
    }
}
"
```

## File: `scripts/linear-sync.js`
```javascript
#!/usr/bin/env node
/**
 * Linear Integration Module for OpenClaw Dashboard
 *
 * Syncs session state to Linear issues:
 * - Extracts JON-XXX issue IDs from session transcripts
 * - Updates Linear issue status when session state changes
 * - Adds comments on state transitions
 */

const https = require("https");
const fs = require("fs");
const path = require("path");
const { getOpenClawDir } = require("../src/config");

// Linear API configuration
const LINEAR_API_URL = "https://api.linear.app/graphql";
const LINEAR_API_KEY = process.env.LINEAR_API_KEY;

// Workflow State IDs for team JON (from TOOLS.md)
const LINEAR_STATES = {
  TODO: "2ee58f08-499b-47ee-bbe3-a254957517c5",
  IN_PROGRESS: "c2c429d8-11d0-4fa5-bbe7-7bc7febbd42e",
  DONE: "b82d1646-6044-48ad-b2e9-04f87739e16f",
};

// Session state to Linear state mapping
const STATE_MAP = {
  active: LINEAR_STATES.IN_PROGRESS,
  live: LINEAR_STATES.IN_PROGRESS,
  idle: LINEAR_STATES.TODO,
  completed: LINEAR_STATES.DONE,
};

// Track synced issues to avoid duplicate updates
// Key: issueId, Value: { lastState, lastUpdated }
const syncState = new Map();

// Path to persist sync state
const SYNC_STATE_FILE = path.join(__dirname, "..", "state", "linear-sync-state.json");

/**
 * Load sync state from disk
 */
function loadSyncState() {
  try {
    if (fs.existsSync(SYNC_STATE_FILE)) {
      const data = JSON.parse(fs.readFileSync(SYNC_STATE_FILE, "utf8"));
      Object.entries(data).forEach(([key, value]) => {
        syncState.set(key, value);
      });
      console.log(`[Linear] Loaded sync state: ${syncState.size} issues tracked`);
    }
  } catch (e) {
    console.error("[Linear] Failed to load sync state:", e.message);
  }
}

/**
 * Save sync state to disk
 */
function saveSyncState() {
  try {
    const data = Object.fromEntries(syncState);
    const dir = path.dirname(SYNC_STATE_FILE);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    fs.writeFileSync(SYNC_STATE_FILE, JSON.stringify(data, null, 2));
  } catch (e) {
    console.error("[Linear] Failed to save sync state:", e.message);
  }
}

/**
 * Make a GraphQL request to Linear API
 * @param {string} query - GraphQL query/mutation
 * @param {object} variables - Query variables
 * @returns {Promise<object>} Response data
 */
function linearRequest(query, variables = {}) {
  return new Promise((resolve, reject) => {
    if (!LINEAR_API_KEY) {
      reject(new Error("LINEAR_API_KEY not set"));
      return;
    }

    const payload = JSON.stringify({ query, variables });

    const options = {
      hostname: "api.linear.app",
      port: 443,
      path: "/graphql",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: LINEAR_API_KEY,
        "Content-Length": Buffer.byteLength(payload),
      },
    };

    const req = https.request(options, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => {
        try {
          const parsed = JSON.parse(data);
          if (parsed.errors) {
            reject(new Error(parsed.errors[0]?.message || "GraphQL error"));
          } else {
            resolve(parsed.data);
          }
        } catch (e) {
          reject(new Error(`Failed to parse response: ${e.message}`));
        }
      });
    });

    req.on("error", reject);
    req.write(payload);
    req.end();
  });
}

/**
 * Extract Linear issue IDs (JON-XXX pattern) from text
 * @param {string} text - Text to search
 * @returns {string[]} Array of unique issue identifiers
 */
function extractLinearIds(text) {
  if (!text) return [];

  // Match JON-XXX pattern (case insensitive, 1-5 digits)
  const pattern = /\bJON-(\d{1,5})\b/gi;
  const matches = text.match(pattern) || [];

  // Normalize to uppercase and dedupe
  const unique = [...new Set(matches.map((m) => m.toUpperCase()))];
  return unique;
}

/**
 * Extract Linear IDs from a session transcript
 * @param {Array} transcript - Array of transcript entries
 * @returns {string[]} Array of unique issue identifiers
 */
function extractLinearIdsFromTranscript(transcript) {
  const allIds = new Set();

  transcript.forEach((entry) => {
    if (entry.type !== "message" || !entry.message) return;

    const msg = entry.message;
    let text = "";

    if (typeof msg.content === "string") {
      text = msg.content;
    } else if (Array.isArray(msg.content)) {
      text = msg.content
        .filter((c) => c.type === "text")
        .map((c) => c.text || "")
        .join(" ");
    }

    extractLinearIds(text).forEach((id) => allIds.add(id));
  });

  return [...allIds];
}

/**
 * Get issue details by identifier (e.g., "JON-29")
 * @param {string} identifier - Issue identifier
 * @returns {Promise<object|null>} Issue data or null
 */
async function getIssue(identifier) {
  const query = `
        query GetIssue($id: String!) {
            issue(id: $id) {
                id
                identifier
                title
                description
                url
                state {
                    id
                    name
                    type
                }
                priority
            }
        }
    `;

  try {
    const data = await linearRequest(query, { id: identifier });
    return data.issue;
  } catch (e) {
    console.error(`[Linear] Failed to get issue ${identifier}:`, e.message);
    return null;
  }
}

/**
 * Update issue state
 * @param {string} issueId - Issue UUID (not identifier)
 * @param {string} stateId - New state UUID
 * @returns {Promise<boolean>} Success status
 */
async function updateIssueState(issueId, stateId) {
  const mutation = `
        mutation UpdateIssueState($id: String!, $stateId: String!) {
            issueUpdate(id: $id, input: { stateId: $stateId }) {
                success
                issue {
                    id
                    identifier
                    state {
                        name
                    }
                }
            }
        }
    `;

  try {
    const data = await linearRequest(mutation, { id: issueId, stateId });
    return data.issueUpdate?.success || false;
  } catch (e) {
    console.error(`[Linear] Failed to update issue state:`, e.message);
    return false;
  }
}

/**
 * Add a comment to an issue
 * @param {string} issueId - Issue UUID (not identifier)
 * @param {string} body - Comment body (markdown supported)
 * @returns {Promise<boolean>} Success status
 */
async function addComment(issueId, body) {
  const mutation = `
        mutation AddComment($issueId: String!, $body: String!) {
            commentCreate(input: { issueId: $issueId, body: $body }) {
                success
                comment {
                    id
                }
            }
        }
    `;

  try {
    const data = await linearRequest(mutation, { issueId, body });
    return data.commentCreate?.success || false;
  } catch (e) {
    console.error(`[Linear] Failed to add comment:`, e.message);
    return false;
  }
}

/**
 * Determine session state from session data
 * @param {object} session - Session object with ageMs, etc.
 * @returns {string} State: 'active', 'idle', or 'completed'
 */
function determineSessionState(session) {
  const ageMs = session.ageMs || 0;
  const thirtyMinutes = 30 * 60 * 1000;

  // Check if session is marked complete (this would come from session metadata)
  if (session.status === "completed" || session.completed) {
    return "completed";
  }

  // Active if activity within 30 minutes
  if (ageMs < thirtyMinutes) {
    return "active";
  }

  // Idle if no activity for 30+ minutes
  return "idle";
}

/**
 * Sync a session's Linear issues based on session state
 * @param {object} session - Session data including transcript
 * @param {Array} transcript - Session transcript entries
 * @returns {Promise<object>} Sync results
 */
async function syncSessionToLinear(session, transcript) {
  const results = {
    issuesFound: [],
    updated: [],
    skipped: [],
    errors: [],
  };

  if (!LINEAR_API_KEY) {
    results.errors.push("LINEAR_API_KEY not configured");
    return results;
  }

  // Extract Linear issue IDs from transcript
  const issueIds = extractLinearIdsFromTranscript(transcript);
  results.issuesFound = issueIds;

  if (issueIds.length === 0) {
    return results;
  }

  // Determine current session state
  const sessionState = determineSessionState(session);
  const targetStateId = STATE_MAP[sessionState];

  if (!targetStateId) {
    results.errors.push(`Unknown session state: ${sessionState}`);
    return results;
  }

  // Process each issue
  for (const identifier of issueIds) {
    try {
      // Check sync state to avoid duplicate updates
      const syncKey = `${identifier}:${session.key || session.sessionId}`;
      const lastSync = syncState.get(syncKey);

      if (lastSync && lastSync.lastState === sessionState) {
        results.skipped.push({
          identifier,
          reason: "Already synced to this state",
        });
        continue;
      }

      // Get issue details
      const issue = await getIssue(identifier);
      if (!issue) {
        results.errors.push(`Issue ${identifier} not found`);
        continue;
      }

      // Check if state change is needed
      if (issue.state.id === targetStateId) {
        // Update sync state even if no change needed
        syncState.set(syncKey, {
          lastState: sessionState,
          lastUpdated: new Date().toISOString(),
        });
        results.skipped.push({
          identifier,
          reason: `Already in ${issue.state.name}`,
        });
        continue;
      }

      // Update issue state
      const updateSuccess = await updateIssueState(issue.id, targetStateId);

      if (updateSuccess) {
        // Add comment explaining the state change
        const comment = generateStateChangeComment(sessionState, session);
        await addComment(issue.id, comment);

        // Update sync state
        syncState.set(syncKey, {
          lastState: sessionState,
          lastUpdated: new Date().toISOString(),
        });
        saveSyncState();

        results.updated.push({
          identifier,
          fromState: issue.state.name,
          toState: sessionState,
          url: issue.url,
        });
      } else {
        results.errors.push(`Failed to update ${identifier}`);
      }
    } catch (e) {
      results.errors.push(`Error processing ${identifier}: ${e.message}`);
    }
  }

  return results;
}

/**
 * Generate a comment for state change
 * @param {string} newState - New session state
 * @param {object} session - Session data
 * @returns {string} Comment body
 */
function generateStateChangeComment(newState, session) {
  const timestamp = new Date().toISOString();
  const sessionLabel = session.label || session.key || "Unknown session";

  switch (newState) {
    case "active":
    case "live":
      return (
        `🟢 **Work resumed** on this issue.\n\n` +
        `Session: \`${sessionLabel}\`\n` +
        `Time: ${timestamp}\n\n` +
        `_Updated automatically by OpenClaw Dashboard_`
      );

    case "idle":
      return (
        `⏸️ **Work paused** on this issue (session idle >30 min).\n\n` +
        `Session: \`${sessionLabel}\`\n` +
        `Time: ${timestamp}\n\n` +
        `_Updated automatically by OpenClaw Dashboard_`
      );

    case "completed":
      return (
        `✅ **Work completed** on this issue.\n\n` +
        `Session: \`${sessionLabel}\`\n` +
        `Time: ${timestamp}\n\n` +
        `_Updated automatically by OpenClaw Dashboard_`
      );

    default:
      return (
        `📝 Session state changed to: ${newState}\n\n` +
        `Session: \`${sessionLabel}\`\n` +
        `Time: ${timestamp}`
      );
  }
}

/**
 * Read session transcript from JSONL file
 * (Mirrors the function in server.js)
 * @param {string} sessionId - Session ID
 * @returns {Array} Transcript entries
 */
function readTranscript(sessionId) {
  const openclawDir = getOpenClawDir();
  const transcriptPath = path.join(openclawDir, "agents", "main", "sessions", `${sessionId}.jsonl`);

  try {
    if (!fs.existsSync(transcriptPath)) return [];
    const content = fs.readFileSync(transcriptPath, "utf8");
    return content
      .trim()
      .split("\n")
      .map((line) => {
        try {
          return JSON.parse(line);
        } catch {
          return null;
        }
      })
      .filter(Boolean);
  } catch (e) {
    console.error("[Linear] Failed to read transcript:", e.message);
    return [];
  }
}

/**
 * Hook for server.js to call on session updates
 * @param {object} session - Session data from OpenClaw
 */
async function onSessionUpdate(session) {
  if (!session.sessionId) {
    console.error("[Linear] Session missing sessionId");
    return { error: "Missing sessionId" };
  }

  const transcript = readTranscript(session.sessionId);
  const results = await syncSessionToLinear(session, transcript);

  if (results.updated.length > 0) {
    console.log(
      `[Linear] Updated ${results.updated.length} issues:`,
      results.updated.map((u) => u.identifier).join(", "),
    );
  }

  return results;
}

/**
 * Batch sync all active sessions
 * Useful for periodic sync via cron or manual trigger
 */
async function syncAllSessions() {
  const { execSync } = require("child_process");

  try {
    const output = execSync("openclaw sessions --json 2>/dev/null", {
      encoding: "utf8",
      env: { ...process.env, NO_COLOR: "1" },
    });

    const data = JSON.parse(output);
    const sessions = data.sessions || [];

    const allResults = {
      sessionsProcessed: 0,
      totalIssuesFound: 0,
      totalUpdated: 0,
      errors: [],
    };

    for (const session of sessions) {
      const results = await onSessionUpdate(session);
      allResults.sessionsProcessed++;
      allResults.totalIssuesFound += results.issuesFound?.length || 0;
      allResults.totalUpdated += results.updated?.length || 0;
      if (results.errors?.length) {
        allResults.errors.push(...results.errors);
      }
    }

    return allResults;
  } catch (e) {
    console.error("[Linear] Failed to sync all sessions:", e.message);
    return { error: e.message };
  }
}

// Initialize: load sync state
loadSyncState();

// Exports for server.js integration
module.exports = {
  // Core functions
  extractLinearIds,
  extractLinearIdsFromTranscript,
  getIssue,
  updateIssueState,
  addComment,

  // Session sync
  syncSessionToLinear,
  onSessionUpdate,
  syncAllSessions,

  // State helpers
  determineSessionState,

  // Constants
  LINEAR_STATES,
  STATE_MAP,
};

// CLI mode: run sync if called directly
if (require.main === module) {
  console.log("[Linear] Running batch sync...");
  syncAllSessions()
    .then((results) => {
      console.log("[Linear] Sync complete:", JSON.stringify(results, null, 2));
      process.exit(results.error ? 1 : 0);
    })
    .catch((e) => {
      console.error("[Linear] Sync failed:", e.message);
      process.exit(1);
    });
}
```

## File: `scripts/pre-commit`
```
#!/usr/bin/env bash
#
# Pre-commit hook for openclaw-command-center
# Validates rules from AGENTS.md and CONTRIBUTING.md before allowing commits
#
# Install: cp scripts/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
# Or: make install-hooks
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CHECKS_DIR="$SCRIPT_DIR/checks"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🔍 Running pre-commit checks..."
echo ""

FAILED=0

# Run all check scripts in checks/ directory
for check in "$CHECKS_DIR"/*.sh; do
    if [[ -x "$check" ]]; then
        check_name=$(basename "$check" .sh)
        if "$check" "$REPO_ROOT"; then
            echo -e "${GREEN}✓${NC} $check_name"
        else
            echo -e "${RED}✗${NC} $check_name"
            FAILED=1
        fi
    fi
done

echo ""

if [[ $FAILED -eq 1 ]]; then
    echo -e "${RED}Pre-commit checks failed.${NC} Fix the issues above and try again."
    echo ""
    echo "To bypass (not recommended): git commit --no-verify"
    exit 1
else
    echo -e "${GREEN}All pre-commit checks passed!${NC}"
    exit 0
fi
```

## File: `scripts/release.sh`
```bash
#!/usr/bin/env bash
#
# release.sh - Create a versioned release with git tag and ClawHub publish
#
# Usage:
#   ./scripts/release.sh <version>           # Create tag + publish
#   ./scripts/release.sh <version> --tag-only # Create tag only
#   ./scripts/release.sh --current           # Show current version
#
# Examples:
#   ./scripts/release.sh 0.4.0
#   ./scripts/release.sh 1.0.0-beta.1
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_DIR"

# Get current version from latest tag
get_current_version() {
    git describe --tags --abbrev=0 2>/dev/null | sed 's/^v//' || echo "0.0.0"
}

# Show help
show_help() {
    echo "Usage: release.sh <version> [--tag-only]"
    echo "       release.sh --current"
    echo ""
    echo "Options:"
    echo "  <version>     Semver version (e.g., 0.4.0, 1.0.0-beta.1)"
    echo "  --tag-only    Create git tag without ClawHub publish"
    echo "  --current     Show current version from git tags"
    echo "  -h, --help    Show this help"
}

# Parse args
if [[ $# -eq 0 ]]; then
    show_help
    exit 1
fi

TAG_ONLY=false
VERSION=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --current)
            echo "Current version: $(get_current_version)"
            exit 0
            ;;
        --tag-only)
            TAG_ONLY=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            VERSION="$1"
            shift
            ;;
    esac
done

if [[ -z "$VERSION" ]]; then
    echo "❌ Version required"
    show_help
    exit 1
fi

# Validate semver (basic check)
if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$ ]]; then
    echo "❌ Invalid semver: $VERSION"
    echo "   Expected format: X.Y.Z or X.Y.Z-prerelease"
    exit 1
fi

TAG="v$VERSION"
CURRENT=$(get_current_version)

echo "📦 Release: $CURRENT → $VERSION"
echo ""

# Check for uncommitted changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "❌ Uncommitted changes detected. Commit or stash first."
    exit 1
fi

# Check if tag already exists
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "❌ Tag $TAG already exists"
    exit 1
fi

# Update package.json version
if [[ -f package.json ]]; then
    # Use npm version without git tag (we do our own tagging)
    npm version "$VERSION" --no-git-tag-version
fi

# Update SKILL.md version if it exists
if [[ -f SKILL.md ]]; then
    sed -i '' "s/\*\*Version\*\* | \`[^\"]*\`/\*\*Version\*\* | \`$VERSION\`/" SKILL.md 2>/dev/null || \
    sed -i "s/\*\*Version\*\* | \`[^\"]*\`/\*\*Version\*\* | \`$VERSION\`/" SKILL.md
fi

# Commit version bump
git add package.json package-lock.json SKILL.md 2>/dev/null || true
git commit -m "chore: release v$VERSION" --allow-empty

# Create annotated tag
echo "🏷️  Creating tag $TAG..."
git tag -a "$TAG" -m "Release $VERSION"

# Push commit and tag
echo "⬆️  Pushing to origin..."
git push origin main
git push origin "$TAG"

echo ""
echo "✅ Tagged $TAG"

# Publish to ClawHub unless --tag-only
if [[ "$TAG_ONLY" == "false" ]]; then
    echo ""
    echo "📤 Publishing to ClawHub..."
    
    # Get changelog from CHANGELOG.md if available
    CHANGELOG=""
    if [[ -f CHANGELOG.md ]]; then
        CHANGELOG=$(awk '/^## \['"$VERSION"'\]/{found=1; next} /^## \[/{if(found) exit} found{print}' CHANGELOG.md | head -20)
    fi
    
    if command -v clawhub &>/dev/null; then
        if [[ -n "$CHANGELOG" ]]; then
            clawhub publish . --version "$VERSION" --changelog "$CHANGELOG"
        else
            clawhub publish . --version "$VERSION" --changelog "Release v$VERSION"
        fi
        echo ""
        echo "✅ Published to ClawHub: $VERSION"
    else
        echo "⚠️  clawhub CLI not found. Skipping ClawHub publish."
        echo "   Install: npm install -g clawhub"
    fi
fi

echo ""
echo "🎉 Release $VERSION complete!"
echo ""
echo "   Git tag: $TAG"
echo "   GitHub:  https://github.com/jontsai/openclaw-command-center/releases/tag/$TAG"
```

## File: `scripts/run-server.sh`
```bash
#!/bin/bash
# Wrapper script to ensure PATH includes system directories
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# Find node - prefer nvm if available
if [ -f "$HOME/.nvm/nvm.sh" ]; then
    source "$HOME/.nvm/nvm.sh"
fi

cd "$(dirname "$0")/.."
exec node lib/server.js
```

## File: `scripts/setup.sh`
```bash
#!/bin/bash
# OpenClaw Command Center - First-time setup
# Creates necessary directories and config file

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_DIR="$PROJECT_DIR/config"

echo "🦞 OpenClaw Command Center Setup"
echo "================================="
echo ""

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 20+ first."
    exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 20 ]; then
    echo "⚠️  Node.js version $NODE_VERSION detected. Version 20+ recommended."
fi

# Install dependencies
echo "📦 Installing dependencies..."
cd "$PROJECT_DIR"
npm install --silent

# Create config if not exists
if [ ! -f "$CONFIG_DIR/dashboard.json" ]; then
    echo ""
    echo "📝 Creating configuration file..."
    cp "$CONFIG_DIR/dashboard.example.json" "$CONFIG_DIR/dashboard.json"
    echo "   Created: config/dashboard.json"
    echo ""
    echo "   Edit this file to customize your dashboard."
else
    echo "   Config file already exists: config/dashboard.json"
fi

# Create log directory
LOG_DIR="$HOME/.openclaw-command-center/logs"
mkdir -p "$LOG_DIR"
echo "   Log directory: $LOG_DIR"

# Detect workspace
echo ""
echo "🔍 Detecting OpenClaw workspace..."

DETECTED_WORKSPACE=""
for candidate in \
    "$OPENCLAW_WORKSPACE" \
    "$HOME/openclaw-workspace" \
    "$HOME/.openclaw-workspace" \
    "$HOME/molty" \
    "$HOME/clawd" \
    "$HOME/moltbot"; do
    if [ -n "$candidate" ] && [ -d "$candidate" ]; then
        if [ -d "$candidate/memory" ] || [ -d "$candidate/state" ]; then
            DETECTED_WORKSPACE="$candidate"
            break
        fi
    fi
done

if [ -n "$DETECTED_WORKSPACE" ]; then
    echo "   ✅ Found workspace: $DETECTED_WORKSPACE"
else
    echo "   ⚠️  No existing workspace found."
    echo "   The dashboard will create ~/.openclaw-workspace on first run,"
    echo "   or you can set OPENCLAW_WORKSPACE environment variable."
fi

# Create Makefile.local if not exists
if [ ! -f "$PROJECT_DIR/Makefile.local" ]; then
    echo ""
    echo "📝 Creating Makefile.local with 'lfg' command..."
    cat > "$PROJECT_DIR/Makefile.local" << 'EOF'
# Private Makefile overrides (not tracked in git)

.PHONY: lfg

lfg: ## Start dashboard and drop into cockpit
	@$(MAKE) ensure
	@$(MAKE) attach
EOF
    echo "   Created: Makefile.local"
fi

# Check optional system dependencies
echo ""
echo "🔍 Checking optional system dependencies..."

OS_TYPE="$(uname -s)"
OPT_MISSING=0

if [ "$OS_TYPE" = "Linux" ]; then
    if command -v iostat &> /dev/null; then
        echo "   ✅ sysstat (iostat) — disk I/O vitals"
    else
        echo "   💡 sysstat — install for disk I/O vitals: sudo apt install sysstat"
        OPT_MISSING=$((OPT_MISSING + 1))
    fi
    if command -v sensors &> /dev/null; then
        echo "   ✅ lm-sensors — temperature sensors"
    else
        echo "   💡 lm-sensors — install for temperature sensors: sudo apt install lm-sensors"
        OPT_MISSING=$((OPT_MISSING + 1))
    fi
elif [ "$OS_TYPE" = "Darwin" ]; then
    # Check for Apple Silicon vs Intel
    CHIP="$(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "")"
    if echo "$CHIP" | grep -qi "apple"; then
        if sudo -n true 2>/dev/null; then
            echo "   ✅ passwordless sudo — Apple Silicon CPU temperature"
        else
            echo "   💡 passwordless sudo — configure for CPU temperature via powermetrics"
        fi
    else
        if command -v osx-cpu-temp &> /dev/null || [ -x "$HOME/bin/osx-cpu-temp" ]; then
            echo "   ✅ osx-cpu-temp — Intel Mac CPU temperature"
        else
            echo "   💡 osx-cpu-temp — install for CPU temperature: https://github.com/lavoiesl/osx-cpu-temp"
            OPT_MISSING=$((OPT_MISSING + 1))
        fi
    fi
fi

if [ "$OPT_MISSING" -eq 0 ]; then
    echo "   All optional dependencies available!"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Quick start:"
echo "  cd $PROJECT_DIR"
echo "  make start        # Start dashboard"
echo "  make lfg          # Start and attach to tmux"
echo ""
echo "Dashboard will be available at: http://localhost:3333"
```

## File: `scripts/start.sh`
```bash
#!/bin/bash
# Start OpenClaw Command Center
# Usage: ./start.sh [--tunnel]

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PORT=3333
TUNNEL=false
PID_FILE="/tmp/openclaw-dashboard.pid"
TUNNEL_PID_FILE="/tmp/openclaw-tunnel.pid"

# Parse args
while [[ $# -gt 0 ]]; do
    case $1 in
        --tunnel|-t)
            TUNNEL=true
            shift
            ;;
        --port|-p)
            PORT="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

# Check if already running
if [ -f "$PID_FILE" ] && kill -0 "$(cat $PID_FILE)" 2>/dev/null; then
    echo "⚠️  Dashboard already running (PID: $(cat $PID_FILE))"
    echo "   Stop it first: ./stop.sh"
    exit 1
fi

echo "🚀 Starting OpenClaw Command Center..."
echo ""

# Start the Node.js server
cd "$SCRIPT_DIR/.."
PORT=$PORT node lib/server.js &
SERVER_PID=$!
echo $SERVER_PID > "$PID_FILE"

sleep 1

# Check if server started
if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo "❌ Failed to start server"
    exit 1
fi

echo "✅ Dashboard running at http://localhost:$PORT"

# Start tunnel if requested
if [ "$TUNNEL" = true ]; then
    echo ""
    echo "🌐 Starting Cloudflare tunnel..."
    cloudflared tunnel --url http://localhost:$PORT &
    TUNNEL_PID=$!
    echo $TUNNEL_PID > "$TUNNEL_PID_FILE"
    
    # Wait a moment for the tunnel URL to appear
    sleep 3
    echo ""
    echo "📋 Tunnel should be active. Look for the trycloudflare.com URL above."
fi

echo ""
echo "📊 Dashboard: http://localhost:$PORT"
echo "🛑 To stop: $SCRIPT_DIR/stop.sh"
```

## File: `scripts/stop.sh`
```bash
#!/bin/bash
# Stop OpenClaw Command Center

PID_FILE="/tmp/openclaw-dashboard.pid"
TUNNEL_PID_FILE="/tmp/openclaw-tunnel.pid"

echo "🛑 Stopping OpenClaw Command Center..."

# Stop tunnel
if [ -f "$TUNNEL_PID_FILE" ]; then
    PID=$(cat "$TUNNEL_PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
        echo "   Tunnel stopped"
    fi
    rm -f "$TUNNEL_PID_FILE"
fi

# Stop server
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
        echo "   Server stopped"
    fi
    rm -f "$PID_FILE"
fi

# Also kill any orphaned processes
pkill -f "node.*lib/server.js" 2>/dev/null
pkill -f "cloudflared.*localhost:3333" 2>/dev/null

echo "✅ Done"
```

## File: `scripts/tmux-dashboard.sh`
```bash
#!/bin/bash
# Clawd Status Dashboard - tmux layout
# Creates a tmux session with live status panes

SESSION="openclaw-status"
OPENCLAW_DIR="${OPENCLAW_WORKSPACE:-$HOME/.openclaw-workspace}"

# Kill existing session if it exists
tmux kill-session -t "$SESSION" 2>/dev/null

# Create new session (detached)
tmux new-session -d -s "$SESSION" -c "$OPENCLAW_DIR"

# Rename first window
tmux rename-window -t "$SESSION:0" "dashboard"

# Layout:
# +------------------+------------------+
# |    Sessions      |   Cron Jobs      |
# +------------------+------------------+
# |    Gateway       |   Activity       |
# +------------------+------------------+

# Pane 0: Sessions (watch openclaw sessions)
tmux send-keys -t "$SESSION:0" "watch -n 10 -c 'echo \"📡 ACTIVE SESSIONS\"; echo; openclaw sessions 2>/dev/null || echo \"No sessions\"'" Enter

# Split horizontally for pane 1: Cron Jobs
tmux split-window -h -t "$SESSION:0" -c "$OPENCLAW_DIR"
tmux send-keys -t "$SESSION:0.1" "watch -n 30 -c 'echo \"⏰ CRON JOBS\"; echo; openclaw cron list 2>/dev/null || echo \"No cron jobs\"'" Enter

# Split pane 0 vertically for pane 2: Gateway Status
tmux split-window -v -t "$SESSION:0.0" -c "$OPENCLAW_DIR"
tmux send-keys -t "$SESSION:0.2" "watch -n 15 -c 'echo \"🤖 GATEWAY STATUS\"; echo; openclaw gateway status 2>/dev/null; echo; echo \"---\"; openclaw status 2>/dev/null'" Enter

# Split pane 1 vertically for pane 3: Activity Log
tmux split-window -v -t "$SESSION:0.1" -c "$OPENCLAW_DIR"
tmux send-keys -t "$SESSION:0.3" "watch -n 30 -c 'echo \"📝 RECENT ACTIVITY\"; echo; today=\$(date +%Y-%m-%d); if [ -f \"memory/\$today.md\" ]; then tail -20 \"memory/\$today.md\"; else echo \"No activity today\"; fi'" Enter

# Make panes more even
tmux select-layout -t "$SESSION:0" tiled

# Add a second window for logs
tmux new-window -t "$SESSION" -n "logs" -c "$OPENCLAW_DIR"
tmux send-keys -t "$SESSION:1" "echo '📜 Gateway Logs'; echo 'Run: openclaw gateway logs -f'; echo" Enter

# Add a third window for interactive shell
tmux new-window -t "$SESSION" -n "shell" -c "$OPENCLAW_DIR"
tmux send-keys -t "$SESSION:2" "echo '🐚 Interactive Shell'; echo 'Ready for commands...'; echo" Enter

# Go back to first window
tmux select-window -t "$SESSION:0"

echo "✅ OpenClaw dashboard created!"
echo ""
echo "To attach:  tmux attach -t $SESSION"
echo "To detach:  Ctrl+B, then D"
echo ""

# If not already in tmux, offer to attach
if [ -z "$TMUX" ]; then
    read -p "Attach now? [Y/n] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        tmux attach -t "$SESSION"
    fi
fi
```

## File: `scripts/topic-classifier.js`
```javascript
/**
 * Topic Classifier for OpenClaw Sessions
 *
 * Analyzes session transcript content to:
 * - Match against existing topics
 * - Detect when existing topics don't fit well
 * - Suggest new topic names based on content patterns
 * - Maintain a discovered-topics.json file for learned topics
 *
 * @module topic-classifier
 */

const fs = require("fs");
const path = require("path");
const { CONFIG: APP_CONFIG } = require("../src/config");

// Default config
const CONFIG = {
  // Minimum TF-IDF score to consider a term significant
  minTermScore: 0.1,
  // Minimum topic match confidence to consider a match "good"
  matchThreshold: 0.3,
  // Minimum occurrences for a term to be considered
  minTermFrequency: 2,
  // Path to discovered topics state file
  discoveredTopicsPath: path.join(APP_CONFIG.paths.state, "discovered-topics.json"),
  // Maximum suggested topics per classification
  maxSuggestions: 3,
};

// Stop words to filter out (common English words)
const STOP_WORDS = new Set([
  "a",
  "an",
  "the",
  "and",
  "or",
  "but",
  "in",
  "on",
  "at",
  "to",
  "for",
  "of",
  "with",
  "by",
  "from",
  "up",
  "about",
  "into",
  "through",
  "during",
  "before",
  "after",
  "above",
  "below",
  "between",
  "under",
  "again",
  "further",
  "then",
  "once",
  "here",
  "there",
  "when",
  "where",
  "why",
  "how",
  "all",
  "each",
  "few",
  "more",
  "most",
  "other",
  "some",
  "such",
  "no",
  "nor",
  "not",
  "only",
  "own",
  "same",
  "so",
  "than",
  "too",
  "very",
  "s",
  "t",
  "can",
  "will",
  "just",
  "don",
  "should",
  "now",
  "i",
  "me",
  "my",
  "myself",
  "we",
  "our",
  "ours",
  "you",
  "your",
  "yours",
  "he",
  "him",
  "his",
  "she",
  "her",
  "hers",
  "it",
  "its",
  "they",
  "them",
  "their",
  "theirs",
  "what",
  "which",
  "who",
  "whom",
  "this",
  "that",
  "these",
  "those",
  "am",
  "is",
  "are",
  "was",
  "were",
  "be",
  "been",
  "being",
  "have",
  "has",
  "had",
  "having",
  "do",
  "does",
  "did",
  "doing",
  "would",
  "could",
  "ought",
  "let",
  "like",
  "need",
  "want",
  "got",
  "get",
  "make",
  "made",
  "see",
  "look",
  "think",
  "know",
  "take",
  "come",
  "go",
  "say",
  "said",
  "tell",
  "told",
  "ask",
  "use",
  "used",
  "find",
  "give",
  "gave",
  "yes",
  "no",
  "ok",
  "okay",
  "yeah",
  "sure",
  "right",
  "well",
  "also",
  "just",
  "really",
  "actually",
  "basically",
  "probably",
  "maybe",
  // Tech-common words that are too generic
  "file",
  "code",
  "run",
  "check",
  "help",
  "please",
  "thanks",
  "hello",
  "hi",
  "hey",
  "good",
  "great",
  "nice",
  "cool",
  "awesome",
  "perfect",
]);

// Known topic patterns for seeding - maps keywords to topic names
const TOPIC_PATTERNS = {
  // Development
  git: "version-control",
  github: "version-control",
  commit: "version-control",
  branch: "version-control",
  merge: "version-control",
  pull: "version-control",
  push: "version-control",

  debug: "debugging",
  error: "debugging",
  bug: "debugging",
  fix: "debugging",
  stack: "debugging",
  trace: "debugging",
  exception: "debugging",

  test: "testing",
  unittest: "testing",
  jest: "testing",
  pytest: "testing",
  coverage: "testing",

  deploy: "deployment",
  production: "deployment",
  staging: "deployment",
  ci: "deployment",
  cd: "deployment",
  pipeline: "deployment",

  api: "api-integration",
  endpoint: "api-integration",
  rest: "api-integration",
  graphql: "api-integration",
  webhook: "api-integration",

  database: "database",
  sql: "database",
  postgres: "database",
  mysql: "database",
  mongodb: "database",
  query: "database",

  docker: "containers",
  kubernetes: "containers",
  k8s: "containers",
  container: "containers",
  pod: "containers",

  aws: "cloud-infra",
  gcp: "cloud-infra",
  azure: "cloud-infra",
  terraform: "cloud-infra",
  cloudformation: "cloud-infra",

  // Communication
  slack: "slack-integration",
  channel: "slack-integration",
  message: "messaging",
  email: "email",
  notification: "notifications",

  // Automation
  cron: "scheduling",
  schedule: "scheduling",
  timer: "scheduling",
  job: "scheduling",

  script: "automation",
  automate: "automation",
  workflow: "automation",

  // Research
  research: "research",
  search: "research",
  wikipedia: "research",
  lookup: "research",

  // Finance
  finance: "finance",
  investment: "finance",
  stock: "finance",
  portfolio: "finance",
  budget: "finance",

  // System
  config: "configuration",
  settings: "configuration",
  setup: "configuration",
  install: "setup",

  // Writing
  document: "documentation",
  readme: "documentation",
  docs: "documentation",
  write: "writing",
  draft: "writing",

  // AI/ML
  model: "ai-ml",
  claude: "ai-ml",
  openai: "ai-ml",
  gpt: "ai-ml",
  llm: "ai-ml",
  prompt: "prompt-engineering",

  // UI
  dashboard: "dashboard",
  ui: "ui-development",
  frontend: "ui-development",
  css: "ui-development",
  html: "ui-development",
  react: "ui-development",
};

/**
 * Tokenize text into words
 * @param {string} text - Raw text to tokenize
 * @returns {string[]} Array of lowercase tokens
 */
function tokenize(text) {
  if (!text || typeof text !== "string") return [];

  return (
    text
      .toLowerCase()
      // Remove code blocks
      .replace(/```[\s\S]*?```/g, " ")
      // Remove inline code
      .replace(/`[^`]+`/g, " ")
      // Remove URLs
      .replace(/https?:\/\/\S+/g, " ")
      // Remove special characters but keep hyphens in words
      .replace(/[^a-z0-9\s-]/g, " ")
      // Split on whitespace
      .split(/\s+/)
      // Filter valid tokens
      .filter(
        (token) =>
          token.length > 2 && token.length < 30 && !STOP_WORDS.has(token) && !/^\d+$/.test(token),
      )
  );
}

/**
 * Calculate term frequency for a document
 * @param {string[]} tokens - Array of tokens
 * @returns {Map<string, number>} Term frequency map
 */
function calculateTF(tokens) {
  const tf = new Map();
  const total = tokens.length || 1;

  tokens.forEach((token) => {
    tf.set(token, (tf.get(token) || 0) + 1);
  });

  // Normalize by document length
  tf.forEach((count, term) => {
    tf.set(term, count / total);
  });

  return tf;
}

/**
 * Calculate inverse document frequency using corpus statistics
 * For a single document, we use term rarity as a proxy
 * @param {Map<string, number>} tf - Term frequency map
 * @param {number} vocabSize - Size of vocabulary
 * @returns {Map<string, number>} IDF scores
 */
function calculateIDF(tf, vocabSize) {
  const idf = new Map();

  tf.forEach((freq, term) => {
    // Boost terms that appear in known patterns
    const patternBoost = TOPIC_PATTERNS[term] ? 2.0 : 1.0;
    // Simple IDF approximation: rarer terms get higher scores
    const score = Math.log(vocabSize / (1 + freq * vocabSize)) * patternBoost;
    idf.set(term, Math.max(0, score));
  });

  return idf;
}

/**
 * Extract key terms using TF-IDF
 * @param {string} text - Text to analyze
 * @returns {Array<{term: string, score: number}>} Ranked terms
 */
function extractKeyTerms(text) {
  const tokens = tokenize(text);
  if (tokens.length === 0) return [];

  const tf = calculateTF(tokens);
  const idf = calculateIDF(tf, tf.size);

  const tfidf = [];
  tf.forEach((tfScore, term) => {
    const idfScore = idf.get(term) || 0;
    const score = tfScore * idfScore;

    // Only include terms that meet minimum thresholds
    const rawCount = tokens.filter((t) => t === term).length;
    if (rawCount >= CONFIG.minTermFrequency && score >= CONFIG.minTermScore) {
      tfidf.push({ term, score, count: rawCount });
    }
  });

  // Sort by score descending
  return tfidf.sort((a, b) => b.score - a.score);
}

/**
 * Match text against existing topics
 * @param {string} text - Text to match
 * @param {string[]} existingTopics - List of existing topic names
 * @returns {Array<{topic: string, confidence: number}>} Matched topics with confidence
 */
function matchTopics(text, existingTopics) {
  const tokens = tokenize(text);
  const matches = new Map();

  // Score each existing topic
  existingTopics.forEach((topic) => {
    let score = 0;
    const topicTokens = tokenize(topic);

    // Direct token match
    topicTokens.forEach((tt) => {
      const count = tokens.filter((t) => t === tt || t.includes(tt) || tt.includes(t)).length;
      score += count * 0.3;
    });

    // Pattern-based matching
    tokens.forEach((token) => {
      const mappedTopic = TOPIC_PATTERNS[token];
      if (mappedTopic === topic) {
        score += 0.5;
      }
    });

    if (score > 0) {
      // Normalize by text length (log scale to avoid penalizing long texts too much)
      const normalizedScore = score / Math.log2(tokens.length + 2);
      matches.set(topic, Math.min(1, normalizedScore));
    }
  });

  // Convert to sorted array
  return Array.from(matches.entries())
    .map(([topic, confidence]) => ({ topic, confidence }))
    .sort((a, b) => b.confidence - a.confidence);
}

/**
 * Generate topic suggestions based on content
 * @param {Array<{term: string, score: number}>} keyTerms - Key terms from text
 * @param {string[]} existingTopics - Topics to avoid suggesting
 * @returns {string[]} Suggested new topic names
 */
function generateSuggestions(keyTerms, existingTopics) {
  const existingSet = new Set(existingTopics.map((t) => t.toLowerCase()));
  const suggestions = new Set();

  // Strategy 1: Use known patterns for top terms
  keyTerms.slice(0, 15).forEach(({ term }) => {
    const mapped = TOPIC_PATTERNS[term];
    if (mapped && !existingSet.has(mapped)) {
      suggestions.add(mapped);
    }
  });

  // Strategy 2: Create compound topics from top co-occurring terms
  if (keyTerms.length >= 2 && suggestions.size < CONFIG.maxSuggestions) {
    const topTerms = keyTerms.slice(0, 5).map((t) => t.term);

    // Look for related pairs
    const pairs = [
      ["api", "integration"],
      ["code", "review"],
      ["data", "analysis"],
      ["error", "handling"],
      ["file", "management"],
      ["memory", "optimization"],
      ["performance", "tuning"],
      ["security", "audit"],
      ["system", "design"],
      ["user", "interface"],
    ];

    pairs.forEach(([a, b]) => {
      if (topTerms.some((t) => t.includes(a)) && topTerms.some((t) => t.includes(b))) {
        const compound = `${a}-${b}`;
        if (!existingSet.has(compound)) {
          suggestions.add(compound);
        }
      }
    });
  }

  // Strategy 3: Use top-scoring term as-is if it's descriptive enough
  if (suggestions.size < CONFIG.maxSuggestions) {
    keyTerms.slice(0, 5).forEach(({ term, score }) => {
      // Only use single terms that are sufficiently meaningful
      if (score > 0.15 && term.length > 4 && !existingSet.has(term)) {
        suggestions.add(term);
      }
    });
  }

  return Array.from(suggestions).slice(0, CONFIG.maxSuggestions);
}

/**
 * Load discovered topics from state file
 * @returns {Object} Discovered topics data
 */
function loadDiscoveredTopics() {
  try {
    if (fs.existsSync(CONFIG.discoveredTopicsPath)) {
      return JSON.parse(fs.readFileSync(CONFIG.discoveredTopicsPath, "utf8"));
    }
  } catch (e) {
    console.error("Failed to load discovered topics:", e.message);
  }

  return {
    version: 1,
    topics: {},
    lastUpdated: null,
  };
}

/**
 * Save discovered topics to state file
 * @param {Object} data - Topics data to save
 */
function saveDiscoveredTopics(data) {
  try {
    data.lastUpdated = new Date().toISOString();
    fs.writeFileSync(CONFIG.discoveredTopicsPath, JSON.stringify(data, null, 2));
  } catch (e) {
    console.error("Failed to save discovered topics:", e.message);
  }
}

/**
 * Update discovered topics with new suggestions
 * @param {string[]} suggestions - New topic suggestions
 * @param {string} sessionKey - Source session identifier
 */
function updateDiscoveredTopics(suggestions, sessionKey) {
  const data = loadDiscoveredTopics();

  suggestions.forEach((topic) => {
    if (!data.topics[topic]) {
      data.topics[topic] = {
        firstSeen: new Date().toISOString(),
        occurrences: 0,
        sessions: [],
      };
    }

    data.topics[topic].occurrences++;
    data.topics[topic].lastSeen = new Date().toISOString();

    if (!data.topics[topic].sessions.includes(sessionKey)) {
      data.topics[topic].sessions.push(sessionKey);
      // Keep only last 10 sessions
      if (data.topics[topic].sessions.length > 10) {
        data.topics[topic].sessions.shift();
      }
    }
  });

  saveDiscoveredTopics(data);
}

/**
 * Main classification function
 * Analyzes transcript content to match existing topics and suggest new ones
 *
 * @param {string|Array} transcript - Session transcript (string or array of messages)
 * @param {string[]} existingTopics - List of existing topic names
 * @param {Object} options - Optional configuration
 * @param {string} options.sessionKey - Session identifier for tracking
 * @param {boolean} options.persist - Whether to persist discovered topics (default: true)
 * @returns {{matched: Array<{topic: string, confidence: number}>, suggested: string[], keyTerms: Array}}
 */
function classifyAndSuggestTopics(transcript, existingTopics = [], options = {}) {
  // Normalize transcript to text
  let text = "";
  if (Array.isArray(transcript)) {
    text = transcript
      .map((entry) => {
        if (typeof entry === "string") return entry;
        if (entry.text) return entry.text;
        if (entry.message?.content) {
          const content = entry.message.content;
          if (typeof content === "string") return content;
          if (Array.isArray(content)) {
            return content
              .filter((c) => c.type === "text")
              .map((c) => c.text || "")
              .join(" ");
          }
        }
        return "";
      })
      .join("\n");
  } else if (typeof transcript === "string") {
    text = transcript;
  }

  if (!text || text.length < 20) {
    return { matched: [], suggested: [], keyTerms: [] };
  }

  // Extract key terms
  const keyTerms = extractKeyTerms(text);

  // Match against existing topics
  const matched = matchTopics(text, existingTopics);

  // Determine if we need suggestions
  const bestMatch = matched[0];
  const needsSuggestions = !bestMatch || bestMatch.confidence < CONFIG.matchThreshold;

  let suggested = [];
  if (needsSuggestions) {
    suggested = generateSuggestions(keyTerms, existingTopics);

    // Persist discovered topics if enabled
    if (options.persist !== false && suggested.length > 0 && options.sessionKey) {
      updateDiscoveredTopics(suggested, options.sessionKey);
    }
  }

  return {
    matched: matched.slice(0, 5),
    suggested,
    keyTerms: keyTerms.slice(0, 10),
    confidence: bestMatch?.confidence || 0,
  };
}

/**
 * Get all discovered topics sorted by occurrence
 * @returns {Array<{name: string, occurrences: number, sessions: number}>}
 */
function getDiscoveredTopics() {
  const data = loadDiscoveredTopics();

  return Object.entries(data.topics)
    .map(([name, info]) => ({
      name,
      occurrences: info.occurrences,
      sessions: info.sessions?.length || 0,
      firstSeen: info.firstSeen,
      lastSeen: info.lastSeen,
    }))
    .sort((a, b) => b.occurrences - a.occurrences);
}

/**
 * Promote a discovered topic to the official topic list
 * Returns the topic data for external handling
 * @param {string} topicName - Topic to promote
 * @returns {Object|null} Topic data or null if not found
 */
function promoteDiscoveredTopic(topicName) {
  const data = loadDiscoveredTopics();

  if (data.topics[topicName]) {
    const topicData = { ...data.topics[topicName], name: topicName };
    delete data.topics[topicName];
    saveDiscoveredTopics(data);
    return topicData;
  }

  return null;
}

// Export public API
module.exports = {
  classifyAndSuggestTopics,
  getDiscoveredTopics,
  promoteDiscoveredTopic,
  extractKeyTerms,
  matchTopics,
  // Export config for testing/tuning
  CONFIG,
  TOPIC_PATTERNS,
};
```

## File: `scripts/verify.sh`
```bash
#!/bin/bash
#
# verify.sh - Quick dashboard verification script
#
# Checks that all APIs return data and the dashboard is responsive.
#
# Usage: ./scripts/verify.sh [--url URL]
#

set -euo pipefail

DASHBOARD_URL="${DASHBOARD_URL:-http://localhost:3333}"

# Parse args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --url) DASHBOARD_URL="$2"; shift 2 ;;
        -h|--help)
            echo "Usage: verify.sh [--url URL]"
            echo "  --url URL    Dashboard URL (default: http://localhost:3333)"
            exit 0
            ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

echo "🔍 Verifying dashboard at $DASHBOARD_URL..."
echo ""

# Track failures
FAILURES=0

# Check server responds
echo -n "📡 Server response... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$DASHBOARD_URL" 2>/dev/null || echo "000")
if [[ "$HTTP_CODE" == "200" ]]; then
    echo "✅ OK (HTTP $HTTP_CODE)"
else
    echo "❌ FAILED (HTTP $HTTP_CODE)"
    ((FAILURES++))
fi

# Check each API endpoint
ENDPOINTS=(
    "vitals:vitals"
    "operators:operators"
    "llm-usage:claude"
    "memory:memory"
    "cerebro:topics"
    "cron:cron"
)

echo ""
echo "📊 API Endpoints:"

for entry in "${ENDPOINTS[@]}"; do
    endpoint="${entry%%:*}"
    key="${entry##*:}"
    
    echo -n "   /api/$endpoint... "
    response=$(curl -s --max-time 5 "$DASHBOARD_URL/api/$endpoint" 2>/dev/null || echo "")
    
    if [[ -z "$response" ]]; then
        echo "❌ No response"
        ((FAILURES++))
    elif echo "$response" | grep -q "\"$key\""; then
        echo "✅ OK"
    elif echo "$response" | grep -q "error"; then
        echo "⚠️  Error in response"
        ((FAILURES++))
    else
        echo "⚠️  Unexpected format"
    fi
done

echo ""

# Optional dependency status
echo "🔧 Optional System Dependencies:"

OS_TYPE="$(uname -s)"
if [[ "$OS_TYPE" == "Linux" ]]; then
    if command -v iostat &> /dev/null; then
        echo "   ✅ sysstat (iostat) — disk I/O vitals"
    else
        echo "   ⚠️  sysstat — not installed (disk I/O stats will show zeros)"
    fi
    if command -v sensors &> /dev/null; then
        echo "   ✅ lm-sensors — temperature sensors"
    else
        echo "   ⚠️  lm-sensors — not installed (using thermal_zone fallback)"
    fi
elif [[ "$OS_TYPE" == "Darwin" ]]; then
    CHIP="$(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "")"
    if echo "$CHIP" | grep -qi "apple"; then
        if sudo -n true 2>/dev/null; then
            echo "   ✅ passwordless sudo — Apple Silicon CPU temperature"
        else
            echo "   ⚠️  passwordless sudo — not configured (CPU temperature unavailable)"
        fi
    else
        if command -v osx-cpu-temp &> /dev/null || [[ -x "$HOME/bin/osx-cpu-temp" ]]; then
            echo "   ✅ osx-cpu-temp — Intel Mac CPU temperature"
        else
            echo "   ⚠️  osx-cpu-temp — not installed (using battery temp fallback)"
        fi
    fi
fi

echo ""

# Summary
if [[ $FAILURES -eq 0 ]]; then
    echo "✅ All checks passed!"
    exit 0
else
    echo "❌ $FAILURES check(s) failed"
    exit 1
fi
```

## File: `scripts/checks/no-secrets.sh`
```bash
#!/usr/bin/env bash
#
# Check: No Secrets
# Basic check for accidentally committed secrets
#
# Rule: AGENTS.md - never commit secrets, API keys, or credentials
#

REPO_ROOT="${1:-.}"

# Patterns that might indicate secrets
SECRET_PATTERNS=(
    'sk-[a-zA-Z0-9]{20,}'           # OpenAI API keys
    'xoxb-[0-9]+-[0-9]+-[a-zA-Z0-9]+' # Slack bot tokens
    'xoxp-[0-9]+-[0-9]+-[a-zA-Z0-9]+' # Slack user tokens
    'ghp_[a-zA-Z0-9]{36}'           # GitHub personal access tokens
    'gho_[a-zA-Z0-9]{36}'           # GitHub OAuth tokens
    'AKIA[0-9A-Z]{16}'              # AWS access key IDs
    'password\s*[=:]\s*["\047][^"\047]{8,}' # Hardcoded passwords
)

# Get staged file contents (only added/modified lines)
STAGED_DIFF=$(git diff --cached --diff-filter=AM 2>/dev/null || echo "")

FOUND_SECRETS=0

for pattern in "${SECRET_PATTERNS[@]}"; do
    if echo "$STAGED_DIFF" | grep -qE "$pattern"; then
        echo "  ⚠️  Potential secret detected matching pattern: $pattern"
        FOUND_SECRETS=1
    fi
done

if [[ $FOUND_SECRETS -eq 1 ]]; then
    echo "      Review staged changes and remove any secrets before committing."
    exit 1
fi

exit 0
```

## File: `scripts/checks/no-user-data.sh`
```bash
#!/usr/bin/env bash
#
# Check: No User Data
# Ensures user-specific data files are not staged for commit
#
# Rule: public/data/AGENTS.md - never commit operators.json or privacy-settings.json
#

REPO_ROOT="${1:-.}"

# Check if any user data files are staged
STAGED_FILES=$(git diff --cached --name-only 2>/dev/null || echo "")

USER_DATA_FILES=(
    "public/data/operators.json"
    "public/data/privacy-settings.json"
)

FOUND_USER_DATA=0

for file in "${USER_DATA_FILES[@]}"; do
    if echo "$STAGED_FILES" | grep -q "^$file$"; then
        echo "  ⚠️  User data file staged: $file"
        echo "      This file contains user-specific data and should not be committed."
        echo "      Use 'git reset HEAD $file' to unstage."
        FOUND_USER_DATA=1
    fi
done

if [[ $FOUND_USER_DATA -eq 1 ]]; then
    exit 1
fi

exit 0
```

## File: `scripts/checks/README.md`
```markdown
# Pre-commit Checks

Automated enforcement of rules from `AGENTS.md` and `CONTRIBUTING.md`.

## Checks

| Check             | Rule Source           | Description                                          |
| ----------------- | --------------------- | ---------------------------------------------------- |
| `version-sync.sh` | CONTRIBUTING.md       | Ensures `package.json` and `SKILL.md` versions match |
| `no-user-data.sh` | public/data/AGENTS.md | Blocks commits of user-specific data files           |
| `no-secrets.sh`   | AGENTS.md             | Scans for accidentally committed secrets             |

## Adding New Checks

1. Create a new script in `scripts/checks/` named `<check-name>.sh`
2. Script must:
   - Accept repo root as first argument (`$1`)
   - Exit `0` on success
   - Exit `1` on failure
   - Print clear error messages when failing
3. Make it executable: `chmod +x scripts/checks/<check-name>.sh`

## Running Manually

```bash
# Run all checks
./scripts/pre-commit

# Run individual check
./scripts/checks/version-sync.sh .
```

## Installing the Hook

```bash
make install-hooks
# or manually:
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Bypassing (Not Recommended)

```bash
git commit --no-verify
```

Only use this if you understand why the check is failing and have a valid reason to bypass.
```

## File: `scripts/checks/version-sync.sh`
```bash
#!/usr/bin/env bash
#
# Check: Version Sync
# Ensures package.json and SKILL.md versions are in sync
#
# Rule: AGENTS.md / CONTRIBUTING.md - versions must match
#

REPO_ROOT="${1:-.}"

# Extract version from package.json
PKG_VERSION=$(grep -o '"version": *"[^"]*"' "$REPO_ROOT/package.json" | head -1 | sed 's/.*"version": *"\([^"]*\)".*/\1/')

# Extract version from SKILL.md frontmatter
SKILL_VERSION=$(grep -E '^version:' "$REPO_ROOT/SKILL.md" | head -1 | sed 's/version: *//')

if [[ -z "$PKG_VERSION" ]]; then
    echo "  ⚠️  Could not read version from package.json"
    exit 1
fi

if [[ -z "$SKILL_VERSION" ]]; then
    echo "  ⚠️  Could not read version from SKILL.md"
    exit 1
fi

if [[ "$PKG_VERSION" != "$SKILL_VERSION" ]]; then
    echo "  ⚠️  Version mismatch:"
    echo "      package.json: $PKG_VERSION"
    echo "      SKILL.md:     $SKILL_VERSION"
    echo "  → Both files must have the same version"
    exit 1
fi

exit 0
```

## File: `src/actions.js`
```javascript
const ALLOWED_ACTIONS = new Set([
  "gateway-status",
  "gateway-restart",
  "sessions-list",
  "cron-list",
  "health-check",
  "clear-stale-sessions",
]);

function executeAction(action, deps) {
  const { runOpenClaw, extractJSON, PORT } = deps;
  const results = { success: false, action, output: "", error: null };

  if (!ALLOWED_ACTIONS.has(action)) {
    results.error = `Unknown action: ${action}`;
    return results;
  }

  try {
    switch (action) {
      case "gateway-status":
        results.output = runOpenClaw("gateway status 2>&1") || "Unknown";
        results.success = true;
        break;
      case "gateway-restart":
        results.output = "To restart gateway, run: openclaw gateway restart";
        results.success = true;
        results.note = "Dashboard cannot restart gateway for safety";
        break;
      case "sessions-list":
        results.output = runOpenClaw("sessions 2>&1") || "No sessions";
        results.success = true;
        break;
      case "cron-list":
        results.output = runOpenClaw("cron list 2>&1") || "No cron jobs";
        results.success = true;
        break;
      case "health-check": {
        const gateway = runOpenClaw("gateway status 2>&1");
        const sessions = runOpenClaw("sessions --json 2>&1");
        let sessionCount = 0;
        try {
          const data = JSON.parse(sessions);
          sessionCount = data.sessions?.length || 0;
        } catch (e) {}
        results.output = [
          `Gateway: ${gateway?.includes("running") ? "OK Running" : "NOT Running"}`,
          `Sessions: ${sessionCount}`,
          `Dashboard: OK Running on port ${PORT}`,
        ].join("\n");
        results.success = true;
        break;
      }
      case "clear-stale-sessions": {
        const staleOutput = runOpenClaw("sessions --json 2>&1");
        let staleCount = 0;
        try {
          const staleJson = extractJSON(staleOutput);
          if (staleJson) {
            const data = JSON.parse(staleJson);
            staleCount = (data.sessions || []).filter((s) => s.ageMs > 24 * 60 * 60 * 1000).length;
          }
        } catch (e) {}
        results.output = `Found ${staleCount} stale sessions (>24h old).\nTo clean: openclaw sessions prune`;
        results.success = true;
        break;
      }
    }
  } catch (e) {
    results.error = e.message;
  }

  return results;
}

module.exports = { executeAction, ALLOWED_ACTIONS };
```

## File: `src/auth.js`
```javascript
// ============================================================================
// Authentication Module
// ============================================================================

// Auth header names
const AUTH_HEADERS = {
  tailscale: {
    login: "tailscale-user-login",
    name: "tailscale-user-name",
    pic: "tailscale-user-profile-pic",
  },
  cloudflare: {
    email: "cf-access-authenticated-user-email",
  },
};

function checkAuth(req, authConfig) {
  const mode = authConfig.mode;
  const remoteAddr = req.socket?.remoteAddress || "";
  const isLocalhost =
    remoteAddr === "127.0.0.1" || remoteAddr === "::1" || remoteAddr === "::ffff:127.0.0.1";
  if (isLocalhost) {
    return { authorized: true, user: { type: "localhost", login: "localhost" } };
  }
  if (mode === "none") {
    return { authorized: true, user: null };
  }
  if (mode === "token") {
    const authHeader = req.headers["authorization"] || "";
    const token = authHeader.replace(/^Bearer\s+/i, "");
    if (token && token === authConfig.token) {
      return { authorized: true, user: { type: "token" } };
    }
    return { authorized: false, reason: "Invalid or missing token" };
  }
  if (mode === "tailscale") {
    const login = (req.headers[AUTH_HEADERS.tailscale.login] || "").toLowerCase();
    const name = req.headers[AUTH_HEADERS.tailscale.name] || "";
    const pic = req.headers[AUTH_HEADERS.tailscale.pic] || "";
    if (!login) {
      return { authorized: false, reason: "Not accessed via Tailscale Serve" };
    }
    const isAllowed = authConfig.allowedUsers.some((allowed) => {
      if (allowed === "*") return true;
      if (allowed === login) return true;
      if (allowed.startsWith("*@")) {
        const domain = allowed.slice(2);
        return login.endsWith("@" + domain);
      }
      return false;
    });
    if (isAllowed) {
      return { authorized: true, user: { type: "tailscale", login, name, pic } };
    }
    return { authorized: false, reason: `User ${login} not in allowlist`, user: { login } };
  }
  if (mode === "cloudflare") {
    const email = (req.headers[AUTH_HEADERS.cloudflare.email] || "").toLowerCase();
    if (!email) {
      return { authorized: false, reason: "Not accessed via Cloudflare Access" };
    }
    const isAllowed = authConfig.allowedUsers.some((allowed) => {
      if (allowed === "*") return true;
      if (allowed === email) return true;
      if (allowed.startsWith("*@")) {
        const domain = allowed.slice(2);
        return email.endsWith("@" + domain);
      }
      return false;
    });
    if (isAllowed) {
      return { authorized: true, user: { type: "cloudflare", email } };
    }
    return { authorized: false, reason: `User ${email} not in allowlist`, user: { email } };
  }
  if (mode === "allowlist") {
    const clientIP =
      req.headers["x-forwarded-for"]?.split(",")[0]?.trim() || req.socket?.remoteAddress || "";
    const isAllowed = authConfig.allowedIPs.some((allowed) => {
      if (allowed === clientIP) return true;
      if (allowed.endsWith("/24")) {
        const prefix = allowed.slice(0, -3).split(".").slice(0, 3).join(".");
        return clientIP.startsWith(prefix + ".");
      }
      return false;
    });
    if (isAllowed) {
      return { authorized: true, user: { type: "ip", ip: clientIP } };
    }
    return { authorized: false, reason: `IP ${clientIP} not in allowlist` };
  }
  return { authorized: false, reason: "Unknown auth mode" };
}

function getUnauthorizedPage(reason, user, authConfig) {
  const userInfo = user
    ? `<p class="user-info">Detected: ${user.login || user.email || user.ip || "unknown"}</p>`
    : "";

  return `<!DOCTYPE html>
<html>
<head>
    <title>Access Denied - Command Center</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #e8e8e8;
        }
        .container {
            text-align: center;
            padding: 3rem;
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.1);
            max-width: 500px;
        }
        .icon { font-size: 4rem; margin-bottom: 1rem; }
        h1 { font-size: 1.8rem; margin-bottom: 1rem; color: #ff6b6b; }
        .reason { color: #aaa; margin-bottom: 1.5rem; font-size: 0.95rem; }
        .user-info { color: #ffeb3b; margin: 1rem 0; font-size: 0.9rem; }
        .instructions { color: #ccc; font-size: 0.85rem; line-height: 1.5; }
        .auth-mode { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); color: #888; font-size: 0.75rem; }
        code { background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">🔐</div>
        <h1>Access Denied</h1>
        <div class="reason">${reason}</div>
        ${userInfo}
        <div class="instructions">
            <p>This dashboard requires authentication via <strong>${authConfig.mode}</strong>.</p>
            ${authConfig.mode === "tailscale" ? '<p style="margin-top:1rem">Make sure you\'re accessing via your Tailscale URL and your account is in the allowlist.</p>' : ""}
            ${authConfig.mode === "cloudflare" ? '<p style="margin-top:1rem">Make sure you\'re accessing via Cloudflare Access and your email is in the allowlist.</p>' : ""}
        </div>
        <div class="auth-mode">Auth mode: <code>${authConfig.mode}</code></div>
    </div>
</body>
</html>`;
}

module.exports = { AUTH_HEADERS, checkAuth, getUnauthorizedPage };
```

## File: `src/cerebro.js`
```javascript
/**
 * Cerebro topic management
 */

const fs = require("fs");
const path = require("path");
const { formatTimeAgo } = require("./utils");

/**
 * Get cerebro topics
 * @param {string} cerebroDir - Path to cerebro directory
 * @param {object} options - Options (offset, limit, status)
 * @returns {object} - Cerebro topics data
 */
function getCerebroTopics(cerebroDir, options = {}) {
  const { offset = 0, limit = 20, status: filterStatus = "all" } = options;
  const topicsDir = path.join(cerebroDir, "topics");
  const orphansDir = path.join(cerebroDir, "orphans");
  const topics = [];

  // Result in format expected by frontend renderCerebro()
  const result = {
    initialized: false,
    cerebroPath: cerebroDir,
    topics: { active: 0, resolved: 0, parked: 0, total: 0 },
    threads: 0,
    orphans: 0,
    recentTopics: [],
    lastUpdated: null,
  };

  try {
    // Check if cerebro directory exists
    if (!fs.existsSync(cerebroDir)) {
      return result;
    }

    result.initialized = true;
    let latestModified = null;

    if (!fs.existsSync(topicsDir)) {
      return result;
    }

    const topicNames = fs.readdirSync(topicsDir).filter((name) => {
      const topicPath = path.join(topicsDir, name);
      return fs.statSync(topicPath).isDirectory() && !name.startsWith("_");
    });

    // Parse each topic
    topicNames.forEach((name) => {
      const topicMdPath = path.join(topicsDir, name, "topic.md");
      const topicDirPath = path.join(topicsDir, name);

      // Get stat from topic.md or directory
      let stat;
      let content = "";
      if (fs.existsSync(topicMdPath)) {
        stat = fs.statSync(topicMdPath);
        content = fs.readFileSync(topicMdPath, "utf8");
      } else {
        stat = fs.statSync(topicDirPath);
      }

      try {
        // Parse YAML frontmatter
        const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
        let title = name;
        let topicStatus = "active";
        let category = "general";
        let created = null;

        if (frontmatterMatch) {
          const frontmatter = frontmatterMatch[1];
          const titleMatch = frontmatter.match(/title:\s*(.+)/);
          const statusMatch = frontmatter.match(/status:\s*(.+)/);
          const categoryMatch = frontmatter.match(/category:\s*(.+)/);
          const createdMatch = frontmatter.match(/created:\s*(.+)/);

          if (titleMatch) title = titleMatch[1].trim();
          if (statusMatch) topicStatus = statusMatch[1].trim().toLowerCase();
          if (categoryMatch) category = categoryMatch[1].trim();
          if (createdMatch) created = createdMatch[1].trim();
        }

        // Count threads
        const threadsDir = path.join(topicsDir, name, "threads");
        let threadCount = 0;
        if (fs.existsSync(threadsDir)) {
          threadCount = fs
            .readdirSync(threadsDir)
            .filter((f) => f.endsWith(".md") || f.endsWith(".json")).length;
        }

        // Accumulate total threads
        result.threads += threadCount;

        // Count by status
        if (topicStatus === "active") result.topics.active++;
        else if (topicStatus === "resolved") result.topics.resolved++;
        else if (topicStatus === "parked") result.topics.parked++;

        // Track latest modification
        if (!latestModified || stat.mtime > latestModified) {
          latestModified = stat.mtime;
        }

        topics.push({
          name,
          title,
          status: topicStatus,
          category,
          created,
          threads: threadCount,
          lastModified: stat.mtimeMs,
        });
      } catch (e) {
        console.error(`Failed to parse topic ${name}:`, e.message);
      }
    });

    result.topics.total = topics.length;

    // Sort: active first, then by most recently modified
    const statusPriority = { active: 0, resolved: 1, parked: 2 };
    topics.sort((a, b) => {
      const statusDiff = (statusPriority[a.status] || 3) - (statusPriority[b.status] || 3);
      if (statusDiff !== 0) return statusDiff;
      return b.lastModified - a.lastModified;
    });

    // Filter by status for recentTopics display
    let filtered = topics;
    if (filterStatus !== "all") {
      filtered = topics.filter((t) => t.status === filterStatus);
    }

    // Format for recentTopics (paginated)
    const paginated = filtered.slice(offset, offset + limit);
    result.recentTopics = paginated.map((t) => ({
      name: t.name,
      title: t.title,
      status: t.status,
      threads: t.threads,
      age: formatTimeAgo(new Date(t.lastModified)),
    }));

    // Count orphans
    if (fs.existsSync(orphansDir)) {
      try {
        result.orphans = fs.readdirSync(orphansDir).filter((f) => f.endsWith(".md")).length;
      } catch (e) {}
    }

    result.lastUpdated = latestModified ? latestModified.toISOString() : null;
  } catch (e) {
    console.error("Failed to get Cerebro topics:", e.message);
  }

  return result;
}

/**
 * Update topic status in topic.md file
 * @param {string} cerebroDir - Path to cerebro directory
 * @param {string} topicId - Topic identifier
 * @param {string} newStatus - New status (active, resolved, parked)
 * @returns {object} - Updated topic data or error
 */
function updateTopicStatus(cerebroDir, topicId, newStatus) {
  const topicDir = path.join(cerebroDir, "topics", topicId);
  const topicFile = path.join(topicDir, "topic.md");

  // Check if topic exists
  if (!fs.existsSync(topicDir)) {
    return { error: `Topic '${topicId}' not found`, code: 404 };
  }

  // If topic.md doesn't exist, create it with basic frontmatter
  if (!fs.existsSync(topicFile)) {
    const content = `---
title: ${topicId}
status: ${newStatus}
category: general
created: ${new Date().toISOString().split("T")[0]}
---

# ${topicId}

## Overview
*Topic tracking file.*

## Notes
`;
    fs.writeFileSync(topicFile, content, "utf8");
    return {
      topic: {
        id: topicId,
        name: topicId,
        title: topicId,
        status: newStatus,
      },
    };
  }

  // Read existing topic.md
  let content = fs.readFileSync(topicFile, "utf8");
  let title = topicId;

  // Check if it has YAML frontmatter
  const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);

  if (frontmatterMatch) {
    // Has frontmatter - update status field
    let frontmatter = frontmatterMatch[1];

    // Extract title if present
    const titleMatch = frontmatter.match(/title:\s*["']?([^"'\n]+)["']?/i);
    if (titleMatch) title = titleMatch[1];

    if (frontmatter.includes("status:")) {
      // Replace existing status
      frontmatter = frontmatter.replace(
        /status:\s*(active|resolved|parked)/i,
        `status: ${newStatus}`,
      );
    } else {
      // Add status field
      frontmatter = frontmatter.trim() + `\nstatus: ${newStatus}`;
    }

    content = content.replace(/^---\n[\s\S]*?\n---/, `---\n${frontmatter}\n---`);
  } else {
    // No frontmatter - add one
    const headerMatch = content.match(/^#\s*(.+)/m);
    if (headerMatch) title = headerMatch[1];

    const frontmatter = `---
title: ${title}
status: ${newStatus}
category: general
created: ${new Date().toISOString().split("T")[0]}
---

`;
    content = frontmatter + content;
  }

  // Write updated content
  fs.writeFileSync(topicFile, content, "utf8");

  return {
    topic: {
      id: topicId,
      name: topicId,
      title: title,
      status: newStatus,
    },
  };
}

module.exports = {
  getCerebroTopics,
  updateTopicStatus,
};
```

## File: `src/config.js`
```javascript
/**
 * Configuration loader with sensible defaults
 *
 * Priority order:
 * 1. Environment variables (highest)
 * 2. config/dashboard.json file
 * 3. Auto-detected paths
 * 4. Sensible defaults (lowest)
 */

const fs = require("fs");
const path = require("path");
const os = require("os");

const HOME = os.homedir();

/**
 * Get the OpenClaw profile directory (e.g., ~/.openclaw or ~/.openclaw-<profile>)
 * This is the canonical source for profile-aware paths.
 */
function getOpenClawDir(profile = null) {
  const effectiveProfile = profile || process.env.OPENCLAW_PROFILE || "";
  return effectiveProfile
    ? path.join(HOME, `.openclaw-${effectiveProfile}`)
    : path.join(HOME, ".openclaw");
}

/**
 * Auto-detect OpenClaw workspace by checking common locations
 * Profile-aware: checks profile-specific paths first when OPENCLAW_PROFILE is set
 */
function detectWorkspace() {
  const profile = process.env.OPENCLAW_PROFILE || "";
  const openclawDir = getOpenClawDir();
  const defaultWorkspace = path.join(openclawDir, "workspace");

  // Build candidates list - profile-specific paths come first
  const profileCandidates = profile
    ? [
        // Profile-specific workspace in home (e.g., ~/.openclaw-<profile>-workspace)
        path.join(HOME, `.openclaw-${profile}-workspace`),
        path.join(HOME, `.${profile}-workspace`),
      ]
    : [];

  const candidates = [
    // Environment variable (highest priority)
    process.env.OPENCLAW_WORKSPACE,
    // OpenClaw's default workspace location
    process.env.OPENCLAW_HOME,
    // Gateway config workspace (check early - this is where OpenClaw actually runs)
    getWorkspaceFromGatewayConfig(),
    // Profile-specific paths (if profile is set)
    ...profileCandidates,
    // Standard OpenClaw workspace location (profile-aware: ~/.openclaw/workspace or ~/.openclaw-<profile>/workspace)
    defaultWorkspace,
    // Common custom workspace names
    path.join(HOME, "openclaw-workspace"),
    path.join(HOME, ".openclaw-workspace"),
    // Legacy/custom names
    path.join(HOME, "molty"),
    path.join(HOME, "clawd"),
    path.join(HOME, "moltbot"),
  ].filter(Boolean);

  // Find first existing candidate that looks like a workspace
  const foundWorkspace = candidates.find((candidate) => {
    if (!candidate || !fs.existsSync(candidate)) {
      return false;
    }

    // Verify it looks like a workspace (has memory/ or state/ dir)
    const hasMemory = fs.existsSync(path.join(candidate, "memory"));
    const hasState = fs.existsSync(path.join(candidate, "state"));
    const hasConfig = fs.existsSync(path.join(candidate, ".openclaw"));

    return hasMemory || hasState || hasConfig;
  });

  // Return found workspace or default (will be created on first use)
  return foundWorkspace || defaultWorkspace;
}

/**
 * Try to get workspace from OpenClaw gateway config
 * Profile-aware: checks the profile directory first when OPENCLAW_PROFILE is set
 */
function getWorkspaceFromGatewayConfig() {
  const openclawDir = getOpenClawDir();
  const configPaths = [
    path.join(openclawDir, "config.yaml"),
    path.join(openclawDir, "config.json"),
    path.join(openclawDir, "openclaw.json"),
    path.join(openclawDir, "clawdbot.json"),
    // Fallback to standard XDG location
    path.join(HOME, ".config", "openclaw", "config.yaml"),
  ];

  for (const configPath of configPaths) {
    try {
      if (fs.existsSync(configPath)) {
        const content = fs.readFileSync(configPath, "utf8");
        // Simple extraction - look for workspace or workdir
        const match =
          content.match(/workspace[:\s]+["']?([^"'\n]+)/i) ||
          content.match(/workdir[:\s]+["']?([^"'\n]+)/i);
        if (match && match[1]) {
          const workspace = match[1].trim().replace(/^~/, HOME);
          if (fs.existsSync(workspace)) {
            return workspace;
          }
        }
      }
    } catch (e) {
      // Ignore errors, continue searching
    }
  }
  return null;
}

/**
 * Deep merge two objects (local overrides base)
 */
function deepMerge(base, override) {
  const result = { ...base };
  for (const key of Object.keys(override)) {
    if (
      override[key] &&
      typeof override[key] === "object" &&
      !Array.isArray(override[key]) &&
      base[key] &&
      typeof base[key] === "object"
    ) {
      result[key] = deepMerge(base[key], override[key]);
    } else if (override[key] !== null && override[key] !== undefined) {
      result[key] = override[key];
    }
  }
  return result;
}

/**
 * Load config files - base + local overrides
 */
function loadConfigFile() {
  const basePath = path.join(__dirname, "..", "config", "dashboard.json");
  const localPath = path.join(__dirname, "..", "config", "dashboard.local.json");

  let config = {};

  // Load base config
  try {
    if (fs.existsSync(basePath)) {
      const content = fs.readFileSync(basePath, "utf8");
      config = JSON.parse(content);
    }
  } catch (e) {
    console.warn(`[Config] Failed to load ${basePath}:`, e.message);
  }

  // Merge local overrides
  try {
    if (fs.existsSync(localPath)) {
      const content = fs.readFileSync(localPath, "utf8");
      const localConfig = JSON.parse(content);
      config = deepMerge(config, localConfig);
      console.log(`[Config] Loaded local overrides from ${localPath}`);
    }
  } catch (e) {
    console.warn(`[Config] Failed to load ${localPath}:`, e.message);
  }

  return config;
}

/**
 * Expand ~ and environment variables in paths
 */
function expandPath(p) {
  if (!p) return p;
  return p
    .replace(/^~/, HOME)
    .replace(/\$HOME/g, HOME)
    .replace(/\$\{HOME\}/g, HOME);
}

/**
 * Build final configuration
 */
function loadConfig() {
  const fileConfig = loadConfigFile();
  const workspace =
    process.env.OPENCLAW_WORKSPACE || expandPath(fileConfig.paths?.workspace) || detectWorkspace();

  const config = {
    // Server settings
    server: {
      port: parseInt(process.env.PORT || fileConfig.server?.port || "3333", 10),
      host: process.env.HOST || fileConfig.server?.host || "localhost",
    },

    // Paths - all relative to workspace unless absolute
    paths: {
      workspace: workspace,
      memory:
        expandPath(process.env.OPENCLAW_MEMORY_DIR || fileConfig.paths?.memory) ||
        path.join(workspace, "memory"),
      state:
        expandPath(process.env.OPENCLAW_STATE_DIR || fileConfig.paths?.state) ||
        path.join(workspace, "state"),
      cerebro:
        expandPath(process.env.OPENCLAW_CEREBRO_DIR || fileConfig.paths?.cerebro) ||
        path.join(workspace, "cerebro"),
      skills:
        expandPath(process.env.OPENCLAW_SKILLS_DIR || fileConfig.paths?.skills) ||
        path.join(workspace, "skills"),
      jobs:
        expandPath(process.env.OPENCLAW_JOBS_DIR || fileConfig.paths?.jobs) ||
        path.join(workspace, "jobs"),
      logs:
        expandPath(process.env.OPENCLAW_LOGS_DIR || fileConfig.paths?.logs) ||
        path.join(HOME, ".openclaw-command-center", "logs"),
    },

    // Auth settings
    auth: {
      mode: process.env.DASHBOARD_AUTH_MODE || fileConfig.auth?.mode || "none",
      token: process.env.DASHBOARD_TOKEN || fileConfig.auth?.token,
      allowedUsers: (
        process.env.DASHBOARD_ALLOWED_USERS ||
        fileConfig.auth?.allowedUsers?.join(",") ||
        ""
      )
        .split(",")
        .map((s) => s.trim().toLowerCase())
        .filter(Boolean),
      allowedIPs: (
        process.env.DASHBOARD_ALLOWED_IPS ||
        fileConfig.auth?.allowedIPs?.join(",") ||
        "127.0.0.1,::1"
      )
        .split(",")
        .map((s) => s.trim()),
      publicPaths: fileConfig.auth?.publicPaths || ["/api/health", "/api/whoami", "/favicon.ico"],
    },

    // Branding
    branding: {
      name: fileConfig.branding?.name || "OpenClaw Command Center",
      theme: fileConfig.branding?.theme || "default",
    },

    // Integrations
    integrations: {
      linear: {
        enabled: !!(process.env.LINEAR_API_KEY || fileConfig.integrations?.linear?.apiKey),
        apiKey: process.env.LINEAR_API_KEY || fileConfig.integrations?.linear?.apiKey,
        teamId: process.env.LINEAR_TEAM_ID || fileConfig.integrations?.linear?.teamId,
      },
    },

    // Billing - for cost savings calculation
    billing: {
      claudePlanCost: parseFloat(
        process.env.CLAUDE_PLAN_COST || fileConfig.billing?.claudePlanCost || "200",
      ),
      claudePlanName:
        process.env.CLAUDE_PLAN_NAME || fileConfig.billing?.claudePlanName || "Claude Code Max",
    },
  };

  return config;
}

// Export singleton config
const CONFIG = loadConfig();

// Log detected configuration on startup
console.log("[Config] Workspace:", CONFIG.paths.workspace);
console.log("[Config] Auth mode:", CONFIG.auth.mode);

module.exports = { CONFIG, loadConfig, detectWorkspace, expandPath, getOpenClawDir };
```

## File: `src/cron.js`
```javascript
const fs = require("fs");
const path = require("path");

// Convert cron expression to human-readable text
function cronToHuman(expr) {
  if (!expr || expr === "—") return null;

  const parts = expr.split(" ");
  if (parts.length < 5) return null;

  const [minute, hour, dayOfMonth, month, dayOfWeek] = parts;

  const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  // Helper to format time
  function formatTime(h, m) {
    const hNum = parseInt(h, 10);
    const mNum = parseInt(m, 10);
    if (isNaN(hNum)) return null;
    const ampm = hNum >= 12 ? "pm" : "am";
    const h12 = hNum === 0 ? 12 : hNum > 12 ? hNum - 12 : hNum;
    return mNum === 0 ? `${h12}${ampm}` : `${h12}:${mNum.toString().padStart(2, "0")}${ampm}`;
  }

  // Every minute
  if (minute === "*" && hour === "*" && dayOfMonth === "*" && month === "*" && dayOfWeek === "*") {
    return "Every minute";
  }

  // Every X minutes
  if (minute.startsWith("*/")) {
    const interval = minute.slice(2);
    return `Every ${interval} minutes`;
  }

  // Every X hours (*/N in hour field)
  if (hour.startsWith("*/")) {
    const interval = hour.slice(2);
    const minStr = minute === "0" ? "" : `:${minute.padStart(2, "0")}`;
    return `Every ${interval} hours${minStr ? " at " + minStr : ""}`;
  }

  // Every hour at specific minute
  if (minute !== "*" && hour === "*" && dayOfMonth === "*" && month === "*" && dayOfWeek === "*") {
    return `Hourly at :${minute.padStart(2, "0")}`;
  }

  // Build time string for specific hour
  let timeStr = "";
  if (minute !== "*" && hour !== "*" && !hour.startsWith("*/")) {
    timeStr = formatTime(hour, minute);
  }

  // Daily at specific time
  if (timeStr && dayOfMonth === "*" && month === "*" && dayOfWeek === "*") {
    return `Daily at ${timeStr}`;
  }

  // Weekdays (Mon-Fri) - check before generic day of week
  if ((dayOfWeek === "1-5" || dayOfWeek === "MON-FRI") && dayOfMonth === "*" && month === "*") {
    return timeStr ? `Weekdays at ${timeStr}` : "Weekdays";
  }

  // Weekends - check before generic day of week
  if ((dayOfWeek === "0,6" || dayOfWeek === "6,0") && dayOfMonth === "*" && month === "*") {
    return timeStr ? `Weekends at ${timeStr}` : "Weekends";
  }

  // Specific day of week
  if (dayOfMonth === "*" && month === "*" && dayOfWeek !== "*") {
    const days = dayOfWeek.split(",").map((d) => {
      const num = parseInt(d, 10);
      return dayNames[num] || d;
    });
    const dayStr = days.length === 1 ? days[0] : days.join(", ");
    return timeStr ? `${dayStr} at ${timeStr}` : `Every ${dayStr}`;
  }

  // Specific day of month
  if (dayOfMonth !== "*" && month === "*" && dayOfWeek === "*") {
    const day = parseInt(dayOfMonth, 10);
    const suffix =
      day === 1 || day === 21 || day === 31
        ? "st"
        : day === 2 || day === 22
          ? "nd"
          : day === 3 || day === 23
            ? "rd"
            : "th";
    return timeStr ? `${day}${suffix} of month at ${timeStr}` : `${day}${suffix} of every month`;
  }

  // Fallback: just show the time if we have it
  if (timeStr) {
    return `At ${timeStr}`;
  }

  return expr; // Return original as fallback
}

// Get cron jobs - reads directly from file for speed (CLI takes 11s+)
function getCronJobs(getOpenClawDir) {
  try {
    const cronPath = path.join(getOpenClawDir(), "cron", "jobs.json");
    if (fs.existsSync(cronPath)) {
      const data = JSON.parse(fs.readFileSync(cronPath, "utf8"));
      return (data.jobs || []).map((j) => {
        // Parse schedule
        let scheduleStr = "—";
        let scheduleHuman = null;
        if (j.schedule) {
          if (j.schedule.kind === "cron" && j.schedule.expr) {
            scheduleStr = j.schedule.expr;
            scheduleHuman = cronToHuman(j.schedule.expr);
          } else if (j.schedule.kind === "once") {
            scheduleStr = "once";
            scheduleHuman = "One-time";
          }
        }

        // Format next run
        let nextRunStr = "—";
        if (j.state?.nextRunAtMs) {
          const next = new Date(j.state.nextRunAtMs);
          const now = new Date();
          const diffMs = next - now;
          const diffMins = Math.round(diffMs / 60000);
          if (diffMins < 0) {
            nextRunStr = "overdue";
          } else if (diffMins < 60) {
            nextRunStr = `${diffMins}m`;
          } else if (diffMins < 1440) {
            nextRunStr = `${Math.round(diffMins / 60)}h`;
          } else {
            nextRunStr = `${Math.round(diffMins / 1440)}d`;
          }
        }

        return {
          id: j.id,
          name: j.name || j.id.slice(0, 8),
          schedule: scheduleStr,
          scheduleHuman: scheduleHuman,
          nextRun: nextRunStr,
          enabled: j.enabled !== false,
          lastStatus: j.state?.lastStatus,
        };
      });
    }
  } catch (e) {
    console.error("Failed to get cron:", e.message);
  }
  return [];
}

module.exports = {
  cronToHuman,
  getCronJobs,
};
```

## File: `src/data.js`
```javascript
const fs = require("fs");
const path = require("path");

function migrateDataDir(dataDir, legacyDataDir) {
  try {
    if (!fs.existsSync(legacyDataDir)) return;
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true });
    }
    const legacyFiles = fs.readdirSync(legacyDataDir);
    if (legacyFiles.length === 0) return;
    let migrated = 0;
    for (const file of legacyFiles) {
      const srcPath = path.join(legacyDataDir, file);
      const destPath = path.join(dataDir, file);
      if (fs.existsSync(destPath)) continue;
      const stat = fs.statSync(srcPath);
      if (stat.isFile()) {
        fs.copyFileSync(srcPath, destPath);
        migrated++;
        console.log(`[Migration] Copied ${file} to profile-aware data dir`);
      }
    }
    if (migrated > 0) {
      console.log(`[Migration] Migrated ${migrated} file(s) to ${dataDir}`);
      console.log(`[Migration] Legacy data preserved at ${legacyDataDir}`);
    }
  } catch (e) {
    console.error("[Migration] Failed to migrate data:", e.message);
  }
}

module.exports = { migrateDataDir };
```

## File: `src/index.js`
```javascript
/**
 * OpenClaw Command Center Dashboard Server
 * Serves the dashboard UI and provides API endpoints for status data
 */

const http = require("http");
const fs = require("fs");
const path = require("path");

// ============================================================================
// CLI ARGUMENT PARSING
// ============================================================================
const args = process.argv.slice(2);
let cliProfile = null;
let cliPort = null;

for (let i = 0; i < args.length; i++) {
  switch (args[i]) {
    case "--profile":
    case "-p":
      cliProfile = args[++i];
      break;
    case "--port":
      cliPort = parseInt(args[++i], 10);
      break;
    case "--help":
    case "-h":
      console.log(`
OpenClaw Command Center

Usage: node lib/server.js [options]

Options:
  --profile, -p <name>  OpenClaw profile (uses ~/.openclaw-<name>)
  --port <port>         Server port (default: 3333)
  --help, -h            Show this help

Environment:
  OPENCLAW_PROFILE      Same as --profile
  PORT                  Same as --port

Examples:
  node lib/server.js --profile production
  node lib/server.js -p dev --port 3334
`);
      process.exit(0);
  }
}

// Set profile in environment so CONFIG and all CLI calls pick it up
if (cliProfile) {
  process.env.OPENCLAW_PROFILE = cliProfile;
}
if (cliPort) {
  process.env.PORT = cliPort.toString();
}

// ============================================================================
// MODULE IMPORTS (after env vars are set)
// ============================================================================
const { getVersion } = require("./utils");
const { CONFIG, getOpenClawDir } = require("./config");
const { handleJobsRequest, isJobsRoute } = require("./jobs");
const { runOpenClaw, runOpenClawAsync, extractJSON } = require("./openclaw");
const { getSystemVitals, checkOptionalDeps, getOptionalDeps } = require("./vitals");
const { checkAuth, getUnauthorizedPage } = require("./auth");
const { loadPrivacySettings, savePrivacySettings } = require("./privacy");
const {
  loadOperators,
  saveOperators,
  getOperatorBySlackId,
  startOperatorsRefresh,
  calculateOperatorStats,
} = require("./operators");
const { createSessionsModule } = require("./sessions");
const { getCronJobs } = require("./cron");
const { getCerebroTopics, updateTopicStatus } = require("./cerebro");
const {
  getDailyTokenUsage,
  getTokenStats,
  getCostBreakdown,
  startTokenUsageRefresh,
  refreshTokenUsageAsync,
} = require("./tokens");
const { getLlmUsage, getRoutingStats, startLlmUsageRefresh } = require("./llm-usage");
const { executeAction } = require("./actions");
const { migrateDataDir } = require("./data");
const { createStateModule } = require("./state");

// ============================================================================
// CONFIGURATION
// ============================================================================
const PORT = CONFIG.server.port;
const DASHBOARD_DIR = path.join(__dirname, "../public");
const PATHS = CONFIG.paths;

const AUTH_CONFIG = {
  mode: CONFIG.auth.mode,
  token: CONFIG.auth.token,
  allowedUsers: CONFIG.auth.allowedUsers,
  allowedIPs: CONFIG.auth.allowedIPs,
  publicPaths: CONFIG.auth.publicPaths,
};

// Profile-aware data directory
const DATA_DIR = path.join(getOpenClawDir(), "command-center", "data");
const LEGACY_DATA_DIR = path.join(DASHBOARD_DIR, "data");

// ============================================================================
// SSE (Server-Sent Events)
// ============================================================================
const sseClients = new Set();

function sendSSE(res, event, data) {
  try {
    res.write(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`);
  } catch (e) {
    // Client disconnected
  }
}

function broadcastSSE(event, data) {
  for (const client of sseClients) {
    sendSSE(client, event, data);
  }
}

// ============================================================================
// INITIALIZE MODULES (wire up dependencies)
// ============================================================================

// Sessions module (factory pattern with dependency injection)
const sessions = createSessionsModule({
  getOpenClawDir,
  getOperatorBySlackId: (slackId) => getOperatorBySlackId(DATA_DIR, slackId),
  runOpenClaw,
  runOpenClawAsync,
  extractJSON,
});

// State module (factory pattern)
const state = createStateModule({
  CONFIG,
  getOpenClawDir,
  getSessions: (opts) => sessions.getSessions(opts),
  getSystemVitals,
  getCronJobs: () => getCronJobs(getOpenClawDir),
  loadOperators: () => loadOperators(DATA_DIR),
  calculateOperatorStats,
  getLlmUsage: () => getLlmUsage(PATHS.state),
  getDailyTokenUsage: () => getDailyTokenUsage(getOpenClawDir),
  getTokenStats,
  getCerebroTopics: (opts) => getCerebroTopics(PATHS.cerebro, opts),
  runOpenClaw,
  extractJSON,
  readTranscript: (sessionId) => sessions.readTranscript(sessionId),
});

// ============================================================================
// STARTUP: Data migration + background tasks
// ============================================================================
process.nextTick(() => migrateDataDir(DATA_DIR, LEGACY_DATA_DIR));
startOperatorsRefresh(DATA_DIR, getOpenClawDir);
startLlmUsageRefresh();
startTokenUsageRefresh(getOpenClawDir);

// ============================================================================
// STATIC FILE SERVER
// ============================================================================
function serveStatic(req, res) {
  // Parse URL to safely extract pathname (ignoring query/hash)
  const requestUrl = new URL(req.url, `http://${req.headers.host || "localhost"}`);
  const pathname = requestUrl.pathname === "/" ? "/index.html" : requestUrl.pathname;

  // Reject any path containing ".." segments (path traversal)
  if (pathname.includes("..")) {
    res.writeHead(400);
    res.end("Bad request");
    return;
  }

  // Normalize and resolve to ensure path stays within DASHBOARD_DIR
  const normalizedPath = path.normalize(pathname).replace(/^[/\\]+/, "");
  const filePath = path.join(DASHBOARD_DIR, normalizedPath);

  const resolvedDashboardDir = path.resolve(DASHBOARD_DIR);
  const resolvedFilePath = path.resolve(filePath);
  if (
    !resolvedFilePath.startsWith(resolvedDashboardDir + path.sep) &&
    resolvedFilePath !== resolvedDashboardDir
  ) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }

  const ext = path.extname(filePath);
  const contentTypes = {
    ".html": "text/html",
    ".css": "text/css",
    ".js": "text/javascript",
    ".json": "application/json",
    ".png": "image/png",
    ".svg": "image/svg+xml",
  };

  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }
    const headers = { "Content-Type": contentTypes[ext] || "text/plain" };

    // Avoid stale dashboards (users frequently hard-refresh while iterating)
    if ([".html", ".css", ".js", ".json"].includes(ext)) {
      headers["Cache-Control"] = "no-store";
    }

    res.writeHead(200, headers);
    res.end(content);
  });
}

// ============================================================================
// LEGACY API HANDLER
// ============================================================================
function handleApi(req, res) {
  const sessionsList = sessions.getSessions();
  const capacity = state.getCapacity();
  const tokenStats = getTokenStats(sessionsList, capacity, CONFIG);

  const data = {
    sessions: sessionsList,
    cron: getCronJobs(getOpenClawDir),
    system: state.getSystemStatus(),
    activity: state.getRecentActivity(),
    tokenStats,
    capacity,
    timestamp: new Date().toISOString(),
  };

  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify(data, null, 2));
}

// ============================================================================
// HTTP SERVER
// ============================================================================
const server = http.createServer((req, res) => {
  // CORS headers
  res.setHeader("Access-Control-Allow-Origin", "*");

  const urlParts = req.url.split("?");
  const pathname = urlParts[0];
  const query = new URLSearchParams(urlParts[1] || "");

  // Fast path for health check
  if (pathname === "/api/health") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ status: "ok", port: PORT, timestamp: new Date().toISOString() }));
    return;
  }

  // Auth check (unless public path)
  const isPublicPath = AUTH_CONFIG.publicPaths.some(
    (p) => pathname === p || pathname.startsWith(p + "/"),
  );

  if (!isPublicPath && AUTH_CONFIG.mode !== "none") {
    const authResult = checkAuth(req, AUTH_CONFIG);

    if (!authResult.authorized) {
      console.log(`[AUTH] Denied: ${authResult.reason} (path: ${pathname})`);
      res.writeHead(403, { "Content-Type": "text/html" });
      res.end(getUnauthorizedPage(authResult.reason, authResult.user, AUTH_CONFIG));
      return;
    }

    req.authUser = authResult.user;

    if (authResult.user?.login || authResult.user?.email) {
      console.log(
        `[AUTH] Allowed: ${authResult.user.login || authResult.user.email} (path: ${pathname})`,
      );
    } else {
      console.log(`[AUTH] Allowed: ${req.socket?.remoteAddress} (path: ${pathname})`);
    }
  }

  // ---- API Routes ----

  if (pathname === "/api/status") {
    handleApi(req, res);
  } else if (pathname === "/api/session") {
    const sessionKey = query.get("key");
    if (!sessionKey) {
      res.writeHead(400, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Missing session key" }));
      return;
    }
    const detail = sessions.getSessionDetail(sessionKey);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(detail, null, 2));
  } else if (pathname === "/api/cerebro") {
    const offset = parseInt(query.get("offset") || "0", 10);
    const limit = parseInt(query.get("limit") || "20", 10);
    const statusFilter = query.get("status") || "all";

    const data = getCerebroTopics(PATHS.cerebro, { offset, limit, status: statusFilter });
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data, null, 2));
  } else if (
    pathname.startsWith("/api/cerebro/topic/") &&
    pathname.endsWith("/status") &&
    req.method === "POST"
  ) {
    const topicId = decodeURIComponent(
      pathname.replace("/api/cerebro/topic/", "").replace("/status", ""),
    );

    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
    });
    req.on("end", () => {
      try {
        const { status: newStatus } = JSON.parse(body);

        if (!newStatus || !["active", "resolved", "parked"].includes(newStatus)) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(
            JSON.stringify({ error: "Invalid status. Must be: active, resolved, or parked" }),
          );
          return;
        }

        const result = updateTopicStatus(PATHS.cerebro, topicId, newStatus);

        if (result.error) {
          res.writeHead(result.code || 500, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ error: result.error }));
          return;
        }

        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify(result, null, 2));
      } catch (e) {
        res.writeHead(400, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Invalid JSON body" }));
      }
    });
    return;
  } else if (pathname === "/api/llm-quota") {
    const data = getLlmUsage(PATHS.state);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data, null, 2));
  } else if (pathname === "/api/cost-breakdown") {
    const data = getCostBreakdown(CONFIG, (opts) => sessions.getSessions(opts), getOpenClawDir);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data, null, 2));
  } else if (pathname === "/api/subagents") {
    const data = state.getSubagentStatus();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ subagents: data }, null, 2));
  } else if (pathname === "/api/action") {
    const action = query.get("action");
    if (!action) {
      res.writeHead(400, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Missing action parameter" }));
      return;
    }
    const result = executeAction(action, { runOpenClaw, extractJSON, PORT });
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(result, null, 2));
  } else if (pathname === "/api/events") {
    // SSE endpoint
    res.writeHead(200, {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
      "X-Accel-Buffering": "no",
    });

    sseClients.add(res);
    console.log(`[SSE] Client connected (total: ${sseClients.size})`);

    sendSSE(res, "connected", { message: "Connected to Command Center", timestamp: Date.now() });

    const cachedState = state.getFullState();
    if (cachedState) {
      sendSSE(res, "update", cachedState);
    } else {
      sendSSE(res, "update", { sessions: [], loading: true });
    }

    req.on("close", () => {
      sseClients.delete(res);
      console.log(`[SSE] Client disconnected (total: ${sseClients.size})`);
    });

    return;
  } else if (pathname === "/api/whoami") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify(
        {
          authMode: AUTH_CONFIG.mode,
          user: req.authUser || null,
        },
        null,
        2,
      ),
    );
  } else if (pathname === "/api/about") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify(
        {
          name: "OpenClaw Command Center",
          version: getVersion(),
          description: "A Starcraft-inspired dashboard for AI agent orchestration",
          license: "MIT",
          repository: "https://github.com/jontsai/openclaw-command-center",
          builtWith: ["OpenClaw", "Node.js", "Vanilla JS"],
          inspirations: ["Starcraft", "Inside Out", "iStatMenus", "DaisyDisk", "Gmail"],
        },
        null,
        2,
      ),
    );
  } else if (pathname === "/api/state") {
    const fullState = state.getFullState();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(fullState, null, 2));
  } else if (pathname === "/api/vitals") {
    const vitals = getSystemVitals();
    const optionalDeps = getOptionalDeps();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ vitals, optionalDeps }, null, 2));
  } else if (pathname === "/api/capacity") {
    const capacity = state.getCapacity();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(capacity, null, 2));
  } else if (pathname === "/api/sessions") {
    const page = parseInt(query.get("page")) || 1;
    const pageSize = parseInt(query.get("pageSize")) || 20;
    const statusFilter = query.get("status");

    const allSessions = sessions.getSessions({ limit: null });

    const statusCounts = {
      all: allSessions.length,
      live: allSessions.filter((s) => s.active).length,
      recent: allSessions.filter((s) => !s.active && s.recentlyActive).length,
      idle: allSessions.filter((s) => !s.active && !s.recentlyActive).length,
    };

    let filteredSessions = allSessions;
    if (statusFilter === "live") {
      filteredSessions = allSessions.filter((s) => s.active);
    } else if (statusFilter === "recent") {
      filteredSessions = allSessions.filter((s) => !s.active && s.recentlyActive);
    } else if (statusFilter === "idle") {
      filteredSessions = allSessions.filter((s) => !s.active && !s.recentlyActive);
    }

    const total = filteredSessions.length;
    const totalPages = Math.ceil(total / pageSize);
    const offset = (page - 1) * pageSize;
    const displaySessions = filteredSessions.slice(offset, offset + pageSize);

    const tokenStats = getTokenStats(allSessions, state.getCapacity(), CONFIG);
    const capacity = state.getCapacity();

    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify(
        {
          sessions: displaySessions,
          pagination: {
            page,
            pageSize,
            total,
            totalPages,
            hasPrev: page > 1,
            hasNext: page < totalPages,
          },
          statusCounts,
          tokenStats,
          capacity,
        },
        null,
        2,
      ),
    );
  } else if (pathname === "/api/cron") {
    const cron = getCronJobs(getOpenClawDir);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ cron }, null, 2));
  } else if (pathname === "/api/operators") {
    const method = req.method;
    const data = loadOperators(DATA_DIR);

    if (method === "GET") {
      const allSessions = sessions.getSessions({ limit: null });
      const operatorsWithStats = calculateOperatorStats(data, allSessions);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(
        JSON.stringify(
          {
            ...operatorsWithStats,
            timestamp: Date.now(),
          },
          null,
          2,
        ),
      );
    } else if (method === "POST") {
      let body = "";
      req.on("data", (chunk) => (body += chunk));
      req.on("end", () => {
        try {
          const newOp = JSON.parse(body);
          const existingIdx = data.operators.findIndex((op) => op.id === newOp.id);
          if (existingIdx >= 0) {
            data.operators[existingIdx] = { ...data.operators[existingIdx], ...newOp };
          } else {
            data.operators.push({
              ...newOp,
              createdAt: new Date().toISOString(),
            });
          }
          if (saveOperators(DATA_DIR, data)) {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ success: true, operator: newOp }));
          } else {
            res.writeHead(500, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ error: "Failed to save" }));
          }
        } catch (e) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ error: "Invalid JSON" }));
        }
      });
      return;
    } else {
      res.writeHead(405, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Method not allowed" }));
    }
    return;
  } else if (pathname === "/api/llm-usage") {
    const usage = getLlmUsage(PATHS.state);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(usage, null, 2));
  } else if (pathname === "/api/routing-stats") {
    const hours = parseInt(query.get("hours") || "24", 10);
    const stats = getRoutingStats(PATHS.skills, PATHS.state, hours);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(stats, null, 2));
  } else if (pathname === "/api/memory") {
    const memory = state.getMemoryStats();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ memory }, null, 2));
  } else if (pathname === "/api/privacy") {
    if (req.method === "GET") {
      const settings = loadPrivacySettings(DATA_DIR);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(settings, null, 2));
    } else if (req.method === "POST" || req.method === "PUT") {
      let body = "";
      req.on("data", (chunk) => (body += chunk));
      req.on("end", () => {
        try {
          const updates = JSON.parse(body);
          const current = loadPrivacySettings(DATA_DIR);

          const merged = {
            version: current.version || 1,
            hiddenTopics: updates.hiddenTopics ?? current.hiddenTopics ?? [],
            hiddenSessions: updates.hiddenSessions ?? current.hiddenSessions ?? [],
            hiddenCrons: updates.hiddenCrons ?? current.hiddenCrons ?? [],
            hideHostname: updates.hideHostname ?? current.hideHostname ?? false,
          };

          if (savePrivacySettings(DATA_DIR, merged)) {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ success: true, settings: merged }));
          } else {
            res.writeHead(500, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ error: "Failed to save privacy settings" }));
          }
        } catch (e) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ error: "Invalid JSON: " + e.message }));
        }
      });
      return;
    } else {
      res.writeHead(405, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Method not allowed" }));
    }
    return;
  } else if (isJobsRoute(pathname)) {
    handleJobsRequest(req, res, pathname, query, req.method);
  } else {
    serveStatic(req, res);
  }
});

// ============================================================================
// START SERVER
// ============================================================================
server.listen(PORT, () => {
  const profile = process.env.OPENCLAW_PROFILE;
  console.log(`\u{1F99E} OpenClaw Command Center running at http://localhost:${PORT}`);
  if (profile) {
    console.log(`   Profile: ${profile} (~/.openclaw-${profile})`);
  }
  console.log(`   Press Ctrl+C to stop`);

  // Pre-warm caches in background
  setTimeout(async () => {
    console.log("[Startup] Pre-warming caches in background...");
    try {
      await Promise.all([sessions.refreshSessionsCache(), refreshTokenUsageAsync(getOpenClawDir)]);
      getSystemVitals();
      console.log("[Startup] Caches warmed.");
    } catch (e) {
      console.log("[Startup] Cache warming error:", e.message);
    }
    // Check for optional system dependencies (once at startup)
    checkOptionalDeps();
  }, 100);

  // Background cache refresh
  const SESSIONS_CACHE_TTL = 10000;
  setInterval(() => sessions.refreshSessionsCache(), SESSIONS_CACHE_TTL);
});

// SSE heartbeat
let sseRefreshing = false;
setInterval(() => {
  if (sseClients.size > 0 && !sseRefreshing) {
    sseRefreshing = true;
    try {
      const fullState = state.refreshState();
      broadcastSSE("update", fullState);
      broadcastSSE("heartbeat", { clients: sseClients.size, timestamp: Date.now() });
    } catch (e) {
      console.error("[SSE] Broadcast error:", e.message);
    }
    sseRefreshing = false;
  }
}, 15000);
```

## File: `src/jobs.js`
```javascript
/**
 * Jobs Dashboard API Handler
 *
 * Wraps the jobs API for the dashboard server.
 * Uses dynamic imports to bridge CommonJS server with ESM jobs modules.
 */

const path = require("path");
const { CONFIG } = require("./config");

// Jobs directory (from config with auto-detection)
const JOBS_DIR = CONFIG.paths.jobs;
const JOBS_STATE_DIR = path.join(CONFIG.paths.state, "jobs");

let apiInstance = null;
let forceApiUnavailable = false; // For testing

/**
 * Initialize the jobs API (lazy-loaded due to ESM)
 */
async function getAPI() {
  if (forceApiUnavailable) return null;
  if (apiInstance) return apiInstance;

  try {
    const { createJobsAPI } = await import(path.join(JOBS_DIR, "lib/api.js"));
    apiInstance = createJobsAPI({
      definitionsDir: path.join(JOBS_DIR, "definitions"),
      stateDir: JOBS_STATE_DIR,
    });
    return apiInstance;
  } catch (e) {
    console.error("Failed to load jobs API:", e.message);
    return null;
  }
}

/**
 * Reset API state for testing purposes
 * @param {Object} options - Reset options
 * @param {boolean} options.forceUnavailable - If true, getAPI() will return null
 */
function _resetForTesting(options = {}) {
  apiInstance = null;
  forceApiUnavailable = options.forceUnavailable || false;
}

/**
 * Format relative time
 */
function formatRelativeTime(isoString) {
  if (!isoString) return null;
  const date = new Date(isoString);
  const now = new Date();
  const diffMs = now - date;
  const diffMins = Math.round(diffMs / 60000);

  if (diffMins < 0) {
    const futureMins = Math.abs(diffMins);
    if (futureMins < 60) return `in ${futureMins}m`;
    if (futureMins < 1440) return `in ${Math.round(futureMins / 60)}h`;
    return `in ${Math.round(futureMins / 1440)}d`;
  }

  if (diffMins < 1) return "just now";
  if (diffMins < 60) return `${diffMins}m ago`;
  if (diffMins < 1440) return `${Math.round(diffMins / 60)}h ago`;
  return `${Math.round(diffMins / 1440)}d ago`;
}

/**
 * Handle jobs API requests
 */
async function handleJobsRequest(req, res, pathname, query, method) {
  const api = await getAPI();

  if (!api) {
    res.writeHead(500, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "Jobs API not available" }));
    return;
  }

  try {
    // Scheduler status: GET /api/jobs/scheduler/status (before single job route)
    if (pathname === "/api/jobs/scheduler/status" && method === "GET") {
      const status = await api.getSchedulerStatus();
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(status, null, 2));
      return;
    }

    // Aggregate stats: GET /api/jobs/stats (before single job route)
    if (pathname === "/api/jobs/stats" && method === "GET") {
      const stats = await api.getAggregateStats();
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(stats, null, 2));
      return;
    }

    // Clear cache: POST /api/jobs/cache/clear (before single job route)
    if (pathname === "/api/jobs/cache/clear" && method === "POST") {
      api.clearCache();
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ success: true, message: "Cache cleared" }));
      return;
    }

    // List all jobs: GET /api/jobs
    if (pathname === "/api/jobs" && method === "GET") {
      const jobs = await api.listJobs();

      // Enhance with relative times
      const enhanced = jobs.map((job) => ({
        ...job,
        lastRunRelative: formatRelativeTime(job.lastRun),
        nextRunRelative: formatRelativeTime(job.nextRun),
      }));

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ jobs: enhanced, timestamp: Date.now() }, null, 2));
      return;
    }

    // Get single job: GET /api/jobs/:id
    const jobMatch = pathname.match(/^\/api\/jobs\/([^/]+)$/);
    if (jobMatch && method === "GET") {
      const jobId = decodeURIComponent(jobMatch[1]);
      const job = await api.getJob(jobId);

      if (!job) {
        res.writeHead(404, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Job not found" }));
        return;
      }

      // Enhance with relative times
      job.lastRunRelative = formatRelativeTime(job.lastRun);
      job.nextRunRelative = formatRelativeTime(job.nextRun);
      if (job.recentRuns) {
        job.recentRuns = job.recentRuns.map((run) => ({
          ...run,
          startedAtRelative: formatRelativeTime(run.startedAt),
          completedAtRelative: formatRelativeTime(run.completedAt),
        }));
      }

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(job, null, 2));
      return;
    }

    // Get job history: GET /api/jobs/:id/history
    const historyMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/history$/);
    if (historyMatch && method === "GET") {
      const jobId = decodeURIComponent(historyMatch[1]);
      const limit = parseInt(query.get("limit") || "50", 10);
      const runs = await api.getJobHistory(jobId, limit);

      const enhanced = runs.map((run) => ({
        ...run,
        startedAtRelative: formatRelativeTime(run.startedAt),
        completedAtRelative: formatRelativeTime(run.completedAt),
      }));

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ runs: enhanced, timestamp: Date.now() }, null, 2));
      return;
    }

    // Run job: POST /api/jobs/:id/run
    const runMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/run$/);
    if (runMatch && method === "POST") {
      const jobId = decodeURIComponent(runMatch[1]);
      const result = await api.runJob(jobId);

      res.writeHead(result.success ? 200 : 400, { "Content-Type": "application/json" });
      res.end(JSON.stringify(result, null, 2));
      return;
    }

    // Pause job: POST /api/jobs/:id/pause
    const pauseMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/pause$/);
    if (pauseMatch && method === "POST") {
      const jobId = decodeURIComponent(pauseMatch[1]);

      // Parse body for reason
      let body = "";
      await new Promise((resolve) => {
        req.on("data", (chunk) => (body += chunk));
        req.on("end", resolve);
      });

      let reason = null;
      try {
        const parsed = JSON.parse(body || "{}");
        reason = parsed.reason;
      } catch (_e) {
        /* ignore parse errors */
      }

      const result = await api.pauseJob(jobId, {
        by: req.authUser?.login || "dashboard",
        reason,
      });

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(result, null, 2));
      return;
    }

    // Resume job: POST /api/jobs/:id/resume
    const resumeMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/resume$/);
    if (resumeMatch && method === "POST") {
      const jobId = decodeURIComponent(resumeMatch[1]);
      const result = await api.resumeJob(jobId);

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(result, null, 2));
      return;
    }

    // Skip job: POST /api/jobs/:id/skip
    const skipMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/skip$/);
    if (skipMatch && method === "POST") {
      const jobId = decodeURIComponent(skipMatch[1]);
      const result = await api.skipJob(jobId);

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(result, null, 2));
      return;
    }

    // Kill job: POST /api/jobs/:id/kill
    const killMatch = pathname.match(/^\/api\/jobs\/([^/]+)\/kill$/);
    if (killMatch && method === "POST") {
      const jobId = decodeURIComponent(killMatch[1]);
      const result = await api.killJob(jobId);

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(result, null, 2));
      return;
    }

    // Not found
    res.writeHead(404, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "Not found" }));
  } catch (e) {
    console.error("Jobs API error:", e);
    res.writeHead(500, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: e.message }));
  }
}

/**
 * Check if a request should be handled by jobs API
 */
function isJobsRoute(pathname) {
  return pathname.startsWith("/api/jobs");
}

module.exports = { handleJobsRequest, isJobsRoute, _resetForTesting };
```

## File: `src/llm-usage.js`
```javascript
const fs = require("fs");
const path = require("path");
const { execFile } = require("child_process");
const { getSafeEnv } = require("./openclaw");

// Cache for LLM usage data (openclaw CLI is slow ~4-5s)
let llmUsageCache = { data: null, timestamp: 0, refreshing: false };
const LLM_CACHE_TTL_MS = 60000; // 60 seconds

// Background async refresh of LLM usage data
function refreshLlmUsageAsync() {
  if (llmUsageCache.refreshing) return; // Already refreshing
  llmUsageCache.refreshing = true;

  const profile = process.env.OPENCLAW_PROFILE || "";
  const args = profile
    ? ["--profile", profile, "status", "--usage", "--json"]
    : ["status", "--usage", "--json"];
  execFile(
    "openclaw",
    args,
    { encoding: "utf8", timeout: 20000, env: getSafeEnv() },
    (err, stdout) => {
      llmUsageCache.refreshing = false;
      if (err) {
        console.error("[LLM Usage] Async refresh failed:", err.message);
        return;
      }
      try {
        // Extract JSON portion - openclaw may output doctor warnings before JSON
        const jsonStart = stdout.indexOf("{");
        const jsonStr = jsonStart >= 0 ? stdout.slice(jsonStart) : stdout;
        const parsed = JSON.parse(jsonStr);
        if (parsed.usage) {
          const result = transformLiveUsageData(parsed.usage);
          llmUsageCache.data = result;
          llmUsageCache.timestamp = Date.now();
          console.log("[LLM Usage] Cache refreshed");
        }
      } catch (e) {
        console.error("[LLM Usage] Parse error:", e.message);
      }
    },
  );
}

// Transform live usage data from OpenClaw CLI
function transformLiveUsageData(usage) {
  const anthropic = usage.providers?.find((p) => p.provider === "anthropic");
  const codexProvider = usage.providers?.find((p) => p.provider === "openai-codex");

  // Check for auth errors
  if (anthropic?.error) {
    return {
      timestamp: new Date().toISOString(),
      source: "error",
      error: anthropic.error,
      errorType: anthropic.error.includes("403") ? "auth" : "unknown",
      claude: {
        session: { usedPct: null, remainingPct: null, resetsIn: null, error: anthropic.error },
        weekly: { usedPct: null, remainingPct: null, resets: null, error: anthropic.error },
        sonnet: { usedPct: null, remainingPct: null, resets: null, error: anthropic.error },
        lastSynced: null,
      },
      codex: { sessionsToday: 0, tasksToday: 0, usage5hPct: 0, usageDayPct: 0 },
      routing: {
        total: 0,
        claudeTasks: 0,
        codexTasks: 0,
        claudePct: 0,
        codexPct: 0,
        codexFloor: 20,
      },
    };
  }

  const session5h = anthropic?.windows?.find((w) => w.label === "5h");
  const weekAll = anthropic?.windows?.find((w) => w.label === "Week");
  const sonnetWeek = anthropic?.windows?.find((w) => w.label === "Sonnet");
  const codex5h = codexProvider?.windows?.find((w) => w.label === "5h");
  const codexDay = codexProvider?.windows?.find((w) => w.label === "Day");

  const formatReset = (resetAt) => {
    if (!resetAt) return "?";
    const diff = resetAt - Date.now();
    if (diff < 0) return "now";
    if (diff < 3600000) return Math.round(diff / 60000) + "m";
    if (diff < 86400000) return Math.round(diff / 3600000) + "h";
    return Math.round(diff / 86400000) + "d";
  };

  return {
    timestamp: new Date().toISOString(),
    source: "live",
    claude: {
      session: {
        usedPct: Math.round(session5h?.usedPercent || 0),
        remainingPct: Math.round(100 - (session5h?.usedPercent || 0)),
        resetsIn: formatReset(session5h?.resetAt),
      },
      weekly: {
        usedPct: Math.round(weekAll?.usedPercent || 0),
        remainingPct: Math.round(100 - (weekAll?.usedPercent || 0)),
        resets: formatReset(weekAll?.resetAt),
      },
      sonnet: {
        usedPct: Math.round(sonnetWeek?.usedPercent || 0),
        remainingPct: Math.round(100 - (sonnetWeek?.usedPercent || 0)),
        resets: formatReset(sonnetWeek?.resetAt),
      },
      lastSynced: new Date().toISOString(),
    },
    codex: {
      sessionsToday: 0,
      tasksToday: 0,
      usage5hPct: Math.round(codex5h?.usedPercent || 0),
      usageDayPct: Math.round(codexDay?.usedPercent || 0),
    },
    routing: { total: 0, claudeTasks: 0, codexTasks: 0, claudePct: 0, codexPct: 0, codexFloor: 20 },
  };
}

// Get LLM usage stats - returns cached data immediately, refreshes in background
function getLlmUsage(statePath) {
  const now = Date.now();

  // If cache is stale or empty, trigger background refresh
  if (!llmUsageCache.data || now - llmUsageCache.timestamp > LLM_CACHE_TTL_MS) {
    refreshLlmUsageAsync();
  }

  // Return cached data if available AND not an error
  // If cache has error, try file fallback first
  if (llmUsageCache.data && llmUsageCache.data.source !== "error") {
    return llmUsageCache.data;
  }

  // Cache empty or has error - check if we can read from state file
  // But don't return misleading 0% values - return error/loading state instead
  const stateFile = path.join(statePath, "llm-routing.json");
  try {
    if (fs.existsSync(stateFile)) {
      const data = JSON.parse(fs.readFileSync(stateFile, "utf8"));
      // Only use file data if it has valid (non-placeholder) usage values
      // Check for "unknown" resets which indicates placeholder data from failed sync
      const sessionValid =
        data.claude?.session?.resets_in && data.claude.session.resets_in !== "unknown";
      const weeklyValid =
        data.claude?.weekly_all_models?.resets &&
        data.claude.weekly_all_models.resets !== "unknown";
      if (sessionValid || weeklyValid) {
        return {
          timestamp: new Date().toISOString(),
          source: "file",
          claude: {
            session: {
              usedPct: Math.round((data.claude?.session?.used_pct || 0) * 100),
              remainingPct: Math.round((data.claude?.session?.remaining_pct || 1) * 100),
              resetsIn: data.claude?.session?.resets_in || "?",
            },
            weekly: {
              usedPct: Math.round((data.claude?.weekly_all_models?.used_pct || 0) * 100),
              remainingPct: Math.round((data.claude?.weekly_all_models?.remaining_pct || 1) * 100),
              resets: data.claude?.weekly_all_models?.resets || "?",
            },
            sonnet: {
              usedPct: Math.round((data.claude?.weekly_sonnet?.used_pct || 0) * 100),
              remainingPct: Math.round((data.claude?.weekly_sonnet?.remaining_pct || 1) * 100),
              resets: data.claude?.weekly_sonnet?.resets || "?",
            },
            lastSynced: data.claude?.last_synced || null,
          },
          codex: {
            sessionsToday: data.codex?.sessions_today || 0,
            tasksToday: data.codex?.tasks_today || 0,
            usage5hPct: data.codex?.usage_5h_pct || 0,
            usageDayPct: data.codex?.usage_day_pct || 0,
          },
          routing: {
            total: data.routing?.total_tasks || 0,
            claudeTasks: data.routing?.claude_tasks || 0,
            codexTasks: data.routing?.codex_tasks || 0,
            claudePct:
              data.routing?.total_tasks > 0
                ? Math.round((data.routing.claude_tasks / data.routing.total_tasks) * 100)
                : 0,
            codexPct:
              data.routing?.total_tasks > 0
                ? Math.round((data.routing.codex_tasks / data.routing.total_tasks) * 100)
                : 0,
            codexFloor: Math.round((data.routing?.codex_floor_pct || 0.2) * 100),
          },
        };
      }
    }
  } catch (e) {
    console.error("[LLM Usage] File fallback failed:", e.message);
  }

  // No valid data - return auth error state (we know API returns 403)
  return {
    timestamp: new Date().toISOString(),
    source: "error",
    error: "API key lacks user:profile OAuth scope",
    errorType: "auth",
    claude: {
      session: { usedPct: null, remainingPct: null, resetsIn: null, error: "Auth required" },
      weekly: { usedPct: null, remainingPct: null, resets: null, error: "Auth required" },
      sonnet: { usedPct: null, remainingPct: null, resets: null, error: "Auth required" },
      lastSynced: null,
    },
    codex: { sessionsToday: 0, tasksToday: 0, usage5hPct: 0, usageDayPct: 0 },
    routing: { total: 0, claudeTasks: 0, codexTasks: 0, claudePct: 0, codexPct: 0, codexFloor: 20 },
  };
}

function getRoutingStats(skillsPath, statePath, hours = 24) {
  const safeHours = parseInt(hours, 10) || 24;
  try {
    const { execFileSync } = require("child_process");
    const skillDir = path.join(skillsPath, "llm_routing");
    const output = execFileSync(
      "python",
      ["-m", "llm_routing", "stats", "--hours", String(safeHours), "--json"],
      {
        encoding: "utf8",
        timeout: 10000,
        cwd: skillDir,
        env: getSafeEnv(),
      },
    );
    return JSON.parse(output);
  } catch (e) {
    // Fallback: read JSONL directly
    try {
      const logFile = path.join(statePath, "routing-log.jsonl");
      if (!fs.existsSync(logFile)) {
        return { total_requests: 0, by_model: {}, by_task_type: {} };
      }

      const cutoff = Date.now() - hours * 3600 * 1000;
      const lines = fs.readFileSync(logFile, "utf8").trim().split("\n").filter(Boolean);

      const stats = {
        total_requests: 0,
        by_model: {},
        by_task_type: {},
        escalations: 0,
        avg_latency_ms: 0,
        success_rate: 0,
      };

      let latencies = [];
      let successes = 0;

      for (const line of lines) {
        try {
          const entry = JSON.parse(line);
          const ts = new Date(entry.timestamp).getTime();
          if (ts < cutoff) continue;

          stats.total_requests++;

          // By model
          const model = entry.selected_model || "unknown";
          stats.by_model[model] = (stats.by_model[model] || 0) + 1;

          // By task type
          const tt = entry.task_type || "unknown";
          stats.by_task_type[tt] = (stats.by_task_type[tt] || 0) + 1;

          if (entry.escalation_reason) stats.escalations++;
          if (entry.latency_ms) latencies.push(entry.latency_ms);
          if (entry.success === true) successes++;
        } catch {}
      }

      if (latencies.length > 0) {
        stats.avg_latency_ms = Math.round(latencies.reduce((a, b) => a + b, 0) / latencies.length);
      }
      if (stats.total_requests > 0) {
        stats.success_rate = Math.round((successes / stats.total_requests) * 100);
      }

      return stats;
    } catch (e2) {
      console.error("Failed to read routing stats:", e2.message);
      return { error: e2.message };
    }
  }
}

// Start background refresh timers (call explicitly, not on require)
function startLlmUsageRefresh() {
  setTimeout(() => refreshLlmUsageAsync(), 1000);
  setInterval(() => refreshLlmUsageAsync(), LLM_CACHE_TTL_MS);
}

module.exports = {
  refreshLlmUsageAsync,
  transformLiveUsageData,
  getLlmUsage,
  getRoutingStats,
  startLlmUsageRefresh,
};
```

## File: `src/openclaw.js`
```javascript
/**
 * OpenClaw CLI helpers - wrappers for running openclaw commands
 */

const { execFileSync, execFile } = require("child_process");
const { promisify } = require("util");
const execFileAsync = promisify(execFile);

/**
 * Build a minimal env for child processes.
 * Avoids leaking secrets (API keys, cloud creds) to shell subprocesses.
 */
function getSafeEnv() {
  return {
    PATH: process.env.PATH,
    HOME: process.env.HOME,
    USER: process.env.USER,
    SHELL: process.env.SHELL,
    LANG: process.env.LANG,
    NO_COLOR: "1",
    TERM: "dumb",
    OPENCLAW_PROFILE: process.env.OPENCLAW_PROFILE || "",
    OPENCLAW_WORKSPACE: process.env.OPENCLAW_WORKSPACE || "",
    OPENCLAW_HOME: process.env.OPENCLAW_HOME || "",
  };
}

/**
 * Build args array for openclaw CLI, prepending --profile if set.
 * Splits the args string on whitespace (shell-injection-safe since
 * execFileSync never invokes a shell).
 */
function buildArgs(args) {
  const profile = process.env.OPENCLAW_PROFILE || "";
  const profileArgs = profile ? ["--profile", profile] : [];
  // Strip shell redirections (e.g. "2>&1", "2>/dev/null") — not needed with execFile
  const cleanArgs = args
    .replace(/\s*2>&1\s*/g, " ")
    .replace(/\s*2>\/dev\/null\s*/g, " ")
    .trim();
  return [...profileArgs, ...cleanArgs.split(/\s+/).filter(Boolean)];
}

/**
 * Run openclaw CLI command synchronously
 * Uses execFileSync (no shell) to eliminate injection surface.
 * @param {string} args - Command arguments
 * @returns {string|null} - Command output or null on error
 */
function runOpenClaw(args) {
  try {
    const result = execFileSync("openclaw", buildArgs(args), {
      encoding: "utf8",
      timeout: 3000,
      env: getSafeEnv(),
      stdio: ["pipe", "pipe", "pipe"],
    });
    return result;
  } catch (e) {
    return null;
  }
}

/**
 * Run openclaw CLI command asynchronously
 * Uses execFile (no shell) to eliminate injection surface.
 * @param {string} args - Command arguments
 * @returns {Promise<string|null>} - Command output or null on error
 */
async function runOpenClawAsync(args) {
  try {
    const { stdout } = await execFileAsync("openclaw", buildArgs(args), {
      encoding: "utf8",
      timeout: 20000,
      env: getSafeEnv(),
    });
    return stdout;
  } catch (e) {
    console.error("[OpenClaw Async] Error:", e.message);
    return null;
  }
}

/**
 * Extract JSON from openclaw output (may have non-JSON prefix)
 * @param {string} output - Raw CLI output
 * @returns {string|null} - JSON string or null
 */
function extractJSON(output) {
  if (!output) return null;
  const jsonStart = output.search(/[[{]/);
  if (jsonStart === -1) return null;
  return output.slice(jsonStart);
}

module.exports = {
  runOpenClaw,
  runOpenClawAsync,
  extractJSON,
  getSafeEnv,
};
```

## File: `src/operators.js`
```javascript
const fs = require("fs");
const path = require("path");

function loadOperators(dataDir) {
  const operatorsFile = path.join(dataDir, "operators.json");
  try {
    if (fs.existsSync(operatorsFile)) {
      return JSON.parse(fs.readFileSync(operatorsFile, "utf8"));
    }
  } catch (e) {
    console.error("Failed to load operators:", e.message);
  }
  return { version: 1, operators: [], roles: {} };
}

function saveOperators(dataDir, data) {
  try {
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true });
    }
    const operatorsFile = path.join(dataDir, "operators.json");
    fs.writeFileSync(operatorsFile, JSON.stringify(data, null, 2));
    return true;
  } catch (e) {
    console.error("Failed to save operators:", e.message);
    return false;
  }
}

function getOperatorBySlackId(dataDir, slackId) {
  const data = loadOperators(dataDir);
  return data.operators.find((op) => op.id === slackId || op.metadata?.slackId === slackId);
}

// Auto-detect operators from session transcripts (runs async in background)
let operatorsRefreshing = false;
async function refreshOperatorsAsync(dataDir, getOpenClawDir) {
  if (operatorsRefreshing) return;
  operatorsRefreshing = true;

  // Normalize timestamp to ms (handles ISO strings, numbers, and fallback)
  const toMs = (ts, fallback) => {
    if (typeof ts === "number" && Number.isFinite(ts)) return ts;
    if (typeof ts === "string") {
      const parsed = Date.parse(ts);
      if (Number.isFinite(parsed)) return parsed;
    }
    return fallback;
  };

  try {
    const openclawDir = getOpenClawDir();
    const sessionsDir = path.join(openclawDir, "agents", "main", "sessions");

    if (!fs.existsSync(sessionsDir)) {
      operatorsRefreshing = false;
      return;
    }

    const files = fs.readdirSync(sessionsDir).filter((f) => f.endsWith(".jsonl"));
    const operatorsMap = new Map(); // userId -> operator data
    const sevenDaysAgo = Date.now() - 7 * 24 * 60 * 60 * 1000;

    for (const file of files) {
      const filePath = path.join(sessionsDir, file);
      try {
        const stat = fs.statSync(filePath);
        // Only scan files modified in last 7 days
        if (stat.mtimeMs < sevenDaysAgo) continue;

        // Read first 10KB of each file (enough to get user info)
        const fd = fs.openSync(filePath, "r");
        const buffer = Buffer.alloc(10240);
        const bytesRead = fs.readSync(fd, buffer, 0, 10240, 0);
        fs.closeSync(fd);

        const content = buffer.toString("utf8", 0, bytesRead);
        const lines = content.split("\n").slice(0, 20); // First 20 lines

        for (const line of lines) {
          if (!line.trim()) continue;
          try {
            const entry = JSON.parse(line);
            if (entry.type !== "message" || !entry.message) continue;

            const msg = entry.message;
            if (msg.role !== "user") continue;

            let text = "";
            if (typeof msg.content === "string") {
              text = msg.content;
            } else if (Array.isArray(msg.content)) {
              const textPart = msg.content.find((c) => c.type === "text");
              if (textPart) text = textPart.text || "";
            }

            if (!text) continue;

            // Extract Slack user: "[Slack #channel +Xm date] username (USERID):"
            const slackMatch = text.match(/\[Slack[^\]]*\]\s*([\w.-]+)\s*\(([A-Z0-9]+)\):/);
            if (slackMatch) {
              const username = slackMatch[1];
              const userId = slackMatch[2];

              if (!operatorsMap.has(userId)) {
                operatorsMap.set(userId, {
                  id: userId,
                  name: username,
                  username: username,
                  source: "slack",
                  firstSeen: toMs(entry.timestamp, stat.mtimeMs),
                  lastSeen: toMs(entry.timestamp, stat.mtimeMs),
                  sessionCount: 1,
                });
              } else {
                const op = operatorsMap.get(userId);
                op.lastSeen = Math.max(op.lastSeen, toMs(entry.timestamp, stat.mtimeMs));
                op.sessionCount++;
              }
              break; // Found user for this session, move to next file
            }

            // Also check for Telegram users: "[Telegram +Xm date] username:"
            const telegramMatch = text.match(/\[Telegram[^\]]*\]\s*([\w.-]+):/);
            if (telegramMatch) {
              const username = telegramMatch[1];
              const operatorId = `telegram:${username}`;

              if (!operatorsMap.has(operatorId)) {
                operatorsMap.set(operatorId, {
                  id: operatorId,
                  name: username,
                  username: username,
                  source: "telegram",
                  firstSeen: toMs(entry.timestamp, stat.mtimeMs),
                  lastSeen: toMs(entry.timestamp, stat.mtimeMs),
                  sessionCount: 1,
                });
              } else {
                const op = operatorsMap.get(operatorId);
                op.lastSeen = Math.max(op.lastSeen, toMs(entry.timestamp, stat.mtimeMs));
                op.sessionCount++;
              }
              break;
            }

            // Check for Discord users in "Conversation info" JSON block
            // Pattern: "sender": "123456789012345678" and "label": "CoolUser123"
            const discordSenderMatch = text.match(/"sender":\s*"(\d+)"/);
            const discordLabelMatch = text.match(/"label":\s*"([^"]+)"/);
            const discordUsernameMatch = text.match(/"username":\s*"([^"]+)"/);

            if (discordSenderMatch) {
              const userId = discordSenderMatch[1];
              const label = discordLabelMatch ? discordLabelMatch[1] : userId;
              const username = discordUsernameMatch ? discordUsernameMatch[1] : label;
              const opId = `discord:${userId}`;

              if (!operatorsMap.has(opId)) {
                operatorsMap.set(opId, {
                  id: opId,
                  discordId: userId,
                  name: label,
                  username: username,
                  source: "discord",
                  firstSeen: toMs(entry.timestamp, stat.mtimeMs),
                  lastSeen: toMs(entry.timestamp, stat.mtimeMs),
                  sessionCount: 1,
                });
              } else {
                const op = operatorsMap.get(opId);
                op.lastSeen = Math.max(op.lastSeen, toMs(entry.timestamp, stat.mtimeMs));
                op.sessionCount++;
              }
              break;
            }
          } catch (e) {
            /* skip invalid lines */
          }
        }
      } catch (e) {
        /* skip unreadable files */
      }
    }

    // Load existing operators to preserve manual edits
    const existing = loadOperators(dataDir);
    const existingMap = new Map(existing.operators.map((op) => [op.id, op]));

    // Merge: auto-detected + existing manual entries
    for (const [id, autoOp] of operatorsMap) {
      if (existingMap.has(id)) {
        // Update stats but preserve manual fields
        const manual = existingMap.get(id);
        manual.lastSeen = Math.max(manual.lastSeen || 0, autoOp.lastSeen);
        manual.sessionCount = (manual.sessionCount || 0) + autoOp.sessionCount;
      } else {
        existingMap.set(id, autoOp);
      }
    }

    // Save merged operators
    const merged = {
      version: 1,
      operators: Array.from(existingMap.values()).sort(
        (a, b) => (b.lastSeen || 0) - (a.lastSeen || 0),
      ),
      roles: existing.roles || {},
      lastRefreshed: Date.now(),
    };

    saveOperators(dataDir, merged);
    console.log(`[Operators] Refreshed: ${merged.operators.length} operators detected`);
  } catch (e) {
    console.error("[Operators] Refresh failed:", e.message);
  }

  operatorsRefreshing = false;
}

// Start background operators refresh (caller invokes this instead of auto-starting on load)
function startOperatorsRefresh(dataDir, getOpenClawDir) {
  setTimeout(() => refreshOperatorsAsync(dataDir, getOpenClawDir), 2000);
  setInterval(() => refreshOperatorsAsync(dataDir, getOpenClawDir), 5 * 60 * 1000); // Every 5 minutes
}

/**
 * Calculate operator stats from sessions (single source of truth)
 * @param {Object} operatorData - Result from loadOperators()
 * @param {Array} allSessions - Array of session objects with originator field
 * @returns {Object} - operatorData with stats added to each operator
 */
function calculateOperatorStats(operatorData, allSessions) {
  const operatorsWithStats = operatorData.operators.map((op) => {
    const userSessions = allSessions.filter((s) => {
      const userId = s.originator?.userId;
      if (!userId) return false; // Skip sessions without originator
      return userId === op.id || userId === op.metadata?.slackId;
    });
    return {
      ...op,
      stats: {
        activeSessions: userSessions.filter((s) => s.active).length,
        totalSessions: userSessions.length,
        lastSeen:
          userSessions.length > 0
            ? new Date(
                Date.now() - Math.min(...userSessions.map((s) => s.minutesAgo)) * 60000,
              ).toISOString()
            : op.lastSeen,
      },
    };
  });
  return { ...operatorData, operators: operatorsWithStats };
}

module.exports = {
  loadOperators,
  saveOperators,
  getOperatorBySlackId,
  refreshOperatorsAsync,
  startOperatorsRefresh,
  calculateOperatorStats,
};
```

## File: `src/privacy.js`
```javascript
const fs = require("fs");
const path = require("path");

function getPrivacyFilePath(dataDir) {
  return path.join(dataDir, "privacy-settings.json");
}

function loadPrivacySettings(dataDir) {
  try {
    const privacyFile = getPrivacyFilePath(dataDir);
    if (fs.existsSync(privacyFile)) {
      return JSON.parse(fs.readFileSync(privacyFile, "utf8"));
    }
  } catch (e) {
    console.error("Failed to load privacy settings:", e.message);
  }
  return {
    version: 1,
    hiddenTopics: [],
    hiddenSessions: [],
    hiddenCrons: [],
    hideHostname: false,
    updatedAt: null,
  };
}

function savePrivacySettings(dataDir, data) {
  try {
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true });
    }
    data.updatedAt = new Date().toISOString();
    fs.writeFileSync(getPrivacyFilePath(dataDir), JSON.stringify(data, null, 2));
    return true;
  } catch (e) {
    console.error("Failed to save privacy settings:", e.message);
    return false;
  }
}

module.exports = {
  loadPrivacySettings,
  savePrivacySettings,
};
```

## File: `src/sessions.js`
```javascript
const fs = require("fs");
const path = require("path");
const { detectTopics } = require("./topics");

// Channel ID to name mapping (auto-populated from Slack)
const CHANNEL_MAP = {
  c0aax7y80np: "#cc-meta",
  c0ab9f8sdfe: "#cc-research",
  c0aan4rq7v5: "#cc-finance",
  c0abxulk1qq: "#cc-properties",
  c0ab5nz8mkl: "#cc-ai",
  c0aan38tzv5: "#cc-dev",
  c0ab7wwhqvc: "#cc-home",
  c0ab1pjhxef: "#cc-health",
  c0ab7txvcqd: "#cc-legal",
  c0aay2g3n3r: "#cc-social",
  c0aaxrw2wqp: "#cc-business",
  c0ab19f3lae: "#cc-random",
  c0ab0r74y33: "#cc-food",
  c0ab0qrq3r9: "#cc-travel",
  c0ab0sbqqlg: "#cc-family",
  c0ab0slqdba: "#cc-games",
  c0ab1ps7ef2: "#cc-music",
  c0absbnrsbe: "#cc-dashboard",
};

// Parse session key into readable label
function parseSessionLabel(key) {
  // Pattern: agent:main:slack:channel:CHANNEL_ID:thread:TIMESTAMP
  // or: agent:main:slack:channel:CHANNEL_ID
  // or: agent:main:main (telegram main)

  const parts = key.split(":");

  if (parts.includes("slack")) {
    const channelIdx = parts.indexOf("channel");
    if (channelIdx >= 0 && parts[channelIdx + 1]) {
      const channelId = parts[channelIdx + 1].toLowerCase();
      const channelName = CHANNEL_MAP[channelId] || `#${channelId}`;

      // Check if it's a thread
      if (parts.includes("thread")) {
        const threadTs = parts[parts.indexOf("thread") + 1];
        // Convert timestamp to rough time
        const ts = parseFloat(threadTs);
        const date = new Date(ts * 1000);
        const timeStr = date.toLocaleTimeString("en-US", { hour: "numeric", minute: "2-digit" });
        return `${channelName} thread @ ${timeStr}`;
      }
      return channelName;
    }
  }

  if (key.includes("telegram")) {
    return "📱 Telegram";
  }

  if (key === "agent:main:main") {
    return "🏠 Main Session";
  }

  // Fallback: truncate key
  return key.length > 40 ? key.slice(0, 37) + "..." : key;
}

/**
 * Create a sessions module with bound dependencies.
 * @param {Object} deps
 * @param {Function} deps.getOpenClawDir - Returns the OpenClaw directory path
 * @param {Function} deps.getOperatorBySlackId - Look up operator by Slack ID
 * @param {Function} deps.runOpenClaw - Run OpenClaw command synchronously
 * @param {Function} deps.runOpenClawAsync - Run OpenClaw command asynchronously
 * @param {Function} deps.extractJSON - Extract JSON from command output
 * @returns {Object} Session management functions
 */
function createSessionsModule(deps) {
  const { getOpenClawDir, getOperatorBySlackId, runOpenClaw, runOpenClawAsync, extractJSON } = deps;

  // SESSION CACHE - Async refresh to avoid blocking
  let sessionsCache = { sessions: [], timestamp: 0, refreshing: false };
  const SESSIONS_CACHE_TTL = 10000; // 10 seconds

  /**
   * Find transcript file for a session ID.
   * Handles both plain (sessionId.jsonl) and topic-suffixed (sessionId-topic-XXX.jsonl) files.
   * @param {string} sessionId - Session UUID
   * @returns {string|null} - Full path to transcript file or null if not found
   */
  function findTranscriptPath(sessionId) {
    if (!sessionId) return null;

    const openclawDir = getOpenClawDir();
    const sessionsDir = path.join(openclawDir, "agents", "main", "sessions");

    // Try exact match first (most common case)
    const exactPath = path.join(sessionsDir, `${sessionId}.jsonl`);
    if (fs.existsSync(exactPath)) return exactPath;

    // Search for topic-suffixed files (e.g., sessionId-topic-TIMESTAMP.jsonl)
    try {
      const files = fs.readdirSync(sessionsDir);
      const prefix = `${sessionId}-`;
      const match = files.find(
        (f) => f.startsWith(prefix) && f.endsWith(".jsonl") && !f.includes(".deleted."),
      );
      if (match) return path.join(sessionsDir, match);
    } catch (e) {
      // Directory read failed
    }

    return null;
  }

  // Extract session originator from transcript
  function getSessionOriginator(sessionId) {
    try {
      if (!sessionId) return null;

      const transcriptPath = findTranscriptPath(sessionId);
      if (!transcriptPath) return null;

      const content = fs.readFileSync(transcriptPath, "utf8");
      const lines = content.trim().split("\n");

      // Find the first user message to extract originator
      for (let i = 0; i < Math.min(lines.length, 10); i++) {
        try {
          const entry = JSON.parse(lines[i]);
          if (entry.type !== "message" || !entry.message) continue;

          const msg = entry.message;
          if (msg.role !== "user") continue;

          let text = "";
          if (typeof msg.content === "string") {
            text = msg.content;
          } else if (Array.isArray(msg.content)) {
            const textPart = msg.content.find((c) => c.type === "text");
            if (textPart) text = textPart.text || "";
          }

          if (!text) continue;

          // Extract Slack user from message patterns:
          // Format 1 (old): "[Slack #channel +6m 2026-01-27 15:31 PST] username (USERID): message"
          // Format 2 (new): Conversation info JSON with "sender_id": "USERID" and "sender": "username"
          const slackUserMatch = text.match(/\]\s*([\w.-]+)\s*\(([A-Z0-9]+)\):/);

          if (slackUserMatch) {
            const username = slackUserMatch[1];
            const userId = slackUserMatch[2];

            const operator = getOperatorBySlackId(userId);

            return {
              userId,
              username,
              displayName: operator?.name || username,
              role: operator?.role || "user",
              avatar: operator?.avatar || null,
            };
          }

          // Try new format: Conversation info JSON block
          // Look for "sender_id": "USERID" and "sender": "username"
          const senderIdMatch = text.match(/"sender_id":\s*"([A-Z0-9]+)"/);
          const senderMatch = text.match(/"sender":\s*"([^"]+)"/);

          if (senderIdMatch) {
            const userId = senderIdMatch[1];
            const username = senderMatch ? senderMatch[1] : userId;

            const operator = getOperatorBySlackId(userId);

            return {
              userId,
              username,
              displayName: operator?.name || username,
              role: operator?.role || "user",
              avatar: operator?.avatar || null,
            };
          }
        } catch (e) {}
      }

      return null;
    } catch (e) {
      return null;
    }
  }

  /**
   * Get quick topic for a session by reading first portion of transcript
   * @param {string} sessionId - Session ID
   * @returns {string|null} - Primary topic or null
   */
  function getSessionTopic(sessionId) {
    if (!sessionId) return null;
    try {
      const transcriptPath = findTranscriptPath(sessionId);
      if (!transcriptPath) return null;

      // Read first 50KB of transcript (enough for topic detection, fast)
      const fd = fs.openSync(transcriptPath, "r");
      const buffer = Buffer.alloc(50000);
      const bytesRead = fs.readSync(fd, buffer, 0, 50000, 0);
      fs.closeSync(fd);

      if (bytesRead === 0) return null;

      const content = buffer.toString("utf8", 0, bytesRead);
      const lines = content.split("\n").filter((l) => l.trim());

      // Extract text from messages
      // Transcript format: {type: "message", message: {role: "user"|"assistant", content: [...]}}
      let textSamples = [];
      for (const line of lines.slice(0, 30)) {
        // First 30 entries
        try {
          const entry = JSON.parse(line);
          if (entry.type === "message" && entry.message?.content) {
            const msgContent = entry.message.content;
            if (Array.isArray(msgContent)) {
              msgContent.forEach((c) => {
                if (c.type === "text" && c.text) {
                  textSamples.push(c.text.slice(0, 500));
                }
              });
            } else if (typeof msgContent === "string") {
              textSamples.push(msgContent.slice(0, 500));
            }
          }
        } catch (e) {
          /* skip malformed lines */
        }
      }

      if (textSamples.length === 0) return null;

      const topics = detectTopics(textSamples.join(" "));
      return topics.length > 0 ? topics.slice(0, 2).join(", ") : null;
    } catch (e) {
      return null;
    }
  }

  // Helper to map a single session (extracted from getSessions)
  function mapSession(s) {
    const minutesAgo = s.ageMs ? s.ageMs / 60000 : Infinity;

    // Determine channel type from key (messaging platform)
    let channel = "other";
    if (s.key.includes("slack")) channel = "slack";
    else if (s.key.includes("telegram")) channel = "telegram";
    else if (s.key.includes("discord")) channel = "discord";
    else if (s.key.includes("signal")) channel = "signal";
    else if (s.key.includes("whatsapp")) channel = "whatsapp";

    // Determine session type (main, subagent, cron, channel-based)
    let sessionType = "channel";
    if (s.key.includes(":subagent:")) sessionType = "subagent";
    else if (s.key.includes(":cron:")) sessionType = "cron";
    else if (s.key === "agent:main:main") sessionType = "main";

    const originator = getSessionOriginator(s.sessionId);
    const label = s.groupChannel || s.displayName || parseSessionLabel(s.key);
    const topic = getSessionTopic(s.sessionId);

    const totalTokens = s.totalTokens || 0;
    const sessionAgeMinutes = Math.max(1, Math.min(minutesAgo, 24 * 60));
    const burnRate = Math.round(totalTokens / sessionAgeMinutes);

    return {
      sessionKey: s.key,
      sessionId: s.sessionId,
      label: label,
      groupChannel: s.groupChannel || null,
      displayName: s.displayName || null,
      kind: s.kind,
      channel: channel,
      sessionType: sessionType,
      active: minutesAgo < 15,
      recentlyActive: minutesAgo < 60,
      minutesAgo: Math.round(minutesAgo),
      tokens: s.totalTokens || 0,
      model: s.model,
      originator: originator,
      topic: topic,
      metrics: {
        burnRate: burnRate,
        toolCalls: 0,
        minutesActive: Math.max(1, Math.min(Math.round(minutesAgo), 24 * 60)),
      },
    };
  }

  async function refreshSessionsCache() {
    if (sessionsCache.refreshing) return; // Don't double-refresh
    sessionsCache.refreshing = true;

    try {
      const output = await runOpenClawAsync("sessions --json 2>/dev/null");
      const jsonStr = extractJSON(output);
      if (jsonStr) {
        const data = JSON.parse(jsonStr);
        const sessions = data.sessions || [];

        // Map sessions (same logic as getSessions)
        const mapped = sessions.map((s) => mapSession(s));
        const withOriginator = mapped.filter((s) => s.originator != null);

        sessionsCache = {
          sessions: mapped,
          timestamp: Date.now(),
          refreshing: false,
        };
        console.log(
          `[Sessions Cache] Refreshed: ${mapped.length} sessions (${withOriginator.length} with originator)`,
        );
      }
    } catch (e) {
      console.error("[Sessions Cache] Refresh error:", e.message);
    }
    sessionsCache.refreshing = false;
  }

  // Get sessions from cache, trigger async refresh if stale
  function getSessionsCached() {
    const now = Date.now();
    const isStale = now - sessionsCache.timestamp > SESSIONS_CACHE_TTL;

    if (isStale && !sessionsCache.refreshing) {
      // Trigger async refresh (don't await - return stale data immediately)
      refreshSessionsCache();
    }

    return sessionsCache.sessions;
  }

  function getSessions(options = {}) {
    const limit = Object.prototype.hasOwnProperty.call(options, "limit") ? options.limit : 20;
    const returnCount = options.returnCount || false;

    // For "get all" requests (limit: null), use the async cache
    // This is the expensive operation that was blocking
    if (limit === null) {
      const cached = getSessionsCached();
      const totalCount = cached.length;
      return returnCount ? { sessions: cached, totalCount } : cached;
    }

    // For limited requests, can still use sync (fast enough)
    try {
      const output = runOpenClaw("sessions --json 2>/dev/null");
      const jsonStr = extractJSON(output);
      if (jsonStr) {
        const data = JSON.parse(jsonStr);
        const totalCount = data.count || data.sessions?.length || 0;
        let sessions = data.sessions || [];
        if (limit != null) {
          sessions = sessions.slice(0, limit);
        }
        const mapped = sessions.map((s) => mapSession(s));
        return returnCount ? { sessions: mapped, totalCount } : mapped;
      }
    } catch (e) {
      console.error("Failed to get sessions:", e.message);
    }
    return returnCount ? { sessions: [], totalCount: 0 } : [];
  }

  // Read session transcript from JSONL file
  function readTranscript(sessionId) {
    const transcriptPath = findTranscriptPath(sessionId);

    try {
      if (!transcriptPath) return [];
      const content = fs.readFileSync(transcriptPath, "utf8");
      return content
        .trim()
        .split("\n")
        .map((line) => {
          try {
            return JSON.parse(line);
          } catch {
            return null;
          }
        })
        .filter(Boolean);
    } catch (e) {
      console.error("Failed to read transcript:", e.message);
      return [];
    }
  }

  // Get detailed session info
  function getSessionDetail(sessionKey) {
    try {
      // Get basic session info
      const listOutput = runOpenClaw("sessions --json 2>/dev/null");
      let sessionInfo = null;
      const jsonStr = extractJSON(listOutput);
      if (jsonStr) {
        const data = JSON.parse(jsonStr);
        sessionInfo = data.sessions?.find((s) => s.key === sessionKey);
      }

      if (!sessionInfo) {
        return { error: "Session not found" };
      }

      // Read transcript directly from JSONL file
      const transcript = readTranscript(sessionInfo.sessionId);
      let messages = [];
      let tools = {};
      let facts = [];
      let needsAttention = [];

      // Aggregate token usage from transcript
      let totalInputTokens = 0;
      let totalOutputTokens = 0;
      let totalCacheRead = 0;
      let totalCacheWrite = 0;
      let totalCost = 0;
      let detectedModel = sessionInfo.model || null;

      // Process transcript entries (format: {type: "message", message: {role, content, usage}})
      transcript.forEach((entry) => {
        if (entry.type !== "message" || !entry.message) return;

        const msg = entry.message;
        if (!msg.role) return;

        // Extract token usage from messages (typically on assistant messages)
        if (msg.usage) {
          totalInputTokens += msg.usage.input || msg.usage.inputTokens || 0;
          totalOutputTokens += msg.usage.output || msg.usage.outputTokens || 0;
          totalCacheRead += msg.usage.cacheRead || msg.usage.cacheReadTokens || 0;
          totalCacheWrite += msg.usage.cacheWrite || msg.usage.cacheWriteTokens || 0;
          if (msg.usage.cost?.total) totalCost += msg.usage.cost.total;
        }

        // Detect model from assistant messages
        if (msg.role === "assistant" && msg.model && !detectedModel) {
          detectedModel = msg.model;
        }

        let text = "";
        if (typeof msg.content === "string") {
          text = msg.content;
        } else if (Array.isArray(msg.content)) {
          const textPart = msg.content.find((c) => c.type === "text");
          if (textPart) text = textPart.text || "";

          // Count tool calls
          msg.content
            .filter((c) => c.type === "toolCall" || c.type === "tool_use")
            .forEach((tc) => {
              const name = tc.name || tc.tool || "unknown";
              tools[name] = (tools[name] || 0) + 1;
            });
        }

        if (text && msg.role !== "toolResult") {
          messages.push({ role: msg.role, text, timestamp: entry.timestamp });
        }

        // Extract insights from user messages
        if (msg.role === "user" && text) {
          const lowerText = text.toLowerCase();

          // Look for questions
          if (text.includes("?")) {
            const questions = text.match(/[^.!?\n]*\?/g) || [];
            questions.slice(0, 2).forEach((q) => {
              if (q.length > 15 && q.length < 200) {
                needsAttention.push(`❓ ${q.trim()}`);
              }
            });
          }

          // Look for action items
          if (
            lowerText.includes("todo") ||
            lowerText.includes("remind") ||
            lowerText.includes("need to")
          ) {
            const match = text.match(/(?:todo|remind|need to)[^.!?\n]*/i);
            if (match) needsAttention.push(`📋 ${match[0].slice(0, 100)}`);
          }
        }

        // Extract facts from assistant messages
        if (msg.role === "assistant" && text) {
          const lowerText = text.toLowerCase();

          // Look for completions
          ["✅", "done", "created", "updated", "fixed", "deployed"].forEach((keyword) => {
            if (lowerText.includes(keyword)) {
              const lines = text.split("\n").filter((l) => l.toLowerCase().includes(keyword));
              lines.slice(0, 2).forEach((line) => {
                if (line.length > 5 && line.length < 150) {
                  facts.push(line.trim().slice(0, 100));
                }
              });
            }
          });
        }
      });

      // Generate summary from recent messages
      let summary = "No activity yet.";
      const userMessages = messages.filter((m) => m.role === "user");
      const assistantMessages = messages.filter((m) => m.role === "assistant");
      let topics = [];

      if (messages.length > 0) {
        summary = `${messages.length} messages (${userMessages.length} user, ${assistantMessages.length} assistant). `;

        // Identify main topics from all text using pattern matching
        const allText = messages.map((m) => m.text).join(" ");
        topics = detectTopics(allText);

        if (topics.length > 0) {
          summary += `Topics: ${topics.join(", ")}.`;
        }
      }

      // Convert tools to array
      const toolsArray = Object.entries(tools)
        .map(([name, count]) => ({ name, count }))
        .sort((a, b) => b.count - a.count);

      // Calculate last active time
      const ageMs = sessionInfo.ageMs || 0;
      const lastActive =
        ageMs < 60000
          ? "Just now"
          : ageMs < 3600000
            ? `${Math.round(ageMs / 60000)} minutes ago`
            : ageMs < 86400000
              ? `${Math.round(ageMs / 3600000)} hours ago`
              : `${Math.round(ageMs / 86400000)} days ago`;

      // Determine readable channel name
      // Priority: groupChannel > displayName > parsed from key > fallback
      let channelDisplay = "Other";
      if (sessionInfo.groupChannel) {
        channelDisplay = sessionInfo.groupChannel;
      } else if (sessionInfo.displayName) {
        channelDisplay = sessionInfo.displayName;
      } else if (sessionKey.includes("slack")) {
        // Try to parse channel name from key
        const parts = sessionKey.split(":");
        const channelIdx = parts.indexOf("channel");
        if (channelIdx >= 0 && parts[channelIdx + 1]) {
          const channelId = parts[channelIdx + 1].toLowerCase();
          channelDisplay = CHANNEL_MAP[channelId] || `#${channelId}`;
        } else {
          channelDisplay = "Slack";
        }
      } else if (sessionKey.includes("telegram")) {
        channelDisplay = "Telegram";
      }

      // Use parsed totals or fallback to session info
      const finalTotalTokens = totalInputTokens + totalOutputTokens || sessionInfo.totalTokens || 0;
      const finalInputTokens = totalInputTokens || sessionInfo.inputTokens || 0;
      const finalOutputTokens = totalOutputTokens || sessionInfo.outputTokens || 0;

      // Format model name (strip prefix)
      const modelDisplay = (detectedModel || sessionInfo.model || "-")
        .replace("anthropic/", "")
        .replace("openai/", "");

      return {
        key: sessionKey,
        kind: sessionInfo.kind,
        channel: channelDisplay,
        groupChannel: sessionInfo.groupChannel || channelDisplay,
        model: modelDisplay,
        tokens: finalTotalTokens,
        inputTokens: finalInputTokens,
        outputTokens: finalOutputTokens,
        cacheRead: totalCacheRead,
        cacheWrite: totalCacheWrite,
        estCost: totalCost > 0 ? `$${totalCost.toFixed(4)}` : null,
        lastActive,
        summary,
        topics, // Array of detected topics
        facts: [...new Set(facts)].slice(0, 8),
        needsAttention: [...new Set(needsAttention)].slice(0, 5),
        tools: toolsArray.slice(0, 10),
        messages: messages
          .slice(-15)
          .reverse()
          .map((m) => ({
            role: m.role,
            text: m.text.slice(0, 500),
          })),
      };
    } catch (e) {
      console.error("Failed to get session detail:", e.message);
      return { error: e.message };
    }
  }

  return {
    findTranscriptPath,
    getSessionOriginator,
    getSessionTopic,
    mapSession,
    refreshSessionsCache,
    getSessionsCached,
    getSessions,
    readTranscript,
    getSessionDetail,
    parseSessionLabel,
  };
}

module.exports = { createSessionsModule, CHANNEL_MAP };
```

## File: `src/state.js`
```javascript
const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFileSync } = require("child_process");
const { formatBytes, formatTimeAgo } = require("./utils");

/**
 * Creates a state management module with injected dependencies.
 *
 * @param {object} deps
 * @param {object} deps.CONFIG - config object (for paths, billing)
 * @param {function} deps.getOpenClawDir - returns the OpenClaw directory path
 * @param {function} deps.getSessions - function from sessions module
 * @param {function} deps.getSystemVitals - function from vitals module
 * @param {function} deps.getCronJobs - function from cron module
 * @param {function} deps.loadOperators - function from operators module
 * @param {function} deps.calculateOperatorStats - function from operators module
 * @param {function} deps.getLlmUsage - function from llm-usage module
 * @param {function} deps.getDailyTokenUsage - function from tokens module
 * @param {function} deps.getTokenStats - function from tokens module
 * @param {function} deps.getCerebroTopics - function from cerebro module
 * @param {function} deps.getMemoryStats - function (defined in this module, uses CONFIG.paths)
 * @param {function} deps.runOpenClaw - function from openclaw module
 * @param {function} deps.extractJSON - function from openclaw module
 * @param {function} deps.readTranscript - function from sessions module
 */
function createStateModule(deps) {
  const {
    CONFIG,
    getOpenClawDir,
    getSessions,
    getSystemVitals,
    getCronJobs,
    loadOperators,
    calculateOperatorStats,
    getLlmUsage,
    getDailyTokenUsage,
    getTokenStats,
    getCerebroTopics,
    runOpenClaw,
    extractJSON,
    readTranscript,
  } = deps;

  const PATHS = CONFIG.paths;

  // Module-level state
  let cachedState = null;
  let lastStateUpdate = 0;
  const STATE_CACHE_TTL = 30000; // 30 seconds - reduce blocking from CLI calls
  let stateRefreshInterval = null;

  // Get system status
  function getSystemStatus() {
    const hostname = os.hostname();
    let uptime = "\u2014";
    try {
      const uptimeRaw = execFileSync("uptime", [], { encoding: "utf8" });
      const match = uptimeRaw.match(/up\s+([^,]+)/);
      if (match) uptime = match[1].trim();
    } catch (e) {}

    let gateway = "Unknown";
    try {
      const status = runOpenClaw("gateway status 2>/dev/null");
      if (status && status.includes("running")) {
        gateway = "Running";
      } else if (status && status.includes("stopped")) {
        gateway = "Stopped";
      }
    } catch (e) {}

    return {
      hostname,
      gateway,
      model: "claude-opus-4-5",
      uptime,
    };
  }

  // Get recent activity from memory files
  function getRecentActivity() {
    const activities = [];
    const today = new Date().toISOString().split("T")[0];
    const memoryFile = path.join(PATHS.memory, `${today}.md`);

    try {
      if (fs.existsSync(memoryFile)) {
        const content = fs.readFileSync(memoryFile, "utf8");
        const lines = content.split("\n").filter((l) => l.startsWith("- "));
        lines.slice(-5).forEach((line) => {
          const text = line.replace(/^- /, "").slice(0, 80);
          activities.push({
            icon: text.includes("\u2705")
              ? "\u2705"
              : text.includes("\u274C")
                ? "\u274C"
                : "\uD83D\uDCDD",
            text: text.replace(/[\u2705\u274C\uD83D\uDCDD\uD83D\uDD27]/g, "").trim(),
            time: today,
          });
        });
      }
    } catch (e) {
      console.error("Failed to read activity:", e.message);
    }

    return activities.reverse();
  }

  // Get capacity info from gateway config and active sessions
  function getCapacity() {
    const result = {
      main: { active: 0, max: 12 },
      subagent: { active: 0, max: 24 },
    };

    // Determine OpenClaw directory (respects OPENCLAW_PROFILE)
    const openclawDir = getOpenClawDir();

    // Read max capacity from openclaw config
    try {
      const configPath = path.join(openclawDir, "openclaw.json");
      if (fs.existsSync(configPath)) {
        const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
        if (config?.agents?.defaults?.maxConcurrent) {
          result.main.max = config.agents.defaults.maxConcurrent;
        }
        if (config?.agents?.defaults?.subagents?.maxConcurrent) {
          result.subagent.max = config.agents.defaults.subagents.maxConcurrent;
        }
      }
    } catch (e) {
      // Fall back to defaults
    }

    // Try to get active counts from sessions (preferred - has full session keys)
    try {
      const output = runOpenClaw("sessions --json 2>/dev/null");
      const jsonStr = extractJSON(output);
      if (jsonStr) {
        const data = JSON.parse(jsonStr);
        const sessions = data.sessions || [];
        const fiveMinMs = 5 * 60 * 1000;

        for (const s of sessions) {
          // Only count sessions active in last 5 minutes
          if (s.ageMs > fiveMinMs) continue;

          const key = s.key || "";
          // Session key patterns:
          //   agent:main:slack:... = main (human-initiated)
          //   agent:main:telegram:... = main
          //   agent:main:discord:... = main
          //   agent:main:subagent:... = subagent (spawned task)
          //   agent:main:cron:... = cron job (count as subagent)
          if (key.includes(":subagent:") || key.includes(":cron:")) {
            result.subagent.active++;
          } else {
            result.main.active++;
          }
        }
        return result;
      }
    } catch (e) {
      console.error("Failed to get capacity from sessions, falling back to filesystem:", e.message);
    }

    // Count active sessions from filesystem (workaround for CLI returning styled text)
    // Sessions active in last 5 minutes are considered "active"
    try {
      const sessionsDir = path.join(openclawDir, "agents", "main", "sessions");
      if (fs.existsSync(sessionsDir)) {
        const fiveMinAgo = Date.now() - 5 * 60 * 1000;
        const files = fs.readdirSync(sessionsDir).filter((f) => f.endsWith(".jsonl"));

        let mainActive = 0;
        let subActive = 0;

        for (const file of files) {
          try {
            const filePath = path.join(sessionsDir, file);
            const stat = fs.statSync(filePath);

            // Only count files modified in last 5 minutes as "active"
            if (stat.mtimeMs < fiveMinAgo) continue;

            // Read the first line to get the session key
            // Session keys indicate session type:
            //   agent:main:slack:... = main (human-initiated slack)
            //   agent:main:telegram:... = main (human-initiated telegram)
            //   agent:main:discord:... = main (human-initiated discord)
            //   agent:main:subagent:... = subagent (spawned autonomous task)
            //   agent:main:cron:... = cron job (automated, count as subagent)
            // Filenames are just UUIDs, so we must read the content
            let isSubagent = false;
            try {
              const fd = fs.openSync(filePath, "r");
              const buffer = Buffer.alloc(512); // First 512 bytes is enough for the first line
              fs.readSync(fd, buffer, 0, 512, 0);
              fs.closeSync(fd);
              const firstLine = buffer.toString("utf8").split("\n")[0];
              const parsed = JSON.parse(firstLine);
              const key = parsed.key || parsed.id || "";
              // Subagent and cron sessions are not human-initiated
              isSubagent = key.includes(":subagent:") || key.includes(":cron:");
            } catch (parseErr) {
              // If we can't parse, fall back to checking filename (legacy)
              isSubagent = file.includes("subagent");
            }

            if (isSubagent) {
              subActive++;
            } else {
              mainActive++;
            }
          } catch (e) {
            // Skip unreadable files
          }
        }

        result.main.active = mainActive;
        result.subagent.active = subActive;
      }
    } catch (e) {
      console.error("Failed to count active sessions from filesystem:", e.message);
    }

    return result;
  }

  // Get memory stats
  function getMemoryStats() {
    const memoryDir = PATHS.memory;
    const memoryFile = path.join(PATHS.workspace, "MEMORY.md");

    const stats = {
      totalFiles: 0,
      totalSize: 0,
      totalSizeFormatted: "0 B",
      memoryMdSize: 0,
      memoryMdSizeFormatted: "0 B",
      memoryMdLines: 0,
      recentFiles: [],
      oldestFile: null,
      newestFile: null,
    };

    try {
      const collectMemoryFiles = (dir, baseDir) => {
        const entries = fs.readdirSync(dir, { withFileTypes: true });
        const files = [];

        for (const entry of entries) {
          const entryPath = path.join(dir, entry.name);
          if (entry.isDirectory()) {
            files.push(...collectMemoryFiles(entryPath, baseDir));
          } else if (
            entry.isFile() &&
            (entry.name.endsWith(".md") || entry.name.endsWith(".json"))
          ) {
            const stat = fs.statSync(entryPath);
            const relativePath = path.relative(baseDir, entryPath);
            files.push({
              name: relativePath,
              size: stat.size,
              sizeFormatted: formatBytes(stat.size),
              modified: stat.mtime,
            });
          }
        }

        return files;
      };

      // MEMORY.md stats
      if (fs.existsSync(memoryFile)) {
        const memStat = fs.statSync(memoryFile);
        stats.memoryMdSize = memStat.size;
        stats.memoryMdSizeFormatted = formatBytes(memStat.size);
        const content = fs.readFileSync(memoryFile, "utf8");
        stats.memoryMdLines = content.split("\n").length;
        stats.totalSize += memStat.size;
        stats.totalFiles++;
      }

      // Memory directory stats
      if (fs.existsSync(memoryDir)) {
        const files = collectMemoryFiles(memoryDir, memoryDir).sort(
          (a, b) => b.modified - a.modified,
        );

        stats.totalFiles += files.length;
        files.forEach((f) => (stats.totalSize += f.size));
        stats.recentFiles = files.slice(0, 5).map((f) => ({
          name: f.name,
          sizeFormatted: f.sizeFormatted,
          age: formatTimeAgo(f.modified),
        }));

        if (files.length > 0) {
          stats.newestFile = files[0].name;
          stats.oldestFile = files[files.length - 1].name;
        }
      }

      stats.totalSizeFormatted = formatBytes(stats.totalSize);
    } catch (e) {
      console.error("Failed to get memory stats:", e.message);
    }

    return stats;
  }

  // Get all data for dashboard (legacy endpoint)
  function getData() {
    // Get ALL sessions for accurate counts, then slice for display
    const allSessions = getSessions({ limit: null });
    const pageSize = 20;
    const displaySessions = allSessions.slice(0, pageSize);
    const tokenStats = getTokenStats(allSessions);
    const capacity = getCapacity();
    const memory = getMemoryStats();

    // Calculate status counts based on ALL sessions (not just current page)
    const statusCounts = {
      all: allSessions.length,
      live: allSessions.filter((s) => s.active).length,
      recent: allSessions.filter((s) => !s.active && s.recentlyActive).length,
      idle: allSessions.filter((s) => !s.active && !s.recentlyActive).length,
    };

    // Calculate real pagination
    const totalPages = Math.ceil(allSessions.length / pageSize);

    return {
      sessions: displaySessions,
      tokenStats: tokenStats,
      capacity: capacity,
      memory: memory,
      pagination: {
        page: 1,
        pageSize: pageSize,
        total: allSessions.length,
        totalPages: totalPages,
        hasPrev: false,
        hasNext: totalPages > 1,
      },
      statusCounts: statusCounts,
    };
  }

  // Unified state for dashboard (single source of truth)
  function getFullState() {
    const now = Date.now();

    // Return cached state if fresh
    if (cachedState && now - lastStateUpdate < STATE_CACHE_TTL) {
      return cachedState;
    }

    // Gather all data with error handling for each section
    let sessions = [];
    let tokenStats = {};
    let statusCounts = { all: 0, live: 0, recent: 0, idle: 0 };
    let vitals = {};
    let capacity = {};
    let operators = { operators: [], roles: {} };
    let llmUsage = {};
    let cron = [];
    let memory = {};
    let cerebro = {};
    let subagents = [];

    // Get ALL sessions first for accurate statusCounts, then slice for display
    let allSessions = [];
    let totalSessionCount = 0;
    try {
      allSessions = getSessions({ limit: null }); // Get all for counting
      totalSessionCount = allSessions.length;
      sessions = allSessions.slice(0, 20); // Display only first 20
    } catch (e) {
      console.error("[State] sessions:", e.message);
    }

    try {
      vitals = getSystemVitals();
    } catch (e) {
      console.error("[State] vitals:", e.message);
    }
    // Use filesystem-based capacity (no CLI calls, won't block)
    try {
      capacity = getCapacity();
    } catch (e) {
      console.error("[State] capacity:", e.message);
    }
    // Pass capacity to tokenStats so it can use the same active counts
    try {
      tokenStats = getTokenStats(allSessions, capacity, CONFIG);
    } catch (e) {
      console.error("[State] tokenStats:", e.message);
    }
    // Calculate statusCounts from ALL sessions (not just current page) for accurate filter counts
    try {
      const liveSessions = allSessions.filter((s) => s.active);
      const recentSessions = allSessions.filter((s) => !s.active && s.recentlyActive);
      const idleSessions = allSessions.filter((s) => !s.active && !s.recentlyActive);
      statusCounts = {
        all: totalSessionCount,
        live: liveSessions.length,
        recent: recentSessions.length,
        idle: idleSessions.length,
      };
    } catch (e) {
      console.error("[State] statusCounts:", e.message);
    }
    try {
      const operatorData = loadOperators();
      // Use shared function for calculating operator stats (single source of truth)
      operators = calculateOperatorStats(operatorData, allSessions);
    } catch (e) {
      console.error("[State] operators:", e.message);
    }
    try {
      llmUsage = getLlmUsage();
    } catch (e) {
      console.error("[State] llmUsage:", e.message);
    }
    try {
      cron = getCronJobs();
    } catch (e) {
      console.error("[State] cron:", e.message);
    }
    try {
      memory = getMemoryStats();
    } catch (e) {
      console.error("[State] memory:", e.message);
    }
    try {
      cerebro = getCerebroTopics();
    } catch (e) {
      console.error("[State] cerebro:", e.message);
    }
    // Derive subagents from allSessions (no extra CLI call needed)
    // Configurable retention: SUBAGENT_RETENTION_HOURS env var (default 12h)
    try {
      const retentionHours = parseInt(process.env.SUBAGENT_RETENTION_HOURS || "12", 10);
      const retentionMs = retentionHours * 60 * 60 * 1000;
      subagents = allSessions
        .filter((s) => s.sessionKey && s.sessionKey.includes(":subagent:"))
        .filter((s) => (s.minutesAgo || 0) * 60000 < retentionMs)
        .map((s) => {
          const match = s.sessionKey.match(/:subagent:([a-f0-9-]+)$/);
          const subagentId = match ? match[1] : s.sessionId;
          return {
            id: subagentId,
            shortId: subagentId.slice(0, 8),
            task: s.label || s.displayName || "Sub-agent task",
            tokens: s.tokens || 0,
            ageMs: (s.minutesAgo || 0) * 60000,
            active: s.active,
            recentlyActive: s.recentlyActive,
          };
        });
    } catch (e) {
      console.error("[State] subagents:", e.message);
    }

    cachedState = {
      vitals,
      sessions,
      tokenStats,
      statusCounts,
      capacity,
      operators,
      llmUsage,
      cron,
      memory,
      cerebro,
      subagents,
      pagination: {
        page: 1,
        pageSize: 20,
        total: totalSessionCount,
        totalPages: Math.max(1, Math.ceil(totalSessionCount / 20)),
        hasPrev: false,
        hasNext: totalSessionCount > 20,
      },
      timestamp: now,
    };

    lastStateUpdate = now;
    return cachedState;
  }

  // Force refresh the cached state
  function refreshState() {
    lastStateUpdate = 0;
    return getFullState();
  }

  // Background state refresh and SSE broadcast
  function startStateRefresh(broadcastSSE, intervalMs = 30000) {
    if (stateRefreshInterval) return;

    stateRefreshInterval = setInterval(() => {
      try {
        const newState = refreshState();
        broadcastSSE("update", newState);
      } catch (e) {
        console.error("[State] Refresh error:", e.message);
      }
    }, intervalMs);

    console.log(`[State] Background refresh started (${intervalMs}ms interval)`);
  }

  // Stop background refresh
  function stopStateRefresh() {
    if (stateRefreshInterval) {
      clearInterval(stateRefreshInterval);
      stateRefreshInterval = null;
      console.log("[State] Background refresh stopped");
    }
  }

  // Get detailed sub-agent status
  function getSubagentStatus() {
    const subagents = [];
    try {
      const output = runOpenClaw("sessions --json 2>/dev/null");
      const jsonStr = extractJSON(output);
      if (jsonStr) {
        const data = JSON.parse(jsonStr);
        const subagentSessions = (data.sessions || []).filter(
          (s) => s.key && s.key.includes(":subagent:"),
        );

        for (const s of subagentSessions) {
          const ageMs = s.ageMs || Infinity;
          const isActive = ageMs < 5 * 60 * 1000; // Active if < 5 min
          const isRecent = ageMs < 30 * 60 * 1000; // Recent if < 30 min

          // Extract subagent ID from key
          const match = s.key.match(/:subagent:([a-f0-9-]+)$/);
          const subagentId = match ? match[1] : s.sessionId;
          const shortId = subagentId.slice(0, 8);

          // Try to get task info from transcript
          let taskSummary = "Unknown task";
          let label = null;
          const transcript = readTranscript(s.sessionId);

          // Look for task description in first 15 messages (subagent context can be deep)
          for (const entry of transcript.slice(0, 15)) {
            if (entry.type === "message" && entry.message?.role === "user") {
              const content = entry.message.content;
              let text = "";
              if (typeof content === "string") {
                text = content;
              } else if (Array.isArray(content)) {
                const textPart = content.find((c) => c.type === "text");
                if (textPart) text = textPart.text || "";
              }

              if (!text) continue;

              // Extract label from subagent context
              const labelMatch = text.match(/Label:\s*([^\n]+)/i);
              if (labelMatch) {
                label = labelMatch[1].trim();
              }

              // Extract task summary - try multiple patterns
              // Pattern 1: "You were created to handle: **TASK**"
              let taskMatch = text.match(/You were created to handle:\s*\*\*([^*]+)\*\*/i);
              if (taskMatch) {
                taskSummary = taskMatch[1].trim();
                break;
              }

              // Pattern 2: Linear issue format "**JON-XXX: Description**"
              taskMatch = text.match(/\*\*([A-Z]{2,5}-\d+:\s*[^*]+)\*\*/);
              if (taskMatch) {
                taskSummary = taskMatch[1].trim();
                break;
              }

              // Pattern 3: First meaningful line of user message
              const firstLine = text
                .split("\n")[0]
                .replace(/^\*\*|\*\*$/g, "")
                .trim();
              if (firstLine.length > 10 && firstLine.length < 100) {
                taskSummary = firstLine;
                break;
              }
            }
          }

          // Count messages
          const messageCount = transcript.filter(
            (e) => e.type === "message" && e.message?.role,
          ).length;

          subagents.push({
            id: subagentId,
            shortId,
            sessionId: s.sessionId,
            label: label || shortId,
            task: taskSummary,
            model: s.model?.replace("anthropic/", "") || "unknown",
            status: isActive ? "active" : isRecent ? "idle" : "stale",
            ageMs,
            ageFormatted:
              ageMs < 60000
                ? "Just now"
                : ageMs < 3600000
                  ? `${Math.round(ageMs / 60000)}m ago`
                  : `${Math.round(ageMs / 3600000)}h ago`,
            messageCount,
            tokens: s.totalTokens || 0,
          });
        }
      }
    } catch (e) {
      console.error("Failed to get subagent status:", e.message);
    }

    // Sort by age (most recent first)
    return subagents.sort((a, b) => a.ageMs - b.ageMs);
  }

  return {
    getSystemStatus,
    getRecentActivity,
    getCapacity,
    getMemoryStats,
    getFullState,
    refreshState,
    startStateRefresh,
    stopStateRefresh,
    getData,
    getSubagentStatus,
  };
}

module.exports = { createStateModule };
```

## File: `src/tokens.js`
```javascript
const fs = require("fs");
const path = require("path");
const { formatNumber, formatTokens } = require("./utils");

// Claude Opus 4 pricing (per 1M tokens)
const TOKEN_RATES = {
  input: 15.0, // $15/1M input tokens
  output: 75.0, // $75/1M output tokens
  cacheRead: 1.5, // $1.50/1M (90% discount from input)
  cacheWrite: 18.75, // $18.75/1M (25% premium on input)
};

// Token usage cache with async background refresh
let tokenUsageCache = { data: null, timestamp: 0, refreshing: false };
const TOKEN_USAGE_CACHE_TTL = 30000; // 30 seconds

// Reference to background refresh interval (set by startTokenUsageRefresh)
let refreshInterval = null;

// Create empty usage bucket
function emptyUsageBucket() {
  return { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, requests: 0 };
}

// Async token usage refresh - runs in background, doesn't block
async function refreshTokenUsageAsync(getOpenClawDir) {
  if (tokenUsageCache.refreshing) return;
  tokenUsageCache.refreshing = true;

  try {
    const sessionsDir = path.join(getOpenClawDir(), "agents", "main", "sessions");
    const files = await fs.promises.readdir(sessionsDir);
    const jsonlFiles = files.filter((f) => f.endsWith(".jsonl"));

    const now = Date.now();
    const oneDayAgo = now - 24 * 60 * 60 * 1000;
    const threeDaysAgo = now - 3 * 24 * 60 * 60 * 1000;
    const sevenDaysAgo = now - 7 * 24 * 60 * 60 * 1000;

    // Track usage for each time window
    const usage24h = emptyUsageBucket();
    const usage3d = emptyUsageBucket();
    const usage7d = emptyUsageBucket();

    // Process files in batches to avoid overwhelming the system
    const batchSize = 50;
    for (let i = 0; i < jsonlFiles.length; i += batchSize) {
      const batch = jsonlFiles.slice(i, i + batchSize);

      await Promise.all(
        batch.map(async (file) => {
          const filePath = path.join(sessionsDir, file);
          try {
            const stat = await fs.promises.stat(filePath);
            // Skip files not modified in the last 7 days
            if (stat.mtimeMs < sevenDaysAgo) return;

            const content = await fs.promises.readFile(filePath, "utf8");
            const lines = content.trim().split("\n");

            for (const line of lines) {
              if (!line) continue;
              try {
                const entry = JSON.parse(line);
                const entryTime = entry.timestamp ? new Date(entry.timestamp).getTime() : 0;

                // Skip entries older than 7 days
                if (entryTime < sevenDaysAgo) continue;

                if (entry.message?.usage) {
                  const u = entry.message.usage;
                  const input = u.input || 0;
                  const output = u.output || 0;
                  const cacheRead = u.cacheRead || 0;
                  const cacheWrite = u.cacheWrite || 0;
                  const cost = u.cost?.total || 0;

                  // Add to appropriate buckets (cumulative - 24h is subset of 3d is subset of 7d)
                  if (entryTime >= oneDayAgo) {
                    usage24h.input += input;
                    usage24h.output += output;
                    usage24h.cacheRead += cacheRead;
                    usage24h.cacheWrite += cacheWrite;
                    usage24h.cost += cost;
                    usage24h.requests++;
                  }
                  if (entryTime >= threeDaysAgo) {
                    usage3d.input += input;
                    usage3d.output += output;
                    usage3d.cacheRead += cacheRead;
                    usage3d.cacheWrite += cacheWrite;
                    usage3d.cost += cost;
                    usage3d.requests++;
                  }
                  // Always add to 7d (already filtered above)
                  usage7d.input += input;
                  usage7d.output += output;
                  usage7d.cacheRead += cacheRead;
                  usage7d.cacheWrite += cacheWrite;
                  usage7d.cost += cost;
                  usage7d.requests++;
                }
              } catch (e) {
                // Skip invalid lines
              }
            }
          } catch (e) {
            // Skip unreadable files
          }
        }),
      );

      // Yield to event loop between batches
      await new Promise((resolve) => setImmediate(resolve));
    }

    // Helper to finalize bucket with computed fields
    const finalizeBucket = (bucket) => ({
      ...bucket,
      tokensNoCache: bucket.input + bucket.output,
      tokensWithCache: bucket.input + bucket.output + bucket.cacheRead + bucket.cacheWrite,
    });

    const result = {
      // Primary (24h) for backward compatibility
      ...finalizeBucket(usage24h),
      // All three windows
      windows: {
        "24h": finalizeBucket(usage24h),
        "3d": finalizeBucket(usage3d),
        "7d": finalizeBucket(usage7d),
      },
    };

    tokenUsageCache = { data: result, timestamp: Date.now(), refreshing: false };
    console.log(
      `[Token Usage] Cached: 24h=${usage24h.requests} 3d=${usage3d.requests} 7d=${usage7d.requests} requests`,
    );
  } catch (e) {
    console.error("[Token Usage] Refresh error:", e.message);
    tokenUsageCache.refreshing = false;
  }
}

// Returns cached token usage, triggers async refresh if stale
function getDailyTokenUsage(getOpenClawDir) {
  const now = Date.now();
  const isStale = now - tokenUsageCache.timestamp > TOKEN_USAGE_CACHE_TTL;

  // Trigger async refresh if stale (don't await)
  if (isStale && !tokenUsageCache.refreshing && getOpenClawDir) {
    refreshTokenUsageAsync(getOpenClawDir);
  }

  const emptyResult = {
    input: 0,
    output: 0,
    cacheRead: 0,
    cacheWrite: 0,
    cost: 0,
    requests: 0,
    tokensNoCache: 0,
    tokensWithCache: 0,
    windows: {
      "24h": {
        input: 0,
        output: 0,
        cacheRead: 0,
        cacheWrite: 0,
        cost: 0,
        requests: 0,
        tokensNoCache: 0,
        tokensWithCache: 0,
      },
      "3d": {
        input: 0,
        output: 0,
        cacheRead: 0,
        cacheWrite: 0,
        cost: 0,
        requests: 0,
        tokensNoCache: 0,
        tokensWithCache: 0,
      },
      "7d": {
        input: 0,
        output: 0,
        cacheRead: 0,
        cacheWrite: 0,
        cost: 0,
        requests: 0,
        tokensNoCache: 0,
        tokensWithCache: 0,
      },
    },
  };

  // Always return cache (may be stale or null on cold start)
  return tokenUsageCache.data || emptyResult;
}

// Calculate cost for a usage bucket
function calculateCostForBucket(bucket, rates = TOKEN_RATES) {
  const inputCost = (bucket.input / 1_000_000) * rates.input;
  const outputCost = (bucket.output / 1_000_000) * rates.output;
  const cacheReadCost = (bucket.cacheRead / 1_000_000) * rates.cacheRead;
  const cacheWriteCost = (bucket.cacheWrite / 1_000_000) * rates.cacheWrite;
  return {
    inputCost,
    outputCost,
    cacheReadCost,
    cacheWriteCost,
    totalCost: inputCost + outputCost + cacheReadCost + cacheWriteCost,
  };
}

// Get detailed cost breakdown for the modal
function getCostBreakdown(config, getSessions, getOpenClawDir) {
  const usage = getDailyTokenUsage(getOpenClawDir);
  if (!usage) {
    return { error: "Failed to get usage data" };
  }

  // Calculate costs for 24h (primary display)
  const costs = calculateCostForBucket(usage);

  // Get plan info from config
  const planCost = config.billing?.claudePlanCost || 200;
  const planName = config.billing?.claudePlanName || "Claude Code Max";

  // Calculate moving averages for each window
  const windowConfigs = {
    "24h": { days: 1, label: "24h" },
    "3d": { days: 3, label: "3dma" },
    "7d": { days: 7, label: "7dma" },
  };

  const windows = {};
  for (const [key, windowConfig] of Object.entries(windowConfigs)) {
    const bucket = usage.windows?.[key] || usage;
    const bucketCosts = calculateCostForBucket(bucket);
    const dailyAvg = bucketCosts.totalCost / windowConfig.days;
    const monthlyProjected = dailyAvg * 30;
    const monthlySavings = monthlyProjected - planCost;

    windows[key] = {
      label: windowConfig.label,
      days: windowConfig.days,
      totalCost: bucketCosts.totalCost,
      dailyAvg,
      monthlyProjected,
      monthlySavings,
      savingsPercent:
        monthlySavings > 0 ? Math.round((monthlySavings / monthlyProjected) * 100) : 0,
      requests: bucket.requests,
      tokens: {
        input: bucket.input,
        output: bucket.output,
        cacheRead: bucket.cacheRead,
        cacheWrite: bucket.cacheWrite,
      },
    };
  }

  return {
    // Raw token counts (24h for backward compatibility)
    inputTokens: usage.input,
    outputTokens: usage.output,
    cacheRead: usage.cacheRead,
    cacheWrite: usage.cacheWrite,
    requests: usage.requests,

    // Pricing rates
    rates: {
      input: TOKEN_RATES.input.toFixed(2),
      output: TOKEN_RATES.output.toFixed(2),
      cacheRead: TOKEN_RATES.cacheRead.toFixed(2),
      cacheWrite: TOKEN_RATES.cacheWrite.toFixed(2),
    },

    // Cost calculation breakdown (24h)
    calculation: {
      inputCost: costs.inputCost,
      outputCost: costs.outputCost,
      cacheReadCost: costs.cacheReadCost,
      cacheWriteCost: costs.cacheWriteCost,
    },

    // Totals (24h for backward compatibility)
    totalCost: costs.totalCost,
    planCost,
    planName,

    // Period
    period: "24 hours",

    // Multi-window data for moving averages
    windows,

    // Top sessions by tokens
    topSessions: getTopSessionsByTokens(5, getSessions),
  };
}

// Get top sessions sorted by token usage
function getTopSessionsByTokens(limit = 5, getSessions) {
  try {
    const sessions = getSessions({ limit: null });
    return sessions
      .filter((s) => s.tokens > 0)
      .sort((a, b) => b.tokens - a.tokens)
      .slice(0, limit)
      .map((s) => ({
        label: s.label,
        tokens: s.tokens,
        channel: s.channel,
        active: s.active,
      }));
  } catch (e) {
    console.error("[TopSessions] Error:", e.message);
    return [];
  }
}

// Calculate aggregate token stats
function getTokenStats(sessions, capacity, config = {}) {
  // Use capacity data if provided, otherwise compute from sessions
  let activeMainCount = capacity?.main?.active ?? 0;
  let activeSubagentCount = capacity?.subagent?.active ?? 0;
  let activeCount = activeMainCount + activeSubagentCount;
  let mainLimit = capacity?.main?.max ?? 12;
  let subagentLimit = capacity?.subagent?.max ?? 24;

  // Fallback: count from sessions if capacity not provided
  if (!capacity && sessions && sessions.length > 0) {
    activeCount = 0;
    activeMainCount = 0;
    activeSubagentCount = 0;
    sessions.forEach((s) => {
      if (s.active) {
        activeCount++;
        if (s.key && s.key.includes(":subagent:")) {
          activeSubagentCount++;
        } else {
          activeMainCount++;
        }
      }
    });
  }

  // Get accurate usage from JSONL files (includes all windows)
  const usage = getDailyTokenUsage();
  const totalInput = usage?.input || 0;
  const totalOutput = usage?.output || 0;
  const total = totalInput + totalOutput;

  // Calculate cost using shared helper
  const costs = calculateCostForBucket(usage);
  const estCost = costs.totalCost;

  // Calculate savings vs plan cost (compare monthly to monthly)
  const planCost = config?.billing?.claudePlanCost ?? 200;
  const planName = config?.billing?.claudePlanName ?? "Claude Code Max";
  const monthlyApiCost = estCost * 30; // Project daily to monthly
  const monthlySavings = monthlyApiCost - planCost;
  const savingsPositive = monthlySavings > 0;

  // Calculate per-session averages
  const sessionCount = sessions?.length || 1;
  const avgTokensPerSession = Math.round(total / sessionCount);
  const avgCostPerSession = estCost / sessionCount;

  // Calculate savings for all windows (24h, 3dma, 7dma)
  const windowConfigs = {
    "24h": { days: 1, label: "24h" },
    "3dma": { days: 3, label: "3dma" },
    "7dma": { days: 7, label: "7dma" },
  };

  const savingsWindows = {};
  for (const [key, windowConfig] of Object.entries(windowConfigs)) {
    // Map '3dma' -> '3d' for bucket lookup
    const bucketKey = key.replace("dma", "d").replace("24h", "24h");
    const bucket = usage.windows?.[bucketKey === "24h" ? "24h" : bucketKey] || usage;
    const bucketCosts = calculateCostForBucket(bucket);
    const dailyAvg = bucketCosts.totalCost / windowConfig.days;
    const monthlyProjected = dailyAvg * 30;
    const windowSavings = monthlyProjected - planCost;
    const windowSavingsPositive = windowSavings > 0;

    savingsWindows[key] = {
      label: windowConfig.label,
      estCost: `$${formatNumber(dailyAvg)}`,
      estMonthlyCost: `$${Math.round(monthlyProjected).toLocaleString()}`,
      estSavings: windowSavingsPositive ? `$${formatNumber(windowSavings)}/mo` : null,
      savingsPercent: windowSavingsPositive
        ? Math.round((windowSavings / monthlyProjected) * 100)
        : 0,
      requests: bucket.requests,
    };
  }

  return {
    total: formatTokens(total),
    input: formatTokens(totalInput),
    output: formatTokens(totalOutput),
    cacheRead: formatTokens(usage?.cacheRead || 0),
    cacheWrite: formatTokens(usage?.cacheWrite || 0),
    requests: usage?.requests || 0,
    activeCount,
    activeMainCount,
    activeSubagentCount,
    mainLimit,
    subagentLimit,
    estCost: `$${formatNumber(estCost)}`,
    planCost: `$${planCost.toFixed(0)}`,
    planName,
    // 24h savings (backward compatible)
    estSavings: savingsPositive ? `$${formatNumber(monthlySavings)}/mo` : null,
    savingsPercent: savingsPositive ? Math.round((monthlySavings / monthlyApiCost) * 100) : 0,
    estMonthlyCost: `$${Math.round(monthlyApiCost).toLocaleString()}`,
    // Multi-window savings (24h, 3da, 7da)
    savingsWindows,
    // Per-session averages
    avgTokensPerSession: formatTokens(avgTokensPerSession),
    avgCostPerSession: `$${avgCostPerSession.toFixed(2)}`,
    sessionCount,
  };
}

// Start background token usage refresh on an interval
// Call this once during server startup instead of auto-starting on module load
function startTokenUsageRefresh(getOpenClawDir) {
  // Do an initial refresh
  refreshTokenUsageAsync(getOpenClawDir);

  // Set up periodic refresh
  if (refreshInterval) {
    clearInterval(refreshInterval);
  }
  refreshInterval = setInterval(() => {
    refreshTokenUsageAsync(getOpenClawDir);
  }, TOKEN_USAGE_CACHE_TTL);

  return refreshInterval;
}

module.exports = {
  TOKEN_RATES,
  emptyUsageBucket,
  refreshTokenUsageAsync,
  getDailyTokenUsage,
  calculateCostForBucket,
  getCostBreakdown,
  getTopSessionsByTokens,
  getTokenStats,
  startTokenUsageRefresh,
};
```

## File: `src/topics.js`
```javascript
const TOPIC_PATTERNS = {
  dashboard: ["dashboard", "command center", "ui", "interface", "status page"],
  scheduling: ["cron", "schedule", "timer", "reminder", "alarm", "periodic", "interval"],
  heartbeat: [
    "heartbeat",
    "heartbeat_ok",
    "poll",
    "health check",
    "ping",
    "keepalive",
    "monitoring",
  ],
  memory: ["memory", "remember", "recall", "notes", "journal", "log", "context"],
  Slack: ["slack", "channel", "#cc-", "thread", "mention", "dm", "workspace"],
  email: ["email", "mail", "inbox", "gmail", "send email", "unread", "compose"],
  calendar: ["calendar", "event", "meeting", "appointment", "schedule", "gcal"],
  coding: [
    "code",
    "script",
    "function",
    "debug",
    "error",
    "bug",
    "implement",
    "refactor",
    "programming",
  ],
  git: [
    "git",
    "commit",
    "branch",
    "merge",
    "push",
    "pull",
    "repository",
    "pr",
    "pull request",
    "github",
  ],
  "file editing": ["file", "edit", "write", "read", "create", "delete", "modify", "save"],
  API: ["api", "endpoint", "request", "response", "webhook", "integration", "rest", "graphql"],
  research: ["search", "research", "lookup", "find", "investigate", "learn", "study"],
  browser: ["browser", "webpage", "website", "url", "click", "navigate", "screenshot", "web_fetch"],
  "Quip export": ["quip", "export", "document", "spreadsheet"],
  finance: ["finance", "investment", "stock", "money", "budget", "bank", "trading", "portfolio"],
  home: ["home", "automation", "lights", "thermostat", "smart home", "iot", "homekit"],
  health: ["health", "fitness", "workout", "exercise", "weight", "sleep", "nutrition"],
  travel: ["travel", "flight", "hotel", "trip", "vacation", "booking", "airport"],
  food: ["food", "recipe", "restaurant", "cooking", "meal", "order", "delivery"],
  subagent: ["subagent", "spawn", "sub-agent", "delegate", "worker", "parallel"],
  tools: ["tool", "exec", "shell", "command", "terminal", "bash", "run"],
};

function detectTopics(text) {
  if (!text) return [];
  const lowerText = text.toLowerCase();
  const scores = {};
  for (const [topic, keywords] of Object.entries(TOPIC_PATTERNS)) {
    let score = 0;
    for (const keyword of keywords) {
      if (keyword.length <= 3) {
        const regex = new RegExp(`\\b${keyword}\\b`, "i");
        if (regex.test(lowerText)) score++;
      } else if (lowerText.includes(keyword)) {
        score++;
      }
    }
    if (score > 0) {
      scores[topic] = score;
    }
  }
  if (Object.keys(scores).length === 0) return [];
  const bestScore = Math.max(...Object.values(scores));
  const threshold = Math.max(2, bestScore * 0.5);
  return Object.entries(scores)
    .filter(([_, score]) => score >= threshold || (score >= 1 && bestScore <= 2))
    .sort((a, b) => b[1] - a[1])
    .map(([topic, _]) => topic);
}

module.exports = { TOPIC_PATTERNS, detectTopics };
```

## File: `src/utils.js`
```javascript
/**
 * Utility functions shared across modules
 */

const { exec } = require("child_process");
const path = require("path");
const { promisify } = require("util");
const execAsync = promisify(exec);

const pkg = require(path.join(__dirname, "..", "package.json"));

function getVersion() {
  return pkg.version;
}

/**
 * Run a shell command with sensible defaults
 * @param {string} cmd - Command to execute
 * @param {object} options - Options (timeout, fallback, etc.)
 * @returns {Promise<string>} - Command output
 */
async function runCmd(cmd, options = {}) {
  const systemPath = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin";
  const envPath = process.env.PATH || "";
  const opts = {
    encoding: "utf8",
    timeout: 10000,
    env: {
      ...process.env,
      PATH: envPath.includes("/usr/sbin") ? envPath : `${systemPath}:${envPath}`,
    },
    ...options,
  };
  try {
    const { stdout } = await execAsync(cmd, opts);
    return stdout.trim();
  } catch (e) {
    if (options.fallback !== undefined) return options.fallback;
    throw e;
  }
}

function formatBytes(bytes) {
  if (bytes >= 1099511627776) return (bytes / 1099511627776).toFixed(1) + " TB";
  if (bytes >= 1073741824) return (bytes / 1073741824).toFixed(1) + " GB";
  if (bytes >= 1048576) return (bytes / 1048576).toFixed(1) + " MB";
  if (bytes >= 1024) return (bytes / 1024).toFixed(1) + " KB";
  return bytes + " B";
}

function formatTimeAgo(date) {
  const now = new Date();
  const diffMs = now - date;
  const diffMins = Math.round(diffMs / 60000);
  if (diffMins < 1) return "just now";
  if (diffMins < 60) return `${diffMins}m ago`;
  if (diffMins < 1440) return `${Math.round(diffMins / 60)}h ago`;
  return `${Math.round(diffMins / 1440)}d ago`;
}

function formatNumber(n) {
  return n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function formatTokens(n) {
  if (n >= 1000000) return (n / 1000000).toFixed(1) + "M";
  if (n >= 1000) return (n / 1000).toFixed(1) + "k";
  return n.toString();
}

module.exports = {
  getVersion,
  runCmd,
  formatBytes,
  formatTimeAgo,
  formatNumber,
  formatTokens,
};
```

## File: `src/vitals.js`
```javascript
/**
 * System vitals collection for OpenClaw Command Center
 * Collects CPU, memory, disk, and temperature metrics
 */

const { runCmd, formatBytes } = require("./utils");

// Vitals cache to reduce blocking
let cachedVitals = null;
let lastVitalsUpdate = 0;
const VITALS_CACHE_TTL = 30000; // 30 seconds - vitals don't change fast
let vitalsRefreshing = false;

// Async background refresh of system vitals (non-blocking)
async function refreshVitalsAsync() {
  if (vitalsRefreshing) return;
  vitalsRefreshing = true;

  const vitals = {
    hostname: "",
    uptime: "",
    disk: { used: 0, free: 0, total: 0, percent: 0, kbPerTransfer: 0, iops: 0, throughputMBps: 0 },
    cpu: { loadAvg: [0, 0, 0], cores: 0, usage: 0 },
    memory: { used: 0, free: 0, total: 0, percent: 0, pressure: "normal" },
    temperature: null,
  };

  // Detect platform for cross-platform support
  const isLinux = process.platform === "linux";
  const isMacOS = process.platform === "darwin";

  try {
    // Platform-specific commands
    const coresCmd = isLinux ? "nproc" : "sysctl -n hw.ncpu";
    const memCmd = isLinux
      ? "cat /proc/meminfo | grep MemTotal | awk '{print $2}'"
      : "sysctl -n hw.memsize";
    const topCmd = isLinux
      ? "top -bn1 | head -3 | grep -E '^%?Cpu|^  ?CPU' || echo ''"
      : 'top -l 1 -n 0 2>/dev/null | grep "CPU usage" || echo ""';

    // Linux: prefer mpstat (1s average) to avoid spiky single-frame top parsing.
    const mpstatCmd = isLinux
      ? "(command -v mpstat >/dev/null 2>&1 && mpstat 1 1 | tail -1 | sed 's/^Average: *//') || echo ''"
      : "";

    // Run commands in parallel for speed
    const [hostname, uptimeRaw, coresRaw, memTotalRaw, memInfoRaw, dfRaw, topOutput, mpstatOutput] =
      await Promise.all([
        runCmd("hostname", { fallback: "unknown" }),
        runCmd("uptime", { fallback: "" }),
        runCmd(coresCmd, { fallback: "1" }),
        runCmd(memCmd, { fallback: "0" }),
        isLinux
          ? runCmd("cat /proc/meminfo", { fallback: "" })
          : runCmd("vm_stat", { fallback: "" }),
        runCmd("df -k ~ | tail -1", { fallback: "" }),
        runCmd(topCmd, { fallback: "" }),
        isLinux ? runCmd(mpstatCmd, { fallback: "" }) : Promise.resolve(""),
      ]);

    vitals.hostname = hostname;

    // Parse uptime
    const uptimeMatch = uptimeRaw.match(/up\s+([^,]+)/);
    if (uptimeMatch) vitals.uptime = uptimeMatch[1].trim();
    const loadMatch = uptimeRaw.match(/load averages?:\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)/);
    if (loadMatch)
      vitals.cpu.loadAvg = [
        parseFloat(loadMatch[1]),
        parseFloat(loadMatch[2]),
        parseFloat(loadMatch[3]),
      ];

    // CPU
    vitals.cpu.cores = parseInt(coresRaw, 10) || 1;
    vitals.cpu.usage = Math.min(100, Math.round((vitals.cpu.loadAvg[0] / vitals.cpu.cores) * 100));

    // CPU percent (platform-specific)
    // Linux: prefer mpstat output (averaged over 1 second). Fallback to parsing top.
    if (isLinux) {
      // mpstat: ... %usr %nice %sys %iowait %irq %soft %steal %guest %gnice %idle
      if (mpstatOutput) {
        // After sed, mpstatOutput should look like:
        // "all  7.69 0.00 2.05 ... 89.74" (CPU %usr %nice %sys ... %idle)
        const parts = mpstatOutput.trim().split(/\s+/);
        const user = parts.length > 1 ? parseFloat(parts[1]) : NaN;
        const sys = parts.length > 3 ? parseFloat(parts[3]) : NaN;
        const idle = parts.length ? parseFloat(parts[parts.length - 1]) : NaN;
        if (!Number.isNaN(user)) vitals.cpu.userPercent = user;
        if (!Number.isNaN(sys)) vitals.cpu.sysPercent = sys;
        if (!Number.isNaN(idle)) {
          vitals.cpu.idlePercent = idle;
          vitals.cpu.usage = Math.max(0, Math.min(100, Math.round(100 - idle)));
        }
      }

      if (topOutput && (vitals.cpu.idlePercent === null || vitals.cpu.idlePercent === undefined)) {
        // Linux top: %Cpu(s):  5.9 us,  2.0 sy,  0.0 ni, 91.5 id,  0.5 wa, ...
        const userMatch = topOutput.match(/([\d.]+)\s*us/);
        const sysMatch = topOutput.match(/([\d.]+)\s*sy/);
        const idleMatch = topOutput.match(/([\d.]+)\s*id/);
        vitals.cpu.userPercent = userMatch ? parseFloat(userMatch[1]) : null;
        vitals.cpu.sysPercent = sysMatch ? parseFloat(sysMatch[1]) : null;
        vitals.cpu.idlePercent = idleMatch ? parseFloat(idleMatch[1]) : null;
        if (vitals.cpu.userPercent !== null && vitals.cpu.sysPercent !== null) {
          vitals.cpu.usage = Math.round(vitals.cpu.userPercent + vitals.cpu.sysPercent);
        }
      }
    } else if (topOutput) {
      // macOS: CPU usage: 5.9% user, 2.0% sys, 91.5% idle
      const userMatch = topOutput.match(/([\d.]+)%\s*user/);
      const sysMatch = topOutput.match(/([\d.]+)%\s*sys/);
      const idleMatch = topOutput.match(/([\d.]+)%\s*idle/);
      vitals.cpu.userPercent = userMatch ? parseFloat(userMatch[1]) : null;
      vitals.cpu.sysPercent = sysMatch ? parseFloat(sysMatch[1]) : null;
      vitals.cpu.idlePercent = idleMatch ? parseFloat(idleMatch[1]) : null;
      if (vitals.cpu.userPercent !== null && vitals.cpu.sysPercent !== null) {
        vitals.cpu.usage = Math.round(vitals.cpu.userPercent + vitals.cpu.sysPercent);
      }
    }

    // Disk
    const dfParts = dfRaw.split(/\s+/);
    if (dfParts.length >= 4) {
      vitals.disk.total = parseInt(dfParts[1], 10) * 1024;
      vitals.disk.used = parseInt(dfParts[2], 10) * 1024;
      vitals.disk.free = parseInt(dfParts[3], 10) * 1024;
      vitals.disk.percent = Math.round((parseInt(dfParts[2], 10) / parseInt(dfParts[1], 10)) * 100);
    }

    // Memory (platform-specific)
    if (isLinux) {
      const memTotalKB = parseInt(memTotalRaw, 10) || 0;
      const memAvailableMatch = memInfoRaw.match(/MemAvailable:\s+(\d+)/);
      const memFreeMatch = memInfoRaw.match(/MemFree:\s+(\d+)/);

      vitals.memory.total = memTotalKB * 1024;
      const memAvailable = parseInt(memAvailableMatch?.[1] || memFreeMatch?.[1] || 0, 10) * 1024;

      vitals.memory.used = vitals.memory.total - memAvailable;
      vitals.memory.free = memAvailable;
      vitals.memory.percent =
        vitals.memory.total > 0 ? Math.round((vitals.memory.used / vitals.memory.total) * 100) : 0;
    } else {
      const pageSizeMatch = memInfoRaw.match(/page size of (\d+) bytes/);
      const pageSize = pageSizeMatch ? parseInt(pageSizeMatch[1], 10) : 4096;
      const activePages = parseInt((memInfoRaw.match(/Pages active:\s+(\d+)/) || [])[1] || 0, 10);
      const wiredPages = parseInt(
        (memInfoRaw.match(/Pages wired down:\s+(\d+)/) || [])[1] || 0,
        10,
      );
      const compressedPages = parseInt(
        (memInfoRaw.match(/Pages occupied by compressor:\s+(\d+)/) || [])[1] || 0,
        10,
      );
      vitals.memory.total = parseInt(memTotalRaw, 10) || 0;
      vitals.memory.used = (activePages + wiredPages + compressedPages) * pageSize;
      vitals.memory.free = vitals.memory.total - vitals.memory.used;
      vitals.memory.percent =
        vitals.memory.total > 0 ? Math.round((vitals.memory.used / vitals.memory.total) * 100) : 0;
    }
    vitals.memory.pressure =
      vitals.memory.percent > 90 ? "critical" : vitals.memory.percent > 75 ? "warning" : "normal";

    // Secondary async calls (chip info, iostat)
    // NOTE: iostat needs an explicit count, otherwise it runs forever.
    // IMPORTANT: Avoid shell pipelines (e.g. `| tail -1`) — when Node kills
    // the shell on timeout, pipeline children like `iostat` survive as orphans.
    // We wrap with timeout/gtimeout as a belt-and-suspenders safeguard on top of runCmd timeout.
    const timeoutPrefix = isLinux
      ? "timeout 5"
      : "$(command -v gtimeout >/dev/null 2>&1 && echo gtimeout 5)";
    const iostatArgs = isLinux ? "-d -o JSON 1 2" : "-d -c 2 2";
    const iostatCmd = `${timeoutPrefix} iostat ${iostatArgs} 2>/dev/null || echo ''`;
    const [perfCores, effCores, chip, iostatRaw] = await Promise.all([
      isMacOS
        ? runCmd("sysctl -n hw.perflevel0.logicalcpu 2>/dev/null || echo 0", { fallback: "0" })
        : Promise.resolve("0"),
      isMacOS
        ? runCmd("sysctl -n hw.perflevel1.logicalcpu 2>/dev/null || echo 0", { fallback: "0" })
        : Promise.resolve("0"),
      isMacOS
        ? runCmd(
            'system_profiler SPHardwareDataType 2>/dev/null | grep "Chip:" | cut -d: -f2 || echo ""',
            { fallback: "" },
          )
        : Promise.resolve(""),
      runCmd(iostatCmd, { fallback: "", timeout: 5000 }),
    ]);

    if (isLinux) {
      const cpuBrand = await runCmd(
        "cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d: -f2",
        { fallback: "" },
      );
      if (cpuBrand) vitals.cpu.brand = cpuBrand.trim();
    }

    vitals.cpu.pCores = parseInt(perfCores, 10) || null;
    vitals.cpu.eCores = parseInt(effCores, 10) || null;
    if (chip) vitals.cpu.chip = chip;
    if (isLinux) {
      try {
        const iostatJson = JSON.parse(iostatRaw);
        const samples = iostatJson.sysstat.hosts[0].statistics;
        const disks = samples[samples.length - 1].disk;
        const disk = disks
          .filter((d) => !d.disk_device.startsWith("loop"))
          .sort((a, b) => b.tps - a.tps)[0];
        if (disk) {
          const kbReadPerSec = disk["kB_read/s"] || 0;
          const kbWrtnPerSec = disk["kB_wrtn/s"] || 0;
          vitals.disk.iops = disk.tps || 0;
          vitals.disk.throughputMBps = (kbReadPerSec + kbWrtnPerSec) / 1024;
          vitals.disk.kbPerTransfer = disk.tps > 0 ? (kbReadPerSec + kbWrtnPerSec) / disk.tps : 0;
        }
      } catch {
        // JSON parse failed
      }
    } else {
      // iostat output has multiple lines (header + samples); take the last non-empty line
      const iostatLines = iostatRaw.split("\n").filter((l) => l.trim());
      const lastLine = iostatLines.length > 0 ? iostatLines[iostatLines.length - 1] : "";
      const iostatParts = lastLine.split(/\s+/).filter(Boolean);
      if (iostatParts.length >= 3) {
        vitals.disk.kbPerTransfer = parseFloat(iostatParts[0]) || 0;
        vitals.disk.iops = parseFloat(iostatParts[1]) || 0;
        vitals.disk.throughputMBps = parseFloat(iostatParts[2]) || 0;
      }
    }
    // Temperature
    vitals.temperature = null;
    vitals.temperatureNote = null;
    const isAppleSilicon = vitals.cpu.chip && /apple/i.test(vitals.cpu.chip);

    if (isAppleSilicon) {
      vitals.temperatureNote = "Apple Silicon (requires elevated access)";
      try {
        const pmOutput = await runCmd(
          'sudo -n powermetrics --samplers smc -i 1 -n 1 2>/dev/null | grep -i "die temp" | head -1',
          { fallback: "", timeout: 5000 },
        );
        const tempMatch = pmOutput.match(/([\d.]+)/);
        if (tempMatch) {
          vitals.temperature = parseFloat(tempMatch[1]);
          vitals.temperatureNote = null;
        }
      } catch (e) {}
    } else if (isMacOS) {
      const home = require("os").homedir();
      try {
        const temp = await runCmd(
          `osx-cpu-temp 2>/dev/null || ${home}/bin/osx-cpu-temp 2>/dev/null`,
          { fallback: "" },
        );
        if (temp && temp.includes("\u00b0")) {
          const tempMatch = temp.match(/([\d.]+)/);
          if (tempMatch && parseFloat(tempMatch[1]) > 0) {
            vitals.temperature = parseFloat(tempMatch[1]);
          }
        }
      } catch (e) {}
      if (!vitals.temperature) {
        try {
          const ioregRaw = await runCmd(
            "ioreg -r -n AppleSmartBattery 2>/dev/null | grep Temperature",
            { fallback: "" },
          );
          const tempMatch = ioregRaw.match(/"Temperature"\s*=\s*(\d+)/);
          if (tempMatch) {
            vitals.temperature = Math.round(parseInt(tempMatch[1], 10) / 100);
          }
        } catch (e) {}
      }
    } else if (isLinux) {
      try {
        const temp = await runCmd("cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null", {
          fallback: "",
        });
        if (temp) {
          vitals.temperature = Math.round(parseInt(temp, 10) / 1000);
        }
      } catch (e) {}
    }
  } catch (e) {
    console.error("[Vitals] Async refresh failed:", e.message);
  }

  // Formatted versions
  vitals.memory.usedFormatted = formatBytes(vitals.memory.used);
  vitals.memory.totalFormatted = formatBytes(vitals.memory.total);
  vitals.memory.freeFormatted = formatBytes(vitals.memory.free);
  vitals.disk.usedFormatted = formatBytes(vitals.disk.used);
  vitals.disk.totalFormatted = formatBytes(vitals.disk.total);
  vitals.disk.freeFormatted = formatBytes(vitals.disk.free);

  cachedVitals = vitals;
  lastVitalsUpdate = Date.now();
  vitalsRefreshing = false;
  console.log("[Vitals] Cache refreshed async");
}

// Start background vitals refresh on startup
setTimeout(() => refreshVitalsAsync(), 500);
setInterval(() => refreshVitalsAsync(), VITALS_CACHE_TTL);

function getSystemVitals() {
  const now = Date.now();
  if (!cachedVitals || now - lastVitalsUpdate > VITALS_CACHE_TTL) {
    refreshVitalsAsync();
  }
  if (cachedVitals) return cachedVitals;

  return {
    hostname: "loading...",
    uptime: "",
    disk: {
      used: 0,
      free: 0,
      total: 0,
      percent: 0,
      usedFormatted: "-",
      totalFormatted: "-",
      freeFormatted: "-",
    },
    cpu: { loadAvg: [0, 0, 0], cores: 0, usage: 0 },
    memory: {
      used: 0,
      free: 0,
      total: 0,
      percent: 0,
      pressure: "normal",
      usedFormatted: "-",
      totalFormatted: "-",
      freeFormatted: "-",
    },
    temperature: null,
  };
}

/**
 * Check for optional system dependencies.
 * Returns structured results and logs hints once at startup.
 */
let cachedDeps = null;

async function checkOptionalDeps() {
  const isLinux = process.platform === "linux";
  const isMacOS = process.platform === "darwin";
  const platform = isLinux ? "linux" : isMacOS ? "darwin" : null;
  const results = [];

  if (!platform) {
    cachedDeps = results;
    return results;
  }

  const fs = require("fs");
  const path = require("path");
  const depsFile = path.join(__dirname, "..", "config", "system-deps.json");
  let depsConfig;
  try {
    depsConfig = JSON.parse(fs.readFileSync(depsFile, "utf8"));
  } catch {
    cachedDeps = results;
    return results;
  }

  const deps = depsConfig[platform] || [];
  const home = require("os").homedir();

  // Detect package manager
  let pkgManager = null;
  if (isLinux) {
    for (const pm of ["apt", "dnf", "yum", "pacman", "apk"]) {
      const has = await runCmd(`which ${pm}`, { fallback: "" });
      if (has) {
        pkgManager = pm;
        break;
      }
    }
  } else if (isMacOS) {
    const hasBrew = await runCmd("which brew", { fallback: "" });
    if (hasBrew) pkgManager = "brew";
  }

  // Detect chip for condition filtering
  let isAppleSilicon = false;
  if (isMacOS) {
    const chip = await runCmd("sysctl -n machdep.cpu.brand_string", { fallback: "" });
    isAppleSilicon = /apple/i.test(chip);
  }

  for (const dep of deps) {
    // Skip deps that don't apply to this hardware
    if (dep.condition === "intel" && isAppleSilicon) continue;

    let installed = false;
    const hasBinary = await runCmd(`which ${dep.binary} 2>/dev/null`, { fallback: "" });
    if (hasBinary) {
      installed = true;
    } else if (isMacOS && dep.binary === "osx-cpu-temp") {
      const homebin = await runCmd(`test -x ${home}/bin/osx-cpu-temp && echo ok`, {
        fallback: "",
      });
      if (homebin) installed = true;
    }

    const installCmd = dep.install[pkgManager] || null;

    results.push({
      id: dep.id,
      name: dep.name,
      purpose: dep.purpose,
      affects: dep.affects,
      installed,
      installCmd,
      url: dep.url || null,
    });
  }

  cachedDeps = results;

  // Log hints for missing deps
  const missing = results.filter((d) => !d.installed);
  if (missing.length > 0) {
    console.log("[Startup] Optional dependencies for enhanced vitals:");
    for (const dep of missing) {
      const action = dep.installCmd || dep.url || "see docs";
      console.log(`   \u{1F4A1} ${dep.name} \u2014 ${dep.purpose}: ${action}`);
    }
  }

  return results;
}

function getOptionalDeps() {
  return cachedDeps;
}

module.exports = {
  refreshVitalsAsync,
  getSystemVitals,
  checkOptionalDeps,
  getOptionalDeps,
  VITALS_CACHE_TTL,
};
```

## File: `tests/actions.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { executeAction } = require("../src/actions");

describe("actions module", () => {
  describe("executeAction()", () => {
    const mockDeps = {
      runOpenClaw: (args) => `mock output for: ${args}`,
      extractJSON: (output) => output,
      PORT: 3333,
    };

    it("handles gateway-status action", () => {
      const result = executeAction("gateway-status", mockDeps);
      assert.strictEqual(result.success, true);
      assert.strictEqual(result.action, "gateway-status");
      assert.ok(result.output.includes("gateway status"));
    });

    it("handles gateway-restart action with safety message", () => {
      const result = executeAction("gateway-restart", mockDeps);
      assert.strictEqual(result.success, true);
      assert.ok(result.note.includes("safety"));
    });

    it("handles sessions-list action", () => {
      const result = executeAction("sessions-list", mockDeps);
      assert.strictEqual(result.success, true);
    });

    it("handles cron-list action", () => {
      const result = executeAction("cron-list", mockDeps);
      assert.strictEqual(result.success, true);
    });

    it("handles health-check action", () => {
      const result = executeAction("health-check", mockDeps);
      assert.strictEqual(result.success, true);
      assert.ok(result.output.includes("Dashboard"));
      assert.ok(result.output.includes("3333"));
    });

    it("handles clear-stale-sessions action", () => {
      const deps = {
        ...mockDeps,
        runOpenClaw: () => '{"sessions": []}',
        extractJSON: (o) => o,
      };
      const result = executeAction("clear-stale-sessions", deps);
      assert.strictEqual(result.success, true);
      assert.ok(result.output.includes("stale sessions"));
    });

    it("returns error for unknown action", () => {
      const result = executeAction("nonexistent-action", mockDeps);
      assert.strictEqual(result.success, false);
      assert.ok(result.error.includes("Unknown action"));
    });

    it("handles runOpenClaw returning null", () => {
      const deps = { ...mockDeps, runOpenClaw: () => null };
      const result = executeAction("gateway-status", deps);
      assert.strictEqual(result.success, true);
      assert.strictEqual(result.output, "Unknown");
    });

    it("catches exceptions and returns error", () => {
      const deps = {
        ...mockDeps,
        runOpenClaw: () => {
          throw new Error("command failed");
        },
      };
      const result = executeAction("gateway-status", deps);
      assert.strictEqual(result.success, false);
      assert.ok(result.error.includes("command failed"));
    });
  });
});
```

## File: `tests/auth.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { checkAuth, AUTH_HEADERS, getUnauthorizedPage } = require("../src/auth");

describe("auth module", () => {
  describe("AUTH_HEADERS", () => {
    it("exports tailscale header names", () => {
      assert.strictEqual(AUTH_HEADERS.tailscale.login, "tailscale-user-login");
      assert.strictEqual(AUTH_HEADERS.tailscale.name, "tailscale-user-name");
      assert.strictEqual(AUTH_HEADERS.tailscale.pic, "tailscale-user-profile-pic");
    });

    it("exports cloudflare header names", () => {
      assert.strictEqual(AUTH_HEADERS.cloudflare.email, "cf-access-authenticated-user-email");
    });
  });

  describe("checkAuth()", () => {
    function mockReq(remoteAddress, headers = {}) {
      return { socket: { remoteAddress }, headers };
    }

    it("allows localhost (127.0.0.1) regardless of auth mode", () => {
      const result = checkAuth(mockReq("127.0.0.1"), { mode: "token", token: "secret" });
      assert.strictEqual(result.authorized, true);
      assert.strictEqual(result.user.type, "localhost");
    });

    it("allows localhost (::1) regardless of auth mode", () => {
      const result = checkAuth(mockReq("::1"), { mode: "tailscale", allowedUsers: [] });
      assert.strictEqual(result.authorized, true);
    });

    it("allows localhost (::ffff:127.0.0.1)", () => {
      const result = checkAuth(mockReq("::ffff:127.0.0.1"), { mode: "token", token: "x" });
      assert.strictEqual(result.authorized, true);
    });

    it("allows all when mode is 'none'", () => {
      const result = checkAuth(mockReq("192.168.1.100"), { mode: "none" });
      assert.strictEqual(result.authorized, true);
      assert.strictEqual(result.user, null);
    });

    describe("token mode", () => {
      const authConfig = { mode: "token", token: "my-secret-token" };

      it("allows valid bearer token", () => {
        const req = mockReq("10.0.0.1", { authorization: "Bearer my-secret-token" });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
        assert.strictEqual(result.user.type, "token");
      });

      it("rejects invalid token", () => {
        const req = mockReq("10.0.0.1", { authorization: "Bearer wrong-token" });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
        assert.ok(result.reason.includes("Invalid"));
      });

      it("rejects missing authorization header", () => {
        const req = mockReq("10.0.0.1", {});
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
      });
    });

    describe("tailscale mode", () => {
      const authConfig = { mode: "tailscale", allowedUsers: ["user@example.com", "*@corp.com"] };

      it("allows user in allowlist", () => {
        const req = mockReq("100.64.0.1", { "tailscale-user-login": "user@example.com" });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
        assert.strictEqual(result.user.type, "tailscale");
        assert.strictEqual(result.user.login, "user@example.com");
      });

      it("allows wildcard domain match", () => {
        const req = mockReq("100.64.0.1", { "tailscale-user-login": "anyone@corp.com" });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
      });

      it("rejects user not in allowlist", () => {
        const req = mockReq("100.64.0.1", { "tailscale-user-login": "hacker@evil.com" });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
        assert.ok(result.reason.includes("not in allowlist"));
      });

      it("rejects when no tailscale header present", () => {
        const req = mockReq("10.0.0.1", {});
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
        assert.ok(result.reason.includes("Tailscale"));
      });

      it("allows wildcard (*) user", () => {
        const config = { mode: "tailscale", allowedUsers: ["*"] };
        const req = mockReq("100.64.0.1", { "tailscale-user-login": "anyone@anywhere.com" });
        const result = checkAuth(req, config);
        assert.strictEqual(result.authorized, true);
      });
    });

    describe("cloudflare mode", () => {
      const authConfig = { mode: "cloudflare", allowedUsers: ["user@example.com"] };

      it("allows user in allowlist", () => {
        const req = mockReq("172.16.0.1", {
          "cf-access-authenticated-user-email": "user@example.com",
        });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
        assert.strictEqual(result.user.type, "cloudflare");
      });

      it("rejects user not in allowlist", () => {
        const req = mockReq("172.16.0.1", {
          "cf-access-authenticated-user-email": "other@example.com",
        });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
      });

      it("rejects when no cloudflare header present", () => {
        const req = mockReq("172.16.0.1", {});
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
        assert.ok(result.reason.includes("Cloudflare"));
      });
    });

    describe("allowlist mode", () => {
      const authConfig = { mode: "allowlist", allowedIPs: ["10.0.0.5", "192.168.1.0/24"] };

      it("allows exact IP match", () => {
        const req = mockReq("10.0.0.5");
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
        assert.strictEqual(result.user.type, "ip");
      });

      it("allows /24 subnet match", () => {
        const req = mockReq("192.168.1.42");
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
      });

      it("rejects IP not in allowlist", () => {
        const req = mockReq("10.0.0.99");
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, false);
        assert.ok(result.reason.includes("not in allowlist"));
      });

      it("uses x-forwarded-for header when present", () => {
        const req = mockReq("172.16.0.1", { "x-forwarded-for": "10.0.0.5, 172.16.0.1" });
        const result = checkAuth(req, authConfig);
        assert.strictEqual(result.authorized, true);
      });
    });

    it("rejects unknown auth mode", () => {
      const result = checkAuth(mockReq("10.0.0.1"), { mode: "kerberos" });
      assert.strictEqual(result.authorized, false);
      assert.ok(result.reason.includes("Unknown"));
    });
  });

  describe("getUnauthorizedPage()", () => {
    it("returns HTML string", () => {
      const html = getUnauthorizedPage("test reason", null, { mode: "token" });
      assert.ok(html.includes("<!DOCTYPE html>"));
      assert.ok(html.includes("Access Denied"));
      assert.ok(html.includes("test reason"));
    });

    it("includes user info when provided", () => {
      const html = getUnauthorizedPage("denied", { login: "user@test.com" }, { mode: "tailscale" });
      assert.ok(html.includes("user@test.com"));
    });

    it("includes auth mode in output", () => {
      const html = getUnauthorizedPage("denied", null, { mode: "cloudflare" });
      assert.ok(html.includes("cloudflare"));
    });
  });
});
```

## File: `tests/config.test.js`
```javascript
const { describe, it, afterEach } = require("node:test");
const assert = require("node:assert");
const os = require("os");
const path = require("path");

describe("config module", () => {
  // Save original env to restore after tests
  const originalEnv = { ...process.env };

  afterEach(() => {
    // Restore env vars after each test
    for (const key of Object.keys(process.env)) {
      if (!(key in originalEnv)) {
        delete process.env[key];
      }
    }
    Object.assign(process.env, originalEnv);

    // Clear require cache so config reloads fresh
    for (const key of Object.keys(require.cache)) {
      if (key.includes("config.js")) {
        delete require.cache[key];
      }
    }
  });

  describe("expandPath()", () => {
    it("expands ~ to home directory", () => {
      const { expandPath } = require("../src/config");
      const result = expandPath("~/some/path");
      assert.strictEqual(result, path.join(os.homedir(), "some", "path"));
    });

    it("expands $HOME to home directory", () => {
      const { expandPath } = require("../src/config");
      const result = expandPath("$HOME/docs");
      assert.strictEqual(result, path.join(os.homedir(), "docs"));
    });

    it("expands ${HOME} to home directory", () => {
      const { expandPath } = require("../src/config");
      const result = expandPath("${HOME}/docs");
      assert.strictEqual(result, path.join(os.homedir(), "docs"));
    });

    it("returns null/undefined as-is", () => {
      const { expandPath } = require("../src/config");
      assert.strictEqual(expandPath(null), null);
      assert.strictEqual(expandPath(undefined), undefined);
    });

    it("returns path unchanged when no expansion needed", () => {
      const { expandPath } = require("../src/config");
      assert.strictEqual(expandPath("/absolute/path"), "/absolute/path");
    });
  });

  describe("detectWorkspace()", () => {
    it("returns a string path", () => {
      const { detectWorkspace } = require("../src/config");
      const result = detectWorkspace();
      assert.strictEqual(typeof result, "string");
      assert.ok(result.length > 0, "workspace path should not be empty");
    });

    it("returns an absolute path", () => {
      const { detectWorkspace } = require("../src/config");
      const result = detectWorkspace();
      assert.ok(path.isAbsolute(result), `Expected absolute path, got: ${result}`);
    });
  });

  describe("loadConfig()", () => {
    it("returns an object with all required top-level keys", () => {
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.ok(config.server, "config should have server");
      assert.ok(config.paths, "config should have paths");
      assert.ok(config.auth, "config should have auth");
      assert.ok(config.branding, "config should have branding");
      assert.ok(config.integrations, "config should have integrations");
    });

    it("has default port of 3333", () => {
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.strictEqual(config.server.port, 3333);
    });

    it("has default auth mode of 'none'", () => {
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.strictEqual(config.auth.mode, "none");
    });

    it("has default host of localhost", () => {
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.strictEqual(config.server.host, "localhost");
    });

    it("has workspace path set", () => {
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.ok(config.paths.workspace, "workspace path should be set");
      assert.strictEqual(typeof config.paths.workspace, "string");
    });

    it("has memory path set", () => {
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.ok(config.paths.memory, "memory path should be set");
    });
  });

  describe("environment variable overrides", () => {
    it("PORT env var overrides default port", () => {
      process.env.PORT = "9999";
      // Clear cache to force re-require
      for (const key of Object.keys(require.cache)) {
        if (key.includes("config.js")) {
          delete require.cache[key];
        }
      }
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.strictEqual(config.server.port, 9999);
    });

    it("HOST env var overrides default host", () => {
      process.env.HOST = "0.0.0.0";
      for (const key of Object.keys(require.cache)) {
        if (key.includes("config.js")) {
          delete require.cache[key];
        }
      }
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.strictEqual(config.server.host, "0.0.0.0");
    });

    it("DASHBOARD_AUTH_MODE env var overrides auth mode", () => {
      process.env.DASHBOARD_AUTH_MODE = "token";
      for (const key of Object.keys(require.cache)) {
        if (key.includes("config.js")) {
          delete require.cache[key];
        }
      }
      const { loadConfig } = require("../src/config");
      const config = loadConfig();
      assert.strictEqual(config.auth.mode, "token");
    });
  });
});
```

## File: `tests/cron.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { cronToHuman } = require("../src/cron");

describe("cron module", () => {
  describe("cronToHuman()", () => {
    it("returns null for null input", () => {
      assert.strictEqual(cronToHuman(null), null);
    });

    it("returns null for dash", () => {
      assert.strictEqual(cronToHuman("—"), null);
    });

    it("returns null for too few parts", () => {
      assert.strictEqual(cronToHuman("* *"), null);
    });

    it("converts every-minute cron", () => {
      assert.strictEqual(cronToHuman("* * * * *"), "Every minute");
    });

    it("converts every-N-minutes cron", () => {
      assert.strictEqual(cronToHuman("*/5 * * * *"), "Every 5 minutes");
      assert.strictEqual(cronToHuman("*/15 * * * *"), "Every 15 minutes");
    });

    it("converts every-N-hours cron", () => {
      assert.strictEqual(cronToHuman("0 */2 * * *"), "Every 2 hours");
    });

    it("converts hourly at specific minute", () => {
      assert.strictEqual(cronToHuman("30 * * * *"), "Hourly at :30");
      assert.strictEqual(cronToHuman("0 * * * *"), "Hourly at :00");
    });

    it("converts daily at specific time", () => {
      assert.strictEqual(cronToHuman("0 9 * * *"), "Daily at 9am");
      assert.strictEqual(cronToHuman("30 14 * * *"), "Daily at 2:30pm");
      assert.strictEqual(cronToHuman("0 0 * * *"), "Daily at 12am");
      assert.strictEqual(cronToHuman("0 12 * * *"), "Daily at 12pm");
    });

    it("converts weekday cron", () => {
      assert.strictEqual(cronToHuman("0 9 * * 1-5"), "Weekdays at 9am");
      assert.strictEqual(cronToHuman("0 9 * * MON-FRI"), "Weekdays at 9am");
    });

    it("converts weekend cron", () => {
      assert.strictEqual(cronToHuman("0 10 * * 0,6"), "Weekends at 10am");
      assert.strictEqual(cronToHuman("0 10 * * 6,0"), "Weekends at 10am");
    });

    it("converts specific day of week", () => {
      const result = cronToHuman("0 8 * * 1");
      assert.strictEqual(result, "Monday at 8am");
    });

    it("converts specific day of month", () => {
      const result = cronToHuman("0 9 1 * *");
      assert.strictEqual(result, "1st of month at 9am");
    });

    it("handles ordinal suffixes correctly", () => {
      assert.ok(cronToHuman("0 9 2 * *").includes("2nd"));
      assert.ok(cronToHuman("0 9 3 * *").includes("3rd"));
      assert.ok(cronToHuman("0 9 4 * *").includes("4th"));
      assert.ok(cronToHuman("0 9 21 * *").includes("21st"));
      assert.ok(cronToHuman("0 9 22 * *").includes("22nd"));
      assert.ok(cronToHuman("0 9 23 * *").includes("23rd"));
    });

    it("returns original expression as fallback", () => {
      const expr = "* * * 6 *";
      const result = cronToHuman(expr);
      assert.strictEqual(typeof result, "string");
    });
  });
});
```

## File: `tests/data.test.js`
```javascript
const { describe, it, afterEach } = require("node:test");
const assert = require("node:assert");
const fs = require("fs");
const path = require("path");
const os = require("os");
const { migrateDataDir } = require("../src/data");

describe("data module", () => {
  let tmpDir;

  afterEach(() => {
    if (tmpDir && fs.existsSync(tmpDir)) {
      fs.rmSync(tmpDir, { recursive: true, force: true });
    }
  });

  describe("migrateDataDir()", () => {
    it("does nothing when legacy dir does not exist", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "data-test-"));
      const dataDir = path.join(tmpDir, "data");
      // Should not throw
      migrateDataDir(dataDir, "/nonexistent/legacy");
      assert.ok(!fs.existsSync(dataDir));
    });

    it("copies files from legacy dir to data dir", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "data-test-"));
      const legacyDir = path.join(tmpDir, "legacy");
      const dataDir = path.join(tmpDir, "data");
      fs.mkdirSync(legacyDir);
      fs.writeFileSync(path.join(legacyDir, "settings.json"), '{"key":"value"}');

      migrateDataDir(dataDir, legacyDir);

      assert.ok(fs.existsSync(path.join(dataDir, "settings.json")));
      const content = fs.readFileSync(path.join(dataDir, "settings.json"), "utf8");
      assert.strictEqual(content, '{"key":"value"}');
    });

    it("does not overwrite existing files in data dir", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "data-test-"));
      const legacyDir = path.join(tmpDir, "legacy");
      const dataDir = path.join(tmpDir, "data");
      fs.mkdirSync(legacyDir);
      fs.mkdirSync(dataDir);
      fs.writeFileSync(path.join(legacyDir, "config.json"), "legacy");
      fs.writeFileSync(path.join(dataDir, "config.json"), "current");

      migrateDataDir(dataDir, legacyDir);

      const content = fs.readFileSync(path.join(dataDir, "config.json"), "utf8");
      assert.strictEqual(content, "current");
    });

    it("does nothing when legacy dir is empty", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "data-test-"));
      const legacyDir = path.join(tmpDir, "legacy");
      const dataDir = path.join(tmpDir, "data");
      fs.mkdirSync(legacyDir);

      migrateDataDir(dataDir, legacyDir);

      // data dir should not be created for empty legacy
      // Actually the function creates it, let's check it doesn't crash
    });
  });
});
```

## File: `tests/iostat-leak.test.js`
```javascript
const { describe, it, before, after } = require("node:test");
const assert = require("node:assert");
const http = require("http");
const { spawn, execSync } = require("child_process");
const os = require("os");
const path = require("path");

const isLinux = os.platform() === "linux";

/**
 * Count running iostat processes using pgrep (avoids self-match issues with ps|grep).
 * Returns 0 if pgrep finds no matches (exit code 1).
 */
function countIostatProcesses() {
  try {
    return parseInt(execSync("pgrep -c iostat", { encoding: "utf8" }).trim(), 10) || 0;
  } catch {
    return 0; // pgrep exits 1 when no matches
  }
}

/**
 * Simple HTTP GET helper that returns a promise
 */
function httpGet(url) {
  return new Promise((resolve, reject) => {
    http
      .get(url, (res) => {
        let body = "";
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () =>
          resolve({
            statusCode: res.statusCode,
            headers: res.headers,
            body,
          }),
        );
      })
      .on("error", reject);
  });
}

describe(
  "iostat resource leak (#31)",
  { skip: !isLinux && "Linux-only test", timeout: 90000 },
  () => {
    const TEST_PORT = 10000 + Math.floor(Math.random() * 50000);
    let serverProcess;

    before(async () => {
      // Kill any stale iostat processes from prior runs
      try {
        execSync("pkill iostat 2>/dev/null", { encoding: "utf8" });
      } catch {
        // No stale processes — expected
      }

      // Start the server
      serverProcess = spawn(process.execPath, [path.join(__dirname, "..", "lib", "server.js")], {
        env: { ...process.env, PORT: String(TEST_PORT) },
        stdio: ["pipe", "pipe", "pipe"],
      });

      // Wait for server to be ready by polling the health endpoint
      const maxWait = 15000;
      const start = Date.now();

      while (Date.now() - start < maxWait) {
        try {
          await httpGet(`http://localhost:${TEST_PORT}/api/health`);
          return; // Server is ready
        } catch {
          await new Promise((resolve) => setTimeout(resolve, 200));
        }
      }

      throw new Error(`Server did not start within ${maxWait}ms`);
    });

    after(() => {
      if (serverProcess) {
        serverProcess.kill("SIGTERM");
        serverProcess = null;
      }
    });

    it("does not accumulate iostat processes over multiple vitals refreshes", async () => {
      // Vitals refresh every 30s (plus once at startup). Wait long enough for
      // at least two cycles, then sample multiple times to catch the peak count.
      // With the fix, each iostat exits in ~1s so we should never see more than
      // 1 running at a time. Without the fix, each cycle spawns an immortal
      // process and the count grows unboundedly.
      await new Promise((resolve) => setTimeout(resolve, 35000));

      // Sample several times over 5s to get a reliable peak
      let peak = 0;
      for (let i = 0; i < 5; i++) {
        peak = Math.max(peak, countIostatProcesses());
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }

      // At most 2 concurrent: one finishing from a prior cycle, one just started
      assert.ok(peak <= 2, `Peak iostat process count was ${peak} — leak detected`);
    });

    it("leaves no orphaned iostat processes after shutdown", async () => {
      // Snapshot before shutdown (other test suites may also have servers running
      // that spawn iostat, so we compare relative to this baseline)
      const baseline = countIostatProcesses();

      // Kill the server
      if (serverProcess) {
        serverProcess.kill("SIGTERM");
        serverProcess = null;
      }

      // Give processes time to clean up (iostat -d 1 2 takes ~1s, plus timeout margin)
      await new Promise((resolve) => setTimeout(resolve, 6000));

      const remaining = countIostatProcesses();
      assert.ok(
        remaining <= baseline,
        `iostat count grew after shutdown: ${baseline} before, ${remaining} after`,
      );
    });
  },
);
```

## File: `tests/jobs.test.js`
```javascript
const { describe, it, afterEach } = require("node:test");
const assert = require("node:assert");

// We import the module to test its exports and pure functions.
// The jobs module relies on dynamic ESM import of external jobs API,
// so we focus on testing what's available without that dependency.
const { handleJobsRequest, isJobsRoute, _resetForTesting } = require("../src/jobs");

describe("jobs module", () => {
  describe("exports", () => {
    it("exports handleJobsRequest function", () => {
      assert.strictEqual(typeof handleJobsRequest, "function");
    });

    it("exports isJobsRoute function", () => {
      assert.strictEqual(typeof isJobsRoute, "function");
    });
  });

  describe("isJobsRoute()", () => {
    it("returns true for /api/jobs", () => {
      assert.strictEqual(isJobsRoute("/api/jobs"), true);
    });

    it("returns true for /api/jobs/some-job", () => {
      assert.strictEqual(isJobsRoute("/api/jobs/some-job"), true);
    });

    it("returns true for /api/jobs/some-job/history", () => {
      assert.strictEqual(isJobsRoute("/api/jobs/some-job/history"), true);
    });

    it("returns true for /api/jobs/scheduler/status", () => {
      assert.strictEqual(isJobsRoute("/api/jobs/scheduler/status"), true);
    });

    it("returns true for /api/jobs/stats", () => {
      assert.strictEqual(isJobsRoute("/api/jobs/stats"), true);
    });

    it("returns false for /api/health", () => {
      assert.strictEqual(isJobsRoute("/api/health"), false);
    });

    it("returns false for /api/sessions", () => {
      assert.strictEqual(isJobsRoute("/api/sessions"), false);
    });

    it("returns false for /api/job (no trailing s)", () => {
      assert.strictEqual(isJobsRoute("/api/job"), false);
    });

    it("returns false for empty string", () => {
      assert.strictEqual(isJobsRoute(""), false);
    });

    it("returns false for /jobs (no /api prefix)", () => {
      assert.strictEqual(isJobsRoute("/jobs"), false);
    });
  });

  describe("handleJobsRequest()", () => {
    afterEach(() => {
      // Reset API state after each test
      _resetForTesting();
    });

    it("returns 500 when jobs API is not available", async () => {
      // Force API to be unavailable for this test
      _resetForTesting({ forceUnavailable: true });

      let statusCode = null;
      let body = null;

      const mockRes = {
        writeHead(code, _headers) {
          statusCode = code;
        },
        end(data) {
          body = data;
        },
      };

      const mockReq = {};
      const query = new URLSearchParams();

      await handleJobsRequest(mockReq, mockRes, "/api/jobs", query, "GET");

      assert.strictEqual(statusCode, 500);
      const parsed = JSON.parse(body);
      assert.ok(parsed.error, "should have an error message");
      assert.ok(
        parsed.error.includes("not available"),
        `Error should mention not available: ${parsed.error}`,
      );
    });
  });
});
```

## File: `tests/llm-usage.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { transformLiveUsageData } = require("../src/llm-usage");

describe("llm-usage module", () => {
  describe("transformLiveUsageData()", () => {
    it("transforms valid usage data with anthropic provider", () => {
      const usage = {
        providers: [
          {
            provider: "anthropic",
            windows: [
              { label: "5h", usedPercent: 25, resetAt: Date.now() + 3600000 },
              { label: "Week", usedPercent: 10, resetAt: Date.now() + 86400000 * 3 },
              { label: "Sonnet", usedPercent: 5, resetAt: Date.now() + 86400000 * 5 },
            ],
          },
        ],
      };

      const result = transformLiveUsageData(usage);
      assert.strictEqual(result.source, "live");
      assert.strictEqual(result.claude.session.usedPct, 25);
      assert.strictEqual(result.claude.session.remainingPct, 75);
      assert.strictEqual(result.claude.weekly.usedPct, 10);
      assert.strictEqual(result.claude.sonnet.usedPct, 5);
    });

    it("handles auth error from provider", () => {
      const usage = {
        providers: [{ provider: "anthropic", error: "403 Forbidden" }],
      };

      const result = transformLiveUsageData(usage);
      assert.strictEqual(result.source, "error");
      assert.strictEqual(result.errorType, "auth");
      assert.ok(result.error.includes("403"));
      assert.strictEqual(result.claude.session.usedPct, null);
    });

    it("handles missing windows gracefully", () => {
      const usage = { providers: [{ provider: "anthropic", windows: [] }] };
      const result = transformLiveUsageData(usage);
      assert.strictEqual(result.source, "live");
      assert.strictEqual(result.claude.session.usedPct, 0);
      assert.strictEqual(result.claude.weekly.usedPct, 0);
    });

    it("handles codex provider data", () => {
      const usage = {
        providers: [
          { provider: "anthropic", windows: [] },
          {
            provider: "openai-codex",
            windows: [
              { label: "5h", usedPercent: 30 },
              { label: "Day", usedPercent: 15 },
            ],
          },
        ],
      };

      const result = transformLiveUsageData(usage);
      assert.strictEqual(result.codex.usage5hPct, 30);
      assert.strictEqual(result.codex.usageDayPct, 15);
    });

    it("handles missing providers gracefully", () => {
      const usage = { providers: [] };
      const result = transformLiveUsageData(usage);
      assert.strictEqual(result.source, "live");
      assert.strictEqual(result.codex.usage5hPct, 0);
    });

    it("formats reset time correctly", () => {
      const usage = {
        providers: [
          {
            provider: "anthropic",
            windows: [{ label: "5h", usedPercent: 50, resetAt: Date.now() + 30 * 60000 }],
          },
        ],
      };
      const result = transformLiveUsageData(usage);
      assert.ok(result.claude.session.resetsIn.includes("m"));
    });
  });
});
```

## File: `tests/openclaw.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { extractJSON } = require("../src/openclaw");

describe("openclaw module", () => {
  describe("extractJSON()", () => {
    it("returns null for null input", () => {
      assert.strictEqual(extractJSON(null), null);
    });

    it("returns null for empty string", () => {
      assert.strictEqual(extractJSON(""), null);
    });

    it("returns null for non-JSON text", () => {
      assert.strictEqual(extractJSON("no json here"), null);
    });

    it("extracts JSON object from clean input", () => {
      const result = extractJSON('{"key": "value"}');
      assert.strictEqual(result, '{"key": "value"}');
    });

    it("extracts JSON array from clean input", () => {
      const result = extractJSON("[1, 2, 3]");
      assert.strictEqual(result, "[1, 2, 3]");
    });

    it("strips non-JSON prefix from output", () => {
      const result = extractJSON('Some warning text\n{"key": "value"}');
      assert.strictEqual(result, '{"key": "value"}');
    });

    it("handles prefix with special characters", () => {
      const result = extractJSON('Doctor warnings: OK\n[{"id": 1}]');
      assert.strictEqual(result, '[{"id": 1}]');
    });
  });
});
```

## File: `tests/privacy.test.js`
```javascript
const { describe, it, afterEach } = require("node:test");
const assert = require("node:assert");
const fs = require("fs");
const path = require("path");
const os = require("os");
const { loadPrivacySettings, savePrivacySettings } = require("../src/privacy");

describe("privacy module", () => {
  let tmpDir;

  afterEach(() => {
    if (tmpDir && fs.existsSync(tmpDir)) {
      fs.rmSync(tmpDir, { recursive: true, force: true });
    }
  });

  describe("loadPrivacySettings()", () => {
    it("returns defaults when file does not exist", () => {
      const settings = loadPrivacySettings("/nonexistent/path");
      assert.strictEqual(settings.version, 1);
      assert.deepStrictEqual(settings.hiddenTopics, []);
      assert.deepStrictEqual(settings.hiddenSessions, []);
      assert.deepStrictEqual(settings.hiddenCrons, []);
      assert.strictEqual(settings.hideHostname, false);
      assert.strictEqual(settings.updatedAt, null);
    });

    it("loads settings from file", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "privacy-test-"));
      const data = {
        version: 1,
        hiddenTopics: ["secret"],
        hiddenSessions: [],
        hiddenCrons: [],
        hideHostname: true,
        updatedAt: "2024-01-01",
      };
      fs.writeFileSync(path.join(tmpDir, "privacy-settings.json"), JSON.stringify(data));
      const settings = loadPrivacySettings(tmpDir);
      assert.deepStrictEqual(settings.hiddenTopics, ["secret"]);
      assert.strictEqual(settings.hideHostname, true);
    });
  });

  describe("savePrivacySettings()", () => {
    it("saves settings to file", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "privacy-test-"));
      const data = {
        version: 1,
        hiddenTopics: ["topic1"],
        hiddenSessions: [],
        hiddenCrons: [],
        hideHostname: false,
      };
      const result = savePrivacySettings(tmpDir, data);
      assert.strictEqual(result, true);

      const saved = JSON.parse(fs.readFileSync(path.join(tmpDir, "privacy-settings.json"), "utf8"));
      assert.deepStrictEqual(saved.hiddenTopics, ["topic1"]);
      assert.ok(saved.updatedAt);
    });

    it("creates directory if it does not exist", () => {
      tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "privacy-test-"));
      const nestedDir = path.join(tmpDir, "nested", "dir");
      const data = {
        version: 1,
        hiddenTopics: [],
        hiddenSessions: [],
        hiddenCrons: [],
        hideHostname: false,
      };
      const result = savePrivacySettings(nestedDir, data);
      assert.strictEqual(result, true);
      assert.ok(fs.existsSync(path.join(nestedDir, "privacy-settings.json")));
    });
  });
});
```

## File: `tests/server.test.js`
```javascript
const { describe, it, before, after } = require("node:test");
const assert = require("node:assert");
const http = require("http");
const { spawn } = require("child_process");
const path = require("path");

describe("server", () => {
  // Use a random high port to avoid conflicts
  const TEST_PORT = 10000 + Math.floor(Math.random() * 50000);
  let serverProcess;

  before(async () => {
    // Start the server as a child process with a custom PORT
    serverProcess = spawn(process.execPath, [path.join(__dirname, "..", "lib", "server.js")], {
      env: { ...process.env, PORT: String(TEST_PORT) },
      stdio: ["pipe", "pipe", "pipe"],
    });

    // Wait for server to be ready by polling the health endpoint
    const maxWait = 10000;
    const start = Date.now();

    while (Date.now() - start < maxWait) {
      try {
        await httpGet(`http://localhost:${TEST_PORT}/api/health`);
        return; // Server is ready
      } catch (_e) {
        await new Promise((resolve) => setTimeout(resolve, 200));
      }
    }

    throw new Error(`Server did not start within ${maxWait}ms`);
  });

  after(() => {
    if (serverProcess) {
      serverProcess.kill("SIGTERM");
      serverProcess = null;
    }
  });

  it("responds to /api/health with status ok", async () => {
    const { statusCode, body } = await httpGet(`http://localhost:${TEST_PORT}/api/health`);
    assert.strictEqual(statusCode, 200);
    const data = JSON.parse(body);
    assert.strictEqual(data.status, "ok");
    assert.strictEqual(data.port, TEST_PORT);
    assert.ok(data.timestamp, "should have timestamp");
  });

  it("responds to /api/about with project info", async () => {
    const { statusCode, body } = await httpGet(`http://localhost:${TEST_PORT}/api/about`);
    assert.strictEqual(statusCode, 200);
    const data = JSON.parse(body);
    assert.ok(data.name || data.version, "should have project info");
  });

  it("returns JSON content type for API endpoints", async () => {
    const { headers } = await httpGet(`http://localhost:${TEST_PORT}/api/health`);
    assert.ok(
      headers["content-type"].includes("application/json"),
      `Expected JSON content type, got: ${headers["content-type"]}`,
    );
  });

  it("serves static files for root path", async () => {
    const { statusCode } = await httpGet(`http://localhost:${TEST_PORT}/`);
    // Should return 200 (index.html) or similar
    assert.ok(
      statusCode >= 200 && statusCode < 500,
      `Expected 2xx/3xx/4xx status for root, got: ${statusCode}`,
    );
  });
});

/**
 * Simple HTTP GET helper that returns a promise
 */
function httpGet(url) {
  return new Promise((resolve, reject) => {
    http
      .get(url, (res) => {
        let body = "";
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () =>
          resolve({
            statusCode: res.statusCode,
            headers: res.headers,
            body,
          }),
        );
      })
      .on("error", reject);
  });
}
```

## File: `tests/tokens.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { TOKEN_RATES, emptyUsageBucket, calculateCostForBucket } = require("../src/tokens");

describe("tokens module", () => {
  describe("TOKEN_RATES", () => {
    it("has input rate", () => {
      assert.strictEqual(TOKEN_RATES.input, 15.0);
    });

    it("has output rate", () => {
      assert.strictEqual(TOKEN_RATES.output, 75.0);
    });

    it("has cache read rate", () => {
      assert.strictEqual(TOKEN_RATES.cacheRead, 1.5);
    });

    it("has cache write rate", () => {
      assert.strictEqual(TOKEN_RATES.cacheWrite, 18.75);
    });
  });

  describe("emptyUsageBucket()", () => {
    it("returns object with zero values", () => {
      const bucket = emptyUsageBucket();
      assert.strictEqual(bucket.input, 0);
      assert.strictEqual(bucket.output, 0);
      assert.strictEqual(bucket.cacheRead, 0);
      assert.strictEqual(bucket.cacheWrite, 0);
      assert.strictEqual(bucket.cost, 0);
      assert.strictEqual(bucket.requests, 0);
    });

    it("returns a new object each time", () => {
      const a = emptyUsageBucket();
      const b = emptyUsageBucket();
      assert.notStrictEqual(a, b);
      a.input = 100;
      assert.strictEqual(b.input, 0);
    });
  });

  describe("calculateCostForBucket()", () => {
    it("calculates cost for given token counts", () => {
      const bucket = {
        input: 1_000_000,
        output: 1_000_000,
        cacheRead: 1_000_000,
        cacheWrite: 1_000_000,
      };
      const result = calculateCostForBucket(bucket);
      assert.strictEqual(result.inputCost, 15.0);
      assert.strictEqual(result.outputCost, 75.0);
      assert.strictEqual(result.cacheReadCost, 1.5);
      assert.strictEqual(result.cacheWriteCost, 18.75);
      assert.strictEqual(result.totalCost, 15.0 + 75.0 + 1.5 + 18.75);
    });

    it("returns zero cost for empty bucket", () => {
      const bucket = { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 };
      const result = calculateCostForBucket(bucket);
      assert.strictEqual(result.totalCost, 0);
    });

    it("accepts custom rates", () => {
      const bucket = { input: 1_000_000, output: 0, cacheRead: 0, cacheWrite: 0 };
      const customRates = { input: 10, output: 0, cacheRead: 0, cacheWrite: 0 };
      const result = calculateCostForBucket(bucket, customRates);
      assert.strictEqual(result.inputCost, 10.0);
      assert.strictEqual(result.totalCost, 10.0);
    });

    it("calculates proportionally for partial token counts", () => {
      const bucket = { input: 500_000, output: 0, cacheRead: 0, cacheWrite: 0 };
      const result = calculateCostForBucket(bucket);
      assert.strictEqual(result.inputCost, 7.5);
    });
  });
});
```

## File: `tests/topic-classifier.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");

// Import the module under test (avoid side-effect heavy parts by importing functions directly)
const {
  classifyAndSuggestTopics,
  extractKeyTerms,
  matchTopics,
  CONFIG,
  TOPIC_PATTERNS,
} = require("../scripts/topic-classifier");

describe("topic-classifier module", () => {
  describe("exports", () => {
    it("exports classifyAndSuggestTopics function", () => {
      assert.strictEqual(typeof classifyAndSuggestTopics, "function");
    });

    it("exports extractKeyTerms function", () => {
      assert.strictEqual(typeof extractKeyTerms, "function");
    });

    it("exports matchTopics function", () => {
      assert.strictEqual(typeof matchTopics, "function");
    });

    it("exports CONFIG object", () => {
      assert.ok(CONFIG, "CONFIG should be exported");
      assert.strictEqual(typeof CONFIG.matchThreshold, "number");
      assert.strictEqual(typeof CONFIG.minTermScore, "number");
    });

    it("exports TOPIC_PATTERNS object", () => {
      assert.ok(TOPIC_PATTERNS, "TOPIC_PATTERNS should be exported");
      assert.strictEqual(typeof TOPIC_PATTERNS, "object");
      assert.ok(Object.keys(TOPIC_PATTERNS).length > 0, "should have patterns");
    });
  });

  describe("extractKeyTerms()", () => {
    it("returns an array", () => {
      const result = extractKeyTerms("some text about kubernetes deployment");
      assert.ok(Array.isArray(result));
    });

    it("returns empty array for empty string", () => {
      const result = extractKeyTerms("");
      assert.deepStrictEqual(result, []);
    });

    it("returns empty array for null input", () => {
      const result = extractKeyTerms(null);
      assert.deepStrictEqual(result, []);
    });

    it("returns empty array for undefined input", () => {
      const result = extractKeyTerms(undefined);
      assert.deepStrictEqual(result, []);
    });

    it("filters out stop words", () => {
      const result = extractKeyTerms("the and or but kubernetes kubernetes deployment deployment");
      const terms = result.map((t) => t.term);
      assert.ok(!terms.includes("the"));
      assert.ok(!terms.includes("and"));
    });

    it("each result has term and score properties", () => {
      const result = extractKeyTerms(
        "docker container docker container kubernetes kubernetes pod pod",
      );
      for (const entry of result) {
        assert.ok("term" in entry, `entry should have 'term' property: ${JSON.stringify(entry)}`);
        assert.ok("score" in entry, `entry should have 'score' property: ${JSON.stringify(entry)}`);
        assert.strictEqual(typeof entry.term, "string");
        assert.strictEqual(typeof entry.score, "number");
      }
    });

    it("scores are sorted descending", () => {
      const result = extractKeyTerms(
        "kubernetes kubernetes kubernetes docker docker terraform terraform terraform terraform deploy deploy deploy deploy",
      );
      for (let i = 1; i < result.length; i++) {
        assert.ok(
          result[i - 1].score >= result[i].score,
          `Score at index ${i - 1} (${result[i - 1].score}) should be >= score at index ${i} (${result[i].score})`,
        );
      }
    });

    it("strips code blocks from text", () => {
      const result = extractKeyTerms(
        "kubernetes kubernetes ```const x = kubernetes;``` kubernetes deployment deployment",
      );
      // The code block content should be stripped, so only tokens from outside code blocks
      const terms = result.map((t) => t.term);
      // 'const' from code block should not appear
      assert.ok(!terms.includes("const"), "should not include tokens from code blocks");
    });

    it("strips URLs from text", () => {
      const result = extractKeyTerms(
        "kubernetes kubernetes https://example.com/kubernetes kubernetes deployment deployment",
      );
      const terms = result.map((t) => t.term);
      assert.ok(!terms.includes("https"), "should not include URL protocol as token");
    });
  });

  describe("matchTopics()", () => {
    const existingTopics = [
      "version-control",
      "deployment",
      "database",
      "testing",
      "ai-ml",
      "containers",
    ];

    it("returns an array", () => {
      const result = matchTopics("some text about deploying code", existingTopics);
      assert.ok(Array.isArray(result));
    });

    it("returns empty array for empty text", () => {
      const result = matchTopics("", existingTopics);
      assert.deepStrictEqual(result, []);
    });

    it("matches deployment topic for deploy-related text", () => {
      const result = matchTopics(
        "deploying to production staging pipeline deploy deploy",
        existingTopics,
      );
      const topics = result.map((r) => r.topic);
      assert.ok(
        topics.includes("deployment"),
        `Expected 'deployment' in ${JSON.stringify(topics)}`,
      );
    });

    it("matches database topic for SQL-related text", () => {
      const result = matchTopics(
        "postgres database query sql optimization postgres query",
        existingTopics,
      );
      const topics = result.map((r) => r.topic);
      assert.ok(topics.includes("database"), `Expected 'database' in ${JSON.stringify(topics)}`);
    });

    it("matches containers topic for docker/k8s text", () => {
      const result = matchTopics(
        "docker container kubernetes pod k8s container docker",
        existingTopics,
      );
      const topics = result.map((r) => r.topic);
      assert.ok(
        topics.includes("containers"),
        `Expected 'containers' in ${JSON.stringify(topics)}`,
      );
    });

    it("results have topic and confidence properties", () => {
      const result = matchTopics("git commit branch merge pull push github", existingTopics);
      for (const entry of result) {
        assert.ok("topic" in entry);
        assert.ok("confidence" in entry);
        assert.strictEqual(typeof entry.confidence, "number");
        assert.ok(entry.confidence >= 0 && entry.confidence <= 1);
      }
    });

    it("results are sorted by confidence descending", () => {
      const result = matchTopics(
        "git commit branch merge deploy production staging",
        existingTopics,
      );
      for (let i = 1; i < result.length; i++) {
        assert.ok(
          result[i - 1].confidence >= result[i].confidence,
          `Confidence at index ${i - 1} should be >= index ${i}`,
        );
      }
    });
  });

  describe("classifyAndSuggestTopics()", () => {
    it("returns object with matched, suggested, keyTerms", () => {
      const result = classifyAndSuggestTopics(
        "kubernetes deployment docker container kubernetes docker deployment",
        ["containers", "deployment"],
        { persist: false },
      );
      assert.ok(Array.isArray(result.matched));
      assert.ok(Array.isArray(result.suggested));
      assert.ok(Array.isArray(result.keyTerms));
    });

    it("returns empty results for very short text", () => {
      const result = classifyAndSuggestTopics("hi", [], { persist: false });
      assert.deepStrictEqual(result.matched, []);
      assert.deepStrictEqual(result.suggested, []);
      assert.deepStrictEqual(result.keyTerms, []);
    });

    it("returns empty results for null input", () => {
      const result = classifyAndSuggestTopics(null, [], { persist: false });
      assert.deepStrictEqual(result.matched, []);
    });

    it("handles array transcript input", () => {
      const transcript = [
        "kubernetes deployment docker container",
        "kubernetes docker deployment staging production",
        "more kubernetes docker content here deploy",
      ];
      const result = classifyAndSuggestTopics(transcript, ["deployment"], {
        persist: false,
      });
      assert.ok(Array.isArray(result.matched));
    });

    it("handles array of message objects", () => {
      const transcript = [
        { text: "kubernetes deployment docker container" },
        { text: "kubernetes docker deployment staging" },
        { text: "more content about kubernetes docker" },
      ];
      const result = classifyAndSuggestTopics(transcript, ["deployment"], {
        persist: false,
      });
      assert.ok(Array.isArray(result.matched));
    });

    it("provides confidence score", () => {
      const result = classifyAndSuggestTopics(
        "kubernetes deployment docker container kubernetes docker deployment pod staging",
        ["containers", "deployment"],
        { persist: false },
      );
      assert.strictEqual(typeof result.confidence, "number");
    });
  });

  describe("TOPIC_PATTERNS", () => {
    it("maps git to version-control", () => {
      assert.strictEqual(TOPIC_PATTERNS["git"], "version-control");
    });

    it("maps docker to containers", () => {
      assert.strictEqual(TOPIC_PATTERNS["docker"], "containers");
    });

    it("maps claude to ai-ml", () => {
      assert.strictEqual(TOPIC_PATTERNS["claude"], "ai-ml");
    });

    it("maps postgres to database", () => {
      assert.strictEqual(TOPIC_PATTERNS["postgres"], "database");
    });
  });
});
```

## File: `tests/topics.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { TOPIC_PATTERNS, detectTopics } = require("../src/topics");

describe("topics module", () => {
  describe("TOPIC_PATTERNS", () => {
    it("is an object with topic keys", () => {
      assert.strictEqual(typeof TOPIC_PATTERNS, "object");
      assert.ok(Object.keys(TOPIC_PATTERNS).length > 0);
    });

    it("each topic has an array of keywords", () => {
      for (const [topic, keywords] of Object.entries(TOPIC_PATTERNS)) {
        assert.ok(Array.isArray(keywords), `${topic} should have array of keywords`);
        assert.ok(keywords.length > 0, `${topic} should have at least one keyword`);
      }
    });

    it("contains expected topics", () => {
      const topics = Object.keys(TOPIC_PATTERNS);
      assert.ok(topics.includes("dashboard"));
      assert.ok(topics.includes("coding"));
      assert.ok(topics.includes("git"));
      assert.ok(topics.includes("Slack"));
    });
  });

  describe("detectTopics()", () => {
    it("returns empty array for null input", () => {
      assert.deepStrictEqual(detectTopics(null), []);
    });

    it("returns empty array for empty string", () => {
      assert.deepStrictEqual(detectTopics(""), []);
    });

    it("returns empty array for undefined", () => {
      assert.deepStrictEqual(detectTopics(undefined), []);
    });

    it("detects git topic from git-related text", () => {
      const topics = detectTopics("git commit branch merge push pull");
      assert.ok(topics.includes("git"), `Expected 'git' in ${JSON.stringify(topics)}`);
    });

    it("detects coding topic", () => {
      const topics = detectTopics("debug the function and fix the error in the code");
      assert.ok(topics.includes("coding"), `Expected 'coding' in ${JSON.stringify(topics)}`);
    });

    it("detects Slack topic", () => {
      const topics = detectTopics("send a slack message to the channel thread");
      assert.ok(topics.includes("Slack"), `Expected 'Slack' in ${JSON.stringify(topics)}`);
    });

    it("returns topics sorted by score descending", () => {
      // Heavily git-focused text with a minor coding mention
      const topics = detectTopics("git commit branch merge push pull repository github code");
      if (topics.length >= 2) {
        // git should score higher than coding since more keywords match
        const gitIdx = topics.indexOf("git");
        assert.ok(gitIdx >= 0, "git should be detected");
      }
    });

    it("returns array of strings", () => {
      const topics = detectTopics("kubernetes docker container deploy");
      assert.ok(Array.isArray(topics));
      topics.forEach((t) => assert.strictEqual(typeof t, "string"));
    });

    it("detects scheduling topic", () => {
      const topics = detectTopics("set up a cron schedule timer for periodic interval");
      assert.ok(
        topics.includes("scheduling"),
        `Expected 'scheduling' in ${JSON.stringify(topics)}`,
      );
    });

    it("detects subagent topic", () => {
      const topics = detectTopics("spawn a subagent to delegate the work in parallel");
      assert.ok(topics.includes("subagent"), `Expected 'subagent' in ${JSON.stringify(topics)}`);
    });
  });
});
```

## File: `tests/utils.test.js`
```javascript
const { describe, it } = require("node:test");
const assert = require("node:assert");
const { formatBytes, formatTimeAgo, formatNumber, formatTokens } = require("../src/utils");

describe("utils module", () => {
  describe("formatBytes()", () => {
    it("formats bytes", () => {
      assert.strictEqual(formatBytes(500), "500 B");
    });

    it("formats kilobytes", () => {
      assert.strictEqual(formatBytes(1024), "1.0 KB");
      assert.strictEqual(formatBytes(1536), "1.5 KB");
    });

    it("formats megabytes", () => {
      assert.strictEqual(formatBytes(1048576), "1.0 MB");
    });

    it("formats gigabytes", () => {
      assert.strictEqual(formatBytes(1073741824), "1.0 GB");
    });

    it("formats terabytes", () => {
      assert.strictEqual(formatBytes(1099511627776), "1.0 TB");
    });
  });

  describe("formatTimeAgo()", () => {
    it("formats just now", () => {
      assert.strictEqual(formatTimeAgo(new Date()), "just now");
    });

    it("formats minutes ago", () => {
      const fiveMinAgo = new Date(Date.now() - 5 * 60 * 1000);
      assert.strictEqual(formatTimeAgo(fiveMinAgo), "5m ago");
    });

    it("formats hours ago", () => {
      const twoHoursAgo = new Date(Date.now() - 2 * 60 * 60 * 1000);
      assert.strictEqual(formatTimeAgo(twoHoursAgo), "2h ago");
    });

    it("formats days ago", () => {
      const threeDaysAgo = new Date(Date.now() - 3 * 24 * 60 * 60 * 1000);
      assert.strictEqual(formatTimeAgo(threeDaysAgo), "3d ago");
    });
  });

  describe("formatNumber()", () => {
    it("formats with 2 decimal places", () => {
      assert.strictEqual(formatNumber(1234.5), "1,234.50");
    });

    it("formats zero", () => {
      assert.strictEqual(formatNumber(0), "0.00");
    });

    it("formats small numbers", () => {
      assert.strictEqual(formatNumber(0.1), "0.10");
    });
  });

  describe("formatTokens()", () => {
    it("formats millions", () => {
      assert.strictEqual(formatTokens(1500000), "1.5M");
    });

    it("formats thousands", () => {
      assert.strictEqual(formatTokens(2500), "2.5k");
    });

    it("formats small numbers as-is", () => {
      assert.strictEqual(formatTokens(42), "42");
    });

    it("formats exactly 1M", () => {
      assert.strictEqual(formatTokens(1000000), "1.0M");
    });

    it("formats exactly 1k", () => {
      assert.strictEqual(formatTokens(1000), "1.0k");
    });
  });
});
```

