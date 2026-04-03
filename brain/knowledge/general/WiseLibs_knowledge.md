---
id: wiselibs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:46.531780
---

# KNOWLEDGE EXTRACT: WiseLibs
> **Extracted on:** 2026-03-30 18:01:18
> **Source:** WiseLibs

---

## File: `better-sqlite3.md`
```markdown
# 📦 WiseLibs/better-sqlite3 [🔖 PENDING/APPROVE]
🔗 https://github.com/WiseLibs/better-sqlite3


## Meta
- **Stars:** ⭐ 7047 | **Forks:** 🍴 451
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The fastest and simplest library for SQLite3 in Node.js.

## README (trích đầu)
```
# better-sqlite3 [![Build Status](https://github.com/JoshuaWise/better-sqlite3/actions/workflows/build.yml/badge.svg)](https://github.com/JoshuaWise/better-sqlite3/actions/workflows/build.yml?query=branch%3Amaster)

The fastest and simplest library for SQLite in Node.js.

- Full transaction support
- High performance, efficiency, and safety
- Easy-to-use synchronous API *(better concurrency than an asynchronous API... yes, you read that correctly)*
- Support for user-defined functions, aggregates, virtual tables, and extensions
- 64-bit integers *(invisible until you need them)*
- Worker thread support *(for large/slow queries)*

## Help this project stay strong! &#128170;

`better-sqlite3` is used by thousands of developers and engineers on a daily basis. Long nights and weekends were spent keeping this project strong and dependable, with no ask for compensation or funding, until now. If your company uses `better-sqlite3`, ask your manager to consider supporting the project:

- [Become a GitHub sponsor](https://github.com/sponsors/JoshuaWise)
- [Become a backer on Patreon](https://www.patreon.com/joshuawise)
- [Make a one-time donation on PayPal](https://www.paypal.me/joshuathomaswise)

## How other libraries compare

|   |select 1 row &nbsp;`get()`&nbsp;|select 100 rows &nbsp;&nbsp;`all()`&nbsp;&nbsp;|select 100 rows `iterate()` 1-by-1|insert 1 row `run()`|insert 100 rows in a transaction|
|---|---|---|---|---|---|
|better-sqlite3|1x|1x|1x|1x|1x|
|[sqlite](https://www.npmjs.com/package/sqlite) and [sqlite3](https://www.npmjs.com/package/sqlite3)|11.7x slower|2.9x slower|24.4x slower|2.8x slower|15.6x slower|

> You can verify these results by [running the benchmark yourself](./docs/benchmark.md).

## Installation

```bash
npm install better-sqlite3
```

> Requires a [currently supported Node.js](https://nodejs.org/en/about/previous-releases) version. Prebuilt binaries are available for [LTS versions](https://nodejs.org/en/about/previous-releases). If you have trouble installing, check the [troubleshooting guide](./docs/troubleshooting.md).

## Usage

```js
const db = require('better-sqlite3')('foobar.db', options);

const row = db.prepare('SELECT * FROM users WHERE id = ?').get(userId);
console.log(row.firstName, row.lastName, row.email);
```

Though not required, [it is generally important to set the WAL pragma for performance reasons](https://github.com/WiseLibs/better-sqlite3/blob/master/docs/performance.md).

```js
db.pragma('journal_mode = WAL');
```

##### In ES6 module notation:

```js
import Database from 'better-sqlite3';
const db = new Database('foobar.db', options);
db.pragma('journal_mode = WAL');
```

## Why should I use this instead of [node-sqlite3](https://github.com/mapbox/node-sqlite3)?

- `node-sqlite3` uses asynchronous APIs for tasks that are either CPU-bound or serialized. That's not only bad design, but it wastes tons of resources. It also causes [mutex thrashing](https://en.wikipedia.org/wiki/Resource_contention) which h
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

