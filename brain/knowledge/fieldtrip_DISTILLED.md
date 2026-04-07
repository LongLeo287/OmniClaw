---
id: fieldtrip
type: knowledge
owner: OA_Triage
---
# fieldtrip
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@eventcatalog/fieldtrip",
  "version": "0.0.1",
  "description": "Search across OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files",
  "bin": {
    "fieldtrip": "./bin/cli.js"
  },
  "files": [
    "bin",
    "dist"
  ],
  "scripts": {
    "build": "npm run build:ui && npm run build:cli",
    "build:ui": "vite build",
    "build:cli": "tsc -p tsconfig.cli.json",
    "dev": "tsx src/cli/index.ts --dir ./test-schemas",
    "changeset": "changeset",
    "version-packages": "changeset version",
    "release": "npm run build && changeset publish"
  },
  "keywords": [
    "schema",
    "search",
    "openapi",
    "asyncapi",
    "protobuf",
    "avro"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@types/d3": "^7.4.3",
    "commander": "^12.0.0",
    "d3": "^7.9.0",
    "express": "^4.18.0",
    "glob": "^10.3.0",
    "minisearch": "^7.0.0",
    "monaco-editor": "^0.55.1",
    "open": "^10.0.0",
    "protobufjs": "^7.2.0",
    "yaml": "^2.4.0"
  },
  "devDependencies": {
    "@changesets/changelog-github": "^0.6.0",
    "@changesets/cli": "^2.30.0",
    "@types/express": "^4.17.21",
    "@types/node": "^20.11.0",
    "tsx": "^4.7.0",
    "typescript": "^5.4.0",
    "vite": "^5.2.0"
  }
}

```

### File: README.md
```md
<div align="center">

# FieldTrip

**Instantly search, explore, and visualize every field across your schemas.**

Point it at a directory. It finds your OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files, indexes every property, and launches a local UI to explore them.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/@eventcatalog/fieldtrip.svg)](https://www.npmjs.com/package/@eventcatalog/fieldtrip)

</div>

---

![FieldTrip Table View](images/table.png)

## Why FieldTrip?

Schema sprawl is real. When your system has dozens of services each with their own schema definitions, it becomes impossible to answer simple questions:

- *"Which schemas use a `customerId` field?"*
- *"Is `email` required everywhere it appears?"*
- *"What fields does `Order` share with `Payment`?"*

FieldTrip answers these in seconds. One command, zero config.

## Quick Start

```bash
npx @eventcatalog/fieldtrip --dir ./schemas
```

That's it. FieldTrip scans the directory, indexes every property, and opens a local UI at `http://localhost:3200`.

## Features

### Table View — Search & Filter

Full-text search across all property names, types, and descriptions. Filter by schema type, sort by name/schema/type, and click any property to view it in context with syntax highlighting.

- Prefix and fuzzy matching
- Exact match with `"quoted strings"`
- Filter by schema type (OpenAPI, AsyncAPI, Proto, Avro, JSON)
- Filter by specific schema files via the sidebar
- Click any row to view the full schema with the property highlighted

![FieldTrip Table View](images/table.png)

### Matrix View — Property x Schema

See which properties appear in which schemas at a glance. A heatmap-style grid where rows are properties and columns are schemas.

- Green cells = required, Blue cells = optional
- Hover to see type, schema, and required status
- Sort by frequency, alphabetical, or required count
- Instantly spot shared fields across your architecture

![FieldTrip Matrix View](images/matrix.png)

### Graph View — Force-Directed Relationships

Visualize how schemas are connected through shared properties. Schema nodes cluster with their properties, and shared fields create visible bridges between schemas.

- D3.js force-directed simulation
- Click a property to highlight all schemas sharing that field
- Click a schema to highlight all its properties
- "Shared only" toggle to reduce noise
- Drag, zoom, and pan

![FieldTrip Graph View](images/graph.png)

## Supported Schemas

| Format | Extensions | What's indexed |
|--------|-----------|---------------|
| **OpenAPI** | `.yaml` `.yml` `.json` | Components, definitions, inline request/response bodies |
| **AsyncAPI** | `.yaml` `.yml` `.json` | Components, messages, channel payloads (v2 & v3) |
| **Protobuf** | `.proto` | Messages, enums, nested types |
| **Avro** | `.avsc` | Records, nested records, unions, arrays, maps |
| **JSON Schema** | `.json` | Properties, nested objects, allOf/oneOf/anyOf |

## CLI Options

```
Usage: fieldtrip [options]

Options:
  --dir <path>     Directory to scan for schema files (required)
  --port <number>  Port for the web UI (default: 3200)
  --no-open        Do not auto-open browser
  -h, --help       Display help
```

## Development

```bash
# Install dependencies
npm install

# Run in dev mode
npm run dev

# Build for production
npm run build
```

## How It Works

1. **Scan** — Recursively finds schema files by extension and content detection
2. **Parse** — Extracts every property with its name, type, description, path, and required status
3. **Index** — Builds a MiniSearch full-text index with prefix search and fuzzy matching
4. **Serve** — Launches an Express server with a Vite-built frontend

## License

[MIT](LICENSE)

```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works
with multi-package repos, or single-package repos to help you version and publish your code. You can
find the full documentation for it [in our repository](https://github.com/changesets/changesets).

We have a quick list of common questions to get you started engaging with this project in
[our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md).

```

### File: website\package.json
```json
{
  "name": "@eventcatalog/fieldtrip-website",
  "type": "module",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5.9.3"
  }
}

```

### File: package-lock.json
```json
{
  "name": "@eventcatalog/fieldtrip",
  "version": "0.0.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "@eventcatalog/fieldtrip",
      "version": "0.0.1",
      "license": "MIT",
      "dependencies": {
        "@types/d3": "^7.4.3",
        "commander": "^12.0.0",
        "d3": "^7.9.0",
        "express": "^4.18.0",
        "glob": "^10.3.0",
        "minisearch": "^7.0.0",
        "monaco-editor": "^0.55.1",
        "open": "^10.0.0",
        "protobufjs": "^7.2.0",
        "yaml": "^2.4.0"
      },
      "bin": {
        "fieldtrip": "bin/cli.js"
      },
      "devDependencies": {
        "@changesets/changelog-github": "^0.6.0",
        "@changesets/cli": "^2.30.0",
        "@types/express": "^4.17.21",
        "@types/node": "^20.11.0",
        "tsx": "^4.7.0",
        "typescript": "^5.4.0",
        "vite": "^5.2.0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.28.6.tgz",
      "integrity": "sha512-05WQkdpL9COIMz4LjTxGpPNCdlpyimKppYNoJ5Di5EUObifl8t4tuLuUBBZEpoLYOmfvIWrsp9fCl0HoPRVTdA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@changesets/apply-release-plan": {
      "version": "7.1.0",
      "resolved": "https://registry.npmjs.org/@changesets/apply-release-plan/-/apply-release-plan-7.1.0.tgz",
      "integrity": "sha512-yq8ML3YS7koKQ/9bk1PqO0HMzApIFNwjlwCnwFEXMzNe8NpzeeYYKCmnhWJGkN8g7E51MnWaSbqRcTcdIxUgnQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/config": "^3.1.3",
        "@changesets/get-version-range-type": "^0.4.0",
        "@changesets/git": "^3.0.4",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "detect-indent": "^6.0.0",
        "fs-extra": "^7.0.1",
        "lodash.startcase": "^4.4.0",
        "outdent": "^0.5.0",
        "prettier": "^2.7.1",
        "resolve-from": "^5.0.0",
        "semver": "^7.5.3"
      }
    },
    "node_modules/@changesets/assemble-release-plan": {
      "version": "6.0.9",
      "resolved": "https://registry.npmjs.org/@changesets/assemble-release-plan/-/assemble-release-plan-6.0.9.tgz",
      "integrity": "sha512-tPgeeqCHIwNo8sypKlS3gOPmsS3wP0zHt67JDuL20P4QcXiw/O4Hl7oXiuLnP9yg+rXLQ2sScdV1Kkzde61iSQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@changesets/get-dependents-graph": "^2.1.3",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "semver": "^7.5.3"
      }
    },
    "node_modules/@changesets/changelog-git": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/@changesets/changelog-git/-/changelog-git-0.2.1.tgz",
      "integrity": "sha512-x/xEleCFLH28c3bQeQIyeZf8lFXyDFVn1SgcBiR2Tw/r4IAWlk1fzxCEZ6NxQAjF2Nwtczoen3OA2qR+UawQ8Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0"
      }
    },
    "node_modules/@changesets/changelog-github": {
      "version": "0.6.0",
      "resolved": "https://registry.npmjs.org/@changesets/changelog-github/-/changelog-github-0.6.0.tgz",
      "integrity": "sha512-wA2/y4hR/A1K411cCT75rz0d46Iezxp1WYRFoFJDIUpkQ6oDBAIUiU7BZkDCmYgz0NBl94X1lgcZO+mHoiHnFg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/get-github-info": "^0.8.0",
        "@changesets/types": "^6.1.0",
        "dotenv": "^8.1.0"
      }
    },
    "node_modules/@changesets/cli": {
      "version": "2.30.0",
      "resolved": "https://registry.npmjs.org/@changesets/cli/-/cli-2.30.0.tgz",
      "integrity": "sha512-5D3Nk2JPqMI1wK25pEymeWRSlSMdo5QOGlyfrKg0AOufrUcjEE3RQgaCpHoBiM31CSNrtSgdJ0U6zL1rLDDfBA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/apply-release-plan": "^7.1.0",
        "@changesets/assemble-release-plan": "^6.0.9",
        "@changesets/changelog-git": "^0.2.1",
        "@changesets/config": "^3.1.3",
        "@changesets/errors": "^0.2.0",
        "@changesets/get-dependents-graph": "^2.1.3",
        "@changesets/get-release-plan": "^4.0.15",
        "@changesets/git": "^3.0.4",
        "@changesets/logger": "^0.1.1",
        "@changesets/pre": "^2.0.2",
        "@changesets/read": "^0.6.7",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@changesets/write": "^0.4.0",
        "@inquirer/external-editor": "^1.0.2",
        "@manypkg/get-packages": "^1.1.3",
        "ansi-colors": "^4.1.3",
        "enquirer": "^2.4.1",
        "fs-extra": "^7.0.1",
        "mri": "^1.2.0",
        "package-manager-detector": "^0.2.0",
        "picocolors": "^1.1.0",
        "resolve-from": "^5.0.0",
        "semver": "^7.5.3",
        "spawndamnit": "^3.0.1",
        "term-size": "^2.1.0"
      },
      "bin": {
        "changeset": "bin.js"
      }
    },
    "node_modules/@changesets/config": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/@changesets/config/-/config-3.1.3.tgz",
      "integrity": "sha512-vnXjcey8YgBn2L1OPWd3ORs0bGC4LoYcK/ubpgvzNVr53JXV5GiTVj7fWdMRsoKUH7hhhMAQnsJUqLr21EncNw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@changesets/get-dependents-graph": "^2.1.3",
        "@changesets/logger": "^0.1.1",
        "@changesets/should-skip-package": "^0.1.2",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "fs-extra": "^7.0.1",
        "micromatch": "^4.0.8"
      }
    },
    "node_modules/@changesets/errors": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/@changesets/errors/-/errors-0.2.0.tgz",
      "integrity": "sha512-6BLOQUscTpZeGljvyQXlWOItQyU71kCdGz7Pi8H8zdw6BI0g3m43iL4xKUVPWtG+qrrL9DTjpdn8eYuCQSRpow==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "extendable-error": "^0.1.5"
      }
    },
    "node_modules/@changesets/get-dependents-graph": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/@changesets/get-dependents-graph/-/get-dependents-graph-2.1.3.tgz",
      "integrity": "sha512-gphr+v0mv2I3Oxt19VdWRRUxq3sseyUpX9DaHpTUmLj92Y10AGy+XOtV+kbM6L/fDcpx7/ISDFK6T8A/P3lOdQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "picocolors": "^1.1.0",
        "semver": "^7.5.3"
      }
    },
    "node_modules/@changesets/get-github-info": {
      "version": "0.8.0",
      "resolved": "https://registry.npmjs.org/@changesets/get-github-info/-/get-github-info-0.8.0.tgz",
      "integrity": "sha512-cRnC+xdF0JIik7coko3iUP9qbnfi1iJQ3sAa6dE+Tx3+ET8bjFEm63PA4WEohgjYcmsOikPHWzPsMWWiZmntOQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "dataloader": "^1.4.0",
        "node-fetch": "^2.5.0"
      }
    },
    "node_modules/@changesets/get-release-plan": {
      "version": "4.0.15",
      "resolved": "https://registry.npmjs.org/@changesets/get-release-plan/-/get-release-plan-4.0.15.tgz",
      "integrity": "sha512-Q04ZaRPuEVZtA+auOYgFaVQQSA98dXiVe/yFaZfY7hoSmQICHGvP0TF4u3EDNHWmmCS4ekA/XSpKlSM2PyTS2g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/assemble-release-plan": "^6.0.9",
        "@changesets/config": "^3.1.3",
        "@changesets/pre": "^2.0.2",
        "@changesets/read": "^0.6.7",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3"
      }
    },
    "node_modules/@changesets/get-version-range-type": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@changesets/get-version-range-type/-/get-version-range-type-0.4.0.tgz",
      "integrity": "sha512-hwawtob9DryoGTpixy1D3ZXbGgJu1Rhr+ySH2PvTLHvkZuQ7sRT4oQwMh0hbqZH1weAooedEjRsbrWcGLCeyVQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@changesets/git": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@changesets/git/-/git-3.0.4.tgz",
      "integrity": "sha512-BXANzRFkX+XcC1q/d27NKvlJ1yf7PSAgi8JG6dt8EfbHFHi4neau7mufcSca5zRhwOL8j9s6EqsxmT+s+/E6Sw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@manypkg/get-packages": "^1.1.3",
        "is-subdir": "^1.1.1",
        "micromatch": "^4.0.8",
        "spawndamnit": "^3.0.1"
      }
    },
    "node_modules/@changesets/logger": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/@changesets/logger/-/logger-0.1.1.tgz",
      "integrity": "sha512-OQtR36ZlnuTxKqoW4Sv6x5YIhOmClRd5pWsjZsddYxpWs517R0HkyiefQPIytCVh4ZcC5x9XaG8KTdd5iRQUfg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "picocolors": "^1.1.0"
      }
    },
    "node_modules/@changesets/parse": {
      "version": "0.4.3",
      "resolved": "https://registry.npmjs.org/@changesets/parse/-/parse-0.4.3.tgz",
      "integrity": "sha512-ZDmNc53+dXdWEv7fqIUSgRQOLYoUom5Z40gmLgmATmYR9NbL6FJJHwakcCpzaeCy+1D0m0n7mT4jj2B/MQPl7A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "js-yaml": "^4.1.1"
      }
    },
    "node_modules/@changesets/pre": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/@changesets/pre/-/pre-2.0.2.tgz",
      "integrity": "sha512-HaL/gEyFVvkf9KFg6484wR9s0qjAXlZ8qWPDkTyKF6+zqjBe/I2mygg3MbpZ++hdi0ToqNUF8cjj7fBy0dg8Ug==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/errors": "^0.2.0",
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3",
        "fs-extra": "^7.0.1"
      }
    },
    "node_modules/@changesets/read": {
      "version": "0.6.7",
      "resolved": "https://registry.npmjs.org/@changesets/read/-/read-0.6.7.tgz",
      "integrity": "sha512-D1G4AUYGrBEk8vj8MGwf75k9GpN6XL3wg8i42P2jZZwFLXnlr2Pn7r9yuQNbaMCarP7ZQWNJbV6XLeysAIMhTA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/git": "^3.0.4",
        "@changesets/logger": "^0.1.1",
        "@changesets/parse": "^0.4.3",
        "@changesets/types": "^6.1.0",
        "fs-extra": "^7.0.1",
        "p-filter": "^2.1.0",
        "picocolors": "^1.1.0"
      }
    },
    "node_modules/@changesets/should-skip-package": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/@changesets/should-skip-package/-/should-skip-package-0.1.2.tgz",
      "integrity": "sha512-qAK/WrqWLNCP22UDdBTMPH5f41elVDlsNyat180A33dWxuUDyNpg6fPi/FyTZwRriVjg0L8gnjJn2F9XAoF0qw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "@manypkg/get-packages": "^1.1.3"
      }
    },
    "node_modules/@changesets/types": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/@changesets/types/-/types-6.1.0.tgz",
      "integrity": "sha512-rKQcJ+o1nKNgeoYRHKOS07tAMNd3YSN0uHaJOZYjBAgxfV7TUE7JE+z4BzZdQwb5hKaYbayKN5KrYV7ODb2rAA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@changesets/write": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@changesets/write/-/write-0.4.0.tgz",
      "integrity": "sha512-CdTLvIOPiCNuH71pyDu3rA+Q0n65cmAbXnwWH84rKGiFumFzkmHNT8KHTMEchcxN+Kl8I54xGUhJ7l3E7X396Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@changesets/types": "^6.1.0",
        "fs-extra": "^7.0.1",
        "human-id": "^4.1.1",
        "prettier": "^2.7.1"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.4.tgz",
      "integrity": "sha512-cQPwL2mp2nSmHHJlCyoXgHGhbEPMrEEU5xhkcy3Hs/O7nGZqEpZ2sUtLaL9MORLtDfRvVl2/3PAuEkYZH0Ty8Q==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.4.tgz",
      "integrity": "sha512-X9bUgvxiC8CHAGKYufLIHGXPJWnr0OCdR0anD2e21vdvgCI8lIfqFbnoeOz7lBjdrAGUhqLZLcQo6MLhTO2DKQ==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.4.tgz",
      "integrity": "sha512-gdLscB7v75wRfu7QSm/zg6Rx29VLdy9eTr2t44sfTW7CxwAtQghZ4ZnqHk3/ogz7xao0QAgrkradbBzcqFPasw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.4.tgz",
      "integrity": "sha512-PzPFnBNVF292sfpfhiyiXCGSn9HZg5BcAz+ivBuSsl6Rk4ga1oEXAamhOXRFyMcjwr2DVtm40G65N3GLeH1Lvw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.4.tgz",
      "integrity": "sha512-b7xaGIwdJlht8ZFCvMkpDN6uiSmnxxK56N2GDTMYPr2/gzvfdQN8rTfBsvVKmIVY/X7EM+/hJKEIbbHs9oA4tQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.4.tgz",
      "integrity": "sha512-sR+OiKLwd15nmCdqpXMnuJ9W2kpy0KigzqScqHI3Hqwr7IXxBp3Yva+yJwoqh7rE8V77tdoheRYataNKL4QrPw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.4.tgz",
      "integrity": "sha512-jnfpKe+p79tCnm4GVa
... [TRUNCATED]
```

### File: tsconfig.cli.json
```json
{
  "extends": "./tsconfig.json"
}

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022"],
    "outDir": "./dist/cli",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": false,
    "sourceMap": false
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "ui", "dist"]
}

```

### File: vite.config.ts
```ts
import { defineConfig } from 'vite';

export default defineConfig({
  root: 'ui',
  build: {
    outDir: '../dist/ui',
    emptyOutDir: true,
  },
});

```

### File: .changeset\config.json
```json
{
  "$schema": "https://unpkg.com/@changesets/config@3.1.3/schema.json",
  "changelog": ["@changesets/changelog-github", { "repo": "event-catalog/fieldtrip" }],
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}

```

### File: bin\cli.js
```js
#!/usr/bin/env node
require('../dist/cli/cli/index.js');

```

### File: ui\index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FieldTrip</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.ts"></script>
</body>
</html>

```

### File: website\package-lock.json
```json
{
  "name": "@eventcatalog/fieldtrip-website",
  "version": "0.0.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "@eventcatalog/fieldtrip-website",
      "version": "0.0.1",
      "dependencies": {
        "astro": "^5.9.3"
      }
    },
    "node_modules/@astrojs/compiler": {
      "version": "2.13.1",
      "resolved": "https://registry.npmjs.org/@astrojs/compiler/-/compiler-2.13.1.tgz",
      "integrity": "sha512-f3FN83d2G/v32ipNClRKgYv30onQlMZX1vCeZMjPsMMPl1mDpmbl0+N5BYo4S/ofzqJyS5hvwacEo0CCVDn/Qg==",
      "license": "MIT"
    },
    "node_modules/@astrojs/internal-helpers": {
      "version": "0.7.6",
      "resolved": "https://registry.npmjs.org/@astrojs/internal-helpers/-/internal-helpers-0.7.6.tgz",
      "integrity": "sha512-GOle7smBWKfMSP8osUIGOlB5kaHdQLV3foCsf+5Q9Wsuu+C6Fs3Ez/ttXmhjZ1HkSgsogcM1RXSjjOVieHq16Q==",
      "license": "MIT"
    },
    "node_modules/@astrojs/markdown-remark": {
      "version": "6.3.11",
      "resolved": "https://registry.npmjs.org/@astrojs/markdown-remark/-/markdown-remark-6.3.11.tgz",
      "integrity": "sha512-hcaxX/5aC6lQgHeGh1i+aauvSwIT6cfyFjKWvExYSxUhZZBBdvCliOtu06gbQyhbe0pGJNoNmqNlQZ5zYUuIyQ==",
      "license": "MIT",
      "dependencies": {
        "@astrojs/internal-helpers": "0.7.6",
        "@astrojs/prism": "3.3.0",
        "github-slugger": "^2.0.0",
        "hast-util-from-html": "^2.0.3",
        "hast-util-to-text": "^4.0.2",
        "import-meta-resolve": "^4.2.0",
        "js-yaml": "^4.1.1",
        "mdast-util-definitions": "^6.0.0",
        "rehype-raw": "^7.0.0",
        "rehype-stringify": "^10.0.1",
        "remark-gfm": "^4.0.1",
        "remark-parse": "^11.0.0",
        "remark-rehype": "^11.1.2",
        "remark-smartypants": "^3.0.2",
        "shiki": "^3.21.0",
        "smol-toml": "^1.6.0",
        "unified": "^11.0.5",
        "unist-util-remove-position": "^5.0.0",
        "unist-util-visit": "^5.0.0",
        "unist-util-visit-parents": "^6.0.2",
        "vfile": "^6.0.3"
      }
    },
    "node_modules/@astrojs/prism": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/@astrojs/prism/-/prism-3.3.0.tgz",
      "integrity": "sha512-q8VwfU/fDZNoDOf+r7jUnMC2//H2l0TuQ6FkGJL8vD8nw/q5KiL3DS1KKBI3QhI9UQhpJ5dc7AtqfbXWuOgLCQ==",
      "license": "MIT",
      "dependencies": {
        "prismjs": "^1.30.0"
      },
      "engines": {
        "node": "18.20.8 || ^20.3.0 || >=22.0.0"
      }
    },
    "node_modules/@astrojs/telemetry": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/@astrojs/telemetry/-/telemetry-3.3.0.tgz",
      "integrity": "sha512-UFBgfeldP06qu6khs/yY+q1cDAaArM2/7AEIqQ9Cuvf7B1hNLq0xDrZkct+QoIGyjq56y8IaE2I3CTvG99mlhQ==",
      "license": "MIT",
      "dependencies": {
        "ci-info": "^4.2.0",
        "debug": "^4.4.0",
        "dlv": "^1.1.3",
        "dset": "^3.1.4",
        "is-docker": "^3.0.0",
        "is-wsl": "^3.1.0",
        "which-pm-runs": "^1.1.0"
      },
      "engines": {
        "node": "18.20.8 || ^20.3.0 || >=22.0.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.0.tgz",
      "integrity": "sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==",
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@capsizecss/unpack": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@capsizecss/unpack/-/unpack-4.0.0.tgz",
      "integrity": "sha512-VERIM64vtTP1C4mxQ5thVT9fK0apjPFobqybMtA1UdUujWka24ERHbRHFGmpbbhp73MhV+KSsHQH9C6uOTdEQA==",
      "license": "MIT",
      "dependencies": {
        "fontkitten": "^1.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.9.0.tgz",
      "integrity": "sha512-QN75eB0IH2ywSpRpNddCRfQIhmJYBCJ1x5Lb3IscKAL8bMnVAKnRg8dCoXbHzVLLH7P38N2Z3mtulB7W0J0FKw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.4.tgz",
      "integrity": "sha512-cQPwL2mp2nSmHHJlCyoXgHGhbEPMrEEU5xhkcy3Hs/O7nGZqEpZ2sUtLaL9MORLtDfRvVl2/3PAuEkYZH0Ty8Q==",
      "cpu": [
        "ppc64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.4.tgz",
      "integrity": "sha512-X9bUgvxiC8CHAGKYufLIHGXPJWnr0OCdR0anD2e21vdvgCI8lIfqFbnoeOz7lBjdrAGUhqLZLcQo6MLhTO2DKQ==",
      "cpu": [
        "arm"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.4.tgz",
      "integrity": "sha512-gdLscB7v75wRfu7QSm/zg6Rx29VLdy9eTr2t44sfTW7CxwAtQghZ4ZnqHk3/ogz7xao0QAgrkradbBzcqFPasw==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.4.tgz",
      "integrity": "sha512-PzPFnBNVF292sfpfhiyiXCGSn9HZg5BcAz+ivBuSsl6Rk4ga1oEXAamhOXRFyMcjwr2DVtm40G65N3GLeH1Lvw==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.4.tgz",
      "integrity": "sha512-b7xaGIwdJlht8ZFCvMkpDN6uiSmnxxK56N2GDTMYPr2/gzvfdQN8rTfBsvVKmIVY/X7EM+/hJKEIbbHs9oA4tQ==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.4.tgz",
      "integrity": "sha512-sR+OiKLwd15nmCdqpXMnuJ9W2kpy0KigzqScqHI3Hqwr7IXxBp3Yva+yJwoqh7rE8V77tdoheRYataNKL4QrPw==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.4.tgz",
      "integrity": "sha512-jnfpKe+p79tCnm4GVav68A7tUFeKQwQyLgESwEAUzyxk/TJr4QdGog9sqWNcUbr/bZt/O/HXouspuQDd9JxFSw==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.4.tgz",
      "integrity": "sha512-2kb4ceA/CpfUrIcTUl1wrP/9ad9Atrp5J94Lq69w7UwOMolPIGrfLSvAKJp0RTvkPPyn6CIWrNy13kyLikZRZQ==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.4.tgz",
      "integrity": "sha512-aBYgcIxX/wd5n2ys0yESGeYMGF+pv6g0DhZr3G1ZG4jMfruU9Tl1i2Z+Wnj9/KjGz1lTLCcorqE2viePZqj4Eg==",
      "cpu": [
        "arm"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.4.tgz",
      "integrity": "sha512-7nQOttdzVGth1iz57kxg9uCz57dxQLHWxopL6mYuYthohPKEK0vU0C3O21CcBK6KDlkYVcnDXY099HcCDXd9dA==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.4.tgz",
      "integrity": "sha512-oPtixtAIzgvzYcKBQM/qZ3R+9TEUd1aNJQu0HhGyqtx6oS7qTpvjheIWBbes4+qu1bNlo2V4cbkISr8q6gRBFA==",
      "cpu": [
        "ia32"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.4.tgz",
      "integrity": "sha512-8mL/vh8qeCoRcFH2nM8wm5uJP+ZcVYGGayMavi8GmRJjuI3g1v6Z7Ni0JJKAJW+m0EtUuARb6Lmp4hMjzCBWzA==",
      "cpu": [
        "loong64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.4.tgz",
      "integrity": "sha512-1RdrWFFiiLIW7LQq9Q2NES+HiD4NyT8Itj9AUeCl0IVCA459WnPhREKgwrpaIfTOe+/2rdntisegiPWn/r/aAw==",
      "cpu": [
        "mips64el"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.4.tgz",
      "integrity": "sha512-tLCwNG47l3sd9lpfyx9LAGEGItCUeRCWeAx6x2Jmbav65nAwoPXfewtAdtbtit/pJFLUWOhpv0FpS6GQAmPrHA==",
      "cpu": [
        "ppc64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.4.tgz",
      "integrity": "sha512-BnASypppbUWyqjd1KIpU4AUBiIhVr6YlHx/cnPgqEkNoVOhHg+YiSVxM1RLfiy4t9cAulbRGTNCKOcqHrEQLIw==",
      "cpu": [
        "riscv64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.4.tgz",
      "integrity": "sha512-+eUqgb/Z7vxVLezG8bVB9SfBie89gMueS+I0xYh2tJdw3vqA/0ImZJ2ROeWwVJN59ihBeZ7Tu92dF/5dy5FttA==",
      "cpu": [
        "s390x"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.4.tgz",
      "integrity": "sha512-S5qOXrKV8BQEzJPVxAwnryi2+Iq5pB40gTEIT69BQONqR7JH1EPIcQ/Uiv9mCnn05jff9umq/5nqzxlqTOg9NA==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.4.tgz",
      "integrity": "sha512-xHT8X4sb0GS8qTqiwzHqpY00C95DPAq7nAwX35Ie/s+LO9830hrMd3oX0ZMKLvy7vsonee73x0lmcdOVXFzd6Q==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.4.tgz",
      "integrity": "sha512-RugOvOdXfdyi5Tyv40kgQnI0byv66BFgAqjdgtAKqHoZTbTF2QqfQrFwa7cHEORJf6X2ht+l9ABLMP0dnKYsgg==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.4.tgz",
      "integrity": "sha512-2MyL3IAaTX+1/qP0O1SwskwcwCoOI4kV2IBX1xYnDDqthmq5ArrW94qSIKCAuRraMgPOmG0RDTA74mzYNQA9ow==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@e
... [TRUNCATED]
```

### File: website\tsconfig.json
```json
{
  "extends": "astro/tsconfigs/strict"
}

```

### File: src\cli\index.ts
```ts
import { Command } from 'commander';
import { scanDirectory } from '../scanner';
import { parseFile } from '../parsers';
import { createIndex } from '../indexer';
import { createServer } from './server';
import { SchemaProperty } from '../parsers/types';

const program = new Command();

program
  .name('fieldtrip')
  .description('Search across OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files')
  .requiredOption('--dir <path>', 'Directory to scan for schema files')
  .option('--port <number>', 'Port for the web UI', '3200')
  .option('--no-open', 'Do not auto-open browser')
  .action(async (opts) => {
    const dir = opts.dir;
    const port = parseInt(opts.port, 10);
    const shouldOpen = opts.open !== false;

    console.log(`\nScanning ${dir} for schema files...\n`);

    // 1. Scan for files
    const files = await scanDirectory(dir);
    console.log(`Found ${files.length} potential schema files`);

    if (files.length === 0) {
      console.log('No schema files found. Check the --dir path and try again.');
      process.exit(1);
    }

    // 2. Parse all files
    const allProperties: SchemaProperty[] = [];
    let parsedCount = 0;

    for (const file of files) {
      try {
        const properties = await parseFile(file.absolutePath, file.relativePath);
        allProperties.push(...properties);
        if (properties.length > 0) parsedCount++;
      } catch (err: any) {
        console.warn(`Warning: Failed to process ${file.relativePath}: ${err.message}`);
      }
    }

    console.log(`Parsed ${parsedCount} schema files, extracted ${allProperties.length} properties\n`);

    if (allProperties.length === 0) {
      console.log('No schema properties were extracted. The files may not contain recognizable schemas.');
      process.exit(1);
    }

    // 3. Build search index
    const index = createIndex(allProperties);
    console.log('Search index built successfully');

    // 4. Start server
    await createServer(index, allProperties, port, dir);
    console.log(`\nFieldTrip is running at http://localhost:${port}\n`);

    // 5. Open browser
    if (shouldOpen) {
      try {
        const open = (await import('open')).default;
        await open(`http://localhost:${port}`);
      } catch {
        // Silently fail if browser can't be opened
      }
    }
  });

program.parse();

```

### File: src\cli\server.ts
```ts
import express from 'express';
import * as path from 'path';
import * as fs from 'fs';
import MiniSearch from 'minisearch';
import { SchemaProperty, SchemaType } from '../parsers/types';

interface Stats {
  totalProperties: number;
  totalFiles: number;
  schemaTypes: Record<string, number>;
}

export function createServer(
  miniSearch: MiniSearch<SchemaProperty>,
  properties: SchemaProperty[],
  port: number,
  scanDir: string
): Promise<void> {
  const app = express();

  // Compute stats
  const fileSet = new Set(properties.map((p) => p.filePath));
  const schemaTypes: Record<string, number> = {};
  for (const p of properties) {
    schemaTypes[p.schemaType] = (schemaTypes[p.schemaType] || 0) + 1;
  }
  const stats: Stats = {
    totalProperties: properties.length,
    totalFiles: fileSet.size,
    schemaTypes,
  };

  // Serve built UI — find dist/ui which contains the Vite-built assets
  // Priority: dist/ui from project root (works for both tsx dev and compiled)
  const candidates = [
    path.resolve(__dirname, '..', '..', 'ui'),       // from dist/cli/cli/ → dist/ui
    path.resolve(__dirname, '..', '..', 'dist', 'ui'), // from src/cli/ → dist/ui (tsx dev)
    path.join(__dirname, '..', 'ui'),                  // fallback
  ];
  let uiPath = candidates[0];
  for (const candidate of candidates) {
    const indexPath = path.join(candidate, 'assets');
    if (fs.existsSync(indexPath)) {
      uiPath = candidate;
      break;
    }
  }
  app.use(express.static(uiPath));

  // Search API — supports "exact match" with quotes
  app.get('/api/search', (req, res) => {
    const rawQuery = (req.query.q as string || '').trim();
    const schemaType = req.query.schemaType as string | undefined;

    if (!rawQuery) {
      res.json({ results: [], total: 0 });
      return;
    }

    // Check for quoted exact-match phrases
    const exactMatch = /^"(.+)"$/.exec(rawQuery);

    const typeFilter = schemaType
      ? (result: any) => result.schemaType === schemaType
      : undefined;

    if (exactMatch) {
      // Exact match: search without fuzzy/prefix, then post-filter to only
      // keep results where a stored field exactly contains the quoted term
      const term = exactMatch[1];
      const searchOpts: any = {
        prefix: false,
        fuzzy: false,
        boost: { name: 3, description: 1 },
        ...(typeFilter ? { filter: typeFilter } : {}),
      };
      const candidates = miniSearch.search(term, searchOpts);
      const termLower = term.toLowerCase();
      const results = candidates.filter((r: any) =>
        r.name?.toLowerCase() === termLower ||
        r.type?.toLowerCase() === termLower ||
        r.description?.toLowerCase().includes(termLower)
      );
      res.json({ results, total: results.length });
    } else {
      const searchOpts: any = {
        prefix: true,
        fuzzy: 0.2,
        boost: { name: 3, description: 1 },
        ...(typeFilter ? { filter: typeFilter } : {}),
      };
      const results = miniSearch.search(rawQuery, searchOpts);
      res.json({ results, total: results.length });
    }
  });

  // All properties endpoint (for browsing)
  app.get('/api/properties', (req, res) => {
    const schemaType = req.query.schemaType as string | undefined;
    let filtered = properties;
    if (schemaType) {
      filtered = properties.filter((p) => p.schemaType === schemaType);
    }
    res.json({ properties: filtered, total: filtered.length });
  });

  // File content endpoint — returns raw schema file
  app.get('/api/file', (req, res) => {
    const filePath = req.query.path as string;
    if (!filePath) {
      res.status(400).json({ error: 'path is required' });
      return;
    }

    const absolutePath = path.resolve(scanDir, filePath);
    // Prevent directory traversal
    if (!absolutePath.startsWith(path.resolve(scanDir))) {
      res.status(403).json({ error: 'forbidden' });
      return;
    }

    try {
      const content = fs.readFileSync(absolutePath, 'utf-8');
      res.json({ content, filePath });
    } catch {
      res.status(404).json({ error: 'file not found' });
    }
  });

  // Schemas list endpoint — grouped by file
  const schemasMap = new Map<string, { filePath: string; schemaType: string; count: number }>();
  for (const p of properties) {
    const existing = schemasMap.get(p.filePath);
    if (existing) {
      existing.count++;
    } else {
      schemasMap.set(p.filePath, { filePath: p.filePath, schemaType: p.schemaType, count: 0 });
      schemasMap.get(p.filePath)!.count = 1;
    }
  }
  const schemasList = Array.from(schemasMap.values());

  app.get('/api/schemas', (_req, res) => {
    res.json({ schemas: schemasList });
  });

  // Stats API
  app.get('/api/stats', (_req, res) => {
    res.json(stats);
  });

  // SPA fallback
  app.get('*', (_req, res) => {
    res.sendFile(path.join(uiPath, 'index.html'));
  });

  return new Promise((resolve) => {
    app.listen(port, () => {
      resolve();
    });
  });
}

```

### File: ui\src\main.ts
```ts
import './styles/main.css';
import * as monaco from 'monaco-editor';
import * as d3 from 'd3';

import editorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker';
import jsonWorker from 'monaco-editor/esm/vs/language/json/json.worker?worker';

self.MonacoEnvironment = {
  getWorker(_: any, label: string) {
    if (label === 'json') return new jsonWorker();
    return new editorWorker();
  },
};

// ─── Types ───

interface Property {
  id: string;
  name: string;
  type: string;
  description: string;
  schemaPath: string;
  filePath: string;
  schemaType: string;
  parentName: string;
  required: boolean;
  format?: string;
  ref?: string;
  score?: number;
}

interface SchemaInfo { filePath: string; schemaType: string; count: number; }
interface Stats { totalProperties: number; totalFiles: number; schemaTypes: Record<string, number>; }

interface GraphNode extends d3.SimulationNodeDatum {
  id: string;
  label: string;
  nodeType: 'schema' | 'property';
  schemaType?: string;
  filePath?: string;
  propertyName?: string;
  propertyType?: string;
  parentName?: string;
  count?: number;
}

interface GraphLink extends d3.SimulationLinkDatum<GraphNode> {
  linkType: 'belongs-to' | 'shared-name';
}

// ─── Constants ───

const TYPE_COLORS: Record<string, string> = {
  openapi: '#3b82f6', asyncapi: '#8b5cf6', protobuf: '#10b981',
  avro: '#f59e0b', jsonschema: '#6366f1',
};

const TYPE_LABELS: Record<string, string> = {
  openapi: 'OPENAPI', asyncapi: 'ASYNCAPI', protobuf: 'PROTO',
  avro: 'AVRO', jsonschema: 'JSON',
};

const TYPE_BG: Record<string, string> = {
  openapi: 'rgba(59,130,246,0.15)', asyncapi: 'rgba(139,92,246,0.15)',
  protobuf: 'rgba(16,185,129,0.15)', avro: 'rgba(245,158,11,0.15)',
  jsonschema: 'rgba(99,102,241,0.15)',
};

const DATA_TYPE_COLORS: Record<string, string> = {
  string: '#22d3ee', integer: '#a78bfa', int32: '#a78bfa', int64: '#a78bfa',
  number: '#a78bfa', double: '#f472b6', float: '#f472b6',
  boolean: '#fb923c', object: '#94a3b8', array: '#34d399',
};

const FILE_LANGUAGES: Record<string, string> = {
  '.yaml': 'yaml', '.yml': 'yaml', '.json': 'json', '.avsc': 'json', '.proto': 'protobuf',
};

// ─── State ───

let allProperties: Property[] = [];
let filteredProperties: Property[] = [];
let schemas: SchemaInfo[] = [];
let activeSchemaFilters: Set<string> = new Set();
let activeTypeFilter: string | null = null;
let sortField: 'name' | 'schema' | 'type' = 'name';
let sortAsc = true;
let searchQuery = '';
let debounceTimer: ReturnType<typeof setTimeout>;
let activeView: 'table' | 'graph' | 'matrix' = 'table';

// Monaco state
let editorInstance: monaco.editor.IStandaloneCodeEditor | null = null;
let currentDecorations: monaco.editor.IEditorDecorationsCollection | null = null;
let currentFilePath: string | null = null;
let showingDetail = false;

// Graph state
let simulation: d3.Simulation<GraphNode, GraphLink> | null = null;
let graphOnlyShared = true;

// Matrix state
let matrixSortField: 'alpha' | 'count' | 'required' = 'count';
let matrixSortAsc = false;

const app = document.getElementById('app')!;

// ─── Init ───

async function init() {
  const [stats, propsData, schemasData] = await Promise.all([
    fetch('/api/stats').then(r => r.json()) as Promise<Stats>,
    fetch('/api/properties').then(r => r.json()),
    fetch('/api/schemas').then(r => r.json()),
  ]);

  allProperties = propsData.properties;
  filteredProperties = [...allProperties];
  schemas = schemasData.schemas;
  sortProperties();

  app.innerHTML = `
    <nav class="topbar">
      <div class="topbar-left">
        <div class="logo">
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#3b82f6"/><path d="M10 12h12M10 16h8M10 20h10" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>
        </div>
        <div class="topbar-title">
          <h1>FieldTrip</h1>
          <span class="topbar-stats">${stats.totalFiles} SCHEMAS &middot; ${stats.totalProperties} PROPERTIES</span>
        </div>
      </div>
      <div class="view-tabs" id="view-tabs">
        <button class="view-tab active" data-view="table">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
          Table
        </button>
        <button class="view-tab" data-view="matrix">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="4" height="4"/><rect x="10" y="3" width="4" height="4"/><rect x="17" y="3" width="4" height="4"/><rect x="3" y="10" width="4" height="4"/><rect x="10" y="10" width="4" height="4"/><rect x="3" y="17" width="4" height="4"/><rect x="17" y="17" width="4" height="4"/></svg>
          Matrix
        </button>
        <button class="view-tab" data-view="graph">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><line x1="7" y1="6" x2="17" y2="6"/><line x1="6" y1="8" x2="11" y2="16"/><line x1="18" y1="8" x2="13" y2="16"/></svg>
          Graph
        </button>
      </div>
    </nav>

    <div class="main-layout">
      <aside class="sidebar" id="sidebar">
        <div class="sidebar-section">
          <div class="sidebar-heading">SCHEMAS<button class="clear-btn" id="clear-schemas">clear all</button></div>
          <div class="schema-list" id="schema-list"></div>
        </div>
      </aside>

      <main class="content" id="content">
        <div class="content-top">
          <div class="search-bar">
            <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
            <input type="text" id="search-input" placeholder="Search properties, types, descriptions..." autofocus />
          </div>
          <div class="type-filters" id="type-filters"></div>
        </div>

        <div id="table-view">
          <div class="table-toolbar" id="table-toolbar"></div>
          <div class="table-wrapper" id="table-wrapper"></div>
        </div>

        <div id="detail-view" class="detail-view hidden">
          <button class="back-btn" id="back-btn">&larr; Back to results</button>
          <div class="detail-header" id="detail-header"></div>
          <div class="detail-editor" id="editor-container"></div>
        </div>

        <div id="matrix-view" class="matrix-view hidden">
          <div class="matrix-toolbar" id="matrix-toolbar"></div>
          <div class="matrix-container" id="matrix-container"></div>
        </div>

        <div id="graph-view" class="graph-view hidden">
          <div class="graph-toolbar" id="graph-toolbar"></div>
          <div class="graph-container" id="graph-container"></div>
        </div>
      </main>
    </div>
  `;

  // Create Monaco (hidden initially)
  editorInstance = monaco.editor.create(document.getElementById('editor-container')!, {
    value: '', language: 'yaml', theme: 'vs-dark', readOnly: true,
    minimap: { enabled: false }, scrollBeyondLastLine: false, fontSize: 13,
    lineNumbers: 'on', renderLineHighlight: 'none', automaticLayout: true,
    padding: { top: 12 }, scrollbar: { verticalScrollbarSize: 8, horizontalScrollbarSize: 8 },
  });

  renderSidebar();
  renderTable();
  bindEvents();
}

// ─── Sidebar ───

function renderSidebar() {
  document.getElementById('schema-list')!.innerHTML = schemas.map(s => {
    const color = TYPE_COLORS[s.schemaType] || '#666';
    const label = TYPE_LABELS[s.schemaType] || s.schemaType.toUpperCase();
    const active = activeSchemaFilters.has(s.filePath);
    const name = s.filePath.replace(/\.[^.]+$/, '');
    return `
      <div class="schema-item${active ? ' active' : ''}" data-file="${esc(s.filePath)}">
        <span class="schema-badge" style="background:${TYPE_BG[s.schemaType]};color:${color}">${label}</span>
        <div class="schema-info">
          <span class="schema-name">${esc(name)}</span>
          <span class="schema-filepath">${esc(s.filePath)}</span>
        </div>
        <span class="schema-count">${s.count}</span>
      </div>
    `;
  }).join('');

  const allTypes = ['all types', ...Object.keys(TYPE_LABELS)];
  document.getElementById('type-filters')!.innerHTML = allTypes.map(t => {
    const isAll = t === 'all types';
    const active = isAll ? !activeTypeFilter : activeTypeFilter === t;
    const label = isAll ? 'all types' : TYPE_LABELS[t]?.toLowerCase() || t;
    return `<button class="type-chip${active ? ' active' : ''}" data-type="${t}">${label}</button>`;
  }).join('');
}

// ─── View Switching ───

function switchView(view: 'table' | 'graph' | 'matrix') {
  if (activeView === view) return;
  activeView = view;

  if (showingDetail) hideDetail();

  document.getElementById('table-view')!.classList.toggle('hidden', view !== 'table');
  document.getElementById('graph-view')!.classList.toggle('hidden', view !== 'graph');
  document.getElementById('matrix-view')!.classList.toggle('hidden', view !== 'matrix');

  document.querySelectorAll('.view-tab').forEach(tab => {
    tab.classList.toggle('active', (tab as HTMLElement).dataset.view === view);
  });

  if (view === 'graph') {
    renderGraph();
  } else if (view === 'matrix') {
    if (simulation) { simulation.stop(); simulation = null; }
    renderMatrix();
  } else {
    if (simulation) { simulation.stop(); simulation = null; }
    renderTable();
  }
}

// ─── Table ───

function renderTable() {
  const toolbar = document.getElementById('table-toolbar')!;
  const wrapper = document.getElementById('table-wrapper')!;

  toolbar.innerHTML = `
    <span class="table-count"><strong>${filteredProperties.length}</strong> of ${allProperties.length} properties</span>
    <div class="sort-controls">
      <button class="sort-btn${sortField === 'name' ? ' active' : ''}" data-sort="name">name ${sortField === 'name' ? (sortAsc ? '&uarr;' : '&darr;') : ''}</button>
      <button class="sort-btn${sortField === 'schema' ? ' active' : ''}" data-sort="schema">schema ${sortField === 'schema' ? (sortAsc ? '&uarr;' : '&darr;') : ''}</button>
      <button class="sort-btn${sortField === 'type' ? ' active' : ''}" data-sort="type">type ${sortField === 'type' ? (sortAsc ? '&uarr;' : '&darr;') : ''}</button>
    </div>
  `;

  if (filteredProperties.length === 0) {
    wrapper.innerHTML = '<div class="table-empty">No properties match your filters</div>';
    return;
  }

  wrapper.innerHTML = `
    <table class="prop-table">
      <thead><tr><th>PROPERTY</th><th>TYPE</th><th>SCHEMA</th><th>REQUIRED</th><th>DESCRIPTION</th></tr></thead>
      <tbody>${filteredProperties.map(p => renderRow(p)).join('')}</tbody>
    </table>
  `;
}

function renderRow(p: Property): string {
  const typeColor = getDataTypeColor(p.type);
  const schemaColor = TYPE_COLORS[p.schemaType] || '#666';
  const schemaLabel = TYPE_LABELS[p.schemaType] || p.schemaType.toUpperCase();
  const schemaBg = TYPE_BG[p.schemaType] || 'rgba(100,100,100,0.15)';
  const schemaName = p.filePath.replace(/\.[^.]+$/, '');
  const reqText = p.required
    ? '<span class="req-yes"><span class="req-dot"></span>required</span>'
    : '<span class="req-no">optional</span>';

  return `
    <tr class="prop-row" data-id="${esc(p.id)}" data-file="${esc(p.filePath)}">
      <td class="col-property"><span class="prop-name">${esc(p.name)}</span><span class="prop-parent">${esc(p.parentName)}</span></td>
      <td class="col-type"><span class="type-badge" style="color:${typeColor};background:${typeColor}15">${esc(p.type)}</span></td>
      <td class="col-schema"><span class="schema-badge-sm" style="background:${schemaBg};color:${schemaColor}">${schemaLabel}</span><span class="schema-file">${esc(schemaName)}</span></td>
      <td class="col-required">${reqText}</td>
      <td class="col-desc">${p.description ? esc(p.description) : '<span class="no-desc">&mdash;</span>'}</td>
    </tr>
  `;
}

function getDataTypeColor(type: string): string {
  return DATA_TYPE_COLORS[type.replace(/\[\]$/, '').toLowerCase()] || '#94a3b8';
}

// ─── Detail View (Monaco) ───

async function showDetail(property: Property) {
  showingDetail = true;
  document.getElementById('table-view')!.classList.add('hidden');
  document.getElementById('detail-view')!.classList.remove('hidden');

  const color = TYPE_COLORS[property.schemaType] || '#666';
  const label = TYPE_LABELS[property.schemaType] || property.schemaType.toUpperCase();
  const bg = TYPE_BG[property.schemaType] || 'rgba(100,100,100,0.15)';
  const typeColor = getDataTypeColor(property.type);

  document.getElementById('detail-header')!.innerHTML = `
    <div class="detail-title-row">
      <span class="detail-name">${esc(property.name)}</span>
      <span class="type-badge" style="color:${typeColor};background:${typeColor}15">${esc(property.type)}</span>
      ${property.required ? '<span class="req-yes"><span class="req-dot"></span>required</span>' : ''}
      ${property.format ? `<span class="detail-format">${esc(property.format)}</span>` : ''}
      <span class="schema-badge-sm" style="background:${bg};color:${color}">${label}</span>
    </div>
    ${property.description ? `<p class="detail-desc">${esc(property.description)}</p>` : ''}
    <div class="detail-path">${esc(property.filePath)} &middot; ${esc(property.schemaPath)}</div>
  `;

  if (currentFilePath !== property.filePath) {
    try {
      const data = await fetch(`/api/file?path=${encodeURIComponent(property.filePath)}`).then(r => r.json());
      currentFilePath = property.filePath;
      const ext = '.' + property.filePath.split('.').pop()?.toLowerCase();
      const model = editorInstance!.getModel()!;
      monaco.editor.setModelLanguage(model, FILE_LANGUAGES[ext] || 'plaintext');
      model.setValue(data.content);
    } catch {
      editorInstance!.getModel()!.setValue('// Failed to load file');
      currentFilePath = null;
    }
  }

  editorInstance!.layout();
  highlightProperty(property);
}

function hideDetail() {
  showingDetail = false;
  document.getElementById('detail-view')!.classList.add('hidden');
  document.getElementById('table-view')!.classList.remove('hidden');
}

function highlightProperty(property: Property) {
  if (!editorInstance) return;
  const model = editorInstance.getModel();
  if (!model) return;

  const lines = model.getLinesContent();
  const matchLines = findPropertyLines(lines, property);
  if (currentDecorations) currentDecorations.clear();
  if (matchLines.length > 0) {
    currentDecorations = editorInstan
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
