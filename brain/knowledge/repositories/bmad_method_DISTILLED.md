---
id: repo-fetched-bmad-method-142655
type: knowledge
owner: OA
registered_at: 2026-04-05T03:58:04.900369
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_BMAD-METHOD_142655

## Assimilation Report
Auto-cloned repository: FETCHED_BMAD-METHOD_142655

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Build More Architect Dreams** — An AI-driven agile development module for the BMad Method Module Ecosystem, the best and most comprehensive Agile AI Driven Development framework that has true scale-adaptive intelligence that adjusts from bug fixes to enterprise systems.

**100% free and open source.** No paywalls. No gated content. No gated Discord. We believe in empowering everyone, not just those who can pay for a gated community or courses.

## Why the BMad Method?

Traditional AI tools do the thinking for you, producing average results. BMad agents and facilitated workflows act as expert collaborators who guide you through a structured process to bring out your best thinking in partnership with the AI.

- **AI Intelligent Help** — Invoke the `bmad-help` skill anytime for guidance on what's next
- **Scale-Domain-Adaptive** — Automatically adjusts planning depth based on project complexity
- **Structured Workflows** — Grounded in agile best practices across analysis, planning, architecture, and implementation
- **Specialized Agents** — 12+ domain experts (PM, Architect, Developer, UX, and more)
- **Party Mode** — Bring multiple agent personas into one session to collaborate and discuss
- **Complete Lifecycle** — From brainstorming to deployment

[Learn more at **docs.bmad-method.org**](https://docs.bmad-method.org)

---

## 🚀 What's Next for BMad?

**V6 is here and we're just getting started!** The BMad Method is evolving rapidly with optimizations including Cross Platform Agent Team and Sub Agent inclusion, Skills Architecture, BMad Builder v1, Dev Loop Automation, and so much more in the works.

**[📍 Check out the complete Roadmap →](https://docs.bmad-method.org/roadmap/)**

---

## Quick Start

**Prerequisites**: [Node.js](https://nodejs.org) v20+

```bash
npx bmad-method install
```

> Want the newest prerelease build? Use `npx bmad-method@next install`. Expect higher churn than the default install.

Follow the installer prompts, then open your AI IDE (Claude Code, Cursor, etc.) in your project folder.

**Non-Interactive Installation** (for CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[See all installation options](https://docs.bmad-method.org/how-to/non-interactive-installation/)

> **Not sure what to do?** Ask `bmad-help` — it tells you exactly what's next and what's optional. You can also ask questions like `bmad-help I just finished the architecture, what do I do next?`

## Modules

BMad Method extends with official modules for specialized domains. Available during installation or anytime after.

| Module                                                                                                            | Purpose                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | Core framework with 34+ workflows                 |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | Create custom BMad agents and workflows           |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | Risk-based test strategy and automation           |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | Game development workflows (Unity, Unreal, Godot) |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Innovation, brainstorming, design thinking        |

## Documentation

[BMad Method Docs Site](https://docs.bmad-method.org) — Tutorials, guides, concepts, and reference

**Quick links:**
- [Getting Started Tutorial](https://docs.bmad-method.org/tutorials/getting-started/)
- [Upgrading from Previous Versions](https://docs.bmad-method.org/how-to/upgrade-to-v6/)
- [Test Architect Documentation](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)


## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Get help, share ideas, collaborate
- [Subscribe on YouTube](https://www.youtube.com/@BMadCode) — Tutorials, master class, and podcast (launching Feb 2025)
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) — Bug reports and feature requests
- [Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions) — Community conversations

## Support BMad

BMad is free for everyone — and always will be. If you'd like to support development:

- ⭐ Please click the star project icon near the top right of this page
- ☕ [Buy Me a Coffee](https://buymeacoffee.com/bmad) — Fuel the development
- 🏢 Corporate sponsorship — DM on Discord
- 🎤 Speaking & Media — Available for conferences, podcasts, interviews (BM on Discord)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**BMad** and **BMAD-METHOD** are trademarks of BMad Code, LLC. See [TRADEMARK.md](TRADEMARK.md) for details.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.

```

### File: AGENTS.md
```md
# BMAD-METHOD

Open source framework for structured, agent-assisted software delivery.

## Rules

- Use Conventional Commits for every commit.
- Before pushing, run `npm ci && npm run quality` on `HEAD` in the exact checkout you are about to push.
  `quality` mirrors the checks in `.github/workflows/quality.yaml`.

- Skill validation rules are in `tools/skill-validator.md`.
- Deterministic skill checks run via `npm run validate:skills` (included in `quality`).

```

### File: CHANGELOG.md
```md
# Changelog

## v6.2.2 - 2026-03-25

### ♻️ Refactoring

* Modernize module-help CSV to 13-column format with `after`/`before` dependency graph replacing sequence numbers (#2120)
* Rewrite bmad-help from procedural 8-step execution to outcome-based skill design (~50% shorter) (#2120)

### 🐛 Bug Fixes

* Update bmad-builder module-definition path from `src/module.yaml` to `skills/module.yaml` for bmad-builder v1.2.0 compatibility (#2126)
* Fix eslint config to ignore gitignored lock files (#2120)

### 📚 Documentation

* Close Epic 4.5 explanation gaps in Chinese (zh-CN): normalize command naming to current `bmad-*` convention and add cross-links across 9 explanation pages (#2102)

## v6.2.1 - 2026-03-24

### 🎁 Highlights

* Full rewrite of code-review skill with sharded step-file architecture, three parallel review layers (Blind Hunter, Edge Case Hunter, Acceptance Auditor), and interactive post-review triage (#2007, #2013, #2055)
* Quick Dev workflow overhaul: smart intent cascade, self-check gate, VS Code integration, clickable spec links, and spec rename (#2105, #2104, #2039, #2085, #2109)
* Add review trail generation with clickable `path:line` stops in spec file (#2033)
* Add clickable spec links using spec-file-relative markdown format (#2085, #2049)
* Preserve tracking identifiers in spec slug derivation (#2108)
* Deterministic skill validator with 19 rules across 6 categories, integrated into CI (#1981, #1982, #2004, #2002, #2051)
* Complete French (fr-FR) documentation translation (#2073)
* Add Ona platform support (#1968)
* Rename tech-spec → spec across templates and all documentation (#2109)

### 📚 Documentation

* Complete French (fr-FR) translation of all documentation with workflow diagrams (#2073)
* Refine Chinese (zh-CN) documentation: epic stories, how-to guides, getting-started, entry copy, help, anchor links (#2092–#2099, #2072)
* Add Chinese translation for core-tools reference (#2002)

## v6.2.0 - 2026-03-15

### 🎁 Highlights

* Fix manifest generation so BMad Builder installs correctly when a module has no agents (#1998)
* Prototype preview of bmad-product-brief-preview skill — try `/bmad-product-brief-preview` and share feedback! (#1959)
* All skills now use native skill directory format for improved modularity and maintainability (#1931, #1945, #1946, #1949, #1950, #1984, #1985, #1988, #1994)

### 🎁 Features

* Rewrite code-review skill with sharded step-file architecture and auto-detect review intent from invocation args (#2007, #2013)
* Add inference-based skill validator with comprehensive rules for naming, variables, paths, and invocation syntax (#1981)
* Add REF-03 skill invocation language rule and PATH-05 skill encapsulation rule to validator (#2004)

### 🐛 Bug Fixes

* Validation pass 2 — fix path, variable, and sequence issues across 32 files (#2008)
* Replace broken party-mode workflow refs with skill syntax (#2000)
* Improve bmad-help description for accurate trigger matching (#2012)
* Point zh-cn doc links to Chinese pages instead of English (#2010)
* Validation cleanup for bmad-quick-flow (#1997), 6 skills batch (#1996), bmad-sprint-planning (#1995), bmad-retrospective (#1993), bmad-dev-story (#1992), bmad-create-story (#1991), bmad-code-review (#1990), bmad-create-epics-and-stories (#1989), bmad-create-architecture (#1987), bmad-check-implementation-readiness (#1986), bmad-create-ux-design (#1983), bmad-create-product-brief (#1982)

### 🔧 Maintenance

* Normalize skill invocation syntax to `Invoke the skill` pattern repo-wide (#2004)

### 📚 Documentation

* Add Chinese translation for core-tools reference (#2002)
* Update version hint, TEA module link, and HTTP→HTTPS links in Chinese README (#1922, #1921)

## [6.1.0] - 2026-03-12

### Highlights

* Whiteport Design Studio (WDS) module enabled in the installer
* Support @next installation channel (`npx bmad-method@next install`) — get the latest tip of main instead of waiting for the next stable published version
* Everything now installs as a skill — all workflows, agents, and tasks converted to markdown with SKILL.md entrypoints (not yet optimized skills, but unified format)
* An experimental preview of the new Quick Dev is available, which will become the main Phase 4 development tool
* Edge Case Hunter added as a parallel code review layer in Phase 4, improving code quality by exhaustively tracing branching paths and boundary conditions (#1791)
* Documentation now available in Chinese (zh-CN) with complete translation (#1822, #1795)

### 💥 Breaking Changes

* Convert entire BMAD method to skills-based architecture with unified skill manifests (#1834)
* Convert all core workflows from YAML+instructions to single workflow.md format
* Migrate all remaining platforms to native Agent Skills format (#1841)
* Remove legacy YAML/XML workflow engine plumbing (#1864)

### 🎁 Features

* Add Pi coding agent as supported platform (#1854)
* Add unified skill scanner decoupled from legacy collectors (#1859)
* Add continuous delivery workflows for npm publishing with trusted OIDC publishing (#1872)

### ♻️ Refactoring

* Update terminology from "commands" to "skills" across all documentation (#1850)

### 🐛 Bug Fixes

* Fix code review removing mandatory minimum issue count that caused infinite review loops (#1913)
* Fix silent loss of brainstorming ideas in PRD by adding reconciliation step (#1914)
* Reduce npm tarball from 533 to 348 files (91% size reduction, 6.2 MB → 555 KB) via .npmignore (#1900)
* Fix party-mode skill conversion review findings (#1919)

---

## [6.0.4]

### 🎁 Features

* Add edge case hunter review task - new reusable review task that exhaustively traces branching paths and boundary conditions in code, reporting only unhandled gaps. Method-driven analysis complementary to adversarial review (#1790)

### 🐛 Bug Fixes

* Fix brainstorming to not overwrite previous sessions; now prompts to continue existing brainstorming or start a new one when older brainstorming sessions are found
* Fix installer templates - replace legacy `@` path prefixes with explicit `{project-root}` syntax for consistency (#1769)
* Fix edge case hunter - remove zero-findings halt condition that was pressuring the LLM to hallucinate findings when none legitimately exist (#1797)
* Fix broken docs domain references in README and GitHub issue templates (#1777)

---

## [6.0.3]

### 🎁 Features

* Add bmad-os-root-cause-analysis skill for analyzing bug-fix commits and producing structured root cause analysis reports with pyramid communication format (#1741)

### 🐛 Bug Fixes

* Fix installer to refuse installation when ancestor directory has BMAD commands, preventing duplicate command autocompletion in nested directories (#1735)
* Fix OpenCode integration by replacing unsupported `name` frontmatter with `mode: all` and update directory names to plural form (#1764)
* Fix CSV manifest pipeline double-escaping of quotes that was corrupting output files; switch Gemini templates to single quotes (#1746)
* Fix workflow descriptions to use proper quotes so they format better in skill conversion and don't break yaml front matter
* Fix workflow help task chaining by removing ambiguous "with-argument" clause that caused LLMs to misinterpret help.md as skill calls (#1740)

### ♻️ Refactoring

* Standardize all workflow descriptions to use proper quotes to prevent breaking command or skill front matter during skill conversion

### 📚 Documentation

* Fix broken TEA hyperlinks to point to new repository URL (#1772)
* Rebrand BMAD acronym to "Build More Architect Dreams" across documentation (#1765)

---

## [6.0.2]

### 🎁 Features

* Add CodeBuddy platform support with installer configuration (#1483)
* Add LLM audit prompt for file reference conventions - new audit tool using parallel subagents (#1720)
* Migrate Codex installer from `.codex/prompts` to `.agents/skills` format to align with Codex CLI changes (#1729)
* Convert review-pr and audit-file-refs tools to proper bmad-os skills with slash commands `bmad-os-review-pr` and `bmad-os-audit-file-refs` (#1732)

### 🐛 Bug Fixes

* Fix 24 broken step references in create-architecture workflow after directory rename (#1734)
* Fix step file path references in check-implementation-readiness workflow (#1709, #1716)
* Fix 3 broken file references and enable strict file reference validation in CI (#1717)
* Fix Rovo Dev integration with custom installer that generates prompts.yml manifest (#1701)
* Fix 104 relative step file references to use standardized `{project-root}/_bmad/` paths across 68 files (#1722)
* Fix code fence imbalance in step-03-starter.md that caused rendering issues (#1724)
* Remove Windsurf from recommended/preferred IDEs list (#1727)
* Fix default Codex install location from global to project for better defaults (#1698)
* Add npx cache workaround to Quick Start for stale beta versions (#1685)
* Add language instructions to replace placeholder text in Research overview (#1703)
* Ignore `.junie/` IDE integration folder in git and prettier configs (#1719)

### ♻️ Refactoring

* Update open source tool skills structure for future plugin migration
* Standardize all workflow descriptions for skill generation with concise format and explicit trigger phrases
* Remove `disable-model-invocation` flag from all IDE installer templates to enable workflow skill calls

### 📚 Documentation

* Elevate `bmad-help` as primary on-ramp across all documentation
* Update workflow names with `bmad-bmm-` prefix and standardize table formatting
* Clarify phase routing and catalog path in help task

---

## [6.0.0]

V6 Stable Release! The End of Beta!

### 🎁 Features

* Add PRD workflow steps 2b (vision/differentiators) and 2c (executive summary) for more complete product requirements documentation
* Add new `bmad uninstall` command with interactive and non-interactive modes for selective component removal
* Add dedicated GitHub Copilot installer that generates enriched `.agent.md`, `.prompt.md` files and project configuration
* Add TEA browser automation prerequisite prompts to guide Playwright CLI/MCP setup after configuration

### 🐛 Bug Fixes

* Fix version comparison to use semantic versioning, preventing incorrect downgrade recommendations to older beta versions
* Fix `--custom-content` flag to properly populate sources and selected files in module config
* Fix module configuration UX messaging to show accurate completion status and improve feedback timing
* Fix changelog URL in installer start message for proper GitHub resolution
* Remove incorrect `mode: primary` from OpenCode agent template and restore `name` field across all templates
* Auto-discover PRD files in validate-prd workflow to reduce manual path input
* Fix installer non-interactive mode hanging and improve IDE configuration handling during updates
* Fix workflow-level config.yaml copying for custom content modules

### ♻️ Refactoring

* Remove alias variables from Phase 4 workflows, use canonical `{implementation_artifacts}` and `{planning_artifacts}`
* Add missing `project_context` references to workflows for consistency

### 📚 Documentation

* Add post-install notes documentation for modules
* Improve project-context documentation and fix folder structure
* Add BMad Builder link to index for extenders

---

## [6.0.0-Beta.8]

**Release: February 8, 2026**

### 🌟 Key Highlights

1. **Non-Interactive Installation** — Full CI/CD support with 10 new CLI flags for automated deployments
2. **Complete @clack/prompts Migration** — Unified CLI experience with consolidated installer output
3. **CSV File Reference Validation** — Extended Layer 1 validator to catch broken workflow references in CSV files
4. **Kiro IDE Support** — Standardized config-driven installation, replacing custom installer

### 🎁 Features

* **Non-Interactive Installation** — Added `--directory`, `--modules`, `--tools`, `--custom-content`, `--user-name`, `--communication-language`, `--document-output-language`, `--output-folder`, and `-y/--yes` flags for CI/CD automation (#1520)
* **CSV File Reference Validation** — Extended validator to scan `.csv` files for broken workflow references, checking 501 references across 212 files (#1573)
* **Kiro IDE Support** — Replaced broken custom installer with config-driven templates using `#[[file:...]]` syntax and `inclusion: manual` frontmatter (#1589)
* **OpenCode Template Consolidation** — Combined split templates with `mode: primary` frontmatter for Tab-switching support, fixing agent discovery (#1556)
* **Modules Reference Page** — Added official external modules reference documentation (#1540)

### 🐛 Bug Fixes

* **Installer Streamlining** — Removed "None - Skip module installation" option, eliminated ~100 lines of dead code, and added ESM/.cjs support for module installers (#1590)
* **CodeRabbit Workflow** — Changed `pull_request` to `pull_request_target` to fix 403 errors and enable reviews on fork PRs (#1583)
* **Party Mode Return Protocol** — Added RETURN PROTOCOL to prevent lost-in-the-middle failures after Party Mode completes (#1569)
* **Spacebar Toggle** — Fixed SPACE key not working in autocomplete multiselect prompts for tool/IDE selection (#1557)
* **OpenCode Agent Routing** — Fixed agents installing to wrong directory by adding `targets` array for routing `.opencode/agent/` vs `.opencode/command/` (#1549)
* **Technical Research Workflow** — Fixed step-05 routing to step-06 and corrected `stepsCompleted` values (#1547)
* **Forbidden Variable Removal** — Removed `workflow_path` variable from 16 workflow step files (#1546)
* **Kilo Installer** — Fixed YAML formatting issues by trimming activation header and converting to yaml.parse/stringify (#1537)
* **bmad-help** — Now reads project-specific docs and respects `communication_language` setting (#1535)
* **Cache Errors** — Removed `--prefer-offline` npm flag to prevent stale cache errors during installation (#1531)

### ♻️ Refactoring

* **Complete @clack/prompts Migration** — Migrated 24 files from legacy libraries (ora, chalk, boxen, figlet, etc.), replaced ~100 console.log+chalk calls, consolidated installer output to single spinner, and removed 5 dependencies (#1586)
* **Downloads Page Removal** — Removed downloads page, bundle generation, and archiver dependency in favor of GitHub's native archives (#1577)
* **Workflow Verb Standardization** — Replaced "invoke/run" with "load and follow/load" in review workflow prompts (#1570)
* **Documentation Language** — Renamed "brownfield" to "established projects" and flattened directory structure for accessibility (#1539)

### 📚 Documentation

* **Comprehensive Site Review** — Fixed broken directory tree diagram, corrected grammar/capitalization, added SEO descriptions, and reordered how-to guides (#1578)
* **SEO Metadata** — Added description front matter to 9 documentation pages for search engine optimization (#1566)
* **PR Template** — Added pull request template for consistent PR descriptions (#1554)
* **Manual Release Cleanup** — Removed broke
... [TRUNCATED]
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

Submit PRs to the `main` branch. We use trunk-based development. Every push to `main` auto-publishes to `npm` under the `next` tag. Stable releases are cut ~weekly to the `latest` tag.

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

| ✅ Do                        | ❌ Don't                      |
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
- Validate file references: `npm run validate:refs`

### File-Pattern-to-Validator Mapping

| File Pattern | Validator | Extraction Function |
| ------------ | --------- | ------------------- |
| `*.yaml`, `*.yml` | `validate-file-refs.js` | `extractYamlRefs` |
| `*.md`, `*.xml` | `validate-file-refs.js` | `extractMarkdownRefs` |
| `*.csv` | `validate-file-refs.js` | `extractCsvRefs` |

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

### File: README_CN.md
```md
![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**筑梦架构（Build More Architect Dreams）** —— 简称 “BMAD 方法”，面向 BMad 模块生态的 AI 驱动敏捷开发方法。它会随项目复杂度调整工作深度，从日常 bug 修复到企业级系统建设都能适配。

**100% 免费且开源。** 没有付费墙，没有封闭内容，也没有封闭 Discord。我们希望每个人都能平等获得高质量的人机协作开发方法。

## 为什么选择 BMad 方法？

传统 AI 工具常常替你思考，结果往往止于“能用”。BMad 通过专业智能体和引导式工作流，让 AI 成为协作者：流程有结构，决策有依据，产出更稳定。

- **AI 智能引导** —— 随时调用 `bmad-help` 获取下一步建议
- **规模与领域自适应** —— 按项目复杂度自动调整规划深度
- **结构化工作流** —— 覆盖分析、规划、架构、实施全流程
- **专业角色智能体** —— 提供 PM、架构师、开发者、UX 等 12+ 角色
- **派对模式** —— 多个智能体可在同一会话协作讨论
- **完整生命周期** —— 从头脑风暴一路到交付上线

[在 **docs.bmad-method.org** 了解更多](https://docs.bmad-method.org/zh-cn/)

---

## 🚀 BMad 的下一步是什么？

**V6 已经上线，而这只是开始。** BMad 仍在快速演进：跨平台智能体团队与子智能体集成、Skills 架构、BMad Builder v1、Dev Loop 自动化等能力都在持续推进。

**[📍 查看完整路线图 →](https://docs.bmad-method.org/zh-cn/roadmap/)**

---

## 快速开始

**先决条件**：[Node.js](https://nodejs.org) v20+

```bash
npx bmad-method install
```

> 想体验最新预发布版本？可使用 `npx bmad-method@next install`。它比默认版本更新更快，也可能更容易发生变化。

按照安装程序提示操作，然后在项目文件夹中打开你的 AI IDE（Claude Code、Cursor 等）。

**非交互式安装**（用于 CI/CD）：

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[查看非交互式安装选项](https://docs.bmad-method.org/zh-cn/how-to/non-interactive-installation/)

> **不确定下一步？** 直接问 `bmad-help`。它会告诉你“必做什么、可选什么”，例如：`bmad-help 我刚完成架构设计，接下来做什么？`

## 模块

BMad 可通过官方模块扩展到不同专业场景。你可以在安装时选择，也可以后续随时补装。

| 模块                                                                                                                | 用途                           |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | 核心框架，内含 34+ 工作流         |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | 创建自定义 BMad 智能体与工作流     |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | 基于风险的测试策略与自动化         |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | 游戏开发工作流（Unity/Unreal/Godot） |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | 创新、头脑风暴、设计思维           |

## 文档

[BMad 方法文档站点](https://docs.bmad-method.org/zh-cn/) — 教程、指南、概念和参考

**快速链接：**
- [入门教程](https://docs.bmad-method.org/zh-cn/tutorials/getting-started/)
- [从旧版本升级](https://docs.bmad-method.org/zh-cn/how-to/upgrade-to-v6/)
- [测试架构师文档（英文）](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)

## 社区

- [Discord](https://discord.gg/gk8jAdXWmj) — 获取帮助、分享想法、协作
- [在 YouTube 上订阅](https://www.youtube.com/@BMadCode) — 教程、大师课和播客（2025 年 2 月推出）
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) — 错误报告和功能请求
- [讨论](https://github.com/bmad-code-org/BMAD-METHOD/discussions) — 社区对话

## 支持 BMad

BMad 对所有人免费，而且会一直免费。如果你愿意支持项目发展：

- ⭐ 给仓库点个 Star
- ☕ [请我喝咖啡](https://buymeacoffee.com/bmad) — 为开发提供动力
- 🏢 企业赞助 — 在 Discord 上私信
- 🎤 演讲与媒体 — 可参加会议、播客、采访（在 Discord 上联系 BM）

## 贡献

我们欢迎贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

## 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。

---

**BMad** 和 **BMAD-METHOD** 是 BMad Code, LLC 的商标。详见 [TRADEMARK.md](TRADEMARK.md)。

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

请参阅 [CONTRIBUTORS.md](CONTRIBUTORS.md) 了解贡献者信息。

```

### File: README_VN.md
```md
![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

[English](README.md) | [简体中文](README_CN.md) | Tiếng Việt

**Build More Architect Dreams** - một mô-đun khung phát triển hướng AI trong hệ sinh thái BMad, có khả năng thích ứng theo quy mô từ sửa lỗi nhỏ đến các hệ thống doanh nghiệp.

**100% miễn phí và mã nguồn mở.** Không có tường phí. Không có nội dung bị khóa. Không có Discord giới hạn quyền truy cập. Chúng tôi tin vào việc trao quyền cho mọi người, không chỉ cho những ai có thể trả tiền để vào một cộng đồng hay khóa học khép kín.

## Vì sao chọn BMad Method?

Các công cụ AI truyền thống thường làm thay phần suy nghĩ của bạn và tạo ra kết quả ở mức trung bình. Các agent chuyên biệt và quy trình làm việc có hướng dẫn của BMad hoạt động như những cộng tác viên chuyên gia, dẫn dắt bạn qua một quy trình có cấu trúc để khai mở tư duy tốt nhất của bạn cùng với AI.

- **Trợ giúp AI thông minh** - Gọi skill `bmad-help` bất kỳ lúc nào để biết bước tiếp theo
- **Thích ứng theo quy mô và miền bài toán** - Tự động điều chỉnh độ sâu lập kế hoạch theo độ phức tạp của dự án
- **Quy trình có cấu trúc** - Dựa trên các thực hành tốt nhất của agile xuyên suốt phân tích, lập kế hoạch, kiến trúc và triển khai
- **Agent chuyên biệt** - Hơn 12 chuyên gia theo vai trò như PM, Architect, Developer, UX, Scrum Master và nhiều vai trò khác
- **Party Mode** - Đưa nhiều persona agent vào cùng một phiên để cộng tác và thảo luận
- **Vòng đời hoàn chỉnh** - Từ động não ý tưởng cho đến triển khai

[Tìm hiểu thêm tại **docs.bmad-method.org**](https://docs.bmad-method.org/vi-vn/)

---

## 🚀 Điều gì tiếp theo cho BMad?

**V6 đã có mặt và đây mới chỉ là khởi đầu!** BMad Method đang phát triển rất nhanh với các cải tiến như đội agent đa nền tảng và tích hợp sub-agent, kiến trúc Skills, BMad Builder v1, tự động hóa vòng lặp phát triển và nhiều thứ khác vẫn đang được xây dựng.

**[📍 Xem lộ trình đầy đủ →](https://docs.bmad-method.org/vi-vn/roadmap/)**

---

## Bắt đầu nhanh

**Điều kiện tiên quyết**: [Node.js](https://nodejs.org) v20+

```bash
npx bmad-method install
```

> Muốn dùng bản prerelease mới nhất? Hãy dùng `npx bmad-method@next install`. Hãy kỳ vọng mức độ biến động cao hơn bản cài đặt mặc định.

Làm theo các lời nhắc của trình cài đặt, sau đó mở AI IDE của bạn như Claude Code hoặc Cursor trong thư mục dự án.

**Cài đặt không tương tác** (cho CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[Xem toàn bộ tùy chọn cài đặt](https://docs.bmad-method.org/vi-vn/how-to/non-interactive-installation/)

> **Chưa chắc nên làm gì?** Hãy hỏi `bmad-help` - nó sẽ cho bạn biết chính xác bước nào tiếp theo và bước nào là tùy chọn. Bạn cũng có thể hỏi kiểu như `bmad-help Tôi vừa hoàn thành phần kiến trúc, tiếp theo tôi cần làm gì?`

## Mô-đun

BMad Method có thể được mở rộng bằng các mô-đun chính thức cho những miền chuyên biệt. Chúng có sẵn trong lúc cài đặt hoặc bất kỳ lúc nào sau đó.

| Module                                                                                                            | Mục đích                                           |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | Khung lõi với hơn 34 quy trình                     |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | Tạo agent và quy trình BMad tùy chỉnh             |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | Chiến lược kiểm thử và tự động hóa dựa trên rủi ro |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | Quy trình phát triển game (Unity, Unreal, Godot)   |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Đổi mới, động não ý tưởng, tư duy thiết kế         |

## Tài liệu

[Trang tài liệu BMad Method](https://docs.bmad-method.org/vi-vn/) - bài hướng dẫn, hướng dẫn tác vụ, giải thích khái niệm và tài liệu tham chiếu

**Liên kết nhanh:**
- [Hướng dẫn bắt đầu](https://docs.bmad-method.org/vi-vn/tutorials/getting-started/)
- [Nâng cấp từ các phiên bản trước](https://docs.bmad-method.org/vi-vn/how-to/upgrade-to-v6/)
- [Tài liệu Test Architect](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)

## Cộng đồng

- [Discord](https://discord.gg/gk8jAdXWmj) - Nhận trợ giúp, chia sẻ ý tưởng, cộng tác
- [Đăng ký trên YouTube](https://www.youtube.com/@BMadCode) - video hướng dẫn, lớp chuyên sâu và podcast (ra mắt tháng 2 năm 2025)
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) - Báo lỗi và yêu cầu tính năng
- [Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions) - Trao đổi cộng đồng

## Hỗ trợ BMad

BMad miễn phí cho tất cả mọi người - và sẽ luôn như vậy. Nếu bạn muốn hỗ trợ quá trình phát triển:

- ⭐ Hãy nhấn sao cho dự án ở góc trên bên phải của trang này
- ☕ [Buy Me a Coffee](https://buymeacoffee.com/bmad) - Tiếp thêm năng lượng cho quá trình phát triển
- 🏢 Tài trợ doanh nghiệp - Nhắn riêng trên Discord
- 🎤 Diễn thuyết và truyền thông - Sẵn sàng cho hội nghị, podcast, phỏng vấn (BM trên Discord)

## Đóng góp

Chúng tôi luôn chào đón đóng góp. Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết hướng dẫn.

## Giấy phép

Giấy phép MIT - xem [LICENSE](LICENSE) để biết chi tiết.

---

**BMad** và **BMAD-METHOD** là các nhãn hiệu của BMad Code, LLC. Xem [TRADEMARK.md](TRADEMARK.md) để biết chi tiết.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

Xem [CONTRIBUTORS.md](CONTRIBUTORS.md) để biết thông tin về những người đóng góp.
```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

We release security patches for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < Latest | :x:               |

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

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bmad_method
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## What
<!-- 1-2 sentences describing WHAT changed -->

## Why
<!-- 1-2 sentences explaining WHY this change is needed -->
<!-- Fixes `#issue_number` (if applicable) -->

## How
<!-- 2-3 bullets listing HOW you implemented it -->
-

## Testing
<!-- 1-2 sentences on how you tested this -->

```

### File: docs\404.md
```md
---
title: Page Not Found
template: splash
---


The page you're looking for doesn't exist or has been moved.

[Return to Home](./index.md)

```

### File: docs\index.md
```md
---
title: Welcome to the BMad Method
description: AI-driven development framework with specialized agents, guided workflows, and intelligent planning
---

The BMad Method (**B**uild **M**ore **A**rchitect **D**reams) is an AI-driven development framework module within the BMad Method Ecosystem that helps you build software through the whole process from ideation and planning all the way through agentic implementation. It provides specialized AI agents, guided workflows, and intelligent planning that adapts to your project's complexity, whether you're fixing a bug or building an enterprise platform.

If you're comfortable working with AI coding assistants like Claude, Cursor, or GitHub Copilot, you're ready to get started.

:::note[🚀 V6 is Here and We're Just Getting Started!]
Skills Architecture, BMad Builder v1, Dev Loop Automation, and so much more in the works. **[Check out the Roadmap →](/roadmap/)**
:::

## New Here? Start with a Tutorial

The fastest way to understand BMad is to try it.

- **[Get Started with BMad](./tutorials/getting-started.md)** — Install and understand how BMad works
- **[Workflow Map](./reference/workflow-map.md)** — Visual overview of BMM phases, workflows, and context management

:::tip[Just Want to Dive In?]
Install BMad and use the `bmad-help` skill — it will guide you through everything based on your project and installed modules.
:::

## How to Use These Docs

These docs are organized into four sections based on what you're trying to do:

| Section           | Purpose                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| **Tutorials**     | Learning-oriented. Step-by-step guides that walk you through building something. Start here if you're new. |
| **How-To Guides** | Task-oriented. Practical guides for solving specific problems. "How do I customize an agent?" lives here.  |
| **Explanation**   | Understanding-oriented. Deep dives into concepts and architecture. Read when you want to know *why*.       |
| **Reference**     | Information-oriented. Technical specifications for agents, workflows, and configuration.                   |

## Extend and Customize

Want to expand BMad with your own agents, workflows, or modules? The **[BMad Builder](https://bmad-builder-docs.bmad-method.org/)** provides the framework and tools for creating custom extensions, whether you're adding new capabilities to BMad or building entirely new modules from scratch.

## What You'll Need

BMad works with any AI coding assistant that supports custom system prompts or project context. Popular options include:

- **[Claude Code](https://code.claude.com)** — Anthropic's CLI tool (recommended)
- **[Cursor](https://cursor.sh)** — AI-first code editor
- **[Codex CLI](https://github.com/openai/codex)** — OpenAI's terminal coding agent

You should be comfortable with basic software development concepts like version control, project structure, and agile workflows. No prior experience with BMad-style agent systems is required—that's what these docs are for.

## Join the Community

Get help, share what you're building, or contribute to BMad:

- **[Discord](https://discord.gg/gk8jAdXWmj)** — Chat with other BMad users, ask questions, share ideas
- **[GitHub](https://github.com/bmad-code-org/BMAD-METHOD)** — Source code, issues, and contributions
- **[YouTube](https://www.youtube.com/@BMadCode)** — Video tutorials and walkthroughs

## Next Step

Ready to dive in? **[Get Started with BMad](./tutorials/getting-started.md)** and build your first project.

```

### File: docs\_STYLE_GUIDE.md
```md
---
title: "Documentation Style Guide"
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
| 1     | Analysis | Brainstorm, research *(optional)*            |
| 2     | Planning | Requirements — PRD or spec *(required)* |
```

**Skills:**

```md
| Skill        | Agent   | Purpose                              |
| ------------ | ------- | ------------------------------------ |
| `bmad-brainstorming` | Analyst | Brainstorm a new project             |
| `bmad-create-prd`        | PM      | Create Product Requirements Document |
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
12. Quick Reference (skills table)
13. Common Questions (FAQ format)
14. Getting Help (community links)
15. Key Takeaways (tip admonition)
```

### Tutorial Checklist

- [ ] Hook describes outcome in 1-2 sentences
- [ ] "What You'll Learn" section present
- [ ] Prerequisites in admonition
- [ ] Quick Path TL;DR admonition at top
- [ ] Tables for phases, skills, agents
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
| **Feature**       | `quick-dev.md`                |
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
   - **Skills:** or **Key Info:** as flat list
3. Universal/Shared (## section) (optional)
```

### Item Deep-Dive Reference

```text
1. Title + Hook (one sentence purpose)
2. Quick Facts (optional note admonition)
   - Module, Skill, Input, Output as list
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
   - Standardized fields: Skill, Agent, Input, Output, Description
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

Yes. The `bmad-correct-course` workflow handles scope changes mid-implementation.

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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
