---
id: privatenumber-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:01.984379
---

# KNOWLEDGE EXTRACT: privatenumber
> **Extracted on:** 2026-03-30 17:51:09
> **Source:** privatenumber

---

## File: `get-tsconfig.md`
```markdown
# 📦 privatenumber/get-tsconfig [🔖 PENDING/APPROVE]
🔗 https://github.com/privatenumber/get-tsconfig


## Meta
- **Stars:** ⭐ 242 | **Forks:** 🍴 19
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Lightweight tsconfig.json parser & paths resolver

## README (trích đầu)
```
<p align="center">
	<img width="160" src=".github/logo.webp">
</p>
<h1 align="center">
	<sup>get-tsconfig</sup>
	<br>
	<a href="https://npm.im/get-tsconfig"><img src="https://badgen.net/npm/v/get-tsconfig"></a> <a href="https://npm.im/get-tsconfig"><img src="https://badgen.net/npm/dm/get-tsconfig"></a>
</h1>

Find and parse `tsconfig.json` files.

### Features
- Zero dependency (not even TypeScript)
- Tested against TypeScript for correctness
- Supports comments & dangling commas in `tsconfig.json`
- Resolves [`extends`](https://www.typescriptlang.org/tsconfig/#extends)
- Fully typed `tsconfig.json`
- Validates and throws parsing errors
- Tiny! `7 kB` Minified + Gzipped

<br>

<p align="center">
	<a href="https://github.com/sponsors/privatenumber/sponsorships?tier_id=398771"><img width="412" src="https://raw.githubusercontent.com/privatenumber/sponsors/master/banners/assets/donate.webp"></a>
	<a href="https://github.com/sponsors/privatenumber/sponsorships?tier_id=397608"><img width="412" src="https://raw.githubusercontent.com/privatenumber/sponsors/master/banners/assets/sponsor.webp"></a>
</p>
<p align="center"><sup><i>Already a sponsor?</i> Join the discussion in the <a href="https://github.com/pvtnbr/get-tsconfig">Development repo</a>!</sup></p>

## Install

```bash
npm install get-tsconfig
```

## Why?
For TypeScript related tooling to correctly parse `tsconfig.json` file without depending on TypeScript.

## API

### getTsconfig(searchPath?, configName?, cache?)

Searches for a tsconfig file (defaults to `tsconfig.json`) in the `searchPath` and parses it. (If you already know the tsconfig path, use [`parseTsconfig`](#parsetsconfigtsconfigpath-cache) instead). Returns `null` if a config file cannot be found, or an object containing the path and parsed TSConfig object if found.

Returns:

```ts
type TsconfigResult = {

    /**
     * The path to the tsconfig.json file
     */
    path: string

    /**
     * The resolved tsconfig.json file
     */
    config: TsConfigJsonResolved
}
```

#### searchPath
Type: `string`

Default: `process.cwd()`

Accepts a path to a file or directory to search up for a `tsconfig.json` file.

#### configName
Type: `string`

Default: `tsconfig.json`

The file name of the TypeScript config file.

#### cache
Type: `Map<string, any>`

Default: `new Map()`

Optional cache for fs operations.

#### Example

```ts
import { getTsconfig } from 'get-tsconfig'

// Searches for tsconfig.json starting in the current directory
console.log(getTsconfig())

// Find tsconfig.json from a TypeScript file path
console.log(getTsconfig('./path/to/index.ts'))

// Find tsconfig.json from a directory file path
console.log(getTsconfig('./path/to/directory'))

// Explicitly pass in tsconfig.json path
console.log(getTsconfig('./path/to/tsconfig.json'))

// Search for jsconfig.json - https://code.visualstudio.com/docs/languages/jsconfig
console.log(getTsconfig('.', 'jsconfig.json'))
```

---

### parseTsconfig(tsconfigPath, cache?)

Parse the tsc
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `resolve-pkg-maps.md`
```markdown
# 📦 privatenumber/resolve-pkg-maps [🔖 PENDING/APPROVE]
🔗 https://github.com/privatenumber/resolve-pkg-maps


## Meta
- **Stars:** ⭐ 61 | **Forks:** 🍴 5
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2025-11-27
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Resolve package.json `exports` & `imports` maps

## README (trích đầu)
```
# resolve-pkg-maps

Utils to resolve `package.json` subpath & conditional [`exports`](https://nodejs.org/api/packages.html#exports)/[`imports`](https://nodejs.org/api/packages.html#imports) in resolvers.

Implements the [ESM resolution algorithm](https://nodejs.org/api/esm.html#resolver-algorithm-specification). Tested [against Node.js](/tests/) for accuracy.

<sub>Support this project by ⭐️ starring and sharing it. [Follow me](https://github.com/privatenumber) to see what other cool projects I'm working on! ❤️</sub>

## Usage

### Resolving `exports`

_utils/package.json_
```json5
{
    // ...
    "exports": {
        "./reverse": {
            "require": "./file.cjs",
            "default": "./file.mjs"
        }
    },
    // ...
}
```

```ts
import { resolveExports } from 'resolve-pkg-maps'

const [packageName, packageSubpath] = parseRequest('utils/reverse')

const resolvedPaths: string[] = resolveExports(
    getPackageJson(packageName).exports,
    packageSubpath,
    ['import', ...otherConditions]
)
// => ['./file.mjs']
```

### Resolving `imports`

_package.json_
```json5
{
    // ...
    "imports": {
        "#supports-color": {
            "node": "./index.js",
            "default": "./browser.js"
        }
    },
    // ...
}
```

```ts
import { resolveImports } from 'resolve-pkg-maps'

const resolvedPaths: string[] = resolveImports(
    getPackageJson('.').imports,
    '#supports-color',
    ['node', ...otherConditions]
)
// => ['./index.js']
```

## API

### resolveExports(exports, request, conditions)

Returns: `string[]`

Resolves the `request` based on `exports` and `conditions`. Returns an array of paths (e.g. in case a fallback array is matched).

#### exports

Type:
```ts
type Exports = PathOrMap | readonly PathOrMap[]

type PathOrMap = string | PathConditionsMap

type PathConditionsMap = {
    [condition: string]: PathConditions | null
}
```

The [`exports` property](https://nodejs.org/api/packages.html#exports) value in `package.json`.

#### request

Type: `string`

The package subpath to resolve. Assumes a normalized path is passed in (eg. [repeating slashes `//`](https://github.com/nodejs/node/issues/44316)).

It _should not_ start with `/` or `./`.

Example: if the full import path is `some-package/subpath/file`, the request is `subpath/file`.


#### conditions

Type: `readonly string[]`

An array of conditions to use when resolving the request. For reference, Node.js's default conditions are [`['node', 'import']`](https://nodejs.org/api/esm.html#:~:text=defaultConditions%20is%20the%20conditional%20environment%20name%20array%2C%20%5B%22node%22%2C%20%22import%22%5D.).

The order of this array does not matter; the order of condition keys in the export map is what matters instead.

Not all conditions in the array need to be met to resolve the request. It just needs enough to resolve to a path.

---

### resolveImports(imports, request, conditions)

Returns: `string[]`

Resolves the `request` based on `imports` and `condition
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

