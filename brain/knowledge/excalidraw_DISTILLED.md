---
id: excalidraw
type: knowledge
owner: OA_Triage
---
# excalidraw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "private": true,
  "name": "excalidraw-monorepo",
  "packageManager": "yarn@1.22.22",
  "workspaces": [
    "excalidraw-app",
    "packages/*",
    "examples/*"
  ],
  "devDependencies": {
    "@babel/preset-env": "7.26.9",
    "@excalidraw/eslint-config": "1.0.3",
    "@excalidraw/prettier-config": "1.0.2",
    "@types/chai": "4.3.0",
    "@types/jest": "27.4.0",
    "@types/lodash.throttle": "4.1.7",
    "@types/react": "19.0.10",
    "@types/react-dom": "19.0.4",
    "@types/socket.io-client": "3.0.0",
    "@vitejs/plugin-react": "3.1.0",
    "@vitest/coverage-v8": "3.0.7",
    "@vitest/ui": "2.0.5",
    "chai": "4.3.6",
    "dotenv": "16.0.1",
    "eslint-config-prettier": "8.5.0",
    "eslint-config-react-app": "7.0.1",
    "eslint-plugin-import": "2.31.0",
    "eslint-plugin-prettier": "3.3.1",
    "http-server": "14.1.1",
    "husky": "7.0.4",
    "jsdom": "22.1.0",
    "lint-staged": "12.3.7",
    "pepjs": "0.5.3",
    "prettier": "2.6.2",
    "rewire": "6.0.0",
    "rimraf": "^5.0.0",
    "typescript": "5.9.3",
    "vite": "5.0.12",
    "vite-plugin-checker": "0.7.2",
    "vite-plugin-ejs": "1.7.0",
    "vite-plugin-pwa": "0.21.1",
    "vite-plugin-svgr": "4.2.0",
    "vitest": "3.0.6",
    "vitest-canvas-mock": "0.3.3"
  },
  "engines": {
    "node": ">=18.0.0"
  },
  "homepage": ".",
  "prettier": "@excalidraw/prettier-config",
  "scripts": {
    "build-node": "node ./scripts/build-node.js",
    "build:app:docker": "yarn --cwd ./excalidraw-app build:app:docker",
    "build:app": "yarn --cwd ./excalidraw-app build:app",
    "build:common": "yarn --cwd ./packages/common build:esm",
    "build:element": "yarn --cwd ./packages/element build:esm",
    "build:excalidraw": "yarn --cwd ./packages/excalidraw build:esm",
    "build:math": "yarn --cwd ./packages/math build:esm",
    "build:packages": "yarn build:common && yarn build:math && yarn build:element && yarn build:excalidraw",
    "build:version": "yarn --cwd ./excalidraw-app build:version",
    "build": "yarn --cwd ./excalidraw-app build",
    "build:preview": "yarn --cwd ./excalidraw-app build:preview",
    "start": "yarn --cwd ./excalidraw-app start",
    "start:production": "yarn --cwd ./excalidraw-app start:production",
    "start:example": "yarn build:packages && yarn --cwd ./examples/with-script-in-browser start",
    "test:all": "yarn test:typecheck && yarn test:code && yarn test:other && yarn test:app --watch=false",
    "test:app": "vitest",
    "test:code": "eslint --max-warnings=0 --ext .js,.ts,.tsx .",
    "test:other": "yarn prettier --list-different",
    "test:typecheck": "tsc",
    "test:update": "yarn test:app --update --watch=false",
    "test": "yarn test:app",
    "test:coverage": "vitest --coverage",
    "test:coverage:watch": "vitest --coverage --watch",
    "test:ui": "yarn test --ui --coverage.enabled=true",
    "fix:code": "yarn test:code --fix",
    "fix:other": "yarn prettier --write",
    "fix": "yarn fix:other && yarn fix:code",
    "locales-coverage": "node scripts/build-locales-coverage.js",
    "locales-coverage:description": "node scripts/locales-coverage-description.js",
    "prepare": "husky install",
    "prettier": "prettier \"**/*.{css,scss,json,md,html,yml}\" --ignore-path=.eslintignore",
    "release": "node scripts/release.js",
    "release:test": "node scripts/release.js --tag=test",
    "release:next": "node scripts/release.js --tag=next",
    "release:latest": "node scripts/release.js --tag=latest",
    "rm:build": "rimraf --glob excalidraw-app/build excalidraw-app/dist excalidraw-app/dev-dist packages/*/dist packages/*/build examples/*/build examples/*/dist",
    "rm:node_modules": "rimraf --glob node_modules excalidraw-app/node_modules packages/*/node_modules",
    "clean-install": "yarn rm:node_modules && yarn install"
  },
  "resolutions": {
    "strip-ansi": "6.0.1"
  }
}

```

### File: README.md
```md
<a href="https://excalidraw.com/" target="_blank" rel="noopener">
  <picture>
    <source media="(prefers-color-scheme: dark)" alt="Excalidraw" srcset="https://excalidraw.nyc3.cdn.digitaloceanspaces.com/github/excalidraw_github_cover_2_dark.png" />
    <img alt="Excalidraw" src="https://excalidraw.nyc3.cdn.digitaloceanspaces.com/github/excalidraw_github_cover_2.png" />
  </picture>
</a>

<h4 align="center">
  <a href="https://excalidraw.com">Excalidraw Editor</a> |
  <a href="https://plus.excalidraw.com/blog">Blog</a> |
  <a href="https://docs.excalidraw.com">Documentation</a> |
  <a href="https://plus.excalidraw.com">Excalidraw+</a>
</h4>

<div align="center">
  <h2>
    An open source virtual hand-drawn style whiteboard. </br>
    Collaborative and end-to-end encrypted. </br>
  <br />
  </h2>
</div>

<br />
<p align="center">
  <a href="https://github.com/excalidraw/excalidraw/blob/master/LICENSE">
    <img alt="Excalidraw is released under the MIT license." src="https://img.shields.io/badge/license-MIT-blue.svg"  /></a>
  <a href="https://www.npmjs.com/package/@excalidraw/excalidraw">
    <img alt="npm downloads/month" src="https://img.shields.io/npm/dm/@excalidraw/excalidraw"  /></a>
  <a href="https://docs.excalidraw.com/docs/introduction/contributing">
    <img alt="PRs welcome!" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat"  /></a>
  <a href="https://discord.gg/UexuTaE">
    <img alt="Chat on Discord" src="https://img.shields.io/discord/723672430744174682?color=738ad6&label=Chat%20on%20Discord&logo=discord&logoColor=ffffff&widget=false"/></a>
  <a href="https://deepwiki.com/excalidraw/excalidraw">
    <img alt="Ask DeepWiki" src="https://deepwiki.com/badge.svg" /></a>
  <a href="https://twitter.com/excalidraw">
    <img alt="Follow Excalidraw on Twitter" src="https://img.shields.io/twitter/follow/excalidraw.svg?label=follow+@excalidraw&style=social&logo=twitter"/></a>
</p>

<div align="center">
  <figure>
    <a href="https://excalidraw.com" target="_blank" rel="noopener">
      <img src="https://excalidraw.nyc3.cdn.digitaloceanspaces.com/github%2Fproduct_showcase.png" alt="Product showcase" />
    </a>
    <figcaption>
      <p align="center">
        Create beautiful hand-drawn like diagrams, wireframes, or whatever you like.
      </p>
    </figcaption>
  </figure>
</div>

## Features

The Excalidraw editor (npm package) supports:

- 💯&nbsp;Free & open-source.
- 🎨&nbsp;Infinite, canvas-based whiteboard.
- ✍️&nbsp;Hand-drawn like style.
- 🌓&nbsp;Dark mode.
- 🏗️&nbsp;Customizable.
- 📷&nbsp;Image support.
- 😀&nbsp;Shape libraries support.
- 🌐&nbsp;Localization (i18n) support.
- 🖼️&nbsp;Export to PNG, SVG & clipboard.
- 💾&nbsp;Open format - export drawings as an `.excalidraw` json file.
- ⚒️&nbsp;Wide range of tools - rectangle, circle, diamond, arrow, line, free-draw, eraser...
- ➡️&nbsp;Arrow-binding & labeled arrows.
- 🔙&nbsp;Undo / Redo.
- 🔍&nbsp;Zoom and panning support.

## Excalidraw.com

The app hosted at [excalidraw.com](https://excalidraw.com) is a minimal showcase of what you can build with Excalidraw. Its [source code](https://github.com/excalidraw/excalidraw/tree/master/excalidraw-app) is part of this repository as well, and the app features:

- 📡&nbsp;PWA support (works offline).
- 🤼&nbsp;Real-time collaboration.
- 🔒&nbsp;End-to-end encryption.
- 💾&nbsp;Local-first support (autosaves to the browser).
- 🔗&nbsp;Shareable links (export to a readonly link you can share with others).

We'll be adding these features as drop-in plugins for the npm package in the future.

## Quick start

**Note:** following instructions are for installing the Excalidraw [npm package](https://www.npmjs.com/package/@excalidraw/excalidraw) when integrating Excalidraw into your own app. To run the repository locally for development, please refer to our [Development Guide](https://docs.excalidraw.com/docs/introduction/development).

Use `npm` or `yarn` to install the package.

```bash
npm install react react-dom @excalidraw/excalidraw
# or
yarn add react react-dom @excalidraw/excalidraw
```

Check out our [documentation](https://docs.excalidraw.com/docs/@excalidraw/excalidraw/installation) for more details!

## Contributing

- Missing something or found a bug? [Report here](https://github.com/excalidraw/excalidraw/issues).
- Want to contribute? Check out our [contribution guide](https://docs.excalidraw.com/docs/introduction/contributing) or let us know on [Discord](https://discord.gg/UexuTaE).
- Want to help with translations? See the [translation guide](https://docs.excalidraw.com/docs/introduction/contributing#translating).

## Integrations

- [VScode extension](https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor)
- [npm package](https://www.npmjs.com/package/@excalidraw/excalidraw)

## Who's integrating Excalidraw

[Google Cloud](https://googlecloudcheatsheet.withgoogle.com/architecture) • [Meta](https://meta.com/) • [CodeSandbox](https://codesandbox.io/) • [Obsidian Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) • [Replit](https://replit.com/) • [Slite](https://slite.com/) • [Notion](https://notion.so/) • [HackerRank](https://www.hackerrank.com/) • and many others

## Sponsors & support

If you like the project, you can become a sponsor at [Open Collective](https://opencollective.com/excalidraw) or use [Excalidraw+](https://plus.excalidraw.com/).

## Thank you for supporting Excalidraw

[<img src="https://opencollective.com/excalidraw/tiers/sponsors/0/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/0/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/1/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/1/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/2/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/2/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/3/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/3/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/4/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/4/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/5/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/5/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/6/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/6/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/7/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/7/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/8/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/8/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/9/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/9/website) [<img src="https://opencollective.com/excalidraw/tiers/sponsors/10/avatar.svg?avatarHeight=120"/>](https://opencollective.com/excalidraw/tiers/sponsors/10/website)

<a href="https://opencollective.com/excalidraw#category-CONTRIBUTE" target="_blank"><img src="https://opencollective.com/excalidraw/tiers/backers.svg?avatarHeight=32"/></a>

Last but not least, we're thankful to these companies for offering their services for free:

[![Vercel](./.github/assets/vercel.svg)](https://vercel.com) [![Sentry](./.github/assets/sentry.svg)](https://sentry.io) [![Crowdin](./.github/assets/crowdin.svg)](https://crowdin.com)

```

### File: packages\common\package.json
```json
{
  "name": "@excalidraw/common",
  "version": "0.18.0",
  "type": "module",
  "types": "./dist/types/common/src/index.d.ts",
  "main": "./dist/prod/index.js",
  "module": "./dist/prod/index.js",
  "exports": {
    ".": {
      "types": "./dist/types/common/src/index.d.ts",
      "development": "./dist/dev/index.js",
      "production": "./dist/prod/index.js",
      "default": "./dist/prod/index.js"
    },
    "./*": {
      "types": "./dist/types/common/src/*.d.ts",
      "development": "./dist/dev/index.js",
      "production": "./dist/prod/index.js",
      "default": "./dist/prod/index.js"
    }
  },
  "files": [
    "dist/*"
  ],
  "description": "Excalidraw common functions, constants, etc.",
  "publishConfig": {
    "access": "public"
  },
  "license": "MIT",
  "keywords": [
    "excalidraw",
    "excalidraw-utils"
  ],
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not ie <= 11",
      "not op_mini all",
      "not safari < 12",
      "not kaios <= 2.5",
      "not edge < 79",
      "not chrome < 70",
      "not and_uc < 13",
      "not samsung < 10"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "bugs": "https://github.com/excalidraw/excalidraw/issues",
  "repository": "https://github.com/excalidraw/excalidraw",
  "scripts": {
    "gen:types": "rimraf types && tsc",
    "build:esm": "rimraf dist && node ../../scripts/buildBase.js && yarn gen:types"
  },
  "dependencies": {
    "tinycolor2": "1.6.0"
  },
  "devDependencies": {
    "@types/tinycolor2": "1.4.6"
  }
}

```

### File: packages\common\README.md
```md
# @excalidraw/common

## Install

```bash
npm install @excalidraw/common
```

If you prefer Yarn over npm, use this command to install the Excalidraw utils package:

```bash
yarn add @excalidraw/common
```

With PNPM, similarly install the package with this command:

```bash
pnpm add @excalidraw/common
```

```

### File: packages\utils\package.json
```json
{
  "name": "@excalidraw/utils",
  "version": "0.1.2",
  "type": "module",
  "types": "./dist/types/utils/src/index.d.ts",
  "main": "./dist/prod/index.js",
  "module": "./dist/prod/index.js",
  "exports": {
    ".": {
      "types": "./dist/types/utils/src/index.d.ts",
      "development": "./dist/dev/index.js",
      "production": "./dist/prod/index.js",
      "default": "./dist/prod/index.js"
    },
    "./*": {
      "types": "./dist/types/utils/src/*.d.ts"
    }
  },
  "files": [
    "dist/*"
  ],
  "description": "Excalidraw utility functions",
  "publishConfig": {
    "access": "public"
  },
  "license": "MIT",
  "keywords": [
    "excalidraw",
    "excalidraw-utils"
  ],
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not ie <= 11",
      "not op_mini all",
      "not safari < 12",
      "not kaios <= 2.5",
      "not edge < 79",
      "not chrome < 70",
      "not and_uc < 13",
      "not samsung < 10"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "dependencies": {
    "@braintree/sanitize-url": "6.0.2",
    "@excalidraw/laser-pointer": "1.3.1",
    "browser-fs-access": "0.38.0",
    "pako": "2.0.3",
    "perfect-freehand": "1.2.0",
    "png-chunk-text": "1.0.0",
    "png-chunks-encode": "1.0.0",
    "png-chunks-extract": "1.0.0",
    "roughjs": "4.6.4"
  },
  "devDependencies": {
    "cross-env": "7.0.3",
    "fonteditor-core": "2.4.0",
    "typescript": "5.9.3",
    "wawoff2": "2.0.1",
    "which": "4.0.0"
  },
  "bugs": "https://github.com/excalidraw/excalidraw/issues",
  "repository": "https://github.com/excalidraw/excalidraw",
  "scripts": {
    "gen:types": "rimraf types && tsc",
    "build:esm": "rimraf dist && node ../../scripts/buildUtils.js && yarn gen:types"
  }
}

```

### File: packages\utils\README.md
```md
# @excalidraw/utils

## Install

```bash
npm install @excalidraw/utils
```

If you prefer Yarn over npm, use this command to install the Excalidraw utils package:

```bash
yarn add @excalidraw/utils
```

## API

### `serializeAsJSON`

See [`serializeAsJSON`](https://github.com/excalidraw/excalidraw/blob/master/src/packages/excalidraw/README.md#serializeAsJSON) for API and description.

### `exportToBlob` (async)

Export an Excalidraw diagram to a [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob).

### `exportToSvg`

Export an Excalidraw diagram to a [SVGElement](https://developer.mozilla.org/en-US/docs/Web/API/SVGElement).

## Usage

Excalidraw utils is published as a UMD (Universal Module Definition). If you are using a module bundler (for instance, Webpack), you can import it as an ES6 module:

```js
import { exportToSvg, exportToBlob } from "@excalidraw/utils";
```

To use it in a browser directly:

```html
<script src="https://unpkg.com/@excalidraw/utils@0.1.0/dist/excalidraw-utils.min.js"></script>
<script>
  // ExcalidrawUtils is a global variable defined by excalidraw.min.js
  const { exportToSvg, exportToBlob } = ExcalidrawUtils;
</script>
```

Here's the `exportToBlob` and `exportToSvg` functions in action:

```js
const excalidrawDiagram = {
  type: "excalidraw",
  version: 2,
  source: "https://excalidraw.com",
  elements: [
    {
      id: "vWrqOAfkind2qcm7LDAGZ",
      type: "ellipse",
      x: 414,
      y: 237,
      width: 214,
      height: 214,
      angle: 0,
      strokeColor: "#000000",
      backgroundColor: "#15aabf",
      fillStyle: "hachure",
      strokeWidth: 1,
      strokeStyle: "solid",
      roughness: 1,
      opacity: 100,
      groupIds: [],
      roundness: null,
      seed: 1041657908,
      version: 120,
      versionNonce: 1188004276,
      isDeleted: false,
      boundElementIds: null,
    },
  ],
  appState: {
    viewBackgroundColor: "#ffffff",
    gridSize: null,
  },
};

// Export the Excalidraw diagram as SVG string
const svg = exportToSvg(excalidrawDiagram);
console.log(svg.outerHTML);

// Export the Excalidraw diagram as PNG Blob URL
(async () => {
  const blob = await exportToBlob({
    ...excalidrawDiagram,
    mimeType: "image/png",
  });

  const urlCreator = window.URL || window.webkitURL;
  console.log(urlCreator.createObjectURL(blob));
})();
```

```

### File: .eslintrc.json
```json
{
  "extends": ["@excalidraw/eslint-config", "react-app"],
  "rules": {
    "import/order": [
      "warn",
      {
        "groups": ["builtin", "external", "internal", "parent", "sibling", "index", "object", "type"],
        "pathGroups": [
          {
            "pattern": "@excalidraw/**",
            "group": "external",
            "position": "after"
          }
        ],
        "newlines-between": "always-and-inside-groups",
        "warnOnUnassignedImports": true
      }
    ],
    "import/no-anonymous-default-export": "off",
    "no-restricted-globals": "off",
    "@typescript-eslint/consistent-type-imports": [
      "error",
      {
        "prefer": "type-imports",
        "disallowTypeAnnotations": false,
        "fixStyle": "separate-type-imports"
      }
    ],
    "no-restricted-imports": [
      "error",
      {
        "name": "jotai",
        "message": "Do not import from \"jotai\" directly. Use our app-specific modules (\"editor-jotai\" or \"app-jotai\")."
      }
    ],
    "react/jsx-no-target-blank": [
      "error",
      {
        "allowReferrer": true
      }
    ]
  },
  "overrides": [
    {
      "files": ["packages/excalidraw/**/*.{ts,tsx}"],
      "excludedFiles": ["packages/excalidraw/**/*.test.{ts,tsx}", "packages/excalidraw/**/*.test.*.{ts,tsx}"],
      "rules": {
        "@typescript-eslint/no-restricted-imports": [
          "error",
          {
            "patterns": [
              {
                "group": ["@excalidraw/excalidraw"],
                "message": "Do not import from the barrel 'index.tsx' files. Use direct relative imports to the specific module instead.",
                "allowTypeImports": true
              }
            ],
            "paths": [".", "..", "../..", "../../..", "../../../..", "../../../../..", "../index", "../../index", "../../../index", "../../../../index"]
          }
        ]
      }
    }
  ]
}

```

### File: .lintstagedrc.js
```js
const { CLIEngine } = require("eslint");

// see https://github.com/okonet/lint-staged#how-can-i-ignore-files-from-eslintignore-
// for explanation
const cli = new CLIEngine({});

module.exports = {
  "*.{js,ts,tsx}": files => {
    return (
      "eslint --max-warnings=0 --fix " + files.filter(file => !cli.isPathIgnored(file)).join(" ")
    );
  },
  "*.{css,scss,json,md,html,yml}": ["prettier --write"],
};

```

### File: CLAUDE.md
```md
# CLAUDE.md

## Project Structure

Excalidraw is a **monorepo** with a clear separation between the core library and the application:

- **`packages/excalidraw/`** - Main React component library published to npm as `@excalidraw/excalidraw`
- **`excalidraw-app/`** - Full-featured web application (excalidraw.com) that uses the library
- **`packages/`** - Core packages: `@excalidraw/common`, `@excalidraw/element`, `@excalidraw/math`, `@excalidraw/utils`
- **`examples/`** - Integration examples (NextJS, browser script)

## Development Workflow

1. **Package Development**: Work in `packages/*` for editor features
2. **App Development**: Work in `excalidraw-app/` for app-specific features
3. **Testing**: Always run `yarn test:update` before committing
4. **Type Safety**: Use `yarn test:typecheck` to verify TypeScript

## Development Commands

```bash
yarn test:typecheck  # TypeScript type checking
yarn test:update     # Run all tests (with snapshot updates)
yarn fix             # Auto-fix formatting and linting issues
```

## Architecture Notes

### Package System

- Uses Yarn workspaces for monorepo management
- Internal packages use path aliases (see `vitest.config.mts`)
- Build system uses esbuild for packages, Vite for the app
- TypeScript throughout with strict configuration

```

### File: CONTRIBUTING.md
```md
# Contributing

Head over to the [docs](https://docs.excalidraw.com/docs/introduction/contributing)

```

### File: setupTests.ts
```ts
import fs from "fs";

// vitest.setup.ts
import "vitest-canvas-mock";
import "@testing-library/jest-dom";
import { vi } from "vitest";

import polyfill from "./packages/excalidraw/polyfill";
import { mockThrottleRAF } from "./packages/excalidraw/tests/helpers/mocks";
import { yellow } from "./packages/excalidraw/tests/helpers/colorize";
import { testPolyfills } from "./packages/excalidraw/tests/helpers/polyfills";

vi.mock("@excalidraw/common", async (importOriginal) => {
  const module = await importOriginal<typeof import("@excalidraw/common")>();

  return {
    ...module,
    throttleRAF: mockThrottleRAF,
  };
});

// mock for pep.js not working with setPointerCapture()
HTMLElement.prototype.setPointerCapture = vi.fn();

Object.assign(globalThis, testPolyfills);

require("fake-indexeddb/auto");

polyfill();

Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: vi.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(), // deprecated
    removeListener: vi.fn(), // deprecated
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});

Object.defineProperty(window, "FontFace", {
  enumerable: true,
  value: class {
    private family: string;
    private source: string;
    private descriptors: any;
    private status: string;
    private unicodeRange: string;

    constructor(family, source, descriptors) {
      this.family = family;
      this.source = source;
      this.descriptors = descriptors;
      this.status = "unloaded";
      this.unicodeRange = "U+0000-00FF";
    }

    load() {
      this.status = "loaded";
    }
  },
});

Object.defineProperty(document, "fonts", {
  value: {
    load: vi.fn().mockResolvedValue([]),
    check: vi.fn().mockResolvedValue(true),
    has: vi.fn().mockResolvedValue(true),
    add: vi.fn(),
  },
});

Object.defineProperty(window, "EXCALIDRAW_ASSET_PATH", {
  value: `file://${__dirname}/`,
});

// mock the font fetch only, so that everything else, as font subsetting, can run inside of the (snapshot) tests
vi.mock(
  "./packages/excalidraw/fonts/ExcalidrawFontFace",
  async (importOriginal) => {
    const mod = await importOriginal<
      typeof import("./packages/excalidraw/fonts/ExcalidrawFontFace")
    >();
    const ExcalidrawFontFaceImpl = mod.ExcalidrawFontFace;

    return {
      ...mod,
      ExcalidrawFontFace: class extends ExcalidrawFontFaceImpl {
        public async fetchFont(url: URL): Promise<ArrayBuffer> {
          if (!url.toString().startsWith("file://")) {
            return super.fetchFont(url);
          }

          // read local assets directly, without running a server
          const content = await fs.promises.readFile(url);
          return content.buffer;
        }
      },
    };
  },
);

// ReactDOM is located inside index.tsx file
// as a result, we need a place for it to render into
const element = document.createElement("div");
element.id = "root";
document.body.appendChild(element);

const _consoleError = console.error.bind(console);
console.error = (...args) => {
  // the react's act() warning usually doesn't contain any useful stack trace
  // so we're catching the log and re-logging the message with the test name,
  // also stripping the actual component stack trace as it's not useful
  if (args[0]?.includes?.("act(")) {
    _consoleError(
      yellow(
        `<<< WARNING: test "${
          expect.getState().currentTestName
        }" does not wrap some state update in act() >>>`,
      ),
    );
  } else {
    _consoleError(...args);
  }
};

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "rootDir": "./",
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "types": ["vitest/globals", "@testing-library/jest-dom"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "ESNext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "baseUrl": ".",
    "paths": {
      "@excalidraw/common": ["./packages/common/src/index.ts"],
      "@excalidraw/common/*": ["./packages/common/src/*"],
      "@excalidraw/excalidraw": ["./packages/excalidraw/index.tsx"],
      "@excalidraw/excalidraw/*": ["./packages/excalidraw/*"],
      "@excalidraw/element": ["./packages/element/src/index.ts"],
      "@excalidraw/element/*": ["./packages/element/src/*"],
      "@excalidraw/math": ["./packages/math/src/index.ts"],
      "@excalidraw/math/*": ["./packages/math/src/*"],
      "@excalidraw/utils": ["./packages/utils/src/index.ts"],
      "@excalidraw/utils/*": ["./packages/utils/src/*"]
    }
  },
  "include": ["packages", "excalidraw-app"],
  "exclude": ["examples", "dist", "types", "tests"]
}

```

### File: vercel.json
```json
{
  "public": true,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "https://excalidraw.com"
        },
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "Feature-Policy",
          "value": "*"
        },
        {
          "key": "Referrer-Policy",
          "value": "origin"
        }
      ]
    },
    {
      "source": "/:file*.woff2",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000"
        },
        {
          "key": "Access-Control-Allow-Origin",
          "value": "https://excalidraw.com"
        }
      ]
    },
    {
      "source": "/(Virgil|Cascadia|Assistant-Regular).woff2",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000"
        },
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        }
      ]
    }
  ],
  "redirects": [
    {
      "source": "/webex/:match*",
      "destination": "https://for-webex.excalidraw.com"
    },
    {
      "source": "/:path*",
      "has": [
        {
          "type": "host",
          "value": "vscode.excalidraw.com"
        }
      ],
      "destination": "https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor"
    }
  ],
  "outputDirectory": "excalidraw-app/build",
  "installCommand": "yarn install"
}

```

### File: .codesandbox\tasks.json
```json
{
  // These tasks will run in order when initializing your CodeSandbox project.
  "setupTasks": [
    {
      "name": "Install Dependencies",
      "command": "yarn install"
    }
  ],

  // These tasks can be run from CodeSandbox. Running one will open a log in the app.
  "tasks": {
    "build": {
      "name": "Build",
      "command": "yarn build",
      "runAtStart": false
    },
    "fix": {
      "name": "Fix",
      "command": "yarn fix",
      "runAtStart": false
    },
    "prettier": {
      "name": "Prettify",
      "command": "yarn prettier",
      "runAtStart": false
    },
    "start": {
      "name": "Start Excalidraw",
      "command": "yarn start",
      "runAtStart": true,
      "preview": {
        "port": 3000
      }
    },
    "test": {
      "name": "Run Tests",
      "command": "yarn test",
      "runAtStart": false
    },
    "install-deps": {
      "name": "Install Dependencies",
      "command": "yarn install",
      "restartOn": {
        "files": ["yarn.lock"],
        "branch": false,
        "resume": false
      }
    }
  }
}

```

### File: .github\copilot-instructions.md
```md
# Project coding standards

## Generic Communication Guidelines

- Be succint and be aware that expansive generative AI answers are costly and slow
- Avoid providing explanations, trying to teach unless asked for, your chat partner is an expert
- Stop apologising if corrected, just provide the correct information or code
- Prefer code unless asked for explanation
- Stop summarizing what you've changed after modifications unless asked for

## TypeScript Guidelines

- Use TypeScript for all new code
- Where possible, prefer implementations without allocation
- When there is an option, opt for more performant solutions and trade RAM usage for less CPU cycles
- Prefer immutable data (const, readonly)
- Use optional chaining (?.) and nullish coalescing (??) operators

## React Guidelines

- Use functional components with hooks
- Follow the React hooks rules (no conditional hooks)
- Keep components small and focused
- Use CSS modules for component styling

## Naming Conventions

- Use PascalCase for component names, interfaces, and type aliases
- Use camelCase for variables, functions, and methods
- Use ALL_CAPS for constants

## Error Handling

- Use try/catch blocks for async operations
- Implement proper error boundaries in React components
- Always log errors with contextual information

## Testing

- Always attempt to fix #problems
- Always offer to run `yarn test:app` in the project root after modifications are complete and attempt fixing the issues reported

## Types

- Always include `packages/math/src/types.ts` in the context when your write math related code and always use the Point type instead of { x, y}

```

### File: packages\eslintrc.base.json
```json
{
  "overrides": [
    {
      "files": ["src/**/*.{ts,tsx}"],
      "rules": {
        "@typescript-eslint/no-restricted-imports": [
          "error",
          {
            "patterns": [
              {
                "group": ["../../excalidraw", "../../../packages/excalidraw", "@excalidraw/excalidraw"],
                "message": "Do not import from '@excalidraw/excalidraw' package anything but types, as this package must be independent.",
                "allowTypeImports": true
              }
            ]
          }
        ]
      }
    }
  ]
}

```

### File: packages\tsconfig.base.json
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "strict": true,
    "skipLibCheck": true,
    "declaration": true,
    "allowSyntheticDefaultImports": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "jsx": "react-jsx",
    "emitDeclarationOnly": true,
    "paths": {
      "@excalidraw/common": ["./common/src/index.ts"],
      "@excalidraw/common/*": ["./common/src/*"],
      "@excalidraw/element": ["./element/src/index.ts"],
      "@excalidraw/element/*": ["./element/src/*"],
      "@excalidraw/excalidraw": ["./excalidraw/index.tsx"],
      "@excalidraw/excalidraw/*": ["./excalidraw/*"],
      "@excalidraw/math": ["./math/src/index.ts"],
      "@excalidraw/math/*": ["./math/src/*"],
      "@excalidraw/utils": ["./utils/src/index.ts"],
      "@excalidraw/utils/*": ["./utils/src/*"]
    }
  }
}

```

### File: public\robots.txt
```txt
User-agent: Twitterbot
Disallow:

User-agent: facebookexternalhit
Disallow:

User-agent: *
Allow: /$
Allow: /
Allow: /sitemap.xml
Disallow: /

Sitemap: https://excalidraw.com/sitemap.xml

```

### File: public\service-worker.js
```js
// Since we migrated to Vite, the service worker strategy changed, in CRA it was a custom service worker named service-worker.js and in Vite its sw.js handled by vite-plugin-pwa
// Due to this the existing CRA users were not able to migrate to Vite or any new changes post Vite unless browser is hard refreshed
// Hence adding a self destroying worker so all CRA service workers are destroyed and migrated to Vite
// We should remove this code after sometime when we are confident that
// all users have migrated to Vite

self.addEventListener("install", () => {
  self.skipWaiting();
});

self.addEventListener("activate", () => {
  self.registration
    .unregister()
    .then(() => {
      return self.clients.matchAll();
    })
    .then((clients) => {
      clients.forEach((client) => client.navigate(client.url));
    });
});

```

### File: scripts\build-locales-coverage.js
```js
const { readdirSync, writeFileSync } = require("fs");
const files = readdirSync(`${__dirname}/../packages/excalidraw/locales`);

const flatten = (object = {}, result = {}, extraKey = "") => {
  for (const key in object) {
    if (typeof object[key] !== "object") {
      result[extraKey + key] = object[key];
    } else {
      flatten(object[key], result, `${extraKey}${key}.`);
    }
  }
  return result;
};

const locales = files.filter(
  (file) => file !== "README.md" && file !== "percentages.json",
);

const percentages = {};

for (let index = 0; index < locales.length; index++) {
  const currentLocale = locales[index];
  const data = flatten(
    require(`${__dirname}/../packages/excalidraw/locales/${currentLocale}`),
  );

  const allKeys = Object.keys(data);
  const translatedKeys = allKeys.filter((item) => data[item] !== "");
  const percentage = Math.floor((100 * translatedKeys.length) / allKeys.length);
  percentages[currentLocale.replace(".json", "")] = percentage;
}

writeFileSync(
  `${__dirname}/../packages/excalidraw/locales/percentages.json`,
  `${JSON.stringify(percentages, null, 2)}\n`,
  "utf8",
);

```

### File: scripts\build-node.js
```js
#!/usr/bin/env node

// In order to use this, you need to install Cairo on your machine. See
// instructions here: https://github.com/Automattic/node-canvas#compiling

// In order to run:
//   npm install canvas # please do not check it in
//   yarn build-node
//   node build/static/js/build-node.js
//   open test.png

const rewire = require("rewire");
const defaults = rewire("react-scripts/scripts/build.js");
const config = defaults.__get__("config");

// Disable multiple chunks
config.optimization.runtimeChunk = false;
config.optimization.splitChunks = {
  cacheGroups: {
    default: false,
  },
};
// Set the filename to be deterministic
config.output.filename = "static/js/build-node.js";
// Don't choke on node-specific requires
config.target = "node";
// Set the node entrypoint
config.entry = "../packages/excalidraw/index-node";
// By default, webpack is going to replace the require of the canvas.node file
// to just a string with the path of the canvas.node file. We need to tell
// webpack to avoid rewriting that dependency.
config.externals = (context, request, callback) => {
  if (/\.node$/.test(request)) {
    return callback(
      null,
      "commonjs ../../../node_modules/canvas/build/Release/canvas.node",
    );
  }
  callback();
};

```

### File: scripts\build-version.js
```js
#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const versionFile = path.join("build", "version.json");
const indexFile = path.join("build", "index.html");

const versionDate = (date) => date.toISOString().replace(".000", "");

const commitHash = () => {
  try {
    return require("child_process")
      .execSync("git rev-parse --short HEAD")
      .toString()
      .trim();
  } catch {
    return "none";
  }
};

const commitDate = (hash) => {
  try {
    const unix = require("child_process")
      .execSync(`git show -s --format=%ct ${hash}`)
      .toString()
      .trim();
    const date = new Date(parseInt(unix) * 1000);
    return versionDate(date);
  } catch {
    return versionDate(new Date());
  }
};

const getFullVersion = () => {
  const hash = commitHash();
  return `${commitDate(hash)}-${hash}`;
};

const data = JSON.stringify(
  {
    version: getFullVersion(),
  },
  undefined,
  2,
);

fs.writeFileSync(versionFile, data);

// https://stackoverflow.com/a/14181136/8418
fs.readFile(indexFile, "utf8", (error, data) => {
  if (error) {
    return console.error(error);
  }
  const result = data.replace(/{version}/g, getFullVersion());

  fs.writeFile(indexFile, result, "utf8", (error) => {
    if (error) {
      return console.error(error);
    }
  });
});

```

### File: scripts\buildBase.js
```js
const path = require("path");

const { build } = require("esbuild");

// contains all dependencies bundled inside
const getConfig = (outdir) => ({
  outdir,
  bundle: true,
  format: "esm",
  entryPoints: ["src/index.ts"],
  entryNames: "[name]",
  assetNames: "[dir]/[name]",
  alias: {
    "@excalidraw/utils": path.resolve(__dirname, "../packages/utils/src"),
  },
  external: ["@excalidraw/common", "@excalidraw/element", "@excalidraw/math"],
});

function buildDev(config) {
  return build({
    ...config,
    sourcemap: true,
    define: {
      "import.meta.env": JSON.stringify({ DEV: true }),
    },
  });
}

function buildProd(config) {
  return build({
    ...config,
    minify: true,
    define: {
      "import.meta.env": JSON.stringify({ PROD: true }),
    },
  });
}

const createESMRawBuild = async () => {
  // development unminified build with source maps
  await buildDev(getConfig("dist/dev"));

  // production minified build without sourcemaps
  await buildProd(getConfig("dist/prod"));
};

(async () => {
  await createESMRawBuild();
})();

```

### File: scripts\buildDocs.js
```js
const { exec } = require("child_process");

// get files changed between prev and head commit
exec(`git diff --name-only HEAD^ HEAD`, async (error, stdout, stderr) => {
  if (error || stderr) {
    console.error(error);
    process.exit(1);
  }
  const changedFiles = stdout.trim().split("\n");

  const docFiles = changedFiles.filter((file) => {
    return file.indexOf("docs") >= 0;
  });

  if (!docFiles.length) {
    console.info("Skipping building docs as no valid diff found");
    process.exit(0);
  }
  // Exit code 1 to build the docs in ignoredBuildStep
  process.exit(1);
});

```

### File: scripts\buildPackage.js
```js
const path = require("path");
const fs = require("fs");
const { pathToFileURL } = require("url");

const { build } = require("esbuild");
const { sassPlugin } = require("esbuild-sass-plugin");

const { parseEnvVariables } = require("../packages/excalidraw/env.cjs");

const ENV_VARS = {
  development: {
    ...parseEnvVariables(`${__dirname}/../.env.development`),
    DEV: true,
  },
  production: {
    ...parseEnvVariables(`${__dirname}/../.env.production`),
    PROD: true,
  },
};

// Resolve a relative path from the source file's directory
const resolveRelativePath = (importPath, sourceFile) => {
  const sourceDir = path.dirname(sourceFile);
  const extensions = [".scss", ".css", ""];

  for (const ext of extensions) {
    const fullPath = path.resolve(sourceDir, importPath + ext);
    if (fs.existsSync(fullPath)) {
      return fullPath;
    }
    // Try with underscore prefix for partials
    const partialPath = path.join(
      path.dirname(fullPath),
      `_${path.basename(fullPath)}`,
    );
    if (fs.existsSync(partialPath)) {
      return partialPath;
    }
  }
  return null;
};

// Precompile function to convert relative paths to absolute paths
const precompile = (source, sourcePath) => {
  // Match @use and @forward statements with relative paths
  const importRegex = /(@use|@forward)\s+["'](\.[^"']+)["']/g;

  return source.replace(importRegex, (match, directive, importPath) => {
    const resolvedPath = resolveRelativePath(importPath, sourcePath);
    if (resolvedPath) {
      // Convert to file:// URL format for sass
      const fileUrl = pathToFileURL(resolvedPath).href;
      return `${directive} "${fileUrl}"`;
    }
    return match;
  });
};

// excludes all external dependencies and bundles only the source code
const getConfig = (outdir) => ({
  outdir,
  bundle: true,
  splitting: true,
  format: "esm",
  packages: "external",
  plugins: [
    sassPlugin({
      precompile,
    }),
  ],
  target: "es2020",
  assetNames: "[dir]/[name]",
  chunkNames: "[dir]/[name]-[hash]",
  alias: {
    "@excalidraw/utils": path.resolve(__dirname, "../packages/utils/src"),
  },
  external: ["@excalidraw/common", "@excalidraw/element", "@excalidraw/math"],
  loader: {
    ".woff2": "file",
  },
});

function buildDev(config) {
  return build({
    ...config,
    sourcemap: true,
    define: {
      "import.meta.env": JSON.stringify(ENV_VARS.development),
    },
  });
}

function buildProd(config) {
  return build({
    ...config,
    minify: true,
    define: {
      "import.meta.env": JSON.stringify(ENV_VARS.production),
    },
  });
}

const createESMRawBuild = async () => {
  const chunksConfig = {
    entryPoints: ["index.tsx", "**/*.chunk.ts"],
    entryNames: "[name]",
  };

  // development unminified build with source maps
  await buildDev({
    ...getConfig("dist/dev"),
    ...chunksConfig,
  });

  // production minified buld without sourcemaps
  await buildProd({
    ...getConfig("dist/prod"),
    ...chunksConfig,
  });
};

(async () => {
  await createESMRawBuild();
})();

```

### File: scripts\buildUtils.js
```js
const path = require("path");

const { build } = require("esbuild");
const { sassPlugin } = require("esbuild-sass-plugin");

const { woff2ServerPlugin } = require("./woff2/woff2-esbuild-plugins");

// contains all dependencies bundled inside
const getConfig = (outdir) => ({
  outdir,
  bundle: true,
  format: "esm",
  entryPoints: ["src/index.ts"],
  entryNames: "[name]",
  assetNames: "[dir]/[name]",
  alias: {
    "@excalidraw/common": path.resolve(__dirname, "../packages/common/src"),
    "@excalidraw/element": path.resolve(__dirname, "../packages/element/src"),
    "@excalidraw/excalidraw": path.resolve(__dirname, "../packages/excalidraw"),
    "@excalidraw/math": path.resolve(__dirname, "../packages/math/src"),
    "@excalidraw/utils": path.resolve(__dirname, "../packages/utils/src"),
  },
});

function buildDev(config) {
  return build({
    ...config,
    sourcemap: true,
    plugins: [sassPlugin(), woff2ServerPlugin()],
    define: {
      "import.meta.env": JSON.stringify({ DEV: true }),
    },
  });
}

function buildProd(config) {
  return build({
    ...config,
    minify: true,
    plugins: [
      sassPlugin(),
      woff2ServerPlugin({
        outdir: `${config.outdir}/assets`,
      }),
    ],
    define: {
      "import.meta.env": JSON.stringify({ PROD: true }),
    },
  });
}

const createESMRawBuild = async () => {
  // development unminified build with source maps
  await buildDev(getConfig("dist/dev"));

  // production minified build without sourcemaps
  await buildProd(getConfig("dist/prod"));
};

(async () => {
  await createESMRawBuild();
})();

```

### File: scripts\buildWasm.js
```js
/**
 * This script is used to convert the wasm modules into js modules, with the binary converted into base64 encoded strings.
 */
const fs = require("fs");
const path = require("path");

const wasmModules = [
  {
    pkg: `../node_modules/fonteditor-core`,
    src: `./wasm/woff2.wasm`,
    dest: `../packages/excalidraw/fonts/wasm/woff2-wasm.ts`,
  },
  {
    pkg: `../node_modules/harfbuzzjs`,
    src: `./wasm/hb-subset.wasm`,
    dest: `../packages/excalidraw/fonts/wasm/hb-subset-wasm.ts`,
  },
];

for (const { pkg, src, dest } of wasmModules) {
  const packagePath = path.resolve(__dirname, pkg, "package.json");
  const licensePath = path.resolve(__dirname, pkg, "LICENSE");
  const sourcePath = path.resolve(__dirname, src);
  const destPath = path.resolve(__dirname, dest);

  const {
    name,
    version,
    author,
    license,
    authors,
    licenses,
  } = require(packagePath);

  const licenseContent = fs.readFileSync(licensePath, "utf-8") || "";
  const base64 = fs.readFileSync(sourcePath, "base64");
  const content = `// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

/**
* The following wasm module is generated with \`scripts/buildWasm.js\` and encoded as base64.
*
* The source of this content is taken from the package "${name}", which contains the following metadata:
* 
* @author ${author || JSON.stringify(authors)} 
* @license ${license || JSON.stringify(licenses)}
* @version ${version}

${licenseContent}
*/

// faster atob alternative - https://github.com/evanw/esbuild/issues/1534#issuecomment-902738399
const __toBinary = /* @__PURE__ */ (() => {
  const table = new Uint8Array(128);
  for (let i = 0; i < 64; i++)
    {table[i < 26 ? i + 65 : i < 52 ? i + 71 : i < 62 ? i - 4 : i * 4 - 205] = i;}
  return (base64) => {
    const n = base64.length; const bytes = new Uint8Array((n - (base64[n - 1] == "=") - (base64[n - 2] == "=")) * 3 / 4 | 0);
    for (let i2 = 0, j = 0; i2 < n; ) {
      const c0 = table[base64.charCodeAt(i2++)]; const c1 = table[base64.charCodeAt(i2++)];
      const c2 = table[base64.charCodeAt(i2++)]; const c3 = table[base64.charCodeAt(i2++)];
      bytes[j++] = c0 << 2 | c1 >> 4;
      bytes[j++] = c1 << 4 | c2 >> 2;
      bytes[j++] = c2 << 6 | c3;
    }
    return bytes;
  };
})();

export default __toBinary(\`${base64}\`);
`;

  fs.writeFileSync(destPath, content);
}

```

### File: scripts\locales-coverage-description.js
```js
const fs = require("fs");

const THRESSHOLD = 85;

// we're using BCP 47 language tags as keys
// e.g. https://gist.github.com/typpo/b2b828a35e683b9bf8db91b5404f1bd1

const crowdinMap = {
  "ar-SA": "en-ar",
  "bg-BG": "en-bg",
  "bn-BD": "en-bn",
  "ca-ES": "en-ca",
  "da-DK": "en-da",
  "de-DE": "en-de",
  "el-GR": "en-el",
  "es-ES": "en-es",
  "eu-ES": "en-eu",
  "fa-IR": "en-fa",
  "fi-FI": "en-fi",
  "fr-FR": "en-fr",
  "gl-ES": "en-gl",
  "he-IL": "en-he",
  "hi-IN": "en-hi",
  "hu-HU": "en-hu",
  "id-ID": "en-id",
  "it-IT": "en-it",
  "ja-JP": "en-ja",
  "kab-KAB": "en-kab",
  "ko-KR": "en-ko",
  "ku-TR": "en-ku",
  "my-MM": "en-my",
  "nb-NO": "en-nb",
  "nl-NL": "en-nl",
  "nn-NO": "en-nnno",
  "oc-FR": "en-oc",
  "pa-IN": "en-pain",
  "pl-PL": "en-pl",
  "pt-BR": "en-ptbr",
  "pt-PT": "en-pt",
  "ro-RO": "en-ro",
  "ru-RU": "en-ru",
  "si-LK": "en-silk",
  "sk-SK": "en-sk",
  "sl-SI": "en-sl",
  "sv-SE": "en-sv",
  "ta-IN": "en-ta",
  "tr-TR": "en-tr",
  "uk-UA": "en-uk",
  "zh-CN": "en-zhcn",
  "zh-HK": "en-zhhk",
  "zh-TW": "en-zhtw",
  "lt-LT": "en-lt",
  "lv-LV": "en-lv",
  "cs-CZ": "en-cs",
  "kk-KZ": "en-kk",
  "vi-VN": "en-vi",
  "mr-IN": "en-mr",
  "th-TH": "en-th",
};

const flags = {
  "ar-SA": "🇸🇦",
  "bg-BG": "🇧🇬",
  "bn-BD": "🇧🇩",
  "ca-ES": "🏳",
  "cs-CZ": "🇨🇿",
  "da-DK": "🇩🇰",
  "de-DE": "🇩🇪",
  "el-GR": "🇬🇷",
  "es-ES": "🇪🇸",
  "fa-IR": "🇮🇷",
  "fi-FI": "🇫🇮",
  "fr-FR": "🇫🇷",
  "gl-ES": "🇪🇸",
  "he-IL": "🇮🇱",
  "hi-IN": "🇮🇳",
  "hu-HU": "🇭🇺",
  "id-ID": "🇮🇩",
  "it-IT": "🇮🇹",
  "ja-JP": "🇯🇵",
  "kab-KAB": "🏳",
  "kk-KZ": "🇰🇿",
  "ko-KR": "🇰🇷",
  "ku-TR": "🏳",
  "lt-LT": "🇱🇹",
  "lv-LV": "🇱🇻",
  "my-MM": "🇲🇲",
  "nb-NO": "🇳🇴",
  "nl-NL": "🇳🇱",
  "nn-NO": "🇳🇴",
  "oc-FR": "🏳",
  "pa-IN": "🇮🇳",
  "pl-PL": "🇵🇱",
  "pt-BR": "🇧🇷",
  "pt-PT": "🇵🇹",
  "ro-RO": "🇷🇴",
  "ru-RU": "🇷🇺",
  "si-LK": "🇱🇰",
  "sk-SK": "🇸🇰",
  "sl-SI": "🇸🇮",
  "sv-SE": "🇸🇪",
  "ta-IN": "🇮🇳",
  "tr-TR": "🇹🇷",
  "uk-UA": "🇺🇦",
  "zh-CN": "🇨🇳",
  "zh-HK": "🇭🇰",
  "zh-TW": "🇹🇼",
  "eu-ES": "🇪🇦",
  "vi-VN": "🇻🇳",
  "mr-IN": "🇮🇳",
  "th-TH": "🇹🇭",
};

const languages = {
  "ar-SA": "العربية",
  "bg-BG": "Български",
  "bn-BD": "Bengali",
  "ca-ES": "Català",
  "cs-CZ": "Česky",
  "da-DK": "Dansk",
  "de-DE": "Deutsch",
  "el-GR": "Ελληνικά",
  "es-ES": "Español",
  "eu-ES": "Euskara",
  "fa-IR": "فارسی",
  "fi-FI": "Suomi",
  "fr-FR": "Français",
  "gl-ES": "Galego",
  "he-IL": "עברית",
  "hi-IN": "हिन्दी",
  "hu-HU": "Magyar",
  "id-ID": "Bahasa Indonesia",
  "it-IT": "Italiano",
  "ja-JP": "日本語",
  "kab-KAB": "Taqbaylit",
  "kk-KZ": "Қазақ тілі",
  "ko-KR": "한국어",
  "ku-TR": "Kurdî",
  "lt-LT": "Lietuvių",
  "lv-LV": "Latviešu",
  "my-MM": "Burmese",
  "nb-NO": "Norsk bokmål",
  "nl-NL": "Nederlands",
  "nn-NO": "Norsk nynorsk",
  "oc-FR": "Occitan",
  "pa-IN": "ਪੰਜਾਬੀ",
  "pl-PL": "Polski",
  "pt-BR": "Português Brasileiro",
  "pt-PT": "Português",
  "ro-RO": "Română",
  "ru-RU": "Русский",
  "si-LK": "සිංහල",
  "sk-SK": "Slovenčina",
  "sl-SI": "Slovenščina",
  "sv-SE": "Svenska",
  "ta-IN": "Tamil",
  "tr-TR": "Türkçe",
  "uk-UA": "Українська",
  "zh-CN": "简体中文",
  "zh-HK": "繁體中文 (香港)",
  "zh-TW": "繁體中文",
  "vi-VN": "Tiếng Việt",
  "mr-IN": "मराठी",
  "th-TH": "ภาษาไทย",
};

const percentages = fs.readFileSync(
  `${__dirname}/../packages/excalidraw/locales/percentages.json`,
);
const rowData = JSON.parse(percentages);

const coverages = Object.entries(rowData)
  .sort(([, a], [, b]) => b - a)
  .reduce((r, [k, v]) => ({ ...r, [k]: v }), {});

const boldIf = (text, condition) => (condition ? `**${text}**` : text);

const printHeader = () => {
  let result = "| | Flag | Locale | % |\n";
  result += "| :--: | :--: | -- | :--: |";
  return result;
};

const printRow = (id, locale, coverage) => {
  const isOver = coverage >= THRESSHOLD;
  let result = `| ${isOver ? id : "..."} | `;
  result += `${locale in flags ? flags[locale] : ""} | `;
  const language = locale in languages ? languages[locale] : locale;
  if (locale in crowdinMap && crowdinMap[locale]) {
    result += `[${boldIf(
      language,
      isOver,
    )}](https://crowdin.com/translate/excalidraw/10/${crowdinMap[locale]}) | `;
  } else {
    result += `${boldIf(language, isOver)} | `;
  }
  result += `${coverage === 100 ? "💯" : boldIf(coverage, isOver)} |`;
  return result;
};

console.info(
  `Each language must be at least **${THRESSHOLD}%** translated in order to appear on Excalidraw. Join us on [Crowdin](https://crowdin.com/project/excalidraw) and help us translate your own language. **Can't find yours yet?** Open an [issue](https://github.com/excalidraw/excalidraw/issues/new) and we'll add it to the list.`,
);
console.info("\n\r");
console.info(printHeader());
let index = 1;
for (const coverage in coverages) {
  if (coverage === "en") {
    continue;
  }
  console.info(printRow(index, coverage, coverages[coverage]));
  index++;
}
console.info("\n\r");
console.info("\\* Languages in **bold** are going to appear on production.");

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
