---
id: shuding-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.624808
---

# KNOWLEDGE EXTRACT: shuding
> **Extracted on:** 2026-03-30 17:53:20
> **Source:** shuding

---

## File: `better-all.md`
```markdown
# 📦 shuding/better-all [🔖 PENDING/APPROVE]
🔗 https://github.com/shuding/better-all


## Meta
- **Stars:** ⭐ 1039 | **Forks:** 🍴 18
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Better Promise.all with automatic dependency optimization

## README (trích đầu)
```
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
- **No hanging promise
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

