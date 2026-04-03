---
id: amannn-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:46.499393
---

# KNOWLEDGE EXTRACT: amannn
> **Extracted on:** 2026-03-30 17:29:08
> **Source:** amannn

---

## File: `action-semantic-pull-request.md`
```markdown
# 📦 amannn/action-semantic-pull-request [🔖 PENDING/APPROVE]
🔗 https://github.com/amannn/action-semantic-pull-request


## Meta
- **Stars:** ⭐ 1303 | **Forks:** 🍴 155
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A GitHub Action that ensures that your PR title matches the Conventional Commits spec

## README (trích đầu)
```
# action-semantic-pull-request

This is a GitHub Action that ensures that your pull request titles match the [Conventional Commits spec](https://www.conventionalcommits.org/). Typically, this is used in combination with a tool like [semantic-release](https://github.com/semantic-release/semantic-release) to automate releases.

Used by: [Electron](https://github.com/electron/electron) · [Vite](https://github.com/vitejs/vite) · [Excalidraw](https://github.com/excalidraw/excalidraw) · [Apache](https://github.com/apache/pulsar) · [Vercel](https://github.com/vercel/ncc) · [Microsoft](https://github.com/microsoft/SynapseML) · [Firebase](https://github.com/firebase/flutterfire) · [AWS](https://github.com/aws-ia/terraform-aws-eks-blueprints) – and [many more](https://github.com/amannn/action-semantic-pull-request/network/dependents).

## Examples

**Valid pull request titles:**

- fix: Correct typo
- feat: Add support for Node.js 18
- refactor!: Drop support for Node.js 12
- feat(ui): Add `Button` component

> Note that since pull request titles only have a single line, you have to use `!` to indicate breaking changes.

See [Conventional Commits](https://www.conventionalcommits.org/) for more examples.

## Installation

1. If your goal is to create squashed commits that will be used for automated releases, you'll want to configure your GitHub repository to [use the squash & merge strategy](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests) and tick the option "Default to PR title for squash merge commits".
2. [Add the action](https://docs.github.com/en/actions/quickstart) with the following configuration:

```yml
name: 'Lint PR'

on:
  pull_request_target:
    types:
      - opened
      - reopened
      - edited
      # - synchronize (if you use required Actions)

jobs:
  main:
    name: Validate PR title
    runs-on: ubuntu-slim
    permissions:
      pull-requests: read
    steps:
      - uses: amannn/action-semantic-pull-request@v6
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

See the [event triggers documentation](#event-triggers) below to learn more about what `pull_request_target` means.

## Configuration

The action works without configuration, however you can provide options for customization.

The following terminology helps to understand the configuration options:

```
feat(ui): Add `Button` component
^    ^    ^
|    |    |__ Subject
|    |_______ Scope
|____________ Type
```

```yml
        with:
          # Configure which types are allowed (newline-delimited).
          # These are regex patterns auto-wrapped in `^ $`.
          # Default: https://github.com/commitizen/conventional-commit-types
          types: |
            fix
            feat
            JIRA-\d+
          # Configure which scopes are allowed (newline-delimited).
          # These are regex patterns auto-wrapped in `^ $`.
       
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

