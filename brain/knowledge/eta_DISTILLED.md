---
id: eta
type: knowledge
owner: OA_Triage
---
# eta
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: README.md
```md
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

### File: .release-please-manifest.json
```json
{".":"4.5.1"}

```

### File: biome.json
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

### File: CHANGELOG.md
```md
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

### File: jsr.json
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

### File: pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    devDependencies:
      '@biomejs/biome':
        specifier: 2.3.5
        version: 2.3.5
      '@size-limit/preset-small-lib':
        specifier: ^11.2.0
        version: 11.2.0(size-limit@11.2.0)
      '@types/node':
        specifier: ^24.10.1
        version: 24.10.1
      '@vitest/coverage-istanbul':
        specifier: 4.0.8
        version: 4.0.8(vitest@4.0.8(@types/node@24.10.1)(jiti@2.6.1)(terser@5.44.0))
      size-limit:
        specifier: ^11.2.0
        version: 11.2.0
      tsdown:
        specifier: ^0.16.4
        version: 0.16.4(ms@2.1.3)(typescript@5.9.3)
      typescript:
        specifier: ^5.9.3
        version: 5.9.3
      vitest:
        specifier: ^4.0.8
        version: 4.0.8(@types/node@24.10.1)(jiti@2.6.1)(terser@5.44.0)

packages:

  '@babel/code-frame@7.27.1':
    resolution: {integrity: sha512-cjQ7ZlQ0Mv3b47hABuTevyTuYN4i+loJKGeV9flcCgIK37cCXRh+L1bd3iBHlynerhQ7BhCkn2BPbQUL+rGqFg==}
    engines: {node: '>=6.9.0'}

  '@babel/compat-data@7.28.5':
    resolution: {integrity: sha512-6uFXyCayocRbqhZOB+6XcuZbkMNimwfVGFji8CTZnCzOHVGvDqzvitu1re2AU5LROliz7eQPhB8CpAMvnx9EjA==}
    engines: {node: '>=6.9.0'}

  '@babel/core@7.28.5':
    resolution: {integrity: sha512-e7jT4DxYvIDLk1ZHmU/m/mB19rex9sv0c2ftBtjSBv+kVM/902eh0fINUzD7UwLLNR+jU585GxUJ8/EBfAM5fw==}
    engines: {node: '>=6.9.0'}

  '@babel/generator@7.28.5':
    resolution: {integrity: sha512-3EwLFhZ38J4VyIP6WNtt2kUdW9dokXA9Cr4IVIFHuCpZ3H8/YFOl5JjZHisrn1fATPBmKKqXzDFvh9fUwHz6CQ==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-compilation-targets@7.27.2':
    resolution: {integrity: sha512-2+1thGUUWWjLTYTHZWK1n8Yga0ijBz1XAhUXcKy81rd5g6yh7hGqMp45v7cadSbEHc9G3OTv45SyneRN3ps4DQ==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-globals@7.28.0':
    resolution: {integrity: sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-imports@7.27.1':
    resolution: {integrity: sha512-0gSFWUPNXNopqtIPQvlD5WgXYI5GY2kP2cCvoT8kczjbfcfuIljTbcWrulD1CIPIX2gt1wghbDy08yE1p+/r3w==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-transforms@7.28.3':
    resolution: {integrity: sha512-gytXUbs8k2sXS9PnQptz5o0QnpLL51SwASIORY6XaBKF88nsOT0Zw9szLqlSGQDP/4TljBAD5y98p2U1fqkdsw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-string-parser@7.27.1':
    resolution: {integrity: sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.28.5':
    resolution: {integrity: sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-option@7.27.1':
    resolution: {integrity: sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==}
    engines: {node: '>=6.9.0'}

  '@babel/helpers@7.28.4':
    resolution: {integrity: sha512-HFN59MmQXGHVyYadKLVumYsA9dBFun/ldYxipEjzA4196jpLZd8UjEEBLkbEkvfYreDqJhZxYAWFPtrfhNpj4w==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.28.5':
    resolution: {integrity: sha512-KKBU1VGYR7ORr3At5HAtUQ+TV3SzRCXmA/8OdDZiLDBIZxVyzXuztPjfLd3BV1PRAQGCMWWSHYhL0F8d5uHBDQ==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/template@7.27.2':
    resolution: {integrity: sha512-LPDZ85aEJyYSd18/DkjNh4/y1ntkE5KwUHWTiqgRxruuZL2F1yuHligVHLvcHY2vMHXttKFpJn6LwfI7cw7ODw==}
    engines: {node: '>=6.9.0'}

  '@babel/traverse@7.28.5':
    resolution: {integrity: sha512-TCCj4t55U90khlYkVV/0TfkJkAkUg3jZFA3Neb7unZT8CPok7iiRfaX0F+WnqWqt7OxhOn0uBKXCw4lbL8W0aQ==}
    engines: {node: '>=6.9.0'}

  '@babel/types@7.28.5':
    resolution: {integrity: sha512-qQ5m48eI/MFLQ5PxQj4PFaprjyCTLI37ElWMmNs0K8Lk3dVeOdNpB3ks8jc7yM5CDmVC73eMVk/trk3fgmrUpA==}
    engines: {node: '>=6.9.0'}

  '@biomejs/biome@2.3.5':
    resolution: {integrity: sha512-HvLhNlIlBIbAV77VysRIBEwp55oM/QAjQEin74QQX9Xb259/XP/D5AGGnZMOyF1el4zcvlNYYR3AyTMUV3ILhg==}
    engines: {node: '>=14.21.3'}
    hasBin: true

  '@biomejs/cli-darwin-arm64@2.3.5':
    resolution: {integrity: sha512-fLdTur8cJU33HxHUUsii3GLx/TR0BsfQx8FkeqIiW33cGMtUD56fAtrh+2Fx1uhiCsVZlFh6iLKUU3pniZREQw==}
    engines: {node: '>=14.21.3'}
    cpu: [arm64]
    os: [darwin]

  '@biomejs/cli-darwin-x64@2.3.5':
    resolution: {integrity: sha512-qpT8XDqeUlzrOW8zb4k3tjhT7rmvVRumhi2657I2aGcY4B+Ft5fNwDdZGACzn8zj7/K1fdWjgwYE3i2mSZ+vOA==}
    engines: {node: '>=14.21.3'}
    cpu: [x64]
    os: [darwin]

  '@biomejs/cli-linux-arm64-musl@2.3.5':
    resolution: {integrity: sha512-eGUG7+hcLgGnMNl1KHVZUYxahYAhC462jF/wQolqu4qso2MSk32Q+QrpN7eN4jAHAg7FUMIo897muIhK4hXhqg==}
    engines: {node: '>=14.21.3'}
    cpu: [arm64]
    os: [linux]

  '@biomejs/cli-linux-arm64@2.3.5':
    resolution: {integrity: sha512-u/pybjTBPGBHB66ku4pK1gj+Dxgx7/+Z0jAriZISPX1ocTO8aHh8x8e7Kb1rB4Ms0nA/SzjtNOVJ4exVavQBCw==}
    engines: {node: '>=14.21.3'}
    cpu: [arm64]
    os: [linux]

  '@biomejs/cli-linux-x64-musl@2.3.5':
    resolution: {integrity: sha512-awVuycTPpVTH/+WDVnEEYSf6nbCBHf/4wB3lquwT7puhNg8R4XvonWNZzUsfHZrCkjkLhFH/vCZK5jHatD9FEg==}
    engines: {node: '>=14.21.3'}
    cpu: [x64]
    os: [linux]

  '@biomejs/cli-linux-x64@2.3.5':
    resolution: {integrity: sha512-XrIVi9YAW6ye0CGQ+yax0gLfx+BFOtKaNX74n+xHWla6Cl6huUmcKNO7HPx7BiKnJUzrxXY1qYlm7xMvi08X4g==}
    engines: {node: '>=14.21.3'}
    cpu: [x64]
    os: [linux]

  '@biomejs/cli-win32-arm64@2.3.5':
    resolution: {integrity: sha512-DlBiMlBZZ9eIq4H7RimDSGsYcOtfOIfZOaI5CqsWiSlbTfqbPVfWtCf92wNzx8GNMbu1s7/g3ZZESr6+GwM/SA==}
    engines: {node: '>=14.21.3'}
    cpu: [arm64]
    os: [win32]

  '@biomejs/cli-win32-x64@2.3.5':
    resolution: {integrity: sha512-nUmR8gb6yvrKhtRgzwo/gDimPwnO5a4sCydf8ZS2kHIJhEmSmk+STsusr1LHTuM//wXppBawvSQi2xFXJCdgKQ==}
    engines: {node: '>=14.21.3'}
    cpu: [x64]
    os: [win32]

  '@emnapi/core@1.7.0':
    resolution: {integrity: sha512-pJdKGq/1iquWYtv1RRSljZklxHCOCAJFJrImO5ZLKPJVJlVUcs8yFwNQlqS0Lo8xT1VAXXTCZocF9n26FWEKsw==}

  '@emnapi/runtime@1.7.0':
    resolution: {integrity: sha512-oAYoQnCYaQZKVS53Fq23ceWMRxq5EhQsE0x0RdQ55jT7wagMu5k+fS39v1fiSLrtrLQlXwVINenqhLMtTrV/1Q==}

  '@emnapi/wasi-threads@1.1.0':
    resolution: {integrity: sha512-WI0DdZ8xFSbgMjR1sFsKABJ/C5OnRrjT06JXbZKexJGrDuPTzZdDYfFlsgcCXCyf+suG5QU2e/y1Wo2V/OapLQ==}

  '@esbuild/aix-ppc64@0.25.12':
    resolution: {integrity: sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.25.12':
    resolution: {integrity: sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.25.12':
    resolution: {integrity: sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.25.12':
    resolution: {integrity: sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.25.12':
    resolution: {integrity: sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.25.12':
    resolution: {integrity: sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.25.12':
    resolution: {integrity: sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.25.12':
    resolution: {integrity: sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.25.12':
    resolution: {integrity: sha512-8bwX7a8FghIgrupcxb4aUmYDLp8pX06rGh5HqDT7bB+8Rdells6mHvrFHHW2JAOPZUbnjUpKTLg6ECyzvas2AQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.25.12':
    resolution: {integrity: sha512-lPDGyC1JPDou8kGcywY0YILzWlhhnRjdof3UlcoqYmS9El818LLfJJc3PXXgZHrHCAKs/Z2SeZtDJr5MrkxtOw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.25.12':
    resolution: {integrity: sha512-0y9KrdVnbMM2/vG8KfU0byhUN+EFCny9+8g202gYqSSVMonbsCfLjUO+rCci7pM0WBEtz+oK/PIwHkzxkyharA==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.25.12':
    resolution: {integrity: sha512-h///Lr5a9rib/v1GGqXVGzjL4TMvVTv+s1DPoxQdz7l/AYv6LDSxdIwzxkrPW438oUXiDtwM10o9PmwS/6Z0Ng==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.25.12':
    resolution: {integrity: sha512-iyRrM1Pzy9GFMDLsXn1iHUm18nhKnNMWscjmp4+hpafcZjrr2WbT//d20xaGljXDBYHqRcl8HnxbX6uaA/eGVw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.25.12':
    resolution: {integrity: sha512-9meM/lRXxMi5PSUqEXRCtVjEZBGwB7P/D4yT8UG/mwIdze2aV4Vo6U5gD3+RsoHXKkHCfSxZKzmDssVlRj1QQA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.25.12':
    resolution: {integrity: sha512-Zr7KR4hgKUpWAwb1f3o5ygT04MzqVrGEGXGLnj15YQDJErYu/BGg+wmFlIDOdJp0PmB0lLvxFIOXZgFRrdjR0w==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.25.12':
    resolution: {integrity: sha512-MsKncOcgTNvdtiISc/jZs/Zf8d0cl/t3gYWX8J9ubBnVOwlk65UIEEvgBORTiljloIWnBzLs4qhzPkJcitIzIg==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.25.12':
    resolution: {integrity: sha512-uqZMTLr/zR/ed4jIGnwSLkaHmPjOjJvnm6TVVitAa08SLS9Z0VM8wIRx7gWbJB5/J54YuIMInDquWyYvQLZkgw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.25.12':
    resolution: {integrity: sha512-xXwcTq4GhRM7J9A8Gv5boanHhRa/Q9KLVmcyXHCTaM4wKfIpWkdXiMog/KsnxzJ0A1+nD+zoecuzqPmCRyBGjg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.25.12':
    resolution: {integrity: sha512-Ld5pTlzPy3YwGec4OuHh1aCVCRvOXdH8DgRjfDy/oumVovmuSzWfnSJg+VtakB9Cm0gxNO9BzWkj6mtO1FMXkQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.25.12':
    resolution: {integrity: sha512-fF96T6KsBo/pkQI950FARU9apGNTSlZGsv1jZBAlcLL1MLjLNIWPBkj5NlSz8aAzYKg+eNqknrUJ24QBybeR5A==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.25.12':
    resolution: {integrity: sha512-MZyXUkZHjQxUvzK7rN8DJ3SRmrVrke8ZyRusHlP+kuwqTcfWLyqMOE3sScPPyeIXN/mDJIfGXvcMqCgYKekoQw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openharmony-arm64@0.25.12':
    resolution: {integrity: sha512-rm0YWsqUSRrjncSXGA7Zv78Nbnw4XL6/dzr20cyrQf7ZmRcsovpcRBdhD43Nuk3y7XIoW2OxMVvwuRvk9XdASg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openharmony]

  '@esbuild/sunos-x64@0.25.12':
    resolution: {integrity: sha512-3wGSCDyuTHQUzt0nV7bocDy72r2lI33QL3gkDNGkod22EsYl04sMf0qLb8luNKTOmgF/eDEDP5BFNwoBKH441w==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/win32-arm64@0.25.12':
    resolution: {integrity: sha512-rMmLrur64A7+DKlnSuwqUdRKyd3UE7oPJZmnljqEptesKM8wx9J8gx5u0+9Pq0fQQW8vqeKebwNXdfOyP+8Bsg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-ia32@0.25.12':
    resolution: {integrity: sha512-HkqnmmBoCbCwxUKKNPBixiWDGCpQGVsrQfJoVGYLPT41XWF8lHuE5N6WhVia2n4o5QK5M4tYr21827fNhi4byQ==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-x64@0.25.12':
    resolution: {integrity: sha512-alJC0uCZpTFrSL0CCDjcgleBXPnCrEAhTBILpeAp7M/OFgoqtAetfBzX0xM00MUsVVPpVjlPuMbREqnZCXaTnA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [win32]

  '@istanbuljs/schema@0.1.3':
    resolution: {integrity: sha512-ZXRY4jNvVgSVQ8DL3LTcakaAtXwTVUxE81hslsyD2AtoXW/wVob10HkOJ1X/pAlcI7D+2YoZKg5do8G/w6RYgA==}
    engines: {node: '>=8'}

  '@jridgewell/gen-mapping@0.3.13':
    resolution: {integrity: sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==}

  '@jridgewell/remapping@2.3.5':
    resolution: {integrity: sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==}

  '@jridgewell/resolve-uri@3.1.2':
    resolution: {integrity: sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==}
    engines: {node: '>=6.0.0'}

  '@jridgewell/source-map@0.3.11':
    resolution: {integrity: sha512-ZMp1V8ZFcPG5dIWnQLr3NSI1MiCU7UETdS/A0G8V/XWHvJv3ZsFqutJn1Y5RPmAPX6F3BiE397OqveU/9NCuIA==}

  '@jridgewell/sourcemap-codec@1.5.5':
    resolution: {integrity: sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==}

  '@jridgewell/trace-mapping@0.3.31':
    resolution: {integrity: sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==}

  '@napi-rs/wasm-runtime@1.0.7':
    resolution: {integrity: sha512-SeDnOO0Tk7Okiq6DbXmmBODgOAb9dp9gjlphokTUxmt8U3liIP1ZsozBahH69j/RJv+Rfs6IwUKHTgQYJ/HBAw==}

  '@oxc-project/runtime@0.97.0':
    resolution: {integrity: sha512-yH0zw7z+jEws4dZ4IUKoix5Lh3yhqIJWF9Dc8PWvhpo7U7O+lJrv7ZZL4BeRO0la8LBQFwcCewtLBnVV7hPe/w==}
    engines: {node: ^20.19.0 || >=22.12.0}

  '@oxc-project/types@0.97.0':
    resolution: {integrity: sha512-lxmZK4xFrdvU0yZiDwgVQTCvh2gHWBJCBk5ALsrtsBWhs0uDIi+FTOnXRQeQfs304imdvTdaakT/lqwQ8hkOXQ==}

  '@quansync/fs@0.1.5':
    resolution: {integrity: sha512-lNS9hL2aS2NZgNW7BBj+6EBl4rOf8l+tQ0eRY6JWCI8jI2kc53gSoqbjojU0OnAWhzoXiOjFyGsHcDGePB3lhA==}

  '@rolldown/binding-android-arm64@1.0.0-beta.50':
    resolution: {integrity: sha512-XlEkrOIHLyGT3avOgzfTFSjG+f+dZMw+/qd+Y3HLN86wlndrB/gSimrJCk4gOhr1XtRtEKfszpadI3Md4Z4/Ag==}
    engines: {node: ^20.19.0 || >=22.12.0}
    cpu: [arm64]
    os: [android]

  '@rolldown/binding-darwin-arm64@1.0.0-beta.50':
    resolution: {integrity: sha512-+JRqKJhoFlt5r9q+DecAGPLZ5PxeLva+wCMtAuoFMWPoZzgcYrr599KQ+Ix0jwll4B4HGP43avu9My8KtSOR+w==}
    engines: {node: ^20.19.0 || >=22.12.0}
    cpu: [arm64]
    os: [darwin]

  '@rolldown/binding-darwin-x64@1.0.0-beta.50':
    resolution: {integrity: sha512-fFXDjXnuX7/gQZQm/1FoivVtRcyAzdjSik7Eo+9iwPQ9EgtA5/nB2+jmbzaKtMGG3q+BnZbdKHCtOacmNrkIDA==}
    engines: {node: ^20.19.0 || >=22.12.0}
    cpu: [x64]
    os: [darwin]

  '@rolldown/binding-freebsd-x64@1.0.0-beta.50':
    resolution: {integrity: sha512-F1b6vARy49tjmT/hbloplzgJS7GIvwWZqt+tAHEstCh0JIh9sa8FAMV
... [TRUNCATED]
```

### File: release-please-config.json
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

### File: tsconfig.json
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

### File: tsdown.config.ts
```ts
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

### File: vitest.config.ts
```ts
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

### File: .github\CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
  advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at alexjovermorales@gmail.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

```

### File: .github\CONTRIBUTING.md
```md
We're really glad you're reading this, because we need volunteer developers to help this project come to fruition. 👏

## Instructions

These steps will guide you through contributing to this project:

- Fork the repo
- Clone it and install dependencies

```
git clone https://github.com/bgub/eta
npm install
```

Keep in mind that after running `npm install` the git repo is reset. So a good way to cope with this is to have a copy of the folder to push the changes, and the other to try them.

Make and commit your changes. Make sure the commands npm run build and npm run test:prod are working.

Finally send a [GitHub Pull Request](https://github.com/bgub/eta/compare?expand=1) with a clear list of what you've done (read more [about pull requests](https://help.github.com/articles/about-pull-requests/)). Make sure all of your commits are atomic (one feature per commit).

```

### File: src\compile-string.ts
```ts
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

### File: src\compile.ts
```ts
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

### File: src\config.ts
```ts
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

### File: src\core.ts
```ts
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

### File: src\err.ts
```ts
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

### File: src\file-handling.ts
```ts
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

### File: src\index.ts
```ts
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

### File: src\internal.ts
```ts
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
