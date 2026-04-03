---
id: github.com-vueuse-skills-451ba643-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:42.626122
---

# KNOWLEDGE EXTRACT: github.com_vueuse_skills_451ba643
> **Extracted on:** 2026-04-01 13:07:11
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522282/github.com_vueuse_skills_451ba643

---

## File: `.gitignore`
```
node_modules
dist
*.log
.DS_Store
```

## File: `.gitmodules`
```
[submodule "vueuse"]
	path = vueuse
	url = https://github.com/vueuse/vueuse
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 SerKo <https://github.com/serkodev>

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
![VueUse Skills banner](./.github/assets/banner.svg)

# VueUse Skills

Agent Skills for [VueUse](https://vueuse.org/) — a collection of essential Vue Composition Utilities.

> [!IMPORTANT]
> Experimental Project: Aims to help AI agents use libraries more accurately with fewer tokens. Feedback is welcome.

- 🪜 Progressive disclosure: send VueUse function overviews first, then load detailed usage and type declarations on demand
- 💰 Minimal token usage: provide only necessary information to reduce token consumption
- 📵 Offline-first design: works without internet access or additional agent permissions
- ⚙️ Customizable policies: users can override function invocation rules in prompts or `AGENTS.md`
- 💉 Reduced hallucinations: precise usage references help prevent invented APIs

## Installation

```bash
npx skills add vueuse/skills
```

### Claude Code Marketplace

An alternative for Claude Code users:

```bash
# Add marketplace
/plugin marketplace add vueuse/skills

# Install individual skills
/plugin install vueuse-functions@vueuse-skills
```

## Example Usage

Install VueUse in your Vue or Nuxt project, then instruct the agent. It will automatically leverage VueUse to assist development.

Example prompt:

```
create a todo app with the following features:
- save todos to local storage
- show remains todo count on browser title
- add a copy button for each todo items
- infinite scrolling for this todo list
- dark / light mode
```

<details>
<summary>Output Snippet</summary>

```vue
<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  useClipboard,
  useColorMode,
  useInfiniteScroll,
  useLocalStorage,
  useTitle,
} from '@vueuse/core'

type Todo = {
  id: number
  text: string
  done: boolean
}

const seedTexts = [
  'Review project goals',
  'Plan the next sprint',
  'Reply to client email',
]

const defaultTodos = Array.from({ length: 36 }, (_, index) => ({
  id: index + 1,
  text:
    seedTexts[index % seedTexts.length] +
    (index >= seedTexts.length ? ` #${index + 1}` : ''),
  done: index % 7 === 0,
}))

const todos = useLocalStorage<Todo[]>('focus-flow-todos', defaultTodos)
const nextId = ref(
  todos.value.reduce((max, todo) => Math.max(max, todo.id), 0) + 1,
)
const newTodo = ref('')

const totalCount = computed(() => todos.value.length)
const remainingCount = computed(() =>
  todos.value.filter((todo) => !todo.done).length,
)
const completedCount = computed(
  () => totalCount.value - remainingCount.value,
)

useTitle(computed(() => `Todos (${remainingCount.value})`))

const mode = useColorMode({
  attribute: 'data-theme',
  disableTransition: false,
})
const isDark = computed(() => mode.value === 'dark')

const toggleMode = () => {
  mode.value = isDark.value ? 'light' : 'dark'
}

const { copy, copied, isSupported } = useClipboard()
const lastCopiedId = ref<number | null>(null)

const handleCopy = async (todo: Todo) => {
  await copy(todo.text)
  lastCopiedId.value = todo.id
}

const pageSize = 8
const visibleCount = ref(Math.min(pageSize, todos.value.length))
const visibleTodos = computed(() => todos.value.slice(0, visibleCount.value))

const listRef = ref<HTMLElement | null>(null)
const { isLoading } = useInfiniteScroll(
  listRef,
  () => {
    if (visibleCount.value < todos.value.length) {
      visibleCount.value = Math.min(
        visibleCount.value + pageSize,
        todos.value.length,
      )
    }
  },
  {
    distance: 120,
    canLoadMore: () => visibleCount.value < todos.value.length,
  },
)

const syncVisibleCount = () => {
  if (todos.value.length <= pageSize) {
    visibleCount.value = todos.value.length
    return
  }

  if (visibleCount.value === 0) {
    visibleCount.value = pageSize
    return
  }

  if (visibleCount.value > todos.value.length) {
    visibleCount.value = todos.value.length
  }
}

const addTodo = () => {
  const value = newTodo.value.trim()
  if (!value)
    return

  todos.value.unshift({
    id: nextId.value++,
    text: value,
    done: false,
  })
  newTodo.value = ''
  syncVisibleCount()
}

const removeTodo = (id: number) => {
  todos.value = todos.value.filter((todo) => todo.id !== id)
  syncVisibleCount()
}
</script>

<template>
  <div class="page">
    <div class="shell">
      <header class="header">
        <div>
          <p class="eyebrow">Minimal todo tracker</p>
          <h1>Focus Flow</h1>
          <p class="subtitle">
            Keep a lightweight list, copy tasks with a click, and scroll as the
            list grows.
          </p>
        </div>
        <button class="btn ghost mode-toggle" type="button" @click="toggleMode">
          <span class="mode-dot" :class="{ dark: isDark }" />
          <span>{{ isDark ? 'Dark' : 'Light' }} mode</span>
        </button>
      </header>

      <form class="composer" @submit.prevent="addTodo">
        <div class="input-wrap">
          <input
            v-model="newTodo"
            type="text"
            maxlength="120"
            placeholder="Add a new task"
            aria-label="Add a new task"
          />
          <button class="btn primary" type="submit" :disabled="!newTodo.trim()">
            Add task
          </button>
        </div>
        <div class="stats">
          <div class="stat">
            <span>Total</span>
            <strong>{{ totalCount }}</strong>
          </div>
          <div class="stat">
            <span>Remaining</span>
            <strong>{{ remainingCount }}</strong>
          </div>
          <div v-if="completedCount" class="stat">
            <span>Done</span>
            <strong>{{ completedCount }}</strong>
          </div>
        </div>
      </form>

      <section class="list-card">
        <div class="list-head">
          <h2>Todo list</h2>
          <span class="list-hint">
            {{ visibleTodos.length }} / {{ totalCount }} shown
          </span>
        </div>
        <div ref="listRef" class="todo-list" aria-live="polite">
          <article
            v-for="(todo, index) in visibleTodos"
            :key="todo.id"
            class="todo-item"
            :class="{ done: todo.done }"
            :style="{ animationDelay: `${index * 0.03}s` }"
          >
            <label class="todo-check">
              <input v-model="todo.done" type="checkbox" />
              <span class="checkmark" />
            </label>
            <p class="todo-text">{{ todo.text }}</p>
            <div class="todo-actions">
              <button
                class="btn ghost"
                type="button"
                :disabled="!isSupported"
                :title="isSupported ? 'Copy task text' : 'Clipboard not supported'"
                @click="handleCopy(todo)"
              >
                {{ copied && lastCopiedId === todo.id ? 'Copied' : 'Copy' }}
              </button>
              <button class="btn danger" type="button" @click="removeTodo(todo.id)">
                Remove
              </button>
            </div>
          </article>

          <p v-if="!visibleTodos.length" class="empty">
            No tasks yet. Add your first todo above.
          </p>

          <div v-if="visibleTodos.length" class="list-footer">
            <span class="footer-status">
              <span v-if="isLoading">Loading more...</span>
              <span v-else-if="visibleTodos.length < totalCount">
                Scroll to load more
              </span>
              <span v-else>All caught up</span>
            </span>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

:root {
  color-scheme: light;
  --bg: #f6f7fb;
  --bg-spot: rgba(59, 130, 246, 0.18);
  --bg-spot-2: rgba(34, 197, 94, 0.18);
  --card: rgba(255, 255, 255, 0.92);
  --surface: rgba(255, 255, 255, 0.84);
  --border: rgba(148, 163, 184, 0.35);
  --text: #0f172a;
  --muted: #64748b;
  --accent: #2563eb;
  --accent-strong: #1d4ed8;
  --accent-soft: rgba(37, 99, 235, 0.18);
  --danger: #ef4444;
  --danger-soft: rgba(239, 68, 68, 0.15);
  --shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
  --radius: 22px;
}

:root[data-theme='dark'] {
  color-scheme: dark;
  --bg: #0b1222;
  --bg-spot: rgba(56, 189, 248, 0.18);
  --bg-spot-2: rgba(16, 185, 129, 0.16);
  --card: rgba(15, 23, 42, 0.86);
  --surface: rgba(15, 23, 42, 0.7);
  --border: rgba(148, 163, 184, 0.25);
  --text: #f8fafc;
  --muted: #94a3b8;
  --accent: #38bdf8;
  --accent-strong: #0ea5e9;
  --accent-soft: rgba(56, 189, 248, 0.2);
  --danger: #f87171;
  --danger-soft: rgba(248, 113, 113, 0.2);
  --shadow: 0 26px 70px rgba(2, 6, 23, 0.55);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: 'Sora', system-ui, -apple-system, sans-serif;
  color: var(--text);
  background:
    radial-gradient(900px circle at top left, var(--bg-spot), transparent 55%),
    radial-gradient(700px circle at bottom right, var(--bg-spot-2), transparent 50%),
    var(--bg);
  transition: background 0.4s ease, color 0.4s ease;
}

#app {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(20px, 4vw, 48px);
}

.page {
  width: min(980px, 100%);
}

.shell {
  display: grid;
  gap: clamp(20px, 3vw, 28px);
  padding: clamp(20px, 4vw, 36px);
  border-radius: var(--radius);
  background: var(--card);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  backdrop-filter: blur(18px);
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-size: 0.72rem;
  color: var(--muted);
  margin: 0 0 10px;
}

h1 {
  margin: 0;
  font-size: clamp(2rem, 3vw, 2.6rem);
}

.subtitle {
  margin: 10px 0 0;
  color: var(--muted);
  max-width: 520px;
}

.composer {
  display: grid;
  gap: 16px;
}

.input-wrap {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
}

input[type='text'] {
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--text);
  font-size: 1rem;
  transition: border 0.2s ease, box-shadow 0.2s ease;
}

input[type='text']:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-soft);
}

.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.stat {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 999px;
  background: var(--surface);
  border: 1px solid var(--border);
  font-size: 0.9rem;
  color: var(--muted);
}

.stat strong {
  font-family: 'Space Mono', ui-monospace, SFMono-Regular, monospace;
  color: var(--text);
  font-size: 0.95rem;
}

.list-card {
  display: grid;
  gap: 16px;
}

.list-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
}

.list-head h2 {
  margin: 0;
  font-size: 1.2rem;
}

.list-hint {
  font-size: 0.85rem;
  color: var(--muted);
  font-family: 'Space Mono', ui-monospace, SFMono-Regular, monospace;
}

.todo-list {
  max-height: clamp(320px, 55vh, 520px);
  overflow-y: auto;
  display: grid;
  gap: 12px;
  padding: 6px;
  margin: -6px;
}

.todo-item {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 14px 16px;
  border-radius: 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  animation: fadeUp 0.4s ease both;
}

.todo-item.done {
  opacity: 0.7;
}

.todo-text {
  margin: 0;
  font-size: 0.98rem;
}

.todo-item.done .todo-text {
  text-decoration: line-through;
  color: var(--muted);
}

.todo-check {
  display: inline-flex;
  align-items: center;
}

.todo-check input {
  width: 18px;
  height: 18px;
  accent-color: var(--accent);
}

.checkmark {
  display: none;
}

.todo-actions {
  display: inline-flex;
  gap: 8px;
  flex-wrap: wrap;
}

.btn {
  border: 1px solid var(--border);
  background: transparent;
  color: var(--text);
  padding: 8px 14px;
  border-radius: 999px;
  font-size: 0.88rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.btn.primary {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
  font-weight: 600;
}

.btn.primary:hover:not(:disabled) {
  background: var(--accent-strong);
  border-color: var(--accent-strong);
}

.btn.ghost:hover:not(:disabled) {
  border-color: var(--accent);
  color: var(--accent);
}

.btn.danger {
  border-color: transparent;
  color: var(--danger);
  background: var(--danger-soft);
}

.mode-toggle {
  white-space: nowrap;
}

.mode-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #facc15;
  box-shadow: 0 0 0 3px rgba(250, 204, 21, 0.2);
}

.mode-dot.dark {
  background: #38bdf8;
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
}

.empty {
  text-align: center;
  padding: 32px 12px;
  color: var(--muted);
  border-radius: 16px;
  border: 1px dashed var(--border);
}

.list-footer {
  text-align: center;
  font-size: 0.85rem;
  color: var(--muted);
  padding: 8px 0 12px;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 820px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
  }

  .input-wrap {
    grid-template-columns: 1fr;
  }

  .todo-item {
    grid-template-columns: auto 1fr;
  }

  .todo-actions {
    grid-column: 1 / -1;
    justify-content: flex-end;
  }
}
</style>
```
</details>

## License

MIT
```

## File: `build.ts`
```typescript
/* eslint-disable no-console */
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import path from 'node:path'
import * as metadata from '@vueuse/metadata'
import { getTypeDefinition } from './vueuse/scripts/utils'

type FunctionInvocation = 'AUTO' | 'EXTERNAL' | 'EXPLICIT_ONLY'

interface FunctionReference {
  name: string
  description: string
  reference: string
}

const SKILL_DIR = './skills/vueuse-functions'
const SKILL_REFERENCE_DIR = './references'
const SKILLS_TEMPLATE_PATH = './templates/vueuse-functions-skills.md'
const VUEUSE_ROOT = './vueuse'

const EXPLICIT_ONLY_FUNCTIONS = new Set([
  'get',
  'set',
  'toRef',
])

;(async () => {
  const categories = await prepareFunctionReferences(SKILL_DIR)
  const functionsTable = prepareFunctionsTable(categories)

  // Generate main skills markdown
  let templateContent = readFileSync(SKILLS_TEMPLATE_PATH, 'utf-8')
  templateContent = templateContent.replace('<!-- FUNCTIONS_TABLE_PLACEHOLDER -->', functionsTable)

  const outputPath = path.join(SKILL_DIR, 'SKILL.md')
  writeFileSync(outputPath, templateContent)

  console.log(`Generated skills documentation at: ${outputPath}`)
})()

// Utils

async function prepareFunctionReferences(outDir: string, referenceDir = SKILL_REFERENCE_DIR): Promise<Record<string, FunctionReference[]>> {
  mkdirSync(path.join(outDir, referenceDir), { recursive: true })

  const categories: Record<string, FunctionReference[]> = {}

  for (const catagory of metadata.categoryNames) {
    if (catagory.startsWith('_'))
      continue

    const refs: FunctionReference[] = []

    const functions = metadata.functions.filter(i => i.category === catagory && !i.internal)
    for (const fn of functions) {
      const description = toTitleCase(fn.description?.replace(/\|/g, '\\|') ?? '')

      if (fn.external) {
        refs.push({ name: fn.name, description, reference: fn.external })
        continue
      }

      const docPath = path.join(VUEUSE_ROOT, `packages/${fn.package}/${fn.name}/index.md`)
      if (existsSync(docPath)) {
        const outputPath = path.join(referenceDir, `${fn.name}.md`)
        const docContent = await genFunctionReference(fn.package, fn.name, docPath)
        writeFileSync(path.join(outDir, outputPath), docContent)
        refs.push({ name: fn.name, description, reference: outputPath })
      }
      else {
        console.warn(`Missing doc: ${fn.name}`)
      }
    }

    categories[catagory] = refs
  }
  return categories
}

function prepareFunctionsTable(categories: Record<string, FunctionReference[]>) {
  let table = ''

  for (const [category, functions] of Object.entries(categories)) {
    table += `### ${category}\n\n`
    table += `| Function | Description | Invocation |\n`
    table += `|----------|-------------|------------|\n`

    for (const fn of functions) {
      const invocation = resolveFunctionInvocation(fn.name, category)
      table += `| [\`${fn.name}\`](${fn.reference}) | ${fn.description} | ${invocation} |\n`
    }
    table += `\n`
  }

  return table
}

function resolveFunctionInvocation(name: string, category: string): FunctionInvocation {
  if (EXPLICIT_ONLY_FUNCTIONS.has(name)) {
    return 'EXPLICIT_ONLY'
  }
  if (category.startsWith('@')) {
    return 'EXTERNAL'
  }
  return 'AUTO'
}

function toTitleCase(str: string): string {
  if (!str)
    return str
  const first = str[0]
  if (first < 'a' || first > 'z')
    return str
  return first.toUpperCase() + str.slice(1)
}

async function genFunctionReference(pkg: string, name: string, mdPath: string) {
  const md = readFileSync(mdPath, 'utf-8')
  const types = await getTypeDefinition(pkg, name)
  if (types) {
    return `${md}
## Type Declarations

\`\`\`ts
${types}
\`\`\`
`
  }
  return md
}
```

## File: `eslint.config.js`
```javascript
import antfu from '@antfu/eslint-config'

export default antfu({
  ignores: [
    'skills/**/*.md',
  ],
})
```

## File: `package.json`
```json
{
  "name": "vueuse-skills",
  "type": "module",
  "private": true,
  "packageManager": "pnpm@10.28.1",
  "license": "MIT",
  "scripts": {
    "build": "tsx build.ts",
    "prepare:vueuse": "cd ./vueuse && pnpm install && pnpm run update:full && pnpm -F @vueuse/metadata build",
    "lint": "eslint"
  },
  "dependencies": {
    "@vueuse/metadata": "link:vueuse/packages/metadata"
  },
  "devDependencies": {
    "@antfu/eslint-config": "^7.2.0",
    "@types/node": "^25.0.10",
    "eslint": "^9.39.2",
    "tsx": "^4.21.0"
  }
}
```

## File: `pnpm-workspace.yaml`
```yaml
shellEmulator: true

trustPolicy: no-downgrade

onlyBuiltDependencies:
  - esbuild
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "esnext",
    "lib": ["esnext"],
    "moduleDetection": "force",
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "types": ["node"],
    "strict": true,
    "strictNullChecks": true,
    "esModuleInterop": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "skipDefaultLibCheck": true,
    "skipLibCheck": true
  },
  "include": ["**/*.ts"]
}
```

## File: `skills/vueuse-functions/SKILL.md`
```markdown
---
name: vueuse-functions
description: Apply VueUse composables where appropriate to build concise, maintainable Vue.js / Nuxt features.
license: MIT
metadata:
    author: SerKo <https://github.com/serkodev>
    version: "1.0"
compatibility: Requires Vue 3 (or above) or Nuxt 3 (or above) project
---

# VueUse Functions

This skill is a decision-and-implementation guide for VueUse composables in Vue.js / Nuxt projects. It maps requirements to the most suitable VueUse function, applies the correct usage pattern, and prefers composable-based solutions over bespoke code to keep implementations concise, maintainable, and performant.

## When to Apply

- Apply this skill whenever assisting user development work in Vue.js / Nuxt.
- Always check first whether a VueUse function can implement the requirement.
- Prefer VueUse composables over custom code to improve readability, maintainability, and performance.
- Map requirements to the most appropriate VueUse function and follow the function’s invocation rule.
- Please refer to the `Invocation` field in the below functions table. For example:
  - `AUTO`: Use automatically when applicable.
  - `EXTERNAL`: Use only if the user already installed the required external dependency; otherwise reconsider, and ask to install only if truly needed.
  - `EXPLICIT_ONLY`: Use only when explicitly requested by the user.
  > *NOTE* User instructions in the prompt or `AGENTS.md` may override a function’s default `Invocation` rule.

## Functions

All functions listed below are part of the [VueUse](https://vueuse.org/) library, each section categorizes functions based on their functionality.

IMPORTANT: Each function entry includes a short `Description` and a detailed `Reference`. When using any function, always consult the corresponding document in `./references` for Usage details and Type Declarations.

### State

| Function | Description | Invocation |
|----------|-------------|------------|
| [`createGlobalState`](references/createGlobalState.md) | Keep states in the global scope to be reusable across Vue instances | AUTO |
| [`createInjectionState`](references/createInjectionState.md) | Create global state that can be injected into components | AUTO |
| [`createSharedComposable`](references/createSharedComposable.md) | Make a composable function usable with multiple Vue instances | AUTO |
| [`injectLocal`](references/injectLocal.md) | Extended `inject` with ability to call `provideLocal` to provide the value in the same component | AUTO |
| [`provideLocal`](references/provideLocal.md) | Extended `provide` with ability to call `injectLocal` to obtain the value in the same component | AUTO |
| [`useAsyncState`](references/useAsyncState.md) | Reactive async state | AUTO |
| [`useDebouncedRefHistory`](references/useDebouncedRefHistory.md) | Shorthand for `useRefHistory` with debounced filter | AUTO |
| [`useLastChanged`](references/useLastChanged.md) | Records the timestamp of the last change | AUTO |
| [`useLocalStorage`](references/useLocalStorage.md) | Reactive [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) | AUTO |
| [`useManualRefHistory`](references/useManualRefHistory.md) | Manually track the change history of a ref when the using calls `commit()` | AUTO |
| [`useRefHistory`](references/useRefHistory.md) | Track the change history of a ref | AUTO |
| [`useSessionStorage`](references/useSessionStorage.md) | Reactive [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) | AUTO |
| [`useStorage`](references/useStorage.md) | Create a reactive ref that can be used to access & modify [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) or [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) | AUTO |
| [`useStorageAsync`](references/useStorageAsync.md) | Reactive Storage in with async support | AUTO |
| [`useThrottledRefHistory`](references/useThrottledRefHistory.md) | Shorthand for `useRefHistory` with throttled filter | AUTO |

### Elements

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useActiveElement`](references/useActiveElement.md) | Reactive `document.activeElement` | AUTO |
| [`useDocumentVisibility`](references/useDocumentVisibility.md) | Reactively track [`document.visibilityState`](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState) | AUTO |
| [`useDraggable`](references/useDraggable.md) | Make elements draggable | AUTO |
| [`useDropZone`](references/useDropZone.md) | Create a zone where files can be dropped | AUTO |
| [`useElementBounding`](references/useElementBounding.md) | Reactive [bounding box](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) of an HTML element | AUTO |
| [`useElementSize`](references/useElementSize.md) | Reactive size of an HTML element | AUTO |
| [`useElementVisibility`](references/useElementVisibility.md) | Tracks the visibility of an element within the viewport | AUTO |
| [`useIntersectionObserver`](references/useIntersectionObserver.md) | Detects that a target element's visibility | AUTO |
| [`useMouseInElement`](references/useMouseInElement.md) | Reactive mouse position related to an element | AUTO |
| [`useMutationObserver`](references/useMutationObserver.md) | Watch for changes being made to the DOM tree | AUTO |
| [`useParentElement`](references/useParentElement.md) | Get parent element of the given element | AUTO |
| [`useResizeObserver`](references/useResizeObserver.md) | Reports changes to the dimensions of an Element's content or the border-box | AUTO |
| [`useWindowFocus`](references/useWindowFocus.md) | Reactively track window focus with `window.onfocus` and `window.onblur` events | AUTO |
| [`useWindowScroll`](references/useWindowScroll.md) | Reactive window scroll | AUTO |
| [`useWindowSize`](references/useWindowSize.md) | Reactive window size | AUTO |

### Browser

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useBluetooth`](references/useBluetooth.md) | Reactive [Web Bluetooth API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API) | AUTO |
| [`useBreakpoints`](references/useBreakpoints.md) | Reactive viewport breakpoints | AUTO |
| [`useBroadcastChannel`](references/useBroadcastChannel.md) | Reactive [BroadcastChannel API](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel) | AUTO |
| [`useBrowserLocation`](references/useBrowserLocation.md) | Reactive browser location | AUTO |
| [`useClipboard`](references/useClipboard.md) | Reactive [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) | AUTO |
| [`useClipboardItems`](references/useClipboardItems.md) | Reactive [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) | AUTO |
| [`useColorMode`](references/useColorMode.md) | Reactive color mode (dark / light / customs) with auto data persistence | AUTO |
| [`useCssSupports`](references/useCssSupports.md) | SSR compatible and reactive [`CSS.supports`](https://developer.mozilla.org/docs/Web/API/CSS/supports_static) | AUTO |
| [`useCssVar`](references/useCssVar.md) | Manipulate CSS variables | AUTO |
| [`useDark`](references/useDark.md) | Reactive dark mode with auto data persistence | AUTO |
| [`useEventListener`](references/useEventListener.md) | Use EventListener with ease | AUTO |
| [`useEyeDropper`](references/useEyeDropper.md) | Reactive [EyeDropper API](https://developer.mozilla.org/en-US/docs/Web/API/EyeDropper_API) | AUTO |
| [`useFavicon`](references/useFavicon.md) | Reactive favicon | AUTO |
| [`useFileDialog`](references/useFileDialog.md) | Open file dialog with ease | AUTO |
| [`useFileSystemAccess`](references/useFileSystemAccess.md) | Create and read and write local files with [FileSystemAccessAPI](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API) | AUTO |
| [`useFullscreen`](references/useFullscreen.md) | Reactive [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API) | AUTO |
| [`useGamepad`](references/useGamepad.md) | Provides reactive bindings for the [Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API) | AUTO |
| [`useImage`](references/useImage.md) | Reactive load an image in the browser | AUTO |
| [`useMediaControls`](references/useMediaControls.md) | Reactive media controls for both `audio` and `video` elements | AUTO |
| [`useMediaQuery`](references/useMediaQuery.md) | Reactive [Media Query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Testing_media_queries) | AUTO |
| [`useMemory`](references/useMemory.md) | Reactive Memory Info | AUTO |
| [`useObjectUrl`](references/useObjectUrl.md) | Reactive URL representing an object | AUTO |
| [`usePerformanceObserver`](references/usePerformanceObserver.md) | Observe performance metrics | AUTO |
| [`usePermission`](references/usePermission.md) | Reactive [Permissions API](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API) | AUTO |
| [`usePreferredColorScheme`](references/usePreferredColorScheme.md) | Reactive [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media query | AUTO |
| [`usePreferredContrast`](references/usePreferredContrast.md) | Reactive [prefers-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast) media query | AUTO |
| [`usePreferredDark`](references/usePreferredDark.md) | Reactive dark theme preference | AUTO |
| [`usePreferredLanguages`](references/usePreferredLanguages.md) | Reactive [Navigator Languages](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorLanguage/languages) | AUTO |
| [`usePreferredReducedMotion`](references/usePreferredReducedMotion.md) | Reactive [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) media query | AUTO |
| [`usePreferredReducedTransparency`](references/usePreferredReducedTransparency.md) | Reactive [prefers-reduced-transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-transparency) media query | AUTO |
| [`useScreenOrientation`](references/useScreenOrientation.md) | Reactive [Screen Orientation API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Orientation_API) | AUTO |
| [`useScreenSafeArea`](references/useScreenSafeArea.md) | Reactive `env(safe-area-inset-*)` | AUTO |
| [`useScriptTag`](references/useScriptTag.md) | Creates a script tag | AUTO |
| [`useShare`](references/useShare.md) | Reactive [Web Share API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share) | AUTO |
| [`useSSRWidth`](references/useSSRWidth.md) | Used to set a global viewport width which will be used when rendering SSR components that rely on the viewport width like [`useMediaQuery`](../INDEX.md) or [`useBreakpoints`](../INDEX.md) | AUTO |
| [`useStyleTag`](references/useStyleTag.md) | Inject reactive `style` element in head | AUTO |
| [`useTextareaAutosize`](references/useTextareaAutosize.md) | Automatically update the height of a textarea depending on the content | AUTO |
| [`useTextDirection`](references/useTextDirection.md) | Reactive [dir](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir) of the element's text | AUTO |
| [`useTitle`](references/useTitle.md) | Reactive document title | AUTO |
| [`useUrlSearchParams`](references/useUrlSearchParams.md) | Reactive [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) | AUTO |
| [`useVibrate`](references/useVibrate.md) | Reactive [Vibration API](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API) | AUTO |
| [`useWakeLock`](references/useWakeLock.md) | Reactive [Screen Wake Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Wake_Lock_API) | AUTO |
| [`useWebNotification`](references/useWebNotification.md) | Reactive [Notification](https://developer.mozilla.org/en-US/docs/Web/API/notification) | AUTO |
| [`useWebWorker`](references/useWebWorker.md) | Simple [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) registration and communication | AUTO |
| [`useWebWorkerFn`](references/useWebWorkerFn.md) | Run expensive functions without blocking the UI | AUTO |

### Sensors

| Function | Description | Invocation |
|----------|-------------|------------|
| [`onClickOutside`](references/onClickOutside.md) | Listen for clicks outside of an element | AUTO |
| [`onElementRemoval`](references/onElementRemoval.md) | Fires when the element or any element containing it is removed from the DOM | AUTO |
| [`onKeyStroke`](references/onKeyStroke.md) | Listen for keyboard keystrokes | AUTO |
| [`onLongPress`](references/onLongPress.md) | Listen for a long press on an element | AUTO |
| [`onStartTyping`](references/onStartTyping.md) | Fires when users start typing on non-editable elements | AUTO |
| [`useBattery`](references/useBattery.md) | Reactive [Battery Status API](https://developer.mozilla.org/en-US/docs/Web/API/Battery_Status_API) | AUTO |
| [`useDeviceMotion`](references/useDeviceMotion.md) | Reactive [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent) | AUTO |
| [`useDeviceOrientation`](references/useDeviceOrientation.md) | Reactive [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent) | AUTO |
| [`useDevicePixelRatio`](references/useDevicePixelRatio.md) | Reactively track [`window.devicePixelRatio`](https://developer.mozilla.org/docs/Web/API/Window/devicePixelRatio) | AUTO |
| [`useDevicesList`](references/useDevicesList.md) | Reactive [enumerateDevices](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices) listing available input/output devices | AUTO |
| [`useDisplayMedia`](references/useDisplayMedia.md) | Reactive [`mediaDevices.getDisplayMedia`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia) streaming | AUTO |
| [`useElementByPoint`](references/useElementByPoint.md) | Reactive element by point | AUTO |
| [`useElementHover`](references/useElementHover.md) | Reactive element's hover state | AUTO |
| [`useFocus`](references/useFocus.md) | Reactive utility to track or set the focus state of a DOM element | AUTO |
| [`useFocusWithin`](references/useFocusWithin.md) | Reactive utility to track if an element or one of its decendants has focus | AUTO |
| [`useFps`](references/useFps.md) | Reactive FPS (frames per second) | AUTO |
| [`useGeolocation`](references/useGeolocation.md) | Reactive [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) | AUTO |
| [`useIdle`](references/useIdle.md) | Tracks whether the user is being inactive | AUTO |
| [`useInfiniteScroll`](references/useInfiniteScroll.md) | Infinite scrolling of the element | AUTO |
| [`useKeyModifier`](references/useKeyModifier.md) | Reactive [Modifier State](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/getModifierState) | AUTO |
| [`useMagicKeys`](references/useMagicKeys.md) | Reactive keys pressed state | AUTO |
| [`useMouse`](references/useMouse.md) | Reactive mouse position | AUTO |
| [`useMousePressed`](references/useMousePressed.md) | Reactive mouse pressing state | AUTO |
| [`useNavigatorLanguage`](references/useNavigatorLanguage.md) | Reactive [navigator.language](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language) | AUTO |
| [`useNetwork`](references/useNetwork.md) | Reactive [Network status](https://developer.mozilla.org/en-US/docs/Web/API/Network_Information_API) | AUTO |
| [`useOnline`](references/useOnline.md) | Reactive online state | AUTO |
| [`usePageLeave`](references/usePageLeave.md) | Reactive state to show whether the mouse leaves the page | AUTO |
| [`useParallax`](references/useParallax.md) | Create parallax effect easily | AUTO |
| [`usePointer`](references/usePointer.md) | Reactive [pointer state](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) | AUTO |
| [`usePointerLock`](references/usePointerLock.md) | Reactive [pointer lock](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API) | AUTO |
| [`usePointerSwipe`](references/usePointerSwipe.md) | Reactive swipe detection based on [PointerEvents](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent) | AUTO |
| [`useScroll`](references/useScroll.md) | Reactive scroll position and state | AUTO |
| [`useScrollLock`](references/useScrollLock.md) | Lock scrolling of the element | AUTO |
| [`useSpeechRecognition`](references/useSpeechRecognition.md) | Reactive [SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) | AUTO |
| [`useSpeechSynthesis`](references/useSpeechSynthesis.md) | Reactive [SpeechSynthesis](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis) | AUTO |
| [`useSwipe`](references/useSwipe.md) | Reactive swipe detection based on [`TouchEvents`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent) | AUTO |
| [`useTextSelection`](references/useTextSelection.md) | Reactively track user text selection based on [`Window.getSelection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getSelection) | AUTO |
| [`useUserMedia`](references/useUserMedia.md) | Reactive [`mediaDevices.getUserMedia`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) streaming | AUTO |

### Network

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useEventSource`](references/useEventSource.md) | An [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) or [Server-Sent-Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) instance opens a persistent connection to an HTTP server | AUTO |
| [`useFetch`](references/useFetch.md) | Reactive [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) provides the ability to abort requests | AUTO |
| [`useWebSocket`](references/useWebSocket.md) | Reactive [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/WebSocket) client | AUTO |

### Animation

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useAnimate`](references/useAnimate.md) | Reactive [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API) | AUTO |
| [`useInterval`](references/useInterval.md) | Reactive counter that increases on every interval | AUTO |
| [`useIntervalFn`](references/useIntervalFn.md) | Wrapper for `setInterval` with controls | AUTO |
| [`useNow`](references/useNow.md) | Reactive current Date instance | AUTO |
| [`useRafFn`](references/useRafFn.md) | Call function on every `requestAnimationFrame` | AUTO |
| [`useTimeout`](references/useTimeout.md) | Reactive value that becomes `true` after a given time | AUTO |
| [`useTimeoutFn`](references/useTimeoutFn.md) | Wrapper for `setTimeout` with controls | AUTO |
| [`useTimestamp`](references/useTimestamp.md) | Reactive current timestamp | AUTO |
| [`useTransition`](references/useTransition.md) | Transition between values | AUTO |

### Component

| Function | Description | Invocation |
|----------|-------------|------------|
| [`computedInject`](references/computedInject.md) | Combine `computed` and `inject` | AUTO |
| [`createReusableTemplate`](references/createReusableTemplate.md) | Define and reuse template inside the component scope | AUTO |
| [`createTemplatePromise`](references/createTemplatePromise.md) | Template as Promise | AUTO |
| [`templateRef`](references/templateRef.md) | Shorthand for binding ref to template element | AUTO |
| [`tryOnBeforeMount`](references/tryOnBeforeMount.md) | Safe `onBeforeMount` | AUTO |
| [`tryOnBeforeUnmount`](references/tryOnBeforeUnmount.md) | Safe `onBeforeUnmount` | AUTO |
| [`tryOnMounted`](references/tryOnMounted.md) | Safe `onMounted` | AUTO |
| [`tryOnScopeDispose`](references/tryOnScopeDispose.md) | Safe `onScopeDispose` | AUTO |
| [`tryOnUnmounted`](references/tryOnUnmounted.md) | Safe `onUnmounted` | AUTO |
| [`unrefElement`](references/unrefElement.md) | Retrieves the underlying DOM element from a Vue ref or component instance | AUTO |
| [`useCurrentElement`](references/useCurrentElement.md) | Get the DOM element of current component as a ref | AUTO |
| [`useMounted`](references/useMounted.md) | Mounted state in ref | AUTO |
| [`useTemplateRefsList`](references/useTemplateRefsList.md) | Shorthand for binding refs to template elements and components inside `v-for` | AUTO |
| [`useVirtualList`](references/useVirtualList.md) | Create virtual lists with ease | AUTO |
| [`useVModel`](references/useVModel.md) | Shorthand for v-model binding | AUTO |
| [`useVModels`](references/useVModels.md) | Shorthand for props v-model binding | AUTO |

### Watch

| Function | Description | Invocation |
|----------|-------------|------------|
| [`until`](references/until.md) | Promised one-time watch for changes | AUTO |
| [`watchArray`](references/watchArray.md) | Watch for an array with additions and removals | AUTO |
| [`watchAtMost`](references/watchAtMost.md) | `watch` with the number of times triggered | AUTO |
| [`watchDebounced`](references/watchDebounced.md) | Debounced watch | AUTO |
| [`watchDeep`](references/watchDeep.md) | Shorthand for watching value with `{deep: true}` | AUTO |
| [`watchIgnorable`](references/watchIgnorable.md) | Ignorable watch | AUTO |
| [`watchImmediate`](references/watchImmediate.md) | Shorthand for watching value with `{immediate: true}` | AUTO |
| [`watchOnce`](references/watchOnce.md) | Shorthand for watching value with `{ once: true }` | AUTO |
| [`watchPausable`](references/watchPausable.md) | Pausable watch | AUTO |
| [`watchThrottled`](references/watchThrottled.md) | Throttled watch | AUTO |
| [`watchTriggerable`](references/watchTriggerable.md) | Watch that can be triggered manually | AUTO |
| [`watchWithFilter`](references/watchWithFilter.md) | `watch` with additional EventFilter control | AUTO |
| [`whenever`](references/whenever.md) | Shorthand for watching value to be truthy | AUTO |

### Reactivity

| Function | Description | Invocation |
|----------|-------------|------------|
| [`computedAsync`](references/computedAsync.md) | Computed for async functions | AUTO |
| [`computedEager`](references/computedEager.md) | Eager computed without lazy evaluation | AUTO |
| [`computedWithControl`](references/computedWithControl.md) | Explicitly define the dependencies of computed | AUTO |
| [`createRef`](references/createRef.md) | Returns a `deepRef` or `shallowRef` depending on the `deep` param | AUTO |
| [`extendRef`](references/extendRef.md) | Add extra attributes to Ref | AUTO |
| [`reactify`](references/reactify.md) | Converts plain functions into reactive functions | AUTO |
| [`reactifyObject`](references/reactifyObject.md) | Apply `reactify` to an object | AUTO |
| [`reactiveComputed`](references/reactiveComputed.md) | Computed reactive object | AUTO |
| [`reactiveOmit`](references/reactiveOmit.md) | Reactively omit fields from a reactive object | AUTO |
| [`reactivePick`](references/reactivePick.md) | Reactively pick fields from a reactive object | AUTO |
| [`refAutoReset`](references/refAutoReset.md) | A ref which will be reset to the default value after some time | AUTO |
| [`refDebounced`](references/refDebounced.md) | Debounce execution of a ref value | AUTO |
| [`refDefault`](references/refDefault.md) | Apply default value to a ref | AUTO |
| [`refManualReset`](references/refManualReset.md) | Create a ref with manual reset functionality | AUTO |
| [`refThrottled`](references/refThrottled.md) | Throttle changing of a ref value | AUTO |
| [`refWithControl`](references/refWithControl.md) | Fine-grained controls over ref and its reactivity | AUTO |
| [`syncRef`](references/syncRef.md) | Two-way refs synchronization | AUTO |
| [`syncRefs`](references/syncRefs.md) | Keep target refs in sync with a source ref | AUTO |
| [`toReactive`](references/toReactive.md) | Converts ref to reactive | AUTO |
| [`toRef`](references/toRef.md) | Normalize value/ref/getter to `ref` or `computed` | EXPLICIT_ONLY |
| [`toRefs`](references/toRefs.md) | Extended [`toRefs`](https://vuejs.org/api/reactivity-utilities.html#torefs) that also accepts refs of an object | AUTO |

### Array

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useArrayDifference`](references/useArrayDifference.md) | Reactive get array difference of two arrays | AUTO |
| [`useArrayEvery`](references/useArrayEvery.md) | Reactive `Array.every` | AUTO |
| [`useArrayFilter`](references/useArrayFilter.md) | Reactive `Array.filter` | AUTO |
| [`useArrayFind`](references/useArrayFind.md) | Reactive `Array.find` | AUTO |
| [`useArrayFindIndex`](references/useArrayFindIndex.md) | Reactive `Array.findIndex` | AUTO |
| [`useArrayFindLast`](references/useArrayFindLast.md) | Reactive `Array.findLast` | AUTO |
| [`useArrayIncludes`](references/useArrayIncludes.md) | Reactive `Array.includes` | AUTO |
| [`useArrayJoin`](references/useArrayJoin.md) | Reactive `Array.join` | AUTO |
| [`useArrayMap`](references/useArrayMap.md) | Reactive `Array.map` | AUTO |
| [`useArrayReduce`](references/useArrayReduce.md) | Reactive `Array.reduce` | AUTO |
| [`useArraySome`](references/useArraySome.md) | Reactive `Array.some` | AUTO |
| [`useArrayUnique`](references/useArrayUnique.md) | Reactive unique array | AUTO |
| [`useSorted`](references/useSorted.md) | Reactive sort array | AUTO |

### Time

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useCountdown`](references/useCountdown.md) | Reactive countdown timer in seconds | AUTO |
| [`useDateFormat`](references/useDateFormat.md) | Get the formatted date according to the string of tokens passed in | AUTO |
| [`useTimeAgo`](references/useTimeAgo.md) | Reactive time ago | AUTO |
| [`useTimeAgoIntl`](references/useTimeAgoIntl.md) | Reactive time ago with i18n supported | AUTO |

### Utilities

| Function | Description | Invocation |
|----------|-------------|------------|
| [`createEventHook`](references/createEventHook.md) | Utility for creating event hooks | AUTO |
| [`createUnrefFn`](references/createUnrefFn.md) | Make a plain function accepting ref and raw values as arguments | AUTO |
| [`get`](references/get.md) | Shorthand for accessing `ref.value` | EXPLICIT_ONLY |
| [`isDefined`](references/isDefined.md) | Non-nullish checking type guard for Ref | AUTO |
| [`makeDestructurable`](references/makeDestructurable.md) | Make isomorphic destructurable for object and array at the same time | AUTO |
| [`set`](references/set.md) | Shorthand for `ref.value = x` | EXPLICIT_ONLY |
| [`useAsyncQueue`](references/useAsyncQueue.md) | Executes each asynchronous task sequentially and passes the current task result to the next task | AUTO |
| [`useBase64`](references/useBase64.md) | Reactive base64 transforming | AUTO |
| [`useCached`](references/useCached.md) | Cache a ref with a custom comparator | AUTO |
| [`useCloned`](references/useCloned.md) | Reactive clone of a ref | AUTO |
| [`useConfirmDialog`](references/useConfirmDialog.md) | Creates event hooks to support modals and confirmation dialog chains | AUTO |
| [`useCounter`](references/useCounter.md) | Basic counter with utility functions | AUTO |
| [`useCycleList`](references/useCycleList.md) | Cycle through a list of items | AUTO |
| [`useDebounceFn`](references/useDebounceFn.md) | Debounce execution of a function | AUTO |
| [`useEventBus`](references/useEventBus.md) | A basic event bus | AUTO |
| [`useMemoize`](references/useMemoize.md) | Cache results of functions depending on arguments and keep it reactive | AUTO |
| [`useOffsetPagination`](references/useOffsetPagination.md) | Reactive offset pagination | AUTO |
| [`usePrevious`](references/usePrevious.md) | Holds the previous value of a ref | AUTO |
| [`useStepper`](references/useStepper.md) | Provides helpers for building a multi-step wizard interface | AUTO |
| [`useSupported`](references/useSupported.md) | SSR compatibility `isSupported` | AUTO |
| [`useThrottleFn`](references/useThrottleFn.md) | Throttle execution of a function | AUTO |
| [`useTimeoutPoll`](references/useTimeoutPoll.md) | Use timeout to poll something | AUTO |
| [`useToggle`](references/useToggle.md) | A boolean switcher with utility functions | AUTO |
| [`useToNumber`](references/useToNumber.md) | Reactively convert a string ref to number | AUTO |
| [`useToString`](references/useToString.md) | Reactively convert a ref to string | AUTO |

### @Electron

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useIpcRenderer`](references/useIpcRenderer.md) | Provides [ipcRenderer](https://www.electronjs.org/docs/api/ipc-renderer) and all of its APIs with Vue reactivity | EXTERNAL |
| [`useIpcRendererInvoke`](references/useIpcRendererInvoke.md) | Reactive [ipcRenderer.invoke API](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererinvokechannel-args) result | EXTERNAL |
| [`useIpcRendererOn`](references/useIpcRendererOn.md) | Use [ipcRenderer.on](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendereronchannel-listener) with ease and [ipcRenderer.removeListener](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovelistenerchannel-listener) automatically on unmounted | EXTERNAL |
| [`useZoomFactor`](references/useZoomFactor.md) | Reactive [WebFrame](https://www.electronjs.org/docs/api/web-frame#webframe) zoom factor | EXTERNAL |
| [`useZoomLevel`](references/useZoomLevel.md) | Reactive [WebFrame](https://www.electronjs.org/docs/api/web-frame#webframe) zoom level | EXTERNAL |

### @Firebase

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useAuth`](references/useAuth.md) | Reactive [Firebase Auth](https://firebase.google.com/docs/auth) binding | EXTERNAL |
| [`useFirestore`](references/useFirestore.md) | Reactive [Firestore](https://firebase.google.com/docs/firestore) binding | EXTERNAL |
| [`useRTDB`](references/useRTDB.md) | Reactive [Firebase Realtime Database](https://firebase.google.com/docs/database) binding | EXTERNAL |

### @Head

| Function | Description | Invocation |
|----------|-------------|------------|
| [`createHead`](https://github.com/vueuse/head#api) | Create the head manager instance. | EXTERNAL |
| [`useHead`](https://github.com/vueuse/head#api) | Update head meta tags reactively. | EXTERNAL |

### @Integrations

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useAsyncValidator`](references/useAsyncValidator.md) | Wrapper for [`async-validator`](https://github.com/yiminghe/async-validator) | EXTERNAL |
| [`useAxios`](references/useAxios.md) | Wrapper for [`axios`](https://github.com/axios/axios) | EXTERNAL |
| [`useChangeCase`](references/useChangeCase.md) | Reactive wrapper for [`change-case`](https://github.com/blakeembrey/change-case) | EXTERNAL |
| [`useCookies`](references/useCookies.md) | Wrapper for [`universal-cookie`](https://www.npmjs.com/package/universal-cookie) | EXTERNAL |
| [`useDrauu`](references/useDrauu.md) | Reactive instance for [drauu](https://github.com/antfu/drauu) | EXTERNAL |
| [`useFocusTrap`](references/useFocusTrap.md) | Reactive wrapper for [`focus-trap`](https://github.com/focus-trap/focus-trap) | EXTERNAL |
| [`useFuse`](references/useFuse.md) | Easily implement fuzzy search using a composable with [Fuse.js](https://github.com/krisk/fuse) | EXTERNAL |
| [`useIDBKeyval`](references/useIDBKeyval.md) | Wrapper for [`idb-keyval`](https://www.npmjs.com/package/idb-keyval) | EXTERNAL |
| [`useJwt`](references/useJwt.md) | Wrapper for [`jwt-decode`](https://github.com/auth0/jwt-decode) | EXTERNAL |
| [`useNProgress`](references/useNProgress.md) | Reactive wrapper for [`nprogress`](https://github.com/rstacruz/nprogress) | EXTERNAL |
| [`useQRCode`](references/useQRCode.md) | Wrapper for [`qrcode`](https://github.com/soldair/node-qrcode) | EXTERNAL |
| [`useSortable`](references/useSortable.md) | Wrapper for [`sortable`](https://github.com/SortableJS/Sortable) | EXTERNAL |

### @Math

| Function | Description | Invocation |
|----------|-------------|------------|
| [`createGenericProjection`](references/createGenericProjection.md) | Generic version of `createProjection` | EXTERNAL |
| [`createProjection`](references/createProjection.md) | Reactive numeric projection from one domain to another | EXTERNAL |
| [`logicAnd`](references/logicAnd.md) | `AND` condition for refs | EXTERNAL |
| [`logicNot`](references/logicNot.md) | `NOT` condition for ref | EXTERNAL |
| [`logicOr`](references/logicOr.md) | `OR` conditions for refs | EXTERNAL |
| [`useAbs`](references/useAbs.md) | Reactive `Math.abs` | EXTERNAL |
| [`useAverage`](references/useAverage.md) | Get the average of an array reactively | EXTERNAL |
| [`useCeil`](references/useCeil.md) | Reactive `Math.ceil` | EXTERNAL |
| [`useClamp`](references/useClamp.md) | Reactively clamp a value between two other values | EXTERNAL |
| [`useFloor`](references/useFloor.md) | Reactive `Math.floor` | EXTERNAL |
| [`useMath`](references/useMath.md) | Reactive `Math` methods | EXTERNAL |
| [`useMax`](references/useMax.md) | Reactive `Math.max` | EXTERNAL |
| [`useMin`](references/useMin.md) | Reactive `Math.min` | EXTERNAL |
| [`usePrecision`](references/usePrecision.md) | Reactively set the precision of a number | EXTERNAL |
| [`useProjection`](references/useProjection.md) | Reactive numeric projection from one domain to another | EXTERNAL |
| [`useRound`](references/useRound.md) | Reactive `Math.round` | EXTERNAL |
| [`useSum`](references/useSum.md) | Get the sum of an array reactively | EXTERNAL |
| [`useTrunc`](references/useTrunc.md) | Reactive `Math.trunc` | EXTERNAL |

### @Motion

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useElementStyle`](https://motion.vueuse.org/api/use-element-style) | Sync a reactive object to a target element CSS styling | EXTERNAL |
| [`useElementTransform`](https://motion.vueuse.org/api/use-element-transform) | Sync a reactive object to a target element CSS transform. | EXTERNAL |
| [`useMotion`](https://motion.vueuse.org/api/use-motion) | Putting your components in motion. | EXTERNAL |
| [`useMotionProperties`](https://motion.vueuse.org/api/use-motion-properties) | Access Motion Properties for a target element. | EXTERNAL |
| [`useMotionVariants`](https://motion.vueuse.org/api/use-motion-variants) | Handle the Variants state and selection. | EXTERNAL |
| [`useSpring`](https://motion.vueuse.org/api/use-spring) | Spring animations. | EXTERNAL |

### @Router

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useRouteHash`](references/useRouteHash.md) | Shorthand for a reactive `route.hash` | EXTERNAL |
| [`useRouteParams`](references/useRouteParams.md) | Shorthand for a reactive `route.params` | EXTERNAL |
| [`useRouteQuery`](references/useRouteQuery.md) | Shorthand for a reactive `route.query` | EXTERNAL |

### @RxJS

| Function | Description | Invocation |
|----------|-------------|------------|
| [`from`](references/from.md) | Wrappers around RxJS's [`from()`](https://rxjs.dev/api/index/function/from) and [`fromEvent()`](https://rxjs.dev/api/index/function/fromEvent) to allow them to accept `ref`s | EXTERNAL |
| [`toObserver`](references/toObserver.md) | Sugar function to convert a `ref` into an RxJS [Observer](https://rxjs.dev/guide/observer) | EXTERNAL |
| [`useExtractedObservable`](references/useExtractedObservable.md) | Use an RxJS [`Observable`](https://rxjs.dev/guide/observable) as extracted from one or more composables | EXTERNAL |
| [`useObservable`](references/useObservable.md) | Use an RxJS [`Observable`](https://rxjs.dev/guide/observable) | EXTERNAL |
| [`useSubject`](references/useSubject.md) | Bind an RxJS [`Subject`](https://rxjs.dev/guide/subject) to a `ref` and propagate value changes both ways | EXTERNAL |
| [`useSubscription`](references/useSubscription.md) | Use an RxJS [`Subscription`](https://rxjs.dev/guide/subscription) without worrying about unsubscribing from it or creating memory leaks | EXTERNAL |
| [`watchExtractedObservable`](references/watchExtractedObservable.md) | Watch the values of an RxJS [`Observable`](https://rxjs.dev/guide/observable) as extracted from one or more composables | EXTERNAL |

### @SchemaOrg

| Function | Description | Invocation |
|----------|-------------|------------|
| [`createSchemaOrg`](https://vue-schema-org.netlify.app/api/core/create-schema-org.html) | Create the schema.org manager instance. | EXTERNAL |
| [`useSchemaOrg`](https://vue-schema-org.netlify.app/api/core/use-schema-org.html) | Update schema.org reactively. | EXTERNAL |

### @Sound

| Function | Description | Invocation |
|----------|-------------|------------|
| [`useSound`](https://github.com/vueuse/sound#examples) | Play sound effects reactively. | EXTERNAL |


```

## File: `skills/vueuse-functions/references/computedAsync.md`
```markdown
---
category: Reactivity
alias: asyncComputed
---

# computedAsync

Computed for async functions.

## Usage

```ts
import { computedAsync } from '@vueuse/core'
import { shallowRef } from 'vue'

const name = shallowRef('jack')

const userInfo = computedAsync(
  async () => {
    return await mockLookUp(name.value)
  },
  null, // initial state
)
```

### Evaluation State

Pass a ref to track if the async function is currently evaluating.

```ts
import { computedAsync } from '@vueuse/core'
import { shallowRef } from 'vue'

const evaluating = shallowRef(false)

const userInfo = computedAsync(
  async () => { /* your logic */ },
  null,
  evaluating, // can also be passed via options: { evaluating }
)
```

### onCancel

When the computed source changes before the previous async function resolves, you may want to cancel the previous one. Here is an example showing how to incorporate with the fetch API.

```ts
import { computedAsync } from '@vueuse/core'
import { shallowRef } from 'vue'

const packageName = shallowRef('@vueuse/core')

const downloads = computedAsync(async (onCancel) => {
  const abortController = new AbortController()

  onCancel(() => abortController.abort())

  return await fetch(
    `https://api.npmjs.org/downloads/point/last-week/${packageName.value}`,
    { signal: abortController.signal },
  )
    .then(response => response.ok ? response.json() : { downloads: '—' })
    .then(result => result.downloads)
}, 0)
```

### Lazy

By default, `computedAsync` will start resolving immediately on creation. Specify `lazy: true` to make it start resolving on the first access.

```ts
import { computedAsync } from '@vueuse/core'
import { shallowRef } from 'vue'

const evaluating = shallowRef(false)

const userInfo = computedAsync(
  async () => { /* your logic */ },
  null,
  { lazy: true, evaluating },
)
```

### Error Handling

Use the `onError` callback to handle errors from the async function.

```ts
import { computedAsync } from '@vueuse/core'
import { shallowRef } from 'vue'

const name = shallowRef('jack')

const userInfo = computedAsync(
  async () => {
    return await mockLookUp(name.value)
  },
  null,
  {
    onError(e) {
      console.error('Failed to fetch user info', e)
    },
  },
)
```

### Shallow Ref

By default, `computedAsync` uses `shallowRef` internally. Set `shallow: false` to use a deep ref instead.

```ts
import { computedAsync } from '@vueuse/core'
import { shallowRef } from 'vue'

const name = shallowRef('jack')

const userInfo = computedAsync(
  async () => {
    return await fetchNestedData(name.value)
  },
  null,
  { shallow: false }, // enables deep reactivity
)
```

## Caveats

- Just like Vue's built-in `computed` function, `computedAsync` does dependency tracking and is automatically re-evaluated when dependencies change. Note however that only dependencies referenced in the first call stack are considered for this. In other words: **Dependencies that are accessed asynchronously will not trigger re-evaluation of the async computed value.**

- As opposed to Vue's built-in `computed` function, re-evaluation of the async computed value is triggered whenever dependencies are changing, regardless of whether its result is currently being tracked or not.

## Type Declarations

```ts
/**
 * Handle overlapping async evaluations.
 *
 * @param cancelCallback The provided callback is invoked when a re-evaluation of the computed value is triggered before the previous one finished
 */
export type AsyncComputedOnCancel = (cancelCallback: Fn) => void
export interface AsyncComputedOptions<
  Lazy = boolean,
> extends ConfigurableFlushSync {
  /**
   * Should value be evaluated lazily
   *
   * @default false
   */
  lazy?: Lazy
  /**
   * Ref passed to receive the updated of async evaluation
   */
  evaluating?: Ref<boolean>
  /**
   * Use shallowRef
   *
   * @default true
   */
  shallow?: boolean
  /**
   * Callback when error is caught.
   */
  onError?: (e: unknown) => void
}
/**
 * Create an asynchronous computed dependency.
 *
 * @see https://vueuse.org/computedAsync
 * @param evaluationCallback     The promise-returning callback which generates the computed value
 * @param initialState           The initial state, used until the first evaluation finishes
 * @param optionsOrRef           Additional options or a ref passed to receive the updates of the async evaluation
 */
export declare function computedAsync<T>(
  evaluationCallback: (onCancel: AsyncComputedOnCancel) => T | Promise<T>,
  initialState: T,
  optionsOrRef: AsyncComputedOptions<true>,
): ComputedRef<T>
export declare function computedAsync<T>(
  evaluationCallback: (onCancel: AsyncComputedOnCancel) => T | Promise<T>,
  initialState: undefined,
  optionsOrRef: AsyncComputedOptions<true>,
): ComputedRef<T | undefined>
export declare function computedAsync<T>(
  evaluationCallback: (onCancel: AsyncComputedOnCancel) => T | Promise<T>,
  initialState: T,
  optionsOrRef?: Ref<boolean> | AsyncComputedOptions,
): Ref<T>
export declare function computedAsync<T>(
  evaluationCallback: (onCancel: AsyncComputedOnCancel) => T | Promise<T>,
  initialState?: undefined,
  optionsOrRef?: Ref<boolean> | AsyncComputedOptions,
): Ref<T | undefined>
/** @deprecated use `computedAsync` instead */
export declare const asyncComputed: typeof computedAsync
```
```

## File: `skills/vueuse-functions/references/computedEager.md`
```markdown
---
category: Reactivity
alias: eagerComputed
---

# computedEager

Eager computed without lazy evaluation.

::: info
This function will be removed in future version.
:::

::: tip
Note💡: If you are using Vue 3.4+, you can use `computed` right away, you no longer need this function.
In Vue 3.4+, if the computed new value does not change, `computed`, `effect`, `watch`, `watchEffect`, `render` dependencies will not be triggered.
See: https://github.com/vuejs/core/pull/5912
:::

Learn more at [Vue: When a computed property can be the wrong tool](https://dev.to/linusborg/vue-when-a-computed-property-can-be-the-wrong-tool-195j).

- Use `computed()` when you have a complex calculation going on, which can actually profit from caching and lazy evaluation and should only be (re-)calculated if really necessary.
- Use `computedEager()` when you have a simple operation, with a rarely changing return value – often a boolean.

## Usage

```ts
import { computedEager } from '@vueuse/core'

const todos = ref([])
const hasOpenTodos = computedEager(() => !!todos.length)

console.log(hasOpenTodos.value) // false
toTodos.value.push({ title: 'Learn Vue' })
console.log(hasOpenTodos.value) // true
```

## Type Declarations

```ts
export type ComputedEagerOptions = WatchOptionsBase
export type ComputedEagerReturn<T = any> = Readonly<ShallowRef<T>>
/**
 *
 * @deprecated This function will be removed in future version.
 *
 * Note: If you are using Vue 3.4+, you can straight use computed instead.
 * Because in Vue 3.4+, if computed new value does not change,
 * computed, effect, watch, watchEffect, render dependencies will not be triggered.
 * refer: https://github.com/vuejs/core/pull/5912
 *
 * @param fn effect function
 * @param options WatchOptionsBase
 * @returns readonly shallowRef
 */
export declare function computedEager<T>(
  fn: () => T,
  options?: ComputedEagerOptions,
): ComputedEagerReturn<T>
/** @deprecated use `computedEager` instead */
export declare const eagerComputed: typeof computedEager
```
```

## File: `skills/vueuse-functions/references/computedInject.md`
```markdown
---
category: Component
---

# computedInject

Combine `computed` and `inject`. Useful for creating a computed property based on an injected value.

## Usage

In Provider Component

```ts twoslash include main
import type { InjectionKey, Ref } from 'vue'
import { provide, ref } from 'vue'

interface Item {
  key: number
  value: string
}

export const ArrayKey: InjectionKey<Ref<Item[]>> = Symbol('symbol-key')

const array = ref([{ key: 1, value: '1' }, { key: 2, value: '2' }, { key: 3, value: '3' }])

provide(ArrayKey, array)
```

In Receiver Component

```ts
// @filename: provider.ts
// @include: main
// ---cut---
import { computedInject } from '@vueuse/core'

import { ArrayKey } from './provider'

const computedArray = computedInject(ArrayKey, (source) => {
  const arr = [...source.value]
  arr.unshift({ key: 0, value: 'all' })
  return arr
})
```

### Default Value

You can provide a default value that will be used if the injection key is not provided by a parent component.

```ts
import { computedInject } from '@vueuse/core'

const computedArray = computedInject(
  ArrayKey,
  (source) => {
    return source.value.map(item => item.value)
  },
  ref([]), // default source value
)
```

### Factory Default

Pass `true` as the fourth argument to treat the default value as a factory function.

```ts
import { computedInject } from '@vueuse/core'

const computedArray = computedInject(
  ArrayKey,
  (source) => {
    return source.value.map(item => item.value)
  },
  () => ref([]), // factory function for default
  true, // treat default as factory
)
```

### Writable Computed

You can also create a writable computed property by passing an object with `get` and `set` functions.

```ts
import { computedInject } from '@vueuse/core'

const computedArray = computedInject(ArrayKey, {
  get(source) {
    return source.value.map(item => item.value)
  },
  set(value) {
    // handle setting the value
    console.log('Setting value:', value)
  },
})
```

## Type Declarations

```ts
export type ComputedInjectGetter<T, K> = (
  source: T | undefined,
  oldValue?: K,
) => K
export type ComputedInjectGetterWithDefault<T, K> = (
  source: T,
  oldValue?: K,
) => K
export type ComputedInjectSetter<T> = (v: T) => void
export interface WritableComputedInjectOptions<T, K> {
  get: ComputedInjectGetter<T, K>
  set: ComputedInjectSetter<K>
}
export interface WritableComputedInjectOptionsWithDefault<T, K> {
  get: ComputedInjectGetterWithDefault<T, K>
  set: ComputedInjectSetter<K>
}
export declare function computedInject<T, K = any>(
  key: InjectionKey<T> | string,
  getter: ComputedInjectGetter<T, K>,
): ComputedRef<K | undefined>
export declare function computedInject<T, K = any>(
  key: InjectionKey<T> | string,
  options: WritableComputedInjectOptions<T, K>,
): ComputedRef<K | undefined>
export declare function computedInject<T, K = any>(
  key: InjectionKey<T> | string,
  getter: ComputedInjectGetterWithDefault<T, K>,
  defaultSource: T,
  treatDefaultAsFactory?: false,
): ComputedRef<K>
export declare function computedInject<T, K = any>(
  key: InjectionKey<T> | string,
  options: WritableComputedInjectOptionsWithDefault<T, K>,
  defaultSource: T | (() => T),
  treatDefaultAsFactory: true,
): ComputedRef<K>
```
```

## File: `skills/vueuse-functions/references/computedWithControl.md`
```markdown
---
category: Reactivity
alias: controlledComputed
---

# computedWithControl

Explicitly define the dependencies of computed.

## Usage

```ts twoslash include main
import { computedWithControl } from '@vueuse/core'

const source = ref('foo')
const counter = ref(0)

const computedRef = computedWithControl(
  () => source.value, // watch source, same as `watch`
  () => counter.value, // computed getter, same as `computed`
)
```

With this, the changes of `counter` won't trigger `computedRef` to update but the `source` ref does.

```ts
// @include: main
// ---cut---
console.log(computedRef.value) // 0

counter.value += 1

console.log(computedRef.value) // 0

source.value = 'bar'

console.log(computedRef.value) // 1
```

### Manual Triggering

You can also manually trigger the update of the computed by:

```ts
// @include: main
// ---cut---
const computedRef = computedWithControl(
  () => source.value,
  () => counter.value,
)

computedRef.trigger()
```

### Deep Watch

Unlike `computed`, `computedWithControl` is shallow by default.
You can specify the same options as `watch` to control the behavior:

```ts
const source = ref({ name: 'foo' })

const computedRef = computedWithControl(
  source,
  () => counter.value,
  { deep: true },
)
```

## Type Declarations

```ts
export interface ComputedWithControlRefExtra {
  /**
   * Force update the computed value.
   */
  trigger: () => void
}
export interface ComputedRefWithControl<T>
  extends ComputedRef<T>, ComputedWithControlRefExtra {}
export interface WritableComputedRefWithControl<T>
  extends WritableComputedRef<T>, ComputedWithControlRefExtra {}
export type ComputedWithControlRef<T = any> =
  | ComputedRefWithControl<T>
  | WritableComputedRefWithControl<T>
export declare function computedWithControl<T>(
  source: WatchSource | MultiWatchSources,
  fn: ComputedGetter<T>,
  options?: WatchOptions,
): ComputedRefWithControl<T>
export declare function computedWithControl<T>(
  source: WatchSource | MultiWatchSources,
  fn: WritableComputedOptions<T>,
  options?: WatchOptions,
): WritableComputedRefWithControl<T>
/** @deprecated use `computedWithControl` instead */
export declare const controlledComputed: typeof computedWithControl
```
```

## File: `skills/vueuse-functions/references/createEventHook.md`
```markdown
---
category: Utilities
---

# createEventHook

Utility for creating event hooks

## Usage

Creating a function that uses `createEventHook`

```ts
import { createEventHook } from '@vueuse/core'

export function useMyFetch(url) {
  const fetchResult = createEventHook<Response>()
  const fetchError = createEventHook<any>()

  fetch(url)
    .then(result => fetchResult.trigger(result))
    .catch(error => fetchError.trigger(error.message))

  return {
    onResult: fetchResult.on,
    onError: fetchError.on,
  }
}
```

Using a function that uses `createEventHook`

```vue
<script setup lang="ts">
import { useMyFetch } from './my-fetch-function'

const { onResult, onError } = useMyFetch('my api url')

onResult((result) => {
  console.log(result)
})

onError((error) => {
  console.error(error)
})
</script>
```

## Type Declarations

```ts
/**
 * The source code for this function was inspired by vue-apollo's `useEventHook` util
 * https://github.com/vuejs/vue-apollo/blob/v4/packages/vue-apollo-composable/src/util/useEventHook.ts
 */
type Callback<T> =
  IsAny<T> extends true
    ? (...param: any) => void
    : [T] extends [void]
      ? (...param: unknown[]) => void
      : [T] extends [any[]]
        ? (...param: T) => void
        : (...param: [T, ...unknown[]]) => void
export type EventHookOn<T = any> = (fn: Callback<T>) => {
  off: () => void
}
export type EventHookOff<T = any> = (fn: Callback<T>) => void
export type EventHookTrigger<T = any> = (
  ...param: Parameters<Callback<T>>
) => Promise<unknown[]>
export interface EventHook<T = any> {
  on: EventHookOn<T>
  off: EventHookOff<T>
  trigger: EventHookTrigger<T>
  clear: () => void
}
export type EventHookReturn<T> = EventHook<T>
/**
 * Utility for creating event hooks
 *
 * @see https://vueuse.org/createEventHook
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createEventHook<T = any>(): EventHookReturn<T>
```
```

## File: `skills/vueuse-functions/references/createGenericProjection.md`
```markdown
---
category: '@Math'
---

# createGenericProjection

Generic version of `createProjection`. Accepts a custom projector function to map arbitrary type of domains.

Refer to `createProjection` and `useProjection`

## Type Declarations

```ts
export type ProjectorFunction<F, T> = (
  input: F,
  from: readonly [F, F],
  to: readonly [T, T],
) => T
export type UseProjection<F, T> = (input: MaybeRefOrGetter<F>) => ComputedRef<T>
export declare function createGenericProjection<F = number, T = number>(
  fromDomain: MaybeRefOrGetter<readonly [F, F]>,
  toDomain: MaybeRefOrGetter<readonly [T, T]>,
  projector: ProjectorFunction<F, T>,
): UseProjection<F, T>
```
```

## File: `skills/vueuse-functions/references/createGlobalState.md`
```markdown
---
category: State
related: createSharedComposable
---

# createGlobalState

Keep states in the global scope to be reusable across Vue instances.

## Usage

### Without Persistence (Store in Memory)

```ts
// store.ts
import { createGlobalState } from '@vueuse/core'
import { shallowRef } from 'vue'

export const useGlobalState = createGlobalState(
  () => {
    const count = shallowRef(0)
    return { count }
  }
)
```

A bigger example:

```ts
// store.ts
import { createGlobalState } from '@vueuse/core'
import { computed, shallowRef } from 'vue'

export const useGlobalState = createGlobalState(
  () => {
    // state
    const count = shallowRef(0)

    // getters
    const doubleCount = computed(() => count.value * 2)

    // actions
    function increment() {
      count.value++
    }

    return { count, doubleCount, increment }
  }
)
```

### With Persistence

Store in `localStorage` with `useStorage`:

```ts twoslash include store
// store.ts
import { createGlobalState, useStorage } from '@vueuse/core'

export const useGlobalState = createGlobalState(
  () => useStorage('vueuse-local-storage', 'initialValue'),
)
```

```ts
// @filename: store.ts
// @include: store
// ---cut---
// component.ts
import { useGlobalState } from './store'

export default defineComponent({
  setup() {
    const state = useGlobalState()
    return { state }
  },
})
```

## Type Declarations

```ts
export type CreateGlobalStateReturn<Fn extends AnyFn = AnyFn> = Fn
/**
 * Keep states in the global scope to be reusable across Vue instances.
 *
 * @see https://vueuse.org/createGlobalState
 * @param stateFactory A factory function to create the state
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createGlobalState<Fn extends AnyFn>(
  stateFactory: Fn,
): CreateGlobalStateReturn<Fn>
```
```

## File: `skills/vueuse-functions/references/createInjectionState.md`
```markdown
---
category: State
---

# createInjectionState

Create global state that can be injected into components.

## Usage

```ts twoslash include useCounterStore
// useCounterStore.ts
import { createInjectionState } from '@vueuse/core'
import { computed, shallowRef } from 'vue'

const [useProvideCounterStore, useCounterStore] = createInjectionState((initialValue: number) => {
  // state
  const count = shallowRef(initialValue)

  // getters
  const double = computed(() => count.value * 2)

  // actions
  function increment() {
    count.value++
  }

  return { count, double, increment }
})

export { useProvideCounterStore }

// If you want to hide `useCounterStore` and wrap it in default value logic or throw error logic, please don't export `useCounterStore`
export { useCounterStore }

export function useCounterStoreWithDefaultValue() {
  return useCounterStore() ?? {
    count: shallowRef(0),
    double: shallowRef(0),
    increment: () => {},
  }
}

export function useCounterStoreOrThrow() {
  const counterStore = useCounterStore()
  if (counterStore == null)
    throw new Error('Please call `useProvideCounterStore` on the appropriate parent component')
  return counterStore
}
```

```vue
<!-- RootComponent.vue -->
<script setup lang="ts">
// @filename: useCounterStore.ts
// @include: useCounterStore
// ---cut---
import { useProvideCounterStore } from './useCounterStore'

useProvideCounterStore(0)
</script>

<template>
  <div>
    <slot />
  </div>
</template>
```

```vue
<!-- CountComponent.vue -->
<script setup lang="ts">
// @filename: useCounterStore.ts
// @include: useCounterStore
// ---cut---
import { useCounterStore } from './useCounterStore'

// use non-null assertion operator to ignore the case that store is not provided.
const { count, double } = useCounterStore()!
// if you want to allow component to working without providing store, you can use follow code instead:
// const { count, double } = useCounterStore() ?? { count: shallowRef(0), double: shallowRef(0) }
// also, you can use another hook to provide default value
// const { count, double } = useCounterStoreWithDefaultValue()
// or throw error
// const { count, double } = useCounterStoreOrThrow()
</script>

<template>
  <ul>
    <li>
      count: {{ count }}
    </li>
    <li>
      double: {{ double }}
    </li>
  </ul>
</template>
```

```vue
<!-- ButtonComponent.vue -->
<script setup lang="ts">
// @filename: useCounterStore.ts
// @include: useCounterStore
// ---cut---
import { useCounterStore } from './useCounterStore'

// use non-null assertion operator to ignore the case that store is not provided.
const { increment } = useCounterStore()!
</script>

<template>
  <button @click="increment">
    +
  </button>
</template>
```

## Provide a custom InjectionKey

```ts
// useCounterStore.ts
import { createInjectionState } from '@vueuse/core'
import { computed, shallowRef } from 'vue'

// custom injectionKey
const CounterStoreKey = 'counter-store'

const [useProvideCounterStore, useCounterStore] = createInjectionState((initialValue: number) => {
  // state
  const count = shallowRef(initialValue)

  // getters
  const double = computed(() => count.value * 2)

  // actions
  function increment() {
    count.value++
  }

  return { count, double, increment }
}, { injectionKey: CounterStoreKey })
```

## Provide a custom default value

```ts
// useCounterStore.ts
import { createInjectionState } from '@vueuse/core'
import { computed, shallowRef } from 'vue'

const [useProvideCounterStore, useCounterStore] = createInjectionState((initialValue: number) => {
  // state
  const count = shallowRef(initialValue)

  // getters
  const double = computed(() => count.value * 2)

  // actions
  function increment() {
    count.value++
  }

  return { count, double, increment }
}, { defaultValue: 0 })
```

## Type Declarations

```ts
export type CreateInjectionStateReturn<
  Arguments extends Array<any>,
  Return,
> = Readonly<
  [
    /**
     * Call this function in a provider component to create and provide the state.
     *
     * @param args Arguments passed to the composable
     * @returns The state returned by the composable
     */
    useProvidingState: (...args: Arguments) => Return,
    /**
     * Call this function in a consumer component to inject the state.
     *
     * @returns The injected state, or `undefined` if not provided and no default value was set.
     */
    useInjectedState: () => Return | undefined,
  ]
>
export interface CreateInjectionStateOptions<Return> {
  /**
   * Custom injectionKey for InjectionState
   */
  injectionKey?: string | InjectionKey<Return>
  /**
   * Default value for the InjectionState
   */
  defaultValue?: Return
}
/**
 * Create global state that can be injected into components.
 *
 * @see https://vueuse.org/createInjectionState
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createInjectionState<
  Arguments extends Array<any>,
  Return,
>(
  composable: (...args: Arguments) => Return,
  options?: CreateInjectionStateOptions<Return>,
): CreateInjectionStateReturn<Arguments, Return>
```
```

## File: `skills/vueuse-functions/references/createProjection.md`
```markdown
---
category: '@Math'
related: useProjection, createGenericProjection
---

# createProjection

Reactive numeric projection from one domain to another.

## Usage

```ts
import { createProjection } from '@vueuse/math'

const useProjector = createProjection([0, 10], [0, 100])
const input = ref(0)
const projected = useProjector(input) // projected.value === 0

input.value = 5 // projected.value === 50
input.value = 10 // projected.value === 100
```

## Type Declarations

```ts
export declare function createProjection(
  fromDomain: MaybeRefOrGetter<readonly [number, number]>,
  toDomain: MaybeRefOrGetter<readonly [number, number]>,
  projector?: ProjectorFunction<number, number>,
): UseProjection<number, number>
```
```

## File: `skills/vueuse-functions/references/createRef.md`
```markdown
---
category: Reactivity
---

# createRef

Returns a `deepRef` or `shallowRef` depending on the `deep` param.

## Usage

```ts
import { createRef } from '@vueuse/core'
import { isShallow, ref } from 'vue'

const initialData = 1

const shallowData = createRef(initialData)
const deepData = createRef(initialData, true)

isShallow(shallowData) // true
isShallow(deepData) // false
```

## Type Declarations

```ts
export type CreateRefReturn<
  T = any,
  D extends boolean = false,
> = ShallowOrDeepRef<T, D>
export type ShallowOrDeepRef<
  T = any,
  D extends boolean = false,
> = D extends true ? Ref<T> : ShallowRef<T>
/**
 * Returns a `deepRef` or `shallowRef` depending on the `deep` param.
 *
 * @example createRef(1) // ShallowRef<number>
 * @example createRef(1, false) // ShallowRef<number>
 * @example createRef(1, true) // Ref<number>
 * @example createRef("string") // ShallowRef<string>
 * @example createRef<"A"|"B">("A", true) // Ref<"A"|"B">
 *
 * @param value
 * @param deep
 * @returns the `deepRef` or `shallowRef`
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createRef<T = any, D extends boolean = false>(
  value: T,
  deep?: D,
): CreateRefReturn<T, D>
```
```

## File: `skills/vueuse-functions/references/createReusableTemplate.md`
```markdown
---
category: Component
outline: deep
---

# createReusableTemplate

Define and reuse template inside the component scope.

## Motivation

It's common to have the need to reuse some part of the template. For example:

```vue
<template>
  <dialog v-if="showInDialog">
    <!-- something complex -->
  </dialog>
  <div v-else>
    <!-- something complex -->
  </div>
</template>
```

We'd like to reuse our code as much as possible. So normally we might need to extract those duplicated parts into a component. However, in a separated component you lose the ability to access the local bindings. Defining props and emits for them can be tedious sometimes.

So this function is made to provide a way for defining and reusing templates inside the component scope.

## Usage

In the previous example, we could refactor it to:

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate()
</script>

<template>
  <DefineTemplate>
    <!-- something complex -->
  </DefineTemplate>

  <dialog v-if="showInDialog">
    <ReuseTemplate />
  </dialog>
  <div v-else>
    <ReuseTemplate />
  </div>
</template>
```

- `<DefineTemplate>` will register the template and renders nothing.
- `<ReuseTemplate>` will render the template provided by `<DefineTemplate>`.
- `<DefineTemplate>` must be used before `<ReuseTemplate>`.

> **Note**: It's recommended to extract as separate components whenever possible. Abusing this function might lead to bad practices for your codebase.

### Options API

When using with [Options API](https://vuejs.org/guide/introduction.html#api-styles), you will need to define `createReusableTemplate` outside of the component setup and pass to the `components` option in order to use them in the template.

```vue
<script>
import { createReusableTemplate } from '@vueuse/core'
import { defineComponent } from 'vue'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate()

export default defineComponent({
  components: {
    DefineTemplate,
    ReuseTemplate,
  },
  setup() {
    // ...
  },
})
</script>

<template>
  <DefineTemplate v-slot="{ data, msg, anything }">
    <div>{{ data }} passed from usage</div>
  </DefineTemplate>

  <ReuseTemplate :data="data" msg="The first usage" />
</template>
```

### Passing Data

You can also pass data to the template using slots:

- Use `v-slot="..."` to access the data on `<DefineTemplate>`
- Directly bind the data on `<ReuseTemplate>` to pass them to the template

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate()
</script>

<template>
  <DefineTemplate v-slot="{ data, msg, anything }">
    <div>{{ data }} passed from usage</div>
  </DefineTemplate>

  <ReuseTemplate :data="data" msg="The first usage" />
  <ReuseTemplate :data="anotherData" msg="The second usage" />
  <ReuseTemplate v-bind="{ data: something, msg: 'The third' }" />
</template>
```

### TypeScript Support

`createReusableTemplate` accepts a generic type to provide type support for the data passed to the template:

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

// Comes with pair of `DefineTemplate` and `ReuseTemplate`
const [DefineFoo, ReuseFoo] = createReusableTemplate<{ msg: string }>()

// You can create multiple reusable templates
const [DefineBar, ReuseBar] = createReusableTemplate<{ items: string[] }>()
</script>

<template>
  <DefineFoo v-slot="{ msg }">
    <!-- `msg` is typed as `string` -->
    <div>Hello {{ msg.toUpperCase() }}</div>
  </DefineFoo>

  <ReuseFoo msg="World" />

  <!-- @ts-expect-error Type Error! -->
  <ReuseFoo :msg="1" />
</template>
```

Optionally, if you are not a fan of array destructuring, the following usages are also legal:

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

const { define: DefineFoo, reuse: ReuseFoo } = createReusableTemplate<{
  msg: string
}>()
</script>

<template>
  <DefineFoo v-slot="{ msg }">
    <div>Hello {{ msg.toUpperCase() }}</div>
  </DefineFoo>

  <ReuseFoo msg="World" />
</template>
```

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

const TemplateFoo = createReusableTemplate<{ msg: string }>()
</script>

<template>
  <TemplateFoo.define v-slot="{ msg }">
    <div>Hello {{ msg.toUpperCase() }}</div>
  </TemplateFoo.define>

  <TemplateFoo.reuse msg="World" />
</template>
```

::: warning
Passing boolean props without `v-bind` is not supported. See the [Caveats](#boolean-props) section for more details.
:::

### Props and Attributes

By default, all props and attributes passed to `<ReuseTemplate>` will be passed to the template. If you don't want certain props to be passed to the DOM, you need to define the runtime props:

```ts
import { createReusableTemplate } from '@vueuse/core'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate({
  props: {
    msg: String,
    enable: Boolean,
  }
})
```

If you don't want to pass any props to the template, you can pass the `inheritAttrs` option:

```ts
import { createReusableTemplate } from '@vueuse/core'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate({
  inheritAttrs: false,
})
```

### Passing Slots

It's also possible to pass slots back from `<ReuseTemplate>`. You can access the slots on `<DefineTemplate>` from `$slots`:

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate()
</script>

<template>
  <DefineTemplate v-slot="{ $slots, otherProp }">
    <div some-layout>
      <!-- To render the slot -->
      <component :is="$slots.default" />
    </div>
  </DefineTemplate>

  <ReuseTemplate>
    <div>Some content</div>
  </ReuseTemplate>
  <ReuseTemplate>
    <div>Another content</div>
  </ReuseTemplate>
</template>
```

## Caveats

### Boolean props

As opposed to Vue's behavior, props defined as `boolean` that were passed without `v-bind` or absent will be resolved into an empty string or `undefined` respectively:

```vue
<script setup lang="ts">
import { createReusableTemplate } from '@vueuse/core'

const [DefineTemplate, ReuseTemplate] = createReusableTemplate<{
  value?: boolean
}>()
</script>

<template>
  <DefineTemplate v-slot="{ value }">
    {{ typeof value }}: {{ value }}
  </DefineTemplate>

  <ReuseTemplate :value="true" />
  <!-- boolean: true -->

  <ReuseTemplate :value="false" />
  <!-- boolean: false -->

  <ReuseTemplate value />
  <!-- string: -->

  <ReuseTemplate />
  <!-- undefined: -->
</template>
```

## References

This function is migrated from [vue-reuse-template](https://github.com/antfu/vue-reuse-template).

Existing Vue discussions/issues about reusing template:

- [Discussion on Reusing Templates](https://github.com/vuejs/core/discussions/6898)

Alternative Approaches:

- [Vue Macros - `namedTemplate`](https://vue-macros.sxzz.moe/features/named-template.html)
- [`unplugin-vue-reuse-template`](https://github.com/liulinboyi/unplugin-vue-reuse-template)

## Type Declarations

```ts
type ObjectLiteralWithPotentialObjectLiterals = Record<
  string,
  Record<string, any> | undefined
>
type GenerateSlotsFromSlotMap<
  T extends ObjectLiteralWithPotentialObjectLiterals,
> = {
  [K in keyof T]: Slot<T[K]>
}
export type DefineTemplateComponent<
  Bindings extends Record<string, any>,
  MapSlotNameToSlotProps extends ObjectLiteralWithPotentialObjectLiterals,
> = DefineComponent & {
  new (): {
    $slots: {
      default: (
        _: Bindings & {
          $slots: GenerateSlotsFromSlotMap<MapSlotNameToSlotProps>
        },
      ) => any
    }
  }
}
export type ReuseTemplateComponent<
  Bindings extends Record<string, any>,
  MapSlotNameToSlotProps extends ObjectLiteralWithPotentialObjectLiterals,
> = DefineComponent<Bindings> & {
  new (): {
    $slots: GenerateSlotsFromSlotMap<MapSlotNameToSlotProps>
  }
}
export type ReusableTemplatePair<
  Bindings extends Record<string, any>,
  MapSlotNameToSlotProps extends ObjectLiteralWithPotentialObjectLiterals,
> = [
  DefineTemplateComponent<Bindings, MapSlotNameToSlotProps>,
  ReuseTemplateComponent<Bindings, MapSlotNameToSlotProps>,
] & {
  define: DefineTemplateComponent<Bindings, MapSlotNameToSlotProps>
  reuse: ReuseTemplateComponent<Bindings, MapSlotNameToSlotProps>
}
export interface CreateReusableTemplateOptions<
  Props extends Record<string, any>,
> {
  /**
   * Inherit attrs from reuse component.
   *
   * @default true
   */
  inheritAttrs?: boolean
  /**
   * Props definition for reuse component.
   */
  props?: ComponentObjectPropsOptions<Props>
}
/**
 * This function creates `define` and `reuse` components in pair,
 * It also allow to pass a generic to bind with type.
 *
 * @see https://vueuse.org/createReusableTemplate
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createReusableTemplate<
  Bindings extends Record<string, any>,
  MapSlotNameToSlotProps extends ObjectLiteralWithPotentialObjectLiterals =
    Record<"default", undefined>,
>(
  options?: CreateReusableTemplateOptions<Bindings>,
): ReusableTemplatePair<Bindings, MapSlotNameToSlotProps>
```
```

## File: `skills/vueuse-functions/references/createSharedComposable.md`
```markdown
---
category: State
related: createGlobalState
---

# createSharedComposable

Make a composable function usable with multiple Vue instances.

> [!WARNING]
> When used in a **SSR** environment, `createSharedComposable` will **automatically fallback** to a non-shared version.
> This means every call will create a fresh instance in SSR to avoid [cross-request state pollution](https://vuejs.org/guide/scaling-up/ssr.html#cross-request-state-pollution).

## Usage

```ts
import { createSharedComposable, useMouse } from '@vueuse/core'

const useSharedMouse = createSharedComposable(useMouse)

// CompA.vue
const { x, y } = useSharedMouse()

// CompB.vue - will reuse the previous state and no new event listeners will be registered
const { x, y } = useSharedMouse()
```

## Type Declarations

```ts
export type SharedComposableReturn<T extends AnyFn = AnyFn> = T
/**
 * Make a composable function usable with multiple Vue instances.
 *
 * @see https://vueuse.org/createSharedComposable
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createSharedComposable<Fn extends AnyFn>(
  composable: Fn,
): SharedComposableReturn<Fn>
```
```

## File: `skills/vueuse-functions/references/createTemplatePromise.md`
```markdown
---
category: Component
outline: deep
---

# createTemplatePromise

Template as Promise. Useful for constructing custom Dialogs, Modals, Toasts, etc.

## Usage

```vue
<script setup lang="ts">
import { createTemplatePromise } from '@vueuse/core'

const TemplatePromise = createTemplatePromise<ReturnType>()

async function open() {
  const result = await TemplatePromise.start()
  // button is clicked, result is 'ok'
}
</script>

<template>
  <TemplatePromise v-slot="{ promise, resolve, reject, args }">
    <!-- your UI -->
    <button @click="resolve('ok')">
      OK
    </button>
  </TemplatePromise>
</template>
```

## Features

- **Programmatic** - call your UI as a promise
- **Template** - use Vue template to render, not a new DSL
- **TypeScript** - full type safety via generic type
- **Renderless** - you take full control of the UI
- **Transition** - use support Vue transition

This function is migrated from [vue-template-promise](https://github.com/antfu/vue-template-promise)

## Usage

`createTemplatePromise` returns a **Vue Component** that you can directly use in your template with `<script setup>`

```ts twoslash include main
import { createTemplatePromise } from '@vueuse/core'

const TemplatePromise = createTemplatePromise()
const MyPromise = createTemplatePromise<boolean>() // with generic type
```

In template, use `v-slot` to access the promise and resolve functions.

```vue
<template>
  <TemplatePromise v-slot="{ promise, resolve, reject, args }">
    <!-- you can have anything -->
    <button @click="resolve('ok')">
      OK
    </button>
  </TemplatePromise>
  <MyPromise v-slot="{ promise, resolve, reject, args }">
    <!-- another one -->
  </MyPromise>
</template>
```

The slot will not be rendered initially (similar to `v-if="false"`), until you call the `start` method from the component.

```ts
// @include: main
// ---cut---
const result = await TemplatePromise.start()
```

Once `resolve` or `reject` is called in the template, the promise will be resolved or rejected, returning the value you passed in. Once resolved, the slot will be removed automatically.

### Passing Arguments

You can pass arguments to the `start` with arguments.

```ts twoslash include passing-arguments
import { createTemplatePromise } from '@vueuse/core'

const TemplatePromise = createTemplatePromise<boolean, [string, number]>()
```

```ts
// @include: passing-arguments
// ---cut---
const result = await TemplatePromise.start('hello', 123) // Pr
```

And in the template slot, you can access the arguments via `args` property.

```vue
<template>
  <TemplatePromise v-slot="{ args, resolve }">
    <div>{{ args[0] }}</div>
    <!-- hello -->
    <div>{{ args[1] }}</div>
    <!-- 123 -->
    <button @click="resolve(true)">
      OK
    </button>
  </TemplatePromise>
</template>
```

### Singleton Mode

Use the `singleton` option to ensure only one instance of the promise can be active at a time. If `start` is called while a promise is already active, it will return the existing promise instead of creating a new one.

```ts
import { createTemplatePromise } from '@vueuse/core'

const TemplatePromise = createTemplatePromise<boolean>({
  singleton: true,
})

// These will return the same promise if called in quick succession
const result1 = TemplatePromise.start()
const result2 = TemplatePromise.start() // returns the same promise as result1
```

### Transition

You can use transition to animate the slot.

```vue
<script setup lang="ts">
const TemplatePromise = createTemplatePromise<ReturnType>({
  transition: {
    name: 'fade',
    appear: true,
  },
})
</script>

<template>
  <TemplatePromise v-slot="{ resolve }">
    <!-- your UI -->
    <button @click="resolve('ok')">
      OK
    </button>
  </TemplatePromise>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
```

Learn more about [Vue Transition](https://vuejs.org/guide/built-ins/transition.html).

### Slot Props

The slot provides the following props:

| Prop          | Type                                     | Description                                               |
| ------------- | ---------------------------------------- | --------------------------------------------------------- |
| `promise`     | `Promise<Return> \| undefined`           | The current promise instance                              |
| `resolve`     | `(v: Return \| Promise<Return>) => void` | Resolve the promise with a value                          |
| `reject`      | `(v: any) => void`                       | Reject the promise                                        |
| `args`        | `Args`                                   | Arguments passed to `start()`                             |
| `isResolving` | `boolean`                                | `true` when resolving another promise passed to `resolve` |
| `key`         | `number`                                 | Unique key for list rendering                             |

```vue
<template>
  <TemplatePromise v-slot="{ promise, resolve, reject, args, isResolving }">
    <div v-if="isResolving">
      Loading...
    </div>
    <div v-else>
      <button @click="resolve('ok')">
        OK
      </button>
      <button @click="reject('cancelled')">
        Cancel
      </button>
    </div>
  </TemplatePromise>
</template>
```

## Motivation

The common approach to call a dialog or a modal programmatically would be like this:

```ts
const dialog = useDialog()
const result = await dialog.open({
  title: 'Hello',
  content: 'World',
})
```

This would work by sending these information to the top-level component and let it render the dialog. However, it limits the flexibility you could express in the UI. For example, you could want the title to be red, or have extra buttons, etc. You would end up with a lot of options like:

```ts
const result = await dialog.open({
  title: 'Hello',
  titleClass: 'text-red',
  content: 'World',
  contentClass: 'text-blue text-sm',
  buttons: [
    { text: 'OK', class: 'bg-red', onClick: () => {} },
    { text: 'Cancel', class: 'bg-blue', onClick: () => {} },
  ],
  // ...
})
```

Even this is not flexible enough. If you want more, you might end up with manual render function.

```ts
const result = await dialog.open({
  title: 'Hello',
  contentSlot: () => h(MyComponent, { content }),
})
```

This is like reinventing a new DSL in the script to express the UI template.

So this function allows **expressing the UI in templates instead of scripts**, where it is supposed to be, while still being able to be manipulated programmatically.

## Type Declarations

```ts
export interface TemplatePromiseProps<Return, Args extends any[] = []> {
  /**
   * The promise instance.
   */
  promise: Promise<Return> | undefined
  /**
   * Resolve the promise.
   */
  resolve: (v: Return | Promise<Return>) => void
  /**
   * Reject the promise.
   */
  reject: (v: any) => void
  /**
   * Arguments passed to TemplatePromise.start()
   */
  args: Args
  /**
   * Indicates if the promise is resolving.
   * When passing another promise to `resolve`, this will be set to `true` until the promise is resolved.
   */
  isResolving: boolean
  /**
   * Options passed to createTemplatePromise()
   */
  options: TemplatePromiseOptions
  /**
   * Unique key for list rendering.
   */
  key: number
}
export interface TemplatePromiseOptions {
  /**
   * Determines if the promise can be called only once at a time.
   *
   * @default false
   */
  singleton?: boolean
  /**
   * Transition props for the promise.
   */
  transition?: TransitionGroupProps
}
export type TemplatePromise<
  Return,
  Args extends any[] = [],
> = DefineComponent<object> & {
  new (): {
    $slots: {
      default: (_: TemplatePromiseProps<Return, Args>) => any
    }
  }
} & {
  start: (...args: Args) => Promise<Return>
}
/**
 * Creates a template promise component.
 *
 * @see https://vueuse.org/createTemplatePromise
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createTemplatePromise<Return, Args extends any[] = []>(
  options?: TemplatePromiseOptions,
): TemplatePromise<Return, Args>
```
```

## File: `skills/vueuse-functions/references/createUnrefFn.md`
```markdown
---
category: Utilities
related: reactify
---

# createUnrefFn

Make a plain function accepting ref and raw values as arguments.
Returns the same value the unconverted function returns, with proper typing.

::: tip
Make sure you're using the right tool for the job. Using `reactify`
might be more pertinent in some cases where you want to evaluate the function on each changes of it's arguments.
:::

## Usage

```ts
import { createUnrefFn } from '@vueuse/core'
import { shallowRef } from 'vue'

const url = shallowRef('https://httpbin.org/post')
const data = shallowRef({ foo: 'bar' })

function post(url, data) {
  return fetch(url, { data })
}
const unrefPost = createUnrefFn(post)

post(url, data) /* ❌ Will throw an error because the arguments are refs */
unrefPost(url, data) /* ✔️ Will Work because the arguments will be auto unref */
```

## Type Declarations

```ts
export type UnrefFn<T> = T extends (...args: infer A) => infer R
  ? (
      ...args: {
        [K in keyof A]: MaybeRef<A[K]>
      }
    ) => R
  : never
/**
 * Make a plain function accepting ref and raw values as arguments.
 * Returns the same value the unconverted function returns, with proper typing.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function createUnrefFn<T extends Function>(fn: T): UnrefFn<T>
```
```

## File: `skills/vueuse-functions/references/extendRef.md`
```markdown
---
category: Reactivity
---

# extendRef

Add extra attributes to Ref.

## Usage

> Please note the extra attribute will not be accessible in Vue's template.

```ts
import { extendRef } from '@vueuse/core'
import { shallowRef } from 'vue'

const myRef = shallowRef('content')

const extended = extendRef(myRef, { foo: 'extra data' })

extended.value === 'content'
extended.foo === 'extra data'
```

Refs will be unwrapped and be reactive

```ts
import { extendRef } from '@vueuse/core'
// ---cut---
const myRef = shallowRef('content')
const extraRef = shallowRef('extra')

const extended = extendRef(myRef, { extra: extraRef })

extended.value === 'content'
extended.extra === 'extra'

extended.extra = 'new data' // will trigger update
extraRef.value === 'new data'
```

## Type Declarations

```ts
export type ExtendRefReturn<T = any> = Ref<T>
export interface ExtendRefOptions<Unwrap extends boolean = boolean> {
  /**
   * Is the extends properties enumerable
   *
   * @default false
   */
  enumerable?: boolean
  /**
   * Unwrap for Ref properties
   *
   * @default true
   */
  unwrap?: Unwrap
}
/**
 * Overload 1: Unwrap set to false
 */
export declare function extendRef<
  R extends Ref<any>,
  Extend extends object,
  Options extends ExtendRefOptions<false>,
>(ref: R, extend: Extend, options?: Options): ShallowUnwrapRef<Extend> & R
/**
 * Overload 2: Unwrap unset or set to true
 */
export declare function extendRef<
  R extends Ref<any>,
  Extend extends object,
  Options extends ExtendRefOptions,
>(ref: R, extend: Extend, options?: Options): Extend & R
```
```

## File: `skills/vueuse-functions/references/from.md`
```markdown
---
category: '@RxJS'
---

# from / fromEvent

Wrappers around RxJS's [`from()`](https://rxjs.dev/api/index/function/from) and [`fromEvent()`](https://rxjs.dev/api/index/function/fromEvent) to allow them to accept `ref`s.

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { from, fromEvent, toObserver, useSubscription } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { map, mapTo, takeUntil, withLatestFrom } from 'rxjs/operators'
import { shallowRef, useTemplateRef } from 'vue'

const count = shallowRef(0)
const button = useTemplateRef('buttonRef')

useSubscription(
  interval(1000)
    .pipe(
      mapTo(1),
      takeUntil(fromEvent(button, 'click')),
      withLatestFrom(from(count, {
        immediate: true,
        deep: false,
      })),
      map(([curr, total]) => curr + total),
    )
    .subscribe(toObserver(count)), // same as ).subscribe(val => (count.value = val))
)
```

## from

The `from` function can accept either a standard RxJS `ObservableInput` or a Vue `ref`. When passed a ref, it creates an Observable that emits whenever the ref's value changes.

### Watch Options

When using `from` with a ref, you can pass Vue's `WatchOptions`:

| Option      | Type                        | Description                        |
| ----------- | --------------------------- | ---------------------------------- |
| `immediate` | `boolean`                   | Emit the current value immediately |
| `deep`      | `boolean`                   | Deeply watch nested objects        |
| `flush`     | `'pre' \| 'post' \| 'sync'` | Timing of the callback flush       |

## fromEvent

The `fromEvent` function extends RxJS's `fromEvent` to accept a ref to an element. When the ref's value changes (e.g., after the component mounts), it automatically subscribes to the new element.

```ts no-twoslash
import { fromEvent, useSubscription } from '@vueuse/rxjs'
import { useTemplateRef } from 'vue'

const button = useTemplateRef('buttonRef')

// Will automatically subscribe when the button element becomes available
useSubscription(
  fromEvent(button, 'click').subscribe(() => {
    console.log('clicked!')
  })
)
```

## Type Declarations

```ts
export declare function from<T>(
  value: ObservableInput<T> | Ref<T>,
  watchOptions?: WatchOptions,
): Observable<T>
export declare function fromEvent<T extends HTMLElement | null>(
  value: MaybeRef<T>,
  event: string,
): Observable<Event>
```
```

## File: `skills/vueuse-functions/references/get.md`
```markdown
---
category: Utilities
---

# get

Shorthand for accessing `ref.value`

## Usage

```ts
import { get } from '@vueuse/core'

const a = ref(42)

console.log(get(a)) // 42
```

## Type Declarations

```ts
/**
 * Shorthand for accessing `ref.value`
 */
export declare function get<T>(ref: MaybeRef<T>): T
export declare function get<T, K extends keyof T>(
  ref: MaybeRef<T>,
  key: K,
): T[K]
```
```

## File: `skills/vueuse-functions/references/injectLocal.md`
```markdown
---
category: State
---

# injectLocal

Extended `inject` with ability to call `provideLocal` to provide the value in the same component.

## Usage

```vue
<script setup>
import { injectLocal, provideLocal } from '@vueuse/core'

provideLocal('MyInjectionKey', 1)
const injectedValue = injectLocal('MyInjectionKey') // injectedValue === 1
</script>
```

## Type Declarations

```ts
/**
 * On the basis of `inject`, it is allowed to directly call inject to obtain the value after call provide in the same component.
 *
 * @example
 * ```ts
 * injectLocal('MyInjectionKey', 1)
 * const injectedValue = injectLocal('MyInjectionKey') // injectedValue === 1
 * ```
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare const injectLocal: typeof inject
```
```

## File: `skills/vueuse-functions/references/isDefined.md`
```markdown
---
category: Utilities
---

# isDefined

Non-nullish checking type guard for Ref.

## Usage

```ts
import { isDefined } from '@vueuse/core'

const example = ref(Math.random() ? 'example' : undefined) // Ref<string | undefined>

if (isDefined(example))
  example // Ref<string>
```

## Type Declarations

```ts
export type IsDefinedReturn = boolean
export declare function isDefined<T>(
  v: ComputedRef<T>,
): v is ComputedRef<Exclude<T, null | undefined>>
export declare function isDefined<T>(
  v: Ref<T>,
): v is Ref<Exclude<T, null | undefined>>
export declare function isDefined<T>(v: T): v is Exclude<T, null | undefined>
```
```

## File: `skills/vueuse-functions/references/logicAnd.md`
```markdown
---
category: '@Math'
alias: and
related: logicNot, logicOr
---

# logicAnd

`AND` condition for refs.

## Usage

```ts
import { whenever } from '@vueuse/core'
import { logicAnd } from '@vueuse/math'

const a = ref(true)
const b = ref(false)

whenever(logicAnd(a, b), () => {
  console.log('both a and b are now truthy!')
})
```

## Type Declarations

```ts
/**
 * `AND` conditions for refs.
 *
 * @see https://vueuse.org/logicAnd
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function logicAnd(
  ...args: MaybeRefOrGetter<any>[]
): ComputedRef<boolean>
/** @deprecated use `logicAnd` instead */
export declare const and: typeof logicAnd
```
```

## File: `skills/vueuse-functions/references/logicNot.md`
```markdown
---
category: '@Math'
alias: not
---

# logicNot

`NOT` condition for ref.

## Usage

```ts
import { whenever } from '@vueuse/core'
import { logicNot } from '@vueuse/math'

const a = ref(true)

whenever(logicNot(a), () => {
  console.log('a is now falsy!')
})
```

## Type Declarations

```ts
/**
 * `NOT` conditions for refs.
 *
 * @see https://vueuse.org/logicNot
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function logicNot(v: MaybeRefOrGetter<any>): ComputedRef<boolean>
/** @deprecated use `logicNot` instead */
export declare const not: typeof logicNot
```
```

## File: `skills/vueuse-functions/references/logicOr.md`
```markdown
---
category: '@Math'
alias: or
related: logicAnd, logicNot
---

# logicOr

`OR` conditions for refs.

## Usage

```ts
import { whenever } from '@vueuse/core'
import { logicOr } from '@vueuse/math'

const a = ref(true)
const b = ref(false)

whenever(logicOr(a, b), () => {
  console.log('either a or b is truthy!')
})
```

## Type Declarations

```ts
/**
 * `OR` conditions for refs.
 *
 * @see https://vueuse.org/logicOr
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function logicOr(
  ...args: MaybeRefOrGetter<any>[]
): ComputedRef<boolean>
/** @deprecated use `logicOr` instead */
export declare const or: typeof logicOr
```
```

## File: `skills/vueuse-functions/references/makeDestructurable.md`
```markdown
---
category: Utilities
---

# makeDestructurable

Make isomorphic destructurable for object and array at the same time. See [this blog](https://antfu.me/posts/destructuring-with-object-or-array/) for more details.

## Usage

TypeScript Example:

```ts twoslash include main
import { makeDestructurable } from '@vueuse/core'

const foo = { name: 'foo' }
const bar = 1024

const obj = makeDestructurable(
  { foo, bar } as const,
  [foo, bar] as const,
)
```

Usage:

```ts twoslash
// @include: main
// ---cut---
let { foo, bar } = obj
let [foo, bar] = obj
```

## Type Declarations

```ts
export declare function makeDestructurable<
  T extends Record<string, unknown>,
  A extends readonly any[],
>(obj: T, arr: A): T & A
```
```

## File: `skills/vueuse-functions/references/onClickOutside.md`
```markdown
---
category: Sensors
---

# onClickOutside

Listen for clicks outside of an element. Useful for modals or dropdowns.

## Usage

```vue
<script setup lang="ts">
import { onClickOutside } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const target = useTemplateRef('target')

onClickOutside(target, event => console.log(event))
</script>

<template>
  <div ref="target">
    Hello world
  </div>
  <div>Outside element</div>
</template>
```

### Return Value

By default, `onClickOutside` returns a `stop` function to remove the event listeners.

```ts
const stop = onClickOutside(target, handler)

// Later, stop listening
stop()
```

### Controls

If you need more control over triggering the handler, you can use the `controls` option. This returns an object with `stop`, `cancel`, and `trigger` functions.

```ts
const { stop, cancel, trigger } = onClickOutside(
  modalRef,
  (event) => {
    modal.value = false
  },
  { controls: true },
)

// cancel prevents the next click from triggering the handler
cancel()

// trigger manually fires the handler
trigger(event)

// stop removes all event listeners
stop()
```

### Ignore Elements

Use the `ignore` option to prevent certain elements from triggering the handler. Provide elements as an array of Refs or CSS selectors.

```ts
const ignoreElRef = useTemplateRef('ignoreEl')

onClickOutside(
  target,
  event => console.log(event),
  { ignore: [ignoreElRef, '.ignore-class', '#ignore-id'] },
)
```

### Capture Phase

By default, the event listener uses the capture phase (`capture: true`). Set `capture: false` to use the bubbling phase instead.

```ts
onClickOutside(target, handler, { capture: false })
```

### Detect Iframe Clicks

Clicks inside an iframe are not detected by default. Enable `detectIframe` to also trigger the handler when focus moves to an iframe.

```ts
onClickOutside(target, handler, { detectIframe: true })
```

## Component Usage

```vue
<template>
  <OnClickOutside :options="{ ignore: [/* ... */] }" @trigger="count++">
    <div>
      Click Outside of Me
    </div>
  </OnClickOutside>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vOnClickOutside } from '@vueuse/components'
import { shallowRef } from 'vue'

const modal = shallowRef(false)
function closeModal() {
  modal.value = false
}
</script>

<template>
  <button @click="modal = true">
    Open Modal
  </button>
  <div v-if="modal" v-on-click-outside="closeModal">
    Hello World
  </div>
</template>
```

You can also set the handler as an array to set the configuration items of the instruction.

```vue
<script setup lang="ts">
import { vOnClickOutside } from '@vueuse/components'
import { shallowRef, useTemplateRef } from 'vue'

const modal = shallowRef(false)

const ignoreElRef = useTemplateRef('ignoreEl')

const onClickOutsideHandler = [
  (ev) => {
    console.log(ev)
    modal.value = false
  },
  { ignore: [ignoreElRef] },
]
</script>

<template>
  <button @click="modal = true">
    Open Modal
  </button>

  <div ref="ignoreElRef">
    click outside ignore element
  </div>

  <div v-if="modal" v-on-click-outside="onClickOutsideHandler">
    Hello World
  </div>
</template>
```

## Type Declarations

```ts
export interface OnClickOutsideOptions<
  Controls extends boolean = false,
> extends ConfigurableWindow {
  /**
   * List of elements that should not trigger the event,
   * provided as Refs or CSS Selectors.
   */
  ignore?: MaybeRefOrGetter<(MaybeElementRef | string)[]>
  /**
   * Use capturing phase for internal event listener.
   * @default true
   */
  capture?: boolean
  /**
   * Run handler function if focus moves to an iframe.
   * @default false
   */
  detectIframe?: boolean
  /**
   * Use controls to cancel/trigger listener.
   * @default false
   */
  controls?: Controls
}
export type OnClickOutsideHandler<
  T extends OnClickOutsideOptions<boolean> = OnClickOutsideOptions,
> = (
  event:
    | (T["detectIframe"] extends true ? FocusEvent : never)
    | (T["controls"] extends true ? Event : never)
    | PointerEvent,
) => void
export type OnClickOutsideReturn<Controls extends boolean = false> =
  Controls extends false
    ? Fn
    : {
        stop: Fn
        cancel: Fn
        trigger: (event: Event) => void
      }
/**
 * Listen for clicks outside of an element.
 *
 * @see https://vueuse.org/onClickOutside
 * @param target
 * @param handler
 * @param options
 */
export declare function onClickOutside<T extends OnClickOutsideOptions>(
  target: MaybeComputedElementRef,
  handler: OnClickOutsideHandler<T>,
  options?: T,
): Fn
export declare function onClickOutside<T extends OnClickOutsideOptions<true>>(
  target: MaybeComputedElementRef,
  handler: OnClickOutsideHandler<T>,
  options: T,
): {
  stop: Fn
  cancel: Fn
  trigger: (event: Event) => void
}
```
```

## File: `skills/vueuse-functions/references/onElementRemoval.md`
```markdown
---
category: Sensors
---

# onElementRemoval

Fires when the element or any element containing it is removed from the DOM.

## Usage

```vue {13}
<script setup lang="ts">
import { onElementRemoval } from '@vueuse/core'
import { shallowRef, useTemplateRef } from 'vue'

const btnRef = useTemplateRef('btn')
const btnState = shallowRef(true)
const removedCount = shallowRef(0)

function btnOnClick() {
  btnState.value = !btnState.value
}

onElementRemoval(btnRef, () => ++removedCount.value)
</script>

<template>
  <button
    v-if="btnState"
    @click="btnOnClick"
  >
    recreate me
  </button>
  <button
    v-else
    ref="btnRef"
    @click="btnOnClick"
  >
    remove me
  </button>
  <b>removed times: {{ removedCount }}</b>
</template>
```

### Callback with Mutation Records

The callback receives an array of `MutationRecord` objects that triggered the removal.

```ts
import { onElementRemoval } from '@vueuse/core'

onElementRemoval(targetRef, (mutationRecords) => {
  console.log('Element removed', mutationRecords)
})
```

### Return Value

Returns a stop function to stop observing.

```ts
const stop = onElementRemoval(targetRef, callback)

// Later, stop observing
stop()
```

## Type Declarations

```ts
export interface OnElementRemovalOptions
  extends
    ConfigurableWindow,
    ConfigurableDocumentOrShadowRoot,
    WatchOptionsBase {}
/**
 * Fires when the element or any element containing it is removed.
 *
 * @param target
 * @param callback
 * @param options
 */
export declare function onElementRemoval(
  target: MaybeElementRef,
  callback: (mutationRecords: MutationRecord[]) => void,
  options?: OnElementRemovalOptions,
): Fn
```
```

## File: `skills/vueuse-functions/references/onKeyStroke.md`
```markdown
---
category: Sensors
---

# onKeyStroke

Listen for keyboard keystrokes. By default, listens on `keydown` events on `window`.

## Usage

```ts
import { onKeyStroke } from '@vueuse/core'

onKeyStroke('ArrowDown', (e) => {
  e.preventDefault()
})
```

See [this table](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values) for all key codes.

### Return Value

Returns a stop function to remove the event listener.

```ts
const stop = onKeyStroke('Escape', handler)

// Later, stop listening
stop()
```

### Listen To Multiple Keys

```ts
import { onKeyStroke } from '@vueuse/core'

onKeyStroke(['s', 'S', 'ArrowDown'], (e) => {
  e.preventDefault()
})

// listen to all keys by passing `true` or skipping the key parameter
onKeyStroke(true, (e) => {
  e.preventDefault()
})
onKeyStroke((e) => {
  e.preventDefault()
})
```

### Custom Key Predicate

You can pass a custom function to determine which keys should trigger the handler.

```ts
import { onKeyStroke } from '@vueuse/core'

onKeyStroke(
  e => e.key === 'A' && e.shiftKey,
  (e) => {
    console.log('Shift+A pressed')
  },
)
```

### Custom Event Target

```ts
import { onKeyStroke } from '@vueuse/core'

onKeyStroke('A', (e) => {
  console.log('Key A pressed on document')
}, { target: document })
```

### Ignore Repeated Events

The callback will trigger only once when pressing `A` and **holding down**. The `dedupe` option can also be a reactive ref.

```ts
import { onKeyStroke } from '@vueuse/core'

onKeyStroke('A', (e) => {
  console.log('Key A pressed')
}, { dedupe: true })
```

Reference: [KeyboardEvent.repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat)

### Passive Mode

Set `passive: true` to use a passive event listener.

```ts
import { onKeyStroke } from '@vueuse/core'

onKeyStroke('A', handler, { passive: true })
```

## Directive Usage

```vue
<script setup lang="ts">
import { vOnKeyStroke } from '@vueuse/components'

function onUpdate(e: KeyboardEvent) {
  // impl...
}
</script>

<template>
  <input v-on-key-stroke:c,v="onUpdate" type="text">
  <!-- with options -->
  <input v-on-key-stroke:c,v="[onUpdate, { eventName: 'keyup' }]" type="text">
</template>
```

### Custom Keyboard Event

```ts
import { onKeyStroke } from '@vueuse/core'
// ---cut---
onKeyStroke('Shift', (e) => {
  console.log('Shift key up')
}, { eventName: 'keyup' })
```

Or

```ts
import { onKeyUp } from '@vueuse/core'
// ---cut---
onKeyUp('Shift', () => console.log('Shift key up'))
```

## Shorthands

- `onKeyDown` - alias for `onKeyStroke(key, handler, {eventName: 'keydown'})`
- `onKeyPressed` - alias for `onKeyStroke(key, handler, {eventName: 'keypress'})`
- `onKeyUp` - alias for `onKeyStroke(key, handler, {eventName: 'keyup'})`

## Type Declarations

```ts
export type KeyPredicate = (event: KeyboardEvent) => boolean
export type KeyFilter = true | string | string[] | KeyPredicate
export type KeyStrokeEventName = "keydown" | "keypress" | "keyup"
export interface OnKeyStrokeOptions {
  eventName?: KeyStrokeEventName
  target?: MaybeRefOrGetter<EventTarget | null | undefined>
  passive?: boolean
  /**
   * Set to `true` to ignore repeated events when the key is being held down.
   *
   * @default false
   */
  dedupe?: MaybeRefOrGetter<boolean>
}
/**
 * Listen for keyboard keystrokes.
 *
 * @see https://vueuse.org/onKeyStroke
 */
export declare function onKeyStroke(
  key: KeyFilter,
  handler: (event: KeyboardEvent) => void,
  options?: OnKeyStrokeOptions,
): () => void
export declare function onKeyStroke(
  handler: (event: KeyboardEvent) => void,
  options?: OnKeyStrokeOptions,
): () => void
/**
 * Listen to the keydown event of the given key.
 *
 * @see https://vueuse.org/onKeyStroke
 * @param key
 * @param handler
 * @param options
 */
export declare function onKeyDown(
  key: KeyFilter,
  handler: (event: KeyboardEvent) => void,
  options?: Omit<OnKeyStrokeOptions, "eventName">,
): () => void
/**
 * Listen to the keypress event of the given key.
 *
 * @see https://vueuse.org/onKeyStroke
 * @param key
 * @param handler
 * @param options
 */
export declare function onKeyPressed(
  key: KeyFilter,
  handler: (event: KeyboardEvent) => void,
  options?: Omit<OnKeyStrokeOptions, "eventName">,
): () => void
/**
 * Listen to the keyup event of the given key.
 *
 * @see https://vueuse.org/onKeyStroke
 * @param key
 * @param handler
 * @param options
 */
export declare function onKeyUp(
  key: KeyFilter,
  handler: (event: KeyboardEvent) => void,
  options?: Omit<OnKeyStrokeOptions, "eventName">,
): () => void
```
```

## File: `skills/vueuse-functions/references/onLongPress.md`
```markdown
---
category: Sensors
---

# onLongPress

Listen for a long press on an element. Returns a stop function.

## Usage

```vue
<script setup lang="ts">
import { onLongPress } from '@vueuse/core'
import { shallowRef, useTemplateRef } from 'vue'

const htmlRefHook = useTemplateRef('htmlRefHook')
const longPressedHook = shallowRef(false)

function onLongPressCallbackHook(e: PointerEvent) {
  longPressedHook.value = true
}
function resetHook() {
  longPressedHook.value = false
}

onLongPress(
  htmlRefHook,
  onLongPressCallbackHook,
  {
    modifiers: {
      prevent: true
    }
  }
)
</script>

<template>
  <p>Long Pressed: {{ longPressedHook }}</p>

  <button ref="htmlRefHook" class="ml-2 button small">
    Press long
  </button>

  <button class="ml-2 button small" @click="resetHook">
    Reset
  </button>
</template>
```

### Custom Delay

By default, the handler fires after 500ms. You can customize this with the `delay` option. It can be a number or a function that receives the `PointerEvent`.

```ts
import { onLongPress } from '@vueuse/core'

// Fixed delay
onLongPress(target, handler, { delay: 1000 })

// Dynamic delay based on event
onLongPress(target, handler, {
  delay: ev => ev.pointerType === 'touch' ? 800 : 500,
})
```

### Distance Threshold

The long press will be canceled if the pointer moves more than the threshold (default: 10 pixels). Set to `false` to disable movement detection.

```ts
import { onLongPress } from '@vueuse/core'

// Custom threshold
onLongPress(target, handler, { distanceThreshold: 20 })

// Disable movement detection
onLongPress(target, handler, { distanceThreshold: false })
```

### On Mouse Up Callback

You can provide an `onMouseUp` callback to be notified when the pointer is released.

```ts
import { onLongPress } from '@vueuse/core'

onLongPress(target, handler, {
  onMouseUp(duration, distance, isLongPress) {
    console.log(`Held for ${duration}ms, moved ${distance}px, long press: ${isLongPress}`)
  },
})
```

### Modifiers

The following modifiers are available:

| Modifier  | Description                                  |
| --------- | -------------------------------------------- |
| `stop`    | Calls `event.stopPropagation()`              |
| `once`    | Removes event listener after first trigger   |
| `prevent` | Calls `event.preventDefault()`               |
| `capture` | Uses capture mode for event listener         |
| `self`    | Only trigger if target is the element itself |

```ts
onLongPress(target, handler, {
  modifiers: {
    prevent: true,
    stop: true,
  },
})
```

## Component Usage

```vue
<script setup lang="ts">
import { OnLongPress } from '@vueuse/components'
import { shallowRef } from 'vue'

const longPressedComponent = shallowRef(false)

function onLongPressCallbackComponent(e: PointerEvent) {
  longPressedComponent.value = true
}
function resetComponent() {
  longPressedComponent.value = false
}
</script>

<template>
  <p>Long Pressed: {{ longPressedComponent }}</p>

  <OnLongPress
    as="button"
    class="ml-2 button small"
    @trigger="onLongPressCallbackComponent"
  >
    Press long
  </OnLongPress>

  <button class="ml-2 button small" @click="resetComponent">
    Reset
  </button>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vOnLongPress } from '@vueuse/components'
import { shallowRef } from 'vue'

const longPressedDirective = shallowRef(false)

function onLongPressCallbackDirective(e: PointerEvent) {
  longPressedDirective.value = true
}
function resetDirective() {
  longPressedDirective.value = false
}
</script>

<template>
  <p>Long Pressed: {{ longPressedDirective }}</p>

  <button
    v-on-long-press.prevent="onLongPressCallbackDirective"
    class="ml-2 button small"
  >
    Press long
  </button>

  <button
    v-on-long-press="[onLongPressCallbackDirective, { delay: 1000, modifiers: { stop: true } }]"
    class="ml-2 button small"
  >
    Press long (with options)
  </button>

  <button class="ml-2 button small" @click="resetDirective">
    Reset
  </button>
</template>
```

## Type Declarations

```ts
export interface OnLongPressOptions {
  /**
   * Time in ms till `longpress` gets called
   *
   * @default 500
   */
  delay?: number | ((ev: PointerEvent) => number)
  modifiers?: OnLongPressModifiers
  /**
   * Allowance of moving distance in pixels,
   * The action will get canceled When moving too far from the pointerdown position.
   * @default 10
   */
  distanceThreshold?: number | false
  /**
   * Function called when the ref element is released.
   * @param duration how long the element was pressed in ms
   * @param distance distance from the pointerdown position
   * @param isLongPress whether the action was a long press or not
   */
  onMouseUp?: (duration: number, distance: number, isLongPress: boolean) => void
}
export interface OnLongPressModifiers {
  stop?: boolean
  once?: boolean
  prevent?: boolean
  capture?: boolean
  self?: boolean
}
export type OnLongPressReturn = () => void
/** @deprecated use {@link OnLongPressReturn} instead */
export type UseOnLongPressReturn = OnLongPressReturn
export declare function onLongPress(
  target: MaybeElementRef,
  handler: (evt: PointerEvent) => void,
  options?: OnLongPressOptions,
): OnLongPressReturn
```
```

## File: `skills/vueuse-functions/references/onStartTyping.md`
```markdown
---
category: Sensors
---

# onStartTyping

Fires when users start typing on non-editable elements. Useful for auto-focusing an input field when the user starts typing anywhere on the page.

## Usage

```vue
<script setup lang="ts">
import { onStartTyping } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const input = useTemplateRef('input')

onStartTyping(() => {
  if (!input.value.active)
    input.value.focus()
})
</script>

<template>
  <input ref="input" type="text" placeholder="Start typing to focus">
</template>
```

## How It Works

The callback only fires when:

- No editable element (`<input>`, `<textarea>`, or `contenteditable`) is focused
- The pressed key is alphanumeric (A-Z, 0-9)
- No modifier keys (Ctrl, Alt, Meta) are held

This allows users to start typing anywhere on the page without accidentally triggering the callback when using keyboard shortcuts or interacting with form fields.

## Type Declarations

```ts
/**
 * Fires when users start typing on non-editable elements.
 *
 * @see https://vueuse.org/onStartTyping
 * @param callback
 * @param options
 */
export declare function onStartTyping(
  callback: (event: KeyboardEvent) => void,
  options?: ConfigurableDocument,
): void
```
```

## File: `skills/vueuse-functions/references/provideLocal.md`
```markdown
---
category: State
---

# provideLocal

Extended `provide` with ability to call `injectLocal` to obtain the value in the same component.

## Usage

```vue
<script setup>
import { injectLocal, provideLocal } from '@vueuse/core'

provideLocal('MyInjectionKey', 1)
const injectedValue = injectLocal('MyInjectionKey') // injectedValue === 1
</script>
```

## Type Declarations

```ts
export type ProvideLocalReturn = void
/**
 * On the basis of `provide`, it is allowed to directly call inject to obtain the value after call provide in the same component.
 *
 * @example
 * ```ts
 * provideLocal('MyInjectionKey', 1)
 * const injectedValue = injectLocal('MyInjectionKey') // injectedValue === 1
 * ```
 */
export declare function provideLocal<T, K = LocalProvidedKey<T>>(
  key: K,
  value: K extends InjectionKey<infer V> ? V : T,
): ProvideLocalReturn
```
```

## File: `skills/vueuse-functions/references/reactify.md`
```markdown
---
category: Reactivity
alias: createReactiveFn
---

# reactify

Converts plain functions into reactive functions. The converted function accepts refs as its arguments and returns a ComputedRef, with proper typing.

::: tip
Interested to see some application or looking for some pre-reactified functions?

Check out [⚗️ Vue Chemistry](https://github.com/antfu/vue-chemistry)!
:::

## Usage

Basic example

```ts
import { reactify } from '@vueuse/core'
import { shallowRef } from 'vue'

// a plain function
function add(a: number, b: number): number {
  return a + b
}

// now it accept refs and returns a computed ref
// (a: number | Ref<number>, b: number | Ref<number>) => ComputedRef<number>
const reactiveAdd = reactify(add)

const a = shallowRef(1)
const b = shallowRef(2)
const sum = reactiveAdd(a, b)

console.log(sum.value) // 3

a.value = 5

console.log(sum.value) // 7
```

An example of implementing a reactive [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem).

<!-- eslint-skip -->

```ts
import { reactify } from '@vueuse/core'
import { shallowRef } from 'vue'

const pow = reactify(Math.pow)
const sqrt = reactify(Math.sqrt)
const add = reactify((a: number, b: number) => a + b)

const a = shallowRef(3)
const b = shallowRef(4)
const c = sqrt(add(pow(a, 2), pow(b, 2)))
console.log(c.value) // 5

// 5:12:13
a.value = 5
b.value = 12
console.log(c.value) // 13
```

You can also do it this way:

```ts
import { reactify } from '@vueuse/core'
import { shallowRef } from 'vue'

function pythagorean(a: number, b: number) {
  return Math.sqrt(a ** 2 + b ** 2)
}

const a = shallowRef(3)
const b = shallowRef(4)

const c = reactify(pythagorean)(a, b)
console.log(c.value) // 5
```

Another example of making reactive `stringify`

```ts
import { reactify } from '@vueuse/core'
import { shallowRef } from 'vue'

const stringify = reactify(JSON.stringify)

const obj = shallowRef(42)
const dumped = stringify(obj)

console.log(dumped.value) // '42'

obj.value = { foo: 'bar' }

console.log(dumped.value) // '{"foo":"bar"}'
```

## Type Declarations

```ts
export type Reactified<T, Computed extends boolean> = T extends (
  ...args: infer A
) => infer R
  ? (
      ...args: {
        [K in keyof A]: Computed extends true
          ? MaybeRefOrGetter<A[K]>
          : MaybeRef<A[K]>
      }
    ) => ComputedRef<R>
  : never
export type ReactifyReturn<
  T extends AnyFn = AnyFn,
  K extends boolean = true,
> = Reactified<T, K>
export interface ReactifyOptions<T extends boolean> {
  /**
   * Accept passing a function as a reactive getter
   *
   * @default true
   */
  computedGetter?: T
}
/**
 * Converts plain function into a reactive function.
 * The converted function accepts refs as it's arguments
 * and returns a ComputedRef, with proper typing.
 *
 * @param fn - Source function
 * @param options - Options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function reactify<T extends AnyFn, K extends boolean = true>(
  fn: T,
  options?: ReactifyOptions<K>,
): ReactifyReturn<T, K>
/** @deprecated use `reactify` instead */
export declare const createReactiveFn: typeof reactify
```
```

## File: `skills/vueuse-functions/references/reactifyObject.md`
```markdown
---
category: Reactivity
---

# reactifyObject

Apply `reactify` to an object

## Usage

```ts
import { reactifyObject } from '@vueuse/core'

const reactifiedConsole = reactifyObject(console)

const a = ref('42')

reactifiedConsole.log(a) // no longer need `.value`
```

## Type Declarations

```ts
export type ReactifyNested<
  T,
  Keys extends keyof T = keyof T,
  S extends boolean = true,
> = {
  [K in Keys]: T[K] extends AnyFn ? Reactified<T[K], S> : T[K]
}
export type ReactifyObjectReturn<
  T,
  Keys extends keyof T,
  S extends boolean = true,
> = ReactifyNested<T, Keys, S>
export interface ReactifyObjectOptions<
  T extends boolean,
> extends ReactifyOptions<T> {
  /**
   * Includes names from Object.getOwnPropertyNames
   *
   * @default true
   */
  includeOwnProperties?: boolean
}
/**
 * Apply `reactify` to an object
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function reactifyObject<T extends object, Keys extends keyof T>(
  obj: T,
  keys?: (keyof T)[],
): ReactifyObjectReturn<T, Keys, true>
export declare function reactifyObject<
  T extends object,
  S extends boolean = true,
>(
  obj: T,
  options?: ReactifyObjectOptions<S>,
): ReactifyObjectReturn<T, keyof T, S>
```
```

## File: `skills/vueuse-functions/references/reactiveComputed.md`
```markdown
---
category: Reactivity
---

# reactiveComputed

Computed reactive object. Instead of returning a ref that `computed` does, `reactiveComputed` returns a reactive object.

## Usage

```ts
import { reactiveComputed } from '@vueuse/core'

const state = reactiveComputed(() => {
  return {
    foo: 'bar',
    bar: 'baz',
  }
})

state.bar // 'baz'
```

## Type Declarations

```ts
export type ReactiveComputedReturn<T extends object> = UnwrapNestedRefs<T>
/**
 * Computed reactive object.
 */
export declare function reactiveComputed<T extends object>(
  fn: ComputedGetter<T>,
): ReactiveComputedReturn<T>
```
```

## File: `skills/vueuse-functions/references/reactiveOmit.md`
```markdown
---
category: Reactivity
---

# reactiveOmit

Reactively omit fields from a reactive object.

## Usage

### Basic Usage

```ts
import { reactiveOmit } from '@vueuse/core'

const obj = reactive({
  x: 0,
  y: 0,
  elementX: 0,
  elementY: 0,
})

const picked = reactiveOmit(obj, 'x', 'elementX') // { y: number, elementY: number }
```

### Predicate Usage

```ts
import { reactiveOmit } from '@vueuse/core'

const obj = reactive({
  bar: 'bar',
  baz: 'should be omit',
  foo: 'foo2',
  qux: true,
})

const picked = reactiveOmit(obj, (value, key) => key === 'baz' || value === true)
// { bar: string, foo: string }
```

### Scenarios

#### Selectively passing props to child

```vue
<script setup lang="ts">
import { reactiveOmit } from '@vueuse/core'

const props = defineProps<{
  value: string
  color?: string
  font?: string
}>()

const childProps = reactiveOmit(props, 'value')
</script>

<template>
  <div>
    <!-- only passes "color" and "font" props to child -->
    <ChildComp v-bind="childProps" />
  </div>
</template>
```

## Type Declarations

```ts
export type ReactiveOmitReturn<
  T extends object,
  K extends keyof T | undefined = undefined,
> = [K] extends [undefined] ? Partial<T> : Omit<T, Extract<K, keyof T>>
export type ReactiveOmitPredicate<T> = (
  value: T[keyof T],
  key: keyof T,
) => boolean
export declare function reactiveOmit<T extends object, K extends keyof T>(
  obj: T,
  ...keys: (K | K[])[]
): ReactiveOmitReturn<T, K>
export declare function reactiveOmit<T extends object>(
  obj: T,
  predicate: ReactiveOmitPredicate<T>,
): ReactiveOmitReturn<T>
```
```

## File: `skills/vueuse-functions/references/reactivePick.md`
```markdown
---
category: Reactivity
---

# reactivePick

Reactively pick fields from a reactive object.

## Usage

### Basic Usage

```ts
import { reactivePick } from '@vueuse/core'

const obj = reactive({
  x: 0,
  y: 0,
  elementX: 0,
  elementY: 0,
})

const picked = reactivePick(obj, 'x', 'elementX') // { x: number, elementX: number }
```

### Predicate Usage

```ts
import { reactivePick } from '@vueuse/core'

const source = reactive({
  foo: 'foo',
  bar: 'bar',
  baz: 'baz',
  qux: true,
})
const state = reactivePick(source, (value, key) => key !== 'bar' && value !== true)
// { foo: string, baz: string }
source.qux = false
// { foo: string, baz: string, qux: boolean }
```

### Scenarios

#### Selectively passing props to child

```vue
<script setup lang="ts">
import { reactivePick } from '@vueuse/core'

const props = defineProps<{
  value: string
  color?: string
  font?: string
}>()

const childProps = reactivePick(props, 'color', 'font')
</script>

<template>
  <div>
    <!-- only passes "color" and "font" props to child -->
    <ChildComp v-bind="childProps" />
  </div>
</template>
```

#### Selectively wrap reactive object

Instead of doing this

```ts
import { useElementBounding } from '@vueuse/core'
import { reactive } from 'vue'

const { height, width } = useElementBounding() // object of refs
const size = reactive({ height, width })
```

Now we can just have this

```ts
import { reactivePick, useElementBounding } from '@vueuse/core'

const size = reactivePick(useElementBounding(), 'height', 'width')
```

## Type Declarations

```ts
export type ReactivePickReturn<T extends object, K extends keyof T> = {
  [S in K]: UnwrapRef<T[S]>
}
export type ReactivePickPredicate<T> = (
  value: T[keyof T],
  key: keyof T,
) => boolean
export declare function reactivePick<T extends object, K extends keyof T>(
  obj: T,
  ...keys: (K | K[])[]
): ReactivePickReturn<T, K>
export declare function reactivePick<T extends object>(
  obj: T,
  predicate: ReactivePickPredicate<T>,
): ReactivePickReturn<T, keyof T>
```
```

## File: `skills/vueuse-functions/references/refAutoReset.md`
```markdown
---
category: Reactivity
alias: autoResetRef
---

# refAutoReset

A ref which will be reset to the default value after some time.

## Usage

```ts
import { refAutoReset } from '@vueuse/core'

const message = refAutoReset('default message', 1000)

function setMessage() {
  // here the value will change to 'message has set' but after 1000ms, it will change to 'default message'
  message.value = 'message has set'
}
```

::: info
You can reassign the entire object to trigger updates after making deep mutations to the inner value.

[Learn more about shallow refs →](https://vuejs.org/api/reactivity-advanced#shallowref)
:::

## Type Declarations

```ts
export type RefAutoResetReturn<T = any> = Ref<T>
/**
 * Create a ref which will be reset to the default value after some time.
 *
 * @see https://vueuse.org/refAutoReset
 * @param defaultValue The value which will be set.
 * @param afterMs      A zero-or-greater delay in milliseconds.
 */
export declare function refAutoReset<T>(
  defaultValue: MaybeRefOrGetter<T>,
  afterMs?: MaybeRefOrGetter<number>,
): RefAutoResetReturn<T>
/** @deprecated use `refAutoReset` instead */
export declare const autoResetRef: typeof refAutoReset
```
```

## File: `skills/vueuse-functions/references/refDebounced.md`
```markdown
---
category: Reactivity
alias: useDebounce, debouncedRef
---

# refDebounced

Debounce execution of a ref value.

## Usage

```ts {5}
import { refDebounced } from '@vueuse/core'
import { shallowRef } from 'vue'

const input = shallowRef('foo')
const debounced = refDebounced(input, 1000)

input.value = 'bar'
console.log(debounced.value) // 'foo'

await sleep(1100)

console.log(debounced.value) // 'bar'
// ---cut-after---
function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms))
}
```

An example with object ref.

```js
import { refDebounced } from '@vueuse/core'
import { shallowRef } from 'vue'

const data = shallowRef({
  name: 'foo',
  age: 18,
})
const debounced = refDebounced(data, 1000)

function update() {
  data.value = {
    ...data.value,
    name: 'bar',
  }
}

console.log(debounced.value) // { name: 'foo', age: 18 }
update()
await sleep(1100)

console.log(debounced.value) // { name: 'bar', age: 18 }
```

You can also pass an optional 3rd parameter including maxWait option. See `useDebounceFn` for details.

## Recommended Reading

- [**Debounce vs Throttle**: Definitive Visual Guide](https://kettanaito.com/blog/debounce-vs-throttle)

## Type Declarations

```ts
export type RefDebouncedReturn<T = any> = Readonly<Ref<T>>
/**
 * Debounce updates of a ref.
 *
 * @return A new debounced ref.
 */
export declare function refDebounced<T>(
  value: Ref<T>,
  ms?: MaybeRefOrGetter<number>,
  options?: DebounceFilterOptions,
): RefDebouncedReturn<T>
/** @deprecated use `refDebounced` instead */
export declare const debouncedRef: typeof refDebounced
/** @deprecated use `refDebounced` instead */
export declare const useDebounce: typeof refDebounced
```
```

## File: `skills/vueuse-functions/references/refDefault.md`
```markdown
---
category: Reactivity
---

# refDefault

Apply default value to a ref.

## Usage

```ts
import { refDefault, useStorage } from '@vueuse/core'

const raw = useStorage('key')
const state = refDefault(raw, 'default')

raw.value = 'hello'
console.log(state.value) // hello

raw.value = undefined
console.log(state.value) // default
```

## Type Declarations

```ts
/**
 * Apply default value to a ref.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function refDefault<T>(
  source: Ref<T | undefined | null>,
  defaultValue: T,
): Ref<T>
```
```

## File: `skills/vueuse-functions/references/refManualReset.md`
```markdown
---
category: Reactivity
---

# refManualReset

Create a ref with manual reset functionality.

## Usage

```ts
import { refManualReset } from '@vueuse/core'

const message = refManualReset('default message')

message.value = 'message has set'

message.reset()

console.log(message.value) // 'default message'
```

## Type Declarations

```ts
/**
 * Define the shape of a ref that supports manual reset functionality.
 *
 * This interface extends the standard `Ref` type from Vue and adds a `reset` method.
 * The `reset` method allows the ref to be manually reset to its default value.
 */
export interface ManualResetRefReturn<T> extends Ref<T> {
  reset: Fn
}
/**
 * Create a ref with manual reset functionality.
 *
 * @see https://vueuse.org/refManualReset
 * @param defaultValue The value which will be set.
 */
export declare function refManualReset<T>(
  defaultValue: MaybeRefOrGetter<T>,
): ManualResetRefReturn<T>
```
```

## File: `skills/vueuse-functions/references/refThrottled.md`
```markdown
---
category: Reactivity
alias: useThrottle, throttledRef
---

# refThrottled

Throttle changing of a ref value.

## Usage

```ts
import { refThrottled } from '@vueuse/core'
import { shallowRef } from 'vue'

const input = shallowRef('')
const throttled = refThrottled(input, 1000)
```

An example with object ref.

```js
import { refThrottled } from '@vueuse/core'
import { shallowRef } from 'vue'

const data = shallowRef({
  count: 0,
  name: 'foo',
})
const throttled = refThrottled(data, 1000)

data.value = { count: 1, name: 'foo' }
console.log(throttled.value) // { count: 1, name: 'foo' } (immediate)

data.value = { count: 2, name: 'bar' }
data.value = { count: 3, name: 'baz' }
data.value = { count: 4, name: 'qux' }
console.log(throttled.value) // { count: 1, name: 'foo' } (still first value)

// After 1000ms, next change will be applied
await sleep(1100)
data.value = { count: 5, name: 'final' }
await nextTick()
console.log(throttled.value) // { count: 5, name: 'final' } (updated)
```

### Trailing

If you don't want to watch trailing changes, set 3rd param `false` (it's `true` by default):

```ts
import { refThrottled } from '@vueuse/core'
import { shallowRef } from 'vue'

const input = shallowRef('')
const throttled = refThrottled(input, 1000, false)
```

### Leading

Allows the callback to be invoked immediately (on the leading edge of the `ms` timeout). If you don't want this behavior, set the 4th param `false` (it's `true` by default):

```ts
import { refThrottled } from '@vueuse/core'
import { shallowRef } from 'vue'

const input = shallowRef('')
const throttled = refThrottled(input, 1000, undefined, false)
```

## Recommended Reading

- [Debounce vs Throttle: Definitive Visual Guide](https://kettanaito.com/blog/debounce-vs-throttle)
- [Debouncing and Throttling Explained Through Examples](https://css-tricks.com/debouncing-throttling-explained-examples/)

## Type Declarations

```ts
export type RefThrottledReturn<T = any> = Ref<T>
/**
 * Throttle execution of a function. Especially useful for rate limiting
 * execution of handlers on events like resize and scroll.
 *
 * @param value Ref value to be watched with throttle effect
 * @param  delay  A zero-or-greater delay in milliseconds. For event callbacks, values around 100 or 250 (or even higher) are most useful.
 * @param trailing if true, update the value again after the delay time is up
 * @param leading if true, update the value on the leading edge of the ms timeout
 */
export declare function refThrottled<T = any>(
  value: Ref<T>,
  delay?: number,
  trailing?: boolean,
  leading?: boolean,
): RefThrottledReturn<T>
/** @deprecated use `refThrottled` instead */
export declare const throttledRef: typeof refThrottled
/** @deprecated use `refThrottled` instead */
export declare const useThrottle: typeof refThrottled
```
```

## File: `skills/vueuse-functions/references/refWithControl.md`
```markdown
---
category: Reactivity
alias: controlledRef
related: computedWithControl
---

# refWithControl

Fine-grained controls over ref and its reactivity.

## Usage

`refWithControl` uses `extendRef` to provide two extra functions `get` and `set` to have better control over when it should track/trigger the reactivity.

```ts
import { refWithControl } from '@vueuse/core'

const num = refWithControl(0)
const doubled = computed(() => num.value * 2)

// just like normal ref
num.value = 42
console.log(num.value) // 42
console.log(doubled.value) // 84

// set value without triggering the reactivity
num.set(30, false)
console.log(num.value) // 30
console.log(doubled.value) // 84 (doesn't update)

// get value without tracking the reactivity
watchEffect(() => {
  console.log(num.peek())
}) // 30

num.value = 50 // watch effect wouldn't be triggered since it collected nothing.
console.log(doubled.value) // 100 (updated again since it's a reactive set)
```

### `peek`, `lay`, `untrackedGet`, `silentSet`

We also provide some shorthands for doing the get/set without track/triggering the reactivity system. The following lines are equivalent.

```ts
import { refWithControl } from '@vueuse/core'
// ---cut---
const foo = refWithControl('foo')
```

```ts
import { refWithControl } from '@vueuse/core'

const foo = refWithControl('foo')
// ---cut---
// getting
foo.get(false)
foo.untrackedGet()
foo.peek() // an alias for `untrackedGet`
```

```ts
import { refWithControl } from '@vueuse/core'

const foo = refWithControl('foo')
// ---cut---
// setting
foo.set('bar', false)
foo.silentSet('bar')
foo.lay('bar') // an alias for `silentSet`
```

## Configurations

### `onBeforeChange()`

`onBeforeChange` option is offered to give control over if a new value should be accepted. For example:

```ts
import { refWithControl } from '@vueuse/core'
// ---cut---
const num = refWithControl(0, {
  onBeforeChange(value, oldValue) {
    // disallow changes larger then ±5 in one operation
    if (Math.abs(value - oldValue) > 5)
      return false // returning `false` to dismiss the change
  },
})

num.value += 1
console.log(num.value) // 1

num.value += 6
console.log(num.value) // 1 (change been dismissed)
```

### `onChanged()`

`onChanged` option offers a similar functionally as Vue's `watch` but being synchronized with less overhead compared to `watch`.

```ts
import { refWithControl } from '@vueuse/core'
// ---cut---
const num = refWithControl(0, {
  onChanged(value, oldValue) {
    console.log(value)
  },
})
```

## Type Declarations

```ts
export interface ControlledRefOptions<T> {
  /**
   * Callback function before the ref changing.
   *
   * Returning `false` to dismiss the change.
   */
  onBeforeChange?: (value: T, oldValue: T) => void | boolean
  /**
   * Callback function after the ref changed
   *
   * This happens synchronously, with less overhead compare to `watch`
   */
  onChanged?: (value: T, oldValue: T) => void
}
/**
 * Fine-grained controls over ref and its reactivity.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function refWithControl<T>(
  initial: T,
  options?: ControlledRefOptions<T>,
): ShallowUnwrapRef<{
  get: (tracking?: boolean) => T
  set: (value: T, triggering?: boolean) => void
  untrackedGet: () => T
  silentSet: (v: T) => void
  peek: () => T
  lay: (v: T) => void
}> &
  Ref<T, T>
/** @deprecated use `refWithControl` instead */
export declare const controlledRef: typeof refWithControl
```
```

## File: `skills/vueuse-functions/references/set.md`
```markdown
---
category: Utilities
---

# set

Shorthand for `ref.value = x`

## Usage

```ts
import { set } from '@vueuse/core'

const a = ref(0)

set(a, 1)

console.log(a.value) // 1
```

## Type Declarations

```ts
export declare function set<T>(ref: Ref<T>, value: T): void
export declare function set<O extends object, K extends keyof O>(
  target: O,
  key: K,
  value: O[K],
): void
```
```

## File: `skills/vueuse-functions/references/syncRef.md`
```markdown
---
category: Reactivity
related: syncRefs
---

# syncRef

Two-way refs synchronization.

## Usage

```ts
import { syncRef } from '@vueuse/core'

const a = ref('a')
const b = ref('b')

const stop = syncRef(a, b)

console.log(a.value) // a

b.value = 'foo'

console.log(a.value) // foo

a.value = 'bar'

console.log(b.value) // bar
```

### One directional

```ts
import { syncRef } from '@vueuse/core'

const a = ref('a')
const b = ref('b')

const stop = syncRef(a, b, { direction: 'rtl' })
```

### Custom Transform

```ts
import { syncRef } from '@vueuse/core'

const a = ref(10)
const b = ref(2)

const stop = syncRef(a, b, {
  transform: {
    ltr: left => left * 2,
    rtl: right => right / 2
  }
})

console.log(b.value) // 20

b.value = 30

console.log(a.value) // 15
```

## Type Declarations

```ts
type Direction = "ltr" | "rtl" | "both"
type SpecificFieldPartial<T, K extends keyof T> = Partial<Pick<T, K>> &
  Omit<T, K>
/**
 * A = B
 */
type Equal<A, B> = [A] extends [B] ? ([B] extends [A] ? true : false) : false
/**
 * A ∩ B ≠ ∅
 */
type IntersectButNotEqual<A, B> =
  Equal<A, B> extends true ? false : A & B extends never ? false : true
/**
 * A ⊆ B
 */
type IncludeButNotEqual<A, B> =
  Equal<A, B> extends true ? false : A extends B ? true : false
/**
 * A ∩ B = ∅
 */
type NotIntersect<A, B> =
  Equal<A, B> extends true ? false : A & B extends never ? true : false
interface EqualType<
  D extends Direction,
  L,
  R,
  O extends keyof Transform<L, R> = D extends "both" ? "ltr" | "rtl" : D,
> {
  transform?: SpecificFieldPartial<Pick<Transform<L, R>, O>, O>
}
type StrictIncludeMap<
  IncludeType extends "LR" | "RL",
  D extends Exclude<Direction, "both">,
  L,
  R,
> = Equal<[IncludeType, D], ["LR", "ltr"]> &
  Equal<[IncludeType, D], ["RL", "rtl"]> extends true
  ? {
      transform?: SpecificFieldPartial<Pick<Transform<L, R>, D>, D>
    }
  : {
      transform: Pick<Transform<L, R>, D>
    }
type StrictIncludeType<
  IncludeType extends "LR" | "RL",
  D extends Direction,
  L,
  R,
> = D extends "both"
  ? {
      transform: SpecificFieldPartial<
        Transform<L, R>,
        IncludeType extends "LR" ? "ltr" : "rtl"
      >
    }
  : D extends Exclude<Direction, "both">
    ? StrictIncludeMap<IncludeType, D, L, R>
    : never
type IntersectButNotEqualType<D extends Direction, L, R> = D extends "both"
  ? {
      transform: Transform<L, R>
    }
  : D extends Exclude<Direction, "both">
    ? {
        transform: Pick<Transform<L, R>, D>
      }
    : never
type NotIntersectType<D extends Direction, L, R> = IntersectButNotEqualType<
  D,
  L,
  R
>
interface Transform<L, R> {
  ltr: (left: L) => R
  rtl: (right: R) => L
}
type TransformType<D extends Direction, L, R> =
  Equal<L, R> extends true
    ? EqualType<D, L, R>
    : IncludeButNotEqual<L, R> extends true
      ? StrictIncludeType<"LR", D, L, R>
      : IncludeButNotEqual<R, L> extends true
        ? StrictIncludeType<"RL", D, L, R>
        : IntersectButNotEqual<L, R> extends true
          ? IntersectButNotEqualType<D, L, R>
          : NotIntersect<L, R> extends true
            ? NotIntersectType<D, L, R>
            : never
export type SyncRefOptions<
  L,
  R,
  D extends Direction,
> = ConfigurableFlushSync & {
  /**
   * Watch deeply
   *
   * @default false
   */
  deep?: boolean
  /**
   * Sync values immediately
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Direction of syncing. Value will be redefined if you define syncConvertors
   *
   * @default 'both'
   */
  direction?: D
} & TransformType<D, L, R>
/**
 * Two-way refs synchronization.
 * From the set theory perspective to restrict the option's type
 * Check in the following order:
 * 1. L = R
 * 2. L ∩ R ≠ ∅
 * 3. L ⊆ R
 * 4. L ∩ R = ∅
 */
export declare function syncRef<L, R, D extends Direction = "both">(
  left: Ref<L>,
  right: Ref<R>,
  ...[options]: Equal<L, R> extends true
    ? [options?: SyncRefOptions<L, R, D>]
    : [options: SyncRefOptions<L, R, D>]
): () => void
```
```

## File: `skills/vueuse-functions/references/syncRefs.md`
```markdown
---
category: Reactivity
related: syncRef
---

# syncRefs

Keep target refs in sync with a source ref

## Usage

```ts
import { syncRefs } from '@vueuse/core'
import { shallowRef } from 'vue'

const source = shallowRef('hello')
const target = shallowRef('target')

const stop = syncRefs(source, target)

console.log(target.value) // hello

source.value = 'foo'

console.log(target.value) // foo
```

### Sync with multiple targets

You can also pass an array of refs to sync.

```ts
import { syncRefs } from '@vueuse/core'
import { shallowRef } from 'vue'

const source = shallowRef('hello')
const target1 = shallowRef('target1')
const target2 = shallowRef('target2')

const stop = syncRefs(source, [target1, target2])

console.log(target1.value) // hello
console.log(target2.value) // hello

source.value = 'foo'

console.log(target1.value) // foo
console.log(target2.value) // foo
```

## Watch options

The options for `syncRefs` are similar to `watch`'s `WatchOptions` but with different default values.

```ts
export interface SyncRefOptions {
  /**
   * Timing for syncing, same as watch's flush option
   *
   * @default 'sync'
   */
  flush?: WatchOptionFlush
  /**
   * Watch deeply
   *
   * @default false
   */
  deep?: boolean
  /**
   * Sync values immediately
   *
   * @default true
   */
  immediate?: boolean
}
```

When setting `{ flush: 'pre' }`, the target reference will be updated at [the end of the current "tick"](https://vuejs.org/guide/essentials/watchers.html#callback-flush-timing) before rendering starts.

```ts
import { syncRefs } from '@vueuse/core'
import { nextTick, shallowRef } from 'vue'

const source = shallowRef('hello')
const target = shallowRef('target')

syncRefs(source, target, { flush: 'pre' })

console.log(target.value) // hello

source.value = 'foo'

console.log(target.value) // hello <- still unchanged, because of flush 'pre'

await nextTick()

console.log(target.value) // foo <- changed!
```

## Type Declarations

```ts
export interface SyncRefsOptions extends ConfigurableFlushSync {
  /**
   * Watch deeply
   *
   * @default false
   */
  deep?: boolean
  /**
   * Sync values immediately
   *
   * @default true
   */
  immediate?: boolean
}
/**
 * Keep target ref(s) in sync with the source ref
 *
 * @param source source ref
 * @param targets
 */
export declare function syncRefs<T>(
  source: WatchSource<T>,
  targets: Ref<T> | Ref<T>[],
  options?: SyncRefsOptions,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/templateRef.md`
```markdown
---
category: Component
---

::: info
This function will be removed in future version.

Vue 3.5 introduced the `useTemplateRef` API which can effectively replace the functionality of `templateRef`, therefore we recommend using the native approach.
:::

# templateRef

Shorthand for binding ref to template element.

## Usage

<!-- eslint-skip -->

```vue
<script lang="ts">
import { templateRef } from '@vueuse/core'

export default {
  setup() {
    const target = templateRef('target')

    // no need to return the `target`, it will bind to the ref magically
  },
}
</script>

<template>
  <div ref="target" />
</template>
```

### With JSX/TSX

```tsx
import { templateRef } from '@vueuse/core'

export default {
  setup() {
    const target = templateRef<HTMLElement | null>('target', null)

    // use string ref
    return () => <div ref="target"></div>
  },
}
```

### `<script setup>`

There is no need for this when using with `<script setup>` since all the variables will be exposed to the template. It will be exactly the same as `ref`.

```vue
<script setup lang="ts">
import { ref } from 'vue'

const target = ref<HTMLElement | null>(null)
</script>

<template>
  <div ref="target" />
</template>
```

## Type Declarations

```ts
/**
 * @deprecated Use Vue's built-in `useTemplateRef` instead.
 *
 * Shorthand for binding ref to template element.
 *
 * @see https://vueuse.org/templateRef
 * @param key
 * @param initialValue
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function templateRef<
  T extends HTMLElement | SVGElement | Component | null,
  Keys extends string = string,
>(key: Keys, initialValue?: T | null): Readonly<Ref<T>>
```
```

## File: `skills/vueuse-functions/references/toObserver.md`
```markdown
---
category: '@RxJS'
---

# toObserver

Sugar function to convert a `ref` into an RxJS [Observer](https://rxjs.dev/guide/observer).

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { from, fromEvent, toObserver, useSubscription } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { map, mapTo, startWith, takeUntil, withLatestFrom } from 'rxjs/operators'
import { shallowRef, useTemplateRef } from 'vue'

const count = shallowRef(0)
const button = useTemplateRef('buttonRef')

useSubscription(
  interval(1000)
    .pipe(
      mapTo(1),
      takeUntil(fromEvent(button, 'click')),
      withLatestFrom(from(count).pipe(startWith(0))),
      map(([curr, total]) => curr + total),
    )
    .subscribe(toObserver(count)), // same as ).subscribe(val => (count.value = val))
)
```

## Type Declarations

```ts
export declare function toObserver<T>(value: Ref<T>): NextObserver<T>
```
```

## File: `skills/vueuse-functions/references/toReactive.md`
```markdown
---
category: Reactivity
---

# toReactive

Converts ref to reactive. Also made possible to create a "swapable" reactive object.

## Usage

```ts
import { toReactive } from '@vueuse/core'
import { ref } from 'vue'

const refState = ref({ foo: 'bar' })

console.log(refState.value.foo) // => 'bar'

const state = toReactive(refState) // <--

console.log(state.foo) // => 'bar'

refState.value = { bar: 'foo' }

console.log(state.foo) // => undefined
console.log(state.bar) // => 'foo'
```

## Type Declarations

```ts
/**
 * Converts ref to reactive.
 *
 * @see https://vueuse.org/toReactive
 * @param objectRef A ref of object
 */
export declare function toReactive<T extends object>(
  objectRef: MaybeRef<T>,
): UnwrapNestedRefs<T>
```
```

## File: `skills/vueuse-functions/references/toRef.md`
```markdown
---
category: Reactivity
alias: resolveRef
---

# toRef

Normalize value/ref/getter to `ref` or `computed`.

## Usage

```ts
import { toRef } from '@vueuse/core'

const foo = ref('hi')

const a = toRef(0) // Ref<number>
const b = toRef(foo) // Ref<string>
const c = toRef(() => 'hi') // ComputedRef<string>
```

## Differences from Vue's `toRef`

VueUse's `toRef` is not the same as Vue’s `toRef` from the `vue` package.

### VueUse `toRef`

- Accepts **value**, **ref**, or **getter**
- Returns:
  - a **ref** for primitive values
  - a **ref** for existing refs
  - a **computed** for getter functions
- Does **not** accept `object + key`
- Getters always produce readonly computed values

### Vue `toRef`

- Accepts only:
  - a **reactive object + property key**, or
  - an existing **ref**
- Produces a **writable ref** linked to the underlying reactive object
- Does **not** accept primitive values
- Does **not** accept getter functions

### Summary

| Behavior                 | VueUse `toRef`            | Vue `toRef`             |
| ------------------------ | ------------------------- | ----------------------- |
| Accepts primitive values | ✔️                        | ❌                      |
| Accepts getter           | ✔️ (computed)             | ❌                      |
| Accepts existing ref     | ✔️                        | ✔️                      |
| Accepts object + key     | ❌                        | ✔️                      |
| Writable                 | ✔️ (except getter)        | ✔️                      |
| Purpose                  | Normalize to ref/computed | Bind to reactive object |

## Type Declarations

```ts
/**
 * Normalize value/ref/getter to `ref` or `computed`.
 */
export declare function toRef<T>(r: () => T): Readonly<Ref<T>>
export declare function toRef<T>(r: ComputedRef<T>): ComputedRef<T>
export declare function toRef<T>(r: MaybeRefOrGetter<T>): Ref<T>
export declare function toRef<T>(r: T): Ref<T>
export declare function toRef<T extends object, K extends keyof T>(
  object: T,
  key: K,
): ToRef<T[K]>
export declare function toRef<T extends object, K extends keyof T>(
  object: T,
  key: K,
  defaultValue: T[K],
): ToRef<Exclude<T[K], undefined>>
```
```

## File: `skills/vueuse-functions/references/toRefs.md`
```markdown
---
category: Reactivity
---

# toRefs

Extended [`toRefs`](https://vuejs.org/api/reactivity-utilities.html#torefs) that also accepts refs of an object.

## Usage

<!-- eslint-disable array-bracket-spacing -->
<!-- eslint-disable ts/no-redeclare -->

```ts
import { toRefs } from '@vueuse/core'
import { reactive, ref } from 'vue'

const objRef = ref({ a: 'a', b: 0 })
const arrRef = ref(['a', 0])

const { a, b } = toRefs(objRef)
const [a, b] = toRefs(arrRef)

const obj = reactive({ a: 'a', b: 0 })
const arr = reactive(['a', 0])

const { a, b } = toRefs(obj)
const [a, b] = toRefs(arr)
```

## Use-cases

### Destructuring a props object

```vue
<script lang="ts">
import { toRefs, useVModel } from '@vueuse/core'

export default {
  setup(props) {
    const refs = toRefs(useVModel(props, 'data'))

    console.log(refs.a.value) // props.data.a
    refs.a.value = 'a' // emit('update:data', { ...props.data, a: 'a' })

    return { ...refs }
  }
}
</script>

<template>
  <div>
    <input v-model="a" type="text">
    <input v-model="b" type="text">
  </div>
</template>
```

## Type Declarations

```ts
export interface ToRefsOptions {
  /**
   * Replace the original ref with a copy on property update.
   *
   * @default true
   */
  replaceRef?: MaybeRefOrGetter<boolean>
}
/**
 * Extended `toRefs` that also accepts refs of an object.
 *
 * @see https://vueuse.org/toRefs
 * @param objectRef A ref or normal object or array.
 * @param options Options
 */
export declare function toRefs<T extends object>(
  objectRef: MaybeRef<T>,
  options?: ToRefsOptions,
): ToRefs<T>
```
```

## File: `skills/vueuse-functions/references/tryOnBeforeMount.md`
```markdown
---
category: Component
---

# tryOnBeforeMount

Safe `onBeforeMount`. Call `onBeforeMount()` if it's inside a component lifecycle, if not, just call the function

## Usage

```ts
import { tryOnBeforeMount } from '@vueuse/core'

tryOnBeforeMount(() => {

})
```

## Type Declarations

```ts
/**
 * Call onBeforeMount() if it's inside a component lifecycle, if not, just call the function
 *
 * @param fn
 * @param sync if set to false, it will run in the nextTick() of Vue
 * @param target
 */
export declare function tryOnBeforeMount(
  fn: Fn,
  sync?: boolean,
  target?: ComponentInternalInstance | null,
): void
```
```

## File: `skills/vueuse-functions/references/tryOnBeforeUnmount.md`
```markdown
---
category: Component
---

# tryOnBeforeUnmount

Safe `onBeforeUnmount`. Call `onBeforeUnmount()` if it's inside a component lifecycle, if not, do nothing

## Usage

```ts
import { tryOnBeforeUnmount } from '@vueuse/core'

tryOnBeforeUnmount(() => {

})
```

## Type Declarations

```ts
/**
 * Call onBeforeUnmount() if it's inside a component lifecycle, if not, do nothing
 *
 * @param fn
 * @param target
 */
export declare function tryOnBeforeUnmount(
  fn: Fn,
  target?: ComponentInternalInstance | null,
): void
```
```

## File: `skills/vueuse-functions/references/tryOnMounted.md`
```markdown
---
category: Component
---

# tryOnMounted

Safe `onMounted`. Call `onMounted()` if it's inside a component lifecycle, if not, just call the function

## Usage

```ts
import { tryOnMounted } from '@vueuse/core'

tryOnMounted(() => {

})
```

## Type Declarations

```ts
/**
 * Call onMounted() if it's inside a component lifecycle, if not, just call the function
 *
 * @param fn
 * @param sync if set to false, it will run in the nextTick() of Vue
 * @param target
 */
export declare function tryOnMounted(
  fn: Fn,
  sync?: boolean,
  target?: ComponentInternalInstance | null,
): void
```
```

## File: `skills/vueuse-functions/references/tryOnScopeDispose.md`
```markdown
---
category: Component
---

# tryOnScopeDispose

Safe `onScopeDispose`. Call `onScopeDispose()` if it's inside an effect scope lifecycle, if not, do nothing

## Usage

```ts
import { tryOnScopeDispose } from '@vueuse/core'

tryOnScopeDispose(() => {

})
```

## Type Declarations

```ts
/**
 * Call onScopeDispose() if it's inside an effect scope lifecycle, if not, do nothing
 *
 * @param fn
 */
export declare function tryOnScopeDispose(
  fn: Fn,
  failSilently?: boolean,
): boolean
```
```

## File: `skills/vueuse-functions/references/tryOnUnmounted.md`
```markdown
---
category: Component
---

# tryOnUnmounted

Safe `onUnmounted`. Call `onUnmounted()` if it's inside a component lifecycle, if not, do nothing

## Usage

```ts
import { tryOnUnmounted } from '@vueuse/core'

tryOnUnmounted(() => {

})
```

## Type Declarations

```ts
/**
 * Call onUnmounted() if it's inside a component lifecycle, if not, do nothing
 *
 * @param fn
 * @param target
 */
export declare function tryOnUnmounted(
  fn: Fn,
  target?: ComponentInternalInstance | null,
): void
```
```

## File: `skills/vueuse-functions/references/unrefElement.md`
```markdown
---
category: Component
---

# unrefElement

Retrieves the underlying DOM element from a Vue ref or component instance

## Usage

```vue
<script setup lang="ts">
import { unrefElement } from '@vueuse/core'
import { onMounted, useTemplateRef } from 'vue'

const div = useTemplateRef('div') // will be bound to the <div> element
const hello = useTemplateRef('hello') // will be bound to the HelloWorld Component

onMounted(() => {
  console.log(unrefElement(div)) // the <div> element
  console.log(unrefElement(hello)) // the root element of the HelloWorld Component
})
</script>

<template>
  <div ref="div" />
  <HelloWorld ref="hello" />
</template>
```

## Type Declarations

```ts
export type VueInstance = ComponentPublicInstance
export type MaybeElementRef<T extends MaybeElement = MaybeElement> = MaybeRef<T>
export type MaybeComputedElementRef<T extends MaybeElement = MaybeElement> =
  MaybeRefOrGetter<T>
export type MaybeElement =
  | HTMLElement
  | SVGElement
  | VueInstance
  | undefined
  | null
export type UnRefElementReturn<T extends MaybeElement = MaybeElement> =
  T extends VueInstance ? Exclude<MaybeElement, VueInstance> : T | undefined
/**
 * Get the dom element of a ref of element or Vue component instance
 *
 * @param elRef
 */
export declare function unrefElement<T extends MaybeElement>(
  elRef: MaybeComputedElementRef<T>,
): UnRefElementReturn<T>
```
```

## File: `skills/vueuse-functions/references/until.md`
```markdown
---
category: Watch
---

# until

Promised one-time watch for changes

## Usage

#### Wait for some async data to be ready

```ts
import { until, useAsyncState } from '@vueuse/core'

const { state, isReady } = useAsyncState(
  fetch('https://jsonplaceholder.typicode.com/todos/1').then(t => t.json()),
  {},
)

;(async () => {
  await until(isReady).toBe(true)

  console.log(state) // state is now ready!
})()
```

#### Wait for custom conditions

> You can use `invoke` to call the async function.

```ts
import { invoke, until, useCounter } from '@vueuse/core'

const { count } = useCounter()

invoke(async () => {
  await until(count).toMatch(v => v > 7)

  alert('Counter is now larger than 7!')
})
```

#### Timeout

```ts
import { until } from '@vueuse/core'
// ---cut---
// will be resolve until ref.value === true or 1000ms passed
await until(ref).toBe(true, { timeout: 1000 })

// will throw if timeout
try {
  await until(ref).toBe(true, { timeout: 1000, throwOnTimeout: true })
  // ref.value === true
}
catch (e) {
  // timeout
}
```

#### More Examples

```ts
import { until } from '@vueuse/core'
// ---cut---
await until(ref).toBe(true)
await until(ref).toMatch(v => v > 10 && v < 100)
await until(ref).changed()
await until(ref).changedTimes(10)
await until(ref).toBeTruthy()
await until(ref).toBeNull()

await until(ref).not.toBeNull()
await until(ref).not.toBeTruthy()
```

## Type Declarations

```ts
export interface UntilToMatchOptions extends ConfigurableFlushSync {
  /**
   * Milliseconds timeout for promise to resolve/reject if the when condition does not meet.
   * 0 for never timed out
   *
   * @default 0
   */
  timeout?: number
  /**
   * Reject the promise when timeout
   *
   * @default false
   */
  throwOnTimeout?: boolean
  /**
   * `deep` option for internal watch
   *
   * @default 'false'
   */
  deep?: WatchOptions["deep"]
}
export interface UntilBaseInstance<T, Not extends boolean = false> {
  toMatch: (<U extends T = T>(
    condition: (v: T) => v is U,
    options?: UntilToMatchOptions,
  ) => Not extends true ? Promise<Exclude<T, U>> : Promise<U>) &
    ((
      condition: (v: T) => boolean,
      options?: UntilToMatchOptions,
    ) => Promise<T>)
  changed: (options?: UntilToMatchOptions) => Promise<T>
  changedTimes: (n?: number, options?: UntilToMatchOptions) => Promise<T>
}
type Falsy = false | void | null | undefined | 0 | 0n | ""
export interface UntilValueInstance<
  T,
  Not extends boolean = false,
> extends UntilBaseInstance<T, Not> {
  readonly not: UntilValueInstance<T, Not extends true ? false : true>
  toBe: <P = T>(
    value: MaybeRefOrGetter<P>,
    options?: UntilToMatchOptions,
  ) => Not extends true ? Promise<T> : Promise<P>
  toBeTruthy: (
    options?: UntilToMatchOptions,
  ) => Not extends true ? Promise<T & Falsy> : Promise<Exclude<T, Falsy>>
  toBeNull: (
    options?: UntilToMatchOptions,
  ) => Not extends true ? Promise<Exclude<T, null>> : Promise<null>
  toBeUndefined: (
    options?: UntilToMatchOptions,
  ) => Not extends true ? Promise<Exclude<T, undefined>> : Promise<undefined>
  toBeNaN: (options?: UntilToMatchOptions) => Promise<T>
}
export interface UntilArrayInstance<T> extends UntilBaseInstance<T> {
  readonly not: UntilArrayInstance<T>
  toContains: (
    value: MaybeRefOrGetter<ElementOf<ShallowUnwrapRef<T>>>,
    options?: UntilToMatchOptions,
  ) => Promise<T>
}
/**
 * Promised one-time watch for changes
 *
 * @see https://vueuse.org/until
 * @example
 * ```
 * const { count } = useCounter()
 *
 * await until(count).toMatch(v => v > 7)
 *
 * alert('Counter is now larger than 7!')
 * ```
 */
export declare function until<T extends unknown[]>(
  r: WatchSource<T> | MaybeRefOrGetter<T>,
): UntilArrayInstance<T>
export declare function until<T>(
  r: WatchSource<T> | MaybeRefOrGetter<T>,
): UntilValueInstance<T>
```
```

## File: `skills/vueuse-functions/references/useAbs.md`
```markdown
---
category: '@Math'
---

# useAbs

Reactive `Math.abs`.

## Usage

```ts
import { useAbs } from '@vueuse/math'

const value = ref(-23)
const absValue = useAbs(value) // Ref<23>
```

## Type Declarations

```ts
/**
 * Reactive `Math.abs`.
 *
 * @see https://vueuse.org/useAbs
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useAbs(
  value: MaybeRefOrGetter<number>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useActiveElement.md`
```markdown
---
category: Elements
---

# useActiveElement

Reactive `document.activeElement`. Returns a shallow ref that updates when focus changes.

## Usage

```vue
<script setup lang="ts">
import { useActiveElement } from '@vueuse/core'
import { watch } from 'vue'

const activeElement = useActiveElement()

watch(activeElement, (el) => {
  console.log('focus changed to', el)
})
</script>
```

### Shadow DOM Support

By default, `useActiveElement` will traverse into shadow DOM to find the deeply active element. Set `deep: false` to disable this behavior.

```ts
import { useActiveElement } from '@vueuse/core'

// Only get the shadow host, not the element inside shadow DOM
const activeElement = useActiveElement({ deep: false })
```

### Track Element Removal

Set `triggerOnRemoval: true` to update the active element when the currently active element is removed from the DOM. This uses a `MutationObserver` under the hood.

```ts
import { useActiveElement } from '@vueuse/core'

const activeElement = useActiveElement({ triggerOnRemoval: true })
```

## Component Usage

```vue
<template>
  <UseActiveElement v-slot="{ element }">
    Active element is {{ element?.dataset.id }}
  </UseActiveElement>
</template>
```

## Type Declarations

```ts
export interface UseActiveElementOptions
  extends ConfigurableWindow, ConfigurableDocumentOrShadowRoot {
  /**
   * Search active element deeply inside shadow dom
   *
   * @default true
   */
  deep?: boolean
  /**
   * Track active element when it's removed from the DOM
   * Using a MutationObserver under the hood
   * @default false
   */
  triggerOnRemoval?: boolean
}
export type UseActiveElementReturn<T extends HTMLElement = HTMLElement> =
  ShallowRef<T | null | undefined>
/**
 * Reactive `document.activeElement`
 *
 * @see https://vueuse.org/useActiveElement
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useActiveElement<T extends HTMLElement>(
  options?: UseActiveElementOptions,
): UseActiveElementReturn<T>
```
```

## File: `skills/vueuse-functions/references/useAnimate.md`
```markdown
---
category: Animation
---

# useAnimate

Reactive [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API).

## Usage

### Basic Usage

The `useAnimate` function returns the animation instance and control functions.

```vue
<script setup lang="ts">
import { useAnimate } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const {
  isSupported,
  animate,

  // actions
  play,
  pause,
  reverse,
  finish,
  cancel,

  // states
  pending,
  playState,
  replaceState,
  startTime,
  currentTime,
  timeline,
  playbackRate,
} = useAnimate(el, { transform: 'rotate(360deg)' }, 1000)
</script>

<template>
  <span ref="el" style="display:inline-block">useAnimate</span>
</template>
```

### Custom Keyframes

Either an array of keyframe objects, or a keyframe object, or a `ref`. See [Keyframe Formats](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Keyframe_Formats) for more details.

```ts
import { useAnimate } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
// ---cut---
const keyframes = { transform: 'rotate(360deg)' }
// Or
const keyframes = [
  { transform: 'rotate(0deg)' },
  { transform: 'rotate(360deg)' },
]
// Or
const keyframes = ref([
  { clipPath: 'circle(20% at 0% 30%)' },
  { clipPath: 'circle(20% at 50% 80%)' },
  { clipPath: 'circle(20% at 100% 30%)' },
])

useAnimate(el, keyframes, 1000)
```

### Options

The third argument accepts a duration number or an options object with the following additional properties on top of [KeyframeAnimationOptions](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate#parameters):

```ts
import { useAnimate } from '@vueuse/core'

useAnimate(el, keyframes, {
  duration: 1000,
  // Start playing immediately (default: true)
  immediate: true,
  // Commit the end styling state to the element (default: false)
  commitStyles: false,
  // Persist the animation (default: false)
  persist: false,
  // Callback when animation is initialized
  onReady(animate) {
    console.log('Animation ready', animate)
  },
  // Callback when an error occurs
  onError(e) {
    console.error('Animation error', e)
  },
})
```

### Delaying Start

Set `immediate: false` to prevent the animation from starting automatically.

```ts
import { useAnimate } from '@vueuse/core'

const { play } = useAnimate(el, keyframes, {
  duration: 1000,
  immediate: false,
})

// Start the animation manually
play()
```

## Type Declarations

```ts
export interface UseAnimateOptions
  extends KeyframeAnimationOptions, ConfigurableWindow {
  /**
   * Will automatically run play when `useAnimate` is used
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Whether to commits the end styling state of an animation to the element being animated
   * In general, you should use `fill` option with this.
   *
   * @default false
   */
  commitStyles?: boolean
  /**
   * Whether to persists the animation
   *
   * @default false
   */
  persist?: boolean
  /**
   * Executed after animation initialization
   */
  onReady?: (animate: Animation) => void
  /**
   * Callback when error is caught.
   */
  onError?: (e: unknown) => void
}
export type UseAnimateKeyframes = MaybeRef<
  Keyframe[] | PropertyIndexedKeyframes | null
>
export interface UseAnimateReturn extends Supportable {
  animate: ShallowRef<Animation | undefined>
  play: () => void
  pause: () => void
  reverse: () => void
  finish: () => void
  cancel: () => void
  pending: ComputedRef<boolean>
  playState: ComputedRef<AnimationPlayState>
  replaceState: ComputedRef<AnimationReplaceState>
  startTime: WritableComputedRef<CSSNumberish | number | null>
  currentTime: WritableComputedRef<CSSNumberish | null>
  timeline: WritableComputedRef<AnimationTimeline | null>
  playbackRate: WritableComputedRef<number>
}
/**
 * Reactive Web Animations API
 *
 * @see https://vueuse.org/useAnimate
 * @param target
 * @param keyframes
 * @param options
 */
export declare function useAnimate(
  target: MaybeComputedElementRef,
  keyframes: UseAnimateKeyframes,
  options?: number | UseAnimateOptions,
): UseAnimateReturn
```
```

## File: `skills/vueuse-functions/references/useArrayDifference.md`
```markdown
---
category: Array
---

# useArrayDifference

Reactive get array difference of two arrays.

By default, it returns the difference of the first array from the second array, so call `A \ B`, [Relative Complement](<https://en.wikipedia.org/wiki/Complement_(set_theory)>) of B in A.

You can pass the `symmetric` option to get the [Symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) of two arrays `A △ B`.

## Usage

### Use with reactive array

```ts
import { useArrayDifference } from '@vueuse/core'

const list1 = ref([0, 1, 2, 3, 4, 5])
const list2 = ref([4, 5, 6])
const result = useArrayDifference(list1, list2)
// result.value: [0, 1, 2, 3]
list2.value = [0, 1, 2]
// result.value: [3, 4, 5]
```

### Use with reactive array and use function comparison

```ts
import { useArrayDifference } from '@vueuse/core'

const list1 = ref([{ id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }, { id: 5 }])
const list2 = ref([{ id: 4 }, { id: 5 }, { id: 6 }])

const result = useArrayDifference(list1, list2, (value, othVal) => value.id === othVal.id)
// result.value: [{ id: 1 }, { id: 2 }, { id: 3 }]
```

### Symmetric Difference

This composable also supports [Symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) by passing the `symmetric` option.

```ts {10}
import { useArrayDifference } from '@vueuse/core'

const list1 = ref([{ id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }, { id: 5 }])
const list2 = ref([{ id: 4 }, { id: 5 }, { id: 6 }])

const result = useArrayDifference(
  list1,
  list2,
  (value, othVal) => value.id === othVal.id,
  { symmetric: true }
)
// result.value: [{ id: 1 }, { id: 2 }, { id: 3 }, { id: 6 }]
```

## Type Declarations

```ts
export interface UseArrayDifferenceOptions {
  /**
   * Returns asymmetric difference
   *
   * @see https://en.wikipedia.org/wiki/Symmetric_difference
   * @default false
   */
  symmetric?: boolean
}
export type UseArrayDifferenceReturn<T = any> = ComputedRef<T[]>
export declare function useArrayDifference<T>(
  list: MaybeRefOrGetter<T[]>,
  values: MaybeRefOrGetter<T[]>,
  key?: keyof T,
  options?: UseArrayDifferenceOptions,
): UseArrayDifferenceReturn<T>
export declare function useArrayDifference<T>(
  list: MaybeRefOrGetter<T[]>,
  values: MaybeRefOrGetter<T[]>,
  compareFn?: (value: T, othVal: T) => boolean,
  options?: UseArrayDifferenceOptions,
): UseArrayDifferenceReturn<T>
```
```

## File: `skills/vueuse-functions/references/useArrayEvery.md`
```markdown
---
category: Array
---

# useArrayEvery

Reactive `Array.every`

## Usage

### Use with array of multiple refs

```ts
import { useArrayEvery } from '@vueuse/core'

const item1 = ref(0)
const item2 = ref(2)
const item3 = ref(4)
const item4 = ref(6)
const item5 = ref(8)
const list = [item1, item2, item3, item4, item5]
const result = useArrayEvery(list, i => i % 2 === 0)
// result.value: true
item1.value = 1
// result.value: false
```

### Use with reactive array

```ts
import { useArrayEvery } from '@vueuse/core'

const list = ref([0, 2, 4, 6, 8])
const result = useArrayEvery(list, i => i % 2 === 0)
// result.value: true
list.value.push(9)
// result.value: false
```

## Type Declarations

```ts
export type UseArrayEveryReturn = ComputedRef<boolean>
/**
 * Reactive `Array.every`
 *
 * @see https://vueuse.org/useArrayEvery
 * @param list - the array was called upon.
 * @param fn - a function to test each element.
 *
 * @returns **true** if the `fn` function returns a **truthy** value for every element from the array. Otherwise, **false**.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayEvery<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: MaybeRefOrGetter<T>[]) => unknown,
): UseArrayEveryReturn
```
```

## File: `skills/vueuse-functions/references/useArrayFilter.md`
```markdown
---
category: Array
---

# useArrayFilter

Reactive `Array.filter`

## Usage

### Use with array of multiple refs

```ts
import { useArrayFilter } from '@vueuse/core'

const item1 = ref(0)
const item2 = ref(2)
const item3 = ref(4)
const item4 = ref(6)
const item5 = ref(8)
const list = [item1, item2, item3, item4, item5]
const result = useArrayFilter(list, i => i % 2 === 0)
// result.value: [0, 2, 4, 6, 8]
item2.value = 1
// result.value: [0, 4, 6, 8]
```

### Use with reactive array

```ts
import { useArrayFilter } from '@vueuse/core'

const list = ref([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
const result = useArrayFilter(list, i => i % 2 === 0)
// result.value: [0, 2, 4, 6, 8]
list.value.shift()
// result.value: [2, 4, 6, 8]
```

## Type Declarations

```ts
export type UseArrayFilterReturn<T = any> = ComputedRef<T[]>
/**
 * Reactive `Array.filter`
 *
 * @see https://vueuse.org/useArrayFilter
 * @param list - the array was called upon.
 * @param fn - a function that is called for every element of the given `list`. Each time `fn` executes, the returned value is added to the new array.
 *
 * @returns a shallow copy of a portion of the given array, filtered down to just the elements from the given array that pass the test implemented by the provided function. If no elements pass the test, an empty array will be returned.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayFilter<T, S extends T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: T[]) => element is S,
): UseArrayFilterReturn<S>
export declare function useArrayFilter<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: T[]) => unknown,
): UseArrayFilterReturn<T>
```
```

## File: `skills/vueuse-functions/references/useArrayFind.md`
```markdown
---
category: Array
---

# useArrayFind

Reactive `Array.find`.

## Usage

```ts
import { useArrayFind } from '@vueuse/core'

const list = [ref(1), ref(-1), ref(2)]
const positive = useArrayFind(list, val => val > 0)
// positive.value: 1
```

### Use with reactive array

```ts
import { useArrayFind } from '@vueuse/core'

const list = reactive([-1, -2])
const positive = useArrayFind(list, val => val > 0)
// positive.value: undefined
list.push(1)
// positive.value: 1
```

## Type Declarations

```ts
export type UseArrayFindReturn<T = any> = ComputedRef<T | undefined>
/**
 * Reactive `Array.find`
 *
 * @see https://vueuse.org/useArrayFind
 * @param list - the array was called upon.
 * @param fn - a function to test each element.
 *
 * @returns the first element in the array that satisfies the provided testing function. Otherwise, undefined is returned.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayFind<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: MaybeRefOrGetter<T>[]) => boolean,
): UseArrayFindReturn<T>
```
```

## File: `skills/vueuse-functions/references/useArrayFindIndex.md`
```markdown
---
category: Array
---

# useArrayFindIndex

Reactive `Array.findIndex`

## Usage

### Use with array of multiple refs

```ts
import { useArrayFindIndex } from '@vueuse/core'

const item1 = ref(0)
const item2 = ref(2)
const item3 = ref(4)
const item4 = ref(6)
const item5 = ref(8)
const list = [item1, item2, item3, item4, item5]
const result = useArrayFindIndex(list, i => i % 2 === 0)
// result.value: 0
item1.value = 1
// result.value: 1
```

### Use with reactive array

```ts
import { useArrayFindIndex } from '@vueuse/core'

const list = ref([0, 2, 4, 6, 8])
const result = useArrayFindIndex(list, i => i % 2 === 0)
// result.value: 0
list.value.unshift(-1)
// result.value: 1
```

## Type Declarations

```ts
export type UseArrayFindIndexReturn = ComputedRef<number>
/**
 * Reactive `Array.findIndex`
 *
 * @see https://vueuse.org/useArrayFindIndex
 * @param list - the array was called upon.
 * @param fn - a function to test each element.
 *
 * @returns the index of the first element in the array that passes the test. Otherwise, "-1".
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayFindIndex<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: MaybeRefOrGetter<T>[]) => unknown,
): UseArrayFindIndexReturn
```
```

## File: `skills/vueuse-functions/references/useArrayFindLast.md`
```markdown
---
category: Array
---

# useArrayFindLast

Reactive `Array.findLast`.

## Usage

```ts
import { useArrayFindLast } from '@vueuse/core'

const list = [ref(1), ref(-1), ref(2)]
const positive = useArrayFindLast(list, val => val > 0)
// positive.value: 2
```

### Use with reactive array

```ts
import { useArrayFindLast } from '@vueuse/core'

const list = reactive([-1, -2])
const positive = useArrayFindLast(list, val => val > 0)
// positive.value: undefined
list.push(10)
// positive.value: 10
list.push(5)
// positive.value: 5
```

## Type Declarations

```ts
export type UseArrayFindLastReturn<T = any> = ComputedRef<T | undefined>
/**
 * Reactive `Array.findLast`
 *
 * @see https://vueuse.org/useArrayFindLast
 * @param list - the array was called upon.
 * @param fn - a function to test each element.
 *
 * @returns the last element in the array that satisfies the provided testing function. Otherwise, undefined is returned.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayFindLast<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: MaybeRefOrGetter<T>[]) => boolean,
): UseArrayFindLastReturn<T>
```
```

## File: `skills/vueuse-functions/references/useArrayIncludes.md`
```markdown
---
category: Array
---

# useArrayIncludes

Reactive `Array.includes`

## Usage

### Use with reactive array

```ts
import { useArrayIncludes } from '@vueuse/core'

const list = ref([0, 2, 4, 6, 8])
const result = useArrayIncludes(list, 10)
// result.value: false
list.value.push(10)
// result.value: true
list.value.pop()
// result.value: false
```

## Type Declarations

```ts
export type UseArrayIncludesComparatorFn<T, V> = (
  element: T,
  value: V,
  index: number,
  array: MaybeRefOrGetter<T>[],
) => boolean
export interface UseArrayIncludesOptions<T, V> {
  fromIndex?: number
  comparator?: UseArrayIncludesComparatorFn<T, V> | keyof T
}
export type UseArrayIncludesReturn = ComputedRef<boolean>
/**
 * Reactive `Array.includes`
 *
 * @see https://vueuse.org/useArrayIncludes
 *
 * @returns true if the `value` is found in the array. Otherwise, false.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayIncludes<T, V = any>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  value: MaybeRefOrGetter<V>,
  comparator?: UseArrayIncludesComparatorFn<T, V>,
): UseArrayIncludesReturn
export declare function useArrayIncludes<T, V = any>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  value: MaybeRefOrGetter<V>,
  comparator?: keyof T,
): UseArrayIncludesReturn
export declare function useArrayIncludes<T, V = any>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  value: MaybeRefOrGetter<V>,
  options?: UseArrayIncludesOptions<T, V>,
): UseArrayIncludesReturn
```
```

## File: `skills/vueuse-functions/references/useArrayJoin.md`
```markdown
---
category: Array
---

# useArrayJoin

Reactive `Array.join`

## Usage

### Use with array of multiple refs

```ts
import { useArrayJoin } from '@vueuse/core'

const item1 = ref('foo')
const item2 = ref(0)
const item3 = ref({ prop: 'val' })
const list = [item1, item2, item3]
const result = useArrayJoin(list)
// result.value: foo,0,[object Object]
item1.value = 'bar'
// result.value: bar,0,[object Object]
```

### Use with reactive array

```ts
import { useArrayJoin } from '@vueuse/core'

const list = ref(['string', 0, { prop: 'val' }, false, [1], [[2]], null, undefined, []])
const result = useArrayJoin(list)
// result.value: string,0,[object Object],false,1,2,,,
list.value.push(true)
// result.value: string,0,[object Object],false,1,2,,,,true
list.value = [null, 'string', undefined]
// result.value: ,string,
```

### Use with reactive separator

```ts
import { useArrayJoin } from '@vueuse/core'

const list = ref(['string', 0, { prop: 'val' }])
const separator = ref()
const result = useArrayJoin(list, separator)
// result.value: string,0,[object Object]
separator.value = ''
// result.value: string0[object Object]
separator.value = '--'
// result.value: string--0--[object Object]
```

## Type Declarations

```ts
export type UseArrayJoinReturn = ComputedRef<string>
/**
 * Reactive `Array.join`
 *
 * @see https://vueuse.org/useArrayJoin
 * @param list - the array was called upon.
 * @param separator - a string to separate each pair of adjacent elements of the array. If omitted, the array elements are separated with a comma (",").
 *
 * @returns a string with all array elements joined. If arr.length is 0, the empty string is returned.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayJoin(
  list: MaybeRefOrGetter<MaybeRefOrGetter<any>[]>,
  separator?: MaybeRefOrGetter<string>,
): UseArrayJoinReturn
```
```

## File: `skills/vueuse-functions/references/useArrayMap.md`
```markdown
---
category: Array
---

# useArrayMap

Reactive `Array.map`

## Usage

### Use with array of multiple refs

```ts
import { useArrayMap } from '@vueuse/core'

const item1 = ref(0)
const item2 = ref(2)
const item3 = ref(4)
const item4 = ref(6)
const item5 = ref(8)
const list = [item1, item2, item3, item4, item5]
const result = useArrayMap(list, i => i * 2)
// result.value: [0, 4, 8, 12, 16]
item1.value = 1
// result.value: [2, 4, 8, 12, 16]
```

### Use with reactive array

```ts
import { useArrayMap } from '@vueuse/core'

const list = ref([0, 1, 2, 3, 4])
const result = useArrayMap(list, i => i * 2)
// result.value: [0, 2, 4, 6, 8]
list.value.pop()
// result.value: [0, 2, 4, 6]
```

## Type Declarations

```ts
export type UseArrayMapReturn<T = any> = ComputedRef<T[]>
/**
 * Reactive `Array.map`
 *
 * @see https://vueuse.org/useArrayMap
 * @param list - the array was called upon.
 * @param fn - a function that is called for every element of the given `list`. Each time `fn` executes, the returned value is added to the new array.
 *
 * @returns a new array with each element being the result of the callback function.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayMap<T, U = T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: T[]) => U,
): UseArrayMapReturn<U>
```
```

## File: `skills/vueuse-functions/references/useArrayReduce.md`
```markdown
---
category: Array
---

# useArrayReduce

Reactive `Array.reduce`.

## Usage

```ts
import { useArrayReduce } from '@vueuse/core'

const sum = useArrayReduce([ref(1), ref(2), ref(3)], (sum, val) => sum + val)
// sum.value: 6
```

### Use with reactive array

```ts
import { useArrayReduce } from '@vueuse/core'

const list = reactive([1, 2])
const sum = useArrayReduce(list, (sum, val) => sum + val)

list.push(3)
// sum.value: 6
```

### Use with initialValue

```ts
import { useArrayReduce } from '@vueuse/core'

const list = reactive([{ num: 1 }, { num: 2 }])
const sum = useArrayReduce(list, (sum, val) => sum + val.num, 0)
// sum.value: 3
```

## Type Declarations

```ts
export type UseArrayReducer<PV, CV, R> = (
  previousValue: PV,
  currentValue: CV,
  currentIndex: number,
) => R
export type UseArrayReduceReturn<T = any> = ComputedRef<T>
/**
 * Reactive `Array.reduce`
 *
 * @see https://vueuse.org/useArrayReduce
 * @param list - the array was called upon.
 * @param reducer - a "reducer" function.
 *
 * @returns the value that results from running the "reducer" callback function to completion over the entire array.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayReduce<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  reducer: UseArrayReducer<T, T, T>,
): UseArrayReduceReturn<T>
/**
 * Reactive `Array.reduce`
 *
 * @see https://vueuse.org/useArrayReduce
 * @param list - the array was called upon.
 * @param reducer - a "reducer" function.
 * @param initialValue - a value to be initialized the first time when the callback is called.
 *
 * @returns the value that results from running the "reducer" callback function to completion over the entire array.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayReduce<T, U>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  reducer: UseArrayReducer<U, T, U>,
  initialValue: MaybeRefOrGetter<U>,
): UseArrayReduceReturn<U>
```
```

## File: `skills/vueuse-functions/references/useArraySome.md`
```markdown
---
category: Array
---

# useArraySome

Reactive `Array.some`

## Usage

### Use with array of multiple refs

```ts
import { useArraySome } from '@vueuse/core'

const item1 = ref(0)
const item2 = ref(2)
const item3 = ref(4)
const item4 = ref(6)
const item5 = ref(8)
const list = [item1, item2, item3, item4, item5]
const result = useArraySome(list, i => i > 10)
// result.value: false
item1.value = 11
// result.value: true
```

### Use with reactive array

```ts
import { useArraySome } from '@vueuse/core'

const list = ref([0, 2, 4, 6, 8])
const result = useArraySome(list, i => i > 10)
// result.value: false
list.value.push(11)
// result.value: true
```

## Type Declarations

```ts
export type UseArraySomeReturn = ComputedRef<boolean>
/**
 * Reactive `Array.some`
 *
 * @see https://vueuse.org/useArraySome
 * @param list - the array was called upon.
 * @param fn - a function to test each element.
 *
 * @returns **true** if the `fn` function returns a **truthy** value for any element from the array. Otherwise, **false**.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArraySome<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  fn: (element: T, index: number, array: MaybeRefOrGetter<T>[]) => unknown,
): UseArraySomeReturn
```
```

## File: `skills/vueuse-functions/references/useArrayUnique.md`
```markdown
---
category: Array
---

# useArrayUnique

reactive unique array

## Usage

### Use with array of multiple refs

```ts
import { useArrayUnique } from '@vueuse/core'

const item1 = ref(0)
const item2 = ref(1)
const item3 = ref(1)
const item4 = ref(2)
const item5 = ref(3)
const list = [item1, item2, item3, item4, item5]
const result = useArrayUnique(list)
// result.value: [0, 1, 2, 3]
item5.value = 1
// result.value: [0, 1, 2]
```

### Use with reactive array

```ts
import { useArrayUnique } from '@vueuse/core'

const list = reactive([1, 2, 2, 3])
const result = useArrayUnique(list)
// result.value: [1, 2, 3]

list.push(1)
// result.value: [1, 2, 3]
```

### Use with custom function

```ts
import { useArrayUnique } from '@vueuse/core'

const list = reactive([
  { id: 1, name: 'foo' },
  { id: 2, name: 'bar' },
  { id: 1, name: 'baz' },
])

const result = useArrayUnique(list, (a, b) => a.id === b.id)
// result.value: [{ id: 1, name: 'foo' }, { id: 2, name: 'bar' }]

list.push({ id: 1, name: 'qux' })
// result.value: [{ id: 1, name: 'foo' }, { id: 2, name: 'bar' }]
```

## Type Declarations

```ts
export type UseArrayUniqueReturn<T = any> = ComputedRef<T[]>
/**
 * reactive unique array
 * @see https://vueuse.org/useArrayUnique
 * @param list - the array was called upon.
 * @param compareFn
 * @returns A computed ref that returns a unique array of items.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useArrayUnique<T>(
  list: MaybeRefOrGetter<MaybeRefOrGetter<T>[]>,
  compareFn?: (a: T, b: T, array: T[]) => boolean,
): UseArrayUniqueReturn<T>
```
```

## File: `skills/vueuse-functions/references/useAsyncQueue.md`
```markdown
---
category: Utilities
---

# useAsyncQueue

Executes each asynchronous task sequentially and passes the current task result to the next task.

## Usage

```ts
import { useAsyncQueue } from '@vueuse/core'

function p1() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(1000)
    }, 10)
  })
}

function p2(result: number) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(1000 + result)
    }, 20)
  })
}

const { activeIndex, result } = useAsyncQueue([p1, p2])

console.log(activeIndex.value) // current pending task index

console.log(result) // the tasks result
```

### Result State

Each task in the result array has a `state` and `data` property:

```ts
interface UseAsyncQueueResult<T> {
  state: 'aborted' | 'fulfilled' | 'pending' | 'rejected'
  data: T | null
}
```

### Interrupt on Failure

By default, if a task fails, subsequent tasks will not be executed. Set `interrupt: false` to continue executing even after failures.

```ts
const { result } = useAsyncQueue([p1, p2], {
  interrupt: false, // continue even if p1 fails
})
```

### Callbacks

```ts
const { result } = useAsyncQueue([p1, p2], {
  onError() {
    console.log('A task failed')
  },
  onFinished() {
    console.log('All tasks completed (or interrupted)')
  },
})
```

### Abort Signal

You can pass an `AbortSignal` to cancel the queue execution.

```ts
const controller = new AbortController()

const { result } = useAsyncQueue([p1, p2], {
  signal: controller.signal,
})

// Later, abort the queue
controller.abort()
```

## Type Declarations

```ts
export type UseAsyncQueueTask<T> = (...args: any[]) => T | Promise<T>
type MapQueueTask<T extends any[]> = {
  [K in keyof T]: UseAsyncQueueTask<T[K]>
}
export interface UseAsyncQueueResult<T> {
  state: "aborted" | "fulfilled" | "pending" | "rejected"
  data: T | null
}
export interface UseAsyncQueueReturn<T> {
  activeIndex: ShallowRef<number>
  result: T
}
export interface UseAsyncQueueOptions {
  /**
   * Interrupt tasks when current task fails.
   *
   * @default true
   */
  interrupt?: boolean
  /**
   * Trigger it when the tasks fails.
   *
   */
  onError?: () => void
  /**
   * Trigger it when the tasks ends.
   *
   */
  onFinished?: () => void
  /**
   * A AbortSignal that can be used to abort the task.
   */
  signal?: AbortSignal
}
/**
 * Asynchronous queue task controller.
 *
 * @see https://vueuse.org/useAsyncQueue
 * @param tasks
 * @param options
 */
export declare function useAsyncQueue<T extends any[], S = MapQueueTask<T>>(
  tasks: S & Array<UseAsyncQueueTask<any>>,
  options?: UseAsyncQueueOptions,
): UseAsyncQueueReturn<{
  [P in keyof T]: UseAsyncQueueResult<T[P]>
}>
```
```

## File: `skills/vueuse-functions/references/useAsyncState.md`
```markdown
---
category: State
---

# useAsyncState

Reactive async state. Will not block your setup function and will trigger changes once the promise is ready. The state is a `shallowRef` by default.

## Usage

```ts
import { useAsyncState } from '@vueuse/core'
import axios from 'axios'

const { state, isReady, isLoading, error } = useAsyncState(
  axios
    .get('https://jsonplaceholder.typicode.com/todos/1')
    .then(t => t.data),
  { id: null },
)
```

### Return Values

| Property           | Description                                         |
| ------------------ | --------------------------------------------------- |
| `state`            | The result of the async function                    |
| `isReady`          | `true` when the promise has resolved at least once  |
| `isLoading`        | `true` while the promise is pending                 |
| `error`            | The error if the promise was rejected               |
| `execute`          | Re-execute the async function with optional delay   |
| `executeImmediate` | Re-execute immediately (shorthand for `execute(0)`) |

### Awaiting the Result

The return value is thenable, so you can await it in async functions or `<script setup>`:

```ts
const { state, isReady } = await useAsyncState(fetchData, null)
// `state` is now populated, `isReady` is true
```

### Manual Execution

Set `immediate: false` to prevent automatic execution on creation.

```vue
<script setup lang="ts">
import { useAsyncState } from '@vueuse/core'

const { state, execute, executeImmediate } = useAsyncState(action, '', { immediate: false })

async function action(event) {
  await new Promise(resolve => setTimeout(resolve, 500))
  return `${event.target.textContent} clicked!`
}
</script>

<template>
  <p>State: {{ state }}</p>

  <button class="button" @click="executeImmediate">
    Execute now
  </button>

  <button class="ml-2 button" @click="event => execute(500, event)">
    Execute with delay
  </button>
</template>
```

### Options

```ts
const { state } = useAsyncState(promise, initialState, {
  // Execute immediately on creation (default: true)
  immediate: true,
  // Delay before first execution in ms (default: 0)
  delay: 0,
  // Reset state to initial before each execution (default: true)
  resetOnExecute: true,
  // Use shallowRef for state (default: true)
  shallow: true,
  // Throw errors instead of catching them (default: false)
  throwError: false,
  // Called when promise resolves
  onSuccess(data) {
    console.log('Success:', data)
  },
  // Called when promise rejects
  onError(error) {
    console.error('Error:', error)
  },
})
```

## Type Declarations

```ts
export interface UseAsyncStateReturnBase<
  Data,
  Params extends any[],
  Shallow extends boolean,
> {
  state: Shallow extends true ? Ref<Data> : Ref<UnwrapRef<Data>>
  isReady: Ref<boolean>
  isLoading: Ref<boolean>
  error: Ref<unknown>
  execute: (delay?: number, ...args: Params) => Promise<Data | undefined>
  executeImmediate: (...args: Params) => Promise<Data | undefined>
}
export type UseAsyncStateReturn<
  Data,
  Params extends any[],
  Shallow extends boolean,
> = UseAsyncStateReturnBase<Data, Params, Shallow> &
  PromiseLike<UseAsyncStateReturnBase<Data, Params, Shallow>>
export interface UseAsyncStateOptions<Shallow extends boolean, D = any> {
  /**
   * Delay for the first execution of the promise when "immediate" is true. In milliseconds.
   *
   * @default 0
   */
  delay?: number
  /**
   * Execute the promise right after the function is invoked.
   * Will apply the delay if any.
   *
   * When set to false, you will need to execute it manually.
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Callback when error is caught.
   */
  onError?: (e: unknown) => void
  /**
   * Callback when success is caught.
   * @param {D} data
   */
  onSuccess?: (data: D) => void
  /**
   * Sets the state to initialState before executing the promise.
   *
   * This can be useful when calling the execute function more than once (for
   * example, to refresh data). When set to false, the current state remains
   * unchanged until the promise resolves.
   *
   * @default true
   */
  resetOnExecute?: boolean
  /**
   * Use shallowRef.
   *
   * @default true
   */
  shallow?: Shallow
  /**
   *
   * An error is thrown when executing the execute function
   *
   * @default false
   */
  throwError?: boolean
}
/**
 * Reactive async state. Will not block your setup function and will trigger changes once
 * the promise is ready.
 *
 * @see https://vueuse.org/useAsyncState
 * @param promise         The promise / async function to be resolved
 * @param initialState    The initial state, used until the first evaluation finishes
 * @param options
 */
export declare function useAsyncState<
  Data,
  Params extends any[] = any[],
  Shallow extends boolean = true,
>(
  promise: Promise<Data> | ((...args: Params) => Promise<Data>),
  initialState: MaybeRef<Data>,
  options?: UseAsyncStateOptions<Shallow, Data>,
): UseAsyncStateReturn<Data, Params, Shallow>
```
```

## File: `skills/vueuse-functions/references/useAsyncValidator.md`
```markdown
---
category: '@Integrations'
---

# useAsyncValidator

Wrapper for [`async-validator`](https://github.com/yiminghe/async-validator).

## Install

```bash
npm i async-validator@^4
```

## Usage

```ts
import { useAsyncValidator } from '@vueuse/integrations/useAsyncValidator'
```

## Type Declarations

```ts
export type AsyncValidatorError = Error & {
  errors: ValidateError[]
  fields: Record<string, ValidateError[]>
}
export interface UseAsyncValidatorExecuteReturn {
  pass: boolean
  errors: AsyncValidatorError["errors"] | undefined
  errorInfo: AsyncValidatorError | null
  errorFields: AsyncValidatorError["fields"] | undefined
}
export interface UseAsyncValidatorReturn {
  pass: ShallowRef<boolean>
  isFinished: ShallowRef<boolean>
  errors: ComputedRef<AsyncValidatorError["errors"] | undefined>
  errorInfo: ShallowRef<AsyncValidatorError | null>
  errorFields: ComputedRef<AsyncValidatorError["fields"] | undefined>
  execute: () => Promise<UseAsyncValidatorExecuteReturn>
}
export interface UseAsyncValidatorOptions {
  /**
   * @see https://github.com/yiminghe/async-validator#options
   */
  validateOption?: ValidateOption
  /**
   * The validation will be triggered right away for the first time.
   * Only works when `manual` is not set to true.
   *
   * @default true
   */
  immediate?: boolean
  /**
   * If set to true, the validation will not be triggered automatically.
   */
  manual?: boolean
}
/**
 * Wrapper for async-validator.
 *
 * @see https://vueuse.org/useAsyncValidator
 * @see https://github.com/yiminghe/async-validator
 */
export declare function useAsyncValidator(
  value: MaybeRefOrGetter<Record<string, any>>,
  rules: MaybeRefOrGetter<Rules>,
  options?: UseAsyncValidatorOptions,
): UseAsyncValidatorReturn & PromiseLike<UseAsyncValidatorReturn>
```
```

## File: `skills/vueuse-functions/references/useAuth.md`
```markdown
---
category: '@Firebase'
---

# useAuth

Reactive [Firebase Auth](https://firebase.google.com/docs/auth) binding. It provides a reactive `user` and `isAuthenticated` so you
can easily react to changes in the users' authentication status.

## Usage

```vue
<script setup lang="ts">
import { useAuth } from '@vueuse/firebase/useAuth'
import { initializeApp } from 'firebase/app'
import { getAuth, GoogleAuthProvider, signInWithPopup } from 'firebase/auth'

const app = initializeApp({ /* config */ })
const auth = getAuth(app)
const { isAuthenticated, user } = useAuth(auth)

const signIn = () => signInWithPopup(auth, new GoogleAuthProvider())
</script>

<template>
  <pre v-if="isAuthenticated">{{ user }}</pre>
  <div v-else>
    <button @click="signIn">
      Sign In with Google
    </button>
  </div>
</template>
```

## Return Values

| Name              | Type                   | Description                                               |
| ----------------- | ---------------------- | --------------------------------------------------------- |
| `user`            | `Ref<User \| null>`    | The current Firebase user, or `null` if not authenticated |
| `isAuthenticated` | `ComputedRef<boolean>` | Whether a user is currently authenticated                 |

The composable automatically updates when the user's ID token changes (including sign-in, sign-out, and token refresh events) using Firebase's `onIdTokenChanged` listener.

## Type Declarations

```ts
export interface UseFirebaseAuthOptions {
  isAuthenticated: ComputedRef<boolean>
  user: Ref<User | null>
}
/**
 * Reactive Firebase Auth binding
 *
 * @see https://vueuse.org/useAuth
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useAuth(auth: Auth): {
  isAuthenticated: ComputedRef<boolean>
  user: Ref<
    {
      readonly emailVerified: boolean
      readonly isAnonymous: boolean
      readonly metadata: {
        readonly creationTime?: string | undefined
        readonly lastSignInTime?: string | undefined
      }
      readonly providerData: {
        readonly displayName: string | null
        readonly email: string | null
        readonly phoneNumber: string | null
        readonly photoURL: string | null
        readonly providerId: string
        readonly uid: string
      }[]
      readonly refreshToken: string
      readonly tenantId: string | null
      delete: () => Promise<void>
      getIdToken: (forceRefresh?: boolean) => Promise<string>
      getIdTokenResult: (forceRefresh?: boolean) => Promise<IdTokenResult>
      reload: () => Promise<void>
      toJSON: () => object
      readonly displayName: string | null
      readonly email: string | null
      readonly phoneNumber: string | null
      readonly photoURL: string | null
      readonly providerId: string
      readonly uid: string
    } | null,
    | User
    | {
        readonly emailVerified: boolean
        readonly isAnonymous: boolean
        readonly metadata: {
          readonly creationTime?: string | undefined
          readonly lastSignInTime?: string | undefined
        }
        readonly providerData: {
          readonly displayName: string | null
          readonly email: string | null
          readonly phoneNumber: string | null
          readonly photoURL: string | null
          readonly providerId: string
          readonly uid: string
        }[]
        readonly refreshToken: string
        readonly tenantId: string | null
        delete: () => Promise<void>
        getIdToken: (forceRefresh?: boolean) => Promise<string>
        getIdTokenResult: (forceRefresh?: boolean) => Promise<IdTokenResult>
        reload: () => Promise<void>
        toJSON: () => object
        readonly displayName: string | null
        readonly email: string | null
        readonly phoneNumber: string | null
        readonly photoURL: string | null
        readonly providerId: string
        readonly uid: string
      }
    | null
  >
}
```
```

## File: `skills/vueuse-functions/references/useAverage.md`
```markdown
---
category: '@Math'
---

# useAverage

Get the average of an array reactively.

## Usage

```ts
import { useAverage } from '@vueuse/math'

const list = ref([1, 2, 3])
const averageValue = useAverage(list) // Ref<2>
```

```ts
import { useAverage } from '@vueuse/math'

const a = ref(1)
const b = ref(3)

const averageValue = useAverage(a, b) // Ref<2>
```

## Type Declarations

```ts
export declare function useAverage(
  array: MaybeRefOrGetter<MaybeRefOrGetter<number>[]>,
): ComputedRef<number>
export declare function useAverage(
  ...args: MaybeRefOrGetter<number>[]
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useAxios.md`
```markdown
---
category: '@Integrations'
---

# useAxios

Wrapper for [`axios`](https://github.com/axios/axios).

## Install

```bash
npm i axios@^1
```

## Usage

```ts
import { useAxios } from '@vueuse/integrations/useAxios'

const { data, isFinished } = useAxios('/api/posts')
```

### Return Values

| Property           | Type                         | Description                              |
| ------------------ | ---------------------------- | ---------------------------------------- |
| `data`             | `Ref<T>`                     | Response data                            |
| `response`         | `Ref<AxiosResponse>`         | Full axios response                      |
| `error`            | `Ref<unknown>`               | Error if request failed                  |
| `isFinished`       | `Ref<boolean>`               | Request has completed (success or error) |
| `isLoading`        | `Ref<boolean>`               | Request is in progress                   |
| `isAborted`        | `Ref<boolean>`               | Request was aborted                      |
| `abort` / `cancel` | `() => void`                 | Abort the current request                |
| `execute`          | `(url?, config?) => Promise` | Execute/re-execute the request           |

### With Axios Instance

```ts
import { useAxios } from '@vueuse/integrations/useAxios'
import axios from 'axios'

const instance = axios.create({
  baseURL: '/api',
})

const { data, isFinished } = useAxios('/posts', instance)
```

### With Config Options

```ts
import { useAxios } from '@vueuse/integrations/useAxios'
import axios from 'axios'

const instance = axios.create({
  baseURL: '/api',
})

const { data, isFinished } = useAxios('/posts', { method: 'POST' }, instance)
```

### Manual Execution

When you don't pass a `url`, the request won't fire immediately:

```ts
import { useAxios } from '@vueuse/integrations/useAxios'

const { execute } = useAxios()
execute(url)
```

The `execute` function `url` is optional - `url2` will replace `url1`:

```ts
import { useAxios } from '@vueuse/integrations/useAxios'

const { execute } = useAxios(url1, {}, { immediate: false })
execute(url2)
```

The `execute` function can accept config only:

```ts
import { useAxios } from '@vueuse/integrations/useAxios'

const { execute } = useAxios(url1, { method: 'GET' }, { immediate: false })
execute({ params: { key: 1 } })
execute({ params: { key: 2 } })
```

### Awaiting Results

The return value is thenable, so you can await it:

```ts
import { useAxios } from '@vueuse/integrations/useAxios'

const { data, isFinished, error } = await useAxios('/api/posts')
// data is now populated
```

Or await the execute function:

```ts
import { useAxios } from '@vueuse/integrations/useAxios'

const { execute } = useAxios()
const result = await execute(url)
```

### Options

```ts
const { data } = useAxios('/api/posts', config, instance, {
  // Execute immediately (default: true if url provided)
  immediate: true,
  // Use shallowRef for data (default: true)
  shallow: true,
  // Abort previous request on new execute (default: true)
  abortPrevious: true,
  // Reset data before executing (default: false)
  resetOnExecute: false,
  // Initial data value
  initialData: [],
  // Callbacks
  onSuccess: data => console.log('Success:', data),
  onError: error => console.error('Error:', error),
  onFinish: () => console.log('Finished'),
})
```

## Type Declarations

```ts
export interface UseAxiosReturn<
  T,
  R = AxiosResponse<T>,
  _D = any,
  O extends UseAxiosOptions = UseAxiosOptions<T>,
> {
  /**
   * Axios Response
   */
  response: ShallowRef<R | undefined>
  /**
   * Axios response data
   */
  data: O extends UseAxiosOptionsWithInitialData<T>
    ? Ref<T>
    : Ref<T | undefined>
  /**
   * Indicates if the request has finished
   */
  isFinished: Ref<boolean>
  /**
   * Indicates if the request is currently loading
   */
  isLoading: Ref<boolean>
  /**
   * Indicates if the request was canceled
   */
  isAborted: Ref<boolean>
  /**
   * Any errors that may have occurred
   */
  error: ShallowRef<unknown | undefined>
  /**
   * Aborts the current request
   */
  abort: (message?: string | undefined) => void
  /**
   * Alias to `abort`
   */
  cancel: (message?: string | undefined) => void
  /**
   * Alias to `isAborted`
   */
  isCanceled: Ref<boolean>
}
export interface StrictUseAxiosReturn<
  T,
  R,
  D,
  O extends UseAxiosOptions = UseAxiosOptions<T>,
> extends UseAxiosReturn<T, R, D, O> {
  /**
   * Manually call the axios request
   */
  execute: (
    url?: string | AxiosRequestConfig<D>,
    config?: AxiosRequestConfig<D>,
  ) => Promise<StrictUseAxiosReturn<T, R, D, O>>
}
export interface EasyUseAxiosReturn<T, R, D> extends UseAxiosReturn<T, R, D> {
  /**
   * Manually call the axios request
   */
  execute: (
    url: string,
    config?: AxiosRequestConfig<D>,
  ) => Promise<EasyUseAxiosReturn<T, R, D>>
}
export interface UseAxiosOptionsBase<T = any> {
  /**
   * Will automatically run axios request when `useAxios` is used
   *
   */
  immediate?: boolean
  /**
   * Use shallowRef.
   *
   * @default true
   */
  shallow?: boolean
  /**
   * Abort previous request when a new request is made.
   *
   * @default true
   */
  abortPrevious?: boolean
  /**
   * Callback when error is caught.
   */
  onError?: (e: unknown) => void
  /**
   * Callback when success is caught.
   */
  onSuccess?: (data: T) => void
  /**
   * Sets the state to initialState before executing the promise.
   */
  resetOnExecute?: boolean
  /**
   * Callback when request is finished.
   */
  onFinish?: () => void
}
export interface UseAxiosOptionsWithInitialData<
  T,
> extends UseAxiosOptionsBase<T> {
  /**
   * Initial data
   */
  initialData: T
}
export type UseAxiosOptions<T = any> =
  | UseAxiosOptionsBase<T>
  | UseAxiosOptionsWithInitialData<T>
export declare function useAxios<
  T = any,
  R = AxiosResponse<T>,
  D = any,
  O extends UseAxiosOptionsWithInitialData<T> =
    UseAxiosOptionsWithInitialData<T>,
>(
  url: string,
  config?: AxiosRequestConfig<D>,
  options?: O,
): StrictUseAxiosReturn<T, R, D, O> & Promise<StrictUseAxiosReturn<T, R, D, O>>
export declare function useAxios<
  T = any,
  R = AxiosResponse<T>,
  D = any,
  O extends UseAxiosOptionsWithInitialData<T> =
    UseAxiosOptionsWithInitialData<T>,
>(
  url: string,
  instance?: AxiosInstance,
  options?: O,
): StrictUseAxiosReturn<T, R, D, O> & Promise<StrictUseAxiosReturn<T, R, D, O>>
export declare function useAxios<
  T = any,
  R = AxiosResponse<T>,
  D = any,
  O extends UseAxiosOptionsWithInitialData<T> =
    UseAxiosOptionsWithInitialData<T>,
>(
  url: string,
  config: AxiosRequestConfig<D>,
  instance: AxiosInstance,
  options?: O,
): StrictUseAxiosReturn<T, R, D, O> & Promise<StrictUseAxiosReturn<T, R, D, O>>
export declare function useAxios<
  T = any,
  R = AxiosResponse<T>,
  D = any,
  O extends UseAxiosOptionsBase<T> = UseAxiosOptionsBase<T>,
>(
  url: string,
  config?: AxiosRequestConfig<D>,
  options?: O,
): StrictUseAxiosReturn<T, R, D, O> & Promise<StrictUseAxiosReturn<T, R, D, O>>
export declare function useAxios<
  T = any,
  R = AxiosResponse<T>,
  D = any,
  O extends UseAxiosOptionsBase<T> = UseAxiosOptionsBase<T>,
>(
  url: string,
  instance?: AxiosInstance,
  options?: O,
): StrictUseAxiosReturn<T, R, D, O> & Promise<StrictUseAxiosReturn<T, R, D, O>>
export declare function useAxios<
  T = any,
  R = AxiosResponse<T>,
  D = any,
  O extends UseAxiosOptionsBase<T> = UseAxiosOptionsBase<T>,
>(
  url: string,
  config: AxiosRequestConfig<D>,
  instance: AxiosInstance,
  options?: O,
): StrictUseAxiosReturn<T, R, D, O> & Promise<StrictUseAxiosReturn<T, R, D, O>>
export declare function useAxios<T = any, R = AxiosResponse<T>, D = any>(
  config?: AxiosRequestConfig<D>,
): EasyUseAxiosReturn<T, R, D> & Promise<EasyUseAxiosReturn<T, R, D>>
export declare function useAxios<T = any, R = AxiosResponse<T>, D = any>(
  instance?: AxiosInstance,
): EasyUseAxiosReturn<T, R, D> & Promise<EasyUseAxiosReturn<T, R, D>>
export declare function useAxios<T = any, R = AxiosResponse<T>, D = any>(
  config?: AxiosRequestConfig<D>,
  instance?: AxiosInstance,
): EasyUseAxiosReturn<T, R, D> & Promise<EasyUseAxiosReturn<T, R, D>>
```
```

## File: `skills/vueuse-functions/references/useBase64.md`
```markdown
---
category: Utilities
---

# useBase64

Reactive base64 transforming. Supports plain text, buffer, files, canvas, objects, maps, sets and images.

## Usage

```ts
import { useBase64 } from '@vueuse/core'
import { shallowRef } from 'vue'

const text = shallowRef('')

const { base64, promise, execute } = useBase64(text)
```

### Supported Input Types

- `string` - Plain text
- `Blob` - File or blob data
- `ArrayBuffer` - Binary data
- `HTMLCanvasElement` - Canvas element
- `HTMLImageElement` - Image element
- `Object` / `Array` / `Map` / `Set` - Serialized to JSON

### Return Values

| Property  | Description                               |
| --------- | ----------------------------------------- |
| `base64`  | The resulting base64 string               |
| `promise` | The promise of the current transformation |
| `execute` | Manually trigger the transformation       |

### Data URL Format

By default, the output is in Data URL format (e.g., `data:text/plain;base64,...`). Set `dataUrl: false` to get raw base64.

```ts
const { base64 } = useBase64(text, { dataUrl: false })
// Returns raw base64 without the data URL prefix
```

### Canvas and Image Options

When transforming canvas or image elements, you can specify the MIME type and quality.

```ts
const canvas = document.querySelector('canvas')

const { base64 } = useBase64(canvas, {
  type: 'image/jpeg', // MIME type
  quality: 0.8, // Image quality (0-1, for jpeg/webp)
})
```

### Custom Serializer

For objects, arrays, maps and sets, you can provide a custom serializer. Otherwise, the data will be serialized using `JSON.stringify` (maps are converted to objects, sets to arrays).

```ts
const data = shallowRef({ foo: 'bar' })

const { base64 } = useBase64(data, {
  serializer: v => JSON.stringify(v, null, 2),
})
```

## Type Declarations

```ts
export interface UseBase64Options {
  /**
   * Output as Data URL format
   *
   * @default true
   */
  dataUrl?: boolean
}
export interface ToDataURLOptions extends UseBase64Options {
  /**
   * MIME type
   */
  type?: string | undefined
  /**
   * Image quality of jpeg or webp
   */
  quality?: any
}
export interface UseBase64ObjectOptions<T> extends UseBase64Options {
  serializer?: (v: T) => string
}
export interface UseBase64Return {
  base64: ShallowRef<string>
  promise: ShallowRef<Promise<string>>
  execute: () => Promise<string>
}
export declare function useBase64(
  target: MaybeRefOrGetter<string | undefined>,
  options?: UseBase64Options,
): UseBase64Return
export declare function useBase64(
  target: MaybeRefOrGetter<Blob | undefined>,
  options?: UseBase64Options,
): UseBase64Return
export declare function useBase64(
  target: MaybeRefOrGetter<ArrayBuffer | undefined>,
  options?: UseBase64Options,
): UseBase64Return
export declare function useBase64(
  target: MaybeRefOrGetter<HTMLCanvasElement | undefined>,
  options?: ToDataURLOptions,
): UseBase64Return
export declare function useBase64(
  target: MaybeRefOrGetter<HTMLImageElement | undefined>,
  options?: ToDataURLOptions,
): UseBase64Return
export declare function useBase64<T extends Record<string, unknown>>(
  target: MaybeRefOrGetter<T>,
  options?: UseBase64ObjectOptions<T>,
): UseBase64Return
export declare function useBase64<T extends Map<string, unknown>>(
  target: MaybeRefOrGetter<T>,
  options?: UseBase64ObjectOptions<T>,
): UseBase64Return
export declare function useBase64<T extends Set<unknown>>(
  target: MaybeRefOrGetter<T>,
  options?: UseBase64ObjectOptions<T>,
): UseBase64Return
export declare function useBase64<T>(
  target: MaybeRefOrGetter<T[]>,
  options?: UseBase64ObjectOptions<T[]>,
): UseBase64Return
```
```

## File: `skills/vueuse-functions/references/useBattery.md`
```markdown
---
category: Sensors
---

# useBattery

Reactive [Battery Status API](https://developer.mozilla.org/en-US/docs/Web/API/Battery_Status_API), more often referred to as the Battery API, provides information about the system's battery charge level and lets you be notified by events that are sent when the battery level or charging status change. This can be used to adjust your app's resource usage to reduce battery drain when the battery is low, or to save changes before the battery runs out in order to prevent data loss.

## Usage

```ts
import { useBattery } from '@vueuse/core'

const { isSupported, charging, chargingTime, dischargingTime, level } = useBattery()
```

| State           | Type      | Description                                                       |
| --------------- | --------- | ----------------------------------------------------------------- |
| isSupported     | `Boolean` | If the Battery Status API is supported in the current browser.    |
| charging        | `Boolean` | If the device is currently charging.                              |
| chargingTime    | `Number`  | The number of seconds until the device becomes fully charged.     |
| dischargingTime | `Number`  | The number of seconds before the device becomes fully discharged. |
| level           | `Number`  | A number between 0 and 1 representing the current charge level.   |

::: warning Browser Support
The Battery Status API has limited browser support. It is currently only available in Chromium-based browsers. Always check `isSupported` before using the values.
:::

## Use-cases

Our applications normally are not empathetic to battery level, we can make a few adjustments to our applications that will be more friendly to low battery users.

- Trigger a special "dark-mode" battery saver theme settings.
- Stop auto playing videos in news feeds.
- Disable some background workers that are not critical.
- Limit network calls and reduce CPU/Memory consumption.

## Component Usage

```vue
<template>
  <UseBattery v-slot="{ isSupported, charging, level }">
    <div v-if="isSupported">
      <p>Is Charging: {{ charging }}</p>
      <p>Battery Level: {{ (level * 100).toFixed(0) }}%</p>
    </div>
    <div v-else>
      Battery API not supported
    </div>
  </UseBattery>
</template>
```

## Type Declarations

```ts
export interface UseBatteryOptions extends ConfigurableNavigator {}
export interface UseBatteryReturn extends Supportable {
  charging: ShallowRef<boolean>
  chargingTime: ShallowRef<number>
  dischargingTime: ShallowRef<number>
  level: ShallowRef<number>
}
export interface BatteryManager extends EventTarget {
  charging: boolean
  chargingTime: number
  dischargingTime: number
  level: number
}
/**
 * Reactive Battery Status API.
 *
 * @see https://vueuse.org/useBattery
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useBattery(
  options?: UseBatteryOptions,
): UseBatteryReturn
```
```

## File: `skills/vueuse-functions/references/useBluetooth.md`
```markdown
---
category: Browser
---

# useBluetooth

Reactive [Web Bluetooth API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API). Provides the ability to connect and interact with Bluetooth Low Energy peripherals.

The Web Bluetooth API lets websites discover and communicate with devices over the Bluetooth 4 wireless standard using the Generic Attribute Profile (GATT).

N.B. It is currently partially implemented in Android M, Chrome OS, Mac, and Windows 10. For a full overview of browser compatibility please see [Web Bluetooth API Browser Compatibility](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API#browser_compatibility)

N.B. There are a number of caveats to be aware of with the web bluetooth API specification. Please refer to the [Web Bluetooth W3C Draft Report](https://webbluetoothcg.github.io/web-bluetooth/) for numerous caveats around device detection and connection.

N.B. This API is not available in Web Workers (not exposed via WorkerNavigator).

## Usage Default

```vue
<script setup lang="ts">
import { useBluetooth } from '@vueuse/core'

const {
  isSupported,
  isConnected,
  device,
  requestDevice,
  server,
  error,
} = useBluetooth({
  acceptAllDevices: true,
})
</script>

<template>
  <button @click="requestDevice()">
    Request Bluetooth Device
  </button>
  <div v-if="error">
    Error: {{ error }}
  </div>
</template>
```

### Return Values

| Property        | Type                             | Description                                |
| --------------- | -------------------------------- | ------------------------------------------ |
| `isSupported`   | `ComputedRef<boolean>`           | Whether the Web Bluetooth API is supported |
| `isConnected`   | `Ref<boolean>`                   | Whether a device is currently connected    |
| `device`        | `Ref<BluetoothDevice>`           | The connected Bluetooth device             |
| `server`        | `Ref<BluetoothRemoteGATTServer>` | The GATT server for the connected device   |
| `error`         | `Ref<unknown>`                   | Any error that occurred during connection  |
| `requestDevice` | `() => Promise<void>`            | Function to request a Bluetooth device     |

When the device has paired and is connected, you can then work with the server object as you wish.

## Usage Battery Level Example

This sample illustrates the use of the Web Bluetooth API to read battery level and be notified of changes from a nearby Bluetooth Device advertising Battery information with Bluetooth Low Energy.

Here, we use the characteristicvaluechanged event listener to handle reading battery level characteristic value. This event listener will optionally handle upcoming notifications as well.

```vue
<script setup lang="ts">
import { useBluetooth, useEventListener, watchPausable } from '@vueuse/core'

const {
  isSupported,
  isConnected,
  device,
  requestDevice,
  server,
} = useBluetooth({
  acceptAllDevices: true,
  optionalServices: [
    'battery_service',
  ],
})

const batteryPercent = ref<undefined | number>()

const isGettingBatteryLevels = ref(false)

async function getBatteryLevels() {
  isGettingBatteryLevels.value = true

  // Get the battery service:
  const batteryService = await server.getPrimaryService('battery_service')

  // Get the current battery level
  const batteryLevelCharacteristic = await batteryService.getCharacteristic(
    'battery_level',
  )

  // Listen to when characteristic value changes on `characteristicvaluechanged` event:
  useEventListener(batteryLevelCharacteristic, 'characteristicvaluechanged', (event) => {
    batteryPercent.value = event.target.value.getUint8(0)
  }, { passive: true })

  // Convert received buffer to number:
  const batteryLevel = await batteryLevelCharacteristic.readValue()

  batteryPercent.value = await batteryLevel.getUint8(0)
}

const { stop } = watchPausable(isConnected, (newIsConnected) => {
  if (!newIsConnected || !server.value || isGettingBatteryLevels.value)
    return
  // Attempt to get the battery levels of the device:
  getBatteryLevels()
  // We only want to run this on the initial connection, as we will use an event listener to handle updates:
  stop()
})
</script>

<template>
  <button @click="requestDevice()">
    Request Bluetooth Device
  </button>
</template>
```

More samples can be found on [Google Chrome's Web Bluetooth Samples](https://googlechrome.github.io/samples/web-bluetooth/).

## Type Declarations

```ts
export interface UseBluetoothRequestDeviceOptions {
  /**
   *
   * An array of BluetoothScanFilters. This filter consists of an array
   * of BluetoothServiceUUIDs, a name parameter, and a namePrefix parameter.
   *
   */
  filters?: BluetoothLEScanFilter[] | undefined
  /**
   *
   * An array of BluetoothServiceUUIDs.
   *
   * @see https://developer.mozilla.org/en-US/docs/Web/API/BluetoothRemoteGATTService/uuid
   *
   */
  optionalServices?: BluetoothServiceUUID[] | undefined
}
export interface UseBluetoothOptions
  extends UseBluetoothRequestDeviceOptions, ConfigurableNavigator {
  /**
   *
   * A boolean value indicating that the requesting script can accept all Bluetooth
   * devices. The default is false.
   *
   * !! This may result in a bunch of unrelated devices being shown
   * in the chooser and energy being wasted as there are no filters.
   *
   *
   * Use it with caution.
   *
   * @default false
   *
   */
  acceptAllDevices?: boolean
}
export declare function useBluetooth(
  options?: UseBluetoothOptions,
): UseBluetoothReturn
export interface UseBluetoothReturn extends Supportable {
  isConnected: Readonly<ShallowRef<boolean>>
  device: ShallowRef<BluetoothDevice | undefined>
  requestDevice: () => Promise<void>
  server: ShallowRef<BluetoothRemoteGATTServer | undefined>
  error: ShallowRef<unknown | null>
}
```
```

## File: `skills/vueuse-functions/references/useBreakpoints.md`
```markdown
---
category: Browser
---

# useBreakpoints

Reactive viewport breakpoints.

## Usage

```ts
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

const breakpoints = useBreakpoints(breakpointsTailwind)

const smAndLarger = breakpoints.greaterOrEqual('sm') // sm and larger
const largerThanSm = breakpoints.greater('sm') // only larger than sm
const lgAndSmaller = breakpoints.smallerOrEqual('lg') // lg and smaller
const smallerThanLg = breakpoints.smaller('lg') // only smaller than lg
```

```vue
<script setup lang="ts">
import { useBreakpoints } from '@vueuse/core'

const breakpoints = useBreakpoints({
  mobile: 0, // optional
  tablet: 640,
  laptop: 1024,
  desktop: 1280,
})

// Can be 'mobile' or 'tablet' or 'laptop' or 'desktop'
const activeBreakpoint = breakpoints.active()

// true or false
const laptop = breakpoints.between('laptop', 'desktop')
</script>

<template>
  <div :class="activeBreakpoint">
    ...
  </div>
</template>
```

### Shortcut Methods

You can access breakpoints directly as properties on the returned object. These return reactive refs.

```ts
const breakpoints = useBreakpoints({
  tablet: 640,
  laptop: 1024,
})

// Equivalent to breakpoints.greaterOrEqual('tablet') with min-width strategy
const isTablet = breakpoints.tablet
```

### Strategy

The `strategy` option controls how the shortcut properties behave:

- `min-width` (default, mobile-first): `breakpoints.lg` is `true` when viewport is `>= lg`
- `max-width` (desktop-first): `breakpoints.lg` is `true` when viewport is `< xl`

```ts
const breakpoints = useBreakpoints(breakpointsTailwind, {
  strategy: 'max-width', // desktop-first
})
```

### Available Methods

| Method                | Description                                              |
| --------------------- | -------------------------------------------------------- |
| `greaterOrEqual(k)`   | Reactive: viewport width >= breakpoint                   |
| `greater(k)`          | Reactive: viewport width > breakpoint                    |
| `smallerOrEqual(k)`   | Reactive: viewport width <= breakpoint                   |
| `smaller(k)`          | Reactive: viewport width < breakpoint                    |
| `between(a, b)`       | Reactive: viewport width between a and b                 |
| `isGreaterOrEqual(k)` | Non-reactive: returns boolean immediately                |
| `isGreater(k)`        | Non-reactive: returns boolean immediately                |
| `isSmallerOrEqual(k)` | Non-reactive: returns boolean immediately                |
| `isSmaller(k)`        | Non-reactive: returns boolean immediately                |
| `isInBetween(a, b)`   | Non-reactive: returns boolean immediately                |
| `current()`           | Returns computed array of all matching breakpoints       |
| `active()`            | Returns computed string of the current active breakpoint |

#### Server Side Rendering and Nuxt

If you are using `useBreakpoints` with SSR enabled, then you need to specify which screen size you would like to render on the server and before hydration to avoid an hydration mismatch

```ts
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

const breakpoints = useBreakpoints(breakpointsTailwind, {
  ssrWidth: 768 // Will enable SSR mode and render like if the screen was 768px wide
})
```

Alternatively you can set this up globally for your app using [`provideSSRWidth`](../INDEX.md)

## Presets

- Tailwind: `breakpointsTailwind`
- Bootstrap v5: `breakpointsBootstrapV5`
- Vuetify v2: `breakpointsVuetifyV2` (deprecated: `breakpointsVuetify`)
- Vuetify v3: `breakpointsVuetifyV3`
- Ant Design: `breakpointsAntDesign`
- Quasar v2: `breakpointsQuasar`
- Sematic: `breakpointsSematic`
- Master CSS: `breakpointsMasterCss`
- Prime Flex: `breakpointsPrimeFlex`
- ElementUI / ElementPlus: `breakpointsElement`

_Breakpoint presets are deliberately not auto-imported, as they do not start with `use` to have the scope of VueUse. They have to be explicitly imported:_

```js
import { breakpointsTailwind } from '@vueuse/core'
// and so on
```

## Type Declarations

```ts
export * from "./breakpoints"
export type Breakpoints<K extends string = string> = Record<
  K,
  MaybeRefOrGetter<number | string>
>
export interface UseBreakpointsOptions extends ConfigurableWindow {
  /**
   * The query strategy to use for the generated shortcut methods like `.lg`
   *
   * 'min-width' - .lg will be true when the viewport is greater than or equal to the lg breakpoint (mobile-first)
   * 'max-width' - .lg will be true when the viewport is smaller than the xl breakpoint (desktop-first)
   *
   * @default "min-width"
   */
  strategy?: "min-width" | "max-width"
  ssrWidth?: number
}
export type UseBreakpointReturn<K extends string = string> = Record<
  K,
  ComputedRef<boolean>
> & {
  greaterOrEqual: (k: MaybeRefOrGetter<K>) => ComputedRef<boolean>
  smallerOrEqual: (k: MaybeRefOrGetter<K>) => ComputedRef<boolean>
  greater: (k: MaybeRefOrGetter<K>) => ComputedRef<boolean>
  smaller: (k: MaybeRefOrGetter<K>) => ComputedRef<boolean>
  between: (
    a: MaybeRefOrGetter<K>,
    b: MaybeRefOrGetter<K>,
  ) => ComputedRef<boolean>
  isGreater: (k: MaybeRefOrGetter<K>) => boolean
  isGreaterOrEqual: (k: MaybeRefOrGetter<K>) => boolean
  isSmaller: (k: MaybeRefOrGetter<K>) => boolean
  isSmallerOrEqual: (k: MaybeRefOrGetter<K>) => boolean
  isInBetween: (a: MaybeRefOrGetter<K>, b: MaybeRefOrGetter<K>) => boolean
  current: () => ComputedRef<K[]>
  active: () => ComputedRef<K | "">
}
/**
 * Reactively viewport breakpoints
 *
 * @see https://vueuse.org/useBreakpoints
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useBreakpoints<K extends string>(
  breakpoints: Breakpoints<K>,
  options?: UseBreakpointsOptions,
): UseBreakpointReturn<K>
```
```

## File: `skills/vueuse-functions/references/useBroadcastChannel.md`
```markdown
---
category: Browser
---

# useBroadcastChannel

Reactive [BroadcastChannel API](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel).

Closes a broadcast channel automatically component unmounted.

## Usage

The BroadcastChannel interface represents a named channel that any browsing
context of a given origin can subscribe to. It allows communication between
different documents (in different windows, tabs, frames, or iframes) of the
same origin.

Messages are broadcasted via a message event fired at all BroadcastChannel
objects listening to the channel.

```ts
import { useBroadcastChannel } from '@vueuse/core'
import { shallowRef } from 'vue'

const {
  isSupported,
  channel,
  post,
  close,
  error,
  isClosed,
} = useBroadcastChannel({ name: 'vueuse-demo-channel' })

const message = shallowRef('')

message.value = 'Hello, VueUse World!'

// Post the message to the broadcast channel:
post(message.value)

// Option to close the channel if you wish:
close()
```

## Type Declarations

```ts
export interface UseBroadcastChannelOptions extends ConfigurableWindow {
  /**
   * The name of the channel.
   */
  name: string
}
/**
 * Reactive BroadcastChannel
 *
 * @see https://vueuse.org/useBroadcastChannel
 * @see https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel
 * @param options
 *
 */
export declare function useBroadcastChannel<D, P>(
  options: UseBroadcastChannelOptions,
): UseBroadcastChannelReturn<D, P>
export interface UseBroadcastChannelReturn<D, P> extends Supportable {
  channel: Ref<BroadcastChannel | undefined>
  data: Ref<D>
  post: (data: P) => void
  close: () => void
  error: ShallowRef<Event | null>
  isClosed: ShallowRef<boolean>
}
```
```

## File: `skills/vueuse-functions/references/useBrowserLocation.md`
```markdown
---
category: Browser
---

# useBrowserLocation

Reactive browser location

> NOTE: If you're using Vue Router, use [`useRoute`](https://router.vuejs.org/guide/advanced/composition-api.html) provided by Vue Router instead.

## Usage

```ts
import { useBrowserLocation } from '@vueuse/core'

const location = useBrowserLocation()
```

## Component Usage

```vue
<UseBrowserLocation v-slot="location">
  Browser Location: {{ location }}
</UseBrowserLocation>
```

## Type Declarations

```ts
export interface UseBrowserLocationOptions extends ConfigurableWindow {}
export interface BrowserLocationState {
  readonly trigger: string
  readonly state?: any
  readonly length?: number
  readonly origin?: string
  hash?: string
  host?: string
  hostname?: string
  href?: string
  pathname?: string
  port?: string
  protocol?: string
  search?: string
}
export type UseBrowserLocationReturn = Ref<BrowserLocationState>
/**
 * Reactive browser location.
 *
 * @see https://vueuse.org/useBrowserLocation
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useBrowserLocation(
  options?: UseBrowserLocationOptions,
): UseBrowserLocationReturn
```
```

## File: `skills/vueuse-functions/references/useCached.md`
```markdown
---
category: Utilities
---

# useCached

Cache a ref with a custom comparator.

## Usage

```ts
import { useCached } from '@vueuse/core'
import { shallowRef } from 'vue'

interface Data {
  value: number
  extra: number
}

const source = shallowRef<Data>({ value: 42, extra: 0 })
const cached = useCached(source, (a, b) => a.value === b.value)

source.value = {
  value: 42,
  extra: 1,
}

console.log(cached.value) // { value: 42, extra: 0 }

source.value = {
  value: 43,
  extra: 1,
}

console.log(cached.value) // { value: 43, extra: 1 }
```

## Type Declarations

```ts
export interface UseCachedOptions<D extends boolean = true>
  extends ConfigurableDeepRefs<D>, WatchOptions {}
export declare function useCached<T, D extends boolean = true>(
  refValue: Ref<T>,
  comparator?: (a: T, b: T) => boolean,
  options?: UseCachedOptions<D>,
): UseCachedReturn<T, D>
export type UseCachedReturn<
  T = any,
  D extends boolean = true,
> = ShallowOrDeepRef<T, D>
```
```

## File: `skills/vueuse-functions/references/useCeil.md`
```markdown
---
category: '@Math'
---

# useCeil

Reactive `Math.ceil`

## Usage

```ts
import { useCeil } from '@vueuse/math'

const value = ref(0.95)
const result = useCeil(value) // 1
```

## Type Declarations

```ts
/**
 * Reactive `Math.ceil`.
 *
 * @see https://vueuse.org/useCeil
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useCeil(
  value: MaybeRefOrGetter<number>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useChangeCase.md`
```markdown
---
category: '@Integrations'
---

# useChangeCase

Reactive wrapper for [`change-case`](https://github.com/blakeembrey/change-case).

Subsitutes `useCamelCase`, `usePascalCase`, `useSnakeCase`, `useSentenceCase`, `useCapitalize`, etc.

## Install

```bash
npm i change-case@^5
```

## Usage

```ts
import { useChangeCase } from '@vueuse/integrations/useChangeCase'

// `changeCase` will be a computed
const changeCase = useChangeCase('hello world', 'camelCase')
changeCase.value // helloWorld
changeCase.value = 'vue use'
changeCase.value // vueUse
// Supported methods
// export {
//   camelCase,
//   capitalCase,
//   constantCase,
//   dotCase,
//   headerCase,
//   noCase,
//   paramCase,
//   pascalCase,
//   pathCase,
//   sentenceCase,
//   snakeCase,
// } from 'change-case'
```

or passing a `ref` to it, the returned `computed` will change along with the source ref's changes.

Can be passed into `options` for customization

```ts
import { useChangeCase } from '@vueuse/integrations/useChangeCase'
import { shallowRef } from 'vue'

const input = shallowRef('helloWorld')
const changeCase = useChangeCase(input, 'camelCase', {
  delimiter: '-',
})
changeCase.value // hello-World
input.value = 'vue use'
changeCase.value // vue-Use
```

## Type Declarations

```ts
type EndsWithCase<T> = T extends `${infer _}Case` ? T : never
type FilterKeys<T> = {
  [K in keyof T as K extends string ? K : never]: EndsWithCase<K>
}
type ChangeCaseKeys = FilterKeys<typeof changeCase>
export type ChangeCaseType = ChangeCaseKeys[keyof ChangeCaseKeys]
export declare function useChangeCase(
  input: MaybeRef<string>,
  type: MaybeRefOrGetter<ChangeCaseType>,
  options?: MaybeRefOrGetter<Options> | undefined,
): WritableComputedRef<string>
export declare function useChangeCase(
  input: MaybeRefOrGetter<string>,
  type: MaybeRefOrGetter<ChangeCaseType>,
  options?: MaybeRefOrGetter<Options> | undefined,
): ComputedRef<string>
```
```

## File: `skills/vueuse-functions/references/useClamp.md`
```markdown
---
category: '@Math'
---

# useClamp

Reactively clamp a value between two other values.

## Usage

```ts
import { useClamp } from '@vueuse/math'

const min = shallowRef(0)
const max = shallowRef(10)
const value = useClamp(0, min, max)
```

### Writable Ref

When you pass a mutable `ref`, the returned value is a **writable computed** that clamps values when setting:

```ts
import { useClamp } from '@vueuse/math'

const number = shallowRef(0)
const clamped = useClamp(number, 0, 10)

clamped.value = 15 // clamped.value will be 10
clamped.value = -5 // clamped.value will be 0
```

### Read-only Mode

When you pass a getter function or readonly ref, the returned value is a read-only computed:

```ts
import { useClamp } from '@vueuse/math'

const value = ref(5)
const clamped = useClamp(() => value.value * 2, 0, 10)

// clamped.value is computed from the getter
```

### Reactive Bounds

All arguments (value, min, max) can be reactive:

```ts
import { useClamp } from '@vueuse/math'

const value = shallowRef(5)
const min = shallowRef(0)
const max = shallowRef(10)

const clamped = useClamp(value, min, max)

max.value = 3 // clamped.value automatically becomes 3
```

## Type Declarations

```ts
/**
 * Reactively clamp a value between two other values.
 *
 * @see https://vueuse.org/useClamp
 * @param value number
 * @param min
 * @param max
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useClamp(
  value: ReadonlyRefOrGetter<number>,
  min: MaybeRefOrGetter<number>,
  max: MaybeRefOrGetter<number>,
): ComputedRef<number>
export declare function useClamp(
  value: MaybeRefOrGetter<number>,
  min: MaybeRefOrGetter<number>,
  max: MaybeRefOrGetter<number>,
): Ref<number>
```
```

## File: `skills/vueuse-functions/references/useClipboard.md`
```markdown
---
category: Browser
---

# useClipboard

Reactive [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API). Provides the ability to respond to clipboard commands (cut, copy, and paste) as well as to asynchronously read from and write to the system clipboard. Access to the contents of the clipboard is gated behind the [Permissions API](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API). Without user permission, reading or altering the clipboard contents is not permitted.

<CourseLink href="https://vueschool.io/lessons/reactive-browser-wrappers-in-vueuse-useclipboard?friend=vueuse">Learn how to reactively save text to the clipboard with this FREE video lesson from Vue School!</CourseLink>

## Usage

```vue
<script setup lang="ts">
import { useClipboard } from '@vueuse/core'

const source = ref('Hello')
const { text, copy, copied, isSupported } = useClipboard({ source })
</script>

<template>
  <div v-if="isSupported">
    <button @click="copy(source)">
      <!-- by default, `copied` will be reset in 1.5s -->
      <span v-if="!copied">Copy</span>
      <span v-else>Copied!</span>
    </button>
    <p>Current copied: <code>{{ text || 'none' }}</code></p>
  </div>
  <p v-else>
    Your browser does not support Clipboard API
  </p>
</template>
```

### Options

| Option         | Type                       | Default | Description                                                       |
| -------------- | -------------------------- | ------- | ----------------------------------------------------------------- |
| `source`       | `MaybeRefOrGetter<string>` | —       | Default content to copy when `copy()` is called without arguments |
| `read`         | `boolean`                  | `false` | Enable reading clipboard content on copy/cut events               |
| `copiedDuring` | `number`                   | `1500`  | Milliseconds before `copied` resets to `false`                    |
| `legacy`       | `boolean`                  | `false` | Fallback to `document.execCommand` if Clipboard API unavailable   |

### Return Values

| Property      | Type                               | Description                                       |
| ------------- | ---------------------------------- | ------------------------------------------------- |
| `isSupported` | `ComputedRef<boolean>`             | Whether clipboard is supported (native or legacy) |
| `text`        | `Ref<string>`                      | Current clipboard content (when `read: true`)     |
| `copied`      | `Ref<boolean>`                     | `true` after successful copy, auto-resets         |
| `copy`        | `(text?: string) => Promise<void>` | Copy text to clipboard                            |

### Legacy Mode

Set `legacy: true` to keep the ability to copy if [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) is not available. It will handle copy with [execCommand](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand) as fallback.

```ts
const { copy, isSupported } = useClipboard({ legacy: true })
```

## Component Usage

```vue
<template>
  <UseClipboard v-slot="{ copy, copied }" source="copy me">
    <button @click="copy()">
      {{ copied ? 'Copied' : 'Copy' }}
    </button>
  </UseClipboard>
</template>
```

## Type Declarations

```ts
export interface UseClipboardOptions<Source> extends ConfigurableNavigator {
  /**
   * Enabled reading for clipboard
   *
   * @default false
   */
  read?: boolean
  /**
   * Copy source
   */
  source?: Source
  /**
   * Milliseconds to reset state of `copied` ref
   *
   * @default 1500
   */
  copiedDuring?: number
  /**
   * Whether fallback to document.execCommand('copy') if clipboard is undefined.
   *
   * @default false
   */
  legacy?: boolean
}
export interface UseClipboardReturn<Optional> extends Supportable {
  text: Readonly<ShallowRef<string>>
  copied: Readonly<ShallowRef<boolean>>
  copy: Optional extends true
    ? (text?: string) => Promise<void>
    : (text: string) => Promise<void>
}
/**
 * Reactive Clipboard API.
 *
 * @see https://vueuse.org/useClipboard
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useClipboard(
  options?: UseClipboardOptions<undefined>,
): UseClipboardReturn<false>
export declare function useClipboard(
  options: UseClipboardOptions<MaybeRefOrGetter<string>>,
): UseClipboardReturn<true>
```
```

## File: `skills/vueuse-functions/references/useClipboardItems.md`
```markdown
---
category: Browser
related:
  - useClipboard
---

# useClipboardItems

Reactive [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API). Provides the ability to respond to clipboard commands (cut, copy, and paste) as well as to asynchronously read from and write to the system clipboard. Access to the contents of the clipboard is gated behind the [Permissions API](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API). Without user permission, reading or altering the clipboard contents is not permitted.

## Difference from `useClipboard`

`useClipboard` is a "text-only" function, while `useClipboardItems` is a [ClipboardItem](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem) based function. You can use `useClipboardItems` to copy any content supported by [ClipboardItem](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem).

## Usage

```vue
<script setup lang="ts">
import { useClipboardItems } from '@vueuse/core'

const mime = 'text/plain'
const source = ref([
  new ClipboardItem({
    [mime]: new Blob(['plain text'], { type: mime }),
  })
])

const { content, copy, copied, isSupported } = useClipboardItems({ source })
</script>

<template>
  <div v-if="isSupported">
    <button @click="copy(source)">
      <!-- by default, `copied` will be reset in 1.5s -->
      <span v-if="!copied">Copy</span>
      <span v-else>Copied!</span>
    </button>
    <p>
      Current copied: <code>{{ content || 'none' }}</code>
    </p>
  </div>
  <p v-else>
    Your browser does not support Clipboard API
  </p>
</template>
```

## Type Declarations

```ts
export interface UseClipboardItemsOptions<
  Source,
> extends ConfigurableNavigator {
  /**
   * Enabled reading for clipboard
   *
   * @default false
   */
  read?: boolean
  /**
   * Copy source
   */
  source?: Source
  /**
   * Milliseconds to reset state of `copied` ref
   *
   * @default 1500
   */
  copiedDuring?: number
}
export interface UseClipboardItemsReturn<Optional> extends Supportable {
  content: Readonly<Ref<ClipboardItems>>
  copied: Readonly<ShallowRef<boolean>>
  copy: Optional extends true
    ? (content?: ClipboardItems) => Promise<void>
    : (text: ClipboardItems) => Promise<void>
  read: () => void
}
/**
 * Reactive Clipboard API.
 *
 * @see https://vueuse.org/useClipboardItems
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useClipboardItems(
  options?: UseClipboardItemsOptions<undefined>,
): UseClipboardItemsReturn<false>
export declare function useClipboardItems(
  options: UseClipboardItemsOptions<MaybeRefOrGetter<ClipboardItems>>,
): UseClipboardItemsReturn<true>
```
```

## File: `skills/vueuse-functions/references/useCloned.md`
```markdown
---
category: Utilities
---

# useCloned

Reactive clone of a ref. By default, it use `JSON.parse(JSON.stringify())` to do the clone.

## Usage

```ts
import { useCloned } from '@vueuse/core'

const original = ref({ key: 'value' })

const { cloned } = useCloned(original)

original.value.key = 'some new value'

console.log(cloned.value.key) // 'value'
```

## Manual cloning

```ts
import { useCloned } from '@vueuse/core'

const original = ref({ key: 'value' })

const { cloned, sync } = useCloned(original, { manual: true })

original.value.key = 'manual'

console.log(cloned.value.key) // 'value'

sync()

console.log(cloned.value.key)// 'manual'
```

## Custom Clone Function

Using [`klona`](https://www.npmjs.com/package/klona) for example:

```ts
import { useCloned } from '@vueuse/core'
import { klona } from 'klona'

const original = ref({ key: 'value' })

const { cloned, isModified, sync } = useCloned(original, { clone: klona })
```

## Type Declarations

```ts
export interface UseClonedOptions<T = any> extends WatchOptions {
  /**
   * Custom clone function.
   *
   * By default, it use `JSON.parse(JSON.stringify(value))` to clone.
   */
  clone?: (source: T) => T
  /**
   * Manually sync the ref
   *
   * @default false
   */
  manual?: boolean
}
export interface UseClonedReturn<T> {
  /**
   * Cloned ref
   */
  cloned: Ref<T>
  /**
   * Ref indicates whether the cloned data is modified
   */
  isModified: Ref<boolean>
  /**
   * Sync cloned data with source manually
   */
  sync: () => void
}
export type CloneFn<F, T = F> = (x: F) => T
export declare function cloneFnJSON<T>(source: T): T
export declare function useCloned<T>(
  source: MaybeRefOrGetter<T>,
  options?: UseClonedOptions,
): UseClonedReturn<T>
```
```

## File: `skills/vueuse-functions/references/useColorMode.md`
```markdown
---
category: Browser
related:
  - useDark
  - usePreferredDark
  - useStorage
---

# useColorMode

Reactive color mode (dark / light / customs) with auto data persistence.

## Basic Usage

```ts
import { useColorMode } from '@vueuse/core'

const mode = useColorMode() // Ref<'dark' | 'light'>
```

By default, it will match with users' browser preference using `usePreferredDark` (a.k.a `auto` mode). When reading the ref, it will by default return the current color mode (`dark`, `light` or your custom modes). The `auto` mode can be included in the returned modes by enabling the `emitAuto` option. When writing to the ref, it will trigger DOM updates and persist the color mode to local storage (or your custom storage). You can pass `auto` to set back to auto mode.

```ts
import { useColorMode } from '@vueuse/core'

const mode = useColorMode()
// ---cut---
mode.value // 'dark' | 'light'

mode.value = 'dark' // change to dark mode and persist

mode.value = 'auto' // change to auto mode
```

## Config

```ts
import { useColorMode } from '@vueuse/core'

const mode = useColorMode({
  attribute: 'theme',
  modes: {
    // custom colors
    dim: 'dim',
    cafe: 'cafe',
  },
}) // Ref<'dark' | 'light' | 'dim' | 'cafe'>
```

## Advanced Usage

You can also explicit access to the system preference and storaged user override mode.

```ts
import { useColorMode } from '@vueuse/core'

const { system, store } = useColorMode()

system.value // 'dark' | 'light'
store.value // 'dark' | 'light' | 'auto'

const myColorMode = computed(() => store.value === 'auto' ? system.value : store.value)
```

## Component Usage

```vue
<template>
  <UseColorMode v-slot="color">
    <button @click="color.mode = color.mode === 'dark' ? 'light' : 'dark'">
      Mode {{ color.mode }}
    </button>
  </UseColorMode>
</template>
```

## Type Declarations

```ts
export type BasicColorMode = "light" | "dark"
export type BasicColorSchema = BasicColorMode | "auto"
export interface UseColorModeOptions<
  T extends string = BasicColorMode,
> extends UseStorageOptions<T | BasicColorMode> {
  /**
   * CSS Selector for the target element applying to
   *
   * @default 'html'
   */
  selector?: string | MaybeElementRef
  /**
   * HTML attribute applying the target element
   *
   * @default 'class'
   */
  attribute?: string
  /**
   * The initial color mode
   *
   * @default 'auto'
   */
  initialValue?: MaybeRefOrGetter<T | BasicColorSchema>
  /**
   * Prefix when adding value to the attribute
   */
  modes?: Partial<Record<T | BasicColorSchema, string>>
  /**
   * A custom handler for handle the updates.
   * When specified, the default behavior will be overridden.
   *
   * @default undefined
   */
  onChanged?: (
    mode: T | BasicColorMode,
    defaultHandler: (mode: T | BasicColorMode) => void,
  ) => void
  /**
   * Custom storage ref
   *
   * When provided, `useStorage` will be skipped
   */
  storageRef?: Ref<T | BasicColorSchema>
  /**
   * Key to persist the data into localStorage/sessionStorage.
   *
   * Pass `null` to disable persistence
   *
   * @default 'vueuse-color-scheme'
   */
  storageKey?: string | null
  /**
   * Storage object, can be localStorage or sessionStorage
   *
   * @default localStorage
   */
  storage?: StorageLike
  /**
   * Emit `auto` mode from state
   *
   * When set to `true`, preferred mode won't be translated into `light` or `dark`.
   * This is useful when the fact that `auto` mode was selected needs to be known.
   *
   * @default undefined
   * @deprecated use `store.value` when `auto` mode needs to be known
   * @see https://vueuse.org/core/useColorMode/#advanced-usage
   */
  emitAuto?: boolean
  /**
   * Disable transition on switch
   *
   * @see https://paco.me/writing/disable-theme-transitions
   * @default true
   */
  disableTransition?: boolean
}
export type UseColorModeReturn<T extends string = BasicColorMode> = Ref<
  T | BasicColorSchema
> & {
  store: Ref<T | BasicColorSchema>
  system: ComputedRef<BasicColorMode>
  state: ComputedRef<T | BasicColorMode>
}
/**
 * Reactive color mode with auto data persistence.
 *
 * @see https://vueuse.org/useColorMode
 * @param options
 */
export declare function useColorMode<T extends string = BasicColorMode>(
  options?: UseColorModeOptions<T>,
): UseColorModeReturn<T>
```
```

## File: `skills/vueuse-functions/references/useConfirmDialog.md`
```markdown
---
category: Utilities
---

# useConfirmDialog

Creates event hooks to support modals and confirmation dialog chains.

Functions can be used on the template, and hooks are a handy skeleton for the business logic of modals dialog or other actions that require user confirmation.

## Functions and hooks

- `reveal()` - triggers `onReveal` hook and sets `revealed.value` to `true`. Returns promise that resolves by `confirm()` or `cancel()`.
- `confirm()` - sets `isRevealed.value` to `false` and triggers `onConfirm` hook.
- `cancel()` - sets `isRevealed.value` to `false` and triggers `onCancel` hook.

## Basic Usage

### Using hooks

```vue
<script setup lang="ts">
import { useConfirmDialog } from '@vueuse/core'

const { isRevealed, reveal, confirm, cancel, onReveal, onConfirm, onCancel }
  = useConfirmDialog()
</script>

<template>
  <button @click="reveal">
    Reveal Modal
  </button>

  <teleport to="body">
    <div v-if="isRevealed" class="modal-bg">
      <div class="modal">
        <h2>Confirm?</h2>
        <button @click="confirm">
          Yes
        </button>
        <button @click="cancel">
          Cancel
        </button>
      </div>
    </div>
  </teleport>
</template>
```

### Promise

If you prefer working with promises:

```vue
<script setup lang="ts">
import { useConfirmDialog } from '@vueuse/core'

const {
  isRevealed,
  reveal,
  confirm,
  cancel,
} = useConfirmDialog()

async function openDialog() {
  const { data, isCanceled } = await reveal()
  if (!isCanceled)
    console.log(data)
}
</script>

<template>
  <button @click="openDialog">
    Show Modal
  </button>

  <teleport to="body">
    <div v-if="isRevealed" class="modal-layout">
      <div class="modal">
        <h2>Confirm?</h2>
        <button @click="confirm(true)">
          Yes
        </button>
        <button @click="confirm(false)">
          No
        </button>
      </div>
    </div>
  </teleport>
</template>
```

## Type Declarations

```ts
export type UseConfirmDialogRevealResult<C, D> =
  | {
      data?: C
      isCanceled: false
    }
  | {
      data?: D
      isCanceled: true
    }
export interface UseConfirmDialogReturn<RevealData, ConfirmData, CancelData> {
  /**
   * Revealing state
   */
  isRevealed: ComputedRef<boolean>
  /**
   * Opens the dialog.
   * Create promise and return it. Triggers `onReveal` hook.
   */
  reveal: (
    data?: RevealData,
  ) => Promise<UseConfirmDialogRevealResult<ConfirmData, CancelData>>
  /**
   * Confirms and closes the dialog. Triggers a callback inside `onConfirm` hook.
   * Resolves promise from `reveal()` with `data` and `isCanceled` ref with `false` value.
   * Can accept any data and to pass it to `onConfirm` hook.
   */
  confirm: (data?: ConfirmData) => void
  /**
   * Cancels and closes the dialog. Triggers a callback inside `onCancel` hook.
   * Resolves promise from `reveal()` with `data` and `isCanceled` ref with `true` value.
   * Can accept any data and to pass it to `onCancel` hook.
   */
  cancel: (data?: CancelData) => void
  /**
   * Event Hook to be triggered right before dialog creating.
   */
  onReveal: EventHookOn<RevealData>
  /**
   * Event Hook to be called on `confirm()`.
   * Gets data object from `confirm` function.
   */
  onConfirm: EventHookOn<ConfirmData>
  /**
   * Event Hook to be called on `cancel()`.
   * Gets data object from `cancel` function.
   */
  onCancel: EventHookOn<CancelData>
}
/**
 * Hooks for creating confirm dialogs. Useful for modal windows, popups and logins.
 *
 * @see https://vueuse.org/useConfirmDialog/
 * @param revealed `boolean` `ref` that handles a modal window
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useConfirmDialog<
  RevealData = any,
  ConfirmData = any,
  CancelData = any,
>(
  revealed?: ShallowRef<boolean>,
): UseConfirmDialogReturn<RevealData, ConfirmData, CancelData>
```
```

## File: `skills/vueuse-functions/references/useCookies.md`
```markdown
---
category: '@Integrations'
---

# useCookies

Wrapper for [`universal-cookie`](https://www.npmjs.com/package/universal-cookie).

::: tip
When using with Nuxt 3, this functions will **NOT** be auto imported in favor of Nuxt's built-in [`useCookie()`](https://v3.nuxtjs.org/api/composables/use-cookie). Use explicit import if you want to use the function from VueUse.
:::

## Install

```bash
npm i universal-cookie@^7
```

## Usage

### Common usage

```vue
<script setup lang="ts">
import { useCookies } from '@vueuse/integrations/useCookies'

const cookies = useCookies(['locale'])
</script>

<template>
  <div>
    <strong>locale</strong>: {{ cookies.get('locale') }}
    <hr>
    <pre>{{ cookies.getAll() }}</pre>
    <button @click="cookies.set('locale', 'ru-RU')">
      Russian
    </button>
    <button @click="cookies.set('locale', 'en-US')">
      English
    </button>
  </div>
</template>
```

## Options

Access and modify cookies using vue composition-api.

> By default, you should use it inside `setup()`, but this function also works anywhere else.

```ts
import { useCookies } from '@vueuse/integrations/useCookies'
// ---cut---
const {
  get,
  getAll,
  set,
  remove,
  addChangeListener,
  removeChangeListener
} = useCookies(['cookie-name'], {
  doNotParse: false,
  autoUpdateDependencies: false
})
```

### `dependencies` (optional)

Let you optionally specify a list of cookie names your component depend on or that should trigger a re-render. If unspecified, it will render on every cookie change.

### `options` (optional)

- `doNotParse` (boolean = false): do not convert the cookie into an object no matter what. **Passed as default value to `get`/`getAll` methods.**
- `autoUpdateDependencies` (boolean = false): automatically add cookie names ever provided to `get` method. If **true** then you don't need to care about provided `dependencies`.

### `cookies` (optional)

Let you provide a `universal-cookie` instance (creates a new instance by default)

> Info about methods available in the [universal-cookie api docs](https://www.npmjs.com/package/universal-cookie#api---cookies-class)

## `createCookies([req])`

Create a `universal-cookie` instance using request (default is window.document.cookie) and returns `useCookies` function with provided universal-cookie instance

- req (object): Node's [http.IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage) request object

## Type Declarations

```ts
/**
 * Creates a new {@link useCookies} function
 * @param req - incoming http request (for SSR)
 * @see https://github.com/reactivestack/cookies/tree/master/packages/universal-cookie universal-cookie
 * @description Creates universal-cookie instance using request (default is window.document.cookie) and returns {@link useCookies} function with provided universal-cookie instance
 */
export declare function createCookies(req?: IncomingMessage): (
  dependencies?: string[] | null,
  {
    doNotParse,
    autoUpdateDependencies,
  }?: {
    doNotParse?: boolean | undefined
    autoUpdateDependencies?: boolean | undefined
  },
) => {
  /**
   * Reactive get cookie by name. If **autoUpdateDependencies = true** then it will update watching dependencies
   */
  get: <T = any>(name: string, options?: CookieGetOptions | undefined) => T
  /**
   * Reactive get all cookies
   */
  getAll: <T = any>(options?: CookieGetOptions | undefined) => T
  set: (
    name: string,
    value: any,
    options?: CookieSetOptions | undefined,
  ) => void
  remove: (name: string, options?: CookieSetOptions | undefined) => void
  addChangeListener: (callback: CookieChangeListener) => void
  removeChangeListener: (callback: CookieChangeListener) => void
}
/**
 * Reactive methods to work with cookies (use {@link createCookies} method instead if you are using SSR)
 * @param dependencies - array of watching cookie's names. Pass empty array if don't want to watch cookies changes.
 * @param options
 * @param options.doNotParse - don't try parse value as JSON
 * @param options.autoUpdateDependencies - automatically update watching dependencies
 * @param cookies - universal-cookie instance
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useCookies(
  dependencies?: string[] | null,
  {
    doNotParse,
    autoUpdateDependencies,
  }?: {
    doNotParse?: boolean | undefined
    autoUpdateDependencies?: boolean | undefined
  },
  cookies?: Cookie,
): {
  /**
   * Reactive get cookie by name. If **autoUpdateDependencies = true** then it will update watching dependencies
   */
  get: <T = any>(name: string, options?: CookieGetOptions | undefined) => T
  /**
   * Reactive get all cookies
   */
  getAll: <T = any>(options?: CookieGetOptions | undefined) => T
  set: (
    name: string,
    value: any,
    options?: CookieSetOptions | undefined,
  ) => void
  remove: (name: string, options?: CookieSetOptions | undefined) => void
  addChangeListener: (callback: CookieChangeListener) => void
  removeChangeListener: (callback: CookieChangeListener) => void
}
```
```

## File: `skills/vueuse-functions/references/useCountdown.md`
```markdown
---
category: Time
---

# useCountdown

Reactive countdown timer in seconds.

## Usage

```ts
import { useCountdown } from '@vueuse/core'

const countdownSeconds = 5
const { remaining, start, stop, pause, resume } = useCountdown(countdownSeconds, {
  onComplete() {

  },
  onTick() {

  }
})
```

You can use a `ref` to change the initial countdown.
`start()` and `resume()` also accept a new countdown value for the next countdown.

```ts
import { useCountdown } from '@vueuse/core'
import { shallowRef } from 'vue'

const countdown = shallowRef(5)
const { start, reset } = useCountdown(countdown, {
})

// change the countdown value
countdown.value = 10

// start a new countdown with 2 seconds
start(2)

// reset the countdown to 4, but do not start it
reset(4)

// start the countdown with the current value of `countdown`
start()
```

## Type Declarations

```ts
export interface UseCountdownOptions extends ConfigurableScheduler {
  /**
   *  Interval for the countdown in milliseconds. Default is 1000ms.
   *
   * @deprecated Please use `scheduler` option instead
   */
  interval?: MaybeRefOrGetter<number>
  /**
   * Callback function called when the countdown reaches 0.
   */
  onComplete?: () => void
  /**
   * Callback function called on each tick of the countdown.
   */
  onTick?: () => void
  /**
   * Start the countdown immediately
   *
   * @deprecated Please use `scheduler` option instead
   * @default false
   */
  immediate?: boolean
}
export interface UseCountdownReturn extends Pausable {
  /**
   * Current countdown value.
   */
  remaining: ShallowRef<number>
  /**
   * Resets the countdown and repeatsLeft to their initial values.
   */
  reset: (countdown?: MaybeRefOrGetter<number>) => void
  /**
   * Stops the countdown and resets its state.
   */
  stop: () => void
  /**
   * Reset the countdown and start it again.
   */
  start: (countdown?: MaybeRefOrGetter<number>) => void
}
/**
 * Reactive countdown timer in seconds.
 *
 * @param initialCountdown
 * @param options
 *
 * @see https://vueuse.org/useCountdown
 */
export declare function useCountdown(
  initialCountdown: MaybeRefOrGetter<number>,
  options?: UseCountdownOptions,
): UseCountdownReturn
```
```

## File: `skills/vueuse-functions/references/useCounter.md`
```markdown
---
category: Utilities
---

# useCounter

Basic counter with utility functions.

## Basic Usage

```ts
import { useCounter } from '@vueuse/core'

const { count, inc, dec, set, reset } = useCounter()
```

## Usage with options

```ts
import { useCounter } from '@vueuse/core'

const { count, inc, dec, set, reset } = useCounter(1, { min: 0, max: 16 })
```

## Type Declarations

```ts
export interface UseCounterOptions {
  min?: number
  max?: number
}
export interface UseCounterReturn {
  /**
   * The current value of the counter.
   */
  readonly count: Readonly<Ref<number>>
  /**
   * Increment the counter.
   *
   * @param {number} [delta=1] The number to increment.
   */
  inc: (delta?: number) => void
  /**
   * Decrement the counter.
   *
   * @param {number} [delta=1] The number to decrement.
   */
  dec: (delta?: number) => void
  /**
   * Get the current value of the counter.
   */
  get: () => number
  /**
   * Set the counter to a new value.
   *
   * @param val The new value of the counter.
   */
  set: (val: number) => void
  /**
   * Reset the counter to an initial value.
   */
  reset: (val?: number) => number
}
/**
 * Basic counter with utility functions.
 *
 * @see https://vueuse.org/useCounter
 * @param [initialValue]
 * @param options
 */
export declare function useCounter(
  initialValue?: MaybeRef<number>,
  options?: UseCounterOptions,
): {
  count: Readonly<
    | Ref<number, number>
    | ShallowRef<number, number>
    | WritableComputedRef<number, number>
  >
  inc: (delta?: number) => number
  dec: (delta?: number) => number
  get: () => number
  set: (val: number) => number
  reset: (val?: number) => number
}
```
```

## File: `skills/vueuse-functions/references/useCssSupports.md`
```markdown
---
category: Browser
---

# useCssSupports

SSR compatible and reactive [`CSS.supports`](https://developer.mozilla.org/docs/Web/API/CSS/supports_static).

## Usage

```ts
import { useCssSupports } from '@vueuse/core'

const { isSupported } = useCssSupports('container-type', 'scroll-state')
```

## Type Declarations

```ts
export interface UseCssSupportsOptions extends ConfigurableWindow {
  ssrValue?: boolean
}
export interface UseCssSupportsReturn extends Supportable {}
export declare function useCssSupports(
  property: MaybeRefOrGetter<string>,
  value: MaybeRefOrGetter<string>,
  options?: UseCssSupportsOptions,
): UseCssSupportsReturn
export declare function useCssSupports(
  conditionText: MaybeRefOrGetter<string>,
  options?: UseCssSupportsOptions,
): UseCssSupportsReturn
```
```

## File: `skills/vueuse-functions/references/useCssVar.md`
```markdown
---
category: Browser
---

# useCssVar

Manipulate CSS variables

## Usage

```ts
import { useCssVar } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const color1 = useCssVar('--color', el)

const elv = useTemplateRef('elv')
const key = ref('--color')
const colorVal = useCssVar(key, elv)

const someEl = useTemplateRef('someEl')
const color2 = useCssVar('--color', someEl, { initialValue: '#eee' })
```

## Type Declarations

```ts
export interface UseCssVarOptions extends ConfigurableWindow {
  initialValue?: string
  /**
   * Use MutationObserver to monitor variable changes
   * @default false
   */
  observe?: boolean
}
/**
 * Manipulate CSS variables.
 *
 * @see https://vueuse.org/useCssVar
 * @param prop
 * @param target
 * @param options
 */
export declare function useCssVar(
  prop: MaybeRefOrGetter<string | null | undefined>,
  target?: MaybeElementRef,
  options?: UseCssVarOptions,
): ShallowRef<string | undefined, string | undefined>
```
```

## File: `skills/vueuse-functions/references/useCurrentElement.md`
```markdown
---
category: Component
---

# useCurrentElement

Get the DOM element of current component as a ref.

## Usage

```ts
import { useCurrentElement } from '@vueuse/core'

const el = useCurrentElement() // ComputedRef<Element>
```

Or pass a specific vue component

```vue
<script setup lang="ts">
import { useCurrentElement, VueInstance } from '@vueuse/core'
import { shallowRef } from 'vue'

const componentRef = shallowRef<VueInstance>(null as unknown as VueInstance)

const el = useCurrentElement(componentRef) // ComputedRef<Element>
</script>

<template>
  <div>
    <OtherVueComponent ref="componentRef" />
    <p>Hello world</p>
  </div>
</template>
```

## Caveats

This functions uses [`$el` under the hood](https://vuejs.org/api/component-instance.html#el).

Value of the ref will be `undefined` until the component is mounted.

- For components with a single root element, it will point to that element.
- For components with text root, it will point to the text node.
- For components with multiple root nodes, it will be the placeholder DOM node that Vue uses to keep track of the component's position in the DOM.

It's recommend to only use this function for components with **a single root element**.

## Type Declarations

```ts
export declare function useCurrentElement<
  T extends MaybeElement = MaybeElement,
  R extends VueInstance = VueInstance,
  E extends MaybeElement = MaybeElement extends T
    ? IsAny<R["$el"]> extends false
      ? R["$el"]
      : T
    : T,
>(rootComponent?: MaybeElementRef<R>): ComputedRefWithControl<E>
```
```

## File: `skills/vueuse-functions/references/useCycleList.md`
```markdown
---
category: Utilities
---

# useCycleList

Cycle through a list of items.

<CourseLink href="https://vueschool.io/lessons/create-an-image-carousel-with-vueuse?friend=vueuse">Learn how to use useCycleList to create an image carousel with this FREE video lesson from Vue School!</CourseLink>

## Usage

```ts
import { useCycleList } from '@vueuse/core'

const { state, next, prev, go } = useCycleList([
  'Dog',
  'Cat',
  'Lizard',
  'Shark',
  'Whale',
  'Dolphin',
  'Octopus',
  'Seal',
])

console.log(state.value) // 'Dog'

prev()

console.log(state.value) // 'Seal'

go(3)

console.log(state.value) // 'Shark'
```

## Type Declarations

```ts
export interface UseCycleListOptions<T> {
  /**
   * The initial value of the state.
   * A ref can be provided to reuse.
   */
  initialValue?: MaybeRef<T>
  /**
   * The default index when
   */
  fallbackIndex?: number
  /**
   * Custom function to get the index of the current value.
   */
  getIndexOf?: (value: T, list: T[]) => number
}
/**
 * Cycle through a list of items
 *
 * @see https://vueuse.org/useCycleList
 */
export declare function useCycleList<T>(
  list: MaybeRefOrGetter<T[]>,
  options?: UseCycleListOptions<T>,
): UseCycleListReturn<T>
export interface UseCycleListReturn<T> {
  state: ShallowRef<T>
  index: WritableComputedRef<number>
  next: (n?: number) => T
  prev: (n?: number) => T
  /**
   * Go to a specific index
   */
  go: (i: number) => T
}
```
```

## File: `skills/vueuse-functions/references/useDark.md`
```markdown
---
category: Browser
related:
  - useColorMode
  - usePreferredDark
  - useStorage
---

# useDark

Reactive dark mode with auto data persistence.

<CourseLink href="https://vueschool.io/lessons/theming-with-vueuse-usedark-and-usecolormode?friend=vueuse">Learn useDark with this FREE video lesson from Vue School!</CourseLink>

## Basic Usage

```ts
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)
```

## Behavior

`useDark` combines with `usePreferredDark` and `useStorage`. On start up, it reads the value from localStorage/sessionStorage (the key is configurable) to see if there is a user configured color scheme, if not, it will use users' system preferences. When you change the `isDark` ref, it will update the corresponding element's attribute and then store the preference to storage (default key: `vueuse-color-scheme`) for persistence.

> Please note `useDark` only handles the DOM attribute changes for you to apply proper selector in your CSS. It does NOT handle the actual style, theme or CSS for you.

## Configuration

By default, it uses [Tailwind CSS favored dark mode](https://tailwindcss.com/docs/dark-mode#toggling-dark-mode-manually), which enables dark mode when class `dark` is applied to the `html` tag, for example:

```html
<!--light-->
<html>
  ...
</html>

<!--dark-->
<html class="dark">
  ...
</html>
```

Still, you can also customize it to make it work with most CSS frameworks.

For example:

```ts
import { useDark } from '@vueuse/core'
// ---cut---
const isDark = useDark({
  selector: 'body',
  attribute: 'color-scheme',
  valueDark: 'dark',
  valueLight: 'light',
})
```

will work like

```html
<!--light-->
<html>
  <body color-scheme="light">
    ...
  </body>
</html>

<!--dark-->
<html>
  <body color-scheme="dark">
    ...
  </body>
</html>
```

If the configuration above still does not fit your needs, you can use the`onChanged` option to take full control over how you handle updates.

```ts
import { useDark } from '@vueuse/core'
// ---cut---
const isDark = useDark({
  onChanged(dark) {
    // update the dom, call the API or something
  },
})
```

## Component Usage

```vue
<template>
  <UseDark v-slot="{ isDark, toggleDark }">
    <button @click="toggleDark()">
      Is Dark: {{ isDark }}
    </button>
  </UseDark>
</template>
```

## Type Declarations

```ts
export interface UseDarkOptions extends Omit<
  UseColorModeOptions<BasicColorSchema>,
  "modes" | "onChanged"
> {
  /**
   * Value applying to the target element when isDark=true
   *
   * @default 'dark'
   */
  valueDark?: string
  /**
   * Value applying to the target element when isDark=false
   *
   * @default ''
   */
  valueLight?: string
  /**
   * A custom handler for handle the updates.
   * When specified, the default behavior will be overridden.
   *
   * @default undefined
   */
  onChanged?: (
    isDark: boolean,
    defaultHandler: (mode: BasicColorSchema) => void,
    mode: BasicColorSchema,
  ) => void
}
export type UseDarkReturn = WritableComputedRef<boolean>
/**
 * Reactive dark mode with auto data persistence.
 *
 * @see https://vueuse.org/useDark
 * @param options
 */
export declare function useDark(options?: UseDarkOptions): UseDarkReturn
```
```

## File: `skills/vueuse-functions/references/useDateFormat.md`
```markdown
---
category: Time
---

# useDateFormat

Get the formatted date according to the string of tokens passed in, inspired
by [dayjs](https://github.com/iamkun/dayjs).

**List of all available formats (HH:mm:ss by default):**

| Format | Output                   | Description                             |
| ------ | ------------------------ | --------------------------------------- |
| `Yo`   | 2018th                   | Ordinal formatted year                  |
| `YY`   | 18                       | Two-digit year                          |
| `YYYY` | 2018                     | Four-digit year                         |
| `M`    | 1-12                     | The month, beginning at 1               |
| `Mo`   | 1st, 2nd, ..., 12th      | The month, ordinal formatted            |
| `MM`   | 01-12                    | The month, 2-digits                     |
| `MMM`  | Jan-Dec                  | The abbreviated month name              |
| `MMMM` | January-December         | The full month name                     |
| `D`    | 1-31                     | The day of the month                    |
| `Do`   | 1st, 2nd, ..., 31st      | The day of the month, ordinal formatted |
| `DD`   | 01-31                    | The day of the month, 2-digits          |
| `H`    | 0-23                     | The hour                                |
| `Ho`   | 0th, 1st, 2nd, ..., 23rd | The hour, ordinal formatted             |
| `HH`   | 00-23                    | The hour, 2-digits                      |
| `h`    | 1-12                     | The hour, 12-hour clock                 |
| `ho`   | 1st, 2nd, ..., 12th      | The hour, 12-hour clock, sorted         |
| `hh`   | 01-12                    | The hour, 12-hour clock, 2-digits       |
| `m`    | 0-59                     | The minute                              |
| `mo`   | 0th, 1st, ..., 59th      | The minute, ordinal formatted           |
| `mm`   | 00-59                    | The minute, 2-digits                    |
| `s`    | 0-59                     | The second                              |
| `so`   | 0th, 1st, ..., 59th      | The second, ordinal formatted           |
| `ss`   | 00-59                    | The second, 2-digits                    |
| `SSS`  | 000-999                  | The millisecond, 3-digits               |
| `A`    | AM PM                    | The meridiem                            |
| `AA`   | A.M. P.M.                | The meridiem, periods                   |
| `a`    | am pm                    | The meridiem, lowercase                 |
| `aa`   | a.m. p.m.                | The meridiem, lowercase and periods     |
| `d`    | 0-6                      | The day of the week, with Sunday as 0   |
| `dd`   | S-S                      | The min name of the day of the week     |
| `ddd`  | Sun-Sat                  | The short name of the day of the week   |
| `dddd` | Sunday-Saturday          | The name of the day of the week         |
| `z`    | GMT, GMT+1               | The timezone with offset                |
| `zz`   | GMT, GMT+1               | The timezone with offset                |
| `zzz`  | GMT, GMT+1               | The timezone with offset                |
| `zzzz` | GMT, GMT+01:00           | The long timezone with offset           |

- Meridiem is customizable by defining `customMeridiem` in `options`.

## Usage

### Basic

```vue
<script setup lang="ts">
import { useDateFormat, useNow } from '@vueuse/core'

const formatted = useDateFormat(useNow(), 'YYYY-MM-DD HH:mm:ss')
</script>

<template>
  <div>{{ formatted }}</div>
</template>
```

### Use with locales

```vue
<script setup lang="ts">
import { useDateFormat, useNow } from '@vueuse/core'

const formatted = useDateFormat(useNow(), 'YYYY-MM-DD (ddd)', { locales: 'en-US' })
</script>

<template>
  <div>{{ formatted }}</div>
</template>
```

### Use with custom meridiem

```vue
<script setup lang="ts">
import { useDateFormat } from '@vueuse/core'

function customMeridiem(hours: number, minutes: number, isLowercase?: boolean, hasPeriod?: boolean) {
  const m = hours > 11 ? (isLowercase ? 'μμ' : 'ΜΜ') : (isLowercase ? 'πμ' : 'ΠΜ')
  return hasPeriod ? m.split('').reduce((acc, current) => acc += `${current}.`, '') : m
}

const am = useDateFormat('2022-01-01 05:05:05', 'hh:mm:ss A', { customMeridiem })
// am.value = '05:05:05 ΠΜ'
const pm = useDateFormat('2022-01-01 17:05:05', 'hh:mm:ss AA', { customMeridiem })
// pm.value = '05:05:05 Μ.Μ.'
</script>
```

## Type Declarations

```ts
export type DateLike = Date | number | string | undefined
export interface UseDateFormatOptions {
  /**
   * The locale(s) to used for dd/ddd/dddd/MMM/MMMM format
   *
   * [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument).
   */
  locales?: MaybeRefOrGetter<Intl.LocalesArgument>
  /**
   * A custom function to re-modify the way to display meridiem
   *
   */
  customMeridiem?: (
    hours: number,
    minutes: number,
    isLowercase?: boolean,
    hasPeriod?: boolean,
  ) => string
}
export declare function formatDate(
  date: Date,
  formatStr: string,
  options?: UseDateFormatOptions,
): string
export declare function normalizeDate(date: DateLike): Date
export type UseDateFormatReturn = ComputedRef<string>
/**
 * Get the formatted date according to the string of tokens passed in.
 *
 * @see https://vueuse.org/useDateFormat
 * @param date - The date to format, can either be a `Date` object, a timestamp, or a string
 * @param formatStr - The combination of tokens to format the date
 * @param options - UseDateFormatOptions
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useDateFormat(
  date: MaybeRefOrGetter<DateLike>,
  formatStr?: MaybeRefOrGetter<string>,
  options?: UseDateFormatOptions,
): UseDateFormatReturn
```
```

## File: `skills/vueuse-functions/references/useDebounceFn.md`
```markdown
---
category: Utilities
related: useThrottleFn
---

# useDebounceFn

Debounce execution of a function.

> Debounce is an overloaded waiter: if you keep asking, your requests will be ignored until you stop and give them some time to think about your latest inquiry.

## Usage

```ts
import { useDebounceFn, useEventListener } from '@vueuse/core'

const debouncedFn = useDebounceFn(() => {
  // do something
}, 1000)

useEventListener(window, 'resize', debouncedFn)
```

You can also pass a 3rd parameter to this, with a maximum wait time, similar to [lodash debounce](https://lodash.com/docs/4.17.15#debounce)

```ts
import { useDebounceFn, useEventListener } from '@vueuse/core'

// If no invokation after 5000ms due to repeated input,
// the function will be called anyway.
const debouncedFn = useDebounceFn(() => {
  // do something
}, 1000, { maxWait: 5000 })

useEventListener(window, 'resize', debouncedFn)
```

Optionally, you can get the return value of the function using promise operations.

```ts
import { useDebounceFn } from '@vueuse/core'

const debouncedRequest = useDebounceFn(() => 'response', 1000)

debouncedRequest().then((value) => {
  console.log(value) // 'response'
})

// or use async/await
async function doRequest() {
  const value = await debouncedRequest()
  console.log(value) // 'response'
}
```

Since unhandled rejection error is quite annoying when developer doesn't need the return value, the promise will **NOT** be rejected if the function is canceled **by default**. You need to specify the option `rejectOnCancel: true` to capture the rejection.

```ts
import { useDebounceFn } from '@vueuse/core'

const debouncedRequest = useDebounceFn(() => 'response', 1000, { rejectOnCancel: true })

debouncedRequest()
  .then((value) => {
    // do something
  })
  .catch(() => {
    // do something when canceled
  })

// calling it again will cancel the previous request and gets rejected
setTimeout(debouncedRequest, 500)
```

## Recommended Reading

- [**Debounce vs Throttle**: Definitive Visual Guide](https://kettanaito.com/blog/debounce-vs-throttle)

## Type Declarations

```ts
export type UseDebounceFnReturn<T extends FunctionArgs> = PromisifyFn<T>
/**
 * Debounce execution of a function.
 *
 * @see https://vueuse.org/useDebounceFn
 * @param  fn          A function to be executed after delay milliseconds debounced.
 * @param  ms          A zero-or-greater delay in milliseconds. For event callbacks, values around 100 or 250 (or even higher) are most useful.
 * @param  options     Options
 *
 * @return A new, debounce, function.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useDebounceFn<T extends FunctionArgs>(
  fn: T,
  ms?: MaybeRefOrGetter<number>,
  options?: DebounceFilterOptions,
): UseDebounceFnReturn<T>
```
```

## File: `skills/vueuse-functions/references/useDebouncedRefHistory.md`
```markdown
---
category: State
related:
  - useRefHistory
  - useThrottledRefHistory
---

# useDebouncedRefHistory

Shorthand for `useRefHistory` with debounced filter.

## Usage

This function takes a snapshot of your counter after 1000ms when the value of it starts to change.

```ts
import { useDebouncedRefHistory } from '@vueuse/core'
import { shallowRef } from 'vue'

const counter = shallowRef(0)
const { history, undo, redo } = useDebouncedRefHistory(counter, { deep: true, debounce: 1000 })
```

## Type Declarations

```ts
/**
 * Shorthand for [useRefHistory](https://vueuse.org/useRefHistory) with debounce filter.
 *
 * @see https://vueuse.org/useDebouncedRefHistory
 * @param source
 * @param options
 */
export declare function useDebouncedRefHistory<Raw, Serialized = Raw>(
  source: Ref<Raw>,
  options?: Omit<UseRefHistoryOptions<Raw, Serialized>, "eventFilter"> & {
    debounce?: MaybeRefOrGetter<number>
  },
): UseRefHistoryReturn<Raw, Serialized>
```
```

## File: `skills/vueuse-functions/references/useDeviceMotion.md`
```markdown
---
category: Sensors
---

# useDeviceMotion

Reactive [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent). Provide web developers with information about the speed of changes for the device's position and orientation.

## Usage

```ts
import { useDeviceMotion } from '@vueuse/core'

const {
  acceleration,
  accelerationIncludingGravity,
  rotationRate,
  interval,
} = useDeviceMotion()
```

> Note: For iOS, you need to use `trigger` and bind it with user interaction.
> After permission granted, the API will run automatically

| State                        | Type            | Description                                                                                                          |
| ---------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------- |
| acceleration                 | `object`        | An object giving the acceleration of the device on the three axis X, Y and Z.                                        |
| accelerationIncludingGravity | `object`        | An object giving the acceleration of the device on the three axis X, Y and Z with the effect of gravity.             |
| rotationRate                 | `object`        | An object giving the rate of change of the device's orientation on the three orientation axis alpha, beta and gamma. |
| interval                     | `Number`        | A number representing the interval of time, in milliseconds, at which data is obtained from the device..             |
| ensurePermissions            | `boolean`       | Indicates whether the platform requires permission to use the API                                                    |
| permissionGranted            | `boolean`       | Indicates whether the user has granted permission. The default is always false                                       |
| trigger                      | `Promise<void>` | An async function to request user permission. The API runs automatically once permission is granted                  |

You can find [more information about the state on the MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent#instance_properties).

## Component Usage

```vue
<template>
  <UseDeviceMotion v-slot="{ acceleration }">
    Acceleration: {{ acceleration }}
  </UseDeviceMotion>
</template>
```

## Type Declarations

```ts
export interface UseDeviceMotionOptions
  extends ConfigurableWindow, ConfigurableEventFilter {
  /**
   * Request for permissions immediately if it's not granted,
   * otherwise label and deviceIds could be empty
   *
   * @default false
   */
  requestPermissions?: boolean
}
/** @deprecated use {@link UseDeviceMotionOptions} instead */
export type DeviceMotionOptions = UseDeviceMotionOptions
export interface UseDeviceMotionReturn extends Supportable {
  acceleration: Ref<DeviceMotionEventAcceleration | null>
  accelerationIncludingGravity: Ref<DeviceMotionEventAcceleration | null>
  rotationRate: Ref<DeviceMotionEventRotationRate | null>
  interval: ShallowRef<number>
  requirePermissions: ComputedRef<boolean>
  ensurePermissions: () => Promise<void>
  permissionGranted: ShallowRef<boolean>
}
/**
 * Reactive DeviceMotionEvent.
 *
 * @see https://vueuse.org/useDeviceMotion
 * @param options
 */
export declare function useDeviceMotion(
  options?: UseDeviceMotionOptions,
): UseDeviceMotionReturn
```
```

## File: `skills/vueuse-functions/references/useDeviceOrientation.md`
```markdown
---
category: Sensors
---

# useDeviceOrientation

Reactive [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent). Provide web developers with information from the physical orientation of the device running the web page.

## Usage

```ts
import { useDeviceOrientation } from '@vueuse/core'

const {
  isAbsolute,
  alpha,
  beta,
  gamma,
} = useDeviceOrientation()
```

| State      | Type      | Description                                                                                                                |
| ---------- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| isAbsolute | `boolean` | A boolean that indicates whether or not the device is providing orientation data absolutely.                               |
| alpha      | `number`  | A number representing the motion of the device around the z axis, express in degrees with values ranging from 0 to 360.    |
| beta       | `number`  | A number representing the motion of the device around the x axis, express in degrees with values ranging from -180 to 180. |
| gamma      | `number`  | A number representing the motion of the device around the y axis, express in degrees with values ranging from -90 to 90.   |

You can find [more information about the state on the MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent#instance_properties).

## Component Usage

```vue
<template>
  <UseDeviceOrientation v-slot="{ alpha, beta, gamma }">
    Alpha: {{ alpha }}
    Beta: {{ beta }}
    Gamma: {{ gamma }}
  </UseDeviceOrientation>
</template>
```

## Type Declarations

```ts
export interface UseDeviceOrientationOptions extends ConfigurableWindow {}
export interface UseDeviceOrientationReturn extends Supportable {
  isAbsolute: ShallowRef<boolean, boolean>
  alpha: Ref<number | null, number | null>
  beta: Ref<number | null, number | null>
  gamma: Ref<number | null, number | null>
}
/**
 * Reactive DeviceOrientationEvent.
 *
 * @see https://vueuse.org/useDeviceOrientation
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useDeviceOrientation(
  options?: UseDeviceOrientationOptions,
): UseDeviceOrientationReturn
```
```

## File: `skills/vueuse-functions/references/useDevicePixelRatio.md`
```markdown
---
category: Sensors
---

# useDevicePixelRatio

Reactively track [`window.devicePixelRatio`](https://developer.mozilla.org/docs/Web/API/Window/devicePixelRatio)

> NOTE: there is no event listener for `window.devicePixelRatio` change. So this function uses [`Testing media queries programmatically (window.matchMedia)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Testing_media_queries) applying the same mechanism as described in [this example](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio#monitoring_screen_resolution_or_zoom_level_changes).

## Usage

```ts
import { useDevicePixelRatio } from '@vueuse/core'

const { pixelRatio } = useDevicePixelRatio()
```

## Component Usage

```vue
<template>
  <UseDevicePixelRatio v-slot="{ pixelRatio }">
    Pixel Ratio: {{ pixelRatio }}
  </UseDevicePixelRatio>
</template>
```

## Type Declarations

```ts
export interface UseDevicePixelRatioOptions extends ConfigurableWindow {}
export interface UseDevicePixelRatioReturn {
  pixelRatio: ShallowRef<number>
  stop: WatchStopHandle
}
/**
 * Reactively track `window.devicePixelRatio`.
 *
 * @see https://vueuse.org/useDevicePixelRatio
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useDevicePixelRatio(
  options?: UseDevicePixelRatioOptions,
): UseDevicePixelRatioReturn
```
```

## File: `skills/vueuse-functions/references/useDevicesList.md`
```markdown
---
category: Sensors
---

# useDevicesList

Reactive [enumerateDevices](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices) listing available input/output devices.

## Usage

```ts
import { useDevicesList } from '@vueuse/core'

const {
  devices,
  videoInputs: cameras,
  audioInputs: microphones,
  audioOutputs: speakers,
} = useDevicesList()
```

## Requesting Permissions

To request permissions, use the `ensurePermissions` method.

```ts
import { useDevicesList } from '@vueuse/core'
// ---cut---
const {
  ensurePermissions,
  permissionGranted,
} = useDevicesList()

await ensurePermissions()
console.log(permissionsGranted.value)
```

# Component

```vue
<template>
  <UseDevicesList v-slot="{ videoInputs, audioInputs, audioOutputs }">
    Cameras: {{ videoInputs }}
    Microphones: {{ audioInputs }}
    Speakers: {{ audioOutputs }}
  </UseDevicesList>
</template>
```

## Type Declarations

```ts
export interface UseDevicesListOptions extends ConfigurableNavigator {
  onUpdated?: (devices: MediaDeviceInfo[]) => void
  /**
   * Request for permissions immediately if it's not granted,
   * otherwise label and deviceIds could be empty
   *
   * @default false
   */
  requestPermissions?: boolean
  /**
   * Request for types of media permissions
   *
   * @default { audio: true, video: true }
   */
  constraints?: MediaStreamConstraints
}
export interface UseDevicesListReturn extends Supportable {
  /**
   * All devices
   */
  devices: Ref<MediaDeviceInfo[]>
  videoInputs: ComputedRef<MediaDeviceInfo[]>
  audioInputs: ComputedRef<MediaDeviceInfo[]>
  audioOutputs: ComputedRef<MediaDeviceInfo[]>
  permissionGranted: ShallowRef<boolean>
  ensurePermissions: () => Promise<boolean>
}
/**
 * Reactive `enumerateDevices` listing available input/output devices
 *
 * @see https://vueuse.org/useDevicesList
 * @param options
 */
export declare function useDevicesList(
  options?: UseDevicesListOptions,
): UseDevicesListReturn
```
```

## File: `skills/vueuse-functions/references/useDisplayMedia.md`
```markdown
---
category: Sensors
related: useUserMedia
---

# useDisplayMedia

Reactive [`mediaDevices.getDisplayMedia`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia) streaming.

## Usage

```vue
<script setup lang="ts">
import { useDisplayMedia } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const { stream, start } = useDisplayMedia()

// start streaming
start()

const videoRef = useTemplateRef('video')
watchEffect(() => {
  // preview on a video element
  videoRef.value.srcObject = stream.value
})
</script>

<template>
  <video ref="video" />
</template>
```

## Type Declarations

```ts
export interface UseDisplayMediaOptions extends ConfigurableNavigator {
  /**
   * If the stream is enabled
   * @default false
   */
  enabled?: MaybeRef<boolean>
  /**
   * If the stream video media constraints
   */
  video?: boolean | MediaTrackConstraints | undefined
  /**
   * If the stream audio media constraints
   */
  audio?: boolean | MediaTrackConstraints | undefined
}
export interface UseDisplayMediaReturn extends Supportable {
  stream: ShallowRef<MediaStream | undefined>
  start: () => Promise<MediaStream | undefined>
  stop: () => void
  enabled: ShallowRef<boolean>
}
/**
 * Reactive `mediaDevices.getDisplayMedia` streaming
 *
 * @see https://vueuse.org/useDisplayMedia
 * @param options
 */
export declare function useDisplayMedia(
  options?: UseDisplayMediaOptions,
): UseDisplayMediaReturn
```
```

## File: `skills/vueuse-functions/references/useDocumentVisibility.md`
```markdown
---
category: Elements
---

# useDocumentVisibility

Reactively track [`document.visibilityState`](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState)

## Usage

```vue
<script setup lang="ts">
import { useDocumentVisibility } from '@vueuse/core'

const visibility = useDocumentVisibility()
</script>
```

## Component Usage

```vue
<template>
  <UseDocumentVisibility v-slot="{ visibility }">
    Document Visibility: {{ visibility }}
  </UseDocumentVisibility>
</template>
```

## Type Declarations

```ts
export interface UseDocumentVisibilityOptions extends ConfigurableDocument {}
export type UseDocumentVisibilityReturn = ShallowRef<DocumentVisibilityState>
/**
 * Reactively track `document.visibilityState`.
 *
 * @see https://vueuse.org/useDocumentVisibility
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useDocumentVisibility(
  options?: UseDocumentVisibilityOptions,
): UseDocumentVisibilityReturn
```
```

## File: `skills/vueuse-functions/references/useDraggable.md`
```markdown
---
category: Elements
---

# useDraggable

Make elements draggable.

## Usage

```vue
<script setup lang="ts">
import { useDraggable } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')

// `style` will be a helper computed for `left: ?px; top: ?px;`
const { x, y, style } = useDraggable(el, {
  initialValue: { x: 40, y: 40 },
})
</script>

<template>
  <div ref="el" :style="style" style="position: fixed">
    Drag me! I am at {{ x }}, {{ y }}
  </div>
</template>
```

### Return Values

| Property     | Type                   | Description                             |
| ------------ | ---------------------- | --------------------------------------- |
| `x`          | `Ref<number>`          | Current x position                      |
| `y`          | `Ref<number>`          | Current y position                      |
| `position`   | `Ref<{x, y}>`          | Current position object                 |
| `isDragging` | `ComputedRef<boolean>` | Whether currently dragging              |
| `style`      | `ComputedRef<string>`  | CSS style string `left: ?px; top: ?px;` |

### Options

```ts
useDraggable(el, {
  // Initial position (default: { x: 0, y: 0 })
  initialValue: { x: 40, y: 40 },
  // Restrict dragging to specific axis: 'x', 'y', or 'both' (default)
  axis: 'both',
  // Only trigger when clicking directly on the element (default: false)
  exact: false,
  // Prevent default browser behavior (default: false)
  preventDefault: true,
  // Stop event propagation (default: false)
  stopPropagation: false,
  // Use capture phase for events (default: true)
  capture: true,
  // Disable dragging (default: false)
  disabled: false,
  // Mouse buttons that trigger drag (default: [0] - left button)
  buttons: [0],
  // Pointer types to listen to (default: ['mouse', 'touch', 'pen'])
  pointerTypes: ['mouse', 'touch', 'pen'],
  // Custom drag handle element (default: target element)
  handle: handleRef,
  // Container element for bounds (default: none)
  containerElement: containerRef,
  // Element to attach pointermove/pointerup events (default: window)
  draggingElement: window,
  // Callbacks
  onStart: (position, event) => {
    // Return false to prevent dragging
  },
  onMove: (position, event) => {},
  onEnd: (position, event) => {},
})
```

### Prevent Default

Set `preventDefault: true` to override the default drag-and-drop behavior of certain elements in the browser (e.g., images).

```ts
import { useDraggable } from '@vueuse/core'

const { x, y, style } = useDraggable(el, {
  preventDefault: true,
})
```

### Container Bounds

Use `containerElement` to constrain dragging within a container.

```ts
import { useDraggable } from '@vueuse/core'

const { x, y } = useDraggable(el, {
  containerElement: containerRef,
})
```

Set `autoScroll: true` to enable auto-scroll when dragging near the edges.

```ts
const { x, y, style } = useDraggable(el, {
  autoScroll: {
    speed: 2, // Control the speed of auto-scroll.
    margin: 30, // Set the margin from the edge that triggers auto-scroll.
    direction: 'both' // Determine the direction of auto-scroll.
  },
})
```

## Component Usage

```vue
<template>
  <UseDraggable v-slot="{ x, y }" :initial-value="{ x: 10, y: 10 }">
    Drag me! I am at {{ x }}, {{ y }}
  </UseDraggable>
</template>
```

For component usage, additional props `storageKey` and `storageType` can be passed to the component and enable the persistence of the element position.

```vue
<template>
  <UseDraggable storage-key="vueuse-draggable" storage-type="session">
    Refresh the page and I am still in the same position!
  </UseDraggable>
</template>
```

## Type Declarations

```ts
export interface UseDraggableOptions {
  /**
   * Only start the dragging when click on the element directly
   *
   * @default false
   */
  exact?: MaybeRefOrGetter<boolean>
  /**
   * Prevent events defaults
   *
   * @default false
   */
  preventDefault?: MaybeRefOrGetter<boolean>
  /**
   * Prevent events propagation
   *
   * @default false
   */
  stopPropagation?: MaybeRefOrGetter<boolean>
  /**
   * Whether dispatch events in capturing phase
   *
   * @default true
   */
  capture?: boolean
  /**
   * Element to attach `pointermove` and `pointerup` events to.
   *
   * @default window
   */
  draggingElement?: MaybeRefOrGetter<
    HTMLElement | SVGElement | Window | Document | null | undefined
  >
  /**
   * Element for calculating bounds (If not set, it will use the event's target).
   *
   * @default undefined
   */
  containerElement?: MaybeRefOrGetter<
    HTMLElement | SVGElement | null | undefined
  >
  /**
   * Handle that triggers the drag event
   *
   * @default target
   */
  handle?: MaybeRefOrGetter<HTMLElement | SVGElement | null | undefined>
  /**
   * Pointer types that listen to.
   *
   * @default ['mouse', 'touch', 'pen']
   */
  pointerTypes?: PointerType[]
  /**
   * Initial position of the element.
   *
   * @default { x: 0, y: 0 }
   */
  initialValue?: MaybeRefOrGetter<Position>
  /**
   * Callback when the dragging starts. Return `false` to prevent dragging.
   */
  onStart?: (position: Position, event: PointerEvent) => void | false
  /**
   * Callback during dragging.
   */
  onMove?: (position: Position, event: PointerEvent) => void
  /**
   * Callback when dragging end.
   */
  onEnd?: (position: Position, event: PointerEvent) => void
  /**
   * Axis to drag on.
   *
   * @default 'both'
   */
  axis?: "x" | "y" | "both"
  /**
   * Disabled drag and drop.
   *
   * @default false
   */
  disabled?: MaybeRefOrGetter<boolean>
  /**
   * Mouse buttons that are allowed to trigger drag events.
   *
   * - `0`: Main button, usually the left button or the un-initialized state
   * - `1`: Auxiliary button, usually the wheel button or the middle button (if present)
   * - `2`: Secondary button, usually the right button
   * - `3`: Fourth button, typically the Browser Back button
   * - `4`: Fifth button, typically the Browser Forward button
   *
   * @see https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/button#value
   * @default [0]
   */
  buttons?: MaybeRefOrGetter<number[]>
  /**
   * Whether to restrict dragging within the visible area of the container.
   *
   * If enabled, the draggable element will not leave the visible area of its container,
   * ensuring it remains within the viewport of the container during the drag.
   *
   * @default false
   */
  restrictInView?: MaybeRefOrGetter<boolean>
  /**
   * Whether to enable auto-scroll when dragging near the edges.
   *
   * @default false
   */
  autoScroll?: MaybeRefOrGetter<
    | boolean
    | {
        /**
         * Speed of auto-scroll.
         *
         * @default 2
         */
        speed?: MaybeRefOrGetter<number | Position>
        /**
         * Margin from the edge to trigger auto-scroll.
         *
         * @default 30
         */
        margin?: MaybeRefOrGetter<number | Position>
        /**
         * Direction of auto-scroll.
         *
         * @default 'both'
         */
        direction?: "x" | "y" | "both"
      }
  >
}
export interface UseDraggableReturn {
  x: Ref<number>
  y: Ref<number>
  position: Ref<Position>
  isDragging: ComputedRef<boolean>
  style: ComputedRef<string>
}
/**
 * Make elements draggable.
 *
 * @see https://vueuse.org/useDraggable
 * @param target
 * @param options
 */
export declare function useDraggable(
  target: MaybeRefOrGetter<HTMLElement | SVGElement | null | undefined>,
  options?: UseDraggableOptions,
): UseDraggableReturn
```
```

## File: `skills/vueuse-functions/references/useDrauu.md`
```markdown
---
category: '@Integrations'
---

# useDrauu

Reactive instance for [drauu](https://github.com/antfu/drauu).

## Install

```bash
npm i drauu@^0
```

## Usage

```vue
<script setup lang="ts">
import { toRefs } from '@vueuse/core'
import { useDrauu } from '@vueuse/integrations/useDrauu'
import { useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const { undo, redo, canUndo, canRedo, brush } = useDrauu(target)
const { color, size } = toRefs(brush)
</script>

<template>
  <svg ref="target" />
</template>
```

## Type Declarations

```ts
export type UseDrauuOptions = Omit<Options, "el">
export interface UseDrauuReturn {
  drauuInstance: Ref<Drauu | undefined>
  load: (svg: string) => void
  dump: () => string | undefined
  clear: () => void
  cancel: () => void
  undo: () => boolean | undefined
  redo: () => boolean | undefined
  canUndo: ShallowRef<boolean>
  canRedo: ShallowRef<boolean>
  brush: Ref<Brush>
  onChanged: EventHookOn
  onCommitted: EventHookOn
  onStart: EventHookOn
  onEnd: EventHookOn
  onCanceled: EventHookOn
}
/**
 * Reactive drauu
 *
 * @see https://vueuse.org/useDrauu
 * @param target The target svg element
 * @param options Drauu Options
 */
export declare function useDrauu(
  target: MaybeComputedElementRef,
  options?: UseDrauuOptions,
): UseDrauuReturn
```
```

## File: `skills/vueuse-functions/references/useDropZone.md`
```markdown
---
category: Elements
---

# useDropZone

Create a zone where files can be dropped.

::: warning

Due to Safari browser limitations, file type validation is only possible during the drop event, not during drag events. As a result, the `isOverDropZone` value will always be `true` during drag operations in Safari, regardless of file type.

:::

## Usage

```vue
<script setup lang="ts">
import { useDropZone } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const dropZoneRef = useTemplateRef('dropZoneRef')

function onDrop(files: File[] | null) {
  // called when files are dropped on zone
}

const { isOverDropZone } = useDropZone(dropZoneRef, {
  onDrop,
  // specify the types of data to be received.
  dataTypes: ['image/jpeg'],
  // control multi-file drop
  multiple: true,
  // whether to prevent default behavior for unhandled events
  preventDefaultForUnhandled: false,
})
</script>

<template>
  <div ref="dropZoneRef">
    Drop files here
  </div>
</template>
```

## Type Declarations

```ts
export interface UseDropZoneReturn {
  files: ShallowRef<File[] | null>
  isOverDropZone: ShallowRef<boolean>
}
export interface UseDropZoneOptions {
  /**
   * Allowed data types, if not set, all data types are allowed.
   * Also can be a function to check the data types.
   */
  dataTypes?:
    | MaybeRef<readonly string[]>
    | ((types: readonly string[]) => boolean)
  /**
   * Similar to dataTypes, but exposes the DataTransferItemList for custom validation.
   * If provided, this function takes precedence over dataTypes.
   */
  checkValidity?: (items: DataTransferItemList) => boolean
  onDrop?: (files: File[] | null, event: DragEvent) => void
  onEnter?: (files: File[] | null, event: DragEvent) => void
  onLeave?: (files: File[] | null, event: DragEvent) => void
  onOver?: (files: File[] | null, event: DragEvent) => void
  /**
   * Allow multiple files to be dropped. Defaults to true.
   */
  multiple?: boolean
  /**
   * Prevent default behavior for unhandled events. Defaults to false.
   */
  preventDefaultForUnhandled?: boolean
}
export declare function useDropZone(
  target: MaybeRefOrGetter<HTMLElement | Document | null | undefined>,
  options?: UseDropZoneOptions | UseDropZoneOptions["onDrop"],
): UseDropZoneReturn
```
```

## File: `skills/vueuse-functions/references/useElementBounding.md`
```markdown
---
category: Elements
---

# useElementBounding

Reactive [bounding box](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) of an HTML element

## Usage

```vue
<script setup lang="ts">
import { useElementBounding } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { x, y, top, right, bottom, left, width, height } = useElementBounding(el)
</script>

<template>
  <div ref="el" />
</template>
```

## Component Usage

```vue
<template>
  <UseElementBounding v-slot="{ width, height }">
    Width: {{ width }} Height: {{ height }}
  </UseElementBounding>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vElementBounding } from '@vueuse/components'

interface BoundingType {
  height: number
  bottom: number
  left: number
  right: number
  top: number
  width: number
  x: number
  y: number
}

function onBounding({ height, bottom, left, right, top, width, x, y }: BoundingType) {
  console.log(height, bottom, left, right, top, width, x, y)
}

const options = {
  reset: true,
  windowResize: true,
  windowScroll: true,
  immediate: true,
  updateTiming: 'sync',
}
</script>

<template>
  <textarea v-element-bounding="onBounding" />
  <!-- with options -->
  <textarea v-element-bounding="[onBounding, options]" />
</template>
```

## Type Declarations

```ts
export interface UseElementBoundingOptions {
  /**
   * Reset values to 0 on component unmounted
   *
   * @default true
   */
  reset?: boolean
  /**
   * Listen to window resize event
   *
   * @default true
   */
  windowResize?: boolean
  /**
   * Listen to window scroll event
   *
   * @default true
   */
  windowScroll?: boolean
  /**
   * Immediately call update on component mounted
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Timing to recalculate the bounding box
   *
   * Setting to `next-frame` can be useful when using this together with something like {@link useBreakpoints}
   * and therefore the layout (which influences the bounding box of the observed element) is not updated on the current tick.
   *
   * @default 'sync'
   */
  updateTiming?: "sync" | "next-frame"
}
export interface UseElementBoundingReturn {
  height: ShallowRef<number>
  bottom: ShallowRef<number>
  left: ShallowRef<number>
  right: ShallowRef<number>
  top: ShallowRef<number>
  width: ShallowRef<number>
  x: ShallowRef<number>
  y: ShallowRef<number>
  update: () => void
}
/**
 * Reactive bounding box of an HTML element.
 *
 * @see https://vueuse.org/useElementBounding
 * @param target
 */
export declare function useElementBounding(
  target: MaybeComputedElementRef,
  options?: UseElementBoundingOptions,
): UseElementBoundingReturn
```
```

## File: `skills/vueuse-functions/references/useElementByPoint.md`
```markdown
---
category: Sensors
---

# useElementByPoint

Reactive element by point.

## Usage

```ts
import { useElementByPoint, useMouse } from '@vueuse/core'

const { x, y } = useMouse({ type: 'client' })
const { element } = useElementByPoint({ x, y })
```

## Type Declarations

```ts
export interface UseElementByPointOptions<Multiple extends boolean = false>
  extends ConfigurableDocument, ConfigurableScheduler {
  x: MaybeRefOrGetter<number>
  y: MaybeRefOrGetter<number>
  multiple?: MaybeRefOrGetter<Multiple>
  /** @deprecated Please use `scheduler` option instead */
  immediate?: boolean
  /** @deprecated Please use `scheduler` option instead */
  interval?: "requestAnimationFrame" | number
}
export interface UseElementByPointReturn<Multiple extends boolean = false>
  extends Supportable, Pausable {
  element: ShallowRef<
    Multiple extends true ? HTMLElement[] : HTMLElement | null
  >
}
/**
 * Reactive element by point.
 *
 * @see https://vueuse.org/useElementByPoint
 * @param options - UseElementByPointOptions
 */
export declare function useElementByPoint<M extends boolean = false>(
  options: UseElementByPointOptions<M>,
): UseElementByPointReturn<M>
```
```

## File: `skills/vueuse-functions/references/useElementHover.md`
```markdown
---
category: Sensors
---

# useElementHover

Reactive element's hover state.

## Usage

```vue
<script setup lang="ts">
import { useElementHover } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const myHoverableElement = useTemplateRef('myHoverableElement')
const isHovered = useElementHover(myHoverableElement)
</script>

<template>
  <button ref="myHoverableElement">
    {{ isHovered }}
  </button>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vElementHover } from '@vueuse/components'
import { shallowRef } from 'vue'

const isHovered = shallowRef(false)
function onHover(state: boolean) {
  isHovered.value = state
}
</script>

<template>
  <button v-element-hover="onHover">
    {{ isHovered ? 'Thank you!' : 'Hover me' }}
  </button>
</template>
```

You can also provide hover options:

```vue
<script setup lang="ts">
import { vElementHover } from '@vueuse/components'
import { shallowRef } from 'vue'

const isHovered = shallowRef(false)
function onHover(hovered: boolean) {
  isHovered.value = hovered
}
</script>

<template>
  <button v-element-hover="[onHover, { delayEnter: 1000 }]">
    <span>{{ isHovered ? 'Thank you!' : 'Hover me' }}</span>
  </button>
</template>
```

## Type Declarations

```ts
export interface UseElementHoverOptions extends ConfigurableWindow {
  delayEnter?: number
  delayLeave?: number
  triggerOnRemoval?: boolean
}
export declare function useElementHover(
  el: MaybeRefOrGetter<EventTarget | null | undefined>,
  options?: UseElementHoverOptions,
): ShallowRef<boolean>
```
```

## File: `skills/vueuse-functions/references/useElementSize.md`
```markdown
---
category: Elements
---

# useElementSize

Reactive size of an HTML element. [ResizeObserver MDN](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)

## Usage

```vue
<script setup lang="ts">
import { useElementSize } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { width, height } = useElementSize(el)
</script>

<template>
  <div ref="el">
    Height: {{ height }}
    Width: {{ width }}
  </div>
</template>
```

## Component Usage

```vue
<template>
  <UseElementSize v-slot="{ width, height }">
    Width: {{ width }} Height: {{ height }}
  </UseElementSize>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vElementSize } from '@vueuse/components'

function onResize({ width, height }: { width: number, height: number }) {
  console.log(width, height)
}
</script>

<template>
  <textarea v-element-size="onResize" />
  <!-- with options -->
  <textarea v-element-size="[onResize, { width: 100, height: 100 }, { box: 'content-box' }]" />
</template>
```

## Type Declarations

```ts
export interface ElementSize {
  width: number
  height: number
}
export interface UseElementSizeOptions extends UseResizeObserverOptions {}
export interface UseElementSizeReturn {
  width: ShallowRef<number>
  height: ShallowRef<number>
  stop: () => void
}
/**
 * Reactive size of an HTML element.
 *
 * @see https://vueuse.org/useElementSize
 */
export declare function useElementSize(
  target: MaybeComputedElementRef,
  initialSize?: ElementSize,
  options?: UseElementSizeOptions,
): UseElementSizeReturn
```
```

## File: `skills/vueuse-functions/references/useElementVisibility.md`
```markdown
---
category: Elements
---

# useElementVisibility

Tracks the visibility of an element within the viewport.

## Usage

```vue
<script setup lang="ts">
import { useElementVisibility } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const targetIsVisible = useElementVisibility(target)
</script>

<template>
  <div ref="target">
    <h1>Hello world</h1>
  </div>
</template>
```

### rootMargin

If you wish to trigger your callback sooner before the element is fully visible, you can use
the `rootMargin` option (See [MDN IntersectionObserver/rootMargin](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/rootMargin)).

```ts
import { useElementVisibility } from '@vueuse/core'
// ---cut---
const targetIsVisible = useElementVisibility(target, {
  rootMargin: '0px 0px 100px 0px',
})
```

### threshold

If you want to control the percentage of the visibility required to update the value, you can use the `threshold` option (See [MDN IntersectionObserver/threshold](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver#threshold)).

```ts
const targetIsVisible = useElementVisibility(target, {
  threshold: 1.0, // 100% visible
})
```

## Component Usage

```vue
<template>
  <UseElementVisibility v-slot="{ isVisible }">
    Is Visible: {{ isVisible }}
  </UseElementVisibility>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vElementVisibility } from '@vueuse/components'
import { shallowRef, useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const isVisible = shallowRef(false)

function onElementVisibility(state) {
  isVisible.value = state
}
</script>

<template>
  <div v-element-visibility="onElementVisibility">
    {{ isVisible ? 'inside' : 'outside' }}
  </div>

  <!-- with options -->
  <div ref="target">
    <div v-element-visibility="[onElementVisibility, { scrollTarget: target }]">
      {{ isVisible ? 'inside' : 'outside' }}
    </div>
  </div>
</template>
```

## Type Declarations

```ts
export interface UseElementVisibilityOptions
  extends
    ConfigurableWindow,
    Pick<UseIntersectionObserverOptions, "rootMargin" | "threshold"> {
  /**
   * Initial value.
   *
   * @default false
   */
  initialValue?: boolean
  /**
   * The element that is used as the viewport for checking visibility of the target.
   */
  scrollTarget?: UseIntersectionObserverOptions["root"]
  /**
   * Stop tracking when element visibility changes for the first time
   *
   * @default false
   */
  once?: boolean
}
export type UseElementVisibilityReturn = ShallowRef<boolean>
/**
 * Tracks the visibility of an element within the viewport.
 *
 * @see https://vueuse.org/useElementVisibility
 */
export declare function useElementVisibility(
  element: MaybeComputedElementRef,
  options?: UseElementVisibilityOptions,
): UseElementVisibilityReturn
```
```

## File: `skills/vueuse-functions/references/useEventBus.md`
```markdown
---
category: Utilities
---

# useEventBus

A basic event bus.

## Usage

```ts
import { useEventBus } from '@vueuse/core'

const bus = useEventBus<string>('news')

function listener(event: string) {
  console.log(`news: ${event}`)
}

// listen to an event
const unsubscribe = bus.on(listener)

// fire an event
bus.emit('The Tokyo Olympics has begun')

// unregister the listener
unsubscribe()
// or
bus.off(listener)

// clearing all listeners
bus.reset()
```

Listeners registered inside of components `setup` will be unregistered automatically when the component gets unmounted.

## TypeScript

Using `EventBusKey` is the key to bind the event type to the key, similar to Vue's [`InjectionKey`](https://antfu.me/posts/typed-provide-and-inject-in-vue) util.

```ts
// fooKey.ts
import type { EventBusKey } from '@vueuse/core'

export const fooKey: EventBusKey<{ name: foo }> = Symbol('symbol-key')
```

```ts
import { useEventBus } from '@vueuse/core'

import { fooKey } from './fooKey'

const bus = useEventBus(fooKey)

bus.on((e) => {
  // `e` will be `{ name: foo }`
})
```

## Type Declarations

```ts
export type EventBusListener<T = unknown, P = any> = (
  event: T,
  payload?: P,
) => void
export type EventBusEvents<T, P = any> = Set<EventBusListener<T, P>>
export interface EventBusKey<T> extends Symbol {}
export type EventBusIdentifier<T = unknown> = EventBusKey<T> | string | number
export interface UseEventBusReturn<T, P> {
  /**
   * Subscribe to an event. When calling emit, the listeners will execute.
   * @param listener watch listener.
   * @returns a stop function to remove the current callback.
   */
  on: (listener: EventBusListener<T, P>) => Fn
  /**
   * Similar to `on`, but only fires once
   * @param listener watch listener.
   * @returns a stop function to remove the current callback.
   */
  once: (listener: EventBusListener<T, P>) => Fn
  /**
   * Emit an event, the corresponding event listeners will execute.
   * @param event data sent.
   */
  emit: (event?: T, payload?: P) => void
  /**
   * Remove the corresponding listener.
   * @param listener watch listener.
   */
  off: (listener: EventBusListener<T>) => void
  /**
   * Clear all events
   */
  reset: () => void
}
export declare function useEventBus<T = unknown, P = any>(
  key: EventBusIdentifier<T>,
): UseEventBusReturn<T, P>
```
```

## File: `skills/vueuse-functions/references/useEventListener.md`
```markdown
---
category: Browser
---

# useEventListener

Use EventListener with ease. Register using [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) on mounted, and [removeEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener) automatically on unmounted.

## Usage

```ts
import { useEventListener } from '@vueuse/core'

useEventListener(document, 'visibilitychange', (evt) => {
  console.log(evt)
})
```

### Default Target

When the target is omitted, it defaults to `window`:

```ts
import { useEventListener } from '@vueuse/core'

// Listens on window
useEventListener('resize', (evt) => {
  console.log(evt)
})
```

### Reactive Target

You can pass a ref as the event target, `useEventListener` will unregister the previous event and register the new one when the target changes.

```vue
<script setup lang="ts">
import { useEventListener } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const element = useTemplateRef('element')
useEventListener(element, 'keydown', (e) => {
  console.log(e.key)
})
</script>

<template>
  <div v-if="cond" ref="element">
    Div1
  </div>
  <div v-else ref="element">
    Div2
  </div>
</template>
```

### Multiple Events

You can pass an array of events to listen to multiple events at once:

```ts
import { useEventListener } from '@vueuse/core'

useEventListener(document, ['mouseenter', 'mouseleave'], (evt) => {
  console.log(evt.type)
})
```

### Multiple Targets

You can also pass an array of targets:

```ts
import { useEventListener } from '@vueuse/core'

const buttons = document.querySelectorAll('button')
useEventListener(buttons, 'click', (evt) => {
  console.log('Button clicked')
})
```

### Cleanup

Returns a cleanup function to manually unregister the listener:

```ts
import { useEventListener } from '@vueuse/core'

const cleanup = useEventListener(document, 'keydown', (e) => {
  console.log(e.key)
})

cleanup() // This will unregister the listener.
```

Note if your components also run in SSR (Server Side Rendering), you might get errors (like `document is not defined`) because DOM APIs like `document` and `window` are not available in Node.js. To avoid that you can put the logic inside `onMounted` hook.

```ts
import { useEventListener } from '@vueuse/core'
// ---cut---
// onMounted will only be called in the client side
// so it guarantees the DOM APIs are available.
onMounted(() => {
  useEventListener(document, 'keydown', (e) => {
    console.log(e.key)
  })
})
```

## Type Declarations

```ts
interface InferEventTarget<Events> {
  addEventListener: (event: Events, fn?: any, options?: any) => any
  removeEventListener: (event: Events, fn?: any, options?: any) => any
}
export type WindowEventName = keyof WindowEventMap
export type DocumentEventName = keyof DocumentEventMap
export type ShadowRootEventName = keyof ShadowRootEventMap
export interface GeneralEventListener<E = Event> {
  (evt: E): void
}
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 1: Omitted Window target
 *
 * @see https://vueuse.org/useEventListener
 */
export declare function useEventListener<E extends keyof WindowEventMap>(
  event: MaybeRefOrGetter<Arrayable<E>>,
  listener: MaybeRef<Arrayable<(this: Window, ev: WindowEventMap[E]) => any>>,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 2: Explicitly Window target
 *
 * @see https://vueuse.org/useEventListener
 * @param target
 * @param event
 * @param listener
 * @param options
 */
export declare function useEventListener<E extends keyof WindowEventMap>(
  target: Window,
  event: MaybeRefOrGetter<Arrayable<E>>,
  listener: MaybeRef<Arrayable<(this: Window, ev: WindowEventMap[E]) => any>>,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 3: Explicitly Document target
 *
 * @see https://vueuse.org/useEventListener
 */
export declare function useEventListener<E extends keyof DocumentEventMap>(
  target: Document,
  event: MaybeRefOrGetter<Arrayable<E>>,
  listener: MaybeRef<
    Arrayable<(this: Document, ev: DocumentEventMap[E]) => any>
  >,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 4: Explicitly ShadowRoot target
 *
 * @see https://vueuse.org/useEventListener
 */
export declare function useEventListener<E extends keyof ShadowRootEventMap>(
  target: MaybeRefOrGetter<Arrayable<ShadowRoot> | null | undefined>,
  event: MaybeRefOrGetter<Arrayable<E>>,
  listener: MaybeRef<
    Arrayable<(this: ShadowRoot, ev: ShadowRootEventMap[E]) => any>
  >,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 5: Explicitly HTMLElement target
 *
 * @see https://vueuse.org/useEventListener
 */
export declare function useEventListener<E extends keyof HTMLElementEventMap>(
  target: MaybeRefOrGetter<Arrayable<HTMLElement> | null | undefined>,
  event: MaybeRefOrGetter<Arrayable<E>>,
  listener: MaybeRef<(this: HTMLElement, ev: HTMLElementEventMap[E]) => any>,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 6: Custom event target with event type infer
 *
 * @see https://vueuse.org/useEventListener
 */
export declare function useEventListener<
  Names extends string,
  EventType = Event,
>(
  target: MaybeRefOrGetter<
    Arrayable<InferEventTarget<Names>> | null | undefined
  >,
  event: MaybeRefOrGetter<Arrayable<Names>>,
  listener: MaybeRef<Arrayable<GeneralEventListener<EventType>>>,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
/**
 * Register using addEventListener on mounted, and removeEventListener automatically on unmounted.
 *
 * Overload 7: Custom event target fallback
 *
 * @see https://vueuse.org/useEventListener
 */
export declare function useEventListener<EventType = Event>(
  target: MaybeRefOrGetter<Arrayable<EventTarget> | null | undefined>,
  event: MaybeRefOrGetter<Arrayable<string>>,
  listener: MaybeRef<Arrayable<GeneralEventListener<EventType>>>,
  options?: MaybeRefOrGetter<boolean | AddEventListenerOptions>,
): Fn
```
```

## File: `skills/vueuse-functions/references/useEventSource.md`
```markdown
---
category: Network
---

# useEventSource

An [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) or [Server-Sent-Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) instance opens a persistent connection to an HTTP server, which sends events in text/event-stream format.

## Usage

```ts
import { useEventSource } from '@vueuse/core'

const { status, data, error, close } = useEventSource('https://event-source-url')
```

See the [Type Declarations](#type-declarations) for more options.

### Named Events

You can define named events with the second parameter

```ts
import { useEventSource } from '@vueuse/core'
// ---cut---
const { event, data } = useEventSource(
  'https://event-source-url',
  ['notice', 'update']
)
```

### immediate

Enable by default.

Establish the connection immediately when the composable is called.

### autoConnect

Enable by default.

If url is provided as a ref, when the url changes, it will automatically reconnect to the new url.

### Auto Reconnection on Errors

Reconnect on errors automatically (disabled by default).

```ts
import { useEventSource } from '@vueuse/core'
// ---cut---
const { status, data, close } = useEventSource(
  'https://event-source-url',
  [],
  {
    autoReconnect: true,
  }
)
```

Or with more controls over its behavior:

```ts
import { useEventSource } from '@vueuse/core'
// ---cut---
const { status, data, close } = useEventSource(
  'https://event-source-url',
  [],
  {
    autoReconnect: {
      retries: 3,
      delay: 1000,
      onFailed() {
        alert('Failed to connect EventSource after 3 retries')
      },
    },
  }
)
```

### Data Serialization

Apply custom transformations to incoming data using a serialization function.

```ts
import { useEventSource } from '@vueuse/core'
// ---cut---
const { data } = useEventSource(
  'https://event-source-url',
  [],
  {
    serializer: {
      read: rawData => JSON.parse(rawData),
    },
  }
)

// If server sends: '{"name":"John","age":30}'
// data.value will be: { name: 'John', age: 30 }
```

## Type Declarations

```ts
export type EventSourceStatus = "CONNECTING" | "OPEN" | "CLOSED"
export interface UseEventSourceOptions<Data> extends EventSourceInit {
  /**
   * Enabled auto reconnect
   *
   * @default false
   */
  autoReconnect?:
    | boolean
    | {
        /**
         * Maximum retry times.
         *
         * Or you can pass a predicate function (which returns true if you want to retry).
         *
         * @default -1
         */
        retries?: number | (() => boolean)
        /**
         * Delay for reconnect, in milliseconds
         *
         * @default 1000
         */
        delay?: number
        /**
         * On maximum retry times reached.
         */
        onFailed?: Fn
      }
  /**
   * Immediately open the connection when calling this composable
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Automatically connect to the websocket when URL changes
   *
   * @default true
   */
  autoConnect?: boolean
  /**
   * Custom data serialization
   */
  serializer?: {
    read: (v?: string) => Data
  }
}
export interface UseEventSourceReturn<Events extends string[], Data = any> {
  /**
   * Reference to the latest data received via the EventSource,
   * can be watched to respond to incoming messages
   */
  data: ShallowRef<Data | null>
  /**
   * The current state of the connection, can be only one of:
   * 'CONNECTING', 'OPEN' 'CLOSED'
   */
  status: ShallowRef<EventSourceStatus>
  /**
   * The latest named event
   */
  event: ShallowRef<Events[number] | null>
  /**
   * The current error
   */
  error: ShallowRef<Event | null>
  /**
   * Closes the EventSource connection gracefully.
   */
  close: EventSource["close"]
  /**
   * Reopen the EventSource connection.
   * If there the current one is active, will close it before opening a new one.
   */
  open: Fn
  /**
   * Reference to the current EventSource instance.
   */
  eventSource: Ref<EventSource | null>
  /**
   * The last event ID string, for server-sent events.
   * @see https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/lastEventId
   */
  lastEventId: ShallowRef<string | null>
}
/**
 * Reactive wrapper for EventSource.
 *
 * @see https://vueuse.org/useEventSource
 * @see https://developer.mozilla.org/en-US/docs/Web/API/EventSource/EventSource EventSource
 * @param url
 * @param events
 * @param options
 */
export declare function useEventSource<Events extends string[], Data = any>(
  url: MaybeRefOrGetter<string | URL | undefined>,
  events?: Events,
  options?: UseEventSourceOptions<Data>,
): UseEventSourceReturn<Events, Data>
```
```

## File: `skills/vueuse-functions/references/useExtractedObservable.md`
```markdown
---
category: '@RxJS'
---

# useExtractedObservable

Use an RxJS [`Observable`](https://rxjs.dev/guide/observable) as extracted from one or more composables, return a `ref`,
and automatically unsubscribe from it when the component is unmounted.

Automatically unsubscribe on observable change, and automatically unsubscribe from it when the component is unmounted.

Supports signatures that match all overloads
of [`watch`](https://vuejs.org/guide/essentials/watchers.html#basic-example).

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { useExtractedObservable } from '@vueuse/rxjs'
import ObservableSocket from 'observable-socket'
import { computed } from 'vue'
import { makeSocket, useUser } from '../some/lib/func'

// setup()
const user = useUser()
const lastMessage = useExtractedObservable(user, u => ObservableSocket.create(makeSocket(u.id)).down)
```

If you want to add custom error handling to an `Observable` that might error, you can supply an optional `onError`
configuration. Without this, RxJS will treat any error in the supplied `Observable` as an "unhandled error" and it will
be thrown in a new call stack and reported to `window.onerror` (or `process.on('error')` if you happen to be in Node).

```ts no-twoslash
import { useExtractedObservable } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { mapTo, scan, startWith, tap } from 'rxjs/operators'
import { shallowRef } from 'vue'

// setup()
const start = shallowRef(0)

const count = useExtractedObservable(
  start,
  (start) => {
    return interval(1000).pipe(
      mapTo(1),
      startWith(start),
      scan((total, next) => next + total),
      tap((n) => {
        if (n === 10)
          throw new Error('oops')
      })
    )
  },
  {
    onError: (err) => {
      console.log(err.message) // "oops"
    },
  }
)
```

You can also supply an optional `onComplete` configuration if you need to attach special behavior when the watched
observable completes.

```ts no-twoslash
import { useExtractedObservable } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { mapTo, scan, startWith, takeWhile } from 'rxjs/operators'
import { shallowRef } from 'vue'

// setup()
const start = shallowRef(0)

const count = useExtractedObservable(
  start,
  (start) => {
    return interval(1000).pipe(
      mapTo(1),
      startWith(start),
      scan((total, next) => next + total),
      takeWhile(num => num < 10)
    )
  },
  {
    onComplete: () => {
      console.log('Done!')
    },
  }
)
```

If you want, you can also pass `watch` options as the last argument:

```ts no-twoslash
import { useExtractedObservable } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { mapTo, scan, startWith, takeWhile } from 'rxjs/operators'
import { shallowRef } from 'vue'

// setup()
const start = shallowRef<number>()

const count = useExtractedObservable(
  start,
  (start) => {
    return interval(1000).pipe(
      mapTo(1),
      startWith(start),
      scan((total, next) => next + total),
      takeWhile(num => num < 10)
    )
  },
  {},
  {
    immediate: false
  }
)
```

## Options

| Option         | Type                 | Description                              |
| -------------- | -------------------- | ---------------------------------------- |
| `initialValue` | `T`                  | Value to use before the Observable emits |
| `onError`      | `(err: any) => void` | Error handler for Observable errors      |
| `onComplete`   | `() => void`         | Called when the Observable completes     |

## Return Value

Returns a readonly `ShallowRef` containing the latest value emitted by the extracted Observable.

## Type Declarations

```ts
export interface UseExtractedObservableOptions<
  E,
> extends UseObservableOptions<E> {
  onComplete?: () => void
}
export declare function useExtractedObservable<
  T extends MultiWatchSources,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  extractor: WatchExtractedObservableCallback<
    MapSources<T>,
    MapOldSources<T, Immediate>,
    E
  >,
  options?: UseExtractedObservableOptions<E>,
  watchOptions?: WatchOptions<Immediate>,
): Readonly<ShallowRef<E>>
export declare function useExtractedObservable<
  T extends Readonly<MultiWatchSources>,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  sources: T,
  extractor: WatchExtractedObservableCallback<
    MapSources<T>,
    MapOldSources<T, Immediate>,
    E
  >,
  options?: UseExtractedObservableOptions<E>,
  watchOptions?: WatchOptions<Immediate>,
): Readonly<ShallowRef<E>>
export declare function useExtractedObservable<
  T,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  sources: WatchSource<T>,
  extractor: WatchExtractedObservableCallback<
    T,
    Immediate extends true ? T | undefined : T,
    E
  >,
  options?: UseExtractedObservableOptions<E>,
  watchOptions?: WatchOptions<Immediate>,
): Readonly<ShallowRef<E>>
export declare function useExtractedObservable<
  T extends object,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  sources: T,
  extractor: WatchExtractedObservableCallback<
    T,
    Immediate extends true ? T | undefined : T,
    E
  >,
  options?: UseExtractedObservableOptions<E>,
  watchOptions?: WatchOptions<Immediate>,
): Readonly<ShallowRef<E>>
```
```

## File: `skills/vueuse-functions/references/useEyeDropper.md`
```markdown
---
category: Browser
---

# useEyeDropper

Reactive [EyeDropper API](https://developer.mozilla.org/en-US/docs/Web/API/EyeDropper_API)

## Usage

```ts
import { useEyeDropper } from '@vueuse/core'

const { isSupported, open, sRGBHex } = useEyeDropper()
```

## Component Usage

```vue
<template>
  <UseEyeDropper v-slot="{ isSupported, sRGBHex, open }">
    <button :disabled="!isSupported" @click="() => open()">
      sRGBHex: {{ sRGBHex }}
    </button>
  </UseEyeDropper>
</template>
```

## Type Declarations

```ts
export interface EyeDropperOpenOptions {
  /**
   * @see https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal
   */
  signal?: AbortSignal
}
export interface EyeDropper {
  new (): EyeDropper
  open: (options?: EyeDropperOpenOptions) => Promise<{
    sRGBHex: string
  }>
  [Symbol.toStringTag]: "EyeDropper"
}
export interface UseEyeDropperOptions {
  /**
   * Initial sRGBHex.
   *
   * @default ''
   */
  initialValue?: string
}
export interface UseEyeDropperReturn extends Supportable {
  sRGBHex: ShallowRef<string>
  open: (openOptions?: EyeDropperOpenOptions) => Promise<
    | {
        sRGBHex: string
      }
    | undefined
  >
}
/**
 * Reactive [EyeDropper API](https://developer.mozilla.org/en-US/docs/Web/API/EyeDropper_API)
 *
 * @see https://vueuse.org/useEyeDropper
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useEyeDropper(
  options?: UseEyeDropperOptions,
): UseEyeDropperReturn
```
```

## File: `skills/vueuse-functions/references/useFavicon.md`
```markdown
---
category: Browser
---

# useFavicon

Reactive favicon

## Usage

```ts {3}
import { useFavicon } from '@vueuse/core'

const icon = useFavicon()

icon.value = 'dark.png' // change current icon
```

### Passing a source ref

You can pass a `ref` to it, changes from of the source ref will be reflected to your favicon automatically.

```ts {7}
import { useFavicon, usePreferredDark } from '@vueuse/core'
import { computed } from 'vue'

const isDark = usePreferredDark()
const favicon = computed(() => isDark.value ? 'dark.png' : 'light.png')

useFavicon(favicon)
```

When a source ref is passed, the return ref will be identical to the source ref

```ts
import { useFavicon } from '@vueuse/core'
// ---cut---
const source = shallowRef('icon.png')
const icon = useFavicon(source)

console.log(icon === source) // true
```

## Type Declarations

```ts
export interface UseFaviconOptions extends ConfigurableDocument {
  baseUrl?: string
  rel?: string
}
export type UseFaviconReturn =
  | ComputedRef<string | null | undefined>
  | Ref<string | null | undefined>
/**
 * Reactive favicon.
 *
 * @see https://vueuse.org/useFavicon
 * @param newIcon
 * @param options
 */
export declare function useFavicon(
  newIcon: ReadonlyRefOrGetter<string | null | undefined>,
  options?: UseFaviconOptions,
): ComputedRef<string | null | undefined>
export declare function useFavicon(
  newIcon?: MaybeRef<string | null | undefined>,
  options?: UseFaviconOptions,
): Ref<string | null | undefined>
```
```

## File: `skills/vueuse-functions/references/useFetch.md`
```markdown
---
category: Network
---

# useFetch

Reactive [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) provides the ability to abort requests, intercept requests before
they are fired, automatically refetch requests when the url changes, and create your own `useFetch` with predefined options.

<CourseLink href="https://vueschool.io/lessons/vueuse-utilities-usefetch-and-reactify?friend=vueuse">Learn useFetch with this FREE video lesson from Vue School!</CourseLink>

::: tip
When using with Nuxt 3, this function will **NOT** be auto imported in favor of Nuxt's built-in [`useFetch()`](https://v3.nuxtjs.org/api/composables/use-fetch). Use explicit import if you want to use the function from VueUse.
:::

## Usage

### Basic Usage

The `useFetch` function can be used by simply providing a url. The url can be either a string or a `ref`. The `data` object will contain the result of the request, the `error` object will contain any errors, and the `isFetching` object will indicate if the request is loading.

```ts
import { useFetch } from '@vueuse/core'

const { isFetching, error, data } = useFetch(url)
```

### Asynchronous Usage

`useFetch` can also be awaited just like a normal fetch. Note that whenever a component is asynchronous, whatever component that uses
it must wrap the component in a `<Suspense>` tag. You can read more about the suspense api in the [Official Vue 3 Docs](https://vuejs.org/guide/built-ins/suspense.html)

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { isFetching, error, data } = await useFetch(url)
```

### Refetching on URL change

Using a `ref` for the url parameter will allow the `useFetch` function to automatically trigger another request when the url is changed.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const url = ref('https://my-api.com/user/1')

const { data } = useFetch(url, { refetch: true })

url.value = 'https://my-api.com/user/2' // Will trigger another request
```

### Prevent request from firing immediately

Setting the `immediate` option to false will prevent the request from firing until the `execute` function is called.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { execute } = useFetch(url, { immediate: false })

execute()
```

### Aborting a request

A request can be aborted by using the `abort` function from the `useFetch` function. The `canAbort` property indicates if the request can be aborted.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { abort, canAbort } = useFetch(url)

setTimeout(() => {
  if (canAbort.value)
    abort()
}, 100)
```

A request can also be aborted automatically by using `timeout` property. It will call `abort` function when the given timeout is reached.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { data } = useFetch(url, { timeout: 100 })
```

### Intercepting a request

The `beforeFetch` option can intercept a request before it is sent and modify the request options and url.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { data } = useFetch(url, {
  async beforeFetch({ url, options, cancel }) {
    const myToken = await getMyToken()

    if (!myToken)
      cancel()

    options.headers = {
      ...options.headers,
      Authorization: `Bearer ${myToken}`,
    }

    return {
      options,
    }
  },
})
```

The `afterFetch` option can intercept the response data before it is updated.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { data } = useFetch(url, {
  afterFetch(ctx) {
    if (ctx.data.title === 'HxH')
      ctx.data.title = 'Hunter x Hunter' // Modifies the response data

    return ctx
  },
})
```

The `onFetchError` option can intercept the response data and error before it is updated when `updateDataOnError` is set to `true`.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { data } = useFetch(url, {
  updateDataOnError: true,
  onFetchError(ctx) {
    // ctx.data can be null when 5xx response
    if (ctx.data === null)
      ctx.data = { title: 'Hunter x Hunter' } // Modifies the response data

    ctx.error = new Error('Custom Error') // Modifies the error
    return ctx
  },
})

console.log(data.value) // { title: 'Hunter x Hunter' }
```

### Setting the request method and return type

The request method and return type can be set by adding the appropriate methods to the end of `useFetch`

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
// Request will be sent with GET method and data will be parsed as JSON
const { data } = useFetch(url).get().json()

// Request will be sent with POST method and data will be parsed as text
const { data } = useFetch(url).post().text()

// Or set the method using the options

// Request will be sent with GET method and data will be parsed as blob
const { data } = useFetch(url, { method: 'GET' }, { refetch: true }).blob()
```

### Creating a Custom Instance

The `createFetch` function will return a useFetch function with whatever pre-configured options that are provided to it. This is useful for interacting with API's throughout an application that uses the same base URL or needs Authorization headers.

```ts
import { createFetch } from '@vueuse/core'
// ---cut---
const useMyFetch = createFetch({
  baseUrl: 'https://my-api.com',
  options: {
    async beforeFetch({ options }) {
      const myToken = await getMyToken()
      options.headers.Authorization = `Bearer ${myToken}`

      return { options }
    },
  },
  fetchOptions: {
    mode: 'cors',
  },
})

const { isFetching, error, data } = useMyFetch('users')
```

If you want to control the behavior of `beforeFetch`, `afterFetch`, `onFetchError` between the pre-configured instance and newly spawned instance. You can provide a `combination` option to toggle between `overwrite` or `chaining`.

```ts
import { createFetch } from '@vueuse/core'
// ---cut---
const useMyFetch = createFetch({
  baseUrl: 'https://my-api.com',
  combination: 'overwrite',
  options: {
    // beforeFetch in pre-configured instance will only run when the newly spawned instance do not pass beforeFetch
    async beforeFetch({ options }) {
      const myToken = await getMyToken()
      options.headers.Authorization = `Bearer ${myToken}`

      return { options }
    },
  },
})

// use useMyFetch beforeFetch
const { isFetching, error, data } = useMyFetch('users')

// use custom beforeFetch
const { isFetching, error, data } = useMyFetch('users', {
  async beforeFetch({ url, options, cancel }) {
    const myToken = await getMyToken()

    if (!myToken)
      cancel()

    options.headers = {
      ...options.headers,
      Authorization: `Bearer ${myToken}`,
    }

    return {
      options,
    }
  },
})
```

You can re-execute the request by calling the `execute` method in `afterFetch` or `onFetchError`. Here is a simple example of refreshing a token:

```ts
import { createFetch } from '@vueuse/core'
// ---cut---
let isRefreshing = false
const refreshSubscribers: Array<() => void> = []

const useMyFetch = createFetch({
  baseUrl: 'https://my-api.com',
  options: {
    async beforeFetch({ options }) {
      const myToken = await getMyToken()
      options.headers.Authorization = `Bearer ${myToken}`

      return { options }
    },
    afterFetch({ data, response, context, execute }) {
      if (needRefreshToken) {
        if (!isRefreshing) {
          isRefreshing = true
          refreshToken().then((newToken) => {
            if (newToken.value) {
              isRefreshing = false
              setMyToken(newToken.value)
              onRefreshed()
            }
            else {
              refreshSubscribers.length = 0
              // handle refresh token error
            }
          })
        }

        return new Promise((resolve) => {
          addRefreshSubscriber(() => {
            execute().then((response) => {
              resolve({ data, response })
            })
          })
        })
      }

      return { data, response }
    },
    // or use onFetchError with updateDataOnError
    updateDataOnError: true,
    onFetchError({ error, data, response, context, execute }) {
      // same as afterFetch
      return { error, data }
    },
  },
  fetchOptions: {
    mode: 'cors',
  },
})

async function refreshToken() {
  const { data, execute } = useFetch<string>('refresh-token', {
    immediate: false,
  })

  await execute()
  return data
}

function onRefreshed() {
  refreshSubscribers.forEach(callback => callback())
  refreshSubscribers.length = 0
}

function addRefreshSubscriber(callback: () => void) {
  refreshSubscribers.push(callback)
}

const { isFetching, error, data } = useMyFetch('users')
```

### Events

The `onFetchResponse` and `onFetchError` will fire on fetch request responses and errors respectively.

```ts
import { useFetch } from '@vueuse/core'
// ---cut---
const { onFetchResponse, onFetchError } = useFetch(url)

onFetchResponse((response) => {
  console.log(response.status)
})

onFetchError((error) => {
  console.error(error.message)
})
```

## Type Declarations

```ts
export interface UseFetchReturn<T> {
  /**
   * Indicates if the fetch request has finished
   */
  isFinished: Readonly<ShallowRef<boolean>>
  /**
   * The statusCode of the HTTP fetch response
   */
  statusCode: ShallowRef<number | null>
  /**
   * The raw response of the fetch response
   */
  response: ShallowRef<Response | null>
  /**
   * Any fetch errors that may have occurred
   */
  error: ShallowRef<any>
  /**
   * The fetch response body on success, may either be JSON or text
   */
  data: ShallowRef<T | null>
  /**
   * Indicates if the request is currently being fetched.
   */
  isFetching: Readonly<ShallowRef<boolean>>
  /**
   * Indicates if the fetch request is able to be aborted
   */
  canAbort: ComputedRef<boolean>
  /**
   * Indicates if the fetch request was aborted
   */
  aborted: ShallowRef<boolean>
  /**
   * Abort the fetch request
   */
  abort: (reason?: any) => void
  /**
   * Manually call the fetch
   * (default not throwing error)
   */
  execute: (throwOnFailed?: boolean) => Promise<any>
  /**
   * Fires after the fetch request has finished
   */
  onFetchResponse: EventHookOn<Response>
  /**
   * Fires after a fetch request error
   */
  onFetchError: EventHookOn
  /**
   * Fires after a fetch has completed
   */
  onFetchFinally: EventHookOn
  get: () => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  post: (
    payload?: MaybeRefOrGetter<unknown>,
    type?: string,
  ) => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  put: (
    payload?: MaybeRefOrGetter<unknown>,
    type?: string,
  ) => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  delete: (
    payload?: MaybeRefOrGetter<unknown>,
    type?: string,
  ) => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  patch: (
    payload?: MaybeRefOrGetter<unknown>,
    type?: string,
  ) => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  head: (
    payload?: MaybeRefOrGetter<unknown>,
    type?: string,
  ) => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  options: (
    payload?: MaybeRefOrGetter<unknown>,
    type?: string,
  ) => UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
  json: <JSON = any>() => UseFetchReturn<JSON> &
    PromiseLike<UseFetchReturn<JSON>>
  text: () => UseFetchReturn<string> & PromiseLike<UseFetchReturn<string>>
  blob: () => UseFetchReturn<Blob> & PromiseLike<UseFetchReturn<Blob>>
  arrayBuffer: () => UseFetchReturn<ArrayBuffer> &
    PromiseLike<UseFetchReturn<ArrayBuffer>>
  formData: () => UseFetchReturn<FormData> &
    PromiseLike<UseFetchReturn<FormData>>
}
type Combination = "overwrite" | "chain"
export interface BeforeFetchContext {
  /**
   * The computed url of the current request
   */
  url: string
  /**
   * The request options of the current request
   */
  options: RequestInit
  /**
   * Cancels the current request
   */
  cancel: Fn
}
export interface AfterFetchContext<T = any> {
  response: Response
  data: T | null
  context: BeforeFetchContext
  execute: (throwOnFailed?: boolean) => Promise<any>
}
export interface OnFetchErrorContext<T = any, E = any> {
  error: E
  data: T | null
  response: Response | null
  context: BeforeFetchContext
  execute: (throwOnFailed?: boolean) => Promise<any>
}
export interface UseFetchOptions {
  /**
   * Fetch function
   */
  fetch?: typeof window.fetch
  /**
   * Will automatically run fetch when `useFetch` is used
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Will automatically refetch when:
   * - the URL is changed if the URL is a ref
   * - the payload is changed if the payload is a ref
   *
   * @default false
   */
  refetch?: MaybeRefOrGetter<boolean>
  /**
   * Initial data before the request finished
   *
   * @default null
   */
  initialData?: any
  /**
   * Timeout for abort request after number of millisecond
   * `0` means use browser default
   *
   * @default 0
   */
  timeout?: number
  /**
   * Allow update the `data` ref when fetch error whenever provided, or mutated in the `onFetchError` callback
   *
   * @default false
   */
  updateDataOnError?: boolean
  /**
   * Will run immediately before the fetch request is dispatched
   */
  beforeFetch?: (
    ctx: BeforeFetchContext,
  ) =>
    | Promise<Partial<BeforeFetchContext> | void>
    | Partial<BeforeFetchContext>
    | void
  /**
   * Will run immediately after the fetch request is returned.
   * Runs after any 2xx response
   */
  afterFetch?: (
    ctx: AfterFetchContext,
  ) => Promise<Partial<AfterFetchContext>> | Partial<AfterFetchContext>
  /**
   * Will run immediately after the fetch request is returned.
   * Runs after any 4xx and 5xx response
   */
  onFetchError?: (
    ctx: OnFetchErrorContext,
  ) => Promise<Partial<OnFetchErrorContext>> | Partial<OnFetchErrorContext>
}
export interface CreateFetchOptions {
  /**
   * The base URL that will be prefixed to all urls unless urls are absolute
   */
  baseUrl?: MaybeRefOrGetter<string>
  /**
   * Determine the inherit behavior for beforeFetch, afterFetch, onFetchError
   * @default 'chain'
   */
  combination?: Combination
  /**
   * Default Options for the useFetch function
   */
  options?: UseFetchOptions
  /**
   * Options for the fetch request
   */
  fetchOptions?: RequestInit
}
export declare function createFetch(
  config?: CreateFetchOptions,
): typeof useFetch
export declare function useFetch<T>(
  url: MaybeRefOrGetter<string>,
): UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
export declare function useFetch<T>(
  url: MaybeRefOrGetter<string>,
  useFetchOptions: UseFetchOptions,
): UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
export declare function useFetch<T>(
  url: MaybeRefOrGetter<string>,
  options: RequestInit,
  useFetchOptions?: UseFetchOptions,
): UseFetchReturn<T> & PromiseLike<UseFetchReturn<T>>
```
```

## File: `skills/vueuse-functions/references/useFileDialog.md`
```markdown
---
category: Browser
---

# useFileDialog

Open file dialog with ease.

## Usage

```vue
<script setup lang="ts">
import { useFileDialog } from '@vueuse/core'

const { files, open, reset, onCancel, onChange } = useFileDialog({
  accept: 'image/*', // Set to accept only image files
  directory: true, // Select directories instead of files if set true
})

onChange((files) => {
  /** do something with files */
})

onCancel(() => {
  /** do something on cancel */
})
</script>

<template>
  <button type="button" @click="open">
    Choose file
  </button>
</template>
```

## Type Declarations

```ts
export interface UseFileDialogOptions extends ConfigurableDocument {
  /**
   * @default true
   */
  multiple?: MaybeRef<boolean>
  /**
   * @default '*'
   */
  accept?: MaybeRef<string>
  /**
   * Select the input source for the capture file.
   * @see [HTMLInputElement Capture](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/capture)
   */
  capture?: MaybeRef<string>
  /**
   * Reset when open file dialog.
   * @default false
   */
  reset?: MaybeRef<boolean>
  /**
   * Select directories instead of files.
   * @see [HTMLInputElement webkitdirectory](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/webkitdirectory)
   * @default false
   */
  directory?: MaybeRef<boolean>
  /**
   * Initial files to set.
   * @default null
   */
  initialFiles?: Array<File> | FileList
  /**
   * The input element to use for file dialog.
   * @default document.createElement('input')
   */
  input?: MaybeElementRef<HTMLInputElement>
}
export interface UseFileDialogReturn {
  files: Ref<FileList | null>
  open: (localOptions?: Partial<UseFileDialogOptions>) => void
  reset: () => void
  onChange: EventHookOn<FileList | null>
  onCancel: EventHookOn
}
/**
 * Open file dialog with ease.
 *
 * @see https://vueuse.org/useFileDialog
 * @param options
 */
export declare function useFileDialog(
  options?: UseFileDialogOptions,
): UseFileDialogReturn
```
```

## File: `skills/vueuse-functions/references/useFileSystemAccess.md`
```markdown
---
category: Browser
---

# useFileSystemAccess

Create and read and write local files with [FileSystemAccessAPI](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API)

## Usage

```ts
import { useFileSystemAccess } from '@vueuse/core'

const {
  isSupported,
  data,
  file,
  fileName,
  fileMIME,
  fileSize,
  fileLastModified,
  create,
  open,
  save,
  saveAs,
  updateData
} = useFileSystemAccess()
```

## Type Declarations

```ts
/**
 * window.showOpenFilePicker parameters
 * @see https://developer.mozilla.org/en-US/docs/Web/API/window/showOpenFilePicker#parameters
 */
export interface FileSystemAccessShowOpenFileOptions {
  multiple?: boolean
  types?: Array<{
    description?: string
    accept: Record<string, string[]>
  }>
  excludeAcceptAllOption?: boolean
}
/**
 * window.showSaveFilePicker parameters
 * @see https://developer.mozilla.org/en-US/docs/Web/API/window/showSaveFilePicker#parameters
 */
export interface FileSystemAccessShowSaveFileOptions {
  suggestedName?: string
  types?: Array<{
    description?: string
    accept: Record<string, string[]>
  }>
  excludeAcceptAllOption?: boolean
}
/**
 * FileHandle
 * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemFileHandle
 */
export interface FileSystemFileHandle {
  getFile: () => Promise<File>
  createWritable: () => FileSystemWritableFileStream
}
/**
 * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream
 */
interface FileSystemWritableFileStream extends WritableStream {
  /**
   * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream/write
   */
  write: FileSystemWritableFileStreamWrite
  /**
   * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream/seek
   */
  seek: (position: number) => Promise<void>
  /**
   * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream/truncate
   */
  truncate: (size: number) => Promise<void>
}
/**
 * FileStream.write
 * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream/write
 */
interface FileSystemWritableFileStreamWrite {
  (data: string | BufferSource | Blob): Promise<void>
  (options: {
    type: "write"
    position: number
    data: string | BufferSource | Blob
  }): Promise<void>
  (options: { type: "seek"; position: number }): Promise<void>
  (options: { type: "truncate"; size: number }): Promise<void>
}
/**
 * FileStream.write
 * @see https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream/write
 */
export type FileSystemAccessWindow = Window & {
  showSaveFilePicker: (
    options: FileSystemAccessShowSaveFileOptions,
  ) => Promise<FileSystemFileHandle>
  showOpenFilePicker: (
    options: FileSystemAccessShowOpenFileOptions,
  ) => Promise<FileSystemFileHandle[]>
}
export type UseFileSystemAccessCommonOptions = Pick<
  FileSystemAccessShowOpenFileOptions,
  "types" | "excludeAcceptAllOption"
>
export type UseFileSystemAccessShowSaveFileOptions = Pick<
  FileSystemAccessShowSaveFileOptions,
  "suggestedName"
>
export type UseFileSystemAccessOptions = ConfigurableWindow &
  UseFileSystemAccessCommonOptions & {
    /**
     * file data type
     */
    dataType?: MaybeRefOrGetter<"Text" | "ArrayBuffer" | "Blob">
  }
/**
 * Create and read and write local files.
 * @see https://vueuse.org/useFileSystemAccess
 */
export declare function useFileSystemAccess(): UseFileSystemAccessReturn<
  string | ArrayBuffer | Blob
>
export declare function useFileSystemAccess(
  options: UseFileSystemAccessOptions & {
    dataType: "Text"
  },
): UseFileSystemAccessReturn<string>
export declare function useFileSystemAccess(
  options: UseFileSystemAccessOptions & {
    dataType: "ArrayBuffer"
  },
): UseFileSystemAccessReturn<ArrayBuffer>
export declare function useFileSystemAccess(
  options: UseFileSystemAccessOptions & {
    dataType: "Blob"
  },
): UseFileSystemAccessReturn<Blob>
export declare function useFileSystemAccess(
  options: UseFileSystemAccessOptions,
): UseFileSystemAccessReturn<string | ArrayBuffer | Blob>
export interface UseFileSystemAccessReturn<T = string> extends Supportable {
  data: ShallowRef<T | undefined>
  file: ShallowRef<File | undefined>
  fileName: ComputedRef<string>
  fileMIME: ComputedRef<string>
  fileSize: ComputedRef<number>
  fileLastModified: ComputedRef<number>
  open: (_options?: UseFileSystemAccessCommonOptions) => Awaitable<void>
  create: (_options?: UseFileSystemAccessShowSaveFileOptions) => Awaitable<void>
  save: (_options?: UseFileSystemAccessShowSaveFileOptions) => Awaitable<void>
  saveAs: (_options?: UseFileSystemAccessShowSaveFileOptions) => Awaitable<void>
  updateData: () => Awaitable<void>
}
```
```

## File: `skills/vueuse-functions/references/useFirestore.md`
```markdown
---
category: '@Firebase'
---

# useFirestore

Reactive [Firestore](https://firebase.google.com/docs/firestore) binding. Making it straightforward to **always keep your local data in sync** with remotes databases.

## Usage

```ts {9,12,17,22}
import { useFirestore } from '@vueuse/firebase/useFirestore'
import { initializeApp } from 'firebase/app'
import { collection, doc, getFirestore, limit, orderBy, query } from 'firebase/firestore'
import { computed, shallowRef } from 'vue'

const app = initializeApp({ projectId: 'MY PROJECT ID' })
const db = getFirestore(app)

const todos = useFirestore(collection(db, 'todos'))

// or for doc reference
const user = useFirestore(doc(db, 'users', 'my-user-id'))

// you can also use ref value for reactive query
const postsLimit = shallowRef(10)
const postsQuery = computed(() => query(collection(db, 'posts'), orderBy('createdAt', 'desc'), limit(postsLimit.value)))
const posts = useFirestore(postsQuery)

// you can use the boolean value to tell a query when it is ready to run
// when it gets falsy value, return the initial value
const userId = shallowRef('')
const userQuery = computed(() => userId.value && doc(db, 'users', userId.value))
const userData = useFirestore(userQuery, null)
```

### Return Value

- For **Document Reference**: Returns `Ref<T | null>` (single document with `id` property)
- For **Query**: Returns `Ref<T[]>` (array of documents, each with `id` property)

The document `id` is automatically added as a read-only property to each returned document.

### Options

| Option         | Type                   | Default         | Description                                                                |
| -------------- | ---------------------- | --------------- | -------------------------------------------------------------------------- |
| `errorHandler` | `(err: Error) => void` | `console.error` | Custom error handler                                                       |
| `autoDispose`  | `boolean \| number`    | `true`          | Auto-unsubscribe on scope dispose. Pass a number for delayed dispose (ms). |

### Error Handling

```ts
const todos = useFirestore(collection(db, 'todos'), [], {
  errorHandler: (err) => {
    console.error('Firestore error:', err)
    // Handle error (e.g., show notification)
  },
})
```

## Share across instances

You can reuse the db reference by passing `autoDispose: false`. You can also set an amount of milliseconds before auto disposing the db reference.

Note : Getting a not disposed db reference again don't cost a Firestore read.

```ts
import { useFirestore } from '@vueuse/firebase/useFirestore'
import { collection } from 'firebase/firestore'
// ---cut---
const todos = useFirestore(collection(db, 'todos'), undefined, { autoDispose: false })
```

or use `createGlobalState` from the core package

```ts twoslash include store
// @filename: store.ts
// ---cut---
// store.ts
import { createGlobalState } from '@vueuse/core'
import { useFirestore } from '@vueuse/firebase/useFirestore'

export const useTodos = createGlobalState(
  () => useFirestore(collection(db, 'todos')),
)
```

```vue
<!-- app.vue -->
<script setup lang="ts">
// @include: store
// ---cut---
import { useTodos } from './store'

const todos = useTodos()
</script>
```

## Type Declarations

```ts
export interface UseFirestoreOptions {
  errorHandler?: (err: Error) => void
  autoDispose?: boolean | number
}
export type FirebaseDocRef<T> = Query<T> | DocumentReference<T>
type Falsy = false | 0 | "" | null | undefined
export declare function useFirestore<T extends DocumentData>(
  maybeDocRef: MaybeRef<DocumentReference<T> | Falsy>,
  initialValue: T,
  options?: UseFirestoreOptions,
): Ref<T | null>
export declare function useFirestore<T extends DocumentData>(
  maybeDocRef: MaybeRef<Query<T> | Falsy>,
  initialValue: T[],
  options?: UseFirestoreOptions,
): Ref<T[]>
export declare function useFirestore<T extends DocumentData>(
  maybeDocRef: MaybeRef<DocumentReference<T> | Falsy>,
  initialValue?: T | undefined | null,
  options?: UseFirestoreOptions,
): Ref<T | undefined | null>
export declare function useFirestore<T extends DocumentData>(
  maybeDocRef: MaybeRef<Query<T> | Falsy>,
  initialValue?: T[],
  options?: UseFirestoreOptions,
): Ref<T[] | undefined>
```
```

## File: `skills/vueuse-functions/references/useFloor.md`
```markdown
---
category: '@Math'
---

# useFloor

Reactive `Math.floor`.

## Usage

```ts
import { useFloor } from '@vueuse/math'

const value = ref(45.95)
const result = useFloor(value) // 45
```

## Type Declarations

```ts
/**
 * Reactive `Math.floor`
 *
 * @see https://vueuse.org/useFloor
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useFloor(
  value: MaybeRefOrGetter<number>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useFocus.md`
```markdown
---
category: Sensors
---

# useFocus

Reactive utility to track or set the focus state of a DOM element. State changes to reflect whether the target element is the focused element. Setting reactive value from the outside will trigger `focus` and `blur` events for `true` and `false` values respectively.

## Basic Usage

```ts
import { useFocus } from '@vueuse/core'

const target = shallowRef()
const { focused } = useFocus(target)

watch(focused, (focused) => {
  if (focused)
    console.log('input element has been focused')
  else console.log('input element has lost focus')
})
```

## Setting initial focus

To focus the element on its first render one can provide the `initialValue` option as `true`. This will trigger a `focus` event on the target element.

```ts
import { useFocus } from '@vueuse/core'

const target = shallowRef()
const { focused } = useFocus(target, { initialValue: true })
```

## Change focus state

Changes of the `focused` reactive ref will automatically trigger `focus` and `blur` events for `true` and `false` values respectively. You can utilize this behavior to focus the target element as a result of another action (e.g. when a button click as shown below).

```vue
<script setup lang="ts">
import { useFocus } from '@vueuse/core'
import { shallowRef } from 'vue'

const input = shallowRef()
const { focused } = useFocus(input)
</script>

<template>
  <div>
    <button type="button" @click="focused = true">
      Click me to focus input below
    </button>
    <input ref="input" type="text">
  </div>
</template>
```

## Type Declarations

```ts
export interface UseFocusOptions extends ConfigurableWindow {
  /**
   * Initial value. If set true, then focus will be set on the target
   *
   * @default false
   */
  initialValue?: boolean
  /**
   * Replicate the :focus-visible behavior of CSS
   *
   * @default false
   */
  focusVisible?: boolean
  /**
   * Prevent scrolling to the element when it is focused.
   *
   * @default false
   */
  preventScroll?: boolean
}
export interface UseFocusReturn {
  /**
   * If read as true, then the element has focus. If read as false, then the element does not have focus
   * If set to true, then the element will be focused. If set to false, the element will be blurred.
   */
  focused: WritableComputedRef<boolean>
}
/**
 * Track or set the focus state of a DOM element.
 *
 * @see https://vueuse.org/useFocus
 * @param target The target element for the focus and blur events.
 * @param options
 */
export declare function useFocus(
  target: MaybeElementRef,
  options?: UseFocusOptions,
): UseFocusReturn
```
```

## File: `skills/vueuse-functions/references/useFocusTrap.md`
```markdown
---
category: '@Integrations'
---

# useFocusTrap

Reactive wrapper for [`focus-trap`](https://github.com/focus-trap/focus-trap).

For more information on what options can be passed, see [`createOptions`](https://github.com/focus-trap/focus-trap#createoptions) in the `focus-trap` documentation.

## Install

```bash
npm i focus-trap@^7
```

## Usage

**Basic Usage**

```vue
<script setup lang="ts">
import { useFocusTrap } from '@vueuse/integrations/useFocusTrap'
import { useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const { hasFocus, activate, deactivate } = useFocusTrap(target)
</script>

<template>
  <div>
    <button @click="activate()">
      Activate
    </button>
    <div ref="target">
      <span>Has Focus: {{ hasFocus }}</span>
      <input type="text">
      <button @click="deactivate()">
        Deactivate
      </button>
    </div>
  </div>
</template>
```

**Multiple Refs**

```vue
<script setup lang="ts">
import { useFocusTrap } from '@vueuse/integrations/useFocusTrap'
import { useTemplateRef } from 'vue'

const targetOne = useTemplateRef('targetOne')
const targetTwo = useTemplateRef('targetTwo')
const { hasFocus, activate, deactivate } = useFocusTrap([targetOne, targetTwo])
</script>

<template>
  <div>
    <button @click="activate()">
      Activate
    </button>
    <div ref="targetOne">
      <span>Has Focus: {{ hasFocus }}</span>
      <input type="text">
    </div>
    ...
    <div ref="targetTow">
      <p>Another target here</p>
      <input type="text">
      <button @click="deactivate()">
        Deactivate
      </button>
    </div>
  </div>
</template>
```

**Dynamic Focus Target**

```vue
<script setup lang="ts">
import { useFocusTrap } from '@vueuse/integrations/useFocusTrap'
import { computed, shallowRef, useTemplateRef } from 'vue'

const left = useTemplateRef('left')
const right = useTemplateRef('right')
const currentRef = shallowRef<'left' | 'right'>('left')

const target = computed(() =>
  currentRef.value === 'left'
    ? left
    : currentRef.value === 'right'
      ? right
      : null,
)

const { activate } = useFocusTrap(target)
</script>

<template>
  <div>
    <div ref="left" class="left">
      ...
    </div>
    <div ref="right" class="right">
      ...
    </div>
  </div>
</template>
```

**Automatically Focus**

```vue
<script setup lang="ts">
import { useFocusTrap } from '@vueuse/integrations/useFocusTrap'
import { useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const { hasFocus, activate, deactivate } = useFocusTrap(target, { immediate: true })
</script>

<template>
  <div>
    <div ref="target">
      ...
    </div>
  </div>
</template>
```

**Conditional Rendering**

This function can't properly activate focus on elements with conditional rendering using `v-if`. This is because they do not exist in the DOM at the time of the focus activation. To solve this you need to activate on the next tick.

```vue
<script setup lang="ts">
import { useFocusTrap } from '@vueuse/integrations/useFocusTrap'
import { nextTick, useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const { activate, deactivate } = useFocusTrap(target, { immediate: true })

const show = ref(false)

async function reveal() {
  show.value = true

  await nextTick()
  activate()
}
</script>

<template>
  <div>
    <div v-if="show" ref="target">
      ...
    </div>

    <button @click="reveal">
      Reveal and Focus
    </button>
  </div>
</template>
```

## Using Component

With the `UseFocusTrap` component, Focus Trap will be activated automatically on mounting this component and deactivated on unmount.

```vue
<script setup lang="ts">
import { UseFocusTrap } from '@vueuse/integrations/useFocusTrap/component'
import { shallowRef } from 'vue'

const show = shallowRef(false)
</script>

<template>
  <UseFocusTrap v-if="show" :options="{ immediate: true }">
    <div class="modal">
      ...
    </div>
  </UseFocusTrap>
</template>
```

## Type Declarations

```ts
export interface UseFocusTrapOptions extends Options {
  /**
   * Immediately activate the trap
   */
  immediate?: boolean
}
export interface UseFocusTrapReturn {
  /**
   * Indicates if the focus trap is currently active
   */
  hasFocus: ShallowRef<boolean>
  /**
   * Indicates if the focus trap is currently paused
   */
  isPaused: ShallowRef<boolean>
  /**
   * Activate the focus trap
   *
   * @see https://github.com/focus-trap/focus-trap#trapactivateactivateoptions
   * @param opts Activate focus trap options
   */
  activate: (opts?: ActivateOptions) => void
  /**
   * Deactivate the focus trap
   *
   * @see https://github.com/focus-trap/focus-trap#trapdeactivatedeactivateoptions
   * @param opts Deactivate focus trap options
   */
  deactivate: (opts?: DeactivateOptions) => void
  /**
   * Pause the focus trap
   *
   * @see https://github.com/focus-trap/focus-trap#trappause
   */
  pause: Fn
  /**
   * Unpauses the focus trap
   *
   * @see https://github.com/focus-trap/focus-trap#trapunpause
   */
  unpause: Fn
}
/**
 * Reactive focus-trap
 *
 * @see https://vueuse.org/useFocusTrap
 */
export declare function useFocusTrap(
  target: MaybeRefOrGetter<
    Arrayable<MaybeRefOrGetter<string> | MaybeComputedElementRef>
  >,
  options?: UseFocusTrapOptions,
): UseFocusTrapReturn
```
```

## File: `skills/vueuse-functions/references/useFocusWithin.md`
```markdown
---
category: Sensors
---

# useFocusWithin

Reactive utility to track if an element or one of its decendants has focus. It is meant to match the behavior of the `:focus-within` CSS pseudo-class. A common use case would be on a form element to see if any of its inputs currently have focus.

## Basic Usage

```vue
<script setup lang="ts">
import { useFocusWithin } from '@vueuse/core'
import { ref, watch } from 'vue'

const target = ref()
const { focused } = useFocusWithin(target)

watch(focused, (focused) => {
  if (focused)
    console.log('Target contains the focused element')
  else
    console.log('Target does NOT contain the focused element')
})
</script>

<template>
  <form ref="target">
    <input type="text" placeholder="First Name">
    <input type="text" placeholder="Last Name">
    <input type="text" placeholder="Email">
    <input type="text" placeholder="Password">
  </form>
</template>
```

## Type Declarations

```ts
export interface UseFocusWithinReturn {
  /**
   * True if the element or any of its descendants are focused
   */
  focused: ComputedRef<boolean>
}
/**
 * Track if focus is contained within the target element
 *
 * @see https://vueuse.org/useFocusWithin
 * @param target The target element to track
 * @param options Focus within options
 */
export declare function useFocusWithin(
  target: MaybeElementRef,
  options?: ConfigurableWindow,
): UseFocusWithinReturn
```
```

## File: `skills/vueuse-functions/references/useFps.md`
```markdown
---
category: Sensors
---

# useFps

Reactive FPS (frames per second).

## Usage

```ts
import { useFps } from '@vueuse/core'

const fps = useFps()
```

## Type Declarations

```ts
export interface UseFpsOptions {
  /**
   * Calculate the FPS on every x frames.
   * @default 10
   */
  every?: number
}
export declare function useFps(options?: UseFpsOptions): ShallowRef<number>
```
```

## File: `skills/vueuse-functions/references/useFullscreen.md`
```markdown
---
category: Browser
---

# useFullscreen

Reactive [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API). It adds methods to present a specific Element (and its descendants) in full-screen mode, and to exit full-screen mode once it is no longer needed. This makes it possible to present desired content—such as an online game—using the user's entire screen, removing all browser user interface elements and other applications from the screen until full-screen mode is shut off.

## Usage

```ts
import { useFullscreen } from '@vueuse/core'

const { isFullscreen, enter, exit, toggle } = useFullscreen()
```

Fullscreen specified element. Some platforms (like iOS's Safari) only allow fullscreen on video elements.

```vue
<script setup lang="ts">
import { useFullscreen } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { isFullscreen, enter, exit, toggle } = useFullscreen(el)
</script>

<template>
  <video ref="el" />
</template>
```

## Component Usage

```vue
<template>
  <UseFullscreen v-slot="{ toggle }">
    <video />
    <button @click="toggle">
      Go Fullscreen
    </button>
  </UseFullscreen>
</template>
```

## Type Declarations

```ts
export interface UseFullscreenOptions extends ConfigurableDocument {
  /**
   * Automatically exit fullscreen when component is unmounted
   *
   * @default false
   */
  autoExit?: boolean
}
export interface UseFullscreenReturn extends Supportable {
  isFullscreen: ShallowRef<boolean>
  enter: () => Promise<void>
  exit: () => Promise<void>
  toggle: () => Promise<void>
}
/**
 * Reactive Fullscreen API.
 *
 * @see https://vueuse.org/useFullscreen
 * @param target
 * @param options
 */
export declare function useFullscreen(
  target?: MaybeElementRef,
  options?: UseFullscreenOptions,
): UseFullscreenReturn
```
```

## File: `skills/vueuse-functions/references/useFuse.md`
```markdown
---
category: '@Integrations'
---

# useFuse

Easily implement fuzzy search using a composable with [Fuse.js](https://github.com/krisk/fuse).

From the Fuse.js website:

> What is fuzzy searching?
>
> Generally speaking, fuzzy searching (more formally known as approximate string matching) is the technique of finding strings that are approximately equal to a given pattern (rather than exactly).

## Install Fuse.js as a peer dependency

### NPM

```bash
npm install fuse.js@^7
```

### Yarn

```bash
yarn add fuse.js
```

## Usage

```ts
import { useFuse } from '@vueuse/integrations/useFuse'
import { shallowRef } from 'vue'

const data = [
  'John Smith',
  'John Doe',
  'Jane Doe',
  'Phillip Green',
  'Peter Brown',
]

const input = shallowRef('Jhon D')

const { results } = useFuse(input, data)

/*
 * Results:
 *
 * { "item": "John Doe", "index": 1 }
 * { "item": "John Smith", "index": 0 }
 * { "item": "Jane Doe", "index": 2 }
 *
 */
```

## Type Declarations

```ts
export type FuseOptions<T> = IFuseOptions<T>
export interface UseFuseOptions<T> {
  fuseOptions?: FuseOptions<T>
  resultLimit?: number
  matchAllWhenSearchEmpty?: boolean
}
export interface UseFuseReturn<DataItem> {
  fuse: Ref<Fuse<DataItem>>
  results: ComputedRef<FuseResult<DataItem>[]>
}
export declare function useFuse<DataItem>(
  search: MaybeRefOrGetter<string>,
  data: MaybeRefOrGetter<DataItem[]>,
  options?: MaybeRefOrGetter<UseFuseOptions<DataItem>>,
): UseFuseReturn<DataItem>
```
```

## File: `skills/vueuse-functions/references/useGamepad.md`
```markdown
---
category: Browser
---

# useGamepad

Provides reactive bindings for the [Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API).

## Usage

> Due to how the Gamepad API works, you must interact with the page using the gamepad before it will be detected.

```vue
<script setup lang="ts">
import { useGamepad } from '@vueuse/core'
import { computed } from 'vue'

const { isSupported, gamepads } = useGamepad()
const gamepad = computed(() => gamepads.value.find(g => g.mapping === 'standard'))
</script>

<template>
  <span>
    {{ gamepad.id }}
  </span>
</template>
```

### Gamepad Updates

Currently the Gamepad API does not have event support to update the state of the gamepad. To update the gamepad state, `requestAnimationFrame` is used to poll for gamepad changes. You can control this polling by using the `pause` and `resume` functions provided by `useGamepad`

```ts
import { useGamepad } from '@vueuse/core'

const { pause, resume, gamepads } = useGamepad()

pause()

// gamepads object will not update

resume()

// gamepads object will update on user input
```

### Gamepad Connect & Disconnect Events

The `onConnected` and `onDisconnected` events will trigger when a gamepad is connected or disconnected.

```ts
import { useGamepad } from '@vueuse/core'
// ---cut---
const { gamepads, onConnected, onDisconnected } = useGamepad()

onConnected((index) => {
  console.log(`${gamepads.value[index].id} connected`)
})

onDisconnected((index) => {
  console.log(`${index} disconnected`)
})
```

### Vibration

> The Gamepad Haptics API is sparse, so check the [compatibility table](https://developer.mozilla.org/en-US/docs/Web/API/GamepadHapticActuator#browser_compatibility) before using.

<!-- eslint-disable import/first -->

```ts
import { useGamepad } from '@vueuse/core'

const { gamepads, onConnected, onDisconnected } = useGamepad()
const gamepad = gamepads.value[0]!
// ---cut---
import { computed } from 'vue'

const supportsVibration = computed(() => gamepad.hapticActuators.length > 0)
function vibrate() {
  if (supportsVibration.value) {
    const actuator = gamepad.hapticActuators[0]
    actuator.playEffect('dual-rumble', {
      startDelay: 0,
      duration: 1000,
      weakMagnitude: 1,
      strongMagnitude: 1,
    })
  }
}
```

### Mappings

To make the Gamepad API easier to use, we provide mappings to map a controller to a controllers button layout.

#### Xbox360 Controller

```vue
<script setup>
import { mapGamepadToXbox360Controller } from '@vueuse/core'

const controller = mapGamepadToXbox360Controller(gamepad)
</script>

<template>
  <span>{{ controller.buttons.a.pressed }}</span>
  <span>{{ controller.buttons.b.pressed }}</span>
  <span>{{ controller.buttons.x.pressed }}</span>
  <span>{{ controller.buttons.y.pressed }}</span>
</template>
```

Currently there are only mappings for the Xbox 360 controller. If you have controller you want to add mappings for, feel free to open a PR for more controller mappings!

### SSR Compatibility

This component is designed to be used in the client side. In some cases, SSR might cause some hydration mismatches.

If you are using Nuxt, you can simply rename your component file with the `.client.vue` suffix (e.g., `GamepadComponent.client.vue`) which will automatically make it render only on the client side, avoiding hydration mismatches.

In other frameworks or plain Vue, you can wrap your usage component with a `<ClientOnly>` component to ensure it is only rendered on the client side.

## Type Declarations

```ts
export interface UseGamepadOptions
  extends ConfigurableWindow, ConfigurableNavigator {}
export interface UseGamepadReturn extends Supportable, Pausable {
  onConnected: EventHookOn<number>
  onDisconnected: EventHookOn<number>
  gamepads: Ref<Gamepad[]>
}
/**
 * Maps a standard standard gamepad to an Xbox 360 Controller.
 */
export declare function mapGamepadToXbox360Controller(
  gamepad: Ref<Gamepad | undefined>,
): ComputedRef<{
  buttons: {
    a: GamepadButton
    b: GamepadButton
    x: GamepadButton
    y: GamepadButton
  }
  bumper: {
    left: GamepadButton
    right: GamepadButton
  }
  triggers: {
    left: GamepadButton
    right: GamepadButton
  }
  stick: {
    left: {
      horizontal: number
      vertical: number
      button: GamepadButton
    }
    right: {
      horizontal: number
      vertical: number
      button: GamepadButton
    }
  }
  dpad: {
    up: GamepadButton
    down: GamepadButton
    left: GamepadButton
    right: GamepadButton
  }
  back: GamepadButton
  start: GamepadButton
} | null>
export declare function useGamepad(
  options?: UseGamepadOptions,
): UseGamepadReturn
```
```

## File: `skills/vueuse-functions/references/useGeolocation.md`
```markdown
---
category: Sensors
---

# useGeolocation

Reactive [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API). It allows the user to provide their location to web applications if they so desire. For privacy reasons, the user is asked for permission to report location information.

## Usage

```ts
import { useGeolocation } from '@vueuse/core'

const { coords, locatedAt, error, resume, pause } = useGeolocation()
```

| State     | Type                                                                          | Description                                                              |
| --------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| coords    | [`Coordinates`](https://developer.mozilla.org/en-US/docs/Web/API/Coordinates) | information about the position retrieved like the latitude and longitude |
| locatedAt | `Date`                                                                        | The time of the last geolocation call                                    |
| error     | `string`                                                                      | An error message in case geolocation API fails.                          |
| resume    | `function`                                                                    | Control function to resume updating geolocation                          |
| pause     | `function`                                                                    | Control function to pause updating geolocation                           |

## Config

`useGeolocation` function takes [PositionOptions](https://developer.mozilla.org/en-US/docs/Web/API/PositionOptions) object as an optional parameter.

## Component Usage

```vue
<template>
  <UseGeolocation v-slot="{ coords: { latitude, longitude } }">
    Latitude: {{ latitude }}
    Longitude: {{ longitude }}
  </UseGeolocation>
</template>
```

## Type Declarations

```ts
export interface UseGeolocationOptions
  extends Partial<PositionOptions>, ConfigurableNavigator {
  immediate?: boolean
}
export interface UseGeolocationReturn extends Supportable {
  coords: Ref<Omit<GeolocationPosition["coords"], "toJSON">>
  locatedAt: ShallowRef<number | null>
  error: ShallowRef<GeolocationPositionError | null>
  resume: () => void
  pause: () => void
}
/**
 * Reactive Geolocation API.
 *
 * @see https://vueuse.org/useGeolocation
 * @param options
 */
export declare function useGeolocation(
  options?: UseGeolocationOptions,
): UseGeolocationReturn
```
```

## File: `skills/vueuse-functions/references/useIDBKeyval.md`
```markdown
---
category: '@Integrations'
---

# useIDBKeyval

Wrapper for [`idb-keyval`](https://www.npmjs.com/package/idb-keyval).

## Install idb-keyval as a peer dependency

```bash
npm install idb-keyval@^6
```

## Usage

```ts
import { useIDBKeyval } from '@vueuse/integrations/useIDBKeyval'

// bind object
const { data: storedObject, isFinished } = useIDBKeyval('my-idb-keyval-store', { hello: 'hi', greeting: 'Hello' })

// update object
storedObject.value.hello = 'hola'

// bind boolean
const flag = useIDBKeyval('my-flag', true) // returns Ref<boolean>

// bind number
const count = useIDBKeyval('my-count', 0) // returns Ref<number>

// awaiting IDB transaction
await count.set(10)
console.log('IDB transaction finished!')

// delete data from idb storage
storedObject.value = null
```

## Type Declarations

```ts
interface Serializer<T> {
  read: (raw: unknown) => T
  write: (value: T) => unknown
}
export interface UseIDBOptions<T> extends ConfigurableFlush {
  /**
   * Watch for deep changes
   *
   * @default true
   */
  deep?: boolean
  /**
   * On error callback
   *
   * Default log error to `console.error`
   */
  onError?: (error: unknown) => void
  /**
   * Use shallow ref as reference
   *
   * @default false
   */
  shallow?: boolean
  /**
   * Write the default value to the storage when it does not exist
   *
   * @default true
   */
  writeDefaults?: boolean
  /**
   * Custom data serialization
   */
  serializer?: Serializer<T>
}
export interface UseIDBKeyvalReturn<T> {
  data: RemovableRef<T>
  isFinished: ShallowRef<boolean>
  set: (value: T) => Promise<void>
}
/**
 *
 * @param key
 * @param initialValue
 * @param options
 */
export declare function useIDBKeyval<T>(
  key: IDBValidKey,
  initialValue: MaybeRefOrGetter<T>,
  options?: UseIDBOptions<T>,
): UseIDBKeyvalReturn<T>
```
```

## File: `skills/vueuse-functions/references/useIdle.md`
```markdown
---
category: Sensors
---

# useIdle

Tracks whether the user is being inactive.

## Usage

```ts
import { useIdle } from '@vueuse/core'

const { idle, lastActive } = useIdle(5 * 60 * 1000) // 5 min

console.log(idle.value) // true or false
```

Programatically resetting:

```ts
import { useCounter, useIdle } from '@vueuse/core'
import { watch } from 'vue'

const { inc, count } = useCounter()

const { idle, lastActive, reset } = useIdle(5 * 60 * 1000) // 5 min

watch(idle, (idleValue) => {
  if (idleValue) {
    inc()
    console.log(`Triggered ${count.value} times`)
    reset() // restarts the idle timer. Does not change lastActive value
  }
})
```

## Component Usage

```vue
<template>
  <UseIdle v-slot="{ idle }" :timeout="5 * 60 * 1000">
    Is Idle: {{ idle }}
  </UseIdle>
</template>
```

## Type Declarations

```ts
export interface UseIdleOptions
  extends ConfigurableWindow, ConfigurableEventFilter {
  /**
   * Event names that listen to for detected user activity
   *
   * @default ['mousemove', 'mousedown', 'resize', 'keydown', 'touchstart', 'wheel']
   */
  events?: WindowEventName[]
  /**
   * Listen for document visibility change
   *
   * @default true
   */
  listenForVisibilityChange?: boolean
  /**
   * Initial state of the ref idle
   *
   * @default false
   */
  initialState?: boolean
}
export interface UseIdleReturn extends Stoppable {
  idle: ShallowRef<boolean>
  lastActive: ShallowRef<number>
  reset: () => void
}
/**
 * Tracks whether the user is being inactive.
 *
 * @see https://vueuse.org/useIdle
 * @param timeout default to 1 minute
 * @param options IdleOptions
 */
export declare function useIdle(
  timeout?: number,
  options?: UseIdleOptions,
): UseIdleReturn
```
```

## File: `skills/vueuse-functions/references/useImage.md`
```markdown
---
category: Browser
---

# useImage

Reactive load an image in the browser, you can wait the result to display it or show a fallback.

## Usage

```vue
<script setup lang="ts">
import { useImage } from '@vueuse/core'

const avatarUrl = 'https://place.dog/300/200'
const { isLoading } = useImage({ src: avatarUrl })
</script>

<template>
  <span v-if="isLoading">Loading</span>
  <img v-else :src="avatarUrl">
</template>
```

## Component Usage

```vue
<template>
  <UseImage src="https://place.dog/300/200">
    <template #loading>
      Loading..
    </template>

    <template #error>
      Failed
    </template>
  </UseImage>
</template>
```

## Type Declarations

```ts
export interface UseImageOptions {
  /** Address of the resource */
  src: string
  /** Images to use in different situations, e.g., high-resolution displays, small monitors, etc. */
  srcset?: string
  /** Image sizes for different page layouts */
  sizes?: string
  /** Image alternative information */
  alt?: string
  /** Image classes */
  class?: string
  /** Image loading */
  loading?: HTMLImageElement["loading"]
  /** Image CORS settings */
  crossorigin?: string
  /** Referrer policy for fetch https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy */
  referrerPolicy?: HTMLImageElement["referrerPolicy"]
  /** Image width */
  width?: HTMLImageElement["width"]
  /** Image height */
  height?: HTMLImageElement["height"]
  /** https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#decoding */
  decoding?: HTMLImageElement["decoding"]
  /** Provides a hint of the relative priority to use when fetching the image */
  fetchPriority?: HTMLImageElement["fetchPriority"]
  /** Provides a hint of the importance of the image */
  ismap?: HTMLImageElement["isMap"]
  /** The partial URL (starting with #) of an image map associated with the element */
  usemap?: HTMLImageElement["useMap"]
}
export type UseImageReturn = UseAsyncStateReturn<
  HTMLImageElement | undefined,
  any[],
  true
>
/**
 * Reactive load an image in the browser, you can wait the result to display it or show a fallback.
 *
 * @see https://vueuse.org/useImage
 * @param options Image attributes, as used in the <img> tag
 * @param asyncStateOptions
 */
export declare function useImage<Shallow extends true>(
  options: MaybeRefOrGetter<UseImageOptions>,
  asyncStateOptions?: UseAsyncStateOptions<Shallow>,
): UseImageReturn
```
```

## File: `skills/vueuse-functions/references/useInfiniteScroll.md`
```markdown
---
category: Sensors
---

# useInfiniteScroll

Infinite scrolling of the element.

## Usage

```vue
<script setup lang="ts">
import { useInfiniteScroll } from '@vueuse/core'
import { ref, useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const data = ref([1, 2, 3, 4, 5, 6])

const { reset } = useInfiniteScroll(
  el,
  () => {
    // load more
    data.value.push(...moreData)
  },
  {
    distance: 10,
    canLoadMore: () => {
      // inidicate when there is no more content to load so onLoadMore stops triggering
      // if (noMoreContent) return false
      return true // for demo purposes
    },
  }
)

function resetList() {
  data.value = []
  reset()
}
</script>

<template>
  <div ref="el">
    <div v-for="item in data">
      {{ item }}
    </div>
  </div>
  <button @click="resetList()">
    Reset
  </button>
</template>
```

## Direction

Different scroll directions require different CSS style settings:

| Direction          | Required CSS                                          |
| ------------------ | ----------------------------------------------------- |
| `bottom` (default) | No special settings required                          |
| `top`              | `display: flex;`<br>`flex-direction: column-reverse;` |
| `left`             | `display: flex;`<br>`flex-direction: row-reverse;`    |
| `right`            | `display: flex;`                                      |

::: warning
Make sure to indicate when there is no more content to load with `canLoadMore`, otherwise `onLoadMore` will trigger as long as there is space for more content.
:::

## Directive Usage

```vue
<script setup lang="ts">
import { vInfiniteScroll } from '@vueuse/components'
import { ref } from 'vue'

const data = ref([1, 2, 3, 4, 5, 6])

function onLoadMore() {
  const length = data.value.length + 1
  data.value.push(...Array.from({ length: 5 }, (_, i) => length + i))
}
function canLoadMore() {
  // inidicate when there is no more content to load so onLoadMore stops triggering
  // if (noMoreContent) return false
  return true // for demo purposes
}
</script>

<template>
  <div v-infinite-scroll="onLoadMore">
    <div v-for="item in data" :key="item">
      {{ item }}
    </div>
  </div>

  <!-- with options -->
  <div v-infinite-scroll="[onLoadMore, { distance: 10, canLoadMore }]">
    <div v-for="item in data" :key="item">
      {{ item }}
    </div>
  </div>
</template>
```

## Type Declarations

```ts
type InfiniteScrollElement =
  | HTMLElement
  | SVGElement
  | Window
  | Document
  | null
  | undefined
export interface UseInfiniteScrollOptions<
  T extends InfiniteScrollElement = InfiniteScrollElement,
> extends UseScrollOptions {
  /**
   * The minimum distance between the bottom of the element and the bottom of the viewport
   *
   * @default 0
   */
  distance?: number
  /**
   * The direction in which to listen the scroll.
   *
   * @default 'bottom'
   */
  direction?: "top" | "bottom" | "left" | "right"
  /**
   * The interval time between two load more (to avoid too many invokes).
   *
   * @default 100
   */
  interval?: number
  /**
   * A function that determines whether more content can be loaded for a specific element.
   * Should return `true` if loading more content is allowed for the given element,
   * and `false` otherwise.
   */
  canLoadMore?: (el: T) => boolean
}
export interface UseInfiniteScrollReturn {
  isLoading: ComputedRef<boolean>
  reset: () => void
}
/**
 * Reactive infinite scroll.
 *
 * @see https://vueuse.org/useInfiniteScroll
 */
export declare function useInfiniteScroll<T extends InfiniteScrollElement>(
  element: MaybeRefOrGetter<T>,
  onLoadMore: (state: UnwrapNestedRefs<UseScrollReturn>) => Awaitable<void>,
  options?: UseInfiniteScrollOptions<T>,
): UseInfiniteScrollReturn
```
```

## File: `skills/vueuse-functions/references/useIntersectionObserver.md`
```markdown
---
category: Elements
---

# useIntersectionObserver

Detects that a target element's visibility.

## Usage

```vue
<script setup lang="ts">
import { useIntersectionObserver } from '@vueuse/core'
import { shallowRef, useTemplateRef } from 'vue'

const target = useTemplateRef('target')
const targetIsVisible = shallowRef(false)

const { stop } = useIntersectionObserver(
  target,
  ([entry], observerElement) => {
    targetIsVisible.value = entry?.isIntersecting || false
  },
)
</script>

<template>
  <div ref="target">
    <h1>Hello world</h1>
  </div>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vIntersectionObserver } from '@vueuse/components'
import { shallowRef, useTemplateRef } from 'vue'

const root = useTemplateRef('root')

const isVisible = shallowRef(false)

function onIntersectionObserver([entry]: IntersectionObserverEntry[]) {
  isVisible.value = entry?.isIntersecting || false
}
</script>

<template>
  <div>
    <p>
      Scroll me down!
    </p>
    <div v-intersection-observer="onIntersectionObserver">
      <p>Hello world!</p>
    </div>
  </div>

  <!-- with options -->
  <div ref="root">
    <p>
      Scroll me down!
    </p>
    <div v-intersection-observer="[onIntersectionObserver, { root }]">
      <p>Hello world!</p>
    </div>
  </div>
</template>
```

[IntersectionObserver MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver)

## Type Declarations

```ts
export interface UseIntersectionObserverOptions extends ConfigurableWindow {
  /**
   * Start the IntersectionObserver immediately on creation
   *
   * @default true
   */
  immediate?: boolean
  /**
   * The Element or Document whose bounds are used as the bounding box when testing for intersection.
   */
  root?: MaybeComputedElementRef | Document
  /**
   * A string which specifies a set of offsets to add to the root's bounding_box when calculating intersections.
   */
  rootMargin?: MaybeRefOrGetter<string>
  /**
   * Either a single number or an array of numbers between 0.0 and 1.
   * @default 0
   */
  threshold?: number | number[]
}
export interface UseIntersectionObserverReturn extends Supportable, Pausable {
  stop: () => void
}
/**
 * Detects that a target element's visibility.
 *
 * @see https://vueuse.org/useIntersectionObserver
 * @param target
 * @param callback
 * @param options
 */
export declare function useIntersectionObserver(
  target:
    | MaybeComputedElementRef
    | MaybeRefOrGetter<MaybeElement[]>
    | MaybeComputedElementRef[],
  callback: IntersectionObserverCallback,
  options?: UseIntersectionObserverOptions,
): UseIntersectionObserverReturn
```
```

## File: `skills/vueuse-functions/references/useInterval.md`
```markdown
---
category: Animation
---

# useInterval

Reactive counter that increases on every interval.

## Usage

```ts
import { useInterval } from '@vueuse/core'

// count will increase every 200ms
const counter = useInterval(200)
```

### With Controls

```ts
import { useInterval } from '@vueuse/core'

const { counter, reset, pause, resume, isActive } = useInterval(200, {
  controls: true,
})

// Reset counter to 0
reset()

// Pause/resume the interval
pause()
resume()
```

### Options

| Option      | Type                      | Default | Description                                                |
| ----------- | ------------------------- | ------- | ---------------------------------------------------------- |
| `controls`  | `boolean`                 | `false` | Expose `pause`, `resume`, `reset`, and `isActive` controls |
| `immediate` | `boolean`                 | `true`  | Start the interval immediately                             |
| `callback`  | `(count: number) => void` | —       | Called on every interval with the current count            |

### Reactive Interval

The interval can be reactive:

```ts
import { useInterval } from '@vueuse/core'

const intervalMs = ref(1000)
const counter = useInterval(intervalMs)

// Change the interval dynamically
intervalMs.value = 500
```

### Callback on Every Interval

```ts
import { useInterval } from '@vueuse/core'

useInterval(1000, {
  callback: (count) => {
    console.log(`Tick ${count}`)
  },
})
```

## Type Declarations

```ts
export interface UseIntervalOptions<Controls extends boolean> {
  /**
   * Expose more controls
   *
   * @default false
   */
  controls?: Controls
  /**
   * Execute the update immediately on calling
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Callback on every interval
   */
  callback?: (count: number) => void
}
export interface UseIntervalControls {
  counter: ShallowRef<number>
  reset: () => void
}
export type UseIntervalReturn =
  | Readonly<ShallowRef<number>>
  | Readonly<UseIntervalControls & Pausable>
/**
 * Reactive counter increases on every interval
 *
 * @see https://vueuse.org/useInterval
 * @param interval
 * @param options
 */
export declare function useInterval(
  interval?: MaybeRefOrGetter<number>,
  options?: UseIntervalOptions<false>,
): Readonly<ShallowRef<number>>
export declare function useInterval(
  interval: MaybeRefOrGetter<number>,
  options: UseIntervalOptions<true>,
): Readonly<UseIntervalControls & Pausable>
```
```

## File: `skills/vueuse-functions/references/useIntervalFn.md`
```markdown
---
category: Animation
---

# useIntervalFn

Wrapper for `setInterval` with controls

## Usage

```ts
import { useIntervalFn } from '@vueuse/core'

const { pause, resume, isActive } = useIntervalFn(() => {
  /* your function */
}, 1000)
```

## Type Declarations

```ts
export interface UseIntervalFnOptions {
  /**
   * Start the timer immediately
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Execute the callback immediately after calling `resume`
   *
   * @default false
   */
  immediateCallback?: boolean
}
export type UseIntervalFnReturn = Pausable
/**
 * Wrapper for `setInterval` with controls
 *
 * @see https://vueuse.org/useIntervalFn
 * @param cb
 * @param interval
 * @param options
 */
export declare function useIntervalFn(
  cb: Fn,
  interval?: MaybeRefOrGetter<number>,
  options?: UseIntervalFnOptions,
): UseIntervalFnReturn
```
```

## File: `skills/vueuse-functions/references/useIpcRenderer.md`
```markdown
---
category: '@Electron'
---

# useIpcRenderer

Provides [ipcRenderer](https://www.electronjs.org/docs/api/ipc-renderer) and all of its APIs with Vue reactivity.

## Usage

```ts
import { useIpcRenderer } from '@vueuse/electron'
import { computed } from 'vue'

// enable nodeIntegration if you don't provide ipcRenderer explicitly
// see: https://www.electronjs.org/docs/api/webview-tag#nodeintegration
const ipcRenderer = useIpcRenderer()

// Ref result will return
const result = ipcRenderer.invoke<string>('custom-channel', 'some data')
const msg = computed(() => result.value?.msg)

// remove listener automatically on unmounted
ipcRenderer.on('custom-event', (event, ...args) => {
  console.log(args)
})
```

### Available Methods

| Method                                     | Description                                          |
| ------------------------------------------ | ---------------------------------------------------- |
| `on(channel, listener)`                    | Listen to channel. Auto-removes listener on unmount. |
| `once(channel, listener)`                  | Listen to channel once                               |
| `removeListener(channel, listener)`        | Remove specific listener                             |
| `removeAllListeners(channel)`              | Remove all listeners for channel                     |
| `send(channel, ...args)`                   | Send async message to main process                   |
| `invoke(channel, ...args)`                 | Send message and get response as `ShallowRef`        |
| `sendSync(channel, ...args)`               | Send sync message and get response as `ShallowRef`   |
| `postMessage(channel, message, transfer?)` | Send message with transferable objects               |
| `sendTo(webContentsId, channel, ...args)`  | Send to specific webContents                         |
| `sendToHost(channel, ...args)`             | Send to webview host                                 |

### With Custom IpcRenderer

If `nodeIntegration` is disabled, you can pass the `ipcRenderer` instance explicitly:

```ts
import { useIpcRenderer } from '@vueuse/electron'
import { ipcRenderer } from 'electron'

const ipc = useIpcRenderer(ipcRenderer)
```

## Type Declarations

```ts
/**
 * Result from useIpcRenderer
 *
 * @see https://www.electronjs.org/docs/api/ipc-renderer
 */
export interface UseIpcRendererReturn {
  /**
   * Listens to channel, when a new message arrives listener would be called with listener(event, args...).
   * [ipcRenderer.removeListener](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovelistenerchannel-listener) automatically on unmounted.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendereronchannel-listener
   */
  on: (channel: string, listener: IpcRendererListener) => IpcRenderer
  /**
   * Adds a one time listener function for the event. This listener is invoked only the next time a message is sent to channel, after which it is removed.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendereroncechannel-listener
   */
  once: (
    channel: string,
    listener: (event: IpcRendererEvent, ...args: any[]) => void,
  ) => IpcRenderer
  /**
   * Removes the specified listener from the listener array for the specified channel.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovelistenerchannel-listener
   */
  removeListener: (
    channel: string,
    listener: (...args: any[]) => void,
  ) => IpcRenderer
  /**
   * Removes all listeners, or those of the specified channel.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovealllistenerschannel
   */
  removeAllListeners: (channel: string) => IpcRenderer
  /**
   * Send an asynchronous message to the main process via channel, along with arguments.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrenderersendchannel-args
   */
  send: (channel: string, ...args: any[]) => void
  /**
   * Returns Promise<any> - Resolves with the response from the main process.
   * Send a message to the main process via channel and expect a result ~~asynchronously~~.
   * As composition-api, it makes asynchronous operations look like synchronous.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererinvokechannel-args
   */
  invoke: <T>(channel: string, ...args: any[]) => ShallowRef<T | null>
  /**
   * Returns any - The value sent back by the ipcMain handler.
   * Send a message to the main process via channel and expect a result synchronously.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrenderersendsyncchannel-args
   */
  sendSync: <T>(channel: string, ...args: any[]) => ShallowRef<T | null>
  /**
   * Send a message to the main process, optionally transferring ownership of zero or more MessagePort objects.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererpostmessagechannel-message-transfer
   */
  postMessage: (channel: string, message: any, transfer?: MessagePort[]) => void
  /**
   * Sends a message to a window with webContentsId via channel.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrenderersendtowebcontentsid-channel-args
   */
  sendTo: (webContentsId: number, channel: string, ...args: any[]) => void
  /**
   * Like ipcRenderer.send but the event will be sent to the <webview> element in the host page instead of the main process.
   *
   * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrenderersendtohostchannel-args
   */
  sendToHost: (channel: string, ...args: any[]) => void
}
/**
 * Get the `ipcRenderer` module with all APIs.
 *
 * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrenderersendtohostchannel-args
 * @see https://vueuse.org/useIpcRenderer
 */
export declare function useIpcRenderer(
  ipcRenderer?: IpcRenderer,
): UseIpcRendererReturn
```
```

## File: `skills/vueuse-functions/references/useIpcRendererInvoke.md`
```markdown
---
category: '@Electron'
---

# useIpcRendererInvoke

Reactive [ipcRenderer.invoke API](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererinvokechannel-args) result. Make asynchronous operations look synchronous.

## Usage

```ts
import { useIpcRendererInvoke } from '@vueuse/electron'
import { computed } from 'vue'

// enable nodeIntegration if you don't provide ipcRenderer explicitly
// see: https://www.electronjs.org/docs/api/webview-tag#nodeintegration
// Ref result will return
const result = useIpcRendererInvoke<string>('custom-channel', 'some data')
const msg = computed(() => result.value?.msg)
```

## Type Declarations

```ts
/**
 * Returns Promise<any> - Resolves with the response from the main process.
 *
 * Send a message to the main process via channel and expect a result ~~asynchronously~~. As composition-api, it makes asynchronous operations look like synchronous.
 *
 * You need to provide `ipcRenderer` to this function.
 *
 * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererinvokechannel-args
 * @see https://vueuse.org/useIpcRendererInvoke
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useIpcRendererInvoke<T>(
  ipcRenderer: IpcRenderer,
  channel: string,
  ...args: any[]
): ShallowRef<T | null>
/**
 * Returns Promise<any> - Resolves with the response from the main process.
 *
 * Send a message to the main process via channel and expect a result ~~asynchronously~~. As composition-api, it makes asynchronous operations look like synchronous.
 *
 * `ipcRenderer` will be automatically gotten.
 *
 * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererinvokechannel-args
 * @see https://vueuse.org/useIpcRendererInvoke
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useIpcRendererInvoke<T>(
  channel: string,
  ...args: any[]
): ShallowRef<T | null>
```
```

## File: `skills/vueuse-functions/references/useIpcRendererOn.md`
```markdown
---
category: '@Electron'
---

# useIpcRendererOn

Use [ipcRenderer.on](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendereronchannel-listener) with ease and [ipcRenderer.removeListener](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovelistenerchannel-listener) automatically on unmounted.

## Usage

```ts
import { useIpcRendererOn } from '@vueuse/electron'

// enable nodeIntegration if you don't provide ipcRenderer explicitly
// see: https://www.electronjs.org/docs/api/webview-tag#nodeintegration
// remove listener automatically on unmounted
useIpcRendererOn('custom-event', (event, ...args) => {
  console.log(args)
})
```

## Type Declarations

```ts
/**
 * Listens to channel, when a new message arrives listener would be called with listener(event, args...).
 * [ipcRenderer.removeListener](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovelistenerchannel-listener) automatically on unmounted.
 *
 * You need to provide `ipcRenderer` to this function.
 *
 * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendereronchannel-listener
 * @see https://vueuse.org/useIpcRendererOn
 */
export declare function useIpcRendererOn(
  ipcRenderer: IpcRenderer,
  channel: string,
  listener: IpcRendererListener,
): IpcRenderer
/**
 * Listens to channel, when a new message arrives listener would be called with listener(event, args...).
 * [ipcRenderer.removeListener](https://www.electronjs.org/docs/api/ipc-renderer#ipcrendererremovelistenerchannel-listener) automatically on unmounted.
 *
 * `ipcRenderer` will be automatically gotten.
 *
 * @see https://www.electronjs.org/docs/api/ipc-renderer#ipcrendereronchannel-listener
 * @see https://vueuse.org/useIpcRendererOn
 */
export declare function useIpcRendererOn(
  channel: string,
  listener: IpcRendererListener,
): IpcRenderer
```
```

## File: `skills/vueuse-functions/references/useJwt.md`
```markdown
---
category: '@Integrations'
---

# useJwt

Wrapper for [`jwt-decode`](https://github.com/auth0/jwt-decode).

## Install

```bash
npm install jwt-decode@^4
```

## Usage

```ts
import { useJwt } from '@vueuse/integrations/useJwt'
import { defineComponent } from 'vue'

const encodedJwt = ref('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ.L8i6g3PfcHlioHCCPURC9pmXT7gdJpx3kOoyAfNUwCc')
const { header, payload } = useJwt(encodedJwt)
```

## Type Declarations

```ts
export interface UseJwtOptions<Fallback> {
  /**
   * Value returned when encounter error on decoding
   *
   * @default null
   */
  fallbackValue?: Fallback
  /**
   * Error callback for decoding
   */
  onError?: (error: unknown) => void
}
export interface UseJwtReturn<Payload, Header, Fallback> {
  header: ComputedRef<Header | Fallback>
  payload: ComputedRef<Payload | Fallback>
}
/**
 * Reactive decoded jwt token.
 *
 * @see https://vueuse.org/useJwt
 */
export declare function useJwt<
  Payload extends object = JwtPayload,
  Header extends object = JwtHeader,
  Fallback = null,
>(
  encodedJwt: MaybeRefOrGetter<string>,
  options?: UseJwtOptions<Fallback>,
): UseJwtReturn<Payload, Header, Fallback>
```
```

## File: `skills/vueuse-functions/references/useKeyModifier.md`
```markdown
---
category: Sensors
---

# useKeyModifier

Reactive [Modifier State](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/getModifierState). Tracks state of any of the [supported modifiers](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/getModifierState#browser_compatibility) - see Browser Compatibility notes.

<CourseLink href="https://vueschool.io/lessons/alt-drag-to-clone-tasks?friend=vueuse">Learn useKeyModifier with this FREE video lesson from Vue School!</CourseLink>

## Usage

```ts
import { useKeyModifier } from '@vueuse/core'

const capsLockState = useKeyModifier('CapsLock')

console.log(capsLockState.value)
```

## Events

You can customize which events will prompt the state to update. By default, these are `mouseup`, `mousedown`, `keyup`, `keydown`. To customize these events:

```ts
import { useKeyModifier } from '@vueuse/core'

const capsLockState = useKeyModifier('CapsLock', { events: ['mouseup', 'mousedown'] })

console.log(capsLockState) // null

// Caps Lock turned on with key press
console.log(capsLockState) // null

// Mouse button clicked
console.log(capsLockState) // true
```

## Initial State

By default, the returned ref will be `Ref<null>` until the first event is received. You can explicitly pass the initial state to it via:

```ts
import { useKeyModifier } from '@vueuse/core'
// ---cut---
const capsLockState1 = useKeyModifier('CapsLock') // Ref<boolean | null>
const capsLockState2 = useKeyModifier('CapsLock', { initial: false }) // Ref<boolean>
```

## Type Declarations

```ts
export type KeyModifier =
  | "Alt"
  | "AltGraph"
  | "CapsLock"
  | "Control"
  | "Fn"
  | "FnLock"
  | "Meta"
  | "NumLock"
  | "ScrollLock"
  | "Shift"
  | "Symbol"
  | "SymbolLock"
export interface UseModifierOptions<Initial> extends ConfigurableDocument {
  /**
   * Event names that will prompt update to modifier states
   *
   * @default ['mousedown', 'mouseup', 'keydown', 'keyup']
   */
  events?: WindowEventName[]
  /**
   * Initial value of the returned ref
   *
   * @default null
   */
  initial?: Initial
}
export type UseKeyModifierReturn<Initial> = ShallowRef<
  Initial extends boolean ? boolean : boolean | null
>
export declare function useKeyModifier<Initial extends boolean | null>(
  modifier: KeyModifier,
  options?: UseModifierOptions<Initial>,
): UseKeyModifierReturn<Initial>
```
```

## File: `skills/vueuse-functions/references/useLastChanged.md`
```markdown
---
category: State
---

# useLastChanged

Records the timestamp of the last change

## Usage

```ts
import { useLastChanged } from '@vueuse/core'
import { nextTick } from 'vue'

const a = ref(0)
const lastChanged = useLastChanged(a)

a.value = 1

await nextTick()

console.log(lastChanged.value) // 1704709379457
```

By default the change is recorded on the next tick (`watch()` with `flush: 'post'`). If you want to record the change immediately, pass `flush: 'sync'` as the second argument.

```ts
import { useLastChanged } from '@vueuse/core'

const a = ref(0)
const lastChanged = useLastChanged(a, { flush: 'sync' })

a.value = 1

console.log(lastChanged.value) // 1704709379457
```

## Type Declarations

```ts
export interface UseLastChangedOptions<
  Immediate extends boolean,
  InitialValue extends number | null | undefined = undefined,
> extends WatchOptions<Immediate> {
  initialValue?: InitialValue
}
export type UseLastChangedReturn =
  | Readonly<ShallowRef<number | null>>
  | Readonly<ShallowRef<number>>
/**
 * Records the timestamp of the last change
 *
 * @see https://vueuse.org/useLastChanged
 */
export declare function useLastChanged(
  source: WatchSource,
  options?: UseLastChangedOptions<false>,
): Readonly<ShallowRef<number | null>>
export declare function useLastChanged(
  source: WatchSource,
  options: UseLastChangedOptions<true> | UseLastChangedOptions<boolean, number>,
): Readonly<ShallowRef<number>>
```
```

## File: `skills/vueuse-functions/references/useLocalStorage.md`
```markdown
---
category: State
---

# useLocalStorage

Reactive [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

## Usage

Please refer to `useStorage`.

## Type Declarations

```ts
export declare function useLocalStorage(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<string>,
  options?: UseStorageOptions<string>,
): RemovableRef<string>
export declare function useLocalStorage(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<boolean>,
  options?: UseStorageOptions<boolean>,
): RemovableRef<boolean>
export declare function useLocalStorage(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<number>,
  options?: UseStorageOptions<number>,
): RemovableRef<number>
export declare function useLocalStorage<T>(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<T>,
  options?: UseStorageOptions<T>,
): RemovableRef<T>
export declare function useLocalStorage<T = unknown>(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<null>,
  options?: UseStorageOptions<T>,
): RemovableRef<T>
```
```

## File: `skills/vueuse-functions/references/useMagicKeys.md`
```markdown
---
category: Sensors
---

# useMagicKeys

Reactive keys pressed state, with magical keys combination support.

## Usage

```ts
import { useMagicKeys } from '@vueuse/core'

const { shift, space, a /* keys you want to monitor */ } = useMagicKeys()

watch(space, (v) => {
  if (v)
    console.log('space has been pressed')
})

watchEffect(() => {
  if (shift.value && a.value)
    console.log('Shift + A have been pressed')
})
```

::: tip NOTE
If you're using TypeScript with `noUncheckedIndexedAccess` enabled in your `tsconfig.json` (or using Nuxt which enables it by default), the destructured keys will have the type `ComputedRef<boolean> | undefined`.

The `noUncheckedIndexedAccess` TypeScript option adds `undefined` to any un-declared field accessed via index signatures. Since `useMagicKeys()` uses an index signature to allow accessing any key dynamically, TypeScript will treat destructured properties as potentially undefined for type safety.

You'll need to use optional chaining or wrap with a getter function:

```ts
const { shift, space, a } = useMagicKeys()

watch(
  () => space?.value,
  (v) => {
    if (v)
      console.log('space has been pressed')
  },
)

watchEffect(() => {
  if (shift?.value && a?.value)
    console.log('Shift + A have been pressed')
})
```

Check the [TypeScript documentation](https://www.typescriptlang.org/tsconfig/#noUncheckedIndexedAccess) for more details about `noUncheckedIndexedAccess`.

:::

Check out [all the possible keycodes](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/code/code_values).

### Combinations

You can magically use combinations (shortcuts/hotkeys) by connecting keys with `+` or `_`.

```ts
import { useMagicKeys } from '@vueuse/core'

const keys = useMagicKeys()
const shiftCtrlA = keys['Shift+Ctrl+A']

watch(shiftCtrlA, (v) => {
  if (v)
    console.log('Shift + Ctrl + A have been pressed')
})
```

```ts
import { useMagicKeys } from '@vueuse/core'

const { Ctrl_A_B, space, alt_s /* ... */ } = useMagicKeys()

watch(Ctrl_A_B, (v) => {
  if (v)
    console.log('Control+A+B have been pressed')
})
```

You can also use `whenever` function to make it shorter

```ts
import { useMagicKeys, whenever } from '@vueuse/core'

const keys = useMagicKeys()

whenever(keys.shift_space, () => {
  console.log('Shift+Space have been pressed')
})
```

### Current Pressed keys

A special property `current` is provided to representing all the keys been pressed currently.

```ts
import { useMagicKeys, whenever } from '@vueuse/core'

const { current } = useMagicKeys()

console.log(current) // Set { 'control', 'a' }

whenever(
  () => current.has('a') && !current.has('b'),
  () => console.log('A is pressed but not B'),
)
```

### Key Aliasing

```ts
import { useMagicKeys, whenever } from '@vueuse/core'

const { shift_cool } = useMagicKeys({
  aliasMap: {
    cool: 'space',
  },
})

whenever(shift_cool, () => console.log('Shift + Space have been pressed'))
```

By default, we have some [preconfigured alias for common practices](https://github.com/vueuse/vueuse/blob/main/packages/core/useMagicKeys/aliasMap.ts).

### Conditionally Disable

You might have some `<input />` elements in your apps, and you don't want to trigger the magic keys handling when users focused on those inputs. There is an example of using `useActiveElement` and `logicAnd` to do that.

```ts
import { useActiveElement, useMagicKeys, whenever } from '@vueuse/core'
import { logicAnd } from '@vueuse/math'

const activeElement = useActiveElement()
const notUsingInput = computed(() =>
  activeElement.value?.tagName !== 'INPUT'
  && activeElement.value?.tagName !== 'TEXTAREA',)

const { tab } = useMagicKeys()

whenever(logicAnd(tab, notUsingInput), () => {
  console.log('Tab has been pressed outside of inputs!')
})
```

### Custom Event Handler

```ts
import { useMagicKeys, whenever } from '@vueuse/core'

const { ctrl_s } = useMagicKeys({
  passive: false,
  onEventFired(e) {
    if (e.ctrlKey && e.key === 's' && e.type === 'keydown')
      e.preventDefault()
  },
})

whenever(ctrl_s, () => console.log('Ctrl+S have been pressed'))
```

> ⚠️ This usage is NOT recommended, please use with caution.

### Reactive Mode

By default, the values of `useMagicKeys()` are `Ref<boolean>`. If you want to use the object in the template, you can set it to reactive mode.

```ts
import { useMagicKeys } from '@vueuse/core'
// ---cut---
const keys = useMagicKeys({ reactive: true })
```

```vue
<template>
  <div v-if="keys.shift">
    You are holding the Shift key!
  </div>
</template>
```

## Type Declarations

```ts
export interface UseMagicKeysOptions<Reactive extends boolean> {
  /**
   * Returns a reactive object instead of an object of refs
   *
   * @default false
   */
  reactive?: Reactive
  /**
   * Target for listening events
   *
   * @default window
   */
  target?: MaybeRefOrGetter<EventTarget>
  /**
   * Alias map for keys, all the keys should be lowercase
   * { target: keycode }
   *
   * @example { ctrl: "control" }
   * @default <predefined-map>
   */
  aliasMap?: Record<string, string>
  /**
   * Register passive listener
   *
   * @default true
   */
  passive?: boolean
  /**
   * Custom event handler for keydown/keyup event.
   * Useful when you want to apply custom logic.
   *
   * When using `e.preventDefault()`, you will need to pass `passive: false` to useMagicKeys().
   */
  onEventFired?: (e: KeyboardEvent) => void | boolean
}
export interface MagicKeysInternal {
  /**
   * A Set of currently pressed keys,
   * Stores raw keyCodes.
   *
   * @see https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key
   */
  current: Set<string>
}
export type UseMagicKeysReturn<Reactive extends boolean> = Readonly<
  Record<string, Reactive extends true ? boolean : ComputedRef<boolean>> &
    MagicKeysInternal
>
/**
 * Reactive keys pressed state, with magical keys combination support.
 *
 * @see https://vueuse.org/useMagicKeys
 */
export declare function useMagicKeys<T extends boolean = false>(
  options?: UseMagicKeysOptions<T>,
): UseMagicKeysReturn<T>
export { DefaultMagicKeysAliasMap } from "./aliasMap"
```
```

## File: `skills/vueuse-functions/references/useManualRefHistory.md`
```markdown
---
category: State
related: useRefHistory
---

# useManualRefHistory

Manually track the change history of a ref when the using calls `commit()`, also provides undo and redo functionality

## Usage

```ts {5} twoslash include usage
import { useManualRefHistory } from '@vueuse/core'
import { shallowRef } from 'vue'

const counter = shallowRef(0)
const { history, commit, undo, redo } = useManualRefHistory(counter)

counter.value += 1
commit()

console.log(history.value)
/* [
  { snapshot: 1, timestamp: 1601912898062 },
  { snapshot: 0, timestamp: 1601912898061 }
] */
```

You can use `undo` to reset the ref value to the last history point.

```ts
// @include: usage
// ---cut---
console.log(counter.value) // 1
undo()
console.log(counter.value) // 0
```

#### History of mutable objects

If you are going to mutate the source, you need to pass a custom clone function or use `clone` `true` as a param, that is a shortcut for a minimal clone function `x => JSON.parse(JSON.stringify(x))` that will be used in both `dump` and `parse`.

```ts {5}
import { useManualRefHistory } from '@vueuse/core'
import { ref } from 'vue'

const counter = ref({ foo: 1, bar: 2 })
const { history, commit, undo, redo } = useManualRefHistory(counter, { clone: true })

counter.value.foo += 1
commit()
```

#### Custom Clone Function

To use a full featured or custom clone function, you can set up via the `clone` options.

For example, using [structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone):

```ts
import { useManualRefHistory } from '@vueuse/core'

const refHistory = useManualRefHistory(target, { clone: structuredClone })
```

Or by using [lodash's `cloneDeep`](https://lodash.com/docs/4.17.15#cloneDeep):

```ts
import { useManualRefHistory } from '@vueuse/core'
import { cloneDeep } from 'lodash-es'

const refHistory = useManualRefHistory(target, { clone: cloneDeep })
```

Or a more lightweight [`klona`](https://github.com/lukeed/klona):

```ts
import { useManualRefHistory } from '@vueuse/core'
import { klona } from 'klona'

const refHistory = useManualRefHistory(target, { clone: klona })
```

#### Custom Dump and Parse Function

Instead of using the `clone` options, you can pass custom functions to control the serialization and parsing. In case you do not need history values to be objects, this can save an extra clone when undoing. It is also useful in case you want to have the snapshots already stringified to be saved to local storage for example.

```ts
import { useManualRefHistory } from '@vueuse/core'

const refHistory = useManualRefHistory(target, {
  dump: JSON.stringify,
  parse: JSON.parse,
})
```

### History Capacity

We will keep all the history by default (unlimited) until you explicitly clear them up, you can set the maximal amount of history to be kept by `capacity` options.

```ts
import { useManualRefHistory } from '@vueuse/core'

const refHistory = useManualRefHistory(target, {
  capacity: 15, // limit to 15 history records
})

refHistory.clear() // explicitly clear all the history
```

## Type Declarations

```ts
export interface UseRefHistoryRecord<T> {
  snapshot: T
  timestamp: number
}
export interface UseManualRefHistoryOptions<Raw, Serialized = Raw> {
  /**
   * Maximum number of history to be kept. Default to unlimited.
   */
  capacity?: number
  /**
   * Clone when taking a snapshot, shortcut for dump: JSON.parse(JSON.stringify(value)).
   * Default to false
   *
   * @default false
   */
  clone?: boolean | CloneFn<Raw>
  /**
   * Serialize data into the history
   */
  dump?: (v: Raw) => Serialized
  /**
   * Deserialize data from the history
   */
  parse?: (v: Serialized) => Raw
  /**
   * set data source
   */
  setSource?: (source: Ref<Raw>, v: Raw) => void
}
export interface UseManualRefHistoryReturn<Raw, Serialized> {
  /**
   * Bypassed tracking ref from the argument
   */
  source: Ref<Raw>
  /**
   * An array of history records for undo, newest comes to first
   */
  history: Ref<UseRefHistoryRecord<Serialized>[]>
  /**
   * Last history point, source can be different if paused
   */
  last: Ref<UseRefHistoryRecord<Serialized>>
  /**
   * Same as {@link UseManualRefHistoryReturn.history | history}
   */
  undoStack: Ref<UseRefHistoryRecord<Serialized>[]>
  /**
   * Records array for redo
   */
  redoStack: Ref<UseRefHistoryRecord<Serialized>[]>
  /**
   * A ref representing if undo is possible (non empty undoStack)
   */
  canUndo: ComputedRef<boolean>
  /**
   * A ref representing if redo is possible (non empty redoStack)
   */
  canRedo: ComputedRef<boolean>
  /**
   * Undo changes
   */
  undo: () => void
  /**
   * Redo changes
   */
  redo: () => void
  /**
   * Clear all the history
   */
  clear: () => void
  /**
   * Create a new history record
   */
  commit: () => void
  /**
   * Reset ref's value with latest history
   */
  reset: () => void
}
/**
 * Track the change history of a ref, also provides undo and redo functionality.
 *
 * @see https://vueuse.org/useManualRefHistory
 * @param source
 * @param options
 */
export declare function useManualRefHistory<Raw, Serialized = Raw>(
  source: Ref<Raw>,
  options?: UseManualRefHistoryOptions<Raw, Serialized>,
): UseManualRefHistoryReturn<Raw, Serialized>
```
```

## File: `skills/vueuse-functions/references/useMath.md`
```markdown
---
category: '@Math'
---

# useMath

Reactive `Math` methods.

## Usage

```ts
import { useMath } from '@vueuse/math'

const base = ref(2)
const exponent = ref(3)
const result = useMath('pow', base, exponent) // Ref<8>

const num = ref(2)
const root = useMath('sqrt', num) // Ref<1.4142135623730951>

num.value = 4
console.log(root.value) // 2
```

## Type Declarations

```ts
export type UseMathKeys = keyof {
  [K in keyof Math as Math[K] extends (...args: any) => any
    ? K
    : never]: unknown
}
export type UseMathReturn<K extends keyof Math> = ReturnType<
  Reactified<Math[K], true>
>
/**
 * Reactive `Math` methods.
 *
 * @see https://vueuse.org/useMath
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useMath<K extends keyof Math>(
  key: K,
  ...args: ArgumentsType<Reactified<Math[K], true>>
): UseMathReturn<K>
```
```

## File: `skills/vueuse-functions/references/useMax.md`
```markdown
---
category: '@Math'
---

# useMax

Reactive `Math.max`.

## Usage

```ts
import { useMax } from '@vueuse/math'

const array = ref([1, 2, 3, 4])
const max = useMax(array) // Ref<4>
```

```ts
import { useMax } from '@vueuse/math'

const a = ref(1)
const b = ref(3)

const max = useMax(a, b, 2) // Ref<3>
```

## Type Declarations

```ts
export declare function useMax(
  array: MaybeRefOrGetter<MaybeRefOrGetter<number>[]>,
): ComputedRef<number>
export declare function useMax(
  ...args: MaybeRefOrGetter<number>[]
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useMediaControls.md`
```markdown
---
category: Browser
---

# useMediaControls

Reactive media controls for both `audio` and `video` elements

## Usage

### Basic Usage

```vue
<script setup lang="ts">
import { useMediaControls } from '@vueuse/core'
import { onMounted, useTemplateRef } from 'vue'

const video = useTemplateRef('video')
const { playing, currentTime, duration, volume } = useMediaControls(video, {
  src: 'video.mp4',
})

// Change initial media properties
onMounted(() => {
  volume.value = 0.5
  currentTime.value = 60
})
</script>

<template>
  <video ref="video" />
  <button @click="playing = !playing">
    Play / Pause
  </button>
  <span>{{ currentTime }} / {{ duration }}</span>
</template>
```

### Providing Captions, Subtitles, etc...

You can provide captions, subtitles, etc in the `tracks` options of the
`useMediaControls` function. The function will return an array of tracks
along with two functions for controlling them, `enableTrack`, `disableTrack`, and `selectedTrack`.
Using these you can manage the currently selected track. `selectedTrack` will
be `-1` if there is no selected track.

```vue
<script setup lang="ts">
import { useMediaControls } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const video = useTemplateRef('video')
const {
  tracks,
  enableTrack
} = useMediaControls(video, {
  src: 'video.mp4',
  tracks: [
    {
      default: true,
      src: './subtitles.vtt',
      kind: 'subtitles',
      label: 'English',
      srcLang: 'en',
    },
  ]
})
</script>

<template>
  <video ref="video" />
  <button v-for="track in tracks" :key="track.id" @click="enableTrack(track)">
    {{ track.label }}
  </button>
</template>
```

## Type Declarations

```ts
/**
 * Many of the jsdoc definitions here are modified version of the
 * documentation from MDN(https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
 */
export interface UseMediaSource {
  /**
   * The source url for the media
   */
  src: string
  /**
   * The media codec type
   */
  type?: string
  /**
   * Specifies the media query for the resource's intended media.
   */
  media?: string
}
export interface UseMediaTextTrackSource {
  /**
   * Indicates that the track should be enabled unless the user's preferences indicate
   * that another track is more appropriate
   */
  default?: boolean
  /**
   * How the text track is meant to be used. If omitted the default kind is subtitles.
   */
  kind: TextTrackKind
  /**
   * A user-readable title of the text track which is used by the browser
   * when listing available text tracks.
   */
  label: string
  /**
   * Address of the track (.vtt file). Must be a valid URL. This attribute
   * must be specified and its URL value must have the same origin as the document
   */
  src: string
  /**
   * Language of the track text data. It must be a valid BCP 47 language tag.
   * If the kind attribute is set to subtitles, then srclang must be defined.
   */
  srcLang: string
}
interface UseMediaControlsOptions extends ConfigurableDocument {
  /**
   * The source for the media, may either be a string, a `UseMediaSource` object, or a list
   * of `UseMediaSource` objects.
   */
  src?: MaybeRefOrGetter<string | UseMediaSource | UseMediaSource[]>
  /**
   * A list of text tracks for the media
   */
  tracks?: MaybeRefOrGetter<UseMediaTextTrackSource[]>
}
export interface UseMediaTextTrack {
  /**
   * The index of the text track
   */
  id: number
  /**
   * The text track label
   */
  label: string
  /**
   * Language of the track text data. It must be a valid BCP 47 language tag.
   * If the kind attribute is set to subtitles, then srclang must be defined.
   */
  language: string
  /**
   * Specifies the display mode of the text track, either `disabled`,
   * `hidden`, or `showing`
   */
  mode: TextTrackMode
  /**
   * How the text track is meant to be used. If omitted the default kind is subtitles.
   */
  kind: TextTrackKind
  /**
   * Indicates the track's in-band metadata track dispatch type.
   */
  inBandMetadataTrackDispatchType: string
  /**
   * A list of text track cues
   */
  cues: TextTrackCueList | null
  /**
   * A list of active text track cues
   */
  activeCues: TextTrackCueList | null
}
export interface UseMediaControlsReturn {
  currentTime: ShallowRef<number>
  duration: ShallowRef<number>
  waiting: ShallowRef<boolean>
  seeking: ShallowRef<boolean>
  ended: ShallowRef<boolean>
  stalled: ShallowRef<boolean>
  buffered: Ref<[number, number][]>
  playing: ShallowRef<boolean>
  rate: ShallowRef<number>
  volume: ShallowRef<number>
  muted: ShallowRef<boolean>
  tracks: Ref<UseMediaTextTrack[]>
  selectedTrack: ShallowRef<number>
  enableTrack: (
    track: number | UseMediaTextTrack,
    disableTracks?: boolean,
  ) => void
  disableTrack: (track?: number | UseMediaTextTrack) => void
  supportsPictureInPicture: boolean
  togglePictureInPicture: () => Promise<PictureInPictureWindow | void>
  isPictureInPicture: ShallowRef<boolean>
  onSourceError: EventHookOn<Event>
  onPlaybackError: EventHookOn<Event>
}
export declare function useMediaControls(
  target: MaybeRef<HTMLMediaElement | null | undefined>,
  options?: UseMediaControlsOptions,
): UseMediaControlsReturn
```
```

## File: `skills/vueuse-functions/references/useMediaQuery.md`
```markdown
---
category: Browser
---

# useMediaQuery

Reactive [Media Query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Testing_media_queries). Once you've created a MediaQueryList object, you can check the result of the query or receive notifications when the result changes.

## Usage

```ts
import { useMediaQuery } from '@vueuse/core'

const isLargeScreen = useMediaQuery('(min-width: 1024px)')
const isPreferredDark = useMediaQuery('(prefers-color-scheme: dark)')
```

#### Server Side Rendering and Nuxt

If you are using `useMediaQuery` with SSR enabled, then you need to specify which screen size you would like to render on the server and before hydration to avoid an hydration mismatch

```ts
import { useMediaQuery } from '@vueuse/core'

const isLarge = useMediaQuery('(min-width: 1024px)', {
  ssrWidth: 768 // Will enable SSR mode and render like if the screen was 768px wide
})

console.log(isLarge.value) // always false because ssrWidth of 768px is smaller than 1024px
onMounted(() => {
  console.log(isLarge.value) // false if screen is smaller than 1024px, true if larger than 1024px
})
```

Alternatively you can set this up globally for your app using [`provideSSRWidth`](../INDEX.md)

## Type Declarations

```ts
/**
 * Reactive Media Query.
 *
 * @see https://vueuse.org/useMediaQuery
 * @param query
 * @param options
 */
export declare function useMediaQuery(
  query: MaybeRefOrGetter<string>,
  options?: ConfigurableWindow & {
    ssrWidth?: number
  },
): ComputedRef<boolean>
```
```

## File: `skills/vueuse-functions/references/useMemoize.md`
```markdown
---
category: Utilities
---

# useMemoize

Cache results of functions depending on arguments and keep it reactive. It can also be used for asynchronous functions and will reuse existing promises to avoid fetching the same data at the same time.

::: tip
The results are not cleared automatically. Call `clear()` in case you no longer need the results or use own caching mechanism to avoid memory leaks.
:::

## Usage

```ts
import { useMemoize } from '@vueuse/core'

const getUser = useMemoize(
  async (userId: number): Promise<UserData> =>
    axios.get(`users/${userId}`).then(({ data }) => data),
)

const user1 = await getUser(1) // Request users/1
const user2 = await getUser(2) // Request users/2
// ...
const user1 = await getUser(1) // Retrieve from cache

// ...
const user1 = await getUser.load(1) // Request users/1

// ...
getUser.delete(1) // Delete cache from user 1
getUser.clear() // Clear full cache
```

Combine with `computed` or `computedAsync` to achieve reactivity:

```ts
import { computedAsync, useMemoize } from '@vueuse/core'

const getUser = useMemoize(
  async (userId: number): Promise<UserData> =>
    axios.get(`users/${userId}`).then(({ data }) => data),
)
// ---cut---
const user1 = computedAsync(() => getUser(1))
// ...
await getUser.load(1) // Will also update user1
```

### Resolving cache key

The key for caching is determined by the arguments given to the function and will be serialized by default with `JSON.stringify`.
This will allow equal objects to receive the same cache key. In case you want to customize the key you can pass `getKey`

::: warning Performance Consideration
Using `JSON.stringify` as the default key generator can be **slow for large or complex objects**. For better performance with complex arguments, it's highly recommended to provide a custom `getKey` function that generates keys based on primitive values or unique identifiers.
:::

#### Basic Example

```ts
import { useMemoize } from '@vueuse/core'
// ---cut---
const getUser = useMemoize(
  async (userId: number, headers: AxiosRequestHeaders): Promise<UserData> =>
    axios.get(`users/${userId}`, { headers }).then(({ data }) => data),
  {
    // Use only userId to get/set cache and ignore headers
    getKey: (userId, headers) => userId,
  },
)
```

### Customize cache mechanism

By default, the results are cached within a `Map`. You can implement your own mechanism by passing `cache` as options with following structure:

```ts
export interface MemoizeCache<Key, Value> {
  /**
   * Get value for key
   */
  get: (key: Key) => Value | undefined
  /**
   * Set value for key
   */
  set: (key: Key, value: Value) => void
  /**
   * Return flag if key exists
   */
  has: (key: Key) => boolean
  /**
   * Delete value for key
   */
  delete: (key: Key) => void
  /**
   * Clear cache
   */
  clear: () => void
}
```

## Type Declarations

```ts
type CacheKey = any
/**
 * Custom memoize cache handler
 */
export interface UseMemoizeCache<Key, Value> {
  /**
   * Get value for key
   */
  get: (key: Key) => Value | undefined
  /**
   * Set value for key
   */
  set: (key: Key, value: Value) => void
  /**
   * Return flag if key exists
   */
  has: (key: Key) => boolean
  /**
   * Delete value for key
   */
  delete: (key: Key) => void
  /**
   * Clear cache
   */
  clear: () => void
}
/**
 * Memoized function
 */
export interface UseMemoizeReturn<Result, Args extends unknown[]> {
  /**
   * Get result from cache or call memoized function
   */
  (...args: Args): Result
  /**
   * Call memoized function and update cache
   */
  load: (...args: Args) => Result
  /**
   * Delete cache of given arguments
   */
  delete: (...args: Args) => void
  /**
   * Clear cache
   */
  clear: () => void
  /**
   * Generate cache key for given arguments
   */
  generateKey: (...args: Args) => CacheKey
  /**
   * Cache container
   */
  cache: UseMemoizeCache<CacheKey, Result>
}
export interface UseMemoizeOptions<Result, Args extends unknown[]> {
  getKey?: (...args: Args) => string | number
  cache?: UseMemoizeCache<CacheKey, Result>
}
/**
 * Reactive function result cache based on arguments
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useMemoize<Result, Args extends unknown[]>(
  resolver: (...args: Args) => Result,
  options?: UseMemoizeOptions<Result, Args>,
): UseMemoizeReturn<Result, Args>
```
```

## File: `skills/vueuse-functions/references/useMemory.md`
```markdown
---
category: Browser
---

# useMemory

Reactive Memory Info.

## Usage

```ts
import { useMemory } from '@vueuse/core'

const { isSupported, memory } = useMemory()
```

## Type Declarations

```ts
/**
 * Performance.memory
 *
 * @see https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory
 */
export interface MemoryInfo {
  /**
   * The maximum size of the heap, in bytes, that is available to the context.
   */
  readonly jsHeapSizeLimit: number
  /**
   *  The total allocated heap size, in bytes.
   */
  readonly totalJSHeapSize: number
  /**
   * The currently active segment of JS heap, in bytes.
   */
  readonly usedJSHeapSize: number
  [Symbol.toStringTag]: "MemoryInfo"
}
export interface UseMemoryOptions extends ConfigurableScheduler {
  /**
   * Start the timer immediately
   *
   * @deprecated Please use `scheduler` option instead
   * @default true
   */
  immediate?: boolean
  /**
   * Execute the callback immediately after calling `resume`
   *
   * @deprecated Please use `scheduler` option instead
   * @default false
   */
  immediateCallback?: boolean
  /** @deprecated Please use `scheduler` option instead */
  interval?: number
}
export interface UseMemoryReturn extends Supportable {
  memory: Ref<MemoryInfo | undefined>
}
/**
 * Reactive Memory Info.
 *
 * @see https://vueuse.org/useMemory
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useMemory(options?: UseMemoryOptions): UseMemoryReturn
```
```

## File: `skills/vueuse-functions/references/useMin.md`
```markdown
---
category: '@Math'
---

# useMin

Reactive `Math.min`.

## Usage

```ts
import { useMin } from '@vueuse/math'

const array = ref([1, 2, 3, 4])
const min = useMin(array) // Ref<1>
```

```ts
import { useMin } from '@vueuse/math'

const a = ref(1)
const b = ref(3)

const min = useMin(a, b, 2) // Ref<1>
```

## Type Declarations

```ts
export declare function useMin(
  array: MaybeRefOrGetter<MaybeRefOrGetter<number>[]>,
): ComputedRef<number>
export declare function useMin(
  ...args: MaybeRefOrGetter<number>[]
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useMounted.md`
```markdown
---
category: Component
---

# useMounted

Mounted state in ref.

## Usage

```ts
import { useMounted } from '@vueuse/core'

const isMounted = useMounted()
```

Which is essentially a shorthand of:

```ts
const isMounted = ref(false)

onMounted(() => {
  isMounted.value = true
})
```

## Type Declarations

```ts
/**
 * Mounted state in ref.
 *
 * @see https://vueuse.org/useMounted
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useMounted(): ShallowRef<boolean, boolean>
```
```

## File: `skills/vueuse-functions/references/useMouse.md`
```markdown
---
category: Sensors
---

# useMouse

Reactive mouse position

## Basic Usage

```ts twoslash
import { useMouse } from '@vueuse/core'

const { x, y, sourceType } = useMouse()
```

Touch is enabled by default. To only detect mouse changes, set `touch` to `false`.
The `dragover` event is used to track mouse position while dragging.

```ts twoslash
import { useMouse } from '@vueuse/core'
// ---cut---
const { x, y } = useMouse({ touch: false })
```

## Custom Extractor

It's also possible to provide a custom extractor function to get the position from the event.

```ts twoslash
import type { UseMouseEventExtractor } from '@vueuse/core'
import { useMouse, useParentElement } from '@vueuse/core'

const parentEl = useParentElement()

const extractor: UseMouseEventExtractor = event => (
  event instanceof MouseEvent
    ? [event.offsetX, event.offsetY]
    : null
)

const { x, y, sourceType } = useMouse({ target: parentEl, type: extractor })
```

## Component Usage

```vue
<template>
  <UseMouse v-slot="{ x, y }">
    x: {{ x }}
    y: {{ y }}
  </UseMouse>
</template>
```

## Type Declarations

```ts
export type UseMouseCoordType = "page" | "client" | "screen" | "movement"
export type UseMouseSourceType = "mouse" | "touch" | null
export type UseMouseEventExtractor = (
  event: MouseEvent | Touch,
) => [x: number, y: number] | null | undefined
export interface UseMouseOptions
  extends ConfigurableWindow, ConfigurableEventFilter {
  /**
   * Mouse position based by page, client, screen, or relative to previous position
   *
   * @default 'page'
   */
  type?: UseMouseCoordType | UseMouseEventExtractor
  /**
   * Listen events on `target` element
   *
   * @default 'Window'
   */
  target?: MaybeRefOrGetter<Window | EventTarget | null | undefined>
  /**
   * Listen to `touchmove` events
   *
   * @default true
   */
  touch?: boolean
  /**
   * Listen to `scroll` events on window, only effective on type `page`
   *
   * @default true
   */
  scroll?: boolean
  /**
   * Reset to initial value when `touchend` event fired
   *
   * @default false
   */
  resetOnTouchEnds?: boolean
  /**
   * Initial values
   */
  initialValue?: Position
}
export interface UseMouseReturn {
  x: ShallowRef<number>
  y: ShallowRef<number>
  sourceType: ShallowRef<UseMouseSourceType>
}
/**
 * Reactive mouse position.
 *
 * @see https://vueuse.org/useMouse
 * @param options
 */
export declare function useMouse(options?: UseMouseOptions): UseMouseReturn
```
```

## File: `skills/vueuse-functions/references/useMouseInElement.md`
```markdown
---
category: Elements
---

# useMouseInElement

Reactive mouse position related to an element

## Usage

```vue
<script setup lang="ts">
import { useMouseInElement } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const target = useTemplateRef('target')

const { x, y, isOutside } = useMouseInElement(target)
</script>

<template>
  <div ref="target">
    <h1>Hello world</h1>
  </div>
</template>
```

## Component Usage

```vue
<template>
  <UseMouseInElement v-slot="{ elementX, elementY, isOutside }">
    x: {{ elementX }}
    y: {{ elementY }}
    Is Outside: {{ isOutside }}
  </UseMouseInElement>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vMouseInElement } from '@vueuse/components'
import { UseMouseSourceType } from '@vueuse/core'

interface MouseInElementType {
  x: number
  y: number
  sourceType: UseMouseSourceType
  elementX: number
  elementY: number
  elementPositionX: number
  elementPositionY: number
  elementHeight: number
  elementWidth: number
  isOutside: boolean
}

const options = {
  handleOutside: true
}
function onMouseInElement({ x, y, sourceType, elementX, elementY, elementPositionX, elementPositionY, elementHeight, elementWidth, isOutside }: MouseInElementType) {
  console.log(x, y, sourceType, elementX, elementY, elementPositionX, elementPositionY, elementHeight, elementWidth, isOutside)
}
</script>

<template>
  <textarea v-mouse-in-element="onMouseInElement" />
  <!-- with options -->
  <textarea v-mouse-in-element="[onMouseInElement, options]" />
</template>
```

## Type Declarations

```ts
export interface MouseInElementOptions extends UseMouseOptions {
  /**
   * Whether to handle mouse events when the cursor is outside the target element.
   * When enabled, mouse position will continue to be tracked even when outside the element bounds.
   *
   * @default true
   */
  handleOutside?: boolean
  /**
   * Listen to window resize event
   *
   * @default true
   */
  windowScroll?: boolean
  /**
   * Listen to window scroll event
   *
   * @default true
   */
  windowResize?: boolean
}
export interface UseMouseInElementReturn extends UseMouseReturn {
  elementX: ShallowRef<number>
  elementY: ShallowRef<number>
  elementPositionX: ShallowRef<number>
  elementPositionY: ShallowRef<number>
  elementHeight: ShallowRef<number>
  elementWidth: ShallowRef<number>
  isOutside: ShallowRef<boolean>
  stop: () => void
}
/**
 * Reactive mouse position related to an element.
 *
 * @see https://vueuse.org/useMouseInElement
 * @param target
 * @param options
 */
export declare function useMouseInElement(
  target?: MaybeElementRef,
  options?: MouseInElementOptions,
): {
  x: ShallowRef<number>
  y: ShallowRef<number>
  sourceType: ShallowRef<UseMouseSourceType>
  elementX: ShallowRef<number, number>
  elementY: ShallowRef<number, number>
  elementPositionX: ShallowRef<number, number>
  elementPositionY: ShallowRef<number, number>
  elementHeight: ShallowRef<number, number>
  elementWidth: ShallowRef<number, number>
  isOutside: ShallowRef<boolean, boolean>
  stop: () => void
}
```
```

## File: `skills/vueuse-functions/references/useMousePressed.md`
```markdown
---
category: Sensors
---

# useMousePressed

Reactive mouse pressing state. Triggered by `mousedown` `touchstart` on target element and released by `mouseup` `mouseleave` `touchend` `touchcancel` on window.

## Basic Usage

```ts
import { useMousePressed } from '@vueuse/core'

const { pressed } = useMousePressed()
```

Touching is enabled by default. To make it only detects mouse changes, set `touch` to `false`

```ts
import { useMousePressed } from '@vueuse/core'
// ---cut---
const { pressed } = useMousePressed({ touch: false })
```

To only capture `mousedown` and `touchstart` on specific element, you can specify `target` by passing a ref of the element.

```vue
<script setup lang="ts">
import { useMousePressed } from '@vueuse/core'
// ---cut---
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')

const { pressed } = useMousePressed({ target: el })
</script>

<template>
  <div ref="el">
    Only clicking on this element will trigger the update.
  </div>
</template>
```

## Component Usage

```vue
<template>
  <UseMousePressed v-slot="{ pressed }">
    Is Pressed: {{ pressed }}
  </UseMousePressed>
</template>
```

## Type Declarations

```ts
export interface UseMousePressedOptions extends ConfigurableWindow {
  /**
   * Listen to `touchstart` `touchend` events
   *
   * @default true
   */
  touch?: boolean
  /**
   * Listen to `dragstart` `drop` and `dragend` events
   *
   * @default true
   */
  drag?: boolean
  /**
   * Add event listeners with the `capture` option set to `true`
   * (see [MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#capture))
   *
   * @default false
   */
  capture?: boolean
  /**
   * Initial values
   *
   * @default false
   */
  initialValue?: boolean
  /**
   * Element target to be capture the click
   */
  target?: MaybeComputedElementRef
  /**
   * Callback to be called when the mouse is pressed
   *
   * @param event
   */
  onPressed?: (event: MouseEvent | TouchEvent | DragEvent) => void
  /**
   * Callback to be called when the mouse is released
   *
   * @param event
   */
  onReleased?: (event: MouseEvent | TouchEvent | DragEvent) => void
}
/** @deprecated use {@link UseMousePressedOptions} instead */
export type MousePressedOptions = UseMousePressedOptions
export interface UseMousePressedReturn {
  pressed: ShallowRef<boolean>
  sourceType: ShallowRef<UseMouseSourceType>
}
/**
 * Reactive mouse pressing state.
 *
 * @see https://vueuse.org/useMousePressed
 * @param options
 */
export declare function useMousePressed(
  options?: UseMousePressedOptions,
): UseMousePressedReturn
```
```

## File: `skills/vueuse-functions/references/useMutationObserver.md`
```markdown
---
category: Elements
---

# useMutationObserver

Watch for changes being made to the DOM tree. [MutationObserver MDN](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)

## Usage

```vue
<script setup lang="ts">
import { useMutationObserver } from '@vueuse/core'
import { ref, useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const messages = ref([])

useMutationObserver(el, (mutations) => {
  if (mutations[0])
    messages.value.push(mutations[0].attributeName)
}, {
  attributes: true,
})
</script>

<template>
  <div ref="el">
    Hello VueUse
  </div>
</template>
```

## Type Declarations

```ts
export interface UseMutationObserverOptions
  extends MutationObserverInit, ConfigurableWindow {}
export interface UseMutationObserverReturn extends Supportable {
  stop: () => void
  takeRecords: () => MutationRecord[] | undefined
}
/**
 * Watch for changes being made to the DOM tree.
 *
 * @see https://vueuse.org/useMutationObserver
 * @see https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver MutationObserver MDN
 * @param target
 * @param callback
 * @param options
 */
export declare function useMutationObserver(
  target:
    | MaybeComputedElementRef
    | MaybeComputedElementRef[]
    | MaybeRefOrGetter<MaybeElement[]>,
  callback: MutationCallback,
  options?: UseMutationObserverOptions,
): UseMutationObserverReturn
```
```

## File: `skills/vueuse-functions/references/useNProgress.md`
```markdown
---
category: '@Integrations'
---

# useNProgress

Reactive wrapper for [`nprogress`](https://github.com/rstacruz/nprogress).

## Install

```bash
npm i nprogress@^0
```

## Usage

```ts {6}
import { useNProgress } from '@vueuse/integrations/useNProgress'

const { isLoading } = useNProgress()

function toggle() {
  isLoading.value = !isLoading.value
}
```

### Passing a progress percentage

You can pass a percentage to indicate where the bar should start from.

```ts {3}
import { useNProgress } from '@vueuse/integrations/useNProgress'

const { progress } = useNProgress(0.5)

function done() {
  progress.value = 1.0
}
```

> To change the progress percentage, set `progress.value = n`, where n is a number between 0..1.

### Customization

Just edit [nprogress.css](https://github.com/rstacruz/nprogress/blob/master/nprogress.css) to your liking. Tip: you probably only want to find and replace occurrences of #29d.

You can [configure](https://github.com/rstacruz/nprogress#configuration) it by passing an object as a second parameter.

```ts {4}
import { useNProgress } from '@vueuse/integrations/useNProgress'

useNProgress(null, {
  minimum: 0.1,
  // ...
})
```

## Type Declarations

```ts
export type UseNProgressOptions = Partial<NProgressOptions>
export interface UseNProgressReturn {
  isLoading: WritableComputedRef<boolean, boolean>
  progress: Ref<number | null | undefined>
  start: () => NProgress
  done: (force?: boolean) => NProgress
  remove: () => void
}
/**
 * Reactive progress bar.
 *
 * @see https://vueuse.org/useNProgress
 */
export declare function useNProgress(
  currentProgress?: MaybeRefOrGetter<number | null | undefined>,
  options?: UseNProgressOptions,
): UseNProgressReturn
```
```

## File: `skills/vueuse-functions/references/useNavigatorLanguage.md`
```markdown
---
category: Sensors
---

# useNavigatorLanguage

Reactive [navigator.language](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language).

## Usage

```ts
import { useNavigatorLanguage } from '@vueuse/core'

const { language } = useNavigatorLanguage()

watch(language, () => {
  // Listen to the value changing
})
```

## Type Declarations

```ts
export interface NavigatorLanguageState extends Supportable {
  /**
   *
   * ISO 639-1 standard Language Code
   *
   * @info The detected user agent language preference as a language tag
   * (which is sometimes referred to as a "locale identifier").
   * This consists of a 2-3 letter base language tag that indicates a
   * language, optionally followed by additional subtags separated by
   * '-'. The most common extra information is the country or region
   * variant (like 'en-US' or 'fr-CA').
   *
   *
   * @see https://www.iso.org/iso-639-language-codes.html
   * @see https://www.loc.gov/standards/iso639-2/php/code_list.php
   *
   */
  language: ShallowRef<string | undefined>
}
export interface UseNavigatorLanguageOptions extends ConfigurableWindow {}
export type UseNavigatorLanguageReturn = Readonly<NavigatorLanguageState>
/**
 *
 * Reactive useNavigatorLanguage
 *
 * Detects the currently selected user language and returns a reactive language
 * @see https://vueuse.org/useNavigatorLanguage
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useNavigatorLanguage(
  options?: UseNavigatorLanguageOptions,
): UseNavigatorLanguageReturn
```
```

## File: `skills/vueuse-functions/references/useNetwork.md`
```markdown
---
category: Sensors
---

# useNetwork

Reactive [Network status](https://developer.mozilla.org/en-US/docs/Web/API/Network_Information_API). The Network Information API provides information about the system's connection in terms of general connection type (e.g., 'wifi', 'cellular', etc.). This can be used to select high definition content or low definition content based on the user's connection. The entire API consists of the addition of the NetworkInformation interface and a single property to the Navigator interface: Navigator.connection.

## Usage

```ts
import { useNetwork } from '@vueuse/core'

const { isOnline, offlineAt, downlink, downlinkMax, effectiveType, saveData, type } = useNetwork()

console.log(isOnline.value)
```

To use as an object, wrap it with `reactive()`

```ts
import { useNetwork } from '@vueuse/core'
// ---cut---
import { reactive } from 'vue'

const network = reactive(useNetwork())

console.log(network.isOnline)
```

## Component Usage

```vue
<template>
  <UseNetwork v-slot="{ isOnline, type }">
    Is Online: {{ isOnline }}
    Type: {{ type }}
  </UseNetwork>
</template>
```

## Type Declarations

```ts
export interface UseNetworkOptions extends ConfigurableWindow {}
export type NetworkType =
  | "bluetooth"
  | "cellular"
  | "ethernet"
  | "none"
  | "wifi"
  | "wimax"
  | "other"
  | "unknown"
export type NetworkEffectiveType = "slow-2g" | "2g" | "3g" | "4g" | undefined
export interface NetworkState extends Supportable {
  /**
   * If the user is currently connected.
   */
  isOnline: Readonly<ShallowRef<boolean>>
  /**
   * The time since the user was last connected.
   */
  offlineAt: Readonly<ShallowRef<number | undefined>>
  /**
   * At this time, if the user is offline and reconnects
   */
  onlineAt: Readonly<ShallowRef<number | undefined>>
  /**
   * The download speed in Mbps.
   */
  downlink: Readonly<ShallowRef<number | undefined>>
  /**
   * The max reachable download speed in Mbps.
   */
  downlinkMax: Readonly<ShallowRef<number | undefined>>
  /**
   * The detected effective speed type.
   */
  effectiveType: Readonly<ShallowRef<NetworkEffectiveType | undefined>>
  /**
   * The estimated effective round-trip time of the current connection.
   */
  rtt: Readonly<ShallowRef<number | undefined>>
  /**
   * If the user activated data saver mode.
   */
  saveData: Readonly<ShallowRef<boolean | undefined>>
  /**
   * The detected connection/network type.
   */
  type: Readonly<ShallowRef<NetworkType>>
}
export type UseNetworkReturn = Readonly<NetworkState>
/**
 * Reactive Network status.
 *
 * @see https://vueuse.org/useNetwork
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useNetwork(
  options?: UseNetworkOptions,
): UseNetworkReturn
```
```

## File: `skills/vueuse-functions/references/useNow.md`
```markdown
---
category: Animation
---

# useNow

Reactive current Date instance.

## Usage

```ts
import { useNow } from '@vueuse/core'

const now = useNow()
```

```ts
import { useNow } from '@vueuse/core'
// ---cut---
const { now, pause, resume } = useNow({ controls: true })
```

## Component Usage

```vue
<template>
  <UseNow v-slot="{ now, pause, resume }">
    Now: {{ now }}
    <button @click="pause()">
      Pause
    </button>
    <button @click="resume()">
      Resume
    </button>
  </UseNow>
</template>
```

## Type Declarations

```ts
export interface UseNowOptions<
  Controls extends boolean,
> extends ConfigurableScheduler {
  /**
   * Expose more controls
   *
   * @default false
   */
  controls?: Controls
  /**
   * Start the clock immediately
   *
   * @deprecated Please use `scheduler` option instead
   * @default true
   */
  immediate?: boolean
  /**
   * Update interval in milliseconds, or use requestAnimationFrame
   *
   * @deprecated Please use `scheduler` option instead
   * @default requestAnimationFrame
   */
  interval?: "requestAnimationFrame" | number
}
export type UseNowReturn<Controls extends boolean> = Controls extends true
  ? {
      now: Ref<Date>
    } & Pausable
  : Ref<Date>
/**
 * Reactive current Date instance.
 *
 * @see https://vueuse.org/useNow
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useNow(options?: UseNowOptions<false>): Ref<Date>
export declare function useNow(options: UseNowOptions<true>): {
  now: Ref<Date>
} & Pausable
```
```

## File: `skills/vueuse-functions/references/useObjectUrl.md`
```markdown
---
category: Browser
---

# useObjectUrl

Reactive URL representing an object.

Creates an URL for the provided `File`, `Blob`, or `MediaSource` via [URL.createObjectURL()](https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL) and automatically releases the URL via [URL.revokeObjectURL()](https://developer.mozilla.org/en-US/docs/Web/API/URL/revokeObjectURL) when the source changes or the component is unmounted.

## Usage

```vue
<script setup lang="ts">
import { useObjectUrl } from '@vueuse/core'
import { shallowRef } from 'vue'

const file = shallowRef()
const url = useObjectUrl(file)

function onFileChange(event) {
  file.value = event.target.files[0]
}
</script>

<template>
  <input type="file" @change="onFileChange">

  <a :href="url">Open file</a>
</template>
```

## Component Usage

```vue
<template>
  <UseObjectUrl v-slot="url" :object="file">
    <a :href="url">Open file</a>
  </UseObjectUrl>
</template>
```

## Type Declarations

```ts
/**
 * Reactive URL representing an object.
 *
 * @see https://vueuse.org/useObjectUrl
 * @param object
 */
export declare function useObjectUrl(
  object: MaybeRefOrGetter<Blob | MediaSource | null | undefined>,
): Readonly<Ref<string | undefined, string | undefined>>
```
```

## File: `skills/vueuse-functions/references/useObservable.md`
```markdown
---
category: '@RxJS'
---

# useObservable

Use an RxJS [`Observable`](https://rxjs.dev/guide/observable), return a `ref`, and automatically unsubscribe from it when the component is unmounted.

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { useObservable } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { mapTo, scan, startWith } from 'rxjs/operators'

// setup()
const count = useObservable(
  interval(1000).pipe(
    mapTo(1),
    startWith(0),
    scan((total, next) => next + total),
  ),
)
```

### Initial Value

You can provide an initial value that will be used before the Observable emits its first value:

```ts no-twoslash
import { useObservable } from '@vueuse/rxjs'
import { interval } from 'rxjs'

const count = useObservable(
  interval(1000),
  { initialValue: 0 },
)
// count.value is 0 until the first emission
```

### Error Handling

If you want to add custom error handling to an `Observable` that might error, you can supply an optional `onError` configuration. Without this, RxJS will treat any error in the supplied `Observable` as an "unhandled error" and it will be thrown in a new call stack and reported to `window.onerror` (or `process.on('error')` if you happen to be in Node).

```ts no-twoslash
import { useObservable } from '@vueuse/rxjs'
import { interval } from 'rxjs'
import { map } from 'rxjs/operators'

// setup()
const count = useObservable(
  interval(1000).pipe(
    map((n) => {
      if (n === 10)
        throw new Error('oops')

      return n + n
    }),
  ),
  {
    onError: (err) => {
      console.log(err.message) // "oops"
    },
  },
)
```

### Options

| Option         | Type                 | Description                              |
| -------------- | -------------------- | ---------------------------------------- |
| `initialValue` | `T`                  | Value to use before the Observable emits |
| `onError`      | `(err: any) => void` | Error handler for Observable errors      |

## Type Declarations

```ts
export interface UseObservableOptions<I> {
  onError?: (err: any) => void
  /**
   * The value that should be set if the observable has not emitted.
   */
  initialValue?: I | undefined
}
export declare function useObservable<H, I = undefined>(
  observable: Observable<H>,
  options?: UseObservableOptions<I | undefined>,
): Readonly<Ref<H | I>>
```
```

## File: `skills/vueuse-functions/references/useOffsetPagination.md`
```markdown
---
category: Utilities
---

# useOffsetPagination

Reactive offset pagination.

## Usage

```ts
import { useOffsetPagination } from '@vueuse/core'

function fetchData({ currentPage, currentPageSize }: { currentPage: number, currentPageSize: number }) {
  fetch(currentPage, currentPageSize).then((responseData) => {
    data.value = responseData
  })
}

const {
  currentPage,
  currentPageSize,
  pageCount,
  isFirstPage,
  isLastPage,
  prev,
  next,
} = useOffsetPagination({
  total: database.value.length,
  page: 1,
  pageSize: 10,
  onPageChange: fetchData,
  onPageSizeChange: fetchData,
})
```

## Component Usage

```vue
<template>
  <UseOffsetPagination
    v-slot="{
      currentPage,
      currentPageSize,
      next,
      prev,
      pageCount,
      isFirstPage,
      isLastPage,
    }"
    :total="database.length"
    @page-change="fetchData"
    @page-size-change="fetchData"
  >
    <div class="gap-x-4 gap-y-2 grid-cols-2 inline-grid items-center">
      <div opacity="50">
        total:
      </div>
      <div>{{ database.length }}</div>
      <div opacity="50">
        pageCount:
      </div>
      <div>{{ pageCount }}</div>
      <div opacity="50">
        currentPageSize:
      </div>
      <div>{{ currentPageSize }}</div>
      <div opacity="50">
        currentPage:
      </div>
      <div>{{ currentPage }}</div>
      <div opacity="50">
        isFirstPage:
      </div>
      <div>{{ isFirstPage }}</div>
      <div opacity="50">
        isLastPage:
      </div>
      <div>{{ isLastPage }}</div>
    </div>
    <div>
      <button :disabled="isFirstPage" @click="prev">
        prev
      </button>
      <button :disabled="isLastPage" @click="next">
        next
      </button>
    </div>
  </UseOffsetPagination>
</template>
```

Component event supported props event callback and event listener.

event listener:

```vue
<template>
  <UseOffsetPagination
    v-slot="{
      currentPage,
      currentPageSize,
      next,
      prev,
      pageCount,
      isFirstPage,
      isLastPage,
    }"
    :total="database.length"
    @page-change="fetchData"
    @page-size-change="fetchData"
    @page-count-change="onPageCountChange"
  >
    <!-- your code -->
  </UseOffsetPagination>
</template>
```

or props event callback:

```vue
<template>
  <UseOffsetPagination
    v-slot="{
      currentPage,
      currentPageSize,
      next,
      prev,
      pageCount,
      isFirstPage,
      isLastPage,
    }"
    :total="database.length"
    :on-page-change="fetchData"
    :on-page-size-change="fetchData"
    :on-page-count-change="onPageCountChange"
  >
    <!-- your code -->
  </UseOffsetPagination>
</template>
```

## Type Declarations

```ts
export interface UseOffsetPaginationOptions {
  /**
   * Total number of items.
   */
  total?: MaybeRefOrGetter<number>
  /**
   * The number of items to display per page.
   * @default 10
   */
  pageSize?: MaybeRefOrGetter<number>
  /**
   * The current page number.
   * @default 1
   */
  page?: MaybeRef<number>
  /**
   * Callback when the `page` change.
   */
  onPageChange?: (
    returnValue: UnwrapNestedRefs<UseOffsetPaginationReturn>,
  ) => unknown
  /**
   * Callback when the `pageSize` change.
   */
  onPageSizeChange?: (
    returnValue: UnwrapNestedRefs<UseOffsetPaginationReturn>,
  ) => unknown
  /**
   * Callback when the `pageCount` change.
   */
  onPageCountChange?: (
    returnValue: UnwrapNestedRefs<UseOffsetPaginationReturn>,
  ) => unknown
}
export interface UseOffsetPaginationReturn {
  currentPage: Ref<number>
  currentPageSize: Ref<number>
  pageCount: ComputedRef<number>
  isFirstPage: ComputedRef<boolean>
  isLastPage: ComputedRef<boolean>
  prev: () => void
  next: () => void
}
export type UseOffsetPaginationInfinityPageReturn = Omit<
  UseOffsetPaginationReturn,
  "isLastPage"
>
export declare function useOffsetPagination(
  options: Omit<UseOffsetPaginationOptions, "total">,
): UseOffsetPaginationInfinityPageReturn
export declare function useOffsetPagination(
  options: UseOffsetPaginationOptions,
): UseOffsetPaginationReturn
```
```

## File: `skills/vueuse-functions/references/useOnline.md`
```markdown
---
category: Sensors
---

# useOnline

Reactive online state. A wrapper of `useNetwork`.

## Usage

```ts
import { useOnline } from '@vueuse/core'

const online = useOnline()
```

## Component Usage

```vue
<template>
  <UseOnline v-slot="{ isOnline }">
    Is Online: {{ isOnline }}
  </UseOnline>
</template>
```

## Type Declarations

```ts
/**
 * Reactive online state.
 *
 * @see https://vueuse.org/useOnline
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useOnline(
  options?: ConfigurableWindow,
): Readonly<ShallowRef<boolean>>
```
```

## File: `skills/vueuse-functions/references/usePageLeave.md`
```markdown
---
category: Sensors
---

# usePageLeave

Reactive state to show whether the mouse leaves the page.

## Usage

```ts
import { usePageLeave } from '@vueuse/core'

const isLeft = usePageLeave()
```

## Component Usage

```vue
<template>
  <UsePageLeave v-slot="{ isLeft }">
    Has Left Page: {{ isLeft }}
  </UsePageLeave>
</template>
```

## Type Declarations

```ts
export interface UsePageLeaveOptions extends ConfigurableWindow {}
export type UsePageLeaveReturn = ShallowRef<boolean>
/**
 * Reactive state to show whether mouse leaves the page.
 *
 * @see https://vueuse.org/usePageLeave
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePageLeave(
  options?: UsePageLeaveOptions,
): UsePageLeaveReturn
```
```

## File: `skills/vueuse-functions/references/useParallax.md`
```markdown
---
category: Sensors
---

# useParallax

Create parallax effect easily. It uses `useDeviceOrientation` and fallback to `useMouse` if orientation is not supported.

## Usage

```vue
<script setup lang="ts">
import { useParallax } from '@vueuse/core'

const container = ref(null)
const { tilt, roll, source } = useParallax(container)
</script>

<template>
  <div ref="container" />
</template>
```

## Type Declarations

```ts
export interface UseParallaxOptions extends ConfigurableWindow {
  deviceOrientationTiltAdjust?: (i: number) => number
  deviceOrientationRollAdjust?: (i: number) => number
  mouseTiltAdjust?: (i: number) => number
  mouseRollAdjust?: (i: number) => number
}
export interface UseParallaxReturn {
  /**
   * Roll value. Scaled to `-0.5 ~ 0.5`
   */
  roll: ComputedRef<number>
  /**
   * Tilt value. Scaled to `-0.5 ~ 0.5`
   */
  tilt: ComputedRef<number>
  /**
   * Sensor source, can be `mouse` or `deviceOrientation`
   */
  source: ComputedRef<"deviceOrientation" | "mouse">
}
/**
 * Create parallax effect easily. It uses `useDeviceOrientation` and fallback to `useMouse`
 * if orientation is not supported.
 *
 * @param target
 * @param options
 */
export declare function useParallax(
  target: MaybeElementRef,
  options?: UseParallaxOptions,
): UseParallaxReturn
```
```

## File: `skills/vueuse-functions/references/useParentElement.md`
```markdown
---
category: Elements
---

# useParentElement

Get parent element of the given element

## Usage

When no argument is passed, it will return the parent element of the current component.

```vue
<script setup lang="ts">
import { useParentElement } from '@vueuse/core'

const parentEl = useParentElement()

onMounted(() => {
  console.log(parentEl.value)
})
</script>
```

It can also accept a `ref` as the first argument.

```vue
<script setup lang="ts">
import { useParentElement } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const tooltip = useTemplateRef('tooltip')

const tooltipWrapper = useParentElement(tooltip)

onMounted(() => {
  console.log(tooltipWrapper.value)
})
</script>

<template>
  <div>
    <p ref="tooltip" />
  </div>
</template>
```

## Type Declarations

```ts
export declare function useParentElement(
  element?: MaybeRefOrGetter<HTMLElement | SVGElement | null | undefined>,
): Readonly<ShallowRef<HTMLElement | SVGElement | null | undefined>>
```
```

## File: `skills/vueuse-functions/references/usePerformanceObserver.md`
```markdown
---
category: Browser
---

# usePerformanceObserver

Observe performance metrics.

## Usage

```ts
import { usePerformanceObserver } from '@vueuse/core'

const entrys = ref<PerformanceEntry[]>([])
usePerformanceObserver({
  entryTypes: ['paint'],
}, (list) => {
  entrys.value = list.getEntries()
})
```

## Type Declarations

```ts
export type UsePerformanceObserverOptions = PerformanceObserverInit &
  ConfigurableWindow & {
    /**
     * Start the observer immediate.
     *
     * @default true
     */
    immediate?: boolean
  }
/**
 * Observe performance metrics.
 *
 * @see https://vueuse.org/usePerformanceObserver
 * @param options
 */
export declare function usePerformanceObserver(
  options: UsePerformanceObserverOptions,
  callback: PerformanceObserverCallback,
): {
  isSupported: UseSupportedReturn
  start: () => void
  stop: () => void
}
```
```

## File: `skills/vueuse-functions/references/usePermission.md`
```markdown
---
category: Browser
---

# usePermission

Reactive [Permissions API](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API). The Permissions API provides the tools to allow developers to implement a better user experience as far as permissions are concerned.

## Usage

```ts
import { usePermission } from '@vueuse/core'

const microphoneAccess = usePermission('microphone')
```

## Type Declarations

```ts
type DescriptorNamePolyfill =
  | "accelerometer"
  | "accessibility-events"
  | "ambient-light-sensor"
  | "background-sync"
  | "camera"
  | "clipboard-read"
  | "clipboard-write"
  | "gyroscope"
  | "magnetometer"
  | "microphone"
  | "notifications"
  | "payment-handler"
  | "persistent-storage"
  | "push"
  | "speaker"
  | "local-fonts"
export type GeneralPermissionDescriptor =
  | PermissionDescriptor
  | {
      name: DescriptorNamePolyfill
    }
export interface UsePermissionOptions<
  Controls extends boolean,
> extends ConfigurableNavigator {
  /**
   * Expose more controls
   *
   * @default false
   */
  controls?: Controls
}
export type UsePermissionReturn = Readonly<
  ShallowRef<PermissionState | undefined>
>
export interface UsePermissionReturnWithControls extends Supportable {
  state: UsePermissionReturn
  query: () => Promise<PermissionStatus | undefined>
}
/**
 * Reactive Permissions API.
 *
 * @see https://vueuse.org/usePermission
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePermission(
  permissionDesc:
    | GeneralPermissionDescriptor
    | GeneralPermissionDescriptor["name"],
  options?: UsePermissionOptions<false>,
): UsePermissionReturn
export declare function usePermission(
  permissionDesc:
    | GeneralPermissionDescriptor
    | GeneralPermissionDescriptor["name"],
  options: UsePermissionOptions<true>,
): UsePermissionReturnWithControls
```
```

## File: `skills/vueuse-functions/references/usePointer.md`
```markdown
---
category: Sensors
---

# usePointer

Reactive [pointer state](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events).

## Basic Usage

```ts
import { usePointer } from '@vueuse/core'

const { x, y, pressure, pointerType } = usePointer()
```

## Component Usage

By default, the component will track the pointer on `window`

```vue
<template>
  <UsePointer v-slot="{ x, y }">
    x: {{ x }}
    y: {{ y }}
  </UsePointer>
</template>
```

To track local position in the element, set `target="self"`:

```vue
<template>
  <UsePointer v-slot="{ x, y }" target="self">
    x: {{ x }} y: {{ y }}
  </UsePointer>
</template>
```

## Type Declarations

```ts
export interface UsePointerState extends Position {
  pressure: number
  pointerId: number
  tiltX: number
  tiltY: number
  width: number
  height: number
  twist: number
  pointerType: PointerType | null
}
export interface UsePointerOptions extends ConfigurableWindow {
  /**
   * Pointer types that listen to.
   *
   * @default ['mouse', 'touch', 'pen']
   */
  pointerTypes?: PointerType[]
  /**
   * Initial values
   */
  initialValue?: MaybeRef<Partial<UsePointerState>>
  /**
   * @default window
   */
  target?: MaybeRef<EventTarget | null | undefined> | Document | Window
}
export interface UsePointerReturn {
  pressure: Ref<number>
  pointerId: Ref<number>
  tiltX: Ref<number>
  tiltY: Ref<number>
  width: Ref<number>
  height: Ref<number>
  twist: Ref<number>
  pointerType: Ref<PointerType | null>
  x: Ref<number>
  y: Ref<number>
  isInside: ShallowRef<boolean>
}
/**
 * Reactive pointer state.
 *
 * @see https://vueuse.org/usePointer
 * @param options
 */
export declare function usePointer(
  options?: UsePointerOptions,
): UsePointerReturn
```
```

## File: `skills/vueuse-functions/references/usePointerLock.md`
```markdown
---
category: Sensors
---

# usePointerLock

Reactive [pointer lock](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API).

## Basic Usage

```ts
import { usePointerLock } from '@vueuse/core'

const {
  isSupported,
  lock,
  unlock,
  element,
  triggerElement
} = usePointerLock()
```

## Component Usage

```vue
<template>
  <UsePointerLock v-slot="{ lock }">
    <canvas />
    <button @click="lock">
      Lock Pointer on Canvas
    </button>
  </UsePointerLock>
</template>
```

## Type Declarations

```ts
export interface UsePointerLockOptions extends ConfigurableDocument {}
export interface UsePointerLockReturn extends Supportable {
  element: ShallowRef<MaybeElement>
  triggerElement: ShallowRef<MaybeElement>
  lock: (e: MaybeElementRef | Event) => Promise<MaybeElement>
  unlock: () => Promise<boolean>
}
/**
 * Reactive pointer lock.
 *
 * @see https://vueuse.org/usePointerLock
 * @param target
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePointerLock(
  target?: MaybeElementRef,
  options?: UsePointerLockOptions,
): UsePointerLockReturn
```
```

## File: `skills/vueuse-functions/references/usePointerSwipe.md`
```markdown
---
category: Sensors
---

# usePointerSwipe

Reactive swipe detection based on [PointerEvents](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent).

## Usage

```vue
<script setup lang="ts">
import { usePointerSwipe } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { isSwiping, direction } = usePointerSwipe(el)
</script>

<template>
  <div ref="el">
    Swipe here
  </div>
</template>
```

## Type Declarations

```ts
export interface UsePointerSwipeOptions {
  /**
   * @default 50
   */
  threshold?: number
  /**
   * Callback on swipe start.
   */
  onSwipeStart?: (e: PointerEvent) => void
  /**
   * Callback on swipe move.
   */
  onSwipe?: (e: PointerEvent) => void
  /**
   * Callback on swipe end.
   */
  onSwipeEnd?: (e: PointerEvent, direction: UseSwipeDirection) => void
  /**
   * Pointer types to listen to.
   *
   * @default ['mouse', 'touch', 'pen']
   */
  pointerTypes?: PointerType[]
  /**
   * Disable text selection on swipe.
   *
   * @default false
   */
  disableTextSelect?: boolean
}
export interface UsePointerSwipeReturn {
  readonly isSwiping: ShallowRef<boolean>
  direction: Readonly<ShallowRef<UseSwipeDirection>>
  readonly posStart: Position
  readonly posEnd: Position
  distanceX: Readonly<ComputedRef<number>>
  distanceY: Readonly<ComputedRef<number>>
  stop: () => void
}
/**
 * Reactive swipe detection based on PointerEvents.
 *
 * @see https://vueuse.org/usePointerSwipe
 * @param target
 * @param options
 */
export declare function usePointerSwipe(
  target: MaybeRefOrGetter<HTMLElement | null | undefined>,
  options?: UsePointerSwipeOptions,
): UsePointerSwipeReturn
```
```

## File: `skills/vueuse-functions/references/usePrecision.md`
```markdown
---
category: '@Math'
---

# usePrecision

Reactively set the precision of a number.

## Usage

```ts
import { usePrecision } from '@vueuse/math'

const value = ref(3.1415)
const result = usePrecision(value, 2) // 3.14

const ceilResult = usePrecision(value, 2, {
  math: 'ceil'
}) // 3.15

const floorResult = usePrecision(value, 3, {
  math: 'floor'
}) // 3.141
```

## Type Declarations

```ts
export interface UsePrecisionOptions {
  /**
   * Method to use for rounding
   *
   * @default 'round'
   */
  math?: "floor" | "ceil" | "round"
}
/**
 * Reactively set the precision of a number.
 *
 * @see https://vueuse.org/usePrecision
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePrecision(
  value: MaybeRefOrGetter<number>,
  digits: MaybeRefOrGetter<number>,
  options?: MaybeRefOrGetter<UsePrecisionOptions>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/usePreferredColorScheme.md`
```markdown
---
category: Browser
---

# usePreferredColorScheme

Reactive [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media query.

## Usage

```ts
import { usePreferredColorScheme } from '@vueuse/core'

const preferredColor = usePreferredColorScheme()
```

## Component Usage

```vue
<template>
  <UsePreferredColorScheme v-slot="{ colorScheme }">
    Preferred Color Scheme: {{ colorScheme }}
  </UsePreferredColorScheme>
</template>
```

## Type Declarations

```ts
export type ColorSchemeType = "dark" | "light" | "no-preference"
/**
 * Reactive prefers-color-scheme media query.
 *
 * @see https://vueuse.org/usePreferredColorScheme
 * @param [options]
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePreferredColorScheme(
  options?: ConfigurableWindow,
): ComputedRef<ColorSchemeType>
```
```

## File: `skills/vueuse-functions/references/usePreferredContrast.md`
```markdown
---
category: Browser
---

# usePreferredContrast

Reactive [prefers-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast) media query.

## Usage

```ts
import { usePreferredContrast } from '@vueuse/core'

const preferredContrast = usePreferredContrast()
```

## Component Usage

```vue
<template>
  <UsePreferredContrast v-slot="{ contrast }">
    Preferred Contrast: {{ contrast }}
  </UsePreferredContrast>
</template>
```

## Type Declarations

```ts
export type ContrastType = "more" | "less" | "custom" | "no-preference"
/**
 * Reactive prefers-contrast media query.
 *
 * @see https://vueuse.org/usePreferredContrast
 * @param [options]
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePreferredContrast(
  options?: ConfigurableWindow,
): ComputedRef<ContrastType>
```
```

## File: `skills/vueuse-functions/references/usePreferredDark.md`
```markdown
---
category: Browser
---

# usePreferredDark

Reactive dark theme preference.

## Usage

```ts
import { usePreferredDark } from '@vueuse/core'

const isDark = usePreferredDark()
```

## Component Usage

```vue
<template>
  <UsePreferredDark v-slot="{ prefersDark }">
    Prefers Dark: {{ prefersDark }}
  </UsePreferredDark>
</template>
```

## Type Declarations

```ts
/**
 * Reactive dark theme preference.
 *
 * @see https://vueuse.org/usePreferredDark
 * @param [options]
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePreferredDark(
  options?: ConfigurableWindow,
): ComputedRef<boolean>
```
```

## File: `skills/vueuse-functions/references/usePreferredLanguages.md`
```markdown
---
category: Browser
---

# usePreferredLanguages

Reactive [Navigator Languages](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorLanguage/languages). It provides web developers with information about the user's preferred languages. For example, this may be useful to adjust the language of the user interface based on the user's preferred languages in order to provide better experience.

## Usage

```ts
import { usePreferredLanguages } from '@vueuse/core'

const languages = usePreferredLanguages()
```

## Component Usage

```vue
<template>
  <UsePreferredLanguages v-slot="{ languages }">
    Preferred Languages: {{ languages }}
  </UsePreferredLanguages>
</template>
```

## Type Declarations

```ts
/**
 * Reactive Navigator Languages.
 *
 * @see https://vueuse.org/usePreferredLanguages
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePreferredLanguages(
  options?: ConfigurableWindow,
): ShallowRef<readonly string[]>
```
```

## File: `skills/vueuse-functions/references/usePreferredReducedMotion.md`
```markdown
---
category: Browser
---

# usePreferredReducedMotion

Reactive [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) media query.

## Usage

```ts
import { usePreferredReducedMotion } from '@vueuse/core'

const preferredMotion = usePreferredReducedMotion()
```

## Component Usage

```vue
<template>
  <UsePreferredReducedMotion v-slot="{ motion }">
    Preferred Reduced Motion: {{ motion }}
  </UsePreferredReducedMotion>
</template>
```

## Type Declarations

```ts
export type ReducedMotionType = "reduce" | "no-preference"
/**
 * Reactive prefers-reduced-motion media query.
 *
 * @see https://vueuse.org/usePreferredReducedMotion
 * @param [options]
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePreferredReducedMotion(
  options?: ConfigurableWindow,
): ComputedRef<ReducedMotionType>
```
```

## File: `skills/vueuse-functions/references/usePreferredReducedTransparency.md`
```markdown
---
category: Browser
---

# usePreferredReducedTransparency

Reactive [prefers-reduced-transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-transparency) media query.

## Usage

```ts
import { usePreferredReducedTransparency } from '@vueuse/core'

const preferredTransparency = usePreferredReducedTransparency()
```

## Component Usage

```vue
<template>
  <UsePreferredReducedTransparency v-slot="{ transparency }">
    Preferred Reduced transparency: {{ transparency }}
  </UsePreferredReducedTransparency>
</template>
```

## Type Declarations

```ts
export type ReducedTransparencyType = "reduce" | "no-preference"
/**
 * Reactive prefers-reduced-transparency media query.
 *
 * @see https://vueuse.org/usePreferredReducedTransparency
 * @param [options]
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function usePreferredReducedTransparency(
  options?: ConfigurableWindow,
): ComputedRef<ReducedTransparencyType>
```
```

## File: `skills/vueuse-functions/references/usePrevious.md`
```markdown
---
category: Utilities
---

# usePrevious

Holds the previous value of a ref.

## Usage

```ts
import { usePrevious } from '@vueuse/core'
import { shallowRef } from 'vue'

const counter = shallowRef('Hello')
const previous = usePrevious(counter)

console.log(previous.value) // undefined

counter.value = 'World'

console.log(previous.value) // Hello
```

## Type Declarations

```ts
/**
 * Holds the previous value of a ref.
 *
 * @see   {@link https://vueuse.org/usePrevious}
 */
export declare function usePrevious<T>(
  value: MaybeRefOrGetter<T>,
): Readonly<ShallowRef<T | undefined>>
export declare function usePrevious<T>(
  value: MaybeRefOrGetter<T>,
  initialValue: T,
): Readonly<ShallowRef<T>>
```
```

## File: `skills/vueuse-functions/references/useProjection.md`
```markdown
---
category: '@Math'
related: createGenericProjection
---

# useProjection

Reactive numeric projection from one domain to another.

## Usage

```ts
import { useProjection } from '@vueuse/math'

const input = ref(0)
const projected = useProjection(input, [0, 10], [0, 100])

input.value = 5 // projected.value === 50
input.value = 10 // projected.value === 100
```

## Type Declarations

```ts
/**
 * Reactive numeric projection from one domain to another.
 *
 * @see https://vueuse.org/useProjection
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useProjection(
  input: MaybeRefOrGetter<number>,
  fromDomain: MaybeRefOrGetter<readonly [number, number]>,
  toDomain: MaybeRefOrGetter<readonly [number, number]>,
  projector?: ProjectorFunction<number, number>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useQRCode.md`
```markdown
---
category: '@Integrations'
---

# useQRCode

Wrapper for [`qrcode`](https://github.com/soldair/node-qrcode).

## Install

```bash
npm i qrcode@^1
```

## Usage

```ts
import { useQRCode } from '@vueuse/integrations/useQRCode'

// `qrcode` will be a ref of data URL
const qrcode = useQRCode('text-to-encode')
```

or passing a `ref` to it, the returned data URL ref will change along with the source ref's changes.

```ts
import { useQRCode } from '@vueuse/integrations/useQRCode'
import { shallowRef } from 'vue'

const text = shallowRef('text-to-encode')
const qrcode = useQRCode(text)
```

```html
<input v-model="text" type="text" />
<img :src="qrcode" alt="QR Code" />
```

## Type Declarations

```ts
/**
 * Wrapper for qrcode.
 *
 * @see https://vueuse.org/useQRCode
 * @param text
 * @param options
 */
export declare function useQRCode(
  text: MaybeRefOrGetter<string>,
  options?: QRCode.QRCodeToDataURLOptions,
): ShallowRef<string, string>
```
```

## File: `skills/vueuse-functions/references/useRTDB.md`
```markdown
---
category: '@Firebase'
---

# useRTDB

Reactive [Firebase Realtime Database](https://firebase.google.com/docs/database) binding. Making it straightforward to **always keep your local data in sync** with remotes databases.

## Usage

```ts
import { useRTDB } from '@vueuse/firebase/useRTDB'
import { initializeApp } from 'firebase/app'
import { getDatabase } from 'firebase/database'

const app = initializeApp({ /* config */ })
const db = getDatabase(app)

// in setup()
const todos = useRTDB(db.ref('todos'))
```

## Options

| Option         | Type                   | Default         | Description                                               |
| -------------- | ---------------------- | --------------- | --------------------------------------------------------- |
| `autoDispose`  | `boolean`              | `true`          | Automatically unsubscribe when the component is unmounted |
| `errorHandler` | `(err: Error) => void` | `console.error` | Custom error handler for database errors                  |

## Return Value

Returns a `Ref<T | undefined>` that is automatically updated when the database value changes.

## Reusing Database References

You can reuse the db reference by passing `autoDispose: false`

```ts
const todos = useRTDB(db.ref('todos'), { autoDispose: false })
```

or use `createGlobalState` from the core package

```ts twoslash include store
// @filename: store.ts
// ---cut---
// store.ts
import { createGlobalState } from '@vueuse/core'
import { useRTDB } from '@vueuse/firebase/useRTDB'

export const useTodos = createGlobalState(
  () => useRTDB(db.ref('todos')),
)
```

```vue
<!-- app.vue -->
<script setup lang="ts">
// @include: store
// ---cut---
import { useTodos } from './store'

const todos = useTodos()
</script>
```

## Type Declarations

```ts
export interface UseRTDBOptions {
  errorHandler?: (err: Error) => void
  autoDispose?: boolean
}
/**
 * Reactive Firebase Realtime Database binding.
 *
 * @see https://vueuse.org/useRTDB
 */
export declare function useRTDB<T = any>(
  docRef: DatabaseReference,
  options?: UseRTDBOptions,
): Ref<T | undefined, T | undefined>
```
```

## File: `skills/vueuse-functions/references/useRafFn.md`
```markdown
---
category: Animation
---

# useRafFn

Call function on every `requestAnimationFrame`. With controls of pausing and resuming.

## Usage

```ts
import { useRafFn } from '@vueuse/core'
import { shallowRef } from 'vue'

const count = shallowRef(0)

const { pause, resume } = useRafFn(() => {
  count.value++
  console.log(count.value)
})
```

## Type Declarations

```ts
export interface UseRafFnCallbackArguments {
  /**
   * Time elapsed between this and the last frame.
   */
  delta: number
  /**
   * Time elapsed since the creation of the web page. See {@link https://developer.mozilla.org/en-US/docs/Web/API/DOMHighResTimeStamp#the_time_origin Time origin}.
   */
  timestamp: DOMHighResTimeStamp
}
export interface UseRafFnOptions extends ConfigurableWindow {
  /**
   * Start the requestAnimationFrame loop immediately on creation
   *
   * @default true
   */
  immediate?: boolean
  /**
   * The maximum frame per second to execute the function.
   * Set to `null` to disable the limit.
   *
   * @default null
   */
  fpsLimit?: MaybeRefOrGetter<number | null>
  /**
   * After the requestAnimationFrame loop executed once, it will be automatically stopped.
   *
   * @default false
   */
  once?: boolean
}
/**
 * Call function on every `requestAnimationFrame`. With controls of pausing and resuming.
 *
 * @see https://vueuse.org/useRafFn
 * @param fn
 * @param options
 */
export declare function useRafFn(
  fn: (args: UseRafFnCallbackArguments) => void,
  options?: UseRafFnOptions,
): Pausable
```
```

## File: `skills/vueuse-functions/references/useRefHistory.md`
```markdown
---
category: State
related: useManualRefHistory
---

# useRefHistory

Track the change history of a ref, also provides undo and redo functionality

<CourseLink href="https://vueschool.io/lessons/ref-history-with-vueuse?friend=vueuse">Learn useRefHistory with this FREE video lesson from Vue School!</CourseLink>

## Usage

```ts {5} twoslash include usage
import { useRefHistory } from '@vueuse/core'
import { shallowRef } from 'vue'

const counter = shallowRef(0)
const { history, undo, redo } = useRefHistory(counter)
```

Internally, `watch` is used to trigger a history point when the ref value is modified. This means that history points are triggered asynchronously batching modifications in the same "tick".

```ts
// @include: usage
// ---cut---
counter.value += 1

await nextTick()
console.log(history.value)
/* [
  { snapshot: 1, timestamp: 1601912898062 },
  { snapshot: 0, timestamp: 1601912898061 }
] */
```

You can use `undo` to reset the ref value to the last history point.

```ts
// @include: usage
// ---cut---
console.log(counter.value) // 1
undo()
console.log(counter.value) // 0
```

### Objects / arrays

When working with objects or arrays, since changing their attributes does not change the reference, it will not trigger the committing. To track attribute changes, you would need to pass `deep: true`. It will create clones for each history record.

```ts
import { useRefHistory } from '@vueuse/core'
// ---cut---
const state = ref({
  foo: 1,
  bar: 'bar',
})

const { history, undo, redo } = useRefHistory(state, {
  deep: true,
})

state.value.foo = 2

await nextTick()
console.log(history.value)
/* [
  { snapshot: { foo: 2, bar: 'bar' } },
  { snapshot: { foo: 1, bar: 'bar' } }
] */
```

#### Custom Clone Function

`useRefHistory` only embeds the minimal clone function `x => JSON.parse(JSON.stringify(x))`. To use a full featured or custom clone function, you can set up via the `clone` options.

For example, using [structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone):

```ts
import { useRefHistory } from '@vueuse/core'

const refHistory = useRefHistory(target, { clone: structuredClone })
```

Or by using [lodash's `cloneDeep`](https://lodash.com/docs/4.17.15#cloneDeep):

```ts
import { useRefHistory } from '@vueuse/core'
import { cloneDeep } from 'lodash-es'

const refHistory = useRefHistory(target, { clone: cloneDeep })
```

Or a more lightweight [`klona`](https://github.com/lukeed/klona):

```ts
import { useRefHistory } from '@vueuse/core'
import { klona } from 'klona'

const refHistory = useRefHistory(target, { clone: klona })
```

#### Custom Dump and Parse Function

Instead of using the `clone` options, you can pass custom functions to control the serialization and parsing. In case you do not need history values to be objects, this can save an extra clone when undoing. It is also useful in case you want to have the snapshots already stringified to be saved to local storage for example.

```ts
import { useRefHistory } from '@vueuse/core'

const refHistory = useRefHistory(target, {
  dump: JSON.stringify,
  parse: JSON.parse,
})
```

### History Capacity

We will keep all the history by default (unlimited) until you explicitly clear them up, you can set the maximal amount of history to be kept by `capacity` options.

```ts
import { useRefHistory } from '@vueuse/core'
// ---cut---
const refHistory = useRefHistory(target, {
  capacity: 15, // limit to 15 history records
})

refHistory.clear() // explicitly clear all the history
```

### History WatchOptionFlush Timing

From [Vue's documentation](https://vuejs.org/guide/essentials/watchers.html#callback-flush-timing): Vue's reactivity system buffers invalidated effects and flush them asynchronously to avoid unnecessary duplicate invocation when there are many state mutations happening in the same "tick".

In the same way as `watch`, you can modify the flush timing using the `flush` option.

```ts
import { useRefHistory } from '@vueuse/core'
// ---cut---
const refHistory = useRefHistory(target, {
  flush: 'sync', // options 'pre' (default), 'post' and 'sync'
})
```

The default is `'pre'`, to align this composable with the default for Vue's watchers. This also helps to avoid common issues, like several history points generated as part of a multi-step update to a ref value that can break invariants of the app state. You can use `commit()` in case you need to create multiple history points in the same "tick"

```ts
import { useRefHistory } from '@vueuse/core'
// ---cut---
const r = shallowRef(0)
const { history, commit } = useRefHistory(r)

r.value = 1
commit()

r.value = 2
commit()

console.log(history.value)
/* [
  { snapshot: 2 },
  { snapshot: 1 },
  { snapshot: 0 },
] */
```

On the other hand, when using flush `'sync'`, you can use `batch(fn)` to generate a single history point for several sync operations

```ts
import { useRefHistory } from '@vueuse/core'
// ---cut---
const r = ref({ names: [], version: 1 })
const { history, batch } = useRefHistory(r, { flush: 'sync' })

batch(() => {
  r.value.names.push('Lena')
  r.value.version++
})

console.log(history.value)
/* [
  { snapshot: { names: [ 'Lena' ], version: 2 },
  { snapshot: { names: [], version: 1 },
] */
```

If `{ flush: 'sync', deep: true }` is used, `batch` is also useful when doing a mutable `splice` in an array. `splice` can generate up to three atomic operations that will be pushed to the ref history.

```ts
import { useRefHistory } from '@vueuse/core'
// ---cut---
const arr = ref([1, 2, 3])
const { history, batch } = useRefHistory(arr, { deep: true, flush: 'sync' })

batch(() => {
  arr.value.splice(1, 1) // batch ensures only one history point is generated
})
```

Another option is to avoid mutating the original ref value using `arr.value = [...arr.value].splice(1,1)`.

## Recommended Readings

- [History and Persistence](https://patak.dev/vue/history-and-persistence.html) - by [@patak-dev](https://github.com/patak-dev)

## Type Declarations

```ts
export interface UseRefHistoryOptions<Raw, Serialized = Raw>
  extends ConfigurableEventFilter, ConfigurableFlush {
  /**
   * Watch for deep changes, default to false
   *
   * When set to true, it will also create clones for values store in the history
   *
   * @default false
   */
  deep?: boolean
  /**
   * Maximum number of history to be kept. Default to unlimited.
   */
  capacity?: number
  /**
   * Clone when taking a snapshot, shortcut for dump: JSON.parse(JSON.stringify(value)).
   * Default to false
   *
   * @default false
   */
  clone?: boolean | CloneFn<Raw>
  /**
   * Serialize data into the history
   */
  dump?: (v: Raw) => Serialized
  /**
   * Deserialize data from the history
   */
  parse?: (v: Serialized) => Raw
  /**
   * Function to determine if the commit should proceed
   * @param oldValue Previous value
   * @param newValue New value
   * @returns boolean indicating if commit should proceed
   */
  shouldCommit?: (oldValue: Raw | undefined, newValue: Raw) => boolean
}
export interface UseRefHistoryReturn<
  Raw,
  Serialized,
> extends UseManualRefHistoryReturn<Raw, Serialized> {
  /**
   * A ref representing if the tracking is enabled
   */
  isTracking: Ref<boolean>
  /**
   * Pause change tracking
   */
  pause: () => void
  /**
   * Resume change tracking
   *
   * @param [commit] if true, a history record will be create after resuming
   */
  resume: (commit?: boolean) => void
  /**
   * A sugar for auto pause and auto resuming within a function scope
   *
   * @param fn
   */
  batch: (fn: (cancel: Fn) => void) => void
  /**
   * Clear the data and stop the watch
   */
  dispose: () => void
}
/**
 * Track the change history of a ref, also provides undo and redo functionality.
 *
 * @see https://vueuse.org/useRefHistory
 * @param source
 * @param options
 */
export declare function useRefHistory<Raw, Serialized = Raw>(
  source: Ref<Raw>,
  options?: UseRefHistoryOptions<Raw, Serialized>,
): UseRefHistoryReturn<Raw, Serialized>
```
```

## File: `skills/vueuse-functions/references/useResizeObserver.md`
```markdown
---
category: Elements
---

# useResizeObserver

Reports changes to the dimensions of an Element's content or the border-box

## Usage

```vue
<script setup lang="ts">
import { useResizeObserver } from '@vueuse/core'
import { ref, useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const text = ref('')

useResizeObserver(el, (entries) => {
  const entry = entries[0]
  const { width, height } = entry.contentRect
  text.value = `width: ${width}, height: ${height}`
})
</script>

<template>
  <div ref="el">
    {{ text }}
  </div>
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vResizeObserver } from '@vueuse/components'

const text = ref('')

function onResizeObserver(entries) {
  const [entry] = entries
  const { width, height } = entry.contentRect
  text.value = `width: ${width}, height: ${height}`
}
</script>

<template>
  <div v-resize-observer="onResizeObserver">
    {{ text }}
  </div>
</template>
```

[ResizeObserver MDN](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)

## Type Declarations

```ts
/**
 * @deprecated This interface is now available in the DOM lib.
 * Use the global {@link globalThis.ResizeObserverSize} instead.
 */
export interface ResizeObserverSize {
  readonly inlineSize: number
  readonly blockSize: number
}
/**
 * @deprecated This interface is now available in the DOM lib.
 * Use the global {@link globalThis.ResizeObserverEntry} instead.
 */
export interface ResizeObserverEntry {
  readonly target: Element
  readonly contentRect: DOMRectReadOnly
  readonly borderBoxSize: ReadonlyArray<ResizeObserverSize>
  readonly contentBoxSize: ReadonlyArray<ResizeObserverSize>
  readonly devicePixelContentBoxSize: ReadonlyArray<ResizeObserverSize>
}
/**
 * @deprecated This interface is now available in the DOM lib.
 * Use the global {@link globalThis.ResizeObserverCallback} instead.
 */
export type ResizeObserverCallback = (
  entries: ReadonlyArray<ResizeObserverEntry>,
  observer: ResizeObserver,
) => void
export interface UseResizeObserverOptions
  extends ResizeObserverOptions, ConfigurableWindow {}
export interface UseResizeObserverReturn extends Supportable {
  stop: () => void
}
/**
 * Reports changes to the dimensions of an Element's content or the border-box
 *
 * @see https://vueuse.org/useResizeObserver
 * @param target
 * @param callback
 * @param options
 */
export declare function useResizeObserver(
  target:
    | MaybeComputedElementRef
    | MaybeComputedElementRef[]
    | MaybeRefOrGetter<MaybeElement[]>,
  callback: globalThis.ResizeObserverCallback,
  options?: UseResizeObserverOptions,
): UseResizeObserverReturn
```
```

## File: `skills/vueuse-functions/references/useRound.md`
```markdown
---
category: '@Math'
---

# useRound

Reactive `Math.round`.

## Usage

```ts
import { useRound } from '@vueuse/math'

const value = ref(20.49)
const result = useRound(value) // 20
```

## Type Declarations

```ts
/**
 * Reactive `Math.round`.
 *
 * @see https://vueuse.org/useRound
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useRound(
  value: MaybeRefOrGetter<number>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useRouteHash.md`
```markdown
---
category: '@Router'
---

# useRouteHash

Shorthand for a reactive `route.hash`.

## Usage

```ts
import { useRouteHash } from '@vueuse/router'

const search = useRouteHash()

console.log(search.value) // route.hash
search.value = 'foobar' // router.replace({ hash: 'foobar' })
```

## Type Declarations

```ts
export declare function useRouteHash(
  defaultValue?: MaybeRefOrGetter<RouteHashValueRaw>,
  { mode, route, router }?: ReactiveRouteOptions,
): Ref<RouteHashValueRaw, RouteHashValueRaw>
```
```

## File: `skills/vueuse-functions/references/useRouteParams.md`
```markdown
---
category: '@Router'
---

# useRouteParams

Shorthand for a reactive `route.params`.

## Usage

```ts
import { useRouteParams } from '@vueuse/router'

const userId = useRouteParams('userId')

const userId = useRouteParams('userId', '-1') // or with a default value

const userId = useRouteParams('page', '1', { transform: Number }) // or transforming value

console.log(userId.value) // route.params.userId
userId.value = '100' // router.replace({ params: { userId: '100' } })
```

## Type Declarations

```ts
export declare function useRouteParams(
  name: string,
): Ref<null | string | string[]>
export declare function useRouteParams<
  T extends RouteParamValueRaw = RouteParamValueRaw,
  K = T,
>(
  name: string,
  defaultValue?: MaybeRefOrGetter<T>,
  options?: ReactiveRouteOptionsWithTransform<T, K>,
): Ref<K>
```
```

## File: `skills/vueuse-functions/references/useRouteQuery.md`
```markdown
---
category: '@Router'
---

# useRouteQuery

Shorthand for a reactive `route.query`. Updates the URL query parameters when the ref changes.

## Usage

```ts
import { useRouteQuery } from '@vueuse/router'

const search = useRouteQuery('search')

const search = useRouteQuery('search', 'foo') // or with a default value

const page = useRouteQuery('page', '1', { transform: Number }) // or transforming value

console.log(search.value) // route.query.search
search.value = 'foobar' // router.replace({ query: { search: 'foobar' } })
```

### Navigation Mode

By default, changes use `router.replace()`. Set `mode: 'push'` to use `router.push()` instead.

```ts
import { useRouteQuery } from '@vueuse/router'

const search = useRouteQuery('search', '', { mode: 'push' })
```

### Bidirectional Transform

You can provide separate `get` and `set` transforms for reading and writing values.

```ts
import { useRouteQuery } from '@vueuse/router'

const filters = useRouteQuery('filters', [], {
  transform: {
    get: v => v ? v.split(',') : [],
    set: v => v.join(','),
  },
})

// Reading: 'a,b,c' -> ['a', 'b', 'c']
// Writing: ['a', 'b', 'c'] -> 'a,b,c'
```

### Default Value Behavior

When the value equals the default value, the query parameter is removed from the URL.

```ts
import { useRouteQuery } from '@vueuse/router'

const page = useRouteQuery('page', '1')

page.value = '2' // URL: ?page=2
page.value = '1' // URL: (no page param, since it equals default)
```

## Type Declarations

```ts
export declare function useRouteQuery(
  name: string,
): Ref<undefined | null | string | string[]>
export declare function useRouteQuery<
  T extends RouteQueryValueRaw = RouteQueryValueRaw,
  K = T,
>(
  name: string,
  defaultValue?: MaybeRefOrGetter<T>,
  options?: ReactiveRouteOptionsWithTransform<T, K>,
): Ref<K>
```
```

## File: `skills/vueuse-functions/references/useSSRWidth.md`
```markdown
---
category: Browser
---

# useSSRWidth

Used to set a global viewport width which will be used when rendering SSR components that rely on the viewport width like [`useMediaQuery`](../INDEX.md) or [`useBreakpoints`](../INDEX.md)

## Usage

```ts
import { provideSSRWidth } from '@vueuse/core'

const app = createApp(App)

provideSSRWidth(500, app)
```

Or in the root component

```vue
<script setup lang="ts">
import { provideSSRWidth } from '@vueuse/core'

provideSSRWidth(500)
</script>
```

To retrieve the provided value if you need it in a subcomponent

```vue
<script setup lang="ts">
import { useSSRWidth } from '@vueuse/core'

const width = useSSRWidth()
</script>
```

## Type Declarations

```ts
export declare function useSSRWidth(): number | undefined
export declare function provideSSRWidth(
  width: number | null,
  app?: App<unknown>,
): void
```
```

## File: `skills/vueuse-functions/references/useScreenOrientation.md`
```markdown
---
category: Browser
---

# useScreenOrientation

Reactive [Screen Orientation API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Orientation_API). It provides web developers with information about the user's current screen orientation.

## Usage

```ts
import { useScreenOrientation } from '@vueuse/core'

const {
  isSupported,
  orientation,
  angle,
  lockOrientation,
  unlockOrientation,
} = useScreenOrientation()
```

To lock the orientation, you can pass an [OrientationLockType](https://developer.mozilla.org/en-US/docs/Web/API/ScreenOrientation/type) to the lockOrientation function:

```ts
import { useScreenOrientation } from '@vueuse/core'

const {
  isSupported,
  orientation,
  angle,
  lockOrientation,
  unlockOrientation,
} = useScreenOrientation()

lockOrientation('portrait-primary')
```

and then unlock again, with the following:

```ts
import { useScreenOrientation } from '@vueuse/core'

const { unlockOrientation } = useScreenOrientation()
// ---cut---
unlockOrientation()
```

Accepted orientation types are one of `"landscape-primary"`, `"landscape-secondary"`, `"portrait-primary"`, `"portrait-secondary"`, `"any"`, `"landscape"`, `"natural"` and `"portrait"`.

[Screen Orientation API MDN](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Orientation_API)

## Type Declarations

```ts
export type OrientationType =
  | "portrait-primary"
  | "portrait-secondary"
  | "landscape-primary"
  | "landscape-secondary"
export type OrientationLockType =
  | "any"
  | "natural"
  | "landscape"
  | "portrait"
  | "portrait-primary"
  | "portrait-secondary"
  | "landscape-primary"
  | "landscape-secondary"
export interface ScreenOrientation extends EventTarget {
  lock: (orientation: OrientationLockType) => Promise<void>
  unlock: () => void
  readonly type: OrientationType
  readonly angle: number
  addEventListener: (
    type: "change",
    listener: (this: this, ev: Event) => any,
    useCapture?: boolean,
  ) => void
}
export interface UseScreenOrientationOptions extends ConfigurableWindow {}
export interface UseScreenOrientationReturn extends Supportable {
  orientation: Ref<OrientationType | undefined>
  angle: ShallowRef<number>
  lockOrientation: (type: OrientationLockType) => Promise<void>
  unlockOrientation: () => void
}
/**
 * Reactive screen orientation
 *
 * @see https://vueuse.org/useScreenOrientation
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useScreenOrientation(
  options?: UseScreenOrientationOptions,
): UseScreenOrientationReturn
```
```

## File: `skills/vueuse-functions/references/useScreenSafeArea.md`
```markdown
---
category: Browser
---

# useScreenSafeArea

Reactive `env(safe-area-inset-*)`

![image](https://webkit.org/wp-content/uploads/safe-areas-1.png)

## Usage

In order to make the page to be fully rendered in the screen, the additional attribute `viewport-fit=cover` within `viewport` meta tag must be set firstly, the viewport meta tag may look like this:

```html
<meta name="viewport" content="initial-scale=1, viewport-fit=cover" />
```

Then we could use `useScreenSafeArea` in the component as shown below:

```ts
import { useScreenSafeArea } from '@vueuse/core'

const {
  top,
  right,
  bottom,
  left,
} = useScreenSafeArea()
```

For further details, you may refer to this documentation: [Designing Websites for iPhone X](https://webkit.org/blog/7929/designing-websites-for-iphone-x/)

## Component Usage

```vue
<template>
  <UseScreenSafeArea top right bottom left>
    content
  </UseScreenSafeArea>
</template>
```

## Type Declarations

```ts
export interface UseScreenSafeAreaReturn {
  top: ShallowRef<string>
  right: ShallowRef<string>
  bottom: ShallowRef<string>
  left: ShallowRef<string>
  update: () => void
}
/**
 * Reactive `env(safe-area-inset-*)`
 *
 * @see https://vueuse.org/useScreenSafeArea
 */
export declare function useScreenSafeArea(): UseScreenSafeAreaReturn
```
```

## File: `skills/vueuse-functions/references/useScriptTag.md`
```markdown
---
category: Browser
---

# useScriptTag

Creates a script tag, with support for automatically unloading (deleting) the script tag on unmount.

If a script tag already exists for the given URL, `useScriptTag()` will not create another script tag, but keep in mind that depending on how you use it, `useScriptTag()` might have already loaded then unloaded that particular JS file from a previous call of `useScriptTag()`.

## Usage

```ts
import { useScriptTag } from '@vueuse/core'

useScriptTag(
  'https://player.twitch.tv/js/embed/v1.js',
  // on script tag loaded.
  (el: HTMLScriptElement) => {
    // do something
  },
)
```

The script will be automatically loaded when the component is mounted and removed when the component is unmounted.

## Configuration

Set `manual: true` to have manual control over the timing to load the script.

```ts
import { useScriptTag } from '@vueuse/core'

const { scriptTag, load, unload } = useScriptTag(
  'https://player.twitch.tv/js/embed/v1.js',
  () => {
    // do something
  },
  { manual: true },
)

// manual controls
await load()
await unload()
```

## Type Declarations

```ts
export interface UseScriptTagOptions extends ConfigurableDocument {
  /**
   * Load the script immediately
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Add `async` attribute to the script tag
   *
   * @default true
   */
  async?: boolean
  /**
   * Script type
   *
   * @default 'text/javascript'
   */
  type?: string
  /**
   * Manual controls the timing of loading and unloading
   *
   * @default false
   */
  manual?: boolean
  crossOrigin?: "anonymous" | "use-credentials"
  referrerPolicy?:
    | "no-referrer"
    | "no-referrer-when-downgrade"
    | "origin"
    | "origin-when-cross-origin"
    | "same-origin"
    | "strict-origin"
    | "strict-origin-when-cross-origin"
    | "unsafe-url"
  noModule?: boolean
  defer?: boolean
  /**
   * Add custom attribute to the script tag
   *
   */
  attrs?: Record<string, string>
  /**
   * Nonce value for CSP (Content Security Policy)
   * @default undefined
   */
  nonce?: string
}
export interface UseScriptTagReturn {
  scriptTag: ShallowRef<HTMLScriptElement | null>
  load: (waitForScriptLoad?: boolean) => Promise<HTMLScriptElement | boolean>
  unload: () => void
}
/**
 * Async script tag loading.
 *
 * @see https://vueuse.org/useScriptTag
 * @param src
 * @param onLoaded
 * @param options
 */
export declare function useScriptTag(
  src: MaybeRefOrGetter<string>,
  onLoaded?: (el: HTMLScriptElement) => void,
  options?: UseScriptTagOptions,
): UseScriptTagReturn
```
```

## File: `skills/vueuse-functions/references/useScroll.md`
```markdown
---
category: Sensors
---

# useScroll

Reactive scroll position and state.

## Usage

```vue
<script setup lang="ts">
import { useScroll } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { x, y, isScrolling, arrivedState, directions } = useScroll(el)
</script>

<template>
  <div ref="el" />
</template>
```

### With offsets

```ts
import { useScroll } from '@vueuse/core'
// ---cut---
const { x, y, isScrolling, arrivedState, directions } = useScroll(el, {
  offset: { top: 30, bottom: 30, right: 30, left: 30 },
})
```

### Setting scroll position

Set the `x` and `y` values to make the element scroll to that position.

```vue
<script setup lang="ts">
import { useScroll } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { x, y } = useScroll(el)
</script>

<template>
  <div ref="el" />
  <button @click="x += 10">
    Scroll right 10px
  </button>
  <button @click="y += 10">
    Scroll down 10px
  </button>
</template>
```

### Smooth scrolling

Set `behavior: smooth` to enable smooth scrolling. The `behavior` option defaults to `auto`, which means no smooth scrolling. See the `behavior` option on [`window.scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo) for more information.

```ts
import { useScroll } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { x, y } = useScroll(el, { behavior: 'smooth' })

// Or as a `ref`:
const smooth = ref(false)
const behavior = computed(() => smooth.value ? 'smooth' : 'auto')
const { x, y } = useScroll(el, { behavior })
```

### Recalculate scroll state

You can call the `measure()` method to manually update the scroll position and `arrivedState` at any time.

This is useful, for example, after dynamic content changes or when you want to recalculate the scroll state outside of scroll events.

```ts
import { useScroll } from '@vueuse/core'
import { nextTick, onMounted, useTemplateRef, watch } from 'vue'

const el = useTemplateRef('el')
const reactiveValue = shallowRef(false)

const { measure } = useScroll(el)

// In a watcher
watch(reactiveValue, () => {
  measure()
})

// Or inside any function
function updateScrollState() {
  // ...some logic
  nextTick(() => {
    measure()
  })
}
```

> [!NOTE]
> it's recommended to call `measure()` inside `nextTick()`, to ensure the DOM is updated first.
> The scroll state is initialized automatically `onMount`.
> You only need to call `measure()` manually if you want to recalculate the state after some dynamic changes.

## Directive Usage

```vue
<script setup lang="ts">
import type { UseScrollReturn } from '@vueuse/core'
import { vScroll } from '@vueuse/components'

const data = ref([1, 2, 3, 4, 5, 6])

function onScroll(state: UseScrollReturn) {
  console.log(state) // {x, y, isScrolling, arrivedState, directions}
}
</script>

<template>
  <div v-scroll="onScroll">
    <div v-for="item in data" :key="item">
      {{ item }}
    </div>
  </div>

  <!-- with options -->
  <div v-scroll="[onScroll, { throttle: 10 }]">
    <div v-for="item in data" :key="item">
      {{ item }}
    </div>
  </div>
</template>
```

## Type Declarations

```ts
export interface UseScrollOptions extends ConfigurableWindow {
  /**
   * Throttle time for scroll event, it’s disabled by default.
   *
   * @default 0
   */
  throttle?: number
  /**
   * The check time when scrolling ends.
   * This configuration will be setting to (throttle + idle) when the `throttle` is configured.
   *
   * @default 200
   */
  idle?: number
  /**
   * Offset arrived states by x pixels
   *
   */
  offset?: {
    left?: number
    right?: number
    top?: number
    bottom?: number
  }
  /**
   * Use MutationObserver to monitor specific DOM changes,
   * such as attribute modifications, child node additions or removals, or subtree changes.
   * @default { mutation: boolean }
   */
  observe?:
    | boolean
    | {
        mutation?: boolean
      }
  /**
   * Trigger it when scrolling.
   *
   */
  onScroll?: (e: Event) => void
  /**
   * Trigger it when scrolling ends.
   *
   */
  onStop?: (e: Event) => void
  /**
   * Listener options for scroll event.
   *
   * @default {capture: false, passive: true}
   */
  eventListenerOptions?: boolean | AddEventListenerOptions
  /**
   * Optionally specify a scroll behavior of `auto` (default, not smooth scrolling) or
   * `smooth` (for smooth scrolling) which takes effect when changing the `x` or `y` refs.
   *
   * @default 'auto'
   */
  behavior?: MaybeRefOrGetter<ScrollBehavior>
  /**
   * On error callback
   *
   * Default log error to `console.error`
   */
  onError?: (error: unknown) => void
}
export interface UseScrollReturn {
  x: WritableComputedRef<number>
  y: WritableComputedRef<number>
  isScrolling: ShallowRef<boolean>
  arrivedState: {
    left: boolean
    right: boolean
    top: boolean
    bottom: boolean
  }
  directions: {
    left: boolean
    right: boolean
    top: boolean
    bottom: boolean
  }
  measure: () => void
}
/**
 * Reactive scroll.
 *
 * @see https://vueuse.org/useScroll
 * @param element
 * @param options
 */
export declare function useScroll(
  element: MaybeRefOrGetter<
    HTMLElement | SVGElement | Window | Document | null | undefined
  >,
  options?: UseScrollOptions,
): UseScrollReturn
```
```

## File: `skills/vueuse-functions/references/useScrollLock.md`
```markdown
---
category: Sensors
---

# useScrollLock

Lock scrolling of the element.

## Usage

```vue
<script setup lang="ts">
import { useScrollLock } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const isLocked = useScrollLock(el)

isLocked.value = true // lock
isLocked.value = false // unlock
</script>

<template>
  <div ref="el" />
</template>
```

## Directive Usage

```vue
<script setup lang="ts">
import { vScrollLock } from '@vueuse/components'

const data = ref([1, 2, 3, 4, 5, 6])
const isLocked = ref(false)
const toggleLock = useToggle(isLocked)
</script>

<template>
  <div v-scroll-lock="isLocked">
    <div v-for="item in data" :key="item">
      {{ item }}
    </div>
  </div>
  <button @click="toggleLock()">
    Toggle lock state
  </button>
</template>
```

## Type Declarations

```ts
/**
 * Lock scrolling of the element.
 *
 * @see https://vueuse.org/useScrollLock
 * @param element
 */
export declare function useScrollLock(
  element: MaybeRefOrGetter<
    HTMLElement | SVGElement | Window | Document | null | undefined
  >,
  initialState?: boolean,
): WritableComputedRef<boolean, boolean>
```
```

## File: `skills/vueuse-functions/references/useSessionStorage.md`
```markdown
---
category: State
---

# useSessionStorage

Reactive [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage).

## Usage

Please refer to `useStorage`.

## Type Declarations

```ts
export declare function useSessionStorage(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<string>,
  options?: UseStorageOptions<string>,
): RemovableRef<string>
export declare function useSessionStorage(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<boolean>,
  options?: UseStorageOptions<boolean>,
): RemovableRef<boolean>
export declare function useSessionStorage(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<number>,
  options?: UseStorageOptions<number>,
): RemovableRef<number>
export declare function useSessionStorage<T>(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<T>,
  options?: UseStorageOptions<T>,
): RemovableRef<T>
export declare function useSessionStorage<T = unknown>(
  key: MaybeRefOrGetter<string>,
  initialValue: MaybeRefOrGetter<null>,
  options?: UseStorageOptions<T>,
): RemovableRef<T>
```
```

## File: `skills/vueuse-functions/references/useShare.md`
```markdown
---
category: Browser
---

# useShare

Reactive [Web Share API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share). The Browser provides features that can share content in text or file.

> The `share` method has to be called following a user gesture like a button click. It can’t simply be called on page load for example. That’s in place to help prevent abuse.

## Usage

```ts
import { useShare } from '@vueuse/core'

const { share, isSupported } = useShare()

function startShare() {
  share({
    title: 'Hello',
    text: 'Hello my friend!',
    url: location.href,
  })
}
```

### Passing a source ref

You can pass a `ref` to it, changes from the source ref will be reflected to your sharing options.

```ts {6}
import { ref } from 'vue'

const shareOptions = ref<ShareOptions>({ text: 'foo' })
const { share, isSupported } = useShare(shareOptions)

shareOptions.value.text = 'bar'

share()
```

## Type Declarations

```ts
export interface UseShareOptions {
  title?: string
  files?: File[]
  text?: string
  url?: string
}
export interface UseShareReturn extends Supportable {
  share: (overrideOptions?: MaybeRefOrGetter<UseShareOptions>) => Promise<void>
}
/**
 * Reactive Web Share API.
 *
 * @see https://vueuse.org/useShare
 * @param shareOptions
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useShare(
  shareOptions?: MaybeRefOrGetter<UseShareOptions>,
  options?: ConfigurableNavigator,
): UseShareReturn
```
```

## File: `skills/vueuse-functions/references/useSortable.md`
```markdown
---
category: '@Integrations'
---

# useSortable

Wrapper for [`sortable`](https://github.com/SortableJS/Sortable).

For more information on what options can be passed, see [`Sortable.options`](https://github.com/SortableJS/Sortable#options) in the `Sortable` documentation.

::: warning
Currently, `useSortable` only implements drag-and-drop sorting for a single list.
:::

## Install

```bash
npm i sortablejs@^1
```

## Usage

### Use template ref

```vue
<script setup lang="ts">
import { useSortable } from '@vueuse/integrations/useSortable'
import { shallowRef, useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const list = shallowRef([{ id: 1, name: 'a' }, { id: 2, name: 'b' }, { id: 3, name: 'c' }])

useSortable(el, list)
</script>

<template>
  <div ref="el">
    <div v-for="item in list" :key="item.id">
      {{ item.name }}
    </div>
  </div>
</template>
```

### Use specifies the selector to operate on

```vue
<script setup lang="ts">
import { useSortable } from '@vueuse/integrations/useSortable'
import { shallowRef, useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const list = shallowRef([{ id: 1, name: 'a' }, { id: 2, name: 'b' }, { id: 3, name: 'c' }])

const animation = 200

const { option } = useSortable(el, list, {
  handle: '.handle',
  // or option set
  // animation
})

// You can use the option method to set and get the option of Sortable
option('animation', animation)
// option('animation') // 200
</script>

<template>
  <div ref="el">
    <div v-for="item in list" :key="item.id">
      <span>{{ item.name }}</span>
      <span class="handle">*</span>
    </div>
  </div>
</template>
```

### Use a selector to get the root element

```vue
<script setup lang="ts">
import { useSortable } from '@vueuse/integrations/useSortable'
import { shallowRef } from 'vue'

const list = shallowRef([{ id: 1, name: 'a' }, { id: 2, name: 'b' }, { id: 3, name: 'c' }])

useSortable('#dv', list)
</script>

<template>
  <div id="dv">
    <div v-for="item in list" :key="item.id">
      <span>{{ item.name }}</span>
    </div>
  </div>
</template>
```

### Return Values

| Property | Description                                                      |
| -------- | ---------------------------------------------------------------- |
| `start`  | Initialize the Sortable instance (called automatically on mount) |
| `stop`   | Destroy the Sortable instance                                    |
| `option` | Get or set Sortable options at runtime                           |

```ts
const { start, stop, option } = useSortable(el, list)

// Stop sorting
stop()

// Start sorting again
start()

// Get/set options
option('animation', 200) // set
const animation = option('animation') // get
```

### Watch Element Changes

Use the `watchElement` option to automatically reinitialize Sortable when the element changes (useful with `v-if`).

```ts
import { useSortable } from '@vueuse/integrations/useSortable'

useSortable(el, list, {
  watchElement: true, // auto-reinitialize when element changes
})
```

### Custom Update Handler

If you want to handle the `onUpdate` yourself, you can pass in `onUpdate` parameters, and we also exposed a function to move the item position.

```ts
import { moveArrayElement, useSortable } from '@vueuse/integrations/useSortable'

useSortable(el, list, {
  onUpdate: (e) => {
    // do something
    moveArrayElement(list, e.oldIndex, e.newIndex, e)
    // nextTick required here as moveArrayElement is executed in a microtask
    // so we need to wait until the next tick until that is finished.
    nextTick(() => {
      /* do something */
    })
  }
})
```

### Helper Functions

The following helper functions are also exported:

| Function                                   | Description                                           |
| ------------------------------------------ | ----------------------------------------------------- |
| `moveArrayElement(list, from, to, event?)` | Move an element in an array from one index to another |
| `insertNodeAt(parent, element, index)`     | Insert a DOM node at a specific index                 |
| `removeNode(node)`                         | Remove a DOM node from its parent                     |

## Type Declarations

```ts
export interface UseSortableReturn {
  /**
   * start sortable instance
   */
  start: () => void
  /**
   * destroy sortable instance
   */
  stop: () => void
  /**
   * Options getter/setter
   * @param name a Sortable.Options property.
   * @param value a value.
   */
  option: (<K extends keyof Sortable.Options>(
    name: K,
    value: Sortable.Options[K],
  ) => void) &
    (<K extends keyof Sortable.Options>(name: K) => Sortable.Options[K])
}
export interface UseSortableOptions extends Options, ConfigurableDocument {
  /**
   * Watch the element reference for changes and automatically reinitialize Sortable
   * when the element changes.
   *
   * When `false` (default), Sortable is only initialized once on mount.
   * You must manually call `start()` if the element reference changes.
   *
   * When `true`, automatically watches the element reference and reinitializes
   * Sortable whenever it changes (e.g., conditional rendering with v-if).
   *
   * @default false
   */
  watchElement?: boolean
}
export declare function useSortable<T>(
  selector: string,
  list: MaybeRef<T[]>,
  options?: UseSortableOptions,
): UseSortableReturn
export declare function useSortable<T>(
  el: MaybeRefOrGetter<MaybeElement>,
  list: MaybeRef<T[]>,
  options?: UseSortableOptions,
): UseSortableReturn
/**
 * Inserts a element into the DOM at a given index.
 * @param parentElement
 * @param element
 * @param {number} index
 * @see https://github.com/Alfred-Skyblue/vue-draggable-plus/blob/a3829222095e1949bf2c9a20979d7b5930e66f14/src/utils/index.ts#L81C1-L94C2
 */
export declare function insertNodeAt(
  parentElement: Element,
  element: Element,
  index: number,
): void
/**
 * Removes a node from the DOM.
 * @param {Node} node
 * @see https://github.com/Alfred-Skyblue/vue-draggable-plus/blob/a3829222095e1949bf2c9a20979d7b5930e66f14/src/utils/index.ts#L96C1-L102C2
 */
export declare function removeNode(node: Node): void
export declare function moveArrayElement<T>(
  list: MaybeRef<T[]>,
  from: number,
  to: number,
  e?: Sortable.SortableEvent | null,
): void
```
```

## File: `skills/vueuse-functions/references/useSorted.md`
```markdown
---
category: Array
---

# useSorted

reactive sort array

## Usage

```ts
import { useSorted } from '@vueuse/core'

// general sort
const source = [10, 3, 5, 7, 2, 1, 8, 6, 9, 4]
const sorted = useSorted(source)
console.log(sorted.value) // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(source) // [10, 3, 5, 7, 2, 1, 8, 6, 9, 4]

// object sort
const objArr = [{
  name: 'John',
  age: 40,
}, {
  name: 'Jane',
  age: 20,
}, {
  name: 'Joe',
  age: 30,
}, {
  name: 'Jenny',
  age: 22,
}]
const objSorted = useSorted(objArr, (a, b) => a.age - b.age)
```

### dirty mode

dirty mode will change the source array.

```ts
const source = ref([10, 3, 5, 7, 2, 1, 8, 6, 9, 4])
const sorted = useSorted(source, (a, b) => a - b, {
  dirty: true,
})
console.log(source)// output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

## Type Declarations

```ts
export type UseSortedCompareFn<T = any> = (a: T, b: T) => number
export type UseSortedFn<T = any> = (
  arr: T[],
  compareFn: UseSortedCompareFn<T>,
) => T[]
export interface UseSortedOptions<T = any> {
  /**
   * sort algorithm
   */
  sortFn?: UseSortedFn<T>
  /**
   * compare function
   */
  compareFn?: UseSortedCompareFn<T>
  /**
   * change the value of the source array
   * @default false
   */
  dirty?: boolean
}
/**
 * reactive sort array
 *
 * @see https://vueuse.org/useSorted
 */
export declare function useSorted<T = any>(
  source: MaybeRefOrGetter<T[]>,
  compareFn?: UseSortedCompareFn<T>,
): Ref<T[]>
export declare function useSorted<T = any>(
  source: MaybeRefOrGetter<T[]>,
  options?: UseSortedOptions<T>,
): Ref<T[]>
export declare function useSorted<T = any>(
  source: MaybeRefOrGetter<T[]>,
  compareFn?: UseSortedCompareFn<T>,
  options?: Omit<UseSortedOptions<T>, "compareFn">,
): Ref<T[]>
```
```

## File: `skills/vueuse-functions/references/useSpeechRecognition.md`
```markdown
---
category: Sensors
---

# useSpeechRecognition

Reactive [SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition).

> [Can I use?](https://caniuse.com/mdn-api_speechrecognitionevent)

## Usage

```ts
import { useSpeechRecognition } from '@vueuse/core'

const {
  isSupported,
  isListening,
  isFinal,
  result,
  start,
  stop,
} = useSpeechRecognition()
```

### Options

The following shows the default values of the options, they will be directly passed to [SpeechRecognition API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition).

```ts
import { useSpeechRecognition } from '@vueuse/core'
// ---cut---
useSpeechRecognition({
  lang: 'en-US',
  interimResults: true,
  continuous: true,
})
```

## Type Declarations

```ts
export interface UseSpeechRecognitionOptions extends ConfigurableWindow {
  /**
   * Controls whether continuous results are returned for each recognition, or only a single result.
   *
   * @default true
   */
  continuous?: boolean
  /**
   * Controls whether interim results should be returned (true) or not (false.) Interim results are results that are not yet final
   *
   * @default true
   */
  interimResults?: boolean
  /**
   * Language for SpeechRecognition
   *
   * @default 'en-US'
   */
  lang?: MaybeRefOrGetter<string>
  /**
   * A number representing the maximum returned alternatives for each result.
   *
   * @see https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition/maxAlternatives
   * @default 1
   */
  maxAlternatives?: number
}
export interface UseSpeechRecognitionReturn extends Supportable {
  isListening: ShallowRef<boolean>
  isFinal: ShallowRef<boolean>
  recognition: SpeechRecognition | undefined
  result: ShallowRef<string>
  error: ShallowRef<SpeechRecognitionErrorEvent | Error | undefined>
  toggle: (value?: boolean) => void
  start: () => void
  stop: () => void
}
/**
 * Reactive SpeechRecognition.
 *
 * @see https://vueuse.org/useSpeechRecognition
 * @see https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition SpeechRecognition
 * @param options
 */
export declare function useSpeechRecognition(
  options?: UseSpeechRecognitionOptions,
): UseSpeechRecognitionReturn
```
```

## File: `skills/vueuse-functions/references/useSpeechSynthesis.md`
```markdown
---
category: Sensors
---

# useSpeechSynthesis

Reactive [SpeechSynthesis](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis).

> [Can I use?](https://caniuse.com/mdn-api_speechsynthesis)

## Usage

```ts
import { useSpeechSynthesis } from '@vueuse/core'

const {
  isSupported,
  isPlaying,
  status,
  voiceInfo,
  utterance,
  error,
  stop,
  toggle,
  speak,
} = useSpeechSynthesis()
```

### Options

The following shows the default values of the options, they will be directly passed to [SpeechSynthesis API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis).

```ts
import { useSpeechSynthesis } from '@vueuse/core'
// ---cut---
useSpeechSynthesis({
  lang: 'en-US',
  pitch: 1,
  rate: 1,
  volume: 1,
})
```

## Type Declarations

```ts
export type UseSpeechSynthesisStatus = "init" | "play" | "pause" | "end"
export interface UseSpeechSynthesisOptions extends ConfigurableWindow {
  /**
   * Language for SpeechSynthesis
   *
   * @default 'en-US'
   */
  lang?: MaybeRefOrGetter<string>
  /**
   * Gets and sets the pitch at which the utterance will be spoken at.
   *
   * @default 1
   */
  pitch?: MaybeRefOrGetter<SpeechSynthesisUtterance["pitch"]>
  /**
   * Gets and sets the speed at which the utterance will be spoken at.
   *
   * @default 1
   */
  rate?: MaybeRefOrGetter<SpeechSynthesisUtterance["rate"]>
  /**
   * Gets and sets the voice that will be used to speak the utterance.
   */
  voice?: MaybeRef<SpeechSynthesisVoice>
  /**
   * Gets and sets the volume that the utterance will be spoken at.
   *
   * @default 1
   */
  volume?: MaybeRefOrGetter<SpeechSynthesisUtterance["volume"]>
  /**
   * Callback function that is called when the boundary event is triggered.
   */
  onBoundary?: (event: SpeechSynthesisEvent) => void
}
export interface UseSpeechSynthesisReturn extends Supportable {
  isPlaying: ShallowRef<boolean>
  status: ShallowRef<UseSpeechSynthesisStatus>
  utterance: ComputedRef<SpeechSynthesisUtterance>
  error: ShallowRef<SpeechSynthesisErrorEvent | undefined>
  stop: () => void
  toggle: (value?: boolean) => void
  speak: () => void
}
/**
 * Reactive SpeechSynthesis.
 *
 * @see https://vueuse.org/useSpeechSynthesis
 * @see https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis SpeechSynthesis
 */
export declare function useSpeechSynthesis(
  text: MaybeRefOrGetter<string>,
  options?: UseSpeechSynthesisOptions,
): UseSpeechSynthesisReturn
```
```

## File: `skills/vueuse-functions/references/useStepper.md`
```markdown
---
category: Utilities
---

# useStepper

Provides helpers for building a multi-step wizard interface.

## Usage

### Steps as array

```ts
import { useStepper } from '@vueuse/core'

const {
  steps,
  stepNames,
  index,
  current,
  next,
  previous,
  isFirst,
  isLast,
  goTo,
  goToNext,
  goToPrevious,
  goBackTo,
  isNext,
  isPrevious,
  isCurrent,
  isBefore,
  isAfter,
} = useStepper([
  'billing-address',
  'terms',
  'payment',
])

// Access the step through `current`
console.log(current.value) // 'billing-address'
```

### Steps as object

```ts
import { useStepper } from '@vueuse/core'

const {
  steps,
  stepNames,
  index,
  current,
  next,
  previous,
  isFirst,
  isLast,
  goTo,
  goToNext,
  goToPrevious,
  goBackTo,
  isNext,
  isPrevious,
  isCurrent,
  isBefore,
  isAfter,
} = useStepper({
  'user-information': {
    title: 'User information',
  },
  'billing-address': {
    title: 'Billing address',
  },
  'terms': {
    title: 'Terms',
  },
  'payment': {
    title: 'Payment',
  },
})

// Access the step object through `current`
console.log(current.value.title) // 'User information'
```

## Type Declarations

```ts
export interface UseStepperReturn<StepName, Steps, Step> {
  /** List of steps. */
  steps: Readonly<Ref<Steps>>
  /** List of step names. */
  stepNames: Readonly<Ref<StepName[]>>
  /** Index of the current step. */
  index: Ref<number>
  /** Current step. */
  current: ComputedRef<Step>
  /** Next step, or undefined if the current step is the last one. */
  next: ComputedRef<StepName | undefined>
  /** Previous step, or undefined if the current step is the first one. */
  previous: ComputedRef<StepName | undefined>
  /** Whether the current step is the first one. */
  isFirst: ComputedRef<boolean>
  /** Whether the current step is the last one. */
  isLast: ComputedRef<boolean>
  /** Get the step at the specified index. */
  at: (index: number) => Step | undefined
  /** Get a step by the specified name. */
  get: (step: StepName) => Step | undefined
  /** Go to the specified step. */
  goTo: (step: StepName) => void
  /** Go to the next step. Does nothing if the current step is the last one. */
  goToNext: () => void
  /** Go to the previous step. Does nothing if the current step is the previous one. */
  goToPrevious: () => void
  /** Go back to the given step, only if the current step is after. */
  goBackTo: (step: StepName) => void
  /** Checks whether the given step is the next step. */
  isNext: (step: StepName) => boolean
  /** Checks whether the given step is the previous step. */
  isPrevious: (step: StepName) => boolean
  /** Checks whether the given step is the current step. */
  isCurrent: (step: StepName) => boolean
  /** Checks if the current step is before the given step. */
  isBefore: (step: StepName) => boolean
  /** Checks if the current step is after the given step. */
  isAfter: (step: StepName) => boolean
}
export declare function useStepper<T extends string | number>(
  steps: MaybeRef<T[]>,
  initialStep?: T,
): UseStepperReturn<T, T[], T>
export declare function useStepper<T extends Record<string, any>>(
  steps: MaybeRef<T>,
  initialStep?: keyof T,
): UseStepperReturn<Exclude<keyof T, symbol>, T, T[keyof T]>
```
```

## File: `skills/vueuse-functions/references/useStorage.md`
```markdown
---
category: State
related: useLocalStorage, useSessionStorage, useStorageAsync
---

# useStorage

Create a reactive ref that can be used to access & modify [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) or [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage).

Uses localStorage by default, other storage sources be specified via third argument.

## Usage

::: tip
When using with Nuxt 3, this function will **NOT** be auto imported in favor of Nitro's built-in [`useStorage()`](https://nitro.unjs.io/guide/storage). Use explicit import if you want to use the function from VueUse.
:::

```ts
import { useStorage } from '@vueuse/core'

// bind object
const state = useStorage('my-store', { hello: 'hi', greeting: 'Hello' })

// bind boolean
const flag = useStorage('my-flag', true) // returns Ref<boolean>

// bind number
const count = useStorage('my-count', 0) // returns Ref<number>

// bind string with SessionStorage
const id = useStorage('my-id', 'some-string-id', sessionStorage) // returns Ref<string>

// delete data from storage
state.value = null
```

## Merge Defaults

By default, `useStorage` will use the value from storage if it is present and ignores the default value. Be aware that when you are adding more properties to the default value, the key might be `undefined` if client's storage does not have that key.

```ts
import { useStorage } from '@vueuse/core'
// ---cut---
localStorage.setItem('my-store', '{"hello": "hello"}')

const state = useStorage('my-store', { hello: 'hi', greeting: 'hello' }, localStorage)

console.log(state.value.greeting) // undefined, since the value is not presented in storage
```

To solve that, you can enable `mergeDefaults` option.

```ts
import { useStorage } from '@vueuse/core'
// ---cut---
localStorage.setItem('my-store', '{"hello": "nihao"}')

const state = useStorage(
  'my-store',
  { hello: 'hi', greeting: 'hello' },
  localStorage,
  { mergeDefaults: true } // <--
)

console.log(state.value.hello) // 'nihao', from storage
console.log(state.value.greeting) // 'hello', from merged default value
```

When setting it to true, it will perform a **shallow merge** for objects. You can pass a function to perform custom merge (e.g. deep merge), for example:

```ts
import { useStorage } from '@vueuse/core'
// ---cut---
const state = useStorage(
  'my-store',
  { hello: 'hi', greeting: 'hello' },
  localStorage,
  { mergeDefaults: (storageValue, defaults) => deepMerge(defaults, storageValue) } // <--
)
```

## Custom Serialization

By default, `useStorage` will smartly use the corresponding serializer based on the data type of provided default value. For example, `JSON.stringify` / `JSON.parse` will be used for objects, `Number.toString` / `parseFloat` for numbers, etc.

You can also provide your own serialization function to `useStorage`:

```ts
import { useStorage } from '@vueuse/core'

useStorage(
  'key',
  {},
  undefined,
  {
    serializer: {
      read: (v: any) => v ? JSON.parse(v) : null,
      write: (v: any) => JSON.stringify(v),
    },
  },
)
```

Please note when you provide `null` as the default value, `useStorage` can't assume the data type from it. In this case, you can provide a custom serializer or reuse the built-in ones explicitly.

```ts
import { StorageSerializers, useStorage } from '@vueuse/core'

const objectLike = useStorage('key', null, undefined, { serializer: StorageSerializers.object })
objectLike.value = { foo: 'bar' }
```

### Built-in Serializers

The following serializers are available via `StorageSerializers`:

| Type      | Description                           |
| --------- | ------------------------------------- |
| `string`  | Plain string                          |
| `number`  | Number (via `parseFloat`)             |
| `boolean` | Boolean                               |
| `object`  | JSON object/array                     |
| `map`     | JavaScript `Map`                      |
| `set`     | JavaScript `Set`                      |
| `date`    | JavaScript `Date` (via `toISOString`) |
| `any`     | Raw string passthrough                |

```ts
import { StorageSerializers, useStorage } from '@vueuse/core'

const myMap = useStorage('my-map', new Map(), undefined, {
  serializer: StorageSerializers.map,
})
```

## Options

```ts
useStorage('key', defaults, storage, {
  // Watch for deep changes in objects/arrays (default: true)
  deep: true,
  // Sync across tabs via storage events (default: true)
  listenToStorageChanges: true,
  // Write default value to storage if not present (default: true)
  writeDefaults: true,
  // Use shallowRef instead of ref (default: false)
  shallow: false,
  // Initialize only after component is mounted (default: false)
  initOnMounted: false,
  // Custom error handler (default: console.error)
  onError: e => console.error(e),
  // Watch flush timing (default: 'pre')
  flush: 'pre',
})
```

## Reactive Key

The storage key can be a ref or getter, and the data will be updated when the key changes:

```ts
import { useStorage } from '@vueuse/core'

const userId = ref('user-1')
const userData = useStorage(
  () => `user-data-${userId.value}`,
  { name: '' },
)

// Changing the key will read from the new storage location
userId.value = 'user-2'
```

## Type Declarations

```ts
export interface Serializer<T> {
  read: (raw: string) => T
  write: (value: T) => string
}
export interface SerializerAsync<T> {
  read: (raw: string) => Awaitable<T>
  write: (value: T) => Awaitable<string>
}
export declare const StorageSerializers: Record<
  "boolean" | "object" | "number" | "any" | "string" | "map" | "set" | "date",
  Serializer<any>
>
export declare const customStorageEventName = "vueuse-storage"
export interface StorageEventLike {
  storageArea: StorageLike | null
  key: StorageEvent["key"]
  oldValue: StorageEvent["oldValue"]
  newValue: StorageEvent["newValue"]
}
export interface UseStorageOptions<T>
  extends ConfigurableEventFilter, ConfigurableWindow, ConfigurableFlush {
  /**
   * Watch for deep changes
   *
   * @default true
   */
  deep?: boolean
  /**
   * Listen to storage changes, useful for multiple tabs application
   *
   * @default true
   */
  listenToStorageChanges?: boolean
  /**
   * Write the default value to the storage when it does not exist
   *
   * @default true
   */
  writeDefaults?: boolean
  /**
   * Merge the default value with the value read from the storage.
   *
   * When setting it to true, it will perform a **shallow merge** for objects.
   * You can pass a function to perform custom merge (e.g. deep merge), for example:
   *
   * @default false
   */
  mergeDefaults?: boolean | ((storageValue: T, defaults: T) => T)
  /**
   * Custom data serialization
   */
  serializer?: Serializer<T>
  /**
   * On error callback
   *
   * Default log error to `console.error`
   */
  onError?: (error: unknown) => void
  /**
   * Use shallow ref as reference
   *
   * @default false
   */
  shallow?: boolean
  /**
   * Wait for the component to be mounted before reading the storage.
   *
   * @default false
   */
  initOnMounted?: boolean
}
export declare function useStorage(
  key: MaybeRefOrGetter<string>,
  defaults: MaybeRefOrGetter<string>,
  storage?: StorageLike,
  options?: UseStorageOptions<string>,
): RemovableRef<string>
export declare function useStorage(
  key: MaybeRefOrGetter<string>,
  defaults: MaybeRefOrGetter<boolean>,
  storage?: StorageLike,
  options?: UseStorageOptions<boolean>,
): RemovableRef<boolean>
export declare function useStorage(
  key: MaybeRefOrGetter<string>,
  defaults: MaybeRefOrGetter<number>,
  storage?: StorageLike,
  options?: UseStorageOptions<number>,
): RemovableRef<number>
export declare function useStorage<T>(
  key: MaybeRefOrGetter<string>,
  defaults: MaybeRefOrGetter<T>,
  storage?: StorageLike,
  options?: UseStorageOptions<T>,
): RemovableRef<T>
export declare function useStorage<T = unknown>(
  key: MaybeRefOrGetter<string>,
  defaults: MaybeRefOrGetter<null>,
  storage?: StorageLike,
  options?: UseStorageOptions<T>,
): RemovableRef<T>
```
```

## File: `skills/vueuse-functions/references/useStorageAsync.md`
```markdown
---
category: State
---

# useStorageAsync

Reactive Storage in with async support.

## Usage

The basic usage please refer to `useStorage`.

## Wait First Loaded

When user entering your app, `useStorageAsync()` will start loading value from an async storage,
sometimes you may get the default initial value, not the real value stored in storage at the very
beginning.

```ts
import { useStorageAsync } from '@vueuse/core'

const accessToken = useStorageAsync('access.token', '', SomeAsyncStorage)

// accessToken.value may be empty before the async storage is ready
console.log(accessToken.value) // ""

setTimeout(() => {
  // After some time, the async storage is ready
  console.log(accessToken.value) // "the real value stored in storage"
}, 500)
```

In this case, you can wait the storage prepared, the returned value is also a `Promise`,
so you can wait it resolved in your template or script.

```ts
// Use top-level await if your environment supports it
const accessToken = await useStorageAsync('access.token', '', SomeAsyncStorage)

console.log(accessToken.value) // "the real value stored in storage"
```

If you must wait multiple storages, put them into a `Promise.allSettled()`

```ts
router.onReady(async () => {
  await Promise.allSettled([
    accessToken,
    refreshToken,
    userData,
  ])

  app.mount('app')
})
```

There is a callback named `onReady` in options:

```ts
import { useStorageAsync } from '@vueuse/core'

// Use ES2024 Promise.withResolvers, you may use any Deferred object or EventBus to do same thing.
const { promise, resolve } = Promise.withResolvers()

const accessToken = useStorageAsync('access.token', '', SomeAsyncStorage, {
  onReady(value) {
    resolve(value)
  }
})

// At main.ts
router.onReady(async () => {
  // Let's wait accessToken loaded
  await promise

  // Now accessToken has loaded, we can safely mount our app

  app.mount('app')
})
```

Simply use `resolve` as callback:

```ts
const accessToken = useStorageAsync('access.token', '', SomeAsyncStorage, {
  onReady: resolve
})
```

## Type Declarations

```ts
export interface UseStorageAsyncOptions<T> extends Omit<
  UseStorageOptions<T>,
  "serializer"
> {
  /**
   * Custom data serialization
   */
  serializer?: SerializerAsync<T>
  /**
   * On first value loaded hook.
   */
  onReady?: (value: T) => void
}
export declare function useStorageAsync(
  key: string,
  initialValue: MaybeRefOrGetter<string>,
  storage?: StorageLikeAsync,
  options?: UseStorageAsyncOptions<string>,
): RemovableRef<string> & Promise<RemovableRef<string>>
export declare function useStorageAsync(
  key: string,
  initialValue: MaybeRefOrGetter<boolean>,
  storage?: StorageLikeAsync,
  options?: UseStorageAsyncOptions<boolean>,
): RemovableRef<boolean> & Promise<RemovableRef<boolean>>
export declare function useStorageAsync(
  key: string,
  initialValue: MaybeRefOrGetter<number>,
  storage?: StorageLikeAsync,
  options?: UseStorageAsyncOptions<number>,
): RemovableRef<number> & Promise<RemovableRef<number>>
export declare function useStorageAsync<T>(
  key: string,
  initialValue: MaybeRefOrGetter<T>,
  storage?: StorageLikeAsync,
  options?: UseStorageAsyncOptions<T>,
): RemovableRef<T> & Promise<RemovableRef<T>>
export declare function useStorageAsync<T = unknown>(
  key: string,
  initialValue: MaybeRefOrGetter<null>,
  storage?: StorageLikeAsync,
  options?: UseStorageAsyncOptions<T>,
): RemovableRef<T> & Promise<RemovableRef<T>>
```
```

## File: `skills/vueuse-functions/references/useStyleTag.md`
```markdown
---
category: Browser
---

# useStyleTag

Inject reactive `style` element in head.

## Usage

### Basic usage

Provide a CSS string, then `useStyleTag` will automatically generate an id and inject it in `<head>`.

```ts
import { useStyleTag } from '@vueuse/core'

const {
  id,
  css,
  load,
  unload,
  isLoaded,
} = useStyleTag('.foo { margin-top: 32px; }')

// Later you can modify styles
css.value = '.foo { margin-top: 64px; }'
```

This code will be injected to `<head>`:

```html
<style id="vueuse_styletag_1">
  .foo {
    margin-top: 64px;
  }
</style>
```

### Custom ID

If you need to define your own id, you can pass `id` as first argument.

```ts
import { useStyleTag } from '@vueuse/core'
// ---cut---
useStyleTag('.foo { margin-top: 32px; }', { id: 'custom-id' })
```

```html
<!-- injected to <head> -->
<style id="custom-id">
  .foo {
    margin-top: 32px;
  }
</style>
```

### Media query

You can pass media attributes as last argument within object.

```ts
import { useStyleTag } from '@vueuse/core'
// ---cut---
useStyleTag('.foo { margin-top: 32px; }', { media: 'print' })
```

```html
<!-- injected to <head> -->
<style id="vueuse_styletag_1" media="print">
  .foo {
    margin-top: 32px;
  }
</style>
```

## Type Declarations

```ts
export interface UseStyleTagOptions extends ConfigurableDocument {
  /**
   * Media query for styles to apply
   */
  media?: string
  /**
   * Load the style immediately
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Manual controls the timing of loading and unloading
   *
   * @default false
   */
  manual?: boolean
  /**
   * DOM id of the style tag
   *
   * @default auto-incremented
   */
  id?: string
  /**
   * Nonce value for CSP (Content Security Policy)
   *
   * @default undefined
   */
  nonce?: string
}
export interface UseStyleTagReturn {
  id: string
  css: ShallowRef<string>
  load: () => void
  unload: () => void
  isLoaded: Readonly<ShallowRef<boolean>>
}
/**
 * Inject <style> element in head.
 *
 * Overload: Omitted id
 *
 * @see https://vueuse.org/useStyleTag
 * @param css
 * @param options
 */
export declare function useStyleTag(
  css: MaybeRef<string>,
  options?: UseStyleTagOptions,
): UseStyleTagReturn
```
```

## File: `skills/vueuse-functions/references/useSubject.md`
```markdown
---
category: '@RxJS'
---

# useSubject

Bind an RxJS [`Subject`](https://rxjs.dev/guide/subject) to a `ref` and propagate value changes both ways.

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { useSubject } from '@vueuse/rxjs'
import { Subject } from 'rxjs'

const subject = new Subject()

// setup()
const subjectRef = useSubject(subject)

// Changes to subjectRef.value will be pushed to the subject
subjectRef.value = 'new value'

// Values emitted by the subject will update subjectRef
subject.next('from subject')
```

### With BehaviorSubject

When using a `BehaviorSubject`, the returned ref is initialized with the subject's current value and the type does not include `undefined`:

```ts no-twoslash
import { useSubject } from '@vueuse/rxjs'
import { BehaviorSubject } from 'rxjs'

const subject = new BehaviorSubject('initial')

// setup()
const subjectRef = useSubject(subject) // Ref<string>, not Ref<string | undefined>
console.log(subjectRef.value) // 'initial'
```

### Error Handling

If you want to add custom error handling to a Subject that might error, you can supply an optional `onError` configuration. Without this, RxJS will treat any error in the supplied observable as an "unhandled error" and it will be thrown in a new call stack and reported to `window.onerror` (or `process.on('error')` if you happen to be in node).

```ts no-twoslash
import { useSubject } from '@vueuse/rxjs'
import { Subject } from 'rxjs'

const subject = new Subject()

// setup()
const subjectRef = useSubject(subject, {
  onError: (err) => {
    console.log(err.message) // "oops"
  },
},)
```

## Type Declarations

```ts
export interface UseSubjectOptions<I = undefined> extends Omit<
  UseObservableOptions<I>,
  "initialValue"
> {}
export declare function useSubject<H>(
  subject: BehaviorSubject<H>,
  options?: UseSubjectOptions,
): Ref<H>
export declare function useSubject<H>(
  subject: Subject<H>,
  options?: UseSubjectOptions,
): Ref<H | undefined>
```
```

## File: `skills/vueuse-functions/references/useSubscription.md`
```markdown
---
category: '@RxJS'
---

# useSubscription

Use an RxJS [`Subscription`](https://rxjs.dev/guide/subscription) without worrying about unsubscribing from it or creating memory leaks.

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { useSubscription } from '@vueuse/rxjs'
import { interval } from 'rxjs'

const count = ref(0)

// useSubscription call unsubscribe method before unmount the component
useSubscription(
  interval(1000)
    .subscribe(() => {
      count.value++
      console.log(count)
    }),
)
```

## Type Declarations

```ts
export declare function useSubscription(subscription: Unsubscribable): void
```
```

## File: `skills/vueuse-functions/references/useSum.md`
```markdown
---
category: '@Math'
---

# useSum

Get the sum of an array reactively

## Usage

```ts
import { useSum } from '@vueuse/math'

const array = ref([1, 2, 3, 4])
const sum = useSum(array) // Ref<10>
```

```ts
import { useSum } from '@vueuse/math'

const a = ref(1)
const b = ref(3)

const sum = useSum(a, b, 2) // Ref<6>
```

## Type Declarations

```ts
export declare function useSum(
  array: MaybeRefOrGetter<MaybeRefOrGetter<number>[]>,
): ComputedRef<number>
export declare function useSum(
  ...args: MaybeRefOrGetter<number>[]
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useSupported.md`
```markdown
---
category: Utilities
---

# useSupported

SSR compatibility `isSupported`

## Usage

```ts
import { useSupported } from '@vueuse/core'

const isSupported = useSupported(() => navigator && 'getBattery' in navigator)

if (isSupported.value) {
  // do something
  navigator.getBattery
}
```

## Type Declarations

```ts
export type UseSupportedReturn = ComputedRef<boolean>
export declare function useSupported(
  callback: () => unknown,
): UseSupportedReturn
```
```

## File: `skills/vueuse-functions/references/useSwipe.md`
```markdown
---
category: Sensors
---

# useSwipe

Reactive swipe detection based on [`TouchEvents`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent).

## Usage

```vue
<script setup lang="ts">
import { useSwipe } from '@vueuse/core'
import { useTemplateRef } from 'vue'

const el = useTemplateRef('el')
const { isSwiping, direction } = useSwipe(el)
</script>

<template>
  <div ref="el">
    Swipe here
  </div>
</template>
```

## Type Declarations

```ts
export type UseSwipeDirection = "up" | "down" | "left" | "right" | "none"
export interface UseSwipeOptions extends ConfigurableWindow {
  /**
   * Register events as passive
   *
   * @default true
   */
  passive?: boolean
  /**
   * @default 50
   */
  threshold?: number
  /**
   * Callback on swipe start
   */
  onSwipeStart?: (e: TouchEvent) => void
  /**
   * Callback on swipe moves
   */
  onSwipe?: (e: TouchEvent) => void
  /**
   * Callback on swipe ends
   */
  onSwipeEnd?: (e: TouchEvent, direction: UseSwipeDirection) => void
}
export interface UseSwipeReturn {
  isSwiping: ShallowRef<boolean>
  direction: ComputedRef<UseSwipeDirection>
  coordsStart: Readonly<Position>
  coordsEnd: Readonly<Position>
  lengthX: ComputedRef<number>
  lengthY: ComputedRef<number>
  stop: () => void
}
/**
 * Reactive swipe detection.
 *
 * @see https://vueuse.org/useSwipe
 * @param target
 * @param options
 */
export declare function useSwipe(
  target: MaybeRefOrGetter<EventTarget | null | undefined>,
  options?: UseSwipeOptions,
): UseSwipeReturn
```
```

## File: `skills/vueuse-functions/references/useTemplateRefsList.md`
```markdown
---
category: Component
---

# useTemplateRefsList

Shorthand for binding refs to template elements and components inside `v-for`.

## Usage

```vue
<script setup lang="ts">
import { useTemplateRefsList } from '@vueuse/core'
import { onUpdated } from 'vue'

const refs = useTemplateRefsList<HTMLDivElement>()

onUpdated(() => {
  console.log(refs)
})
</script>

<template>
  <div v-for="i of 5" :key="i" :ref="refs.set" />
</template>
```

## Type Declarations

```ts
export type TemplateRefsList<T> = T[] & {
  set: (el: object | null) => void
}
export declare function useTemplateRefsList<T = Element>(): Readonly<
  Ref<Readonly<TemplateRefsList<T>>>
>
```
```

## File: `skills/vueuse-functions/references/useTextDirection.md`
```markdown
---
category: Browser
---

# useTextDirection

Reactive [dir](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir) of the element's text.

## Usage

```ts
import { useTextDirection } from '@vueuse/core'

const dir = useTextDirection() // Ref<'ltr' | 'rtl' | 'auto'>
```

By default, it returns `rtl` direction when dir `rtl` is applied to the `html` tag, for example:

```html
<!--ltr-->
<html>
  ...
</html>

<!--rtl-->
<html dir="rtl">
  ...
</html>
```

## Options

```ts
import { useTextDirection } from '@vueuse/core'

const mode = useTextDirection({
  selector: 'body'
}) // Ref<'ltr' | 'rtl' | 'auto'>
```

## Type Declarations

```ts
export type UseTextDirectionValue = "ltr" | "rtl" | "auto"
export interface UseTextDirectionOptions extends ConfigurableDocument {
  /**
   * CSS Selector for the target element applying to
   *
   * @default 'html'
   */
  selector?: string
  /**
   * Observe `document.querySelector(selector)` changes using MutationObserve
   *
   * @default false
   */
  observe?: boolean
  /**
   * Initial value
   *
   * @default 'ltr'
   */
  initialValue?: UseTextDirectionValue
}
/**
 * Reactive dir of the element's text.
 *
 * @see https://vueuse.org/useTextDirection
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useTextDirection(
  options?: UseTextDirectionOptions,
): WritableComputedRef<UseTextDirectionValue, UseTextDirectionValue>
```
```

## File: `skills/vueuse-functions/references/useTextSelection.md`
```markdown
---
category: Sensors
---

# useTextSelection

Reactively track user text selection based on [`Window.getSelection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getSelection).

## Usage

```vue
<script setup lang="ts">
import { useTextSelection } from '@vueuse/core'

const state = useTextSelection()
</script>

<template>
  <p>{{ state.text }}</p>
</template>
```

## Type Declarations

```ts
export interface UseTextSelectionOptions extends ConfigurableWindow {}
export interface UseTextSelectionReturn {
  text: ComputedRef<string>
  rects: ComputedRef<DOMRect[]>
  ranges: ComputedRef<Range[]>
  selection: ShallowRef<Selection | null>
}
/**
 * Reactively track user text selection based on [`Window.getSelection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getSelection).
 *
 * @see https://vueuse.org/useTextSelection
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useTextSelection(
  options?: UseTextSelectionOptions,
): UseTextSelectionReturn
```
```

## File: `skills/vueuse-functions/references/useTextareaAutosize.md`
```markdown
---
category: Browser
---

# useTextareaAutosize

Automatically update the height of a textarea depending on the content.

## Usage

### Simple example

```vue
<script setup lang="ts">
import { useTextareaAutosize } from '@vueuse/core'

const { textarea, input } = useTextareaAutosize()
</script>

<template>
  <textarea
    ref="textarea"
    v-model="input"
    class="resize-none"
    placeholder="What's on your mind?"
  />
</template>
```

::: info

It's recommended to reset the scrollbar styles for the textarea element to avoid incorrect height values for large amounts of text.

```css
textarea {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

textarea::-webkit-scrollbar {
  display: none;
}
```

:::

### With `rows` attribute

If you need support for the rows attribute on a textarea element, then you should set the `styleProp` option to `minHeight`.

```vue
<script setup lang="ts">
import { useTextareaAutosize } from '@vueuse/core'

const { textarea, input } = useTextareaAutosize({ styleProp: 'minHeight' })
</script>

<template>
  <textarea
    ref="textarea"
    v-model="input"
    class="resize-none"
    placeholder="What's on your mind?"
    rows="3"
  />
</template>
```

## Type Declarations

```ts
export interface UseTextareaAutosizeOptions extends ConfigurableWindow {
  /** Textarea element to autosize. */
  element?: MaybeRef<HTMLTextAreaElement | undefined | null>
  /** Textarea content. */
  input?: MaybeRef<string>
  /** Watch sources that should trigger a textarea resize. */
  watch?: WatchSource | MultiWatchSources
  /** Function called when the textarea size changes. */
  onResize?: () => void
  /** Specify style target to apply the height based on textarea content. If not provided it will use textarea it self.  */
  styleTarget?: MaybeRef<HTMLElement | undefined>
  /** Specify the style property that will be used to manipulate height. Can be `height | minHeight`. Default value is `height`. */
  styleProp?: "height" | "minHeight"
}
export interface UseTextareaAutosizeReturn {
  textarea: Ref<HTMLTextAreaElement | undefined | null>
  input: Ref<string>
  triggerResize: () => void
}
export declare function useTextareaAutosize(
  options?: UseTextareaAutosizeOptions,
): UseTextareaAutosizeReturn
```
```

## File: `skills/vueuse-functions/references/useThrottleFn.md`
```markdown
---
category: Utilities
related: refThrottled, refDebounced, useDebounceFn
---

# useThrottleFn

Throttle execution of a function. Especially useful for rate limiting execution of handlers on events like resize and scroll.

> Throttle is a spring that throws balls: after a ball flies out it needs some time to shrink back, so it cannot throw any more balls unless it's ready.

## Usage

```ts
import { useThrottleFn } from '@vueuse/core'

const throttledFn = useThrottleFn(() => {
  // do something, it will be called at most 1 time per second
}, 1000)

useEventListener(window, 'resize', throttledFn)
```

## Recommended Reading

- [**Debounce vs Throttle**: Definitive Visual Guide](https://kettanaito.com/blog/debounce-vs-throttle)

## Type Declarations

```ts
/**
 * Throttle execution of a function. Especially useful for rate limiting
 * execution of handlers on events like resize and scroll.
 *
 * @param   fn             A function to be executed after delay milliseconds. The `this` context and all arguments are passed through, as-is,
 *                                    to `callback` when the throttled-function is executed.
 * @param   ms             A zero-or-greater delay in milliseconds. For event callbacks, values around 100 or 250 (or even higher) are most useful.
 *                                    (default value: 200)
 *
 * @param [trailing] if true, call fn again after the time is up (default value: false)
 *
 * @param [leading] if true, call fn on the leading edge of the ms timeout (default value: true)
 *
 * @param [rejectOnCancel] if true, reject the last call if it's been cancel (default value: false)
 *
 * @return  A new, throttled, function.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useThrottleFn<T extends FunctionArgs>(
  fn: T,
  ms?: MaybeRefOrGetter<number>,
  trailing?: boolean,
  leading?: boolean,
  rejectOnCancel?: boolean,
): PromisifyFn<T>
```
```

## File: `skills/vueuse-functions/references/useThrottledRefHistory.md`
```markdown
---
category: State
related: useDebouncedRefHistory, useRefHistory
---

# useThrottledRefHistory

Shorthand for `useRefHistory` with throttled filter.

## Usage

This function takes the first snapshot right after the counter's value was changed and the second with a delay of 1000ms.

```ts
import { useThrottledRefHistory } from '@vueuse/core'
import { shallowRef } from 'vue'

const counter = shallowRef(0)
const { history, undo, redo } = useThrottledRefHistory(counter, { deep: true, throttle: 1000 })
```

## Type Declarations

```ts
export type UseThrottledRefHistoryOptions<Raw, Serialized = Raw> = Omit<
  UseRefHistoryOptions<Raw, Serialized>,
  "eventFilter"
> & {
  throttle?: MaybeRef<number>
  trailing?: boolean
}
export type UseThrottledRefHistoryReturn<
  Raw,
  Serialized = Raw,
> = UseRefHistoryReturn<Raw, Serialized>
/**
 * Shorthand for [useRefHistory](https://vueuse.org/useRefHistory) with throttled filter.
 *
 * @see https://vueuse.org/useThrottledRefHistory
 * @param source
 * @param options
 */
export declare function useThrottledRefHistory<Raw, Serialized = Raw>(
  source: Ref<Raw>,
  options?: UseThrottledRefHistoryOptions<Raw, Serialized>,
): UseThrottledRefHistoryReturn<Raw, Serialized>
```
```

## File: `skills/vueuse-functions/references/useTimeAgo.md`
```markdown
---
category: Time
---

# useTimeAgo

Reactive time ago. Automatically update the time ago string when the time changes.

## Usage

```ts
import { useTimeAgo } from '@vueuse/core'

const timeAgo = useTimeAgo(new Date(2021, 0, 1))
```

## Component Usage

```vue
<template>
  <UseTimeAgo v-slot="{ timeAgo }" :time="new Date(2021, 0, 1)">
    Time Ago: {{ timeAgo }}
  </UseTimeAgo>
</template>
```

## Non-Reactivity Usage

In case you don't need the reactivity, you can use the `formatTimeAgo` function to get the formatted string instead of a Ref.

```ts
import { formatTimeAgo } from '@vueuse/core'

const timeAgo = formatTimeAgo(new Date(2021, 0, 1)) // string
```

## Type Declarations

```ts
export type UseTimeAgoFormatter<T = number> = (
  value: T,
  isPast: boolean,
) => string
export type UseTimeAgoUnitNamesDefault =
  | "second"
  | "minute"
  | "hour"
  | "day"
  | "week"
  | "month"
  | "year"
export interface UseTimeAgoMessagesBuiltIn {
  justNow: string
  past: string | UseTimeAgoFormatter<string>
  future: string | UseTimeAgoFormatter<string>
  invalid: string
}
export type UseTimeAgoMessages<
  UnitNames extends string = UseTimeAgoUnitNamesDefault,
> = UseTimeAgoMessagesBuiltIn &
  Record<UnitNames, string | UseTimeAgoFormatter<number>>
export interface FormatTimeAgoOptions<
  UnitNames extends string = UseTimeAgoUnitNamesDefault,
> {
  /**
   * Maximum unit (of diff in milliseconds) to display the full date instead of relative
   *
   * @default undefined
   */
  max?: UnitNames | number
  /**
   * Formatter for full date
   */
  fullDateFormatter?: (date: Date) => string
  /**
   * Messages for formatting the string
   */
  messages?: UseTimeAgoMessages<UnitNames>
  /**
   * Minimum display time unit (default is minute)
   *
   * @default false
   */
  showSecond?: boolean
  /**
   * Rounding method to apply.
   *
   * @default 'round'
   */
  rounding?: "round" | "ceil" | "floor" | number
  /**
   * Custom units
   */
  units?: UseTimeAgoUnit<UnitNames>[]
}
export interface UseTimeAgoOptions<
  Controls extends boolean,
  UnitNames extends string = UseTimeAgoUnitNamesDefault,
>
  extends FormatTimeAgoOptions<UnitNames>, ConfigurableScheduler {
  /**
   * Expose more controls
   *
   * @default false
   */
  controls?: Controls
  /**
   * Intervals to update, set 0 to disable auto update
   *
   * @deprecated Please use `scheduler` option instead
   * @default 30_000
   */
  updateInterval?: number
}
export interface UseTimeAgoUnit<
  Unit extends string = UseTimeAgoUnitNamesDefault,
> {
  max: number
  value: number
  name: Unit
}
export type UseTimeAgoReturn<Controls extends boolean = false> =
  Controls extends true
    ? {
        timeAgo: ComputedRef<string>
      } & Pausable
    : ComputedRef<string>
/**
 * Reactive time ago formatter.
 *
 * @see https://vueuse.org/useTimeAgo
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useTimeAgo<
  UnitNames extends string = UseTimeAgoUnitNamesDefault,
>(
  time: MaybeRefOrGetter<Date | number | string>,
  options?: UseTimeAgoOptions<false, UnitNames>,
): UseTimeAgoReturn<false>
export declare function useTimeAgo<
  UnitNames extends string = UseTimeAgoUnitNamesDefault,
>(
  time: MaybeRefOrGetter<Date | number | string>,
  options: UseTimeAgoOptions<true, UnitNames>,
): UseTimeAgoReturn<true>
export declare function formatTimeAgo<
  UnitNames extends string = UseTimeAgoUnitNamesDefault,
>(
  from: Date,
  options?: FormatTimeAgoOptions<UnitNames>,
  now?: Date | number,
): string
```
```

## File: `skills/vueuse-functions/references/useTimeAgoIntl.md`
```markdown
---
category: Time
---

# useTimeAgoIntl

Reactive time ago with i18n supported. Automatically update the time ago string when the time changes. Powered by `Intl.RelativeTimeFormat`.

## Usage

```js
import { useTimeAgoIntl } from '@vueuse/core'

const timeAgoIntl = useTimeAgoIntl(new Date(2021, 0, 1))
```

## Non-Reactivity Usage

In case you don't need the reactivity, you can use the `formatTimeAgo` function to get the formatted string instead of a Ref.

```js
import { formatTimeAgoIntl } from '@vueuse/core'

const timeAgoIntl = formatTimeAgoIntl(new Date(2021, 0, 1)) // string
```

## Type Declarations

```ts
type Locale = Intl.UnicodeBCP47LocaleIdentifier | Intl.Locale
export interface FormatTimeAgoIntlOptions {
  /**
   * The locale to format with
   *
   * @default undefined
   * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#locales
   */
  locale?: Locale
  /**
   * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#options
   */
  relativeTimeFormatOptions?: Intl.RelativeTimeFormatOptions
  /**
   * Whether to insert spaces between parts.
   *
   * Ignored if `joinParts` is provided.
   *
   * @default true
   */
  insertSpace?: boolean
  /**
   * Custom function to join the parts returned by `Intl.RelativeTimeFormat.formatToParts`.
   *
   * If provided, it will be used instead of the default join logic.
   */
  joinParts?: (
    parts: Intl.RelativeTimeFormatPart[],
    locale?: Intl.UnicodeBCP47LocaleIdentifier | Intl.Locale,
  ) => string
  /**
   * Custom units
   */
  units?: TimeAgoUnit[]
}
export interface UseTimeAgoIntlOptions<Controls extends boolean>
  extends FormatTimeAgoIntlOptions, ConfigurableScheduler {
  /**
   * Expose more controls and the raw `parts` result.
   *
   * @default false
   */
  controls?: Controls
  /**
   * Update interval in milliseconds, set 0 to disable auto update
   *
   * @deprecated Please use `scheduler` option instead
   * @default 30_000
   */
  updateInterval?: number
}
type UseTimeAgoReturn<Controls extends boolean = false> = Controls extends true
  ? {
      timeAgoIntl: ComputedRef<string>
      parts: ComputedRef<Intl.RelativeTimeFormatPart[]>
    } & Pausable
  : ComputedRef<string>
export interface TimeAgoUnit {
  name: Intl.RelativeTimeFormatUnit
  ms: number
}
/**
 * A reactive wrapper for `Intl.RelativeTimeFormat`.
 */
export declare function useTimeAgoIntl(
  time: MaybeRefOrGetter<Date | number | string>,
  options?: UseTimeAgoIntlOptions<false>,
): UseTimeAgoReturn<false>
export declare function useTimeAgoIntl(
  time: MaybeRefOrGetter<Date | number | string>,
  options: UseTimeAgoIntlOptions<true>,
): UseTimeAgoReturn<true>
/**
 * Non-reactive version of useTimeAgoIntl
 */
export declare function formatTimeAgoIntl(
  from: Date,
  options?: FormatTimeAgoIntlOptions,
  now?: Date | number,
): string
/**
 * Format parts into a string
 */
export declare function formatTimeAgoIntlParts(
  parts: Intl.RelativeTimeFormatPart[],
  options?: FormatTimeAgoIntlOptions,
): string
```
```

## File: `skills/vueuse-functions/references/useTimeout.md`
```markdown
---
category: Animation
---

# useTimeout

Reactive value that becomes `true` after a given time.

## Usage

```ts
import { useTimeout } from '@vueuse/core'

const ready = useTimeout(1000)
```

After 1 second, `ready.value` becomes `true`.

### With Controls

```ts
import { useTimeout } from '@vueuse/core'

const { ready, start, stop, isPending } = useTimeout(1000, { controls: true })

// Check if timeout is pending
console.log(isPending.value) // true

// Stop the timeout
stop()

// Start/restart the timeout
start()
```

### Options

| Option      | Type         | Default | Description                                      |
| ----------- | ------------ | ------- | ------------------------------------------------ |
| `controls`  | `boolean`    | `false` | Expose `start`, `stop`, and `isPending` controls |
| `immediate` | `boolean`    | `true`  | Start the timeout immediately                    |
| `callback`  | `() => void` | —       | Called when the timeout completes                |

### Callback on Timeout

```ts
import { useTimeout } from '@vueuse/core'

useTimeout(1000, {
  callback: () => {
    console.log('Timeout completed!')
  },
})
```

### Reactive Interval

The timeout duration can be reactive:

```ts
import { useTimeout } from '@vueuse/core'

const duration = ref(1000)
const ready = useTimeout(duration)

// Change the duration (only affects future timeouts when using controls)
duration.value = 2000
```

## Type Declarations

```ts
export interface UseTimeoutOptions<
  Controls extends boolean,
> extends UseTimeoutFnOptions {
  /**
   * Expose more controls
   *
   * @default false
   */
  controls?: Controls
  /**
   * Callback on timeout
   */
  callback?: Fn
}
export type UseTimeoutReturn =
  | ComputedRef<boolean>
  | ({
      readonly ready: ComputedRef<boolean>
    } & Stoppable)
/**
 * @deprecated use UseTimeoutReturn instead
 */
export type UseTimoutReturn = UseTimeoutReturn
/**
 * Update value after a given time with controls.
 *
 * @see   {@link https://vueuse.org/useTimeout}
 * @param interval
 * @param options
 */
export declare function useTimeout(
  interval?: MaybeRefOrGetter<number>,
  options?: UseTimeoutOptions<false>,
): ComputedRef<boolean>
export declare function useTimeout(
  interval: MaybeRefOrGetter<number>,
  options: UseTimeoutOptions<true>,
): {
  ready: ComputedRef<boolean>
} & Stoppable
```
```

## File: `skills/vueuse-functions/references/useTimeoutFn.md`
```markdown
---
category: Animation
---

# useTimeoutFn

Wrapper for `setTimeout` with controls.

## Usage

```ts
import { useTimeoutFn } from '@vueuse/core'

const { isPending, start, stop } = useTimeoutFn(() => {
  /* ... */
}, 3000)
```

## Type Declarations

```ts
export interface UseTimeoutFnOptions {
  /**
   * Start the timer immediately
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Execute the callback immediately after calling `start`
   *
   * @default false
   */
  immediateCallback?: boolean
}
export type UseTimeoutFnReturn<CallbackFn extends AnyFn> = Stoppable<
  Parameters<CallbackFn> | []
>
/**
 * Wrapper for `setTimeout` with controls.
 *
 * @param cb
 * @param interval
 * @param options
 */
export declare function useTimeoutFn<CallbackFn extends AnyFn>(
  cb: CallbackFn,
  interval: MaybeRefOrGetter<number>,
  options?: UseTimeoutFnOptions,
): UseTimeoutFnReturn<CallbackFn>
```
```

## File: `skills/vueuse-functions/references/useTimeoutPoll.md`
```markdown
---
category: Utilities
---

# useTimeoutPoll

Use timeout to poll something. It will trigger callback after last task is done.

## Usage

```ts
import { useTimeoutPoll } from '@vueuse/core'

const count = ref(0)

async function fetchData() {
  await new Promise(resolve => setTimeout(resolve, 1000))
  count.value++
}

// Only trigger after last fetch is done
const { isActive, pause, resume } = useTimeoutPoll(fetchData, 1000)
```

## Type Declarations

```ts
export interface UseTimeoutPollOptions {
  /**
   * Start the timer immediately
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Execute the callback immediately after calling `resume`
   *
   * @default false
   */
  immediateCallback?: boolean
}
export declare function useTimeoutPoll(
  fn: () => Awaitable<void>,
  interval: MaybeRefOrGetter<number>,
  options?: UseTimeoutFnOptions,
): Pausable
```
```

## File: `skills/vueuse-functions/references/useTimestamp.md`
```markdown
---
category: Animation
---

# useTimestamp

Reactive current timestamp

## Usage

```ts
import { useTimestamp } from '@vueuse/core'

const timestamp = useTimestamp({ offset: 0 })
```

```ts
import { useTimestamp } from '@vueuse/core'
// ---cut---
const { timestamp, pause, resume } = useTimestamp({ controls: true })
```

## Component Usage

```vue
<template>
  <UseTimestamp v-slot="{ timestamp, pause, resume }">
    Current Time: {{ timestamp }}
    <button @click="pause()">
      Pause
    </button>
    <button @click="resume()">
      Resume
    </button>
  </UseTimestamp>
</template>
```

## Type Declarations

```ts
export interface UseTimestampOptions<
  Controls extends boolean,
> extends ConfigurableScheduler {
  /**
   * Expose more controls
   *
   * @default false
   */
  controls?: Controls
  /**
   * Offset value adding to the value
   *
   * @default 0
   */
  offset?: number
  /**
   * Update the timestamp immediately
   *
   * @deprecated Please use `scheduler` option instead
   * @default true
   */
  immediate?: boolean
  /**
   * Update interval, or use requestAnimationFrame
   *
   * @deprecated Please use `scheduler` option instead
   * @default requestAnimationFrame
   */
  interval?: "requestAnimationFrame" | number
  /**
   * Callback on each update
   */
  callback?: (timestamp: number) => void
}
export type UseTimestampReturn<Controls extends boolean> = Controls extends true
  ? {
      timestamp: ShallowRef<number>
    } & Pausable
  : ShallowRef<number>
/**
 * Reactive current timestamp.
 *
 * @see https://vueuse.org/useTimestamp
 * @param options
 */
export declare function useTimestamp(
  options?: UseTimestampOptions<false>,
): ShallowRef<number>
export declare function useTimestamp(options: UseTimestampOptions<true>): {
  timestamp: ShallowRef<number>
} & Pausable
```
```

## File: `skills/vueuse-functions/references/useTitle.md`
```markdown
---
category: Browser
---

# useTitle

Reactive document title.

::: warning
This composable isn't compatible with SSR.
:::

## Usage

```ts
import { useTitle } from '@vueuse/core'

const title = useTitle()
console.log(title.value) // print current title
title.value = 'Hello' // change current title
```

Set initial title immediately:

```ts
import { useTitle } from '@vueuse/core'
// ---cut---
const title = useTitle('New Title')
```

Pass a `ref` and the title will be updated when the source ref changes:

```ts
import { useTitle } from '@vueuse/core'
import { shallowRef } from 'vue'

const messages = shallowRef(0)

const title = computed(() => {
  return !messages.value ? 'No message' : `${messages.value} new messages`
})

useTitle(title) // document title will match with the ref "title"
```

Pass an optional template tag [Vue Meta Title Template](https://vue-meta.nuxtjs.org/guide/metainfo.html) to update the title to be injected into this template:

```ts
import { useTitle } from '@vueuse/core'
// ---cut---
const title = useTitle('New Title', {
  titleTemplate: '%s | My Awesome Website'
})
```

::: warning
`observe` is incompatible with `titleTemplate`.
:::

## Type Declarations

```ts
export type UseTitleOptionsBase = {
  /**
   * Restore the original title when unmounted
   * @param originTitle original title
   * @returns restored title
   */
  restoreOnUnmount?:
    | false
    | ((
        originalTitle: string,
        currentTitle: string,
      ) => string | null | undefined)
} & (
  | {
      /**
       * Observe `document.title` changes using MutationObserve
       * Cannot be used together with `titleTemplate` option.
       *
       * @default false
       */
      observe?: boolean
    }
  | {
      /**
       * The template string to parse the title (e.g., '%s | My Website')
       * Cannot be used together with `observe` option.
       *
       * @default '%s'
       */
      titleTemplate?: MaybeRef<string> | ((title: string) => string)
    }
)
export type UseTitleOptions = ConfigurableDocument & UseTitleOptionsBase
export type UseTitleReturn =
  | ComputedRef<string | null | undefined>
  | Ref<string | null | undefined>
/**
 * Reactive document title.
 *
 * @see https://vueuse.org/useTitle
 * @param newTitle
 * @param options
 * @description It's not SSR compatible. Your value will be applied only on client-side.
 */
export declare function useTitle(
  newTitle: ReadonlyRefOrGetter<string | null | undefined>,
  options?: UseTitleOptions,
): ComputedRef<string | null | undefined>
export declare function useTitle(
  newTitle?: MaybeRef<string | null | undefined>,
  options?: UseTitleOptions,
): Ref<string | null | undefined>
```
```

## File: `skills/vueuse-functions/references/useToNumber.md`
```markdown
---
category: Utilities
---

# useToNumber

Reactively convert a string ref to number.

## Usage

```ts
import { useToNumber } from '@vueuse/core'
import { shallowRef } from 'vue'

const str = shallowRef('123')
const number = useToNumber(str)

number.value // 123
```

## Type Declarations

```ts
export interface UseToNumberOptions {
  /**
   * Method to use to convert the value to a number.
   *
   * Or a custom function for the conversion.
   *
   * @default 'parseFloat'
   */
  method?: "parseFloat" | "parseInt" | ((value: string | number) => number)
  /**
   * The base in mathematical numeral systems passed to `parseInt`.
   * Only works with `method: 'parseInt'`
   */
  radix?: number
  /**
   * Replace NaN with zero
   *
   * @default false
   */
  nanToZero?: boolean
}
/**
 * Reactively convert a string ref to number.
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useToNumber(
  value: MaybeRefOrGetter<number | string>,
  options?: UseToNumberOptions,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useToString.md`
```markdown
---
category: Utilities
---

# useToString

Reactively convert a ref to string.

## Usage

```ts
import { useToString } from '@vueuse/core'
import { shallowRef } from 'vue'

const number = shallowRef(3.14)
const str = useToString(number)

str.value // '3.14'
```

## Type Declarations

```ts
/**
 * Reactively convert a ref to string.
 *
 * @see https://vueuse.org/useToString
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useToString(
  value: MaybeRefOrGetter<unknown>,
): ComputedRef<string>
```
```

## File: `skills/vueuse-functions/references/useToggle.md`
```markdown
---
category: Utilities
---

# useToggle

A boolean switcher with utility functions.

## Usage

```ts
import { useToggle } from '@vueuse/core'

const [value, toggle] = useToggle()
```

When you pass a ref, `useToggle` will return a simple toggle function instead:

```ts
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)
```

### Toggle Function

The toggle function can be called in two ways:

```ts
const [value, toggle] = useToggle()

toggle() // toggle between true and false
toggle(true) // set to specific value

// The toggle function returns the new value
const newValue = toggle() // returns the new value after toggling
```

### Custom Values

You can use custom truthy and falsy values instead of `true` and `false`:

```ts
import { useToggle } from '@vueuse/core'

const [value, toggle] = useToggle('on', {
  truthyValue: 'on',
  falsyValue: 'off',
})

toggle() // 'off'
toggle() // 'on'
```

The custom values can also be reactive:

```ts
import { useToggle } from '@vueuse/core'
import { ref } from 'vue'

const truthy = ref('yes')
const falsy = ref('no')

const [value, toggle] = useToggle('yes', {
  truthyValue: truthy,
  falsyValue: falsy,
})
```

## Caution

Be aware that the toggle function accepts the first argument as the override value. You might want to avoid directly passing the function to events in the template, as the event object will be passed in.

```html
<!-- caution: $event will be passed in -->
<button @click="toggleDark" />
<!-- recommended to do this -->
<button @click="toggleDark()" />
```

## Type Declarations

```ts
export type ToggleFn = (value?: boolean) => void
export type UseToggleReturn = [ShallowRef<boolean>, ToggleFn] | ToggleFn
export interface UseToggleOptions<Truthy, Falsy> {
  truthyValue?: MaybeRefOrGetter<Truthy>
  falsyValue?: MaybeRefOrGetter<Falsy>
}
export declare function useToggle<Truthy, Falsy, T = Truthy | Falsy>(
  initialValue: Ref<T>,
  options?: UseToggleOptions<Truthy, Falsy>,
): (value?: T) => T
export declare function useToggle<
  Truthy = true,
  Falsy = false,
  T = Truthy | Falsy,
>(
  initialValue?: T,
  options?: UseToggleOptions<Truthy, Falsy>,
): [ShallowRef<T>, (value?: T) => T]
```
```

## File: `skills/vueuse-functions/references/useTransition.md`
```markdown
---
category: Animation
---

# useTransition

Transition between values

## Usage

Define a source value to follow, and when changed the output will transition to the new value. If the source changes while a transition is in progress, a new transition will begin from where the previous one was interrupted.

```ts
import { TransitionPresets, useTransition } from '@vueuse/core'
import { shallowRef } from 'vue'

const source = shallowRef(0)

const output = useTransition(source, {
  duration: 1000,
  easing: TransitionPresets.easeInOutCubic,
})
```

Transition easing can be customized using [cubic bezier curves](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/cubic-bezier#description).

```ts
import { useTransition } from '@vueuse/core'
// ---cut---
useTransition(source, {
  easing: [0.75, 0, 0.25, 1],
})
```

The following transitions are available via the `TransitionPresets` constant.

- [`linear`](https://cubic-bezier.com/#0,0,1,1)
- [`easeInSine`](https://cubic-bezier.com/#.12,0,.39,0)
- [`easeOutSine`](https://cubic-bezier.com/#.61,1,.88,1)
- [`easeInOutSine`](https://cubic-bezier.com/#.37,0,.63,1)
- [`easeInQuad`](https://cubic-bezier.com/#.11,0,.5,0)
- [`easeOutQuad`](https://cubic-bezier.com/#.5,1,.89,1)
- [`easeInOutQuad`](https://cubic-bezier.com/#.45,0,.55,1)
- [`easeInCubic`](https://cubic-bezier.com/#.32,0,.67,0)
- [`easeOutCubic`](https://cubic-bezier.com/#.33,1,.68,1)
- [`easeInOutCubic`](https://cubic-bezier.com/#.65,0,.35,1)
- [`easeInQuart`](https://cubic-bezier.com/#.5,0,.75,0)
- [`easeOutQuart`](https://cubic-bezier.com/#.25,1,.5,1)
- [`easeInOutQuart`](https://cubic-bezier.com/#.76,0,.24,1)
- [`easeInQuint`](https://cubic-bezier.com/#.64,0,.78,0)
- [`easeOutQuint`](https://cubic-bezier.com/#.22,1,.36,1)
- [`easeInOutQuint`](https://cubic-bezier.com/#.83,0,.17,1)
- [`easeInExpo`](https://cubic-bezier.com/#.7,0,.84,0)
- [`easeOutExpo`](https://cubic-bezier.com/#.16,1,.3,1)
- [`easeInOutExpo`](https://cubic-bezier.com/#.87,0,.13,1)
- [`easeInCirc`](https://cubic-bezier.com/#.55,0,1,.45)
- [`easeOutCirc`](https://cubic-bezier.com/#0,.55,.45,1)
- [`easeInOutCirc`](https://cubic-bezier.com/#.85,0,.15,1)
- [`easeInBack`](https://cubic-bezier.com/#.36,0,.66,-.56)
- [`easeOutBack`](https://cubic-bezier.com/#.34,1.56,.64,1)
- [`easeInOutBack`](https://cubic-bezier.com/#.68,-.6,.32,1.6)

For more complex easing, a custom function can be provided.

```ts
import { useTransition } from '@vueuse/core'
// ---cut---
function easeOutElastic(n) {
  return n === 0
    ? 0
    : n === 1
      ? 1
      : (2 ** (-10 * n)) * Math.sin((n * 10 - 0.75) * ((2 * Math.PI) / 3)) + 1
}

useTransition(source, {
  easing: easeOutElastic,
})
```

By default the `source` must be a number, or array of numbers. For more complex values, define a custom `interpolation` function. For example, the following would transition a Three.js rotation.

```ts
import { useTransition } from '@vueuse/core'
// ---cut---
import { Quaternion } from 'three'

const source = ref(new Quaternion())

const output = useTransition(source, {
  interpolation: (q1, q2, t) => new Quaternion().slerpQuaternions(q1, q2, t)
})
```

To control when a transition starts, set a `delay` value. To choreograph behavior around a transition, define `onStarted` or `onFinished` callbacks.

```ts
import { useTransition } from '@vueuse/core'
// ---cut---
useTransition(source, {
  delay: 1000,
  onStarted() {
    // called after the transition starts
  },
  onFinished() {
    // called after the transition ends
  },
})
```

To stop transitioning, define a boolean `disabled` property. Be aware, this is not the same a `duration` of `0`. Disabled transitions track the source value **_synchronously_**. They do not respect a `delay`, and do not fire `onStarted` or `onFinished` callbacks.

For even more control, transitions can be executed manually via the `transition` function. This function returns a promise that resolves when the transition is complete. Manual transitions can be cancelled by defining an `abort` function that returns a truthy value.

```ts
import { transition } from '@vueuse/core'

await transition(source, from, to, {
  abort() {
    if (shouldAbort)
      return true
  }
})
```

## Type Declarations

```ts
/**
 * Cubic bezier points
 */
export type CubicBezierPoints = [number, number, number, number]
/**
 * Easing function
 */
export type EasingFunction = (n: number) => number
/**
 * Interpolation function
 */
export type InterpolationFunction<T> = (from: T, to: T, t: number) => T
/**
 * Transition options
 */
export interface TransitionOptions<T> extends ConfigurableWindow {
  /**
   * Manually abort a transition
   */
  abort?: () => any
  /**
   * Transition duration in milliseconds
   */
  duration?: MaybeRef<number>
  /**
   * Easing function or cubic bezier points to calculate transition progress
   */
  easing?: MaybeRef<EasingFunction | CubicBezierPoints>
  /**
   * Custom interpolation function
   */
  interpolation?: InterpolationFunction<T>
  /**
   * Easing function or cubic bezier points to calculate transition progress
   * @deprecated The `transition` option is deprecated, use `easing` instead.
   */
  transition?: MaybeRef<EasingFunction | CubicBezierPoints>
}
export interface UseTransitionOptions<T> extends TransitionOptions<T> {
  /**
   * Milliseconds to wait before starting transition
   */
  delay?: MaybeRef<number>
  /**
   * Disables the transition
   */
  disabled?: MaybeRef<boolean>
  /**
   * Callback to execute after transition finishes
   */
  onFinished?: () => void
  /**
   * Callback to execute after transition starts
   */
  onStarted?: () => void
}
declare const _TransitionPresets: {
  readonly easeInSine: readonly [0.12, 0, 0.39, 0]
  readonly easeOutSine: readonly [0.61, 1, 0.88, 1]
  readonly easeInOutSine: readonly [0.37, 0, 0.63, 1]
  readonly easeInQuad: readonly [0.11, 0, 0.5, 0]
  readonly easeOutQuad: readonly [0.5, 1, 0.89, 1]
  readonly easeInOutQuad: readonly [0.45, 0, 0.55, 1]
  readonly easeInCubic: readonly [0.32, 0, 0.67, 0]
  readonly easeOutCubic: readonly [0.33, 1, 0.68, 1]
  readonly easeInOutCubic: readonly [0.65, 0, 0.35, 1]
  readonly easeInQuart: readonly [0.5, 0, 0.75, 0]
  readonly easeOutQuart: readonly [0.25, 1, 0.5, 1]
  readonly easeInOutQuart: readonly [0.76, 0, 0.24, 1]
  readonly easeInQuint: readonly [0.64, 0, 0.78, 0]
  readonly easeOutQuint: readonly [0.22, 1, 0.36, 1]
  readonly easeInOutQuint: readonly [0.83, 0, 0.17, 1]
  readonly easeInExpo: readonly [0.7, 0, 0.84, 0]
  readonly easeOutExpo: readonly [0.16, 1, 0.3, 1]
  readonly easeInOutExpo: readonly [0.87, 0, 0.13, 1]
  readonly easeInCirc: readonly [0.55, 0, 1, 0.45]
  readonly easeOutCirc: readonly [0, 0.55, 0.45, 1]
  readonly easeInOutCirc: readonly [0.85, 0, 0.15, 1]
  readonly easeInBack: readonly [0.36, 0, 0.66, -0.56]
  readonly easeOutBack: readonly [0.34, 1.56, 0.64, 1]
  readonly easeInOutBack: readonly [0.68, -0.6, 0.32, 1.6]
}
/**
 * Common transitions
 *
 * @see https://easings.net
 */
export declare const TransitionPresets: Record<
  keyof typeof _TransitionPresets,
  CubicBezierPoints
> & {
  linear: EasingFunction
}
/**
 * Transition from one value to another.
 *
 * @param source
 * @param from
 * @param to
 * @param options
 */
export declare function transition<T>(
  source: Ref<T>,
  from: MaybeRefOrGetter<T>,
  to: MaybeRefOrGetter<T>,
  options?: TransitionOptions<T>,
): PromiseLike<void>
/**
 * Transition from one value to another.
 * @deprecated The `executeTransition` function is deprecated, use `transition` instead.
 *
 * @param source
 * @param from
 * @param to
 * @param options
 */
export declare function executeTransition<T>(
  source: Ref<T>,
  from: MaybeRefOrGetter<T>,
  to: MaybeRefOrGetter<T>,
  options?: TransitionOptions<T>,
): PromiseLike<void>
export declare function useTransition<T extends MaybeRefOrGetter<number>[]>(
  source: [...T],
  options?: UseTransitionOptions<T>,
): ComputedRef<{
  [K in keyof T]: number
}>
export declare function useTransition<T extends MaybeRefOrGetter<number[]>>(
  source: T,
  options?: UseTransitionOptions<T>,
): ComputedRef<number[]>
export declare function useTransition<T>(
  source: MaybeRefOrGetter<T>,
  options?: UseTransitionOptions<T>,
): ComputedRef<T>
```
```

## File: `skills/vueuse-functions/references/useTrunc.md`
```markdown
---
category: '@Math'
---

# useTrunc

Reactive `Math.trunc`.

## Usage

```ts
import { useTrunc } from '@vueuse/math'

const value1 = ref(0.95)
const value2 = ref(-2.34)
const result1 = useTrunc(value1) // 0
const result2 = useTrunc(value2) // -2
```

## Type Declarations

```ts
/**
 * Reactive `Math.trunc`.
 *
 * @see https://vueuse.org/useTrunc
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useTrunc(
  value: MaybeRefOrGetter<number>,
): ComputedRef<number>
```
```

## File: `skills/vueuse-functions/references/useUrlSearchParams.md`
```markdown
---
category: Browser
---

# useUrlSearchParams

Reactive [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)

## Usage

```ts
import { useUrlSearchParams } from '@vueuse/core'

const params = useUrlSearchParams('history')

console.log(params.foo) // 'bar'

params.foo = 'bar'
params.vueuse = 'awesome'
// url updated to `?foo=bar&vueuse=awesome`
```

### Hash Mode

When using with hash mode route, specify the `mode` to `hash`

```ts
import { useUrlSearchParams } from '@vueuse/core'

const params = useUrlSearchParams('hash')

params.foo = 'bar'
params.vueuse = 'awesome'
// url updated to `#/your/route?foo=bar&vueuse=awesome`
```

### Hash Params

When using with history mode route, but want to use hash as params, specify the `mode` to `hash-params`

```ts
import { useUrlSearchParams } from '@vueuse/core'

const params = useUrlSearchParams('hash-params')

params.foo = 'bar'
params.vueuse = 'awesome'
// url updated to `/your/route#foo=bar&vueuse=awesome`
```

### Custom Stringify Function

You can provide a custom function to serialize URL parameters using the `stringify` option. This is useful when you need special formatting for your query string.

```js
import { useUrlSearchParams } from '@vueuse/core'

// Custom stringify function that removes equal signs for empty values
const params = useUrlSearchParams('history', {
  stringify: (params) => {
    return params.toString().replace(/=(&|$)/g, '$1')
  }
})

params.foo = ''
params.bar = 'value'
// url updated to `?foo&bar=value` instead of `?foo=&bar=value`
```

## Type Declarations

```ts
export type UrlParams = Record<string, string[] | string>
export interface UseUrlSearchParamsOptions<T> extends ConfigurableWindow {
  /**
   * @default true
   */
  removeNullishValues?: boolean
  /**
   * @default false
   */
  removeFalsyValues?: boolean
  /**
   * @default {}
   */
  initialValue?: T
  /**
   * Write back to `window.history` automatically
   *
   * @default true
   */
  write?: boolean
  /**
   * Write mode for `window.history` when `write` is enabled
   * - `replace`: replace the current history entry
   * - `push`: push a new history entry
   * @default 'replace'
   */
  writeMode?: "replace" | "push"
  /**
   * Custom function to serialize URL parameters
   * When provided, this function will be used instead of the default URLSearchParams.toString()
   * @param params The URLSearchParams object to serialize
   * @returns The serialized query string (should not include the leading '?' or '#')
   */
  stringify?: (params: URLSearchParams) => string
}
/**
 * Reactive URLSearchParams
 *
 * @see https://vueuse.org/useUrlSearchParams
 * @param mode
 * @param options
 */
export declare function useUrlSearchParams<
  T extends Record<string, any> = UrlParams,
>(
  mode?: "history" | "hash" | "hash-params",
  options?: UseUrlSearchParamsOptions<T>,
): T
```
```

## File: `skills/vueuse-functions/references/useUserMedia.md`
```markdown
---
category: Sensors
related: useDevicesList, usePermission
---

# useUserMedia

Reactive [`mediaDevices.getUserMedia`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) streaming.

## Usage

```vue
<script setup lang="ts">
import { useUserMedia } from '@vueuse/core'
import { useTemplateRef, watchEffect } from 'vue'

const { stream, start } = useUserMedia()
start()

const videoRef = useTemplateRef('video')
watchEffect(() => {
  // preview on a video element
  videoRef.value.srcObject = stream.value
})
</script>

<template>
  <video ref="video" />
</template>
```

### Devices

```ts
import { useDevicesList, useUserMedia } from '@vueuse/core'
import { computed, reactive } from 'vue'

const {
  videoInputs: cameras,
  audioInputs: microphones,
} = useDevicesList({
  requestPermissions: true,
})
const currentCamera = computed(() => cameras.value[0]?.deviceId)
const currentMicrophone = computed(() => microphones.value[0]?.deviceId)

const { stream } = useUserMedia({
  constraints: reactive({
    video: { deviceId: currentCamera },
    audio: { deviceId: currentMicrophone, }
  })
})
```

## Type Declarations

```ts
export interface UseUserMediaOptions extends ConfigurableNavigator {
  /**
   * If the stream is enabled
   * @default false
   */
  enabled?: MaybeRef<boolean>
  /**
   * Recreate stream when deviceIds or constraints changed
   *
   * @default true
   */
  autoSwitch?: MaybeRef<boolean>
  /**
   * MediaStreamConstraints to be applied to the requested MediaStream
   * If provided, the constraints will override videoDeviceId and audioDeviceId
   *
   * @default {}
   */
  constraints?: MaybeRef<MediaStreamConstraints>
}
export interface UseUserMediaReturn extends Supportable {
  stream: Ref<MediaStream | undefined>
  start: () => Promise<MediaStream | undefined>
  stop: () => void
  restart: () => Promise<MediaStream | undefined>
  constraints: Ref<MediaStreamConstraints | undefined>
  enabled: ShallowRef<boolean>
  autoSwitch: ShallowRef<boolean>
}
/**
 * Reactive `mediaDevices.getUserMedia` streaming
 *
 * @see https://vueuse.org/useUserMedia
 * @param options
 */
export declare function useUserMedia(
  options?: UseUserMediaOptions,
): UseUserMediaReturn
```
```

## File: `skills/vueuse-functions/references/useVModel.md`
```markdown
---
category: Component
---

# useVModel

Shorthand for v-model binding, props + emit -> ref

> We encourage you to use Vue's [`defineModel`](https://vuejs.org/api/sfc-script-setup.html#definemodel) over this composable, however there are some edge-cases like using `TSX` or the `deep: true` option that `defineModel` doesn't support.

## Usage

```ts
import { useVModel } from '@vueuse/core'

const props = defineProps<{
  modelValue: string
}>()
const emit = defineEmits(['update:modelValue'])

const data = useVModel(props, 'modelValue', emit)
```

### Options API

```ts
import { useVModel } from '@vueuse/core'

export default {
  setup(props, { emit }) {
    const data = useVModel(props, 'data', emit)

    console.log(data.value) // props.data
    data.value = 'foo' // emit('update:data', 'foo')
  },
}
```

## Options

### Passive Mode

By default, `useVModel` returns a computed ref. In passive mode, it creates a local ref that syncs with the prop via `watch`, allowing deep reactivity tracking.

```ts
const data = useVModel(props, 'modelValue', emit, { passive: true })
```

### Deep Watching

When using `passive: true`, you can enable deep watching for nested object changes:

```ts
const data = useVModel(props, 'modelValue', emit, {
  passive: true,
  deep: true,
})
```

### Clone Values

Clone the prop value to avoid mutating the original object. Set to `true` to use `JSON.parse(JSON.stringify())` or provide a custom clone function.

```ts
const data = useVModel(props, 'modelValue', emit, {
  clone: true,
  // or provide custom clone function
  // clone: (val) => structuredClone(val),
})
```

### Default Value

Provide a default value when the prop is undefined:

```ts
const data = useVModel(props, 'modelValue', emit, {
  defaultValue: 'default',
})
```

### Custom Event Name

Override the default `update:propName` event name:

```ts
const data = useVModel(props, 'value', emit, {
  eventName: 'change',
})
```

### Emit Validation

Use `shouldEmit` to validate before emitting. Return `false` to prevent the emit:

```ts
const data = useVModel(props, 'modelValue', emit, {
  shouldEmit: (value) => {
    // Only emit if value is valid
    return value.length > 0
  },
})
```

## Type Declarations

```ts
export interface UseVModelOptions<T, Passive extends boolean = false> {
  /**
   * When passive is set to `true`, it will use `watch` to sync with props and ref.
   * Instead of relying on the `v-model` or `.sync` to work.
   *
   * @default false
   */
  passive?: Passive
  /**
   * When eventName is set, it's value will be used to overwrite the emit event name.
   *
   * @default undefined
   */
  eventName?: string
  /**
   * Attempting to check for changes of properties in a deeply nested object or array.
   * Apply only when `passive` option is set to `true`
   *
   * @default false
   */
  deep?: boolean
  /**
   * Defining default value for return ref when no value is passed.
   *
   * @default undefined
   */
  defaultValue?: T
  /**
   * Clone the props.
   * Accepts a custom clone function.
   * When setting to `true`, it will use `JSON.parse(JSON.stringify(value))` to clone.
   *
   * @default false
   */
  clone?: boolean | CloneFn<T>
  /**
   * The hook before triggering the emit event can be used for form validation.
   * if false is returned, the emit event will not be triggered.
   *
   * @default undefined
   */
  shouldEmit?: (v: T) => boolean
}
/**
 * Shorthand for v-model binding, props + emit -> ref
 *
 * @see https://vueuse.org/useVModel
 * @param props
 * @param key (default 'modelValue')
 * @param emit
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useVModel<
  P extends object,
  K extends keyof P,
  Name extends string,
>(
  props: P,
  key?: K,
  emit?: (name: Name, ...args: any[]) => void,
  options?: UseVModelOptions<P[K], false>,
): WritableComputedRef<P[K]>
export declare function useVModel<
  P extends object,
  K extends keyof P,
  Name extends string,
>(
  props: P,
  key?: K,
  emit?: (name: Name, ...args: any[]) => void,
  options?: UseVModelOptions<P[K], true>,
): Ref<UnwrapRef<P[K]>>
```
```

## File: `skills/vueuse-functions/references/useVModels.md`
```markdown
---
category: Component
related: useVModel
---

# useVModels

Shorthand for props v-model binding. Think it like `toRefs(props)` but changes will also trigger emit.

## Usage

```ts
import { useVModels } from '@vueuse/core'

const props = defineProps({
  foo: string,
  bar: number,
})

const emit = defineEmits(['update:foo', 'update:bar'])

const { foo, bar } = useVModels(props, emit)
```

### Options API

```ts
import { useVModels } from '@vueuse/core'

export default {
  props: {
    foo: String,
    bar: Number,
  },
  setup(props, { emit }) {
    const { foo, bar } = useVModels(props, emit)

    console.log(foo.value) // props.foo
    foo.value = 'foo' // emit('update:foo', 'foo')
  },
}
```

## Type Declarations

```ts
/**
 * Shorthand for props v-model binding. Think like `toRefs(props)` but changes will also emit out.
 *
 * @see https://vueuse.org/useVModels
 * @param props
 * @param emit
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useVModels<P extends object, Name extends string>(
  props: P,
  emit?: (name: Name, ...args: any[]) => void,
  options?: UseVModelOptions<any, true>,
): ToRefs<P>
export declare function useVModels<P extends object, Name extends string>(
  props: P,
  emit?: (name: Name, ...args: any[]) => void,
  options?: UseVModelOptions<any, false>,
): ToRefs<P>
```
```

## File: `skills/vueuse-functions/references/useVibrate.md`
```markdown
---
category: Browser
---

# useVibrate

Reactive [Vibration API](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API)

Most modern mobile devices include vibration hardware, which lets software
code provides physical feedback to the user by causing the device to shake.

The Vibration API offers Web apps the ability to access this hardware,
if it exists, and does nothing if the device doesn't support it.

## Usage

Vibration is described as a pattern of on-off pulses, which may be of varying
lengths.

The pattern may consist of either a single integer describing the
number of milliseconds to vibrate, or an array of integers describing
a pattern of vibrations and pauses.

```ts
import { useVibrate } from '@vueuse/core'

// This vibrates the device for 300 ms
// then pauses for 100 ms before vibrating the device again for another 300 ms:
const { vibrate, stop, isSupported } = useVibrate({ pattern: [300, 100, 300] })

// Start the vibration, it will automatically stop when the pattern is complete:
vibrate()

// But if you want to stop it, you can:
stop()
```

## Type Declarations

```ts
export interface UseVibrateOptions
  extends ConfigurableNavigator, ConfigurableScheduler {
  /**
   *
   * Vibration Pattern
   *
   * An array of values describes alternating periods in which the
   * device is vibrating and not vibrating. Each value in the array
   * is converted to an integer, then interpreted alternately as
   * the number of milliseconds the device should vibrate and the
   * number of milliseconds it should not be vibrating
   *
   * @default []
   *
   */
  pattern?: MaybeRefOrGetter<Arrayable<number>>
  /**
   * Interval to run a persistent vibration, in ms
   *
   * Pass `0` to disable
   *
   * @deprecated Please use `scheduler` option instead
   * @default 0
   *
   */
  interval: number
}
export interface UseVibrateReturn extends Supportable {
  pattern: MaybeRefOrGetter<Arrayable<number>>
  intervalControls?: Pausable
  vibrate: (pattern?: Arrayable<number>) => void
  stop: () => void
}
/**
 * Reactive vibrate
 *
 * @see https://vueuse.org/useVibrate
 * @see https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useVibrate(
  options?: UseVibrateOptions,
): UseVibrateReturn
```
```

## File: `skills/vueuse-functions/references/useVirtualList.md`
```markdown
---
category: Component
---

# useVirtualList

::: warning
Consider using [`@tanstack/vue-virtual`](https://tanstack.com/virtual/v3/docs/framework/vue/vue-virtual) instead, if you are looking for more features.
:::

Create virtual lists with ease. Virtual lists (sometimes called [_virtual scrollers_](https://vue-virtual-scroller-demo.netlify.app/)) allow you to render a large number of items performantly. They only render the minimum number of DOM nodes necessary to show the items within the `container` element by using the `wrapper` element to emulate the container element's full height.

## Usage

### Simple list

```ts
import { useVirtualList } from '@vueuse/core'

const { list, containerProps, wrapperProps } = useVirtualList(
  Array.from(Array.from({ length: 99999 }).keys()),
  {
    // Keep `itemHeight` in sync with the item's row.
    itemHeight: 22,
  },
)
```

### Config

| State      | Type     | Description                                                                                     |
| ---------- | -------- | ----------------------------------------------------------------------------------------------- |
| itemHeight | `number` | ensure that the total height of the `wrapper` element is calculated correctly.\*                |
| itemWidth  | `number` | ensure that the total width of the `wrapper` element is calculated correctly.\*                 |
| overscan   | `number` | number of pre-rendered DOM nodes. Prevents whitespace between items if you scroll very quickly. |

\* The `itemHeight` or `itemWidth` must be kept in sync with the height of each row rendered. If you are seeing extra whitespace or jitter when scrolling to the bottom of the list, ensure the `itemHeight` or `itemWidth` is the same height as the row.

### Reactive list

```ts
import { useToggle, useVirtualList } from '@vueuse/core'
import { computed } from 'vue'

const [isEven, toggle] = useToggle()
const allItems = Array.from(Array.from({ length: 99999 }).keys())
const filteredList = computed(() => allItems.filter(i => isEven.value ? i % 2 === 0 : i % 2 === 1))

const { list, containerProps, wrapperProps } = useVirtualList(
  filteredList,
  {
    itemHeight: 22,
  },
)
```

```vue
<template>
  <p>Showing {{ isEven ? 'even' : 'odd' }} items</p>
  <button @click="toggle">
    Toggle Even/Odd
  </button>
  <div v-bind="containerProps" style="height: 300px">
    <div v-bind="wrapperProps">
      <div v-for="item in list" :key="item.index" style="height: 22px">
        Row: {{ item.data }}
      </div>
    </div>
  </div>
</template>
```

### Horizontal list

```ts
import { useVirtualList } from '@vueuse/core'

const allItems = Array.from(Array.from({ length: 99999 }).keys())

const { list, containerProps, wrapperProps } = useVirtualList(
  allItems,
  {
    itemWidth: 200,
  },
)
```

```vue
<template>
  <div v-bind="containerProps" style="height: 300px">
    <div v-bind="wrapperProps">
      <div v-for="item in list" :key="item.index" style="width: 200px">
        Row: {{ item.data }}
      </div>
    </div>
  </div>
</template>
```

## Component Usage

```vue
<template>
  <UseVirtualList :list="list" :options="options" height="300px">
    <template #default="props">
      <!-- you can get current item of list here -->
      <div style="height: 22px">
        Row {{ props.index }} {{ props.data }}
      </div>
    </template>
  </UseVirtualList>
</template>
```

To scroll to a specific element, the component exposes `scrollTo(index: number) => void`.

## Type Declarations

```ts
type UseVirtualListItemSize = number | ((index: number) => number)
export interface UseHorizontalVirtualListOptions extends UseVirtualListOptionsBase {
  /**
   * item width, accept a pixel value or a function that returns the width
   *
   * @default 0
   */
  itemWidth: UseVirtualListItemSize
}
export interface UseVerticalVirtualListOptions extends UseVirtualListOptionsBase {
  /**
   * item height, accept a pixel value or a function that returns the height
   *
   * @default 0
   */
  itemHeight: UseVirtualListItemSize
}
export interface UseVirtualListOptionsBase {
  /**
   * the extra buffer items outside of the view area
   *
   * @default 5
   */
  overscan?: number
}
export type UseVirtualListOptions =
  | UseHorizontalVirtualListOptions
  | UseVerticalVirtualListOptions
export interface UseVirtualListItem<T> {
  data: T
  index: number
}
export interface UseVirtualListReturn<T> {
  list: Ref<UseVirtualListItem<T>[]>
  scrollTo: (index: number) => void
  containerProps: {
    ref: Ref<HTMLElement | null>
    onScroll: () => void
    style: StyleValue
  }
  wrapperProps: ComputedRef<{
    style:
      | {
          width: string
          height: string
          marginTop: string
        }
      | {
          width: string
          height: string
          marginLeft: string
          display: string
        }
  }>
}
/**
 * Please consider using [`vue-virtual-scroller`](https://github.com/Akryum/vue-virtual-scroller) if you are looking for more features.
 */
export declare function useVirtualList<T = any>(
  list: MaybeRef<readonly T[]>,
  options: UseVirtualListOptions,
): UseVirtualListReturn<T>
```
```

## File: `skills/vueuse-functions/references/useWakeLock.md`
```markdown
---
category: Browser
---

# useWakeLock

Reactive [Screen Wake Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Wake_Lock_API). Provides a way to prevent devices from dimming or locking the screen when an application needs to keep running.

## Usage

```ts
import { useWakeLock } from '@vueuse/core'

const { isSupported, isActive, forceRequest, request, release } = useWakeLock()
```

When `request` is called, the wake lock will be requested if the document is visible. Otherwise, the request will be queued until the document becomes visible. If the request is successful, `isActive` will be **true**. Whenever the document is hidden, the `isActive` will be **false**.

When `release` is called, the wake lock will be released. If there is a queued request, it will be canceled.

To request a wake lock immediately, even if the document is hidden, use `forceRequest`. Note that this may throw an error if the document is hidden.

## Type Declarations

```ts
type WakeLockType = "screen"
export interface WakeLockSentinel extends EventTarget {
  type: WakeLockType
  released: boolean
  release: () => Promise<void>
}
export type UseWakeLockOptions = ConfigurableNavigator & ConfigurableDocument
export interface UseWakeLockReturn extends Supportable {
  sentinel: ShallowRef<WakeLockSentinel | null>
  isActive: ComputedRef<boolean>
  request: (type: WakeLockType) => Promise<void>
  forceRequest: (type: WakeLockType) => Promise<void>
  release: () => Promise<void>
}
/**
 * Reactive Screen Wake Lock API.
 *
 * @see https://vueuse.org/useWakeLock
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useWakeLock(
  options?: UseWakeLockOptions,
): UseWakeLockReturn
```
```

## File: `skills/vueuse-functions/references/useWebNotification.md`
```markdown
---
category: Browser
---

# useWebNotification

Reactive [Notification](https://developer.mozilla.org/en-US/docs/Web/API/notification)

The Web Notification interface of the Notifications API is used to configure and display desktop notifications to the user.

## Usage

::: tip
Before an app can send a notification, the user must grant the application the right to do so. The user's OS settings may also prevent expected notification behaviour.
:::

```ts
import { useWebNotification } from '@vueuse/core'

const {
  isSupported,
  notification,
  permissionGranted,
  show,
  close,
  onClick,
  onShow,
  onError,
  onClose,
} = useWebNotification({
  title: 'Hello, VueUse world!',
  dir: 'auto',
  lang: 'en',
  renotify: true,
  tag: 'test',
})

if (isSupported.value && permissionGranted.value)
  show()
```

This composable also utilizes the createEventHook utility from '@vueuse/shared`:

```ts
import { useWebNotification } from '@vueuse/core'

const { onClick, onShow, onError, onClose, } = useWebNotification()
// ---cut---
onClick((evt: Event) => {
  // Do something with the notification on:click event...
})

onShow((evt: Event) => {
  // Do something with the notification on:show event...
})

onError((evt: Event) => {
  // Do something with the notification on:error event...
})

onClose((evt: Event) => {
  // Do something with the notification on:close event...
})
```

## Type Declarations

```ts
export interface WebNotificationOptions {
  /**
   * The title read-only property of the Notification interface indicates
   * the title of the notification
   *
   * @default ''
   */
  title?: string
  /**
   * The body string of the notification as specified in the constructor's
   * options parameter.
   *
   * @default ''
   */
  body?: string
  /**
   * The text direction of the notification as specified in the constructor's
   * options parameter.
   *
   * @default ''
   */
  dir?: "auto" | "ltr" | "rtl"
  /**
   * The language code of the notification as specified in the constructor's
   * options parameter.
   *
   * @default DOMString
   */
  lang?: string
  /**
   * The ID of the notification(if any) as specified in the constructor's options
   * parameter.
   *
   * @default ''
   */
  tag?: string
  /**
   * The URL of the image used as an icon of the notification as specified
   * in the constructor's options parameter.
   *
   * @default ''
   */
  icon?: string
  /**
   * Specifies whether the user should be notified after a new notification
   * replaces an old one.
   *
   * @default false
   */
  renotify?: boolean
  /**
   * A boolean value indicating that a notification should remain active until the
   * user clicks or dismisses it, rather than closing automatically.
   *
   * @default false
   */
  requireInteraction?: boolean
  /**
   * The silent read-only property of the Notification interface specifies
   * whether the notification should be silent, i.e., no sounds or vibrations
   * should be issued, regardless of the device settings.
   *
   * @default false
   */
  silent?: boolean
  /**
   * Specifies a vibration pattern for devices with vibration hardware to emit.
   * A vibration pattern, as specified in the Vibration API spec
   *
   * @see https://w3c.github.io/vibration/
   */
  vibrate?: number[]
}
export interface UseWebNotificationOptions
  extends ConfigurableWindow, WebNotificationOptions {
  /**
   * Request for permissions onMounted if it's not granted.
   *
   * Can be disabled and calling `ensurePermissions` to grant afterwords.
   *
   * @default true
   */
  requestPermissions?: boolean
}
export interface UseWebNotificationReturn extends Supportable {
  notification: Ref<Notification | null>
  ensurePermissions: () => Promise<boolean | undefined>
  permissionGranted: ShallowRef<boolean>
  show: (
    overrides?: WebNotificationOptions,
  ) => Promise<Notification | undefined>
  close: () => void
  onClick: EventHookOn<Event>
  onShow: EventHookOn<Event>
  onError: EventHookOn<Event>
  onClose: EventHookOn<Event>
}
/**
 * Reactive useWebNotification
 *
 * @see https://vueuse.org/useWebNotification
 * @see https://developer.mozilla.org/en-US/docs/Web/API/notification
 */
export declare function useWebNotification(
  options?: UseWebNotificationOptions,
): UseWebNotificationReturn
```
```

## File: `skills/vueuse-functions/references/useWebSocket.md`
```markdown
---
category: Network
---

# useWebSocket

Reactive [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/WebSocket) client.

## Usage

```ts
import { useWebSocket } from '@vueuse/core'

const { status, data, send, open, close, ws } = useWebSocket('ws://websocketurl')
```

### Return Values

| Property | Type                                      | Description                          |
| -------- | ----------------------------------------- | ------------------------------------ |
| `data`   | `Ref<any>`                                | Latest received data                 |
| `status` | `Ref<'OPEN' \| 'CONNECTING' \| 'CLOSED'>` | Connection status                    |
| `ws`     | `Ref<WebSocket>`                          | WebSocket instance                   |
| `send`   | `(data, useBuffer?) => boolean`           | Send data (buffers if not connected) |
| `open`   | `() => void`                              | Open/reconnect the connection        |
| `close`  | `(code?, reason?) => void`                | Close the connection                 |

### Callbacks

```ts
const { data } = useWebSocket('ws://websocketurl', {
  onConnected(ws) {
    console.log('Connected!')
  },
  onDisconnected(ws, event) {
    console.log('Disconnected!', event.code)
  },
  onError(ws, event) {
    console.error('Error:', event)
  },
  onMessage(ws, event) {
    console.log('Message:', event.data)
  },
})
```

See the [Type Declarations](#type-declarations) for more options.

### immediate

Enable by default.

Establish the connection immediately when the composable is called.

### autoConnect

Enable by default.

If a URL is provided as a ref, when the URL changes, it will automatically reconnect to the new URL.

### autoClose

Enable by default.

This will call `close()` automatically when the `beforeunload` event is triggered or the associated effect scope is stopped.

### autoReconnect

Reconnect on errors automatically (disabled by default).

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, close } = useWebSocket('ws://websocketurl', {
  autoReconnect: true,
})
```

Or with more controls over its behavior:

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, close } = useWebSocket('ws://websocketurl', {
  autoReconnect: {
    retries: 3,
    delay: 1000,
    onFailed() {
      alert('Failed to connect WebSocket after 3 retries')
    },
  },
})
```

You can also pass a function to `delay` to calculate the delay based on the number of retries. This is useful for implementing exponential backoff:

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, close } = useWebSocket('ws://websocketurl', {
  autoReconnect: {
    retries: 5,
    // Exponential backoff: 1s, 2s, 4s, 8s, 16s
    delay: retries => Math.min(1000 * 2 ** (retries - 1), 30000),
  },
})
```

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, close } = useWebSocket('ws://websocketurl', {
  autoReconnect: {
    retries: 5,
    // Linear backoff: 1s, 2s, 3s, 4s, 5s
    delay: retries => retries * 1000,
  },
})
```

Explicitly calling `close()` won't trigger the auto reconnection.

### heartbeat

It's common practice to send a small message (heartbeat) for every given time passed to keep the connection active. In this function we provide a convenient helper to do it:

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, close } = useWebSocket('ws://websocketurl', {
  heartbeat: true,
})
```

Or with more controls:

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, close } = useWebSocket('ws://websocketurl', {
  heartbeat: {
    message: 'ping',
    scheduler: cb => useIntervalFn(cb, 2000),
    pongTimeout: 1000,
  },
})
```

### Sub-protocols

List of one or more subprotocols to use, in this case SOAP and WAMP.

```ts
import { useWebSocket } from '@vueuse/core'
// ---cut---
const { status, data, send, open, close } = useWebSocket('ws://websocketurl', {
  protocols: ['soap'], // ['soap', 'wamp']
})
```

## Type Declarations

```ts
export type WebSocketStatus = "OPEN" | "CONNECTING" | "CLOSED"
export type WebSocketHeartbeatMessage = string | ArrayBuffer | Blob
export interface UseWebSocketOptions {
  onConnected?: (ws: WebSocket) => void
  onDisconnected?: (ws: WebSocket, event: CloseEvent) => void
  onError?: (ws: WebSocket, event: Event) => void
  onMessage?: (ws: WebSocket, event: MessageEvent) => void
  /**
   * Send heartbeat for every x milliseconds passed
   *
   * @default false
   */
  heartbeat?:
    | boolean
    | (ConfigurableScheduler & {
        /**
         * Message for the heartbeat
         *
         * @default 'ping'
         */
        message?: MaybeRefOrGetter<WebSocketHeartbeatMessage>
        /**
         * Response message for the heartbeat, if undefined the message will be used
         */
        responseMessage?: MaybeRefOrGetter<WebSocketHeartbeatMessage>
        /**
         * Interval, in milliseconds
         *
         * @deprecated Please use `scheduler` option instead
         * @default 1000
         */
        interval?: number
        /**
         * Heartbeat response timeout, in milliseconds
         *
         * @default 1000
         */
        pongTimeout?: number
      })
  /**
   * Enabled auto reconnect
   *
   * @default false
   */
  autoReconnect?:
    | boolean
    | {
        /**
         * Maximum retry times.
         *
         * Or you can pass a predicate function (which returns true if you want to retry).
         *
         * @default -1
         */
        retries?: number | ((retried: number) => boolean)
        /**
         * Delay for reconnect, in milliseconds
         *
         * Or you can pass a function to calculate the delay based on the number of retries.
         *
         * @default 1000
         */
        delay?: number | ((retries: number) => number)
        /**
         * On maximum retry times reached.
         */
        onFailed?: Fn
      }
  /**
   * Immediately open the connection when calling this composable
   *
   * @default true
   */
  immediate?: boolean
  /**
   * Automatically connect to the websocket when URL changes
   *
   * @default true
   */
  autoConnect?: boolean
  /**
   * Automatically close a connection
   *
   * @default true
   */
  autoClose?: boolean
  /**
   * List of one or more sub-protocol strings
   *
   * @default []
   */
  protocols?: string[]
}
export interface UseWebSocketReturn<T> {
  /**
   * Reference to the latest data received via the websocket,
   * can be watched to respond to incoming messages
   */
  data: Ref<T | null>
  /**
   * The current websocket status, can be only one of:
   * 'OPEN', 'CONNECTING', 'CLOSED'
   */
  status: ShallowRef<WebSocketStatus>
  /**
   * Closes the websocket connection gracefully.
   */
  close: WebSocket["close"]
  /**
   * Reopen the websocket connection.
   * If there the current one is active, will close it before opening a new one.
   */
  open: Fn
  /**
   * Sends data through the websocket connection.
   *
   * @param data
   * @param useBuffer when the socket is not yet open, store the data into the buffer and sent them one connected. Default to true.
   */
  send: (data: string | ArrayBuffer | Blob, useBuffer?: boolean) => boolean
  /**
   * Reference to the WebSocket instance.
   */
  ws: Ref<WebSocket | undefined>
}
/**
 * Reactive WebSocket client.
 *
 * @see https://vueuse.org/useWebSocket
 * @param url
 */
export declare function useWebSocket<Data = any>(
  url: MaybeRefOrGetter<string | URL | undefined>,
  options?: UseWebSocketOptions,
): UseWebSocketReturn<Data>
```
```

## File: `skills/vueuse-functions/references/useWebWorker.md`
```markdown
---
category: Browser
related: useWebWorkerFn
---

# useWebWorker

Simple [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) registration and communication.

## Usage

```ts
import { useWebWorker } from '@vueuse/core'

const { data, post, terminate, worker } = useWebWorker('/path/to/worker.js')
```

| State  | Type                              | Description                                                                                          |
| ------ | --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| data   | `Ref<any>`                        | Reference to the latest data received via the worker, can be watched to respond to incoming messages |
| worker | `ShallowRef<Worker \| undefined>` | Reference to the instance of the WebWorker                                                           |

| Method    | Signature                                                                                                                     | Description                      |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| post      | `(message: any, transfer: Transferable[]): void`<br>`(message: any, options?: StructuredSerializeOptions \| undefined): void` | Sends data to the worker thread. |
| terminate | `() => void`                                                                                                                  | Stops and terminates the worker. |

## Type Declarations

```ts
type PostMessage = (typeof Worker.prototype)["postMessage"]
export interface UseWebWorkerReturn<Data = any> {
  data: Ref<Data>
  post: PostMessage
  terminate: () => void
  worker: ShallowRef<Worker | undefined>
}
type WorkerFn = (...args: unknown[]) => Worker
/**
 * Simple Web Workers registration and communication.
 *
 * @see https://vueuse.org/useWebWorker
 * @param url
 * @param workerOptions
 * @param options
 */
export declare function useWebWorker<T = any>(
  url: string,
  workerOptions?: WorkerOptions,
  options?: ConfigurableWindow,
): UseWebWorkerReturn<T>
/**
 * Simple Web Workers registration and communication.
 *
 * @see https://vueuse.org/useWebWorker
 */
export declare function useWebWorker<T = any>(
  worker: Worker | WorkerFn,
): UseWebWorkerReturn<T>
```
```

## File: `skills/vueuse-functions/references/useWebWorkerFn.md`
```markdown
---
category: Browser
---

# useWebWorkerFn

Run expensive functions without blocking the UI, using a simple syntax that makes use of Promise. A port of [alewin/useWorker](https://github.com/alewin/useWorker).

## Usage

### Basic example

```ts
import { useWebWorkerFn } from '@vueuse/core'

const { workerFn } = useWebWorkerFn(() => {
  // some heavy works to do in web worker
})
```

### With dependencies

```ts {7-9}
import { useWebWorkerFn } from '@vueuse/core'

const { workerFn, workerStatus, workerTerminate } = useWebWorkerFn(
  dates => dates.sort(dateFns.compareAsc),
  {
    timeout: 50000,
    dependencies: [
      'https://cdnjs.cloudflare.com/ajax/libs/date-fns/1.30.1/date_fns.js', // dateFns
    ],
  },
)
```

### With local dependencies

```ts {9-9}
import { useWebWorkerFn } from '@vueuse/core'

const pow = (a: number) => a * a

const { workerFn, workerStatus, workerTerminate } = useWebWorkerFn(
  numbers => pow(numbers),
  {
    timeout: 50000,
    localDependencies: [pow]
  },
)
```

## Web Worker

Before you start using this function, we suggest you read the [Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) documentation.

## Credit

This function is a Vue port of https://github.com/alewin/useWorker by Alessio Koci, with the help of [@Donskelle](https://github.com/Donskelle) to migration.

## Type Declarations

```ts
export type WebWorkerStatus =
  | "PENDING"
  | "SUCCESS"
  | "RUNNING"
  | "ERROR"
  | "TIMEOUT_EXPIRED"
export interface UseWebWorkerOptions extends ConfigurableWindow {
  /**
   * Number of milliseconds before killing the worker
   *
   * @default undefined
   */
  timeout?: number
  /**
   * An array that contains the external dependencies needed to run the worker
   */
  dependencies?: string[]
  /**
   * An array that contains the local dependencies needed to run the worker
   */
  localDependencies?: Function[]
}
export interface UseWebWorkerFnReturn<T extends (...fnArgs: any[]) => any> {
  workerFn: (...fnArgs: Parameters<T>) => Promise<ReturnType<T>>
  workerStatus: ShallowRef<WebWorkerStatus>
  workerTerminate: (status?: WebWorkerStatus) => void
}
/**
 * Run expensive function without blocking the UI, using a simple syntax that makes use of Promise.
 *
 * @see https://vueuse.org/useWebWorkerFn
 * @param fn
 * @param options
 */
export declare function useWebWorkerFn<T extends (...fnArgs: any[]) => any>(
  fn: T,
  options?: UseWebWorkerOptions,
): UseWebWorkerFnReturn<T>
```
```

## File: `skills/vueuse-functions/references/useWindowFocus.md`
```markdown
---
category: Elements
---

# useWindowFocus

Reactively track window focus with `window.onfocus` and `window.onblur` events.

## Usage

```vue
<script setup lang="ts">
import { useWindowFocus } from '@vueuse/core'

const focused = useWindowFocus()
</script>

<template>
  <div>{{ focused }}</div>
</template>
```

## Component Usage

```vue
<template>
  <UseWindowFocus v-slot="{ focused }">
    Document Focus: {{ focused }}
  </UseWindowFocus>
</template>
```

## Type Declarations

```ts
/**
 * Reactively track window focus with `window.onfocus` and `window.onblur`.
 *
 * @see https://vueuse.org/useWindowFocus
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useWindowFocus(
  options?: ConfigurableWindow,
): ShallowRef<boolean>
```
```

## File: `skills/vueuse-functions/references/useWindowScroll.md`
```markdown
---
category: Elements
---

# useWindowScroll

Reactive window scroll

## Usage

```vue
<script setup lang="ts">
import { useWindowScroll } from '@vueuse/core'

const { x, y } = useWindowScroll()
</script>

<template>
  <div>
    read current x, y scroll: {{ x }}, {{ y }}
  </div>
  <button @click="x = 100">
    scroll X to 100
  </button>
  <button @click="y = 100">
    scroll Y to 100
  </button>
</template>
```

## Type Declarations

```ts
export interface UseWindowScrollOptions
  extends ConfigurableWindow, UseScrollOptions {}
export interface UseWindowScrollReturn extends UseScrollReturn {}
/**
 * Reactive window scroll.
 *
 * @see https://vueuse.org/useWindowScroll
 * @param options
 */
export declare function useWindowScroll(
  options?: UseWindowScrollOptions,
): UseWindowScrollReturn
```
```

## File: `skills/vueuse-functions/references/useWindowSize.md`
```markdown
---
category: Elements
---

# useWindowSize

Reactive window size

## Usage

```vue
<script setup lang="ts">
import { useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()
</script>

<template>
  <div>
    Width: {{ width }}
    Height: {{ height }}
  </div>
</template>
```

## Component Usage

```vue
<template>
  <UseWindowSize v-slot="{ width, height }">
    Width: {{ width }}
    Height: {{ height }}
  </UseWindowSize>
</template>
```

## Type Declarations

```ts
export interface UseWindowSizeOptions extends ConfigurableWindow {
  initialWidth?: number
  initialHeight?: number
  /**
   * Listen to window `orientationchange` event
   *
   * @default true
   */
  listenOrientation?: boolean
  /**
   * Whether the scrollbar should be included in the width and height
   * Only effective when `type` is `'inner'`
   *
   * @default true
   */
  includeScrollbar?: boolean
  /**
   * Use `window.innerWidth` or `window.outerWidth` or `window.visualViewport`
   * visualViewport documentation from MDN(https://developer.mozilla.org/zh-CN/docs/Web/API/VisualViewport)
   * @default 'inner'
   */
  type?: "inner" | "outer" | "visual"
}
export interface UseWindowSizeReturn {
  width: ShallowRef<number>
  height: ShallowRef<number>
}
/**
 * Reactive window size.
 *
 * @see https://vueuse.org/useWindowSize
 * @param options
 *
 * @__NO_SIDE_EFFECTS__
 */
export declare function useWindowSize(
  options?: UseWindowSizeOptions,
): UseWindowSizeReturn
```
```

## File: `skills/vueuse-functions/references/useZoomFactor.md`
```markdown
---
category: '@Electron'
---

# useZoomFactor

Reactive [WebFrame](https://www.electronjs.org/docs/api/web-frame#webframe) zoom factor.

## Usage

```ts
import { useZoomFactor } from '@vueuse/electron'

// enable nodeIntegration if you don't provide webFrame explicitly
// see: https://www.electronjs.org/docs/api/webview-tag#nodeintegration
// Ref result will return
const factor = useZoomFactor()
console.log(factor.value) // print current zoom factor
factor.value = 2 // change current zoom factor
```

Set initial zoom factor immediately

```ts
import { useZoomFactor } from '@vueuse/electron'

const factor = useZoomFactor(2)
```

Pass a `ref` and the factor will be updated when the source ref changes

```ts
import { useZoomFactor } from '@vueuse/electron'
import { shallowRef } from 'vue'

const factor = shallowRef(1)

useZoomFactor(factor) // zoom factor will match with the ref

factor.value = 2 // zoom factor will change
```

## Type Declarations

```ts
export declare function useZoomFactor(factor: MaybeRef<number>): Ref<number>
export declare function useZoomFactor(
  webFrame: WebFrame,
  factor: MaybeRef<number>,
): Ref<number>
export declare function useZoomFactor(webFrame: WebFrame): Ref<number>
export declare function useZoomFactor(): Ref<number>
```
```

## File: `skills/vueuse-functions/references/useZoomLevel.md`
```markdown
---
category: '@Electron'
---

# useZoomLevel

Reactive [WebFrame](https://www.electronjs.org/docs/api/web-frame#webframe) zoom level.

## Usage

```ts
import { useZoomLevel } from '@vueuse/electron'

// enable nodeIntegration if you don't provide webFrame explicitly
// see: https://www.electronjs.org/docs/api/webview-tag#nodeintegration
// Ref result will return
const level = useZoomLevel()
console.log(level.value) // print current zoom level
level.value = 2 // change current zoom level
```

Set initial zoom level immediately

```ts
import { useZoomLevel } from '@vueuse/electron'

const level = useZoomLevel(2)
```

Pass a `ref` and the level will be updated when the source ref changes

```ts
import { useZoomLevel } from '@vueuse/electron'
import { shallowRef } from 'vue'

const level = shallowRef(1)

useZoomLevel(level) // zoom level will match with the ref

level.value = 2 // zoom level will change
```

## Type Declarations

```ts
export declare function useZoomLevel(level: MaybeRef<number>): Ref<number>
export declare function useZoomLevel(
  webFrame: WebFrame,
  level: MaybeRef<number>,
): Ref<number>
export declare function useZoomLevel(webFrame: WebFrame): Ref<number>
export declare function useZoomLevel(): Ref<number>
```
```

## File: `skills/vueuse-functions/references/watchArray.md`
```markdown
---
category: Watch
---

# watchArray

Watch for an array with additions and removals.

## Usage

Similar to `watch`, but provides the added and removed elements to the callback function. Pass `{ deep: true }` if the list is updated in place with `push`, `splice`, etc.

```ts
import { watchArray } from '@vueuse/core'

const list = ref([1, 2, 3])

watchArray(list, (newList, oldList, added, removed) => {
  console.log(newList) // [1, 2, 3, 4]
  console.log(oldList) // [1, 2, 3]
  console.log(added) // [4]
  console.log(removed) // []
})

onMounted(() => {
  list.value = [...list.value, 4]
})
```

## Type Declarations

```ts
export declare type WatchArrayCallback<V = any, OV = any> = (
  value: V,
  oldValue: OV,
  added: V,
  removed: OV,
  onCleanup: (cleanupFn: () => void) => void,
) => any
/**
 * Watch for an array with additions and removals.
 *
 * @see https://vueuse.org/watchArray
 */
export declare function watchArray<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T[]> | T[],
  cb: WatchArrayCallback<T[], Immediate extends true ? T[] | undefined : T[]>,
  options?: WatchOptions<Immediate>,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/watchAtMost.md`
```markdown
---
category: Watch
---

# watchAtMost

`watch` with the number of times triggered.

## Usage

Similar to `watch` with an extra option `count` which set up the number of times the callback function is triggered. After the count is reached, the watch will be stopped automatically.

```ts
import { watchAtMost } from '@vueuse/core'

watchAtMost(
  source,
  () => { console.log('trigger!') }, // triggered it at most 3 times
  {
    count: 3, // the number of times triggered
  },
)
```

## Type Declarations

```ts
export interface WatchAtMostOptions<
  Immediate,
> extends WatchWithFilterOptions<Immediate> {
  count: MaybeRefOrGetter<number>
}
export interface WatchAtMostReturn {
  stop: WatchStopHandle
  pause: () => void
  resume: () => void
  count: ShallowRef<number>
}
export declare function watchAtMost<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options: WatchAtMostOptions<Immediate>,
): WatchAtMostReturn
export declare function watchAtMost<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  sources: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options: WatchAtMostOptions<Immediate>,
): WatchAtMostReturn
```
```

## File: `skills/vueuse-functions/references/watchDebounced.md`
```markdown
---
category: Watch
alias: debouncedWatch
---

# watchDebounced

Debounced watch. The callback will only be invoked after the source stops changing for the specified duration.

## Usage

Similar to `watch`, but offering extra options `debounce` and `maxWait` which will be applied to the callback function.

```ts
import { watchDebounced } from '@vueuse/core'

watchDebounced(
  source,
  () => { console.log('changed!') },
  { debounce: 500, maxWait: 1000 },
)
```

### Options

| Option     | Type                       | Default | Description                                |
| ---------- | -------------------------- | ------- | ------------------------------------------ |
| `debounce` | `MaybeRefOrGetter<number>` | `0`     | Debounce delay in ms (can be reactive)     |
| `maxWait`  | `MaybeRefOrGetter<number>` | —       | Maximum wait time before forced invocation |

All standard `watch` options (`deep`, `immediate`, `flush`, etc.) are also supported.

### Reactive Debounce Time

The debounce time can be reactive:

```ts
import { watchDebounced } from '@vueuse/core'

const debounceMs = ref(500)

watchDebounced(
  source,
  () => { console.log('changed!') },
  { debounce: debounceMs },
)

// Later, change the debounce time
debounceMs.value = 1000
```

## How It Works

It's essentially a shorthand for the following code:

```ts
import { debounceFilter, watchWithFilter } from '@vueuse/core'

watchWithFilter(
  source,
  () => { console.log('changed!') },
  {
    eventFilter: debounceFilter(500, { maxWait: 1000 }),
  },
)
```

## Type Declarations

```ts
export interface WatchDebouncedOptions<Immediate>
  extends WatchOptions<Immediate>, DebounceFilterOptions {
  debounce?: MaybeRefOrGetter<number>
}
export declare function watchDebounced<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options?: WatchDebouncedOptions<Immediate>,
): WatchHandle
export declare function watchDebounced<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchDebouncedOptions<Immediate>,
): WatchHandle
export declare function watchDebounced<
  T extends object,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchDebouncedOptions<Immediate>,
): WatchHandle
/** @deprecated use `watchDebounced` instead */
export declare const debouncedWatch: typeof watchDebounced
```
```

## File: `skills/vueuse-functions/references/watchDeep.md`
```markdown
---
category: Watch
---

# watchDeep

Shorthand for watching value with `{deep: true}`

## Usage

Similar to `watch`, but with `{ deep: true }`

```ts
import { watchDeep } from '@vueuse/core'

const nestedObject = ref({ foo: { bar: { deep: 5 } } })

watchDeep(nestedObject, (updated) => {
  console.log(updated)
})

onMounted(() => {
  nestedObject.value.foo.bar.deep = 10
})
```

## Type Declarations

```ts
export declare function watchDeep<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  source: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options?: Omit<WatchOptions<Immediate>, "deep">,
): WatchHandle
export declare function watchDeep<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: Omit<WatchOptions<Immediate>, "deep">,
): WatchHandle
export declare function watchDeep<
  T extends object,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: Omit<WatchOptions<Immediate>, "deep">,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/watchExtractedObservable.md`
```markdown
---
category: '@RxJS'
---

# watchExtractedObservable

Watch the values of an RxJS [`Observable`](https://rxjs.dev/guide/observable) as extracted from one or more composables.

Automatically unsubscribe on observable change, and automatically unsubscribe from it when the component is unmounted.

Supports all overloads of [`watch`](https://vuejs.org/guide/essentials/watchers.html#basic-example).

## Usage

<!-- TODO: import rxjs error if enable twoslash -->

```ts no-twoslash
import { watchExtractedObservable } from '@vueuse/rxjs'
import { computed, reactive, useTemplateRef } from 'vue'
import { AudioPlayer } from '../my/libs/AudioPlayer'

// setup()

const audio = useTemplateRef('audio')
const player = computed(() => (audio.value ? new AudioPlayer(audio.value) : null))
const state = reactive({
  progress: 0,
})

watchExtractedObservable(player, p => p.progress$, (percentage) => {
  state.progress = percentage * 100
})
```

If you want to add custom error handling to an `Observable` that might error, you can supply an optional `onError` configuration. Without this, RxJS will treat any error in the supplied `Observable` as an "unhandled error" and it will be thrown in a new call stack and reported to `window.onerror` (or `process.on('error')` if you happen to be in Node).

You can also supply an optional `onComplete` configuration if you need to attach special behavior when the watched observable completes.

```ts no-twoslash
import { watchExtractedObservable } from '@vueuse/rxjs'
import { computed, reactive, useTemplateRef } from 'vue'
import { AudioPlayer } from '../my/libs/AudioPlayer'

// setup()

const audio = useTemplateRef('audio')
const player = computed(() => (audio.value ? new AudioPlayer(audio.value) : null))
const state = reactive({
  progress: 0,
})

watchExtractedObservable(player, p => p.progress$, (percentage) => {
  state.progress = percentage * 100
}, {
  onError: (err: unknown) => {
    console.error(err)
  },
  onComplete: () => {
    state.progress = 100 // or 0, or whatever
  },
})
```

If you want, you can also pass `watch` options as the last argument:

```ts no-twoslash
import { watchExtractedObservable } from '@vueuse/rxjs'
import { computed, reactive, useTemplateRef } from 'vue'
import { AudioPlayer } from '../my/libs/AudioPlayer'

// setup()

const audio = useTemplateRef('audio')
const player = computed(() => (audio.value ? new AudioPlayer(audio.value) : null))
const state = reactive({
  progress: 0,
})

watchExtractedObservable(player, p => p.progress$, (percentage) => {
  state.progress = percentage * 100
}, {
  onError: (err: unknown) => {
    console.error(err)
  }
}, {
  immediate: true
})
```

## Subscription Options

| Option       | Type                     | Description                          |
| ------------ | ------------------------ | ------------------------------------ |
| `onError`    | `(err: unknown) => void` | Error handler for Observable errors  |
| `onComplete` | `() => void`             | Called when the Observable completes |

## Return Value

Returns a `WatchHandle` that can be used to stop watching:

```ts no-twoslash
import { watchExtractedObservable } from '@vueuse/rxjs'
import { ref } from 'vue'

const source = ref({ data$: null })

const stop = watchExtractedObservable(source, s => s.data$, (data) => {
  console.log(data)
})

// Later, stop watching
stop()
```

## Type Declarations

```ts
export type OnCleanup = (cleanupFn: () => void) => void
export type WatchExtractedObservableCallback<
  Value,
  OldValue,
  ObservableElement,
> = (
  value: NonNullable<Value>,
  oldValue: OldValue,
  onCleanup: OnCleanup,
) => Observable<ObservableElement>
export interface WatchExtractedObservableOptions {
  onError?: (err: unknown) => void
  onComplete?: () => void
}
export declare function watchExtractedObservable<
  T extends MultiWatchSources,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  extractor: WatchExtractedObservableCallback<
    MapSources<T>,
    MapOldSources<T, Immediate>,
    E
  >,
  callback: (snapshot: E) => void,
  subscriptionOptions?: WatchExtractedObservableOptions,
  watchOptions?: WatchOptions<Immediate>,
): WatchHandle
export declare function watchExtractedObservable<
  T extends Readonly<MultiWatchSources>,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  extractor: WatchExtractedObservableCallback<
    MapSources<T>,
    MapOldSources<T, Immediate>,
    E
  >,
  callback: (snapshot: E) => void,
  subscriptionOptions?: WatchExtractedObservableOptions,
  watchOptions?: WatchOptions<Immediate>,
): WatchHandle
export declare function watchExtractedObservable<
  T,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  extractor: WatchExtractedObservableCallback<
    T,
    Immediate extends true ? T | undefined : T,
    E
  >,
  callback: (snapshot: E) => void,
  subscriptionOptions?: WatchExtractedObservableOptions,
  watchOptions?: WatchOptions<Immediate>,
): WatchHandle
export declare function watchExtractedObservable<
  T extends object,
  E,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  extractor: WatchExtractedObservableCallback<
    T,
    Immediate extends true ? T | undefined : T,
    E
  >,
  callback: (snapshot: E) => void,
  subscriptionOptions?: WatchExtractedObservableOptions,
  watchOptions?: WatchOptions<Immediate>,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/watchIgnorable.md`
```markdown
---
category: Watch
alias: ignorableWatch
---

# watchIgnorable

Ignorable watch

## Usage

Extended `watch` that returns extra `ignoreUpdates(updater)` and `ignorePrevAsyncUpdates()` to ignore particular updates to the source.

```ts
import { watchIgnorable } from '@vueuse/core'
import { nextTick, shallowRef } from 'vue'

const source = shallowRef('foo')

const { stop, ignoreUpdates } = watchIgnorable(
  source,
  v => console.log(`Changed to ${v}!`),
)

source.value = 'bar'
await nextTick() // logs: Changed to bar!

ignoreUpdates(() => {
  source.value = 'foobar'
})
await nextTick() // (nothing happened)

source.value = 'hello'
await nextTick() // logs: Changed to hello!

ignoreUpdates(() => {
  source.value = 'ignored'
})
source.value = 'logged'

await nextTick() // logs: Changed to logged!
```

## WatchOptionFlush timing

`watchIgnorable` accepts the same options as `watch` and uses the same defaults.
So, by default the composable works using `flush: 'pre'`.

## `ignorePrevAsyncUpdates`

This feature is only for async flush `'pre'` and `'post'`. If `flush: 'sync'` is used, `ignorePrevAsyncUpdates()` is a no-op as the watch will trigger immediately after each update to the source. It is still provided for sync flush so the code can be more generic.

```ts
import { watchIgnorable } from '@vueuse/core'
import { nextTick, shallowRef } from 'vue'

const source = shallowRef('foo')

const { ignorePrevAsyncUpdates } = watchIgnorable(
  source,
  v => console.log(`Changed to ${v}!`),
)

source.value = 'bar'
await nextTick() // logs: Changed to bar!

source.value = 'good'
source.value = 'by'
ignorePrevAsyncUpdates()

await nextTick() // (nothing happened)

source.value = 'prev'
ignorePrevAsyncUpdates()
source.value = 'after'

await nextTick() // logs: Changed to after!
```

## Recommended Readings

- [Ignorable Watch](https://patak.dev/vue/ignorable-watch.html) - by [@patak-dev](https://github.com/patak-dev)

## Type Declarations

```ts
export type IgnoredUpdater = (updater: () => void) => void
export type IgnoredPrevAsyncUpdates = () => void
export interface WatchIgnorableReturn {
  ignoreUpdates: IgnoredUpdater
  ignorePrevAsyncUpdates: IgnoredPrevAsyncUpdates
  stop: WatchStopHandle
}
export declare function watchIgnorable<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options?: WatchWithFilterOptions<Immediate>,
): WatchIgnorableReturn
export declare function watchIgnorable<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchWithFilterOptions<Immediate>,
): WatchIgnorableReturn
export declare function watchIgnorable<
  T extends object,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchWithFilterOptions<Immediate>,
): WatchIgnorableReturn
/** @deprecated use `watchIgnorable` instead */
export declare const ignorableWatch: typeof watchIgnorable
```
```

## File: `skills/vueuse-functions/references/watchImmediate.md`
```markdown
---
category: Watch
---

# watchImmediate

Shorthand for watching value with `{immediate: true}`

## Usage

Similar to `watch`, but with `{ immediate: true }`

```ts
import { watchImmediate } from '@vueuse/core'

const obj = ref('vue-use')

// changing the value from some external store/composables
obj.value = 'VueUse'

watchImmediate(obj, (updated) => {
  console.log(updated) // Console.log will be logged twice
})
```

## Type Declarations

```ts
export declare function watchImmediate<T extends Readonly<MultiWatchSources>>(
  source: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, true>>,
  options?: Omit<WatchOptions<true>, "immediate">,
): WatchHandle
export declare function watchImmediate<T>(
  source: WatchSource<T>,
  cb: WatchCallback<T, T | undefined>,
  options?: Omit<WatchOptions<true>, "immediate">,
): WatchHandle
export declare function watchImmediate<T extends object>(
  source: T,
  cb: WatchCallback<T, T | undefined>,
  options?: Omit<WatchOptions<true>, "immediate">,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/watchOnce.md`
```markdown
---
category: Watch
---

# watchOnce

Shorthand for watching value with `{ once: true }`. Once the callback fires once, the watcher will be stopped.
See [Vue's docs](https://vuejs.org/guide/essentials/watchers.html#once-watchers) for full details.

## Usage

Similar to `watch`, but with `{ once: true }`

```ts
import { watchOnce } from '@vueuse/core'

watchOnce(source, () => {
  // triggers only once
  console.log('source changed!')
})
```

## Type Declarations

```ts
export declare function watchOnce<T extends Readonly<MultiWatchSources>>(
  source: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, true>>,
  options?: Omit<WatchOptions<true>, "once">,
): WatchHandle
export declare function watchOnce<T>(
  source: WatchSource<T>,
  cb: WatchCallback<T, T | undefined>,
  options?: Omit<WatchOptions<true>, "once">,
): WatchHandle
export declare function watchOnce<T extends object>(
  source: T,
  cb: WatchCallback<T, T | undefined>,
  options?: Omit<WatchOptions<true>, "once">,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/watchPausable.md`
```markdown
---
category: Watch
alias: pausableWatch
---

# watchPausable

Pausable watch

::: info
This function will be removed in future version.
:::

::: tip

[Pausable Watcher](https://vuejs.org/api/reactivity-core.html#watch) has been added to Vue [since 3.5](https://github.com/vuejs/core/pull/9651), use `const { stop, pause, resume } = watch(watchSource, callback)` instead.

:::

## Usage

Use as normal the `watch`, but return extra `pause()` and `resume()` functions to control.

```ts
import { watchPausable } from '@vueuse/core'
import { nextTick, shallowRef } from 'vue'

const source = shallowRef('foo')

const { stop, pause, resume } = watchPausable(
  source,
  v => console.log(`Changed to ${v}!`),
)

source.value = 'bar'
await nextTick() // Changed to bar!

pause()

source.value = 'foobar'
await nextTick() // (nothing happend)

resume()

source.value = 'hello'
await nextTick() // Changed to hello!
```

## Type Declarations

```ts
export interface WatchPausableReturn extends Pausable {
  stop: WatchStopHandle
}
export type WatchPausableOptions<Immediate> =
  WatchWithFilterOptions<Immediate> & PausableFilterOptions
/** @deprecated Use Vue's built-in `watch` instead. This function will be removed in future version. */
export declare function watchPausable<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options?: WatchPausableOptions<Immediate>,
): WatchPausableReturn
/** @deprecated Use Vue's built-in `watch` instead. This function will be removed in future version. */
export declare function watchPausable<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchPausableOptions<Immediate>,
): WatchPausableReturn
/** @deprecated Use Vue's built-in `watch` instead. This function will be removed in future version. */
export declare function watchPausable<
  T extends object,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchPausableOptions<Immediate>,
): WatchPausableReturn
/** @deprecated Use Vue's built-in `watch` instead. This function will be removed in future version. */
export declare const pausableWatch: typeof watchPausable
```
```

## File: `skills/vueuse-functions/references/watchThrottled.md`
```markdown
---
category: Watch
alias: throttledWatch
---

# watchThrottled

Throttled watch. The callback will be invoked at most once per specified duration.

## Usage

Similar to `watch`, but offering extra options `throttle`, `trailing`, and `leading` which will be applied to the callback function.

```ts
import { watchThrottled } from '@vueuse/core'

watchThrottled(
  source,
  () => { console.log('changed!') },
  { throttle: 500 },
)
```

### Options

| Option     | Type                       | Default | Description                               |
| ---------- | -------------------------- | ------- | ----------------------------------------- |
| `throttle` | `MaybeRefOrGetter<number>` | `0`     | Throttle interval in ms (can be reactive) |
| `trailing` | `boolean`                  | `true`  | Invoke on the trailing edge               |
| `leading`  | `boolean`                  | `true`  | Invoke on the leading edge                |

All standard `watch` options (`deep`, `immediate`, `flush`, etc.) are also supported.

### Leading and Trailing

Control when the callback is invoked:

```ts
import { watchThrottled } from '@vueuse/core'

// Only invoke at the start of each throttle period
watchThrottled(source, callback, {
  throttle: 500,
  leading: true,
  trailing: false,
})

// Only invoke at the end of each throttle period
watchThrottled(source, callback, {
  throttle: 500,
  leading: false,
  trailing: true,
})
```

## How It Works

It's essentially a shorthand for the following code:

```ts
import { throttleFilter, watchWithFilter } from '@vueuse/core'

watchWithFilter(
  source,
  () => { console.log('changed!') },
  {
    eventFilter: throttleFilter(500),
  },
)
```

## Type Declarations

```ts
export interface WatchThrottledOptions<
  Immediate,
> extends WatchOptions<Immediate> {
  throttle?: MaybeRefOrGetter<number>
  trailing?: boolean
  leading?: boolean
}
export declare function watchThrottled<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options?: WatchThrottledOptions<Immediate>,
): WatchHandle
export declare function watchThrottled<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchThrottledOptions<Immediate>,
): WatchHandle
export declare function watchThrottled<
  T extends object,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchThrottledOptions<Immediate>,
): WatchHandle
/** @deprecated use `watchThrottled` instead */
export declare const throttledWatch: typeof watchThrottled
```
```

## File: `skills/vueuse-functions/references/watchTriggerable.md`
```markdown
---
category: Watch
---

# watchTriggerable

Watch that can be triggered manually

## Usage

A `watch` wrapper that supports manual triggering of `WatchCallback`, which returns an additional `trigger` to execute a `WatchCallback` immediately.

```ts
import { watchTriggerable } from '@vueuse/core'
import { nextTick, shallowRef } from 'vue'

const source = shallowRef(0)

const { trigger, ignoreUpdates } = watchTriggerable(
  source,
  v => console.log(`Changed to ${v}!`),
)

source.value = 'bar'
await nextTick() // logs: Changed to bar!

// Execution of WatchCallback via `trigger` does not require waiting
trigger() // logs: Changed to bar!
```

### `onCleanup`

When you want to manually call a `watch` that uses the onCleanup parameter; simply taking the `WatchCallback` out and calling it doesn't make it easy to implement the `onCleanup` parameter.

Using `watchTriggerable` will solve this problem.

```ts
import { watchTriggerable } from '@vueuse/core'
import { shallowRef } from 'vue'

const source = shallowRef(0)

const { trigger } = watchTriggerable(
  source,
  async (v, _, onCleanup) => {
    let canceled = false
    onCleanup(() => canceled = true)

    await new Promise(resolve => setTimeout(resolve, 500))
    if (canceled)
      return

    console.log(`The value is "${v}"\n`)
  },
)

source.value = 1 // no log
await trigger() // logs (after 500 ms): The value is "1"
```

## Type Declarations

```ts
export interface WatchTriggerableReturn<
  FnReturnT = void,
> extends WatchIgnorableReturn {
  /** Execute `WatchCallback` immediately */
  trigger: () => FnReturnT
}
type OnCleanup = (cleanupFn: () => void) => void
export type WatchTriggerableCallback<V = any, OV = any, R = void> = (
  value: V,
  oldValue: OV,
  onCleanup: OnCleanup,
) => R
export declare function watchTriggerable<
  T extends Readonly<MultiWatchSources>,
  FnReturnT,
>(
  sources: [...T],
  cb: WatchTriggerableCallback<
    MapSources<T>,
    MapOldSources<T, true>,
    FnReturnT
  >,
  options?: WatchWithFilterOptions<boolean>,
): WatchTriggerableReturn<FnReturnT>
export declare function watchTriggerable<T, FnReturnT>(
  source: WatchSource<T>,
  cb: WatchTriggerableCallback<T, T | undefined, FnReturnT>,
  options?: WatchWithFilterOptions<boolean>,
): WatchTriggerableReturn<FnReturnT>
export declare function watchTriggerable<T extends object, FnReturnT>(
  source: T,
  cb: WatchTriggerableCallback<T, T | undefined, FnReturnT>,
  options?: WatchWithFilterOptions<boolean>,
): WatchTriggerableReturn<FnReturnT>
```
```

## File: `skills/vueuse-functions/references/watchWithFilter.md`
```markdown
---
category: Watch
---

# watchWithFilter

`watch` with additional EventFilter control.

## Usage

Similar to `watch`, but offering an extra option `eventFilter` which will be applied to the callback function.

```ts
import { debounceFilter, watchWithFilter } from '@vueuse/core'

watchWithFilter(
  source,
  () => { console.log('changed!') }, // callback will be called in 500ms debounced manner
  {
    eventFilter: debounceFilter(500), // throttledFilter, pausableFilter or custom filters
  },
)
```

## Type Declarations

```ts
export interface WatchWithFilterOptions<Immediate>
  extends WatchOptions<Immediate>, ConfigurableEventFilter {}
export declare function watchWithFilter<
  T extends Readonly<MultiWatchSources>,
  Immediate extends Readonly<boolean> = false,
>(
  sources: [...T],
  cb: WatchCallback<MapSources<T>, MapOldSources<T, Immediate>>,
  options?: WatchWithFilterOptions<Immediate>,
): WatchHandle
export declare function watchWithFilter<
  T,
  Immediate extends Readonly<boolean> = false,
>(
  source: WatchSource<T>,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchWithFilterOptions<Immediate>,
): WatchHandle
export declare function watchWithFilter<
  T extends object,
  Immediate extends Readonly<boolean> = false,
>(
  source: T,
  cb: WatchCallback<T, Immediate extends true ? T | undefined : T>,
  options?: WatchWithFilterOptions<Immediate>,
): WatchHandle
```
```

## File: `skills/vueuse-functions/references/whenever.md`
```markdown
---
category: Watch
---

# whenever

Shorthand for watching value to be truthy.

## Usage

```js
import { useAsyncState, whenever } from '@vueuse/core'

const { state, isReady } = useAsyncState(
  fetch('https://jsonplaceholder.typicode.com/todos/1').then(t => t.json()),
  {},
)

whenever(isReady, () => console.log(state))
```

```ts
import { whenever } from '@vueuse/core'
// ---cut---
// this
whenever(ready, () => console.log(state))

// is equivalent to:
watch(ready, (isReady) => {
  if (isReady)
    console.log(state)
})
```

### Callback Function

Same as `watch`, the callback will be called with `cb(value, oldValue, onInvalidate)`.

```ts
import { whenever } from '@vueuse/core'
// ---cut---
whenever(height, (current, lastHeight) => {
  if (current > lastHeight)
    console.log(`Increasing height by ${current - lastHeight}`)
})
```

### Computed

Same as `watch`, you can pass a getter function to calculate on each change.

```ts
import { whenever } from '@vueuse/core'
// ---cut---
// this
whenever(
  () => counter.value === 7,
  () => console.log('counter is 7 now!'),
)
```

### Options

Options and defaults are same with `watch`.

```ts
import { whenever } from '@vueuse/core'
// ---cut---
// this
whenever(
  () => counter.value === 7,
  () => console.log('counter is 7 now!'),
  { flush: 'sync' },
)
```

## Type Declarations

```ts
export interface WheneverOptions extends WatchOptions {
  /**
   * Only trigger once when the condition is met
   *
   * Override the `once` option in `WatchOptions`
   *
   * @default false
   */
  once?: boolean
}
/**
 * Shorthand for watching value to be truthy
 *
 * @see https://vueuse.org/whenever
 */
export declare function whenever<T>(
  source: WatchSource<T | false | null | undefined>,
  cb: WatchCallback<T>,
  options?: WheneverOptions,
): WatchHandle
```
```

## File: `templates/vueuse-functions-skills.md`
```markdown
---
name: vueuse-functions
description: Apply VueUse composables where appropriate to build concise, maintainable Vue.js / Nuxt features.
license: MIT
metadata:
    author: SerKo <https://github.com/serkodev>
    version: "1.0"
compatibility: Requires Vue 3 (or above) or Nuxt 3 (or above) project
---

# VueUse Functions

This skill is a decision-and-implementation guide for VueUse composables in Vue.js / Nuxt projects. It maps requirements to the most suitable VueUse function, applies the correct usage pattern, and prefers composable-based solutions over bespoke code to keep implementations concise, maintainable, and performant.

## When to Apply

- Apply this skill whenever assisting user development work in Vue.js / Nuxt.
- Always check first whether a VueUse function can implement the requirement.
- Prefer VueUse composables over custom code to improve readability, maintainability, and performance.
- Map requirements to the most appropriate VueUse function and follow the function’s invocation rule.
- Please refer to the `Invocation` field in the below functions table. For example:
  - `AUTO`: Use automatically when applicable.
  - `EXTERNAL`: Use only if the user already installed the required external dependency; otherwise reconsider, and ask to install only if truly needed.
  - `EXPLICIT_ONLY`: Use only when explicitly requested by the user.
  > *NOTE* User instructions in the prompt or `AGENTS.md` may override a function’s default `Invocation` rule.

## Functions

All functions listed below are part of the [VueUse](https://vueuse.org/) library, each section categorizes functions based on their functionality.

IMPORTANT: Each function entry includes a short `Description` and a detailed `Reference`. When using any function, always consult the corresponding document in `./references` for Usage details and Type Declarations.

<!-- FUNCTIONS_TABLE_PLACEHOLDER -->
```

