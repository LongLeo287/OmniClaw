---
id: repo-fetched-bmad-module-creative-intelligence-suite-14
type: knowledge
owner: OA
registered_at: 2026-04-05T03:58:25.208228
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bmad-module-creative-intelligence-suite_142713

## Assimilation Report
Auto-cloned repository: FETCHED_bmad-module-creative-intelligence-suite_142713

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Creative Intelligence Suite

[![Version](https://img.shields.io/npm/v/bmad-creative-intelligence-suite?color=blue&label=version)](https://www.npmjs.com/package/bmad-creative-intelligence-suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Think differently.** A collection of agents and workflows for innovation, brainstorming, design thinking, and creative problem-solving.

## About CIS

The Creative Intelligence Suite (CIS) extends BMad Method with tools for the fuzzy front-end of development—where ideas are born, problems are reframed, and solutions emerge through structured creativity.

## Modules Included

| Agent/Workflow | Purpose |
|---------------|---------|
| **Innovation Strategist** | Identify disruption opportunities and business model innovation |
| **Design Thinking Coach** | Human-centered design through empathy, ideation, and prototyping |
| **Brainstorming Coach** | Facilitate creative ideation sessions with proven techniques |
| **Problem Solver** | Systematic problem diagnosis and root cause analysis |
| **Creative Problem Solver** | Generate creative solutions using lateral thinking |
| **Storyteller** | Craft compelling narratives for products and features |
| **Presentation Master** | Structure and deliver persuasive presentations |

## Installation

CIS is installed as a module during BMad Method setup:

```bash
npx bmad-method@alpha install
```

Select **Creative Intelligence Suite** from the modules list.

## Quick Start

After installing BMad Method with CIS, try these workflows:

```
/cis-brainstorm      # Generate ideas with structured techniques
/cis-design-thinking # Human-centered design process
/cis-problem-solve   # Systematic problem analysis
/cis-innovation      # Business model and disruption analysis
```

## When to Use CIS

| Situation | Use This |
|-----------|----------|
| Stuck on a problem | `/cis-problem-solve` |
| Need fresh ideas | `/cis-brainstorm` |
| Designing for users | `/cis-design-thinking` |
| Finding market gaps | `/cis-innovation` |
| Telling your product story | `/cis-storytelling` |
| Preparing a pitch | `/cis-presentation` |

## Example: Brainstorming Session

```
You: /cis-brainstorm
CIS: What would you like to brainstorm about?
You: Ways to improve user onboarding
CIS: Let's use the SCAMPER technique...
    [Guides you through 7 creative angles]
    [Generates diverse, actionable ideas]
```

## Workflow Capabilities

- **Idea Generation** — Multiple ideation frameworks (SCAMPER, Reverse Brainstorming, etc.)
- **Problem Reframing** — Turn obstacles into opportunities
- **User Empathy** — Build deep understanding of user needs
- **Solution Divergence** — Generate many options before converging
- **Narrative Craft** — Shape your product's story

## Team Collaboration

CIS includes team configurations for collaborative creativity:

- **Creative Squad** — Cross-functional creative sessions
- **Design Pair** — Two-person design thinking

## Documentation

**[Creative Intelligence Suite Documentation](http://cis-docs.bmad-method.org)** — Tutorials, how-to guides, and reference

- [Getting Started](http://cis-docs.bmad-method.org/tutorials/)
- [BMad Method Docs](http://docs.bmad-method.org) — Core framework documentation

## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Share your creative breakthroughs
- [GitHub Issues](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues) — Report issues

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**Creative Intelligence Suite** — Part of the [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) ecosystem.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/bmad-module-creative-intelligence-suite)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.

```

### File: CHANGELOG.md
```md
# CHANGELOG

## v0.1.9 - Mar 18, 2026

* Patch conversion rename of folder and conversion to skill format

## v0.1.8 - Feb 23, 2026

* Fix: use consistent YAML quoting in workflow descriptions

## v0.1.7 - Feb 22, 2026

* Add AGENTS.md with comprehensive development documentation, architecture overview, and schema validation guidance
* Convert test files from CommonJS to ES modules for better consistency
* Fix assert() calls to use assert.ok() for proper boolean validation
* Optimize workflow descriptions for skill selection with "Use when..." trigger patterns
* Remove redundant web_bundle sections from workflow configurations

## v0.1.6 - Feb 22, 2026

* Improve module-help.csv descriptions with "Use when..." clauses following '[Action]. Use [trigger].' pattern for better LLM comprehension

## v0.1.5 - Feb 8, 2026

* Add Astro + Starlight documentation site with comprehensive CIS documentation
* Add AI banner component to match BMAD-METHOD layout
* Remove _module-installer pattern for declarative directory creation
* Fix landing page layout to match BMAD-METHOD
* Fix docs workflow to use npm install instead of npm ci

## v0.1.4 - Feb 1, 2026

* Initial release

```

### File: CONTRIBUTING.md
```md
# Contributing to BMad

Thank you for considering contributing to the BMad project! We believe in **Human Amplification, Not Replacement** - bringing out the best thinking in both humans and AI through guided collaboration.

💬 **Discord Community**: Join our [Discord server](https://discord.gg/gk8jAdXWmj) for real-time discussions:

- **#bmad-development** - Technical discussions and development questions
- **#suggestions-feedback** - Feature ideas and suggestions
- **#report-bugs-and-issues** - Bug reports and issue discussions

## Our Philosophy

### BMad Core™: Universal Foundation

BMad Core empowers humans and AI agents working together in true partnership across any domain through our **C.O.R.E. Framework** (Collaboration Optimized Reflection Engine):

- **Collaboration**: Human-AI partnership where both contribute unique strengths
- **Optimized**: The collaborative process refined for maximum effectiveness
- **Reflection**: Guided thinking that helps discover better solutions and insights
- **Engine**: The powerful framework that orchestrates specialized agents and workflows

### BMad Method™: Agile AI-Driven Development

The BMad Method is the flagship bmad module for agile AI-driven software development. It emphasizes thorough planning and solid architectural foundations to provide detailed context for developer agents, mirroring real-world agile best practices.

### Core Principles

**Partnership Over Automation** - AI agents act as expert coaches, mentors, and collaborators who amplify human capability rather than replace it.

**Bidirectional Guidance** - Agents guide users through structured workflows while users push agents with advanced prompting. Both sides actively work to extract better information from each other.

**Systems of Workflows** - BMad Core builds comprehensive systems of guided workflows with specialized agent teams for any domain.

**Tool-Agnostic Foundation** - BMad Core remains tool-agnostic, providing stable, extensible groundwork that adapts to any domain.

## What Makes a Good Contribution?

Every contribution should strengthen human-AI collaboration. Ask yourself: **"Does this make humans and AI better together?"**

**✅ Contributions that align:**

- Enhance universal collaboration patterns
- Improve agent personas and workflows
- Strengthen planning and context continuity
- Increase cross-domain accessibility
- Add domain-specific modules leveraging BMad Core

**❌ What detracts from our mission:**

- Purely automated solutions that sideline humans
- Tools that don't improve the partnership
- Complexity that creates barriers to adoption
- Features that fragment BMad Core's foundation

## Before You Contribute

### Reporting Bugs

1. **Check existing issues** first to avoid duplicates
2. **Consider discussing in Discord** (#report-bugs-and-issues channel) for quick help
3. **Use the bug report template** when creating a new issue - it guides you through providing:
   - Clear bug description
   - Steps to reproduce
   - Expected vs actual behavior
   - Model/IDE/BMad version details
   - Screenshots or links if applicable
4. **Indicate if you're working on a fix** to avoid duplicate efforts

### Suggesting Features or New Modules

1. **Discuss first in Discord** (#suggestions-feedback channel) - the feature request template asks if you've done this
2. **Check existing issues and discussions** to avoid duplicates
3. **Use the feature request template** when creating an issue
4. **Be specific** about why this feature would benefit the BMad community and strengthen human-AI collaboration

### Before Starting Work

⚠️ **Required before submitting PRs:**

1. **For bugs**: Check if an issue exists (create one using the bug template if not)
2. **For features**: Discuss in Discord (#suggestions-feedback) AND create a feature request issue
3. **For large changes**: Always open an issue first to discuss alignment

Please propose small, granular changes! For large or significant changes, discuss in Discord and open an issue first. This prevents wasted effort on PRs that may not align with planned changes.

## Pull Request Guidelines

### Which Branch?

**Submit PR's to `main` branch** (critical only):

- 🚨 Critical bug fixes that break basic functionality
- 🔒 Security patches
- 📚 Fixing dangerously incorrect documentation
- 🐛 Bugs preventing installation or basic usage

### PR Size Guidelines

- **Ideal PR size**: 200-400 lines of code changes
- **Maximum PR size**: 800 lines (excluding generated files)
- **One feature/fix per PR**: Each PR should address a single issue or add one feature
- **If your change is larger**: Break it into multiple smaller PRs that can be reviewed independently
- **Related changes**: Even related changes should be separate PRs if they deliver independent value

### Breaking Down Large PRs

If your change exceeds 800 lines, use this checklist to split it:

- [ ] Can I separate the refactoring from the feature implementation?
- [ ] Can I introduce the new API/interface in one PR and implementation in another?
- [ ] Can I split by file or module?
- [ ] Can I create a base PR with shared utilities first?
- [ ] Can I separate test additions from implementation?
- [ ] Even if changes are related, can they deliver value independently?
- [ ] Can these changes be merged in any order without breaking things?

Example breakdown:

1. PR #1: Add utility functions and types (100 lines)
2. PR #2: Refactor existing code to use utilities (200 lines)
3. PR #3: Implement new feature using refactored code (300 lines)
4. PR #4: Add comprehensive tests (200 lines)

**Note**: PRs #1 and #4 could be submitted simultaneously since they deliver independent value.

### Pull Request Process

#### New to Pull Requests?

If you're new to GitHub or pull requests, here's a quick guide:

1. **Fork the repository** - Click the "Fork" button on GitHub to create your own copy
2. **Clone your fork** - `git clone https://github.com/YOUR-USERNAME/bmad-module-creative-intelligence-suite.git`
3. **Create a new branch** - Never work on `main` directly!
   ```bash
   git checkout -b fix/description
   # or
   git checkout -b feature/description
   ```
4. **Make your changes** - Edit files, keeping changes small and focused
5. **Commit your changes** - Use clear, descriptive commit messages
   ```bash
   git add .
   git commit -m "fix: correct typo in README"
   ```
6. **Push to your fork** - `git push origin fix/description`
7. **Create the Pull Request** - Go to your fork on GitHub and click "Compare & pull request"

### PR Description Template

Keep your PR description concise and focused. Use this template:

```markdown
## What

[1-2 sentences describing WHAT changed]

## Why

[1-2 sentences explaining WHY this change is needed]
Fixes #[issue number] (if applicable)

## How

## [2-3 bullets listing HOW you implemented it]

-
-

## Testing

[1-2 sentences on how you tested this]
```

**Maximum PR description length: 200 words** (excluding code examples if needed)

### Good vs Bad PR Descriptions

❌ **Bad Example:**

> This revolutionary PR introduces a paradigm-shifting enhancement to the system's architecture by implementing a state-of-the-art solution that leverages cutting-edge methodologies to optimize performance metrics...

✅ **Good Example:**

> **What:** Added validation for agent dependency resolution
> **Why:** Build was failing silently when agents had circular dependencies
> **How:**
>
> - Added cycle detection in dependency-resolver.js
> - Throws clear error with dependency chain
>   **Testing:** Tested with circular deps between 3 agents

### Commit Message Convention

Use conventional commits format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code change that neither fixes a bug nor adds a feature
- `test:` Adding missing tests
- `chore:` Changes to build process or auxiliary tools

Keep commit messages under 72 characters.

### Atomic Commits

Each commit should represent one logical change:

- **Do:** One bug fix per commit
- **Do:** One feature addition per commit
- **Don't:** Mix refactoring with bug fixes
- **Don't:** Combine unrelated changes

## What Makes a Good Pull Request?

✅ **Good PRs:**

- Change one thing at a time
- Have clear, descriptive titles
- Explain what and why in the description
- Include only the files that need to change
- Reference related issue numbers

❌ **Avoid:**

- Changing formatting of entire files
- Multiple unrelated changes in one PR
- Copying your entire project/repo into the PR
- Changes without explanation
- Working directly on `main` branch

## Common Mistakes to Avoid

1. **Don't reformat entire files** - only change what's necessary
2. **Don't include unrelated changes** - stick to one fix/feature per PR
3. **Don't paste code in issues** - create a proper PR instead
4. **Don't submit your whole project** - contribute specific improvements

## Prompt & Agent Guidelines

- Keep dev agents lean - they need context for coding, not documentation
- Web/planning agents can be larger with more complex tasks
- Everything is natural language (markdown) - no code in core framework
- Use bmad modules for domain-specific features
- Validate YAML schemas with `npm run validate:schemas` before committing

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. We foster a collaborative, respectful environment focused on building better human-AI partnerships.

## Need Help?

- 💬 Join our [Discord Community](https://discord.gg/gk8jAdXWmj):
  - **#bmad-development** - Technical questions and discussions
  - **#suggestions-feedback** - Feature ideas and suggestions
  - **#report-bugs-and-issues** - Get help with bugs before filing issues
- 🐛 Report bugs using the [bug report template](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues/new?template=bug_report.md)
- 💡 Suggest features using the [feature request template](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues/new?template=feature_request.md)
- 📖 Browse the [GitHub Discussions](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/discussions)

---

**Remember**: We're here to help! Don't be afraid to ask questions. Every expert was once a beginner. Together, we're building a future where humans and AI work better together.

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

```

### File: CONTRIBUTORS.md
```md
# Contributors

The Creative Intelligence Suite is made possible by contributions from our community. We gratefully acknowledge everyone who has helped improve this project.

## How We Credit Contributors

- **Git history** — Every contribution is preserved in the project's commit history
- **Contributors badge** — See the dynamic contributors list on our [README](README.md)
- **GitHub contributors graph** — Visual representation at <https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/graphs/contributors>

## Becoming a Contributor

Anyone who submits a pull request that is merged becomes a contributor. Contributions include:

- Bug fixes
- New agents or workflows
- Documentation improvements
- Bug reports and issue triaging
- Code reviews
- Helping others in discussions

There are no minimum contribution requirements — whether it's a one-character typo fix or a major feature, we value all contributions.

## Copyright

The Creative Intelligence Suite project is copyrighted by BMad Code, LLC. Individual contributions are licensed under the same MIT License as the project. Contributors retain authorship credit through Git history and the contributors graph.

---

**Thank you to everyone who has helped make the Creative Intelligence Suite better!**

For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bmad_module_creative_intelligence_suite
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\index.md
```md
---
title: Welcome
description: Creative Intelligence Suite - Innovation, brainstorming, and problem-solving
---

# Creative Intelligence Suite

A collection of agents and workflows for innovation, brainstorming, design thinking, and creative problem-solving.

---

## What is CIS?

The Creative Intelligence Suite (CIS) extends BMad Method with tools for the fuzzy front-end of development—where ideas are born, problems are reframed, and solutions emerge through structured creativity.

## Available Agents

| Agent/Workflow | Purpose |
|---------------|---------|
| **Innovation Strategist** | Identify disruption opportunities and business model innovation |
| **Design Thinking Coach** | Human-centered design through empathy, ideation, and prototyping |
| **Brainstorming Coach** | Facilitate creative ideation sessions with proven techniques |
| **Problem Solver** | Systematic problem diagnosis and root cause analysis |
| **Creative Problem Solver** | Generate creative solutions using lateral thinking |
| **Storyteller** | Craft compelling narratives for products and features |
| **Presentation Master** | Structure and deliver persuasive presentations |

---

## Quick Links

| Section | Purpose |
| ------- | ------- |
| **[Tutorials](/tutorials/)** | Get started with CIS workflows |
| **[How-To Guides](/how-to/)** | Practical guides for specific tasks |
| **[Explanation](/explanation/)** | Learn how CIS works |
| **[Reference](/reference/)** | Technical reference |

---

## Getting Started

New to CIS? Start with the [Getting Started tutorial](/tutorials/getting-started.md) to learn how to:

- Install CIS with BMad Method
- Run your first brainstorming session
- Apply design thinking to user challenges
- Develop innovation strategies
- Solve problems systematically
- Craft compelling stories

---

## Community

- **[Discord](https://discord.gg/gk8jAdXWmj)** — Share your creative breakthroughs
- **[GitHub](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** — Source code and issues
- **[BMad Method Docs](https://docs.bmad-method.org)** — Core framework documentation

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**Steps to Reproduce**
What lead to the bug and can it be reliable recreated - if so with what steps.

**PR**
If you have an idea to fix and would like to contribute, please indicate here you are working on a fix, or link to a proposed PR to fix the issue. Please review the contribution.md - contributions are always welcome!

**Expected behavior**
A clear and concise description of what you expected to happen.

**Please be Specific if relevant**
Model(s) Used:
Agentic IDE Used:
WebSite Used:
Project Language:
BMad Method version:

**Screenshots or Links**
If applicable, add screenshots or links (if web sharable record) to help explain your problem.

**Additional context**
Add any other context about the problem here. The more information you can provide, the easier it will be to suggest a fix or resolve

```

