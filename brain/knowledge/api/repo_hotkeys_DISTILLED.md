---
id: repo-hotkeys
type: api
owner: OA
registered_at: 2026-04-05T16:57:44.295881
tags: ["auto-cloned", "JavaScript", "React", "Web Development", "Keyboard Shortcuts", "oa-assimilated"]
---

# hotkeys

## Assimilation Report
TanStack Hotkeys is a library providing type-safe, cross-platform keyboard shortcut handling for web applications. It offers flexible binding methods (template strings or parsed objects) and utilities for managing complex key interactions like sequences and state tracking.

## Application for OmniClaw
OmniClaw can integrate this API to create a 'Contextual Hotkey Manager' agent. Instead of global hotkeys, the agent would analyze the current UI component (e.g., a code editor, a form, a data table) and dynamically load a specific, scoped hotkey map from the TanStack Hotkeys API. This allows OmniClaw to provide highly specialized, context-aware shortcuts (e.g., 'Ctrl+Shift+Enter' to run a specific query in the current data view) without conflicting with global application shortcuts, significantly enhancing the user's interaction layer.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "root",
  "private": true,
  "repository": {
    "type": "git",
    "url": "git+https://github.com/TanStack/hotkeys.git"
  },
  "packageManager": "pnpm@10.33.0",
  "type": "module",
  "scripts": {
    "build": "nx affected --skip-nx-cache --targets=build --exclude=examples/** && size-limit",
    "build:all": "nx run-many --targets=build --exclude=examples/**",
    "build:core": "nx run-many --targets=build --projects=packages/hotkeys",
    "changeset": "changeset",
    "changeset:publish": "changeset publish",
    "changeset:version": "changeset version && pnpm install --no-frozen-lockfile && pnpm format",
    "clean": "find . -name 'dist' -type d -prune -exec rm -rf {} +",
    "clean:node_modules": "find . -name 'node_modules' -type d -prune -exec rm -rf {} +",
    "clean:all": "pnpm run clean && pnpm run clean:node_modules",
    "copy:readme": "cp README.md packages/hotkeys/README.md && cp README.md packages/hotkeys-devtools/README.md && cp README.md packages/angular-hotkeys/README.md && cp README.md packages/react-hotkeys/README.md && cp README.md packages/react-hotkeys-devtools/README.md && cp README.md packages/preact-hotkeys/README.md && cp README.md packages/preact-hotkeys-devtools/README.md && cp README.md packages/solid-hotkeys/README.md && cp README.md packages/solid-hotkeys-devtools/README.md && cp README.md packages/vue-hotkeys/README.md && cp README.md packages/vue-hotkeys-devtools/README.md && cp README.md packages/lit-hotkeys/README.md && cp README.md packages/svelte-hotkeys/README.md",
    "dev": "pnpm run watch",
    "format": "prettier --experimental-cli --ignore-unknown '**/*' --write",
    "generate-docs": "node scripts/generate-docs.ts && pnpm run copy:readme",
    "lint": "nx affected --target=lint --exclude=examples/**",
    "lint:all": "pnpm run test:eslint && pnpm -r --filter \"./examples/**\" --if-present lint",
    "lint:fix": "nx affected --target=lint:fix --exclude=examples/**",
    "lint:fix:all": "nx run-many --targets=lint:fix",
    "test": "pnpm run test:ci",
    "test:ci": "pnpm run lint:all && nx run-many --targets=test:sherif,test:knip,test:docs,test:lib,test:types,build",
    "test:docs": "node scripts/verify-links.ts",
    "test:eslint": "nx affected --target=test:eslint --exclude=examples/**",
    "test:knip": "knip",
    "test:lib": "nx affected --targets=test:lib --exclude=examples/**",
    "test:lib:dev": "pnpm test:lib && nx watch --all -- pnpm test:lib",
    "test:pr": "pnpm run lint:all && nx affected --targets=test:sherif,test:knip,test:docs,test:lib,test:types,build",
    "test:sherif": "sherif",
    "test:types": "nx affected --targets=test:types --exclude=examples/**",
    "watch": "pnpm run build:all && nx watch --all -- pnpm run build:all"
  },
  "size-limit": [
    {
      "path": "packages/hotkeys/dist/index.js",
      "limit": "8 KB"
    }
  ],
  "nx": {
    "includedScripts": [
      "test:docs",
      "test:knip",
      "test:sherif"
    ]
  },
  "pnpm": {
    "overrides": {
      "rolldown": "1.0.0-rc.12"
    }
  },
  "devDependencies": {
    "@changesets/cli": "^2.30.0",
    "@faker-js/faker": "^10.4.0",
    "@size-limit/preset-small-lib": "^12.0.1",
    "@svitejs/changesets-changelog-github-compact": "^1.2.0",
    "@tanstack/eslint-config": "0.4.0",
    "@tanstack/typedoc-config": "0.3.3",
    "@testing-library/jest-dom": "^6.9.1",
    "@types/node": "^25.5.0",
    "eslint": "^10.1.0",
    "eslint-plugin-unused-imports": "^4.4.1",
    "happy-dom": "^20.8.9",
    "knip": "^6.1.0",
    "markdown-link-extractor": "^4.0.3",
    "nx": "^22.6.3",
    "premove": "^4.0.0",
    "prettier": "^3.8.1",
    "prettier-plugin-svelte": "^3.5.1",
    "publint": "^0.3.18",
    "sherif": "^1.11.0",
    "size-limit": "^12.0.1",
    "tinyglobby": "^0.2.15",
    "tsdown": "^0.21.7",
    "typescript": "6.0.2",
    "vitest": "^4.1.2"
  },
  "overrides": {
    "@tanstack/angular-hotkeys": "workspace:*",
    "@tanstack/hotkeys": "workspace:*",
    "@tanstack/hotkeys-devtools": "workspace:*",
    "@tanstack/lit-hotkeys": "workspace:*",
    "@tanstack/lit-hotkeys-devtools": "workspace:*",
    "@tanstack/preact-hotkeys": "workspace:*",
    "@tanstack/preact-hotkeys-devtools": "workspace:*",
    "@tanstack/react-hotkeys": "workspace:*",
    "@tanstack/react-hotkeys-devtools": "workspace:*",
    "@tanstack/solid-hotkeys": "workspace:*",
    "@tanstack/solid-hotkeys-devtools": "workspace:*",
    "@tanstack/svelte-hotkeys": "workspace:*",
    "@tanstack/vue-hotkeys": "workspace:*",
    "@tanstack/vue-hotkeys-devtools": "workspace:*"
  },
  "volta": {
    "node": "24.14.1"
  }
}

```

### File: README.md
```md
<div align="center">
  <img src="./media/header_hotkeys.png" alt="TanStack Hotkeys" />
</div>

<br />

<div align="center">
	<a href="https://www.npmjs.com/package/@tanstack/hotkeys" target="\_parent">
	  <img alt="" src="https://img.shields.io/npm/dm/@tanstack/hotkeys.svg" alt="npm downloads" />
	</a>
	<a href="https://github.com/TanStack/hotkeys" target="\_parent">
	  <img alt="" src="https://img.shields.io/github/stars/TanStack/hotkeys.svg?style=social&label=Star" alt="GitHub stars" />
	</a>
	<a href="https://bundlephobia.com/result?p=@tanstack/react-hotkeys@latest" target="\_parent">
	  <img alt="" src="https://badgen.net/bundlephobia/minzip/@tanstack/react-hotkeys@latest" alt="Bundle size" />
	</a>
</div>

<div align="center">
	<a href="#badge">
	  <img alt="semantic-release" src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg">
	</a>
	<a href="#badge">
	  <img src="https://img.shields.io/github/v/release/tanstack/hotkeys" alt="Release"/>
	</a>
	<a href="https://twitter.com/tan_stack">
	  <img src="https://img.shields.io/twitter/follow/tan_stack.svg?style=social" alt="Follow @TanStack"/>
	</a>
</div>

<div align="center">

### [Become a Sponsor!](https://github.com/sponsors/tannerlinsley/)

</div>

# TanStack Hotkeys

> [!NOTE]
> TanStack Hotkeys is alpha. We are actively developing the library and are open to feedback and contributions.

Type-safe keyboard shortcuts for the web. Template-string bindings, parsed objects, a cross-platform `Mod` key, a singleton Hotkey Manager, and utilities for cheatsheet UIs—built to stay SSR-friendly.

- Type-safe bindings — template strings (`Mod+Shift+S`, `Escape`) or parsed objects for full control
- Flexible options — `keydown`/`keyup`, `preventDefault`, `stopPropagation`, conditional enabled, `requireReset`
- Cross-platform Mod — maps to Cmd on macOS and Ctrl on Windows/Linux
- Batteries included — validation + matching, sequences (Vim-style), key-state tracking, recorder UI helpers, framework adapters, and devtools

### <a href="https://tanstack.com/hotkeys">Read the docs →</a>

<br />

> [!NOTE]
> You may know **TanStack Hotkeys** by our adapter names, too!
>
> - [**React Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/react/react-hotkeys)
> - [**Preact Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/preact/preact-hotkeys)
> - [**Solid Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/solid/reference)
> - [**Angular Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/angular/reference)
> - [**Vue Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/vue/reference)
> - [**Lit Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/lit/reference)
> - [**Svelte Hotkeys**](https://tanstack.com/hotkeys/latest/docs/framework/svelte/reference)

## Get Involved

- We welcome issues and pull requests!
- Participate in [GitHub discussions](https://github.com/TanStack/hotkeys/discussions)
- Chat with the community on [Discord](https://discord.com/invite/WrRKjPJ)
- See [CONTRIBUTING.md](./CONTRIBUTING.md) for setup instructions

## Partners

<div align="center">

<table align="center">
  <tr>
    <td>
      <a href="https://www.coderabbit.ai/?via=tanstack&dub_id=aCcEEdAOqqutX6OS" >
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/coderabbit-dark-D643Zkrv.svg" height="40" />
          <source media="(prefers-color-scheme: light)" srcset="https://tanstack.com/assets/coderabbit-light-CIzGLYU_.svg" height="40" />
          <img src="https://tanstack.com/assets/coderabbit-light-DVMJ2jHi.svg" height="40" alt="CodeRabbit" />
        </picture>
      </a>
    </td>
    <td>
      <a href="https://www.cloudflare.com?utm_source=tanstack">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://tanstack.com/assets/cloudflare-white-Co-Tyjbl.svg" height="60" />
          <source media="(prefers-color-scheme: light)" srcset="https://tanstack.com/assets/cloudflare-black-6Ojsn8yh.svg" height="60" />
          <img src="https://tanstack.com/assets/cloudflare-black-CPufaW0B.svg" height="60" alt="Cloudflare" />
        </picture>
      </a>
    </td>
  </tr>
</table>

<div align="center">
<img src="media/partner_logo.svg" alt="Keys & you?" height="65">
<p>
We're looking for TanStack Hotkeys Partners to join our mission! Partner with us to push the boundaries of TanStack Hotkeys and build amazing things together.
</p>
<a href="mailto:partners@tanstack.com?subject=TanStack Hotkeys Partnership"><b>LET'S CHAT</b></a>
</div>

</div>

## Explore the TanStack Ecosystem

- <a href="https://github.com/tanstack/config"><b>TanStack Config</b></a> – Tooling for JS/TS packages
- <a href="https://github.com/tanstack/db"><b>TanStack DB</b></a> – Reactive sync client store
- <a href="https://github.com/tanstack/devtools"><b>TanStack DevTools</b></a> – Unified devtools panel
- <a href="https://github.com/tanstack/form"><b>TanStack Form</b></a> – Type‑safe form state
- <a href="https://github.com/tanstack/hotkeys"><b>TanStack Hotkeys</b></a> – Type‑safe keyboard shortcuts
- <a href="https://github.com/tanstack/query"><b>TanStack Query</b></a> – Async state & caching
- <a href="https://github.com/tanstack/ranger"><b>TanStack Ranger</b></a> – Range & slider primitives
- <a href="https://github.com/tanstack/router"><b>TanStack Router</b></a> – Type‑safe routing, caching & URL state
- <a href="https://github.com/tanstack/start"><b>TanStack Start</b></a> – Full‑stack SSR & streaming
- <a href="https://github.com/tanstack/store"><b>TanStack Store</b></a> – Reactive data store
- <a href="https://github.com/tanstack/table"><b>TanStack Table</b></a> – Headless datagrids
- <a href="https://github.com/tanstack/virtual"><b>TanStack Virtual</b></a> – Virtualized rendering

… and more at <a href="https://tanstack.com"><b>TanStack.com »</b></a>

```

### File: .coderabbit.yaml
```yaml
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
# Path filters: mirror .cursorignore where noted; other entries are explicit exclusions.
language: 'en-US'
early_access: false
reviews:
  profile: 'chill'
  request_changes_workflow: false
  high_level_summary: true
  poem: true
  review_status: true
  review_details: false
  auto_review:
    enabled: true
    drafts: false
  path_filters:
    # Generated API reference (matches .cursorignore)
    - '!docs/**/reference/**'
    # Lock files
    - '!**/package-lock.json'
    - '!**/yarn.lock'
    - '!**/pnpm-lock.yaml'
    - '!**/bun.lockb'
    - '!**/*.lock'
chat:
  auto_reply: true

```

### File: CODE_OF_CONDUCT.md
```md
---
title: Code of Conduct
id: code-of-conduct
---

# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

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
reported by contacting the project team at TANNERLINSLEY@GMAIL.COM. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq

```

### File: CONTRIBUTING.md
```md
---
title: Contributing
id: contributing
---

# Contributing

## Questions

If you have questions about implementation details, help or support, then please use our dedicated community forum at [Github Discussions](https://github.com/tanstack/hotkeys/discussions) **PLEASE NOTE:** If you choose to instead open an issue for your question, your issue will be immediately closed and redirected to the forum.

## Reporting Issues

If you have found what you think is a bug, please [file an issue](https://github.com/tanstack/hotkeys/issues/new). **PLEASE NOTE:** Issues that are identified as implementation questions or non-issues will be immediately closed and redirected to [Github Discussions](https://github.com/tanstack/hotkeys/discussions)

## Suggesting new features

If you are here to suggest a feature, first create an issue if it does not already exist. From there, we will discuss use-cases for the feature and then finally discuss how it could be implemented.

## Development

Before proceeding with development, ensure you match one of the following criteria:

- Fixing a small bug
- Fixing a larger issue that has been previously discussed and agreed-upon by maintainers
- Adding a new feature that has been previously discussed and agreed-upon by maintainers

## Development Workflow

- Fork this repository, we prefer the `feat-*` branch name style
- Ensure you have `pnpm` installed
- Install projects dependencies and linkages by running `pnpm install`
- Auto-build and auto-test files as you edit by running `pnpm dev`
- Implement your changes and tests
- To run examples, follow their individual directions. Usually this includes:
  - cd into the example directory
  - Do NOT install dependencies again or do any linking. Nx already handles this for you. Only run install from the project root.
  - Starting the dev server with `pnpm dev` or `pnpm start` (from the example directory)
- To test in your own projects:
  - Build/watch for changes with `pnpm build`/`pnpm dev`
- Document your changes in the appropriate documentation website markdown pages
- Run `pnpm test` to ensure all tests pass before committing
- Create a changeset (changelog entry) for your changes by running `pnpm changeset`
- Commit your work and open a pull request
- Submit PR for review

## Adding a new example

- Clone an existing example into the appropriate `examples` directory
- Name it the example name in kebab-case
- Update the new example's package.json to match the new example name and any other details
- Check dependencies for unused packages
- Install any additional packages to the example that you may need
- Update the docs/config.json file to include the new example in the navigation sidebar
- Commit the example eg. `docs: Add example-name`

```

### File: eslint.config.js
```js
// @ts-check

// @ts-ignore Needed due to moduleResolution Node vs Bundler
import { tanstackConfig } from '@tanstack/eslint-config'
import unusedImports from 'eslint-plugin-unused-imports'

/** @type {import('eslint').Linter.Config[]} */
const config = [
  ...tanstackConfig,
  {
    name: 'tanstack/temp',
    plugins: {
      'unused-imports': unusedImports,
    },
    rules: {
      'no-case-declarations': 'off',
      'no-shadow': 'off',
      'unused-imports/no-unused-imports': 'warn',
      'pnpm/enforce-catalog': 'off',
      'pnpm/json-enforce-catalog': 'off',
    },
  },
]

export default config

```

### File: knip.json
```json
{
  "$schema": "https://unpkg.com/knip@5/schema.json",
  "ignoreDependencies": ["@faker-js/faker"],
  "ignoreWorkspaces": ["examples/**"],
  "workspaces": {
    "packages/react-hotkeys": {
      "ignore": []
    }
  }
}

```

### File: nx.json
```json
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "defaultBase": "main",
  "nxCloudId": "69c86659c7b8022e1c5ead91",
  "useInferencePlugins": false,
  "parallel": 5,
  "tui": {
    "enabled": false
  },
  "namedInputs": {
    "sharedGlobals": [
      "{workspaceRoot}/.nvmrc",
      "{workspaceRoot}/package.json",
      "{workspaceRoot}/tsconfig.json"
    ],
    "default": [
      "sharedGlobals",
      "{projectRoot}/**/*",
      "!{projectRoot}/**/*.md"
    ],
    "production": [
      "default",
      "!{projectRoot}/tests/**/*",
      "!{projectRoot}/eslint.config.js"
    ]
  },
  "targetDefaults": {
    "test:lib": {
      "cache": true,
      "dependsOn": ["^build"],
      "inputs": ["default", "^production"],
      "outputs": ["{projectRoot}/coverage"]
    },
    "lint": {
      "cache": true,
      "inputs": ["default", "{workspaceRoot}/eslint.config.js"]
    },
    "lint:fix": {
      "cache": true,
      "inputs": ["default", "{workspaceRoot}/eslint.config.js"]
    },
    "test:eslint": {
      "cache": true,
      "dependsOn": ["^build"],
      "inputs": ["default", "^production", "{workspaceRoot}/eslint.config.js"]
    },
    "test:types": {
      "cache": true,
      "dependsOn": ["^build"],
      "inputs": ["default", "^production"]
    },
    "build": {
      "cache": true,
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"],
      "outputs": ["{projectRoot}/build", "{projectRoot}/dist"]
    },
    "test:docs": {
      "cache": true,
      "inputs": ["{workspaceRoot}/docs/**/*"]
    },
    "test:knip": {
      "cache": true,
      "inputs": ["{workspaceRoot}/**/*"]
    },
    "test:sherif": {
      "cache": true,
      "inputs": ["{workspaceRoot}/**/package.json"]
    }
  },
  "analytics": true
}

```

### File: pnpm-workspace.yaml
```yaml
cleanupUnusedCatalogs: true
linkWorkspacePackages: true
preferWorkspacePackages: true

packages:
  - 'examples/**/*'
  - 'packages/*'
onlyBuiltDependencies:
  - esbuild

```

### File: prettier.config.js
```js
// @ts-check

/** @type {import('prettier').Config} */
const config = {
  semi: false,
  singleQuote: true,
  trailingComma: 'all',
  plugins: ['prettier-plugin-svelte'],
  overrides: [{ files: '*.svelte', options: { parser: 'svelte' } }],
}

export default config

```

### File: tsconfig.json
```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "compilerOptions": {
    "allowJs": true,
    "allowSyntheticDefaultImports": true,
    "allowUnreachableCode": false,
    "allowUnusedLabels": false,
    "checkJs": true,
    "declaration": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,
    "lib": ["DOM", "DOM.Iterable", "ES2022"],
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "noEmit": true,
    "noImplicitReturns": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "strict": true,
    "target": "ES2020",
    "noErrorTruncation": true
  },
  "include": ["scripts", "*.config.*", "vitest.workspace.ts"]
}

```

### File: vitest.workspace.ts
```ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    projects: [
      './packages/hotkeys-devtools/vitest.config.ts',
      './packages/hotkeys/vitest.config.ts',
      './packages/preact-hotkeys-devtools/vitest.config.ts',
      './packages/preact-hotkeys/vitest.config.ts',
      './packages/react-hotkeys-devtools/vitest.config.ts',
      './packages/react-hotkeys/vitest.config.ts',
      './packages/solid-hotkeys-devtools/vitest.config.ts',
      './packages/solid-hotkeys/vitest.config.ts',
      './packages/angular-hotkeys/vitest.config.ts',
      './packages/vue-hotkeys/vitest.config.ts',
      './packages/svelte-hotkeys/vitest.config.ts',
    ],
  },
})

```

### File: .github\pull_request_template.md
```md
## 🎯 Changes

<!-- What changes are made in this PR? Describe the change and its motivation. -->

## ✅ Checklist

- [ ] I have followed the steps in the [Contributing guide](https://github.com/TanStack/hotkeys/blob/main/CONTRIBUTING.md).
- [ ] I have tested this code locally with `pnpm run test:pr`.

## 🚀 Release Impact

- [ ] This change affects published code, and I have generated a [changeset](https://github.com/changesets/changesets/blob/main/docs/adding-a-changeset.md).
- [ ] This change is docs/CI/dev-only (no release).

```

### File: .github\renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "configMigration": true,
  "extends": [
    "config:recommended",
    "group:allNonMajor",
    "schedule:weekly",
    ":approveMajorUpdates",
    ":automergeMinor",
    ":disablePeerDependencies",
    ":maintainLockFilesMonthly",
    ":semanticCommits",
    ":semanticCommitTypeAll(chore)"
  ],
  "ignorePresets": [":ignoreModulesAndTests"],
  "labels": ["dependencies"],
  "rangeStrategy": "bump",
  "postUpdateOptions": ["pnpmDedupe"],
  "ignoreDeps": ["@types/node", "node"]
}

```

