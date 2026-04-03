---
id: github.com-efremidze-swift-patterns-skill-635dd9ca
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.407556
---

# KNOWLEDGE EXTRACT: github.com_efremidze_swift-patterns-skill_635dd9ca
> **Extracted on:** 2026-04-01 12:39:54
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521941/github.com_efremidze_swift-patterns-skill_635dd9ca

---

## File: `.gitignore`
```
# Dependencies
node_modules/
npm-debug.log*

# Build output
build/
dist/
*.js
*.js.map
*.d.ts

# Keep root files
!src/**/*.js

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
Thumbs.db

# Logs
logs/
*.log

# Environment
.env
.env.local
.env.*.local

# Testing
coverage/
.nyc_output/

# Git keep files
*.gitkeep

# MCP
.swift-patterns-mcp/

# Claude Code
.claude/
.gsd/
.opencode/
.worktrees/

# Secrets
*.pem
*.key
```

## File: `AGENTS.md`
```markdown
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

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Swift Patterns

We'd love your help making this skill better! Whether you're fixing outdated patterns, adding modern Swift APIs, or clarifying confusing guidance—every improvement helps developers write better code.

## About Agent Skills

This repository follows the [Agent Skills format](https://agentskills.io/home). See the [documentation](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills) for details on structure and format.

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

- [Agent Skills](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills)
- [AgentSkills.io](https://agentskills.io/home)

## Questions?

Open an issue to discuss major changes before starting work.

## Code of Conduct

Be respectful and constructive. Focus on making Swift guidance better for everyone.
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Lasha Efremidze

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

## File: `README.md`
```markdown
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

## File: `marketplace.json`
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

## File: `plugin.json`
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

## File: `efremidze-swift-patterns-skill-2e9b66b/.gitignore`
```
# Dependencies
node_modules/
npm-debug.log*

# Build output
build/
dist/
*.js
*.js.map
*.d.ts

# Keep root files
!src/**/*.js

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
Thumbs.db

# Logs
logs/
*.log

# Environment
.env
.env.local
.env.*.local

# Testing
coverage/
.nyc_output/

# Git keep files
*.gitkeep

# MCP
.swift-patterns-mcp/

# Claude Code
.claude/
.gsd/
.opencode/
.worktrees/

# Secrets
*.pem
*.key
```

## File: `efremidze-swift-patterns-skill-2e9b66b/AGENTS.md`
```markdown
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

## File: `efremidze-swift-patterns-skill-2e9b66b/CONTRIBUTING.md`
```markdown
# Contributing to Swift Patterns

We'd love your help making this skill better! Whether you're fixing outdated patterns, adding modern Swift APIs, or clarifying confusing guidance—every improvement helps developers write better code.

## About Agent Skills

This repository follows the [Agent Skills format](https://agentskills.io/home). See the [documentation](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills) for details on structure and format.

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

- [Agent Skills](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills)
- [AgentSkills.io](https://agentskills.io/home)

## Questions?

Open an issue to discuss major changes before starting work.

## Code of Conduct

Be respectful and constructive. Focus on making Swift guidance better for everyone.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/LICENSE`
```
MIT License

Copyright (c) 2026 Lasha Efremidze

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

## File: `efremidze-swift-patterns-skill-2e9b66b/README.md`
```markdown
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

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/SKILL.md`
```markdown
---
name: swift-patterns
description: Review, refactor, or build SwiftUI features with correct state management, modern API usage, optimal view composition, navigation patterns, performance optimization, and testing best practices.
---

# swift-patterns

Review, refactor, or build SwiftUI features with correct state management, modern API usage, optimal view composition, and performance-conscious patterns. Prioritize native APIs, Apple design guidance, and testable code structure. This skill focuses on facts and best practices without enforcing specific architectural patterns.

## Workflow Decision Tree

### 1) Review existing SwiftUI code
→ Read `references/workflows-review.md` for review methodology
- Check state management against property wrapper selection (see `references/state.md`)
- Verify view composition and extraction patterns (see `references/view-composition.md`)
- Audit list performance and identity stability (see `references/lists-collections.md`)
- Validate modern API usage (see `references/modern-swiftui-apis.md`)
- Check async work patterns with .task (see `references/concurrency.md`)
- Verify navigation implementation (see `references/navigation.md`)
- Use Review Response Template (below)

### 2) Refactor existing SwiftUI code
→ Read `references/workflows-refactor.md` for refactor methodology
- Extract complex views using playbooks (see `references/refactor-playbooks.md`)
- Migrate deprecated APIs to modern equivalents (see `references/modern-swiftui-apis.md`)
- Optimize performance hot paths (see `references/performance.md`)
- Restructure state ownership (see `references/state.md`)
- Apply common patterns (see `references/patterns.md`)
- Use Refactor Response Template (below)

### 3) Implement new SwiftUI features
- Design data flow first: identify owned vs injected state (see `references/state.md`)
- Structure views for optimal composition (see `references/view-composition.md`)
- Use modern APIs only (see `references/modern-swiftui-apis.md`)
- Handle async work with .task modifier (see `references/concurrency.md`)
- Apply performance patterns early (see `references/performance.md`)
- Implement navigation flows (see `references/navigation.md`)

### 4) Answer best practice questions
- Load relevant reference file(s) based on topic (see Reference Files below)
- Provide direct guidance with examples

**If intent unclear, ask:** "Do you want findings only (review), or should I change the code (refactor)?"

## Response Templates

**Review Response:**
1. **Scope** - What was reviewed
2. **Findings** - Grouped by severity with actionable statements
3. **Evidence** - File paths or code locations
4. **Risks and tradeoffs** - What could break or needs attention
5. **Next steps** - What to fix first or verify

**Refactor Response:**
1. **Intent + scope** - What is being changed and why
2. **Changes** - Bulleted list with file paths
3. **Behavior preservation** - What should remain unchanged
4. **Next steps** - Tests or verification needed

## Quick Reference: Property Wrapper Selection

| Wrapper | Use When | Ownership |
|---------|----------|-----------|
| `@State` | Internal view state (value type or `@Observable` class) | View owns |
| `@Binding` | Child needs to modify parent's state | Parent owns |
| `@Bindable` | Injected `@Observable` object needing bindings | Injected |
| `let` | Read-only value from parent | Injected |
| `var` + `.onChange()` | Read-only value needing reactive updates | Injected |

**Key rules:**
- Always mark `@State` as `private` (makes ownership explicit)
- Never use `@State` for passed values (accepts initial value only)
- Use `@State` with `@Observable` classes (not `@StateObject`)

See `references/state.md` for detailed guidance and tradeoffs.

## Quick Reference: Modern API Replacements

| Deprecated | Modern Alternative | Notes |
|------------|-------------------|-------|
| `foregroundColor()` | `foregroundStyle()` | Supports dynamic type |
| `cornerRadius()` | `.clipShape(.rect(cornerRadius:))` | More flexible |
| `NavigationView` | `NavigationStack` | Type-safe navigation |
| `tabItem()` | `Tab` API | iOS 18+ |
| `onTapGesture()` | `Button` | Unless need location/count |
| `onChange(of:) { value in }` | `onChange(of:) { old, new in }` or `onChange(of:) { }` | Two or zero parameters |
| `UIScreen.main.bounds` | `GeometryReader` or layout APIs | Avoid hard-coded sizes |

See `references/modern-swiftui-apis.md` for complete migration guide.

## Review Checklist

Use this when reviewing SwiftUI code:

### State Management
- [ ] `@State` properties marked `private`
- [ ] Passed values NOT declared as `@State` or `@StateObject`
- [ ] `@Binding` only where child modifies parent state
- [ ] Property wrapper selection follows ownership rules
- [ ] State ownership clear and intentional

### Modern APIs
- [ ] No deprecated modifiers (foregroundColor, cornerRadius, etc.)
- [ ] Using `NavigationStack` instead of `NavigationView`
- [ ] Using `Button` instead of `onTapGesture` when appropriate
- [ ] Using two-parameter or no-parameter `onChange()`

### View Composition
- [ ] Using modifiers over conditionals for state changes (maintains identity)
- [ ] Complex views extracted to separate subviews
- [ ] Views kept small and focused
- [ ] View `body` simple and pure (no side effects)

### Navigation & Sheets
- [ ] Using `navigationDestination(for:)` for type-safe navigation
- [ ] Using `.sheet(item:)` for model-based sheets
- [ ] Sheets own their dismiss actions

### Lists & Collections
- [ ] `ForEach` uses stable identity (never `.indices` for dynamic data)
- [ ] Constant number of views per `ForEach` element
- [ ] No inline filtering in `ForEach` (prefilter and cache)
- [ ] No `AnyView` in list rows

### Performance
- [ ] Passing only needed values to views (not large config objects)
- [ ] Eliminating unnecessary dependencies
- [ ] Checking value changes before state assignment in hot paths
- [ ] Using `LazyVStack`/`LazyHStack` for large lists
- [ ] No object creation in view `body`

### Async Work
- [ ] Using `.task` for automatic cancellation
- [ ] Using `.task(id:)` for value-dependent tasks
- [ ] Not mixing `.onAppear` with async work

See reference files for detailed explanations of each item.

## Constraints

- **Swift/SwiftUI focus only** - Exclude server-side Swift and UIKit unless bridging required
- **No Swift concurrency patterns** - Use `.task` for SwiftUI async work
- **No architecture mandates** - Don't require MVVM/MVC/VIPER or specific structures
- **No formatting/linting rules** - Focus on correctness and patterns
- **No tool-specific guidance** - No Xcode, Instruments, or IDE instructions
- **Citations allowed:** `developer.apple.com/documentation/swiftui/`, `developer.apple.com/documentation/swift/`

All workflows must follow these constraints.

## Philosophy

This skill focuses on **facts and best practices** from Apple's documentation:
- Modern APIs over deprecated ones
- Clear state ownership patterns
- Performance-conscious view composition
- Testable code structure
- No architectural mandates (MVVM/VIPER not required)
- Apple Human Interface Guidelines adherence

## Reference Files

All references in `references/`:
- `workflows-review.md` - Review methodology and findings taxonomy
- `workflows-refactor.md` - Refactor methodology and invariants
- `refactor-playbooks.md` - Step-by-step refactor guides
- `state.md` - Property wrappers and ownership patterns
- `navigation.md` - Navigation implementation patterns
- `view-composition.md` - View structure and extraction
- `lists-collections.md` - Identity and ForEach patterns
- `scrolling.md` - Scroll handling and pagination
- `concurrency.md` - Async work with .task
- `performance.md` - Optimization strategies
- `testing-di.md` - Testing and dependency injection
- `patterns.md` - Common SwiftUI patterns
- `modern-swiftui-apis.md` - Legacy API migration
- `code-review-refactoring.md` - Code quality checks
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/code-review-refactoring.md`
```markdown
# Code Smells & Anti-Patterns (SwiftUI)

Common issues to look for when reviewing or refactoring SwiftUI code.

## SwiftUI Code Smells

- **Duplicate source of truth:** `@State` and model both hold the same value.
- **Stored derived state:** Computing and storing values that could be computed properties.
- **Side effects in body:** Mutations or async work triggered during view rendering.
- **Unstable list identity:** Using `.indices` or non-unique IDs for dynamic `ForEach`.
- **Competing navigation sources:** Multiple `NavigationStack` roots or duplicated path state.
- **Heavy work in body:** Formatters, parsing, or sorting recreated every render.
- **Silent error handling:** Swallowing errors without user feedback.

## Examples

### Duplicate Source of Truth
```swift
// Bad: state duplicated
struct PlayerView: View {
    @State private var isPlaying = false
    let model: PlayerModel

    var body: some View {
        Toggle("Playing", isOn: $isPlaying)
            .onChange(of: isPlaying) { model.isPlaying = $0 }
    }
}

// Good: single source of truth
struct PlayerView: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Toggle("Playing", isOn: $isPlaying)
    }
}
```

### Unstable List Identity
```swift
// Bad: indices shift on insert/delete
ForEach(items.indices, id: \.self) { index in
    RowView(item: items[index])
}

// Good: stable identity from model
ForEach(items, id: \.id) { item in
    RowView(item: item)
}
```

### Stored Derived State
```swift
// Bad: derived value stored and manually synced
struct CheckoutView: View {
    let subtotal: Decimal
    @State private var total: Decimal = 0

    var body: some View {
        Text("Total: \(total)")
            .onAppear { total = subtotal * 1.08 }
    }
}

// Good: compute directly
struct CheckoutView: View {
    let subtotal: Decimal
    var total: Decimal { subtotal * 1.08 }

    var body: some View {
        Text("Total: \(total)")
    }
}
```

## Anti-Patterns

- Global mutable state accessed by multiple views without clear ownership.
- Navigation driven by both view state and model state (competing sources).
- Copying view state into models without ownership boundaries.
- Silent error handling that hides failures from users.
- Over-abstraction that reduces testability without clear benefit.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/concurrency.md`
```markdown
# SwiftUI Concurrency (Lifecycle-Scoped)

## Overview
This reference focuses on SwiftUI-friendly async patterns: `.task`, `.task(id:)`, cancellation checks, and safe UI updates with `@MainActor`.
It intentionally avoids deep concurrency patterns and architecture mandates.

## Decision Tree: `.task` vs `.onAppear` vs `.onChange`

1) Do you need async work tied to the view lifecycle?
- Yes -> Use `.task`

2) Does the async work depend on a changing identifier or filter?
- Yes -> Use `.task(id:)` to auto-cancel and restart when the value changes

3) Do you need to react to a value change (possibly multiple times)?
- Yes -> Use `.onChange` and start async work inside a `Task`

4) Do you only need lightweight, non-async setup when a view appears?
- Yes -> Use `.onAppear` with a guard to avoid duplicate work

## Core Patterns

### Basic `.task` for View-Scoped Loading
```swift
struct DetailView: View {
    @State private var item: Item?

    var body: some View {
        Group {
            if let item {
                Text(item.title)
            } else {
                ProgressView()
            }
        }
        .task {
            await loadItem()
        }
    }

    @MainActor
    private func loadItem() async {
        item = await fetchItem()
    }
}
```

### `.task(id:)` for ID-Driven Reloads
```swift
struct FilteredList: View {
    @State private var items: [Item] = []
    let filter: Filter

    var body: some View {
        List(items) { item in
            Text(item.title)
        }
        .task(id: filter) {
            await load(filter: filter)
        }
    }

    @MainActor
    private func load(filter: Filter) async {
        items = await fetchItems(filter: filter)
    }
}
```

### `.onChange` for Value-Driven Async Work
```swift
.onChange(of: query) { _, newValue in
    Task {
        await performSearch(query: newValue)
    }
}
```

## Cancellation Awareness
SwiftUI cancels `.task` when the view disappears or the id changes. Long-running work should check cancellation.

```swift
func loadPages() async throws {
    for page in pages {
        try Task.checkCancellation()
        try await fetchPage(page)
    }
}
```

## `@MainActor` for UI Updates
Update UI state on the main actor.

- Use `@MainActor` on functions that mutate view state.
- If your project uses default actor isolation, explicit `@MainActor` may not be required.

```swift
@MainActor
func updateState(with items: [Item]) {
    self.items = items
}
```

## Common Pitfalls

- Starting async work in `body` causes repeated execution on every render.
- Using `.onAppear` for network loads without guards leads to duplicate requests.
- Ignoring cancellation can result in stale or out-of-order UI updates.
- Updating UI state off the main actor can cause crashes or warnings.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/lists-collections.md`
```markdown
# Lists and Collections

Use stable identity and lazy containers to keep lists correct and performant.

## Stable Identity

- Prefer `Identifiable` models for lists and `ForEach`.
- If not `Identifiable`, provide a stable `id:`.
- Avoid `.indices` for dynamic data; indices shift on insert/delete and break identity.

```swift
struct Item: Identifiable {
    let id: UUID
    let title: String
}

List(items) { item in
    Text(item.title)
}
```

## List vs ScrollView + LazyVStack

- Use `List` for standard scrolling, selection, swipe actions, and system row behavior.
- Use `ScrollView` + `LazyVStack` for fully custom layouts or mixed content.
- For large collections, prefer lazy containers (`List`, `LazyVStack`, `LazyVGrid`).

## Sections and Empty States

- Group related rows into `Section` for clarity.
- Provide explicit empty states when the collection is empty.

```swift
if items.isEmpty {
    ContentUnavailableView("No Items", systemImage: "tray")
} else {
    List {
        Section("Recent") {
            ForEach(items) { item in
                Row(item: item)
            }
        }
    }
}
```

## Row Composition

- Keep row views lightweight and pure.
- Move heavy work (formatting, image decoding) out of row `body` when it can be cached.
- Pass values into rows; avoid side effects inside the row body.

## Common Pitfalls

- **Identity churn:** using unstable IDs causes rows to show the wrong data.
- **Row-level side effects:** triggers repeat work during scrolling.
- **Too much per-row state:** pushes state ownership into the wrong place.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/modern-swiftui-apis.md`
```markdown
# Modern SwiftUI API Replacements

Prefer modern APIs when the deployment target allows. This catalog covers legacy patterns and their replacements, plus new APIs by iOS version.

## Contents

### Legacy → Modern Migration Tables
- [Navigation](#navigation)
- [Appearance](#appearance)
- [State & Data](#state--data)
- [Events & Lifecycle](#events--lifecycle)
- [Lists & Collections](#lists--collections)
- [Tabs (iOS 18+)](#tabs-ios-18)
- [Layout & Sizing](#layout--sizing)
- [Sheets & Presentation](#sheets--presentation)

### New APIs by Version
- [iOS 17 New APIs](#ios-17-new-apis) - @Observable, ScrollView, Animation, Inspector, Sensory Feedback, Container Relative Frame, onChange initial, Shape Improvements
- [iOS 18 New APIs](#ios-18-new-apis) - @Entry, @Previewable, Tab API, Mesh Gradients, Zoom Transitions, SF Symbol Animations, Custom Container Views, Controls
- [iOS 26 New APIs](#ios-26-new-apis) - Liquid Glass, WebView, Rich Text, Glass Button, Toolbar Spacer, TabView Minimize, Navigation Subtitles, Label Icon Width, Scene Padding, @Animatable, 3D Charts, openURL In-App, Drag Container

### Guidelines
- [Migration Priority](#migration-priority)
- [Availability Patterns](#availability-patterns)

## Navigation

| Legacy | Modern | Notes |
|--------|--------|-------|
| `NavigationView` | `NavigationStack` | Value-based, type-safe navigation |
| `NavigationLink(destination:)` | `NavigationLink(value:)` + `navigationDestination(for:)` | Decouple link from destination |
| `navigationBarTitle(_:)` | `navigationTitle(_:)` | Unified API |
| `navigationBarItems(leading:trailing:)` | `toolbar { ToolbarItem(placement:) }` | Consistent placement |
| `navigationBarHidden(_:)` | `toolbar(.hidden, for: .navigationBar)` | iOS 16+ |
| `.isDetailLink(false)` | Not needed | NavigationStack handles automatically |

## Appearance

| Legacy | Modern | Notes |
|--------|--------|-------|
| `foregroundColor(_:)` | `foregroundStyle(_:)` | Supports gradients, materials |
| `accentColor(_:)` | `tint(_:)` | Per-view accent color |
| `cornerRadius(_:)` | `.clipShape(.rect(cornerRadius:))` | More flexible, selective corners |
| `background(Color.x)` | `background { }` or `.background(.x, in:)` | Shape-aware backgrounds |
| `overlay(Circle())` | `overlay { Circle() }` | ViewBuilder syntax |

## State & Data

| Legacy | Modern | Notes |
|--------|--------|-------|
| `@StateObject` | `@State` with `@Observable` | Simpler, no wrapper needed |
| `@ObservedObject` | Direct reference to `@Observable` | Automatic tracking |
| `@EnvironmentObject` | `@Environment(MyType.self)` | Type-safe environment |
| `@Published` | Not needed with `@Observable` | Automatic property tracking |
| `Image("name")` | `Image(.name)` | Type-safe asset references |

## Events & Lifecycle

| Legacy | Modern | Notes |
|--------|--------|-------|
| `onChange(of:) { value in }` | `onChange(of:) { old, new in }` or `onChange(of:) { }` | Two or zero params (iOS 17+) |
| `onAppear { Task { } }` | `.task { }` | Auto-cancellation on disappear |
| `onReceive(publisher)` | `.task` or `.onChange` | When lifecycle-safe |
| `onTapGesture { }` | `Button` | Unless need tap location/count |

## Lists & Collections

| Legacy | Modern | Notes |
|--------|--------|-------|
| Manual pull-to-refresh | `.refreshable { }` | Native refresh control |
| `EditButton()` standalone | `.toolbar { EditButton() }` | Toolbar placement |
| `id: \.self` for value types | Prefer `Identifiable` | Better performance |

## Tabs (iOS 18+)

| Legacy | Modern | Notes |
|--------|--------|-------|
| `TabView { }.tabItem { }` | `TabView { Tab("", systemImage:) { } }` | New Tab API |
| Manual sidebar | `TabViewStyle.sidebarAdaptable` | Adaptive sidebar on iPad |

## Layout & Sizing

| Legacy | Modern | Notes |
|--------|--------|-------|
| `UIScreen.main.bounds` | `GeometryReader` or layout APIs | Avoid hard-coded sizes |
| `GeometryReader` for sizing | `containerRelativeFrame()` | iOS 17+, cleaner |
| `frame(width:height:)` fixed | `frame(minWidth:maxWidth:)` | Flexible sizing |

## Sheets & Presentation

| Legacy | Modern | Notes |
|--------|--------|-------|
| `.sheet(isPresented:)` | `.sheet(item:)` | When driven by model |
| Custom sheet sizing | `presentationDetents([.medium, .large])` | Native detents |
| Dismiss via binding | `@Environment(\.dismiss)` | Cleaner dismiss action |

---

## iOS 17 New APIs

### @Observable Macro
Replaces `ObservableObject` with simpler syntax:
```swift
// iOS 17+
@Observable
class UserModel {
    var name = ""      // Automatically tracked
    var age = 0
}

struct ContentView: View {
    @State private var user = UserModel()  // Use @State, not @StateObject
    var body: some View {
        TextField("Name", text: $user.name)
    }
}
```

### Scroll View Enhancements
```swift
ScrollView {
    content
}
.scrollTargetBehavior(.paging)           // Paging behavior
.scrollPosition(id: $selectedID)          // Programmatic scroll
.scrollTransition { content, phase in     // Scroll-based transitions
    content.opacity(phase.isIdentity ? 1 : 0.5)
}
.defaultScrollAnchor(.bottom)             // Start at bottom
.scrollIndicatorsFlash(trigger: items)    // Flash indicators
```

### Animation Improvements
```swift
// New spring animations
withAnimation(.bouncy) { }
withAnimation(.snappy) { }

// Phase animator for multi-step animations
PhaseAnimator([0, 1, 2]) { phase in
    Circle()
        .scaleEffect(phase == 1 ? 1.5 : 1)
}

// Keyframe animations
KeyframeAnimator(initialValue: AnimationValues()) { value in
    Circle()
        .scaleEffect(value.scale)
        .offset(value.offset)
} keyframes: { _ in
    KeyframeTrack(\.scale) {
        SpringKeyframe(1.5, duration: 0.3)
        SpringKeyframe(1.0, duration: 0.3)
    }
}

// Animation completion
withAnimation(.default) {
    isExpanded.toggle()
} completion: {
    // Animation finished
}
```

### Inspector Modifier
```swift
NavigationStack {
    ContentView()
        .inspector(isPresented: $showInspector) {
            InspectorView()
        }
}
```

### Sensory Feedback
```swift
Button("Tap") { }
    .sensoryFeedback(.impact, trigger: tapCount)

// Conditional feedback
Button("Submit") { }
    .sensoryFeedback(.success, trigger: submitCount) { old, new in
        new > old  // Only when count increases
    }
```

### Container Relative Frame
```swift
Image("photo")
    .containerRelativeFrame(.horizontal) { size, axis in
        size * 0.8  // 80% of container width
    }
```

### onChange with Initial Value
```swift
.onChange(of: searchText, initial: true) { oldValue, newValue in
    // Fires immediately with initial value
}
```

### Shape Improvements
```swift
// Selective corner rounding
RoundedRectangle(cornerRadii: .init(topLeading: 20, bottomTrailing: 20))

// Combined fill and stroke
Circle()
    .stroke(.red, lineWidth: 2)
    .fill(.blue)
```

---

## iOS 18 New APIs

### @Entry Macro for Environment
```swift
// Simplified custom environment values
extension EnvironmentValues {
    @Entry var myCustomValue: String = "default"
}

// Usage
.environment(\.myCustomValue, "custom")
@Environment(\.myCustomValue) var value
```

### @Previewable Macro
```swift
#Preview {
    @Previewable @State var count = 0
    Button("Count: \(count)") { count += 1 }
}
```

### Tab API
```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    Tab("Search", systemImage: "magnifyingglass", role: .search) {
        SearchView()
    }
}
.tabViewStyle(.sidebarAdaptable)  // Sidebar on iPad
```

### Mesh Gradients
```swift
MeshGradient(
    width: 3, height: 3,
    points: [
        [0, 0], [0.5, 0], [1, 0],
        [0, 0.5], [0.5, 0.5], [1, 0.5],
        [0, 1], [0.5, 1], [1, 1]
    ],
    colors: [
        .red, .orange, .yellow,
        .green, .blue, .purple,
        .pink, .cyan, .mint
    ]
)
```

### Zoom Navigation Transition
```swift
NavigationLink(value: item) {
    ItemRow(item: item)
}
.matchedTransitionSource(id: item.id, in: namespace)

// Destination
DetailView(item: item)
    .navigationTransition(.zoom(sourceID: item.id, in: namespace))
```

### SF Symbol Animations
```swift
Image(systemName: "checkmark.circle")
    .symbolEffect(.bounce, value: isComplete)
    .symbolEffect(.rotate, value: isLoading)
```

### Custom Container Views
```swift
struct CardStack<Content: View>: View {
    @ViewBuilder var content: Content

    var body: some View {
        ForEach(subviews: content) { subview in
            subview
                .padding()
                .background(.ultraThinMaterial)
        }
    }
}
```

### Controls for Lock Screen / Control Center
```swift
struct MyControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(kind: "MyControl") {
            ControlWidgetButton(action: MyIntent()) {
                Label("Toggle", systemImage: "lightbulb")
            }
        }
    }
}
```

---

## iOS 26 New APIs

### Liquid Glass Design
Automatic with Xcode 26 build. Opt out if needed:
```swift
// Disable Liquid Glass for transition period
.preferredGlassEffect(.disabled)
```

### WebView (Native)
```swift
import WebKit

struct BrowserView: View {
    @State private var page = WebPage()

    var body: some View {
        WebView(page)
            .onAppear {
                page.load(URLRequest(url: URL(string: "https://apple.com")!))
            }
    }
}
```

### Rich Text Editing with AttributedString
```swift
struct RichTextEditor: View {
    @State private var text = AttributedString("Hello")

    var body: some View {
        TextEditor(text: $text)
            .toolbar {
                Button("Bold") {
                    text.font = .boldSystemFont(ofSize: 17)
                }
            }
    }
}
```

### Glass Button Style
```swift
Button("Action") { }
    .buttonStyle(.glass)
```

### Toolbar Spacer
```swift
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        Button("Save") { }
    }
    ToolbarSpacer(.fixed)
    ToolbarItem(placement: .primaryAction) {
        Button("Share") { }
    }
}
```

### TabView Minimize on Scroll
```swift
TabView {
    Tab("Home", systemImage: "house") {
        ScrollView {
            // Content
        }
    }
}
.tabBarMinimizeBehavior(.automatic)
```

### Navigation Subtitles
```swift
.navigationTitle("Documents")
.navigationSubtitle("23 items")
```

### Label Icon Fixed Width
```swift
Label("Settings", systemImage: "gear")
    .labelIconFixedWidth()
```

### Scene Padding
```swift
VStack {
    content
}
.scenePadding()  // Automatic padding for scene context
```

### @Animatable Macro
```swift
@Animatable
struct PulsingCircle: View {
    var scale: Double

    var body: some View {
        Circle()
            .scaleEffect(scale)
    }
}
```

### 3D Charts
```swift
Chart3D {
    ForEach(data) { item in
        BarMark3D(
            x: .value("X", item.x),
            y: .value("Y", item.y),
            z: .value("Z", item.z)
        )
    }
}
```

### openURL In-App Browser
```swift
@Environment(\.openURL) var openURL

Button("Open Link") {
    openURL(url, prefersInApp: true)  // Opens in-app browser
}
```

### Drag Container
```swift
List(selection: $selection) {
    ForEach(items) { item in
        ItemRow(item: item)
    }
}
.dragContainer(for: selection) { items in
    // Return drag preview
}
```

---

## Migration Priority

1. **High:** NavigationView → NavigationStack (architecture impact)
2. **High:** ObservableObject → @Observable (iOS 17+)
3. **High:** TabView tabItem → Tab API (iOS 18+)
4. **Medium:** foregroundColor → foregroundStyle
5. **Medium:** onChange single-param → two-param
6. **Medium:** @EnvironmentObject → @Environment
7. **Low:** cornerRadius → clipShape (visual only)

## Availability Patterns

```swift
// Feature check
if #available(iOS 17, *) {
    ContentView()
        .containerRelativeFrame(.horizontal)
} else {
    GeometryReader { geo in
        ContentView()
            .frame(width: geo.size.width * 0.8)
    }
}

// View modifier extension for compatibility
extension View {
    @ViewBuilder
    func iOS17ContainerFrame() -> some View {
        if #available(iOS 17, *) {
            self.containerRelativeFrame(.horizontal)
        } else {
            self
        }
    }
}
```

Sources: [Hacking with Swift - iOS 17](https://www.hackingwithswift.com/articles/260/whats-new-in-swiftui-for-ios-17), [Hacking with Swift - iOS 18](https://www.hackingwithswift.com/articles/270/whats-new-in-swiftui-for-ios-18), [Hacking with Swift - iOS 26](https://www.hackingwithswift.com/articles/278/whats-new-in-swiftui-for-ios-26), [Swift with Majid - WWDC25](https://swiftwithmajid.com/2025/06/10/what-is-new-in-swiftui-after-wwdc25/)
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/navigation.md`
```markdown
# NavigationStack Guidance

Use value-based navigation with a single source of truth. Keep navigation state in one place without mandating a coordinator pattern.

## Core Patterns

- Prefer `NavigationStack` over legacy navigation APIs.
- Use `NavigationLink(value:)` with `navigationDestination(for:)`.
- Keep navigation state in one owner (root view, feature root, or environment model).
- Avoid nested `NavigationStack` instances in the same flow.

## Basic Structure

```swift
enum Route: Hashable {
    case detail(Item.ID)
}

struct RootView: View {
    @State private var path: [Route] = []

    var body: some View {
        NavigationStack(path: $path) {
            List(items) { item in
                NavigationLink(value: Route.detail(item.id)) {
                    Text(item.title)
                }
            }
            .navigationDestination(for: Route.self) { route in
                switch route {
                case .detail(let id):
                    DetailView(id: id)
                }
            }
        }
    }
}
```

## Navigation State Ownership

- Use `@State` for simple paths local to a flow.
- For shared navigation state, store the path in a shared model injected through the environment.
- Keep programmatic navigation scoped to a single owner to avoid conflicting updates.

## Sheets and Full-Screen Presentation

- Use `sheet(item:)` when a selection drives presentation.
- Use `sheet(isPresented:)` for simple toggles.
- Use `fullScreenCover` for full-screen flows.
- Dismiss with `@Environment(\.dismiss)` from within the presented view.

```swift
struct ContentView: View {
    @State private var selectedItem: Item?

    var body: some View {
        List(items) { item in
            Button(item.title) { selectedItem = item }
        }
        .sheet(item: $selectedItem) { item in
            DetailSheet(item: item)
        }
    }
}

struct DetailSheet: View {
    let item: Item
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            DetailView(id: item.id)
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) {
                        Button("Close") { dismiss() }
                    }
                }
        }
    }
}
```

## Avoid These Patterns

- Nested `NavigationStack` inside a view that is already in a stack.
- Mixing `NavigationView` and `NavigationStack` in the same flow.
- Scattering navigation state across multiple views.

## Consider When Needed (Optional)

- Use `NavigationPath` for dynamic, multi-type navigation stacks.
- Consider deep-link parsing and path restoration only when the product needs it.

## Modern Replacements

For legacy navigation API replacements, see `references/modern-swiftui-apis.md`.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/patterns.md`
```markdown
# Reusable SwiftUI Patterns

Building blocks for common SwiftUI scenarios. Use these patterns as starting points, not rigid templates.

## Container Views

Wrap content with loading/error states to avoid repeating conditional logic.

```swift
struct AsyncContentView<Content: View>: View {
    let isLoading: Bool
    let error: Error?
    @ViewBuilder let content: () -> Content
    let retry: () -> Void

    var body: some View {
        if isLoading {
            ProgressView()
        } else if let error {
            ContentUnavailableView {
                Label("Error", systemImage: "exclamationmark.triangle")
            } description: {
                Text(error.localizedDescription)
            } actions: {
                Button("Retry", action: retry)
            }
        } else {
            content()
        }
    }
}

// Usage
AsyncContentView(
    isLoading: viewModel.isLoading,
    error: viewModel.error,
    content: { UserList(users: viewModel.users) },
    retry: { Task { await viewModel.load() } }
)
```

## ViewModifiers for Reusable Styling

Extract repeated styling into modifiers instead of copying view code.

```swift
struct CardStyle: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color(.systemBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .shadow(color: .black.opacity(0.1), radius: 5, y: 2)
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardStyle())
    }
}

// Usage
Text("Hello").cardStyle()
```

## Environment-Based Dependency Injection

Use custom environment keys for app-wide dependencies.

```swift
// Define the key
private struct UserServiceKey: EnvironmentKey {
    static let defaultValue: UserServiceProtocol = UserService()
}

extension EnvironmentValues {
    var userService: UserServiceProtocol {
        get { self[UserServiceKey.self] }
        set { self[UserServiceKey.self] = newValue }
    }
}

// Inject at app root
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.userService, UserService())
        }
    }
}

// Use in views
struct ContentView: View {
    @Environment(\.userService) private var userService

    var body: some View {
        Text("Hello")
            .task {
                let users = try? await userService.fetchUsers()
            }
    }
}
```

## PreferenceKeys for Child-to-Parent Communication

Pass values up the view hierarchy when callbacks aren't practical.

```swift
struct ScrollOffsetPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = nextValue()
    }
}

struct ContentView: View {
    @State private var scrollOffset: CGFloat = 0

    var body: some View {
        ScrollView {
            VStack {
                ForEach(0..<50, id: \.self) { i in
                    Text("Item \(i)")
                }
            }
            .background(
                GeometryReader { geometry in
                    Color.clear.preference(
                        key: ScrollOffsetPreferenceKey.self,
                        value: geometry.frame(in: .named("scroll")).minY
                    )
                }
            )
        }
        .coordinateSpace(name: "scroll")
        .onPreferenceChange(ScrollOffsetPreferenceKey.self) { value in
            scrollOffset = value
        }
    }
}
```

## When to Use Each Pattern

- **Container views**: Loading states, error handling, empty states, permission gates
- **ViewModifiers**: Repeated styling, conditional appearance, reusable animations
- **Environment DI**: Services, repositories, feature flags, app-wide configuration
- **PreferenceKeys**: Scroll position, child geometry, aggregating values from children
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/performance.md`
```markdown
# Performance (SwiftUI)

Use this reference to apply a baseline checklist first, then consider safe, SwiftUI-specific optimizations.

## Performance baseline

Start here before suggesting changes:

- Expensive work in `body` (formatters, parsing, sorting, image decoding).
- Unstable list identity (indices or non-unique IDs) causing row churn.
- Heavy work on the main thread (blocking file/network/JSON work).
- Async work detached from the view lifecycle (duplicate or stale tasks).

If issues persist after baseline fixes, profiling tools like Instruments can help identify hot paths.

## Safe optimizations

Consider these when the baseline checklist points to them:

- **Identity stability:** use stable IDs in `ForEach` and `List`. See `references/lists-collections.md`.
- **Lazy containers:** use `List`, `LazyVStack`, or `LazyVGrid` for long collections. See `references/scrolling.md`.
- **Expensive-work avoidance:** move formatters, parsing, and derived values out of `body` so they are not recreated every render.

## SwiftUI lifecycle for async work

Prefer `.task` to tie async work to view lifecycle, and check cancellation in long-running tasks.
Use `.task(id:)` when work depends on inputs like filters, IDs, or search terms.

## SwiftUI snippets

### Stable identity in `ForEach`
```swift
ForEach(items, id: \.id) { item in
    Row(item: item)
}
```

### Move formatter out of `body`
```swift
private let formatter: DateFormatter = {
    let f = DateFormatter()
    f.dateStyle = .medium
    return f
}()

var body: some View {
    Text(formatter.string(from: date))
}
```

### Tie async work to view lifecycle
```swift
.task(id: userID) {
    try Task.checkCancellation()
    await loadUser(id: userID)
}
```

## Risk cues (split refactors)

If any of these change, split the refactor or add tests first:

- State ownership moves between views or wrappers.
- List identity or ordering changes.
- Async work moves between `body`, `.task`, or other lifecycle hooks.

## Related references

- `references/lists-collections.md` for stable identity guidance.
- `references/scrolling.md` for lazy containers and pagination patterns.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/refactor-playbooks.md`
```markdown
# Refactor Playbooks (SwiftUI)

Goal-based playbooks for behavior-preserving refactors. Each playbook starts from a baseline, preserves refactor invariants, and ends with verification against the original behavior.

**Invariants:** See [workflows-refactor.md](workflows-refactor.md#invariants). These are non-negotiables for every step.

## Playbook: View extraction

**Goal**
Extract a view to improve readability while preserving state ownership, stable identity, and data flow.

**Pre-checks**
- Capture the current behavior baseline (visual output, interactions, state changes).
- Identify state owners vs editors using [State ownership](../../../vault/archives/archive_legacy/claude-scientific-skills/scientific-skills/markdown-mermaid-writing/references/diagrams/state.md).
- Map data-flow paths using [View composition](view-composition.md).
- Confirm any list content uses stable identity per Invariants.

**Steps**
1) Mark the source of truth for each value (owner vs editor). Keep ownership in the current owner.
2) Extract the new view with immutable inputs for display-only data.
3) Pass editable values via `@Binding` and events via callbacks.
4) Preserve list identity by passing stable IDs (do not swap to indices).
5) Keep async work in the same lifecycle hook (`.task`, `.onChange`) unless you are intentionally relocating it.
6) Re-evaluate invariants after extraction: identity, ownership, navigation source, async lifecycle.

**Verify**
- Behavior baseline still matches (same visuals, same interactions).
- Invariants remain true (identity, ownership, navigation, async).
- Data flow is still down, events up (no child mutation of parent state).

**Risk cues**
- State ownership moves to the new child view.
- `ForEach` identity changes or becomes index-based.
- Async work moves from `.task`/`.onChange` to `body`.

## Playbook: Navigation migration to NavigationStack

**Goal**
Migrate legacy navigation APIs to `NavigationStack` while keeping a single navigation source of truth.

**Pre-checks**
- Capture navigation baseline (start screen, push/pop behavior, deep-link entry if present).
- Identify the current navigation owner (root view or shared model).
- Review [NavigationStack guidance](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/engine_reference/godot/modules/navigation.md) and Invariants.

**Steps**
1) Define a route enum or path model that represents current destinations.
2) Create a single `NavigationStack` at the flow root with a single path source of truth.
3) Replace legacy links with `NavigationLink(value:)` and add `navigationDestination(for:)`.
4) Keep navigation state in one place (root view or shared model) and pass bindings down.
5) Preserve existing presentation behavior for sheets and full-screen covers.
6) Re-check invariants: single navigation source of truth, stable identity, state ownership.

**Verify**
- Navigation baseline unchanged (push, back, restore, modal presentation).
- Invariants hold for navigation source and data flow.
- State updates still drive navigation correctly (no duplicated path state).

**Risk cues**
- Multiple `NavigationStack` instances in the same flow.
- Path state duplicated across views.
- Navigation state stored in both view state and shared model.

## Playbook: State hoisting

**Goal**
Move state up the hierarchy without breaking bindings, updates, or async work.

**Pre-checks**
- Capture behavior baseline (what changes when state updates).
- Identify the current owner and consumers using [State ownership](../../../vault/archives/archive_legacy/claude-scientific-skills/scientific-skills/markdown-mermaid-writing/references/diagrams/state.md).
- Review [View composition](view-composition.md) for data flow rules.

**Steps**
1) Choose the new owner based on lifetime and sharing needs (parent or shared model).
2) Move the source of truth to the new owner; keep the previous view as an editor via `@Binding`.
3) Update child inputs to use bindings or immutable values (no duplicated state).
4) Keep async work tied to the view that still owns the lifecycle or to the new owner if its lifetime changed.
5) Verify identity and navigation invariants remain intact after moving state.

**Verify**
- Behavior baseline unchanged (updates propagate, UI stays in sync).
- Invariants hold for ownership and data flow.
- Async work still cancels and restarts correctly when inputs change.

**Risk cues**
- Multiple sources of truth emerge (old and new owners both mutate state).
- Bindings no longer update the UI or update the wrong instance.
- Async work no longer tied to the correct lifecycle owner.

## Related references

- `workflows-refactor.md` for invariants and refactor checklist.
- `state.md` for ownership and wrapper selection.
- `navigation.md` for NavigationStack patterns and migration details.
- `view-composition.md` for extraction and data flow patterns.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/scrolling.md`
```markdown
# Scrolling and Pagination (SwiftUI)

## Overview
Use `List` for standard row-based content with selection, swipe actions, and built-in behavior.
Use `ScrollView` when you need custom layouts or non-list composition.
Use `ScrollViewReader` only when you must programmatically scroll to a specific item.

## Decision Tree

Start here:

1) Do you need row features (selection, swipe actions, edit mode, separators)?
- Yes -> Use `List`
- No -> Continue

2) Do you need custom layout (grids, mixed sections, cards, horizontal + vertical stacks)?
- Yes -> Use `ScrollView` with `LazyVStack`/`LazyHStack`
- No -> Continue

3) Do you need to programmatically scroll to an item or anchor?
- Yes -> Wrap in `ScrollViewReader`
- No -> Use `ScrollView` or `List` based on layout needs

## Safe Pagination Triggers

### Preferred: Sentinel Row
Add a dedicated footer row that appears after the list and triggers loading.

```swift
List {
    ForEach(items) { item in
        Row(item)
    }

    if hasMore {
        ProgressView()
            .frame(maxWidth: .infinity)
            .task {
                await loadNextPageIfNeeded()
            }
    }
}
```

### Alternate: Last-Item Appearance
Trigger when the last item appears, but guard against rapid re-entry.

```swift
ForEach(items) { item in
    Row(item)
        .onAppear {
            if item.id == items.last?.id {
                Task { await loadNextPageIfNeeded() }
            }
        }
}
```

### Guard Conditions (Avoid Duplicate Loads)
Always gate loading with explicit state:

- `isLoading == false`
- `hasMore == true`
- Track the last requested page or cursor

```swift
@MainActor
func loadNextPageIfNeeded() async {
    guard !isLoading, hasMore else { return }
    isLoading = true
    defer { isLoading = false }

    do {
        let page = try await fetchPage(cursor: nextCursor)
        items.append(contentsOf: page.items)
        nextCursor = page.nextCursor
        hasMore = page.hasMore
    } catch is CancellationError {
        return
    } catch {
        errorMessage = error.localizedDescription
    }
}
```

### Prefer `.task(id:)` for Filtered Loads
When pagination depends on a filter or identifier, reset and reload using `.task(id:)`.

```swift
.task(id: filter) {
    resetPagination()
    await loadNextPageIfNeeded()
}
```

## Common Pitfalls

- Side effects inside row `body` cause repeated work on every update.
- `onAppear` triggers multiple times during fast scrolling; guard with loading state.
- Starting work in `.onAppear` without cancellation can lead to overlapping loads.
- Geometry-based scroll offset triggers are noisy; prefer sentinel rows for stability.

## Notes on Async Pagination
Use cancellation-aware `.task` patterns for pagination work.
See `references/concurrency.md` for SwiftUI lifecycle and cancellation guidance.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/state.md`
```markdown
# State Ownership

Use ownership to choose the right property wrapper. Keep a single source of truth and pass state down through bindings or immutable values.

## Decision Tree

1. Does this view own the value and it can reset when the view goes away?
   - Yes: use `@State`.
2. Does a parent own the value and this view only edits it?
   - Yes: use `@Binding`.
3. Is this value shared across many views or the app lifecycle?
   - Yes: inject through `@Environment` or a shared model in the environment.
4. Is this a reference-type model with derived state and logic?
   - iOS 17+: prefer `@Observable` models.
   - Earlier OS support: use `ObservableObject` with `@StateObject` (owner) or `@ObservedObject` (observer).

## Wrapper Cheatsheet

- `@State`: view-owned, ephemeral value types.
- `@Binding`: child edits parent-owned state.
- `@Environment`: shared values supplied by the system or the app.
- `@Observable`: modern reference models (iOS 17+).
- `ObservableObject`: compatibility fallback for earlier OSes.

## Ownership Rules

- One owner, many readers. Avoid duplicate sources of truth.
- If a child edits a value, pass a `Binding` instead of copying.
- Keep shared models in the environment when many views need access.
- Hoist state up only when multiple siblings need it; otherwise keep it local.

## Examples

### Parent owns, child edits
```swift
struct ParentView: View {
    @State private var count = 0

    var body: some View {
        CounterView(count: $count)
    }
}

struct CounterView: View {
    @Binding var count: Int

    var body: some View {
        Button("Count: \(count)") { count += 1 }
    }
}
```

### Shared model in environment
```swift
@Observable
final class SessionModel {
    var isSignedIn = false
}

struct RootView: View {
    @State private var session = SessionModel()

    var body: some View {
        ContentView()
            .environment(session)
    }
}
```

## Observation Notes

- `@Observable` is preferred for new code on iOS 17+.
- For earlier OS support, use `ObservableObject` with `@StateObject` or `@ObservedObject`.
- `@Observable` models that mutate UI-facing state may need `@MainActor` depending on project isolation.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/testing-di.md`
```markdown
# Testing and DI (SwiftUI)

Lightweight seams reduce refactor risk without introducing new tools or architecture mandates.

## Refactor safety seams

Use small, targeted seams to keep behavior stable while changing code.

- **Protocol abstraction:** define a protocol for external dependencies (network, storage, time).
- **Initializer injection with defaults:** inject dependencies, but provide a production default.
- **Closure-based seams:** inject a function for small, single-use dependencies.

```swift
protocol UserServiceProtocol {
    func fetchUser(id: String) async throws -> User
}

final class UserStore {
    private let userService: UserServiceProtocol

    init(userService: UserServiceProtocol = LiveUserService()) {
        self.userService = userService
    }
}
```

## Test doubles quick guide

- **Stub:** returns canned data (queries).
- **Mock:** verifies interactions (commands).
- **Spy:** records calls for later assertions.
- **Fake:** working in-memory implementation.

Minimal example (stub):
```swift
struct StubUserService: UserServiceProtocol {
    var result: Result<User, Error>

    func fetchUser(id: String) async throws -> User {
        try result.get()
    }
}
```

If tests exist, XCTest is the default baseline. Avoid adding new frameworks unless the project already uses them.

## When to add seams

Add seams before refactors that change:

- State ownership between views or wrappers.
- Navigation structure or destinations.
- Side-effect boundaries (networking, storage, analytics).

For refactor steps and invariants, see `references/workflows-refactor.md`.

## Optional tools

Third-party view inspection libraries (for example, ViewInspector) can be useful but are optional and not required.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/view-composition.md`
```markdown
# View Composition

Extract views to improve readability without breaking identity or state ownership. Data flows down, events flow up.

## Safe Extraction Patterns

- Keep state in the view that owns the lifetime.
- Pass immutable values for display-only content.
- Use `@Binding` for edit flows.
- Use callbacks for events (tap, submit, delete).

## Parent/Child Data Flow

- **Display-only:** pass values as plain properties.
- **Editable:** pass a `Binding`.
- **Actions:** pass closures for intent events.

## Smells and Fixes

- **Smell:** Child view owns state that should be shared.
  - **Fix:** Hoist state to the parent and pass a `Binding`.
- **Smell:** Multiple siblings compute the same derived value.
  - **Fix:** Compute once in the parent and pass the result.
- **Smell:** Child mutates parent state by reaching into environment or global state.
  - **Fix:** Pass explicit bindings or callbacks.

## Bad -> Better

### Mutating shared state in the child
```swift
// Bad: child owns shared state
struct ToggleRow: View {
    @State private var isOn = false
    var body: some View { Toggle("Enabled", isOn: $isOn) }
}

// Better: parent owns, child edits
struct ToggleRow: View {
    @Binding var isOn: Bool
    var body: some View { Toggle("Enabled", isOn: $isOn) }
}
```

### Overloading a child with business logic
```swift
// Bad: child decides deletion rules
struct Row: View {
    let item: Item
    var body: some View {
        Button("Delete") { item.deleteIfAllowed() }
    }
}

// Better: child exposes intent, parent decides
struct Row: View {
    let item: Item
    let onDelete: () -> Void

    var body: some View {
        Button("Delete", action: onDelete)
    }
}
```

## Where State Should Live

- **Local state:** view-specific toggles, text input, transient UI.
- **Hoisted state:** values shared across multiple siblings.
- **Shared state:** environment-injected models used across screens.

## Invariants

- Stable IDs stay stable across updates.
- State ownership stays with the correct view.
- Navigation state remains the source of truth.
- Async work remains cancellable and tied to view lifecycle.

## Layout Guidance

Keep layout rules simple and predictable. Let containers do the work.

### Stacks and Spacing

- Use `HStack`, `VStack`, and `ZStack` to express hierarchy.
- Prefer `spacing` on stacks over per-view padding when you need consistent gaps.
- Use `Spacer()` to distribute space and avoid hard-coded offsets.

### Alignment

- Use stack `alignment` for consistent edge alignment.
- Prefer `alignmentGuide` only when you need custom alignment behavior.

### Adaptive Layout

- Use size classes or `ViewThatFits` to adapt layout without branching the entire view.
- Keep layout resilient by avoiding fixed widths/heights when content can grow.
- For complex custom layout, consider the `Layout` protocol to centralize measurement and placement.
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/workflows-refactor.md`
```markdown
# Refactor Workflow (SwiftUI)

Use this workflow when the user asks to change code while preserving existing behavior.

**Constraints:** See [SKILL.md Constraints](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#constraints).

## Invariants

These must hold when refactoring:

- **Stable identity:** Use stable IDs for `List`/`ForEach`. No `.indices` for dynamic data.
- **State ownership:** `@State` = view-local, `@Binding` = parent-owned, `@Observable` = shared.
- **Single navigation source:** One `NavigationStack` root, one path source of truth.
- **Cancellable async:** Tie async work to view lifecycle with `.task`.
- **Unidirectional flow:** Data down, events up. No child mutation of parent state.

## Playbooks

Use the playbooks when you need step-by-step guidance for behavior-preserving refactors:

- View extraction (preserve state ownership, stable identity, data flow)
- Navigation migration to `NavigationStack` with a single source of truth
- State hoisting without breaking bindings or async work

See [Refactor playbooks](refactor-playbooks.md).

## Behavior-Preserving Refactor Checklist

### Pre-checks

- Confirm the request is a refactor (code changes, behavior preserved)
- Capture the current behavior that must remain unchanged
- Identify the files and views in scope
- Map the Invariants above to the code being changed

### Changes

- Preserve stable identity for lists and `ForEach` content
- Keep state ownership mapping consistent (`@State`, `@Binding`, `@Observable`)
- Maintain a single navigation source of truth (one root/path)
- Keep data flowing down and events flowing up
- Ensure async work remains cancellable and tied to view lifecycle
- Avoid introducing architecture mandates or tool-specific steps

### Verification

- Re-check invariants after changes
- Confirm behavior matches the captured baseline
- If tests exist, ensure they still pass

## Risk Cues (Split Refactor or Add Tests First)

If any of these are present, split the refactor or ask for tests before proceeding:

- No tests protect the behavior being refactored
- State ownership shifts between views or wrappers
- Navigation path or root changes are required
- List identity or ordering is being changed
- Async work is moved, duplicated, or detached
- Refactor spans multiple screens or shared components
```

## File: `efremidze-swift-patterns-skill-2e9b66b/swift-patterns/references/workflows-review.md`
```markdown
# Review Workflow (SwiftUI)

Use this workflow when the user asks for findings, risks, or assessment without code changes.

**Constraints:** See [SKILL.md Constraints](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#constraints).

For refactor invariants, see [workflows-refactor.md](workflows-refactor.md#invariants).

## Scope and Inputs

Record the scope and inputs before reviewing:

- Files and components reviewed
- Requirements or expected behaviors
- Platform constraints (iOS version, feature flags, availability)

## Findings Taxonomy

Classify findings consistently so review output is stable and comparable:

- **Correctness:** Behavior mismatches, edge cases, crashes, or broken flows
- **Data flow:** Ownership, bindings, and unidirectional flow violations
- **Navigation:** Competing sources of truth, path mismatches, or route handling gaps
- **Identity:** Unstable list identity, incorrect `id:` usage, state loss
- **Performance:** Unnecessary recomputation, heavy work in body, missing lazy containers
- **Accessibility (when required or requested):** Missing labels, contrast, or focus issues

## Review Checklist

See the detailed Review Checklist in [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#review-checklist).

## Risk Cues (Ask for Tests or Split Work)

Escalate when you see any of these signals:

- No tests cover the behavior being reviewed or changed soon after
- State ownership is changing or being inferred during review
- Navigation path state appears in multiple places or is being redefined
- List identity changes could reset selection or row state
- Async work was moved or detached from view lifecycle
- Refactor scope touches multiple screens or core flows without verification
```

## File: `swift-patterns/SKILL.md`
```markdown
---
name: swift-patterns
description: Review, refactor, or build SwiftUI features with correct state management, modern API usage, optimal view composition, navigation patterns, performance optimization, and testing best practices.
---

# swift-patterns

Review, refactor, or build SwiftUI features with correct state management, modern API usage, optimal view composition, and performance-conscious patterns. Prioritize native APIs, Apple design guidance, and testable code structure. This skill focuses on facts and best practices without enforcing specific architectural patterns.

## Workflow Decision Tree

### 1) Review existing SwiftUI code
→ Read `references/workflows-review.md` for review methodology
- Check state management against property wrapper selection (see `references/state.md`)
- Verify view composition and extraction patterns (see `references/view-composition.md`)
- Audit list performance and identity stability (see `references/lists-collections.md`)
- Validate modern API usage (see `references/modern-swiftui-apis.md`)
- Check async work patterns with .task (see `references/concurrency.md`)
- Verify navigation implementation (see `references/navigation.md`)
- Use Review Response Template (below)

### 2) Refactor existing SwiftUI code
→ Read `references/workflows-refactor.md` for refactor methodology
- Extract complex views using playbooks (see `references/refactor-playbooks.md`)
- Migrate deprecated APIs to modern equivalents (see `references/modern-swiftui-apis.md`)
- Optimize performance hot paths (see `references/performance.md`)
- Restructure state ownership (see `references/state.md`)
- Apply common patterns (see `references/patterns.md`)
- Use Refactor Response Template (below)

### 3) Implement new SwiftUI features
- Design data flow first: identify owned vs injected state (see `references/state.md`)
- Structure views for optimal composition (see `references/view-composition.md`)
- Use modern APIs only (see `references/modern-swiftui-apis.md`)
- Handle async work with .task modifier (see `references/concurrency.md`)
- Apply performance patterns early (see `references/performance.md`)
- Implement navigation flows (see `references/navigation.md`)

### 4) Answer best practice questions
- Load relevant reference file(s) based on topic (see Reference Files below)
- Provide direct guidance with examples

**If intent unclear, ask:** "Do you want findings only (review), or should I change the code (refactor)?"

## Response Templates

**Review Response:**
1. **Scope** - What was reviewed
2. **Findings** - Grouped by severity with actionable statements
3. **Evidence** - File paths or code locations
4. **Risks and tradeoffs** - What could break or needs attention
5. **Next steps** - What to fix first or verify

**Refactor Response:**
1. **Intent + scope** - What is being changed and why
2. **Changes** - Bulleted list with file paths
3. **Behavior preservation** - What should remain unchanged
4. **Next steps** - Tests or verification needed

## Quick Reference: Property Wrapper Selection

| Wrapper | Use When | Ownership |
|---------|----------|-----------|
| `@State` | Internal view state (value type or `@Observable` class) | View owns |
| `@Binding` | Child needs to modify parent's state | Parent owns |
| `@Bindable` | Injected `@Observable` object needing bindings | Injected |
| `let` | Read-only value from parent | Injected |
| `var` + `.onChange()` | Read-only value needing reactive updates | Injected |

**Key rules:**
- Always mark `@State` as `private` (makes ownership explicit)
- Never use `@State` for passed values (accepts initial value only)
- Use `@State` with `@Observable` classes (not `@StateObject`)

See `references/state.md` for detailed guidance and tradeoffs.

## Quick Reference: Modern API Replacements

| Deprecated | Modern Alternative | Notes |
|------------|-------------------|-------|
| `foregroundColor()` | `foregroundStyle()` | Supports dynamic type |
| `cornerRadius()` | `.clipShape(.rect(cornerRadius:))` | More flexible |
| `NavigationView` | `NavigationStack` | Type-safe navigation |
| `tabItem()` | `Tab` API | iOS 18+ |
| `onTapGesture()` | `Button` | Unless need location/count |
| `onChange(of:) { value in }` | `onChange(of:) { old, new in }` or `onChange(of:) { }` | Two or zero parameters |
| `UIScreen.main.bounds` | `GeometryReader` or layout APIs | Avoid hard-coded sizes |

See `references/modern-swiftui-apis.md` for complete migration guide.

## Review Checklist

Use this when reviewing SwiftUI code:

### State Management
- [ ] `@State` properties marked `private`
- [ ] Passed values NOT declared as `@State` or `@StateObject`
- [ ] `@Binding` only where child modifies parent state
- [ ] Property wrapper selection follows ownership rules
- [ ] State ownership clear and intentional

### Modern APIs
- [ ] No deprecated modifiers (foregroundColor, cornerRadius, etc.)
- [ ] Using `NavigationStack` instead of `NavigationView`
- [ ] Using `Button` instead of `onTapGesture` when appropriate
- [ ] Using two-parameter or no-parameter `onChange()`

### View Composition
- [ ] Using modifiers over conditionals for state changes (maintains identity)
- [ ] Complex views extracted to separate subviews
- [ ] Views kept small and focused
- [ ] View `body` simple and pure (no side effects)

### Navigation & Sheets
- [ ] Using `navigationDestination(for:)` for type-safe navigation
- [ ] Using `.sheet(item:)` for model-based sheets
- [ ] Sheets own their dismiss actions

### Lists & Collections
- [ ] `ForEach` uses stable identity (never `.indices` for dynamic data)
- [ ] Constant number of views per `ForEach` element
- [ ] No inline filtering in `ForEach` (prefilter and cache)
- [ ] No `AnyView` in list rows

### Performance
- [ ] Passing only needed values to views (not large config objects)
- [ ] Eliminating unnecessary dependencies
- [ ] Checking value changes before state assignment in hot paths
- [ ] Using `LazyVStack`/`LazyHStack` for large lists
- [ ] No object creation in view `body`

### Async Work
- [ ] Using `.task` for automatic cancellation
- [ ] Using `.task(id:)` for value-dependent tasks
- [ ] Not mixing `.onAppear` with async work

See reference files for detailed explanations of each item.

## Constraints

- **Swift/SwiftUI focus only** - Exclude server-side Swift and UIKit unless bridging required
- **No Swift concurrency patterns** - Use `.task` for SwiftUI async work
- **No architecture mandates** - Don't require MVVM/MVC/VIPER or specific structures
- **No formatting/linting rules** - Focus on correctness and patterns
- **No tool-specific guidance** - No Xcode, Instruments, or IDE instructions
- **Citations allowed:** `developer.apple.com/documentation/swiftui/`, `developer.apple.com/documentation/swift/`

All workflows must follow these constraints.

## Philosophy

This skill focuses on **facts and best practices** from Apple's documentation:
- Modern APIs over deprecated ones
- Clear state ownership patterns
- Performance-conscious view composition
- Testable code structure
- No architectural mandates (MVVM/VIPER not required)
- Apple Human Interface Guidelines adherence

## Reference Files

All references in `references/`:
- `workflows-review.md` - Review methodology and findings taxonomy
- `workflows-refactor.md` - Refactor methodology and invariants
- `refactor-playbooks.md` - Step-by-step refactor guides
- `state.md` - Property wrappers and ownership patterns
- `navigation.md` - Navigation implementation patterns
- `view-composition.md` - View structure and extraction
- `lists-collections.md` - Identity and ForEach patterns
- `scrolling.md` - Scroll handling and pagination
- `concurrency.md` - Async work with .task
- `performance.md` - Optimization strategies
- `testing-di.md` - Testing and dependency injection
- `patterns.md` - Common SwiftUI patterns
- `modern-swiftui-apis.md` - Legacy API migration
- `code-review-refactoring.md` - Code quality checks
```

## File: `swift-patterns/references/code-review-refactoring.md`
```markdown
# Code Smells & Anti-Patterns (SwiftUI)

Common issues to look for when reviewing or refactoring SwiftUI code.

## SwiftUI Code Smells

- **Duplicate source of truth:** `@State` and model both hold the same value.
- **Stored derived state:** Computing and storing values that could be computed properties.
- **Side effects in body:** Mutations or async work triggered during view rendering.
- **Unstable list identity:** Using `.indices` or non-unique IDs for dynamic `ForEach`.
- **Competing navigation sources:** Multiple `NavigationStack` roots or duplicated path state.
- **Heavy work in body:** Formatters, parsing, or sorting recreated every render.
- **Silent error handling:** Swallowing errors without user feedback.

## Examples

### Duplicate Source of Truth
```swift
// Bad: state duplicated
struct PlayerView: View {
    @State private var isPlaying = false
    let model: PlayerModel

    var body: some View {
        Toggle("Playing", isOn: $isPlaying)
            .onChange(of: isPlaying) { model.isPlaying = $0 }
    }
}

// Good: single source of truth
struct PlayerView: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Toggle("Playing", isOn: $isPlaying)
    }
}
```

### Unstable List Identity
```swift
// Bad: indices shift on insert/delete
ForEach(items.indices, id: \.self) { index in
    RowView(item: items[index])
}

// Good: stable identity from model
ForEach(items, id: \.id) { item in
    RowView(item: item)
}
```

### Stored Derived State
```swift
// Bad: derived value stored and manually synced
struct CheckoutView: View {
    let subtotal: Decimal
    @State private var total: Decimal = 0

    var body: some View {
        Text("Total: \(total)")
            .onAppear { total = subtotal * 1.08 }
    }
}

// Good: compute directly
struct CheckoutView: View {
    let subtotal: Decimal
    var total: Decimal { subtotal * 1.08 }

    var body: some View {
        Text("Total: \(total)")
    }
}
```

## Anti-Patterns

- Global mutable state accessed by multiple views without clear ownership.
- Navigation driven by both view state and model state (competing sources).
- Copying view state into models without ownership boundaries.
- Silent error handling that hides failures from users.
- Over-abstraction that reduces testability without clear benefit.
```

## File: `swift-patterns/references/concurrency.md`
```markdown
# SwiftUI Concurrency (Lifecycle-Scoped)

## Overview
This reference focuses on SwiftUI-friendly async patterns: `.task`, `.task(id:)`, cancellation checks, and safe UI updates with `@MainActor`.
It intentionally avoids deep concurrency patterns and architecture mandates.

## Decision Tree: `.task` vs `.onAppear` vs `.onChange`

1) Do you need async work tied to the view lifecycle?
- Yes -> Use `.task`

2) Does the async work depend on a changing identifier or filter?
- Yes -> Use `.task(id:)` to auto-cancel and restart when the value changes

3) Do you need to react to a value change (possibly multiple times)?
- Yes -> Use `.onChange` and start async work inside a `Task`

4) Do you only need lightweight, non-async setup when a view appears?
- Yes -> Use `.onAppear` with a guard to avoid duplicate work

## Core Patterns

### Basic `.task` for View-Scoped Loading
```swift
struct DetailView: View {
    @State private var item: Item?

    var body: some View {
        Group {
            if let item {
                Text(item.title)
            } else {
                ProgressView()
            }
        }
        .task {
            await loadItem()
        }
    }

    @MainActor
    private func loadItem() async {
        item = await fetchItem()
    }
}
```

### `.task(id:)` for ID-Driven Reloads
```swift
struct FilteredList: View {
    @State private var items: [Item] = []
    let filter: Filter

    var body: some View {
        List(items) { item in
            Text(item.title)
        }
        .task(id: filter) {
            await load(filter: filter)
        }
    }

    @MainActor
    private func load(filter: Filter) async {
        items = await fetchItems(filter: filter)
    }
}
```

### `.onChange` for Value-Driven Async Work
```swift
.onChange(of: query) { _, newValue in
    Task {
        await performSearch(query: newValue)
    }
}
```

## Cancellation Awareness
SwiftUI cancels `.task` when the view disappears or the id changes. Long-running work should check cancellation.

```swift
func loadPages() async throws {
    for page in pages {
        try Task.checkCancellation()
        try await fetchPage(page)
    }
}
```

## `@MainActor` for UI Updates
Update UI state on the main actor.

- Use `@MainActor` on functions that mutate view state.
- If your project uses default actor isolation, explicit `@MainActor` may not be required.

```swift
@MainActor
func updateState(with items: [Item]) {
    self.items = items
}
```

## Common Pitfalls

- Starting async work in `body` causes repeated execution on every render.
- Using `.onAppear` for network loads without guards leads to duplicate requests.
- Ignoring cancellation can result in stale or out-of-order UI updates.
- Updating UI state off the main actor can cause crashes or warnings.
```

## File: `swift-patterns/references/lists-collections.md`
```markdown
# Lists and Collections

Use stable identity and lazy containers to keep lists correct and performant.

## Stable Identity

- Prefer `Identifiable` models for lists and `ForEach`.
- If not `Identifiable`, provide a stable `id:`.
- Avoid `.indices` for dynamic data; indices shift on insert/delete and break identity.

```swift
struct Item: Identifiable {
    let id: UUID
    let title: String
}

List(items) { item in
    Text(item.title)
}
```

## List vs ScrollView + LazyVStack

- Use `List` for standard scrolling, selection, swipe actions, and system row behavior.
- Use `ScrollView` + `LazyVStack` for fully custom layouts or mixed content.
- For large collections, prefer lazy containers (`List`, `LazyVStack`, `LazyVGrid`).

## Sections and Empty States

- Group related rows into `Section` for clarity.
- Provide explicit empty states when the collection is empty.

```swift
if items.isEmpty {
    ContentUnavailableView("No Items", systemImage: "tray")
} else {
    List {
        Section("Recent") {
            ForEach(items) { item in
                Row(item: item)
            }
        }
    }
}
```

## Row Composition

- Keep row views lightweight and pure.
- Move heavy work (formatting, image decoding) out of row `body` when it can be cached.
- Pass values into rows; avoid side effects inside the row body.

## Common Pitfalls

- **Identity churn:** using unstable IDs causes rows to show the wrong data.
- **Row-level side effects:** triggers repeat work during scrolling.
- **Too much per-row state:** pushes state ownership into the wrong place.
```

## File: `swift-patterns/references/modern-swiftui-apis.md`
```markdown
# Modern SwiftUI API Replacements

Prefer modern APIs when the deployment target allows. This catalog covers legacy patterns and their replacements, plus new APIs by iOS version.

## Contents

### Legacy → Modern Migration Tables
- [Navigation](#navigation)
- [Appearance](#appearance)
- [State & Data](#state--data)
- [Events & Lifecycle](#events--lifecycle)
- [Lists & Collections](#lists--collections)
- [Tabs (iOS 18+)](#tabs-ios-18)
- [Layout & Sizing](#layout--sizing)
- [Sheets & Presentation](#sheets--presentation)

### New APIs by Version
- [iOS 17 New APIs](#ios-17-new-apis) - @Observable, ScrollView, Animation, Inspector, Sensory Feedback, Container Relative Frame, onChange initial, Shape Improvements
- [iOS 18 New APIs](#ios-18-new-apis) - @Entry, @Previewable, Tab API, Mesh Gradients, Zoom Transitions, SF Symbol Animations, Custom Container Views, Controls
- [iOS 26 New APIs](#ios-26-new-apis) - Liquid Glass, WebView, Rich Text, Glass Button, Toolbar Spacer, TabView Minimize, Navigation Subtitles, Label Icon Width, Scene Padding, @Animatable, 3D Charts, openURL In-App, Drag Container

### Guidelines
- [Migration Priority](#migration-priority)
- [Availability Patterns](#availability-patterns)

## Navigation

| Legacy | Modern | Notes |
|--------|--------|-------|
| `NavigationView` | `NavigationStack` | Value-based, type-safe navigation |
| `NavigationLink(destination:)` | `NavigationLink(value:)` + `navigationDestination(for:)` | Decouple link from destination |
| `navigationBarTitle(_:)` | `navigationTitle(_:)` | Unified API |
| `navigationBarItems(leading:trailing:)` | `toolbar { ToolbarItem(placement:) }` | Consistent placement |
| `navigationBarHidden(_:)` | `toolbar(.hidden, for: .navigationBar)` | iOS 16+ |
| `.isDetailLink(false)` | Not needed | NavigationStack handles automatically |

## Appearance

| Legacy | Modern | Notes |
|--------|--------|-------|
| `foregroundColor(_:)` | `foregroundStyle(_:)` | Supports gradients, materials |
| `accentColor(_:)` | `tint(_:)` | Per-view accent color |
| `cornerRadius(_:)` | `.clipShape(.rect(cornerRadius:))` | More flexible, selective corners |
| `background(Color.x)` | `background { }` or `.background(.x, in:)` | Shape-aware backgrounds |
| `overlay(Circle())` | `overlay { Circle() }` | ViewBuilder syntax |

## State & Data

| Legacy | Modern | Notes |
|--------|--------|-------|
| `@StateObject` | `@State` with `@Observable` | Simpler, no wrapper needed |
| `@ObservedObject` | Direct reference to `@Observable` | Automatic tracking |
| `@EnvironmentObject` | `@Environment(MyType.self)` | Type-safe environment |
| `@Published` | Not needed with `@Observable` | Automatic property tracking |
| `Image("name")` | `Image(.name)` | Type-safe asset references |

## Events & Lifecycle

| Legacy | Modern | Notes |
|--------|--------|-------|
| `onChange(of:) { value in }` | `onChange(of:) { old, new in }` or `onChange(of:) { }` | Two or zero params (iOS 17+) |
| `onAppear { Task { } }` | `.task { }` | Auto-cancellation on disappear |
| `onReceive(publisher)` | `.task` or `.onChange` | When lifecycle-safe |
| `onTapGesture { }` | `Button` | Unless need tap location/count |

## Lists & Collections

| Legacy | Modern | Notes |
|--------|--------|-------|
| Manual pull-to-refresh | `.refreshable { }` | Native refresh control |
| `EditButton()` standalone | `.toolbar { EditButton() }` | Toolbar placement |
| `id: \.self` for value types | Prefer `Identifiable` | Better performance |

## Tabs (iOS 18+)

| Legacy | Modern | Notes |
|--------|--------|-------|
| `TabView { }.tabItem { }` | `TabView { Tab("", systemImage:) { } }` | New Tab API |
| Manual sidebar | `TabViewStyle.sidebarAdaptable` | Adaptive sidebar on iPad |

## Layout & Sizing

| Legacy | Modern | Notes |
|--------|--------|-------|
| `UIScreen.main.bounds` | `GeometryReader` or layout APIs | Avoid hard-coded sizes |
| `GeometryReader` for sizing | `containerRelativeFrame()` | iOS 17+, cleaner |
| `frame(width:height:)` fixed | `frame(minWidth:maxWidth:)` | Flexible sizing |

## Sheets & Presentation

| Legacy | Modern | Notes |
|--------|--------|-------|
| `.sheet(isPresented:)` | `.sheet(item:)` | When driven by model |
| Custom sheet sizing | `presentationDetents([.medium, .large])` | Native detents |
| Dismiss via binding | `@Environment(\.dismiss)` | Cleaner dismiss action |

---

## iOS 17 New APIs

### @Observable Macro
Replaces `ObservableObject` with simpler syntax:
```swift
// iOS 17+
@Observable
class UserModel {
    var name = ""      // Automatically tracked
    var age = 0
}

struct ContentView: View {
    @State private var user = UserModel()  // Use @State, not @StateObject
    var body: some View {
        TextField("Name", text: $user.name)
    }
}
```

### Scroll View Enhancements
```swift
ScrollView {
    content
}
.scrollTargetBehavior(.paging)           // Paging behavior
.scrollPosition(id: $selectedID)          // Programmatic scroll
.scrollTransition { content, phase in     // Scroll-based transitions
    content.opacity(phase.isIdentity ? 1 : 0.5)
}
.defaultScrollAnchor(.bottom)             // Start at bottom
.scrollIndicatorsFlash(trigger: items)    // Flash indicators
```

### Animation Improvements
```swift
// New spring animations
withAnimation(.bouncy) { }
withAnimation(.snappy) { }

// Phase animator for multi-step animations
PhaseAnimator([0, 1, 2]) { phase in
    Circle()
        .scaleEffect(phase == 1 ? 1.5 : 1)
}

// Keyframe animations
KeyframeAnimator(initialValue: AnimationValues()) { value in
    Circle()
        .scaleEffect(value.scale)
        .offset(value.offset)
} keyframes: { _ in
    KeyframeTrack(\.scale) {
        SpringKeyframe(1.5, duration: 0.3)
        SpringKeyframe(1.0, duration: 0.3)
    }
}

// Animation completion
withAnimation(.default) {
    isExpanded.toggle()
} completion: {
    // Animation finished
}
```

### Inspector Modifier
```swift
NavigationStack {
    ContentView()
        .inspector(isPresented: $showInspector) {
            InspectorView()
        }
}
```

### Sensory Feedback
```swift
Button("Tap") { }
    .sensoryFeedback(.impact, trigger: tapCount)

// Conditional feedback
Button("Submit") { }
    .sensoryFeedback(.success, trigger: submitCount) { old, new in
        new > old  // Only when count increases
    }
```

### Container Relative Frame
```swift
Image("photo")
    .containerRelativeFrame(.horizontal) { size, axis in
        size * 0.8  // 80% of container width
    }
```

### onChange with Initial Value
```swift
.onChange(of: searchText, initial: true) { oldValue, newValue in
    // Fires immediately with initial value
}
```

### Shape Improvements
```swift
// Selective corner rounding
RoundedRectangle(cornerRadii: .init(topLeading: 20, bottomTrailing: 20))

// Combined fill and stroke
Circle()
    .stroke(.red, lineWidth: 2)
    .fill(.blue)
```

---

## iOS 18 New APIs

### @Entry Macro for Environment
```swift
// Simplified custom environment values
extension EnvironmentValues {
    @Entry var myCustomValue: String = "default"
}

// Usage
.environment(\.myCustomValue, "custom")
@Environment(\.myCustomValue) var value
```

### @Previewable Macro
```swift
#Preview {
    @Previewable @State var count = 0
    Button("Count: \(count)") { count += 1 }
}
```

### Tab API
```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    Tab("Search", systemImage: "magnifyingglass", role: .search) {
        SearchView()
    }
}
.tabViewStyle(.sidebarAdaptable)  // Sidebar on iPad
```

### Mesh Gradients
```swift
MeshGradient(
    width: 3, height: 3,
    points: [
        [0, 0], [0.5, 0], [1, 0],
        [0, 0.5], [0.5, 0.5], [1, 0.5],
        [0, 1], [0.5, 1], [1, 1]
    ],
    colors: [
        .red, .orange, .yellow,
        .green, .blue, .purple,
        .pink, .cyan, .mint
    ]
)
```

### Zoom Navigation Transition
```swift
NavigationLink(value: item) {
    ItemRow(item: item)
}
.matchedTransitionSource(id: item.id, in: namespace)

// Destination
DetailView(item: item)
    .navigationTransition(.zoom(sourceID: item.id, in: namespace))
```

### SF Symbol Animations
```swift
Image(systemName: "checkmark.circle")
    .symbolEffect(.bounce, value: isComplete)
    .symbolEffect(.rotate, value: isLoading)
```

### Custom Container Views
```swift
struct CardStack<Content: View>: View {
    @ViewBuilder var content: Content

    var body: some View {
        ForEach(subviews: content) { subview in
            subview
                .padding()
                .background(.ultraThinMaterial)
        }
    }
}
```

### Controls for Lock Screen / Control Center
```swift
struct MyControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(kind: "MyControl") {
            ControlWidgetButton(action: MyIntent()) {
                Label("Toggle", systemImage: "lightbulb")
            }
        }
    }
}
```

---

## iOS 26 New APIs

### Liquid Glass Design
Automatic with Xcode 26 build. Opt out if needed:
```swift
// Disable Liquid Glass for transition period
.preferredGlassEffect(.disabled)
```

### WebView (Native)
```swift
import WebKit

struct BrowserView: View {
    @State private var page = WebPage()

    var body: some View {
        WebView(page)
            .onAppear {
                page.load(URLRequest(url: URL(string: "https://apple.com")!))
            }
    }
}
```

### Rich Text Editing with AttributedString
```swift
struct RichTextEditor: View {
    @State private var text = AttributedString("Hello")

    var body: some View {
        TextEditor(text: $text)
            .toolbar {
                Button("Bold") {
                    text.font = .boldSystemFont(ofSize: 17)
                }
            }
    }
}
```

### Glass Button Style
```swift
Button("Action") { }
    .buttonStyle(.glass)
```

### Toolbar Spacer
```swift
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        Button("Save") { }
    }
    ToolbarSpacer(.fixed)
    ToolbarItem(placement: .primaryAction) {
        Button("Share") { }
    }
}
```

### TabView Minimize on Scroll
```swift
TabView {
    Tab("Home", systemImage: "house") {
        ScrollView {
            // Content
        }
    }
}
.tabBarMinimizeBehavior(.automatic)
```

### Navigation Subtitles
```swift
.navigationTitle("Documents")
.navigationSubtitle("23 items")
```

### Label Icon Fixed Width
```swift
Label("Settings", systemImage: "gear")
    .labelIconFixedWidth()
```

### Scene Padding
```swift
VStack {
    content
}
.scenePadding()  // Automatic padding for scene context
```

### @Animatable Macro
```swift
@Animatable
struct PulsingCircle: View {
    var scale: Double

    var body: some View {
        Circle()
            .scaleEffect(scale)
    }
}
```

### 3D Charts
```swift
Chart3D {
    ForEach(data) { item in
        BarMark3D(
            x: .value("X", item.x),
            y: .value("Y", item.y),
            z: .value("Z", item.z)
        )
    }
}
```

### openURL In-App Browser
```swift
@Environment(\.openURL) var openURL

Button("Open Link") {
    openURL(url, prefersInApp: true)  // Opens in-app browser
}
```

### Drag Container
```swift
List(selection: $selection) {
    ForEach(items) { item in
        ItemRow(item: item)
    }
}
.dragContainer(for: selection) { items in
    // Return drag preview
}
```

---

## Migration Priority

1. **High:** NavigationView → NavigationStack (architecture impact)
2. **High:** ObservableObject → @Observable (iOS 17+)
3. **High:** TabView tabItem → Tab API (iOS 18+)
4. **Medium:** foregroundColor → foregroundStyle
5. **Medium:** onChange single-param → two-param
6. **Medium:** @EnvironmentObject → @Environment
7. **Low:** cornerRadius → clipShape (visual only)

## Availability Patterns

```swift
// Feature check
if #available(iOS 17, *) {
    ContentView()
        .containerRelativeFrame(.horizontal)
} else {
    GeometryReader { geo in
        ContentView()
            .frame(width: geo.size.width * 0.8)
    }
}

// View modifier extension for compatibility
extension View {
    @ViewBuilder
    func iOS17ContainerFrame() -> some View {
        if #available(iOS 17, *) {
            self.containerRelativeFrame(.horizontal)
        } else {
            self
        }
    }
}
```

Sources: [Hacking with Swift - iOS 17](https://www.hackingwithswift.com/articles/260/whats-new-in-swiftui-for-ios-17), [Hacking with Swift - iOS 18](https://www.hackingwithswift.com/articles/270/whats-new-in-swiftui-for-ios-18), [Hacking with Swift - iOS 26](https://www.hackingwithswift.com/articles/278/whats-new-in-swiftui-for-ios-26), [Swift with Majid - WWDC25](https://swiftwithmajid.com/2025/06/10/what-is-new-in-swiftui-after-wwdc25/)
```

## File: `swift-patterns/references/navigation.md`
```markdown
# NavigationStack Guidance

Use value-based navigation with a single source of truth. Keep navigation state in one place without mandating a coordinator pattern.

## Core Patterns

- Prefer `NavigationStack` over legacy navigation APIs.
- Use `NavigationLink(value:)` with `navigationDestination(for:)`.
- Keep navigation state in one owner (root view, feature root, or environment model).
- Avoid nested `NavigationStack` instances in the same flow.

## Basic Structure

```swift
enum Route: Hashable {
    case detail(Item.ID)
}

struct RootView: View {
    @State private var path: [Route] = []

    var body: some View {
        NavigationStack(path: $path) {
            List(items) { item in
                NavigationLink(value: Route.detail(item.id)) {
                    Text(item.title)
                }
            }
            .navigationDestination(for: Route.self) { route in
                switch route {
                case .detail(let id):
                    DetailView(id: id)
                }
            }
        }
    }
}
```

## Navigation State Ownership

- Use `@State` for simple paths local to a flow.
- For shared navigation state, store the path in a shared model injected through the environment.
- Keep programmatic navigation scoped to a single owner to avoid conflicting updates.

## Sheets and Full-Screen Presentation

- Use `sheet(item:)` when a selection drives presentation.
- Use `sheet(isPresented:)` for simple toggles.
- Use `fullScreenCover` for full-screen flows.
- Dismiss with `@Environment(\.dismiss)` from within the presented view.

```swift
struct ContentView: View {
    @State private var selectedItem: Item?

    var body: some View {
        List(items) { item in
            Button(item.title) { selectedItem = item }
        }
        .sheet(item: $selectedItem) { item in
            DetailSheet(item: item)
        }
    }
}

struct DetailSheet: View {
    let item: Item
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            DetailView(id: item.id)
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) {
                        Button("Close") { dismiss() }
                    }
                }
        }
    }
}
```

## Avoid These Patterns

- Nested `NavigationStack` inside a view that is already in a stack.
- Mixing `NavigationView` and `NavigationStack` in the same flow.
- Scattering navigation state across multiple views.

## Consider When Needed (Optional)

- Use `NavigationPath` for dynamic, multi-type navigation stacks.
- Consider deep-link parsing and path restoration only when the product needs it.

## Modern Replacements

For legacy navigation API replacements, see `references/modern-swiftui-apis.md`.
```

## File: `swift-patterns/references/patterns.md`
```markdown
# Reusable SwiftUI Patterns

Building blocks for common SwiftUI scenarios. Use these patterns as starting points, not rigid templates.

## Container Views

Wrap content with loading/error states to avoid repeating conditional logic.

```swift
struct AsyncContentView<Content: View>: View {
    let isLoading: Bool
    let error: Error?
    @ViewBuilder let content: () -> Content
    let retry: () -> Void

    var body: some View {
        if isLoading {
            ProgressView()
        } else if let error {
            ContentUnavailableView {
                Label("Error", systemImage: "exclamationmark.triangle")
            } description: {
                Text(error.localizedDescription)
            } actions: {
                Button("Retry", action: retry)
            }
        } else {
            content()
        }
    }
}

// Usage
AsyncContentView(
    isLoading: viewModel.isLoading,
    error: viewModel.error,
    content: { UserList(users: viewModel.users) },
    retry: { Task { await viewModel.load() } }
)
```

## ViewModifiers for Reusable Styling

Extract repeated styling into modifiers instead of copying view code.

```swift
struct CardStyle: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color(.systemBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .shadow(color: .black.opacity(0.1), radius: 5, y: 2)
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardStyle())
    }
}

// Usage
Text("Hello").cardStyle()
```

## Environment-Based Dependency Injection

Use custom environment keys for app-wide dependencies.

```swift
// Define the key
private struct UserServiceKey: EnvironmentKey {
    static let defaultValue: UserServiceProtocol = UserService()
}

extension EnvironmentValues {
    var userService: UserServiceProtocol {
        get { self[UserServiceKey.self] }
        set { self[UserServiceKey.self] = newValue }
    }
}

// Inject at app root
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.userService, UserService())
        }
    }
}

// Use in views
struct ContentView: View {
    @Environment(\.userService) private var userService

    var body: some View {
        Text("Hello")
            .task {
                let users = try? await userService.fetchUsers()
            }
    }
}
```

## PreferenceKeys for Child-to-Parent Communication

Pass values up the view hierarchy when callbacks aren't practical.

```swift
struct ScrollOffsetPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = nextValue()
    }
}

struct ContentView: View {
    @State private var scrollOffset: CGFloat = 0

    var body: some View {
        ScrollView {
            VStack {
                ForEach(0..<50, id: \.self) { i in
                    Text("Item \(i)")
                }
            }
            .background(
                GeometryReader { geometry in
                    Color.clear.preference(
                        key: ScrollOffsetPreferenceKey.self,
                        value: geometry.frame(in: .named("scroll")).minY
                    )
                }
            )
        }
        .coordinateSpace(name: "scroll")
        .onPreferenceChange(ScrollOffsetPreferenceKey.self) { value in
            scrollOffset = value
        }
    }
}
```

## When to Use Each Pattern

- **Container views**: Loading states, error handling, empty states, permission gates
- **ViewModifiers**: Repeated styling, conditional appearance, reusable animations
- **Environment DI**: Services, repositories, feature flags, app-wide configuration
- **PreferenceKeys**: Scroll position, child geometry, aggregating values from children
```

## File: `swift-patterns/references/performance.md`
```markdown
# Performance (SwiftUI)

Use this reference to apply a baseline checklist first, then consider safe, SwiftUI-specific optimizations.

## Performance baseline

Start here before suggesting changes:

- Expensive work in `body` (formatters, parsing, sorting, image decoding).
- Unstable list identity (indices or non-unique IDs) causing row churn.
- Heavy work on the main thread (blocking file/network/JSON work).
- Async work detached from the view lifecycle (duplicate or stale tasks).

If issues persist after baseline fixes, profiling tools like Instruments can help identify hot paths.

## Safe optimizations

Consider these when the baseline checklist points to them:

- **Identity stability:** use stable IDs in `ForEach` and `List`. See `references/lists-collections.md`.
- **Lazy containers:** use `List`, `LazyVStack`, or `LazyVGrid` for long collections. See `references/scrolling.md`.
- **Expensive-work avoidance:** move formatters, parsing, and derived values out of `body` so they are not recreated every render.

## SwiftUI lifecycle for async work

Prefer `.task` to tie async work to view lifecycle, and check cancellation in long-running tasks.
Use `.task(id:)` when work depends on inputs like filters, IDs, or search terms.

## SwiftUI snippets

### Stable identity in `ForEach`
```swift
ForEach(items, id: \.id) { item in
    Row(item: item)
}
```

### Move formatter out of `body`
```swift
private let formatter: DateFormatter = {
    let f = DateFormatter()
    f.dateStyle = .medium
    return f
}()

var body: some View {
    Text(formatter.string(from: date))
}
```

### Tie async work to view lifecycle
```swift
.task(id: userID) {
    try Task.checkCancellation()
    await loadUser(id: userID)
}
```

## Risk cues (split refactors)

If any of these change, split the refactor or add tests first:

- State ownership moves between views or wrappers.
- List identity or ordering changes.
- Async work moves between `body`, `.task`, or other lifecycle hooks.

## Related references

- `references/lists-collections.md` for stable identity guidance.
- `references/scrolling.md` for lazy containers and pagination patterns.
```

## File: `swift-patterns/references/refactor-playbooks.md`
```markdown
# Refactor Playbooks (SwiftUI)

Goal-based playbooks for behavior-preserving refactors. Each playbook starts from a baseline, preserves refactor invariants, and ends with verification against the original behavior.

**Invariants:** See [workflows-refactor.md](workflows-refactor.md#invariants). These are non-negotiables for every step.

## Playbook: View extraction

**Goal**
Extract a view to improve readability while preserving state ownership, stable identity, and data flow.

**Pre-checks**
- Capture the current behavior baseline (visual output, interactions, state changes).
- Identify state owners vs editors using [State ownership](../../../vault/archives/archive_legacy/claude-scientific-skills/scientific-skills/markdown-mermaid-writing/references/diagrams/state.md).
- Map data-flow paths using [View composition](view-composition.md).
- Confirm any list content uses stable identity per Invariants.

**Steps**
1) Mark the source of truth for each value (owner vs editor). Keep ownership in the current owner.
2) Extract the new view with immutable inputs for display-only data.
3) Pass editable values via `@Binding` and events via callbacks.
4) Preserve list identity by passing stable IDs (do not swap to indices).
5) Keep async work in the same lifecycle hook (`.task`, `.onChange`) unless you are intentionally relocating it.
6) Re-evaluate invariants after extraction: identity, ownership, navigation source, async lifecycle.

**Verify**
- Behavior baseline still matches (same visuals, same interactions).
- Invariants remain true (identity, ownership, navigation, async).
- Data flow is still down, events up (no child mutation of parent state).

**Risk cues**
- State ownership moves to the new child view.
- `ForEach` identity changes or becomes index-based.
- Async work moves from `.task`/`.onChange` to `body`.

## Playbook: Navigation migration to NavigationStack

**Goal**
Migrate legacy navigation APIs to `NavigationStack` while keeping a single navigation source of truth.

**Pre-checks**
- Capture navigation baseline (start screen, push/pop behavior, deep-link entry if present).
- Identify the current navigation owner (root view or shared model).
- Review [NavigationStack guidance](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/engine_reference/godot/modules/navigation.md) and Invariants.

**Steps**
1) Define a route enum or path model that represents current destinations.
2) Create a single `NavigationStack` at the flow root with a single path source of truth.
3) Replace legacy links with `NavigationLink(value:)` and add `navigationDestination(for:)`.
4) Keep navigation state in one place (root view or shared model) and pass bindings down.
5) Preserve existing presentation behavior for sheets and full-screen covers.
6) Re-check invariants: single navigation source of truth, stable identity, state ownership.

**Verify**
- Navigation baseline unchanged (push, back, restore, modal presentation).
- Invariants hold for navigation source and data flow.
- State updates still drive navigation correctly (no duplicated path state).

**Risk cues**
- Multiple `NavigationStack` instances in the same flow.
- Path state duplicated across views.
- Navigation state stored in both view state and shared model.

## Playbook: State hoisting

**Goal**
Move state up the hierarchy without breaking bindings, updates, or async work.

**Pre-checks**
- Capture behavior baseline (what changes when state updates).
- Identify the current owner and consumers using [State ownership](../../../vault/archives/archive_legacy/claude-scientific-skills/scientific-skills/markdown-mermaid-writing/references/diagrams/state.md).
- Review [View composition](view-composition.md) for data flow rules.

**Steps**
1) Choose the new owner based on lifetime and sharing needs (parent or shared model).
2) Move the source of truth to the new owner; keep the previous view as an editor via `@Binding`.
3) Update child inputs to use bindings or immutable values (no duplicated state).
4) Keep async work tied to the view that still owns the lifecycle or to the new owner if its lifetime changed.
5) Verify identity and navigation invariants remain intact after moving state.

**Verify**
- Behavior baseline unchanged (updates propagate, UI stays in sync).
- Invariants hold for ownership and data flow.
- Async work still cancels and restarts correctly when inputs change.

**Risk cues**
- Multiple sources of truth emerge (old and new owners both mutate state).
- Bindings no longer update the UI or update the wrong instance.
- Async work no longer tied to the correct lifecycle owner.

## Related references

- `workflows-refactor.md` for invariants and refactor checklist.
- `state.md` for ownership and wrapper selection.
- `navigation.md` for NavigationStack patterns and migration details.
- `view-composition.md` for extraction and data flow patterns.
```

## File: `swift-patterns/references/scrolling.md`
```markdown
# Scrolling and Pagination (SwiftUI)

## Overview
Use `List` for standard row-based content with selection, swipe actions, and built-in behavior.
Use `ScrollView` when you need custom layouts or non-list composition.
Use `ScrollViewReader` only when you must programmatically scroll to a specific item.

## Decision Tree

Start here:

1) Do you need row features (selection, swipe actions, edit mode, separators)?
- Yes -> Use `List`
- No -> Continue

2) Do you need custom layout (grids, mixed sections, cards, horizontal + vertical stacks)?
- Yes -> Use `ScrollView` with `LazyVStack`/`LazyHStack`
- No -> Continue

3) Do you need to programmatically scroll to an item or anchor?
- Yes -> Wrap in `ScrollViewReader`
- No -> Use `ScrollView` or `List` based on layout needs

## Safe Pagination Triggers

### Preferred: Sentinel Row
Add a dedicated footer row that appears after the list and triggers loading.

```swift
List {
    ForEach(items) { item in
        Row(item)
    }

    if hasMore {
        ProgressView()
            .frame(maxWidth: .infinity)
            .task {
                await loadNextPageIfNeeded()
            }
    }
}
```

### Alternate: Last-Item Appearance
Trigger when the last item appears, but guard against rapid re-entry.

```swift
ForEach(items) { item in
    Row(item)
        .onAppear {
            if item.id == items.last?.id {
                Task { await loadNextPageIfNeeded() }
            }
        }
}
```

### Guard Conditions (Avoid Duplicate Loads)
Always gate loading with explicit state:

- `isLoading == false`
- `hasMore == true`
- Track the last requested page or cursor

```swift
@MainActor
func loadNextPageIfNeeded() async {
    guard !isLoading, hasMore else { return }
    isLoading = true
    defer { isLoading = false }

    do {
        let page = try await fetchPage(cursor: nextCursor)
        items.append(contentsOf: page.items)
        nextCursor = page.nextCursor
        hasMore = page.hasMore
    } catch is CancellationError {
        return
    } catch {
        errorMessage = error.localizedDescription
    }
}
```

### Prefer `.task(id:)` for Filtered Loads
When pagination depends on a filter or identifier, reset and reload using `.task(id:)`.

```swift
.task(id: filter) {
    resetPagination()
    await loadNextPageIfNeeded()
}
```

## Common Pitfalls

- Side effects inside row `body` cause repeated work on every update.
- `onAppear` triggers multiple times during fast scrolling; guard with loading state.
- Starting work in `.onAppear` without cancellation can lead to overlapping loads.
- Geometry-based scroll offset triggers are noisy; prefer sentinel rows for stability.

## Notes on Async Pagination
Use cancellation-aware `.task` patterns for pagination work.
See `references/concurrency.md` for SwiftUI lifecycle and cancellation guidance.
```

## File: `swift-patterns/references/state.md`
```markdown
# State Ownership

Use ownership to choose the right property wrapper. Keep a single source of truth and pass state down through bindings or immutable values.

## Decision Tree

1. Does this view own the value and it can reset when the view goes away?
   - Yes: use `@State`.
2. Does a parent own the value and this view only edits it?
   - Yes: use `@Binding`.
3. Is this value shared across many views or the app lifecycle?
   - Yes: inject through `@Environment` or a shared model in the environment.
4. Is this a reference-type model with derived state and logic?
   - iOS 17+: prefer `@Observable` models.
   - Earlier OS support: use `ObservableObject` with `@StateObject` (owner) or `@ObservedObject` (observer).

## Wrapper Cheatsheet

- `@State`: view-owned, ephemeral value types.
- `@Binding`: child edits parent-owned state.
- `@Environment`: shared values supplied by the system or the app.
- `@Observable`: modern reference models (iOS 17+).
- `ObservableObject`: compatibility fallback for earlier OSes.

## Ownership Rules

- One owner, many readers. Avoid duplicate sources of truth.
- If a child edits a value, pass a `Binding` instead of copying.
- Keep shared models in the environment when many views need access.
- Hoist state up only when multiple siblings need it; otherwise keep it local.

## Examples

### Parent owns, child edits
```swift
struct ParentView: View {
    @State private var count = 0

    var body: some View {
        CounterView(count: $count)
    }
}

struct CounterView: View {
    @Binding var count: Int

    var body: some View {
        Button("Count: \(count)") { count += 1 }
    }
}
```

### Shared model in environment
```swift
@Observable
final class SessionModel {
    var isSignedIn = false
}

struct RootView: View {
    @State private var session = SessionModel()

    var body: some View {
        ContentView()
            .environment(session)
    }
}
```

## Observation Notes

- `@Observable` is preferred for new code on iOS 17+.
- For earlier OS support, use `ObservableObject` with `@StateObject` or `@ObservedObject`.
- `@Observable` models that mutate UI-facing state may need `@MainActor` depending on project isolation.
```

## File: `swift-patterns/references/testing-di.md`
```markdown
# Testing and DI (SwiftUI)

Lightweight seams reduce refactor risk without introducing new tools or architecture mandates.

## Refactor safety seams

Use small, targeted seams to keep behavior stable while changing code.

- **Protocol abstraction:** define a protocol for external dependencies (network, storage, time).
- **Initializer injection with defaults:** inject dependencies, but provide a production default.
- **Closure-based seams:** inject a function for small, single-use dependencies.

```swift
protocol UserServiceProtocol {
    func fetchUser(id: String) async throws -> User
}

final class UserStore {
    private let userService: UserServiceProtocol

    init(userService: UserServiceProtocol = LiveUserService()) {
        self.userService = userService
    }
}
```

## Test doubles quick guide

- **Stub:** returns canned data (queries).
- **Mock:** verifies interactions (commands).
- **Spy:** records calls for later assertions.
- **Fake:** working in-memory implementation.

Minimal example (stub):
```swift
struct StubUserService: UserServiceProtocol {
    var result: Result<User, Error>

    func fetchUser(id: String) async throws -> User {
        try result.get()
    }
}
```

If tests exist, XCTest is the default baseline. Avoid adding new frameworks unless the project already uses them.

## When to add seams

Add seams before refactors that change:

- State ownership between views or wrappers.
- Navigation structure or destinations.
- Side-effect boundaries (networking, storage, analytics).

For refactor steps and invariants, see `references/workflows-refactor.md`.

## Optional tools

Third-party view inspection libraries (for example, ViewInspector) can be useful but are optional and not required.
```

## File: `swift-patterns/references/view-composition.md`
```markdown
# View Composition

Extract views to improve readability without breaking identity or state ownership. Data flows down, events flow up.

## Safe Extraction Patterns

- Keep state in the view that owns the lifetime.
- Pass immutable values for display-only content.
- Use `@Binding` for edit flows.
- Use callbacks for events (tap, submit, delete).

## Parent/Child Data Flow

- **Display-only:** pass values as plain properties.
- **Editable:** pass a `Binding`.
- **Actions:** pass closures for intent events.

## Smells and Fixes

- **Smell:** Child view owns state that should be shared.
  - **Fix:** Hoist state to the parent and pass a `Binding`.
- **Smell:** Multiple siblings compute the same derived value.
  - **Fix:** Compute once in the parent and pass the result.
- **Smell:** Child mutates parent state by reaching into environment or global state.
  - **Fix:** Pass explicit bindings or callbacks.

## Bad -> Better

### Mutating shared state in the child
```swift
// Bad: child owns shared state
struct ToggleRow: View {
    @State private var isOn = false
    var body: some View { Toggle("Enabled", isOn: $isOn) }
}

// Better: parent owns, child edits
struct ToggleRow: View {
    @Binding var isOn: Bool
    var body: some View { Toggle("Enabled", isOn: $isOn) }
}
```

### Overloading a child with business logic
```swift
// Bad: child decides deletion rules
struct Row: View {
    let item: Item
    var body: some View {
        Button("Delete") { item.deleteIfAllowed() }
    }
}

// Better: child exposes intent, parent decides
struct Row: View {
    let item: Item
    let onDelete: () -> Void

    var body: some View {
        Button("Delete", action: onDelete)
    }
}
```

## Where State Should Live

- **Local state:** view-specific toggles, text input, transient UI.
- **Hoisted state:** values shared across multiple siblings.
- **Shared state:** environment-injected models used across screens.

## Invariants

- Stable IDs stay stable across updates.
- State ownership stays with the correct view.
- Navigation state remains the source of truth.
- Async work remains cancellable and tied to view lifecycle.

## Layout Guidance

Keep layout rules simple and predictable. Let containers do the work.

### Stacks and Spacing

- Use `HStack`, `VStack`, and `ZStack` to express hierarchy.
- Prefer `spacing` on stacks over per-view padding when you need consistent gaps.
- Use `Spacer()` to distribute space and avoid hard-coded offsets.

### Alignment

- Use stack `alignment` for consistent edge alignment.
- Prefer `alignmentGuide` only when you need custom alignment behavior.

### Adaptive Layout

- Use size classes or `ViewThatFits` to adapt layout without branching the entire view.
- Keep layout resilient by avoiding fixed widths/heights when content can grow.
- For complex custom layout, consider the `Layout` protocol to centralize measurement and placement.
```

## File: `swift-patterns/references/workflows-refactor.md`
```markdown
# Refactor Workflow (SwiftUI)

Use this workflow when the user asks to change code while preserving existing behavior.

**Constraints:** See [SKILL.md Constraints](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#constraints).

## Invariants

These must hold when refactoring:

- **Stable identity:** Use stable IDs for `List`/`ForEach`. No `.indices` for dynamic data.
- **State ownership:** `@State` = view-local, `@Binding` = parent-owned, `@Observable` = shared.
- **Single navigation source:** One `NavigationStack` root, one path source of truth.
- **Cancellable async:** Tie async work to view lifecycle with `.task`.
- **Unidirectional flow:** Data down, events up. No child mutation of parent state.

## Playbooks

Use the playbooks when you need step-by-step guidance for behavior-preserving refactors:

- View extraction (preserve state ownership, stable identity, data flow)
- Navigation migration to `NavigationStack` with a single source of truth
- State hoisting without breaking bindings or async work

See [Refactor playbooks](refactor-playbooks.md).

## Behavior-Preserving Refactor Checklist

### Pre-checks

- Confirm the request is a refactor (code changes, behavior preserved)
- Capture the current behavior that must remain unchanged
- Identify the files and views in scope
- Map the Invariants above to the code being changed

### Changes

- Preserve stable identity for lists and `ForEach` content
- Keep state ownership mapping consistent (`@State`, `@Binding`, `@Observable`)
- Maintain a single navigation source of truth (one root/path)
- Keep data flowing down and events flowing up
- Ensure async work remains cancellable and tied to view lifecycle
- Avoid introducing architecture mandates or tool-specific steps

### Verification

- Re-check invariants after changes
- Confirm behavior matches the captured baseline
- If tests exist, ensure they still pass

## Risk Cues (Split Refactor or Add Tests First)

If any of these are present, split the refactor or ask for tests before proceeding:

- No tests protect the behavior being refactored
- State ownership shifts between views or wrappers
- Navigation path or root changes are required
- List identity or ordering is being changed
- Async work is moved, duplicated, or detached
- Refactor spans multiple screens or shared components
```

## File: `swift-patterns/references/workflows-review.md`
```markdown
# Review Workflow (SwiftUI)

Use this workflow when the user asks for findings, risks, or assessment without code changes.

**Constraints:** See [SKILL.md Constraints](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#constraints).

For refactor invariants, see [workflows-refactor.md](workflows-refactor.md#invariants).

## Scope and Inputs

Record the scope and inputs before reviewing:

- Files and components reviewed
- Requirements or expected behaviors
- Platform constraints (iOS version, feature flags, availability)

## Findings Taxonomy

Classify findings consistently so review output is stable and comparable:

- **Correctness:** Behavior mismatches, edge cases, crashes, or broken flows
- **Data flow:** Ownership, bindings, and unidirectional flow violations
- **Navigation:** Competing sources of truth, path mismatches, or route handling gaps
- **Identity:** Unstable list identity, incorrect `id:` usage, state loss
- **Performance:** Unnecessary recomputation, heavy work in body, missing lazy containers
- **Accessibility (when required or requested):** Missing labels, contrast, or focus issues

## Review Checklist

See the detailed Review Checklist in [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#review-checklist).

## Risk Cues (Ask for Tests or Split Work)

Escalate when you see any of these signals:

- No tests cover the behavior being reviewed or changed soon after
- State ownership is changing or being inferred during review
- Navigation path state appears in multiple places or is being redefined
- List identity changes could reset selection or row state
- Async work was moved or detached from view lifecycle
- Refactor scope touches multiple screens or core flows without verification
```

