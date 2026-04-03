---
id: changesets-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.653782
---

# KNOWLEDGE EXTRACT: changesets
> **Extracted on:** 2026-03-30 17:31:17
> **Source:** changesets

---

## File: `changesets.md`
```markdown
# 📦 changesets/changesets [🔖 PENDING/APPROVE]
🔗 https://github.com/changesets/changesets


## Meta
- **Stars:** ⭐ 11593 | **Forks:** 🍴 770
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🦋       A way to manage your versioning and changelogs with a focus on monorepos

## README (trích đầu)
```
<p align="center">
  <img src="./assets/images/changesets-banner-light.png" />
</p>

<p align="center">
  A tool to manage versioning and changelogs <br/>
  with a focus on multi-package repositories
</p>
<br/>

[![npm package](https://img.shields.io/npm/v/@changesets/cli?label=%40changesets%2Fcli)](https://npmjs.com/package/@changesets/cli)
[![View changelog](https://img.shields.io/badge/Explore%20Changelog-brightgreen)](./packages/cli/CHANGELOG.md)

The `changesets` workflow is designed to help when people are making changes, all the way through to publishing. It lets contributors declare how their changes should be released, then we automate updating package versions, and changelogs, and publishing new versions of packages based on the provided information.

Changesets has a focus on solving these problems for multi-package repositories, and keeps packages that rely on each other within the multi-package repository up-to-date, as well as making it easy to make changes to groups of packages.

## How do we do that?

A `changeset` is an intent to release a set of packages at particular [semver bump types](https://semver.org/) with a summary of the changes made.

The **@changesets/cli** package allows you to write `changeset` files as you make changes, then combine any number of changesets into a release, that flattens the bump-types into a single release per package, handles internal dependencies in a multi-package-repository, and updates changelogs, as well as release all updated packages from a mono-repository with one command.

## How do I get started?

If you just want to jump in to using changesets, the [Intro to using changesets](./brain/knowledge/docs_legacy/intro-to-using-changesets.md) and [@changesets/cli](../../../README.md) docs are where you should head.

If you want a detailed explanation of the concepts behind changesets, or to understand how you would build on top
of changesets, check out our [detailed-explanation](./brain/knowledge/docs_legacy/detailed-explanation.md).

We also have a [dictionary](./brain/knowledge/docs_legacy/dictionary.md).

## Integrating with CI

While changesets can be an entirely manual process, we recommend integrating it with how your CI works.

To check that PRs contain a changeset, we recommend using [the changeset bot](https://github.com/apps/changeset-bot), or if you want to fail builds on a changesets failure, run `yarn changeset status` in CI.

To make releasing easier, you can use [this changesets github action](https://github.com/changesets/action) to automate creating versioning pull requests, and optionally publishing packages.

## Documentation

- [Intro to using changesets](./brain/knowledge/docs_legacy/intro-to-using-changesets.md)
- [Detailed explanation](./brain/knowledge/docs_legacy/detailed-explanation.md)
- [Common questions](./brain/knowledge/docs_legacy/common-questions.md)
- [Adding a changeset](./brain/knowledge/docs_legacy/adding-a-changeset.md)
- [Automating changesets](./brain/knowledge/docs_legacy/automating-changesets.md)
- [Checking for changesets](./brain/knowledge/docs_legacy/checking-for-changesets.md)
- [Command line options](./brain/knowledge/docs_legacy/command-line-options.md)
- [Config fil
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

