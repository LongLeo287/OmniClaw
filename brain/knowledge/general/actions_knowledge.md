---
id: actions-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:39.618253
---

# KNOWLEDGE EXTRACT: actions
> **Extracted on:** 2026-03-30 17:29:01
> **Source:** actions

---

## File: `dependency-review-action.md`
```markdown
# 📦 actions/dependency-review-action [🔖 PENDING/APPROVE]
🔗 https://github.com/actions/dependency-review-action


## Meta
- **Stars:** ⭐ 799 | **Forks:** 🍴 165
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A GitHub Action for detecting vulnerable dependencies and invalid licenses in your PRs

## README (trích đầu)
```
# dependency-review-action

- [dependency-review-action](#dependency-review-action)
  - [Overview](#overview)
    - [Viewing the results](#viewing-the-results)
  - [Installation](#installation)
    - [Installation (standard)](#installation-standard)
    - [Installation (GitHub Enterprise Server)](#installation-github-enterprise-server)
  - [Configuration](#configuration)
    - [Configuration options](#configuration-options)
    - [Configuration methods](#configuration-methods)
      - [Option 1: Using inline configuration](#option-1-using-inline-configuration)
      - [Option 2: Using an external configuration file](#option-2-using-an-external-configuration-file)
      - [`OTHER` in license strings](#other-in-license-strings)
      - [Further information](#further-information)
  - [Using dependency review action to block a pull request from being merged](#using-dependency-review-action-to-block-a-pull-request-from-being-merged)
  - [Outputs](#outputs)
  - [Getting help](#getting-help)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

The dependency review action scans your pull requests for dependency changes, and will raise an error if any vulnerabilities or invalid licenses are being introduced.
The action is supported by an [API endpoint](https://docs.github.com/en/rest/dependency-graph/dependency-review?apiVersion=2022-11-28) that diffs the dependencies between any two revisions on your default branch.

The action is available for:

- Public repositories
- Private repositories with a [GitHub Advanced Security](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/about-github-advanced-security) license.

### Viewing the results

When the action runs, you can see the results on:

- The **job logs** page.
  1. Go to the **Actions** tab for the repository and select the relevant workflow run.
  1. Then under "Jobs", click **dependency review**.

  <img width="850" alt="GitHub workflow run log showing Dependency Review job output" src="https://user-images.githubusercontent.com/2161/161042286-b22d7dd3-13cb-458d-8744-ce70ed9bf562.png">

- The **job summary** page.
  1. Go to the **Actions** tab for the repository and select the relevant workflow run.
  1. Click **Summary**, then scroll to "dependency-review summary".

     <img width="850" alt="GitHub job summary showing Dependency Review output" src="https://github.com/actions/dependency-review-action/assets/2161/42fbed1d-64a7-42bf-9b05-c416bc67493f">

## Installation

- [Installation (standard)](#installation)
- [Installation (GitHub Enterprise Server)](#installation-github-enterprise-server)

#### Installation (standard)

You can install the action on any public repository, or any organization-owned private repository, provided the organization has a GitHub Advanced Security license.

1. Add a new YAML workflow to your `.github/workflows` folder:

   ```yaml
   name: 'Dependency Review'
   on: [pull_request]

   permissions:
     contents: rea
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `runner-images.md`
```markdown
# 📦 actions/runner-images [🔖 PENDING/APPROVE]
🔗 https://github.com/actions/runner-images


## Meta
- **Stars:** ⭐ 12600 | **Forks:** 🍴 3702
- **Language:** PowerShell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Actions runner images

## README (trích đầu)
```
# GitHub Actions Runner Images

**Table of Contents**

- [About](#about)
- [Available Images](#available-images)
- [Announcements](#announcements)
- [Image Definitions](#image-definitions)
- [Image Releases](#image-releases)
- [Software and Image Support](#software-and-image-support)
- [How to Interact with the Repo](#how-to-interact-with-the-repo)
- [FAQs](#faqs)

## About

This repository contains the source code used to create the VM images for [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners) used for Actions, as well as for [Microsoft-hosted agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops#use-a-microsoft-hosted-agent) used for Azure Pipelines.
To build a VM machine from this repo's source, see the [instructions](brain/knowledge/docs_legacy/create-image-and-azure-resources.md).

## Available Images

| Image | Architecture | YAML Label | Included Software |
| --------------------|--------------|---------------------|------------------|
| Ubuntu 24.04<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fubuntu24.json) | x64 | `ubuntu-latest` or `ubuntu-24.04` | [ubuntu-24.04] |
| Ubuntu 22.04<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fubuntu22.json) | x64 | `ubuntu-22.04` | [ubuntu-22.04] |
| Ubuntu Slim ![preview](https://img.shields.io/badge/preview-0969DA?style=flat&logoColor=white)<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fubuntu-slim.json) | x64 | `ubuntu-slim` | [ubuntu-slim] |
| macOS 26 Arm64<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fmacos-26-arm64.json) | arm64 | `macos-26` or `macos-26-xlarge` | [macOS-26-arm64] |
| macOS 26<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fmacos-26.json) | x64 | `macos-26-intel`, `macos-26-large` | [macOS-26] |
| macOS 15<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fmacos-15.json) | x64 | `macos-latest-large`, `macos-15-large`, or `macos-15-intel` | [macOS-15] |
| macOS 15 Arm64<br>![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fhosted-runners-images-bot%2F79267492faab096d04cdd25ce7014cec%2Fraw%2Fmacos-15-arm64.json) | arm64 | `macos-latest`, `macos-15`, or `macos-15-xlarge` | [macOS-15-arm64] |
| macOS 14<br>![Endpoint Badge](https://img
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `stale.md`
```markdown
# 📦 actions/stale [🔖 PENDING/APPROVE]
🔗 https://github.com/actions/stale


## Meta
- **Stars:** ⭐ 1656 | **Forks:** 🍴 418
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Marks issues and pull requests that have not had recent interaction

## README (trích đầu)
```
# Close Stale Issues and PRs

[![Basic validation](https://github.com/actions/stale/actions/workflows/basic-validation.yml/badge.svg?branch=main)](https://github.com/actions/stale/actions/workflows/basic-validation.yml)
[![e2e tests](https://github.com/actions/stale/actions/workflows/e2e-tests.yml/badge.svg?branch=main)](https://github.com/actions/stale/actions/workflows/e2e-tests.yml)

## Breaking changes in V10

- Upgraded action from node20 to node 24
  > Make sure your runner is on version v2.327.1 or later to ensure compatibility with this release. [Release Notes](https://github.com/actions/runner/releases/tag/v2.327.1)

For more details, see the full release notes on the [release page](https://github.com/actions/stale/releases/tag/v10.0.0)

Warns and then closes issues and PRs that have had no activity for a specified amount of time.

The configuration must be on the default branch and the default values will:

- Add a label "Stale" on issues and pull requests after 60 days of inactivity and comment on them
- Close the stale issues and pull requests after 7 days of inactivity
- If an update/comment occur on stale issues or pull requests, the stale label will be removed and the timer will restart

## Recommended permissions

For the execution of this action, it must be able to fetch all issues and pull requests from your repository.  
In addition, based on the provided configuration, the action could require more permission(s) (e.g.: add label, remove label, comment, close, delete branch, etc.).  
This can be achieved with the following [configuration in the action](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#permissions) if the permissions are restricted:

```yaml
permissions:
  actions: write
  contents: write # only for delete-branch option
  issues: write
  pull-requests: write
```

You can find more information about the required permissions under the corresponding options that you wish to use.

## Statefulness

If the action ends because of [operations-per-run](#operations-per-run) then the next run will start from the first
unprocessed issue skipping the issues processed during the previous run(s). The state is reset when all the issues are
processed. This should be considered for scheduling workflow runs.

The saved state lifetime is the same as the
[actions cache](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy)
configured for the repo.

## All options

### List of input options

Every argument is optional.

| Input                                                               | Description                                                                 | Default               |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------- |
| [repo-token](#repo-token)                                           |
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `upload-artifact.md`
```markdown
# 📦 actions/upload-artifact [🔖 PENDING/APPROVE]
🔗 https://github.com/actions/upload-artifact


## Meta
- **Stars:** ⭐ 3999 | **Forks:** 🍴 1032
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# `@actions/upload-artifact`

> [!WARNING]
> actions/upload-artifact@v3 is scheduled for deprecation on **November 30, 2024**. [Learn more.](https://github.blog/changelog/2024-04-16-deprecation-notice-v3-of-the-artifact-actions/)
> Similarly, v1/v2 are scheduled for deprecation on **June 30, 2024**.
> Please update your workflow to use v4 of the artifact actions.
> This deprecation will not impact any existing versions of GitHub Enterprise Server being used by customers.

Upload [Actions Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts) from your Workflow Runs. Internally powered by [@actions/artifact](https://github.com/actions/toolkit/tree/main/packages/artifact) package.

See also [download-artifact](https://github.com/actions/download-artifact).

- [`@actions/upload-artifact`](#actionsupload-artifact)
  - [v6 - What's new](#v6---whats-new)
  - [v4 - What's new](#v4---whats-new)
    - [Improvements](#improvements)
    - [Breaking Changes](#breaking-changes)
  - [Usage](#usage)
    - [Inputs](#inputs)
    - [Outputs](#outputs)
  - [Examples](#examples)
    - [Upload an Individual File](#upload-an-individual-file)
    - [Upload an Entire Directory](#upload-an-entire-directory)
    - [Upload using a Wildcard Pattern](#upload-using-a-wildcard-pattern)
    - [Upload using Multiple Paths and Exclusions](#upload-using-multiple-paths-and-exclusions)
    - [Altering compressions level (speed v. size)](#altering-compressions-level-speed-v-size)
    - [Customization if no files are found](#customization-if-no-files-are-found)
    - [(Not) Uploading to the same artifact](#not-uploading-to-the-same-artifact)
    - [Environment Variables and Tilde Expansion](#environment-variables-and-tilde-expansion)
    - [Retention Period](#retention-period)
    - [Using Outputs](#using-outputs)
      - [Example output between steps](#example-output-between-steps)
      - [Example output between jobs](#example-output-between-jobs)
    - [Overwriting an Artifact](#overwriting-an-artifact)
  - [Limitations](#limitations)
    - [Number of Artifacts](#number-of-artifacts)
    - [Zip archives](#zip-archives)
    - [Permission Loss](#permission-loss)
  - [Where does the upload go?](#where-does-the-upload-go)


## v6 - What's new

> [!IMPORTANT]
> actions/upload-artifact@v6 now runs on Node.js 24 (`runs.using: node24`) and requires a minimum Actions Runner version of 2.327.1. If you are using self-hosted runners, ensure they are updated before upgrading.

### Node.js 24

This release updates the runtime to Node.js 24. v5 had preliminary support for Node.js 24, however this action was by default still running on Node.js 20. Now this action by default will run on Node.js 24.

## v4 - What's new

> [!IMPORTANT]
> upload-artifact@v4+ is not currently supported on GitHub Enterprise Server (GHES) yet. If you are on GHES, you must use [v3](https://github.com/actions/upload-artifact/releases/tag/v3) (Node 16) or [v3-node20](https://github
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

