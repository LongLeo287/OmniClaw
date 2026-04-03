---
id: eta-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:22.655577
---

# KNOWLEDGE EXTRACT: eta
> **Extracted on:** 2026-03-30 13:29:56
> **Source:** eta

---

## File: `.gitignore`
```
node_modules
coverage
.nyc_output
.DS_Store
*.log
.vscode
.idea
compiled
.awcache
.rpt2_cache
docs

dist

package-lock.json
yarn.lock
```

## File: `.release-please-manifest.json`
```json
{".":"4.5.1"}
```

## File: `biome.json`
```json
{
  "$schema": "https://biomejs.dev/schemas/2.3.5/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "ignoreUnknown": false,
    "includes": [
      "**",
      "!.release-please-manifest.json",
      "!jsr.json",
      "!browser-tests"
    ]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space"
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "style": {
        "useTemplate": "off"
      }
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double"
    }
  },
  "assist": {
    "enabled": true,
    "actions": {
      "source": {
        "organizeImports": "on"
      }
    }
  }
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [4.5.1](https://github.com/bgub/eta/compare/v4.5.0...v4.5.1) (2026-02-05)


### Bug Fixes

* add semicolons to compiled output to prevent ASI issues with forEach ([e0f1d65](https://github.com/bgub/eta/commit/e0f1d653f1c563b14b3592abef6378e3210dd90d))
* add semicolons to compiled template statements for consistency ([#362](https://github.com/bgub/eta/issues/362)) ([e0f1d65](https://github.com/bgub/eta/commit/e0f1d653f1c563b14b3592abef6378e3210dd90d))

## [4.5.0](https://github.com/bgub/eta/compare/v4.4.1...v4.5.0) (2025-12-12)


### Features

* add require field for core module in package.json ([#357](https://github.com/bgub/eta/issues/357)) ([29f52f8](https://github.com/bgub/eta/commit/29f52f8d06461b5cb57e5428be0c224b3286eada))

## [4.4.1](https://github.com/bgub/eta/compare/v4.4.0...v4.4.1) (2025-11-13)


### Bug Fixes

* revert "eta/core" to ESM build ([37cc1ab](https://github.com/bgub/eta/commit/37cc1ab70499608f433edccdd02b0f072756e88a))

## [4.4.0](https://github.com/bgub/eta/compare/v4.3.1...v4.4.0) (2025-11-13)


### Features

* add ts-base to README, update rmWhitespace explanation ([d6db743](https://github.com/bgub/eta/commit/d6db743ff53887dcfccdd2d9b776f521820fe51a))

## [4.3.1](https://github.com/bgub/eta/compare/v4.3.0...v4.3.1) (2025-11-13)


### Bug Fixes

* exports are .mjs not .js ([f870aaf](https://github.com/bgub/eta/commit/f870aaf85984118d840a2910860b5d0aaad086b0))

## [4.3.0](https://github.com/bgub/eta/compare/v4.2.0...v4.3.0) (2025-11-13)


### Features

* add error.cause to RuntimeErr ([#306](https://github.com/bgub/eta/issues/306)) ([61b8715](https://github.com/bgub/eta/commit/61b87155311d25dfe3326c24407c27f494d275a4))


### Bug Fixes

* generate a CJS build, update build and type exports ([65cafd0](https://github.com/bgub/eta/commit/65cafd0ca48a144c9bb3db8b0609e02f5e7a9354))

## [4.2.0](https://github.com/bgub/eta/compare/v4.1.0...v4.2.0) (2025-11-12)


### Features

* add prepare script to allow installation from Git ([#348](https://github.com/bgub/eta/issues/348)) ([d8bacbb](https://github.com/bgub/eta/commit/d8bacbb840369cace6d495ac738b1acebc6cc374))


### Bug Fixes

* merge data dictionary when including ([#347](https://github.com/bgub/eta/issues/347)) ([c0cd1db](https://github.com/bgub/eta/commit/c0cd1dbb8e9aede71670268cc188dd385c567384))
* remove typo from README ([eb948d3](https://github.com/bgub/eta/commit/eb948d300403af6c8cfc67100c7877264f982c1c))
* use correct path for types exports ([#340](https://github.com/bgub/eta/issues/340)) ([b8d4b30](https://github.com/bgub/eta/commit/b8d4b3076a93b059e074ae3bd57ecbd218481eb3))

## [4.1.0](https://github.com/bgub/eta/compare/v4.0.1...v4.1.0) (2025-11-12)


### Features

* add outputFunctionName config property ([ed33823](https://github.com/bgub/eta/commit/ed33823d4253c483a07c9149b2e42c2a10da39c8))
* Add outputFunctionName config property ([#331](https://github.com/bgub/eta/issues/331)) ([ed33823](https://github.com/bgub/eta/commit/ed33823d4253c483a07c9149b2e42c2a10da39c8))

## [4.0.1](https://github.com/bgub/eta/compare/eta-v4.0.0...eta-v4.0.1) (2025-09-17)


### Bug Fixes

* change deno.land link to jsr in README ([21b3afc](https://github.com/bgub/eta/commit/21b3afc82318d37e410ec49121c57feba7785445))

## [4.0.0](https://github.com/bgub/eta/compare/eta-v4.0.0-beta.1...eta-v4.0.0) (2025-09-17)


### Bug Fixes

* combine release-please and publish workflows ([02f033a](https://github.com/bgub/eta/commit/02f033a2db05f98b246e254288a21ca2b2e14fd8))


### Miscellaneous Chores

* remove mention of beta in README ([fb9e779](https://github.com/bgub/eta/commit/fb9e7795f6ed81d4cdcec831518af0b503821137))

## [4.0.0-beta.1](https://github.com/bgub/eta/compare/eta-v4.0.0-alpha.2...eta-v4.0.0-beta.1) (2025-09-13)


### Features

* rename browser export to 'core' ([#326](https://github.com/bgub/eta/issues/326)) ([9d73de2](https://github.com/bgub/eta/commit/9d73de247d2cc0ae824ab47623240ee3e5c5088a))


### Bug Fixes

* add CI token ([#322](https://github.com/bgub/eta/issues/322)) ([1129aba](https://github.com/bgub/eta/commit/1129aba061d53d9e2a379b6c86f9b3f453a1b569))
* install latest npm version ([4185b29](https://github.com/bgub/eta/commit/4185b290717cba0fc33e8044f0e6d464d1dce4b6))
* last try before bed ([#324](https://github.com/bgub/eta/issues/324)) ([7b3650a](https://github.com/bgub/eta/commit/7b3650a26a9fd69e4df78a60614ad10164154b2d))


### Miscellaneous Chores

* update README ([9d8f6f4](https://github.com/bgub/eta/commit/9d8f6f480beacea41aa39458699347022c15025a))

## [4.0.0-alpha.2](https://github.com/bgub/eta/compare/eta-v4.0.0-alpha.1...eta-v4.0.0-alpha.2) (2025-09-10)


### Bug Fixes

* CI tweaks ([#317](https://github.com/bgub/eta/issues/317)) ([cd533c6](https://github.com/bgub/eta/commit/cd533c63a1f03919a68145cb4cdb09a3346e53fa))
* remove -w flag in CI publish ([#319](https://github.com/bgub/eta/issues/319)) ([dfe66e0](https://github.com/bgub/eta/commit/dfe66e022f1763264fe12ce9cc885d85437560ae))
* switch to OIDC for npm publish ([#320](https://github.com/bgub/eta/issues/320)) ([69b6e84](https://github.com/bgub/eta/commit/69b6e8447f6a6f2a3c1923d6ccc521a7a7a37693))
* tweak CI ([#321](https://github.com/bgub/eta/issues/321)) ([58d28ff](https://github.com/bgub/eta/commit/58d28ff6d0b49ce6e7e344e7eb77f00e4937b686))

## [4.0.0-alpha.1](https://github.com/bgub/eta/compare/eta-v3.5.0...eta-v4.0.0-alpha.1) (2025-09-10)


### Features

* prep for version 4 ([c23560d](https://github.com/bgub/eta/commit/c23560debc876aa78725d88b9300c81c92b0a5f4))


### Bug Fixes

* add manifest ([#312](https://github.com/bgub/eta/issues/312)) ([2de3fe6](https://github.com/bgub/eta/commit/2de3fe6716e284963040d282d21605abe4dd273a))
* add release-please bootstrap-sha ([#314](https://github.com/bgub/eta/issues/314)) ([0dd4824](https://github.com/bgub/eta/commit/0dd48248a2737899600084626425b53bfc166130))
* semantic PR workflow ([#313](https://github.com/bgub/eta/issues/313)) ([dba2152](https://github.com/bgub/eta/commit/dba215257c7c286c2fdb84cfc8b055457c56754e))


### Miscellaneous Chores

* remove all-contributors section ([#316](https://github.com/bgub/eta/issues/316)) ([90bf130](https://github.com/bgub/eta/commit/90bf1309ae90b16ee03fbf95b8845c3ceef653e9))
```

## File: `jsr.json`
```json
{
  "name": "@bgub/eta",
  "version": "4.5.1",
  "license": "MIT",
  "exports": "./src/index.ts",
  "publish": {
    "include": [
      "LICENSE",
      "README.md",
      "src/**/*.ts"
    ]
  }
}
```

## File: `LICENSE`
```
Copyright 2025 Ben Gubler <nebrelbug@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `package.json`
```json
{
  "name": "eta",
  "version": "4.5.1",
  "description": "Lightweight, fast, and powerful embedded JS template engine",
  "keywords": [
    "handlebars",
    "ejs",
    "eta",
    "template engine",
    "embedded template engine",
    "layouts",
    "partials",
    "typescript types"
  ],
  "homepage": "https://eta.js.org",
  "type": "module",
  "exports": {
    ".": {
      "types": {
        "import": "./dist/index.d.mts",
        "require": "./dist/index.d.cts"
      },
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs"
    },
    "./core": {
      "require": "./dist/core.js",
      "import": "./dist/core.js",
      "types": "./dist/core.d.ts"
    },
    "./package.json": "./package.json"
  },
  "main": "./dist/index.cjs",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.mts",
  "sideEffects": false,
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "tsdown",
    "prepare": "npm run build",
    "dev": "tsdown --watch",
    "lint": "biome check --error-on-warnings",
    "format": "biome format --write",
    "test": "vitest run --coverage",
    "size": "size-limit"
  },
  "author": "Ben Gubler <nebrelbug@gmail.com>",
  "funding": "https://github.com/bgub/eta?sponsor=1",
  "repository": "github:bgub/eta",
  "bugs": {
    "url": "https://github.com/bgub/eta/issues"
  },
  "license": "MIT",
  "engines": {
    "node": ">=20"
  },
  "size-limit": [
    {
      "path": "dist/core.js",
      "limit": "3.5 KB"
    }
  ],
  "devDependencies": {
    "@biomejs/biome": "2.3.5",
    "@size-limit/preset-small-lib": "^11.2.0",
    "@types/node": "^24.10.1",
    "@vitest/coverage-istanbul": "4.0.8",
    "size-limit": "^11.2.0",
    "tsdown": "^0.16.4",
    "typescript": "^5.9.3",
    "vitest": "^4.0.8"
  }
}
```

## File: `README.md`
```markdown
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

<details>
  <summary>
    <b>Visual Studio Code</b>
  </summary>

[@shadowtime2000](https://github.com/shadowtime2000) created [eta-vscode](https://marketplace.visualstudio.com/items?itemName=shadowtime2000.eta-vscode).

</details>

<details>
  <summary>
    <b>ESLint</b>
  </summary>

[eslint-plugin-eta](https://github.com/eta-dev/eslint-plugin-eta) was created to provide an ESLint processor so you can lint your Eta templates.

</details>

<details>
  <summary>
    <b>Webpack</b>
  </summary>

Currently there is no official Webpack integration but [@clshortfuse](https://github.com/clshortfuse) shared the loader he uses:

```javascript
{
  loader: 'html-loader',
  options: {
    preprocessor(content, loaderContext) {
      return eta.render(content, {}, { filename: loaderContext.resourcePath });
    },
  },
}
```

</details>

<details>
  <summary>
    <b>Node-RED</b>
  </summary>

To operate with Eta templates in Node-RED: [@ralphwetzel/node-red-contrib-eta](https://flows.nodered.org/node/@ralphwetzel/node-red-contrib-eta)

  <img width="150" alt="image" src="https://user-images.githubusercontent.com/16342003/160198427-2a69ff10-e8bf-4873-9d99-2929a584ccc8.png">

</details>

<details>
  <summary>
    <b>Koa</b>
  </summary>

To render Eta templates in [Koa](https://koajs.com) web framework: [@cedx/koa-eta](https://github.com/cedx/koa-eta/wiki)

</details>

<details>
  <summary>
    <b>Vite</b>
  </summary>

To use Eta templates in your Vite project: [@rinoshiyo/vite-plugin-eta](https://github.com/rinoshiyo/vite-plugin-eta)

</details>

<br />

## Projects using `eta`

- [Docusaurus v2](https://v2.docusaurus.io): open-source documentation framework that uses Eta to generate a SSR build
- [swagger-typescript-api](https://github.com/acacode/swagger-typescript-api): Open source typescript api codegenerator from Swagger. Uses Eta as codegenerator by templates
- [html-bundler-webpack-plugin](https://github.com/webdiscus/html-bundler-webpack-plugin): Webpack plugin make easily to bundle HTML pages from templates, source styles and scripts
- [SmartDeno](https://github.com/guildenstern70/SmartDeno): SmartDeno is an easy to setup web template using Deno & Oak
- [stc](https://github.com/long-woo/stc): OpenAPI (Swagger) and Apifox documentation converted to api. Use eta templates to generate code.
- [Add yours!](https://github.com/bgub/eta/edit/master/README.md)

## Contributors

Made with ❤️ by [bgub](https://github.com/bgub) and [many wonderful contributors](https://github.com/bgub/eta/graphs/contributors). Contributions of any kind are welcome!

## Credits

- Async support, file handling, and error formatting were based on code from [EJS](https://github.com/mde/ejs), which is licensed under the Apache-2.0 license. Code was modified and refactored to some extent.
- Syntax and some parts of compilation are heavily based off EJS, Nunjucks, and doT.
```

## File: `release-please-config.json`
```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "release-type": "node",
  "prerelease": true,
  "packages": {
    ".": {
      "package-name": "eta",
      "extra-files": ["jsr.json"],
      "prerelease-type": "alpha",
      "include-component-in-tag": false
    }
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "esnext",
    "lib": ["es2023"],
    "moduleDetection": "force",
    "module": "preserve",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "types": ["node"],
    "strict": true,
    "noUnusedLocals": true,
    "declaration": true,
    "declarationMap": true,
    "allowImportingTsExtensions": true,
    "emitDeclarationOnly": true,
    "esModuleInterop": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
```

## File: `tsdown.config.ts`
```typescript
import { defineConfig } from "tsdown";

export default defineConfig([
  {
    entry: ["./src/index.ts"],
    format: ["esm", "cjs"],
    platform: "node",
    dts: true,
    sourcemap: true,
  },
  {
    entry: ["./src/core.ts"],
    platform: "browser",
    dts: true,
    minify: true,
    sourcemap: true,
  },
]);
```

## File: `vitest.config.ts`
```typescript
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      provider: "istanbul",
      reporter: ["lcov"],
      include: ["src/**/*.ts"],
      thresholds: {
        branches: 85,
        functions: 95,
        lines: 95,
        statements: 95,
      },
    },
  },
});
```

## File: `browser-tests/benchmark.html`
```html
<!doctype html>

<!--
Modified from AUI's docs. See their license below:
==================================================
Copyright (c) 2017 糖饼

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-->

<html lang="en" id="page-rendering-test">
    <head>
        <meta charset="utf-8" />
        <title>Eta Rendering Benchmarks</title>
        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

        <link
            rel="stylesheet"
            href="https://www.unpkg.com/font-awesome@4.3.0/css/font-awesome.min.css"
        />

        <style>
            html {
                box-sizing: border-box;
            }
            *,
            *:before,
            *:after {
                box-sizing: inherit;
            }

            input,
            button,
            select {
                margin: 0;
                padding: 0;
                border: 0;
            }
            html,
            body {
                margin: 0;
                padding: 0;
            }
            @media screen {
                html,
                body {
                    height: 100%;
                }
            }
            body {
                background: #fff;
                font-size: 16px;
                font-family:
                    "Source Sans Pro", "Helvetica Neue", Arial, sans-serif;
                color: #444;
                text-rendering: optimizeLegibility;
                -webkit-font-smoothing: antialiased;
                overflow-x: hidden;
            }

            pre .keyword,
            pre .javascript .function {
                color: #8959a8;
            }
            #page-rendering-test #content-wrap {
                padding: 0 60px;
                max-width: 800px;
            }
            #page-rendering-test #content-wrap input[type="number"] {
                width: 6em;
                border-bottom: 1px solid #003cb1;
            }
            #page-rendering-test #content-wrap .button {
                padding: 8px;
                margin-right: 10px;
                border-radius: 2em;
                display: inline-block;
                color: #fff;
                transition: all 0.15s ease;
                box-sizing: border-box;
                text-decoration: none;
                background: #003cb1;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <div id="content-wrap">
                <div id="app"></div>
            </div>

            <script src="https://unpkg.com/highcharts@10.2.0/highcharts.js"></script>

            <script src="https://unpkg.com/art-template@4.13.2/lib/template-web.js"></script>
            <script src="https://unpkg.com/dot@1.1.3/doT.min.js"></script>
            <script src="https://unpkg.com/ejs@3.1.8/ejs.min.js"></script>
            <script src="https://unpkg.com/handlebars@4.7.7/dist/handlebars.min.js"></script>
            <script src="https://unpkg.com/squirrelly@9.0.0"></script>
            <script src="https://unpkg.com/mustache@4.2.0/mustache.min.js"></script>
            <script src="https://pugjs.org/js/pug.js"></script>
            <script src="https://unpkg.com/swig@1.4.2/dist/swig.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/lodash/lodash.min.js"></script>

            <script type="module" src="./benchmark.js"></script>
        </div>
    </body>
</html>
```

## File: `browser-tests/benchmark.js`
```javascript
/* eslint-disable dot-notation, space-before-function-paren */
/* global template, doT, ejs, Handlebars, Sqrl, Mustache, swig, Highcharts, _, Eta */

/*

Modified from AUI's docs. See their license below:
==================================================
Copyright (c) 2017 糖饼

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

import * as eta from '../dist/core.js'

const etaInstance = new eta.Eta({
  autoTrim: false,
});

Sqrl.defaultConfig.autoTrim = false;

var templateList = {
  template: `
<ul>
    <% for (var i = 0, l = list.length; i < l; i ++) { %>
        <li>User: <%= list[i].user %> / Web Site: <%= list[i].site %></li>
    <% } %>
</ul>`,
  "template-raw": `
<ul>
    <% for (var i = 0, l = list.length; i < l; i ++) { %>
        <li>User: <%- list[i].user %> / Web Site: <%- list[i].site %></li>
    <% } %>
</ul>`,
  "template-fast-mode": `
<ul>
    <% for (var i = 0, l = $data.list.length; i < l; i ++) { %>
        <li>User: <%= $data.list[i].user %> / Web Site: <%= $data.list[i].site %></li>
    <% } %>
</ul>`,
  "template-fast-mode-raw": `
<ul>
    <% for (var i = 0, l = $data.list.length; i < l; i ++) { %>
        <li>User: <%- $data.list[i].user %> / Web Site: <%- $data.list[i].site %></li>
    <% } %>
</ul>`,
  eta: `
<ul>
    <% for (var i = 0, ln = it.list.length; i < ln; i ++) { %>
        <li>User: <%= it.list[i].user %> / Web Site: <%= it.list[i].site %></li>
    <% } %>
</ul>`,
  "eta-raw": `
<ul>
    <% for (var i = 0, ln = it.list.length; i < ln; i ++) { %>
        <li>User: <%~ it.list[i].user %> / Web Site: <%~ it.list[i].site %></li>
    <% } %>
</ul>`,
  dot: `
<ul>
    {{ for (var i = 0, l = it.list.length; i < l; i ++) { }}
        <li>User: {{!it.list[i].user}} / Web Site: {{!it.list[i].site}}</li>
    {{ } }}
</ul>`,
  "dot-raw": `
<ul>
    {{ for (var i = 0, l = it.list.length; i < l; i ++) { }}
        <li>User: {{=it.list[i].user}} / Web Site: {{=it.list[i].site}}</li>
    {{ } }}
</ul>`,
};

/* ----------------- */

var config = {
  length: 20,
  calls: 6000,
  escape: true,
};

function getParameterByName(name) {
  var url = window.location.href;
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)");
  var results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return "";
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

if (window.location.search) {
  if (getParameterByName("length")) {
    config.length = Number(getParameterByName("length"));
  }
  if (getParameterByName("calls")) {
    config.calls = Number(getParameterByName("calls"));
  }
  if (getParameterByName("escape")) {
    config.escape = getParameterByName("escape") === "true";
  }
}

// 制造测试数据
var data = {
  list: [],
};

for (let i = 0; i < config.length; i++) {
  data.list.push({
    index: i,
    user: '<strong style="color:red">糖饼</strong>',
    site: "https://github.com/aui",
    weibo: "http://weibo.com/planeart",
    QQweibo: "http://t.qq.com/tangbin",
  });
}

// 待测试的引擎列表
var testList = [
  {
    name: "art-template",
    tester: () => {
      var id = config.escape ? "template" : "template-raw";
      var source = templateList[id];
      //   console.log(fn.toString())
      var html = "";
      for (let i = 0; i < config.calls; i++) {
        const fn = template.compile(source);
        html = fn(data);
      }
      return html;
    },
  },

  {
    name: "art-template / fast mode",
    tester: () => {
      var id = config.escape ? "template-fast-mode" : "template-fast-mode-raw";
      var source = templateList[id];
      var html = "";
      for (let i = 0; i < config.calls; i++) {
        const fn = template.compile(source);
        html = fn(data);
      }
      return html;
    },
  },

  {
    name: "lodash.template",
    tester: () => {
      var id = config.escape ? "template" : "template-raw";
      var source = templateList[id];
      var html = "";
      for (let i = 0; i < config.calls; i++) {
        const fn = _.template(source);
        html = fn(data);
      }
      return html;
    },
  },

  {
    name: "doT",
    tester: () => {
      var id = config.escape ? "dot" : "dot-raw";
      var source = templateList[id];
      var html = "";
      for (let i = 0; i < config.calls; i++) {
        const fn = doT.template(source);
        html = fn(data);
      }
      return html;
    },
  },

  {
    name: "ejs",
    tester: () => {
      var id = config.escape ? "template" : "template-raw";
      var source = templateList[id];
      var html = "";
      for (let i = 0; i < config.calls; i++) {
        const fn = ejs.compile(source);
        html = fn(data);
      }
      return html;
    },
  },

  {
    name: "Eta",
    tester: () => {
      var id = config.escape ? "eta" : "eta-raw";

      var source = templateList[id];
      var html = "";
      data.$name = "temp";
      for (let i = 0; i < config.calls; i++) {
        const fn = etaInstance.compile(source);
        html = etaInstance.render(fn, data);
      }
      return html;
    },
  },
];

Highcharts.setOptions({
  colors: [
    "#EF6F65",
    "#F3AB63",
    "#F8D56F",
    "#99DD7A",
    "#74BBF3",
    "#CB93E0",
    "#A2A2A4",
    "#E1AC65",
    "#6AF9C4",
  ],
});

var runTest = (callback) => {
  var list = testList.filter(
    (test) => !config.escape || test.supportEscape !== false,
  );

  var Timer = function () {
    this.startTime = window.performance.now();
  };

  Timer.prototype.stop = function () {
    return window.performance.now() - this.startTime;
  };

  var colors = Highcharts.getOptions().colors;
  var categories = [];

  for (let i = 0; i < list.length; i++) {
    categories.push(list[i].name);
  }

  var chart = new Highcharts.Chart({
    chart: {
      animation: {
        duration: 150,
      },
      renderTo: "test-container",
      height: categories.length * 32,
      type: "bar",
    },

    title: false,

    // subtitle: {
    //     text: config.length + ' list × ' + config.calls + ' calls'
    // },

    xAxis: {
      categories: categories,
      labels: {},
    },

    yAxis: {
      min: 0,
      title: {
        text: "Time",
      },
    },

    legend: {
      enabled: false,
    },

    tooltip: {
      formatter: function () {
        return "<b>" + this.x + "</b><br/>" + this.y + " ops/sec";
      },
    },

    credits: {
      enabled: false,
    },
    plotOptions: {
      bar: {
        dataLabels: {
          enabled: true,
          formatter: function () {
            return this.y + " ops/sec";
          },
        },
      },
    },
    series: [
      {
        data: [],
      },
    ],
  });

  function tester(target) {
    var time = new Timer();
    var html = target.tester();
    var endTime = time.stop();
    console.log(target.name + "------------------\n", html);

    var timeInSecs = endTime / 1000;
    var opsPerSec = Math.round(config.calls / timeInSecs);

    chart.series[0].addPoint({
      color: colors.shift(),
      y: opsPerSec,
    });

    if (!list.length) {
      callback();
      return;
    }

    target = list.shift();

    setTimeout(() => {
      tester(target);
    }, 500);
  }

  var target = list.shift();
  tester(target);
};

window.restart = (key, value) => {
  config[key] = value;
};

function getLink() {
  window.location.search =
    "length=" +
    config.length +
    "&calls=" +
    config.calls +
    "&escape=" +
    config.escape;
}

window.load = (selector) => {
  var app = document.querySelector(selector);
  var body = `
<h1>Eta Browser Benchmarks</h1>
<br>
<em>This benchmark of popular embedded template engines measures both compilation and rendering. Since the results can be somewhat inconsistent (and don't reflect the full picture, like feature support) this feature is best used by developers working on Eta.</em>
<br><br>
<em>Note: doT and Eta usually trade off the lead on unescaped templates. Keep in mind that Eta supports template tags inside strings & comments, plugins, whitespace trimming, etc.</em>
<br><br>
<em>Note: these benchmarks are ONLY VALID if page is served by a server (localhost, RawGit are ok). Otherwise results are highly variable and inaccurate (I don't know why!)</em>
<br><br>
<strong>Longer (more ops/sec) is better</strong>

<div class="header">
    <p class="item">
        <button id="button-start" class="button">Run Test&raquo;</button>
        <button id="button-restart" class="button" style="display:none">Restart</button>
        <br><br>
        <span>config: </span>
        <label><input type="number" value="{{it.length}}" onchange="restart('length', this.value)"> list</label>
        <strong>×</strong>
        <label><input type="number" value="{{it.calls}}" onchange="restart('calls', this.value)"> calls</label>
        <label><input type="checkbox" {{@if(it.escape)}}checked{{/if}} onchange="restart('escape', this.checked)"> escape</label>
        <button id="get-link" class="button">&#x1f517; Get link</button>

    </p>
    <p class="item">
    </p>
</div>
<div id="test-container" style="min-width: 400px; margin: 0 auto"></div>`;

  var data = config;
  data.testList = testList;
  app.innerHTML = Sqrl.render(body, data, { name: "body" });

  document.getElementById("get-link").addEventListener("click", getLink);

  document.getElementById("button-start").onclick = function () {
    this.disabled = true;
    runTest(() => {
      this.style.display = "none";
      document.getElementById("button-restart").style.display = "";
    });
  };

  document.getElementById("button-restart").onclick = () => {
    window.location.reload();
  };
};

window.load("#app");
```

## File: `browser-tests/demo.html`
```html
<!--Based on @olado's excellent tester from doT.js-->
<!--Modified by Ben Gubler-->
<!--NOTE: You have to serve this file if you want to see the sourcemaps. NPM Package 'serve' works-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"
    />
    <meta name="description" content="Test out Eta templates in the browser here" />
    <style>
      body {
        background-color: #f4f4f4;
        color: #555;
        max-width: 800px;
        padding: 20px;
        font-size: 16px;
        font-weight: 200;
        margin: 0 auto;
        font-family: Helvetica Neue, arial, verdana;
      }

      h2 {
        text-shadow: 0 1px 2px #fff;
        margin: 0;
      }

      h2 span {
        font-weight: 200;
        font-size: 14px;
      }

      a {
        color: #2b80ff;
      }

      .smaller {
        font-size: 0.8em;
      }

      h4 {
        margin: 4px 0;
        font-weight: 400;
        font-size: 20px;
      }

      textarea {
        border: 1px solid lightgrey;
        outline: none;
        font-size: 14px;
        width: 96%;
        height: 210px;
        padding: 10px;
        text-align: left;
        resize: vertical;
      }

      .templategroup,
      .datagroup,
      .functiongroup,
      .resultgroup {
        width: 48%;
        margin: 4px 2% 4px 0;
        float: left;
        min-width: 300px;
      }

      #function,
      #result {
        background: #ddd;
        height: 212px;
        padding: 10px;
        font-size: 14px;
        overflow-y: auto;
      }

      #function,
      #result {
        white-space: pre;
      }

      .definegroup {
        display: none;
      }

      .templategroup.withdefs .definegroup {
        display: block;
      }

      .templategroup.withdefs #template {
        height: 90px;
      }

      textarea.defines {
        height: 60px;
      }

      .stripgroup {
        padding-top: 8px;
        width: 160px;
        float: left;
      }

      #sampletabs {
        list-style: none;
        margin: 0;
        padding: 0;
      }

      #sampletabs li {
        float: left;
        margin: 4px;
        padding: 4px 8px;
        background: #ddd;
        cursor: pointer;
      }

      #sampletabs li.active {
        background: #2b80ff;
        color: #fff;
      }

      @media all and (max-width: 740px) {
        .templategroup,
        .datagroup,
        .functiongroup,
        .resultgroup {
          width: 100%;
          margin-right: 0;
        }

        pre {
          overflow-x: scroll;
        }
      }
    </style>
    <title>Eta Playground</title>
  </head>

  <body>
    <h2>
      Playground
      <span
        >Based on the excellent
        <a href="http://olado.github.io/doT/index.html">DoT.js</a> website</span
      >
    </h2>
    <div id="samples">
      <ul id="sampletabs"></ul>
      <!--Keeping this just in case I implement a similar tabs feature-->
      <!-- <div class="stripgroup">
            <input id="strip" type="checkbox" checked="checked" />
            <label for="strip">Strip whitespaces</label>
        </div> -->
      <div style="clear: both; height: 10px"></div>
      <div class="templategroup">
        <h4>Template</h4>
        <textarea autocomplete="off" id="template">
Hi
<% console.log("Hope you like Eta!"); %>
<%= it.htmlstuff %>

<% for (var key in it.obj) { %>
Value: <%= it.obj[key] %>, Key: <%= key %>

<% if (key === 'thirdchild') { %>
  <% for (var i = 0, arr = it.obj[key]; i < arr.length; i++) { %>
      Salutations! Index: <%= i %>, parent key: <%= key %>

  <% } %>
<% } %>
<% } %>

Partial: <%~ include("mypartial") %>
</textarea
        >
      </div>
      <div class="functiongroup">
        <h4>eta.compile()</h4>
        <div id="function"></div>
      </div>
      <div style="clear: both"></div>
      <div class="datagroup">
        <h4>Data</h4>
        <textarea autocomplete="off" id="data">
"htmlstuff": "<script>alert('hey')</script><p>alert('hey')</p><p>alert('hey')</p><p>alert('hey')</p>",
"arr": ["Hey", "<p>Malicious XSS</p>", "Hey", 3, 12],
"obj": {
    "firstchild": "this is a lowercase string",
    "secondchild": "HEY",
    "thirdchild": [3, 6, 3, 2, 5, 4]
}
        </textarea>
      </div>
      <div class="resultgroup">
        <h4>Result</h4>
        <div id="result"></div>
      </div>
    </div>
    <script type="module">
      import { Eta } from "../dist/core.js";

      // TODO: add fallback using unpkg

      var eta = new Eta();

      window.onload = function () {
        eta.loadTemplate("mypartial", eta.compile("This is a partial"));

        function escape(str) {
          // To handle escaping for the function result
          var escMap = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;",
            "/": "&#x2F;",
          };

          function replaceChar(s) {
            return escMap[s];
          }
          var newStr = String(str);
          if (/[&<>"'/]/.test(newStr)) {
            return newStr.replace(/[&<>"'/]/g, replaceChar);
          } else {
            return newStr;
          }
        }

        function render() {
          console.clear();
          var options = JSON.parse("{" + document.getElementById("data").value + "}");
          console.log(JSON.stringify(options));
          var template = document.getElementById("template").value;
          try {
            var functionResult = eta.compile(template).toString();
            document.getElementById("function").innerHTML = escape(functionResult);
            if (!eta.config.async) {
              document.getElementById("result").innerHTML = eta.renderString(template, options);
            } else {
              eta.renderStringAsync(template, options).then(function (res) {
                document.getElementById("result").innerHTML = res;
              });
            }
            console.log(eta.renderString(template, options));
          } catch (ex) {
            console.error(ex.message);
          }
        }
        render();
        document.getElementById("template").addEventListener("input", render);
        document.getElementById("data").addEventListener("input", render);
      };
    </script>
  </body>
</html>
```

## File: `src/compile-string.ts`
```typescript
import type { Options } from "./config.ts";
import type { Eta } from "./internal.ts";
import type { AstObject } from "./parse.ts";

/**
 * Compiles a template string to a function string. Most often users just use `compile()`, which calls `compileToString` and creates a new function using the result
 */

export function compileToString(
  this: Eta,
  str: string,
  options?: Partial<Options>,
): string {
  const config = this.config;
  const isAsync = options?.async;

  const compileBody = this.compileBody;

  const buffer: Array<AstObject> = this.parse.call(this, str);

  // note: when the include function passes through options, the only parameter that matters is the filepath parameter
  let res = `${config.functionHeader}
let include = (__eta_t, __eta_d) => this.render(__eta_t, {...${config.varName}, ...(__eta_d ?? {})}, options);
let includeAsync = (__eta_t, __eta_d) => this.renderAsync(__eta_t, {...${config.varName}, ...(__eta_d ?? {})}, options);

let __eta = {res: "", e: this.config.escapeFunction, f: this.config.filterFunction${
    config.debug
      ? ', line: 1, templateStr: "' +
        str.replace(/\\|"/g, "\\$&").replace(/\r\n|\n|\r/g, "\\n") +
        '"'
      : ""
  }};

function layout(path, data) {
  __eta.layout = path;
  __eta.layoutData = data;
}${config.debug ? "try {" : ""}${
    config.useWith ? "with(" + config.varName + "||{}){" : ""
  }

function ${config.outputFunctionName}(s){__eta.res+=s;}

${compileBody.call(this, buffer)}
if (__eta.layout) {
  __eta.res = ${
    isAsync ? "await includeAsync" : "include"
  } (__eta.layout, {...${
    config.varName
  }, body: __eta.res, ...__eta.layoutData});
}
${config.useWith ? "}" : ""}${
  config.debug
    ? "} catch (e) { this.RuntimeErr(e, __eta.templateStr, __eta.line, options.filepath) }"
    : ""
}
return __eta.res;
`;

  if (config.plugins) {
    for (let i = 0; i < config.plugins.length; i++) {
      const plugin = config.plugins[i];
      if (plugin.processFnString) {
        res = plugin.processFnString(res, config);
      }
    }
  }

  return res;
}

/**
 * Loops through the AST generated by `parse` and transform each item into JS calls
 *
 * **Example**
 *
 * ```js
 * let templateAST = ['Hi ', { val: 'it.name', t: 'i' }]
 * compileBody.call(Eta, templateAST)
 * // => "__eta.res+='Hi '\n__eta.res+=__eta.e(it.name)\n"
 * ```
 */

export function compileBody(this: Eta, buff: Array<AstObject>): string {
  const config = this.config;

  let i = 0;
  const buffLength = buff.length;
  let returnStr = "";

  for (i; i < buffLength; i++) {
    const currentBlock = buff[i];
    if (typeof currentBlock === "string") {
      const str = currentBlock;

      // we know string exists
      returnStr += "__eta.res+='" + str + "';\n";
    } else {
      const type = currentBlock.t; // "r", "e", or "i"
      let content = currentBlock.val || "";

      if (config.debug) returnStr += "__eta.line=" + currentBlock.lineNo + "\n";

      if (type === "r") {
        // raw

        if (config.autoFilter) {
          content = "__eta.f(" + content + ")";
        }

        returnStr += "__eta.res+=" + content + ";\n";
      } else if (type === "i") {
        // interpolate

        if (config.autoFilter) {
          content = "__eta.f(" + content + ")";
        }

        if (config.autoEscape) {
          content = "__eta.e(" + content + ")";
        }

        returnStr += "__eta.res+=" + content + ";\n";
      } else if (type === "e") {
        // execute
        returnStr += content + "\n";
      }
    }
  }

  return returnStr;
}
```

## File: `src/compile.ts`
```typescript
import type { EtaConfig, Options } from "./config.ts";
import { EtaParseError } from "./err.ts";
import type { Eta } from "./internal.ts";

export type TemplateFunction = (
  this: Eta,
  data?: object,
  options?: Partial<Options>,
) => string;
/* END TYPES */

/* istanbul ignore next */
const AsyncFunction = (async () => {}).constructor;

/**
 * Takes a template string and returns a template function that can be called with (data, config)
 *
 * @param str - The template string
 * @param config - A custom configuration object (optional)
 */

export function compile(
  this: Eta,
  str: string,
  options?: Partial<Options>,
): TemplateFunction {
  const config: EtaConfig = this.config;

  /* ASYNC HANDLING */
  // code gratefully taken from https://github.com/mde/ejs and adapted
  const ctor = options?.async
    ? (AsyncFunction as FunctionConstructor)
    : Function;
  /* END ASYNC HANDLING */

  try {
    return new ctor(
      config.varName,
      "options",
      this.compileToString.call(this, str, options),
    ) as TemplateFunction; // eslint-disable-line no-new-func
  } catch (e) {
    if (e instanceof SyntaxError) {
      throw new EtaParseError(
        "Bad template syntax\n\n" +
          e.message +
          "\n" +
          Array(e.message.length + 1).join("=") +
          "\n" +
          this.compileToString.call(this, str, options) +
          "\n", // This will put an extra newline before the callstack for extra readability
      );
    } else {
      throw e;
    }
  }
}
```

## File: `src/config.ts`
```typescript
import type { AstObject } from "./parse.ts";
import { XMLEscape } from "./utils.ts";

type trimConfig = "nl" | "slurp" | false;

export interface Options {
  /** Compile to async function */
  async?: boolean;

  /** Absolute path to template file */
  filepath?: string;
}

export interface EtaConfig {
  /** Whether or not to automatically XML-escape interpolations. Default true */
  autoEscape: boolean;

  /** Apply a filter function defined on the class to every interpolation or raw interpolation */
  autoFilter: boolean;

  /** Configure automatic whitespace trimming. Default `[false, 'nl']` */
  autoTrim: trimConfig | [trimConfig, trimConfig];

  /** Whether or not to cache templates if `name` or `filename` is passed */
  cache: boolean;

  /** Holds cache of resolved filepaths. Set to `false` to disable. */
  cacheFilepaths: boolean;

  /** Whether to pretty-format error messages (introduces runtime penalties) */
  debug: boolean;

  /** Function to XML-sanitize interpolations */
  escapeFunction: (str: unknown) => string;

  /** Function applied to all interpolations when autoFilter is true */
  filterFunction: (val: unknown) => string;

  /** Name of the function that can be used in template code to output text to the result (like EJS's `outputFunctionName`). */
  outputFunctionName: string;

  /** Raw JS code inserted in the template function. Useful for declaring global variables for user templates */
  functionHeader: string;

  /** Parsing options */
  parse: {
    /** Which prefix to use for evaluation. Default `""`, does not support `"-"` or `"_"` */
    exec: string;

    /** Which prefix to use for interpolation. Default `"="`, does not support `"-"` or `"_"` */
    interpolate: string;

    /** Which prefix to use for raw interpolation. Default `"~"`, does not support `"-"` or `"_"` */
    raw: string;
  };

  /** Array of plugins */
  plugins: Array<{
    processFnString?: (fnString: string, env?: EtaConfig) => string;
    processAST?: (ast: AstObject[], env?: EtaConfig) => AstObject[];
    processTemplate?: (fnString: string, env?: EtaConfig) => string;
  }>;

  /** Remove empty lines and whitespace between lines */
  rmWhitespace: boolean;

  /** Delimiters: by default `['<%', '%>']` */
  tags: [string, string];

  /** Make data available on the global object instead of varName */
  useWith: boolean;

  /** Name of the data object. Default `it` */
  varName: string;

  /** Directory that contains templates */
  views?: string;

  /** Control template file extension defaults. Default `.eta` */
  defaultExtension?: string;
}

/* END TYPES */

/** Eta's base (global) configuration */
const defaultConfig: EtaConfig = {
  autoEscape: true,
  autoFilter: false,
  autoTrim: [false, "nl"],
  cache: false,
  cacheFilepaths: true,
  debug: false,
  escapeFunction: XMLEscape,
  // default filter function (not used unless enables) just stringifies the input
  filterFunction: (val) => String(val),
  outputFunctionName: "output",
  functionHeader: "",
  parse: {
    exec: "",
    interpolate: "=",
    raw: "~",
  },
  plugins: [],
  rmWhitespace: false,
  tags: ["<%", "%>"],
  useWith: false,
  varName: "it",
  defaultExtension: ".eta",
};

export { defaultConfig };
```

## File: `src/core.ts`
```typescript
import { Eta as EtaCore } from "./internal.ts";

export type { TemplateFunction } from "./compile.ts";
export type { EtaConfig, Options } from "./config.ts";
export {
  EtaError,
  EtaFileResolutionError,
  EtaNameResolutionError,
  EtaParseError,
  EtaRuntimeError,
} from "./err.ts";

export class Eta extends EtaCore {}
```

## File: `src/err.ts`
```typescript
export class EtaError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "Eta Error";
  }
}

export class EtaParseError extends EtaError {
  constructor(message: string) {
    super(message);
    this.name = "EtaParser Error";
  }
}

export class EtaRuntimeError extends EtaError {
  constructor(message: string) {
    super(message);
    this.name = "EtaRuntime Error";
  }
}

export class EtaFileResolutionError extends EtaError {
  constructor(message: string) {
    super(message);
    this.name = "EtaFileResolution Error";
  }
}

export class EtaNameResolutionError extends EtaError {
  constructor(message: string) {
    super(message);
    this.name = "EtaNameResolution Error";
  }
}

/**
 * Throws an EtaError with a nicely formatted error and message showing where in the template the error occurred.
 */

export function ParseErr(message: string, str: string, indx: number): never {
  const whitespace = str.slice(0, indx).split(/\n/);

  const lineNo = whitespace.length;
  const colNo = whitespace[lineNo - 1].length + 1;
  message +=
    " at line " +
    lineNo +
    " col " +
    colNo +
    ":\n\n" +
    "  " +
    str.split(/\n/)[lineNo - 1] +
    "\n" +
    "  " +
    Array(colNo).join(" ") +
    "^";
  throw new EtaParseError(message);
}

export function RuntimeErr(
  originalError: Error,
  str: string,
  lineNo: number,
  path: string,
): never {
  // code gratefully taken from https://github.com/mde/ejs and adapted

  const lines = str.split("\n");
  const start = Math.max(lineNo - 3, 0);
  const end = Math.min(lines.length, lineNo + 3);
  const filename = path;
  // Error context
  const context = lines
    .slice(start, end)
    .map((line, i) => {
      const curr = i + start + 1;
      return (curr === lineNo ? " >> " : "    ") + curr + "| " + line;
    })
    .join("\n");

  const header = filename
    ? filename + ":" + lineNo + "\n"
    : "line " + lineNo + "\n";

  const err = new EtaRuntimeError(
    header + context + "\n\n" + originalError.message,
  );

  err.name = originalError.name; // the original name (e.g. ReferenceError) may be useful
  err.cause = originalError;

  throw err;
}
```

## File: `src/file-handling.ts`
```typescript
import * as fs from "node:fs";
import * as path from "node:path";

import type { Options } from "./config.ts";
import { EtaFileResolutionError } from "./err.ts";
import type { Eta as EtaCore } from "./internal.ts";

export function readFile(this: EtaCore, path: string): string {
  let res = "";

  try {
    res = fs.readFileSync(path, "utf8");
    // biome-ignore lint/suspicious/noExplicitAny: it's an error
  } catch (err: any) {
    if (err?.code === "ENOENT") {
      throw new EtaFileResolutionError(`Could not find template: ${path}`);
    } else {
      throw err;
    }
  }

  return res;
}

export function resolvePath(
  this: EtaCore,
  templatePath: string,
  options?: Partial<Options>,
): string {
  let resolvedFilePath = "";

  const views = this.config.views;

  if (!views) {
    throw new EtaFileResolutionError("Views directory is not defined");
  }

  const baseFilePath = options?.filepath;
  const defaultExtension =
    this.config.defaultExtension === undefined
      ? ".eta"
      : this.config.defaultExtension;

  // how we index cached template paths
  const cacheIndex = JSON.stringify({
    filename: baseFilePath, // filename of the template which called includeFile()
    path: templatePath,
    views: this.config.views,
  });

  templatePath += path.extname(templatePath) ? "" : defaultExtension;

  // if the file was included from another template
  if (baseFilePath) {
    // check the cache

    if (this.config.cacheFilepaths && this.filepathCache[cacheIndex]) {
      return this.filepathCache[cacheIndex];
    }

    const absolutePathTest = absolutePathRegExp.exec(templatePath);

    if (absolutePathTest?.length) {
      const formattedPath = templatePath.replace(/^\/*|^\\*/, "");
      resolvedFilePath = path.join(views, formattedPath);
    } else {
      resolvedFilePath = path.join(path.dirname(baseFilePath), templatePath);
    }
  } else {
    resolvedFilePath = path.join(views, templatePath);
  }

  if (dirIsChild(views, resolvedFilePath)) {
    // add resolved path to the cache
    if (baseFilePath && this.config.cacheFilepaths) {
      this.filepathCache[cacheIndex] = resolvedFilePath;
    }

    return resolvedFilePath;
  } else {
    throw new EtaFileResolutionError(
      `Template '${templatePath}' is not in the views directory`,
    );
  }
}

function dirIsChild(parent: string, dir: string) {
  const relative = path.relative(parent, dir);
  return relative && !relative.startsWith("..") && !path.isAbsolute(relative);
}

const absolutePathRegExp = /^\\|^\//;
```

## File: `src/index.ts`
```typescript
import { readFile, resolvePath } from "./file-handling.ts";
import { Eta as EtaCore } from "./internal.ts";

export type { TemplateFunction } from "./compile.ts";
export type { EtaConfig, Options } from "./config.ts";
export {
  EtaError,
  EtaFileResolutionError,
  EtaNameResolutionError,
  EtaParseError,
  EtaRuntimeError,
} from "./err.ts";

export class Eta extends EtaCore {
  readFile = readFile;

  resolvePath = resolvePath;
}
```

## File: `src/internal.ts`
```typescript
import type { TemplateFunction } from "./compile.ts";
import { compile } from "./compile.ts";
import { compileBody, compileToString } from "./compile-string.ts";
import type { EtaConfig, Options } from "./config.ts";
import { defaultConfig } from "./config.ts";
import { EtaError, RuntimeErr } from "./err.ts";
import { parse } from "./parse.ts";
import {
  render,
  renderAsync,
  renderString,
  renderStringAsync,
} from "./render.ts";
import { Cacher } from "./storage.ts";

export class Eta {
  constructor(customConfig?: Partial<EtaConfig>) {
    if (customConfig) {
      this.config = { ...defaultConfig, ...customConfig };
    } else {
      this.config = { ...defaultConfig };
    }
  }

  config: EtaConfig;

  RuntimeErr = RuntimeErr;

  compile = compile;
  compileToString = compileToString;
  compileBody = compileBody;
  parse = parse;
  render = render;
  renderAsync = renderAsync;
  renderString = renderString;
  renderStringAsync = renderStringAsync;

  filepathCache: Record<string, string> = {};
  templatesSync: Cacher<TemplateFunction> = new Cacher<TemplateFunction>({});
  templatesAsync: Cacher<TemplateFunction> = new Cacher<TemplateFunction>({});

  // resolvePath takes a relative path from the "views" directory
  resolvePath:
    | null
    | ((this: Eta, template: string, options?: Partial<Options>) => string) =
    null;
  readFile: null | ((this: Eta, path: string) => string) = null;

  // METHODS

  configure(customConfig: Partial<EtaConfig>) {
    this.config = { ...this.config, ...customConfig };
  }

  withConfig(customConfig: Partial<EtaConfig>): this & { config: EtaConfig } {
    return { ...this, config: { ...this.config, ...customConfig } };
  }

  loadTemplate(
    name: string,
    template: string | TemplateFunction, // template string or template function
    options?: { async: boolean },
  ): void {
    if (typeof template === "string") {
      const templates = options?.async
        ? this.templatesAsync
        : this.templatesSync;

      templates.define(name, this.compile(template, options));
    } else {
      let templates = this.templatesSync;

      if (template.constructor.name === "AsyncFunction" || options?.async) {
        templates = this.templatesAsync;
      }

      templates.define(name, template);
    }
  }
}

// for instance checking against thrown errors
export { EtaError };
```

## File: `src/parse.ts`
```typescript
import { ParseErr } from "./err.ts";
import type { Eta } from "./internal.ts";
import { trimWS } from "./utils.ts";

export type TagType = "r" | "e" | "i" | "";

export interface TemplateObject {
  t: TagType;
  val: string;
  lineNo?: number;
}

export type AstObject = string | TemplateObject;

/* END TYPES */

const templateLitReg =
  /`(?:\\[\s\S]|\${(?:[^{}]|{(?:[^{}]|{[^}]*})*})*}|(?!\${)[^\\`])*`/g;

const singleQuoteReg = /'(?:\\[\s\w"'\\`]|[^\n\r'\\])*?'/g;

const doubleQuoteReg = /"(?:\\[\s\w"'\\`]|[^\n\r"\\])*?"/g;

/** Escape special regular expression characters inside a string */

function escapeRegExp(string: string) {
  // From MDN
  return string.replace(/[.*+\-?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string
}

function getLineNo(str: string, index: number) {
  return str.slice(0, index).split("\n").length;
}

export function parse(this: Eta, str: string): Array<AstObject> {
  const config = this.config;

  let buffer: Array<AstObject> = [];
  let trimLeftOfNextStr: string | false = false;
  let lastIndex = 0;
  const parseOptions = config.parse;

  if (config.plugins) {
    for (let i = 0; i < config.plugins.length; i++) {
      const plugin = config.plugins[i];
      if (plugin.processTemplate) {
        str = plugin.processTemplate(str, config);
      }
    }
  }

  /* Adding for EJS compatibility */
  if (config.rmWhitespace) {
    // Code taken directly from EJS
    // Have to use two separate replaces here as `^` and `$` operators don't
    // work well with `\r` and empty lines don't work well with the `m` flag.
    // Essentially, this replaces the whitespace at the beginning and end of
    // each line and removes multiple newlines.
    str = str.replace(/[\r\n]+/g, "\n").replace(/^\s+|\s+$/gm, "");
  }
  /* End rmWhitespace option */

  templateLitReg.lastIndex = 0;
  singleQuoteReg.lastIndex = 0;
  doubleQuoteReg.lastIndex = 0;

  function pushString(strng: string, shouldTrimRightOfString?: string | false) {
    if (strng) {
      // if string is truthy it must be of type 'string'

      strng = trimWS(
        strng,
        config,
        trimLeftOfNextStr, // this will only be false on the first str, the next ones will be null or undefined
        shouldTrimRightOfString,
      );

      if (strng) {
        // replace \ with \\, ' with \'
        // we're going to convert all CRLF to LF so it doesn't take more than one replace

        strng = strng.replace(/\\|'/g, "\\$&").replace(/\r\n|\n|\r/g, "\\n");

        buffer.push(strng);
      }
    }
  }

  const prefixes = [
    parseOptions.exec,
    parseOptions.interpolate,
    parseOptions.raw,
  ].reduce((accumulator, prefix) => {
    if (accumulator && prefix) {
      return accumulator + "|" + escapeRegExp(prefix);
    } else if (prefix) {
      // accumulator is falsy
      return escapeRegExp(prefix);
    } else {
      // prefix and accumulator are both falsy
      return accumulator;
    }
  }, "");

  const parseOpenReg = new RegExp(
    escapeRegExp(config.tags[0]) + "(-|_)?\\s*(" + prefixes + ")?\\s*",
    "g",
  );

  const parseCloseReg = new RegExp(
    "'|\"|`|\\/\\*|(\\s*(-|_)?" + escapeRegExp(config.tags[1]) + ")",
    "g",
  );

  let m: RegExpExecArray | null;

  // biome-ignore lint/suspicious/noAssignInExpressions: this is performant
  while ((m = parseOpenReg.exec(str))) {
    const precedingString = str.slice(lastIndex, m.index);

    lastIndex = m[0].length + m.index;

    const wsLeft = m[1];
    const prefix = m[2] || ""; // by default either ~, =, or empty

    pushString(precedingString, wsLeft);

    parseCloseReg.lastIndex = lastIndex;
    let closeTag: RegExpExecArray | null;
    let currentObj: AstObject | false = false;

    // biome-ignore lint/suspicious/noAssignInExpressions: this is performant
    while ((closeTag = parseCloseReg.exec(str))) {
      if (closeTag[1]) {
        const content = str.slice(lastIndex, closeTag.index);

        parseOpenReg.lastIndex = lastIndex = parseCloseReg.lastIndex;

        trimLeftOfNextStr = closeTag[2];

        const currentType: TagType =
          prefix === parseOptions.exec
            ? "e"
            : prefix === parseOptions.raw
              ? "r"
              : prefix === parseOptions.interpolate
                ? "i"
                : "";

        currentObj = { t: currentType, val: content };
        break;
      } else {
        const char = closeTag[0];
        if (char === "/*") {
          const commentCloseInd = str.indexOf("*/", parseCloseReg.lastIndex);

          if (commentCloseInd === -1) {
            ParseErr("unclosed comment", str, closeTag.index);
          }
          parseCloseReg.lastIndex = commentCloseInd;
        } else if (char === "'") {
          singleQuoteReg.lastIndex = closeTag.index;

          const singleQuoteMatch = singleQuoteReg.exec(str);
          if (singleQuoteMatch) {
            parseCloseReg.lastIndex = singleQuoteReg.lastIndex;
          } else {
            ParseErr("unclosed string", str, closeTag.index);
          }
        } else if (char === '"') {
          doubleQuoteReg.lastIndex = closeTag.index;
          const doubleQuoteMatch = doubleQuoteReg.exec(str);

          if (doubleQuoteMatch) {
            parseCloseReg.lastIndex = doubleQuoteReg.lastIndex;
          } else {
            ParseErr("unclosed string", str, closeTag.index);
          }
        } else if (char === "`") {
          templateLitReg.lastIndex = closeTag.index;
          const templateLitMatch = templateLitReg.exec(str);
          if (templateLitMatch) {
            parseCloseReg.lastIndex = templateLitReg.lastIndex;
          } else {
            ParseErr("unclosed string", str, closeTag.index);
          }
        }
      }
    }
    if (currentObj) {
      if (config.debug) {
        currentObj.lineNo = getLineNo(str, m.index);
      }
      buffer.push(currentObj);
    } else {
      ParseErr("unclosed tag", str, m.index);
    }
  }

  pushString(str.slice(lastIndex, str.length), false);

  if (config.plugins) {
    for (let i = 0; i < config.plugins.length; i++) {
      const plugin = config.plugins[i];
      if (plugin.processAST) {
        buffer = plugin.processAST(buffer, config);
      }
    }
  }

  return buffer;
}
```

## File: `src/render.ts`
```typescript
import type { TemplateFunction } from "./compile.ts";

/* TYPES */
import type { Options } from "./config.ts";
import { EtaNameResolutionError } from "./err.ts";
import type { Eta } from "./internal.ts";

/* END TYPES */

function handleCache(
  this: Eta,
  template: string,
  options: Partial<Options>,
): TemplateFunction {
  const templateStore = options?.async
    ? this.templatesAsync
    : this.templatesSync;

  if (this.resolvePath && this.readFile && !template.startsWith("@")) {
    const templatePath = options.filepath as string;

    const cachedTemplate = templateStore.get(templatePath);

    if (this.config.cache && cachedTemplate) {
      return cachedTemplate;
    } else {
      const templateString = this.readFile(templatePath);

      const templateFn = this.compile(templateString, options);

      if (this.config.cache) templateStore.define(templatePath, templateFn);

      return templateFn;
    }
  } else {
    const cachedTemplate = templateStore.get(template);

    if (cachedTemplate) {
      return cachedTemplate;
    } else {
      throw new EtaNameResolutionError(`Failed to get template '${template}'`);
    }
  }
}

export function render<T extends object>(
  this: Eta,
  template: string | TemplateFunction, // template name or template function
  data: T,
  meta?: { filepath: string },
): string {
  let templateFn: TemplateFunction;
  const options = { ...meta, async: false };

  if (typeof template === "string") {
    if (this.resolvePath && this.readFile && !template.startsWith("@")) {
      options.filepath = this.resolvePath(template, options);
    }

    templateFn = handleCache.call(this, template, options);
  } else {
    templateFn = template;
  }

  const res = templateFn.call(this, data, options);

  return res;
}

export function renderAsync<T extends object>(
  this: Eta,
  template: string | TemplateFunction, // template name or template function
  data: T,
  meta?: { filepath: string },
): Promise<string> {
  let templateFn: TemplateFunction;
  const options = { ...meta, async: true };

  if (typeof template === "string") {
    if (this.resolvePath && this.readFile && !template.startsWith("@")) {
      options.filepath = this.resolvePath(template, options);
    }

    templateFn = handleCache.call(this, template, options);
  } else {
    templateFn = template;
  }

  const res = templateFn.call(this, data, options);

  // Return a promise
  return Promise.resolve(res);
}

export function renderString<T extends object>(
  this: Eta,
  template: string,
  data: T,
): string {
  const templateFn = this.compile(template, { async: false });

  return render.call(this, templateFn, data);
}

export function renderStringAsync<T extends object>(
  this: Eta,
  template: string,
  data: T,
): Promise<string> {
  const templateFn = this.compile(template, { async: true });

  return renderAsync.call(this, templateFn, data);
}
```

## File: `src/storage.ts`
```typescript
/**
 * Handles storage and accessing of values
 *
 * In this case, we use it to store compiled template functions
 * Indexed by their `name` or `filename`
 */

export class Cacher<T> {
  constructor(private cache: Record<string, T>) {}
  define(key: string, val: T): void {
    this.cache[key] = val;
  }
  get(key: string): T {
    return this.cache[key];
  }
  remove(key: string): void {
    delete this.cache[key];
  }
  reset(): void {
    this.cache = {};
  }
  load(cacheObj: Record<string, T>): void {
    this.cache = { ...this.cache, ...cacheObj };
  }
}
```

## File: `src/utils.ts`
```typescript
import type { EtaConfig } from "./config.ts";

/**
 * Takes a string within a template and trims it, based on the preceding tag's whitespace control and `config.autoTrim`
 */

export function trimWS(
  str: string,
  config: EtaConfig,
  wsLeft: string | false,
  wsRight?: string | false,
): string {
  let leftTrim: string | false;
  let rightTrim: string | false;

  if (Array.isArray(config.autoTrim)) {
    // Slightly confusing,
    // but _}} will trim the left side of the following string
    leftTrim = config.autoTrim[1];
    rightTrim = config.autoTrim[0];
  } else {
    leftTrim = rightTrim = config.autoTrim;
  }

  if (wsLeft || wsLeft === false) {
    leftTrim = wsLeft;
  }

  if (wsRight || wsRight === false) {
    rightTrim = wsRight;
  }

  if (!rightTrim && !leftTrim) {
    return str;
  }

  if (leftTrim === "slurp" && rightTrim === "slurp") {
    return str.trim();
  }

  if (leftTrim === "_" || leftTrim === "slurp") {
    // full slurp
    str = str.trimStart();
  } else if (leftTrim === "-" || leftTrim === "nl") {
    // nl trim
    str = str.replace(/^(?:\r\n|\n|\r)/, "");
  }

  if (rightTrim === "_" || rightTrim === "slurp") {
    // full slurp
    str = str.trimEnd();
  } else if (rightTrim === "-" || rightTrim === "nl") {
    // nl trim
    str = str.replace(/(?:\r\n|\n|\r)$/, "");
  }

  return str;
}

/**
 * A map of special HTML characters to their XML-escaped equivalents
 */

const escMap: { [key: string]: string } = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;",
};

function replaceChar(s: string): string {
  return escMap[s];
}

/**
 * XML-escapes an input value after converting it to a string
 *
 * @param str - Input value (usually a string)
 * @returns XML-escaped string
 */

export function XMLEscape(str: unknown): string {
  // To deal with XSS. Based on Escape implementations of Mustache.JS and Marko, then customized.
  const newStr = String(str);
  if (/[&<>"']/.test(newStr)) {
    return newStr.replace(/[&<>"']/g, replaceChar);
  } else {
    return newStr;
  }
}
```

## File: `test/compile-string.spec.ts`
```typescript
import { describe, expect, it } from "vitest";

import { Eta } from "../src/index";

const eta = new Eta();

const fs = require("node:fs"),
  path = require("node:path"),
  filePath = path.join(__dirname, "templates/complex.eta");

const complexTemplate = fs.readFileSync(filePath, "utf8");

describe("Compile to String test", () => {
  it("compiles a simple template", () => {
    const str = eta.compileToString("hi <%= it.name %>");
    expect(str).toEqual(`
let include = (__eta_t, __eta_d) => this.render(__eta_t, {...it, ...(__eta_d ?? {})}, options);
let includeAsync = (__eta_t, __eta_d) => this.renderAsync(__eta_t, {...it, ...(__eta_d ?? {})}, options);

let __eta = {res: "", e: this.config.escapeFunction, f: this.config.filterFunction};

function layout(path, data) {
  __eta.layout = path;
  __eta.layoutData = data;
}

function output(s){__eta.res+=s;}

__eta.res+='hi ';
__eta.res+=__eta.e(it.name);

if (__eta.layout) {
  __eta.res = include (__eta.layout, {...it, body: __eta.res, ...__eta.layoutData});
}

return __eta.res;
`);
  });

  it("compiles a simple template with a raw tag", () => {
    const str = eta.compileToString("hi <%~ it.name %>");
    expect(str).toEqual(`
let include = (__eta_t, __eta_d) => this.render(__eta_t, {...it, ...(__eta_d ?? {})}, options);
let includeAsync = (__eta_t, __eta_d) => this.renderAsync(__eta_t, {...it, ...(__eta_d ?? {})}, options);

let __eta = {res: "", e: this.config.escapeFunction, f: this.config.filterFunction};

function layout(path, data) {
  __eta.layout = path;
  __eta.layoutData = data;
}

function output(s){__eta.res+=s;}

__eta.res+='hi ';
__eta.res+=it.name;

if (__eta.layout) {
  __eta.res = include (__eta.layout, {...it, body: __eta.res, ...__eta.layoutData});
}

return __eta.res;
`);
  });

  it("works with whitespace trimming", () => {
    const str = eta.compileToString(
      "hi\n<%- = it.firstname-%>\n<%_ = it.lastname_%>",
    );
    expect(str).toEqual(`
let include = (__eta_t, __eta_d) => this.render(__eta_t, {...it, ...(__eta_d ?? {})}, options);
let includeAsync = (__eta_t, __eta_d) => this.renderAsync(__eta_t, {...it, ...(__eta_d ?? {})}, options);

let __eta = {res: "", e: this.config.escapeFunction, f: this.config.filterFunction};

function layout(path, data) {
  __eta.layout = path;
  __eta.layoutData = data;
}

function output(s){__eta.res+=s;}

__eta.res+='hi';
__eta.res+=__eta.e(it.firstname);
__eta.res+=__eta.e(it.lastname);

if (__eta.layout) {
  __eta.res = include (__eta.layout, {...it, body: __eta.res, ...__eta.layoutData});
}

return __eta.res;
`);
  });

  it("compiles complex template", () => {
    const str = eta.compileToString(complexTemplate);
    expect(str).toEqual(`
let include = (__eta_t, __eta_d) => this.render(__eta_t, {...it, ...(__eta_d ?? {})}, options);
let includeAsync = (__eta_t, __eta_d) => this.renderAsync(__eta_t, {...it, ...(__eta_d ?? {})}, options);

let __eta = {res: "", e: this.config.escapeFunction, f: this.config.filterFunction};

function layout(path, data) {
  __eta.layout = path;
  __eta.layoutData = data;
}

function output(s){__eta.res+=s;}

__eta.res+='Hi\\n';
console.log("Hope you like Eta!")
__eta.res+=__eta.e(it.htmlstuff);
__eta.res+='\\n';
for (var key in it.obj) {
__eta.res+='Value: ';
__eta.res+=__eta.e(it.obj[key]);
__eta.res+=', Key: ';
__eta.res+=__eta.e(key);
__eta.res+='\\n';
if (key === 'thirdchild') {
__eta.res+='  ';
for (var i = 0, arr = it.obj[key]; i < arr.length; i++) {
__eta.res+='      Salutations! Index: ';
__eta.res+=__eta.e(i);
__eta.res+=', parent key: ';
__eta.res+=__eta.e(key);
__eta.res+='      \\n  ';
}
}
}
__eta.res+='\\nThis is a partial: ';
__eta.res+=include("mypartial");

if (__eta.layout) {
  __eta.res = include (__eta.layout, {...it, body: __eta.res, ...__eta.layoutData});
}

return __eta.res;
`);
  });
});
```

## File: `test/compile.spec.ts`
```typescript
import { describe, expect, it, test } from "vitest";

import { Eta } from "../src/index";

const eta = new Eta();

const fs = require("node:fs"),
  path = require("node:path"),
  filePath = path.join(__dirname, "templates/complex.eta");

const complexTemplate = fs.readFileSync(filePath, "utf8");

describe("Compile test", () => {
  it("parses a simple template", () => {
    const str = eta.compile("hi <%= hey %>");
    expect(str).toBeTruthy();
  });

  it("works with plain string templates", () => {
    const str = eta.compile("hi this is a template");
    expect(str).toBeTruthy();
  });

  it("compiles complex template", () => {
    const str = eta.compile(complexTemplate);
    expect(str).toBeTruthy();
  });

  test("throws with bad inner JS syntax", () => {
    expect(() => {
      eta.compile("<% hi (=h) %>");
    }).toThrow();
  });
});
```

## File: `test/config.spec.ts`
```typescript
import { describe, expect, it } from "vitest";

import { Eta } from "../src/index";

describe("Config Tests", () => {
  it("custom tags", () => {
    const eta = new Eta({ tags: ["<<", ">>"] });
    const res = eta.renderString("hi <<= it.name >>", { name: "Ben" });
    expect(res).toEqual("hi Ben");
  });

  it("no autoescape", () => {
    const eta = new Eta({ autoEscape: false });
    const res = eta.renderString("<%= it.html %>", { html: "<p>Hi</p>" });
    expect(res).toEqual("<p>Hi</p>"); // not escaped
  });

  it("default filter function stringifies data", () => {
    const eta = new Eta();

    expect(eta.config.filterFunction({ a: 1 })).toEqual("[object Object]");
  });

  it("filter function", () => {
    const template = "My favorite food is <%= it.fav %>";
    const baseEta = new Eta();

    expect(baseEta.renderString(template, {})).toEqual(
      "My favorite food is undefined",
    );

    const etaWithSimpleFilter = new Eta({
      autoFilter: true,
      // turn every value into "apples"
      filterFunction: (_val) => "apples",
    });

    expect(etaWithSimpleFilter.renderString(template, {})).toEqual(
      "My favorite food is apples",
    );
  });

  it("complex filter function", () => {
    let timesFilterCalled = 0;
    const eta = new Eta({
      autoFilter: true,
      filterFunction: () => {
        timesFilterCalled++;
        if (timesFilterCalled <= 1) {
          return "The first";
        } else {
          return "another";
        }
      },
    });

    expect(
      eta.renderString("<%= it.val1 %>, <%~ it.val2 %>, <%~ it.val3 %>", {}),
    ).toEqual("The first, another, another");
  });

  it("withConfig", () => {
    const eta = new Eta();

    const res = eta
      .withConfig({ tags: ["{{", "}}"] })
      .renderString("{{= it.name }}", { name: "John Appleseed" });

    expect(res).toEqual("John Appleseed");

    // the original tags should remain unchanged
    expect(eta.config.tags).toEqual(["<%", "%>"]);
  });

  it("configure", () => {
    const eta = new Eta();

    eta.configure({ tags: ["{{", "}}"] });

    const res = eta.renderString("{{= it.name }}", { name: "John Appleseed" });

    expect(res).toEqual("John Appleseed");

    // the original tags should have changed
    expect(eta.config.tags).toEqual(["{{", "}}"]);
  });
});
```

## File: `test/err.spec.ts`
```typescript
import path from "node:path";
import { describe, expect, it } from "vitest";
import {
  Eta,
  EtaError,
  EtaFileResolutionError,
  EtaNameResolutionError,
  EtaParseError,
  EtaRuntimeError,
} from "../src/index";

describe("ParseErr", () => {
  const eta = new Eta();

  it("error while parsing - renderString", () => {
    try {
      eta.renderString("template <%", {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaError);
      expect(ex).toBeInstanceOf(EtaParseError);
      expect((ex as EtaParseError).name).toBe("EtaParser Error");
      expect((ex as EtaParseError).message).toBe(`unclosed tag at line 1 col 10:

  template <%
           ^`);
      expect(ex instanceof Error).toBe(true);
    }
  });

  it("error while parsing - compile", () => {
    try {
      eta.compile("template <%");
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaError);
      expect(ex).toBeInstanceOf(EtaParseError);
      expect((ex as EtaParseError).name).toBe("EtaParser Error");
      expect((ex as EtaParseError).message).toBe(`unclosed tag at line 1 col 10:

  template <%
           ^`);
      expect(ex instanceof Error).toBe(true);
    }
  });
});

describe("RuntimeErr", () => {
  const eta = new Eta({
    debug: true,
    views: path.join(__dirname, "templates"),
  });

  const errorFilepath = path.join(__dirname, "templates/runtime-error.eta");

  it("error throws correctly", () => {
    try {
      eta.render("./runtime-error", {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaError);
      expect(ex).toBeInstanceOf(EtaRuntimeError);
      expect((ex as EtaRuntimeError).name).toBe("ReferenceError");
      expect((ex as EtaRuntimeError).message).toBe(`${errorFilepath}:2
    1| 
 >> 2| <%= undefinedVariable %>
    3| Lorem Ipsum

undefinedVariable is not defined`);
    }
  });
});

describe("EtaFileResolutionError", () => {
  it("error throws correctly when template does not exist", () => {
    const eta = new Eta({
      debug: true,
      views: path.join(__dirname, "templates"),
    });
    const errorFilepath = path.join(
      __dirname,
      "templates/not-existing-template.eta",
    );

    try {
      eta.render("./not-existing-template", {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaError);
      expect(ex).toBeInstanceOf(EtaFileResolutionError);
      expect((ex as EtaFileResolutionError).name).toBe(
        "EtaFileResolution Error",
      );
      expect((ex as EtaFileResolutionError).message).toBe(
        `Could not find template: ${errorFilepath}`,
      );
    }
  });

  it("error throws correctly when views options is missing", async () => {
    const eta = new Eta({ debug: true });
    try {
      eta.render("Hi", {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaFileResolutionError);
      expect((ex as EtaFileResolutionError).name).toBe(
        "EtaFileResolution Error",
      );
      expect((ex as EtaFileResolutionError).message).toBe(
        "Views directory is not defined",
      );
    }

    try {
      await eta.renderAsync("Hi", {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaFileResolutionError);
      expect((ex as EtaFileResolutionError).name).toBe(
        "EtaFileResolution Error",
      );
      expect((ex as EtaFileResolutionError).message).toBe(
        "Views directory is not defined",
      );
    }
  });

  it("error throws correctly when template in not in th view directory", () => {
    const eta = new Eta({
      debug: true,
      views: path.join(__dirname, "templates"),
    });

    const filePath = "../../../simple.eta";
    try {
      eta.render(filePath, {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaFileResolutionError);
      expect((ex as EtaFileResolutionError).name).toBe(
        "EtaFileResolution Error",
      );
      expect((ex as EtaFileResolutionError).message).toBe(
        `Template '${filePath}' is not in the views directory`,
      );
    }
  });
});

describe("EtaNameResolutionError", () => {
  const eta = new Eta({
    debug: true,
    views: path.join(__dirname, "templates"),
  });

  it("error throws correctly", () => {
    const template = "@not-existing-tp";

    try {
      eta.render(template, {});
    } catch (ex) {
      expect(ex).toBeInstanceOf(EtaNameResolutionError);
      expect((ex as EtaNameResolutionError).name).toBe(
        "EtaNameResolution Error",
      );
      expect((ex as EtaNameResolutionError).message).toBe(
        `Failed to get template '${template}'`,
      );
    }
  });
});
```

## File: `test/file-handling.spec.ts`
```typescript
import path from "node:path";
import { describe, expect, it } from "vitest";

import { Eta } from "../src/index";

const viewsDir = path.join(__dirname, "templates");

const eta = new Eta({ views: viewsDir, cache: true });

describe("Filepath caching", () => {
  it("Filepath caching works as expected", async () => {
    // This test renders templates/has-include.eta with caching enabled, then checks to make sure
    // `config.filepathCache` contains the expected result afterward

    const templateResult = eta.render("has-include", {});

    expect(templateResult).toEqual(
      `This is the outermost template. Now we'll include a partial

===========================================================
This is a partial.
Hi Test Runner`,
    );

    // The cache is indexed by {filename, path, root, views} (JSON.stringify ignores keys with undefined as their value)

    // Filepath caching is based on the premise that given the same path, includer filename, root directory, and views directory (or directories)
    // the getPath function will always return the same result (assuming that caching is enabled and we're not expecting the templates to change)

    const pathToPartial = `{"filename":${JSON.stringify(path.join(viewsDir, "has-include.eta"))},"path":"./partial","views":${JSON.stringify(viewsDir)}}`;

    const pathToSimple = `{"filename":${JSON.stringify(path.join(viewsDir, "partial.eta"))},"path":"./simple","views":${JSON.stringify(viewsDir)}}`;

    expect(eta.filepathCache).toEqual({
      [pathToPartial]: path.join(viewsDir, "partial.eta"),
      [pathToSimple]: path.join(viewsDir, "simple.eta"),
    });
  });
});

describe("file handling errors", () => {
  const eta = new Eta({ views: viewsDir });

  it("throws if accessing a file outside the views directory", () => {
    expect(() => {
      eta.render("../../sensitive-file.json", {});
    }).toThrow();
  });

  it("throws if accessing a partial outside the views directory", () => {
    expect(() => {
      eta.render("out-of-views-dir", {});
    }).toThrow();
  });

  it("throws if template doesn't exist", () => {
    expect(() => {
      eta.render("nonexistent.eta", {});
    }).toThrow(/Could not find template/);
  });

  it("throws if views directory isn't defined", () => {
    const testEta = new Eta();

    expect(() => {
      testEta.render("simple.eta", {});
    }).toThrow();
  });
});

describe("filepath default extension tests", () => {
  console.log("Templates are in ", viewsDir);

  it("works with defaultExtension", async () => {
    const eta = new Eta({
      views: viewsDir,
      cache: true,
      defaultExtension: ".tmpl",
    });
    const templateResult = await eta.render("template-extn", {
      name: "TMPL Run",
    });

    expect(templateResult).toEqual(`Hi TMPL Run`);
  });

  it("works with no extension", async () => {
    const eta = new Eta({ views: viewsDir, cache: true, defaultExtension: "" });
    const templateResult = await eta.render("template-without-extn", {
      name: "TMPL Run",
    });

    expect(templateResult).toEqual(`Hi TMPL Run`);
  });
});
```

## File: `test/parse.spec.ts`
```typescript
import fs from "node:fs";
import path from "node:path";
import { describe, expect, it, test } from "vitest";

import { Eta } from "../src/index";

const eta = new Eta();

const filePath = path.join(__dirname, "templates/complex.eta");

const complexTemplate = fs.readFileSync(filePath, "utf8");

describe("parse test", () => {
  it("parses a simple template", () => {
    const buff = eta.parse("hi <%= hey %>");
    expect(buff).toEqual(["hi ", { val: "hey", t: "i" }]);
  });

  it("parses a raw tag", () => {
    const buff = eta.parse("hi <%~ hey %>");
    expect(buff).toEqual(["hi ", { val: "hey", t: "r" }]);
  });

  it("works with whitespace trimming", () => {
    const buff = eta.parse("hi\n<%- = hey-%> <%_ = hi _%>");
    expect(buff).toEqual(["hi", { val: "hey", t: "i" }, { val: "hi", t: "i" }]);
  });

  it("works with multiline comments", () => {
    const buff = eta.parse("hi <% /* comment contains delimiter %> */ %>");
    expect(buff).toEqual([
      "hi ",
      { val: "/* comment contains delimiter %> */", t: "e" },
    ]);
  });

  it("parses with simple template literal", () => {
    // biome-ignore lint/suspicious/noTemplateCurlyInString: intentional
    const buff = eta.parse("hi <%= `template %> ${value}` %>");
    // biome-ignore lint/suspicious/noTemplateCurlyInString: intentional
    expect(buff).toEqual(["hi ", { val: "`template %> ${value}`", t: "i" }]);
  });

  it("compiles complex template", () => {
    const buff = eta.parse(complexTemplate);
    expect(buff).toEqual([
      "Hi\\n",
      { t: "e", val: 'console.log("Hope you like Eta!")' },
      { t: "i", val: "it.htmlstuff" },
      "\\n",
      { t: "e", val: "for (var key in it.obj) {" },
      "Value: ",
      { t: "i", val: "it.obj[key]" },
      ", Key: ",
      { t: "i", val: "key" },
      "\\n",
      { t: "e", val: "if (key === 'thirdchild') {" },
      "  ",
      {
        t: "e",
        val: "for (var i = 0, arr = it.obj[key]; i < arr.length; i++) {",
      },
      "      Salutations! Index: ",
      { t: "i", val: "i" },
      ", parent key: ",
      { t: "i", val: "key" },
      "      \\n  ",
      { t: "e", val: "}" },
      { t: "e", val: "}" },
      { t: "e", val: "}" },
      "\\nThis is a partial: ",
      { t: "r", val: 'include("mypartial")' },
    ]);
  });

  test("throws with unclosed tag", () => {
    expect(() => {
      eta.parse('<%hi("hey")');
    }).toThrowError("hi");
  });

  test("throws with unclosed single-quote string", () => {
    expect(() => {
      eta.parse("<%= ' %>");
    }).toThrowError(`unclosed string at line 1 col 5:

  <%= ' %>
      ^`);
  });

  test("throws with unclosed double-quote string", () => {
    expect(() => {
      eta.parse('<%= " %>');
    }).toThrowError(`unclosed string at line 1 col 5:

  <%= " %>
      ^`);
  });

  test("throws with unclosed template literal", () => {
    expect(() => {
      eta.parse("<%= ` %>");
    }).toThrowError(`unclosed string at line 1 col 5:

  <%= \` %>
      ^`);
  });

  test("throws with unclosed multi-line comment", () => {
    expect(() => {
      eta.parse("<%= /* %>");
    }).toThrowError(`unclosed comment at line 1 col 5:

  <%= /* %>
      ^`);
  });
});
```

## File: `test/plugins.spec.ts`
```typescript
import { describe, expect, it } from "vitest";

import type { EtaConfig } from "../src/config";
import { Eta } from "../src/index";
import type { AstObject } from "../src/parse";

function myPlugin() {
  return {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    processAST: (ast: Array<AstObject>, _env?: EtaConfig) => {
      ast.push("String to append");
      return ast;
    },
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    processFnString: (str: string, _env?: EtaConfig) => {
      return str.replace(/@@num@@/, "2352.3");
    },
  };
}

const emojiTransform = () => {
  return {
    processTemplate: (str: string) => str.replace(":thumbsup:", "👍"),
  };
};

const capitalizeCool = () => {
  return {
    processTemplate: (str: string) => str.replace("cool", "COOL"),
  };
};

const replaceThumbsUp = () => {
  return {
    processTemplate: (str: string) => str.replace("👍", "✨"),
  };
};

describe("Plugins", () => {
  it("Plugins function properly", () => {
    const eta = new Eta({ plugins: [myPlugin()] });
    const template = `<%= it.val %> <%= @@num@@ %>.`;

    expect(eta.renderString(template, { val: "value" })).toEqual(
      "value 2352.3.String to append",
    );
  });
});

describe("processTemplate plugin", () => {
  it("Simple plugin works correctly", () => {
    const eta = new Eta({ plugins: [emojiTransform()] });
    const template = ":thumbsup:";

    const res = eta.renderString(template, {});

    expect(res).toEqual("👍");
  });

  it("Multiple chained plugins work correctly", () => {
    const eta = new Eta({
      plugins: [emojiTransform(), capitalizeCool(), replaceThumbsUp()],
    });
    const template = ":thumbsup: This is a cool template";

    const res = eta.renderString(template, {});

    expect(res).toEqual("✨ This is a COOL template");
  });
});
```

## File: `test/render.spec.ts`
```typescript
import path from "node:path";
import { describe, expect, it } from "vitest";

import { Eta } from "../src/index";

interface SimpleEtaTemplate {
  greeting?: string;
  name: string;
}

describe("basic functionality", () => {
  const eta = new Eta();

  it("renderString: template compiles", () => {
    expect(
      eta.renderString("Hi <%= it.name%>", { name: "Ada Lovelace" }),
    ).toEqual("Hi Ada Lovelace");
  });
  it("renderString: string trimming", () => {
    expect(
      eta.renderString("Hi \n<%- =it.name_%>  !", { name: "Ada Lovelace" }),
    ).toEqual("Hi Ada Lovelace!");
  });
  it("render: passing in a template function", () => {
    expect(
      eta.render(eta.compile("Hi \n<%- =it.name_%>  !"), {
        name: "Ada Lovelace",
      }),
    ).toEqual("Hi Ada Lovelace!");
  });
});

describe("render caching", () => {
  const eta = new Eta({ cache: true });

  eta.loadTemplate("@template1", "Hi <%=it.name%>");

  it("Simple template caches", () => {
    expect(eta.render("@template1", { name: "Ada Lovelace" })).toEqual(
      "Hi Ada Lovelace",
    );

    expect(eta.templatesSync.get("@template1")).toBeTruthy();
  });

  it("throws if template doesn't exist", () => {
    expect(() => {
      eta.render("@should-error", {});
    }).toThrow(/Failed to get template/);
  });
});

describe("render caching w/ files", () => {
  const eta = new Eta({
    cache: true,
    views: path.join(__dirname, "templates"),
  });

  eta.loadTemplate(
    path.join(__dirname, "templates/nonexistent.eta"),
    "Hi <%=it.name%>",
  );

  it("Template files cache", () => {
    expect(eta.render("./nonexistent", { name: "Ada Lovelace" })).toEqual(
      "Hi Ada Lovelace",
    );
  });
});

describe("useWith", () => {
  it("Puts `it` in global scope with env.useWith", () => {
    const etaWithUseWith = new Eta({ useWith: true });

    expect(
      etaWithUseWith.renderString("Hi <%=name%>", { name: "Ada Lovelace" }),
    ).toEqual("Hi Ada Lovelace");
  });
});

function resolveAfter2Seconds(val: string): Promise<string> {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(val);
    }, 20);
  });
}

async function asyncTest() {
  const result = await resolveAfter2Seconds("HI FROM ASYNC");
  return result;
}

describe("async", () => {
  const eta = new Eta();

  it("compiles asynchronously", async () => {
    expect(
      await eta.renderStringAsync("Hi <%= it.name %>", {
        name: "Ada Lovelace",
      }),
    ).toEqual("Hi Ada Lovelace");
  });

  it("async function works", async () => {
    expect(
      await eta.renderStringAsync("<%= await it.asyncTest() %>", {
        asyncTest: asyncTest,
      }),
    ).toEqual("HI FROM ASYNC");
  });

  it("Async template w/ syntax error throws", async () => {
    await expect(async () => {
      await eta.renderStringAsync("<%= @#$%^ %>", {});
    }).rejects.toThrow();
  });
});

describe("layouts", () => {
  const eta = new Eta({ views: path.join(__dirname, "templates") });

  it("Nested layouts work as expected", () => {
    const res = eta.render("index.eta", { title: "Cool Title" });

    expect(res).toEqual(`<!DOCTYPE html>
<html lang="en">
<head>
    <title>Cool Title</title>
</head>
<body>
This is the template body.
</body>
</html>`);
  });

  it("Layouts are called with arguments if they're provided", async () => {
    eta.loadTemplate(
      "@my-layout",
      `<%= it.title %> - <%~ it.body %> - <%~ it.content %> - <%~ it.randomNum %>`,
    );

    const res = await eta.renderString(
      `<% layout("@my-layout", { title: 'Nifty title', content: 'Nice content'}) %>
This is a layout`,
      { title: "Cool Title", randomNum: 3 },
    );

    // Note that layouts automatically accept the data of the template which called them,
    // after it is merged with `it` and { body:__eta.res }

    expect(res).toEqual("Nifty title - This is a layout - Nice content - 3");
  });
});

describe("file rendering", () => {
  const eta = new Eta({ views: path.join(__dirname, "templates") });

  it("renders template file properly", () => {
    const res = eta.render<SimpleEtaTemplate>("simple.eta", { name: "friend" });

    expect(res).toEqual("Hi friend");
  });

  it("renders async template file properly", async () => {
    const res = await eta.renderAsync("async.eta", {});

    expect(res).toEqual(`ASYNC CONTENT BELOW!



HI FROM ASYNC`);
  });
});

describe("import values merging", () => {
  const eta = new Eta({ views: path.join(__dirname, "templates") });
  eta.loadTemplate("@simple", "<%= it.greeting ?? 'Hi' %> <%= it.name %>");
  eta.loadTemplate(
    "@partial",
    "This is a partial.\n<%~ include('@simple', {name: 'Test Runner'}) %>\n",
  );
  eta.loadTemplate(
    "@partial-merge",
    "This is a partial.\n<%~ include('@simple', {greeting: 'Hello'}) %>\n",
  );
  eta.loadTemplate(
    "@partial-pass-data",
    "This is a partial.\n<%~ include('@simple') %>",
  );

  it("can override value", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial", {
      greeting: "Hello",
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello Test Runner");
  });

  it("merges values", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial-merge", {
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello friend");
  });

  it("passes original values", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial-pass-data", {
      greeting: "Hello",
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello friend");
  });
});

describe("import values merging with varName data", () => {
  const eta = new Eta({
    varName: "data",
    views: path.join(__dirname, "templates"),
  });

  eta.loadTemplate("@simple", "<%= data.greeting ?? 'Hi' %> <%= data.name %>");
  eta.loadTemplate(
    "@partial",
    "This is a partial.\n<%~ include('@simple', {name: 'Test Runner'}) %>\n",
  );
  eta.loadTemplate(
    "@partial-merge",
    "This is a partial.\n<%~ include('@simple', {greeting: 'Hello'}) %>\n",
  );
  eta.loadTemplate(
    "@partial-pass-data",
    "This is a partial.\n<%~ include('@simple') %>",
  );

  it("can override value", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial", {
      greeting: "Hello",
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello Test Runner");
  });

  it("merges values", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial-merge", {
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello friend");
  });

  it("passes original values", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial-pass-data", {
      greeting: "Hello",
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello friend");
  });
});

describe("import values merging with the useWith", () => {
  const eta = new Eta({
    useWith: true,
    views: path.join(__dirname, "templates"),
  });

  eta.loadTemplate(
    "@simple",
    "<%= typeof greeting !== 'undefined' ? greeting : 'Hi' %> <%= name %>",
  );
  eta.loadTemplate(
    "@partial",
    "This is a partial.\n<%~ include('@simple', {name: 'Test Runner'}) %>\n",
  );
  eta.loadTemplate(
    "@partial-merge",
    "This is a partial.\n<%~ include('@simple', {greeting: 'Hello'}) %>\n",
  );
  eta.loadTemplate(
    "@partial-pass-data",
    "This is a partial.\n<%~ include('@simple') %>",
  );

  it("can override value", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial", {
      greeting: "Hello",
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello Test Runner");
  });

  it("merges values", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial-merge", {
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello friend");
  });

  it("passes original values", () => {
    const res = eta.render<SimpleEtaTemplate>("@partial-pass-data", {
      greeting: "Hello",
      name: "friend",
    });

    expect(res).toEqual("This is a partial.\nHello friend");
  });
});

describe("forEach loops in included templates", () => {
  const eta = new Eta();

  it("renders forEach loop inside included partial", () => {
    eta.loadTemplate(
      "@loop-partial",
      `<ul>
<% (it.items || []).forEach(item => { %>
<li><%= item %></li>
<% }) %>
</ul>`,
    );

    eta.loadTemplate(
      "@loop-main",
      `<%~ include('@loop-partial', {items: ['a', 'b', 'c']}) %>`,
    );

    const result = eta.render("@loop-main", {});

    expect(result).toContain("<li>a</li>");
    expect(result).toContain("<li>b</li>");
    expect(result).toContain("<li>c</li>");
  });

  it("renders includes called from within a forEach loop", () => {
    eta.loadTemplate(
      "@nested-partial",
      `<div>
<% (it.question.items || []).forEach(opt => { %>
<span><%= opt %></span>
<% }) %>
</div>`,
    );

    eta.loadTemplate(
      "@nested-main",
      `<% [{items: ['a', 'b']}, {items: ['c', 'd']}].forEach(q => { %>
<%~ include('@nested-partial', {question: q}) %>
<% }) %>`,
    );

    const result = eta.render("@nested-main", {});

    expect(result).toContain("<span>a</span>");
    expect(result).toContain("<span>b</span>");
    expect(result).toContain("<span>c</span>");
    expect(result).toContain("<span>d</span>");
  });
});
```

## File: `test/storage.spec.ts`
```typescript
import { describe, expect, it } from "vitest";

import { Cacher } from "../src/storage";

const Container = new Cacher<number>({ one: 1, two: 2 });

describe("Config Tests", () => {
  it("Cache.get works", () => {
    expect(Container.get("one")).toEqual(1);
  });

  it("Cache.define works", () => {
    Container.define("three", 3);
    expect(Container.get("three")).toEqual(3);
  });

  it("Cache.remove works", () => {
    Container.remove("one");
    expect(Container.get("one")).toEqual(undefined);
  });

  it("Cache.reset works", () => {
    Container.reset();
    expect(Container.get("two")).toEqual(undefined);
  });

  it("Cache.load works", () => {
    Container.reset();
    Container.load({ seven: 7, eight: 8 });
    expect(Container.get("eight")).toEqual(8);
  });
});
```

## File: `test/utils.spec.ts`
```typescript
import { describe, expect, it } from "vitest";

import { defaultConfig } from "../src/config";
import { trimWS, XMLEscape } from "../src/utils";

describe("Whitespace trim", () => {
  describe("#trimLeft", () => {
    it("WS slurp with str.trimLeft", () => {
      expect(trimWS("  jestjs", defaultConfig, "_")).toBe("jestjs");
    });
    it("WS slurp without str.trimLeft", () => {
      Object.defineProperty(String.prototype, "trimLeft", { value: undefined });
      expect(trimWS("  jestjs", defaultConfig, "_")).toBe("jestjs");
    });
    it("WS newline", () => {
      expect(trimWS("\njestjs", defaultConfig, "-")).toBe("jestjs");
    });
    it("WS slurp and WS newline are equal with newline", () => {
      Object.defineProperty(String.prototype, "trimLeft", { value: undefined });
      expect(trimWS(" jestjs", defaultConfig, "_")).toBe(
        trimWS("\njestjs", defaultConfig, "-"),
      );
    });
  });

  describe("#trimRight", () => {
    it("WS slurp with str.trimRight", () => {
      expect(trimWS("jestjs  ", defaultConfig, "", "_")).toBe("jestjs");
    });
    it("WS slurp without str.trimRight", () => {
      Object.defineProperty(String.prototype, "trimRight", {
        value: undefined,
      });
      expect(trimWS("jestjs  ", defaultConfig, "", "_")).toBe("jestjs");
    });
    it("WS newline", () => {
      expect(trimWS("jestjs\n", defaultConfig, "", "-")).toBe("jestjs");
    });
    it("WS slurp and WS newline are equal with newline", () => {
      Object.defineProperty(String.prototype, "trimRight", {
        value: undefined,
      });
      expect(trimWS("jestjs ", defaultConfig, "", "_")).toBe(
        trimWS("jestjs\n", defaultConfig, "", "-"),
      );
    });
  });

  describe("#trim", () => {
    it("WS slurp both sides", () => {
      expect(
        trimWS(
          " somestring  ",
          { ...defaultConfig, autoTrim: ["slurp", "slurp"] },
          "",
          "",
        ),
      ).toBe("somestring");
    });

    it("defaultConfig.autoTrim set to false", () => {
      expect(
        trimWS(
          " some string\n  ",
          { ...defaultConfig, autoTrim: false },
          "",
          "",
        ),
      ).toBe(" some string\n  ");
    });
  });
});

describe("HTML Escape", () => {
  it("properly escapes HTML characters", () => {
    expect(XMLEscape("<p>HTML</p>")).toBe("&lt;p&gt;HTML&lt;/p&gt;");
    expect(XMLEscape("no html here")).toBe("no html here");
  });
});
```

## File: `test/templates/async-partial.eta`
```
<% function resolveAfter2Seconds(val) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(val);
    }, 20);
  });
} %>

<% async function asyncTest() {
  const result = await resolveAfter2Seconds("HI FROM ASYNC");
  return result;
} %>

<%= await asyncTest() %>
```

## File: `test/templates/async.eta`
```
ASYNC CONTENT BELOW!

<%= await includeAsync("./async-partial") %>
```

## File: `test/templates/complex.eta`
```
Hi
<% console.log("Hope you like Eta!") %>
<%= it.htmlstuff %>

<% for (var key in it.obj) { %>
Value: <%= it.obj[key] %>, Key: <%= key %>

<% if (key === 'thirdchild') { %>
  <% for (var i = 0, arr = it.obj[key]; i < arr.length; i++) { %>
      Salutations! Index: <%= i %>, parent key: <%= key %>
      
  <% } %>
<% } %>
<% } %>

This is a partial: <%~ include("mypartial") %>
```

## File: `test/templates/has-include.eta`
```
This is the outermost template. Now we'll include a partial

===========================================================
<%~ include('./partial') %>
```

## File: `test/templates/index.eta`
```
<% layout('./layout') %>
This is the template body.
```

## File: `test/templates/layout.eta`
```
<% layout('./outer-layout') %>
<head>
    <title><%= it.title %></title>
</head>
<body>
<%~ it.body %>
</body>
```

## File: `test/templates/out-of-views-dir.eta`
```
<% include("../../sensitive-file.json") %>
```

## File: `test/templates/outer-layout.eta`
```
<!DOCTYPE html>
<html lang="en">
<%~ it.body %>
</html>
```

## File: `test/templates/partial.eta`
```
This is a partial.
<%~ include('./simple', {name: 'Test Runner'}) %>
```

## File: `test/templates/runtime-error.eta`
```

<%= undefinedVariable %>
Lorem Ipsum
```

## File: `test/templates/simple.eta`
```
Hi <%= it.name %>
```

## File: `test/templates/template-extn.tmpl`
```
Hi <%= it.name %>
```

## File: `test/templates/template-without-extn`
```
Hi <%= it.name %>
```

