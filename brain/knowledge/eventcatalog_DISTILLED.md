---
id: eventcatalog
type: knowledge
owner: OA_Triage
---
# eventcatalog
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "eventcatalog-monorepo",
  "private": true,
  "license": "MIT",
  "scripts": {
    "build:bin": "turbo run build:bin",
    "build": "turbo run build",
    "test": "turbo run test",
    "test:ci": "turbo run test:ci",
    "format": "turbo run format",
    "format:diff": "turbo run format:diff",
    "start:playground": "pnpm --filter @eventcatalog/dsl-playground run dev",
    "start:dsl-docs": "pnpm --filter @eventcatalog/language-server run docs:dev",
    "build:dsl-docs": "pnpm --filter @eventcatalog/sdk run build && pnpm --filter @eventcatalog/language-server run build && pnpm --filter @eventcatalog/language-server run docs:build",
    "start:catalog": "pnpm --filter @eventcatalog/core run start:catalog",
    "export:catalog": "pnpm --filter @eventcatalog/core run export:catalog",
    "preview:catalog": "pnpm --filter @eventcatalog/core run preview:catalog",
    "start:catalog:server": "pnpm --filter @eventcatalog/core run start:catalog:server",
    "verify-build:catalog": "pnpm --filter @eventcatalog/core run verify-build:catalog",
    "changeset": "changeset",
    "release": "changeset publish"
  },
  "devDependencies": {
    "@changesets/cli": "^2.27.5",
    "prettier-plugin-astro": "^0.14.1",
    "turbo": "^2.8.4"
  },
  "pnpm": {
    "overrides": {
      "prismjs": ">=1.30.0"
    }
  },
  "packageManager": "pnpm@10.23.0+sha512.21c4e5698002ade97e4efe8b8b4a89a8de3c85a37919f957e7a0f30f38fbc5bbdd05980ffe29179b2fb6e6e691242e098d945d1601772cad0fef5fb6411e2a4b",
  "dependencies": {}
}

```

### File: README.md
```md
<div align="center">

<img src="./images/banner.png" alt="EventCatalog overview" width="800" />

## The architecture catalog for distributed systems 

Discover your domains, services, events, and schemas — with AI-powered discovery, interactive visualizations, and 15+ generators for Kafka, EventBridge, RabbitMQ, and more.

[![main](https://github.com/event-catalog/eventcatalog/actions/workflows/verify-build.yml/badge.svg)](https://github.com/event-catalog/eventcatalog/actions/workflows/verify-build.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/event-catalog/eventcatalog/blob/main/LICENSE)
[![npm version](https://badge.fury.io/js/@eventcatalog%2Fcore.svg)](https://badge.fury.io/js/@eventcatalog/core)
[![All Contributors](https://img.shields.io/badge/all_contributors-69-orange.svg?style=flat-square)](#contributors-)

**31,000+ catalogs created**


</div>

<br/>

<p align="center">
  <img src="./images/overview-demo.gif" alt="EventCatalog overview" width="800" />
</p>

[Documentation](https://www.eventcatalog.dev/docs) | [Live Demo](https://demo.eventcatalog.dev) | [Discord](https://discord.gg/3rjaZMmrAm)


<br/>

## Get started in seconds

```bash
npx @eventcatalog/create-eventcatalog@latest my-catalog
```

That's it. Open `http://localhost:3000` and start documenting your architecture.

Looking for a guided walkthrough? Check out the [Getting Started](https://www.eventcatalog.dev/docs/development/getting-started/installation) guide.

---

## Core Features

### Visualise your architecture

Interactive node graphs that map your entire system — services, events, commands, queries, domains, and how they connect.

<p align="center">
  <img src="./images/visualizer-demo.gif" alt="Architecture visualiser" width="800" />
</p>

### AI-powered discovery

Ask questions about your architecture and business in natural language. The built-in AI chat and MCP server let you and your tools explore your catalog.

<p align="center">
  <img src="./images/ai-demo.gif" alt="AI-powered discovery" width="800" />
</p>

### Schema explorer

Quickly find any schema across your catalog — OpenAPI, AsyncAPI, Protobuf, JSON Schema, Avro, and more. All in one searchable place.

<p align="center">
  <img src="./images/schema-explorer-demo.gif" alt="Schema explorer" width="800" />
</p>

### Schema fields

Filter and find any property on any field across your entire catalog. See how fields are used across services and messages.

<p align="center">
  <img src="./images/schema-fields-demo.gif" alt="Schema fields explorer" width="800" />
</p>

### Bring your own docs

Attach architecture decision records, runbooks, and any custom documentation to your domains, services, and teams. Version them alongside your architecture.

<p align="center">
  <img src="./images/bring-your-own-docs.gif" alt="Bring your own docs" width="800" />
</p>

### Document business flows

Tell the end-to-end story of your business workflows. Reference the services and messages you already have to build a higher-level picture of how everything fits together.

<p align="center">
  <img src="./images/flow-demo.gif" alt="Business flow documentation" width="800" />
</p>

### And much more...

- **Version your resources** — Full semantic versioning for events, commands, services, and more
- **15+ generators** — Auto-generate from AsyncAPI, OpenAPI, Kafka, Confluent, AWS EventBridge, and more
- **Customizable** — Themes, custom MDX components, and configurable layouts
- **Enterprise ready** — OAuth2, RBAC, schema governance, breaking change detection

---

## Demos

See EventCatalog powering real-world architectures:

| | | |
|---|---|---|
| [**E-Commerce**](https://demo.eventcatalog.dev/) | [**Finance**](https://eventcatalog-examples-finance.vercel.app/) | [**Healthcare**](https://eventcatalog-examples-healthcare.vercel.app/) |
| [**SaaS**](https://eventcatalog-examples-saas.vercel.app/) | | |

---

## Packages

| Package | Description |
|---------|-------------|
| [@eventcatalog/core](./packages/core) | Main catalog application (Astro + React) |
| [@eventcatalog/sdk](./packages/sdk) | Node.js SDK for programmatic catalog management |
| [@eventcatalog/create-eventcatalog](./packages/create-eventcatalog) | CLI scaffolding tool |
| [@eventcatalog/visualiser](./packages/visualiser) | Standalone React visualiser component |
| [@eventcatalog/dsl-playground](./packages/playground) | Browser-based DSL playground |

---

## Documentation

Visit the [official docs](https://www.eventcatalog.dev/docs/development/getting-started) to learn more.

---

## Support

Need help? Join the [EventCatalog Discord](https://discord.gg/3rjaZMmrAm).

---

## Contributing

We welcome contributions! See the [contributing guidelines](https://eventcatalog.dev/docs/contributing/overview) to get started.

---

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://boyney.io/"><img src="https://avatars.githubusercontent.com/u/3268013?v=4?s=100" width="100px;" alt="David Boyne"/><br /><sub><b>David Boyne</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=boyney123" title="Code">💻</a> <a href="#content-boyney123" title="Content">🖋</a> <a href="#design-boyney123" title="Design">🎨</a> <a href="#example-boyney123" title="Examples">💡</a> <a href="#ideas-boyney123" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=boyney123" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://otbe.io"><img src="https://avatars.githubusercontent.com/u/3391052?v=4?s=100" width="100px;" alt="Benjamin Otto"/><br /><sub><b>Benjamin Otto</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=otbe" title="Code">💻</a> <a href="#ideas-otbe" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=otbe" title="Documentation">📖</a> <a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Aotbe" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pongz79"><img src="https://avatars.githubusercontent.com/u/250872?v=4?s=100" width="100px;" alt="Tiago Oliveira"/><br /><sub><b>Tiago Oliveira</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=pongz79" title="Documentation">📖</a> <a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Apongz79" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.bigjump.com/"><img src="https://avatars.githubusercontent.com/u/11387911?v=4?s=100" width="100px;" alt="Jay McGuinness"/><br /><sub><b>Jay McGuinness</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=jaymcguinness" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/davidkpiano"><img src="https://avatars.githubusercontent.com/u/1093738?v=4?s=100" width="100px;" alt="David Khourshid"/><br /><sub><b>David Khourshid</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=davidkpiano" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/thim81"><img src="https://avatars.githubusercontent.com/u/952446?v=4?s=100" width="100px;" alt="thim81"/><br /><sub><b>thim81</b></sub></a><br /><a href="#ideas-thim81" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Athim81" title="Bug reports">🐛</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=thim81" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Muthuveerappanv"><img src="https://avatars.githubusercontent.com/u/33663725?v=4?s=100" width="100px;" alt="Muthu"/><br /><sub><b>Muthu</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3AMuthuveerappanv" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tavelli"><img src="https://avatars.githubusercontent.com/u/484951?v=4?s=100" width="100px;" alt="Dan Tavelli"/><br /><sub><b>Dan Tavelli</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=tavelli" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/steppi91"><img src="https://avatars.githubusercontent.com/u/25939641?v=4?s=100" width="100px;" alt="steppi91"/><br /><sub><b>steppi91</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=steppi91" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://twitter.com/PipoPeperoni"><img src="https://avatars.githubusercontent.com/u/1152805?v=4?s=100" width="100px;" alt="Donald Pipowitch"/><br /><sub><b>Donald Pipowitch</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Adonaldpipowitch" title="Bug reports">🐛</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=donaldpipowitch" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://unravelled.dev"><img src="https://avatars.githubusercontent.com/u/2233210?v=4?s=100" width="100px;" alt="Ken"/><br /><sub><b>Ken</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=kzhen" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://rtoro.cl"><img src="https://avatars.githubusercontent.com/u/5186897?v=4?s=100" width="100px;" alt="Rodolfo Toro"/><br /><sub><b>Rodolfo Toro</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=rtoro" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://blog.hackedbrain.com"><img src="https://avatars.githubusercontent.com/u/284152?v=4?s=100" width="100px;" alt="Drew Marsh"/><br /><sub><b>Drew Marsh</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=drub0y" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dpwdec"><img src="https://avatars.githubusercontent.com/u/51292634?v=4?s=100" width="100px;" alt="Dec Kolakowski"/><br /><sub><b>Dec Kolakowski</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=dpwdec" title="Code">💻</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=dpwdec" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dytyniuk"><img src="https://avatars.githubusercontent.com/u/1890615?v=4?s=100" width="100px;" alt="Yevhenii Dytyniuk"/><br /><sub><b>Yevhenii Dytyniuk</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=dytyniuk" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lcsbltm"><img src="https://avatars.githubusercontent.com/u/25868958?v=4?s=100" width="100px;" alt="lcsbltm"/><br /><sub><b>lcsbltm</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=lcsbltm" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://matt.martz.codes"><img src="https://avatars.githubusercontent.com/u/978362?v=4?s=100" width="100px;" alt="Matt Martz"/><br /><sub><b>Matt Martz</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=martzcodes" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/michelgrootjans"><img src="https://avatars.githubusercontent.com/u/345770?v=4?s=100" width="100px;" alt="Michel Grootjans"/><br /><sub><b>Michel Grootjans</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=michelgrootjans" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/arturoabruzzini"><img src="https://avatars.githubusercontent.com/u/17528406?v=4?s=100" width="100px;" alt="Arturo Abruzzini"/><br /><sub><b>Arturo Abruzzini</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=arturoabruzzini" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/adlecluse"><img src="https://avatars.githubusercontent.com/u/13390934?v=4?s=100" width="100px;" alt="Ad L'Ecluse"/><br /><sub><b>Ad L'Ecluse</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=adlecluse" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rafaelrenanpacheco"><img src="https://avatars.githubusercontent.com/u/12160864?v=4?s=100" width="100px;" alt="Rafael Renan Pacheco"/><br /><sub><b>Rafael Renan Pacheco</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=rafaelrenanpacheco" title="Code">💻</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=rafaelrenanpacheco" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://ldiego73.github.io/"><img src="https://avatars.githubusercontent.com/u/394222?v=4?s=100" width="100px;" alt="Luis Diego"/><br /><sub><b>Luis Diego</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=ldiego73" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/danielruf/"><img src="https://avatars.githubusercontent.com/u/827205?v=4?s=100" width="100px;" alt="Daniel Ruf"/><br /><sub><b>Daniel Ruf</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=DanielRuf" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/frenkan"><img src="https://avatars.githubusercontent.com/u/859840?v=4?s=100" width="100px;" alt="Fredrik Johansson"/><br /><sub><b>Fredrik Johansson</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=frenkan" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://gaddam1987.github.io/"><img src="https://avatars.githubusercontent.com/u/2576375?v=4?s=100" width="100px;" alt="Naresh Kumar Reddy Gaddam"/><br /><su
... [TRUNCATED]
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

### File: packages\cli\package.json
```json
{
  "name": "@eventcatalog/cli",
  "version": "0.5.11",
  "description": "CLI for EventCatalog",
  "scripts": {
    "build": "tsup",
    "build:bin": "tsup",
    "test": "vitest --run",
    "test:ci": "vitest --run",
    "bench:import-export": "node src/test/bench/import-export.benchmark.js",
    "format": "prettier --write .",
    "format:diff": "prettier --list-different ."
  },
  "bin": {
    "eventcatalog": "./dist/cli/index.js"
  },
  "publishConfig": {
    "access": "public"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "files": [
    "dist",
    "package.json"
  ],
  "exports": {
    "./cli-docs": {
      "types": "./dist/cli-docs.d.ts",
      "require": "./dist/cli-docs.js",
      "import": "./dist/cli-docs.mjs"
    }
  },
  "dependencies": {
    "@eventcatalog/breaking-changes": "workspace:*",
    "@eventcatalog/language-server": "workspace:*",
    "@eventcatalog/sdk": "workspace:*",
    "@eventcatalog/license": "^0.0.7",
    "commander": "^12.0.0",
    "dotenv": "^16.5.0",
    "gray-matter": "^4.0.3",
    "js-yaml": "^4.1.1",
    "langium": "^3.3.1",
    "open": "^11.0.0",
    "semver": "^7.7.2"
  },
  "devDependencies": {
    "@types/js-yaml": "^4.0.9",
    "@types/node": "^20.14.10",
    "prettier": "^3.3.3",
    "tsup": "^8.1.0",
    "typescript": "^5.5.3",
    "vitest": "^3.2.4"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/event-catalog/eventcatalog"
  }
}

```

### File: packages\cli\README.md
```md
## @eventcatalog/cli

Command-line interface for [EventCatalog](https://eventcatalog.dev). Import and export catalogs using the [EventCatalog DSL](https://www.eventcatalog.dev/docs/development/dsl/introduction), run SDK functions directly from your terminal, and automate your EventCatalog workflows.

### Installation

```sh
npm i @eventcatalog/cli
```

### Running with npx (no installation required)

```bash
npx @eventcatalog/cli --dir <catalog-path> <command> [args...]
```

### Running after installation

If you've installed the package, the `eventcatalog` command is available:

```bash
eventcatalog --dir <catalog-path> <command> [args...]
```

### Global Options

| Option             | Description                    | Default                 |
| ------------------ | ------------------------------ | ----------------------- |
| `-d, --dir <path>` | Path to your catalog directory | `.` (current directory) |

---

### Commands

#### `import` — Import DSL files into your catalog

Parse `.ec` (EventCatalog DSL) files and write them as catalog resources (markdown + frontmatter).

```bash
eventcatalog import [files...] [options]
```

**Options:**

| Option      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `--stdin`   | Read DSL from stdin instead of files                         |
| `--dry-run` | Preview changes without writing to disk                      |
| `--flat`    | Write all resources at the top level (no nested directories) |
| `--no-init` | Skip the interactive catalog scaffolding prompt              |

**Examples:**

```bash
# Import a single DSL file
eventcatalog import architecture.ec

# Import multiple files
eventcatalog import services.ec events.ec domains.ec

# Pipe DSL from another tool
cat architecture.ec | eventcatalog import --stdin

# Preview what would change
eventcatalog import architecture.ec --dry-run

# Import without nesting services inside domains
eventcatalog import architecture.ec --flat
```

**Behaviors:**

- If no `eventcatalog.config.js` exists, you'll be prompted to scaffold a new catalog (skip with `--no-init`).
- Importing a newer version of an existing resource automatically versions the old one.
- Re-importing the same version overwrites the existing resource.
- Referenced resources that aren't defined in the DSL (e.g., `sends event OrderCreated` without an inline body) are created as stubs at version `0.0.1`.
- Existing resource locations are preserved — updates go to where the resource already lives.

---

#### `export` — Export catalog resources to DSL

Convert catalog resources back into EventCatalog DSL (`.ec`) format.

```bash
eventcatalog export [options]
```

**Options:**

| Option                | Description                                                                               |
| --------------------- | ----------------------------------------------------------------------------------------- |
| `--all`               | Export the entire catalog                                                                 |
| `--resource <type>`   | Resource type to export (`event`, `command`, `query`, `service`, `domain`, `channel`)     |
| `--id <id>`           | Export a specific resource by ID (requires `--resource`)                                  |
| `--version <version>` | Export a specific version (requires `--resource` and `--id`)                              |
| `--hydrate`           | Include referenced resources (e.g., messages referenced by a service)                     |
| `--stdout`            | Print to stdout instead of writing a file                                                 |
| `--playground`        | Open the exported DSL in the [EventCatalog Playground](https://compass.eventcatalog.dev/) |
| `--output <path>`     | Custom output file path                                                                   |

**Examples:**

```bash
# Export a single event
eventcatalog export --resource event --id OrderCreated --stdout

# Export all services with their referenced messages
eventcatalog export --resource service --hydrate --stdout

# Export the entire catalog to a file
eventcatalog export --all --output catalog.ec

# Export and open in the playground
eventcatalog export --all --playground
```

---

#### `list` — List available SDK functions

Display all SDK functions organized by category (Events, Commands, Queries, Services, Domains, etc.).

```bash
eventcatalog list
```

---

#### `<function>` — Run any SDK function

Any unrecognized command is treated as an SDK function call. Output is JSON.

```bash
eventcatalog <function-name> [args...]
```

**Examples:**

```bash
# Get an event (latest version)
eventcatalog --dir ./my-catalog getEvent "OrderCreated"

# Get a specific version
eventcatalog --dir ./my-catalog getEvent "OrderCreated" "1.0.0"

# Get all events with options
eventcatalog --dir ./my-catalog getEvents '{"latestOnly":true}'

# Write an event
eventcatalog --dir ./my-catalog writeEvent '{"id":"OrderCreated","name":"Order Created","version":"1.0.0","markdown":"# Order Created"}'

# Get a service
eventcatalog --dir ./my-catalog getService "InventoryService"

# Add an event to a service
eventcatalog --dir ./my-catalog addEventToService "InventoryService" "sends" '{"id":"OrderCreated","version":"1.0.0"}'
```

Run `eventcatalog list` to see all available functions.

---

### Piping and Composing

Output from SDK functions is JSON, making it easy to pipe to tools like `jq`:

```bash
# Filter events by version
eventcatalog --dir ./my-catalog getEvents | jq '.[] | select(.version == "1.0.0")'

# Count total events
eventcatalog --dir ./my-catalog getEvents | jq 'length'

# Extract event IDs
eventcatalog --dir ./my-catalog getEvents | jq '.[].id'
```

### Arguments Format

Arguments are automatically parsed:

- **JSON objects:** `'{"key":"value"}'` — parsed as object
- **JSON arrays:** `'["item1","item2"]'` — parsed as array
- **Booleans:** `true` or `false` — parsed as boolean
- **Numbers:** `42` or `3.14` — parsed as number
- **Strings:** anything else — kept as string

### Documentation

- [EventCatalog DSL](https://www.eventcatalog.dev/docs/development/dsl/introduction)
- [SDK reference](https://www.eventcatalog.dev/docs/sdk)
- [CLI documentation](https://www.eventcatalog.dev/docs/development/cli)

## Enterprise support

Interested in collaborating with us? Our offerings include dedicated support, priority assistance, feature development, custom integrations, and more.

Find more details on our [services page](https://eventcatalog.dev/services).

```

### File: packages\core\package.json
```json
{
  "name": "@eventcatalog/core",
  "homepage": "https://github.com/event-catalog/eventcatalog",
  "repository": {
    "type": "git",
    "url": "https://github.com/event-catalog/eventcatalog.git"
  },
  "license": "SEE LICENSE IN LICENSE",
  "type": "module",
  "version": "3.26.16",
  "publishConfig": {
    "access": "public"
  },
  "bin": {
    "eventcatalog": "bin/eventcatalog.js"
  },
  "files": [
    "eventcatalog/",
    "!eventcatalog/**/__tests__/",
    "bin/",
    "dist/"
  ],
  "scripts": {
    "dev": "astro dev",
    "build:bin": "tsup",
    "prepublishOnly": "pnpm run build:bin",
    "test": "cross-env DISABLE_EVENTCATALOG_CACHE=true vitest",
    "test:ci": "node scripts/ci/test.js",
    "start": "astro dev",
    "build": "astro build",
    "build:cd": "node scripts/build-ci.js",
    "preview": "astro preview",
    "astro": "astro",
    "start:catalog": "node scripts/start-catalog-locally.js",
    "export:catalog": "node scripts/export-catalog-locally.js",
    "start:catalog:server": "node scripts/start-server-locally.js",
    "preview:catalog": "node scripts/preview-catalog-locally.js",
    "generate:catalog": "node scripts/generate-catalog-locally.js",
    "verify-build:catalog": "rimraf dist && pnpm run build:cd",
    "generate": "pnpm run build:bin && npx . generate",
    "format": "prettier --config .prettierrc --write \"**/*.{js,jsx,ts,tsx,json,astro}\"",
    "format:diff": "prettier --config .prettierrc --list-different \"**/*.{js,jsx,ts,tsx,json,astro}\"",
    "lint:catalog": "pnpm dlx @eventcatalog/linter examples/default",
    "check": "node scripts/check-types.js",
    "turbo:test": "turbo run test",
    "turbo:build": "turbo run build:bin"
  },
  "dependencies": {
    "@ai-sdk/react": "^3.0.17",
    "@astrojs/markdown-remark": "^7.0.1",
    "@astrojs/mdx": "^5.0.2",
    "@astrojs/node": "^10.0.3",
    "@astrojs/react": "^5.0.1",
    "@astrojs/rss": "^4.0.17",
    "@asyncapi/avro-schema-parser": "3.0.24",
    "@asyncapi/parser": "^3.6.0",
    "@asyncapi/react-component": "3.0.2",
    "@auth/core": "^0.37.4",
    "@eventcatalog/license": "^0.0.7",
    "@eventcatalog/linter": "workspace:*",
    "@eventcatalog/sdk": "workspace:*",
    "@eventcatalog/visualiser": "workspace:^",
    "@fontsource/inter": "^5.2.5",
    "@headlessui/react": "^2.0.3",
    "@heroicons/react": "^2.1.3",
    "@iconify-json/logos": "^1.2.4",
    "@mermaid-js/layout-elk": "^0.2.0",
    "@modelcontextprotocol/sdk": "^1.26.0",
    "@nanostores/react": "^1.0.0",
    "@parcel/watcher": "^2.4.1",
    "@radix-ui/react-context-menu": "^2.2.6",
    "@radix-ui/react-dialog": "^1.1.6",
    "@radix-ui/react-dropdown-menu": "^2.1.12",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-tooltip": "^1.1.8",
    "@scalar/api-reference-react": "^0.4.37",
    "@tailwindcss/typography": "^0.5.16",
    "@tailwindcss/vite": ">=4.1.5 <4.2.2",
    "@tanstack/react-table": "^8.17.3",
    "@xyflow/react": "^12.3.6",
    "ai": "^6.0.17",
    "astro": "^6.0.8",
    "astro-compress": "^2.4.0",
    "astro-expressive-code": "^0.41.7",
    "astro-seo": "^0.8.4",
    "auth-astro": "^4.2.0",
    "axios": "^1.13.5",
    "boxen": "^8.0.1",
    "commander": "^12.1.0",
    "concurrently": "^8.2.2",
    "cross-env": "^7.0.3",
    "dagre": "^0.8.5",
    "diff": "^8.0.3",
    "diff2html": "^3.4.56",
    "dotenv": "^16.5.0",
    "elkjs": "^0.10.0",
    "glob": "^13.0.6",
    "gray-matter": "^4.0.3",
    "hono": "4.12.7",
    "html-to-image": "^1.11.11",
    "js-yaml": "^4.1.1",
    "jsonpath": "^1.3.0",
    "jsonwebtoken": "^9.0.2",
    "lodash.debounce": "^4.0.8",
    "lodash.merge": "4.6.2",
    "lucide-react": "^0.453.0",
    "marked": "^15.0.6",
    "mdast-util-find-and-replace": "^3.0.2",
    "mermaid": "^11.12.1",
    "nanostores": "^1.1.0",
    "pako": "^2.1.0",
    "picocolors": "^1.1.1",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-markdown": "^10.1.0",
    "react-syntax-highlighter": "^15.6.6",
    "rehype-autolink-headings": "^7.1.0",
    "rehype-expressive-code": "^0.41.7",
    "rehype-slug": "^6.0.0",
    "remark-comment": "^1.0.0",
    "remark-directive": "^3.0.0",
    "remark-gfm": "^4.0.1",
    "rimraf": "^6.1.3",
    "semver": "7.6.3",
    "shelljs": "^0.9.0",
    "sql.js": "^1.12.0",
    "svg-pan-zoom": "^3.6.2",
    "tailwindcss": "^4.1.5",
    "typescript": "^5.4.5",
    "unist-util-visit": "^5.0.0",
    "update-notifier": "^7.3.1",
    "uuid": "^10.0.0",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "@astrojs/check": "^0.9.8",
    "@types/dagre": "^0.7.52",
    "@types/diff": "^5.2.2",
    "@types/js-yaml": "^4.0.9",
    "@types/jsonpath": "^0.2.4",
    "@types/jsonwebtoken": "^9.0.10",
    "@types/lodash.debounce": "^4.0.9",
    "@types/lodash.merge": "4.6.9",
    "@types/node": "^20.14.2",
    "@types/pako": "^2.0.3",
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@types/semver": "^7.5.8",
    "@types/shelljs": "^0.8.15",
    "@types/update-notifier": "^6.0.8",
    "@types/uuid": "^10.0.0",
    "prettier": "^3.3.3",
    "prettier-plugin-astro": "^0.14.1",
    "tsup": "^8.1.0",
    "vite": "^7.1.11",
    "vite-tsconfig-paths": "^4.3.2",
    "vitest": "^4.0.18"
  },
  "pnpm": {
    "overrides": {
      "prismjs": ">=1.30.0"
    }
  },
  "packageManager": "pnpm@10.23.0+sha512.21c4e5698002ade97e4efe8b8b4a89a8de3c85a37919f957e7a0f30f38fbc5bbdd05980ffe29179b2fb6e6e691242e098d945d1601772cad0fef5fb6411e2a4b"
}

```

### File: packages\core\README.md
```md
<div align="center">

<!-- <h1>📖 EventCatalog</h1> -->
<!-- <h3>The open source tool to help you discover and document your event-driven architectures</h3> -->




<!-- [![Star on GitHub][github-star-badge]][github-star] -->
<!-- <h3>Bring discoverability to your -->
<!-- event-driven architectures</h3> -->
<!-- <p>Discover, Explore and Document your Event Driven Architectures.</p> -->

<!-- [![MIT License][license-badge]][license] -->
<!-- [![PRs Welcome][prs-badge]][prs] -->


<!-- [![Watch on GitHub][github-watch-badge]][github-watch] -->
<!-- [![Star on GitHub][github-star-badge]][github-star] -->

<!-- <hr /> -->



<img width="745" alt="EventCatalog" src="./packages/core/images/example.png" />

<p align="center">
  <br/>
  <a href="https://eventcatalog.dev">EventCatalog</a> is a documentation tool for software architectures &mdash;
  <br/>
  bring discoverability to complex systems.
  <br/><br/>
</p>

<div align="center">

[![main](https://github.com/event-catalog/eventcatalog/actions/workflows/verify-build.yml/badge.svg)](https://github.com/event-catalog/eventcatalog/actions/workflows/verify-build.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/event-catalog/eventcatalog/blob/main/LICENSE)
[![npm version](https://badge.fury.io/js/@eventcatalog%2Fcore.svg)](https://badge.fury.io/js/@eventcatalog/core)

</div>


<!-- 

[![MIT License][license-badge]][license]
[![PRs Welcome][prs-badge]][prs]
<img src="https://img.shields.io/github/actions/workflow/status/event-catalog/eventcatalog/verify-build.yml"/>
[![](https://dcbadge.limes.pink/api/server/https://discord.gg/3rjaZMmrAm?style=flat)](https://discord.gg/3rjaZMmrAm) [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="20px" />](https://www.linkedin.com/in/david-boyne/) [![blog](https://img.shields.io/badge/blog-EDA--Visuals-brightgreen)](https://eda-visuals.boyney.io/?utm_source=event-catalog-gihub) 
 -->





<!-- 

<h4>Features: Documentation for Event Driven Architectures, Integration with any broker, Generator from your OpenAPI and AsyncAPI documents, Docs and Code, Markdown driven, Document Domains/Services/Messages/Schemas and more, Content versioning, Assign Owners, Schemas, OpenAPI, MDX Components and more...</h4> -->

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-68-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- [Read the Docs](https://www.eventcatalog.dev/docs/development/getting-started/introduction) | [View Demo](https://demo.eventcatalog.dev) -->

</div>

## Install

The **recommended** way to install the latest version of EventCatalog is by running the command below:
```
npx @eventcatalog/create-eventcatalog@latest my-catalog
```

Looking for help? Start with our [Getting Started](https://www.eventcatalog.dev/docs/development/getting-started/installation) guide

## Documentation
Visit our [official documentation](https://www.eventcatalog.dev/docs/development/getting-started).

## Support
Having trouble? Get help in the official [EventCatalog Discord](https://discord.gg/3rjaZMmrAm).

## Demos

Here are some examples of EventCatalog in action:

- [Finance System](https://eventcatalog-examples-finance.vercel.app/)
- [Healthcare System](https://eventcatalog-examples-healthcare.vercel.app/)
- [E-Commerce System](https://demo.eventcatalog.dev/)
- [SaaS System](https://eventcatalog-examples-saas.vercel.app/)


## Contributing

If you have any questions, features or issues please raise any issue or pull requests you like. We will try my best to get back to you.

You can find the [contributing guidelines here](https://eventcatalog.dev/docs/contributing/overview).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://boyney.io/"><img src="https://avatars.githubusercontent.com/u/3268013?v=4?s=100" width="100px;" alt="David Boyne"/><br /><sub><b>David Boyne</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=boyney123" title="Code">💻</a> <a href="#content-boyney123" title="Content">🖋</a> <a href="#design-boyney123" title="Design">🎨</a> <a href="#example-boyney123" title="Examples">💡</a> <a href="#ideas-boyney123" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=boyney123" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://otbe.io"><img src="https://avatars.githubusercontent.com/u/3391052?v=4?s=100" width="100px;" alt="Benjamin Otto"/><br /><sub><b>Benjamin Otto</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=otbe" title="Code">💻</a> <a href="#ideas-otbe" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=otbe" title="Documentation">📖</a> <a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Aotbe" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pongz79"><img src="https://avatars.githubusercontent.com/u/250872?v=4?s=100" width="100px;" alt="Tiago Oliveira"/><br /><sub><b>Tiago Oliveira</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=pongz79" title="Documentation">📖</a> <a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Apongz79" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.bigjump.com/"><img src="https://avatars.githubusercontent.com/u/11387911?v=4?s=100" width="100px;" alt="Jay McGuinness"/><br /><sub><b>Jay McGuinness</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=jaymcguinness" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/davidkpiano"><img src="https://avatars.githubusercontent.com/u/1093738?v=4?s=100" width="100px;" alt="David Khourshid"/><br /><sub><b>David Khourshid</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=davidkpiano" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/thim81"><img src="https://avatars.githubusercontent.com/u/952446?v=4?s=100" width="100px;" alt="thim81"/><br /><sub><b>thim81</b></sub></a><br /><a href="#ideas-thim81" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Athim81" title="Bug reports">🐛</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=thim81" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Muthuveerappanv"><img src="https://avatars.githubusercontent.com/u/33663725?v=4?s=100" width="100px;" alt="Muthu"/><br /><sub><b>Muthu</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3AMuthuveerappanv" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tavelli"><img src="https://avatars.githubusercontent.com/u/484951?v=4?s=100" width="100px;" alt="Dan Tavelli"/><br /><sub><b>Dan Tavelli</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=tavelli" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/steppi91"><img src="https://avatars.githubusercontent.com/u/25939641?v=4?s=100" width="100px;" alt="steppi91"/><br /><sub><b>steppi91</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=steppi91" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://twitter.com/PipoPeperoni"><img src="https://avatars.githubusercontent.com/u/1152805?v=4?s=100" width="100px;" alt="Donald Pipowitch"/><br /><sub><b>Donald Pipowitch</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/issues?q=author%3Adonaldpipowitch" title="Bug reports">🐛</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=donaldpipowitch" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://unravelled.dev"><img src="https://avatars.githubusercontent.com/u/2233210?v=4?s=100" width="100px;" alt="Ken"/><br /><sub><b>Ken</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=kzhen" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://rtoro.cl"><img src="https://avatars.githubusercontent.com/u/5186897?v=4?s=100" width="100px;" alt="Rodolfo Toro"/><br /><sub><b>Rodolfo Toro</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=rtoro" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://blog.hackedbrain.com"><img src="https://avatars.githubusercontent.com/u/284152?v=4?s=100" width="100px;" alt="Drew Marsh"/><br /><sub><b>Drew Marsh</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=drub0y" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dpwdec"><img src="https://avatars.githubusercontent.com/u/51292634?v=4?s=100" width="100px;" alt="Dec Kolakowski"/><br /><sub><b>Dec Kolakowski</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=dpwdec" title="Code">💻</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=dpwdec" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dytyniuk"><img src="https://avatars.githubusercontent.com/u/1890615?v=4?s=100" width="100px;" alt="Yevhenii Dytyniuk"/><br /><sub><b>Yevhenii Dytyniuk</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=dytyniuk" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lcsbltm"><img src="https://avatars.githubusercontent.com/u/25868958?v=4?s=100" width="100px;" alt="lcsbltm"/><br /><sub><b>lcsbltm</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=lcsbltm" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://matt.martz.codes"><img src="https://avatars.githubusercontent.com/u/978362?v=4?s=100" width="100px;" alt="Matt Martz"/><br /><sub><b>Matt Martz</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=martzcodes" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/michelgrootjans"><img src="https://avatars.githubusercontent.com/u/345770?v=4?s=100" width="100px;" alt="Michel Grootjans"/><br /><sub><b>Michel Grootjans</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=michelgrootjans" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/arturoabruzzini"><img src="https://avatars.githubusercontent.com/u/17528406?v=4?s=100" width="100px;" alt="Arturo Abruzzini"/><br /><sub><b>Arturo Abruzzini</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=arturoabruzzini" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/adlecluse"><img src="https://avatars.githubusercontent.com/u/13390934?v=4?s=100" width="100px;" alt="Ad L'Ecluse"/><br /><sub><b>Ad L'Ecluse</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=adlecluse" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rafaelrenanpacheco"><img src="https://avatars.githubusercontent.com/u/12160864?v=4?s=100" width="100px;" alt="Rafael Renan Pacheco"/><br /><sub><b>Rafael Renan Pacheco</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=rafaelrenanpacheco" title="Code">💻</a> <a href="https://github.com/event-catalog/eventcatalog/commits?author=rafaelrenanpacheco" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://ldiego73.github.io/"><img src="https://avatars.githubusercontent.com/u/394222?v=4?s=100" width="100px;" alt="Luis Diego"/><br /><sub><b>Luis Diego</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=ldiego73" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/danielruf/"><img src="https://avatars.githubusercontent.com/u/827205?v=4?s=100" width="100px;" alt="Daniel Ruf"/><br /><sub><b>Daniel Ruf</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=DanielRuf" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/frenkan"><img src="https://avatars.githubusercontent.com/u/859840?v=4?s=100" width="100px;" alt="Fredrik Johansson"/><br /><sub><b>Fredrik Johansson</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=frenkan" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://gaddam1987.github.io/"><img src="https://avatars.githubusercontent.com/u/2576375?v=4?s=100" width="100px;" alt="Naresh Kumar Reddy Gaddam"/><br /><sub><b>Naresh Kumar Reddy Gaddam</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=gaddam1987" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dremonkey"><img src="https://avatars.githubusercontent.com/u/480159?v=4?s=100" width="100px;" alt="Andre Deutmeyer"/><br /><sub><b>Andre Deutmeyer</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=dremonkey" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pebbz"><img src="https://avatars.githubusercontent.com/u/1685464?v=4?s=100" width="100px;" alt="Pebbz"/><br /><sub><b>Pebbz</b></sub></a><br /><a href="https://github.com/event-catalog/eventcatalog/commits?author=pebbz" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://alexander.holbreich.org/"><img src="https://avatars.githubusercontent.com/u/16252784?v=4?s=100" width="10
... [TRUNCATED]
```

### File: AGENTS.md
```md
# Repository Guidelines

## Project Structure & Module Organization
This repository is a `pnpm` + Turborepo monorepo. Packages live in `packages/*`:
- `packages/core`: main EventCatalog app (Astro + React) and local scripts.
- `packages/cli`, `packages/sdk`, `packages/linter`, `packages/language-server`, `packages/visualiser`, `packages/create-eventcatalog`.
- `packages/playground`: local DSL playground app.

Examples and integration checks live in `examples/` (notably `examples/default`). Shared release metadata is in `.changeset/`.

## Build, Test, and Development Commands
Run from repo root unless noted:
- `pnpm i`: install workspace dependencies.
- `pnpm build:bin`: build distributable artifacts across packages.
- `pnpm build`: run full Turbo build graph.
- `pnpm test`: run package tests.
- `pnpm test:ci`: CI-style test run used by GitHub Actions.
- `pnpm format` / `pnpm format:diff`: format or check formatting.
- `pnpm start:catalog`: run local catalog via `@eventcatalog/core`.
- `pnpm --filter @eventcatalog/<pkg> run <script>`: work on one package (example: `pnpm --filter @eventcatalog/sdk test`).

## Coding Style & Naming Conventions
Code is primarily TypeScript. Follow package Prettier rules:
- 2 spaces, semicolons, single quotes, trailing commas (`es5`), print width 130.
- Astro files in core use `prettier-plugin-astro`.

Naming patterns:
- React components: `PascalCase` (for example `NodeGraph.tsx`).
- Utility/module files: existing local style (`kebab-case` or descriptive lowercase) within that package.
- Keep public API names explicit and package-scoped.

## Testing Guidelines
Vitest is the default test framework across packages. Tests are placed either near source (`src/test`, `test`, `tests`) or under `__tests__`.
- Use `*.test.ts` or `*.spec.ts` to match existing suites.
- Add/adjust tests with every behavior change.
- For CLI tests (especially under `packages/cli/src/test/import-export`), use descriptive, rule-style test names that read in plain English, for example: `when we import a domain that does not exist in the catalog, a domain resource is created`.
- For CLI export tests, assert exact expected outputs and errors (prefer `toBe` with full strings) instead of partial-match assertions like `toContain`.
- For multiline CLI export DSL assertions, use the shared `dsl` template tag with `toBe(...)` so expected blocks stay readable and indented in the test file.
- For core/UI-impacting changes, also verify catalog build paths (`pnpm verify-build:catalog`).

## Commit & Pull Request Guidelines
Recent history favors Conventional Commit style with scopes:
- `feat(cli): add import command`
- `fix(core): avoid first-run dev restart`

Use `<type>(<scope>): <imperative summary>` when possible. For PRs:
- Fill in the Motivation section from `.github/PULL_REQUEST_TEMPLATE.md`.
- Link related issues.
- Include screenshots/GIFs for UI changes.
- Add a changeset (`pnpm changeset`) for publishable package changes unless the change is internal-only.

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

EventCatalog is an open-source documentation tool for Event-Driven Architectures. It helps teams document events, commands, queries, services, domains, and flows in a discoverable catalog. Built with Astro, React, and TypeScript.

This is a **monorepo** managed with Turborepo and pnpm workspaces containing these packages:
- `@eventcatalog/core` - The main EventCatalog application
- `@eventcatalog/sdk` - SDK for programmatically interacting with EventCatalog
- `@eventcatalog/create-eventcatalog` - CLI tool for scaffolding new EventCatalog projects
- `@eventcatalog/visualiser` - Standalone React visualiser component (ReactFlow-based node graphs)
- `@eventcatalog/dsl-playground` - Browser-based DSL playground for authoring EventCatalog DSL
- `@eventcatalog/language-server` - Language server for the EventCatalog DSL (parsing, diagnostics, completion)

## Quick Reference Commands

| Task | Command |
|------|---------|
| Start dev server | `pnpm run start:catalog` |
| Start SSR server | `pnpm run start:catalog:server` |
| Build all packages | `pnpm run build` or `pnpm run build:bin` |
| Build catalog example | `pnpm run verify-build:catalog` |
| Test (all packages) | `pnpm run test` |
| Test (CI mode) | `pnpm run test:ci` |
| Test (single file) | `pnpm run test path/to/file.test.ts --run` |
| Format code | `pnpm run format` |
| Check formatting | `pnpm run format:diff` |
| E2E tests | `pnpm run test:e2e` |
| Create changeset | `pnpm changeset` |
| Release packages | `pnpm run release` |

## Project Structure

```
/packages
  /core                      # @eventcatalog/core
    /eventcatalog            # Main application source
      /src
        /components          # React and Astro components
        /pages               # Astro pages and API routes
        /enterprise          # Scale plan features (AI Chat, MCP Server)
        /utils               # Shared utilities
          /collections       # Astro content collection helpers
        /layouts             # Page layouts
        /styles              # CSS and theme files
        /types               # TypeScript type definitions
        /stores              # Nanostores state management
        /content             # Content collection definitions
        /__tests__           # Unit tests (colocated with source)
    /bin                     # CLI entry point
    /scripts                 # Build and development scripts
  /sdk                       # @eventcatalog/sdk
    /src                     # SDK source code
      /test                  # SDK tests (510 tests)
    /dist                    # Built output (not committed)
  /create-eventcatalog       # @eventcatalog/create-eventcatalog
    /templates               # Project templates (default, asyncapi, openapi, etc.)
    /helpers                 # Template helpers
    /dist                    # Built output (not committed)
  /visualiser                # @eventcatalog/visualiser
    /src
      /components            # NodeGraph, FocusMode, Search, etc.
      /nodes                 # Node type components (service, event, command, etc.)
      /edges                 # Edge type components (animated, multiline, flow)
      /utils                 # Layout, mermaid export, clipboard utilities
      /types                 # Shared types (including DslGraph)
  /playground                # @eventcatalog/dsl-playground
    /src
      /components            # Editor, Visualizer, TabBar
      /hooks                 # useDslParser
      /monaco                # Monaco editor config, completions, diagnostics
      /examples              # Built-in DSL examples
  /language-server           # @eventcatalog/language-server
    /src                     # DSL parser, graph builder, formatter
/examples
  /default                   # Default example catalog (used by start:catalog)
  /e-commerce                # E-commerce example
/.changeset                  # Changesets for versioning
/.github/workflows           # CI/CD workflows
```

## Tech Stack

- **Monorepo**: Turborepo + pnpm workspaces
- **Framework**: Astro 5 with React islands
- **Styling**: Tailwind CSS with CSS variables for theming
- **State**: Nanostores
- **Testing**: Vitest (unit), Playwright (E2E)
- **Content**: Astro Content Collections with Zod schemas
- **AI Features**: Vercel AI SDK, MCP Protocol
- **Versioning**: Changesets

## Code Conventions

### Imports

```typescript
// Use node: prefix for Node.js built-ins
import fs from 'node:fs';
import path from 'node:path';

// Use path aliases
import { getCollection } from 'astro:content';
import { myUtil } from '@utils/my-util';
import { MyComponent } from '@components/MyComponent';
```

### TypeScript

- Strict typing enabled
- Use `as const` for literal types
- Prefer type guards over type assertions
- Use Zod for runtime validation (especially in API routes)

### Astro Content Collections

Resources are stored in content collections. Key collections:
- `events`, `commands`, `queries` (messages)
- `services`, `domains`, `flows`, `channels`, `entities`
- `teams`, `users` (non-versioned)

The whole astro collection schemas are in the `eventcatalog/src/content.config.ts` file.


### Getting collection information

We prefer to use the utility classes we have to get collection for example:

```
import { getEvents } from '@utils/collections/events';
import { getCommands } from '@utils/collections/commands';
import { getQueries } from '@utils/collections/queries';
import { getServices } from '@utils/collections/services';
import { getDomains } from '@utils/collections/domains';
import { getFlows } from '@utils/collections/flows';
import { getChannels } from '@utils/collections/channels';
import { getEntities } from '@utils/collections/entities';
import { getTeams } from '@utils/collections/teams';
import { getUsers } from '@utils/collections/users';
```

Where you cant do that though you may use the `getCollection` and `getEntry` functions from the `astro:content` package.

```typescript
// Getting collections
import { getCollection, getEntry } from 'astro:content';

const events = await getCollection('events');
const event = await getEntry('events', 'OrderCreated-1.0.0');
```

### Versioning

Most resources are versioned. Entry IDs follow the pattern: `{id}-{version}` (e.g., `OrderCreated-1.0.0`).

When you need to get specific version or latest version you need to use the `getItemsFromCollectionByIdAndSemverOrLatest` utility function.

```typescript
// Use existing utilities for version handling
import { getItemsFromCollectionByIdAndSemverOrLatest } from '@utils/collections/util';
```

### Error Handling

For API routes and tools, return error objects instead of throwing:

```typescript
if (!resource) {
  return { error: `Resource not found: ${id}` };
}
```

### Pagination

Use cursor-based pagination with the `paginate()` helper from `@enterprise/tools/catalog-tools`:

```typescript
import { paginate } from '@enterprise/tools/catalog-tools';

const result = paginate(items, cursor, pageSize);
if ('error' in result) return result;
```

## Feature Flags

Check feature availability before using enterprise features:

```typescript
import { isEventCatalogScaleEnabled, isSSR } from '@utils/feature';

if (!isEventCatalogScaleEnabled()) {
  return { error: 'Feature requires Scale plan' };
}
```

## Testing

- Tests are colocated in `__tests__` directories (core) or `src/test` (SDK)
- Test files use `.test.ts` or `.test.tsx` extension
- Example catalogs for testing: `packages/core/eventcatalog/src/__tests__/example-catalog/`
- SDK has 510 tests in `packages/sdk/src/test/`

Don't run tests in watch mode.

```bash
# Run all tests (all packages via Turbo)
pnpm run test

# Run tests in CI mode
pnpm run test:ci

# Run specific test file
pnpm run test packages/core/eventcatalog/src/utils/__tests__/my-util.test.ts --run

# Run SDK tests only
pnpm --filter @eventcatalog/sdk run test

# Run tests matching pattern
pnpm run test -t "getResources" --run
```

## Theming Guidelines

EventCatalog uses CSS variables for theming to support light/dark mode and custom themes.

### Use CSS Variables Instead of Hardcoded Colors

```astro
<!-- Correct - uses CSS variables -->
<div class="bg-[rgb(var(--ec-page-bg))] text-[rgb(var(--ec-page-text))]">

<!-- Incorrect - hardcoded colors -->
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white">
```

### Common CSS Variables

| Variable | Usage |
|----------|-------|
| `--ec-page-bg` | Page/content background |
| `--ec-page-text` | Primary text color |
| `--ec-page-text-muted` | Secondary/muted text |
| `--ec-page-border` | Borders and dividers |
| `--ec-card-bg` | Card/elevated surface background |
| `--ec-accent` | Accent/brand color |
| `--ec-accent-subtle` | Light accent background |
| `--ec-accent-text` | Text on accent backgrounds |
| `--ec-button-bg` | Button background |
| `--ec-button-text` | Button text |
| `--ec-icon-color` | Icon default color |
| `--ec-icon-hover` | Icon hover color |
| `--ec-input-bg` | Input field background |
| `--ec-input-border` | Input field border |
| `--ec-input-text` | Input field text |

### Theme Files

- Base theme: `eventcatalog/src/styles/theme.css`
- Additional themes: `eventcatalog/src/styles/themes/*.css`

### Key Points

1. Variables use RGB values without `rgb()` wrapper for Tailwind opacity support
2. Use syntax `[rgb(var(--ec-variable))]` in Tailwind classes
3. For opacity: `[rgb(var(--ec-variable)/0.5)]`
4. Dark mode handled via `data-theme="dark"` attribute
5. Never use `dark:` Tailwind variants for theme colors

## Common Patterns

### API Routes with Hono

For complex API routes, use Hono inside Astro API routes:

```typescript
import type { APIRoute } from 'astro';
import { Hono } from 'hono';

const app = new Hono().basePath('/api/my-route');

app.get('/', async (c) => {
  return c.json({ message: 'Hello' });
});

export const ALL: APIRoute = async ({ request }) => {
  return app.fetch(request);
};

export const prerender = false;
```

### Shared Tool Implementations

When building features used by both AI Chat and MCP Server, add shared logic to `@enterprise/tools/catalog-tools.ts`.

## Monorepo Workflow

### Working with Packages

- **Core** depends on **SDK** and **Visualiser** via `workspace:*` references
- **Playground** depends on **Visualiser** and **Language Server**
- **Visualiser** is standalone (no internal workspace dependencies)
- Changes to workspace dependencies are automatically picked up in development
- Build commands run via Turbo (handles dependency ordering and caching)
- Each package has its own `package.json` with build/test/format scripts

### Running Package-Specific Commands

```bash
# Run command in specific package
pnpm --filter @eventcatalog/core run start:catalog
pnpm --filter @eventcatalog/sdk run test

# Run command in all packages (via Turbo)
pnpm run build        # Builds all packages
pnpm run test         # Tests all packages
pnpm run format       # Formats all packages
```

### Versioning and Releases

- Use **changesets** for versioning: `pnpm changeset`
- Changesets go in `.changeset/` directory
- Choose version bump: `patch`, `minor`, or `major`
- Select which packages are affected
- On merge to main, changesets bot creates version PR
- Merging version PR publishes all packages to npm

### CI/CD

- `.github/workflows/verify-build.yml` - Builds and tests all packages
- `.github/workflows/lint.yml` - Runs format check on all packages
- `.github/workflows/release.yml` - Publishes packages via changesets
- Turbo caches builds and tests (only runs what changed)

## Development Tips

- The example catalog at `/examples/default` is used when running `pnpm run start:catalog`
- SSR mode is required for AI Chat and MCP Server features
- Use `DISABLE_EVENTCATALOG_CACHE=true` env var to disable caching during development
- Run `pnpm run format` before committing changes
- Never verify the build, the developer will do this themselves
- SDK test files may get modified during test runs - restore with `git restore packages/sdk/src/test/`

## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
