---
id: changesets
type: knowledge
owner: OA_Triage
---
# changesets
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@changesets/repository",
  "version": "1.0.0",
  "private": true,
  "description": "A tool to help manage the versioning and changelogs for open source packages",
  "scripts": {
    "test": "jest",
    "build": "preconstruct build",
    "watch": "preconstruct watch",
    "postinstall": "preconstruct dev && manypkg check",
    "lint": "yarn eslint . --ext .ts,.tsx,.js",
    "types:check": "tsc",
    "format": "prettier --list-different \"**/*.{js,ts,tsx,md}\"",
    "format:fix": "prettier --write \"**/*.{js,ts,tsx,md}\"",
    "changeset": "packages/cli/bin.js",
    "check-all": "yarn test && yarn types:check && yarn lint && yarn format",
    "version-packages": "changeset version && yarn format:fix",
    "release": "yarn build && changeset publish"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/changesets/changesets.git"
  },
  "packageManager": "yarn@1.22.22",
  "workspaces": [
    "packages/*",
    "scripts/*"
  ],
  "author": "Changesets Contributors",
  "contributors": [
    "Ben Conolly",
    "Mitchell Hamilton",
    "Mateusz Burzyński <mateuszburzynski@gmail.com> (https://github.com/Andarist)"
  ],
  "license": "MIT",
  "devDependencies": {
    "@babel/cli": "^7.27.0",
    "@babel/core": "^7.28.5",
    "@babel/preset-env": "^7.28.5",
    "@babel/preset-typescript": "^7.27.0",
    "@manypkg/cli": "^0.25.1",
    "@preconstruct/cli": "^2.8.12",
    "@types/fs-extra": "^5.1.0",
    "@types/jest": "^24.0.12",
    "@types/jest-in-case": "^1.0.6",
    "@types/lodash": "^4.17.13",
    "@types/node": "^24.10.1",
    "@types/node-fetch": "^2.6.13",
    "@types/prettier": "^2.7.1",
    "@types/semver": "^7.7.1",
    "@typescript-eslint/eslint-plugin": "^5.43.0",
    "@typescript-eslint/parser": "^5.62.0",
    "eslint": "^8.28.0",
    "eslint-config-prettier": "^8.5.0",
    "eslint-config-standard": "^17.1.0",
    "eslint-plugin-import": "^2.31.0",
    "eslint-plugin-n": "^15.5.1",
    "eslint-plugin-promise": "^6.1.1",
    "eslint-plugin-standard": "^5.0.0",
    "jest": "^29.3.1",
    "jest-junit": "^16.0.0",
    "jest-watch-typeahead": "^2.2.2",
    "prettier": "^2.7.1",
    "typescript": "^5.8.3"
  },
  "preconstruct": {
    "packages": [
      "packages/*",
      "scripts/*"
    ],
    "exports": {
      "importConditionDefaultExport": "default"
    },
    "___experimentalFlags_WILL_CHANGE_IN_PATCH": {
      "importsConditions": true
    }
  },
  "prettier": {}
}

```

### File: README.md
```md
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

If you just want to jump in to using changesets, the [Intro to using changesets](./docs/intro-to-using-changesets.md) and [@changesets/cli](./packages/cli/README.md) docs are where you should head.

If you want a detailed explanation of the concepts behind changesets, or to understand how you would build on top
of changesets, check out our [detailed-explanation](./docs/detailed-explanation.md).

We also have a [dictionary](./docs/dictionary.md).

## Integrating with CI

While changesets can be an entirely manual process, we recommend integrating it with how your CI works.

To check that PRs contain a changeset, we recommend using [the changeset bot](https://github.com/apps/changeset-bot), or if you want to fail builds on a changesets failure, run `yarn changeset status` in CI.

To make releasing easier, you can use [this changesets github action](https://github.com/changesets/action) to automate creating versioning pull requests, and optionally publishing packages.

## Documentation

- [Intro to using changesets](./docs/intro-to-using-changesets.md)
- [Detailed explanation](./docs/detailed-explanation.md)
- [Common questions](./docs/common-questions.md)
- [Adding a changeset](./docs/adding-a-changeset.md)
- [Automating changesets](./docs/automating-changesets.md)
- [Checking for changesets](./docs/checking-for-changesets.md)
- [Command line options](./docs/command-line-options.md)
- [Config file options](./docs/config-file-options.md)
- [Decisions](./docs/decisions.md)
- [Dictionary](./docs/dictionary.md)
- [Fixed packages](./docs/fixed-packages.md)
- [Linked packages](./docs/linked-packages.md)
- [Modifying changelog format](./docs/modifying-changelog-format.md)
- [Prereleases](./docs/prereleases.md)
- [Problems publishing in monorepos](./docs/problems-publishing-in-monorepos.md)
- [Snapshot releases](./docs/snapshot-releases.md)
- [Versioning applications and other non-npm packages](./docs/versioning-apps.md)
- [Experimental Options](./docs/experimental-options.md)

## Cool Projects already using Changesets for versioning and changelogs

- [atlaskit](https://atlaskit.atlassian.com)
- [emotion](https://emotion.sh/docs/introduction)
- [keystone](https://keystonejs.com)
- [react-select](https://react-select.com/home)
- [XState](https://xstate.js.org)
- [pnpm](https://pnpm.io)
- [tinyhttp](https://github.com/talentlessguy/tinyhttp)
- [Firebase Javascript SDK](https://github.com/firebase/firebase-js-sdk)
- [Formik](https://github.com/jaredpalmer/formik)
- [MobX](https://github.com/mobxjs/mobx)
- [Nhost](https://github.com/nhost/nhost)
- [verdaccio](https://verdaccio.org)
- [Chakra UI](https://chakra-ui.com)
- [Astro](https://astro.build)
- [Biome](https://biomejs.dev)
- [SvelteKit](https://kit.svelte.dev)
- [Hydrogen](https://hydrogen.shopify.dev)
- [react-pdf](https://github.com/diegomura/react-pdf)
- [GraphQL Code Generator](https://github.com/dotansimha/graphql-code-generator)
- [GraphQL Yoga](https://github.com/dotansimha/graphql-yoga)
- [GraphQL-Mesh](https://github.com/Urigo/graphql-mesh)
- [GraphiQL](https://github.com/graphql/graphiql)
- [wagmi](https://github.com/wagmi-dev/wagmi)
- [refine](https://github.com/pankod/refine)
- [Modern Web](https://modern-web.dev)
- [Atomizer](https://github.com/acss-io/atomizer)
- [Medusa](https://github.com/medusajs/medusa)
- [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts)
- [Block Protocol](https://github.com/blockprotocol/blockprotocol)
- [Remix](https://remix.run/)
- [Clerk](https://github.com/clerk/javascript)
- [Hey API](https://github.com/hey-api/openapi-ts)
- [neverthrow](https://github.com/supermacro/neverthrow)
- [Apollo Client](https://github.com/apollographql/apollo-client)
- [Adobe Spectrum CSS](https://github.com/adobe/spectrum-css)
- [Adobe Spectrum Web Components](https://github.com/adobe/spectrum-web-components)
- [React Email](https://react.email)

<!-- NOTE: we currently only accept new entries with at least 1000 GitHub stars -->

# Thanks/Inspiration

- [bolt](https://github.com/boltpkg/bolt) - Brought us a strong concept of how packages in a mono-repo should be able to interconnect, and provided the initial infrastructure to get inter-package information.
- [Atlassian](https://www.atlassian.com/) - The original idea/sponsor of the changesets code, and where many of the ideas and processes were fermented. It was originally implemented by the team behind [atlaskit](https://atlaskit.atlassian.com).
- [lerna-semantic-release](https://github.com/atlassian/lerna-semantic-release) - put down many of the initial patterns around updating packages within a multi-package-repository, and started us thinking about how to manage dependent packages.
- [Thinkmill](https://www.thinkmill.com.au) - For sponsoring the focused open sourcing of this project, and the version two rearchitecture.

```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works with mono-repos or single package repos to help you version and release your code. You can find the full documentation for it [in our repository](https://github.com/changesets/changesets).

We have a quick list of common questions to get you started engaging with this project in [our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md).

```

### File: assets\README.md
```md
<p align="center">
  <a href="https://github.com/changesets/changesets">
    <img
      alt="The Changesets logo concept, in light."
      src="./images/changesets-banner-light.png"
    />
  </a>
</p>
<p align="center">
  <a href="https://github.com/changesets/changesets">
    <img
      alt="The Changesets logo concept, in dark."
      src="./images/changesets-banner-dark.png"
    />
  </a>
</p>

```

### File: .changeset_DISTILLED.md
```md
---
id: .changeset
type: distilled_knowledge
---
# .changeset

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works with mono-repos or single package repos to help you version and release your code. You can find the full documentation for it [in our repository](https://github.com/changesets/changesets).

We have a quick list of common questions to get you started engaging with this project in [our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md).

```

### File: config.json
```json
{
  "changelog": [
    "@changesets/changelog-github",
    { "repo": "changesets/changesets" }
  ],
  "baseBranch": "main",
  "commit": false,
  "access": "public",
  "___experimentalUnsafeOptions_WILL_CHANGE_IN_PATCH": {
    "updateInternalDependents": "always"
  }
}

```

### File: fix-workspace-dependents-assemble.md
```md
---
"@changesets/assemble-release-plan": patch
---

Fix dependent bump detection for workspace path references. Dependencies declared with specifiers like `workspace:packages/pkg` are now resolved correctly when deciding whether dependents need a release.

```

### File: fix-workspace-path-dependency-graph.md
```md
---
"@changesets/get-dependents-graph": patch
---

Fix dependency graph validation for workspace path references. Valid `workspace:packages/pkg` specifiers are now treated as local dependencies instead of being rejected as invalid ranges.

```

### File: fix-workspace-prefix-semver.md
```md
---
"@changesets/apply-release-plan": patch
---

Fix workspace protocol dependency updates for explicit ranges, aliases, and path references. Valid `workspace:` dependency forms are now preserved and only rewritten when the referenced release leaves the supported range or path.

```

### File: fix-workspace-protocol-cli.md
```md
---
"@changesets/cli": patch
---

Fix several `changeset version` issues with workspace protocol dependencies. Valid explicit `workspace:` ranges and aliases are no longer rewritten unnecessarily, and workspace path references are handled correctly during versioning.

```

### File: flat-zoos-share.md
```md
---
"@changesets/cli": minor
---

Error on unsupported flags for individual CLI commands and print the matching command usage to make mistakes easier to spot.

```

### File: help-on-all-commands.md
```md
---
"@changesets/cli": minor
---

Respond to `--help` on all subcommands. Previously, `--help` was only handled when it was the sole argument; passing it alongside a subcommand (e.g. `changeset version --help`) would silently execute the command instead. Now `--help` always exits early and prints per-command usage when a known subcommand is provided, or the general help text otherwise.

```

### File: stale-registry-republish.md
```md
---
"@changesets/cli": patch
---

Gracefully handle stale `npm info` data leading to duplicate publish attempts.

```

### File: warm-kings-hammer.md
```md
---
"@changesets/cli": patch
---

Improved detection for `published` state of prerelease-only packages without `latest` dist-tag on GitHub Packages registry.

```


```

### File: assets_DISTILLED.md
```md
---
id: assets
type: distilled_knowledge
---
# assets

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://github.com/changesets/changesets">
    <img
      alt="The Changesets logo concept, in light."
      src="./images/changesets-banner-light.png"
    />
  </a>
</p>
<p align="center">
  <a href="https://github.com/changesets/changesets">
    <img
      alt="The Changesets logo concept, in dark."
      src="./images/changesets-banner-dark.png"
    />
  </a>
</p>

```


```

### File: babel.config.js
```js
module.exports = {
  presets: [
    [
      "@babel/preset-env",
      {
        targets: { node: 8 },
      },
    ],
  ],
  overrides: [{ test: "**/*.ts", presets: ["@babel/preset-typescript"] }],
};

```

### File: docs_DISTILLED.md
```md
---
id: docs
type: distilled_knowledge
---
# docs

## SWALLOW ENGINE DISTILLATION

### File: adding-a-changeset.md
```md
# Adding a changeset

Hi! You might be here because a person or a bot has asked you to 'add a changeset' to a project. Let's walk through adding a changeset. But first, what is a changeset?

## What is a changeset?

A changeset is a piece of information about changes made in a branch or commit. It holds three bits of information:

- What we need to release
- What version we are releasing packages at (using a [semver bump type](https://semver.org/))
- A changelog entry for the released packages

## I am in a multi-package repository (a mono-repo)

1. Run the command line script `yarn changeset` or `pnpm changeset` or `npx @changesets/cli`.
2. Select the packages you want to include in the changeset using <kbd>↑</kbd> and <kbd>↓</kbd> to navigate to packages, and <kbd>space</kbd> to select a package. Hit enter when all desired packages are selected.
3. You will be prompted to select a bump type for each selected package. Select an appropriate bump type for the changes made. See [here](https://semver.org/) for information on semver versioning
4. Your final prompt will be to provide a message to go alongside the changeset. This will be written into the changelog when the next release occurs.

After this, a new changeset will be added which is a markdown file with YAML front matter.

```
-| .changeset/
-|-| UNIQUE_ID.md
```

The message you typed can be found in the markdown file. If you want to expand on it, you can write as much markdown as you want, which will all be added to the changelog on publish. If you want to add more packages or change the bump types of any packages, that's also fine.

While not every changeset is going to need a huge amount of detail, a good idea of what should be in a changeset is:

- WHAT the change is
- WHY the change was made
- HOW a consumer should update their code

5. Once you are happy with the changeset, commit the file to your branch.

## I am in a single-package repository

1. Run the command line script `yarn changeset` or `pnpm changeset` or `npx @changesets/cli`.
2. Select an appropriate bump type for the changes made. See [here](https://semver.org/) for information on semver versioning.
3. Your final prompt will be to provide a message to go alongside the changeset. This will be written into the changelog when the next release occurs.

After this, a new changeset will be added which is a markdown file with YAML front matter.

```
-| .changeset/
-|-| UNIQUE_ID.md
```

The message you typed can be found in the markdown file. If you want to expand on it, you can write as much markdown as you want, which will all be added to the changelog on publish. If you want to change the bump type for the changeset, that's also fine.

While not every changeset is going to need a huge amount of detail, a good idea of what should be in a changeset is:

- WHAT the change is
- WHY the change was made
- HOW a consumer should update their code

4. Once you are happy with the changeset, commit the file to your branch.

## Tips on adding changesets

### You can add more than one changeset to a pull request

Changesets are designed to stack, so there's no problem with adding multiple. You might want to add more than one changeset when:

- You want to release multiple packages with different changelog entries
- You have made multiple changes to a package that should each be called out separately

## I want to know more about changesets

[here is a more in-depth explanation](./detailed-explanation.md)

```

### File: automating-changesets.md
```md
# Automating Changesets

While changesets are designed to work with a fully manual process, it also provides tools to help automate these releases. These can be broken into two major decisions:

1. How do I want to ensure pull requests have changesets?
2. How do I run the version and publish commands?

Here we have a quick-start recommended workflow, with more

## Recommended Automation Flow

1. Install our [changeset bot](https://github.com/apps/changeset-bot) into your repository.
2. Add the [github action](https://github.com/changesets/action) to your repository.

## How do I want to ensure pull requests have changesets?

Changesets are committed to files, so a diligent reviewer can always technically tell if a changeset is absent and request one be added. As humans though, a file not being there is easy to miss. We recommend adding some way to detect the presence or absence of changesets on a pull request so you don't have to, as well as highlight it to pull-request makers so you don't have to.

This has two main approaches.

### Non-blocking

In this approach, a pull request may be merged if no changeset is present, and a missing changeset does not create a red build. Our [github changeset bot](https://github.com/apps/changeset-bot) is the best way to prompt for changesets without making them blocking. As a handy extra feature, they give you a link to add your own changeset as a maintainer to smooth over merging pull requests without waiting for the contributor to add a changeset.

### Blocking

Sometimes, you may want to make CI fail if no changeset is present to ensure no PR can be merged without a changeset. To do this:

In your CI process, add a step that runs:

```bash
changeset status --since=main
```

This will exit with exit code 1 if there have been no new changesets since main.

In some cases, you may _want_ to merge a change without doing any releases (such as when you only change tests or build tools). In this case, you can run `changeset --empty`. This will add a special changeset that does not release anything.

## How do I run the version and publish commands?

We have a [github action](https://github.com/changesets/action) that

- creates a `version` PR, then keeps it up to date, recreating it when merged. This PR always has an up-to-date run of `changeset version`
- Optionally allows you to do releases when changes are merged to the base branch.

If you don't want to use this action, the manual workflow we recommend for running the `version` and `publish` commands is:

- A release coordinator (RC) calls to stop any merging to the base branch
- The RC pulls down the base branch, runs `changeset version`, then makes a new PR with the versioning changes
- The versioning changes are merged back into the base branch
- The RC pulls the base branch again and runs `changeset publish`
- The RC runs `git push --follow-tags` to push the release tags back
- The RC unblocks merging to the base branch

This is a lot of steps and is quite finicky (we have to pull from the base branch twice). Feel free to finesse it to your own circumstances.

```

### File: checking-for-changesets.md
```md
# Checking for changesets

Using `@changesets/cli`, there is a `status` command. See the docs for it in the
[@changesets/cli readme](../packages/cli/README.md#status)

We have a [github bot](https://github.com/apps/changeset-bot) and a
[bitbucket addon](https://bitbucket.org/atlassian/atlaskit-mk-2/src/master/build/bitbucket-release-addon/) that
alert users of missing changesets.

If you want to cause a failure in CI on missing changesets (not recommended), you can run `changeset status --since=main`,
which will exit with a status code of 1 if there are no new changesets.

```

### File: command-line-options.md
```md
# Command line options

The command line for changesets is the main way of interacting with it. There are 4 main commands. If you are looking for how we recommend you setup and manage changesets with the commands, check out our [intro to using changesets](./intro-to-using-changesets.md)

- init
- add [--empty] [--open] [--since <ref>] [--message <text>]
- version [--ignore, --snapshot]
- publish [--otp=code, --tag]
- status [--since=master --verbose --output=JSON_FILE.json]
- pre [exit|enter {tag}]
- tag

The most important commands are `add`, which is used by contributors to add information about their changes, `version` - which is responsible for using the changesets generated by `add` to update package versions and changelogs, and then `publish` which publishes changes to npm.

## `init`

```
changeset init
```

This command sets up the `.changeset` folder. It generates a readme and a config file. The config file includes the default options and comments on what these options represent. You should run this command once when you are setting up changesets.

## `add`

```
changeset add
```

or just

```
changeset
```

This is the main command people use to interact with the changesets.

This command will ask you a series of questions, first about what packages you want to release, then what semver bump type for each package, then it will ask for a summary of the entire changeset. The final step will show the changeset it will generate and confirm that you want to add it.

Once confirmed, the changeset will be written as a Markdown file that contains the summary and YAML front matter which stores the packages that will be released and the semver bump types for them.

A changeset that major bumps `@changesets/cli` would look like this:

```
---
"@changesets/cli": major
---

A description of the major changes.
If you want to modify this file after it's generated, that's completely fine or if you want to write changeset files yourself, that's also fine.
```

- `--empty` - allows you to create an empty changeset if no packages are being bumped, usually only required if you have CI that blocks merges without a changeset.

```
changeset --empty
```

A changeset created with the empty flag would look like this:

```
---
---
```

If you set the commit option in the config, the command will add the updated changeset files and then commit them.

- `--open` - opens the created changeset in an external editor
- `--message` (or `-m`) - provides the changeset summary from the command line instead of prompting for it.

- `--since` - uses the provided branch, tag, or git ref (such as `main` or a git commit hash) to detect which packages have changed when populating the list of changed packages in the CLI. This is useful in gitflow workflows where you have multiple target branches and `baseBranch` in the config doesn't cover all use cases. If not provided, the command falls back to the `baseBranch` value in your `.changeset/config.json`.

```
changeset add --since=develop
```

## version

```
changeset version
```

This is one of two commands responsible for releasing packages. The version command takes changesets that have been made and updates versions and dependencies of packages, as well as writing changelogs. It is responsible for all file changes to versions before publishing to npm.

> We recommend making sure changes made from this command are merged back into the base branch before you run publish.

Version has two options, `ignore` and `snapshot`:

```
changeset version --ignore PACKAGE_NAME
```

This command is used to allow you to skip packages from being published. This allows you to run partial publishes of the repository. Using ignore has some safety rails:

1. If the package is mentioned in a changeset that also includes a package that is not ignored, publishing will fail.
2. If the package requires one of its dependencies to be updated as part of a publish.

These restrictions exist to ensure your repository or published code does not end up in a broken state. For additional information on the intricacies of publishing, check out our guide on [problems publishing in monorepos](./problems-publishing-in-monorepos.md).

```
changeset version --snapshot
```

Snapshot is used for a special kind of publishing for testing - it creates temporary versions with a tag, instead of updating versions from the current semver ranges. You should not use this without [reading the documentation on snapshot releases](./snapshot-releases.md)

## publish

```
changeset publish [--otp={token}]
```

This publishes changes to npm, and creates git tags. This works by going into each package, checking if the version it has in its `package.json` is published on npm, and if it is not, running the `npm publish`. If you are using `pnpm` as a package manager, this automatically detects it and uses `pnpm publish` instead.

Because this command assumes that the last commit is the release commit, you should not commit any changes between calling version and publish. These commands are separate to enable you to check if the release changes are accurate.

`--otp={token}` - allows you to provide an npm one-time password if you have auth and writes enabled on npm. The CLI also prompts for the OTP if it's not provided with the --otp option.

`--tag TAGNAME` - for packages that are published, the chosen tag will be used instead of `latest`, allowing you to publish changes intended for testing and validation, not main consumption. This will most likely be used with [snapshot releases](./snapshot-releases.md).

### Git Tags

It is useful to have git tags of a publish, to allow people looking for the code at that time to find them. We generate tags in git during publish, but you will need to push them back up if you want to make them available. We recommend after publish you run:

```
git push --follow-tags
```

## status

```
changeset status [--verbose] [--output={filePath}] [--since={gitTag}]
```

The status command provides information about the changesets that currently exist. If there are no changesets present, it exits with an error status code.

- `--verbose` - use if you want to know the new versions, and get a link to the relevant changeset summary.

- `--output` - allows you to write the JSON object of the status output for consumption by other tools, such as CI.

- `--since` - to only display information about changesets since a specific branch or git tag (such as `main`, or the git hash of latest). While this can be used to add a CI check for changesets, we recommend not doing this. We instead recommend using the [changeset bot](https://github.com/apps/changeset-bot) to detect pull requests missing changesets, as not all pull requests need one if you are on GitHub.

> NOTE: `status` will fail if you are in the middle of running `version` or `publish`. If you want to get changeset status at the time of a version increase and publish, you need to run it immediately before running `version`.

## pre

```
changeset pre [exit|enter {tag}]
```

The pre command enters and exits pre mode. The command does not do any actual versioning, when doing a pre-release, you should run changeset pre enter next(or a different tag, the tag is what is in versions and is the npm dist tag) and then do the normal release process with changeset version and changeset publish. For more information about the pre command, see the prereleases [the prereleases documentation](https://github.com/changesets/changesets/blob/master/docs/prereleases.md).

> NOTE: pre-releases are a very complicated fe
... [TRUNCATED]
```

### File: FUNDING.json
```json
{
  "drips": {
    "ethereum": {
      "ownedBy": "0x334C0464Ec1e9B32835B18465250c95aCa86FaF9"
    }
  }
}

```

### File: jest.config.js
```js
module.exports = {
  clearMocks: true,
  watchPlugins: [
    "jest-watch-typeahead/filename",
    "jest-watch-typeahead/testname",
  ],
};

```

### File: SECURITY.md
```md
# Security policy

## Supported versions

The latest version of the project is currently supported with security updates.

## Reporting a vulnerability

You can report a vulnerability by contacting maintainers via email.

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "commonjs",
    "moduleResolution": "node",
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "strict": true,
    "noEmit": true
  }
}

```

### File: .changeset\config.json
```json
{
  "changelog": [
    "@changesets/changelog-github",
    { "repo": "changesets/changesets" }
  ],
  "baseBranch": "main",
  "commit": false,
  "access": "public",
  "___experimentalUnsafeOptions_WILL_CHANGE_IN_PATCH": {
    "updateInternalDependents": "always"
  }
}

```

### File: .changeset\fix-workspace-dependents-assemble.md
```md
---
"@changesets/assemble-release-plan": patch
---

Fix dependent bump detection for workspace path references. Dependencies declared with specifiers like `workspace:packages/pkg` are now resolved correctly when deciding whether dependents need a release.

```

### File: .changeset\fix-workspace-path-dependency-graph.md
```md
---
"@changesets/get-dependents-graph": patch
---

Fix dependency graph validation for workspace path references. Valid `workspace:packages/pkg` specifiers are now treated as local dependencies instead of being rejected as invalid ranges.

```

### File: .changeset\fix-workspace-prefix-semver.md
```md
---
"@changesets/apply-release-plan": patch
---

Fix workspace protocol dependency updates for explicit ranges, aliases, and path references. Valid `workspace:` dependency forms are now preserved and only rewritten when the referenced release leaves the supported range or path.

```

### File: .changeset\fix-workspace-protocol-cli.md
```md
---
"@changesets/cli": patch
---

Fix several `changeset version` issues with workspace protocol dependencies. Valid explicit `workspace:` ranges and aliases are no longer rewritten unnecessarily, and workspace path references are handled correctly during versioning.

```

### File: .changeset\flat-zoos-share.md
```md
---
"@changesets/cli": minor
---

Error on unsupported flags for individual CLI commands and print the matching command usage to make mistakes easier to spot.

```

### File: .changeset\help-on-all-commands.md
```md
---
"@changesets/cli": minor
---

Respond to `--help` on all subcommands. Previously, `--help` was only handled when it was the sole argument; passing it alongside a subcommand (e.g. `changeset version --help`) would silently execute the command instead. Now `--help` always exits early and prints per-command usage when a known subcommand is provided, or the general help text otherwise.

```

### File: .changeset\stale-registry-republish.md
```md
---
"@changesets/cli": patch
---

Gracefully handle stale `npm info` data leading to duplicate publish attempts.

```

### File: .changeset\warm-kings-hammer.md
```md
---
"@changesets/cli": patch
---

Improved detection for `published` state of prerelease-only packages without `latest` dist-tag on GitHub Packages registry.

```

### File: .github\ISSUE_TEMPLATE.md
```md
## Affected Packages

<!-- Because monorepos, it's super helpful if you tell us which packages are affected, so it's easy to find the change points. Adding a tag pf `pkg:package-name` would be the best 🙏 -->

## Problem

<!-- Write the problem you are encountering here. If it is a bug, or process problem, please provide reproduction steps. If you have a repository we can look at that would be great. 😁 -->

## Proposed solution

<!-- If you have an idea of how to solve it, otherwise that's fine as well. We may edit this description to add details later -->

```

### File: docs\adding-a-changeset.md
```md
# Adding a changeset

Hi! You might be here because a person or a bot has asked you to 'add a changeset' to a project. Let's walk through adding a changeset. But first, what is a changeset?

## What is a changeset?

A changeset is a piece of information about changes made in a branch or commit. It holds three bits of information:

- What we need to release
- What version we are releasing packages at (using a [semver bump type](https://semver.org/))
- A changelog entry for the released packages

## I am in a multi-package repository (a mono-repo)

1. Run the command line script `yarn changeset` or `pnpm changeset` or `npx @changesets/cli`.
2. Select the packages you want to include in the changeset using <kbd>↑</kbd> and <kbd>↓</kbd> to navigate to packages, and <kbd>space</kbd> to select a package. Hit enter when all desired packages are selected.
3. You will be prompted to select a bump type for each selected package. Select an appropriate bump type for the changes made. See [here](https://semver.org/) for information on semver versioning
4. Your final prompt will be to provide a message to go alongside the changeset. This will be written into the changelog when the next release occurs.

After this, a new changeset will be added which is a markdown file with YAML front matter.

```
-| .changeset/
-|-| UNIQUE_ID.md
```

The message you typed can be found in the markdown file. If you want to expand on it, you can write as much markdown as you want, which will all be added to the changelog on publish. If you want to add more packages or change the bump types of any packages, that's also fine.

While not every changeset is going to need a huge amount of detail, a good idea of what should be in a changeset is:

- WHAT the change is
- WHY the change was made
- HOW a consumer should update their code

5. Once you are happy with the changeset, commit the file to your branch.

## I am in a single-package repository

1. Run the command line script `yarn changeset` or `pnpm changeset` or `npx @changesets/cli`.
2. Select an appropriate bump type for the changes made. See [here](https://semver.org/) for information on semver versioning.
3. Your final prompt will be to provide a message to go alongside the changeset. This will be written into the changelog when the next release occurs.

After this, a new changeset will be added which is a markdown file with YAML front matter.

```
-| .changeset/
-|-| UNIQUE_ID.md
```

The message you typed can be found in the markdown file. If you want to expand on it, you can write as much markdown as you want, which will all be added to the changelog on publish. If you want to change the bump type for the changeset, that's also fine.

While not every changeset is going to need a huge amount of detail, a good idea of what should be in a changeset is:

- WHAT the change is
- WHY the change was made
- HOW a consumer should update their code

4. Once you are happy with the changeset, commit the file to your branch.

## Tips on adding changesets

### You can add more than one changeset to a pull request

Changesets are designed to stack, so there's no problem with adding multiple. You might want to add more than one changeset when:

- You want to release multiple packages with different changelog entries
- You have made multiple changes to a package that should each be called out separately

## I want to know more about changesets

[here is a more in-depth explanation](./detailed-explanation.md)

```

### File: docs\automating-changesets.md
```md
# Automating Changesets

While changesets are designed to work with a fully manual process, it also provides tools to help automate these releases. These can be broken into two major decisions:

1. How do I want to ensure pull requests have changesets?
2. How do I run the version and publish commands?

Here we have a quick-start recommended workflow, with more

## Recommended Automation Flow

1. Install our [changeset bot](https://github.com/apps/changeset-bot) into your repository.
2. Add the [github action](https://github.com/changesets/action) to your repository.

## How do I want to ensure pull requests have changesets?

Changesets are committed to files, so a diligent reviewer can always technically tell if a changeset is absent and request one be added. As humans though, a file not being there is easy to miss. We recommend adding some way to detect the presence or absence of changesets on a pull request so you don't have to, as well as highlight it to pull-request makers so you don't have to.

This has two main approaches.

### Non-blocking

In this approach, a pull request may be merged if no changeset is present, and a missing changeset does not create a red build. Our [github changeset bot](https://github.com/apps/changeset-bot) is the best way to prompt for changesets without making them blocking. As a handy extra feature, they give you a link to add your own changeset as a maintainer to smooth over merging pull requests without waiting for the contributor to add a changeset.

### Blocking

Sometimes, you may want to make CI fail if no changeset is present to ensure no PR can be merged without a changeset. To do this:

In your CI process, add a step that runs:

```bash
changeset status --since=main
```

This will exit with exit code 1 if there have been no new changesets since main.

In some cases, you may _want_ to merge a change without doing any releases (such as when you only change tests or build tools). In this case, you can run `changeset --empty`. This will add a special changeset that does not release anything.

## How do I run the version and publish commands?

We have a [github action](https://github.com/changesets/action) that

- creates a `version` PR, then keeps it up to date, recreating it when merged. This PR always has an up-to-date run of `changeset version`
- Optionally allows you to do releases when changes are merged to the base branch.

If you don't want to use this action, the manual workflow we recommend for running the `version` and `publish` commands is:

- A release coordinator (RC) calls to stop any merging to the base branch
- The RC pulls down the base branch, runs `changeset version`, then makes a new PR with the versioning changes
- The versioning changes are merged back into the base branch
- The RC pulls the base branch again and runs `changeset publish`
- The RC runs `git push --follow-tags` to push the release tags back
- The RC unblocks merging to the base branch

This is a lot of steps and is quite finicky (we have to pull from the base branch twice). Feel free to finesse it to your own circumstances.

```

### File: docs\checking-for-changesets.md
```md
# Checking for changesets

Using `@changesets/cli`, there is a `status` command. See the docs for it in the
[@changesets/cli readme](../packages/cli/README.md#status)

We have a [github bot](https://github.com/apps/changeset-bot) and a
[bitbucket addon](https://bitbucket.org/atlassian/atlaskit-mk-2/src/master/build/bitbucket-release-addon/) that
alert users of missing changesets.

If you want to cause a failure in CI on missing changesets (not recommended), you can run `changeset status --since=main`,
which will exit with a status code of 1 if there are no new changesets.

```

### File: docs\command-line-options.md
```md
# Command line options

The command line for changesets is the main way of interacting with it. There are 4 main commands. If you are looking for how we recommend you setup and manage changesets with the commands, check out our [intro to using changesets](./intro-to-using-changesets.md)

- init
- add [--empty] [--open] [--since <ref>] [--message <text>]
- version [--ignore, --snapshot]
- publish [--otp=code, --tag]
- status [--since=master --verbose --output=JSON_FILE.json]
- pre [exit|enter {tag}]
- tag

The most important commands are `add`, which is used by contributors to add information about their changes, `version` - which is responsible for using the changesets generated by `add` to update package versions and changelogs, and then `publish` which publishes changes to npm.

## `init`

```
changeset init
```

This command sets up the `.changeset` folder. It generates a readme and a config file. The config file includes the default options and comments on what these options represent. You should run this command once when you are setting up changesets.

## `add`

```
changeset add
```

or just

```
changeset
```

This is the main command people use to interact with the changesets.

This command will ask you a series of questions, first about what packages you want to release, then what semver bump type for each package, then it will ask for a summary of the entire changeset. The final step will show the changeset it will generate and confirm that you want to add it.

Once confirmed, the changeset will be written as a Markdown file that contains the summary and YAML front matter which stores the packages that will be released and the semver bump types for them.

A changeset that major bumps `@changesets/cli` would look like this:

```
---
"@changesets/cli": major
---

A description of the major changes.
If you want to modify this file after it's generated, that's completely fine or if you want to write changeset files yourself, that's also fine.
```

- `--empty` - allows you to create an empty changeset if no packages are being bumped, usually only required if you have CI that blocks merges without a changeset.

```
changeset --empty
```

A changeset created with the empty flag would look like this:

```
---
---
```

If you set the commit option in the config, the command will add the updated changeset files and then commit them.

- `--open` - opens the created changeset in an external editor
- `--message` (or `-m`) - provides the changeset summary from the command line instead of prompting for it.

- `--since` - uses the provided branch, tag, or git ref (such as `main` or a git commit hash) to detect which packages have changed when populating the list of changed packages in the CLI. This is useful in gitflow workflows where you have multiple target branches and `baseBranch` in the config doesn't cover all use cases. If not provided, the command falls back to the `baseBranch` value in your `.changeset/config.json`.

```
changeset add --since=develop
```

## version

```
changeset version
```

This is one of two commands responsible for releasing packages. The version command takes changesets that have been made and updates versions and dependencies of packages, as well as writing changelogs. It is responsible for all file changes to versions before publishing to npm.

> We recommend making sure changes made from this command are merged back into the base branch before you run publish.

Version has two options, `ignore` and `snapshot`:

```
changeset version --ignore PACKAGE_NAME
```

This command is used to allow you to skip packages from being published. This allows you to run partial publishes of the repository. Using ignore has some safety rails:

1. If the package is mentioned in a changeset that also includes a package that is not ignored, publishing will fail.
2. If the package requires one of its dependencies to be updated as part of a publish.

These restrictions exist to ensure your repository or published code does not end up in a broken state. For additional information on the intricacies of publishing, check out our guide on [problems publishing in monorepos](./problems-publishing-in-monorepos.md).

```
changeset version --snapshot
```

Snapshot is used for a special kind of publishing for testing - it creates temporary versions with a tag, instead of updating versions from the current semver ranges. You should not use this without [reading the documentation on snapshot releases](./snapshot-releases.md)

## publish

```
changeset publish [--otp={token}]
```

This publishes changes to npm, and creates git tags. This works by going into each package, checking if the version it has in its `package.json` is published on npm, and if it is not, running the `npm publish`. If you are using `pnpm` as a package manager, this automatically detects it and uses `pnpm publish` instead.

Because this command assumes that the last commit is the release commit, you should not commit any changes between calling version and publish. These commands are separate to enable you to check if the release changes are accurate.

`--otp={token}` - allows you to provide an npm one-time password if you have auth and writes enabled on npm. The CLI also prompts for the OTP if it's not provided with the --otp option.

`--tag TAGNAME` - for packages that are published, the chosen tag will be used instead of `latest`, allowing you to publish changes intended for testing and validation, not main consumption. This will most likely be used with [snapshot releases](./snapshot-releases.md).

### Git Tags

It is useful to have git tags of a publish, to allow people looking for the code at that time to find them. We generate tags in git during publish, but you will need to push them back up if you want to make them available. We recommend after publish you run:

```
git push --follow-tags
```

## status

```
changeset status [--verbose] [--output={filePath}] [--since={gitTag}]
```

The status command provides information about the changesets that currently exist. If there are no changesets present, it exits with an error status code.

- `--verbose` - use if you want to know the new versions, and get a link to the relevant changeset summary.

- `--output` - allows you to write the JSON object of the status output for consumption by other tools, such as CI.

- `--since` - to only display information about changesets since a specific branch or git tag (such as `main`, or the git hash of latest). While this can be used to add a CI check for changesets, we recommend not doing this. We instead recommend using the [changeset bot](https://github.com/apps/changeset-bot) to detect pull requests missing changesets, as not all pull requests need one if you are on GitHub.

> NOTE: `status` will fail if you are in the middle of running `version` or `publish`. If you want to get changeset status at the time of a version increase and publish, you need to run it immediately before running `version`.

## pre

```
changeset pre [exit|enter {tag}]
```

The pre command enters and exits pre mode. The command does not do any actual versioning, when doing a pre-release, you should run changeset pre enter next(or a different tag, the tag is what is in versions and is the npm dist tag) and then do the normal release process with changeset version and changeset publish. For more information about the pre command, see the prereleases [the prereleases documentation](https://github.com/changesets/changesets/blob/master/docs/prereleases.md).

> NOTE: pre-releases are a very complicated feature. Many of the safety rails that changesets helps you with will be taken off. We recommend that you read both [problems publishing in monorepos](./problems-publishing-in-monorepos.md) and be clear on both exiting and entering pre-releases before using it. You may also prefer using [snapshot releases](./snapshot-releases.md) for a slightly less involved process.

## tag

```
changeset tag
```

The tag command creates git tags for the current version of all packages. The tags created are equivalent to those created by [`changeset publish`](#publish), but the `tag` command does not publish anything to npm.

This is helpful in situations where a different tool, such as `pnpm publish -r`, is used to publish packages instead of changeset. For situations where `changeset publish` is executed, running `changeset tag` is not needed.

The git tags in monorepos are created in the format `pkg-name@version-number` and are based on the current version number of the `package.json` for each package. Note that in single-package repositories, the git tag will include `v` before the version number, for example, `v1.0.0`. It is expected that [`changeset version`](#version) is run before `changeset tag`, so the `package.json` versions are updated before the git tags are created.

```

### File: docs\common-questions.md
```md
# Common Questions

A quick list of common questions you might want answered to understand what changesets is doing, without going into minutiae or workflow.

## Changesets are automatically generated

Changesets are generated by the `yarn changeset` or `npx @changesets/cli` command. As long as you are following a changeset release flow, you shouldn't have any problems.

## Each changeset is its own file

We use random human readable names by default for these files to avoid collisions when generating them, but there's no harm that will come from renaming them.

## Changesets are automatically removed

When `changeset version` or equivalent command is run, all the changeset files are removed. This is so we only ever use a changeset once. This makes the `.changeset` folder a very bad place to store any other information.

## Changesets are markdown files with YAML front matter

The two parts of the file are for different purposes. You should feel free to edit both parts as much as you want.

- The markdown text is a summary of the changes that will be prepended to your changelog when you next run your version command.
- The YAML front matter describes what should be versioned by the version command

## I want to edit the summary or package bump types - is it safe to do that?

Editing the summary or package bump types is completely safe. You can even write changesets without the command if you want.

## Can I manually delete changesets?

You can, but you should be aware this will remove the intent to release communicated by the changeset, and should be done with caution.

```

### File: docs\config-file-options.md
```md
# Configuring Changesets

Changesets has a minimal amount of configuration options. Mostly these are for when you need to change the default workflows. These are stored in `.changeset/config.json`. Our default config is:

```json
{
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "restricted",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}
```

> NOTE: the `linked`, `fixed`, `updateInternalDependencies`, `bumpVersionsWithWorkspaceProtocolOnly`, and `ignore` options are only for behaviour in monorepos.

## `commit` (`boolean`, or module path as a `string`, or a tuple like `[modulePath: string, options: any]`)

This option is for setting if the `changeset add` command and the `changeset version` commands will also add and commit the changed files using git, and how the commit messages should be generated for them.

By default, we do not commit the files, and leave it to the user to commit the files. If it is `true`, we use the default commit message generator (`["@changesets/cli/commit", { "skipCI": "version" }]`). Setting it to a string and options tuple specifies a path from where we will load the commit message generation functions. It expects to be a file that exports one or both of the following:

```
{
  getAddMessage,
  getVersionMessage
}
```

If one of the methods is not present then we will not commit the files changed for that command.

You would specify a custom commit message generator with:

```json
{
  "commit": ["../scripts/commit.js", { "customOption": true }]
}
```

This is similar to how the [changelog generator functions work](#changelog-false-or-a-path).

## `access` (`restricted` | `public`)

This sets how packages are published - if `access: "restricted"`, packages will be published as private, requiring log in to an npm account with access to install. If `access: "public"`, the packages will be made available on the public registry.

By default, npm publishes scoped npm packages as `restricted` - so to ensure you do not accidentally publish code publicly, we default to `restricted`. For most cases you will want to set this to `public`.

This can be overridden in specific packages by setting the `access` in a package's `package.json`.

If you want to prevent a package from being published to npm, set `private: true` in that package's `package.json`

## `baseBranch` (git branch name)

The branch to which changesets will make comparisons to detect what has changed since the last commit of the base branch. This should generally be set to the default branch you merge changes into, e.g. `main` or `master`.

Commands that use this information accept a `--since` option which can be used to override this.

Locally, make sure the base branch exists and is up to date so changesets can make accurate comparisons.

## `ignore` (array of packages)

This option allows you to specify some packages that will not be published, even if they are referenced in changesets. Instead, those changesets will be skipped until they are removed from this array.

> THIS FEATURE IS DESIGNED FOR TEMPORARY USE TO ALLOW CHANGES TO BE MERGED WITHOUT PUBLISHING THEM - If you want to stop a package from being published at all, set `private: true` in its `package.json`.

There are two caveats to this.

1. If the package is mentioned in a changeset that also includes a package that is not ignored, publishing will fail.
2. If the package requires one of its dependencies to be updated as part of a publish.

These restrictions exist to ensure your repository or published code do not end up in a broken state. For a more detailed intricacies of publishing, check out our guide on [problems publishing in monorepos](./problems-publishing-in-monorepos.md).

> NOTE: you can also provide glob expressions to match the packages, according to the [micromatch](https://www.npmjs.com/package/micromatch) format.

## `fixed` (array of arrays of package names)

This option can be used to declare that packages should be version-bumped and published together. As an example, if you have a `@changesets/button` component and a `@changesets/theme` component and you want to make sure that when one gets bumped to `1.1.0`, the other is also bumped to `1.1.0` regardless if it has any change or not. To achieve this you would have the config:

```json
{
  "fixed": [["@changesets/button", "@changesets/theme"]]
}
```

If you want to use this option, you should read the documentation on [fixed packages](./fixed-packages.md) to fully understand the implementation and implications.

## `linked` (array of arrays of package names)

This option can be used to declare that packages should 'share' a version, instead of being versioned completely independently. As an example, if you have a `@changesets/button` component and a `@changesets/theme` component and you want to make sure that when one gets bumped to `2.0.0`, the other is also bumped to `2.0.0`. To achieve this you would have the config:

```json
{
  "linked": [["@changesets/button", "@changesets/theme"]]
}
```

If you want to use this option, you should read the documentation on [linked packages](./linked-packages.md) to fully understand the implementation and implications.

> NOTE: This does not do what some other tools do, which is make sure when any package is published, all other packages are also published with the same version.

## `updateInternalDependencies`

This option sets whether, when a package that is being depended upon changes, whether you should update what version it depends on. To make this more understandable, here is an example:

Say we have two packages, one depending on the other:

```
pkg-a @ version 1.0.0
pkg-b @ version 1.0.0
  depends on pkg-a at range `^1.0.0
```

Say we are publishing a patch of both `pkg-a` and `pkg-b` - this flag is for determining whether we update how `pkg-b` depends on `pkg-a`.

If the option is set to `patch`, we will update the dependency so we will now have:

```
pkg-a @ version 1.0.1
pkg-b @ version 1.0.1
  depends on pkg-a at range `^1.0.1
```

If however the option is set to `minor`, what it depends on will only be updated when there is a minor change, so the state would be:

```
pkg-a @ version 1.0.1
pkg-b @ version 1.0.1
  depends on pkg-a at range `^1.0.0
```

Using `minor` allows consumers to more actively control their own deduplication of packages, and will allow them to install fewer versions if you have many interconnected packages. Using `patch` will mean consumers will more often be using more updated code, but may cause problems with deduplication.

Changesets will always update the dependency if it would leave the old semver range.

> ⚠ Note: this is only applied for packages which are already released in the current release. If A depends on B and we only release B then A won't be bumped.

## `changelog` (false or a path)

This option is for setting how the changelog for packages should be generated. If it is `false`, no changelogs will be generated. Setting it to a string specifies a path from where we will load the changelog generation functions. It expects a file that exports the following:

```
{
  getReleaseLine,
  getDependencyReleaseLine
}
```

As well as the default one, you can use `@changesets/changelog-git`, which adds links to commits into changelogs, or `@changesets/changelog-github`, which requires github authentication, and includes a thankyou message to the person who added the changeset as well as a link to the relevant PR.

You would specify our github changelog generator with:

```json
{
  "changelog": ["@changesets/changelog-github", { "repo": "<org>/<repo>" }]
}
```

For more details on these functions and information on how to write your own see [changelog-functions](./modifying-changelog-format.md)

## `bumpVersionsWithWorkspaceProtocolOnly` (optional boolean)

Default value: `false`

Determines whether Changesets should only bump dependency ranges that use workspace protocol of packages that are part of the workspace.

## `snapshot` (object or undefined)

Default value: `undefined`

### `useCalculatedVersion` (optional boolean)

Default value: `false`

When `changesets version --snapshot` is used, the default behavior is to use `0.0.0` as the base version for the snapshot release.

Setting `useCalculatedVersion: true` will change the default behavior and will use the calculated version, based on the changeset files.

### `prereleaseTemplate` (optional string)

Default value: `undefined` (see note below)

Configures the suffix for the snapshot releases, using a template with placeholders.

**Available placeholders:**

You can use the following placeholders for customizing the snapshot release version:

- `{tag}` - the name of the snapshot tag, as specified in `--snapshot something`
- `{commit}` - the Git commit ID
- `{timestamp}` - Unix timestamp of the time of the release
- `{datetime}` - date and time of the release (14 characters, for example, `20211213000730`)

> Note: if you are using `--snapshot` with empty tag name, you cannot use `{tag}` as placeholder - this will result in error.

**Default behavior**

If you are not specifying `prereleaseTemplate`, the default behavior will fall back to using the following template: `{tag}-{datetime}`, and in cases where the tag is empty (`--snapshot` with no tag name), it will use `{datetime}` only.

## `privatePackages` (object or false)

This option is for setting how private packages should be handled. By default, Changesets will update the changelog for private packages and update their version, but will not create a tag. You can configure this option to change the default behavior.

### `version` (optional boolean)

Default value: `true`

When `version` is set to `true`, Changesets will update the version for private packages. If set to `false`, Changesets will not update the version for private packages.

### `tag` (optional boolean)

Default value: `false`

When `tag` is set to `true`, Changesets will create a tag for private packages. If set to `false`, Changesets will not create a tag for private packages.

### Example

```json
{
  "privatePackages": {
    "version": true,
    "tag": false
  }
}
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
