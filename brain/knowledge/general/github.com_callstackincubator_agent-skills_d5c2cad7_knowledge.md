---
id: github.com-callstackincubator-agent-skills-d5c2cad
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:36.311227
---

# KNOWLEDGE EXTRACT: github.com_callstackincubator_agent-skills_d5c2cad7
> **Extracted on:** 2026-04-01 15:51:04
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524800/github.com_callstackincubator_agent-skills_d5c2cad7

---

## File: `.gitignore`
```
# Dependencies
node_modules/

# Build outputs
dist/
build/
*.tgz

# IDE
.idea/
*.swp
*.swo
.vscode/
!.vscode/settings.json
!.vscode/extensions.json

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment
.env
.env.local
.env.*.local

# Testing
coverage/

# Temporary files
*.tmp
*.temp
.cache/
```

## File: `AGENTS.md`
```markdown
# Agent Skills

Markdown-only repo with agent skills for React Native and GitHub workflows. No build step.

## Adding New Skills

Follow [agentskills.io spec](https://agentskills.io/specification) and [Claude Code best practices](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills/best-practices).

### Quick Checklist

1. Create `skills/<skill-name>/SKILL.md`
2. Directory name must match `name` field exactly
3. Required frontmatter:
   ```yaml
   ---
   name: skill-name          # lowercase, hyphens only, 1-64 chars
   description: Third person description of what it does. Use when [trigger conditions].
   ---
   ```
4. Optional frontmatter: `license`, `metadata` (author, tags), `compatibility`
5. Keep body under 500 lines
6. Use markdown links: `[file.md](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/guide/supply_chain/vex/file.md)` not bare filenames
7. Run `/validate-skills` to verify

### What Makes a Good Skill

- **Concise**: Only add context Claude doesn't already have
- **Third person description**: "Processes X" not "I help with X"
- **What + When**: Description says what it does AND when to use it
- **One-level deep**: Reference files link from SKILL.md, not from other references
- **No redundancy**: Don't repeat description content in body

## Repo Structure

```
skills/
├── react-native-best-practices/
│   ├── SKILL.md                    # Main entry point with quick reference + problem→skill mapping
│   └── references/
│       ├── images/                 # Visual references (profiler screenshots, diagrams)
│       ├── js-*.md                 # JavaScript/React skills
│       ├── native-*.md             # iOS/Android native skills
│       └── bundle-*.md             # Bundling & app size skills
│
└── github/
    ├── SKILL.md                    # Main entry point with workflow patterns
    └── references/
```

All reference files are flat in `references/` — no subfolders. Prefix groups related skills.

## When Editing

- Follow format of existing reference files
- Keep "Quick" sections ≤10 lines
- Update `SKILL.md` tables when adding/removing references
- Maintain bidirectional "Related Skills" links

## Details

- [Skill file conventions](./brain/knowledge/docs_legacy/skill-conventions.md)
- [AI assistant integration guide](./brain/knowledge/docs_legacy/ai-assistant-integration.md)
```

## File: `CLAUDE.md`
```markdown
AGENTS.md
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Callstack Incubator

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
# Agent Skills

A collection of agent-optimized skills for AI coding assistants. The repo ships raw Agent Skills for assistants that can read `skills/` directly, plus marketplace metadata for both Claude Code and Codex plugin workflows.

## Available Skills

| Skill                                                                | Description                                             |
| -------------------------------------------------------------------- | ------------------------------------------------------- |
| [react-native-best-practices](./skills/react-native-best-practices/) | React Native optimization best practices from Callstack |
| [github](./skills/github/)                                           | GitHub workflow patterns for PRs, code review, branching |
| [github-actions](./skills/github-actions/)                           | GitHub Actions workflow patterns for React Native simulator/emulator build artifacts |
| [upgrading-react-native](./skills/upgrading-react-native/)           | React Native upgrade workflow: templates, dependencies, and common pitfalls |
| [react-native-brownfield-migration](./skills/react-native-brownfield-migration/) | Incremental migration strategy to adopt React Native or Expo in native apps using @callstack/react-native-brownfield, with setup, packaging, and phased integration steps |

## React Native Best Practices

Performance optimization skills based on [**The Ultimate Guide to React Native Optimization**](https://www.callstack.com/ebooks/the-ultimate-guide-to-react-native-optimization) by [Callstack](https://www.callstack.com/).

Covers:

- **JavaScript/React**: Profiling, FPS, re-renders, lists, state management, animations
- **Native**: iOS/Android profiling, TTI, memory management, Turbo Modules
- **Bundling**: Bundle analysis, tree shaking, R8, app size optimization

### Quick Start

#### Claude Code

Use the Claude Code marketplace metadata in `.claude-plugin/marketplace.json`.

**1. Add the marketplace:**

```bash
/plugin marketplace add callstackincubator/agent-skills
```

**2. Install the skill you want:**

```bash
/plugin install react-native-best-practices@callstack-agent-skills
```

Other available installs:

```bash
/plugin install github@callstack-agent-skills
/plugin install github-actions@callstack-agent-skills
/plugin install upgrading-react-native@callstack-agent-skills
/plugin install react-native-brownfield-migration@callstack-agent-skills
```

Or use the interactive menu:

```bash
/plugin menu
```

**For local development:**

```bash
claude --plugin-dir ./path/to/agent-skills
```

Once installed, Claude will automatically load the relevant skill based on the task.

#### OpenAI Codex

This repo supports Codex in two different ways.

**Option 1: Install the bundled Codex plugins**

```bash
npx codex-plugin add callstackincubator/agent-skills
```

This reads `.agents/plugins/marketplace.json`, installs the bundled plugins into `.codex/plugins/`, and makes them available after restarting Codex.

**Option 2: Install standalone skills**

All major AI coding assistants support the Agent Skills standard.

**Install via skill-installer:**

```
$skill-installer install react-native-best-practices from callstackincubator/agent-skills
```

**Or clone manually:**

```bash
# Project-level
git clone https://github.com/callstackincubator/agent-skills.git
cp -r agent-skills/skills/* .codex/skills/

# User-level
cp -r agent-skills/skills/* ~/.codex/skills/
```

Restart Codex to recognize newly installed skills.

**Usage:** Type `$` to mention a skill or use `/skills` command.

These skills include `agents/openai.yaml` metadata for Codex Skills UI compatibility.

#### Other AI Assistants

##### Cursor

**Option 1: Install from GitHub (Recommended)**

1. Open Cursor Settings (`Cmd+Shift+J` / `Ctrl+Shift+J`)
2. Navigate to **Rules → Add Rule → Remote Rule (GitHub)**
3. Enter: `https://github.com/callstackincubator/agent-skills.git`

**Option 2: Local Installation**

```bash
# Project-level
git clone https://github.com/callstackincubator/agent-skills.git .cursor/skills/agent-skills

# User-level (available in all projects)
git clone https://github.com/callstackincubator/agent-skills.git ~/.cursor/skills/agent-skills
```

**Usage:** Type `/` in Agent chat to search and select skills by name.

##### Gemini CLI

**Install from repository:**

```bash
gemini skills install https://github.com/callstackincubator/agent-skills.git
```

**Or install to workspace:**

```bash
gemini skills install https://github.com/callstackincubator/agent-skills.git --scope workspace
```

**Management commands:**
- `/skills list` - view all discovered skills
- `/skills enable <name>` / `/skills disable <name>` - toggle availability
- `/skills reload` - refresh skill inventory

##### OpenCode

Clone to any supported skills directory:

```bash
# Project-level
git clone https://github.com/callstackincubator/agent-skills.git
cp -r agent-skills/skills/* .opencode/skill/

# User-level
cp -r agent-skills/skills/* ~/.config/opencode/skill/
```

OpenCode also discovers Claude-compatible paths (`.claude/skills/`, `~/.claude/skills/`).

**Permission control** in `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "*": "allow"
    }
  }
}
```

##### Other Assistants

For assistants without native skills support, point them to the skill file:

```
Read skills/react-native-best-practices/SKILL.md for React Native performance guidelines
```

Or reference specific topics:

```
Look up js-profile-react.md for React DevTools profiling instructions
```

### Code Examples

The [callstack/optimization-best-practices](https://github.com/callstack/optimization-best-practices) repository contains runnable code examples for:

- React Compiler setup
- Dedicated React Native SDKs vs web polyfills
- R8 code shrinking on Android

## Other AI Assistants

See [AI Assistant Integration Guide](./brain/knowledge/docs_legacy/ai-assistant-integration.md) for detailed setup instructions with Cursor, GitHub Copilot, Claude API, ChatGPT, and other AI coding assistants.

## Structure

### Repo Structure

```
agent-skills/
├── .claude-plugin/
│   └── marketplace.json     # Claude Code marketplace definition
├── .agents/
│   └── plugins/
│       └── marketplace.json # Codex marketplace definition for bundled plugins
├── plugins/
│   ├── building-react-native-apps/
│   └── testing-react-native-apps/
└── skills/
    ├── react-native-best-practices/
    │   ├── SKILL.md              # Main skill file with quick reference
    │   └── references/           # Detailed skill files
    │       ├── images/           # Visual references for profilers, diagrams
    │       ├── js-*.md           # JavaScript/React skills
    │       ├── native-*.md       # Native iOS/Android skills
    │       └── bundle-*.md       # Bundling & app size skills
    │
    ├── github/
    │   ├── SKILL.md              # Main skill file with PR workflow patterns
    │   └── references/           # Detailed GitHub workflow files
    │
    ├── github-actions/
    │   ├── SKILL.md              # Main skill file for GitHub Actions build artifacts
    │   ├── agents/openai.yaml    # Codex Skills UI metadata
    │   └── references/           # iOS/Android action templates and download flows
    │
    ├── upgrading-react-native/
    │   ├── SKILL.md              # Main skill file with RN upgrade workflow routing
    │   └── references/           # Detailed upgrade flow files
    │
    └── react-native-brownfield-migration/
        ├── SKILL.md              # Main skill file for Expo/bare path routing
        ├── agents/openai.yaml    # Codex Skills UI metadata
        └── references/           # Brownfield packaging and integration flow files
```

Use `.claude-plugin/marketplace.json` for Claude Code plugin installs and `.agents/plugins/marketplace.json` for Codex plugin installs.

The standalone `skills/` directory contains repo-local skills. The `plugins/` directory contains installable Codex plugin bundles.

## Contributing

Contributions welcome! Skills should be:

- **Actionable**: Step-by-step instructions, not theory
- **Searchable**: Clear headings and keywords
- **Complete**: Include code examples and common pitfalls

When adding or editing skills, follow the [agentskills.io specification](https://agentskills.io/specification) and [Claude Code best practices](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills/best-practices). The maintainer checklist lives in [AGENTS.md](../../../.claude/skills/supabase-postgres-best-practices/AGENTS.md), with supporting details in [brain/knowledge/docs_legacy/skill-conventions.md](./brain/knowledge/docs_legacy/skill-conventions.md).

## Roadmap / Work in Progress

This is just the start! The following features are planned or in progress.

### Visual Feedback Integration (Planned)

Several skills involve interpreting visual profiler output (flame graphs, treemaps, memory snapshots). AI agents cannot yet process these autonomously.

**Affected skills:**

- `js-profile-react.md` - React DevTools flame graphs
- `js-measure-fps.md` - FPS graphs and performance overlays
- `native-profiling.md` - Xcode Instruments / Android Studio Profiler
- `native-measure-tti.md` - TTI timeline visualization
- `native-view-flattening.md` - View hierarchy inspection
- `bundle-analyze-js.md` - Bundle treemap visualization
- `bundle-analyze-app.md` - App size breakdown (Emerge Tools, Ruler)

**Planned solution:** MCP (Model Context Protocol) integration for screenshot capture and visual analysis. Contributions welcome!

### Complementary Skills

For complete coverage, consider pairing with:

- [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/tree/react-best-practices/skills/react-best-practices) - React/Next.js web optimization (40+ rules)

### Future Work

- [ ] MCP integration for visual profiler feedback
- [ ] Additional skills for debugging, testing, and CI/CD
- [ ] More code examples and interactive tutorials

---

## Made with ❤️ at Callstack

React Native performance skills based on The Ultimate Guide to React Native Optimization.

[Callstack](https://www.callstack.com/) is a group of React and React Native experts. Contact us at [hello@callstack.com](mailto:hello@callstack.com) if you need help with performance optimization or just want to say hi!

Like what we do? ⚛️ [Join the Callstack team](https://www.callstack.com/careers) and work on amazing React Native projects!
```

## File: `brain/knowledge/docs_legacy/ai-assistant-integration.md`
```markdown
# AI Assistant Integration Guide

How to use agent skills with various AI coding assistants beyond the primary installation methods in the README.

## Cursor

### Method 1: Rules for AI (Recommended)

Add to your project's `.cursor/rules`:

```
When working on React Native code, reference the skills in skills/react-native-best-practices/SKILL.md for performance optimization guidelines.

For specific issues:
- FPS/jank: Read js-measure-fps.md and js-profile-react.md
- Memory leaks: Read js-memory-leaks.md or native-memory-leaks.md
- Bundle size: Read bundle-analyze-js.md and bundle-barrel-exports.md
- Slow startup: Read native-measure-tti.md
```

### Method 2: Direct Reference

In chat, ask Cursor to read the skill file:

```
Read skills/react-native-best-practices/SKILL.md and help me optimize my FlatList performance
```

### Method 3: @ Mention

Use `@file` to include skill context:

```
@skills/react-native-best-practices/references/js-lists-flatlist-flashlist.md

How can I apply FlashList to my current implementation?
```

## GitHub Copilot

### Copilot Chat

Reference skills directly in chat:

```
#file:skills/react-native-best-practices/SKILL.md

How do I profile React Native performance?
```

### Workspace Instructions

Add to `.github/copilot-instructions.md`:

```markdown
## React Native Performance

When reviewing or writing React Native code, apply the optimization guidelines from:
- skills/react-native-best-practices/SKILL.md (main reference)
- skills/react-native-best-practices/references/ (detailed skills)

Key patterns:
- Use FlashList over FlatList for large lists
- Avoid barrel exports
- Profile before optimizing
```

## Claude (API / Claude.ai Projects)

### Project Knowledge

Upload the `skills/react-native-best-practices/` directory as project knowledge.

### System Prompt

```
You have access to React Native performance optimization skills based on Callstack's Ultimate Guide. The skills are organized as:

- SKILL.md: Quick reference and problem→skill mapping
- references/js-*.md: JavaScript/React optimizations
- references/native-*.md: iOS/Android native optimizations
- references/bundle-*.md: Bundle size optimizations

When the user asks about React Native performance, reference these skills for actionable guidance.
```

## ChatGPT / Custom GPTs

### Custom Instructions

```
When helping with React Native development, I follow performance best practices from Callstack's Ultimate Guide:

JavaScript:
- Profile with React DevTools before optimizing
- Use FlashList for large lists
- Use React Compiler for automatic memoization
- Prefer atomic state (Jotai/Zustand)

Native:
- Measure TTI with react-native-performance
- Use background threads for heavy work
- Prefer async Turbo Module methods

Bundling:
- Avoid barrel exports
- Enable R8 on Android
- Analyze bundle with source-map-explorer
```

## OpenAI Codex / API

### System Message

Include the SKILL.md content in your system message:

```python
system_message = """
You are a React Native performance expert. Apply these guidelines:

{Read and include contents of SKILL.md}

When the user asks about performance, provide specific, actionable advice 
based on these skills. Include code examples.
"""
```

## Windsurf / Codeium

### Rules

Add to project rules:

```yaml
rules:
  - name: React Native Performance
    description: Apply optimization best practices
    files:
      - skills/react-native-best-practices/**/*.md
    context: |
      When working on React Native code, reference performance skills for:
      - FPS optimization
      - Memory management
      - Bundle size reduction
      - TTI improvement
```

## General Tips

### 1. Start with the Main Skill File

Always point assistants to `SKILL.md` first—it contains:
- Quick reference commands
- Problem → skill mapping
- Priority-ordered guidelines

### 2. Use Specific References for Deep Dives

For detailed implementation, reference specific files:

```
Read references/js-profile-react.md for step-by-step React DevTools profiling
```

### 3. Include Images for Vision-Capable Models

The `references/images/` directory contains profiler screenshots and diagrams. Vision-capable models (GPT-4V, Claude 3, Gemini) can interpret these for better context.

### 4. Combine with Project Context

Best results come from combining skills with your actual code:

```
@MyListComponent.tsx
@skills/react-native-best-practices/references/js-lists-flatlist-flashlist.md

Migrate this component to use FlashList
```

### 5. Pair with Complementary Skills

For teams using both React Native and React web, consider combining with:

- [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/tree/react-best-practices/skills/react-best-practices) - 40+ React/Next.js optimization rules

Example setup in `.cursor/rules`:

```
For React Native: reference skills/react-native-best-practices/SKILL.md
For React/Next.js web: reference skills/react-best-practices/SKILL.md
```

Both skill sets follow the agentskills.io specification and can be used together.
```

## File: `brain/knowledge/docs_legacy/skill-conventions.md`
```markdown
# Skill File Conventions

Detailed guidelines for writing and maintaining agent skills.

## File Naming

| Prefix | Category | Example |
|--------|----------|---------|
| `js-` | JavaScript/React | `js-profile-react.md` |
| `native-` | iOS/Android native | `native-turbo-modules.md` |
| `bundle-` | Bundling & app size | `bundle-barrel-exports.md` |

Use lowercase, hyphen-separated names that describe the action or topic.

## YAML Frontmatter

Required fields:

```yaml
---
title: Human-readable title
impact: CRITICAL | HIGH | MEDIUM
tags: comma, separated, searchable, keywords
---
```

## Section Order

1. **Quick Pattern / Quick Command / Quick Config / Quick Reference** — Choose one based on skill type
2. **When to Use** — Conditions that trigger this skill
3. **Prerequisites** — Required tools, versions, setup
4. **Step-by-Step Instructions** — Numbered, actionable steps
5. **Code Examples** — Before/after patterns
6. **Common Pitfalls** — What to avoid
7. **Related Skills** — Links to complementary skills

## Quick Section Types

| Type | Use When | Example |
|------|----------|---------|
| Quick Pattern | Code transformation | Incorrect → Correct code |
| Quick Command | Shell/tool invocation | `npx source-map-explorer` |
| Quick Config | Configuration change | metro.config.js snippet |
| Quick Reference | Conceptual overview | Summary table |

## Writing Style

- **Imperative voice**: "Run this command" not "You should run this command"
- **Scannable**: Bullet points over paragraphs
- **Specific**: Include version numbers, exact commands
- **Testable**: Every instruction should be verifiable

## Images

Store in `references/images/` with descriptive names:

```
devtools-flamegraph.png
bundle-treemap-source-map-explorer.png
```

Reference with relative paths:

```markdown
![React DevTools Flamegraph](images/devtools-flamegraph.png)
```

Add a note for AI limitations:

```markdown
> **Note**: This skill involves interpreting visual profiler output. 
> AI agents cannot yet process screenshots autonomously.
```

## Linking

Use relative paths for internal links:

```markdown
See [bundle analysis](./bundle-analyze-js.md) for verification.
```

Maintain bidirectional links in Related Skills sections.

## Impact Ratings

| Rating | Meaning | User Action |
|--------|---------|-------------|
| CRITICAL | Major performance impact | Fix immediately |
| HIGH | Significant improvement | Prioritize |
| MEDIUM | Worthwhile optimization | Address when possible |

## SKILL.md Structure

The main `SKILL.md` file should contain:

1. **YAML frontmatter** with name, description, license, metadata
2. **Overview** — What the skill covers
3. **Skill Format** — Explain the reference file structure
4. **When to Apply** — Trigger conditions
5. **Priority-Ordered Guidelines** — Table with priority, category, impact, prefix
6. **Quick Reference** — Most common commands/patterns
7. **References** — Tables linking to all reference files
8. **Problem → Skill Mapping** — Symptom to solution lookup
```

## File: `packages/codex-plugin/LICENSE`
```
MIT License

Copyright (c) 2026 Callstack. All rights reserved.

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

## File: `packages/codex-plugin/README.md`
```markdown
# codex-plugin

CLI for installing a remote Codex plugin marketplace from a GitHub repository into either project or global configuration.

It clones the remote repository, reads `.agents/plugins/marketplace.json`, copies plugin directories into `.codex/plugins/`, and writes marketplace entries that point to `./.codex/plugins/<plugin-name>`.

Expected repository structure:

- `.agents/plugins/marketplace.json` is the source marketplace file committed to the repo
- `plugins/<plugin-name>` contains each plugin directory

In the repo marketplace, `source.path` values should be relative to the repo root:

- `./plugins/building-react-native-apps`
- `./plugins/testing-react-native-apps`

During installation, the CLI rewrites those entries to the installed layout under `.codex/plugins/`.

It supports one command today:

- `codex-plugin add <org/repo>`

Install targets:

- personal Codex marketplace under `~/.agents/plugins/marketplace.json`
- project Codex marketplace under `<cwd>/.agents/plugins/marketplace.json`

Install layout:

- global: marketplace in `~/.agents/plugins/marketplace.json`, plugins copied into `~/.codex/plugins/`
- project: marketplace in `<cwd>/.agents/plugins/marketplace.json`, plugins copied into `<cwd>/.codex/plugins/`

Run with:

```bash
bun run src/index.ts add callstackincubator/agent-skills
```

Flags:

```bash
bun run src/index.ts add callstackincubator/agent-skills --project
bun run src/index.ts add callstackincubator/agent-skills --global
bun run src/index.ts add callstackincubator/agent-skills --ref feat/codex-plugin
bun run src/index.ts add callstackincubator/agent-skills --project --yes
```

Intended published usage:

```bash
npx codex-plugin add callstackincubator/agent-skills
npx codex-plugin add callstackincubator/agent-skills --ref feat/codex-plugin
```
```

## File: `packages/codex-plugin/bun.lock`
```
{
  "lockfileVersion": 1,
  "workspaces": {
    "": {
      "name": "@callstack/install-marketplace",
      "dependencies": {
        "@clack/prompts": "^0.10.1",
      },
      "devDependencies": {
        "@types/bun": "^1.3.11",
      },
    },
  },
  "packages": {
    "@clack/core": ["@clack/core@0.4.2", "", { "dependencies": { "picocolors": "^1.0.0", "sisteransi": "^1.0.5" } }, "sha512-NYQfcEy8MWIxrT5Fj8nIVchfRFA26yYKJcvBS7WlUIlw2OmQOY9DhGGXMovyI5J5PpxrCPGkgUi207EBrjpBvg=="],

    "@clack/prompts": ["@clack/prompts@0.10.1", "", { "dependencies": { "@clack/core": "0.4.2", "picocolors": "^1.0.0", "sisteransi": "^1.0.5" } }, "sha512-Q0T02vx8ZM9XSv9/Yde0jTmmBQufZhPJfYAg2XrrrxWWaZgq1rr8nU8Hv710BQ1dhoP8rtY7YUdpGej2Qza/cw=="],

    "@types/bun": ["@types/bun@1.3.11", "", { "dependencies": { "bun-types": "1.3.11" } }, "sha512-5vPne5QvtpjGpsGYXiFyycfpDF2ECyPcTSsFBMa0fraoxiQyMJ3SmuQIGhzPg2WJuWxVBoxWJ2kClYTcw/4fAg=="],

    "@types/node": ["@types/node@25.5.0", "", { "dependencies": { "undici-types": "~7.18.0" } }, "sha512-jp2P3tQMSxWugkCUKLRPVUpGaL5MVFwF8RDuSRztfwgN1wmqJeMSbKlnEtQqU8UrhTmzEmZdu2I6v2dpp7XIxw=="],

    "bun-types": ["bun-types@1.3.11", "", { "dependencies": { "@types/node": "*" } }, "sha512-1KGPpoxQWl9f6wcZh57LvrPIInQMn2TQ7jsgxqpRzg+l0QPOFvJVH7HmvHo/AiPgwXy+/Thf6Ov3EdVn1vOabg=="],

    "picocolors": ["picocolors@1.1.1", "", {}, "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA=="],

    "sisteransi": ["sisteransi@1.0.5", "", {}, "sha512-bLGGlR1QxBcynn2d5YmDX4MGjlZvy2MRBDRNHLJ8VI6l6+9FUiyTFNJ0IveOSP0bcXgVDPRcfGqA0pjaqUpfVg=="],

    "undici-types": ["undici-types@7.18.2", "", {}, "sha512-AsuCzffGHJybSaRrmr5eHr81mwJU3kjw6M+uprWvCXiNeN9SOGwQ3Jn8jb8m3Z6izVgknn1R0FTCEAP2QrLY/w=="],
  }
}
```

## File: `packages/codex-plugin/package.json`
```json
{
  "name": "codex-plugin",
  "version": "0.1.3",
  "description": "CLI for installing a remote Codex plugin marketplace into project or global configuration.",
  "type": "module",
  "author": {
    "name": "Mike Grabowski",
    "email": "mike@callstack.com"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/callstackincubator/agent-skills.git",
    "directory": "packages/codex-plugin"
  },
  "homepage": "https://github.com/callstackincubator/agent-skills/tree/main/packages/codex-plugin",
  "bugs": {
    "url": "https://github.com/callstackincubator/agent-skills/issues"
  },
  "bin": {
    "codex-plugin": "dist/index.js"
  },
  "files": [
    "dist",
    "README.md",
    "LICENSE"
  ],
  "dependencies": {
    "@clack/prompts": "^0.10.1"
  },
  "scripts": {
    "build": "mkdir -p dist && bun build src/index.ts --target=node --outfile dist/index.js",
    "prepare": "bun run build",
    "start": "bun run src/index.ts"
  },
  "devDependencies": {
    "@types/bun": "^1.3.11"
  }
}
```

## File: `packages/codex-plugin/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "moduleResolution": "Bundler",
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true,
    "types": [
      "bun"
    ]
  },
  "include": [
    "src/**/*.ts"
  ]
}
```

## File: `packages/codex-plugin/src/index.ts`
```typescript
#!/usr/bin/env node
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { execFileSync } from "node:child_process";
import { cancel, confirm, intro, isCancel, outro, select } from "@clack/prompts";

type InstallScope = "global" | "project";

type MarketplaceManifest = {
  name: string;
  interface: {
    displayName: string;
  };
  plugins: MarketplacePluginEntry[];
};

type MarketplacePluginEntry = {
  name: string;
  source: {
    source: "local";
    path: string;
  };
  policy: {
    installation: "AVAILABLE" | "NOT_AVAILABLE" | "INSTALLED_BY_DEFAULT";
    authentication: "ON_INSTALL" | "ON_USE";
  };
  category: string;
};

type CliOptions = {
  command: "add";
  repoRef: string;
  scope?: InstallScope;
  gitRef?: string;
  yes: boolean;
};

function parseArgs(argv: string[]): CliOptions {
  const [command, ...rest] = argv;
  if (command !== "add") {
    throw new Error(
      "Usage: codex-plugin add <org/repo> [--project|--global] [--ref <branch-or-tag>] [--yes]"
    );
  }

  const input = [...rest];
  let repoRef = "";
  let scope: InstallScope | undefined;
  let gitRef: string | undefined;
  let yes = false;

  while (input.length > 0) {
    const arg = input.shift()!;
    if (arg === "--project") {
      if (scope) {
        throw new Error("Use only one of --project or --global.");
      }
      scope = "project";
      continue;
    }
    if (arg === "--global") {
      if (scope) {
        throw new Error("Use only one of --project or --global.");
      }
      scope = "global";
      continue;
    }
    if (arg === "--yes") {
      yes = true;
      continue;
    }
    if (arg === "--ref") {
      const value = input.shift()?.trim();
      if (!value) {
        throw new Error("Pass a branch, tag, or commit after --ref.");
      }
      gitRef = value;
      continue;
    }
    if (arg.startsWith("--")) {
      throw new Error(`Unknown flag: ${arg}`);
    }
    if (repoRef) {
      throw new Error("Pass exactly one repository argument in the form org/repo.");
    }
    repoRef = arg;
  }

  if (!repoRef || !/^[^/\s]+\/[^/\s]+$/.test(repoRef)) {
    throw new Error(
      "Usage: codex-plugin add <org/repo> [--project|--global] [--ref <branch-or-tag>] [--yes]"
    );
  }

  return { command: "add", repoRef, scope, gitRef, yes };
}

async function chooseScope(providedScope?: InstallScope): Promise<InstallScope> {
  if (providedScope) {
    return providedScope;
  }

  const result = await select<InstallScope>({
    message: "Install marketplace where?",
    options: [
      {
        value: "global",
        label: "Global",
        hint: "~/.agents/plugins/marketplace.json + ~/.codex/plugins"
      },
      {
        value: "project",
        label: "Project",
        hint: "./.agents/plugins/marketplace.json + ./.codex/plugins"
      }
    ]
  });

  if (isCancel(result)) {
    cancel("Installation cancelled.");
    process.exit(1);
  }

  return result;
}

function getRepoUrl(repoRef: string): string {
  return `https://github.com/${repoRef}.git`;
}

function cloneRepo(repoUrl: string, gitRef?: string): string {
  const cloneRoot = join(tmpdir(), `callstack-marketplace-${Date.now()}`);
  const args = ["clone", "--depth", "1"];
  if (gitRef) {
    args.push("--branch", gitRef);
  }
  args.push(repoUrl, cloneRoot);
  execFileSync("git", args, {
    stdio: "inherit"
  });
  return cloneRoot;
}

function getPaths(scope: InstallScope, cwd: string) {
  const home = process.env.HOME;
  if (!home) {
    throw new Error("HOME is not set.");
  }

  if (scope === "global") {
    return {
      marketplacePath: join(home, ".agents", "plugins", "marketplace.json"),
      pluginRepoRoot: join(home, ".codex", "plugins")
    };
  }

  return {
    marketplacePath: join(cwd, ".agents", "plugins", "marketplace.json"),
    pluginRepoRoot: join(cwd, ".codex", "plugins")
  };
}

function loadJsonFile<T>(path: string): T {
  return JSON.parse(readFileSync(path, "utf8")) as T;
}

function resolveSourceRepoRoot(clonedRepoRoot: string): string {
  const clonedManifestPath = join(clonedRepoRoot, ".agents", "plugins", "marketplace.json");
  if (existsSync(clonedManifestPath)) {
    return clonedRepoRoot;
  }

  throw new Error(
    "Remote clone does not contain .agents/plugins/marketplace.json. Push the marketplace files before using this installer."
  );
}

function ensureDir(path: string): void {
  mkdirSync(path, { recursive: true });
}

function copyPluginsPayload(
  clonedRepoRoot: string,
  pluginRoot: string,
  manifest: MarketplaceManifest
): void {
  ensureDir(pluginRoot);

  for (const plugin of manifest.plugins) {
    const sourcePluginDir = join(clonedRepoRoot, "plugins", plugin.name);
    const targetPluginDir = join(pluginRoot, plugin.name);
    rmSync(targetPluginDir, { recursive: true, force: true });
    cpSync(sourcePluginDir, targetPluginDir, { recursive: true, dereference: true });
  }
}

function rewriteEntriesForScope(manifest: MarketplaceManifest): MarketplacePluginEntry[] {
  return manifest.plugins.map((plugin) => {
    return {
      ...plugin,
      source: {
        source: "local",
        path: `./.codex/plugins/${plugin.name}`
      }
    };
  });
}

function mergeMarketplace(
  marketplacePath: string,
  sourceManifest: MarketplaceManifest,
  pluginsToMerge: MarketplacePluginEntry[]
): MarketplaceManifest {
  const existing = existsSync(marketplacePath)
    ? loadJsonFile<MarketplaceManifest>(marketplacePath)
    : {
        name: "user-personal-marketplace",
        interface: {
          displayName: "User Personal Makretplace"
        },
        plugins: []
      };

  const mergedByName = new Map<string, MarketplacePluginEntry>();

  for (const plugin of existing.plugins) {
    mergedByName.set(plugin.name, plugin);
  }
  for (const plugin of pluginsToMerge) {
    mergedByName.set(plugin.name, plugin);
  }

  return {
    name: existing.name ?? sourceManifest.name,
    interface: existing.interface ?? sourceManifest.interface,
    plugins: Array.from(mergedByName.values())
  };
}

function saveMarketplace(path: string, manifest: MarketplaceManifest): void {
  ensureDir(dirname(path));
  writeFileSync(path, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
}

async function confirmInstall(
  repoRef: string,
  scope: InstallScope,
  pluginNames: string[],
  gitRef: string | undefined,
  yes: boolean
): Promise<void> {
  if (yes) {
    return;
  }

  const message = [
    `Install marketplace from ${repoRef}?`,
    `Scope: ${scope}`,
    gitRef ? `Ref: ${gitRef}` : "Ref: default branch",
    "Plugins:",
    ...pluginNames.map((name) => `- ${name}`)
  ].join("\n");

  const approved = await confirm({
    message
  });

  if (isCancel(approved) || !approved) {
    cancel("Installation cancelled.");
    process.exit(1);
  }
}

async function main(): Promise<void> {
  const options = parseArgs(process.argv.slice(2));
  intro("Marketplace");

  const scope = await chooseScope(options.scope);
  const repoUrl = getRepoUrl(options.repoRef);
  const clonedRepoRoot = cloneRepo(repoUrl, options.gitRef);

  try {
    const sourceRepoRoot = resolveSourceRepoRoot(clonedRepoRoot);
    const sourceManifest = loadJsonFile<MarketplaceManifest>(
      join(sourceRepoRoot, ".agents", "plugins", "marketplace.json")
    );
    const pluginNames = sourceManifest.plugins.map((plugin) => plugin.name);
    await confirmInstall(options.repoRef, scope, pluginNames, options.gitRef, options.yes);

    const { marketplacePath, pluginRepoRoot } = getPaths(scope, process.cwd());

    copyPluginsPayload(sourceRepoRoot, pluginRepoRoot, sourceManifest);
    const pluginsToMerge = rewriteEntriesForScope(sourceManifest);

    const mergedMarketplace = mergeMarketplace(
      marketplacePath,
      sourceManifest,
      pluginsToMerge
    );

    saveMarketplace(marketplacePath, mergedMarketplace);

    outro(
      [
        `Installed marketplace to ${marketplacePath}`,
        `Copied plugins to ${pluginRepoRoot}`,
        "Restart Codex to pick up the updated marketplace."
      ].join("\n")
    );
  } finally {
    rmSync(clonedRepoRoot, { recursive: true, force: true });
  }
}

await main();
```

## File: `plugins/building-react-native-apps/README.md`
```markdown
# Building React Native Apps

Build React Native apps with stronger defaults for architecture, performance, and long-term maintenance.

## Example commands

- Review this React Native screen for architecture and performance issues.
- Suggest better implementation patterns for a newly added React Native feature.
- Plan the upgrade path for this app to a newer React Native version.

## Skills included

### Best Practices

- [Vercel React Native Skills](https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills)
  Covers practical React Native implementation work, including app structure, development patterns, and guidance that helps teams make better technical choices while building features.
- [React Native Best Practices](https://skills.sh/callstackincubator/agent-skills/react-native-best-practices)
  Focuses on production-quality React Native performance work such as profiling, startup time, rendering behavior, memory issues, bundle size, and native integration tradeoffs.

### Upgrading

- [Upgrading React Native](https://skills.sh/callstackincubator/agent-skills/upgrading-react-native)
  Guides React Native version upgrades, including template diffs, dependency alignment, iOS and Android project changes, and verification steps after the upgrade.

## Credits

The Vercel skill included in this plugin comes from the [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) repository.
```

## File: `plugins/building-react-native-apps/skills/react-native-best-practices`
```
../../../skills/react-native-best-practices
```

## File: `plugins/building-react-native-apps/skills/upgrading-react-native`
```
../../../skills/upgrading-react-native
```

## File: `plugins/building-react-native-apps/skills/vercel-react-native-skills`
```
../../vendored/.agents/skills/vercel-react-native-skills
```

## File: `plugins/testing-react-native-apps/README.md`
```markdown
# Testing React Native Apps

Testing support for React Native projects that need both structured test-writing guidance and device-level QA workflows.

## Example commands

- Add tests for a newly added navigator public interface.
- Verify accessibility for a core checkout flow and check whether it meets EEA guidelines.
- Verify this PR on a simulator and record the full flow.

## Skills included

- [React Native Testing](https://skills.sh/callstack/react-native-testing-library/react-native-testing)
  Covers writing and maintaining React Native tests with React Native Testing Library, including test structure, assertions, and user-focused testing patterns.
- [agent-device](https://skills.sh/callstackincubator/agent-device/agent-device)
  Provides device automation for iOS and Android, including app launch, navigation, input, screenshots, logs, performance checks, and UI inspection on simulators, emulators, and devices.
- [dogfood](https://skills.sh/callstackincubator/agent-device/dogfood)
  Adds an exploratory QA workflow built on top of device automation, intended for realistic app walkthroughs, bug hunts, smoke checks, and structured manual verification.
```

## File: `plugins/testing-react-native-apps/skills/agent-device`
```
../../vendored/.agents/skills/agent-device
```

## File: `plugins/testing-react-native-apps/skills/dogfood`
```
../../vendored/.agents/skills/dogfood
```

## File: `plugins/testing-react-native-apps/skills/react-native-testing`
```
../../vendored/.agents/skills/react-native-testing
```

## File: `plugins/vendored/README.md`
```markdown
# Vendored Skills

This directory contains external skills vendored into the repository and referenced by the local plugins.

The current setup exists as a workaround for third-party skill composition. It should be removed once plugins can reference external skills directly in a cleaner way.

## Source of truth

- `skills-lock.json` tracks the external skills that should be present here.
- `.agents/skills/` contains the vendored skill directories used by the plugins.

## Updating vendored skills

- Add one skill: `./scripts/add-skill.sh <package> <skill-name>`
- Update all vendored skills: `./scripts/update-skills.sh`
- Restore everything from `skills-lock.json`: `./scripts/restore-skills.sh`

All three scripts keep the vendored copy under `.agents/skills/` and clean up extra agent-specific directories generated by the CLI.
They also sync the updated `skills-lock.json` back into `plugins/vendored/` so the committed lock file remains the source of truth for nightly refreshes and restores.

The repo also runs `.github/workflows/update-vendored-skills.yml` nightly and on manual dispatch to refresh vendored skills and open a PR when changes are detected.
```

## File: `plugins/vendored/skills-lock.json`
```json
{
  "version": 1,
  "skills": {
    "agent-device": {
      "source": "callstackincubator/agent-device",
      "sourceType": "github",
      "computedHash": "4d403e8da02f16d946f5223da4500a2a68459bd1575fd8db4b5c1315e13c8527"
    },
    "dogfood": {
      "source": "callstackincubator/agent-device",
      "sourceType": "github",
      "computedHash": "47e0ea18e07bbe14fc7547b3f79f9f4f1bd895e6d7cbb514055076d78c6ba9d0"
    },
    "react-native-testing": {
      "source": "callstack/react-native-testing-library",
      "sourceType": "github",
      "computedHash": "7ffa231b9f3e4caefca0cc45de10871a0455968f9466c46d1f49ff95527cba28"
    },
    "vercel-react-native-skills": {
      "source": "vercel-labs/agent-skills",
      "sourceType": "github",
      "computedHash": "2e9088a7333666d8c2833b8ff58bd51b955501c42b4c7244f72b4cbf22dafcc4"
    }
  }
}
```

## File: `plugins/vendored/scripts/add-skill.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <package> <skill-name>" >&2
  exit 1
fi

script_dir="$(cd "$(dirname "$0")" && pwd)"
source "$script_dir/lib.sh"

package="$1"
skill_name="$2"

workspace="$(create_vendored_workspace)"

cleanup() {
  rm -rf "$workspace"
}
trap cleanup EXIT

(
  cd "$workspace"
  npx skills add "$package" --skill "$skill_name" -y
)

sync_vendored_workspace "$workspace" "${SKILLS_UPDATE_REHOME:-0}"
```

## File: `plugins/vendored/scripts/cleanup-generated.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

find . -mindepth 1 -maxdepth 1 \
  ! -name ".agents" \
  ! -name "scripts" \
  ! -name "README.md" \
  ! -name "skills-lock.json" \
  -exec /bin/rm -rf {} +
```

## File: `plugins/vendored/scripts/lib.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
vendored_root="$(cd "$script_dir/.." && pwd)"
cleanup_script="$script_dir/cleanup-generated.sh"

create_vendored_workspace() {
  local workspace
  workspace="$(mktemp -d)"

  mkdir -p "$workspace"

  if [[ -f "$vendored_root/skills-lock.json" ]]; then
    cp "$vendored_root/skills-lock.json" "$workspace/skills-lock.json"
  fi

  if [[ -d "$vendored_root/.agents" ]]; then
    cp -R "$vendored_root/.agents" "$workspace/.agents"
  fi

  printf '%s\n' "$workspace"
}

sync_vendored_workspace() {
  local workspace="$1"
  local rehome_global_agents="${2:-0}"

  # Some CLI flows still materialize skills in HOME instead of the project.
  if [[ "$rehome_global_agents" == "1" && -d "$HOME/.agents" && ! -d "$workspace/.agents" ]]; then
    mv "$HOME/.agents" "$workspace/.agents"
  fi

  rm -rf "$vendored_root/.agents"

  if [[ -d "$workspace/.agents" ]]; then
    mv "$workspace/.agents" "$vendored_root/.agents"
  fi

  if [[ -f "$workspace/skills-lock.json" ]]; then
    cp "$workspace/skills-lock.json" "$vendored_root/skills-lock.json"
  fi

  "$cleanup_script"
}
```

## File: `plugins/vendored/scripts/restore-skills.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
source "$script_dir/lib.sh"

workspace="$(create_vendored_workspace)"

cleanup() {
  rm -rf "$workspace"
}
trap cleanup EXIT

(
  cd "$workspace"
  npx skills experimental_install
)

sync_vendored_workspace "$workspace" "${SKILLS_UPDATE_REHOME:-0}"
```

## File: `plugins/vendored/scripts/update-skills.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
source "$script_dir/lib.sh"

workspace="$(create_vendored_workspace)"

cleanup() {
  rm -rf "$workspace"
}
trap cleanup EXIT

(
  cd "$workspace"
  npx -y skills update
)

sync_vendored_workspace "$workspace" "${SKILLS_UPDATE_REHOME:-0}"
```

## File: `skills/github/SKILL.md`
```markdown
---
name: github
description: GitHub patterns using gh CLI for pull requests, stacked PRs, code review, branching strategies, and repository automation. Use when working with GitHub PRs, merging strategies, or repository management tasks.
license: MIT
metadata:
  author: Callstack
  tags: github, gh-cli, pull-request, stacked-pr, squash, rebase
---

# GitHub Patterns

## Tools

Use `gh` CLI for all GitHub operations. Prefer CLI over GitHub MCP servers for lower context usage.

## Quick Commands

```bash
# Create a PR from the current branch
gh pr create --title "feat: add feature" --body "Description"

# Squash-merge a PR
gh pr merge <PR_NUMBER> --squash --title "feat: add feature (#<PR_NUMBER>)"

# View PR status and checks
gh pr status
gh pr checks <PR_NUMBER>
```

## Stacked PR Workflow Summary

When merging a chain of stacked PRs (each targeting the previous branch):

1. **Merge the first PR** into main via squash merge
2. **For each subsequent PR**: rebase onto main, update base to main, then squash merge
3. **On conflicts**: stop and ask the user to resolve manually

```bash
# Rebase next PR's branch onto main, excluding already-merged commits
git rebase --onto origin/main <old-base-branch> <next-branch>
git push --force-with-lease origin <next-branch>
gh pr edit <N> --base main
gh pr merge <N> --squash --title "<PR title> (#N)"
```

See [stacked-pr-workflow.md][stacked-pr-workflow] for full step-by-step details.

## Quick Reference

| File | Description |
| --- | --- |
| [stacked-pr-workflow.md][stacked-pr-workflow] | Merge stacked PRs into main as individual squash commits |

## Problem -> Skill Mapping

| Problem | Start With |
| --- | --- |
| Merge stacked PRs cleanly | [stacked-pr-workflow.md][stacked-pr-workflow] |

[stacked-pr-workflow]: references/stacked-pr-workflow.md
```

## File: `skills/github/agents/openai.yaml`
```yaml
interface:
  display_name: "GitHub Workflows"
  short_description: "GitHub PR and code review workflow patterns"
  default_prompt: "Use $github to apply GitHub PR and review workflows."
```

## File: `skills/github/references/stacked-pr-workflow.md`
```markdown
---
title: Merge PR Chain
tags: pull-request, stacked-pr, merge, squash, cherry-pick, github
---

# Skill: Merge PR Chain

Merge a chain of stacked GitHub PRs into main as individual squash commits. Use when user has multiple PRs where each targets the previous one's branch (e.g., PR #2 → PR #1's branch → main) and wants to squash merge them all to main while preserving separate commits per PR.

## Workflow

### 1. Identify the chain

Fetch PR details to map the chain structure:
```
main
  └── #1 (base: main, branch: feat-a)
        └── #2 (base: feat-a, branch: feat-b)
              └── #3 (base: feat-b, branch: feat-c)
```

### 2. Merge and rebase sequentially

**First PR** (targets main):
```bash
# Squash merge via GitHub CLI
gh pr merge <N> --squash --title "<PR title> (#N)"
git pull origin main
```

**Subsequent PRs** — rebase onto main, update base, then merge:
```bash
# 1. Checkout the branch for the next PR
git checkout <next-branch>

# 2. Rebase onto main, excluding commits from the old base branch
#    This replays only this PR's commits onto main
git rebase --onto origin/main <old-base-branch> <next-branch>

# 3. Force push the rebased branch
git push --force-with-lease origin <next-branch>

# 4. Update the PR's base branch to main via GitHub CLI
gh pr edit <N> --base main

# 5. Squash merge the PR
gh pr merge <N> --squash --title "<PR title> (#N)"

# 6. Update local main
git fetch origin main
git checkout main
git pull origin main
```

Repeat step 2 for each subsequent PR in the chain.

## Key details

- **Always use PR title as commit title** — GitHub may default to branch name or first commit otherwise. Pass `--title` explicitly.
- **Use `--force-with-lease`** — Safer than `--force`, fails if remote has unexpected changes.
- **Update PR base before merging** — After rebasing, change the PR's base branch to `main` so it merges correctly and shows "merged into main" in GitHub UI.

## Handling conflicts

When `git rebase --onto` encounters conflicts:

1. Git will pause and show which files have conflicts
2. **Stop and ask the user** to resolve conflicts manually
3. After user resolves: `git add <resolved-files> && git rebase --continue`
4. If user wants to abort: `git rebase --abort`

**Never auto-resolve conflicts** — always ask the user to review and resolve manually.

## Why this works

`git rebase --onto <new-base> <old-base> <branch>` takes commits that are in `<branch>` but not in `<old-base>` and replays them onto `<new-base>`. This effectively strips the already-merged commits and moves only the PR's unique changes onto main.

## Benefits over cherry-pick

- PRs show as "merged into main" in GitHub UI
- Clean linear history on main
- No duplicate commits or confusing merge states
- Each PR's diff remains reviewable until merged
```

## File: `skills/github-actions/SKILL.md`
```markdown
---
name: github-actions
description: GitHub Actions workflow patterns for React Native iOS simulator and Android emulator cloud builds with downloadable artifacts. Use when setting up CI build pipelines or downloading GitHub Actions artifacts via gh CLI and GitHub API.
license: MIT
metadata:
  author: Callstack
  tags: github-actions, github, ci, react-native, ios, android, simulator, emulator, artifacts, gh-cli
---

# GitHub Actions Build Artifacts

## Overview

Reusable GitHub Actions patterns to build React Native apps for iOS simulators and Android emulators in the cloud, then publish artifacts retrievable via `gh` CLI or GitHub API.

## When to Apply

Use this skill when:
- Creating CI workflows that build React Native simulator/emulator artifacts.
- Uploading iOS simulator and Android emulator installables from PRs or manual dispatch runs.
- Replacing local-only mobile builds with downloadable CI artifacts.
- Needing stable artifact IDs/names for scripted retrieval with `gh` or REST API.

## Quick Reference

1. Add composite actions from [gha-ios-composite-action.md][gha-ios-composite-action] and [gha-android-composite-action.md][gha-android-composite-action].
2. Wire them into `.github/workflows/mobile-build.yml` from [gha-workflow-and-downloads.md][gha-workflow-and-downloads].
3. Upload with `actions/upload-artifact@v4` and capture `artifact-id` output.
4. Download with `gh run download` or `GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}`.

## References

| File | Description |
|------|-------------|
| [gha-ios-composite-action.md][gha-ios-composite-action] | Composite `action.yml` for iOS simulator `.app.tar.gz` builds and artifact upload |
| [gha-android-composite-action.md][gha-android-composite-action] | Composite `action.yml` for Android emulator `.apk` builds and artifact upload |
| [gha-workflow-and-downloads.md][gha-workflow-and-downloads] | End-to-end workflow wiring plus `gh` and REST download commands |

## Problem -> Skill Mapping

| Problem | Start With |
|---------|------------|
| Need CI iOS simulator `.app.tar.gz` artifact | [gha-ios-composite-action.md][gha-ios-composite-action] |
| Need CI Android emulator `.apk` artifact | [gha-android-composite-action.md][gha-android-composite-action] |
| Need one workflow to trigger both platform jobs | [gha-workflow-and-downloads.md][gha-workflow-and-downloads] |
| Need scripted artifact download | [gha-workflow-and-downloads.md][gha-workflow-and-downloads] |

## Source Inspiration

- [callstackincubator/ios/action.yml](https://github.com/callstackincubator/ios/blob/main/action.yml)
- [callstackincubator/android/action.yml](https://github.com/callstackincubator/android/blob/main/action.yml)

[gha-ios-composite-action]: references/gha-ios-composite-action.md
[gha-android-composite-action]: references/gha-android-composite-action.md
[gha-workflow-and-downloads]: references/gha-workflow-and-downloads.md
```

## File: `skills/github-actions/agents/openai.yaml`
```yaml
interface:
  display_name: "GitHub Actions Builds"
  short_description: "React Native GitHub Actions simulator/emulator build artifact patterns"
  default_prompt: "Use $github-actions to set up React Native GitHub Actions builds and download artifacts with gh or API."
```

## File: `skills/github-actions/references/gha-android-composite-action.md`
```markdown
---
title: Android Emulator Composite Action (RN CLI)
impact: HIGH
tags: android, emulator, github-actions, react-native, gradle, artifact
---

# Skill: Android Emulator Composite Action (RN CLI)

Composite action template for building React Native Android emulator APKs in GitHub Actions and uploading the resulting artifact.

## Quick Config

1. Create `.github/actions/github-actions/android-build/action.yml`.
2. Copy the template below.
3. Set `variant` (for emulator flows, use `Debug` by default).
4. Use action outputs (`artifact-name`, `artifact-id`, `artifact-url`) in downstream jobs.

## When to Use

- Need cloud Android emulator build artifacts for testing.
- Need configurable debug-style builds from one action.
- Need reliable artifact retrieval through `gh` and REST API.

## Prerequisites

- Linux runner with JDK 17.
- React Native dependencies installed.
- Android SDK and Gradle wrapper available in the repository.

## Template (`.github/actions/github-actions/android-build/action.yml`)

```yaml
name: React Native Android Emulator Build
description: Build React Native Android emulator APK in GitHub Actions and upload artifact

inputs:
  working-directory:
    description: Project root
    required: false
    default: "."
  variant:
    description: Build variant (Debug by default for emulator flows)
    required: false
    default: Debug
  artifact-prefix:
    description: Prefix for artifact naming
    required: false
    default: rn-android-emulator
  custom-identifier:
    description: Optional stable identifier (PR number, channel, etc.)
    required: false
  artifact-retention-days:
    description: GitHub artifact retention
    required: false
    default: "7"

outputs:
  artifact-name:
    description: Uploaded artifact name
    value: ${{ steps.names.outputs.artifact_name }}
  artifact-id:
    description: Uploaded artifact id
    value: ${{ steps.upload.outputs.artifact-id }}
  artifact-url:
    description: Uploaded artifact URL
    value: ${{ steps.upload.outputs.artifact-url }}

runs:
  using: composite
  steps:
    - name: Resolve Android project settings
      id: resolve
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: |
        set -euo pipefail

        CONFIG_JSON="$(npx react-native config)"
        ANDROID_SOURCE_DIR="$(printf '%s' "$CONFIG_JSON" | node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(j.project?.android?.sourceDir || 'android')")"
        APP_NAME="$(printf '%s' "$CONFIG_JSON" | node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(j.project?.android?.appName || 'app')")"

        IDENTIFIER="${{ inputs.custom-identifier }}"
        if [[ -z "$IDENTIFIER" ]]; then
          if [[ "${{ github.event_name }}" == "pull_request" ]]; then
            IDENTIFIER="pr-${{ github.event.pull_request.number }}"
          else
            IDENTIFIER="${GITHUB_SHA::7}"
          fi
        fi

        echo "android_source_dir=$ANDROID_SOURCE_DIR" >> "$GITHUB_OUTPUT"
        echo "app_name=$APP_NAME" >> "$GITHUB_OUTPUT"
        echo "identifier=$IDENTIFIER" >> "$GITHUB_OUTPUT"

    - name: Build Android APK
      id: build
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: |
        set -euo pipefail

        VARIANT="${{ inputs.variant }}"
        VARIANT_LOWER="$(echo "$VARIANT" | tr '[:upper:]' '[:lower:]')"
        GRADLE_TASK="assemble${VARIANT}"

        (
          cd "${{ steps.resolve.outputs.android_source_dir }}"
          ./gradlew ":${{ steps.resolve.outputs.app_name }}:${GRADLE_TASK}"
        )

        OUTPUT_ROOT="${{ steps.resolve.outputs.android_source_dir }}/${{ steps.resolve.outputs.app_name }}/build/outputs/apk"
        SEARCH_DIR="$OUTPUT_ROOT"
        if [[ -d "$OUTPUT_ROOT/$VARIANT_LOWER" ]]; then
          SEARCH_DIR="$OUTPUT_ROOT/$VARIANT_LOWER"
        fi

        APK_PATH="$(find "$SEARCH_DIR" -type f -name '*.apk' ! -name '*androidTest*' | sort | head -n1 || true)"
        if [[ -z "$APK_PATH" ]]; then
          APK_PATH="$(find "$OUTPUT_ROOT" -type f -name '*.apk' ! -name '*androidTest*' | sort | head -n1 || true)"
        fi

        if [[ -z "$APK_PATH" ]]; then
          echo "No Android APK found"
          exit 1
        fi

        echo "apk_path=$APK_PATH" >> "$GITHUB_OUTPUT"

    - name: Build artifact name
      id: names
      shell: bash
      run: |
        set -euo pipefail

        VARIANT="$(echo "${{ inputs.variant }}" | tr '[:upper:]' '[:lower:]')"
        NAME="${{ inputs.artifact-prefix }}-${VARIANT}-${{ steps.resolve.outputs.identifier }}"
        echo "artifact_name=$NAME" >> "$GITHUB_OUTPUT"

    - name: Upload artifact
      id: upload
      uses: actions/upload-artifact@v4
      with:
        name: ${{ steps.names.outputs.artifact_name }}
        path: ${{ steps.build.outputs.apk_path }}
        if-no-files-found: error
        retention-days: ${{ inputs.artifact-retention-days }}
```

## Common Pitfalls

- Lowercase `variant` values causing wrong Gradle task names.
- Missing JDK setup in caller workflow.
- Hardcoding module name to `app` when `react-native config` reports a custom `appName`.

## Related Skills

- [gha-ios-composite-action.md](gha-ios-composite-action.md)
- [gha-workflow-and-downloads.md](gha-workflow-and-downloads.md)
```

## File: `skills/github-actions/references/gha-ios-composite-action.md`
```markdown
---
title: iOS Simulator Composite Action (RN CLI)
impact: HIGH
tags: ios, simulator, github-actions, react-native, xcodebuild, artifact
---

# Skill: iOS Simulator Composite Action (RN CLI)

Composite action template for building React Native iOS simulator apps in GitHub Actions and uploading `.app.tar.gz` artifacts.

## Quick Config

1. Create `.github/actions/github-actions/ios-build/action.yml`.
2. Copy the template below.
3. Set your app `scheme` and optional `configuration`.
4. Use `actions/upload-artifact@v4` outputs (`artifact-id`, `artifact-url`).
5. Download later by ID (REST) or by run/name (`gh run download`).

## When to Use

- Need cloud iOS simulator build artifacts for QA or PR validation.
- Need deterministic artifact naming and machine-readable IDs.
- Need RN CLI project discovery without Rock (`npx react-native config`).

## Prerequisites

- macOS runner (`macos-latest` recommended).
- Xcode scheme is known and buildable in CI.
- JS dependencies installed before invoking the action.

## Template (`.github/actions/github-actions/ios-build/action.yml`)

```yaml
name: React Native iOS Simulator Build
description: Build React Native iOS simulator app in GitHub Actions and upload artifact

inputs:
  working-directory:
    description: Project root
    required: false
    default: "."
  scheme:
    description: Xcode scheme
    required: true
  configuration:
    description: Xcode configuration
    required: false
    default: Debug
  workspace-path:
    description: Optional path to .xcworkspace
    required: false
  project-path:
    description: Optional path to .xcodeproj
    required: false
  derived-data-path:
    description: DerivedData path relative to working-directory
    required: false
    default: build/ios/DerivedData
  artifact-prefix:
    description: Prefix for artifact naming
    required: false
    default: rn-ios-simulator
  custom-identifier:
    description: Optional stable identifier (PR number, channel, etc.)
    required: false
  artifact-retention-days:
    description: GitHub artifact retention
    required: false
    default: "7"

outputs:
  artifact-name:
    description: Uploaded artifact name
    value: ${{ steps.names.outputs.artifact_name }}
  artifact-id:
    description: Uploaded artifact id
    value: ${{ steps.upload.outputs.artifact-id }}
  artifact-url:
    description: Uploaded artifact URL
    value: ${{ steps.upload.outputs.artifact-url }}

runs:
  using: composite
  steps:
    - name: Validate inputs
      shell: bash
      run: |
        set -euo pipefail

        if [[ -n "${{ inputs.workspace-path }}" && -n "${{ inputs.project-path }}" ]]; then
          echo "Use workspace-path or project-path, not both"
          exit 1
        fi

    - name: Resolve iOS project settings
      id: resolve
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: |
        set -euo pipefail

        CONFIG_JSON="$(npx react-native config)"
        IOS_SOURCE_DIR="$(printf '%s' "$CONFIG_JSON" | node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(j.project?.ios?.sourceDir || 'ios')")"

        WORKSPACE="${{ inputs.workspace-path }}"
        PROJECT="${{ inputs.project-path }}"

        if [[ -z "$WORKSPACE" && -z "$PROJECT" ]]; then
          WORKSPACE="$(find "$IOS_SOURCE_DIR" -maxdepth 2 -name '*.xcworkspace' | head -n1 || true)"
          PROJECT="$(find "$IOS_SOURCE_DIR" -maxdepth 2 -name '*.xcodeproj' | head -n1 || true)"
        fi

        if [[ -n "$WORKSPACE" ]]; then
          CONTAINER_KIND="workspace"
          CONTAINER_PATH="$WORKSPACE"
        elif [[ -n "$PROJECT" ]]; then
          CONTAINER_KIND="project"
          CONTAINER_PATH="$PROJECT"
        else
          echo "Could not find .xcworkspace or .xcodeproj"
          exit 1
        fi

        IDENTIFIER="${{ inputs.custom-identifier }}"
        if [[ -z "$IDENTIFIER" ]]; then
          if [[ "${{ github.event_name }}" == "pull_request" ]]; then
            IDENTIFIER="pr-${{ github.event.pull_request.number }}"
          else
            IDENTIFIER="${GITHUB_SHA::7}"
          fi
        fi

        echo "container_kind=$CONTAINER_KIND" >> "$GITHUB_OUTPUT"
        echo "container_path=$CONTAINER_PATH" >> "$GITHUB_OUTPUT"
        echo "identifier=$IDENTIFIER" >> "$GITHUB_OUTPUT"

    - name: Build iOS simulator
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: |
        set -euo pipefail

        if [[ "${{ steps.resolve.outputs.container_kind }}" == "workspace" ]]; then
          XCODE_CONTAINER=( -workspace "${{ steps.resolve.outputs.container_path }}" )
        else
          XCODE_CONTAINER=( -project "${{ steps.resolve.outputs.container_path }}" )
        fi

        xcodebuild \
          "${XCODE_CONTAINER[@]}" \
          -scheme "${{ inputs.scheme }}" \
          -configuration "${{ inputs.configuration }}" \
          -sdk iphonesimulator \
          -destination "generic/platform=iOS Simulator" \
          -derivedDataPath "${{ inputs.derived-data-path }}" \
          CODE_SIGNING_ALLOWED=NO \
          build

    - name: Package simulator app
      id: simulator
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: |
        set -euo pipefail

        PRODUCTS_DIR="${{ inputs.derived-data-path }}/Build/Products"
        CONFIG_PRODUCTS_DIR="$PRODUCTS_DIR/${{ inputs.configuration }}-iphonesimulator"
        SEARCH_DIR="$PRODUCTS_DIR"
        if [[ -d "$CONFIG_PRODUCTS_DIR" ]]; then
          SEARCH_DIR="$CONFIG_PRODUCTS_DIR"
        fi

        # Prefer the app matching the scheme, then deterministic non-test fallbacks.
        APP_PATH="$(find "$SEARCH_DIR" -type d -name "${{ inputs.scheme }}.app" | sort | head -n1 || true)"
        if [[ -z "$APP_PATH" ]]; then
          APP_PATH="$(find "$SEARCH_DIR" -type d -name '*.app' \
            ! -name '*Tests*.app' \
            ! -name '*UITests*.app' \
            ! -name '*-Runner.app' \
            | sort | head -n1 || true)"
        fi
        if [[ -z "$APP_PATH" ]]; then
          APP_PATH="$(find "$SEARCH_DIR" -type d -name '*.app' | sort | head -n1 || true)"
        fi

        if [[ -z "$APP_PATH" ]]; then
          echo "No .app found in $SEARCH_DIR"
          exit 1
        fi

        mkdir -p build/ios
        APP_DIR="$(dirname "$APP_PATH")"
        APP_NAME="$(basename "$APP_PATH")"
        TARBALL="build/ios/${APP_NAME%.app}.app.tar.gz"
        tar -C "$APP_DIR" -czf "$TARBALL" "$APP_NAME"

        echo "artifact_path=$TARBALL" >> "$GITHUB_OUTPUT"

    - name: Build artifact name
      id: names
      shell: bash
      run: |
        set -euo pipefail

        CONFIG="$(echo "${{ inputs.configuration }}" | tr '[:upper:]' '[:lower:]')"
        NAME="${{ inputs.artifact-prefix }}-${CONFIG}-${{ steps.resolve.outputs.identifier }}"
        echo "artifact_name=$NAME" >> "$GITHUB_OUTPUT"

    - name: Upload artifact
      id: upload
      uses: actions/upload-artifact@v4
      with:
        name: ${{ steps.names.outputs.artifact_name }}
        path: ${{ steps.simulator.outputs.artifact_path }}
        if-no-files-found: error
        retention-days: ${{ inputs.artifact-retention-days }}
```

## Common Pitfalls

- Passing both `workspace-path` and `project-path`.
- Uploading `.app` directly instead of `tar.gz` (permission loss risk).
- Using non-macOS runner for iOS jobs.

## Related Skills

- [gha-android-composite-action.md](gha-android-composite-action.md)
- [gha-workflow-and-downloads.md](gha-workflow-and-downloads.md)
```

## File: `skills/github-actions/references/gha-workflow-and-downloads.md`
```markdown
---
title: Workflow Wiring and Artifact Downloads
impact: CRITICAL
tags: github-actions, workflow, artifacts, gh-cli, rest-api, simulator, emulator
---

# Skill: Workflow Wiring and Artifact Downloads

Use this workflow to run iOS simulator and Android emulator builds in cloud CI and expose artifact metadata for scripted retrieval.

## Minimum Required Inputs

Set these before first run:
- iOS scheme: exact Xcode scheme name (for example `YourApp`).
- Android variant: Gradle variant for emulator artifacts (usually `Debug`).
- Branch strategy: branches for `push` and `pull_request` triggers (default below uses `main`).
- Retention days: artifact retention period passed to upload steps (for example `7`).

## Repo-Compat Checklist (Before First Run)

- Confirm the iOS scheme exists and builds locally.
- Confirm `pod install` works in CI context from iOS source dir.
- Confirm `android/gradlew` is executable (`chmod +x android/gradlew` if needed).
- Confirm `npx react-native config` resolves valid `project.ios.sourceDir` and `project.android.sourceDir`.

## Quick Config

1. Create `.github/workflows/mobile-build.yml`.
2. Call local composite actions from this skill (`github-actions/ios-build`, `github-actions/android-build`).
3. Keep `actions/upload-artifact@v4` output IDs.
4. Retrieve with `gh run download` or `gh api`.

## When to Use

- Need one pipeline for simulator/emulator artifacts.
- Need PR, push, and manual dispatch triggers.
- Need deterministic artifact retrieval in CI/CD or external tooling.

## Workflow Template (`.github/workflows/mobile-build.yml`)

```yaml
name: RN Cloud Build

on:
  # Baseline trigger strategy: validate incoming changes and direct branch updates.
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
    inputs:
      ios_scheme:
        description: iOS scheme name
        required: true
        default: YourApp
        type: string
      ios_configuration:
        description: iOS configuration
        required: true
        default: Debug
        type: string
      android_variant:
        description: Android Gradle variant
        required: true
        default: Debug
        type: string
      artifact_retention_days:
        description: Artifact retention days
        required: true
        default: '7'
        type: string

permissions:
  contents: read
  actions: read

env:
  IOS_SCHEME: YourApp
  IOS_CONFIGURATION: Debug
  ANDROID_VARIANT: Debug
  ARTIFACT_RETENTION_DAYS: '7'

jobs:
  ios:
    name: iOS simulator build
    runs-on: macos-latest
    outputs:
      artifact_name: ${{ steps.build.outputs.artifact-name }}
      artifact_id: ${{ steps.build.outputs.artifact-id }}
      artifact_url: ${{ steps.build.outputs.artifact-url }}
    steps:
      - uses: actions/checkout@v4

      - name: Resolve Node version from package.json engines
        id: node-version
        run: |
          set -euo pipefail
          NODE_SPEC="$(python3 - <<'PY'
import json
from pathlib import Path
pkg = Path('package.json')
if not pkg.exists():
    print('22')
else:
    data = json.loads(pkg.read_text())
    print((data.get('engines', {}).get('node') or '22').strip())
PY
          )"
          echo "value=$NODE_SPEC" >> "$GITHUB_OUTPUT"

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ steps.node-version.outputs.value }}
          cache: npm

      - name: Install JS dependencies
        run: npm ci

      - name: Install CocoaPods dependencies
        run: |
          set -euo pipefail
          IOS_SOURCE_DIR="$(npx react-native config | node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(j.project?.ios?.sourceDir || 'ios')")"
          cd "$IOS_SOURCE_DIR"
          pod install --repo-update

      # Optional: only add ruby/setup-ruby when this repo enforces Ruby tooling
      # (for example via .ruby-version and Bundler workflow).
      # - uses: ruby/setup-ruby@v1
      #   with:
      #     bundler-cache: true

      - name: Resolve iOS inputs
        id: ios-inputs
        run: |
          if [[ "${{ github.event_name }}" == "workflow_dispatch" ]]; then
            echo "scheme=${{ inputs.ios_scheme }}" >> "$GITHUB_OUTPUT"
            echo "config=${{ inputs.ios_configuration }}" >> "$GITHUB_OUTPUT"
            echo "retention=${{ inputs.artifact_retention_days }}" >> "$GITHUB_OUTPUT"
          else
            echo "scheme=${{ env.IOS_SCHEME }}" >> "$GITHUB_OUTPUT"
            echo "config=${{ env.IOS_CONFIGURATION }}" >> "$GITHUB_OUTPUT"
            echo "retention=${{ env.ARTIFACT_RETENTION_DAYS }}" >> "$GITHUB_OUTPUT"
          fi

      - name: Build iOS simulator
        id: build
        uses: ./.github/actions/github-actions/ios-build
        with:
          scheme: ${{ steps.ios-inputs.outputs.scheme }}
          configuration: ${{ steps.ios-inputs.outputs.config }}
          artifact-prefix: rn-ios-simulator
          artifact-retention-days: ${{ steps.ios-inputs.outputs.retention }}

  android:
    name: Android emulator build
    runs-on: ubuntu-latest
    outputs:
      artifact_name: ${{ steps.build.outputs.artifact-name }}
      artifact_id: ${{ steps.build.outputs.artifact-id }}
      artifact_url: ${{ steps.build.outputs.artifact-url }}
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'
          cache: gradle

      - name: Resolve Node version from package.json engines
        id: node-version
        run: |
          set -euo pipefail
          NODE_SPEC="$(python3 - <<'PY'
import json
from pathlib import Path
pkg = Path('package.json')
if not pkg.exists():
    print('22')
else:
    data = json.loads(pkg.read_text())
    print((data.get('engines', {}).get('node') or '22').strip())
PY
          )"
          echo "value=$NODE_SPEC" >> "$GITHUB_OUTPUT"

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ steps.node-version.outputs.value }}
          cache: npm

      - name: Install JS dependencies
        run: npm ci

      - name: Resolve Android inputs
        id: android-inputs
        run: |
          if [[ "${{ github.event_name }}" == "workflow_dispatch" ]]; then
            echo "variant=${{ inputs.android_variant }}" >> "$GITHUB_OUTPUT"
            echo "retention=${{ inputs.artifact_retention_days }}" >> "$GITHUB_OUTPUT"
          else
            echo "variant=${{ env.ANDROID_VARIANT }}" >> "$GITHUB_OUTPUT"
            echo "retention=${{ env.ARTIFACT_RETENTION_DAYS }}" >> "$GITHUB_OUTPUT"
          fi

      - name: Build Android emulator APK
        id: build
        uses: ./.github/actions/github-actions/android-build
        with:
          variant: ${{ steps.android-inputs.outputs.variant }}
          artifact-prefix: rn-android-emulator
          artifact-retention-days: ${{ steps.android-inputs.outputs.retention }}

  summary:
    name: Build summary
    runs-on: ubuntu-latest
    needs: [ios, android]
    steps:
      - name: Publish artifact metadata
        run: |
          {
            echo "## RN Cloud Build Artifacts"
            echo ""
            echo "- iOS simulator (.app.tar.gz): name=${{ needs.ios.outputs.artifact_name }}, id=${{ needs.ios.outputs.artifact_id }}"
            echo "- Android emulator (.apk): name=${{ needs.android.outputs.artifact_name }}, id=${{ needs.android.outputs.artifact_id }}"
            echo ""
            echo "Artifact URLs (auth required):"
            echo "- iOS: ${{ needs.ios.outputs.artifact_url }}"
            echo "- Android: ${{ needs.android.outputs.artifact_url }}"
          } >> "$GITHUB_STEP_SUMMARY"
```

## CocoaPods and Ruby Notes

- Run `pod install` from `ios/` or from `project.ios.sourceDir` resolved via `npx react-native config`.
- Do not assume Bundler or pinned Ruby is always required.
- `ruby/setup-ruby` is optional and should be added only when repo policy enforces Ruby tooling (for example `.ruby-version` and Bundler-managed pods).

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `ruby/setup-ruby` or Bundler fails | Repo does not require Ruby toolchain in CI | Remove Ruby setup and run plain `pod install` |
| `xcodebuild: Scheme ... not found` | Wrong iOS scheme value | Use exact shared scheme from Xcode project/workspace |
| `Task ':app:assembledebug' not found` | Wrong Android variant casing | Use Gradle-style casing (`Debug`, `Release`, `StagingDebug`) |
| `pod install --repo-update` is slow or flaky | CocoaPods spec repo updates | Retry, cache Pods, or drop `--repo-update` when lockfile + mirror are stable |

## Download Artifacts with `gh`

```bash
# 1) Find recent runs for this workflow
gh run list --workflow "RN Cloud Build" --limit 10

# 2) Download by run id + artifact name
gh run download <run-id> -n <artifact-name> -D ./artifacts

# 3) Inspect artifacts for a run (IDs + names)
gh api repos/<owner>/<repo>/actions/runs/<run-id>/artifacts \
  --jq '.artifacts[] | {id, name, size_in_bytes, expired}'
```

## Download Artifacts with Direct REST API

```bash
# List repo artifacts
curl -sS \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<owner>/<repo>/actions/artifacts" | jq '.artifacts[] | {id, name}'

# Download one artifact zip by ID
curl -L \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<owner>/<repo>/actions/artifacts/<artifact-id>/zip" \
  -o artifact.zip
```

## Common Pitfalls

- Forgetting to set `permissions.actions: read` for API-driven artifact listing.
- Assuming artifact URLs are public; they require authenticated access.
- Not pinning artifact names, making `gh run download -n` brittle.

## Related Skills

- [gha-ios-composite-action.md](gha-ios-composite-action.md)
- [gha-android-composite-action.md](gha-android-composite-action.md)
```

## File: `skills/react-native-best-practices/POWER.md`
```markdown
---
name: react-native-best-practices
description: Provides React Native performance optimization guidelines for FPS, TTI, bundle size, memory leaks, re-renders, and animations. Applies to tasks involving Hermes optimization, JS thread blocking, bridge overhead, FlashList, native modules, or debugging jank and frame drops.
license: MIT
author: Callstack
keywords: ["react-native", "expo", "performance", "optimization", "profiling"]
---

# Onboarding

## Step 1: Validate React Native Setup

Before applying performance optimizations, ensure:
- **Expo CLI** or **React Native CLI** is installed
  - Verify with: `npx expo --version` and `npx react-native --version`
- Metro bundler is running (**apply only for** bundle analysis)
- React Native DevTools is available (**apply only for** profiling)
  - Press 'j' in Metro terminal or shake device → "Open DevTools"

## Security Guardrails

- Review shell commands before running them and prefer version-pinned tooling from trusted sources.
- Do not pipe remote install scripts directly into a shell.
- Treat third-party packages as normal supply-chain dependencies that require provenance and version review.
- If using Re.Pack code splitting, only load first-party chunks from trusted HTTPS origins tied to the current release.

# When to Load Reference Files

Load specific reference files from `references/` based on the task:

## JavaScript/React Performance (`js-*`)

- **Debugging slow/janky UI or animations** → `references/js-measure-fps.md`
- **Investigating re-render issues** → `references/js-profile-react.md` → `references/js-react-compiler.md`
- **Optimizing list scrolling** → `references/js-lists-flatlist-flashlist.md`
- **Reducing re-renders with state management** → `references/js-atomic-state.md`
- **Using Concurrent React features** → `references/js-concurrent-react.md`
- **Enabling automatic memoization** → `references/js-react-compiler.md`
- **Optimizing animations** → `references/js-animations-reanimated.md`
- **Fixing TextInput lag** → `references/js-uncontrolled-components.md`
- **Hunting JavaScript memory leaks** → `references/js-memory-leaks.md`

## Native Performance (`native-*`)

- **Measuring startup time (TTI)** → `references/native-measure-tti.md`
- **Building native modules** → `references/native-turbo-modules.md`
- **Understanding native threading** → `references/native-threading-model.md`
- **Profiling native code** → `references/native-profiling.md`
- **Setting up native tooling** → `references/native-platform-setup.md`
- **Debugging view hierarchy** → `references/native-view-flattening.md`
- **Native memory patterns** → `references/native-memory-patterns.md`
- **Hunting native memory leaks** → `references/native-memory-leaks.md`
- **Choosing native SDKs vs polyfills** → `references/native-sdks-over-polyfills.md`
- **Fixing Android 16KB alignment** → `references/native-android-16kb-alignment.md`

## Bundle & App Size (`bundle-*`)

- **Analyzing bundle size** → `references/bundle-analyze-js.md`
- **Analyzing app size** → `references/bundle-analyze-app.md`
- **Fixing barrel imports** → `references/bundle-barrel-exports.md`
- **Enabling tree shaking** → `references/bundle-tree-shaking.md`
- **Android code shrinking** → `references/bundle-r8-android.md`
- **Optimizing Hermes bundle loading** → `references/bundle-hermes-mmap.md`
- **Managing native assets** → `references/bundle-native-assets.md`
- **Evaluating library size** → `references/bundle-library-size.md`
- **Code splitting** → `references/bundle-code-splitting.md`

## Problem → Reference Mapping

Use this quick lookup when debugging specific issues:

| Problem | Start With |
|---------|-----------|
| App feels slow/janky | `references/js-measure-fps.md` → `references/js-profile-react.md` |
| Too many re-renders | `references/js-profile-react.md` → `references/js-react-compiler.md` |
| Slow startup (TTI) | `references/native-measure-tti.md` → `references/bundle-analyze-js.md` |
| Large app size | `references/bundle-analyze-app.md` → `references/bundle-r8-android.md` |
| Memory growing | `references/js-memory-leaks.md` or `references/native-memory-leaks.md` |
| Animation drops frames | `references/js-animations-reanimated.md` |
| List scroll jank | `references/js-lists-flatlist-flashlist.md` |
| TextInput lag | `references/js-uncontrolled-components.md` |
| Native module slow | `references/native-turbo-modules.md` → `references/native-threading-model.md` |
| Native library alignment issue | `references/native-android-16kb-alignment.md` |

## Quick Reference Commands

### FPS & Re-renders
```bash
# Open React Native DevTools
# Press 'j' in Metro, or shake device → "Open DevTools"
```

**Common fixes:**
- Replace ScrollView with FlatList/FlashList for lists
- Use React Compiler for automatic memoization
- Use atomic state (Jotai/Zustand) to reduce re-renders
- Use `useDeferredValue` for expensive computations

### Analyze Bundle Size
```bash
npx react-native bundle \
  --entry-file index.js \
  --bundle-output output.js \
  --platform ios \
  --sourcemap-output output.js.map \
  --dev false --minify true

npx source-map-explorer output.js --no-border-checks
```

**Common fixes:**
- Avoid barrel imports (import directly from source)
- Remove unnecessary Intl polyfills only after checking Hermes API and method coverage
- Enable tree shaking (Expo SDK 52+ or Re.Pack)
- Enable R8 for Android native code shrinking

### Measure TTI
- Use `react-native-performance` for markers
- Only measure cold starts (exclude warm/hot/prewarm)

**Common fixes:**
- Disable JS bundle compression on Android (enables Hermes mmap)
- Use native navigation (react-native-screens)
- Preload commonly-used expensive screens before navigating to them

### Native Performance

**Profile native:**
- iOS: Xcode Instruments → Time Profiler
- Android: Android Studio → CPU Profiler

**Common fixes:**
- Use background threads for heavy native work
- Prefer async over sync Turbo Module methods
- Use C++ for cross-platform performance-critical code

## Priority Guidelines

Apply optimizations in this order:

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | FPS & Re-renders | CRITICAL | `js-*` |
| 2 | Bundle Size | CRITICAL | `bundle-*` |
| 3 | TTI Optimization | HIGH | `native-*`, `bundle-*` |
| 4 | Native Performance | HIGH | `native-*` |
| 5 | Memory Management | MEDIUM-HIGH | `js-*`, `native-*` |
| 6 | Animations | MEDIUM | `js-*` |

## Attribution

Based on "The Ultimate Guide to React Native Optimization" by Callstack.
```

## File: `skills/react-native-best-practices/SKILL.md`
```markdown
---
name: react-native-best-practices
description: Provides React Native performance optimization guidelines for FPS, TTI, bundle size, memory leaks, re-renders, and animations. Applies to tasks involving Hermes optimization, JS thread blocking, bridge overhead, FlashList, native modules, or debugging jank and frame drops.
license: MIT
metadata:
  author: Callstack
  tags: react-native, expo, performance, optimization, profiling
---

# React Native Best Practices

## Overview

Performance optimization guide for React Native applications, covering JavaScript/React, Native (iOS/Android), and bundling optimizations. Based on Callstack's "Ultimate Guide to React Native Optimization".

## Skill Format

Each reference file follows a hybrid format for fast lookup and deep understanding:

- **Quick Pattern**: Incorrect/Correct code snippets for immediate pattern matching
- **Quick Command**: Shell commands for process/measurement skills
- **Quick Config**: Configuration snippets for setup-focused skills
- **Quick Reference**: Summary tables for conceptual skills
- **Deep Dive**: Full context with When to Use, Prerequisites, Step-by-Step, Common Pitfalls

**Impact ratings**: CRITICAL (fix immediately), HIGH (significant improvement), MEDIUM (worthwhile optimization)

## When to Apply

Reference these guidelines when:
- Debugging slow/janky UI or animations
- Investigating memory leaks (JS or native)
- Optimizing app startup time (TTI)
- Reducing bundle or app size
- Writing native modules (Turbo Modules)
- Profiling React Native performance
- Reviewing React Native code for performance

## Security Notes

- Treat shell commands in these references as local developer operations. Review them before running, prefer version-pinned tooling, and avoid piping remote scripts directly to a shell.
- Treat third-party libraries and plugins as dependencies that still require normal supply-chain controls: pin versions, verify provenance, and update through your standard review process.
- Treat Re.Pack code splitting as first-party artifact delivery only. Remote chunks must come from trusted HTTPS origins you control and be pinned to the current app release.

## Priority-Ordered Guidelines

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | FPS & Re-renders | CRITICAL | `js-*` |
| 2 | Bundle Size | CRITICAL | `bundle-*` |
| 3 | TTI Optimization | HIGH | `native-*`, `bundle-*` |
| 4 | Native Performance | HIGH | `native-*` |
| 5 | Memory Management | MEDIUM-HIGH | `js-*`, `native-*` |
| 6 | Animations | MEDIUM | `js-*` |

## Quick Reference

### Optimization Workflow

Follow this cycle for any performance issue: **Measure → Optimize → Re-measure → Validate**

1. **Measure**: Capture baseline metrics (FPS, TTI, bundle size) before changes
2. **Optimize**: Apply the targeted fix from the relevant reference
3. **Re-measure**: Run the same measurement to get updated metrics
4. **Validate**: Confirm improvement (e.g., FPS 45→60, TTI 3.2s→1.8s, bundle 2.1MB→1.6MB)

If metrics did not improve, revert and try the next suggested fix.

### Critical: FPS & Re-renders

**Profile first:**
```bash
# Open React Native DevTools
# Press 'j' in Metro, or shake device → "Open DevTools"
```

**Common fixes:**
- Replace ScrollView with FlatList/FlashList for lists
- Use React Compiler for automatic memoization
- Use atomic state (Jotai/Zustand) to reduce re-renders
- Use `useDeferredValue` for expensive computations

### Critical: Bundle Size

**Analyze bundle:**
```bash
npx react-native bundle \
  --entry-file index.js \
  --bundle-output output.js \
  --platform ios \
  --sourcemap-output output.js.map \
  --dev false --minify true

npx source-map-explorer output.js --no-border-checks
```

**Verify improvement after optimization:**
```bash
# Record baseline size before changes
ls -lh output.js  # e.g., Before: 2.1 MB

# After applying fixes, re-bundle and compare
npx react-native bundle --entry-file index.js --bundle-output output.js \
  --platform ios --dev false --minify true
ls -lh output.js  # e.g., After: 1.6 MB  (24% reduction)
```

**Common fixes:**
- Avoid barrel imports (import directly from source)
- Remove unnecessary Intl polyfills only after checking Hermes API and method coverage
- Enable tree shaking (Expo SDK 52+ or Re.Pack)
- Enable R8 for Android native code shrinking

### High: TTI Optimization

**Measure TTI:**
- Use `react-native-performance` for markers
- Only measure cold starts (exclude warm/hot/prewarm)

**Common fixes:**
- Disable JS bundle compression on Android (enables Hermes mmap)
- Use native navigation (react-native-screens)
- Preload commonly-used expensive screens before navigating to them

### High: Native Performance

**Profile native:**
- iOS: Xcode Instruments → Time Profiler
- Android: Android Studio → CPU Profiler

**Common fixes:**
- Use background threads for heavy native work
- Prefer async over sync Turbo Module methods
- Use C++ for cross-platform performance-critical code

## References

Full documentation with code examples in [references/][references]:

### JavaScript/React (`js-*`)

| File | Impact | Description |
|------|--------|-------------|
| [js-lists-flatlist-flashlist.md][js-lists-flatlist-flashlist] | CRITICAL | Replace ScrollView with virtualized lists |
| [js-profile-react.md][js-profile-react] | MEDIUM | React DevTools profiling |
| [js-measure-fps.md][js-measure-fps] | HIGH | FPS monitoring and measurement |
| [js-memory-leaks.md][js-memory-leaks] | MEDIUM | JS memory leak hunting |
| [js-atomic-state.md][js-atomic-state] | HIGH | Jotai/Zustand patterns |
| [js-concurrent-react.md][js-concurrent-react] | HIGH | useDeferredValue, useTransition |
| [js-react-compiler.md][js-react-compiler] | HIGH | Automatic memoization |
| [js-animations-reanimated.md][js-animations-reanimated] | MEDIUM | Reanimated worklets |
| [js-bottomsheet.md][js-bottomsheet] | HIGH | Bottom sheet optimization |
| [js-uncontrolled-components.md][js-uncontrolled-components] | HIGH | TextInput optimization |

### Native (`native-*`)

| File | Impact | Description |
|------|--------|-------------|
| [native-turbo-modules.md][native-turbo-modules] | HIGH | Building fast native modules |
| [native-sdks-over-polyfills.md][native-sdks-over-polyfills] | HIGH | Native vs JS libraries |
| [native-measure-tti.md][native-measure-tti] | HIGH | TTI measurement setup |
| [native-threading-model.md][native-threading-model] | HIGH | Turbo Module threads |
| [native-profiling.md][native-profiling] | MEDIUM | Xcode/Android Studio profiling |
| [native-platform-setup.md][native-platform-setup] | MEDIUM | iOS/Android tooling guide |
| [native-view-flattening.md][native-view-flattening] | MEDIUM | View hierarchy debugging |
| [native-memory-patterns.md][native-memory-patterns] | MEDIUM | C++/Swift/Kotlin memory |
| [native-memory-leaks.md][native-memory-leaks] | MEDIUM | Native memory leak hunting |
| [native-android-16kb-alignment.md][native-android-16kb-alignment] | CRITICAL | Third-party library alignment for Google Play |

### Bundling (`bundle-*`)

| File | Impact | Description |
|------|--------|-------------|
| [bundle-barrel-exports.md][bundle-barrel-exports] | CRITICAL | Avoid barrel imports |
| [bundle-analyze-js.md][bundle-analyze-js] | CRITICAL | JS bundle visualization |
| [bundle-tree-shaking.md][bundle-tree-shaking] | HIGH | Dead code elimination |
| [bundle-analyze-app.md][bundle-analyze-app] | HIGH | App size analysis |
| [bundle-r8-android.md][bundle-r8-android] | HIGH | Android code shrinking |
| [bundle-hermes-mmap.md][bundle-hermes-mmap] | HIGH | Disable bundle compression |
| [bundle-native-assets.md][bundle-native-assets] | HIGH | Asset catalog setup |
| [bundle-library-size.md][bundle-library-size] | MEDIUM | Evaluate dependencies |
| [bundle-code-splitting.md][bundle-code-splitting] | MEDIUM | Re.Pack code splitting |


## Searching References

```bash
# Find patterns by keyword
grep -l "reanimated" references/
grep -l "flatlist" references/
grep -l "memory" references/
grep -l "profil" references/
grep -l "tti" references/
grep -l "bundle" references/
```

## Problem → Skill Mapping

| Problem | Start With |
|---------|------------|
| App feels slow/janky | [js-measure-fps.md][js-measure-fps] → [js-profile-react.md][js-profile-react] |
| Too many re-renders | [js-profile-react.md][js-profile-react] → [js-react-compiler.md][js-react-compiler] |
| Slow startup (TTI) | [native-measure-tti.md][native-measure-tti] → [bundle-analyze-js.md][bundle-analyze-js] |
| Large app size | [bundle-analyze-app.md][bundle-analyze-app] → [bundle-r8-android.md][bundle-r8-android] |
| Memory growing | [js-memory-leaks.md][js-memory-leaks] or [native-memory-leaks.md][native-memory-leaks] |
| Animation drops frames | [js-animations-reanimated.md][js-animations-reanimated] |
| Bottom sheet jank/re-renders | [js-bottomsheet.md][js-bottomsheet] → [js-animations-reanimated.md][js-animations-reanimated] |
| List scroll jank | [js-lists-flatlist-flashlist.md][js-lists-flatlist-flashlist] |
| TextInput lag | [js-uncontrolled-components.md][js-uncontrolled-components] |
| Native module slow | [native-turbo-modules.md][native-turbo-modules] → [native-threading-model.md][native-threading-model] |
| Native library alignment issue | [native-android-16kb-alignment.md][native-android-16kb-alignment] |

[references]: references/
[js-lists-flatlist-flashlist]: references/js-lists-flatlist-flashlist.md
[js-profile-react]: references/js-profile-react.md
[js-measure-fps]: references/js-measure-fps.md
[js-memory-leaks]: references/js-memory-leaks.md
[js-atomic-state]: references/js-atomic-state.md
[js-concurrent-react]: references/js-concurrent-react.md
[js-react-compiler]: references/js-react-compiler.md
[js-animations-reanimated]: references/js-animations-reanimated.md
[js-bottomsheet]: references/js-bottomsheet.md
[js-uncontrolled-components]: references/js-uncontrolled-components.md
[native-turbo-modules]: references/native-turbo-modules.md
[native-sdks-over-polyfills]: references/native-sdks-over-polyfills.md
[native-measure-tti]: references/native-measure-tti.md
[native-threading-model]: references/native-threading-model.md
[native-profiling]: references/native-profiling.md
[native-platform-setup]: references/native-platform-setup.md
[native-view-flattening]: references/native-view-flattening.md
[native-memory-patterns]: references/native-memory-patterns.md
[native-memory-leaks]: references/native-memory-leaks.md
[native-android-16kb-alignment]: references/native-android-16kb-alignment.md
[bundle-barrel-exports]: references/bundle-barrel-exports.md
[bundle-analyze-js]: references/bundle-analyze-js.md
[bundle-tree-shaking]: references/bundle-tree-shaking.md
[bundle-analyze-app]: references/bundle-analyze-app.md
[bundle-r8-android]: references/bundle-r8-android.md
[bundle-hermes-mmap]: references/bundle-hermes-mmap.md
[bundle-native-assets]: references/bundle-native-assets.md
[bundle-library-size]: references/bundle-library-size.md
[bundle-code-splitting]: references/bundle-code-splitting.md

## Attribution

Based on "The Ultimate Guide to React Native Optimization" by Callstack.
```

## File: `skills/react-native-best-practices/agents/openai.yaml`
```yaml
interface:
  display_name: "React Native Best Practices"
  short_description: "React Native performance optimization guide"
  default_prompt: "Use $react-native-best-practices to diagnose and improve React Native performance."
```

## File: `skills/react-native-best-practices/references/bundle-analyze-app.md`
```markdown
---
title: Analyze App Bundle Size
impact: HIGH
tags: app-size, ruler, emerge-tools, thinning
---

# Skill: Analyze App Bundle Size

Measure iOS and Android app download/install sizes using Ruler, App Store Connect, and Emerge Tools.

## Quick Command

```bash
# Android (Ruler)
cd android && ./gradlew analyzeReleaseBundle

# iOS (Xcode export with thinning)
cd ios && xcodebuild -exportArchive \
  -archivePath MyApp.xcarchive \
  -exportPath ./export \
  -exportOptionsPlist ExportOptions.plist
# Check: App Thinning Size Report.txt
```

## When to Use

- App download size is too large
- Users complain about storage usage
- App approaching store limits
- Comparing releases for size regression

> **Note**: This skill involves interpreting visual size reports (Ruler, Emerge Tools X-Ray). AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing the reports manually, or await MCP-based visual feedback integration (see roadmap).

## Key Metrics

| Metric | Description | User Impact |
|--------|-------------|-------------|
| Download Size | Compressed, transferred over network | Download time, data usage |
| Install Size | Uncompressed, on device storage | Storage space |

**Google finding**: Every 6 MB increase reduces installs by 1%.

## Android: Ruler (Spotify)

### Setup

Add to `android/build.gradle`:

```groovy
buildscript {
    dependencies {
        classpath("com.spotify.ruler:ruler-gradle-plugin:2.0.0-beta-3")
    }
}
```

Add to `android/app/build.gradle`:

```groovy
apply plugin: "com.spotify.ruler"

ruler {
    abi.set("arm64-v8a")  // Target architecture
    locale.set("en")
    screenDensity.set(480)
    sdkVersion.set(34)
}
```

### Analyze

```bash
cd android
./gradlew analyzeReleaseBundle
```

Opens HTML report with:
- Download size
- Install size
- Component breakdown (biggest → smallest)

### CI Size Validation

```groovy
ruler {
    verification {
        downloadSizeThreshold = 20 * 1024 * 1024  // 20 MB
        installSizeThreshold = 50 * 1024 * 1024   // 50 MB
    }
}
```

Build fails if thresholds exceeded.

## iOS: Xcode App Thinning

### Via App Store Connect (Most Accurate)

After uploading to TestFlight:
1. Open App Store Connect
2. Go to your build
3. View size table by device variant

**Note**: TestFlight builds include debug data, App Store builds slightly larger due to DRM.

### Via Xcode Export

1. Archive app: **Product → Archive**
2. In Organizer, click **Distribute App**
3. Select **Custom**
4. Choose **App Thinning: All compatible device variants**

Or in `ExportOptions.plist`:

```xml
<key>thinning</key>
<string>&lt;thin-for-all-variants&gt;</string>
```

### Output

Creates folder with:
- **Universal IPA**: All variants combined
- **Thinned IPAs**: One per device variant
- **App Thinning Size Report.txt**:

```
Variant: SampleApp-<UUID>.ipa
App + On Demand Resources size: 3.5 MB compressed, 10.6 MB uncompressed
App size: 3.5 MB compressed, 10.6 MB uncompressed
```

- Compressed = Download size
- Uncompressed = Install size

## Emerge Tools (Cross-Platform)

Third-party service with visual analysis.

### Upload

Upload IPA, APK, or AAB through their web interface or CI integration.

### Features

![Emerge Tools X-Ray for iOS](images/emerge-xray-ios.png)

- **X-Ray**: Treemap visualization (like source-map-explorer for binaries)
  - Shows Frameworks (hermes.framework), Mach-O sections (TEXT, DATA), etc.
  - Color-coded: Binaries, Localizations, Fonts, Asset Catalogs, Videos, CoreML Models
  - Visible components: `main.jsbundle` (JS code), RCT modules, DYLD sections
- **Breakdown**: Component-by-component size
- **Insights**: Automated suggestions (use with caution)

**Caution**: Some suggestions may not apply to React Native (e.g., "remove Hermes").

## Size Comparison

| Tool | Platform | Accuracy | CI Integration |
|------|----------|----------|----------------|
| Ruler | Android | High | Yes (Gradle) |
| App Store Connect | iOS | Highest | No |
| Xcode Export | iOS | High | Yes (xcodebuild) |
| Emerge Tools | Both | High | Yes (API) |

## Typical React Native App Sizes

| Component | Approximate Size |
|-----------|------------------|
| Hermes engine | ~2-3 MB |
| React Native core | ~3-5 MB |
| JavaScript bundle | 1-10 MB |
| Assets (images, etc.) | Varies |

**Baseline empty app**: ~6-10 MB download

## Optimization Impact Example

| Optimization | Size Reduction |
|--------------|----------------|
| Enable R8 (Android) | ~30% |
| Remove unused polyfills | 400+ KB |
| Asset catalog (iOS) | 10-50% of assets |
| Tree shaking | 10-15% |

## Quick Commands

```bash
# Android release bundle size
cd android && ./gradlew bundleRelease
# Check: android/app/build/outputs/bundle/release/

# iOS archive
cd ios && xcodebuild -workspace ios/MyApp.xcworkspace \
  -scheme MyApp \
  -configuration Release \
  -archivePath MyApp.xcarchive \
  archive

# Export with thinning report
cd ios && xcodebuild -exportArchive \
  -archivePath MyApp.xcarchive \
  -exportPath ./export \
  -exportOptionsPlist ExportOptions.plist
```

## Related Skills

- [bundle-r8-android.md](./bundle-r8-android.md) - Reduce Android size
- [bundle-native-assets.md](./bundle-native-assets.md) - Optimize asset delivery
- [bundle-analyze-js.md](./bundle-analyze-js.md) - JS bundle analysis
```

## File: `skills/react-native-best-practices/references/bundle-analyze-js.md`
```markdown
---
title: Analyze JS Bundle Size
impact: CRITICAL
tags: bundle, analysis, source-map-explorer, expo-atlas
---

# Skill: Analyze JS Bundle Size

Use source-map-explorer and Expo Atlas to visualize what's in your JavaScript bundle.

## Quick Command

```bash
# React Native CLI
npx react-native bundle \
  --entry-file index.js \
  --bundle-output output.js \
  --platform ios \
  --sourcemap-output output.js.map \
  --dev false --minify true && \
npx source-map-explorer output.js --no-border-checks

# Expo
EXPO_UNSTABLE_ATLAS=true npx expo export --platform ios && npx expo-atlas
```

## When to Use

- JS bundle seems too large
- Want to identify heavy dependencies
- Investigating startup time issues
- Before/after optimization comparison

> **Note**: This skill involves interpreting visual treemap output (source-map-explorer, Expo Atlas). AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing the visualization manually, or await MCP-based visual feedback integration (see roadmap).

## Understanding Hermes Bytecode

Modern React Native (0.70+) uses Hermes bytecode, not raw JavaScript:
- Skips parsing at runtime
- Still benefits from smaller bundles
- Heavy imports still execute on startup

**Impact of bundle size:**
- Larger bytecode = longer download from store
- More imports on init path = slower TTI

## Method 1: source-map-explorer

### Generate Bundle with Source Map

**React Native CLI:**

```bash
npx react-native bundle \
  --entry-file index.js \
  --bundle-output output.js \
  --platform ios \
  --sourcemap-output output.js.map \
  --dev false \
  --minify true
```

**Expo (SDK 51+):**

```bash
npx expo export --platform ios --source-maps --output-dir dist
# Bundle at: dist/ios/_expo/static/js/ios/*.js
# Source map at: dist/ios/_expo/static/js/ios/*.map
```

### Analyze

```bash
npx source-map-explorer output.js --no-border-checks
```

**Note**: `--no-border-checks` needed due to Metro's non-standard source maps.

Opens browser with treemap visualization:

![Bundle Treemap from source-map-explorer](images/bundle-treemap-source-map-explorer.png)

The treemap shows:
- **Hierarchy**: `node_modules/` → `react-native/` → `Libraries/` → individual files
- **Size**: Box area proportional to file size (KB shown in labels)
- **Major components visible**: 
  - `react-native` (724.18 KB, 80.5%)
  - `Renderer` (208.44 KB) - ReactNativeRenderer-prod.js, ReactFabric-prod.js
  - `Components` (125.29 KB) - Touchable, ScrollView, etc.
  - `Animated` (79.48 KB) - Animation system
  - `virtualized-lists` (57.57 KB) - FlatList internals

Click on any section to drill down into that directory.

**Limitation**: May lose ~30% info due to mapping issues.

## Method 2: Expo Atlas

More accurate for Expo projects (or with workaround for bare RN).

### For Expo Projects

```bash
# Start with Atlas enabled
EXPO_UNSTABLE_ATLAS=true npx expo start --no-dev

# Or export
EXPO_UNSTABLE_ATLAS=true npx expo export
```

Then launch UI:

```bash
npx expo-atlas
```

![Expo Atlas Treemap](images/expo-atlas-treemap.png)

Expo Atlas provides more accurate visualization for Expo projects, with similar treemap interface showing module sizes and dependencies.

### For Non-Expo Projects

Use `expo-atlas-without-expo` package.

## Method 3: Re.Pack Bundle Analysis (Webpack/Rspack)

If using Re.Pack:

### webpack-bundle-analyzer

```bash
rspack build --analyze
```

### bundle-stats / statoscope

```bash
# Generate stats
npx react-native bundle \
  --platform android \
  --entry-file index.js \
  --dev false \
  --minify true \
  --json stats.json

# Analyze
npx bundle-stats --html --json stats.json
```

### Rsdoctor

```javascript
// rspack.config.js
const { RsdoctorRspackPlugin } = require('@rsdoctor/rspack-plugin');

module.exports = {
  plugins: [
    process.env.RSDOCTOR && new RsdoctorRspackPlugin(),
  ].filter(Boolean),
};
```

Run with:

```bash
RSDOCTOR=true npx react-native start
```

## What to Look For

### Red Flags

| Finding | Problem | Solution |
|---------|---------|----------|
| Entire library imported | Barrel exports | Use direct imports |
| Duplicate packages | Multiple versions | Dedupe in package.json |
| Dev dependencies in bundle | Incorrect imports | Check conditional imports |
| Large polyfills | Unnecessary for Hermes | Remove (see native-sdks-over-polyfills.md) |
| Moment.js with locales | Bloated date library | Switch to date-fns or dayjs |

### Common Offenders

- **Lodash full import**: Use `lodash-es` or specific imports
- **Moment.js**: Replace with `date-fns` or `dayjs`
- **Intl polyfills**: Check Hermes API and method coverage before removing them
- **AWS SDK**: Import specific services only

## Code Examples

### Identify Barrel Import Impact

```tsx
// BAD: Imports entire library through barrel
import { format } from 'date-fns';

// In bundle: All of date-fns loaded

// GOOD: Direct import
import format from 'date-fns/format';

// In bundle: Only format function
```

## Comparing Bundles

### source-map-explorer

```bash
# Generate baseline
npx react-native bundle ... --bundle-output baseline.js --sourcemap-output baseline.js.map

# Make changes, generate new bundle
npx react-native bundle ... --bundle-output current.js --sourcemap-output current.js.map

# Compare manually in browser
```

### Re.Pack (automated)

```bash
npx bundle-stats compare baseline-stats.json current-stats.json
```

## Quick Commands

**React Native CLI:**

```bash
# iOS bundle analysis
npx react-native bundle \
  --entry-file index.js \
  --bundle-output ios-bundle.js \
  --platform ios \
  --sourcemap-output ios-bundle.js.map \
  --dev false \
  --minify true && \
npx source-map-explorer ios-bundle.js --no-border-checks

# Android bundle analysis  
npx react-native bundle \
  --entry-file index.js \
  --bundle-output android-bundle.js \
  --platform android \
  --sourcemap-output android-bundle.js.map \
  --dev false \
  --minify true && \
npx source-map-explorer android-bundle.js --no-border-checks
```

**Expo:**

```bash
# Use Expo Atlas (recommended for Expo projects)
EXPO_UNSTABLE_ATLAS=true npx expo export --platform ios
npx expo-atlas
```

## Related Skills

- [bundle-barrel-exports.md](./bundle-barrel-exports.md) - Fix barrel import issues
- [bundle-tree-shaking.md](./bundle-tree-shaking.md) - Enable dead code elimination
- [bundle-library-size.md](./bundle-library-size.md) - Check library sizes before adding
```

## File: `skills/react-native-best-practices/references/bundle-barrel-exports.md`
```markdown
---
title: Avoid Barrel Exports
impact: CRITICAL
tags: bundle, imports, barrel, tree-shaking
---

# Skill: Avoid Barrel Exports

Refactor barrel imports (index files) to reduce bundle size and improve startup time.

## Quick Pattern

**Incorrect:**

```tsx
import { Button } from './components';
// Loads ALL exports from components/index.ts
```

**Correct:**

```tsx
import Button from './components/Button';
// Loads only Button
```

## When to Use

- Bundle contains unused code from libraries
- Circular dependency warnings in Metro
- Hot Module Replacement (HMR) breaks frequently
- TTI is slow due to module evaluation

## What Are Barrel Exports?

```tsx
// components/index.ts (barrel file)
export { Button } from './Button';
export { Card } from './Card';
export { Modal } from './Modal';
export { Sidebar } from './Sidebar';

// Usage (barrel import)
import { Button } from './components';
```

## Problems with Barrel Imports

### 1. Bundle Size Overhead

Metro includes **all exports** even if you use one:

```tsx
// Only need Button, but entire barrel is bundled
import { Button } from './components';
// Card, Modal, Sidebar also included!
```

### 2. Runtime Overhead

All modules evaluate before returning your import:

```tsx
import { Button } from './components';
// JavaScript must evaluate:
// - Button.tsx
// - Card.tsx
// - Modal.tsx  
// - Sidebar.tsx
// Even though you only use Button
```

### 3. Circular Dependencies

Barrel files make cycles easier to create accidentally:

```
Warning: Require cycle:
  components/index.ts -> Button.tsx -> utils/index.ts -> components/index.ts
```

Breaks HMR, causes unpredictable behavior.

## Solution 1: Direct Imports

Replace barrel imports with direct paths:

```tsx
// BEFORE: Barrel import
import { Button, Card } from './components';

// AFTER: Direct imports
import Button from './components/Button';
import Card from './components/Card';
```

### Enforce with ESLint

```bash
npm install -D eslint-plugin-no-barrel-files
```

```javascript
// eslint.config.js
import noBarrelFiles from 'eslint-plugin-no-barrel-files';

export default [
  {
    plugins: { 'no-barrel-files': noBarrelFiles },
    rules: {
      'no-barrel-files/no-barrel-files': 'error',
    },
  },
];
```

## Solution 2: Tree Shaking (Automatic)

Enable tree shaking to automatically remove unused barrel exports.

### Expo SDK 52+

```tsx
// metro.config.js
const { getDefaultConfig } = require('expo/metro-config');
const config = getDefaultConfig(__dirname);

config.transformer.getTransformOptions = async () => ({
  transform: {
    experimentalImportSupport: true,
  },
});

module.exports = config;
```

```bash
# .env
EXPO_UNSTABLE_METRO_OPTIMIZE_GRAPH=1
EXPO_UNSTABLE_TREE_SHAKING=1
```

### metro-serializer-esbuild

```bash
npm install @rnx-kit/metro-serializer-esbuild
```

### Re.Pack (Webpack/Rspack)

Tree shaking built-in.

## Real-World Example: date-fns

```tsx
// BAD: Imports entire library
import { format, addDays, isToday } from 'date-fns';

// GOOD: Direct imports
import format from 'date-fns/format';
import addDays from 'date-fns/addDays';
import isToday from 'date-fns/isToday';
```

## Library-Specific Solutions

Some libraries provide Babel plugins:

### React Native Paper

```javascript
// babel.config.js
module.exports = {
  plugins: [
    'react-native-paper/babel',  // Auto-transforms imports
  ],
};
```

Transforms:
```tsx
import { Button } from 'react-native-paper';
// Into:
import Button from 'react-native-paper/lib/module/components/Button';
```

## Refactoring Strategy

### Step 1: Identify Barrel Files

Look for `index.ts` files with multiple exports:

```bash
grep -r "export \* from" src/
grep -r "export { .* } from" src/
```

### Step 2: Update Imports

```tsx
// Find all usages
// VS Code: Cmd+Shift+F for "from './components'"

// Replace each with direct import
import Button from './components/Button';
```

### Step 3: (Optional) Keep Barrel for External API

If your package is consumed by others:

```tsx
// Keep index.ts for package API
// components/index.ts
export { Button } from './Button';

// Internal code uses direct imports
// src/screens/Home.tsx
import Button from '../components/Button';
```

## Migration Script Example

```bash
# Use codemod or search-replace
# Find: import { (\w+) } from '\.\/components';
# Replace: import $1 from './components/$1';
```

## Verification

After refactoring:

1. Run bundle analysis (see [bundle-analyze-js.md](./bundle-analyze-js.md))
2. Compare sizes before/after
3. Check for circular dependency warnings

## Common Pitfalls

- **Breaking external consumers**: If publishing a library, keep barrel for public API
- **IDE auto-imports**: Configure IDE to prefer direct imports
- **Inconsistent patterns**: Enforce with ESLint across team

## Related Skills

- [bundle-analyze-js.md](./bundle-analyze-js.md) - Verify impact
- [bundle-tree-shaking.md](./bundle-tree-shaking.md) - Automatic solution
- [bundle-library-size.md](./bundle-library-size.md) - Check library patterns
```

## File: `skills/react-native-best-practices/references/bundle-code-splitting.md`
```markdown
---
title: Remote Code Loading
impact: MEDIUM
tags: code-splitting, repack, lazy-loading, chunks
---

# Skill: Remote Code Loading

Set up code splitting with Re.Pack for on-demand bundle loading from trusted, first-party assets.

## Quick Pattern

**Before (static import):**

```jsx
import SettingsScreen from './screens/SettingsScreen';
```

**After (lazy loaded chunk):**

```jsx
const SettingsScreen = React.lazy(() =>
  import(/* webpackChunkName: "settings" */ './screens/SettingsScreen')
);

<Suspense fallback={<Loading />}>
  <SettingsScreen />
</Suspense>
```

## When to Use

Consider code splitting when:
- **Not using Hermes** (JSC/V8 benefits more)
- App size exceeds 200 MB (Play Store limit)
- Building micro-frontend architecture
- Loading features based on user permissions
- Other optimizations exhausted

**Note**: Hermes already uses memory mapping for efficient bundle reading. Benefits of code splitting are minimal with Hermes or even counterproductive in some cases.

## Security Model

Remote chunks are executable application code. Only load chunks that you build and publish yourself.

Keep these guardrails in place:
- Serve chunks only from a first-party, HTTPS-only origin you control
- Resolve `scriptId` through a fixed allowlist or release manifest
- Fail closed if a chunk is missing or unexpected
- Do not load chunks from user-controlled input, query params, or third-party domains

## Prerequisites

- Re.Pack installed (replaces Metro)

```bash
npx @callstack/repack-init
```

## Step-by-Step Instructions

### 1. Initialize Re.Pack

```bash
npx @callstack/repack-init
```

Follow prompts to migrate from Metro. Check [migration guide](https://re-pack.dev/brain/knowledge/docs_legacy/getting-started/quick-start).

### 2. Create Split Point with React.lazy

```tsx
// BEFORE: Static import
import SettingsScreen from './screens/SettingsScreen';

// AFTER: Dynamic import (creates split point)
const SettingsScreen = React.lazy(() =>
  import(/* webpackChunkName: "settings" */ './screens/SettingsScreen')
);
```

### 3. Wrap with Suspense

```tsx
import React, { Suspense } from 'react';

const App = () => {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <SettingsScreen />
    </Suspense>
  );
};
```

### 4. Configure Chunk Loading

```jsx
// index.js (before AppRegistry)
import { ScriptManager, Script } from '@callstack/repack/client';

const CHUNK_URLS = {
  settings: 'https://assets.example.com/app/v42/settings.chunk.bundle',
};

ScriptManager.shared.addResolver((scriptId) => ({
  url: __DEV__ ? Script.getDevServerURL(scriptId) : getChunkUrl(scriptId),
}));

function getChunkUrl(scriptId) {
  const url = CHUNK_URLS[scriptId];

  if (!url) {
    throw new Error(`Unknown chunk: ${scriptId}`);
  }

  return url;
}

AppRegistry.registerComponent(appName, () => App);
```

### 5. Build and Deploy Chunks

Build generates:
- `index.bundle` - Main bundle
- `settings.chunk.bundle` - Lazy-loaded chunk

Deploy chunks to a first-party CDN with versioned paths, and keep the allowlist or manifest in sync with the app release.

## Complete Example

```tsx
// App.tsx
import React, { Suspense, useState } from 'react';
import { Button, View, ActivityIndicator } from 'react-native';

// Lazy load heavy feature
const HeavyFeature = React.lazy(() =>
  import(/* webpackChunkName: "heavy-feature" */ './HeavyFeature')
);

const App = () => {
  const [showFeature, setShowFeature] = useState(false);
  
  return (
    <View>
      <Button 
        title="Load Feature" 
        onPress={() => setShowFeature(true)} 
      />
      
      {showFeature && (
        <Suspense fallback={<ActivityIndicator />}>
          <HeavyFeature />
        </Suspense>
      )}
    </View>
  );
};
```

## Module Federation (Advanced)

For micro-frontend architecture:

```tsx
// Host app loads remote module
const RemoteModule = React.lazy(() =>
  import('remote-app/Module')
);
```

Enables:
- Independent team deployments
- Shared dependencies
- Runtime composition

**Complexity warning**: Only use when organizational benefits outweigh overhead. Federation increases the trust boundary, so keep the same first-party origin and allowlist rules as above.

### Version Management

Consider [Zephyr Cloud](https://zephyr-cloud.io/) for:
- Sub-second deployments
- Version management
- Re.Pack integration

## Caching Strategy

```tsx
ScriptManager.shared.addResolver((scriptId) => ({
  url: getChunkUrl(scriptId),
  cache: {
    // Enable caching
    enabled: true,
    // Cache location
    path: `${FileSystem.cacheDirectory}/chunks/`,
  },
}));
```

## When NOT to Use

| Scenario | Why Not |
|----------|---------|
| Using Hermes | mmap already efficient |
| Small app | Overhead not worth it |
| Simple navigation | Native navigation better |
| Quick iteration needed | Added complexity |

## Hermes Memory Mapping

Hermes reads bytecode lazily via mmap:
- Only loads executed code into memory
- No parse step needed
- Code splitting provides marginal benefit

## Verification

```tsx
// Check if chunk loaded correctly
ScriptManager.shared.on('loading', (scriptId) => {
  console.log(`Loading: ${scriptId}`);
});

ScriptManager.shared.on('loaded', (scriptId) => {
  console.log(`Loaded: ${scriptId}`);
});

ScriptManager.shared.on('error', (scriptId, error) => {
  console.error(`Failed: ${scriptId}`, error);
});
```

## Common Pitfalls

- **Forgetting Suspense**: Lazy components need fallback
- **Wrong CDN path**: Chunks 404 in production
- **No caching**: Re-downloads on every load
- **Too many chunks**: Network overhead exceeds savings
- **Untrusted chunk source**: Remote JS from third-party or user-controlled origins is equivalent to remote code execution

## Related Skills

- [bundle-tree-shaking.md](./bundle-tree-shaking.md) - Re.Pack tree shaking
- [bundle-analyze-js.md](./bundle-analyze-js.md) - Measure chunk sizes
- [native-measure-tti.md](./native-measure-tti.md) - Verify TTI impact
```

## File: `skills/react-native-best-practices/references/bundle-hermes-mmap.md`
```markdown
---
title: Disable JS Bundle Compression
impact: HIGH
tags: android, hermes, mmap, tti, startup
---

# Skill: Disable JS Bundle Compression

Disable Android JS bundle compression to enable Hermes memory mapping for faster startup.

## Quick Config

```groovy
// android/app/build.gradle
android {
    androidResources {
        noCompress += ["bundle"]
    }
}
```

**Note**: Default in React Native 0.79+. Only needed for 0.78 and earlier.

## When to Use

- Android app using Hermes
- Want faster TTI (Time to Interactive)
- Willing to trade install size for startup speed
- React Native version is 0.78 or earlier, skip otherwise (see applicability)

## Background

Android compresses most files in APK/AAB by default, including `index.android.bundle`.

**Problem**: Compressed files can't be memory-mapped (mmap).

**Impact**: Hermes must decompress before reading, losing one of its key optimizations.

## How Hermes Memory Mapping Works

Without compression:
1. Hermes opens bytecode file
2. OS memory-maps directly to disk
3. Only pages actually accessed are loaded
4. **Result**: Fast startup, low memory

With compression:
1. Android decompresses entire bundle
2. Loaded into memory
3. Then Hermes processes
4. **Result**: Slower startup, higher memory

## Step-by-Step Implementation

### Edit build.gradle

In `android/app/build.gradle`:

```groovy
android {
    androidResources {
        noCompress += ["bundle"]
    }
}
```

### Full Context

```groovy
android {
    namespace "com.myapp"
    defaultConfig {
        applicationId "com.myapp"
        // ...
    }
    
    androidResources {
        noCompress += ["bundle"]
    }
    
    buildTypes {
        release {
            minifyEnabled true
            // ...
        }
    }
}
```

### Rebuild

```bash
cd android
./gradlew clean
./gradlew bundleRelease
# or
./gradlew assembleRelease
```

## Trade-offs

| Metric | Without Change | With Change |
|--------|----------------|-------------|
| Download size | Same | Same |
| Install size | Smaller | **+8% larger** |
| TTI | Slower | **-16% faster** |

**Real example**: 75.9 MB install → 82 MB install, but 450ms faster startup.

## Applicability

**React Native 0.78 and earlier**: Apply this optimization manually.

**React Native 0.79+**: Skip this—bundle compression is disabled by default.

## Verification

### Check APK Contents

```bash
# Unzip APK
unzip app-release.apk -d apk-contents

# Check if bundle is compressed
file apk-contents/assets/index.android.bundle
# Should show: "data" (not "gzip compressed")
```

### Measure TTI Impact

Use performance markers (see [native-measure-tti.md](./native-measure-tti.md)) to compare before/after.

## Multiple File Types

If you have other files that benefit from mmap:

```groovy
androidResources {
    noCompress += ["bundle", "hbc", "data"]
}
```

## Common Pitfalls

- **Not rebuilding**: Change requires clean build
- **Wrong config location**: Must be in `android` block
- **Ignoring size increase**: Monitor user feedback on install size
- **Already default**: Check if React Native version includes this

## Expo Notes

For Expo projects, run `npx expo prebuild` first to generate `android/` folder, then apply the `build.gradle` changes. Add `android/` to version control or use a [config plugin](https://docs.expo.dev/config-plugins/introduction/) for persistent changes.

## Should You Enable This?

| Scenario | Recommendation |
|----------|---------------|
| Startup-critical app | ✅ Enable |
| Storage-sensitive users | ⚠️ Test impact |
| Already fast TTI | Maybe not worth it |
| Large JS bundle | ✅ Bigger benefit |

## Related Skills

- [native-measure-tti.md](./native-measure-tti.md) - Measure TTI improvement
- [bundle-analyze-app.md](./bundle-analyze-app.md) - Check size impact
- [bundle-r8-android.md](./bundle-r8-android.md) - Offset size increase
```

## File: `skills/react-native-best-practices/references/bundle-library-size.md`
```markdown
---
title: Determine Library Size
impact: MEDIUM
tags: dependencies, bundlephobia, library-size
---

# Skill: Determine Library Size

Evaluate third-party library size impact before adding to your project.

## Quick Command

```bash
# Check size before installing
# Visit: https://bundlephobia.com/package/[package-name]

# Or use CLI
npx bundle-phobia-cli <package-name>
```

## When to Use

- Evaluating new dependencies
- Comparing alternative libraries
- Auditing existing dependencies
- Investigating bundle bloat

## Tools Overview

| Tool | Type | Best For |
|------|------|----------|
| bundlephobia.com | Web | Quick size check |
| pkg-size.dev | Web | Backup/alternative |
| Import Cost (VS Code) | IDE extension | Real-time feedback |

## bundlephobia.com

### Usage

Visit [bundlephobia.com](https://bundlephobia.com) and enter package name.

### Shows

- **Minified size**: Raw JS size
- **Minified + Gzipped**: Network transfer size
- **Download time**: Estimated on various connections
- **Dependencies**: What else gets pulled in
- **Composition**: Breakdown by dependency

### Example Analysis

```
react-native-paper
├── Minified: 312 kB
├── Gzipped: 78 kB
└── Dependencies: 12 packages
    ├── @callstack/react-theme-provider
    ├── color
    └── ...
```

## pkg-size.dev

Backup when bundlephobia fails.

Visit [pkg-size.dev](https://pkg-size.dev) with package name.

**Difference**: Actually installs package in web container, may be more accurate for edge cases.

## Import Cost (VS Code Extension)

### Install

Search "Import Cost" in VS Code extensions or:

```bash
code --install-extension wix.vscode-import-cost
```

### Usage

Shows inline size next to imports:

```tsx
import React from 'react';           // 6.5K (gzipped)
import { View, Text } from 'react-native';  // 0B (native)
import lodash from 'lodash';         // 71.5K (gzipped: 24.7K)
import get from 'lodash/get';        // 8K (gzipped: 2.9K)
```

### Limitations

- Uses Webpack internally (not Metro)
- May fail on React Native-specific packages
- Doesn't account for tree shaking

## Comparison Workflow

### Before Adding Dependency

1. Check on bundlephobia:
   ```
   https://bundlephobia.com/package/[package-name]
   ```

2. Compare alternatives:
   ```
   moment (289 kB) vs date-fns (75 kB) vs dayjs (6 kB)
   ```

3. Check what you actually need:
   - Full library import vs specific functions
   - Native alternative available?

### After Adding

1. Analyze bundle (see [bundle-analyze-js.md](./bundle-analyze-js.md))
2. Verify actual impact matches expected
3. Check for duplicate dependencies

## Size Guidelines

| Size (gzipped) | Assessment | Action |
|----------------|------------|--------|
| < 5 KB | Small | Generally fine |
| 5-20 KB | Medium | Evaluate necessity |
| 20-50 KB | Large | Look for alternatives |
| > 50 KB | Very large | Strong justification needed |

## Common Large Dependencies

| Library | Size (gzipped) | Alternative |
|---------|----------------|-------------|
| moment | ~70 KB | dayjs (~3 KB) |
| lodash (full) | ~25 KB | lodash-es + direct imports |
| aws-sdk (full) | 200+ KB | @aws-sdk/client-* |
| crypto-js | ~15 KB | react-native-quick-crypto |

## Quick Size Check Script

```bash
# Check size before installing
npx bundle-phobia-cli <package-name>

# Or use npm directly (less accurate)
npm pack <package-name> --dry-run 2>&1 | grep "total files"
```

## Decision Matrix

| Factor | Keep JS Library | Use Native Alternative |
|--------|-----------------|------------------------|
| Size | > 50 KB | < 50 KB |
| Platform coverage | Both platforms | Single platform OK |
| Performance | Not critical | Critical path |
| Functionality | Simple | Complex computation |

## Code Example: Optimizing Imports

```tsx
// BAD: Full library (71.5 KB)
import _ from 'lodash';
_.get(obj, 'path.to.value');

// BETTER: Specific import (8 KB)
import get from 'lodash/get';
get(obj, 'path.to.value');

// BEST: Native JS (0 KB)
obj?.path?.to?.value;
```

## Related Skills

- [bundle-analyze-js.md](./bundle-analyze-js.md) - Verify actual bundle impact
- [bundle-barrel-exports.md](./bundle-barrel-exports.md) - Optimize how you import
- [native-sdks-over-polyfills.md](./native-sdks-over-polyfills.md) - Native alternatives to JS libs
```

## File: `skills/react-native-best-practices/references/bundle-native-assets.md`
```markdown
---
title: Native Assets
impact: HIGH
tags: assets, images, asset-catalog, app-thinning
---

# Skill: Native Assets

Configure platform-specific asset delivery to reduce app download size.

## Quick Config

**iOS Asset Catalog (Build Phase):**

```bash
# Add to "Bundle React Native code and images" build phase
export EXTRA_PACKAGER_ARGS="--asset-catalog-dest ./"
```

**Android**: Automatic via AAB — Play Store delivers correct density per device.

## When to Use

- Images bloating app size
- Different device densities need different assets
- Want to leverage App Store/Play Store optimization
- Using high-resolution images

## Concept: Size Suffixes

React Native convention for multiple resolutions:

```
assets/
├── image.jpg       # 1x resolution (base)
├── image@2x.jpg    # 2x resolution
└── image@3x.jpg    # 3x resolution
```

```tsx
// React Native selects best one for device
<Image source={require('./assets/image.jpg')} />
```

## Android: Automatic Optimization

Android handles this automatically.

### How It Works

1. Build AAB:
   ```bash
   cd android && ./gradlew bundleRelease
   ```

2. Metro places images in density folders:
   ```
   android/app/build/outputs/bundle/release/
   └── base/
       └── res/
           ├── drawable-mdpi-v4/     # 1x
           ├── drawable-hdpi-v4/     # 1.5x
           ├── drawable-xhdpi-v4/    # 2x
           ├── drawable-xxhdpi-v4/   # 3x
           └── drawable-xxxhdpi-v4/  # 4x
   ```

3. Play Store delivers only needed density per device.

**No configuration required** for Android.

## iOS: Asset Catalog Setup

iOS requires explicit configuration.

### Step 1: Create Asset Catalog

Create folder in `ios/`:

```
ios/RNAssets.xcassets/
```

**Important**: Must be named exactly `RNAssets.xcassets` (hardcoded in React Native).

### Step 2: Configure Build Phase

In Xcode:
1. Open project settings
2. Go to **Build Phases**
3. Find **"Bundle React Native code and images"**
4. Add before line 8:

```bash
export EXTRA_PACKAGER_ARGS="--asset-catalog-dest ./"
```

### Step 3: Build

Run build to populate asset catalog:

```bash
npx react-native run-ios --mode Release
```

Or manually:

```bash
npx react-native bundle \
  --entry-file index.js \
  --bundle-output ios-bundle.js \
  --platform ios \
  --dev false \
  --asset-catalog-dest ios \
  --assets-dest ios/assets
```

### Step 4: Verify

After build, `RNAssets.xcassets` contains:

```
ios/RNAssets.xcassets/
└── assets_image_image.imageset/
    ├── Contents.json
    ├── image.jpg
    ├── image@2x.jpg
    └── image@3x.jpg
```

App Store then delivers only needed resolution.

## Before/After Comparison

### Without Asset Catalog (All Variants)

```
App bundle contains:
├── image.jpg       (100 KB)
├── image@2x.jpg    (300 KB)
└── image@3x.jpg    (600 KB)
Total: 1 MB
```

### With Asset Catalog (Device-Specific)

```
iPhone 15 Pro receives:
└── image@3x.jpg    (600 KB)
Total: 600 KB  (40% smaller)
```

## Asset Optimization Tips

### 1. Compress Images

Use tools before adding to project:

```bash
# ImageOptim (macOS)
# TinyPNG (web)
# sharp (programmatic)

npx sharp-cli input.jpg -o output.jpg --quality 80
```

### 2. Use Appropriate Formats

| Format | Best For |
|--------|----------|
| JPEG | Photos |
| PNG | Icons, transparency |
| WebP | Both (smaller) |
| SVG | Vector icons |

### 3. Consider react-native-fast-image

Caching and better image handling:

```bash
npm install react-native-fast-image
```

## Verification

### iOS App Thinning Report

After export, check `App Thinning Size Report.txt`:

```
Variant: MyApp-<UUID>.ipa
Supported variant descriptors: iPhone15,2 ...
App size: 3.5 MB compressed, 10.6 MB uncompressed
```

### Use Emerge Tools

Upload IPA to see asset breakdown.

## Common Pitfalls

- **Wrong folder name**: Must be `RNAssets.xcassets` exactly
- **Missing build phase config**: Assets not processed
- **Not using size suffixes**: All variants included anyway
- **Forgetting to rebuild**: Changes need fresh build

## Future Note

As of January 2025, Asset Catalog is not default. May become default in future React Native versions.

## Related Skills

- [bundle-analyze-app.md](./bundle-analyze-app.md) - Verify asset impact
- [bundle-r8-android.md](./bundle-r8-android.md) - Android code optimization
```

## File: `skills/react-native-best-practices/references/bundle-r8-android.md`
```markdown
---
title: R8 Code Shrinking
impact: HIGH
tags: android, r8, proguard, minify, shrink
---

# Skill: R8 Code Shrinking

Enable R8 for Android to shrink, optimize, and obfuscate native code.

## Quick Config

```groovy
// android/app/build.gradle
def enableProguardInReleaseBuilds = true

android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true
        }
    }
}
```

## When to Use

- Android app size too large
- Want to obfuscate code for security
- Building release APK/AAB

## What is R8?

R8 replaces ProGuard in Android:
- **Shrinks**: Removes unused code
- **Optimizes**: Improves bytecode
- **Obfuscates**: Renames classes/methods

**Compatibility**: Uses ProGuard configuration format.

## Step-by-Step Instructions

### 1. Enable R8

Edit `android/app/build.gradle`:

```groovy
def enableProguardInReleaseBuilds = true
```

This sets `minifyEnabled = true` for release builds.

### 2. Enable Resource Shrinking (Optional)

Further reduces size by removing unused resources:

```groovy
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true  // Requires minifyEnabled
            
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

### 3. Configure ProGuard Rules (If Needed)

Edit `android/app/proguard-rules.pro`. React Native defaults are usually sufficient—only add rules when specific libraries break after enabling R8.

**Only add if using Firebase (`@react-native-firebase/*`):**

```proguard
-keep class io.invertase.firebase.** { *; }
-dontwarn io.invertase.firebase.**
```

**Only add if using Retrofit:**

```proguard
-keepattributes Signature
-keepattributes *Annotation*
-keep class retrofit2.** { *; }
-dontwarn retrofit2.**
```

See [Common Library Rules](#common-library-rules) and [Troubleshooting](#troubleshooting) for more examples.

### 4. Build and Test

```bash
cd android
./gradlew assembleRelease
# or
./gradlew bundleRelease
```

**Critical**: Test thoroughly! R8 can remove code it thinks is unused.

## ProGuard Rules Reference

| Rule | Effect |
|------|--------|
| `-keep class X` | Don't remove class X |
| `-keepclassmembers` | Keep members but allow rename |
| `-keepnames` | Keep names but allow removal if unused |
| `-dontwarn X` | Suppress warnings for X |
| `-dontobfuscate` | Disable obfuscation |

### Keep Entire Package

```proguard
-keep class com.mypackage.** { *; }
```

### Keep Classes with Annotation

```proguard
-keep @interface com.facebook.proguard.annotations.DoNotStrip
-keep @com.facebook.proguard.annotations.DoNotStrip class *
-keepclassmembers class * {
    @com.facebook.proguard.annotations.DoNotStrip *;
}
```

## Disable Obfuscation (If Needed)

```proguard
# proguard-rules.pro
-dontobfuscate
```

Use when:
- Debugging crashes (stack traces more readable)
- Library requires class names

## Size Impact

Example from guide:
- **Without R8**: 9.5 MB
- **With R8**: 6.3 MB
- **Savings**: 33%

Larger apps may see 20-30% reduction.

## Troubleshooting

### App Crashes After R8

Usually means needed class was removed.

**Debug steps**:

1. Check crash log for class name
2. Add keep rule:
   ```proguard
   -keep class com.example.CrashedClass { *; }
   ```
3. Rebuild and test

### Library Specific Rules

Many libraries provide ProGuard rules. Check:
- Library README
- Library's `consumer-proguard-rules.pro`
- Stack Overflow for library + proguard

### Common Library Rules

```proguard
# Hermes (usually auto-included)
-keep class com.facebook.hermes.unicode.** { *; }

# React Native
-keep class com.facebook.react.** { *; }

# Gson
-keepattributes Signature
-keep class com.google.gson.** { *; }

# OkHttp
-dontwarn okhttp3.**
-dontwarn okio.**
```

## Verification

### Check APK Size

```bash
# Build
./gradlew assembleRelease

# Check size
ls -la android/app/build/outputs/apk/release/
```

### Use Ruler for Detailed Analysis

See [bundle-analyze-app.md](./bundle-analyze-app.md).

### Verify Obfuscation

Decompile APK to check class names are obfuscated:

```bash
# Using jadx or similar
jadx android/app/build/outputs/apk/release/app-release.apk
```

## Common Pitfalls

- **Not testing release build**: Always QA with R8 enabled
- **Missing library rules**: Check library docs
- **Over-keeping**: Too many keep rules negates benefits
- **Reflection**: Code using reflection may break

## Related Skills

- [bundle-analyze-app.md](./bundle-analyze-app.md) - Measure size impact
- [bundle-native-assets.md](./bundle-native-assets.md) - Further size reduction
```

## File: `skills/react-native-best-practices/references/bundle-tree-shaking.md`
```markdown
---
title: Tree Shaking
impact: HIGH
tags: bundle, tree-shaking, dead-code, metro, repack
---

# Skill: Tree Shaking

Enable dead code elimination to remove unused exports from your JavaScript bundle.

## Quick Config

```bash
# .env (Expo SDK 52+)
EXPO_UNSTABLE_METRO_OPTIMIZE_GRAPH=1
EXPO_UNSTABLE_TREE_SHAKING=1
```

```javascript
// metro.config.js
config.transformer.getTransformOptions = async () => ({
  transform: { experimentalImportSupport: true },
});
```

```javascript
// babel.config.js (non-Expo projects must set `disableImportExportTransform`)
module.exports = {
  presets: [
    [
      'module:@react-native/babel-preset',
      { disableImportExportTransform: true },
    ],
  ],
};
```

## When to Use

- Bundle includes unused library code
- Want automatic barrel export optimization
- Using Expo SDK 52+ (recommended approach)
- Project already uses Re.Pack (`@callstack/repack`)

## Platform Support

| Bundler        | Tree Shaking    | Notes                        |
| -------------- | --------------- | ---------------------------- |
| Metro          | ❌ No           | Use metro-serializer-esbuild |
| Expo (SDK 52+) | ✅ Experimental | Requires config              |
| Re.Pack        | ✅ Yes          | Built-in via Webpack/Rspack  |

## Setup: Expo SDK 52+

### 1. Enable Import Support

```javascript
// metro.config.js
const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

config.transformer.getTransformOptions = async () => ({
  transform: {
    experimentalImportSupport: true,
  },
});

module.exports = config;
```

### 2. Enable Tree Shaking

Create/edit `.env`:

```bash
EXPO_UNSTABLE_METRO_OPTIMIZE_GRAPH=1
EXPO_UNSTABLE_TREE_SHAKING=1
```

**Note**: Only applies in production builds.

## Setup: Metro with ESBuild

```bash
npm install @rnx-kit/metro-serializer-esbuild
```

Configure in metro.config.js.

## Setup: Re.Pack (Only If Already Installed)

> **Important**: Re.Pack (`@callstack/repack`) is a custom bundler using Rspack/Webpack. Only apply these instructions if the project already has Re.Pack configured. Do not suggest migrating a codebase to Re.Pack—it's rarely necessary and requires significant setup.

**If project has `@callstack/repack` in dependencies:**

Tree shaking is enabled by default with Rspack. Verify in config:

```javascript
// rspack.config.js or webpack.config.js
module.exports = {
  optimization: {
    usedExports: true, // Mark unused exports
    minimize: true, // Remove during minification
  },
};
```

## Platform Shaking

Code inside `Platform.OS` and `Platform.select` checks is removed for other platforms:

```tsx
// IMPORTANT: import Platform directly from 'react-native'
import { Platform } from 'react-native';

if (Platform.OS === 'ios') {
  // Removed from Android bundle
}

if (Platform.select({ ios: true, android: false }) === 'ios') {
  // Removed from Android bundle
}
```

**Critical**: Must use direct import. This does NOT work:

```tsx
import * as RN from 'react-native';
if (RN.Platform.OS === 'ios') {
  // NOT removed - optimization fails
}
```

For non-Expo projects, requires both `experimentalImportSupport: true` in Metro config and `disableImportExportTransform: true` in Babel config.

Impact: Savings from enabling platform shaking on a bare React Native Community CLI project are:
- 5% smaller Hermes bytecode (2.79 MB → 2.64 MB)
- 15% smaller minified JS bundle (1 MB → 0.85 MB)

## Requirements for Tree Shaking

### ESM Imports Required

```tsx
// ✅ ESM - Tree shakeable
import { foo } from './module';

// ❌ CommonJS - Not tree shakeable
const { foo } = require('./module');
```

### Side Effects Declaration

Libraries must declare side-effect-free in `package.json`:

```json
{
  "sideEffects": false
}
```

Or specify files with side effects:

```json
{
  "sideEffects": ["*.css", "./src/polyfills.js"]
}
```

## Size Impact

| Bundle Type       | Metro (MB) | Re.Pack (MB) | Change   |
| ----------------- | ---------- | ------------ | -------- |
| Production        | 35.63      | 38.48        | +8%      |
| Prod Minified     | 15.54      | 13.36        | **-14%** |
| Prod HBC          | 21.79      | 19.35        | **-11%** |
| Prod Minified HBC | 21.62      | 19.05        | **-12%** |

**Expected improvement**: 10-15% bundle size reduction.

## Verification

1. Build production bundle (see [bundle-analyze-js.md](./bundle-analyze-js.md))
2. Analyze with source-map-explorer (see [bundle-analyze-js.md](./bundle-analyze-js.md))
3. Search for functions you know are unused
4. If found → tree shaking not working

### Test Example

```tsx
// test-treeshake.js
export const usedFunction = () => 'used';
export const unusedFunction = () => 'unused'; // Should be removed

// app.js
import { usedFunction } from './test-treeshake';
```

After building, search bundle for `unusedFunction`. Should not exist.

## Common Pitfalls

- **Not using production build**: Tree shaking only in prod
- **CommonJS modules**: Need ESM for full effectiveness
- **Side effects not declared**: Library may not be shakeable
- **Dynamic imports**: `require(variable)` prevents analysis
- **Babel/Metro config mismatch**: `disableImportExportTransform` must match `experimentalImportSupport`

## Related Skills

- [bundle-analyze-js.md](./bundle-analyze-js.md) - Verify tree shaking effect
- [bundle-barrel-exports.md](./bundle-barrel-exports.md) - Manual alternative
- [bundle-code-splitting.md](./bundle-code-splitting.md) - Re.Pack code splitting
```

## File: `skills/react-native-best-practices/references/js-animations-reanimated.md`
```markdown
---
title: High-Performance Animations
impact: MEDIUM
tags: reanimated, animations, worklets, ui-thread
---

# Skill: High-Performance Animations

Use React Native Reanimated for smooth 60+ FPS animations.

## Quick Pattern

**Incorrect (JS thread - blocks on heavy work):**

```jsx
const opacity = useRef(new Animated.Value(0)).current;
Animated.timing(opacity, { toValue: 1 }).start();
```

**Correct (UI thread - smooth even during JS work):**

```jsx
const opacity = useSharedValue(0);
const style = useAnimatedStyle(() => ({ opacity: opacity.value }));
opacity.value = withTiming(1);
```

## When to Use

- Animations drop frames or feel janky
- UI freezes during animations
- Need gesture-driven animations
- Want animations to run during heavy JS work

## Prerequisites

- `react-native-reanimated` (v4+) and `react-native-worklets` installed

```bash
npm install react-native-reanimated react-native-worklets
```

Add to `babel.config.js`:

```javascript
module.exports = {
  plugins: ['react-native-worklets/plugin'],  // Must be last
};
```

> **Note**: Reanimated 4 requires React Native's **New Architecture** (Fabric + TurboModules). The Legacy Architecture is no longer supported. If upgrading from v3, see the migration notes at the end of this document.

## Key Concepts

### Main Thread vs JS Thread

- **Main/UI Thread**: Handles native rendering (60+ FPS target)
- **JS Thread**: Runs React and your JavaScript

**Problem**: Heavy JS work blocks animations running on JS thread.

**Solution**: Run animations on UI thread with Reanimated worklets.

## Step-by-Step Instructions

### 1. Basic Animated Style (UI Thread)

```jsx
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming
} from 'react-native-reanimated';

const FadeInView = () => {
  const opacity = useSharedValue(0);

  // This runs on UI thread - won't be blocked by JS
  const animatedStyle = useAnimatedStyle(() => {
    return { opacity: opacity.value };
  });

  useEffect(() => {
    opacity.value = withTiming(1, { duration: 500 });
  }, []);

  return <Animated.View style={[styles.box, animatedStyle]} />;
};
```

### 2. Run Code on UI Thread with `scheduleOnUI`

```jsx
import { scheduleOnUI } from 'react-native-worklets';

const triggerAnimation = () => {
  scheduleOnUI(() => {
    'worklet';
    console.log('Running on UI thread');
    // Direct UI manipulations here
  });
};
```

### 3. Call JS from UI Thread with `scheduleOnRN`

```jsx
import { scheduleOnRN } from 'react-native-worklets';

// Regular JS function
const trackAnalytics = (value) => {
  analytics.track('animation_complete', { value });
};

const AnimatedComponent = () => {
  const progress = useSharedValue(0);

  const animatedStyle = useAnimatedStyle(() => {
    // When animation completes, call JS function
    if (progress.value === 1) {
      scheduleOnRN(trackAnalytics, progress.value);
    }
    return { opacity: progress.value };
  });

  return <Animated.View style={animatedStyle} />;
};
```

### 4. Animation with Callback

```jsx
import { scheduleOnRN } from 'react-native-worklets';

const AnimatedButton = () => {
  const scale = useSharedValue(1);

  const onComplete = () => {
    console.log('Animation finished!');
  };

  const handlePress = () => {
    scale.value = withTiming(
      1.2,
      { duration: 200 },
      (finished) => {
        if (finished) {
          scheduleOnRN(onComplete);
        }
      }
    );
  };

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }));

  return (
    <Pressable onPress={handlePress}>
      <Animated.View style={[styles.button, animatedStyle]}>
        <Text>Press Me</Text>
      </Animated.View>
    </Pressable>
  );
};
```

## When to Use What

| Thread | Best For |
|--------|----------|
| **UI Thread** (worklets) | Visual animations, transforms, gestures |
| **JS Thread** | State updates, data processing, API calls |

| Hook/API | Use Case |
|----------|----------|
| `useAnimatedStyle` | Animated styles (auto UI thread) |
| `scheduleOnUI` | Manual UI thread execution (from `react-native-worklets`) |
| `scheduleOnRN` | Call JS functions from worklets (from `react-native-worklets`) |
| `useTransition` | Alternative for React state-driven delays |

## Common Pitfalls

- **Accessing React state in worklets**: Use `useSharedValue` instead of `useState` for animated values
- **Not using Animated components**: Must use `Animated.View`, `Animated.Text`, etc.
- **Heavy computation in useAnimatedStyle**: Keep worklets fast
- **Forgetting 'worklet' directive**: Required for inline worklet functions

```jsx
// BAD: Regular function in useAnimatedStyle
const style = useAnimatedStyle(() => {
  heavyComputation();  // Blocks UI thread!
  return { opacity: 1 };
});

// GOOD: Keep worklets fast
const style = useAnimatedStyle(() => {
  return { opacity: opacity.value };  // Just read value
});
```

## Migrating from Reanimated 3.x to 4.x

If you're upgrading from Reanimated 3.x, here are the key changes.

> **Can't upgrade to v4?** If your project is blocked from migrating to New Architecture (e.g., incompatible native libraries, complex native code, or timeline constraints), keep using existing APIs and leverage native drivers where applicable. Avoid introducing legacy Reanimated 3.x or older to reduce future migration complexity.

### Breaking Changes

| Old API (v3) | New API (v4) | Package |
|--------------|--------------|---------|
| `runOnUI(() => {...})()` | `scheduleOnUI(() => {...})` | `react-native-worklets` |
| `runOnJS(fn)(args)` | `scheduleOnRN(fn, args)` | `react-native-worklets` |
| `executeOnUIRuntimeSync` | `runOnUISync` | `react-native-worklets` |
| `runOnRuntime` | `scheduleOnRuntime` | `react-native-worklets` |
| `useScrollViewOffset` | `useScrollOffset` | `react-native-reanimated` |
| `useWorkletCallback` | Use `useCallback` with `'worklet';` directive | React |

### Removed APIs

- `useAnimatedGestureHandler` - Migrate to the Gesture API from `react-native-gesture-handler` v2+
- `addWhitelistedNativeProps` / `addWhitelistedUIProps` - No longer needed
- `combineTransition` - Use `EntryExitTransition.entering(...).exiting(...)` instead

### withSpring Changes

```jsx
// Before (v3)
withSpring(value, {
  restDisplacementThreshold: 0.01,
  restSpeedThreshold: 0.01,
  duration: 300,
});

// After (v4)
withSpring(value, {
  energyThreshold: 0.01,  // Replaces both threshold parameters
  duration: 200,          // Duration is now "perceptual" (~1.5x actual time)
});
```

### Migration Checklist

1. **Enable New Architecture** - Reanimated 4 only supports Fabric + TurboModules
2. **Install `react-native-worklets`** - Required new dependency
3. **Update Babel plugin** - Change `'react-native-reanimated/plugin'` to `'react-native-worklets/plugin'`
4. **Update imports** - Move worklet functions to `react-native-worklets`
5. **Update API calls** - New functions take callback + args directly (not curried)
6. **Rebuild native apps** - Required after adding `react-native-worklets`

## Related Skills

- [js-measure-fps.md](./js-measure-fps.md) - Verify animation frame rate
- [js-bottomsheet.md](./js-bottomsheet.md) - Keep bottom sheet visual state on the UI thread
- [js-concurrent-react.md](./js-concurrent-react.md) - React-level deferral with useTransition
```

## File: `skills/react-native-best-practices/references/js-atomic-state.md`
```markdown
---
title: Atomic State Management
impact: HIGH
tags: state, jotai, zustand, re-renders, context
---

# Skill: Atomic State Management

Use atomic state libraries (Jotai, Zustand) to reduce unnecessary re-renders without manual memoization.

## Quick Pattern

**Before (Context - all consumers re-render):**

```jsx
const { filter, todos } = useContext(TodoContext);
// Re-renders when ANY state changes
```

**After (Zustand - only subscribed state):**

```jsx
const filter = useTodoStore((s) => s.filter);
// Only re-renders when filter changes
```

## When to Use

- Global state changes cause widespread re-renders
- Using React Context for app state
- Components re-render even when their data hasn't changed
- Want to avoid manual `useMemo`/`useCallback` everywhere
- Not ready to adopt React Compiler

## Prerequisites

- State management library: `jotai` or `zustand`

```bash
npm install jotai
# or
npm install zustand
```

## Problem Description

With traditional React state or Context:

```jsx
// When filter OR todos change, EVERYTHING re-renders
const App = () => {
  const [filter, setFilter] = useState('all');
  const [todos, setTodos] = useState([]);
  
  return (
    <>
      <FilterMenu filter={filter} setFilter={setFilter} />
      <TodoList todos={todos} filter={filter} setTodos={setTodos} />
    </>
  );
};
```

Changing a todo re-renders FilterMenu even though it doesn't use todos.

## Step-by-Step Instructions

### Using Jotai

#### 1. Define Atoms

```jsx
import { atom } from 'jotai';

// Each atom is an independent piece of state
const filterAtom = atom('all');
const todosAtom = atom([]);

// Derived atom (computed value)
const filteredTodosAtom = atom((get) => {
  const filter = get(filterAtom);
  const todos = get(todosAtom);
  
  if (filter === 'active') return todos.filter(t => !t.completed);
  if (filter === 'completed') return todos.filter(t => t.completed);
  return todos;
});
```

#### 2. Use Atoms in Components

```jsx
import { useAtom, useAtomValue, useSetAtom } from 'jotai';

// Only re-renders when filterAtom changes
const FilterMenu = () => {
  const [filter, setFilter] = useAtom(filterAtom);
  
  return (
    <View>
      {['all', 'active', 'completed'].map((f) => (
        <Pressable key={f} onPress={() => setFilter(f)}>
          <Text style={filter === f ? styles.active : null}>{f}</Text>
        </Pressable>
      ))}
    </View>
  );
};

// Only re-renders when todosAtom changes
const TodoItem = ({ id }) => {
  const setTodos = useSetAtom(todosAtom);  // Only setter, no re-render on read
  
  const toggleTodo = () => {
    setTodos((prev) => 
      prev.map((t) => t.id === id ? { ...t, completed: !t.completed } : t)
    );
  };
  
  return <Pressable onPress={toggleTodo}>...</Pressable>;
};
```

### Using Zustand

#### 1. Create Store

```jsx
import { create } from 'zustand';

const useTodoStore = create((set, get) => ({
  filter: 'all',
  todos: [],
  
  setFilter: (filter) => set({ filter }),
  
  toggleTodo: (id) => set((state) => ({
    todos: state.todos.map((t) =>
      t.id === id ? { ...t, completed: !t.completed } : t
    ),
  })),
  
  // Selector for derived state
  getFilteredTodos: () => {
    const { filter, todos } = get();
    if (filter === 'active') return todos.filter(t => !t.completed);
    if (filter === 'completed') return todos.filter(t => t.completed);
    return todos;
  },
}));
```

#### 2. Use Selectors

```jsx
// Only re-renders when filter changes
const FilterMenu = () => {
  const filter = useTodoStore((state) => state.filter);
  const setFilter = useTodoStore((state) => state.setFilter);
  
  return (
    <View>
      {['all', 'active', 'completed'].map((f) => (
        <Pressable key={f} onPress={() => setFilter(f)}>
          <Text>{f}</Text>
        </Pressable>
      ))}
    </View>
  );
};

// Only re-renders when todos change
const TodoList = () => {
  const todos = useTodoStore((state) => state.todos);
  return todos.map((todo) => <TodoItem key={todo.id} {...todo} />);
};
```

## Code Examples

### Before: Context-Based (Many Re-renders)

```jsx
const TodoContext = createContext();

const TodoProvider = ({ children }) => {
  const [state, setState] = useState({ filter: 'all', todos: [] });
  return (
    <TodoContext.Provider value={{ state, setState }}>
      {children}
    </TodoContext.Provider>
  );
};

// Every component using this context re-renders on ANY state change
const FilterMenu = () => {
  const { state, setState } = useContext(TodoContext);
  // Re-renders when todos change too!
};
```

### After: Atomic (Targeted Re-renders)

```jsx
// Jotai version - only affected components re-render
const filterAtom = atom('all');
const todosAtom = atom([]);

const FilterMenu = () => {
  const [filter, setFilter] = useAtom(filterAtom);
  // Only re-renders when filter changes
};

const TodoList = () => {
  const todos = useAtomValue(todosAtom);
  // Only re-renders when todos change
};
```

## Comparison

| Feature | Context | Jotai | Zustand |
|---------|---------|-------|---------|
| Re-render scope | All consumers | Atom subscribers | Selector subscribers |
| Derived state | Manual | Built-in atoms | Selectors |
| DevTools | React DevTools | Jotai DevTools | Zustand DevTools |
| Bundle size | 0 KB | ~3 KB | ~2 KB |
| Learning curve | Low | Medium | Low |

## When to Use Which

- **Jotai**: Fine-grained state, many small atoms, derived/async atoms
- **Zustand**: Simpler mental model, single store, familiar Redux-like pattern
- **React Compiler**: If available, may eliminate need for these libraries

## Common Pitfalls

- **Over-atomizing**: Don't create an atom for every variable. Group related state.
- **Missing selectors in Zustand**: Always use selectors to prevent unnecessary re-renders.
- **Derived state without memoization**: Use derived atoms (Jotai) or memoized selectors.

## Related Skills

- [js-bottomsheet.md](./js-bottomsheet.md) - Avoid context-driven bottom sheet subtree re-renders
- [js-react-compiler.md](./js-react-compiler.md) - Automatic memoization alternative
- [js-profile-react.md](./js-profile-react.md) - Verify re-render reduction
```

## File: `skills/react-native-best-practices/references/js-bottomsheet.md`
```markdown
---
title: Bottom Sheet
impact: HIGH
tags: bottom-sheet, gorhom, re-renders, shared-values, gestures, context, scrollable, modal, keyboard
---

# Skill: Bottom Sheet Best Practices

Optimize `@gorhom/bottom-sheet` for smooth 60 FPS by keeping gesture/scroll-driven state on the UI thread.

## Quick Pattern

**Incorrect (can re-enter JS repeatedly during interaction — full subtree re-render):**

```jsx
const handleAnimate = useCallback((fromIndex, toIndex) => {
  setIsExpanded(toIndex > 0); // re-renders entire tree
}, []);

<BottomSheet onAnimate={handleAnimate}>
  <ExpensiveContent isExpanded={isExpanded} />
</BottomSheet>
```

**Correct (stays on UI thread — zero re-renders):**

```jsx
const animatedIndex = useSharedValue(0);

const overlayStyle = useAnimatedStyle(() => ({
  opacity: withTiming(animatedIndex.value > 0 ? 0.5 : 0),
}));

<BottomSheet animatedIndex={animatedIndex}>
  <ExpensiveContent />
</BottomSheet>
<Animated.View style={[styles.overlay, overlayStyle]} />
```

## When to Use

- Implementing or optimizing a bottom sheet with `@gorhom/bottom-sheet`
- Bottom sheet gestures cause jank or dropped frames
- Scroll inside bottom sheet triggers excessive re-renders
- Context provider wrapping bottom sheet re-renders the entire subtree
- Visual-only state (shadow, opacity, footer visibility) managed with `useState`
- Need to choose between `BottomSheet` and `BottomSheetModal`
- Scrollable content inside bottom sheet doesn't coordinate with gestures
- Keyboard doesn't interact properly with the sheet

## Prerequisites

- Check the official [`@gorhom/bottom-sheet` versioning / compatibility table](https://github.com/gorhom/react-native-bottom-sheet#versioning) first.
- If your app is on `@gorhom/bottom-sheet` below v5, upgrade to v5 before applying the patterns in this skill.
- `@gorhom/bottom-sheet` v5 is the current maintained line and is built for `react-native-reanimated` v3.
- `react-native-reanimated` v4 may work in some apps, but the bottom-sheet docs do not officially guarantee it. Decide explicitly whether to stay on v3 or try v4 and validate thoroughly on device.
- `react-native-gesture-handler` v2+

```bash
npm install @gorhom/bottom-sheet@^5 react-native-reanimated@^3 react-native-gesture-handler
```

> **Note**: In v5, `enableDynamicSizing` defaults to `true`. If you need fixed snap-point indexing or do not want the library to insert a dynamic snap point based on content height, set `enableDynamicSizing={false}` explicitly.

## Problem Description

Bottom-sheet gesture, animation, and scroll callbacks that update React state can re-render the sheet subtree during interaction. In practice, callbacks like `onAnimate` may run repeatedly as the sheet retargets animations, which can cause visible jank if they drive expensive React updates.

## Step-by-Step Instructions

### 1. Convert Gesture-Driven State to SharedValue

Avoid React state for gesture-driven visual state. Update a shared value and consume it via `useAnimatedStyle`.

**Before:**

```jsx
const [shadowOpacity, setShadowOpacity] = useState(0);

const handleAnimate = useCallback((fromIndex, toIndex) => {
  setShadowOpacity(toIndex > 0 ? 0.3 : 0);
}, []);

<BottomSheet onAnimate={handleAnimate}>
  <View style={{ shadowOpacity }}>
    <HeavyContent />
  </View>
</BottomSheet>
```

**After:**

```jsx
const animatedIndex = useSharedValue(0);

const shadowStyle = useAnimatedStyle(() => ({
  shadowOpacity: withTiming(animatedIndex.value > 0 ? 0.3 : 0),
}));

<BottomSheet animatedIndex={animatedIndex}>
  <Animated.View style={shadowStyle}>
    <HeavyContent />
  </Animated.View>
</BottomSheet>
```

### 2. Drive Sheet-Index Visibility via `useAnimatedReaction`

Toggling content based on sheet index via `{showFooter && <Footer/>}` causes mount/unmount cycles on every snap. Instead, always mount, animate visibility from `animatedIndex`, and bridge only the minimal boolean needed for `pointerEvents`/accessibility — scoped to a wrapper so the full tree doesn't re-render.

**Before:**

```jsx
const [showFooter, setShowFooter] = useState(false);

// re-mounts footer on every toggle
{showFooter && <Footer />}
```

**After:**

```jsx
const SheetVisibilityWrapper = ({ animatedIndex, threshold = 1, children }) => {
  const [isInteractive, setIsInteractive] = useState(false);

  const style = useAnimatedStyle(() => ({
    opacity: withTiming(animatedIndex.value >= threshold ? 1 : 0),
    transform: [{ translateY: withTiming(animatedIndex.value >= threshold ? 0 : 50) }],
  }));

  useAnimatedReaction(
    () => animatedIndex.value >= threshold,
    (visible, prev) => {
      if (visible !== prev) runOnJS(setIsInteractive)(visible);
    }
  );

  return (
    <Animated.View
      style={style}
      pointerEvents={isInteractive ? 'auto' : 'none'}
      accessibilityElementsHidden={!isInteractive}
      importantForAccessibility={isInteractive ? 'auto' : 'no-hide-descendants'}
    >
      {children}
    </Animated.View>
  );
};

// Usage:
<SheetVisibilityWrapper animatedIndex={animatedIndex}>
  <Footer />
</SheetVisibilityWrapper>
```

### 3. Keep Scroll-Driven Logic off the JS Thread

`BottomSheetScrollView` ignores `scrollEventThrottle`, so setting it is not an optimization. Keep JS `onScroll` work minimal, or move scroll-driven logic to `useAnimatedScrollHandler` (see [js-animations-reanimated.md](./js-animations-reanimated.md)) so it stays on the UI thread:

```jsx
const scrollHandler = useAnimatedScrollHandler((event) => {
  scrollY.value = event.contentOffset.y;
});

<BottomSheetScrollView onScroll={scrollHandler}>
  <Content />
</BottomSheetScrollView>
```

### 4. Use Library-Provided Components and Props

**Scrollables** — always use these instead of React Native built-ins inside a bottom sheet:

```jsx
import {
  BottomSheetScrollView,
  BottomSheetFlatList,
  BottomSheetSectionList,
} from '@gorhom/bottom-sheet';

// FlashList v2: BottomSheetFlashList is deprecated.
// Create the scroll component, then pass it to FlashList.
import { useBottomSheetScrollableCreator } from '@gorhom/bottom-sheet';
import { FlashList } from '@shopify/flash-list';

const BottomSheetFlashListScrollComponent = useBottomSheetScrollableCreator();

<BottomSheet snapPoints={snapPoints} enableDynamicSizing={false}>
  <FlashList
    data={data}
    keyExtractor={(item) => item.id}
    renderItem={renderItem}
    renderScrollComponent={BottomSheetFlashListScrollComponent}
  />
</BottomSheet>
```

**Key props:**

| Prop | Purpose |
|------|---------|
| `containerHeight` | Provide to skip extra measurement re-render on mount |
| `enableDynamicSizing={false}` | Use when you want fixed snap-point indexing and do not want a dynamic content-height snap point inserted |
| `animatedIndex` | SharedValue for continuous index tracking on UI thread |
| `animatedPosition` | SharedValue for continuous position tracking on UI thread |
| `onChange` | Fires on snap **completion** only (discrete) — use for analytics/side effects |
| `onAnimate` | Fires before each animation start/retarget — use sparingly, because it can run repeatedly during interaction |

### 5. BottomSheetModal Setup

```jsx
import {
  BottomSheetModal,
  BottomSheetModalProvider,
} from '@gorhom/bottom-sheet';

const App = () => (
  <BottomSheetModalProvider>
    <BottomSheetModal
      ref={modalRef}
      snapPoints={snapPoints}
      enableDismissOnClose={true}
    >
      <Content />
    </BottomSheetModal>
  </BottomSheetModalProvider>
);
```

**iOS layering fix** — use `FullWindowOverlay` to render above native navigation:

```jsx
import { FullWindowOverlay } from 'react-native-screens';

<BottomSheetModal
  containerComponent={(props) => <FullWindowOverlay>{props.children}</FullWindowOverlay>}
>
```

### 6. Keyboard Handling

```jsx
<BottomSheet
  snapPoints={snapPoints}
  enableDynamicSizing={false}
  keyboardBehavior="interactive"    // 'extend' | 'fillParent' | 'interactive'
  keyboardBlurBehavior="restore"    // reset sheet position when keyboard dismisses
  enableBlurKeyboardOnGesture={true} // dismiss keyboard on drag
>
  <BottomSheetTextInput
    placeholder="Type here..."
    style={styles.input}
  />
</BottomSheet>
```

| `keyboardBehavior` | Effect |
|--------------------|--------|
| `extend` | Sheet grows to accommodate keyboard |
| `fillParent` | Sheet fills parent when keyboard appears |
| `interactive` | Sheet follows keyboard position interactively |

> Prefer `BottomSheetTextInput` inside a bottom sheet. If you need a custom input, copy the focus/blur handlers from the library's `BottomSheetTextInput` implementation so keyboard handling still works correctly.

## Derived Animations with `animatedPosition`

Use the `animatedPosition` shared value for smooth derived UI that stays on the UI thread:

```jsx
const animatedPosition = useSharedValue(0);

const backdropStyle = useAnimatedStyle(() => ({
  opacity: interpolate(
    animatedPosition.value,
    [0, 300],
    [0.5, 0],
    Extrapolation.CLAMP
  ),
}));

<BottomSheet animatedPosition={animatedPosition} snapPoints={snapPoints}>
  <Content />
</BottomSheet>
<Animated.View style={[StyleSheet.absoluteFill, backdropStyle]} pointerEvents="none" />
```

## Native Alternative: react-native-true-sheet

If your app already runs on **New Architecture (Fabric)**, consider `@lodev09/react-native-true-sheet` — a fully native bottom sheet that sidesteps JS re-render problems entirely.

| Scenario | Recommendation |
|----------|---------------|
| Need deep JS customization (custom gestures, animated derived UI) | `@gorhom/bottom-sheet` |
| Standard sheet with native feel + accessibility | `react-native-true-sheet` |
| Legacy Architecture (no Fabric) | `@gorhom/bottom-sheet` (true-sheet v3+ requires Fabric) |
| Web support needed | Either (true-sheet uses `@gorhom/bottom-sheet` on web internally) |

**Advantages**: zero JS overhead (sheet lives in native land — no SharedValue plumbing needed), built-in keyboard handling, native screen reader support, side sheet on tablets, iOS 26+ Liquid Glass support, React Navigation sheet navigator integration.

**Requirements**: New Architecture (Fabric) for v3+, use v2.x for Legacy Architecture.

```bash
npm install @lodev09/react-native-true-sheet
```

> If requirements are met and you don't need the fine-grained Reanimated-driven customization described in this skill, `react-native-true-sheet` is the simpler and more performant choice.

## Common Pitfalls

- **Using `onChange` for continuous position tracking** — it fires on snap completion only (discrete). Use `animatedPosition` or `animatedIndex` shared values instead.
- **Forgetting `pointerEvents='none'` on always-mounted hidden elements** — invisible elements still capture touches.
- **Missing accessibility attributes on hidden elements** — add `accessibilityElementsHidden` and `importantForAccessibility='no-hide-descendants'`.
- **Bundling independent state values in one context** — see [js-atomic-state.md](./js-atomic-state.md) for splitting patterns.
- **Assuming `enableDynamicSizing` must be disabled whenever you pass `snapPoints`** — it does not have to be, but leaving it enabled can insert an additional snap point and change indexing.
- **Using React Native `ScrollView`/`FlatList` inside bottom sheet** — gestures won't coordinate. Use `BottomSheetScrollView`, `BottomSheetFlatList`, etc.
- **Using React Native touchables on Android** — import `TouchableOpacity`, `TouchableHighlight`, or `TouchableWithoutFeedback` from `@gorhom/bottom-sheet`.
- **Not providing `containerHeight`** — causes an extra re-render on mount for measurement.
- **Using a custom `TextInput` without porting the library's focus/blur handlers** — keyboard handling will be incomplete. Prefer `BottomSheetTextInput` unless you need a custom input.

## Related Skills

- [js-animations-reanimated.md](./js-animations-reanimated.md) — SharedValue and useAnimatedStyle fundamentals
- [js-atomic-state.md](./js-atomic-state.md) — Context splitting and atomic state patterns
- [js-profile-react.md](./js-profile-react.md) — Profiling to measure re-render reduction
- [js-measure-fps.md](./js-measure-fps.md) — Verify FPS improvement after optimization
```

## File: `skills/react-native-best-practices/references/js-concurrent-react.md`
```markdown
---
title: Concurrent React
impact: HIGH
tags: useDeferredValue, useTransition, suspense, concurrent
---

# Skill: Concurrent React

Use `useDeferredValue` and `useTransition` to improve perceived performance by prioritizing critical updates.

## Quick Pattern

**Incorrect (blocks input on every keystroke):**

```jsx
const [query, setQuery] = useState('');
<TextInput value={query} onChangeText={setQuery} />
<ExpensiveList query={query} />  // Blocks typing
```

**Correct (input stays responsive):**

```jsx
const [query, setQuery] = useState('');
const deferredQuery = useDeferredValue(query);
<TextInput value={query} onChangeText={setQuery} />
<ExpensiveList query={deferredQuery} />  // Deferred update
```

## When to Use

- Search/filter inputs feel laggy with large result sets
- Expensive computations block UI interactions
- Loading states appear too frequently
- Want to show stale content while loading new content
- Need to prioritize user input over background updates

## Prerequisites

- React Native with New Architecture enabled (default in RN 0.76+)
- React 18+ features (`useDeferredValue`, `useTransition`, `Suspense`)

## Concept Overview

**Concurrent React** allows updates to be:
- **Paused**: Low-priority work can wait
- **Interrupted**: User input takes priority
- **Abandoned**: Outdated updates can be skipped

## Step-by-Step Instructions

### Pattern 1: Defer Expensive Rendering with `useDeferredValue`

Use when a value drives expensive computation but you want input to stay responsive.

```jsx
import { useState, useDeferredValue } from 'react';

const SearchScreen = () => {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  
  // query updates immediately (input stays responsive)
  // deferredQuery updates when React has time
  
  return (
    <View>
      <TextInput
        value={query}
        onChangeText={setQuery}
        placeholder="Search..."
      />
      {/* ExpensiveList receives deferred value */}
      <ExpensiveList query={deferredQuery} />
    </View>
  );
};
```

### Pattern 2: Show Stale Content While Loading

```jsx
const SearchWithStaleIndicator = () => {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;
  
  return (
    <View>
      <TextInput value={query} onChangeText={setQuery} />
      <View style={isStale && { opacity: 0.7 }}>
        <SearchResults query={deferredQuery} />
      </View>
      {isStale && <ActivityIndicator />}
    </View>
  );
};
```

### Pattern 3: Transition Non-Critical Updates with `useTransition`

Use when you have multiple state updates and want to mark some as low-priority.

```jsx
import { useState, useTransition } from 'react';

const TransitionExample = () => {
  const [count, setCount] = useState(0);
  const [heavyData, setHeavyData] = useState(null);
  const [isPending, startTransition] = useTransition();
  
  const handleIncrement = () => {
    // High priority - updates immediately
    setCount(c => c + 1);
    
    // Low priority - can be interrupted
    startTransition(() => {
      setHeavyData(computeExpensiveData());
    });
  };
  
  return (
    <View>
      <Text>Count: {count}</Text>
      {isPending ? <ActivityIndicator /> : <HeavyComponent data={heavyData} />}
      <Button onPress={handleIncrement} title="Increment" />
    </View>
  );
};
```

### Pattern 4: Suspense for Data Fetching

```jsx
import { Suspense, useDeferredValue } from 'react';

const DataScreen = () => {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  
  return (
    <View>
      <TextInput value={query} onChangeText={setQuery} />
      <Suspense fallback={<LoadingSpinner />}>
        <SearchResults query={deferredQuery} />
      </Suspense>
    </View>
  );
};
```

## Code Examples

### Slow Component Optimization

```jsx
// Without Concurrent React - UI freezes
const SlowSearch = () => {
  const [query, setQuery] = useState('');
  
  return (
    <>
      <TextInput value={query} onChangeText={setQuery} />
      <SlowComponent query={query} /> {/* Blocks every keystroke */}
    </>
  );
};

// With Concurrent React - UI stays responsive  
const FastSearch = () => {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  
  return (
    <>
      <TextInput value={query} onChangeText={setQuery} />
      <SlowComponent query={deferredQuery} />
    </>
  );
};

// Important: Wrap SlowComponent in memo to prevent re-renders from parent
const SlowComponent = memo(({ query }) => {
  // Expensive computation here
});
```

### Automatic Batching (React 18+)

React 18 automatically batches state updates:

```jsx
// Before React 18 - 2 re-renders
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // Rendered twice
}, 1000);

// React 18+ - 1 re-render (automatic batching)
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // Rendered once!
}, 1000);
```

## When to Use Which

| Scenario | Solution |
|----------|----------|
| Single value drives expensive render | `useDeferredValue` |
| Multiple state updates, some non-critical | `useTransition` |
| Need loading indicator for transition | `useTransition` (has `isPending`) |
| Data fetching with loading states | `Suspense` + `useDeferredValue` |
| Simple parent-to-child value deferral | `useDeferredValue` |

## Important Considerations

1. **Wrap expensive components in `memo()`**: Without memoization, the component re-renders from parent anyway.

2. **Use with New Architecture**: Concurrent features require New Architecture in React Native.

3. **Don't overuse**: Only defer truly expensive work. Adding complexity for fast components is counterproductive.

## Common Pitfalls

- **Forgetting memo()**: `useDeferredValue` is useless if child re-renders from parent
- **Using for simple state**: Overhead isn't worth it for cheap updates
- **Expecting faster computation**: These hooks don't make code faster, they prioritize what runs when

## Related Skills

- [js-profile-react.md](./js-profile-react.md) - Identify slow components
- [js-react-compiler.md](./js-react-compiler.md) - Automatic memoization
- [js-lists-flatlist-flashlist.md](./js-lists-flatlist-flashlist.md) - For list-specific optimizations
```

## File: `skills/react-native-best-practices/references/js-lists-flatlist-flashlist.md`
```markdown
---
title: Higher-Order Lists
impact: CRITICAL
tags: lists, flatlist, flashlist, scrollview, virtualization
---

# Skill: Higher-Order Lists

Replace ScrollView with FlatList or FlashList for performant large list rendering.

## Quick Pattern

**Incorrect:**

```jsx
<ScrollView>
  {items.map((item) => <Item key={item.id} {...item} />)}
</ScrollView>
```

**Correct:**

```jsx
<FlashList
  data={items}
  keyExtractor={(item) => item.id}
  renderItem={({ item }) => <Item {...item} />}
  estimatedItemSize={50}
/>
```

## When to Use

- Rendering more than 10-20 items in a list
- List scrolling is choppy or laggy
- App freezes when loading list data
- Memory usage spikes with long lists

## Prerequisites

- `@shopify/flash-list` for FlashList (recommended)
- Understanding of list virtualization

## Step-by-Step Instructions

### 1. Identify the Problem

![FPS Drop Graph](images/fps-drop-graph.png)

The FPS graph shows a severe performance problem during list rendering:
- FPS starts at ~60 (smooth)
- Drops to ~3 FPS during heavy list operation
- Recovers after rendering completes

```jsx
// BAD: ScrollView renders ALL items at once
const BadList = ({ items }) => (
  <ScrollView>
    {items.map((item, index) => (
      <View key={index}>
        <Text>{item}</Text>
      </View>
    ))}
  </ScrollView>
);
```

With 5000 items, this creates 5000 views immediately, causing:
- Multi-second freeze
- FPS drop to 0
- High memory usage

### 2. Replace with FlatList

```jsx
import { FlatList } from 'react-native';

const BetterList = ({ items }) => {
  const renderItem = ({ item }) => (
    <View>
      <Text>{item}</Text>
    </View>
  );
  
  return (
    <FlatList
      data={items}
      renderItem={renderItem}
      keyExtractor={(item, index) => index.toString()}
    />
  );
};
```

FlatList only renders visible items + buffer (windowing).

### 3. Optimize FlatList with getItemLayout

For fixed-height items, skip layout measurement:

```jsx
const ITEM_HEIGHT = 50;

const OptimizedList = ({ items }) => {
  const renderItem = ({ item }) => (
    <View style={{ height: ITEM_HEIGHT }}>
      <Text>{item}</Text>
    </View>
  );
  
  const getItemLayout = (_, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  });
  
  return (
    <FlatList
      data={items}
      renderItem={renderItem}
      keyExtractor={(item, index) => index.toString()}
      getItemLayout={getItemLayout}
    />
  );
};
```

### 4. Upgrade to FlashList (Best Performance)

```bash
npm install @shopify/flash-list
```

```jsx
import { FlashList } from '@shopify/flash-list';

const BestList = ({ items }) => {
  const renderItem = ({ item }) => (
    <View style={{ height: 50 }}>
      <Text>{item}</Text>
    </View>
  );
  
  return (
    <FlashList
      data={items}
      renderItem={renderItem}
      estimatedItemSize={50}  // Required for FlashList
    />
  );
};
```

**FlashList advantages:**
- Recycles views instead of creating new ones
- 78/100 vs 25/100 performance score in benchmarks
- Smoother scrolling at ~54 FPS vs lower for FlatList

## Code Examples

### Variable Height Items

```jsx
// Calculate average for estimatedItemSize
// Items are 50px, 100px, 150px
// Average: (50 + 100 + 150) / 3 = 100px

<FlashList
  data={items}
  renderItem={renderItem}
  estimatedItemSize={100}
/>
```

### Mixed Item Types

```jsx
<FlashList
  data={items}
  renderItem={({ item }) => {
    if (item.type === 'header') return <Header {...item} />;
    if (item.type === 'product') return <Product {...item} />;
    return <DefaultItem {...item} />;
  }}
  getItemType={(item) => item.type}  // Helps recycling
  estimatedItemSize={80}
/>
```

### FlatList Optimizations (if not using FlashList)

```jsx
<FlatList
  data={items}
  renderItem={renderItem}
  // Performance props
  removeClippedSubviews={true}
  maxToRenderPerBatch={10}
  updateCellsBatchingPeriod={50}
  initialNumToRender={10}
  windowSize={5}
  // Avoid re-renders
  keyExtractor={(item) => item.id}
  extraData={selectedId}  // Only when selection changes
/>
```

## Performance Comparison

| Component | 5000 Items Load | Scroll FPS | Memory |
|-----------|-----------------|------------|--------|
| ScrollView | 1-3 seconds freeze | < 30 | High |
| FlatList | ~100ms | ~45 | Medium |
| FlashList | ~50ms | ~54 | Low |

## Decision Matrix

| Scenario | Recommendation |
|----------|---------------|
| < 20 static items | ScrollView OK |
| 20-100 items | FlatList minimum |
| > 100 items | FlashList |
| Complex item layouts | FlashList with `getItemType` |
| Fixed height items | Add `getItemLayout` or `estimatedItemSize` |

## Common Pitfalls

- **Inline renderItem functions**: Causes re-renders. Define outside or use `useCallback`.
- **Missing keyExtractor**: Use unique IDs, not array index when possible.
- **Ignoring estimatedItemSize warning**: FlashList warns if not set. Always provide it.
- **Heavy item components**: Keep list items light. Move side effects out.

## Related Skills

- [js-profile-react.md](./js-profile-react.md) - Profile list rendering
- [js-measure-fps.md](./js-measure-fps.md) - Measure scroll performance
```

## File: `skills/react-native-best-practices/references/js-measure-fps.md`
```markdown
---
title: Measure JS FPS
impact: HIGH
tags: fps, performance, monitoring, flashlight
---

# Skill: Measure JS FPS

Monitor and measure JavaScript frame rate to quantify app smoothness and identify performance regressions.

## Quick Command

```bash
# Method 1: Built-in Perf Monitor
# Shake device → Dev Menu → "Perf Monitor"

# Method 2: Flashlight (Android, detailed reports)
# Install Flashlight from an official, verified release channel first.
flashlight measure
```

## When to Use

- Animations feel choppy or janky
- Scrolling is not smooth
- Need baseline FPS metrics before/after optimization
- Want to compare performance across builds

## Prerequisites

- React Native app running on device/simulator
- For Flashlight: Android device (iOS not supported)

> **Note**: This skill involves interpreting visual output (FPS graphs, performance overlays). AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing metrics manually, or await MCP-based visual feedback integration (see roadmap).

## Step-by-Step Instructions

### Method 1: React Perf Monitor (Quick Check)

1. Open Dev Menu:
   - iOS Simulator: `Ctrl + Cmd + Z` or Device > Shake
   - Android Emulator: `Cmd + M` (Mac) / `Ctrl + M` (Windows)

2. Select **"Perf Monitor"**

3. Observe the overlay showing:
   - **UI (Main) thread FPS** - Native rendering
   - **JS thread FPS** - JavaScript execution
   - **RAM usage**

4. Hide with "Hide Perf Monitor" from Dev Menu

**Interpretation:**
- **60 FPS** = Smooth (16.6ms per frame)
- **< 60 FPS** = Dropping frames
- **120 FPS** target for high refresh rate devices (8.3ms per frame)

### Method 2: Flashlight (Automated Benchmarking)

> Android only. Provides detailed reports and JSON export.

![Flashlight FlatList vs FlashList Comparison](images/flashlight-flatlist-vs-flashlist.png)

Flashlight shows comparative performance data:
- **Score** (0-100): Overall performance rating (higher is better)
- **Average FPS**: Target 60 FPS for smooth scrolling
- **FPS Graph**: Real-time frame rate over test duration
- **CPU/RAM metrics**: Resource consumption

The image shows FlatList (score: 3) vs FlashList (score: 67) - a dramatic difference visible in both the score and FPS graph.

**Installation:**

Install Flashlight from the vendor's official release channel before using it. Prefer a package manager or a version-pinned binary with checksum/signature verification. Do not pipe a remote install script directly into a shell.

**Usage:**

```bash
# Start measuring (app must be running on Android)
flashlight measure
```

**Features:**
- Real-time FPS graph
- Average FPS calculation
- CPU and RAM metrics
- Overall performance score
- JSON export for CI comparison

### Important: Disable Dev Mode

**Always disable development mode for accurate measurements:**

**Android:**
1. Open Dev Menu
2. Settings > JS Dev Mode → **OFF**

**iOS (React Native CLI):**
```bash
# Run Metro in production mode
npx react-native start --reset-cache
# Then build release variant
```

**Expo:**
```bash
# Start Metro without dev mode
npx expo start --no-dev --minify
# For accurate measurements, use EAS Build for release testing
```

## Code Examples

### Identify FPS Drop Source

If **UI FPS drops but JS FPS is fine:**
- Native rendering issue
- Too many views/complex layouts
- Heavy native animations

If **JS FPS drops but UI FPS is fine:**
- JavaScript computation blocking
- Expensive React re-renders
- Look for `longRunningFunction` patterns

If **Both drop:**
- Mixed issue, start with JS profiling

### Target Frame Budgets

```javascript
// 60 FPS = 16.6ms per frame
const FRAME_BUDGET_60 = 16.6;

// 120 FPS = 8.3ms per frame  
const FRAME_BUDGET_120 = 8.3;

// If your function takes longer, it will drop frames
const longRunningFunction = () => {
  let i = 0;
  while (i < 1000000000) { // This blocks for seconds!
    i++;
  }
};
```

## Interpreting Results

| FPS Range | User Perception | Action |
|-----------|-----------------|--------|
| 55-60 | Smooth | Acceptable |
| 45-55 | Slight stutter | Investigate |
| 30-45 | Noticeable jank | Optimize required |
| < 30 | Very choppy | Critical fix needed |

## Flashlight CI Integration

```bash
# Export measurements to JSON
flashlight measure --output results.json

# Compare builds
flashlight compare baseline.json current.json
```

## Common Pitfalls

- **Measuring in dev mode**: Results will be artificially slow
- **Not using real device**: Simulators don't reflect real performance
- **Ignoring UI thread**: React Native has two threads - JS issues don't always show on UI thread
- **Single measurement**: Run multiple times, FPS varies

## Related Skills

- [js-profile-react.md](./js-profile-react.md) - Find what's causing FPS drops
- [js-animations-reanimated.md](./js-animations-reanimated.md) - Fix animation-related drops
- [js-bottomsheet.md](./js-bottomsheet.md) - Measure bottom sheet gesture and snap performance
- [js-lists-flatlist-flashlist.md](./js-lists-flatlist-flashlist.md) - Fix scroll-related drops
```

## File: `skills/react-native-best-practices/references/js-memory-leaks.md`
```markdown
---
title: Hunt JS Memory Leaks
impact: MEDIUM
tags: memory, leaks, profiling, cleanup
---

# Skill: Hunt JS Memory Leaks

Find and fix JavaScript memory leaks using React Native DevTools memory profiling.

## Quick Pattern

**Incorrect (listener not cleaned up):**

```jsx
useEffect(() => {
  const sub = EventEmitter.addListener('event', handler);
  // Missing cleanup!
}, []);
```

**Correct (proper cleanup):**

```jsx
useEffect(() => {
  const sub = EventEmitter.addListener('event', handler);
  return () => sub.remove();
}, []);
```

## When to Use

- App memory usage grows over time
- App crashes after extended use
- Navigating between screens increases memory
- Suspecting event listeners or timers not cleaned up

## Prerequisites

- React Native DevTools accessible
- App running in development mode

## Step-by-Step Instructions

### 1. Open Memory Profiler

1. Launch React Native DevTools (press `j` in Metro)
2. Go to **Memory** tab
3. Select **"Allocation instrumentation on timeline"**

### 2. Record Memory Allocations

1. Click **"Start"** at the bottom
2. Perform actions that might leak (navigate, trigger events, etc.)
3. Wait 10-30 seconds
4. Click **"Stop"**

### 3. Analyze the Timeline

**Key indicators:**
- **Blue bars** = Memory allocated
- **Gray bars** = Memory freed (garbage collected)
- **Blue bars that stay blue** = Potential leak!

### 4. Investigate Leaking Objects

![Memory Heap Snapshot](images/memory-heap-snapshot.png)

The Memory tab shows:
- **Timeline** (top): Blue bars = allocations, select time range to filter
- **Summary view** (bottom): Lists constructors with allocation counts

**Key columns:**
- **Constructor**: Object type (e.g., `JSObject`, `Function`, `(string)`)
- **Count**: Number of instances (×85000 = 85,000 objects)
- **Shallow Size**: Memory of the object itself
- **Retained Size**: Memory freed if object is deleted (including references)

**Red flag**: Large retained size % with small shallow size % = closures or references holding large objects.

**To investigate:**
1. Click on a blue spike in the timeline
2. Look at the Constructor list below
3. Check **Shallow size** vs **Retained size**
4. Expand constructors to see individual allocations
5. Click to see the exact source location

### 5. Verify the Fix

After fixing, re-profile. All bars should turn gray (except the most recent).

## Code Examples

### Common Leak Patterns

**1. Listeners Not Cleaned Up:**

```jsx
// BAD: Memory leak
const BadEventComponent = () => {
  useEffect(() => {
    const subscription = EventEmitter.addListener('myEvent', handleEvent);
    // Missing cleanup!
  }, []);
  
  return <Text>Listening...</Text>;
};

// GOOD: Proper cleanup
const GoodEventComponent = () => {
  useEffect(() => {
    const subscription = EventEmitter.addListener('myEvent', handleEvent);
    return () => subscription.remove(); // Cleanup!
  }, []);
  
  return <Text>Listening...</Text>;
};
```

**2. Timers Not Cleared:**

```jsx
// BAD: Memory leak
const BadTimerComponent = () => {
  useEffect(() => {
    const timer = setInterval(() => {
      setCount(prev => prev + 1);
    }, 1000);
    // Missing cleanup!
  }, []);
};

// GOOD: Proper cleanup
const GoodTimerComponent = () => {
  useEffect(() => {
    const timer = setInterval(() => {
      setCount(prev => prev + 1);
    }, 1000);
    return () => clearInterval(timer); // Cleanup!
  }, []);
};
```

**3. Closures Capturing Large Objects:**

```jsx
// BAD: Closure captures entire array
class BadClosureExample {
  private largeData = new Array(1000000).fill('data');
  
  createLeakyFunction() {
    return () => this.largeData.length; // Captures this.largeData
  }
}

// GOOD: Only capture what's needed
class GoodClosureExample {
  private largeData = new Array(1000000).fill('data');
  
  createEfficientFunction() {
    const length = this.largeData.length; // Extract value
    return () => length; // Only captures primitive
  }
}
```

**4. Global Arrays Growing:**

```jsx
// BAD: Global array never cleared
let leakyClosures = [];

const createLeak = () => {
  const data = generateLargeData();
  leakyClosures.push(() => data); // Keeps growing!
};

// GOOD: Clear when done or use WeakRef
const createNoLeak = () => {
  const data = generateLargeData();
  const closure = () => data;
  // Use it and let it be garbage collected
  return closure;
};
```

## Memory Profiler Metrics

| Metric | Meaning |
|--------|---------|
| **Shallow size** | Memory held by the object itself |
| **Retained size** | Memory freed if object is deleted (includes references) |

**Large retained size with small shallow size** = Object holding references to other large objects (common in closures).

## Common Pitfalls

- **Not forcing GC**: GC runs periodically. Allocate something else to trigger collection before concluding there's a leak.
- **Ignoring gray bars**: Gray = properly collected. Only blue bars that persist are leaks.
- **Missing useEffect cleanup**: Most common React Native leak source.

## Related Skills

- [native-memory-leaks.md](./native-memory-leaks.md) - Native-side memory leaks
- [js-profile-react.md](./js-profile-react.md) - General profiling
```

## File: `skills/react-native-best-practices/references/js-profile-react.md`
```markdown
---
title: Profile React Performance
impact: MEDIUM
tags: profiling, devtools, re-renders, flamegraph
---

# Skill: Profile React Performance

Identify unnecessary re-renders and performance bottlenecks in React Native apps using React Native DevTools.

## Quick Command

```bash
# Open React Native DevTools (press 'j' in Metro terminal)
# Or shake device → "Open DevTools"
# Go to Profiler tab → Start profiling → Perform actions → Stop
```

## When to Use

- App feels sluggish or janky during interactions
- Need to identify which components re-render unnecessarily
- Investigating slow list scrolling or form inputs
- Before applying memoization or state management changes

## Prerequisites

- React Native DevTools accessible (press `j` in Metro or use Dev Menu)
- App running in development mode
- React DevTools version 6.0.1+ for React Compiler support

> **Note**: This skill involves interpreting visual profiler output (flame graphs, component highlighting). AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing the profiler UI manually, or await MCP-based visual feedback integration (see roadmap).

## Step-by-Step Instructions

### 1. Open React Native DevTools

```bash
# Option A: Press 'j' in Metro terminal (works with both RN CLI and Expo)
# Option B: Shake device / Cmd+D (iOS) / Cmd+M (Android) → "Open DevTools"
# Expo: Also accessible via Expo DevTools in browser
```

### 2. Configure Profiler Settings

1. Go to **Profiler** tab
2. Click gear icon (⚙️) for settings
3. Enable:
   - "Highlight updates when components render"
   - "Record why each component rendered while profiling"

### 3. Record a Profiling Session

```
1. Click "Start profiling" (blue circle) or "Reload and start profiling"
2. Perform the interaction you want to analyze
3. Click "Stop profiling"
```

**Use "Reload and start profiling"** for startup performance analysis.

### 4. Analyze the Flame Graph

![React DevTools Flamegraph](images/devtools-flamegraph.png)

The flame graph shows component render hierarchy with timing:

**Color indicators:**
- **Yellow components**: Most time spent rendering (focus here)
- **Green components**: Fast/memoized
- **Gray components**: Did not render

**Right panel shows "Why did this render?":**
- Props changed (shows which prop, e.g., `children`, `onPress`)
- Rendered at timestamps with duration (e.g., "3.7s for 0.9ms")

**Click on a component to see:**
- Why it rendered (hook change, props change, parent re-render)
- Render duration
- Child components affected

### 5. Use Ranked View for Bottom-Up Analysis

Click "Ranked" tab to see components sorted by render time (slowest first).

### 6. Profile JavaScript CPU

For non-React performance issues:

1. Go to **JavaScript Profiler** tab (enable in settings if hidden)
2. Click "Start" to record
3. Perform actions
4. Click "Stop"
5. Use **Heavy (Bottom Up)** view to find slowest functions

## Code Examples

### Before: Unnecessary Re-renders

```jsx
const App = () => {
  const [count, setCount] = useState(0);
  
  return (
    <View>
      <Text>{count}</Text>
      {/* Button re-renders on every count change */}
      <Button onPress={() => setCount(count + 1)} title="Press" />
    </View>
  );
};

const Button = ({onPress, title}) => (
  <Pressable onPress={onPress}>
    <Text>{title}</Text>
  </Pressable>
);
```

### After: Memoized

```jsx
const App = () => {
  const [count, setCount] = useState(0);
  const onPressHandler = useCallback(() => setCount(c => c + 1), []);
  
  return (
    <View>
      <Text>{count}</Text>
      <Button onPress={onPressHandler} title="Press" />
    </View>
  );
};

const Button = memo(({onPress, title}) => (
  <Pressable onPress={onPress}>
    <Text>{title}</Text>
  </Pressable>
));
```

## Interpreting Results

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Many yellow components | Cascading re-renders | Add memoization or use React Compiler |
| "Props changed" on callbacks | Inline functions recreated | Use `useCallback` |
| "Parent component rendered" | State too high in tree | Move state down or use atomic state |
| Long JS thread block | Heavy computation | Move to background or use `useDeferredValue` |

## Common Pitfalls

- **Profiling in dev mode**: Always disable JS Dev Mode for accurate measurements (Settings > JS Dev Mode on Android)
- **Not using production builds**: Some issues only appear with minified code
- **Ignoring "Why did this render?"**: This tells you exactly what to fix

## Related Skills

- [js-react-compiler.md](./js-react-compiler.md) - Automatic memoization
- [js-atomic-state.md](./js-atomic-state.md) - Reduce re-renders with Jotai/Zustand
- [js-bottomsheet.md](./js-bottomsheet.md) - Profile bottom sheet callback-driven re-renders
- [js-measure-fps.md](./js-measure-fps.md) - Quantify frame rate impact
```

## File: `skills/react-native-best-practices/references/js-react-compiler.md`
```markdown
---
title: React Compiler
impact: HIGH
tags: memoization, react-compiler, memo, useMemo, useCallback
---

# Skill: React Compiler

Set up React Compiler to automatically memoize components and eliminate unnecessary re-renders.

## Quick Pattern

**Before (manual memoization):**

```jsx
const MemoizedButton = memo(({ onPress }) => <Pressable onPress={onPress} />);
const handler = useCallback(() => doSomething(), []);
```

**After (automatic with React Compiler):**

```jsx
// No memo/useCallback needed - compiler handles it
const Button = ({ onPress }) => <Pressable onPress={onPress} />;
const handler = () => doSomething();
```

## When to Use

- Want automatic performance optimization without manual `memo`/`useMemo`/`useCallback`
- Codebase follows Rules of React
- React Native 0.76+ or Expo SDK 52+
- Ready to remove boilerplate memoization code

## Prerequisites

- React 17+ (React 19 recommended for best compatibility)
- Babel-based build system
- Code follows [Rules of React](https://react.dev/reference/rules)

## Step-by-Step Instructions

### Step 1: Check Compatibility

Before enabling the compiler, verify your project is compatible:

```bash
npx react-compiler-healthcheck@latest
```

This checks if your app follows the Rules of React and identifies potential issues.

### Step 2: Install React Compiler

#### Expo Projects

**SDK 54 and later** (simplified setup):

```bash
npx expo install babel-plugin-react-compiler
```

**SDK 52-53**:

```bash
npx expo install babel-plugin-react-compiler@beta react-compiler-runtime@beta
```

Then enable in your app config:

```json
// app.json
{
  "expo": {
    "experiments": {
      "reactCompiler": true
    }
  }
}
```

#### React Native (without Expo)

```bash
npm install -D babel-plugin-react-compiler@latest
```

For React Native < 0.78 (React < 19), also install the runtime:

```bash
npm install react-compiler-runtime@beta
```

### Step 3: Configure Babel (React Native without Expo)

For non-Expo React Native projects, configure Babel manually:

```javascript
// babel.config.js
const ReactCompilerConfig = {
  target: '19', // Use '18' for React Native < 0.78
};

module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['module:@react-native/babel-preset'],
    plugins: [
      ['babel-plugin-react-compiler', ReactCompilerConfig], // Must run first!
      // ... other plugins
    ],
  };
};
```

> **Important**: React Compiler must run **first** in your Babel plugin pipeline. The compiler needs the original source information for proper analysis.

### Step 4: Set Up ESLint (Recommended)

The ESLint plugin helps identify code that can't be optimized and enforces the Rules of React.

#### Expo Projects

```bash
npx expo lint  # Ensures ESLint is set up
npx expo install eslint-plugin-react-compiler -- -D
```

Configure ESLint:

```javascript
// .eslintrc.js
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');
const reactCompiler = require('eslint-plugin-react-compiler');

module.exports = defineConfig([
  expoConfig,
  reactCompiler.configs.recommended,
  {
    ignores: ['dist/*'],
  },
]);
```

#### React Native (without Expo)

```bash
npm install -D eslint-plugin-react-hooks@latest
```

The compiler rules are available in the `recommended-latest` preset. Follow the [eslint-plugin-react-hooks installation instructions](https://github.com/facebook/react/tree/main/packages/eslint-plugin-react-hooks).

### Step 5: Verify Optimizations

Open React DevTools. Optimized components show a `Memo ✨` badge.

You can also verify by checking build output—compiled code includes automatic memoization:

```javascript
import { c as _c } from 'react/compiler-runtime';

export default function MyApp() {
  const $ = _c(1);
  let t0;
  if ($[0] === Symbol.for('react.memo_cache_sentinel')) {
    t0 = <div>Hello World</div>;
    $[0] = t0;
  } else {
    t0 = $[0];
  }
  return t0;
}
```

**Note**: React Native 0.76+ includes DevTools with Memo badge support by default. For older versions or third-party debuggers with version mismatches, you may need to override `react-devtools-core` in `package.json`.

## Incremental Adoption

You can incrementally adopt React Compiler using two strategies:

### Strategy 1: Limit to Specific Directories

Configure the Babel plugin to only run on specific files, e.g. `src/path/to/dir` in the following examples:

**Expo** (create `babel.config.js` with `npx expo customize babel.config.js`):

```javascript
// babel.config.js
module.exports = function (api) {
  api.cache(true);
  return {
    presets: [
      [
        'babel-preset-expo',
        {
          'react-compiler': {
            sources: (filename) => {
              return filename.includes('src/path/to/dir');
            },
          },
        },
      ],
    ],
  };
};
```

**React Native (without Expo)**:

```javascript
// babel.config.js
const ReactCompilerConfig = {
  target: '19',
  sources: (filename) => {
    return filename.includes('src/path/to/dir');
  },
};

module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['module:@react-native/babel-preset'],
    plugins: [['babel-plugin-react-compiler', ReactCompilerConfig]],
  };
};
```

After changing `babel.config.js`, restart Metro with cache cleared:

```bash
# Expo
npx expo start --clear

# React Native CLI
npx react-native start --reset-cache
```

### Strategy 2: Opt Out Specific Components

Use the `"use no memo"` directive to skip optimization for specific components or files:

```jsx
function ProblematicComponent() {
  'use no memo';

  return <Text>Will not be optimized</Text>;
}
```

This is useful for temporarily opting out components that cause issues. Fix the underlying problem and remove the directive once resolved.

## How It Works

The compiler transforms your code to automatically cache values:

**Before (your code):**

```jsx
export default function MyApp() {
  const [value, setValue] = useState('');
  return (
    <TextInput onChangeText={() => setValue(value)}>Hello World</TextInput>
  );
}
```

**After (compiled output):**

```jsx
import { c as _c } from 'react/compiler-runtime';

export default function MyApp() {
  const $ = _c(2); // Cache with 2 slots
  const [value, setValue] = useState('');

  let t0;
  if ($[0] !== value) {
    t0 = (
      <TextInput onChangeText={() => setValue(value)}>Hello World</TextInput>
    );
    $[0] = value;
    $[1] = t0;
  } else {
    t0 = $[1]; // Return cached JSX
  }
  return t0;
}
```

## Code Examples

### React Compiler Playground

Test transformations at [React Playground](https://playground.react.dev/).

### What Gets Optimized

```jsx
// Components - auto-memoized
const Button = ({ onPress, label }) => (
  <Pressable onPress={onPress}>
    <Text>{label}</Text>
  </Pressable>
);

// Callbacks - auto-cached (no useCallback needed)
const handlePress = () => {
  console.log('pressed');
};

// Expensive computations - auto-cached (no useMemo needed)
const filtered = items.filter((item) => item.active);
```

### What Breaks Compilation

```jsx
// BAD: Mutating props
const BadComponent = ({ items }) => {
  items.push('new item'); // Mutation!
  return <List data={items} />;
};

// BAD: Mutating during render
const BadMutation = () => {
  const [items, setItems] = useState([]);
  items.push('new'); // Mutation during render!
  return <List data={items} />;
};

// BAD: Non-idempotent render
let counter = 0;
const BadRender = () => {
  counter++; // Side effect during render!
  return <Text>{counter}</Text>;
};
```

## Should You Remove Manual Memoization?

Improvements are primarily automatic. You can remove instances of `useCallback`, `useMemo`, and `React.memo` in favor of automatic memoization once the compiler is working correctly in your project.

**Note**: Class components will not be optimized. Migrate to function components for full benefits.

Expo's implementation only runs on application code (not node_modules), and only when bundling for the client (disabled in server rendering).

## Expected Performance Improvements

Testing on Expensify app showed:

- **4.3% improvement** in Chat Finder TTI
- Significant reduction in cascading re-renders
- Most impact on apps without existing manual optimization

Already heavily optimized apps may see marginal gains.

## Common Pitfalls

- **Not fixing ESLint errors first**: When ESLint reports an error, the compiler skips that component—this is safe but means you miss optimization
- **Expecting it to fix bad patterns**: Compiler optimizes good code, doesn't fix bad code
- **Forgetting shallow comparison**: Like `memo`, compiler uses shallow comparison for objects/arrays
- **Not running healthcheck**: Always run `npx react-compiler-healthcheck@latest` before enabling

## Related Skills

- [js-profile-react.md](./js-profile-react.md) - Verify optimization impact
- [js-atomic-state.md](./js-atomic-state.md) - Alternative for state-related re-renders
```

## File: `skills/react-native-best-practices/references/js-uncontrolled-components.md`
```markdown
---
title: Uncontrolled Components
impact: HIGH
tags: textinput, forms, controlled, uncontrolled
---

# Skill: Uncontrolled Components

Fix TextInput synchronization and flickering issues by using uncontrolled component pattern.

## Quick Pattern

**Before (controlled - may flicker on legacy arch):**

```jsx
<TextInput value={text} onChangeText={setText} />
```

**After (uncontrolled - native owns state):**

```jsx
<TextInput defaultValue={text} onChangeText={setText} />
```

## When to Use

- TextInput flickers or shows wrong characters during fast typing
- Text input lags behind user input on low-end devices
- Using legacy (non-New Architecture) React Native
- Need maximum input responsiveness

## Prerequisites

- Understanding of React controlled vs uncontrolled components
- TextInput component in use

## Problem Description

![Controlled TextInput Ping-Pong Communication](images/controlled-textinput-pingpong.png)

The diagram shows what happens when typing "TEST" with a controlled `TextInput`:

1. User types "T" → `onChangeText('T')` fires
2. React calls `setValue('T')` → native updates to "T"
3. User types "E" → `onChangeText('TE')` fires
4. React calls `setValue('TE')` → native updates to "TE"
5. ...continues for each character

**The problem**: Each character requires a round-trip between native and JavaScript. On legacy architecture, if React state update is slow, native may show intermediate states (flicker).

**New Architecture note:** This issue is largely resolved in New Architecture, but uncontrolled pattern still provides best performance.

## Step-by-Step Instructions

### 1. Identify Controlled TextInput

```jsx
// Controlled - value prop syncs state to native
const ControlledInput = () => {
  const [value, setValue] = useState('');
  
  return (
    <TextInput
      value={value}           // This causes sync issues
      onChangeText={setValue}
    />
  );
};
```

### 2. Convert to Uncontrolled

Remove the `value` prop to make it uncontrolled:

```jsx
// Uncontrolled - native owns the state
const UncontrolledInput = () => {
  const [value, setValue] = useState('');
  
  return (
    <TextInput
      defaultValue={value}     // Only sets initial value
      onChangeText={setValue}  // Still updates React state
    />
  );
};
```

### 3. Use Ref for Programmatic Control

If you need to read/set value programmatically:

```jsx
const UncontrolledWithRef = () => {
  const inputRef = useRef(null);
  
  const clearInput = () => {
    inputRef.current?.clear();
  };
  
  const getValue = () => {
    // Use onChangeText to track value, or native methods
  };
  
  return (
    <TextInput
      ref={inputRef}
      defaultValue=""
      onChangeText={(text) => console.log('Current:', text)}
    />
  );
};
```

## Code Examples

### Full Migration Example

**Before (Controlled):**

```jsx
const SearchInput = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  
  const handleChange = (text) => {
    setQuery(text);
    fetchResults(text).then(setResults);
  };
  
  return (
    <View>
      <TextInput
        value={query}              // Remove this
        onChangeText={handleChange}
        placeholder="Search..."
      />
      <ResultsList data={results} />
    </View>
  );
};
```

**After (Uncontrolled):**

```jsx
const SearchInput = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  
  const handleChange = (text) => {
    setQuery(text);
    fetchResults(text).then(setResults);
  };
  
  return (
    <View>
      <TextInput
        defaultValue=""           // Initial value only
        onChangeText={handleChange}
        placeholder="Search..."
      />
      <ResultsList data={results} />
    </View>
  );
};
```

### When You Need Value Control

For input masking or validation that modifies input:

```jsx
// Option 1: Accept the controlled behavior (may flicker)
const MaskedInput = () => {
  const [value, setValue] = useState('');
  
  const handleChange = (text) => {
    // Phone mask: (123) 456-7890
    const masked = maskPhone(text);
    setValue(masked);
  };
  
  return (
    <TextInput
      value={value}  // Necessary for masking
      onChangeText={handleChange}
    />
  );
};

// Option 2: Use a native masked input library
// react-native-masked-text handles this natively
```

## Decision Matrix

| Scenario | Recommendation |
|----------|---------------|
| Simple text input | Uncontrolled |
| Search/filter input | Uncontrolled |
| Form with validation on submit | Uncontrolled |
| Input masking (phone, credit card) | Controlled or native library |
| Character-by-character validation | Controlled |
| New Architecture app | Either works well |

## Common Pitfalls

- **Forgetting `defaultValue`**: Without it, input starts empty
- **Trying to clear with state**: Use `ref.current.clear()` instead
- **Mixing patterns**: Don't use both `value` and `defaultValue`

## Related Skills

- [js-profile-react.md](./js-profile-react.md) - Profile input performance
- [js-concurrent-react.md](./js-concurrent-react.md) - Defer expensive search operations
```

## File: `skills/react-native-best-practices/references/native-android-16kb-alignment.md`
```markdown
---
title: Android 16 KB Page Size Alignment
impact: CRITICAL
tags: android, native, 16kb, alignment, page-size, google-play, third-party
---

# Android 16 KB page size alignment

---

## Quick Reference

| Item                   | Details                                              |
| ---------------------- | ---------------------------------------------------- |
| Google Play deadline   | November 1, 2025 for apps targeting Android 15+      |
| React Native support   | Built-in since React Native 0.79                     |
| What to check          | Third-party native libraries (`.so` files)           |
| Official documentation | [developer.android.com/guide/practices/page-sizes][] |

[developer.android.com/guide/practices/page-sizes]: https://developer.android.com/guide/practices/page-sizes

---

## Quick Command

Verify APK alignment using Android's official `zipalign` tool:

```bash
zipalign -c -P 16 -v 4 app-release.apk
```

If any 64-bit libraries (`arm64-v8a`, `x86_64`) show misalignment, they need updating.

For deeper ELF-level inspection, use Android's [check_elf_alignment.sh][] script.

[check_elf_alignment.sh]: https://cs.android.com/android/platform/superproject/main/+/main:core/extras/tools/check_elf_alignment.sh

---

## When to Check

React Native 0.79+ builds core binaries with correct alignment. However, **third-party
native libraries** may still be misaligned. Check alignment when:

* Adding or updating SDKs with native code
* Preparing a release for Google Play
* Investigating crashes on Android 15+ devices with 16 KB page size

---

## CI Integration

Add alignment check to your release pipeline to catch issues before submission, example:

```bash
zipalign -c -P 16 -v 4 app-release.apk 2>&1 | tee alignment.log
if grep -q "Verification FAILED" alignment.log; then exit 1; fi
```

## Step-by-Step

1. Build your release APK or AAB
2. Run `zipalign` verification (see Quick Command)
3. If misaligned libraries are found, trace them to source packages (see below)
4. Update, replace, or remove the affected dependencies

For runtime testing, use the [16KB Android Emulator image][] or enable
"Boot with 16KB page size" on Pixel 8/8a/9 devices.

[16KB Android Emulator image]: https://developer.android.com/guide/practices/page-sizes#set-up-the-android-emulator-with-a-16-kb-based-system-image

---

## Tracing Misaligned Libraries

When `zipalign` reports a misaligned library like `libfoo.so`, find its source package:

```bash
# Find the .so file in node_modules
find node_modules -name "libfoo.so" 2>/dev/null

# Or search gradle files for references
grep -r "foo" node_modules/*/android --include="*.gradle" 2>/dev/null
```

Once identified, update the dependency or contact the vendor for a 16KB-compatible build.

---

## Common Pitfalls

* Waiting for Play Store rejection instead of checking in CI
* Assuming a React Native upgrade rebuilds third-party native binaries
* Only checking 32-bit ABIs (`armeabi-v7a`, `x86`) — these are not affected
* Using `zipalign` without the `-P 16` flag (checks 4 KB, not 16 KB)
* Validating only debug builds

---

## Fixing Alignment Issues

Alignment issues require **rebuilding** the native library with a compatible toolchain.
Repackaging alone does not fix them.

See [official remediation steps][] for detailed guidance.

[official remediation steps]: https://developer.android.com/guide/practices/page-sizes#build-app-16kb

---

## Related Skills

* [native-profiling.md](./native-profiling.md) — Native debugging tools
```

## File: `skills/react-native-best-practices/references/native-measure-tti.md`
```markdown
---
title: Measure TTI (Time to Interactive)
impact: HIGH
tags: tti, startup, performance, markers
---

# Skill: Measure TTI (Time to Interactive)

Set up performance markers to measure app startup time and track TTI improvements.

## Quick Command

```bash
npm install react-native-performance
```

```tsx
// Mark when screen is interactive
import performance from 'react-native-performance';

useEffect(() => {
  performance.mark('screenInteractive');
}, []);
```

## When to Use

- App startup feels slow
- Need baseline metrics for optimization
- Setting up performance monitoring
- Comparing TTI across releases

## Prerequisites

- `react-native-performance` library (recommended)

```bash
npm install react-native-performance
```

> **Note**: This skill involves interpreting visual timeline diagrams and profiler output. AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing metrics manually, or await MCP-based visual feedback integration (see roadmap).

## Understanding TTI

**Time to Interactive**: Time from app icon tap to displaying usable content.

### Startup Types

| Type | Description | Measure? |
|------|-------------|----------|
| Cold | App not in memory, full init | ✅ Yes |
| Warm | Process exists, activity recreated | ❌ Skip |
| Hot | App in background, resumed | ❌ Skip |
| Prewarmed (iOS) | iOS pre-initialized app | ❌ Filter out |

**Only measure cold starts** for consistent metrics.

## React Native Startup Pipeline

![TTI Warm Start Diagram](images/tti-warm-start-diagram.png)

The diagram shows a warm start (app was in memory):

**UI Thread:**
1. `init native process` → `init native app`
2. Gap while user is away (e.g., "5h break from using the app")
3. `JS bundle load` → `RootView render`

**JS Thread (runs in parallel):**
- `init entrypoint` → `registerComponent`

**Pipeline markers:**
```
1. Native Process Init     (nativeLaunchStart → nativeLaunchEnd)
2. Native App Init         (appCreationStart → appCreationEnd)  
3. JS Bundle Load          (runJSBundleStart → runJSBundleEnd)
4. RN Root View Render     (contentAppeared)
5. React App Interactive   (screenInteractive) ← This is TTI
```

## Step-by-Step Implementation

### 1. Detect Cold Start

**iOS (Swift):**

```swift
let isColdStart = ProcessInfo.processInfo.environment["ActivePrewarm"] != "1"
```

**Android (Kotlin):**

```kotlin
class MainApplication : Application() {
    var isColdStart = false
    
    override fun onCreate() {
        super.onCreate()
        
        var firstPostEnqueued = true
        Handler().post { firstPostEnqueued = false }
        
        registerActivityLifecycleCallbacks(object : ActivityLifecycleCallbacks {
            override fun onActivityCreated(activity: Activity, savedInstanceState: Bundle?) {
                unregisterActivityLifecycleCallbacks(this)
                if (firstPostEnqueued && savedInstanceState == null) {
                    isColdStart = true
                }
            }
            // ... other callbacks
        })
    }
}
```

### 2. Check Foreground State

Only measure when app starts in foreground.

**iOS:**

```swift
var isForegroundProcess = false

override func application(_ application: UIApplication, 
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    if application.applicationState == .active {
        isForegroundProcess = true
    }
    return true
}
```

**Android:**

```kotlin
private fun isForegroundProcess(): Boolean {
    val processInfo = ActivityManager.RunningAppProcessInfo()
    ActivityManager.getMyMemoryState(processInfo)
    return processInfo.importance == IMPORTANCE_FOREGROUND
}
```

### 3. Set Up Performance Markers

Using `react-native-performance`:

**Native (iOS):**

```swift
import ReactNativePerformance

RNPerformance.sharedInstance().mark("appCreationStart")
// ... app init ...
RNPerformance.sharedInstance().mark("appCreationEnd")
```

**Native (Android):**

```kotlin
import com.oblador.performance.RNPerformance

RNPerformance.getInstance().mark("appCreationStart")
// ... app init ...
RNPerformance.getInstance().mark("appCreationEnd")
```

### 4. Mark Screen Interactive (JavaScript)

```tsx
import performance from 'react-native-performance';

export default function HomeScreen() {
    useEffect(() => {
        // Mark when meaningful content is displayed
        performance.mark('screenInteractive');
    }, []);
    
    return <TabNavigator />;
}
```

### 5. Collect and Report Metrics

```tsx
import performance from 'react-native-performance';

const collectTTIMetrics = () => {
    const entries = performance.getEntriesByType('mark');
    
    // Calculate durations
    const metrics = {
        nativeInit: getMarkDuration('nativeLaunchStart', 'nativeLaunchEnd'),
        appCreation: getMarkDuration('appCreationStart', 'appCreationEnd'),
        jsBundleLoad: getMarkDuration('runJSBundleStart', 'runJSBundleEnd'),
        tti: getMarkDuration('nativeLaunchStart', 'screenInteractive'),
    };
    
    // Send to analytics
    analytics.track('app_performance', metrics);
};
```

## Built-in Markers

`react-native-performance` provides automatic markers:

| Marker | Description |
|--------|-------------|
| `nativeLaunchStart` | Process start (pre-main) |
| `nativeLaunchEnd` | Native init complete |
| `runJSBundleStart` | JS bundle loading starts |
| `runJSBundleEnd` | JS bundle loaded |
| `contentAppeared` | RN root view rendered |

## Listening to Native Events

**iOS (JS Bundle Load):**

```swift
NotificationCenter.default.addObserver(
    self,
    selector: #selector(onJSLoad),
    name: NSNotification.Name("RCTJavaScriptDidLoadNotification"),
    object: nil
)
```

**Android (JS Bundle Load):**

```kotlin
ReactMarker.addListener { name ->
    when (name) {
        RUN_JS_BUNDLE_START -> { /* mark start */ }
        RUN_JS_BUNDLE_END -> { /* mark end */ }
        CONTENT_APPEARED -> { /* mark content */ }
    }
}
```

## Target Metrics

| Metric | Good | Acceptable | Needs Work |
|--------|------|------------|------------|
| TTI | < 2s | 2-4s | > 4s |
| JS Bundle Load | < 500ms | 500ms-1s | > 1s |
| Native Init | < 500ms | 500ms-1s | > 1s |

**Note**: Targets vary by app complexity and device tier.

## Common Pitfalls

- **Including prewarmed starts**: iOS prewarming skews metrics
- **Measuring warm/hot starts**: Only cold starts are meaningful
- **Wrong screenInteractive placement**: Mark when truly interactive, not just mounted
- **Not filtering background launches**: Push notifications can start app in background

## Related Skills

- [bundle-analyze-js.md](./bundle-analyze-js.md) - Reduce JS bundle load time
- [native-profiling.md](./native-profiling.md) - Profile native init
- [bundle-hermes-mmap.md](./bundle-hermes-mmap.md) - Improve Android TTI
```

## File: `skills/react-native-best-practices/references/native-memory-leaks.md`
```markdown
---
title: Hunt Native Memory Leaks
impact: MEDIUM
tags: memory, leaks, xcode, instruments, profiler
---

# Skill: Hunt Native Memory Leaks

Find native memory leaks using Xcode Leaks and Android Studio Memory Profiler.

## Quick Command

```bash
# iOS: Profile with Leaks instrument
# Xcode → Product → Profile (Cmd+I) → Leaks template

# Android: Memory Profiler
# Android Studio → Run → Profile → Track Memory Consumption
```

## When to Use

- App memory grows despite JS profiler showing no leaks
- Native modules suspected of leaking
- Activity recreation causes memory growth (Android)
- C++/Swift/Kotlin code under investigation

## iOS: Xcode Leaks

### Quick Check: Memory Report

1. Run app via Xcode
2. Open **Debug Navigator** (side panel)
3. Click **Memory**
4. Watch graph for continuous growth

### Deep Analysis: Instruments Leaks

![Xcode Instruments Templates](images/xcode-instruments-templates.png)

1. **Xcode → Product → Profile** (or Cmd+I)
2. Select **Leaks** template (highlighted with orange triangle icon in the grid)
3. Click **Choose**
4. Click **Record** (red circle)
5. Use the app, perform suspect actions
6. Stop recording

The template picker shows all available Instruments:
- **Leaks**: Memory leak detection (what we need)
- **Allocations**: All memory allocations over time
- **Time Profiler**: CPU usage profiling
- **Zombies**: Detect messages to deallocated objects

### Analyzing Results

**Red markers** = Leaked memory detected

Click on leak to see:
- **Leaked Object**: Type and size
- **Responsible Library**: Which code leaked
- **Responsible Frame**: Exact function
- **Stack Trace**: Full call path (right panel)

**Double-click function** to see source code.

### Common iOS Leak: Missing delete

```cpp
// BAD: Memory leak
void createNewStrings() {
    std::string* str = new std::string("Hello");
    // Forgot delete str;
}

// GOOD: Fixed
void createNewStrings() {
    std::string* str = new std::string("Hello");
    // ... use str ...
    delete str;
}

// BETTER: Use smart pointers
void createNewStrings() {
    auto str = std::make_unique<std::string>("Hello");
    // Automatically deleted
}
```

## Android: Memory Profiler

### Launch Profiler

1. **Run → Profile** (or click Profile in toolbar)
2. Or: **View → Tool Windows → Profiler**
3. Select **"Track Memory Consumption"**

### Recording

1. Start the app
2. Perform actions that might leak
3. Watch memory graph for growth patterns

### Analyzing Allocations

Memory profiler shows:
- **Allocations count**: Objects created
- **Deallocations count**: Objects freed
- **Live objects**: Still in memory

**If allocations >> deallocations**, you have a leak.

### Common Android Leak: Listener Not Removed

```kotlin
// BAD: Leaks MainActivity on config change
class MainActivity : AppCompatActivity(), Callback {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        EventManager.addListener(this)
        // Never removed!
    }
}

// GOOD: Remove listener
class MainActivity : AppCompatActivity(), Callback {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        EventManager.addListener(this)
    }
    
    override fun onDestroy() {
        EventManager.removeListener(this)
        super.onDestroy()
    }
}
```

### Activity Recreation Test

Android recreates activities on:
- Screen rotation
- Dark mode change
- Locale change

**Test**: Rotate device multiple times, check if old activities are freed.

React Native note: RN opts out via `android:configChanges` in manifest, but native code might not.

## Debugging Workflow

### iOS

1. Profile with Instruments Leaks
2. Trigger suspect actions repeatedly
3. Wait for red leak markers
4. Click to identify responsible frame
5. Fix and re-test

### Android

1. Profile memory consumption
2. Trigger suspect actions (rotate, navigate)
3. Check allocation/deallocation counts
4. Look for classes with 0 deallocations
5. Fix and re-test

## Code Fixes by Pattern

### Reference Cycle (Swift)

```swift
// BAD
class Parent {
    var child: Child?
}
class Child {
    var parent: Parent?  // Strong reference cycle
}

// GOOD
class Parent {
    var child: Child?
}
class Child {
    weak var parent: Parent?  // Weak breaks cycle
}
```

### Missing Cleanup (C++)

```cpp
// BAD
void process() {
    auto* data = new LargeData();
    if (error) return;  // Leak!
    delete data;
}

// GOOD: RAII with unique_ptr
void process() {
    auto data = std::make_unique<LargeData>();
    if (error) return;  // Automatically cleaned up
}
```

### Global Singleton Holding References (Kotlin)

```kotlin
// BAD: Holds strong references
object Cache {
    private val items = mutableMapOf<String, Callback>()
}

// GOOD: Use weak references
object Cache {
    private val items = mutableMapOf<String, WeakReference<Callback>>()
}
```

## Verification

After fixing:
1. Re-run profiler
2. Perform same actions
3. Verify:
   - iOS: No red leak markers
   - Android: Allocations ≈ Deallocations

## Common Pitfalls

- **Testing in debug mode**: Some leaks only appear in release
- **Not waiting for GC**: Force GC before concluding no leak
- **Ignoring small leaks**: They add up over time
- **Missing cleanup in invalidate()**: Turbo Modules need proper cleanup

## Related Skills

- [native-memory-patterns.md](./native-memory-patterns.md) - Understanding memory patterns
- [js-memory-leaks.md](./js-memory-leaks.md) - JS-side leaks
- [native-threading-model.md](./native-threading-model.md) - Module invalidation
```

## File: `skills/react-native-best-practices/references/native-memory-patterns.md`
```markdown
---
title: Native Memory Management
impact: MEDIUM
tags: memory, c++, swift, kotlin, arc, smart-pointers
---

# Skill: Native Memory Management

Understand memory management patterns in C++, Swift, and Kotlin for React Native native modules.

## Quick Reference

| Pattern | Languages | Mechanism |
|---------|-----------|-----------|
| Reference Counting | Swift, Obj-C, C++ (smart ptrs) | Count refs, free at zero |
| Garbage Collection | Kotlin/Java, JavaScript | GC scans and frees unreachable |
| Manual | C, C++ (raw pointers) | Explicit new/delete |

**Key rule**: Use `std::unique_ptr`/`std::shared_ptr` in C++, `weak` for delegates in Swift.

## When to Use

- Writing native modules with manual memory management
- Debugging native memory leaks
- Interfacing C++ with Swift/Kotlin
- Understanding reference counting vs garbage collection

## Memory Management Patterns

| Pattern | Languages | Mechanism |
|---------|-----------|-----------|
| Reference Counting | Swift, Obj-C, C++ (smart pointers) | Count refs, free at zero |
| Garbage Collection | Kotlin/Java, JavaScript | GC scans and frees unreachable |
| Manual | C, C++ (raw pointers) | Explicit new/delete |

## C++ Smart Pointers

### `std::unique_ptr` - Single Owner

```cpp
#include <memory>

void takeOwnership(std::unique_ptr<std::string> s) {
    std::cout << *s;
    // Automatically deleted when function ends
}

int main() {
    auto str = std::make_unique<std::string>("Hello");
    
    // Can only be moved, not copied
    takeOwnership(std::move(str));
    // str is now empty
    
    return 0;
}
```

### `std::shared_ptr` - Multiple Owners

```cpp
void useShared(std::shared_ptr<std::string> s) {
    std::cout << *s;  // Reference count temporarily +1
}

void useReference(const std::shared_ptr<std::string>& s) {
    std::cout << *s;  // No ref count change (passed by reference)
}

int main() {
    auto str = std::make_shared<std::string>("Hello");
    
    useShared(str);      // Copies pointer, ref count +1
    useReference(str);   // No copy, ref count unchanged
    
    std::cout << *str;   // Still valid
    return 0;
}
```

### `std::weak_ptr` - Non-Owning Reference

```cpp
void useWeak(std::weak_ptr<std::string> weak) {
    if (auto shared = weak.lock()) {  // Check if still exists
        std::cout << *shared;
    } else {
        std::cout << "Object destroyed";
    }
}

int main() {
    auto str = std::make_shared<std::string>("Hello");
    std::weak_ptr<std::string> weak = str;  // No ref count increase
    
    useWeak(weak);  // Works
    str.reset();    // Destroys object
    useWeak(weak);  // "Object destroyed"
    
    return 0;
}
```

## Swift ARC (Automatic Reference Counting)

```swift
class Person {
    let name: String
    init(name: String) { self.name = name }
    deinit { print("Deallocated") }
}

do {
    let person1 = Person(name: "John")  // Ref count: 1
    
    do {
        let person2 = person1  // Ref count: 2
    }  // person2 out of scope, ref count: 1
    
}  // person1 out of scope, ref count: 0, "Deallocated"
```

### Breaking Reference Cycles with `weak`

```swift
// BAD: Reference cycle (memory leak)
class A {
    var b: B?
}
class B {
    var a: A?  // Strong reference creates cycle
}

// GOOD: Use weak to break cycle
class A {
    var b: B?
}
class B {
    weak var a: A?  // Weak reference, doesn't prevent deallocation
}
```

## Kotlin/Android GC

### WeakHashMap for Caches

```kotlin
val weakMap = WeakHashMap<String, String>()

run {
    weakMap[String("temp")] = "value"
    println(weakMap.size)  // 1
}

System.gc()  // Force garbage collection
Thread.sleep(100)

println(weakMap.size)  // 0 (key was collected)
```

### WeakReference for Callbacks

```kotlin
class DataManager {
    // Weak references to listeners prevent memory leaks
    private val listeners = mutableListOf<WeakReference<DataListener>>()
    
    fun addListener(listener: DataListener) {
        listeners.add(WeakReference(listener))
    }
    
    fun notifyListeners(data: String) {
        listeners.forEach { ref ->
            ref.get()?.onDataChanged(data)
        }
    }
}
```

## Common Memory Leak Sources

### 1. Forgetting to Delete (C++)

```cpp
// BAD: Memory leak
int main() {
    std::string* str = new std::string("Hello");
    // Forgot to delete!
    return 0;
}

// GOOD: Use smart pointers or stack allocation
int main() {
    auto str = std::make_unique<std::string>("Hello");
    // Automatically deleted
    return 0;
}
```

### 2. Reference Cycles (Swift/C++)

```cpp
// BAD: Cycle
class A { std::shared_ptr<B> b; };
class B { std::shared_ptr<A> a; };

// GOOD: Break with weak_ptr
class A { std::shared_ptr<B> b; };
class B { std::weak_ptr<A> a; };
```

### 3. Unremoved Listeners (Kotlin)

```kotlin
// BAD: Listener never removed
class MyClass {
    private val listener = object : Callback {
        override fun onEvent() { /* ... */ }
    }
    
    init {
        EventManager.addListener(listener)
        // Never removed!
    }
}

// GOOD: Implement cleanup
class MyClass : AutoCloseable {
    private val listener = object : Callback {
        override fun onEvent() { /* ... */ }
    }
    
    init {
        EventManager.addListener(listener)
    }
    
    override fun close() {
        EventManager.removeListener(listener)
    }
}
```

## Swift `Unmanaged` (Advanced)

For C interop, manually manage reference counts:

```swift
let obj = MyObject()                        // Ref count: 1

// Increment manually
let unmanaged = Unmanaged.passRetained(obj) // Ref count: 2

// Decrement and get object
let retrieved = unmanaged.takeRetainedValue() // Ref count: 1

// Get raw pointer for C
let pointer = unmanaged.toOpaque()
```

**Rule**: Match `passRetained` with `takeRetainedValue`, `passUnretained` with `takeUnretainedValue`.

## Best Practices Summary

| Language | Best Practice |
|----------|---------------|
| C++ | Use smart pointers (`shared_ptr`, `unique_ptr`) |
| Swift | Use `weak` for delegates, breaking cycles |
| Kotlin | Implement `AutoCloseable`, use `WeakReference` |
| All | Prefer stack over heap when possible |

## Related Skills

- [native-memory-leaks.md](./native-memory-leaks.md) - Find leaks with profilers
- [native-turbo-modules.md](./native-turbo-modules.md) - Build memory-safe modules
```

## File: `skills/react-native-best-practices/references/native-platform-setup.md`
```markdown
---
title: Platform Differences
impact: MEDIUM
tags: ios, android, xcode, gradle, cocoapods
---

# Skill: Platform Differences

Navigate iOS and Android tooling, dependency management, and build systems in React Native.

## Quick Reference

| Platform | IDE | Package Manager | Build System |
|----------|-----|-----------------|--------------|
| JavaScript | VS Code | npm/yarn/pnpm/bun | Metro |
| iOS | Xcode | CocoaPods | xcodebuild |
| Android | Android Studio | Gradle | Gradle |

```bash
# Common commands
bundle install                      # Install ruby bundler
cd ios && bundle exec pod install   # Install CocoaPods deps
cd android && ./gradlew clean       # Clean Android build
xed ios/                            # Open Xcode
```

## When to Use

- Setting up native development environment
- Adding native dependencies
- Debugging platform-specific issues
- Understanding build processes

## Dependency Management

### JavaScript (npm/yarn/pnpm/bun)

Infer package manager from lockfile: `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `bun.lockb`.

### iOS (CocoaPods)

```bash
# Install pods after npm install
bundle install
cd ios && bundle exec pod install

# Key files
ios/Podfile           # Pod dependencies
ios/Pods/             # Installed pods (gitignored)
ios/*.xcworkspace     # Open this in Xcode (not .xcodeproj)
Gemfile               # Ruby/CocoaPods version
```


### Android (Gradle)

```bash
# Sync after adding dependencies
cd android && ./gradlew clean

# Key files
android/build.gradle           # Project-level config
android/app/build.gradle       # App dependencies
android/gradle.properties      # Build flags
android/gradlew                # Gradle wrapper
```

## Common Commands

```bash
# iOS
bundle install                         # Install ruby bundler
cd ios && bundle exec pod install      # Install pods
xcrun simctl list                      # List simulators

# Android  
cd android && ./gradlew clean          # Clean build
./gradlew tasks                        # List available tasks
./gradlew assembleRelease              # Build release APK

# React Native CLI
npx react-native start                 # Start Metro
npx react-native run-ios               # Run on iOS
npx react-native run-android           # Run on Android
npx react-native build-ios             # Build for iOS
npx react-native build-android         # Build for Android

# Expo
npx expo start                         # Start Metro (Expo)
npx expo run:ios                       # Run on iOS (dev client)
npx expo run:android                   # Run on Android (dev client)
npx expo prebuild                      # Generate native projects
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pod install fails | `cd ios && bundle exec pod install --repo-update` |
| Xcode build fails | `cd ios && xcodebuild clean` |
| Android Gradle sync fails | `./gradlew clean` then sync |
| Can't find simulator | `xcrun simctl list` to verify name |
| Metro cache issues | `npx react-native start --reset-cache` |
| React Native cache issues | `npx react-native clean` |

## Related Skills

- [native-profiling.md](./native-profiling.md) - Use IDE profilers
- [native-turbo-modules.md](./native-turbo-modules.md) - Build native modules
- [upgrading-react-native.md](../../upgrading-react-native/references/upgrading-react-native.md) - Upgrade React Native safely
```

## File: `skills/react-native-best-practices/references/native-profiling.md`
```markdown
---
title: Profile Native Code
impact: MEDIUM
tags: xcode, instruments, android-studio, profiler
---

# Skill: Profile Native Code

Use Xcode Instruments and Android Studio Profiler to identify native performance bottlenecks.

## Quick Command

```bash
# iOS: Open Instruments
# Xcode → Open Developer Tool → Instruments → Time Profiler

# Android: Open Profiler
# Android Studio → View → Tool Windows → Profiler
```

## When to Use

- App is slow but JS profiler shows no issues
- Investigating native module performance
- Startup feels slow (native init)
- Battery drain concerns
- Need CPU/memory breakdown by thread

> **Note**: This skill involves interpreting visual profiler output (Xcode Instruments, Android Studio Profiler). AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing the profiler UI manually, or await MCP-based visual feedback integration (see roadmap).

## iOS Profiling with Xcode

### Quick Check: Debug Navigator

1. Run app via Xcode
2. Open Debug Navigator (side panel)
3. View real-time: CPU, Memory, Disk, Network

**CPU percentage can exceed 100%** (multi-core usage).

### Deep Profiling: Instruments

1. Open: **Xcode → Open Developer Tool → Instruments**
2. Select **Time Profiler**
3. Choose target device and app
4. Click record (red circle)
5. Perform actions in app
6. Stop recording

### Analyzing Time Profiler Results

**Key views:**
- **Flame Graph**: Visual call stack over time
- **Call Tree**: Hierarchical function breakdown
- **Ranked**: Functions sorted by time (Bottom-Up)

**Useful filters:**
- Hide System Libraries
- Invert Call Tree (bottom-up view)
- Filter by thread (main, JS, etc.)

**Identifying problems:**
- **Microhang**: Brief UI unresponsiveness
- **Hang**: Full UI thread block (critical)
- Yellow = most time spent

### Thread Breakdown

Pin threads to compare:
- **Main thread** (SampleApp): UI rendering
- **JavaScript thread**: React/JS execution
- **Background threads**: Native modules

**Pro tip**: JS thread blocking ≠ UI block (React Native design benefit).

## Android Profiling with Android Studio

### Launch Profiler

1. **View → Tool Windows → Profiler**
2. Or: Click "Profile" in toolbar

### CPU Profiling

1. Select **"Find CPU Hotspots"**
2. Click **"Start profiler task"**
3. Interact with app
4. Stop to analyze

### Analyzing Results

**Flame Graph:**
- Zoom with scroll/pinch
- Click to expand call stacks
- Filter by keyword (e.g., "hermes")

**Views:**
- **Top Down**: From entry points down
- **Bottom Up**: From slowest functions up
- **Flame Chart**: Timeline visualization

### Reading the Call Stack

Example analysis:
```
JS Thread activity after button press:
- Event handler on main thread
- Triggers JS work via sync JSI calls
- Hermes processes React reconciliation
- ~30% time in "commit" phase (Yoga layout)
```

## Code Example: What to Look For

### 5000 Views in ScrollView (Bad)

Profiler shows:
- 240ms+ JS thread work
- Many 1ms Hermes spikes
- Exceeds 16.6ms frame budget
- Result: Dropped frames, UI jank

### Using FlatList (Better)

Profiler shows:
- Minimal JS work (windowed rendering)
- Smooth main thread
- Stays within frame budget

## Platform Tools Summary

| Tool | Platform | Use Case |
|------|----------|----------|
| Time Profiler | iOS | CPU hotspots |
| Leaks | iOS | Memory leaks |
| Hangs | iOS | UI thread blocks |
| CPU Profiler | Android | CPU hotspots |
| Memory Profiler | Android | Memory tracking |
| Perfetto | Android | Advanced trace analysis |

## Perfetto (Advanced Android)

Export traces from Android Studio and analyze at [ui.perfetto.dev](https://ui.perfetto.dev/):

- Cross-process analysis
- Custom trace events
- Additional visualizations

## Pro Tips

1. **Profile on low-end devices**: Issues appear more clearly
2. **Use release builds**: Debug builds have overhead
3. **Compare before/after**: Export traces for comparison
4. **Filter by thread**: Focus on relevant work
5. **Look for patterns**: Spikes correlating with interactions

## Expo Notes

- **Expo Go**: Cannot profile native code directly; JS profiling only
- **Dev Client / Prebuild**: Full native profiling supported via Xcode/Android Studio
- Run `npx expo prebuild` to generate native projects, then profile as bare React Native

## Common Findings

| Symptom | Likely Cause |
|---------|--------------|
| Main thread hangs | Heavy UI work, blocked operations |
| JS thread spikes | React re-renders, heavy computation |
| Background thread busy | Native module work |
| Memory climbing | Leak (see memory profiling skills) |

## Related Skills

- [native-measure-tti.md](./native-measure-tti.md) - Profile startup specifically
- [native-memory-leaks.md](./native-memory-leaks.md) - Memory profiling
- [js-profile-react.md](./js-profile-react.md) - JS/React profiling
```

## File: `skills/react-native-best-practices/references/native-sdks-over-polyfills.md`
```markdown
---
title: Native SDKs
impact: HIGH
tags: polyfills, intl, crypto, navigation, native
---

# Skill: Native SDKs

Replace web polyfills and JS navigators with native React Native implementations for better performance.

## Quick Pattern

**Before (JS polyfills - 430+ KB):**

```tsx
import '@formatjs/intl-datetimeformat/polyfill';
import CryptoJS from 'crypto-js';
import { createStackNavigator } from '@react-navigation/stack';
```

**After (native implementations):**

```tsx
// Hermes has native Intl.DateTimeFormat support, so this polyfill is often unnecessary
import { createHash } from 'react-native-quick-crypto';  // 58x faster
import { createNativeStackNavigator } from '@react-navigation/native-stack';
```

## When to Use

- Large JS bundle from polyfills
- Navigation feels non-native
- Crypto operations are slow
- Internationalization bloating bundle

## Step-by-Step Instructions

### 1. Remove Unnecessary Intl Polyfills

Hermes supports many `Intl` APIs natively, but not every constructor and method combination across platforms. Audit the exact APIs and methods you use before removing polyfills:

```tsx
// BEFORE: All these polyfills (430+ KB)
import '@formatjs/intl-getcanonicallocales/polyfill';
import '@formatjs/intl-locale/polyfill';
import '@formatjs/intl-numberformat/polyfill';
import '@formatjs/intl-numberformat/locale-data/en';
import '@formatjs/intl-datetimeformat/polyfill';
import '@formatjs/intl-datetimeformat/locale-data/en';
import '@formatjs/intl-pluralrules/polyfill';
import '@formatjs/intl-pluralrules/locale-data/en';
import '@formatjs/intl-relativetimeformat/polyfill';
import '@formatjs/intl-relativetimeformat/locale-data/en';
import '@formatjs/intl-displaynames/polyfill';
```

**Hermes Support (as of March 2026):**

| API | Hermes | Keep Polyfill? |
|-----|--------|----------------|
| `Intl.Collator` | ✅ | No |
| `Intl.DateTimeFormat` | ✅ | No |
| `Intl.NumberFormat` | ⚠️ Partial | Maybe |
| `Intl.getCanonicalLocales()` | ✅ | No |
| `Intl.supportedValuesOf()` | ✅ | No |
| `Intl.Locale` | ❌ | Yes |
| `Intl.PluralRules` | ❌ | Yes |
| `Intl.RelativeTimeFormat` | ❌ | Yes |
| `Intl.DisplayNames` | ❌ | Yes |
| `Intl.ListFormat` | ❌ | Yes |
| `Intl.Segmenter` | ❌ | Yes |

`Intl.NumberFormat` is not fully covered on Hermes across platforms. In particular, `Intl.NumberFormat.prototype.formatToParts()` still has an iOS gap, so keep `@formatjs/intl-numberformat` if your app relies on that method.

```tsx
// AFTER: Keep only the polyfills your app still needs
import '@formatjs/intl-locale/polyfill';
import '@formatjs/intl-pluralrules/polyfill';
import '@formatjs/intl-pluralrules/locale-data/en';
import '@formatjs/intl-relativetimeformat/polyfill';
import '@formatjs/intl-relativetimeformat/locale-data/en';
import '@formatjs/intl-displaynames/polyfill';
```

If you use `Intl.NumberFormat.prototype.formatToParts()` on Hermes/iOS, also keep:

```tsx
import '@formatjs/intl-numberformat/polyfill';
import '@formatjs/intl-numberformat/locale-data/en';
```

### 2. Use Native Crypto

Replace JS crypto with native C++ implementation:

```bash
npm install react-native-quick-crypto
```

**Performance**: Up to 58x faster than `crypto-js`.

```tsx
// BEFORE: Slow JS implementation
import CryptoJS from 'crypto-js';

// AFTER: Native C++ implementation
import { createHash } from 'react-native-quick-crypto';
```

Essential for:
- Web3 wallet seed generation
- CSPRNG (Cryptographically Secure Random Numbers)
- Any heavy cryptographic operations

### 3. Use Native Stack Navigator

```bash
npm install @react-navigation/native-stack react-native-screens
```

```tsx
// BEFORE: JS-based stack (more flexible, less native)
import { createStackNavigator } from '@react-navigation/stack';
const Stack = createStackNavigator();

// AFTER: Native stack (native feel, better performance)
import { createNativeStackNavigator } from '@react-navigation/native-stack';
const Stack = createNativeStackNavigator();

// Usage is nearly identical
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>
```

**Benefits:**
- Native navigation animations
- Platform-specific headers (large titles on iOS)
- Lower memory usage
- Offloads work from JS thread

### 4. Use Native Bottom Tabs

```bash
npm install @bottom-tabs/react-navigation react-native-bottom-tabs
```

```tsx
// BEFORE: JS tabs
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
const Tabs = createBottomTabNavigator();

// AFTER: Native tabs
import { createNativeBottomTabNavigator } from '@bottom-tabs/react-navigation';
const Tabs = createNativeBottomTabNavigator();

<Tabs.Navigator>
  <Tabs.Screen name="Home" component={HomeScreen} />
  <Tabs.Screen name="Profile" component={ProfileScreen} />
</Tabs.Navigator>
```

## Recommended Native Libraries

| Category | Library | Description |
|----------|---------|-------------|
| Navigation | `react-native-screens` | Native screen containers |
| Menus | `zeego` | Native menus (Radix-like API) |
| Slider | `@react-native-community/slider` | Native slider |
| Date Picker | `react-native-date-picker` | Native date/time picker |
| Image | `react-native-fast-image` | Native image caching |

## Decision Matrix

| Scenario | Use Native? | Tradeoff |
|----------|-------------|----------|
| Standard navigation | ✅ Yes | Slight API differences |
| Custom transition animations | ⚠️ Maybe | Native is more limited |
| Platform-consistent UI | ✅ Yes | Less customization |
| Unique/branded design | ⚠️ Consider JS | Native may not support |

## Common Pitfalls

- **Assuming constructor support means full method coverage**: Check the specific Hermes API and methods you call
- **Ignoring migration effort**: Native navigators have slightly different APIs
- **Over-customizing native components**: If design requires heavy customization, JS might be better

## Related Skills

- [bundle-analyze-js.md](./bundle-analyze-js.md) - Measure polyfill impact
- [bundle-library-size.md](./bundle-library-size.md) - Compare library sizes
```

## File: `skills/react-native-best-practices/references/native-threading-model.md`
```markdown
---
title: Threading Model
impact: HIGH
tags: threads, turbo-modules, fabric, async, sync
---

# Skill: Threading Model

Understand which threads Turbo Modules and Fabric use for initialization, method calls, and view updates.

## Quick Reference

| Action | iOS Thread | Android Thread |
|--------|------------|----------------|
| Module init | Main | JS (lazy) / Native (eager) |
| Sync method | JS | JS |
| Async method | Native modules | Native modules |
| View init/props | Main | Main |
| Yoga layout | JS | JS |

**Key rule**: Sync methods block JS thread. Keep under 16ms or make async.

## When to Use

- Building native modules
- Debugging threading issues
- Accessing UI from native code
- Understanding async vs sync method behavior

## Available Threads

| Thread | Name in Debugger | Purpose |
|--------|------------------|---------|
| Main/UI | Main thread | UI rendering, UIKit/Android Views |
| JavaScript | `mqt_v_js` | JS execution, React |
| Native Modules | `mqt_v_native` | Async Turbo Module calls |
| Custom | Various | Your background threads |

## Turbo Modules Threading

### Initialization

| Platform | Thread | Notes |
|----------|--------|-------|
| iOS | Main thread | Assumes UIKit access needed |
| Android (lazy) | JS thread | Default behavior |
| Android (eager) | Native modules thread | When `needsEagerInit = true` |

**iOS**: React Native runs `init` on main thread assuming UIKit access.

**Android Eager Loading:**

```kotlin
// ReactModuleInfo constructor params:
// canOverrideExistingModule, needsEagerInit, isCxxModule, isTurboModule
ReactModuleInfo(
    AwesomeModule.NAME,
    AwesomeModule.NAME,
    false,
    true,   // needsEagerInit = true → runs on native modules thread
    false,
    true
)
```

### Synchronous Method Calls

**Always run on JS thread** - blocks until return.

```swift
// iOS - runs on JS thread
@objc func multiply(_ a: Double, b: Double) -> NSNumber {
    // This blocks JS for entire duration!
    return a * b as NSNumber
}
```

**Danger**: Long sync operations freeze the app:

```swift
// BAD: Blocks JS for 20 seconds
@objc func multiply(_ a: Double, b: Double) -> NSNumber {
    Thread.sleep(forTimeInterval: 20)  // App frozen!
    return a * b as NSNumber
}
```

### Asynchronous Method Calls

**Run on Native Modules thread** - doesn't block JS.

```swift
// iOS - runs on mqt_v_native thread
@objc func asyncOperation(
    _ a: Double,
    resolve: @escaping RCTPromiseResolveBlock,
    reject: RCTPromiseRejectBlock
) {
    // Already on background thread
    resolve(a * 2)
}
```

```kotlin
// Android - runs on native modules thread
override fun asyncOperation(a: Double, promise: Promise?) {
    // Already on background thread
    promise?.resolve(a * 2)
}
```

### Module Invalidation

Called when React Native instance is torn down (e.g., Metro reload):

| Platform | Thread |
|----------|--------|
| iOS | Native modules thread |
| Android | ReactHost thread pool |

**iOS**: Implement `RCTInvalidating` protocol.

## Fabric (Native Views) Threading

### View Lifecycle

| Operation | Thread |
|-----------|--------|
| View init | Main thread |
| Prop updates | Main thread |
| Layout (Yoga) | JS thread |

Views always manipulate UI on main thread (UIKit/Android requirement).

### Yoga Layout

Layout calculations happen on JS thread:

```
JS Thread: Calculate Yoga tree → Shadow tree
Main Thread: Apply layout to native views
```

## Moving Work to Background

### iOS: DispatchQueue

```swift
@objc func heavyWork(
    resolve: @escaping RCTPromiseResolveBlock,
    reject: RCTPromiseRejectBlock
) {
    DispatchQueue.global().async {
        // Heavy computation here
        let result = self.compute()
        resolve(result)
    }
}
```

### Android: Coroutines

```kotlin
class MyModule(reactContext: ReactApplicationContext) :
    NativeMyModuleSpec(reactContext) {
    
    private val moduleScope = CoroutineScope(Dispatchers.Default + SupervisorJob())
    
    override fun heavyWork(promise: Promise?) {
        moduleScope.launch {
            // Heavy computation here
            val result = compute()
            promise?.resolve(result)
        }
    }
    
    override fun invalidate() {
        super.invalidate()
        moduleScope.cancel()  // Important: cancel to prevent leaks
    }
}
```

## Thread Safety Checklist

| Scenario | Safe? | Solution |
|----------|-------|----------|
| Sync method accessing shared state | ⚠️ | Use locks/synchronized |
| Async method accessing UI | ❌ | Dispatch to main thread |
| Multiple async calls to same resource | ⚠️ | Queue or mutex |
| Accessing JS from background | ❌ | Use CallInvoker |

### Accessing UI from Background (iOS)

```swift
DispatchQueue.global().async {
    let result = self.heavyComputation()
    
    DispatchQueue.main.async {
        // Safe to update UI here
        self.updateUI(with: result)
    }
}
```

### Accessing UI from Background (Android)

```kotlin
moduleScope.launch(Dispatchers.Default) {
    val result = heavyComputation()
    
    withContext(Dispatchers.Main) {
        // Safe to update UI here
        updateUI(result)
    }
}
```

## Summary Table

| Action | iOS Thread | Android Thread |
|--------|------------|----------------|
| Module init | Main | JS (lazy) / Native (eager) |
| Sync method | JS | JS |
| Async method | Native modules | Native modules |
| View init | Main | Main |
| Prop update | Main | Main |
| Yoga layout | JS | JS |
| Invalidate | Native modules | ReactHost pool |

## Related Skills

- [native-turbo-modules.md](./native-turbo-modules.md) - Implement background threads
- [native-profiling.md](./native-profiling.md) - Debug thread issues
```

## File: `skills/react-native-best-practices/references/native-turbo-modules.md`
```markdown
---
title: Fast Native Modules
impact: HIGH
tags: turbo-modules, native, swift, kotlin, c++
---

# Skill: Fast Native Modules

Build performant Turbo Modules using modern languages and background threading.

## Quick Pattern

**Incorrect (sync method blocks JS thread):**

```swift
@objc func heavyWork() -> NSNumber {
    Thread.sleep(forTimeInterval: 2)  // Blocks JS for 2s!
    return 42
}
```

**Correct (async on background thread):**

```swift
@objc func heavyWork(
    resolve: @escaping RCTPromiseResolveBlock,
    reject: RCTPromiseRejectBlock
) {
    DispatchQueue.global().async {
        let result = self.compute()
        resolve(result)
    }
}
```

## When to Use

- Creating new native modules
- Optimizing existing module performance
- Heavy computation needs to run off JS thread
- Cross-platform C++ code needed

## Prerequisites

- React Native Builder Bob for scaffolding

```bash
npx create-react-native-library@latest my-library
```

## Step-by-Step Instructions

### 1. Scaffold with Builder Bob

```bash
npx create-react-native-library@latest awesome-library
# Follow prompts: choose Turbo Module, select languages
```

Creates ready-to-publish library with:
- iOS (Obj-C/Swift) support
- Android (Kotlin) support
- TypeScript definitions
- Codegen setup

For local modules:

```bash
npx create-react-native-library@latest awesome-library --local
```

### 2. Enable Swift in iOS Module

Update `awesome-library.podspec`:

```diff
- s.source_files = "ios/**/*.{h,m,mm,cpp}"
+ s.source_files = "ios/**/*.{h,m,mm,cpp,swift}"
```

Create Swift file in Xcode (accept bridging header prompt).

Update header file for Swift compatibility:

```objc
// AwesomeLibrary.h
#import <Foundation/Foundation.h>

#if __cplusplus
#import "ReactCodegen/RNAwesomeLibrarySpec/RNAwesomeLibrarySpec.h"
#endif

@interface AwesomeLibrary : NSObject
#if __cplusplus
<NativeAwesomeLibrarySpec>
#endif
@end
```

Import header in bridging header:

```objc
// AwesomeLibrary-Bridging-Header.h
#import "AwesomeLibrary.h"
```

Implement in Swift:

```swift
// AwesomeLibrary.swift
import Foundation

extension AwesomeLibrary {
    @objc func multiply(_ a: Double, b: Double) -> NSNumber {
        return (a * b) as NSNumber
    }
}
```

Bridge in Obj-C++:

```objc
// AwesomeLibrary.mm
#import "AwesomeLibrary.h"

#if __has_include("awesome_library/awesome_library-Swift.h")
#import "awesome_library/awesome_library-Swift.h"
#else
#import "awesome_library-Swift.h"
#endif

@implementation AwesomeLibrary
RCT_EXPORT_MODULE()
RCT_EXTERN_METHOD(multiply:(double)a b:(double)b);
@end
```

### 3. Run on Background Thread (iOS)

```swift
@objc func heavyOperation(
    _ input: Double,
    resolve: @escaping RCTPromiseResolveBlock,
    reject: RCTPromiseRejectBlock
) {
    DispatchQueue.global().async {
        // Heavy work on background thread
        let result = self.expensiveComputation(input)
        resolve(result)
    }
}
```

### 4. Run on Background Thread (Android)

```kotlin
class AwesomeLibraryModule(reactContext: ReactApplicationContext) :
    NativeAwesomeLibrarySpec(reactContext) {
    
    private val moduleScope = CoroutineScope(Dispatchers.Default + SupervisorJob())
    
    override fun heavyOperation(input: Double, promise: Promise?) {
        moduleScope.launch {
            // Heavy work on coroutine
            val result = expensiveComputation(input)
            promise?.resolve(result)
        }
    }
    
    override fun invalidate() {
        super.invalidate()
        moduleScope.cancel()  // Prevent memory leaks!
    }
}
```

### 5. Use C++ for Cross-Platform Code

Create C++ Turbo Module for shared logic:

```cpp
// MyCppModule.h
#pragma once

#include <ReactCommon/TurboModule.h>

namespace facebook::react {

class MyCppModule : public TurboModule {
public:
    MyCppModule(std::shared_ptr<CallInvoker> jsInvoker);
    
    double multiply(double a, double b);
};

} // namespace facebook::react
```

Register for iOS auto-linking:

```objc
// MyCppModuleRegistration.mm
#include <ReactCommon/CxxTurboModuleUtils.h>

@implementation MyCppModuleRegistration

+ (void)load {
    facebook::react::registerCxxModuleToGlobalModuleMap(
        std::string(facebook::react::MyCppModule::kModuleName),
        [&](std::shared_ptr<facebook::react::CallInvoker> jsInvoker) {
            return std::make_shared<facebook::react::MyCppModule>(jsInvoker);
        }
    );
}

@end
```

## Threading Summary

| Method Type | Default Thread | Best Practice |
|-------------|----------------|---------------|
| Sync | JS thread | Keep fast (<16ms) |
| Async | Native modules thread | OK for moderate work |
| Heavy async | Custom background | Use DispatchQueue/Coroutines |

## Language Interop Costs

| Interface | Overhead | Notes |
|-----------|----------|-------|
| Obj-C ↔ C++ | ~0 | Compile-time |
| Swift ↔ C++ | ~0 | Swift 5.9+ interop |
| Kotlin ↔ C++ (JNI) | Medium | Per-call lookup |
| C++ Turbo Module | Low | JSI direct access |

**Tip**: C++ Turbo Modules skip JNI at runtime since JS holds direct C++ function references via JSI.

## Code Example: Complete Async Operation

```typescript
// TypeScript interface
export interface Spec extends TurboModule {
    multiply(a: number, b: number): number;  // Sync
    heavyOperation(input: number): Promise<number>;  // Async
}
```

```kotlin
// Android implementation
override fun heavyOperation(input: Double, promise: Promise?) {
    moduleScope.launch {
        try {
            val result = withContext(Dispatchers.Default) {
                // Simulate heavy work
                delay(1000)
                input * 2
            }
            promise?.resolve(result)
        } catch (e: Exception) {
            promise?.reject("ERROR", e.message)
        }
    }
}
```

```swift
// iOS implementation
@objc func heavyOperation(
    _ input: Double,
    resolve: @escaping RCTPromiseResolveBlock,
    reject: @escaping RCTPromiseRejectBlock
) {
    DispatchQueue.global(qos: .userInitiated).async {
        // Simulate heavy work
        Thread.sleep(forTimeInterval: 1.0)
        let result = input * 2
        resolve(result)
    }
}
```

## Common Pitfalls

- **Sync methods that block**: Keep under 16ms or make async
- **Forgetting to cancel coroutine scope**: Causes memory leaks
- **Not handling errors in async**: Always try/catch with reject
- **Accessing UI from background**: Dispatch to main thread

## Related Skills

- [native-threading-model.md](./native-threading-model.md) - Thread details
- [native-memory-patterns.md](./native-memory-patterns.md) - Memory in native code
```

## File: `skills/react-native-best-practices/references/native-view-flattening.md`
```markdown
---
title: View Flattening
impact: MEDIUM
tags: views, flattening, collapsable, hierarchy
---

# Skill: View Flattening

Understand and debug React Native's view flattening optimization.

## Quick Pattern

**Problem (children get flattened unexpectedly):**

```jsx
<NativeTabBar>
  <Tab1 />  // May be flattened, breaking native component
  <Tab2 />
</NativeTabBar>
```

**Solution (prevent flattening):**

```jsx
<NativeTabBar>
  <Tab1 collapsable={false} />
  <Tab2 collapsable={false} />
</NativeTabBar>
```

## When to Use

- Native component receives unexpected number of children
- Layout debugging with native components
- Building native components that accept children
- Understanding React Native rendering

> **Note**: This skill involves interpreting visual view hierarchy tools (Xcode Debug View Hierarchy, Android Layout Inspector). AI agents cannot yet process screenshots autonomously. Use this as a guide while reviewing the hierarchy manually, or await MCP-based visual feedback integration (see roadmap).

## What is View Flattening?

React Native's renderer automatically removes "layout-only" views that:
- Only affect layout (no visual rendering)
- Don't need to exist in native view hierarchy

**Benefits**: Reduced memory, faster rendering, shallower view tree.

## The Problem with Native Components

```tsx
// You expect 3 children
<MyNativeComponent>
  <Child1 />
  <Child2 />
  <Child3 />
</MyNativeComponent>
```

If `Child1` is flattened, its internal views become direct children:

```tsx
// Native side receives 5 views instead of 3!
<MyNativeComponent>
  <View />   // Was inside Child1
  <View />   // Was inside Child1  
  <View />   // Was inside Child1
  <Child2 />
  <Child3 />
</MyNativeComponent>
```

## Preventing Flattening with `collapsable`

```tsx
<MyNativeComponent>
  <Child1 collapsable={false} />
  <Child2 collapsable={false} />
  <Child3 collapsable={false} />
</MyNativeComponent>
```

Now native side always receives exactly 3 children.

## Debugging View Hierarchy

![View Hierarchy Flattening](images/view-hierarchy-flattening.png)

Use native debugging tools to see the actual view hierarchy:

### Xcode (iOS)

1. Run app via Xcode
2. Click **"Debug View Hierarchy"** in debug toolbar (shown in image)
3. Inspect 3D view of native hierarchy

**React Native components map to:**
- `<View />` → `RCTViewComponentView`
- `<Text />` → `RCTTextView`

### Android Studio

1. Run app via Android Studio
2. **View → Tool Windows → Layout Inspector**
3. Select running process

**React Native components map to:**
- `<View />` → `ReactViewGroup`
- `<Text />` → `ReactTextView`

## Code Examples

### When Flattening Breaks Your Component

```tsx
// Your native component expects exactly 2 tabs
const NativeTabBar = requireNativeComponent('RCTTabBar');

// BAD: TabContent might get flattened
const MyTabs = () => (
  <NativeTabBar>
    <TabContent title="Home">
      <View><Text>Home content</Text></View>
    </TabContent>
    <TabContent title="Profile">
      <View><Text>Profile content</Text></View>
    </TabContent>
  </NativeTabBar>
);

// GOOD: Prevent flattening
const MyTabs = () => (
  <NativeTabBar>
    <TabContent title="Home" collapsable={false}>
      <View><Text>Home content</Text></View>
    </TabContent>
    <TabContent title="Profile" collapsable={false}>
      <View><Text>Profile content</Text></View>
    </TabContent>
  </NativeTabBar>
);
```

### Wrapper Component with collapsable

```tsx
// Wrapper that prevents flattening
const NativeChildWrapper = ({ children, ...props }) => (
  <View collapsable={false} {...props}>
    {children}
  </View>
);

// Usage
<NativeComponent>
  <NativeChildWrapper>
    <ComplexChild />
  </NativeChildWrapper>
</NativeComponent>
```

## When Views Get Flattened

Views are considered "layout-only" when they:
- Have no `backgroundColor`
- Have no `borderWidth`, `borderColor`
- Have no `shadowColor`, `elevation`
- Don't handle events (no `onPress`, etc.)
- Don't use `opacity` < 1
- Don't have `overflow: 'hidden'`

## Forcing a View to Stay

Besides `collapsable={false}`, these also prevent flattening:

```tsx
// Any of these prevent flattening
<View style={{ backgroundColor: 'transparent' }} />
<View style={{ borderWidth: 0.01 }} />
<View style={{ opacity: 0.99 }} />
<View onLayout={() => {}} />
```

But `collapsable={false}` is the cleanest solution.

## Debugging Checklist

1. **Check native child count**: Log received children in native code
2. **Use Layout Inspector**: Visual hierarchy debugging
3. **Add collapsable={false}**: Test if flattening is the issue
4. **Check wrapper components**: Intermediate views may be flattened

## Common Pitfalls

- **Assuming JS children = native children**: Flattening changes this
- **Not documenting native component requirements**: If your native component expects specific child count, document it
- **Over-using collapsable={false}**: Only use when necessary (loses optimization benefits)

## Related Skills

- [native-platform-setup.md](./native-platform-setup.md) - IDE setup for debugging
- [native-profiling.md](./native-profiling.md) - Performance impact analysis
```

## File: `skills/react-native-brownfield-migration/SKILL.md`
```markdown
---
name: react-native-brownfield-migration
description: Provides an incremental adoption strategy to migrate native iOS or Android apps to React Native or Expo using @callstack/react-native-brownfield for initial setup. Use when planning migration steps, packaging XCFramework/AAR artifacts, and integrating them into host apps.
license: MIT
metadata:
  author: Callstack
  tags: react-native, brownfield, expo, bare, ios, android, xcframework, aar, native-integration
---

# Migrating to React Native

## Overview

Prescriptive workflow for incremental adoption of React Native in existing native apps using `@callstack/react-native-brownfield`, from initial setup through phased host integration.

- Expo track
- Bare React Native track

Use one track per task unless the user explicitly asks for migration or comparison.

## Migration Strategy

Use this strategy for brownfield migration planning and execution:

1. Assess app state and select Expo or bare path.
2. Perform initial setup with `@callstack/react-native-brownfield`.
3. Package RN artifacts (`XCFramework`/`AAR`) from the RN source app.
4. Integrate one RN surface into the host app and validate startup/runtime.
5. Repeat integration by feature/screen for incremental rollout.

## Agent Guardrails (Global)

Apply these rules across all reference files:

1. Select one path first (Expo or bare) and do not mix steps.
2. Use placeholders from the docs (`<framework_target_name>`, `<android_module_name>`, `<registered_module_name>`) and resolve from project files.
3. Validate each packaging command before moving to host integration.
4. Prefer official docs for long platform snippets and CLI option details.
5. Keep host apps isolated from direct React Native APIs when possible (facade approach).

## Canonical Docs

- [Quick Start](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/quick-start.md)
- [Expo Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/expo.md)
- [iOS Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/ios.md)
- [Android Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/android.md)
- [Brownfield CLI](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/cli/brownfield.md)
- [Guidelines](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/guidelines.md)
- [Troubleshooting](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/troubleshooting.md)

## Path Selection Gate (Must Run First)

Before selecting any reference file, classify the project:

1. If no React Native app exists yet, use Expo creation path:
   - [expo-create-app.md][expo-create-app] -> [expo-quick-start.md][expo-quick-start]
2. If React Native app exists, inspect `package.json` and `app.json`:
   - Expo if `expo` is present or Expo plugin workflow is requested.
   - Bare RN if native folders and direct RN CLI workflow are used without Expo path requirements.
3. If still unclear, ask one disambiguation question.
4. Continue with exactly one path.

## When to Apply

Reference this package when:

- Planning incremental migration from native-only apps to React Native or Expo
- Creating brownfield integration flows for Expo or bare React Native projects
- Performing initial setup with `@callstack/react-native-brownfield`
- Generating iOS XCFramework artifacts from a React Native app
- Generating and publishing Android AAR artifacts from a React Native app
- Integrating generated artifacts into host iOS/Android apps

## Quick Reference

| File | Description |
|------|-------------|
| [quick-start.md][quick-start] | Shared preflight and mandatory path-selection gate |
| [expo-create-app.md][expo-create-app] | Scaffold a new Expo app before Expo brownfield setup |
| [expo-quick-start.md][expo-quick-start] | Expo plugin setup and packaging readiness |
| [expo-ios-integration.md][expo-ios-integration] | Expo iOS packaging and host startup integration |
| [expo-android-integration.md][expo-android-integration] | Expo Android packaging, publish, and host integration |
| [bare-quick-start.md][bare-quick-start] | Bare React Native baseline setup |
| [bare-ios-xcframework-generation.md][bare-ios-xcframework-generation] | Bare iOS XCFramework generation |
| [bare-android-aar-generation.md][bare-android-aar-generation] | Bare Android AAR generation and publish |
| [bare-ios-native-integration.md][bare-ios-native-integration] | Bare iOS host integration |
| [bare-android-native-integration.md][bare-android-native-integration] | Bare Android host integration |

## Problem -> Skill Mapping

| Problem | Start With |
|---------|------------|
| Need path decision first | [quick-start.md][quick-start] |
| Need to create a new Expo app for brownfield | [expo-create-app.md][expo-create-app] |
| Need Expo brownfield setup and plugin wiring | [expo-quick-start.md][expo-quick-start] |
| Need Expo iOS brownfield integration | [expo-ios-integration.md][expo-ios-integration] |
| Need Expo Android brownfield integration | [expo-android-integration.md][expo-android-integration] |
| Need bare RN baseline setup | [bare-quick-start.md][bare-quick-start] |
| Need bare RN iOS XCFramework generation | [bare-ios-xcframework-generation.md][bare-ios-xcframework-generation] |
| Need bare RN Android AAR generation/publish | [bare-android-aar-generation.md][bare-android-aar-generation] |
| Need bare RN iOS host integration | [bare-ios-native-integration.md][bare-ios-native-integration] |
| Need bare RN Android host integration | [bare-android-native-integration.md][bare-android-native-integration] |

[quick-start]: references/quick-start.md
[expo-create-app]: references/expo-create-app.md
[expo-quick-start]: references/expo-quick-start.md
[expo-ios-integration]: references/expo-ios-integration.md
[expo-android-integration]: references/expo-android-integration.md
[bare-quick-start]: references/bare-quick-start.md
[bare-ios-xcframework-generation]: references/bare-ios-xcframework-generation.md
[bare-android-aar-generation]: references/bare-android-aar-generation.md
[bare-ios-native-integration]: references/bare-ios-native-integration.md
[bare-android-native-integration]: references/bare-android-native-integration.md
```

## File: `skills/react-native-brownfield-migration/agents/openai.yaml`
```yaml
interface:
  display_name: "React Native Brownfield Migration"
  short_description: "Incremental migration to React Native or Expo using @callstack/react-native-brownfield with strategy and phased integration steps"
  default_prompt: "Use $react-native-brownfield-migration to plan and execute incremental migration from native iOS/Android to React Native or Expo using @callstack/react-native-brownfield, including initial setup, packaging, and phased host integration."
```

## File: `skills/react-native-brownfield-migration/references/bare-android-aar-generation.md`
```markdown
---
title: Bare Android AAR Generation
impact: CRITICAL
tags: react-native, brownfield, bare, android, aar
---

# Skill: Bare Android AAR Generation

Package a bare React Native app into an Android AAR and publish it for native host consumption.

## Quick Command

```bash
npx brownfield package:android --variant release --module-name <android_module_name>
npx brownfield publish:android --module-name <android_module_name>
```

## When to Use

- Building Android artifact from bare RN app
- Publishing AAR for host app dependency resolution

## Prerequisites

- [bare-quick-start.md](./bare-quick-start.md) completed
- Dedicated Android library module exists (`com.android.library`)
- Brownfield Gradle plugin configured
- RN and Hermes dependency versions aligned with `package.json`

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Library module verified
- [ ] Plugin + autolinking configured
- [ ] Publishing configured
- [ ] package:android succeeds
- [ ] publish:android succeeds
- [ ] Host app resolves Maven coordinate
```

1. Verify target module is a library module and will be passed as `--module-name`.
2. Ensure module plugins include:
   - `com.android.library`
   - `org.jetbrains.kotlin.android`
   - `com.facebook.react`
   - `com.callstack.react.brownfield`
   - `maven-publish`
3. Ensure autolinking is enabled in module:

```kotlin
react {
    autolinkLibrariesWithApp()
}
```

4. Add/verify facade bootstrap class in artifact module (host app should call only this facade):

```kotlin
object ReactNativeHostManager {
    fun initialize(application: Application, onJSBundleLoaded: OnJSBundleLoaded? = null) {
        loadReactNative(application)
        val packageList = PackageList(application).packages
        ReactNativeBrownfield.initialize(application, packageList, onJSBundleLoaded)
    }
}
```

5. Package AAR:
   - `npx brownfield package:android --variant release --module-name <android_module_name>`
6. Publish to Maven local:
   - `npx brownfield publish:android --module-name <android_module_name>`
7. Validate host app resolves `groupId:artifactId:version` with `mavenLocal()` enabled.

## Stop Conditions

Proceed only if:

- package and publish commands exit with code `0`
- host app resolves published coordinate

## If Failed

- Re-check module type (`com.android.library`) and module-name flag
- Re-check plugin configuration and `maven-publish`
- Clean/rebuild Android project and retry package/publish
- Do not proceed to runtime integration until coordinate resolution passes

## Canonical Docs

- [Android Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/android.md)
- [Brownfield CLI](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/cli/brownfield.md)
- [Guidelines](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/guidelines.md)
- [Troubleshooting](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/troubleshooting.md)

## Common Pitfalls

- Using app module instead of library module for packaging
- RN/Hermes dependency mismatch vs `package.json`
- Missing `mavenLocal()` in host dependency resolution

## Related Skills

- [bare-quick-start.md](./bare-quick-start.md) - Bare setup prerequisites
- [bare-android-native-integration.md](./bare-android-native-integration.md) - Bare Android host integration
```

## File: `skills/react-native-brownfield-migration/references/bare-android-native-integration.md`
```markdown
---
title: Bare Android Native Integration
impact: HIGH
tags: react-native, brownfield, bare, android, aar
---

# Skill: Bare Android Native Integration

Consume published bare RN AAR in host Android app and verify runtime rendering.

## Quick Command

```kotlin
// settings.gradle.kts
repositories { mavenLocal() }

// app/build.gradle.kts
dependencies { implementation("<groupId>:<artifactId>:<version>") }
```

## When to Use

- Consuming locally published AAR from bare RN artifact module
- Wiring host startup and rendering for RN-powered screens

## Prerequisites

- [bare-android-aar-generation.md](./bare-android-aar-generation.md) completed
- AAR published to local Maven
- Host app Gradle sync is healthy

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Add mavenLocal in host repositories
- [ ] Add dependency coordinate
- [ ] Initialize host runtime
- [ ] Render RN module
```

1. Add `mavenLocal()` in host `dependencyResolutionManagement` repositories.
2. Add published dependency coordinate in app module.
3. Initialize runtime before RN UI creation:

```kotlin
ReactNativeHostManager.initialize(this.application) {
    println("JS bundle loaded")
}
```

4. Render RN UI:
   - `ReactNativeFragment.createReactNativeFragment("<registered_module_name>")`
   - or `ReactNativeBrownfield.shared.createView(...)`
5. Verify host app resolves dependency and RN module renders.

## Stop Conditions

Mark complete only if:

- Gradle sync/build succeeds with published coordinate
- runtime initializes before UI creation
- RN module renders expected screen

## If Failed

- Re-check coordinate and repository order
- Re-package and re-publish if artifact is stale
- Re-check module name registration in JS

## Canonical Docs

- [Android Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/android.md)
- [Guidelines](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/guidelines.md)
- [Troubleshooting](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/troubleshooting.md)

## Common Pitfalls

- Missing `mavenLocal()`
- Dependency coordinate mismatch
- Creating RN UI before host manager initialization

## Related Skills

- [bare-android-aar-generation.md](./bare-android-aar-generation.md) - Bare Android artifact generation
- [bare-quick-start.md](./bare-quick-start.md) - Bare setup prerequisites
```

## File: `skills/react-native-brownfield-migration/references/bare-ios-native-integration.md`
```markdown
---
title: Bare iOS Native Integration
impact: HIGH
tags: react-native, brownfield, bare, ios, swiftui, appdelegate
---

# Skill: Bare iOS Native Integration

Integrate bare RN XCFramework artifacts into native iOS host app and verify startup/runtime behavior.

## Quick Command

```swift
ReactNativeBrownfield.shared.bundle = ReactNativeBundle
ReactNativeBrownfield.shared.startReactNative { print("React Native bundle loaded") }
```

## When to Use

- Consuming generated bare RN XCFrameworks in host iOS app
- Wiring runtime initialization for UIKit or SwiftUI entrypoints

## Prerequisites

- [bare-ios-xcframework-generation.md](./bare-ios-xcframework-generation.md) completed
- Artifacts available in package output (`ios/.brownfield/package` or `.brownfield/ios/package`)
- Host app builds in Xcode

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Link generated frameworks
- [ ] Initialize RN startup
- [ ] Render registered module
- [ ] Verify Debug and Release behavior
```

1. Link these frameworks into host app:
   - `<framework_target_name>.xcframework`
   - `ReactBrownfield.xcframework`
   - `hermesvm.xcframework` (or `hermes.xcframework` for older RN)
2. In app startup:

```swift
import <framework_target_name>

ReactNativeBrownfield.shared.bundle = ReactNativeBundle
ReactNativeBrownfield.shared.startReactNative(onBundleLoaded: {
    print("React Native bundle loaded")
}, launchOptions: launchOptions)
```

3. Render RN UI with JS-registered module name:
   - UIKit: `ReactNativeViewController(moduleName: "<registered_module_name>")`
   - SwiftUI: `ReactNativeView(moduleName: "<registered_module_name>")`
4. Validate:
   - Debug with Metro (`npx react-native start`)
   - Release without Metro

## Stop Conditions

Mark complete only if:

- host app builds in Debug and Release
- RN module renders in both configurations

## If Failed

- Re-check startup order: set bundle -> start runtime -> create RN view/controller
- Re-check `moduleName` matches `AppRegistry.registerComponent`
- Re-link all required frameworks if Release cannot load JS

## Canonical Docs

- [iOS Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/ios.md)
- [Swift API](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/api-reference/react-native-brownfield/swift.md)
- [Troubleshooting](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/troubleshooting.md)

## Common Pitfalls

- Missing `ReactNativeBrownfield.shared.bundle = ReactNativeBundle`
- Wrong module name compared to JS registration
- Linking only app XCFramework without brownfield/hermes frameworks

## Related Skills

- [bare-ios-xcframework-generation.md](./bare-ios-xcframework-generation.md) - Bare iOS artifact generation
- [bare-quick-start.md](./bare-quick-start.md) - Bare setup prerequisites
```

## File: `skills/react-native-brownfield-migration/references/bare-ios-xcframework-generation.md`
```markdown
---
title: Bare iOS XCFramework Generation
impact: CRITICAL
tags: react-native, brownfield, bare, ios, xcframework, xcode
---

# Skill: Bare iOS XCFramework Generation

Package a bare React Native app into XCFramework artifacts for native iOS host consumption.

## Quick Command

```bash
npx brownfield package:ios --scheme <framework_target_name> --configuration Release
```

## When to Use

- Building iOS artifacts from a bare RN app
- Rebuilding XCFramework after RN/native dependency updates

## Prerequisites

- [bare-quick-start.md](./bare-quick-start.md) completed
- Framework target exists in `ios/*.xcworkspace`
- Podfile includes framework target with `inherit! :complete`
- If running `pod install` directly, static linking is configured as recommended in iOS integration docs
- Framework target build settings:
  - Build Libraries for Distribution = `YES`
  - User Script Sandboxing = `NO`
  - Skip Install = `NO`
  - Enable Module Verifier = `NO`

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Framework target + Podfile ready
- [ ] Bundle script present on framework target
- [ ] Public interface file exports ReactBrownfield
- [ ] package:ios succeeds
- [ ] Artifacts validated
```

1. Create or verify framework target in Xcode workspace.
   - If target folders are folder references, convert them to groups (per iOS integration docs).
2. Ensure Podfile has nested framework target and run `pod install`.
3. Ensure framework target includes `Bundle React Native code and images` run script with expected input files (`$(SRCROOT)/.xcode.env.local`, `$(SRCROOT)/.xcode.env`).
4. Add framework interface file:

```swift
@_exported import ReactBrownfield
public let ReactNativeBundle = Bundle(for: InternalClassForBundle.self)
class InternalClassForBundle {}
```

5. Package framework:
   - `npx brownfield package:ios --scheme <framework_target_name> --configuration Release`
6. Validate output directory produced by command (commonly `ios/.brownfield/package` or `.brownfield/ios/package`):
   - `<framework_target_name>.xcframework`
   - `ReactBrownfield.xcframework`
   - `hermesvm.xcframework` (or `hermes.xcframework` for older RN)

## Stop Conditions

Proceed only if:

- package command exits with code `0`
- all required frameworks are present in package output

## If Failed

- Re-run pods and retry package command
- Re-check framework target build settings and run script phase
- Do not proceed to host integration until artifacts are complete

## Canonical Docs

- [iOS Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/ios.md)
- [Brownfield CLI](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/cli/brownfield.md)
- [Troubleshooting](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/guides/troubleshooting.md)

## Common Pitfalls

- Packaging app target instead of framework target
- Missing bundle run script on framework target
- Incomplete framework set linked into host app

## Related Skills

- [bare-quick-start.md](./bare-quick-start.md) - Bare setup prerequisites
- [bare-ios-native-integration.md](./bare-ios-native-integration.md) - Bare iOS host integration
```

## File: `skills/react-native-brownfield-migration/references/bare-quick-start.md`
```markdown
---
title: Bare React Native Quick Start
impact: CRITICAL
tags: react-native, brownfield, bare, setup, cocoapods, gradle
---

# Skill: Bare React Native Quick Start

Prepare a bare React Native project for brownfield packaging and host integration.

## Quick Command

```bash
npm install @callstack/react-native-brownfield
cd ios && pod install && cd ..
```

## When to Use

- User explicitly chooses bare React Native path
- Project directly manages native iOS/Android folders

## Prerequisites

- Bare RN app with working `ios/` and `android/`
- CocoaPods and Gradle working

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Install package
- [ ] Install pods
- [ ] Continue to bare platform packaging
```

1. Install package in RN app root.
2. Run `pod install` for iOS.
3. Continue with one platform packaging file:
   - [bare-ios-xcframework-generation.md](./bare-ios-xcframework-generation.md)
   - [bare-android-aar-generation.md](./bare-android-aar-generation.md)

## Canonical Docs

- [Quick Start](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/quick-start.md)
- [iOS Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/ios.md)
- [Android Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/android.md)

## Common Pitfalls

- Starting packaging before `pod install`
- Mixing Expo-only startup APIs into bare flow

## Related Skills

- [quick-start.md](./quick-start.md) - Shared path-selection gate
- [bare-ios-xcframework-generation.md](./bare-ios-xcframework-generation.md) - Bare iOS artifact generation
- [bare-android-aar-generation.md](./bare-android-aar-generation.md) - Bare Android artifact generation
```

## File: `skills/react-native-brownfield-migration/references/expo-android-integration.md`
```markdown
---
title: Expo Android Integration
impact: HIGH
tags: react-native, brownfield, expo, android, aar, reactnativehostmanager
---

# Skill: Expo Android Integration

Package and publish Expo Android AAR, then initialize host runtime and mount RN UI.

## Quick Command

```bash
npx brownfield package:android --module-name <android_module_name> --variant release
npx brownfield publish:android --module-name <android_module_name>
```

## When to Use

- User requests Expo Android brownfield integration
- Host app must consume Expo-backed RN AAR

## Prerequisites

- [expo-quick-start.md](./expo-quick-start.md) completed
- Android host app builds and syncs
- Android module name resolved (`brownfieldlib` by default unless overridden in Expo plugin options)

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Package AAR
- [ ] Publish to Maven local
- [ ] Initialize host runtime
- [ ] Render RN module
```

1. Build AAR:
   - `npx brownfield package:android --module-name <android_module_name> --variant release`
2. Publish to Maven local:
   - `npx brownfield publish:android --module-name <android_module_name>`
3. Initialize runtime in `Activity` or `Application`:

```kotlin
ReactNativeHostManager.initialize(application) {
  Toast.makeText(this, "React Native has been loaded", Toast.LENGTH_LONG).show()
}
```

4. Forward configuration changes:

```kotlin
override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)
    ReactNativeHostManager.onConfigurationChanged(application, newConfig)
}
```

5. Render RN UI with JS-registered module name:
   - `ReactNativeFragment.createReactNativeFragment("<registered_module_name>")`
   - or `ReactNativeBrownfield.shared.createView(context, activity, "<registered_module_name>")`

## Stop Conditions

Mark complete only if:

- package and publish commands both exit with code `0`
- host app resolves published dependency and renders module

## Canonical Docs

- [Expo Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/expo.md)
- [Android Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/android.md)
- [Brownfield CLI](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/cli/brownfield.md)

## Common Pitfalls

- Using `ComponentActivity` with Expo (use `AppCompatActivity`)
- Missing `ReactNativeHostManager.initialize(...)` before UI creation
- Module name mismatch with `AppRegistry.registerComponent`

## Related Skills

- [expo-quick-start.md](./expo-quick-start.md) - Expo setup and plugin wiring
- [expo-ios-integration.md](./expo-ios-integration.md) - Expo iOS equivalent
```

## File: `skills/react-native-brownfield-migration/references/expo-create-app.md`
```markdown
---
title: Expo Create App for Brownfield
impact: CRITICAL
tags: react-native, brownfield, expo, create-app, setup
---

# Skill: Expo Create App for Brownfield

Create a new Expo app as the source project for Expo brownfield packaging and host integration.

## Quick Command

```bash
npx create-expo-app@latest my-expo-brownfield --yes
```

## When to Use

- User wants to add React Native to native apps via Expo path
- No existing Expo/RN project is available for brownfield packaging

## Prerequisites

- Node.js and `npx` available
- New project directory name selected

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Create Expo app
- [ ] Install brownfield package
- [ ] Continue on Expo-only path
```

1. Create a new Expo app in a standalone directory (not inside existing iOS/Android host repo).
2. `cd my-expo-brownfield`
3. Install brownfield package: `npm install @callstack/react-native-brownfield`
4. Continue to [expo-quick-start.md](./expo-quick-start.md).

## Stop Conditions

Proceed only if:

- create command exits with code `0`
- `app.json` exists at project root

## Canonical Docs

- [Expo Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/expo.md)
- [Quick Start](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/quick-start.md)

## Common Pitfalls

- Creating Expo app inside host native app project
- Jumping to iOS/Android integration before Expo plugin setup

## Related Skills

- [quick-start.md](./quick-start.md) - Path-selection gate
- [expo-quick-start.md](./expo-quick-start.md) - Expo plugin and packaging setup
```

## File: `skills/react-native-brownfield-migration/references/expo-ios-integration.md`
```markdown
---
title: Expo iOS Integration
impact: HIGH
tags: react-native, brownfield, expo, ios, xcframework, swiftui, appdelegate
---

# Skill: Expo iOS Integration

Package Expo app as XCFramework artifacts, link them into host iOS app, and initialize Expo-compatible RN runtime.

## Quick Command

```bash
npx brownfield package:ios --scheme <framework_target_name> --configuration Release
```

## When to Use

- User requests Expo iOS brownfield integration
- Host app must render Expo-backed React Native UI

## Prerequisites

- [expo-quick-start.md](./expo-quick-start.md) completed
- iOS host app builds successfully
- Framework scheme name resolved (`BrownfieldLib` by default unless overridden in Expo plugin options)

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Package XCFrameworks
- [ ] Link frameworks in host app
- [ ] Configure startup
- [ ] Render RN module
```

1. Package iOS artifacts:
   - `npx brownfield package:ios --scheme <framework_target_name> --configuration Release`
2. Link artifacts from package output directory (`ios/.brownfield/package` or `.brownfield/ios/package`) into host app project:
   - `<framework_target_name>.xcframework`
   - `ReactBrownfield.xcframework`
   - `hermesvm.xcframework` (or `hermes.xcframework` for older RN)
3. Initialize runtime in app entrypoint:

```swift
ReactNativeBrownfield.shared.bundle = ReactNativeBundle
ReactNativeBrownfield.shared.startReactNative {
    print("React Native has been loaded")
}
ReactNativeBrownfield.shared.ensureExpoModulesProvider()
```

4. Forward `didFinishLaunchingWithOptions` to brownfield handler.
5. Render RN UI using the module registered in JS (`AppRegistry.registerComponent`):
   - `ReactNativeView(moduleName: "<registered_module_name>")`
   - or `ReactNativeBrownfield.shared.view(moduleName: "<registered_module_name>", initialProps: nil)`

## Stop Conditions

Mark complete only if:

- package command exits with code `0`
- host app builds in Debug and Release
- selected module renders successfully

## Canonical Docs

- [Expo Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/expo.md)
- [iOS Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/ios.md)
- [Swift API](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/api-reference/react-native-brownfield/swift.md)

## Common Pitfalls

- Missing `ensureExpoModulesProvider()` in Expo startup flow
- Not forwarding `didFinishLaunchingWithOptions`
- Using wrong module name instead of JS-registered component name

## Related Skills

- [expo-quick-start.md](./expo-quick-start.md) - Expo setup and plugin wiring
- [expo-android-integration.md](./expo-android-integration.md) - Expo Android equivalent
```

## File: `skills/react-native-brownfield-migration/references/expo-quick-start.md`
```markdown
---
title: Expo Brownfield Quick Start
impact: CRITICAL
tags: react-native, brownfield, expo, app.json, plugin, setup
---

# Skill: Expo Brownfield Quick Start

Configure Expo project for brownfield packaging before iOS/Android host integration.

## Quick Command

```bash
npm install @callstack/react-native-brownfield
```

## When to Use

- Expo managed or prebuild project needs brownfield packaging
- Continuing after [expo-create-app.md](./expo-create-app.md)

## Prerequisites

- Expo project with `app.json`
- Expo path selected in router

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Install package
- [ ] Configure plugin
- [ ] Continue to platform integration
```

1. Install package in the Expo project.
2. Add plugin to `app.json`:

```json
{
  "plugins": ["@callstack/react-native-brownfield"]
}
```

3. Optionally add package scripts for packaging/publish commands used by your team.
4. Continue to exactly one platform file:
   - [expo-ios-integration.md](./expo-ios-integration.md)
   - [expo-android-integration.md](./expo-android-integration.md)

## Canonical Docs

- [Expo Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/expo.md)
- [Brownfield CLI](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/cli/brownfield.md)

## Common Pitfalls

- Missing plugin entry in `app.json`
- Mixing Expo flow with bare packaging files

## Related Skills

- [quick-start.md](./quick-start.md) - Path-selection gate
- [expo-ios-integration.md](./expo-ios-integration.md) - Expo iOS integration
- [expo-android-integration.md](./expo-android-integration.md) - Expo Android integration
```

## File: `skills/react-native-brownfield-migration/references/quick-start.md`
```markdown
---
title: Brownfield Quick Start
impact: CRITICAL
tags: react-native, brownfield, setup, path-selection, expo, bare
---

# Skill: Brownfield Quick Start

Run shared setup, select one path (Expo or bare), and route immediately to path-specific instructions.

## Quick Command

```bash
npm install @callstack/react-native-brownfield
```

## When to Use

- Starting brownfield setup and deciding between Expo and bare RN
- Preparing project prerequisites before platform-specific packaging

## Prerequisites

- React Native project root identified
- Node.js and package manager available

## Step-by-Step Instructions

```text
Progress checklist:
- [ ] Install package
- [ ] Select Expo or bare path
- [ ] Continue only on selected path
```

1. Install package in the React Native app root.
2. Classify request/project intent:
   - Expo signals: `expo`, `prebuild`, Expo plugin workflow
   - Bare signals: direct RN CLI workflow, explicit XCFramework/AAR-only path
3. Route to exactly one path:
   - Expo path: [expo-create-app.md](./expo-create-app.md) (if no RN app yet) -> [expo-quick-start.md](./expo-quick-start.md)
   - Bare path: [bare-quick-start.md](./bare-quick-start.md)
4. If unclear, ask one disambiguation question and stop.

## Stop Conditions

Proceed only if:

- package install exits with code `0`
- exactly one path is selected

## If Failed

- If install fails, retry with the active package manager and lockfile sync
- If path intent is ambiguous, stop and ask one Expo vs bare question

## Canonical Docs

- [Quick Start](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/quick-start.md)
- [Expo Integration](https://oss.callstack.com/react-native-brownfield/brain/knowledge/docs_legacy/getting-started/expo.md)

## Common Pitfalls

- Mixing Expo and bare steps in one flow
- Starting platform integration before path selection

## Related Skills

- [expo-create-app.md](./expo-create-app.md) - Create new Expo app for brownfield
- [expo-quick-start.md](./expo-quick-start.md) - Expo setup and plugin wiring
- [bare-quick-start.md](./bare-quick-start.md) - Bare RN baseline setup
```

## File: `skills/upgrading-react-native/SKILL.md`
```markdown
---
name: upgrading-react-native
description: Upgrades React Native apps to newer versions by applying rn-diff-purge template diffs, updating package.json dependencies, migrating native iOS and Android configuration, resolving CocoaPods and Gradle changes, and handling breaking API updates. Use when upgrading React Native, bumping RN version, updating from RN 0.x to 0.y, or migrating Expo SDK alongside a React Native upgrade.
license: MIT
metadata:
  author: Callstack
  tags: react-native, upgrade, upgrade-helper, npm, changelog, cocoapods, ios, android
---

# Upgrading React Native

## Overview

Covers the full React Native upgrade workflow: template diffs via Upgrade Helper, dependency updates, Expo SDK steps, and common pitfalls.

## Typical Upgrade Sequence

1. **Route**: Choose the right upgrade path via [upgrading-react-native.md][upgrading-react-native]
2. **Diff**: Fetch the canonical template diff using Upgrade Helper via [upgrade-helper-core.md][upgrade-helper-core]
3. **Dependencies**: Assess and update third-party packages via [upgrading-dependencies.md][upgrading-dependencies]
4. **React**: Align React version if upgraded via [react.md][react]
5. **Expo** (if applicable): Apply Expo SDK layer via [expo-sdk-upgrade.md][expo-sdk-upgrade]
6. **Verify**: Run post-upgrade checks via [upgrade-verification.md][upgrade-verification]

```bash
# Quick start: detect current version and fetch diff
npm pkg get dependencies.react-native --prefix "$APP_DIR"
npm view react-native dist-tags.latest

# Example: upgrading from 0.76.9 to 0.78.2
# 1. Fetch the template diff
curl -L -f -o /tmp/rn-diff.diff \
  "https://raw.githubusercontent.com/react-native-community/rn-diff-purge/diffs/diffs/0.76.9..0.78.2.diff" \
  && echo "Diff downloaded OK" || echo "ERROR: diff not found, check versions"
# 2. Review changed files
grep -n "^diff --git" /tmp/rn-diff.diff
# 3. Update package.json, apply native changes, then install + rebuild
npm install --prefix "$APP_DIR"
cd "$APP_DIR/ios" && pod install
# 4. Validate: both platforms must build successfully
npx react-native build-android --mode debug --no-packager
xcodebuild -workspace "$APP_DIR/ios/App.xcworkspace" -scheme App -sdk iphonesimulator build
```

## When to Apply

Reference these guidelines when:
- Moving a React Native app to a newer version
- Reconciling native config changes from Upgrade Helper
- Validating release notes for breaking changes

## Quick Reference

| File | Description |
|------|-------------|
| [upgrading-react-native.md][upgrading-react-native] | Router: choose the right upgrade path |
| [upgrade-helper-core.md][upgrade-helper-core] | Core Upgrade Helper workflow and reliability gates |
| [upgrading-dependencies.md][upgrading-dependencies] | Dependency compatibility checks and migration planning |
| [react.md][react] | React and React 19 upgrade alignment rules |
| [expo-sdk-upgrade.md][expo-sdk-upgrade] | Expo SDK-specific upgrade layer (conditional) |
| [upgrade-verification.md][upgrade-verification] | Manual post-upgrade verification checklist |
| [monorepo-singlerepo-targeting.md][monorepo-singlerepo-targeting] | Monorepo and single-repo app targeting and command scoping |

## Problem → Skill Mapping

| Problem | Start With |
|---------|------------|
| Need to upgrade React Native | [upgrade-helper-core.md][upgrade-helper-core] |
| Need dependency risk triage and migration options | [upgrading-dependencies.md][upgrading-dependencies] |
| Need React/React 19 package alignment | [react.md][react] |
| Need workflow routing first | [upgrading-react-native.md][upgrading-react-native] |
| Need Expo SDK-specific steps | [expo-sdk-upgrade.md][expo-sdk-upgrade] |
| Need manual regression validation | [upgrade-verification.md][upgrade-verification] |
| Need repo/app command scoping | [monorepo-singlerepo-targeting.md][monorepo-singlerepo-targeting] |

[upgrading-react-native]: references/upgrading-react-native.md
[upgrade-helper-core]: references/upgrade-helper-core.md
[upgrading-dependencies]: references/upgrading-dependencies.md
[react]: references/react.md
[expo-sdk-upgrade]: references/expo-sdk-upgrade.md
[upgrade-verification]: references/upgrade-verification.md
[monorepo-singlerepo-targeting]: references/monorepo-singlerepo-targeting.md
```

## File: `skills/upgrading-react-native/agents/openai.yaml`
```yaml
interface:
  display_name: "Upgrade React Native"
  short_description: "React Native upgrade workflow updated templates, dependencies, and common pitfalls"
  default_prompt: "Use $upgrading-react-native to plan and execute a React Native upgrade."
```

## File: `skills/upgrading-react-native/references/expo-sdk-upgrade.md`
```markdown
---
title: Expo SDK Upgrade Layer
impact: HIGH
tags: expo, sdk, react-native, dependencies
---

# Skill: Expo SDK Upgrade Layer

Expo-specific add-on to the core Upgrade Helper workflow. Use only when `expo` exists in app `package.json`.

## Quick Commands

```bash
npm pkg get dependencies.expo devDependencies.expo --prefix "$APP_DIR"
cd "$APP_DIR" && npx expo install --fix
cd "$APP_DIR" && npx expo-doctor
```

## When to Apply

- `expo` or `expo-updates` is present in the target app package
- RN upgrade is paired with Expo SDK upgrade

## Official Expo Reference

- Follow Expo's official upgrade skill as a primary guide:
  - [Expo Upgrading Expo Skill][expo-upgrading-expo-skill]
- Important for this workflow: skip `app.json` changes, because this is not an Expo Managed project.

## Pre-Upgrade Audit (Required)

- Confirm SDK version and target path.
- Inventory dependencies and native modules.
- Review config plugins and prebuild behavior.
- Review native build setup (Gradle, iOS settings, CI/EAS config).
- Identify critical app flows for regression testing before changes.

## Workflow Additions

1. Run Expo compatibility alignment.
   - `npx expo install --fix` (source of truth for SDK-compatible versions).
   - Treat `expo-modules` package versions as SDK-coupled; align them with Expo recommendations.
2. Run health checks.
   - `npx expo-doctor`; resolve blocking issues first.
3. If native folders are part of workflow, reconcile prebuild output.
   - `npx expo prebuild --clean` (when applicable).
4. Handle React 19 pairing.
   - Run [react.md](react.md).
5. Run [upgrade-verification.md](upgrade-verification.md) for manual regression checks and release gates.

## Notes

- Use `npx expo ...`; do not require global `expo-cli`.
- Some package bumps may be optional if not SDK-bound; validate before deferring.
- Read Expo and React Native release notes deeply before editing code, then map each breaking change to a concrete code/task item.

## Related Skills

- [upgrading-react-native.md](upgrading-react-native.md) - Routing and mode selection
- [upgrade-helper-core.md](upgrade-helper-core.md) - Base upgrade workflow
- [react.md](react.md) - React and React 19 alignment
- [upgrade-verification.md](upgrade-verification.md) - Manual post-upgrade validation
- [monorepo-singlerepo-targeting.md](monorepo-singlerepo-targeting.md) - Repo/app selection and command scoping

[expo-upgrading-expo-skill]: https://github.com/expo/skills/blob/main/plugins/upgrading-expo/skills/upgrading-expo/SKILL.md
```

## File: `skills/upgrading-react-native/references/monorepo-singlerepo-targeting.md`
```markdown
---
title: Monorepo vs Single-App Targeting
impact: HIGH
tags: monorepo, workspace, react-native, app-selection
---

# Skill: Monorepo vs Single-App Targeting

Small instruction set for selecting the correct app package and running upgrade commands in the right scope.

## Quick Commands

```bash
APP_DIR=apps/mobile
npm pkg get dependencies.react-native devDependencies.react-native --prefix "$APP_DIR"
```

## Rules

1. Pick one target app package before any upgrade command.
2. Run all app-specific commands with `--prefix "$APP_DIR"` or from `cd "$APP_DIR"`.
3. Use `APP_DIR=.` for single-package repos.
4. Never apply diffs to workspace root when RN app lives in a subpackage.

## Verification

- `react-native` is present in `APP_DIR/package.json`.
- `ios/` and `android/` paths used for build/pods are under `APP_DIR`.

## Related Skills

- [upgrading-react-native.md](upgrading-react-native.md) - Routing and mode selection
- [upgrade-helper-core.md](upgrade-helper-core.md) - Base upgrade workflow
- [expo-sdk-upgrade.md](expo-sdk-upgrade.md) - Expo-specific steps
```

## File: `skills/upgrading-react-native/references/react.md`
```markdown
---
title: React Upgrade Layer
impact: HIGH
tags: react, react-19, rntl, types
---

# Skill: React Upgrade Layer

React-specific upgrade rules to run when `react` changes during a React Native or Expo upgrade.

## When to Apply

- `react` version changes (major, minor, or patch).
- React Native target implies a newer React pairing.
- Tests/types break after React upgrade.

## React Pairing Rules

1. Keep companion packages aligned with installed React version:
   - `react-test-renderer`
   - `@types/react`
   - `react-dom` (if used by the app)
2. Prefer matching React major and minor exactly; patch should also match when available.
3. Do not leave these packages on older `x.y` after upgrading `react`.

## React 19 Rules

1. Upgrade `@testing-library/react-native` to `v13+`.
2. Follow:
   - [Expo React 19 Reference][expo-react-19-reference]
   - [RNTL LLM Docs][rntl-llm-docs]
3. Expect type-level breakages from deprecated API removals; fix code and mocks accordingly.

## Related Skills

- [upgrade-helper-core.md](upgrade-helper-core.md) - Core RN upgrade workflow
- [upgrading-dependencies.md](upgrading-dependencies.md) - Dependency compatibility triage
- [expo-sdk-upgrade.md](expo-sdk-upgrade.md) - Expo-specific upgrade layer
- [upgrade-verification.md](upgrade-verification.md) - Post-upgrade manual validation

[expo-react-19-reference]: https://github.com/expo/skills/blob/main/plugins/upgrading-expo/skills/upgrading-expo/references/react-19.md
[rntl-llm-docs]: https://oss.callstack.com/react-native-testing-library/llms.txt
```

## File: `skills/upgrading-react-native/references/upgrade-helper-core.md`
```markdown
---
title: Upgrade Helper Core Workflow
impact: HIGH
tags: react-native, upgrade-helper, rn-diff-purge, ios, android
---

# Skill: Upgrade Helper Core Workflow

Reliable, framework-agnostic workflow for React Native upgrades using Upgrade Helper and rn-diff-purge.

Run shared environment checks first in [upgrading-react-native.md](upgrading-react-native.md) under `Prerequisites (All Upgrade Paths)`.

## Quick Commands

```bash
npm pkg get dependencies.react-native devDependencies.react-native --prefix "$APP_DIR"
npm view react-native dist-tags.latest
curl -L "https://raw.githubusercontent.com/react-native-community/rn-diff-purge/master/RELEASES"
curl -L -o /tmp/rn-diff-<current_version>..<target_version>.diff "https://raw.githubusercontent.com/react-native-community/rn-diff-purge/diffs/diffs/<current_version>..<target_version>.diff"
grep -n "^diff --git" /tmp/rn-diff-<current_version>..<target_version>.diff
```

## Upgrade Helper API (Inline Reference)

- List supported versions:
  - `https://raw.githubusercontent.com/react-native-community/rn-diff-purge/master/RELEASES`
- Fetch raw unified diff:
  - `https://raw.githubusercontent.com/react-native-community/rn-diff-purge/diffs/diffs/<current_version>..<target_version>.diff`
- GitHub compare view:
  - `https://github.com/react-native-community/rn-diff-purge/compare/release/<current_version>..release/<target_version>`
- Upgrade Helper UI:
  - `https://react-native-community.github.io/upgrade-helper/?from=<current_version>&to=<target_version>`
- Path mapping note:
  - Diff paths are prefixed with `RnDiffApp/`; remap to your app paths and package names.

## Inputs

- `APP_DIR`: app package path (`.` for single-package repos)
- `current_version`: current React Native version
- `target_version`: target React Native version (latest by default)

## Reliable Workflow

1. Detect app and versions.
   - Read `react-native` from `APP_DIR/package.json`.
   - Resolve target via `npm view react-native dist-tags.latest` unless user provides one.
2. Validate `target_version` exists.
   - Check `RELEASES` from rn-diff-purge and confirm `target_version` is listed.
   - If missing, stop and ask user to choose one of available versions.
3. Collect canonical sources.
   - Upgrade Helper URL.
   - rn-diff-purge raw diff.
4. Fetch diff with fallback.
   - Try exact raw diff: `<current_version>..<target_version>`.
   - If 404, try nearest available patch versions and report what was attempted.
   - If no available pair works, stop and ask user for target adjustment.
5. Build dependency baseline from rn-diff-purge first.
   - Start with the `RnDiffApp/package.json` diff for the exact version pair.
   - Do not manually install RN packages one-by-one before this baseline is captured.
6. Publish a short execution plan before edits.
   - Include ordered phases: dependency baseline, one-pass install, native/tooling merges, verification.
   - If dependency migrations are ambiguous, ask for user confirmation before modifying package choices.
7. Run dependency risk planning.
   - Use [upgrading-dependencies.md](upgrading-dependencies.md).
   - Fold approved migrations into the same dependency update pass.
8. Apply dependency updates in one pass.
   - Update `APP_DIR/package.json` (and lockfile) from the baseline plus approved migrations.
   - Run exactly one install command with the repo's package manager (`npm install`, `yarn install`, `pnpm install`, or `bun install`).
   - Avoid piecemeal installs such as repeated `npm install <pkg>` unless explicitly requested.
9. Build a change checklist from diff.
   - Group by JS/TS, iOS, Android, tooling.
   - Skip template-only UI (`App.tsx`) unless explicitly requested.
   - Skip template-only dependencies (`@react-native/new-app-screen`) unless they exist in the app.
10. Apply diff safely.
   - Treat `RnDiffApp` as placeholder; remap app/package names.
   - Merge, do not overwrite project-specific customizations.
11. Sync native deps.
   - Run iOS pods in `APP_DIR/ios`.
12. Validate and gate completion.
   - iOS build passes.
   - Android build passes.
   - tests/typecheck/lint pass or failures are documented with next actions.
   - If `react` was upgraded, run [react.md](react.md).
   - If `target_version >= 0.81` and tests fail due to missing modules, add proper mocks.
     - Example (`BackHandler` mock removal): https://github.com/facebook/react-native/issues/52667#issuecomment-3094788618
   - Run [upgrade-verification.md](upgrade-verification.md) before closing the upgrade.

## Stop Conditions

- Missing `react-native` dependency in target package.
- Diff source unavailable and no fallback available.
- Unresolved native merge conflicts in iOS/Android entry files.

## Reliability Rules

- Keep operations version-pair scoped (`current_version -> target_version`).
- Prefer official sources over ad-hoc guides.
- Record every manual deviation from Upgrade Helper.
- Do not run Expo-specific commands here.

## Common Pitfalls

- Upgrading an Expo project with only RN CLI steps: apply the Expo layer ([expo-sdk-upgrade.md](expo-sdk-upgrade.md)).
- Skipping the Upgrade Helper: leads to missed native config changes.
- Treating `RnDiffApp` paths as literal project paths.
- Copying the entire template wholesale: use the diff as a guide and merge only needed changes.
- Using the wrong changelog: `0.7x` changes live in `CHANGELOG-0.7x.md`.
- Running the wrong package manager: always match the repo lockfile.
- Forgetting CocoaPods: iOS builds will fail without `pod install`.
- Not updating Android Gradle wrapper binary: update `android/gradle/wrapper/gradle-wrapper.jar` for the target RN version. Source template:
  - `https://raw.githubusercontent.com/react-native-community/rn-diff-purge/release/<target_version>/RnDiffApp/android/gradle/wrapper/gradle-wrapper.jar`
- Flipper artifacts lingering after removal in v0.74: remove `ReactNativeFlipper.kt` and `FLIPPER_VERSION` when the target RN version drops Flipper.
- Skipping platform rebuilds after Pod/Gradle changes.

## Related Skills

- [upgrading-react-native.md](upgrading-react-native.md) - Routing and mode selection
- [upgrading-dependencies.md](upgrading-dependencies.md) - Dependency compatibility and migration plan
- [expo-sdk-upgrade.md](expo-sdk-upgrade.md) - Expo-only layer on top of core workflow
- [react.md](react.md) - React and React 19 alignment
- [upgrade-verification.md](upgrade-verification.md) - Manual post-upgrade validation
- [monorepo-singlerepo-targeting.md](monorepo-singlerepo-targeting.md) - Repo/app selection and command scoping
```

## File: `skills/upgrading-react-native/references/upgrade-verification.md`
```markdown
---
title: Upgrade Verification
impact: HIGH
tags: verification, regression, android, ios, navigation
---

# Skill: Upgrade Verification

Manual validation checklist for human developers after React Native and/or Expo upgrades.

## Scope

- Focus on behavior and UX regressions that static diffs cannot prove.
- Keep checks small, repeatable, and tied to critical user flows.

## Manual Checks (Required)

1. App launch and core journeys work on both iOS and Android.
2. Navigation behavior is correct (forward/back stack, params, deep links, modal flows).
3. Android edge-to-edge is visually correct (status bar, nav bar, safe area insets, keyboard overlays).
4. Permissions and device APIs work (camera, location, notifications, file/media access).
5. Background/restore paths work (app resume, push open, interrupted flows).

## Build and Test Gates

1. Run unit/integration tests and fix all upgrade-related failures.
2. If `target_version >= 0.81` and tests fail due to missing modules, add proper mocks.
   - Example (`BackHandler` mock removal): https://github.com/facebook/react-native/issues/52667#issuecomment-3094788618
3. Build installable artifacts for both platforms.
4. For Expo apps, run `npx expo-doctor` from [expo-sdk-upgrade.md](expo-sdk-upgrade.md).

## Evidence to Capture

- Screen recordings/screenshots for changed flows.
- List of verified scenarios and pass/fail status.
- Follow-up fixes for any observed regressions.

## Related Skills

- [upgrading-react-native.md](upgrading-react-native.md) - Upgrade workflow router
- [upgrade-helper-core.md](upgrade-helper-core.md) - Core RN diff/merge workflow
- [expo-sdk-upgrade.md](expo-sdk-upgrade.md) - Expo-specific checks and commands
- [react.md](react.md) - React-specific upgrade rules
```

## File: `skills/upgrading-react-native/references/upgrading-dependencies.md`
```markdown
---
title: Upgrading Dependencies
impact: HIGH
tags: react-native, dependencies, compatibility, migration
---

# Skill: Upgrading Dependencies

Common dependency issues and mitigations when upgrading React Native.

## Quick Checks

```bash
npm ls --depth=0
```

## Dependency Risk and Migration Plan

1. Review compatibility signals:
   - [RN nightly tests](https://react-native-community.github.io/nightly-tests/)
   - [React Native Directory](https://reactnative.directory/packages?newArchitecture=false)
2. If `react` is upgraded, run [react.md](react.md) for companion package alignment and React 19 rules.
3. Handle known risky packages:
   - `react-native-fast-image` -> prefer `@d11/react-native-fast-image` or `expo-image` (confirm with user)
   - `@react-native-cookies/cookies` -> prefer `@preeternal/react-native-cookie-manager` (confirm with user)
   - `react-native-code-push` -> treat as incompatible; disable for upgrade and consider `@appzung/react-native-code-push`, `@bravemobile/react-native-code-push`, or `expo-updates`
   - `react-native-image-crop-picker` -> upgrade to `>=0.51.1`; if unstable, plan migration to `expo-image-picker` (confirm with user)
   - `react-native-network-logger` - lists `react` and `react-native` in peer deps as `*` which can be misleading. Upgrade to v2 if `target_version >= 0.79`.
   - `react-native-permissions` - upgrade to v5 if possible (requires RN 0.74+)
4. Apply additional cleanup rules:
   - If `@rnx-kit/metro-resolver-symlinks` is present, remove it from deps and `metro.config.js` (Metro supports symlinks since 0.72)
   - If app uses `react-native-localize` timezone APIs and `@callstack/timezone-hermes-fix` is missing, ask whether to add it
5. If no safe alternative is found for a critical dependency, ask for explicit user confirmation before continuing.
6. Read only breaking/manual steps from RN blog posts between `current_version` and `target_version`.

## Related Skills

- [upgrade-helper-core.md](upgrade-helper-core.md) - Core upgrade workflow
- [react.md](react.md) - React and React 19 alignment
- [expo-sdk-upgrade.md](expo-sdk-upgrade.md) - Expo-specific dependency alignment
- [upgrading-react-native.md](upgrading-react-native.md) - Routing and mode selection
```

## File: `skills/upgrading-react-native/references/upgrading-react-native.md`
```markdown
---
title: Upgrading React Native
impact: HIGH
tags: react-native, upgrade, routing
---

# Skill: Upgrading React Native

Router for React Native upgrade workflows. Start with core Upgrade Helper instructions, then apply focused add-ons by project shape.

## Prerequisites (All Upgrade Paths)

- Ensure the repo is clean or on a dedicated upgrade branch.
- Know which package manager the repo uses (`npm`, `yarn`, `pnpm`, `bun`).
- Use Node.js `20.19.4+`, Java `17`, and Xcode `16.4+` (with Command Line Tools), following https://reactnative.dev/brain/knowledge/docs_legacy/set-up-your-environment.
  - Optional: use [Xcodes](https://github.com/XcodesOrg/XcodesApp) to manage Xcode versions.
- Verify active versions before upgrading: `node -v`, `java -version`.
- Verify Android Studio is installed.
- For iOS, verify Xcode CLI toolchain is in sync (common pitfall after Xcode upgrades):
  - Check:
    - `xcode-select --print-path`
    - `xcodebuild -version`
    - `xcrun --sdk iphoneos --show-sdk-version`
  - If mismatch is suspected, re-point and initialize:
    - `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`
    - `sudo xcodebuild -runFirstLaunch`

## Quick Start

0. Run the [Prerequisites (All Upgrade Paths)](#prerequisites-all-upgrade-paths) checklist.
1. Set `APP_DIR` to the app folder (`.` for single-app repos).
2. Use [monorepo-singlerepo-targeting.md](monorepo-singlerepo-targeting.md) if you need help choosing `APP_DIR`.
3. Run [upgrade-helper-core.md](upgrade-helper-core.md) first to anchor changes to rn-diff-purge.
4. Publish a short plan (ordered phases) before making versioned edits.
5. Run [upgrading-dependencies.md](upgrading-dependencies.md) to assess risky packages and migrations.
6. Apply dependency updates in one pass and run a single install with the repo package manager.
7. Run [react.md](react.md) when `react` is upgraded.
8. Add [expo-sdk-upgrade.md](expo-sdk-upgrade.md) only if `expo` is present in `APP_DIR/package.json`.
9. Finish with [upgrade-verification.md](upgrade-verification.md).

## Decision Map

- Need canonical RN diff/merge workflow: [upgrade-helper-core.md](upgrade-helper-core.md)
- Need to ensure dependencies are compatible: [upgrading-dependencies.md](upgrading-dependencies.md)
- Need React and React 19 alignment: [react.md](react.md)
- Project contains Expo SDK deps: [expo-sdk-upgrade.md](expo-sdk-upgrade.md)
- Need manual post-upgrade validation: [upgrade-verification.md](upgrade-verification.md)

## Related Skills

- [native-platform-setup.md](../../react-native-best-practices/references/native-platform-setup.md) - Tooling and native dependency basics
- [native-android-16kb-alignment.md](../../react-native-best-practices/references/native-android-16kb-alignment.md) - Third-party library alignment for Google Play
```

