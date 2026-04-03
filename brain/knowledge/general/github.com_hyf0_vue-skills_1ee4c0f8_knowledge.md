---
id: github.com-hyf0-vue-skills-1ee4c0f8-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:08.800020
---

# KNOWLEDGE EXTRACT: github.com_hyf0_vue-skills_1ee4c0f8
> **Extracted on:** 2026-04-01 07:43:25
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519197/github.com_hyf0_vue-skills_1ee4c0f8

---

## File: `AGENTS.md`
```markdown
# Vue Skills Development Guide

## Branch Strategy

> **IMPORTANT: Never develop on `main` branch!**
>
> - `main` is the **publishing branch** — it only contains released skills
> - `dev` is the **development branch** — all work happens here
> - Use the "Sync to Main" GitHub Action to publish changes from `dev` to `main`

| Branch | Purpose | Direct commits |
|--------|---------|----------------|
| `main` | Publishing (`npx skills add vuejs-ai/skills`) | Forbidden |
| `dev` | Development, tests, experiments | Via PR only |

## Development Workflow

After completing any task, run:

```bash
pnpm typecheck
```

This ensures TypeScript types are correct before committing.

## Skill Scopes

| Skill | Scope |
|-------|-------|
| **vue-best-practices** | Vue 3 with Composition API, `<script setup lang="ts">`, TypeScript, SSR. Includes render functions for cases where templates can't handle the requirement. |
| **vue-options-api-best-practices** | Vue 3 Options API style (`data()`, `methods`, `this` context). Each rule shows Options API solution only. |
| **vue-jsx-best-practices** | JSX syntax in Vue (e.g., `class` vs `className`, JSX plugin config). |
| **vue-testing-best-practices** | Testing with Vitest, Vue Test Utils, and Playwright for E2E. |
| **vue-router-best-practices** | Vue Router 4 patterns, navigation guards, route params, and route-component lifecycle interactions. |
| **vue-pinia-best-practices** | Pinia stores, state management patterns, store setup, and reactivity with stores. |
| **vue-debug-guides** | Debugging and troubleshooting Vue 3: runtime errors, warnings, async error handling, SSR hydration issues. |
| **create-adaptable-composable** | Creating reusable composables with `MaybeRef`/`MaybeRefOrGetter` input patterns. |

## Common Pitfalls & Best Practices

- **Vue-specific only:** Reference files must cover Vue patterns and gotchas, not general web/JS knowledge.
- **No edge cases:** Avoid niche scenarios, tool-specific quirks, and obvious/well-known practices.
- **Required structure:** Each reference file needs title, impact level, task checklist, and incorrect/correct code examples.
- **SKILL.md is for coding agents:** Follow [official best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): be concise (context window is a public good), assume the coding agent is smart (only add what it doesn't know), no hardcoded counts or historical background. Use progressive disclosure — SKILL.md is an overview that points to reference files.

## Checklist for effective Skills

Before sharing a Skill, verify:

### Core quality
- [ ] Description is specific and includes key terms
- [ ] Description includes both what the Skill does and when to use it
- [ ] SKILL.md body is under 500 lines
- [ ] Additional details are in separate files (if needed)
- [ ] No time-sensitive information (or in "old patterns" section)
- [ ] Consistent terminology throughout
- [ ] Examples are concrete, not abstract
- [ ] File references are one level deep
- [ ] Progressive disclosure used appropriately
- [ ] Workflows have clear steps

### Code and scripts
- [ ] Scripts solve problems rather than punt to Claude
- [ ] Error handling is explicit and helpful
- [ ] No "voodoo constants" (all values justified)
- [ ] Required packages listed in instructions and verified as available
- [ ] Scripts have clear documentation
- [ ] No Windows-style paths (all forward slashes)
- [ ] Validation/verification steps for critical operations
- [ ] Feedback loops included for quality-critical tasks

## Evaluating Skills

### Evaluation-Driven Development

Following [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#evaluation-and-iteration):

1. **Create evaluations FIRST** - Before writing extensive documentation
2. **Establish baseline** - Run without skill, document failures
3. **Test with skill** - Run with skill loaded, compare improvement
4. **Iterate** - Refine skill based on evaluation results

### Eval Structure

Each reference file requires 3 evals organized as scenarios:

```
evals/suites/skills/vue-best-practices/
├── computed-vs-methods/           # Reference name
│   ├── scenario-1/                # Eval 1 of 3
│   │   ├── eval.json
│   │   ├── eval.ts
│   │   ├── results.json           # Tracks run results
│   │   └── src/...
│   ├── scenario-2/                # Eval 2 of 3
│   └── scenario-3/                # Eval 3 of 3
```

Each scenario is a self-contained Vue project:

```
evals/suites/skills/vue-best-practices/computed-vs-methods/scenario-1/
├── eval.json           # Eval configuration with query and expected behavior
├── eval.ts             # Vitest assertions (withheld from agent)
├── results.json        # Tracks run results per model
├── package.json        # Self-contained Vue project
├── vite.config.ts
├── tsconfig.json
├── index.html
├── eslint.config.js
└── src/
    ├── main.ts
    ├── App.vue
    ├── vite-env.d.ts
    └── components/
        └── ProductList.vue   # Empty stub component
```

**Key files:**
- `eval.json` - Eval configuration with query, skills, and expected_behavior
- `eval.ts` - Vitest tests that validate the generated code (withheld from agent during generation)
- `results.json` - Tracks run results per model (auto-generated)
- `package.json` - Each suite is self-contained with all dependencies

**eval.json format:**
```json
{
  "skills": ["vue-best-practices"],
  "query": "Create a Vue component that displays a filtered list...",
  "files": ["src/components/ProductList.vue"],
  "expected_behavior": [
    "Uses computed property for filtered list, not a method",
    "Does not call filtering function in template"
  ]
}
```

### Eval Tiers

Each eval runs through 4 tiers to measure skill effectiveness:

| Tier | Prompt | Setup |
|------|--------|-------|
| `baseline` | `[original prompt]` | No skill |
| `with-skill` | `[original prompt]` | Skill installed |
| `with-skill-prompt` | `use vue-best-practices skill, [original prompt]` | Skill installed |
| `with-agents-md` | `[original prompt]` | Skill content embedded in project AGENTS.md |

### Results Tracking

Results are stored in `results.json` within each eval directory. Only the latest result per model is kept. Standalone runs with specific tiers are not recorded.

**results.json format:**
```json
{
  "haiku": {
    "timestamp": "2025-01-29T14:32:05Z",
    "tiers": {
      "baseline": { "passed": true, "duration": 45000 },
      "with-skill": { "passed": true, "duration": 52000 },
      "with-skill-prompt": { "passed": true, "duration": 48000 },
      "with-agents-md": { "passed": true, "duration": 41000 }
    }
  },
  "sonnet": {
    "timestamp": "2025-01-29T15:10:22Z",
    "tiers": {
      "baseline": { "passed": false, "duration": 38000 },
      "with-skill": { "passed": true, "duration": 55000 },
      "with-skill-prompt": { "passed": true, "duration": 51000 },
      "with-agents-md": { "passed": true, "duration": 47000 }
    }
  }
}
```

**Field definitions:**
- Model keys: `haiku`, `sonnet`, `opus` (absent = not run yet)
- `timestamp`: ISO 8601 format with seconds precision
- `duration`: total milliseconds for both runs
- `passed`: true = both runs passed, false = failed on run 1 or 2 (fail fast)

**Run logic (2 runs, fail fast):**
1. Run 1: if fails → stop, record `passed: false`
2. Run 1: if passes → proceed to run 2
3. Run 2: if fails → record `passed: false`
4. Run 2: if passes → record `passed: true`

New runs overwrite previous results for that model.

### Writing eval.ts

Tests validate generated code using **file content pattern matching**:

```typescript
import { expect, test } from "vitest";
import { readFileSync } from "fs";
import { join } from "path";

test("Uses computed property for filtering", () => {
  const content = readFileSync(
    join(process.cwd(), "src/components/Example.vue"),
    "utf-8"
  );

  // Assert pattern SHOULD exist
  expect(content).toMatch(/const\s+\w+\s*=\s*computed\s*\(/);

  // Assert pattern should NOT exist
  expect(content).not.toMatch(/v-for="[^"]*\s+in\s+\w+\(\)"/);
});
```

### Eval Guidelines

1. **Self-contained projects** - Each suite includes all files needed to build
2. **Input stubs must be clean** - No comments, hints, TODOs, or any information suggesting how to solve the task. The query alone should define the work.
3. **Tests read file content** - Use `readFileSync()` to get generated code
4. **Use regex for flexibility** - Match patterns, not exact strings
5. **Test what matters** - Focus on the specific pattern being tested
6. **Binary scoring** - Build + eval.ts tests = Pass/Fail
7. **Multi-model testing** - Test with Haiku, Sonnet, and Opus

### Running Evals

```bash
# Full run - all 4 tiers (skips if results.json exists for model)
pnpm eval computed-vs-methods

# Force re-run even if results exist
pnpm eval computed-vs-methods --force

# Run all missing evals
pnpm eval --all

# Re-run everything
pnpm eval --all --force

# Select model (haiku, sonnet, opus)
pnpm eval computed-vs-methods --model haiku

# Single tier run (for debugging, NOT recorded to results.json)
pnpm eval computed-vs-methods --tier baseline
pnpm eval computed-vs-methods --tier with-skill
pnpm eval computed-vs-methods --tier with-skill-prompt
pnpm eval computed-vs-methods --tier with-agents-md

# Dry run (validate fixtures only, no LLM call)
pnpm eval computed-vs-methods --dry

# Verbose output (keep temp dir, show details)
pnpm eval computed-vs-methods --verbose

# Type check evals library
pnpm --filter @vue-skills/evals typecheck
```

**Skip logic:**
- If `results.json` has an entry for the selected model → skip (unless `--force`)
- Only full runs (all 4 tiers) are recorded
- Single tier runs with `--tier` flag are for debugging and not tracked

### How the Runner Works

1. Copies eval suite to temp directory (excludes eval.ts and eval.json)
2. Installs skill via `npx skills add` (unless `--baseline`)
3. Reads query from eval.json and runs Claude Code with safe tool permissions
4. Copies eval.ts back to temp directory
5. Runs `pnpm install` and `pnpm run build`
6. Runs `vitest run eval.ts`
7. Reports pass/fail based on build + test results

### Available Evals

| Eval | Skill | Tests |
|------|-------|-------|
| `computed-vs-methods` | vue-best-practices | Uses computed() for derived data |
| `no-v-if-with-v-for` | vue-best-practices | Separates v-if and v-for |
| `v-for-key-attribute` | vue-best-practices | Uses :key with unique id |
| `testing-vitest` | vue-testing-best-practices | Uses Vitest + Vue Test Utils |
| `testing-async-flushpromises` | vue-testing-best-practices | Uses flushPromises for async |
| `router-param-change` | vue-router-best-practices | Watches route params |
| `pinia-store-destructuring` | vue-pinia-best-practices | Uses storeToRefs |
| `no-arrow-functions-methods` | vue-options-api-best-practices | Regular function syntax |
| `jsx-vue-vs-react` | vue-jsx-best-practices | Uses class not className |
| `create-composable` | vue-best-practices | Creates reusable composable |

### Full Eval Matrix

Each reference file requires:

3 evals × 4 tiers × 3 models × 2 runs = 72 runs (fail fast)

Example for one reference:
- 3 evals (scenario-1, scenario-2, scenario-3)
- × 4 tiers (baseline, with-skill, with-skill-prompt, with-agents-md)
- × 3 models (haiku, sonnet, opus)
- × 2 runs (both must pass, fail fast on first failure)

Only latest result per model is kept. Re-run with `--force` to update.

### Validation Checklist

Before considering a skill validated:

- [ ] 3 evals per reference file
- [ ] Each eval has results for all 3 models (haiku, sonnet, opus)
- [ ] Each model run covers all 4 tiers (baseline, with-skill, with-skill-prompt, with-agents-md)
- [ ] Results show improvement over baseline
```

## File: `CLAUDE.md`
```markdown
@AGENTS.md
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 hyf0, SerKo <https://github.com/serkodev>

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

Original from `create-agnostic-composable` of [`serkodev/vue-skills`](https://github.com/serkodev/vue-skills/tree/main)

#### Demo - useHidden

Prompt

```
create a reusable composable for controlling hidden for a element
```

🔎 See demo [full output](https://github.com/vuejs-ai/skills/tree/dev/demo/hidden-composable).

#### Changes after using skill

- Used `MaybeRef` and `MaybeRefOrGetter` for input parameters for reactivity flexibility.

```ts
export interface UseHiddenOptions {
  hidden?: MaybeRef<boolean>
  initialHidden?: MaybeRefOrGetter<boolean>
  syncAria?: boolean
}

export function useHidden(
  target?: MaybeRefOrGetter<HTMLElement | null | undefined>,
  options: UseHiddenOptions = {},
)
```

## Methodology

### Skill Types

Skills are classified into two categories:

- **Capability**: AI *cannot* solve the problem without the skill. These address version-specific issues, undocumented behaviors, recent features, or edge cases outside AI's training data.

- **Efficiency**: AI *can* solve the problem but not well. These provide optimal patterns, best practices, and consistent approaches that improve solution quality.

### Validation Process

Each skill rule is validated through automated evals:

1. **Baseline**: Run without skill installed
2. **With-skill**: Run with skill installed

A rule is kept only if it enables the model to solve problems it couldn't solve without it.

| Baseline | With Skill | Action |
|----------|------------|--------|
| Fail | Pass | Keep |
| Pass | Pass | Considered removed |

## Contributing

Development happens on the `dev` branch. The `main` branch is reserved for published skills only.

1. Create a feature branch from `dev`
2. Submit a PR to `dev`
3. After approval, changes are merged to `dev`
4. Maintainers sync `dev` → `main` via GitHub Action when ready to publish

## Related projects

- [antfu/skills](https://github.com/antfu/skills) - Anthony Fu's curated collection of agent skills for Vue/Vite/Nuxt
- [vueuse/vueuse-skills](https://github.com/vueuse/vueuse-skills) - Agent skills for VueUse development
- [onmax/nuxt-skills](https://github.com/onmax/nuxt-skills) - Agent skills for Nuxt development

## License

MIT
```

## File: `skills/create-adaptable-composable/SKILL.md`
```markdown
---
name: create-adaptable-composable
description: Create a library-grade Vue composable that accepts maybe-reactive inputs (MaybeRef / MaybeRefOrGetter) so callers can pass a plain value, ref, or getter. Normalize inputs with toValue()/toRef() inside reactive effects (watch/watchEffect) to keep behavior predictable and reactive. Use this skill when user asks for creating adaptable or reusable composables.
license: MIT
metadata:
  author: github.com/vuejs-ai
  version: "17.0.0"
compatibility: Requires Vue 3 (or above) or Nuxt 3 (or above) project
---

# Create Adaptable Composable

Adaptable composables are reusable functions that can accept both reactive and non-reactive inputs. This allows developers to use the composable in a variety of contexts without worrying about the reactivity of the inputs.

Steps to design an adaptable composable in Vue.js:
1. Confirm the composable's purpose and API design and expected inputs/outputs.
2. Identify inputs params that should be reactive (MaybeRef / MaybeRefOrGetter).
3. Use `toValue()` or `toRef()` to normalize inputs inside reactive effects.
4. Implement the core logic of the composable using Vue's reactivity APIs.

## Core Type Concepts

### Type Utilities

```ts
/**
 * value or writable ref (value/ref/shallowRef/writable computed)
 */
export type MaybeRef<T = any> = T | Ref<T> | ShallowRef<T> | WritableComputedRef<T>;

/**
 * MaybeRef<T> + ComputedRef<T> + () => T
 */
export type MaybeRefOrGetter<T = any> = MaybeRef<T> | ComputedRef<T> | (() => T);
```

### Policy and Rules

- Read-only, computed-friendly input: use `MaybeRefOrGetter`
- Needs to be writable / two-way input: use `MaybeRef`
- Parameter might be a function value (callback/predicate/comparator): do not use `MaybeRefOrGetter`, or you may accidentally invoke it as a getter.
- DOM/Element targets: if you want computed/derived targets, use `MaybeRefOrGetter`.

When `MaybeRefOrGetter` or `MaybeRef` is used: 
- resolve reactive value using `toRef()` (e.g. watcher source)
- resolve non-reactive value using `toValue()`

### Examples

Adaptable `useDocumentTitle` Composable: read-only title parameter

```ts
import { watch, toRef } from 'vue'
import type { MaybeRefOrGetter } from 'vue'

export function useDocumentTitle(title: MaybeRefOrGetter<string>) {
  watch(toRef(title), (t) => {
    document.title = t
  }, { immediate: true })
}
```

Adaptable `useCounter` Composable: two-way writable count parameter

```ts
import { watch, toRef } from 'vue'
import type { MaybeRef } from 'vue'

function useCounter(count: MaybeRef<number>) {
  const countRef = toRef(count)
  function add() {
    countRef.value++
  }
  return { add }
}
```
```

## File: `skills/vue-best-practices/SKILL.md`
```markdown
---
name: vue-best-practices
description: MUST be used for Vue.js tasks. Strongly recommends Composition API with `<script setup>` and TypeScript as the standard approach. Covers Vue 3, SSR, Volar, vue-tsc. Load for any Vue, .vue files, Vue Router, Pinia, or Vite with Vue work. ALWAYS use Composition API unless the project explicitly requires Options API.
license: MIT
metadata:
  author: github.com/vuejs-ai
  version: "18.0.0"
---

# Vue Best Practices Workflow

Use this skill as an instruction set. Follow the workflow in order unless the user explicitly asks for a different order.

## Core Principles
- **Keep state predictable:** one source of truth, derive everything else.
- **Make data flow explicit:** Props down, Events up for most cases.
- **Favor small, focused components:** easier to test, reuse, and maintain.
- **Avoid unnecessary re-renders:** use computed properties and watchers wisely.
- **Readability counts:** write clear, self-documenting code.

## 1) Confirm architecture before coding (required)

- Default stack: Vue 3 + Composition API + `<script setup lang="ts">`.
- If the project explicitly uses Options API, load `vue-options-api-best-practices` skill if available.
- If the project explicitly uses JSX, load `vue-jsx-best-practices` skill if available.

### 1.1 Must-read core references (required)

- Before implementing any Vue task, make sure to read and apply these core references:
  - `references/reactivity.md`
  - `references/sfc.md`
  - `references/component-data-flow.md`
  - `references/composables.md`
- Keep these references in active working context for the entire task, not only when a specific issue appears.

### 1.2 Plan component boundaries before coding (required)

Create a brief component map before implementation for any non-trivial feature.

- Define each component's single responsibility in one sentence.
- Keep entry/root and route-level view components as composition surfaces by default.
- Move feature UI and feature logic out of entry/root/view components unless the task is intentionally a tiny single-file demo.
- Define props/emits contracts for each child component in the map.
- Prefer a feature folder layout (`components/<feature>/...`, `composables/use<Feature>.ts`) when adding more than one component.

## 2) Apply essential Vue foundations (required)

These are essential, must-know foundations. Apply all of them in every Vue task using the core references already loaded in section `1.1`.

### Reactivity

- Must-read reference from `1.1`: [reactivity](references/reactivity.md)
- Keep source state minimal (`ref`/`reactive`), derive everything possible with `computed`.
- Use watchers for side effects if needed.
- Avoid recomputing expensive logic in templates.

### SFC structure and template safety

- Must-read reference from `1.1`: [sfc](references/sfc.md)
- Keep SFC sections in this order: `<script>` → `<template>` → `<style>`.
- Keep SFC responsibilities focused; split large components.
- Keep templates declarative; move branching/derivation to script.
- Apply Vue template safety rules (`v-html`, list rendering, conditional rendering choices).

### Keep components focused

Split a component when it has **more than one clear responsibility** (e.g. data orchestration + UI, or multiple independent UI sections).

- Prefer **smaller components + composables** over one “mega component”
- Move **UI sections** into child components (props in, events out).
- Move **state/side effects** into composables (`useXxx()`).

Apply objective split triggers. Split the component if **any** condition is true:

- It owns both orchestration/state and substantial presentational markup for multiple sections.
- It has 3+ distinct UI sections (for example: form, filters, list, footer/status).
- A template block is repeated or could become reusable (item rows, cards, list entries).

Entry/root and route view rule:

- Keep entry/root and route view components thin: app shell/layout, provider wiring, and feature composition.
- Do not place full feature implementations in entry/root/view components when those features contain independent parts.
- For CRUD/list features (todo, table, catalog, inbox), split at least into:
  - feature container component
  - input/form component
  - list (and/or item) component
  - footer/actions or filter/status component
- Allow a single-file implementation only for very small throwaway demos; if chosen, explicitly justify why splitting is unnecessary.

### Component data flow

- Must-read reference from `1.1`: [component-data-flow](references/component-data-flow.md)
- Use props down, events up as the primary model.
- Use `v-model` only for true two-way component contracts.
- Use provide/inject only for deep-tree dependencies or shared context.
- Keep contracts explicit and typed with `defineProps`, `defineEmits`, and `InjectionKey` as needed.

### Composables

- Must-read reference from `1.1`: [composables](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/templates/javascript_typescript/examples/vue_app/.claude/commands/composables.md)
- Extract logic into composables when it is reused, stateful, or side-effect heavy.
- Keep composable APIs small, typed, and predictable.
- Separate feature logic from presentational components.

## 3) Consider optional features only when requirements call for them

### 3.1 Standard optional features

Do not add these by default. Load the matching reference only when the requirement exists.

- Slots: parent needs to control child content/layout -> [component-slots](../../../vault/archives/knowledge_items/KI-BATCH-20260331205007519197/github.com_hyf0_vue-skills_1ee4c0f8/skills/vue-best-practices/references/component-slots.md)
- Fallthrough attributes: wrapper/base components must forward attrs/events safely -> [component-fallthrough-attrs](references/component-fallthrough-attrs.md)
- Built-in component `<KeepAlive>` for stateful view caching -> [component-keep-alive](references/component-keep-alive.md)
- Built-in component `<Teleport>` for overlays/portals -> [component-teleport](references/component-teleport.md)
- Built-in component `<Suspense>` for async subtree fallback boundaries -> [component-suspense](references/component-suspense.md)
- Animation-related features: pick the simplest approach that matches the required motion behavior.
  - Built-in component `<Transition>` for enter/leave effects -> [transition](references/component-transition.md)
  - Built-in component `<TransitionGroup>` for animated list mutations -> [transition-group](references/component-transition-group.md)
  - Class-based animation for non-enter/leave effects -> [animation-class-based-technique](references/animation-class-based-technique.md)
  - State-driven animation for user-input-driven animation -> [animation-state-driven-technique](references/animation-state-driven-technique.md)

### 3.2 Less-common optional features

Use these only when there is explicit product or technical need.

- Directives: behavior is DOM-specific and not a good composable/component fit -> [directives](references/directives.md)
- Async components: heavy/rarely-used UI should be lazy loaded -> [component-async](references/component-async.md)
- Render functions only when templates cannot express the requirement -> [render-functions](references/render-functions.md)
- Plugins when behavior must be installed app-wide -> [plugins](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/engine_reference/unity/PLUGINS.md)
- State management patterns: app-wide shared state crosses feature boundaries -> [state-management](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/ai-research/model-architecture-rwkv/references/state-management.md)

## 4) Run performance optimization after behavior is correct

Performance work is a post-functionality pass. Do not optimize before core behavior is implemented and verified.

- Large list rendering bottlenecks -> [perf-virtualize-large-lists](references/perf-virtualize-large-lists.md)
- Static subtrees re-rendering unnecessarily -> [perf-v-once-v-memo-directives](references/perf-v-once-v-memo-directives.md)
- Over-abstraction in hot list paths -> [perf-avoid-component-abstraction-in-lists](references/perf-avoid-component-abstraction-in-lists.md)
- Expensive updates triggered too often -> [updated-hook-performance](references/updated-hook-performance.md)

## 5) Final self-check before finishing

- Core behavior works and matches requirements.
- All must-read references were read and applied.
- Reactivity model is minimal and predictable.
- SFC structure and template rules are followed.
- Components are focused and well-factored, splitting when needed.
- Entry/root and route view components remain composition surfaces unless there is an explicit small-demo exception.
- Component split decisions are explicit and defensible (responsibility boundaries are clear).
- Data flow contracts are explicit and typed.
- Composables are used where reuse/complexity justifies them.
- Moved state/side effects into composables if applicable
- Optional features are used only when requirements demand them.
- Performance changes were applied only after functionality was complete.
```

## File: `skills/vue-best-practices/references/animation-class-based-technique.md`
```markdown
---
title: Use Class-based Animations for Non-Enter/Leave Effects
impact: LOW
impactDescription: Class-based animations are simpler and more performant for elements that remain in the DOM
type: best-practice
tags: [vue3, animation, css, class-binding, state]
---

# Use Class-based Animations for Non-Enter/Leave Effects

**Impact: LOW** - For animations on elements that are not entering or leaving the DOM, use CSS class-based animations triggered by Vue's reactive state. This is simpler than `<Transition>` and more appropriate for feedback animations like shake, pulse, or highlight effects.

## Task List

- Use class-based animations for elements staying in the DOM
- Use `<Transition>` only for enter/leave animations
- Combine CSS animations with Vue's class bindings (`:class`)
- Consider using `setTimeout` to auto-remove animation classes

**When to Use Class-based Animations:**
- User feedback (shake on error, pulse on success)
- Attention-grabbing effects (highlight changes)
- Hover/focus states that need more than CSS transitions
- Any animation where the element stays mounted

**When to Use Transition Component:**
- Elements entering/leaving the DOM (v-if/v-show)
- Route transitions
- List item additions/removals

## Basic Pattern

```vue
<template>
  <div :class="{ shake: showError }">
    <button @click="submitForm">Submit</button>
    <span v-if="showError">This feature is disabled!</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const showError = ref(false)

function submitForm() {
  if (!isValid()) {
    // Trigger shake animation
    showError.value = true

    // Auto-remove class after animation completes
    setTimeout(() => {
      showError.value = false
    }, 820)  // Match animation duration
  }
}
</script>

<style>
.shake {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);  /* Enable GPU acceleration */
}

@keyframes shake {
  10%, 90% { transform: translate3d(-1px, 0, 0); }
  20%, 80% { transform: translate3d(2px, 0, 0); }
  30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
  40%, 60% { transform: translate3d(4px, 0, 0); }
}
</style>
```

## Common Animation Patterns

### Pulse on Success

```vue
<template>
  <button
    @click="save"
    :class="{ pulse: saved }"
  >
    {{ saved ? 'Saved!' : 'Save' }}
  </button>
</template>

<script setup>
import { ref } from 'vue'

const saved = ref(false)

async function save() {
  await saveData()
  saved.value = true
  setTimeout(() => saved.value = false, 1000)
}
</script>

<style>
.pulse {
  animation: pulse 0.5s ease-in-out;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}
</style>
```

### Highlight on Change

```vue
<template>
  <div
    :class="{ highlight: justUpdated }"
  >
    Value: {{ value }}
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const value = ref(0)
const justUpdated = ref(false)

watch(value, () => {
  justUpdated.value = true
  setTimeout(() => justUpdated.value = false, 1000)
})
</script>

<style>
.highlight {
  animation: highlight 1s ease-out;
}

@keyframes highlight {
  0% { background-color: yellow; }
  100% { background-color: transparent; }
}
</style>
```

### Bounce Attention

```vue
<template>
  <div
    :class="{ bounce: needsAttention }"
    @animationend="needsAttention = false"
  >
    <BellIcon />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const needsAttention = ref(false)

function notifyUser() {
  needsAttention.value = true
  // No setTimeout needed - using animationend event
}
</script>

<style>
.bounce {
  animation: bounce 0.5s ease;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
</style>
```

## Using animationend Event

Instead of `setTimeout`, use the `animationend` event for cleaner code:

```vue
<template>
  <div
    :class="{ animate: isAnimating }"
    @animationend="isAnimating = false"
  >
    Content
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isAnimating = ref(false)

function triggerAnimation() {
  isAnimating.value = true
  // Class is automatically removed when animation ends
}
</script>
```

## Composable for Reusable Animations

```javascript
// composables/useAnimation.js
import { ref } from 'vue'

export function useAnimation(duration = 500) {
  const isAnimating = ref(false)

  function trigger() {
    isAnimating.value = true
    setTimeout(() => {
      isAnimating.value = false
    }, duration)
  }

  return {
    isAnimating,
    trigger
  }
}
```

```vue
<script setup>
import { useAnimation } from '@/composables/useAnimation'

const shake = useAnimation(820)
const pulse = useAnimation(500)
</script>

<template>
  <button
    :class="{ shake: shake.isAnimating.value }"
    @click="shake.trigger()"
  >
    Shake me
  </button>

  <button
    :class="{ pulse: pulse.isAnimating.value }"
    @click="pulse.trigger()"
  >
    Pulse me
  </button>
</template>
```
```

## File: `skills/vue-best-practices/references/animation-state-driven-technique.md`
```markdown
---
title: State-driven Animations with CSS Transitions and Style Bindings
impact: LOW
impactDescription: Combining Vue's reactive style bindings with CSS transitions creates smooth, interactive animations
type: best-practice
tags: [vue3, animation, css, transition, style-binding, state, interactive]
---

# State-driven Animations with CSS Transitions and Style Bindings

**Impact: LOW** - For responsive, interactive animations that react to user input or state changes, combine Vue's dynamic style bindings with CSS transitions. This creates smooth animations that interpolate values in real-time based on state.

## Task List

- Use `:style` binding for dynamic properties that change frequently
- Add CSS `transition` property to smoothly animate between values
- Consider using `transform` and `opacity` for GPU-accelerated animations
- For complex value interpolation, use watchers with animation libraries

## Basic Pattern

```vue
<template>
  <div
    @mousemove="onMousemove"
    :style="{ backgroundColor: `hsl(${hue}, 80%, 50%)` }"
    class="interactive-area"
  >
    <p>Move your mouse across this div...</p>
    <p>Hue: {{ hue }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const hue = ref(0)

function onMousemove(e) {
  // Map mouse X position to hue (0-360)
  const rect = e.currentTarget.getBoundingClientRect()
  hue.value = Math.round((e.clientX - rect.left) / rect.width * 360)
}
</script>

<style>
.interactive-area {
  transition: background-color 0.3s ease;
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
```

## Common Use Cases

### Following Mouse Position

```vue
<template>
  <div
    class="container"
    @mousemove="onMousemove"
  >
    <div
      class="follower"
      :style="{
        transform: `translate(${x}px, ${y}px)`
      }"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const x = ref(0)
const y = ref(0)

function onMousemove(e) {
  const rect = e.currentTarget.getBoundingClientRect()
  x.value = e.clientX - rect.left
  y.value = e.clientY - rect.top
}
</script>

<style>
.container {
  position: relative;
  height: 300px;
}

.follower {
  position: absolute;
  width: 20px;
  height: 20px;
  background: blue;
  border-radius: 50%;
  /* Smooth following with transition */
  transition: transform 0.1s ease-out;
  /* Prevent the follower from triggering mousemove */
  pointer-events: none;
}
</style>
```

### Progress Animation

```vue
<template>
  <div class="progress-container">
    <div
      class="progress-bar"
      :style="{ width: `${progress}%` }"
    />
  </div>
  <input
    type="range"
    v-model.number="progress"
    min="0"
    max="100"
  />
</template>

<script setup>
import { ref } from 'vue'

const progress = ref(0)
</script>

<style>
.progress-container {
  height: 20px;
  background: #e0e0e0;
  border-radius: 10px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #4CAF50, #8BC34A);
  transition: width 0.3s ease;
}
</style>
```

### Scroll-based Animation

```vue
<template>
  <div
    class="hero"
    :style="{
      opacity: heroOpacity,
      transform: `translateY(${scrollOffset}px)`
    }"
  >
    <h1>Scroll Down</h1>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const scrollY = ref(0)

const heroOpacity = computed(() => {
  return Math.max(0, 1 - scrollY.value / 300)
})

const scrollOffset = computed(() => {
  return scrollY.value * 0.5  // Parallax effect
})

function handleScroll() {
  scrollY.value = window.scrollY
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style>
.hero {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  /* Note: No transition for scroll-based animations - they should be instant */
}
</style>
```

### Color Theme Transition

```vue
<template>
  <div
    class="app"
    :style="themeStyles"
  >
    <button @click="toggleTheme">Toggle Theme</button>
    <p>Current theme: {{ isDark ? 'Dark' : 'Light' }}</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const isDark = ref(false)

const themeStyles = computed(() => ({
  '--bg-color': isDark.value ? '#1a1a1a' : '#ffffff',
  '--text-color': isDark.value ? '#ffffff' : '#1a1a1a',
  backgroundColor: 'var(--bg-color)',
  color: 'var(--text-color)'
}))

function toggleTheme() {
  isDark.value = !isDark.value
}
</script>

<style>
.app {
  min-height: 100vh;
  transition: background-color 0.5s ease, color 0.5s ease;
}
</style>
```

## Advanced: Numerical Tweening with Watchers

For smooth number animations (counters, stats), use watchers with animation libraries:

```vue
<template>
  <div>
    <input v-model.number="targetNumber" type="number" />
    <p class="counter">{{ displayNumber.toFixed(0) }}</p>
  </div>
</template>

<script setup>
import { computed, ref, reactive, watch } from 'vue'
import gsap from 'gsap'

const targetNumber = ref(0)
const tweened = reactive({ value: 0 })

// Computed for display
const displayNumber = computed(() => tweened.value)

watch(targetNumber, (newValue) => {
  gsap.to(tweened, {
    duration: 0.5,
    value: Number(newValue) || 0,
    ease: 'power2.out'
  })
})
</script>
```

## Performance Considerations

```vue
<style>
/* GOOD: GPU-accelerated properties */
.element {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

/* AVOID: Properties that trigger layout recalculation */
.element {
  transition: width 0.3s ease, height 0.3s ease, margin 0.3s ease;
}

/* For high-frequency updates, consider will-change */
.frequently-animated {
  will-change: transform;
}
</style>
```
```

## File: `skills/vue-best-practices/references/component-async.md`
```markdown
---
title: Async Component Best Practices
impact: MEDIUM
impactDescription: Poor async component strategy can delay interactivity in SSR apps and create loading UI flicker
type: best-practice
tags: [vue3, async-components, ssr, hydration, performance, ux]
---

# Async Component Best Practices

**Impact: MEDIUM** - Async components should reduce JavaScript cost without degrading perceived performance. Focus on hydration timing in SSR and stable loading UX.

## Task List

- Use lazy hydration strategies for non-critical SSR component trees
- Import only the hydration helpers you actually use
- Keep `loadingComponent` delay near the default `200ms` unless real UX data suggests otherwise
- Configure `delay` and `timeout` together for predictable loading behavior

## Use Lazy Hydration Strategies in SSR

In Vue 3.5+, async components can delay hydration until idle time, visibility, media query match, or user interaction.

**BAD:**
```vue
<script setup lang="ts">
import { defineAsyncComponent } from 'vue'

const AsyncComments = defineAsyncComponent({
  loader: () => import('./Comments.vue')
})
</script>
```

**GOOD:**
```vue
<script setup lang="ts">
import {
  defineAsyncComponent,
  hydrateOnVisible,
  hydrateOnIdle
} from 'vue'

const AsyncComments = defineAsyncComponent({
  loader: () => import('./Comments.vue'),
  hydrate: hydrateOnVisible({ rootMargin: '100px' })
})

const AsyncFooter = defineAsyncComponent({
  loader: () => import('./Footer.vue'),
  hydrate: hydrateOnIdle(5000)
})
</script>
```

## Prevent Loading Spinner Flicker

Avoid showing loading UI immediately for components that usually resolve quickly.

**BAD:**
```vue
<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import LoadingSpinner from './LoadingSpinner.vue'

const AsyncDashboard = defineAsyncComponent({
  loader: () => import('./Dashboard.vue'),
  loadingComponent: LoadingSpinner,
  delay: 0
})
</script>
```

**GOOD:**
```vue
<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import LoadingSpinner from './LoadingSpinner.vue'
import ErrorDisplay from './ErrorDisplay.vue'

const AsyncDashboard = defineAsyncComponent({
  loader: () => import('./Dashboard.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  delay: 200,
  timeout: 30000
})
</script>
```

## Delay Guidelines

| Scenario | Recommended Delay |
|----------|-------------------|
| Small component, fast network | `200ms` |
| Known heavy component | `100ms` |
| Background or non-critical UI | `300-500ms` |
```

## File: `skills/vue-best-practices/references/component-data-flow.md`
```markdown
---
title: Component Data Flow Best Practices
impact: HIGH
impactDescription: Clear data flow between components prevents state bugs, stale UI, and brittle coupling
type: best-practice
tags: [vue3, props, emits, v-model, provide-inject, data-flow, typescript]
---

# Component Data Flow Best Practices

**Impact: HIGH** - Vue components stay reliable when data flow is explicit: props go down, events go up, `v-model` handles two-way bindings, and provide/inject supports cross-tree dependencies. Blurring these boundaries leads to stale state, hidden coupling, and hard-to-debug UI.

The main principle of data flow in Vue.js is **Props Down / Events Up**. This is the most maintainable default, and one-way flow scales well.

## Task List

- Treat props as read-only inputs
- Use props/emit for component communication; reserve refs for imperative actions
- When refs are required for imperative APIs, type them with template refs
- Emit events instead of mutating parent state directly
- Use `defineModel` for v-model in modern Vue (3.4+)
- Handle v-model modifiers deliberately in child components
- Use symbols for provide/inject keys to avoid props drilling (over ~3 layers)
- Keep mutations in the provider or expose explicit actions
- In TypeScript projects, prefer type-based `defineProps`, `defineEmits`, and `InjectionKey`

## Props: One-Way Data Down

Props are inputs. Do not mutate them in the child.

**BAD:**
```vue
<script setup>
const props = defineProps({ count: Number })

function increment() {
  props.count++
}
</script>
```

**GOOD:**

If state needs to change, emit an event, use `v-model` or create a local copy.

## Prefer props/emit over component refs

**BAD:**
```vue
<script setup>
import { ref } from 'vue'
import UserForm from './UserForm.vue'

const formRef = ref(null)

function submitForm() {
  if (formRef.value.isValid) {
    formRef.value.submit()
  }
}
</script>

<template>
  <UserForm ref="formRef" />
  <button @click="submitForm">Submit</button>
</template>
```

**GOOD:**
```vue
<script setup>
import UserForm from './UserForm.vue'

function handleSubmit(formData) {
  api.submit(formData)
}
</script>

<template>
  <UserForm @submit="handleSubmit" />
</template>
```

## Type component refs when imperative access is required

Prefer props/emits by default. When a parent must call an exposed child method, type the ref explicitly and expose only the intended API from the child with `defineExpose`.

**BAD:**
```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import DialogPanel from './DialogPanel.vue'

const panelRef = ref(null)

onMounted(() => {
  panelRef.value.open()
})
</script>

<template>
  <DialogPanel ref="panelRef" />
</template>
```

**GOOD:**
```vue
<!-- DialogPanel.vue -->
<script setup lang="ts">
function open() {}

defineExpose({ open })
</script>
```

```vue
<!-- Parent.vue -->
<script setup lang="ts">
import { onMounted, useTemplateRef } from 'vue'
import DialogPanel from './DialogPanel.vue'

// Vue 3.5+ with useTemplateRef
const panelRef = useTemplateRef('panelRef')

// Before Vue 3.5 with manual typing and ref
// const panelRef = ref<InstanceType<typeof DialogPanel> | null>(null)

onMounted(() => {
  panelRef.value?.open()
})
</script>

<template>
  <DialogPanel ref="panelRef" />
</template>
```

## Emits: Explicit Events Up

Component events do not bubble. If a parent needs to know about an event, re-emit it explicitly.

**BAD:**
```vue
<!-- Parent expects "saved" from grandchild, but it won't bubble -->
<Child @saved="onSaved" />
```

**GOOD:**
```vue
<!-- Child.vue -->
<script setup>
const emit = defineEmits(['saved'])

function onGrandchildSaved(payload) {
  emit('saved', payload)
}
</script>

<template>
  <Grandchild @saved="onGrandchildSaved" />
</template>
```

**Event naming:** use kebab-case in templates and camelCase in script:
```vue
<script setup>
const emit = defineEmits(['updateUser'])
</script>

<template>
  <ProfileForm @update-user="emit('updateUser', $event)" />
</template>
```

## `v-model`: Predictable Two-Way Bindings

Use `defineModel` by default for component bindings and emit updates on input. Only use the `modelValue` + `update:modelValue` pattern if you are on Vue < 3.4.

**BAD:**
```vue
<script setup>
const props = defineProps({ value: String })
</script>

<template>
  <input :value="props.value" @input="$emit('input', $event.target.value)" />
</template>
```

**GOOD (Vue 3.4+):**
```vue
<script setup>
const model = defineModel({ type: String })
</script>

<template>
  <input v-model="model" />
</template>
```

**GOOD (Vue < 3.4):**
```vue
<script setup>
const props = defineProps({ modelValue: String })
const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <input
    :value="props.modelValue"
    @input="emit('update:modelValue', $event.target.value)"
  />
</template>
```

If you need the updated value immediately after a change, use the input event value or `nextTick` in the parent.

## Provide/Inject: Shared Context Without Prop Drilling

Use provide/inject for cross-tree state, but keep mutations centralized in the provider and expose explicit actions.

**BAD:**
```vue
// Provider.vue
provide('theme', reactive({ dark: false }))

// Consumer.vue
const theme = inject('theme')
// Mutating shared state from any depth becomes hard to track
theme.dark = true
```

**GOOD:**
```vue
// Provider.vue
const theme = reactive({ dark: false })
const toggleTheme = () => { theme.dark = !theme.dark }

provide(themeKey, readonly(theme))
provide(themeActionsKey, { toggleTheme })

// Consumer.vue
const theme = inject(themeKey)
const { toggleTheme } = inject(themeActionsKey)
```

Use symbols for keys to avoid collisions in large apps:
```ts
export const themeKey = Symbol('theme')
export const themeActionsKey = Symbol('theme-actions')
```

## Use TypeScript Contracts for Public Component APIs

In TypeScript projects, type component boundaries directly with `defineProps`, `defineEmits`, and `InjectionKey` so invalid payloads and mismatched injections fail at compile time.

**BAD:**
```vue
<script setup lang="ts">
import { inject } from 'vue'

const props = defineProps({
  userId: String
})

const emit = defineEmits(['save'])
const settings = inject('settings')

// Payload shape is not checked here
emit('save', 123)

// Key is string-based and not type-safe
settings?.theme = 'dark'
</script>
```

**GOOD:**
```vue
<script setup lang="ts">
import { inject, provide } from 'vue'
import type { InjectionKey } from 'vue'

interface Props {
  userId: string
}

interface Emits {
  save: [payload: { id: string; draft: boolean }]
}

interface Settings {
  theme: 'light' | 'dark'
}

const settingsKey: InjectionKey<Settings> = Symbol('settings')

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

provide(settingsKey, { theme: 'light' })

const settings = inject(settingsKey)
if (settings) {
  emit('save', { id: props.userId, draft: false })
}
</script>
```
```

## File: `skills/vue-best-practices/references/component-fallthrough-attrs.md`
```markdown
---
title: Component Fallthrough Attributes Best Practices
impact: MEDIUM
impactDescription: Incorrect $attrs access and reactivity assumptions can cause undefined values and watchers that never run
type: best-practice
tags: [vue3, attrs, fallthrough-attributes, composition-api, reactivity]
---

# Component Fallthrough Attributes Best Practices

**Impact: MEDIUM** - Fallthrough attributes are straightforward once you follow Vue's conventions: hyphenated names use bracket notation, listener keys are camelCase `onX`, and `useAttrs()` is current-but-not-reactive.

## Task List

- Access hyphenated attribute names with bracket notation (for example `attrs['data-testid']`)
- Access event listeners with camelCase `onX` keys (for example `attrs.onClick`)
- Do not `watch()` values returned from `useAttrs()`; those watchers do not trigger on attr changes
- Use `onUpdated()` for attr-driven side effects
- Promote frequently observed attrs to props when reactive observation is required

## Access Attribute and Listener Keys Correctly

Hyphenated attribute names preserve their original casing in JavaScript, so dot notation does not work for keys that include `-`.

**BAD:**
```vue
<script setup>
import { useAttrs } from 'vue'

const attrs = useAttrs()

console.log(attrs.data-testid)  // Syntax error
console.log(attrs.dataTestid)   // undefined for data-testid
console.log(attrs['on-click'])  // undefined
console.log(attrs['@click'])    // undefined
</script>
```

**GOOD:**
```vue
<script setup>
import { useAttrs } from 'vue'

const attrs = useAttrs()

console.log(attrs['data-testid'])
console.log(attrs['aria-label'])
console.log(attrs['foo-bar'])

console.log(attrs.onClick)
console.log(attrs.onCustomEvent)
console.log(attrs.onMouseEnter)
</script>
```

### Naming Reference

| Parent Usage | Access in `attrs` |
|--------------|-------------------|
| `class="foo"` | `attrs.class` |
| `data-id="123"` | `attrs['data-id']` |
| `aria-label="..."` | `attrs['aria-label']` |
| `foo-bar="baz"` | `attrs['foo-bar']` |
| `@click="fn"` | `attrs.onClick` |
| `@custom-event="fn"` | `attrs.onCustomEvent` |
| `@update:modelValue="fn"` | `attrs['onUpdate:modelValue']` |

## `useAttrs()` Is Not Reactive

`useAttrs()` always reflects the latest values, but it is intentionally not reactive for watcher tracking.

**BAD:**
```vue
<script setup>
import { watch, watchEffect, useAttrs } from 'vue'

const attrs = useAttrs()

watch(
  () => attrs.someAttr,
  (newValue) => {
    console.log('Changed:', newValue) // Never runs on attr changes
  }
)

watchEffect(() => {
  console.log(attrs.class) // Runs on setup, not on attr updates
})
</script>
```

**GOOD:**
```vue
<script setup>
import { onUpdated, useAttrs } from 'vue'

const attrs = useAttrs()

onUpdated(() => {
  console.log('Latest attrs:', attrs)
})
</script>
```

**GOOD:**
```vue
<script setup>
import { watch } from 'vue'

const props = defineProps({
  someAttr: String
})

watch(
  () => props.someAttr,
  (newValue) => {
    console.log('Changed:', newValue)
  }
)
</script>
```

## Common Patterns

### Check for optional attrs safely

```vue
<script setup>
import { computed, useAttrs } from 'vue'

const attrs = useAttrs()

const hasTestId = computed(() => 'data-testid' in attrs)
const ariaLabel = computed(() => attrs['aria-label'] ?? 'Default label')
</script>
```

### Forward listeners after internal logic

```vue
<script setup>
import { useAttrs } from 'vue'

defineOptions({ inheritAttrs: false })

const attrs = useAttrs()

function handleClick(event) {
  console.log('Internal handling first')
  attrs.onClick?.(event)
}
</script>

<template>
  <button @click="handleClick">
    <slot />
  </button>
</template>
```

## TypeScript Notes

`useAttrs()` is typed as `Record<string, unknown>`, so cast individual keys when needed.

```vue
<script setup lang="ts">
import { useAttrs } from 'vue'

const attrs = useAttrs()

const testId = attrs['data-testid'] as string | undefined
const onClick = attrs.onClick as ((event: MouseEvent) => void) | undefined
</script>
```
```

## File: `skills/vue-best-practices/references/component-keep-alive.md`
```markdown
---
title: KeepAlive Component Best Practices
impact: HIGH
impactDescription: KeepAlive caches component instances; misuse causes stale data, memory growth, or unexpected lifecycle behavior
type: best-practice
tags: [vue3, keepalive, cache, performance, router, dynamic-components]
---

# KeepAlive Component Best Practices

**Impact: HIGH** - `<KeepAlive>` caches component instances instead of destroying them. Use it to preserve state across switches, but manage cache size and freshness explicitly to avoid memory growth or stale UI.

## Task List

- Use KeepAlive only where state preservation improves UX
- Set a reasonable `max` to cap cache size
- Declare component names for include/exclude matching
- Use `onActivated`/`onDeactivated` for cache-aware logic
- Decide how and when cached views refresh their data
- Avoid caching memory-heavy or security-sensitive views

## When to Use KeepAlive

Use KeepAlive when switching between views where state should persist (tabs, multi-step forms, dashboards). Avoid it when each visit should start fresh.

**BAD:**
```vue
<template>
  <!-- State resets on every switch -->
  <component :is="currentTab" />
</template>
```

**GOOD:**
```vue
<template>
  <!-- State preserved between switches -->
  <KeepAlive>
    <component :is="currentTab" />
  </KeepAlive>
</template>
```

## When NOT to Use KeepAlive

- Search or filter pages where users expect fresh results
- Memory-heavy components (maps, large tables, media players)
- Sensitive flows where data must be cleared on exit
- Components with heavy background activity you cannot pause

## Limit and Control the Cache

Always cap cache size with `max` and restrict caching to specific components when possible.

```vue
<template>
  <KeepAlive :max="5" include="Dashboard,Settings">
    <component :is="currentView" />
  </KeepAlive>
</template>
```

## Ensure Component Names Match include/exclude

`include` and `exclude` match the component `name` option. Explicitly set names for reliable caching.

```vue
<!-- TabA.vue -->
<script setup>
defineOptions({ name: 'TabA' })
</script>
```

```vue
<template>
  <KeepAlive include="TabA,TabB">
    <component :is="currentTab" />
  </KeepAlive>
</template>
```

## Cache Invalidation Strategies

Vue 3 has no direct API to remove a specific cached instance. Use keys or dynamic include/exclude to force refreshes.

```vue
<script setup>
import { ref, reactive } from 'vue'

const currentView = ref('Dashboard')
const viewKeys = reactive({ Dashboard: 0, Settings: 0 })

function invalidateCache(view) {
  viewKeys[view]++
}
</script>

<template>
  <KeepAlive>
    <component :is="currentView" :key="`${currentView}-${viewKeys[currentView]}`" />
  </KeepAlive>
</template>
```

## Lifecycle Hooks for Cached Components

Cached components are not destroyed on switch. Use activation hooks for refresh and cleanup.

```vue
<script setup>
import { onActivated, onDeactivated } from 'vue'

onActivated(() => {
  refreshData()
})

onDeactivated(() => {
  pauseTimers()
})
</script>
```

## Router Caching and Freshness

Decide whether navigation should show cached state or a fresh view. A common pattern is to key by route when params change.

```vue
<template>
  <router-view v-slot="{ Component, route }">
    <KeepAlive>
      <component :is="Component" :key="route.fullPath" />
    </KeepAlive>
  </router-view>
</template>
```

If you want cache reuse but fresh data, refresh in `onActivated` and compare query/params before fetching.
```

## File: `skills/vue-best-practices/references/component-slots.md`
```markdown
---
title: Component Slots Best Practices
impact: MEDIUM
impactDescription: Poor slot API design causes empty DOM wrappers, weak TypeScript safety, brittle defaults, and unnecessary component overhead
type: best-practice
tags: [vue3, slots, components, typescript, composables]
---

# Component Slots Best Practices

**Impact: MEDIUM** - Slots are a core component API surface in Vue. Structure them intentionally so templates stay predictable, typed, and performant.

## Task List

- Use shorthand syntax for named slots (`#` instead of `v-slot:`)
- Render optional slot wrapper elements only when slot content exists (`$slots` checks)
- Type scoped slot contracts with `defineSlots` in TypeScript components
- Provide fallback content for optional slots
- Prefer composables over renderless components for pure logic reuse

## Shorthand syntax for named slots

**BAD:**
```vue
<MyComponent>
  <template v-slot:header> ... </template>
</MyComponent>
```

**GOOD:**
```vue
<MyComponent>
  <template #header> ... </template>
</MyComponent>
```

## Conditionally Render Optional Slot Wrappers

Use `$slots` checks when wrapper elements add spacing, borders, or layout constraints.

**BAD:**
```vue
<!-- Card.vue -->
<template>
  <article class="card">
    <header class="card-header">
      <slot name="header" />
    </header>

    <section class="card-body">
      <slot />
    </section>

    <footer class="card-footer">
      <slot name="footer" />
    </footer>
  </article>
</template>
```

**GOOD:**
```vue
<!-- Card.vue -->
<template>
  <article class="card">
    <header v-if="$slots.header" class="card-header">
      <slot name="header" />
    </header>

    <section v-if="$slots.default" class="card-body">
      <slot />
    </section>

    <footer v-if="$slots.footer" class="card-footer">
      <slot name="footer" />
    </footer>
  </article>
</template>
```

## Type Scoped Slot Props with defineSlots

In `<script setup lang="ts">`, use `defineSlots` so slot consumers get autocomplete and static checks.

**BAD:**
```vue
<!-- ProductList.vue -->
<script setup lang="ts">
interface Product {
  id: number
  name: string
}

defineProps<{ products: Product[] }>()
</script>

<template>
  <ul>
    <li v-for="(product, index) in products" :key="product.id">
      <slot :product="product" :index="index" />
    </li>
  </ul>
</template>
```

**GOOD:**
```vue
<!-- ProductList.vue -->
<script setup lang="ts">
interface Product {
  id: number
  name: string
}

defineProps<{ products: Product[] }>()

defineSlots<{
  default(props: { product: Product; index: number }): any
  empty(): any
}>()
</script>

<template>
  <ul v-if="products.length">
    <li v-for="(product, index) in products" :key="product.id">
      <slot :product="product" :index="index" />
    </li>
  </ul>
  <slot v-else name="empty" />
</template>
```

## Provide Slot Fallback Content

Fallback content makes components resilient when parents omit optional slots.

**BAD:**
```vue
<!-- SubmitButton.vue -->
<template>
  <button type="submit" class="btn-primary">
    <slot />
  </button>
</template>
```

**GOOD:**
```vue
<!-- SubmitButton.vue -->
<template>
  <button type="submit" class="btn-primary">
    <slot>Submit</slot>
  </button>
</template>
```

## Prefer Composables for Pure Logic Reuse

Renderless components are still useful for slot-driven composition, but composables are usually cleaner for logic-only reuse.

**BAD:**
```vue
<!-- MouseTracker.vue -->
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const x = ref(0)
const y = ref(0)

function onMove(event: MouseEvent) {
  x.value = event.pageX
  y.value = event.pageY
}

onMounted(() => window.addEventListener('mousemove', onMove))
onUnmounted(() => window.removeEventListener('mousemove', onMove))
</script>

<template>
  <slot :x="x" :y="y" />
</template>
```

**GOOD:**
```ts
// composables/useMouse.ts
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function onMove(event: MouseEvent) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', onMove))
  onUnmounted(() => window.removeEventListener('mousemove', onMove))

  return { x, y }
}
```

```vue
<!-- MousePosition.vue -->
<script setup lang="ts">
import { useMouse } from '@/composables/useMouse'

const { x, y } = useMouse()
</script>

<template>
  <p>{{ x }}, {{ y }}</p>
</template>
```
```

## File: `skills/vue-best-practices/references/component-suspense.md`
```markdown
---
title: Suspense Component Best Practices
impact: MEDIUM
impactDescription: Suspense coordinates async dependencies with fallback UI; misconfiguration leads to missing loading states or confusing UX
type: best-practice
tags: [vue3, suspense, async-components, async-setup, loading, fallback, router, transition, keepalive]
---

# Suspense Component Best Practices

**Impact: MEDIUM** - `<Suspense>` coordinates async dependencies (async components or async setup) and renders a fallback while they resolve. Misconfiguration leads to missing loading states, empty renders, or subtle UX bugs.

## Task List

- Wrap default and fallback slot content in a single root node
- Use `timeout` when you need the fallback to appear on reverts
- Force root replacement with `:key` when you need Suspense to re-trigger
- Add `suspensible` to nested Suspense boundaries (Vue 3.3+)
- Use `@pending`, `@resolve`, and `@fallback` for programmatic loading state
- Nest `RouterView` -> `Transition` -> `KeepAlive` -> `Suspense` in that order
- Keep Suspense usage centralized and documented in production

## Single Root in Default and Fallback Slots

Suspense tracks a single immediate child in both slots. Wrap multiple elements in a single element or component.

**BAD:**
```vue
<template>
  <Suspense>
    <AsyncHeader />
    <AsyncList />

    <template #fallback>
      <LoadingSpinner />
      <LoadingHint />
    </template>
  </Suspense>
</template>
```

**GOOD:**
```vue
<template>
  <Suspense>
    <div>
      <AsyncHeader />
      <AsyncList />
    </div>

    <template #fallback>
      <div>
        <LoadingSpinner />
        <LoadingHint />
      </div>
    </template>
  </Suspense>
</template>
```

## Fallback Timing on Reverts (`timeout`)

When Suspense is already resolved and new async work starts, the previous content remains visible until the timeout elapses. Use `timeout="0"` for immediate fallback or a short delay to avoid flicker.

**BAD:**
```vue
<template>
  <Suspense>
    <component :is="currentView" :key="viewKey" />

    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

**GOOD:**
```vue
<template>
  <Suspense :timeout="200">
    <component :is="currentView" :key="viewKey" />

    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

## Pending State Only Re-triggers on Root Replacement

Once resolved, Suspense only re-enters pending when the root node of the default slot changes. If async work happens deeper in the tree, no fallback appears.

**BAD:**
```vue
<template>
  <Suspense>
    <TabContainer>
      <AsyncDashboard v-if="tab === 'dashboard'" />
      <AsyncSettings v-else />
    </TabContainer>

    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

**GOOD:**
```vue
<template>
  <Suspense>
    <component :is="tabs[tab]" :key="tab" />

    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

## Use `suspensible` for Nested Suspense (Vue 3.3+)

Nested Suspense boundaries need `suspensible` on the inner boundary so the parent can coordinate loading state. Without it, inner async content may render empty nodes until resolved.

**BAD:**
```vue
<template>
  <Suspense>
    <LayoutShell>
      <Suspense>
        <AsyncWidget />
        <template #fallback>Loading widget...</template>
      </Suspense>
    </LayoutShell>

    <template #fallback>Loading layout...</template>
  </Suspense>
</template>
```

**GOOD:**
```vue
<template>
  <Suspense>
    <LayoutShell>
      <Suspense suspensible>
        <AsyncWidget />
        <template #fallback>Loading widget...</template>
      </Suspense>
    </LayoutShell>

    <template #fallback>Loading layout...</template>
  </Suspense>
</template>
```

## Track Loading with Suspense Events

Use `@pending`, `@resolve`, and `@fallback` for analytics, global loading indicators, or coordinating UI outside the Suspense boundary.

```vue
<script setup>
import { ref } from 'vue'

const isLoading = ref(false)

const onPending = () => {
  isLoading.value = true
}

const onResolve = () => {
  isLoading.value = false
}
</script>

<template>
  <LoadingBar v-if="isLoading" />

  <Suspense @pending="onPending" @resolve="onResolve">
    <AsyncPage />
    <template #fallback>
      <PageSkeleton />
    </template>
  </Suspense>
</template>
```

## Recommended Nesting with RouterView, Transition, KeepAlive

When combining these components, the nesting order should be `RouterView` -> `Transition` -> `KeepAlive` -> `Suspense` so each wrapper works correctly.

**BAD:**
```vue
<template>
  <RouterView v-slot="{ Component }">
    <Suspense>
      <KeepAlive>
        <Transition mode="out-in">
          <component :is="Component" />
        </Transition>
      </KeepAlive>
    </Suspense>
  </RouterView>
</template>
```

**GOOD:**
```vue
<template>
  <RouterView v-slot="{ Component }">
    <Transition mode="out-in">
      <KeepAlive>
        <Suspense>
          <component :is="Component" />
          <template #fallback>Loading...</template>
        </Suspense>
      </KeepAlive>
    </Transition>
  </RouterView>
</template>
```

## Treat Suspense Cautiously in Production

In production code, keep Suspense boundaries minimal, document where they are used, and have a fallback loading strategy if you ever need to replace or refactor them.
```

## File: `skills/vue-best-practices/references/component-teleport.md`
```markdown
---
title: Teleport Component Best Practices
impact: MEDIUM
impactDescription: Teleport renders content outside the component's DOM position, which is essential for overlays but affects styling and layout
type: best-practice
tags: [vue3, teleport, modal, overlay, positioning, responsive]
---

# Teleport Component Best Practices

**Impact: MEDIUM** - `<Teleport>` renders part of a component's template in a different place in the DOM while preserving the Vue component hierarchy. Use it for overlays (modals, toasts, tooltips) or any UI that must escape stacking contexts, overflow, or fixed positioning constraints.

## Task List

- Teleport overlays to `body` or a dedicated container outside the app root
- Keep a shared target for similar UI (`#modals`, `#notifications`) and control layering with order or z-index
- Use `:disabled` for responsive layouts that should render inline on small screens
- Remember props, emits, and provide/inject still work through teleport
- Avoid relying on parent stacking contexts or transforms for teleported UI

## Teleport Overlays Out of Transformed Containers

When an ancestor has `transform`, `filter`, or `perspective`, fixed-position overlays can behave like they are locally positioned. Teleport escapes that context.

**BAD:**
```vue
<template>
  <div class="animated-container">
    <button @click="open = true">Open</button>

    <!-- Broken: fixed positioning is scoped to the transformed parent -->
    <div v-if="open" class="modal">Modal</div>
  </div>
</template>

<style>
.animated-container {
  transform: translateZ(0);
}

.modal {
  position: fixed;
  inset: 0;
  z-index: 9999;
}
</style>
```

**GOOD:**
```vue
<template>
  <div class="animated-container">
    <button @click="open = true">Open</button>

    <Teleport to="body">
      <div v-if="open" class="modal">Modal</div>
    </Teleport>
  </div>
</template>
```

## Responsive Layouts with `disabled`

Use `:disabled` to render inline on mobile and teleport on larger screens:

```vue
<script setup>
import { useMediaQuery } from '@vueuse/core'

const isMobile = useMediaQuery('(max-width: 768px)')
</script>

<template>
  <Teleport to="body" :disabled="isMobile">
    <nav class="sidebar">Navigation</nav>
  </Teleport>
</template>
```

## Logical Hierarchy Is Preserved

Teleport changes DOM position, not the Vue component tree. Props, emits, slots, and provide/inject still work:

```vue
<template>
  <Teleport to="body">
    <ChildPanel :message="message" @close="open = false" />
  </Teleport>
</template>
```

## Multiple Teleports to the Same Target

Teleports to the same target append in declaration order:

```vue
<template>
  <Teleport to="#notifications">
    <div>First</div>
  </Teleport>

  <Teleport to="#notifications">
    <div>Second</div>
  </Teleport>
</template>
```

Use a shared container to keep stacking predictable, and apply z-index only when you need explicit layering.
```

## File: `skills/vue-best-practices/references/component-transition-group.md`
```markdown
---
title: TransitionGroup Component Best Practices
impact: MEDIUM
impactDescription: TransitionGroup animates list items; missing keys or misuse leads to broken list transitions
type: best-practice
tags: [vue3, transition-group, animation, lists, keys]
---

# TransitionGroup Component Best Practices

**Impact: MEDIUM** - `<TransitionGroup>` animates lists of items entering, leaving, and moving. Use it for `v-for` lists or dynamic collections where individual items change over time.

## Task List

- Use `<TransitionGroup>` only for lists and repeated items
- Provide unique, stable keys for every direct child
- Use `tag` when you need semantic or layout wrappers
- Avoid the `mode` prop (not supported)
- Use JavaScript hooks for staggered effects

## Use TransitionGroup for Lists

`<TransitionGroup>` is designed for list items. Use `tag` to control the wrapper element when needed.

**BAD:**
```vue
<template>
  <TransitionGroup name="fade">
    <ComponentA />
    <ComponentB />
  </TransitionGroup>
</template>
```

**GOOD:**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>
```

## Always Provide Stable Keys

Keys are required. Without stable keys, Vue cannot track item positions and animations break.

**BAD:**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="(item, index) in items" :key="index">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>
```

**GOOD:**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>
```

## Do Not Use `mode` on TransitionGroup

`mode` is only for `<Transition>` because it swaps a single element. Use `<Transition>` if you need in/out sequencing.

**BAD:**
```vue
<template>
  <TransitionGroup name="list" tag="div" mode="out-in">
    <div v-for="item in items" :key="item.id">{{ item.name }}</div>
  </TransitionGroup>
</template>
```

**GOOD:**
```vue
<template>
  <Transition name="fade" mode="out-in">
    <component :is="currentView" :key="currentView" />
  </Transition>
</template>
```

## Stagger List Animations with Data Attributes

For cascading list animations, pass the index to JavaScript hooks and compute delay per item.

```vue
<template>
  <TransitionGroup
    tag="ul"
    :css="false"
    @before-enter="onBeforeEnter"
    @enter="onEnter"
  >
    <li v-for="(item, index) in items" :key="item.id" :data-index="index">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>

<script setup>
function onBeforeEnter(el) {
  el.style.opacity = 0
  el.style.transform = 'translateY(12px)'
}

function onEnter(el, done) {
  const delay = Number(el.dataset.index) * 80
  setTimeout(() => {
    el.style.transition = 'all 0.25s ease'
    el.style.opacity = 1
    el.style.transform = 'translateY(0)'
    setTimeout(done, 250)
  }, delay)
}
</script>
```
```

## File: `skills/vue-best-practices/references/component-transition.md`
```markdown
---
title: Transition Component Best Practices
impact: MEDIUM
impactDescription: Transition animates a single element or component; incorrect structure or keys prevent animations
type: best-practice
tags: [vue3, transition, animation, performance, keys]
---

# Transition Component Best Practices

**Impact: MEDIUM** - `<Transition>` animates entering/leaving of a single element or component. It is ideal for toggling UI states, swapping views, or animating one component at a time.

## Task List

- Wrap a single element or component inside `<Transition>`
- Provide a `key` when switching between same element types
- Use `mode="out-in"` when you need sequential swaps
- Prefer `transform` and `opacity` for smooth animations

## Use Transition for a Single Root Element

`<Transition>` only supports one direct child. Wrap multiple nodes in a single element or component.

**BAD:**
```vue
<template>
  <Transition name="fade">
    <h3>Title</h3>
    <p>Description</p>
  </Transition>
</template>
```

**GOOD:**
```vue
<template>
  <Transition name="fade">
    <div>
      <h3>Title</h3>
      <p>Description</p>
    </div>
  </Transition>
</template>
```

## Force Transitions Between Same Element Types

Vue reuses the same DOM element when the tag type does not change. Add `key` so Vue treats it as a new element and triggers enter/leave.

**BAD:**
```vue
<template>
  <Transition name="fade">
    <p v-if="isActive">Active</p>
    <p v-else>Inactive</p>
  </Transition>
</template>
```

**GOOD:**
```vue
<template>
  <Transition name="fade" mode="out-in">
    <p v-if="isActive" key="active">Active</p>
    <p v-else key="inactive">Inactive</p>
  </Transition>
</template>
```

## Use `mode` to Avoid Overlap During Swaps

When swapping components or views, use `mode="out-in"` to prevent both from being visible at the same time.

**BAD:**
```vue
<template>
  <Transition name="fade">
    <component :is="currentView" />
  </Transition>
</template>
```

**GOOD:**
```vue
<template>
  <Transition name="fade" mode="out-in">
    <component :is="currentView" :key="currentView" />
  </Transition>
</template>
```

## Animate `transform` and `opacity` for Performance

Avoid layout-triggering properties such as `height`, `margin`, or `top`. Use `transform` and `opacity` for smooth, GPU-friendly transitions.

**BAD:**
```css
.slide-enter-active,
.slide-leave-active {
  transition: height 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  height: 0;
}
```

**GOOD:**
```css
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-enter-from {
  transform: translateX(-12px);
  opacity: 0;
}

.slide-leave-to {
  transform: translateX(12px);
  opacity: 0;
}
```
```

## File: `skills/vue-best-practices/references/composables.md`
```markdown
---
title: Composable Organization Patterns
impact: MEDIUM
impactDescription: Well-structured composables improve maintainability, reusability, and update performance
type: best-practice
tags: [vue3, composables, composition-api, code-organization, api-design, readonly, utilities]
---

# Composable Organization Patterns

**Impact: MEDIUM** - Treat composables as reusable, stateful building blocks and keep their code organized by feature concern. This keeps large components maintainable and prevents hard-to-debug mutation and API design issues.

## Task List

- Compose complex behavior from small, focused composables
- Use options objects for composables with multiple optional parameters
- Return readonly state when updates must flow through explicit actions
- Keep pure utility functions as plain utilities, not composables
- Organize composable and component code by feature concern, and extract composables when components grow

## Compose Composables from Smaller Primitives

**BAD:**
```vue
<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const x = ref(0)
const y = ref(0)
const inside = ref(false)
const el = ref(null)

function onMove(e) {
  x.value = e.pageX
  y.value = e.pageY
  if (!el.value) return
  const r = el.value.getBoundingClientRect()
  inside.value = x.value >= r.left && x.value <= r.right &&
    y.value >= r.top && y.value <= r.bottom
}

onMounted(() => window.addEventListener('mousemove', onMove))
onUnmounted(() => window.removeEventListener('mousemove', onMove))
</script>
```

**GOOD:**
```javascript
// composables/useEventListener.js
import { onMounted, onUnmounted, toValue } from 'vue'

export function useEventListener(target, event, callback) {
  onMounted(() => toValue(target).addEventListener(event, callback))
  onUnmounted(() => toValue(target).removeEventListener(event, callback))
}
```

```javascript
// composables/useMouse.js
import { ref } from 'vue'
import { useEventListener } from './useEventListener'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  useEventListener(window, 'mousemove', (e) => {
    x.value = e.pageX
    y.value = e.pageY
  })

  return { x, y }
}
```

```javascript
// composables/useMouseInElement.js
import { computed } from 'vue'
import { useMouse } from './useMouse'

export function useMouseInElement(elementRef) {
  const { x, y } = useMouse()

  const isOutside = computed(() => {
    if (!elementRef.value) return true
    const rect = elementRef.value.getBoundingClientRect()
    return x.value < rect.left || x.value > rect.right ||
      y.value < rect.top || y.value > rect.bottom
  })

  return { x, y, isOutside }
}
```

## Use Options Object Pattern for Composable Parameters

**BAD:**
```javascript
export function useFetch(url, method, headers, timeout, retries, immediate) {
  // hard to read and easy to misorder
}

useFetch('/api/users', 'GET', null, 5000, 3, true)
```

**GOOD:**
```javascript
export function useFetch(url, options = {}) {
  const {
    method = 'GET',
    headers = {},
    timeout = 30000,
    retries = 0,
    immediate = true
  } = options

  // implementation
  return { method, headers, timeout, retries, immediate }
}

useFetch('/api/users', {
  method: 'POST',
  timeout: 5000,
  retries: 3
})
```

```typescript
interface UseCounterOptions {
  initial?: number
  min?: number
  max?: number
  step?: number
}

export function useCounter(options: UseCounterOptions = {}) {
  const { initial = 0, min = -Infinity, max = Infinity, step = 1 } = options
  // implementation
}
```

## Return Readonly State with Explicit Actions

**BAD:**
```javascript
export function useCart() {
  const items = ref([])
  const total = computed(() => items.value.reduce((sum, item) => sum + item.price, 0))
  return { items, total } // any consumer can mutate directly
}

const { items } = useCart()
items.value.push({ id: 1, price: 10 })
```

**GOOD:**
```javascript
import { ref, computed, readonly } from 'vue'

export function useCart() {
  const _items = ref([])

  const total = computed(() =>
    _items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  )

  function addItem(product, quantity = 1) {
    const existing = _items.value.find(item => item.id === product.id)
    if (existing) {
      existing.quantity += quantity
      return
    }
    _items.value.push({ ...product, quantity })
  }

  function removeItem(productId) {
    _items.value = _items.value.filter(item => item.id !== productId)
  }

  return {
    items: readonly(_items),
    total,
    addItem,
    removeItem
  }
}
```

## Keep Utilities as Utilities

**BAD:**
```javascript
export function useFormatters() {
  const formatDate = (date) => new Intl.DateTimeFormat('en-US').format(date)
  const formatCurrency = (amount) =>
    new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount)
  return { formatDate, formatCurrency }
}

const { formatDate } = useFormatters()
```

**GOOD:**
```javascript
// utils/formatters.js
export function formatDate(date) {
  return new Intl.DateTimeFormat('en-US').format(date)
}

export function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount)
}
```

```javascript
// composables/useInvoiceSummary.js
import { computed } from 'vue'
import { formatCurrency } from '@/utils/formatters'

export function useInvoiceSummary(invoiceRef) {
  const totalLabel = computed(() => formatCurrency(invoiceRef.value.total))
  return { totalLabel }
}
```

## Organize Composable and Component Code by Feature Concern

**BAD:**
```vue
<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const searchQuery = ref('')
const items = ref([])
const selected = ref(null)
const showModal = ref(false)
const sortBy = ref('name')
const filter = ref('all')
const loading = ref(false)

const filtered = computed(() => items.value.filter(i => i.category === filter.value))
function openModal() { showModal.value = true }
const sorted = computed(() => [...filtered.value].sort(/* ... */))
watch(searchQuery, () => { /* ... */ })
onMounted(() => { /* ... */ })
</script>
```

**GOOD:**
```vue
<script setup>
import { useItems } from '@/composables/useItems'
import { useSearch } from '@/composables/useSearch'
import { useSelectionModal } from '@/composables/useSelectionModal'

// Data
const { items, loading, fetchItems } = useItems()

// Search/filter/sort
const { query, visibleItems } = useSearch(items)

// Selection + modal
const { selectedItem, isModalOpen, selectItem, closeModal } = useSelectionModal()
</script>
```

```javascript
// composables/useItems.js
import { ref, onMounted } from 'vue'

export function useItems() {
  const items = ref([])
  const loading = ref(false)

  async function fetchItems() {
    loading.value = true
    try {
      items.value = await api.getItems()
    } finally {
      loading.value = false
    }
  }

  onMounted(fetchItems)
  return { items, loading, fetchItems }
}
```
```

## File: `skills/vue-best-practices/references/directives.md`
```markdown
---
title: Directive Best Practices
impact: MEDIUM
impactDescription: Custom directives are powerful but easy to misuse; following patterns prevents leaks, invalid usage, and unclear abstractions
type: best-practice
tags: [vue3, directives, custom-directives, composition, typescript]
---

# Directive Best Practices

**Impact: MEDIUM** - Directives are for low-level DOM access. Use them sparingly, keep them side-effect safe, and prefer components or composables when you need stateful or reusable UI behavior.

## Task List

- Use directives only when you need direct DOM access
- Do not mutate directive arguments or binding objects
- Clean up timers, listeners, and observers in `unmounted`
- Register directives in `<script setup>` with the `v-` prefix
- In TypeScript projects, type directive values and augment template directive types
- Prefer components or composables for complex behavior

## Treat Directive Arguments as Read-Only

Directive bindings are not reactive storage. Don’t write to them.

```ts
const vFocus = {
  mounted(el, binding) {
    // binding.value is read-only
    el.focus()
  }
}
```

## Avoid Directives on Components

Directives apply to DOM elements. When used on components, they attach to the root element and can break if the root changes.

**BAD:**
```vue
<MyInput v-focus />
```

**GOOD:**
```vue
<!-- MyInput.vue -->
<script setup>
const vFocus = (el) => el.focus()
</script>

<template>
  <input v-focus />
</template>
```

## Clean Up Side Effects in `unmounted`

Any timers, listeners, or observers must be removed to avoid leaks.

```ts
const vResize = {
  mounted(el) {
    const observer = new ResizeObserver(() => {})
    observer.observe(el)
    el._observer = observer
  },
  unmounted(el) {
    el._observer?.disconnect()
  }
}
```

## Prefer Function Shorthand for Single-Hook Directives

If you only need `mounted`/`updated`, use the function form.

```ts
const vAutofocus = (el) => el.focus()
```

## Use the `v-` Prefix and Script Setup Registration

```vue
<script setup>
const vFocus = (el) => el.focus()
</script>

<template>
  <input v-focus />
</template>
```

## Type Custom Directives in TypeScript Projects

Use `Directive<Element, ValueType>` so `binding.value` is typed, and augment Vue's template types so directives are recognized in SFC templates.

**BAD:**
```ts
// Untyped directive value and no template type augmentation
export const vHighlight = {
  mounted(el, binding) {
    el.style.backgroundColor = binding.value
  }
}
```

**GOOD:**
```ts
import type { Directive } from 'vue'

type HighlightValue = string

export const vHighlight = {
  mounted(el, binding) {
    el.style.backgroundColor = binding.value
  }
} satisfies Directive<HTMLElement, HighlightValue>

declare module 'vue' {
  interface ComponentCustomProperties {
    vHighlight: typeof vHighlight
  }
}
```

## Handle SSR with `getSSRProps`

Directive hooks such as `mounted` and `updated` do not run during SSR. If a directive sets attributes/classes that affect rendered HTML, provide an SSR equivalent via `getSSRProps` to avoid hydration mismatches.

**BAD:**
```ts
const vTooltip = {
  mounted(el, binding) {
    el.setAttribute('data-tooltip', binding.value)
    el.classList.add('has-tooltip')
  }
}
```

**GOOD:**
```ts
const vTooltip = {
  mounted(el, binding) {
    el.setAttribute('data-tooltip', binding.value)
    el.classList.add('has-tooltip')
  },
  getSSRProps(binding) {
    return {
      'data-tooltip': binding.value,
      class: 'has-tooltip'
    }
  }
}
```

## Prefer Declarative Templates When Possible

If a standard attribute or binding works, use it instead of a directive.

## Decide Between Directives and Components

Use a directive for DOM-level behavior. Use a component when behavior affects structure, state, or rendering.
```

## File: `skills/vue-best-practices/references/perf-avoid-component-abstraction-in-lists.md`
```markdown
---
title: Avoid Excessive Component Abstraction in Large Lists
impact: MEDIUM
impactDescription: Each component instance has memory and render overhead - abstractions multiply this in lists
type: efficiency
tags: [vue3, performance, components, abstraction, lists, optimization]
---

# Avoid Excessive Component Abstraction in Large Lists

**Impact: MEDIUM** - Component instances are more expensive than plain DOM nodes. While abstractions improve code organization, unnecessary nesting creates overhead. In large lists, this overhead multiplies - 100 items with 3 levels of abstraction means 300+ component instances instead of 100.

Don't avoid abstraction entirely, but be mindful of component depth in frequently-rendered elements like list items.

## Task List

- Review list item components for unnecessary wrapper components
- Consider flattening component hierarchies in hot paths
- Use native elements when a component adds no value
- Profile component counts using Vue DevTools
- Focus optimization efforts on the most-rendered components

**BAD:**
```vue
<!-- BAD: Deep abstraction in list items -->
<template>
  <div class="user-list">
    <!-- For 100 users: Creates 400 component instances -->
    <UserCard v-for="user in users" :key="user.id" :user="user" />
  </div>
</template>

<!-- UserCard.vue -->
<template>
  <Card>  <!-- Wrapper component #1 -->
    <CardHeader>  <!-- Wrapper component #2 -->
      <UserAvatar :src="user.avatar" />  <!-- Wrapper component #3 -->
    </CardHeader>
    <CardBody>  <!-- Wrapper component #4 -->
      <Text>{{ user.name }}</Text>
    </CardBody>
  </Card>
</template>

<!-- Each UserCard creates: Card + CardHeader + CardBody + UserAvatar + Text
     100 users = 500+ component instances -->
```

**GOOD:**
```vue
<!-- GOOD: Flattened structure in list items -->
<template>
  <div class="user-list">
    <!-- For 100 users: Creates 100 component instances -->
    <UserCard v-for="user in users" :key="user.id" :user="user" />
  </div>
</template>

<!-- UserCard.vue - Flattened, uses native elements -->
<template>
  <div class="card">
    <div class="card-header">
      <img :src="user.avatar" :alt="user.name" class="avatar" />
    </div>
    <div class="card-body">
      <span class="user-name">{{ user.name }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  user: Object
})
</script>

<style scoped>
/* Styles that would have been in Card, CardHeader, etc. */
.card { /* ... */ }
.card-header { /* ... */ }
.card-body { /* ... */ }
.avatar { /* ... */ }
</style>
```

## When Abstraction Is Still Worth It

```vue
<!-- Component abstraction is valuable when: -->

<!-- 1. Complex behavior is encapsulated -->
<UserStatusIndicator :user="user" />  <!-- Has logic, tooltips, etc. -->

<!-- 2. Reused outside of the hot path -->
<Card>  <!-- OK to use in one-off places, not in 100-item lists -->

<!-- 3. The list itself is small -->
<template v-if="items.length < 20">
  <FancyItem v-for="item in items" :key="item.id" />
</template>

<!-- 4. Virtualization is used (only ~20 items rendered at once) -->
<RecycleScroller :items="items">
  <template #default="{ item }">
    <ComplexItem :item="item" />  <!-- OK - only 20 instances exist -->
  </template>
</RecycleScroller>
```

## Measuring Component Overhead

```javascript
// In development, profile component counts
import { onMounted, getCurrentInstance } from 'vue'

onMounted(() => {
  const instance = getCurrentInstance()
  let count = 0

  function countComponents(vnode) {
    if (vnode.component) count++
    if (vnode.children) {
      vnode.children.forEach(child => {
        if (child.component || child.children) countComponents(child)
      })
    }
  }

  // Use Vue DevTools instead for accurate counts
  console.log('Check Vue DevTools Components tab for instance counts')
})
```

## Alternatives to Wrapper Components

```vue
<!-- Instead of a <Button> component for styling: -->
<button class="btn btn-primary">Click</button>

<!-- Instead of a <Text> component: -->
<span class="text-body">{{ content }}</span>

<!-- Instead of layout wrapper components in lists: -->
<div class="flex items-center gap-2">
  <!-- content -->
</div>

<!-- Use CSS classes or Tailwind instead of component abstractions for styling -->
```

## Impact Calculation

| List Size | Components per Item | Total Instances | Memory Impact |
|-----------|---------------------|-----------------|---------------|
| 100 items | 1 (flat) | 100 | Baseline |
| 100 items | 3 (nested) | 300 | ~3x memory |
| 100 items | 5 (deeply nested) | 500 | ~5x memory |
| 1000 items | 1 (flat) | 1000 | High |
| 1000 items | 5 (deeply nested) | 5000 | Very High |
```

## File: `skills/vue-best-practices/references/perf-v-once-v-memo-directives.md`
```markdown
---
title: Use v-once and v-memo to Skip Unnecessary Updates
impact: MEDIUM
impactDescription: v-once skips all future updates for static content; v-memo conditionally memoizes subtrees
type: efficiency
tags: [vue3, performance, v-once, v-memo, optimization, directives]
---

# Use v-once and v-memo to Skip Unnecessary Updates

**Impact: MEDIUM** - Vue re-evaluates templates on every reactive change. For content that never changes or changes infrequently, `v-once` and `v-memo` tell Vue to skip updates, reducing render work.

Use `v-once` for truly static content and `v-memo` for conditionally-static content in lists.

## Task List

- Apply `v-once` to elements that use runtime data but never need updating
- Apply `v-memo` to list items that should only update on specific condition changes
- Verify memoized content doesn't need to respond to other state changes
- Profile with Vue DevTools to confirm update skipping

## v-once: Render Once, Never Update

**BAD:**
```vue
<template>
  <!-- BAD: Re-evaluated on every parent re-render -->
  <div class="terms-content">
    <h1>Terms of Service</h1>
    <p>Version: {{ termsVersion }}</p>
    <div v-html="termsContent"></div>
  </div>

  <!-- This content NEVER changes, but Vue checks it every render -->
  <footer>
    <p>Copyright {{ copyrightYear }} {{ companyName }}</p>
  </footer>
</template>
```

**GOOD:**
```vue
<template>
  <!-- GOOD: Rendered once, skipped on all future updates -->
  <div class="terms-content" v-once>
    <h1>Terms of Service</h1>
    <p>Version: {{ termsVersion }}</p>
    <div v-html="termsContent"></div>
  </div>

  <!-- v-once tells Vue this never needs to update -->
  <footer v-once>
    <p>Copyright {{ copyrightYear }} {{ companyName }}</p>
  </footer>
</template>

<script setup>
// These values are set once at component creation
const termsVersion = '2.1'
const termsContent = fetchedTermsHTML
const copyrightYear = 2024
const companyName = 'Acme Corp'
</script>
```

## v-memo: Conditional Memoization for Lists

**BAD:**
```vue
<template>
  <!-- BAD: All items re-render when selectedId changes -->
  <div v-for="item in list" :key="item.id">
    <div :class="{ selected: item.id === selectedId }">
      <ExpensiveComponent :data="item" />
    </div>
  </div>
</template>
```

**GOOD:**
```vue
<template>
  <!-- GOOD: Items only re-render when their selection state changes -->
  <div
    v-for="item in list"
    :key="item.id"
    v-memo="[item.id === selectedId]"
  >
    <div :class="{ selected: item.id === selectedId }">
      <ExpensiveComponent :data="item" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const list = ref([/* many items */])
const selectedId = ref(null)

// When selectedId changes:
// - Only the previously-selected item re-renders (selected: true -> false)
// - Only the newly-selected item re-renders (selected: false -> true)
// - All other items are SKIPPED (v-memo values unchanged)
</script>
```

## v-memo with Multiple Dependencies

```vue
<template>
  <!-- Re-render only when item's selection OR editing state changes -->
  <div
    v-for="item in items"
    :key="item.id"
    v-memo="[item.id === selectedId, item.id === editingId]"
  >
    <ItemCard
      :item="item"
      :selected="item.id === selectedId"
      :editing="item.id === editingId"
    />
  </div>
</template>

<script setup>
const selectedId = ref(null)
const editingId = ref(null)
const items = ref([/* ... */])
</script>
```

## v-memo with Empty Array = v-once

```vue
<template>
  <!-- v-memo="[]" is equivalent to v-once -->
  <div v-for="item in staticList" :key="item.id" v-memo="[]">
    {{ item.name }}
  </div>
</template>
```

## When NOT to Use These Directives

```vue
<template>
  <!-- DON'T: Content that DOES need to update -->
  <div v-once>
    <span>Count: {{ count }}</span>  <!-- count won't update! -->
  </div>

  <!-- DON'T: When child components have their own reactive state -->
  <div v-memo="[selected]">
    <InputField v-model="item.name" />  <!-- v-model won't work properly -->
  </div>

  <!-- DON'T: When the memoization benefit is minimal -->
  <span v-once>{{ simpleText }}</span>  <!-- Overhead not worth it -->
</template>
```

## Performance Comparison

| Scenario | Without Directive | With v-once/v-memo |
|----------|-------------------|-------------------|
| Static header, parent re-renders 100x | Re-evaluated 100x | Evaluated 1x |
| 1000 items, selection changes | 1000 items re-render | 2 items re-render |
| Complex child component | Full re-render | Skipped if memoized |

## Debugging Memoized Components

```vue
<script setup>
import { onUpdated } from 'vue'

// This won't fire if v-memo prevents update
onUpdated(() => {
  console.log('Component updated')
})
</script>
```
```

## File: `skills/vue-best-practices/references/perf-virtualize-large-lists.md`
```markdown
---
title: Virtualize Large Lists to Avoid DOM Overload
impact: HIGH
impactDescription: Rendering thousands of list items creates excessive DOM nodes, causing slow renders and high memory usage
type: efficiency
tags: [vue3, performance, virtual-list, large-data, dom, optimization]
---

# Virtualize Large Lists to Avoid DOM Overload

**Impact: HIGH** - Rendering all items in a large list (hundreds or thousands) creates massive amounts of DOM nodes. Each node consumes memory, slows down initial render, and makes updates expensive. List virtualization only renders visible items, dramatically improving performance.

Use a virtualization library when dealing with lists that could exceed 50-100 items, especially if items have complex content.

## Task List

- Identify lists that render more than 50-100 items
- Install a virtualization library (vue-virtual-scroller, @tanstack/vue-virtual)
- Replace standard `v-for` with virtualized component
- Ensure list items have consistent or estimable heights
- Test with realistic data volumes during development

## Recommended Libraries

| Library | Best For | Notes |
|---------|----------|-------|
| `vue-virtual-scroller` | General use, easy setup | Most popular, good defaults |
| `@tanstack/vue-virtual` | Complex layouts, headless | Framework-agnostic, flexible |
| `vue-virtual-scroll-grid` | Grid layouts | 2D virtualization |
| `vueuc/VVirtualList` | Naive UI projects | Part of Naive UI ecosystem |

**BAD:**
```vue
<template>
  <!-- BAD: Renders ALL 10,000 items immediately -->
  <div class="user-list">
    <UserCard
      v-for="user in users"
      :key="user.id"
      :user="user"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import UserCard from './UserCard.vue'

const users = ref([])

onMounted(async () => {
  // 10,000 DOM nodes created, browser struggles
  users.value = await fetchAllUsers()
})
</script>
```

**GOOD:**
```vue
<template>
  <!-- GOOD: Only renders ~20 visible items at a time -->
  <RecycleScroller
    class="user-list"
    :items="users"
    :item-size="80"
    key-field="id"
    v-slot="{ item }"
  >
    <UserCard :user="item" />
  </RecycleScroller>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RecycleScroller } from 'vue-virtual-scroller'
import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'
import UserCard from './UserCard.vue'

const users = ref([])

onMounted(async () => {
  // 10,000 items in memory, but only ~20 DOM nodes
  users.value = await fetchAllUsers()
})
</script>

<style scoped>
.user-list {
  height: 600px; /* Container must have fixed height */
}
</style>
```

## Using @tanstack/vue-virtual

```vue
<template>
  <div ref="parentRef" class="list-container">
    <div
      :style="{
        height: `${rowVirtualizer.getTotalSize()}px`,
        position: 'relative'
      }"
    >
      <div
        v-for="virtualRow in rowVirtualizer.getVirtualItems()"
        :key="virtualRow.key"
        :style="{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: `${virtualRow.size}px`,
          transform: `translateY(${virtualRow.start}px)`
        }"
      >
        <UserCard :user="users[virtualRow.index]" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useVirtualizer } from '@tanstack/vue-virtual'

const users = ref([/* 10,000 users */])
const parentRef = ref(null)

const rowVirtualizer = useVirtualizer({
  count: users.value.length,
  getScrollElement: () => parentRef.value,
  estimateSize: () => 80,  // Estimated row height
  overscan: 5  // Render 5 extra items above/below viewport
})
</script>

<style scoped>
.list-container {
  height: 600px;
  overflow: auto;
}
</style>
```

## Dynamic Heights with vue-virtual-scroller

```vue
<template>
  <!-- For variable height items, use DynamicScroller -->
  <DynamicScroller
    :items="messages"
    :min-item-size="54"
    key-field="id"
  >
    <template #default="{ item, index, active }">
      <DynamicScrollerItem
        :item="item"
        :active="active"
        :data-index="index"
      >
        <ChatMessage :message="item" />
      </DynamicScrollerItem>
    </template>
  </DynamicScroller>
</template>

<script setup>
import { DynamicScroller, DynamicScrollerItem } from 'vue-virtual-scroller'
</script>
```

## Performance Comparison

| Approach | 100 Items | 1,000 Items | 10,000 Items |
|----------|-----------|-------------|--------------|
| Regular v-for | ~100 DOM nodes | ~1,000 DOM nodes | ~10,000 DOM nodes |
| Virtualized | ~20 DOM nodes | ~20 DOM nodes | ~20 DOM nodes |
| Initial render | Fast | Slow | Very slow / crashes |
| Virtualized render | Fast | Fast | Fast |

## When NOT to Virtualize

- Lists under 50 items with simple content
- Lists where all items must be accessible to screen readers simultaneously
- Print layouts where all content must render
- SEO-critical content that must be in initial HTML
```

## File: `skills/vue-best-practices/references/plugins.md`
```markdown
---
title: Vue Plugin Best Practices
impact: MEDIUM
impactDescription: Incorrect plugin structure or injection key strategy causes install failures, collisions, and unsafe APIs
type: best-practice
tags: [vue3, plugins, provide-inject, typescript, dependency-injection]
---

# Vue Plugin Best Practices

**Impact: MEDIUM** - Vue plugins should follow the `app.use()` contract, expose explicit capabilities, and use collision-safe injection keys. This keeps plugin setup predictable and composable across large apps.

## Task List

- Export plugins as an object with `install()` or as an install function
- Use the `app` instance in `install()` to register components/directives/provides
- Type plugin APIs with `Plugin` (and options tuple types when needed)
- Use symbol keys (prefer `InjectionKey<T>`) for `provide/inject` in plugins
- Add a small typed composable wrapper for required injections to fail fast

## Structure Plugins for `app.use()`

A Vue plugin must be either:
- An object with `install(app, options?)`
- A function with the same signature

**BAD:**
```ts
const notAPlugin = {
  doSomething() {}
}

app.use(notAPlugin)
```

**GOOD:**
```ts
import type { App } from 'vue'

interface PluginOptions {
  prefix?: string
  debug?: boolean
}

const myPlugin = {
  install(app: App, options: PluginOptions = {}) {
    const { prefix = 'my', debug = false } = options

    if (debug) {
      console.log('Installing myPlugin with prefix:', prefix)
    }

    app.provide('myPlugin', { prefix })
  }
}

app.use(myPlugin, { prefix: 'custom', debug: true })
```

**GOOD:**
```ts
import type { App } from 'vue'

function simplePlugin(app: App, options?: { message: string }) {
  app.config.globalProperties.$greet = () => options?.message ?? 'Hello!'
}

app.use(simplePlugin, { message: 'Welcome!' })
```

## Register Capabilities Explicitly in `install()`

Inside `install()`, wire behavior through Vue application APIs:
- `app.component()` for global components
- `app.directive()` for global directives
- `app.provide()` for injectable services and config
- `app.config.globalProperties` for optional global helpers (sparingly)

**BAD:**
```ts
const uselessPlugin = {
  install(app, options) {
    const service = createService(options)
  }
}
```

**GOOD:**
```ts
const usefulPlugin = {
  install(app, options) {
    const service = createService(options)
    app.provide(serviceKey, service)
  }
}
```

## Type Plugin Contracts

Use Vue's `Plugin` type to keep install signatures and options type-safe.

```ts
import type { App, Plugin } from 'vue'

interface MyOptions {
  apiKey: string
}

const myPlugin: Plugin<[MyOptions]> = {
  install(app: App, options: MyOptions) {
    app.provide(apiKeyKey, options.apiKey)
  }
}
```

## Use Symbol Injection Keys in Plugins

String keys can collide (`'http'`, `'config'`, `'i18n'`). Use symbol keys with `InjectionKey<T>` so injections are unique and typed.

**BAD:**
```ts
export default {
  install(app) {
    app.provide('http', axios)
    app.provide('config', appConfig)
  }
}
```

**GOOD:**
```ts
import type { InjectionKey } from 'vue'
import type { AxiosInstance } from 'axios'

interface AppConfig {
  apiUrl: string
  timeout: number
}

export const httpKey: InjectionKey<AxiosInstance> = Symbol('http')
export const configKey: InjectionKey<AppConfig> = Symbol('appConfig')

export default {
  install(app) {
    app.provide(httpKey, axios)
    app.provide(configKey, { apiUrl: '/api', timeout: 5000 })
  }
}
```

## Provide Required Injection Helpers

Wrap required injections in composables that throw clear setup errors.

```ts
import { inject } from 'vue'
import { authKey, type AuthService } from '@/injection-keys'

export function useAuth(): AuthService {
  const auth = inject(authKey)
  if (!auth) {
    throw new Error('Auth plugin not installed. Did you forget app.use(authPlugin)?')
  }
  return auth
}
```
```

## File: `skills/vue-best-practices/references/reactivity.md`
```markdown
---
title: Reactivity Core Patterns (ref, reactive, shallowRef, computed, watch)
impact: MEDIUM
impactDescription: Clear reactivity choices keep state predictable and reduce unnecessary updates in Vue 3 apps
type: efficiency
tags: [vue3, reactivity, ref, reactive, shallowRef, computed, watch, watchEffect, external-state, best-practice]
---

# Reactivity Core Patterns (ref, reactive, shallowRef, computed, watch)

**Impact: MEDIUM** - Choose the right reactive primitive first, derive with `computed`, and use watchers only for side effects.

This reference covers the core reactivity decisions for local state, external data, derived values, and effects.

## Task List

- Declare reactive state correctly
  - Always use `shallowRef()` instead of `ref()` for primitive values
  - Choose the correct reactive declaration method for objects/arrays/map/set
- Follow best practices for `reactive`
  - Avoid destructuring from `reactive()` directly
  - Watch correctly for `reactive`
- Follow best practices for `computed`
  - Prefer `computed` over watcher-assigned derived refs
  - Keep filtered/sorted derivations out of templates
  - Use `computed` for reusable class/style logic
  - Keep computed getters pure (no side effects) and put side effects in watchers
- Follow best practices for watchers
  - Use `immediate: true` instead of duplicate initial calls
  - Clean up async effects for watchers

## Declare reactive state correctly

### Always use `shallowRef()` instead of `ref()` for primitive values (string, number, boolean, null, etc.) for better performance.

**Incorrect:**
```ts
import { ref } from 'vue'
const count = ref(0)
```

**Correct:**
```ts
import { shallowRef } from 'vue'
const count = shallowRef(0)
```

### Choose the correct reactive declaration method for objects/arrays/map/set

Use `ref()` when you often **replace the entire value** (`state.value = newObj`) and still want deep reactivity inside it, usually used for:

- Frequently reassigned state (replace fetched object/list, reset to defaults, switch presets).
- Composable return values where updates happen mostly via `.value` reassignment.

Use `reactive()` when you mainly **mutate properties** and full replacement is uncommon, usually used for:

- “Single state object” patterns (stores/forms): `state.count++`, `state.items.push(...)`, `state.user.name = ...`.
- Situations where you want to avoid `.value` and update nested fields in place.

```ts
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  user: { name: 'Alice', age: 30 }
})

state.count++ // ✅ reactive
state.user.age = 31 // ✅ reactive
// ❌ avoid replacing the reactive object reference:
// state = reactive({ count: 1 })
```

Use `shallowRef()` when the value is **opaque / should not be proxied** (class instances, external library objects, very large nested data) and you only want updates to trigger when you **replace** `state.value` (no deep tracking), usually used for:

- Storing external instances/handles (SDK clients, class instances) without Vue proxying internals.
- Large data where you update by replacing the root reference (immutable-style updates).

```ts
import { shallowRef } from 'vue'

const user = shallowRef({ name: 'Alice', age: 30 })

user.value.age = 31 // ❌ not reactive
user.value = { name: 'Bob', age: 25 } // ✅ triggers update
```

Use `shallowReactive()` when you want **only top-level properties** reactive; nested objects remain raw, usually used for:

- Container objects where only top-level keys change and nested payloads should stay unmanaged/unproxied.
- Mixed structures where Vue tracks the wrapper object, but not deeply nested or foreign objects.

```ts
import { shallowReactive } from 'vue'

const state = shallowReactive({
  count: 0,
  user: { name: 'Alice', age: 30 }
})

state.count++ // ✅ reactive
state.user.age = 31 // ❌ not reactive
```

## Best practices for `reactive`

### Avoid destructuring from `reactive()` directly

**BAD:**

```ts
import { reactive } from 'vue'

const state = reactive({ count: 0 })
const { count } = state // ❌ disconnected from reactivity
```

### Watch correctly for reactive

**BAD:**

passing a non-getter value into `watch()`

```ts
import { reactive, watch } from 'vue'

const state = reactive({ count: 0 })

// ❌ watch expects a getter, ref, reactive object, or array of these
watch(state.count, () => { /* ... */ })
```

**GOOD:**

preserve reactivity with `toRefs()` and use a getter for `watch()`

```ts
import { reactive, toRefs, watch } from 'vue'

const state = reactive({ count: 0 })
const { count } = toRefs(state) // ✅ count is a ref

watch(count, () => { /* ... */ }) // ✅
watch(() => state.count, () => { /* ... */ }) // ✅
```

## Best practices for `computed`

### Prefer `computed` over watcher-assigned derived refs

**BAD:**
```ts
import { ref, watchEffect } from 'vue'

const items = ref([{ price: 10 }, { price: 20 }])
const total = ref(0)

watchEffect(() => {
  total.value = items.value.reduce((sum, item) => sum + item.price, 0)
})
```

**GOOD:**
```ts
import { ref, computed } from 'vue'

const items = ref([{ price: 10 }, { price: 20 }])
const total = computed(() =>
  items.value.reduce((sum, item) => sum + item.price, 0)
)
```

### Keep filtered/sorted derivations out of templates

**BAD:**
```vue
<template>
  <li v-for="item in items.filter(item => item.active)" :key="item.id">
    {{ item.name }}
  </li>

  <li v-for="item in getSortedItems()" :key="item.id">
    {{ item.name }}
  </li>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, name: 'B', active: true },
  { id: 2, name: 'A', active: false }
])

function getSortedItems() {
  return [...items.value].sort((a, b) => a.name.localeCompare(b.name))
}
</script>
```

**GOOD:**
```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([
  { id: 1, name: 'B', active: true },
  { id: 2, name: 'A', active: false }
])

const visibleItems = computed(() =>
  items.value
    .filter(item => item.active)
    .sort((a, b) => a.name.localeCompare(b.name))
)
</script>

<template>
  <li v-for="item in visibleItems" :key="item.id">
    {{ item.name }}
  </li>
</template>
```

### Use `computed` for reusable class/style logic

**BAD:**
```vue
<template>
  <button :class="{ btn: true, 'btn-primary': type === 'primary' && !disabled, 'btn-disabled': disabled }">
    {{ label }}
  </button>
</template>
```

**GOOD:**
```vue
<script setup>
import { computed } from 'vue'

const props = defineProps({
  type: { type: String, default: 'primary' },
  disabled: Boolean,
  label: String
})

const buttonClasses = computed(() => ({
  btn: true,
  [`btn-${props.type}`]: !props.disabled,
  'btn-disabled': props.disabled
}))
</script>

<template>
  <button :class="buttonClasses">
    {{ label }}
  </button>
</template>
```

### Keep computed getters pure (no side effects) and put side effects in watchers instead

A computed getter should only derive a value. No mutation, no API calls, no storage writes, no event emits.
([Reference](https://vuejs.org/guide/essentials/computed.html#best-practices))

**BAD:**

side effects inside computed

```ts
const count = ref(0)

const doubled = computed(() => {
  // ❌ side effect
  if (count.value > 10) console.warn('Too big!')
  return count.value * 2
})
```

**GOOD:**

pure computed + `watch()` for side effects

```ts
const count = ref(0)
const doubled = computed(() => count.value * 2)

watch(count, (value) => {
  if (value > 10) console.warn('Too big!')
})
```

## Best practices for watchers

### Use `immediate: true` instead of duplicate initial calls

**BAD:**
```ts
import { ref, watch, onMounted } from 'vue'

const userId = ref(1)

function loadUser(id) {
  // ...
}

onMounted(() => loadUser(userId.value))
watch(userId, (id) => loadUser(id))
```

**GOOD:**
```ts
import { ref, watch } from 'vue'

const userId = ref(1)

watch(
  userId,
  (id) => loadUser(id),
  { immediate: true }
)
```

### Clean up async effects for watchers

When reacting to rapid changes (search boxes, filters), cancel the previous request.

**GOOD:**

```ts
const query = ref('')
const results = ref<string[]>([])

watch(query, async (q, _prev, onCleanup) => {
  const controller = new AbortController()
  onCleanup(() => controller.abort())

  const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`, {
    signal: controller.signal,
  })

  results.value = await res.json()
})
```
```

## File: `skills/vue-best-practices/references/render-functions.md`
```markdown
---
title: Render Function Patterns and Performance
impact: MEDIUM
impactDescription: Render functions require explicit patterns for lists, events, v-model, and performance to stay correct and maintainable
type: best-practice
tags: [vue3, render-function, h, v-model, directives, performance, jsx]
---

# Render Function Patterns and Performance

**Impact: MEDIUM** - Render functions are powerful but opt out of template compiler optimizations. Use them intentionally and apply the key patterns below to keep output correct and performant.

## Task List

- Prefer templates; use render functions only when templates cannot express the logic
- Always add stable keys when rendering lists with `h()`/JSX
- Use `withModifiers` / `withKeys` for event modifiers
- Implement `v-model` via `modelValue` + `onUpdate:modelValue`
- Apply custom directives with `withDirectives`
- Use functional components for stateless presentational UI

## Prefer templates over render functions

**BAD:**
```vue
<script setup>
import { h, ref } from 'vue'

const count = ref(0)
const render = () => h('div', `Count: ${count.value}`)
</script>
```

**GOOD:**
```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <div>Count: {{ count }}</div>
</template>
```

## Always add keys for list rendering

**BAD:**
```javascript
import { h, ref } from 'vue'

export default {
  setup() {
    const items = ref([{ id: 1, name: 'Apple' }])

    return () => h('ul',
      items.value.map(item => h('li', item.name))
    )
  }
}
```

**GOOD:**
```javascript
import { h, ref } from 'vue'

export default {
  setup() {
    const items = ref([{ id: 1, name: 'Apple' }])

    return () => h('ul',
      items.value.map(item => h('li', { key: item.id }, item.name))
    )
  }
}
```

## Use `withModifiers` / `withKeys` for event modifiers

**BAD:**
```javascript
import { h } from 'vue'

export default {
  setup() {
    const handleClick = (e) => {
      e.stopPropagation()
      e.preventDefault()
    }

    return () => h('button', { onClick: handleClick }, 'Click')
  }
}
```

**GOOD:**
```javascript
import { h, withModifiers, withKeys } from 'vue'

export default {
  setup() {
    const handleClick = () => {}
    const handleEnter = () => {}

    return () => h('div', [
      h('button', {
        onClick: withModifiers(handleClick, ['stop', 'prevent'])
      }, 'Click'),
      h('input', {
        onKeyup: withKeys(handleEnter, ['enter'])
      })
    ])
  }
}
```

## Implement `v-model` explicitly

**BAD:**
```javascript
import { h, ref } from 'vue'
import CustomInput from './CustomInput.vue'

export default {
  setup() {
    const text = ref('')
    return () => h(CustomInput, { modelValue: text.value })
  }
}
```

**GOOD:**
```javascript
import { h, ref } from 'vue'
import CustomInput from './CustomInput.vue'

export default {
  setup() {
    const text = ref('')
    return () => h(CustomInput, {
      modelValue: text.value,
      'onUpdate:modelValue': (value) => { text.value = value }
    })
  }
}
```

## Use `withDirectives` for custom directives

**BAD:**
```javascript
import { h } from 'vue'

const vFocus = { mounted: (el) => el.focus() }

export default {
  setup() {
    return () => h('input', { 'v-focus': true })
  }
}
```

**GOOD:**
```javascript
import { h, withDirectives } from 'vue'

const vFocus = { mounted: (el) => el.focus() }

export default {
  setup() {
    return () => withDirectives(h('input'), [[vFocus]])
  }
}
```

## Prefer functional components for stateless UI

**BAD:**
```javascript
import { h } from 'vue'

export default {
  setup() {
    return () => h('span', { class: 'badge' }, 'New')
  }
}
```

**GOOD:**
```javascript
import { h } from 'vue'

function Badge(props, { slots }) {
  return h('span', { class: 'badge' }, slots.default?.())
}

Badge.props = ['variant']

export default Badge
```
```

## File: `skills/vue-best-practices/references/sfc.md`
```markdown
---
title: Single-File Component Structure, Styling, and Template Patterns
impact: MEDIUM
impactDescription: Consistent SFC structure and styling choices improve maintainability, tooling support, and render performance
type: best-practice
tags: [vue3, sfc, scoped-css, styles, build-tools, performance, template, v-html, v-for, computed, v-if, v-show]
---

# Single-File Component Structure, Styling, and Template Patterns

**Impact: MEDIUM** - Using SFCs with consistent structure and performant styling keeps components easier to maintain and avoids unnecessary render overhead.

## Task List

- Use `.vue` SFCs instead of separate `.js`/`.ts` and `.css` files for components
- Colocate template, script, and styles in the same SFC by default
- Use PascalCase for component names in templates and filenames
- Prefer component-scoped styles
- Prefer class selectors (not element selectors) in scoped CSS for performance
- Access DOM / component refs with `useTemplateRef()` in Vue 3.5+
- Use camelCase keys in `:style` bindings for consistency and IDE support
- Use `v-for` and `v-if` correctly
- Never use `v-html` with untrusted/user-provided content
- Choose `v-if` vs `v-show` based on toggle frequency and initial render cost

## Colocate template, script, and styles

**BAD:**
```
components/
├── UserCard.vue
├── UserCard.js
└── UserCard.css
```

**GOOD:**
```vue
<!-- components/UserCard.vue -->
<script setup>
import { computed } from 'vue'

const props = defineProps({
  user: { type: Object, required: true }
})

const displayName = computed(() =>
  `${props.user.firstName} ${props.user.lastName}`
)
</script>

<template>
  <div class="user-card">
    <h3 class="name">{{ displayName }}</h3>
  </div>
</template>

<style scoped>
.user-card {
  padding: 1rem;
}

.name {
  margin: 0;
}
</style>
```

## Use PascalCase for component names

**BAD:**
```vue
<script setup>
import userProfile from './user-profile.vue'
</script>

<template>
  <user-profile :user="currentUser" />
</template>
```

**GOOD:**
```vue
<script setup>
import UserProfile from './UserProfile.vue'
</script>

<template>
  <UserProfile :user="currentUser" />
</template>
```

## Best practices for `<style>` block in SFCs

### Prefer component-scoped styles

- Use `<style scoped>` for styles that belong to a component.
- Keep **global CSS** in a dedicated file (e.g. `src/assets/main.css`) for resets, typography, tokens, etc.
- Use `:deep()` sparingly (edge cases only).

**BAD:**

```vue
<style>
/* ❌ leaks everywhere */
button { border-radius: 999px; }
</style>
```

**GOOD:**

```vue
<style scoped>
.button { border-radius: 999px; }
</style>
```

**GOOD:**

```css
/* src/assets/main.css */
/* ✅ resets, tokens, typography, app-wide rules */
:root { --radius: 999px; }
```

### Use class selectors in scoped CSS

**BAD:**
```vue
<template>
  <article>
    <h1>{{ title }}</h1>
    <p>{{ subtitle }}</p>
  </article>
</template>

<style scoped>
article { max-width: 800px; }
h1 { font-size: 2rem; }
p { line-height: 1.6; }
</style>
```

**GOOD:**
```vue
<template>
  <article class="article">
    <h1 class="article-title">{{ title }}</h1>
    <p class="article-subtitle">{{ subtitle }}</p>
  </article>
</template>

<style scoped>
.article { max-width: 800px; }
.article-title { font-size: 2rem; }
.article-subtitle { line-height: 1.6; }
</style>
```

## Access DOM / component refs with `useTemplateRef()`

For Vue 3.5+: use `useTemplateRef()` to access template refs.

```vue
<script setup lang="ts">
import { onMounted, useTemplateRef } from 'vue'

const inputRef = useTemplateRef<HTMLInputElement>('input')

onMounted(() => {
  inputRef.value?.focus()
})
</script>

<template>
  <input ref="input" />
</template>
```

## Use camelCase in `:style` bindings

**BAD:**
```vue
<template>
  <div :style="{ 'font-size': fontSize + 'px', 'background-color': bg }">
    Content
  </div>
</template>
```

**GOOD:**
```vue
<template>
  <div :style="{ fontSize: fontSize + 'px', backgroundColor: bg }">
    Content
  </div>
</template>
```

## Use `v-for` and `v-if` correctly

### Always provide a stable `:key`

- Prefer primitive keys (`string | number`).
- Avoid using objects as keys.

**GOOD:**

```vue
<li v-for="item in items" :key="item.id">
  <input v-model="item.text" />
</li>
```

### Avoid `v-if` and `v-for` on the same element

It leads to unclear intent and unnecessary work.
([Reference](https://vuejs.org/guide/essentials/list.html#v-for-with-v-if))

**To filter items**
**BAD:**

```vue
<li v-for="user in users" v-if="user.active" :key="user.id">
  {{ user.name }}
</li>
```

**GOOD:**

```vue
<script setup lang="ts">
import { computed } from 'vue'

const activeUsers = computed(() => users.value.filter(u => u.active))
</script>

<template>
  <li v-for="user in activeUsers" :key="user.id">
    {{ user.name }}
  </li>
</template>
```

**To conditionally show/hide the entire list**
**GOOD:**

```vue
<ul v-if="shouldShowUsers">
  <li v-for="user in users" :key="user.id">
    {{ user.name }}
  </li>
</ul>
```

## Never render untrusted HTML with `v-html`

**BAD:**
```vue
<template>
  <!-- DANGEROUS: untrusted input can inject scripts -->
  <article v-html="userProvidedContent"></article>
</template>
```

**GOOD:**
```vue
<script setup>
import { computed } from 'vue'
import DOMPurify from 'dompurify'

const props = defineProps<{
  trustedHtml?: string
  plainText: string
}>()

const safeHtml = computed(() => DOMPurify.sanitize(props.trustedHtml ?? ''))
</script>

<template>
  <!-- Preferred: escaped interpolation -->
  <p>{{ props.plainText }}</p>

  <!-- Only for trusted/sanitized HTML -->
  <article v-html="safeHtml"></article>
</template>
```

## Choose `v-if` vs `v-show` by toggle behavior

**BAD:**
```vue
<template>
  <!-- Frequent toggles with v-if cause repeated mount/unmount -->
  <ComplexPanel v-if="isPanelOpen" />

  <!-- Rarely shown content with v-show pays initial render cost -->
  <AdminPanel v-show="isAdmin" />
</template>
```

**GOOD:**
```vue
<template>
  <!-- Frequent toggles: keep in DOM, toggle display -->
  <ComplexPanel v-show="isPanelOpen" />

  <!-- Rare condition: lazy render only when true -->
  <AdminPanel v-if="isAdmin" />
</template>
```
```

## File: `skills/vue-best-practices/references/state-management.md`
```markdown
---
title: State Management Strategy
impact: HIGH
impactDescription: Choosing the wrong store pattern can cause SSR request leaks, brittle mutation flows, and poor scaling
type: best-practice
tags: [vue3, state-management, pinia, composables, ssr, vueuse]
---

# State Management Strategy

**Impact: HIGH** - Use the lightest state solution that fits your app architecture. SPA-only apps can use lightweight global composables, while SSR/Nuxt apps should default to Pinia for request-safe isolation and predictable tooling.

## Task List

- Keep state local first, then promote to shared/global only when needed
- Use singleton composables only in non-SSR applications
- Expose global state as readonly and mutate through explicit actions
- Prefer Pinia for SSR/Nuxt, large apps, and advanced debugging/plugin needs
- Avoid exporting mutable module-level reactive state directly

## Choose the Lightest Store Approach

- **Feature composable:** Default for reusable logic with local/feature-level state.
- **Singleton composable or VueUse `createGlobalState`:** Small non-SSR apps needing shared app state.
- **Pinia:** SSR/Nuxt apps, medium-to-large apps, and cases requiring DevTools, plugins, or action tracing.

## Avoid Exporting Mutable Module State

**BAD:**
```ts
// store/cart.ts
import { reactive } from 'vue'

export const cart = reactive({
  items: [] as Array<{ id: string; qty: number }>
})
```

**GOOD:**
```ts
// composables/useCartStore.ts
import { reactive, readonly } from 'vue'

let _store: ReturnType<typeof createCartStore> | null = null

function createCartStore() {
  const state = reactive({
    items: [] as Array<{ id: string; qty: number }>
  })

  function addItem(id: string, qty = 1) {
    const existing = state.items.find((item) => item.id === id)
    if (existing) {
      existing.qty += qty
      return
    }
    state.items.push({ id, qty })
  }

  return {
    state: readonly(state),
    addItem
  }
}

export function useCartStore() {
  if (!_store) _store = createCartStore()
  return _store
}
```

## Do Not Use Runtime Singletons in SSR

Module singletons live for the runtime lifetime. In SSR this can leak state between requests.

**BAD:**
```ts
// shared singleton reused across requests
const cartStore = useCartStore()

export function useServerCart() {
  return cartStore
}
```

**GOOD:**

> `pinia` dependency required.

```ts
// stores/cart.ts
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [] as Array<{ id: string; qty: number }>
  }),
  actions: {
    addItem(id: string, qty = 1) {
      const existing = this.items.find((item) => item.id === id)
      if (existing) {
        existing.qty += qty
        return
      }
      this.items.push({ id, qty })
    }
  }
})
```

## Use `createGlobalState` for Small SPA Global State

> `@vueuse/core` dependency required.

If the app is non-SSR and already uses VueUse, `createGlobalState` removes singleton boilerplate.

```ts
import { createGlobalState } from '@vueuse/core'
import { computed, ref } from 'vue'

export const useAuthState = createGlobalState(() => {
  const token = ref<string | null>(null)
  const isAuthenticated = computed(() => token.value !== null)

  function setToken(next: string | null) {
    token.value = next
  }

  return {
    token,
    isAuthenticated,
    setToken
  }
})
```
```

## File: `skills/vue-best-practices/references/updated-hook-performance.md`
```markdown
---
title: Avoid Expensive Operations in Updated Hook
impact: MEDIUM
impactDescription: Heavy computations in updated hook cause performance bottlenecks and potential infinite loops
type: capability
tags: [vue3, vue2, lifecycle, updated, performance, optimization, reactivity]
---

# Avoid Expensive Operations in Updated Hook

**Impact: MEDIUM** - The `updated` hook runs after every reactive state change that causes a re-render. Placing expensive operations, API calls, or state mutations here can cause severe performance degradation, infinite loops, and dropped frames below the optimal 60fps threshold.

Use `updated`/`onUpdated` sparingly for post-DOM-update operations that cannot be handled by watchers or computed properties. For most reactive data handling, prefer watchers (`watch`/`watchEffect`) which provide more control over what triggers the callback.

## Task List

- Never perform API calls in updated hook
- Never mutate reactive state inside updated (causes infinite loops)
- Use conditional checks to verify updates are relevant before acting
- Prefer `watch` or `watchEffect` for reacting to specific data changes
- Use throttling/debouncing if updated operations are expensive
- Reserve updated for low-level DOM synchronization tasks

**BAD:**
```javascript
// BAD: API call in updated - fires on every re-render
export default {
  data() {
    return { items: [], lastUpdate: null }
  },
  updated() {
    // This runs after every single state change!
    fetch('/api/sync', {
      method: 'POST',
      body: JSON.stringify(this.items)
    })
  }
}
```

```javascript
// BAD: State mutation in updated - infinite loop
export default {
  data() {
    return { renderCount: 0 }
  },
  updated() {
    // This causes another update, which triggers updated again!
    this.renderCount++ // Infinite loop
  }
}
```

```javascript
// BAD: Heavy computation on every update
export default {
  updated() {
    // Expensive operation runs on every keystroke, every state change
    this.processedData = this.heavyComputation(this.rawData)
    this.analytics = this.calculateMetrics(this.allData)
  }
}
```

**GOOD:**
```javascript
import debounce from 'lodash-es/debounce'

// GOOD: Use watcher for specific data changes
export default {
  data() {
    return { items: [] }
  },
  watch: {
    // Only fires when items actually changes
    items: {
      handler(newItems) {
        this.syncToServer(newItems)
      },
      deep: true
    }
  },
  methods: {
    syncToServer: debounce(function(items) {
      fetch('/api/sync', {
        method: 'POST',
        body: JSON.stringify(items)
      })
    }, 500)
  }
}
```

```vue
<!-- GOOD: Composition API with targeted watchers -->
<script setup>
import { ref, watch, onUpdated } from 'vue'
import { useDebounceFn } from '@vueuse/core'

const items = ref([])
const scrollContainer = ref(null)

// Watch specific data - not all updates
watch(items, (newItems) => {
  syncToServer(newItems)
}, { deep: true })

const syncToServer = useDebounceFn((items) => {
  fetch('/api/sync', { method: 'POST', body: JSON.stringify(items) })
}, 500)

// Only use onUpdated for DOM synchronization
onUpdated(() => {
  // Scroll to bottom only if content changed height
  if (scrollContainer.value) {
    scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight
  }
})
</script>
```

```javascript
// GOOD: Conditional check in updated hook
export default {
  data() {
    return {
      content: '',
      lastSyncedContent: ''
    }
  },
  updated() {
    // Only act if specific condition is met
    if (this.content !== this.lastSyncedContent) {
      this.syncContent()
      this.lastSyncedContent = this.content
    }
  },
  methods: {
    syncContent: debounce(function() {
      // Sync logic
    }, 300)
  }
}
```

## Valid Use Cases for Updated Hook

```javascript
// GOOD: Low-level DOM synchronization
export default {
  updated() {
    // Sync third-party library with Vue's DOM
    this.thirdPartyWidget.refresh()

    // Update scroll position after content change
    this.$nextTick(() => {
      this.maintainScrollPosition()
    })
  }
}
```

## Prefer Computed Properties for Derived Data

```javascript
// BAD: Calculating derived data in updated
export default {
  data() {
    return { numbers: [1, 2, 3, 4, 5] }
  },
  updated() {
    this.sum = this.numbers.reduce((a, b) => a + b, 0) // Causes another update!
  }
}

// GOOD: Use computed property instead
export default {
  data() {
    return { numbers: [1, 2, 3, 4, 5] }
  },
  computed: {
    sum() {
      return this.numbers.reduce((a, b) => a + b, 0)
    }
  }
}
```
```

## File: `skills/vue-debug-guides/SKILL.md`
```markdown
---
name: vue-debug-guides
description: Vue 3 debugging and error handling for runtime errors, warnings, async failures, and SSR/hydration issues. Use when diagnosing or fixing Vue issues.
---

Vue 3 debugging and error handling for runtime issues, warnings, async failures, and hydration bugs.
For development best practices and common gotchas, use `vue-best-practices`.

### Reactivity
- Tracing unexpected re-renders and state updates → See [reactivity-debugging-hooks](reference/reactivity-debugging-hooks.md)
- Ref values not updating due to missing .value access → See [ref-value-access](reference/ref-value-access.md)
- State stops updating after destructuring reactive objects → See [reactive-destructuring](reference/reactive-destructuring.md)
- Refs inside arrays, Maps, or Sets not unwrapping → See [refs-in-collections-need-value](reference/refs-in-collections-need-value.md)
- Nested refs rendering as [object Object] in templates → See [template-ref-unwrapping-top-level](reference/template-ref-unwrapping-top-level.md)
- Reactive proxy identity comparisons always return false → See [reactivity-proxy-identity-hazard](reference/reactivity-proxy-identity-hazard.md)
- Third-party instances breaking when proxied → See [reactivity-markraw-for-non-reactive](reference/reactivity-markraw-for-non-reactive.md)
- Watchers only firing once per tick unexpectedly → See [reactivity-same-tick-batching](reference/reactivity-same-tick-batching.md)

### Computed
- Computed getter triggers mutations or requests unexpectedly → See [computed-no-side-effects](reference/computed-no-side-effects.md)
- Mutating computed values causes changes to disappear → See [computed-return-value-readonly](reference/computed-return-value-readonly.md)
- Computed value never updates after conditional logic → See [computed-conditional-dependencies](reference/computed-conditional-dependencies.md)
- Sorting or reversing arrays breaks original state → See [computed-array-mutation](reference/computed-array-mutation.md)
- Passing parameters to computed properties fails → See [computed-no-parameters](reference/computed-no-parameters.md)

### Watchers
- Async operations overwriting with stale data → See [watch-async-cleanup](reference/watch-async-cleanup.md)
- Creating watchers inside async callbacks → See [watch-async-creation-memory-leak](reference/watch-async-creation-memory-leak.md)
- Watcher never triggers for reactive object properties → See [watch-reactive-property-getter](reference/watch-reactive-property-getter.md)
- Async watchEffect misses dependencies after await → See [watcheffect-async-dependency-tracking](reference/watcheffect-async-dependency-tracking.md)
- DOM reads are stale inside watcher callbacks → See [watch-flush-timing](reference/watch-flush-timing.md)
- Deep watchers report identical old/new values → See [watch-deep-same-object-reference](reference/watch-deep-same-object-reference.md)
- watchEffect runs before template refs update → See [watcheffect-flush-post-for-refs](reference/watcheffect-flush-post-for-refs.md)

### Components
- Child component throws "component not found" error → See [local-components-not-in-descendants](reference/local-components-not-in-descendants.md)
- Click listener doesn't fire on custom component → See [click-events-on-components](reference/click-events-on-components.md)
- Parent can't access child ref data in script setup → See [component-ref-requires-defineexpose](reference/component-ref-requires-defineexpose.md)
- HTML template parsing breaks Vue component syntax → See [in-dom-template-parsing-caveats](reference/in-dom-template-parsing-caveats.md)
- Wrong component renders due to naming collisions → See [component-naming-conflicts](reference/component-naming-conflicts.md)
- Parent styles don't apply to multi-root component → See [multi-root-component-class-attrs](reference/multi-root-component-class-attrs.md)

### Props & Emits
- Variables referenced in defineProps cause errors → See [prop-defineprops-scope-limitation](reference/prop-defineprops-scope-limitation.md)
- Component emits undeclared event causing warnings → See [declare-emits-for-documentation](reference/declare-emits-for-documentation.md)
- defineEmits used inside function or conditional → See [defineEmits-must-be-top-level](reference/defineEmits-must-be-top-level.md)
- defineEmits has both type and runtime arguments → See [defineEmits-no-runtime-and-type-mixed](reference/defineEmits-no-runtime-and-type-mixed.md)
- Native event listeners not responding to clicks → See [native-event-collision-with-emits](reference/native-event-collision-with-emits.md)
- Component event fires twice when clicking → See [undeclared-emits-double-firing](reference/undeclared-emits-double-firing.md)

### Templates
- Getting template compilation errors with statements → See [template-expressions-restrictions](reference/template-expressions-restrictions.md)
- "Cannot read property of undefined" runtime errors → See [v-if-null-check-order](reference/v-if-null-check-order.md)
- Dynamic directive arguments not working properly → See [dynamic-argument-constraints](reference/dynamic-argument-constraints.md)
- v-else elements rendering unconditionally always → See [v-else-must-follow-v-if](reference/v-else-must-follow-v-if.md)
- Mixing v-if with v-for causes precedence bugs and migration breakage → See [no-v-if-with-v-for](reference/no-v-if-with-v-for.md)
- Template function calls mutating state cause unpredictable re-render bugs → See [template-functions-no-side-effects](reference/template-functions-no-side-effects.md)
- Child components in loops showing undefined data → See [v-for-component-props](reference/v-for-component-props.md)
- Array order changing after sorting or reversing → See [v-for-computed-reverse-sort](reference/v-for-computed-reverse-sort.md)
- List items disappearing or swapping state unexpectedly → See [v-for-key-attribute](reference/v-for-key-attribute.md)
- Getting off-by-one errors with range iteration → See [v-for-range-starts-at-one](reference/v-for-range-starts-at-one.md)
- v-show or v-else not working on template elements → See [v-show-template-limitation](reference/v-show-template-limitation.md)

### Template Refs
- Ref becomes null when element is conditionally hidden → See [template-ref-null-with-v-if](reference/template-ref-null-with-v-if.md)
- Ref array indices don't match data array in loops → See [template-ref-v-for-order](reference/template-ref-v-for-order.md)
- Refactoring template ref names breaks silently in code → See [use-template-ref-vue35](reference/use-template-ref-vue35.md)

### Forms & v-model
- Initial form values not showing when using v-model → See [v-model-ignores-html-attributes](reference/v-model-ignores-html-attributes.md)
- Textarea content changes not updating the ref → See [textarea-no-interpolation](reference/textarea-no-interpolation.md)
- iOS users cannot select dropdown first option → See [select-initial-value-ios-bug](reference/select-initial-value-ios-bug.md)
- Parent and child components have different values → See [define-model-default-value-sync](reference/define-model-default-value-sync.md)
- Object property changes not syncing to parent → See [definemodel-object-mutation-no-emit](reference/definemodel-object-mutation-no-emit.md)
- Real-time search/validation broken for Chinese/Japanese input → See [v-model-ime-composition](reference/v-model-ime-composition.md)
- Number input returns empty string instead of zero → See [v-model-number-modifier-behavior](reference/v-model-number-modifier-behavior.md)
- Custom checkbox values not submitted in forms → See [checkbox-true-false-value-form-submission](reference/checkbox-true-false-value-form-submission.md)

### Events & Modifiers
- Chaining multiple event modifiers produces unexpected results → See [event-modifier-order-matters](reference/event-modifier-order-matters.md)
- Keyboard shortcuts don't fire with system modifier keys → See [keyup-modifier-timing](reference/keyup-modifier-timing.md)
- Keyboard shortcuts fire with unintended modifier combinations → See [exact-modifier-for-precise-shortcuts](reference/exact-modifier-for-precise-shortcuts.md)
- Combining passive and prevent modifiers breaks event behavior → See [no-passive-with-prevent](reference/no-passive-with-prevent.md)

### Lifecycle
- Memory leaks from unremoved event listeners → See [cleanup-side-effects](reference/cleanup-side-effects.md)
- DOM access fails before component mounts → See [lifecycle-dom-access-timing](reference/lifecycle-dom-access-timing.md)
- DOM reads return stale values after state changes → See [dom-update-timing-nexttick](reference/dom-update-timing-nexttick.md)
- SSR rendering differs from client hydration → See [lifecycle-ssr-awareness](reference/lifecycle-ssr-awareness.md)
- Lifecycle hooks registered asynchronously never run → See [lifecycle-hooks-synchronous-registration](reference/lifecycle-hooks-synchronous-registration.md)

### Slots
- Accessing child component data in slot content returns undefined values → See [slot-render-scope-parent-only](reference/slot-render-scope-parent-only.md)
- Mixing named and scoped slots together causes compilation errors → See [slot-named-scoped-explicit-default](reference/slot-named-scoped-explicit-default.md)
- Using v-slot on native HTML elements causes compilation errors → See [slot-v-slot-on-components-or-templates-only](reference/slot-v-slot-on-components-or-templates-only.md)
- Unexpected content placement from implicit default slot behavior → See [slot-implicit-default-content](reference/slot-implicit-default-content.md)
- Scoped slot props missing expected name property → See [slot-name-reserved-prop](reference/slot-name-reserved-prop.md)
- Wrapper components breaking child slot functionality → See [slot-forwarding-to-child-components](reference/slot-forwarding-to-child-components.md)

### Provide/Inject
- Calling provide after async operations fails silently → See [provide-inject-synchronous-setup](reference/provide-inject-synchronous-setup.md)
- Tracing where provided values come from → See [provide-inject-debugging-challenges](reference/provide-inject-debugging-challenges.md)
- Injected values not updating when provider changes → See [provide-inject-reactivity-not-automatic](reference/provide-inject-reactivity-not-automatic.md)
- Multiple components share same default object → See [provide-inject-default-value-factory](reference/provide-inject-default-value-factory.md)

### Attrs
- Both internal and fallthrough event handlers execute → See [attrs-event-listener-merging](reference/attrs-event-listener-merging.md)
- Explicit attributes overwritten by fallthrough values → See [fallthrough-attrs-overwrite-vue3](reference/fallthrough-attrs-overwrite-vue3.md)
- Attributes applying to wrong element in wrappers → See [inheritattrs-false-for-wrapper-components](reference/inheritattrs-false-for-wrapper-components.md)

### Composables
- Composable called outside setup context or asynchronously → See [composable-call-location-restrictions](reference/composable-call-location-restrictions.md)
- Composable reactive dependency not updating when input changes → See [composable-tovalue-inside-watcheffect](reference/composable-tovalue-inside-watcheffect.md)
- Composable mutates external state unexpectedly → See [composable-avoid-hidden-side-effects](reference/composable-avoid-hidden-side-effects.md)
- Destructuring composable returns breaks reactivity unexpectedly → See [composable-naming-return-pattern](reference/composable-naming-return-pattern.md)

### Composition API
- Lifecycle hooks failing silently after async operations → See [composition-api-script-setup-async-context](reference/composition-api-script-setup-async-context.md)
- Parent component refs unable to access exposed properties → See [define-expose-before-await](reference/define-expose-before-await.md)
- Functional-programming patterns break expected Vue reactivity behavior → See [composition-api-not-functional-programming](reference/composition-api-not-functional-programming.md)
- React Hook mental model causes incorrect Composition API usage → See [composition-api-vs-react-hooks-differences](reference/composition-api-vs-react-hooks-differences.md)

### Animation
- Animations fail to trigger when DOM nodes are reused → See [animation-key-for-rerender](reference/animation-key-for-rerender.md)
- TransitionGroup list updates feel laggy under load → See [animation-transitiongroup-performance](reference/animation-transitiongroup-performance.md)

### TypeScript
- Mutable prop defaults leak state between component instances → See [ts-withdefaults-mutable-factory-function](reference/ts-withdefaults-mutable-factory-function.md)
- reactive() generic typing causes ref unwrapping mismatches → See [ts-reactive-no-generic-argument](reference/ts-reactive-no-generic-argument.md)
- Template refs throw null access errors before mount or after v-if unmount → See [ts-template-ref-null-handling](reference/ts-template-ref-null-handling.md)
- Optional boolean props behave as false instead of undefined → See [ts-defineprops-boolean-default-false](reference/ts-defineprops-boolean-default-false.md)
- Imported defineProps types fail with unresolvable or complex type references → See [ts-defineprops-imported-types-limitations](reference/ts-defineprops-imported-types-limitations.md)
- Untyped DOM event handlers fail under strict TypeScript settings → See [ts-event-handler-explicit-typing](reference/ts-event-handler-explicit-typing.md)
- Dynamic component refs trigger reactive component warnings → See [ts-shallowref-for-dynamic-components](reference/ts-shallowref-for-dynamic-components.md)
- Union-typed template expressions fail type checks without narrowing → See [ts-template-type-casting](reference/ts-template-type-casting.md)

### Async Components
- Route components misconfigured with defineAsyncComponent lazy loading → See [async-component-vue-router](reference/async-component-vue-router.md)
- Network failures or timeouts loading components → See [async-component-error-handling](reference/async-component-error-handling.md)
- Template refs undefined after component reactivation → See [async-component-keepalive-ref-issue](reference/async-component-keepalive-ref-issue.md)

### Render Functions
- Render function output stays static after state changes → See [rendering-render-function-return-from-setup](reference/rendering-render-function-return-from-setup.md)
- Reused vnode instances render incorrectly → See [render-function-vnodes-must-be-unique](reference/render-function-vnodes-must-be-unique.md)
- String component names render as HTML elements → See [rendering-resolve-component-for-string-names](reference/rendering-resolve-component-for-string-names.md)
- Accessing vnode internals breaks on Vue updates → See [render-function-avoid-internal-vnode-properties](reference/render-function-avoid-internal-vnode-properties.md)
- Vue 2 render function patterns crash in Vue 3 → See [rendering-render-function-h-import-vue3](reference/rendering-render-function-h-import-vue3.md)
- Slot content not rendering from h() → See [rendering-render-function-slots-as-functions](reference/rendering-render-function-slots-as-functions.md)

### KeepAlive
- Child components mount twice with nested Vue Router routes → See [keepalive-router-nested-double-mount](reference/keepalive-router-nested-double-mount.md)
- Memory grows when combining KeepAlive with Transition animations → See [keepalive-transition-memory-leak](reference/keepalive-transition-memory-leak.md)

### Transitions
- JavaScript transition hooks hang without done callback → See [transition-js-hooks-done-callback](reference/transition-js-hooks-done-callback.md)
- Move animations fail on inline list elements → See [transition-group-flip-inline-elements](reference/transition-group-flip-inline-elements.md)
- List items jump instead of smoothly animating → See [transition-group-move-animation-position-absolute](reference/transition-group-move-animation-position-absolute.md)
- Vue 2 to Vue 3 TransitionGroup wrapper changes break layout → See [transition-group-no-default-wrapper-vue3](reference/transition-group-no-default-wrapper-vue3.md)
- Nested transitions cut off before finishing → See [transition-nested-duration](reference/transition-nested-duration.md)
- Scoped styles stop working in reusable transition wrappers → See [transition-reusable-scoped-style](reference/transition-reusable-scoped-style.md)
- RouterView transitions animate unexpectedly on first render → See [transition-router-view-appear](reference/transition-router-view-appear.md)
- Mixing CSS transitions and animations causes timing issues → See [transition-type-when-mixed](reference/transition-type-when-mixed.md)
- Cleanup hooks missed during rapid transition swaps → See [transition-unmount-hook-timing](reference/transition-unmount-hook-timing.md)

### Teleport
- Teleport target element not found in DOM → See [teleport-target-must-exist](reference/teleport-target-must-exist.md)
- Teleported content breaks SSR hydration → See [teleport-ssr-hydration](reference/teleport-ssr-hydration.md)
- Scoped styles not applying to teleported content → See [teleport-scoped-styles-limitation](reference/teleport-scoped-styles-limitation.md)

### Suspense
- Need to handle async errors from Suspense components → See [suspense-no-builtin-error-handling](reference/suspense-no-builtin-error-handling.md)
- Using Suspense with server-side rendering → See [suspense-ssr-hydration-issues](reference/suspense-ssr-hydration-issues.md)
- Async component loading/error UI ignored under Suspense → See [async-component-suspense-control](reference/async-component-suspense-control.md)

### SSR
- HTML differs between server and client renders → See [ssr-hydration-mismatch-causes](reference/ssr-hydration-mismatch-causes.md)
- User state leaks between requests from shared singleton stores → See [state-ssr-cross-request-pollution](reference/state-ssr-cross-request-pollution.md)
- Browser-only APIs crash server rendering in universal code paths → See [ssr-platform-specific-apis](reference/ssr-platform-specific-apis.md)

### Performance
- List children re-render unnecessarily because parent passes unstable props → See [perf-props-stability-update-optimization](reference/perf-props-stability-update-optimization.md)
- Computed objects retrigger effects despite equivalent values → See [perf-computed-object-stability](reference/perf-computed-object-stability.md)

### SFC (Single File Components)
- Trying to use named exports from component script blocks → See [sfc-named-exports-forbidden](reference/sfc-named-exports-forbidden.md)
- Variables not updating in template after changes → See [sfc-script-setup-reactivity](reference/sfc-script-setup-reactivity.md)
- Scoped styles not applying to child component elements → See [sfc-scoped-css-child-component-styling](reference/sfc-scoped-css-child-component-styling.md)
- Scoped styles not applying to dynamic v-html content → See [sfc-scoped-css-dynamic-content](reference/sfc-scoped-css-dynamic-content.md)
- Scoped styles not applying to slot content → See [sfc-scoped-css-slot-content](reference/sfc-scoped-css-slot-content.md)
- Tailwind classes missing when built dynamically → See [tailwind-dynamic-class-generation](reference/tailwind-dynamic-class-generation.md)
- Recursive components not rendering due to name conflicts → See [self-referencing-component-name](reference/self-referencing-component-name.md)

### Plugins
- Debugging why global properties cause naming conflicts → See [plugin-global-properties-sparingly](reference/plugin-global-properties-sparingly.md)
- Plugin not working or inject returns undefined → See [plugin-install-before-mount](reference/plugin-install-before-mount.md)
- Plugin global properties are unavailable in setup-based components → See [plugin-prefer-provide-inject-over-global-properties](reference/plugin-prefer-provide-inject-over-global-properties.md)
- Plugin type augmentation mistakes break ComponentCustomProperties typing → See [plugin-typescript-type-augmentation](reference/plugin-typescript-type-augmentation.md)

### App Configuration
- App configuration methods not working after mount call → See [configure-app-before-mount](reference/configure-app-before-mount.md)
- Chaining app config off mount() fails because mount returns component instance → See [mount-return-value](reference/mount-return-value.md)
- require.context-based component auto-registration fails in Vite → See [dynamic-component-registration-vite](reference/dynamic-component-registration-vite.md)
```

## File: `skills/vue-debug-guides/reference/animation-key-for-rerender.md`
```markdown
---
title: Use Key Attribute to Force Re-render Animations
impact: MEDIUM
impactDescription: Without key attributes, Vue reuses DOM elements and animation libraries like AutoAnimate cannot detect changes to animate
type: gotcha
tags: [vue3, animation, key, autoanimate, rerender, dom]
---

# Use Key Attribute to Force Re-render Animations

**Impact: MEDIUM** - Vue optimizes performance by reusing DOM elements when possible. However, this optimization can prevent animation libraries (like AutoAnimate) from detecting changes, because the element is updated in place rather than re-created. Adding a `:key` attribute forces Vue to treat changed elements as new, triggering proper animations.

## Task Checklist

- [ ] Add `:key` to elements that should animate when their content changes
- [ ] Use unique, changing values for keys (not indices)
- [ ] For route transitions, add `:key="$route.fullPath"` to `<router-view>`
- [ ] Apply `v-auto-animate` to the parent element of keyed children

**Problematic Code:**
```vue
<template>
  <!-- BAD: Text changes but no animation occurs -->
  <div v-auto-animate>
    <p>{{ message }}</p>  <!-- No key - element is reused -->
  </div>

  <!-- BAD: Image source changes but no animation -->
  <div v-auto-animate>
    <img :src="imageUrl" />  <!-- No key - element is reused -->
  </div>

  <!-- BAD: Route changes don't animate -->
  <router-view v-auto-animate />  <!-- No key -->
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Hello')
const imageUrl = ref('/images/photo1.jpg')

// Changing these won't trigger animations because
// Vue updates the existing elements rather than replacing them
</script>
```

**Correct Code:**
```vue
<template>
  <!-- GOOD: Key forces re-render, triggering animation -->
  <div v-auto-animate>
    <p :key="message">{{ message }}</p>
  </div>

  <!-- GOOD: Image animates when source changes -->
  <div v-auto-animate>
    <img :key="imageUrl" :src="imageUrl" />
  </div>

  <!-- GOOD: Route changes animate properly -->
  <router-view :key="$route.fullPath" v-auto-animate />
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Hello')
const imageUrl = ref('/images/photo1.jpg')

// Now changing these will trigger animations
function updateMessage() {
  message.value = 'World'  // Triggers enter animation for new <p>
}
</script>
```

## Why This Works

When Vue sees a `:key` change:
1. It considers the old element and new element as different
2. The old element is removed (triggering leave animation)
3. A new element is created (triggering enter animation)

Without `:key`:
1. Vue sees the same element type in the same position
2. It updates the element's properties in place
3. No DOM addition/removal occurs, so no animation triggers

## Common Use Cases

### Animating Text Content Changes

```vue
<template>
  <div v-auto-animate>
    <h1 :key="title">{{ title }}</h1>
    <p :key="description">{{ description }}</p>
  </div>
</template>
```

### Animating Dynamic Components

```vue
<template>
  <div v-auto-animate>
    <component :is="currentComponent" :key="currentComponent" />
  </div>
</template>
```

### Animating Route Transitions

```vue
<template>
  <router-view v-slot="{ Component, route }">
    <div v-auto-animate>
      <component :is="Component" :key="route.fullPath" />
    </div>
  </router-view>
</template>
```

## With Vue's Built-in Transition

The same principle applies to Vue's `<Transition>` component:

```vue
<template>
  <!-- GOOD: Key triggers transition on content change -->
  <Transition name="fade" mode="out-in">
    <p :key="message">{{ message }}</p>
  </Transition>

  <!-- GOOD: Different keys for conditional content -->
  <Transition name="fade" mode="out-in">
    <div v-if="isLoading" key="loading">Loading...</div>
    <div v-else key="content">{{ content }}</div>
  </Transition>
</template>
```

## Caution: Performance Implications

Using `:key` forces full component re-creation. For frequently changing data:
- The entire component tree under the keyed element is destroyed and recreated
- Any component state is lost
- Consider whether the animation is worth the performance cost

```vue
<!-- Be cautious with complex components -->
<ComplexDashboard :key="refreshTrigger" />
<!-- This destroys and recreates the entire dashboard! -->
```

## Reference
- [Vue.js Animation Techniques](https://vuejs.org/guide/extras/animation.html)
- [AutoAnimate with Vue](https://auto-animate.formkit.com/#usage-vue)
- [Vue.js v-for with key](https://vuejs.org/guide/essentials/list.html#maintaining-state-with-key)
```

## File: `skills/vue-debug-guides/reference/animation-transitiongroup-performance.md`
```markdown
---
title: TransitionGroup Performance with Large Lists and CSS Frameworks
impact: MEDIUM
impactDescription: TransitionGroup can cause noticeable DOM update lag when animating list changes, especially with CSS frameworks
type: gotcha
tags: [vue3, transition-group, animation, performance, list, css-framework]
---

# TransitionGroup Performance with Large Lists and CSS Frameworks

**Impact: MEDIUM** - Vue's `<TransitionGroup>` can experience significant DOM update lag when animating list changes, particularly when:
- Using CSS frameworks (Tailwind, Bootstrap, etc.)
- Performing array operations like `slice()` that change multiple items
- Working with larger lists

Without TransitionGroup, DOM updates occur instantly. With it, there can be noticeable delay before the UI reflects changes.

## Task Checklist

- [ ] For frequently updated lists, consider if transition animations are necessary
- [ ] Use CSS `content-visibility: auto` for long lists to reduce render cost
- [ ] Minimize CSS framework classes on list items during transitions
- [ ] Consider virtual scrolling for very large animated lists
- [ ] Profile with Vue DevTools to identify transition bottlenecks

**Problematic Pattern:**
```vue
<template>
  <!-- Potentially slow with large lists or complex CSS -->
  <TransitionGroup name="list" tag="ul">
    <li
      v-for="item in items"
      :key="item.id"
      class="p-4 m-2 rounded-lg shadow-md bg-gradient-to-r from-blue-500 to-purple-600
             hover:shadow-lg transition-all duration-300 ease-in-out transform hover:scale-105
             border border-gray-200 flex items-center justify-between"
    >
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([/* many items */])

// Operations like slice can cause visible lag
function removeItems() {
  items.value = items.value.slice(5)  // May lag with TransitionGroup
}
</script>

<style>
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
</style>
```

**Optimized Approach:**
```vue
<template>
  <!-- Simpler classes, shorter transitions -->
  <TransitionGroup name="list" tag="ul" class="relative">
    <li
      v-for="item in items"
      :key="item.id"
      class="list-item"
    >
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>

<script setup>
import { ref, computed } from 'vue'

const items = ref([/* items */])

// For large batch operations, consider disabling animations temporarily
const isAnimating = ref(true)
</script>

<style>
/* Keep transition CSS simple and specific */
.list-item {
  /* Minimal styles during animation */
  padding: 1rem;
}

.list-move {
  transition: transform 0.3s ease;  /* Shorter duration */
}

.list-enter-active,
.list-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

/* Use will-change sparingly */
.list-enter-active {
  will-change: opacity, transform;
}

/* Absolute positioning for leaving elements prevents layout thrashing */
.list-leave-active {
  position: absolute;
  width: 100%;
}
</style>
```

## Performance Optimization Strategies

### 1. Skip Animations for Bulk Operations

```vue
<template>
  <TransitionGroup v-if="animationsEnabled" name="list" tag="ul">
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </TransitionGroup>

  <!-- Instant update without animations -->
  <ul v-else>
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </ul>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const animationsEnabled = ref(true)

async function bulkUpdate(newItems) {
  // Disable animations for bulk operations
  animationsEnabled.value = false
  items.value = newItems
  await nextTick()
  animationsEnabled.value = true
}
</script>
```

### 2. Virtual Scrolling for Large Lists

```vue
<template>
  <!-- Use a virtual list library for large datasets -->
  <RecycleScroller
    :items="items"
    :item-size="50"
    key-field="id"
    v-slot="{ item }"
  >
    <div class="list-item">{{ item.name }}</div>
  </RecycleScroller>
</template>

<script setup>
import { RecycleScroller } from 'vue-virtual-scroller'
</script>
```

### 3. Reduce CSS Complexity During Transitions

```vue
<style>
/* Move complex styles to a stable wrapper */
.list-item-wrapper {
  @apply p-4 m-2 rounded-lg shadow-md bg-gradient-to-r from-blue-500 to-purple-600;
}

/* Keep animated element styles minimal */
.list-item {
  /* Only essential layout styles */
}

.list-move,
.list-enter-active,
.list-leave-active {
  /* Only animate transform/opacity - GPU accelerated */
  transition: transform 0.3s ease, opacity 0.3s ease;
}
</style>
```

### 4. Use CSS content-visibility

```css
/* For very long lists, defer rendering of off-screen items */
.list-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 50px; /* Estimated height */
}
```

## When to Avoid TransitionGroup

Consider alternatives when:
- List updates are frequent (real-time data)
- List contains 100+ items
- Items have complex CSS or nested components
- Performance is critical (mobile, low-end devices)

```vue
<!-- Simple alternative: CSS-only animations on individual items -->
<ul>
  <li
    v-for="item in items"
    :key="item.id"
    class="animate-in"
  >
    {{ item.name }}
  </li>
</ul>

<style>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-in {
  animation: fadeIn 0.3s ease forwards;
}
</style>
```

## Reference
- [Vue.js TransitionGroup](https://vuejs.org/guide/built-ins/transition-group.html)
- [GitHub Issue: transition-group DOM update lag](https://github.com/vuejs/vue/issues/5845)
- [Vue Virtual Scroller](https://github.com/Akryum/vue-virtual-scroller)
```

## File: `skills/vue-debug-guides/reference/async-component-error-handling.md`
```markdown
# Async Component Error Handling

## Rule

Always configure error handling for async components using `errorComponent` and/or `onError` callback. Without proper error handling, failed component loads can leave the UI in an undefined state with no user feedback.

## Why This Matters

Network failures, timeouts, and server errors are common in production. Without error handling, users see blank spaces or broken UIs with no indication of what went wrong or how to recover.

## Bad Code

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

// No error handling - fails silently
const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue')
)
</script>
```

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

// isLoading never becomes false on error - infinite spinner
const isLoading = ref(true)
const Widget = defineAsyncComponent({
  loader: () => import('./Widget.vue').finally(() => {
    isLoading.value = false  // Only runs on success
  })
})
</script>
```

## Good Code

```vue
<script setup>
import { defineAsyncComponent } from 'vue'
import LoadingSpinner from './LoadingSpinner.vue'
import ErrorDisplay from './ErrorDisplay.vue'

const AsyncWidget = defineAsyncComponent({
  loader: () => import('./Widget.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  delay: 200,    // Prevent loading flicker
  timeout: 10000 // Show error after 10 seconds
})
</script>
```

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

// With retry logic using onError
const AsyncWidget = defineAsyncComponent({
  loader: () => import('./Widget.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  onError(error, retry, fail, attempts) {
    if (attempts <= 3) {
      // Retry up to 3 times
      retry()
    } else {
      // Give up and show error component
      fail()
    }
  }
})
</script>
```

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

// Fallback component pattern - catch in loader
const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue').catch(() => import('./WidgetFallback.vue'))
)
</script>
```

## onError Callback Parameters

The `onError` callback receives four arguments:

| Parameter | Type | Description |
|-----------|------|-------------|
| `error` | `Error` | The error that caused the load to fail |
| `retry` | `Function` | Call to retry loading the component |
| `fail` | `Function` | Call to give up and show errorComponent |
| `attempts` | `number` | Number of load attempts so far |

## Key Points

1. Always provide an `errorComponent` for production applications
2. Use `timeout` to prevent indefinite loading states
3. Consider retry logic with `onError` for transient network issues
4. The `delay` option (default 200ms) prevents loading flicker on fast networks
5. Use the fallback pattern (`.catch()` in loader) when you want a seamless degradation

## SSR Warning

Using `onError` with SSR can cause issues in some configurations, potentially leading to infinite loading. Test thoroughly in SSR environments.

## References

- [Vue.js Async Components Documentation](https://vuejs.org/guide/components/async)
- [Handling Async Components' loading errors](https://awad.dev/blog/handling-async-component-loading-errors/)
```

## File: `skills/vue-debug-guides/reference/async-component-keepalive-ref-issue.md`
```markdown
# Async Components with keep-alive Ref Issues

## Rule

When using `<keep-alive>`, `<component>`, and `defineAsyncComponent` together, be aware that template refs can become undefined when the component is re-activated after being deactivated.

## Why This Matters

This is a known Vue issue where the ref binding works correctly on first activation but becomes undefined on subsequent activations. This can cause runtime errors when trying to access component methods or properties through refs.

## Problem Scenario

```vue
<script setup>
import { ref, defineAsyncComponent } from 'vue'

const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue')
)

const currentComponent = ref(AsyncWidget)
const widgetRef = ref(null)

function callWidgetMethod() {
  // May be undefined after component reactivation!
  widgetRef.value?.doSomething()
}
</script>

<template>
  <keep-alive>
    <component :is="currentComponent" ref="widgetRef" />
  </keep-alive>
</template>
```

## Workarounds

### Option 1: Use onActivated to re-establish ref access

```vue
<script setup>
import { ref, defineAsyncComponent, onActivated, nextTick } from 'vue'

const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue')
)

const currentComponent = ref(AsyncWidget)
const widgetRef = ref(null)

// Use a computed or method that waits for ref to be available
async function callWidgetMethod() {
  await nextTick()
  if (widgetRef.value) {
    widgetRef.value.doSomething()
  }
}
</script>
```

### Option 2: Avoid mixing all three patterns

If possible, use one of these alternatives:

```vue
<!-- Option A: Don't use keep-alive with async components -->
<template>
  <component :is="currentComponent" ref="widgetRef" />
</template>

<!-- Option B: Use static component with keep-alive -->
<script setup>
import Widget from './Widget.vue'  // Regular import
</script>
<template>
  <keep-alive>
    <component :is="Widget" ref="widgetRef" />
  </keep-alive>
</template>
```

### Option 3: Use provide/inject instead of refs

```vue
<!-- Parent.vue -->
<script setup>
import { provide, ref } from 'vue'

const sharedState = ref({ /* shared data */ })
provide('widgetState', sharedState)
</script>

<!-- Widget.vue (async component) -->
<script setup>
import { inject } from 'vue'
const widgetState = inject('widgetState')
</script>
```

## Key Points

1. This is a known issue when combining `<keep-alive>`, `<component :is>`, and `defineAsyncComponent`
2. Refs may become undefined after component deactivation/reactivation
3. Use `nextTick` and null checks when accessing refs
4. Consider alternative patterns like provide/inject for cross-component communication
5. Test thoroughly when using this combination

## References

- [Vue.js GitHub Discussion #11334](https://github.com/orgs/vuejs/discussions/11334)
- [Vue.js Async Components Documentation](https://vuejs.org/guide/components/async)
```

## File: `skills/vue-debug-guides/reference/async-component-suspense-control.md`
```markdown
---
title: Suspense Overrides Async Component Loading and Error Options
impact: MEDIUM
impactDescription: Async component loading/error options are ignored under a parent Suspense, leading to missing spinners and error UIs
type: gotcha
tags: [vue3, suspense, async-components, loading, error-handling]
---

# Suspense Overrides Async Component Loading and Error Options

**Impact: MEDIUM** - When an async component renders inside a parent `<Suspense>`, its `loadingComponent`, `errorComponent`, `delay`, and `timeout` options do not run. The parent Suspense controls loading and error UX instead.

## Task Checklist

- [ ] Confirm whether the async component is inside a `<Suspense>` boundary
- [ ] Use `suspensible: false` when the component must manage its own loading/error UI
- [ ] Or move loading/error UI to the parent `<Suspense>` fallback and an error boundary (`onErrorCaptured`)
- [ ] Provide a retry path for failed loads

**Incorrect:**
```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const AsyncDashboard = defineAsyncComponent({
  loader: () => import('./Dashboard.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  timeout: 3000
})
</script>

<template>
  <Suspense>
    <AsyncDashboard />
    <template #fallback>Loading...</template>
  </Suspense>
</template>
```

**Correct (component handles its own states):**
```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const AsyncDashboard = defineAsyncComponent({
  loader: () => import('./Dashboard.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  timeout: 3000,
  suspensible: false
})
</script>

<template>
  <AsyncDashboard />
</template>
```

**Correct (parent Suspense owns loading/error UI):**
```vue
<script setup>
import { onErrorCaptured, ref } from 'vue'
import AsyncDashboard from './AsyncDashboard.vue'

const error = ref(null)

onErrorCaptured((err) => {
  error.value = err
  return false
})
</script>

<template>
  <ErrorDisplay v-if="error" :error="error" />

  <Suspense v-else>
    <AsyncDashboard />
    <template #fallback>
      <LoadingSpinner />
    </template>
  </Suspense>
</template>
```
```

## File: `skills/vue-debug-guides/reference/async-component-vue-router.md`
```markdown
# Do Not Use defineAsyncComponent with Vue Router

## Rule

Never use `defineAsyncComponent` when configuring Vue Router route components. Vue Router has its own lazy loading mechanism using dynamic imports directly.

## Why This Matters

Vue Router's lazy loading is specifically designed for route-level code splitting. Using `defineAsyncComponent` for routes adds unnecessary overhead and can cause unexpected behavior with navigation guards, loading states, and route transitions.

## Bad Code

```javascript
import { defineAsyncComponent } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/dashboard',
      // WRONG: Don't use defineAsyncComponent here
      component: defineAsyncComponent(() =>
        import('./views/Dashboard.vue')
      )
    },
    {
      path: '/profile',
      // WRONG: This also won't work as expected
      component: defineAsyncComponent({
        loader: () => import('./views/Profile.vue'),
        loadingComponent: LoadingSpinner
      })
    }
  ]
})
```

## Good Code

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/dashboard',
      // CORRECT: Use dynamic import directly
      component: () => import('./views/Dashboard.vue')
    },
    {
      path: '/profile',
      // CORRECT: Simple arrow function with import
      component: () => import('./views/Profile.vue')
    }
  ]
})
```

## Handling Loading States with Vue Router

For route-level loading states, use Vue Router's navigation guards or a global loading indicator:

```vue
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isLoading = ref(false)

router.beforeEach(() => {
  isLoading.value = true
})

router.afterEach(() => {
  isLoading.value = false
})
</script>

<template>
  <LoadingBar v-if="isLoading" />
  <RouterView />
</template>
```

## When to Use defineAsyncComponent

Use `defineAsyncComponent` for:
- Components loaded conditionally within a page
- Heavy components that aren't always needed
- Modal dialogs or panels that load on demand

Use Vue Router's lazy loading for:
- Route-level components (views/pages)
- Any component configured in route definitions

## Key Points

1. Vue Router and `defineAsyncComponent` are separate lazy loading mechanisms
2. Route components should use direct dynamic imports: `() => import('./View.vue')`
3. Use navigation guards for route-level loading indicators
4. `defineAsyncComponent` is for component-level lazy loading within pages

## References

- [Vue Router Lazy Loading Routes](https://router.vuejs.org/guide/advanced/lazy-loading.html)
- [Vue.js Async Components Documentation](https://vuejs.org/guide/components/async)
```

## File: `skills/vue-debug-guides/reference/attrs-event-listener-merging.md`
```markdown
# Fallthrough Event Listeners Are Additive

## Rule

When an event listener is passed to a component as a fallthrough attribute, it is added to the root element's existing listeners of the same type - both will trigger. This is different from props where values are replaced. Be aware that both the component's internal handler and the parent's handler will execute.

## Why This Matters

- Developers may expect event listeners to override like props
- Both handlers execute, which can cause double submissions, duplicate API calls
- Order of execution: internal handler first, then fallthrough handler
- This is actually useful for composition but can cause bugs if unexpected

## Bad Code

```vue
<!-- BaseButton.vue - Potential double-action bug -->
<template>
  <button @click="internalClick">
    <slot />
  </button>
</template>

<script setup>
const emit = defineEmits(['action'])

function internalClick() {
  // This runs first
  emit('action')
  console.log('Internal click handler')
}
</script>

<!-- Parent.vue -->
<template>
  <BaseButton @click="parentClick">Submit</BaseButton>
</template>

<script setup>
function parentClick() {
  // This ALSO runs (after internal)
  submitForm()  // Might cause double submission!
  console.log('Parent click handler')
}
</script>

<!--
  RESULT: Both handlers fire!
  Console output:
  1. "Internal click handler"
  2. "Parent click handler"

  If both trigger API calls, you get duplicate requests
-->
```

## Good Code

### Option 1: Prevent fallthrough with inheritAttrs: false

```vue
<!-- BaseButton.vue - Control event handling explicitly -->
<script setup>
defineOptions({
  inheritAttrs: false
})

const emit = defineEmits(['click'])

function handleClick(event) {
  // Component controls all click behavior
  console.log('Handled internally')
  emit('click', event)  // Explicitly forward if needed
}
</script>

<template>
  <button @click="handleClick">
    <slot />
  </button>
</template>
```

### Option 2: Document the additive behavior

```vue
<!-- BaseButton.vue - Design for composition -->
<script setup>
/**
 * BaseButton - A composable button component
 *
 * Note: Click handlers passed to this component are ADDITIVE.
 * The internal handler runs first, then any parent @click handler.
 * Use @action event if you only want to respond to the action.
 */
const emit = defineEmits(['action'])

function internalClick() {
  // Internal logic (e.g., ripple effect, analytics)
  emit('action')
}
</script>

<template>
  <button @click="internalClick">
    <slot />
  </button>
</template>

<!-- Parent.vue - Use the custom event instead -->
<template>
  <!-- Use @action, not @click, to avoid double handling -->
  <BaseButton @action="handleAction">Submit</BaseButton>
</template>
```

### Option 3: Use stopPropagation if needed

```vue
<!-- BaseButton.vue - Stop event propagation when needed -->
<script setup>
const props = defineProps({
  stopPropagation: Boolean
})

function handleClick(event) {
  if (props.stopPropagation) {
    event.stopPropagation()
  }
  // Internal handling...
}
</script>

<template>
  <button @click="handleClick">
    <slot />
  </button>
</template>
```

## Using Additive Behavior Intentionally

The additive behavior can be useful for extending functionality:

```vue
<!-- EnhancedButton.vue - Leveraging additive listeners -->
<template>
  <button
    @click="trackClick"
    @focus="trackFocus"
  >
    <slot />
  </button>
</template>

<script setup>
function trackClick() {
  analytics.track('button_click')
  // Parent's @click will also run - that's intentional!
}

function trackFocus() {
  analytics.track('button_focus')
}
</script>

<!-- Parent.vue -->
<template>
  <!-- Both analytics AND form submission happen -->
  <EnhancedButton @click="submitForm">Submit</EnhancedButton>
</template>
```

## Execution Order

```vue
<script setup>
// Component
function componentHandler() {
  console.log('1. Component handler (first)')
}
</script>

<template>
  <button @click="componentHandler">Click</button>
</template>

<!-- Parent passes @click -->
<!-- Execution order:
     1. componentHandler (defined in component)
     2. parentHandler (passed as fallthrough)
-->
```

## Best Practices

1. **For UI components**: Use `inheritAttrs: false` and emit custom events
2. **For HOCs/wrappers**: Document that listeners are additive
3. **For analytics/tracking**: Leverage additive behavior intentionally
4. **Avoid side effects**: Don't assume your handler is the only one running

## References

- [Fallthrough Attributes - v-on Listener Inheritance](https://vuejs.org/guide/components/attrs.html#v-on-listener-inheritance)
- [Component Events](https://vuejs.org/guide/components/events.html)
```

## File: `skills/vue-debug-guides/reference/checkbox-true-false-value-form-submission.md`
```markdown
---
title: Checkbox true-value/false-value Not Submitted in Forms
impact: MEDIUM
impactDescription: true-value and false-value attributes don't affect form submission - unchecked boxes send nothing
type: capability
tags: [vue3, v-model, forms, checkbox, form-submission]
---

# Checkbox true-value/false-value Not Submitted in Forms

**Impact: MEDIUM** - Vue's `true-value` and `false-value` attributes only affect the JavaScript binding, NOT the actual form submission. Unchecked checkboxes are never included in form submissions by browsers, regardless of `false-value`.

This is a browser limitation, not a Vue issue. If you need to submit one of two values (like "yes"/"no" or "active"/"inactive"), use radio buttons instead of a checkbox.

## Task Checklist

- [ ] Don't rely on `false-value` for form submissions - it won't be sent
- [ ] Use radio buttons when you need to submit one of exactly two values
- [ ] Remember `true-value`/`false-value` are for JavaScript state only
- [ ] For form submissions with custom values, handle the transformation server-side or in submit handler

**Problem - false-value not submitted:**
```html
<script setup>
import { ref } from 'vue'

const status = ref('no')  // JavaScript value works correctly
</script>

<template>
  <form action="/api/update" method="POST">
    <!-- PROBLEM: When unchecked, nothing is submitted for this field -->
    <!-- Server receives no "status" field at all, not "no" -->
    <input
      type="checkbox"
      v-model="status"
      true-value="yes"
      false-value="no"
      name="status"
    >
    <label>Active</label>

    <!-- status.value correctly shows "yes" or "no" in Vue -->
    <!-- But form submission only sends "status=yes" when checked -->
    <!-- When unchecked, "status" field is completely missing -->
  </form>
</template>
```

**Solution 1 - Use radio buttons for two-value submission:**
```html
<script setup>
import { ref } from 'vue'

const status = ref('no')
</script>

<template>
  <form action="/api/update" method="POST">
    <!-- CORRECT: Radio buttons always submit a value -->
    <label>
      <input type="radio" v-model="status" value="yes" name="status">
      Active
    </label>
    <label>
      <input type="radio" v-model="status" value="no" name="status">
      Inactive
    </label>

    <!-- Form always submits "status=yes" or "status=no" -->
  </form>
</template>
```

**Solution 2 - Handle in submit handler (for SPA/AJAX):**
```html
<script setup>
import { ref } from 'vue'

const isActive = ref(false)

async function submitForm() {
  // Transform checkbox state to desired value before sending
  const payload = {
    status: isActive.value ? 'yes' : 'no'
  }

  await fetch('/api/update', {
    method: 'POST',
    body: JSON.stringify(payload)
  })
}
</script>

<template>
  <!-- For AJAX submission, checkbox is fine - transform in handler -->
  <input type="checkbox" v-model="isActive">
  <label>Active</label>

  <button @click="submitForm">Save</button>
</template>
```

**Solution 3 - Hidden input fallback:**
```html
<template>
  <form action="/api/update" method="POST">
    <!-- Hidden input provides fallback value -->
    <input type="hidden" name="status" value="no">
    <!-- Checkbox overrides with "yes" when checked -->
    <input type="checkbox" name="status" value="yes" v-model="isActive">
    <label>Active</label>
  </form>
</template>
```

## Reference
- [Vue.js Form Input Bindings - Checkbox](https://vuejs.org/guide/essentials/forms.html#checkbox)
```

## File: `skills/vue-debug-guides/reference/cleanup-side-effects.md`
```markdown
---
title: Clean Up Event Listeners and Intervals in onUnmounted
impact: HIGH
impactDescription: Failing to clean up side effects causes memory leaks and ghost event handlers
type: capability
tags: [vue3, lifecycle, memory-leak, event-listeners, intervals, cleanup]
---

# Clean Up Event Listeners and Intervals in onUnmounted

**Impact: HIGH** - Failing to clean up event listeners, intervals, timeouts, and subscriptions when a component unmounts causes memory leaks and ghost handlers that continue running, leading to performance degradation and subtle bugs in Single Page Applications.

When using custom events, timers, WebSocket connections, or third-party libraries, always clean up in `onUnmounted` (Composition API) or `unmounted` (Options API).

## Task Checklist

- [ ] Track all addEventListener calls and remove them in onUnmounted
- [ ] Clear all setInterval and setTimeout calls in onUnmounted
- [ ] Unsubscribe from external event emitters and observables
- [ ] Disconnect WebSocket connections and third-party library instances
- [ ] Use `onBeforeUnmount` if cleanup must happen before DOM removal

**Incorrect:**
```javascript
// Composition API - WRONG: No cleanup
import { onMounted } from 'vue'

export default {
  setup() {
    onMounted(() => {
      // These keep running after component unmounts!
      window.addEventListener('resize', handleResize)
      setInterval(pollServer, 5000)
      socket.on('message', handleMessage)
    })
  }
}
```

```javascript
// Options API - WRONG: No cleanup
export default {
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
    this.timer = setInterval(this.refresh, 10000)
  }
  // Component unmounts, but listeners and timers persist!
}
```

**Correct:**
```javascript
// Composition API - CORRECT: Proper cleanup
import { onMounted, onUnmounted, ref } from 'vue'

export default {
  setup() {
    const intervalId = ref(null)

    const handleResize = () => {
      // handle resize
    }

    const handleMessage = (msg) => {
      // handle message
    }

    onMounted(() => {
      window.addEventListener('resize', handleResize)
      intervalId.value = setInterval(pollServer, 5000)
      socket.on('message', handleMessage)
    })

    onUnmounted(() => {
      // Clean up everything!
      window.removeEventListener('resize', handleResize)

      if (intervalId.value) {
        clearInterval(intervalId.value)
      }

      socket.off('message', handleMessage)
    })
  }
}
```

```javascript
// Options API - CORRECT: Proper cleanup
export default {
  data() {
    return {
      timer: null
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
    this.timer = setInterval(this.refresh, 10000)
  },
  unmounted() {
    window.removeEventListener('scroll', this.handleScroll)
    if (this.timer) {
      clearInterval(this.timer)
    }
  },
  methods: {
    handleScroll() { /* ... */ },
    refresh() { /* ... */ }
  }
}
```

## Using Composable Pattern for Auto-Cleanup

```javascript
// Reusable composable with automatic cleanup
import { onMounted, onUnmounted } from 'vue'

export function useEventListener(target, event, handler) {
  onMounted(() => {
    target.addEventListener(event, handler)
  })

  onUnmounted(() => {
    target.removeEventListener(event, handler)
  })
}

export function useInterval(callback, delay) {
  let intervalId = null

  onMounted(() => {
    intervalId = setInterval(callback, delay)
  })

  onUnmounted(() => {
    if (intervalId) clearInterval(intervalId)
  })
}

// Usage - cleanup is automatic
import { useEventListener, useInterval } from './composables'

export default {
  setup() {
    useEventListener(window, 'resize', handleResize)
    useInterval(pollServer, 5000)
    // No manual cleanup needed!
  }
}
```

## VueUse Alternative

```javascript
// VueUse provides cleanup-aware composables
import { useEventListener, useIntervalFn } from '@vueuse/core'

export default {
  setup() {
    // Automatically cleaned up on unmount
    useEventListener(window, 'resize', handleResize)

    const { pause, resume } = useIntervalFn(pollServer, 5000)
    // Also provides pause/resume controls
  }
}
```

## Reference
- [Vue.js Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)
- [VueUse - useEventListener](https://vueuse.org/core/useEventListener/)
```

## File: `skills/vue-debug-guides/reference/click-events-on-components.md`
```markdown
---
title: Click Events on Custom Components Require Emit or Fallthrough
impact: HIGH
impactDescription: Native click events on custom components won't work without proper emit declaration or attribute fallthrough
type: gotcha
tags: [vue3, events, components, emit, click, migration]
---

# Click Events on Custom Components Require Emit or Fallthrough

**Impact: HIGH** - Unlike native HTML elements, custom Vue components don't automatically forward native DOM events like `click`. You must either emit the event explicitly, rely on attribute fallthrough to a single root element, or use the `.native` modifier (Vue 2 only, removed in Vue 3). This is a common source of confusion and migration issues.

## Task Checklist

- [ ] Declare emitted events using `defineEmits` in child components
- [ ] Emit click events from child component when needed
- [ ] Understand that single-root components automatically forward attrs to root
- [ ] Remove `.native` modifier when migrating from Vue 2 to Vue 3
- [ ] For multi-root components, explicitly bind `$attrs` or emit events

**Incorrect:**
```html
<!-- WRONG: Expecting native click to work on custom component -->
<template>
  <MyButton @click="handleClick">Click me</MyButton>
  <!-- This may not work as expected! -->
</template>
```

```html
<!-- WRONG: Vue 2 .native modifier doesn't exist in Vue 3 -->
<template>
  <MyButton @click.native="handleClick">Click me</MyButton>
  <!-- Error in Vue 3: .native modifier removed -->
</template>
```

```html
<!-- WRONG: Multi-root component with no attr binding -->
<!-- MyButton.vue -->
<template>
  <span>Icon</span>
  <button>{{ label }}</button>
  <!-- No root element to receive click! -->
</template>
```

**Correct:**
```html
<!-- CORRECT: Child component emits the click event -->
<!-- MyButton.vue -->
<template>
  <button @click="$emit('click', $event)">
    <slot></slot>
  </button>
</template>

<script setup>
defineEmits(['click'])
</script>

<!-- Parent.vue -->
<template>
  <MyButton @click="handleClick">Click me</MyButton>
</template>
```

```html
<!-- CORRECT: Single root element with automatic fallthrough -->
<!-- MyButton.vue -->
<template>
  <button>
    <slot></slot>
  </button>
  <!-- @click from parent automatically falls through to button -->
</template>

<!-- Parent.vue -->
<template>
  <MyButton @click="handleClick">Click me</MyButton>
</template>
```

```html
<!-- CORRECT: Multi-root component with explicit $attrs binding -->
<!-- MyButton.vue -->
<template>
  <span>Icon</span>
  <button v-bind="$attrs">
    <slot></slot>
  </button>
</template>

<script setup>
defineOptions({
  inheritAttrs: false
})
</script>
```

## Component Events Don't Bubble

```javascript
// Important: Component-emitted events do NOT bubble
// You can only listen to events from direct children

// WRONG: Trying to catch grandchild events
<GrandParent @child-event="handle">  <!-- Won't receive! -->
  <Parent>
    <Child @click="$emit('child-event')" />
  </Parent>
</GrandParent>

// CORRECT: Each level must relay the event
<GrandParent @child-event="handle">
  <Parent @child-event="$emit('child-event', $event)">
    <Child @click="$emit('child-event')" />
  </Parent>
</GrandParent>
```

## Vue 3 Native Event Behavior

```javascript
// In Vue 3, if you declare an event in emits:
defineEmits(['click'])

// Then @click on the component ONLY listens to emitted events
// NOT native click events

// If you don't declare 'click' in emits:
defineEmits(['custom-event'])

// Then @click on single-root component will:
// 1. Fall through to root element as native listener
// 2. Fire on native click
```

## Composition API Emit Pattern

```vue
<script setup>
// Define what events this component emits
const emit = defineEmits(['click', 'update', 'delete'])

function handleClick(event) {
  // Do component logic
  processClick()

  // Then emit to parent
  emit('click', event)
}
</script>

<template>
  <button @click="handleClick">
    <slot></slot>
  </button>
</template>
```

## Migration from Vue 2

```html
<!-- Vue 2: Used .native for native events on components -->
<MyComponent @click.native="handleClick" />

<!-- Vue 3: Remove .native, ensure component handles the event -->
<MyComponent @click="handleClick" />

<!-- Make sure MyComponent either:
     1. Has single root that receives fallthrough attrs
     2. Explicitly emits 'click' event
     3. Uses v-bind="$attrs" on intended element -->
```

## Reference
- [Vue.js Component Events](https://vuejs.org/guide/components/events.html)
- [Vue.js Fallthrough Attributes](https://vuejs.org/guide/components/attrs.html)
- [Vue 3 Migration - .native Modifier Removed](https://v3-migration.vuejs.org/breaking-changes/v-on-native-modifier-removed.html)
```

## File: `skills/vue-debug-guides/reference/component-naming-conflicts.md`
```markdown
---
title: Avoid Component Naming Conflicts Between Global and Local
impact: HIGH
impactDescription: Naming conflicts cause unexpected component rendering and hard-to-debug issues
type: gotcha
tags: [vue3, component-registration, naming-conflicts, global-local, debugging]
---

# Avoid Component Naming Conflicts Between Global and Local

**Impact: HIGH** - When a global component and a local component have the same name (or resolve to the same name due to casing differences), unexpected behavior occurs. The precedence rules can be confusing, and the wrong component may render silently without any error. This is particularly problematic when using third-party component libraries.

## Task Checklist

- [ ] Use unique, prefixed names for global components (e.g., `BaseButton`, `AppHeader`)
- [ ] Check for naming conflicts when adding global components
- [ ] Explicitly alias local components if there's potential conflict
- [ ] When overriding third-party components, document and test thoroughly

**Incorrect:**
```javascript
// main.js
import { createApp } from 'vue'
import Button from './components/Button.vue'

const app = createApp(App)
app.component('Button', Button) // Global Button
```

```vue
<!-- SomeComponent.vue -->
<script setup>
// This local Button might conflict with global Button
import Button from './local/Button.vue'
</script>

<template>
  <!-- Which Button renders? Behavior may be unexpected -->
  <Button>Click me</Button>
</template>
```

```vue
<!-- Another confusing scenario -->
<script setup>
// Registering with camelCase
import MyButton from './MyButton.vue'
</script>

<template>
  <!-- Using kebab-case - might match a global 'my-button' instead -->
  <my-button>Click</my-button>
</template>
```

**Correct:**
```javascript
// main.js - use prefixes for global components
import { createApp } from 'vue'
import BaseButton from './components/BaseButton.vue'
import BaseIcon from './components/BaseIcon.vue'

const app = createApp(App)
app.component('BaseButton', BaseButton)
app.component('BaseIcon', BaseIcon)
```

```vue
<!-- SomeComponent.vue -->
<script setup>
// Local components have distinct names
import SubmitButton from './local/SubmitButton.vue'
</script>

<template>
  <!-- No ambiguity - each name is unique -->
  <BaseButton>Generic button</BaseButton>
  <SubmitButton>Submit form</SubmitButton>
</template>
```

## Explicit Aliasing for Clarity

When you intentionally want to override or have similar names, use explicit aliasing:

```vue
<script setup>
// Explicit alias to avoid confusion
import { default as LocalButton } from './Button.vue'
</script>

<template>
  <LocalButton>Local version</LocalButton>
</template>
```

```vue
<!-- Options API with explicit component name -->
<script>
import ThirdPartyModal from 'some-library'
import CustomModal from './CustomModal.vue'

export default {
  components: {
    // Explicit names prevent ambiguity
    LibraryModal: ThirdPartyModal,
    CustomModal
  }
}
</script>
```

## Resolution Order

Understanding Vue's component resolution order helps debug issues:

1. **Local registration** takes precedence over global
2. **Exact case match** takes precedence over case-insensitive match
3. Self-referencing component name (file name) has lowest priority

```vue
<!-- If all exist: GlobalButton, local Button, and file is Button.vue -->
<script setup>
import Button from './Button.vue' // Local registration
</script>

<template>
  <!-- Resolves to locally imported Button, not global -->
  <Button />
</template>
```

## Third-Party Library Conflicts

```vue
<script setup>
// Be explicit when using components from multiple libraries
import { Button as AntButton } from 'ant-design-vue'
import { Button as ElButton } from 'element-plus'
</script>

<template>
  <AntButton>Ant Design</AntButton>
  <ElButton>Element Plus</ElButton>
</template>
```

## Naming Convention Strategy

| Component Type | Naming Pattern | Example |
|----------------|---------------|---------|
| Base/Global | `Base*` or `App*` prefix | `BaseButton`, `AppHeader` |
| Domain-specific | Domain prefix | `UserCard`, `ProductList` |
| Page components | `*Page` or `*View` suffix | `HomePage`, `UserView` |
| Layout components | `*Layout` suffix | `DefaultLayout`, `AdminLayout` |

## Reference
- [Vue.js Component Registration](https://vuejs.org/guide/components/registration.html)
- [GitHub Issue: Global component naming conflicts](https://github.com/vuejs/vue/issues/4434)
```

## File: `skills/vue-debug-guides/reference/component-ref-requires-defineexpose.md`
```markdown
---
title: Component Refs Require defineExpose with Script Setup
impact: HIGH
impactDescription: Parent components cannot access child ref properties unless explicitly exposed
type: gotcha
tags: [vue3, template-refs, script-setup, defineExpose, component-communication]
---

# Component Refs Require defineExpose with Script Setup

**Impact: HIGH** - Components using `<script setup>` are private by default. A parent component using a template ref to access a child will get an empty object unless the child explicitly exposes properties using `defineExpose()`. This is a fundamental change from Options API behavior.

This catches many developers off-guard when migrating from Options API, where `this.$refs.child` gave full access to the child instance.

## Task Checklist

- [ ] Use `defineExpose()` to explicitly expose properties/methods to parent refs
- [ ] Only expose what's necessary - keep component internals private
- [ ] Document exposed APIs as they form your component's public interface
- [ ] Prefer props/emit for parent-child communication; use refs sparingly
- [ ] Call defineExpose before any await operation (see async caveat)

**Incorrect:**
```vue
<!-- ChildComponent.vue -->
<script setup>
import { ref } from 'vue'

const count = ref(0)
const internalState = ref('private')

function increment() {
  count.value++
}

function reset() {
  count.value = 0
}

// WRONG: Nothing exposed - parent ref sees empty object
</script>

<template>
  <div>{{ count }}</div>
</template>
```

```vue
<!-- ParentComponent.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import ChildComponent from './ChildComponent.vue'

const childRef = ref(null)

onMounted(() => {
  // WRONG: childRef.value is {} - empty object!
  console.log(childRef.value.count) // undefined
  childRef.value.increment() // TypeError: not a function
})
</script>

<template>
  <ChildComponent ref="childRef" />
</template>
```

**Correct:**
```vue
<!-- ChildComponent.vue -->
<script setup>
import { ref } from 'vue'

const count = ref(0)
const internalState = ref('private') // Keep this private

function increment() {
  count.value++
}

function reset() {
  count.value = 0
}

// CORRECT: Explicitly expose public API
defineExpose({
  count,      // Expose the ref
  increment,  // Expose methods
  reset
  // internalState NOT exposed - stays private
})
</script>

<template>
  <div>{{ count }}</div>
</template>
```

```vue
<!-- ParentComponent.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import ChildComponent from './ChildComponent.vue'

const childRef = ref(null)

onMounted(() => {
  // CORRECT: Can access exposed properties
  console.log(childRef.value.count) // 0
  childRef.value.increment() // Works!

  // internalState is not accessible (private)
  console.log(childRef.value.internalState) // undefined
})
</script>

<template>
  <ChildComponent ref="childRef" />
</template>
```

```vue
<!-- Input wrapper example - exposing native element -->
<script setup>
import { ref } from 'vue'

const inputEl = ref(null)

// Expose the native input for parent to access (e.g., for focus)
defineExpose({
  focus: () => inputEl.value?.focus(),
  blur: () => inputEl.value?.blur(),
  // Or expose the element directly
  el: inputEl
})
</script>

<template>
  <input ref="inputEl" v-bind="$attrs" />
</template>
```

```javascript
// Options API equivalent using expose option
export default {
  expose: ['count', 'increment', 'reset'],
  data() {
    return {
      count: 0,
      internalState: 'private'
    }
  },
  methods: {
    increment() { this.count++ },
    reset() { this.count = 0 }
  }
}
```

## Best Practice Reminder

Component refs create tight coupling between parent and child. Prefer standard patterns:

```vue
<!-- PREFERRED: Use props and emit for communication -->
<script setup>
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])
</script>

<!-- Only use refs for imperative actions like focus(), scrollTo(), etc. -->
```

## Reference
- [Vue.js Component Refs](https://vuejs.org/guide/essentials/template-refs.html#ref-on-component)
- [Script Setup - defineExpose](https://vuejs.org/api/sfc-script-setup.html#defineexpose)
```

## File: `skills/vue-debug-guides/reference/composable-avoid-hidden-side-effects.md`
```markdown
---
title: Avoid Hidden Side Effects in Composables
impact: HIGH
impactDescription: Side effects hidden in composables make debugging difficult and create implicit coupling between components
type: best-practice
tags: [vue3, composables, composition-api, side-effects, provide-inject, global-state]
---

# Avoid Hidden Side Effects in Composables

**Impact: HIGH** - Composables should encapsulate stateful logic, not hide side effects that affect things outside their scope. Hidden side effects like modifying global state, using provide/inject internally, or manipulating the DOM directly make composables unpredictable and hard to debug.

When a composable has unexpected side effects, consumers can't reason about what calling it will do. This leads to bugs that are difficult to trace and composables that can't be safely reused.

## Task Checklist

- [ ] Avoid using provide/inject inside composables (make dependencies explicit)
- [ ] Don't modify Pinia/Vuex store state internally (accept store as parameter instead)
- [ ] Don't manipulate DOM directly (use template refs passed as arguments)
- [ ] Document any unavoidable side effects clearly
- [ ] Keep composables focused on returning reactive state and methods

**Incorrect:**
```javascript
// WRONG: Hidden provide/inject dependency
export function useTheme() {
  // Consumer has no idea this depends on a provided theme
  const theme = inject('theme')  // What if nothing provides this?

  const isDark = computed(() => theme?.mode === 'dark')
  return { isDark }
}

// WRONG: Modifying global store internally
import { useUserStore } from '@/stores/user'

export function useLogin() {
  const userStore = useUserStore()

  async function login(credentials) {
    const user = await api.login(credentials)
    // Hidden side effect: modifying global state
    userStore.setUser(user)
    userStore.setToken(user.token)
    // Consumer doesn't know the store was modified!
  }

  return { login }
}

// WRONG: Hidden DOM manipulation
export function useFocusTrap() {
  onMounted(() => {
    // Which element? Consumer has no control
    document.querySelector('.modal')?.focus()
  })
}

// WRONG: Hidden provide that affects descendants
export function useFormContext() {
  const form = reactive({ values: {}, errors: {} })
  // Components calling this have no idea it provides something
  provide('form-context', form)
  return form
}
```

**Correct:**
```javascript
// CORRECT: Explicit dependency injection
export function useTheme(injectedTheme) {
  // If no theme passed, consumer must handle it
  const theme = injectedTheme ?? { mode: 'light' }

  const isDark = computed(() => theme.mode === 'dark')
  return { isDark }
}

// Usage - dependency is explicit
const theme = inject('theme', { mode: 'light' })
const { isDark } = useTheme(theme)

// CORRECT: Return actions, let consumer decide when to call them
export function useLogin() {
  const user = ref(null)
  const token = ref(null)
  const isLoading = ref(false)
  const error = ref(null)

  async function login(credentials) {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.login(credentials)
      user.value = response.user
      token.value = response.token
      return response
    } catch (e) {
      error.value = e
      throw e
    } finally {
      isLoading.value = false
    }
  }

  return { user, token, isLoading, error, login }
}

// Consumer decides what to do with the result
const { user, token, login } = useLogin()
const userStore = useUserStore()

async function handleLogin(credentials) {
  await login(credentials)
  // Consumer explicitly updates the store
  userStore.setUser(user.value)
  userStore.setToken(token.value)
}

// CORRECT: Accept element as parameter
export function useFocusTrap(targetRef) {
  onMounted(() => {
    targetRef.value?.focus()
  })

  onUnmounted(() => {
    // Cleanup focus trap
  })
}

// Usage - consumer controls which element
const modalRef = ref(null)
useFocusTrap(modalRef)

// CORRECT: Separate composable from provider
export function useFormContext() {
  const form = reactive({ values: {}, errors: {} })
  return form
}

// In parent component - explicit provide
const form = useFormContext()
provide('form-context', form)
```

## Acceptable Side Effects (With Documentation)

Some side effects are acceptable when they're the core purpose of the composable:

```javascript
/**
 * Tracks mouse position globally.
 *
 * SIDE EFFECTS:
 * - Adds 'mousemove' event listener to window (cleaned up on unmount)
 *
 * @returns {Object} Mouse coordinates { x, y }
 */
export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  // This side effect is the whole point of the composable
  // and is properly cleaned up
  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }

  return { x, y }
}
```

## Pattern: Dependency Injection for Flexibility

```javascript
// Composable accepts its dependencies
export function useDataFetcher(apiClient, cache = null) {
  const data = ref(null)

  async function fetch(url) {
    if (cache) {
      const cached = cache.get(url)
      if (cached) {
        data.value = cached
        return
      }
    }

    data.value = await apiClient.get(url)
    cache?.set(url, data.value)
  }

  return { data, fetch }
}

// Usage - dependencies are explicit and testable
const apiClient = inject('apiClient')
const cache = inject('cache', null)
const { data, fetch } = useDataFetcher(apiClient, cache)
```

## Reference
- [Vue.js Composables](https://vuejs.org/guide/reusability/composables.html)
- [Common Mistakes Creating Composition Functions](https://www.telerik.com/blogs/common-mistakes-creating-composition-functions-vue)
```

## File: `skills/vue-debug-guides/reference/composable-call-location-restrictions.md`
```markdown
---
title: Call Composables Only in Setup Context Synchronously
impact: HIGH
impactDescription: Composables called outside setup context or asynchronously fail to register lifecycle hooks and may cause memory leaks
type: gotcha
tags: [vue3, composables, composition-api, setup, async, lifecycle]
---

# Call Composables Only in Setup Context Synchronously

**Impact: HIGH** - Composables must be called synchronously within `<script setup>`, the `setup()` function, or lifecycle hooks. Calling composables asynchronously (after await), in callbacks, or outside component context prevents Vue from associating lifecycle hooks with the component instance, causing silent failures.

This is critical because composables often register `onMounted` and `onUnmounted` hooks internally. If called in the wrong context, these hooks are never registered, leading to uninitialized state or memory leaks.

## Task Checklist

- [ ] Call all composables at the top level of `<script setup>` or `setup()`
- [ ] Never call composables inside async callbacks, setTimeout, or Promise.then
- [ ] Never call composables conditionally (if/else) - call unconditionally and handle the condition inside
- [ ] Never call composables inside loops - restructure to call once with array data
- [ ] Exception: Composables CAN be called in lifecycle hooks like `onMounted`

**Incorrect:**
```vue
<script setup>
import { useFetch } from './composables/useFetch'
import { useAuth } from './composables/useAuth'

// WRONG: Composable called after await
const config = await loadConfig()
const { data } = useFetch(config.apiUrl)  // Lifecycle hooks won't register!

// WRONG: Composable called conditionally
if (someCondition) {
  const { user } = useAuth()  // Inconsistent hook registration!
}

// WRONG: Composable called in callback
setTimeout(() => {
  const { data } = useFetch('/api/delayed')  // No component context!
}, 1000)

// WRONG: Composable called in loop
for (const url of urls) {
  const { data } = useFetch(url)  // Creates multiple instances incorrectly
}
</script>
```

**Correct:**
```vue
<script setup>
import { ref, onMounted } from 'vue'
import { useFetch } from './composables/useFetch'
import { useAuth } from './composables/useAuth'

// CORRECT: Call composables synchronously at top level
const { user, isAuthenticated } = useAuth()
const apiUrl = ref('/api/default')
const { data, execute } = useFetch(apiUrl)

// Handle async config loading differently
onMounted(async () => {
  const config = await loadConfig()
  apiUrl.value = config.apiUrl  // Update the ref, composable reacts
})

// CORRECT: Handle condition inside, not outside
const showUserData = computed(() => isAuthenticated.value && someCondition)

// CORRECT: For multiple URLs, use a different pattern
const urls = ref(['/api/a', '/api/b', '/api/c'])
const results = ref([])

// Either fetch in onMounted or use a composable designed for arrays
onMounted(async () => {
  results.value = await Promise.all(urls.value.map(url => fetch(url)))
})
</script>
```

## Exception: Calling in Lifecycle Hooks

Composables CAN be called inside lifecycle hooks because Vue maintains the component context:

```vue
<script setup>
import { onMounted } from 'vue'
import { useEventListener } from '@vueuse/core'

// CORRECT: Called in lifecycle hook - component context is available
onMounted(() => {
  // This works because we're still in the component's execution context
  useEventListener(document, 'visibilitychange', handleVisibility)
})
</script>
```

## Special Case: Async Setup in `<script setup>`

Top-level await in `<script setup>` is special - Vue's compiler automatically preserves context:

```vue
<script setup>
import { useFetch } from './composables/useFetch'

// CORRECT: Top-level await in <script setup> preserves context
// Vue compiler handles this specially
const config = await loadConfig()
const { data } = useFetch(config.apiUrl)  // This works!

// But nested awaits still break context:
async function initLater() {
  await delay(1000)
  const { data } = useFetch('/api/late')  // WRONG: This won't work!
}
</script>
```

## Why This Matters

When you call a composable, Vue needs to know which component instance to associate it with. This association happens through an internal "current instance" that's only set during synchronous setup execution.

```javascript
// Inside a composable
export function useFetch(url) {
  const data = ref(null)

  // These need the current component instance!
  onMounted(() => { /* ... */ })
  onUnmounted(() => { /* cleanup */ })

  // If called outside setup context, Vue can't find the instance
  // and these hooks are silently ignored
  return { data }
}
```

## Reference
- [Vue.js Composables - Usage Restrictions](https://vuejs.org/guide/reusability/composables.html#usage-restrictions)
- [Vue.js Composition API - Setup Context](https://vuejs.org/api/composition-api-setup.html)
```

## File: `skills/vue-debug-guides/reference/composable-naming-return-pattern.md`
```markdown
---
title: Follow Composable Naming Convention and Return Pattern
impact: MEDIUM
impactDescription: Inconsistent composable patterns lead to confusing APIs and reactivity issues when destructuring
type: best-practice
tags: [vue3, composables, composition-api, naming, conventions, refs]
---

# Follow Composable Naming Convention and Return Pattern

**Impact: MEDIUM** - Vue composables should follow established conventions: prefix names with "use" and return plain objects containing refs (not reactive objects). Returning reactive objects causes reactivity loss when destructuring, while inconsistent naming makes code harder to understand.

## Task Checklist

- [ ] Name composables with "use" prefix (e.g., `useMouse`, `useFetch`, `useAuth`)
- [ ] Return a plain object containing refs, not a reactive object
- [ ] Allow both destructuring and object-style access
- [ ] Document the returned refs for consumers

**Incorrect:**
```javascript
// WRONG: No "use" prefix - unclear it's a composable
export function mousePosition() {
  const x = ref(0)
  const y = ref(0)
  return { x, y }
}

// WRONG: Returning reactive object - destructuring loses reactivity
export function useMouse() {
  const state = reactive({
    x: 0,
    y: 0
  })
  // When consumer destructures: const { x, y } = useMouse()
  // x and y become plain values, not reactive!
  return state
}

// WRONG: Returning single ref directly - inconsistent API
export function useCounter() {
  const count = ref(0)
  return count  // Consumer must use .value everywhere
}
```

**Correct:**
```javascript
// CORRECT: "use" prefix and returns plain object with refs
export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  // Return plain object containing refs
  return { x, y }
}

// Consumer can destructure and keep reactivity
const { x, y } = useMouse()
watch(x, (newX) => console.log('x changed:', newX))  // Works!

// Or use as object if preferred
const mouse = useMouse()
console.log(mouse.x.value)
```

## Using reactive() Wrapper for Auto-Unwrapping

If consumers prefer auto-unwrapping (no `.value`), they can wrap the result:

```javascript
import { reactive } from 'vue'
import { useMouse } from './composables/useMouse'

// Wrapping in reactive() links the refs
const mouse = reactive(useMouse())

// Now access without .value
console.log(mouse.x)  // Auto-unwrapped, still reactive

// But DON'T destructure from this!
const { x } = reactive(useMouse())  // WRONG: loses reactivity again
```

## Pattern: Returning Both State and Actions

```javascript
// Composable with state AND methods
export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  const doubleCount = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  function decrement() {
    count.value--
  }

  function reset() {
    count.value = initialValue
  }

  // Return all refs and functions in plain object
  return {
    count,
    doubleCount,
    increment,
    decrement,
    reset
  }
}

// Usage
const { count, doubleCount, increment, reset } = useCounter(10)
```

## Naming Convention Examples

| Good Name | Bad Name | Reason |
|-----------|----------|--------|
| `useFetch` | `fetch` | Conflicts with native fetch |
| `useAuth` | `authStore` | "Store" implies Pinia/Vuex |
| `useLocalStorage` | `localStorage` | Conflicts with native API |
| `useFormValidation` | `validateForm` | Sounds like a one-shot function |
| `useWindowSize` | `getWindowSize` | "get" implies synchronous getter |

## Reference
- [Vue.js Composables - Conventions and Best Practices](https://vuejs.org/guide/reusability/composables.html#conventions-and-best-practices)
- [Vue.js Composables - Return Values](https://vuejs.org/guide/reusability/composables.html#return-values)
```

## File: `skills/vue-debug-guides/reference/composable-tovalue-inside-watcheffect.md`
```markdown
---
title: Call toValue() Inside watchEffect for Proper Dependency Tracking
impact: HIGH
impactDescription: Calling toValue() outside watchEffect prevents reactive dependency tracking, causing the effect to never re-run
type: gotcha
tags: [vue3, composables, composition-api, watchEffect, toValue, reactivity]
---

# Call toValue() Inside watchEffect for Proper Dependency Tracking

**Impact: HIGH** - When writing composables that accept `MaybeRefOrGetter` arguments, you must call `toValue()` inside the `watchEffect` callback, not outside. If you extract the value before the watchEffect, Vue cannot track the dependency and the effect will never re-run when the source changes.

This is a subtle but critical mistake that leads to composables that work with initial values but never update.

## Task Checklist

- [ ] Always call `toValue()` inside `watchEffect` callbacks, not before
- [ ] Similarly, access `.value` on refs inside watchEffect, not outside
- [ ] For `watch()`, use a getter function that calls `toValue()`
- [ ] Test that composables update when their inputs change

**Incorrect:**
```javascript
import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)

  // WRONG: toValue called outside watchEffect
  // This extracts the value ONCE and passes a static string
  const urlValue = toValue(url)

  watchEffect(async () => {
    try {
      // urlValue is a static string - no dependency tracked!
      const response = await fetch(urlValue)
      data.value = await response.json()
    } catch (e) {
      error.value = e
    }
  })

  return { data, error }
}

// When used like this:
const apiUrl = ref('/api/users')
const { data } = useFetch(apiUrl)

// Later...
apiUrl.value = '/api/products'  // useFetch will NOT refetch!
```

**Correct:**
```javascript
import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)

  watchEffect(async () => {
    // CORRECT: toValue called INSIDE watchEffect
    // Vue tracks this as a dependency
    const urlValue = toValue(url)

    try {
      const response = await fetch(urlValue)
      data.value = await response.json()
    } catch (e) {
      error.value = e
    }
  })

  return { data, error }
}

// Now when used:
const apiUrl = ref('/api/users')
const { data } = useFetch(apiUrl)

// Later...
apiUrl.value = '/api/products'  // useFetch WILL refetch!
```

## The Same Applies to Direct Ref Access

```javascript
// WRONG: Accessing .value outside the effect
export function useDebounce(source, delay = 300) {
  // This captures the initial value, not a reactive dependency
  const initialValue = source.value  // or toValue(source)

  watchEffect(() => {
    // initialValue is static - this only runs once
    console.log('Value:', initialValue)
  })
}

// CORRECT: Access inside the effect
export function useDebounce(source, delay = 300) {
  watchEffect(() => {
    // Vue tracks source.value or toValue(source) as dependency
    console.log('Value:', toValue(source))
  })
}
```

## Pattern: Using watch() with Getter Functions

For `watch()`, wrap `toValue()` in a getter:

```javascript
import { ref, watch, toValue } from 'vue'

export function useLocalStorage(key, defaultValue) {
  const data = ref(defaultValue)

  // CORRECT: Use getter function with watch
  watch(
    () => toValue(key),  // Getter calls toValue, tracks dependency
    (newKey) => {
      const stored = localStorage.getItem(newKey)
      data.value = stored ? JSON.parse(stored) : defaultValue
    },
    { immediate: true }
  )

  return data
}
```

## Why This Happens

Vue's reactivity tracking works by detecting property accesses during effect execution:

```javascript
watchEffect(() => {
  // When this runs, Vue is "recording" what reactive sources are accessed
  const value = someRef.value  // Vue records: "this effect depends on someRef"
})

// But if you extract the value before:
const value = someRef.value  // Vue isn't recording yet
watchEffect(() => {
  console.log(value)  // Just using a plain JavaScript variable
})
```

`toValue()` works the same way - it accesses `.value` internally, so it must happen during effect execution for tracking to work.

## Quick Checklist for Composable Authors

When accepting `MaybeRefOrGetter` inputs:

1. Store the raw argument (don't call `toValue` during setup)
2. Call `toValue()` inside any reactive context (`watchEffect`, `watch`, `computed`)
3. Test with both static values AND refs that change

```javascript
export function useMyComposable(input) {
  // Store raw - don't extract value here
  // const value = toValue(input)  // WRONG

  const result = computed(() => {
    // Extract value inside reactive context
    return transform(toValue(input))  // CORRECT
  })

  watchEffect(() => {
    // Extract value inside reactive context
    doSomething(toValue(input))  // CORRECT
  })

  return { result }
}
```

## Reference
- [Vue.js Reactivity API - toValue](https://vuejs.org/api/reactivity-utilities.html#tovalue)
- [Vue.js Composables - Accepting Ref Arguments](https://vuejs.org/guide/reusability/composables.html#accepting-reactive-state)
```

## File: `skills/vue-debug-guides/reference/composition-api-not-functional-programming.md`
```markdown
---
title: Composition API Uses Mutable Reactivity, Not Functional Programming
impact: MEDIUM
impactDescription: Misunderstanding the paradigm leads to incorrect state management patterns
type: gotcha
tags: [vue3, composition-api, reactivity, functional-programming, paradigm]
---

# Composition API Uses Mutable Reactivity, Not Functional Programming

**Impact: MEDIUM** - Despite being function-based, the Composition API follows Vue's mutable, fine-grained reactivity paradigm—NOT functional programming principles. Treating it like a functional paradigm leads to incorrect patterns like unnecessary cloning, immutable-style updates, or avoiding mutation when mutation is the intended pattern.

Vue's Composition API leverages imported functions to organize code, but the underlying model is based on mutable reactive state that Vue tracks and responds to. This is fundamentally different from functional programming with immutability (like Redux reducers).

## Task Checklist

- [ ] Mutate reactive state directly - don't create new objects for every update
- [ ] Don't apply immutability patterns unnecessarily (spreading, Object.assign for updates)
- [ ] Understand that `ref()` and `reactive()` enable mutable state tracking
- [ ] Use Vue's reactivity as intended: direct mutation with automatic tracking

**Incorrect:**
```javascript
import { ref } from 'vue'

const todos = ref([])

// WRONG: Treating Vue like Redux/functional - unnecessary immutability
function addTodo(todo) {
  // Creating a new array every time is wasteful in Vue
  todos.value = [...todos.value, todo]
}

function updateTodo(id, updates) {
  // Unnecessary spread - Vue tracks mutations directly
  todos.value = todos.value.map(t =>
    t.id === id ? { ...t, ...updates } : t
  )
}

const user = ref({ name: 'John', age: 30 })

// WRONG: Creating new object for simple update
function updateName(newName) {
  user.value = { ...user.value, name: newName }
}
```

**Correct:**
```javascript
import { ref, reactive } from 'vue'

const todos = ref([])

// CORRECT: Mutate directly - Vue tracks the change
function addTodo(todo) {
  todos.value.push(todo)  // Direct mutation is the Vue way
}

function updateTodo(id, updates) {
  const todo = todos.value.find(t => t.id === id)
  if (todo) {
    Object.assign(todo, updates)  // Direct mutation
  }
}

const user = ref({ name: 'John', age: 30 })

// CORRECT: Mutate the property directly
function updateName(newName) {
  user.value.name = newName  // Vue tracks this!
}

// Or with reactive():
const state = reactive({ name: 'John', age: 30 })

function updateNameReactive(newName) {
  state.name = newName  // Direct mutation, reactivity preserved
}
```

## When Immutability Patterns Make Sense

```javascript
// Immutability IS appropriate when:

// 1. Replacing the entire state (e.g., from API response)
const users = ref([])
async function fetchUsers() {
  users.value = await api.getUsers()  // Complete replacement is fine
}

// 2. When you need a snapshot for comparison
const previousState = { ...currentState }  // For undo/redo

// 3. When passing data to external libraries expecting immutable data
const chartData = computed(() => [...rawData.value])  // Copy for chart lib
```

## The Vue Mental Model

```javascript
// Vue's reactivity is like a spreadsheet:
// - Cell A1 contains a value (ref)
// - Cell B1 has a formula referencing A1 (computed)
// - Change A1, and B1 automatically updates

const a1 = ref(10)
const b1 = computed(() => a1.value * 2)

// You CHANGE A1 (mutate), you don't create a new A1
a1.value = 20  // b1 automatically becomes 40

// This is fundamentally different from:
// state = reducer(state, action)  // Functional/Redux pattern
```

## Reference
- [Composition API FAQ](https://vuejs.org/guide/extras/composition-api-faq.html)
- [Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)
```

## File: `skills/vue-debug-guides/reference/composition-api-script-setup-async-context.md`
```markdown
---
title: Top-Level await in script setup Preserves Component Context
impact: HIGH
impactDescription: Misunderstanding async context causes lifecycle hooks and watchers to silently fail
type: gotcha
tags: [vue3, composition-api, script-setup, async, await, suspense]
---

# Top-Level await in script setup Preserves Component Context

**Impact: HIGH** - In `<script setup>`, top-level `await` statements preserve component context (allowing lifecycle hooks and watchers after `await`), but this is a special case. Nested async functions or callbacks lose context, causing lifecycle hooks to silently fail.

Vue's compiler automatically injects context restoration after each top-level await in `<script setup>`. This doesn't apply to `setup()` function or nested async contexts.

## Task Checklist

- [ ] Understand that top-level await in `<script setup>` is specially handled
- [ ] Never register lifecycle hooks in nested async functions
- [ ] Use `<Suspense>` when using async `<script setup>` components
- [ ] In regular `setup()`, never use await before lifecycle hook registration
- [ ] Register hooks synchronously, then do async work inside them

**Top-Level await Works (script setup only):**
```vue
<script setup>
import { ref, onMounted, watch } from 'vue'

// This is TOP-LEVEL await - Vue compiler preserves context
const config = await fetchConfig()  // OK!

// These hooks work because Vue restored context
onMounted(() => {
  console.log('This will run!')  // Works
})

watch(someRef, () => {
  console.log('This will track!')  // Works
})

// Another top-level await - still OK
const data = await fetchData(config.apiUrl)  // OK!

// Still works after multiple awaits
onMounted(() => {
  console.log('This also runs!')  // Works
})
</script>

<!-- IMPORTANT: Parent must use Suspense -->
<template>
  <Suspense>
    <AsyncComponent />
  </Suspense>
</template>
```

**Nested Async Breaks Context:**
```vue
<script setup>
import { ref, onMounted, watch } from 'vue'

// WRONG: Nested async function - context lost after await
async function initializeData() {
  const config = await fetchConfig()

  // BUG: This hook will NOT be registered!
  // We're no longer in the synchronous setup context
  onMounted(() => {
    console.log('This will NEVER run!')  // Silent failure
  })

  // BUG: This watcher won't auto-dispose on unmount
  watch(someRef, () => {
    console.log('Memory leak - not cleaned up!')
  })
}

// Calling the async function
initializeData()  // Hooks inside won't work!

// WRONG: Callbacks also lose context
setTimeout(async () => {
  await delay(100)
  onMounted(() => {
    console.log('Never runs!')  // Silent failure
  })
}, 0)
</script>
```

**Correct Patterns:**
```vue
<script setup>
import { ref, onMounted, watch } from 'vue'

const data = ref(null)
const config = ref(null)

// CORRECT: Register hooks synchronously FIRST
onMounted(async () => {
  // Then do async work INSIDE the hook
  config.value = await fetchConfig()
  data.value = await fetchData(config.value.apiUrl)
})

// CORRECT: Watchers registered synchronously
watch(config, async (newConfig) => {
  if (newConfig) {
    data.value = await fetchData(newConfig.apiUrl)
  }
})

// Or use top-level await for initial data
const initialConfig = await fetchConfig()  // OK - top level
config.value = initialConfig

onMounted(() => {
  console.log('Works!')  // Context preserved by compiler
})
</script>
```

**setup() Function (Not script setup):**
```javascript
// In regular setup(), await ALWAYS breaks context
export default {
  async setup() {
    const data = ref(null)

    // WRONG: Hooks after await won't register
    const config = await fetchConfig()

    onMounted(() => {
      console.log('Never runs!')  // Silent failure!
    })

    return { data }
  }
}

// CORRECT: Register hooks before any await
export default {
  async setup() {
    const data = ref(null)

    // Register hooks FIRST (synchronous)
    onMounted(async () => {
      const config = await fetchConfig()
      data.value = await fetchData(config)
    })

    // Now you can await if needed
    // But hooks must be registered before this point

    return { data }
  }
}
```

## Why This Happens

```javascript
// Vue tracks the "current component instance" during setup
// This is like a global variable that gets set and cleared

// During synchronous setup:
function setup() {
  currentInstance = this  // Vue sets this

  onMounted(cb)  // Uses currentInstance to register

  // After await, JavaScript resumes in a microtask
  await something()

  // currentInstance is now null or different!
  onMounted(cb)  // Can't find the instance - silently fails
}

// <script setup> compiler adds restoration:
// After each await, it injects: setCurrentInstance(savedInstance)
```

## Suspense Requirement

```vue
<!-- When using async script setup, parent needs Suspense -->
<template>
  <Suspense>
    <!-- Async component with top-level await -->
    <AsyncChild />

    <!-- Optional: Loading state -->
    <template #fallback>
      <LoadingSpinner />
    </template>
  </Suspense>
</template>
```

## Reference
- [Composition API FAQ - Async Setup](https://vuejs.org/guide/extras/composition-api-faq.html)
- [Composables - Async Without Await](https://antfu.me/posts/async-with-composition-api)
- [Suspense](https://vuejs.org/guide/built-ins/suspense.html)
```

## File: `skills/vue-debug-guides/reference/composition-api-vs-react-hooks-differences.md`
```markdown
---
title: Vue Composition API Runs Once, Unlike React Hooks
impact: MEDIUM
impactDescription: Understanding this difference prevents over-engineering and React patterns that don't apply
type: gotcha
tags: [vue3, composition-api, react-hooks, setup, stale-closure]
---

# Vue Composition API Runs Once, Unlike React Hooks

**Impact: MEDIUM** - Vue's `setup()` or `<script setup>` executes only once per component instance, while React Hooks run on every render. Developers coming from React often apply patterns (dependency arrays, excessive memoization, useCallback) that are unnecessary and counterproductive in Vue.

Understanding this fundamental difference is crucial for writing idiomatic Vue code. Vue's approach eliminates entire categories of bugs (stale closures, exhaustive deps) that plague React applications.

## Task Checklist

- [ ] Don't implement "dependency arrays" - Vue tracks dependencies automatically
- [ ] Don't wrap functions in "useCallback" equivalents - not needed in Vue
- [ ] Don't use "useMemo" patterns - Vue's `computed()` handles this automatically
- [ ] Understand that closures in Vue don't go "stale" like in React
- [ ] Don't worry about "call order" - Vue composables can be conditional

**React Patterns to Avoid in Vue:**
```javascript
// These patterns are UNNECESSARY in Vue - they solve React-specific problems

// WRONG: Trying to implement dependency arrays (React pattern)
watch(
  [dep1, dep2, dep3],  // Vue tracks deps automatically in watchEffect
  () => {
    // ...
  }
)
// Unless you specifically WANT to control which deps trigger the watcher,
// prefer watchEffect() which auto-tracks

// WRONG: Memoizing callbacks like useCallback
const memoizedHandler = computed(() => {
  return () => doSomething(state.value)
})
// In Vue, just define the function normally - no memoization needed

// WRONG: Worrying about stale closures
function useData() {
  const data = ref(null)

  // In React, this could capture stale 'data' - NOT in Vue!
  // Vue refs are always current
  const handler = () => {
    console.log(data.value)  // Always gets current value
  }

  return { data, handler }
}
```

**Correct Vue Patterns:**
```javascript
import { ref, computed, watchEffect } from 'vue'

// CORRECT: Auto-dependency tracking with watchEffect
const query = ref('')
const filter = ref('all')

watchEffect(() => {
  // Vue automatically detects that this depends on query and filter
  // No dependency array needed!
  fetchResults(query.value, filter.value)
})

// CORRECT: computed() handles memoization automatically
const expensiveResult = computed(() => {
  // Only recalculates when dependencies actually change
  return heavyComputation(data.value)
})

// CORRECT: Functions don't need memoization
function handleClick() {
  count.value++
}
// Just use it directly - no useCallback wrapper needed
// <button @click="handleClick">

// CORRECT: Closures always access current values
const count = ref(0)
const message = ref('')

function logState() {
  // This always logs CURRENT values, never stale ones
  console.log(`Count: ${count.value}, Message: ${message.value}`)
}

setTimeout(() => {
  logState()  // Gets current values even if called later
}, 5000)
```

## Vue's Advantages Over React Hooks

```javascript
// 1. No stale closure problems
const count = ref(0)

onMounted(() => {
  setInterval(() => {
    // In React: would need useRef or deps array to avoid stale value
    // In Vue: count.value is always current
    console.log(count.value)
  }, 1000)
})

// 2. Composables can be conditional
if (featureEnabled) {
  const { data } = useSomeFeature()  // This is FINE in Vue!
}
// In React: "Hooks cannot be conditional" - not a problem in Vue

// 3. No exhaustive-deps linting headaches
watchEffect(() => {
  // Use any reactive values - Vue tracks them all automatically
  // No ESLint rule yelling about missing dependencies
  doSomething(a.value, b.value, c.value)
})

// 4. Child components don't need memoization by default
// Vue's reactivity system only updates what actually changed
// No need for React.memo() equivalents in most cases
```

## When Vue Patterns Differ

```javascript
// Setup runs once - so initialization happens once
<script setup>
import { ref, onMounted } from 'vue'

// This code runs ONCE when component is created
const data = ref(null)
console.log('Setup running')  // Only logs once

onMounted(() => {
  console.log('Mounted')  // Only logs once
})

// If you need something to run on every reactive change,
// use watch or watchEffect
watchEffect(() => {
  // This runs when dependencies change
  console.log('Data changed:', data.value)
})
</script>
```

## Reference
- [Composition API FAQ - Relationship with React Hooks](https://vuejs.org/guide/extras/composition-api-faq.html#relationship-with-react-hooks)
- [Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)
```

## File: `skills/vue-debug-guides/reference/computed-array-mutation.md`
```markdown
---
title: Avoid Mutating Methods on Arrays in Computed Properties
impact: HIGH
impactDescription: Array mutating methods in computed modify source data causing unexpected behavior
type: capability
tags: [vue3, computed, arrays, mutation, sort, reverse]
---

# Avoid Mutating Methods on Arrays in Computed Properties

**Impact: HIGH** - JavaScript array methods like `reverse()`, `sort()`, `splice()`, `push()`, `pop()`, `shift()`, and `unshift()` mutate the original array. Using them directly on reactive arrays inside computed properties will modify your source data, causing unexpected side effects and bugs.

## Task Checklist

- [ ] Always create a copy of arrays before using mutating methods
- [ ] Use spread operator `[...array]` or `slice()` to copy arrays
- [ ] Prefer non-mutating alternatives when available
- [ ] Be aware which array methods mutate vs return new arrays

**Incorrect:**
```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([3, 1, 4, 1, 5, 9, 2, 6])
const users = ref([
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 25 }
])

// BAD: sort() mutates the original array!
const sortedItems = computed(() => {
  return items.value.sort((a, b) => a - b)
})

// BAD: reverse() mutates the original array!
const reversedItems = computed(() => {
  return items.value.reverse()
})

// BAD: Both arrays now point to the same mutated data
// items.value and sortedItems.value are the SAME array
// items.value and reversedItems.value are the SAME array

// BAD: Chained mutations
const sortedUsers = computed(() => {
  return users.value.sort((a, b) => a.age - b.age)
})
</script>

<template>
  <!-- Original array is corrupted! -->
  <div>Original: {{ items }}</div>
  <div>Sorted: {{ sortedItems }}</div>
</template>
```

**Correct:**
```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([3, 1, 4, 1, 5, 9, 2, 6])
const users = ref([
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 25 }
])

// GOOD: Spread operator creates a copy first
const sortedItems = computed(() => {
  return [...items.value].sort((a, b) => a - b)
})

// GOOD: slice() also creates a copy
const reversedItems = computed(() => {
  return items.value.slice().reverse()
})

// GOOD: Copy before sorting objects
const sortedUsers = computed(() => {
  return [...users.value].sort((a, b) => a.age - b.age)
})

// GOOD: Use toSorted() (ES2023) - non-mutating
const sortedItemsModern = computed(() => {
  return items.value.toSorted((a, b) => a - b)
})

// GOOD: Use toReversed() (ES2023) - non-mutating
const reversedItemsModern = computed(() => {
  return items.value.toReversed()
})
</script>

<template>
  <!-- Original array stays intact -->
  <div>Original: {{ items }}</div>
  <div>Sorted: {{ sortedItems }}</div>
  <div>Reversed: {{ reversedItems }}</div>
</template>
```

## Mutating vs Non-Mutating Array Methods

| Mutating (Avoid in Computed) | Non-Mutating (Safe) |
|------------------------------|---------------------|
| `sort()` | `toSorted()` (ES2023) |
| `reverse()` | `toReversed()` (ES2023) |
| `splice()` | `toSpliced()` (ES2023) |
| `push()` | `concat()` |
| `pop()` | `slice(0, -1)` |
| `shift()` | `slice(1)` |
| `unshift()` | `[item, ...array]` |
| `fill()` | `map()` with new values |

## ES2023 Non-Mutating Alternatives

Modern JavaScript (ES2023) provides non-mutating versions of common array methods:

```javascript
// These return NEW arrays, safe for computed properties
const sorted = array.toSorted((a, b) => a - b)
const reversed = array.toReversed()
const spliced = array.toSpliced(1, 2, 'new')
const withReplaced = array.with(0, 'newFirst')
```

## Deep Copy for Nested Arrays

For arrays of objects where you might mutate nested properties:

```javascript
const items = ref([{ name: 'A', values: [1, 2, 3] }])

// Shallow copy - nested arrays still shared
const copied = computed(() => [...items.value])

// Deep copy if you need to mutate nested structures
const deepCopied = computed(() => {
  return JSON.parse(JSON.stringify(items.value))
  // Or use structuredClone():
  // return structuredClone(items.value)
})
```

## Reference
- [Vue.js Computed Properties - Avoid Mutating Computed Value](https://vuejs.org/guide/essentials/computed.html#avoid-mutating-computed-value)
- [MDN Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
```

## File: `skills/vue-debug-guides/reference/computed-conditional-dependencies.md`
```markdown
---
title: Ensure All Dependencies Are Accessed in Computed Properties
impact: HIGH
impactDescription: Conditional logic can prevent dependency tracking causing stale computed values
type: capability
tags: [vue3, computed, reactivity, dependency-tracking, gotcha]
---

# Ensure All Dependencies Are Accessed in Computed Properties

**Impact: HIGH** - Vue tracks computed property dependencies by monitoring which reactive properties are accessed during execution. If conditional logic prevents a property from being accessed on the first run, Vue won't track it as a dependency, causing the computed property to not update when that property changes.

This is a subtle but common source of bugs, especially with short-circuit evaluation (`&&`, `||`) and early returns.

## Task Checklist

- [ ] Access all reactive dependencies before any conditional logic
- [ ] Be cautious with short-circuit operators (`&&`, `||`) that may skip property access
- [ ] Store all dependencies in variables at the start of the computed getter
- [ ] Test computed properties with different initial states

**Incorrect:**
```vue
<script setup>
import { ref, computed } from 'vue'

const isEnabled = ref(false)
const data = ref('important data')

// BAD: If isEnabled is false initially, data.value is never accessed
// Vue won't track 'data' as a dependency!
const result = computed(() => {
  if (!isEnabled.value) {
    return 'disabled'
  }
  return data.value  // This dependency may not be tracked
})

// BAD: Short-circuit prevents second access
const password = ref('')
const confirmPassword = ref('')

const isValid = computed(() => {
  // If password is empty, confirmPassword is never accessed
  return password.value && password.value === confirmPassword.value
})

// BAD: Early return prevents dependency access
const user = ref(null)
const permissions = ref(['read', 'write'])

const canEdit = computed(() => {
  if (!user.value) {
    return false  // permissions.value never accessed when user is null
  }
  return permissions.value.includes('write')
})
</script>
```

**Correct:**
```vue
<script setup>
import { ref, computed } from 'vue'

const isEnabled = ref(false)
const data = ref('important data')

// GOOD: Access all dependencies first
const result = computed(() => {
  const enabled = isEnabled.value
  const currentData = data.value  // Always accessed

  if (!enabled) {
    return 'disabled'
  }
  return currentData
})

// GOOD: Access both values before comparison
const password = ref('')
const confirmPassword = ref('')

const isValid = computed(() => {
  const pwd = password.value
  const confirm = confirmPassword.value  // Always accessed

  return pwd && pwd === confirm
})

// GOOD: Access all reactive sources upfront
const user = ref(null)
const permissions = ref(['read', 'write'])

const canEdit = computed(() => {
  const currentUser = user.value
  const currentPermissions = permissions.value  // Always accessed

  if (!currentUser) {
    return false
  }
  return currentPermissions.includes('write')
})
</script>
```

## The Dependency Tracking Mechanism

Vue's reactivity system works by tracking which reactive properties are accessed when a computed property runs:

```javascript
// How Vue tracks dependencies (simplified):
// 1. Start tracking
// 2. Run the getter function
// 3. Record every .value or reactive property access
// 4. Stop tracking

const computed = computed(() => {
  // Vue starts tracking here
  if (conditionA.value) {      // conditionA is tracked
    return valueB.value        // valueB is ONLY tracked if conditionA is true
  }
  return 'default'             // If conditionA is false, valueB is NOT tracked!
})
```

## Pattern: Destructure All Dependencies First

```javascript
// GOOD PATTERN: Destructure/access everything at the top
const result = computed(() => {
  // Access all potential dependencies
  const { user, settings, items } = toRefs(store)
  const userVal = user.value
  const settingsVal = settings.value
  const itemsVal = items.value

  // Now use conditional logic safely
  if (!userVal) return []
  if (!settingsVal.enabled) return []
  return itemsVal.filter(i => i.active)
})
```

## Reference
- [Vue.js Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth.html)
- [GitHub Discussion: Dependency collection gotcha with conditionals](https://github.com/vuejs/Discussion/issues/15)
```

## File: `skills/vue-debug-guides/reference/computed-no-parameters.md`
```markdown
---
title: Computed Properties Cannot Accept Parameters
impact: MEDIUM
impactDescription: Attempting to pass arguments to computed properties fails or defeats caching
type: capability
tags: [vue3, computed, methods, parameters, common-mistake]
---

# Computed Properties Cannot Accept Parameters

**Impact: MEDIUM** - Computed properties are designed to derive values from reactive state without parameters. Attempting to pass arguments defeats the caching mechanism or causes errors. Use methods or computed properties that return functions instead.

## Task Checklist

- [ ] Use methods when you need to pass parameters
- [ ] Consider if the parameter can be reactive state instead
- [ ] If you must parameterize, understand that returning a function loses caching benefits
- [ ] Prefer method calls in templates for parameterized operations

**Incorrect:**
```vue
<template>
  <!-- BAD: Computed properties don't accept parameters like this -->
  <p>{{ filteredItems('active') }}</p>
  <p>{{ formattedPrice(100, 'USD') }}</p>
</template>

<script setup>
import { ref, computed } from 'vue'

const items = ref([/* ... */])

// BAD: This won't work as expected
// Computed is called once, not per parameter
const filteredItems = computed((status) => {  // status will be undefined or previous value
  return items.value.filter(i => i.status === status)
})
</script>
```

```vue
<script>
export default {
  data() {
    return { items: [/* ... */] }
  },
  computed: {
    // BAD: Computed doesn't receive arguments
    filteredItems(status) {  // 'status' is actually 'this' or undefined
      return this.items.filter(i => i.status === status)
    }
  }
}
</script>
```

**Correct:**
```vue
<template>
  <!-- GOOD: Use method for parameterized operations -->
  <p>{{ getFilteredItems('active') }}</p>
  <p>{{ formatPrice(100, 'USD') }}</p>

  <!-- GOOD: Or use computed with reactive filter state -->
  <select v-model="statusFilter">
    <option value="active">Active</option>
    <option value="inactive">Inactive</option>
  </select>
  <p>{{ filteredItems }}</p>
</template>

<script setup>
import { ref, computed } from 'vue'

const items = ref([/* ... */])
const statusFilter = ref('active')

// GOOD: Method for parameterized operations
function getFilteredItems(status) {
  return items.value.filter(i => i.status === status)
}

function formatPrice(amount, currency) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency
  }).format(amount)
}

// GOOD: Computed with reactive parameter
const filteredItems = computed(() => {
  return items.value.filter(i => i.status === statusFilter.value)
})
</script>
```

## Workaround: Computed Returning a Function

If you need something computed-like with parameters, you can return a function. **However, this defeats the caching benefit:**

```vue
<template>
  <p>{{ getItemsByStatus('active') }}</p>
</template>

<script setup>
import { ref, computed } from 'vue'

const items = ref([/* ... */])

// This works but provides NO caching benefit
// The inner function runs every time it's called
const getItemsByStatus = computed(() => {
  return (status) => items.value.filter(i => i.status === status)
})

// This is essentially equivalent to just using a method
// Only useful if you need to compose with other computed properties
</script>
```

## When to Use Each Approach

| Scenario | Approach | Caching |
|----------|----------|---------|
| Fixed filter based on reactive state | Computed | Yes |
| Dynamic filter passed as argument | Method | No |
| Filter options from user selection | Computed + reactive param | Yes |
| Formatting with variable parameters | Method | No |
| Composed derivation with argument | Computed returning function | Partial |

## Make Parameters Reactive

The best pattern is often to make the "parameter" a reactive value:

```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([/* ... */])

// Instead of passing 'status' as a parameter:
const currentStatus = ref('active')

// Make a computed that uses the reactive status
const filteredItems = computed(() => {
  return items.value.filter(i => i.status === currentStatus.value)
})

// Change the filter by updating the ref
function filterByStatus(status) {
  currentStatus.value = status
}
</script>
```

## Reference
- [Vue.js Computed Properties](https://vuejs.org/guide/essentials/computed.html)
- [Vue.js Methods](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-methods)
```

## File: `skills/vue-debug-guides/reference/computed-no-side-effects.md`
```markdown
---
title: Computed Property Getters Must Be Side-Effect Free
impact: HIGH
impactDescription: Side effects in computed getters break reactivity and cause unpredictable behavior
type: efficiency
tags: [vue3, computed, reactivity, side-effects, best-practices]
---

# Computed Property Getters Must Be Side-Effect Free

**Impact: HIGH** - Computed getter functions should only perform pure computation. Side effects in computed getters break Vue's reactivity model and cause bugs that are difficult to trace.

Computed properties are designed to declaratively describe how to derive a value from other reactive state. They are not meant to perform actions or modify state.

## Task Checklist

- [ ] Never mutate other reactive state inside a computed getter
- [ ] Never make async requests or API calls inside a computed getter
- [ ] Never perform DOM mutations inside a computed getter
- [ ] Use watchers for reacting to state changes with side effects
- [ ] Use event handlers for user-triggered actions

**Incorrect:**
```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([])
const count = ref(0)
const lastFetch = ref(null)

// BAD: Mutates other state
const doubledCount = computed(() => {
  count.value++  // Side effect - modifying state!
  return count.value * 2
})

// BAD: Makes async request
const userData = computed(async () => {
  const response = await fetch('/api/user')  // Side effect - API call!
  return response.json()
})

// BAD: Modifies DOM
const highlightedItems = computed(() => {
  document.title = `${items.value.length} items`  // Side effect - DOM mutation!
  return items.value.filter(i => i.highlighted)
})

// BAD: Writes to external state
const processedData = computed(() => {
  lastFetch.value = new Date()  // Side effect - modifying state!
  return items.value.map(i => i.name)
})
</script>
```

**Correct:**
```vue
<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const items = ref([])
const count = ref(0)
const userData = ref(null)

// GOOD: Pure computation only
const doubledCount = computed(() => {
  return count.value * 2
})

// GOOD: Use lifecycle hook for initial fetch
onMounted(async () => {
  const response = await fetch('/api/user')
  userData.value = await response.json()
})

// GOOD: Pure filtering
const highlightedItems = computed(() => {
  return items.value.filter(i => i.highlighted)
})

// GOOD: Use watcher for side effects
watch(items, (newItems) => {
  document.title = `${newItems.length} items`
}, { immediate: true })

// Increment count through event handler, not computed
function increment() {
  count.value++
}
</script>
```

## What Counts as a Side Effect

| Side Effect Type | Example | Alternative |
|-----------------|---------|-------------|
| State mutation | `otherRef.value = x` | Use watcher |
| API calls | `fetch()`, `axios()` | Use watcher or lifecycle hook |
| DOM manipulation | `document.title = x` | Use watcher |
| Console logging | `console.log()` | Remove or use watcher |
| Storage access | `localStorage.setItem()` | Use watcher |
| Timer setup | `setTimeout()` | Use lifecycle hook |

## Reference
- [Vue.js Computed Properties - Getters Should Be Side-Effect Free](https://vuejs.org/guide/essentials/computed.html#getters-should-be-side-effect-free)
```

## File: `skills/vue-debug-guides/reference/computed-return-value-readonly.md`
```markdown
---
title: Never Mutate Computed Property Return Values
impact: HIGH
impactDescription: Mutating computed values causes silent failures and lost changes
type: capability
tags: [vue3, computed, reactivity, immutability, common-mistake]
---

# Never Mutate Computed Property Return Values

**Impact: HIGH** - The returned value from a computed property is derived state - a temporary snapshot. Mutating this value leads to bugs that are difficult to debug.

**Important:** Mutations DO persist while the computed cache remains valid, but are lost when recomputation occurs. The danger lies in unpredictable cache invalidation timing - any change to the computed's dependencies triggers recomputation, silently discarding your mutations. This makes bugs intermittent and hard to reproduce.

Every time the source state changes, a new snapshot is created. Mutating a snapshot is meaningless because it will be discarded on the next recalculation.

## Task Checklist

- [ ] Treat computed return values as read-only
- [ ] Update the source state instead of the computed value
- [ ] Use writable computed properties if bidirectional binding is needed
- [ ] Avoid array mutating methods (push, pop, splice, reverse, sort) on computed arrays

**Incorrect:**
```vue
<script setup>
import { ref, computed } from 'vue'

const books = ref(['Vue Guide', 'React Handbook'])

const publishedBooks = computed(() => {
  return books.value.filter(book => book.includes('Guide'))
})

function addBook() {
  // BAD: Mutating computed value - change will be lost!
  publishedBooks.value.push('New Book')
}

// BAD: Mutating computed array
const sortedBooks = computed(() => books.value.filter(b => b))

function reverseBooks() {
  // BAD: This mutates the computed snapshot
  sortedBooks.value.reverse()
}
</script>
```

```vue
<script>
export default {
  data() {
    return {
      author: {
        name: 'John',
        books: ['Book A', 'Book B']
      }
    }
  },
  computed: {
    authorBooks() {
      return this.author.books
    }
  },
  methods: {
    addBook() {
      // BAD: Mutating computed value
      this.authorBooks.push('New Book')
    }
  }
}
</script>
```

**Correct:**
```vue
<script setup>
import { ref, computed } from 'vue'

const books = ref(['Vue Guide', 'React Handbook'])

const publishedBooks = computed(() => {
  return books.value.filter(book => book.includes('Guide'))
})

function addBook(bookName) {
  // GOOD: Update the source state
  books.value.push(bookName)
}

// GOOD: Create a copy before mutating for display
const sortedBooks = computed(() => {
  return [...books.value].sort()  // Spread to create copy before sort
})

const reversedBooks = computed(() => {
  return [...books.value].reverse()  // Spread to create copy before reverse
})
</script>
```

```vue
<script>
export default {
  data() {
    return {
      author: {
        name: 'John',
        books: ['Book A', 'Book B']
      }
    }
  },
  computed: {
    authorBooks() {
      return this.author.books
    }
  },
  methods: {
    addBook(bookName) {
      // GOOD: Update source state
      this.author.books.push(bookName)
    }
  }
}
</script>
```

## Writable Computed for Bidirectional Binding

If you genuinely need to "set" a computed value, use a writable computed property:

```vue
<script setup>
import { ref, computed } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

// Writable computed with getter and setter
const fullName = computed({
  get() {
    return `${firstName.value} ${lastName.value}`
  },
  set(newValue) {
    // Update source state based on the new value
    const parts = newValue.split(' ')
    firstName.value = parts[0] || ''
    lastName.value = parts[1] || ''
  }
})

// Now this is valid:
fullName.value = 'Jane Smith'  // Updates firstName and lastName
</script>
```

## Reference
- [Vue.js Computed Properties - Avoid Mutating Computed Value](https://vuejs.org/guide/essentials/computed.html#avoid-mutating-computed-value)
- [Vue.js Computed Properties - Writable Computed](https://vuejs.org/guide/essentials/computed.html#writable-computed)
```

## File: `skills/vue-debug-guides/reference/configure-app-before-mount.md`
```markdown
---
title: Configure Vue App Before Calling mount()
impact: HIGH
impactDescription: App configurations after mount() are silently ignored, causing missing plugins and handlers
type: capability
tags: [vue3, createApp, mount, configuration, setup]
---

# Configure Vue App Before Calling mount()

**Impact: HIGH** - Any app configurations applied after `.mount()` is called are silently ignored. This includes error handlers, global components, directives, and plugins, leading to mysterious missing functionality.

The `.mount()` method should always be called after all app configurations and asset registrations are done. This is a critical ordering requirement that, when violated, produces no errors but causes features to silently fail.

## Task Checklist

- [ ] Register all plugins (router, store, etc.) before mount()
- [ ] Configure error handlers before mount()
- [ ] Register global components and directives before mount()
- [ ] Set all `app.config` properties before mount()
- [ ] Call `.mount()` as the final step in app initialization

**Incorrect:**
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

// WRONG: Mounting first, then configuring
app.mount('#app')

// These are silently IGNORED - app is already mounted!
app.use(router)
app.config.errorHandler = (err) => {
  console.error('Global error:', err)
}
app.component('GlobalButton', GlobalButton)
```

**Correct:**
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import GlobalButton from './components/GlobalButton.vue'

const app = createApp(App)

// Configure everything FIRST
app.use(router)
app.use(createPinia())

// Set up error handling
app.config.errorHandler = (err, instance, info) => {
  console.error('Global error:', err)
  console.log('Component:', instance)
  console.log('Error info:', info)
}

// Register global components
app.component('GlobalButton', GlobalButton)

// Mount LAST - after all configuration is complete
app.mount('#app')
```

## Common Mistake: Chaining with Mount

```javascript
// WRONG: Chaining mount in the middle of configuration
createApp(App)
  .use(router)
  .mount('#app')  // Everything after this line is a problem
  .use(pinia)     // This doesn't even work - mount returns component instance!

// CORRECT: Either complete chain before mount, or use intermediate variable
createApp(App)
  .use(router)
  .use(pinia)
  .component('GlobalButton', GlobalButton)
  .mount('#app')  // Mount at the very end
```

## Reference
- [Vue.js - Creating a Vue Application](https://vuejs.org/guide/essentials/application.html)
- [Vue.js Application API](https://vuejs.org/api/application.html)
```

## File: `skills/vue-debug-guides/reference/declare-emits-for-documentation.md`
```markdown
---
title: Always Declare Emits for Documentation and Validation
impact: MEDIUM
impactDescription: Undeclared emits cause warnings, break TypeScript inference, and prevent event validation
type: best-practice
tags: [vue3, emits, defineEmits, component-events, typescript, documentation]
---

# Always Declare Emits for Documentation and Validation

**Impact: MEDIUM** - Declaring emitted events with `defineEmits()` or the `emits` option is technically optional, but strongly recommended. Without declarations, Vue shows runtime warnings, TypeScript can't infer event types, and you lose the ability to validate event payloads.

Declared emits also serve as self-documentation, making it immediately clear what events a component can emit.

## Task Checklist

- [ ] Use `defineEmits()` in `<script setup>` to declare all events
- [ ] Use `emits` option when not using `<script setup>`
- [ ] Add TypeScript types for event payloads
- [ ] Consider adding validation functions for complex payloads
- [ ] Document the purpose of each event

## The Warning

When you emit without declaring:

```vue
<script setup>
// No defineEmits declaration
function handleClick() {
  emit('select', item) // Vue warns in dev mode
}
</script>
```

Vue warns:
```
[Vue warn]: Component emitted event "select" but it is neither declared
in the emits option nor as an "onSelect" prop.
```

## Basic Declaration

**Correct - Array syntax:**
```vue
<script setup>
const emit = defineEmits(['submit', 'cancel', 'update'])

function handleSubmit() {
  emit('submit', formData)
}

function handleCancel() {
  emit('cancel')
}
</script>
```

**Correct - Options API:**
```js
export default {
  emits: ['submit', 'cancel', 'update'],

  methods: {
    handleSubmit() {
      this.$emit('submit', this.formData)
    }
  }
}
```

## TypeScript Typed Emits

**Correct - Type-based declaration (recommended for TypeScript):**
```vue
<script setup lang="ts">
interface User {
  id: number
  name: string
}

const emit = defineEmits<{
  submit: [data: FormData]
  cancel: []
  'update:modelValue': [value: string]
  select: [user: User, index: number]
}>()

// Now TypeScript enforces correct payloads
emit('submit', formData) // OK
emit('submit') // Error: Expected 1 argument
emit('select', user) // Error: Expected 2 arguments
emit('unknown') // Error: Unknown event
</script>
```

**Alternative syntax (Vue 3.3+):**
```vue
<script setup lang="ts">
const emit = defineEmits<{
  (e: 'submit', data: FormData): void
  (e: 'cancel'): void
  (e: 'update:modelValue', value: string): void
}>()
</script>
```

## Event Validation

You can validate event payloads at runtime:

**Correct - Validation functions:**
```vue
<script setup>
const emit = defineEmits({
  // No validation, just declaration
  cancel: null,

  // Validate payload
  submit: (payload) => {
    if (!payload.email) {
      console.warn('Submit event requires email')
      return false
    }
    return true
  },

  // Validate with type checking
  click: (id) => typeof id === 'number'
})
</script>
```

Returning `false` from a validator logs a console warning but doesn't prevent the event from being emitted.

## Benefits of Declaring Emits

### 1. Fallthrough Attribute Separation

Without declaration, native event listeners fall through to the root element:

```vue
<!-- ParentComponent.vue -->
<ChildComponent @click="handleClick" />
```

```vue
<!-- ChildComponent.vue - WITHOUT emits declaration -->
<template>
  <!-- Native click listener falls through to button -->
  <button>Click me</button>
</template>
```

With declaration, Vue knows it's a component event:

```vue
<script setup>
// Now Vue knows 'click' is a component event, not native
const emit = defineEmits(['click'])
</script>
```

### 2. Self-Documentation

```vue
<script setup>
// Clear contract: this component emits these events
const emit = defineEmits<{
  'row-click': [row: TableRow]
  'row-select': [row: TableRow, selected: boolean]
  'page-change': [page: number]
  'sort-change': [column: string, direction: 'asc' | 'desc']
}>()
</script>
```

### 3. IDE Support

With declarations, your IDE can:
- Autocomplete event names when using the component
- Show event payload types
- Warn about typos in event names
- Navigate to event definitions

## $emit in Template vs emit in Script

```vue
<script setup>
// $emit is available in template, but...
// emit() is needed in <script setup>
const emit = defineEmits(['submit'])

function handleSubmit() {
  // $emit doesn't work here - use emit()
  emit('submit', data)
}
</script>

<template>
  <!-- $emit works in template -->
  <button @click="$emit('submit', data)">Submit</button>

  <!-- Or use the declared emit function -->
  <button @click="emit('submit', data)">Submit</button>
</template>
```

## Reference
- [Vue.js Component Events - Declaring Emitted Events](https://vuejs.org/guide/components/events.html#declaring-emitted-events)
- [Vue.js Component Events - Events Validation](https://vuejs.org/guide/components/events.html#events-validation)
- [Vue 3 Migration - emits Option](https://v3-migration.vuejs.org/breaking-changes/emits-option)
```

## File: `skills/vue-debug-guides/reference/define-expose-before-await.md`
```markdown
---
title: defineExpose Must Be Called Before Any Await
impact: HIGH
impactDescription: Properties exposed after await are inaccessible to parent component refs
type: gotcha
tags: [vue3, script-setup, defineExpose, async, component-refs]
---

# defineExpose Must Be Called Before Any Await

**Impact: HIGH** - In `<script setup>`, if you call `defineExpose()` after an `await` statement, the exposed properties will NOT be accessible to parent components using template refs. This is a subtle async timing issue that causes silent failures.

The compiler transforms top-level await, and code after await runs in a different execution context where defineExpose cannot properly register with the component instance.

## Task Checklist

- [ ] Always call defineExpose() at the top of script setup, before any await
- [ ] If async data is needed in exposed methods, fetch it separately
- [ ] Structure code so expose declarations come first
- [ ] Test parent ref access when using async setup

**Incorrect:**
```vue
<!-- ChildComponent.vue -->
<script setup>
import { ref } from 'vue'

const data = ref(null)
const count = ref(0)

function increment() {
  count.value++
}

// WRONG: await before defineExpose
const response = await fetch('/api/data')
data.value = await response.json()

// BROKEN: This won't work - called after await!
defineExpose({
  count,
  increment,
  data
})
</script>

<template>
  <div>{{ data }}</div>
</template>
```

```vue
<!-- ParentComponent.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import ChildComponent from './ChildComponent.vue'

const childRef = ref(null)

onMounted(() => {
  // FAILS: All exposed properties are undefined!
  console.log(childRef.value.count) // undefined
  childRef.value.increment() // TypeError
})
</script>

<template>
  <Suspense>
    <ChildComponent ref="childRef" />
  </Suspense>
</template>
```

**Correct:**
```vue
<!-- ChildComponent.vue -->
<script setup>
import { ref } from 'vue'

const data = ref(null)
const count = ref(0)

function increment() {
  count.value++
}

// CORRECT: defineExpose BEFORE any await
defineExpose({
  count,
  increment,
  data
})

// Now safe to use await
const response = await fetch('/api/data')
data.value = await response.json()
</script>

<template>
  <div>{{ data }}</div>
</template>
```

```vue
<!-- Alternative: Separate async logic from expose -->
<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const loading = ref(true)

function getData() {
  return data.value
}

async function refreshData() {
  loading.value = true
  const response = await fetch('/api/data')
  data.value = await response.json()
  loading.value = false
}

// CORRECT: No await at top level - defineExpose always works
defineExpose({
  data,
  getData,
  refreshData,
  loading
})

// Trigger async load in lifecycle hook instead
onMounted(() => {
  refreshData()
})
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else>{{ data }}</div>
</template>
```

```vue
<!-- If you must use top-level await, define expose first -->
<script setup>
import { ref } from 'vue'

const user = ref(null)
const posts = ref([])

// CORRECT: All expose calls come first
defineExpose({
  user,
  posts,
  refresh: () => loadData()
})

// Now safe to await
async function loadData() {
  const [userRes, postsRes] = await Promise.all([
    fetch('/api/user'),
    fetch('/api/posts')
  ])
  user.value = await userRes.json()
  posts.value = await postsRes.json()
}

// Top-level await after defineExpose is safe
await loadData()
</script>
```

## Why This Happens

Vue's compiler transforms `<script setup>` with top-level await into an async setup function. The component instance context is only available synchronously before the first await. After await, the execution resumes outside that context, making defineExpose ineffective.

```javascript
// What the compiler roughly generates:
async setup() {
  const count = ref(0)

  // Context available here
  await fetch(...)  // Suspends execution

  // Context lost after resuming
  defineExpose({ count }) // Too late!
}
```

## Reference
- [Vue.js Script Setup - defineExpose](https://vuejs.org/api/sfc-script-setup.html#defineexpose)
- [Vue.js Async Components](https://vuejs.org/guide/components/async.html)
```

## File: `skills/vue-debug-guides/reference/define-model-default-value-sync.md`
```markdown
---
title: defineModel Default Value Can Cause Parent-Child Desync
impact: HIGH
impactDescription: Default values in defineModel don't sync back to parent, causing state inconsistency
type: capability
tags: [vue3, v-model, defineModel, components, props, two-way-binding]
---

# defineModel Default Value Can Cause Parent-Child Desync

**Impact: HIGH** - When using `defineModel()` with a default value and the parent doesn't provide a value, the parent and child components will have different values. The parent's ref stays `undefined` while the child uses the default, breaking the two-way binding contract.

This subtle bug can cause confusing behavior where the parent component shows one value while the child shows another, and updates may not propagate correctly.

## Task Checklist

- [ ] Always provide initial values from the parent when using v-model
- [ ] Don't rely on defineModel defaults as the primary source of truth
- [ ] If defaults are needed, also set them in the parent component
- [ ] Test components with and without v-model props provided

**Problem - Parent and child out of sync:**
```html
<!-- ChildComponent.vue -->
<script setup>
// Default value of 1 if parent doesn't provide value
const model = defineModel({ default: 1 })
</script>

<template>
  <input v-model="model" type="number">
  <!-- Shows: 1 (from default) -->
</template>
```

```html
<!-- ParentComponent.vue -->
<script setup>
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

// PROBLEM: Parent ref is undefined, not synced with child's default
const myValue = ref()  // undefined
</script>

<template>
  <ChildComponent v-model="myValue" />

  <!-- DESYNC: Child shows 1, but parent shows undefined -->
  <p>Parent value: {{ myValue }}</p>  <!-- Shows: undefined -->

  <!-- Even after child changes value, parent may not update correctly -->
</template>
```

**Solution 1 - Always provide initial value from parent:**
```html
<!-- ParentComponent.vue -->
<script setup>
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

// CORRECT: Parent provides the initial value
const myValue = ref(1)  // Match the expected default
</script>

<template>
  <ChildComponent v-model="myValue" />
  <p>Parent value: {{ myValue }}</p>  <!-- Shows: 1, stays in sync -->
</template>
```

**Solution 2 - Child emits default on mount (if parent control not possible):**
```html
<!-- ChildComponent.vue -->
<script setup>
import { onMounted } from 'vue'

const model = defineModel({ default: 1 })

// Sync default value back to parent on mount
onMounted(() => {
  if (model.value === 1) {  // Is using default
    // Force emit to sync parent
    model.value = 1
  }
})
</script>

<template>
  <input v-model="model" type="number">
</template>
```

**Solution 3 - Use required prop or explicit undefined handling:**
```html
<!-- ChildComponent.vue -->
<script setup>
import { computed } from 'vue'

// Mark as required - TypeScript will warn if not provided
const model = defineModel({ required: true })

// Or handle undefined explicitly
const safeModel = computed({
  get: () => model.value ?? 1,  // Provide fallback
  set: (val) => { model.value = val }
})
</script>

<template>
  <input v-model="safeModel" type="number">
</template>
```

**Best Practice - Document expected initial values:**
```html
<!-- ChildComponent.vue -->
<script setup>
/**
 * @prop modelValue - The numeric value (parent should initialize to 1 or desired default)
 */
const model = defineModel({
  type: Number,
  default: 1,
  // Adding validator helps catch issues in development
  validator: (value) => {
    if (value === undefined) {
      console.warn('ChildComponent: v-model value is undefined. Provide initial value from parent.')
    }
    return true
  }
})
</script>
```

## Reference
- [Vue.js Component v-model](https://vuejs.org/guide/components/v-model.html)
- [Vue School - defineModel Guide](https://vueschool.io/articles/vuejs-tutorials/v-model-and-definemodel-a-comprehensive-guide-to-two-way-binding-in-vue-js-3/)
```

## File: `skills/vue-debug-guides/reference/defineEmits-must-be-top-level.md`
```markdown
---
title: defineEmits Must Be Used at Top Level of script setup
impact: HIGH
impactDescription: Using defineEmits inside functions causes compilation errors - macros must be at module scope
type: gotcha
tags: [vue3, defineEmits, script-setup, macros, composition-api]
---

# defineEmits Must Be Used at Top Level of script setup

**Impact: HIGH** - The `defineEmits()` macro can only be used directly within `<script setup>` at the top level. It cannot be placed inside functions, conditionals, or any other nested scope. Vue's compiler hoists these macros to module scope during compilation.

This applies to all Vue macros: `defineProps`, `defineEmits`, `defineExpose`, `defineOptions`, and `defineSlots`.

## Task Checklist

- [ ] Place `defineEmits()` directly in `<script setup>`, not inside functions
- [ ] Do not wrap macro calls in conditionals or loops
- [ ] Do not reference local variables in macro arguments
- [ ] Store the emit function and reuse it throughout the component

## The Problem

**Incorrect - Inside a function:**
```vue
<script setup>
function useEvents() {
  // ERROR: defineEmits cannot be used inside a function
  const emit = defineEmits(['submit', 'cancel'])
  return emit
}

const emit = useEvents() // This fails at compile time
</script>
```

**Incorrect - Inside a conditional:**
```vue
<script setup>
if (someCondition) {
  // ERROR: Cannot use defineEmits in conditional
  const emit = defineEmits(['eventA'])
} else {
  const emit = defineEmits(['eventB'])
}
</script>
```

**Incorrect - Referencing local variables:**
```vue
<script setup>
const eventNames = ['submit', 'cancel']

// ERROR: Cannot reference local variables
const emit = defineEmits(eventNames)
</script>
```

## Correct Usage

**Correct - Top level declaration:**
```vue
<script setup>
// CORRECT: defineEmits at top level of script setup
const emit = defineEmits(['submit', 'cancel', 'update'])

function handleSubmit() {
  emit('submit', data)
}

function handleCancel() {
  emit('cancel')
}
</script>
```

**Correct - With TypeScript types:**
```vue
<script setup lang="ts">
// CORRECT: Type-based declaration at top level
const emit = defineEmits<{
  submit: [data: FormData]
  cancel: []
  'update:modelValue': [value: string]
}>()

function handleSubmit(data: FormData) {
  emit('submit', data)
}
</script>
```

**Correct - Using constant arrays (compile-time constant):**
```vue
<script setup>
// CORRECT: Literal array is fine
const emit = defineEmits(['submit', 'cancel'])
</script>
```

## Why This Restriction Exists

Vue's compiler processes `<script setup>` macros at compile time, not runtime. The arguments must be statically analyzable so Vue can:

1. Generate the correct component options
2. Provide TypeScript type inference
3. Enable IDE support for event autocompletion
4. Validate emitted events

Since the macro is hoisted out of `<script setup>` during compilation, it cannot access anything that only exists at runtime.

## Using emit in Composables

If you want to share emit logic in a composable, pass the emit function as an argument:

**Correct - Pass emit to composable:**
```vue
<script setup>
const emit = defineEmits(['submit', 'cancel', 'validate'])

// Pass emit to composable
const { handleSubmit, handleCancel } = useFormEvents(emit)
</script>
```

```js
// composables/useFormEvents.js
export function useFormEvents(emit) {
  function handleSubmit(data) {
    emit('submit', data)
  }

  function handleCancel() {
    emit('cancel')
  }

  return { handleSubmit, handleCancel }
}
```

## ESLint Rule

The `eslint-plugin-vue` provides the `vue/valid-define-emits` rule that catches these errors:

```js
// eslint.config.js
export default [
  {
    rules: {
      'vue/valid-define-emits': 'error'
    }
  }
]
```

This rule reports:
- `defineEmits` used inside functions
- `defineEmits` referencing local variables
- Multiple `defineEmits` calls in the same component
- `defineEmits` used outside `<script setup>`

## Reference
- [Vue.js SFC script setup](https://vuejs.org/api/sfc-script-setup.html#defineprops-defineemits)
- [ESLint vue/valid-define-emits](https://eslint.vuejs.org/rules/valid-define-emits)
```

## File: `skills/vue-debug-guides/reference/defineEmits-no-runtime-and-type-mixed.md`
```markdown
---
title: Cannot Mix Runtime and Type Declarations in defineEmits
impact: HIGH
impactDescription: Using both array/object syntax AND TypeScript generics in defineEmits causes compile errors
type: gotcha
tags: [vue3, defineEmits, typescript, compilation-error, script-setup]
---

# Cannot Mix Runtime and Type Declarations in defineEmits

**Impact: HIGH** - `defineEmits` supports two declaration styles: runtime (array/object syntax) and type-based (TypeScript generics). You CANNOT use both at the same time. Attempting to do so results in a compile-time error.

This is a common mistake when learning Vue 3 with TypeScript.

## Task Checklist

- [ ] Choose ONE declaration style: runtime OR type-based
- [ ] For TypeScript projects, prefer type-based declaration
- [ ] For JavaScript projects, use runtime (array/object) declaration
- [ ] Never pass arguments when using generic type parameter

## The Problem

**Incorrect - Mixing both styles:**
```vue
<script setup lang="ts">
// ERROR: Cannot use both type argument and runtime argument
const emit = defineEmits<{
  submit: [data: FormData]
}>(['submit'])  // This array argument causes the error!
</script>
```

**Compiler error:**
```
defineEmits() cannot accept both type and non-type arguments at the same time.
Use one or the other.
```

**Also incorrect:**
```vue
<script setup lang="ts">
// ERROR: Same problem with object syntax
const emit = defineEmits<{
  submit: [data: FormData]
}>({
  submit: (data) => !!data
})
</script>
```

## Correct: Type-Based Declaration (TypeScript)

```vue
<script setup lang="ts">
// CORRECT: Type argument only, no runtime argument
const emit = defineEmits<{
  submit: [data: FormData]
  cancel: []
  'update:modelValue': [value: string]
}>()

emit('submit', formData)  // TypeScript validates this
emit('cancel')
emit('unknown')  // TypeScript error: unknown event
</script>
```

**Alternative call signature syntax:**
```vue
<script setup lang="ts">
const emit = defineEmits<{
  (e: 'submit', data: FormData): void
  (e: 'cancel'): void
  (e: 'update:modelValue', value: string): void
}>()
</script>
```

## Correct: Runtime Declaration (JavaScript or Simple Cases)

**Array syntax:**
```vue
<script setup>
// CORRECT: Runtime array, no type argument
const emit = defineEmits(['submit', 'cancel', 'update:modelValue'])

emit('submit', formData)
emit('cancel')
</script>
```

**Object syntax with validation:**
```vue
<script setup>
// CORRECT: Runtime object for validation
const emit = defineEmits({
  submit: (data) => {
    if (!data?.email) {
      console.warn('Missing email')
      return false
    }
    return true
  },
  cancel: null  // No validation
})
</script>
```

## Adding Validation to Type-Based Emits

If you want TypeScript types AND runtime validation, define the validator separately:

```vue
<script setup lang="ts">
interface FormData {
  email: string
  message: string
}

// Type-based declaration for TypeScript
const emit = defineEmits<{
  submit: [data: FormData]
}>()

// Separate validation function
function emitSubmit(data: FormData) {
  if (!data.email.includes('@')) {
    console.warn('Invalid email format')
    return
  }
  emit('submit', data)
}
</script>

<template>
  <button @click="emitSubmit(formData)">Submit</button>
</template>
```

## Choosing Between Styles

| Style | Use When | Benefits |
|-------|----------|----------|
| Type-based | TypeScript project | Compile-time checking, IDE support |
| Array | JavaScript, simple events | Simple, no types needed |
| Object | Need runtime validation | Validates payloads at runtime |

**Recommendation:** In TypeScript projects, use type-based declaration. It provides the best developer experience with autocompletion and type checking.

## Same Rule Applies to defineProps

This restriction also applies to `defineProps`:

```vue
<script setup lang="ts">
// ERROR: Cannot mix
const props = defineProps<{ name: string }>({ name: String })

// CORRECT: Type-based only
const props = defineProps<{ name: string }>()

// CORRECT: Runtime only
const props = defineProps({ name: String })
</script>
```

## Reference
- [Vue.js SFC script setup - defineEmits](https://vuejs.org/api/sfc-script-setup.html#defineprops-defineemits)
- [Vue.js TypeScript with Composition API](https://vuejs.org/guide/typescript/composition-api.html#typing-component-emits)
```

## File: `skills/vue-debug-guides/reference/definemodel-object-mutation-no-emit.md`
```markdown
---
title: defineModel Object Properties Must Be Replaced, Not Mutated
impact: HIGH
impactDescription: Mutating object properties via defineModel doesn't emit update events, breaking parent sync
type: gotcha
tags: [vue3, v-model, defineModel, objects, reactivity, two-way-binding]
---

# defineModel Object Properties Must Be Replaced, Not Mutated

**Impact: HIGH** - When using `defineModel()` with objects or arrays, directly mutating nested properties like `model.value.prop = x` does NOT emit the `update:modelValue` event. The parent component never receives the change notification, causing silent sync failures.

This happens because Vue only detects when the `model.value` reference itself changes, not when properties of the object are mutated in place.

## Task Checklist

- [ ] Never mutate object properties directly: `model.value.prop = x`
- [ ] Always create a new object reference when updating: `model.value = {...model.value, prop: x}`
- [ ] For arrays, use spread or slice: `model.value = [...model.value, newItem]`
- [ ] Consider using structuredClone for deeply nested objects

**Incorrect - Mutation without event emission:**
```vue
<script setup>
// Child component with object v-model
const model = defineModel<{ name: string; age: number }>()

function updateName(newName: string) {
  // WRONG: This mutates the object in place
  // Parent receives NO update:modelValue event!
  model.value.name = newName
}

function addToList() {
  // WRONG: Push mutates the array
  model.value.items.push('new item')  // Parent not notified
}
</script>
```

**Correct - Replace object reference to trigger event:**
```vue
<script setup>
const model = defineModel<{ name: string; age: number }>()

function updateName(newName: string) {
  // CORRECT: Create new object reference
  // This triggers update:modelValue event to parent
  model.value = {
    ...model.value,
    name: newName
  }
}

function addToList() {
  // CORRECT: Create new array reference
  model.value = {
    ...model.value,
    items: [...model.value.items, 'new item']
  }
}
</script>
```

## Deep Nesting Requires Full Path Replacement

```vue
<script setup>
const model = defineModel<{
  user: {
    address: {
      city: string
    }
  }
}>()

// WRONG: Deep mutation
model.value.user.address.city = 'New York'

// CORRECT: Replace entire chain
model.value = {
  ...model.value,
  user: {
    ...model.value.user,
    address: {
      ...model.value.user.address,
      city: 'New York'
    }
  }
}

// ALTERNATIVE: Use structuredClone for complex updates
function updateCity(city: string) {
  const updated = structuredClone(model.value)
  updated.user.address.city = city
  model.value = updated  // New reference triggers event
}
</script>
```

## Race Condition Warning with Spread Operator

When multiple updates occur rapidly, earlier changes can be lost:

```vue
<script setup>
const model = defineModel<{ a: string; b: string }>()

// CAUTION: Race condition if called in same tick
function updateBothWrong() {
  model.value = { ...model.value, a: 'new-a' }  // First update
  model.value = { ...model.value, b: 'new-b' }  // May use stale model.value!
}

// CORRECT: Batch updates into single assignment
function updateBothCorrect() {
  model.value = {
    ...model.value,
    a: 'new-a',
    b: 'new-b'
  }
}
</script>
```

## Alternative: VueUse's useVModel with Deep Option

For complex objects, consider VueUse:

```vue
<script setup>
import { useVModel } from '@vueuse/core'

const props = defineProps<{ modelValue: { name: string } }>()
const emit = defineEmits(['update:modelValue'])

// Deep tracking with passive updates
const model = useVModel(props, 'modelValue', emit, { deep: true, passive: true })

// Now direct mutations work
model.value.name = 'New Name'  // Properly syncs with parent
</script>
```

## Reference
- [Vue.js Component v-model](https://vuejs.org/guide/components/v-model.html)
- [GitHub Discussion: defineModel with objects](https://github.com/orgs/vuejs/discussions/10538)
- [SIMPL Engineering: Vue defineModel Pitfalls](https://engineering.simpl.de/post/vue_definemodel/)
```

## File: `skills/vue-debug-guides/reference/dom-update-timing-nexttick.md`
```markdown
---
title: Use nextTick() to Wait for DOM Updates
impact: MEDIUM
impactDescription: DOM updates are batched and asynchronous - direct DOM access after state changes sees stale values
type: capability
tags: [vue3, dom, nextTick, reactivity, async]
---

# Use nextTick() to Wait for DOM Updates

**Impact: MEDIUM** - Vue batches DOM updates asynchronously for performance. If you access the DOM immediately after changing reactive state, you'll see the old values. Use `nextTick()` to wait for the DOM to update.

When you modify reactive state, Vue doesn't update the DOM synchronously. Instead, it buffers changes and applies them in the next "tick" of the event loop. This is a performance optimization, but it can cause bugs when you need to read from or manipulate the DOM after state changes.

## Task Checklist

- [ ] Use `await nextTick()` when you need to access updated DOM elements after state changes
- [ ] Use `nextTick()` when measuring DOM elements (heights, widths) after data changes
- [ ] Use `nextTick()` when focusing inputs or scrolling after content updates
- [ ] Consider if you really need DOM access - often you can work with reactive data instead

**Incorrect:**
```javascript
import { ref } from 'vue'

const message = ref('Hello')
const messageEl = ref(null)

function updateMessage() {
  message.value = 'Updated!'

  // WRONG: DOM still shows "Hello" at this point
  console.log(messageEl.value.textContent) // "Hello" - stale!

  // WRONG: Scrolling/focusing may not work correctly
  scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight
}
```

**Correct:**
```javascript
import { ref, nextTick } from 'vue'

const message = ref('Hello')
const messageEl = ref(null)

async function updateMessage() {
  message.value = 'Updated!'

  // CORRECT: Wait for DOM to update
  await nextTick()

  // Now the DOM is updated
  console.log(messageEl.value.textContent) // "Updated!"

  // Scrolling and focusing now work correctly
  scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight
}

// Alternative: callback syntax
function updateWithCallback() {
  message.value = 'Updated!'

  nextTick(() => {
    console.log(messageEl.value.textContent) // "Updated!"
  })
}
```

```vue
<script setup>
import { ref, nextTick } from 'vue'

const items = ref([])
const listRef = ref(null)

async function addItem() {
  items.value.push({ id: Date.now(), text: 'New item' })

  await nextTick()

  // Now we can safely scroll to the new item
  listRef.value.lastElementChild?.scrollIntoView({ behavior: 'smooth' })
}
</script>
```

## Reference
- [Vue.js Reactivity Fundamentals - DOM Update Timing](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#dom-update-timing)
- [Vue.js nextTick API](https://vuejs.org/api/general.html#nexttick)
```

## File: `skills/vue-debug-guides/reference/dynamic-argument-constraints.md`
```markdown
---
title: Dynamic Directive Arguments Have Syntax Constraints
impact: MEDIUM
impactDescription: Invalid dynamic arguments cause silent failures or browser compatibility issues
type: capability
tags: [vue3, template, directives, v-bind, v-on, dynamic-arguments]
---

# Dynamic Directive Arguments Have Syntax Constraints

**Impact: MEDIUM** - Dynamic directive arguments (e.g., `:[attributeName]`, `@[eventName]`) have value and syntax constraints that can cause silent failures. In-DOM templates also have case sensitivity issues with browsers lowercasing attribute names.

Dynamic arguments allow runtime determination of which attribute or event to bind, but they have restrictions that differ from static arguments.

## Task Checklist

- [ ] Ensure dynamic arguments evaluate to strings or `null`
- [ ] Avoid spaces and quotes inside dynamic argument brackets
- [ ] Use computed properties for complex dynamic argument expressions
- [ ] In in-DOM templates, use lowercase attribute names or switch to SFCs
- [ ] Use `null` to explicitly remove a binding

**Incorrect:**
```vue
<template>
  <!-- ERROR: Spaces and quotes not allowed in dynamic arguments -->
  <a :[' foo' + bar]="value">Link</a>
  <a :["data-" + name]="value">Link</a>

  <!-- WARNING: Non-string values (except null) trigger warnings -->
  <a :[123]="value">Link</a>
  <a :[someObject]="value">Link</a>

  <!-- BUG in in-DOM templates: Browsers lowercase attribute names -->
  <!-- This becomes :[someattr] which won't match someAttr -->
  <a :[someAttr]="url">Link</a>
</template>

<script setup>
// If component expects someAttr but browser lowercases to someattr
// the binding silently fails
const someAttr = 'href'
</script>
```

**Correct:**
```vue
<template>
  <!-- OK: Simple variable reference -->
  <a :[attributeName]="url">Link</a>

  <!-- OK: Use computed property for complex expressions -->
  <a :[dynamicAttr]="value">Link</a>

  <!-- OK: null removes the binding -->
  <button :[disabledAttr]="isDisabled">Submit</button>

  <!-- OK: Dynamic event names -->
  <button @[eventName]="handler">Click</button>

  <!-- OK: In SFCs, case is preserved -->
  <a :[someAttr]="url">Link</a>
</template>

<script setup>
import { ref, computed } from 'vue'

// Simple string variable
const attributeName = ref('href')
const url = ref('https://vuejs.org')

// Complex expression via computed property
const prefix = ref('data')
const name = ref('id')
const dynamicAttr = computed(() => `${prefix.value}-${name.value}`)

// Conditional binding with null
const isDisabled = ref(false)
const disabledAttr = computed(() => isDisabled.value ? 'disabled' : null)

// Dynamic events
const useTouch = ref(false)
const eventName = computed(() => useTouch.value ? 'touchstart' : 'click')

function handler() {
  console.log('Event triggered')
}
</script>
```

## In-DOM Template Workaround

When writing templates directly in HTML (not SFCs), use lowercase:

```html
<!-- In-DOM template (index.html) -->
<div id="app">
  <!-- Use lowercase to avoid browser issues -->
  <a :[attrname]="url">Link</a>
</div>

<script type="module">
import { createApp, ref } from 'vue'

createApp({
  setup() {
    // Match the lowercase used in template
    const attrname = ref('href')
    const url = ref('https://vuejs.org')
    return { attrname, url }
  }
}).mount('#app')
</script>
```

## SFC vs In-DOM Templates

| Feature | SFC (.vue files) | In-DOM (HTML) |
|---------|------------------|---------------|
| Case sensitivity | Preserved | Lowercased by browser |
| Dynamic arguments | Full support | Lowercase only |
| Recommendation | Preferred | Use for progressive enhancement |

## Valid Dynamic Argument Values

```vue
<script setup>
// String values - OK
const attr1 = 'href'
const attr2 = 'data-custom'

// null - OK (removes binding)
const attr3 = null

// undefined - OK (removes binding)
const attr4 = undefined

// Numbers, objects, arrays - WARNING
const attr5 = 123        // Warning: should be string
const attr6 = { foo: 1 } // Warning: should be string
</script>
```

## Reference
- [Vue.js Template Syntax - Dynamic Arguments](https://vuejs.org/guide/essentials/template-syntax.html#dynamic-arguments)
- [Vue.js Template Syntax - Dynamic Argument Value Constraints](https://vuejs.org/guide/essentials/template-syntax.html#dynamic-argument-value-constraints)
```

## File: `skills/vue-debug-guides/reference/dynamic-component-registration-vite.md`
```markdown
---
title: Use import.meta.glob for Dynamic Component Registration in Vite
impact: MEDIUM
impactDescription: require.context from Webpack doesn't work in Vite projects
type: gotcha
tags: [vue3, component-registration, vite, dynamic-import, migration, webpack]
---

# Use import.meta.glob for Dynamic Component Registration in Vite

**Impact: MEDIUM** - When migrating from Webpack to Vite or starting a new Vite project, the `require.context` pattern for dynamically registering components won't work. Vite uses `import.meta.glob` instead. Using the wrong approach will cause build errors or runtime failures.

## Task Checklist

- [ ] Replace `require.context` with `import.meta.glob` in Vite projects
- [ ] Update component registration patterns when migrating from Vue CLI to Vite
- [ ] Use `{ eager: true }` for synchronous loading when needed
- [ ] Handle async components appropriately with `defineAsyncComponent`

**Incorrect (Webpack pattern - doesn't work in Vite):**
```javascript
// main.js - WRONG for Vite
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// This Webpack-specific API doesn't exist in Vite
const requireComponent = require.context(
  './components/base',
  false,
  /Base[A-Z]\w+\.vue$/
)

requireComponent.keys().forEach(fileName => {
  const componentConfig = requireComponent(fileName)
  const componentName = fileName
    .split('/')
    .pop()
    .replace(/\.\w+$/, '')

  app.component(componentName, componentConfig.default || componentConfig)
})

app.mount('#app')
```

**Correct (Vite pattern):**
```javascript
// main.js - Correct for Vite
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// Vite's glob import - eager loading for synchronous registration
const modules = import.meta.glob('./components/base/Base*.vue', { eager: true })

for (const path in modules) {
  // Extract component name from path: './components/base/BaseButton.vue' -> 'BaseButton'
  const componentName = path.split('/').pop().replace('.vue', '')
  app.component(componentName, modules[path].default)
}

app.mount('#app')
```

## Lazy Loading with Async Components

```javascript
// main.js - Lazy loading variant
import { createApp, defineAsyncComponent } from 'vue'
import App from './App.vue'

const app = createApp(App)

// Without { eager: true }, returns functions that return Promises
const modules = import.meta.glob('./components/base/Base*.vue')

for (const path in modules) {
  const componentName = path.split('/').pop().replace('.vue', '')
  // Wrap in defineAsyncComponent for lazy loading
  app.component(componentName, defineAsyncComponent(modules[path]))
}

app.mount('#app')
```

## Glob Pattern Examples

```javascript
// All .vue files in a directory (not recursive)
import.meta.glob('./components/*.vue', { eager: true })

// All .vue files recursively
import.meta.glob('./components/**/*.vue', { eager: true })

// Specific naming pattern
import.meta.glob('./components/Base*.vue', { eager: true })

// Multiple patterns
import.meta.glob([
  './components/Base*.vue',
  './components/App*.vue'
], { eager: true })

// Exclude patterns
import.meta.glob('./components/**/*.vue', {
  eager: true,
  ignore: ['**/*.test.vue', '**/*.spec.vue']
})
```

## TypeScript Support

```typescript
// main.ts - with proper typing
import { createApp, Component } from 'vue'
import App from './App.vue'

const app = createApp(App)

const modules = import.meta.glob<{ default: Component }>(
  './components/base/Base*.vue',
  { eager: true }
)

for (const path in modules) {
  const componentName = path.split('/').pop()!.replace('.vue', '')
  app.component(componentName, modules[path].default)
}

app.mount('#app')
```

## Migration Checklist (Webpack to Vite)

| Webpack | Vite |
|---------|------|
| `require.context(dir, recursive, regex)` | `import.meta.glob(pattern, options)` |
| Synchronous by default | Use `{ eager: true }` for sync |
| `.keys()` returns array | Returns object with paths as keys |
| Returns module directly | Access via `.default` for ES modules |

## Reference
- [Vite - Glob Import](https://vitejs.dev/guide/features.html#glob-import)
- [Vue.js Component Registration](https://vuejs.org/guide/components/registration.html)
```

## File: `skills/vue-debug-guides/reference/event-modifier-order-matters.md`
```markdown
---
title: Event Modifier Order Matters
impact: MEDIUM
impactDescription: Modifier order affects event handling behavior - wrong order causes unexpected propagation or prevention
type: gotcha
tags: [vue3, events, modifiers, v-on, click, form]
---

# Event Modifier Order Matters

**Impact: MEDIUM** - When chaining event modifiers, the order determines behavior because Vue generates code in the same sequence. Using `.prevent.self` vs `.self.prevent` produces different results that can cause subtle bugs in event handling.

## Task Checklist

- [ ] Always consider modifier order when chaining multiple modifiers
- [ ] Use `.prevent.self` to prevent default on element AND children
- [ ] Use `.self.prevent` to prevent default ONLY on the element itself
- [ ] Test event behavior on both the element and its children

**Incorrect:**
```html
<!-- WRONG: Unintended behavior - prevents clicks on children too -->
<template>
  <div @click.prevent.self="handleClick">
    <button>Child Button</button> <!-- Default also prevented here! -->
  </div>
</template>
```

```html
<!-- WRONG: Assuming order doesn't matter -->
<template>
  <!-- Developer expects only self clicks to be handled -->
  <!-- But .prevent runs first, affecting all clicks -->
  <a href="/page" @click.prevent.self="navigate">
    <span>Click me</span>
  </a>
</template>
```

**Correct:**
```html
<!-- CORRECT: Only prevent default on the element itself -->
<template>
  <div @click.self.prevent="handleClick">
    <button>Child Button</button> <!-- Default NOT prevented here -->
  </div>
</template>
```

```html
<!-- CORRECT: Prevent default on element and children -->
<template>
  <form @submit.prevent.self="onSubmit">
    <button type="submit">Submit</button>
  </form>
</template>
```

```html
<!-- CORRECT: Explicit intent with separate handlers when needed -->
<template>
  <div @click.self="handleSelfClick">
    <button @click.prevent="handleChildClick">
      Child with prevented default
    </button>
  </div>
</template>
```

## How Modifier Order Works

```javascript
// Vue compiles modifiers in order, so:

// @click.prevent.self compiles to:
// event.preventDefault()
// if (event.target !== event.currentTarget) return
// handler()

// @click.self.prevent compiles to:
// if (event.target !== event.currentTarget) return
// event.preventDefault()
// handler()
```

## Common Modifier Combinations

```html
<!-- Stop propagation AND prevent default -->
<a @click.stop.prevent="handleClick">Link</a>

<!-- Capture mode with once -->
<div @click.capture.once="handleOnce">...</div>

<!-- Only exact modifier key combination -->
<button @click.ctrl.exact="onCtrlClick">Ctrl+Click Only</button>
```

## Reference
- [Vue.js Event Handling - Event Modifiers](https://vuejs.org/guide/essentials/event-handling.html#event-modifiers)
```

## File: `skills/vue-debug-guides/reference/exact-modifier-for-precise-shortcuts.md`
```markdown
---
title: Use .exact Modifier for Precise Keyboard/Mouse Shortcuts
impact: MEDIUM
impactDescription: Without .exact, shortcuts fire even when additional modifier keys are pressed, causing unintended behavior
type: best-practice
tags: [vue3, events, keyboard, modifiers, shortcuts, accessibility]
---

# Use .exact Modifier for Precise Keyboard/Mouse Shortcuts

**Impact: MEDIUM** - By default, Vue's modifier key handlers (`.ctrl`, `.alt`, `.shift`, `.meta`) fire even when other modifier keys are also pressed. Use `.exact` to require that ONLY the specified modifiers are pressed, preventing accidental triggering of shortcuts.

## Task Checklist

- [ ] Use `.exact` when you need precise modifier combinations
- [ ] Without `.exact`: `@click.ctrl` fires for Ctrl+Click AND Ctrl+Shift+Click
- [ ] With `.exact`: `@click.ctrl.exact` fires ONLY for Ctrl+Click
- [ ] Use `@click.exact` for plain clicks with no modifiers

**Incorrect:**
```html
<!-- WRONG: Fires even with additional modifiers -->
<template>
  <button @click.ctrl="copyItem">Copy</button>
  <!-- Also fires on Ctrl+Shift+Click, Ctrl+Alt+Click, etc. -->

  <button @click.ctrl.shift="copyAll">Copy All</button>
  <!-- User expects Ctrl+Shift, but also fires on Ctrl+Shift+Alt -->
</template>
```

```html
<!-- WRONG: Conflicting shortcuts without .exact -->
<template>
  <div>
    <button @click.ctrl="copy">Copy (Ctrl+Click)</button>
    <button @click.ctrl.shift="copyAll">Copy All (Ctrl+Shift+Click)</button>
    <!-- Both fire when user does Ctrl+Shift+Click! -->
  </div>
</template>
```

**Correct:**
```html
<!-- CORRECT: Precise modifier matching with .exact -->
<template>
  <button @click.ctrl.exact="copyItem">Copy (Ctrl only)</button>
  <!-- Only fires on Ctrl+Click, not Ctrl+Shift+Click -->

  <button @click.ctrl.shift.exact="copyAll">Copy All (Ctrl+Shift only)</button>
  <!-- Only fires on Ctrl+Shift+Click, not Ctrl+Shift+Alt+Click -->
</template>
```

```html
<!-- CORRECT: Plain click without any modifiers -->
<template>
  <button @click.exact="selectItem">Select</button>
  <!-- Only fires when NO modifier keys are pressed -->
  <!-- Ctrl+Click, Shift+Click, etc. will NOT trigger this -->
</template>
```

```html
<!-- CORRECT: Non-conflicting shortcuts -->
<template>
  <div class="editor">
    <div
      @click.exact="selectItem"
      @click.ctrl.exact="addToSelection"
      @click.shift.exact="extendSelection"
      @click.ctrl.shift.exact="selectRange"
    >
      Click, Ctrl+Click, Shift+Click, or Ctrl+Shift+Click
    </div>
  </div>
</template>
```

## Behavior Comparison

```javascript
// WITHOUT .exact
@click.ctrl="handler"
// Fires when: Ctrl+Click, Ctrl+Shift+Click, Ctrl+Alt+Click, Ctrl+Shift+Alt+Click
// Does NOT fire: Click (without Ctrl)

// WITH .exact
@click.ctrl.exact="handler"
// Fires when: ONLY Ctrl+Click
// Does NOT fire: Ctrl+Shift+Click, Ctrl+Alt+Click, Click

// ONLY .exact (no other modifiers)
@click.exact="handler"
// Fires when: Plain click with NO modifiers
// Does NOT fire: Ctrl+Click, Shift+Click, Alt+Click
```

## Practical Example: File Browser Selection

```vue
<template>
  <ul class="file-list">
    <li
      v-for="file in files"
      :key="file.id"
      @click.exact="selectSingle(file)"
      @click.ctrl.exact="toggleSelection(file)"
      @click.shift.exact="selectRange(file)"
      @click.ctrl.shift.exact="addRangeToSelection(file)"
      :class="{ selected: isSelected(file) }"
    >
      {{ file.name }}
    </li>
  </ul>
</template>

<script setup>
// Each click type has distinct, non-overlapping behavior
function selectSingle(file) {
  // Clear selection and select only this file
}

function toggleSelection(file) {
  // Add or remove this file from current selection
}

function selectRange(file) {
  // Select all files from last selected to this one
}

function addRangeToSelection(file) {
  // Add range to existing selection
}
</script>
```

## Keyboard Shortcuts with .exact

```html
<template>
  <div
    tabindex="0"
    @keydown.ctrl.s.exact.prevent="save"
    @keydown.ctrl.shift.s.exact.prevent="saveAs"
    @keydown.ctrl.z.exact.prevent="undo"
    @keydown.ctrl.shift.z.exact.prevent="redo"
  >
    <!-- Each shortcut is precisely defined -->
  </div>
</template>
```

## Reference
- [Vue.js Event Handling - .exact Modifier](https://vuejs.org/guide/essentials/event-handling.html#exact-modifier)
```

## File: `skills/vue-debug-guides/reference/fallthrough-attrs-overwrite-vue3.md`
```markdown
# Fallthrough Attributes Overwrite Explicit Attributes in Vue 3

## Rule

In Vue 3, fallthrough attributes overwrite explicitly set attributes on the root element (except `class` and `style` which are merged). This is a breaking change from Vue 2. To preserve explicit attribute values, use `inheritAttrs: false` and manually bind `$attrs` before the explicit attribute.

## Why This Matters

- Silent behavior change from Vue 2 to Vue 3
- Can cause unexpected attribute values in migrated codebases
- Only `class` and `style` merge intelligently; other attributes are overwritten
- Affects component composition patterns and wrapper components

## Bad Code

```vue
<!-- Parent.vue -->
<template>
  <Child msg="Passed from Parent" />
</template>

<!-- Child.vue - UNEXPECTED BEHAVIOR -->
<template>
  <GrandChild msg="Set in Child" />
</template>

<!--
  Vue 3 Result: GrandChild receives msg="Passed from Parent"
  The fallthrough attribute OVERWRITES the explicit one!

  Vue 2 Result: GrandChild receives msg="Set in Child"
  The explicit attribute took precedence
-->
```

### Another common case with data attributes

```vue
<!-- Parent.vue -->
<template>
  <Button data-testid="parent-button" />
</template>

<!-- Button.vue - WRONG: explicit data-testid is overwritten -->
<template>
  <button data-testid="submit-btn">Submit</button>
</template>

<!-- Result: <button data-testid="parent-button">Submit</button> -->
<!-- The component's intended test ID is lost! -->
```

## Good Code

### Option 1: Control attribute order with inheritAttrs: false

```vue
<!-- Child.vue - CORRECT: Control attribute precedence -->
<script setup>
defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <!-- v-bind="$attrs" FIRST, then explicit attribute -->
  <GrandChild v-bind="$attrs" msg="Set in Child" />
</template>

<!--
  Result: GrandChild receives msg="Set in Child"
  Explicit attribute overrides fallthrough because it comes last
-->
```

### Option 2: Exclude specific attrs from fallthrough

```vue
<script setup>
import { computed, useAttrs } from 'vue'

defineOptions({
  inheritAttrs: false
})

const attrs = useAttrs()

// Filter out attributes you want to control explicitly
const filteredAttrs = computed(() => {
  const { msg, ...rest } = attrs
  return rest
})
</script>

<template>
  <GrandChild v-bind="filteredAttrs" msg="Set in Child" />
</template>
```

### Option 3: For wrapper components, declare as prop

```vue
<!-- Button.vue - BEST: Declare attributes you need to control -->
<script setup>
const props = defineProps({
  dataTestid: {
    type: String,
    default: 'submit-btn'
  }
})

defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <button :data-testid="dataTestid" v-bind="$attrs">
    <slot />
  </button>
</template>
```

## Class and Style Are Special

Unlike other attributes, `class` and `style` merge rather than overwrite:

```vue
<!-- Parent.vue -->
<template>
  <Button class="large" style="color: red" />
</template>

<!-- Button.vue -->
<template>
  <button class="btn" style="padding: 10px">Submit</button>
</template>

<!--
  Result: <button class="btn large" style="padding: 10px; color: red">
  Both classes and styles are MERGED, not overwritten
-->
```

## Vue 2 to Vue 3 Migration Checklist

When migrating components that rely on attribute precedence:

1. Identify components that set explicit attributes on root elements
2. Check if parent components pass the same attributes
3. If explicit values should take precedence:
   - Add `inheritAttrs: false`
   - Use `v-bind="$attrs"` before explicit attributes

## References

- [Fallthrough Attributes](https://vuejs.org/guide/components/attrs.html)
- [Vue 3 Migration Guide - Attribute Coercion Behavior](https://v3-migration.vuejs.org/breaking-changes/)
- [Vue Fallthrough Attributes behaviour changes from Vue 2 to Vue 3](https://lukes.tips/posts/vue-3-fallthough-attributes-changes/)
```

## File: `skills/vue-debug-guides/reference/in-dom-template-parsing-caveats.md`
```markdown
---
title: In-DOM Template Parsing Caveats
impact: HIGH
impactDescription: Browser HTML parsing before Vue compilation causes case sensitivity, self-closing tag, and element nesting issues
type: gotcha
tags: [vue3, templates, in-dom, html-parsing, kebab-case, self-closing-tags]
---

# In-DOM Template Parsing Caveats

**Impact: HIGH** - When writing Vue templates directly in the DOM (not in `.vue` files), the browser's native HTML parser processes the template BEFORE Vue sees it. This causes three critical issues: case sensitivity problems, self-closing tag failures, and element placement restrictions.

These issues do NOT apply to Single-File Components (SFCs) or string templates where Vue's compiler handles parsing directly.

## Task Checklist

- [ ] Use kebab-case for component names in in-DOM templates
- [ ] Use kebab-case for prop names in in-DOM templates
- [ ] Use explicit closing tags (not self-closing) in in-DOM templates
- [ ] Use `is="vue:component-name"` for components inside restricted elements
- [ ] Prefer SFCs to avoid all in-DOM parsing issues

## Issue 1: Case Insensitivity

HTML is case-insensitive. The browser lowercases everything before Vue sees it.

**Incorrect (in-DOM template):**
```html
<!-- Browser converts to: <blogpost posttitle="hello"> -->
<BlogPost postTitle="hello" @updatePost="onUpdate"></BlogPost>
```

**Correct (in-DOM template):**
```html
<!-- Use kebab-case for everything -->
<blog-post post-title="hello" @update-post="onUpdate"></blog-post>
```

**In SFCs, PascalCase works fine:**
```vue
<!-- BlogPost.vue - PascalCase recommended -->
<template>
  <BlogPost postTitle="hello" @updatePost="onUpdate" />
</template>
```

## Issue 2: Self-Closing Tags Fail

HTML only allows self-closing syntax for void elements (`<input>`, `<img>`, etc.). For all others, the browser expects closing tags.

**Incorrect (in-DOM template):**
```html
<!-- Browser thinks the tag never closed, breaks nesting -->
<my-component />
<another-component />
```

**Correct (in-DOM template):**
```html
<!-- Explicit closing tags required -->
<my-component></my-component>
<another-component></another-component>
```

**In SFCs, self-closing works fine:**
```vue
<template>
  <MyComponent />
  <AnotherComponent />
</template>
```

## Issue 3: Element Placement Restrictions

Some HTML elements have strict rules about valid children. Invalid elements are hoisted out by the browser before Vue sees the template.

**Restricted parent elements:**
- `<ul>`, `<ol>` - only allow `<li>`
- `<table>` - only allows `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<caption>`, `<colgroup>`
- `<tr>` - only allows `<td>`, `<th>`
- `<select>` - only allows `<option>`, `<optgroup>`

**Incorrect (in-DOM template):**
```html
<!-- Browser hoists blog-post-row outside the table -->
<table>
  <blog-post-row v-for="post in posts" :post="post"></blog-post-row>
</table>

<!-- Renders as: -->
<blog-post-row></blog-post-row>
<blog-post-row></blog-post-row>
<table></table>
```

**Correct (in-DOM template):**
```html
<!-- Use is="vue:component-name" on a valid native element -->
<table>
  <tr is="vue:blog-post-row" v-for="post in posts" :key="post.id" :post="post"></tr>
</table>
```

```html
<ul>
  <li is="vue:todo-item" v-for="todo in todos" :key="todo.id" :todo="todo"></li>
</ul>
```

**Important:** The `vue:` prefix is required! Without it, `is` is treated as a native customized built-in element attribute.

```html
<!-- WRONG: Missing vue: prefix -->
<tr is="blog-post-row"></tr>

<!-- CORRECT: With vue: prefix -->
<tr is="vue:blog-post-row"></tr>
```

## When Do These Apply?

| Template Type | Affected? | Example |
|---------------|-----------|---------|
| Single-File Component (`.vue`) | No | `<template>` section |
| String template | No | `template: '<div>...</div>'` |
| In-DOM template | **Yes** | `<div id="app">...</div>` |
| `<script type="text/x-template">` | **Yes** | Browser parses the script content |

## Best Practice: Use SFCs

The simplest solution is to use Single-File Components (`.vue` files) which completely avoid in-DOM parsing issues:

```vue
<!-- MyComponent.vue - All issues avoided -->
<script setup>
import BlogPost from './BlogPost.vue'
</script>

<template>
  <BlogPost postTitle="hello" @updatePost="onUpdate" />

  <table>
    <BlogPostRow v-for="post in posts" :key="post.id" :post="post" />
  </table>
</template>
```

## Reference
- [Vue.js - In-DOM Template Parsing Caveats](https://vuejs.org/guide/essentials/component-basics.html#in-dom-template-parsing-caveats)
```

## File: `skills/vue-debug-guides/reference/inheritattrs-false-for-wrapper-components.md`
```markdown
# Use inheritAttrs: false for Wrapper Components

## Rule

When building wrapper components where attributes should be applied to an inner element instead of the root element, always set `inheritAttrs: false` and explicitly bind `$attrs` to the target element.

## Why This Matters

- By default, Vue applies all non-prop attributes to the root element
- Wrapper components often have a non-semantic root (div wrapper, label wrapper)
- Attributes like `id`, `aria-*`, `data-*`, and event listeners should target the functional element
- Without `inheritAttrs: false`, accessibility and functionality can break

## Bad Code

```vue
<!-- BaseInput.vue - WRONG: attrs go to wrapper div, not input -->
<template>
  <div class="input-wrapper">
    <label>{{ label }}</label>
    <input type="text" />
  </div>
</template>

<script setup>
defineProps(['label'])
</script>

<!-- Parent usage -->
<BaseInput
  id="email"
  placeholder="Enter email"
  aria-describedby="email-help"
  @focus="handleFocus"
/>

<!--
  RESULT: All attrs go to the wrapper div!
  <div class="input-wrapper" id="email" placeholder="Enter email" ...>
    <label>...</label>
    <input type="text" />  <!-- No id, placeholder, or aria! -->
  </div>
-->
```

## Good Code

```vue
<!-- BaseInput.vue - CORRECT: attrs bound to input element -->
<script setup>
defineProps(['label'])

defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <div class="input-wrapper">
    <label>{{ label }}</label>
    <input type="text" v-bind="$attrs" />
  </div>
</template>

<!-- Parent usage -->
<BaseInput
  id="email"
  placeholder="Enter email"
  aria-describedby="email-help"
  @focus="handleFocus"
/>

<!--
  RESULT: Attrs correctly applied to input
  <div class="input-wrapper">
    <label>...</label>
    <input type="text" id="email" placeholder="Enter email"
           aria-describedby="email-help" />
  </div>
-->
```

## Setting inheritAttrs in Different Syntaxes

### Script Setup (Vue 3.3+)

```vue
<script setup>
defineOptions({
  inheritAttrs: false
})
</script>
```

### Script Setup (Before Vue 3.3)

```vue
<script>
export default {
  inheritAttrs: false
}
</script>

<script setup>
// Your setup code here
</script>
```

### Options API

```vue
<script>
export default {
  inheritAttrs: false,
  // other options...
}
</script>
```

## Common Wrapper Component Patterns

### Form Input Wrapper

```vue
<script setup>
import { useAttrs, computed } from 'vue'

defineProps({
  label: String,
  error: String
})

defineOptions({
  inheritAttrs: false
})

const attrs = useAttrs()

// Separate class/style for wrapper vs input
const inputAttrs = computed(() => {
  const { class: _, style: __, ...rest } = attrs
  return rest
})
</script>

<template>
  <div class="form-field" :class="{ 'has-error': error }">
    <label v-if="label">{{ label }}</label>
    <input v-bind="inputAttrs" />
    <span v-if="error" class="error">{{ error }}</span>
  </div>
</template>
```

### Button with Icon Wrapper

```vue
<script setup>
defineProps({
  icon: String,
  iconPosition: {
    type: String,
    default: 'left'
  }
})

defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <button class="icon-button" v-bind="$attrs">
    <span v-if="icon && iconPosition === 'left'" class="icon">{{ icon }}</span>
    <slot />
    <span v-if="icon && iconPosition === 'right'" class="icon">{{ icon }}</span>
  </button>
</template>
```

### Link Wrapper Component

```vue
<script setup>
defineProps({
  to: String,
  external: Boolean
})

defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <a
    v-if="external"
    :href="to"
    target="_blank"
    rel="noopener noreferrer"
    v-bind="$attrs"
  >
    <slot />
  </a>
  <router-link v-else :to="to" v-bind="$attrs">
    <slot />
  </router-link>
</template>
```

## When NOT to Use inheritAttrs: false

- Simple components with a single semantic root element
- Components where the root element should receive all attributes
- Components that don't wrap other functional elements

```vue
<!-- SimpleCard.vue - No need for inheritAttrs: false -->
<template>
  <article class="card">
    <slot />
  </article>
</template>
<!-- Passing class, id, or data-* to the root article is fine -->
```

## References

- [Fallthrough Attributes - Disabling Attribute Inheritance](https://vuejs.org/guide/components/attrs.html#disabling-attribute-inheritance)
- [Build Advanced Components in Vue 3 using $attrs](https://www.thisdot.co/blog/build-advanced-components-in-vue-3-using-usdattrs)
```

## File: `skills/vue-debug-guides/reference/keepalive-router-nested-double-mount.md`
```markdown
---
title: KeepAlive with Nested Routes Double Mount Issue
impact: HIGH
impactDescription: Using KeepAlive with nested Vue Router routes can cause child components to mount twice
type: gotcha
tags: [vue3, keepalive, vue-router, nested-routes, double-mount, bug]
---

# KeepAlive with Nested Routes Double Mount Issue

**Impact: HIGH** - When using `<KeepAlive>` with nested Vue Router routes, child route components may mount twice. This is a known issue that can cause duplicate API calls, broken state, and confusing behavior.

## Task Checklist

- [ ] Test nested routes thoroughly when using KeepAlive
- [ ] Avoid mixing KeepAlive with deeply nested route structures
- [ ] Use workarounds if double mount is observed
- [ ] Consider alternative caching strategies for nested routes

## The Problem

```vue
<!-- App.vue -->
<template>
  <router-view v-slot="{ Component }">
    <KeepAlive>
      <component :is="Component" />
    </KeepAlive>
  </router-view>
</template>
```

```javascript
// router.js
const routes = [
  {
    path: '/parent',
    component: Parent,
    children: [
      {
        path: 'child',
        component: Child  // This may mount TWICE!
      }
    ]
  }
]
```

**Symptoms:**
- `onMounted` called twice in child component
- Duplicate API requests
- State initialization runs twice
- Console logs appear doubled

## Diagnosis

Add logging to confirm the issue:

```vue
<!-- Child.vue -->
<script setup>
import { onMounted, onActivated } from 'vue'

let mountCount = 0

onMounted(() => {
  mountCount++
  console.log('Child mounted - count:', mountCount)
  // If you see "count: 2", you have the double mount issue
})

onActivated(() => {
  console.log('Child activated')
})
</script>
```

## Workarounds

### Option 1: Use `useActivatedRoute` Pattern

Don't use `useRoute()` directly with KeepAlive:

```vue
<script setup>
import { ref, onActivated } from 'vue'
import { useRoute } from 'vue-router'

// Problem: useRoute() can cause issues with KeepAlive
// const route = useRoute()

// Solution: Get route info in onActivated
const routeParams = ref({})

onActivated(() => {
  const route = useRoute()
  routeParams.value = { ...route.params }
})
</script>
```

### Option 2: Avoid KeepAlive for Nested Route Parents

Only cache leaf routes, not parent layouts:

```vue
<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// Only cache specific leaf routes
const cachedRoutes = computed(() => {
  // Don't cache parent routes that have children
  return ['UserProfile', 'UserSettings'] // Only leaf components
})
</script>

<template>
  <router-view v-slot="{ Component, route: currentRoute }">
    <KeepAlive :include="cachedRoutes">
      <component :is="Component" :key="currentRoute.fullPath" />
    </KeepAlive>
  </router-view>
</template>
```

### Option 3: Guard Against Double Initialization

Protect your component from double mount effects:

```vue
<script setup>
import { ref, onMounted } from 'vue'

const isInitialized = ref(false)

onMounted(() => {
  if (isInitialized.value) {
    console.warn('Double mount detected, skipping initialization')
    return
  }
  isInitialized.value = true

  // Safe to initialize
  fetchData()
  setupEventListeners()
})
</script>
```

### Option 4: Use Route-Level Cache Control

```vue
<!-- App.vue -->
<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// Define which routes should be cached in route meta
const shouldCache = computed(() => {
  return route.meta.keepAlive !== false
})
</script>

<template>
  <router-view v-slot="{ Component }">
    <KeepAlive v-if="shouldCache">
      <component :is="Component" />
    </KeepAlive>
    <component v-else :is="Component" />
  </router-view>
</template>
```

```javascript
// router.js
const routes = [
  {
    path: '/parent',
    component: Parent,
    meta: { keepAlive: false }, // Don't cache parent routes
    children: [
      {
        path: 'child',
        component: Child,
        meta: { keepAlive: true } // Cache leaf routes
      }
    ]
  }
]
```

### Option 5: Flatten Route Structure

Avoid nesting if possible:

```javascript
// Instead of nested routes
const routes = [
  // Flat structure avoids the issue
  { path: '/users', component: UserList },
  { path: '/users/:id', component: UserDetail },
  { path: '/users/:id/settings', component: UserSettings }
]
```

## Key Points

1. **Known Vue Router issue** - Double mount with KeepAlive + nested routes
2. **Watch for symptoms** - Duplicate API calls, doubled logs
3. **Avoid caching parent routes** - Only cache leaf components
4. **Add initialization guards** - Protect against double execution
5. **Test thoroughly** - This issue may not appear immediately

## Reference
- [Vue Router Issue #626: keep-alive in nested route mounted twice](https://github.com/vuejs/router/issues/626)
- [GitHub: vue3-keep-alive-component workaround](https://github.com/emiyalee1005/vue3-keep-alive-component)
- [Vue.js KeepAlive Documentation](https://vuejs.org/guide/built-ins/keep-alive.html)
```

## File: `skills/vue-debug-guides/reference/keepalive-transition-memory-leak.md`
```markdown
---
title: KeepAlive with Transition Memory Leak
impact: MEDIUM
impactDescription: Combining KeepAlive with Transition can cause memory leaks in certain Vue versions
type: gotcha
tags: [vue3, keepalive, transition, memory-leak, animation]
---

# KeepAlive with Transition Memory Leak

**Impact: MEDIUM** - There is a known memory leak when using `<Transition>` and `<KeepAlive>` together. Component instances may not be properly freed from memory when combining these features.

## Task Checklist

- [ ] Test memory behavior when using KeepAlive + Transition together
- [ ] Consider if transition animation is necessary with cached components
- [ ] Use browser DevTools Memory tab to verify no leak
- [ ] Keep Vue updated to get latest bug fixes

## The Problem

```vue
<template>
  <!-- Known memory leak combination in some Vue versions -->
  <Transition name="fade">
    <KeepAlive>
      <component :is="currentView" />
    </KeepAlive>
  </Transition>
</template>
```

When switching between components repeatedly:
- Component instances accumulate in memory
- References prevent garbage collection
- Memory usage grows with each switch

## Diagnosis

Use Chrome DevTools to detect the leak:

1. Open DevTools > Memory tab
2. Take heap snapshot
3. Switch between components 10+ times
4. Take another heap snapshot
5. Compare: look for growing VueComponent count

## Workarounds

### Option 1: Remove Transition if Not Essential

```vue
<template>
  <!-- No memory leak without Transition -->
  <KeepAlive :max="5">
    <component :is="currentView" />
  </KeepAlive>
</template>
```

### Option 2: Use CSS Animations Instead

```vue
<template>
  <KeepAlive :max="5">
    <component
      :is="currentView"
      :class="{ 'fade-enter': isTransitioning }"
    />
  </KeepAlive>
</template>

<style>
.fade-enter {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>
```

### Option 3: Use Strict Cache Limits

If you must use both, minimize impact with strict limits:

```vue
<template>
  <Transition name="fade" mode="out-in">
    <KeepAlive :max="3">
      <component :is="currentView" />
    </KeepAlive>
  </Transition>
</template>
```

### Option 4: Key-Based Cache Invalidation

Force fresh instances when needed:

```vue
<script setup>
import { ref, computed } from 'vue'

const currentView = ref('Dashboard')
const cacheKey = ref(0)

function switchViewFresh(view) {
  currentView.value = view
  cacheKey.value++ // Force new instance
}
</script>

<template>
  <Transition name="fade" mode="out-in">
    <KeepAlive :max="3">
      <component :is="currentView" :key="cacheKey" />
    </KeepAlive>
  </Transition>
</template>
```

## Keep Vue Updated

This is a known issue tracked in Vue's GitHub repository. Memory leak fixes are periodically released, so ensure you're on the latest Vue version:

```bash
npm update vue
```

## Key Points

1. **Known issue** - Memory leaks with KeepAlive + Transition are documented
2. **Test in DevTools** - Use Memory tab to verify your specific usage
3. **Consider alternatives** - CSS animations may work without the leak
4. **Set strict `max`** - Limit cache size to cap memory impact
5. **Keep Vue updated** - Bug fixes are released periodically

## Reference
- [GitHub Issue #9842: Memory leak with transition and keep-alive](https://github.com/vuejs/vue/issues/9842)
- [GitHub Issue #9840: Memory leak with transition and keep-alive](https://github.com/vuejs/vue/issues/9840)
- [Vue.js KeepAlive Documentation](https://vuejs.org/guide/built-ins/keep-alive.html)
```

## File: `skills/vue-debug-guides/reference/keyup-modifier-timing.md`
```markdown
---
title: System Modifier Keys Must Be Held During keyup Events
impact: MEDIUM
impactDescription: Modifier keys (ctrl, alt, shift, meta) behave differently with keyup - they must be held when the key is released
type: gotcha
tags: [vue3, events, keyboard, modifiers, keyup, shortcuts]
---

# System Modifier Keys Must Be Held During keyup Events

**Impact: MEDIUM** - When using system modifier keys (`.ctrl`, `.alt`, `.shift`, `.meta`) with `keyup` events, the modifier must still be pressed when the other key is released. Releasing the modifier key first will not trigger the event, causing keyboard shortcuts to appear broken.

## Task Checklist

- [ ] Understand that `@keyup.ctrl` requires Ctrl to be held while releasing another key
- [ ] Consider using `keydown` instead of `keyup` for modifier key combinations
- [ ] Use `.exact` when you need precise modifier key control
- [ ] Test keyboard shortcuts with proper key release order

**Incorrect:**
```html
<!-- WRONG: Expecting this to fire when Ctrl is released -->
<template>
  <input @keyup.ctrl="onCtrlRelease" />
  <!-- This does NOT fire when you just release Ctrl! -->
  <!-- It fires when you release ANY key while holding Ctrl -->
</template>
```

```html
<!-- WRONG: Misunderstanding keyup.ctrl behavior -->
<template>
  <div @keyup.ctrl="handleShortcut">
    <!-- User presses Ctrl+S, releases Ctrl first, then S -->
    <!-- Event does NOT fire because Ctrl wasn't held during S release -->
  </div>
</template>
```

**Correct:**
```html
<!-- CORRECT: User must hold Ctrl while releasing another key -->
<template>
  <input @keyup.ctrl.s="saveDocument" />
  <!-- User presses Ctrl+S, then releases S while holding Ctrl -->
  <!-- Event fires correctly -->
</template>

<script setup>
function saveDocument(event) {
  event.preventDefault()
  // Save logic here
}
</script>
```

```html
<!-- CORRECT: Use keydown for more intuitive modifier behavior -->
<template>
  <div @keydown.ctrl.s="saveDocument">
    <!-- keydown fires immediately when both keys are pressed -->
    <!-- More intuitive for keyboard shortcuts -->
  </div>
</template>
```

```html
<!-- CORRECT: Use .exact for precise modifier control -->
<template>
  <!-- Only fires when ONLY Ctrl is pressed (no Shift, Alt, etc.) -->
  <button @click.ctrl.exact="onCtrlClick">Ctrl+Click Only</button>

  <!-- Fires with no system modifiers at all -->
  <button @click.exact="onPlainClick">Plain Click Only</button>
</template>
```

## How System Modifiers Work with keyup

```javascript
// Timeline of Ctrl+S keydown:
// 1. User presses Ctrl (keydown fires)
// 2. User presses S while holding Ctrl (keydown fires)

// Timeline of Ctrl+S keyup:
// 3. User releases S while holding Ctrl (keyup.ctrl.s fires!)
// 4. User releases Ctrl (keyup fires, but not keyup.ctrl.s)

// Common mistake:
// 3. User releases Ctrl first (nothing fires for our handler)
// 4. User releases S (keyup.s fires, but not keyup.ctrl.s)
```

## System Modifier Keys

```html
<!-- Available system modifiers -->
<input @keyup.ctrl="..." />   <!-- Ctrl key -->
<input @keyup.alt="..." />    <!-- Alt key (Option on Mac) -->
<input @keyup.shift="..." />  <!-- Shift key -->
<input @keyup.meta="..." />   <!-- Cmd on Mac, Windows key on PC -->
```

## The .exact Modifier

```html
<!-- Different .exact behaviors -->

<!-- Fires even if Shift/Alt are also pressed -->
<button @click.ctrl="onClick">Ctrl + any other modifiers</button>

<!-- Fires ONLY when Ctrl alone is pressed -->
<button @click.ctrl.exact="onClick">Ctrl only, no other modifiers</button>

<!-- Fires ONLY when no system modifiers are pressed -->
<button @click.exact="onClick">No modifiers allowed</button>
```

## Best Practice: Prefer keydown for Shortcuts

```html
<template>
  <div
    tabindex="0"
    @keydown.ctrl.s.prevent="save"
    @keydown.ctrl.z.prevent="undo"
    @keydown.ctrl.shift.z.prevent="redo"
  >
    <!-- keydown is more reliable for keyboard shortcuts -->
    <!-- Add .prevent to stop browser default (e.g., save dialog) -->
  </div>
</template>
```

## Reference
- [Vue.js Event Handling - Key Modifiers](https://vuejs.org/guide/essentials/event-handling.html#key-modifiers)
- [Vue.js Event Handling - System Modifier Keys](https://vuejs.org/guide/essentials/event-handling.html#system-modifier-keys)
```

## File: `skills/vue-debug-guides/reference/lifecycle-dom-access-timing.md`
```markdown
---
title: Access DOM Only After Mounted Hook
impact: HIGH
impactDescription: Accessing DOM elements before mounted causes undefined errors and silent failures
type: capability
tags: [vue3, vue2, lifecycle, dom, mounted, created, beforeMount, template-refs]
---

# Access DOM Only After Mounted Hook

**Impact: HIGH** - Attempting to access DOM elements or `this.$el` in `created` or `beforeMount` hooks fails because the component's template has not yet been rendered to the DOM. This leads to undefined errors, null references, and failed third-party library initializations.

The component's DOM is only available starting from the `mounted` hook (Options API) or after `onMounted` runs (Composition API). Before this point, `this.$el` is undefined and template refs are null.

## Task Checklist

- [ ] Perform DOM manipulations only in `mounted`/`onMounted` or later
- [ ] Initialize DOM-dependent libraries (charts, maps, editors) in mounted
- [ ] Use `created` for data initialization and API calls (non-DOM operations)
- [ ] Access template refs only after mounted
- [ ] Use `$nextTick` if you need DOM after reactive data changes

**Incorrect:**
```javascript
// WRONG: Accessing DOM in created hook
export default {
  created() {
    // DOM doesn't exist yet!
    console.log(this.$el) // undefined
    this.$el.querySelector('.chart') // Error: Cannot read property 'querySelector' of undefined

    // Third-party library initialization fails
    new Chart(document.getElementById('myChart')) // Element doesn't exist yet
  }
}
```

```javascript
// WRONG: Accessing DOM in beforeMount
export default {
  beforeMount() {
    // Still too early - template is compiled but not mounted
    console.log(this.$el) // undefined in Vue 3
    this.$refs.myInput.focus() // Error: Cannot read property 'focus' of undefined
  }
}
```

```vue
<!-- WRONG: Accessing template ref synchronously in setup -->
<script setup>
import { ref } from 'vue'

const myInput = ref(null)

// This runs during setup, before mounting
myInput.value.focus() // Error: Cannot read property 'focus' of null
</script>

<template>
  <input ref="myInput" />
</template>
```

**Correct:**
```javascript
// CORRECT: Use created for data, mounted for DOM
export default {
  data() {
    return { chartData: null }
  },
  async created() {
    // Data fetching is fine in created
    this.chartData = await fetchChartData()
  },
  mounted() {
    // Now the DOM exists and is safe to access
    console.log(this.$el) // <div>...</div>

    // Initialize DOM-dependent libraries
    this.chart = new Chart(this.$refs.chartCanvas, {
      data: this.chartData
    })
  }
}
```

```vue
<!-- CORRECT: Access template refs in onMounted -->
<script setup>
import { ref, onMounted } from 'vue'

const myInput = ref(null)

onMounted(() => {
  // DOM is now available
  myInput.value.focus() // Works!
})
</script>

<template>
  <input ref="myInput" />
</template>
```

```javascript
// CORRECT: Using $nextTick for DOM access after data changes
export default {
  methods: {
    async addItem() {
      this.items.push(newItem)

      // Wait for Vue to update the DOM
      await this.$nextTick()

      // Now the new element exists in DOM
      this.$refs.list.lastElementChild.scrollIntoView()
    }
  }
}
```

## Vue 3 Composition API Pattern

```vue
<script setup>
import { ref, onMounted, nextTick } from 'vue'

const listRef = ref(null)
const items = ref([])

onMounted(() => {
  // Safe to access DOM here
  listRef.value.style.height = '400px'
})
</script>
```

## Vue 3.5+ useTemplateRef Pattern

```vue
<script setup>
import { useTemplateRef, onMounted } from 'vue'

// Vue 3.5+ recommended approach - decouples ref name from variable name
const input = useTemplateRef('my-input')

onMounted(() => {
  input.value.focus()
})
</script>

<template>
  <input ref="my-input" />
</template>
```

## Composition API with nextTick

```vue
<script setup>
import { ref, nextTick } from 'vue'

const listRef = ref(null)
const items = ref([])

async function addItem(item) {
  items.value.push(item)

  // Wait for DOM update after reactive change
  await nextTick()

  // Now new item is in DOM
  listRef.value.lastElementChild.focus()
}
</script>

<template>
  <ul ref="listRef">
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </ul>
</template>
```

## Common Third-Party Libraries

```javascript
// CORRECT: Initialize in mounted
export default {
  mounted() {
    // Chart.js
    this.chart = new Chart(this.$refs.canvas, config)

    // Leaflet maps
    this.map = L.map(this.$refs.mapContainer).setView([51.505, -0.09], 13)

    // Monaco Editor
    this.editor = monaco.editor.create(this.$refs.editorContainer, options)

    // Video.js
    this.player = videojs(this.$refs.videoElement)
  },
  beforeUnmount() {
    // Don't forget cleanup!
    this.chart?.destroy()
    this.map?.remove()
    this.editor?.dispose()
    this.player?.dispose()
  }
}
```

## Reference
- [Vue.js Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)
- [Vue.js Template Refs](https://vuejs.org/guide/essentials/template-refs.html)
- [Vue.js nextTick](https://vuejs.org/api/general.html#nexttick)
```

## File: `skills/vue-debug-guides/reference/lifecycle-hooks-synchronous-registration.md`
```markdown
---
title: Register Lifecycle Hooks Synchronously During Setup
impact: HIGH
impactDescription: Asynchronously registered lifecycle hooks will never execute
type: capability
tags: [vue3, composition-api, lifecycle, onMounted, onUnmounted, async, setup]
---

# Register Lifecycle Hooks Synchronously During Setup

**Impact: HIGH** - Lifecycle hooks registered asynchronously (e.g., inside setTimeout, after await) will never be called because Vue cannot associate them with the component instance. This leads to silent failures where expected initialization or cleanup code never runs.

In Vue 3's Composition API, lifecycle hooks like `onMounted`, `onUnmounted`, `onUpdated`, etc. must be registered synchronously during component setup. The hook registration doesn't need to be lexically inside `setup()` or `<script setup>`, but the call stack must be synchronous and originate from within setup.

## Task Checklist

- [ ] Register all lifecycle hooks at the top level of setup() or `<script setup>`
- [ ] Never register hooks inside setTimeout, setInterval, or Promise callbacks
- [ ] When calling composables that use lifecycle hooks, call them synchronously
- [ ] Hooks CAN be in external functions if called synchronously from setup

**Incorrect:**
```javascript
// WRONG: Hook registered asynchronously - will NEVER execute
import { onMounted } from 'vue'

export default {
  async setup() {
    // After await, we're in a different call stack
    const data = await fetchInitialData()

    // This hook will NOT be registered!
    onMounted(() => {
      console.log('This will never run')
    })
  }
}
```

```javascript
// WRONG: Hook registered in setTimeout - will NEVER execute
import { onMounted } from 'vue'

export default {
  setup() {
    setTimeout(() => {
      // This is asynchronous - hook won't be registered!
      onMounted(() => {
        initializeChart()
      })
    }, 100)
  }
}
```

```javascript
// WRONG: Hook registered in Promise callback
import { onMounted } from 'vue'

export default {
  setup() {
    fetchConfig().then(() => {
      // Asynchronous! This will silently fail
      onMounted(() => {
        applyConfig()
      })
    })
  }
}
```

**Correct:**
```javascript
// CORRECT: Hook registered synchronously at top level
import { onMounted, ref } from 'vue'

export default {
  setup() {
    const data = ref(null)

    // Register hook synchronously FIRST
    onMounted(async () => {
      // Async operations are fine INSIDE the hook
      data.value = await fetchInitialData()
      initializeChart()
    })

    return { data }
  }
}
```

```vue
<!-- CORRECT: <script setup> - hooks at top level -->
<script setup>
import { onMounted, onUnmounted, ref } from 'vue'

const isReady = ref(false)

// These are synchronous during script setup execution
onMounted(() => {
  isReady.value = true
})

onUnmounted(() => {
  cleanup()
})
</script>
```

```javascript
// CORRECT: Hook in external function called synchronously from setup
import { onMounted, onUnmounted } from 'vue'

function useWindowResize(callback) {
  // This is fine - it's called synchronously from setup
  onMounted(() => {
    window.addEventListener('resize', callback)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', callback)
  })
}

export default {
  setup() {
    // Composable called synchronously - hooks will be registered
    useWindowResize(handleResize)
  }
}
```

## Multiple Hooks Are Allowed

```javascript
// CORRECT: You can register the same hook multiple times
import { onMounted } from 'vue'

export default {
  setup() {
    // Both will run, in order of registration
    onMounted(() => {
      initializeA()
    })

    onMounted(() => {
      initializeB()
    })
  }
}
```

## Reference
- [Vue.js Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)
- [Composition API Lifecycle Hooks](https://vuejs.org/api/composition-api-lifecycle.html)
```

## File: `skills/vue-debug-guides/reference/lifecycle-ssr-awareness.md`
```markdown
---
title: Mounted and Unmounted Hooks Do Not Run During SSR
impact: MEDIUM
impactDescription: SSR applications may fail if mounted-only code is essential for functionality
type: capability
tags: [vue3, lifecycle, ssr, server-side-rendering, nuxt, onMounted, mounted, hydration]
---

# Mounted and Unmounted Hooks Do Not Run During SSR

**Impact: MEDIUM** - During server-side rendering (SSR), lifecycle hooks like `mounted`, `onMounted`, `unmounted`, and `onUnmounted` are never called on the server. This can cause differences between server-rendered and client-rendered content, hydration mismatches, and missing functionality if critical logic is placed only in these hooks.

On the server, only `beforeCreate`, `created`, and their Composition API equivalents run. Client-specific operations (DOM access, browser APIs, third-party libraries) must be in mounted hooks, but you must handle the SSR case appropriately.

## Task Checklist

- [ ] Place browser-specific code (window, document, localStorage) in mounted/onMounted
- [ ] Ensure critical data fetching happens in hooks that run on server (created)
- [ ] Handle hydration mismatches for content that differs client vs server
- [ ] Use `<ClientOnly>` wrapper (Nuxt) or conditional rendering for client-only components
- [ ] Check for browser environment before using browser APIs

**Incorrect:**
```javascript
// WRONG: Accessing browser APIs in created - breaks SSR
export default {
  created() {
    // These don't exist on the server!
    this.width = window.innerWidth // ReferenceError: window is not defined
    this.savedData = localStorage.getItem('data') // ReferenceError: localStorage is not defined
  }
}
```

```javascript
// WRONG: Critical initialization only in mounted - won't run on server
export default {
  data() {
    return { user: null }
  },
  async mounted() {
    // This won't run on server - page renders without user data
    // Then hydrates with user data - causes flash of content
    this.user = await fetchCurrentUser()
  }
}
```

**Correct:**
```javascript
// CORRECT: Data fetching in created (runs on server), DOM in mounted
export default {
  data() {
    return {
      user: null,
      windowWidth: 0
    }
  },
  async created() {
    // This runs on both server and client
    this.user = await fetchCurrentUser()
  },
  mounted() {
    // Browser-specific code safely in mounted
    this.windowWidth = window.innerWidth
    window.addEventListener('resize', this.handleResize)
  },
  unmounted() {
    window.removeEventListener('resize', this.handleResize)
  }
}
```

```vue
<!-- CORRECT: Composition API with SSR awareness -->
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const user = ref(null)
const windowWidth = ref(0)

// This runs on both server and client (during setup)
user.value = await useFetch('/api/user')

// These only run on client
onMounted(() => {
  windowWidth.value = window.innerWidth
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

function handleResize() {
  windowWidth.value = window.innerWidth
}
</script>
```

## Checking for Browser Environment

```javascript
// CORRECT: Guard browser API access
export default {
  data() {
    return { theme: 'light' }
  },
  created() {
    // Check if we're in browser before accessing browser APIs
    if (typeof window !== 'undefined') {
      this.theme = localStorage.getItem('theme') || 'light'
    }
  },
  mounted() {
    // mounted only runs in browser, so this is always safe
    this.applyTheme()
  }
}
```

## Nuxt.js Specific Patterns

```vue
<!-- CORRECT: Using Nuxt's ClientOnly for client-specific components -->
<template>
  <div>
    <!-- This content renders on both server and client -->
    <h1>Dashboard</h1>

    <!-- This only renders on client - no hydration mismatch -->
    <ClientOnly>
      <ChartComponent :data="chartData" />
      <template #fallback>
        <p>Loading chart...</p>
      </template>
    </ClientOnly>
  </div>
</template>
```

```javascript
// CORRECT: Using Nuxt's process.client/process.server
export default {
  created() {
    if (process.client) {
      // Only runs in browser
      this.initAnalytics()
    }
    if (process.server) {
      // Only runs on server
      this.logServerRequest()
    }
  }
}
```

## Handling Hydration Mismatches

```vue
<script setup>
import { ref, onMounted } from 'vue'

// Start with a value that matches what server renders
const currentTime = ref(null)

onMounted(() => {
  // Update to real value only on client
  // This prevents hydration mismatch
  currentTime.value = new Date().toLocaleTimeString()
})
</script>

<template>
  <!-- Renders null on server, then updates on client -->
  <span v-if="currentTime">{{ currentTime }}</span>
  <span v-else>Loading...</span>
</template>
```

## Reference
- [Vue.js SSR Guide](https://vuejs.org/guide/scaling-up/ssr.html)
- [Nuxt.js Lifecycle](https://nuxt.com/docs/api/composables/use-nuxt-app#lifecycle-hooks)
- [Vue SSR Hydration](https://vuejs.org/guide/scaling-up/ssr.html#client-hydration)
```

## File: `skills/vue-debug-guides/reference/local-components-not-in-descendants.md`
```markdown
---
title: Locally Registered Components Are Not Available in Descendants
impact: HIGH
impactDescription: Common source of "component not found" errors in nested components
type: gotcha
tags: [vue3, component-registration, local-registration, scope, nested-components]
---

# Locally Registered Components Are Not Available in Descendants

**Impact: HIGH** - Locally registered components are only available in the component where they are registered, NOT in its child or descendant components. This is a common source of "Unknown component" or "Failed to resolve component" errors when developers expect a component registered in a parent to be available in children.

## Task Checklist

- [ ] Import and register components in every file where they are used
- [ ] Do not expect parent's local components to be available in children
- [ ] If a component is needed in many places, consider global registration only as a last resort
- [ ] Use IDE auto-import features to simplify repeated imports

**Incorrect:**
```vue
<!-- ParentComponent.vue -->
<script setup>
import Card from './Card.vue'
import ChildComponent from './ChildComponent.vue'
</script>

<template>
  <Card>Parent content</Card>
  <ChildComponent />
</template>
```

```vue
<!-- ChildComponent.vue -->
<script setup>
// WRONG: Expecting Card to be available because parent imported it
// This will cause "Failed to resolve component: Card" error
</script>

<template>
  <!-- ERROR: Card is not available here! -->
  <Card>
    Child content
  </Card>
</template>
```

**Correct:**
```vue
<!-- ParentComponent.vue -->
<script setup>
import Card from './Card.vue'
import ChildComponent from './ChildComponent.vue'
</script>

<template>
  <Card>Parent content</Card>
  <ChildComponent />
</template>
```

```vue
<!-- ChildComponent.vue -->
<script setup>
// CORRECT: Each component must import what it uses
import Card from './Card.vue'
</script>

<template>
  <Card>
    Child content
  </Card>
</template>
```

## Common Scenarios

### Scenario 1: Deeply Nested Components
```vue
<!-- GrandchildComponent.vue -->
<script setup>
// Even if parent and grandparent both use Card,
// grandchild must import it separately
import Card from '@/components/Card.vue'
import Button from '@/components/Button.vue'
</script>

<template>
  <Card>
    <Button>Click me</Button>
  </Card>
</template>
```

### Scenario 2: Slot Content with Components
```vue
<!-- Parent.vue -->
<script setup>
import Modal from './Modal.vue'
import Form from './Form.vue'
</script>

<template>
  <!-- Form is registered in Parent, so it works in slot content -->
  <Modal>
    <Form /> <!-- This works because slot content is compiled in Parent's scope -->
  </Modal>
</template>
```

```vue
<!-- Modal.vue -->
<script setup>
// Modal doesn't need to import Form because slot content
// is compiled in the parent's scope, not Modal's scope
</script>

<template>
  <div class="modal">
    <slot /> <!-- Form component works here because it's parent's slot content -->
  </div>
</template>
```

### Scenario 3: Dynamic Components
```vue
<!-- Container.vue -->
<script setup>
import TabA from './TabA.vue'
import TabB from './TabB.vue'
import { ref, shallowRef } from 'vue'

// When using dynamic components, all possible components must be imported
const currentTab = shallowRef(TabA)
</script>

<template>
  <component :is="currentTab" />
</template>
```

## Why This Design?

Local registration provides:
1. **Explicit dependencies** - You can see exactly what each component uses
2. **Tree-shaking** - Unused components are removed from bundles
3. **Clear scope** - No magic or implicit behavior

## Reference
- [Vue.js Component Registration - Local Registration](https://vuejs.org/guide/components/registration.html#local-registration)
```

## File: `skills/vue-debug-guides/reference/mount-return-value.md`
```markdown
---
title: mount() Returns Component Instance, Not App Instance
impact: MEDIUM
impactDescription: Using mount() return value for app configuration silently fails
type: capability
tags: [vue3, createApp, mount, api]
---

# mount() Returns Component Instance, Not App Instance

**Impact: MEDIUM** - The `.mount()` method returns the root component instance, not the application instance. Attempting to chain app configuration methods after mount() will fail or produce unexpected behavior.

This is a subtle API detail that catches developers who assume mount() returns the app for continued chaining.

## Task Checklist

- [ ] Never chain app configuration methods after mount()
- [ ] If you need both instances, store them separately
- [ ] Use the component instance for accessing root component state or methods
- [ ] Use the app instance for configuration, plugins, and global registration

**Incorrect:**
```javascript
import { createApp } from 'vue'
import App from './App.vue'

// WRONG: Assuming mount returns app instance
const app = createApp(App).mount('#app')

// This fails! app is actually the root component instance
app.use(router)  // TypeError: app.use is not a function
app.config.errorHandler = fn  // app.config is undefined
```

```javascript
// WRONG: Trying to save both in one line
const { app, component } = createApp(App).mount('#app')  // Doesn't work this way
```

**Correct:**
```javascript
import { createApp } from 'vue'
import App from './App.vue'

// Store app instance separately
const app = createApp(App)

// Configure the app
app.use(router)
app.config.errorHandler = (err) => console.error(err)

// Store component instance if needed
const rootComponent = app.mount('#app')

// Now you have access to both:
// - app: the application instance (for config, plugins)
// - rootComponent: the root component instance (for state, methods)
```

```javascript
// If you only need the app configured and mounted (most common case):
createApp(App)
  .use(router)
  .use(pinia)
  .mount('#app')  // Return value (component instance) discarded - that's fine
```

## When You Need the Root Component Instance

```javascript
const app = createApp(App)
const vm = app.mount('#app')

// Access root component's exposed state/methods
console.log(vm.someExposedProperty)
vm.someExposedMethod()

// In Vue 3 with <script setup>, use defineExpose to expose:
// <script setup>
// import { ref } from 'vue'
// const count = ref(0)
// defineExpose({ count })
// </script>
```

## Reference
- [Vue.js - Mounting the App](https://vuejs.org/guide/essentials/application.html#mounting-the-app)
- [Vue.js Application API - mount()](https://vuejs.org/api/application.html#app-mount)
```

## File: `skills/vue-debug-guides/reference/multi-root-component-class-attrs.md`
```markdown
# Multi-Root Component Class Attribute Inheritance

## Rule

When a Vue 3 component has multiple root elements, class and style bindings from the parent will NOT automatically fall through. You must explicitly bind `$attrs.class` or `$attrs.style` to the target element.

## Why This Matters

- Vue 3 components can have multiple root elements (fragments)
- Unlike single-root components, multi-root components have no automatic attribute fallthrough
- Without explicit handling, classes and styles passed from parent are silently ignored
- Vue will emit a runtime warning, but styles/classes simply won't apply

## Bad Code

```vue
<!-- ChildComponent.vue - WRONG: classes from parent won't apply -->
<template>
  <header>Header</header>
  <main>Content</main>
  <footer>Footer</footer>
</template>

<!-- Parent usage -->
<ChildComponent class="my-custom-class" />
<!-- Result: my-custom-class is NOT applied to any element -->
```

## Good Code

```vue
<!-- ChildComponent.vue - CORRECT: explicitly bind $attrs.class -->
<template>
  <header>Header</header>
  <main :class="$attrs.class" :style="$attrs.style">Content</main>
  <footer>Footer</footer>
</template>

<!-- Or bind all attrs to one element -->
<template>
  <header>Header</header>
  <main v-bind="$attrs">Content</main>
  <footer>Footer</footer>
</template>
```

## Accessing $attrs in script setup

```vue
<script setup>
import { useAttrs } from 'vue'
const attrs = useAttrs()
// attrs.class and attrs.style are available
</script>

<template>
  <header>Header</header>
  <main :class="attrs.class">Content</main>
  <footer>Footer</footer>
</template>
```

## Disabling Automatic Inheritance

For single-root components where you want to control attribute placement:

```vue
<script>
export default {
  inheritAttrs: false
}
</script>

<script setup>
import { useAttrs } from 'vue'
const attrs = useAttrs()
</script>

<template>
  <div class="wrapper">
    <input v-bind="attrs" />
  </div>
</template>
```

## Vue 2 to Vue 3 Migration Note

In Vue 2, `$attrs` did NOT include `class` and `style`. In Vue 3, `$attrs` contains ALL attributes including `class` and `style`. This is a breaking change that affects how you handle attribute forwarding.

## References

- [Fallthrough Attributes](https://vuejs.org/guide/components/attrs.html)
- [Vue 3 Migration Guide - $attrs includes class & style](https://v3-migration.vuejs.org/breaking-changes/attrs-includes-class-style)
```

## File: `skills/vue-debug-guides/reference/native-event-collision-with-emits.md`
```markdown
---
title: Declaring Native Event Names in Emits Blocks Native Listeners
impact: MEDIUM
impactDescription: Declaring native events like 'click' in emits prevents native DOM event listeners from working
type: gotcha
tags: [vue3, emits, native-events, click, event-collision]
---

# Declaring Native Event Names in Emits Blocks Native Listeners

**Impact: MEDIUM** - When you declare a native DOM event name (like `click`, `input`, `focus`) in your component's `emits` option, listeners for that event will ONLY respond to your component's `emit()` calls. They will no longer respond to the actual native DOM events on the root element.

This can cause unexpected behavior where clicks seem to stop working on your component.

## Task Checklist

- [ ] Understand that declaring native event names changes listener behavior
- [ ] Always emit the event when you declare it
- [ ] Don't declare native events if you want fallthrough behavior
- [ ] Test click/input handling after adding emits declarations

## The Problem

**Incorrect - Declaring but not emitting:**
```vue
<!-- ClickableCard.vue -->
<script setup>
// Declared 'click' but never emit it!
const emit = defineEmits(['click', 'select'])
</script>

<template>
  <div class="card">
    <slot></slot>
  </div>
</template>
```

```vue
<!-- Parent.vue -->
<template>
  <!-- This NEVER fires! Native clicks are blocked -->
  <ClickableCard @click="handleClick">
    Click me
  </ClickableCard>
</template>
```

**Why it fails:**
1. `click` is declared in `emits`
2. Vue treats `@click` as a component event listener
3. Native click on the `<div>` doesn't trigger component event
4. Since `emit('click')` is never called, handler never fires

## The Solution

**Option 1: Emit the event explicitly:**
```vue
<!-- ClickableCard.vue -->
<script setup>
const emit = defineEmits(['click', 'select'])
</script>

<template>
  <!-- Explicitly emit click when div is clicked -->
  <div class="card" @click="emit('click', $event)">
    <slot></slot>
  </div>
</template>
```

**Option 2: Don't declare native events (use fallthrough):**
```vue
<!-- ClickableCard.vue -->
<script setup>
// Only declare custom events, not native ones
const emit = defineEmits(['select', 'custom-action'])
</script>

<template>
  <!-- Native @click from parent falls through to this div -->
  <div class="card">
    <slot></slot>
  </div>
</template>
```

```vue
<!-- Parent.vue -->
<template>
  <!-- Native click falls through and works -->
  <ClickableCard @click="handleClick">
    Click me
  </ClickableCard>
</template>
```

## Native Events Affected

This applies to any native DOM event you might declare:

| Event | Behavior When Declared |
|-------|----------------------|
| `click` | Only responds to `emit('click')`, not native clicks |
| `input` | Only responds to `emit('input')`, not native input |
| `change` | Only responds to `emit('change')`, not native change |
| `focus` | Only responds to `emit('focus')`, not native focus |
| `blur` | Only responds to `emit('blur')`, not native blur |
| `submit` | Only responds to `emit('submit')`, not native form submit |
| `keydown` | Only responds to `emit('keydown')`, not native keydown |

## When This Is Intentional

Sometimes you WANT to intercept native events:

```vue
<!-- CustomInput.vue -->
<script setup>
// Intentionally intercept 'input' to transform the value
const emit = defineEmits(['input', 'update:modelValue'])

function handleInput(event) {
  const transformedValue = event.target.value.toUpperCase()
  emit('input', transformedValue) // Emit transformed value, not raw event
  emit('update:modelValue', transformedValue)
}
</script>

<template>
  <input @input="handleInput" />
</template>
```

Here, declaring `input` is correct because you want to intercept and transform the native event before passing it to the parent.

## Debugging Tips

If your click handlers aren't firing:

1. Check if the event is declared in `emits`
2. If declared, ensure you're calling `emit('click')` somewhere
3. If you want native behavior, remove from `emits` declaration
4. Use Vue DevTools to see which events are being emitted

```vue
<script setup>
const emit = defineEmits(['click'])

function handleClick(event) {
  console.log('Native click received, now emitting component event')
  emit('click', event)
}
</script>

<template>
  <div @click="handleClick">Click me</div>
</template>
```

## Reference
- [Vue.js Component Events](https://vuejs.org/guide/components/events.html)
- [Vue.js Fallthrough Attributes](https://vuejs.org/guide/components/attrs.html)
```

## File: `skills/vue-debug-guides/reference/no-passive-with-prevent.md`
```markdown
---
title: Never Use .passive and .prevent Together
impact: HIGH
impactDescription: Conflicting modifiers cause .prevent to be ignored and trigger browser warnings
type: gotcha
tags: [vue3, events, modifiers, scroll, touch, performance]
---

# Never Use .passive and .prevent Together

**Impact: HIGH** - The `.passive` modifier tells the browser you will NOT call `preventDefault()`, while `.prevent` does exactly that. Using them together causes `.prevent` to be ignored and triggers browser console warnings. This is a logical contradiction that leads to broken event handling.

## Task Checklist

- [ ] Never combine `.passive` and `.prevent` on the same event
- [ ] Use `.passive` for scroll/touch events where you want better performance
- [ ] Use `.prevent` when you need to stop the default browser action
- [ ] If you need conditional prevention, handle it in JavaScript without `.passive`

**Incorrect:**
```html
<!-- WRONG: Conflicting modifiers -->
<template>
  <div @scroll.passive.prevent="handleScroll">
    <!-- .prevent will be IGNORED -->
    <!-- Browser shows warning -->
  </div>
</template>
```

```html
<!-- WRONG: On touch events -->
<template>
  <div @touchstart.passive.prevent="handleTouch">
    <!-- Cannot prevent default - passive already promised not to -->
  </div>
</template>
```

```html
<!-- WRONG: On wheel events -->
<template>
  <div @wheel.passive.prevent="handleWheel">
    <!-- Broken: will scroll anyway despite .prevent -->
  </div>
</template>
```

**Correct:**
```html
<!-- CORRECT: Use .passive for performance (no prevention needed) -->
<template>
  <div @scroll.passive="handleScroll">
    <!-- Good for scroll tracking without blocking -->
  </div>
</template>
```

```html
<!-- CORRECT: Use .prevent when you need to prevent default -->
<template>
  <form @submit.prevent="handleSubmit">
    <!-- Correctly prevents form submission -->
  </form>
</template>
```

```html
<!-- CORRECT: For touch events where you need to prevent -->
<template>
  <div @touchmove="handleTouchMove">
    <!-- Handle prevention conditionally in JS -->
  </div>
</template>

<script setup>
function handleTouchMove(event) {
  if (shouldPreventScroll.value) {
    event.preventDefault()
  }
  // ... handle touch
}
</script>
```

## Understanding .passive

```javascript
// .passive tells the browser:
// "I promise I won't call preventDefault()"

// This allows the browser to:
// 1. Start scrolling immediately without waiting for JS
// 2. Improve scroll performance, especially on mobile
// 3. Reduce jank and stuttering

// Equivalent to:
element.addEventListener('scroll', handler, { passive: true })
```

## When to Use .passive

```html
<!-- Good use cases for .passive -->

<!-- Scroll tracking analytics -->
<div @scroll.passive="trackScrollPosition">

<!-- Touch gesture detection (no prevention needed) -->
<div @touchmove.passive="detectGesture">

<!-- Wheel event monitoring -->
<div @wheel.passive="monitorWheel">
```

## When to Use .prevent (Without .passive)

```html
<!-- Good use cases for .prevent -->

<!-- Form submission -->
<form @submit.prevent="handleSubmit">

<!-- Link clicks with custom navigation -->
<a @click.prevent="navigate">

<!-- Preventing context menu -->
<div @contextmenu.prevent="showCustomMenu">
```

## Browser Warning

When you combine `.passive` and `.prevent`, the browser console shows:
```
[Intervention] Unable to preventDefault inside passive event listener
due to target being treated as passive.
```

## Reference
- [Vue.js Event Handling - Event Modifiers](https://vuejs.org/guide/essentials/event-handling.html#event-modifiers)
- [MDN - Improving scroll performance with passive listeners](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#improving_scrolling_performance_with_passive_listeners)
```

## File: `skills/vue-debug-guides/reference/no-v-if-with-v-for.md`
```markdown
---
title: Never Use v-if and v-for on the Same Element
impact: HIGH
impactDescription: Causes confusing precedence issues and Vue 2 to 3 migration bugs
type: capability
tags: [vue3, v-if, v-for, conditional-rendering, list-rendering, eslint]
---

# Never Use v-if and v-for on the Same Element

**Impact: HIGH** - Using `v-if` and `v-for` on the same element creates ambiguous precedence that differs between Vue 2 and Vue 3. In Vue 2, `v-for` had higher precedence; in Vue 3, `v-if` has higher precedence. This breaking change causes subtle bugs during migration and makes code intent unclear.

The ESLint rule `vue/no-use-v-if-with-v-for` enforces this best practice.

## Task Checklist

- [ ] Never place v-if and v-for on the same element
- [ ] For filtering list items: use a computed property that filters the array
- [ ] For hiding entire list: wrap with `<template v-if>` around the v-for
- [ ] Enable eslint-plugin-vue rule `vue/no-use-v-if-with-v-for`

**Incorrect:**
```html
<!-- WRONG: v-if and v-for on same element - ambiguous precedence -->
<template>
  <!-- Intent: show only active users -->
  <li v-for="user in users" v-if="user.isActive" :key="user.id">
    {{ user.name }}
  </li>
</template>
```

```html
<!-- WRONG: Hiding entire list conditionally -->
<template>
  <li v-for="user in users" v-if="shouldShowList" :key="user.id">
    {{ user.name }}
  </li>
</template>
```

```html
<!-- WRONG: Vue 3 precedence issue -->
<template>
  <!-- In Vue 3, v-if runs FIRST, so 'user' is undefined! -->
  <li v-for="user in users" v-if="user.isActive" :key="user.id">
    {{ user.name }}
  </li>
  <!-- Error: Cannot read property 'isActive' of undefined -->
</template>
```

**Correct:**
```html
<!-- CORRECT: Filter with computed property -->
<template>
  <li v-for="user in activeUsers" :key="user.id">
    {{ user.name }}
  </li>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps(['users'])

const activeUsers = computed(() =>
  props.users.filter(user => user.isActive)
)
</script>
```

```html
<!-- CORRECT: Wrap with <template v-if> for conditional list -->
<template>
  <template v-if="shouldShowList">
    <li v-for="user in users" :key="user.id">
      {{ user.name }}
    </li>
  </template>
</template>
```

```html
<!-- CORRECT: v-if inside the loop (per-item condition) -->
<template>
  <ul>
    <template v-for="user in users" :key="user.id">
      <li v-if="user.isActive">
        {{ user.name }}
      </li>
    </template>
  </ul>
</template>
```

## Vue 2 vs Vue 3 Precedence Change

```javascript
// Vue 2: v-for evaluated first
// <li v-for="user in users" v-if="user.isActive">
// Equivalent to: users.forEach(user => { if (user.isActive) render(user) })

// Vue 3: v-if evaluated first
// <li v-for="user in users" v-if="user.isActive">
// Equivalent to: if (user.isActive) users.forEach(user => render(user))
// Problem: 'user' doesn't exist yet when v-if runs!
```

## Why Computed Properties Are Better

```javascript
// Benefits of filtering via computed:
// 1. Clear separation of concerns (logic vs template)
// 2. Cached - only recalculates when dependencies change
// 3. Reusable - can be used elsewhere in component
// 4. Testable - can unit test the filtering logic
// 5. No ambiguity about intent

const activeUsers = computed(() =>
  users.value.filter(u => u.isActive)
)

// Can add more complex filtering
const filteredUsers = computed(() =>
  users.value
    .filter(u => u.isActive)
    .filter(u => u.role === selectedRole.value)
    .sort((a, b) => a.name.localeCompare(b.name))
)
```

## Reference
- [Vue.js Style Guide - Avoid v-if with v-for](https://vuejs.org/style-guide/rules-essential.html#avoid-v-if-with-v-for)
- [Vue 3 Migration Guide - v-if vs v-for Precedence](https://v3-migration.vuejs.org/breaking-changes/v-if-v-for)
- [ESLint Plugin Vue - no-use-v-if-with-v-for](https://eslint.vuejs.org/rules/no-use-v-if-with-v-for)
```

## File: `skills/vue-debug-guides/reference/perf-computed-object-stability.md`
```markdown
---
title: Return Stable Object References from Computed Properties
impact: MEDIUM
impactDescription: Computed properties returning new objects trigger effects even when values haven't meaningfully changed
type: efficiency
tags: [vue3, computed, performance, reactivity, vue3.4]
---

# Return Stable Object References from Computed Properties

**Impact: MEDIUM** - In Vue 3.4+, computed properties only trigger effects when their value changes. However, if a computed returns a new object each time, Vue cannot detect that the values inside are the same. This causes unnecessary effect re-runs.

For primitive values, Vue 3.4+ handles this automatically. For objects, manually compare and return the previous value when nothing meaningful has changed.

## Task Checklist

- [ ] For computed properties returning primitives, Vue 3.4+ handles stability automatically
- [ ] For computed properties returning objects, compare with previous value and return old reference if unchanged
- [ ] Always perform the full computation before comparing (to track dependencies correctly)
- [ ] Consider if you really need to return an object, or if primitives would suffice

**Incorrect:**
```vue
<script setup>
import { ref, computed, watchEffect } from 'vue'

const count = ref(0)

// BAD: Returns new object every time, always triggers effects
const stats = computed(() => {
  return {
    isEven: count.value % 2 === 0,
    doubleValue: count.value * 2
  }
})

watchEffect(() => {
  console.log('Stats changed:', stats.value)
  // Logs on EVERY count change, even when isEven hasn't changed
  // count: 0 -> 2 -> 4: isEven is always true, but effect runs each time
})
</script>
```

**Correct:**
```vue
<script setup>
import { ref, computed, watchEffect } from 'vue'

const count = ref(0)

// GOOD (Vue 3.4+): Primitive computed - automatic stability
const isEven = computed(() => count.value % 2 === 0)

watchEffect(() => {
  console.log('isEven:', isEven.value)
  // Only logs when isEven actually changes (0, 2, 4 won't re-trigger)
})

// GOOD (Vue 3.4+): Manual comparison for object returns
const stats = computed((oldValue) => {
  // Step 1: Always compute the new value first (to track dependencies)
  const newValue = {
    isEven: count.value % 2 === 0,
    category: count.value < 10 ? 'small' : 'large'
  }

  // Step 2: Compare with previous value
  if (oldValue &&
      oldValue.isEven === newValue.isEven &&
      oldValue.category === newValue.category) {
    return oldValue  // Return old reference - no effect triggers
  }

  return newValue
})

watchEffect(() => {
  console.log('Stats changed:', stats.value)
  // Now only logs when isEven or category actually changes
})
</script>
```

## Primitive vs Object Computed Behavior (Vue 3.4+)

```javascript
import { ref, computed, watchEffect } from 'vue'

const count = ref(0)

// PRIMITIVE: Vue automatically detects value hasn't changed
const isEven = computed(() => count.value % 2 === 0)

watchEffect(() => console.log(isEven.value))  // true

count.value = 2  // isEven still true - NO log
count.value = 4  // isEven still true - NO log
count.value = 3  // isEven now false - logs: false

// OBJECT: New reference every time (without manual comparison)
const obj = computed(() => ({ isEven: count.value % 2 === 0 }))

watchEffect(() => console.log(obj.value))  // { isEven: true }

count.value = 2  // Logs again! New object reference
count.value = 4  // Logs again! New object reference
```

## Advanced: Deep Object Comparison

```javascript
import { ref, computed } from 'vue'
import { isEqual } from 'lodash-es'  // For deep comparison

const filters = ref({ category: 'all', sortBy: 'date', page: 1 })

// For complex objects, use deep comparison
const activeFilters = computed((oldValue) => {
  const newValue = {
    ...filters.value,
    hasFilters: filters.value.category !== 'all' || filters.value.sortBy !== 'date'
  }

  // Deep compare for complex objects
  if (oldValue && isEqual(oldValue, newValue)) {
    return oldValue
  }

  return newValue
})
```

## Important: Always Compute Before Comparing

```javascript
// BAD: Early return prevents dependency tracking
const optimized = computed((oldValue) => {
  if (oldValue && someCondition) {
    return oldValue  // Dependencies not tracked!
  }
  return computeExpensiveValue()
})

// GOOD: Compute first, then compare
const optimized = computed((oldValue) => {
  const newValue = computeExpensiveValue()  // Always track dependencies
  if (oldValue && newValue === oldValue) {
    return oldValue
  }
  return newValue
})
```

## Reference
- [Vue.js Performance - Computed Stability](https://vuejs.org/guide/best-practices/performance.html#computed-stability)
- [Vue.js Computed Properties](https://vuejs.org/guide/essentials/computed.html)
```

## File: `skills/vue-debug-guides/reference/perf-props-stability-update-optimization.md`
```markdown
---
title: Keep Props Stable to Minimize Child Re-renders
impact: HIGH
impactDescription: Passing changing props to list items causes ALL children to re-render unnecessarily
type: efficiency
tags: [vue3, performance, props, v-for, re-renders, optimization]
---

# Keep Props Stable to Minimize Child Re-renders

**Impact: HIGH** - When props passed to child components change, Vue must re-render those components. Passing derived values like `activeId` to every list item causes all items to re-render when activeId changes, even if only one item's active state actually changed.

Move comparison logic to the parent and pass the boolean result instead. This is one of the most impactful update performance optimizations in Vue.

## Task Checklist

- [ ] Avoid passing parent-level state that all children compare against (like `activeId`)
- [ ] Pre-compute derived boolean props in the parent (like `:active="item.id === activeId"`)
- [ ] Profile re-renders using Vue DevTools to identify prop stability issues
- [ ] Consider this pattern especially critical for large lists

**Incorrect:**
```vue
<template>
  <!-- BAD: activeId changes -> ALL 100 ListItems re-render -->
  <ListItem
    v-for="item in list"
    :key="item.id"
    :id="item.id"
    :active-id="activeId"
  />
</template>

<script setup>
import { ref } from 'vue'

const list = ref([/* 100 items */])
const activeId = ref(null)

// When activeId changes from 1 to 2:
// - ListItem 1 needs to re-render (was active, now not)
// - ListItem 2 needs to re-render (was not active, now active)
// - All other 98 ListItems ALSO re-render because activeId prop changed!
</script>
```

```vue
<!-- ListItem.vue - receives activeId and compares internally -->
<template>
  <div :class="{ active: id === activeId }">
    {{ id }}
  </div>
</template>

<script setup>
defineProps({
  id: Number,
  activeId: Number  // This prop changes for ALL items
})
</script>
```

**Correct:**
```vue
<template>
  <!-- GOOD: Only items whose :active actually changed will re-render -->
  <ListItem
    v-for="item in list"
    :key="item.id"
    :id="item.id"
    :active="item.id === activeId"
  />
</template>

<script setup>
import { ref } from 'vue'

const list = ref([/* 100 items */])
const activeId = ref(null)

// When activeId changes from 1 to 2:
// - ListItem 1: :active changed from true to false -> re-renders
// - ListItem 2: :active changed from false to true -> re-renders
// - All other 98 ListItems: :active is still false -> NO re-render!
</script>
```

```vue
<!-- ListItem.vue - receives pre-computed boolean -->
<template>
  <div :class="{ active }">
    {{ id }}
  </div>
</template>

<script setup>
defineProps({
  id: Number,
  active: Boolean  // This only changes for items that truly changed
})
</script>
```

## Common Patterns That Cause Prop Instability

```vue
<!-- BAD: Passing index that could shift -->
<Item
  v-for="(item, index) in items"
  :key="item.id"
  :index="index"
  :total="items.length"  <!-- Changes when list changes -->
/>

<!-- BAD: Passing entire selection set -->
<Item
  v-for="item in items"
  :key="item.id"
  :selected-ids="selectedIds"  <!-- All items re-render on any selection -->
/>

<!-- GOOD: Pre-compute the boolean -->
<Item
  v-for="item in items"
  :key="item.id"
  :selected="selectedIds.includes(item.id)"
/>
```

## Performance Impact Example

| Scenario | Props Changed | Components Re-rendered |
|----------|---------------|------------------------|
| 100 items, pass `activeId` | 100 | 100 (all) |
| 100 items, pass `:active` boolean | 2 | 2 (only changed) |
| 1000 items, pass `activeId` | 1000 | 1000 (all) |
| 1000 items, pass `:active` boolean | 2 | 2 (only changed) |

## Reference
- [Vue.js Performance - Props Stability](https://vuejs.org/guide/best-practices/performance.html#props-stability)
```

## File: `skills/vue-debug-guides/reference/plugin-global-properties-sparingly.md`
```markdown
# Use Global Properties Sparingly in Plugins

## Rule

When using `app.config.globalProperties` in Vue plugins, use them sparingly and with clear naming conventions. Excessive global properties lead to confusion, naming conflicts, and debugging difficulties.

## Why This Matters

1. **Implicit dependencies**: Global properties make component dependencies invisible, making code harder to understand and maintain.

2. **Naming collisions**: Multiple plugins may try to use the same property name (e.g., `$http`, `$api`), causing silent overwrites.

3. **Debugging difficulty**: When issues arise, tracing back to which plugin provides a global property is challenging.

4. **IDE limitations**: Global properties may not have proper autocomplete or type checking without careful configuration.

5. **Testing complexity**: Global state is harder to mock and isolate in unit tests.

## Bad Practice

```typescript
// Too many global properties from various plugins
app.config.globalProperties.$http = axios
app.config.globalProperties.$api = apiClient
app.config.globalProperties.$auth = authService
app.config.globalProperties.$translate = i18n.translate
app.config.globalProperties.$format = formatters
app.config.globalProperties.$utils = utilities
app.config.globalProperties.$config = appConfig
app.config.globalProperties.$logger = logger

// In component - where did all these come from?
export default {
  mounted() {
    this.$logger.info('Mounted')
    const data = await this.$http.get(this.$config.apiUrl)
    this.$api.process(this.$utils.transform(data))
  }
}
```

## Good Practice

```typescript
// Use provide/inject for most functionality
export default {
  install(app, options) {
    // Provide services via injection
    app.provide('api', apiClient)
    app.provide('auth', authService)
    app.provide('i18n', i18n)

    // Reserve globalProperties for truly global template helpers
    // that are used extensively in templates across the app
    app.config.globalProperties.$t = i18n.translate  // Common convention
  }
}

// In component - explicit dependencies
<script setup>
import { inject } from 'vue'

const api = inject('api')
const auth = inject('auth')
</script>

<template>
  <!-- $t is acceptable for common template-only usage -->
  <h1>{{ $t('welcome') }}</h1>
</template>
```

## Naming Conventions

If you do use globalProperties:

1. **Use `$` prefix**: This is the Vue convention and avoids conflicts with component data/methods
2. **Use unique prefixes for your library**: e.g., `$myLib_translate` for third-party plugins
3. **Document all global properties**: Keep a central registry of what each plugin provides

```typescript
// Good: namespaced to avoid conflicts
app.config.globalProperties.$myPlugin = {
  translate: (key) => /* ... */,
  format: (value) => /* ... */
}

// Usage
{{ $myPlugin.translate('key') }}
```

## Auditing Global Properties

You can inspect all global properties for debugging:

```typescript
console.log(app.config.globalProperties)
```

## When Global Properties Are Acceptable

1. **Template-only utilities** used very frequently (like `$t` for translations)
2. **Legacy migration** when transitioning from Vue 2
3. **Libraries that need Options API compatibility** (but prefer also providing inject)

## References

- [Vue.js Plugins Documentation](https://vuejs.org/guide/reusability/plugins.html)
- [Vue.js Global Properties](https://vuejs.org/api/application.html#app-config-globalproperties)
```

## File: `skills/vue-debug-guides/reference/plugin-install-before-mount.md`
```markdown
# Install Plugins Before Mounting the App

## Rule

All plugins must be installed using `app.use()` BEFORE calling `app.mount()`. Installing plugins after the app is mounted can lead to reactivity issues, missing dependencies, and unexpected behavior.

## Why This Matters

1. **Hidden dependencies**: Components may render before plugins they depend on are available, causing runtime errors.

2. **Reactivity issues**: Late plugin installation can cause subtle reactivity problems where provided values aren't properly reactive.

3. **Initialization order**: Many plugins (like vue-router, pinia) need to set up state before any component renders.

4. **Ecosystem complexity**: Adding plugins after mount can cause issues with Vue's internal ecosystem and hydration in SSR scenarios.

## Bad Practice

```typescript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import i18nPlugin from './plugins/i18n'

const app = createApp(App)

// Mounting first - plugins not yet available!
app.mount('#app')

// Installing after mount - TOO LATE!
app.use(router)
app.use(i18nPlugin, { locale: 'en' })
```

## Good Practice

```typescript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import i18nPlugin from './plugins/i18n'

const app = createApp(App)

// Install all plugins BEFORE mounting
app.use(createPinia())
app.use(router)
app.use(i18nPlugin, { locale: 'en' })

// Mount LAST
app.mount('#app')
```

## Plugin Installation Order

The order of `app.use()` calls can matter when plugins depend on each other:

```typescript
const app = createApp(App)

// 1. State management first (other plugins might need it)
app.use(createPinia())

// 2. Router (may depend on state)
app.use(router)

// 3. Other plugins (may depend on router or state)
app.use(authPlugin)
app.use(i18nPlugin, { locale: 'en' })

// 4. Mount last
app.mount('#app')
```

## Async Plugin Installation

If you need to perform async operations before mounting:

```typescript
import { createApp } from 'vue'
import App from './App.vue'
import { loadPlugins } from './plugins'

async function bootstrap() {
  const app = createApp(App)

  // Await async plugin setup
  const i18nPlugin = await loadI18nMessages()

  // Install all plugins
  app.use(i18nPlugin)

  // Mount after everything is ready
  app.mount('#app')
}

bootstrap()
```

## Duplicate Installation Protection

Vue's `app.use()` automatically prevents duplicate plugin installation:

```typescript
app.use(myPlugin)
app.use(myPlugin) // This second call is ignored - no double installation

// This is handled internally by Vue, providing a safety net
```

## Common Symptoms of Late Plugin Installation

- `inject()` returns `undefined` unexpectedly
- Router navigation guards not firing
- Store state not reactive
- Template errors about undefined global properties
- Hydration mismatches in SSR

## References

- [Vue.js Plugins Documentation](https://vuejs.org/guide/reusability/plugins.html)
- [Vue.js Application API](https://vuejs.org/api/application.html)
- [Vue 3 Migration Guide - Global API](https://v3-migration.vuejs.org/breaking-changes/global-api.html)
```

## File: `skills/vue-debug-guides/reference/plugin-prefer-provide-inject-over-global-properties.md`
```markdown
# Prefer provide/inject Over Global Properties in Plugins

## Rule

When creating Vue plugins, prefer using `app.provide()` to make plugin functionality available to components instead of attaching properties to `app.config.globalProperties`.

## Why This Matters

1. **globalProperties don't work in setup()**: Properties attached to `globalProperties` are only accessible via `this` in Options API. They are NOT available in the Composition API's `setup()` function.

2. **Type safety**: `provide/inject` integrates better with TypeScript and requires less type augmentation boilerplate.

3. **Testability**: Injected dependencies are easier to mock in tests compared to global properties.

4. **Code clarity**: Explicit `inject()` calls make dependencies visible, while global properties can appear "magic".

5. **Scoping**: `provide/inject` follows Vue's component hierarchy, making it easier to provide different values to different parts of your app.

## Bad Practice

```typescript
// plugins/i18n.ts
export default {
  install(app, options) {
    // Attaching to globalProperties - only works with Options API
    app.config.globalProperties.$translate = (key: string) => {
      return key.split('.').reduce((o, i) => o?.[i], options)
    }
  }
}

// In component - requires type augmentation for TypeScript
// Also DOES NOT work in <script setup>
export default {
  mounted() {
    console.log(this.$translate('greeting.hello'))
  }
}
```

## Good Practice

```typescript
// plugins/i18n.ts
import type { InjectionKey, App } from 'vue'

export interface I18nOptions {
  [key: string]: string | I18nOptions
}

export interface I18n {
  translate: (key: string) => string
  options: I18nOptions
}

export const i18nKey: InjectionKey<I18n> = Symbol('i18n')

export default {
  install(app: App, options: I18nOptions) {
    const translate = (key: string): string => {
      return key.split('.').reduce((o, i) => o?.[i], options) as string ?? key
    }

    // Use provide for Composition API compatibility
    app.provide(i18nKey, { translate, options })
  }
}

// In component - works in setup() and has full type safety
<script setup lang="ts">
import { inject } from 'vue'
import { i18nKey } from '@/plugins/i18n'

const i18n = inject(i18nKey)
console.log(i18n?.translate('greeting.hello'))
</script>
```

## Hybrid Approach

If you must support both APIs (e.g., for backwards compatibility), provide both:

```typescript
export default {
  install(app: App, options: I18nOptions) {
    const i18n = {
      translate: (key: string) => /* ... */
    }

    // For Composition API
    app.provide(i18nKey, i18n)

    // For Options API (use sparingly)
    app.config.globalProperties.$i18n = i18n
  }
}
```

## TypeScript Type Augmentation (if using globalProperties)

If you must use globalProperties, you need proper type augmentation:

```typescript
// types/vue.d.ts
export {}

declare module 'vue' {
  interface ComponentCustomProperties {
    $translate: (key: string) => string
  }
}
```

**Important**: The file MUST contain `export {}` or another top-level export/import. Without it, the augmentation will OVERWRITE types instead of augmenting them.

## References

- [Vue.js Plugins Documentation](https://vuejs.org/guide/reusability/plugins.html)
- [Vue.js Provide/Inject](https://vuejs.org/guide/components/provide-inject.html)
- [TypeScript with Options API](https://vuejs.org/guide/typescript/options-api.html)
```

## File: `skills/vue-debug-guides/reference/plugin-typescript-type-augmentation.md`
```markdown
# Proper TypeScript Type Augmentation for Plugins

## Rule

When creating Vue plugins that add global properties, you MUST properly augment TypeScript types. The augmentation file MUST contain at least one top-level `import` or `export` statement to be treated as a module.

## Why This Matters

1. **Without module syntax, types are overwritten**: If your augmentation file isn't a module, it will OVERWRITE Vue's types instead of augmenting them, breaking type checking for the entire application.

2. **Type safety**: Proper augmentation enables autocomplete and type checking for plugin-provided properties.

3. **IDE support**: Developers get proper IntelliSense for global properties like `this.$translate`.

4. **Error prevention**: Catch typos and incorrect usage at compile time rather than runtime.

## Critical Rule: Module Syntax Required

```typescript
// BAD - This OVERWRITES Vue types instead of augmenting!
// types/vue.d.ts
declare module 'vue' {
  interface ComponentCustomProperties {
    $translate: (key: string) => string
  }
}

// GOOD - The export {} makes this a module, so it AUGMENTS types
// types/vue.d.ts
export {}  // This line is CRITICAL!

declare module 'vue' {
  interface ComponentCustomProperties {
    $translate: (key: string) => string
  }
}
```

## Complete Plugin Type Augmentation Example

```typescript
// plugins/i18n.ts
import type { App, InjectionKey } from 'vue'

export interface I18nOptions {
  locale: string
  messages: Record<string, Record<string, string>>
}

export interface I18nInstance {
  translate: (key: string) => string
  locale: string
}

export const i18nInjectionKey: InjectionKey<I18nInstance> = Symbol('i18n')

export function createI18n(options: I18nOptions) {
  const i18n: I18nInstance = {
    translate(key: string) {
      return options.messages[options.locale]?.[key] ?? key
    },
    locale: options.locale
  }

  return {
    install(app: App) {
      // For Composition API
      app.provide(i18nInjectionKey, i18n)

      // For Options API / templates
      app.config.globalProperties.$t = i18n.translate
      app.config.globalProperties.$i18n = i18n
    }
  }
}

// types/i18n.d.ts (or in the same file after export)
export {}

declare module 'vue' {
  interface ComponentCustomProperties {
    $t: (key: string) => string
    $i18n: I18nInstance
  }
}
```

## Alternative: Augment @vue/runtime-core

Some plugins augment `@vue/runtime-core` instead of `vue`:

```typescript
// types/global.d.ts
export {}

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $myPlugin: MyPluginInstance
  }
}
```

Both approaches work, but `'vue'` is more common in application code.

## Ensure tsconfig.json Includes the Declaration File

```json
{
  "compilerOptions": {
    // ...
  },
  "include": [
    "src/**/*.ts",
    "src/**/*.vue",
    "types/**/*.d.ts"  // Include your declaration files
  ]
}
```

## For Library Authors: package.json Types Field

If publishing a plugin as a package:

```json
{
  "name": "my-vue-plugin",
  "types": "./dist/types/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/types/index.d.ts",
      "import": "./dist/index.mjs"
    }
  }
}
```

## Common Errors and Solutions

### Error: Property '$xyz' does not exist on type

1. Check that your `.d.ts` file has `export {}` or an import statement
2. Verify the file is included in `tsconfig.json`
3. Restart your TypeScript language server (VS Code: Cmd+Shift+P > "Restart TS Server")

### Error: Types work in some components but not others

This often happens when using Vetur instead of Volar. If you're on Vue 3, switch to Volar (Vue - Official extension).

### Error in Options API but not Composition API

Global properties on `this` require proper augmentation of `ComponentCustomProperties`. The Composition API uses `inject()` which is typed separately.

## References

- [Vue.js TypeScript with Options API](https://vuejs.org/guide/typescript/options-api.html)
- [TypeScript Module Augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation)
- [Vue.js Plugins Documentation](https://vuejs.org/guide/reusability/plugins.html)
```

## File: `skills/vue-debug-guides/reference/prop-defineprops-scope-limitation.md`
```markdown
---
title: defineProps Cannot Access Variables from script setup
impact: MEDIUM
impactDescription: Variables declared in script setup are not accessible inside defineProps arguments
type: gotcha
tags: [vue3, props, script-setup, defineProps, compiler]
---

# defineProps Cannot Access Variables from script setup

**Impact: MEDIUM** - Code inside the `defineProps()` argument cannot access other variables declared in `<script setup>`. The entire expression is moved to an outer function scope when compiled, making local variables inaccessible.

This commonly surprises developers trying to use imported constants or computed validation logic.

## Task Checklist

- [ ] Define validation constants outside `<script setup>` or in a separate file
- [ ] Import constants before using them in defineProps
- [ ] Use external type definitions for TypeScript props
- [ ] For dynamic validation, use watchers instead of prop validators

**Incorrect:**
```vue
<script setup>
import { ref } from 'vue'

// These are in <script setup> scope
const VALID_SIZES = ['sm', 'md', 'lg']
const maxLength = ref(100)

defineProps({
  size: {
    type: String,
    // WRONG: VALID_SIZES is not accessible here
    validator: (v) => VALID_SIZES.includes(v)  // ReferenceError!
  },
  name: {
    type: String,
    // WRONG: Cannot access refs
    validator: (v) => v.length <= maxLength.value  // ReferenceError!
  }
})
</script>
```

**Correct:**
```vue
<script>
// Define constants in regular <script> block (module scope)
export const VALID_SIZES = ['sm', 'md', 'lg']
export const MAX_LENGTH = 100
</script>

<script setup>
// Now accessible in defineProps
defineProps({
  size: {
    type: String,
    validator: (v) => VALID_SIZES.includes(v)  // Works!
  },
  name: {
    type: String,
    validator: (v) => v.length <= MAX_LENGTH  // Works!
  }
})
</script>
```

## Pattern: Import from External File

```javascript
// validation.js
export const VALID_SIZES = ['sm', 'md', 'lg']
export const VALID_COLORS = ['red', 'blue', 'green']
export const sizeValidator = (v) => VALID_SIZES.includes(v)
```

```vue
<script setup>
import { VALID_SIZES, VALID_COLORS, sizeValidator } from './validation'

// Imported values ARE accessible
defineProps({
  size: {
    type: String,
    validator: sizeValidator
  },
  color: {
    type: String,
    validator: (v) => VALID_COLORS.includes(v)
  }
})
</script>
```

## Pattern: Dual Script Blocks

```vue
<script>
// Regular script for module-level declarations
const options = {
  themes: ['light', 'dark', 'system'],
  defaults: {
    theme: 'light',
    size: 'md'
  }
}
</script>

<script setup>
// options is accessible here
const props = defineProps({
  theme: {
    type: String,
    default: options.defaults.theme,
    validator: (v) => options.themes.includes(v)
  }
})
</script>
```

## TypeScript: External Type Definitions

```typescript
// types.ts
export interface UserProps {
  name: string
  email: string
  age?: number
}
```

```vue
<script setup lang="ts">
import type { UserProps } from './types'

// Type imports work fine
const props = defineProps<UserProps>()
</script>
```

## Why This Happens

Vue's compiler transforms `<script setup>` code. The `defineProps()` call is extracted and moved to component options at compile time, before the setup function runs:

```javascript
// Your code:
const MY_CONST = 'value'
defineProps({ prop: { default: MY_CONST } })

// Compiled (simplified):
export default {
  props: { prop: { default: MY_CONST } },  // MY_CONST doesn't exist here!
  setup() {
    const MY_CONST = 'value'  // Defined too late
  }
}
```

## Reference
- [Vue.js Script Setup - defineProps](https://vuejs.org/api/sfc-script-setup.html#defineprops-defineemits)
```

## File: `skills/vue-debug-guides/reference/provide-inject-debugging-challenges.md`
```markdown
---
title: Provide/Inject Has Limited DevTools Support - Plan for Debugging
impact: LOW
impactDescription: Unlike props and state, provided values are harder to trace in Vue DevTools, making debugging more challenging
type: gotcha
tags: [vue3, provide-inject, debugging, devtools, architecture]
---

# Provide/Inject Has Limited DevTools Support - Plan for Debugging

**Impact: LOW** - While provide/inject is powerful for avoiding prop drilling, it creates less visible data flow than props. Provided values are not as easily inspectable in Vue DevTools, and tracing where a value comes from requires navigating the component tree manually.

## Task Checklist

- [ ] Document provided values at the provider component level
- [ ] Use descriptive Symbol descriptions for easier identification
- [ ] Consider adding development-only logging for provided state changes
- [ ] Keep provide/inject chains shallow when possible
- [ ] Prefer Pinia for complex state that needs DevTools integration

## The Challenge

Unlike props which are clearly visible in Vue DevTools for each component, provided values:

1. Don't show which ancestor provided them
2. Require manual navigation to find the provider
3. Don't show in the standard props/data panels
4. Can be shadowed by closer ancestors using the same key

## Strategies for Better Debugging

### 1. Use Descriptive Symbol Names

```js
// injection-keys.js

// BETTER: Descriptive names appear in errors and debugging
export const UserAuthKey = Symbol('UserAuthenticationState')
export const ThemeConfigKey = Symbol('ThemeConfiguration')
export const FormContextKey = Symbol('FormValidationContext')

// WORSE: Generic names are harder to trace
export const UserKey = Symbol()
export const ThemeKey = Symbol('theme')
```

### 2. Document Providers Clearly

```vue
<!-- AuthProvider.vue -->
<script setup>
/**
 * Authentication Provider
 *
 * Provides:
 * - UserAuthKey: Current user state (Ref<User | null>)
 * - AuthActionsKey: { login, logout, refresh }
 *
 * Must wrap any component that needs authentication state.
 */
import { provide, ref, readonly } from 'vue'
import { UserAuthKey, AuthActionsKey } from '@/injection-keys'

const user = ref(null)

// ... implementation

provide(UserAuthKey, readonly(user))
provide(AuthActionsKey, { login, logout, refresh })
</script>
```

### 3. Development-Only Logging

```js
// composables/useProvideWithLogging.js
import { provide, watch, getCurrentInstance } from 'vue'

export function useProvideWithLogging(key, value, name) {
  provide(key, value)

  if (import.meta.env.DEV) {
    const instance = getCurrentInstance()
    const componentName = instance?.type?.name || 'Unknown'

    console.log(`[Provide] ${name} provided by <${componentName}>`)

    // Log reactive changes
    if (value && typeof value === 'object' && 'value' in value) {
      watch(value, (newVal) => {
        console.log(`[Provide] ${name} changed:`, newVal)
      }, { deep: true })
    }
  }
}
```

```vue
<script setup>
import { ref } from 'vue'
import { useProvideWithLogging } from '@/composables/useProvideWithLogging'
import { ThemeKey } from '@/injection-keys'

const theme = ref('dark')

// In development, logs when provided and when changed
useProvideWithLogging(ThemeKey, theme, 'Theme')
</script>
```

### 4. Inject with Missing Provider Warnings

```js
// composables/useSafeInject.js
import { inject, getCurrentInstance } from 'vue'

export function useSafeInject(key, fallback, keyName) {
  const value = inject(key, undefined)

  if (value === undefined) {
    const instance = getCurrentInstance()
    const componentName = instance?.type?.name || 'Unknown'

    if (import.meta.env.DEV) {
      console.warn(
        `[Inject] ${keyName || String(key)} not provided. ` +
        `Component <${componentName}> is using fallback value. ` +
        `Ensure a provider exists in the ancestor chain.`
      )
    }

    return typeof fallback === 'function' ? fallback() : fallback
  }

  return value
}
```

```vue
<script setup>
import { useSafeInject } from '@/composables/useSafeInject'
import { ThemeKey } from '@/injection-keys'

// Warns in dev if no provider found
const theme = useSafeInject(ThemeKey, () => ({ mode: 'light' }), 'ThemeConfig')
</script>
```

### 5. Create Provider Registry for Complex Apps

```js
// utils/provider-registry.js
const providerRegistry = new Map()

export function registerProvider(key, componentName, value) {
  if (import.meta.env.DEV) {
    providerRegistry.set(key, {
      componentName,
      value,
      timestamp: Date.now()
    })
  }
}

export function getProviderInfo(key) {
  return providerRegistry.get(key)
}

// For DevTools custom plugin or debugging
export function getAllProviders() {
  return Object.fromEntries(providerRegistry)
}

// Expose to window for console debugging
if (import.meta.env.DEV) {
  window.__VUE_PROVIDERS__ = {
    getAll: getAllProviders,
    get: getProviderInfo
  }
}
```

## When to Use Pinia Instead

If you find yourself needing extensive debugging for state:

| Use Provide/Inject | Use Pinia |
|-------------------|-----------|
| Component library internals | Application-wide state |
| Theme/locale configuration | User session data |
| Form context | Shopping cart |
| Simple parent-child sharing | Complex state with actions |
| Plugin configuration | State that needs time-travel debugging |

Pinia provides excellent DevTools integration with:
- State inspection
- Time-travel debugging
- Action logging
- Hot module replacement

## Reference
- [Vue DevTools](https://devtools.vuejs.org/)
- [Pinia DevTools](https://pinia.vuejs.org/core-concepts/index.html#devtools)
```

## File: `skills/vue-debug-guides/reference/provide-inject-default-value-factory.md`
```markdown
---
title: Use Factory Functions for Non-Primitive Inject Default Values
impact: MEDIUM
impactDescription: Using object literals as default values creates shared references across all consuming components
type: gotcha
tags: [vue3, provide-inject, composition-api, memory, shared-state]
---

# Use Factory Functions for Non-Primitive Inject Default Values

**Impact: MEDIUM** - When providing default values for `inject()`, using an object literal creates a single shared reference. All components using that default will share the same object, leading to unexpected state sharing and bugs.

## Task Checklist

- [ ] Always use factory functions for object/array default values in inject
- [ ] Pass `true` as the third argument to enable factory mode in Composition API
- [ ] Use the object syntax with factory function in Options API
- [ ] Only use literal defaults for primitive values (strings, numbers, booleans)

## The Gotcha: Shared Default References

**Wrong - Object literal creates shared reference:**
```vue
<script setup>
import { inject } from 'vue'

// WRONG: All components without a provider share this SAME object
const config = inject('config', { debug: false, apiUrl: '' })

// If one component does this:
config.debug = true

// ALL other components using this default now have debug: true!
</script>
```

**Correct - Factory function creates unique instance:**
```vue
<script setup>
import { inject } from 'vue'

// CORRECT: Each component gets its own object
// Third argument `true` indicates the second arg is a factory function
const config = inject('config', () => ({ debug: false, apiUrl: '' }), true)
</script>
```

## API Explanation

The `inject()` function has multiple signatures:

```ts
// Simple default value (OK for primitives)
inject(key, defaultValue)

// Factory function for non-primitives (REQUIRED for objects/arrays)
inject(key, factoryFunction, true)
```

The third argument `true` tells Vue that the second argument is a factory function, not the default value itself.

## Examples

### Primitive Defaults (No Factory Needed)

```vue
<script setup>
import { inject } from 'vue'

// Primitives are safe without factory
const count = inject('count', 0)
const name = inject('name', 'Guest')
const enabled = inject('enabled', false)
</script>
```

### Object Defaults (Factory Required)

```vue
<script setup>
import { inject } from 'vue'

// Objects MUST use factory
const user = inject('user', () => ({
  id: null,
  name: 'Anonymous',
  preferences: {}
}), true)

const settings = inject('settings', () => ({
  theme: 'light',
  language: 'en',
  notifications: true
}), true)
</script>
```

### Array Defaults (Factory Required)

```vue
<script setup>
import { inject } from 'vue'

// Arrays MUST use factory
const items = inject('items', () => [], true)
const permissions = inject('permissions', () => ['read'], true)
</script>
```

### Class Instance Defaults (Factory Required)

```vue
<script setup>
import { inject } from 'vue'
import { Logger } from '@/utils/logger'

// Class instances MUST use factory
const logger = inject('logger', () => new Logger({ level: 'warn' }), true)
</script>
```

## Options API Syntax

In Options API, use the object syntax with a `default` factory function:

```js
export default {
  inject: {
    // Primitive - can use literal
    theme: {
      from: 'theme',
      default: 'light'
    },

    // Object - MUST use factory
    config: {
      from: 'config',
      default: () => ({ debug: false })
    },

    // Array - MUST use factory
    permissions: {
      from: 'permissions',
      default: () => []
    }
  }
}
```

## Real-World Example: Form Context

```vue
<!-- FormProvider.vue -->
<script setup>
import { provide, reactive } from 'vue'

const formContext = reactive({
  values: {},
  errors: {},
  touched: {},
  isSubmitting: false
})

provide('formContext', formContext)
</script>

<!-- FormField.vue (might be used outside FormProvider) -->
<script setup>
import { inject } from 'vue'

// Safe default that won't be shared
const formContext = inject('formContext', () => ({
  values: {},
  errors: {},
  touched: {},
  isSubmitting: false,
  // Mark as standalone mode
  isStandalone: true
}), true)

// Component works both inside and outside FormProvider
</script>
```

## TypeScript: Typing Factory Defaults

```ts
import { inject } from 'vue'
import type { InjectionKey } from 'vue'

interface Config {
  apiUrl: string
  debug: boolean
  features: string[]
}

const ConfigKey: InjectionKey<Config> = Symbol('config')

// TypeScript understands the factory return type
const config = inject(ConfigKey, () => ({
  apiUrl: 'https://api.example.com',
  debug: false,
  features: []
}), true)
```

## Common Mistake in Testing

This gotcha often appears in tests where components are rendered without providers:

```ts
// test.spec.ts
import { mount } from '@vue/test-utils'
import MyComponent from './MyComponent.vue'

// Without provider, all test instances share the wrong default
it('test 1', () => {
  const wrapper = mount(MyComponent)
  wrapper.vm.config.debug = true // Pollutes other tests!
})

it('test 2', () => {
  const wrapper = mount(MyComponent)
  // Might fail because debug is still true from test 1
})
```

**Fix: Use factory functions in the component, or provide in tests:**

```ts
it('test with provider', () => {
  const wrapper = mount(MyComponent, {
    global: {
      provide: {
        config: { debug: false, apiUrl: '' }
      }
    }
  })
})
```

## Reference
- [Vue.js inject() API Reference](https://vuejs.org/api/composition-api-dependency-injection.html#inject)
- [Vue.js Provide/Inject Guide](https://vuejs.org/guide/components/provide-inject.html)
```

## File: `skills/vue-debug-guides/reference/provide-inject-reactivity-not-automatic.md`
```markdown
---
title: Provide/Inject Values Are Not Reactive by Default
impact: HIGH
impactDescription: Provided primitive values lose reactivity, causing injecting components to not update when the source value changes
type: gotcha
tags: [vue3, provide-inject, reactivity, composition-api, options-api]
---

# Provide/Inject Values Are Not Reactive by Default

**Impact: HIGH** - A common misconception is that provide/inject automatically maintains reactivity. By default, provided primitive values are NOT reactive. If the provided value changes in the provider, injecting components will NOT be updated.

## Task Checklist

- [ ] Always wrap primitive values in `ref()` before providing
- [ ] Use `computed()` in Options API `provide()` for reactive data
- [ ] Never destructure refs when providing - pass the ref directly
- [ ] Understand that provided refs are NOT auto-unwrapped in injectors

## The Gotcha: Primitives Lose Reactivity

**Wrong - Primitive loses reactivity:**
```vue
<!-- Provider.vue -->
<script setup>
import { ref, provide } from 'vue'

const count = ref(0)

// WRONG: Providing the unwrapped value loses reactivity
provide('count', count.value) // Provides 0, not a reactive value

function increment() {
  count.value++ // Injector will NOT see this change
}
</script>
```

```vue
<!-- Injector.vue -->
<script setup>
import { inject } from 'vue'

const count = inject('count') // Gets 0, forever static
</script>

<template>
  <!-- This will always show 0 -->
  <div>Count: {{ count }}</div>
</template>
```

**Correct - Provide the ref itself:**
```vue
<!-- Provider.vue -->
<script setup>
import { ref, provide } from 'vue'

const count = ref(0)

// CORRECT: Provide the ref, not the value
provide('count', count)

function increment() {
  count.value++ // Injector WILL see this change
}
</script>
```

```vue
<!-- Injector.vue -->
<script setup>
import { inject } from 'vue'

// The ref is injected as-is, maintaining reactivity
const count = inject('count')
</script>

<template>
  <!-- Access .value in script, auto-unwrapped in template -->
  <div>Count: {{ count }}</div>
</template>
```

## Options API: Use computed() for Reactivity

In Options API, the `provide` option with plain properties is NOT reactive:

**Wrong - Options API without computed:**
```js
export default {
  data() {
    return {
      message: 'Hello'
    }
  },
  // WRONG: This is NOT reactive
  provide() {
    return {
      message: this.message // Provides 'Hello' as a static string
    }
  }
}
```

**Correct - Use computed() in Options API:**
```js
import { computed } from 'vue'

export default {
  data() {
    return {
      message: 'Hello'
    }
  },
  provide() {
    return {
      // CORRECT: Wrap in computed for reactivity
      message: computed(() => this.message)
    }
  }
}
```

## Understanding Ref Behavior in Inject

When you provide a ref, it is injected as-is and NOT auto-unwrapped:

```vue
<!-- Provider.vue -->
<script setup>
import { ref, provide } from 'vue'

const user = ref({ name: 'John' })
provide('user', user)
</script>
```

```vue
<!-- Injector.vue -->
<script setup>
import { inject } from 'vue'

const user = inject('user')

// In script, access with .value
console.log(user.value.name) // 'John'

function updateName(newName) {
  user.value.name = newName // Works, but mutations should be in provider
}
</script>

<template>
  <!-- In template, auto-unwrapped at top level -->
  <div>{{ user.name }}</div>
</template>
```

## Providing Reactive Objects

Reactive objects (created with `reactive()`) maintain reactivity when provided:

```vue
<!-- Provider.vue -->
<script setup>
import { reactive, provide } from 'vue'

const state = reactive({
  count: 0,
  message: 'Hello'
})

provide('state', state)
</script>
```

```vue
<!-- Injector.vue -->
<script setup>
import { inject } from 'vue'

const state = inject('state')
// state.count and state.message are reactive
</script>
```

## Common Mistake: Destructuring Breaks Reactivity

**Wrong - Destructuring provided reactive state:**
```vue
<script setup>
import { inject } from 'vue'

// WRONG: Destructuring loses reactivity
const { count, message } = inject('state')
// count and message are now static values
</script>
```

**Correct - Keep the reference intact:**
```vue
<script setup>
import { inject, toRefs } from 'vue'

const state = inject('state')
// Use state.count and state.message directly

// Or use toRefs if you need destructured reactive refs
const { count, message } = toRefs(state)
</script>
```

## Debugging Tip

If your injected value isn't updating:

1. Check if you provided `ref.value` instead of `ref`
2. Check if you destructured a reactive object
3. In Options API, ensure you used `computed()`
4. Use Vue DevTools to inspect the provided values

## Reference
- [Vue.js Provide/Inject - Working with Reactivity](https://vuejs.org/guide/components/provide-inject.html#working-with-reactivity)
- [How to make provide/inject reactive - LogRocket Blog](https://blog.logrocket.com/how-to-make-provide-inject-reactive/)
- [GitHub Issue: Inject/Provide is not reactive](https://github.com/vuejs/vue/issues/7017)
```

## File: `skills/vue-debug-guides/reference/provide-inject-synchronous-setup.md`
```markdown
---
title: Provide Must Be Called Synchronously During Setup
impact: HIGH
impactDescription: Calling provide() asynchronously or conditionally may fail silently or cause inconsistent injection behavior
type: gotcha
tags: [vue3, provide-inject, composition-api, async, setup]
---

# Provide Must Be Called Synchronously During Setup

**Impact: HIGH** - The `provide()` function must be called synchronously during the component's `setup()` phase. Calling it asynchronously (inside callbacks, promises, or after await) will fail silently, and descendant components will not receive the provided value.

## Task Checklist

- [ ] Always call `provide()` at the top level of `setup()` or `<script setup>`
- [ ] Never call `provide()` inside async callbacks or after await statements
- [ ] For async data, provide a ref first, then update its value later
- [ ] Use immediate `provide()` with reactive containers for dynamic data

## The Gotcha: Async Provide Fails Silently

**Wrong - Provide after async operation:**
```vue
<script setup>
import { provide } from 'vue'

// WRONG: provide() called after await - will NOT work
onMounted(async () => {
  const userData = await fetchUser()
  provide('user', userData) // Silent failure!
})
</script>
```

**Wrong - Provide inside callback:**
```vue
<script setup>
import { provide } from 'vue'

// WRONG: provide() inside callback - will NOT work
setTimeout(() => {
  provide('config', { theme: 'dark' }) // Silent failure!
}, 0)
</script>
```

**Wrong - Provide after await in setup:**
```vue
<script setup>
import { provide } from 'vue'

const response = await fetch('/api/config')
const config = await response.json()

// WRONG: This is after an await, setup context may be lost
provide('config', config) // May not work reliably
</script>
```

## Solution: Provide Synchronously, Update Async

**Correct - Provide ref immediately, update later:**
```vue
<script setup>
import { provide, ref, onMounted } from 'vue'

// Provide immediately with initial value
const user = ref(null)
const isLoading = ref(true)
const error = ref(null)

provide('userState', {
  user,
  isLoading,
  error
})

// Update the ref values asynchronously
onMounted(async () => {
  try {
    const userData = await fetchUser()
    user.value = userData
  } catch (e) {
    error.value = e
  } finally {
    isLoading.value = false
  }
})
</script>
```

```vue
<!-- Consumer component -->
<script setup>
import { inject } from 'vue'

const { user, isLoading, error } = inject('userState')
</script>

<template>
  <div v-if="isLoading">Loading...</div>
  <div v-else-if="error">Error: {{ error.message }}</div>
  <div v-else>Welcome, {{ user?.name }}</div>
</template>
```

## Pattern: Async Data Provider

Create a reusable pattern for async-provided data:

```vue
<!-- AsyncDataProvider.vue -->
<script setup>
import { provide, ref, onMounted, watch } from 'vue'

const props = defineProps({
  fetchFn: {
    type: Function,
    required: true
  },
  provideKey: {
    type: [String, Symbol],
    required: true
  },
  immediate: {
    type: Boolean,
    default: true
  }
})

const data = ref(null)
const isLoading = ref(false)
const error = ref(null)

async function load() {
  isLoading.value = true
  error.value = null

  try {
    data.value = await props.fetchFn()
  } catch (e) {
    error.value = e
  } finally {
    isLoading.value = false
  }
}

// Provide synchronously
provide(props.provideKey, {
  data,
  isLoading,
  error,
  reload: load
})

// Fetch asynchronously
if (props.immediate) {
  onMounted(load)
}
</script>

<template>
  <slot />
</template>
```

Usage:

```vue
<template>
  <AsyncDataProvider
    :fetch-fn="() => api.getUser(userId)"
    provide-key="userData"
  >
    <UserProfile />
  </AsyncDataProvider>
</template>
```

## Why This Happens

Vue's `provide()` relies on the current component instance context, which is only available synchronously during setup. After setup completes:

1. The setup context is cleared
2. `provide()` can't find the current instance
3. The call fails silently (no error thrown)

## Checking for Setup Context

You can verify if setup context is available:

```js
import { getCurrentInstance } from 'vue'

function debugProvide(key, value) {
  const instance = getCurrentInstance()

  if (!instance) {
    console.error(
      `provide() called outside setup context. ` +
      `Key: ${String(key)}. This will fail silently.`
    )
    return
  }

  provide(key, value)
}
```

## App-Level Provide (Exception)

`app.provide()` can be called anytime during app initialization:

```js
// main.js
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// This works - app-level provide
app.provide('appConfig', { version: '1.0.0' })

// Even async is OK at app level before mount
fetchConfig().then(config => {
  app.provide('apiConfig', config)
  app.mount('#app')
})
```

But once the app is mounted, `app.provide()` should not be called.

## Reference
- [Vue.js Composition API - provide()](https://vuejs.org/api/composition-api-dependency-injection.html#provide)
- [Vue.js Provide/Inject Guide](https://vuejs.org/guide/components/provide-inject.html)
```

## File: `skills/vue-debug-guides/reference/reactive-destructuring.md`
```markdown
---
title: Never Destructure reactive() Objects Directly
impact: HIGH
impactDescription: Destructuring reactive objects breaks reactivity - changes won't trigger updates
type: capability
tags: [vue3, reactivity, reactive, composition-api, destructuring]
---

# Never Destructure reactive() Objects Directly

**Impact: HIGH** - Destructuring a `reactive()` object breaks the reactive connection. Updates to destructured variables won't trigger UI updates, leading to stale data display.

Vue's `reactive()` uses JavaScript Proxies to track property access. When you destructure, you extract primitive values from the proxy, losing the reactive connection. This is especially dangerous when destructuring from composables or imported state.

## Task Checklist

- [ ] Never destructure reactive objects directly if you need reactivity
- [ ] Use `toRefs()` to convert reactive object properties to refs before destructuring
- [ ] Consider using `ref()` instead of `reactive()` to avoid this pitfall entirely
- [ ] When importing state from composables, check if it's reactive before destructuring

**Incorrect:**
```javascript
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  name: 'Vue'
})

// WRONG: Destructuring breaks reactivity
const { count, name } = state

// These updates work on the original state...
state.count++  // state.count is now 1

// ...but the destructured variables are NOT updated
console.log(count)  // Still 0! Lost reactivity
```

```javascript
// WRONG: Destructuring from a composable
function useCounter() {
  const state = reactive({ count: 0 })
  return state
}

const { count } = useCounter()  // count is now a non-reactive primitive
```

**Correct:**
```javascript
import { reactive, toRefs } from 'vue'

const state = reactive({
  count: 0,
  name: 'Vue'
})

// CORRECT: Use toRefs() to maintain reactivity
const { count, name } = toRefs(state)

state.count++
console.log(count.value)  // 1 - Reactivity preserved! (note: now needs .value)
```

```javascript
// CORRECT: Return toRefs from composables
function useCounter() {
  const state = reactive({ count: 0 })
  return toRefs(state)  // Now safe to destructure
}

const { count } = useCounter()  // count is now a ref, reactivity preserved
```

```javascript
// ALTERNATIVE: Just use ref() to avoid the issue entirely
import { ref } from 'vue'

const count = ref(0)
const name = ref('Vue')

// No destructuring needed, no gotchas
```

## Reference
- [Vue.js Reactivity Fundamentals - reactive()](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive)
- [Vue.js Reactivity API - toRefs()](https://vuejs.org/api/reactivity-utilities.html#torefs)
```

## File: `skills/vue-debug-guides/reference/reactivity-debugging-hooks.md`
```markdown
---
title: Use Debug Hooks to Trace Reactivity Issues
impact: MEDIUM
impactDescription: Debug hooks help identify which dependencies trigger re-renders and watcher executions
type: efficiency
tags: [vue3, reactivity, debugging, computed, watch, development]
---

# Use Debug Hooks to Trace Reactivity Issues

**Impact: MEDIUM** - Vue provides debug hooks (`onTrack`, `onTrigger`, `renderTracked`, `renderTriggered`) that help identify exactly which reactive dependencies are being tracked and which mutations trigger re-execution. These are invaluable for debugging performance issues and unexpected re-renders.

Debug hooks only work in development mode and are stripped in production builds. Use them to understand why a computed property, watcher, or component is re-executing.

## Task Checklist

- [ ] Use `onTrack` and `onTrigger` options on computed/watch for granular debugging
- [ ] Use `onRenderTracked` and `onRenderTriggered` lifecycle hooks for component render debugging
- [ ] Add `debugger` statements inside hooks to pause execution and inspect state
- [ ] Remove or comment out debug hooks before production (they're no-ops but add clutter)

> **Note:** `onTrack` and `onTrigger` are development-only hooks. They are stripped from production builds and may not fire in test environments (e.g., Vitest, Jest) depending on how Vue is bundled. If you need to verify reactivity behavior in tests, use direct assertions on reactive state changes rather than relying on these debug callbacks.

**Debugging computed properties:**
```javascript
import { ref, computed } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2, {
  onTrack(event) {
    // Called when a dependency is tracked
    // event.target = the reactive object
    // event.key = the property being accessed
    debugger
    console.log('Tracking:', event)
  },
  onTrigger(event) {
    // Called when a dependency mutation triggers re-computation
    debugger
    console.log('Triggered by:', event)
  }
})
```

**Debugging watchers:**
```javascript
import { ref, watch, watchEffect } from 'vue'

const source = ref(0)

// With watch()
watch(source, (newVal, oldVal) => {
  console.log('Changed:', oldVal, '->', newVal)
}, {
  onTrack(e) {
    debugger // Pause to see what's being tracked
  },
  onTrigger(e) {
    debugger // Pause to see what triggered the watcher
  }
})

// With watchEffect()
watchEffect(() => {
  console.log('Source is:', source.value)
}, {
  onTrack(e) {
    console.log('Tracking dependency:', e.key)
  },
  onTrigger(e) {
    console.log('Triggered by:', e.key, 'mutation')
  }
})
```

**Debugging component renders:**
```vue
<script setup>
import { onRenderTracked, onRenderTriggered, ref } from 'vue'

const count = ref(0)

// Called for every reactive dependency accessed during render
onRenderTracked((event) => {
  console.log('Render tracked:', event.key, 'from', event.target)
  debugger // Pause to inspect which dependencies are tracked
})

// Called when a reactive dependency triggers re-render
onRenderTriggered((event) => {
  console.log('Render triggered by:', event.key)
  console.log('Old value:', event.oldValue)
  console.log('New value:', event.newValue)
  debugger // Pause to see exactly what caused the re-render
})
</script>
```

**Options API equivalent:**
```javascript
export default {
  data() {
    return { count: 0 }
  },
  renderTracked(event) {
    console.log('Dependency tracked during render:', event)
    debugger
  },
  renderTriggered(event) {
    console.log('Re-render triggered by:', event)
    debugger
  }
}
```

**Debug event properties:**
```javascript
// The event object contains:
{
  effect: ReactiveEffect,  // The effect being debugged
  target: object,          // The reactive object
  type: 'get' | 'set' | 'add' | 'delete' | 'clear',
  key: string | symbol,    // The property being accessed/mutated
  oldValue: any,           // Previous value (for onTrigger)
  newValue: any            // New value (for onTrigger)
}
```

## Reference
- [Vue.js Reactivity in Depth - Debugging](https://vuejs.org/guide/extras/reactivity-in-depth.html#reactivity-debugging)
- [Vue.js computed() API](https://vuejs.org/api/reactivity-core.html#computed)
- [Vue.js onRenderTracked()](https://vuejs.org/api/composition-api-lifecycle.html#onrendertracked)
```

## File: `skills/vue-debug-guides/reference/reactivity-markraw-for-non-reactive.md`
```markdown
---
title: Use markRaw() for Objects That Should Never Be Reactive
impact: MEDIUM
impactDescription: Library instances, DOM nodes, and complex objects cause overhead and bugs when wrapped in Vue proxies
type: efficiency
tags: [vue3, reactivity, markRaw, performance, external-libraries, dom]
---

# Use markRaw() for Objects That Should Never Be Reactive

**Impact: MEDIUM** - Vue's `markRaw()` tells the reactivity system to never wrap an object in a Proxy. Use it for library instances, DOM nodes, class instances with internal state, and complex objects that Vue shouldn't track. This prevents unnecessary proxy overhead and avoids subtle bugs from double-proxying.

Without `markRaw()`, placing these objects inside reactive state causes Vue to wrap them in Proxies, which can break library internals, cause identity issues, and waste memory on objects that don't need change tracking.

## Task Checklist

- [ ] Use `markRaw()` for third-party library instances (maps, charts, editors)
- [ ] Use `markRaw()` for DOM elements stored in reactive state
- [ ] Use `markRaw()` for class instances that manage their own state
- [ ] Use `markRaw()` for large static data that will never change
- [ ] Remember: markRaw only affects the root level - nested objects may still be proxied

**Incorrect:**
```javascript
import { reactive, ref } from 'vue'
import mapboxgl from 'mapbox-gl'
import * as monaco from 'monaco-editor'

// WRONG: Library instances wrapped in Proxy
const state = reactive({
  map: new mapboxgl.Map({ container: 'map' }),  // Proxied!
  editor: monaco.editor.create(element, {}),    // Proxied!
})

// Problems:
// 1. Library's internal this references may break
// 2. Unnecessary memory overhead
// 3. Methods may not work correctly through proxy
// 4. Performance degradation

// WRONG: DOM elements in reactive state
const elements = reactive({
  container: document.getElementById('app'),  // Proxied DOM node!
})
```

**Correct:**
```javascript
import { reactive, markRaw, shallowRef } from 'vue'
import mapboxgl from 'mapbox-gl'
import * as monaco from 'monaco-editor'

// CORRECT: Mark library instances as raw
const state = reactive({
  map: markRaw(new mapboxgl.Map({ container: 'map' })),
  editor: markRaw(monaco.editor.create(element, {})),
})

// CORRECT: Or use shallowRef for mutable references
const map = shallowRef(null)
onMounted(() => {
  map.value = markRaw(new mapboxgl.Map({ container: 'map' }))
})

// CORRECT: Large static data
const geoJsonData = markRaw(await fetch('/huge-geojson.json').then(r => r.json()))
const state = reactive({
  mapData: geoJsonData  // Won't be proxied
})
```

**Class instances with internal state:**
```javascript
import { markRaw, reactive } from 'vue'

class WebSocketManager {
  constructor(url) {
    this.socket = new WebSocket(url)
    this.listeners = new Map()
  }

  on(event, callback) {
    this.listeners.set(event, callback)
  }
}

// CORRECT: Mark class instance
const wsManager = markRaw(new WebSocketManager('ws://example.com'))

const state = reactive({
  connection: wsManager  // Won't be proxied
})

// Can still use the instance normally
state.connection.on('message', handleMessage)
```

**Gotcha: markRaw only affects root level:**
```javascript
import { markRaw, reactive } from 'vue'

const rawObject = markRaw({
  nested: { value: 1 }  // This nested object is NOT marked raw
})

const state = reactive({
  data: rawObject
})

// rawObject itself won't be proxied
// But if you access nested objects through a reactive parent:
const container = reactive({ raw: rawObject })
// container.raw.nested might still be proxied in some cases

// SAFER: Use shallowRef for the container
import { shallowRef } from 'vue'
const safeContainer = shallowRef(rawObject)
```

**Combining with shallowRef for best results:**
```javascript
import { shallowRef, markRaw, onMounted, onUnmounted } from 'vue'

// Pattern: shallowRef + markRaw for external library instances
export function useMapbox(containerId) {
  const map = shallowRef(null)

  onMounted(() => {
    const instance = new mapboxgl.Map({
      container: containerId,
      style: 'mapbox://styles/mapbox/streets-v11'
    })

    // Mark raw to prevent any proxy wrapping
    map.value = markRaw(instance)
  })

  onUnmounted(() => {
    map.value?.remove()
  })

  return { map }
}
```

## Reference
- [Vue.js markRaw() API](https://vuejs.org/api/reactivity-advanced.html#markraw)
- [Vue.js Reducing Reactivity Overhead](https://vuejs.org/guide/best-practices/performance.html#reduce-reactivity-overhead-for-large-immutable-structures)
- [Vue.js Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth.html)
```

## File: `skills/vue-debug-guides/reference/reactivity-proxy-identity-hazard.md`
```markdown
---
title: Avoid Comparing Reactive Objects with === Operator
impact: HIGH
impactDescription: Reactive proxies have different identity than original objects - comparison bugs are silent and hard to debug
type: gotcha
tags: [vue3, reactivity, proxy, comparison, debugging, identity]
---

# Avoid Comparing Reactive Objects with === Operator

**Impact: HIGH** - Vue's `reactive()` returns a Proxy wrapper that has a different identity than the original object. Using `===` to compare reactive objects can lead to silent bugs where comparisons unexpectedly return `false`.

When you wrap an object with `reactive()`, the returned proxy is NOT equal to the original object. Additionally, accessing nested objects from a reactive object returns new proxy wrappers each time, which can cause identity comparison issues.

## Task Checklist

- [ ] Never compare reactive object instances with `===` directly
- [ ] Use unique identifiers (ID, UUID) for object comparison instead
- [ ] Use `toRaw()` on both sides when identity comparison is absolutely necessary
- [ ] Consider using primitive identifiers from database records for comparison

**Incorrect:**
```javascript
import { reactive } from 'vue'

const original = { id: 1, name: 'Item' }
const state = reactive(original)

// BUG: Always returns false - proxy !== original
if (state === original) {
  console.log('Same object') // Never executes
}

// BUG: Nested object comparison fails
const items = reactive([{ id: 1 }, { id: 2 }])
const item = items[0]

// Later...
if (items[0] === item) {
  // May or may not work depending on Vue's proxy caching
}

// BUG: Comparing items from different reactive sources
const listA = reactive([{ id: 1 }])
const listB = reactive([{ id: 1 }])
if (listA[0] === listB[0]) {
  // Never true, even though they represent the same data
}
```

**Correct:**
```javascript
import { reactive, toRaw } from 'vue'

const original = { id: 1, name: 'Item' }
const state = reactive(original)

// CORRECT: Use toRaw() for identity comparison
if (toRaw(state) === original) {
  console.log('Same underlying object') // Works!
}

// BEST: Use unique identifiers instead
const items = reactive([
  { id: 'uuid-1', name: 'Item 1' },
  { id: 'uuid-2', name: 'Item 2' }
])

function findItem(targetId) {
  return items.find(item => item.id === targetId)
}

function isSelected(item) {
  return selectedId.value === item.id // Compare IDs, not objects
}

// CORRECT: For Set/Map operations, use primitive keys
const selectedIds = reactive(new Set())
selectedIds.add(item.id)  // Use ID, not object
selectedIds.has(item.id)  // Check by ID
```

```javascript
// When you must compare objects, use toRaw on both sides
import { toRaw, isReactive } from 'vue'

function areEqual(a, b) {
  const rawA = isReactive(a) ? toRaw(a) : a
  const rawB = isReactive(b) ? toRaw(b) : b
  return rawA === rawB
}
```

## Reference
- [Vue.js Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth.html)
- [Vue.js toRaw() API](https://vuejs.org/api/reactivity-advanced.html#toraw)
```

## File: `skills/vue-debug-guides/reference/reactivity-same-tick-batching.md`
```markdown
---
title: Understand Reactive Updates are Batched Per Event Loop Tick
impact: MEDIUM
impactDescription: Multiple synchronous reactive changes are batched - watchers only see the final value, not intermediate states
type: gotcha
tags: [vue3, reactivity, batching, event-loop, watchers, nextTick]
---

# Understand Reactive Updates are Batched Per Event Loop Tick

**Impact: MEDIUM** - Vue batches multiple reactive state changes that happen synchronously within the same event loop tick. Watchers and computed properties only see the final state, not intermediate values. This is an optimization, but it can be surprising if you expect watchers to fire for each individual change.

Understanding this behavior is essential for debugging scenarios where you expect to observe every state transition.

## Task Checklist

- [ ] Understand watchers fire once per tick with final value, not for each mutation
- [ ] Use `nextTick()` if you need to ensure DOM updates between state changes
- [ ] Use `flush: 'sync'` on watchers only if you absolutely need immediate execution
- [ ] For intermediate value tracking, consider logging or explicit state snapshots

**Example of batching behavior:**
```javascript
import { ref, watch } from 'vue'

const count = ref(0)

watch(count, (newValue) => {
  console.log('Count changed to:', newValue)
})

// Multiple synchronous changes in the same tick
function multipleUpdates() {
  count.value = 1
  count.value = 2
  count.value = 3
  count.value = 4
}

multipleUpdates()
// Console output: "Count changed to: 4"
// NOT: 1, 2, 3, 4 - only the final value is observed!
```

**The console logs you WON'T see:**
```javascript
const items = reactive([])

watch(items, (newItems) => {
  console.log('Items count:', newItems.length)
})

// Batch of changes
items.push('a')  // length: 1
items.push('b')  // length: 2
items.push('c')  // length: 3

// Output: "Items count: 3"
// You won't see 1, 2, 3 logged separately
```

**Using flush: 'sync' for immediate watching (use with caution):**
```javascript
import { ref, watch } from 'vue'

const count = ref(0)

// Sync watcher fires immediately on each change
watch(count, (newValue) => {
  console.log('Immediate:', newValue)
}, { flush: 'sync' })

count.value = 1  // Logs: "Immediate: 1"
count.value = 2  // Logs: "Immediate: 2"
count.value = 3  // Logs: "Immediate: 3"

// WARNING: flush: 'sync' can cause performance issues
// and creates less predictable behavior. Avoid if possible.
```

**Using nextTick to separate batches:**
```javascript
import { ref, watch, nextTick } from 'vue'

const count = ref(0)

watch(count, (newValue) => {
  console.log('Count:', newValue)
})

async function separatedUpdates() {
  count.value = 1
  await nextTick()  // Force flush
  // Output: "Count: 1"

  count.value = 2
  await nextTick()
  // Output: "Count: 2"

  count.value = 3
  // Output: "Count: 3"
}
```

**Practical example - form validation:**
```javascript
const formData = reactive({
  email: '',
  password: ''
})

const validationErrors = ref([])

// This watcher only fires once, with final form state
watch(formData, (data) => {
  // Runs once after all fields are updated
  validateForm(data)
}, { deep: true })

// When user submits, you might update multiple fields
function populateFromSavedData(saved) {
  formData.email = saved.email
  formData.password = saved.password
  // Validation runs once with both fields set
}
```

**When batching helps performance:**
```javascript
// Without batching, this would trigger 1000 watcher/render cycles
const list = reactive([])

function addManyItems() {
  for (let i = 0; i < 1000; i++) {
    list.push(i)
  }
}
// With batching: renders once with all 1000 items
// Without batching: would render 1000 times!
```

**Debugging intermediate states:**
```javascript
// If you need to observe every change for debugging:
import { ref, watch } from 'vue'

const count = ref(0)

// Method 1: Sync watcher (not recommended for production)
watch(count, (val) => console.log('DEBUG:', val), { flush: 'sync' })

// Method 2: Track history manually
const history = []
const originalSet = count.value
Object.defineProperty(count, 'value', {
  set(val) {
    history.push(val)
    originalSet.call(this, val)
  }
})
```

## Reference
- [Vue.js Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth.html)
- [Vue.js Watchers - Callback Flush Timing](https://vuejs.org/guide/essentials/watchers.html#callback-flush-timing)
- [Vue.js nextTick()](https://vuejs.org/api/general.html#nexttick)
```

## File: `skills/vue-debug-guides/reference/ref-value-access.md`
```markdown
---
title: Always Use .value When Accessing ref() in JavaScript
impact: HIGH
impactDescription: Forgetting .value causes silent failures and bugs in reactive state updates
type: capability
tags: [vue3, reactivity, ref, composition-api]
---

# Always Use .value When Accessing ref() in JavaScript

**Impact: HIGH** - Forgetting `.value` causes silent failures where state updates don't trigger reactivity, leading to hard-to-debug issues.

When using `ref()` in Vue 3's Composition API, the reactive value is wrapped in an object and must be accessed via `.value` in JavaScript code. However, in templates, Vue automatically unwraps refs so `.value` is not needed there. This inconsistency is a common source of bugs.

## Task Checklist

- [ ] Always use `.value` when reading or writing ref values in `<script>` or `.js`/`.ts` files
- [ ] Never use `.value` in `<template>` - Vue unwraps refs automatically there
- [ ] When passing refs to functions, decide whether to pass the ref object or `.value`
- [ ] Use IDE/TypeScript to catch missing `.value` errors early

**Incorrect:**
```javascript
import { ref } from 'vue'

const count = ref(0)

// These do NOT work as expected
count++           // Tries to increment the ref object, not the value
count = 5         // Reassigns the variable, loses reactivity
console.log(count) // Logs "[object Object]", not the number

const items = ref([1, 2, 3])
items.push(4)     // Error: push is not a function
```

**Correct:**
```javascript
import { ref } from 'vue'

const count = ref(0)

// Always use .value in JavaScript
count.value++           // Correctly increments to 1
count.value = 5         // Correctly sets value to 5
console.log(count.value) // Logs "5"

const items = ref([1, 2, 3])
items.value.push(4)     // Correctly adds 4 to the array
```

```vue
<template>
  <!-- In templates, NO .value needed - Vue unwraps automatically -->
  <p>{{ count }}</p>
  <button @click="count++">Increment</button>
</template>
```

## Reference
- [Vue.js Reactivity Fundamentals - ref()](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref)
```

## File: `skills/vue-debug-guides/reference/refs-in-collections-need-value.md`
```markdown
---
title: Refs in Arrays and Collections Require .value
impact: MEDIUM
impactDescription: Refs inside reactive arrays, Maps, or Sets are NOT auto-unwrapped like in reactive objects
type: capability
tags: [vue3, reactivity, ref, arrays, collections, unwrapping]
---

# Refs in Arrays and Collections Require .value

**Impact: MEDIUM** - Unlike when a ref is a property of a reactive object, refs inside reactive arrays, Maps, and Sets are NOT automatically unwrapped. You must access them with `.value`, and forgetting this leads to silent bugs.

Vue only auto-unwraps refs when they are properties of reactive objects. When refs are elements in arrays or values in Maps/Sets, they remain as ref objects and require explicit `.value` access.

## Task Checklist

- [ ] Always use `.value` when accessing refs stored in reactive arrays
- [ ] Always use `.value` when accessing refs stored in reactive Maps or Sets
- [ ] Consider storing plain values instead of refs in collections to avoid confusion
- [ ] Be aware of this when iterating over arrays containing refs

**Incorrect:**
```javascript
import { ref, reactive } from 'vue'

const books = reactive([ref('Vue 3 Guide')])
const counts = reactive(new Map([['clicks', ref(0)]]))

// WRONG: Refs in arrays are NOT unwrapped
console.log(books[0])        // Ref object, not 'Vue 3 Guide'
books[0] = 'New Title'       // Replaces the ref, doesn't update it!

// WRONG: Refs in Maps are NOT unwrapped
console.log(counts.get('clicks'))     // Ref object, not 0
counts.get('clicks')++                // Does nothing useful
```

**Correct:**
```javascript
import { ref, reactive } from 'vue'

const books = reactive([ref('Vue 3 Guide')])
const counts = reactive(new Map([['clicks', ref(0)]]))

// CORRECT: Use .value for refs in arrays
console.log(books[0].value)    // 'Vue 3 Guide'
books[0].value = 'New Title'   // Updates the ref's value

// CORRECT: Use .value for refs in Maps
console.log(counts.get('clicks').value)  // 0
counts.get('clicks').value++             // Increments to 1
```

```javascript
// ALTERNATIVE: Just store plain values in collections (simpler)
const books = reactive(['Vue 3 Guide', 'Vuex Handbook'])
const counts = reactive(new Map([['clicks', 0]]))

// No .value needed - but changes to individual items aren't independently reactive
console.log(books[0])            // 'Vue 3 Guide'
console.log(counts.get('clicks')) // 0

// Mutations still trigger reactivity through the reactive wrapper
books[0] = 'New Title'           // Works
counts.set('clicks', counts.get('clicks') + 1)  // Works
```

```vue
<template>
  <!-- In templates, refs in arrays also need special handling -->
  <div v-for="(book, index) in books" :key="index">
    <!-- If book is a ref, you'd need: -->
    {{ book.value }}

    <!-- Or use computed to unwrap them first -->
  </div>
</template>
```

## Reference
- [Vue.js Reactivity Fundamentals - Caveat in Arrays and Collections](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-in-arrays-and-collections)
```

## File: `skills/vue-debug-guides/reference/render-function-avoid-internal-vnode-properties.md`
```markdown
---
title: Do Not Rely on Internal VNode Properties
impact: MEDIUM
impactDescription: Using undocumented vnode properties causes code to break on Vue updates
type: gotcha
tags: [vue3, render-function, vnode, internal-api]
---

# Do Not Rely on Internal VNode Properties

**Impact: MEDIUM** - The `VNode` interface contains many internal properties used by Vue's rendering system. Relying on any properties other than the documented public ones will cause your code to break when Vue's internal implementation changes.

Only use the documented vnode properties: `type`, `props`, `children`, and `key`. All other properties are internal implementation details that may change without notice between Vue versions.

## Task Checklist

- [ ] Only access documented vnode properties: `type`, `props`, `children`, `key`
- [ ] Never access properties like `el`, `component`, `shapeFlag`, `patchFlag`, etc.
- [ ] If you need DOM element access, use template refs instead
- [ ] Treat vnodes as opaque data structures for rendering, not inspection

**Incorrect:**
```javascript
import { h } from 'vue'

export default {
  setup(props, { slots }) {
    return () => {
      const slotContent = slots.default?.()

      // WRONG: Accessing internal properties
      if (slotContent?.[0]?.el) {
        // el is an internal property
        console.log(slotContent[0].el.tagName)
      }

      // WRONG: Using shapeFlag internal property
      if (slotContent?.[0]?.shapeFlag & 1) {
        // This is internal implementation
      }

      return h('div', slotContent)
    }
  }
}
```

```javascript
// WRONG: Inspecting component instance via vnode
const vnode = h(MyComponent)
console.log(vnode.component) // Internal property
console.log(vnode.appContext) // Internal property
```

**Correct:**
```javascript
import { h } from 'vue'

export default {
  setup(props, { slots }) {
    return () => {
      const slotContent = slots.default?.()

      // CORRECT: Only use documented properties
      if (slotContent?.[0]) {
        const vnode = slotContent[0]
        console.log(vnode.type)     // Safe: element type or component
        console.log(vnode.props)    // Safe: props object
        console.log(vnode.children) // Safe: children
        console.log(vnode.key)      // Safe: key prop
      }

      return h('div', slotContent)
    }
  }
}
```

```javascript
import { h, ref, onMounted } from 'vue'

export default {
  setup() {
    // CORRECT: Use template refs for DOM access
    const divRef = ref(null)

    onMounted(() => {
      // Safe way to access DOM element
      console.log(divRef.value.tagName)
    })

    return () => h('div', { ref: divRef }, 'Content')
  }
}
```

## Documented VNode Properties

| Property | Type | Description |
|----------|------|-------------|
| `type` | `string \| Component` | Element tag name or component definition |
| `props` | `object \| null` | Props passed to the vnode |
| `children` | `any` | Child vnodes, text, or slots |
| `key` | `string \| number \| null` | Key for list rendering |

## Safe VNode Inspection Patterns

```javascript
import { h, isVNode } from 'vue'

export default {
  setup(props, { slots }) {
    return () => {
      const children = slots.default?.() || []

      // Safe: Check if something is a vnode
      children.forEach(child => {
        if (isVNode(child)) {
          // Safe: Check vnode type
          if (typeof child.type === 'string') {
            console.log('Element:', child.type)
          } else if (typeof child.type === 'object') {
            console.log('Component:', child.type.name)
          }

          // Safe: Read props
          if (child.props?.class) {
            console.log('Has class:', child.props.class)
          }
        }
      })

      return h('div', children)
    }
  }
}
```

## Why This Matters

Vue's internal vnode structure may change for:
- Performance optimizations
- New feature implementations
- Bug fixes
- Tree-shaking improvements

Code relying on internal properties will break silently or throw errors when upgrading Vue versions. The documented properties are part of Vue's public API and are guaranteed to remain stable.

## Reference
- [Vue.js Render Function APIs](https://vuejs.org/api/render-function.html)
- [Vue.js Render Functions - The Virtual DOM](https://vuejs.org/guide/extras/render-function.html#the-virtual-dom)
```

## File: `skills/vue-debug-guides/reference/render-function-vnodes-must-be-unique.md`
```markdown
---
title: VNodes Must Be Unique in Render Functions
impact: HIGH
impactDescription: Reusing vnode references causes rendering bugs and unexpected behavior
type: gotcha
tags: [vue3, render-function, vnode, composition-api]
---

# VNodes Must Be Unique in Render Functions

**Impact: HIGH** - Reusing the same vnode reference multiple times in a render function tree causes rendering bugs, where only one instance appears or updates behave unexpectedly.

Every vnode in a component's render tree must be unique. You cannot use the same vnode object multiple times. If you need to render the same element multiple times, create each vnode separately using a factory function or by calling `h()` in a loop.

## Task Checklist

- [ ] Never store a vnode in a variable and use it multiple times in the same tree
- [ ] Use a factory function or `.map()` to create multiple similar vnodes
- [ ] Each `h()` call creates a new vnode, so call it for each instance needed
- [ ] Be especially careful when extracting vnode creation into helper functions

**Incorrect:**
```javascript
import { h } from 'vue'

export default {
  setup() {
    return () => {
      // WRONG: Same vnode reference used twice
      const p = h('p', 'Hello')
      return h('div', [p, p]) // Bug! Duplicate vnode reference
    }
  }
}
```

```javascript
import { h } from 'vue'

export default {
  setup() {
    return () => {
      // WRONG: Reusing vnode in different parts of tree
      const icon = h('span', { class: 'icon' }, '★')
      return h('div', [
        h('button', [icon, ' Save']),    // Uses icon
        h('button', [icon, ' Delete'])   // Reuses same icon - Bug!
      ])
    }
  }
}
```

**Correct:**
```javascript
import { h } from 'vue'

export default {
  setup() {
    return () => {
      // CORRECT: Create new vnode for each use
      return h('div', [
        h('p', 'Hello'),
        h('p', 'Hello')
      ])
    }
  }
}
```

```javascript
import { h } from 'vue'

export default {
  setup() {
    return () => {
      // CORRECT: Factory function creates new vnode each time
      const createIcon = () => h('span', { class: 'icon' }, '★')
      return h('div', [
        h('button', [createIcon(), ' Save']),
        h('button', [createIcon(), ' Delete'])
      ])
    }
  }
}
```

```javascript
import { h } from 'vue'

export default {
  setup() {
    return () => {
      // CORRECT: Using map to create multiple vnodes
      return h('div',
        Array.from({ length: 20 }).map(() => h('p', 'Hello'))
      )
    }
  }
}
```

```javascript
import { h } from 'vue'

export default {
  setup() {
    const items = ['Apple', 'Banana', 'Cherry']

    return () => h('ul',
      // CORRECT: Each iteration creates a new vnode
      items.map((item, index) =>
        h('li', { key: index }, item)
      )
    )
  }
}
```

## Why VNodes Must Be Unique

VNodes are lightweight JavaScript objects that Vue's virtual DOM algorithm uses for diffing and patching. When the same vnode reference appears multiple times:
- Vue cannot differentiate between the instances
- The diffing algorithm produces incorrect results
- Only one instance may render, or updates may corrupt the DOM

Each vnode maintains its own identity and position in the tree, which is essential for:
- Correct DOM patching during updates
- Proper lifecycle hook execution
- Accurate key-based reconciliation in lists

## Reference
- [Vue.js Render Functions - Vnodes Must Be Unique](https://vuejs.org/guide/extras/render-function.html#vnodes-must-be-unique)
```

## File: `skills/vue-debug-guides/reference/rendering-render-function-h-import-vue3.md`
```markdown
---
title: Import h Globally in Vue 3 Render Functions
impact: HIGH
impactDescription: Vue 3 requires explicit h import; using Vue 2 patterns causes runtime errors
type: gotcha
tags: [vue3, render-function, migration, h, vnode, breaking-change]
---

# Import h Globally in Vue 3 Render Functions

**Impact: HIGH** - In Vue 2, the `h` function (createElement) was passed as an argument to render functions. In Vue 3, `h` must be explicitly imported from 'vue'. Using Vue 2 patterns causes runtime errors.

## Task Checklist

- [ ] Import `h` from 'vue' at the top of files using render functions
- [ ] Remove the `h` parameter from render function signatures
- [ ] Update all render functions when migrating from Vue 2

**Incorrect (Vue 2 pattern - broken in Vue 3):**
```js
// WRONG: Vue 2 pattern - h is not passed as argument in Vue 3
export default {
  render(h) {  // h is undefined in Vue 3!
    return h('div', [
      h('span', 'Hello')
    ])
  }
}

// WRONG: Using createElement alias from Vue 2
export default {
  render(createElement) {  // Also undefined
    return createElement('div', 'Hello')
  }
}
```

**Correct (Vue 3 pattern):**
```js
// CORRECT: Import h from vue
import { h } from 'vue'

export default {
  render() {
    return h('div', [
      h('span', 'Hello')
    ])
  }
}
```

## With Composition API

```js
import { h, ref } from 'vue'

export default {
  setup() {
    const count = ref(0)

    // Return a render function from setup
    return () => h('div', [
      h('button', { onClick: () => count.value++ }, `Count: ${count.value}`)
    ])
  }
}
```

## With script setup (Not Recommended)

```vue
<script setup>
import { h, ref } from 'vue'

const count = ref(0)

// Cannot return render function from script setup
// Must use a separate render option or template
</script>

<!-- script setup typically uses templates, not render functions -->
<template>
  <div>
    <button @click="count++">Count: {{ count }}</button>
  </div>
</template>
```

If you need render functions with `<script setup>`, use the `render` option:

```vue
<script>
import { h, ref } from 'vue'

export default {
  setup() {
    const count = ref(0)
    return () => h('button', { onClick: () => count.value++ }, count.value)
  }
}
</script>
```

## Component Resolution Change

In Vue 3, you must also explicitly resolve components:

**Incorrect:**
```js
// Vue 2: Could use string names for registered components
render(h) {
  return h('my-component', { props: { value: 1 } })
}
```

**Correct:**
```js
import { h, resolveComponent } from 'vue'

export default {
  render() {
    // Must resolve component by name
    const MyComponent = resolveComponent('my-component')
    return h(MyComponent, { value: 1 })
  }
}

// Or import the component directly (preferred)
import { h } from 'vue'
import MyComponent from './MyComponent.vue'

export default {
  render() {
    return h(MyComponent, { value: 1 })
  }
}
```

## Why This Changed

Vue 3's `h` is globally importable to:
1. Enable tree-shaking (unused features can be removed)
2. Support better TypeScript inference
3. Allow use outside of component context

## Reference
- [Vue 3 Migration Guide - Render Function API](https://v3-migration.vuejs.org/breaking-changes/render-function-api.html)
- [Vue.js Render Functions & JSX](https://vuejs.org/guide/extras/render-function.html)
```

## File: `skills/vue-debug-guides/reference/rendering-render-function-return-from-setup.md`
```markdown
---
title: Return Render Function from setup(), Not Direct VNodes
impact: HIGH
impactDescription: Returning a vnode directly from setup makes it static; returning a function enables reactive updates
type: gotcha
tags: [vue3, render-function, composition-api, setup, reactivity]
---

# Return Render Function from setup(), Not Direct VNodes

**Impact: HIGH** - When using render functions with the Composition API, you must return a function that returns vnodes, not the vnodes directly. Returning vnodes directly creates a static render that never updates when reactive state changes.

## Task Checklist

- [ ] Always return an arrow function from setup() when using render functions
- [ ] Never return h() calls directly from setup()
- [ ] Ensure reactive values are accessed inside the returned function

**Incorrect:**
```js
import { h, ref } from 'vue'

export default {
  setup() {
    const count = ref(0)
    const increment = () => count.value++

    // WRONG: Returns a static vnode, created once
    // Clicking the button updates count.value, but the DOM never changes!
    return h('div', [
      h('p', `Count: ${count.value}`),  // Captures count.value at setup time (0)
      h('button', { onClick: increment }, 'Increment')
    ])
  }
}
```

**Correct:**
```js
import { h, ref } from 'vue'

export default {
  setup() {
    const count = ref(0)
    const increment = () => count.value++

    // CORRECT: Returns a render function
    // Vue calls this function on every reactive update
    return () => h('div', [
      h('p', `Count: ${count.value}`),  // Re-evaluated each render
      h('button', { onClick: increment }, 'Increment')
    ])
  }
}
```

## Why This Happens

```js
// What Vue does internally:

// WRONG approach - setup runs once:
const result = setup()
// result is a vnode { type: 'div', children: [...] }
// Vue renders this once, then has no way to re-render

// CORRECT approach - setup returns a function:
const renderFn = setup()
// renderFn is () => h('div', ...)
// Vue calls renderFn() on mount
// Vue calls renderFn() again whenever dependencies change
```

## Common Mistake: Mixing Template and Render Function

```vue
<script setup>
import { h, ref } from 'vue'

const count = ref(0)

// WRONG: Can't use render functions in script setup with templates
// This h() call does nothing
const node = h('div', count.value)
</script>

<template>
  <!-- Template is used, render function is ignored -->
  <div>{{ count }}</div>
</template>
```

If you need a render function with Composition API, don't use `<script setup>`:

```vue
<script>
import { h, ref } from 'vue'

export default {
  setup() {
    const count = ref(0)
    return () => h('div', count.value)
  }
}
</script>
<!-- No template - render function is used -->
```

## Exposing Values While Using Render Functions

```js
import { h, ref } from 'vue'

export default {
  setup(props, { expose }) {
    const count = ref(0)
    const reset = () => { count.value = 0 }

    // Expose methods for parent refs
    expose({ reset })

    // Still return the render function
    return () => h('div', count.value)
  }
}
```

## With Slots

```js
import { h, ref } from 'vue'

export default {
  setup(props, { slots }) {
    const count = ref(0)

    return () => h('div', [
      h('p', `Count: ${count.value}`),
      // Slots must also be called inside the render function
      slots.default?.()
    ])
  }
}
```

## Reference
- [Vue.js Render Functions with Composition API](https://vuejs.org/guide/extras/render-function.html#render-functions-jsx)
- [Vue.js Composition API setup()](https://vuejs.org/api/composition-api-setup.html)
```

## File: `skills/vue-debug-guides/reference/rendering-render-function-slots-as-functions.md`
```markdown
---
title: Pass Slots as Functions in Render Functions, Not Direct Children
impact: HIGH
impactDescription: Passing slot content incorrectly causes slots to not render or be treated as props
type: gotcha
tags: [vue3, render-function, slots, children, vnode]
---

# Pass Slots as Functions in Render Functions, Not Direct Children

**Impact: HIGH** - When creating component vnodes with `h()`, children must be passed as slot functions, not as direct children. Passing children directly may cause them to be interpreted as props or fail to render.

## Task Checklist

- [ ] Pass slot content as functions: `{ default: () => [...] }`
- [ ] Use `null` for props when only passing slots to avoid misinterpretation
- [ ] For default slot only, a single function can be passed directly
- [ ] For named slots, use an object with slot function properties

**Incorrect:**
```js
import { h } from 'vue'
import MyComponent from './MyComponent.vue'

// WRONG: Children array may be misinterpreted
h(MyComponent, [
  h('span', 'Slot content')  // May not render as expected
])

// WRONG: Named slots as direct properties
h(MyComponent, {
  header: h('h1', 'Title'),  // This is a prop, not a slot!
  default: h('p', 'Content')  // This is also a prop
})
```

**Correct:**
```js
import { h } from 'vue'
import MyComponent from './MyComponent.vue'

// CORRECT: Default slot as function
h(MyComponent, null, {
  default: () => h('span', 'Slot content')
})

// CORRECT: Single default slot shorthand
h(MyComponent, null, () => h('span', 'Slot content'))

// CORRECT: Named slots as functions
h(MyComponent, null, {
  header: () => h('h1', 'Title'),
  default: () => h('p', 'Content'),
  footer: () => [
    h('span', 'Footer item 1'),
    h('span', 'Footer item 2')
  ]
})

// CORRECT: With props AND slots
h(MyComponent, { size: 'large' }, {
  default: () => 'Button Text'
})
```

## Why Functions?

Slots in Vue 3 are functions for lazy evaluation:

```js
// Slots are called by the child component when needed
// This enables:
// 1. Scoped slots (passing data back)
// 2. Conditional rendering (slot not called if not used)
// 3. Proper reactivity tracking

h(MyList, { items }, {
  // Scoped slot - receives data from child
  item: ({ item, index }) => h('li', `${index}: ${item.name}`)
})
```

## The null Props Gotcha

When passing only slots, always use `null` for props:

```js
// WRONG: Slots object interpreted as props!
h(MyComponent, {
  default: () => 'Hello'
})
// MyComponent receives: props.default = () => 'Hello'

// CORRECT: null signals "no props, next arg is slots"
h(MyComponent, null, {
  default: () => 'Hello'
})
// MyComponent receives slot correctly
```

## Forwarding Slots from Parent

```js
export default {
  setup(props, { slots }) {
    return () => h(ChildComponent, null, {
      // Forward all slots from parent
      ...slots,

      // Or forward specific slots
      default: slots.default,
      header: slots.header
    })
  }
}
```

## Scoped Slots in Render Functions

```js
// Parent: Receives data from child via slot props
h(DataTable, { data: items }, {
  row: (slotProps) => h('tr', [
    h('td', slotProps.item.name),
    h('td', slotProps.item.value)
  ])
})

// Child (DataTable): Calls slot with data
export default {
  props: ['data'],
  setup(props, { slots }) {
    return () => h('table', [
      h('tbody',
        props.data.map(item =>
          // Pass data to slot function
          slots.row?.({ item })
        )
      )
    ])
  }
}
```

## Common Patterns

```js
// Wrapper component forwarding slots
h('div', { class: 'wrapper' }, [
  h(InnerComponent, null, slots)
])

// Conditional slot rendering
h('div', [
  slots.header?.(),  // Optional chaining - only render if slot provided
  h('main', slots.default?.()),
  slots.footer?.()
])

// Slot with fallback content
h('div', [
  slots.default?.() ?? h('p', 'Default content when slot not provided')
])
```

## Reference
- [Vue.js Render Functions - Passing Slots](https://vuejs.org/guide/extras/render-function.html#passing-slots)
- [Vue.js Render Functions - Children](https://vuejs.org/guide/extras/render-function.html#children)
```

## File: `skills/vue-debug-guides/reference/rendering-resolve-component-for-string-names.md`
```markdown
---
title: Use resolveComponent for String Component Names in Render Functions
impact: HIGH
impactDescription: String component names don't work in Vue 3 render functions; causes silent failures or runtime errors
type: gotcha
tags: [vue3, render-function, components, resolveComponent, migration]
---

# Use resolveComponent for String Component Names in Render Functions

**Impact: HIGH** - In Vue 2, render functions could use string names for globally or locally registered components. In Vue 3, you must either import components directly or use `resolveComponent()`. Using string names causes components to render as HTML elements or fail silently.

## Task Checklist

- [ ] Import components directly when possible (preferred)
- [ ] Use `resolveComponent()` for dynamically registered components
- [ ] Use `resolveDynamicComponent()` for `<component :is="">` equivalent
- [ ] Call `resolveComponent()` inside `setup()` or the render function
- [ ] Handle the case when component is not found

**Incorrect:**
```js
import { h } from 'vue'

export default {
  render() {
    // WRONG: String names don't resolve to components
    return h('div', [
      h('my-component', { value: 1 }),  // Renders <my-component> HTML element!
      h('router-link', { to: '/' }, 'Home')  // Also fails
    ])
  }
}
```

**Correct (Direct Import - Preferred):**
```js
import { h } from 'vue'
import MyComponent from './MyComponent.vue'
import { RouterLink } from 'vue-router'

export default {
  render() {
    return h('div', [
      h(MyComponent, { value: 1 }),
      h(RouterLink, { to: '/' }, () => 'Home')
    ])
  }
}
```

**Correct (resolveComponent for Registered Components):**
```js
import { h, resolveComponent } from 'vue'

export default {
  components: {
    MyComponent: () => import('./MyComponent.vue')
  },

  setup() {
    // Resolve inside setup - component context is available
    const MyComponent = resolveComponent('MyComponent')

    return () => h('div', [
      h(MyComponent, { value: 1 })
    ])
  }
}

// Or resolve inside render function
export default {
  render() {
    const MyComponent = resolveComponent('MyComponent')
    const RouterLink = resolveComponent('RouterLink')

    return h('div', [
      h(MyComponent, { value: 1 }),
      h(RouterLink, { to: '/' }, () => 'Home')
    ])
  }
}
```

## When to Use Each Approach

| Approach | Use When |
|----------|----------|
| Direct Import | Component is known at build time (most common) |
| `resolveComponent()` | Component is registered globally or locally by name |
| `resolveComponent()` | Dynamic component selection from registered set |

## Handling Missing Components

```js
import { h, resolveComponent } from 'vue'

export default {
  setup() {
    // resolveComponent returns the component or the string name if not found
    const DynamicComponent = resolveComponent('MaybeRegistered')

    // Check if resolution succeeded
    if (typeof DynamicComponent === 'string') {
      console.warn(`Component "${DynamicComponent}" not found`)
    }

    return () => h(DynamicComponent, { value: 1 })
  }
}
```

## Dynamic Component Selection

```js
import { h, resolveComponent, computed } from 'vue'

export default {
  props: ['componentName'],

  setup(props) {
    // For truly dynamic components, resolve in render function
    return () => {
      const Component = resolveComponent(props.componentName)
      return h(Component, { /* props */ })
    }
  }
}
```

For the equivalent of `<component :is="componentName">`, use `resolveDynamicComponent`:

```js
import { h, resolveDynamicComponent } from 'vue'

export default {
  props: ['componentType'],
  setup(props) {
    return () => {
      // Resolves string names, component objects, or built-in elements
      const component = resolveDynamicComponent(props.componentType)
      return h(component, { /* props */ })
    }
  }
}
```

## Practical Example: Tab Component

```js
import { h, resolveComponent, ref } from 'vue'

export default {
  setup() {
    const currentTab = ref('TabA')
    const tabs = ['TabA', 'TabB', 'TabC']

    return () => h('div', [
      // Tab buttons
      h('div', { class: 'tabs' },
        tabs.map(tab =>
          h('button', {
            key: tab,
            class: { active: currentTab.value === tab },
            onClick: () => currentTab.value = tab
          }, tab)
        )
      ),

      // Dynamic component based on current tab
      h(resolveComponent(currentTab.value))
    ])
  }
}
```

## Resolving Built-in Components

For built-in components like `<Transition>` or `<KeepAlive>`, import them directly from Vue:

```js
import { h, Transition, KeepAlive, Teleport, Suspense } from 'vue'

export default {
  setup() {
    return () => h(Transition, { name: 'fade' }, () =>
      h('div', 'Content')
    )
  }
}
```

## Resolving Directives

Similar pattern for custom directives:

```js
import { h, resolveDirective, withDirectives } from 'vue'

export default {
  render() {
    const vFocus = resolveDirective('focus')

    return withDirectives(
      h('input', { type: 'text' }),
      [[vFocus]]
    )
  }
}
```

## Migration from Vue 2

```js
// Vue 2 (worked with registered components)
render(h) {
  return h('my-component', { props: { value: 1 } })
}

// Vue 3 (must resolve or import)
import { h, resolveComponent } from 'vue'

render() {
  const MyComponent = resolveComponent('my-component')
  return h(MyComponent, { value: 1 })  // Note: props go directly, not in 'props' key
}
```

## Reference
- [Vue 3 Migration - Render Function API](https://v3-migration.vuejs.org/breaking-changes/render-function-api.html)
- [Vue.js Render Function API - resolveComponent](https://vuejs.org/api/render-function.html#resolvecomponent)
```

## File: `skills/vue-debug-guides/reference/select-initial-value-ios-bug.md`
```markdown
---
title: Select Element iOS Bug - Always Include Disabled Placeholder Option
impact: HIGH
impactDescription: On iOS, users cannot select the first option if v-model initial value doesn't match any option
type: capability
tags: [vue3, v-model, forms, select, ios, mobile, accessibility]
---

# Select Element iOS Bug - Always Include Disabled Placeholder Option

**Impact: HIGH** - When a `<select>` element's v-model initial value doesn't match any option, iOS renders it as "unselected" and users CANNOT select the first item. iOS doesn't fire a change event when selecting an already-visually-selected option, leaving users stuck.

This is a platform-specific bug that only manifests on iOS Safari. Desktop browsers and Android handle this gracefully, making it easy to miss during development. The fix is simple: always include a disabled placeholder option.

## Task Checklist

- [ ] Always add a disabled placeholder option with empty value to select elements
- [ ] Ensure v-model initial value is empty string to match the placeholder
- [ ] Test select inputs on iOS devices or simulators
- [ ] Consider this for any user-facing forms, especially on mobile-first apps

**Problem - iOS users cannot select first option:**
```html
<script setup>
import { ref } from 'vue'

// Initial value is empty string, doesn't match any option
const selected = ref('')
</script>

<template>
  <!-- PROBLEM: On iOS, "Apple" appears selected but user cannot actually select it -->
  <!-- Tapping "Apple" does nothing because iOS doesn't fire change event -->
  <select v-model="selected">
    <option value="apple">Apple</option>
    <option value="banana">Banana</option>
    <option value="orange">Orange</option>
  </select>

  <!-- selected remains '' even though "Apple" appears highlighted -->
</template>
```

**Solution - Add disabled placeholder option:**
```html
<script setup>
import { ref } from 'vue'

const selected = ref('')  // Matches the placeholder option
</script>

<template>
  <!-- CORRECT: Disabled placeholder ensures user must actively select -->
  <select v-model="selected">
    <option disabled value="">Please select a fruit</option>
    <option value="apple">Apple</option>
    <option value="banana">Banana</option>
    <option value="orange">Orange</option>
  </select>
</template>
```

```html
<!-- Variant with required attribute for form validation -->
<select v-model="selected" required>
  <option disabled value="">-- Select an option --</option>
  <option value="a">Option A</option>
  <option value="b">Option B</option>
</select>
```

```html
<!-- If you MUST have a pre-selected default, set the initial value to match -->
<script setup>
import { ref } from 'vue'

// Set initial value to match an actual option
const country = ref('us')  // Pre-selects "United States"
</script>

<template>
  <select v-model="country">
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
    <option value="ca">Canada</option>
  </select>
</template>
```

## Reference
- [Vue.js Form Input Bindings - Select](https://vuejs.org/guide/essentials/forms.html#select)
```

## File: `skills/vue-debug-guides/reference/self-referencing-component-name.md`
```markdown
---
title: Self-Referencing Components Use Filename as Implicit Name
impact: LOW
impactDescription: Understanding this avoids confusion with recursive components
type: gotcha
tags: [vue3, component-registration, self-reference, recursive-components, sfc]
---

# Self-Referencing Components Use Filename as Implicit Name

**Impact: LOW** - In Single-File Components (SFC), a component can reference itself in its own template using its filename as the component name. This is useful for recursive components like tree structures or nested comments. However, this implicit registration has lower priority than explicitly imported components, which can cause confusion.

## Task Checklist

- [ ] Use the filename (without extension) to self-reference a component
- [ ] Be aware that imported components take precedence over self-reference
- [ ] For clarity in recursive components, consider explicit naming

**Example:**
```vue
<!-- TreeItem.vue -->
<script setup>
defineProps({
  item: Object
})
</script>

<template>
  <div class="tree-item">
    <span>{{ item.name }}</span>
    <!-- Self-reference using filename -->
    <TreeItem
      v-for="child in item.children"
      :key="child.id"
      :item="child"
    />
  </div>
</template>
```

```vue
<!-- Comment.vue - recursive comments -->
<script setup>
defineProps({
  comment: Object
})
</script>

<template>
  <div class="comment">
    <p>{{ comment.text }}</p>
    <div class="replies" v-if="comment.replies?.length">
      <!-- Self-reference for nested replies -->
      <Comment
        v-for="reply in comment.replies"
        :key="reply.id"
        :comment="reply"
      />
    </div>
  </div>
</template>
```

## Priority: Imports Override Self-Reference

```vue
<!-- FooBar.vue -->
<script setup>
// If you import a component named FooBar, it takes precedence
import FooBar from './different/FooBar.vue'
</script>

<template>
  <!-- This renders the IMPORTED FooBar, not this file -->
  <FooBar />
</template>
```

To explicitly self-reference when there's a naming conflict:

```vue
<!-- FooBar.vue -->
<script setup>
import OtherFooBar from './different/FooBar.vue'
// No way to explicitly import "self" in script setup
// Must rename the import to avoid conflict
</script>

<template>
  <OtherFooBar />
  <!-- FooBar still refers to self (this file) because
       the import was aliased -->
  <FooBar />
</template>
```

## Options API: Explicit Name Option

```vue
<!-- RecursiveList.vue -->
<script>
export default {
  name: 'RecursiveList', // Explicit name for self-reference
  props: {
    items: Array
  }
}
</script>

<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
      <RecursiveList v-if="item.children" :items="item.children" />
    </li>
  </ul>
</template>
```

## Common Use Cases for Self-Reference

1. **Tree structures** - File explorers, org charts
2. **Nested comments** - Reddit-style comment threads
3. **Menu navigation** - Recursive dropdown menus
4. **Category hierarchies** - Product categories, taxonomies

## Avoid Infinite Recursion

```vue
<!-- TreeNode.vue -->
<script setup>
defineProps({
  node: Object,
  maxDepth: { type: Number, default: 10 },
  currentDepth: { type: Number, default: 0 }
})
</script>

<template>
  <div class="node">
    {{ node.name }}
    <!-- Guard against infinite recursion -->
    <template v-if="node.children && currentDepth < maxDepth">
      <TreeNode
        v-for="child in node.children"
        :key="child.id"
        :node="child"
        :max-depth="maxDepth"
        :current-depth="currentDepth + 1"
      />
    </template>
  </div>
</template>
```

## Reference
- [Vue.js Component Registration](https://vuejs.org/guide/components/registration.html)
```

## File: `skills/vue-debug-guides/reference/sfc-named-exports-forbidden.md`
```markdown
---
title: SFC Script Block Must Use Default Export Only
impact: HIGH
impactDescription: Named exports in SFC script blocks will fail silently or cause build errors - Vue expects exactly one default export
type: gotcha
tags: [vue3, sfc, export, script-block, composition-api]
---

# SFC Script Block Must Use Default Export Only

**Impact: HIGH** - Vue Single-File Components expect exactly one default export from the `<script>` block. Using named exports for your component will cause build failures or runtime errors because Vue's tooling is designed to process a single default-exported component definition per `.vue` file.

## Task Checklist

- [ ] Always use `export default` in `<script>` blocks (Options API)
- [ ] Use `<script setup>` which handles exports automatically (Composition API)
- [ ] Move shared utilities to separate `.js`/`.ts` files, not the component's script block
- [ ] If you need to export types, use a separate `<script>` block alongside `<script setup>`

**Problematic Code:**
```vue
<!-- MyComponent.vue -->
<script>
// BAD: Named exports don't work for the component itself
export const MyComponent = {
  data() {
    return { count: 0 }
  }
}

// BAD: Exporting multiple things from component script
export const CONSTANT = 42
export function helper() { }
</script>

<template>
  <div>{{ count }}</div>
</template>
```

**Correct Code:**
```vue
<!-- MyComponent.vue - Options API -->
<script>
// GOOD: Single default export
export default {
  data() {
    return { count: 0 }
  }
}
</script>

<template>
  <div>{{ count }}</div>
</template>
```

```vue
<!-- MyComponent.vue - Composition API with script setup -->
<script setup>
// GOOD: No export needed, component is auto-exported
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <div>{{ count }}</div>
</template>
```

## Exporting Types Alongside Script Setup

For TypeScript, use a separate regular script block for type exports:

```vue
<script lang="ts">
// Regular script block for exports
export interface User {
  id: number
  name: string
}

export type Status = 'pending' | 'active' | 'inactive'
</script>

<script setup lang="ts">
// Setup script for component logic
import { ref } from 'vue'

const users = ref<User[]>([])
</script>

<template>
  <ul>
    <li v-for="user in users" :key="user.id">{{ user.name }}</li>
  </ul>
</template>
```

## Sharing Utilities Across Components

Don't put shared code in component script blocks. Create separate files:

```typescript
// utils/constants.ts
export const ITEMS_PER_PAGE = 20
export const API_BASE_URL = '/api/v1'

// utils/helpers.ts
export function formatDate(date: Date): string {
  return date.toLocaleDateString()
}

export function formatCurrency(amount: number): string {
  return `$${amount.toFixed(2)}`
}
```

```vue
<!-- ProductList.vue -->
<script setup>
// GOOD: Import shared utilities from external files
import { ITEMS_PER_PAGE } from '@/utils/constants'
import { formatCurrency } from '@/utils/helpers'
import { ref } from 'vue'

const products = ref([])
</script>
```

## Why This Restriction Exists

Vue's SFC compiler and build tools expect:

1. **One component per file**: The `.vue` file format is designed for single-component definitions
2. **Predictable structure**: Tools like Volar, vue-tsc, and bundler plugins assume default export
3. **Hot Module Replacement**: HMR relies on the single-component-per-file convention

```javascript
// How Vue tooling processes SFCs internally
import MyComponent from './MyComponent.vue'
// ^ Always expects the default export to be the component
```

## Common Mistake: Reusing Code via SFC Exports

```vue
<!-- BAD PATTERN: Trying to reuse code from components -->
<script>
// This won't work as expected
export const sharedLogic = () => { ... }

export default {
  // component definition
}
</script>
```

Instead, use composables:

```typescript
// composables/useSharedLogic.ts
export function useSharedLogic() {
  // Shared reactive logic
  const state = ref(0)
  const increment = () => state.value++

  return { state, increment }
}
```

```vue
<!-- ComponentA.vue -->
<script setup>
import { useSharedLogic } from '@/composables/useSharedLogic'

const { state, increment } = useSharedLogic()
</script>
```

## Reference
- [Vue.js SFC Specification](https://vuejs.org/api/sfc-spec.html)
- [Vue.js Composition API - Composables](https://vuejs.org/guide/reusability/composables.html)
```

## File: `skills/vue-debug-guides/reference/sfc-scoped-css-child-component-styling.md`
```markdown
---
title: Use Deep Selectors for Styling Child Component Elements
impact: HIGH
impactDescription: Scoped styles cannot target elements inside child components without deep selectors, leading to silently broken styles
type: gotcha
tags: [vue3, sfc, scoped-css, deep-selector, child-components]
---

# Use Deep Selectors for Styling Child Component Elements

**Impact: HIGH** - When using scoped CSS in Vue SFCs, styles do not penetrate into child components. Without using deep selectors (`:deep()`), your styles will silently fail to apply to elements rendered by child components or third-party libraries.

## Task Checklist

- [ ] Use `:deep()` selector to style elements inside child components
- [ ] Never use deprecated `>>>` or `/deep/` selectors (Vue 3 only supports `:deep()`)
- [ ] Scope deep selectors to a parent class when possible to limit impact
- [ ] Consider using unscoped styles or CSS modules for heavily nested styling

**Problematic Code:**
```vue
<template>
  <div class="container">
    <ThirdPartyDatePicker />
  </div>
</template>

<style scoped>
/* BAD: These styles won't apply to elements inside ThirdPartyDatePicker */
.container .date-input {
  border-color: blue;
}

.container .calendar-popup {
  background: white;
}
</style>
```

**Correct Code:**
```vue
<template>
  <div class="container">
    <ThirdPartyDatePicker />
  </div>
</template>

<style scoped>
/* GOOD: Use :deep() to style child component elements */
.container :deep(.date-input) {
  border-color: blue;
}

.container :deep(.calendar-popup) {
  background: white;
}

/* Also correct: deep selector at root level */
:deep(.date-picker-wrapper) {
  padding: 1rem;
}
</style>
```

## How Scoped CSS Works

Vue scoped CSS adds a unique data attribute to all elements in the component's template and appends it to CSS selectors:

```vue
<!-- Template output -->
<div class="container" data-v-7ba5bd90>
  <!-- Child component elements DON'T get data-v-7ba5bd90 -->
  <div class="date-input">...</div>
</div>
```

```css
/* Generated scoped CSS */
.container[data-v-7ba5bd90] .date-input[data-v-7ba5bd90] { ... }
/* ^ This won't match because .date-input doesn't have the attribute */
```

## Vue 3 Deep Selector Syntax

```vue
<style scoped>
/* Vue 3 recommended syntax */
.parent :deep(.child-class) {
  color: red;
}

/* DEPRECATED - don't use these in Vue 3 */
.parent >>> .child-class { }   /* Won't work in SCSS */
.parent /deep/ .child-class { } /* Deprecated */
.parent ::v-deep .child-class { } /* Old syntax */
</style>
```

## Scoping Deep Selectors for Safety

Always scope `:deep()` to a parent selector to limit its reach:

```vue
<style scoped>
/* BAD: Affects ALL .btn elements in child components globally */
:deep(.btn) {
  background: blue;
}

/* GOOD: Only affects .btn inside .my-component */
.my-component :deep(.btn) {
  background: blue;
}
</style>
```

## Child Component Root Element Exception

Note: A child component's root element IS affected by parent scoped CSS. This is intentional for layout purposes:

```vue
<!-- Parent.vue -->
<template>
  <ChildComponent class="styled-child" />
</template>

<style scoped>
/* This WILL work - targets child's root element */
.styled-child {
  margin: 1rem;
  border: 1px solid gray;
}
</style>
```

## Performance Consideration

Using `:deep()` with element selectors can be slower:

```vue
<style scoped>
/* SLOWER: Element selector with deep */
.container :deep(p) {
  color: red;
}

/* FASTER: Class selector with deep */
.container :deep(.paragraph) {
  color: red;
}
</style>
```

## Reference
- [Vue.js Scoped CSS - Deep Selectors](https://vuejs.org/api/sfc-css-features.html#deep-selectors)
- [Vue Loader Scoped CSS](https://vue-loader.vuejs.org/guide/scoped-css.html)
```

## File: `skills/vue-debug-guides/reference/sfc-scoped-css-dynamic-content.md`
```markdown
---
title: Scoped CSS Does Not Apply to Dynamically Added Content
impact: HIGH
impactDescription: Programmatically inserted DOM elements won't receive scoped style data attributes, causing styles to fail silently
type: gotcha
tags: [vue3, sfc, scoped-css, dynamic-content, v-html]
---

# Scoped CSS Does Not Apply to Dynamically Added Content

**Impact: HIGH** - Vue's scoped CSS works by adding data attributes to elements at compile time. Content added dynamically at runtime (via `v-html`, JavaScript DOM manipulation, or third-party libraries) won't have these attributes, so scoped styles won't apply.

## Task Checklist

- [ ] For `v-html` content, use `:deep()` selectors or unscoped styles
- [ ] Avoid programmatic DOM manipulation; prefer Vue's reactive template system
- [ ] When DOM manipulation is unavoidable, use global styles with unique class prefixes
- [ ] Consider CSS modules for content that mixes static and dynamic elements

**Problematic Code:**
```vue
<script setup>
import { ref } from 'vue'

const htmlContent = ref('<p class="dynamic">This is dynamic content</p>')
</script>

<template>
  <div class="container">
    <div v-html="htmlContent"></div>
  </div>
</template>

<style scoped>
/* BAD: Won't apply to the dynamic <p> element! */
.dynamic {
  color: red;
  font-weight: bold;
}
</style>
```

**Correct Code:**
```vue
<script setup>
import { ref } from 'vue'

const htmlContent = ref('<p class="dynamic">This is dynamic content</p>')
</script>

<template>
  <div class="container">
    <div v-html="htmlContent"></div>
  </div>
</template>

<style scoped>
/* GOOD: Use :deep() for v-html content */
.container :deep(.dynamic) {
  color: red;
  font-weight: bold;
}
</style>
```

## Why This Happens

Vue scoped CSS adds a unique data attribute (e.g., `data-v-7ba5bd90`) to:
1. All elements in the component's template (at compile time)
2. All CSS selectors

```html
<!-- What Vue generates at compile time -->
<div class="container" data-v-7ba5bd90>
  <div data-v-7ba5bd90>
    <!-- v-html content is inserted at runtime WITHOUT the attribute -->
    <p class="dynamic">This is dynamic content</p>
  </div>
</div>
```

```css
/* Generated scoped CSS */
.dynamic[data-v-7ba5bd90] { color: red; }
/* ^ Won't match because the dynamic <p> doesn't have data-v-7ba5bd90 */
```

## Alternative: Global Styles with Unique Prefix

```vue
<script setup>
import { ref } from 'vue'
const htmlContent = ref('<p class="my-component-dynamic">Dynamic text</p>')
</script>

<template>
  <div class="my-component">
    <div v-html="htmlContent"></div>
  </div>
</template>

<!-- Use unscoped styles with unique prefixes -->
<style>
.my-component .my-component-dynamic {
  color: red;
}
</style>
```

## Programmatic DOM Manipulation

When using third-party libraries that manipulate the DOM:

```vue
<script setup>
import { ref, onMounted } from 'vue'

const editorRef = ref(null)

onMounted(() => {
  // Third-party editor that injects its own DOM elements
  initRichEditor(editorRef.value)
})
</script>

<template>
  <div class="editor-wrapper">
    <div ref="editorRef"></div>
  </div>
</template>

<style scoped>
/* BAD: Won't reach injected editor elements */
.editor-toolbar { ... }
.editor-content { ... }
</style>

<style>
/* GOOD: Global styles scoped by parent class */
.editor-wrapper .editor-toolbar {
  background: #f5f5f5;
}
.editor-wrapper .editor-content {
  padding: 1rem;
}
</style>
```

## Best Practice: Prefer Reactive Templates

Instead of dynamic HTML, use Vue's reactive system when possible:

```vue
<script setup>
import { ref } from 'vue'

// BAD: Dynamic HTML that needs special style handling
const badHtml = ref('<span class="highlight">text</span>')

// GOOD: Reactive data that templates handle
const items = ref([
  { text: 'Item 1', isHighlighted: true },
  { text: 'Item 2', isHighlighted: false }
])
</script>

<template>
  <!-- BAD -->
  <div v-html="badHtml"></div>

  <!-- GOOD: Scoped styles work normally -->
  <ul>
    <li
      v-for="item in items"
      :key="item.text"
      :class="{ highlight: item.isHighlighted }"
    >
      {{ item.text }}
    </li>
  </ul>
</template>

<style scoped>
/* Works perfectly with reactive template */
.highlight {
  background: yellow;
}
</style>
```

## Reference
- [Vue.js Scoped CSS](https://vuejs.org/api/sfc-css-features.html#scoped-css)
- [GitHub Issue: Scoped CSS not applied for programmatically added elements](https://github.com/vuejs/vue/issues/7649)
```

## File: `skills/vue-debug-guides/reference/sfc-scoped-css-slot-content.md`
```markdown
---
title: Scoped CSS Cannot Style Slot Content Directly
impact: HIGH
impactDescription: Slot content receives the parent component's scope, not the child's, causing styles to fail unexpectedly
type: gotcha
tags: [vue3, sfc, scoped-css, slots, deep-selector]
---

# Scoped CSS Cannot Style Slot Content Directly

**Impact: HIGH** - When a parent passes content through a slot, that content receives the parent component's scoped style attributes, not the child component's. This means the child component cannot style slot content with regular scoped CSS.

## Task Checklist

- [ ] Use `:deep()` selector in the wrapper component to style slot content
- [ ] Alternatively, use `:slotted()` pseudo-selector to target slotted elements
- [ ] For complex slot styling, consider using CSS modules or unscoped styles
- [ ] Document expected slot content structure when styling assumptions exist

**Problematic Code:**
```vue
<!-- Card.vue (child component) -->
<template>
  <div class="card">
    <div class="card-body">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.card-body {
  padding: 1rem;
}

/* BAD: Won't apply to slot content! */
.card-body h2 {
  color: #333;
  margin-bottom: 0.5rem;
}

.card-body p {
  color: #666;
}
</style>
```

```vue
<!-- Parent.vue -->
<template>
  <Card>
    <!-- This h2 and p won't be styled by Card's scoped CSS -->
    <h2>Card Title</h2>
    <p>Card description text.</p>
  </Card>
</template>
```

**Correct Code:**
```vue
<!-- Card.vue - Using :slotted() -->
<template>
  <div class="card">
    <div class="card-body">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.card-body {
  padding: 1rem;
}

/* GOOD: :slotted() targets slot content */
:slotted(h2) {
  color: #333;
  margin-bottom: 0.5rem;
}

:slotted(p) {
  color: #666;
}
</style>
```

## Using :deep() Alternative

```vue
<!-- Card.vue - Using :deep() -->
<style scoped>
.card-body {
  padding: 1rem;
}

/* :deep() also works for slot content */
.card-body :deep(h2) {
  color: #333;
}

.card-body :deep(p) {
  color: #666;
}
</style>
```

## Why This Happens

Slot content is compiled in the parent component's scope:

```vue
<!-- Parent template compiles to: -->
<Card>
  <h2 data-v-parent123>Card Title</h2>
  <p data-v-parent123>Card description</p>
</Card>

<!-- Card template compiles to: -->
<div class="card" data-v-card456>
  <div class="card-body" data-v-card456>
    <slot />  <!-- Content inserted WITHOUT data-v-card456 -->
  </div>
</div>
```

The `<h2>` has `data-v-parent123`, but Card's scoped CSS expects `data-v-card456`.

## :slotted() vs :deep() for Slots

Both work, but have subtle differences:

```vue
<style scoped>
/* :slotted() - Specifically for slot content */
/* Only targets direct slotted elements */
:slotted(h2) {
  color: blue;
}

/* :deep() - More general deep selector */
/* Can target nested elements within slot content */
.card-body :deep(h2) {
  color: blue;
}

/* For nested elements in slot content, must use :deep() */
:slotted(.wrapper h2) { }  /* Won't work for nested h2 */
.card-body :deep(.wrapper h2) { }  /* Works for nested */
</style>
```

## Combining with Named Slots

```vue
<template>
  <div class="card">
    <header class="card-header">
      <slot name="header" />
    </header>
    <div class="card-body">
      <slot />
    </div>
    <footer class="card-footer">
      <slot name="footer" />
    </footer>
  </div>
</template>

<style scoped>
/* Style specific slot content */
.card-header :slotted(h1),
.card-header :slotted(h2) {
  margin: 0;
  font-size: 1.25rem;
}

.card-body :slotted(p) {
  margin-bottom: 1rem;
}

.card-footer :slotted(button) {
  margin-right: 0.5rem;
}
</style>
```

## Performance Tip: Use Classes

Element selectors with `:slotted()` can be slower:

```vue
<style scoped>
/* SLOWER: Element selector */
:slotted(p) {
  color: gray;
}

/* FASTER: Class selector */
:slotted(.card-text) {
  color: gray;
}
</style>
```

## When to Use Unscoped Styles

For complex slot styling, unscoped styles may be cleaner:

```vue
<template>
  <article class="article-card">
    <slot />
  </article>
</template>

<style>
/* Unscoped with unique prefix for complex content styling */
.article-card h1,
.article-card h2,
.article-card h3 {
  font-family: Georgia, serif;
  line-height: 1.2;
}

.article-card p {
  line-height: 1.6;
}

.article-card img {
  max-width: 100%;
}

.article-card blockquote {
  border-left: 3px solid #ccc;
  padding-left: 1rem;
}
</style>
```

## Reference
- [Vue.js Scoped CSS - Slotted Selectors](https://vuejs.org/api/sfc-css-features.html#slotted-selectors)
- [Vue.js Deep Selectors](https://vuejs.org/api/sfc-css-features.html#deep-selectors)
```

## File: `skills/vue-debug-guides/reference/sfc-script-setup-reactivity.md`
```markdown
---
title: Variables in Script Setup Are Not Reactive by Default
impact: HIGH
impactDescription: Forgetting to wrap variables with ref() or reactive() causes silent reactivity failures in script setup
type: gotcha
tags: [vue3, sfc, script-setup, reactivity, ref, composition-api]
---

# Variables in Script Setup Are Not Reactive by Default

**Impact: HIGH** - Unlike Options API's `data()` which automatically makes properties reactive, variables declared in `<script setup>` are plain JavaScript values. You must explicitly use `ref()` or `reactive()` to make them reactive. Forgetting this causes the UI to not update when values change.

## Task Checklist

- [ ] Always wrap primitive values (strings, numbers, booleans) with `ref()`
- [ ] Use `reactive()` for objects when you don't need to reassign the whole object
- [ ] Remember to access `.value` on refs in script (not needed in templates)
- [ ] Use `computed()` from Vue, not a plain function, for derived reactive state

**Problematic Code:**
```vue
<script setup>
// BAD: These are NOT reactive!
let count = 0
let message = 'Hello'
let user = { name: 'John', age: 30 }

function increment() {
  count++  // This change won't update the UI!
}

function updateMessage() {
  message = 'World'  // UI won't reflect this change!
}
</script>

<template>
  <div>
    <!-- Will always show initial values -->
    <p>Count: {{ count }}</p>
    <p>Message: {{ message }}</p>
    <button @click="increment">Increment</button>
    <button @click="updateMessage">Update</button>
  </div>
</template>
```

**Correct Code:**
```vue
<script setup>
import { ref, reactive, computed } from 'vue'

// GOOD: Primitives wrapped with ref()
const count = ref(0)
const message = ref('Hello')

// GOOD: Object with reactive()
const user = reactive({ name: 'John', age: 30 })

// GOOD: Computed for derived state
const doubleCount = computed(() => count.value * 2)

function increment() {
  count.value++  // Use .value for refs in script
}

function updateMessage() {
  message.value = 'World'
}

function updateUser() {
  user.name = 'Jane'  // No .value needed for reactive objects
}
</script>

<template>
  <div>
    <!-- No .value needed in templates - Vue unwraps automatically -->
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <p>Message: {{ message }}</p>
    <p>User: {{ user.name }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```

## Common Mistake: Plain Computed

```vue
<script setup>
import { ref } from 'vue'

const items = ref([1, 2, 3, 4, 5])

// BAD: Plain function, not reactive - won't update when items change
const total = items.value.reduce((sum, n) => sum + n, 0)

// BAD: Arrow function - recalculates but Vue doesn't track it
const getTotal = () => items.value.reduce((sum, n) => sum + n, 0)
</script>

<template>
  <!-- total never updates, getTotal works but isn't optimal -->
  <p>Total: {{ total }}</p>
</template>
```

```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([1, 2, 3, 4, 5])

// GOOD: computed() tracks dependencies and caches result
const total = computed(() => items.value.reduce((sum, n) => sum + n, 0))
</script>

<template>
  <p>Total: {{ total }}</p>  <!-- Updates when items change -->
</template>
```

## When to Use ref() vs reactive()

```vue
<script setup>
import { ref, reactive } from 'vue'

// Use ref() for:
// - Primitives (string, number, boolean)
// - Values you might reassign entirely
const count = ref(0)
const isLoading = ref(false)
const selectedId = ref<number | null>(null)

// Use reactive() for:
// - Objects/arrays you'll mutate but not reassign
// - When you want to avoid .value
const form = reactive({
  name: '',
  email: '',
  errors: []
})

// Gotcha: Can't reassign reactive objects
const user = reactive({ name: 'John' })
// user = { name: 'Jane' }  // This breaks reactivity!
// user.name = 'Jane'       // This works

// Use ref() if you need to reassign objects
const userData = ref({ name: 'John' })
userData.value = { name: 'Jane' }  // This works
</script>
```

## Template Automatic Unwrapping

Vue automatically unwraps refs in templates:

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const user = ref({ name: 'John' })
</script>

<template>
  <!-- All of these work - no .value needed -->
  <p>{{ count }}</p>
  <p>{{ user.name }}</p>
  <input v-model="count" type="number">
  <button @click="count++">Increment</button>
</template>
```

But in event handlers written inline, you might still need `.value`:

```vue
<template>
  <!-- This works (Vue handles it) -->
  <button @click="count++">+1</button>

  <!-- For complex logic, .value may be needed -->
  <button @click="() => { count.value = Math.max(0, count.value - 1) }">
    -1 (min 0)
  </button>
</template>
```

## Reference
- [Vue.js Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)
- [Vue.js ref()](https://vuejs.org/api/reactivity-core.html#ref)
- [Vue.js reactive()](https://vuejs.org/api/reactivity-core.html#reactive)
```

## File: `skills/vue-debug-guides/reference/slot-forwarding-to-child-components.md`
```markdown
---
title: Forward Slots to Child Components Correctly
impact: MEDIUM
impactDescription: Wrapper components that don't forward slots break slot functionality for consumers
type: best-practice
tags: [vue3, slots, component-composition, wrapper-components, slot-forwarding]
---

# Forward Slots to Child Components Correctly

**Impact: MEDIUM** - When creating wrapper components that enhance or extend other components, you need to forward slots from the parent to the wrapped child. Without proper slot forwarding, consumers of your wrapper cannot customize the inner component's slots.

## Task Checklist

- [ ] Use `v-for` with `$slots` to iterate over all provided slots
- [ ] Use dynamic slot names with `v-slot:[slotName]`
- [ ] Pass slot props through with `v-bind="slotProps"`
- [ ] Handle cases where slotProps might be undefined

**Basic Slot Forwarding Pattern:**
```vue
<!-- EnhancedButton.vue - Wrapper component -->
<script setup>
import BaseButton from './BaseButton.vue'
</script>

<template>
  <div class="button-wrapper">
    <BaseButton v-bind="$attrs">
      <!-- Forward all slots to BaseButton -->
      <template v-for="(_, slotName) in $slots" v-slot:[slotName]="slotProps">
        <slot :name="slotName" v-bind="slotProps ?? {}" />
      </template>
    </BaseButton>
  </div>
</template>
```

**Usage:**
```vue
<script setup>
import EnhancedButton from './EnhancedButton.vue'
</script>

<template>
  <!-- Slots pass through to BaseButton -->
  <EnhancedButton>
    <template #icon>
      <IconCheck />
    </template>
    <template #default>
      Click me
    </template>
  </EnhancedButton>
</template>
```

## Handling Scoped Slots

When the child component provides slot props, you must forward them:

```vue
<!-- DataTableWrapper.vue -->
<script setup>
import DataTable from './DataTable.vue'

const props = defineProps(['data'])
</script>

<template>
  <div class="table-container">
    <DataTable :items="data">
      <!-- Forward slots including scoped slot props -->
      <template v-for="(_, slotName) in $slots" v-slot:[slotName]="slotProps">
        <slot :name="slotName" v-bind="slotProps ?? {}" />
      </template>
    </DataTable>
  </div>
</template>
```

```vue
<!-- Consumer can use scoped slot props -->
<DataTableWrapper :data="users">
  <template #row="{ item, index }">
    <tr>
      <td>{{ index + 1 }}</td>
      <td>{{ item.name }}</td>
    </tr>
  </template>
</DataTableWrapper>
```

## Alternative: Handling Undefined slotProps

Some scenarios require checking if slotProps exists:

```vue
<template>
  <ChildComponent>
    <template v-for="(_, name) in $slots" v-slot:[name]="slotProps">
      <!-- Handle both scoped and non-scoped slots -->
      <slot v-if="slotProps" :name="name" v-bind="slotProps" />
      <slot v-else :name="name" />
    </template>
  </ChildComponent>
</template>
```

## Forwarding Specific Slots Only

If you only want to forward certain slots:

```vue
<template>
  <ChildComponent>
    <!-- Only forward header and footer slots -->
    <template v-if="$slots.header" #header="slotProps">
      <slot name="header" v-bind="slotProps ?? {}" />
    </template>

    <template v-if="$slots.footer" #footer="slotProps">
      <slot name="footer" v-bind="slotProps ?? {}" />
    </template>

    <!-- Default slot handled differently -->
    <slot />
  </ChildComponent>
</template>
```

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Not using `v-bind="slotProps"` | Scoped slot data lost | Always bind slotProps |
| Forgetting `?? {}` or null check | Error when slotProps undefined | Add nullish coalescing |
| Static slot names in loop | Only forwards one slot | Use `v-slot:[slotName]` dynamic syntax |
| Missing `v-for` key warning | Vue warning (non-critical) | Keys not needed for slot functions |

## Reference
- [Vue Land FAQ - Forwarding Slots](https://vue-land.github.io/faq/forwarding-slots)
- [Vue.js Slots - Scoped Slots](https://vuejs.org/guide/components/slots.html#scoped-slots)
```

## File: `skills/vue-debug-guides/reference/slot-implicit-default-content.md`
```markdown
---
title: Non-Template Content Is Implicitly Default Slot Content
impact: LOW
impactDescription: Unexpected content placement when mixing named slots with loose content
type: gotcha
tags: [vue3, slots, named-slots, default-slot, implicit-behavior]
---

# Non-Template Content Is Implicitly Default Slot Content

**Impact: LOW** - When using named slots, any top-level content not wrapped in a `<template>` tag is automatically treated as default slot content. This implicit behavior can cause confusion about where content will render.

## Task Checklist

- [ ] Understand that loose content goes to the default slot
- [ ] Use explicit `<template #default>` when clarity matters
- [ ] Keep slot content organization intentional

**The Implicit Behavior:**
```vue
<script setup>
import BaseLayout from './BaseLayout.vue'
</script>

<template>
  <BaseLayout>
    <template #header>
      <h1>Page Title</h1>
    </template>

    <!-- These are IMPLICITLY in the default slot -->
    <p>First paragraph of main content.</p>
    <p>Second paragraph of main content.</p>

    <template #footer>
      <p>Footer content</p>
    </template>
  </BaseLayout>
</template>
```

The two `<p>` elements are automatically placed in `<slot>` (the default slot) in the child component.

**Equivalent Explicit Version:**
```vue
<template>
  <BaseLayout>
    <template #header>
      <h1>Page Title</h1>
    </template>

    <!-- Explicit default slot -->
    <template #default>
      <p>First paragraph of main content.</p>
      <p>Second paragraph of main content.</p>
    </template>

    <template #footer>
      <p>Footer content</p>
    </template>
  </BaseLayout>
</template>
```

## When Implicit Behavior Causes Confusion

**Scattered Content:**
```vue
<template>
  <BaseLayout>
    <template #header>
      <h1>Title</h1>
    </template>

    <p>Content A</p>  <!-- Goes to default slot -->

    <template #sidebar>
      <nav>Navigation</nav>
    </template>

    <p>Content B</p>  <!-- Also goes to default slot! -->

    <template #footer>
      <p>Footer</p>
    </template>

    <p>Content C</p>  <!-- Also goes to default slot! -->
  </BaseLayout>
</template>
```

All three `<p>` elements end up in the default slot together, which may not be the intended order or grouping.

**Clearer with Explicit Default:**
```vue
<template>
  <BaseLayout>
    <template #header>
      <h1>Title</h1>
    </template>

    <template #default>
      <p>Content A</p>
      <p>Content B</p>
      <p>Content C</p>
    </template>

    <template #sidebar>
      <nav>Navigation</nav>
    </template>

    <template #footer>
      <p>Footer</p>
    </template>
  </BaseLayout>
</template>
```

## Best Practices

| Scenario | Recommendation |
|----------|---------------|
| Only default slot used | Implicit is fine |
| Mixed named + default slots | Consider explicit `#default` |
| Complex layouts | Always use explicit templates |
| Team/shared codebase | Prefer explicit for clarity |

## The Child Component

```vue
<!-- BaseLayout.vue -->
<template>
  <div class="layout">
    <header>
      <slot name="header"></slot>
    </header>

    <aside>
      <slot name="sidebar"></slot>
    </aside>

    <main>
      <!-- All implicit content ends up here -->
      <slot></slot>
    </main>

    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>
```

## Reference
- [Vue.js Slots - Named Slots](https://vuejs.org/guide/components/slots.html#named-slots)
```

## File: `skills/vue-debug-guides/reference/slot-name-reserved-prop.md`
```markdown
---
title: Slot Name is Reserved and Not Included in Slot Props
impact: LOW
impactDescription: Expecting 'name' in scoped slot props when it's reserved causes confusion
type: gotcha
tags: [vue3, slots, scoped-slots, reserved-props, naming]
---

# Slot Name is Reserved and Not Included in Slot Props

**Impact: LOW** - When using scoped slots, the `name` attribute on the `<slot>` element is reserved for identifying the slot. It is not passed as part of the slot props to the parent component.

## Task Checklist

- [ ] Don't expect `name` in slot props - it's reserved
- [ ] Use a different prop name if you need to pass a name value
- [ ] Remember only explicitly bound attributes become slot props

**Incorrect Expectation:**
```vue
<!-- ChildComponent.vue -->
<template>
  <div>
    <slot name="header" title="Welcome"></slot>
  </div>
</template>
```

```vue
<!-- ParentComponent.vue -->
<ChildComponent>
  <template #header="props">
    <!-- props = { title: "Welcome" } -->
    <!-- 'name' is NOT included! -->
    {{ props.name }}  <!-- undefined -->
    {{ props.title }} <!-- "Welcome" -->
  </template>
</ChildComponent>
```

**If You Need to Pass a "Name" Value:**
```vue
<!-- ChildComponent.vue -->
<template>
  <div>
    <!-- Use a different prop name like 'slotName' or 'label' -->
    <slot name="header" :label="slotLabel" :title="title"></slot>
  </div>
</template>

<script setup>
const slotLabel = 'header'
const title = 'Welcome'
</script>
```

```vue
<!-- ParentComponent.vue -->
<ChildComponent>
  <template #header="{ label, title }">
    <h2>{{ title }}</h2>
    <span>Section: {{ label }}</span>
  </template>
</ChildComponent>
```

## What Gets Passed as Slot Props

| Attribute on `<slot>` | Passed to Parent? |
|----------------------|-------------------|
| `name` | No (reserved for slot identification) |
| `:text="message"` | Yes, as `text` |
| `:count="5"` | Yes, as `count` |
| `v-bind="object"` | Yes, spreads object properties |
| `class="..."` | No (not bound with `:`) |

## Multiple Named Slots Example

```vue
<!-- TabPanel.vue -->
<template>
  <div class="tabs">
    <slot name="tab1" :active="activeTab === 1" :label="'First Tab'"></slot>
    <slot name="tab2" :active="activeTab === 2" :label="'Second Tab'"></slot>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const activeTab = ref(1)
</script>
```

```vue
<!-- Usage -->
<TabPanel>
  <template #tab1="{ active, label }">
    <!-- 'name' not available, but 'label' is -->
    <button :class="{ active }">{{ label }}</button>
  </template>

  <template #tab2="{ active, label }">
    <button :class="{ active }">{{ label }}</button>
  </template>
</TabPanel>
```

## Reference
- [Vue.js Slots - Scoped Slots](https://vuejs.org/guide/components/slots.html#scoped-slots)
```

## File: `skills/vue-debug-guides/reference/slot-named-scoped-explicit-default.md`
```markdown
---
title: Use Explicit Default Template When Mixing Named and Scoped Slots
impact: HIGH
impactDescription: Mixing v-slot on component with named slots inside causes ambiguous scope and compilation errors
type: gotcha
tags: [vue3, slots, scoped-slots, named-slots, compilation-error]
---

# Use Explicit Default Template When Mixing Named and Scoped Slots

**Impact: HIGH** - When a component uses both the default scoped slot and named slots, you must use an explicit `<template #default>` for the default slot. Using `v-slot` directly on the component while having nested named slot templates causes scope ambiguity and compilation errors.

## Task Checklist

- [ ] When using named slots alongside a default slot with props, always use explicit `<template #default>`
- [ ] Never mix `v-slot` on the component element with `<template #name>` inside
- [ ] Keep slot scope clear and unambiguous

**Incorrect:**
```vue
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<template>
  <!-- BAD: v-slot on component + named template inside causes ambiguity -->
  <MyComponent v-slot="{ message }">
    <p>{{ message }}</p>

    <template #footer>
      <!-- Ambiguous: Is 'message' available here? Vue can't determine -->
      <p>Footer: {{ message }}</p>
    </template>
  </MyComponent>
</template>
```

This causes a compilation error because Vue cannot determine:
1. Whether `message` from the default slot should be available in the footer slot
2. Which scope applies to the non-template content

**Correct:**
```vue
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<template>
  <!-- GOOD: Explicit template for each slot with clear scope -->
  <MyComponent>
    <template #default="{ message }">
      <p>{{ message }}</p>
    </template>

    <template #footer>
      <!-- Clear: footer slot has its own scope, no access to default's 'message' -->
      <p>Footer content here</p>
    </template>
  </MyComponent>
</template>
```

**Correct - When Footer Also Has Props:**
```vue
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<template>
  <MyComponent>
    <template #default="{ message }">
      <p>{{ message }}</p>
    </template>

    <template #footer="{ year }">
      <!-- Each slot receives its own props -->
      <p>Copyright {{ year }}</p>
    </template>
  </MyComponent>
</template>
```

## The Rule

When you have **any** named slots (`<template #name>`), always use explicit templates for **all** slots, including the default slot. This makes scope boundaries clear and prevents compilation errors.

| Pattern | Valid? | Notes |
|---------|--------|-------|
| `v-slot` on component only | Yes | Single default scoped slot |
| Named templates only | Yes | Multiple named slots |
| `v-slot` on component + named templates | No | Ambiguous scope |
| All explicit templates | Yes | Clear scope for each slot |

## Reference
- [Vue.js Slots - Named Scoped Slots](https://vuejs.org/guide/components/slots.html#named-scoped-slots)
```

## File: `skills/vue-debug-guides/reference/slot-render-scope-parent-only.md`
```markdown
---
title: Slot Content Only Has Access to Parent Component Scope
impact: HIGH
impactDescription: Attempting to access child component data in slot content results in undefined values or errors
type: gotcha
tags: [vue3, slots, scope, reactivity, common-mistake]
---

# Slot Content Only Has Access to Parent Component Scope

**Impact: HIGH** - Slot content is compiled in the parent component's scope and cannot access data defined in the child component. This follows JavaScript's lexical scoping rules and is a common source of confusion.

When you provide content for a slot, that content is defined in your parent template and can only access data available in the parent component. The child component's internal state is not accessible unless explicitly passed via scoped slots.

## Task Checklist

- [ ] Remember that slot content is compiled in parent scope
- [ ] Never try to access child component data directly in slot content
- [ ] Use scoped slots when child data needs to be exposed to parent
- [ ] Check that all template expressions reference data available in the current component

**Incorrect:**
```vue
<!-- Parent.vue -->
<script setup>
import SubmitButton from './SubmitButton.vue'
</script>

<template>
  <!-- BAD: Trying to access child's buttonText - this will be undefined -->
  <SubmitButton>{{ buttonText }}</SubmitButton>

  <!-- BAD: Trying to access child's isLoading state -->
  <SubmitButton>
    <span v-if="isLoading">Loading...</span>
    <span v-else>Submit</span>
  </SubmitButton>
</template>
```

```vue
<!-- SubmitButton.vue (Child) -->
<script setup>
import { ref } from 'vue'

const buttonText = ref('Click me')  // Not accessible in parent's slot content
const isLoading = ref(false)        // Not accessible in parent's slot content
</script>

<template>
  <button>
    <slot></slot>
  </button>
</template>
```

**Correct - Use Scoped Slots:**
```vue
<!-- SubmitButton.vue (Child) - Expose data via slot props -->
<script setup>
import { ref } from 'vue'

const buttonText = ref('Click me')
const isLoading = ref(false)
</script>

<template>
  <button>
    <!-- Pass child data as slot props -->
    <slot :text="buttonText" :loading="isLoading"></slot>
  </button>
</template>
```

```vue
<!-- Parent.vue -->
<script setup>
import SubmitButton from './SubmitButton.vue'
</script>

<template>
  <!-- GOOD: Receive child data via scoped slot -->
  <SubmitButton v-slot="{ text, loading }">
    <span v-if="loading">Loading...</span>
    <span v-else>{{ text }}</span>
  </SubmitButton>
</template>
```

**Correct - Use Parent Data:**
```vue
<!-- Parent.vue -->
<script setup>
import { ref } from 'vue'
import SubmitButton from './SubmitButton.vue'

// Define data in parent where slot content is compiled
const message = ref('Submit Form')
const isSubmitting = ref(false)
</script>

<template>
  <!-- GOOD: Using parent's own data in slot content -->
  <SubmitButton>
    <span v-if="isSubmitting">Processing...</span>
    <span v-else>{{ message }}</span>
  </SubmitButton>
</template>
```

## The Function Analogy

Think of slots as function parameters:

```javascript
// Slot content is like a callback defined in parent scope
function Parent() {
  const parentData = 'Hello'

  // This callback can only see parentData, not childData
  Child((slotProps) => {
    return parentData + (slotProps?.text || '')
  })
}

function Child(slotCallback) {
  const childData = 'World'  // Not visible to callback

  // Must explicitly pass data via slot props
  return slotCallback({ text: childData })
}
```

## Reference
- [Vue.js Slots - Render Scope](https://vuejs.org/guide/components/slots.html#render-scope)
```

## File: `skills/vue-debug-guides/reference/slot-v-slot-on-components-or-templates-only.md`
```markdown
---
title: v-slot Can Only Be Used on Components or Template Tags
impact: HIGH
impactDescription: Using v-slot on HTML elements causes compilation errors
type: gotcha
tags: [vue3, slots, v-slot, compilation-error, common-mistake]
---

# v-slot Can Only Be Used on Components or Template Tags

**Impact: HIGH** - The `v-slot` directive (and its shorthand `#`) can only be used on Vue components or `<template>` tags. Using it on native HTML elements like `<div>` or `<span>` causes a Vue compilation error.

## Task Checklist

- [ ] Only use `v-slot` on component elements or `<template>` tags
- [ ] When using default scoped slot shorthand, apply to the component itself
- [ ] For named slots, always use `<template #name>` syntax

**Incorrect:**
```vue
<template>
  <!-- BAD: v-slot on a native HTML element -->
  <div v-slot:header>
    <h1>Title</h1>
  </div>

  <!-- BAD: Shorthand on HTML element -->
  <span #default="{ item }">
    {{ item.name }}
  </span>

  <!-- BAD: v-slot inside a plain HTML element -->
  <div>
    <p v-slot:content>Some text</p>
  </div>
</template>
```

These cause the error: `v-slot can only be used on components or <template> tags`

**Correct:**
```vue
<template>
  <!-- GOOD: v-slot on component element (default scoped slot) -->
  <MyComponent v-slot="{ item }">
    {{ item.name }}
  </MyComponent>

  <!-- GOOD: Named slots use template tags -->
  <BaseLayout>
    <template #header>
      <h1>Title</h1>
    </template>

    <template #default>
      <p>Main content</p>
    </template>

    <template #footer>
      <p>Footer content</p>
    </template>
  </BaseLayout>

  <!-- GOOD: Shorthand on component for default slot -->
  <FancyList #default="{ item }">
    <div>{{ item.name }}</div>
  </FancyList>
</template>
```

## Common Scenarios

### Wrapping Slot Content in HTML
If you need HTML wrappers around slot content, put them inside the template:

```vue
<!-- WRONG -->
<MyComponent>
  <div v-slot:header class="header-wrapper">
    <h1>Title</h1>
  </div>
</MyComponent>

<!-- CORRECT -->
<MyComponent>
  <template #header>
    <div class="header-wrapper">
      <h1>Title</h1>
    </div>
  </template>
</MyComponent>
```

### Multiple v-slot on Same Element
Another error occurs when you have multiple v-slot directives - only the first is recognized:

```vue
<!-- BAD: Multiple v-slot directives -->
<MyComponent v-slot:header v-slot:footer>
  Content
</MyComponent>

<!-- GOOD: Separate template for each slot -->
<MyComponent>
  <template #header>Header</template>
  <template #footer>Footer</template>
</MyComponent>
```

## Valid v-slot Locations

| Element Type | v-slot Allowed? | Example |
|--------------|-----------------|---------|
| Component | Yes | `<MyComponent v-slot="props">` |
| `<template>` | Yes | `<template #header>` |
| `<div>` | No | Compilation error |
| `<span>` | No | Compilation error |
| Any HTML element | No | Compilation error |

## Reference
- [Vue.js Slots](https://vuejs.org/guide/components/slots.html)
- [DeepScan - vue-misused-v-slot](https://deepscan.io/docs/rules/vue-misused-v-slot)
```

## File: `skills/vue-debug-guides/reference/ssr-hydration-mismatch-causes.md`
```markdown
---
title: Understand and Fix SSR Hydration Mismatches
impact: HIGH
impactDescription: Hydration mismatches cause visual flickering, performance loss, and broken functionality
type: gotcha
tags: [vue3, ssr, hydration, debugging, nuxt, server-side-rendering]
---

# Understand and Fix SSR Hydration Mismatches

**Impact: HIGH** - Hydration mismatches occur when the HTML rendered on the client differs from what the server rendered. Vue attempts to recover by discarding and re-rendering mismatched nodes, causing performance degradation, visual flickering, and potentially broken event handlers.

Understanding the common causes helps you prevent and debug these issues effectively.

## Task Checklist

- [ ] Validate HTML structure for proper nesting (no div in p, no nested a tags)
- [ ] Move random value generation to onMounted or use seeded randoms
- [ ] Format dates/times on client side only
- [ ] Use `data-allow-mismatch` (Vue 3.5+) for intentional mismatches
- [ ] Check for browser-modified HTML in dev tools

## Cause 1: Invalid HTML Nesting

Browsers auto-correct invalid HTML, creating different DOM than Vue expects.

**Incorrect:**
```vue
<template>
  <!-- WRONG: <div> cannot be inside <p> -->
  <p>
    <div>This will break hydration</div>
  </p>

  <!-- WRONG: <a> cannot be inside <a> -->
  <a href="/parent">
    <a href="/child">Nested link</a>
  </a>

  <!-- WRONG: Block elements in inline elements -->
  <span>
    <div>Block in inline</div>
  </span>
</template>
```

Browser converts the first example to:
```html
<p></p>
<div>This will break hydration</div>
<p></p>
```

**Correct:**
```vue
<template>
  <!-- CORRECT: Use appropriate nesting -->
  <div>
    <div>This works fine</div>
  </div>

  <!-- CORRECT: Single link with event handling -->
  <a href="/parent" @click="handleParentClick">
    <span @click.stop="handleChildClick">Nested action</span>
  </a>

  <!-- CORRECT: Block element wrapper -->
  <div>
    <div>Block in block</div>
  </div>
</template>
```

## Cause 2: Random Values in Render

Server and client generate different random values.

**Incorrect:**
```vue
<template>
  <!-- WRONG: Different ID on server vs client -->
  <div :id="'field-' + Math.random()">
    Form field
  </div>

  <!-- WRONG: Random order differs -->
  <div v-for="item in shuffledItems" :key="item.id">
    {{ item.name }}
  </div>
</template>

<script setup>
import { computed } from 'vue'

const items = [/* ... */]

// WRONG: Random shuffle runs differently on server and client
const shuffledItems = computed(() =>
  [...items].sort(() => Math.random() - 0.5)
)
</script>
```

**Correct - Client-Only Random:**
```vue
<template>
  <div :id="fieldId">
    Form field
  </div>

  <div v-for="item in displayItems" :key="item.id">
    {{ item.name }}
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const items = [/* ... */]

// CORRECT: Start with deterministic value
const fieldId = ref('field-default')
const displayItems = ref(items) // Original order on server

onMounted(() => {
  // Randomize only on client
  fieldId.value = 'field-' + Math.random().toString(36).slice(2)
  displayItems.value = [...items].sort(() => Math.random() - 0.5)
})
</script>
```

**Correct - Seeded Random:**
```javascript
// utils/seededRandom.js
export function createSeededRandom(seed) {
  return function() {
    seed = (seed * 9301 + 49297) % 233280
    return seed / 233280
  }
}

// Use same seed on server and client
const seed = 12345 // Could be based on user ID, page, etc.
const random = createSeededRandom(seed)
```

## Cause 3: Timezone and Date Differences

Server may be in different timezone than client.

**Incorrect:**
```vue
<template>
  <!-- WRONG: Server time != client time -->
  <span>{{ new Date().toLocaleTimeString() }}</span>

  <!-- WRONG: Server formats dates in server's timezone -->
  <span>{{ formatDate(article.createdAt) }}</span>
</template>

<script setup>
function formatDate(date) {
  return new Date(date).toLocaleDateString()
}
</script>
```

**Correct:**
```vue
<template>
  <!-- CORRECT: Render placeholder, update on client -->
  <span>{{ displayTime || 'Loading...' }}</span>

  <!-- CORRECT: Use UTC or defer to client -->
  <span>{{ formattedDate }}</span>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps(['article'])
const displayTime = ref(null)
const isClient = ref(false)

onMounted(() => {
  displayTime.value = new Date().toLocaleTimeString()
  isClient.value = true
})

// CORRECT: Server renders UTC, client converts to local
const formattedDate = computed(() => {
  if (!props.article?.createdAt) return ''

  if (isClient.value) {
    // Client: user's local timezone
    return new Date(props.article.createdAt).toLocaleDateString()
  } else {
    // Server: consistent UTC format
    return new Date(props.article.createdAt).toISOString().split('T')[0]
  }
})
</script>
```

## Cause 4: Browser Extensions and Modifications

Browser extensions can inject content into the DOM.

**Mitigation:**
```vue
<template>
  <!-- Use data-allow-mismatch for areas extensions might modify -->
  <head data-allow-mismatch>
    <title>{{ pageTitle }}</title>
  </head>
</template>
```

## Vue 3.5+ Suppressing Intentional Mismatches

```vue
<template>
  <!-- Suppress specific mismatch types -->
  <div data-allow-mismatch="text">
    {{ clientOnlyText }}
  </div>

  <!-- Suppress all mismatches for this element -->
  <div data-allow-mismatch>
    <ComplexClientComponent />
  </div>
</template>
```

Valid `data-allow-mismatch` values:
- `text` - Text content mismatches
- `children` - Child element mismatches
- `class` - Class attribute mismatches
- `style` - Style attribute mismatches
- `attribute` - Other attribute mismatches
- (no value) - All mismatches

## Debugging Hydration Mismatches

```javascript
// Enable detailed hydration mismatch warnings in development
// vite.config.js
export default {
  define: {
    __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: true
  }
}
```

```vue
<script setup>
import { onMounted } from 'vue'

// Debug: Compare server HTML with client expectation
onMounted(() => {
  const serverHTML = document.getElementById('app').innerHTML
  console.log('Server rendered:', serverHTML)
})
</script>
```

## Common Error Messages

| Error | Likely Cause |
|-------|--------------|
| "Hydration text content mismatch" | Different text on server/client (dates, random) |
| "Hydration children mismatch" | Invalid HTML nesting, conditional rendering |
| "Hydration attribute mismatch" | Dynamic attributes with different values |
| "Hydration node mismatch" | Completely different elements rendered |

## Reference
- [Vue.js SSR Guide - Hydration Mismatch](https://vuejs.org/guide/scaling-up/ssr.html#hydration-mismatch)
- [Nuxt Hydration Best Practices](https://nuxt.com/docs/guide/best-practices/hydration)
- [data-allow-mismatch RFC](https://github.com/vuejs/core/pull/9562)
```

## File: `skills/vue-debug-guides/reference/ssr-platform-specific-apis.md`
```markdown
---
title: Guard Platform-Specific APIs in Universal SSR Code
impact: HIGH
impactDescription: Accessing browser-only APIs on server causes crashes; Node.js APIs fail in browser
type: gotcha
tags: [vue3, ssr, browser-api, nodejs, universal, isomorphic, server-side-rendering]
---

# Guard Platform-Specific APIs in Universal SSR Code

**Impact: HIGH** - SSR applications run the same code on both server (Node.js) and client (browser). Browser APIs like `window`, `document`, and `localStorage` don't exist in Node.js and will throw `ReferenceError`. Similarly, Node.js APIs like `fs` and `process` aren't available in browsers.

Universal/isomorphic code must guard platform-specific API access or use libraries that work on both platforms.

## Task Checklist

- [ ] Never access `window`, `document`, `navigator` in `setup()` or `created()`
- [ ] Move browser API access to `onMounted()` lifecycle hook
- [ ] Use `typeof window !== 'undefined'` guard when needed outside lifecycle
- [ ] Use cross-platform libraries for common functionality (fetch, storage)
- [ ] Use Nuxt's `process.client` / `process.server` guards in Nuxt projects

## Common Browser APIs That Break SSR

| API | Node.js Behavior |
|-----|-----------------|
| `window` | `ReferenceError: window is not defined` |
| `document` | `ReferenceError: document is not defined` |
| `localStorage` / `sessionStorage` | `ReferenceError` |
| `navigator` | `ReferenceError` |
| `location` | `ReferenceError` |
| `history` | `ReferenceError` |
| `alert` / `confirm` / `prompt` | `ReferenceError` |
| `requestAnimationFrame` | `ReferenceError` |
| `IntersectionObserver` | `ReferenceError` |
| `ResizeObserver` | `ReferenceError` |

**Incorrect - Crashes on Server:**
```javascript
// WRONG: These run during setup/SSR - crashes in Node.js
const width = ref(window.innerWidth)
const theme = localStorage.getItem('theme')
const userAgent = navigator.userAgent
```

```vue
<script setup>
import { ref } from 'vue'

// WRONG: Runs on server, crashes
const scrollY = ref(window.scrollY)

// WRONG: document doesn't exist on server
document.title = 'My Page'
</script>
```

**Correct - Use onMounted:**
```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Safe defaults that work on server
const width = ref(0)
const theme = ref('light')
const scrollY = ref(0)

onMounted(() => {
  // Browser APIs only accessed after mount (client-only)
  width.value = window.innerWidth
  theme.value = localStorage.getItem('theme') || 'light'
  scrollY.value = window.scrollY

  // Event listeners safe in mounted
  window.addEventListener('resize', handleResize)
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('scroll', handleScroll)
})

function handleResize() {
  width.value = window.innerWidth
}

function handleScroll() {
  scrollY.value = window.scrollY
}
</script>
```

**Correct - Guard with typeof:**
```javascript
// When you need to check outside lifecycle hooks
function getStoredValue(key, defaultValue) {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem(key) ?? defaultValue
  }
  return defaultValue
}

// Composable with SSR awareness
export function useMediaQuery(query) {
  const matches = ref(false)

  // Only run on client
  if (typeof window !== 'undefined') {
    const mediaQuery = window.matchMedia(query)
    matches.value = mediaQuery.matches

    // Setup listener in lifecycle
    onMounted(() => {
      const handler = (e) => { matches.value = e.matches }
      mediaQuery.addEventListener('change', handler)
      onUnmounted(() => mediaQuery.removeEventListener('change', handler))
    })
  }

  return matches
}
```

## Nuxt.js Guards

```vue
<script setup>
// Nuxt provides process.client and process.server
if (process.client) {
  // Only runs in browser
  window.analytics.track('page_view')
}

if (process.server) {
  // Only runs on server
  console.log('Rendering on server')
}
</script>
```

```vue
<template>
  <!-- ClientOnly component for client-only rendering -->
  <ClientOnly>
    <BrowserOnlyChart :data="chartData" />
    <template #fallback>
      <ChartSkeleton />
    </template>
  </ClientOnly>
</template>
```

## Cross-Platform Libraries

Use libraries that abstract platform differences:

```javascript
// Fetch - works in both Node.js 18+ and browsers
const response = await fetch('/api/data')

// For older Node.js, use node-fetch or axios
import axios from 'axios'
const { data } = await axios.get('/api/data')
```

```javascript
// Universal cookie handling
import Cookies from 'js-cookie' // Client only
import { parse } from 'cookie' // Works both

// In Nuxt, use useCookie()
const token = useCookie('auth-token')
```

## Common Node.js APIs That Break in Browser

| API | Browser Behavior |
|-----|-----------------|
| `fs` | Module not found |
| `path` | Module not found |
| `process` (full) | Undefined or limited |
| `Buffer` | Undefined (unless polyfilled) |
| `__dirname` / `__filename` | Undefined |
| `require()` | Undefined in ES modules |

**Incorrect:**
```javascript
// WRONG: Node.js APIs in universal code
import fs from 'fs'
const config = JSON.parse(fs.readFileSync('./config.json'))
```

**Correct - Separate Server Code:**
```javascript
// server/utils.js - Server-only file
import fs from 'fs'
export function loadConfig() {
  return JSON.parse(fs.readFileSync('./config.json'))
}

// app.js - Universal code uses API instead
const config = await fetch('/api/config').then(r => r.json())
```

## Environment Detection Utility

```javascript
// utils/environment.js
export const isClient = typeof window !== 'undefined'
export const isServer = !isClient

export const isBrowser = isClient && typeof document !== 'undefined'
export const isNode = typeof process !== 'undefined' &&
                      process.versions?.node != null

// Usage
import { isClient, isServer } from '@/utils/environment'

if (isClient) {
  // Browser-specific code
}
```

## Third-Party Library Issues

Some libraries auto-access browser APIs on import:

```javascript
// WRONG: Library accesses window on import
import SomeChartLibrary from 'some-chart-library'
// ^ Crashes on server if library does: const x = window.something
```

**Correct - Dynamic Import:**
```vue
<script setup>
import { defineAsyncComponent } from 'vue'

// Dynamic import only loads on client
const Chart = defineAsyncComponent(() =>
  import('some-chart-library').then(m => m.ChartComponent)
)
</script>

<template>
  <ClientOnly>
    <Chart :data="data" />
  </ClientOnly>
</template>
```

## Reference
- [Vue.js SSR - Platform-Specific APIs](https://vuejs.org/guide/scaling-up/ssr.html#access-to-platform-specific-apis)
- [Nuxt ClientOnly Component](https://nuxt.com/docs/api/components/client-only)
- [MDN: Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
```

## File: `skills/vue-debug-guides/reference/state-ssr-cross-request-pollution.md`
```markdown
---
title: Prevent Cross-Request State Pollution in SSR Applications
impact: CRITICAL
impactDescription: Singleton stores in SSR share state across all server requests, potentially leaking user data between requests
type: gotcha
tags: [vue3, ssr, state-management, pinia, vuex, security, server-side-rendering, nuxt]
---

# Prevent Cross-Request State Pollution in SSR Applications

**Impact: CRITICAL** - In Server-Side Rendering (SSR) applications, a singleton store pattern creates a single instance that is shared across all server requests. This means data from one user's request could leak into another user's response, causing serious security and data integrity issues.

This is one of the most critical gotchas in Vue state management that can have severe production consequences.

## Task Checklist

- [ ] Never use a singleton store pattern in SSR applications
- [ ] Create a fresh store instance per request when using SSR
- [ ] Use Pinia which handles SSR state management correctly
- [ ] Test SSR state isolation with concurrent requests
- [ ] Review any global reactive state for SSR compatibility

## The Problem: Singleton State in SSR

```javascript
// store.js - DANGEROUS for SSR
import { reactive } from 'vue'

// This is a singleton - same instance for ALL requests
export const store = reactive({
  user: null,
  cart: [],
  preferences: {}
})
```

**What happens in SSR:**

1. Request A comes in for User A
2. Server sets `store.user = userA`
3. Before response completes, Request B arrives for User B
4. Request B sees `store.user = userA` (User A's data leaked!)
5. Server sets `store.user = userB`
6. Request A's response might now contain User B's data

This creates unpredictable behavior and potential security vulnerabilities.

## Solution 1: Use Pinia (Recommended)

Pinia handles SSR correctly by creating fresh store instances per request:

```javascript
// stores/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    preferences: {}
  }),
  actions: {
    setUser(user) {
      this.user = user
    }
  }
})
```

```javascript
// main.js (or entry-server.js)
import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'

// For SSR: Create fresh instances per request
export function createAppInstance() {
  const app = createApp(App)
  const pinia = createPinia()

  app.use(pinia)

  return { app, pinia }
}
```

```javascript
// entry-server.js
import { createAppInstance } from './main'
import { renderToString } from 'vue/server-renderer'

export async function render(url, context) {
  // Fresh app and store instance per request
  const { app, pinia } = createAppInstance()

  // ... setup router, fetch data, etc.

  const html = await renderToString(app)

  // Serialize state for client hydration
  const state = pinia.state.value

  return { html, state }
}
```

```javascript
// entry-client.js - Hydrate from serialized state
import { createAppInstance } from './main'

const { app, pinia } = createAppInstance()

// Restore server state before mounting
if (window.__PINIA_STATE__) {
  pinia.state.value = window.__PINIA_STATE__
}

app.mount('#app')
```

## Solution 2: Factory Pattern for Hand-Rolled State

If not using Pinia, create a factory function:

```javascript
// store.js - SSR-safe with factory
import { reactive, readonly } from 'vue'

// Factory function creates fresh state per call
export function createStore() {
  const state = reactive({
    user: null,
    cart: [],
    preferences: {}
  })

  return {
    state: readonly(state),
    setUser(user) {
      state.user = user
    },
    addToCart(item) {
      state.cart.push(item)
    }
  }
}
```

```javascript
// entry-server.js
import { createStore } from './store'
import { provide } from 'vue'

export async function render(url) {
  const app = createApp(App)

  // Fresh store instance for this request only
  const store = createStore()
  app.provide('store', store)

  // ... render
}
```

## Solution 3: Context-Based State (Advanced)

For frameworks like Nuxt, use request context:

```javascript
// composables/useRequestState.js
import { useSSRContext } from 'vue'

export function useRequestState(key, initialValue) {
  if (import.meta.env.SSR) {
    const ctx = useSSRContext()
    ctx.state = ctx.state || {}

    if (!(key in ctx.state)) {
      ctx.state[key] = initialValue()
    }

    return ctx.state[key]
  }

  // Client-side: use regular reactive state
  return reactive(initialValue())
}
```

## Nuxt.js Handles This Automatically

In Nuxt 3, state isolation is handled automatically:

```javascript
// Nuxt automatically creates fresh Pinia instance per request
// You can use stores normally

export default defineNuxtPlugin(async (nuxtApp) => {
  const userStore = useUserStore()
  await userStore.fetchUser()
})
```

## Testing for State Pollution

```javascript
// test/ssr-state-isolation.test.js
import { describe, it, expect } from 'vitest'
import { render } from './entry-server'

describe('SSR State Isolation', () => {
  it('should not leak state between concurrent requests', async () => {
    // Simulate concurrent requests
    const [result1, result2] = await Promise.all([
      render('/user/1', { userId: '1' }),
      render('/user/2', { userId: '2' })
    ])

    // Each should have their own user data
    expect(result1.html).toContain('User 1')
    expect(result2.html).toContain('User 2')

    // State should not be mixed
    expect(result1.html).not.toContain('User 2')
    expect(result2.html).not.toContain('User 1')
  })
})
```

```javascript
// Alternative: Test store isolation directly
import { createApp } from './app.js'

test('requests do not share state', async () => {
  // Simulate two concurrent requests
  const { app: app1, store: store1 } = createApp()
  const { app: app2, store: store2 } = createApp()

  store1.user = { id: 1, name: 'Alice' }
  store2.user = { id: 2, name: 'Bob' }

  // Each should have its own state
  expect(store1.user.name).toBe('Alice')
  expect(store2.user.name).toBe('Bob')
})
```

## Red Flags to Watch For

```javascript
// ANY module-level reactive state is dangerous in SSR

// BAD: Module-level reactive
export const globalUser = ref(null)

// BAD: Module-level reactive object
export const appState = reactive({})

// BAD: Shared Map/Set
export const cache = new Map()

// BAD: Even plain objects can be problematic
let requestCount = 0  // Shared across requests
```

## Why Pinia is Recommended for SSR

1. **Automatic request isolation** - Fresh store instances per request
2. **Built-in state serialization** - Easy hydration on client
3. **DevTools support** - Debug state on both server and client
4. **TypeScript support** - Type-safe state management
5. **Tested patterns** - Battle-tested SSR handling

## Reference
- [Vue.js State Management - SSR Considerations](https://vuejs.org/guide/scaling-up/state-management.html#ssr-considerations)
- [Pinia SSR Guide](https://pinia.vuejs.org/ssr/)
- [Vue SSR Guide](https://vuejs.org/guide/scaling-up/ssr.html)
```

## File: `skills/vue-debug-guides/reference/suspense-no-builtin-error-handling.md`
```markdown
# Suspense Has No Built-in Error Handling

## Rule

`<Suspense>` does not provide error handling via the component itself. You must implement error handling using `errorCaptured` option or `onErrorCaptured()` hook in a parent component to catch async errors.

## Why This Matters

Without explicit error handling, async errors in suspended components will propagate uncaught, potentially crashing the application or leaving users stuck on loading states. Unlike React's Error Boundaries, Vue's Suspense requires manual error boundary implementation.

## Bad Code

```vue
<script setup>
// No error handling - async errors will propagate uncaught
</script>

<template>
  <Suspense>
    <AsyncComponent />
    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

## Good Code

```vue
<script setup>
import { ref, onErrorCaptured } from 'vue'
import AsyncComponent from './AsyncComponent.vue'

const error = ref(null)

onErrorCaptured((err) => {
  error.value = err
  return false // Prevent error from propagating further
})
</script>

<template>
  <div v-if="error" class="error-state">
    <p>Something went wrong: {{ error.message }}</p>
    <button @click="error = null">Retry</button>
  </div>

  <Suspense v-else>
    <AsyncComponent />
    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>
```

## Reusable Error Boundary Pattern

```vue
<!-- ErrorBoundary.vue -->
<script setup>
import { ref, onErrorCaptured } from 'vue'

const props = defineProps({
  fallback: {
    type: String,
    default: 'Something went wrong'
  }
})

const emit = defineEmits(['error'])

const error = ref(null)

onErrorCaptured((err, instance, info) => {
  error.value = { err, instance, info }
  emit('error', { err, instance, info })
  return false
})

const reset = () => {
  error.value = null
}

defineExpose({ reset })
</script>

<template>
  <slot v-if="!error" />
  <slot v-else name="error" :error="error" :reset="reset">
    <div class="error-boundary">
      {{ fallback }}
      <button @click="reset">Retry</button>
    </div>
  </slot>
</template>
```

```vue
<!-- Usage -->
<template>
  <ErrorBoundary @error="logError">
    <Suspense>
      <AsyncDashboard />
      <template #fallback>Loading dashboard...</template>
    </Suspense>

    <template #error="{ error, reset }">
      <DashboardError :error="error" @retry="reset" />
    </template>
  </ErrorBoundary>
</template>
```

## Key Points

1. Always wrap `<Suspense>` with error handling logic in production
2. Use `onErrorCaptured` for Composition API or `errorCaptured` option for Options API
3. Return `false` from the error handler to stop propagation
4. Consider creating a reusable `ErrorBoundary` component to reduce boilerplate
5. Provide a way for users to retry failed operations

## References

- [Vue.js Suspense Documentation](https://vuejs.org/guide/built-ins/suspense#error-handling)
- [Vue.js onErrorCaptured](https://vuejs.org/api/composition-api-lifecycle#onerrorcaptured)
```

## File: `skills/vue-debug-guides/reference/suspense-ssr-hydration-issues.md`
```markdown
# Suspense SSR Hydration Issues and Workarounds

## Rule

`<Suspense>` has known issues with SSR hydration, particularly with async components. During initial hydration, Suspense may not properly include child components within its "cloak of suspense," leading to hydration mismatches, flickering, or runtime crashes.

## Why This Matters

In SSR applications, hydration mismatches cause:
- Visual flickering as the client re-renders
- Loss of state in affected components
- Console warnings in development (silent failures in production)
- Potential runtime crashes in edge cases
- Poor user experience, especially on slower networks

## Bad Code

```vue
<template>
  <!-- Async component directly in Suspense can fail hydration -->
  <Suspense>
    <AsyncDashboard />
    <template #fallback>
      Loading...
    </template>
  </Suspense>
</template>

<script setup>
import { defineAsyncComponent } from 'vue'

const AsyncDashboard = defineAsyncComponent(
  () => import('./Dashboard.vue')
)
</script>
```

## Good Code

### Solution 1: Wrap Async Components with Suspense

```vue
<template>
  <!-- Each async component wrapped in its own Suspense -->
  <div class="dashboard">
    <Suspense>
      <AsyncHeader />
      <template #fallback><HeaderSkeleton /></template>
    </Suspense>

    <Suspense>
      <AsyncContent />
      <template #fallback><ContentSkeleton /></template>
    </Suspense>
  </div>
</template>
```

### Solution 2: Use ClientOnly Wrapper (Nuxt/SSR Frameworks)

```vue
<template>
  <!-- Prevent SSR for problematic async components -->
  <ClientOnly>
    <Suspense>
      <AsyncDashboard />
      <template #fallback>
        Loading dashboard...
      </template>
    </Suspense>

    <template #fallback>
      <DashboardSkeleton />
    </template>
  </ClientOnly>
</template>
```

### Solution 3: Prefetch with Proper Stale Time (with TanStack Query)

```vue
<script setup>
import { useQuery, useQueryClient } from '@tanstack/vue-query'

// IMPORTANT: All useQuery calls must be BEFORE any await
const { data, suspense } = useQuery({
  queryKey: ['dashboard'],
  queryFn: fetchDashboardData,
  staleTime: 1000 * 60 * 5, // 5 minutes - prevents refetch after hydration
})

// Wait for suspense AFTER all useQuery calls
await suspense()

// Now safe to use data
</script>
```

### Solution 4: Handle Hydration Errors Gracefully

```vue
<script setup>
import { ref, onErrorCaptured, onMounted } from 'vue'

const hydrationError = ref(false)
const isClient = ref(false)

onMounted(() => {
  isClient.value = true
})

onErrorCaptured((err) => {
  if (err.message?.includes('hydration')) {
    hydrationError.value = true
    return false
  }
})
</script>

<template>
  <div v-if="hydrationError" class="hydration-recovery">
    <!-- Force client-only re-render -->
    <Suspense v-if="isClient">
      <AsyncContent />
      <template #fallback>Recovering...</template>
    </Suspense>
  </div>

  <Suspense v-else>
    <AsyncContent />
    <template #fallback>Loading...</template>
  </Suspense>
</template>
```

## Common SSR + Suspense Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Hydration mismatch | Async chunk not loaded in time | Wrap with Suspense or use ClientOnly |
| Empty flash on Safari | Slow chunk loading | Preload critical chunks, use skeleton |
| useQuery after await error | Vue context lost after await | Put all useQuery calls before any await |
| Immediate refetch after hydration | staleTime too low | Set appropriate staleTime value |

## Key Points

1. Suspense + SSR has known edge cases - test thoroughly
2. Safari has slower chunk loading that triggers more hydration issues
3. With data-fetching libraries, ensure queries are set up before awaiting suspense
4. Consider ClientOnly wrappers for non-critical async content
5. Set appropriate staleTime to prevent unnecessary refetches after hydration
6. Use skeleton screens that match server-rendered content structure

## References

- [Vue.js Suspense Documentation](https://vuejs.org/guide/built-ins/suspense)
- [Vue Issue #6638 - Suspense hydration](https://github.com/vuejs/core/issues/6638)
- [Vue Issue #7672 - defineAsyncComponent SSR](https://github.com/vuejs/core/issues/7672)
- [TanStack Query SSR Discussion](https://github.com/TanStack/query/discussions/4870)
```

## File: `skills/vue-debug-guides/reference/tailwind-dynamic-class-generation.md`
```markdown
# Tailwind CSS Dynamic Class Generation

## Rule

Never construct Tailwind CSS class names dynamically using string concatenation or template literals. Tailwind's build process cannot detect dynamically generated class names, causing styles to be missing in production.

## Why This Matters

- Tailwind uses static analysis at build time to determine which CSS classes to include
- Dynamically constructed class names (e.g., `bg-${color}-500`) are invisible to Tailwind's scanner
- Classes work in development with JIT but fail silently in production builds
- This is a common source of "it works locally but not in production" bugs

## Bad Code

```vue
<script setup>
const props = defineProps({
  color: String, // 'red', 'blue', 'green'
  size: String   // 'sm', 'md', 'lg'
})
</script>

<template>
  <!-- WRONG: Tailwind cannot detect these classes -->
  <div :class="`bg-${color}-500 text-${size}`">
    Content
  </div>

  <!-- WRONG: String concatenation -->
  <div :class="'p-' + padding">
    Content
  </div>

  <!-- WRONG: Template literal in array -->
  <div :class="[`gap-x-${spacing}`]">
    Content
  </div>
</template>
```

## Good Code

```vue
<script setup>
const props = defineProps({
  color: String,
  size: String
})

// Use a mapping object with complete class names
const colorClasses = {
  red: 'bg-red-500',
  blue: 'bg-blue-500',
  green: 'bg-green-500'
}

const sizeClasses = {
  sm: 'text-sm p-2',
  md: 'text-base p-4',
  lg: 'text-lg p-6'
}
</script>

<template>
  <!-- CORRECT: Full class names that Tailwind can detect -->
  <div :class="[colorClasses[color], sizeClasses[size]]">
    Content
  </div>
</template>
```

## Using Conditional Objects

```vue
<script setup>
const props = defineProps({
  variant: String // 'primary', 'secondary', 'danger'
})
</script>

<template>
  <!-- CORRECT: All class names are complete strings -->
  <button :class="{
    'bg-blue-500 hover:bg-blue-600': variant === 'primary',
    'bg-gray-500 hover:bg-gray-600': variant === 'secondary',
    'bg-red-500 hover:bg-red-600': variant === 'danger'
  }">
    Click me
  </button>
</template>
```

## Safelist for Truly Dynamic Classes

If you must use dynamic classes, add them to Tailwind's safelist:

```javascript
// tailwind.config.js
module.exports = {
  safelist: [
    'bg-red-500',
    'bg-blue-500',
    'bg-green-500',
    // Or use patterns (use sparingly - increases bundle size)
    {
      pattern: /bg-(red|blue|green)-(100|500|900)/
    }
  ]
}
```

## Alternative: CSS Custom Properties

For truly dynamic values, use CSS custom properties:

```vue
<script setup>
const props = defineProps({
  customColor: String // Any hex color
})
</script>

<template>
  <!-- Use CSS variable for truly dynamic values -->
  <div
    class="dynamic-bg"
    :style="{ '--dynamic-color': customColor }"
  >
    Content
  </div>
</template>

<style>
.dynamic-bg {
  background-color: var(--dynamic-color);
}
</style>
```

## References

- [Tailwind CSS Dynamic Class Names](https://tailwindcss.com/docs/content-configuration#dynamic-class-names)
- [Tailwind Safelist](https://tailwindcss.com/docs/content-configuration#safelisting-classes)
```

## File: `skills/vue-debug-guides/reference/teleport-scoped-styles-limitation.md`
```markdown
---
title: Scoped Styles May Not Apply to Teleported Content
impact: MEDIUM
impactDescription: Scoped styles can fail to apply to teleported elements due to data attribute limitations
type: gotcha
tags: [vue3, teleport, scoped-styles, css]
---

# Scoped Styles May Not Apply to Teleported Content

**Impact: MEDIUM** - When using scoped styles with Teleport, the styles may not apply correctly to teleported elements. This is a known limitation related to how Vue's scoped style attributes work with elements rendered outside the component's DOM tree.

## Task Checklist

- [ ] Test scoped styles on teleported content
- [ ] Use `:deep()` selector or non-scoped styles for teleported content
- [ ] Consider CSS modules as an alternative
- [ ] Keep teleported content styles in a separate non-scoped style block

**Problem - Scoped Styles Not Applied:**
```vue
<template>
  <Teleport to="body">
    <div class="modal">
      <p class="modal-text">This text may not be styled!</p>
    </div>
  </Teleport>
</template>

<style scoped>
/* These styles may NOT apply to teleported content */
.modal {
  background: white;
  padding: 20px;
}

.modal-text {
  color: blue;  /* May not work */
}
</style>
```

**Solution 1 - Use Non-Scoped Styles for Teleported Content:**
```vue
<template>
  <Teleport to="body">
    <div class="my-modal">
      <p class="my-modal-text">This text will be styled</p>
    </div>
  </Teleport>
</template>

<style scoped>
/* Component-specific styles */
.button { color: blue; }
</style>

<style>
/* Non-scoped styles for teleported content */
/* Use specific class names to avoid conflicts */
.my-modal {
  background: white;
  padding: 20px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.my-modal-text {
  color: blue;
}
</style>
```

**Solution 2 - Use :deep() Selector:**
```vue
<template>
  <Teleport to="body">
    <div class="modal">
      <p class="modal-text">Styled with :deep()</p>
    </div>
  </Teleport>
</template>

<style scoped>
:deep(.modal) {
  background: white;
  padding: 20px;
}

:deep(.modal-text) {
  color: blue;
}
</style>
```

**Solution 3 - CSS Modules:**
```vue
<template>
  <Teleport to="body">
    <div :class="$style.modal">
      <p :class="$style.modalText">Styled with CSS modules</p>
    </div>
  </Teleport>
</template>

<style module>
.modal {
  background: white;
  padding: 20px;
}

.modalText {
  color: blue;
}
</style>
```

## Multi-Root Components with Teleport

Using Teleport as one of multiple root nodes causes additional issues:

```vue
<template>
  <!-- Multi-root component -->
  <button @click="open = true">Open</button>
  <Teleport to="body">
    <div class="modal">Content</div>
  </Teleport>
</template>

<!-- Warning: class/style attributes may not be inherited -->
```

Pass classes explicitly to avoid inheritance issues:

```vue
<template>
  <button @click="open = true">Open</button>
  <Teleport to="body">
    <div :class="['modal', $attrs.class]" :style="$attrs.style">
      Content
    </div>
  </Teleport>
</template>
```

## Best Practice: Dedicated Modal Styles

Create a dedicated stylesheet for modal/overlay components:

```css
/* modal-styles.css */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  border-radius: 8px;
  padding: 24px;
  max-width: 500px;
  width: 90%;
}
```

```vue
<script setup>
import './modal-styles.css'
</script>

<template>
  <Teleport to="body">
    <div v-if="open" class="modal-overlay">
      <div class="modal-content">
        <slot />
      </div>
    </div>
  </Teleport>
</template>
```

## Reference
- [Vue.js SFC CSS Features - Scoped CSS](https://vuejs.org/api/sfc-css-features.html#scoped-css)
- [GitHub Issue #2047 - Scoped styles and teleport](https://github.com/vuejs/core/issues/2047)
```

## File: `skills/vue-debug-guides/reference/teleport-ssr-hydration.md`
```markdown
---
title: Handle Teleport SSR Hydration Carefully
impact: HIGH
impactDescription: Teleported content causes hydration mismatches in SSR/SSG applications
type: gotcha
tags: [vue3, teleport, ssr, nuxt, hydration]
---

# Handle Teleport SSR Hydration Carefully

**Impact: HIGH** - Teleports require special handling during SSR. The teleported content is not part of the server-rendered HTML string, causing hydration mismatches that can break the application or cause content to disappear.

This is a critical issue for Nuxt, Quasar SSR, and custom Vue SSR setups.

## Task Checklist

- [ ] Wrap Teleport in `<ClientOnly>` component (Nuxt) for client-only rendering
- [ ] Use conditional rendering based on mount state for non-Nuxt SSR
- [ ] Use `data-allow-mismatch` attribute in Vue 3.5+ when intentional
- [ ] Test SSR applications thoroughly for hydration issues

**Problem - SSR Hydration Mismatch:**
```vue
<template>
  <!-- Server renders nothing for teleported content -->
  <!-- Client expects teleported content at #modals -->
  <!-- = Hydration mismatch -->
  <Teleport to="#modals">
    <div v-if="showModal" class="modal">
      Modal content
    </div>
  </Teleport>
</template>
```

Common error messages:
```
[Vue warn]: Hydration children mismatch in <div>:
server rendered element contains fewer child nodes than client vdom.
```

**Solution 1 - Nuxt ClientOnly:**
```vue
<template>
  <button @click="showModal = true">Open Modal</button>

  <!-- Only render on client, avoiding SSR -->
  <ClientOnly>
    <Teleport to="body">
      <div v-if="showModal" class="modal">
        Modal content
      </div>
    </Teleport>
  </ClientOnly>
</template>
```

**Solution 2 - Manual Client Detection:**
```vue
<template>
  <button @click="showModal = true">Open Modal</button>

  <!-- Only render after component mounts on client -->
  <Teleport v-if="isMounted" to="body">
    <div v-if="showModal" class="modal">
      Modal content
    </div>
  </Teleport>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const showModal = ref(false)
const isMounted = ref(false)

onMounted(() => {
  isMounted.value = true
})
</script>
```

**Solution 3 - Vue 3.5+ data-allow-mismatch:**
```vue
<template>
  <!-- Suppress hydration warnings for intentional mismatches -->
  <div data-allow-mismatch>
    <Teleport to="body">
      <div v-if="showModal" class="modal">
        Modal content
      </div>
    </Teleport>
  </div>
</template>
```

## SSR with Multiple Teleports

Multiple teleports to the same target can cause additional hydration issues:

```vue
<!-- Parent.vue -->
<template>
  <!-- First teleport -->
  <Teleport to="#modals">
    <NotificationBanner />
  </Teleport>

  <ChildComponent />
</template>

<!-- ChildComponent.vue -->
<template>
  <!-- Second teleport to same target - order matters! -->
  <Teleport to="#modals">
    <Modal />
  </Teleport>
</template>
```

For SSR, ensure consistent ordering or wrap each in `ClientOnly`.

## Element Plus and UI Library SSR

Many UI libraries use Teleport internally. Element Plus components that use Teleport include:
- ElDialog
- ElDrawer
- ElTooltip
- ElDropdown
- ElSelect
- ElDatePicker

```vue
<template>
  <!-- These need special SSR handling -->
  <ClientOnly>
    <ElDialog v-model="visible">
      Dialog content
    </ElDialog>
  </ClientOnly>
</template>
```

## Known Vue Issues

- Disabled teleports in fragments can cause hydration mismatches (Vue issue #6152)
- Nested teleports may cause app to break on hydration (Vue issue #5242)

## Reference
- [Vue.js SSR - Teleports](https://vuejs.org/guide/scaling-up/ssr.html#teleports)
- [Element Plus SSR Guide](https://element-plus.org/en-US/guide/ssr.html)
- [Nuxt ClientOnly Component](https://nuxt.com/docs/api/components/client-only)
```

## File: `skills/vue-debug-guides/reference/teleport-target-must-exist.md`
```markdown
---
title: Teleport Target Must Exist Before Mount
impact: HIGH
impactDescription: Teleport will fail silently or throw errors if target element doesn't exist when component mounts
type: gotcha
tags: [vue3, teleport, modal, dom, lifecycle]
---

# Teleport Target Must Exist Before Mount

**Impact: HIGH** - The teleport `to` target must already exist in the DOM when the `<Teleport>` component is mounted. If the target doesn't exist, Vue will throw an error and the teleported content won't render.

This is a common source of bugs when using modals, tooltips, or other teleported UI elements, especially when targeting Vue-rendered elements.

## Task Checklist

- [ ] Ensure teleport target exists in the DOM before `<Teleport>` mounts
- [ ] Place teleport containers (e.g., `#modals`, `#tooltips`) in `index.html` outside the Vue app
- [ ] If targeting Vue-rendered elements, ensure they mount before the Teleport
- [ ] Use Vue 3.5+ `defer` prop when target is rendered later in the same component tree

**Incorrect:**
```vue
<template>
  <!-- ERROR: Target doesn't exist yet when Teleport mounts -->
  <Teleport to="#modal-container">
    <div class="modal">Modal content</div>
  </Teleport>

  <!-- Target is defined after the Teleport -->
  <div id="modal-container"></div>
</template>
```

**Correct - Option 1: External container in index.html:**
```html
<!-- index.html -->
<body>
  <div id="app"></div>
  <!-- Container exists before Vue app mounts -->
  <div id="modals"></div>
  <div id="tooltips"></div>
</body>
```

```vue
<template>
  <!-- Safe: #modals exists before any Vue component mounts -->
  <Teleport to="#modals">
    <div v-if="showModal" class="modal">Modal content</div>
  </Teleport>
</template>
```

**Correct - Option 2: Teleport to body:**
```vue
<template>
  <!-- Safe: body always exists -->
  <Teleport to="body">
    <div v-if="showModal" class="modal">Modal content</div>
  </Teleport>
</template>
```

**Correct - Option 3: Vue 3.5+ defer prop:**
```vue
<template>
  <!-- Works in Vue 3.5+: defer resolves target after other parts mount -->
  <Teleport defer to="#late-container">
    <div class="modal">Modal content</div>
  </Teleport>

  <!-- Target rendered later in template -->
  <div id="late-container"></div>
</template>
```

## Defer Prop Limitations (Vue 3.5+)

The `defer` prop only waits for elements rendered in the **same mount/update tick**:

```vue
<template>
  <!-- ERROR: defer won't help if target mounts asynchronously -->
  <Teleport defer to="#async-container">
    <div>Content</div>
  </Teleport>

  <!-- If this component loads asynchronously, defer won't work -->
  <Suspense>
    <AsyncComponent />  <!-- Contains #async-container -->
  </Suspense>
</template>
```

## Common Patterns

### Recommended: Centralized Teleport Containers
```html
<!-- index.html -->
<body>
  <div id="app"></div>

  <!-- Teleport destinations outside Vue app -->
  <div id="modals" aria-live="polite"></div>
  <div id="notifications" aria-live="assertive"></div>
  <div id="tooltips"></div>
</body>
```

## Reference
- [Vue.js Teleport - Using with Vue-rendered Targets](https://vuejs.org/guide/built-ins/teleport.html#using-with-vue-rendered-targets)
- [Vue.js Teleport - Deferred Teleport](https://vuejs.org/guide/built-ins/teleport.html#deferred-teleport)
```

## File: `skills/vue-debug-guides/reference/template-expressions-restrictions.md`
```markdown
---
title: Template Expressions Must Be Single Expressions
impact: MEDIUM
impactDescription: Using statements instead of expressions in templates causes compilation errors
type: capability
tags: [vue3, template, expressions, interpolation, syntax]
---

# Template Expressions Must Be Single Expressions

**Impact: MEDIUM** - Vue templates only support single JavaScript expressions, not statements. Using variable declarations, if statements, or multiple statements will cause template compilation errors.

Template interpolation `{{ }}` and directive bindings evaluate JavaScript expressions that produce a value. Statements like `if`, `for`, variable declarations, or multi-line code blocks are not allowed.

## Task Checklist

- [ ] Use only single expressions in `{{ }}` interpolation
- [ ] Use ternary operators instead of if/else statements
- [ ] Move complex logic to computed properties or methods
- [ ] Avoid variable declarations in templates
- [ ] Use `v-if`/`v-else` directives for conditional rendering

**Incorrect:**
```vue
<template>
  <!-- ERROR: Variable declaration is a statement, not expression -->
  <p>{{ var greeting = 'Hello' }}</p>
  <p>{{ let x = 1 }}</p>
  <p>{{ const name = 'Vue' }}</p>

  <!-- ERROR: if statement not allowed -->
  <p>{{ if (ok) { return message } }}</p>
  <p>{{ if (user) return user.name }}</p>

  <!-- ERROR: Multiple statements not allowed -->
  <p>{{ count++; return count }}</p>
  <p>{{ items.push(newItem); items.length }}</p>

  <!-- ERROR: for/while loops not allowed -->
  <p>{{ for (let i = 0; i < 5; i++) { } }}</p>
</template>
```

**Correct:**
```vue
<template>
  <!-- OK: Simple expressions -->
  <p>{{ message }}</p>
  <p>{{ count + 1 }}</p>
  <p>{{ items.length }}</p>

  <!-- OK: Ternary operators for conditionals -->
  <p>{{ ok ? 'YES' : 'NO' }}</p>
  <p>{{ user ? user.name : 'Guest' }}</p>
  <p>{{ score >= 60 ? 'Pass' : 'Fail' }}</p>

  <!-- OK: Method/function calls -->
  <p>{{ formatDate(date) }}</p>
  <p>{{ items.filter(i => i.active).length }}</p>

  <!-- OK: Chained expressions -->
  <p>{{ message.split('').reverse().join('') }}</p>

  <!-- OK: Template literals -->
  <p>{{ `Hello, ${name}!` }}</p>

  <!-- OK: Object/array expressions -->
  <p>{{ { name: 'Vue', version: 3 } }}</p>
</template>

<script setup>
import { ref, computed } from 'vue'

const ok = ref(true)
const message = ref('Hello')
const user = ref({ name: 'Alice' })
const score = ref(85)

// Move complex logic to computed properties
const greeting = computed(() => {
  if (user.value) {
    return `Welcome back, ${user.value.name}!`
  }
  return 'Hello, Guest!'
})

// Or use methods for reusable logic
function formatDate(date) {
  return new Date(date).toLocaleDateString()
}
</script>
```

## Use Directives for Control Flow

```vue
<template>
  <!-- Instead of if/else in expressions, use v-if/v-else -->
  <p v-if="user">Welcome, {{ user.name }}!</p>
  <p v-else>Please log in</p>

  <!-- Instead of loops in expressions, use v-for -->
  <ul>
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </ul>

  <!-- Conditional display without removing from DOM -->
  <p v-show="isVisible">This toggles visibility</p>
</template>
```

## Reference
- [Vue.js Template Syntax - Using JavaScript Expressions](https://vuejs.org/guide/essentials/template-syntax.html#using-javascript-expressions)
- [Vue.js Conditional Rendering](https://vuejs.org/guide/essentials/conditional.html)
```

## File: `skills/vue-debug-guides/reference/template-functions-no-side-effects.md`
```markdown
---
title: Template Functions Must Be Pure Without Side Effects
impact: MEDIUM
impactDescription: Functions with side effects in templates cause unpredictable behavior on every re-render
type: efficiency
tags: [vue3, template, functions, performance, side-effects]
---

# Template Functions Must Be Pure Without Side Effects

**Impact: MEDIUM** - Functions called in templates execute on every component re-render. Functions with side effects (modifying data, API calls, logging) will cause unpredictable behavior, performance issues, and difficult-to-debug bugs.

Template expressions including function calls are evaluated whenever the component updates. This makes them unsuitable for operations that should only happen once or that modify state.

## Task Checklist

- [ ] Keep template functions pure (same input = same output)
- [ ] Never modify reactive state inside template functions
- [ ] Never make API calls or async operations in template functions
- [ ] Move side effects to event handlers, watchers, or lifecycle hooks
- [ ] Use computed properties for derived values instead of functions when possible
- [ ] Avoid expensive computations; use computed properties for caching

**Incorrect:**
```vue
<template>
  <!-- BAD: Modifies state on every render -->
  <p>{{ incrementAndGet() }}</p>

  <!-- BAD: API call on every render -->
  <div>{{ fetchUserName() }}</div>

  <!-- BAD: Logging side effect -->
  <span>{{ logAndFormat(date) }}</span>

  <!-- BAD: Expensive computation without caching -->
  <ul>
    <li v-for="item in filterAndSort(items)" :key="item.id">
      {{ item.name }}
    </li>
  </ul>

  <!-- BAD: Random values change on every render -->
  <p>{{ getRandomGreeting() }}</p>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)
const items = ref([/* large array */])

// BAD: Has side effect - modifies state
function incrementAndGet() {
  count.value++  // Side effect!
  return count.value
}

// BAD: Async operation in template
async function fetchUserName() {
  const res = await fetch('/api/user')  // Side effect!
  return (await res.json()).name
}

// BAD: Logging is a side effect
function logAndFormat(date) {
  console.log('Formatting date:', date)  // Side effect!
  return new Date(date).toLocaleDateString()
}

// BAD: Expensive, runs every render without caching
function filterAndSort(items) {
  return items
    .filter(i => i.active)
    .sort((a, b) => a.name.localeCompare(b.name))
}

// BAD: Non-deterministic
function getRandomGreeting() {
  const greetings = ['Hello', 'Hi', 'Hey']
  return greetings[Math.floor(Math.random() * greetings.length)]
}
</script>
```

**Correct:**
```vue
<template>
  <!-- OK: Pure formatting function -->
  <p>Count: {{ count }}</p>
  <button @click="increment">Increment</button>

  <!-- OK: Data fetched via lifecycle/watcher -->
  <div>{{ userName }}</div>

  <!-- OK: Pure function, no side effects -->
  <span>{{ formatDate(date) }}</span>

  <!-- OK: Computed property caches result -->
  <ul>
    <li v-for="item in filteredAndSortedItems" :key="item.id">
      {{ item.name }}
    </li>
  </ul>

  <!-- OK: Random value set once -->
  <p>{{ greeting }}</p>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const count = ref(0)
const userName = ref('')
const date = ref(new Date())
const items = ref([/* large array */])

// Side effects in event handlers
function increment() {
  count.value++
}

// Fetch data in lifecycle hook
onMounted(async () => {
  const res = await fetch('/api/user')
  userName.value = (await res.json()).name
})

// Pure function - same input, same output
function formatDate(date) {
  return new Date(date).toLocaleDateString()
}

// Computed property - cached, only recalculates when dependencies change
const filteredAndSortedItems = computed(() => {
  return items.value
    .filter(i => i.active)
    .sort((a, b) => a.name.localeCompare(b.name))
})

// Set random value once, not on every render
const greetings = ['Hello', 'Hi', 'Hey']
const greeting = ref(greetings[Math.floor(Math.random() * greetings.length)])
</script>
```

## Pure Function Guidelines

A pure function:
1. Given the same inputs, always returns the same output
2. Does not modify any external state
3. Does not perform I/O operations (network, console, file system)
4. Does not depend on mutable external state

```javascript
// PURE - safe for templates
function formatCurrency(amount, currency = 'USD') {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(amount)
}

function fullName(first, last) {
  return `${first} ${last}`
}

function isExpired(date) {
  return new Date(date) < new Date()
}

// IMPURE - unsafe for templates
function logAndReturn(value) {
  console.log(value)  // I/O
  return value
}

function getFromLocalStorage(key) {
  return localStorage.getItem(key)  // External state
}

function updateAndReturn(obj, key, value) {
  obj[key] = value  // Mutation
  return obj
}
```

## Reference
- [Vue.js Template Syntax - Calling Functions](https://vuejs.org/guide/essentials/template-syntax.html#calling-functions)
- [Vue.js Computed Properties](https://vuejs.org/guide/essentials/computed.html)
```

## File: `skills/vue-debug-guides/reference/template-ref-null-with-v-if.md`
```markdown
---
title: Template Refs Become Null When Elements Are Unmounted
impact: MEDIUM
impactDescription: Refs become null when conditionally rendered elements are removed, causing errors if not handled
type: gotcha
tags: [vue3, template-refs, v-if, watchers, conditional-rendering]
---

# Template Refs Become Null When Elements Are Unmounted

**Impact: MEDIUM** - When using template refs with `v-if`, the ref becomes `null` when the element is unmounted. Watchers and effects that access these refs must handle the null case to avoid runtime errors.

This is especially tricky with `watchEffect` since it runs automatically and may execute when the ref is null.

## Task Checklist

- [ ] Always check for null before accessing ref properties when using v-if
- [ ] In watchers, explicitly handle the null case (element unmounted or not yet mounted)
- [ ] Consider whether v-show is more appropriate if you need persistent ref access
- [ ] Use optional chaining (?.) when accessing ref properties in uncertain contexts

**Incorrect:**
```vue
<script setup>
import { ref, watchEffect } from 'vue'

const inputEl = ref(null)
const showInput = ref(true)

// WRONG: No null check - will error when v-if is false
watchEffect(() => {
  inputEl.value.focus() // TypeError when showInput is false
})
</script>

<template>
  <input v-if="showInput" ref="inputEl" />
  <button @click="showInput = !showInput">Toggle</button>
</template>
```

**Correct:**
```vue
<script setup>
import { ref, watchEffect } from 'vue'

const inputEl = ref(null)
const showInput = ref(true)

// CORRECT: Handle both mounted and unmounted states
watchEffect(() => {
  if (inputEl.value) {
    inputEl.value.focus()
  } else {
    // Element not mounted yet, or unmounted by v-if
    console.log('Input element not available')
  }
})
</script>

<template>
  <input v-if="showInput" ref="inputEl" />
  <button @click="showInput = !showInput">Toggle</button>
</template>
```

```vue
<script setup>
import { ref, watch } from 'vue'

const inputEl = ref(null)
const showInput = ref(true)

// CORRECT: Watch the ref and handle null explicitly
watch(inputEl, (el) => {
  if (el) {
    el.focus()
  }
})
</script>

<template>
  <input v-if="showInput" ref="inputEl" />
</template>
```

```vue
<script setup>
import { useTemplateRef, watchEffect } from 'vue'

// Vue 3.5+ approach
const input = useTemplateRef('my-input')

// CORRECT: Use optional chaining for safe access
watchEffect(() => {
  input.value?.focus()
})
</script>

<template>
  <input v-if="showInput" ref="my-input" />
</template>
```

```vue
<script setup>
import { ref, onMounted } from 'vue'

const inputEl = ref(null)
const showInput = ref(true)

// ALTERNATIVE: Use v-show if you need consistent ref access
// v-show keeps element in DOM, just hides it with CSS
</script>

<template>
  <!-- Element always exists in DOM, ref is never null -->
  <input v-show="showInput" ref="inputEl" />
</template>
```

## Reference
- [Vue.js Template Refs](https://vuejs.org/guide/essentials/template-refs.html)
```

## File: `skills/vue-debug-guides/reference/template-ref-unwrapping-top-level.md`
```markdown
---
title: Template Ref Unwrapping Only Works for Top-Level Properties
impact: MEDIUM
impactDescription: Nested refs in template expressions render as [object Object] instead of their values
type: capability
tags: [vue3, reactivity, ref, template, unwrapping]
---

# Template Ref Unwrapping Only Works for Top-Level Properties

**Impact: MEDIUM** - Vue only auto-unwraps refs that are top-level properties in the template render context. Nested refs (refs inside objects) are NOT unwrapped in expressions, causing `[object Object]` rendering or calculation errors.

This caveat trips up developers when they store refs inside reactive objects or plain objects and try to use them in template expressions like `{{ object.count + 1 }}`.

## Task Checklist

- [ ] Keep refs at the top level of your setup return or script setup
- [ ] Destructure nested refs to top-level variables before using in expressions
- [ ] Be aware that text interpolation `{{ object.ref }}` DOES unwrap, but expressions `{{ object.ref + 1 }}` do NOT
- [ ] Consider restructuring data to avoid nested refs in templates

**Incorrect:**
```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const object = { id: ref(1) }
</script>

<template>
  <!-- WRONG: Nested ref in expression - does NOT unwrap -->
  <p>ID + 1 = {{ object.id + 1 }}</p>
  <!-- Renders: "ID + 1 = [object Object]1" -->

  <!-- Surprisingly, plain interpolation DOES work -->
  <p>ID = {{ object.id }}</p>
  <!-- Renders: "ID = 1" (unwrapped because it's the final expression) -->
</template>
```

**Correct:**
```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const object = { id: ref(1) }

// SOLUTION 1: Destructure to top-level
const { id } = object
</script>

<template>
  <!-- CORRECT: Top-level ref unwraps in all expressions -->
  <p>Count + 1 = {{ count + 1 }}</p>
  <!-- Renders: "Count + 1 = 1" -->

  <!-- CORRECT: Destructured ref is now top-level -->
  <p>ID + 1 = {{ id + 1 }}</p>
  <!-- Renders: "ID + 1 = 2" -->
</template>
```

```vue
<script setup>
import { ref, computed } from 'vue'

const object = { id: ref(1) }

// SOLUTION 2: Use computed for derived values
const idPlusOne = computed(() => object.id.value + 1)
</script>

<template>
  <!-- CORRECT: Computed handles the .value access -->
  <p>ID + 1 = {{ idPlusOne }}</p>
</template>
```

```vue
<script setup>
import { reactive } from 'vue'

// SOLUTION 3: Use reactive object instead (refs inside reactive auto-unwrap)
const object = reactive({ id: 1 })
</script>

<template>
  <!-- CORRECT: Plain reactive property works in expressions -->
  <p>ID + 1 = {{ object.id + 1 }}</p>
</template>
```

```javascript
// WHY this happens:
// - Template compilation only adds .value to top-level identifiers
// - {{ count + 1 }} compiles to: count.value + 1
// - {{ object.id + 1 }} compiles to: object.id + 1 (no .value added!)
// - Plain {{ object.id }} has special handling for display purposes
```

## Reference
- [Vue.js Reactivity Fundamentals - Caveat when Unwrapping in Templates](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-when-unwrapping-in-templates)
```

## File: `skills/vue-debug-guides/reference/template-ref-v-for-order.md`
```markdown
---
title: Template Ref Array Order Not Guaranteed in v-for
impact: MEDIUM
impactDescription: Refs collected from v-for may not match source array order, causing index-based bugs
type: gotcha
tags: [vue3, template-refs, v-for, arrays, ordering]
---

# Template Ref Array Order Not Guaranteed in v-for

**Impact: MEDIUM** - When using template refs inside `v-for`, Vue collects the element references into an array. However, this array does NOT guarantee the same order as the source array. Relying on index-based access can lead to subtle bugs.

This caveat is not obvious and can cause hard-to-debug issues when you assume the ref array matches your data order.

> **Warning: `useTemplateRef()` does NOT work with v-for refs in Vue 3.5**
>
> The `useTemplateRef()` API returns `null` when used with refs inside `v-for`. This is a known limitation. You must use the legacy pattern with `ref()` and a matching template ref name:
>
> ```ts
> // Does NOT work with v-for - returns null
> const itemRefs = useTemplateRef('items')
>
> // Works with v-for - use this pattern instead
> const items = ref([])  // name must match ref="items" in template
> ```
>
> The examples in this rule show `useTemplateRef()` for illustration, but in practice you should use the legacy `ref()` pattern for v-for scenarios until this limitation is addressed.

## Task Checklist

- [ ] Never assume ref array indices match source data array indices
- [ ] Use data attributes or other identifiers to correlate refs with data
- [ ] Consider function refs for complex scenarios requiring ordered access
- [ ] Test with dynamic list operations (add, remove, reorder) to verify behavior

**Incorrect:**
```vue
<script setup>
import { ref, useTemplateRef, onMounted } from 'vue'

const items = ref(['First', 'Second', 'Third'])
const itemRefs = useTemplateRef('items')

onMounted(() => {
  // WRONG: Assuming itemRefs[0] corresponds to items[0]
  // The order is NOT guaranteed to match!
  items.value.forEach((item, index) => {
    console.log(`${item}: `, itemRefs.value[index]) // May be wrong element!
  })
})
</script>

<template>
  <ul>
    <li v-for="item in items" ref="items" :key="item">
      {{ item }}
    </li>
  </ul>
</template>
```

**Correct:**
```vue
<script setup>
import { ref, useTemplateRef, onMounted } from 'vue'

const items = ref([
  { id: 1, text: 'First' },
  { id: 2, text: 'Second' },
  { id: 3, text: 'Third' }
])
const itemRefs = useTemplateRef('items')

onMounted(() => {
  // CORRECT: Use data attributes to identify elements
  itemRefs.value.forEach(el => {
    const id = el.dataset.id
    const item = items.value.find(i => i.id === Number(id))
    console.log(`${item.text}: `, el)
  })
})
</script>

<template>
  <ul>
    <li
      v-for="item in items"
      ref="items"
      :key="item.id"
      :data-id="item.id"
    >
      {{ item.text }}
    </li>
  </ul>
</template>
```

```vue
<script setup>
import { ref, onMounted, onBeforeUpdate } from 'vue'

const items = ref(['First', 'Second', 'Third'])
const itemRefs = ref(new Map())

// CORRECT: Use function refs for precise control
function setItemRef(el, item) {
  if (el) {
    itemRefs.value.set(item, el)
  } else {
    itemRefs.value.delete(item)
  }
}

// Reset before each update to handle removed items
onBeforeUpdate(() => {
  itemRefs.value.clear()
})

onMounted(() => {
  // Access refs by their associated data item
  items.value.forEach(item => {
    const el = itemRefs.value.get(item)
    console.log(`${item}: `, el)
  })
})
</script>

<template>
  <ul>
    <li
      v-for="item in items"
      :key="item"
      :ref="(el) => setItemRef(el, item)"
    >
      {{ item }}
    </li>
  </ul>
</template>
```

```vue
<script setup>
import { ref, useTemplateRef, onMounted } from 'vue'

const items = ref(['First', 'Second', 'Third'])
const itemRefs = useTemplateRef('items')

// CORRECT: If order matters, sort refs by DOM position
onMounted(() => {
  const sortedRefs = [...itemRefs.value].sort((a, b) => {
    // Sort by DOM order using compareDocumentPosition
    return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1
  })

  // Now sortedRefs matches visual/DOM order
  sortedRefs.forEach((el, index) => {
    console.log(`Position ${index}: `, el.textContent)
  })
})
</script>

<template>
  <ul>
    <li v-for="item in items" ref="items" :key="item">
      {{ item }}
    </li>
  </ul>
</template>
```

## Reference
- [Vue.js Template Refs - Refs inside v-for](https://vuejs.org/guide/essentials/template-refs.html#refs-inside-v-for)
```

## File: `skills/vue-debug-guides/reference/textarea-no-interpolation.md`
```markdown
---
title: Textarea Interpolation is One-Way Only - Use v-model for Two-Way Binding
impact: HIGH
impactDescription: Using {{ text }} inside textarea displays initial value but user input does NOT update the ref
type: capability
tags: [vue3, v-model, forms, textarea, interpolation, template]
---

# Textarea Interpolation is One-Way Only - Use v-model for Two-Way Binding

**Impact: HIGH** - Interpolation in textarea (`{{ text }}`) provides one-way binding only - it displays the initial value but user input does NOT update the ref. This creates a confusing disconnect where the textarea shows content but edits are silently lost.

Unlike v-model which provides two-way binding, interpolation only renders the initial ref value into the textarea. When users type, the ref remains unchanged, making form submissions return stale data. Always use v-model for two-way binding in textareas.

## Task Checklist

- [ ] Never use interpolation inside textarea tags
- [ ] Always use v-model for textarea two-way binding
- [ ] Search codebase for `<textarea>{{` patterns that may be silently broken
- [ ] Add linting rules to catch this pattern if possible

**Incorrect:**
```html
<script setup>
import { ref } from 'vue'

const message = ref('Hello World')
</script>

<template>
  <!-- WRONG: One-way binding only! Shows initial value but edits don't update ref -->
  <textarea>{{ message }}</textarea>

  <!-- Also WRONG: User can type but changes are lost -->
  <textarea>{{ userBio }}</textarea>

  <!-- The textarea displays content but ref never updates -->
</template>
```

**Correct:**
```html
<script setup>
import { ref } from 'vue'

const message = ref('Hello World')
</script>

<template>
  <!-- CORRECT: Use v-model for textarea -->
  <textarea v-model="message"></textarea>

  <!-- For read-only display, still use v-model or :value -->
  <textarea v-model="message" readonly></textarea>

  <!-- Or one-way binding with :value -->
  <textarea :value="message" readonly></textarea>
</template>
```

```html
<!-- With placeholder and other attributes -->
<textarea
  v-model="message"
  placeholder="Enter your message..."
  rows="5"
  maxlength="500"
></textarea>
```

## Reference
- [Vue.js Form Input Bindings - Multiline text](https://vuejs.org/guide/essentials/forms.html#multiline-text)
```

## File: `skills/vue-debug-guides/reference/transition-group-flip-inline-elements.md`
```markdown
---
title: TransitionGroup FLIP Animations Do Not Work With Inline Elements
impact: MEDIUM
impactDescription: Move animations silently fail on inline elements, causing items to jump
type: gotcha
tags: [vue3, transition-group, animation, flip, css, display, inline-block]
---

# TransitionGroup FLIP Animations Do Not Work With Inline Elements

**Impact: MEDIUM** - The FLIP (First, Last, Invert, Play) animation technique that Vue uses for `<TransitionGroup>` move transitions does not work with elements that have `display: inline`. The move animation will silently fail, and items will jump to their new positions instead of smoothly transitioning.

This is a CSS limitation, not a Vue bug. CSS transforms (which FLIP uses internally) do not apply to inline elements per the CSS specification.

## Task Checklist

- [ ] Ensure list items are not `display: inline` elements
- [ ] Use `display: inline-block` or `display: block` for list items
- [ ] Use flexbox or grid containers which make children block-level
- [ ] Check if inherited styles are setting `display: inline`

**Incorrect - Inline elements break move animations:**
```vue
<template>
  <!-- BROKEN: span elements are inline by default -->
  <TransitionGroup name="tag" tag="div" class="tag-container">
    <span v-for="tag in tags" :key="tag.id" class="tag">
      {{ tag.name }}
    </span>
  </TransitionGroup>
</template>

<style>
.tag-move {
  transition: transform 0.3s ease;
  /* This won't work because spans are inline! */
}
</style>
```

**Correct - Use inline-block:**
```vue
<template>
  <TransitionGroup name="tag" tag="div" class="tag-container">
    <span v-for="tag in tags" :key="tag.id" class="tag">
      {{ tag.name }}
    </span>
  </TransitionGroup>
</template>

<style>
.tag {
  display: inline-block; /* REQUIRED for FLIP animations */
}

.tag-move {
  transition: transform 0.3s ease;
}
</style>
```

**Correct - Use flexbox container:**
```vue
<template>
  <TransitionGroup name="tag" tag="div" class="tag-container">
    <span v-for="tag in tags" :key="tag.id" class="tag">
      {{ tag.name }}
    </span>
  </TransitionGroup>
</template>

<style>
.tag-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

/* Flex children are block-level, FLIP works automatically */
.tag-move {
  transition: transform 0.3s ease;
}
</style>
```

**Correct - Use block elements:**
```vue
<template>
  <!-- div elements are block by default -->
  <TransitionGroup name="item" tag="div">
    <div v-for="item in items" :key="item.id" class="item">
      {{ item.name }}
    </div>
  </TransitionGroup>
</template>

<style>
.item-move {
  transition: transform 0.3s ease;
}
</style>
```

## Why Inline Elements Don't Work

Per CSS specifications, the `transform` property does not apply to inline boxes. Since FLIP animations use CSS transforms to animate element positions:

```css
/* Vue internally applies something like this during move */
.item {
  transform: translateX(-50px) translateY(-20px);
  /* Then transitions to transform: none */
}
```

This transform is ignored on inline elements, so no animation occurs.

## Elements That Are Inline by Default

Be aware of these common inline elements that need `display: inline-block`:

- `<span>`
- `<a>`
- `<em>`, `<strong>`, `<i>`, `<b>`
- `<code>`, `<kbd>`
- `<label>`
- `<button>` (inline-block by default, but verify)

## Move Animations Also Require Transform Transition

The `.move` class must have `transform` in its `transition` property:

```css
/* CORRECT */
.list-move {
  transition: transform 0.3s ease;
}

/* ALSO CORRECT */
.list-move {
  transition: all 0.3s ease; /* 'all' includes transform */
}

/* WRONG - transform not included */
.list-move {
  transition: opacity 0.3s ease; /* Move won't animate! */
}
```

## Reference
- [Vue.js TransitionGroup Move Transitions](https://vuejs.org/guide/built-ins/transition-group.html#move-transitions)
- [MDN CSS Transform - Formal Definition](https://developer.mozilla.org/en-US/docs/Web/CSS/transform#formal_definition)
```

## File: `skills/vue-debug-guides/reference/transition-group-move-animation-position-absolute.md`
```markdown
---
title: TransitionGroup Move Animation Requires Position Absolute on Leaving Items
impact: HIGH
impactDescription: Without position absolute, surrounding items jump instead of smoothly animating
type: gotcha
tags: [vue3, transition-group, animation, move-transition, css, list-animation]
---

# TransitionGroup Move Animation Requires Position Absolute on Leaving Items

**Impact: HIGH** - When items are added or removed from a list with `<TransitionGroup>`, surrounding items will instantly "jump" to their new positions instead of smoothly animating. This creates a jarring user experience and is one of the most common mistakes with list animations.

The fix is to set `position: absolute` on the `leave-active` class so leaving items are taken out of the layout flow, allowing other items to smoothly animate into their new positions.

## Task Checklist

- [ ] Add `.list-move` class (or `.[name]-move`) for smooth repositioning
- [ ] Set `position: absolute` on `.list-leave-active` class
- [ ] Ensure the parent container has `position: relative` if needed
- [ ] Test with rapid add/remove operations to verify smooth animations

**Incorrect - Items jump instead of moving:**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>

<style>
/* INCOMPLETE: Missing move class and position absolute */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
```

**Correct - Smooth move transitions:**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>

<style>
/* CORRECT: Full set of classes for smooth animations */

/* Apply transition to moving elements */
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* CRITICAL: Take leaving items out of layout flow */
.list-leave-active {
  position: absolute;
}
</style>
```

## Why This Works

The FLIP animation technique Vue uses internally needs to calculate element positions. When an item leaves:

1. Without `position: absolute`: The leaving item still occupies space in the DOM
2. Other items can't move until the leaving item is fully removed
3. Result: Items snap to new positions after leave animation completes

With `position: absolute`:

1. Leaving item is removed from normal layout flow immediately
2. Other items can begin moving into the vacated space
3. Result: Leaving animation and move animation happen simultaneously

## Visual Diagram

```
Without position: absolute:
[A] [B] [C] [D]  <- Remove B
[A]     [C] [D]  <- B fading out, C/D waiting
[A] [C] [D]      <- B gone, C/D jump instantly

With position: absolute:
[A] [B] [C] [D]  <- Remove B
[A][B][C] [D]    <- B fading (absolute), C/D sliding left
[A] [C] [D]      <- Smooth completion
```

## Additional Considerations

**Container Width:** When using `position: absolute`, items may need explicit widths:

```css
.list-leave-active {
  position: absolute;
  width: 100%; /* Or specific width to maintain layout during leave */
}
```

**Stacking Context:** Leaving items with `position: absolute` may stack above other elements:

```css
.list-leave-active {
  position: absolute;
  z-index: -1; /* Optional: put behind other items */
}
```

## Reference
- [Vue.js TransitionGroup Move Transitions](https://vuejs.org/guide/built-ins/transition-group.html#move-transitions)
- [FLIP Animation Technique](https://aerotwist.com/blog/flip-your-animations/)
```

## File: `skills/vue-debug-guides/reference/transition-group-no-default-wrapper-vue3.md`
```markdown
---
title: TransitionGroup No Longer Renders Default Wrapper Element in Vue 3
impact: MEDIUM
impactDescription: Vue 2 to Vue 3 migration may break layouts relying on the default span wrapper
type: gotcha
tags: [vue3, transition-group, migration, vue2, breaking-change, wrapper-element]
---

# TransitionGroup No Longer Renders Default Wrapper Element in Vue 3

**Impact: MEDIUM** - In Vue 2, `<transition-group>` always rendered a wrapper element (default `<span>`), but in Vue 3, it renders no wrapper element by default thanks to fragment support. This breaking change can cause layout issues and broken styles when migrating from Vue 2.

If your code relies on the wrapper element for styling or layout, you must explicitly specify the `tag` prop in Vue 3.

## Task Checklist

- [ ] When migrating from Vue 2, add explicit `tag` prop to all `<TransitionGroup>` components
- [ ] Review CSS selectors that targeted the wrapper element
- [ ] Update parent component styles that expected a wrapper element
- [ ] Consider if the wrapper element is actually needed in Vue 3

**Vue 2 Behavior (wrapper element by default):**
```vue
<template>
  <transition-group name="list">
    <div v-for="item in items" :key="item.id">{{ item }}</div>
  </transition-group>
</template>

<!-- Renders as: -->
<span>  <!-- Default wrapper in Vue 2 -->
  <div>Item 1</div>
  <div>Item 2</div>
</span>
```

**Vue 3 Behavior (no wrapper by default):**
```vue
<template>
  <TransitionGroup name="list">
    <div v-for="item in items" :key="item.id">{{ item }}</div>
  </TransitionGroup>
</template>

<!-- Renders as (fragment): -->
<div>Item 1</div>
<div>Item 2</div>
<!-- No wrapper element! -->
```

**Vue 3 - Explicitly specify wrapper:**
```vue
<template>
  <!-- Use tag prop to specify wrapper element -->
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">{{ item }}</li>
  </TransitionGroup>
</template>

<!-- Renders as: -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

## Migration Scenarios

### Layout Depending on Wrapper

**Vue 2 code that breaks in Vue 3:**
```vue
<template>
  <transition-group class="grid-container" name="list">
    <div v-for="item in items" :key="item.id">{{ item }}</div>
  </transition-group>
</template>

<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
</style>
```

In Vue 3, the class is not applied to anything because there's no wrapper element.

**Fixed for Vue 3:**
```vue
<template>
  <TransitionGroup class="grid-container" name="list" tag="div">
    <div v-for="item in items" :key="item.id">{{ item }}</div>
  </TransitionGroup>
</template>
```

### Semantic HTML Lists

**Vue 2:**
```vue
<transition-group tag="ul" name="list">
  <li v-for="item in items" :key="item.id">{{ item }}</li>
</transition-group>
```

**Vue 3 (same syntax, but now tag is more important):**
```vue
<TransitionGroup tag="ul" name="list">
  <li v-for="item in items" :key="item.id">{{ item }}</li>
</TransitionGroup>
```

### When You Don't Need a Wrapper

Vue 3's fragment support means you might not need a wrapper at all:

```vue
<template>
  <div class="parent-with-styles">
    <!-- No tag needed if parent handles layout -->
    <TransitionGroup name="fade">
      <span v-for="item in items" :key="item.id">{{ item }}</span>
    </TransitionGroup>
  </div>
</template>

<style>
.parent-with-styles {
  display: flex;
  gap: 8px;
}
</style>
```

## In-DOM Template Syntax

When using in-DOM templates (not SFCs), remember to use kebab-case:

```html
<!-- In-DOM template -->
<transition-group tag="ul" name="list">
  <li v-for="item in items" :key="item.id">{{ item }}</li>
</transition-group>

<!-- NOT -->
<TransitionGroup tag="ul" name="list">  <!-- Won't work in DOM templates -->
```

## Reference
- [Vue 3 Migration Guide - TransitionGroup Root Element](https://v3-migration.vuejs.org/breaking-changes/transition-group.html)
- [Vue.js TransitionGroup](https://vuejs.org/guide/built-ins/transition-group.html)
```

## File: `skills/vue-debug-guides/reference/transition-js-hooks-done-callback.md`
```markdown
---
title: JavaScript Transition Hooks Require done() Callback with css="false"
impact: HIGH
impactDescription: Without calling done(), JavaScript-only transitions complete immediately, skipping the animation entirely
type: gotcha
tags: [vue3, transition, javascript, animation, hooks, gsap, done-callback]
---

# JavaScript Transition Hooks Require done() Callback with css="false"

**Impact: HIGH** - When using JavaScript-only transitions (with `:css="false"`), the `@enter` and `@leave` hooks **must** call the `done()` callback to signal when the animation completes. Without calling `done()`, Vue considers the transition finished immediately, causing elements to appear/disappear without animation.

This is especially important when using animation libraries like GSAP, Anime.js, or the Web Animations API.

## Task Checklist

- [ ] When using `:css="false"`, always call `done()` in `@enter` and `@leave` hooks
- [ ] Call `done()` when your JavaScript animation completes (in the `onComplete` callback)
- [ ] Remember: `done()` is optional when CSS handles the transition, but **required** with `:css="false"`
- [ ] Use `:css="false"` to prevent CSS rules from interfering with JS animations

**Problematic Code:**
```vue
<template>
  <!-- BAD: No done() callback - animation is skipped! -->
  <Transition :css="false" @enter="onEnter" @leave="onLeave">
    <div v-if="show" class="box">Content</div>
  </Transition>
</template>

<script setup>
import gsap from 'gsap'

function onEnter(el) {
  // Animation starts but Vue doesn't wait for it!
  gsap.from(el, {
    opacity: 0,
    y: 50,
    duration: 0.5
  })
  // Missing done() call - element appears with no animation
}

function onLeave(el) {
  gsap.to(el, {
    opacity: 0,
    y: -50,
    duration: 0.5
  })
  // Missing done() call - element removed immediately!
}
</script>
```

**Correct Code:**
```vue
<template>
  <!-- GOOD: done() callback signals animation completion -->
  <Transition :css="false" @enter="onEnter" @leave="onLeave">
    <div v-if="show" class="box">Content</div>
  </Transition>
</template>

<script setup>
import gsap from 'gsap'

function onEnter(el, done) {
  gsap.from(el, {
    opacity: 0,
    y: 50,
    duration: 0.5,
    onComplete: done  // Tell Vue animation is complete
  })
}

function onLeave(el, done) {
  gsap.to(el, {
    opacity: 0,
    y: -50,
    duration: 0.5,
    onComplete: done  // Element removed after animation
  })
}
</script>
```

## Why Use `:css="false"`?

1. **Prevents CSS interference**: Vue won't add transition classes that might conflict
2. **Slight performance benefit**: Skips CSS transition detection
3. **Clearer intent**: Makes it explicit that JS controls the animation

```vue
<template>
  <!-- Without :css="false", Vue adds v-enter-active etc. classes -->
  <!-- These can interfere with your JS animation timing -->
  <Transition @enter="onEnter" @leave="onLeave">
    <div v-if="show">May have CSS conflicts</div>
  </Transition>

  <!-- With :css="false", no classes added - full JS control -->
  <Transition :css="false" @enter="onEnter" @leave="onLeave">
    <div v-if="show">Pure JS animation</div>
  </Transition>
</template>
```

## Complete JavaScript Transition Example

```vue
<template>
  <Transition
    :css="false"
    @before-enter="onBeforeEnter"
    @enter="onEnter"
    @after-enter="onAfterEnter"
    @enter-cancelled="onEnterCancelled"
    @before-leave="onBeforeLeave"
    @leave="onLeave"
    @after-leave="onAfterLeave"
    @leave-cancelled="onLeaveCancelled"
  >
    <div v-if="show" class="animated-box">Content</div>
  </Transition>
</template>

<script setup>
import gsap from 'gsap'
import { ref } from 'vue'

const show = ref(false)
let enterAnimation = null
let leaveAnimation = null

function onBeforeEnter(el) {
  // Set initial state before animation
  el.style.opacity = 0
  el.style.transform = 'translateY(50px)'
}

function onEnter(el, done) {
  // Store animation reference for potential cancellation
  enterAnimation = gsap.to(el, {
    opacity: 1,
    y: 0,
    duration: 0.5,
    ease: 'power2.out',
    onComplete: done  // REQUIRED with :css="false"
  })
}

function onAfterEnter(el) {
  // Cleanup after enter completes
  enterAnimation = null
}

function onEnterCancelled() {
  // Handle interruption (e.g., user toggles quickly)
  if (enterAnimation) {
    enterAnimation.kill()
    enterAnimation = null
  }
}

function onBeforeLeave(el) {
  // Set state before leaving
}

function onLeave(el, done) {
  leaveAnimation = gsap.to(el, {
    opacity: 0,
    y: -50,
    duration: 0.5,
    ease: 'power2.in',
    onComplete: done  // REQUIRED with :css="false"
  })
}

function onAfterLeave(el) {
  leaveAnimation = null
}

function onLeaveCancelled() {
  if (leaveAnimation) {
    leaveAnimation.kill()
    leaveAnimation = null
  }
}
</script>
```

## Using Web Animations API

```vue
<script setup>
function onEnter(el, done) {
  const animation = el.animate([
    { opacity: 0, transform: 'scale(0.9)' },
    { opacity: 1, transform: 'scale(1)' }
  ], {
    duration: 300,
    easing: 'ease-out'
  })

  animation.onfinish = done  // Call done when animation ends
}

function onLeave(el, done) {
  const animation = el.animate([
    { opacity: 1, transform: 'scale(1)' },
    { opacity: 0, transform: 'scale(0.9)' }
  ], {
    duration: 300,
    easing: 'ease-in'
  })

  animation.onfinish = done
}
</script>
```

## Common Mistakes

```javascript
// WRONG: Calling done() immediately instead of after animation
function onEnter(el, done) {
  gsap.from(el, { opacity: 0, duration: 0.5 })
  done() // Called immediately - animation skipped!
}

// WRONG: Forgetting done() parameter
function onEnter(el) {  // No 'done' parameter
  gsap.from(el, {
    opacity: 0,
    onComplete: done  // Error: done is not defined!
  })
}

// CORRECT: Pass done to animation callback
function onEnter(el, done) {
  gsap.from(el, {
    opacity: 0,
    duration: 0.5,
    onComplete: done  // Called after 0.5s
  })
}
```

## Reference
- [Vue.js Transition - JavaScript Hooks](https://vuejs.org/guide/built-ins/transition.html#javascript-hooks)
- [GSAP with Vue](https://gsap.com/resources/vue/)
```

## File: `skills/vue-debug-guides/reference/transition-nested-duration.md`
```markdown
---
title: Specify Explicit Duration for Nested Transitions
impact: MEDIUM
impactDescription: Nested transitions with different timings may end prematurely when Vue detects only the root element's transition end
type: gotcha
tags: [vue3, transition, animation, duration, nested, timing]
---

# Specify Explicit Duration for Nested Transitions

**Impact: MEDIUM** - When transitioning elements that contain nested child elements with different animation timings, Vue by default listens only for the first `transitionend` or `animationend` event on the **root** transition element. This means if inner elements have longer or delayed animations, they may be cut off when the root element's transition completes.

## Task Checklist

- [ ] Identify if your transition contains nested elements with different animation durations
- [ ] Use the `:duration` prop to specify the total time Vue should wait
- [ ] Consider using separate enter and leave durations if they differ
- [ ] Test animations to ensure nested elements complete fully

**Problematic Code:**
```vue
<template>
  <!-- BAD: Inner element has longer animation that gets cut off -->
  <Transition name="nested">
    <div v-if="show" class="outer">
      <div class="inner">Hello</div>
    </div>
  </Transition>
</template>

<style>
.nested-enter-active .outer,
.nested-leave-active .outer {
  transition: opacity 0.3s ease;
}

.nested-enter-active .inner,
.nested-leave-active .inner {
  /* This 0.5s animation gets cut off at 0.3s when outer finishes! */
  transition: transform 0.5s ease 0.2s; /* 0.2s delay + 0.5s = 0.7s total */
}

.nested-enter-from .outer,
.nested-leave-to .outer {
  opacity: 0;
}

.nested-enter-from .inner,
.nested-leave-to .inner {
  transform: translateX(-30px);
}
</style>
```

**Correct Code:**
```vue
<template>
  <!-- GOOD: Explicit duration ensures all nested animations complete -->
  <Transition name="nested" :duration="700">
    <div v-if="show" class="outer">
      <div class="inner">Hello</div>
    </div>
  </Transition>
</template>

<style>
.nested-enter-active .outer,
.nested-leave-active .outer {
  transition: opacity 0.3s ease;
}

.nested-enter-active .inner,
.nested-leave-active .inner {
  /* Now this animation completes fully */
  transition: transform 0.5s ease 0.2s;
}

.nested-enter-from .outer,
.nested-leave-to .outer {
  opacity: 0;
}

.nested-enter-from .inner,
.nested-leave-to .inner {
  transform: translateX(-30px);
}
</style>
```

## Different Enter and Leave Durations

```vue
<template>
  <!-- GOOD: Separate durations for enter and leave -->
  <Transition
    name="complex"
    :duration="{ enter: 500, leave: 800 }"
  >
    <div v-if="show" class="container">
      <h1 class="title">Title</h1>
      <p class="content">Content with staggered animation</p>
    </div>
  </Transition>
</template>

<style>
/* Enter: title first, then content */
.complex-enter-active .title {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.complex-enter-active .content {
  transition: opacity 0.3s ease 0.2s, transform 0.3s ease 0.2s;
}

/* Leave: content first, then title (reverse order) */
.complex-leave-active .content {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.complex-leave-active .title {
  transition: opacity 0.5s ease 0.3s, transform 0.5s ease 0.3s;
}

.complex-enter-from .title,
.complex-enter-from .content,
.complex-leave-to .title,
.complex-leave-to .content {
  opacity: 0;
  transform: translateY(20px);
}
</style>
```

## Choreographed Staggered Animations

```vue
<template>
  <Transition name="stagger" :duration="800">
    <div v-if="show" class="card">
      <img class="card-image" src="..." />
      <h2 class="card-title">Title</h2>
      <p class="card-body">Body text...</p>
      <button class="card-action">Action</button>
    </div>
  </Transition>
</template>

<style>
/* Staggered entrance: image -> title -> body -> action */
.stagger-enter-active .card-image { transition: all 0.3s ease; }
.stagger-enter-active .card-title { transition: all 0.3s ease 0.1s; }
.stagger-enter-active .card-body { transition: all 0.3s ease 0.2s; }
.stagger-enter-active .card-action { transition: all 0.3s ease 0.3s; }
/* Total: 0.3s delay + 0.3s animation = 0.6s, but use 800ms for safety */

.stagger-enter-from .card-image,
.stagger-enter-from .card-title,
.stagger-enter-from .card-body,
.stagger-enter-from .card-action {
  opacity: 0;
  transform: translateY(10px);
}
</style>
```

## Calculating Duration

Use this formula to calculate the correct duration:
```
duration = max(delay + animation_duration) for all nested elements
```

Example:
- Element A: no delay, 300ms duration = 300ms total
- Element B: 100ms delay, 300ms duration = 400ms total
- Element C: 200ms delay, 500ms duration = 700ms total

**Required `:duration`**: 700 (or slightly higher for safety margin)

## Reference
- [Vue.js Transition - Nested Transitions](https://vuejs.org/guide/built-ins/transition.html#nested-transitions-and-explicit-transition-durations)
```

## File: `skills/vue-debug-guides/reference/transition-reusable-scoped-style.md`
```markdown
---
title: Avoid Scoped Styles in Reusable Transition Components
impact: MEDIUM
impactDescription: Scoped styles in transition wrapper components won't apply to slotted content, breaking the transition animation
type: gotcha
tags: [vue3, transition, scoped-css, slot, reusable-component]
---

# Avoid Scoped Styles in Reusable Transition Components

**Impact: MEDIUM** - When creating reusable transition wrapper components, using `<style scoped>` will prevent the transition CSS classes from applying to slotted content. Scoped styles only affect elements directly in the component's template, not content passed through slots. Your transition animations will silently fail.

## Task Checklist

- [ ] In reusable transition components, use `<style>` without `scoped`
- [ ] Alternatively, use unique class name prefixes to avoid global conflicts
- [ ] Or use CSS modules with `:global()` for transition classes
- [ ] Test that transitions work when component is used in different contexts

**Problematic Code:**
```vue
<!-- MyFadeTransition.vue -->
<template>
  <Transition name="my-fade">
    <slot />
  </Transition>
</template>

<!-- BAD: Scoped styles won't apply to slot content! -->
<style scoped>
.my-fade-enter-active,
.my-fade-leave-active {
  transition: opacity 0.3s ease;
}

.my-fade-enter-from,
.my-fade-leave-to {
  opacity: 0;
}
</style>
```

```vue
<!-- Parent component using the transition -->
<template>
  <MyFadeTransition>
    <div v-if="show">This won't animate!</div>
  </MyFadeTransition>
</template>

<!--
The <div> is slotted content, so .my-fade-* classes
applied by Vue won't match the scoped CSS selectors
-->
```

**Correct Code:**
```vue
<!-- MyFadeTransition.vue -->
<template>
  <Transition name="my-fade">
    <slot />
  </Transition>
</template>

<!-- GOOD: Unscoped styles apply to any element -->
<style>
.my-fade-enter-active,
.my-fade-leave-active {
  transition: opacity 0.3s ease;
}

.my-fade-enter-from,
.my-fade-leave-to {
  opacity: 0;
}
</style>
```

## Alternative: Use Unique Prefixed Class Names

To avoid global style conflicts, use distinctive prefixes:

```vue
<!-- FadeTransition.vue -->
<template>
  <Transition name="v-fade-transition">
    <slot />
  </Transition>
</template>

<style>
/* Unique prefix reduces collision risk */
.v-fade-transition-enter-active,
.v-fade-transition-leave-active {
  transition: opacity 0.3s ease;
}

.v-fade-transition-enter-from,
.v-fade-transition-leave-to {
  opacity: 0;
}
</style>
```

## Alternative: CSS Modules with :global()

```vue
<!-- FadeTransition.vue -->
<template>
  <Transition name="fade">
    <slot />
  </Transition>
</template>

<style module>
/* Use :global() for transition classes */
:global(.fade-enter-active),
:global(.fade-leave-active) {
  transition: opacity 0.3s ease;
}

:global(.fade-enter-from),
:global(.fade-leave-to) {
  opacity: 0;
}
</style>
```

## Alternative: Custom Transition Classes

Use the custom class props to apply scoped classes:

```vue
<!-- FadeTransition.vue -->
<template>
  <Transition
    :enter-active-class="$style.enterActive"
    :leave-active-class="$style.leaveActive"
    :enter-from-class="$style.enterFrom"
    :leave-to-class="$style.leaveTo"
  >
    <slot />
  </Transition>
</template>

<style module>
.enterActive,
.leaveActive {
  transition: opacity 0.3s ease;
}

.enterFrom,
.leaveTo {
  opacity: 0;
}
</style>
```

## Complete Reusable Transition Component Example

```vue
<!-- transitions/SlideTransition.vue -->
<template>
  <Transition
    name="slide"
    :mode="mode"
    :appear="appear"
    @before-enter="$emit('before-enter', $event)"
    @enter="$emit('enter', $event)"
    @after-enter="$emit('after-enter', $event)"
    @before-leave="$emit('before-leave', $event)"
    @leave="$emit('leave', $event)"
    @after-leave="$emit('after-leave', $event)"
  >
    <slot />
  </Transition>
</template>

<script setup>
defineProps({
  mode: {
    type: String,
    default: 'out-in',
    validator: (v) => ['out-in', 'in-out', ''].includes(v)
  },
  appear: {
    type: Boolean,
    default: false
  }
})

defineEmits([
  'before-enter', 'enter', 'after-enter',
  'before-leave', 'leave', 'after-leave'
])
</script>

<!-- Unscoped so styles apply to slotted content -->
<style>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(-20px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(20px);
}
</style>
```

Usage:
```vue
<template>
  <SlideTransition>
    <div v-if="show" class="content">
      This will properly animate!
    </div>
  </SlideTransition>
</template>
```

## Why This Happens

Vue's scoped styles work by adding a unique data attribute (e.g., `data-v-7ba5bd90`) to elements and selectors:

```css
/* What you write */
.my-fade-enter-active { ... }

/* What Vue generates (scoped) */
.my-fade-enter-active[data-v-7ba5bd90] { ... }
```

Slotted content comes from the parent component and gets the parent's data attribute, not the transition component's attribute. So the selectors never match.

## Reference
- [Vue.js Reusable Transitions](https://vuejs.org/guide/built-ins/transition.html#reusable-transitions)
- [Vue.js Scoped CSS](https://vuejs.org/api/sfc-css-features.html#scoped-css)
```

## File: `skills/vue-debug-guides/reference/transition-router-view-appear.md`
```markdown
---
title: RouterView Transitions Always Apply Despite Missing appear Prop
impact: LOW
impactDescription: Initial page load with RouterView triggers transition animation even without the appear prop due to async navigation
type: gotcha
tags: [vue3, transition, vue-router, appear, initial-load, navigation]
---

# RouterView Transitions Always Apply Despite Missing appear Prop

**Impact: LOW** - When using `<Transition>` with Vue Router's `<RouterView>`, the enter transition animation runs on initial page load even if you haven't added the `appear` prop. This differs from normal Transition behavior where `appear` is required for initial render animations. This happens because Vue Router's navigations are asynchronous, causing the component to mount after the initial render.

## Task Checklist

- [ ] Be aware that RouterView transitions always animate on initial load
- [ ] If you want NO animation on initial load, you need to handle this explicitly
- [ ] Don't add `appear` prop expecting it to change behavior - it's already effectively enabled
- [ ] Consider whether initial animation is desired for your UX

**Expected Behavior (Normal Transition):**
```vue
<template>
  <!-- Without appear: No animation on initial render -->
  <Transition name="fade">
    <div v-if="show">Content</div>
  </Transition>

  <!-- With appear: Animates on initial render -->
  <Transition name="fade" appear>
    <div v-if="show">Content</div>
  </Transition>
</template>
```

**RouterView Behavior (Different!):**
```vue
<template>
  <!-- RouterView transitions ALWAYS animate on initial load -->
  <!-- The appear prop has no effect here -->
  <RouterView v-slot="{ Component }">
    <Transition name="fade">
      <component :is="Component" />
    </Transition>
  </RouterView>
</template>

<!--
On initial page load:
1. Vue renders the app
2. Router resolves the route (async)
3. Component mounts AFTER initial render
4. Enter transition triggers (as if toggled from v-if="false" to v-if="true")
-->
```

## Why This Happens

Vue Router navigations are asynchronous. The sequence is:

1. Vue application mounts with empty RouterView
2. Router resolves the initial route
3. Route component is inserted into RouterView
4. This insertion triggers the enter transition

Since the component wasn't present in the initial render and is "inserted" afterward, Vue treats it as a normal enter transition, not an initial render.

## If You Want to Disable Initial Animation

```vue
<template>
  <RouterView v-slot="{ Component }">
    <Transition :name="isInitialLoad ? '' : 'fade'" mode="out-in">
      <component :is="Component" />
    </Transition>
  </RouterView>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const isInitialLoad = ref(true)
const router = useRouter()

// After first navigation completes, enable transitions
router.isReady().then(() => {
  // Small delay to ensure initial render is complete
  setTimeout(() => {
    isInitialLoad.value = false
  }, 0)
})
</script>
```

## Alternative: Use CSS to Skip First Animation

```vue
<template>
  <RouterView v-slot="{ Component }">
    <Transition name="fade" mode="out-in">
      <component :is="Component" :class="{ 'skip-initial': isInitialLoad }" />
    </Transition>
  </RouterView>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const isInitialLoad = ref(true)
const router = useRouter()

router.isReady().then(() => {
  isInitialLoad.value = false
})
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Skip animation on initial load */
.skip-initial.fade-enter-active {
  transition: none;
}
</style>
```

## Standard RouterView Transition Pattern

If you're fine with initial animation (often desired), use the standard pattern:

```vue
<template>
  <RouterView v-slot="{ Component, route }">
    <Transition :name="route.meta.transition || 'fade'" mode="out-in">
      <component :is="Component" :key="route.path" />
    </Transition>
  </RouterView>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Route-specific transitions via meta */
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from {
  transform: translateX(100%);
}

.slide-leave-to {
  transform: translateX(-100%);
}
</style>
```

```javascript
// router.js
const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/about',
    component: About,
    meta: { transition: 'slide' }  // Custom transition for this route
  }
]
```

## Reference
- [Vue Router Transitions](https://router.vuejs.org/guide/advanced/transitions.html)
- [Vue.js Transition appear](https://vuejs.org/guide/built-ins/transition.html#transition-on-appear)
```

## File: `skills/vue-debug-guides/reference/transition-type-when-mixed.md`
```markdown
---
title: Specify Transition Type When Mixing CSS Transitions and Animations
impact: MEDIUM
impactDescription: Vue may detect the wrong transition end event when both CSS transitions and animations are applied, causing timing issues
type: gotcha
tags: [vue3, transition, animation, css, type, timing]
---

# Specify Transition Type When Mixing CSS Transitions and Animations

**Impact: MEDIUM** - When you have both CSS transitions and CSS animations applied to the same element (for example, a Vue-triggered animation combined with a hover transition effect), Vue cannot automatically determine which end event to listen for. You must explicitly tell Vue which type to prioritize using the `type` attribute with a value of either `"animation"` or `"transition"`.

## Task Checklist

- [ ] Check if your element has both `transition` and `animation` CSS properties
- [ ] Determine which timing should control when Vue considers the transition complete
- [ ] Add `type="animation"` or `type="transition"` to the `<Transition>` component
- [ ] The type should match whichever animation/transition is longer or more important

**Problematic Code:**
```vue
<template>
  <!-- BAD: Both transition and animation present, Vue might pick wrong end event -->
  <Transition name="bounce">
    <div v-if="show" class="box">
      Hover me for additional effect
    </div>
  </Transition>
</template>

<style>
/* Vue-triggered CSS animation */
.bounce-enter-active {
  animation: bounce-in 0.5s;
}

.bounce-leave-active {
  animation: bounce-out 0.3s;
}

@keyframes bounce-in {
  0% { transform: scale(0); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

@keyframes bounce-out {
  0% { transform: scale(1); }
  100% { transform: scale(0); }
}

/* Additional hover transition on same element */
.box {
  transition: background-color 0.2s ease, box-shadow 0.2s ease;
}

.box:hover {
  background-color: #f0f0f0;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
```

**Correct Code:**
```vue
<template>
  <!-- GOOD: Explicitly specify that animation controls timing -->
  <Transition name="bounce" type="animation">
    <div v-if="show" class="box">
      Hover me for additional effect
    </div>
  </Transition>
</template>

<style>
/* Vue-triggered CSS animation - this is what we care about */
.bounce-enter-active {
  animation: bounce-in 0.5s;
}

.bounce-leave-active {
  animation: bounce-out 0.3s;
}

@keyframes bounce-in {
  0% { transform: scale(0); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

@keyframes bounce-out {
  0% { transform: scale(1); }
  100% { transform: scale(0); }
}

/* Additional hover transition - unrelated to Vue transition timing */
.box {
  transition: background-color 0.2s ease, box-shadow 0.2s ease;
}

.box:hover {
  background-color: #f0f0f0;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
```

## When to Use Each Type

### Use `type="animation"` when:
- Your enter/leave effects use `@keyframes` animations
- The animation is longer than any transitions
- You want precise control over multi-step animations

```vue
<Transition name="fancy" type="animation">
  <div v-if="show" class="animated-element" />
</Transition>

<style>
.fancy-enter-active {
  animation: fancy-entrance 1s ease-out;
}

.animated-element {
  /* This shorter transition should not affect timing */
  transition: color 0.2s;
}
</style>
```

### Use `type="transition"` when:
- Your enter/leave effects use CSS `transition` property
- You have decorative animations that shouldn't affect timing

```vue
<Transition name="slide" type="transition">
  <div v-if="show" class="sliding-element" />
</Transition>

<style>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(-100%);
}

/* Decorative infinite animation should not affect timing */
.sliding-element {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}
</style>
```

## Common Symptoms Without Type Specification

1. Transition ends too early (element snaps to final position)
2. Transition hangs or takes too long to complete
3. Element disappears before animation finishes
4. CSS classes remain applied after transition should be complete

## Reference
- [Vue.js Transition Documentation](https://vuejs.org/guide/built-ins/transition.html#css-based-transitions)
```

## File: `skills/vue-debug-guides/reference/transition-unmount-hook-timing.md`
```markdown
---
title: Unmount Hooks May Not Fire Inside Transitions During Fast Replacement
impact: MEDIUM
impactDescription: Components inside transitions can be destroyed without unmount hooks firing under race conditions
type: gotcha
tags: [vue3, lifecycle, transition, onUnmounted, unmounted, cleanup, race-condition]
---

# Unmount Hooks May Not Fire Inside Transitions During Fast Replacement

**Impact: MEDIUM** - When a component inside a `<transition>` is replaced by another component during the transition's loading phase, the unmount hooks (`onBeforeUnmount`, `onUnmounted`) may not be called even though the component is removed from the DOM. This can cause memory leaks and resource leaks from unclean side effects.

This is a known edge case that occurs when the timing is specific - if a parent component with a child inside a transition is replaced while the child is still mounting. The child's mount hooks fire, but unmount hooks never do.

## Task Checklist

- [ ] Be aware that unmount hooks are not 100% guaranteed inside transitions
- [ ] For critical cleanup, consider alternative cleanup strategies
- [ ] Use `mode="out-in"` on transitions to ensure old component fully unmounts before new mounts
- [ ] For essential resources, consider cleanup at parent component level
- [ ] Test component replacement scenarios during development

**Problematic Scenario:**
```vue
<!-- Parent component with lazy-loaded child in transition -->
<template>
  <transition>
    <Suspense>
      <component :is="currentComponent" />
    </Suspense>
  </transition>
</template>
```

```javascript
// Child component - unmount hooks may not fire if parent changes quickly
export default {
  setup() {
    const socket = new WebSocket('wss://example.com')

    onMounted(() => {
      console.log('Mounted - this will run')
      socket.connect()
    })

    onUnmounted(() => {
      // WARNING: This may NOT run if component is inside transition
      // and parent navigates away during mounting phase!
      console.log('Unmounted - might not run')
      socket.close()
    })
  }
}
```

**Safer Patterns:**
```vue
<!-- SAFER: Use out-in mode to ensure proper sequencing -->
<template>
  <transition mode="out-in">
    <component :is="currentComponent" :key="currentKey" />
  </transition>
</template>
```

```javascript
// SAFER: Cleanup at parent level for critical resources
// Parent component
export default {
  setup() {
    const childSocket = ref(null)

    // Parent controls resource lifecycle
    provide('registerSocket', (socket) => {
      childSocket.value = socket
    })

    onUnmounted(() => {
      // Parent ensures cleanup even if child unmount hook doesn't fire
      childSocket.value?.close()
    })
  }
}

// Child component
export default {
  setup() {
    const registerSocket = inject('registerSocket')
    const socket = new WebSocket('wss://example.com')

    // Register with parent for backup cleanup
    registerSocket(socket)

    onMounted(() => {
      socket.connect()
    })

    onUnmounted(() => {
      socket.close() // Still attempt cleanup here
    })
  }
}
```

```javascript
// SAFER: Use AbortController pattern for cancellable operations
export default {
  setup() {
    const abortController = new AbortController()

    onMounted(() => {
      fetch('/api/data', { signal: abortController.signal })
        .then(handleData)
        .catch(err => {
          if (err.name !== 'AbortError') {
            handleError(err)
          }
        })
    })

    onUnmounted(() => {
      // If this doesn't fire, request continues but response is ignored
      // Not a memory leak - just potentially wasted network call
      abortController.abort()
    })
  }
}
```

## Testing for This Issue

```javascript
// Test by rapidly switching components during async loading
async function testUnmountHooks() {
  // Mount component A (has async setup)
  await mountComponent('A')

  // Immediately switch to B before A finishes mounting
  await mountComponent('B')

  // Check if A's unmount hooks fired
  // They may not have!
}
```

## Reference
- [Vue.js GitHub Issue #6260](https://github.com/vuejs/core/issues/6260)
- [Vue.js Transition](https://vuejs.org/guide/built-ins/transition.html)
- [Vue.js Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)
```

## File: `skills/vue-debug-guides/reference/ts-defineprops-boolean-default-false.md`
```markdown
---
title: Boolean Props Default to false, Not undefined
impact: MEDIUM
impactDescription: TypeScript expects optional boolean to be undefined but Vue defaults it to false, causing type confusion
type: gotcha
tags: [vue3, typescript, props, boolean, defineProps]
---

# Boolean Props Default to false, Not undefined

**Impact: MEDIUM** - When using type-based `defineProps`, optional boolean props (marked with `?`) behave differently than TypeScript expects. Vue treats boolean props specially: an absent boolean prop defaults to `false`, not `undefined`. This can cause confusion when TypeScript thinks the type is `boolean | undefined`.

## Task Checklist

- [ ] Understand that Vue's boolean casting makes absent booleans `false`
- [ ] Use `withDefaults()` to be explicit about boolean defaults
- [ ] Consider using non-boolean types if `undefined` is a meaningful state
- [ ] Document this Vue-specific behavior for your team

## The Gotcha

```vue
<script setup lang="ts">
interface Props {
  disabled?: boolean  // TypeScript sees: boolean | undefined
}

const props = defineProps<Props>()

// TypeScript thinks props.disabled could be undefined
if (props.disabled === undefined) {
  console.log('This will NEVER run!')
  // Vue's boolean casting means disabled is false, not undefined
}
</script>

<template>
  <!-- When used without the prop -->
  <MyComponent />
  <!-- disabled is false, NOT undefined -->
</template>
```

## Why This Happens

Vue has special "boolean casting" behavior inherited from HTML boolean attributes:

```vue
<!-- All of these make disabled = true -->
<MyComponent disabled />
<MyComponent :disabled="true" />
<MyComponent disabled="" />

<!-- This makes disabled = false (NOT undefined) -->
<MyComponent />

<!-- Explicit false -->
<MyComponent :disabled="false" />
```

This is by design to match how HTML works:
```html
<!-- HTML: presence means true, absence means false -->
<button disabled>Can't click</button>
<button>Can click</button>
```

## Solutions

### Solution 1: Be Explicit with withDefaults

Make your intention clear:

```vue
<script setup lang="ts">
interface Props {
  disabled?: boolean
}

// Explicitly document the default
const props = withDefaults(defineProps<Props>(), {
  disabled: false  // Now it's clear this defaults to false
})
</script>
```

### Solution 2: Use a Three-State Type

If you actually need to distinguish "not set" from "explicitly false":

```vue
<script setup lang="ts">
interface Props {
  // Use a union type instead of optional boolean
  state?: 'enabled' | 'disabled' | undefined

  // Or use undefined explicitly
  toggleState?: boolean | undefined
}

const props = withDefaults(defineProps<Props>(), {
  state: undefined,  // Can actually be undefined
  toggleState: undefined
})

// Now you can check for undefined
if (props.state === undefined) {
  // Use parent's state
} else if (props.state === 'disabled') {
  // Explicitly disabled
}
</script>
```

### Solution 3: Use null for "Not Set"

```vue
<script setup lang="ts">
interface Props {
  // null = not set, false = explicitly off, true = explicitly on
  selected: boolean | null
}

const props = withDefaults(defineProps<Props>(), {
  selected: null
})

// Three distinct states
if (props.selected === null) {
  console.log('Selection not specified')
} else if (props.selected) {
  console.log('Selected')
} else {
  console.log('Explicitly not selected')
}
</script>
```

## Boolean Casting Order

Vue also has special behavior when Boolean and String are both valid:

```typescript
// Order matters in runtime declaration!
defineProps({
  // Boolean first: empty string becomes true
  disabled: [Boolean, String]
})

// <MyComponent disabled /> → disabled = true
// <MyComponent disabled="" /> → disabled = true
```

```typescript
defineProps({
  // String first: empty string stays as string
  disabled: [String, Boolean]
})

// <MyComponent disabled /> → disabled = ''
// <MyComponent disabled="" /> → disabled = ''
```

With type-based declaration, Boolean always takes priority for absent props.

## Common Bug Pattern

```vue
<!-- Parent.vue -->
<script setup lang="ts">
const userPreferences = ref({
  darkMode: undefined as boolean | undefined
})

// Fetch preferences...
onMounted(async () => {
  userPreferences.value = await fetchPreferences()
})
</script>

<template>
  <!-- Bug: undefined becomes false, not "inherit system preference" -->
  <ThemeToggle :darkMode="userPreferences.darkMode" />
</template>
```

**Fix:**

```vue
<script setup lang="ts">
const userPreferences = ref<{
  darkMode: boolean | null
}>({
  darkMode: null  // Use null for "not yet loaded"
})
</script>

<template>
  <!-- Now ThemeToggle can distinguish between null and false -->
  <ThemeToggle :darkMode="userPreferences.darkMode" />
</template>
```

## TypeScript Type Accuracy

The Vue type system handles this, but it can be confusing:

```typescript
interface Props {
  disabled?: boolean
}

const props = defineProps<Props>()

// At compile time: boolean | undefined
// At runtime: boolean (never undefined due to Vue's boolean casting)

// TypeScript is technically "wrong" here, but the withDefaults usage
// or explicit false default can help align expectations
```

## Reference
- [Vue.js Props - Boolean Casting](https://vuejs.org/guide/components/props.html#boolean-casting)
- [GitHub Issue: Boolean props default to false](https://github.com/vuejs/core/issues/8576)
- [TypeScript Vue 3 Props](https://madewithlove.com/blog/typescript-vue-3-and-strongly-typed-props/)
```

## File: `skills/vue-debug-guides/reference/ts-defineprops-imported-types-limitations.md`
```markdown
---
title: Imported Types Have Limitations in defineProps
impact: MEDIUM
impactDescription: Complex imported types like conditional types can cause compiler errors in defineProps
type: gotcha
tags: [vue3, typescript, defineProps, imported-types, vue3.3]
---

# Imported Types Have Limitations in defineProps

**Impact: MEDIUM** - While Vue 3.3+ supports imported types in `defineProps<>()`, certain complex types are not fully supported. Conditional types, mapped types that require full type analysis, and global ambient types can cause "Unresolvable type reference" errors.

## Task Checklist

- [ ] Understand which type patterns are supported vs unsupported
- [ ] Keep prop type definitions simple and explicit
- [ ] Move complex type logic outside of defineProps
- [ ] Export interfaces explicitly rather than using global declarations

## Supported Patterns (Vue 3.3+)

```typescript
// types/user.ts
export interface User {
  id: string
  name: string
  email?: string
}

export interface ListProps<T> {
  items: T[]
  selectedItem?: T
}

export type Status = 'pending' | 'active' | 'completed'
```

```vue
<script setup lang="ts">
import type { User, Status } from '@/types/user'

// WORKS: Simple imported interface
defineProps<{
  user: User
}>()

// WORKS: Imported union type
defineProps<{
  status: Status
}>()

// WORKS: Direct imported interface
defineProps<User>()
</script>
```

## Unsupported Patterns

### Conditional Types for Entire Props Object

```typescript
// types/conditional.ts
export type ConditionalProps<T> = T extends string
  ? { value: string; onChange: (v: string) => void }
  : { value: number; onChange: (v: number) => void }
```

```vue
<script setup lang="ts">
import type { ConditionalProps } from '@/types/conditional'

// ERROR: Conditional types not supported for entire props object
defineProps<ConditionalProps<string>>()
</script>
```

**Workaround:**
```vue
<script setup lang="ts">
// Define the resolved type directly
interface StringProps {
  value: string
  onChange: (v: string) => void
}

defineProps<StringProps>()
</script>
```

### Conditional Types for Individual Props ARE Supported

```vue
<script setup lang="ts">
// This WORKS - conditional type on individual prop
interface Props {
  value: SomeType extends string ? string : number  // OK
}

defineProps<Props>()
</script>
```

### Global Ambient Types

```typescript
// global.d.ts (ambient declaration without export)
interface GlobalUser {
  id: string
  name: string
}

// No export statement - this is an ambient declaration
```

```vue
<script setup lang="ts">
// ERROR: "Unresolvable type reference"
defineProps<{
  user: GlobalUser  // Can't resolve ambient global type
}>()
</script>
```

**Workaround:**
```typescript
// types/user.ts - Use explicit export
export interface GlobalUser {
  id: string
  name: string
}
```

```vue
<script setup lang="ts">
import type { GlobalUser } from '@/types/user'

// WORKS: Explicitly imported
defineProps<{
  user: GlobalUser
}>()
</script>
```

### Complex Mapped Types

```typescript
// types/complex.ts
export type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P]
}

export interface User {
  id: string
  profile: { name: string }
}
```

```vue
<script setup lang="ts">
import type { DeepReadonly, User } from '@/types/complex'

// May fail or produce incorrect types
defineProps<{
  user: DeepReadonly<User>
}>()
</script>
```

**Workaround:**
```typescript
// Resolve the type explicitly
export interface ReadonlyUser {
  readonly id: string
  readonly profile: { readonly name: string }
}
```

### Union of Imported Interfaces

```typescript
// types/forms.ts
export interface TextInput { type: 'text'; value: string }
export interface NumberInput { type: 'number'; value: number }
```

```vue
<script setup lang="ts">
import type { TextInput, NumberInput } from '@/types/forms'

// Can cause issues in some Vue versions
defineProps<{
  input: TextInput | NumberInput
}>()
</script>
```

**Workaround:**
```typescript
// Define the union in the types file
export type AnyInput = TextInput | NumberInput
```

```vue
<script setup lang="ts">
import type { AnyInput } from '@/types/forms'

defineProps<{
  input: AnyInput
}>()
</script>
```

## Best Practices

### Keep Props Types Simple

```typescript
// GOOD: Simple, explicit interface
export interface ButtonProps {
  variant: 'primary' | 'secondary' | 'danger'
  size: 'sm' | 'md' | 'lg'
  disabled?: boolean
  loading?: boolean
}

// AVOID: Over-engineered generic types
export type ButtonProps<V extends string, S extends string> = {
  variant: V
  size: S
  // ...complex type gymnastics
}
```

### Resolve Types Before Export

```typescript
// Instead of exporting generic utilities
// export type PartialBy<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>

// Export the resolved type
export interface CreateUserProps {
  name: string
  email: string
  age?: number  // Made optional
  role?: 'admin' | 'user'  // Made optional
}
```

### Use Dual Script Blocks for Complex Cases

```vue
<script lang="ts">
// Regular script block for complex type definitions
import type { ComplexType } from '@/types'

// Resolve the type here
type ResolvedProps = ComplexType extends SomeCondition
  ? { a: string }
  : { b: number }
</script>

<script setup lang="ts">
// Use the resolved type
defineProps<ResolvedProps>()
</script>
```

## Version-Specific Behavior

| Vue Version | Imported Types | Complex Types |
|-------------|---------------|---------------|
| 3.2 | Not supported | Not supported |
| 3.3 | Supported | Limited |
| 3.4+ | Supported | Better support |

Always check the Vue changelog for updates to type support in defineProps.

## Reference
- [Vue.js TypeScript with Composition API](https://vuejs.org/guide/typescript/composition-api.html)
- [GitHub Issue: defineProps with imported interfaces](https://github.com/vuejs/core/issues/8612)
- [GitHub Issue: Union types in defineProps](https://github.com/vuejs/core/issues/5804)
```

## File: `skills/vue-debug-guides/reference/ts-event-handler-explicit-typing.md`
```markdown
---
title: Always Explicitly Type Event Handlers
impact: MEDIUM
impactDescription: Without explicit typing, event parameters have implicit 'any' type causing TypeScript errors in strict mode
type: gotcha
tags: [vue3, typescript, events, dom-events, composition-api]
---

# Always Explicitly Type Event Handlers

**Impact: MEDIUM** - Native DOM event handlers in Vue components have implicit `any` type for the `event` parameter. In TypeScript strict mode, this causes errors. You must explicitly type event parameters and use type assertions for `event.target`.

## Task Checklist

- [ ] Always type the `event` parameter explicitly (e.g., `Event`, `MouseEvent`)
- [ ] Use type assertions when accessing element-specific properties
- [ ] Consider using inline handlers for simple cases
- [ ] Be aware of Vue's synthetic event system

## The Problem

```vue
<script setup lang="ts">
// WRONG: event has implicit 'any' type
function handleChange(event) {  // Error in strict mode!
  console.log(event.target.value)  // Also error: target might be null
}

// WRONG: Missing type assertion for element access
function handleInput(event: Event) {
  console.log(event.target.value)  // Error: 'value' doesn't exist on EventTarget
}
</script>

<template>
  <input @change="handleChange" @input="handleInput" />
</template>
```

## The Solution

```vue
<script setup lang="ts">
// CORRECT: Explicit Event type + type assertion
function handleChange(event: Event) {
  const target = event.target as HTMLInputElement
  console.log(target.value)
}

// CORRECT: Specific event type when needed
function handleClick(event: MouseEvent) {
  console.log(event.clientX, event.clientY)
}

function handleKeydown(event: KeyboardEvent) {
  if (event.key === 'Enter') {
    submitForm()
  }
}

function handleSubmit(event: SubmitEvent) {
  event.preventDefault()
  const formData = new FormData(event.target as HTMLFormElement)
}
</script>

<template>
  <input @change="handleChange" />
  <button @click="handleClick">Click</button>
  <input @keydown="handleKeydown" />
  <form @submit="handleSubmit">...</form>
</template>
```

## Common Event Types

| Event | Type | Common Properties |
|-------|------|-------------------|
| click, dblclick | `MouseEvent` | clientX, clientY, button |
| keydown, keyup, keypress | `KeyboardEvent` | key, code, ctrlKey, shiftKey |
| input, change | `Event` | target (needs assertion) |
| focus, blur | `FocusEvent` | relatedTarget |
| submit | `SubmitEvent` | submitter |
| drag, dragstart, drop | `DragEvent` | dataTransfer |
| wheel, scroll | `WheelEvent` | deltaX, deltaY |
| touch events | `TouchEvent` | touches, changedTouches |

## Element-Specific Type Assertions

```vue
<script setup lang="ts">
// HTMLInputElement for text, number, checkbox, radio inputs
function handleTextInput(event: Event) {
  const input = event.target as HTMLInputElement
  console.log(input.value, input.checked)
}

// HTMLSelectElement for select dropdowns
function handleSelect(event: Event) {
  const select = event.target as HTMLSelectElement
  console.log(select.value, select.selectedIndex)
}

// HTMLTextAreaElement for textareas
function handleTextarea(event: Event) {
  const textarea = event.target as HTMLTextAreaElement
  console.log(textarea.value, textarea.selectionStart)
}

// HTMLFormElement for forms
function handleFormSubmit(event: SubmitEvent) {
  event.preventDefault()
  const form = event.target as HTMLFormElement
  const formData = new FormData(form)
}
</script>
```

## Inline Event Handler Pattern

For simple cases, inline handlers with type annotations work well:

```vue
<template>
  <!-- Inline with type assertion -->
  <input
    @input="(event: Event) => {
      const input = event.target as HTMLInputElement
      searchQuery = input.value
    }"
  />

  <!-- Or with $event cast -->
  <input @input="searchQuery = ($event.target as HTMLInputElement).value" />
</template>
```

## Generic Handler Pattern

Create reusable typed handlers:

```typescript
// utils/events.ts
export function getInputValue(event: Event): string {
  return (event.target as HTMLInputElement).value
}

export function getSelectValue(event: Event): string {
  return (event.target as HTMLSelectElement).value
}

export function getCheckboxChecked(event: Event): boolean {
  return (event.target as HTMLInputElement).checked
}
```

```vue
<script setup lang="ts">
import { getInputValue, getCheckboxChecked } from '@/utils/events'

const name = ref('')
const agreed = ref(false)
</script>

<template>
  <input @input="e => name = getInputValue(e)" />
  <input type="checkbox" @change="e => agreed = getCheckboxChecked(e)" />
</template>
```

## Vue Component Events

For Vue component events (not DOM events), use `defineEmits` for type safety:

```vue
<script setup lang="ts">
const emit = defineEmits<{
  'custom-event': [data: { id: number; name: string }]
}>()

// Handler for child component event
function handleChildEvent(data: { id: number; name: string }) {
  console.log(data.id, data.name)
}
</script>

<template>
  <!-- Custom component event - properly typed -->
  <ChildComponent @custom-event="handleChildEvent" />
</template>
```

## Avoiding currentTarget vs target Confusion

```typescript
function handleClick(event: MouseEvent) {
  // target: The element that triggered the event (could be a child)
  const target = event.target as HTMLElement

  // currentTarget: The element the listener is attached to
  const currentTarget = event.currentTarget as HTMLButtonElement

  // Be explicit about which you need
  if (target.tagName === 'SPAN') {
    // Clicked on span inside button
  }
}
```

## Reference
- [Vue.js TypeScript with Composition API - Event Handlers](https://vuejs.org/guide/typescript/composition-api.html#typing-event-handlers)
- [MDN Event Reference](https://developer.mozilla.org/en-US/docs/Web/Events)
- [TypeScript DOM Types](https://github.com/microsoft/TypeScript/blob/main/lib/lib.dom.d.ts)
```

## File: `skills/vue-debug-guides/reference/ts-reactive-no-generic-argument.md`
```markdown
---
title: Do Not Use Generic Argument with reactive()
impact: MEDIUM
impactDescription: The generic argument type differs from the actual return type due to ref unwrapping, causing type mismatches
type: gotcha
tags: [vue3, typescript, reactive, ref-unwrapping, composition-api]
---

# Do Not Use Generic Argument with reactive()

**Impact: MEDIUM** - It is NOT recommended to use the generic argument of `reactive()` because the returned type, which handles nested ref unwrapping, is different from the generic argument type. Use interface annotation on the variable instead.

## Task Checklist

- [ ] Use type annotation on the variable, not generic argument
- [ ] Understand that `reactive()` unwraps nested refs
- [ ] For generic composables, use `shallowRef` or explicit `Ref<T>` typing
- [ ] Prefer `ref()` for simple values to avoid these issues

## The Problem

```vue
<script setup lang="ts">
import { reactive, ref } from 'vue'

interface Book {
  title: string
  year: number
  author: Ref<string>  // Nested ref
}

// WRONG: Generic argument doesn't account for ref unwrapping
const book = reactive<Book>({
  title: 'Vue 3 Guide',
  year: 2024,
  author: ref('John Doe')
})

// TypeScript thinks book.author is Ref<string>
// But at runtime, it's unwrapped to just string!
book.author.value  // TypeScript: OK, Runtime: ERROR (author is a string, not a ref)
</script>
```

## The Solution: Interface Annotation

```vue
<script setup lang="ts">
import { reactive, ref } from 'vue'

interface Book {
  title: string
  year?: number
}

// CORRECT: Annotate the variable, not the generic
const book: Book = reactive({
  title: 'Vue 3 Guide'
})

book.title = 'New Title'  // TypeScript knows this is string
book.year = 2024         // TypeScript knows this is number | undefined
</script>
```

## Why This Happens

When you use `reactive()`, Vue automatically unwraps any nested refs:

```typescript
import { reactive, ref, Ref } from 'vue'

const name = ref('John')
const state = reactive({
  name: name  // This is a Ref<string>
})

// At runtime, state.name is 'John' (string), NOT a Ref
console.log(state.name)       // 'John' (not ref object)
console.log(state.name.value) // Runtime error: .value doesn't exist

// The ACTUAL return type is different from what you'd expect
// reactive<{ name: Ref<string> }>() does NOT return { name: Ref<string> }
// It returns { name: string } due to automatic unwrapping
```

## Correct Patterns

### Pattern 1: Simple Interface Annotation

```vue
<script setup lang="ts">
interface FormState {
  name: string
  email: string
  age: number
}

const form: FormState = reactive({
  name: '',
  email: '',
  age: 0
})
</script>
```

### Pattern 2: Partial for Optional Fields

```vue
<script setup lang="ts">
interface User {
  id: string
  name: string
  email: string
}

// Start with partial data
const user: Partial<User> = reactive({})

// Fill in later
user.id = '123'
user.name = 'John'
</script>
```

### Pattern 3: Use ref() Instead

For simpler cases, prefer `ref()` which has more predictable typing:

```vue
<script setup lang="ts">
interface User {
  id: string
  name: string
}

// ref() works well with generics
const user = ref<User>({
  id: '1',
  name: 'John'
})

// Access with .value - clear and predictable
user.value.name = 'Jane'
</script>
```

## Generic Composables: Use Ref<T> or shallowRef

When working with generic type parameters in composables:

```typescript
// PROBLEM: Generic T with ref() causes UnwrapRef issues
function useBroken<T>(initial: T) {
  const state = ref(initial)  // Type becomes Ref<UnwrapRef<T>>
  state.value = initial       // Error: T is not assignable to UnwrapRef<T>
  return state
}

// SOLUTION 1: Use explicit Ref<T> type
function useFixed1<T>(initial: T) {
  const state: Ref<T> = ref(initial) as Ref<T>
  return state
}

// SOLUTION 2: Use shallowRef (no unwrapping)
function useFixed2<T>(initial: T) {
  const state = shallowRef(initial)  // Properly typed as ShallowRef<T>
  return state
}
```

## When Generic Argument IS Safe

For simple non-ref values without nested reactivity, the generic is safe:

```typescript
// Safe: no nested refs
const state = reactive<{ count: number; name: string }>({
  count: 0,
  name: ''
})

// Also safe: explicit simple types
const list = reactive<string[]>([])
const map = reactive<Map<string, number>>(new Map())
```

The issue only arises when:
1. You have nested Ref types in your interface
2. You're using generic type parameters that might contain refs

## Reference
- [Vue.js TypeScript with Composition API - Typing reactive()](https://vuejs.org/guide/typescript/composition-api.html#typing-reactive)
- [GitHub Issue: ref with generic type](https://github.com/vuejs/core/discussions/9564)
- [Vue TypeScript Caveats Gist](https://gist.github.com/LinusBorg/e041ff635994b50b7cec9383c3a067f1)
```

## File: `skills/vue-debug-guides/reference/ts-shallowref-for-dynamic-components.md`
```markdown
---
title: Use shallowRef for Dynamic Component References
impact: MEDIUM
impactDescription: Storing components in reactive() or ref() triggers Vue warnings and can cause performance issues
type: gotcha
tags: [typescript, shallowRef, dynamic-components, reactivity, performance]
---

# Use shallowRef for Dynamic Component References

**Impact: MEDIUM** - When storing Vue components in reactive state for dynamic rendering, using `ref()` or `reactive()` causes Vue warnings and unnecessary reactivity overhead. Use `shallowRef()` instead.

## Task Checklist

- [ ] Use `shallowRef` for storing component references
- [ ] Use `markRaw` when storing components in reactive objects
- [ ] Avoid wrapping component definitions with deep reactivity
- [ ] Check console for "[Vue warn]: Vue received a Component that was made a reactive object"

## The Problem

Vue components are objects with internal properties that should not be made reactive. When you store a component in `ref()` or `reactive()`, Vue traverses all properties deeply, which:

1. Triggers a console warning
2. Creates unnecessary reactive proxies
3. Can cause subtle bugs with component identity
4. Impacts performance

**Incorrect - Using ref() for components:**
```typescript
import { ref } from 'vue'
import ComponentA from './ComponentA.vue'
import ComponentB from './ComponentB.vue'

// BAD: Vue will warn about making component reactive
const currentComponent = ref(ComponentA)

function switchComponent() {
  currentComponent.value = ComponentB
}
```

**Console warning:**
```
[Vue warn]: Vue received a Component that was made a reactive object.
This can lead to unnecessary performance overhead and should be avoided
by marking the component with `markRaw` or using `shallowRef` instead of `ref`.
```

## Solution 1: Use shallowRef

`shallowRef` only makes the `.value` reference reactive, not the contents:

```typescript
import { shallowRef, type Component } from 'vue'
import ComponentA from './ComponentA.vue'
import ComponentB from './ComponentB.vue'

// CORRECT: shallowRef doesn't deep-proxy the component
const currentComponent = shallowRef<Component>(ComponentA)

function switchComponent() {
  currentComponent.value = ComponentB
}
```

```vue
<template>
  <component :is="currentComponent" />
</template>
```

## Solution 2: Use markRaw in Reactive Objects

When components are part of a larger reactive object:

```typescript
import { reactive, markRaw, type Component } from 'vue'
import TabHome from './TabHome.vue'
import TabProfile from './TabProfile.vue'
import TabSettings from './TabSettings.vue'

interface Tab {
  name: string
  component: Component
}

// CORRECT: markRaw prevents reactivity on component objects
const tabs = reactive<Tab[]>([
  { name: 'Home', component: markRaw(TabHome) },
  { name: 'Profile', component: markRaw(TabProfile) },
  { name: 'Settings', component: markRaw(TabSettings) }
])

const activeTab = shallowRef<Tab>(tabs[0])
```

```vue
<template>
  <div class="tabs">
    <button
      v-for="tab in tabs"
      :key="tab.name"
      @click="activeTab = tab"
    >
      {{ tab.name }}
    </button>
  </div>
  <component :is="activeTab.component" />
</template>
```

## TypeScript Typing

For proper TypeScript support with dynamic components:

```typescript
import { shallowRef, type Component, type DefineComponent } from 'vue'

// Generic component type
const currentComponent = shallowRef<Component | null>(null)

// Or more specific with props
interface MyComponentProps {
  title: string
}

const currentComponent = shallowRef<DefineComponent<MyComponentProps> | null>(null)
```

## Dynamic Import with shallowRef

When using dynamic imports for code splitting:

```typescript
import { shallowRef, defineAsyncComponent, type Component } from 'vue'

const currentComponent = shallowRef<Component | null>(null)

async function loadComponent(name: string) {
  const component = defineAsyncComponent(
    () => import(`./components/${name}.vue`)
  )
  currentComponent.value = component
}
```

## Component Registry Pattern

For tab systems or wizard-like interfaces:

```typescript
import { shallowRef, markRaw, type Component } from 'vue'

// Type-safe component registry
const componentRegistry = {
  home: markRaw(defineAsyncComponent(() => import('./Home.vue'))),
  about: markRaw(defineAsyncComponent(() => import('./About.vue'))),
  contact: markRaw(defineAsyncComponent(() => import('./Contact.vue')))
} as const

type ComponentKey = keyof typeof componentRegistry

const currentView = shallowRef<ComponentKey>('home')

// Computed to get current component
const currentComponent = computed(() => componentRegistry[currentView.value])
```

```vue
<template>
  <component :is="currentComponent" />
</template>
```

## When to Use Each Approach

| Scenario | Solution |
|----------|----------|
| Single dynamic component reference | `shallowRef` |
| Component in reactive array/object | `markRaw` on component |
| Component map/registry | `markRaw` each component |
| Async components | `defineAsyncComponent` + `shallowRef` |

## Common Mistakes

### Mistake 1: Using computed with ref

```typescript
// BAD: Still triggers warning
const components = ref([ComponentA, ComponentB])
const current = computed(() => components.value[index.value])

// GOOD: Use shallowRef for the array
const components = shallowRef([ComponentA, ComponentB])
```

### Mistake 2: Forgetting markRaw in map

```typescript
// BAD: Components in map become reactive
const routes = reactive(new Map([
  ['home', HomeComponent],
  ['about', AboutComponent]
]))

// GOOD: Mark each component as raw
const routes = reactive(new Map([
  ['home', markRaw(HomeComponent)],
  ['about', markRaw(AboutComponent)]
]))
```

## Reference

- [Vue.js Reactivity in Depth - Reducing Reactivity Overhead](https://vuejs.org/guide/extras/reactivity-in-depth.html#reducing-reactivity-overhead-for-large-immutable-structures)
- [Vue.js API - shallowRef](https://vuejs.org/api/reactivity-advanced.html#shallowref)
- [Vue.js API - markRaw](https://vuejs.org/api/reactivity-advanced.html#markraw)
```

## File: `skills/vue-debug-guides/reference/ts-template-ref-null-handling.md`
```markdown
---
title: Template Refs Are Null Until Mounted
impact: HIGH
impactDescription: Accessing template ref before mount or after unmount causes runtime errors
type: gotcha
tags: [vue3, typescript, template-refs, lifecycle, null-safety]
---

# Template Refs Are Null Until Mounted

**Impact: HIGH** - Template refs have an initial value of `null` and remain null until the component mounts. They can also become null again if the referenced element is removed by `v-if`. Always account for this in TypeScript with union types and optional chaining.

## Task Checklist

- [ ] Always type template refs with `| null` union
- [ ] Only access refs inside `onMounted` or after
- [ ] Use optional chaining (`?.`) when accessing ref properties
- [ ] Handle `v-if` scenarios where ref can become null again
- [ ] Consider using `useTemplateRef` in Vue 3.5+

## The Problem

```vue
<script setup lang="ts">
import { ref } from 'vue'

// WRONG: Doesn't account for null
const inputRef = ref<HTMLInputElement>()

// WRONG: Will crash if accessed before mount
inputRef.value.focus()  // Error: Cannot read properties of null

// WRONG: Accessed in setup, element doesn't exist yet
console.log(inputRef.value.value)  // Error!
</script>

<template>
  <input ref="inputRef" />
</template>
```

## The Solution

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

// CORRECT: Include null in the type
const inputRef = ref<HTMLInputElement | null>(null)

// CORRECT: Access in onMounted when DOM exists
onMounted(() => {
  inputRef.value?.focus()  // Safe with optional chaining
})

// CORRECT: Guard before accessing
function focusInput() {
  if (inputRef.value) {
    inputRef.value.focus()
  }
}
</script>

<template>
  <input ref="inputRef" />
</template>
```

## Vue 3.5+: useTemplateRef

Vue 3.5 introduces `useTemplateRef` with better type inference:

```vue
<script setup lang="ts">
import { useTemplateRef, onMounted } from 'vue'

// Type is automatically inferred for static refs
const inputRef = useTemplateRef<HTMLInputElement>('input')

onMounted(() => {
  inputRef.value?.focus()
})
</script>

<template>
  <input ref="input" />
</template>
```

## Handling v-if Scenarios

Refs can become `null` when elements are conditionally rendered:

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'

const showModal = ref(false)
const modalRef = ref<HTMLDivElement | null>(null)

// WRONG: Assuming ref always exists after first mount
function closeModal() {
  modalRef.value.classList.remove('open')  // May be null!
}

// CORRECT: Always guard access
function closeModal() {
  modalRef.value?.classList.remove('open')
}

// CORRECT: Watch for ref changes
watch(modalRef, (newRef) => {
  if (newRef) {
    // Modal element just mounted
    newRef.focus()
  }
  // If null, modal was unmounted
})
</script>

<template>
  <div v-if="showModal" ref="modalRef" class="modal">
    Modal content
  </div>
</template>
```

## Component Refs

For component refs, use `InstanceType`:

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import ChildComponent from './ChildComponent.vue'

// Component ref with null
const childRef = ref<InstanceType<typeof ChildComponent> | null>(null)

onMounted(() => {
  // Access exposed methods/properties
  childRef.value?.exposedMethod()
})
</script>

<template>
  <ChildComponent ref="childRef" />
</template>
```

Remember: Child components must use `defineExpose` to expose methods:

```vue
<!-- ChildComponent.vue -->
<script setup lang="ts">
function exposedMethod() {
  console.log('Called from parent')
}

defineExpose({
  exposedMethod
})
</script>
```

## Multiple Refs with v-for

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

const items = ref(['a', 'b', 'c'])

// Array of refs for v-for
const itemRefs = ref<(HTMLLIElement | null)[]>([])

onMounted(() => {
  // Access specific item
  itemRefs.value[0]?.focus()

  // Iterate safely
  itemRefs.value.forEach(el => {
    el?.classList.add('mounted')
  })
})
</script>

<template>
  <ul>
    <li
      v-for="(item, index) in items"
      :key="item"
      :ref="el => { itemRefs[index] = el as HTMLLIElement }"
    >
      {{ item }}
    </li>
  </ul>
</template>
```

## Async Operations and Refs

Be careful with async operations:

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

const containerRef = ref<HTMLDivElement | null>(null)

onMounted(async () => {
  // containerRef.value exists here

  await fetchData()

  // CAREFUL: Component might have unmounted during await
  // Always re-check before accessing
  if (containerRef.value) {
    containerRef.value.scrollTop = 0
  }
})
</script>
```

## Type Guard Pattern

Create a reusable type guard for cleaner code:

```typescript
// utils/refs.ts
export function assertRef<T>(
  ref: Ref<T | null>,
  message = 'Ref is not available'
): asserts ref is Ref<T> {
  if (ref.value === null) {
    throw new Error(message)
  }
}

// Usage in component
function mustFocus() {
  assertRef(inputRef, 'Input element not mounted')
  inputRef.value.focus()  // TypeScript knows it's not null here
}
```

## Reference
- [Vue.js TypeScript with Composition API - Template Refs](https://vuejs.org/guide/typescript/composition-api.html#typing-template-refs)
- [Vue.js Template Refs](https://vuejs.org/guide/essentials/template-refs.html)
```

## File: `skills/vue-debug-guides/reference/ts-template-type-casting.md`
```markdown
---
title: Use Type Casting in Templates for Union Types
impact: MEDIUM
impactDescription: Template expressions with union types cause TypeScript errors even when the runtime type is known
type: gotcha
tags: [typescript, templates, type-casting, union-types, script-setup]
---

# Use Type Casting in Templates for Union Types

**Impact: MEDIUM** - When using `lang="ts"` in Vue Single File Components, template expressions get strict type checking. If a variable has a union type, you may need inline type casting to access type-specific methods or properties.

## Task Checklist

- [ ] Use `(value as Type)` syntax for type casting in templates
- [ ] Consider narrowing types in script before using in template
- [ ] Remember template type checking requires `lang="ts"` attribute
- [ ] For Vue CLI/webpack: ensure vue-loader >= 16.8.0

## The Problem

When a variable has a union type, TypeScript cannot know which specific type it is at template compile time:

**Template with type error:**
```vue
<script setup lang="ts">
// Union type: could be string OR number
let x: string | number = 1
</script>

<template>
  <!-- ERROR: Property 'toFixed' does not exist on type 'string | number' -->
  {{ x.toFixed(2) }}
</template>
```

TypeScript correctly identifies that `toFixed()` only exists on `number`, not `string`.

## Solution 1: Inline Type Casting

Use `(value as Type)` syntax directly in the template:

```vue
<script setup lang="ts">
let x: string | number = 1
</script>

<template>
  <!-- CORRECT: Cast to number to access toFixed -->
  {{ (x as number).toFixed(2) }}
</template>
```

## Solution 2: Computed Property (Preferred)

Create a computed property that narrows or transforms the type:

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

const value = ref<string | number>(1)

const formattedValue = computed(() => {
  if (typeof value.value === 'number') {
    return value.value.toFixed(2)
  }
  return value.value
})
</script>

<template>
  <!-- Clean template, type-safe logic in script -->
  {{ formattedValue }}
</template>
```

## Solution 3: Type Guard Function

Define a type guard and use it in the template:

```vue
<script setup lang="ts">
import { ref } from 'vue'

const data = ref<string | number | null>(null)

function isNumber(val: unknown): val is number {
  return typeof val === 'number'
}

function formatNumber(val: number): string {
  return val.toFixed(2)
}
</script>

<template>
  <div v-if="isNumber(data)">
    {{ formatNumber(data) }}
  </div>
  <div v-else-if="data !== null">
    {{ data }}
  </div>
</template>
```

## Common Use Cases

### API Response Data

```vue
<script setup lang="ts">
interface ApiResponse {
  status: 'success' | 'error'
  data?: UserData
  error?: string
}

const response = ref<ApiResponse | null>(null)
</script>

<template>
  <div v-if="response?.status === 'success'">
    <!-- Cast to access data safely -->
    {{ (response as { data: UserData }).data.name }}
  </div>
</template>
```

**Better approach with computed:**
```vue
<script setup lang="ts">
const userData = computed(() => {
  if (response.value?.status === 'success') {
    return response.value.data
  }
  return null
})
</script>

<template>
  <div v-if="userData">
    {{ userData.name }}
  </div>
</template>
```

### Event Handlers with Event Types

```vue
<script setup lang="ts">
function handleInput(event: Event) {
  // Cast to HTMLInputElement to access 'value'
  const value = (event.target as HTMLInputElement).value
  console.log(value)
}
</script>

<template>
  <input @input="handleInput" />
</template>
```

### Array Item Access

```vue
<script setup lang="ts">
const items = ref<(string | number)[]>([1, 'two', 3])
</script>

<template>
  <ul>
    <li v-for="item in items" :key="item">
      <!-- Cast when you know the type -->
      <span v-if="typeof item === 'number'">
        Number: {{ (item as number).toFixed(1) }}
      </span>
      <span v-else>
        String: {{ (item as string).toUpperCase() }}
      </span>
    </li>
  </ul>
</template>
```

## When Type Casting is Needed

| Scenario | Solution |
|----------|----------|
| Union types | Cast to specific type |
| Nullable types | Use optional chaining or cast after null check |
| Event targets | Cast `event.target` to specific element type |
| Array methods | Cast when TS can't narrow array item types |

## Important Notes

### Template Type Checking Requirements

Template type checking is enabled when:
1. `<script lang="ts">` or `<script setup lang="ts">` is used
2. Vue Language Server (Volar) is active in your IDE
3. For webpack: vue-loader >= 16.8.0 is required

### Avoid Excessive Casting

If you find yourself casting frequently in templates, consider:
- Moving logic to computed properties
- Using type guards in the script section
- Refactoring data structures to be more specific

## Reference

- [Vue.js TypeScript Overview - TypeScript in Templates](https://vuejs.org/guide/typescript/overview.html#typescript-in-templates)
- [Vue.js TypeScript with Composition API](https://vuejs.org/guide/typescript/composition-api.html)
```

## File: `skills/vue-debug-guides/reference/ts-withdefaults-mutable-factory-function.md`
```markdown
---
title: Wrap Mutable Default Values in Factory Functions
impact: HIGH
impactDescription: Without factory functions, all component instances share the same mutable reference causing cross-contamination bugs
type: gotcha
tags: [vue3, typescript, props, withDefaults, mutable-types]
---

# Wrap Mutable Default Values in Factory Functions

**Impact: HIGH** - When using `withDefaults()` with type-based props declaration, default values for mutable types (arrays and objects) MUST be wrapped in factory functions. Without this, all component instances share the same reference, causing bugs where modifying the prop in one instance affects all others.

## Task Checklist

- [ ] Always wrap array defaults in factory functions: `() => []`
- [ ] Always wrap object defaults in factory functions: `() => ({})`
- [ ] Primitive types (string, number, boolean) do NOT need factory functions
- [ ] Review existing components for this pattern

## The Problem: Shared Mutable References

**WRONG - Shared reference across instances:**
```vue
<script setup lang="ts">
interface Props {
  items?: string[]
  config?: { theme: string }
}

const props = withDefaults(defineProps<Props>(), {
  items: ['default'],           // WRONG! All instances share this array
  config: { theme: 'light' }    // WRONG! All instances share this object
})
</script>
```

When you have multiple instances of this component:
```vue
<template>
  <!-- Both share the SAME items array! -->
  <MyComponent ref="comp1" />
  <MyComponent ref="comp2" />
</template>

<script setup>
// If comp1 modifies its items, comp2's items change too!
comp1.value.items.push('new item')  // comp2 also has 'new item' now
</script>
```

## The Solution: Factory Functions

**CORRECT - Unique instance per component:**
```vue
<script setup lang="ts">
interface Props {
  items?: string[]
  config?: { theme: string }
  nested?: { data: { values: number[] } }
}

const props = withDefaults(defineProps<Props>(), {
  items: () => ['default'],                      // Factory function!
  config: () => ({ theme: 'light' }),            // Factory function!
  nested: () => ({ data: { values: [] } })       // Factory function!
})
</script>
```

## When Factory Functions Are Required

| Type | Factory Required | Example Default |
|------|-----------------|-----------------|
| `string` | No | `'hello'` |
| `number` | No | `42` |
| `boolean` | No | `false` |
| `string[]` | **Yes** | `() => []` |
| `number[]` | **Yes** | `() => [1, 2, 3]` |
| `object` | **Yes** | `() => ({})` |
| `Map` | **Yes** | `() => new Map()` |
| `Set` | **Yes** | `() => new Set()` |
| `Date` | **Yes** | `() => new Date()` |

## Complete Example

```vue
<script setup lang="ts">
interface User {
  id: string
  name: string
}

interface Props {
  // Primitives - no factory needed
  title?: string
  count?: number
  disabled?: boolean

  // Mutable types - factory required
  items?: string[]
  users?: User[]
  metadata?: Record<string, unknown>
  selectedIds?: Set<string>
}

const props = withDefaults(defineProps<Props>(), {
  // Primitives
  title: 'Default Title',
  count: 0,
  disabled: false,

  // Mutable types with factory functions
  items: () => [],
  users: () => [],
  metadata: () => ({}),
  selectedIds: () => new Set()
})
</script>
```

## Vue 3.5+ Reactive Props Destructure

Vue 3.5 introduces reactive props destructure, which handles this automatically:

```vue
<script setup lang="ts">
interface Props {
  items?: string[]
  config?: { theme: string }
}

// Vue 3.5+ - defaults work correctly without explicit factory functions
const {
  items = ['default'],        // Each instance gets its own array
  config = { theme: 'light' } // Each instance gets its own object
} = defineProps<Props>()
</script>
```

Note: Under the hood, Vue 3.5 handles the instance isolation for you.

## Common Bug Pattern

This bug often appears in list/table components:

```vue
<!-- ListItem.vue - BUGGY -->
<script setup lang="ts">
interface Props {
  selectedRows?: number[]
}

// All ListItems share the same selectedRows array!
const props = withDefaults(defineProps<Props>(), {
  selectedRows: []  // BUG: Missing factory function
})
</script>
```

Users report: "Selecting a row in one table selects it in all tables!"

**Fix:**
```typescript
const props = withDefaults(defineProps<Props>(), {
  selectedRows: () => []  // Now each instance has its own array
})
```

## Reference
- [Vue.js TypeScript with Composition API - Default Props](https://vuejs.org/guide/typescript/composition-api.html#props-default-values)
- [Vue RFC - Reactive Props Destructure](https://github.com/vuejs/rfcs/discussions/502)
```

## File: `skills/vue-debug-guides/reference/undeclared-emits-double-firing.md`
```markdown
---
title: Undeclared Emits Cause Double Event Firing
impact: HIGH
impactDescription: Native events re-emitted without declaration fire twice - once from emit() and once from native listener on root element
type: gotcha
tags: [vue3, emits, defineEmits, events, native-events, fallthrough]
---

# Undeclared Emits Cause Double Event Firing

**Impact: HIGH** - When a component re-emits a native DOM event (like `click`) without declaring it in `emits`, the event can fire twice. This happens because undeclared event listeners become part of `$attrs` and fall through to the root element, where they listen for native events while your `emit()` call also fires.

This is a common bug when wrapping native elements or migrating from Vue 2 to Vue 3.

## Task Checklist

- [ ] Declare all emitted events in `defineEmits()` or `emits` option
- [ ] Pay special attention when re-emitting native events (click, input, change, etc.)
- [ ] Check for double firing if component wraps native elements
- [ ] Understand that undeclared listeners fall through to `$attrs`

## The Problem

**Incorrect - Undeclared emit causes double firing:**
```vue
<!-- MyButton.vue -->
<script setup>
// NO defineEmits declaration!
</script>

<template>
  <!-- Native click listener from parent falls through to button -->
  <!-- PLUS we re-emit click -->
  <button @click="$emit('click', $event)">
    <slot></slot>
  </button>
</template>
```

```vue
<!-- Parent.vue -->
<template>
  <!-- This handler fires TWICE on each click! -->
  <MyButton @click="handleClick">Click me</MyButton>
</template>

<script setup>
function handleClick() {
  console.log('clicked') // Logs twice!
}
</script>
```

**What happens:**
1. User clicks the button
2. Native click event fires on the button element
3. `@click` falls through to button (because 'click' isn't in emits), triggering `handleClick`
4. The button's `@click="$emit('click', $event)"` also fires, emitting a component event
5. Parent's `@click="handleClick"` receives the emitted event, triggering `handleClick` again

## The Solution

**Correct - Declare the emit:**
```vue
<!-- MyButton.vue -->
<script setup>
// Declare 'click' as a component event
const emit = defineEmits(['click'])
</script>

<template>
  <!-- Now @click="handleClick" in parent only listens to emit() -->
  <button @click="emit('click', $event)">
    <slot></slot>
  </button>
</template>
```

```vue
<!-- Parent.vue -->
<template>
  <!-- Now fires only once -->
  <MyButton @click="handleClick">Click me</MyButton>
</template>
```

When you declare `click` in `emits`:
- Vue knows `@click` on the component is listening for a component event
- The listener does NOT fall through to the root element
- Only your explicit `emit('click')` triggers the parent's handler

## Options API Version

**Correct - Using emits option:**
```vue
<script>
export default {
  emits: ['click', 'input', 'change'],

  methods: {
    handleClick(event) {
      this.$emit('click', event)
    }
  }
}
</script>
```

## Common Scenarios

### Wrapping Form Inputs

```vue
<!-- CustomInput.vue -->
<script setup>
// Declare all events you re-emit
const emit = defineEmits(['input', 'change', 'focus', 'blur'])
</script>

<template>
  <input
    @input="emit('input', $event)"
    @change="emit('change', $event)"
    @focus="emit('focus', $event)"
    @blur="emit('blur', $event)"
  />
</template>
```

### Wrapper Components

```vue
<!-- IconButton.vue -->
<script setup>
const emit = defineEmits(['click'])
</script>

<template>
  <button @click="emit('click', $event)">
    <Icon :name="icon" />
    <slot></slot>
  </button>
</template>
```

## Alternative: Don't Re-emit, Let It Fall Through

If your component has a single root element and you want native event behavior:

```vue
<!-- MyButton.vue -->
<script setup>
// Don't declare 'click' - let it fall through naturally
const emit = defineEmits(['custom-action'])
</script>

<template>
  <!-- Native @click from parent falls through to this button -->
  <button>
    <slot></slot>
  </button>
</template>
```

```vue
<!-- Parent.vue -->
<template>
  <!-- This native click falls through to the button -->
  <MyButton @click="handleClick">Click me</MyButton>
</template>
```

This works because:
- You don't re-emit 'click' explicitly
- The native click listener falls through to the single root button
- Native click fires once when button is clicked

## Debugging Double Firing

```vue
<script setup>
function handleClick(event) {
  console.log('Event type:', event?.type)
  console.log('Is native:', event instanceof Event)
  console.trace('Click handler called')
}
</script>
```

If you see two stack traces with different origins, you have the double-firing issue.

## Reference
- [Vue 3 Migration - emits Option](https://v3-migration.vuejs.org/breaking-changes/emits-option)
- [Vue.js Component Events](https://vuejs.org/guide/components/events.html)
- [Vue.js Fallthrough Attributes](https://vuejs.org/guide/components/attrs.html)
```

## File: `skills/vue-debug-guides/reference/use-template-ref-vue35.md`
```markdown
---
title: Use useTemplateRef for Template Refs in Vue 3.5+
impact: MEDIUM
impactDescription: Legacy ref pattern is error-prone due to name matching requirement
type: best-practice
tags: [vue3, vue35, template-refs, useTemplateRef, composition-api]
---

# Use useTemplateRef for Template Refs in Vue 3.5+

**Impact: MEDIUM** - Before Vue 3.5, template refs required declaring a `ref()` with a name exactly matching the template's ref attribute. This fragile connection breaks silently during refactoring. Vue 3.5's `useTemplateRef()` eliminates this issue with explicit binding and better TypeScript support.

The legacy pattern causes no errors or warnings when names don't match - the ref simply stays null, leading to confusing debugging sessions.

## Task Checklist

- [ ] Use `useTemplateRef('ref-name')` in Vue 3.5+ projects
- [ ] The first argument must exactly match the ref attribute value in the template
- [ ] IDE support provides auto-completion for available ref names
- [ ] TypeScript automatically infers the element type

**Incorrect (Legacy Pattern):**
```vue
<script setup>
import { ref, onMounted } from 'vue'

// FRAGILE: Variable name MUST match template ref value exactly
const input = ref(null)

// DANGER: After refactoring, names may not match
const inputElement = ref(null) // Renamed variable...

onMounted(() => {
  // NO ERROR - just silently null!
  inputElement.value?.focus() // Does nothing
})
</script>

<template>
  <!-- But template still uses old name -->
  <input ref="input" />
</template>
```

```vue
<script setup>
import { ref } from 'vue'

// TYPO: 'inupt' instead of 'input' - no warning!
const inupt = ref(null)
</script>

<template>
  <input ref="input" />
  <!-- inupt.value will always be null -->
</template>
```

**Correct (Vue 3.5+):**
```vue
<script setup>
import { useTemplateRef, onMounted } from 'vue'

// CORRECT: Explicit binding - argument matches template ref
const inputElement = useTemplateRef('my-input')

onMounted(() => {
  inputElement.value?.focus()
})
</script>

<template>
  <!-- ref name is explicitly connected via useTemplateRef argument -->
  <input ref="my-input" />
</template>
```

```vue
<script setup>
import { useTemplateRef, onMounted } from 'vue'

// BENEFITS:
// 1. Variable name is independent of ref attribute
// 2. IDE auto-completes available ref names
// 3. TypeScript infers correct element type
// 4. Typos in argument cause visible errors

const searchInput = useTemplateRef('search-box')
const submitButton = useTemplateRef('submit-btn')

onMounted(() => {
  // TypeScript knows these are HTMLInputElement and HTMLButtonElement
  searchInput.value?.focus()
  submitButton.value?.disabled = false
})
</script>

<template>
  <input ref="search-box" type="search" />
  <button ref="submit-btn">Submit</button>
</template>
```

## Limitation: v-for Refs

`useTemplateRef()` does **NOT** work with `v-for` refs. You must use the legacy `ref()` pattern for collecting multiple element references in a loop.

```vue
<script setup>
import { ref, onMounted } from 'vue'

// CORRECT: Legacy pattern required for v-for refs
const itemRefs = ref([])

onMounted(() => {
  // itemRefs.value is an array of DOM elements
  itemRefs.value.forEach(el => {
    console.log(el.textContent)
  })
})
</script>

<template>
  <ul>
    <li v-for="item in items" ref="itemRefs" :key="item.id">
      {{ item.text }}
    </li>
  </ul>
</template>
```

**Why this limitation exists:** When using `v-for`, Vue populates the ref with an array of elements. The `useTemplateRef()` API was designed for single element references and does not support the array population mechanism that `v-for` requires.

## Migration Guide

```vue
<!-- BEFORE (Vue < 3.5) -->
<script setup>
import { ref } from 'vue'
const myElement = ref(null) // Name must match template
</script>
<template>
  <div ref="myElement"></div>
</template>

<!-- AFTER (Vue 3.5+) -->
<script setup>
import { useTemplateRef } from 'vue'
const element = useTemplateRef('my-element') // Any variable name
</script>
<template>
  <div ref="my-element"></div>
</template>
```

## Reference
- [Vue.js Template Refs - Composition API](https://vuejs.org/guide/essentials/template-refs.html#accessing-the-refs)
- [Vue 3.5 Release Notes](https://blog.vuejs.org/posts/vue-3-5)
```

## File: `skills/vue-debug-guides/reference/v-else-must-follow-v-if.md`
```markdown
---
title: v-else Must Immediately Follow v-if or v-else-if
impact: MEDIUM
impactDescription: Misplaced v-else causes a compile-time error in SFCs, or renders unconditionally with runtime template compilation
type: capability
tags: [vue3, conditional-rendering, v-if, v-else, v-else-if]
---

# v-else Must Immediately Follow v-if or v-else-if

**Impact: MEDIUM** - A `v-else` or `v-else-if` element must immediately follow a `v-if` or `v-else-if` element in the DOM. If there's any element in between:

- **SFC compilation (Vite/vue-loader):** Vue throws a **compile-time SyntaxError** - the code won't build at all
- **Runtime template compilation:** The element renders unconditionally (always visible), losing its conditional behavior

In most modern Vue projects using Single File Components, this is caught at build time.

## Task Checklist

- [ ] Place v-else immediately after the v-if element (no elements in between)
- [ ] Place v-else-if immediately after v-if or another v-else-if
- [ ] Use `<template>` wrapper if you need to group multiple elements within a branch
- [ ] If you need content between conditions, restructure using nested conditionals or computed

**Incorrect:**
```html
<!-- WRONG: v-else not immediately after v-if -->
<template>
  <div v-if="isLoggedIn">
    Welcome back!
  </div>

  <p>Some other content in between</p>

  <div v-else>
    <!-- This v-else is NOT recognized! It will ALWAYS render (unconditionally) -->
    Please log in
  </div>
</template>
```

```html
<!-- WRONG: Comment or whitespace element between -->
<template>
  <span v-if="status === 'loading'">Loading...</span>
  <!-- This comment breaks the chain! -->
  <span v-else-if="status === 'error'">Error occurred</span>
  <span v-else>Done</span>
</template>
```

```html
<!-- WRONG: Text node between conditions -->
<template>
  <div v-if="showA">A</div>
  Just some text here
  <div v-else>B</div>  <!-- Not recognized, always renders -->
</template>
```

**Correct:**
```html
<!-- CORRECT: v-else immediately follows v-if -->
<template>
  <div v-if="isLoggedIn">
    Welcome back!
  </div>
  <div v-else>
    Please log in
  </div>

  <p>Some other content (placed after the conditional block)</p>
</template>
```

```html
<!-- CORRECT: Full v-if/v-else-if/v-else chain -->
<template>
  <span v-if="status === 'loading'">Loading...</span>
  <span v-else-if="status === 'error'">Error: {{ errorMessage }}</span>
  <span v-else-if="status === 'empty'">No data found</span>
  <span v-else>{{ data }}</span>
</template>
```

```html
<!-- CORRECT: Using <template> for multiple elements per branch -->
<template>
  <template v-if="isLoggedIn">
    <h1>Welcome back!</h1>
    <p>Your dashboard</p>
    <UserStats />
  </template>
  <template v-else>
    <h1>Please log in</h1>
    <LoginForm />
  </template>
</template>
```

```html
<!-- CORRECT: Restructure if you need content between conditions -->
<template>
  <div class="conditional-section">
    <div v-if="isLoggedIn">Welcome back!</div>
    <div v-else>Please log in</div>
  </div>

  <div class="always-shown">
    Some other content
  </div>

  <div class="another-conditional">
    <div v-if="showMore">More info</div>
    <div v-else>Click to expand</div>
  </div>
</template>
```

## Debugging Tips

```html
<!-- If v-else is always visible (rendering unconditionally), check for: -->

<!-- 1. Elements between v-if and v-else -->
<!-- 2. HTML comments that break the chain -->
<!-- 3. Text nodes (including whitespace in some cases) -->
<!-- 4. Component tags that render content between -->

<!-- SFC compilation throws: "v-else/v-else-if has no adjacent v-if or v-else-if" (build fails) -->
<!-- Runtime template compilation shows a warning but renders the element unconditionally -->
<!-- Vue DevTools will show the v-else element as not part of the condition chain -->
```

## Reference
- [Vue.js Conditional Rendering - v-else](https://vuejs.org/guide/essentials/conditional.html#v-else)
```

## File: `skills/vue-debug-guides/reference/v-for-component-props.md`
```markdown
---
title: Always Pass v-for Data to Components via Props
impact: MEDIUM
impactDescription: Components have isolated scope - v-for iteration data is not automatically available inside child components
type: gotcha
tags: [vue3, v-for, components, props, list-rendering]
---

# Always Pass v-for Data to Components via Props

**Impact: MEDIUM** - Vue components have isolated scope by design. When using `v-for` to render components, the iteration variable (e.g., `item`) is NOT automatically available inside the child component. You must explicitly pass the data through props.

This isolation is intentional - it keeps components reusable and their data dependencies explicit. Forgetting to pass props results in `undefined` data or errors about missing properties.

## Task Checklist

- [ ] Always bind iteration data to component props explicitly
- [ ] Pass both the item and index if the component needs them
- [ ] Always include a unique `:key` when rendering components with v-for
- [ ] Define corresponding props in the child component to receive the data

**Incorrect:**
```html
<!-- WRONG: Component cannot access 'todo' - it's not in scope -->
<TodoItem v-for="todo in todos" :key="todo.id" />

<!-- Inside TodoItem.vue: this.todo or todo is undefined! -->
```

```html
<!-- WRONG: Key provided but no data passed -->
<UserCard
  v-for="user in users"
  :key="user.id"
/>
<!-- UserCard has no user data to display -->
```

**Correct:**
```html
<!-- CORRECT: Explicitly pass the item as a prop -->
<TodoItem
  v-for="todo in todos"
  :key="todo.id"
  :todo="todo"
/>
```

```html
<!-- CORRECT: Pass multiple pieces of data -->
<UserCard
  v-for="(user, index) in users"
  :key="user.id"
  :user="user"
  :index="index"
  :is-first="index === 0"
/>
```

```vue
<!-- Child component: UserCard.vue -->
<script setup>
defineProps({
  user: {
    type: Object,
    required: true
  },
  index: {
    type: Number,
    required: true
  },
  isFirst: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <div class="user-card">
    <span>{{ index + 1 }}. {{ user.name }}</span>
    <span v-if="isFirst">(First User)</span>
  </div>
</template>
```

## Why Explicit Props?

1. **Clear data flow**: Makes dependencies explicit and traceable
2. **Reusability**: Components work anywhere, not just inside specific v-for loops
3. **Type safety**: Props can be validated with type and required checks
4. **Maintainability**: Easier to understand what data a component needs

## Reference
- [Vue.js List Rendering - v-for with Components](https://vuejs.org/guide/essentials/list.html#v-for-with-a-component)
```

## File: `skills/vue-debug-guides/reference/v-for-computed-reverse-sort.md`
```markdown
---
title: Copy Arrays Before reverse() or sort() in Computed Properties
impact: MEDIUM
impactDescription: reverse() and sort() mutate the original array, causing unintended side effects in computed getters
type: gotcha
tags: [vue3, v-for, computed, array, mutation, list-rendering]
---

# Copy Arrays Before reverse() or sort() in Computed Properties

**Impact: MEDIUM** - The `reverse()` and `sort()` methods mutate the original array in-place. When used directly in a computed property getter, this causes the source array to be modified, leading to infinite reactivity loops or incorrect data state.

Computed properties should be pure - they calculate a value without side effects. Mutating the source data inside a computed getter violates this principle and causes unpredictable behavior.

## Task Checklist

- [ ] Always create a copy of the array before calling `reverse()` or `sort()` in computed properties
- [ ] Use spread operator `[...array]` or `Array.from(array)` or `array.slice()` to copy
- [ ] This applies to any in-place mutation method used in computed getters
- [ ] Consider using `toSorted()` and `toReversed()` (ES2023) which return new arrays

**Incorrect:**
```javascript
const numbers = ref([1, 2, 3, 4, 5])

// WRONG: Mutates the original array
const reversedNumbers = computed(() => {
  return numbers.value.reverse()  // Modifies numbers.value!
})

// WRONG: Same issue with sort
const sortedItems = computed(() => {
  return items.value.sort((a, b) => a.name.localeCompare(b.name))
})
```

**Correct:**
```javascript
const numbers = ref([1, 2, 3, 4, 5])

// CORRECT: Create a copy first with spread operator
const reversedNumbers = computed(() => {
  return [...numbers.value].reverse()
})

// CORRECT: Create a copy before sorting
const sortedItems = computed(() => {
  return [...items.value].sort((a, b) => a.name.localeCompare(b.name))
})

// CORRECT: Using slice() to copy
const reversedNumbers = computed(() => {
  return numbers.value.slice().reverse()
})

// CORRECT: ES2023 non-mutating methods (if supported)
const reversedNumbers = computed(() => {
  return numbers.value.toReversed()
})

const sortedItems = computed(() => {
  return items.value.toSorted((a, b) => a.price - b.price)
})
```

## Also Applies to Methods Used in Templates

When using methods to filter/sort in nested v-for loops, the same rule applies:

```javascript
// CORRECT: Method that doesn't mutate
function getSortedChildren(parent) {
  return [...parent.children].sort((a, b) => a.order - b.order)
}
```

```html
<ul v-for="parent in parents" :key="parent.id">
  <li v-for="child in getSortedChildren(parent)" :key="child.id">
    {{ child.name }}
  </li>
</ul>
```

## Reference
- [Vue.js List Rendering - Displaying Filtered/Sorted Results](https://vuejs.org/guide/essentials/list.html#displaying-filtered-sorted-results)
```

## File: `skills/vue-debug-guides/reference/v-for-key-attribute.md`
```markdown
---
title: Always Provide Unique Keys in v-for Loops
impact: HIGH
impactDescription: Missing or improper keys cause hard-to-debug bugs when list items have state, components, or animations
type: gotcha
tags: [vue3, v-for, list-rendering, key, state, components]
---

# Always Provide Unique Keys in v-for Loops

**Impact: HIGH** - Without proper keys, Vue cannot track element identity when lists change. This causes component state loss, incorrect animations, form input values jumping between items, and bugs that are extremely difficult to debug.

The `key` attribute tells Vue how your data relates to the DOM elements it renders. When data ordering changes (via sort, filter, add, or remove), Vue uses keys to determine what to update, remove, or create. Without unique keys, Vue reuses DOM elements in-place which can cause one item's state to incorrectly appear on another item.

## Task Checklist

- [ ] Always provide `:key` with unique, stable identifiers (database IDs, UUIDs)
- [ ] Never use array index as key - indices shift when items are added/removed
- [ ] Use primitive values only (strings or numbers) - never use objects as keys
- [ ] On `<template v-for>`, place the key on the `<template>` tag itself (Vue 3 change)
- [ ] When using components in v-for, keys are mandatory, not optional

**Incorrect:**
```html
<!-- WRONG: No key provided -->
<li v-for="item in items">{{ item.name }}</li>

<!-- WRONG: Using array index as key - shifts when list changes -->
<li v-for="(item, index) in items" :key="index">
  <input v-model="item.value" />
</li>

<!-- WRONG: Object as key -->
<li v-for="item in items" :key="item">{{ item.name }}</li>

<!-- WRONG (Vue 3): Key on child instead of template -->
<template v-for="item in items">
  <li :key="item.id">{{ item.name }}</li>
</template>
```

```javascript
// Bug demonstration: Using index as key
// Initial: ['Alice', 'Bob', 'Charlie'] at indices [0, 1, 2]
// After removing 'Bob': ['Alice', 'Charlie'] at indices [0, 1]
// Charlie now has index 1, so Vue reuses Bob's DOM/component state for Charlie!
```

**Correct:**
```html
<!-- CORRECT: Unique identifier as key -->
<li v-for="item in items" :key="item.id">
  {{ item.name }}
</li>

<!-- CORRECT: With components -->
<MyComponent
  v-for="item in items"
  :key="item.id"
  :item="item"
/>

<!-- CORRECT (Vue 3): Key on template tag -->
<template v-for="item in items" :key="item.id">
  <li>{{ item.name }}</li>
  <span>{{ item.description }}</span>
</template>

<!-- CORRECT: With stateful elements -->
<div v-for="user in users" :key="user.id">
  <input v-model="user.email" />
  <select v-model="user.role">
    <option value="admin">Admin</option>
    <option value="user">User</option>
  </select>
</div>
```

## When Keys Are Critical

Keys are absolutely required when v-for loops contain:
- Components with local state
- Form elements (`<input>`, `<select>`, `<textarea>`)
- Elements with initialization logic (mounted/created hooks)
- Animations or transitions
- Direct DOM manipulation

## Reference
- [Vue.js List Rendering - Key](https://vuejs.org/guide/essentials/list.html#maintaining-state-with-key)
- [Vue 3 Migration Guide - Key on Template](https://v3-migration.vuejs.org/breaking-changes/key-attribute)
```

## File: `skills/vue-debug-guides/reference/v-for-range-starts-at-one.md`
```markdown
---
title: v-for Range Iteration Starts at 1, Not 0
impact: LOW
impactDescription: v-for with a number range starts at 1, unlike JavaScript arrays which start at 0
type: gotcha
tags: [vue3, v-for, list-rendering, range]
---

# v-for Range Iteration Starts at 1, Not 0

**Impact: LOW** - When using `v-for` with a number (range iteration), the iteration starts at `1`, not `0`. This differs from typical JavaScript behavior where arrays are 0-indexed.

This gotcha commonly causes off-by-one errors when the generated numbers are used for calculations or array indexing.

## Task Checklist

- [ ] Remember `v-for="n in 10"` produces 1 through 10, not 0 through 9
- [ ] When using range values for array indexing, subtract 1: `items[n - 1]`
- [ ] Consider creating a computed array if you need 0-based indices

**Incorrect Assumption:**
```html
<!-- Developer expects 0-9, but gets 1-10 -->
<span v-for="n in 10">{{ n }}</span>
<!-- Output: 1 2 3 4 5 6 7 8 9 10 -->

<!-- WRONG: Off-by-one error when used for array access -->
<li v-for="n in items.length" :key="n">
  {{ items[n].name }}  <!-- Error! items[10] is undefined when length is 10 -->
</li>
```

**Correct:**
```html
<!-- Correct understanding: 1-based range -->
<span v-for="n in 10" :key="n">{{ n }}</span>
<!-- Output: 1 2 3 4 5 6 7 8 9 10 -->

<!-- CORRECT: Adjust index for array access -->
<li v-for="n in items.length" :key="n">
  {{ items[n - 1].name }}  <!-- n-1 converts to 0-based -->
</li>

<!-- BETTER: Just iterate the array directly -->
<li v-for="(item, index) in items" :key="item.id">
  {{ index + 1 }}. {{ item.name }}  <!-- index is 0-based, add 1 for display -->
</li>
```

```html
<!-- Range for repeating elements (no array involved) -->
<div v-for="n in 3" :key="n" class="skeleton-row">
  Loading placeholder {{ n }} of 3...
</div>
<!-- Output: Loading placeholder 1 of 3, 2 of 3, 3 of 3 -->
```

## When Range Iteration Is Useful

- Rendering a fixed number of placeholder/skeleton elements
- Creating pagination buttons: `v-for="page in totalPages"`
- Generating star ratings: `v-for="star in 5"`
- Repeating template structures a set number of times

## Reference
- [Vue.js List Rendering - v-for with a Range](https://vuejs.org/guide/essentials/list.html#v-for-with-a-range)
```

## File: `skills/vue-debug-guides/reference/v-if-null-check-order.md`
```markdown
---
title: Check for Null/Undefined Before Accessing Properties in v-if
impact: MEDIUM
impactDescription: Accessing properties on null/undefined causes runtime errors and crashes
type: capability
tags: [vue3, conditional-rendering, v-if, null-check, defensive-programming]
---

# Check for Null/Undefined Before Accessing Properties in v-if

**Impact: MEDIUM** - Accessing properties on null or undefined objects in `v-if` conditions causes "Cannot read property of undefined" runtime errors. This commonly occurs when data is loaded asynchronously or when optional object properties are accessed without null checks.

## Task Checklist

- [ ] Always check that an object exists before accessing its properties
- [ ] Use optional chaining (?.) in Vue 3 templates for cleaner null checks
- [ ] Consider using computed properties for complex conditional logic
- [ ] Handle loading states explicitly rather than relying on undefined checks

**Incorrect:**
```html
<!-- WRONG: Accessing property before checking object exists -->
<template>
  <div v-if="user.isAdmin">
    Admin Panel
  </div>
  <!-- Error if user is null/undefined: Cannot read property 'isAdmin' of undefined -->
</template>
```

```html
<!-- WRONG: Nested property access without checks -->
<template>
  <div v-if="order.customer.address.city === 'NYC'">
    Local delivery available
  </div>
  <!-- Error if any level is undefined -->
</template>
```

```html
<!-- WRONG: Array access without existence check -->
<template>
  <div v-if="items[0].name === 'Featured'">
    {{ items[0].description }}
  </div>
  <!-- Error if items is empty array -->
</template>
```

**Correct:**
```html
<!-- CORRECT: Check object exists first with && -->
<template>
  <div v-if="user && user.isAdmin">
    Admin Panel
  </div>
</template>
```

```html
<!-- CORRECT: Optional chaining (Vue 3) -->
<template>
  <div v-if="user?.isAdmin">
    Admin Panel
  </div>
</template>
```

```html
<!-- CORRECT: Optional chaining for nested properties -->
<template>
  <div v-if="order?.customer?.address?.city === 'NYC'">
    Local delivery available
  </div>
</template>
```

```html
<!-- CORRECT: Array length check before access -->
<template>
  <div v-if="items.length > 0 && items[0].name === 'Featured'">
    {{ items[0].description }}
  </div>

  <!-- Or with optional chaining -->
  <div v-if="items?.[0]?.name === 'Featured'">
    {{ items[0].description }}
  </div>
</template>
```

```html
<!-- CORRECT: Explicit loading state handling -->
<template>
  <div v-if="isLoading">Loading...</div>
  <div v-else-if="error">Error: {{ error.message }}</div>
  <div v-else-if="user">
    <h1>Welcome, {{ user.name }}</h1>
    <div v-if="user.isAdmin">Admin Panel</div>
  </div>
  <div v-else>No user data</div>
</template>
```

## Using Computed Properties for Complex Checks

```javascript
// CORRECT: Move complex checks to computed properties
<script setup>
import { computed } from 'vue'

const props = defineProps(['user', 'permissions'])

const canAccessAdmin = computed(() => {
  return props.user?.isAdmin &&
         props.permissions?.includes('admin_panel') &&
         !props.user?.isDisabled
})

const userDisplayName = computed(() => {
  return props.user?.profile?.displayName ||
         props.user?.name ||
         'Anonymous'
})
</script>

<template>
  <div v-if="canAccessAdmin">
    Admin Panel
  </div>
  <span>{{ userDisplayName }}</span>
</template>
```

## Common Async Data Pattern

```javascript
// CORRECT: Handle async data loading properly
<script setup>
import { ref, onMounted } from 'vue'

const user = ref(null)
const isLoading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    user.value = await fetchUser()
  } catch (e) {
    error.value = e
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div v-if="isLoading">Loading user...</div>
  <div v-else-if="error">Failed to load user</div>
  <div v-else-if="user">
    <!-- Safe to access user properties here -->
    <h1>{{ user.name }}</h1>
    <p v-if="user.bio">{{ user.bio }}</p>
  </div>
</template>
```

## Reference
- [Vue.js Conditional Rendering](https://vuejs.org/guide/essentials/conditional.html)
- [MDN - Optional Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
```

## File: `skills/vue-debug-guides/reference/v-model-ignores-html-attributes.md`
```markdown
---
title: v-model Ignores Initial HTML Attributes
impact: HIGH
impactDescription: v-model ignores value, checked, and selected HTML attributes - initial state must be set in JavaScript
type: capability
tags: [vue3, v-model, forms, input, checkbox, select, initialization]
---

# v-model Ignores Initial HTML Attributes

**Impact: HIGH** - Setting initial values via HTML `value`, `checked`, or `selected` attributes has no effect when using v-model. The form will appear empty or in an unexpected state, confusing users and potentially causing data loss.

Vue's v-model always treats the bound JavaScript state as the single source of truth. Any initial attributes in the HTML are completely ignored. This is a common mistake when migrating from plain HTML forms or when copying HTML templates.

## Task Checklist

- [ ] Never rely on HTML `value`, `checked`, or `selected` attributes when using v-model
- [ ] Always declare initial values in JavaScript using `ref()` or `reactive()`
- [ ] When migrating plain HTML forms to Vue, move all default values to JavaScript state
- [ ] Audit existing forms for hardcoded HTML default values that may be silently ignored

**Incorrect:**
```html
<script setup>
import { ref } from 'vue'

const username = ref('')  // Empty!
const isSubscribed = ref(false)  // Not checked!
const country = ref('')  // No default selection!
</script>

<template>
  <!-- WRONG: These HTML attributes are completely ignored -->
  <input v-model="username" value="default_user">

  <input type="checkbox" v-model="isSubscribed" checked>

  <select v-model="country">
    <option value="us" selected>United States</option>
    <option value="uk">United Kingdom</option>
  </select>
</template>
```

**Correct:**
```html
<script setup>
import { ref } from 'vue'

// CORRECT: Set initial values in JavaScript
const username = ref('default_user')
const isSubscribed = ref(true)
const country = ref('us')
</script>

<template>
  <!-- HTML attributes not needed - JavaScript state controls everything -->
  <input v-model="username">

  <input type="checkbox" v-model="isSubscribed">

  <select v-model="country">
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
  </select>
</template>
```

```javascript
// Options API equivalent
export default {
  data() {
    return {
      username: 'default_user',
      isSubscribed: true,
      country: 'us'
    }
  }
}
```

## Reference
- [Vue.js Form Input Bindings](https://vuejs.org/guide/essentials/forms.html)
```

## File: `skills/vue-debug-guides/reference/v-model-ime-composition.md`
```markdown
---
title: v-model Does Not Update During IME Composition
impact: MEDIUM
impactDescription: v-model won't capture intermediate input for Chinese, Japanese, Korean and other IME languages
type: capability
tags: [vue3, v-model, forms, input, ime, internationalization, i18n, cjk]
---

# v-model Does Not Update During IME Composition

**Impact: MEDIUM** - When users type in languages that require an Input Method Editor (Chinese, Japanese, Korean, etc.), v-model won't update until the composition is complete. This breaks real-time validation, character counters, and live search features for international users.

IME (Input Method Editor) allows users to compose complex characters by typing multiple keystrokes. During this composition phase, v-model deliberately waits until the user confirms their selection before updating. This is usually desired, but can break features that need every keystroke.

## Task Checklist

- [ ] Test forms with IME input if your app serves CJK (Chinese, Japanese, Korean) users
- [ ] For real-time features (live search, character counters), use manual event binding instead of v-model
- [ ] Consider both behaviors when designing - sometimes waiting for composition completion IS correct
- [ ] Document expected behavior for international users

**Problem - v-model waits for composition:**
```html
<script setup>
import { ref } from 'vue'

const searchQuery = ref('')
const charCount = ref(0)
</script>

<template>
  <!-- PROBLEM: During IME composition, searchQuery won't update -->
  <!-- Chinese user types "ni hao" -> sees no results until they press space/enter -->
  <input v-model="searchQuery" placeholder="Live search...">
  <p>{{ searchQuery.length }} characters</p>

  <!-- Character counter stays at 0 during IME input -->
</template>
```

**Solution - Manual event binding for real-time updates:**
```html
<script setup>
import { ref } from 'vue'

const searchQuery = ref('')

// This captures EVERY input event, including during IME composition
function handleInput(event) {
  searchQuery.value = event.target.value
}
</script>

<template>
  <!-- CORRECT: Manual binding captures all input, including IME composition -->
  <input
    :value="searchQuery"
    @input="handleInput"
    placeholder="Live search..."
  >
  <p>{{ searchQuery.length }} characters</p>
</template>
```

```html
<!-- Shorter inline version -->
<input
  :value="searchQuery"
  @input="event => searchQuery = event.target.value"
>
```

**When v-model behavior IS correct:**
```html
<!-- For form submission, waiting for composition IS usually better -->
<!-- User expects to confirm their character selection before it's "official" -->
<input v-model="formName" placeholder="Enter your name">

<!-- The final composed characters will be submitted, not intermediate states -->
```

## Reference
- [Vue.js Form Input Bindings](https://vuejs.org/guide/essentials/forms.html)
```

## File: `skills/vue-debug-guides/reference/v-model-number-modifier-behavior.md`
```markdown
---
title: v-model.number Uses parseFloat Not valueAsNumber
impact: MEDIUM
impactDescription: .number modifier returns empty string for empty input and uses parseFloat, not native valueAsNumber
type: capability
tags: [vue3, v-model, forms, input, number, type-coercion, modifiers]
---

# v-model.number Uses parseFloat Not valueAsNumber

**Impact: MEDIUM** - The `.number` modifier doesn't behave like the native `valueAsNumber` property. It returns an empty string (not NaN) for empty inputs, and uses `parseFloat()` which has different parsing rules. This can cause unexpected type issues in calculations and validations.

Understanding these differences is crucial when working with numeric forms, especially for calculations, min/max validation, or when interfacing with APIs that expect strict number types.

## Task Checklist

- [ ] Expect empty string (not 0 or NaN) when input is cleared with `.number` modifier
- [ ] Handle the empty string case in your validation and calculations
- [ ] Remember `.number` uses parseFloat - "123abc" becomes 123, not NaN
- [ ] For strict numeric parsing, add custom validation

**Key Differences:**

| Scenario | `.number` modifier | Native `valueAsNumber` |
|----------|-------------------|----------------------|
| Empty input | `''` (empty string) | `NaN` |
| `"123"` | `123` | `123` |
| `"123.45"` | `123.45` | `123.45` |
| `"123abc"` | `123` | `NaN` |
| `"abc"` | `'abc'` (original string) | `NaN` |

**Problem - Unexpected types:**
```html
<script setup>
import { ref, computed } from 'vue'

const price = ref(0)
const quantity = ref(1)

const total = computed(() => {
  // PROBLEM: price might be '' (empty string) when input is cleared
  return price.value * quantity.value  // '' * 1 = 0, but typeof is still number
})

function validatePrice() {
  // PROBLEM: This check fails when input is empty
  if (typeof price.value !== 'number') {
    // Never enters here! '' is still treated as "processed"
  }

  // PROBLEM: parseFloat("$100") returns NaN, but "100abc" returns 100
}
</script>

<template>
  <input v-model.number="price" type="number">
  <!-- When user clears input, price.value becomes '' not 0 or NaN -->
</template>
```

**Solution - Handle empty string explicitly:**
```html
<script setup>
import { ref, computed } from 'vue'

const price = ref(0)
const quantity = ref(1)

const total = computed(() => {
  // CORRECT: Handle empty string case
  const priceNum = price.value === '' ? 0 : price.value
  return priceNum * quantity.value
})

// Or use a wrapper computed for safer access
const safePrice = computed(() => {
  if (price.value === '' || price.value === null) return 0
  return Number(price.value) || 0
})
</script>

<template>
  <input v-model.number="price" type="number" min="0">
  <p>Total: ${{ total.toFixed(2) }}</p>
</template>
```

**Solution - Custom input handling for strict parsing:**
```html
<script setup>
import { ref } from 'vue'

const price = ref(0)

function handlePriceInput(event) {
  const value = event.target.value

  // Strict parsing - only accept valid numbers
  const parsed = parseFloat(value)

  if (value === '') {
    price.value = 0  // Or null, depending on your needs
  } else if (!isNaN(parsed) && isFinite(parsed)) {
    // Additional check: ensure entire string is numeric
    if (/^-?\d*\.?\d+$/.test(value.trim())) {
      price.value = parsed
    }
  }
  // Invalid input - keep previous value
}
</script>

<template>
  <!-- Manual binding for strict numeric control -->
  <input
    :value="price"
    @input="handlePriceInput"
    type="number"
  >
</template>
```

## Reference
- [Vue.js Form Input Bindings - .number](https://vuejs.org/guide/essentials/forms.html#number)
```

## File: `skills/vue-debug-guides/reference/v-show-template-limitation.md`
```markdown
---
title: v-show Does Not Work on template or With v-else
impact: MEDIUM
impactDescription: Using v-show on template silently fails, element is always rendered
type: capability
tags: [vue3, conditional-rendering, v-show, template, limitations]
---

# v-show Does Not Work on template or With v-else

**Impact: MEDIUM** - `v-show` cannot be used on `<template>` elements because templates don't render to the DOM (so there's nothing to apply `display: none` to). Additionally, `v-show` does not support `v-else`. Using these incorrectly results in elements that are always visible or else branches that never work.

## Task Checklist

- [ ] Never use v-show on `<template>` elements - use v-if instead
- [ ] Never use v-else with v-show - use separate v-show with negated condition
- [ ] Remember v-show only works on actual DOM elements
- [ ] If you need to toggle multiple elements frequently, wrap in a real element (div, span)

**Incorrect:**
```html
<!-- WRONG: v-show on <template> - silently does nothing -->
<template>
  <template v-show="isVisible">
    <h1>Title</h1>
    <p>Content</p>
  </template>
  <!-- These elements will ALWAYS be visible -->
</template>
```

```html
<!-- WRONG: v-else with v-show - v-else is not supported -->
<template>
  <div v-show="isLoggedIn">Welcome!</div>
  <div v-else>Please log in</div>  <!-- This v-else won't work -->
</template>
```

```html
<!-- WRONG: Mixing v-show and v-else expectations -->
<template>
  <span v-show="status === 'success'">Success!</span>
  <span v-else-if="status === 'error'">Error</span>  <!-- Not supported -->
</template>
```

**Correct:**
```html
<!-- CORRECT: Use v-if on <template> for multiple elements -->
<template>
  <template v-if="isVisible">
    <h1>Title</h1>
    <p>Content</p>
  </template>
</template>
```

```html
<!-- CORRECT: Use negated v-show for "else" behavior -->
<template>
  <div v-show="isLoggedIn">Welcome!</div>
  <div v-show="!isLoggedIn">Please log in</div>
</template>
```

```html
<!-- CORRECT: Wrap in a real element if you need v-show for multiple elements -->
<template>
  <div v-show="isVisible">
    <h1>Title</h1>
    <p>Content</p>
  </div>
</template>
```

```html
<!-- CORRECT: Use v-if/v-else when you need else branches -->
<template>
  <div v-if="status === 'success'">Success!</div>
  <div v-else-if="status === 'error'">Error</div>
  <div v-else>Loading...</div>
</template>
```

```html
<!-- CORRECT: Multiple v-show conditions -->
<template>
  <span v-show="status === 'success'">Success!</span>
  <span v-show="status === 'error'">Error</span>
  <span v-show="status === 'loading'">Loading...</span>
</template>
```

## Why This Limitation Exists

```javascript
// v-show works by toggling the CSS display property
// This requires an actual DOM element

// <template> is a virtual element - it doesn't render to DOM
// It's just a wrapper for Vue's rendering logic

// After compilation:
// <template v-if="show"><p>Hi</p></template>
// Renders as: <p>Hi</p> (when show is true)
// Template itself is gone

// v-show needs a real element to set display: none on
// Since <template> doesn't exist in DOM, v-show has nothing to work with
```

## When to Choose Each

| Need | Use |
|------|-----|
| Toggle multiple elements with CSS | Wrap in real element + `v-show` |
| Toggle multiple elements without wrapper | `<template v-if>` |
| Need v-else branches | `v-if`/`v-else` |
| Frequent toggle, single element | `v-show` |
| Frequent toggle, need "else" | Two `v-show` with negated conditions |

## Reference
- [Vue.js Conditional Rendering - v-show](https://vuejs.org/guide/essentials/conditional.html#v-show)
```

## File: `skills/vue-debug-guides/reference/watch-async-cleanup.md`
```markdown
---
title: Clean Up Async Operations in Watchers to Prevent Race Conditions
impact: HIGH
impactDescription: Stale async requests can overwrite newer data, causing incorrect UI state and hard-to-debug issues
type: capability
tags: [vue3, watch, watchers, async, cleanup, race-condition, abort]
---

# Clean Up Async Operations in Watchers to Prevent Race Conditions

**Impact: HIGH** - When a watched value changes rapidly, multiple async operations run concurrently. Without cleanup, a slow earlier request can complete after a faster later request, overwriting current data with stale results.

Always use `onWatcherCleanup` or the `onCleanup` callback parameter to cancel pending async operations when the watcher re-runs or the component unmounts.

## Task Checklist

- [ ] Use `onWatcherCleanup()` or `onCleanup` parameter in async watchers
- [ ] Use `AbortController` to cancel pending fetch requests
- [ ] Cancel any setTimeout/setInterval calls in cleanup
- [ ] Invalidate previous async operation results with flags
- [ ] Consider debouncing rapid changes before fetching

**Incorrect:**
```javascript
import { ref, watch } from 'vue'

const searchQuery = ref('')
const results = ref([])

// BAD: Race condition - slow request for "a" can finish after fast request for "ab"
watch(searchQuery, async (query) => {
  if (query) {
    const response = await fetch(`/api/search?q=${query}`)
    results.value = await response.json()  // May overwrite newer results!
  }
})

// BAD: No cleanup for timeouts
watch(searchQuery, (query) => {
  // Previous timeout keeps running even when query changes
  setTimeout(() => {
    performExpensiveSearch(query)
  }, 500)
})
```

**Correct:**
```javascript
import { ref, watch, onWatcherCleanup } from 'vue'

const searchQuery = ref('')
const results = ref([])
const loading = ref(false)

// CORRECT: Using onWatcherCleanup (Vue 3.5+)
watch(searchQuery, async (query) => {
  if (!query) {
    results.value = []
    return
  }

  const controller = new AbortController()

  // Register cleanup to abort on re-run or unmount
  onWatcherCleanup(() => {
    controller.abort()
  })

  loading.value = true
  try {
    const response = await fetch(`/api/search?q=${query}`, {
      signal: controller.signal
    })
    results.value = await response.json()
  } catch (err) {
    if (err.name !== 'AbortError') {
      console.error('Search failed:', err)
    }
  } finally {
    loading.value = false
  }
})
```

## Using onCleanup Parameter

```javascript
import { ref, watch } from 'vue'

const userId = ref(1)
const userData = ref(null)

// CORRECT: Using onCleanup callback parameter
watch(userId, (newId, oldId, onCleanup) => {
  const controller = new AbortController()

  fetch(`/api/users/${newId}`, { signal: controller.signal })
    .then(res => res.json())
    .then(data => {
      userData.value = data
    })
    .catch(err => {
      if (err.name !== 'AbortError') {
        console.error(err)
      }
    })

  onCleanup(() => {
    controller.abort()
  })
})
```

## Cleanup with Timeouts

```javascript
import { ref, watch, onWatcherCleanup } from 'vue'

const input = ref('')

// CORRECT: Cancel previous timeout on new input
watch(input, (value) => {
  const timeoutId = setTimeout(() => {
    performExpensiveOperation(value)
  }, 300)

  onWatcherCleanup(() => {
    clearTimeout(timeoutId)
  })
})
```

## Invalidation Flag Pattern

```javascript
import { ref, watch } from 'vue'

const id = ref(1)
const data = ref(null)

// CORRECT: Invalidation flag for non-abortable operations
watch(id, async (newId, oldId, onCleanup) => {
  let cancelled = false

  onCleanup(() => {
    cancelled = true
  })

  const result = await someNonAbortableAsyncOperation(newId)

  // Check if this watch run is still valid
  if (!cancelled) {
    data.value = result
  }
})
```

## watchEffect Cleanup

```javascript
import { ref, watchEffect, onWatcherCleanup } from 'vue'

const resourceId = ref('abc')

watchEffect(async () => {
  const id = resourceId.value
  const controller = new AbortController()

  onWatcherCleanup(() => {
    controller.abort()
  })

  const data = await fetchResource(id, { signal: controller.signal })
  processData(data)
})
```

## Reference
- [Vue.js Watchers - Callback Flush Timing](https://vuejs.org/guide/essentials/watchers.html#callback-flush-timing)
- [Vue.js Watchers - Side Effect Cleanup](https://vuejs.org/api/reactivity-core.html#watcheffect)
```

## File: `skills/vue-debug-guides/reference/watch-async-creation-memory-leak.md`
```markdown
---
title: Watchers Created Asynchronously Must Be Manually Stopped
impact: HIGH
impactDescription: Async-created watchers are not bound to component lifecycle and cause memory leaks
type: capability
tags: [vue3, watch, watchers, async, memory-leak, lifecycle, cleanup]
---

# Watchers Created Asynchronously Must Be Manually Stopped

**Impact: HIGH** - Watchers created inside async callbacks (setTimeout, Promise.then, async/await) are not automatically bound to the component instance. They continue running after the component unmounts, causing memory leaks and errors.

Always manually stop watchers that are created asynchronously, or restructure your code to create watchers synchronously with conditional logic.

## Task Checklist

- [ ] Create watchers synchronously in setup() or lifecycle hooks when possible
- [ ] If async creation is unavoidable, store and call the unwatch function
- [ ] Use `onUnmounted` to clean up async-created watchers
- [ ] Consider using conditional logic inside a sync watcher instead
- [ ] Watch for this pattern in setTimeout, Promise callbacks, and after await

**Incorrect:**
```vue
<script setup>
import { ref, watch, watchEffect, onMounted } from 'vue'

const data = ref(null)

// BAD: Watcher created in setTimeout won't auto-stop
onMounted(() => {
  setTimeout(() => {
    watchEffect(() => {
      console.log(data.value)  // Keeps running after unmount!
    })
  }, 1000)
})

// BAD: Watcher created after await won't auto-stop
onMounted(async () => {
  await loadInitialData()

  // This watcher is NOT bound to component lifecycle
  watch(data, (newVal) => {
    processData(newVal)  // Memory leak!
  })
})

// BAD: Watcher in Promise callback
fetch('/api/config').then(() => {
  watch(data, () => {
    // Leaks memory!
  })
})
</script>
```

**Correct:**
```vue
<script setup>
import { ref, watch, watchEffect, onMounted, onUnmounted } from 'vue'

const data = ref(null)
const isDataLoaded = ref(false)
let asyncWatcherCleanup = null

// CORRECT: Synchronous watcher with conditional logic
watch(
  data,
  (newVal) => {
    if (isDataLoaded.value && newVal) {
      processData(newVal)
    }
  }
)

onMounted(async () => {
  await loadInitialData()
  isDataLoaded.value = true
})

// CORRECT: Manual cleanup for async-created watcher
onMounted(() => {
  setTimeout(() => {
    const unwatch = watchEffect(() => {
      console.log(data.value)
    })

    // Store for cleanup
    asyncWatcherCleanup = unwatch
  }, 1000)
})

onUnmounted(() => {
  // Clean up async watcher
  if (asyncWatcherCleanup) {
    asyncWatcherCleanup()
  }
})
</script>
```

## Preferred Pattern: Conditional Watch Logic

```vue
<script setup>
import { ref, watch, onMounted } from 'vue'

const config = ref(null)
const userData = ref(null)

// BEST: Create watcher synchronously, handle async condition inside
watch(
  userData,
  (newData) => {
    // Only process when config is loaded
    if (config.value && newData) {
      applyUserSettings(config.value, newData)
    }
  }
)

onMounted(async () => {
  config.value = await fetchConfig()
  // Watcher will start processing once config is loaded
})
</script>
```

## Using watchEffect with Conditional Logic

```vue
<script setup>
import { ref, watchEffect, onMounted } from 'vue'

const apiData = ref(null)
const isReady = ref(false)

// GOOD: Synchronous watchEffect with condition
watchEffect(() => {
  if (isReady.value && apiData.value) {
    // This pattern avoids async watcher creation
    doSomethingWithData(apiData.value)
  }
})

onMounted(async () => {
  apiData.value = await fetchData()
  isReady.value = true
})
</script>
```

## Tracking Multiple Async Watchers

```vue
<script setup>
import { ref, watch, onUnmounted } from 'vue'

const unwatchers = []

function createDynamicWatcher(source, callback) {
  const unwatch = watch(source, callback)
  unwatchers.push(unwatch)
  return unwatch
}

// Clean up all dynamic watchers
onUnmounted(() => {
  unwatchers.forEach(unwatch => unwatch())
})
</script>
```

## Reference
- [Vue.js Watchers - Stopping a Watcher](https://vuejs.org/guide/essentials/watchers.html#stopping-a-watcher)
```

## File: `skills/vue-debug-guides/reference/watch-deep-same-object-reference.md`
```markdown
---
title: Deep Watch Callback Receives Same Object Reference for Old and New Values
impact: MEDIUM
impactDescription: Comparing oldValue and newValue in deep watchers is misleading since they reference the same object
type: capability
tags: [vue3, watch, watchers, deep, oldValue, newValue, object-reference]
---

# Deep Watch Callback Receives Same Object Reference for Old and New Values

**Impact: MEDIUM** - When using deep watchers on reactive objects, both `newValue` and `oldValue` in the callback point to the same object reference. They will always be equal for nested mutations because Vue doesn't clone the object before mutation.

Don't rely on comparing `newValue` to `oldValue` in deep watchers for detecting what changed. Instead, track specific values or implement your own diffing.

## Task Checklist

- [ ] Don't compare newValue === oldValue in deep watchers to detect changes
- [ ] For change detection, watch specific properties instead
- [ ] If you need old values, manually snapshot before changes
- [ ] Consider using a serialization approach for complex diffing needs
- [ ] The values differ only when the entire object is replaced

**Incorrect:**
```javascript
import { reactive, watch } from 'vue'

const state = reactive({
  user: {
    name: 'John',
    preferences: { theme: 'dark' }
  }
})

// BAD: Trying to compare old and new values
watch(
  () => state.user,
  (newUser, oldUser) => {
    // This comparison is ALWAYS true for nested mutations!
    if (newUser === oldUser) {
      console.log('Same reference!')  // Always logs for nested changes
    }

    // This also won't work - they're the same object
    if (newUser.name !== oldUser.name) {
      console.log('Name changed')  // Never logs for nested mutations
    }
  },
  { deep: true }
)

// When this happens:
state.user.name = 'Jane'
// Both newUser and oldUser are { name: 'Jane', preferences: { theme: 'dark' } }
```

**Correct:**
```javascript
import { reactive, watch, ref } from 'vue'

const state = reactive({
  user: {
    name: 'John',
    preferences: { theme: 'dark' }
  }
})

// CORRECT: Watch specific properties you care about
watch(
  () => state.user.name,
  (newName, oldName) => {
    console.log(`Name changed from "${oldName}" to "${newName}"`)
    // oldName and newName are primitives, work correctly
  }
)

// CORRECT: Watch multiple specific properties
watch(
  [() => state.user.name, () => state.user.preferences.theme],
  ([newName, newTheme], [oldName, oldTheme]) => {
    if (newName !== oldName) {
      console.log(`Name: ${oldName} -> ${newName}`)
    }
    if (newTheme !== oldTheme) {
      console.log(`Theme: ${oldTheme} -> ${newTheme}`)
    }
  }
)
```

## Manual Snapshot Pattern

```javascript
import { reactive, watch, ref } from 'vue'

const state = reactive({ count: 0, items: [] })

// Keep a manual snapshot for comparison
const previousSnapshot = ref(JSON.stringify(state))

watch(
  state,
  (newState) => {
    const currentSnapshot = JSON.stringify(newState)

    if (currentSnapshot !== previousSnapshot.value) {
      const oldData = JSON.parse(previousSnapshot.value)
      console.log('Old:', oldData)
      console.log('New:', newState)

      // Update snapshot for next comparison
      previousSnapshot.value = currentSnapshot
    }
  },
  { deep: true }
)
```

## When Old and New Values Differ

```javascript
import { reactive, watch } from 'vue'

const state = reactive({
  currentUser: { name: 'John' }
})

watch(
  () => state.currentUser,
  (newUser, oldUser) => {
    // THESE DIFFER when the object itself is replaced
    console.log('Old:', oldUser)  // { name: 'John' }
    console.log('New:', newUser)  // { name: 'Jane' }
  },
  { deep: true }
)

// Object replacement - old and new are different
state.currentUser = { name: 'Jane' }

// vs. Mutation - old and new are the same reference
// state.currentUser.name = 'Jane'
```

## Using Getter Returns New Object

```javascript
import { reactive, watch } from 'vue'

const state = reactive({
  user: { firstName: 'John', lastName: 'Doe' }
})

// CORRECT: Getter returns new object, so old/new comparison works
watch(
  () => ({ ...state.user }),  // Shallow clone
  (newUser, oldUser) => {
    // Now these are different objects
    console.log('Changed from', oldUser, 'to', newUser)
  },
  { deep: true }
)
```

## Reference
- [Vue.js Watchers - Deep Watchers](https://vuejs.org/guide/essentials/watchers.html#deep-watchers)
```

## File: `skills/vue-debug-guides/reference/watch-flush-timing.md`
```markdown
---
title: Use flush post When Accessing Updated DOM in Watchers
impact: MEDIUM
impactDescription: Default watcher timing runs before DOM updates, causing stale DOM reads
type: capability
tags: [vue3, watch, watchers, flush, DOM, timing, post]
---

# Use flush: 'post' When Accessing Updated DOM in Watchers

**Impact: MEDIUM** - By default, watcher callbacks run before the component's DOM is updated. If you access the DOM in a watcher callback, you'll see the pre-update state. Use `flush: 'post'` or `watchPostEffect` when you need to access the updated DOM.

## Task Checklist

- [ ] Use `{ flush: 'post' }` when reading DOM after reactive state changes
- [ ] Use `watchPostEffect()` as a shorthand for `watchEffect` with flush: 'post'
- [ ] Avoid `{ flush: 'sync' }` unless absolutely necessary (performance impact)
- [ ] Remember default timing is ideal for most non-DOM operations

**Incorrect:**
```vue
<script setup>
import { ref, watch, watchEffect } from 'vue'

const count = ref(0)
const listItems = ref(['a', 'b', 'c'])

// BAD: DOM shows old value when this runs
watch(count, () => {
  // Element still shows the OLD count value
  const el = document.querySelector('.counter')
  console.log('DOM shows:', el.textContent)  // Old value!
})

// BAD: List DOM not yet updated
watchEffect(() => {
  console.log('Items:', listItems.value.length)
  // DOM still has old number of list items
  const items = document.querySelectorAll('.list-item')
  console.log('DOM items:', items.length)  // Old count!
})
</script>

<template>
  <div class="counter">{{ count }}</div>
  <ul>
    <li v-for="item in listItems" :key="item" class="list-item">
      {{ item }}
    </li>
  </ul>
</template>
```

**Correct:**
```vue
<script setup>
import { ref, watch, watchEffect, watchPostEffect } from 'vue'

const count = ref(0)
const listItems = ref(['a', 'b', 'c'])

// CORRECT: flush: 'post' runs after DOM update
watch(
  count,
  () => {
    const el = document.querySelector('.counter')
    console.log('DOM shows:', el.textContent)  // Correct new value!
  },
  { flush: 'post' }
)

// CORRECT: watchPostEffect shorthand
watchPostEffect(() => {
  console.log('Items:', listItems.value.length)
  const items = document.querySelectorAll('.list-item')
  console.log('DOM items:', items.length)  // Matches listItems.length!
})

// CORRECT: Using watchEffect with flush option
watchEffect(
  () => {
    // Access reactive state and DOM together
    const expectedCount = listItems.value.length
    const actualCount = document.querySelectorAll('.list-item').length
    console.log(`Expected: ${expectedCount}, Actual: ${actualCount}`)
  },
  { flush: 'post' }
)
</script>

<template>
  <div class="counter">{{ count }}</div>
  <ul>
    <li v-for="item in listItems" :key="item" class="list-item">
      {{ item }}
    </li>
  </ul>
</template>
```

## Flush Timing Options

```javascript
import { watch, watchEffect, watchPostEffect, watchSyncEffect } from 'vue'

// Default: 'pre' - runs before component DOM update
watch(source, callback)  // Same as { flush: 'pre' }

// Post: runs after component DOM update
watch(source, callback, { flush: 'post' })
watchPostEffect(callback)  // Shorthand

// Sync: runs immediately when reactive value changes
// USE WITH CAUTION - no batching, fires on every mutation
watch(source, callback, { flush: 'sync' })
watchSyncEffect(callback)  // Shorthand
```

## When to Use Each Flush Timing

| Timing | Use Case |
|--------|----------|
| `'pre'` (default) | Logic that doesn't need DOM access |
| `'post'` | Reading or measuring updated DOM |
| `'sync'` | Debug logging, simple boolean flags only |

## Sync Watcher Warning

```javascript
import { ref, watch } from 'vue'

const items = ref([1, 2, 3])

// DANGEROUS: Fires for EVERY array mutation
watch(
  items,
  () => {
    console.log('Changed!')  // Called 3 times for push, push, push
  },
  { flush: 'sync' }
)

// This triggers the watcher 3 times synchronously
items.value.push(4)
items.value.push(5)
items.value.push(6)

// Better: Use default flush which batches updates
watch(items, () => {
  console.log('Changed!')  // Called once after all mutations
}, { deep: true })
```

## Practical Example: Auto-scroll

```vue
<script setup>
import { ref, watchPostEffect } from 'vue'

const messages = ref([])
const containerRef = ref(null)

// Auto-scroll to bottom when new messages arrive
watchPostEffect(() => {
  // Access messages.value to track it
  const msgCount = messages.value.length

  // DOM is updated, safe to scroll
  if (containerRef.value && msgCount > 0) {
    containerRef.value.scrollTop = containerRef.value.scrollHeight
  }
})

function addMessage(text) {
  messages.value.push({ text, timestamp: Date.now() })
}
</script>

<template>
  <div ref="containerRef" class="messages">
    <div v-for="msg in messages" :key="msg.timestamp">
      {{ msg.text }}
    </div>
  </div>
</template>
```

## Reference
- [Vue.js Watchers - Callback Flush Timing](https://vuejs.org/guide/essentials/watchers.html#callback-flush-timing)
```

## File: `skills/vue-debug-guides/reference/watch-reactive-property-getter.md`
```markdown
---
title: Use Getter Function When Watching Reactive Object Properties
impact: HIGH
impactDescription: Watching reactive properties directly passes a primitive value, causing the watcher to never trigger
type: capability
tags: [vue3, watch, watchers, reactive, getter, common-mistake]
---

# Use Getter Function When Watching Reactive Object Properties

**Impact: HIGH** - Directly watching a property of a reactive object passes a primitive value to `watch()`, not a reactive reference. The watcher will never trigger because primitives are not reactive.

When you need to watch a specific property of a reactive object, always wrap it in a getter function `() => obj.property`.

## Task Checklist

- [ ] Always use getter functions when watching properties of reactive objects
- [ ] Remember that `watch(obj.count, ...)` passes the current value, not a reactive reference
- [ ] For refs, you can watch directly: `watch(myRef, ...)`
- [ ] For entire reactive objects, you can watch directly (creates implicit deep watcher)

**Incorrect:**
```javascript
import { reactive, watch } from 'vue'

const state = reactive({ count: 0, name: 'Vue' })

// WRONG: Passes the number 0 to watch(), not a reactive reference
// This watcher will NEVER fire!
watch(state.count, (newCount) => {
  console.log(`Count changed to: ${newCount}`)
})

// WRONG: Same problem with string property
watch(state.name, (newName) => {
  console.log(`Name changed to: ${newName}`)
})
```

**Correct:**
```javascript
import { reactive, watch } from 'vue'

const state = reactive({ count: 0, name: 'Vue' })

// CORRECT: Use a getter function
watch(
  () => state.count,
  (newCount, oldCount) => {
    console.log(`Count changed from ${oldCount} to ${newCount}`)
  }
)

// CORRECT: Multiple properties with getter
watch(
  () => state.name,
  (newName) => {
    console.log(`Name changed to: ${newName}`)
  }
)

// CORRECT: Watching derived values
watch(
  () => state.count * 2,
  (doubledCount) => {
    console.log(`Doubled count: ${doubledCount}`)
  }
)
```

## Watching Multiple Properties

```javascript
import { reactive, watch } from 'vue'

const state = reactive({ firstName: 'John', lastName: 'Doe' })

// Watch multiple properties with array of getters
watch(
  [() => state.firstName, () => state.lastName],
  ([newFirst, newLast], [oldFirst, oldLast]) => {
    console.log(`Name changed from ${oldFirst} ${oldLast} to ${newFirst} ${newLast}`)
  }
)
```

## When Direct Watching Works

```javascript
import { ref, reactive, watch } from 'vue'

const count = ref(0)
const state = reactive({ nested: { value: 1 } })

// CORRECT: Refs can be watched directly
watch(count, (newVal) => {
  console.log(`Count: ${newVal}`)
})

// CORRECT: Entire reactive objects create implicit deep watcher
watch(state, (newState) => {
  // Fires on any nested change
  // Note: newState === oldState (same object reference)
})
```

## Reference
- [Vue.js Watchers - Watch Source Types](https://vuejs.org/guide/essentials/watchers.html#watch-source-types)
```

## File: `skills/vue-debug-guides/reference/watcheffect-async-dependency-tracking.md`
```markdown
---
title: watchEffect Only Tracks Dependencies Before First Await
impact: HIGH
impactDescription: Dependencies accessed after await are not tracked, causing watchers to miss reactive changes
type: capability
tags: [vue3, watchEffect, watchers, async, await, dependency-tracking]
---

# watchEffect Only Tracks Dependencies Before First Await

**Impact: HIGH** - `watchEffect` automatically tracks reactive dependencies, but only during synchronous execution. Any reactive properties accessed after the first `await` statement will NOT be tracked, and changes to them won't trigger the watcher.

For async operations, either access all dependencies before the await, or use `watch` with explicit dependencies.

## Task Checklist

- [ ] Access all reactive dependencies BEFORE the first await in watchEffect
- [ ] Use `watch` with explicit source when async tracking is needed
- [ ] Store reactive values in local variables before await
- [ ] Be aware that dependencies after await are invisible to Vue

**Incorrect:**
```vue
<script setup>
import { ref, watchEffect } from 'vue'

const userId = ref(1)
const includeDetails = ref(true)
const userData = ref(null)

// BAD: includeDetails is accessed after await - NOT TRACKED!
watchEffect(async () => {
  const response = await fetch(`/api/users/${userId.value}`)
  const data = await response.json()

  // This dependency is NOT tracked - changes won't trigger re-run
  if (includeDetails.value) {
    userData.value = { ...data, details: await fetchDetails(data.id) }
  } else {
    userData.value = data
  }
})

// BAD: Multiple dependencies after await
watchEffect(async () => {
  await someAsyncSetup()

  // None of these are tracked!
  console.log(optionA.value)  // Not tracked
  console.log(optionB.value)  // Not tracked
  doSomething(optionC.value)  // Not tracked
})
</script>
```

**Correct:**
```vue
<script setup>
import { ref, watchEffect, watch } from 'vue'

const userId = ref(1)
const includeDetails = ref(true)
const userData = ref(null)

// CORRECT: Access all dependencies before await
watchEffect(async () => {
  // Capture reactive values synchronously
  const id = userId.value
  const withDetails = includeDetails.value

  // Now these are tracked
  const response = await fetch(`/api/users/${id}`)
  const data = await response.json()

  if (withDetails) {
    userData.value = { ...data, details: await fetchDetails(data.id) }
  } else {
    userData.value = data
  }
})

// ALTERNATIVE: Use watch with explicit dependencies
watch(
  [userId, includeDetails],
  async ([id, withDetails]) => {
    const response = await fetch(`/api/users/${id}`)
    const data = await response.json()

    if (withDetails) {
      userData.value = { ...data, details: await fetchDetails(data.id) }
    } else {
      userData.value = data
    }
  },
  { immediate: true }
)
</script>
```

## Pattern: Extract Dependencies First

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const filters = ref({ status: 'active', sortBy: 'name' })
const page = ref(1)
const results = ref([])

// CORRECT: Extract all needed values synchronously
watchEffect(async () => {
  // All dependencies accessed before await - all tracked!
  const { status, sortBy } = filters.value
  const currentPage = page.value

  // Now safe to do async work
  const response = await fetch(
    `/api/items?status=${status}&sort=${sortBy}&page=${currentPage}`
  )
  results.value = await response.json()
})
</script>
```

## When to Use watch Instead

```vue
<script setup>
import { ref, watch } from 'vue'

const source = ref('initial')
const option = ref('default')
const result = ref(null)

// BEST for complex async: Use watch with explicit sources
// All dependencies are explicitly declared and always tracked
watch(
  [source, option],
  async ([sourceVal, optionVal]) => {
    const data = await processAsync(sourceVal)
    result.value = applyOption(data, optionVal)
  },
  { immediate: true }
)
</script>
```

## Debugging Untracked Dependencies

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const a = ref(1)
const b = ref(2)

watchEffect(async () => {
  console.log('Tracked dependency a:', a.value)  // Tracked

  await someAsyncOperation()

  console.log('Untracked dependency b:', b.value)  // NOT tracked!
  // Changing b.value won't re-run this watchEffect
})

// Test: Change a.value -> watchEffect re-runs
// Test: Change b.value -> watchEffect does NOT re-run
</script>
```

## Reference
- [Vue.js Watchers - watchEffect](https://vuejs.org/guide/essentials/watchers.html#watcheffect)
- [Vue.js API - watchEffect](https://vuejs.org/api/reactivity-core.html#watcheffect)
```

## File: `skills/vue-debug-guides/reference/watcheffect-flush-post-for-refs.md`
```markdown
---
title: Use flush post for watchEffect with Template Refs
impact: MEDIUM
impactDescription: Default watchEffect runs before DOM updates, causing refs to be out of sync
type: gotcha
tags: [vue3, watchEffect, template-refs, flush, dom-timing]
---

# Use flush post for watchEffect with Template Refs

**Impact: MEDIUM** - By default, `watchEffect` runs before the DOM is updated. When watching template refs, this means the effect may run with stale or null ref values. Use `flush: 'post'` to ensure the effect runs after DOM updates when refs are current.

This timing issue is particularly confusing because the watcher runs, but the ref doesn't yet reflect the current DOM state.

## Task Checklist

- [ ] Use `{ flush: 'post' }` when watchEffect accesses template refs
- [ ] Alternatively, use `watchPostEffect` helper for cleaner syntax
- [ ] Still include null checks as refs can be unmounted
- [ ] Consider using `watch` with explicit ref watching instead

**Incorrect:**
```vue
<script setup>
import { ref, watchEffect } from 'vue'

const inputEl = ref(null)
const text = ref('')

// WRONG: Runs BEFORE DOM update - ref may be null or stale
watchEffect(() => {
  // On first run: inputEl.value is null (DOM not rendered yet)
  // On updates: May reference old element state
  if (inputEl.value) {
    console.log('Input value:', inputEl.value.value) // Stale!
    inputEl.value.focus()
  }
})
</script>

<template>
  <input ref="inputEl" v-model="text" />
</template>
```

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const items = ref([1, 2, 3])
const itemRefs = ref([])

// WRONG: Refs array not yet populated when this runs
watchEffect(() => {
  console.log('Number of refs:', itemRefs.value.length) // Always 0!
})
</script>

<template>
  <div v-for="item in items" :key="item" :ref="el => itemRefs.value.push(el)">
    {{ item }}
  </div>
</template>
```

**Correct:**
```vue
<script setup>
import { ref, watchEffect } from 'vue'

const inputEl = ref(null)
const text = ref('')

// CORRECT: flush: 'post' runs AFTER DOM update
watchEffect(() => {
  if (inputEl.value) {
    console.log('Input value:', inputEl.value.value) // Current!
    inputEl.value.focus()
  }
}, { flush: 'post' })
</script>

<template>
  <input ref="inputEl" v-model="text" />
</template>
```

```vue
<script setup>
import { ref, watchPostEffect } from 'vue'

const inputEl = ref(null)
const showInput = ref(true)

// CORRECT: watchPostEffect is shorthand for flush: 'post'
watchPostEffect(() => {
  if (inputEl.value) {
    inputEl.value.focus()
  }
})
</script>

<template>
  <input v-if="showInput" ref="inputEl" />
</template>
```

```vue
<script setup>
import { ref, watch, onMounted } from 'vue'

const inputEl = ref(null)

// ALTERNATIVE: Use watch on the ref directly
watch(inputEl, (el) => {
  if (el) {
    el.focus()
  }
}, { flush: 'post' })

// ALTERNATIVE: For one-time setup, onMounted is sufficient
onMounted(() => {
  inputEl.value?.focus()
})
</script>

<template>
  <input ref="inputEl" />
</template>
```

```vue
<script setup>
import { useTemplateRef, watchPostEffect } from 'vue'

// Vue 3.5+ with useTemplateRef
const input = useTemplateRef('my-input')

// CORRECT: watchPostEffect with useTemplateRef
watchPostEffect(() => {
  input.value?.focus()
})
</script>

<template>
  <input ref="my-input" />
</template>
```

## Flush Options Explained

```javascript
// Default: 'pre' - runs before DOM update
watchEffect(() => { ... }) // Same as { flush: 'pre' }

// 'post' - runs after DOM update (use for refs)
watchEffect(() => { ... }, { flush: 'post' })
watchPostEffect(() => { ... }) // Shorthand

// 'sync' - runs synchronously (rarely needed, can cause issues)
watchEffect(() => { ... }, { flush: 'sync' })
watchSyncEffect(() => { ... }) // Shorthand
```

## When to Use Each Flush Mode

| Scenario | Recommended Flush |
|----------|-------------------|
| Accessing template refs | `post` |
| Reading updated DOM | `post` |
| Triggering before render | `pre` (default) |
| Performance-critical sync updates | `sync` (with caution) |

## Reference
- [Vue.js Watchers - Callback Flush Timing](https://vuejs.org/guide/essentials/watchers.html#callback-flush-timing)
- [Vue.js watchEffect API](https://vuejs.org/api/reactivity-core.html#watcheffect)
```

## File: `skills/vue-jsx-best-practices/SKILL.md`
```markdown
---
name: vue-jsx-best-practices
description: JSX syntax in Vue (e.g., class vs className, JSX plugin config).
version: 2.0.0
license: MIT
author: github.com/vuejs-ai
---

Vue JSX best practices and differences from React JSX.

### JSX
- Migrating React JSX code to Vue or getting attribute type errors → See [render-function-jsx-vue-vs-react](reference/render-function-jsx-vue-vs-react.md)
```

## File: `skills/vue-jsx-best-practices/reference/render-function-jsx-vue-vs-react.md`
```markdown
---
title: Vue JSX Uses HTML Attributes Not React Conventions
impact: MEDIUM
impactDescription: Using className or htmlFor in Vue JSX causes TypeScript errors and inconsistent code style
type: gotcha
tags: [vue3, jsx, tsx, render-function]
---

# Vue JSX Uses HTML Attributes Not React Conventions

**Impact: MEDIUM** - Vue's JSX transform uses standard HTML attribute names (`class`, `for`) instead of React's JavaScript-friendly names (`className`, `htmlFor`). With proper TypeScript configuration, using React conventions like `className` or `htmlFor` will produce TypeScript errors, which is good for catching these inconsistencies early. Note that Vue's runtime is lenient and will actually convert these attributes correctly, but using HTML attributes is the recommended practice for consistency with Vue templates and proper type safety.

When writing JSX in Vue, use the same attribute names you would use in regular HTML templates. This is a fundamental difference from React's JSX where `class` and `for` are reserved JavaScript keywords.

## Task Checklist

- [ ] Use `class` instead of `className` in Vue JSX
- [ ] Use `for` instead of `htmlFor` in Vue JSX
- [ ] Use standard HTML event names with `on` prefix (onClick, onInput)
- [ ] When migrating React components to Vue, update all attribute names
- [ ] Configure TypeScript properly for Vue JSX type inference

**Incorrect (React-style):**
```jsx
// AVOID: React conventions cause TypeScript errors in Vue JSX
// (Vue runtime is lenient and converts these, but types don't allow them)
export default {
  setup() {
    return () => (
      <div className="container">
        <label htmlFor="email">Email:</label>
        <input id="email" className="input-field" />
      </div>
    )
  }
}
```

```tsx
// AVOID: TypeScript will reject className/htmlFor with Vue's JSX types
const Button = () => (
  <button
    className="btn btn-primary"  // TS error: Property 'className' does not exist
    htmlFor="form"               // TS error: Property 'htmlFor' does not exist
  >
    Submit
  </button>
)
```

**Correct (Vue-style):**
```jsx
// CORRECT: Use standard HTML attributes
export default {
  setup() {
    return () => (
      <div class="container">
        <label for="email">Email:</label>
        <input id="email" class="input-field" />
      </div>
    )
  }
}
```

```tsx
// CORRECT: Vue TSX with HTML attributes
const Button = () => (
  <button
    class="btn btn-primary"
  >
    Submit
  </button>
)
```

## TypeScript Configuration for Vue JSX

To enable proper type inference and IntelliSense for Vue JSX/TSX, configure your `tsconfig.json`:

```json
{
  "compilerOptions": {
    "jsx": "preserve",
    "jsxImportSource": "vue"
  }
}
```

Starting from Vue 3.4, Vue no longer implicitly registers the global JSX namespace, so `jsxImportSource` is required for TypeScript to use Vue's JSX type definitions.

## Vite Configuration

For Vite projects, ensure you have the JSX plugin configured in `vite.config.ts`:

```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

export default defineConfig({
  plugins: [vue(), vueJsx()]
})
```

## Other Attribute Differences

| React JSX | Vue JSX | HTML |
|-----------|---------|------|
| className | class | class |
| htmlFor | for | for |
| onChange | onInput (for live updates) | oninput |
| tabIndex | tabindex | tabindex |
| readOnly | readonly | readonly |

## Event Handling in Vue JSX

```jsx
// Vue JSX event handling
export default {
  setup() {
    const handleClick = () => console.log('clicked')
    const handleInput = (e) => console.log(e.target.value)

    return () => (
      <div>
        <button onClick={handleClick}>Click</button>
        <input onInput={handleInput} />

        {/* Event modifiers via helper */}
        <div onClick={withModifiers(handleClick, ['self'])}>
          Only triggers on self
        </div>
      </div>
    )
  }
}
```

## Reference
- [Vue.js JSX and TSX](https://vuejs.org/guide/extras/render-function.html#jsx-tsx)
```

## File: `skills/vue-options-api-best-practices/SKILL.md`
```markdown
---
name: vue-options-api-best-practices
description: "Vue 3 Options API style (data(), methods, this context). Each reference shows Options API solution only."
version: 2.0.0
license: MIT
author: github.com/vuejs-ai
---

Vue.js Options API best practices, TypeScript integration, and common gotchas.

### TypeScript
- Need to enable TypeScript type inference for component properties → See [ts-options-api-use-definecomponent](reference/ts-options-api-use-definecomponent.md)
- Enabling type safety for Options API this context → See [ts-strict-mode-options-api](reference/ts-strict-mode-options-api.md)
- Using old TypeScript versions with prop validators → See [ts-options-api-arrow-functions-validators](reference/ts-options-api-arrow-functions-validators.md)
- Event handler parameters need proper type safety → See [ts-options-api-type-event-handlers](reference/ts-options-api-type-event-handlers.md)
- Need to type object or array props with interfaces → See [ts-options-api-proptype-complex-types](reference/ts-options-api-proptype-complex-types.md)
- Injected properties missing TypeScript types completely → See [ts-options-api-provide-inject-limitations](reference/ts-options-api-provide-inject-limitations.md)
- Complex computed properties lack clear type documentation → See [ts-options-api-computed-return-types](reference/ts-options-api-computed-return-types.md)

### Methods & Lifecycle
- Methods aren't binding to component instance context → See [no-arrow-functions-in-methods](reference/no-arrow-functions-in-methods.md)
- Lifecycle hooks losing access to component data → See [no-arrow-functions-in-lifecycle-hooks](reference/no-arrow-functions-in-lifecycle-hooks.md)
- Debounced functions sharing state across component instances → See [stateful-methods-lifecycle](reference/stateful-methods-lifecycle.md)
```

## File: `skills/vue-options-api-best-practices/reference/no-arrow-functions-in-lifecycle-hooks.md`
```markdown
---
title: Never Use Arrow Functions for Options API Lifecycle Hooks
impact: HIGH
impactDescription: Arrow functions in lifecycle hooks break `this` binding to component instance
type: capability
tags: [vue3, vue2, options-api, lifecycle, arrow-functions, this-binding, mounted, created]
---

# Never Use Arrow Functions for Options API Lifecycle Hooks

**Impact: HIGH** - Using arrow functions for lifecycle hooks in the Options API prevents Vue from binding `this` to the component instance. This causes `this` to be `undefined` or reference the wrong context, leading to runtime errors when accessing component data, methods, or other properties.

Arrow functions lexically bind `this` from their enclosing scope. Vue's Options API lifecycle hooks (created, mounted, updated, unmounted, etc.) require regular functions so Vue can set `this` to the component instance at runtime.

## Task Checklist

- [ ] Always use regular function syntax for Options API lifecycle hooks
- [ ] Use ES6 method shorthand (preferred) for cleaner code
- [ ] Arrow functions ARE allowed inside lifecycle hooks for callbacks

**Incorrect:**
```javascript
export default {
  data() {
    return { message: 'Hello' }
  },
  // WRONG: Arrow function - `this` will be undefined
  created: () => {
    console.log(this.message) // Error: Cannot read property 'message' of undefined
  },
  // WRONG: Arrow function for mounted
  mounted: () => {
    this.initializePlugin() // Error: this.initializePlugin is not a function
  },
  // WRONG: Arrow function for beforeUnmount
  beforeUnmount: () => {
    this.cleanup() // Will fail!
  },
  methods: {
    initializePlugin() { /* ... */ },
    cleanup() { /* ... */ }
  }
}
```

**Correct:**
```javascript
export default {
  data() {
    return { message: 'Hello' }
  },
  // CORRECT: ES6 method shorthand (preferred)
  created() {
    console.log(this.message) // Works! this refers to component instance
  },
  // CORRECT: Regular function expression
  mounted: function() {
    this.initializePlugin() // Works!
  },
  // CORRECT: Method shorthand
  beforeUnmount() {
    this.cleanup() // Works!
  },
  methods: {
    initializePlugin() {
      // Arrow functions ARE fine for callbacks inside lifecycle hooks
      this.$nextTick(() => {
        this.isReady = true // Arrow inherits `this` from mounted
      })
    },
    cleanup() { /* ... */ }
  }
}
```

## All Affected Lifecycle Hooks

The following Options API hooks must NOT use arrow functions:
- `beforeCreate`
- `created`
- `beforeMount`
- `mounted`
- `beforeUpdate`
- `updated`
- `beforeUnmount` (Vue 3) / `beforeDestroy` (Vue 2)
- `unmounted` (Vue 3) / `destroyed` (Vue 2)
- `activated`
- `deactivated`
- `errorCaptured`
- `renderTracked`
- `renderTriggered`

## Reference
- [Vue.js Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)
- [Vue.js Options Lifecycle](https://vuejs.org/api/options-lifecycle.html)
```

## File: `skills/vue-options-api-best-practices/reference/no-arrow-functions-in-methods.md`
```markdown
---
title: Never Use Arrow Functions in Methods Option
impact: HIGH
impactDescription: Arrow functions prevent Vue from binding `this` to the component instance
type: capability
tags: [vue3, vue2, options-api, methods, this-binding]
---

# Never Use Arrow Functions in Methods Option

**Impact: HIGH** - Using arrow functions in the `methods` option causes `this` to be `undefined` or the wrong context, leading to runtime errors when trying to access component data, computed properties, or other methods.

Arrow functions lexically bind `this` from their enclosing scope, not from the object they're defined on. Vue's `methods` option requires regular functions so Vue can bind `this` to the component instance.

## Task Checklist

- [ ] Always use regular function syntax for methods in Options API
- [ ] If using ES6 shorthand, use method shorthand (preferred)
- [ ] Arrow functions ARE allowed inside methods for callbacks

**Incorrect:**
```javascript
export default {
  data() {
    return { count: 0 }
  },
  methods: {
    // WRONG: Arrow function - `this` will be undefined
    increment: () => {
      this.count++ // Error: Cannot read property 'count' of undefined
    },
    // WRONG: Arrow function assigned to property
    decrement: () => {
      this.count--
    }
  }
}
```

**Correct:**
```javascript
export default {
  data() {
    return { count: 0 }
  },
  methods: {
    // CORRECT: ES6 method shorthand (preferred)
    increment() {
      this.count++ // Works! this refers to component instance
    },
    // CORRECT: Traditional function expression
    decrement: function() {
      this.count--
    },
    // Arrow functions ARE fine for callbacks INSIDE methods
    fetchData() {
      fetch('/api/data')
        .then(response => response.json())
        .then(data => {
          this.data = data // Arrow function inherits `this` from fetchData
        })
    }
  }
}
```

## Reference
- [Vue.js Methods - Avoid Arrow Functions](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#methods)
```

## File: `skills/vue-options-api-best-practices/reference/stateful-methods-lifecycle.md`
```markdown
---
title: Create Stateful Methods in Lifecycle Hooks
impact: MEDIUM
impactDescription: Stateful functions like debounce/throttle in methods are shared across all component instances
type: capability
tags: [vue3, options-api, debounce, throttle, lifecycle, cleanup]
---

# Create Stateful Methods in Lifecycle Hooks

**Impact: MEDIUM** - If you define debounced, throttled, or other stateful functions directly in the `methods` option, all instances of the component share the same function state. This causes race conditions and bugs in lists of components.

When a component is reused (e.g., in v-for), each instance needs its own debounced/throttled function. Define these in the `created()` hook and clean them up in `unmounted()` to prevent memory leaks.

## Task Checklist

- [ ] Never define debounced/throttled functions directly in `methods`
- [ ] Create stateful functions in `created()` lifecycle hook
- [ ] Always clean up (cancel timers) in `unmounted()`

**Incorrect:**
```javascript
import { debounce } from 'lodash-es'

export default {
  methods: {
    // WRONG: All component instances share this debounced function!
    // If used in a v-for, clicking one button affects all instances
    handleClick: debounce(function() {
      this.performSearch()
    }, 500)
  }
}
```

**Correct:**
```javascript
import { debounce } from 'lodash-es'

export default {
  created() {
    // CORRECT: Each instance gets its own debounced function
    this.debouncedSearch = debounce(this.performSearch, 500)
  },
  unmounted() {
    // CORRECT: Clean up to prevent memory leaks and stale calls
    this.debouncedSearch.cancel()
  },
  methods: {
    handleClick() {
      this.debouncedSearch()
    },
    performSearch() {
      // Actual search logic
    }
  }
}
```

## Reference
- [Vue.js Reactivity Fundamentals - Stateful Methods](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#stateful-methods)
```

## File: `skills/vue-options-api-best-practices/reference/ts-options-api-arrow-functions-validators.md`
```markdown
---
title: Use Arrow Functions for Prop Validators in TypeScript < 4.7
impact: HIGH
impactDescription: Regular functions in prop validators can break type inference for the entire component in TypeScript versions before 4.7
type: gotcha
tags: [vue3, typescript, options-api, props, type-inference, defineComponent, legacy]
---

# Use Arrow Functions for Prop Validators in TypeScript < 4.7

> **LEGACY CONCERN:** This issue was fixed in TypeScript 4.7 (released May 2022). Most modern projects using TypeScript 4.7+ do not need this workaround. If you're starting a new project or have upgraded TypeScript recently, you can safely use regular functions in prop validators. This rule is primarily relevant for legacy codebases still running TypeScript < 4.7.

**Impact: HIGH** - If your TypeScript version is less than 4.7, using regular functions for `validator` and `default` prop options can cause TypeScript to fail when inferring the type of `this`, which breaks type inference for the ENTIRE component, not just the prop.

## Task Checklist

- [ ] Check your TypeScript version (`tsc --version`)
- [ ] If TypeScript < 4.7, use arrow functions for all `validator` and `default` prop options
- [ ] Consider upgrading to TypeScript 4.7+ to avoid this limitation entirely

## The Problem

TypeScript needs to infer the type of `this` inside regular functions. In Vue's Options API context, this inference can fail in versions before 4.7, causing cascading type inference failures.

**BAD - Can break type inference in TS < 4.7:**
```typescript
import { defineComponent, PropType } from 'vue'

interface Book {
  title: string
  author: string
  year: number
}

export default defineComponent({
  props: {
    book: {
      type: Object as PropType<Book>,
      required: true,
      // Regular function - causes inference issues in TS < 4.7
      validator: function(book: Book) {
        return book.title.length > 0
      }
    },
    count: {
      type: Number,
      // Regular function - causes inference issues in TS < 4.7
      default: function() {
        return 0
      }
    }
  },
  // Type inference for computed, methods, etc. may break!
  computed: {
    bookTitle() {
      // 'this' might be typed as 'any' due to broken inference
      return this.book.title
    }
  }
})
```

**GOOD - Use arrow functions:**
```typescript
import { defineComponent, PropType } from 'vue'

interface Book {
  title: string
  author: string
  year: number
}

export default defineComponent({
  props: {
    book: {
      type: Object as PropType<Book>,
      required: true,
      // Arrow function - safe for all TS versions
      validator: (book: Book) => book.title.length > 0
    },
    count: {
      type: Number,
      // Arrow function - safe for all TS versions
      default: () => 0
    }
  },
  computed: {
    bookTitle() {
      // 'this' is properly typed
      return this.book.title  // Type: string
    }
  }
})
```

## Why Arrow Functions Work

Arrow functions don't have their own `this` binding, so TypeScript doesn't need to infer a `this` type for them. This avoids the type inference bug that affects regular functions in older TypeScript versions.

## For Object/Array Default Values

Arrow functions are especially important for object and array defaults (which Vue requires to be functions anyway):

```typescript
props: {
  config: {
    type: Object as PropType<Config>,
    // Must be a function, use arrow syntax
    default: () => ({
      enabled: true,
      maxItems: 10
    })
  },
  tags: {
    type: Array as PropType<string[]>,
    // Must be a function, use arrow syntax
    default: () => []
  }
}
```

## When You Can Ignore This

- **TypeScript 4.7+**: This issue was fixed in TypeScript 4.7 (May 2022). If your project uses 4.7 or later, regular functions work fine. Since TypeScript 4.7 has been available for over 3 years, most actively maintained projects have already upgraded and do not need this workaround.
- **New projects**: If you're starting a new Vue project in 2024 or later, you'll almost certainly be using TypeScript 4.7+ by default and can ignore this rule entirely.
- **Arrow functions are still fine**: While not required in modern TypeScript, using arrow functions for validators and defaults remains a valid stylistic choice and causes no issues.

## Checking Your TypeScript Version

```bash
# Check installed TypeScript version
npx tsc --version

# Or check package.json
grep typescript package.json
```

## Reference

- [Vue.js TypeScript with Options API](https://vuejs.org/guide/typescript/options-api.html#caveats)
- [TypeScript 4.7 Release Notes](https://devblogs.microsoft.com/typescript/announcing-typescript-4-7/)
```

## File: `skills/vue-options-api-best-practices/reference/ts-options-api-computed-return-types.md`
```markdown
---
title: Explicitly Annotate Computed Property Return Types
impact: LOW
impactDescription: While Vue usually infers computed types correctly, explicit annotations prevent circular inference issues and improve code documentation
type: best-practice
tags: [vue3, typescript, options-api, computed, type-inference]
---

# Explicitly Annotate Computed Property Return Types

**Impact: LOW** - Vue can usually infer computed property return types automatically. However, explicit return type annotations prevent edge cases involving circular inference loops and serve as documentation for complex computed properties.

## Task Checklist

- [ ] Consider adding return types to computed properties, especially complex ones
- [ ] Always add return types when TypeScript inference fails or shows incorrect types
- [ ] Add return types for writable computed properties (getter and setter)

## When Explicit Types Are Helpful

### 1. Complex Computed Properties

```typescript
import { defineComponent } from 'vue'

interface CartItem {
  id: number
  name: string
  price: number
  quantity: number
}

export default defineComponent({
  data() {
    return {
      items: [] as CartItem[],
      discountPercent: 10
    }
  },
  computed: {
    // Without annotation - works but intent unclear
    cartSummary() {
      return {
        subtotal: this.items.reduce((sum, item) => sum + item.price * item.quantity, 0),
        itemCount: this.items.reduce((sum, item) => sum + item.quantity, 0)
      }
    },

    // With annotation - clear intent, documented type
    cartSummaryTyped(): { subtotal: number; itemCount: number; discount: number; total: number } {
      const subtotal = this.items.reduce((sum, item) => sum + item.price * item.quantity, 0)
      const discount = subtotal * (this.discountPercent / 100)
      return {
        subtotal,
        itemCount: this.items.reduce((sum, item) => sum + item.quantity, 0),
        discount,
        total: subtotal - discount
      }
    }
  }
})
```

### 2. Circular Inference Issues

Sometimes computed properties that reference each other can cause TypeScript inference to fail:

```typescript
export default defineComponent({
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe'
    }
  },
  computed: {
    // Explicit return type breaks potential circular inference
    fullName(): string {
      return `${this.firstName} ${this.lastName}`
    },

    // References fullName - explicit type prevents inference issues
    greeting(): string {
      return `Hello, ${this.fullName}!`
    }
  }
})
```

### 3. Writable Computed Properties

Always annotate writable computed properties for clarity:

```typescript
export default defineComponent({
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe'
    }
  },
  computed: {
    // Writable computed - explicit types for getter and setter
    fullName: {
      get(): string {
        return `${this.firstName} ${this.lastName}`
      },
      set(newValue: string) {
        const parts = newValue.split(' ')
        this.firstName = parts[0] || ''
        this.lastName = parts.slice(1).join(' ') || ''
      }
    }
  }
})
```

## When You Can Skip Explicit Types

Simple computed properties that TypeScript infers correctly:

```typescript
computed: {
  // Simple string - TypeScript infers correctly
  upperName() {
    return this.name.toUpperCase()
  },

  // Simple boolean - TypeScript infers correctly
  isEmpty() {
    return this.items.length === 0
  },

  // Simple number - TypeScript infers correctly
  totalCount() {
    return this.items.length
  }
}
```

## Interface for Complex Return Types

For complex computed return types, define interfaces:

```typescript
interface PaginationInfo {
  currentPage: number
  totalPages: number
  hasNext: boolean
  hasPrev: boolean
  pageItems: Item[]
}

export default defineComponent({
  computed: {
    pagination(): PaginationInfo {
      const totalPages = Math.ceil(this.items.length / this.pageSize)
      const start = (this.currentPage - 1) * this.pageSize

      return {
        currentPage: this.currentPage,
        totalPages,
        hasNext: this.currentPage < totalPages,
        hasPrev: this.currentPage > 1,
        pageItems: this.items.slice(start, start + this.pageSize)
      }
    }
  }
})
```

## Debugging Type Inference

If you're unsure what TypeScript infers, hover over the computed property in your IDE, or add a temporary annotation to see errors:

```typescript
computed: {
  // Hover over 'mystery' in IDE to see inferred type
  mystery() {
    return this.someComplexCalculation()
  },

  // Or add annotation to verify
  mystery(): ExpectedType {  // Error if inference differs
    return this.someComplexCalculation()
  }
}
```

## Reference

- [Vue.js TypeScript with Options API - Typing Computed Properties](https://vuejs.org/guide/typescript/options-api.html#typing-computed-properties)
```

## File: `skills/vue-options-api-best-practices/reference/ts-options-api-proptype-complex-types.md`
```markdown
---
title: Use PropType for Complex Prop Types in Options API
impact: MEDIUM
impactDescription: Vue's runtime prop types cannot express complex TypeScript types without PropType, leading to 'any' type inference
type: best-practice
tags: [vue3, typescript, options-api, props, PropType, type-safety]
---

# Use PropType for Complex Prop Types in Options API

**Impact: MEDIUM** - Vue's runtime `props` option only supports basic constructor functions (String, Number, etc.). To type complex props like interfaces, function signatures, or union types, you must use Vue's `PropType` utility type.

## Task Checklist

- [ ] Import `PropType` from 'vue' for complex prop types
- [ ] Use `as PropType<YourType>` after `Object`, `Array`, or `Function`
- [ ] Define interfaces for your complex types
- [ ] Remember: PropType is purely for TypeScript - runtime validation only checks the constructor

## The Problem

Vue's runtime prop system uses JavaScript constructor functions, which can't express complex TypeScript types:

```typescript
// What runtime props support:
props: {
  name: String,       // OK: string
  count: Number,      // OK: number
  enabled: Boolean,   // OK: boolean
  items: Array,       // Problem: any[]
  config: Object,     // Problem: Record<string, any>
  handler: Function   // Problem: (...args: any[]) => any
}
```

## Using PropType for Complex Types

**Import and use PropType:**
```typescript
import { defineComponent, PropType } from 'vue'
// or
import type { PropType } from 'vue'

interface User {
  id: number
  name: string
  email: string
}

interface Config {
  theme: 'light' | 'dark'
  maxItems: number
}

export default defineComponent({
  props: {
    // Object with interface
    user: {
      type: Object as PropType<User>,
      required: true
    },

    // Array of typed items
    users: {
      type: Array as PropType<User[]>,
      default: () => []
    },

    // Object with union type
    config: {
      type: Object as PropType<Config>,
      default: () => ({ theme: 'light', maxItems: 10 })
    },

    // Typed function
    onSubmit: {
      type: Function as PropType<(data: User) => Promise<void>>,
      required: true
    },

    // Union of primitives
    id: {
      type: [String, Number] as PropType<string | number>,
      required: true
    },

    // Literal union type
    status: {
      type: String as PropType<'pending' | 'active' | 'completed'>,
      default: 'pending'
    }
  },

  methods: {
    async handleSubmit() {
      // Full type inference!
      await this.onSubmit(this.user)  // onSubmit is properly typed
      console.log(this.user.email)    // user.email is string
      console.log(this.config.theme)  // theme is 'light' | 'dark'
    }
  }
})
```

## Important: Runtime vs Compile-Time

PropType only affects TypeScript compilation. At runtime, Vue still only validates using the constructor:

```typescript
props: {
  user: {
    type: Object as PropType<User>,
    required: true
  }
}

// Runtime: Vue only checks typeof value === 'object'
// It does NOT validate { id, name, email } structure

// To add runtime validation, use validator:
props: {
  user: {
    type: Object as PropType<User>,
    required: true,
    validator: (user: User) => {
      return typeof user.id === 'number' &&
             typeof user.name === 'string' &&
             typeof user.email === 'string'
    }
  }
}
```

## Common PropType Patterns

### Nullable Props

```typescript
props: {
  // Optional object that can be null
  selectedItem: {
    type: Object as PropType<Item | null>,
    default: null
  }
}
```

### Enum-like Props

```typescript
type ButtonVariant = 'primary' | 'secondary' | 'danger'

props: {
  variant: {
    type: String as PropType<ButtonVariant>,
    default: 'primary',
    validator: (v: ButtonVariant) =>
      ['primary', 'secondary', 'danger'].includes(v)
  }
}
```

### Generic-like Props with Multiple Types

```typescript
props: {
  // Accept string, number, or object with id
  value: {
    type: [String, Number, Object] as PropType<string | number | { id: string }>,
    required: true
  }
}
```

### Event Handler Props

```typescript
interface ClickEventData {
  item: Item
  index: number
}

props: {
  onClick: {
    type: Function as PropType<(data: ClickEventData) => void>,
    required: false
  }
}
```

## Why Not Just Use `as`?

You might think to skip `PropType`:

```typescript
// WRONG - doesn't work as expected
props: {
  user: Object as User  // TypeScript error or incorrect inference
}

// CORRECT - use PropType
props: {
  user: Object as PropType<User>
}
```

`PropType<T>` is specifically designed to work with Vue's prop type system.

## Reference

- [Vue.js TypeScript with Options API - Typing Component Props](https://vuejs.org/guide/typescript/options-api.html#typing-component-props)
- [Vue.js Props Documentation](https://vuejs.org/guide/components/props.html)
```

## File: `skills/vue-options-api-best-practices/reference/ts-options-api-provide-inject-limitations.md`
```markdown
---
title: Provide/Inject Has Limited Type Inference in Options API
impact: MEDIUM
impactDescription: Injected properties in Options API are not automatically typed, requiring manual type assertions or type augmentation
type: gotcha
tags: [vue3, typescript, options-api, provide-inject, type-safety]
---

# Provide/Inject Has Limited Type Inference in Options API

**Impact: MEDIUM** - When using `provide/inject` with the Options API and TypeScript, injected properties won't be automatically typed. TypeScript will show errors that the property doesn't exist on the component, even though it works at runtime.

## Task Checklist

- [ ] Be aware that Options API inject has limited type support
- [ ] Use type augmentation to add types to injected values
- [ ] Consider using typed computed wrappers for injected values

## The Problem

```typescript
// Provider component (parent)
import { defineComponent } from 'vue'

export default defineComponent({
  provide() {
    return {
      theme: 'dark',
      user: { id: 1, name: 'John' }
    }
  }
})
```

```typescript
// Consumer component (child) - Options API
import { defineComponent } from 'vue'

export default defineComponent({
  inject: ['theme', 'user'],

  mounted() {
    // TypeScript Error: Property 'theme' does not exist on type...
    console.log(this.theme)

    // TypeScript Error: Property 'user' does not exist on type...
    console.log(this.user.name)
  }
})
```

## Solution 1: Type Augmentation

Augment the component type to include injected properties:

```typescript
// types/injections.d.ts
import 'vue'

declare module 'vue' {
  interface ComponentCustomProperties {
    theme: 'light' | 'dark'
    user: { id: number; name: string }
  }
}

export {}
```

```typescript
// Consumer component - now typed
import { defineComponent } from 'vue'

export default defineComponent({
  inject: ['theme', 'user'],

  mounted() {
    // Now works - typed from ComponentCustomProperties
    console.log(this.theme)  // 'light' | 'dark'
    console.log(this.user.name)  // string
  }
})
```

**Note**: This adds types globally to ALL components, not just those that inject these values.

## Solution 2: Typed Computed Wrappers

Use the object syntax with computed property wrappers for type safety:

```typescript
import { defineComponent } from 'vue'

interface User {
  id: number
  name: string
}

export default defineComponent({
  inject: {
    theme: {
      from: 'theme',
      default: 'light'
    },
    user: {
      from: 'user',
      default: () => ({ id: 0, name: 'Guest' })
    }
  },

  computed: {
    // Type via computed wrapper
    typedTheme(): 'light' | 'dark' {
      return this.theme as 'light' | 'dark'
    },
    typedUser(): User {
      return this.user as User
    }
  },

  mounted() {
    console.log(this.typedTheme)
    console.log(this.typedUser.name)
  }
})
```

## Why This Happens

The Options API `inject` array syntax `inject: ['theme']` doesn't provide type information to TypeScript. Vue knows about the injection at runtime, but TypeScript's static analysis can't trace the provide/inject relationship across components.

## Reference

- [Vue.js Provide/Inject](https://vuejs.org/guide/components/provide-inject.html)
- [GitHub Issue: Add type inference to Options API provide/inject](https://github.com/vuejs/core/issues/3031)
```

## File: `skills/vue-options-api-best-practices/reference/ts-options-api-type-event-handlers.md`
```markdown
---
title: Explicitly Type Event Handlers in Options API Methods
impact: MEDIUM
impactDescription: Untyped event handler arguments default to 'any', missing type errors and losing IDE support for DOM event properties
type: best-practice
tags: [vue3, typescript, options-api, events, type-safety, DOM]
---

# Explicitly Type Event Handlers in Options API Methods

**Impact: MEDIUM** - Without explicit type annotations, event handler parameters in Options API methods are typed as `any`. This defeats TypeScript's purpose, causing `noImplicitAny` errors in strict mode and losing type safety for DOM event properties.

## Task Checklist

- [ ] Always add type annotations to event handler method parameters
- [ ] Use the correct DOM event type (Event, MouseEvent, KeyboardEvent, etc.)
- [ ] Use type assertions for event.target when accessing element-specific properties
- [ ] Enable `strict: true` in tsconfig.json to catch implicit any errors

## The Problem

```typescript
import { defineComponent } from 'vue'

export default defineComponent({
  methods: {
    // BAD - 'event' is implicitly 'any'
    handleClick(event) {
      console.log(event.target.value)  // No type checking!
    },

    // BAD - Causes error with noImplicitAny
    handleInput(event) {
      // Error: Parameter 'event' implicitly has an 'any' type
      this.searchTerm = event.target.value
    }
  }
})
```

## The Solution: Explicit Event Types

```typescript
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      searchTerm: ''
    }
  },
  methods: {
    // GOOD - Explicit Event type
    handleClick(event: MouseEvent) {
      console.log(event.clientX, event.clientY)
      // Cast target for element-specific properties
      const button = event.target as HTMLButtonElement
      console.log(button.disabled)
    },

    // GOOD - Explicit Event type with target assertion
    handleInput(event: Event) {
      const input = event.target as HTMLInputElement
      this.searchTerm = input.value
    },

    // GOOD - KeyboardEvent for keyboard handlers
    handleKeydown(event: KeyboardEvent) {
      if (event.key === 'Enter') {
        this.submit()
      }
    }
  }
})
```

## Common DOM Event Types

| Event Type | Use For |
|------------|---------|
| `Event` | Generic events, custom events |
| `MouseEvent` | click, dblclick, mouseenter, mouseleave, etc. |
| `KeyboardEvent` | keydown, keyup, keypress |
| `InputEvent` | input (modern browsers) |
| `FocusEvent` | focus, blur |
| `SubmitEvent` | form submit |
| `DragEvent` | drag, drop, dragenter, dragover |
| `TouchEvent` | touchstart, touchend, touchmove |
| `WheelEvent` | wheel |

## Type Assertions for event.target

`event.target` is typed as `EventTarget | null`, which is too generic. Use type assertions:

```typescript
methods: {
  // Input element
  onInputChange(event: Event) {
    const target = event.target as HTMLInputElement
    console.log(target.value)
    console.log(target.checked)  // for checkboxes
  },

  // Select element
  onSelectChange(event: Event) {
    const target = event.target as HTMLSelectElement
    console.log(target.value)
    console.log(target.selectedIndex)
  },

  // Form element
  onFormSubmit(event: SubmitEvent) {
    event.preventDefault()
    const form = event.target as HTMLFormElement
    const formData = new FormData(form)
  },

  // Using currentTarget (often more reliable)
  onButtonClick(event: MouseEvent) {
    // currentTarget is the element the handler is attached to
    const button = event.currentTarget as HTMLButtonElement
    console.log(button.dataset.id)
  }
}
```

## Template Usage

```vue
<template>
  <div>
    <!-- Mouse events -->
    <button @click="handleClick">Click me</button>

    <!-- Input events -->
    <input @input="handleInput" @keydown="handleKeydown" />

    <!-- Form events -->
    <form @submit.prevent="handleSubmit">
      <button type="submit">Submit</button>
    </form>
  </div>
</template>
```

## With Custom Component Events

For custom component events, type based on what the component emits:

```typescript
methods: {
  // Child emits: emit('update', { id: number, value: string })
  handleChildUpdate(payload: { id: number; value: string }) {
    console.log(payload.id, payload.value)
  },

  // Child emits primitive: emit('change', newValue)
  handleValueChange(newValue: number) {
    this.count = newValue
  }
}
```

## Generic Event Handler Pattern

For reusable handlers:

```typescript
methods: {
  // Generic handler that works with any input
  updateField<T extends HTMLInputElement | HTMLTextAreaElement>(
    field: keyof typeof this.$data,
    event: Event
  ) {
    const target = event.target as T
    ;(this as any)[field] = target.value
  }
}
```

## Why currentTarget vs target?

- **target**: The element that triggered the event (could be a child)
- **currentTarget**: The element the event listener is attached to

```typescript
methods: {
  // If button contains <span>Click</span>, clicking the span:
  // - event.target = span
  // - event.currentTarget = button
  handleClick(event: MouseEvent) {
    // Use currentTarget when you want the handler's element
    const button = event.currentTarget as HTMLButtonElement
  }
}
```

## Reference

- [Vue.js TypeScript with Options API - Typing Event Handlers](https://vuejs.org/guide/typescript/options-api.html#typing-event-handlers)
- [MDN Event Interface](https://developer.mozilla.org/en-US/docs/Web/API/Event)
- [TypeScript DOM Types](https://github.com/microsoft/TypeScript/blob/main/lib/lib.dom.d.ts)
```

## File: `skills/vue-options-api-best-practices/reference/ts-options-api-use-definecomponent.md`
```markdown
---
title: Always Use defineComponent for TypeScript Type Inference
impact: HIGH
impactDescription: Without defineComponent, TypeScript cannot infer types for props, computed properties, methods, or the 'this' context in Options API components
type: best-practice
tags: [vue3, typescript, options-api, defineComponent, type-inference]
---

# Always Use defineComponent for TypeScript Type Inference

**Impact: HIGH** - When using TypeScript with Vue's Options API, you MUST wrap your component definition with `defineComponent()` to enable proper type inference. Without it, `this` is typed as `any`, losing all TypeScript benefits.

## Task Checklist

- [ ] Always import and use `defineComponent` from 'vue' for Options API components
- [ ] Enable `strict: true` (or at minimum `noImplicitThis: true`) in tsconfig.json
- [ ] Consider migrating to Composition API with `<script setup>` for better type inference

## The Problem

Vue's Options API relies heavily on the `this` context, which TypeScript cannot automatically type without `defineComponent`:

**BAD - No type inference:**
```typescript
// No defineComponent - 'this' is typed as 'any'
export default {
  props: {
    message: String
  },
  computed: {
    // 'this' is 'any' - no type checking!
    greeting() {
      return this.message + '!'  // No type inference
    }
  },
  methods: {
    // 'this' is 'any' - mistakes won't be caught
    handleClick() {
      console.log(this.mesage)  // Typo not caught!
    }
  }
}
```

**GOOD - Full type inference:**
```typescript
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    message: {
      type: String,
      required: true
    },
    count: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      localState: ''
    }
  },
  computed: {
    // 'this.message' is typed as string
    // 'this.count' is typed as number
    greeting(): string {
      return this.message + '!'
    }
  },
  methods: {
    handleClick() {
      console.log(this.mesage)  // Error: Property 'mesage' does not exist
      console.log(this.message)  // OK: string
    }
  }
})
```

## What defineComponent Enables

1. **Props type inference**: Vue infers types from `type`, `required`, and `default`
2. **`this` context typing**: All options (data, computed, methods) are properly typed
3. **Cross-option references**: Access data in methods, computed properties, etc. with full types
4. **IDE autocompletion**: Get suggestions for all component properties and methods

## TypeScript Configuration Required

For proper `this` type checking, enable strict mode or at minimum `noImplicitThis`:

```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    // Or at minimum:
    "noImplicitThis": true
  }
}
```

Without this, TypeScript allows implicit `any` for `this`, defeating the purpose of using `defineComponent`.

## defineComponent is a No-Op at Runtime

`defineComponent` does nothing at runtime - it simply returns the object you pass to it. Its only purpose is to help TypeScript infer types:

```typescript
// At runtime, this is equivalent to:
// export default { props: { ... }, ... }
export default defineComponent({
  props: { /* ... */ }
})
```

This means there's zero runtime cost to using `defineComponent`.

## When to Use defineComponent vs script setup

| Approach | Use Case |
|----------|----------|
| `defineComponent` | Options API, Class-based migration, JSX/TSX components |
| `<script setup>` | New components, better type inference, less boilerplate |

**Official recommendation**: "While Vue does support TypeScript usage with Options API, it is recommended to use Vue with TypeScript via Composition API as it offers simpler, more efficient and more robust type inference."

## With Vue Single-File Components

```vue
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MyComponent',
  props: {
    title: {
      type: String,
      required: true
    }
  },
  computed: {
    upperTitle(): string {
      return this.title.toUpperCase()
    }
  }
})
</script>

<template>
  <h1>{{ upperTitle }}</h1>
</template>
```

## Common Mistake: Missing defineComponent

This often happens when copying JavaScript components to TypeScript:

```typescript
// Copied from JS - MISSING defineComponent!
export default {
  name: 'MyComponent',
  // ... entire component without type inference
}
```

Always add `defineComponent` when converting to TypeScript.

## Reference

- [Vue.js TypeScript with Options API](https://vuejs.org/guide/typescript/options-api.html)
- [Vue.js Using Vue with TypeScript](https://vuejs.org/guide/typescript/overview.html)
```

## File: `skills/vue-options-api-best-practices/reference/ts-strict-mode-options-api.md`
```markdown
---
title: Enable strict Mode for Proper Options API TypeScript Support
impact: HIGH
impactDescription: Without strict mode, 'this' in Options API components is typed as 'any', losing all type safety
type: gotcha
tags: [typescript, options-api, tsconfig, this-typing, configuration]
---

# Enable strict Mode for Proper Options API TypeScript Support

**Impact: HIGH** - Without `strict: true` (or at minimum `noImplicitThis: true`) in your tsconfig.json, the `this` context in Options API components is typed as `any`. This silently disables type checking for all property access on component instances.

## Task Checklist

- [ ] Enable `strict: true` in tsconfig.json (recommended)
- [ ] Or enable `noImplicitThis: true` at minimum
- [ ] Wrap components with `defineComponent()` for proper inference
- [ ] Verify type errors appear when accessing non-existent properties

## The Problem

TypeScript's default behavior without strict mode allows implicit `any` typing, which defeats the purpose of using TypeScript with Vue's Options API.

**tsconfig.json without strict mode:**
```json
{
  "compilerOptions": {
    "target": "ES2020"
    // No strict mode - this is DANGEROUS
  }
}
```

**Component with hidden type errors:**
```typescript
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      count: 0,
      message: 'Hello'
    }
  },
  methods: {
    increment() {
      // Without strict mode, these errors are SILENT:
      this.cont++          // Typo: should be 'count'
      this.nonExistent     // Property doesn't exist
      this.message.toFixed() // Wrong method for string
    }
  }
})
```

All of the above errors compile successfully without strict mode because `this` is implicitly `any`.

## Correct Configuration

**Recommended tsconfig.json:**
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "jsx": "preserve",
    "isolatedModules": true
  }
}
```

**Minimum for Options API type safety:**
```json
{
  "compilerOptions": {
    "noImplicitThis": true
  }
}
```

## What strict Mode Enables

The `strict` flag is a shorthand for enabling multiple type-checking options:

| Option | Effect |
|--------|--------|
| `noImplicitThis` | Errors on `this` with implicit `any` type |
| `noImplicitAny` | Errors on expressions with implicit `any` type |
| `strictNullChecks` | null and undefined are distinct types |
| `strictFunctionTypes` | Stricter function parameter checking |
| `strictPropertyInitialization` | Class properties must be initialized |
| `strictBindCallApply` | Stricter bind, call, apply typing |
| `alwaysStrict` | Emits "use strict" in output |

## Correct Component with Proper Typing

```typescript
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      count: 0,
      message: 'Hello'
    }
  },
  computed: {
    doubleCount(): number {
      return this.count * 2  // 'this.count' is typed as number
    }
  },
  methods: {
    increment() {
      this.count++           // Type-safe: count is number
      // this.cont++         // ERROR: Property 'cont' does not exist
    },
    greet(name: string) {
      return `${this.message}, ${name}!`  // Type-safe
    }
  }
})
```

## Common Errors After Enabling Strict Mode

### Error: Property 'xxx' does not exist

```typescript
// Before: worked silently
this.unknownProp

// After: TypeScript error
// Property 'unknownProp' does not exist on type 'ComponentPublicInstance<...>'
```

Fix by adding the property to `data()` or declaring it properly.

### Error: Object is possibly 'undefined'

```typescript
methods: {
  getFirst() {
    const items = this.items
    // Error: Object is possibly 'undefined'
    return items[0].name
  }
}
```

Fix with proper null checks:
```typescript
methods: {
  getFirst() {
    return this.items?.[0]?.name
  }
}
```

## Important: defineComponent is Required

Even with strict mode, you must use `defineComponent()` to enable proper type inference:

```typescript
// BAD - No type inference for 'this'
export default {
  data() {
    return { count: 0 }
  },
  methods: {
    increment() {
      this.count++  // 'this' is any even with strict mode!
    }
  }
}

// GOOD - Full type inference
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return { count: 0 }
  },
  methods: {
    increment() {
      this.count++  // 'this.count' is properly typed as number
    }
  }
})
```

## Reference

- [Vue.js TypeScript Overview - tsconfig.json](https://vuejs.org/guide/typescript/overview.html#configuring-tsconfig-json)
- [Vue.js TypeScript with Options API](https://vuejs.org/guide/typescript/options-api.html)
- [TypeScript strict Mode](https://www.typescriptlang.org/tsconfig#strict)
```

## File: `skills/vue-pinia-best-practices/SKILL.md`
```markdown
---
name: vue-pinia-best-practices
description: "Pinia stores, state management patterns, store setup, and reactivity with stores."
version: 1.0.0
license: MIT
author: github.com/vuejs-ai
---

Pinia best practices, common gotchas, and state management patterns.

### Store Setup
- Getting "getActivePinia was called" error at startup → See [pinia-no-active-pinia-error](reference/pinia-no-active-pinia-error.md)
- Setup stores missing state in DevTools or SSR → See [pinia-setup-store-return-all-state](reference/pinia-setup-store-return-all-state.md)

### Reactivity
- Store destructuring stops updating UI reactively → See [pinia-store-destructuring-breaks-reactivity](reference/pinia-store-destructuring-breaks-reactivity.md)
- Store methods lose context in template calls → See [store-method-binding-parentheses](reference/store-method-binding-parentheses.md)

### State Patterns
- Filters reset on refresh or can't be shared → See [state-url-for-ephemeral-filters](reference/state-url-for-ephemeral-filters.md)
- Building production app without DevTools or conventions → See [state-use-pinia-for-large-apps](reference/state-use-pinia-for-large-apps.md)
```

## File: `skills/vue-pinia-best-practices/reference/pinia-no-active-pinia-error.md`
```markdown
---
title: Fix "No Active Pinia" Error - Store Setup Timing
impact: HIGH
impactDescription: Using Pinia stores before app.use(pinia) causes "getActivePinia was called but there was no active Pinia" error
type: gotcha
tags: [vue3, pinia, state-management, setup, initialization, error]
---

# Fix "No Active Pinia" Error - Store Setup Timing

**Impact: HIGH** - The error "getActivePinia() was called but there was no active Pinia" is one of the most common Pinia errors. It occurs when you try to use a store before Pinia has been installed on the Vue app, causing your application to crash.

## Task Checklist

- [ ] Ensure `app.use(pinia)` is called before `app.mount()`
- [ ] Ensure `app.use(pinia)` is called before `app.use(router)` if router guards use stores
- [ ] Never call `useXxxStore()` in module-level (top-level) code
- [ ] Only call `useXxxStore()` inside setup functions, composables, or after app initialization
- [ ] Check for `<script setup>` vs `<script>` - the latter runs too early

## The Error

```
[🍍]: "getActivePinia()" was called but there was no active Pinia.
Did you forget to install pinia?
```

## Common Cause 1: Wrong Plugin Order

```javascript
// main.js - WRONG ORDER
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'  // Router uses a store in navigation guard
import App from './App.vue'

const app = createApp(App)

// WRONG: Router is installed first, but its guards use stores
app.use(router)  // Router guard calls useAuthStore() - FAILS!
app.use(createPinia())
app.mount('#app')
```

**Fix: Install Pinia first:**

```javascript
// main.js - CORRECT ORDER
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'

const app = createApp(App)

// CORRECT: Pinia installed before anything that uses stores
app.use(createPinia())
app.use(router)  // Now router guards can safely use stores
app.mount('#app')
```

## Common Cause 2: Store Used at Module Level

```javascript
// api.js - WRONG: Module-level store usage
import { useAuthStore } from '@/stores/auth'

// This runs immediately when the module is imported!
const authStore = useAuthStore()  // ERROR: No active Pinia yet

export function fetchUser() {
  return fetch('/api/user', {
    headers: {
      Authorization: `Bearer ${authStore.token}`
    }
  })
}
```

**Fix: Call useStore inside functions:**

```javascript
// api.js - CORRECT: Store used inside function
import { useAuthStore } from '@/stores/auth'

export function fetchUser() {
  // Store is accessed when function is called, not when module loads
  const authStore = useAuthStore()

  return fetch('/api/user', {
    headers: {
      Authorization: `Bearer ${authStore.token}`
    }
  })
}
```

## Common Cause 3: Script Tag Missing "setup"

```vue
<!-- WRONG: <script> runs before component setup -->
<script>
import { useUserStore } from '@/stores/user'

// This runs too early, before the component is set up
const userStore = useUserStore()  // ERROR!

export default {
  // ...
}
</script>
```

**Fix: Use `<script setup>` or move to setup function:**

```vue
<!-- CORRECT: <script setup> runs at the right time -->
<script setup>
import { useUserStore } from '@/stores/user'

// This runs during component setup, Pinia is active
const userStore = useUserStore()  // Works!
</script>
```

```vue
<!-- CORRECT: Options API with setup function -->
<script>
import { useUserStore } from '@/stores/user'

export default {
  setup() {
    // Called during component initialization
    const userStore = useUserStore()  // Works!
    return { userStore }
  }
}
</script>
```

## Common Cause 4: mapStores with Parentheses

```vue
<script>
import { mapStores } from 'pinia'
import { useProductsStore } from '@/stores/products'

export default {
  computed: {
    // WRONG: Called the function instead of passing it
    ...mapStores(useProductsStore())  // ERROR!
  }
}
</script>
```

**Fix: Pass the function reference, not the result:**

```vue
<script>
import { mapStores } from 'pinia'
import { useProductsStore } from '@/stores/products'

export default {
  computed: {
    // CORRECT: Pass the function without calling it
    ...mapStores(useProductsStore)  // No parentheses!
  }
}
</script>
```

## Common Cause 5: Router Guards Before Pinia

```javascript
// router/index.js - WRONG
import { createRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({ /* ... */ })

// This guard is registered immediately
router.beforeEach((to) => {
  // When this runs during app startup, Pinia might not be ready
  const authStore = useAuthStore()  // May fail!

  if (to.meta.requiresAuth && !authStore.isLoggedIn) {
    return '/login'
  }
})
```

**Fix: Use lazy store access or ensure plugin order:**

```javascript
// router/index.js - CORRECT
import { createRouter } from 'vue-router'

const router = createRouter({ /* ... */ })

router.beforeEach((to) => {
  // Dynamically import to avoid module-level execution
  const { useAuthStore } = await import('@/stores/auth')
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isLoggedIn) {
    return '/login'
  }
})

// OR ensure main.js has correct order:
// app.use(pinia)
// app.use(router)
```

## Debugging Checklist

When you see "No active Pinia":

1. **Check main.js order**: Is `app.use(pinia)` before other plugins?
2. **Search for top-level useStore calls**: Any store usage outside functions/setup?
3. **Check script tags**: Using `<script>` instead of `<script setup>`?
4. **Check mapStores usage**: Using `useStore()` instead of `useStore`?
5. **Check import chains**: Does an early import trigger store usage?

## Safe Pattern: Conditional Store Access

```javascript
// For code that might run before Pinia is ready
import { getActivePinia } from 'pinia'

export function safelyUseStore() {
  const pinia = getActivePinia()

  if (!pinia) {
    console.warn('Pinia not initialized yet')
    return null
  }

  const { useUserStore } = await import('@/stores/user')
  return useUserStore()
}
```

## Reference
- [Vue Land FAQ - No Active Pinia](https://vue-land.github.io/faq/no-active-pinia)
- [Pinia - Using a Store Outside of a Component](https://pinia.vuejs.org/core-concepts/outside-component-usage.html)
- [Pinia - Getting Started](https://pinia.vuejs.org/getting-started.html)
```

## File: `skills/vue-pinia-best-practices/reference/pinia-setup-store-return-all-state.md`
```markdown
---
title: Return All State Properties in Pinia Setup Stores
impact: HIGH
impactDescription: Not returning state properties in setup stores breaks SSR, DevTools, and plugin compatibility
type: gotcha
tags: [vue3, pinia, state-management, setup-stores, ssr, devtools]
---

# Return All State Properties in Pinia Setup Stores

**Impact: HIGH** - When using Pinia's setup store syntax (Composition API style), you MUST return all state properties from the setup function. Private state that isn't returned will break Server-Side Rendering (SSR), Vue DevTools inspection, and Pinia plugins.

This is a critical gotcha that can cause silent failures in production.

## Task Checklist

- [ ] Return ALL reactive state properties from setup stores
- [ ] Do not create "private" state by omitting it from the return
- [ ] If you need private state, use a prefix convention instead (e.g., `_internal`)
- [ ] Test stores with DevTools to verify all state is visible
- [ ] Verify SSR hydration includes all necessary state

## The Problem: Private State in Setup Stores

```javascript
// stores/user.js - WRONG: Private state breaks SSR/DevTools
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // Public state
  const name = ref('')
  const email = ref('')

  // "Private" state - NOT returned
  const authToken = ref('')  // Won't be serialized for SSR!
  const lastFetchTime = ref(null)  // Won't appear in DevTools!

  const isLoggedIn = computed(() => !!authToken.value)

  async function login(credentials) {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify(credentials)
    })
    const data = await response.json()

    authToken.value = data.token  // This state won't transfer to client in SSR!
    name.value = data.name
    email.value = data.email
    lastFetchTime.value = Date.now()
  }

  // WRONG: Not returning authToken and lastFetchTime
  return {
    name,
    email,
    isLoggedIn,
    login
  }
})
```

**What breaks:**

1. **SSR Hydration**: `authToken` and `lastFetchTime` won't be serialized and sent to the client
2. **DevTools**: These properties won't appear in the store inspector
3. **Plugins**: Persistence plugins won't save these properties
4. **Time-travel debugging**: Can't track changes to hidden state

## The Solution: Return Everything

```javascript
// stores/user.js - CORRECT: All state returned
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // All state properties
  const name = ref('')
  const email = ref('')
  const authToken = ref('')
  const lastFetchTime = ref(null)

  // Getters
  const isLoggedIn = computed(() => !!authToken.value)

  // Actions
  async function login(credentials) {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify(credentials)
    })
    const data = await response.json()

    authToken.value = data.token
    name.value = data.name
    email.value = data.email
    lastFetchTime.value = Date.now()
  }

  function logout() {
    authToken.value = ''
    name.value = ''
    email.value = ''
  }

  // CORRECT: Return ALL state, getters, and actions
  return {
    // State
    name,
    email,
    authToken,
    lastFetchTime,
    // Getters
    isLoggedIn,
    // Actions
    login,
    logout
  }
})
```

## If You Need "Private" State

Use naming conventions instead of actually hiding state:

```javascript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // Convention: underscore prefix for "internal" state
  // Still returned, but signals it's not for external use
  const _authToken = ref('')
  const _lastFetchTime = ref(null)

  // Public state
  const name = ref('')
  const email = ref('')

  const isLoggedIn = computed(() => !!_authToken.value)

  // Return everything - convention communicates intent
  return {
    // "Private" - use with caution
    _authToken,
    _lastFetchTime,
    // Public
    name,
    email,
    isLoggedIn
  }
})
```

## Option Stores Don't Have This Problem

With the Options API syntax, all state is automatically tracked:

```javascript
// stores/user.js - Options syntax: all state is tracked automatically
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    name: '',
    email: '',
    authToken: '',  // Automatically included
    lastFetchTime: null  // Automatically included
  }),

  getters: {
    isLoggedIn: (state) => !!state.authToken
  },

  actions: {
    async login(credentials) {
      // ...
    }
  }
})
```

## How Setup Stores Map to State

Understanding the mapping helps avoid mistakes:

```javascript
defineStore('example', () => {
  // ref() becomes state
  const count = ref(0)  // → state.count

  // computed() becomes getters
  const double = computed(() => count.value * 2)  // → getters.double

  // Regular functions become actions
  function increment() {  // → actions.increment
    count.value++
  }

  // CRITICAL: Must return all of them
  return { count, double, increment }
})
```

## Debugging: Verify All State is Returned

```javascript
// Test that DevTools can see all state
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// In DevTools console or tests:
console.log(userStore.$state)
// Should include ALL reactive state properties

// Check what's returned
console.log(Object.keys(userStore))
// Should include: name, email, authToken, lastFetchTime, isLoggedIn, login, logout
```

## Reference
- [Pinia - Setup Stores](https://pinia.vuejs.org/core-concepts/#setup-stores)
- [Pinia - SSR](https://pinia.vuejs.org/ssr/)
- [Mastering Pinia - Common Mistakes](https://masteringpinia.com/blog/top-5-mistakes-to-avoid-when-using-pinia)
```

## File: `skills/vue-pinia-best-practices/reference/pinia-store-destructuring-breaks-reactivity.md`
```markdown
---
title: Use storeToRefs When Destructuring Pinia Stores
impact: HIGH
impactDescription: Destructuring Pinia stores directly breaks reactivity - state changes won't trigger UI updates
type: gotcha
tags: [vue3, pinia, state-management, reactivity, destructuring]
---

# Use storeToRefs When Destructuring Pinia Stores

**Impact: HIGH** - Pinia stores are wrapped with `reactive`, so destructuring them directly extracts non-reactive values. Changes to the store won't be reflected in your component, causing stale UI and confusing bugs.

This is one of the most common mistakes when using Pinia, especially for developers coming from Vuex or other state management libraries.

## Task Checklist

- [ ] Never destructure state or getters directly from a Pinia store
- [ ] Use `storeToRefs()` to extract reactive state and getters
- [ ] Destructure actions directly (they don't need reactivity)
- [ ] Remember: `storeToRefs` is for state/getters, direct destructure is for actions

## The Problem: Direct Destructuring

```vue
<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// WRONG: Direct destructuring breaks reactivity
const { name, email, isLoggedIn } = userStore

// Later, when store updates...
userStore.login({ name: 'John', email: 'john@example.com' })

// name and email are still the OLD values!
// UI won't update because these are no longer reactive
console.log(name) // undefined (or initial value)
</script>

<template>
  <!-- This won't update when store changes -->
  <div>{{ name }}</div>
</template>
```

## The Solution: Use storeToRefs

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// CORRECT: Use storeToRefs for state and getters
const { name, email, isLoggedIn } = storeToRefs(userStore)

// Actions can be destructured directly (they're just functions)
const { login, logout } = userStore

// Now when the store updates...
login({ name: 'John', email: 'john@example.com' })

// name and email are reactive refs that update automatically
console.log(name.value) // 'John'
</script>

<template>
  <!-- This updates reactively -->
  <div>{{ name }}</div>
  <button @click="logout">Logout</button>
</template>
```

## Understanding Why This Happens

Pinia stores are reactive objects (like `reactive()`). When you destructure:

```javascript
const store = useCounterStore()
// store is a reactive Proxy

const { count } = store
// count is now just a primitive number (0), not reactive
// It's like doing: const count = 0

// vs with storeToRefs
const { count } = storeToRefs(store)
// count is now a ref that stays connected to the store
// It's like: const count = computed(() => store.count)
```

## Complete Pattern: State, Getters, and Actions

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()

// State and getters: USE storeToRefs
const {
  items,           // state
  itemCount,       // getter
  totalPrice,      // getter
  isEmpty          // getter
} = storeToRefs(cartStore)

// Actions: destructure directly
const {
  addItem,
  removeItem,
  clearCart
} = cartStore
</script>

<template>
  <div v-if="isEmpty">Cart is empty</div>
  <div v-else>
    <p>{{ itemCount }} items - ${{ totalPrice }}</p>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }}
        <button @click="removeItem(item.id)">Remove</button>
      </li>
    </ul>
    <button @click="clearCart">Clear All</button>
  </div>
</template>
```

## Alternative: Don't Destructure

If you prefer, you can avoid destructuring entirely:

```vue
<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
// Use userStore.name, userStore.login(), etc. directly
</script>

<template>
  <div>{{ userStore.name }}</div>
  <button @click="userStore.logout()">Logout</button>
</template>
```

This works fine but is more verbose for stores used frequently in the template.

## Common Mistake: Mixing storeToRefs with Actions

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// WRONG: Don't include actions in storeToRefs
// Actions are just functions and storeToRefs will skip them anyway
const { name, login } = storeToRefs(userStore)
// login is undefined! Actions aren't included in storeToRefs result

// CORRECT: Separate state/getters from actions
const { name } = storeToRefs(userStore)
const { login } = userStore
</script>
```

## TypeScript Tip

With TypeScript, the types work correctly:

```typescript
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// name is Ref<string>, email is Ref<string>
const { name, email } = storeToRefs(userStore)

// login is (credentials: Credentials) => Promise<void>
const { login } = userStore
```

## Reference
- [Pinia - Destructuring from a Store](https://pinia.vuejs.org/core-concepts/#destructuring-from-a-store)
- [Pinia API - storeToRefs](https://pinia.vuejs.org/api/modules/pinia.html#storetorefs)
```

## File: `skills/vue-pinia-best-practices/reference/state-url-for-ephemeral-filters.md`
```markdown
---
title: Use URL State for Shareable Filters Instead of Stores
impact: MEDIUM
impactDescription: Storing filter/search state only in stores loses state on refresh and prevents link sharing
type: best-practice
tags: [vue3, state-management, url, router, filters, ux, vue-router]
---

# Use URL State for Shareable Filters Instead of Stores

**Impact: MEDIUM** - Storing ephemeral UI state like filters, search queries, pagination, and sorting only in Pinia or component state means users lose that state on page refresh and cannot share links to specific filtered views. This hurts user experience and SEO.

For state that represents a "view" of data, use URL query parameters instead of or alongside stores.

## Task Checklist

- [ ] Identify ephemeral UI state: filters, search, sort, pagination, tab selection
- [ ] Store such state in URL query parameters
- [ ] Sync URL state with component/store state bidirectionally
- [ ] Consider using VueUse's `useRouteQuery` for type-safe URL state
- [ ] Keep URL state minimal and human-readable

## The Problem: Store-Only State

```vue
<script setup>
import { ref } from 'vue'
import { useProductStore } from '@/stores/products'

const productStore = useProductStore()

// Filter state in component/store only
const selectedCategory = ref('all')
const priceRange = ref([0, 1000])
const sortBy = ref('newest')
const searchQuery = ref('')

// Problems with this approach:
// 1. User refreshes page → filters reset to defaults
// 2. User bookmarks page → bookmark doesn't include filter state
// 3. User shares link → friend sees unfiltered view
// 4. Back button doesn't restore previous filter state
</script>
```

## The Solution: URL-Based State

```vue
<script setup>
import { computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

// Read filter state FROM URL
const selectedCategory = computed({
  get: () => route.query.category || 'all',
  set: (value) => updateQuery({ category: value === 'all' ? undefined : value })
})

const sortBy = computed({
  get: () => route.query.sort || 'newest',
  set: (value) => updateQuery({ sort: value === 'newest' ? undefined : value })
})

const searchQuery = computed({
  get: () => route.query.q || '',
  set: (value) => updateQuery({ q: value || undefined })
})

const page = computed({
  get: () => parseInt(route.query.page) || 1,
  set: (value) => updateQuery({ page: value === 1 ? undefined : value })
})

// Helper to update URL without full navigation
function updateQuery(newParams) {
  router.push({
    query: {
      ...route.query,
      ...newParams
    }
  })
}
</script>

<template>
  <div>
    <input v-model="searchQuery" placeholder="Search...">

    <select v-model="selectedCategory">
      <option value="all">All Categories</option>
      <option value="electronics">Electronics</option>
      <option value="clothing">Clothing</option>
    </select>

    <select v-model="sortBy">
      <option value="newest">Newest</option>
      <option value="price-low">Price: Low to High</option>
      <option value="price-high">Price: High to Low</option>
    </select>

    <!-- URL now looks like: /products?category=electronics&sort=price-low&q=phone -->
    <!-- Users can bookmark, share, and refresh without losing state -->
  </div>
</template>
```

## Using VueUse for Cleaner Code

VueUse provides `useRouteQuery` for type-safe URL state:

```vue
<script setup>
import { useRouteQuery } from '@vueuse/router'

// Automatically syncs with URL query parameters
const category = useRouteQuery('category', 'all')
const sort = useRouteQuery('sort', 'newest')
const search = useRouteQuery('q', '')
const page = useRouteQuery('page', 1, { transform: Number })
const showOutOfStock = useRouteQuery('inStock', false, { transform: Boolean })

// Arrays work too
const selectedTags = useRouteQuery('tags', [], {
  transform: (v) => Array.isArray(v) ? v : v ? [v] : []
})
</script>

<template>
  <input v-model="search" placeholder="Search...">
  <select v-model="category">...</select>
  <input type="checkbox" v-model="showOutOfStock"> Show out of stock
</template>
```

## Hybrid Approach: URL + Store

For complex state, sync URL with store:

```javascript
// stores/productFilters.js
import { defineStore } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import { watch } from 'vue'

export const useProductFiltersStore = defineStore('productFilters', () => {
  const route = useRoute()
  const router = useRouter()

  // Local reactive state
  const category = ref('all')
  const sortBy = ref('newest')
  const searchQuery = ref('')
  const page = ref(1)

  // Initialize from URL on store creation
  function initFromUrl() {
    category.value = route.query.category || 'all'
    sortBy.value = route.query.sort || 'newest'
    searchQuery.value = route.query.q || ''
    page.value = parseInt(route.query.page) || 1
  }

  // Sync state changes TO URL
  function syncToUrl() {
    router.replace({
      query: {
        category: category.value !== 'all' ? category.value : undefined,
        sort: sortBy.value !== 'newest' ? sortBy.value : undefined,
        q: searchQuery.value || undefined,
        page: page.value > 1 ? page.value : undefined
      }
    })
  }

  // Watch for URL changes (back/forward navigation)
  watch(() => route.query, initFromUrl, { immediate: true })

  // Watch for state changes and sync to URL
  watch([category, sortBy, searchQuery, page], syncToUrl)

  return {
    category,
    sortBy,
    searchQuery,
    page,
    initFromUrl
  }
})
```

## What Goes in URL vs Store

| State Type | URL | Store | Notes |
|------------|-----|-------|-------|
| Filters | Yes | Optional | Shareable, bookmarkable |
| Search query | Yes | Optional | SEO benefit |
| Pagination | Yes | Optional | Deep linking |
| Sort order | Yes | Optional | User expectation |
| Selected tab | Yes | Optional | Deep linking |
| Modal open state | Maybe | Yes | Usually not shareable |
| Form draft | No | Yes | Private, temporary |
| User session | No | Yes | Security |
| Shopping cart | No | Yes | Persistence needed |

## Benefits of URL State

1. **Shareable**: Users can share exact filtered views
2. **Bookmarkable**: Save specific searches/filters
3. **Browser history**: Back/forward works as expected
4. **SEO**: Search engines can index filtered pages
5. **Refresh-safe**: State survives page reload
6. **Deep linking**: Direct links to specific states

## Clean URL Best Practices

```javascript
// GOOD: Clean, readable URLs
/products?category=electronics&sort=price&q=phone

// AVOID: Overly complex URLs
/products?filters=%7B%22category%22%3A%22electronics%22%7D
```

```javascript
// Use defaults to keep URLs minimal
const sort = useRouteQuery('sort', 'newest')

// URL shows: /products (when using default sort)
// URL shows: /products?sort=price-low (when changed)
```

## Reference
- [VueUse - useRouteQuery](https://vueuse.org/router/useRouteQuery/)
- [Vue Router - Query Parameters](https://router.vuejs.org/guide/essentials/passing-props.html#passing-props-to-route-components)
- [Mastering Pinia - URL State](https://masteringpinia.com/blog/top-5-mistakes-to-avoid-when-using-pinia)
```

## File: `skills/vue-pinia-best-practices/reference/state-use-pinia-for-large-apps.md`
```markdown
---
title: Use Pinia for Large-Scale Vue Applications
impact: MEDIUM
impactDescription: Hand-rolled reactive stores lack DevTools integration, TypeScript support, and debugging capabilities needed for production apps
type: best-practice
tags: [vue3, pinia, state-management, devtools, architecture, scalability]
---

# Use Pinia for Large-Scale Vue Applications

**Impact: MEDIUM** - While Vue's Composition API allows creating simple reactive stores with `reactive()` and `ref()`, these hand-rolled solutions lack the tooling, conventions, and debugging capabilities needed for large-scale production applications. Pinia is the official Vue state management solution and should be used for any non-trivial application.

## Task Checklist

- [ ] Use Pinia for applications with shared state across multiple components
- [ ] Use Pinia when team collaboration requires consistent patterns
- [ ] Use Pinia when you need Vue DevTools state debugging
- [ ] Hand-rolled `reactive()` is acceptable only for simple, single-developer apps
- [ ] Migrate from Vuex to Pinia (Vuex is in maintenance mode)

## When Hand-Rolled State is Acceptable

Simple reactive state is fine for:
- Prototypes and proof-of-concepts
- Very small applications with minimal shared state
- Single-developer projects with limited scope
- Learning purposes

```javascript
// Simple hand-rolled store - OK for small apps
import { reactive, readonly } from 'vue'

export const store = reactive({
  count: 0,
  increment() {
    this.count++
  }
})
```

## When to Use Pinia

Use Pinia when you have any of these requirements:

### 1. DevTools Integration

Pinia provides rich Vue DevTools support:
- Timeline of state changes
- State inspection and editing
- Time-travel debugging
- Action tracking

```javascript
// Pinia store - fully visible in DevTools
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  actions: {
    increment() {
      this.count++  // Tracked in DevTools timeline
    }
  }
})
```

### 2. TypeScript Support

Pinia has excellent TypeScript inference:

```typescript
// Full type inference without extra configuration
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    name: '',
    age: 0,
    preferences: {
      theme: 'light' as 'light' | 'dark'
    }
  }),

  getters: {
    // Return type is inferred
    displayName: (state) => state.name || 'Anonymous'
  },

  actions: {
    // Full parameter type checking
    setUser(name: string, age: number) {
      this.name = name
      this.age = age
    }
  }
})

// Usage is fully typed
const userStore = useUserStore()
userStore.name  // string
userStore.displayName  // string
userStore.setUser('John', 30)  // Type-checked
```

### 3. Team Collaboration

Pinia enforces conventions that help teams:

```javascript
// Consistent structure across all stores
// stores/products.js
export const useProductsStore = defineStore('products', {
  state: () => ({ /* ... */ }),
  getters: { /* ... */ },
  actions: { /* ... */ }
})

// stores/cart.js - Same structure
export const useCartStore = defineStore('cart', {
  state: () => ({ /* ... */ }),
  getters: { /* ... */ },
  actions: { /* ... */ }
})
```

### 4. Hot Module Replacement (HMR)

Pinia supports HMR out of the box - state persists during development:

```javascript
// State survives code changes during development
// No need to re-login or re-create state after every edit
```

### 5. Server-Side Rendering (SSR)

Pinia handles SSR state correctly:

```javascript
// Automatic per-request state isolation
// State serialization for hydration
// No cross-request pollution
```

### 6. Plugin Ecosystem

Pinia supports plugins for common needs:

```javascript
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

// Now stores can persist to localStorage
export const useSettingsStore = defineStore('settings', {
  state: () => ({
    theme: 'light',
    language: 'en'
  }),
  persist: true  // Automatically saved/restored
})
```

## Pinia vs Hand-Rolled Comparison

| Feature | Hand-Rolled `reactive()` | Pinia |
|---------|-------------------------|-------|
| DevTools integration | No | Yes |
| TypeScript inference | Manual | Automatic |
| HMR support | No | Yes |
| SSR support | Manual | Built-in |
| Plugins | No | Yes |
| Time-travel debugging | No | Yes |
| Learning curve | Lower | Slightly higher |
| Bundle size | Smaller | ~1KB |
| Team conventions | None | Enforced |

## Migration from Vuex

Vuex is now in maintenance mode. Migrate to Pinia for new features:

```javascript
// Vuex (legacy)
export default createStore({
  state: { count: 0 },
  mutations: {
    INCREMENT(state) { state.count++ }
  },
  actions: {
    increment({ commit }) { commit('INCREMENT') }
  }
})

// Pinia (recommended)
export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  actions: {
    increment() { this.count++ }  // No mutations needed!
  }
})
```

**Pinia advantages over Vuex:**
- No mutations (simpler mental model)
- Better TypeScript support
- No nested modules complexity
- Smaller bundle size
- Composition API style available

## Pinia Store Styles

Choose the style that fits your team:

### Options Style (Similar to Options API)

```javascript
export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  getters: {
    double: (state) => state.count * 2
  },
  actions: {
    increment() { this.count++ }
  }
})
```

### Setup Style (Composition API)

```javascript
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const double = computed(() => count.value * 2)
  function increment() { count.value++ }

  return { count, double, increment }
})
```

## Quick Start

```bash
npm install pinia
```

```javascript
// main.js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
app.use(createPinia())
app.mount('#app')
```

## Reference
- [Vue.js - State Management](https://vuejs.org/guide/scaling-up/state-management.html)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Pinia vs Vuex](https://pinia.vuejs.org/introduction.html#comparison-with-vuex)
```

## File: `skills/vue-pinia-best-practices/reference/store-method-binding-parentheses.md`
```markdown
---
title: Include Parentheses When Calling Store Methods in Templates
impact: MEDIUM
impactDescription: Omitting parentheses on store method calls loses the correct 'this' context, causing unexpected behavior
type: gotcha
tags: [vue3, state-management, reactive, methods, templates, this-binding]
---

# Include Parentheses When Calling Store Methods in Templates

**Impact: MEDIUM** - When calling methods on a reactive store object in Vue templates, you must include parentheses (even without arguments) to ensure the method is called with the correct `this` context. Without parentheses, `this` inside the method may not refer to the store.

This is a subtle gotcha that can cause hard-to-debug issues with hand-rolled reactive stores.

## Task Checklist

- [ ] Always use parentheses when calling store methods in templates: `@click="store.increment()"`
- [ ] Avoid passing store methods as bare references: `@click="store.increment"` is problematic
- [ ] Consider using arrow functions or Pinia (which handles this automatically)
- [ ] Test store method calls work correctly with `this` references

## The Problem

```javascript
// store.js
import { reactive } from 'vue'

export const store = reactive({
  count: 0,
  increment() {
    this.count++  // 'this' should refer to the store
  }
})
```

```vue
<template>
  <!-- WRONG: Without parentheses, 'this' binding may be lost -->
  <button @click="store.increment">
    {{ store.count }}
  </button>
</template>
```

When you write `@click="store.increment"` (without parentheses), Vue passes the method as a callback to the event handler. The method gets called without being bound to the store object, so `this` inside `increment()` may be `undefined` or the global object instead of the store.

## The Solution

```vue
<template>
  <!-- CORRECT: With parentheses, method is called with correct context -->
  <button @click="store.increment()">
    {{ store.count }}
  </button>
</template>
```

With parentheses, you're telling Vue to call `store.increment()` directly, which preserves the `this` context as the store object.

## Why This Happens

In JavaScript, when you reference a method without calling it, you get the function itself without its binding:

```javascript
const store = {
  count: 0,
  increment() {
    this.count++
  }
}

// With parentheses - correct context
store.increment()  // this === store ✓

// Without parentheses - getting the function
const fn = store.increment
fn()  // this === undefined (in strict mode) ✗
```

Vue's event handler behavior:
- `@click="store.increment"` - Vue receives `store.increment` as a function and calls it later
- `@click="store.increment()"` - Vue evaluates `store.increment()` when the event fires

## Alternative Solutions

### 1. Use Arrow Functions in the Template

```vue
<template>
  <button @click="() => store.increment()">
    {{ store.count }}
  </button>
</template>
```

### 2. Bind Methods in the Store Definition

```javascript
// store.js
import { reactive } from 'vue'

const state = reactive({
  count: 0
})

// Methods defined separately, arrow functions don't have 'this' issues
export const store = {
  get count() { return state.count },
  increment: () => { state.count++ }
}
```

### 3. Use Pinia (Recommended)

Pinia handles method binding correctly:

```javascript
// stores/counter.js
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  actions: {
    increment() {
      this.count++  // Pinia ensures 'this' is correct
    }
  }
})
```

```vue
<script setup>
import { useCounterStore } from '@/stores/counter'
const counter = useCounterStore()
</script>

<template>
  <!-- Both work correctly with Pinia -->
  <button @click="counter.increment">Works</button>
  <button @click="counter.increment()">Also works</button>
</template>
```

### 4. Wrap in a Local Function

```vue
<script setup>
import { store } from './store'

// Wrap store method to ensure correct binding
function increment() {
  store.increment()
}
</script>

<template>
  <!-- Now safe to use without parentheses -->
  <button @click="increment">
    {{ store.count }}
  </button>
</template>
```

## When This Matters

This gotcha specifically affects:
- Hand-rolled reactive stores using `reactive()`
- Methods that reference `this` inside them
- Direct method references in templates without parentheses

It does NOT affect:
- Pinia stores (methods are auto-bound)
- Arrow function methods (no `this` binding)
- Methods that don't use `this`
- Method calls with parentheses

## Quick Reference

| Pattern | Safe? | Notes |
|---------|-------|-------|
| `@click="store.method()"` | Yes | Explicit call preserves context |
| `@click="store.method"` | No* | Context may be lost |
| `@click="() => store.method()"` | Yes | Arrow wrapper preserves context |
| `@click="localMethod"` | Yes | Component methods are auto-bound |
| Pinia: `@click="store.action"` | Yes | Pinia handles binding |

*Only problematic if the method uses `this`

## Reference
- [Vue.js State Management - Tip on Method Binding](https://vuejs.org/guide/scaling-up/state-management.html#simple-state-management-with-reactivity-api)
- [MDN - this in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
```

## File: `skills/vue-router-best-practices/SKILL.md`
```markdown
---
name: vue-router-best-practices
description: "Vue Router 4 patterns, navigation guards, route params, and route-component lifecycle interactions."
version: 1.0.0
license: MIT
author: github.com/vuejs-ai
---

Vue Router best practices, common gotchas, and navigation patterns.

### Navigation Guards
- Navigating between same route with different params → See [router-beforeenter-no-param-trigger](reference/router-beforeenter-no-param-trigger.md)
- Accessing component instance in beforeRouteEnter guard → See [router-beforerouteenter-no-this](reference/router-beforerouteenter-no-this.md)
- Navigation guard making API calls without awaiting → See [router-guard-async-await-pattern](reference/router-guard-async-await-pattern.md)
- Users trapped in infinite redirect loops → See [router-navigation-guard-infinite-loop](reference/router-navigation-guard-infinite-loop.md)
- Navigation guard using deprecated next() function → See [router-navigation-guard-next-deprecated](reference/router-navigation-guard-next-deprecated.md)

### Route Lifecycle
- Stale data when navigating between same route → See [router-param-change-no-lifecycle](reference/router-param-change-no-lifecycle.md)
- Event listeners persisting after component unmounts → See [router-simple-routing-cleanup](reference/router-simple-routing-cleanup.md)

### Setup
- Building production single-page application → See [router-use-vue-router-for-production](reference/router-use-vue-router-for-production.md)
```

## File: `skills/vue-router-best-practices/reference/router-beforeenter-no-param-trigger.md`
```markdown
---
title: Per-Route beforeEnter Guards Ignore Param/Query Changes
impact: MEDIUM
impactDescription: Route-level beforeEnter guards don't fire when only params, query, or hash change, causing unexpected bypasses of validation logic
type: gotcha
tags: [vue3, vue-router, navigation-guards, params, query]
---

# Per-Route beforeEnter Guards Ignore Param/Query Changes

**Impact: MEDIUM** - The `beforeEnter` guard defined in route configuration only triggers when entering a route from a DIFFERENT route. Changes to params, query strings, or hash within the same route do NOT trigger `beforeEnter`, potentially bypassing important validation logic.

## Task Checklist

- [ ] Use in-component `onBeforeRouteUpdate` for param/query changes
- [ ] Or use global `beforeEach` with route.params/query checks
- [ ] Document which guards protect which scenarios
- [ ] Test navigation between same route with different params

## The Problem

```javascript
// router.js
const routes = [
  {
    path: '/orders/:id',
    component: OrderDetail,
    beforeEnter: async (to, from) => {
      // This runs when entering from /products
      // But NOT when navigating from /orders/1 to /orders/2!
      const order = await checkOrderAccess(to.params.id)
      if (!order.canView) {
        return '/unauthorized'
      }
    }
  }
]
```

**Scenario:**
1. User navigates from `/products` to `/orders/1` - beforeEnter runs, access checked
2. User navigates from `/orders/1` to `/orders/2` - beforeEnter DOES NOT run!
3. User might access order they don't have permission for!

## What Triggers beforeEnter vs. What Doesn't

| Navigation | beforeEnter fires? |
|------------|-------------------|
| `/products` → `/orders/1` | YES |
| `/orders/1` → `/orders/2` | NO |
| `/orders/1` → `/orders/1?tab=details` | NO |
| `/orders/1#section` → `/orders/1#other` | NO |
| `/orders/1` → `/products` → `/orders/2` | YES (leaving and re-entering) |

## Solution 1: Add In-Component Guard

```vue
<!-- OrderDetail.vue -->
<script setup>
import { onBeforeRouteUpdate } from 'vue-router'

// Handle param changes within the same route
onBeforeRouteUpdate(async (to, from) => {
  if (to.params.id !== from.params.id) {
    const order = await checkOrderAccess(to.params.id)
    if (!order.canView) {
      return '/unauthorized'
    }
  }
})
</script>
```

## Solution 2: Use Global beforeEach Instead

```javascript
// router.js
router.beforeEach(async (to, from) => {
  // Handle all order access checks globally
  if (to.name === 'OrderDetail') {
    // This runs on EVERY navigation to this route, including param changes
    const order = await checkOrderAccess(to.params.id)
    if (!order.canView) {
      return '/unauthorized'
    }
  }
})
```

## Solution 3: Combine Both Guards

```javascript
// router.js - For entering from different route
const routes = [
  {
    path: '/orders/:id',
    component: OrderDetail,
    beforeEnter: (to) => validateOrderAccess(to.params.id)
  }
]

// In component - For param changes within route
// OrderDetail.vue
onBeforeRouteUpdate((to) => validateOrderAccess(to.params.id))

// Shared validation function
async function validateOrderAccess(orderId) {
  const order = await checkOrderAccess(orderId)
  if (!order.canView) {
    return '/unauthorized'
  }
}
```

## Solution 4: Use beforeEnter with Array of Guards

```javascript
// guards/orderGuards.js
export const orderAccessGuard = async (to) => {
  const order = await checkOrderAccess(to.params.id)
  if (!order.canView) {
    return '/unauthorized'
  }
}

// router.js
const routes = [
  {
    path: '/orders/:id',
    component: OrderDetail,
    beforeEnter: [orderAccessGuard]  // Can add multiple guards
  }
]

// Still need in-component guard for param changes!
```

## Full Navigation Guard Execution Order

Understanding when each guard type fires:

```
1. beforeRouteLeave (in-component, leaving component)
2. beforeEach (global)
3. beforeEnter (per-route, ONLY when entering from different route)
4. beforeRouteEnter (in-component, entering component)
5. beforeResolve (global)
6. afterEach (global, after navigation confirmed)

For param/query changes on same route:
1. beforeRouteUpdate (in-component) - ONLY this fires!
2. beforeEach (global)
3. beforeResolve (global)
4. afterEach (global)
```

## Key Points

1. **beforeEnter is for route ENTRY only** - Not for within-route changes
2. **Use onBeforeRouteUpdate for param changes** - This is the in-component solution
3. **Global beforeEach always runs** - Good for centralized validation
4. **Test param change scenarios** - Easy to miss during development
5. **Consider security implications** - Param-based access control needs both guards

## Reference
- [Vue Router Navigation Guards](https://router.vuejs.org/guide/advanced/navigation-guards.html)
- [Vue Router Per-Route Guards](https://router.vuejs.org/guide/advanced/navigation-guards.html#per-route-guard)
```

## File: `skills/vue-router-best-practices/reference/router-beforerouteenter-no-this.md`
```markdown
---
title: beforeRouteEnter Cannot Access Component Instance
impact: MEDIUM
impactDescription: The beforeRouteEnter guard runs before component creation, so 'this' is undefined; use the next callback to access the instance
type: gotcha
tags: [vue3, vue-router, navigation-guards, lifecycle, this]
---

# beforeRouteEnter Cannot Access Component Instance

**Impact: MEDIUM** - The `beforeRouteEnter` in-component navigation guard executes BEFORE the component is created, meaning you cannot access `this` or any component instance properties. This is the ONLY navigation guard that supports a callback in the `next()` function to access the component instance after navigation.

## Task Checklist

- [ ] Use next(vm => ...) callback to access component instance
- [ ] Or use composition API guards which have different patterns
- [ ] Move data fetching logic appropriately based on timing needs
- [ ] Consider using global guards for data that doesn't need component access

## The Problem

```javascript
// Options API - WRONG: this is undefined
export default {
  data() {
    return { user: null }
  },
  beforeRouteEnter(to, from, next) {
    // BUG: this is undefined here - component doesn't exist yet!
    this.user = await fetchUser(to.params.id)  // ERROR!
    next()
  }
}
```

## Solution: Use next() Callback (Options API)

```javascript
// Options API - CORRECT: Use callback to access vm
export default {
  data() {
    return {
      user: null,
      loading: true
    }
  },

  beforeRouteEnter(to, from, next) {
    // Fetch data before component exists
    fetchUser(to.params.id)
      .then(user => {
        // Pass callback to next() - receives component instance as 'vm'
        next(vm => {
          vm.user = user
          vm.loading = false
        })
      })
      .catch(error => {
        next(vm => {
          vm.error = error
          vm.loading = false
        })
      })
  }
}
```

## Solution: Async beforeRouteEnter (Options API)

```javascript
export default {
  data() {
    return { userData: null }
  },

  async beforeRouteEnter(to, from, next) {
    try {
      const user = await fetchUser(to.params.id)

      // Still need callback for component access
      next(vm => {
        vm.userData = user
      })
    } catch (error) {
      // Redirect on error
      next('/error')
    }
  }
}
```

## Composition API Alternative

In Composition API with `<script setup>`, you cannot use `beforeRouteEnter` directly because the component instance is being set up. Use different patterns instead:

```vue
<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const user = ref(null)
const loading = ref(true)

// Option 1: Fetch in onMounted (after component exists)
onMounted(async () => {
  user.value = await fetchUser(route.params.id)
  loading.value = false
})

// Option 2: Handle subsequent param changes
onBeforeRouteUpdate(async (to, from) => {
  if (to.params.id !== from.params.id) {
    loading.value = true
    user.value = await fetchUser(to.params.id)
    loading.value = false
  }
})
</script>
```

## Route-Level Data Fetching

For data that should load BEFORE navigation, use route-level guards:

```javascript
// router.js
const routes = [
  {
    path: '/users/:id',
    component: () => import('./UserProfile.vue'),
    beforeEnter: async (to, from) => {
      try {
        // Store data for component to access
        const user = await fetchUser(to.params.id)
        to.meta.user = user  // Attach to route meta
      } catch (error) {
        return '/error'
      }
    }
  }
]
```

```vue
<!-- UserProfile.vue -->
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
// Access pre-fetched data from meta
const user = route.meta.user
</script>
```

## Comparison of Navigation Guards

| Guard | Has `this`/component? | Can delay navigation? | Use case |
|-------|----------------------|----------------------|----------|
| beforeRouteEnter | NO (use next callback) | YES | Pre-fetch, redirect if data missing |
| beforeRouteUpdate | YES | YES | React to param changes |
| beforeRouteLeave | YES | YES | Unsaved changes warning |
| Global beforeEach | NO | YES | Auth checks |
| Route beforeEnter | NO | YES | Route-specific validation |

## Key Points

1. **beforeRouteEnter runs before component creation** - No access to `this`
2. **Use next(vm => ...) callback** - Only way to access component instance
3. **Composition API has limitations** - Use onMounted or global guards instead
4. **Consider route meta for pre-fetched data** - Clean separation of concerns
5. **beforeRouteUpdate and beforeRouteLeave have component access** - They run when component exists

## Reference
- [Vue Router In-Component Guards](https://router.vuejs.org/guide/advanced/navigation-guards.html#in-component-guards)
- [Vue Router Navigation Resolution Flow](https://router.vuejs.org/guide/advanced/navigation-guards.html#the-full-navigation-resolution-flow)
```

## File: `skills/vue-router-best-practices/reference/router-guard-async-await-pattern.md`
```markdown
---
title: Async Navigation Guards Require Proper Promise Handling
impact: MEDIUM
impactDescription: Unawaited promises in guards cause navigation to complete before async checks finish, allowing unauthorized access or missing data
type: gotcha
tags: [vue3, vue-router, navigation-guards, async, promises]
---

# Async Navigation Guards Require Proper Promise Handling

**Impact: MEDIUM** - Navigation guards that perform async operations (API calls, auth checks) must properly handle promises. If you don't await async operations or return the promise, navigation completes before your check finishes, potentially allowing unauthorized access or navigating with incomplete data.

## Task Checklist

- [ ] Use async/await in navigation guards
- [ ] Return the promise if not using async/await
- [ ] Add loading states for long async operations
- [ ] Implement timeouts for slow API calls
- [ ] Handle errors to prevent navigation hanging

## The Problem

```javascript
// WRONG: Not awaiting - navigation proceeds immediately
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth) {
    checkAuth()  // This returns a Promise but we're not waiting!
    // Navigation continues before checkAuth completes
  }
})

// WRONG: Async function but forgot return
router.beforeEach(async (to, from) => {
  if (to.meta.requiresAuth) {
    const isValid = await checkAuth()
    if (!isValid) {
      // This redirect might happen after navigation already completed!
      return '/login'
    }
  }
  // Missing return - implicitly returns undefined, allowing navigation
})
```

## Solution: Proper Async/Await Pattern

```javascript
// CORRECT: Async function with proper returns
router.beforeEach(async (to, from) => {
  if (to.meta.requiresAuth) {
    try {
      const isAuthenticated = await checkAuth()

      if (!isAuthenticated) {
        return { name: 'Login', query: { redirect: to.fullPath } }
      }
    } catch (error) {
      console.error('Auth check failed:', error)
      return { name: 'Error', params: { message: 'Authentication failed' } }
    }
  }
  // Explicitly return nothing to proceed
  return true
})
```

## Solution: Promise-Based Pattern (Alternative)

```javascript
// CORRECT: Return promise explicitly
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth) {
    return checkAuth()
      .then(isAuthenticated => {
        if (!isAuthenticated) {
          return { name: 'Login' }
        }
      })
      .catch(error => {
        console.error('Auth check failed:', error)
        return { name: 'Error' }
      })
  }
})
```

## Loading State During Async Guards

```javascript
// app/composables/useNavigationLoading.js
import { ref } from 'vue'

const isNavigating = ref(false)

export function useNavigationLoading() {
  return { isNavigating }
}

export function setupNavigationLoading(router) {
  router.beforeEach(() => {
    isNavigating.value = true
  })

  router.afterEach(() => {
    isNavigating.value = false
  })

  router.onError(() => {
    isNavigating.value = false
  })
}
```

```vue
<!-- App.vue -->
<script setup>
import { useNavigationLoading } from '@/composables/useNavigationLoading'

const { isNavigating } = useNavigationLoading()
</script>

<template>
  <LoadingBar v-if="isNavigating" />
  <router-view />
</template>
```

## Timeout Pattern for Slow APIs

```javascript
// CORRECT: Add timeout to prevent indefinite waiting
function withTimeout(promise, ms = 5000) {
  return Promise.race([
    promise,
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error('Request timeout')), ms)
    )
  ])
}

router.beforeEach(async (to, from) => {
  if (to.meta.requiresAuth) {
    try {
      const isValid = await withTimeout(checkAuth(), 5000)
      if (!isValid) {
        return '/login'
      }
    } catch (error) {
      if (error.message === 'Request timeout') {
        // Let user through but show warning
        console.warn('Auth check timed out')
      } else {
        return '/login'
      }
    }
  }
})
```

## Multiple Async Checks

```javascript
// CORRECT: Run independent checks in parallel
router.beforeEach(async (to, from) => {
  if (to.meta.requiresAuth && to.meta.requiresSubscription) {
    try {
      const [isAuthenticated, hasSubscription] = await Promise.all([
        checkAuth(),
        checkSubscription()
      ])

      if (!isAuthenticated) {
        return '/login'
      }

      if (!hasSubscription) {
        return '/subscribe'
      }
    } catch (error) {
      return '/error'
    }
  }
})
```

## Error Handling Best Practices

```javascript
router.beforeEach(async (to, from) => {
  try {
    // Your async logic here
    await performChecks(to)
  } catch (error) {
    // Always handle errors to prevent navigation from hanging

    if (error.response?.status === 401) {
      return '/login'
    }

    if (error.response?.status === 403) {
      return '/forbidden'
    }

    if (error.code === 'NETWORK_ERROR') {
      // Offline - maybe allow navigation but show warning
      return true
    }

    // Unknown error - redirect to error page
    console.error('Navigation guard error:', error)
    return { name: 'Error', state: { error: error.message } }
  }
})
```

## Key Points

1. **Always await async operations** - Otherwise navigation proceeds immediately
2. **Return values matter** - Return route to redirect, false to cancel, true/undefined to proceed
3. **Handle all error cases** - Uncaught errors can hang navigation
4. **Add timeouts** - Slow APIs shouldn't block navigation indefinitely
5. **Show loading state** - Users need feedback during async checks
6. **Parallelize independent checks** - Use Promise.all for better performance

## Reference
- [Vue Router Navigation Guards](https://router.vuejs.org/guide/advanced/navigation-guards.html)
- [Vue Router Navigation Failures](https://router.vuejs.org/guide/advanced/navigation-failures.html)
```

## File: `skills/vue-router-best-practices/reference/router-navigation-guard-infinite-loop.md`
```markdown
---
title: Navigation Guard Infinite Redirect Loops
impact: HIGH
impactDescription: Misconfigured navigation guards can trap users in infinite redirect loops, crashing the browser or making the app unusable
type: gotcha
tags: [vue3, vue-router, navigation-guards, redirect, debugging]
---

# Navigation Guard Infinite Redirect Loops

**Impact: HIGH** - A common mistake in navigation guards is creating conditions that cause infinite redirects. Vue Router will detect this and show a warning, but in production, it can crash the browser or create a broken user experience.

## Task Checklist

- [ ] Always check if already on target route before redirecting
- [ ] Test guard logic with all possible navigation scenarios
- [ ] Add route meta to control which routes need protection
- [ ] Use Vue Router devtools to debug redirect chains

## The Problem

```javascript
// WRONG: Infinite loop - always redirects to login, even when on login!
router.beforeEach((to, from) => {
  if (!isAuthenticated()) {
    return '/login'  // Redirects to /login, which triggers guard again...
  }
})

// WRONG: Circular redirect between two routes
router.beforeEach((to, from) => {
  if (to.path === '/dashboard' && !hasProfile()) {
    return '/profile'
  }
  if (to.path === '/profile' && !isVerified()) {
    return '/dashboard'  // Back to dashboard, which goes to profile...
  }
})
```

**Error you'll see:**
```
[Vue Router warn]: Detected an infinite redirection in a navigation guard when going from "/" to "/login". Aborting to avoid a Stack Overflow.
```

## Solution 1: Exclude Target Route

```javascript
// CORRECT: Don't redirect if already going to login
router.beforeEach((to, from) => {
  if (!isAuthenticated() && to.path !== '/login') {
    return '/login'
  }
})

// CORRECT: Use route name for cleaner check
router.beforeEach((to, from) => {
  const publicPages = ['Login', 'Register', 'ForgotPassword']

  if (!isAuthenticated() && !publicPages.includes(to.name)) {
    return { name: 'Login' }
  }
})
```

## Solution 2: Use Route Meta Fields

```javascript
// router.js
const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresAuth: false }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/public',
    name: 'PublicPage',
    component: PublicPage,
    meta: { requiresAuth: false }
  }
]

// Guard checks meta field
router.beforeEach((to, from) => {
  // Only redirect if route requires auth
  if (to.meta.requiresAuth && !isAuthenticated()) {
    return { name: 'Login', query: { redirect: to.fullPath } }
  }
})
```

## Solution 3: Handle Redirect Chains Carefully

```javascript
// CORRECT: Break potential circular redirects
router.beforeEach((to, from) => {
  // Prevent redirect loops by tracking redirect depth
  const redirectCount = to.query._redirectCount || 0

  if (redirectCount > 3) {
    console.error('Too many redirects, stopping at:', to.path)
    return '/error'  // Escape hatch
  }

  if (needsRedirect(to)) {
    return {
      path: getRedirectTarget(to),
      query: { ...to.query, _redirectCount: redirectCount + 1 }
    }
  }
})
```

## Solution 4: Centralized Redirect Logic

```javascript
// guards/auth.js
export function createAuthGuard(router) {
  const publicRoutes = new Set(['Login', 'Register', 'ForgotPassword', 'ResetPassword'])
  const guestOnlyRoutes = new Set(['Login', 'Register'])

  router.beforeEach((to, from) => {
    const isPublic = publicRoutes.has(to.name)
    const isGuestOnly = guestOnlyRoutes.has(to.name)
    const isLoggedIn = isAuthenticated()

    // Not logged in, trying to access protected route
    if (!isLoggedIn && !isPublic) {
      return { name: 'Login', query: { redirect: to.fullPath } }
    }

    // Logged in, trying to access guest-only route (like login page)
    if (isLoggedIn && isGuestOnly) {
      return { name: 'Dashboard' }
    }

    // All other cases: proceed
  })
}
```

## Debugging Redirect Loops

```javascript
// Add logging to understand the redirect chain
router.beforeEach((to, from) => {
  console.log(`Navigation: ${from.path} -> ${to.path}`)
  console.log('Auth state:', isAuthenticated())
  console.log('Route meta:', to.meta)

  // Your guard logic here
})

// Or use afterEach for confirmed navigations
router.afterEach((to, from) => {
  console.log(`Navigated: ${from.path} -> ${to.path}`)
})
```

## Common Redirect Loop Patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Auth check without exclusion | Login redirects to login | Exclude `/login` from check |
| Role-based with circular deps | Admin -> User -> Admin | Use single source of truth for role requirements |
| Onboarding flow | Step 1 -> Step 2 -> Step 1 | Track completion state properly |
| Redirect query handling | Reading redirect creates new redirect | Process redirect only once |

## Key Points

1. **Always exclude the target route** - Never redirect to a route that would trigger the same redirect
2. **Use route meta fields** - Cleaner than path string comparisons
3. **Test edge cases** - Direct URL access, refresh, back button
4. **Add logging during development** - Helps trace redirect chains
5. **Have an escape hatch** - Error page or max redirect count

## Reference
- [Vue Router Navigation Guards](https://router.vuejs.org/guide/advanced/navigation-guards.html)
- [Vue Router Route Meta Fields](https://router.vuejs.org/guide/advanced/meta.html)
```

## File: `skills/vue-router-best-practices/reference/router-navigation-guard-next-deprecated.md`
```markdown
---
title: Vue Router Navigation Guard next() Function Deprecated
impact: HIGH
impactDescription: Using the deprecated next() function incorrectly causes navigation to hang, infinite loops, or silent failures
type: gotcha
tags: [vue3, vue-router, navigation-guards, migration, async]
---

# Vue Router Navigation Guard next() Function Deprecated

**Impact: HIGH** - The third `next()` argument in navigation guards is deprecated in Vue Router 4. While still supported for backward compatibility, using it incorrectly is one of the most common sources of bugs: calling it multiple times, forgetting to call it, or calling it conditionally without proper logic.

## Task Checklist

- [ ] Refactor guards to use return-based syntax instead of next()
- [ ] Remove all next() calls from navigation guards
- [ ] Use async/await pattern for asynchronous checks
- [ ] Return false to cancel, return route to redirect, return nothing to proceed

## The Problem

```javascript
// WRONG: Using deprecated next() function
router.beforeEach((to, from, next) => {
  if (!isAuthenticated) {
    next('/login')  // Easy to forget this call
  }
  // BUG: next() not called when authenticated - navigation hangs!
})

// WRONG: Multiple next() calls
router.beforeEach((to, from, next) => {
  if (!isAuthenticated) {
    next('/login')
  }
  next()  // BUG: Called twice when not authenticated!
})

// WRONG: next() in async code without proper handling
router.beforeEach(async (to, from, next) => {
  const user = await fetchUser()
  if (!user) {
    next('/login')
  }
  next()  // Still gets called even after redirect!
})
```

## Solution: Use Return-Based Guards

```javascript
// CORRECT: Return-based syntax (modern Vue Router 4+)
router.beforeEach((to, from) => {
  if (!isAuthenticated) {
    return '/login'  // Redirect
  }
  // Return nothing (undefined) to proceed
})

// CORRECT: Return false to cancel navigation
router.beforeEach((to, from) => {
  if (hasUnsavedChanges) {
    return false  // Cancel navigation
  }
})

// CORRECT: Async with return-based syntax
router.beforeEach(async (to, from) => {
  const user = await fetchUser()
  if (!user) {
    return { name: 'Login', query: { redirect: to.fullPath } }
  }
  // Proceed with navigation
})
```

## Return Values Explained

```javascript
router.beforeEach((to, from) => {
  // Return nothing/undefined - allow navigation
  return

  // Return false - cancel navigation, stay on current route
  return false

  // Return string path - redirect to path
  return '/login'

  // Return route object - redirect with full control
  return { name: 'Login', query: { redirect: to.fullPath } }

  // Return Error - cancel and trigger router.onError()
  return new Error('Navigation cancelled')
})
```

## If You Must Use next() (Legacy Code)

If maintaining legacy code that uses `next()`, follow these rules strictly:

```javascript
// CORRECT: Exactly one next() call per code path
router.beforeEach((to, from, next) => {
  if (!isAuthenticated) {
    next('/login')
    return  // CRITICAL: Exit after calling next()
  }

  if (!hasPermission(to)) {
    next('/forbidden')
    return  // CRITICAL: Exit after calling next()
  }

  next()  // Only reached if all checks pass
})
```

## Error Handling Pattern

```javascript
router.beforeEach(async (to, from) => {
  try {
    await validateAccess(to)
    // Proceed
  } catch (error) {
    if (error.status === 401) {
      return '/login'
    }
    if (error.status === 403) {
      return '/forbidden'
    }
    // Log error and proceed anyway (or return false)
    console.error('Access validation failed:', error)
    return false
  }
})
```

## Key Points

1. **Prefer return-based syntax** - Cleaner, less error-prone, modern standard
2. **next() must be called exactly once** - If using legacy syntax, ensure single call per path
3. **Always return/exit after redirect** - Prevent multiple navigation actions
4. **Async guards work naturally** - Just return the redirect route or nothing
5. **Test all code paths** - Each branch must result in either return or next()

## Reference
- [Vue Router Navigation Guards](https://router.vuejs.org/guide/advanced/navigation-guards.html)
- [RFC: Remove next() from Navigation Guards](https://github.com/vuejs/rfcs/discussions/302)
```

## File: `skills/vue-router-best-practices/reference/router-param-change-no-lifecycle.md`
```markdown
---
title: Route Param Changes Do Not Trigger Lifecycle Hooks
impact: HIGH
impactDescription: Navigating between routes with different params reuses the component instance, skipping created/mounted hooks and leaving stale data
type: gotcha
tags: [vue3, vue-router, lifecycle, params, reactivity]
---

# Route Param Changes Do Not Trigger Lifecycle Hooks

**Impact: HIGH** - When navigating between routes that use the same component (e.g., `/users/1` to `/users/2`), Vue Router reuses the existing component instance for performance. This means `onMounted`, `created`, and other lifecycle hooks do NOT fire, leaving you with stale data from the previous route.

## Task Checklist

- [ ] Use `watch` on route params for data fetching
- [ ] Or use `onBeforeRouteUpdate` in-component guard
- [ ] Or use `:key="route.params.id"` to force re-creation (less efficient)
- [ ] Never rely solely on `onMounted` for route-param-dependent data

## The Problem

```vue
<!-- UserProfile.vue - Used for /users/:id -->
<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const user = ref(null)

// BUG: Only runs once when component first mounts!
// Navigating from /users/1 to /users/2 does NOT trigger this
onMounted(async () => {
  user.value = await fetchUser(route.params.id)
})
</script>

<template>
  <div>
    <!-- Still shows User 1 data when navigating to /users/2! -->
    <h1>{{ user?.name }}</h1>
  </div>
</template>
```

**Scenario:**
1. Visit `/users/1` - Component mounts, fetches User 1 data
2. Navigate to `/users/2` - Component is REUSED, onMounted doesn't run
3. UI still shows User 1's data!

## Solution 1: Watch Route Params (Recommended)

```vue
<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const user = ref(null)
const loading = ref(false)

// Watch for param changes - handles both initial load and navigation
watch(
  () => route.params.id,
  async (newId) => {
    loading.value = true
    user.value = await fetchUser(newId)
    loading.value = false
  },
  { immediate: true }  // Run immediately for initial load
)
</script>
```

## Solution 2: Use onBeforeRouteUpdate Guard

```vue
<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const user = ref(null)

async function loadUser(id) {
  user.value = await fetchUser(id)
}

// Initial load
onMounted(() => loadUser(route.params.id))

// Handle param changes within same route
onBeforeRouteUpdate(async (to, from) => {
  if (to.params.id !== from.params.id) {
    await loadUser(to.params.id)
  }
})
</script>
```

## Solution 3: Force Component Re-creation with Key

```vue
<!-- App.vue or parent component -->
<template>
  <router-view :key="$route.fullPath" />
</template>
```

**Tradeoffs:**
- Simple but less performant
- Destroys and recreates component on every param change
- Loses component state
- Use only when component state should reset completely

## Solution 4: Composable for Route-Reactive Data

```javascript
// composables/useRouteData.js
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

export function useRouteData(paramName, fetcher) {
  const route = useRoute()
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  watch(
    () => route.params[paramName],
    async (id) => {
      if (!id) return

      loading.value = true
      error.value = null

      try {
        data.value = await fetcher(id)
      } catch (e) {
        error.value = e
      } finally {
        loading.value = false
      }
    },
    { immediate: true }
  )

  return { data, loading, error }
}
```

```vue
<!-- Usage in component -->
<script setup>
import { useRouteData } from '@/composables/useRouteData'
import { fetchUser } from '@/api/users'

const { data: user, loading, error } = useRouteData('id', fetchUser)
</script>
```

## What Triggers vs. What Doesn't

| Navigation Type | Lifecycle Hooks | beforeRouteUpdate | Watch on params |
|----------------|-----------------|-------------------|-----------------|
| `/users/1` to `/posts/1` | YES | NO | YES |
| `/users/1` to `/users/2` | NO | YES | YES |
| `/users/1?tab=a` to `/users/1?tab=b` | NO | YES | NO (different watch) |
| `/users/1` to `/users/1` (same) | NO | NO | NO |

## Key Points

1. **Same route, different params = same component instance** - This is a performance optimization
2. **Lifecycle hooks only fire once** - When component first mounts
3. **Use `watch` with `immediate: true`** - Covers both initial load and updates
4. **`onBeforeRouteUpdate` is navigation-aware** - Good for data that must load before view updates
5. **`:key="route.fullPath"` is a sledgehammer** - Use only when necessary

## Reference
- [Vue Router Dynamic Route Matching](https://router.vuejs.org/guide/essentials/dynamic-matching.html#reacting-to-params-changes)
- [Vue School: Reacting to Param Changes](https://vueschool.io/lessons/reacting-to-param-changes)
```

## File: `skills/vue-router-best-practices/reference/router-simple-routing-cleanup.md`
```markdown
---
title: Simple Hash Routing Requires Event Listener Cleanup
impact: MEDIUM
impactDescription: When implementing basic routing without Vue Router, forgetting to remove hashchange listeners causes memory leaks and multiple handler execution
type: gotcha
tags: [vue3, routing, events, memory-leak, cleanup]
---

# Simple Hash Routing Requires Event Listener Cleanup

**Impact: MEDIUM** - When implementing basic client-side routing without Vue Router (using hash-based routing with `hashchange` events), you must clean up event listeners when the component unmounts. Failure to do so causes memory leaks and can result in multiple handlers firing after the component is recreated.

## Task Checklist

- [ ] Store event listener reference for cleanup
- [ ] Use onUnmounted to remove event listener
- [ ] Consider using Vue Router instead for production apps
- [ ] Test component mount/unmount cycles

## The Problem

```vue
<script setup>
import { ref, computed } from 'vue'
import Home from './Home.vue'
import About from './About.vue'

const routes = {
  '/': Home,
  '/about': About
}

const currentPath = ref(window.location.hash)

// BUG: Event listener is never removed!
// Each time this component mounts, a NEW listener is added
// After mounting 5 times, you have 5 listeners running
window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/']
})
</script>
```

**What happens:**
1. Component mounts, adds listener
2. Component unmounts (e.g., route change, v-if toggle)
3. Component mounts again, adds ANOTHER listener
4. Now TWO listeners respond to each hash change
5. Eventually causes performance issues and memory leaks

## Solution: Proper Cleanup with onUnmounted

```vue
<script setup>
import { ref, computed, onUnmounted } from 'vue'
import Home from './Home.vue'
import About from './About.vue'
import NotFound from './NotFound.vue'

const routes = {
  '/': Home,
  '/about': About
}

const currentPath = ref(window.location.hash)

// Store handler reference for cleanup
function handleHashChange() {
  currentPath.value = window.location.hash
}

// Add listener
window.addEventListener('hashchange', handleHashChange)

// CRITICAL: Remove listener on unmount
onUnmounted(() => {
  window.removeEventListener('hashchange', handleHashChange)
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>
```

## Solution: Using Options API

```vue
<script>
import Home from './Home.vue'
import About from './About.vue'
import NotFound from './NotFound.vue'

const routes = {
  '/': Home,
  '/about': About
}

export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },

  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/'] || NotFound
    }
  },

  mounted() {
    // Store bound handler for cleanup
    this.hashHandler = () => {
      this.currentPath = window.location.hash
    }
    window.addEventListener('hashchange', this.hashHandler)
  },

  beforeUnmount() {
    // Clean up
    window.removeEventListener('hashchange', this.hashHandler)
  }
}
</script>
```

## Solution: Composable for Reusable Hash Routing

```javascript
// composables/useHashRouter.js
import { ref, computed, onUnmounted } from 'vue'

export function useHashRouter(routes, notFoundComponent = null) {
  const currentPath = ref(window.location.hash)

  function handleHashChange() {
    currentPath.value = window.location.hash
  }

  // Setup
  window.addEventListener('hashchange', handleHashChange)

  // Cleanup - handled automatically when component unmounts
  onUnmounted(() => {
    window.removeEventListener('hashchange', handleHashChange)
  })

  const currentView = computed(() => {
    const path = currentPath.value.slice(1) || '/'
    return routes[path] || notFoundComponent
  })

  function navigate(path) {
    window.location.hash = path
  }

  return {
    currentPath,
    currentView,
    navigate
  }
}
```

```vue
<!-- Usage -->
<script setup>
import { useHashRouter } from '@/composables/useHashRouter'
import Home from './Home.vue'
import About from './About.vue'
import NotFound from './NotFound.vue'

const { currentView } = useHashRouter({
  '/': Home,
  '/about': About
}, NotFound)
</script>

<template>
  <component :is="currentView" />
</template>
```

## When to Use Simple Routing vs Vue Router

| Use Simple Hash Routing | Use Vue Router |
|------------------------|----------------|
| Learning/prototyping | Production apps |
| Very simple apps (2-3 pages) | Nested routes needed |
| No build step available | Navigation guards needed |
| Bundle size critical | Lazy loading needed |
| Static hosting only | History mode (clean URLs) |

## Key Points

1. **Always clean up event listeners** - Use onUnmounted or beforeUnmount
2. **Store handler reference** - Anonymous functions can't be removed
3. **Consider Vue Router for real apps** - It handles cleanup automatically
4. **Test unmount scenarios** - v-if toggling, hot module replacement
5. **Composables help encapsulate cleanup logic** - Reusable and automatic

## Reference
- [Vue.js Routing Documentation](https://vuejs.org/guide/scaling-up/routing.html)
- [Vue Router Official Library](https://router.vuejs.org/)
```

## File: `skills/vue-router-best-practices/reference/router-use-vue-router-for-production.md`
```markdown
---
title: Use Vue Router Library for Production Applications
impact: LOW
impactDescription: Simple hash routing lacks essential features for production SPAs; Vue Router provides navigation guards, lazy loading, and proper history management
type: best-practice
tags: [vue3, vue-router, spa, production, architecture]
---

# Use Vue Router Library for Production Applications

**Impact: LOW** - While you can implement basic routing with hash changes and dynamic components, the official Vue Router library should be used for any production single-page application. It provides essential features like navigation guards, nested routes, lazy loading, and proper browser history integration that are tedious and error-prone to implement manually.

## Task Checklist

- [ ] Install Vue Router for production SPAs
- [ ] Use simple routing only for learning or tiny prototypes
- [ ] Leverage built-in features: guards, lazy loading, meta fields
- [ ] Consider router-based state and data loading patterns

## When Simple Routing is Acceptable

```vue
<!-- Only for: learning, prototypes, or micro-apps with 2-3 pages -->
<script setup>
import { ref, computed } from 'vue'
import Home from './Home.vue'
import About from './About.vue'

const routes = { '/': Home, '/about': About }
const currentPath = ref(window.location.hash.slice(1) || '/')

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash.slice(1) || '/'
})

const currentView = computed(() => routes[currentPath.value])
</script>

<template>
  <nav>
    <a href="#/">Home</a>
    <a href="#/about">About</a>
  </nav>
  <component :is="currentView" />
</template>
```

## Why Vue Router for Production

### Features You'd Have to Implement Manually

| Feature | Simple Routing | Vue Router |
|---------|---------------|------------|
| Navigation guards | Manual, error-prone | Built-in, composable |
| Nested routes | Complex to implement | Native support |
| Route params | Parse manually | Automatic extraction |
| Lazy loading | DIY with dynamic imports | Built-in with code splitting |
| History mode (clean URLs) | Requires server config + manual | Built-in |
| Scroll behavior | Manual | Configurable |
| Route transitions | DIY | Integrated with Transition |
| Active link styling | Manual class toggling | `router-link-active` class |
| Programmatic navigation | `location.hash = ...` | `router.push()`, `router.replace()` |
| Route meta fields | N/A | Built-in |

## Production Setup with Vue Router

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),  // Lazy loaded
    meta: { requiresAuth: false }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: 'settings',
        name: 'Settings',
        component: () => import('@/views/Settings.vue')
      }
    ]
  },
  {
    path: '/users/:id',
    name: 'UserProfile',
    component: () => import('@/views/UserProfile.vue'),
    props: true  // Pass params as props
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }
  }
})

// Global navigation guard
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    return { name: 'Login', query: { redirect: to.fullPath } }
  }
})

export default router
```

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App)
  .use(router)
  .mount('#app')
```

```vue
<!-- App.vue -->
<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/dashboard">Dashboard</router-link>
  </nav>

  <router-view v-slot="{ Component }">
    <transition name="fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
</template>
```

## Modern Vue Router Features (2025+)

```javascript
// Data Loading API (Vue Router 4.2+)
const routes = [
  {
    path: '/users/:id',
    component: UserProfile,
    // Load data at route level
    loader: async (route) => {
      return { user: await fetchUser(route.params.id) }
    }
  }
]

// View Transitions API integration
const router = createRouter({
  // Enable native browser view transitions
  // Requires browser support (Chrome 111+)
})
```

## Key Points

1. **Use Vue Router for any app beyond a prototype** - The features are essential
2. **Simple routing is for learning** - Understand the concepts, then use the library
3. **Lazy loading is critical for bundle size** - Vue Router makes it trivial
4. **Navigation guards prevent security issues** - Hard to get right manually
5. **History mode requires Vue Router** - Clean URLs need proper handling
6. **New features keep coming** - Data Loading API, View Transitions

## Reference
- [Vue.js Routing Guide](https://vuejs.org/guide/scaling-up/routing.html)
- [Vue Router Documentation](https://router.vuejs.org/)
- [Vue Router Getting Started](https://router.vuejs.org/guide/)
```

## File: `skills/vue-testing-best-practices/SKILL.md`
```markdown
---
name: vue-testing-best-practices
version: 1.0.0
license: MIT
author: github.com/vuejs-ai
description: Use for Vue.js testing. Covers Vitest, Vue Test Utils, component testing, mocking, testing patterns, and Playwright for E2E testing.
---

Vue.js testing best practices, patterns, and common gotchas.

### Testing
- Setting up test infrastructure for Vue 3 projects → See [testing-vitest-recommended-for-vue](reference/testing-vitest-recommended-for-vue.md)
- Tests keep breaking when refactoring component internals → See [testing-component-blackbox-approach](reference/testing-component-blackbox-approach.md)
- Tests fail intermittently with race conditions → See [testing-async-await-flushpromises](reference/testing-async-await-flushpromises.md)
- Composables using lifecycle hooks or inject fail to test → See [testing-composables-helper-wrapper](reference/testing-composables-helper-wrapper.md)
- Getting "injection Symbol(pinia) not found" errors in tests → See [testing-pinia-store-setup](reference/testing-pinia-store-setup.md)
- Components with async setup won't render in tests → See [testing-suspense-async-components](reference/testing-suspense-async-components.md)
- Snapshot tests keep passing despite broken functionality → See [testing-no-snapshot-only](reference/testing-no-snapshot-only.md)
- Choosing end-to-end testing framework for Vue apps → See [testing-e2e-playwright-recommended](reference/testing-e2e-playwright-recommended.md)
- Tests need to verify computed styles or real DOM events → See [testing-browser-vs-node-runners](reference/testing-browser-vs-node-runners.md)
- Testing components created with defineAsyncComponent fails → See [async-component-testing](reference/async-component-testing.md)
- Teleported modal content can't be found in wrapper queries → See [teleport-testing-complexity](reference/teleport-testing-complexity.md)

## Reference

- [Vue.js Testing Guide](https://vuejs.org/guide/scaling-up/testing)
- [Vue Test Utils](https://test-utils.vuejs.org/)
- [Vitest Documentation](https://vitest.dev/)
- [Playwright Documentation](https://playwright.dev/)
```

## File: `skills/vue-testing-best-practices/reference/async-component-testing.md`
```markdown
---
title: Use flushPromises for Testing Async Components
impact: HIGH
impactDescription: Without awaiting async operations, tests make assertions before the component has rendered, causing false negatives
type: gotcha
tags: [vue3, testing, async, defineAsyncComponent, flushPromises, vitest]
---

# Use flushPromises for Testing Async Components

**Impact: HIGH** - When testing async components created with `defineAsyncComponent`, you must use `await flushPromises()` to ensure the component has loaded before making assertions. Vue updates asynchronously, so tests that don't account for this will make assertions before the component has rendered.

## Task Checklist

- [ ] Use `async/await` in test functions for async components
- [ ] Call `await flushPromises()` after mounting async components
- [ ] Test loading states by making assertions before `flushPromises()`
- [ ] Test error states using rejected promises in `defineAsyncComponent`
- [ ] Use `trigger()` with `await` as it returns a Promise

**Incorrect:**

```javascript
import { mount } from '@vue/test-utils'
import { defineAsyncComponent } from 'vue'

const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue')
)

test('renders async component', () => {
  const wrapper = mount(AsyncWidget)

  // FAILS: Component hasn't loaded yet
  expect(wrapper.text()).toContain('Widget Content')
})
```

**Correct:**

```javascript
import { mount, flushPromises } from '@vue/test-utils'
import { defineAsyncComponent, nextTick } from 'vue'

const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue')
)

test('renders async component', async () => {
  const wrapper = mount(AsyncWidget)

  // Wait for async component to load
  await flushPromises()

  expect(wrapper.text()).toContain('Widget Content')
})

test('shows loading state initially', async () => {
  const AsyncWithLoading = defineAsyncComponent({
    loader: () => import('./Widget.vue'),
    loadingComponent: { template: '<div>Loading...</div>' },
    delay: 0
  })

  const wrapper = mount(AsyncWithLoading)

  // Check loading state immediately
  expect(wrapper.text()).toContain('Loading...')

  // Wait for component to load
  await flushPromises()

  // Check final state
  expect(wrapper.text()).toContain('Widget Content')
})
```

## Testing with Suspense

```javascript
import { mount, flushPromises } from '@vue/test-utils'
import { Suspense, defineAsyncComponent, h } from 'vue'

const AsyncWidget = defineAsyncComponent(() =>
  import('./Widget.vue')
)

test('renders async component with Suspense', async () => {
  const wrapper = mount({
    components: { AsyncWidget },
    template: `
      <Suspense>
        <AsyncWidget />
        <template #fallback>
          <div>Loading...</div>
        </template>
      </Suspense>
    `
  })

  // Initially shows fallback
  expect(wrapper.text()).toContain('Loading...')

  // Wait for async resolution
  await flushPromises()

  // Now shows actual content
  expect(wrapper.text()).toContain('Widget Content')
})
```

## Testing Error States

```javascript
import { mount, flushPromises } from '@vue/test-utils'
import { defineAsyncComponent } from 'vue'

test('shows error component on load failure', async () => {
  const AsyncWithError = defineAsyncComponent({
    loader: () => Promise.reject(new Error('Failed to load')),
    errorComponent: { template: '<div>Error loading component</div>' }
  })

  const wrapper = mount(AsyncWithError)

  await flushPromises()

  expect(wrapper.text()).toContain('Error loading component')
})
```

## Utilities Reference

| Utility | Purpose |
|---------|---------|
| `await flushPromises()` | Resolves all pending promises |
| `await nextTick()` | Waits for Vue's next DOM update cycle |
| `await wrapper.trigger('click')` | Triggers event and waits for update |

## Dynamic Import Handling

**Note:** Dynamic imports (`import('./File.vue')`) may require additional handling beyond `flushPromises()` in test environments. Test runners like Vitest handle module resolution differently than runtime bundlers, which can cause timing issues with dynamic imports. If `flushPromises()` alone doesn't resolve the component, consider:

- Mocking the dynamic import to return the component synchronously
- Using multiple `await flushPromises()` calls in sequence
- Wrapping assertions in `waitFor()` or retry utilities
- Configuring your test runner's module resolution settings

```javascript
// If flushPromises() isn't sufficient, mock the import
vi.mock('./Widget.vue', () => ({
  default: { template: '<div>Widget Content</div>' }
}))

// Or use multiple flush calls for nested async operations
await flushPromises()
await flushPromises()
```

## References

- [Vue Test Utils - Asynchronous Behavior](https://test-utils.vuejs.org/guide/advanced/async-suspense)
- [Vue.js Async Components Documentation](https://vuejs.org/guide/components/async)
```

## File: `skills/vue-testing-best-practices/reference/teleport-testing-complexity.md`
```markdown
---
title: Teleported Content Requires Special Testing Approach
impact: MEDIUM
impactDescription: Vue Test Utils cannot find teleported content using standard wrapper.find() methods
type: gotcha
tags: [vue3, teleport, testing, vue-test-utils]
---

# Teleported Content Requires Special Testing Approach

**Impact: MEDIUM** - Vue Test Utils scopes queries to the mounted component. Teleported content renders outside the component's DOM tree, so `wrapper.find()` cannot locate it. This leads to failing tests and confusion.

## Task Checklist

- [ ] Stub Teleport in unit tests to keep content in component tree
- [ ] Use `document.body` queries for integration tests with real Teleport
- [ ] Consider using `getComponent()` instead of DOM queries for teleported components

**Problem - Standard Testing Fails:**
```vue
<!-- Modal.vue -->
<template>
  <button @click="open = true">Open</button>
  <Teleport to="body">
    <div v-if="open" class="modal" data-testid="modal">
      <input type="text" data-testid="modal-input" />
    </div>
  </Teleport>
</template>
```

```ts
// Modal.spec.ts - BROKEN
import { mount } from '@vue/test-utils'
import Modal from './Modal.vue'

test('modal input exists', async () => {
  const wrapper = mount(Modal)
  await wrapper.find('button').trigger('click')

  // FAILS: Teleported content is not in wrapper's DOM tree
  expect(wrapper.find('[data-testid="modal-input"]').exists()).toBe(true)
})
```

**Solution 1 - Stub Teleport:**
```ts
import { mount } from '@vue/test-utils'
import Modal from './Modal.vue'

test('modal input exists', async () => {
  const wrapper = mount(Modal, {
    global: {
      stubs: {
        // Stub teleport to render content inline
        Teleport: true
      }
    }
  })

  await wrapper.find('button').trigger('click')

  // Works: Content renders inside wrapper
  expect(wrapper.find('[data-testid="modal-input"]').exists()).toBe(true)
})
```

**Solution 2 - Query Document Body:**
```ts
import { mount } from '@vue/test-utils'
import Modal from './Modal.vue'

test('modal renders to body', async () => {
  const wrapper = mount(Modal, {
    attachTo: document.body  // Required for Teleport to work
  })

  await wrapper.find('button').trigger('click')

  // Query the actual DOM
  const modal = document.querySelector('[data-testid="modal"]')
  expect(modal).toBeTruthy()

  const input = document.querySelector('[data-testid="modal-input"]')
  expect(input).toBeTruthy()

  // Cleanup
  wrapper.unmount()
})
```

**Solution 3 - Custom Teleport Stub with Content Access:**
```ts
import { mount, config } from '@vue/test-utils'
import { h, Teleport } from 'vue'
import Modal from './Modal.vue'

// Custom stub that renders content in a testable way
const TeleportStub = {
  setup(props, { slots }) {
    return () => h('div', { class: 'teleport-stub' }, slots.default?.())
  }
}

test('modal with custom stub', async () => {
  const wrapper = mount(Modal, {
    global: {
      stubs: {
        Teleport: TeleportStub
      }
    }
  })

  await wrapper.find('button').trigger('click')

  // Content is inside .teleport-stub
  expect(wrapper.find('.teleport-stub [data-testid="modal-input"]').exists()).toBe(true)
})
```

## Testing Vue Final Modal and UI Libraries

Libraries like Vue Final Modal use Teleport internally, causing test failures:

```ts
// Problem: Vue Final Modal teleports to body
import { VueFinalModal } from 'vue-final-modal'

test('modal content', async () => {
  const wrapper = mount(MyComponent, {
    global: {
      stubs: {
        // Stub the modal component to avoid teleport issues
        VueFinalModal: true
      }
    }
  })
})
```

## E2E Testing (Cypress, Playwright)

E2E tests query the real DOM, so Teleport works naturally:

```ts
// Cypress
it('opens modal', () => {
  cy.visit('/page-with-modal')
  cy.get('button').click()

  // Works: Cypress queries the real DOM
  cy.get('[data-testid="modal"]').should('be.visible')
})
```

## Reference
- [Vue Test Utils - Teleport](https://test-utils.vuejs.org/guide/advanced/teleport)
- [Vue Test Utils - Stubs](https://test-utils.vuejs.org/guide/advanced/stubs-shallow-mount)
```

## File: `skills/vue-testing-best-practices/reference/testing-async-await-flushpromises.md`
```markdown
---
title: Properly Handle Async Updates with nextTick and flushPromises
impact: HIGH
impactDescription: Race conditions and flaky tests occur when async DOM updates or API calls complete after assertions run
type: gotcha
tags: [vue3, testing, async, flushPromises, nextTick, vitest, vue-test-utils, race-condition]
---

# Properly Handle Async Updates with nextTick and flushPromises

**Impact: HIGH** - Vue updates the DOM asynchronously. Without properly awaiting these updates, tests may assert against stale DOM state, causing intermittent failures and false negatives.

Use `await` with triggers and `setValue`, use `nextTick` for reactive updates, and use `flushPromises` for external async operations like API calls.

## Task Checklist

- [ ] Always await `trigger()` and `setValue()` calls
- [ ] Use `await nextTick()` after programmatic reactive state changes
- [ ] Use `await flushPromises()` for external async operations (API calls, timers)
- [ ] Don't chain multiple `nextTick` calls - use `flushPromises` instead
- [ ] Consider using `waitFor` from testing-library for polling assertions

**Incorrect:**
```javascript
import { mount } from '@vue/test-utils'
import SearchComponent from './SearchComponent.vue'

// BAD: Not awaiting trigger - assertion runs before DOM updates
test('search filters results', () => {
  const wrapper = mount(SearchComponent)

  wrapper.find('input').setValue('vue')  // Missing await!
  wrapper.find('button').trigger('click')  // Missing await!

  // This assertion likely fails - DOM hasn't updated yet
  expect(wrapper.findAll('.result').length).toBe(3)
})

// BAD: Using nextTick for API calls
test('loads data from API', async () => {
  const wrapper = mount(DataLoader)

  await nextTick()  // This won't wait for the API call!

  // Assertion runs before fetch completes
  expect(wrapper.find('.data').text()).toBe('Loaded data')
})
```

**Correct:**
```javascript
import { mount, flushPromises } from '@vue/test-utils'
import { nextTick } from 'vue'
import SearchComponent from './SearchComponent.vue'
import DataLoader from './DataLoader.vue'

// CORRECT: Await trigger and setValue
test('search filters results', async () => {
  const wrapper = mount(SearchComponent)

  await wrapper.find('input').setValue('vue')
  await wrapper.find('button').trigger('click')

  expect(wrapper.findAll('.result').length).toBe(3)
})

// CORRECT: Use flushPromises for API calls
test('loads data from API', async () => {
  const wrapper = mount(DataLoader)

  // Wait for all pending promises to resolve
  await flushPromises()

  expect(wrapper.find('.data').text()).toBe('Loaded data')
})
```

## When to Use Each Method

### `await trigger()` / `await setValue()` - User Interactions
```javascript
// These methods return nextTick internally
await wrapper.find('button').trigger('click')
await wrapper.find('input').setValue('new value')
await wrapper.find('form').trigger('submit')
```

### `await nextTick()` - Programmatic Reactive Updates
```javascript
import { nextTick } from 'vue'

test('reflects programmatic state changes', async () => {
  const wrapper = mount(Counter)

  // Direct state modification (when testing with exposed internals)
  wrapper.vm.count = 5

  await nextTick()  // Wait for Vue to update DOM

  expect(wrapper.find('.count').text()).toBe('5')
})
```

### `await flushPromises()` - External Async Operations
```javascript
import { flushPromises } from '@vue/test-utils'

test('displays fetched data', async () => {
  const wrapper = mount(UserProfile, {
    props: { userId: 1 }
  })

  // Wait for component's API call to complete
  await flushPromises()

  expect(wrapper.find('.username').text()).toBe('John')
})

// Sometimes you need multiple flushPromises for chained async operations
test('processes data after fetch', async () => {
  const wrapper = mount(DataProcessor)

  await flushPromises()  // Wait for fetch
  await flushPromises()  // Wait for processing triggered by fetch

  expect(wrapper.find('.processed').exists()).toBe(true)
})
```

## Common Pattern: Combining Methods
```javascript
test('submits form and shows success', async () => {
  const wrapper = mount(ContactForm)

  // Fill form (awaiting each interaction)
  await wrapper.find('#name').setValue('John')
  await wrapper.find('#email').setValue('john@example.com')

  // Submit form
  await wrapper.find('form').trigger('submit')

  // Wait for API submission to complete
  await flushPromises()

  // Assert success state
  expect(wrapper.find('.success-message').exists()).toBe(true)
})
```

## Testing with MSW or Mock APIs
```javascript
import { flushPromises } from '@vue/test-utils'
import { rest } from 'msw'
import { setupServer } from 'msw/node'

const server = setupServer(
  rest.get('/api/user', (req, res, ctx) => {
    return res(ctx.json({ name: 'John' }))
  })
)

test('displays user data', async () => {
  const wrapper = mount(UserCard)

  // MSW might require multiple flushPromises
  await flushPromises()
  await flushPromises()

  expect(wrapper.find('.name').text()).toBe('John')
})
```

## Reference
- [Vue Test Utils - Asynchronous Behavior](https://test-utils.vuejs.org/guide/advanced/async-suspense)
- [Vue.js Testing Guide](https://vuejs.org/guide/scaling-up/testing)
```

## File: `skills/vue-testing-best-practices/reference/testing-browser-vs-node-runners.md`
```markdown
---
title: Choose Browser-Based Runner for Style and DOM Event Testing
impact: MEDIUM
impactDescription: Node-based runners cannot test real CSS behavior, native DOM events, cookies, or computed styles
type: capability
tags: [vue3, testing, component-testing, vitest, browser, jsdom]
---

# Choose Browser-Based Runner for Style and DOM Event Testing

**Impact: MEDIUM** - Node-based test runners (Vitest with jsdom/happy-dom) simulate the DOM but cannot test real CSS rendering, native browser events, cookies, computed styles, or cross-browser behavior. Use browser-based runners when these matter.

Use Vitest for most component tests (fast), but use Vitest Browser Mode when testing visual/DOM-dependent features.

## Task Checklist

- [ ] Use Vitest (node) for logic-focused component tests
- [ ] Use Vitest Browser Mode for style-dependent tests
- [ ] Use Vitest Browser Mode for native events (focus, drag, resize)
- [ ] Use Vitest Browser Mode for cookies and computed CSS styles
- [ ] Accept slower speed tradeoff for browser accuracy

## When to Use Each Approach

### Node-Based Runner (Vitest + happy-dom/jsdom)
Best for:
- Pure logic testing
- State management
- Event emission
- Props/slots behavior
- Most component interactions
- Fast CI/CD pipelines

```javascript
// vitest.config.js
export default defineConfig({
  test: {
    environment: 'happy-dom',  // or 'jsdom'
  }
})
```

```javascript
// Fast but limited - fine for most tests
test('button emits click event', async () => {
  const wrapper = mount(Button)
  await wrapper.trigger('click')
  expect(wrapper.emitted('click')).toBeTruthy()
})
```

### Vitest Browser Mode
Required for:
- CSS computed styles verification
- CSS transitions/animations
- Real focus/blur behavior
- Drag and drop
- Cookie operations
- Viewport-dependent behavior
- Cross-browser validation

## Vitest Browser Mode Setup

```bash
npm install -D @vitest/browser playwright
```

```javascript
// vitest.config.js
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      name: 'chromium',
      provider: 'playwright',
    },
  },
})
```

```javascript
// Button.browser.test.js
import { render } from 'vitest-browser-vue'
import Button from './Button.vue'

test('has correct hover styling', async () => {
  const { getByRole } = render(Button, { props: { label: 'Click me' } })

  const button = getByRole('button')

  // Check initial style
  await expect.element(button).toHaveStyle({
    backgroundColor: 'rgb(59, 130, 246)'  // blue
  })
})

test('maintains focus after click', async () => {
  const { getByRole } = render(Button)

  const button = getByRole('button')
  await button.click()

  await expect.element(button).toHaveFocus()
})
```

## Examples: What Each Runner Can/Cannot Test

### Styles - Browser Required
```javascript
// Node runner: CANNOT verify actual CSS
test('danger button has red background', () => {
  const wrapper = mount(Button, { props: { variant: 'danger' } })
  // This only checks class exists, not actual color
  expect(wrapper.classes()).toContain('bg-red-500')
})

// Vitest Browser Mode: CAN verify computed styles
test('danger button renders red', async () => {
  const { getByRole } = render(Button, { props: { variant: 'danger' } })
  await expect.element(getByRole('button')).toHaveStyle({
    backgroundColor: 'rgb(239, 68, 68)'
  })
})
```

### Computed CSS Styles - Browser Required
```javascript
// Node runner: CANNOT get real computed styles
test('button has correct padding', () => {
  const wrapper = mount(Button)
  // getComputedStyle returns empty/default values in jsdom
  const style = window.getComputedStyle(wrapper.element)
  // style.padding will be empty string, not actual computed value
})

// Vitest Browser Mode: Real computed styles
test('button has correct padding', async () => {
  const { getByRole } = render(Button)
  const button = getByRole('button')

  await expect.element(button).toHaveStyle({
    padding: '12px 24px'
  })
})
```

### Native Events - Browser Required
```javascript
// Node runner: Synthetic events only
test('handles drag and drop', async () => {
  const wrapper = mount(DraggableList)
  // trigger('dragstart') is synthetic - may not work as expected
  await wrapper.find('.item').trigger('dragstart')
})

// Vitest Browser Mode: Real native events via userEvent
import { userEvent } from '@vitest/browser/context'

test('reorders items on drag', async () => {
  const { getByTestId } = render(DraggableList)

  const item = getByTestId('item-1')
  const target = getByTestId('item-3')

  await userEvent.dragAndDrop(item, target)

  // Assert reordering
})
```

## Recommended Testing Strategy

```javascript
// vitest.config.js - Separate test configurations

export default defineConfig({
  test: {
    // Default: Node environment for speed
    environment: 'happy-dom',

    // Browser tests in separate directory
    include: ['src/**/*.test.{js,ts}'],
  },
})

// Run browser tests separately
// npx vitest --browser.enabled
```

### Directory Structure
```
tests/
├── unit/              # Fast node-based tests
│   ├── Button.test.js
│   └── useCounter.test.js
├── component/         # Slower browser-based tests
│   ├── Button.browser.test.js
│   └── DragDrop.browser.test.js
└── e2e/               # Full E2E tests (Playwright)
    └── user-flow.spec.ts
```

## Reference
- [Vue.js Testing - Component Testing](https://vuejs.org/guide/scaling-up/testing#component-testing)
- [Vitest Browser Mode](https://vitest.dev/guide/browser.html)
```

## File: `skills/vue-testing-best-practices/reference/testing-component-blackbox-approach.md`
```markdown
---
title: Test Components Using Blackbox Approach - Focus on Behavior Not Implementation
impact: HIGH
impactDescription: Implementation-aware tests become brittle and break during refactoring, leading to high maintenance burden
type: best-practice
tags: [vue3, testing, component-testing, vitest, vue-test-utils, blackbox]
---

# Test Components Using Blackbox Approach - Focus on Behavior Not Implementation

**Impact: HIGH** - Tests that rely on implementation details (internal state, private methods, component structure) break during refactoring even when functionality remains correct. This leads to false negatives and high test maintenance burden.

Follow Kent C. Dodds' testing philosophy: "The more your tests resemble how your software is used, the more confidence they can give you."

## Task Checklist

- [ ] Test what the component does, not how it does it
- [ ] Query elements by user-visible attributes (text, role, testid)
- [ ] Simulate user interactions (click, type) rather than calling methods directly
- [ ] Assert on rendered output, emitted events, and visible state changes
- [ ] Avoid accessing component internal state or private methods
- [ ] Use data-testid attributes for elements without semantic meaning

**Incorrect:**
```javascript
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

// BAD: Testing implementation details
test('counter increments', async () => {
  const wrapper = mount(Counter)

  // Accessing internal state directly
  expect(wrapper.vm.count).toBe(0)

  // Calling internal method instead of simulating user action
  wrapper.vm.increment()

  // Checking internal state instead of visible output
  expect(wrapper.vm.count).toBe(1)
})

// BAD: Testing component structure
test('has increment button', () => {
  const wrapper = mount(Counter)

  // Testing implementation detail - what if button becomes an anchor?
  expect(wrapper.find('button').exists()).toBe(true)
})
```

**Correct:**
```javascript
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

// CORRECT: Testing behavior like a user would
test('counter displays updated value after clicking increment', async () => {
  const wrapper = mount(Counter, {
    props: { max: 10 }
  })

  // Assert initial visible state
  expect(wrapper.find('[data-testid="counter-value"]').text()).toContain('0')

  // Simulate user action
  await wrapper.find('[data-testid="increment-button"]').trigger('click')

  // Assert visible result
  expect(wrapper.find('[data-testid="counter-value"]').text()).toContain('1')
})

// CORRECT: Testing emitted events (public API)
test('emits change event with new value when incremented', async () => {
  const wrapper = mount(Counter)

  await wrapper.find('[data-testid="increment-button"]').trigger('click')

  expect(wrapper.emitted('change')).toHaveLength(1)
  expect(wrapper.emitted('change')[0]).toEqual([1])
})
```

## Using @testing-library/vue for Better Blackbox Tests

```javascript
import { render, screen, fireEvent } from '@testing-library/vue'
import Counter from './Counter.vue'

// Testing Library encourages accessible, user-centric queries
test('increments counter on button click', async () => {
  render(Counter)

  // Query by role - how screen readers see it
  const button = screen.getByRole('button', { name: /increment/i })
  const display = screen.getByText('0')

  await fireEvent.click(button)

  expect(screen.getByText('1')).toBeInTheDocument()
})
```

## What to Test vs What Not to Test

### DO Test (Public Interface)
```javascript
// Props affect rendered output
test('shows title from props', () => {
  const wrapper = mount(Card, {
    props: { title: 'Hello World' }
  })
  expect(wrapper.text()).toContain('Hello World')
})

// Slots render correctly
test('renders slot content', () => {
  const wrapper = mount(Card, {
    slots: { default: '<p>Slot content</p>' }
  })
  expect(wrapper.text()).toContain('Slot content')
})

// Emitted events
test('emits close event when X clicked', async () => {
  const wrapper = mount(Modal)
  await wrapper.find('[data-testid="close-button"]').trigger('click')
  expect(wrapper.emitted('close')).toBeTruthy()
})
```

### DON'T Test (Implementation Details)
```javascript
// Don't test internal computed properties
// Don't test internal methods
// Don't test component options/setup internals
// Don't test that specific child components are rendered (unless critical)
// Don't rely exclusively on snapshot tests for correctness
```

## Reference
- [Vue.js Testing Guide](https://vuejs.org/guide/scaling-up/testing)
- [Vue Test Utils - Testing Philosophy](https://test-utils.vuejs.org/guide/)
- [Testing Library Guiding Principles](https://testing-library.com/docs/guiding-principles)
```

## File: `skills/vue-testing-best-practices/reference/testing-composables-helper-wrapper.md`
```markdown
---
title: Test Complex Composables with Host Component Wrapper
impact: MEDIUM
impactDescription: Composables using lifecycle hooks or provide/inject fail when tested directly without a component context
type: capability
tags: [vue3, testing, composables, vitest, lifecycle-hooks, provide-inject]
---

# Test Complex Composables with Host Component Wrapper

**Impact: MEDIUM** - Composables that use Vue lifecycle hooks (`onMounted`, `onUnmounted`) or dependency injection (`inject`) require a component context to function. Testing them directly will cause errors or incorrect behavior.

Simple composables using only reactivity APIs can be tested directly. Complex composables need a helper function that creates a host component context.

## Task Checklist

- [ ] Identify if composable uses lifecycle hooks or inject
- [ ] For simple composables (refs, computed only): test directly
- [ ] For complex composables: use `withSetup` helper pattern
- [ ] Clean up by unmounting the test app after each test
- [ ] Use `app.provide()` to mock injected dependencies

**Simple Composable - Test Directly:**
```javascript
// composables/useCounter.js
import { ref, computed } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  const doubled = computed(() => count.value * 2)
  const increment = () => count.value++

  return { count, doubled, increment }
}
```

```javascript
// useCounter.test.js
import { describe, it, expect } from 'vitest'
import { useCounter } from './useCounter'

// CORRECT: Simple composable can be tested directly
describe('useCounter', () => {
  it('initializes with default value', () => {
    const { count } = useCounter()
    expect(count.value).toBe(0)
  })

  it('increments count', () => {
    const { count, increment } = useCounter()
    increment()
    expect(count.value).toBe(1)
  })

  it('computes doubled value', () => {
    const { count, doubled, increment } = useCounter(5)
    expect(doubled.value).toBe(10)
    increment()
    expect(doubled.value).toBe(12)
  })
})
```

**Complex Composable - Use Host Wrapper:**
```javascript
// composables/useFetch.js
import { ref, onMounted, onUnmounted, inject } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const loading = ref(true)
  let controller = null

  // Uses inject - needs component context
  const apiClient = inject('apiClient')

  // Uses lifecycle hooks - needs component context
  onMounted(async () => {
    controller = new AbortController()
    try {
      const response = await apiClient.get(url, { signal: controller.signal })
      data.value = response.data
    } catch (e) {
      if (e.name !== 'AbortError') error.value = e
    } finally {
      loading.value = false
    }
  })

  onUnmounted(() => {
    controller?.abort()
  })

  return { data, error, loading }
}
```

```javascript
// test-utils.js
import { createApp } from 'vue'

/**
 * Helper to test composables that need component context
 */
export function withSetup(composable) {
  let result

  const app = createApp({
    setup() {
      result = composable()
      // Return a render function to suppress warnings
      return () => {}
    }
  })

  app.mount(document.createElement('div'))

  return [result, app]
}
```

```javascript
// useFetch.test.js
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { flushPromises } from '@vue/test-utils'
import { withSetup } from './test-utils'
import { useFetch } from './useFetch'

describe('useFetch', () => {
  let app
  const mockApiClient = {
    get: vi.fn()
  }

  afterEach(() => {
    // IMPORTANT: Clean up to trigger onUnmounted
    app?.unmount()
  })

  it('fetches data on mount', async () => {
    mockApiClient.get.mockResolvedValue({ data: { id: 1, name: 'Test' } })

    const [result, testApp] = withSetup(() => useFetch('/api/test'))
    app = testApp

    // Provide mocked dependency
    app.provide('apiClient', mockApiClient)

    // Wait for async operations
    await flushPromises()

    expect(result.data.value).toEqual({ id: 1, name: 'Test' })
    expect(result.loading.value).toBe(false)
    expect(result.error.value).toBeNull()
  })

  it('handles errors', async () => {
    const testError = new Error('Network error')
    mockApiClient.get.mockRejectedValue(testError)

    const [result, testApp] = withSetup(() => useFetch('/api/test'))
    app = testApp
    app.provide('apiClient', mockApiClient)

    await flushPromises()

    expect(result.error.value).toBe(testError)
    expect(result.data.value).toBeNull()
  })
})
```

## Enhanced withSetup Helper with Provide Support
```javascript
// test-utils.js
export function withSetup(composable, options = {}) {
  let result

  const app = createApp({
    setup() {
      result = composable()
      return () => {}
    }
  })

  // Apply global provides before mounting
  if (options.provide) {
    Object.entries(options.provide).forEach(([key, value]) => {
      app.provide(key, value)
    })
  }

  app.mount(document.createElement('div'))

  return [result, app]
}

// Usage
const [result, app] = withSetup(() => useMyComposable(), {
  provide: {
    apiClient: mockApiClient,
    currentUser: { id: 1, name: 'Test User' }
  }
})
```

## Testing with @vue/test-utils mount
```javascript
import { mount } from '@vue/test-utils'
import { defineComponent } from 'vue'
import { useFetch } from './useFetch'

test('useFetch in component context', async () => {
  const TestComponent = defineComponent({
    setup() {
      const { data, loading } = useFetch('/api/users')
      return { data, loading }
    },
    template: '<div>{{ loading ? "Loading..." : data }}</div>'
  })

  const wrapper = mount(TestComponent, {
    global: {
      provide: {
        apiClient: mockApiClient
      }
    }
  })

  await flushPromises()
  expect(wrapper.text()).toContain('Test data')
})
```

## Reference
- [Vue.js Testing Guide - Testing Composables](https://vuejs.org/guide/scaling-up/testing#testing-composables)
- [Vue Test Utils - Mounting Components](https://test-utils.vuejs.org/guide/)
```

## File: `skills/vue-testing-best-practices/reference/testing-e2e-playwright-recommended.md`
```markdown
---
title: Use Playwright for E2E Testing - Cross-Browser Support and Better DX
impact: MEDIUM
impactDescription: Cypress has browser limitations and some features require paid subscriptions
type: best-practice
tags: [vue3, testing, e2e, playwright, cypress, end-to-end]
---

# Use Playwright for E2E Testing - Cross-Browser Support and Better DX

**Impact: MEDIUM** - Playwright offers superior cross-browser testing (Chromium, WebKit, Firefox), excellent debugging tools, and is fully open source. Cypress has limitations with WebKit support and requires paid subscriptions for some features.

Use Playwright for new E2E testing setups. Consider Cypress if team already has expertise or for its visual debugging UI.

## Task Checklist

- [ ] Install Playwright with browsers for your target platforms
- [ ] Configure for Vue dev server integration
- [ ] Set up projects for different browsers
- [ ] Use locator strategies that match component test patterns
- [ ] Configure CI for parallel test execution
- [ ] Use trace and screenshot features for debugging

## Quick Setup

```bash
# Install Playwright
npm init playwright@latest

# This will create:
# - playwright.config.ts
# - tests/ directory
# - tests-examples/ directory
```

**playwright.config.ts:**
```typescript
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',

  use: {
    // Base URL for navigation
    baseURL: 'http://localhost:5173',
    // Capture trace on first retry
    trace: 'on-first-retry',
    // Screenshot on failure
    screenshot: 'only-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    // Mobile viewports
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
  ],

  // Run local dev server before tests
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:5173',
    reuseExistingServer: !process.env.CI,
  },
})
```

## E2E Test Example

```typescript
// e2e/user-flow.spec.ts
import { test, expect } from '@playwright/test'

test.describe('User Authentication', () => {
  test('user can log in and see dashboard', async ({ page }) => {
    // Navigate to login
    await page.goto('/login')

    // Fill login form
    await page.getByLabel('Email').fill('user@example.com')
    await page.getByLabel('Password').fill('password123')
    await page.getByRole('button', { name: 'Sign In' }).click()

    // Verify redirect to dashboard
    await expect(page).toHaveURL('/dashboard')
    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible()
  })

  test('shows error for invalid credentials', async ({ page }) => {
    await page.goto('/login')

    await page.getByLabel('Email').fill('wrong@example.com')
    await page.getByLabel('Password').fill('wrongpassword')
    await page.getByRole('button', { name: 'Sign In' }).click()

    await expect(page.getByRole('alert')).toContainText('Invalid credentials')
    await expect(page).toHaveURL('/login')
  })
})
```

## Playwright vs Cypress Comparison

| Feature | Playwright | Cypress |
|---------|------------|---------|
| Browsers | Chromium, Firefox, WebKit | Chromium, Firefox, Electron (WebKit experimental) |
| Cross-browser | Full support | Limited |
| Parallelization | Built-in | Requires Cypress Cloud |
| Open source | Fully | Core only |
| Mobile testing | Device emulation | Limited |
| Debugging | Inspector, trace viewer | Time-travel UI |
| API testing | Built-in | Plugin required |
| Iframes | Full support | Limited |

## Testing Vue Components with Data-Testid

```typescript
// e2e/product-list.spec.ts
import { test, expect } from '@playwright/test'

test('user can add product to cart', async ({ page }) => {
  await page.goto('/products')

  // Use data-testid for reliable selectors
  await page.getByTestId('product-card').first().click()

  // Verify product detail page
  await expect(page.getByTestId('product-title')).toBeVisible()

  // Add to cart
  await page.getByTestId('add-to-cart-button').click()

  // Verify cart updated
  await expect(page.getByTestId('cart-count')).toHaveText('1')
})
```

## Page Object Pattern for Vue Apps

```typescript
// e2e/pages/LoginPage.ts
import { Page, Locator } from '@playwright/test'

export class LoginPage {
  readonly page: Page
  readonly emailInput: Locator
  readonly passwordInput: Locator
  readonly submitButton: Locator
  readonly errorMessage: Locator

  constructor(page: Page) {
    this.page = page
    this.emailInput = page.getByLabel('Email')
    this.passwordInput = page.getByLabel('Password')
    this.submitButton = page.getByRole('button', { name: 'Sign In' })
    this.errorMessage = page.getByRole('alert')
  }

  async goto() {
    await this.page.goto('/login')
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.submitButton.click()
  }
}
```

```typescript
// e2e/auth.spec.ts
import { test, expect } from '@playwright/test'
import { LoginPage } from './pages/LoginPage'

test('successful login', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.goto()
  await loginPage.login('user@example.com', 'password123')

  await expect(page).toHaveURL('/dashboard')
})
```

## Visual Regression Testing

```typescript
test('homepage visual regression', async ({ page }) => {
  await page.goto('/')

  // Full page screenshot comparison
  await expect(page).toHaveScreenshot('homepage.png')

  // Element-specific screenshot
  await expect(page.getByTestId('hero-section')).toHaveScreenshot('hero.png')
})
```

## Running Tests

```bash
# Run all tests
npx playwright test

# Run in headed mode (see browser)
npx playwright test --headed

# Run specific file
npx playwright test e2e/auth.spec.ts

# Run in specific browser
npx playwright test --project=chromium

# Debug mode
npx playwright test --debug

# Generate test from actions
npx playwright codegen localhost:5173
```

## Reference
- [Playwright Documentation](https://playwright.dev/)
- [Vue.js E2E Testing Recommendations](https://vuejs.org/guide/scaling-up/testing#e2e-testing)
- [Playwright Best Practices](https://playwright.dev/docs/best-practices)
```

## File: `skills/vue-testing-best-practices/reference/testing-no-snapshot-only.md`
```markdown
---
title: Avoid Snapshot-Only Tests - They Don't Prove Correctness
impact: MEDIUM
impactDescription: Snapshot tests verify structure but not functionality, leading to false confidence and brittle tests
type: best-practice
tags: [vue3, testing, snapshot, vitest, vue-test-utils, anti-pattern]
---

# Avoid Snapshot-Only Tests - They Don't Prove Correctness

**Impact: MEDIUM** - Snapshot tests only verify that HTML structure hasn't changed - they don't verify that the component works correctly. Relying exclusively on snapshots leads to false confidence and tests that break on any refactoring, even when functionality is preserved.

Use snapshots sparingly for regression detection. Prefer behavioral assertions that test what the component does.

## Task Checklist

- [ ] Don't use snapshots as the only assertion for component behavior
- [ ] Use snapshots for regression detection on stable UI components
- [ ] Always pair snapshots with behavioral assertions
- [ ] Keep snapshots small and focused (avoid full component snapshots)
- [ ] Review snapshot diffs carefully - don't blindly update
- [ ] Consider inline snapshots for small, critical structures

**Incorrect:**
```javascript
import { mount } from '@vue/test-utils'
import UserCard from './UserCard.vue'

// BAD: Snapshot-only test proves nothing about functionality
test('UserCard renders correctly', () => {
  const wrapper = mount(UserCard, {
    props: { user: { name: 'John', email: 'john@example.com' } }
  })

  expect(wrapper.html()).toMatchSnapshot()
})

// This test passes even if:
// - The email isn't clickable
// - The avatar doesn't load
// - User actions are completely broken
// - Accessibility is broken
```

**Correct:**
```javascript
import { mount } from '@vue/test-utils'
import UserCard from './UserCard.vue'

// CORRECT: Test actual behavior
test('UserCard displays user information', () => {
  const wrapper = mount(UserCard, {
    props: { user: { name: 'John', email: 'john@example.com' } }
  })

  expect(wrapper.find('[data-testid="user-name"]').text()).toBe('John')
  expect(wrapper.find('[data-testid="user-email"]').text()).toBe('john@example.com')
})

test('UserCard email link is clickable', async () => {
  const wrapper = mount(UserCard, {
    props: { user: { name: 'John', email: 'john@example.com' } }
  })

  const emailLink = wrapper.find('a[href^="mailto:"]')
  expect(emailLink.exists()).toBe(true)
  expect(emailLink.attributes('href')).toBe('mailto:john@example.com')
})

test('UserCard emits select event when clicked', async () => {
  const wrapper = mount(UserCard, {
    props: { user: { id: 1, name: 'John' } }
  })

  await wrapper.trigger('click')

  expect(wrapper.emitted('select')).toBeTruthy()
  expect(wrapper.emitted('select')[0]).toEqual([{ id: 1, name: 'John' }])
})
```

## When Snapshots ARE Useful

### Regression Detection for Stable Components
```javascript
// ACCEPTABLE: Snapshot as additional check, not the only check
test('ErrorBoundary renders error message', () => {
  const wrapper = mount(ErrorBoundary, {
    props: { error: new Error('Something went wrong') }
  })

  // Primary assertions - verify behavior
  expect(wrapper.find('.error-title').text()).toBe('Error')
  expect(wrapper.find('.error-message').text()).toContain('Something went wrong')

  // Secondary snapshot - catches unexpected structural changes
  expect(wrapper.find('.error-container').html()).toMatchSnapshot()
})
```

### Inline Snapshots for Small Structures
```javascript
// ACCEPTABLE: Inline snapshot for small, critical structure
test('generates correct list markup', () => {
  const wrapper = mount(ListItem, { props: { item: 'Test' } })

  expect(wrapper.html()).toMatchInlineSnapshot(`
    "<li class="list-item">Test</li>"
  `)
})
```

### Complex SVG or Icon Output
```javascript
// ACCEPTABLE: Snapshot for complex generated content
test('renders correct chart SVG', () => {
  const wrapper = mount(PieChart, {
    props: { data: [30, 40, 30] }
  })

  // Verify key behavior
  expect(wrapper.findAll('path').length).toBe(3)

  // Snapshot for full SVG structure
  expect(wrapper.find('svg').html()).toMatchSnapshot()
})
```

## Better Alternatives to Snapshots

### Test Specific Elements
```javascript
// Instead of snapshotting entire component
test('renders product with all required fields', () => {
  const wrapper = mount(ProductCard, {
    props: { product: { name: 'Widget', price: 9.99, inStock: true } }
  })

  expect(wrapper.find('.product-name').text()).toBe('Widget')
  expect(wrapper.find('.product-price').text()).toContain('9.99')
  expect(wrapper.find('.in-stock-badge').exists()).toBe(true)
})
```

### Test CSS Classes for Styling
```javascript
test('applies danger styling for errors', () => {
  const wrapper = mount(Alert, {
    props: { type: 'error', message: 'Failed!' }
  })

  expect(wrapper.classes()).toContain('alert-danger')
  expect(wrapper.find('.alert-icon').classes()).toContain('icon-error')
})
```

### Use Testing Library Queries
```javascript
import { render, screen } from '@testing-library/vue'

test('form has accessible labels', () => {
  render(LoginForm)

  // Testing Library queries verify accessibility
  expect(screen.getByLabelText('Email')).toBeInTheDocument()
  expect(screen.getByLabelText('Password')).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Sign In' })).toBeInTheDocument()
})
```

## Snapshot Anti-Patterns

```javascript
// ANTI-PATTERN: Giant component snapshot
test('page renders', () => {
  const wrapper = mount(EntirePageComponent)
  expect(wrapper.html()).toMatchSnapshot()  // 500+ lines of HTML
})

// ANTI-PATTERN: Snapshot with dynamic content
test('shows current date', () => {
  const wrapper = mount(DateDisplay)
  expect(wrapper.html()).toMatchSnapshot()  // Fails every day!
})

// ANTI-PATTERN: Snapshot after every test
test('button works', async () => {
  const wrapper = mount(Counter)
  await wrapper.find('button').trigger('click')
  expect(wrapper.html()).toMatchSnapshot()  // Redundant
})
```

## Reference
- [Vue.js Testing Guide - What Not to Test](https://vuejs.org/guide/scaling-up/testing)
- [Effective Snapshot Testing](https://kentcdodds.com/blog/effective-snapshot-testing)
- [Vitest Snapshot Testing](https://vitest.dev/guide/snapshot.html)
```

## File: `skills/vue-testing-best-practices/reference/testing-pinia-store-setup.md`
```markdown
---
title: Configure Pinia Testing with createTestingPinia and setActivePinia
impact: HIGH
impactDescription: Missing Pinia configuration causes 'injection Symbol(pinia) not found' errors and failing tests
type: gotcha
tags: [vue3, testing, pinia, vitest, store, mocking, createTestingPinia]
---

# Configure Pinia Testing with createTestingPinia and setActivePinia

**Impact: HIGH** - Testing components or composables that use Pinia stores without proper configuration results in "[Vue warn]: injection Symbol(pinia) not found" errors. Tests will fail or behave unexpectedly.

Use `@pinia/testing` package with `createTestingPinia` for component tests and `setActivePinia(createPinia())` for unit testing stores directly.

## Task Checklist

- [ ] Install `@pinia/testing` as a dev dependency
- [ ] Use `createTestingPinia` in component tests with `global.plugins`
- [ ] Use `setActivePinia(createPinia())` in `beforeEach` for store unit tests
- [ ] Configure `createSpy: vi.fn` when NOT using `globals: true` in Vitest
- [ ] Initialize store inside each test to get fresh state
- [ ] Use `stubActions: false` when you need real action execution

**Incorrect:**
```javascript
import { mount } from '@vue/test-utils'
import UserProfile from './UserProfile.vue'

// BAD: Missing Pinia - causes injection error
test('displays user name', () => {
  const wrapper = mount(UserProfile)  // ERROR: injection "Symbol(pinia)" not found
  expect(wrapper.text()).toContain('John')
})
```

```javascript
import { useUserStore } from '@/stores/user'

// BAD: No active Pinia instance
test('user store actions', () => {
  const store = useUserStore()  // ERROR: no active Pinia
  store.login('john', 'password')
})
```

**Correct - Component Testing:**
```javascript
import { mount } from '@vue/test-utils'
import { createTestingPinia } from '@pinia/testing'
import { vi } from 'vitest'
import UserProfile from './UserProfile.vue'
import { useUserStore } from '@/stores/user'

// CORRECT: Provide testing pinia with stubbed actions
test('displays user name', () => {
  const wrapper = mount(UserProfile, {
    global: {
      plugins: [
        createTestingPinia({
          createSpy: vi.fn,  // Required if not using globals: true
          initialState: {
            user: { name: 'John', email: 'john@example.com' }
          }
        })
      ]
    }
  })

  expect(wrapper.text()).toContain('John')
})

// CORRECT: Test with stubbed actions (default behavior)
test('calls logout action', async () => {
  const wrapper = mount(UserProfile, {
    global: {
      plugins: [createTestingPinia({ createSpy: vi.fn })]
    }
  })

  // Get store AFTER mounting with createTestingPinia
  const store = useUserStore()

  await wrapper.find('[data-testid="logout"]').trigger('click')

  // Actions are stubbed and wrapped in spies
  expect(store.logout).toHaveBeenCalled()
})
```

**Correct - Store Unit Testing:**
```javascript
import { describe, it, expect, beforeEach, vi } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useUserStore } from '@/stores/user'

describe('User Store', () => {
  beforeEach(() => {
    // Create fresh Pinia instance for each test
    setActivePinia(createPinia())
  })

  it('initializes with empty user', () => {
    const store = useUserStore()
    expect(store.user).toBeNull()
    expect(store.isLoggedIn).toBe(false)
  })

  it('updates user on login', async () => {
    const store = useUserStore()

    // Real action executes - not stubbed
    await store.login('john', 'password')

    expect(store.user).toEqual({ name: 'John' })
    expect(store.isLoggedIn).toBe(true)
  })

  it('clears user on logout', () => {
    const store = useUserStore()
    store.user = { name: 'John' }  // Set initial state

    store.logout()

    expect(store.user).toBeNull()
  })
})
```

## Testing with Real Actions vs Stubbed Actions

```javascript
import { createTestingPinia } from '@pinia/testing'

// Stubbed actions (default) - for isolation
const wrapper = mount(Component, {
  global: {
    plugins: [
      createTestingPinia({
        createSpy: vi.fn,
        // stubActions: true (default) - actions are mocked
      })
    ]
  }
})

// Real actions - for integration testing
const wrapper = mount(Component, {
  global: {
    plugins: [
      createTestingPinia({
        createSpy: vi.fn,
        stubActions: false  // Actions execute normally
      })
    ]
  }
})
```

## Mocking Specific Action Implementations

```javascript
import { mount } from '@vue/test-utils'
import { createTestingPinia } from '@pinia/testing'
import { vi } from 'vitest'
import { useCartStore } from '@/stores/cart'

test('handles checkout failure', async () => {
  const wrapper = mount(Checkout, {
    global: {
      plugins: [createTestingPinia({ createSpy: vi.fn })]
    }
  })

  const cartStore = useCartStore()

  // Mock specific action behavior
  cartStore.checkout.mockRejectedValue(new Error('Payment failed'))

  await wrapper.find('[data-testid="checkout"]').trigger('click')
  await flushPromises()

  expect(wrapper.find('.error').text()).toContain('Payment failed')
})
```

## Spying on Actions with vi.spyOn

```javascript
import { setActivePinia, createPinia } from 'pinia'
import { vi } from 'vitest'
import { useUserStore } from '@/stores/user'

test('tracks action calls', async () => {
  setActivePinia(createPinia())
  const store = useUserStore()

  const loginSpy = vi.spyOn(store, 'login')
  loginSpy.mockResolvedValue({ success: true })

  await store.login('john', 'password')

  expect(loginSpy).toHaveBeenCalledWith('john', 'password')
})
```

## Testing Store $subscribe

```javascript
import { setActivePinia, createPinia } from 'pinia'
import { useUserStore } from '@/stores/user'

test('subscription triggers on state change', () => {
  setActivePinia(createPinia())
  const store = useUserStore()

  const callback = vi.fn()
  store.$subscribe(callback)

  store.user = { name: 'John' }

  expect(callback).toHaveBeenCalled()
})
```

## Reference
- [Pinia Testing Guide](https://pinia.vuejs.org/cookbook/testing.html)
- [@pinia/testing Package](https://www.npmjs.com/package/@pinia/testing)
- [Vue Test Utils - Plugins](https://test-utils.vuejs.org/guide/advanced/plugins.html)
```

## File: `skills/vue-testing-best-practices/reference/testing-suspense-async-components.md`
```markdown
---
title: Wrap Async Setup Components in Suspense for Testing
impact: HIGH
impactDescription: Components with async setup() fail to render in tests without Suspense wrapper, causing cryptic errors
type: gotcha
tags: [vue3, testing, suspense, async-setup, vue-test-utils, vitest]
---

# Wrap Async Setup Components in Suspense for Testing

**Impact: HIGH** - Components using `async setup()` require a `<Suspense>` wrapper to function correctly. Testing them without Suspense causes the component to never render, leading to test failures and confusing errors.

Create a test wrapper component with Suspense or use a `mountSuspense` helper function for testing async components.

## Task Checklist

- [ ] Identify components with async setup (uses `await` in `<script setup>` or `async setup()`)
- [ ] Create a wrapper component with `<Suspense>` for testing
- [ ] Use `flushPromises()` after mounting to wait for async resolution
- [ ] Access the actual component via `findComponent()` for assertions
- [ ] Consider using `@testing-library/vue` with caution (has Suspense issues)

**Incorrect:**
```javascript
import { mount } from '@vue/test-utils'
import AsyncUserProfile from './AsyncUserProfile.vue'

// BAD: Async component without Suspense wrapper
test('displays user data', async () => {
  // This won't render - Vue expects Suspense wrapper for async setup
  const wrapper = mount(AsyncUserProfile, {
    props: { userId: 1 }
  })

  await flushPromises()

  // This fails - component never rendered
  expect(wrapper.find('.username').text()).toBe('John')
})
```

**Correct - Manual Wrapper Component:**
```javascript
import { mount, flushPromises } from '@vue/test-utils'
import { defineComponent, Suspense } from 'vue'
import AsyncUserProfile from './AsyncUserProfile.vue'

test('displays user data', async () => {
  // Create wrapper component with Suspense
  const TestWrapper = defineComponent({
    components: { AsyncUserProfile },
    template: `
      <Suspense>
        <AsyncUserProfile :user-id="1" />
        <template #fallback>Loading...</template>
      </Suspense>
    `
  })

  const wrapper = mount(TestWrapper)

  // Initially shows fallback
  expect(wrapper.text()).toContain('Loading...')

  // Wait for async setup to complete
  await flushPromises()

  // Find the actual component for detailed assertions
  const profile = wrapper.findComponent(AsyncUserProfile)
  expect(profile.find('.username').text()).toBe('John')
})
```

**Correct - Reusable Helper Function:**
```javascript
// test-utils.js
import { mount, flushPromises } from '@vue/test-utils'
import { defineComponent, Suspense, h } from 'vue'

export async function mountSuspense(component, options = {}) {
  const { props, slots, ...mountOptions } = options

  const wrapper = mount(
    defineComponent({
      render() {
        return h(
          Suspense,
          null,
          {
            default: () => h(component, props, slots),
            fallback: () => h('div', 'Loading...')
          }
        )
      }
    }),
    mountOptions
  )

  // Wait for async component to resolve
  await flushPromises()

  return {
    wrapper,
    // Provide easy access to the actual component
    component: wrapper.findComponent(component)
  }
}
```

```javascript
// AsyncUserProfile.test.js
import { mountSuspense } from './test-utils'
import AsyncUserProfile from './AsyncUserProfile.vue'

test('displays user data', async () => {
  const { component } = await mountSuspense(AsyncUserProfile, {
    props: { userId: 1 },
    global: {
      stubs: {
        // Stub any child components if needed
      }
    }
  })

  expect(component.find('.username').text()).toBe('John')
})

test('handles errors gracefully', async () => {
  const { component } = await mountSuspense(AsyncUserProfile, {
    props: { userId: 'invalid' }
  })

  expect(component.find('.error').exists()).toBe(true)
})
```

## Testing with onErrorCaptured

```javascript
import { mount, flushPromises } from '@vue/test-utils'
import { defineComponent, Suspense, h, ref, onErrorCaptured } from 'vue'
import AsyncComponent from './AsyncComponent.vue'

test('catches async errors', async () => {
  const capturedError = ref(null)

  const TestWrapper = defineComponent({
    setup() {
      onErrorCaptured((error) => {
        capturedError.value = error
        return true // Prevent error propagation
      })
      return { capturedError }
    },
    render() {
      return h(Suspense, null, {
        default: () => h(AsyncComponent, { shouldFail: true }),
        fallback: () => h('div', 'Loading...')
      })
    }
  })

  const wrapper = mount(TestWrapper)
  await flushPromises()

  expect(capturedError.value).toBeTruthy()
  expect(capturedError.value.message).toContain('Failed to load')
})
```

## Using with Nuxt's mountSuspended

```javascript
// If using Nuxt, use the built-in mountSuspended helper
import { mountSuspended } from '@nuxt/test-utils/runtime'
import AsyncPage from './AsyncPage.vue'

test('renders async page', async () => {
  const wrapper = await mountSuspended(AsyncPage, {
    props: { id: 1 }
  })

  expect(wrapper.find('h1').text()).toBe('Page Title')
})
```

## Important Caveats

### @testing-library/vue Limitation
```javascript
// CAUTION: @testing-library/vue has issues with Suspense
// Use @vue/test-utils for async components instead

// If you must use Testing Library, create manual wrapper:
import { render, waitFor } from '@testing-library/vue'

test('async component with testing library', async () => {
  const TestWrapper = {
    template: `
      <Suspense>
        <AsyncComponent />
      </Suspense>
    `,
    components: { AsyncComponent }
  }

  const { getByText } = render(TestWrapper)

  await waitFor(() => {
    expect(getByText('Loaded content')).toBeInTheDocument()
  })
})
```

### Accessing Component Instance
```javascript
test('access vm on async component', async () => {
  const { wrapper, component } = await mountSuspense(AsyncComponent)

  // The wrapper.vm is the Suspense wrapper - not useful
  // Use component.vm for the actual async component
  expect(component.vm.someData).toBe('value')
})
```

## Reference
- [Vue Test Utils - Async Suspense](https://test-utils.vuejs.org/guide/advanced/async-suspense)
- [Vue.js Suspense Documentation](https://vuejs.org/guide/built-ins/suspense.html)
- [Testing Library Vue Suspense Issue](https://github.com/testing-library/vue-testing-library/issues/230)
```

## File: `skills/vue-testing-best-practices/reference/testing-vitest-recommended-for-vue.md`
```markdown
---
title: Use Vitest for Vue 3 Testing - Recommended by Vue Team
impact: MEDIUM
impactDescription: Using Jest or other runners with Vite projects requires complex configuration and causes slower test runs
type: best-practice
tags: [vue3, testing, vitest, vite, configuration, setup]
---

# Use Vitest for Vue 3 Testing - Recommended by Vue Team

**Impact: MEDIUM** - Vitest is created and maintained by Vue/Vite team members and shares the same configuration and transform pipeline as Vite. Using Jest or other test runners with Vite-based projects requires additional configuration and can result in slower test execution and compatibility issues.

Use Vitest for new Vue 3 projects. Only consider Jest if migrating an existing test suite.

## Task Checklist

- [ ] Install Vitest and related packages for Vue testing
- [ ] Configure vitest in vite.config.js or vitest.config.js
- [ ] Set up proper test environment (happy-dom or jsdom)
- [ ] Add test scripts to package.json
- [ ] Configure globals if desired for cleaner test syntax
- [ ] Use @vue/test-utils for component mounting

## Quick Setup

```bash
# Install required packages
npm install -D vitest @vue/test-utils happy-dom
# or with jsdom
npm install -D vitest @vue/test-utils jsdom
```

**vite.config.js:**
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    // Enable global test APIs (describe, it, expect)
    globals: true,
    // Use happy-dom for faster tests (or 'jsdom' for better compatibility)
    environment: 'happy-dom',
    // Optional: Setup files for global configuration
    setupFiles: ['./src/test/setup.js']
  }
})
```

**package.json:**
```json
{
  "scripts": {
    "test": "vitest",
    "test:run": "vitest run",
    "test:coverage": "vitest run --coverage"
  }
}
```

**tsconfig.json (if using TypeScript):**
```json
{
  "compilerOptions": {
    "types": ["vitest/globals"]
  }
}
```

## Test File Example

```javascript
// src/components/Counter.test.js
import { describe, it, expect, beforeEach } from 'vitest'  // optional with globals: true
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

describe('Counter', () => {
  let wrapper

  beforeEach(() => {
    wrapper = mount(Counter)
  })

  it('renders initial count', () => {
    expect(wrapper.find('[data-testid="count"]').text()).toBe('0')
  })

  it('increments when button clicked', async () => {
    await wrapper.find('[data-testid="increment"]').trigger('click')
    expect(wrapper.find('[data-testid="count"]').text()).toBe('1')
  })
})
```

## Vitest vs Jest Comparison

| Feature | Vitest | Jest |
|---------|--------|------|
| Vite Integration | Native | Requires config |
| Speed | Very fast (ESM native) | Slower with Vite |
| Watch Mode | Excellent | Good |
| Vue SFC Support | Works with Vite | Needs vue-jest |
| Config Sharing | Same as vite.config | Separate |
| API | Jest-compatible | Standard |

## Using with Testing Library

```bash
npm install -D @testing-library/vue @testing-library/jest-dom
```

```javascript
// src/test/setup.js
import { expect } from 'vitest'
import * as matchers from '@testing-library/jest-dom/matchers'

expect.extend(matchers)
```

```javascript
// Component.test.js
import { render, screen, fireEvent } from '@testing-library/vue'
import UserCard from './UserCard.vue'

test('displays user name', () => {
  render(UserCard, {
    props: { name: 'John Doe' }
  })

  expect(screen.getByText('John Doe')).toBeInTheDocument()
})
```

## Advanced Configuration

```javascript
// vitest.config.js (separate file if preferred)
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'happy-dom',
    include: ['**/*.{test,spec}.{js,ts,jsx,tsx}'],
    exclude: ['node_modules', 'dist', 'e2e'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules', 'test']
    },
    // Helpful for debugging
    reporters: ['verbose'],
    // Run tests in sequence in CI
    poolOptions: {
      threads: {
        singleThread: process.env.CI === 'true'
      }
    }
  }
})
```

## Common Patterns

### Mocking Modules
```javascript
import { vi } from 'vitest'

vi.mock('@/api/users', () => ({
  fetchUser: vi.fn().mockResolvedValue({ name: 'John' })
}))
```

### Testing with Fake Timers
```javascript
import { vi, beforeEach, afterEach } from 'vitest'

beforeEach(() => {
  vi.useFakeTimers()
})

afterEach(() => {
  vi.restoreAllMocks()
})

test('debounced search', async () => {
  const wrapper = mount(SearchBox)
  await wrapper.find('input').setValue('vue')

  vi.advanceTimersByTime(300)
  await flushPromises()

  expect(wrapper.emitted('search')).toBeTruthy()
})
```

## Reference
- [Vitest Documentation](https://vitest.dev/)
- [Vue.js Testing Guide](https://vuejs.org/guide/scaling-up/testing)
- [Vue Test Utils](https://test-utils.vuejs.org/)
```

