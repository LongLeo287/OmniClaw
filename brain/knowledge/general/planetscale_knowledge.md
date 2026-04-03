---
id: planetscale-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:30:59.428934
---

# KNOWLEDGE EXTRACT: planetscale
> **Extracted on:** 2026-03-30 17:51:03
> **Source:** planetscale

---

## File: `database-js.md`
```markdown
# 📦 planetscale/database-js [🔖 PENDING/APPROVE]
🔗 https://github.com/planetscale/database-js
🌐 https://planetscale.com/docs/tutorials/planetscale-serverless-driver

## Meta
- **Stars:** ⭐ 1192 | **Forks:** 🍴 41
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Fetch API-compatible PlanetScale database driver

## README (trích đầu)
```
![PlanetScale serverless driver for JavaScript](https://github.com/planetscale/database-js/assets/440926/0dfab33f-b01f-4814-ae40-c5fe5cbe94e3)

# PlanetScale serverless JavaScript driver for Vitess/MySQL

A Fetch API-compatible PlanetScale Vitess/MySQL database driver for serverless and edge compute platforms that require HTTP external connections, such as Cloudflare Workers or Vercel Edge Functions

> [!TIP]
> Connecting to a PlanetScale Postgres database? We support the Neon serverless driver, [read the documentation](https://planetscale.com/docs/postgres/connecting/neon-serverless-driver) to connect.

## Installation

```sh
npm install @planetscale/database
```

## Usage

```ts
import { connect } from '@planetscale/database'

const config = {
  host: '<host>',
  username: '<user>',
  PASSWORD='[REDACTED_PASSWORD]'
}

const conn = connect(config)
const results = await conn.execute('select 1 from dual where 1=?', [1])
console.log(results)
```

### Database URL

A single database URL value can be used to configure the `host`, `username`, and `password` values.

```ts
import { connect } from '@planetscale/database'

const config = {
  url: process.env['DATABASE_URL'] || 'mysql://user:pass@host'
}

const conn = connect(config)
```

### Connection factory

Use the `Client` connection factory class to create fresh connections for each transaction or web request handler.

```ts
import { Client } from '@planetscale/database'

const client = new Client({
  host: '<host>',
  username: '<user>',
  PASSWORD='[REDACTED_PASSWORD]'
})

const conn = client.connection()
const results = await conn.execute('select 1 from dual')
console.log(results)
```

### Transactions

Use the `transaction` function to safely perform database transactions. If any unhandled errors are thrown during execution of the transaction, the transaction will be rolled back.

The following example is based on [the Slotted Counter Pattern](https://planetscale.com/blog/the-slotted-counter-pattern).

```ts
import { connect } from '@planetscale/database'

const config = {
  host: '<host>',
  username: '<user>',
  PASSWORD='[REDACTED_PASSWORD]'
}

const conn = connect(config)
const results = await conn.transaction(async (tx) => {
  const whenBranch = await tx.execute('INSERT INTO branches (database_id, name) VALUES (?, ?)', [42, "planetscale"])
  const whenCounter = await tx.execute('INSERT INTO slotted_counters(record_type, record_id, slot, count) VALUES (?, ?, RAND() * 100, 1) ON DUPLICATE KEY UPDATE count = count + 1', ['branch_count', 42])
  return [whenBranch, whenCounter]
})
console.log(results)
```

### Custom fetch function

Node.js version 18 includes a built-in global `fetch` function. When using an older version of Node.js, you can provide a custom fetch function implementation. We recommend the [`undici`][1] package on which Node's built-in fetch is based.

[1]: https://github.com/nodejs/undici

```ts
import { connect } from '@planetscale/database'
import { fetch } from 'undici'

const config = {
  fetch,

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

