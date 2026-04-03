---
id: callstackincubator-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.186730
---

# KNOWLEDGE EXTRACT: callstackincubator
> **Extracted on:** 2026-03-30 17:31:15
> **Source:** callstackincubator

---

## File: `agent-skills.md`
```markdown
# 📦 callstackincubator/agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/callstackincubator/agent-skills


## Meta
- **Stars:** ⭐ 1085 | **Forks:** 🍴 67
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A collection of agent-optimized React Native skills for AI coding assistants.

## README (trích đầu)
```
# Agent Skills

A collection of agent-optimized skills for AI coding assistants. Skills provide structured, actionable instructions for domain-specific tasks.

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

#### Install as Claude Code Plugin

**1. Add the marketplace:**
```bash
/plugin marketplace add callstackincubator/agent-skills
```

**2. Install the skill:**
```bash
/plugin install react-native-best-practices@callstack-agent-skills
```

Or use the interactive menu:
```bash
/plugin menu
```

**For local development:**
```bash
claude --plugin-dir ./path/to/agent-skills
```

Once installed, Claude will automatically use the React Native best practices skill when working on React Native projects.

#### Use with Other AI Assistants

All major AI coding assistants support the Agent Skills standard.

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

**Usage:** Type `/` in Agent chat to search and select skills by 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

