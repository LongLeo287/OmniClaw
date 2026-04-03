---
id: gajus-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.822936
---

# KNOWLEDGE EXTRACT: gajus
> **Extracted on:** 2026-03-30 17:37:23
> **Source:** gajus

---

## File: `slonik.md`
```markdown
# 📦 gajus/slonik [🔖 PENDING/APPROVE]
🔗 https://github.com/gajus/slonik


## Meta
- **Stars:** ⭐ 4895 | **Forks:** 🍴 155
- **Language:** TypeScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Node.js PostgreSQL client with runtime and build time type safety, and composable SQL.

## README (trích đầu)
```
# Slonik

[![NPM version](http://img.shields.io/npm/v/slonik.svg?style=flat-square)](https://www.npmjs.org/package/slonik)
[![Canonical Code Style](https://img.shields.io/badge/code%20style-canonical-blue.svg?style=flat-square)](https://github.com/gajus/canonical)
[![Twitter Follow](https://img.shields.io/twitter/follow/kuizinas.svg?style=social&label=Follow)](https://twitter.com/kuizinas)

A [battle-tested](#battle-tested) Node.js PostgreSQL client with strict types, detailed logging and assertions.

> [!NOTE]
> NEW! Use Slonik with [`eslint-plugin-slonik`](https://github.com/gajus/eslint-plugin-slonik) to validate your SQL queries against your database schema.

![Tailing Slonik logs](./.README/slonik-log-tailing.gif)

(The above GIF shows Slonik producing [query logs](https://github.com/gajus/slonik#logging). Slonik produces logs using [Roarr](https://github.com/gajus/roarr). Logs include stack trace of the actual query invocation location and values used to execute the query.)

## Sponsors

If you value my work and want to see Slonik and [many other of my](https://github.com/gajus/) Open-Source projects to be continuously improved, then please consider becoming a patron:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/gajus)
[![Become a Patron](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/gajus)

## Principles

- Promotes writing raw SQL.
- Discourages ad-hoc dynamic generation of SQL.

Read: [Stop using Knex.js](https://medium.com/@gajus/bf410349856c)

Note: Using this project does not require TypeScript. It is a regular ES6 module. Ignore the type definitions used in the documentation if you do not use a type system.

## Features

- [Runtime validation](#runtime-validation).
- [Assertions and type safety](#repeating-code-patterns-and-type-safety).
- [Safe connection handling](#protecting-against-unsafe-connection-handling).
- [Safe transaction handling](#protecting-against-unsafe-transaction-handling).
- [Safe value interpolation](#protecting-against-unsafe-value-interpolation).
- [Transaction nesting](#transaction-nesting).
- [Transaction events](#transaction-events).
- [Transaction retrying](#transaction-retrying).
- [Query retrying](#query-retrying).
- Detailed [logging](#debugging).
- [Asynchronous stack trace resolution](#capture-stack-trace).
- [Middlewares](#interceptors).
- [Mapped errors](#error-handling).
- [ESLint plugin](https://github.com/gajus/eslint-plugin-sql).

## Contents

- [Slonik](#slonik)
  - [Sponsors](#sponsors)
  - [Principles](#principles)
  - [Features](#features)
  - [Contents](#contents)
  - [About Slonik](#about-slonik)
    - [Battle-Tested](#battle-tested)
    - [Origin of the name](#origin-of-the-name)
    - [Repeating code patterns and type safety](#repeating-code-patterns-and-type-safety)
    - [Protecting against unsafe connection handling](#protecting-against-unsafe-connection-handling)
   
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

