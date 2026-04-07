---
id: react
type: knowledge
owner: OA_Triage
---
# react
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "private": true,
  "workspaces": [
    "packages/*"
  ],
  "devDependencies": {
    "@babel/cli": "^7.10.5",
    "@babel/code-frame": "^7.10.4",
    "@babel/core": "^7.11.1",
    "@babel/helper-define-map": "^7.18.6",
    "@babel/helper-module-imports": "^7.10.4",
    "@babel/parser": "^7.11.3",
    "@babel/plugin-external-helpers": "^7.10.4",
    "@babel/plugin-proposal-class-properties": "^7.10.4",
    "@babel/plugin-proposal-object-rest-spread": "^7.11.0",
    "@babel/plugin-syntax-dynamic-import": "^7.8.3",
    "@babel/plugin-syntax-import-meta": "^7.10.4",
    "@babel/plugin-syntax-jsx": "^7.23.3",
    "@babel/plugin-syntax-typescript": "^7.14.5",
    "@babel/plugin-transform-arrow-functions": "^7.10.4",
    "@babel/plugin-transform-block-scoped-functions": "^7.10.4",
    "@babel/plugin-transform-block-scoping": "^7.11.1",
    "@babel/plugin-transform-class-properties": "^7.25.9",
    "@babel/plugin-transform-classes": "^7.10.4",
    "@babel/plugin-transform-computed-properties": "^7.10.4",
    "@babel/plugin-transform-destructuring": "^7.10.4",
    "@babel/plugin-transform-for-of": "^7.10.4",
    "@babel/plugin-transform-literals": "^7.10.4",
    "@babel/plugin-transform-modules-commonjs": "^7.10.4",
    "@babel/plugin-transform-object-super": "^7.10.4",
    "@babel/plugin-transform-parameters": "^7.10.5",
    "@babel/plugin-transform-private-methods": "^7.10.4",
    "@babel/plugin-transform-react-jsx": "^7.23.4",
    "@babel/plugin-transform-react-jsx-development": "^7.22.5",
    "@babel/plugin-transform-react-jsx-source": "^7.10.5",
    "@babel/plugin-transform-shorthand-properties": "^7.10.4",
    "@babel/plugin-transform-spread": "^7.11.0",
    "@babel/plugin-transform-template-literals": "^7.10.5",
    "@babel/preset-env": "^7.26.9",
    "@babel/preset-flow": "^7.10.4",
    "@babel/preset-react": "^7.23.3",
    "@babel/preset-typescript": "^7.26.0",
    "@babel/traverse": "^7.11.0",
    "@rollup/plugin-babel": "^6.0.3",
    "@rollup/plugin-commonjs": "^24.0.1",
    "@rollup/plugin-node-resolve": "^15.0.1",
    "@rollup/plugin-replace": "^5.0.2",
    "@rollup/plugin-typescript": "^12.1.2",
    "@types/invariant": "^2.2.35",
    "@typescript-eslint/eslint-plugin": "^6.21.0",
    "@typescript-eslint/parser": "^6.21.0",
    "abortcontroller-polyfill": "^1.7.5",
    "art": "0.10.1",
    "babel-plugin-syntax-hermes-parser": "^0.32.0",
    "babel-plugin-syntax-trailing-function-commas": "^6.5.0",
    "chalk": "^3.0.0",
    "cli-table": "^0.3.1",
    "coffee-script": "^1.12.7",
    "confusing-browser-globals": "^1.0.9",
    "core-js": "^3.6.4",
    "create-react-class": "^15.6.3",
    "danger": "^11.2.3",
    "error-stack-parser": "^2.0.6",
    "eslint": "^7.7.0",
    "eslint-config-prettier": "^6.9.0",
    "eslint-plugin-babel": "^5.3.0",
    "eslint-plugin-es": "^4.1.0",
    "eslint-plugin-eslint-plugin": "^3.5.3",
    "eslint-plugin-ft-flow": "^2.0.3",
    "eslint-plugin-jest": "28.4.0",
    "eslint-plugin-no-for-of-loops": "^1.0.0",
    "eslint-plugin-no-function-declare-after-return": "^1.0.0",
    "eslint-plugin-react": "^6.7.1",
    "eslint-plugin-react-hooks-published": "npm:eslint-plugin-react-hooks@^5.2.0",
    "eslint-plugin-react-internal": "link:./scripts/eslint-rules",
    "fbjs-scripts": "^3.0.1",
    "filesize": "^6.0.1",
    "flow-bin": "^0.279.0",
    "flow-remove-types": "^2.279.0",
    "flow-typed": "^4.1.1",
    "glob": "^7.1.6",
    "glob-stream": "^6.1.0",
    "google-closure-compiler": "^20230206.0.0",
    "gzip-size": "^5.1.1",
    "hermes-eslint": "^0.32.0",
    "hermes-parser": "^0.32.0",
    "jest": "^29.4.2",
    "jest-cli": "^29.4.2",
    "jest-diff": "^29.4.2",
    "jest-environment-jsdom": "^29.4.2",
    "jest-silent-reporter": "^0.6.0",
    "jest-snapshot-serializer-raw": "^1.2.0",
    "minimatch": "^3.0.4",
    "minimist": "^1.2.3",
    "mkdirp": "^0.5.1",
    "ncp": "^2.0.0",
    "prettier": "^3.3.3",
    "prettier-2": "npm:prettier@^2",
    "pretty-format": "^29.4.1",
    "prop-types": "^15.6.2",
    "random-seed": "^0.3.0",
    "react-lifecycles-compat": "^3.0.4",
    "rimraf": "^3.0.0",
    "rollup": "^3.29.5",
    "rollup-plugin-dts": "^6.1.1",
    "rollup-plugin-prettier": "^4.1.1",
    "rollup-plugin-strip-banner": "^3.0.0",
    "semver": "^7.1.1",
    "shelljs": "^0.8.5",
    "signedsource": "^2.0.0",
    "targz": "^1.0.1",
    "through2": "^3.0.1",
    "tmp": "^0.1.0",
    "to-fast-properties": "^2.0.0",
    "tsup": "^8.4.0",
    "typescript": "^5.4.3",
    "undici": "^5.28.4",
    "web-streams-polyfill": "^3.1.1",
    "yargs": "^15.3.1"
  },
  "jest": {
    "testRegex": "/scripts/jest/dont-run-jest-directly\\.js$"
  },
  "scripts": {
    "prebuild": "./scripts/react-compiler/link-compiler.sh",
    "build": "node ./scripts/rollup/build-all-release-channels.js",
    "build-for-devtools": "cross-env yarn build react/index,react/jsx,react/compiler-runtime,react-dom/index,react-dom/client,react-dom/unstable_testing,react-dom/test-utils,react-is,react-debug-tools,scheduler,react-test-renderer,react-refresh,react-art --type=NODE --release-channel=experimental",
    "build-for-devtools-dev": "yarn build-for-devtools --type=NODE_DEV",
    "build-for-devtools-prod": "yarn build-for-devtools --type=NODE_PROD",
    "build-for-flight-dev": "cross-env RELEASE_CHANNEL=experimental node ./scripts/rollup/build.js react/index,react/jsx,react.react-server,react-dom/index,react-dom/client,react-dom/server,react-dom.react-server,react-dom-server.node,react-dom-server-legacy.node,scheduler,react-server-dom-webpack/,react-server-dom-unbundled/ --type=NODE_DEV,ESM_PROD,NODE_ES2015 && mv ./build/node_modules ./build/oss-experimental",
    "build-for-flight-prod": "cross-env RELEASE_CHANNEL=experimental node ./scripts/rollup/build.js react/index,react/jsx,react.react-server,react-dom/index,react-dom/client,react-dom/server,react-dom.react-server,react-dom-server.node,react-dom-server-legacy.node,scheduler,react-server-dom-webpack/,react-server-dom-unbundled/ --type=NODE_PROD,ESM_PROD,NODE_ES2015 && mv ./build/node_modules ./build/oss-experimental",
    "build-for-vt-dev": "cross-env RELEASE_CHANNEL=experimental node ./scripts/rollup/build.js react/index,react/jsx,react-dom/index,react-dom/client,react-dom/server,react-dom-server.node,react-dom-server-legacy.node,scheduler --type=NODE_DEV && mv ./build/node_modules ./build/oss-experimental",
    "flow-typed-install": "yarn flow-typed install --skip --skipFlowRestart --ignore-deps=dev",
    "linc": "node ./scripts/tasks/linc.js",
    "lint": "node ./scripts/tasks/eslint.js",
    "lint-build": "node ./scripts/rollup/validate/index.js",
    "extract-errors": "node scripts/error-codes/extract-errors.js",
    "postinstall": "node ./scripts/flow/createFlowConfigs.js",
    "test": "node ./scripts/jest/jest-cli.js",
    "test-stable": "node ./scripts/jest/jest-cli.js --release-channel=stable",
    "test-www": "node ./scripts/jest/jest-cli.js --release-channel=www-modern",
    "test-classic": "node ./scripts/jest/jest-cli.js --release-channel=www-classic",
    "test-build-devtools": "node ./scripts/jest/jest-cli.js --build --project devtools --release-channel=experimental",
    "test-dom-fixture": "cd fixtures/dom && yarn && yarn test",
    "flow": "node ./scripts/tasks/flow.js",
    "flow-ci": "node ./scripts/tasks/flow-ci.js",
    "prettier": "node ./scripts/prettier/index.js write-changed",
    "prettier-all": "node ./scripts/prettier/index.js write",
    "prettier-check": "node ./scripts/prettier/index.js",
    "version-check": "node ./scripts/tasks/version-check.js",
    "publish-prereleases": "echo 'This command has been deprecated. Please refer to https://github.com/facebook/react/tree/main/scripts/release#trigger-an-automated-prerelease'",
    "download-build": "node ./scripts/release/download-experimental-build.js",
    "download-build-for-head": "node ./scripts/release/download-experimental-build.js --commit=$(git rev-parse HEAD)",
    "download-build-in-codesandbox-ci": "yarn build --type=node react/index react.react-server react-dom/index react-dom/client react-dom/src/server react-dom/test-utils react-dom.react-server scheduler/index react/jsx-runtime react/jsx-dev-runtime react-server-dom-webpack",
    "check-release-dependencies": "node ./scripts/release/check-release-dependencies",
    "generate-inline-fizz-runtime": "node ./scripts/rollup/generate-inline-fizz-runtime.js",
    "generate-changelog": "node ./scripts/tasks/generate-changelog/index.js",
    "flags": "node ./scripts/flags/flags.js"
  },
  "resolutions": {
    "react-is": "npm:react-is",
    "jsdom": "22.1.0"
  },
  "packageManager": "yarn@1.22.22"
}

```

### File: README.md
```md
<a href="https://www.callstack.com/open-source?utm_campaign=generic&utm_source=github&utm_medium=referral&utm_content=react-native-bottom-tabs" align="center">
  <picture>
    <img alt="React Native Bottom Tabs" src="https://github.com/user-attachments/assets/bbd9632c-4df1-450b-832b-3e03280f3ce7">
  </picture>
</a>
<p align="center">
  <strong><a href="https://oss.callstack.com/react-native-bottom-tabs/">React Native Bottom Tabs</a> that use native platform primitives.</strong><br>
</p>

<div align="center">

[![mit licence](https://img.shields.io/dub/l/vibe-d.svg?style=for-the-badge)](https://github.com/callstack/react-native-bottom-tabs/blob/main/LICENSE)
[![npm version](https://img.shields.io/npm/v/react-native-bottom-tabs?style=for-the-badge)](https://www.npmjs.org/package/react-native-bottom-tabs)
[![npm downloads](https://img.shields.io/npm/dt/react-native-bottom-tabs.svg?style=for-the-badge)](https://www.npmjs.org/package/react-native-bottom-tabs)
[![npm downloads](https://img.shields.io/npm/dm/react-native-bottom-tabs.svg?style=for-the-badge)](https://www.npmjs.org/package/react-native-bottom-tabs)

</div>

https://github.com/user-attachments/assets/09e96ac3-827d-4ac0-add0-e7b88ee9197c

## Supported Platforms

| Platform |  |
|:---:|:---:|
| **iOS** | <img src="https://github.com/user-attachments/assets/bd737e01-d7be-44f2-a0b6-67664e670933" width="400" /> |
| **Android** | <img src="https://github.com/user-attachments/assets/5120a6d0-be92-44cf-a3bf-668944ad9475" width="400" /> |
| **iPadOS** | <img src="https://github.com/user-attachments/assets/1504949f-ed36-44cc-9153-373f9e584f44" width="400" /> |
| **visionOS** | <img src="https://github.com/user-attachments/assets/7d990950-b9bb-4a42-ab0c-fac975ffd098" width="400" /> |
| **tvOS** | <img src="https://github.com/user-attachments/assets/2fe8483d-73f9-408f-9315-100eee7bf2af" width="400" /> |
| **macOS** | <img src="https://github.com/user-attachments/assets/758decf4-6e70-4c55-8f2d-c16927f2c56d" width="400" /> |

> **Note:** This library uses native platform primitives which are not available on web. For web support, see the [Web Platform Support guide](https://oss.callstack.com/react-native-bottom-tabs/docs/guides/web-platform-support) in the documentation.

## Package Versions

| Name                                                                         |                                                                      Latest Version                                                                       |
| ---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [react-native-bottom-tabs](/packages/react-native-bottom-tabs)               | [![badge](https://img.shields.io/npm/v/react-native-bottom-tabs?style=for-the-badge)](https://www.npmjs.com/package/react-native-bottom-tabs)                             |
| [@bottom-tabs/react-navigation](/packages/react-navigation)                  | [![badge](https://img.shields.io/npm/v/@bottom-tabs/react-navigation.svg?style=for-the-badge)](https://www.npmjs.com/package/@bottom-tabs/react-navigation)                   |

## Documentation

The full documentation can be found on our [website](https://oss.callstack.com/react-native-bottom-tabs/).

## Contributing

See the [contributing guide](CONTRIBUTING.md) to learn how to contribute to the repository and the development workflow.

## License

MIT

---

Made with ❤️ and [create-react-native-library](https://github.com/callstack/react-native-builder-bob)

```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works
with multi-package repos, or single-package repos to help you version and publish your code. You can
find the full documentation for it [in our repository](https://github.com/changesets/changesets)

We have a quick list of common questions to get you started engaging with this project in
[our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md)

```

### File: docs\package.json
```json
{
  "name": "react-native-bottom-tabs-docs",
  "version": "1.0.0",
  "private": true,
  "installConfig": {
    "hoistingLimits": "workspaces"
  },
  "scripts": {
    "dev": "rspress dev",
    "build": "rspress build",
    "preview": "rspress preview"
  },
  "dependencies": {
    "@callstack/rspress-preset": "^0.4.1",
    "@rspress/core": "2.0.0-beta.32"
  },
  "devDependencies": {
    "@types/node": "^20"
  }
}

```

### File: registry\README.md
```md
# react-kino shadcn Registry

Install thin react-kino wrapper components directly into your project using the shadcn CLI:

```bash
# Install a single component
npx shadcn add https://react-kino.dev/registry/components/scene.json

# Install the package used by wrappers (recommended)
npm install react-kino
```

## Available Components

| Component | Description |
|-----------|-------------|
| `kino` | Root provider |
| `scene` | Pinned scroll section |
| `reveal` | Scroll-triggered entrance |
| `parallax` | Speed-shifted layer |
| `counter` | Animated number |
| `compare-slider` | Before/after slider |
| `horizontal-scroll` | Horizontal scroll section |
| `progress` | Scroll indicator |
| `video-scroll` | Scroll-driven video scrubber |
| `text-reveal` | Progressive text reveal |

```

### File: apps\docs\package.json
```json
{
  "name": "@react-kino/docs",
  "private": true,
  "scripts": {
    "build": "next build",
    "dev": "next dev --port 5173",
    "start": "next start",
    "clean": "rm -rf .next .source",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "fumadocs-core": "^14.7.7",
    "fumadocs-mdx": "^10.1.0",
    "fumadocs-ui": "^14.7.7",
    "next": "^15",
    "react": "^19",
    "react-dom": "^19",
    "@react-kino/templates": "workspace:*",
    "react-kino": "workspace:*"
  },
  "devDependencies": {
    "@types/mdx": "^2",
    "@types/node": "^22",
    "@types/react": "~19.1.0",
    "@types/react-dom": "~19.1.0",
    "autoprefixer": "^10",
    "postcss": "^8",
    "tailwindcss": "^3.4.14",
    "typescript": "^5"
  }
}

```

### File: apps\example\index.js
```js
import { AppRegistry } from 'react-native';
import App from './src/App';
import { name as appName } from './app.json';

AppRegistry.registerComponent(appName, () => App);

```

### File: apps\example\package.json
```json
{
  "name": "react-native-bottom-tabs-example",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "android": "react-native run-android",
    "build:android": "npm run mkdist && react-native bundle --entry-file index.js --platform android --dev true --bundle-output dist/main.android.jsbundle --assets-dest dist && react-native build-android --extra-params \"--no-daemon --console=plain -PreactNativeArchitectures=arm64-v8a -PnewArchEnabled=true\"",
    "build:ios": "npm run mkdist && react-native bundle --entry-file index.js --platform ios --dev true --bundle-output dist/main.ios.jsbundle --assets-dest dist",
    "ios": "react-native run-ios",
    "mkdist": "node -e \"require('node:fs').mkdirSync('dist', { recursive: true, mode: 0o755 })\"",
    "start": "react-native start"
  },
  "dependencies": {
    "@bottom-tabs/react-navigation": "*",
    "@react-navigation/bottom-tabs": "^7.4.7",
    "@react-navigation/devtools": "^7.0.44",
    "@react-navigation/native": "^7.1.17",
    "@react-navigation/native-stack": "^7.3.26",
    "@react-navigation/stack": "^7.4.8",
    "color": "^5.0.0",
    "react": "^19.1.0",
    "react-native": "^0.81.4",
    "react-native-bottom-tabs": "*",
    "react-native-edge-to-edge": "^1.7.0",
    "react-native-gesture-handler": "^2.28.0",
    "react-native-paper": "^5.14.5",
    "react-native-safe-area-context": "^5.6.1",
    "react-native-screens": "^4.18.0",
    "react-native-vector-icons": "^10.2.0"
  },
  "devDependencies": {
    "@babel/core": "^7.28.4",
    "@babel/preset-env": "^7.28.3",
    "@babel/runtime": "^7.28.4",
    "@react-native-community/cli": "^20.0.2",
    "@react-native/babel-preset": "^0.81.4",
    "@react-native/metro-config": "0.81.4",
    "@react-native/typescript-config": "0.81.4",
    "@rnx-kit/metro-config": "^2.1.0",
    "@types/react-native-vector-icons": "^6.4.18",
    "babel-plugin-module-resolver": "^5.0.2",
    "react-native-builder-bob": "^0.40.13",
    "react-native-test-app": "^4.4.10"
  },
  "engines": {
    "node": ">=18"
  }
}

```

### File: apps\playground\package.json
```json
{
  "name": "@react-kino/playground",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "clean": "rm -rf dist",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^19",
    "react-dom": "^19",
    "react-kino": "workspace:*"
  },
  "devDependencies": {
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitejs/plugin-react": "^5",
    "typescript": "^5",
    "vite": "^7"
  }
}

```

### File: apps\test\package.json
```json
{
  "name": "@react-kino/test",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "clean": "rm -rf dist"
  },
  "dependencies": {
    "react": "^19",
    "react-dom": "^19",
    "react-kino": "^0.3.1"
  },
  "devDependencies": {
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitejs/plugin-react": "^5",
    "typescript": "^5",
    "vite": "^7"
  }
}

```

### File: apps\website\package.json
```json
{
  "name": "@react-grab/website",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "pnpm --filter react-grab build && pnpm --filter react-grab exec cp dist/index.global.js ../../apps/website/public/script.js && pnpm --filter @react-grab/design-system build && next build",
    "start": "next start",
    "lint": "oxlint"
  },
  "dependencies": {
    "@base-ui/react": "^1.2.0",
    "@react-grab/design-system": "workspace:*",
    "@vercel/analytics": "^1.5.0",
    "calligraph": "^1.4.1",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.553.0",
    "motion": "^12.23.24",
    "next": "16.0.10",
    "nuqs": "^2.8.1",
    "react": "19.2.1",
    "react-dom": "19.2.1",
    "react-grab": "workspace:*",
    "shiki": "^1.24.3",
    "tailwind-merge": "^3.4.0",
    "web-haptics": "^0.0.6"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "tailwindcss": "^4",
    "tw-animate-css": "^1.4.0",
    "typescript": "^5"
  },
  "browserslist": [
    "chrome >= 91",
    "firefox >= 90",
    "safari >= 15",
    "edge >= 91"
  ]
}

```

### File: packages\cli\package.json
```json
{
  "name": "@react-kino/cli",
  "version": "0.1.3",
  "description": "CLI for scaffolding react-kino scroll pages",
  "bin": {
    "kino": "./dist/index.js"
  },
  "main": "./dist/index.js",
  "files": [
    "dist",
    "templates"
  ],
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "clean": "rm -rf dist",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "fs-extra": "^11",
    "kleur": "^4",
    "prompts": "^2"
  },
  "devDependencies": {
    "@types/fs-extra": "^11",
    "@types/prompts": "^2",
    "tsup": "^8",
    "typescript": "^5"
  },
  "license": "MIT",
  "engines": {
    "node": ">=20"
  }
}

```

### File: packages\cli\README.md
```md
# @react-grab/cli

Interactive CLI to install and configure React Grab in your project.

## Quick Start

```bash
npx grab@latest init
```

## Commands

### `grab init`

Initialize React Grab in your project. Auto-detects your framework and applies the necessary changes.

```bash
npx grab@latest init
```

| Option           | Alias | Description                              |
| ---------------- | ----- | ---------------------------------------- |
| `--yes`          | `-y`  | Skip confirmation prompts                |
| `--force`        | `-f`  | Force overwrite existing config          |
| `--key <key>`    | `-k`  | Activation key (e.g. Meta+K, Space)      |
| `--skip-install` |       | Skip package installation                |
| `--pkg <pkg>`    |       | Custom package URL                       |
| `--cwd <cwd>`   | `-c`  | Working directory (default: current dir) |

### `grab add`

Connect React Grab to your coding agent via MCP.

```bash
npx grab@latest add mcp
```

| Option       | Alias | Description                              |
| ------------ | ----- | ---------------------------------------- |
| `--yes`      | `-y`  | Skip confirmation prompts                |
| `--cwd <cwd>`| `-c` | Working directory (default: current dir) |

### `grab remove`

Disconnect React Grab from your coding agent.

```bash
npx grab@latest remove mcp
```

| Option       | Alias | Description                              |
| ------------ | ----- | ---------------------------------------- |
| `--yes`      | `-y`  | Skip confirmation prompts                |
| `--cwd <cwd>`| `-c` | Working directory (default: current dir) |

### `grab configure`

Configure React Grab options. Runs an interactive wizard when called without flags.

```bash
npx grab@latest configure
```

| Option                  | Alias | Description                                  |
| ----------------------- | ----- | -------------------------------------------- |
| `--yes`                 | `-y`  | Skip confirmation prompts                    |
| `--key <key>`           | `-k`  | Activation key (e.g. Meta+K, Ctrl+Shift+G)   |
| `--mode <mode>`         | `-m`  | Activation mode (`toggle` or `hold`)          |
| `--hold-duration <ms>`  |       | Key hold duration in ms (hold mode, max 2000) |
| `--allow-input <bool>`  |       | Allow activation inside input fields          |
| `--context-lines <n>`   |       | Max context lines (max 50)                    |
| `--cdn <domain>`        |       | CDN domain (e.g. unpkg.com)                   |
| `--cwd <cwd>`           | `-c`  | Working directory (default: current dir)      |

## Examples

```bash
# Interactive setup
npx grab@latest init

# Non-interactive setup
npx grab@latest init -y

# Set a custom activation key
npx grab@latest init -k "Meta+K"

# Connect MCP to your agent
npx grab@latest add mcp

# Change activation mode to hold
npx grab@latest configure --mode hold --hold-duration 500

# Interactive configuration wizard
npx grab@latest configure
```

## Supported Frameworks

| Framework              | Detection                            |
| ---------------------- | ------------------------------------ |
| Next.js (App Router)   | `next.config.ts` + `app/` directory  |
| Next.js (Pages Router) | `next.config.ts` + `pages/` directory|
| Vite                   | `vite.config.ts`                     |
| Webpack                | `webpack.config.*`                   |

```

### File: packages\core\package.json
```json
{
  "name": "@react-kino/core",
  "version": "0.1.3",
  "description": "Framework-agnostic scroll engine powering react-kino",
  "main": "./dist/index.js",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.js"
    }
  },
  "files": [
    "dist"
  ],
  "sideEffects": false,
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "clean": "rm -rf dist",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "lint": "tsc --noEmit"
  },
  "devDependencies": {
    "tsup": "^8",
    "typescript": "^5",
    "vitest": "^4"
  },
  "author": "Bilal Tahir",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/btahir/react-kino.git",
    "directory": "packages/core"
  },
  "homepage": "https://github.com/btahir/react-kino#readme",
  "bugs": {
    "url": "https://github.com/btahir/react-kino/issues"
  }
}

```

### File: packages\design-system\package.json
```json
{
  "name": "@react-grab/design-system",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "main": "dist/index.js",
  "module": "dist/index.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "import": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      },
      "require": {
        "types": "./dist/index.d.cts",
        "default": "./dist/index.cjs"
      }
    }
  },
  "scripts": {
    "build": "vp pack",
    "dev": "vp pack --watch",
    "lint": "vp lint",
    "format": "vp fmt",
    "format:check": "vp fmt --check",
    "check": "vp check",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "react-grab": "workspace:*",
    "solid-js": "^1.9.10"
  },
  "devDependencies": {
    "@babel/core": "^7.28.5",
    "@babel/preset-typescript": "^7.28.5",
    "babel-preset-solid": "^1.9.10"
  }
}

```

### File: packages\mcp\package.json
```json
{
  "name": "@react-grab/mcp",
  "version": "0.1.29",
  "bin": {
    "react-grab-mcp": "./dist/cli.cjs"
  },
  "files": [
    "dist"
  ],
  "type": "module",
  "browser": "dist/client.global.js",
  "exports": {
    "./client": {
      "types": "./dist/client.d.ts",
      "import": "./dist/client.js",
      "require": "./dist/client.cjs"
    },
    "./server": {
      "types": "./dist/server.d.ts",
      "import": "./dist/server.js",
      "require": "./dist/server.cjs"
    },
    "./dist/*": "./dist/*.js",
    "./dist/*.js": "./dist/*.js"
  },
  "scripts": {
    "dev": "vp pack --watch",
    "build": "rm -rf dist && NODE_ENV=production vp pack && cp dist/client.iife.js dist/client.global.js",
    "lint": "vp lint",
    "format": "vp fmt",
    "format:check": "vp fmt --check",
    "check": "vp check"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.25.0",
    "fkill": "^9.0.0",
    "react-grab": "workspace:*",
    "zod": "^3.25.0"
  },
  "devDependencies": {
    "@types/node": "^22.10.7"
  }
}

```

### File: packages\react\index.js
```js
/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */

// Keep in sync with https://github.com/facebook/flow/blob/main/lib/react.js
export type ElementType = React$ElementType;
export type Element<+C> = React$Element<C>;
export type MixedElement = React$Element<ElementType>;
export type Key = React$Key;
export type Node = React$Node;
export type Context<T> = React$Context<T>;
export type Portal = React$Portal;
export type RefSetter<-I> = React$RefSetter<I>;
export type ElementProps<C> = React$ElementProps<C>;
export type ElementConfig<C> = React$ElementConfig<C>;
export type ElementRef<C> = React$ElementRef<C>;
export type ChildrenArray<+T> = $ReadOnlyArray<ChildrenArray<T>> | T;

export {
  __CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE,
  __COMPILER_RUNTIME,
  Children,
  Component,
  Fragment,
  Profiler,
  PureComponent,
  StrictMode,
  Suspense,
  cloneElement,
  createContext,
  createElement,
  createRef,
  use,
  forwardRef,
  isValidElement,
  lazy,
  memo,
  cache,
  cacheSignal,
  startTransition,
  unstable_LegacyHidden,
  Activity,
  unstable_Scope,
  unstable_SuspenseList,
  unstable_TracingMarker,
  ViewTransition,
  addTransitionType,
  unstable_getCacheForType,
  unstable_useCacheRefresh,
  useId,
  useCallback,
  useContext,
  useDebugValue,
  useDeferredValue,
  useEffect,
  useEffectEvent,
  useImperativeHandle,
  useInsertionEffect,
  useLayoutEffect,
  useMemo,
  useOptimistic,
  useSyncExternalStore,
  useReducer,
  useRef,
  useState,
  useTransition,
  useActionState,
  version,
} from './src/ReactClient';

```

### File: packages\react\package.json
```json
{
  "name": "react-kino",
  "version": "0.3.1",
  "description": "Cinematic scroll-driven storytelling components for React",
  "main": "./dist/index.js",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.js"
    }
  },
  "files": [
    "dist"
  ],
  "sideEffects": false,
  "scripts": {
    "build": "tsup && node scripts/add-use-client.mjs",
    "dev": "tsup --watch",
    "clean": "rm -rf dist",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "@react-kino/core": "workspace:^"
  },
  "peerDependencies": {
    "react": ">=18.0.0",
    "react-dom": ">=18.0.0"
  },
  "devDependencies": {
    "@testing-library/react": "^16",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "jsdom": "^28",
    "react": "^19",
    "react-dom": "^19",
    "tsup": "^8",
    "typescript": "^5",
    "vitest": "^4"
  },
  "keywords": [
    "react",
    "scroll",
    "animation",
    "storytelling",
    "parallax",
    "scroll-driven",
    "apple",
    "cinematic",
    "pinned",
    "sticky"
  ],
  "author": "Bilal Tahir",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/btahir/react-kino.git",
    "directory": "packages/react"
  },
  "homepage": "https://github.com/btahir/react-kino#readme",
  "bugs": {
    "url": "https://github.com/btahir/react-kino/issues"
  }
}

```

### File: packages\react\README.md
```md
<p align="center">
  <img src="https://raw.githubusercontent.com/btahir/react-kino/main/apps/docs/public/hero.gif" alt="react-kino — cinematic scroll-driven storytelling for React" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/npm/v/react-kino?style=flat-square&color=000" alt="npm version" />
  <img src="https://img.shields.io/bundlephobia/minzip/react-kino?style=flat-square&color=000" alt="bundle size" />
  <img src="https://img.shields.io/npm/l/react-kino?style=flat-square&color=000" alt="license" />
</p>

<h1 align="center">react-kino</h1>

<p align="center">
Cinematic scroll-driven storytelling for React.<br/>
Core scroll engine under 1 KB gzipped.
</p>

---

## Why react-kino

- **Tiny** -- the core scroll engine is under 1 KB gzipped. GSAP ScrollTrigger alone is 33 KB.
- **Declarative** -- compose `<Scene>`, `<Reveal>`, `<ScrollTransform>`, `<Parallax>`, `<Counter>`, `<StickyHeader>`, `<Marquee>`, and `<TextReveal>` like regular React components. No imperative timelines.
- **Lightweight runtime** -- `react-kino` uses a tiny internal engine package (`@react-kino/core`) plus React peers.
- **SSR-safe** -- every component renders children on the server and animates on the client.

## Installation

```bash
npm install react-kino
```

```bash
pnpm add react-kino
```

```bash
bun add react-kino
```

**Requirements:** React 18+

## Quick Start

```tsx
import { Kino, Scene, Reveal, Counter } from "react-kino";

function App() {
  return (
    <Kino>
      {/* A pinned scene that spans 300vh of scroll distance */}
      <Scene duration="300vh">
        {(progress) => (
          <div style={{ height: "100vh", display: "grid", placeItems: "center" }}>
            <Reveal animation="fade-up" at={0}>
              <h1>Welcome</h1>
            </Reveal>

            <Reveal animation="scale" at={0.3}>
              <p>Scroll-driven storytelling, made simple.</p>
            </Reveal>

            <Reveal animation="fade" at={0.6}>
              <Counter from={0} to={10000} format={(n) => `${n.toLocaleString()}+ users`} />
            </Reveal>
          </div>
        )}
      </Scene>
    </Kino>
  );
}
```

That is a complete scroll experience: the section pins in place, content fades in at different scroll points, and a number counts up -- all in ~20 lines.

---

## Components

### `<Kino>`

Root provider that initializes the scroll tracking engine. Wrap your app or page layout.

```tsx
import { Kino } from "react-kino";

<Kino>
  {/* your scenes and content */}
</Kino>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | -- | Child elements |

---

### `<Scene>`

A pinned scroll section. Content stays fixed in the viewport while the user scrolls through the scene's duration. This is the core building block.

```tsx
import { Scene } from "react-kino";

{/* Static children -- use child components that read progress from context */}
<Scene duration="200vh">
  <MyAnimatedContent />
</Scene>

{/* Render prop -- get progress directly */}
<Scene duration="400vh">
  {(progress) => (
    <div style={{ opacity: progress }}>
      {Math.round(progress * 100)}% scrolled
    </div>
  )}
</Scene>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `duration` | `string` | -- | Scroll distance the scene spans. Supports `vh` and `px` units (e.g. `"200vh"`, `"1500px"`) |
| `pin` | `boolean` | `true` | Whether to pin (sticky) the inner content during scroll |
| `children` | `ReactNode \| (progress: number) => ReactNode` | -- | Static content or render function receiving progress (0-1) |
| `className` | `string` | -- | CSS class for the outer spacer element |
| `style` | `CSSProperties` | -- | Inline styles for the sticky inner container |

**Context:** `<Scene>` provides a `SceneContext` that child components (`<Reveal>`, `<Counter>`, `<CompareSlider>`) automatically read from. You do not need to pass progress manually.

---

### `<Reveal>`

Scroll-triggered entrance animation. Place inside a `<Scene>` or provide a `progress` prop directly.

```tsx
import { Reveal } from "react-kino";

<Scene duration="300vh">
  <Reveal animation="fade-up" at={0.2}>
    <h2>Appears at 20% scroll</h2>
  </Reveal>

  <Reveal animation="blur" at={0.5} duration={800} delay={200}>
    <p>Blurs in at 50% with a delay</p>
  </Reveal>
</Scene>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `at` | `number` | `0` | Progress value (0-1) when animation triggers |
| `animation` | `RevealAnimation` | `"fade"` | Animation preset (see below) |
| `duration` | `number` | `600` | Animation duration in milliseconds |
| `delay` | `number` | `0` | Delay before animation starts in milliseconds |
| `progress` | `number` | -- | Direct progress override (0-1). If omitted, reads from parent `<Scene>` context |
| `children` | `ReactNode` | -- | Content to reveal |
| `className` | `string` | -- | CSS class for the wrapper div |

**Animation presets:**

| Preset | Effect |
|--------|--------|
| `"fade"` | Opacity 0 to 1 |
| `"fade-up"` | Fade in + slide up 40px |
| `"fade-down"` | Fade in + slide down 40px |
| `"scale"` | Fade in + scale from 0.9 to 1 |
| `"blur"` | Fade in + unblur from 12px |

---

### `<Parallax>`

A layer that scrolls at a different speed than the page, creating depth.

```tsx
import { Parallax } from "react-kino";

{/* Background image scrolls at half speed */}
<Parallax speed={0.3}>
  <img src="/hero-bg.jpg" alt="" style={{ width: "100%", height: "120vh", objectFit: "cover" }} />
</Parallax>

{/* Foreground element scrolls faster */}
<Parallax speed={1.5}>
  <div className="floating-badge">New</div>
</Parallax>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `speed` | `number` | `0.5` | Speed multiplier. `1` = normal scroll, `< 1` = slower (background feel), `> 1` = faster (foreground feel) |
| `direction` | `"vertical" \| "horizontal"` | `"vertical"` | Scroll direction for the parallax offset |
| `children` | `ReactNode` | -- | Content to apply parallax to |
| `className` | `string` | -- | CSS class |
| `style` | `CSSProperties` | -- | Inline styles (merged with transform) |

---

### `<Counter>`

An animated number that counts between two values as the user scrolls. Automatically reads progress from a parent `<Scene>`.

```tsx
import { Counter } from "react-kino";

<Scene duration="200vh">
  <Counter from={0} to={1000000} at={0.2} span={0.5} />

  <Counter
    from={0}
    to={99.9}
    format={(n) => `${n.toFixed(1)}%`}
    easing="ease-in-out"
  />
</Scene>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `from` | `number` | -- | Starting value |
| `to` | `number` | -- | Ending value |
| `at` | `number` | `0` | Progress value (0-1) when counting begins |
| `span` | `number` | `0.3` | How much of the progress range (0-1) the count spans |
| `format` | `(value: number) => string` | `toLocaleString` | Formatting function for the displayed value |
| `easing` | `string \| (t: number) => number` | `"ease-out"` | Easing preset name or custom easing function |
| `progress` | `number` | -- | Direct progress override (0-1). If omitted, reads from parent `<Scene>` context |
| `className` | `string` | -- | CSS class for the `<span>` element |

---

### `<ScrollTransform>`

Interpolates CSS transforms and opacity between two states as the user scrolls. Perfect for 3D device tilts, slide-in effects, and any scroll-driven transform animation.

```tsx
import { ScrollTransform } from "react-kino";

<Scene duration="350vh">
  <ScrollTransform
    from={{ rotateX: 40, rotateY: -12, scale: 0.82, opacity: 0.3 }}
    to={{ rotateX: 0, rotateY: 0, scale: 1, opacity: 1 }}
    perspective={1200}
    easing="ease-out-cubic"
    transformOrigin="center bottom"
  >
    <div className="card">Your content</div>
  </ScrollTransform>
</Scene>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `from` | `TransformState` | -- | Starting transform state |
| `to` | `TransformState` | -- | Ending transform state |
| `at` | `number` | `0` | Progress value (0-1) when transform begins |
| `span` | `number` | `1` | How much of the progress range the transform spans |
| `easing` | `string \| (t: number) => number` | `"ease-out"` | Easing preset name or custom function |
| `perspective` | `number` | -- | CSS perspective in px (enables 3D transforms) |
| `transformOrigin` | `string` | `"center center"` | CSS transform-origin |
| `progress` | `number` | -- | Direct progress override. If omitted, reads from parent `<Scene>` context |
| `className` | `string` | -- | CSS class for the wrapper div |
| `style` | `CSSProperties` | -- | Inline styles (merged with computed transform) |

**TransformState properties:** `x`, `y`, `z` (px), `scale`, `scaleX`, `scaleY`, `rotate`, `rotateX`, `rotateY` (deg), `skewX`, `skewY` (deg), `opacity` (0-1).

---

### `<CompareSlider>`

A before/after comparison slider. Supports both drag interaction and scroll-driven modes.

```tsx
import { CompareSlider } from "react-kino";

{/* Interactive drag mode */}
<CompareSlider
  before={<img src="/before.jpg" alt="Before" />}
  after={<img src="/after.jpg" alt="After" />}
/>

{/* Scroll-driven mode inside a Scene */}
<Scene duration="200vh">
  <CompareSlider
    scrollDriven
    before={<img src="/before.jpg" alt="Before" />}
    after={<img src="/after.jpg" alt="After" />}
  />
</Scene>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `before` | `ReactNode` | -- | Content shown on the "before" side (always visible underneath) |
| `after` | `ReactNode` | -- | Content shown on the "after" side (revealed via clip) |
| `scrollDriven` | `boolean` | `false` | If `true`, slider position follows scroll progress instead of drag |
| `progress` | `number` | -- | Progress override (0-1). When `scrollDriven`, defaults to parent `<Scene>` context |
| `initialPosition` | `number` | `0.5` | Initial slider position (0-1) in drag mode |
| `className` | `string` | -- | CSS class for the container |

---

### `<HorizontalScroll>`

Converts vertical scroll into horizontal movement. Wrap `<Panel>` components inside it.

```tsx
import { HorizontalScroll, Panel } from "react-kino";

<HorizontalScroll>
  <Panel>
    <div style={{ background: "#111", color: "#fff", padding: 60 }}>
      <h2>Panel One</h2>
    </div>
  </Panel>
  <Panel>
    <div style={{ background: "#222", color: "#fff", padding: 60 }}>
      <h2>Panel Two</h2>
    </div>
  </Panel>
</HorizontalScroll>
```

**`<HorizontalScroll>` props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | -- | `<Panel>` components |
| `className` | `string` | -- | CSS class for the outer spacer |
| `panelHeight` | `string` | `"100vh"` | Height of each panel as a CSS string |

**`<Panel>` props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | -- | Panel content |
| `className` | `string` | -- | CSS class |
| `style` | `CSSProperties` | -- | Inline styles (merged with default `100vw x 100vh` sizing) |

---

### `<Progress>`

A fixed scroll progress indicator. Supports bar, dots, and ring styles.

```tsx
import { Progress } from "react-kino";

{/* Simple top bar */}
<Progress />

{/* Ring indicator in the corner */}
<Progress type="ring" position="bottom" color="#10b981" ringSize={40} />

{/* Dot pagination on the right */}
<Progress type="dots" position="right" dotCount={8} color="#fff" />
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `"bar" \| "dots" \| "ring"` | `"bar"` | Visual style of the indicator |
| `position` | `"top" \| "bottom" \| "left" \| "right"` | `"top"` | Fixed position on screen |
| `color` | `string` | `"#3b82f6"` | Color of the progress fill / active dots / ring stroke |
| `trackColor` | `string` | `"transparent"` | Background / inactive color |
| `progress` | `number` | -- | Progress override (0-1). If omitted, reads page scroll progress |
| `dotCount` | `number` | `5` | Number of dots (only for `"dots"` type) |
| `ringSize` | `number` | `48` | Diameter in pixels (only for `"ring"` type) |
| `className` | `string` | -- | CSS class for the wrapper |

---

### `<VideoScroll>`

Scrubs through a video as the user scrolls -- like the AirPods Pro / iPhone product pages.

```tsx
import { VideoScroll } from "react-kino";

<VideoScroll src="/product.mp4" duration="400vh" poster="/poster.jpg">
  {(progress) => (
    <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center" }}>
      <h2 style={{ opacity: progress, color: "#fff", fontSize: "4rem" }}>
        Scroll to reveal
      </h2>
    </div>
  )}
</VideoScroll>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `src` | `string` | -- | URL of the video file (MP4 recommended, no audio needed) |
| `duration` | `string` | `"300vh"` | Scroll distance the video scrubbing spans |
| `pin` | `boolean` | `true` | Whether to pin the video while scrubbing |
| `poster` | `string` | -- | Poster image shown before the video loads |
| `children` | `ReactNode \| (progress: number) => ReactNode` | -- | Overlay content rendered on top of the video |
| `className` | `string` | -- | CSS class for the outer spacer |

---

### `<StickyHeader>`

A sticky navigation bar that transitions from transparent to a solid background with backdrop blur as the user scrolls past a threshold.

```tsx
import { StickyHeader } from "react-kino";

<StickyHeader threshold={40} background="rgba(0, 0, 0, 0.72)" blur>
  <div style={{ maxWidth: 980, margin: "0 auto", height: 48, display: "flex", alignItems: "center", justifyContent: "space-between", padding: "0 24px" }}>
    <span>My Site</span>
    <nav>
      <a href="#features">Features</a>
      <a href="#pricing">Pricing</a>
    </nav>
  </div>
</StickyHeader>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `threshold` | `number` | `80` | Scroll distance (px) before the header becomes solid |
| `background` | `string` | `"rgba(0,0,0,0.8)"` | Background color when scrolled past threshold |
| `blur` | `boolean` | `true` | Whether to apply backdrop blur when scrolled |
| `children` | `ReactNode` | -- | Header content |
| `className` | `string` | -- | CSS class |
| `style` | `CSSProperties` | -- | Inline styles |

---

### `<Marquee>`

An infinitely scrolling ticker. Items are automatically duplicated to create a seamless loop. Respects `prefers-reduced-motion` by falling back to a static flex layout.

```tsx
import { Marquee } from "react-kino";

<Marquee speed={30} direction="left" pauseOnHover>
  <span>React</span>
  <span>TypeScript</span>
  <span>Next.js</span>
  <span>Tailwind</span>
</Marquee>
```

| Prop | Type | Default | Description |
|-----
... [TRUNCATED]
```

### File: packages\scheduler\index.js
```js
/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

'use strict';

export * from './src/forks/Scheduler';

```

### File: packages\scheduler\package.json
```json
{
  "name": "scheduler",
  "version": "0.28.0",
  "description": "Cooperative scheduler for the browser environment.",
  "repository": {
    "type": "git",
    "url": "https://github.com/facebook/react.git",
    "directory": "packages/scheduler"
  },
  "license": "MIT",
  "keywords": [
    "react"
  ],
  "bugs": {
    "url": "https://github.com/facebook/react/issues"
  },
  "homepage": "https://react.dev/",
  "files": [
    "LICENSE",
    "README.md",
    "index.js",
    "index.native.js",
    "unstable_mock.js",
    "unstable_post_task.js",
    "cjs/"
  ]
}

```

### File: packages\scheduler\README.md
```md
# `scheduler`

This is a package for cooperative scheduling in a browser environment. It is currently used internally by React, but we plan to make it more generic.

The public API for this package is not yet finalized.

### Thanks

The React team thanks [Anton Podviaznikov](https://podviaznikov.com/) for donating the `scheduler` package name.

```

### File: packages\shared\package.json
```json
{
  "private": true,
  "name": "shared",
  "version": "0.0.0"
}

```

### File: packages\templates\package.json
```json
{
  "name": "@react-kino/templates",
  "version": "0.1.3",
  "description": "Pre-built full-page scroll experience templates for react-kino",
  "main": "./dist/index.js",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.js"
    },
    "./product-launch": {
      "types": "./dist/product-launch.d.ts",
      "import": "./dist/product-launch.mjs",
      "require": "./dist/product-launch.js"
    },
    "./case-study": {
      "types": "./dist/case-study.d.ts",
      "import": "./dist/case-study.mjs",
      "require": "./dist/case-study.js"
    },
    "./portfolio": {
      "types": "./dist/portfolio.d.ts",
      "import": "./dist/portfolio.mjs",
      "require": "./dist/portfolio.js"
    }
  },
  "files": [
    "dist",
    "README.md"
  ],
  "sideEffects": false,
  "scripts": {
    "build": "tsup && node scripts/add-use-client.mjs",
    "dev": "tsup --watch",
    "clean": "rm -rf dist",
    "typecheck": "tsc --noEmit",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "react-kino": "workspace:*"
  },
  "peerDependencies": {
    "react": ">=18.0.0",
    "react-dom": ">=18.0.0"
  },
  "devDependencies": {
    "@types/react": "^19",
    "react": "^19",
    "tsup": "^8",
    "typescript": "^5"
  },
  "author": "Bilal Tahir",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/btahir/react-kino.git",
    "directory": "packages/templates"
  },
  "homepage": "https://github.com/btahir/react-kino#readme",
  "bugs": {
    "url": "https://github.com/btahir/react-kino/issues"
  }
}

```

### File: packages\templates\README.md
```md
<h1 align="center">@react-kino/templates</h1>

<p align="center">
Pre-built, full-page cinematic scroll experiences for <a href="https://www.npmjs.com/package/react-kino">react-kino</a>.<br/>
Drop in a template, pass your content as props, ship.
</p>

---

## Installation

```bash
npm install @react-kino/templates react-kino
```

```bash
pnpm add @react-kino/templates react-kino
```

**Requirements:** React 18+, `react-kino` as a peer dependency.

---

## Templates

### `<ProductLaunch>`

Apple-style product launch page with a scroll-away hero, sticky nav, stat counters, horizontal feature panels, and a marquee ticker.

```tsx
import { ProductLaunch } from "@react-kino/templates/product-launch";

<ProductLaunch
  name="Acme Pro"
  tagline="The tool that changes everything."
  accentColor="#dc2626"
  navItems={[
    { label: "Features", href: "#features" },
    { label: "Pricing", href: "#pricing" },
  ]}
  stats={[
    { value: 10000, label: "Users", format: (n) => `${n.toLocaleString()}+` },
    { value: 99.9, label: "Uptime", format: (n) => `${n.toFixed(1)}%` },
  ]}
  features={[
    { title: "Tiny core", description: "Under 1 KB gzipped.", icon: "⚡" },
    { title: "GPU accelerated", description: "Compositor-only properties.", icon: "🚀" },
  ]}
/>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` | **required** | Product name (hero heading + sticky header) |
| `tagline` | `string` | **required** | Hero subtitle |
| `heroBackground` | `string` | dark gradient | CSS background for the hero |
| `accentColor` | `string` | `"#dc2626"` | Brand accent color used throughout |
| `stats` | `Array<{ value, label, format? }>` | 3 defaults | Animated counters section |
| `features` | `Array<{ title, description, icon? }>` | 3 defaults | Horizontal scroll feature panels |
| `navItems` | `Array<{ label, href? }>` | -- | Sticky header navigation links |
| `headerCtaText` | `string` | `"Get Started"` | CTA button text in sticky header |
| `headerCtaHref` | `string` | `"#"` | CTA button link |
| `showScrollHint` | `boolean` | `true` | Show scroll-down arrow on hero |
| `marqueeItems` | `string[]` | feature titles | Custom items for the ticker between features and CTA |

**Sections:** Sticky header -- Hero (scroll-away) -- Feature cards -- Stat counters -- Horizontal scroll features -- Marquee ticker -- CTA

---

### `<CaseStudy>`

Portfolio case study page with word-by-word overview reveal, smooth challenge/solution cards, result counters, and a results ticker.

```tsx
import { CaseStudy } from "@react-kino/templates/case-study";

<CaseStudy
  title="Redesigning the Future of Commerce"
  client="Acme Corp"
  year={2024}
  overview="We partnered with Acme Corp to reimagine their entire commerce platform from the ground up, delivering a system that scales to millions of transactions."
  challenge="The legacy platform couldn't handle peak traffic, leading to lost revenue during key shopping events."
  solution="A ground-up rebuild using edge computing and progressive rendering, cutting load times by 80%."
  results={[
    { metric: "Faster load time", value: 80, format: (n) => `${n}%` },
    { metric: "Revenue increase", value: 3.2, format: (n) => `${n}x` },
  ]}
  nextProject={{ title: "Project Atlas", href: "/work/atlas" }}
/>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | `string` | **required** | Project title (hero heading) |
| `client` | `string` | **required** | Client name (sticky header + hero subtitle) |
| `year` | `string \| number` | **required** | Project year |
| `heroImage` | `string` | -- | Hero background image URL |
| `overview` | `string` | **required** | Project overview (rendered word-by-word via TextReveal) |
| `challenge` | `string` | **required** | The challenge description |
| `solution` | `string` | **required** | The solution description |
| `results` | `Array<{ metric, value, format? }>` | `[]` | Animated result counters |
| `nextProject` | `{ title, href }` | -- | Link to the next project |
| `navItems` | `Array<{ label, href? }>` | -- | Sticky header navigation links |
| `showScrollHint` | `boolean` | `true` | Show scroll-down arrow on hero |
| `marqueeItems` | `string[]` | formatted results | Custom items for the results ticker |

**Sections:** Sticky header -- Hero (scroll-away) -- Overview (TextReveal) -- Challenge & Solution (ScrollTransform) -- Result counters -- Marquee ticker -- Next project

---

### `<Portfolio>`

Personal portfolio page with a scroll-away name/role hero, word-by-word bio, fluid project cards, skills marquee, and contact section.

```tsx
import { Portfolio } from "@react-kino/templates/portfolio";

<Portfolio
  name="Jane Smith"
  role="Design Engineer"
  bio="I craft interfaces that feel alive. Ten years of turning complex products into experiences people love."
  accentColor="#3b82f6"
  projects={[
    { title: "Project Alpha", description: "A design system for scale.", year: 2024, tags: ["React", "Design Systems"] },
    { title: "Project Beta", description: "Real-time collaboration tool.", year: 2023, tags: ["WebSocket", "Canvas"] },
  ]}
  skills={["React", "TypeScript", "Figma", "Three.js", "Motion Design"]}
  contactEmail="jane@example.com"
/>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` | **required** | Your name (hero heading + sticky header) |
| `role` | `string` | **required** | Your role/title (hero subtitle) |
| `bio` | `string` | **required** | Bio text (rendered word-by-word via TextReveal) |
| `accentColor` | `string` | `"#3b82f6"` | Accent color for highlights and tags |
| `projects` | `Array<{ title, description, year, tags? }>` | `[]` | Project cards with scroll-driven entrance |
| `skills` | `string[]` | `[]` | Skills shown in horizontal scroll panels |
| `contactEmail` | `string` | -- | Contact email shown in header and footer |
| `navItems` | `Array<{ label, href? }>` | -- | Sticky header navigation links |
| `showScrollHint` | `boolean` | `true` | Show scroll-down arrow on hero |
| `marqueeItems` | `string[]` | skills list | Custom items for the skills ticker |

**Sections:** Sticky header -- Hero (scroll-away) -- Bio (TextReveal) -- Projects (ScrollTransform) -- Skills marquee -- Skills horizontal scroll -- Contact

---

## What's included

Every template is built with these react-kino components:

| Component | Used for |
|-----------|----------|
| `StickyHeader` | Transparent-to-solid navigation bar |
| `ScrollTransform` | Hero scroll-away effect, fluid card entrances |
| `TextReveal` | Word-by-word text reveal on scroll |
| `Marquee` | Infinitely scrolling ticker |
| `Scene` | Pinned scroll sections with progress tracking |
| `Reveal` | Scroll-triggered entrance animations |
| `Parallax` | Background depth layers |
| `Counter` | Animated stat numbers |
| `HorizontalScroll` / `Panel` | Horizontal feature/skill panels |
| `Progress` | Fixed scroll progress bar |

---

## Tree-shaking

Each template has its own entry point. Import only what you use:

```tsx
// Only bundles ProductLaunch (not CaseStudy or Portfolio)
import { ProductLaunch } from "@react-kino/templates/product-launch";
```

Or import everything from the barrel:

```tsx
import { ProductLaunch, CaseStudy, Portfolio } from "@react-kino/templates";
```

---

## SSR / Next.js

Templates are SSR-safe and include `"use client"` directives. Use them directly in Next.js App Router pages:

```tsx
// app/page.tsx
"use client";
import { ProductLaunch } from "@react-kino/templates/product-launch";

export default function Page() {
  return <ProductLaunch name="My Product" tagline="Ship faster." />;
}
```

---

## License

MIT

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
