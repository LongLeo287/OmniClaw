---
id: bgub-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:57.755582
---

# KNOWLEDGE EXTRACT: bgub
> **Extracted on:** 2026-03-30 17:30:49
> **Source:** bgub

---

## File: `eta.md`
```markdown
# 📦 bgub/eta [🔖 PENDING/APPROVE]
🔗 https://github.com/bgub/eta
🌐 https://eta.js.org

## Meta
- **Stars:** ⭐ 1689 | **Forks:** 🍴 89
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Embedded JS template engine for Node, Deno, and the browser. Lighweight, fast, and pluggable. Written in TypeScript

## README (trích đầu)
```
<p align="center">
  <img align="center" width="50%" src="https://github.com/bgub/eta/assets/25597854/041dbe34-883b-459b-8607-c787815c441a">
</p>

<h1 align="center" style="text-align: center; width: fit-content; margin-left: auto; margin-right: auto;">eta (η)</h1>

<p align="center">
  <a href="https://eta.js.org">Documentation</a> -
  <a href="https://discord.gg/27gGncJYE2">Chat</a> -
  <a href="https://eta.js.org/playground">Playground</a>
</p>

<span align="center">

[![GitHub package.json version (main)](https://img.shields.io/github/package-json/v/bgub/eta/main?label=current%20version)](https://www.npmjs.com/package/eta)
[![GitHub Actions Status](https://github.com/bgub/eta/actions/workflows/ci.yml/badge.svg)](https://github.com/bgub/eta/actions)
[![Codecov](https://codecov.io/github/bgub/eta/branch/main/graph/badge.svg)](https://codecov.io/github/bgub/eta)
[![Donate](https://img.shields.io/badge/donate-paypal-blue.svg)](https://paypal.me/bengubler)

</span>

<span align="center">

**You're viewing the source for Eta v4**

</span>

## Summary

Eta is a lightweight and blazing fast embedded JS templating engine that works inside Node, Deno, and the browser. It's written in TypeScript and emphasizes great performance, configurability, and small bundle size.

> 🎯 **Built with [ts-base](https://github.com/bgub/ts-base)** — A TypeScript library starter template featuring Biome, Vitest, tsdown, and automated releases. Check out ts-base for a modern TypeScript project setup!

### 🌟 Features

- 📦 0 dependencies
- 💡 Only ~3.5 KB minzipped
- ⚡️ Written in TypeScript
- ✨ Deno support (+ Node and browser)
- 🚀 Super Fast
- 🔧 Configurable
  - Plugins, custom delimiters, caching
- 🔨 Powerful
  - Precompilation, partials, async
  - **Layout support**!
- 🔥 Reliable
  - Better quotes/comments support
    - _ex._ `<%= someval + "string %>" %>` compiles correctly, while it fails with doT or EJS
  - Great error reporting
- ⚡️ Exports ES Modules
- 📝 Easy template syntax

## Get Started

_For more thorough documentation, visit [https://eta.js.org](https://eta.js.org)_

Install Eta

```bash
npm install eta
```

In the root of your project, create `templates/simple.eta`

```eta
Hi <%= it.name %>!
```

Then, in your JS file:

```js
import { Eta } from "eta";
// or use https://jsr.io/@bgub/eta

const eta = new Eta({ views: path.join(__dirname, "templates") });

// Render a template

const res = eta.render("./simple", { name: "Ben" });
console.log(res); // Hi Ben!
```

## FAQs

<details>
  <summary>
    <b>Where did Eta's name come from?</b>
  </summary>

"Eta" means tiny in Esperanto. Plus, it can be used as an acronym for all sorts of cool phrases: "ECMAScript Template Awesomeness", "Embedded Templating Alternative", etc....

Additionally, Eta is a letter of the Greek alphabet (it stands for all sorts of cool things in various mathematical fields, including efficiency) and is three letters long (perfect for a file extension).

</details>

<br />

## Integrations

<d
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `npm-to-yarn.md`
```markdown
# 📦 bgub/npm-to-yarn [🔖 PENDING/APPROVE]
🔗 https://github.com/bgub/npm-to-yarn
🌐 https://nebrelbug.github.io/npm-to-yarn/test.html

## Meta
- **Stars:** ⭐ 37 | **Forks:** 🍴 13
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2025-09-12
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Convert npm CLI commands to yarn, and vice versa

## README (trích đầu)
```
# npm-to-yarn

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[logo]: https://img.shields.io/badge/all_contributors-0-orange.svg 'Number of contributors on All-Contributors'

<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![npm](https://img.shields.io/npm/v/npm-to-yarn)](https://www.npmjs.com/package/npm-to-yarn)
[![License](https://img.shields.io/npm/l/npm-to-yarn)](./LICENSE)
[![CI](https://github.com/nebrelbug/npm-to-yarn/actions/workflows/ci.yml/badge.svg)](https://github.com/nebrelbug/npm-to-yarn/actions/workflows/ci.yml)
[![Coveralls](https://img.shields.io/coveralls/nebrelbug/npm-to-yarn.svg)](https://coveralls.io/github/nebrelbug/npm-to-yarn)

[![styled with prettier](https://img.shields.io/badge/styled_with-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![Donate](https://img.shields.io/badge/donate-paypal-blue.svg)](https://paypal.me/bengubler)

**Summary**

`npm-to-yarn` is designed to convert NPM CLI commands to their Yarn equivalents (and vice versa).

## Why `npm-to-yarn`?

`npm-to-yarn` is super helpful in documentation, for example in generating code tabs.

## 📜 Docs

```js
import convert from 'npm-to-yarn'

// or
// var convert = require('npm-to-yarn')

convert('npm install squirrelly', 'yarn')
// yarn add squirrelly

// npx conversions

convert('npx create-next-app', 'yarn')
// yarn dlx create-next-app
```

`npm-to-yarn` exposes a UMD build, so you can also install it with a CDN (it exposes global variable `n2y`)

### API

```ts
/**
 * Converts between npm and yarn command
 */
export default function convert (str: string, to: 'npm' | 'yarn' | 'pnpm' | 'bun'): string
```

## ✔️ Tests

Tests can be run with `npm test`. Multiple tests check that parsing, rendering, and compiling return expected results, formatting follows guidelines, and code coverage is at the expected level.

## 📦 Contributing to `npm-to-yarn` - Setup Guide

Install Dependencies

```sh copy
npm install
```

Run the development server

```sh
npm run start
```

A new file: `npm-to-yarn.mjs` is created in `dist` folder. <br>
Open `node` inside the terminal and write the following code to test new changes

```js
const npmToYarn = await import('./dist/npm-to-yarn.mjs')
const convert = npmToYarn.default

convert('npm install react', 'bun')
```

## Resources

To be added

## Projects using `npm-to-yarn`

- [Dynamoose](https://dynamoosejs.com)
- [Docusaurus](https://docusaurus.io)

## Contributors

Made with ❤ by [@nebrelbug](https://github.com/nebrelbug) and all these wonderful contributors ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->


<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind are welcome!
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

