---
id: swiftui-agent-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.899054
---

# KNOWLEDGE EXTRACT: SwiftUI-Agent-Skill
> **Extracted on:** 2026-03-29 23:47:53
> **Source:** SwiftUI-Agent-Skill

---

## File: `.gitignore`
```
# Xcode
#
# gitignore contributors: remember to update Global/Xcode.gitignore, Objective-C.gitignore & Swift.gitignore

## User settings
xcuserdata/

## Obj-C/Swift specific
*.hmap

## App packaging
*.ipa
*.dSYM.zip
*.dSYM

## Playgrounds
timeline.xctimeline
playground.xcworkspace

# Swift Package Manager
#
# Add this line if you want to avoid checking in source code from Swift Package Manager dependencies.
# Packages/
# Package.pins
# Package.resolved
# *.xcodeproj
#
# Xcode automatically generates this directory with a .xcworkspacedata file and xcuserdata
# hence it is not needed unless you have added a package configuration file to your project
# .swiftpm

.build/

# CocoaPods
#
# We recommend against adding the Pods directory to your .gitignore. However
# you should judge for yourself, the pros and cons are mentioned at:
# https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control
#
# Pods/
#
# Add this line if you want to avoid checking in source code from the Xcode workspace
# *.xcworkspace

# Carthage
#
# Add this line if you want to avoid checking in source code from Carthage dependencies.
# Carthage/Checkouts

Carthage/Build/

# fastlane
#
# It is recommended to not store the screenshots in the git repo.
# Instead, use fastlane to re-generate the screenshots whenever they are needed.
# For more information about the recommended setup visit:
# https://docs.fastlane.tools/best-practices/source-control/#source-control

fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots/**/*.png
fastlane/test_output

# Node
node_modules/
```

## File: `AGENTS.md`
```markdown
# Agent Guidelines for SwiftUI Expert Skill

This document provides guidance for AI agents working with this skill to ensure consistency and avoid common pitfalls.

## Core Principles

### 1. SwiftUI Focus Only
**This is a SwiftUI skill.** Do not include:
- Swift concurrency patterns (use `.task` for SwiftUI-specific needs only)
- General Swift language features unrelated to SwiftUI
- Backend or server-side Swift patterns
- UIKit patterns (except when bridging is necessary)

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

## What to Include

### ✅ Include These Topics:
- Property wrapper selection (`@State`, `@Binding`, `@Observable`, etc.)
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
- Testing frameworks and patterns
- Build system configuration
- Project structure mandates

## Language and Tone

### Use Clear, Direct Language:
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
2. Select SwiftUI template
3. Record and analyze...
```

## Updating the Skill

When adding new content:
1. Ask: "Is this SwiftUI-specific?"
2. Ask: "Is this a fact or an opinion?"
3. Ask: "Can agents actually use this?"
4. Ask: "Is this about correctness or style?"

If unsure, err on the side of excluding content. It's better to have a focused, factual skill than a comprehensive but opinionated one.

## Maintenance Skills

This repository includes a maintenance skill for keeping API guidance up to date:

- **`.agents/skills/update-swiftui-apis/SKILL.md`** — Scan Apple's SwiftUI documentation via the Sosumi MCP, identify deprecated APIs and their modern replacements, and update `swiftui-expert-skill/references/latest-apis.md`. Use after new iOS/Xcode releases or when you want to refresh the deprecated API reference.

## Summary

**Focus**: SwiftUI APIs, patterns, and correctness
**Avoid**: Formatting, architecture, tools, Swift language features
**Tone**: Factual, helpful, non-prescriptive
**Goal**: Make agents SwiftUI experts without enforcing opinions
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to SwiftUI Expert Skill

Thanks for your interest in improving this skill. Contributions that make SwiftUI guidance clearer, more accurate, and more up to date are welcome.

## About Agent Skills
Agent Skills are structured prompt assets with:
- A `SKILL.md` file that defines behavior and checklists
- Reference files that provide focused guidance for specific topics

## Recommended Workflow (Skill Creator)
If you use the `skill-creator` skill, you can:
- Propose changes in plain language
- Have the skill generate or refine `SKILL.md` and reference content
- Review for SwiftUI accuracy and consistency

## Alternative Workflows
### Claude without skill-creator
- Make changes directly in `SKILL.md` or `swiftui-expert-skill/references/`
- Keep content concise and focused on SwiftUI

### Manual edits
- Edit Markdown files directly
- Ensure headings and checklists stay consistent

## Updating Latest API Guidance

To refresh the deprecated-to-modern API reference after a new iOS or Xcode release, use the maintenance skill at `.agents/skills/update-swiftui-apis/SKILL.md`. It walks through scanning Apple's documentation via the Sosumi MCP and updating `swiftui-expert-skill/references/latest-apis.md` with new findings.

## Types of Contributions
- Fix incorrect SwiftUI guidance
- Add new modern APIs or deprecations
- Improve clarity in checklists
- Expand reference files with specific SwiftUI patterns
- Improve documentation in README or this guide

## Quality Standards
- SwiftUI-specific content only
- Avoid architecture mandates or project structure requirements
- Avoid tooling instructions beyond basic git usage
- Use modern APIs and flag deprecated ones
- Prefer clear, direct language over opinionated phrasing

## Pull Request Process
1. Fork the repo (or branch if you have access).
2. Make changes in a focused scope.
3. Ensure `SKILL.md` and references remain consistent.
4. Open a PR with a short summary and test notes.

## Development Setup
- Standard Markdown editing is sufficient.
- If you add or rename reference files, the README structure is auto-synced via GitHub Actions.

## Resources
- Agent Skills documentation: https://docs.anthropic.com/en/docs/claude-code/agent-skills
- SwiftUI documentation: https://developer.apple.com/documentation/swiftui

## Code of Conduct
Be respectful and constructive. Assume positive intent and focus on improving the quality of SwiftUI guidance.
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Antoine van der Lee

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
# SwiftUI Expert Skill
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/AvdLee/SwiftUI-Agent-Skill/blob/main/LICENSE)
[![Weekly Installs](https://img.shields.io/badge/weekly%20installs-10.9k-brightgreen)](https://skills.sh/avdlee/swiftui-agent-skill/swiftui-expert-skill)
[![GitHub Release](https://img.shields.io/github/v/release/AvdLee/SwiftUI-Agent-Skill)](https://github.com/AvdLee/SwiftUI-Agent-Skill/releases)
[![GitHub Stars](https://img.shields.io/github/stars/AvdLee/SwiftUI-Agent-Skill?style=flat)](https://github.com/AvdLee/SwiftUI-Agent-Skill/stargazers)

Expert guidance for any AI coding tool that supports the [Agent Skills open format](https://agentskills.io/home) — SwiftUI state management, view composition, performance, and iOS 26+ Liquid Glass adoption.

This repository distills practical SwiftUI best practices into actionable, concise references for agents and code review workflows.

## Who this is for
- Teams adopting modern SwiftUI APIs who want quick, correct defaults
- Developers reviewing or refactoring SwiftUI views and data flow
- Anyone shipping performant lists, scrolling, sheets, and navigation in SwiftUI

## See also my other skills:
- [Swift Concurrency Expert](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill)
- [Core Data Expert](https://github.com/AvdLee/Core-Data-Agent-Skill)
- [Swift Testing Expert](https://github.com/AvdLee/Swift-Testing-Agent-Skill)

## How to Use This Skill

### Option A: Using skills.sh
Install this skill with a single command:

```bash
npx skills add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill
```

For more information, [visit the skills.sh platform page](https://skills.sh/avdlee/swiftui-agent-skill/swiftui-expert-skill).

Then use the skill in your AI agent, for example:
> Use the swiftui expert skill and review the current SwiftUI code for state-management and performance improvements

### Option B: Claude Code Plugin

#### Personal Usage
To install this Skill for your personal use in Claude Code:

1. Add the marketplace:

```bash
/plugin marketplace add AvdLee/SwiftUI-Agent-Skill
```

2. Install the Skill:

```bash
/plugin install swiftui-expert@swiftui-expert-skill
```

### Option C: Cursor plugin (coming soon)
This repository is now packaged for Cursor plugin submission, but the marketplace listing is not live yet.

Once approved, you'll be able to install it from the Cursor Marketplace.

#### Project Configuration
To automatically provide this Skill to everyone working in a repository, configure the repository's `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "swiftui-expert@swiftui-expert-skill": true
  },
  "extraKnownMarketplaces": {
    "swiftui-expert-skill": {
      "source": {
        "source": "github",
        "repo": "AvdLee/SwiftUI-Agent-Skill"
      }
    }
  }
}
```

When team members open the project, Claude Code will prompt them to install the Skill.

### Option D: Codex / OpenAI-compatible tools
This repository includes an `agents/openai.yaml` manifest. Copy or symlink the `swiftui-expert-skill/` folder into your Codex skills directory:

```bash
cp -R swiftui-expert-skill/ "$CODEX_HOME/skills/swiftui-expert-skill"
```

See [Codex skills documentation](https://developers.openai.com/codex/skills/) for details on where to save skills.

### Option E: Manual install
1) **Clone** this repository.
2) **Install or symlink** the `swiftui-expert-skill/` folder following your tool’s official skills installation docs (see links below).
3) **Use your AI tool** as usual and ask it to use the “swiftui-expert” skill for SwiftUI tasks.

#### Where to Save Skills
Follow your tool’s official documentation, here are a few popular ones:
- **Codex:** [Where to save skills](https://developers.openai.com/codex/skills/#where-to-save-skills)
- **Claude:** [Using Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#using-skills)
- **Cursor:** [Plugins documentation](https://cursor.com/docs/plugins) or [Enabling Skills](https://cursor.com/docs/context/skills#enabling-skills)

**How to verify**:

Your agent should reference the workflow/checklists in `swiftui-expert-skill/SKILL.md` and jump into the relevant reference file for your task.

## What's Inside

This skill covers the full surface of SwiftUI development -- from state management and view composition to Swift Charts, macOS multi-window scenes, animations, and iOS 26+ Liquid Glass -- without bloating your agent's task context. Reference files load on demand, so your agent gets deep guidance only for the topic at hand.

- **State management** -- property wrapper selection, `@Observable`, data flow patterns
- **View composition** -- extraction patterns, container views, identity stability
- **Performance** -- hot-path optimization, lazy loading, `@Observable` granularity
- **Lists & ForEach** -- stable identity, Table, inline filtering pitfalls
- **Navigation & sheets** -- NavigationStack, NavigationSplitView, Inspector, enum-based sheets
- **Swift Charts** -- marks, axes, selection, styling, accessibility, Chart3D
- **Animations** -- implicit/explicit, transitions, phase/keyframe, `@Animatable` macro
- **macOS** -- scenes, window styling, Table, HSplitView, AppKit interop
- **Liquid Glass** -- iOS 26+ glass effects, containers, fallback patterns
- **Accessibility** -- VoiceOver, Dynamic Type, grouping, traits
- **Image optimization** -- AsyncImage, downsampling, caching
- **Latest APIs** -- deprecated-to-modern migration guide (iOS 15+ through iOS 26+)

Non-opinionated: focuses on correctness and performance, not architecture or code style.

## Skill Structure
<!-- BEGIN REFERENCE STRUCTURE -->
```text
swiftui-expert-skill/
  SKILL.md
  references/
    accessibility-patterns.md - Accessibility traits, grouping, Dynamic Type, and VoiceOver
    animation-advanced.md - Performance, interpolation, and complex animation chains
    animation-basics.md - Core animation concepts, implicit/explicit animations, timing
    animation-transitions.md - View transitions, matchedGeometryEffect, and state changes
    charts-accessibility.md - Charts accessibility, fallback strategies, and WWDC sessions
    charts.md - Swift Charts marks, axes, selection, styling, composition, and Chart3D
    image-optimization.md - AsyncImage usage, downsampling, caching
    latest-apis.md
    layout-best-practices.md - Layout patterns and GeometryReader alternatives
    liquid-glass.md - iOS 26+ glass effects and fallback patterns
    list-patterns.md - ForEach identity and list performance
    macos-scenes.md - Scene lifecycle, multi-window setups, and menu bar scenes on macOS
    macos-views.md - macOS-specific SwiftUI views and platform differences from iOS
    macos-window-styling.md - Window chrome, toolbar, and title bar styling in SwiftUI
    performance-patterns.md - Hot-path optimizations and update control
    scroll-patterns.md - ScrollViewReader and programmatic scrolling
    sheet-navigation-patterns.md - Sheets and type-safe navigation
    state-management.md - Property wrapper selection and data flow
    view-structure.md - View extraction and composition patterns
```
<!-- END REFERENCE STRUCTURE -->

## Maintenance

The repository includes a maintenance skill for keeping API guidance current:

```text
.agents/skills/update-swiftui-apis/
  SKILL.md               - Workflow for scanning Apple docs and updating latest-apis.md
  references/
    scan-manifest.md     - Categorized API areas, doc paths, and search queries to scan
```

Use this skill after new iOS or Xcode releases to refresh the deprecated API reference. It requires the [Sosumi MCP](https://github.com/kanaa257/sosumi.ai) to be available. See `AGENTS.md` or `CONTRIBUTING.md` for details.

Note: only `swiftui-expert-skill` is intended to be published in the Cursor plugin. The maintenance skill remains a repository workflow utility.

## Contributing

Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.io/home), which has specific structural requirements.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to contribute improvements to `SKILL.md` and the reference files
- Format requirements and quality standards
- Pull request process

## Acknowledgments

Several SwiftUI guidelines in this skill were inspired by or derived from the following works:

- [Skills](https://github.com/Dimillian/Skills) by [Thomas Ricouard](https://github.com/Dimillian) — a collection of SwiftUI-focused Codex skills covering UI patterns, performance auditing, and Liquid Glass.
- [SwiftLee SwiftUI articles](https://www.avanderlee.com/category/swiftui/) and [Swift articles](https://www.avanderlee.com/category/swift/) by [Antoine van der Lee](https://www.avanderlee.com) — practical SwiftUI best practices covering state management, accessibility, view composition, performance debugging, image optimization, and more.
- [Swift Charts Examples](https://github.com/jordibruin/Swift-Charts-Examples) by [Jordi Bruin](https://x.com/jordibruin) — a comprehensive collection of Swift Charts examples covering line, bar, area, range, heat map, and point charts with accessibility and customization patterns. Used with permission.

## About the authors

Created by [Antoine van der Lee](https://www.avanderlee.com) and [Omar Elsayed](https://www.swiftdifferently.com). With years of experience in Swift & SwiftUI, this skill distills practical knowledge into actionable guidance for AI assistants. Antoine [published tens of articles on SwiftUI](https://www.avanderlee.com/category/swiftui/) on his blog called SwiftLee.

## Resources
- [Story behind this skill](https://www.swiftdifferently.com/blog/swiftui/How%20I%20stopped-resisting-ai-and-atarted-teaching-it)

## License

This skill is open-source and available under the MIT License. See [LICENSE](LICENSE) for details.
```

## File: `agents/openai.yaml`
```yaml
name: swiftui-expert
version: "2.2.0"
description: >-
  Expert SwiftUI guidance for state management, view composition,
  performance, and iOS 26+ Liquid Glass adoption.
author:
  name: Antoine van der Lee
  email: contact@avanderlee.com
repository: https://github.com/AvdLee/SwiftUI-Agent-Skill
license: MIT
logo: assets/logo.svg
keywords:
  - swift
  - swiftui
  - ios
  - apple
  - state-management
  - performance
  - liquid-glass
  - view-composition
  - navigation
  - lists
  - sheets
skills:
  - swiftui-expert-skill
```

## File: `swiftui-expert-skill/SKILL.md`
```markdown
---
name: swiftui-expert-skill
description: Write, review, or improve SwiftUI code following best practices for state management, view composition, performance, macOS-specific APIs, and iOS 26+ Liquid Glass adoption. Use when building new SwiftUI features, refactoring existing views, reviewing code quality, or adopting modern SwiftUI patterns.
---

# SwiftUI Expert Skill

## Operating Rules

- Consult `references/latest-apis.md` at the start of every task to avoid deprecated APIs
- Prefer native SwiftUI APIs over UIKit/AppKit bridging unless bridging is necessary
- Focus on correctness and performance; do not enforce specific architectures (MVVM, VIPER, etc.)
- Encourage separating business logic from views for testability without mandating how
- Follow Apple's Human Interface Guidelines and API design patterns
- Only adopt Liquid Glass when explicitly requested by the user (see `references/liquid-glass.md`)
- Present performance optimizations as suggestions, not requirements
- Use `#available` gating with sensible fallbacks for version-specific APIs

## Task Workflow

### Review existing SwiftUI code
- Read the code under review and identify which topics apply
- Flag deprecated APIs (compare against `references/latest-apis.md`)
- Run the Topic Router below for each relevant topic
- Validate `#available` gating and fallback paths for iOS 26+ features

### Improve existing SwiftUI code
- Audit current implementation against the Topic Router topics
- Replace deprecated APIs with modern equivalents from `references/latest-apis.md`
- Refactor hot paths to reduce unnecessary state updates
- Extract complex view bodies into separate subviews
- Suggest image downsampling when `UIImage(data:)` is encountered (optional optimization, see `references/image-optimization.md`)

### Implement new SwiftUI feature
- Design data flow first: identify owned vs injected state
- Structure views for optimal diffing (extract subviews early)
- Apply correct animation patterns (implicit vs explicit, transitions)
- Use `Button` for all tappable elements; add accessibility grouping and labels
- Gate version-specific APIs with `#available` and provide fallbacks

### Topic Router

Consult the reference file for each topic relevant to the current task:

| Topic | Reference |
|-------|-----------|
| State management | `references/state-management.md` |
| View composition | `references/view-structure.md` |
| Performance | `references/performance-patterns.md` |
| Lists and ForEach | `references/list-patterns.md` |
| Layout | `references/layout-best-practices.md` |
| Sheets and navigation | `references/sheet-navigation-patterns.md` |
| ScrollView | `references/scroll-patterns.md` |
| Animations (basics) | `references/animation-basics.md` |
| Animations (transitions) | `references/animation-transitions.md` |
| Animations (advanced) | `references/animation-advanced.md` |
| Accessibility | `references/accessibility-patterns.md` |
| Swift Charts | `references/charts.md` |
| Charts accessibility | `references/charts-accessibility.md` |
| Image optimization | `references/image-optimization.md` |
| Liquid Glass (iOS 26+) | `references/liquid-glass.md` |
| macOS scenes | `references/macos-scenes.md` |
| macOS window styling | `references/macos-window-styling.md` |
| macOS views | `references/macos-views.md` |
| Deprecated API lookup | `references/latest-apis.md` |

## Correctness Checklist

These are hard rules -- violations are always bugs:

- [ ] `@State` properties are `private`
- [ ] `@Binding` only where a child modifies parent state
- [ ] Passed values never declared as `@State` or `@StateObject` (they ignore updates)
- [ ] `@StateObject` for view-owned objects; `@ObservedObject` for injected
- [ ] iOS 17+: `@State` with `@Observable`; `@Bindable` for injected observables needing bindings
- [ ] `ForEach` uses stable identity (never `.indices` for dynamic content)
- [ ] Constant number of views per `ForEach` element
- [ ] `.animation(_:value:)` always includes the `value` parameter
- [ ] iOS 26+ APIs gated with `#available` and fallback provided
- [ ] `import Charts` present in files using chart types

## References

- `references/latest-apis.md` -- **Read first for every task.** Deprecated-to-modern API transitions (iOS 15+ through iOS 26+)
- `references/state-management.md` -- Property wrappers, data flow, `@Observable` migration
- `references/view-structure.md` -- View extraction, container patterns, `@ViewBuilder`
- `references/performance-patterns.md` -- Hot-path optimization, update control, `_logChanges()`
- `references/list-patterns.md` -- ForEach identity, Table (iOS 16+), inline filtering pitfalls
- `references/layout-best-practices.md` -- Layout patterns, GeometryReader alternatives
- `references/accessibility-patterns.md` -- VoiceOver, Dynamic Type, grouping, traits
- `references/animation-basics.md` -- Implicit/explicit animations, timing, performance
- `references/animation-transitions.md` -- View transitions, `matchedGeometryEffect`, `Animatable`
- `references/animation-advanced.md` -- Phase/keyframe animations (iOS 17+), `@Animatable` macro (iOS 26+)
- `references/charts.md` -- Swift Charts marks, axes, selection, styling, Chart3D (iOS 26+)
- `references/charts-accessibility.md` -- Charts VoiceOver, Audio Graph, fallback strategies
- `references/sheet-navigation-patterns.md` -- Sheets, NavigationSplitView, Inspector
- `references/scroll-patterns.md` -- ScrollViewReader, programmatic scrolling
- `references/image-optimization.md` -- AsyncImage, downsampling, caching
- `references/liquid-glass.md` -- iOS 26+ Liquid Glass effects and fallback patterns
- `references/macos-scenes.md` -- Settings, MenuBarExtra, WindowGroup, multi-window
- `references/macos-window-styling.md` -- Toolbar styles, window sizing, Commands
- `references/macos-views.md` -- HSplitView, Table, PasteButton, AppKit interop
```

## File: `swiftui-expert-skill/references/accessibility-patterns.md`
```markdown
# SwiftUI Accessibility Patterns Reference

## Table of Contents

- [Core Principle](#core-principle)
- [Dynamic Type and @ScaledMetric](#dynamic-type-and-scaledmetric)
- [Accessibility Traits](#accessibility-traits)
- [Decorative Images](#decorative-images)
- [Element Grouping](#element-grouping)
- [Custom Controls](#custom-controls)
- [Summary Checklist](#summary-checklist)

## Core Principle

Prefer `Button` over `onTapGesture` for tappable elements. `Button` provides VoiceOver support, focus handling, and proper traits for free.

## Dynamic Type and @ScaledMetric

System text styles scale with Dynamic Type automatically. Prefer built-in styles like `.largeTitle`, `.title`, `.title2`, `.title3`, `.headline`, `.subheadline`, `.body`, `.callout`, `.footnote`, `.caption`, and `.caption2` when they fit your UI:

```swift
VStack(alignment: .leading) {
    Text("Inbox")
        .font(.title2)
    Text("3 unread messages")
        .font(.body)
    Text("Updated just now")
        .font(.caption)
}
```

For custom fonts, use a Dynamic Type-aware font initializer so the text still follows the user's preferred content size:

```swift
VStack(alignment: .leading) {
    Text("Article")
        .font(.custom("SourceSerif4-Semibold", size: 28, relativeTo: .title2))
    Text("Body copy")
        .font(.custom("SourceSerif4-Regular", size: 17))
}
```

`Font.custom(_:size:relativeTo:)` lets you match a specific text style. `Font.custom(_:size:)` scales relative to the body style. Avoid fixed-size custom fonts for primary content that should respond to Dynamic Type.

For non-text numeric values like padding, spacing, and image sizes, use `@ScaledMetric`:

```swift
struct ProfileHeader: View {
    @ScaledMetric private var avatarSize = 60.0
    @ScaledMetric private var spacing = 12.0

    var body: some View {
        HStack(spacing: spacing) {
            Image("avatar")
                .resizable()
                .frame(width: avatarSize, height: avatarSize)
            Text("Username")
        }
    }
}
```

Specify a `relativeTo` text style when the value should track a specific Dynamic Type style, including for images or icons that should stay proportional to nearby text:

```swift
struct StatusRow: View {
    @ScaledMetric(relativeTo: .body) private var iconSize = 18.0

    var body: some View {
        HStack(spacing: 8) {
            Image(systemName: "checkmark.circle.fill")
                .font(.system(size: iconSize))
            Text("Synced")
                .font(.custom("AvenirNext-Regular", size: 17, relativeTo: .body))
        }
    }
}
```

## Accessibility Traits

Use `accessibilityAddTraits` and `accessibilityRemoveTraits` for state-driven traits:

```swift
Text(item.title)
    .accessibilityAddTraits(item.isSelected ? [.isSelected, .isButton] : .isButton)
```

Use `.disabled(true)` to make VoiceOver announce "Dimmed" for non-interactive elements.

## Decorative Images

Use `Image(decorative:bundle:)` when an asset image is purely visual and should not appear in the accessibility tree.

```swift
Image(decorative: "confetti")
```

This is appropriate for backgrounds, flourishes, and icons that do not add meaning beyond nearby text.

If the image conveys information, keep it accessible and provide a clear label:

```swift
Image("receipt")
    .accessibilityLabel("Receipt")
```

For non-asset images, such as SF Symbols, hide decorative content with `accessibilityHidden(true)` instead:

```swift
Image(systemName: "sparkles")
    .accessibilityHidden(true)
```

## Element Grouping

### .combine -- Auto-join child labels

```swift
HStack {
    Image(systemName: "star.fill")
    Text("Favorites")
    Text("(\(count))")
}
.accessibilityElement(children: .combine)
```

VoiceOver reads all child labels as one element, separated by commas.

### .ignore -- Manual label for container

```swift
HStack {
    Text(item.name)
    Spacer()
    Text(item.price)
}
.accessibilityElement(children: .ignore)
.accessibilityLabel("\(item.name), \(item.price)")
```

### .contain -- Semantic grouping

```swift
HStack {
    ForEach(tabs) { tab in
        TabButton(tab: tab)
    }
}
.accessibilityElement(children: .contain)
.accessibilityLabel("Tab bar")
```

VoiceOver announces the container name when focus enters/exits.

## Custom Controls

### Adjustable controls (increment/decrement)

```swift
PageControl(selectedIndex: $selectedIndex, pageCount: pageCount)
    .accessibilityElement()
    .accessibilityValue("Page \(selectedIndex + 1) of \(pageCount)")
    .accessibilityAdjustableAction { direction in
        switch direction {
        case .increment:
            guard selectedIndex < pageCount - 1 else { break }
            selectedIndex += 1
        case .decrement:
            guard selectedIndex > 0 else { break }
            selectedIndex -= 1
        @unknown default:
            break
        }
    }
```

### Representing custom views as native controls

When a custom view should behave like a native control for accessibility:

```swift
HStack {
    Text(label)
    Toggle("", isOn: $isOn)
}
.accessibilityRepresentation {
    Toggle(label, isOn: $isOn)
}
```

### Label-content pairing

```swift
@Namespace private var ns

HStack {
    Text("Volume")
        .accessibilityLabeledPair(role: .label, id: "volume", in: ns)
    Slider(value: $volume)
        .accessibilityLabeledPair(role: .content, id: "volume", in: ns)
}
```

## Summary Checklist

- [ ] Use `Button` instead of `onTapGesture` for tappable elements
- [ ] Use built-in text styles or Dynamic Type-aware custom fonts for text
- [ ] Use `@ScaledMetric` for custom values that should scale with Dynamic Type
- [ ] Mark purely decorative images as decorative or hidden from accessibility
- [ ] Group related elements with `accessibilityElement(children:)`
- [ ] Provide `accessibilityLabel` when default labels are unclear
- [ ] Use `accessibilityRepresentation` for custom controls
- [ ] Use `accessibilityAdjustableAction` for increment/decrement controls
- [ ] Ensure navigation flow is logical when using VoiceOver grouping
```

## File: `swiftui-expert-skill/references/animation-advanced.md`
```markdown
# SwiftUI Advanced Animations

Transactions, phase animations (iOS 17+), keyframe animations (iOS 17+), completion handlers (iOS 17+), and `@Animatable` macro (iOS 26+).

## Table of Contents
- [Transactions](#transactions)
- [Phase Animations (iOS 17+)](#phase-animations-ios-17)
- [Keyframe Animations (iOS 17+)](#keyframe-animations-ios-17)
- [Animation Completion Handlers (iOS 17+)](#animation-completion-handlers-ios-17)
- [@Animatable Macro (iOS 26+)](#animatable-macro-ios-26)

---

## Transactions

The underlying mechanism for all animations in SwiftUI.

### Basic Usage

```swift
// withAnimation is shorthand for withTransaction
withAnimation(.default) { flag.toggle() }

// Equivalent explicit transaction
var transaction = Transaction(animation: .default)
withTransaction(transaction) { flag.toggle() }
```

### The .transaction Modifier

```swift
Rectangle()
    .frame(width: flag ? 100 : 50, height: 50)
    .transaction { t in
        t.animation = .default
    }
```

**Note:** This behaves like the deprecated `.animation(_:)` without value parameter - it animates on every state change.

### Animation Precedence

**Implicit animations override explicit animations** (later in view tree wins).

```swift
Button("Tap") {
    withAnimation(.linear) { flag.toggle() }
}
.animation(.bouncy, value: flag)  // .bouncy wins!
```

### Disabling Animations

```swift
// Prevent implicit animations from overriding
.transaction { t in
    t.disablesAnimations = true
}

// Remove animation entirely
.transaction { $0.animation = nil }
```

### Custom Transaction Keys (iOS 17+)

Pass metadata through transactions.

```swift
struct ChangeSourceKey: TransactionKey {
    static let defaultValue: String = "unknown"
}

extension Transaction {
    var changeSource: String {
        get { self[ChangeSourceKey.self] }
        set { self[ChangeSourceKey.self] = newValue }
    }
}

// Set source
var transaction = Transaction(animation: .default)
transaction.changeSource = "server"
withTransaction(transaction) { flag.toggle() }

// Read in view tree
.transaction { t in
    if t.changeSource == "server" {
        t.animation = .smooth
    } else {
        t.animation = .bouncy
    }
}
```

---

## Phase Animations (iOS 17+)

Cycle through discrete phases automatically. Each phase change is a separate animation.

### Basic Usage

```swift
// GOOD - triggered phase animation
Button("Shake") { trigger += 1 }
    .phaseAnimator(
        [0.0, -10.0, 10.0, -5.0, 5.0, 0.0],
        trigger: trigger
    ) { content, offset in
        content.offset(x: offset)
    }

// Infinite loop (no trigger)
Circle()
    .phaseAnimator([1.0, 1.2, 1.0]) { content, scale in
        content.scaleEffect(scale)
    }
```

### Enum Phases (Recommended for Clarity)

```swift
// GOOD - enum phases are self-documenting
enum BouncePhase: CaseIterable {
    case initial, up, down, settle

    var scale: CGFloat {
        switch self {
        case .initial: 1.0
        case .up: 1.2
        case .down: 0.9
        case .settle: 1.0
        }
    }
}

Circle()
    .phaseAnimator(BouncePhase.allCases, trigger: trigger) { content, phase in
        content.scaleEffect(phase.scale)
    }
```

### Custom Timing Per Phase

```swift
.phaseAnimator([0, -20, 20], trigger: trigger) { content, offset in
    content.offset(x: offset)
} animation: { phase in
    switch phase {
    case -20: .bouncy
    case 20: .linear
    default: .smooth
    }
}
```

### Good vs Bad

```swift
// GOOD - use phaseAnimator for multi-step sequences
.phaseAnimator([0, -10, 10, 0], trigger: trigger) { content, offset in
    content.offset(x: offset)
}

// BAD - manual DispatchQueue sequencing
Button("Animate") {
    withAnimation(.easeOut(duration: 0.1)) { offset = -10 }
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
        withAnimation { offset = 10 }
    }
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.2) {
        withAnimation { offset = 0 }
    }
}
```

---

## Keyframe Animations (iOS 17+)

Precise timing control with exact values at specific times.

### Basic Usage

```swift
Button("Bounce") { trigger += 1 }
    .keyframeAnimator(
        initialValue: AnimationValues(),
        trigger: trigger
    ) { content, value in
        content
            .scaleEffect(value.scale)
            .offset(y: value.verticalOffset)
    } keyframes: { _ in
        KeyframeTrack(\.scale) {
            SpringKeyframe(1.2, duration: 0.15)
            SpringKeyframe(0.9, duration: 0.1)
            SpringKeyframe(1.0, duration: 0.15)
        }
        KeyframeTrack(\.verticalOffset) {
            LinearKeyframe(-20, duration: 0.15)
            LinearKeyframe(0, duration: 0.25)
        }
    }

struct AnimationValues {
    var scale: CGFloat = 1.0
    var verticalOffset: CGFloat = 0
}
```

### Keyframe Types

| Type | Behavior |
|------|----------|
| `CubicKeyframe` | Smooth interpolation |
| `LinearKeyframe` | Straight-line interpolation |
| `SpringKeyframe` | Spring physics |
| `MoveKeyframe` | Instant jump (no interpolation) |

### Multiple Synchronized Tracks

Tracks run **in parallel**, each animating one property.

```swift
// GOOD - bell shake with synchronized rotation and scale
struct BellAnimation {
    var rotation: Double = 0
    var scale: CGFloat = 1.0
}

Image(systemName: "bell.fill")
    .keyframeAnimator(
        initialValue: BellAnimation(),
        trigger: trigger
    ) { content, value in
        content
            .rotationEffect(.degrees(value.rotation))
            .scaleEffect(value.scale)
    } keyframes: { _ in
        KeyframeTrack(\.rotation) {
            CubicKeyframe(15, duration: 0.1)
            CubicKeyframe(-15, duration: 0.1)
            CubicKeyframe(10, duration: 0.1)
            CubicKeyframe(-10, duration: 0.1)
            CubicKeyframe(0, duration: 0.1)
        }
        KeyframeTrack(\.scale) {
            CubicKeyframe(1.1, duration: 0.25)
            CubicKeyframe(1.0, duration: 0.25)
        }
    }

// BAD - manual timer-based animation
Image(systemName: "bell.fill")
    .onTapGesture {
        withAnimation(.easeOut(duration: 0.1)) { rotation = 15 }
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            withAnimation { rotation = -15 }
        }
        // ... more manual timing - error prone
    }
```

### KeyframeTimeline (iOS 17+)

Query animation values directly for testing or non-SwiftUI use.

```swift
let timeline = KeyframeTimeline(initialValue: AnimationValues()) {
    KeyframeTrack(\.scale) {
        CubicKeyframe(1.2, duration: 0.25)
        CubicKeyframe(1.0, duration: 0.25)
    }
}

let midpoint = timeline.value(time: 0.25)
print(midpoint.scale)  // Value at 0.25 seconds
```

---

## Animation Completion Handlers (iOS 17+)

Execute code when animations finish.

### With withAnimation

```swift
// GOOD - completion with withAnimation
Button("Animate") {
    withAnimation(.spring) {
        isExpanded.toggle()
    } completion: {
        showNextStep = true
    }
}
```

### With Transaction (For Reexecution)

```swift
// GOOD - completion fires on every trigger change
Circle()
    .scaleEffect(bounceCount % 2 == 0 ? 1.0 : 1.2)
    .transaction(value: bounceCount) { transaction in
        transaction.animation = .spring
        transaction.addAnimationCompletion {
            message = "Bounce \(bounceCount) complete"
        }
    }

// BAD - completion only fires ONCE (no value parameter)
Circle()
    .scaleEffect(bounceCount % 2 == 0 ? 1.0 : 1.2)
    .animation(.spring, value: bounceCount)
    .transaction { transaction in  // No value!
        transaction.addAnimationCompletion {
            completionCount += 1  // Only fires once, ever
        }
    }
```

---

## @Animatable Macro (iOS 26+)

The `@Animatable` macro auto-synthesizes `animatableData` from all animatable stored properties, eliminating verbose manual conformance. Use `@AnimatableIgnored` to exclude properties that should not animate.

### Before (Manual)

```swift
struct Wedge: Shape {
    var startAngle: Angle
    var endAngle: Angle
    var drawClockwise: Bool

    var animatableData: AnimatablePair<Double, Double> {
        get { AnimatablePair(startAngle.radians, endAngle.radians) }
        set {
            startAngle = .radians(newValue.first)
            endAngle = .radians(newValue.second)
        }
    }

    func path(in rect: CGRect) -> Path { /* ... */ }
}
```

### After (@Animatable)

```swift
@Animatable
struct Wedge: Shape {
    var startAngle: Angle
    var endAngle: Angle
    @AnimatableIgnored var drawClockwise: Bool

    func path(in rect: CGRect) -> Path { /* ... */ }
}
```

### When to Use
- **Prefer `@Animatable`** for any custom `Shape`, `AnimatableModifier`, or type conforming to `Animatable` with multiple properties
- **Use `@AnimatableIgnored`** for properties that control behavior but should not interpolate (e.g., directions, flags, identifiers)
- The macro works with any type conforming to `Animatable`, not just `Shape`

> Source: "What's new in SwiftUI" (WWDC25, session 256)

---

## Quick Reference

### Transactions (All iOS versions)
- `withTransaction` is the explicit form of `withAnimation`
- Implicit animations override explicit (later in view tree wins)
- Use `disablesAnimations` to prevent override
- Use `.transaction { $0.animation = nil }` to remove animation

### Custom Transaction Keys (iOS 17+)
- Pass metadata through animation system via `TransactionKey`

### Phase Animations (iOS 17+)
- Use for multi-step sequences returning to start
- Prefer enum phases for clarity
- Each phase change is a separate animation
- Use `trigger` parameter for one-shot animations

### Keyframe Animations (iOS 17+)
- Use for precise timing control
- Tracks run in parallel
- Use `KeyframeTimeline` for testing/advanced use
- Prefer over manual DispatchQueue timing

### Completion Handlers (iOS 17+)
- Use `withAnimation(.animation) { } completion: { }` for one-shot completion handlers
- Use `.transaction(value:)` for handlers that should refire on every value change
- Without `value:` parameter, completion only fires once

### @Animatable Macro (iOS 26+)
- Use `@Animatable` to auto-synthesize `animatableData` from stored properties
- Use `@AnimatableIgnored` to exclude non-animatable properties
- Replaces verbose manual `animatableData` getters/setters
```

## File: `swiftui-expert-skill/references/animation-basics.md`
```markdown
# SwiftUI Animation Basics

Core animation concepts, implicit vs explicit animations, timing curves, and performance patterns.

## Table of Contents
- [Core Concepts](#core-concepts)
- [Implicit Animations](#implicit-animations)
- [Explicit Animations](#explicit-animations)
- [Animation Placement](#animation-placement)
- [Selective Animation](#selective-animation)
- [Timing Curves](#timing-curves)
- [Animation Performance](#animation-performance)
- [Disabling Animations](#disabling-animations)
- [Debugging](#debugging)

---

## Core Concepts

State changes trigger view updates. SwiftUI provides mechanisms to animate these changes.

**Animation Process:**
1. State change triggers view tree re-evaluation
2. SwiftUI compares new tree to current render tree
3. Animatable properties are identified and interpolated (~60 fps)

**Key Characteristics:**
- Animations are additive and cancelable
- Always start from current render tree state
- Blend smoothly when interrupted

---

## Implicit Animations

Use `.animation(_:value:)` to animate when a specific value changes.

```swift
// GOOD - uses value parameter
Rectangle()
    .frame(width: isExpanded ? 200 : 100, height: 50)
    .animation(.spring, value: isExpanded)
    .onTapGesture { isExpanded.toggle() }

// BAD - deprecated, animates all changes unexpectedly
Rectangle()
    .frame(width: isExpanded ? 200 : 100, height: 50)
    .animation(.spring)  // Deprecated!
```

---

## Explicit Animations

Use `withAnimation` for event-driven state changes.

```swift
// GOOD - explicit animation
Button("Toggle") {
    withAnimation(.spring) {
        isExpanded.toggle()
    }
}

// BAD - no animation context
Button("Toggle") {
    isExpanded.toggle()  // Abrupt change
}
```

**When to use which:**
- **Implicit**: Animations tied to specific value changes, precise view tree scope
- **Explicit**: Event-driven animations (button taps, gestures)

---

## Animation Placement

Place animation modifiers after the properties they should animate.

```swift
// GOOD - animation after properties
Rectangle()
    .frame(width: isExpanded ? 200 : 100, height: 50)
    .foregroundStyle(isExpanded ? .blue : .red)
    .animation(.default, value: isExpanded)  // Animates both

// BAD - animation before properties
Rectangle()
    .animation(.default, value: isExpanded)  // Too early!
    .frame(width: isExpanded ? 200 : 100, height: 50)
```

---

## Selective Animation

Animate only specific properties using multiple animation modifiers or scoped animations.

```swift
// GOOD - selective animation
Rectangle()
    .frame(width: isExpanded ? 200 : 100, height: 50)
    .animation(.spring, value: isExpanded)  // Animate size
    .foregroundStyle(isExpanded ? .blue : .red)
    .animation(nil, value: isExpanded)  // Don't animate color

// iOS 17+ scoped animation
Rectangle()
    .foregroundStyle(isExpanded ? .blue : .red)  // Not animated
    .animation(.spring) {
        $0.frame(width: isExpanded ? 200 : 100, height: 50)  // Animated
    }
```

---

## Timing Curves

### Built-in Curves

| Curve | Use Case |
|-------|----------|
| `.spring` | Interactive elements, most UI |
| `.easeInOut` | Appearance changes |
| `.bouncy` | Playful feedback (iOS 17+) |
| `.linear` | Progress indicators only |

### Modifiers

```swift
.animation(.default.speed(2.0), value: flag)  // 2x faster
.animation(.default.delay(0.5), value: flag)  // Delayed start
.animation(.default.repeatCount(3, autoreverses: true), value: flag)
```

### Good vs Bad Timing

```swift
// GOOD - appropriate timing for interaction type
Button("Tap") {
    withAnimation(.spring(response: 0.3, dampingFraction: 0.7)) {
        isActive.toggle()
    }
}
.scaleEffect(isActive ? 0.95 : 1.0)

// BAD - too slow for button feedback
Button("Tap") {
    withAnimation(.easeInOut(duration: 1.0)) {  // Way too slow!
        isActive.toggle()
    }
}

// BAD - linear feels robotic
Rectangle()
    .animation(.linear(duration: 0.5), value: isActive)  // Mechanical
```

---

## Animation Performance

### Prefer Transforms Over Layout

```swift
// GOOD - GPU accelerated transforms
Rectangle()
    .frame(width: 100, height: 100)
    .scaleEffect(isActive ? 1.5 : 1.0)  // Fast
    .offset(x: isActive ? 50 : 0)        // Fast
    .rotationEffect(.degrees(isActive ? 45 : 0))  // Fast
    .animation(.spring, value: isActive)

// BAD - layout changes are expensive
Rectangle()
    .frame(width: isActive ? 150 : 100, height: isActive ? 150 : 100)  // Expensive
    .padding(isActive ? 50 : 0)  // Expensive
```

### Narrow Animation Scope

```swift
// GOOD - animation scoped to specific subview
VStack {
    HeaderView()  // Not affected
    ExpandableContent(isExpanded: isExpanded)
        .animation(.spring, value: isExpanded)  // Only this
    FooterView()  // Not affected
}

// BAD - animation at root
VStack {
    HeaderView()
    ExpandableContent(isExpanded: isExpanded)
    FooterView()
}
.animation(.spring, value: isExpanded)  // Animates everything
```

### Avoid Animation in Hot Paths

```swift
// GOOD - gate by threshold
.onPreferenceChange(ScrollOffsetKey.self) { offset in
    let shouldShow = offset.y < -50
    if shouldShow != showTitle {  // Only when crossing threshold
        withAnimation(.easeOut(duration: 0.2)) {
            showTitle = shouldShow
        }
    }
}

// BAD - animating every scroll change
.onPreferenceChange(ScrollOffsetKey.self) { offset in
    withAnimation {  // Fires constantly!
        self.offset = offset.y
    }
}
```

---

## Disabling Animations

```swift
// GOOD - disable with transaction
Text("Count: \(count)")
    .transaction { $0.animation = nil }

// GOOD - disable from parent context
DataView()
    .transaction { $0.disablesAnimations = true }

// BAD - hacky zero duration
Text("Count: \(count)")
    .animation(.linear(duration: 0), value: count)  // Hacky
```

---

## Debugging

```swift
// Slow down for inspection
#if DEBUG
.animation(.linear(duration: 3.0).speed(0.2), value: isExpanded)
#else
.animation(.spring, value: isExpanded)
#endif

// Debug modifier to log values
struct AnimationDebugModifier: ViewModifier, Animatable {
    var value: Double
    var animatableData: Double {
        get { value }
        set {
            value = newValue
            print("Animation: \(newValue)")
        }
    }
    func body(content: Content) -> some View {
        content.opacity(value)
    }
}
```

---

## Quick Reference

### Do
- Use `.animation(_:value:)` with value parameter
- Use `withAnimation` for event-driven animations
- Prefer transforms over layout changes
- Scope animations narrowly
- Choose appropriate timing curves

### Don't
- Use deprecated `.animation(_:)` without value
- Animate layout properties in hot paths
- Apply broad animations at root level
- Use linear timing for UI (feels robotic)
- Animate on every frame in scroll handlers
```

## File: `swiftui-expert-skill/references/animation-transitions.md`
```markdown
# SwiftUI Transitions

Transitions for view insertion/removal, custom transitions, and the Animatable protocol.

## Table of Contents
- [Property Animations vs Transitions](#property-animations-vs-transitions)
- [Basic Transitions](#basic-transitions)
- [Asymmetric Transitions](#asymmetric-transitions)
- [Custom Transitions](#custom-transitions)
- [Identity and Transitions](#identity-and-transitions)
- [The Animatable Protocol](#the-animatable-protocol)

---

## Property Animations vs Transitions

**Property animations**: Interpolate values on views that exist before AND after state change.

**Transitions**: Animate views being inserted or removed from the render tree.

```swift
// Property animation - same view, different properties
Rectangle()
    .frame(width: isExpanded ? 200 : 100, height: 50)
    .animation(.spring, value: isExpanded)

// Transition - view inserted/removed
if showDetail {
    DetailView()
        .transition(.scale)
}
```

---

## Basic Transitions

### Critical: Transitions Require Animation Context

```swift
// GOOD - animation outside conditional
VStack {
    Button("Toggle") { showDetail.toggle() }
    if showDetail {
        DetailView()
            .transition(.slide)
    }
}
.animation(.spring, value: showDetail)

// GOOD - explicit animation
Button("Toggle") {
    withAnimation(.spring) {
        showDetail.toggle()
    }
}
if showDetail {
    DetailView()
        .transition(.scale.combined(with: .opacity))
}

// BAD - animation inside conditional (removed with view!)
if showDetail {
    DetailView()
        .transition(.slide)
        .animation(.spring, value: showDetail)  // Won't work on removal!
}

// BAD - no animation context
Button("Toggle") {
    showDetail.toggle()  // No animation
}
if showDetail {
    DetailView()
        .transition(.slide)  // Ignored - just appears/disappears
}
```

### Built-in Transitions

| Transition | Effect |
|------------|--------|
| `.opacity` | Fade in/out (default) |
| `.scale` | Scale up/down |
| `.slide` | Slide from leading edge |
| `.move(edge:)` | Move from specific edge |
| `.offset(x:y:)` | Move by offset amount |

### Combining Transitions

```swift
// Parallel - both simultaneously
.transition(.slide.combined(with: .opacity))

// Chained
.transition(.scale.combined(with: .opacity).combined(with: .offset(y: 20)))
```

---

## Asymmetric Transitions

Different animations for insertion vs removal.

```swift
// GOOD - different animations for insert/remove
if showCard {
    CardView()
        .transition(
            .asymmetric(
                insertion: .scale.combined(with: .opacity),
                removal: .move(edge: .bottom).combined(with: .opacity)
            )
        )
}

// BAD - same transition when different behaviors needed
if showCard {
    CardView()
        .transition(.slide)  // Same both ways - may feel awkward
}
```

---

## Custom Transitions

### Pre-iOS 17

```swift
struct BlurModifier: ViewModifier {
    var radius: CGFloat
    func body(content: Content) -> some View {
        content.blur(radius: radius)
    }
}

extension AnyTransition {
    static func blur(radius: CGFloat) -> AnyTransition {
        .modifier(
            active: BlurModifier(radius: radius),
            identity: BlurModifier(radius: 0)
        )
    }
}

// Usage
.transition(.blur(radius: 10))
```

### iOS 17+ (Transition Protocol)

```swift
struct BlurTransition: Transition {
    var radius: CGFloat

    func body(content: Content, phase: TransitionPhase) -> some View {
        content
            .blur(radius: phase.isIdentity ? 0 : radius)
            .opacity(phase.isIdentity ? 1 : 0)
    }
}

// Usage
.transition(BlurTransition(radius: 10))
```

### Good vs Bad Custom Transitions

```swift
// GOOD - reusable transition
if showContent {
    ContentView()
        .transition(BlurTransition(radius: 10))
}

// BAD - inline logic (won't animate on removal!)
if showContent {
    ContentView()
        .blur(radius: showContent ? 0 : 10)  // Not a transition
        .opacity(showContent ? 1 : 0)
}
```

---

## Identity and Transitions

View identity changes trigger transitions, not property animations.

```swift
// Triggers transition - different branches have different identities
if isExpanded {
    Rectangle().frame(width: 200, height: 50)
} else {
    Rectangle().frame(width: 100, height: 50)
}

// Triggers transition - .id() changes identity
Rectangle()
    .id(flag)  // Different identity when flag changes
    .transition(.scale)

// Property animation - same view, same identity
Rectangle()
    .frame(width: isExpanded ? 200 : 100, height: 50)
    .animation(.spring, value: isExpanded)
```

---

## The Animatable Protocol

Enables custom property interpolation during animations.

### Protocol Definition

```swift
protocol Animatable {
    associatedtype AnimatableData: VectorArithmetic
    var animatableData: AnimatableData { get set }
}
```

### Basic Implementation

```swift
// GOOD - explicit animatableData
struct ShakeModifier: ViewModifier, Animatable {
    var shakeCount: Double

    var animatableData: Double {
        get { shakeCount }
        set { shakeCount = newValue }
    }

    func body(content: Content) -> some View {
        content.offset(x: sin(shakeCount * .pi * 2) * 10)
    }
}

extension View {
    func shake(count: Int) -> some View {
        modifier(ShakeModifier(shakeCount: Double(count)))
    }
}

// Usage
Button("Shake") { shakeCount += 3 }
    .shake(count: shakeCount)
    .animation(.default, value: shakeCount)

// BAD - missing animatableData (silent failure!)
struct BadShakeModifier: ViewModifier {
    var shakeCount: Double
    // Missing animatableData! Uses EmptyAnimatableData

    func body(content: Content) -> some View {
        content.offset(x: sin(shakeCount * .pi * 2) * 10)
    }
}
// Animation jumps to final value instead of interpolating
```

### Multiple Properties with AnimatablePair

```swift
// GOOD - AnimatablePair for two properties
struct ComplexModifier: ViewModifier, Animatable {
    var scale: CGFloat
    var rotation: Double

    var animatableData: AnimatablePair<CGFloat, Double> {
        get { AnimatablePair(scale, rotation) }
        set {
            scale = newValue.first
            rotation = newValue.second
        }
    }

    func body(content: Content) -> some View {
        content
            .scaleEffect(scale)
            .rotationEffect(.degrees(rotation))
    }
}

// GOOD - nested AnimatablePair for 3+ properties
struct ThreePropertyModifier: ViewModifier, Animatable {
    var x: CGFloat
    var y: CGFloat
    var rotation: Double

    var animatableData: AnimatablePair<AnimatablePair<CGFloat, CGFloat>, Double> {
        get { AnimatablePair(AnimatablePair(x, y), rotation) }
        set {
            x = newValue.first.first
            y = newValue.first.second
            rotation = newValue.second
        }
    }

    func body(content: Content) -> some View {
        content
            .offset(x: x, y: y)
            .rotationEffect(.degrees(rotation))
    }
}
```

---

## Quick Reference

### Do
- Place transitions outside conditional structures
- Use `withAnimation` or `.animation` outside the `if`
- Implement `animatableData` explicitly for custom Animatable
- Use `AnimatablePair` for multiple animated properties
- Use asymmetric transitions when insert/remove need different effects

### Don't
- Put animation modifiers inside conditionals for transitions
- Forget `animatableData` implementation (silent failure)
- Use inline blur/opacity instead of proper transitions
- Expect property animation when view identity changes
```

## File: `swiftui-expert-skill/references/charts-accessibility.md`
```markdown
# Swift Charts Accessibility, Fallback, and Resources

## Table of Contents

- [Accessibility](#accessibility)
  - [Meaningful Labels](#meaningful-labels)
  - [Custom Audio Graphs](#custom-audio-graphs)
- [Composite Example](#composite-example)
- [Fallback Strategies](#fallback-strategies)
  - [Version Breakdown](#version-breakdown)
- [WWDC Sessions](#wwdc-sessions)
- [Summary Checklist](#summary-checklist)

---

## Accessibility

Swift Charts provides built-in accessibility support. VoiceOver users get three rotor actions automatically:

- **Describe Chart** — overview of axes and data series
- **Audio Graph** — sonification where pitch represents data values
- **Chart Detail** — interactive mode for exploring individual data points

### Meaningful Labels

**Always** use clear, descriptive strings in `.value(_, _)` calls. These labels are read by VoiceOver and used in the Audio Graph.

```swift
// Good — descriptive labels
LineMark(
    x: .value("Date", entry.date),
    y: .value("Daily Steps", entry.count)
)

// Bad — generic labels
LineMark(
    x: .value("X", entry.date),
    y: .value("Y", entry.count)
)
```

### Custom Audio Graphs

For advanced accessibility, conform your chart view to `AXChartDescriptorRepresentable` and implement `makeChartDescriptor()`. Attach it with `.accessibilityChartDescriptor(self)`.

```swift
struct StepsChart: View, AXChartDescriptorRepresentable {
    let steps: [DailySteps]

    var body: some View {
        Chart(steps) { day in
            LineMark(x: .value("Date", day.date), y: .value("Steps", day.count))
        }
        .accessibilityChartDescriptor(self)
    }

    func makeChartDescriptor() -> AXChartDescriptor {
        guard let first = steps.first, let last = steps.last else {
            return AXChartDescriptor(title: "Daily Step Count", summary: nil,
                xAxis: AXNumericDataAxisDescriptor(title: "Date", range: 0...1, gridlinePositions: []) { "\($0)" },
                yAxis: AXNumericDataAxisDescriptor(title: "Steps", range: 0...1, gridlinePositions: []) { "\($0)" },
                additionalAxes: [], series: [])
        }
        let xAxis = AXDateDataAxisDescriptor(
            title: "Date", range: first.date...last.date, gridlinePositions: [])
        let yAxis = AXNumericDataAxisDescriptor(
            title: "Steps", range: 0...Double(steps.map(\.count).max() ?? 0),
            gridlinePositions: []) { "\(Int($0)) steps" }
        let series = AXDataSeriesDescriptor(
            name: "Daily Steps", isContinuous: true,
            dataPoints: steps.map { .init(x: $0.date, y: Double($0.count)) })
        return AXChartDescriptor(title: "Daily Step Count", summary: nil,
            xAxis: xAxis, yAxis: yAxis, additionalAxes: [], series: [series])
    }
}
```

## Composite Example

A scrollable bar chart with range selection combining multiple iOS 17+ APIs:

```swift
@State private var selectedRange: ClosedRange<Int>?

Chart(weeklyRevenue) { week in
    BarMark(x: .value("Week", week.index), y: .value("Revenue", week.revenue))
        .foregroundStyle(by: .value("Region", week.region))
}
.chartScrollableAxes(.horizontal)
.chartXVisibleDomain(length: 8)
.chartXSelection(range: $selectedRange)
.chartXAxis {
    AxisMarks(values: .stride(by: 1)) {
        AxisGridLine()
        AxisValueLabel { Text("W\($0.as(Int.self) ?? 0)") }
    }
}
```

## Fallback Strategies

Gate advanced APIs with `#available` and provide a fallback chart without the gated features. Because chart modifiers like `.chartXSelection` change the return type, you must duplicate the entire `Chart` — you cannot conditionally apply the modifier:

### Version Breakdown

- iOS 16+: `Chart`, custom axes, scales, `BarMark`, `LineMark`, `AreaMark`, `PointMark`, `RectangleMark`, `RuleMark`, `ChartProxy`, `chartOverlay`, `chartBackground`
- iOS 17+: `SectorMark`, `chartXSelection`, `chartYSelection`, `chartAngleSelection`, `chartScrollableAxes`, visible-domain scrolling APIs, `chartGesture`
- iOS 18+: `AreaPlot`, `BarPlot`, `LinePlot`, `PointPlot`, `RectanglePlot`, `RulePlot`, `SectorPlot`, function plotting
- iOS 26+: `Chart3D`, `SurfacePlot`, Z-axis marks, 3D camera and pose APIs

## WWDC Sessions

- [Hello Swift Charts](https://developer.apple.com/videos/play/wwdc2022/10136/) (WWDC 2022) — introduction to the framework
- [Swift Charts: Raise the bar](https://developer.apple.com/videos/play/wwdc2022/10137/) (WWDC 2022) — marks, composition, customization
- [Design an effective chart](https://developer.apple.com/videos/play/wwdc2022/110340/) (WWDC 2022) — chart design principles
- [Design app experiences with charts](https://developer.apple.com/videos/play/wwdc2022/110342/) (WWDC 2022) — integrating charts into app UX
- [Explore pie charts and interactivity in Swift Charts](https://developer.apple.com/videos/play/wwdc2023/10037/) (WWDC 2023) — SectorMark, selection, scrolling
- [Swift Charts: Vectorized and function plots](https://developer.apple.com/videos/play/wwdc2024/10155/) (WWDC 2024) — LinePlot, AreaPlot, function plotting
- [Bring Swift Charts to the third dimension](https://developer.apple.com/videos/play/wwdc2025/313/) (WWDC 2025) — Chart3D, SurfacePlot, 3D marks

## Summary Checklist

- [ ] `import Charts` is present in files using chart types
- [ ] Deployment target matches the APIs used (`Chart` on iOS 16+, selection and `SectorMark` on iOS 17+, plot types on iOS 18+, `Chart3D` on iOS 26+)
- [ ] Chart data models use `Identifiable` (or `Chart(data, id:)` is provided)
- [ ] All chart families are represented with the correct mark type
- [ ] Axes use `AxisMarks` when default ticks are too dense or unclear
- [ ] `chartXScale` or `chartYScale` is set when fixed domains matter
- [ ] Chart-wide modifiers are applied to `Chart`, not individual marks
- [ ] `foregroundStyle(by:)` used for categorical series (not manual per-mark colors)
- [ ] Single-value selection uses `chartXSelection(value:)` or `chartYSelection(value:)`
- [ ] Range selection uses `chartXSelection(range:)` or `chartYSelection(range:)`
- [ ] `SectorMark` selection uses `chartAngleSelection(value:)`
- [ ] iOS 17+, iOS 18+, and iOS 26+ APIs are guarded with `#available`
- [ ] `.value()` labels are descriptive for VoiceOver and Audio Graph accessibility
```

## File: `swiftui-expert-skill/references/charts.md`
```markdown
# SwiftUI Charts Reference

## Table of Contents

- [Overview](#overview)
- [Availability](#availability)
- [Core APIs](#core-apis)
- [Chart Types](#chart-types)
- [Axis Tweaks](#axis-tweaks)
- [Selection APIs](#selection-apis)
- [Annotations](#annotations)
- [ChartProxy and Custom Touch Handling](#chartproxy-and-custom-touch-handling)
- [Modifier Scope](#modifier-scope)
- [Styling and Visual Channels](#styling-and-visual-channels)
- [Composing Multiple Marks](#composing-multiple-marks)
- [Animating Chart Data](#animating-chart-data)
- [Best Practices](#best-practices)

## Overview

Swift Charts is Apple's native charting framework for SwiftUI. Use `Chart` with one or more marks to build bar, line, area, point, rule, rectangle, and sector charts. This reference covers the standard 2D chart APIs, axis customization, built-in selection APIs, annotations, and custom touch handling.

## Availability

Base `Chart`, custom axes, scales, and most marks require iOS 16 or later.

- `BarMark`, `LineMark`, `AreaMark`, `PointMark`, `RectangleMark`, and `RuleMark` are available on iOS 16+
- `SectorMark`, built-in selection, and scrollable chart axes require iOS 17+
- Data-driven plot types such as `BarPlot` and `LinePlot` require iOS 18+
- Chart3D and Z-axis APIs exist on iOS 26+; this reference is primarily about 2D `Chart`, with a dedicated Chart3D section below

```swift
if #available(iOS 17, *) {
    // Selection, SectorMark, scrollable axes
} else {
    // Base Chart, axes, scales, and core marks
}
```

## Core APIs

### Import the Framework

Always check that the file imports `Charts` before using `Chart`, `Chart3D`, `BarMark`, `SectorMark`, or `ChartProxy`.

```swift
import SwiftUI
import Charts
```

If chart types are unresolved, the first thing to verify is that `Charts` is imported in that file.

### Chart Container

`Chart` is the root view. Add one or more marks inside it.

```swift
Chart(sales) { item in
    BarMark(
        x: .value("Month", item.month),
        y: .value("Revenue", item.revenue)
    )
}
```

### Data Models Should Be Identifiable

Prefer `Identifiable` models for chart data so identity stays stable as data changes.

```swift
struct SalesPoint: Identifiable {
    let id: UUID
    let month: String
    let revenue: Double
}
```

If your model cannot conform to `Identifiable`, provide an explicit id key path:

```swift
Chart(sales, id: \.month) { item in
    BarMark(
        x: .value("Month", item.month),
        y: .value("Revenue", item.revenue)
    )
}
```

### Plottable Values

Use `.value(_, _)` to describe what each axis value means. Those labels are reused by axes, legends, and accessibility.

```swift
LineMark(
    x: .value("Day", entry.date),
    y: .value("Steps", entry.count)
)
```

## Chart Types

### BarMark

```swift
BarMark(
    x: .value("Product", product.name),
    y: .value("Units", product.units)
)
```

Stacking via `MarkStackingMethod`: `.standard`, `.normalized`, `.center`, `.unstacked`.

### LineMark

```swift
LineMark(
    x: .value("Day", day.date),
    y: .value("Steps", day.count)
)
.interpolationMethod(.monotone)
```

Interpolation methods: `.linear`, `.monotone`, `.cardinal`, `.catmullRom`, `.stepStart`, `.stepCenter`, `.stepEnd`. Cardinal and Catmull-Rom accept optional tension/alpha parameters.

### AreaMark

```swift
AreaMark(
    x: .value("Hour", sample.hour),
    y: .value("Temperature", sample.value),
    stacking: .unstacked
)
```

Ranged areas use `yStart`/`yEnd` for bands like min/max or confidence intervals:

```swift
AreaMark(
    x: .value("Day", sample.day),
    yStart: .value("Low", sample.low),
    yEnd: .value("High", sample.high)
)
```

### PointMark

```swift
PointMark(
    x: .value("Time", measurement.time),
    y: .value("Value", measurement.value)
)
```

### RectangleMark

```swift
RectangleMark(
    xStart: .value("Start Day", cell.startDay),
    xEnd: .value("End Day", cell.endDay),
    yStart: .value("Low", cell.low),
    yEnd: .value("High", cell.high)
)
```

### RuleMark

```swift
RuleMark(y: .value("Goal", 10_000))
    .foregroundStyle(.red)
```

### SectorMark

Use `SectorMark` for pie and donut-style charts. `SectorMark` requires iOS 17 or later.

```swift
Chart(expenses) { expense in
    SectorMark(
        angle: .value("Amount", expense.amount),
        innerRadius: .ratio(0.6),
        angularInset: 2
    )
    .foregroundStyle(by: .value("Category", expense.category))
}
```

Use `innerRadius` to turn a pie chart into a donut chart, and `angularInset` to separate slices visually.

### Plot Types (iOS 18+)

iOS 18 adds data-driven plot wrappers: `AreaPlot`, `BarPlot`, `LinePlot`, `PointPlot`, `RectanglePlot`, `RulePlot`, and `SectorPlot`.

`LinePlot` and `AreaPlot` also accept function closures for plotting mathematical functions without discrete data:

```swift
if #available(iOS 18, *) {
    Chart {
        LinePlot(x: "x", y: "sin(x)") { x in
            sin(x)
        }
    }
    .chartXScale(domain: -Double.pi ... Double.pi)
    .chartYScale(domain: -1.5 ... 1.5)
}
```

Use plot types when you want a data-first API surface or need function plotting. The underlying chart families stay the same.

### Chart3D (iOS 26+)

`Chart3D` is a separate API for 3D chart content. It supports 3D `PointMark`, `RectangleMark`, `RuleMark`, and `SurfacePlot`.

```swift
if #available(iOS 26, *) {
    Chart3D(points) { point in
        PointMark(
            x: .value("X", point.x),
            y: .value("Y", point.y),
            z: .value("Z", point.z)
        )
    }
    .chart3DPose(.front)
    .chart3DCameraProjection(.perspective)
}
```

`SurfacePlot` visualizes mathematical surfaces by evaluating a two-variable function:

```swift
if #available(iOS 26, *) {
    Chart3D {
        SurfacePlot(x: "x", y: "height", z: "z") { x, z in
            sin(x) * cos(z)
        }
    }
    .chartXScale(domain: -Double.pi ... Double.pi)
    .chartZScale(domain: -Double.pi ... Double.pi)
}
```

Camera and pose configuration:

- **Projection**: `.chart3DCameraProjection(.orthographic)` (default, precise measurements) or `.perspective` (depth effect)
- **Pose presets**: `.chart3DPose(.default)`, `.front`, `.back`, `.left`, `.right`
- **Custom pose**: `.chart3DPose(azimuth: .degrees(45), inclination: .degrees(30))`
- On visionOS, Chart3D supports natural 3D interaction gestures for rotation and exploration

**Always** gate `Chart3D` with `#available(iOS 26, *)` — it is not available on earlier OS versions.

## Axis Tweaks

### Axis Visibility and Labels

Use `chartXAxis`, `chartYAxis`, `chartXAxisLabel`, and `chartYAxisLabel` on the `Chart` container.
Axis visibility supports `.automatic`, `.visible`, and `.hidden`.

```swift
Chart(data) { item in
    BarMark(
        x: .value("Month", item.month),
        y: .value("Revenue", item.revenue)
    )
}
.chartXAxis(.visible)
.chartYAxis(.hidden)
.chartXAxisLabel("Month")
.chartYAxisLabel("Revenue")
```

### Custom Axis Marks

Use `AxisMarks` to control tick placement, labels, and grid lines.

```swift
Chart(steps) { day in
    LineMark(
        x: .value("Day", day.date),
        y: .value("Steps", day.count)
    )
}
.chartXAxis {
    AxisMarks(
        preset: .aligned,
        position: .bottom,
        values: .stride(by: .day)
    ) {
        AxisGridLine()
        AxisTick(length: .label)
        AxisValueLabel(format: .dateTime.weekday(.abbreviated))
    }
}
```

Useful `AxisMarks` inputs:

- `preset`: `.automatic`, `.extended`, `.aligned`, `.inset`
- `position`: `.automatic`, `.leading`, `.trailing`, `.top`, `.bottom`
- `values`: `.automatic`, `.automatic(desiredCount:)`, `.stride(by:)`, `.stride(by:count:)`, or an explicit array

### Axis Components

Within `AxisMarks`, combine the built-in axis components as needed:

```swift
AxisGridLine()
AxisTick()
AxisValueLabel()
```

`AxisValueLabel` can be tuned for dense axes:

```swift
AxisValueLabel(
    collisionResolution: .greedy(minimumSpacing: 8),
    orientation: .vertical
)
```

Label orientations: `.automatic`, `.horizontal`, `.vertical`, `.verticalReversed`.

Collision strategies: `.automatic`, `.greedy`, `.greedy(priority:minimumSpacing:)`, `.truncate`, `.disabled`.

### Axis Domains and Plot Area Tweaks

Use scales when you need explicit axis domains or plot area control.

```swift
Chart(data) { item in
    LineMark(
        x: .value("Index", item.index),
        y: .value("Score", item.score)
    )
}
.chartXScale(domain: 0...30)
.chartYScale(domain: 0...100)
.chartPlotStyle { plotArea in
    plotArea
        .background(.gray.opacity(0.08))
}
```

You can set one axis domain without forcing the other:

```swift
.chartXScale(domain: startDate...endDate)
```

### Scrollable Axes (iOS 17+)

For larger datasets, make the plot area scroll and control the visible domain.

```swift
@State private var scrollX = 7

Chart(data) { item in
    BarMark(
        x: .value("Day", item.day),
        y: .value("Value", item.value)
    )
}
.chartScrollableAxes(.horizontal)
.chartXVisibleDomain(length: 7)
.chartScrollPosition(x: $scrollX)
```

## Selection APIs

### Single-Value Selection

Use `chartXSelection(value:)` or `chartYSelection(value:)` for one selected value.

```swift
@State private var selectedDate: Date?

Chart(steps) { day in
    LineMark(x: .value("Day", day.date), y: .value("Steps", day.count))

    if let selectedDate {
        RuleMark(x: .value("Selected Day", selectedDate))
            .foregroundStyle(.secondary)
    }
}
.chartXSelection(value: $selectedDate)
```

### Range Selection

Use `chartXSelection(range:)` or `chartYSelection(range:)` for a dragged range. Bind to a `ClosedRange` whose bound type matches the plotted axis value.

```swift
@State private var selectedWeeks: ClosedRange<Int>?

Chart(weeks) { week in
    BarMark(x: .value("Week", week.index), y: .value("Revenue", week.revenue))
}
.chartXSelection(range: $selectedWeeks)
```

### Choosing Single vs Range

- Use `value:` bindings when only one point or axis value should be selected.
- Use `range:` bindings when users should brush a span (for zoom windows, comparisons, or grouped summaries).

### Angle Selection

Use `chartAngleSelection(value:)` with `SectorMark` charts. No built-in range overload for angle selection.

```swift
@State private var selectedAmount: Double?

Chart(expenses) { expense in
    SectorMark(angle: .value("Amount", expense.amount))
        .foregroundStyle(by: .value("Category", expense.category))
}
.chartAngleSelection(value: $selectedAmount)
```

**Important**: Selection bindings return the plottable axis value, not the full data element. Map back to your model if you need the selected record.

## Annotations

Use `annotation(position:)` on a mark when you need labels, callouts, or highlighted values attached to the plotted content.

```swift
BarMark(
    x: .value("Month", item.month),
    y: .value("Revenue", item.revenue)
)
.annotation(position: .top) {
    Text(item.revenue.formatted())
}
```

This is useful for selected values, thresholds, summaries, and direct labeling. Common positions include `.overlay`, `.top`, `.bottom`, `.leading`, and `.trailing`.

## ChartProxy and Custom Touch Handling

Use `chartOverlay`/`chartBackground` (iOS 16+) or `chartGesture` (iOS 17+) with `ChartProxy` when built-in selection modifiers are not enough.

```swift
.chartOverlay { proxy in
    GeometryReader { geometry in
        Rectangle().fill(.clear).contentShape(Rectangle())
            .gesture(
                DragGesture(minimumDistance: 0)
                    .onChanged { value in
                        guard let plotFrame = proxy.plotFrame else { return } // iOS 16: use proxy.plotAreaFrame
                        let frame = geometry[plotFrame]
                        let x = value.location.x - frame.origin.x
                        guard x >= 0, x <= frame.size.width else { return }
                        selectedDate = proxy.value(atX: x, as: Date.self)
                    }
                    .onEnded { _ in selectedDate = nil }
            )
    }
}
```

Use `proxy.plotFrame` (iOS 17+) or `proxy.plotAreaFrame` (iOS 16) to get the plot area anchor.

`ChartProxy` gives you lower-level access to:

- `value(atX:as:)`, `value(atY:as:)`, and `value(at:as:)` for converting gesture coordinates into chart values
- `position(forX:)`, `position(forY:)`, and `position(for:)` for placing custom overlays or indicators
- `selectXValue(at:)`, `selectYValue(at:)`, `selectXRange(from:to:)`, and `selectYRange(from:to:)` for driving built-in selection from custom gestures
- `plotFrame` (iOS 17+) or `plotAreaFrame` (iOS 16) with `plotSize` for converting between gesture coordinates and the plot area

`select*` ChartProxy selection methods and `chartGesture` are available on iOS 17+.

## Modifier Scope

Apply chart-wide modifiers to the `Chart` container and mark-specific modifiers to the individual mark.

```swift
Chart(data) { item in
    LineMark(
        x: .value("Day", item.date),
        y: .value("Value", item.value)
    )
    .interpolationMethod(.monotone)   // Mark-level modifier
}
.chartXAxis { AxisMarks() }            // Chart-level modifier
.chartYScale(domain: 0...100)          // Chart-level modifier
.chartPlotStyle { $0.background(.thinMaterial) }
```

## Styling and Visual Channels

### Categorical Coloring

Use `foregroundStyle(by: .value(...))` to color marks by a data property. Swift Charts generates a legend automatically.

```swift
Chart(sales) { item in
    BarMark(
        x: .value("Month", item.month),
        y: .value("Revenue", item.revenue)
    )
    .foregroundStyle(by: .value("Region", item.region))
}
```

**Avoid** applying `.foregroundStyle(.red)` per mark for categorical data — this suppresses the automatic legend and breaks accessibility.

### Custom Color Scales

Use `chartForegroundStyleScale` to control the mapping from data values to colors.

```swift
.chartForegroundStyleScale([
    "North": .blue,
    "South": .orange,
    "East": .green
])
```

For dynamic data where not all series appear at every point, use the mapping overload:

```swift
.chartForegroundStyleScale(domain: regions, mapping: { region in
    colorForRegion(region)
})
```

### Symbol and Size Channels

Use `symbol(by:)` and `symbolSize(by:)` to encode additional data dimensions on `PointMark` and `LineMark`.

```swift
Chart(measurements) { item in
    PointMark(
        x: .value("Time", item.time),
        y: .value("Value", item.value)
    )
    .foregroundStyle(by: .value("Category", item.category))
    .symbol(by: .value("Category", item.category))
    .symbolSize(by: .value("Weight", item.weight))
}
```

### Legend Control

```swift
.chartLegend(.visible)
.chartLegend(.hidden)
.chartLegend(position: .bottom, alignment: .center)
```

## Composing Multiple Marks

Combine different mark types inside the same `Chart` closure:

```swift
// Line with points
LineMark(x: .value("Day", day.date), y: .value("Steps", day.count))
    .interpolationMethod(.monotone)
PointMark(x: .value("Day", day.date), y: .value("Steps", day.count))

// Bars with threshold line
BarMark(x: .value("Month", item.month), y: .value("Revenue", item.revenue))
RuleMark(y: .value("Target", 10_000))
    .foregroundStyle(.red)
    .lineStyle(StrokeStyle(dash: [5, 3]))
```

## Animating Chart Data

Chart marks animate automatically when data identity is stable and changes are wrapped in an animation.

```swift
withAnimation(.easeInOut) {
    chartData = updatedData
}
```

**Always** use `Identifiable` models (or explicit `id:`) so Swift Charts can match old and new data points and animate transitions between them.

## Best Practices

### Do

- Use semantic `.value(_, _)` labels so axes and accessibility read clearly
- Prefer `Identifiable` models (or explicit `id:`) for stable chart data identity
- Use `foregroundStyle(by:)` for categorical series to get automatic legends and accessibility
- Use `RuleMark` for goals, thresholds, and selected-value indicators
- Use explicit `AxisMarks(values:)` when automatic tick generation gets crowded
- Use `chartXScale` and `chartYScale` when you need stable visual comparisons
- Use `chartXSelection(range:)` or `chartYSelection(range:)` for brushed selection
- Gate iOS 17+ APIs such as `SectorMark` and selection with `#available`

### Don't

- Put chart-wide modifiers such as `chartXAxis` or `chartXSelection` on individual marks
- Apply manual `.foregroundStyle(.color)` per mark for categorical data — use `foregroundStyle(by:)` instead
- Rely on unstable identities when chart data can be inserted, removed, or reordered
- Use string values for naturally numeric or date-based axes unless you want categorical behavior
- Stack unrelated series by default just because `BarMark` and `AreaMark` allow it
- Force every tick label to display when collision handling or stride values would be clearer
- Assume selection returns a model object; it only returns the plottable axis value
- Forget that range selection is available only for X and Y axes, not angle selection

For chart accessibility (VoiceOver, Audio Graph, `AXChartDescriptorRepresentable`), fallback strategies, WWDC sessions, and a full summary checklist, see `charts-accessibility.md`.
```

## File: `swiftui-expert-skill/references/image-optimization.md`
```markdown
# SwiftUI Image Optimization Reference

## Table of Contents

- [AsyncImage Best Practices](#asyncimage-best-practices)
- [Image Decoding and Downsampling (Optional Optimization)](#image-decoding-and-downsampling-optional-optimization)
- [UIImage Loading and Memory](#uiimage-loading-and-memory)
- [SF Symbols](#sf-symbols)
- [Summary Checklist](#summary-checklist)

## AsyncImage Best Practices

### Basic AsyncImage with Phase Handling

```swift
// Good - handles loading and error states
AsyncImage(url: imageURL) { phase in
    switch phase {
    case .empty:
        ProgressView()
    case .success(let image):
        image
            .resizable()
            .aspectRatio(contentMode: .fit)
    case .failure:
        Image(systemName: "photo")
            .foregroundStyle(.secondary)
    @unknown default:
        EmptyView()
    }
}
.frame(width: 200, height: 200)
```

For custom placeholders, replace `ProgressView()` in the `.empty` case with your placeholder view. Add `.transition(.opacity)` to the success case and `.animation(.easeInOut, value: imageURL)` to the container for fade-in transitions.

## Image Decoding and Downsampling (Optional Optimization)

**When you encounter `UIImage(data:)` usage, consider suggesting image downsampling as a potential performance improvement**, especially for large images in lists or grids.

### Current Pattern That Could Be Optimized

```swift
// Current pattern - decodes full image on main thread
// Unsafe - force unwrap can crash if imageData is invalid
Image(uiImage: UIImage(data: imageData)!)
    .resizable()
    .aspectRatio(contentMode: .fit)
    .frame(width: 200, height: 200)
```

### Suggested Optimization Pattern

```swift
// Suggested optimization - decode and downsample off main thread
struct OptimizedImageView: View {
    let imageData: Data
    let targetSize: CGSize
    @State private var processedImage: UIImage?
    
    var body: some View {
        Group {
            if let processedImage {
                Image(uiImage: processedImage)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
            } else {
                ProgressView()
            }
        }
        .task {
            processedImage = await decodeAndDownsample(imageData, targetSize: targetSize)
        }
    }
    
    private func decodeAndDownsample(_ data: Data, targetSize: CGSize) async -> UIImage? {
        await Task.detached {
            guard let source = CGImageSourceCreateWithData(data as CFData, nil) else {
                return nil
            }
            
            let options: [CFString: Any] = [
                kCGImageSourceThumbnailMaxPixelSize: max(targetSize.width, targetSize.height),
                kCGImageSourceCreateThumbnailFromImageAlways: true,
                kCGImageSourceCreateThumbnailWithTransform: true
            ]
            
            guard let cgImage = CGImageSourceCreateThumbnailAtIndex(source, 0, options as CFDictionary) else {
                return nil
            }
            
            return UIImage(cgImage: cgImage)
        }.value
    }
}

// Usage
OptimizedImageView(
    imageData: imageData,
    targetSize: CGSize(width: 200, height: 200)
)
```

### Reusable Downsampling Actor

For production use, wrap the logic in an `actor` with scale-aware sizing and cache-disabled source options:

```swift
actor ImageProcessor {
    func downsample(data: Data, targetSize: CGSize) -> UIImage? {
        let scale = await UIScreen.main.scale
        let maxPixel = max(targetSize.width, targetSize.height) * scale
        let sourceOptions: [CFString: Any] = [kCGImageSourceShouldCache: false]
        guard let source = CGImageSourceCreateWithData(data as CFData, sourceOptions as CFDictionary) else { return nil }
        let downsampleOptions: [CFString: Any] = [
            kCGImageSourceCreateThumbnailFromImageAlways: true,
            kCGImageSourceThumbnailMaxPixelSize: maxPixel,
            kCGImageSourceCreateThumbnailWithTransform: true,
            kCGImageSourceShouldCacheImmediately: true
        ]
        guard let cgImage = CGImageSourceCreateThumbnailAtIndex(source, 0, downsampleOptions as CFDictionary) else { return nil }
        return UIImage(cgImage: cgImage)
    }
}
```

Key details: `kCGImageSourceShouldCache: false` on the source prevents the full-resolution image from being cached in memory. Multiplying `targetSize` by `UIScreen.main.scale` ensures the thumbnail is sharp on Retina displays. `kCGImageSourceShouldCacheImmediately: true` on the thumbnail forces decoding at creation time rather than at first render.

### When to Suggest This Optimization

Mention this optimization when you see `UIImage(data:)` usage, particularly in:
- Scrollable content (List, ScrollView with LazyVStack/LazyHStack)
- Grid layouts with many images
- Image galleries or carousels
- Any scenario where large images are displayed at smaller sizes

**Don't automatically apply it**—present it as an optional improvement for performance-sensitive scenarios.

## UIImage Loading and Memory

### UIImage(named:) Caches in System Cache

`UIImage(named:)` adds images to the system cache, which can cause memory spikes when loading many images (e.g., in a slider or gallery). For single-use or frequently-rotated images, use `UIImage(contentsOfFile:)` to bypass the cache:

```swift
// Caches in system cache -- memory builds up
let image = UIImage(named: "Wallpapers/image_001.jpg")

// No system caching -- memory stays flat
guard let path = Bundle.main.path(forResource: "Wallpapers/image_001.jpg", ofType: nil) else { return nil }
let image = UIImage(contentsOfFile: path)
```

### NSCache for Controlled Image Caching

When image processing (resizing, filtering) is needed, use `NSCache` with a `countLimit` to bound memory instead of relying on system caching:

```swift
struct ImageCache {
    private let cache = NSCache<NSString, UIImage>()

    init(countLimit: Int = 50) {
        cache.countLimit = countLimit
    }

    subscript(key: String) -> UIImage? {
        get { cache.object(forKey: key as NSString) }
        nonmutating set {
            if let newValue {
                cache.setObject(newValue, forKey: key as NSString)
            } else {
                cache.removeObject(forKey: key as NSString)
            }
        }
    }
}
```

## SF Symbols

```swift
Image(systemName: "star.fill")
    .foregroundStyle(.yellow)
    .symbolRenderingMode(.multicolor)     // or .hierarchical, .palette, .monochrome

// Animated symbols (iOS 17+)
Image(systemName: "antenna.radiowaves.left.and.right")
    .symbolEffect(.variableColor)
```

Variants are available via naming convention: `star.circle.fill`, `star.square.fill`, `folder.badge.plus`.

## Summary Checklist

- [ ] Use `AsyncImage` with proper phase handling
- [ ] Handle empty, success, and failure states
- [ ] Consider downsampling for `UIImage(data:)` in performance-sensitive scenarios
- [ ] Decode and downsample images off the main thread
- [ ] Use appropriate target sizes for downsampling
- [ ] Consider image caching for frequently accessed images
- [ ] Use SF Symbols with appropriate rendering modes

**Performance Note**: Image downsampling is an optional optimization. Only suggest it when you encounter `UIImage(data:)` usage in performance-sensitive contexts like scrollable lists or grids.
```

## File: `swiftui-expert-skill/references/latest-apis.md`
```markdown
# Latest SwiftUI APIs Reference

> Based on a comparison of Apple's documentation using the Sosumi MCP, we found the latest recommended APIs to use.

## Table of Contents
- [Always Use (iOS 15+)](#always-use-ios-15)
- [When Targeting iOS 16+](#when-targeting-ios-16)
- [When Targeting iOS 17+](#when-targeting-ios-17)
- [When Targeting iOS 18+](#when-targeting-ios-18)
- [When Targeting iOS 26+](#when-targeting-ios-26)

---

## Always Use (iOS 15+)

These APIs have been deprecated long enough that there is no reason to use the old variants.

### Compact Replacements

These replacements have minimal API shape changes. Most are near-direct swaps; a few require an additional parameter or structural adjustment:

- **`navigationTitle(_:)`** instead of `navigationBarTitle(_:)`
- **`toolbar { ToolbarItem(...) }`** instead of `navigationBarItems(...)` (structural change)
- **`toolbarVisibility(.hidden, for: .navigationBar)`** instead of `navigationBarHidden(_:)`
- **`statusBarHidden(_:)`** instead of `statusBar(hidden:)`
- **`ignoresSafeArea(_:edges:)`** instead of `edgesIgnoringSafeArea(_:)`
- **`preferredColorScheme(_:)`** instead of `colorScheme(_:)`
- **`foregroundStyle(_:)`** instead of `foregroundColor(_:)` (e.g., `.foregroundStyle(.primary)`)
- **`clipShape(.rect(cornerRadius:))`** instead of `cornerRadius()`
- **`textInputAutocapitalization(_:)`** instead of `autocapitalization(_:)` (note: `.never` replaces `.none`)
- **`animation(_:value:)`** instead of `animation(_:)` (adds required `value:` parameter; back-deploys to iOS 13+)

### Presentation

- **Always use `.confirmationDialog(_:isPresented:actions:message:)`** instead of `actionSheet(...)`.
- **Always use `.alert(_:isPresented:actions:message:)`** instead of `alert(isPresented:content:)`.

Both take a title `String`, `isPresented: Binding<Bool>`, an `actions` builder with `Button` items (supporting `role: .destructive` / `.cancel`), and an optional `message` builder:

```swift
.alert("Delete Item?", isPresented: $showAlert) {
    Button("Delete", role: .destructive) { deleteItem() }
    Button("Cancel", role: .cancel) { }
} message: {
    Text("This action cannot be undone.")
}
```

### Text Input

**Always use `onSubmit(of:_:)` and `focused(_:equals:)` instead of `TextField` `onEditingChanged`/`onCommit` callbacks.**

```swift
@FocusState private var isFocused: Bool

TextField("Search", text: $query)
    .focused($isFocused)
    .onSubmit { performSearch() }
```

### Accessibility

**Always use dedicated accessibility modifiers instead of the generic `accessibility(...)` variants.** Use `.accessibilityLabel()`, `.accessibilityValue()`, `.accessibilityHint()`, `.accessibilityAddTraits()`, `.accessibilityHidden()` instead of `.accessibility(label:)`, `.accessibility(value:)`, etc.

### Custom Environment / Container Values

**Always use the `@Entry` macro instead of manual `EnvironmentKey` conformance.** The `@Entry` macro was introduced in Xcode 16 and back-deploys to all OS versions.

```swift
// Modern — one line replaces ~10 lines of EnvironmentKey boilerplate
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
}
```

### Styling

**Always use `Button` instead of `onTapGesture()` unless you need tap location or count.**

```swift
Button("Tap me") { performAction() }

// Use onTapGesture only when you need location or count
Image("photo")
    .onTapGesture(count: 2) { handleDoubleTap() }
```

---

## When Targeting iOS 16+

### Navigation

**Use `NavigationStack` (or `NavigationSplitView`) instead of `NavigationView`.** Value-based `NavigationLink(value:)` with `.navigationDestination(for:)` replaces destination-based links.

```swift
NavigationStack {
    List(items) { item in
        NavigationLink(value: item) { Text(item.name) }
    }
    .navigationDestination(for: Item.self) { DetailView(item: $0) }
}
```

### Simple Renames

- **`tint(_:)`** instead of `accentColor(_:)`
- **`autocorrectionDisabled(_:)`** instead of `disableAutocorrection(_:)`

### Clipboard

**Prefer `PasteButton` for user-initiated paste UI** to avoid paste prompts. It handles permissions automatically. Use `UIPasteboard` only when you need programmatic or non-`Transferable` clipboard access (triggers the paste permission prompt).

```swift
PasteButton(payloadType: String.self) { strings in
    pastedText = strings.first ?? ""
}
```

---

## When Targeting iOS 17+

### State Management

- **Prefer `@Observable` over `ObservableObject` for new code.** Use `@State` instead of `@StateObject`; use `@Bindable` instead of `@ObservedObject`. See `state-management.md` for full `@Observable` migration patterns.

### Events

**Use `onChange(of:initial:_:)` or `onChange(of:) { }` instead of `onChange(of:perform:)`.**

The deprecated variant passes only the new value. The modern variants provide either both old and new values, or a no-parameter closure.

- **No-parameter** (most common): `.onChange(of: value) { doSomething() }`
- **Old and new values**: `.onChange(of: value) { old, new in ... }`
- **With initial trigger**: `.onChange(of: value, initial: true) { ... }`
- **Deprecated**: `.onChange(of: value) { newValue in ... }` — single-parameter closure

### Gestures

- **`MagnifyGesture`** instead of `MagnificationGesture` (access magnitude via `value.magnification`)
- **`RotateGesture`** instead of `RotationGesture` (access angle via `value.rotation`)

### Layout

**Consider `containerRelativeFrame()` or `visualEffect()` as alternatives to `GeometryReader` for sizing and position-based effects.** `GeometryReader` is not deprecated and remains necessary for many measurement-based layouts.

```swift
Image("hero")
    .resizable()
    .containerRelativeFrame(.horizontal) { length, axis in length * 0.8 }
```

- **`visualEffect { content, geometry in ... }`** — position-based effects (parallax, offsets) without a `GeometryReader` wrapper.
- **`onGeometryChange(for:of:action:)`** — react to geometry changes of a specific view; useful for driving state/effects. `GeometryReader` is still better when layout itself depends on geometry. Note the two-closure shape:
  ```swift
  .onGeometryChange(for: CGFloat.self) { proxy in proxy.size.height } action: { newHeight in height = newHeight }
  ```
- **`.coordinateSpace(.named("scroll"))`** instead of `.coordinateSpace(name: "scroll")`.

---

## When Targeting iOS 18+

### Tabs

**Use the `Tab` API instead of `tabItem(_:)`.**

```swift
TabView {
    Tab("Home", systemImage: "house") { HomeView() }
    Tab("Search", systemImage: "magnifyingglass") { SearchView() }
    Tab("Profile", systemImage: "person") { ProfileView() }
}
```

When using `Tab(role:)`, all tabs must use the `Tab` syntax. Mixing `Tab(role:)` with `.tabItem()` causes compilation errors.

### Previews

**Use `@Previewable` for dynamic properties in previews.**

```swift
// Modern (iOS 18+)
#Preview {
    @Previewable @State var isOn = false
    Toggle("Setting", isOn: $isOn)
}
```

---

## When Targeting iOS 26+

For Liquid Glass APIs (`glassEffect`, `GlassEffectContainer`, glass button styles), see [liquid-glass.md](liquid-glass.md).

### Scroll Edge Effects

**Use `scrollEdgeEffectStyle(_:for:)` to configure scroll edge behavior.**

```swift
ScrollView {
    // content
}
.scrollEdgeEffectStyle(.soft, for: .top)
```

### Background Extension

**Use `backgroundExtensionEffect()` for edge-extending blurred backgrounds.**

Views behind a Liquid Glass sidebar can appear clipped. This modifier mirrors and blurs content outside the safe area so artwork remains visible.

```swift
Image("hero")
    .backgroundExtensionEffect()
```

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

### Tab Bar

**Use `tabBarMinimizeBehavior(_:)` to control tab bar minimization on scroll.**

```swift
TabView {
    // tabs
}
.tabBarMinimizeBehavior(.onScrollDown)
```

**Use `tabViewBottomAccessory` for persistent controls above the tab bar.** Read `tabViewBottomAccessoryPlacement` from the environment to adapt content when the accessory collapses into the tab bar area.

```swift
TabView {
    // tabs
}
.tabViewBottomAccessory {
    NowPlayingBar()
}
```

**Use `Tab(role: .search)` for a dedicated search tab.** The tab separates from the rest and morphs into a search field when selected.

```swift
TabView {
    Tab("Home", systemImage: "house") { HomeView() }
    Tab("Profile", systemImage: "person") { ProfileView() }
    Tab(role: .search) { SearchResultsView() }
}
```

> Source: "What's new in SwiftUI" (WWDC25, session 256) and "Build a SwiftUI app with the new design" (WWDC25, session 323)

### Toolbars

**Use `ToolbarSpacer` to control grouping of toolbar items.** Fixed spacers visually separate related groups; flexible spacers push items apart.

```swift
.toolbar {
    ToolbarItem(placement: .topBarTrailing) {
        Button("Up", systemImage: "chevron.up") { }
    }
    ToolbarItem(placement: .topBarTrailing) {
        Button("Down", systemImage: "chevron.down") { }
    }
    ToolbarSpacer(.fixed)
    ToolbarItem(placement: .topBarTrailing) {
        Button("Settings", systemImage: "gear") { }
    }
}
```

**Use `sharedBackgroundVisibility(.hidden)` to remove the glass group background from an individual toolbar item.**

```swift
ToolbarItem(placement: .topBarTrailing) {
    Image(systemName: "person.circle.fill")
        .sharedBackgroundVisibility(.hidden)
}
```

**Use `badge(_:)` on toolbar item content to display an indicator.**

```swift
ToolbarItem(placement: .topBarTrailing) {
    Button("Notifications", systemImage: "bell") { }
        .badge(unreadCount)
}
```

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

### Search

**Use `searchToolbarBehavior(.minimizable)` to opt into a minimized search button.** The system may automatically minimize search into a toolbar button depending on available space. Use this modifier to explicitly opt in.

```swift
NavigationStack {
    ContentView()
        .searchable(text: $query)
        .searchToolbarBehavior(.minimizable)
}
```

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

### Animations

**Use `@Animatable` macro instead of manual `animatableData` declarations.** The macro auto-synthesizes `animatableData` from all animatable properties. Use `@AnimatableIgnored` to exclude specific properties.

```swift
@Animatable
struct Wedge: Shape {
    var startAngle: Angle
    var endAngle: Angle
    @AnimatableIgnored var drawClockwise: Bool

    func path(in rect: CGRect) -> Path { /* ... */ }
}
```

> Source: "What's new in SwiftUI" (WWDC25, session 256)

### Presentations

**Use `navigationZoomTransition` to morph sheets out of their source view.** Toolbar items and buttons can serve as the transition source.

```swift
.toolbar {
    ToolbarItem {
        Button("Add", systemImage: "plus") { showSheet = true }
            .navigationTransitionSource(id: "addSheet", namespace: namespace)
    }
}
.sheet(isPresented: $showSheet) {
    AddItemView()
        .navigationTransitionDestination(id: "addSheet", namespace: namespace)
}
```

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

### Controls

**Use `controlSize(.extraLarge)` for extra-large prominent action buttons.**

```swift
Button("Get Started") { }
    .buttonStyle(.borderedProminent)
    .controlSize(.extraLarge)
```

**Use `concentric` corner style for buttons that match their container's corners.**

```swift
Button("Confirm") { }
    .clipShape(.rect(cornerRadius: 12, style: .concentric))
```

**Sliders now support tick marks and a neutral value.**

```swift
Slider(value: $speed, in: 0.5...2.0, step: 0.25) {
    Text("Speed")
} ticks: {
    SliderTick(value: 0.6)
    SliderTick(value: 0.9)
}
.sliderNeutralValue(1.0)
```

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

### Rich Text

**Use `TextEditor` with an `AttributedString` binding for rich text editing.** Supports bold, italic, underline, strikethrough, custom fonts, foreground/background colors, paragraph styles, and Genmoji.

```swift
@State private var text: AttributedString = "Hello, world!"

var body: some View {
    TextEditor(text: $text)
}
```

> Source: "Cook up a rich text experience in SwiftUI with AttributedString" (WWDC25, session 280)

### Web Content

**Use `WebView` to display web content.** For richer interaction, create a `WebPage` observable model.

```swift
// Simple URL display
WebView(url: URL(string: "https://example.com")!)

// With observable model
@State private var page = WebPage()

WebView(page)
    .onAppear { page.load(URLRequest(url: myURL)) }
    .navigationTitle(page.title ?? "")
```

> Source: "Meet WebKit for SwiftUI" (WWDC25, session 231)

### Drag and Drop

**Use `dragContainer` for multi-item drag operations.** Combine with `DragConfiguration` for custom drag behavior and `onDragSessionUpdated` to observe events.

```swift
PhotoGrid(photos: photos)
    .dragContainer(for: Photo.self) { selection in
        return selection.map { $0.transferable }
    }
    .onDragSessionUpdated { session in
        if session.phase == .endedWithDelete {
            deleteSelectedPhotos()
        }
    }
```

> Source: "What's new in SwiftUI" (WWDC25, session 256)

### Scene Bridging

**UIKit and AppKit lifecycle apps can now request SwiftUI scenes.** This enables using SwiftUI-only scene types like `MenuBarExtra` and `ImmersiveSpace` from imperative lifecycle apps via `UIApplication.shared.activateSceneSession(for:errorHandler:)`.

> Source: "What's new in SwiftUI" (WWDC25, session 256)

---

## Quick Lookup Table

| Deprecated | Recommended | Since |
|-----------|-------------|-------|
| `navigationBarTitle(_:)` | `navigationTitle(_:)` | iOS 15+ |
| `navigationBarItems(...)` | `toolbar { ToolbarItem(...) }` | iOS 15+ |
| `navigationBarHidden(_:)` | `toolbarVisibility(.hidden, for: .navigationBar)` | iOS 15+ |
| `statusBar(hidden:)` | `statusBarHidden(_:)` | iOS 15+ |
| `edgesIgnoringSafeArea(_:)` | `ignoresSafeArea(_:edges:)` | iOS 15+ |
| `colorScheme(_:)` | `preferredColorScheme(_:)` | iOS 15+ |
| `foregroundColor(_:)` | `foregroundStyle(_:)` | iOS 15+ |
| `cornerRadius(_:)` | `clipShape(.rect(cornerRadius:))` | iOS 15+ |
| `actionSheet(...)` | `confirmationDialog(...)` | iOS 15+ |
| `alert(isPresented:content:)` | `alert(_:isPresented:actions:message:)` | iOS 15+ |
| `autocapitalization(_:)` | `textInputAutocapitalization(_:)` | iOS 15+ |
| `accessibility(label:)` etc. | `accessibilityLabel()` etc. | iOS 15+ |
| `TextField` `onCommit`/`onEditingChanged` | `onSubmit` + `focused` | iOS 15+ |
| `animation(_:)` (no value) | `animation(_:value:)` | Back-deploys (iOS 13+) |
| Manual `EnvironmentKey` | `@Entry` macro | Back-deploys (Xcode 16+) |
| `NavigationView` | `NavigationStack` / `NavigationSplitView` | iOS 16+ |
| `accentColor(_:)` | `tint(_:)` | iOS 16+ |
| `disableAutocorrection(_:)` | `autocorrectionDisabled(_:)` | iOS 16+ |
| `UIPasteboard.general` | `PasteButton` | iOS 16+ |
| `onChange(of:perform:)` | `onChange(of:) { }` or `onChange(of:) { old, new in }` | iOS 17+ |
| `MagnificationGesture` | `MagnifyGesture` | iOS 17+ |
| `RotationGesture` | `RotateGesture` | iOS 17+ |
| `coordinateSpace(name:)` | `coordinateSpace(.named(...))` | iOS 17+ |
| `ObservableObject` | `@Observable` | iOS 17+ |
| `tabItem(_:)` | `Tab` API | iOS 18+ |
| Manual `animatableData` | `@Animatable` macro | iOS 26+ |
| `presentationBackground(_:)` on sheets | Default Liquid Glass sheet material | iOS 26+ |
| Custom toolbar background hacks | `scrollEdgeEffectStyle(_:for:)` | iOS 26+ |
```

## File: `swiftui-expert-skill/references/layout-best-practices.md`
```markdown
# SwiftUI Layout Best Practices Reference

## Table of Contents

- [Relative Layout Over Constants](#relative-layout-over-constants)
- [Context-Agnostic Views](#context-agnostic-views)
- [Own Your Container](#own-your-container)
- [Layout Performance](#layout-performance)
- [View Logic and Testability](#view-logic-and-testability)
- [Full-Width Views](#full-width-views)
- [Action Handlers](#action-handlers)
- [Summary Checklist](#summary-checklist)

## Relative Layout Over Constants

**Use dynamic layout calculations instead of hard-coded values.**

```swift
// Good - relative to actual layout
GeometryReader { geometry in
    VStack {
        HeaderView()
            .frame(height: geometry.size.height * 0.2)
        ContentView()
    }
}

// Avoid - magic numbers that don't adapt
VStack {
    HeaderView()
        .frame(height: 150)  // Doesn't adapt to different screens
    ContentView()
}
```

**Why**: Hard-coded values don't account for different screen sizes, orientations, or dynamic content (like status bars during phone calls).

## Context-Agnostic Views

**Views should work in any context.** Never assume presentation style or screen size.

```swift
// Good - adapts to given space
struct ProfileCard: View {
    let user: User
    
    var body: some View {
        VStack {
            Image(user.avatar)
                .resizable()
                .aspectRatio(contentMode: .fit)
            Text(user.name)
            Spacer()
        }
        .padding()
    }
}

// Avoid - assumes full screen
struct ProfileCard: View {
    let user: User
    
    var body: some View {
        VStack {
            Image(user.avatar)
                .frame(width: UIScreen.main.bounds.width)  // Wrong!
            Text(user.name)
        }
    }
}
```

**Why**: Views should work as full screens, modals, sheets, popovers, or embedded content.

## Own Your Container

**Custom views should own static containers but not lazy/repeatable ones.**

```swift
// Good - owns static container
struct HeaderView: View {
    var body: some View {
        HStack {
            Image(systemName: "star")
            Text("Title")
            Spacer()
        }
    }
}

// Avoid - missing container
struct HeaderView: View {
    var body: some View {
        Image(systemName: "star")
        Text("Title")
        // Caller must wrap in HStack
    }
}

// Good - caller owns lazy container
struct FeedView: View {
    let items: [Item]
    
    var body: some View {
        LazyVStack {
            ForEach(items) { item in
                ItemRow(item: item)
            }
        }
    }
}
```

## Layout Performance

### Avoid Layout Thrash

**Minimize deep view hierarchies and excessive layout dependencies.**

```swift
// Bad - deep nesting, excessive layout passes
VStack {
    HStack {
        VStack {
            HStack {
                VStack {
                    Text("Deep")
                }
            }
        }
    }
}

// Good - flatter hierarchy
VStack {
    Text("Shallow")
    Text("Structure")
}
```

**Avoid excessive `GeometryReader` and preference chains:**

```swift
// Bad - multiple geometry readers cause layout thrash
GeometryReader { outerGeometry in
    VStack {
        GeometryReader { innerGeometry in
            // Layout recalculates multiple times
        }
    }
}

// Good - single geometry reader or use alternatives (iOS 17+)
containerRelativeFrame(.horizontal) { width, _ in
    width * 0.8
}
```

**Gate frequent geometry updates:**

```swift
// Bad - updates on every pixel change
.onPreferenceChange(ViewSizeKey.self) { size in
    currentSize = size
}

// Good - gate by threshold
.onPreferenceChange(ViewSizeKey.self) { size in
    let difference = abs(size.width - currentSize.width)
    if difference > 10 {  // Only update if significant change
        currentSize = size
    }
}
```

## View Logic and Testability

### Keep Business Logic in Services and Models

**Business logic belongs in services and models, not in views.** Views should stay simple and declarative — orchestrating UI state, not implementing business rules. This makes logic independently testable without requiring view instantiation.

> **iOS 17+**: Use `@Observable` with `@State`.

```swift
@Observable
final class AuthService {
    var email = ""
    var password = ""
    var isValid: Bool {
        !email.isEmpty && password.count >= 8
    }

    func login() async throws {
        // Business logic here — testable without the view
    }
}

struct LoginView: View {
    @State private var authService = AuthService()

    var body: some View {
        Form {
            TextField("Email", text: $authService.email)
            SecureField("Password", text: $authService.password)
            Button("Login") {
                Task {
                    try? await authService.login()
                }
            }
            .disabled(!authService.isValid)
        }
    }
}
```

For iOS 16 and earlier, use `ObservableObject` with `@StateObject` -- see `state-management.md` for the legacy pattern.

Avoid embedding business logic directly in view closures (e.g., validation checks inside a `Button` action). This makes logic untestable without view instantiation.

**Note**: This is about making business logic testable, not about enforcing a specific architecture. The key is that logic lives outside views where it can be tested independently.

## Full-Width Views

**When a single view needs to fill the available width, use `.frame(maxWidth: .infinity, alignment:)` instead of wrapping it in a stack with a `Spacer`.**

```swift
// Good - frame modifier
Text("Hello")
    .frame(maxWidth: .infinity, alignment: .leading)

// Avoid - unnecessary stack and spacer
HStack {
    Text("Hello")
    Spacer()
}
```

**Why**: `.frame(maxWidth:alignment:)` is a single modifier that clearly communicates intent. Wrapping in an `HStack` with a `Spacer` adds an extra container to the view hierarchy for no benefit.

## Action Handlers

**Separate layout from logic.** View body should reference action methods, not contain inline logic.

```swift
// Good - action references method
Button("Publish Project", action: publishService.handlePublish)

// Avoid - multi-line logic in closure
Button("Publish Project") {
    isLoading = true
    apiService.publish(project) { result in /* ... */ }
}
```

## Summary Checklist

- [ ] Use relative layout over hard-coded constants
- [ ] Views work in any context (don't assume screen size)
- [ ] Custom views own static containers
- [ ] Avoid deep view hierarchies (layout thrash)
- [ ] Gate frequent geometry updates by thresholds
- [ ] Business logic kept in services and models (not in views)
- [ ] Action handlers reference methods, not inline logic
- [ ] Use `.frame(maxWidth: .infinity, alignment:)` for full-width views (not `HStack` + `Spacer`)
- [ ] Avoid excessive `GeometryReader` usage
- [ ] Use `containerRelativeFrame()` when appropriate
```

## File: `swiftui-expert-skill/references/liquid-glass.md`
```markdown
# SwiftUI Liquid Glass Reference (iOS 26+)

## Table of Contents

- [Overview](#overview)
- [Availability](#availability)
- [Core APIs](#core-apis)
- [GlassEffectContainer](#glasseffectcontainer)
- [Glass Button Styles](#glass-button-styles)
- [Morphing Transitions](#morphing-transitions)
- [Modifier Order](#modifier-order)
- [Complete Examples](#complete-examples)
- [Fallback Strategies](#fallback-strategies)
- [Design System Notes](#design-system-notes)
- [Best Practices](#best-practices)
- [Checklist](#checklist)

## Overview

Liquid Glass is Apple's new design language introduced in iOS 26. It provides translucent, dynamic surfaces that respond to content and user interaction. This reference covers the native SwiftUI APIs for implementing Liquid Glass effects.

**Only adopt Liquid Glass when explicitly requested by the user.** Do not proactively convert existing UI to glass effects.

## Availability

All Liquid Glass APIs require iOS 26 or later. Always provide fallbacks:

```swift
if #available(iOS 26, *) {
    // Liquid Glass implementation
} else {
    // Fallback using materials
}
```

## Core APIs

### glassEffect Modifier

The primary modifier for applying glass effects to views:

```swift
.glassEffect(_ style: GlassEffectStyle = .regular, in shape: some Shape = .rect)
```

#### Basic Usage

```swift
Text("Hello")
    .padding()
    .glassEffect()  // Default regular style, rect shape
```

#### With Shape

```swift
Text("Rounded Glass")
    .padding()
    .glassEffect(in: .rect(cornerRadius: 16))

Image(systemName: "star")
    .padding()
    .glassEffect(in: .circle)

Text("Capsule")
    .padding(.horizontal, 20)
    .padding(.vertical, 10)
    .glassEffect(in: .capsule)
```

### GlassEffectStyle

#### Prominence Levels

```swift
.glassEffect(.regular)     // Standard glass appearance
.glassEffect(.prominent)   // More visible, higher contrast
```

#### Tinting

Add color tint to the glass:

```swift
.glassEffect(.regular.tint(.blue))
.glassEffect(.prominent.tint(.red.opacity(0.3)))
```

#### Interactivity

Make glass respond to touch/pointer hover:

```swift
// Interactive glass - responds to user interaction
.glassEffect(.regular.interactive())

// Combined with tint
.glassEffect(.regular.tint(.blue).interactive())
```

**Important**: Only use `.interactive()` on elements that actually respond to user input (buttons, tappable views, focusable elements).

## GlassEffectContainer

Wraps multiple glass elements for proper visual grouping and spacing.

**Glass cannot sample other glass.** The glass material reflects and refracts light by sampling content from an area larger than itself. Nearby glass elements in different containers will produce inconsistent visual results because they cannot sample each other. `GlassEffectContainer` gives grouped elements a shared sampling region, ensuring a consistent appearance.

```swift
GlassEffectContainer {
    HStack {
        Button("One") { }
            .glassEffect()
        Button("Two") { }
            .glassEffect()
    }
}
```

### With Spacing

Control the visual spacing between glass elements:

```swift
GlassEffectContainer(spacing: 24) {
    HStack(spacing: 24) {
        GlassChip(icon: "pencil")
        GlassChip(icon: "eraser")
        GlassChip(icon: "trash")
    }
}
```

**Note**: The container's `spacing` parameter should match the actual spacing in your layout for proper glass effect rendering.

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

## Glass Button Styles

Built-in button styles for glass appearance:

```swift
// Standard glass button
Button("Action") { }
    .buttonStyle(.glass)

// Prominent glass button (higher visibility)
Button("Primary Action") { }
    .buttonStyle(.glassProminent)
```

### Custom Glass Buttons

For more control, apply glass effect manually:

```swift
Button(action: { }) {
    Label("Settings", systemImage: "gear")
        .padding()
}
.glassEffect(.regular.interactive(), in: .capsule)
```

## Morphing Transitions

Create smooth transitions between glass elements using `glassEffectID` and `@Namespace`:

```swift
struct MorphingExample: View {
    @Namespace private var animation
    @State private var isExpanded = false

    var body: some View {
        GlassEffectContainer {
            if isExpanded {
                ExpandedCard()
                    .glassEffect()
                    .glassEffectID("card", in: animation)
            } else {
                CompactCard()
                    .glassEffect()
                    .glassEffectID("card", in: animation)
            }
        }
        .animation(.smooth, value: isExpanded)
    }
}
```

### Requirements for Morphing

1. Both views must have the same `glassEffectID`
2. Use the same `@Namespace`
3. Wrap in `GlassEffectContainer`
4. Apply animation to the container or parent

## Modifier Order

**Critical**: Apply `glassEffect` after layout and visual modifiers:

```swift
// CORRECT order
Text("Label")
    .font(.headline)           // 1. Typography
    .foregroundStyle(.primary) // 2. Color
    .padding()                 // 3. Layout
    .glassEffect()             // 4. Glass effect LAST

// WRONG order - glass applied too early
Text("Label")
    .glassEffect()             // Wrong position
    .padding()
    .font(.headline)
```

## Complete Examples

### Toolbar with Glass Buttons

```swift
struct GlassToolbar: View {
    var body: some View {
        if #available(iOS 26, *) {
            GlassEffectContainer(spacing: 16) {
                HStack(spacing: 16) {
                    ToolbarButton(icon: "pencil", action: { })
                    ToolbarButton(icon: "eraser", action: { })
                    ToolbarButton(icon: "scissors", action: { })
                    Spacer()
                    ToolbarButton(icon: "square.and.arrow.up", action: { })
                }
                .padding(.horizontal)
            }
        } else {
            // Fallback toolbar
            HStack(spacing: 16) {
                // ... fallback implementation
            }
        }
    }
}

struct ToolbarButton: View {
    let icon: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Image(systemName: icon)
                .font(.title2)
                .frame(width: 44, height: 44)
        }
        .glassEffect(.regular.interactive(), in: .circle)
    }
}
```

### Card with Glass Effect

```swift
struct GlassCard: View {
    let title: String
    let subtitle: String

    var body: some View {
        if #available(iOS 26, *) {
            cardContent
                .glassEffect(.regular, in: .rect(cornerRadius: 20))
        } else {
            cardContent
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 20))
        }
    }

    private var cardContent: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(title)
                .font(.headline)
            Text(subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

### Segmented Control

```swift
struct GlassSegmentedControl: View {
    @Binding var selection: Int
    let options: [String]
    @Namespace private var animation

    var body: some View {
        if #available(iOS 26, *) {
            GlassEffectContainer(spacing: 4) {
                HStack(spacing: 4) {
                    ForEach(options.indices, id: \.self) { index in
                        Button(options[index]) {
                            withAnimation(.smooth) {
                                selection = index
                            }
                        }
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .glassEffect(
                            selection == index ? .prominent.interactive() : .regular.interactive(),
                            in: .capsule
                        )
                        .glassEffectID(selection == index ? "selected" : "option\(index)", in: animation)
                    }
                }
                .padding(4)
            }
        } else {
            Picker("Options", selection: $selection) {
                ForEach(options.indices, id: \.self) { index in
                    Text(options[index]).tag(index)
                }
            }
            .pickerStyle(.segmented)
        }
    }
}
```

## Fallback Strategies

### Using Materials

```swift
if #available(iOS 26, *) {
    content.glassEffect()
} else {
    content.background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
}
```

### Available Materials for Fallback

- `.ultraThinMaterial` - Closest to glass appearance
- `.thinMaterial` - Slightly more opaque
- `.regularMaterial` - Standard blur
- `.thickMaterial` - More opaque
- `.ultraThickMaterial` - Most opaque

### Conditional Modifier Extension

```swift
extension View {
    @ViewBuilder
    func glassEffectWithFallback(
        _ style: GlassEffectStyle = .regular,
        in shape: some Shape = .rect,
        fallbackMaterial: Material = .ultraThinMaterial
    ) -> some View {
        if #available(iOS 26, *) {
            self.glassEffect(style, in: shape)
        } else {
            self.background(fallbackMaterial, in: shape)
        }
    }
}
```

## Design System Notes

### Toolbar Icons

In the new design, toolbar icons use **monochrome rendering** by default. The monochrome palette reduces visual noise and maintains legibility. Use `tint(_:)` only to convey meaning (e.g., a call to action), not for visual effect.

### Sheet Presentations

Partial-height sheets use a Liquid Glass background by default. If you previously used `presentationBackground(_:)` with a custom background, consider removing it to let the new material shine. Sheets can morph out of the glass controls that present them using `navigationZoomTransition`.

### Scroll Edge Effects

An automatic scroll edge effect blurs and fades content under system toolbars to keep controls legible. Remove any custom background-darkening effects behind bar items, as they will interfere.

> Source: "Build a SwiftUI app with the new design" (WWDC25, session 323)

## Best Practices

### Do

- Use `GlassEffectContainer` for grouped glass elements (glass cannot sample other glass)
- Apply glass after layout modifiers
- Use `.interactive()` only on tappable elements
- Match container spacing with layout spacing
- Provide material-based fallbacks for older iOS
- Keep glass shapes consistent within a feature
- Remove custom `presentationBackground(_:)` on sheets to use the default glass material

### Don't

- Apply glass to every element (use sparingly)
- Use `.interactive()` on static content
- Mix different corner radii arbitrarily
- Forget iOS version checks
- Apply glass before padding/frame modifiers
- Nest `GlassEffectContainer` unnecessarily
- Add custom darkening backgrounds behind toolbars (conflicts with scroll edge effect)

## Checklist

- [ ] `#available(iOS 26, *)` with fallback
- [ ] `GlassEffectContainer` wraps grouped elements
- [ ] `.glassEffect()` applied after layout modifiers
- [ ] `.interactive()` only on user-interactable elements
- [ ] `glassEffectID` with `@Namespace` for morphing
- [ ] Consistent shapes and spacing across feature
- [ ] Container spacing matches layout spacing
- [ ] Appropriate prominence levels used
```

## File: `swiftui-expert-skill/references/list-patterns.md`
```markdown
# SwiftUI List Patterns Reference

## Table of Contents

- [ForEach Identity and Stability](#foreach-identity-and-stability)
- [Enumerated Sequences](#enumerated-sequences)
- [List with Custom Styling](#list-with-custom-styling)
- [List with Pull-to-Refresh](#list-with-pull-to-refresh)
- [Empty States with ContentUnavailableView (iOS 17+)](#empty-states-with-contentunavailableview-ios-17)
- [Custom List Backgrounds](#custom-list-backgrounds)
- [Table](#table)
- [Summary Checklist](#summary-checklist)

## ForEach Identity and Stability

**Always provide stable identity for `ForEach`.** Never use `.indices` for dynamic content.

```swift
// Good - stable identity via Identifiable
extension User: Identifiable {
    var id: String { userId }
}

ForEach(users) { user in
    UserRow(user: user)
}

// Good - stable identity via keypath
ForEach(users, id: \.userId) { user in
    UserRow(user: user)
}

// Wrong - indices create static content
ForEach(users.indices, id: \.self) { index in
    UserRow(user: users[index])  // Can crash on removal!
}

// Wrong - unstable identity
ForEach(users, id: \.self) { user in
    UserRow(user: user)  // Only works if User is Hashable and stable
}
```

**Critical**: Ensure **constant number of views per element** in `ForEach`:

```swift
// Good - consistent view count
ForEach(items) { item in
    ItemRow(item: item)
}

// Bad - variable view count breaks identity
ForEach(items) { item in
    if item.isSpecial {
        SpecialRow(item: item)
        DetailRow(item: item)
    } else {
        RegularRow(item: item)
    }
}
```

**Avoid inline filtering:**

```swift
// Bad - unstable identity, changes on every update
ForEach(items.filter { $0.isEnabled }) { item in
    ItemRow(item: item)
}

// Good - prefilter and cache
@State private var enabledItems: [Item] = []

var body: some View {
    ForEach(enabledItems) { item in
        ItemRow(item: item)
    }
    .onChange(of: items) { _, newItems in
        enabledItems = newItems.filter { $0.isEnabled }
    }
}
```

**Avoid `AnyView` in list rows:**

```swift
// Bad - hides identity, increases cost
ForEach(items) { item in
    AnyView(item.isSpecial ? SpecialRow(item: item) : RegularRow(item: item))
}

// Good - Create a unified row view
ForEach(items) { item in
    ItemRow(item: item)
}

struct ItemRow: View {
    let item: Item

    var body: some View {
        if item.isSpecial {
            SpecialRow(item: item)
        } else {
            RegularRow(item: item)
        }
    }
}
```

**Why**: Stable identity is critical for performance and animations. Unstable identity causes excessive diffing, broken animations, and potential crashes.

### Identifiable ID Must Be Truly Unique

Non-unique IDs cause SwiftUI to treat different items as identical, leading to duplicate rendering or missing views:

```swift
// Bug -- two articles with the same URL show identical content
struct Article: Identifiable {
    let title: String
    let url: URL
    var id: String { url.absoluteString }  // Not unique if URLs repeat!
}

// Fix -- use a genuinely unique identifier
struct Article: Identifiable {
    let id: UUID
    let title: String
    let url: URL
}
```

**Classes get a default `ObjectIdentifier`-based `id`** when conforming to `Identifiable` without providing one. This is only unique for the object's lifetime and can be recycled after deallocation.

## Enumerated Sequences

**Always convert enumerated sequences to arrays. To be able to use them in a ForEach.**

```swift
let items = ["A", "B", "C"]

// Correct
ForEach(Array(items.enumerated()), id: \.offset) { index, item in
    Text("\(index): \(item)")
}

// Wrong - Doesn't compile, enumerated() isn't an array
ForEach(items.enumerated(), id: \.offset) { index, item in
    Text("\(index): \(item)")
}
```

## List with Custom Styling

```swift
// Remove default background and separators
List(items) { item in
    ItemRow(item: item)
        .listRowInsets(EdgeInsets(top: 8, leading: 16, bottom: 8, trailing: 16))
        .listRowSeparator(.hidden)
}
.listStyle(.plain)
.scrollContentBackground(.hidden)
.background(Color.customBackground)
.environment(\.defaultMinListRowHeight, 1)  // Allows custom row heights
```

## List with Pull-to-Refresh

```swift
List(items) { item in
    ItemRow(item: item)
}
.refreshable {
    await loadItems()
}
```

## Empty States with ContentUnavailableView (iOS 17+)

Use `ContentUnavailableView` for empty list/search states. The built-in `.search` variant is auto-localized:

```swift
List {
    ForEach(searchResults) { item in
        ItemRow(item: item)
    }
}
.overlay {
    if searchResults.isEmpty, !searchText.isEmpty {
        ContentUnavailableView.search(text: searchText)
    }
}
```

For non-search empty states, use a custom instance:

```swift
ContentUnavailableView(
    "No Articles",
    systemImage: "doc.richtext.fill",
    description: Text("Articles you save will appear here.")
)
```

## Custom List Backgrounds

Use `.scrollContentBackground(.hidden)` to replace the default list background:

```swift
List(items) { item in
    ItemRow(item: item)
}
.scrollContentBackground(.hidden)
.background(Color.customBackground)
```

Without `.scrollContentBackground(.hidden)`, a custom `.background()` has no visible effect on `List`.

## Table

> **Availability:** iOS 16.0+, iPadOS 16.0+, visionOS 1.0+

A multi-column data container that presents rows of `Identifiable` data with sortable, selectable columns. On compact size classes (iPhone, iPad Slide Over), columns after the first are automatically hidden.

### Basic Table

```swift
struct Person: Identifiable {
    let givenName: String
    let familyName: String
    let emailAddress: String
    let id = UUID()
    var fullName: String { givenName + " " + familyName }
}

struct PeopleTable: View {
    @State private var people: [Person] = [ /* ... */ ]

    var body: some View {
        Table(people) {
            TableColumn("Given Name", value: \.givenName)
            TableColumn("Family Name", value: \.familyName)
            TableColumn("E-Mail Address", value: \.emailAddress)
        }
    }
}
```

### Table with Selection

Bind to a single `ID` for single-selection, or a `Set<ID>` for multi-selection:

```swift
struct SelectableTable: View {
    @State private var people: [Person] = [ /* ... */ ]
    @State private var selectedPeople = Set<Person.ID>()

    var body: some View {
        Table(people, selection: $selectedPeople) {
            TableColumn("Given Name", value: \.givenName)
            TableColumn("Family Name", value: \.familyName)
            TableColumn("E-Mail Address", value: \.emailAddress)
        }
        Text("\(selectedPeople.count) people selected")
    }
}
```

### Sortable Table

Provide a binding to `[KeyPathComparator]` and re-sort the data in `.onChange(of:)`:

```swift
struct SortableTable: View {
    @State private var people: [Person] = [ /* ... */ ]
    @State private var sortOrder = [KeyPathComparator(\Person.givenName)]

    var body: some View {
        Table(people, sortOrder: $sortOrder) {
            TableColumn("Given Name", value: \.givenName)
            TableColumn("Family Name", value: \.familyName)
            TableColumn("E-Mail Address", value: \.emailAddress)
        }
        .onChange(of: sortOrder) { _, newOrder in
            people.sort(using: newOrder)
        }
    }
}
```

**Important:** The table does **not** sort data itself — you must re-sort the collection when `sortOrder` changes.

### Adaptive Table for Compact Size Classes

On iPhone or iPad in Slide Over, only the first column is shown. Customize it to display combined information:

```swift
struct AdaptiveTable: View {
    @Environment(\.horizontalSizeClass) private var horizontalSizeClass
    private var isCompact: Bool { horizontalSizeClass == .compact }

    @State private var people: [Person] = [ /* ... */ ]
    @State private var sortOrder = [KeyPathComparator(\Person.givenName)]

    var body: some View {
        Table(people, sortOrder: $sortOrder) {
            TableColumn("Given Name", value: \.givenName) { person in
                VStack(alignment: .leading) {
                    Text(isCompact ? person.fullName : person.givenName)
                    if isCompact {
                        Text(person.emailAddress)
                            .foregroundStyle(.secondary)
                    }
                }
            }
            TableColumn("Family Name", value: \.familyName)
            TableColumn("E-Mail Address", value: \.emailAddress)
        }
        .onChange(of: sortOrder) { _, newOrder in
            people.sort(using: newOrder)
        }
    }
}
```

### Table with Static Rows

Use `init(of:columns:rows:)` when rows are known at compile time:

```swift
struct Purchase: Identifiable {
    let price: Decimal
    let id = UUID()
}

struct TipTable: View {
    let currencyStyle = Decimal.FormatStyle.Currency(code: "USD")

    var body: some View {
        Table(of: Purchase.self) {
            TableColumn("Base price") { purchase in
                Text(purchase.price, format: currencyStyle)
            }
            TableColumn("With 15% tip") { purchase in
                Text(purchase.price * 1.15, format: currencyStyle)
            }
            TableColumn("With 20% tip") { purchase in
                Text(purchase.price * 1.2, format: currencyStyle)
            }
        } rows: {
            TableRow(Purchase(price: 20))
            TableRow(Purchase(price: 50))
            TableRow(Purchase(price: 75))
        }
    }
}
```

### Table with Dynamic Number of Columns

> **Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, visionOS 1.1+

If the number of columns is not known at runtime use `TableColumnForEach` to create columns based on a `RandomAccessCollection` of some data type. Either the collection’s elements must conform to `Identifiable` or you need to provide an id parameter to the `TableColumnForEach` initializer.

This can be mixed with static compile time known `TableColumn` usage.

```swift
struct AudioChannel: Identifiable {
    let name: String
    let id: UUID
}

struct AudioSample: Identifiable {
    let id: UUID
    let timestamp: TimeInterval
    func level(channel: AudioChannel.ID) -> Double {
        1
    }
}

@Observable
class AudioSampleTrack {
    let channels: [AudioChannel]
    var samples: [AudioSample]
}

struct ContentView: View {
    var track: AudioSampleTrack

    var body: some View {
        Table(track.samples) {
            TableColumn("Timestamp (ms)") { sample in
                Text(sample.timestamp, format: .number.scale(1000))
                    .monospacedDigit()
            }
            TableColumnForEach(track.channels) { channel in
                TableColumn(channel.name) { sample in
                    Text(sample.level(channel: channel.id),
                         format: .number.precision(.fractionLength(2))
                    )
                    .monospacedDigit()
                }
                .width(ideal: 70)
                .alignment(.numeric)
            }
        }
    }
}
```

### Table Styles

```swift
// Inset (no borders)
Table(people) { /* columns */ }
    .tableStyle(.inset)

// Hide column headers
Table(people) { /* columns */ }
    .tableColumnHeaders(.hidden)
```

### Platform Behavior

| Platform | Behavior |
|----------|----------|
| **iPadOS (regular)** | Full multi-column layout; headers and all columns visible |
| **iPadOS (compact)** | Only the first column shown; headers hidden |
| **iPhone (all sizes)** | Only the first column shown; headers hidden; list-like appearance |

> **Best Practice:** Prefer handling the compact size class by showing combined info in the first column. This provides a seamless transition when the size class changes (e.g., entering/exiting Slide Over on iPad).

## Summary Checklist

- [ ] ForEach uses stable identity (never `.indices` for dynamic content)
- [ ] Identifiable IDs are truly unique across all items
- [ ] Constant number of views per ForEach element
- [ ] No inline filtering in ForEach (prefilter and cache instead)
- [ ] No `AnyView` in list rows
- [ ] Don't convert enumerated sequences to arrays
- [ ] Use `.refreshable` for pull-to-refresh
- [ ] Use `ContentUnavailableView` for empty states (iOS 17+)
- [ ] Use `.scrollContentBackground(.hidden)` for custom list backgrounds
- [ ] `Table` adapts for compact size classes (first column shows combined info)
- [ ] `Table` sorting re-sorts data in `.onChange(of: sortOrder)` (table doesn't sort itself)
- [ ] `Table` data conforms to `Identifiable`
```

## File: `swiftui-expert-skill/references/macos-scenes.md`
```markdown
# macOS Scenes Reference

> SwiftUI scene types for macOS apps — `Settings`, `MenuBarExtra`, `WindowGroup`, `Window`, `UtilityWindow`, and `DocumentGroup`. Covers macOS-only scenes and cross-platform scenes with macOS-specific behavior.

## Table of Contents

- [Quick Lookup Table](#quick-lookup-table)
- [Settings (macOS-only)](#settings-macos-only)
- [MenuBarExtra (macOS-only)](#menubarextra-macos-only)
- [WindowGroup (macOS behavior)](#windowgroup-macos-behavior)
- [Window](#window)
- [UtilityWindow (macOS-only)](#utilitywindow-macos-only)
- [DocumentGroup](#documentgroup)
- [Platform Conditionals](#platform-conditionals)
- [Best Practices](#best-practices)

---

## Quick Lookup Table

| API | Availability | macOS-Only? | macOS-Specific Behavior |
|-----|-------------|:-----------:|------------------------|
| `WindowGroup` | macOS 11.0+ | No | Multiple window instances, tabbed interface, automatic Window menu commands |
| `Window` | macOS 13.0+ | No | App quits when sole window closes; adds itself to Windows menu |
| `UtilityWindow` | macOS 15.0+ | Yes | Floating tool palette; receives `FocusedValues` from active main window |
| `Settings` | macOS 11.0+ | Yes | Presents preferences window (Cmd+,) |
| `MenuBarExtra` | macOS 13.0+ | Yes | Persistent icon/menu in the system menu bar |
| `DocumentGroup` | macOS 11.0+ | No | Document-based menu bar commands (File > New/Open/Save); multiple document windows |

---

## Settings (macOS-only)

Presents the app's preferences window, accessible via **Cmd+,** or the app menu. SwiftUI automatically enables the Settings menu item and manages the window lifecycle.

```swift
Settings {
    TabView {
        Tab("General", systemImage: "gear") { GeneralSettingsView() }
        Tab("Advanced", systemImage: "star") { AdvancedSettingsView() }
    }
    .scenePadding()
    .frame(maxWidth: 350, minHeight: 100)
}
```

Use `TabView` with `Tab` items for multi-pane preferences. Each tab's content is typically a `Form` with `@AppStorage`-backed controls.

### SettingsLink (macOS 14.0+)

A button that opens the Settings scene. Use for in-app navigation to preferences.

```swift
struct SidebarFooter: View {
    var body: some View {
        SettingsLink {
            Label("Preferences", systemImage: "gear")
        }
    }
}
```

### openSettings environment action (macOS 14.0+)

Programmatically open (or bring to front) the Settings window.

```swift
struct OpenSettingsButton: View {
    @Environment(\.openSettings) private var openSettings

    var body: some View {
        Button("Open Settings") {
            openSettings()
        }
    }
}
```

---

## MenuBarExtra (macOS-only)

Renders a persistent control in the system menu bar. Two styles available:
- **`.menu`** (default) — standard dropdown menu
- **`.window`** — popover panel with custom SwiftUI views

### Menu-style (dropdown)

```swift
MenuBarExtra("My Utility", systemImage: "hammer") {
    Button("Action One") { /* ... */ }
    Button("Action Two") { /* ... */ }
    Divider()
    Button("Quit") { NSApplication.shared.terminate(nil) }
}
```

### Window-style (popover panel)

```swift
MenuBarExtra("Status", systemImage: "chart.bar") {
    DashboardView()
        .frame(width: 240)
}
.menuBarExtraStyle(.window)
```

**Variations:**
- **Toggleable** — pass `isInserted:` with an `@AppStorage` binding to let users show/hide the extra: `MenuBarExtra("Status", systemImage: "chart.bar", isInserted: $showMenuBarExtra)`
- **Menu-bar-only app** — use `MenuBarExtra` as the sole scene + set `LSUIElement = true` in Info.plist to hide the Dock icon. The app auto-terminates if the user removes the extra from the menu bar.

---

## WindowGroup (macOS behavior)

On macOS, `WindowGroup` supports:
- **Multiple window instances** — users can open many windows from File > New Window
- **Tabbed interface** — users can merge windows into tabs
- **Automatic Window menu** — commands for window management appear automatically

```swift
@main
struct Mail: App {
    var body: some Scene {
        // Basic multi-window support
        WindowGroup {
            MailViewer()
        }

        // Data-presenting window opened programmatically
        WindowGroup("Message", for: Message.ID.self) { $messageID in
            MessageDetail(messageID: messageID)
        }
    }
}

// Open a specific window programmatically
struct NewMessageButton: View {
    var message: Message
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open Message") {
            openWindow(value: message.id)
        }
    }
}
```

> **Key difference from `Window`:** `WindowGroup` keeps the app running even after all windows are closed. `Window` (as sole scene) quits the app when closed.

---

## Window

A single, unique window scene. The system ensures only one instance exists.

```swift
@main
struct Mail: App {
    var body: some Scene {
        WindowGroup {
            MailViewer()
        }

        // Supplementary singleton window
        Window("Connection Doctor", id: "connection-doctor") {
            ConnectionDoctor()
        }
    }
}

// Open programmatically — brings to front if already open
struct OpenDoctorButton: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Connection Doctor") {
            openWindow(id: "connection-doctor")
        }
    }
}
```

### Window as sole scene

If `Window` is the only scene, the app quits when the window closes:

```swift
@main
struct VideoCall: App {
    var body: some Scene {
        Window("VideoCall", id: "main") {
            CameraView()
        }
    }
}
```

> **Recommendation:** In most cases, prefer `WindowGroup` for the primary scene. Use `Window` for supplementary singleton windows.

---

## UtilityWindow (macOS-only)

A specialized floating window for tool palettes and inspector panels. Available since macOS 15.0.

**Key behaviors:**
- Receives `FocusedValues` from the focused main scene (like menu bar commands)
- Floats above main windows (default level: `.floating`)
- Hides when the app is no longer active
- Only becomes focused when explicitly needed (e.g., clicking the title bar)
- Dismissible with the Escape key
- Not minimizable by default
- Automatically adds a show/hide item to the View menu

```swift
@main
struct PhotoBrowser: App {
    var body: some Scene {
        WindowGroup {
            PhotoGallery()
        }

        UtilityWindow("Photo Info", id: "photo-info") {
            PhotoInfoViewer()
        }
    }
}

struct PhotoInfoViewer: View {
    // Automatically updates based on whichever main window is focused
    @FocusedValue(PhotoSelection.self) private var selectedPhotos

    var body: some View {
        if let photos = selectedPhotos {
            Text("\(photos.count) photos selected")
        } else {
            Text("No selection")
                .foregroundStyle(.secondary)
        }
    }
}
```

> **Tip:** Remove the automatic View menu item with `.commandsRemoved()` and place a `WindowVisibilityToggle` elsewhere in your commands.

---

## DocumentGroup

Document-based apps with automatic file management. On macOS, provides:
- **Document-based menu bar commands** (File > New, Open, Save, Revert)
- **Multiple document windows** simultaneously
- On iOS, shows a document browser instead

```swift
DocumentGroup(newDocument: TextFile()) { config in
    ContentView(document: config.$document)
}
```

The document type must conform to `FileDocument` (value type) or `ReferenceFileDocument` (reference type). Key requirements:

```swift
struct TextFile: FileDocument {
    static var readableContentTypes: [UTType] { [.plainText] }
    var text: String = ""
    init() {}
    init(configuration: ReadConfiguration) throws {
        text = String(data: configuration.file.regularFileContents ?? Data(), encoding: .utf8) ?? ""
    }
    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        FileWrapper(regularFileWithContents: Data(text.utf8))
    }
}
```

For multiple document types, add additional `DocumentGroup` scenes — use `DocumentGroup(viewing:)` for read-only formats.

---

## Platform Conditionals

Always wrap macOS-only scenes in `#if os(macOS)`:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }

        #if os(macOS)
        Settings {
            SettingsView()
        }

        MenuBarExtra("Status", systemImage: "bolt") {
            StatusMenu()
        }
        #endif
    }
}
```

---

## Best Practices

- **Use `Settings`** for preferences — prefer this over a custom preferences window
- **Use `MenuBarExtra`** for menu bar items — prefer this over managing AppKit's `NSStatusItem` directly
- **Use `WindowGroup`** as the primary scene — reserve `Window` for supplementary singletons
- **Use `UtilityWindow`** for inspectors/palettes — it handles floating, focus, and visibility automatically
- **Use `DocumentGroup`** for document-based apps — it provides the full File menu and document lifecycle
- **Gate macOS-only scenes** with `#if os(macOS)` for multiplatform projects
- **Use `openWindow(id:)`** to open windows programmatically — it brings existing windows to front
```

## File: `swiftui-expert-skill/references/macos-views.md`
```markdown
# macOS Views & Components Reference

> macOS-specific SwiftUI views, file operations, drag & drop, and AppKit interop. Covers `HSplitView`, `VSplitView`, `Table`, `PasteButton`, file dialogs, cross-app drag & drop, and `NSViewRepresentable`.

## Table of Contents

- [Quick Lookup Table](#quick-lookup-table)
- [HSplitView & VSplitView (macOS-only)](#hsplitview--vsplitview-macos-only)
- [Table](#table)
- [PasteButton & CopyButton](#pastebutton--copybutton)
- [File Operations](#file-operations)
- [Drag, Drop & Pasteboard](#drag-drop--pasteboard)
- [AppKit Interop](#appkit-interop)
- [Best Practices](#best-practices)

---

## Quick Lookup Table

### Views

| API | Availability | macOS-Only? | Usage |
|-----|-------------|:-----------:|-------|
| `HSplitView` | macOS 10.15+ | Yes | Horizontal resizable split layout with user-draggable dividers |
| `VSplitView` | macOS 10.15+ | Yes | Vertical resizable split layout with user-draggable dividers |
| `Table` | macOS 12.0+ | No | Full multi-column layout with sorting; on iOS compact, columns collapse |
| `PasteButton` | macOS 10.15+ | No | System button that reads clipboard; does NOT auto-validate on macOS |
| `CopyButton` | macOS 15.0+ | Yes | System button that copies `Transferable` content to clipboard |

### File Operations

| API | Availability | macOS-Only? | Usage |
|-----|-------------|:-----------:|-------|
| `fileImporter()` | macOS 11.0+ | No | Native NSOpenPanel with column/list/gallery view, sidebar, tags, QuickLook |
| `fileExporter()` | macOS 11.0+ | No | Native NSSavePanel with format dropdown, tags field |
| `fileMover()` | macOS 11.0+ | No | Native macOS move panel with Finder-like navigation |
| `fileDialogMessage(_:)` | macOS 13.0+ | Yes | Custom message text in file dialogs |
| `fileDialogConfirmationLabel(_:)` | macOS 13.0+ | Yes | Custom confirm button text in file dialogs |
| `fileExporterFilenameLabel(_:)` | macOS 13.0+ | Yes | Custom filename field label in file exporter |

### Drag, Drop & Pasteboard

| API | Availability | macOS-Only? | Usage |
|-----|-------------|:-----------:|-------|
| `onDrag(_:)` / `draggable(_:)` | macOS 11.0+ | No | Drag image follows cursor; items draggable between apps |
| `onDrop(of:delegate:)` / `dropDestination(for:action:)` | macOS 11.0+ | No | Accepts drops from any macOS app including Finder |

### AppKit Interop

| API | Availability | macOS-Only? | Usage |
|-----|-------------|:-----------:|-------|
| `NSViewRepresentable` | macOS 10.15+ | Yes | Wrap an AppKit `NSView` in SwiftUI |
| `NSViewControllerRepresentable` | macOS 10.15+ | Yes | Wrap an AppKit `NSViewController` in SwiftUI |
| `NSHostingController` | macOS 10.15+ | Yes | Host SwiftUI inside an AppKit view controller |
| `NSHostingView` | macOS 10.15+ | Yes | Host SwiftUI inside an AppKit `NSView` hierarchy |

---

## HSplitView & VSplitView (macOS-only)

Resizable split layouts with user-draggable dividers. Use for IDE-style panes where all panels are equal peers. `VSplitView` works identically but splits vertically (use `minHeight` instead).

```swift
HSplitView {
    FileTreeView()
        .frame(minWidth: 200)
    CodeEditorView()
        .frame(minWidth: 400)
    PreviewPane()
        .frame(minWidth: 200)
}
```

> **When to use which:**
> - **`NavigationSplitView`** — sidebar-based navigation (sidebar drives content/detail)
> - **`HSplitView`/`VSplitView`** — IDE-style layouts where all panes are equal peers

---

## Table

For `Table` basics (creation, selection, sorting, adaptive compact layout), see `list-patterns.md`. This section covers macOS-specific table styling.

### Table styles

```swift
// Bordered with visible grid lines (macOS-only)
Table(people) { /* columns */ }
    .tableStyle(.bordered)

// Bordered with alternating row backgrounds
Table(people) { /* columns */ }
    .tableStyle(.bordered(alternatesRowBackgrounds: true))

// Inset (no borders)
Table(people) { /* columns */ }
    .tableStyle(.inset)

// Hide column headers
Table(people) { /* columns */ }
    .tableColumnHeaders(.hidden)
```

---

## PasteButton & CopyButton

### PasteButton

System button that reads clipboard content via `Transferable`. On macOS, it does NOT auto-validate pasteboard changes (unlike iOS).

```swift
struct ClipboardView: View {
    @State private var pastedText = ""

    var body: some View {
        HStack {
            PasteButton(payloadType: String.self) { strings in
                pastedText = strings[0]
            }
            Divider()
            Text(pastedText)
            Spacer()
        }
    }
}
```

### CopyButton (macOS 15.0+, macOS-only)

System button that copies `Transferable` content to the clipboard.

```swift
struct CopyableContent: View {
    let shareableText = "Hello, world!"

    var body: some View {
        HStack {
            Text(shareableText)
            CopyButton(item: shareableText)
        }
    }
}
```

---

## File Operations

### fileImporter

On macOS, presents a native `NSOpenPanel` with column/list/gallery view, sidebar favorites, tags, and QuickLook.

```swift
.fileImporter(
    isPresented: $showImporter,
    allowedContentTypes: [.pdf],
    allowsMultipleSelection: false
) { result in
    if case .success(let urls) = result, let url = urls.first {
        guard url.startAccessingSecurityScopedResource() else { return }
        defer { url.stopAccessingSecurityScopedResource() }
        // use url
    }
}
```

> **Important:** Always call `startAccessingSecurityScopedResource()` on returned URLs, and `stopAccessingSecurityScopedResource()` when done. These are security-scoped bookmarks — access fails without this.

### fileExporter

On macOS, presents a native `NSSavePanel` with format dropdown and tags.

```swift
.fileExporter(
    isPresented: $showExporter,
    document: document,
    contentType: .plainText,
    defaultFilename: "MyFile.txt"
) { result in
    // handle Result<URL, Error>
}
```

### File dialog customization (macOS-only)

Customize text in file dialogs with these macOS-specific modifiers:

```swift
// Custom message and confirm button on file importer
.fileImporter(
    isPresented: $showImporter,
    allowedContentTypes: [.image]
) { result in
    // handle result
}
.fileDialogMessage("Select an image to use as your profile photo")
.fileDialogConfirmationLabel("Use This Photo")

// Custom filename label on file exporter
.fileExporter(
    isPresented: $showExporter,
    document: myDocument,
    contentType: .png
) { result in
    // handle result
}
.fileExporterFilenameLabel("Export As:")
```

---

## Drag, Drop & Pasteboard

On macOS, drag and drop works **across applications** (e.g., drag from your app to Finder, Mail, or other apps).

### Modern approach (Transferable)

```swift
// Drag source
struct DraggableCard: View {
    let item: MyItem

    var body: some View {
        Text(item.title)
            .draggable(item)  // Requires Transferable conformance
    }
}

// Drop target
struct DropZone: View {
    @State private var droppedItems: [MyItem] = []

    var body: some View {
        VStack {
            ForEach(droppedItems) { item in
                Text(item.title)
            }
        }
        .dropDestination(for: MyItem.self) { items, location in
            droppedItems.append(contentsOf: items)
            return true
        }
        .frame(width: 300, height: 200)
        .border(.secondary)
    }
}
```

### Legacy approach (NSItemProvider)

```swift
// Drag source
Image(systemName: "doc")
    .onDrag {
        NSItemProvider(object: fileURL as NSURL)
    }

// Drop target
Text("Drop files here")
    .onDrop(of: [.fileURL], isTargeted: nil) { providers in
        // handle providers
        return true
    }
```

---

## AppKit Interop

### NSViewRepresentable (macOS-only)

Wraps an AppKit `NSView` for use in SwiftUI. Implement `makeNSView(context:)` and `updateNSView(_:context:)`.

```swift
struct WebView: NSViewRepresentable {
    let url: URL
    func makeNSView(context: Context) -> WKWebView { WKWebView() }
    func updateNSView(_ nsView: WKWebView, context: Context) {
        nsView.load(URLRequest(url: url))
    }
}
```

### NSViewRepresentable with Coordinator

Use a Coordinator to forward delegate/target-action callbacks to SwiftUI.

```swift
struct SearchField: NSViewRepresentable {
    @Binding var text: String

    func makeNSView(context: Context) -> NSSearchField {
        let field = NSSearchField()
        field.delegate = context.coordinator
        return field
    }
    func updateNSView(_ nsView: NSSearchField, context: Context) {
        nsView.stringValue = text
    }
    func makeCoordinator() -> Coordinator { Coordinator(text: $text) }

    class Coordinator: NSObject, NSSearchFieldDelegate {
        var text: Binding<String>
        init(text: Binding<String>) { self.text = text }
        func controlTextDidChange(_ obj: Notification) {
            if let field = obj.object as? NSSearchField {
                text.wrappedValue = field.stringValue
            }
        }
    }
}
```

> **Warning:** Never set `frame`/`bounds` directly on the managed `NSView` — SwiftUI owns the layout.

### NSViewControllerRepresentable (macOS-only)

Wraps an AppKit `NSViewController` for use in SwiftUI.

```swift
struct MapViewWrapper: NSViewControllerRepresentable {
    func makeNSViewController(context: Context) -> MapViewController {
        MapViewController()
    }

    func updateNSViewController(_ nsViewController: MapViewController, context: Context) {
        // Update the controller when SwiftUI state changes
    }
}
```

### NSHostingController & NSHostingView (macOS-only)

Host SwiftUI content inside AppKit (reverse direction — AppKit app embedding SwiftUI views).

```swift
// Host SwiftUI as a view controller
let hostingController = NSHostingController(rootView: MySwiftUIView())
window.contentViewController = hostingController

// Host SwiftUI directly as an NSView
let hostingView = NSHostingView(rootView: MySwiftUIView())
someNSView.addSubview(hostingView)
```

---

## Best Practices

- **Use `NavigationSplitView`** for sidebar-driven navigation — reserve `HSplitView`/`VSplitView` for IDE-style equal peer panes
- **Make `Table` adaptive** — handle compact size classes by showing combined info in the first column
- **Always call `startAccessingSecurityScopedResource()`** on URLs from `fileImporter` — they are security-scoped
- **Use `Transferable`** for drag & drop (modern) — fall back to `NSItemProvider` only for legacy compatibility
- **Use `NSViewRepresentable` with Coordinator** when you need delegate callbacks from AppKit views
- **Never set `frame`/`bounds`** directly on views managed by `NSViewRepresentable` — SwiftUI owns the layout
- **Prefer native SwiftUI** over AppKit interop when possible — only use `NSViewRepresentable` for features SwiftUI doesn't provide
```

## File: `swiftui-expert-skill/references/macos-window-styling.md`
```markdown
# macOS Window & Toolbar Styling Reference

> Window configuration, toolbar styles, sizing, positioning, and navigation patterns specific to macOS SwiftUI apps.

## Table of Contents

- [Quick Lookup Table](#quick-lookup-table)
- [Toolbar Styles](#toolbar-styles)
- [Window Style](#window-style)
- [Window Sizing](#window-sizing)
- [MenuBarExtra Style (macOS-only)](#menubarextra-style-macos-only)
- [Navigation Layout (macOS behavior)](#navigation-layout-macos-behavior)
- [Commands & Keyboard](#commands--keyboard)
- [Best Practices](#best-practices)

---

## Quick Lookup Table

| API | Availability | macOS-Only? | Usage |
|-----|-------------|:-----------:|-------|
| `windowToolbarStyle(_:)` | macOS 11.0+ | Yes | Sets toolbar style: `.unified`, `.unifiedCompact`, `.expanded` |
| `windowStyle(_:)` | macOS 11.0+ | No | Supports `.hiddenTitleBar` for chromeless windows |
| `windowResizability(_:)` | macOS 13.0+ | No | Controls resize handle and green zoom button behavior |
| `defaultSize(width:height:)` | macOS 13.0+ | No | Initial frame size when user creates a new window |
| `defaultPosition(_:)` | macOS 13.0+ | No | Initial window position on screen |
| `windowIdealPlacement(_:)` | macOS 15.0+ | No | Closure with display geometry for precise window positioning |
| `menuBarExtraStyle(_:)` | macOS 13.0+ | Yes | Sets MenuBarExtra to `.menu` or `.window` style |
| `NavigationSplitView` | macOS 13.0+ | No | Columns always visible side-by-side on macOS; translucent sidebar |
| `Inspector` | macOS 14.0+ | No | Trailing-edge sidebar panel; resizable by dragging |

---

## Toolbar Styles

### windowToolbarStyle (macOS-only)

Controls how the toolbar and title bar are displayed. Applied to a scene.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // Title bar and toolbar in a single row
        .windowToolbarStyle(.unified)
    }
}
```

**Available styles:**

| Style | Description |
|-------|-------------|
| `.automatic` | System default |
| `.unified` | Title bar and toolbar in a single combined row |
| `.unifiedCompact` | Same as unified but with reduced vertical height |
| `.expanded` | Title bar displayed above the toolbar (more toolbar space) |

```swift
// Unified compact — minimal chrome
.windowToolbarStyle(.unifiedCompact)

// Expanded — title bar above toolbar
.windowToolbarStyle(.expanded)

// Unified with title hidden
.windowToolbarStyle(.unified(showsTitle: false))
```

### Toolbar content

```swift
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        NavigationSplitView {
            SidebarView()
        } detail: {
            DetailView()
        }
        .toolbar {
            ToolbarItem(placement: .automatic) {
                Button(action: addItem) {
                    Label("Add", systemImage: "plus")
                }
            }
        }
        .searchable(text: $searchText, placement: .sidebar)
    }
}
```

---

## Window Style

### windowStyle

Set the visual style of a window. Use `.hiddenTitleBar` for chromeless, immersive windows.

```swift
// Standard title bar (default)
WindowGroup {
    ContentView()
}
.windowStyle(.titleBar)

// Hidden title bar — chromeless window
WindowGroup {
    ContentView()
}
.windowStyle(.hiddenTitleBar)
```

> **Use case:** `.hiddenTitleBar` is useful for media players, custom-chrome apps, or immersive experiences where the standard title bar is unwanted.

---

## Window Sizing

### windowResizability, defaultSize, defaultPosition

These modifiers work together to configure window sizing and placement:

```swift
WindowGroup {
    ContentView()
        .frame(minWidth: 600, minHeight: 400)
}
.defaultSize(width: 900, height: 600)
.defaultPosition(.center)
.windowResizability(.contentMinSize)
```

**`windowResizability` options:**

| Value | Behavior |
|-------|----------|
| `.automatic` | System decides resize behavior |
| `.contentSize` | Fixed to content size; no user resize; zoom button disabled |
| `.contentMinSize` | Resizable with minimum based on content's `minWidth`/`minHeight` |

**`defaultPosition` options:** `.center`, `.topLeading`, `.top`, `.topTrailing`, `.leading`, `.trailing`, `.bottomLeading`, `.bottom`, `.bottomTrailing`

**Guidelines:**
- Set `minWidth`/`minHeight` via `.frame()` on content, enforce with `.contentMinSize`
- Use `.defaultSize()` for initial dimensions (larger than minimums)
- `defaultSize` also accepts `CGSize`

### windowIdealPlacement (macOS 15.0+)

For precise programmatic positioning, use a closure with display geometry:

```swift
.windowIdealPlacement { context in
    let screen = context.defaultDisplay.visibleArea
    return WindowPlacement(x: screen.midX, y: screen.midY,
                           width: screen.width / 2, height: screen.height)
}
```

---

## MenuBarExtra Style (macOS-only)

Choose between dropdown menu and popover panel for `MenuBarExtra`.

```swift
// Dropdown menu (default)
MenuBarExtra("Status", systemImage: "chart.bar") {
    Button("Action") { /* ... */ }
}
.menuBarExtraStyle(.menu)

// Popover panel with custom SwiftUI content
MenuBarExtra("Status", systemImage: "chart.bar") {
    DashboardView()
}
.menuBarExtraStyle(.window)
```

---

## Navigation Layout (macOS behavior)

### NavigationSplitView

On macOS, `NavigationSplitView` displays columns side-by-side (never overlaid). The sidebar gets a translucent material background. Columns support variable-width resizing by the user.

```swift
NavigationSplitView {
    List(items, selection: $selectedId) { item in
        Text(item.name)
    }
    .navigationSplitViewColumnWidth(min: 180, ideal: 220, max: 300)
} detail: {
    DetailView(id: selectedId)
}
.navigationSplitViewStyle(.balanced)
```

Use the three-column variant (`sidebar` / `content` / `detail`) for master-detail-detail layouts. Customize column widths with `.navigationSplitViewColumnWidth(min:ideal:max:)`.

### Inspector (macOS 14.0+)

A trailing-edge panel for supplementary information. On macOS, it appears as a sidebar-style panel that can be resized by dragging its edge.

```swift
struct ContentView: View {
    @State private var showInspector = false

    var body: some View {
        MainContent()
            .inspector(isPresented: $showInspector) {
                InspectorView()
                    .inspectorColumnWidth(min: 200, ideal: 250, max: 400)
            }
            .toolbar {
                ToolbarItem {
                    Button {
                        showInspector.toggle()
                    } label: {
                        Label("Inspector", systemImage: "info.circle")
                    }
                }
            }
    }
}
```

---

## Commands & Keyboard

### Commands, CommandGroup, CommandMenu

Define menu bar commands. On macOS, these populate the menu bar directly. On iOS, they create key commands.

```swift
.commands {
    CommandMenu("Tools") {
        Button("Run Analysis") { /* ... */ }
            .keyboardShortcut("r", modifiers: [.command, .shift])
    }
    CommandGroup(after: .newItem) {
        Button("New From Template...") { /* ... */ }
    }
}
```

**`CommandGroup` placement options:** `.replacing(_:)` replaces a system group, `.before(_:)` / `.after(_:)` inserts adjacent to it. Common placements: `.newItem`, `.saveItem`, `.help`, `.toolbar`, `.sidebar`.

### KeyboardShortcut

On macOS, shortcuts are displayed alongside menu items and in button tooltips on hover.

```swift
Button("Save") {
    save()
}
.keyboardShortcut("s", modifiers: .command)

Button("Delete") {
    delete()
}
.keyboardShortcut(.delete, modifiers: .command)
```

### openWindow

Programmatically open a window. If the target window is already open, brings it to the front.

```swift
struct ToolbarActions: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Connection Doctor") {
            openWindow(id: "connection-doctor")
        }

        Button("Show Message") {
            openWindow(value: message.id)  // Type-matched to WindowGroup
        }
    }
}
```

---

## Best Practices

- **Use `.unified` or `.unifiedCompact`** for most apps — `.expanded` only when you need many toolbar items
- **Set min frame sizes on content** and use `.windowResizability(.contentMinSize)` to enforce them
- **Always provide `defaultSize`** so new windows start at a reasonable size
- **Use `NavigationSplitView`** for sidebar navigation — not `HSplitView`
- **Use `Inspector`** for supplementary panels — it integrates with the toolbar automatically
- **Define `Commands`** for all repeatable actions — users expect keyboard shortcuts on macOS
- **Use `#if os(macOS)`** to wrap macOS-only window configuration in multiplatform projects
```

## File: `swiftui-expert-skill/references/performance-patterns.md`
```markdown
# SwiftUI Performance Patterns Reference

## Table of Contents

- [Performance Optimization](#performance-optimization)
- [Anti-Patterns](#anti-patterns)
- [Summary Checklist](#summary-checklist)

## Performance Optimization

### 1. Avoid Redundant State Updates

SwiftUI doesn't compare values before triggering updates:

```swift
// BAD - triggers update even if value unchanged
.onReceive(publisher) { value in
    self.currentValue = value  // Always triggers body re-evaluation
}

// GOOD - only update when different
.onReceive(publisher) { value in
    if self.currentValue != value {
        self.currentValue = value
    }
}
```

### 2. Optimize Hot Paths

Hot paths are frequently executed code (scroll handlers, animations, gestures):

```swift
// BAD - updates state on every scroll position change
.onPreferenceChange(ScrollOffsetKey.self) { offset in
    shouldShowTitle = offset.y <= -32  // Fires constantly during scroll!
}

// GOOD - only update when threshold crossed
.onPreferenceChange(ScrollOffsetKey.self) { offset in
    let shouldShow = offset.y <= -32
    if shouldShow != shouldShowTitle {
        shouldShowTitle = shouldShow  // Fires only when crossing threshold
    }
}
```

### 3. Pass Only What Views Need

**Avoid passing large "config" or "context" objects.** Pass only the specific values each view needs.

```swift
// Good - pass specific values
ThemeSelector(theme: config.theme)
FontSizeSlider(fontSize: config.fontSize)

// Avoid - passing entire config (creates broad dependency)
ThemeSelector(config: config)  // Notified of ALL config changes
```

With `ObservableObject`, any `@Published` change triggers all observers. With `@Observable`, views update only when accessed properties change, but passing entire objects still creates broader dependencies than necessary.

### 4. Use Equatable Views

For views with expensive bodies, conform to `Equatable`:

```swift
struct ExpensiveView: View, Equatable {
    let data: SomeData

    static func == (lhs: Self, rhs: Self) -> Bool {
        lhs.data.id == rhs.data.id  // Custom equality check
    }

    var body: some View {
        // Expensive computation
    }
}

// Usage
ExpensiveView(data: data)
    .equatable()  // Use custom equality
```

**Caution**: If you add new state or dependencies to your view, remember to update your `==` function!

### 5. POD Views for Fast Diffing

**POD (Plain Old Data) views use `memcmp` for fastest diffing.** A view is POD if it only contains simple value types and no property wrappers.

```swift
// POD view - fastest diffing
struct FastView: View {
    let title: String
    let count: Int
    
    var body: some View {
        Text("\(title): \(count)")
    }
}

// Non-POD view - uses reflection or custom equality
struct SlowerView: View {
    let title: String
    @State private var isExpanded = false  // Property wrapper makes it non-POD
    
    var body: some View {
        Text(title)
    }
}
```

**Advanced Pattern**: Wrap expensive non-POD views in POD parent views:

```swift
// POD wrapper for fast diffing
struct ExpensiveView: View {
    let value: Int
    
    var body: some View {
        ExpensiveViewInternal(value: value)
    }
}

// Internal view with state
private struct ExpensiveViewInternal: View {
    let value: Int
    @State private var item: Item?
    
    var body: some View {
        // Expensive rendering
    }
}
```

**Why**: The POD parent uses fast `memcmp` comparison. Only when `value` changes does the internal view get diffed.

### 6. Lazy Loading

Use lazy containers for large collections:

```swift
// BAD - creates all views immediately
ScrollView {
    VStack {
        ForEach(items) { item in
            ExpensiveRow(item: item)
        }
    }
}

// GOOD - creates views on demand
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ExpensiveRow(item: item)
        }
    }
}
```

**iOS 26+ note**: Nested scroll views containing lazy stacks now automatically defer loading their children until they are about to appear, matching the behavior of top-level lazy stacks. This benefits patterns like horizontal photo carousels inside a vertical scroll view.

> Source: "What's new in SwiftUI" (WWDC25, session 256)

### 7. Task Cancellation

Cancel async work when view disappears:

```swift
struct DataView: View {
    @State private var data: [Item] = []

    var body: some View {
        List(data) { item in
            Text(item.name)
        }
        .task {
            // Automatically cancelled when view disappears
            data = await fetchData()
        }
    }
}
```

### 8. Debug View Updates

**Use `Self._printChanges()` or `Self._logChanges()` to debug unexpected view updates.**

```swift
struct DebugView: View {
    @State private var count = 0
    @State private var name = ""
    
    var body: some View {
        #if DEBUG
        let _ = Self._logChanges()  // Xcode 15.1+: logs to com.apple.SwiftUI subsystem
        #endif
        
        VStack {
            Text("Count: \(count)")
            Text("Name: \(name)")
        }
    }
}
```

- `Self._printChanges()`: Prints which properties changed to standard output.
- `Self._logChanges()` (iOS 17+): Logs to the `com.apple.SwiftUI` subsystem with category "Changed Body Properties", using `os_log` for structured output.

Both print `@self` when the view value itself changed and `@identity` when the view's persistent data was recycled.

**Why**: This helps identify which state changes are causing view updates. Isolating redraw triggers into single-responsibility subviews is often the fix -- extracting a subview means SwiftUI can skip its body when its inputs haven't changed.

### 9. Eliminate Unnecessary Dependencies

**Narrow state scope to reduce update fan-out.** Instead of passing an entire `@Observable` model to a row view (which creates a dependency on all accessed properties), pass only the specific values the view needs as `let` properties.

```swift
// Bad - broad dependency on entire model
struct ItemRow: View {
    @Environment(AppModel.self) private var model
    let item: Item
    var body: some View { Text(item.name).foregroundStyle(model.theme.primaryColor) }
}

// Good - narrow dependency
struct ItemRow: View {
    let item: Item
    let themeColor: Color
    var body: some View { Text(item.name).foregroundStyle(themeColor) }
}
```

**Avoid storing frequently-changing values in the environment.** Even when a view doesn't read the changed key, SwiftUI still checks all environment readers. This cost adds up with many views and frequent updates (geometry values, timers).

> Source: "Optimize SwiftUI performance with Instruments" (WWDC25, session 306)

### 10. @Observable Dependency Granularity

**Consider per-item `@Observable` state holders (one per row/item) to narrow update scope.** When multiple list items share a dependency on the same `@Observable` array, changing one element causes all items to re-evaluate their bodies.

```swift
// BAD - all item views depend on the full favorites array
@Observable
class ModelData {
    var favorites: [Landmark] = []

    func isFavorite(_ landmark: Landmark) -> Bool {
        favorites.contains(landmark)
    }
}

struct LandmarkRow: View {
    let landmark: Landmark
    @Environment(ModelData.self) private var model

    var body: some View {
        HStack {
            Text(landmark.name)
            if model.isFavorite(landmark) {
                Image(systemName: "heart.fill")
            }
        }
    }
}

// GOOD - each item has its own observable view model
@Observable
class LandmarkViewModel {
    var isFavorite: Bool = false
}

struct LandmarkRow: View {
    let landmark: Landmark
    let viewModel: LandmarkViewModel

    var body: some View {
        HStack {
            Text(landmark.name)
            if viewModel.isFavorite {
                Image(systemName: "heart.fill")
            }
        }
    }
}
```

**Why**: With the bad pattern, toggling one favorite marks the entire array as changed, causing every `LandmarkRow` to re-run its body. With per-item view models, only the toggled item's body runs.

> Source: "Optimize SwiftUI performance with Instruments" (WWDC25, session 306)

### 11. Off-Main-Thread Closures

**SwiftUI may call certain closures on a background thread for performance.** These closures must be `Sendable` and should avoid accessing `@MainActor`-isolated state directly. Instead, capture needed values in the closure's capture list.

Closures that may run off the main thread:
- `Shape.path(in:)`
- `visualEffect` closure
- `Layout` protocol methods
- `onGeometryChange` transform closure

```swift
// BAD - accessing @MainActor state directly
.visualEffect { content, geometry in
    content.blur(radius: self.pulse ? 5 : 0)  // Compiler error: @MainActor isolated
}

// GOOD - capture the value
.visualEffect { [pulse] content, geometry in
    content.blur(radius: pulse ? 5 : 0)
}
```

> Source: "Explore concurrency in SwiftUI" (WWDC25, session 266)

### 12. Common Performance Issues

**Be aware of common performance bottlenecks in SwiftUI:**

- View invalidation storms from broad state changes
- Unstable identity in lists causing excessive diffing
- Heavy work in `body` (formatting, sorting, image decoding)
- Layout thrash from deep stacks or preference chains

**When performance issues arise**, suggest the user profile with Instruments (SwiftUI template) to identify specific bottlenecks.

## Anti-Patterns

### 1. Creating Objects in Body

```swift
// BAD - creates new formatter every body call
var body: some View {
    let formatter = DateFormatter()
    formatter.dateStyle = .long
    return Text(formatter.string(from: date))
}

// GOOD - static or stored formatter
private static let dateFormatter: DateFormatter = {
    let f = DateFormatter()
    f.dateStyle = .long
    return f
}()

var body: some View {
    Text(Self.dateFormatter.string(from: date))
}
```

### 2. Heavy Computation in Body

**Keep view body simple and pure.** Avoid side effects, dispatching, or complex logic.

```swift
// BAD - sorts array every body call
var body: some View {
    List(items.sorted { $0.name < $1.name }) { item in Text(item.name) }
}

// GOOD - compute once, update via onChange or a computed property in the model
@State private var sortedItems: [Item] = []

var body: some View {
    List(sortedItems) { item in Text(item.name) }
        .onChange(of: items) { _, newItems in
            sortedItems = newItems.sorted { $0.name < $1.name }
        }
}
```

Move sorting, filtering, and formatting into models or computed properties. The `body` should be a pure structural representation of state.

### 3. Unnecessary State

```swift
// BAD - derived state stored separately
@State private var items: [Item] = []
@State private var itemCount: Int = 0  // Unnecessary!

// GOOD - compute derived values
@State private var items: [Item] = []

var itemCount: Int { items.count }  // Computed property
```

## Summary Checklist

- [ ] State updates check for value changes before assigning
- [ ] Hot paths minimize state updates
- [ ] Pass only needed values to views (avoid large config objects)
- [ ] Large lists use `LazyVStack`/`LazyHStack`
- [ ] No object creation in `body`
- [ ] Heavy computation moved out of `body`
- [ ] Body kept simple and pure (no side effects)
- [ ] Derived state computed, not stored
- [ ] Use `Self._logChanges()` or `Self._printChanges()` to debug unexpected updates
- [ ] Equatable conformance for expensive views (when appropriate)
- [ ] Consider POD view wrappers for advanced optimization
- [ ] Consider using granular @Observable dependencies for list items (smaller observable units per row when it measurably reduces updates)
- [ ] Frequently-changing values not stored in the environment
- [ ] Sendable closures (Shape, visualEffect, Layout) capture values instead of accessing @MainActor state
```

## File: `swiftui-expert-skill/references/scroll-patterns.md`
```markdown
# SwiftUI ScrollView Patterns Reference

## Table of Contents

- [ScrollViewReader for Programmatic Scrolling](#scrollviewreader-for-programmatic-scrolling)
- [Scroll Position Tracking](#scroll-position-tracking)
- [Scroll Transitions and Effects](#scroll-transitions-and-effects)
- [Scroll Target Behavior](#scroll-target-behavior)
- [Summary Checklist](#summary-checklist)

## ScrollViewReader for Programmatic Scrolling

**Use `ScrollViewReader` for scroll-to-top, scroll-to-bottom, and anchor-based jumps.**

```swift
struct ChatView: View {
    @State private var messages: [Message] = []
    private let bottomID = "bottom"
    
    var body: some View {
        ScrollViewReader { proxy in
            ScrollView {
                LazyVStack {
                    ForEach(messages) { message in
                        MessageRow(message: message)
                            .id(message.id)
                    }
                    Color.clear
                        .frame(height: 1)
                        .id(bottomID)
                }
            }
            .onChange(of: messages.count) { _, _ in
                withAnimation {
                    proxy.scrollTo(bottomID, anchor: .bottom)
                }
            }
            .onAppear {
                proxy.scrollTo(bottomID, anchor: .bottom)
            }
        }
    }
}
```

### Scroll-to-Top Pattern

```swift
struct FeedView: View {
    @State private var items: [Item] = []
    @State private var scrollToTop = false
    private let topID = "top"
    
    var body: some View {
        ScrollViewReader { proxy in
            ScrollView {
                LazyVStack {
                    Color.clear
                        .frame(height: 1)
                        .id(topID)
                    
                    ForEach(items) { item in
                        ItemRow(item: item)
                    }
                }
            }
            .onChange(of: scrollToTop) { _, shouldScroll in
                if shouldScroll {
                    withAnimation {
                        proxy.scrollTo(topID, anchor: .top)
                    }
                    scrollToTop = false
                }
            }
        }
    }
}
```

**Why**: `ScrollViewReader` provides programmatic scroll control with stable anchors. Always use stable IDs and explicit animations.

## Scroll Position Tracking

### Basic Scroll Position

**Avoid** - Storing scroll position directly triggers view updates on every scroll frame:

```swift
// ❌ Bad Practice - causes unnecessary re-renders
struct ContentView: View {
    @State private var scrollPosition: CGFloat = 0

    var body: some View {
        ScrollView {
            content
                .background(
                    GeometryReader { geometry in
                        Color.clear
                            .preference(
                                key: ScrollOffsetPreferenceKey.self,
                                value: geometry.frame(in: .named("scroll")).minY
                            )
                    }
                )
        }
        .coordinateSpace(name: "scroll")
        .onPreferenceChange(ScrollOffsetPreferenceKey.self) { value in
            scrollPosition = value
        }
    }
}
```

**Preferred** - Check scroll position and update a flag based on thresholds for smoother, more efficient scrolling:

```swift
// ✅ Good Practice - only updates state when crossing threshold
struct ContentView: View {
    @State private var startAnimation: Bool = false

    var body: some View {
        ScrollView {
            content
                .background(
                    GeometryReader { geometry in
                        Color.clear
                            .preference(
                                key: ScrollOffsetPreferenceKey.self,
                                value: geometry.frame(in: .named("scroll")).minY
                            )
                    }
                )
        }
        .coordinateSpace(name: "scroll")
        .onPreferenceChange(ScrollOffsetPreferenceKey.self) { value in
            if value < -100 {
                startAnimation = true
            } else {
                startAnimation = false
            }
        }
    }
}

struct ScrollOffsetPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = nextValue()
    }
}
```

### Scroll-Based Header Visibility

```swift
struct ContentView: View {
    @State private var showHeader = true
    
    var body: some View {
        VStack(spacing: 0) {
            if showHeader {
                HeaderView()
                    .transition(.move(edge: .top))
            }
            
            ScrollView {
                content
                    .background(
                        GeometryReader { geometry in
                            Color.clear
                                .preference(
                                    key: ScrollOffsetPreferenceKey.self,
                                    value: geometry.frame(in: .named("scroll")).minY
                                )
                        }
                    )
            }
            .coordinateSpace(name: "scroll")
            .onPreferenceChange(ScrollOffsetPreferenceKey.self) { offset in
                if offset < -50 { // Scrolling down
                   withAnimation { showHeader = false }
                } else if offset > 50 { // Scrolling up
                  withAnimation { showHeader = true }
                }
            }
        }
    }
}
```

## Scroll Transitions and Effects

> **iOS 17+**: All APIs in this section require iOS 17 or later.

### Scroll-Based Opacity

```swift
struct ParallaxView: View {
    var body: some View {
        ScrollView {
            LazyVStack(spacing: 20) {
                ForEach(items) { item in
                    ItemCard(item: item)
                        .visualEffect { content, geometry in
                            let frame = geometry.frame(in: .scrollView)
                            let distance = min(0, frame.minY)
                            return content
                                .opacity(1 + distance / 200)
                        }
                }
            }
        }
    }
}
```

### Parallax Effect

```swift
struct ParallaxHeader: View {
    var body: some View {
        ScrollView {
            VStack(spacing: 0) {
                Image("hero")
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(height: 300)
                    .visualEffect { content, geometry in
                        let offset = geometry.frame(in: .scrollView).minY
                        return content
                            .offset(y: offset > 0 ? -offset * 0.5 : 0)
                    }
                    .clipped()
                
                ContentView()
            }
        }
    }
}
```

## Scroll Target Behavior

> **iOS 17+**: All APIs in this section require iOS 17 or later.

### Paging ScrollView

```swift
struct PagingView: View {
    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: 0) {
                ForEach(pages) { page in
                    PageView(page: page)
                        .containerRelativeFrame(.horizontal)
                }
            }
            .scrollTargetLayout()
        }
        .scrollTargetBehavior(.paging)
    }
}
```

### Snap to Items

```swift
struct SnapScrollView: View {
    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: 16) {
                ForEach(items) { item in
                    ItemCard(item: item)
                        .frame(width: 280)
                }
            }
            .scrollTargetLayout()
        }
        .scrollTargetBehavior(.viewAligned)
        .contentMargins(.horizontal, 20)
    }
}
```

## Summary Checklist

- [ ] Use `ScrollViewReader` with stable IDs for programmatic scrolling
- [ ] Always use explicit animations with `scrollTo()`
- [ ] Use `.visualEffect` for scroll-based visual changes
- [ ] Use `.scrollTargetBehavior(.paging)` for paging behavior
- [ ] Use `.scrollTargetBehavior(.viewAligned)` for snap-to-item behavior
- [ ] Gate frequent scroll position updates by thresholds
- [ ] Use preference keys for custom scroll position tracking
```

## File: `swiftui-expert-skill/references/sheet-navigation-patterns.md`
```markdown
# SwiftUI Sheet, Navigation & Inspector Patterns Reference

## Table of Contents

- [Sheet Patterns](#sheet-patterns)
- [Navigation Patterns](#navigation-patterns)
- [Multi-Column Navigation with NavigationSplitView](#multi-column-navigation-with-navigationsplitview)
- [Inspector](#inspector)
- [Presentation Modifiers](#presentation-modifiers)
- [Summary Checklist](#summary-checklist)

## Sheet Patterns

### Item-Driven Sheets (Preferred)

**Use `.sheet(item:)` instead of `.sheet(isPresented:)` when presenting model-based content.**

```swift
// Good - item-driven
@State private var selectedItem: Item?

var body: some View {
    List(items) { item in
        Button(item.name) {
            selectedItem = item
        }
    }
    .sheet(item: $selectedItem) { item in
        ItemDetailSheet(item: item)
    }
}

// Avoid - boolean flag requires separate state
@State private var showSheet = false
@State private var selectedItem: Item?

var body: some View {
    List(items) { item in
        Button(item.name) {
            selectedItem = item
            showSheet = true
        }
    }
    .sheet(isPresented: $showSheet) {
        if let selectedItem {
            ItemDetailSheet(item: selectedItem)
        }
    }
}
```

**Why**: `.sheet(item:)` automatically handles presentation state and avoids optional unwrapping in the sheet body.

### Sheets Own Their Actions

**Sheets should handle their own dismiss and actions internally** using `@Environment(\.dismiss)`. Avoid passing `onSave`/`onCancel` closures from the parent -- it creates callback prop-drilling and reduces reusability.

```swift
struct EditItemSheet: View {
    @Environment(\.dismiss) private var dismiss
    let item: Item
    @State private var name: String

    init(item: Item) {
        self.item = item
        _name = State(initialValue: item.name)
    }

    var body: some View {
        NavigationStack {
            Form { TextField("Name", text: $name) }
                .navigationTitle("Edit Item")
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) { Button("Cancel") { dismiss() } }
                    ToolbarItem(placement: .confirmationAction) { Button("Save") { /* save and dismiss */ } }
                }
        }
    }
}
```

### Enum-Based Sheet Management

When presenting multiple different sheets, use an `Identifiable` enum with `.sheet(item:)` instead of multiple boolean state properties:

```swift
struct ArticlesView: View {
    enum Sheet: Identifiable {
        case add, edit(Article), categories
        var id: String {
            switch self {
            case .add: "add"
            case .edit(let a): "edit-\(a.id)"
            case .categories: "categories"
            }
        }
    }

    @State private var presentedSheet: Sheet?

    var body: some View {
        List { /* ... */ }
            .toolbar {
                Button("Add") { presentedSheet = .add }
            }
            .sheet(item: $presentedSheet) { sheet in
                switch sheet {
                case .add: AddArticleView()
                case .edit(let article): EditArticleView(article: article)
                case .categories: CategoriesView()
                }
            }
    }
}
```

**Why**: A single `@State` property and one `.sheet(item:)` modifier replaces N boolean properties and N sheet modifiers, improving readability and preventing only-one-sheet-at-a-time conflicts.

## Navigation Patterns

### Type-Safe Navigation with NavigationStack

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Profile", value: Route.profile)
                NavigationLink("Settings", value: Route.settings)
            }
            .navigationDestination(for: Route.self) { route in
                switch route {
                case .profile:
                    ProfileView()
                case .settings:
                    SettingsView()
                }
            }
        }
    }
}

enum Route: Hashable {
    case profile
    case settings
}
```

### Programmatic Navigation

```swift
struct ContentView: View {
    @State private var navigationPath = NavigationPath()
    
    var body: some View {
        NavigationStack(path: $navigationPath) {
            List {
                Button("Go to Detail") {
                    navigationPath.append(DetailRoute.item(id: 1))
                }
            }
            .navigationDestination(for: DetailRoute.self) { route in
                switch route {
                case .item(let id):
                    ItemDetailView(id: id)
                }
            }
        }
    }
}

enum DetailRoute: Hashable {
    case item(id: Int)
}
```

## Multi-Column Navigation with NavigationSplitView

### Two-Column Layout

Use `NavigationSplitView` for sidebar-driven navigation. Available on iOS 16+, macOS 13+, tvOS 16+, watchOS 9+.

```swift
struct ContentView: View {
    @State private var selectedItem: Item.ID?

    var body: some View {
        NavigationSplitView {
            List(items, selection: $selectedItem) { item in
                Text(item.name)
            }
            .navigationTitle("Items")
        } detail: {
            if let selectedItem, let item = items.first(where: { $0.id == selectedItem }) {
                ItemDetailView(item: item)
            } else {
                ContentUnavailableView("Select an Item", systemImage: "doc")
            }
        }
    }
}
```

### Three-Column Layout

```swift
struct ContentView: View {
    @State private var departmentId: Department.ID?
    @State private var employeeIds = Set<Employee.ID>()

    var body: some View {
        NavigationSplitView {
            List(model.departments, selection: $departmentId) { dept in
                Text(dept.name)
            }
        } content: {
            if let department = model.department(id: departmentId) {
                List(department.employees, selection: $employeeIds) { emp in
                    Text(emp.name)
                }
            } else {
                Text("Select a department")
            }
        } detail: {
            EmployeeDetails(for: employeeIds)
        }
    }
}
```

### Configuration

- **Column visibility**: `NavigationSplitView(columnVisibility: $visibility)` with `NavigationSplitViewVisibility` (`.detailOnly`, `.doubleColumn`, `.all`)
- **Column widths**: `.navigationSplitViewColumnWidth(min:ideal:max:)` on each column
- **Compact column**: `NavigationSplitView(preferredCompactColumn: $column)` to control which column shows on narrow devices
- **Style**: `.navigationSplitViewStyle(.balanced)` or `.prominentDetail` (default)

### Platform Behavior

| Platform | Behavior |
|----------|----------|
| **macOS** | Columns always visible side-by-side; sidebar has translucent material; variable-width column resizing by dragging |
| **iPadOS (regular)** | Sidebar can overlay or push detail; supports column visibility toggle via toolbar button |
| **iOS / iPadOS (compact)** | Collapses into a single `NavigationStack`; sidebar items show disclosure chevrons; back button navigates between columns |
| **iPhone (all sizes)** | Always collapsed into a stack; sidebar appears as the root list; selections push detail onto the stack |
| **watchOS / tvOS** | Collapses into a single stack |

## Inspector

> **Availability:** iOS 17.0+, macOS 14.0+

A trailing-edge panel for supplementary information.

On wider size classes (macOS, iPad landscape), it appears as a **trailing column**. On compact size classes (iPhone), it **adapts to a sheet** automatically.

### Basic Inspector

```swift
struct ShapeEditor: View {
    @State private var showInspector = false

    var body: some View {
        MyEditorView()
            .inspector(isPresented: $showInspector) {
                InspectorContent()
            }
            .toolbar {
                ToolbarItem {
                    Button {
                        showInspector.toggle()
                    } label: {
                        Label("Inspector", systemImage: "info.circle")
                    }
                }
            }
    }
}
```

### Inspector with Column Width

```swift
MyEditorView()
    .inspector(isPresented: $showInspector) {
        InspectorContent()
            .inspectorColumnWidth(min: 200, ideal: 250, max: 400)
    }
```

### Inspector with Fixed Width

```swift
MyEditorView()
    .inspector(isPresented: $showInspector) {
        InspectorContent()
            .inspectorColumnWidth(300)
    }
```

### Platform Behavior

| Platform | Behavior |
|----------|----------|
| **macOS** | Trailing-edge sidebar panel; resizable by dragging edge; integrates with window toolbar |
| **iPadOS (regular)** | Trailing column alongside content; toggleable via toolbar button |
| **iOS / iPadOS (compact)** | Adapts to a sheet presentation; swipe-to-dismiss supported |
| **iPhone (all sizes)** | Always presented as a sheet (no trailing column); dismiss via swipe or button |

> **Tip:** Use `InspectorCommands` in your app's `.commands` to include the default inspector toggle keyboard shortcut.

## Presentation Modifiers

### Full Screen Cover

```swift
struct ContentView: View {
    @State private var showFullScreen = false
    
    var body: some View {
        Button("Show Full Screen") {
            showFullScreen = true
        }
        .fullScreenCover(isPresented: $showFullScreen) {
            FullScreenView()
        }
    }
}
```

### Popover

```swift
struct ContentView: View {
    @State private var showPopover = false
    
    var body: some View {
        Button("Show Popover") {
            showPopover = true
        }
        .popover(isPresented: $showPopover) {
            PopoverContentView()
                .presentationCompactAdaptation(.popover)  // Don't adapt to sheet on iPhone
        }
    }
}
```

For `alert` and `confirmationDialog` API patterns, see `latest-apis.md`.

## Summary Checklist

- [ ] Use `.sheet(item:)` for model-based sheets
- [ ] Sheets own their actions and dismiss internally
- [ ] Use `NavigationStack` with `navigationDestination(for:)` for type-safe navigation
- [ ] Use `NavigationPath` for programmatic navigation
- [ ] Use `NavigationSplitView` for sidebar-driven multi-column layouts
- [ ] Use `Inspector` for trailing-edge supplementary panels
- [ ] Set column widths with `navigationSplitViewColumnWidth(min:ideal:max:)` or `inspectorColumnWidth(min:ideal:max:)`
- [ ] Use appropriate presentation modifiers (sheet, fullScreenCover, popover)
- [ ] Alerts and confirmation dialogs use modern API with actions
- [ ] Avoid passing dismiss/save callbacks to sheets
- [ ] Use enum-based `Identifiable` type with `.sheet(item:)` when presenting multiple sheets
- [ ] Navigation state can be saved/restored when needed
```

## File: `swiftui-expert-skill/references/state-management.md`
```markdown
# SwiftUI State Management Reference

## Table of Contents

- [Property Wrapper Selection Guide](#property-wrapper-selection-guide)
- [@State](#state)
- [Property Wrappers Inside @Observable Classes](#property-wrappers-inside-observable-classes)
- [@Binding](#binding)
- [@FocusState](#focusstate)
- [@StateObject vs @ObservedObject (Legacy - Pre-iOS 17)](#stateobject-vs-observedobject-legacy---pre-ios-17)
- [Don't Pass Values as @State](#dont-pass-values-as-state)
- [@Bindable (iOS 17+)](#bindable-ios-17)
- [let vs var for Passed Values](#let-vs-var-for-passed-values)
- [Environment and Preferences](#environment-and-preferences)
- [Decision Flowchart](#decision-flowchart)
- [State Privacy Rules](#state-privacy-rules)
- [Avoid Nested ObservableObject](#avoid-nested-observableobject)
- [Key Principles](#key-principles)

## Property Wrapper Selection Guide

| Wrapper | Use When | Notes |
|---------|----------|-------|
| `@State` | Internal view state that triggers updates | Must be `private` |
| `@Binding` | Child view needs to modify parent's state | Don't use for read-only |
| `@Bindable` | iOS 17+: View receives `@Observable` object and needs bindings | For injected observables |
| `let` | Read-only value passed from parent | Simplest option |
| `var` | Read-only value that child observes via `.onChange()` | For reactive reads |

**Legacy (Pre-iOS 17):**
| Wrapper | Use When | Notes |
|---------|----------|-------|
| `@StateObject` | View owns an `ObservableObject` instance | Use `@State` with `@Observable` instead |
| `@ObservedObject` | View receives an `ObservableObject` from outside | Never create inline |

## @State

Always mark `@State` properties as `private`. Use for internal view state that triggers UI updates.

```swift
// Correct
@State private var isAnimating = false
@State private var selectedTab = 0
```

**Why Private?** Marking state as `private` makes it clear what's created by the view versus what's passed in. It also prevents accidentally passing initial values that will be ignored (see "Don't Pass Values as @State" below).

### iOS 17+ with @Observable (Preferred)

**Always prefer `@Observable` over `ObservableObject`.** With iOS 17's `@Observable` macro, use `@State` instead of `@StateObject`:

```swift
@Observable
@MainActor  // Always mark @Observable classes with @MainActor
final class DataModel {
    var name = "Some Name"
    var count = 0
}

struct MyView: View {
    @State private var model = DataModel()  // Use @State, not @StateObject

    var body: some View {
        VStack {
            TextField("Name", text: $model.name)
            Stepper("Count: \(model.count)", value: $model.count)
        }
    }
}
```

**Critical**: When a view *owns* an `@Observable` object, always use `@State` -- not `let`. Without `@State`, SwiftUI may recreate the instance when a parent view redraws, losing accumulated state. `@State` tells SwiftUI to preserve the instance across view redraws. Using `@State` also provides bindings directly (no need for `@Bindable`).

**Note**: You may want to mark `@Observable` classes with `@MainActor` to ensure thread safety with SwiftUI, unless your project or package uses Default Actor Isolation set to `MainActor`—in which case, the explicit attribute is redundant and can be omitted.

## Property Wrappers Inside @Observable Classes

**Critical**: The `@Observable` macro transforms stored properties to add observation tracking. Property wrappers (like `@AppStorage`, `@SceneStorage`, `@Query`) also transform properties with their own storage. These two transformations conflict, causing a compiler error.

**Always annotate property-wrapper properties with `@ObservationIgnored` inside `@Observable` classes.**

```swift
@Observable
@MainActor
final class SettingsModel {
    // WRONG - compiler error: property wrappers conflict with @Observable
    // @AppStorage("username") var username = ""

    // CORRECT - @ObservationIgnored prevents the conflict
    @ObservationIgnored @AppStorage("username") var username = ""
    @ObservationIgnored @AppStorage("isDarkMode") var isDarkMode = false

    // Regular stored properties work fine with @Observable
    var isLoading = false
}
```

This applies to **any** property wrapper used inside an `@Observable` class, including but not limited to:
- `@AppStorage`
- `@SceneStorage`
- `@Query` (SwiftData)

**Note**: Since `@ObservationIgnored` disables observation tracking for that property, SwiftUI won't detect changes through the Observation framework. However, property wrappers like `@AppStorage` already notify SwiftUI of changes through their own mechanisms (e.g., UserDefaults KVO), so views still update correctly.

**Never remove `@ObservationIgnored`** from property-wrapper properties in `@Observable` classes — doing so causes a compiler error.

## @Binding

Use only when child view needs to **modify** parent's state. If child only reads the value, use `let` instead.

```swift
// Parent
struct ParentView: View {
    @State private var isSelected = false

    var body: some View {
        ChildView(isSelected: $isSelected)
    }
}

// Child - will modify the value
struct ChildView: View {
    @Binding var isSelected: Bool

    var body: some View {
        Button("Toggle") {
            isSelected.toggle()
        }
    }
}
```

### When NOT to use @Binding

- **Don't use `@Binding` for read-only values.** If the child only displays the value and never modifies it, use `let` instead. `@Binding` adds unnecessary overhead and implies a write contract that doesn't exist.

## @FocusState

Use `@FocusState` to control text input focus in SwiftUI. Choose the focus value type based on how many fields the view manages.

### Bool vs enum

- Use `@FocusState private var isFocused: Bool` when the view has a single focusable field.
- Use a `Hashable` enum optional value for multiple fields, for better readability and type safety.

### Single Field: Bool

```swift
@FocusState private var isFocused: Bool

TextField("Email", text: $email)
    .focused($isFocused)
    .onAppear { isFocused = true }
```

### Multiple Fields: Enum (Preferred)

Use a `Hashable` enum optional focus value when a view manages multiple fields.

```swift
enum Field: Hashable { case name, email, password }
@FocusState private var focusedField: Field?

TextField("Name", text: $name)
    .focused($focusedField, equals: .name)
TextField("Email", text: $email)
    .focused($focusedField, equals: .email)
```

Set `focusedField = .email` to move focus programmatically; set `nil` to dismiss the keyboard.

## @StateObject vs @ObservedObject (Legacy - Pre-iOS 17)

**Note**: Always prefer `@Observable` with `@State` for iOS 17+.

The key distinction is **ownership**: `@StateObject` when the view **creates and owns** the object; `@ObservedObject` when the view **receives** it from outside.

```swift
// View creates it → @StateObject
@StateObject private var viewModel = MyViewModel()

// View receives it → @ObservedObject
@ObservedObject var viewModel: MyViewModel
```

**Never** create an `ObservableObject` inline with `@ObservedObject` -- it recreates the instance on every view update.

### @StateObject instantiation in View's initializer

Prefer storing the `@StateObject` in the parent view and passing it down. If you must create one in a custom initializer, pass the expression directly to `StateObject(wrappedValue:)` so the `@autoclosure` prevents redundant allocations:

```swift
// Inside a View's init(movie:):
// WRONG — assigning to a local first defeats @autoclosure
let vm = MovieDetailsViewModel(movie: movie)
_viewModel = StateObject(wrappedValue: vm)

// CORRECT — inline expression defers creation
_viewModel = StateObject(wrappedValue: MovieDetailsViewModel(movie: movie))
```

**Modern Alternative**: Use `@Observable` with `@State` instead.

## Don't Pass Values as @State

**Critical**: Never declare passed values as `@State` or `@StateObject`. They only accept an initial value and ignore subsequent updates from the parent.

```swift
// WRONG - child ignores parent updates
struct ChildView: View {
    @State var item: Item  // Shows initial value forever!
    var body: some View { Text(item.name) }
}

// CORRECT - child receives updates
struct ChildView: View {
    let item: Item  // Or @Binding if child needs to modify
    var body: some View { Text(item.name) }
}
```

**Prevention**: Always mark `@State` and `@StateObject` as `private`. This prevents them from appearing in the generated initializer.

## @Bindable (iOS 17+)

Use when receiving an `@Observable` object from outside and needing bindings:

```swift
@Observable
final class UserModel {
    var name = ""
    var email = ""
}

struct ParentView: View {
    @State private var user = UserModel()

    var body: some View {
        EditUserView(user: user)
    }
}

struct EditUserView: View {
    @Bindable var user: UserModel  // Received from parent, needs bindings

    var body: some View {
        Form {
            TextField("Name", text: $user.name)
            TextField("Email", text: $user.email)
        }
    }
}
```

## let vs var for Passed Values

### Use `let` for read-only display

```swift
struct ProfileHeader: View {
    let username: String
    let avatarURL: URL

    var body: some View {
        HStack {
            AsyncImage(url: avatarURL)
            Text(username)
        }
    }
}
```

### Use `var` when reacting to changes with `.onChange()`

```swift
struct ReactiveView: View {
    var externalValue: Int  // Watch with .onChange()
    @State private var displayText = ""

    var body: some View {
        Text(displayText)
            .onChange(of: externalValue) { oldValue, newValue in
                displayText = "Changed from \(oldValue) to \(newValue)"
            }
    }
}
```

## Environment and Preferences

### @Environment

Access environment values provided by SwiftUI or parent views:

```swift
struct MyView: View {
    @Environment(\.colorScheme) private var colorScheme
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Button("Done") { dismiss() }
            .foregroundStyle(colorScheme == .dark ? .white : .black)
    }
}
```

### Custom Environment Values with @Entry

Use the `@Entry` macro (Xcode 16+, backward compatible to iOS 13) to define custom environment values without boilerplate:

```swift
extension EnvironmentValues {
    @Entry var accentTheme: Theme = .default
}

// Inject
ContentView()
    .environment(\.accentTheme, customTheme)

// Access
struct ThemedView: View {
    @Environment(\.accentTheme) private var theme
}
```

The `@Entry` macro replaces the manual `EnvironmentKey` conformance pattern. It also works with `TransactionValues`, `ContainerValues`, and `FocusedValues`.

### @Environment with @Observable (iOS 17+ - Preferred)

**Always prefer this pattern** for sharing state through the environment:

```swift
@Observable
@MainActor
final class AppState {
    var isLoggedIn = false
}

// Inject
ContentView()
    .environment(AppState())

// Access
struct ChildView: View {
    @Environment(AppState.self) private var appState
}
```

### @EnvironmentObject (Legacy - Pre-iOS 17)

Legacy pattern: inject with `.environmentObject(AppState())`, access with `@EnvironmentObject var appState: AppState`. Prefer `@Observable` with `@Environment` instead.

## Decision Flowchart

```
Is this value owned by this view?
├─ YES: Is it a simple value type?
│       ├─ YES → @State private var
│       └─ NO (class):
│           ├─ Use @Observable → @State private var (mark class @MainActor)
│           └─ Legacy ObservableObject → @StateObject private var
│
└─ NO (passed from parent):
    ├─ Does child need to MODIFY it?
    │   ├─ YES → @Binding var
    │   └─ NO: Does child need BINDINGS to its properties?
    │       ├─ YES (@Observable) → @Bindable var
    │       └─ NO: Does child react to changes?
    │           ├─ YES → var + .onChange()
    │           └─ NO → let
    │
    └─ Is it a legacy ObservableObject from parent?
        └─ YES → @ObservedObject var (consider migrating to @Observable)
```

## State Privacy Rules

**All view-owned state should be `private`:**

```swift
// Correct - clear what's created vs passed
struct MyView: View {
    // Created by view - private
    @State private var isExpanded = false
    @State private var viewModel = ViewModel()
    @AppStorage("theme") private var theme = "light"
    @Environment(\.colorScheme) private var colorScheme
    
    // Passed from parent - not private
    let title: String
    @Binding var isSelected: Bool
    @Bindable var user: User
    
    var body: some View {
        // ...
    }
}
```

**Why**: This makes dependencies explicit and improves code completion for the generated initializer.

## Avoid Nested ObservableObject

**Note**: This limitation only applies to `ObservableObject`. `@Observable` fully supports nested observed objects.

SwiftUI can't track changes through nested `ObservableObject` properties. Workaround: pass the nested object directly to child views as `@ObservedObject`. With `@Observable`, nesting works automatically.

## Key Principles

1. **Always prefer `@Observable` over `ObservableObject`** for new code
2. **Mark `@Observable` classes with `@MainActor` for thread safety (unless using default actor isolation)`**
3. Use `@State` with `@Observable` classes (not `@StateObject`)
4. Use `@Bindable` for injected `@Observable` objects that need bindings
5. **Always mark `@State` and `@StateObject` as `private`**
6. **Never declare passed values as `@State` or `@StateObject`**
7. With `@Observable`, nested objects work fine; with `ObservableObject`, pass nested objects directly to child views
8. **Always add `@ObservationIgnored` to property wrappers** (e.g., `@AppStorage`, `@SceneStorage`, `@Query`) inside `@Observable` classes — they conflict with the macro's property transformation
```

## File: `swiftui-expert-skill/references/view-structure.md`
```markdown
# SwiftUI View Structure Reference

## Table of Contents

- [View Structure Principles](#view-structure-principles)
- [Prefer Modifiers Over Conditional Views](#prefer-modifiers-over-conditional-views)
- [Extract Subviews, Not Computed Properties](#extract-subviews-not-computed-properties)
- [When @ViewBuilder Functions Are Acceptable](#when-viewbuilder-functions-are-acceptable)
- [When to Extract Subviews](#when-to-extract-subviews)
- [Container View Pattern](#container-view-pattern)
- [ZStack vs overlay/background](#zstack-vs-overlaybackground)
- [Compositing Group Before Clipping](#compositing-group-before-clipping)
- [Reusable Styling with ViewModifier](#reusable-styling-with-viewmodifier)
- [Skeleton Loading with Redacted Views](#skeleton-loading-with-redacted-views)
- [UIViewRepresentable Essentials](#uiviewrepresentable-essentials)
- [Summary Checklist](#summary-checklist)

## View Structure Principles

SwiftUI's diffing algorithm compares view hierarchies to determine what needs updating. Proper view composition directly impacts performance.

## Prefer Modifiers Over Conditional Views

**Prefer "no-effect" modifiers over conditionally including views.** When you introduce a branch, consider whether you're representing multiple views or two states of the same view.

### Use Opacity Instead of Conditional Inclusion

```swift
// Good - same view, different states
SomeView()
    .opacity(isVisible ? 1 : 0)

// Avoid - creates/destroys view identity
if isVisible {
    SomeView()
}
```

**Why**: Conditional view inclusion can cause loss of state, poor animation performance, and breaks view identity. Using modifiers maintains view identity across state changes.

### When Conditionals Are Appropriate

Use conditionals when you truly have **different views**, not different states:

```swift
// Correct - fundamentally different views
if isLoggedIn {
    DashboardView()
} else {
    LoginView()
}

// Correct - optional content
if let user {
    UserProfileView(user: user)
}
```

### Conditional View Modifier Extensions Break Identity

A common pattern is an `if`-based `View` extension for conditional modifiers. This changes the view's return type between branches, which destroys view identity and breaks animations:

```swift
// Problematic -- different return types per branch
extension View {
    @ViewBuilder func `if`<T: View>(_ condition: Bool, transform: (Self) -> T) -> some View {
        if condition {
            transform(self)  // Returns T
        } else {
            self              // Returns Self
        }
    }
}
```

Prefer applying the modifier directly with a ternary or always-present modifier:

```swift
// Good -- same view identity maintained
Text("Hello")
    .opacity(isHighlighted ? 1 : 0.5)

// Good -- modifier always present, value changes
Text("Hello")
    .foregroundStyle(isError ? .red : .primary)
```

## Extract Subviews, Not Computed Properties

### The Problem with @ViewBuilder Functions

When you use `@ViewBuilder` functions or computed properties for complex views, the entire function re-executes on every parent state change:

```swift
// BAD - re-executes complexSection() on every tap
struct ParentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Button("Tap: \(count)") { count += 1 }
            complexSection()  // Re-executes every tap!
        }
    }

    @ViewBuilder
    func complexSection() -> some View {
        // Complex views that re-execute unnecessarily
        ForEach(0..<100) { i in
            HStack {
                Image(systemName: "star")
                Text("Item \(i)")
                Spacer()
                Text("Detail")
            }
        }
    }
}
```

### The Solution: Separate Structs

Extract to separate `struct` views. SwiftUI can skip their `body` when inputs don't change:

```swift
// GOOD - ComplexSection body SKIPPED when its inputs don't change
struct ParentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Button("Tap: \(count)") { count += 1 }
            ComplexSection()  // Body skipped during re-evaluation
        }
    }
}

struct ComplexSection: View {
    var body: some View {
        ForEach(0..<100) { i in
            HStack {
                Image(systemName: "star")
                Text("Item \(i)")
                Spacer()
                Text("Detail")
            }
        }
    }
}
```

### Why This Works

1. SwiftUI compares the `ComplexSection` struct (which has no properties)
2. Since nothing changed, SwiftUI skips calling `ComplexSection.body`
3. The complex view code never executes unnecessarily

## When @ViewBuilder Functions Are Acceptable

Use for small, simple sections (a few views, no expensive computation) that don't affect performance. `@ViewBuilder` functions work particularly well for static content that doesn't depend on any `@State` or `@Binding`, since SwiftUI won't need to diff them independently. Extract to a separate `struct` when the section is complex, depends on state, or needs to be skipped during re-evaluation.

## When to Extract Subviews

Extract complex views into separate subviews when:
- The view has multiple logical sections or responsibilities
- The view contains reusable components
- The view body becomes difficult to read or understand
- You need to isolate state changes for performance
- The view is becoming large (keep views small for better performance)

## Container View Pattern

### Avoid Closure-Based Content

Closures can't be compared, causing unnecessary re-renders:

```swift
// BAD - closure prevents SwiftUI from skipping updates
struct MyContainer<Content: View>: View {
    let content: () -> Content

    var body: some View {
        VStack {
            Text("Header")
            content()  // Always called, can't compare closures
        }
    }
}

// Usage forces re-render on every parent update
MyContainer {
    ExpensiveView()
}
```

### Use @ViewBuilder Property Instead

```swift
// GOOD - view can be compared
struct MyContainer<Content: View>: View {
    @ViewBuilder let content: Content

    var body: some View {
        VStack {
            Text("Header")
            content  // SwiftUI can compare and skip if unchanged
        }
    }
}

// Usage - SwiftUI can diff ExpensiveView
MyContainer {
    ExpensiveView()
}
```

## ZStack vs overlay/background

Use `ZStack` to **compose multiple peer views** that should be layered together and jointly define layout.

Prefer `overlay` / `background` when you’re **decorating a primary view**.  
Not primarily because they don’t affect layout size, but because they **express intent and improve readability**: the view being modified remains the clear layout anchor.

A key difference is **size proposal behavior**:
- In `overlay` / `background`, the child view implicitly adopts the size proposed to the parent when it doesn’t define its own size, making decorative attachments feel natural and predictable.
- In `ZStack`, each child participates independently in layout, and no implicit size inheritance exists. This makes it better suited for peer composition, but less intuitive for simple decoration.

Use `ZStack` (or another container) when the “decoration” **must explicitly participate in layout sizing**—for example, when reserving space, extending tappable/visible bounds, or preventing overlap with neighboring views.

### Examples

```swift
// GOOD - decoration via overlay (layout anchored to button)
Button("Continue") { }
    .overlay(alignment: .trailing) {
        Image(systemName: "lock.fill").padding(.trailing, 8)
    }

// BAD - ZStack when overlay suffices (layout no longer anchored to button)
ZStack(alignment: .trailing) {
    Button("Continue") { }
    Image(systemName: "lock.fill").padding(.trailing, 8)
}

// GOOD - background shape takes parent size
HStack(spacing: 12) { Text("Inbox"); Text("Next") }
    .background { Capsule().strokeBorder(.blue, lineWidth: 2) }
```

## Compositing Group Before Clipping

**Always add `.compositingGroup()` before `.clipShape()` when clipping layered views (`.overlay` or `.background`).** Without it, each layer is antialiased separately and then composited. Where antialiased edges overlap — typically at rounded corners — you get visible color fringes (semi-transparent pixels of different colors blending together).

```swift
let shape = RoundedRectangle(cornerRadius: 16)

// BAD - each layer antialiased separately, producing color fringes at corners
Color.red
    .overlay(.white, in: shape)
    .clipShape(shape)
    .frame(width: 200, height: 150)

// GOOD - layers composited first, antialiasing applied once during clipping
Color.red
    .overlay(.white, in: .rect)
    .compositingGroup()
    .clipShape(shape)
    .frame(width: 200, height: 150)
```

`.compositingGroup()` forces all child layers to be rendered into a single offscreen buffer before the clip is applied. This means antialiasing only happens once — on the final composited result — eliminating the fringe artifacts.

## Reusable Styling with ViewModifier

Extract repeated modifier combinations into a `ViewModifier` struct. Expose via a `View` extension for autocompletion:

```swift
private struct CardStyle: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color(.secondarySystemBackground))
            .clipShape(.rect(cornerRadius: 12))
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardStyle())
    }
}
```

### Custom ButtonStyle

Use the `ButtonStyle` protocol for reusable button designs. Use `PrimitiveButtonStyle` only when you need custom interaction handling (e.g., simultaneous gestures):

```swift
struct PrimaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .bold()
            .foregroundStyle(.white)
            .padding(.horizontal, 16)
            .padding(.vertical, 8)
            .background(Color.accentColor)
            .clipShape(Capsule())
            .scaleEffect(configuration.isPressed ? 0.95 : 1)
            .animation(.smooth, value: configuration.isPressed)
    }
}
```

### Discoverability with Static Member Lookup

Make custom styles and modifiers discoverable via leading-dot syntax:

```swift
extension ButtonStyle where Self == PrimaryButtonStyle {
    static var primary: PrimaryButtonStyle { .init() }
}

// Usage: .buttonStyle(.primary)
```

This pattern works for any SwiftUI style protocol (`ButtonStyle`, `ListStyle`, `ToggleStyle`, etc.).

## Skeleton Loading with Redacted Views

Use `.redacted(reason: .placeholder)` to show skeleton views while data loads. Use `.unredacted()` to opt out specific views:

```swift
VStack(alignment: .leading) {
    Text(article?.title ?? String(repeating: "X", count: 20))
        .font(.headline)
    Text(article?.author ?? String(repeating: "X", count: 12))
        .font(.subheadline)
    Text("SwiftLee")
        .font(.caption)
        .unredacted()
}
.redacted(reason: article == nil ? .placeholder : [])
```

Apply `.redacted` on a container to redact all children at once.

## UIViewRepresentable Essentials

When bridging UIKit views into SwiftUI:

- `makeUIView(context:)` is called **once** to create the UIKit view
- `updateUIView(_:context:)` is called on **every SwiftUI redraw** to sync state
- The representable struct itself is **recreated on every redraw** -- avoid heavy work in its init
- Use a `Coordinator` for delegate callbacks and two-way communication

```swift
struct MapView: UIViewRepresentable {
    let coordinate: CLLocationCoordinate2D

    func makeUIView(context: Context) -> MKMapView {
        let map = MKMapView()
        map.delegate = context.coordinator
        return map
    }

    func updateUIView(_ map: MKMapView, context: Context) {
        map.setCenter(coordinate, animated: true)
    }

    func makeCoordinator() -> Coordinator { Coordinator() }

    class Coordinator: NSObject, MKMapViewDelegate { }
}
```

## Summary Checklist

- [ ] Prefer modifiers over conditional views for state changes
- [ ] Avoid `if`-based conditional modifier extensions (they break view identity)
- [ ] Complex views extracted to separate subviews
- [ ] Views kept small for better performance
- [ ] `@ViewBuilder` functions only for simple sections
- [ ] Container views use `@ViewBuilder let content: Content`
- [ ] Extract views when they have multiple responsibilities or become hard to read
- [ ] Reusable styling extracted into `ViewModifier` or `ButtonStyle`
- [ ] Custom styles exposed via static member lookup for discoverability
- [ ] Use `.redacted(reason: .placeholder)` for skeleton loading states
- [ ] `.compositingGroup()` before `.clipShape()` on layered views (overlay/background) to avoid antialiasing fringes
- [ ] UIViewRepresentable: heavy work in make/update, not in struct init
```

