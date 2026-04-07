---
id: cucumber-js-examples
type: knowledge
owner: OA_Triage
---
# cucumber-js-examples
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Cucumber-JS Examples

There are so many ways you can use [Cucumber-JS](https://github.com/cucumber/cucumber-js)!

For example:

  * [a Node.js app with ESM](./examples/esm-node)
  * a TypeScript Node.js app
    * [using CommonJS format](./examples/typescript-node-commonjs)
    * [using ESM format](./examples/typescript-node-esm)
  * [a Command-line Node.js app](./examples/command-line)
  * [a GitHub Probot app](./examples/probot)

```

### File: renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "local>cucumber/renovate-config"
  ]
}

```

### File: .github\workflows\zizmor-analysis.yaml
```yaml
name: GitHub Actions Security Analysis

on:
  push:
    branches:
      - main
      - 'releases/**'
    paths:
      - '.github/**'
  pull_request:
    paths:
      - '.github/**'

permissions: {}

jobs:
  zizmor:
    name: Run Zizmor
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          persist-credentials: false

      - name: Run Zizmor
        uses: zizmorcore/zizmor-action@71321a20a9ded102f6e9ce5718a2fcec2c4f70d8 # v0.5.2

```

