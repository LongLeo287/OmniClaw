---
id: github.com-shuding-better-all-4ad0d369-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.084602
---

# KNOWLEDGE EXTRACT: github.com_shuding_better-all_4ad0d369
> **Extracted on:** 2026-04-01 13:57:46
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523566/github.com_shuding_better-all_4ad0d369

---

## File: `.gitignore`
```
node_modules/
dist/
coverage/
*.log
.DS_Store
.claude
.pnpm-store/
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Shu Ding

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
# better-all

Promise.all with automatic dependency optimization and full type inference.

## Why?

When you have tasks with dependencies, the common `Promise.all` pattern is sometimes inefficient:

```typescript
// Common pattern: Sequential execution wastes time
const [a, b] = await Promise.all([getA(), getB()])  // a: 1s, b: 10s → takes 10s
const c = await getC(a)                             // c: 10s → takes 10s
// Total: 20 seconds
```

You could optimize this manually by parallelizing `b` and `c`:

```typescript
const a = await getA()               // a: 1s -> takes 1s
const [b, c] = await Promise.all([   // b: 10s, c: 10s -> takes 10s
  getB(),
  getC(a)
])
// Total: 11 seconds
```

But what if the durations of these methods change (i.e. unstable network latency)? Say `getA()` now takes 10 seconds and `getC()` takes 1 second. The previous manual optimization becomes suboptimal again, compared to the naive approach:

```typescript
const a = await getA()              // a: 10s -> takes 10s
const [b, c] = await Promise.all([  // b: 10s, c: 1s -> takes 10s
  getB(),
  getC(a)
])
// Total: 20 seconds

// Naive approach:
const [a, b] = await Promise.all([getA(), getB()])  // a: 10s, b: 10s → takes 10s
const c = await getC(a)                             // c: 1s → takes 1s
// Total: 11 seconds
```

To correctly optimize such cases using `Promise.all`, you'd have to _manually analyze and declare the dependency graph_:

```typescript
const [[a, c], b] = await Promise.all([
  getA().then(a => getC(a).then(c => [a, c])),
  getB()
])
```

This quickly becomes unmanageable in real-world scenarios with many tasks and complex dependencies, not to mention the loss of readability.

In real-world application code, there are more downsides of the naive approach and ad-hoc promise adjustments.
[Give this a read](https://github.com/shuding/better-all/discussions/3) if you are still not convinced.

## Better `Promise.all`

**This library solves it automatically:**

```typescript
import { all } from 'better-all'

const { a, b, c } = await all({
  async a() { return getA() },               // 1s
  async b() { return getB() },               // 10s
  async c() { return getC(await this.$.a) }  // 10s (waits for a)
})
// Total: 11 seconds - optimal parallelization!
```

`all` automatically kicks off all tasks immediately, and when hitting an `await this.$.dependency`, it waits for that specific task to complete.

The magical `this.$` object gives you access to all other task results as promises, allowing you to express dependencies naturally.

The library ensures maximal parallelization automatically.

## Installation

```bash
npm install better-all
# or
pnpm add better-all
# or
bun add better-all
# or
yarn add better-all
```

## Features

- **Full type inference**: Both results and dependencies are fully typed
- **Automatic maximal parallelization**: Independent tasks run in parallel
- **Object-based API**: Minimal cognitive load, easy to read
- **No hanging promises**: Avoids the uncaught dangling promises problem often seen in manual optimization
- **Auto-abort on failure**: Cancel remaining tasks when one fails via `this.$signal`
- **Debug mode with waterfall visualization**: See exactly how tasks execute with ASCII waterfall charts
- **Early exit support**: Exit flows early when a result is determined
- **Lightweight**: Minimal dependencies and small bundle size

## API

### `all(tasks, options?)`

Execute tasks with automatic dependency resolution.

- `tasks`: Object of async task functions
- `options`: Optional configuration object
  - `debug`: Set to `true` to output a waterfall chart showing task execution timeline
  - `signal`: An `AbortSignal` to abort all tasks externally
- Each task function receives:
  - `this.$` - an object with promises for all task results
  - `this.$signal` - an `AbortSignal` that aborts when any sibling task fails
- Returns a promise that resolves to an object with all task results
- Rejects if any task fails (like `Promise.all`)

### `allSettled(tasks, options?)`

Execute tasks with automatic dependency resolution, returning settled results for all tasks.

- `tasks`: Object of async task functions
- `options`: Optional configuration object
  - `debug`: Set to `true` to output a waterfall chart showing task execution timeline
  - `signal`: An `AbortSignal` to abort all tasks externally
- Each task function receives:
  - `this.$` - an object with promises for all task results
  - `this.$signal` - an `AbortSignal` (only aborts on external signal, not on sibling failure)
- Returns a promise that resolves to an object with all task results as `{ status: 'fulfilled', value }` or `{ status: 'rejected', reason }`
- Never rejects - failed tasks are included in the result (like `Promise.allSettled`)
- If a task depends on a failed task, the dependent task will also fail unless it catches the error

### `flow<R>(tasks, options?)`

Execute tasks with automatic dependency resolution and early exit support.

- **Type parameter `<R>`**: **Required**. Specifies the return type that `$end()` must accept
- `tasks`: Object of async task functions
- `options`: Same as `all()` - optional configuration object
- Each task function receives:
  - `this.$` - an object with promises for all task results
  - `this.$signal` - an `AbortSignal` for resource cleanup
  - `this.$end(value: R)` - function to exit the entire flow early with a return value of type `R`
- Returns a promise that resolves to `R | undefined`
  - Returns the value passed to the first `$end()` call
  - Returns `undefined` if no task calls `$end()`
- See [Early Exit Flow](#early-exit-flow) for detailed usage

## Examples

### Basic Parallel Execution

```typescript
const { a, b, c } = await all({
  async a() { await sleep(1000); return 1 },
  async b() { await sleep(1000); return 2 },
  async c() { await sleep(1000); return 3 }
})

// All three run in parallel
// Returns { a: 1, b: 2, c: 3 }
```

### With Dependencies

```typescript
const { user, profile, settings } = await all({
  async user() { return fetchUser(1) },
  async profile() { return fetchProfile((await this.$.user).id) },
  async settings() { return fetchSettings((await this.$.user).id) }
})

// User runs first, then profile and settings run in parallel
```

## Type Safety

Full TypeScript support with automatic type inference:

```typescript
const result = await all({
  async num() { return 42 },
  async str() { return 'hello' },
  async combined() {
    const n = await this.$.num  // n: number (auto-inferred!)
    const s = await this.$.str  // s: string (auto-inferred!)
    return `${s}: ${n}`
  }
})

result.num       // number
result.str       // string
result.combined  // string
```

### Complex Dependency Graph

```typescript
const { a, b, c, d, e } = await all({
  async a() { return 1 },
  async b() { return 2 },
  async c() { return (await this.$.a) + 10 },
  async d() { return (await this.$.b) + 20 },
  async e() { return (await this.$.c) + (await this.$.d) }
})

// a and b run in parallel
// c waits for a, d waits for b (c and d can overlap)
// e waits for both c and d

// { a: 1, b: 2, c: 11, d: 22, e: 33 }
console.log({ a, b, c, d, e })
```

### Stepped Dependency Chain

In this example, the `postsWithAuthor` task calls `await this.$.user` and `await this.$.posts` sequentially but there won't be any actual delays. The `all` function will always kick off all tasks as early as possible, so `posts` was already running while we awaited `this.$.user`:

```typescript
const result = await all({
  async user() {
    return fetchUser(1)
  },
  async posts() {
    return fetchPosts((await this.$.user).id)
  },
  async postsWithAuthor() {
    const user = await this.$.user
    console.log(`Fetched user: ${user.name}`)
    const posts = await this.$.posts
    return posts.map(post => ({ ...post, author: user.name }))
  },
})
```

This still gives optimal parallelization.

## Debug Mode

Enable debug mode to visualize task execution with a waterfall chart:

```typescript
const result = await all({
  async config() {
    await sleep(50)
    return { apiUrl: 'https://api.example.com' }
  },
  async user() {
    await sleep(120)
    return { id: 1, name: 'Alice' }
  },
  async posts() {
    const user = await this.$.user
    await sleep(200)
    return fetchPosts(user.id)
  },
  async profile() {
    const user = await this.$.user
    const config = await this.$.config
    await sleep(80)
    return fetchProfile(user.id, config.apiUrl)
  },
  async analytics() {
    const posts = await this.$.posts
    const profile = await this.$.profile
    await sleep(40)
    return computeAnalytics(posts, profile)
  }
}, { debug: true })
```

This outputs an ASCII waterfall chart showing:
- Task execution timeline
- Task duration in milliseconds
- Dependencies for each task
- Visual representation of parallel vs sequential execution

Example output:

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                           Task Execution Waterfall                             ║
╠════════════════════════════════════════════════════════════════════════════════╣
║ Total Duration: 364.54ms                                                       ║
╚════════════════════════════════════════════════════════════════════════════════╝

Task      │ Deps           │ Duration │ Timeline
──────────┼────────────────┼──────────┼──────────────────────────────────────────────────────────────────
config    │ -              │   51.4ms │ ████████                                                         
user      │ -              │  121.4ms │ ████████████████████                                             
posts     │ user           │  322.6ms │ ░░░░░░░░░░░░░░░░░░░░██████████████████████████████████████       
profile   │ user, config   │  202.9ms │ ░░░░░░░░░░░░░░░░░░░░███████████████████                          
analytics │ posts, profile │  364.4ms │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███████

Legend: █ = active (fulfilled), ▓ = active (rejected), ░ = waiting on dependency
```

The enhanced waterfall visualization shows:
- **█** (solid bars) = Active execution time when the task is running its code
- **░** (light shade) = Waiting time when the task is blocked on a dependency
- **▓** (dashed bars) = Active execution for tasks that failed

This makes it easy to:
- Distinguish between active execution vs waiting on dependencies
- Identify which tasks are running in parallel
- See exactly how long each task actively executes vs waits
- Understand the dependency chain and blocking relationships
- Spot opportunities for optimization (e.g., tasks with long wait times)

## Error Handling

### With `all()`

Errors propagate to dependent tasks automatically, similar to `Promise.all`:

```typescript
try {
  await all({
    async a() { throw new Error('Failed') },
    async b() { return (await this.$.a) + 1 }
  })
} catch (err) {
  console.error(err) // Error: Failed
}
```

### With `allSettled()`

All tasks complete and return their settled state, never rejecting:

```typescript
const result = await allSettled({
  async a() { return 1 },
  async b() { throw new Error('Task b failed') },
  async c() { return 3 }
})

// result.a: { status: 'fulfilled', value: 1 }
// result.b: { status: 'rejected', reason: Error('Task b failed') }
// result.c: { status: 'fulfilled', value: 3 }

if (result.a.status === 'fulfilled') {
  console.log(result.a.value) // 1
}

if (result.b.status === 'rejected') {
  console.error(result.b.reason) // Error: Task b failed
}
```

### Handling Dependency Failures with `allSettled()`

When a task depends on a failed task, it will also fail unless the error is caught:

```typescript
const result = await allSettled({
  async a() { throw new Error('a failed') },
  async b() {
    // This will fail because 'a' failed
    const aValue = await this.$.a
    return aValue + 10
  },
  async c() {
    // This handles the error and succeeds
    try {
      const aValue = await this.$.a
      return aValue + 10
    } catch (err) {
      return 'fallback value'
    }
  }
})

// result.a: { status: 'rejected', reason: Error('a failed') }
// result.b: { status: 'rejected', reason: Error('a failed') }
// result.c: { status: 'fulfilled', value: 'fallback value' }
```

## Abort Signal

When a task fails in `all()`, you may want to cancel other running tasks to avoid wasting resources (e.g., API calls, LLM requests).

Each task receives `this.$signal` - an `AbortSignal` that gets aborted when any sibling task fails:

```typescript
const result = await all({
  async fetchUser() {
    const res = await fetch('/api/user', { signal: this.$signal })
    return res.json()
  },
  async fetchPosts() {
    // If fetchUser fails, this.$signal will be aborted
    const res = await fetch('/api/posts', { signal: this.$signal })
    return res.json()
  }
})
```

You can also pass an external signal to respect parent abort controllers:

```typescript
const controller = new AbortController()

const result = await all({
  async a() { return fetchData(this.$signal) },
  async b() { return fetchMoreData(this.$signal) }
}, { signal: controller.signal })
```

**Note:** `allSettled()` does NOT auto-abort on task failure (to preserve its "wait for all" behavior), but external signal abort still works.

## Early Exit Flow

`flow` allows you to exit early from complex async flows when a task determines the final result. This is useful for optimization patterns like:

- **Cache checks**: Exit early if cached data is available
- **Racing operations**: Return the first successful result
- **Conditional computations**: Skip remaining work based on intermediate results

### `flow(tasks, options?)`

Execute tasks with automatic dependency resolution, but allow any task to end the entire flow early by calling `this.$end(value)`.

**Key behaviors:**
- All tasks start together in parallel (same as `all()`)
- First task to call `this.$end(value)` determines the return value
- After `$end()` is called, other tasks that try to access dependencies will receive errors (caught silently)
- Real errors (not from `$end`) still propagate to the caller
- Integrates with `this.$signal` for resource cleanup

### Early Exit from Cache

```typescript
import { flow } from 'better-all'

const data = await flow<YourDataType>({
  async checkCache() {
    const cached = await getFromCache('key')
    if (cached) this.$end(cached)  // Exit early with cached data
    return null
  },
  async fetchFromApi() {
    const user = await this.$.checkCache  // Will throw if cache hit
    return await fetchExpensiveData()
  },
  async processData() {
    const apiData = await this.$.fetchFromApi
    this.$end(transform(apiData))
  }
})
```

### Racing Operations

```typescript
const result = await flow<ResponseData>({
  async fetchFromPrimary() {
    await sleep(100)
    const data = await fetch('/api/primary')
    this.$end(await data.json())
  },
  async fetchFromBackup() {
    await sleep(500)
    const data = await fetch('/api/backup')
    this.$end(await data.json())
  }
})
// Returns data from whichever endpoint responds first
```

### Conditional Early Exit

```typescript
const result = await flow<{ error: string } | ProcessedData>({
  async validateInput() {
    const isValid = await validate(input)
    if (!isValid) this.$end({ error: 'Invalid input' })
    return input
  },
  async processData() {
    const validInput = await this.$.validateInput
    const processed = await heavyComputation(validInput)
    this.$end({ success: true, data: processed })
  }
})
```

### Return Type

You must specify the return type as a type parameter to `flow`:

```typescript
const result = await flow<number | string>({
  async task1() {
    this.$end(42)  // number
    return 1
  },
  async task2() {
    this.$end('hello')  // string
    return 'world'
  }
})
// result: number | string | undefined
```

To explicitly allow `undefined` as a return value:

```typescript
// Explicitly allow undefined
const result = await flow<string | undefined>({
  async task1() {
    const data = await getData()
    if (!data) this.$end(undefined)  // ✅ OK: undefined is in the type parameter
    this.$end(data)
  }
})
// result: string | undefined
```

**⚠️ Important Notes:**
- The type parameter `<R>` is **required** and specifies what type `$end()` accepts
- If you want to call `$end(undefined)`, you must explicitly include `undefined` in `R` (e.g., `flow<undefined>` or `flow<string | undefined>`)
- If no task calls `this.$end()`, the flow will return `undefined`
- Once `$end()` is called, subsequent dependency accesses will fail (but are caught silently)
- `$end()` stops the current task execution (throws internally)

## Development

```bash
pnpm install     # Install dependencies
pnpm test        # Run tests
pnpm build       # Build
```

## Author

[Shu Ding](https://shud.in)

## License

MIT
```

## File: `index.ts`
```typescript
export { all, allSettled, type Task } from './lib/index'
```

## File: `package.json`
```json
{
  "name": "better-all",
  "version": "0.0.7",
  "description": "Better Promise.all with automatic dependency optimization",
  "type": "module",
  "main": "./dist/es/index.js",
  "module": "./dist/es/index.js",
  "types": "./dist/es/index.d.ts",
  "author": "Shu Ding <g@shud.in>",
  "repository": "github:shuding/better-all",
  "license": "MIT",
  "exports": {
    ".": {
      "types": "./dist/es/index.d.ts",
      "import": "./dist/es/index.js",
      "require": "./dist/index.cjs"
    }
  },
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "bunchee",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "prepublishOnly": "npm run build"
  },
  "keywords": [
    "promise",
    "async",
    "parallel",
    "dependency",
    "optimization"
  ],
  "devDependencies": {
    "@types/node": "^22.10.5",
    "@vitest/coverage-v8": "^3.0.5",
    "bunchee": "^6.3.1",
    "typescript": "^5.9.3",
    "vitest": "^3.0.5"
  }
}
```

## File: `pnpm-workspace.yaml`
```yaml
onlyBuiltDependencies:
  - '@swc/core'
  - esbuild
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020"],
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist"
  },
  "include": ["lib/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `vitest.config.ts`
```typescript
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'dist/',
        '**/*.config.ts',
        '**/*.test.ts',
      ],
    },
  },
})
```

## File: `lib/index.test.ts`
```typescript
import { describe, it, expect, vi, expectTypeOf } from 'vitest'
import { all, allSettled, flow } from './index'

/**
 * Utility function to sleep for a specified number of milliseconds
 */
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms))

describe('all', () => {
  describe('Basic parallel execution', () => {
    it('should execute independent tasks in parallel', async () => {
      const executionOrder: string[] = []

      const result = await all({
        async a() {
          executionOrder.push('a-start')
          await sleep(20)
          executionOrder.push('a-end')
          return 1
        },
        async b() {
          executionOrder.push('b-start')
          await sleep(10)
          executionOrder.push('b-end')
          return 2
        },
        async c() {
          executionOrder.push('c-start')
          await sleep(5)
          executionOrder.push('c-end')
          return 3
        },
      })

      expect(result).toEqual({ a: 1, b: 2, c: 3 })
      expect(executionOrder).toEqual([
        'a-start',
        'b-start',
        'c-start',
        'c-end',
        'b-end',
        'a-end',
      ])
    })

    it('should handle synchronous tasks', async () => {
      const result = await all({
        a() {
          return 1
        },
        b() {
          return 2
        },
        c() {
          return 3
        },
      })

      expect(result).toEqual({ a: 1, b: 2, c: 3 })
    })

    it('should handle mixed sync and async tasks', async () => {
      const result = await all({
        a() {
          return 1
        },
        async b() {
          await sleep(10)
          return 2
        },
        c() {
          return 3
        },
      })

      expect(result).toEqual({ a: 1, b: 2, c: 3 })
    })
  })

  describe('Dependency resolution', () => {
    it('should handle single dependency', async () => {
      const executionOrder: string[] = []

      const result = await all({
        async a() {
          executionOrder.push('a')
          return 1
        },
        async b() {
          const aValue = await this.$.a
          executionOrder.push('b')
          return aValue + 10
        },
      })

      expect(result).toEqual({ a: 1, b: 11 })
      expect(executionOrder).toEqual(['a', 'b'])
    })

    it('should handle multiple dependencies', async () => {
      const result = await all({
        async a() {
          await sleep(10)
          return 1
        },
        async b() {
          await sleep(10)
          return 2
        },
        async c() {
          const aValue = await this.$.a
          const bValue = await this.$.b
          return aValue + bValue
        },
      })

      expect(result).toEqual({ a: 1, b: 2, c: 3 })
    })

    it('should handle chained dependencies', async () => {
      const executionOrder: string[] = []

      const result = await all({
        async a() {
          executionOrder.push('a')
          return 1
        },
        async b() {
          const aValue = await this.$.a
          executionOrder.push('b')
          return aValue + 10
        },
        async c() {
          const bValue = await this.$.b
          executionOrder.push('c')
          return bValue + 100
        },
      })

      expect(result).toEqual({ a: 1, b: 11, c: 111 })
      expect(executionOrder).toEqual(['a', 'b', 'c'])
    })

    it('should handle multiple tasks depending on the same task', async () => {
      const executionOrder: string[] = []

      const result = await all({
        async a() {
          executionOrder.push('a')
          await sleep(10)
          return 1
        },
        async b() {
          const aValue = await this.$.a
          executionOrder.push('b')
          return aValue + 10
        },
        async c() {
          const aValue = await this.$.a
          executionOrder.push('c')
          return aValue + 100
        },
      })

      expect(result).toEqual({ a: 1, b: 11, c: 101 })
      expect(executionOrder[0]).toBe('a')
    })

    it('should execute each task only once even when used by multiple dependents', async () => {
      const callCounts = { a: 0, b: 0, c: 0 }

      const result = await all({
        async a() {
          callCounts.a++
          await sleep(10)
          return 1
        },
        async b() {
          callCounts.b++
          const aValue = await this.$.a
          return aValue + 10
        },
        async c() {
          callCounts.c++
          const aValue = await this.$.a
          return aValue + 100
        },
      })

      expect(result).toEqual({ a: 1, b: 11, c: 101 })
      expect(callCounts).toEqual({ a: 1, b: 1, c: 1 })
    })

    it('should execute task only once even when awaited multiple times in same task', async () => {
      const callCounts = { a: 0, b: 0 }

      const result = await all({
        async a() {
          callCounts.a++
          return 1
        },
        async b() {
          callCounts.b++
          const first = await this.$.a
          const second = await this.$.a
          const third = await this.$.a
          return first + second + third
        },
      })

      expect(result).toEqual({ a: 1, b: 3 })
      expect(callCounts).toEqual({ a: 1, b: 1 })
    })

    it('should handle complex dependency graph', async () => {
      const result = await all({
        async a() {
          return 1
        },
        async b() {
          return 2
        },
        async c() {
          return (await this.$.a) + 10
        },
        async d() {
          return (await this.$.b) + 20
        },
        async e() {
          return (await this.$.c) + (await this.$.d)
        },
      })

      expect(result).toEqual({ a: 1, b: 2, c: 11, d: 22, e: 33 })
    })
  })

  describe('Error handling', () => {
    it('should propagate errors from independent tasks', async () => {
      await expect(
        all({
          async a() {
            throw new Error('Task a failed')
          },
          async b() {
            return 2
          },
        }),
      ).rejects.toThrow('Task a failed')
    })

    it('should propagate errors from dependent tasks', async () => {
      await expect(
        all({
          async a() {
            return 1
          },
          async b() {
            await this.$.a
            throw new Error('Task b failed')
          },
        }),
      ).rejects.toThrow('Task b failed')
    })

    it('should propagate errors to tasks waiting for dependency', async () => {
      await expect(
        all({
          async a() {
            await sleep(10)
            throw new Error('Task a failed')
          },
          async b() {
            const aValue = await this.$.a
            return aValue + 10
          },
        }),
      ).rejects.toThrow('Task a failed')
    })

    it('should throw error for unknown dependency', async () => {
      await expect(
        all({
          async a() {
            await (this.$ as any).unknownTask
            return 1
          },
        }),
      ).rejects.toThrow('Unknown task "unknownTask"')
    })

    it('should handle errors in multiple tasks', async () => {
      await expect(
        all({
          async a() {
            throw new Error('Task a failed')
          },
          async b() {
            throw new Error('Task b failed')
          },
        }),
      ).rejects.toThrow()
    })
  })

  describe('Return values', () => {
    it('should return values of various types', async () => {
      const result = await all({
        num() {
          return 42
        },
        str() {
          return 'hello'
        },
        bool() {
          return true
        },
        arr() {
          return [1, 2, 3]
        },
        obj() {
          return { key: 'value' }
        },
        nil() {
          return null
        },
        undef() {
          return undefined
        },
      })

      expect(result).toEqual({
        num: 42,
        str: 'hello',
        bool: true,
        arr: [1, 2, 3],
        obj: { key: 'value' },
        nil: null,
        undef: undefined,
      })
    })

    it('should handle promises that resolve to various types', async () => {
      const result = await all({
        async num() {
          return Promise.resolve(42)
        },
        async str() {
          return Promise.resolve('hello')
        },
        async obj() {
          return Promise.resolve({ key: 'value' })
        },
      })

      expect(result).toEqual({
        num: 42,
        str: 'hello',
        obj: { key: 'value' },
      })
    })

    it('should preserve object references', async () => {
      const obj = { key: 'value' }
      const arr = [1, 2, 3]

      const result = await all({
        obj() {
          return obj
        },
        arr() {
          return arr
        },
      })

      expect(result.obj).toBe(obj)
      expect(result.arr).toBe(arr)
    })
  })

  describe('Edge cases', () => {
    it('should handle empty object', async () => {
      const result = await all({})
      expect(result).toEqual({})
    })

    it('should handle single task', async () => {
      const result = await all({
        a() {
          return 1
        },
      })
      expect(result).toEqual({ a: 1 })
    })

    it('should handle task names with special characters', async () => {
      const result = await all({
        'task-1'() {
          return 1
        },
        task_2() {
          return 2
        },
        task$3() {
          return 3
        },
      })

      expect(result).toEqual({
        'task-1': 1,
        task_2: 2,
        task$3: 3,
      })
    })
  })

  describe('Performance', () => {
    it('should execute independent tasks truly in parallel', async () => {
      const startTime = Date.now()

      await all({
        async a() {
          await sleep(50)
          return 1
        },
        async b() {
          await sleep(50)
          return 2
        },
        async c() {
          await sleep(50)
          return 3
        },
      })

      const duration = Date.now() - startTime

      expect(duration).toBeLessThan(100)
    })

    it('should not block independent tasks when one task has dependency', async () => {
      const executionOrder: string[] = []

      await all({
        async a() {
          await sleep(30)
          executionOrder.push('a')
          return 1
        },
        async b() {
          await sleep(10)
          executionOrder.push('b')
          return 2
        },
        async c() {
          const aValue = await this.$.a
          executionOrder.push('c')
          return aValue + 10
        },
      })

      expect(executionOrder).toEqual(['b', 'a', 'c'])
    })
  })

  describe('Type inference', () => {
    it('should infer correct types for simple tasks', async () => {
      const result = await all({
        num() {
          return 42
        },
        str() {
          return 'hello'
        },
        async asyncNum() {
          return 123
        },
      })

      expectTypeOf(result.num).toEqualTypeOf<42>()
      expectTypeOf(result.str).toEqualTypeOf<'hello'>()
      expectTypeOf(result.asyncNum).toEqualTypeOf<number>()

      expect(result.num).toBe(42)
      expect(result.str).toBe('hello')
      expect(result.asyncNum).toBe(123)
    })

    it('should infer types with dependency access', async () => {
      const result = await all({
        num() {
          return 42
        },
        str() {
          return 'hello'
        },
        async combined() {
          const n = await this.$.num
          const s = await this.$.str
          return `${s}: ${n}`
        },
      })

      expectTypeOf(result.num).toEqualTypeOf<42>()
      expectTypeOf(result.str).toEqualTypeOf<'hello'>()
      expectTypeOf(result.combined).toEqualTypeOf<string>()

      expect(result.combined).toBe('hello: 42')
    })

    it('should infer complex object types', async () => {
      const result = await all({
        user() {
          return { id: 1, name: 'Alice' }
        },
        async profile() {
          const user = await this.$.user
          return { userId: user.id, displayName: user.name.toUpperCase() }
        },
      })

      expectTypeOf(result.user).toEqualTypeOf<{ id: number; name: string }>()
      expectTypeOf(result.profile).toEqualTypeOf<{
        userId: number
        displayName: string
      }>()

      expect(result.profile).toEqual({ userId: 1, displayName: 'ALICE' })
    })

    it('should error on non-function task definitions', async () => {
      await expect(
        // @ts-expect-error
        all({
          invalidTask: 1,
        }),
      ).rejects.toThrow('Task "invalidTask" is not a function')

      await expect(
        // @ts-expect-error
        all({
          invalidTask: {
            a: 1,
          },
        }),
      ).rejects.toThrow('Task "invalidTask" is not a function')
    })

    it('should allow functions with optional arguments', async () => {
      async function a(options?: number) {
        return options ?? 1
      }

      const result = await all({
        a,
        async b() {
          return (await this.$.a) + 2
        },
      })
      expect(result.a).toBe(1)
      expect(result.b).toBe(3)
    })
  })

  describe('Real-world scenarios', () => {
    it('should handle API call pattern with dependent requests', async () => {
      const mockFetch = vi.fn()

      mockFetch
        .mockResolvedValueOnce({ id: 1, name: 'User' })
        .mockResolvedValueOnce([{ id: 1, title: 'Post 1' }])
        .mockResolvedValueOnce([{ id: 1, text: 'Comment 1' }])

      const result = await all({
        async user() {
          return mockFetch('/user/1')
        },
        async posts() {
          const user = await this.$.user
          return mockFetch(`/user/${user.id}/posts`)
        },
        async comments() {
          const posts = await this.$.posts
          return mockFetch(`/post/${posts[0].id}/comments`)
        },
      })

      expect(mockFetch).toHaveBeenCalledTimes(3)
      expect(result.user).toEqual({ id: 1, name: 'User' })
      expect(result.posts).toEqual([{ id: 1, title: 'Post 1' }])
      expect(result.comments).toEqual([{ id: 1, text: 'Comment 1' }])
    })

    it('should handle mixed parallel and dependent operations', async () => {
      const result = await all({
        async config() {
          await sleep(10)
          return { apiUrl: 'https://api.example.com' }
        },
        async staticData() {
          await sleep(10)
          return { locale: 'en' }
        },
        async userData() {
          const config = await this.$.config
          return { name: 'User', from: config.apiUrl }
        },
        async page() {
          const user = await this.$.userData
          const staticData = await this.$.staticData
          return {
            title: `Hello ${user.name}`,
            locale: staticData.locale,
          }
        },
      })

      expect(result.page).toEqual({
        title: 'Hello User',
        locale: 'en',
      })
    })

    it('should handle data transformation pipeline', async () => {
      const result = await all({
        async rawData() {
          return [1, 2, 3, 4, 5]
        },
        async filtered() {
          const data = await this.$.rawData
          return data.filter((n) => n % 2 === 0)
        },
        async mapped() {
          const data = await this.$.filtered
          return data.map((n) => n * 2)
        },
        async reduced() {
          const data = await this.$.mapped
          return data.reduce((sum, n) => sum + n, 0)
        },
      })

      expect(result).toEqual({
        rawData: [1, 2, 3, 4, 5],
        filtered: [2, 4],
        mapped: [4, 8],
        reduced: 12,
      })
    })
  })

  describe('Multiple dependencies', () => {
    it('should handle three dependencies', async () => {
      const result = await all({
        a() {
          return 1
        },
        b() {
          return 2
        },
        c() {
          return 3
        },
        async sum() {
          const a = await this.$.a
          const b = await this.$.b
          const c = await this.$.c
          return a + b + c
        },
      })

      expect(result.sum).toBe(6)
    })

    it('should handle computation between dependency values', async () => {
      const result = await all({
        a() {
          return 5
        },
        b() {
          return 3
        },
        async computed() {
          const a = await this.$.a
          const b = await this.$.b
          const squared = a * a
          const doubled = b * 2
          return squared + doubled
        },
      })

      expect(result.computed).toBe(31)
    })

    it('should handle async operations in dependent tasks', async () => {
      const result = await all({
        async a() {
          await sleep(10)
          return 1
        },
        async b() {
          const aValue = await this.$.a
          await sleep(10)
          return aValue + 10
        },
      })

      expect(result).toEqual({ a: 1, b: 11 })
    })
  })
})

describe('allSettled', () => {
  describe('Basic execution with mixed results', () => {
    it('should return fulfilled and rejected results without throwing', async () => {
      const result = await allSettled({
        async a() {
          return 1
        },
        async b() {
          throw new Error('Task b failed')
        },
        async c() {
          return 3
        },
      })

      expect(result.a).toEqual({ status: 'fulfilled', value: 1 })
      expect(result.b).toEqual({
        status: 'rejected',
        reason: expect.any(Error),
      })
      expect(result.b.status === 'rejected' && result.b.reason.message).toBe(
        'Task b failed',
      )
      expect(result.c).toEqual({ status: 'fulfilled', value: 3 })
    })

    it('should handle all tasks succeeding', async () => {
      const result = await allSettled({
        a() {
          return 1
        },
        async b() {
          return 'hello'
        },
        async c() {
          return true
        },
      })

      expect(result).toEqual({
        a: { status: 'fulfilled', value: 1 },
        b: { status: 'fulfilled', value: 'hello' },
        c: { status: 'fulfilled', value: true },
      })
    })

    it('should handle all tasks failing', async () => {
      const result = await allSettled({
        async a() {
          throw new Error('a failed')
        },
        async b() {
          throw new Error('b failed')
        },
      })

      expect(result.a).toEqual({
        status: 'rejected',
        reason: expect.any(Error),
      })
      expect(result.b).toEqual({
        status: 'rejected',
        reason: expect.any(Error),
      })
    })
  })

  describe('Dependency resolution with failures', () => {
    it('should handle successful task depending on another successful task', async () => {
      const result = await allSettled({
        async a() {
          return 1
        },
        async b() {
          const aValue = await this.$.a
          return aValue + 10
        },
      })

      expect(result).toEqual({
        a: { status: 'fulfilled', value: 1 },
        b: { status: 'fulfilled', value: 11 },
      })
    })

    it('should handle task depending on failed task', async () => {
      const result = await allSettled({
        async a() {
          throw new Error('Task a failed')
        },
        async b() {
          const aValue = await this.$.a
          return aValue + 10
        },
      })

      expect(result.a).toEqual({
        status: 'rejected',
        reason: expect.any(Error),
      })
      expect(result.b).toEqual({
        status: 'rejected',
        reason: expect.any(Error),
      })
    })

    it('should allow dependent task to catch and handle dependency failure', async () => {
      const result = await allSettled({
        async a() {
          throw new Error('Task a failed')
        },
        async b() {
          try {
            const aValue = await this.$.a
            return aValue + 10
          } catch (err) {
            return 'handled error'
          }
        },
      })

      expect(result.a).toEqual({
        status: 'rejected',
        reason: expect.any(Error),
      })
      expect(result.b).toEqual({
        status: 'fulfilled',
        value: 'handled error',
      })
    })

    it('should handle multiple tasks depending on one failed task', async () => {
      const result = await allSettled({
        async a() {
          throw new Error('Task a failed')
        },
        async b() {
          const aValue = await this.$.a
          return aValue + 10
        },
        async c() {
          const aValue = await this.$.a
          return aValue + 100
        },
      })

      expect(result.a.status).toBe('rejected')
      expect(result.b.status).toBe('rejected')
      expect(result.c.status).toBe('rejected')
    })

    it('should not block independent tasks when one fails', async () => {
      const executionOrder: string[] = []

      const result = await allSettled({
        async a() {
          await sleep(10)
          executionOrder.push('a')
          throw new Error('a failed')
        },
        async b() {
          await sleep(5)
          executionOrder.push('b')
          return 2
        },
        async c() {
          await sleep(15)
          executionOrder.push('c')
          return 3
        },
      })

      expect(executionOrder).toEqual(['b', 'a', 'c'])
      expect(result.a.status).toBe('rejected')
      expect(result.b).toEqual({ status: 'fulfilled', value: 2 })
      expect(result.c).toEqual({ status: 'fulfilled', value: 3 })
    })
  })

  describe('Complex scenarios', () => {
    it('should handle complex dependency graph with mixed results', async () => {
      const result = await allSettled({
        async a() {
          return 1
        },
        async b() {
          throw new Error('b failed')
        },
        async c() {
          const aValue = await this.$.a
          return aValue + 10
        },
        async d() {
          const bValue = await this.$.b
          return bValue + 20
        },
        async e() {
          const cValue = await this.$.c
          return cValue + 100
        },
      })

      expect(result.a).toEqual({ status: 'fulfilled', value: 1 })
      expect(result.b.status).toBe('rejected')
      expect(result.c).toEqual({ status: 'fulfilled', value: 11 })
      expect(result.d.status).toBe('rejected')
      expect(result.e).toEqual({ status: 'fulfilled', value: 111 })
    })

    it('should handle partial failure in API call pattern', async () => {
      const mockFetch = vi.fn()

      // user and settings run in parallel, posts depends on user
      // Order of execution: user (1st call), settings (2nd call), posts (3rd call)
      mockFetch
        .mockResolvedValueOnce({ id: 1, name: 'User' }) // user call
        .mockResolvedValueOnce({ theme: 'dark' }) // settings call (parallel)
        .mockRejectedValueOnce(new Error('Posts API failed')) // posts call (after user)

      const result = await allSettled({
        async user() {
          return mockFetch('/user/1')
        },
        async posts() {
          const user = await this.$.user
          return mockFetch(`/user/${user.id}/posts`)
        },
        async settings() {
          return mockFetch('/settings')
        },
      })

      expect(result.user).toEqual({
        status: 'fulfilled',
        value: { id: 1, name: 'User' },
      })
      expect(result.posts.status).toBe('rejected')
      expect(result.settings).toEqual({
        status: 'fulfilled',
        value: { theme: 'dark' },
      })
    })
  })

  describe('Edge cases', () => {
    it('should handle empty object', async () => {
      const result = await allSettled({})
      expect(result).toEqual({})
    })

    it('should handle single successful task', async () => {
      const result = await allSettled({
        a() {
          return 1
        },
      })
      expect(result).toEqual({
        a: { status: 'fulfilled', value: 1 },
      })
    })

    it('should handle single failed task', async () => {
      const result = await allSettled({
        async a() {
          throw new Error('failed')
        },
      })
      expect(result.a.status).toBe('rejected')
    })

    it('should preserve different error types', async () => {
      const customError = new TypeError('type error')
      const result = await allSettled({
        async a() {
          throw customError
        },
        async b() {
          throw 'string error'
        },
        async c() {
          throw { code: 'CUSTOM', message: 'object error' }
        },
      })

      expect(result.a).toEqual({
        status: 'rejected',
        reason: customError,
      })
      expect(result.b).toEqual({
        status: 'rejected',
        reason: 'string error',
      })
      expect(result.c).toEqual({
        status: 'rejected',
        reason: { code: 'CUSTOM', message: 'object error' },
      })
    })
  })

  describe('Type inference', () => {
    it('should infer correct types for settled results', async () => {
      const result = await allSettled({
        num() {
          return 42
        },
        str() {
          return 'hello'
        },
        async asyncNum() {
          return 123
        },
      })

      expectTypeOf(result.num).toEqualTypeOf<
        { status: 'fulfilled'; value: 42 } | { status: 'rejected'; reason: any }
      >()
      expectTypeOf(result.str).toEqualTypeOf<
        | { status: 'fulfilled'; value: 'hello' }
        | { status: 'rejected'; reason: any }
      >()

      if (result.num.status === 'fulfilled') {
        expect(result.num.value).toBe(42)
      }
      if (result.str.status === 'fulfilled') {
        expect(result.str.value).toBe('hello')
      }
      if (result.asyncNum.status === 'fulfilled') {
        expect(result.asyncNum.value).toBe(123)
      }
    })
  })

  describe('Return value types', () => {
    it('should handle various return types in fulfilled results', async () => {
      const result = await allSettled({
        num() {
          return 42
        },
        str() {
          return 'hello'
        },
        arr() {
          return [1, 2, 3]
        },
        obj() {
          return { key: 'value' }
        },
        nil() {
          return null
        },
        undef() {
          return undefined
        },
      })

      expect(result).toEqual({
        num: { status: 'fulfilled', value: 42 },
        str: { status: 'fulfilled', value: 'hello' },
        arr: { status: 'fulfilled', value: [1, 2, 3] },
        obj: { status: 'fulfilled', value: { key: 'value' } },
        nil: { status: 'fulfilled', value: null },
        undef: { status: 'fulfilled', value: undefined },
      })
    })
  })
})

describe('Debug mode', () => {
  describe('all() with debug', () => {
    it('should output waterfall chart with debug: true', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      const result = await all(
        {
          async a() {
            await sleep(50)
            return 1
          },
          async b() {
            await sleep(30)
            return 2
          },
          async c() {
            const aValue = await this.$.a
            await sleep(20)
            return aValue + 10
          },
        },
        { debug: true },
      )

      expect(result).toEqual({ a: 1, b: 2, c: 11 })
      expect(consoleSpy).toHaveBeenCalledTimes(1)

      const output = consoleSpy.mock.calls[0][0]
      expect(output).toContain('Task Execution Waterfall')
      expect(output).toContain('Total Duration')
      expect(output).toContain('Timeline')
      expect(output).toContain('a')
      expect(output).toContain('b')
      expect(output).toContain('c')

      consoleSpy.mockRestore()
    })

    it('should show multiple dependencies in deps column', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async a() {
            return 1
          },
          async b() {
            return 2
          },
          async c() {
            const aValue = await this.$.a
            const bValue = await this.$.b
            return aValue + bValue
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')
      const cLine = lines.find((line: string) => line.trim().startsWith('c'))

      expect(cLine).toBeDefined()
      // Should list both dependencies (order may vary)
      expect(cLine).toMatch(/a.*b|b.*a/)

      consoleSpy.mockRestore()
    })

    it('should show complex dependency graph with wait-active-wait pattern', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await allSettled(
        {
          async fastTask() {
            await sleep(20)
          },
          async slowTask() {
            await sleep(100)
          },
          async multiWaitTask() {
            await this.$.fastTask
            await sleep(30)
            await this.$.slowTask
            await sleep(10)
          },
          async waitForMultiWaitTask() {
            await this.$.multiWaitTask
            await sleep(10)
          },
          async errorAfterFastTask() {
            await this.$.fastTask
            await sleep(15)
            throw new Error()
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      consoleSpy.mockRestore()

      console.log(output)

      // multiWaitTask should show: ░(wait for fast) █(30ms active) ░(wait for slow) █(10ms active)
      const lines = output.split('\n')
      const multiWaitLine = lines.find((line: string) =>
        line.includes('multiWaitTask'),
      )
      expect(multiWaitLine).toBeDefined()

      // Should contain both waiting (░) and active (█) characters
      expect(multiWaitLine).toContain('░')
      expect(multiWaitLine).toContain('█')
    })

    it('should show dependencies in waterfall chart', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async a() {
            return 1
          },
          async b() {
            return 2
          },
          async c() {
            const aValue = await this.$.a
            const bValue = await this.$.b
            return aValue + bValue
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      // Check that task c shows dependencies on a and b
      expect(output).toContain('a')
      expect(output).toContain('b')
      expect(output).toContain('c')

      consoleSpy.mockRestore()
    })

    it('should work with no dependencies', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      const result = await all(
        {
          async a() {
            return 1
          },
          async b() {
            return 2
          },
        },
        { debug: true },
      )

      expect(result).toEqual({ a: 1, b: 2 })
      expect(consoleSpy).toHaveBeenCalledTimes(1)

      consoleSpy.mockRestore()
    })

    it('should still output waterfall on error', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await expect(
        all(
          {
            async a() {
              throw new Error('a failed')
            },
            async b() {
              return 2
            },
          },
          { debug: true },
        ),
      ).rejects.toThrow('a failed')

      expect(consoleSpy).toHaveBeenCalledTimes(1)
      const output = consoleSpy.mock.calls[0][0]
      expect(output).toContain('Task Execution Waterfall')

      consoleSpy.mockRestore()
    })
  })

  describe('allSettled() with debug', () => {
    it('should output waterfall chart with debug: true', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      const result = await allSettled(
        {
          async a() {
            return 1
          },
          async b() {
            throw new Error('b failed')
          },
          async c() {
            return 3
          },
        },
        { debug: true },
      )

      expect(result.a).toEqual({ status: 'fulfilled', value: 1 })
      expect(result.b.status).toBe('rejected')
      expect(result.c).toEqual({ status: 'fulfilled', value: 3 })

      expect(consoleSpy).toHaveBeenCalledTimes(1)
      const output = consoleSpy.mock.calls[0][0]
      expect(output).toContain('Task Execution Waterfall')
      expect(output).toContain('Legend')

      consoleSpy.mockRestore()
    })

    it('should show rejected tasks with different visual (▓)', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await allSettled(
        {
          async failed() {
            await sleep(30)
            throw new Error('failed')
          },
          async success() {
            await sleep(30)
            return 'ok'
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')
      const failedLine = lines.find((line: string) => line.includes('failed'))
      const successLine = lines.find((line: string) => line.includes('success'))

      // Failed task should show ▓ (rejected bars)
      expect(failedLine).toContain('▓')
      // Success task should show █ (fulfilled bars)
      expect(successLine).toContain('█')

      // Legend should explain both
      expect(output).toContain('active (rejected)')
      expect(output).toContain('▓')

      consoleSpy.mockRestore()
    })

    it('should show tasks that depend on failed tasks as waiting', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await allSettled(
        {
          async a() {
            await sleep(50)
            throw new Error('a failed')
          },
          async b() {
            const aValue = await this.$.a
            await sleep(20)
            return aValue + 10
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')
      const bLine = lines.find((line: string) => line.trim().startsWith('b'))

      // Task b should show waiting (░) for dependency a
      // When a fails, b fails immediately at the await point
      // So it shows waiting time only (no active execution time)
      expect(bLine).toContain('░') // Waiting for a

      consoleSpy.mockRestore()
    })
  })

  describe('Edge cases', () => {
    it('should handle empty object with debug (inline snapshot)', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      const result = await all({}, { debug: true })
      expect(result).toEqual({})

      // Should still output chart (even if empty)
      expect(consoleSpy).toHaveBeenCalledTimes(1)
      const output = consoleSpy.mock.calls[0][0]

      expect(output).toMatchInlineSnapshot(`""`)

      consoleSpy.mockRestore()
    })

    it('should work without debug option (backwards compatibility)', async () => {
      const consoleSpy = vi.spyOn(console, 'log')

      const result = await all({
        async a() {
          return 1
        },
      })

      expect(result).toEqual({ a: 1 })
      // Should not output anything without debug flag
      expect(consoleSpy).not.toHaveBeenCalled()

      consoleSpy.mockRestore()
    })

    it('should handle single task with debug', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async onlyTask() {
            await sleep(25)
            return 'done'
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')
      const taskLine = lines.find((line: string) => line.includes('onlyTask'))

      expect(taskLine).toBeDefined()
      expect(taskLine).toContain('│ -') // No dependencies
      expect(taskLine).toContain('█') // Active bar

      consoleSpy.mockRestore()
    })

    it('should handle task names with special characters', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async 'task-1'() {
            return 1
          },
          async task_2() {
            return 2
          },
          async task$3() {
            return 3
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]

      // All task names should appear in output
      expect(output).toContain('task-1')
      expect(output).toContain('task_2')
      expect(output).toContain('task$3')

      consoleSpy.mockRestore()
    })

    it('should handle long dependency chains in output', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async a() {
            return 1
          },
          async b() {
            return await this.$.a
          },
          async c() {
            return await this.$.b
          },
          async d() {
            return await this.$.c
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')

      // Each task should show its dependency
      const bLine = lines.find((line: string) => line.trim().startsWith('b'))
      const cLine = lines.find((line: string) => line.trim().startsWith('c'))
      const dLine = lines.find((line: string) => line.trim().startsWith('d'))

      expect(bLine).toContain('a')
      expect(cLine).toContain('b')
      expect(dLine).toContain('c')

      // Later tasks should show more waiting (░)
      const dTimelineMatch = dLine?.match(/Timeline[^│]*│\s*(.+)$/)
      if (dTimelineMatch) {
        const dTimeline = dTimelineMatch[1]
        expect(dTimeline).toContain('░')
      }

      consoleSpy.mockRestore()
    })

    it('should properly format table alignment', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async shortName() {
            return 1
          },
          async veryLongTaskNameHere() {
            return 2
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')

      // Find header separator line
      const separatorLine = lines.find((line: string) => line.includes('─┼─'))
      expect(separatorLine).toBeDefined()

      // All task lines should have the same number of │ separators
      const taskLines = lines.filter(
        (line: string) =>
          (line.includes('shortName') ||
            line.includes('veryLongTaskNameHere')) &&
          line.includes('│'),
      )

      taskLines.forEach((line: string) => {
        // Should have exactly 3 separators (4 columns)
        const separators = (line.match(/│/g) || []).length
        expect(separators).toBe(3)
      })

      consoleSpy.mockRestore()
    })

    it('should show correct timeline width', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async task() {
            await sleep(50)
            return 1
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]
      const lines = output.split('\n')
      const taskLine = lines.find(
        (line: string) => line.includes('task') && line.includes('█'),
      )

      if (taskLine) {
        // Timeline should be at least 60 characters (the chart width)
        const parts = taskLine.split('│')
        const timeline = parts[parts.length - 1]
        // Timeline column should be consistently sized
        expect(timeline.length).toBeGreaterThanOrEqual(60)
      }

      consoleSpy.mockRestore()
    })

    it('should display durations in milliseconds with precision', async () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

      await all(
        {
          async quickTask() {
            await sleep(15)
            return 1
          },
          async slowerTask() {
            await sleep(55)
            return 2
          },
        },
        { debug: true },
      )

      const output = consoleSpy.mock.calls[0][0]

      // Should show durations with decimal precision (e.g., "15.2ms", "55.7ms")
      expect(output).toMatch(/\d+\.\d+ms/)

      // Total duration should also be present
      expect(output).toMatch(/Total Duration: \d+\.\d+ms/)

      consoleSpy.mockRestore()
    })
  })
})

describe('Abort signal', () => {
  describe('all() with $signal', () => {
    it('should provide $signal as an AbortSignal', async () => {
      let receivedSignal: AbortSignal | undefined

      await all({
        async a() {
          receivedSignal = this.$signal
          return 1
        },
      })

      expect(receivedSignal).toBeInstanceOf(AbortSignal)
    })

    it('should abort $signal when a sibling task fails', async () => {
      const abortEvents: string[] = []

      await expect(
        all({
          async fast() {
            throw new Error('fast failed')
          },
          async slow() {
            this.$signal.addEventListener('abort', () => {
              abortEvents.push('slow-aborted')
            })
            await sleep(50)
            return 'slow done'
          },
        }),
      ).rejects.toThrow('fast failed')

      // Give time for abort event to fire
      await sleep(10)
      expect(abortEvents).toContain('slow-aborted')
    })

    it('should set abort reason to the error that caused the failure', async () => {
      let abortReason: any

      const errorToThrow = new Error('task failed')

      await expect(
        all({
          async failing() {
            throw errorToThrow
          },
          async waiting() {
            this.$signal.addEventListener('abort', () => {
              abortReason = this.$signal.reason
            })
            await sleep(50)
            return 'done'
          },
        }),
      ).rejects.toThrow('task failed')

      await sleep(10)
      expect(abortReason).toBe(errorToThrow)
    })

    it('should allow tasks to check signal.aborted', async () => {
      let wasAborted = false
      let checkCompleted = false

      await expect(
        all({
          async failing() {
            await sleep(10)
            throw new Error('failed')
          },
          async checking() {
            // Wait longer than failing task, then check abort status
            await sleep(30)
            wasAborted = this.$signal.aborted
            checkCompleted = true
            return 'done'
          },
        }),
      ).rejects.toThrow('failed')

      // Wait for checking task to complete its check
      await sleep(50)
      expect(checkCompleted).toBe(true)
      expect(wasAborted).toBe(true)
    })

    it('should propagate external signal abort to $signal', async () => {
      const controller = new AbortController()
      let internalAborted = false

      const promise = all(
        {
          async task() {
            this.$signal.addEventListener('abort', () => {
              internalAborted = true
            })
            // Check signal and throw if aborted
            await sleep(50)
            if (this.$signal.aborted) {
              throw this.$signal.reason
            }
            return 'done'
          },
        },
        { signal: controller.signal },
      )

      // Abort after a short delay
      await sleep(10)
      controller.abort(new Error('external abort'))

      await expect(promise).rejects.toThrow('external abort')
      expect(internalAborted).toBe(true)
    })

    it('should handle already aborted external signal', async () => {
      const controller = new AbortController()
      controller.abort(new Error('pre-aborted'))

      let signalAborted = false

      await expect(
        all(
          {
            async task() {
              signalAborted = this.$signal.aborted
              if (this.$signal.aborted) {
                throw this.$signal.reason
              }
              return 'done'
            },
          },
          { signal: controller.signal },
        ),
      ).rejects.toThrow('pre-aborted')

      expect(signalAborted).toBe(true)
    })

    it('should not abort other tasks until one actually fails', async () => {
      const states: string[] = []

      const result = await all({
        async a() {
          states.push('a-start')
          await sleep(20)
          states.push('a-end')
          return 1
        },
        async b() {
          states.push('b-start')
          expect(this.$signal.aborted).toBe(false)
          await sleep(10)
          expect(this.$signal.aborted).toBe(false)
          states.push('b-end')
          return 2
        },
      })

      expect(result).toEqual({ a: 1, b: 2 })
      expect(states).toContain('a-end')
      expect(states).toContain('b-end')
    })
  })

  describe('allSettled() with $signal', () => {
    it('should provide $signal as an AbortSignal', async () => {
      let receivedSignal: AbortSignal | undefined

      await allSettled({
        async a() {
          receivedSignal = this.$signal
          return 1
        },
      })

      expect(receivedSignal).toBeInstanceOf(AbortSignal)
    })

    it('should NOT abort $signal when a sibling task fails', async () => {
      const abortEvents: string[] = []

      const result = await allSettled({
        async fast() {
          throw new Error('fast failed')
        },
        async slow() {
          this.$signal.addEventListener('abort', () => {
            abortEvents.push('slow-aborted')
          })
          await sleep(30)
          return 'slow done'
        },
      })

      // Give time for any abort event to fire (it should NOT)
      await sleep(10)

      expect(result.fast.status).toBe('rejected')
      expect(result.slow).toEqual({ status: 'fulfilled', value: 'slow done' })
      expect(abortEvents).not.toContain('slow-aborted')
    })

    it('should NOT set signal.aborted when a sibling task fails', async () => {
      let wasAborted = false

      const result = await allSettled({
        async failing() {
          throw new Error('failed')
        },
        async checking() {
          await sleep(20)
          wasAborted = this.$signal.aborted
          return 'done'
        },
      })

      expect(result.failing.status).toBe('rejected')
      expect(result.checking).toEqual({ status: 'fulfilled', value: 'done' })
      expect(wasAborted).toBe(false)
    })

    it('should still propagate external signal abort to $signal', async () => {
      const controller = new AbortController()
      let internalAborted = false

      const promise = allSettled(
        {
          async task() {
            this.$signal.addEventListener('abort', () => {
              internalAborted = true
            })
            await sleep(100)
            return 'done'
          },
        },
        { signal: controller.signal },
      )

      // Abort after a short delay
      await sleep(10)
      controller.abort(new Error('external abort'))

      const result = await promise
      expect(internalAborted).toBe(true)
      // Task still completes since allSettled never rejects
      expect(result.task).toBeDefined()
    })
  })

  describe('External signal options', () => {
    it('should pass external signal reason when aborting', async () => {
      const controller = new AbortController()
      const customReason = { code: 'TIMEOUT', message: 'Request timed out' }
      let receivedReason: any

      const promise = all(
        {
          async task() {
            this.$signal.addEventListener('abort', () => {
              receivedReason = this.$signal.reason
            })
            await sleep(50)
            // Check signal and throw if aborted
            if (this.$signal.aborted) {
              throw new Error('Task aborted')
            }
            return 'done'
          },
        },
        { signal: controller.signal },
      )

      await sleep(10)
      controller.abort(customReason)

      await expect(promise).rejects.toThrow('Task aborted')
      expect(receivedReason).toBe(customReason)
    })

    it('should work without signal option (backwards compatibility)', async () => {
      const result = await all({
        async a() {
          return 1
        },
        async b() {
          return (await this.$.a) + 10
        },
      })

      expect(result).toEqual({ a: 1, b: 11 })
    })

    it('should work with signal option and dependencies', async () => {
      const controller = new AbortController()

      const result = await all(
        {
          async a() {
            return 1
          },
          async b() {
            return (await this.$.a) + 10
          },
        },
        { signal: controller.signal },
      )

      expect(result).toEqual({ a: 1, b: 11 })
    })
  })

  describe('Real-world abort scenarios', () => {
    it('should allow aborting fetch-like operations', async () => {
      // Simulate fetch with abort support
      const mockFetch = (signal: AbortSignal): Promise<string> => {
        return new Promise((resolve, reject) => {
          const timeout = setTimeout(() => resolve('data'), 100)
          signal.addEventListener('abort', () => {
            clearTimeout(timeout)
            reject(new Error('Aborted'))
          })
        })
      }

      await expect(
        all({
          async failing() {
            await sleep(10)
            throw new Error('API error')
          },
          async fetching() {
            return mockFetch(this.$signal)
          },
        }),
      ).rejects.toThrow('API error')
    })

    it('should handle multiple concurrent abort-aware tasks', async () => {
      const completedTasks: string[] = []

      const mockOperation = (
        name: string,
        signal: AbortSignal,
      ): Promise<string> => {
        return new Promise((resolve, reject) => {
          const timeout = setTimeout(() => {
            completedTasks.push(name)
            resolve(name)
          }, 50)
          signal.addEventListener('abort', () => {
            clearTimeout(timeout)
            reject(new Error(`${name} aborted`))
          })
        })
      }

      await expect(
        all({
          async failing() {
            await sleep(10)
            throw new Error('First failure')
          },
          async task1() {
            return mockOperation('task1', this.$signal)
          },
          async task2() {
            return mockOperation('task2', this.$signal)
          },
          async task3() {
            return mockOperation('task3', this.$signal)
          },
        }),
      ).rejects.toThrow('First failure')

      // None of the mock operations should have completed
      expect(completedTasks).toEqual([])
    })
  })
})

describe('flow', () => {
  describe('Early exit scenarios', () => {
    it('should exit immediately when first task calls $end()', async () => {
      const executionOrder: string[] = []

      const f = await flow<number>({
        async task1() {
          executionOrder.push('task1-start')
          this.$end(42)
          executionOrder.push('task1-after-end') // Never reached
          return 1
        },
        async task2() {
          executionOrder.push('task2-start')
          await sleep(10)
          const r = await this.$.task1 // Will throw FlowAbortedError
          executionOrder.push('task2-after-await') // Never reached
          return r + 10
        },
      })

      expect(f).toBe(42)
      expect(executionOrder).toEqual(['task1-start', 'task2-start'])
    })

    it('should handle conditional early exit', async () => {
      const getCached = async (shouldCache: boolean) => {
        return await flow<string>({
          async task1() {
            const cached = shouldCache ? 'cached-value' : null
            if (cached) this.$end(cached)
            return 'api-value'
          },
          async task2() {
            const data = await this.$.task1
            this.$end(`transformed-${data}`)
          },
        })
      }

      const cached = await getCached(true)
      expect(cached).toBe('cached-value')

      const fromApi = await getCached(false)
      expect(fromApi).toBe('transformed-api-value')
    })

    it('should support race between tasks - first $end() wins', async () => {
      const f = await flow<string>({
        async fast() {
          await sleep(10)
          this.$end('fast won')
        },
        async slow() {
          await sleep(100)
          this.$end('slow won')
        },
      })

      expect(f).toBe('fast won')
    })

    it('should support race between tasks - verify slow does not override', async () => {
      const executionOrder: string[] = []

      const f = await flow<string>({
        async fast() {
          executionOrder.push('fast-start')
          await sleep(10)
          executionOrder.push('fast-end')
          this.$end('fast won')
        },
        async slow() {
          executionOrder.push('slow-start')
          await sleep(50)
          executionOrder.push('slow-before-end')
          this.$end('slow won')
          executionOrder.push('slow-after-end') // Never reached
        },
      })

      expect(f).toBe('fast won')
      // Both should start, fast should end first
      expect(executionOrder).toContain('fast-start')
      expect(executionOrder).toContain('slow-start')
      expect(executionOrder).toContain('fast-end')
    })
  })

  describe('Dependency handling after $end()', () => {
    it('should throw FlowAbortedError when accessing dependencies after flow ends', async () => {
      const executionOrder: string[] = []

      const f = await flow<number>({
        async task1() {
          executionOrder.push('task1')
          this.$end(100)
        },
        async task2() {
          executionOrder.push('task2-start')
          await sleep(20)
          executionOrder.push('task2-before-await')
          try {
            await this.$.task1
            executionOrder.push('task2-after-await') // Never reached
          } catch (err: any) {
            executionOrder.push(`task2-caught-${err.name}`)
          }
          return 2
        },
      })

      expect(f).toBe(100)
      expect(executionOrder).toContain('task1')
      expect(executionOrder).toContain('task2-start')
      // task2 should catch FlowAbortedError but it's caught silently by flow
    })

    it('should allow tasks to complete normally if they do not depend on ended tasks', async () => {
      const f = await flow<string>({
        async task1() {
          await sleep(50)
          this.$end('first')
        },
        async task2() {
          await sleep(10)
          this.$end('second')
        },
      })

      // task2 finishes first, so its $end wins
      expect(f).toBe('second')
    })
  })

  describe('Error handling', () => {
    it('should propagate real errors (not FlowEndError)', async () => {
      await expect(
        flow<number>({
          async task1() {
            throw new Error('Real error')
          },
          async task2() {
            await sleep(10)
            this.$end(42)
          },
        })
      ).rejects.toThrow('Real error')
    })

    it('should handle errors in tasks with dependencies', async () => {
      await expect(
        flow<number>({
          async task1() {
            throw new Error('Task 1 failed')
          },
          async task2() {
            const r = await this.$.task1 // Will throw the error from task1
            this.$end(r + 1)
          },
        })
      ).rejects.toThrow('Task 1 failed')
    })
  })

  describe('Complex scenarios', () => {
    it('should handle multiple tasks with complex dependencies', async () => {
      const executionOrder: string[] = []

      const f = await flow<{ cached: boolean; data: string }>({
        async fetchUser() {
          executionOrder.push('fetchUser')
          await sleep(20)
          return { id: 1, name: 'Alice' }
        },
        async fetchPosts() {
          executionOrder.push('fetchPosts-start')
          const user = await this.$.fetchUser
          executionOrder.push(`fetchPosts-got-user-${user.id}`)
          await sleep(10)
          return [{ id: 1, title: 'Post 1' }]
        },
        async checkCache() {
          executionOrder.push('checkCache')
          await sleep(5)
          // Simulate cache hit
          this.$end({ cached: true, data: 'cached-result' })
        },
      })

      expect(f).toEqual({ cached: true, data: 'cached-result' })
      expect(executionOrder).toContain('checkCache')
      // Other tasks may or may not complete depending on timing
    })

    it('should work with $signal for cleanup', async () => {
      const abortedTasks: string[] = []

      const f = await flow<string>({
        async task1() {
          await sleep(10)
          this.$end('done')
        },
        async task2() {
          try {
            await sleep(100)
          } catch (err) {
            if (this.$signal.aborted) {
              abortedTasks.push('task2')
            }
          }
          return 'task2-done'
        },
      })

      expect(f).toBe('done')
      // Note: $signal is not automatically aborted by $end in current implementation
      // This test verifies that $signal is available
    })

    it('should handle synchronous $end() call', async () => {
      const f = await flow<number>({
        task1() {
          this.$end(123)
          return 1
        },
        async task2() {
          await sleep(10)
          return 2
        },
      })

      expect(f).toBe(123)
    })

    it('should handle early exit with complex return types', async () => {
      const f = await flow<
        { status: 'success'; data: number[] } | { status: 'error'; message: string }
      >({
        async task1() {
          await sleep(10)
          this.$end({ status: 'success', data: [1, 2, 3] })
        },
        async task2() {
          await sleep(20)
          this.$end({ status: 'error', message: 'Failed' })
        },
      })

      expect(f).toEqual({ status: 'success', data: [1, 2, 3] })
    })
  })

  describe('Type inference', () => {
    it('should require explicit type parameter', async () => {
      const f = await flow<number | string>({
        async task1() {
          this.$end(42)
          return 1
        },
        async task2() {
          this.$end('hello')
          return 'world'
        },
      })

      // f should be number | string | undefined
      expectTypeOf(f).toMatchTypeOf<number | string | undefined>()
    })
  })

  describe('Edge cases', () => {
    it('should return undefined if no task calls $end()', async () => {
      const result = await flow<number>({
        async task1() {
          return 1
        },
        async task2() {
          return 2
        },
      })
      expect(result).toBeUndefined()
    })

    it('should handle $end() with undefined value', async () => {
      const f = await flow<undefined>({
        async task1() {
          this.$end(undefined)
        },
      })

      expect(f).toBeUndefined()
    })

    it('should handle $end() with null value', async () => {
      const f = await flow<null>({
        async task1() {
          this.$end(null)
        },
      })

      expect(f).toBeNull()
    })

    it('should handle $end() with 0 value', async () => {
      const f = await flow<number>({
        async task1() {
          this.$end(0)
        },
      })

      expect(f).toBe(0)
    })

    it('should handle $end() with false value', async () => {
      const f = await flow<boolean>({
        async task1() {
          this.$end(false)
        },
      })

      expect(f).toBe(false)
    })
  })

  describe('External signal integration', () => {
    it('should respect external abort signal', async () => {
      const controller = new AbortController()

      const promise = flow<string>(
        {
          async task1() {
            // Check signal before sleeping
            if (this.$signal.aborted) throw this.$signal.reason
            await sleep(100)
            if (this.$signal.aborted) throw this.$signal.reason
            this.$end('done')
          },
          async task2() {
            if (this.$signal.aborted) throw this.$signal.reason
            await sleep(200)
            if (this.$signal.aborted) throw this.$signal.reason
            this.$end('also-done')
          },
        },
        { signal: controller.signal }
      )

      // Abort after a short delay
      setTimeout(() => controller.abort(new Error('Aborted')), 10)

      await expect(promise).rejects.toThrow('Aborted')
    })
  })
})
```

## File: `lib/index.ts`
```typescript
/**
 * Promise.all with automatic dependency optimization and full type inference
 *
 * Usage:
 * const { a, b, c } = await all({
 *   a() { return 1 },
 *   async b() { return 'hello' },
 *   async c() { return (await this.$.a) + 10 }
 * })
 */

// Extract the resolved return type from task functions
type TaskResult<T> = T extends (...args: any[]) => infer R ? Awaited<R> : never

// The $ proxy type - all task results as promises
type DepProxy<T extends Record<string, (...args: any[]) => any>> = {
  readonly [K in keyof T]: Promise<TaskResult<T[K]>>
}

// Context available to each task via `this`
type TaskContext<T extends Record<string, (...args: any[]) => any>> = {
  $: DepProxy<T>
  $signal: AbortSignal
}

// Result type - all tasks resolved to their return values
type AllResult<T extends Record<string, (...args: any[]) => any>> = {
  [K in keyof T]: TaskResult<T[K]>
}

// Settled result types for allSettled
type SettledFulfilled<T> = {
  status: 'fulfilled'
  value: T
}

type SettledRejected = {
  status: 'rejected'
  reason: any
}

type SettledResult<T> = SettledFulfilled<T> | SettledRejected

// Result type for allSettled - all tasks as settled results
type AllSettledResult<T extends Record<string, (...args: any[]) => any>> = {
  [K in keyof T]: SettledResult<TaskResult<T[K]>>
}

// Options for all() and allSettled()
type ExecutionOptions = {
  debug?: boolean
  signal?: AbortSignal
}

// Internal options for executeTasksInternal
type InternalExecutionOptions = ExecutionOptions & {
  flowMode?: boolean
}

// Tracking info for debug mode
type TaskTiming = {
  name: string
  startTime: number
  endTime: number
  duration: number
  dependencies: string[]
  status: 'fulfilled' | 'rejected'
  waitPeriods: Array<{ start: number; end: number }>
}

/**
 * Generate ASCII waterfall chart for task execution
 */
function generateWaterfallChart(timings: TaskTiming[]): string {
  if (timings.length === 0) return ''

  const startTime = Math.min(...timings.map((t) => t.startTime))
  const endTime = Math.max(...timings.map((t) => t.endTime))
  const totalDuration = endTime - startTime

  // Find longest task name for padding
  const maxNameLength = Math.max(...timings.map((t) => t.name.length))
  const maxDepsLength = Math.max(
    ...timings.map((t) =>
      t.dependencies.length > 0 ? t.dependencies.join(', ').length : 0,
    ),
    4, // minimum for "Deps" header
  )

  // Calculate scale (how many ms per character)
  const chartWidth = 60
  const scale = totalDuration / chartWidth
  const threshold = 0.5

  const totalDurationString = totalDuration.toFixed(2)

  let output = '\n'
  output +=
    '╔════════════════════════════════════════════════════════════════════════════════╗\n'
  output +=
    '║                           Task Execution Waterfall                             ║\n'
  output +=
    '╠════════════════════════════════════════════════════════════════════════════════╣\n'
  output += `║ Total Duration: ${totalDurationString}ms${' '.repeat(
    61 - totalDurationString.length,
  )}║\n`
  output +=
    '╚════════════════════════════════════════════════════════════════════════════════╝\n\n'

  // Header
  output += `${'Task'.padEnd(maxNameLength)} │ ${'Deps'.padEnd(
    maxDepsLength,
  )} │ Duration │ Timeline\n`
  output += `${'─'.repeat(maxNameLength)}─┼─${'─'.repeat(
    maxDepsLength,
  )}─┼──────────┼─${'─'.repeat(chartWidth)}\n`

  // Sort by start time
  const sortedTimings = [...timings].sort((a, b) => a.startTime - b.startTime)

  for (const timing of sortedTimings) {
    const name = timing.name.padEnd(maxNameLength)
    const deps = (
      timing.dependencies.length > 0 ? timing.dependencies.join(', ') : '-'
    ).padEnd(maxDepsLength)
    const duration = `${timing.duration.toFixed(1)}ms`.padStart(8)

    // Build timeline character by character
    const timeline: string[] = []
    const relativeStart = timing.startTime - startTime
    const relativeEnd = timing.endTime - startTime

    for (let i = 0; i < chartWidth; i++) {
      // Add threshold to avoid execution delay (i.e. 0.1ms) while the task
      // starts at the same time.
      const timePos = i * scale + threshold

      if (timePos < relativeStart || timePos >= relativeEnd) {
        // Before task starts or after task ends
        timeline.push(' ')
      } else {
        // Task is executing in this time range
        // Check if this position is in a wait period
        const absoluteTime = startTime + timePos
        const isWaiting = timing.waitPeriods.some(
          (wait) => absoluteTime >= wait.start && absoluteTime < wait.end,
        )

        if (isWaiting) {
          // Waiting on dependency
          timeline.push('░')
        } else {
          // Active execution
          timeline.push(timing.status === 'fulfilled' ? '█' : '▓')
        }
      }
    }

    output += `${name} │ ${deps} │ ${duration} │ ${timeline.join('')}\n`
  }

  output += '\n'
  output +=
    'Legend: █ = active (fulfilled), ▓ = active (rejected), ░ = waiting on dependency\n'
  output += '\n'

  return output
}

/**
 * Internal core implementation for executing tasks with automatic dependency resolution.
 * This is shared between `all`, `allSettled`, and `flow`.
 */
function executeTasksInternal<T extends Record<string, any>>(
  tasks: T,
  handleSettled: boolean,
  options: InternalExecutionOptions = {},
): Promise<any> {
  const taskNames = Object.keys(tasks) as (keyof T)[]
  const results = new Map<keyof T, any>()
  const errors = new Map<keyof T, any>()
  const resolvers = new Map<
    keyof T,
    [(value: any) => void, (reason?: any) => void][]
  >()
  const returnValue: Record<string, any> = {}

  // Flow mode tracking
  let flowEnded = false
  let flowEndValue: any = undefined

  // Create internal abort controller for auto-abort on failure and external signal propagation
  const internalController = new AbortController()

  // Controller to manage cleanup of the external signal listener
  const cleanupController = new AbortController()

  // If external signal is provided, propagate its abort to internal controller
  if (options.signal) {
    if (options.signal.aborted) {
      internalController.abort(options.signal.reason)
    } else {
      options.signal.addEventListener(
        'abort',
        () => internalController.abort(options.signal!.reason),
        { once: true, signal: cleanupController.signal },
      )
    }
  }

  // Debug tracking
  const timings: TaskTiming[] = []
  const taskStartTimes = new Map<keyof T, number>()
  const taskDependencies = new Map<keyof T, Set<string>>()
  const taskWaitPeriods = new Map<
    keyof T,
    Array<{ start: number; end: number }>
  >()

  const waitForDep = (taskName: keyof T, depName: keyof T): Promise<any> => {
    if (!(depName in tasks)) {
      return Promise.reject(new Error(`Unknown task "${String(depName)}"`))
    }

    // In flow mode, if flow has ended, reject with FlowAbortedError
    if (options.flowMode && flowEnded) {
      return Promise.reject(new FlowAbortedError())
    }

    // Track dependency for debug mode
    if (options.debug) {
      if (!taskDependencies.has(taskName)) {
        taskDependencies.set(taskName, new Set())
      }
      taskDependencies.get(taskName)!.add(String(depName))
    }

    let basePromise: Promise<any>

    if (results.has(depName)) {
      basePromise = Promise.resolve(results.get(depName))
    } else if (errors.has(depName)) {
      basePromise = Promise.reject(errors.get(depName))
    } else {
      basePromise = new Promise((resolve, reject) => {
        if (!resolvers.has(depName)) {
          resolvers.set(depName, [])
        }
        resolvers.get(depName)!.push([resolve, reject])
      })
    }

    // Wrap promise to track wait time in debug mode
    if (options.debug) {
      const waitStart = performance.now()
      return basePromise.then(
        (value) => {
          const waitEnd = performance.now()
          if (!taskWaitPeriods.has(taskName)) {
            taskWaitPeriods.set(taskName, [])
          }
          taskWaitPeriods
            .get(taskName)!
            .push({ start: waitStart, end: waitEnd })
          return value
        },
        (error) => {
          const waitEnd = performance.now()
          if (!taskWaitPeriods.has(taskName)) {
            taskWaitPeriods.set(taskName, [])
          }
          taskWaitPeriods
            .get(taskName)!
            .push({ start: waitStart, end: waitEnd })
          throw error
        },
      )
    }

    return basePromise
  }

  const handleResult = (name: keyof T, value: any) => {
    results.set(name, value)
    if (handleSettled) {
      returnValue[name as string] = { status: 'fulfilled', value }
    } else if (!options.flowMode) {
      returnValue[name as string] = value
    }
    if (resolvers.has(name)) {
      for (const [resolve] of resolvers.get(name)!) {
        resolve(value)
      }
    }
  }

  const handleError = (name: keyof T, err: any) => {
    errors.set(name, err)
    if (handleSettled) {
      returnValue[name as string] = { status: 'rejected', reason: err }
    }
    if (resolvers.has(name)) {
      for (const [, reject] of resolvers.get(name)!) {
        reject(err)
      }
    }
  }

  // Run all tasks in parallel
  const promises = taskNames.map(async (name) => {
    try {
      const taskFn = tasks[name]
      if (typeof taskFn !== 'function') {
        throw new Error(`Task "${String(name)}" is not a function`)
      }

      // Track start time for debug mode
      if (options.debug) {
        taskStartTimes.set(name, performance.now())
      }

      // Create a unique dep proxy for each task to track dependencies
      const depProxy = new Proxy({} as DepProxy<T>, {
        get(_, depName: string) {
          return waitForDep(name, depName as keyof T)
        },
      })

      // Create $end function for flow mode
      const $end = options.flowMode
        ? (value: any): never => {
            if (!flowEnded) {
              flowEnded = true
              flowEndValue = value
            }
            throw new FlowEndError(value)
          }
        : undefined

      const context: any = {
        $: depProxy,
        $signal: internalController.signal,
      }

      if (options.flowMode && $end) {
        context.$end = $end
      }

      const result = await taskFn.call(context)

      // Track end time and create timing record
      if (options.debug) {
        const endTime = performance.now()
        const startTime = taskStartTimes.get(name)!
        timings.push({
          name: String(name),
          startTime,
          endTime,
          duration: endTime - startTime,
          dependencies: Array.from(taskDependencies.get(name) || []),
          status: 'fulfilled',
          waitPeriods: taskWaitPeriods.get(name) || [],
        })
      }

      handleResult(name, result)
    } catch (err) {
      // In flow mode, handle FlowEndError and FlowAbortedError specially
      if (options.flowMode) {
        if (err instanceof FlowEndError) {
          // This is intentional early exit, don't propagate as error
          return
        }
        if (err instanceof FlowAbortedError) {
          // Flow was ended by another task, silently ignore
          return
        }
      }

      // Track end time for failed tasks too
      if (options.debug) {
        const endTime = performance.now()
        const startTime = taskStartTimes.get(name)!
        timings.push({
          name: String(name),
          startTime,
          endTime,
          duration: endTime - startTime,
          dependencies: Array.from(taskDependencies.get(name) || []),
          status: 'rejected',
          waitPeriods: taskWaitPeriods.get(name) || [],
        })
      }

      handleError(name, err)
      if (!handleSettled) {
        // Abort other tasks when one fails (only for all(), not allSettled())
        internalController.abort(err)
        throw err
      }
    }
  })

  const finalPromise = options.flowMode
    ? // For flow mode, use allSettled and handle flow end
      Promise.allSettled(promises).then((results) => {
        cleanupController.abort()

        // Check if external signal was aborted
        if (options.signal?.aborted) {
          throw options.signal.reason || new Error('Aborted')
        }

        // Check if any task had a real error
        for (const result of results) {
          if (result.status === 'rejected') {
            throw result.reason
          }
        }

        // If flow ended early, return that value
        if (flowEnded) {
          return flowEndValue
        }

        // No task called $end() - return undefined
        return undefined
      })
    : handleSettled
      ? // For allSettled, wait for all promises to settle (never rejects)
        Promise.allSettled(promises).then(() => returnValue)
      : // For all, reject on first error (like Promise.all)
        Promise.all(promises).then(() => returnValue)

  // Cleanup external signal listener when tasks complete
  const withCleanup = options.flowMode
    ? finalPromise
    : finalPromise.finally(() => {
        cleanupController.abort()
      })

  // Output waterfall chart in debug mode
  if (options.debug) {
    return withCleanup.then(
      (result) => {
        console.log(generateWaterfallChart(timings))
        return result
      },
      (error) => {
        console.log(generateWaterfallChart(timings))
        throw error
      },
    )
  }

  return withCleanup
}

/**
 * Execute tasks with automatic dependency resolution.
 *
 * @example
 * const { a, b, c } = await all({
 *   async a() { return 1 },
 *   async b() { return 'hello' },
 *   async c() { return (await this.$.a) + 10 }
 * })
 *
 * @example
 * // With debug mode
 * const result = await all({
 *   async a() { return 1 },
 *   async b() { return (await this.$.a) + 10 }
 * }, { debug: true })
 *
 * @example
 * // With auto-abort on failure - this.$signal is aborted when any sibling task fails
 * const result = await all({
 *   async a() { return fetchWithSignal(this.$signal) },
 *   async b() { throw new Error('fails') }, // This will abort tasks a and c
 *   async c() { return fetchWithSignal(this.$signal) }
 * })
 *
 * @example
 * // With external signal
 * const controller = new AbortController()
 * const result = await all({
 *   async a() { return fetchWithSignal(this.$signal) }
 * }, { signal: controller.signal })
 */
export function all<T extends Record<string, any>>(
  tasks: T &
    ThisType<{
      $: {
        [K in keyof T]: ReturnType<T[K]> extends Promise<infer R>
          ? Promise<R>
          : Promise<ReturnType<T[K]>>
      }
      $signal: AbortSignal
    }> & {
      [K in keyof T as T[K] extends Function
        ? K
        : `Error: task \`${K & string}\` is not a function`]-?: T[K]
    },
  options?: ExecutionOptions,
): Promise<AllResult<T>> {
  return executeTasksInternal(tasks, false, options) as Promise<AllResult<T>>
}

/**
 * Execute tasks with automatic dependency resolution, returning settled results for all tasks.
 * Unlike `all`, this will never reject - failed tasks will be included in the result with their error.
 *
 * @example
 * const { a, b, c } = await allSettled({
 *   async a() { return 1 },
 *   async b() { throw new Error('failed') },
 *   async c() { return (await this.$.a) + 10 }
 * })
 * // a: { status: 'fulfilled', value: 1 }
 * // b: { status: 'rejected', reason: Error('failed') }
 * // c: { status: 'fulfilled', value: 11 }
 *
 * @example
 * // With debug mode
 * const result = await allSettled({
 *   async a() { return 1 },
 *   async b() { throw new Error('failed') }
 * }, { debug: true })
 */
export function allSettled<T extends Record<string, any>>(
  tasks: T &
    ThisType<{
      $: {
        [K in keyof T]: ReturnType<T[K]> extends Promise<infer R>
          ? Promise<R>
          : Promise<ReturnType<T[K]>>
      }
      $signal: AbortSignal
    }> & {
      [P in keyof T]: T[P] extends (...args: any[]) => any ? T[P] : never
    },
  options?: ExecutionOptions,
): Promise<AllSettledResult<T>> {
  return executeTasksInternal(tasks, true, options) as Promise<
    AllSettledResult<T>
  >
}

/**
 * Custom error class for early exit via $end()
 * @internal
 */
class FlowEndError extends Error {
  constructor(public readonly value: any) {
    super('Flow ended early')
    this.name = 'FlowEndError'
  }
}

/**
 * Custom error class for aborted dependency access
 * @internal
 */
class FlowAbortedError extends Error {
  constructor() {
    super('Flow has been ended, cannot access dependencies')
    this.name = 'FlowAbortedError'
  }
}

// Context available to each task in flow via `this`
type FlowTaskContext<
  T extends Record<string, (...args: any[]) => any>,
  R,
> = {
  $: DepProxy<T>
  $signal: AbortSignal
  $end: (value: R) => never
}

/**
 * Execute tasks with automatic dependency resolution and support for early exit.
 * The first task to call `this.$end(value)` determines the return value.
 *
 * @example
 * // Early exit from first task
 * const f = await flow<number>({
 *   async task1() {
 *     this.$end(42)  // Immediately ends, f = 42
 *     return 1       // Never reached
 *   },
 *   async task2() {
 *     const r = await this.$.task1  // Throws (silently caught)
 *     return r + 10
 *   },
 * })
 * // f = 42
 *
 * @example
 * // Conditional early exit
 * const f = await flow<string>({
 *   async task1() {
 *     const cached = await checkCache()
 *     if (cached) this.$end(cached)  // Early exit if cached
 *     return await fetchFromApi()
 *   },
 *   async task2() {
 *     const data = await this.$.task1
 *     this.$end(transform(data))
 *   },
 * })
 *
 * @example
 * // Race between tasks
 * const f = await flow<string>({
 *   async fast() {
 *     await sleep(100)
 *     this.$end('fast won')
 *   },
 *   async slow() {
 *     await sleep(1000)
 *     this.$end('slow won')
 *   },
 * })
 * // f = 'fast won'
 */
export function flow<R, T extends Record<string, any> = Record<string, any>>(
  tasks: T &
    ThisType<{
      $: {
        [K in keyof T]: ReturnType<T[K]> extends Promise<infer U>
          ? Promise<U>
          : Promise<ReturnType<T[K]>>
      }
      $signal: AbortSignal
      $end: (value: R) => never
    }> & {
      [K in keyof T as T[K] extends Function
        ? K
        : `Error: task \`${K & string}\` is not a function`]-?: T[K]
    },
  options?: ExecutionOptions,
): Promise<R | undefined> {
  return executeTasksInternal(tasks, false, {
    ...options,
    flowMode: true,
  }) as Promise<R | undefined>
}
```

## File: `src/index.ts`
```typescript
export { all, allSettled, flow } from '../lib/index'
```

