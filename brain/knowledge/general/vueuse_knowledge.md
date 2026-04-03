---
id: vueuse-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.329816
---

# KNOWLEDGE EXTRACT: vueuse
> **Extracted on:** 2026-03-30 18:01:15
> **Source:** vueuse

---

## File: `skills.md`
```markdown
# 📦 vueuse/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/vueuse/skills


## Meta
- **Stars:** ⭐ 346 | **Forks:** 🍴 8
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent Skills for VueUse

## README (trích đầu)
```
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
const visibleCount = 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

