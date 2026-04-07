---
id: swift-patterns-skill
type: knowledge
owner: OA_Triage
---
# swift-patterns-skill
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Swift Patterns Skill

[![Validate Skill](https://github.com/efremidze/swift-patterns-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/efremidze/swift-patterns-skill/actions/workflows/validate-skill.yml)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io/home)
![Release](https://img.shields.io/github/v/release/efremidze/swift-patterns-skill)

A comprehensive Swift/SwiftUI knowledge base for AI coding tools, following the [Agent Skills standard](https://agentskills.io/home).

Provides expert guidance on state management, navigation, view composition, performance optimization, and modern SwiftUI API usage to help AI assistants generate better SwiftUI code.

## What This Skill Provides

Comprehensive SwiftUI expertise across:

### Core Topics
- **State Management** – Property wrapper selection (`@State`, `@Binding`, `@Observable`), ownership rules, data flow patterns
- **Modern APIs** – iOS 17/18/26 replacements for deprecated APIs, complete migration guides
- **View Composition** – Extraction patterns, parent/child data flow, view identity and performance
- **Navigation** – `NavigationStack`, sheets, deep linking, type-safe routing patterns

### Advanced Areas
- **Lists & Collections** – Stable identity with `ForEach`, pagination, lazy containers
- **Performance Optimization** – View optimization strategies, avoiding recomputation, memory management
- **Testing & Dependency Injection** – Protocol-based patterns, test doubles, testable architecture
- **Code Quality** – Refactoring playbooks, code smell detection, anti-pattern identification

All guidance is based on Apple's official documentation and focuses on **facts over opinions** – no architectural mandates.

## Quick Start

Install with a single command:

```bash
npx skills add https://github.com/efremidze/swift-patterns-skill --skill swift-patterns
```

Then use it in your AI assistant:
> Review my SwiftUI view for state management issues

[View on skills.sh →](https://skills.sh/efremidze/swift-patterns-skill/swift-patterns)

## Installation

### Recommended: Using skills.sh CLI

The easiest way to install:

```bash
npx skills add https://github.com/efremidze/swift-patterns-skill --skill swift-patterns
```

This installs the skill and makes it available to your AI assistant.

### Alternative: Claude Code Plugin

For Claude Code users, add via the marketplace:

1. Add the marketplace:
   ```bash
   /plugin marketplace add efremidze/swift-patterns-skill
   ```

2. Install the skill:
   ```bash
   /plugin install swift-patterns@swift-patterns-skill
   ```

Or configure for your team in `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "swift-patterns@swift-patterns-skill": true
  },
  "extraKnownMarketplaces": {
    "swift-patterns-skill": {
      "source": {
        "source": "github",
        "repo": "efremidze/swift-patterns-skill"
      }
    }
  }
}
```

### Manual Installation

If you prefer manual setup:

1. Clone this repository
2. Install or symlink `swift-patterns/` to your tool's skills directory
3. Configure your AI tool to use `swift-patterns`

## Skill Structure

The skill follows a progressive disclosure model—core workflows in `SKILL.md`, detailed guidance in `references/`:

```
swift-patterns/
  SKILL.md                          # Entry point: workflow routing, quick refs, review checklist
  references/
    state.md                        # Property wrappers, ownership, @Observable patterns
    navigation.md                   # NavigationStack, sheets, deep linking
    view-composition.md             # View extraction, data flow patterns
    lists-collections.md            # ForEach identity, List vs LazyVStack
    scrolling.md                    # Pagination, scroll position management
    concurrency.md                  # .task modifier, async lifecycle
    performance.md                  # View optimization, lazy loading strategies
    testing-di.md                   # Dependency injection, test doubles
    patterns.md                     # Container views, ViewModifiers, PreferenceKeys
    modern-swiftui-apis.md          # iOS 17/18/26 API replacements and migration
    refactor-playbooks.md           # Step-by-step refactoring guides
    workflows-review.md             # Review methodology and standards
    workflows-refactor.md           # Refactoring methodology, invariants
    code-review-refactoring.md      # Code smells, anti-patterns, quality checks
```

## Related Projects

### Other Skills
- **[swift-architecture-skill](https://github.com/efremidze/swift-architecture-skill)** – Architectural patterns and project structure guidance (complements this skill's focus on SwiftUI patterns)

### Dynamic Runtime Tools
- **[swift-patterns-mcp](https://github.com/efremidze/swift-patterns-mcp)** – MCP server with intelligent search, retrieval, and persistent memory

**Key difference:**
- **swift-patterns-skill** (this repo) = Static guidance, portable, no runtime dependencies
- **swift-patterns-mcp** = Dynamic tooling with search, retrieval, and premium integrations

## Contributing

Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.io/home).

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on improving the skill content and reference files.

## License

MIT License. See [LICENSE](LICENSE) for details.

```

### File: AGENTS.md
```md
# Agent Guidelines for Swift Patterns

This document provides guidance for AI agents working with this skill to ensure consistency and avoid common pitfalls.

## Core Principles

### 1. Swift and SwiftUI Focus
**This is a Swift and SwiftUI skill.** Do not include:
- Server-side Swift patterns
- UIKit patterns (except when bridging is necessary)
- Deep Swift concurrency patterns (actors, Sendable, etc.) — use `.task` for SwiftUI async work when needed

### 2. No Code Formatting or Linting
**Do not include formatting/linting rules.** Avoid:
- Property ordering requirements (environment, state, body, etc.)
- Code organization mandates
- Whitespace or indentation rules
- Naming convention enforcement
- File structure requirements

**Exception**: Mention organization patterns as *optional suggestions* for readability, never as requirements.

### 3. No Architectural Opinions
**Stick to facts, not architectures.** Avoid:
- Enforcing MVVM, MVC, VIPER, or any specific architecture
- Mandating view model patterns
- Requiring specific folder structures
- Dictating dependency injection patterns
- Prescribing router/coordinator patterns

**Exception**: Suggest separating business logic for testability without enforcing how.

### 4. No Tool-Specific Instructions
**Agents cannot use external tools.** Do not include:
- Xcode Instruments profiling instructions
- Debugging tool usage
- IDE-specific features
- Command-line tool usage beyond basic git

**Exception**: Mention that users can profile with Instruments if performance issues arise, but don't provide detailed instructions.

## Content Guidelines

### Suggestions vs Requirements

**Use "suggest" or "consider" for optional optimizations:**
- ✅ "Consider downsampling images when using `UIImage(data:)`"
- ❌ "Always downsample images"

**Use "always" or "never" only for correctness issues:**
- ✅ "Never use `.indices` for dynamic ForEach content"
- ✅ "Always mark `@State` as `private`"

### Performance Optimizations

**Present performance optimizations as optional improvements:**
- Image downsampling: Suggest when `UIImage(data:)` is encountered
- POD view wrappers: Mention as advanced optimization technique
- Equatable conformance: Suggest for expensive views

**Do not automatically apply optimizations.** Let developers decide based on their performance needs.

### Modern API Usage

**Enforce modern API usage for correctness:**
- ✅ `foregroundStyle()` instead of `foregroundColor()`
- ✅ `NavigationStack` instead of `NavigationView`
- ✅ `@Observable` instead of `ObservableObject` for new code

These are about using current, non-deprecated APIs, not optimization.

### State Management

**Be clear about `@MainActor` requirements:**
- Mention that `@Observable` classes may need `@MainActor`
- Note that projects with default actor isolation don't need explicit `@MainActor`
- Don't mandate it as "always required"

## What to Include

### ✅ Include These Topics:
- Property wrapper selection (`@State`, `@Binding`, `@Observable`, etc.)
- Modern API replacements for deprecated APIs
- View composition and extraction patterns
- Performance patterns (stable identity, lazy loading, etc.)
- Common pitfalls and how to avoid them
- Sheet, navigation, and list patterns
- Liquid Glass API usage (iOS 26+)
- Accessibility best practices

### ❌ Exclude These Topics:
- Swift concurrency deep dives (actors, sendable, etc.)
- Code formatting and style rules
- Architectural patterns and mandates
- Tool usage instructions (Instruments, debuggers)
- File organization requirements
- Testing framework setup (XCTest configuration, CI pipelines)
- Build system configuration
- Project structure mandates

## Language and Tone

### Use Clear, Direct Language:
- "Use X instead of Y" (for deprecated APIs)
- "Consider X when Y" (for optimizations)
- "Avoid X because Y" (for anti-patterns)
- "X is preferred over Y" (for best practices)

### Avoid Prescriptive Language:
- ❌ "You must organize properties in this order"
- ❌ "Always use MVVM architecture"
- ❌ "Profile with Instruments following these steps"
- ❌ "Structure your project like this"

## Examples

### Good Example:
```markdown
## ForEach Identity

**Always provide stable identity for `ForEach`.** Never use `.indices` for dynamic content.

When you encounter `UIImage(data:)`, consider suggesting image downsampling as a performance optimization.
```

### Bad Example:
```markdown
## View Organization

**Always organize view properties in this order:**
1. Environment
2. State
3. Body
4. Helpers

**Use Instruments to profile:**
1. Open Instruments
2. Select Swift template
3. Record and analyze...
```

## Updating the Skill

When adding new content:
1. Ask: "Is this Swift-specific?"
2. Ask: "Is this a fact or an opinion?"
3. Ask: "Can agents actually use this?"
4. Ask: "Is this about correctness or style?"

If unsure, err on the side of excluding content. It's better to have a focused, factual skill than a comprehensive but opinionated one.

## Summary

**Focus**: Swift APIs, patterns, and correctness
**Avoid**: Formatting, architecture, tools, Swift language features
**Tone**: Factual, helpful, non-prescriptive
**Goal**: Make agents Swift experts without enforcing opinions

```

### File: CONTRIBUTING.md
```md
# Contributing to Swift Patterns

We'd love your help making this skill better! Whether you're fixing outdated patterns, adding modern Swift APIs, or clarifying confusing guidance—every improvement helps developers write better code.

## About Agent Skills

This repository follows the [Agent Skills format](https://agentskills.io/home). See the [documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills) for details on structure and format.

## Ways to Contribute

**Using skill-creator (recommended)**
- Propose changes in plain language
- Let the skill generate or refine content
- Review for Swift accuracy and consistency

**Direct editing**
- Edit `SKILL.md` or files in `references/` directly
- Keep content focused and actionable
- Maintain consistent structure across files

## What to Contribute

✅ Fix incorrect Swift or SwiftUI guidance  
✅ Add modern API patterns or flag deprecations  
✅ Improve clarity in decision trees and checklists  
✅ Expand reference files with practical patterns  
✅ Update documentation in README or this guide  

## Quality Guidelines

**Content focus**
- Swift and SwiftUI best practices only
- Avoid mandating specific architectures or project structures
- Use modern APIs and note deprecated alternatives
- Show tradeoffs, not just prescriptive rules

**Writing style**
- Clear and direct language
- Practical code examples that work
- Explain "when" and "why", not just "what"
- Keep anti-patterns section focused on common mistakes

## Pull Request Process

1. Fork the repository and create a branch
2. Make focused changes to one area
3. Ensure `SKILL.md` and references stay consistent
4. Open a PR with a clear description of changes

## References

- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills)
- [AgentSkills.io](https://agentskills.io/home)

## Questions?

Open an issue to discuss major changes before starting work.

## Code of Conduct

Be respectful and constructive. Focus on making Swift guidance better for everyone.

```

### File: .claude-plugin\marketplace.json
```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/marketplace/marketplace.schema.json",
  "name": "swift-patterns-skill",
  "version": "1.0.0",
  "owner": {
    "name": "Lasha Efremidze",
    "email": "efremidzel@hotmail.com"
  },
  "metadata": {
    "description": "Swift and SwiftUI best practices for modern iOS development. Use when writing, reviewing, or refactoring code."
  },
  "plugins": [
    {
      "name": "swift-patterns",
      "description": "Expert Swift and SwiftUI guidance for state management, navigation, testing, dependency injection, performance optimization, and code quality patterns.",
      "repository": "https://github.com/efremidze/swift-patterns-skill",
      "version": "1.0.0",
      "author": {
        "name": "Lasha Efremidze",
        "email": "efremidzel@hotmail.com"
      },
      "license": "MIT",
      "category": "development",
      "keywords": [
        "swift",
        "swiftui",
        "ios",
        "apple",
        "state-management",
        "navigation",
        "testing",
        "dependency-injection",
        "performance"
      ],
      "tags": [
        "swift",
        "swiftui",
        "ios",
        "apple",
        "state-management",
        "navigation",
        "testing",
        "dependency-injection",
        "performance"
      ],
      "source": "./",
      "skills": [
        "./swift-patterns"
      ],
      "strict": false
    }
  ]
}

```

### File: .claude-plugin\plugin.json
```json
{
  "name": "swift-patterns",
  "version": "1.0.0",
  "description": "Expert Swift and SwiftUI guidance for state management, navigation, testing, dependency injection, performance optimization, and code quality patterns.",
  "author": {
    "name": "Lasha Efremidze",
    "email": "efremidzel@hotmail.com"
  },
  "repository": "https://github.com/efremidze/swift-patterns-skill",
  "license": "MIT",
  "keywords": [
    "swift",
    "swiftui",
    "ios",
    "apple",
    "state-management",
    "performance",
    "view-composition",
    "navigation",
    "lists",
    "sheets",
    "testing"
  ],
  "skills": [
    "./swift-patterns"
  ]
}

```

### File: .planning\config.json
```json
{
  "mode": "interactive",
  "depth": "quick",
  "parallelization": true,
  "commit_docs": true,
  "model_profile": "balanced",
  "workflow": {
    "research": true,
    "plan_check": true,
    "verifier": true
  }
}

```

### File: .planning\MILESTONES.md
```md
# Project Milestones: Swift Expert Skill Refactor

## v1.0 MVP (Shipped: 2026-01-26)

**Delivered:** Swift/SwiftUI agent skill with constraint-linked workflows, decision routing, and guidance playbooks.

**Phases completed:** 1-5 (9 plans total)

**Key accomplishments:**
- Established SKILL constraints + citation allowlist and standardized refactor/review templates.
- Added workflow routing, review/refactor checklists, and invariants for safety.
- Published SwiftUI core guidance plus scrolling/concurrency references.
- Delivered performance/testing guidance and refactor playbooks.
- Aligned code-review reference with constraints and SwiftUI-only examples.

**Stats:**
- 65 files changed
- 4,328 lines added, 3,305 removed
- 5 phases, 9 plans, 18 tasks
- 1 day from start to ship (2026-01-25 → 2026-01-26)

**Git range:** `adac2a9` → `03fa81f`

**What's next:** Define v1.1 requirements and roadmap

---

```

### File: .planning\PROJECT.md
```md
# Swift Expert Skill Refactor

## What This Is

A refactor of this repository into a reusable Agent Skill that AI coding agents can load on demand for Swift/SwiftUI review and refactoring. It will provide clear workflows, decision logic, and high-signal best-practice guidance as actionable rules and checklists.

## Core Value

AI agents can quickly apply consistent, modern Swift/SwiftUI guidance to refactor and review code without ambiguity.

## Requirements

### Validated

- ✓ Existing Agent Skill content with a workflow entry point — existing (`swift-patterns/SKILL.md`)
- ✓ Topic-specific reference docs covering core Swift/SwiftUI areas — existing (`swift-patterns/references/*.md`)
- ✓ Repository-level usage documentation — existing (`README.md`)
- ✓ Restructure skill content for immediate agent usability (clear workflows and decision logic) — v1.0
- ✓ Provide actionable rules and checklists for Swift/SwiftUI refactoring and review — v1.0
- ✓ Ensure guidance is modern and agent-friendly (focused on SwiftUI, concurrency, navigation, testing/DI, performance/refactoring) — v1.0

### Active

- [ ] None yet — define during next milestone planning

### Out of Scope

- Architecture mandates — avoid prescribing MVVM/MVC/VIPER or similar
- Formatting/style rules — no linting or ordering requirements
- Tool-specific steps — no Xcode/CLI instructions beyond basics
- Swift language deep dives — avoid non-SwiftUI Swift features

## Context

This repository already contains an Agent Skill in `swift-patterns/` with topic references in `swift-patterns/references/`, plus lightweight Node.js hooks in `.opencode/hooks/` and `.claude/hooks/`. The refactor will focus on making the skill content immediately usable by AI agents via structured workflows, decision logic, and concise guidance.

## Current State

v1.0 shipped with a complete Swift/SwiftUI agent skill: constraint-linked workflows, decision routing, core SwiftUI guidance, quality/playbooks, and constraint-aligned reference hub content.

## Constraints

- **Format**: Must follow Agent Skills format with metadata and procedural instructions — required for agent loading
- **Audience**: Optimize first for AI coding agents — fast lookup and step-by-step guidance
- **Scope**: Emphasize SwiftUI state, concurrency, navigation, testing/DI, and performance/refactoring
- **Exclusions**: No architecture mandates, formatting rules, or tool-specific instructions

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Optimize for immediate agent usability | Primary goal is agent on-demand usage | ✓ Shipped v1.0 |
| Emphasize SwiftUI state, concurrency, navigation, testing/DI, performance/refactoring | Core areas for refactor/review workflows | ✓ Shipped v1.0 |
| Exclude architecture mandates, formatting rules, tool-specific steps | Aligns with skill guidelines and avoids prescriptions | ✓ Shipped v1.0 |

## Next Milestone Goals

- Define the next set of requirements and roadmap after v1.0 archive

---
*Last updated: 2026-01-26 after v1.0 milestone*

```

### File: .planning\ROADMAP.md
```md
# Roadmap: Swift Expert Skill Refactor

## Overview

This roadmap delivers a decision-gated Swift/SwiftUI skill that agents can use immediately for review and refactor work. It starts with compliant packaging and response templates, then adds workflow decisioning and safety checks before expanding into SwiftUI guidance, modernization, and quality playbooks.

## Milestones

- ✅ **v1.0 MVP** — Phases 1-5 (shipped 2026-01-26). Archive: `.planning/milestones/v1.0-ROADMAP.md`

## Phases

<details>
<summary>✅ v1.0 MVP (Phases 1-5) — SHIPPED 2026-01-26</summary>

- [x] Phase 1: Compliance + Output Foundations (2/2 plans)
- [x] Phase 2: Decisioned Workflows + Safety (2/2 plans)
- [x] Phase 3: SwiftUI Guidance Core (2/2 plans)
- [x] Phase 4: Quality + Playbooks (2/2 plans)
- [x] Phase 5: Constraints Alignment for Code Review Reference (1/1 plan)

</details>

### 🚧 Next Milestone (Not started)

Run `/gsd-new-milestone` to define requirements and create the next roadmap.

## Progress

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Compliance + Output Foundations | v1.0 | 2/2 | Complete | 2026-01-26 |
| 2. Decisioned Workflows + Safety | v1.0 | 2/2 | Complete | 2026-01-26 |
| 3. SwiftUI Guidance Core | v1.0 | 2/2 | Complete | 2026-01-26 |
| 4. Quality + Playbooks | v1.0 | 2/2 | Complete | 2026-01-26 |
| 5. Constraints Alignment for Code Review Reference | v1.0 | 1/1 | Complete | 2026-01-26 |

```

### File: .planning\STATE.md
```md
# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-01-25)

**Core value:** AI agents can quickly apply consistent, modern Swift/SwiftUI guidance to refactor and review code without ambiguity.
**Current focus:** Planning next milestone

## Current Position

Phase: Not started
Plan: Not started
Status: Ready to plan
Last activity: 2026-01-26 — v1.0 milestone complete

Progress: [░░░░░░░░░░] 0%

## Performance Metrics

**Velocity:**
- Total plans completed: 9
- Average duration: 1 min
- Total execution time: 0.1 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 1. Compliance + Output Foundations | 2 | 2 | 1 min |
| 2. Decisioned Workflows + Safety | 2 | 2 | 1 min |
| 3. SwiftUI Guidance Core | 2 | 2 | 1 min |
| 4. Quality + Playbooks | 2 | 2 | 0 min |
| 5. Constraints Alignment for Code Review Reference | 1 | 1 | 2 min |

**Recent Trend:**
- Last 5 plans: 05-01 (2 min), 04-02 (0 min), 04-01 (0 min), 03-02 (2 min), 03-01 (2 min)
- Trend: Stable

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- None yet.

### Pending Todos

None yet.

### Blockers/Concerns

None yet.

## Session Continuity

Last session: 2026-01-26 20:27
Stopped at: Completed 05-01-PLAN.md
Resume file: None

```

### File: .planning\codebase\ARCHITECTURE.md
```md
# Architecture

**Analysis Date:** 2026-01-25

## Pattern Overview

**Overall:** Documentation repository with lightweight Node.js hook scripts.

**Key Characteristics:**
- Skill content lives in Markdown under `swift-patterns/`
- Tooling hooks live in `.opencode/hooks/` and `.claude/hooks/`
- No application runtime or build pipeline present

## Layers

**Skill Content:**
- Purpose: Primary deliverable (Swift skill guidance)
- Location: `swift-patterns/`
- Contains: `SKILL.md`, reference documents in `swift-patterns/references/*.md`
- Depends on: None
- Used by: Documentation consumers and agent skill tooling

**Project Docs:**
- Purpose: Repository-level documentation
- Location: `README.md`, `CONTRIBUTING.md`, `LICENSE`
- Contains: Usage, contribution, license
- Depends on: None
- Used by: End users and contributors

**Automation Hooks:**
- Purpose: Statusline and update checks for GSD workflows
- Location: `.opencode/hooks/`, `.claude/hooks/`
- Contains: Node.js scripts (see `.opencode/hooks/gsd-check-update.js`, `.opencode/hooks/gsd-statusline.js`)
- Depends on: Node.js runtime, local filesystem
- Used by: Claude/Opencode hook systems

## Data Flow

**GSD Update Check:**
1. `.opencode/hooks/gsd-check-update.js` resolves local version file from `.claude/get-shit-done/VERSION`.
2. Script shells out to `npm view get-shit-done-cc version`.
3. Result is cached to `~/.claude/cache/gsd-update-check.json`.

**Statusline Render:**
1. `.opencode/hooks/gsd-statusline.js` reads JSON from stdin.
2. Script reads todos from `~/.claude/todos` for current session.
3. Script reads update cache from `~/.claude/cache/gsd-update-check.json`.
4. Statusline is written to stdout.

**State Management:**
- State is file-based (JSON cache and session todos in the user home directory).

## Key Abstractions

**Skill Document:**
- Purpose: Defines the workflow and references for the Swift skill
- Examples: `swift-patterns/SKILL.md`
- Pattern: Markdown-based declarative documentation

**Reference Document:**
- Purpose: Deep-dive guidance on a specific topic
- Examples: `swift-patterns/references/concurrency.md`, `swift-patterns/references/performance.md`
- Pattern: Markdown guides with sectioned content

## Entry Points

**Skill Overview:**
- Location: `swift-patterns/SKILL.md`
- Triggers: Loaded by agent tooling that supports Agent Skills format
- Responsibilities: Provide decision tree and references

**Repository Readme:**
- Location: `README.md`
- Triggers: Viewed by users on GitHub or after clone
- Responsibilities: Installation and usage instructions

**Hook Scripts:**
- Location: `.opencode/hooks/gsd-check-update.js`, `.opencode/hooks/gsd-statusline.js`
- Triggers: Hook system invokes scripts
- Responsibilities: Update checks and statusline rendering

## Error Handling

**Strategy:** Best-effort, silent failure

**Patterns:**
- `try/catch` with empty handlers in `.opencode/hooks/gsd-check-update.js`
- Silent failure on JSON parse in `.opencode/hooks/gsd-statusline.js`

## Cross-Cutting Concerns

**Logging:** None (scripts are intentionally quiet)
**Validation:** Minimal (JSON parse guarded)
**Authentication:** None

---

*Architecture analysis: 2026-01-25*

```

### File: .planning\codebase\CONCERNS.md
```md
# Codebase Concerns

**Analysis Date:** 2026-01-25

## Tech Debt

**Duplicate Hook Scripts:**
- Issue: Same hook logic exists in two locations and can drift
- Files: `.opencode/hooks/gsd-check-update.js`, `.claude/hooks/gsd-check-update.js`, `.opencode/hooks/gsd-statusline.js`, `.claude/hooks/gsd-statusline.js`
- Impact: Behavior differences across environments if one copy changes
- Fix approach: Consolidate or document the source of truth

## Known Bugs

**Not detected**

## Security Considerations

**External Command Execution:**
- Risk: `npm view` is executed via shell
- Files: `.opencode/hooks/gsd-check-update.js`
- Current mitigation: Command is fixed string, no user input
- Recommendations: Keep command string static and avoid user-supplied input

## Performance Bottlenecks

**Not detected**

## Fragile Areas

**Local Cache Dependence:**
- Files: `.opencode/hooks/gsd-statusline.js`
- Why fragile: Assumes cache and todo directories exist in `~/.claude/`
- Safe modification: Guard file reads and keep try/catch behavior
- Test coverage: No automated tests detected

## Scaling Limits

**Not detected**

## Dependencies at Risk

**Not detected**

## Missing Critical Features

**Not detected**

## Test Coverage Gaps

**No automated tests:**
- What's not tested: Hook script behavior and parsing
- Files: `.opencode/hooks/gsd-check-update.js`, `.opencode/hooks/gsd-statusline.js`
- Risk: Regressions in statusline output or update checks
- Priority: Medium

---

*Concerns audit: 2026-01-25*

```

### File: .planning\codebase\CONVENTIONS.md
```md
# Coding Conventions

**Analysis Date:** 2026-01-25

## Naming Patterns

**Files:**
- Markdown references: lowercase kebab-case (e.g. `concurrency.md` in `swift-patterns/references/`)
- Root docs: uppercase (e.g. `README.md`, `CONTRIBUTING.md`)
- Hook scripts: kebab-case with `.js` (e.g. `.opencode/hooks/gsd-statusline.js`)

**Functions:**
- JavaScript functions use camelCase (e.g. `process.stdin.on`, `fs.readFileSync` usage in `.opencode/hooks/gsd-statusline.js`)

**Variables:**
- JavaScript variables use lowerCamelCase and `const` where possible (see `.opencode/hooks/gsd-check-update.js`)

**Types:**
- Not applicable (no TypeScript/types)

## Code Style

**Formatting:**
- No formatter config detected

**Linting:**
- No lint config detected

## Import Organization

**Order:**
1. Built-in Node.js modules via `require` (e.g. `fs`, `path`, `os` in `.opencode/hooks/gsd-statusline.js`)

**Path Aliases:**
- Not detected

## Error Handling

**Patterns:**
- Silent failure via empty `catch` blocks (e.g. `.opencode/hooks/gsd-check-update.js`)
- Try/catch around JSON parsing in `.opencode/hooks/gsd-statusline.js`

## Logging

**Framework:** None

**Patterns:**
- Scripts avoid logging; output is reserved for statusline rendering

## Comments

**When to Comment:**
- Header comments describe script purpose and behavior (e.g. `.opencode/hooks/gsd-statusline.js`)

**JSDoc/TSDoc:**
- Not detected

## Function Design

**Size:**
- Small utility scripts with a single entry point (`process.stdin.on('end', ...)`)

**Parameters:**
- Standard Node.js callbacks and configuration objects

**Return Values:**
- Output via stdout or filesystem writes

## Module Design

**Exports:**
- Not detected (scripts are executables, not modules)

**Barrel Files:**
- Not detected

---

*Convention analysis: 2026-01-25*

```

### File: .planning\codebase\INTEGRATIONS.md
```md
# External Integrations

**Analysis Date:** 2026-01-25

## APIs & External Services

**Package Registry:**
- npm registry - version check used by `.opencode/hooks/gsd-check-update.js`
  - SDK/Client: Node.js `child_process.execSync` shelling out to `npm view`
  - Auth: None

## Data Storage

**Databases:**
- Not detected

**File Storage:**
- Local filesystem only (cache in `~/.claude/cache/gsd-update-check.json` written by `.opencode/hooks/gsd-check-update.js`)

**Caching:**
- Local JSON cache at `~/.claude/cache/gsd-update-check.json`

## Authentication & Identity

**Auth Provider:**
- Not detected

## Monitoring & Observability

**Error Tracking:**
- Not detected

**Logs:**
- Hook scripts are silent by default (no logging in `.opencode/hooks/gsd-check-update.js` or `.opencode/hooks/gsd-statusline.js`)

## CI/CD & Deployment

**Hosting:**
- Not detected

**CI Pipeline:**
- Not detected

## Environment Configuration

**Required env vars:**
- Not detected

**Secrets location:**
- Not detected

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None

---

*Integration audit: 2026-01-25*

```

### File: .planning\codebase\STACK.md
```md
# Technology Stack

**Analysis Date:** 2026-01-25

## Languages

**Primary:**
- Markdown - documentation in `README.md`, `swift-patterns/SKILL.md`, `swift-patterns/references/*.md`

**Secondary:**
- JavaScript (Node.js) - hook scripts in `.opencode/hooks/gsd-check-update.js`, `.opencode/hooks/gsd-statusline.js`, `.claude/hooks/gsd-check-update.js`, `.claude/hooks/gsd-statusline.js`

## Runtime

**Environment:**
- Node.js (version not specified) - required to run hook scripts

**Package Manager:**
- npm (version not specified)
- Lockfile: `package-lock.json` present

## Frameworks

**Core:**
- Not detected

**Testing:**
- Not detected

**Build/Dev:**
- Not detected

## Key Dependencies

**Critical:**
- Not detected (no dependencies listed in `package.json`)

**Infrastructure:**
- Not detected

## Configuration

**Environment:**
- No project-level env configuration detected

**Build:**
- No build config detected

## Platform Requirements

**Development:**
- Node.js available on PATH for hook scripts
- Git (repository metadata in `.git/`)

**Production:**
- Not applicable (documentation repository)

---

*Stack analysis: 2026-01-25*

```

### File: .planning\codebase\STRUCTURE.md
```md
# Codebase Structure

**Analysis Date:** 2026-01-25

## Directory Layout

```
[project-root]/
├── swift-patterns/      # Skill definition and references
│   ├── SKILL.md             # Main workflow/decision tree
│   └── references/          # Topic-specific guidance
├── .opencode/               # OpenCode automation hooks
│   └── hooks/               # Node.js hook scripts
├── .claude/                 # Claude-specific workflows/hooks
│   └── hooks/               # Node.js hook scripts
├── .planning/               # Planning artifacts (created by GSD)
├── README.md                # Repository documentation
├── package.json             # npm metadata
├── package-lock.json        # npm lockfile
└── AGENTS.md                # Agent behavior guidelines
```

## Directory Purposes

**swift-patterns/**
- Purpose: Core skill content
- Contains: `SKILL.md`, `references/*.md`
- Key files: `swift-patterns/SKILL.md`, `swift-patterns/references/concurrency.md`

**.opencode/**
- Purpose: OpenCode automation assets
- Contains: hook scripts in `.opencode/hooks/`
- Key files: `.opencode/hooks/gsd-check-update.js`, `.opencode/hooks/gsd-statusline.js`

**.claude/**
- Purpose: Claude workflows, hooks, and templates
- Contains: `.claude/hooks/` and GSD workflow definitions
- Key files: `.claude/agents/gsd-codebase-mapper.md`, `.claude/get-shit-done/workflows/map-codebase.md`

**.planning/**
- Purpose: GSD planning artifacts (generated)
- Contains: `.planning/codebase/*.md` and future planning docs

## Key File Locations

**Entry Points:**
- `swift-patterns/SKILL.md`: Skill overview and workflow
- `README.md`: Repository usage and install instructions

**Configuration:**
- `package.json`: npm metadata
- `package-lock.json`: npm lockfile
- `AGENTS.md`: Agent constraints

**Core Logic:**
- `.opencode/hooks/gsd-check-update.js`: Update check hook
- `.opencode/hooks/gsd-statusline.js`: Statusline hook

**Testing:**
- Not detected

## Naming Conventions

**Files:**
- Markdown references use lowercase with hyphens, e.g. `concurrency.md`
- Root docs use uppercase names, e.g. `README.md`, `CONTRIBUTING.md`

**Directories:**
- Feature grouping by purpose, e.g. `swift-patterns/references/`

## Where to Add New Code

**New Skill Content:**
- Primary docs: `swift-patterns/`
- References: `swift-patterns/references/`

**New Hooks:**
- OpenCode hooks: `.opencode/hooks/`
- Claude hooks: `.claude/hooks/`

**Utilities:**
- Not detected (no shared code utilities directory)

## Special Directories

**.planning/**
- Purpose: Generated planning artifacts
- Generated: Yes
- Committed: Depends on workflow config

---

*Structure analysis: 2026-01-25*

```

### File: .planning\codebase\TESTING.md
```md
# Testing Patterns

**Analysis Date:** 2026-01-25

## Test Framework

**Runner:**
- Not detected

**Assertion Library:**
- Not detected

**Run Commands:**
```bash
# Not detected
```

## Test File Organization

**Location:**
- Not detected

**Naming:**
- Not detected

**Structure:**
```
# Not detected
```

## Test Structure

**Suite Organization:**
```text
Not detected
```

**Patterns:**
- Not detected

## Mocking

**Framework:** Not detected

**Patterns:**
```text
Not detected
```

**What to Mock:**
- Not detected

**What NOT to Mock:**
- Not detected

## Fixtures and Factories

**Test Data:**
```text
Not detected
```

**Location:**
- Not detected

## Coverage

**Requirements:** None enforced

**View Coverage:**
```bash
# Not detected
```

## Test Types

**Unit Tests:**
- Not detected

**Integration Tests:**
- Not detected

**E2E Tests:**
- Not detected

## Common Patterns

**Async Testing:**
```text
Not detected
```

**Error Testing:**
```text
Not detected
```

---

*Testing analysis: 2026-01-25*

```

### File: .planning\milestones\v1.0-MILESTONE-AUDIT.md
```md
---
milestone: v1.0
audited: 2026-01-26T20:30:00Z
status: passed
scores:
  requirements: 22/22
  phases: 5/5
  integration: 4/4
  flows: 4/4
gaps:
  requirements: []
  integration: []
  flows: []
tech_debt: []
---

# Milestone Audit: v1.0

## Summary

- Requirements coverage is complete (22/22) and all phases are verified.
- Cross-phase wiring and Quick Decision Guide flows are complete.

## Requirements Coverage

| Requirement Group | Status | Notes |
| --- | --- | --- |
| Core workflows (CORE-01..07) | ✓ Complete | Verified in Phase 1-2 reports. |
| SwiftUI guidance (SWUI-01..06) | ✓ Complete | Verified in Phase 3 report. |
| Concurrency (CONC-01..02) | ✓ Complete | Verified in Phase 3 report. |
| Modernization (MOD-01..02) | ✓ Complete | Verified in Phase 3 report. |
| Quality & performance (PERF-01..02) | ✓ Complete | Verified in Phase 4 report. |
| Testing/DI (TEST-01) | ✓ Complete | Verified in Phase 4 report. |
| Playbooks (PLAY-01) | ✓ Complete | Verified in Phase 4 report. |

## Phase Verification Status

| Phase | Status | Report |
| --- | --- | --- |
| 01-compliance-output-foundations | passed | .planning/phases/01-compliance-output-foundations/01-compliance-output-foundations-VERIFICATION.md |
| 02-decisioned-workflows-+-safety | passed | .planning/phases/02-decisioned-workflows-+-safety/02-decisioned-workflows-+-safety-VERIFICATION.md |
| 03-swiftui-guidance-core | passed | .planning/phases/03-swiftui-guidance-core/03-swiftui-guidance-core-VERIFICATION.md |
| 04-quality-+-playbooks | passed | .planning/phases/04-quality-+-playbooks/04-quality-+-playbooks-VERIFICATION.md |
| 05-constraints-alignment-code-review-reference | passed | .planning/phases/05-constraints-alignment-code-review-reference/05-constraints-alignment-code-review-reference-VERIFICATION.md |

## Integration Check

### Missing Connections

None found.

### Broken Flows

None found.

## Tech Debt

None recorded.

## Recommendation

No additional gap closure required. Milestone is ready to complete.

```

### File: .planning\milestones\v1.0-REQUIREMENTS.md
```md
# Requirements Archive: v1.0 MVP

**Archived:** 2026-01-26
**Status:** ✅ SHIPPED

This is the archived requirements specification for v1.0.
For current requirements, see `.planning/REQUIREMENTS.md` (created for next milestone).

---

# Requirements: Swift Expert Skill Refactor

**Defined:** 2026-01-25
**Core Value:** AI agents can quickly apply consistent, modern Swift/SwiftUI guidance to refactor and review code without ambiguity.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Core Workflows

- [x] **CORE-01**: Agent can route requests into review vs refactor workflow based on user intent cues
- [x] **CORE-02**: Refactor checklist defines behavior-preserving steps for SwiftUI changes
- [x] **CORE-03**: Review checklist produces consistent SwiftUI review findings
- [x] **CORE-04**: Risk assessment cues indicate when to split refactors or add tests first
- [x] **CORE-05**: Output templates standardize refactor/review responses for agent usability
- [x] **CORE-06**: Single constraints section is referenced by all workflows to prevent scope drift
- [x] **CORE-07**: Identity and data flow invariants list what refactors must preserve (stable IDs, state ownership, navigation source of truth, cancellable async work)

### SwiftUI Guidance

- [x] **SWUI-01**: State ownership guidance covers `@State`, `@Binding`, `@Observable`, and `@Environment`
- [x] **SWUI-02**: Navigation guidance covers `NavigationStack`, destinations, and presentation patterns
- [x] **SWUI-03**: List/collection guidance covers stable identity, `ForEach` pitfalls, and lazy containers
- [x] **SWUI-04**: View composition guidance covers extraction and data flow between parent/child views
- [x] **SWUI-05**: Layout guidance covers stack usage, alignment, spacing, and adaptive layout patterns
- [x] **SWUI-06**: Scroll guidance covers `ScrollView` patterns and safe pagination triggers

### Swift Concurrency (Lightweight)

- [x] **CONC-01**: Async work guidance for SwiftUI uses `.task` and cancellation-aware patterns
- [x] **CONC-02**: UI update guidance clarifies `@MainActor` usage without deep concurrency dives

### Quality & Performance

- [x] **PERF-01**: Performance baseline guidance covers common SwiftUI pitfalls and safe optimizations
- [x] **PERF-02**: Performance best-practice patterns cover view identity stability and expensive work avoidance
- [x] **TEST-01**: Testing/DI guidance shows lightweight seams for refactor safety without tool mandates

### Modernization & Decisioning

- [x] **MOD-01**: Modern API replacement catalog maps deprecated SwiftUI APIs to current equivalents
- [x] **MOD-02**: Decision trees guide selection of state wrappers based on ownership and sharing

### Advanced Playbooks

- [x] **PLAY-01**: Goal-based refactor playbooks guide common migrations (view extraction, navigation, state hoisting)

### Compliance & Packaging

- [x] **COMP-01**: Skill conforms to Agent Skills spec (metadata + procedural instructions in `SKILL.md`)
- [x] **COMP-02**: AI-safe citations rule restricts references to links listed in `/references/`

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Accessibility

- **A11Y-01**: Accessibility basics cover labels, dynamic type, and hit targets

### Examples & Tuning

- **CASE-01**: Before/after case studies show refactor decisions and tradeoffs
- **PERF-03**: Performance tuning recipes provide advanced optimization guidance

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Architecture mandates (MVVM/MVC/VIPER) | Conflicts with non-prescriptive guidance goal |
| Formatting or linting rules | Style policing, not refactor guidance |
| Tool-specific steps (Xcode/Instruments/CLI workflows) | Not usable in all agent environments |
| Generic Swift language tutorials | Dilutes SwiftUI refactor focus |
| UIKit or server-side Swift guidance | Outside SwiftUI-focused scope |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| CORE-01 | Phase 2 | Complete |
| CORE-02 | Phase 2 | Complete |
| CORE-03 | Phase 2 | Complete |
| CORE-04 | Phase 2 | Complete |
| CORE-05 | Phase 1 | Complete |
| CORE-06 | Phase 1 | Complete |
| CORE-07 | Phase 2 | Complete |
| SWUI-01 | Phase 3 | Complete |
| SWUI-02 | Phase 3 | Complete |
| SWUI-03 | Phase 3 | Complete |
| SWUI-04 | Phase 3 | Complete |
| SWUI-05 | Phase 3 | Complete |
| SWUI-06 | Phase 3 | Complete |
| CONC-01 | Phase 3 | Complete |
| CONC-02 | Phase 3 | Complete |
| PERF-01 | Phase 4 | Complete |
| PERF-02 | Phase 4 | Complete |
| TEST-01 | Phase 4 | Complete |
| MOD-01 | Phase 3 | Complete |
| MOD-02 | Phase 3 | Complete |
| PLAY-01 | Phase 4 | Complete |
| COMP-01 | Phase 1 | Complete |
| COMP-02 | Phase 1 | Complete |

---

## Milestone Summary

**Shipped:** 22 of 22 v1 requirements
**Adjusted:** None
**Dropped:** None

---

*Archived: 2026-01-26 as part of v1.0 milestone completion*

```

### File: .planning\milestones\v1.0-ROADMAP.md
```md
# Milestone v1.0: MVP

**Status:** ✅ SHIPPED 2026-01-26
**Phases:** 1-5
**Total Plans:** 9

## Overview

This roadmap delivers a decision-gated Swift/SwiftUI skill that agents can use immediately for review and refactor work. It starts with compliant packaging and response templates, then adds workflow decisioning and safety checks before expanding into SwiftUI guidance, modernization, and quality playbooks.

## Phases

### Phase 1: Compliance + Output Foundations

**Goal**: The skill loads correctly and provides constraints plus standardized refactor/review response templates.
**Depends on**: Nothing (first phase)
**Plans**: 2 plans

Plans:

- [x] 01-01: Define skill metadata, constraints, and citation rules
- [x] 01-02: Establish standardized response templates

**Details:**
1. User can load the skill and see required metadata and procedural instructions in `SKILL.md`.
2. User can see refactor and review response templates that standardize agent output format.
3. User can verify citations are restricted to sources listed in `/references/`.
4. User can find a single constraints section referenced by all workflows.

### Phase 2: Decisioned Workflows + Safety

**Goal**: Users can route requests into refactor vs review workflows with consistent, risk-aware checklists and a shared constraints section.
**Depends on**: Phase 1
**Plans**: 2 plans

Plans:

- [x] 02-01: Build workflow routing and shared constraints section
- [x] 02-02: Add refactor/review checklists with risk cues and invariants

**Details:**
1. User can determine whether a request should follow review or refactor workflow using intent cues.
2. User can apply a behavior-preserving refactor checklist for SwiftUI changes.
3. User can apply a SwiftUI review checklist and receive consistent findings.
4. User can identify when a refactor should be split or when tests should be added first.
5. User can apply an invariants list that preserves identity and data flow during refactors.

### Phase 3: SwiftUI Guidance Core

**Goal**: Users can apply core SwiftUI guidance for state, navigation, lists, composition, layout, scrolling, and lightweight concurrency.
**Depends on**: Phase 2
**Plans**: 2 plans

Plans:

- [x] 03-01: Draft SwiftUI state, navigation, lists, composition, layout guidance, and API replacements
- [x] 03-02: Add scroll and lightweight concurrency guidance with decision trees

**Details:**
1. User can select the appropriate state wrapper using ownership guidance and decision trees.
2. User can implement navigation and presentation patterns with `NavigationStack` and destinations.
3. User can build lists/collections with stable identity and appropriate lazy containers.
4. User can structure view composition and data flow with layout, alignment, spacing, and adaptive patterns.
5. User can apply scrolling patterns with safe pagination triggers and async work using `.task` and `@MainActor` guidance.
6. User can replace deprecated SwiftUI APIs using a modern replacement catalog.

### Phase 4: Quality + Playbooks

**Goal**: Users can apply quality, performance, and refactor playbooks safely.
**Depends on**: Phase 3
**Plans**: 2 plans

Plans:

- [x] 04-01: Publish performance baseline and testing/DI seams guidance
- [x] 04-02: Add goal-based refactor playbooks and workflow wiring

**Details:**
1. User can avoid common performance pitfalls with baseline SwiftUI guidance.
2. User can apply best-practice patterns for identity stability and expensive work avoidance.
3. User can introduce lightweight testing/DI seams to reduce refactor risk.
4. User can follow goal-based refactor playbooks for common migrations.

### Phase 5: Constraints Alignment for Code Review Reference

**Goal**: Code review/refactor reference content complies with constraints and keeps Quick Decision Guide flows safe.
**Depends on**: Phase 4
**Plans**: 1 plan

Plans:

- [x] 05-01: Align code review reference with constraints

**Details:**
1. Quick Decision Guide links to a code review/refactor reference that enforces constraints.
2. Tool-specific steps, formatting rules, and UIKit examples are removed from that reference.
3. The reference links back to the Constraints section for scope enforcement.

---

## Milestone Summary

**Decimal Phases:** None

**Key Decisions:**
- Optimize for immediate agent usability — ✓ Shipped v1.0
- Emphasize SwiftUI state, concurrency, navigation, testing/DI, performance/refactoring — ✓ Shipped v1.0
- Exclude architecture mandates, formatting rules, tool-specific steps — ✓ Shipped v1.0

**Issues Resolved:**
- Enforced single Constraints section and citation allowlist.
- Added workflow routing with risk cues and invariants.
- Closed Quick Decision Guide constraints gap for code-review reference.

**Issues Deferred:**
- None recorded.

**Technical Debt Incurred:**
- None recorded.

---

_For current project status, see .planning/ROADMAP.md_

```

### File: .planning\research\ARCHITECTURE.md
```md
# Architecture Research

**Domain:** Agent Skill architecture for Swift/SwiftUI refactor + review guidance
**Researched:** 2026-01-25
**Confidence:** LOW

## Standard Architecture

### System Overview

```
┌───────────────────────────────────────────────────────────────────────┐
│                         Skill Interface Layer                         │
├───────────────────────────────────────────────────────────────────────┤
│  ┌────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Prompts &  │  │ Output Rules │  │ Glossary &   │  │ Constraints  │ │
│  │ Intents    │  │ & Templates  │  │ Terminology  │  │ (Do/Don't)   │ │
│  └─────┬──────┘  └─────┬────────┘  └─────┬────────┘  └─────┬────────┘ │
│        │               │                │                │           │
├────────┴───────────────┴────────────────┴────────────────┴───────────┤
│                         Decision Logic Layer                          │
├───────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────┐    │
│  │  Triage → Scope → Workflow Selection → Decision Gates          │    │
│  └───────────────────────────────────────────────────────────────┘    │
├───────────────────────────────────────────────────────────────────────┤
│                         Workflow Modules                              │
├───────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │
│  │ Refactor     │  │ Review       │  │ Diagnostics  │                │
│  │ Playbooks    │  │ Playbooks    │  │ & Escalation │                │
│  └──────────────┘  └──────────────┘  └──────────────┘                │
├───────────────────────────────────────────────────────────────────────┤
│                         Knowledge Units                               │
├───────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │
│  │ SwiftUI      │  │ Concurrency  │  │ Navigation   │                │
│  │ State Rules  │  │ & Testing    │  │ & Lists      │                │
│  └──────────────┘  └──────────────┘  └──────────────┘                │
└───────────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| Prompts & intents | Define entry points and expected outcomes (refactor vs review) | Short intent blocks and role framing in `README`/entry docs |
| Constraints | Enforce domain boundaries (no architecture mandates, no tooling steps) | Do/Don't lists with rationale |
| Output rules & templates | Keep responses consistent and high-signal | Response schema + example outputs |
| Glossary & terminology | Normalize language across guidance | Definitions and preferred terms |
| Decision logic | Route requests to correct workflow and gates | Triage checklist + decision tables |
| Refactor playbooks | Step-by-step guidance for refactor tasks | Task flows, decision gates, examples |
| Review playbooks | Code review checklists and findings taxonomy | Issue categories, severity, remediation |
| Diagnostics & escalation | When to ask questions or defer | Known unknowns, validation triggers |
| Knowledge units | Swift/SwiftUI rules and pitfalls | Modular topic notes and examples |

## Recommended Project Structure

```
.opencode/
├── agents/                         # Agent roles and high-level behavior
├── get-shit-done/                  # Orchestrator + templates
└── skills/                         # Skill content root
    └── swiftui-refactor-review/    # Skill package
        ├── INDEX.md                # Entry point + navigation
        ├── CONSTRAINTS.md          # Do/Don't + exclusions
        ├── OUTPUT.md               # Response format templates
        ├── GLOSSARY.md             # Domain terms
        ├── DECISIONS.md            # Triage + routing logic
        ├── workflows/              # Refactor/review playbooks
        │   ├── REFACTOR.md
        │   └── REVIEW.md
        ├── topics/                 # Modular knowledge units
        │   ├── STATE.md
        │   ├── CONCURRENCY.md
        │   ├── NAVIGATION.md
        │   ├── PERFORMANCE.md
        │   └── TESTING_DI.md
        └── examples/               # Minimal, focused examples
            ├── refactor-patterns.md
            └── review-findings.md
```

### Structure Rationale

- **`DECISIONS.md`:** separates routing logic from content so workflow selection stays stable as topic content grows.
- **`workflows/`:** refactor and review flows remain distinct but can link into shared topic modules.
- **`topics/`:** small, reusable units avoid repetition and allow partial updates without touching workflows.

## Architectural Patterns

### Pattern 1: Decision-Gated Guidance

**What:** Route requests through gates (scope, change type, severity) before guidance.
**When to use:** Any request that could be review or refactor, or risks violating constraints.
**Trade-offs:** Adds upfront steps but prevents mis-scoped advice.

**Example:**
```markdown
Gate 1: Is the request a review or refactor?
Gate 2: Is the change SwiftUI view, state, navigation, or concurrency?
Gate 3: Does it require asking a question (blocking info)?
```

### Pattern 2: Atomic Rules + Composite Workflows

**What:** Keep canonical rules in topic modules; workflows reference them.
**When to use:** Domains with overlapping guidance across multiple workflows.
**Trade-offs:** Requires linking discipline, but reduces drift.

**Example:**
```markdown
Workflow step → link to topics/STATE.md#ForEach-identity
```

### Pattern 3: Findings Taxonomy for Reviews

**What:** Classify review issues by type and severity (correctness, performance, maintainability, accessibility).
**When to use:** Review output must be consistent across different codebases.
**Trade-offs:** Slightly more structure, faster consumption.

## Data Flow

### Request Flow

```
User Request
    ↓
Triage (intent + scope)
    ↓
Decision Gates (constraints + topic routing)
    ↓
Workflow Module (refactor or review)
    ↓
Topic Units (state, navigation, concurrency, performance)
    ↓
Output Template (final response)
```

### State Management

```
Knowledge Units → Workflows → Output
      ↑                 ↓
   Constraints ← Decision Logic
```

### Key Data Flows

1. **Refactor request:** intent → refactor workflow → topic references → recommendations → output.
2. **Review request:** intent → review workflow → findings taxonomy → remediation → output.

## Scaling Considerations

| Scale | Architecture Adjustments |
|-------|--------------------------|
| Small skill | Keep all rules in one file to reduce navigation friction |
| Medium skill | Split by workflows + topics; add decision logic file |
| Large skill | Add cross-topic index, tags, and change log for updates |

### Scaling Priorities

1. **First bottleneck:** conflicting guidance across files → fix with single-source topic units.
2. **Second bottleneck:** inconsistent outputs → fix with output templates and examples.

## Anti-Patterns

### Anti-Pattern 1: Workflow-Only Guidance

**What people do:** Put all rules inside workflows.
**Why it's wrong:** Rules drift, repeated edits, inconsistent advice.
**Do this instead:** Keep atomic rules in topic units and reference them.

### Anti-Pattern 2: Monolithic Knowledge Dump

**What people do:** One giant document for everything.
**Why it's wrong:** Hard to keep current; weak routing; slow to update.
**Do this instead:** Split into decisions, workflows, and topic modules.

## Integration Points

### External Services

| Service | Integration Pattern | Notes |
|---------|---------------------|-------|
| None (skill-only) | N/A | Avoid tool-specific steps per project constraints |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Decision logic ↔ workflows | References and links | Keep routing in one place |
| Workflows ↔ topics | Direct references | Avoid duplicating rules |

## Build Order (Dependencies)

1. **Constraints + glossary** → establishes boundaries and terms for all other files.
2. **Decision logic** → enables routing to refactor vs review.
3. **Workflows** → refactor and review playbooks.
4. **Topic units** → attach as references from workflows.
5. **Output templates + examples** → validate guidance consistency.

## Sources

- No external sources used; based on internal synthesis. Confidence is LOW and should be validated.

---
*Architecture research for: agent skill for Swift/SwiftUI refactor + review*
*Researched: 2026-01-25*

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
