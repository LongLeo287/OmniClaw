---
id: repo-fetched-bmad-builder-142708
type: knowledge
owner: OA
registered_at: 2026-04-05T03:57:44.708398
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bmad-builder_142708

## Assimilation Report
Auto-cloned repository: FETCHED_bmad-builder_142708

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# BMad Builder

[![Version](https://img.shields.io/npm/v/bmad-builder?color=blue&label=version)](https://www.npmjs.com/package/bmad-builder)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Build More, Architect Dreams... With the BMad Builder!**

BMad Builder is so much more than a skill builder. BMad Method modules support:

- **Agents** that transform your AI tool into exactly who you need to talk to — with memory that persists across sessions
- **Workflows** that go far beyond simple tasks into truly guided, facilitated processes that can produce near-infinite steps and turns as needed
- **Modules** that are entire ecosystems, not just skill packs — like the BMad Method module for agile AI-driven development. You can create simpler or vastly more complex modules for any entertainment or work purpose.

## The Dream

Imagine AI that truly knows you — a fitness coach that remembers every PR, a writing partner that knows your characters better than you do, a research assistant that learns your preferences.

BMad Builder lets you create:

- **Personal AI Companions** — Agents with memory that evolve with you over time
- **Domain Experts** — Specialists for any field: legal, medical, creative, technical
- **Workflow Automations** — Structured processes that guide you through complex tasks
- **Custom Modules** — Bundle agents and workflows into shareable packages that can empower any type of business or domain

## What Makes It Different

| Feature               | Why It Matters                                              |
| --------------------- | ----------------------------------------------------------- |
| **Persistent Memory** | Agents remember across sessions — they learn and grow       |
| **Composable**        | Your creations work alongside the entire BMad ecosystem     |
| **Skill-Compliant**   | Built on open standards that work with any AI tool          |
| **Shareable**         | Package your modules for the BMad Marketplace (coming soon) |

## What You Can Build

| Domain           | Example                                                     |
| ---------------- | ----------------------------------------------------------- |
| **Personal**     | Journal companion, habit coach, learning tutor              |
| **Professional** | Code reviewer, documentation specialist, workflow automator |
| **Creative**     | Story architect, character developer, campaign designer     |
| **Any Domain**   | If you can describe it, you can build it                    |

## Learn More

**[Documentation and Quick Start](https://bmad-builder-docs.bmad-method.org)**

Complete guides for building agents, workflows, and modules.

## Community

- **[Discord](https://discord.gg/gk8jAdXWmj)** — Get help and share what you've built
- **[BMad Method](https://docs.bmad-method.org)** — Core framework documentation

## License

MIT — see [LICENSE](LICENSE) for details.

**BMad Builder** — Part of the [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) ecosystem.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/bmad-builder)](https://github.com/bmad-code-org/bmad-builder/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.

```

### File: AGENTS.md
```md
# AGENTS.md

## Project Overview

**BMad Builder (BMB)** is a meta-module for the BMad Code Platform that helps users create custom AI agents, workflows, and domain-specific modules. It's a documentation-driven project with YAML-based agent/workflow definitions and some minimal Node.js tooling.

## Key Commands

### Development

```bash
npm run docs:dev          # Start Astro dev server (http://localhost:4321)
npm run docs:build        # Build documentation site
npm run docs:preview      # Preview built site
```

### Testing & Validation

```bash
npm test                  # Run full test suite (schemas, refs, lint, format, md)
npm run test:schemas      # Validate agent YAML schemas
npm run test:refs         # Validate internal file references
npm run validate:schemas  # Validate actual agent files against schema
npm run validate:refs     # Check file references (alias for above)
```

### Code Quality

```bash
npm run lint              # ESLint check
npm run lint:fix          # ESLint auto-fix
npm run lint:md           # Markdown lint
npm run format:check      # Prettier check
npm run format:fix        # Prettier format
```

### Release

```bash
npm run release           # Bump patch version and push tag
npm run release:minor     # Bump minor version
npm run release:major     # Bump major version
```

## Architecture

### Source Structure (`src/`)

- **`agents/`** — Agent definitions (`*.agent.yaml`) with persona, menu, and metadata
- **`workflows/`** — Multi-step guided processes organized by type (agent, workflow, module)
  - Each workflow has `steps-c/` (create), `steps-e/` (edit), `steps-v/` (validate)
  - Step-file architecture: JIT loading, sequential execution, state tracking
  - `data/` contains CSV knowledge bases for agents

### Module Structure

```
your-module/
├── src/
│   ├── module.yaml      # Module metadata, install config, variables
│   ├── agents/          # *.agent.yaml files
│   ├── workflows/       # Workflow files with step subdirectories
│   └── tools/           # Optional reusable tools
└── package.json
```

### Build Tools (`tools/`)

- **`build-docs.mjs`** — Consolidates docs, generates LLM-friendly files (`llms.txt`), builds Astro site
- **`validate-file-refs.mjs`** — Validates cross-file references in agents/workflows

### Documentation (`docs/`)

- Diataxis structure: tutorials, how-to, explanation, reference
- Starlight-based site in `website/`
- `_STYLE_GUIDE.md` — Project-specific writing conventions (Google style + Diataxis)

### Skills (`.claude/skills/`)

- BMad OS (Open Source) skills for maintainer workflows
- `bmad-os-add-doc` — Diataxis documentation authoring
- `bmad-os-release-module` — Module release process
- `bmad-os-gh-triage` — GitHub issue triage

## Important Concepts

### Agent YAML Structure

- `agent.metadata` — id, name, title, icon, module
- `agent.persona` — role, identity, communication_style, principles
- `agent.menu` — trigger commands that execute workflows
- `conversational_knowledge` — CSV files loaded at runtime

### Workflow Step Architecture

- Micro-file design: each step is self-contained
- Just-in-time loading: only current step in memory
- Sequential enforcement with state tracking
- Menus halt execution waiting for user input
- Frontmatter defines: name, description, web_bundle, createWorkflow

### Path Variables

- `{project-root}/_bmad/bmb/` — Installation path (in repo, maps to `src/`)
- `{bmad_builder_output_folder}` — User's custom content output
- Runtime variables: `{output_folder}`, `{project-root}` from Core config

## Development Notes

- **Node.js 22+ required** (see `.nvmrc`)
- Module is `default_selected: false` — not auto-installed
- File references in src/ become `_bmad/bmb/` after installation
- All YAML uses double quotes with `avoidEscape: true`
- Website builds to `build/site/` for deployment
- LLM docs have 600k char limit (~150k tokens)

## Publishing

BMad modules are published as npm packages. The module code (`src/`) is what gets installed into user projects via `npx bmad-method install`. The astro website is deployed separately (GitHub Pages via CNAME).

```

### File: CHANGELOG.md
```md
# Changelog

## [1.4.0] - 2026-03-29

### 🎁 Features

* **Standalone self-registering modules** — Single-skill modules no longer need a dedicated `-setup` skill. The Module Builder auto-detects single vs multi-skill input and embeds registration directly in the skill via `assets/module-setup.md`. First-run init hooks into existing agent sidecar detection for a unified setup experience
* **Module Builder skill** — New `bmad-module-builder` with three capabilities: Ideate Module (IM) for creative brainstorming, Create Module (CM) for scaffolding both standalone and multi-skill modules, and Validate Module (VM) for structural and quality validation with `--headless` CI support
* **BMB Setup skill** — Extracted and regenerated as `bmad-bmb-setup` using the Module Builder itself. Manages config.yaml, config.user.yaml, and module-help.csv with anti-zombie merge pattern and legacy migration
* **Workflow Convert capability (CW)** — One-command skill modernization via `--convert <path-or-url>`. Produces a clean BMad-compliant equivalent with an interactive HTML before/after comparison report including token metrics, categorized changes, and dark/light mode
* **Script creation standards** — Formalized Python-first policy with PEP 723 metadata, cross-platform portability via `uv run`, and explicit user approval for external dependencies

### 🐛 Bug Fixes

* Fix HTML quality report data injection — template used `const RAW` but generator looked for `const DATA`, causing broken report rendering in both builders
* Fix merge-help-csv.py HEADER schema — synced from 15 columns to canonical 13-column schema, preventing silent CSV corruption during module setup
* Fix `{project-root}` path validation overcorrection — scanner incorrectly rejected valid project-scope paths like `{project-root}/docs/report.md`
* Add bmad-module-builder to marketplace.json — skill was merged but not registered in the plugin manifest

### ♻️ Refactoring

* **Outcome-driven builder overhaul** — Reframe both builders around discovery-first design: existing skill input treated as reference material, 3-way routing (Analyze/Edit/Rebuild), pruning check in Phase 4, "Quality Optimizer" renamed to "Quality Analysis". Net 44% token reduction in Workflow Builder Phase 5 context
* **Ideation restructured into 7 phases** — Module identity locked in Phase 1, new Phase 6 capability review with user, mandatory config section, self-contained skill briefs, writing discipline (raw ideas in phases 1-2, structured from phase 3+)
* Consolidate plugin.json metadata into marketplace.json — single source of truth for plugin metadata
* Remove npm publishing pipeline — distribution now via `.claude-plugin/` manifest

### 📚 Documentation

* **Comprehensive docs overhaul** — Quick start guide with `bmad-bmb-setup` registration, full 13-column CSV guide explaining how `bmad-help` uses each column, "Distribution: Plugins and Marketplaces" section covering 43+ skills platforms, standalone vs multi-skill patterns throughout all docs
* Add personal-use guidance — users can copy skill folders directly to their tool's skills directory without module packaging
* Remove deprecated bmad-init references from workflow-patterns docs
* New explanation doc: Scripts in Skills — design patterns for deterministic scripting

### 🔧 Maintenance

* Bump version to 1.4.0 across package.json and marketplace.json
* Remove npm release scripts and publishConfig from package.json

## [1.1.0] - 2026-03-19

### Changed

- Flatten skill folder structure to align with Agent Skills spec
- Replace bmad-init dependency with direct config loading
- Optimize workflow-builder and agent-builder skills

### Improved

- Optimizer now captures all fragments in report and produces a final HTML report

### Removed

- Obsolete sample files from old skill structure
- Unneeded images from project root

## [1.0.0] - 2026-03-15

### Release

First official v1 release of BMad Builder — a standard skill-compliant factory for creating BMad Agents, Workflows, and Modules.
The module specific skill is coming soon pending alignment on final format with skill transition.

```

### File: CONTRIBUTING.md
```md
# Contributing to BMad

Thank you for considering contributing! We believe in **Human Amplification, Not Replacement** — bringing out the best thinking in both humans and AI through guided collaboration.

💬 **Discord**: [Join our community](https://discord.gg/gk8jAdXWmj) for real-time discussions, questions, and collaboration.

---

## Our Philosophy

BMad strengthens human-AI collaboration through specialized agents and guided workflows. Every contribution should answer: **"Does this make humans and AI better together?"**

**✅ What we welcome:**

- Enhanced collaboration patterns and workflows
- Improved agent personas and prompts
- Domain-specific modules leveraging BMad Core
- Better planning and context continuity

**❌ What doesn't fit:**

- Purely automated solutions that sideline humans
- Complexity that creates barriers to adoption
- Features that fragment BMad Core's foundation

---

## Reporting Issues

**ALL bug reports and feature requests MUST go through GitHub Issues.**

### Before Creating an Issue

1. **Search existing issues** — Use the GitHub issue search to check if your bug or feature has already been reported
2. **Search closed issues** — Your issue may have been fixed or addressed previously
3. **Check discussions** — Some conversations happen in [GitHub Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions)

### Bug Reports

After searching, if the bug is unreported, use the [bug report template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=bug_report.md) and include:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (model, IDE, BMad version)
- Screenshots or error messages if applicable

### Feature Requests

After searching, use the [feature request template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=feature_request.md) and explain:

- What the feature is
- Why it would benefit the BMad community
- How it strengthens human-AI collaboration

**For community modules**, review [TRADEMARK.md](TRADEMARK.md) for proper naming conventions (e.g., "My Module (BMad Community Module)").

---

## Before Starting Work

⚠️ **Required before submitting PRs:**

| Work Type     | Requirement                                    |
| ------------- | ---------------------------------------------- |
| Bug fix       | An open issue (create one if it doesn't exist) |
| Feature       | An open feature request issue                  |
| Large changes | Discussion via issue first                     |

**Why?** This prevents wasted effort on work that may not align with project direction.

---

## Pull Request Guidelines

### Target Branch

Submit PRs to the `main` branch.

### PR Size

- **Ideal**: 200-400 lines of code changes
- **Maximum**: 800 lines (excluding generated files)
- **One feature/fix per PR**

If your change exceeds 800 lines, break it into smaller PRs that can be reviewed independently.

### New to Pull Requests?

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/bmad-method.git`
3. **Create a branch**: `git checkout -b fix/description` or `git checkout -b feature/description`
4. **Make changes** — keep them focused
5. **Commit**: `git commit -m "fix: correct typo in README"`
6. **Push**: `git push origin fix/description`
7. **Open PR** from your fork on GitHub

### PR Description Template

```markdown
## What

[1-2 sentences describing WHAT changed]

## Why

[1-2 sentences explaining WHY this change is needed]
Fixes #[issue number]

## How

- [2-3 bullets listing HOW you implemented it]
-

## Testing

[1-2 sentences on how you tested this]
```

**Keep it under 200 words.**

### Commit Messages

Use conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code change (no bug/feature)
- `test:` Adding tests
- `chore:` Build/tools changes

Keep messages under 72 characters. Each commit = one logical change.

---

## What Makes a Good PR?

| ✅ Do                       | ❌ Don't                     |
| --------------------------- | ---------------------------- |
| Change one thing per PR     | Mix unrelated changes        |
| Clear title and description | Vague or missing explanation |
| Reference related issues    | Reformat entire files        |
| Small, focused commits      | Copy your whole project      |
| Work on a branch            | Work directly on `main`      |

---

## Prompt & Agent Guidelines

- Keep dev agents lean — focus on coding context, not documentation
- Web/planning agents can be larger with complex tasks
- Everything is natural language (markdown) — no code in core framework
- Use BMad modules for domain-specific features
- Validate YAML schemas: `npm run validate:schemas`

---

## Need Help?

- 💬 **Discord**: [Join the community](https://discord.gg/gk8jAdXWmj)
- 🐛 **Bugs**: Use the [bug report template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=bug_report.md)
- 💡 **Features**: Use the [feature request template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=feature_request.md)

---

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## License

By contributing, your contributions are licensed under the same MIT License. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor attribution.

```

### File: CONTRIBUTORS.md
```md
# Contributors

BMad Core, BMad Method and BMad and Community BMad Modules are made possible by contributions from our community. We gratefully acknowledge everyone who has helped improve this project.

## How We Credit Contributors

- **Git history** — Every contribution is preserved in the project's commit history
- **Contributors badge** — See the dynamic contributors list on our [README](README.md)
- **GitHub contributors graph** — Visual representation at <https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors>

## Becoming a Contributor

Anyone who submits a pull request that is merged becomes a contributor. Contributions include:

- Bug fixes
- New features or workflows
- Documentation improvements
- Bug reports and issue triaging
- Code reviews
- Helping others in discussions

There are no minimum contribution requirements — whether it's a one-character typo fix or a major feature, we value all contributions.

## Copyright

The BMad Method project is copyrighted by BMad Code, LLC. Individual contributions are licensed under the same MIT License as the project. Contributors retain authorship credit through Git history and the contributors graph.

---

**Thank you to everyone who has helped make BMad Method better!**

For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

We release security patches for the following versions:

| Version  | Supported          |
| -------- | ------------------ |
| Latest   | :white_check_mark: |
| < Latest | :x:                |

We recommend always using the latest version of BMad Method to ensure you have the most recent security updates.

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please report it responsibly.

### How to Report

**Do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of these methods:

1. **GitHub Security Advisories** (Preferred): Use [GitHub's private vulnerability reporting](https://github.com/bmad-code-org/BMAD-METHOD/security/advisories/new) to submit a confidential report.

2. **Discord**: Contact a maintainer directly via DM on our [Discord server](https://discord.gg/gk8jAdXWmj).

### What to Include

Please include as much of the following information as possible:

- Type of vulnerability (e.g., prompt injection, path traversal, etc.)
- Full paths of source file(s) related to the vulnerability
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if available)
- Impact assessment of the vulnerability

### Response Timeline

- **Initial Response**: Within 48 hours of receiving your report
- **Status Update**: Within 7 days with our assessment
- **Resolution Target**: Critical issues within 30 days; other issues within 90 days

### What to Expect

1. We will acknowledge receipt of your report
2. We will investigate and validate the vulnerability
3. We will work on a fix and coordinate disclosure timing with you
4. We will credit you in the security advisory (unless you prefer to remain anonymous)

## Security Scope

### In Scope

- Vulnerabilities in BMad Method core framework code
- Security issues in agent definitions or workflows that could lead to unintended behavior
- Path traversal or file system access issues
- Prompt injection vulnerabilities that bypass intended agent behavior
- Supply chain vulnerabilities in dependencies

### Out of Scope

- Security issues in user-created custom agents or modules
- Vulnerabilities in third-party AI providers (Claude, GPT, etc.)
- Issues that require physical access to a user's machine
- Social engineering attacks
- Denial of service attacks that don't exploit a specific vulnerability

## Security Best Practices for Users

When using BMad Method:

1. **Review Agent Outputs**: Always review AI-generated code before executing it
2. **Limit File Access**: Configure your AI IDE to limit file system access where possible
3. **Keep Updated**: Regularly update to the latest version
4. **Validate Dependencies**: Review any dependencies added by generated code
5. **Environment Isolation**: Consider running AI-assisted development in isolated environments

## Acknowledgments

We appreciate the security research community's efforts in helping keep BMad Method secure. Contributors who report valid security issues will be acknowledged in our security advisories.

---

Thank you for helping keep BMad Method and our community safe.

```

### File: TRADEMARK.md
```md
# Trademark Notice & Guidelines

## Trademark Ownership

The following names and logos are trademarks of BMad Code, LLC:

- **BMad** (word mark, all casings: BMad, bmad, BMAD)
- **BMad Method** (word mark, includes BMadMethod, BMAD-METHOD, and all variations)
- **BMad Core** (word mark, includes BMadCore, BMAD-CORE, and all variations)
- **BMad Code** (word mark)
- BMad Method logo and visual branding
- The "Build More, Architect Dreams" tagline

**All casings, stylings, and variations** of the above names (with or without hyphens, spaces, or specific capitalization) are covered by these trademarks.

These trademarks are protected under trademark law and are **not** licensed under the MIT License. The MIT License applies to the software code only, not to the BMad brand identity.

## What This Means

You may:

- Use the BMad software under the terms of the MIT License
- Refer to BMad to accurately describe compatibility or integration (e.g., "Compatible with BMad Method v6")
- Link to <https://github.com/bmad-code-org/BMAD-METHOD>
- Fork the software and distribute your own version under a different name

You may **not**:

- Use "BMad" or any confusingly similar variation as your product name, service name, company name, or domain name
- Present your product as officially endorsed, approved, or certified by BMad Code, LLC when it is not, without written consent from an authorized representative of BMad Code, LLC
- Use BMad logos or branding in a way that suggests your product is an official or endorsed BMad product
- Register domain names, social media handles, or trademarks that incorporate BMad branding

## Examples

| Permitted                                              | Not Permitted                                |
| ------------------------------------------------------ | -------------------------------------------- |
| "My workflow tool, compatible with BMad Method"        | "BMadFlow" or "BMad Studio"                  |
| "An alternative implementation inspired by BMad"       | "BMad Pro" or "BMad Enterprise"              |
| "My Awesome Healthcare Module (Bmad Community Module)" | "The Official BMad Core Healthcare Module"   |
| Accurately stating you use BMad as a dependency        | Implying official endorsement or partnership |

## Commercial Use

You may sell products that incorporate or work with BMad software. However:

- Your product must have its own distinct name and branding
- You must not use BMad trademarks in your marketing, domain names, or product identity
- You may truthfully describe technical compatibility (e.g., "Works with BMad Method")

## Questions?

If you have questions about trademark usage or would like to discuss official partnership or endorsement opportunities, please reach out:

- **Email**: <contact@bmadcode.com>

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bmad_builder
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
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

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
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
the official BMAD Discord server (<https://discord.com/invite/gk8jAdXWmj>) - DM a moderator or flag a post.
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
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
<https://www.contributor-covenant.org/version/2/0/code_of_conduct.html>.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
<https://www.contributor-covenant.org/faq>. Translations are available at
<https://www.contributor-covenant.org/translations>.

```

### File: docs\404.md
```md
---
title: Page Not Found
template: splash
---

The page you're looking for doesn't exist or has been moved.

[Return to Home](/index.md)

```

### File: docs\index.md
```md
---
title: Welcome
description: BMad Builder - Build More, Architect Dreams
---

# BMad Builder - A BMad Method EcoSystem Module

**Build More, Architect Dreams.**

## The Dream

Imagine AI that truly knows you — a fitness coach that remembers every PR, a writing partner that knows your characters better than you do, a research assistant that learns your preferences.

BMad Builder lets you create:

- **Personal AI Companions** — Agents with memory that evolve with you over time
- **Domain Experts** — Specialists for any field: legal, medical, creative, technical
- **Workflow Automations** — Structured processes that guide you through complex tasks
- **Custom Modules** — Bundle agents and workflows into shareable packages

## What Makes It Different

| Feature               | Why It Matters                                              |
| --------------------- | ----------------------------------------------------------- |
| **Persistent Memory** | Agents remember across sessions — they learn and grow       |
| **Composable**        | Your creations work alongside the entire BMad ecosystem     |
| **Skill-Compliant**   | Built on open standards that work with any AI tool          |
| **Shareable**         | Package your modules for the BMad Marketplace (coming soon) |

## Quick Start

### 1. Register the Module

On first use, run `bmad-bmb-setup` to register BMad Builder in your project. This collects your preferences (name, language, output paths) and registers the builder's capabilities with the help system so `bmad-help` can guide you.

:::tip[Single-Skill Modules]
If you install a module that contains only one skill, that skill handles its own registration on first run — no separate setup step needed.
:::

### 2. Build Something

Invoke the **Agent Builder** or **Workflow Builder** and describe what you want to create. Both guide you through conversational discovery and produce a ready-to-use skill folder.

| Goal                      | Builder          | Menu Code |
| ------------------------- | ---------------- | --------- |
| AI companion with memory  | Agent Builder    | BA        |
| Structured process / tool | Workflow Builder | BW        |
| Package skills as module  | Module Builder   | CM        |

### 3. Use Your Skill

The builders produce a complete skill folder. To use it, copy the folder into your AI tool's skills directory — for Claude Code that's `.claude/skills/` at project scope or `~/.claude/skills/` at user scope. For other tools, ask your AI agent where skills are installed or consult the tool's documentation.

:::tip[No Module Required]
If you're building something for personal use or just testing it out, you don't need to package it as a module. Copy the skill folder, use it directly. Module packaging (with `bmad-help` registration and configuration) is for when you want to share or need richer discoverability.
:::

### 4. Learn More

See the [Builder Commands Reference](/reference/builder-commands.md) for all capabilities, modes, and phases.

## What You Can Build

| Domain           | Example                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| **Personal**     | Journal companion, habit coach, learning tutor, friendly personal companions that remember |
| **Professional** | Code reviewer, documentation specialist, workflow automator                                |
| **Creative**     | Story architect, character developer, campaign designer                                    |
| **Any Domain**   | If you can describe it, you can build it                                                   |

## Design Patterns

Build better skills with these guides distilled from real-world BMad development.

| Guide                                                                                | What You'll Learn                                                    |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **[Progressive Disclosure](/explanation/progressive-disclosure.md)**                 | Structure skills so they load only the context needed at each moment |
| **[Subagent Patterns](/explanation/subagent-patterns.md)**                           | Six orchestration patterns for parallel and hierarchical work        |
| **[Skill Authoring Best Practices](/explanation/skill-authoring-best-practices.md)** | Core principles, quality dimensions, and anti-patterns               |

## Documentation

| Section                                              | Purpose                                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------------ |
| **[Concepts](/explanation/)**                        | What agents, workflows, and skills are — and how they relate             |
| **[Design Patterns](/explanation/#design-patterns)** | Progressive disclosure, subagent orchestration, authoring best practices |
| **[Reference](/reference/)**                         | Builder commands, workflow patterns                                      |

## Community

- **[Discord](https://discord.gg/gk8jAdXWmj)** — Get unstuck, share what you built
- **[GitHub](https://github.com/bmad-code-org/bmad-builder)** — Source code
- **[BMad Method](https://docs.bmad-method.org)** — Core framework

```

### File: docs\_STYLE_GUIDE.md
```md
---
title: 'Documentation Style Guide'
description: Project-specific documentation conventions based on Google style and Diataxis structure
---

This project adheres to the [Google Developer Documentation Style Guide](https://developers.google.com/style) and uses [Diataxis](https://diataxis.fr/) to structure content. Only project-specific conventions follow.

## Project-Specific Rules

| Rule                             | Specification                            |
| -------------------------------- | ---------------------------------------- |
| No horizontal rules (`---`)      | Fragments reading flow                   |
| No `####` headers                | Use bold text or admonitions instead     |
| No "Related" or "Next:" sections | Sidebar handles navigation               |
| No deeply nested lists           | Break into sections instead              |
| No code blocks for non-code      | Use admonitions for dialogue examples    |
| No bold paragraphs for callouts  | Use admonitions instead                  |
| 1-2 admonitions per section max  | Tutorials allow 3-4 per major section    |
| Table cells / list items         | 1-2 sentences max                        |
| Header budget                    | 8-12 `##` per doc; 2-3 `###` per section |

## Admonitions (Starlight Syntax)

```md
:::tip[Title]
Shortcuts, best practices
:::

:::note[Title]
Context, definitions, examples, prerequisites
:::

:::caution[Title]
Caveats, potential issues
:::

:::danger[Title]
Critical warnings only — data loss, security issues
:::
```

### Standard Uses

| Admonition               | Use For                       |
| ------------------------ | ----------------------------- |
| `:::note[Prerequisites]` | Dependencies before starting  |
| `:::tip[Quick Path]`     | TL;DR summary at document top |
| `:::caution[Important]`  | Critical caveats              |
| `:::note[Example]`       | Command/response examples     |

## Standard Table Formats

**Phases:**

```md
| Phase | Name     | What Happens                                 |
| ----- | -------- | -------------------------------------------- |
| 1     | Analysis | Brainstorm, research _(optional)_            |
| 2     | Planning | Requirements — PRD or tech-spec _(required)_ |
```

**Commands:**

```md
| Command      | Agent   | Purpose                              |
| ------------ | ------- | ------------------------------------ |
| `brainstorm` | Analyst | Brainstorm a new project             |
| `prd`        | PM      | Create Product Requirements Document |
```

## Folder Structure Blocks

Show in "What You've Accomplished" sections:

````md
```
your-project/
├── _bmad/                                   # BMad configuration
├── _bmad-output/
│   ├── planning-artifacts/
│   │   └── PRD.md                           # Your requirements document
│   ├── implementation-artifacts/
│   └── project-context.md                   # Implementation rules (optional)
└── ...
```
````

## Tutorial Structure

```text
1. Title + Hook (1-2 sentences describing outcome)
2. Version/Module Notice (info or warning admonition) (optional)
3. What You'll Learn (bullet list of outcomes)
4. Prerequisites (info admonition)
5. Quick Path (tip admonition - TL;DR summary)
6. Understanding [Topic] (context before steps - tables for phases/agents)
7. Installation (optional)
8. Step 1: [First Major Task]
9. Step 2: [Second Major Task]
10. Step 3: [Third Major Task]
11. What You've Accomplished (summary + folder structure)
12. Quick Reference (commands table)
13. Common Questions (FAQ format)
14. Getting Help (community links)
15. Key Takeaways (tip admonition)
```

### Tutorial Checklist

- [ ] Hook describes outcome in 1-2 sentences
- [ ] "What You'll Learn" section present
- [ ] Prerequisites in admonition
- [ ] Quick Path TL;DR admonition at top
- [ ] Tables for phases, commands, agents
- [ ] "What You've Accomplished" section present
- [ ] Quick Reference table present
- [ ] Common Questions section present
- [ ] Getting Help section present
- [ ] Key Takeaways admonition at end

## How-To Structure

```text
1. Title + Hook (one sentence: "Use the `X` workflow to...")
2. When to Use This (bullet list of scenarios)
3. When to Skip This (optional)
4. Prerequisites (note admonition)
5. Steps (numbered ### subsections)
6. What You Get (output/artifacts produced)
7. Example (optional)
8. Tips (optional)
9. Next Steps (optional)
```

### How-To Checklist

- [ ] Hook starts with "Use the `X` workflow to..."
- [ ] "When to Use This" has 3-5 bullet points
- [ ] Prerequisites listed
- [ ] Steps are numbered `###` subsections with action verbs
- [ ] "What You Get" describes output artifacts

## Explanation Structure

### Types

| Type              | Example                       |
| ----------------- | ----------------------------- |
| **Index/Landing** | `core-concepts/index.md`      |
| **Concept**       | `what-are-agents.md`          |
| **Feature**       | `quick-flow.md`               |
| **Philosophy**    | `why-solutioning-matters.md`  |
| **FAQ**           | `established-projects-faq.md` |

### General Template

```text
1. Title + Hook (1-2 sentences)
2. Overview/Definition (what it is, why it matters)
3. Key Concepts (### subsections)
4. Comparison Table (optional)
5. When to Use / When Not to Use (optional)
6. Diagram (optional - mermaid, 1 per doc max)
7. Next Steps (optional)
```

### Index/Landing Pages

```text
1. Title + Hook (one sentence)
2. Content Table (links with descriptions)
3. Getting Started (numbered list)
4. Choose Your Path (optional - decision tree)
```

### Concept Explainers

```text
1. Title + Hook (what it is)
2. Types/Categories (### subsections) (optional)
3. Key Differences Table
4. Components/Parts
5. Which Should You Use?
6. Creating/Customizing (pointer to how-to guides)
```

### Feature Explainers

```text
1. Title + Hook (what it does)
2. Quick Facts (optional - "Perfect for:", "Time to:")
3. When to Use / When Not to Use
4. How It Works (mermaid diagram optional)
5. Key Benefits
6. Comparison Table (optional)
7. When to Graduate/Upgrade (optional)
```

### Philosophy/Rationale Documents

```text
1. Title + Hook (the principle)
2. The Problem
3. The Solution
4. Key Principles (### subsections)
5. Benefits
6. When This Applies
```

### Explanation Checklist

- [ ] Hook states what document explains
- [ ] Content in scannable `##` sections
- [ ] Comparison tables for 3+ options
- [ ] Diagrams have clear labels
- [ ] Links to how-to guides for procedural questions
- [ ] 2-3 admonitions max per document

## Reference Structure

### Types

| Type              | Example               |
| ----------------- | --------------------- |
| **Index/Landing** | `workflows/index.md`  |
| **Catalog**       | `agents/index.md`     |
| **Deep-Dive**     | `document-project.md` |
| **Configuration** | `core-tasks.md`       |
| **Glossary**      | `glossary/index.md`   |
| **Comprehensive** | `bmgd-workflows.md`   |

### Reference Index Pages

```text
1. Title + Hook (one sentence)
2. Content Sections (## for each category)
   - Bullet list with links and descriptions
```

### Catalog Reference

```text
1. Title + Hook
2. Items (## for each item)
   - Brief description (one sentence)
   - **Commands:** or **Key Info:** as flat list
3. Universal/Shared (## section) (optional)
```

### Item Deep-Dive Reference

```text
1. Title + Hook (one sentence purpose)
2. Quick Facts (optional note admonition)
   - Module, Command, Input, Output as list
3. Purpose/Overview (## section)
4. How to Invoke (code block)
5. Key Sections (## for each aspect)
   - Use ### for sub-options
6. Notes/Caveats (tip or caution admonition)
```

### Configuration Reference

```text
1. Title + Hook
2. Table of Contents (jump links if 4+ items)
3. Items (## for each config/task)
   - **Bold summary** — one sentence
   - **Use it when:** bullet list
   - **How it works:** numbered steps (3-5 max)
   - **Output:** expected result (optional)
```

### Comprehensive Reference Guide

```text
1. Title + Hook
2. Overview (## section)
   - Diagram or table showing organization
3. Major Sections (## for each phase/category)
   - Items (### for each item)
   - Standardized fields: Command, Agent, Input, Output, Description
4. Next Steps (optional)
```

### Reference Checklist

- [ ] Hook states what document references
- [ ] Structure matches reference type
- [ ] Items use consistent structure throughout
- [ ] Tables for structured/comparative data
- [ ] Links to explanation docs for conceptual depth
- [ ] 1-2 admonitions max

## Glossary Structure

Starlight generates right-side "On this page" navigation from headers:

- Categories as `##` headers — appear in right nav
- Terms in tables — compact rows, not individual headers
- No inline TOC — right sidebar handles navigation

### Table Format

```md
## Category Name

| Term         | Definition                                                                               |
| ------------ | ---------------------------------------------------------------------------------------- |
| **Agent**    | Specialized AI persona with specific expertise that guides users through workflows.      |
| **Workflow** | Multi-step guided process that orchestrates AI agent activities to produce deliverables. |
```

### Definition Rules

| Do                            | Don't                                       |
| ----------------------------- | ------------------------------------------- |
| Start with what it IS or DOES | Start with "This is..." or "A [term] is..." |
| Keep to 1-2 sentences         | Write multi-paragraph explanations          |
| Bold term name in cell        | Use plain text for terms                    |

### Context Markers

Add italic context at definition start for limited-scope terms:

- `*Quick Flow only.*`
- `*BMad Method/Enterprise.*`
- `*Phase N.*`
- `*BMGD.*`
- `*Established projects.*`

### Glossary Checklist

- [ ] Terms in tables, not individual headers
- [ ] Terms alphabetized within categories
- [ ] Definitions 1-2 sentences
- [ ] Context markers italicized
- [ ] Term names bolded in cells
- [ ] No "A [term] is..." definitions

## FAQ Sections

```md
## Questions

- [Do I always need architecture?](#do-i-always-need-architecture)
- [Can I change my plan later?](#can-i-change-my-plan-later)

### Do I always need architecture?

Only for BMad Method and Enterprise tracks. Quick Flow skips to implementation.

### Can I change my plan later?

Yes. The SM agent has a `correct-course` workflow for handling scope changes.

**Have a question not answered here?** [Open an issue](...) or ask in [Discord](...).
```

## Validation Commands

Before submitting documentation changes:

```bash
npm run docs:fix-links            # Preview link format fixes
npm run docs:fix-links -- --write # Apply fixes
npm run docs:validate-links       # Check links exist
npm run docs:build                # Verify no build errors
```

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature Request
about: Suggest an idea or new feature
title: ''
labels: ''
assignees: ''
---

**Describe your idea**
A clear and concise description of what you'd like to see added or changed.

**Why is this needed?**
Explain the problem this solves or the benefit it brings to the BMad community.

**How should it work?**
Describe your proposed solution. If you have ideas on implementation, share them here.

**PR**
If you'd like to contribute, please indicate you're working on this or link to your PR. Please review [CONTRIBUTING.md](../../CONTRIBUTING.md) — contributions are always welcome!

**Additional context**
Add any other context, screenshots, or links that help explain your idea.

```

### File: .github\ISSUE_TEMPLATE\issue.md
```md
---
name: Issue
about: Report a problem or something that's not working
title: ''
labels: ''
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**Steps to reproduce**

1. What were you doing when the bug occurred?
2. What steps can recreate the issue?

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment (if relevant)**

- Model(s) used:
- Agentic IDE used:
- BMad version:
- Project language:

**Screenshots or links**
If applicable, add screenshots or links to help explain the problem.

**PR**
If you'd like to contribute a fix, please indicate you're working on it or link to your PR. See [CONTRIBUTING.md](../../CONTRIBUTING.md) — contributions are always welcome!

**Additional context**
Add any other context about the problem here. The more information you provide, the easier it is to help.

```

