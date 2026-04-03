---
id: vuejs-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.316870
---

# KNOWLEDGE EXTRACT: vuejs-ai
> **Extracted on:** 2026-03-30 18:01:14
> **Source:** vuejs-ai

---

## File: `skills.md`
```markdown
# 📦 vuejs-ai/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/vuejs-ai/skills


## Meta
- **Stars:** ⭐ 2065 | **Forks:** 🍴 110
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent skills for Vue 3 development

## README (trích đầu)
```
# vue-skills

Agent skills for Vue 3 development.

> 🚧 **Early Experiment / Community Project**
>
> This repository is an early experiment in creating specialized skills for AI agents to enhance Vue 3 development. Skills are derived from real-world issues but may be incomplete due to hallucinations—please give feedback. If valuable, I plan to propose transferring this project to the Vue organization to benefit the wider community.

## Installation

```bash
npx skills add vuejs-ai/skills
```

### Claude Code Marketplace

An alternative for Claude Code users:

```bash
# Add marketplace
/plugin marketplace add vuejs-ai/skills

# Install all skills at once
/plugin install vue-skills-bundle@vue-skills

# Install individual skills
/plugin install vue-best-practices@vue-skills

# Install multiple skills
/plugin install vue-best-practices@vue-skills vue-router-best-practices@vue-skills
```

## Usage

For most reliable results, prefix your prompt with `use vue skill`:

```
Use vue skill, <your prompt here>
```

This explicitly triggers the skill and ensures the AI follows the documented patterns. Without the prefix, skill triggering may be inconsistent depending on how closely your prompt matches the skill's description keywords.

## Available Skills

| Skill | When to use | Description |
|-------|-------------|-------------|
| **vue-best-practices** | Vue 3 + Composition API + TypeScript | Best practices, common gotchas, SSR guidance, performance |
| **vue-options-api-best-practices** | Options API (`data()`, `methods`) | `this` context, lifecycle, TypeScript with Options API |
| **vue-router-best-practices** | Vue Router 4 | Navigation guards, route params, route-component lifecycle |
| **vue-pinia-best-practices** | Pinia for state management | Store setup, reactivity, state patterns |
| **vue-testing-best-practices** | Writing component or E2E tests | Vitest, Vue Test Utils, Playwright |
| **vue-jsx-best-practices** | JSX in Vue | Syntax differences from React JSX |
| **vue-debug-guides** | Debugging Vue 3 issues | Runtime errors, warnings, async error handling, hydration issues |
| **create-adaptable-composable** | Creating reusable composables | `MaybeRef`/`MaybeRefOrGetter` input patterns |

## Examples

### vue-best-practices

#### Demo - Todo App

Prompt

```
create a todo app
```

🔎 See demo [full output](https://github.com/vuejs-ai/skills/tree/dev/demo/todo-app).

#### Changes after using skill

- More readable [code](https://github.com/vuejs-ai/skills/tree/dev/demo/todo-app/with-skills/App.vue)
- [Components](https://github.com/vuejs-ai/skills/tree/dev/demo/todo-app/with-skills/components) split
- Moved states into composables ([useTodos.ts](https://github.com/vuejs-ai/skills/tree/dev/demo/todo-app/with-skills/composables/useTodos.ts))
- Use `shallowRef` for primitive reactive data (see [Reactivity](skills/vue-best-practices/references/reactivity.md) reference)

### create-adaptable-composable

Original from `create-agnostic-composable` of [`s
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

