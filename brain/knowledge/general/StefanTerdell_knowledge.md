---
id: stefanterdell-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:17.263952
---

# KNOWLEDGE EXTRACT: StefanTerdell
> **Extracted on:** 2026-03-30 17:54:06
> **Source:** StefanTerdell

---

## File: `json-schema-to-zod.md`
```markdown
# 📦 StefanTerdell/json-schema-to-zod [🔖 PENDING/APPROVE]
🔗 https://github.com/StefanTerdell/json-schema-to-zod


## Meta
- **Stars:** ⭐ 525 | **Forks:** 🍴 71
- **Language:** TypeScript | **License:** ISC
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Json-Schema-to-Zod

[![NPM Version](https://img.shields.io/npm/v/json-schema-to-zod.svg)](https://npmjs.org/package/json-schema-to-zod)
[![NPM Downloads](https://img.shields.io/npm/dw/json-schema-to-zod.svg)](https://npmjs.org/package/json-schema-to-zod)

# Notice of (pending) deprecation

I'm waiting for a response regarding the Zod v4 support PR. After that has been merged, a final version of this package will be released, and this repo will be archived.

_Please do not open any new issues or pull requests as I'm not likely to attend to them._

## Summary

A runtime package and CLI tool to convert JSON schema (draft 4+) objects or files into Zod schemas in the form of JavaScript code.

Before v2 it used [`prettier`](https://www.npmjs.com/package/prettier) for formatting and [`json-refs`](https://www.npmjs.com/package/json-refs) to resolve schemas. To replicate the previous behaviour, please use their respective CLI tools.

Since v2 the CLI supports piped JSON.

_Looking for the exact opposite? Check out [zod-to-json-schema](https://npmjs.org/package/zod-to-json-schema)_

## Usage

### Online

[Just paste your JSON schemas here!](https://stefanterdell.github.io/json-schema-to-zod-react/)

### CLI

#### Simplest example

```console
npm i -g json-schema-to-zod
```

```console
json-schema-to-zod -i mySchema.json -o mySchema.ts
```

#### Example with `$refs` resolved and output formatted

```console
npm i -g json-schema-to-zod json-refs prettier
```

```console
json-refs resolve mySchema.json | json-schema-to-zod | prettier --parser typescript > mySchema.ts
```

#### Options

| Flag           | Shorthand | Function                                                                                       |
| -------------- | --------- | ---------------------------------------------------------------------------------------------- |
| `--input`      | `-i`      | JSON or a source file path. Required if no data is piped.                                      |
| `--output`     | `-o`      | A file path to write to. If not supplied stdout will be used.                                  |
| `--name`       | `-n`      | The name of the schema in the output                                                           |
| `--depth`      | `-d`      | Maximum depth of recursion in schema before falling back to `z.any()`. Defaults to 0.          |
| `--module`     | `-m`      | Module syntax; `esm`, `cjs` or none. Defaults to `esm` in the CLI and `none` programmaticly.   |
| `--type`       | `-t`      | Export a named type along with the schema. Requires `name` to be set and `module` to be `esm`. |
| `--noImport`   | `-ni`     | Removes the `import { z } from 'zod';` or equivalent from the output.                          |
| `--withJsdocs` | `-wj`     | Generate jsdocs off of the description property.                                               |

### Programmatic

#### Simple example

```typescript
import { jsonSchemaToZod } from "json-schema-to-zod";

const myO
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

